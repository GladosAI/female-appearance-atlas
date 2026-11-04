"""Prepare two additional sheets for the existing sit/crouch/kneel/rise dimension."""
import sys,json
from pathlib import Path
sys.pycache_prefix=str(Path(__file__).resolve().parents[1]/'.work/cache/python')
import _bootstrap
from seated_pose_expansion_v37 import CATALOG,DIMENSION,SHEET_TOPICS
root=_bootstrap.ROOT
entries=[e for e in CATALOG if e.get('seated_pose_reference')]
for index,e in enumerate(entries,205):e['id']=f'PO{index:03}'
common='''Use case: stylized-concept.
Asset type: original anime/game full-body adult female pose-reference contact sheet.
Primary request: EXACTLY16 distinct anatomy-correct poses in the specified cell order, each as a single complete figure with the necessary chair/stool/bench/step/floor support.
Canvas/layout: PORTRAIT 2048x3072, EXACTLY4 equal columns by4 equal rows, tall equal cells, thin straight light-gray rules at quarter axes. Row-major left to right then down. Each cell has generous margins containing the whole head, both hands, both legs and both feet, and all relevant furniture or support contacts. No overlapping cells. Put ONLY the exact ID small and dark at the top left of each cell. NO other text, headings, captions, arrows, footers, extra panels or watermarks.
Subject: SAME original mature ADULT woman age25-35 throughout, adult face and adult proportions, tied-back dark-brown ponytail. Complete opaque teal long-sleeved sport top, charcoal full-length athletic trousers, plain soft flat sneakers. Clothing remains consistent in every cell; clearly draw trouser folds and the outline of both legs, with contrasting shoe soles where needed. Ordinary practical clothed pose drawing, neutral expression, no erotic framing, no exposed underwear or skin-focus.
Style: polished professional 2D anime anatomy-reference illustration, precise clean linework, restrained cel shading, clear readable silhouette. Warm ivory background, simple floor baseline, natural consistent light, neutral original clothing with no logos. Simple pale-gray solid furniture and thin exercise mat only where called for. One figure in every cell, no ghost figures or diagrams.
Anatomy/contacts: exactly two arms, two hands, two legs and two feet per person, correct joint directions. Feet, knees, palms and seat must visibly make the described contact, not float or merge. Keep left/right limb overlap understandable. For single-knee poses ONE knee touches floor and the OTHER foot is planted in front; do not turn every kneel into two knees on the floor. Camera at ordinary chest/hip level for the specified frontal, profile or three-quarter view; no dramatic perspective.
'''
directions={
 SHEET_TOPICS[0]:'''Cells1-3 are true KNEE-OVER-KNEE chair sitting: upper thigh crosses OVER lower thigh, top knee stacked above bottom knee; bottom foot touches floor, upper foot hangs. Cell4 is DIFFERENT: FIGURE-FOUR ankle-over-opposite-knee, upper knee points outward, making a visible triangular leg opening. Cell5 crosses at ANKLES only with knees together. Cells6-16 are individually different seated silhouettes; respect the listed seat versus floor support, and full trouser coverage. A simple chair may have a back and armrests when specified. Cross-legged floor/seat sitting is ordinary relaxed tailoring-clothed reference, no extreme splits.''',
 SHEET_TOPICS[1]:'''Cells1-6 are distinct ONE-KNEE half-kneels, the rear knee on floor and front sole planted; show these contacts unambiguously in every view. Cells7-8 are HEEL-SITTING kneels, hips visibly resting on heels, one front view and one strict side view, unlike upright high kneeling. Cells9-11 are low crouches with the specified hand support. Cells12-16 are specific transition FRAMES, not motion sequences: distinguish knee still touching ground, knee just lifted, palm-supported transition, near-standing chair-rise and just-off-seat arms-forward rise. No extra intermediate silhouettes. Keep every figure and support furniture wholly inside the cell.'''}
jobs=[]
for topic in SHEET_TOPICS:
    es=[e for e in entries if e['pose_sheet_topic']==topic];assert len(es)==16
    prompt=common+'Sheet direction: '+directions[topic]+'\nOrdered cells:\n'+'\n'.join(f"Cell{i+1}, ID {e['id']}: {e['en']} / {e['name']}. Camera: {e['pose_view']}. Support: {e['pose_support']}. Phase: {e['pose_phase']}. Pose: {e['pose_focus']}" for i,e in enumerate(es))
    jobs.append(dict(id='seated-v37-'+es[0]['id'].lower(),category='pose',dimension=DIMENSION,title=topic+' · 16项',image=f"images/sheet-{es[0]['id'].lower()}-{es[-1]['id'].lower()}.png",columns=4,rows=4,edition=37,entries=[{k:e[k] for k in ['id','name','en']} for e in es],prompt=prompt))
path=root/'source/image-jobs.json';old=json.loads(path.read_text(encoding='utf-8'));previous={j['id']:j for j in old if j.get('edition')==37}
for job in jobs:
    for field in ['image','reference_image','edit_prompt','column_boundaries','row_boundaries']:
        if field in previous.get(job['id'],{}):job[field]=previous[job['id']][field]
path.write_text(json.dumps([j for j in old if j.get('edition')!=37]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
output=root/'.work/verification/pose-v37/jobs.json';output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'image':j['image'],'count':len(j['entries'])} for j in jobs]))
