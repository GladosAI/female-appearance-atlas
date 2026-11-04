from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
report=json.loads((root/'verification-v4/image-cells.json').read_text(encoding='utf-8'))
assert report['checked']==report['expected']==1677 and not report['suspect']
jobs=[j for j in json.loads((root/'image-jobs.json').read_text(encoding='utf-8')) if j.get('edition')==4]
assert len(jobs)==16 and sum(len(j['entries']) for j in jobs)==176
ids={j['id'] for j in jobs};p=root/'extra-illustrations.json';boards=json.loads(p.read_text(encoding='utf-8'))
assert ids<={b['id'] for b in boards}
for b in boards:
    if b['id'] in ids:b['qa_status']='image_cells_checked'
p.write_text(json.dumps(boards,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
review={'edition':'4.0','new_sheets':16,'new_entries':176,'manual_review':'New sheets inspected for labels, shoulder exposure, distinct clothing structures and concrete fashion coordinates.',
        'coverage':'All 1677 mapped cells contain nonblank image content. Pixel inspection measures coverage, not historical or technical accuracy.',
        'classification':'Style tags can overlap. Ordinary sleeveless and dropped-shoulder items are not automatically labelled as exposed-shoulder garments.'}
(root/'verification-v4/content-review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'mapped_cells':1677,'new_pages':16,'blank_cells':0}))
