"""Prepare eight full-body presence sheets and four larger hand/face-acting sheets."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent));import _bootstrap
import build_atlas_v2
import presence_gesture_v48 as content
root=_bootstrap.ROOT
counts={'persona_looks':96,'face_hands':48};prefix={'persona_looks':'QL','face_hands':'HG'}
es=[]
for e in content.NEW_ENTRIES:
    counts[e['category']]+=1
    es.append(dict(e,id=prefix[e['category']]+f"{counts[e['category']]:03}"))
common='''Use case: stylized-concept. Asset: original adult female character-design appearance atlas.
Create EXACTLY TWO COLUMNS by TWO ROWS, FOUR LARGE portrait cells, order top-left, top-right, bottom-left, bottom-right. Canvas portrait approximately2:3. Thin straight gray separator rules through middle x and middle y. NO outer title. Label each cell with its EXACT short ID at top left in small plain black text. No other text, logos or watermarks. Pale warm ivory cell background, consistent diffuse studio lighting. Polished detailed anime-adjacent fashion illustration, controlled fine outlines, rich fabric shading, nuanced mature faces. Exactly ONE clearly ADULT woman age25–35 per cell, four adult women total. No childlike proportions.
Hands are crucial: exactly two anatomically coherent arms per person, correct five-digit hands with one thumb and four fingers, natural believable occlusion when hands clasp; do not force all fingers visible. No extra fingers, fused fingertips, floating wrists or arms cut by cell borders. Fingers must touch only where intended. Keep complete face, crown and every relevant hand and wrist INSIDE its own cell with clear margin. No additional inset hands, faces or people.
All outfits opaque at private areas. No sexual context or posing. Gestures are general original character acting, not depictions of a named religious rite or a medical condition.
'''
frames={
'full_body':'FRAMING: full standing body in EVERY panel, entire hairstyle and COMPLETE shoes/feet, complete hands or natural occlusion; leave clear margins. Face, posture and outfit must jointly express the requested label. Balanced adult anatomy, no exaggerated curves.',
'upper_body':'FRAMING: LARGE WAIST-UP portrait in EVERY panel. Deliberate lower crop is at waist, NEVER at a wrist or fingertips. Show full crown, face, shoulders, both forearms and COMPLETE hands, with facial features and individual fingers large and readable. No whole-body tiny figures.',
'head_to_knees':'FRAMING: EVERY panel shows full crown through just BELOW BOTH KNEES, deliberately cropped below knees, not full shoes. Include COMPLETE hands, forearms, relevant torso bow, skirt-holding folds and the bent-knee curtsy. Keep face readable; no extreme deep bow or face hidden by hands.'}
jobs=[]
for key,cid,title,framing in content.GROUPS:
    field='persona_group' if cid=='persona_looks' else 'gesture_group'
    group=[e for e in es if e.get(field)==key];assert len(group)==4
    prompt=common+'\n'+frames[framing]+'\nFour ordered cells:\n'+'\n'.join(f"Panel{i+1}, ID {e['id']}: {e['en']}. {e['illustration_recipe']}." for i,e in enumerate(group))
    jobs.append(dict(id='presence-gesture-v48-'+key,category=cid,dimension=title,title=title+' · 4项',framing=framing,image=f"images/sheet-{group[0]['id'].lower()}-{group[-1]['id'].lower()}.png",columns=2,rows=2,edition=48,entries=[{k:e[k] for k in ['id','name','en']} for e in group],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==48}
for j in jobs:
    for k in ['image','column_boundaries','row_boundaries','edit_prompt','reference_image','edit_history']:
        if k in prior.get(j['id'],{}):j[k]=prior[j['id']][k]
p.write_text(json.dumps([j for j in old if j.get('edition')!=48]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/presence-gesture-v48/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'entries':len(j['entries']),'framing':j['framing']} for j in jobs]))
