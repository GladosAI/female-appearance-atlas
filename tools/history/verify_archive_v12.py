"""Check that the delivered offline archive matches its live catalog and files."""
from pathlib import Path
import json, zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT.parent / 'female-appearance-atlas.zip'
data = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
critical = [
    'index.html', 'catalog.json', 'illustrations.json', 'README.md',
    'atlas.md', 'clothing-atlas.md', 'hair-atlas.md', 'cosplay-atlas.md',
    'facial-atlas.md', 'fashion-guide.md', 'sources.md', 'references.json',
    'combinations.json', 'image-prompts-v11.json', 'image-prompts-v12.json',
    'image-jobs.json', 'extra-illustrations.json', 'expanded-entries.json',
    'tools/atlas_template.html', 'tools/build_atlas_v2.py',
    'tools/facial_expansion.py', 'tools/facial_docs.py', 'facial-references.json',
]
mapped = sorted({b['image'] for b in data['boards']} |
                {r['image'] for r in data['references'] if r.get('image')})
assert len(data['boards']) == 260
assert data['meta']['illustrated_count'] == 3661
with zipfile.ZipFile(ARCHIVE) as z:
    names = z.namelist()
    assert len(names) == len(set(names)), 'Duplicate archive paths'
    assert not any('verification' in n or '__pycache__' in n or
                   n.endswith(('.lock', '.tmp')) or 'preview' in Path(n).name
                   for n in names), 'Temporary QA content in archive'
    assert z.testzip() is None, 'Archive CRC failure'
    for relative in critical + mapped:
        assert z.read(ROOT.name + '/' + relative) == (ROOT / relative).read_bytes(), relative
    originals = [b['reference_image'] for b in data['boards'] if b.get('reference_image')]
    for relative in originals:
        assert z.read(ROOT.name + '/' + relative) == (ROOT / relative).read_bytes(), relative
report = {'passed': True, 'bytes': ARCHIVE.stat().st_size, 'files': len(names),
          'entries': len(data['entries']), 'mapped_boards': len(data['boards']),
          'mapped_assets': len(mapped), 'critical_files_exact': len(critical),
          'retained_edit_reference_files': len(set(originals)), 'crc_passed': True}
(ROOT / 'verification-v12' / 'archive-report.json').write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report, ensure_ascii=False))
