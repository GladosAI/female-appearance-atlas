"""Offline translation overlays, coverage and incremental translation tasks.

Canonical catalog identifiers and source text never change through this tool.
No network request, image recognition or paid translation API is involved.
"""
import argparse
from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ('en', 'ja')
FIELDS = ('name', 'description', 'design_tip')
SCHEMA = 'female-appearance-i18n/v1'
TASK_SCHEMA = 'female-appearance-translation-tasks/v1'
HASH = re.compile(r'^[0-9a-f]{64}$')
PLACEHOLDER = re.compile(r'\{([A-Za-z_][A-Za-z0-9_]*)\}')
PROTECTED_FIELDS = {'id', 'stable_id', 'category', 'dimension', 'en', 'visual', 'wearing_visual',
                    'fullbody_visual', 'related_reading', 'styles', 'source_key'}


def source_hash(value):
    """Fingerprint an original field, independently of unrelated catalog edits."""
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False,
                                                         sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def normalize(text):
    return unicodedata.normalize('NFKC', str(text)).casefold()


def load_catalog(root=ROOT):
    return json.loads((Path(root) / 'data/catalog.json').read_text(encoding='utf-8'))


def empty_locale(locale):
    return {'schema': SCHEMA, 'locale': locale, 'messages': {}, 'entries': {},
            'source_hashes': {}, 'review': {}}


def load_locales(root=ROOT):
    """Load maintained overlays. Absent packs stay explicit empty fallbacks."""
    packs = {}
    for locale in LOCALES:
        path = Path(root) / f'source/i18n/{locale}.json'
        packs[locale] = (json.loads(path.read_text(encoding='utf-8'))
                         if path.exists() else empty_locale(locale))
    return packs


def load_message_sources(root=ROOT, packs=None):
    path = Path(root) / 'source/i18n/messages.json'
    if path.exists():
        source = json.loads(path.read_text(encoding='utf-8'))
        if (not isinstance(source, dict) or source.get('schema') != 'female-appearance-i18n-messages/v1' or
                not isinstance(source.get('messages'), list) or
                not all(_has_translation(text) for text in source['messages']) or
                len(source['messages']) != len(set(source['messages']))):
            raise ValueError('invalid canonical source/i18n/messages.json')
        return set(source['messages'])
    packs = load_locales(root) if packs is None else packs
    return set().union(*(set(pack.get('messages', {})) for pack in packs.values()))


def placeholders_match(source, translated):
    return Counter(PLACEHOLDER.findall(source)) == Counter(PLACEHOLDER.findall(translated))


def _has_translation(value):
    return isinstance(value, str) and bool(value.strip())


