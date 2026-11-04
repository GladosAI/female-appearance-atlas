"""Prepare ten paired full-body identity sheets with explicit same-character direction."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent));import _bootstrap
import build_atlas_v2
import identity_v51 as content
root=_bootstrap.ROOT;counts={cid:0 for cid in content.NEW_CATEGORIES};prefix=dict(zip(content.NEW_CATEGORIES,['IS','ID','IC']));es=[]
for e in content.NEW_ENTRIES:
    counts[e['category']]+=1;es.append(dict(e,id=prefix[e['category']]+f"{counts[e['category']]:03}"))
common='''Use case: stylized-concept. Asset: original adult female character-design identity atlas.
Create EXACTLY TWO tall portrait cells SIDE BY SIDE, TWO COLUMNS and ONE ROW, TWO full-body figures total. Wide landscape canvas approximately3:2, thin straight gray separator at middle x. No title or extra text. Pale warm ivory background, consistent diffuse studio lighting, polished detailed anime-adjacent fashion illustration, clean controlled outlines and rich fabric shading. Put each exact short ID at the TOP LEFT of its own cell in small plain black text. No logo or watermark.
Each cell shows ONE clearly adult woman age25–38: full standing body with COMPLETE crown/hairstyle, hands or natural occlusion, full garments and BOTH complete shoes/feet, all well inside cell edges with clear margins. Hands anatomically coherent, one thumb and four fingers, natural occlusion, no extra limbs. Keep facial features large and readable. Opaque garments cover private areas. These are original fictional character concepts, not historical replicas or named real characters. No sexual scene, violence, injury, weapons or childlike anatomy. No extra insets, floating props or additional people.
The two cells MUST depict the SAME woman in two distinct outfits and situations. Match face identity, age, eye color, skin tone, hair color and described signature details exactly.\n'''
jobs=[]
for key,cid,title,character in content.GROUPS:
    group=[e for e in es if e['identity_pair']==key];assert len(group)==2
    prompt=common+'\nSame-character design: '+character+'\n'+'\n'.join(f"{'LEFT' if i==0 else 'RIGHT'} cell, ID {e['id']}: {e['en']}. {e['illustration_recipe']}." for i,e in enumerate(group))
    jobs.append(dict(id='identity-v51-'+key,category=cid,dimension=title,title=title+' · 双造型对照',framing='paired_full_body',image=f"images/sheet-{group[0]['id'].lower()}-{group[-1]['id'].lower()}.png",columns=2,rows=1,edition=51,entries=[{k:e[k] for k in ['id','name','en']} for e in group],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==51}
for j in jobs:
    for k in ['image','column_boundaries','row_boundaries','edit_prompt','reference_image','edit_history']:
        if k in prior.get(j['id'],{}):j[k]=prior[j['id']][k]
p.write_text(json.dumps([j for j in old if j.get('edition')!=51]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/identity-v51/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'entries':len(j['entries'])} for j in jobs]))
