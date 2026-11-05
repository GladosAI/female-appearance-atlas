"""Prepare local review artifacts; never publishes or creates a hosting account."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile
from build_provenance import application_info
from web_delivery import write_runtime

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.git', '.work', 'node_modules', '__pycache__', 'dist', '.venv'}
LICENSE_BUNDLE_FILES = ['LICENSE', 'CONTENT-LICENSE', 'LICENSE-SCOPE.md', 'NOTICE.md',
                        'THIRD_PARTY_NOTICES.md', 'docs/licensing-proposal.md',
                        'docs/material-rights-audit.md', 'source/license-policy.json',
                        'source/rights-review.json', 'source/rights-evidence.json',
                        'source/rights-provenance.json']


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def allowed(path, root):
    return (not (set(path.relative_to(root).parts) & EXCLUDED)
            and path.suffix not in {'.tmp', '.pyc', '.lock'}
            and not (path.name.startswith('.env') and path.name!='.env.example')
            and not path.name.startswith('character-research'))


def package_legacy(root, archive):
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=3) as bundle:
        for path in sorted(root.rglob('*')):
            if path.is_file() and allowed(path, root):
                bundle.write(path, root.name + '/' + path.relative_to(root).as_posix())


def json_payload(html, element):
    match = re.search(r'(<script id="' + element + r'" type="application/json">)(.*?)(</script>)', html, re.S)
    if not match:
        raise ValueError('Missing runtime data element: ' + element)
    return json.loads(match.group(2).replace('<\\/', '</'))


def runtime_data(data):
    # Prompt recipes belong in authoring data, not in every visitor's initial download.
    source = json.loads(json.dumps(data))
    source['boards'] = [{key: value for key, value in board.items()
                         if key not in {'prompt', 'edit_prompt', 'reference_image', 'edit_history', 'source_png', 'original', 'entries'}}
                        for board in source['boards']]
    for entry in source['entries']:
        for key in ['illustration_recipe', 'history_recipe']:
            entry.pop(key, None)
    source['image_exports'] = {}  # HTTP can read same-origin original image files.
    return source


def manifest(folder):
    files = []
    for path in sorted(folder.rglob('*')):
        if path.is_file() and path.name != 'release-manifest.json':
            content = path.read_bytes()
            files.append({'path': path.relative_to(folder).as_posix(), 'bytes': len(content),
                          'sha256': hashlib.sha256(content).hexdigest()})
    policy_path=ROOT/'source/license-policy.json'
    policy=json.loads(policy_path.read_text(encoding='utf-8')) if policy_path.exists() else {}
    content_selected=all(policy.get(key,{}).get('status')=='selected' and policy[key].get('license')
                         for key in ['editorial_content','ai_images','brand_artwork'])
    result = {'schema': 'female-appearance-release/v1', 'files': files,
              'total_bytes': sum(item['bytes'] for item in files),
              'license_status': 'selected' if content_selected and (ROOT/'LICENSE').exists() else 'partial-code-only' if (ROOT/'LICENSE').exists() else 'pending-review',
              'code_license': policy.get('code',{}).get('spdx'),
              'content_license_status': 'selected' if content_selected else 'pending-owner-decision',
              'content_licenses': {key:policy.get(key,{}).get('license')
                                   for key in ['editorial_content','ai_images','brand_artwork']},
              'third_party_licenses': 'Per-asset exceptions retain their original terms; see THIRD_PARTY_NOTICES.md'}
    build_info=folder/'build-info.json'
    if build_info.exists():
        result['build']=json.loads(build_info.read_text(encoding='utf-8'))
    (folder / 'release-manifest.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return result


def build_web(output, image_mode='original'):
    output.mkdir(parents=True, exist_ok=True)
    # Work in a fresh target; old optimized assets must not survive a mode switch.
    if any(output.iterdir()):
        raise ValueError('Output must be empty; choose a new folder instead of overwriting a release')
    html = (ROOT / 'index.html').read_text(encoding='utf-8')
    full_data = json_payload(html, 'atlas-data')
    data = runtime_data(full_data)
    nav = json_payload(html, 'atlas-navigation')
    images = sorted({board['image'] for board in data['boards']} |
                    {ref['image'] for ref in data['references'] if ref.get('image')})
    mapping = {}
    if image_mode == 'webp':
        job = ROOT / '.work/web-image-job.json'
        job.parent.mkdir(exist_ok=True)
        job.write_text(json.dumps({'root': str(ROOT), 'output': str(output), 'images': images}), encoding='utf-8')
        subprocess.run(['node', str(ROOT / 'tools/prepare_web_images.cjs'), str(job)], check=True)
        mapping = {image: str(Path(image).with_suffix('.webp')).replace('\\', '/') for image in images if image.endswith('.png')}
        def replace_images(value):
            if isinstance(value, dict):
                return {key: replace_images(item) for key, item in value.items()}
            if isinstance(value, list):
                return [replace_images(item) for item in value]
            return mapping.get(value, value) if isinstance(value, str) else value
        data = replace_images(data)
        full_data = replace_images(full_data)
        html = html.replace('下载图片</button>', '下载预览图</button>')
    else:
        for image in images:
            target = output / image
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / image, target)
    for directory in ['assets', 'docs', 'schemas']:
        if (ROOT / directory).exists():
            shutil.copytree(ROOT / directory, output / directory, dirs_exist_ok=True)
    contribution_index=output/'assets/contribution-index.js'
    contribution_hash=sha256_file(contribution_index)[:12]
    contribution_name='assets/contribution-index-'+contribution_hash+'.js'
    contribution_index.rename(output/contribution_name)
    contribution_page=(ROOT/'contribute.html').read_text(encoding='utf-8').replace('assets/contribution-index.js',contribution_name)
    (output/'contribute.html').write_text(contribution_page,encoding='utf-8')
    shutil.copy2(ROOT/'CONTRIBUTING.md',output/'CONTRIBUTING.md')
    relative, detail_chunks = write_runtime(output, data, nav)
    build_info=application_info(ROOT,include_commit=True)
    build_info['image_delivery']=image_mode
    build_info['runtime_index']=relative
    build_info['detail_chunks']=detail_chunks
    (output/'build-info.json').write_text(json.dumps(build_info,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    html=re.sub(r'(<script id="atlas-build" type="application/json">).*?(</script>)',
                lambda match:match[1]+json.dumps(build_info,ensure_ascii=False,separators=(',',':'))+match[2],html,flags=re.S)
    html = re.sub(r'(<script id="atlas-data" type="application/json">).*?(</script>)', r'\1\2', html, flags=re.S)
    html = re.sub(r'(<script id="atlas-navigation" type="application/json">).*?(</script>)', r'\1\2' + f'\n<script src="{relative}"></script>', html, flags=re.S)
    if image_mode == 'webp':
        html = html.replace('<footer class="footer">', '<footer class="footer">在线预览使用有损 WebP 压缩图片；<a href="https://github.com/GladosAI/female-appearance-atlas/releases/latest" target="_blank" rel="noopener">下载完整离线资源包与原图</a>。<br>')
    (output / 'index.html').write_text(html, encoding='utf-8')
    (output / '.nojekyll').write_text('', encoding='utf-8')
    (output / 'data').mkdir(exist_ok=True)
    for path in (ROOT / 'data').glob('*'):
        if path.is_file() and path.name != 'image-export-index.json':
            shutil.copy2(path, output / 'data' / path.name)
    full_data['image_exports'] = {}
    (output/'data/catalog.json').write_text(json.dumps(full_data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (output/'data/illustrations.json').write_text(json.dumps(full_data['boards'],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if image_mode=='webp':
        path=output/'data/agent-index.jsonl'
        records=[replace_images(json.loads(line)) for line in path.read_text(encoding='utf-8').splitlines() if line]
        path.write_text(''.join(json.dumps(record,ensure_ascii=False,separators=(',',':'))+'\n' for record in records),encoding='utf-8')
    data_manifest={'schema':'female-appearance-data-manifest/v1','catalog_version':full_data['meta']['version'],'delivery':image_mode,'files':{}}
    for relative in ['data/catalog.json','data/navigation.json','data/agent-index.jsonl']:
        path=output/relative
        data_manifest['files'][relative]={'bytes':path.stat().st_size,'sha256':sha256_file(path)}
    (output/'data/manifest.json').write_text(json.dumps(data_manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for file in ['view-relations.html', 'NOTICE.md', 'LICENSE', 'CONTENT-LICENSE', 'LICENSE-SCOPE.md', 'THIRD_PARTY_NOTICES.md']:
        if (ROOT / file).exists():
            shutil.copy2(ROOT / file, output / file)
    # Public audit links must resolve in the preview without exposing private receipts.
    for file in ['license-policy.json','rights-review.json','rights-evidence.json','rights-provenance.json']:
        if (ROOT/'source'/file).exists():
            (output/'source').mkdir(exist_ok=True)
            shutil.copy2(ROOT/'source'/file,output/'source'/file)
    quality_records = sorted((ROOT/'source/quality-reviews').glob('*.json'))
    quality_records += sorted((ROOT/'source').glob('material-quality-prompts-*.json'))
    for source in quality_records:
        target = output/source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    scene_records = sorted((ROOT/'source').glob('scene-*.json'))
    scene_records += sorted((ROOT/'source/contributions').glob('scenes-v*.json'))
    scene_records += sorted((ROOT/'source/rights-history').glob('*.json'))
    for plan in sorted((ROOT/'source').glob('scene-plan-v*.json')):
        scene_records.append(ROOT/'prompts'/('image-prompts-v'+plan.stem.removeprefix('scene-plan-v')+'.json'))
    for source in scene_records:
        target = output/source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    (output / '_headers').write_text('/assets/runtime-*.js\n  Cache-Control: public, max-age=31536000, immutable\n/images/*\n  Cache-Control: public, max-age=3600\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n', encoding='utf-8')
    (output / 'wrangler.jsonc').write_text(json.dumps({'name': 'female-appearance-atlas', 'compatibility_date': '2026-11-02', 'assets': {'directory': '.', 'not_found_handling': '404-page'}}, indent=2) + '\n', encoding='utf-8')
    result = manifest(output)
    files = result['files']
    result['static_host_check'] = {'pages_file_limit_ok': len(files) + 2 <= 20000,
                                  'pages_max_file_ok': all(item['bytes'] < 25 * 1024**2 for item in files),
                                  'github_pages_size_ok': result['total_bytes'] < 1024**3}
    print(json.dumps({'output': str(output), 'files': len(files), 'bytes': result['total_bytes'],
                      'image_mode': image_mode, 'limits': result['static_host_check']}, ensure_ascii=False))


def build_packages(output):
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        raise ValueError('Output must be empty')
    groups = {'source': [], 'images': [], 'offline-copy': []}
    catalog=json.loads((ROOT/'data/catalog.json').read_text(encoding='utf-8'))
    needed_images={board['image'] for board in catalog['boards']} | {ref['image'] for ref in catalog['references'] if ref.get('image')}
    export_index=json.loads((ROOT/'data/image-export-index.json').read_text(encoding='utf-8'))
    needed_exports={record['file'] for image,record in export_index.items() if image in needed_images}
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file() or not allowed(path, ROOT):
            continue
        relative = path.relative_to(ROOT)
        group = 'offline-copy' if relative.parts[:2] == ('images', 'export-data') else 'images' if relative.parts[0] == 'images' else 'source'
        if group=='images' and relative.as_posix() not in needed_images:
            continue
        if group=='offline-copy' and relative.as_posix() not in needed_exports:
            continue
        groups[group].append(path)
    for group in ['images', 'offline-copy']:
        for relative in LICENSE_BUNDLE_FILES:
            file = ROOT / relative
            if not file.is_file():
                raise ValueError('Missing license bundle file: ' + relative)
            if file not in groups[group]:
                groups[group].append(file)
    results = []
    for group, paths in groups.items():
        archive = output / f'female-appearance-atlas-{group}.zip'
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=3) as bundle:
            for path in paths:
                bundle.write(path, 'female-appearance-atlas/' + path.relative_to(ROOT).as_posix())
        if archive.stat().st_size >= 2 * 1024**3:
            raise ValueError(archive.name + ' exceeds GitHub Release single-file limit')
        results.append({'file': archive.name, 'bytes': archive.stat().st_size,
                        'sha256': sha256_file(archive)})
    (output / 'CHECKSUMS.json').write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(results))


def build_application(output):
    """Publish code updates with explicit links to unchanged, separately versioned resources."""
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        raise ValueError('Output must be empty')
    info=application_info(ROOT,include_commit=True)
    if not info.get('source_commit') or info.get('source_dirty'):
        raise ValueError('Application release requires a clean, committed source checkout')
    registry=json.loads((ROOT/'source/resource-packs.json').read_text(encoding='utf-8'))
    resources=registry['releases'][info['image_release']]
    # application_info has already checked version compatibility and, for metadata revisions, inventory identity.
    archive=output/'female-appearance-atlas-source.zip'
    subprocess.run(['git','archive','--format=zip','--prefix=female-appearance-atlas/',
                    '--output='+str(archive),info['source_commit']],cwd=ROOT,check=True)
    with zipfile.ZipFile(archive,'a',zipfile.ZIP_DEFLATED) as bundle:
        metadata=zipfile.ZipInfo('female-appearance-atlas/build-info.json',(1980,1,1,0,0,0))
        metadata.compress_type=zipfile.ZIP_DEFLATED
        bundle.writestr(metadata,json.dumps(info,ensure_ascii=False,indent=2)+'\n')
    tag='app-v'+info['app_version']
    records=[{'file':archive.name,'bytes':archive.stat().st_size,'sha256':sha256_file(archive),
              'url':f'https://github.com/GladosAI/female-appearance-atlas/releases/download/{tag}/{archive.name}'},
             *resources['assets']]
    (output/'CHECKSUMS.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
    (output/'RESOURCE-PACKS.json').write_text(json.dumps({'build':info,'resource_release':info['image_release'],
        'assets':resources['assets']},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'tag':tag,'build':info,'assets':records},ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', choices=['web', 'packages', 'application'])
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--image-mode', choices=['original', 'webp'], default='original')
    args = parser.parse_args()
    output = args.output.resolve()
    if output == ROOT or ROOT.is_relative_to(output):
        parser.error('Output cannot be the project root or one of its parents')
    if args.target == 'web':
        build_web(output, args.image_mode)
    elif args.target == 'packages':
        build_packages(output)
    else:
        build_application(output)


if __name__ == '__main__':
    main()