def validate_locale(pack, data, expected_locale=None):
    """Return schema/source-drift errors; incomplete translation is reportable."""
    errors = []
    if not isinstance(pack, dict):
        return ['locale pack must be an object']
    if pack.get('schema') != SCHEMA:
        errors.append('locale pack has unsupported schema')
    locale = pack.get('locale')
    if locale not in LOCALES or expected_locale and locale != expected_locale:
        errors.append('locale pack has invalid or mismatched locale')
    for key in ['messages', 'entries', 'source_hashes', 'review']:
        if key not in pack and key in {'source_hashes', 'review'}:
            continue
        if not isinstance(pack.get(key), dict):
            errors.append(f'{locale}: {key} must be an object')
    if errors:
        return errors
    entries = {entry['id']: entry for entry in data['entries']}
    for text, translated in pack['messages'].items():
        if not text.strip() or not _has_translation(translated):
            errors.append(f'{locale}: invalid message translation for {text!r}')
        elif not placeholders_match(text, translated):
            errors.append(f'{locale}: message placeholder mismatch for {text!r}')
    message_review=pack.get('message_review',{})
    if not isinstance(message_review,dict):
        errors.append(f'{locale}: message_review must be an object')
    else:
        for text,status in message_review.items():
            if text not in pack['messages'] or status not in {'draft','reviewed'}:
                errors.append(f'{locale}: invalid message review for {text!r}')
    for identifier, fields in pack['entries'].items():
        if identifier not in entries:
            errors.append(f'{locale}: unknown translated entry {identifier}')
            continue
        if not isinstance(fields, dict):
            errors.append(f'{locale}: translated entry {identifier} must be an object')
            continue
        for field, value in fields.items():
            if field in PROTECTED_FIELDS:
                errors.append(f'{locale}: identity/resource field cannot be translated: {identifier}.{field}')
                continue
            if field == 'aliases':
                valid = isinstance(value, list) and all(_has_translation(item) for item in value)
            else:
                valid = _has_translation(value)
            if not valid:
                errors.append(f'{locale}: invalid translation {identifier}.{field}')
                continue
            if isinstance(value, str) and isinstance(entries[identifier].get(field), str) and not placeholders_match(entries[identifier][field], value):
                errors.append(f'{locale}: entry placeholder mismatch {identifier}.{field}')
            recorded = pack.get('source_hashes', {}).get(identifier, {})
            if not isinstance(recorded, dict):
                errors.append(f'{locale}: source hashes for {identifier} must be an object')
                continue
            fingerprint = recorded.get(field)
            if fingerprint is not None:
                if not isinstance(fingerprint, str) or not HASH.fullmatch(fingerprint):
                    errors.append(f'{locale}: invalid source hash {identifier}.{field}')
                elif fingerprint != source_hash(entries[identifier].get(field, '')):
                    errors.append(f'{locale}: stale translation {identifier}.{field}')
    for identifier, fields in pack.get('source_hashes', {}).items():
        if identifier not in entries or not isinstance(fields, dict):
            errors.append(f'{locale}: invalid source hash entry {identifier}')
            continue
        for field, fingerprint in fields.items():
            if not isinstance(fingerprint, str) or not HASH.fullmatch(fingerprint):
                errors.append(f'{locale}: invalid source hash {identifier}.{field}')
    for identifier, fields in pack.get('review', {}).items():
        if identifier not in entries or not isinstance(fields, dict):
            errors.append(f'{locale}: invalid review entry {identifier}')
            continue
        for field, status in fields.items():
            if status not in {'draft', 'reviewed'}:
                errors.append(f'{locale}: invalid review status {identifier}.{field}')
            if status == 'reviewed':
                translated = pack['entries'].get(identifier, {}).get(field)
                recorded = pack.get('source_hashes', {}).get(identifier, {})
                if not translated or not isinstance(recorded, dict) or recorded.get(field) != source_hash(entries[identifier].get(field, '')):
                    errors.append(f'{locale}: reviewed field lacks current source evidence {identifier}.{field}')
    return errors


def validate_locales(root=ROOT, data=None):
    data = load_catalog(root) if data is None else data
    errors = []
    try:
        load_message_sources(root, {})
    except (OSError, ValueError) as error:
        errors.append(str(error))
    for locale in LOCALES:
        path = Path(root) / f'source/i18n/{locale}.json'
        if not path.exists():
            errors.append(f'missing locale pack: source/i18n/{locale}.json')
            continue
        try:
            pack = json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError) as error:
            errors.append(f'{locale}: cannot read locale pack: {error}')
            continue
        errors.extend(validate_locale(pack, data, locale))
    return errors


def locale_report(pack, data, message_sources=None):
    """Coverage is independent from review; source fallback never counts as translated."""
    report = {'locale': pack.get('locale'), 'entries': len(data['entries']), 'fields': {}}
    for field in FIELDS:
        counts = {'translated': 0, 'missing': 0, 'stale': 0, 'untracked': 0,
                  'draft': 0, 'reviewed': 0}
        for entry in data['entries']:
            identifier = entry['id']
            value = pack.get('entries', {}).get(identifier, {}).get(field)
            if not _has_translation(value):
                counts['missing'] += 1
                continue
            counts['translated'] += 1
            recorded = pack.get('source_hashes', {}).get(identifier, {}).get(field)
            if recorded is None:
                counts['untracked'] += 1
            elif recorded != source_hash(entry.get(field, '')):
                counts['stale'] += 1
            if (recorded == source_hash(entry.get(field, '')) and
                    pack.get('review', {}).get(identifier, {}).get(field) == 'reviewed'):
                counts['reviewed'] += 1
            else:
                counts['draft'] += 1
        report['fields'][field] = counts
    sources = set(message_sources or pack.get('messages', {}))
    translated = sum(_has_translation(pack.get('messages', {}).get(text)) for text in sources)
    report['messages'] = {'total': len(sources), 'translated': translated,
                          'missing': len(sources) - translated}
    report['message_review']={'reviewed':sum(pack.get('message_review',{}).get(text)=='reviewed'
        and _has_translation(pack.get('messages',{}).get(text)) for text in sources)}
    report['message_review']['draft']=translated-report['message_review']['reviewed']
    return report


