import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from install_image_pack import IMAGE_PACKAGE, install_image_pack


class InstallImagePackTests(unittest.TestCase):
    def make_package(self, folder, members):
        archive = folder / IMAGE_PACKAGE
        with zipfile.ZipFile(archive, 'w') as bundle:
            for name, content in members:
                bundle.writestr(name, content)
        checksums = folder / 'CHECKSUMS.json'
        checksums.write_text(json.dumps([{'file': IMAGE_PACKAGE, 'bytes': archive.stat().st_size,
                                         'sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}]))
        return archive, checksums

    def test_install_images_without_overwriting_checked_out_license(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            root = folder / 'checkout'
            root.mkdir()
            (root / 'CONTENT-LICENSE').write_text('current license')
            archive, checksums = self.make_package(folder, [
                ('female-appearance-atlas/images/board.png', b'image'),
                ('female-appearance-atlas/CONTENT-LICENSE', b'old license')])
            result = install_image_pack(archive, checksums, root)
            self.assertEqual(result['installed_images'], 1)
            self.assertEqual((root / 'images/board.png').read_bytes(), b'image')
            self.assertEqual((root / 'CONTENT-LICENSE').read_text(), 'current license')

    def test_mismatched_hash_writes_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            archive, checksums = self.make_package(folder, [
                ('female-appearance-atlas/images/board.png', b'image')])
            archive.write_bytes(archive.read_bytes() + b'changed')
            with self.assertRaisesRegex(ValueError, 'SHA-256 mismatch'):
                install_image_pack(archive, checksums, folder / 'checkout')
            self.assertFalse((folder / 'checkout').exists())

    def test_traversal_is_rejected_before_installing_other_members(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            archive, checksums = self.make_package(folder, [
                ('female-appearance-atlas/images/board.png', b'image'),
                ('female-appearance-atlas/../escape.png', b'escape')])
            with self.assertRaisesRegex(ValueError, 'Unsafe'):
                install_image_pack(archive, checksums, folder / 'checkout')
            self.assertFalse((folder / 'checkout').exists())


if __name__ == '__main__':
    unittest.main()
