"""Download only the six individually verified Public Domain museum images."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys, json, urllib.request
sys.pycache_prefix = str(Path(__file__).resolve().parents[1] / '.work/cache/python')
import _bootstrap

ROOT = _bootstrap.ROOT
refs = json.loads((ROOT / 'data/references.json').read_text(encoding='utf-8'))

def download(ref):
    target = ROOT / ref['image']
    if target.exists() and target.stat().st_size > 1000:
        return ref['id'], 'already saved', target.stat().st_size
    request = urllib.request.Request(ref['image_url'], headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(request, timeout=35) as response:
        assert response.headers.get_content_type().startswith('image/'), ref['id']
        data = response.read()
    assert len(data)>1000 and data[:3]==b'\xff\xd8\xff', ref['id']
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return ref['id'], 'saved', len(data)

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as pool:
        for outcome in pool.map(download, [r for r in refs if r.get('image')]):
            print(*outcome)