def localized_text(text, pack):
    return pack.get('messages', {}).get(text, text)


def translated_field(entry, field, locale, packs):
    """Return display text and actual language without mutating source records."""
    if locale == 'zh':
        return entry.get(field, ''), 'zh'
    for candidate in (locale, 'en') if locale == 'ja' else ('en',):
        pack = packs.get(candidate, {})
        value = pack.get('entries', {}).get(entry['id'], {}).get(field)
        fingerprint = pack.get('source_hashes', {}).get(entry['id'], {}).get(field)
        if _has_translation(value) and (fingerprint is None or fingerprint == source_hash(entry.get(field, ''))):
            return value, candidate
    if field == 'name' and entry.get('en'):
        return entry['en'], 'en'
    return entry.get(field, ''), 'zh'


def localize_entry(entry, locale, packs):
    """Keep stable routing values and expose original source_* for agent clients."""
    if locale == 'zh':
        return dict(entry)
    result = dict(entry)
    pack = packs.get(locale, {})
    fallback = []
    for field in FIELDS:
        if field not in entry and field != 'name':
            continue
        translated, actual_locale = translated_field(entry, field, locale, packs)
        result['source_' + field] = entry.get(field, '')
        result[field] = translated
        result[field + '_locale'] = actual_locale
        if actual_locale != locale:
            fallback.append(field)
    for field in ['category_name', 'domain_name']:
        if field in entry:
            result['source_' + field] = entry[field]
            result[field] = localized_text(entry[field], pack)
    if 'dimension' in entry:
        result['dimension_label'] = localized_text(entry['dimension'], pack)
    result['locale'] = locale
    result['translation_fallback'] = fallback
    if result.get('detail_url'):
        from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
        url = urlsplit(result['detail_url'])
        query = dict(parse_qsl(url.query))
        query['lang'] = locale
        result['detail_url'] = urlunsplit((url.scheme, url.netloc, url.path, urlencode(query), url.fragment))
    return result


def translation_tasks(pack, data, fields=FIELDS, include_all=False, message_sources=None):
    tasks = []
    for entry in data['entries']:
        identifier = entry['id']
        for field in fields:
            current = pack.get('entries', {}).get(identifier, {}).get(field, '')
            recorded = pack.get('source_hashes', {}).get(identifier, {}).get(field)
            digest = source_hash(entry.get(field, ''))
            reason = 'missing' if not _has_translation(current) else ('untracked' if recorded is None else 'stale' if recorded != digest else 'current')
            if include_all or reason != 'current':
                tasks.append({'kind': 'entry', 'id': identifier, 'field': field,
                              'source': entry.get(field, ''), 'source_hash': digest,
                              'translation': current, 'review': pack.get('review', {}).get(identifier, {}).get(field, 'draft'),
                              'reason': reason})
    for text in sorted(set(message_sources or pack.get('messages', {}))):
        current = pack.get('messages', {}).get(text, '')
        if include_all or not _has_translation(current):
            tasks.append({'kind': 'message', 'source': text, 'source_hash': source_hash(text),
                          'translation': current, 'review': pack.get('message_review',{}).get(text,'draft'),
                          'reason': 'current' if _has_translation(current) else 'missing'})
    return {'schema': TASK_SCHEMA, 'locale': pack['locale'], 'tasks': tasks}


