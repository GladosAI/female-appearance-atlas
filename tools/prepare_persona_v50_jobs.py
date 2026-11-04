"""Prepare five full-body sheets, preserving published QL IDs."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent));import _bootstrap
import build_atlas_v2
import persona_v50 as content
root=_bootstrap.ROOT
es=[dict(e,id=f'QL{153+i:03}') for i,e in enumerate(content.NEW_ENTRIES)]
common='''Use case: stylized-concept. Asset: original adult female character-design appearance atlas.
Create EXACTLY TWO COLUMNS by TWO ROWS, FOUR LARGE portrait cells, order top-left, top-right, bottom-left, bottom-right. Portrait canvas approximately2:3. Thin straight gray separator rules at middle x and middle y. No outer title. Put each EXACT short ID at top left of its cell in small plain black text. No other text, logos or watermarks. Pale warm ivory background, diffuse studio lighting. Polished anime-adjacent fashion illustration, clean controlled fine outlines, rich fabric shading, readable expressive mature faces. Exactly ONE clearly ADULT woman age25–34 in every cell, four adult women total. Youthful cute adult faces allowed, but keep natural mature adult anatomy.
Full standing body in EVERY panel: complete hairstyle and crown, full outfit, complete arms/hands or natural occlusion, COMPLETE shoes and feet, clear margins from cell edges. Keep faces large enough for brows, gaze and lips to be readable. Express each requested acting direction jointly through outfit, expression, gestures and stance. Hands: one thumb and four fingers, correct arm connections and natural occlusion, no fused fingers or extra limbs. No additional inset people or floating body parts. Opaque clothing covers private areas. No sexual scene, no childlike bodies, no school uniforms. No weapons, violence, injuries, blood, self-harm, straitjackets, restraints, horror caricatures or diagnostic symbols. These are fictional acting labels, not claims that appearance establishes a medical diagnosis.\n'''
jobs=[]
for key,title in content.GROUPS:
    group=[e for e in es if e['persona_group']==key];assert len(group)==4
    prompt=common+'\nFour ordered cells:\n'+'\n'.join(f"Panel{i+1}, ID {e['id']}: {e['en']}. {e['illustration_recipe']}." for i,e in enumerate(group))
    jobs.append(dict(id='persona-v50-'+key,category='persona_looks',dimension=title,title=title+' · 4项',framing='full_body',image=f"images/sheet-{group[0]['id'].lower()}-{group[-1]['id'].lower()}.png",columns=2,rows=2,edition=50,entries=[{k:e[k] for k in ['id','name','en']} for e in group],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==50}
for j in jobs:
    for k in ['image','column_boundaries','row_boundaries','edit_prompt','reference_image','edit_history']:
        if k in prior.get(j['id'],{}):j[k]=prior[j['id']][k]
p.write_text(json.dumps([j for j in old if j.get('edition')!=50]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/persona-v50/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'entries':len(j['entries'])} for j in jobs]))
