import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
sys.path.insert(0, str(ROOT / 'tools/builders'))
from validate_atlas import validate, local_path
from project_data import assign_ids, write_json, source_key
from query_atlas import search
from release_atlas import allowed, runtime_data


class CatalogContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / 'data/catalog.json').read_text(encoding='utf-8'))
        cls.navigation = json.loads((ROOT / 'data/navigation.json').read_text(encoding='utf-8'))

    def test_current_graph(self):
        self.assertEqual(validate(self.data, self.navigation, assets=False), [])

    def test_unknown_reference_is_rejected(self):
        data = copy.deepcopy(self.data)
        data['entries'][0]['related_reading'].append('MISSING-REFERENCE')
        self.assertTrue(any('unknown reading' in error for error in validate(data, self.navigation, assets=False)))

    def test_executable_source_url_is_rejected(self):
        data=copy.deepcopy(self.data)
        data['references'][0]['url']='javascript:alert(1)'
        self.assertTrue(any('invalid source URL' in error for error in validate(data,self.navigation,assets=False)))

    def test_crop_outside_image_is_rejected(self):
        data = copy.deepcopy(self.data)
        entry = next(entry for entry in data['entries'] if entry['visual'].get('crop'))
        entry['visual']['crop']['x'] = entry['visual']['crop']['sheet_width']
        self.assertTrue(any('crop out of bounds' in error for error in validate(data, self.navigation, assets=False)))

    def test_incomplete_storyboard_is_rejected(self):
        data = copy.deepcopy(self.data)
        entry = data['entries'][0]
        entry.update(sequence_reference=True, sequence_labels=['开始', '结束'], sequence_order='left-to-right')
        self.assertTrue(any('three stage labels' in error for error in validate(data, self.navigation, assets=False)))

    def test_duplicate_and_misclassified_entries_are_rejected(self):
        data = copy.deepcopy(self.data)
        data['entries'][1]['id'] = data['entries'][0]['id']
        data['entries'][2]['category'] = 'nonexistent'
        errors = validate(data, self.navigation, assets=False)
        self.assertTrue(any('duplicate identifiers' in error for error in errors))
        self.assertTrue(any('unknown category' in error for error in errors))

    def test_portable_paths(self):
        for path in ['../escape.png', '/escape.png', 'C:/private/photo.png', 'images\\test.png']:
            with self.subTest(path=path), self.assertRaises(ValueError):
                local_path(ROOT, path)

    def test_reorder_insert_rename_never_reassigns_published_ids(self):
        old = [{'category': 'hair', 'name': 'first', 'en': 'first'}, {'category': 'hair', 'name': 'second', 'en': 'second'}]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            write_json(root / 'source/id-registry.json', {'entries': [{'id': 'HA001', 'source_key': source_key(old[0])}, {'id': 'HA002', 'source_key': source_key(old[1])}]})
            entries = [old[1], {'category': 'hair', 'name': 'new', 'en': 'new'}, old[0]]
            registry = assign_ids(root, entries, [{'id': 'hair'}], ['HA'])
            self.assertEqual([entry['id'] for entry in entries], ['HA002', 'HA003', 'HA001'])
            write_json(root / 'source/id-registry.json', registry)
            renamed = [{'category': 'hair', 'name': 'renamed', 'en': 'renamed', 'stable_id': 'HA001'}]
            updated = assign_ids(root, renamed, [{'id': 'hair'}], ['HA'])
            self.assertEqual(renamed[0]['id'], 'HA001')
            self.assertIn('HA002', {record['id'] for record in updated['entries']})

    def test_query_combines_aliases_and_filters(self):
        records = [{'id': 'A001', 'name': '缎带', 'en': 'ribbon', 'aliases': ['发绳'], 'category': 'hair', 'domain': 'hair_design'},
                   {'id': 'A002', 'name': '缎带鞋', 'en': 'ribbon shoes', 'aliases': [], 'category': 'shoes'}]
        self.assertEqual([r['id'] for r in search(records, 'ribbon 发绳', 'hair')], ['A001'])
        self.assertEqual(list(search(records, 'missing')), [])

    def test_system_examples_reject_duplicate_and_unknown_references(self):
        data=copy.deepcopy(self.data)
        card=next(c for c in data['combinations'] if c.get('character_example'))
        card['entry_ids'][1]=card['entry_ids'][0]
        errors=validate(data,self.navigation,assets=False)
        self.assertTrue(any('small unique reference set' in error for error in errors))
        card['entry_ids'][1]='MISSING-EXAMPLE-ENTRY'
        self.assertTrue(any('unknown saved entry' in error for error in validate(data,self.navigation,assets=False)))

    def test_system_example_coverage_matches_references(self):
        entries={entry['id']:entry for entry in self.data['entries']}
        cards=[card for card in self.data['combinations'] if not card.get('archived')]
        expected={cid:[card['id'] for card in cards if any(entries[eid]['category']==cid for eid in card['entry_ids'])]
                  for cid in (c['id'] for c in self.data['categories'])}
        self.assertEqual(self.data['example_coverage']['category_examples'],expected)
        self.assertEqual(len(cards),self.data['meta']['combination_count'])

    def test_runtime_keeps_board_mapping_and_removes_authoring_recipes(self):
        runtime = runtime_data(self.data)
        self.assertIn('items', runtime['boards'][0])
        self.assertNotIn('prompt', runtime['boards'][-1])
        self.assertEqual(runtime['entries'][0]['visual'], self.data['entries'][0]['visual'])
        reference = next(entry for entry in runtime['entries'] if entry.get('fixed_conditions'))
        self.assertTrue(reference['changed_condition'])

    def test_package_excludes_personal_and_build_files(self):
        for path in ['.work/private.json', 'dist/site/index.html', 'node_modules/secret.js', '.git/config']:
            self.assertFalse(allowed(ROOT / path, ROOT))
        self.assertTrue(allowed(ROOT / 'package-lock.json', ROOT))


if __name__ == '__main__':
    unittest.main()
