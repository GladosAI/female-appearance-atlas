import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from i18n_tools import (empty_locale, import_tasks, load_locales, load_message_sources, locale_report,
                        localize_entry, source_hash, translated_field,
                        translation_tasks, validate_locale, validate_locales)
from query_atlas import search
from localization_delivery import (compact, localization_bootstrap, localization_files,
                                   prepare_web_locales, write_localization)


class LocalizationTests(unittest.TestCase):
    def setUp(self):
        self.entry = {'id': 'HA001', 'name': '高马尾', 'en': 'high ponytail',
                      'category': 'hair', 'category_name': '发型', 'dimension': '束发',
                      'domain': 'hair_design', 'domain_name': '头发与发型',
                      'description': '束根较高。', 'design_tip': '观察发束。',
                      'aliases': ['马尾辫'], 'detail_url': 'index.html?section=hair&entry=HA001'}
        self.data = {'entries': [self.entry, {'id': 'HA002', 'name': '低马尾',
                                            'en': 'low ponytail', 'description': '束根较低。',
                                            'design_tip': '保留自然垂落。'}]}
        self.packs = {lang: empty_locale(lang) for lang in ['en', 'ja']}

    def add_translation(self, lang, field, value, status='draft'):
        pack = self.packs[lang]
        pack['entries'].setdefault('HA001', {})[field] = value
        pack['source_hashes'].setdefault('HA001', {})[field] = source_hash(self.entry[field])
        pack['review'].setdefault('HA001', {})[field] = status

    def test_stable_hash_ignores_unrelated_fields_and_detects_source_edit(self):
        self.add_translation('ja', 'description', '高い位置で結ぶ。')
        self.entry['visual'] = {'board': 'new-board'}
        self.assertEqual(validate_locale(self.packs['ja'], self.data), [])
        self.entry['description'] = '束根更高。'
        self.assertTrue(any('stale translation HA001.description' in message
                            for message in validate_locale(self.packs['ja'], self.data)))

    def test_missing_falls_back_without_mutating_canonical_values(self):
        self.packs['ja']['messages'] = {'发型': 'ヘアスタイル', '束发': 'まとめ髪'}
        before = copy.deepcopy(self.entry)
        translated = localize_entry(self.entry, 'ja', self.packs)
        self.assertEqual(self.entry, before)
        self.assertEqual(translated['name'], 'high ponytail')
        self.assertEqual(translated['name_locale'], 'en')
        self.assertEqual(translated['source_name'], '高马尾')
        self.assertEqual(translated['category'], 'hair')
        self.assertEqual(translated['category_name'], 'ヘアスタイル')
        self.assertEqual(translated['dimension'], '束发')
        self.assertEqual(translated['dimension_label'], 'まとめ髪')
        self.assertEqual(translated['description_locale'], 'zh')
        self.assertIn('entry=HA001', translated['detail_url'])
        self.assertIn('lang=ja', translated['detail_url'])
        self.assertEqual(localize_entry(self.entry, 'zh', self.packs), self.entry)

    def test_japanese_uses_current_english_before_original_description(self):
        self.add_translation('en', 'description', 'Hair is tied high.')
        self.add_translation('ja', 'description', '高い位置で結ぶ。')
        self.assertEqual(translated_field(self.entry, 'description', 'ja', self.packs),
                         ('高い位置で結ぶ。', 'ja'))
        self.packs['ja']['source_hashes']['HA001']['description'] = '0' * 64
        self.assertEqual(translated_field(self.entry, 'description', 'ja', self.packs),
                         ('Hair is tied high.', 'en'))

    def test_coverage_does_not_count_fallback_or_draft_as_reviewed(self):
        self.add_translation('ja', 'name', 'ハイポニーテール', 'draft')
        self.add_translation('ja', 'description', '高い位置で結ぶ。', 'reviewed')
        report = locale_report(self.packs['ja'], self.data, ['发型', '束发'])
        self.assertEqual(report['fields']['name']['translated'], 1)
        self.assertEqual(report['fields']['name']['missing'], 1)
        self.assertEqual(report['fields']['name']['reviewed'], 0)
        self.assertEqual(report['fields']['description']['reviewed'], 1)
        self.assertEqual(report['messages']['missing'], 2)

    def test_reviewed_translation_requires_current_source_tracking(self):
        self.packs['ja']['entries'] = {'HA001': {'name': 'ハイポニーテール'}}
        self.packs['ja']['review'] = {'HA001': {'name': 'reviewed'}}
        self.assertTrue(any('reviewed field lacks current source evidence'
                            in error for error in validate_locale(self.packs['ja'], self.data)))
        report = locale_report(self.packs['ja'], self.data)
        self.assertEqual(report['fields']['name']['untracked'], 1)
        self.assertEqual(report['fields']['name']['reviewed'], 0)

    def test_export_only_changed_missing_and_untracked_fields(self):
        self.add_translation('ja', 'name', 'ハイポニーテール')
        tasks = translation_tasks(self.packs['ja'], self.data, ['name'],
                                  message_sources=['发型'])['tasks']
        self.assertEqual([(task['kind'], task.get('id')) for task in tasks],
                         [('entry', 'HA002'), ('message', None)])
        self.entry['name'] = '高位马尾'
        tasks = translation_tasks(self.packs['ja'], self.data, ['name'])['tasks']
        self.assertEqual(tasks[0]['reason'], 'stale')

    def test_import_rejects_drift_duplicate_and_unknown_before_changing_pack(self):
        original = copy.deepcopy(self.packs['ja'])
        task_file = translation_tasks(original, self.data, ['name'])
        task_file['tasks'][0]['translation'] = 'ハイポニーテール'
        for change in ['drift', 'duplicate', 'unknown']:
            with self.subTest(change=change):
                damaged = copy.deepcopy(task_file)
                if change == 'drift':
                    damaged['tasks'][0]['source_hash'] = '0' * 64
                elif change == 'duplicate':
                    damaged['tasks'].append(damaged['tasks'][0])
                else:
                    damaged['tasks'][0]['id'] = 'UNKNOWN'
                with self.assertRaises(ValueError):
                    import_tasks(original, damaged, self.data)
                self.assertEqual(original, self.packs['ja'])

    def test_import_records_hash_and_explicit_review_without_editing_catalog(self):
        before = copy.deepcopy(self.data)
        tasks = translation_tasks(self.packs['ja'], self.data, ['name'])
        tasks['tasks'][0].update(translation='ハイポニーテール', review='reviewed')
        updated = import_tasks(self.packs['ja'], tasks, self.data)
        self.assertEqual(updated['entries']['HA001']['name'], 'ハイポニーテール')
        self.assertEqual(updated['review']['HA001']['name'], 'reviewed')
        self.assertEqual(updated['source_hashes']['HA001']['name'], source_hash('高马尾'))
        self.assertEqual(self.data, before)
        self.assertEqual(self.packs['ja']['entries'], {})

    def test_alias_search_is_cross_language_normalized_and_filterable(self):
        self.packs['ja']['entries'] = {'HA001': {'name': 'ハイポニーテール', 'aliases': ['ポニテ']}}
        self.assertEqual([entry['id'] for entry in search([self.entry], 'ＨＡ００１ ポニテ', locales=self.packs)], ['HA001'])
        self.assertEqual(list(search([self.entry], 'ポニテ', category='other', locales=self.packs)), [])
        self.assertEqual(list(search([self.entry], 'ハイポニーテール missing', locales=self.packs)), [])

    def test_locale_validation_rejects_identity_changes_and_unknown_ids(self):
        self.packs['ja']['entries'] = {'HA001': {'category': 'changed'}, 'UNKNOWN': {'name': '未知'}}
        errors = validate_locale(self.packs['ja'], self.data)
        self.assertTrue(any('identity/resource field' in error for error in errors))
        self.assertTrue(any('unknown translated entry' in error for error in errors))

    def test_named_placeholders_are_preserved_in_messages_and_tasks(self):
        self.packs['ja']['messages'] = {'已选择 {count} 项': '{number} 件を選択'}
        self.assertTrue(any('placeholder mismatch' in error for error in validate_locale(self.packs['ja'], self.data)))
        self.packs['ja']['messages'] = {'已选择 {count} 项': '{count} 件を選択'}
        self.assertEqual(validate_locale(self.packs['ja'], self.data), [])

    def test_canonical_message_manifest_reports_missing_locale_messages(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'source/i18n').mkdir(parents=True)
            (root / 'source/i18n/messages.json').write_text(json.dumps({
                'schema': 'female-appearance-i18n-messages/v1', 'messages': ['发型', '束发']}), encoding='utf-8')
            self.assertEqual(load_message_sources(root, self.packs), {'发型', '束发'})
            report = locale_report(self.packs['ja'], self.data, load_message_sources(root, self.packs))
            self.assertEqual(report['messages'], {'total': 2, 'translated': 0, 'missing': 2})

    def test_interface_review_roundtrip_is_distinct_from_draft_coverage(self):
        self.packs['ja']['messages']={'发型':'ヘアスタイル'}
        self.packs['ja']['message_review']={'发型':'reviewed'}
        tasks=translation_tasks(self.packs['ja'],self.data,fields=[],include_all=True,message_sources={'发型'})
        message=next(task for task in tasks['tasks'] if task['kind']=='message')
        self.assertEqual(message['review'],'reviewed')
        updated=import_tasks(empty_locale('ja'),{**tasks,'tasks':[message]},self.data)
        self.assertEqual(updated['message_review'],{'发型':'reviewed'})
        self.assertEqual(locale_report(updated,self.data,{'发型'})['message_review'],{'reviewed':1,'draft':0})
        updated['message_review']['发型']='automatic-approved'
        self.assertTrue(any('message review' in error for error in validate_locale(updated,self.data)))

    def test_load_missing_pack_is_fallback_but_release_validation_reports_it(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'source/i18n').mkdir(parents=True)
            (root / 'source/i18n/en.json').write_text(json.dumps(self.packs['en']), encoding='utf-8')
            loaded = load_locales(root)
            self.assertEqual(loaded['ja'], empty_locale('ja'))
            self.assertTrue(any('missing locale pack' in message for message in validate_locales(root, self.data)))


class LocalizationDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        (self.root / 'source/i18n').mkdir(parents=True)
        self.tip = '同一段需要复用的设计说明。'
        self.data = {'entries': [
            {'id': 'HA001', 'name': '高马尾', 'en': 'high ponytail', 'description': '高位束发。', 'design_tip': self.tip},
            {'id': 'HA002', 'name': '低马尾', 'en': 'low ponytail', 'description': '低位束发。', 'design_tip': self.tip}]}
        self.packs = {locale: empty_locale(locale) for locale in ['en', 'ja']}
        self.packs['en']['messages'] = {'发型': 'Hairstyle'}
        for entry in self.data['entries']:
            fields = {'name': entry['en'], 'description': 'Description of ' + entry['en'],
                      'design_tip': 'One shared design note.'}
            self.packs['en']['entries'][entry['id']] = fields
            self.packs['en']['source_hashes'][entry['id']] = {field: source_hash(entry[field]) for field in fields}
            self.packs['en']['review'][entry['id']] = {field: 'draft' for field in fields}
        self.write_packs()

    def write_packs(self):
        for locale, pack in self.packs.items():
            (self.root / f'source/i18n/{locale}.json').write_text(json.dumps(pack, ensure_ascii=False), encoding='utf-8')
        (self.root / 'source/i18n/messages.json').write_text(json.dumps({
            'schema': 'female-appearance-i18n-messages/v1', 'messages': ['发型']}), encoding='utf-8')

    def runtime(self, files, locale='en'):
        return json.loads(files[f'data/locales/{locale}.js'].split(']=', 1)[1].rstrip(';\n'))

    def test_shared_notes_are_deduplicated_without_source_or_identity_mutation(self):
        before = copy.deepcopy(self.data)
        originals = {locale: (self.root / f'source/i18n/{locale}.json').read_bytes() for locale in ['en', 'ja']}
        files = localization_files(self.root, self.data)
        runtime = self.runtime(files)
        self.assertEqual(set(runtime['entries']), {'HA001', 'HA002'})
        self.assertEqual(runtime['messages'][self.tip], 'One shared design note.')
        self.assertEqual(files['data/locales/en.js'].count('One shared design note.'), 1)
        self.assertNotIn('source_hashes', runtime)
        self.assertNotIn('review', runtime)
        self.assertEqual(self.data, before)
        for locale, original in originals.items():
            self.assertEqual((self.root / f'source/i18n/{locale}.json').read_bytes(), original)
        bootstrap = localization_bootstrap(self.root, self.data)
        self.assertIn('ATLAS_LOCALE_SEARCH', bootstrap)
        self.assertNotIn('One shared design note.', bootstrap)
        self.assertNotIn('Description of', bootstrap)

    def test_distinct_translations_of_same_note_are_never_silently_overwritten(self):
        self.packs['en']['entries']['HA002']['design_tip'] = 'A deliberately different contextual translation.'
        self.write_packs()
        try:
            runtime = self.runtime(localization_files(self.root, self.data))
        except ValueError as error:
            self.assertIn('conflict', str(error).lower())
            return
        for entry in self.data['entries']:
            actual = runtime['entries'][entry['id']].get('design_tip') or runtime['messages'][entry['design_tip']]
            self.assertEqual(actual, self.packs['en']['entries'][entry['id']]['design_tip'])

    def test_search_bootstrap_reuses_canonical_names_and_is_omitted_from_forms(self):
        self.packs['ja']['entries']['HA001'] = {'name': 'ポニーテール'}
        self.packs['ja']['source_hashes']['HA001'] = {'name': source_hash('高马尾')}
        self.packs['en']['entries']['HA002']['name'] = 'low tied ponytail'
        self.write_packs()
        bootstrap = localization_bootstrap(self.root, self.data)
        self.assertIn('ポニーテール', bootstrap)
        self.assertIn('low tied ponytail', bootstrap)
        self.assertNotIn('high ponytail', bootstrap)
        form = localization_bootstrap(self.root, self.data, include_search=False)
        self.assertNotIn('HA001', form)
        self.assertIn('ATLAS_LOCALE_PATHS', form)

    def test_written_language_file_bytes_match_hash_on_every_platform(self):
        write_localization(self.root, self.data)
        manifest = json.loads((self.root / 'data/locales/manifest.json').read_text(encoding='utf-8'))
        for record in manifest['locales'].values():
            payload = (self.root / record['path']).read_bytes()
            self.assertEqual(record['bytes'], len(payload))
            self.assertEqual(record['sha256'], hashlib.sha256(payload).hexdigest())

    def test_online_manifest_points_to_real_hashed_language_assets(self):
        write_localization(self.root, self.data)
        output = self.root / 'web'
        (output / 'assets').mkdir(parents=True)
        offline_manifest = json.loads((self.root / 'data/locales/manifest.json').read_text(encoding='utf-8'))
        paths = [record['path'] + '?v=' + record['sha256'][:12] for record in offline_manifest['locales'].values()]
        html = '<script>const paths=' + json.dumps(paths) + '</script>'
        web_html, contribution = prepare_web_locales(self.root, output, html, html)
        web_manifest = json.loads((output / 'data/locales/manifest.json').read_text(encoding='utf-8'))
        for record in web_manifest['locales'].values():
            self.assertTrue((output / record['path']).is_file(), record['path'])
            self.assertIn(record['path'], web_html)
            self.assertIn(record['path'], contribution)
            self.assertEqual(hashlib.sha256((output / record['path']).read_bytes()).hexdigest(), record['sha256'])
        self.assertEqual(json.loads((self.root / 'data/locales/manifest.json').read_text(encoding='utf-8')), offline_manifest)

    def test_translation_edit_invalidates_only_that_language_cache(self):
        first = json.loads(localization_files(self.root, self.data)['data/locales/manifest.json'])['locales']
        self.packs['en']['entries']['HA001']['description'] = 'A revised English translation.'
        self.write_packs()
        second = json.loads(localization_files(self.root, self.data)['data/locales/manifest.json'])['locales']
        self.assertNotEqual(first['en']['sha256'], second['en']['sha256'])
        self.assertEqual(first['ja']['sha256'], second['ja']['sha256'])

    def test_embedded_json_preserves_literal_text_and_escapes_closing_script(self):
        source = {'text': '</script><script>alert(1)</script>', 'ja': '髪型'}
        encoded = compact(source)
        self.assertNotIn('</script>', encoded.lower())
        self.assertEqual(json.loads(encoded), source)


if __name__ == '__main__':
    unittest.main()
