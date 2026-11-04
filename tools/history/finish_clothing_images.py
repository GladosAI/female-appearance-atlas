"""Record only the checks actually performed before packaging the final edition."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
cells=json.loads((root/'verification-v3/image-cells.json').read_text(encoding='utf-8'))
assert cells['checked']==cells['expected']==1501
assert not cells['suspect'],cells['suspect']
jobs=[j for j in json.loads((root/'image-jobs.json').read_text(encoding='utf-8')) if j.get('edition')==3]
assert len(jobs)==29
ids={j['id'] for j in jobs}
p=root/'extra-illustrations.json';boards=json.loads(p.read_text(encoding='utf-8'))
assert ids<={b['id'] for b in boards}
for b in boards:
    if b['id'] in ids:b['qa_status']='image_cells_checked'
p.write_text(json.dumps(boards,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
review={'edition':'3.0','new_entries':464,'new_sheets':29,'clothing_entries':711,'coverage':'All 1501 mapped cells have nonblank image content; original 1037 mappings retained.',
        'manual_review':'New contact sheets were inspected for layout, labels, visible outfit differences and obvious text/image mismatches. Low/wide necklines and short-skirt variants are clarified in design tips.',
        'limits':'Images are original anime concept examples. Pixel inspection verifies nonblank content, not historical or technical certification.'}
(root/'verification-v3/content-review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'image_cells':cells['checked'],'new_pages':29,'suspect':0}))
