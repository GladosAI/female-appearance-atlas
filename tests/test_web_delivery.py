import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from web_delivery import browsing_index, write_runtime
from build_provenance import application_info


class WebDeliveryTests(unittest.TestCase):
    def fixture(self):
        entry = {'id': 'T001', 'category': 'hair', 'category_name': '头发', 'name': '高马尾',
                 'en': 'high ponytail', 'dimension': '扎发', 'description': '发束扎在头顶。',
                 'keywords': ['高马尾', 'hair elastic', 'hair elastic'], 'aliases': ['高束发'], 'styles': [],
                 'design_tip': '检查发绳固定位置', 'search_query': 'high ponytail reference',
                 'related_reading': ['R01'], 'authoring_note': '维护记录',
                 'visual': {'board': 'B01', 'image': 'images/board.webp', 'columns': 2, 'rows': 2,
                            'column': 0, 'row': 1, 'label': 'T001',
                            'crop': {'x': 0, 'y': 100, 'width': 100, 'height': 100,
                                     'sheet_width': 200, 'sheet_height': 200}}}
        data = {'entries': [entry], 'categories': [{'id': 'hair', 'name': '头发'}],
                'boards': [{'id': 'B01', 'title': '头发', 'image': 'images/board.webp',
                            'columns': 2, 'rows': 2, 'width': 200, 'height': 200,
                            'items': [{'entry_id': 'T001', 'label': 'T001', 'name': '高马尾'}]}]}
        navigation = {'groups': [{'id': 'hair-domain', 'categories': ['hair']}]}
        return data, navigation

    def test_index_preserves_search_and_moves_complete_detail_to_its_domain(self):
        data, navigation = self.fixture()
        original = copy.deepcopy(data)
        index, chunks, domains = browsing_index(data, navigation)
        entry = index['entries'][0]
        self.assertEqual(entry['keywords'], ['hair elastic'])
        self.assertEqual(entry['aliases'], ['高束发'])
        self.assertNotIn('design_tip', entry)
        self.assertNotIn('authoring_note', entry)
        self.assertEqual(chunks['hair-domain'][0]['design_tip'], '检查发绳固定位置')
        self.assertEqual(chunks['hair-domain'][0]['related_reading'], ['R01'])
        self.assertEqual(domains['hair'], 'hair-domain')
        visual = entry['visual']
        self.assertEqual(visual['crop']['height'], original['entries'][0]['visual']['crop']['height'])
        self.assertNotIn('sheet_width', visual['crop'])
        self.assertEqual(index['boards'][0]['width'], 200)
        self.assertEqual(data, original, 'Online optimization must not mutate original authoring data')

    def test_detail_edits_invalidate_the_chunk_url(self):
        data, navigation = self.fixture()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'assets').mkdir()
            _, before = write_runtime(root, data, navigation)
            data['entries'][0]['design_tip'] = '修订后的固定说明'
            _, after = write_runtime(root, data, navigation)
            self.assertNotEqual(before, after)
            self.assertTrue((root / after['hair-domain']).is_file())

    def test_application_and_package_versions_must_agree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'source').mkdir()
            (root / 'source/app-release.json').write_text(json.dumps({'version': '1.0.0', 'image_release': 'v70.0'}))
            (root / 'source/content-release.json').write_text(json.dumps({'version': '70.0'}))
            (root / 'package.json').write_text(json.dumps({'version': '0.9.0'}))
            with self.assertRaisesRegex(ValueError, 'Application version differs'):
                application_info(root)


if __name__ == '__main__':
    unittest.main()
