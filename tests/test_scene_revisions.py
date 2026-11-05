import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import prepare_scenes_v71 as scenes


class SceneRevisionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / 'source/contributions/scenes-original.json'
        self.path.parent.mkdir(parents=True)
        self.original = {
            'schema': 'female-appearance-contribution/v1',
            'entries': [
                {'stable_id': 'SNW005', 'name': 'Old classroom', 'added_in': '71.0'},
                {'stable_id': 'SNU001', 'name': 'Unrelated school', 'added_in': '72.0'},
            ],
            'boards': [{'id': 'original-board', 'image': 'images/old.png'}],
        }
        self.path.write_text(json.dumps(self.original), encoding='utf-8')

    def replace(self, entries, boards):
        with patch.object(scenes, 'ROOT', self.root):
            scenes.replace_existing_contributions(entries, boards)

    def test_revision_preserves_ids_first_publication_and_unrelated_entries(self):
        self.replace(
            [{'stable_id': 'SNW005', 'name': 'Secondary classroom', 'added_in': '73.0'}],
            [{'id': 'original-board', 'image': 'images/new.png'}],
        )
        result = json.loads(self.path.read_text(encoding='utf-8'))
        self.assertEqual(len(result['entries']), 2)
        self.assertEqual(result['entries'][0], {'stable_id': 'SNW005', 'name': 'Secondary classroom', 'added_in': '71.0'})
        self.assertEqual(result['entries'][1], self.original['entries'][1])
        self.assertEqual(result['boards'], [{'id': 'original-board', 'image': 'images/new.png'}])
        self.assertEqual(len(list(self.path.parent.glob('*.json'))), 1)

    def test_missing_targets_do_not_write_partial_revisions(self):
        original_bytes = self.path.read_bytes()
        with self.assertRaisesRegex(AssertionError, 'replacement target missing'):
            self.replace(
                [{'stable_id': 'SNW005', 'name': 'Changed'}, {'stable_id': 'SNW999', 'name': 'Missing'}],
                [{'id': 'original-board', 'image': 'images/new.png'}],
            )
        self.assertEqual(self.path.read_bytes(), original_bytes)

    def test_unrecorded_first_publication_is_not_invented_by_a_revision(self):
        original = copy.deepcopy(self.original)
        original['entries'][0].pop('added_in')
        self.path.write_text(json.dumps(original), encoding='utf-8')
        self.replace([{'stable_id': 'SNW005', 'name': 'Revised', 'added_in': '73.0'}], [])
        result = json.loads(self.path.read_text(encoding='utf-8'))
        self.assertNotIn('added_in', result['entries'][0])


if __name__ == '__main__':
    unittest.main()
