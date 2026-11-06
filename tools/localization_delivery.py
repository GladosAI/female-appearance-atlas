"""Portable, independently cached display-language overlays for the static atlas."""
import hashlib
import json

from i18n_tools import load_locales, load_message_sources, locale_report, validate_locales


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')


def localization_files(root, data):
    errors = validate_locales(root, data)
    if errors:
        raise ValueError('Invalid translations: ' + '; '.join(errors[:20]))
    packs = load_locales(root)
    sources = load_message_sources(root, packs)
    files, manifest, coverage = {}, {}, {}
    entries = {entry['id']: entry for entry in data['entries']}
    for locale, maintained in packs.items():
        # Review bookkeeping stays in source. Repeated design notes are shared by
        # original text; the canonical note arrives with the existing detail chunk.
        messages = dict(maintained.get('messages', {}))
        translated_entries = {}
        for identifier, fields in maintained.get('entries', {}).items():
            entry = entries[identifier]
            translated_entries[identifier] = {key: value for key, value in fields.items()
                                               if key != 'design_tip'}
            if fields.get('design_tip'):
                source=entry['design_tip']
                if source in messages and messages[source]!=fields['design_tip']:
                    translated_entries[identifier]['design_tip']=fields['design_tip']
                else:
                    messages.setdefault(source,fields['design_tip'])
        runtime = {'schema': maintained['schema'], 'locale': locale,
                   'messages': messages, 'entries': translated_entries}
        script = 'globalThis.ATLAS_LOCALES??={};\nglobalThis.ATLAS_LOCALES[' + compact(locale) + ']=' + compact(runtime) + ';\n'
        path = f'data/locales/{locale}.js'
        digest = hashlib.sha256(script.encode('utf-8')).hexdigest()
        files[path] = script
        manifest[locale] = {'path': path, 'sha256': digest, 'bytes': len(script.encode('utf-8'))}
        coverage[locale] = locale_report(maintained, data, sources)
    files['data/locales/manifest.json'] = json.dumps({'schema': 'female-appearance-locale-assets/v1',
        'locales': manifest}, ensure_ascii=False, indent=2) + '\n'
    files['data/locales/coverage.json'] = json.dumps({'schema': 'female-appearance-translation-coverage/v1',
        'locales': coverage}, ensure_ascii=False, indent=2) + '\n'
    return files


def localization_bootstrap(root, data, include_search=True):
    files = localization_files(root, data)
    manifest = json.loads(files['data/locales/manifest.json'])['locales']
    paths = {locale: record['path'] + '?v=' + record['sha256'][:12]
             for locale, record in manifest.items()}
    search = {}
    canonical = {entry['id']: entry for entry in data['entries']}
    for locale, pack in (load_locales(root).items() if include_search else []):
        for identifier, fields in pack['entries'].items():
            # Canonical English names already live in the search index. Only
            # retain overrides, Japanese names and added aliases here.
            translated = fields.get('name')
            if translated and (locale != 'en' or translated != canonical[identifier].get('en')):
                search.setdefault(identifier, {})[locale] = translated
            if fields.get('aliases'):
                search.setdefault(identifier, {}).setdefault('aliases', []).extend(fields['aliases'])
    return ('globalThis.ATLAS_LOCALE_PATHS=' + compact(paths) + ';\n'
            'globalThis.ATLAS_LOCALE_SEARCH=' + compact(search) + ';\n')


def apply_localization(root, html, data, include_search=True):
    runtime = (root / 'tools/templates/i18n.js').read_text(encoding='utf-8')
    styles = (root / 'tools/templates/i18n.css').read_text(encoding='utf-8')
    return html.replace('__I18N_SCRIPT__', localization_bootstrap(root, data, include_search) + runtime).replace('__I18N_STYLES__', styles)


def write_localization(root, data):
    for relative, text in localization_files(root, data).items():
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.read_text(encoding='utf-8') != text:
            target.write_text(text, encoding='utf-8',newline='\n')


def prepare_web_locales(root, output, html, contribution_html):
    """Publish content-hashed language URLs; no image is copied per language."""
    manifest = json.loads((root / 'data/locales/manifest.json').read_text(encoding='utf-8'))
    target = output / 'data/locales'
    target.mkdir(parents=True, exist_ok=True)
    for locale, record in manifest['locales'].items():
        source = root / record['path']
        content = source.read_bytes()
        if hashlib.sha256(content).hexdigest() != record['sha256']:
            raise ValueError('Stale generated locale: ' + locale)
        relative = 'assets/locale-' + locale + '-' + record['sha256'][:12] + '.js'
        (output / relative).write_bytes(content)
        old = record['path'] + '?v=' + record['sha256'][:12]
        html = html.replace(old, relative)
        contribution_html = contribution_html.replace(old, relative)
        record['path']=relative
    (target/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    (target/'coverage.json').write_bytes((root/'data/locales/coverage.json').read_bytes())
    return html, contribution_html
