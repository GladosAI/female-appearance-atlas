"""Prepare eight four-cell full-body sheets without changing existing IDs."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent));import _bootstrap
import build_atlas_v2
import persona_v49 as content
root=_bootstrap.ROOT;counts={'persona_looks':128,'fashion_outfits':264,'traditional':64};prefix={'persona_looks':'QL','fashion_outfits':'FS','traditional':'TR'}
es=[]
for e in content.NEW_ENTRIES:
    counts[e['category']]+=1;es.append(dict(e,id=prefix[e['category']]+f"{counts[e['category']]:03}"))
common='''Use case: stylized-concept. Asset: original adult female character-design appearance atlas.
Create EXACTLY TWO COLUMNS by TWO ROWS, FOUR LARGE portrait cells in order top-left, top-right, bottom-left, bottom-right. Canvas portrait approximately2:3. Thin straight gray separator rules through middle x and middle y. NO outer title. Label each cell with its EXACT short ID at top left in small plain black text. No other text, logos or watermarks. Pale warm ivory cell background, consistent diffuse studio lighting. Polished detailed anime-adjacent fashion illustration, controlled fine outlines, rich fabric shading, nuanced mature faces. Exactly ONE clearly ADULT woman age25–40 per cell, four adult women total, natural mature anatomy.
Every panel shows the FULL standing body: complete hairstyle, full outfit, complete arms and hands or natural occlusion, and COMPLETE shoes and feet, with clear margins from every cell edge. Keep each figure tall enough that eyebrows, eyelids, gaze and lips remain readable. Costume, expression, hands and stance must jointly express each specified acting label. Correct hands with one thumb and four fingers; natural finger occlusion, no extra digits or arms. No inset faces or extra figures. All garments opaque at private areas. No sexual action, violence, self-harm, injury, blood or diagnosis imagery. Acting labels are original fictional character designs. No childlike anatomy, no school-age styling.
'''
jobs=[]
for key,cid,title in content.GROUPS:
    group=[e for e in es if e['presence_v49_group']==key];assert len(group)==4
    prompt=common+'\nFour ordered cells:\n'+'\n'.join(f"Panel{i+1}, ID {e['id']}: {e['en']}. {e['illustration_recipe']}." for i,e in enumerate(group))
    jobs.append(dict(id='persona-v49-'+key,category=cid,dimension=title,title=title+' · 4项',framing='full_body',image=f"images/sheet-{group[0]['id'].lower()}-{group[-1]['id'].lower()}.png",columns=2,rows=2,edition=49,entries=[{k:e[k] for k in ['id','name','en']} for e in group],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==49}
for j in jobs:
    for k in ['image','column_boundaries','row_boundaries','edit_prompt','reference_image','edit_history']:
        if k in prior.get(j['id'],{}):j[k]=prior[j['id']][k]
p.write_text(json.dumps([j for j in old if j.get('edition')!=49]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/persona-v49/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'entries':len(j['entries'])} for j in jobs]))
