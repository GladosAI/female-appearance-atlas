"""Public application/content/resource versions, without private machine metadata."""
import json
import re
import subprocess


def application_info(root, include_commit=False):
    release = json.loads((root / 'source/app-release.json').read_text(encoding='utf-8'))
    content = json.loads((root / 'source/content-release.json').read_text(encoding='utf-8'))
    package = json.loads((root / 'package.json').read_text(encoding='utf-8'))
    if release['version'] != package['version']:
        raise ValueError('Application version differs between package.json and source/app-release.json')
    if not re.fullmatch(r'v[0-9]+(?:\.[0-9]+)*', release['image_release']):
        raise ValueError('Invalid image resource Release tag')
    info = {'schema': 'female-appearance-build/v1', 'app_version': release['version'],
            'content_version': content['version'], 'image_release': release['image_release']}
    registry=root/'source/resource-packs.json'
    if registry.exists():
        packs=json.loads(registry.read_text(encoding='utf-8'))['releases']
        resources=packs.get(release['image_release'])
        if not resources or resources['content_version']!=content['version']:
            raise ValueError('Registered resource pack does not match the content version')
        expected={'female-appearance-atlas-images.zip','female-appearance-atlas-offline-copy.zip'}
        if len(resources['assets'])!=len(expected) or {asset['file'] for asset in resources['assets']}!=expected:
            raise ValueError('Incomplete resource pack registration')
        for asset in resources['assets']:
            url=f"https://github.com/GladosAI/female-appearance-atlas/releases/download/{release['image_release']}/{asset['file']}"
            if (asset['url']!=url or not re.fullmatch('[0-9a-f]{64}',asset['sha256'])
                    or type(asset['bytes']) is not int or asset['bytes']<=0):
                raise ValueError('Invalid resource pack digest or download address')
    if include_commit:
        info.update(source_commit=None,source_dirty=None)
        try:
            top=subprocess.run(['git','rev-parse','--show-toplevel'],cwd=root,capture_output=True,text=True)
            from pathlib import Path
            if top.returncode==0 and Path(top.stdout.strip()).resolve()==root.resolve():
                result = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=root, capture_output=True, text=True)
                commit = result.stdout.strip()
                info['source_commit'] = commit if result.returncode == 0 and re.fullmatch('[0-9a-f]{40}', commit) else None
                status = subprocess.run(['git', 'status', '--porcelain', '--untracked-files=no'],
                                        cwd=root, capture_output=True, text=True)
                info['source_dirty'] = bool(status.stdout.strip()) if status.returncode == 0 else None
        except FileNotFoundError:
            pass  # A downloaded source bundle can build without Git; do not invent a commit.
    return info
