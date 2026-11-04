"""Prepare sixteen four-cell original concept sheets."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent));import _bootstrap
import build_atlas_v2
import scholar_myth_v53 as content
root=_bootstrap.ROOT;counts={cid:0 for cid in content.NEW_CATEGORIES};es=[]
for e in content.NEW_ENTRIES:
    counts[e['category']]+=1;es.append(dict(e,id=content.PREFIXES[e['category']]+f"{counts[e['category']]:03}"))
common='''Use case: stylized-concept. Asset: original adult female character appearance atlas, a final illustrated reference sheet.
Polished detailed anime-adjacent illustration with clean controlled outlines, readable mature adult faces, natural adult anatomy, carefully shaded opaque fabrics or described fantasy materials. Pale warm ivory cell backgrounds, even diffuse studio lighting. EXACTLY TWO COLUMNS and TWO ROWS, FOUR spacious tall portrait cells in row-major order, portrait canvas approximately2:3. Thin straight gray grid separators. EXACTLY ONE clearly adult woman age28–42 per cell, no additional figures, no insets.
Show the entire subject from hair/crown to full feet or shoes with generous clear margins on ALL sides; ALL fingertips, wings, tails, hair tips and footwear remain completely inside their own cell. Scale figure to fit, do not clip any extremity. Two coherent arms and legs, correct normal hands with believable occlusion. Frontal or three-quarter standing as described. Put ONLY the exact short ID in small plain black type at TOP LEFT of its own cell, no other text, titles, logo or watermark. No copied franchise costumes. No sexual context, nudity, violence or gore. Private areas fully opaque and covered; for liquid figures use an opaque clothing-shaped body surface without exposed anatomical detail. For cultural studies retain stated clothing structure and avoid mixing cultural insignia.\n'''
jobs=[]
for key,cid,title in content.GROUPS:
    group=[e for e in es if e['expansion_group']==key];assert len(group)==4
    prompt=common+'Ordered cells:\n'+'\n'.join(f"Cell{i+1}, ID {e['id']}: {e['en']}. {e['illustration_recipe']}." for i,e in enumerate(group))
    jobs.append(dict(id='scholar-myth-v53-'+key,category=cid,dimension=title,title=title+' · 4项',image=f"images/sheet-{group[0]['id'].lower()}-{group[-1]['id'].lower()}.png",columns=2,rows=2,edition=53,entries=[{k:e[k] for k in ['id','name','en']} for e in group],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==53}
for j in jobs:
    for k in ['image','column_boundaries','row_boundaries','edit_prompt','reference_image','edit_history','original_generation_prompt']:
        if k in prior.get(j['id'],{}):j[k]=prior[j['id']][k]
p.write_text(json.dumps([j for j in old if j.get('edition')!=53]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/scholar-myth-v53/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'entries':len(j['entries'])} for j in jobs]))
