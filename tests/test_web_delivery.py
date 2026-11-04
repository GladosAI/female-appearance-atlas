import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from web_delivery import browsing_index, write_runtime
from build_provenance import application_info, resource_inventory_digest


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

    def test_scene_prompt_group_is_available_before_loading_details(self):
        data, navigation = self.fixture()
        data['entries'][0]['scene_reference'] = True
        index, chunks, _ = browsing_index(data, navigation)
        self.assertTrue(index['entries'][0]['scene_reference'])
        self.assertNotIn('design_tip', index['entries'][0])
        self.assertNotIn('scene_reference', chunks['hair-domain'][0])
        self.assertEqual(chunks['hair-domain'][0]['design_tip'], '检查发绳固定位置')

    def test_application_and_package_versions_must_agree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'source').mkdir()
            (root / 'source/app-release.json').write_text(json.dumps({'version': '1.0.0', 'image_release': 'v70.0'}))
            (root / 'source/content-release.json').write_text(json.dumps({'version': '70.0'}))
            (root / 'package.json').write_text(json.dumps({'version': '0.9.0'}))
            with self.assertRaisesRegex(ValueError, 'Application version differs'):
                application_info(root)

    def test_metadata_revision_reuses_resources_only_with_matching_inventory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'source').mkdir()
            (root/'data').mkdir()
            def write(name, value):
                (root/name).write_text(json.dumps(value), encoding='utf-8')
            write('source/app-release.json', {'version':'1.0.0','image_release':'v70.0'})
            write('source/content-release.json', {'version':'70.1'})
            write('package.json', {'version':'1.0.0'})
            data, _ = self.fixture()
            write('data/catalog.json', data)
            rights = {'assets':[{'path':'images/board.webp','sha256':'a'*64}]}
            write('source/rights-review.json', rights)
            exports = {'images/board.webp':{'file':'images/export-data/board.js','mime':'image/png','source_sha256':'a'*64}}
            write('data/image-export-index.json', exports)
            resources = {'content_version':'70.0','compatible_content_versions':['70.1'],
                         'assets':[{'file':name,'bytes':10,'sha256':'b'*64,
                                    'url':'https://github.com/GladosAI/female-appearance-atlas/releases/download/v70.0/'+name}
                                   for name in ['female-appearance-atlas-images.zip','female-appearance-atlas-offline-copy.zip']]}
            write('source/resource-packs.json', {'releases':{'v70.0':resources}})
            with self.assertRaisesRegex(ValueError, 'not proven compatible'):
                application_info(root)
            resources['inventory_sha256'] = resource_inventory_digest(root)
            write('source/resource-packs.json', {'releases':{'v70.0':resources}})
            self.assertEqual(application_info(root)['content_version'], '70.1')
            data['entries'][0]['visual']['crop']['y'] = 99
            write('data/catalog.json', data)
            self.assertEqual(application_info(root)['image_release'], 'v70.0')
            rights['assets'][0]['sha256'] = 'c'*64
            write('source/rights-review.json', rights)
            with self.assertRaisesRegex(ValueError, 'not proven compatible'):
                application_info(root)
            rights['assets'][0]['sha256'] = 'a'*64
            write('source/rights-review.json', rights)
            exports['images/board.webp']['file'] = 'images/export-data/changed.js'
            write('data/image-export-index.json', exports)
            with self.assertRaisesRegex(ValueError, 'not proven compatible'):
                application_info(root)


if __name__ == '__main__':
    unittest.main()
