"""Read-only smoke check of a deployed edition and its hashed assets."""
import argparse
import hashlib
import json
from pathlib import PurePosixPath
import time
import urllib.parse
import urllib.request


def check(base, expected_commit):
    def read(relative, limit=8*1024*1024):
        path=PurePosixPath(relative)
        if path.is_absolute() or '..' in path.parts or '\\' in relative:
            raise ValueError('Invalid release asset path')
        request=urllib.request.Request(urllib.parse.urljoin(base,relative),headers={'User-Agent':'female-appearance-atlas-smoke-check'})
        with urllib.request.urlopen(request,timeout=20) as response:
            raw=response.read(limit+1)
            if len(raw)>limit:raise ValueError('Unexpected response size: '+relative)
            return raw
    build=json.loads(read('build-info.json'))
    if build.get('source_commit')!=expected_commit or build.get('source_dirty') is not False:
        raise ValueError('Expected source commit is not live yet')
    manifest=json.loads(read('release-manifest.json'))
    if manifest.get('build')!=build:raise ValueError('Build and release manifests disagree')
    html=read('index.html').decode('utf-8')
    if build['runtime_index'] not in html or '女性之美' not in html:raise ValueError('Unexpected homepage')
    files={item['path']:item for item in manifest['files']}
    sample_image=next(name for name in files if name.startswith('images/') and name.endswith(('.webp','.jpg','.png')))
    paths=[build['runtime_index'],next(iter(build['detail_chunks'].values())),sample_image]
    for path in paths:
        raw=read(path)
        if len(raw)!=files[path]['bytes'] or hashlib.sha256(raw).hexdigest()!=files[path]['sha256']:
            raise ValueError('Published asset digest mismatch: '+path)
    return {'passed':True,'url':base,'app_version':build['app_version'],
            'content_version':build['content_version'],'source_commit':expected_commit,'checked_assets':paths}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base',required=True)
    parser.add_argument('--expect-commit',required=True)
    parser.add_argument('--attempts',type=int,default=6)
    args=parser.parse_args()
    parsed=urllib.parse.urlsplit(args.base)
    if parsed.scheme!='https' or not args.base.endswith('/'):
        parser.error('Expected an HTTPS website base ending in /')
    for attempt in range(args.attempts):
        try:
            print(json.dumps(check(args.base,args.expect_commit),ensure_ascii=False));return
        except (OSError,ValueError,KeyError,StopIteration) as error:
            if attempt+1==args.attempts:raise
            print('Waiting for published assets: '+str(error),flush=True);time.sleep(10)


if __name__=='__main__':main()
