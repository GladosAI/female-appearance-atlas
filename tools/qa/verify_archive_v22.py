"""Check that the delivered offline archive matches its live catalog and files."""
import sys
from pathlib import Path
sys.pycache_prefix = str(Path(__file__).resolve().parents[2] / '.work/cache/python')
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _bootstrap
from pathlib import Path
import json, zipfile

ROOT = _bootstrap.ROOT
ARCHIVE = _bootstrap.PACKAGE
data = json.loads((ROOT / 'data/catalog.json').read_text(encoding='utf-8'))
critical = [
    'source/nun-states-growth-references.json','source/catalog/nun_states_growth_expansion.py','tools/builders/nun_states_growth_docs.py','docs/nun-atlas.md','docs/sleep-coma-death-atlas.md','docs/age-size-atlas.md','prompts/image-prompts-v21.json','tools/qa/verify_atlas_v21.cjs','tools/qa/verify_navigation_v21.cjs','tools/qa/verify_archive_v21.py','tools/qa/inspect_image_cells_v22.cjs','tools/qa/inspect_nun_states_growth_grid_v22.cjs',
    'source/special-age-references.json','source/catalog/special_age_expansion.py','tools/builders/special_age_docs.py','docs/special-variants-atlas.md','docs/female-ages-atlas.md','prompts/image-prompts-v22.json','tools/qa/verify_atlas_v22.cjs','tools/qa/verify_navigation_v22.cjs','tools/qa/verify_archive_v22.py',
    'source/costume-hair-references.json','source/catalog/costume_hair_expansion.py','tools/builders/costume_hair_docs.py','docs/special-costumes-atlas.md','docs/hair-states-atlas.md','prompts/image-prompts-v20.json','tools/qa/verify_atlas_v20.cjs','tools/qa/verify_navigation_v20.cjs','tools/qa/verify_archive_v20.py',
    'source/wedding-references.json','source/catalog/wedding_expansion.py','tools/builders/wedding_docs.py','docs/wedding-atlas.md','prompts/image-prompts-v19.json','tools/qa/verify_atlas_v19.cjs','tools/qa/verify_navigation_v19.cjs','tools/qa/verify_archive_v19.py',
    'source/trend-model-references.json','source/catalog/trend_model_expansion.py','tools/builders/trend_model_docs.py','docs/trend-fashion-model-atlas.md','prompts/image-prompts-v18.json','tools/qa/verify_atlas_v18.cjs','tools/qa/verify_navigation_v18.cjs','tools/qa/verify_archive_v18.py',
    'source/navigation.json', 'data/navigation.json', 'docs/directory.md', 'tools/builders/navigation_docs.py', 'tools/qa/verify_navigation_v17.cjs',
    'tools/_bootstrap.py', 'tools/builders/layout_docs.py', 'source/catalog/catalog_layout.py', 'index.html', 'data/catalog.json', 'data/illustrations.json', 'README.md',
    'docs/atlas.md', 'docs/clothing-atlas.md', 'docs/hair-atlas.md', 'docs/cosplay-atlas.md',
    'docs/facial-atlas.md', 'docs/fashion-guide.md', 'docs/sources.md', 'data/references.json',
    'data/combinations.json', 'prompts/image-prompts-v14.json', 'prompts/image-prompts-v15.json',
    'prompts/image-prompts-v16.json', 'docs/anthro-atlas.md', 'source/anthro-references.json', 'source/catalog/anthro_expansion.py', 'tools/builders/anthro_docs.py', 'prompts/image-prompts-v17.json', 'docs/seasonal-atlas.md', 'source/catalog/seasonal_expansion.py', 'tools/builders/seasonal_docs.py', 'source/image-jobs.json', 'source/extra-illustrations.json', 'source/expanded-entries.json',
    'tools/templates/atlas_template.html', 'tools/builders/build_atlas_v2.py',
    'source/catalog/facial_expansion.py', 'tools/builders/facial_docs.py', 'source/facial-references.json',
    'tools/qa/verify_atlas_v17.cjs', 'tools/qa/inspect_image_cells_v17.cjs', 'tools/qa/inspect_seasonal_grid_v17.cjs', 'tools/qa/verify_archive_v17.py', 'tools/builders/latest_docs.py', 'docs/socks-atlas.md', 'source/catalog/hosiery_expansion.py', 'tools/builders/hosiery_docs.py', 'source/hosiery-references.json',
]
mapped = sorted({b['image'] for b in data['boards']} |
                {r['image'] for r in data['references'] if r.get('image')})
assert len(data['boards']) == 337
assert data['meta']['illustrated_count'] == 4893
with zipfile.ZipFile(ARCHIVE) as z:
    names = z.namelist()
    assert len(names) == len(set(names)), 'Duplicate archive paths'
    assert not any('/.work/' in n or 'verification' in n or '__pycache__' in n or
                   n.endswith(('.lock', '.tmp')) or 'preview' in Path(n).name
                   for n in names), 'Temporary QA content in archive'
    assert z.testzip() is None, 'Archive CRC failure'
    for relative in critical + mapped:
        assert z.read(ROOT.name + '/' + relative) == (ROOT / relative).read_bytes(), relative
    originals = [b['reference_image'] for b in data['boards'] if b.get('reference_image')] + [h['reference_image'] for b in data['boards'] for h in b.get('edit_history', [])]
    for relative in originals:
        assert z.read(ROOT.name + '/' + relative) == (ROOT / relative).read_bytes(), relative
report = {'passed': True, 'bytes': ARCHIVE.stat().st_size, 'files': len(names),
          'entries': len(data['entries']), 'mapped_boards': len(data['boards']),
          'mapped_assets': len(mapped), 'critical_files_exact': len(critical),
          'retained_edit_reference_files': len(set(originals)), 'crc_passed': True}
(ROOT / '.work/verification/v22' / 'archive-report.json').write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report, ensure_ascii=False))