def import_tasks(pack, task_file, data):
    """Validate the entire review file before returning a changed overlay."""
    if (not isinstance(task_file, dict) or task_file.get('schema') != TASK_SCHEMA or
            task_file.get('locale') != pack.get('locale') or not isinstance(task_file.get('tasks'), list)):
        raise ValueError('translation task schema or locale does not match the destination')
    entries = {entry['id']: entry for entry in data['entries']}
    updated = copy.deepcopy(pack)
    seen = set()
    for task in task_file['tasks']:
        if not isinstance(task, dict):
            raise ValueError('translation task must be an object')
        kind = task.get('kind')
        identifier, field = task.get('id'), task.get('field')
        if kind == 'entry':
            if identifier not in entries or field not in FIELDS:
                raise ValueError('translation task references unknown entry or unsupported field')
            original = entries[identifier].get(field, '')
            key = (kind, identifier, field)
        elif kind == 'message' and _has_translation(task.get('source')):
            original = task['source']
            key = (kind, original)
        else:
            raise ValueError('translation task has unsupported kind')
        if key in seen:
            raise ValueError('duplicate translation task')
        seen.add(key)
        if task.get('source_hash') != source_hash(original) or task.get('source') != original:
            raise ValueError(f'translation source changed: {identifier or original}.{field or "message"}')
        value = task.get('translation')
        if value in (None, ''):
            continue
        if not _has_translation(value):
            raise ValueError('translation must be nonempty text')
        status = task.get('review', 'draft')
        if status not in {'draft', 'reviewed'}:
            raise ValueError('translation review must be draft or reviewed')
        if kind == 'entry':
            updated.setdefault('entries', {}).setdefault(identifier, {})[field] = value
            updated.setdefault('source_hashes', {}).setdefault(identifier, {})[field] = source_hash(original)
            updated.setdefault('review', {}).setdefault(identifier, {})[field] = status
        else:
            updated.setdefault('messages', {})[original] = value
            updated.setdefault('message_review',{})[original]=status
    errors = validate_locale(updated, data, pack['locale'])
    if errors:
        raise ValueError('; '.join(errors))
    return updated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help=argparse.SUPPRESS)
    sub = parser.add_subparsers(dest='action', required=True)
    for command in ['check', 'report', 'export', 'import']:
        child = sub.add_parser(command)
        child.add_argument('--locale', choices=LOCALES, required=command in {'export', 'import'})
        if command == 'export':
            child.add_argument('--output', type=Path, required=True)
            child.add_argument('--all', action='store_true', help='Include already-current translations for review')
            child.add_argument('--field', choices=FIELDS, action='append', dest='fields')
        if command == 'import':
            child.add_argument('tasks', type=Path)
            child.add_argument('--output', type=Path, help='Default: maintained source/i18n/<locale>.json')
    args = parser.parse_args()
    data, packs = load_catalog(args.root), load_locales(args.root)
    chosen = [args.locale] if args.locale else list(LOCALES)
    message_sources = load_message_sources(args.root, packs)
    if args.action == 'check':
        errors = []
        for locale in chosen:
            if not (args.root / f'source/i18n/{locale}.json').exists():
                errors.append(f'missing locale pack: source/i18n/{locale}.json')
            errors.extend(validate_locale(packs[locale], data, locale))
        print(json.dumps({'passed': not errors, 'errors': errors}, ensure_ascii=False, indent=2))
        return int(bool(errors))
    if args.action == 'report':
        print(json.dumps([locale_report(packs[locale], data, message_sources) for locale in chosen], ensure_ascii=False, indent=2))
        return 0
    if args.action == 'export':
        value = translation_tasks(packs[args.locale], data, args.fields or FIELDS,
                                  args.all, message_sources)
        output = args.output
    else:
        value = import_tasks(packs[args.locale], json.loads(args.tasks.read_text(encoding='utf-8')), data)
        output = args.output or args.root / f'source/i18n/{args.locale}.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'output': str(output), 'locale': args.locale,
                      **({'tasks': len(value['tasks'])} if args.action == 'export' else {})}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        raise SystemExit(str(error)) from error
