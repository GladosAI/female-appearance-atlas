import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import release_atlas


class StandaloneResourceLicenseTests(unittest.TestCase):
    def test_each_download_package_carries_its_license_and_exceptions(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)/'project'
            for relative in release_atlas.LICENSE_BUNDLE_FILES:
                file=root/relative;file.parent.mkdir(parents=True,exist_ok=True)
                file.write_text('CC0 exceptions' if relative=='THIRD_PARTY_NOTICES.md' else 'Noncommercial license fixture')
            (root/'data').mkdir()
            (root/'data/catalog.json').write_text(json.dumps({'boards':[{'image':'images/board.png'}],'references':[]}))
            (root/'images/export-data').mkdir(parents=True)
            (root/'images/board.png').write_bytes(b'board fixture')
            (root/'images/export-data/board.js').write_text('offline copy fixture')
            output=Path(folder)/'packages'
            with patch.object(release_atlas,'ROOT',root),contextlib.redirect_stdout(io.StringIO()):
                release_atlas.build_packages(output)
            archives=list(output.glob('*.zip'))
            self.assertEqual(len(archives),3)
            for archive in archives:
                with zipfile.ZipFile(archive) as bundle:
                    self.assertIn('female-appearance-atlas/CONTENT-LICENSE',bundle.namelist())
                    self.assertEqual(bundle.read('female-appearance-atlas/THIRD_PARTY_NOTICES.md'),b'CC0 exceptions')
                    self.assertIn('female-appearance-atlas/source/rights-review.json',bundle.namelist())
                    self.assertEqual(len(bundle.namelist()),len(set(bundle.namelist())))


if __name__=='__main__':unittest.main()
