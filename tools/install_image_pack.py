"""Verify a release image ZIP and install only images, preserving checked-out source."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import zipfile

ROOT = Path(__file__).resolve().parents[1]
IMAGE_PACKAGE = 'female-appearance-atlas-images.zip'


def install_image_pack(archive, checksums, root=ROOT):
    records = json.loads(checksums.read_text(encoding='utf-8'))
    matches = [item for item in records if item.get('file') == IMAGE_PACKAGE]
    if len(matches) != 1:
        raise ValueError('Expected exactly one image package checksum')
    expected = matches[0]
    if (type(expected.get('bytes')) is not int or expected['bytes'] <= 0
            or not re.fullmatch(r'[0-9a-f]{64}', expected.get('sha256', ''))):
        raise ValueError('Invalid image package checksum record')
    digest = hashlib.sha256()
    with archive.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    if archive.stat().st_size != expected['bytes'] or digest.hexdigest() != expected['sha256']:
        raise ValueError('Image package size or SHA-256 mismatch; nothing installed')

    root = root.resolve()
    images = []
    seen = set()
    with zipfile.ZipFile(archive) as bundle:
        # Validate the complete archive before writing anything, including ignored license copies.
        for info in bundle.infolist():
            path = PurePosixPath(info.filename)
            if (path.is_absolute() or '..' in path.parts or '\\' in info.filename
                    or ':' in info.filename or not path.parts
                    or path.parts[0] != 'female-appearance-atlas'
                    or stat.S_ISLNK(info.external_attr >> 16)):
                raise ValueError('Unsafe image package member: ' + info.filename)
            if info.is_dir():
                continue
            relative = Path(*path.parts[1:])
            if relative.as_posix() in seen:
                raise ValueError('Duplicate image package member: ' + info.filename)
            seen.add(relative.as_posix())
            if relative.parts[:1] != ('images',):
                continue  # Never overwrite current code, data, or license metadata from the ZIP.
            if (len(relative.parts) != 2
                    or relative.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.webp'}):
                raise ValueError('Unexpected image package path: ' + info.filename)
            target = (root / relative).resolve()
            if not target.is_relative_to(root / 'images'):
                raise ValueError('Image target escapes the checkout')
            images.append((info, target))
        if not images:
            raise ValueError('Image package contains no images')
        for info, target in images:
            target.parent.mkdir(parents=True, exist_ok=True)
            with bundle.open(info) as source, target.open('wb') as destination:
                shutil.copyfileobj(source, destination)
    return {'installed_images': len(images), 'sha256': digest.hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', required=True, type=Path)
    parser.add_argument('--checksums', required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(install_image_pack(args.archive, args.checksums)))


if __name__ == '__main__':
    main()
