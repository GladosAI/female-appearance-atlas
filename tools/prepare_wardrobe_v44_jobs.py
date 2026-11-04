"""Prepare twelve roomy 8-cell product reference sheets."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent));import _bootstrap
from catalog_content import CATALOG
import build_atlas_v2
import wardrobe_parts_v44 as content
root=_bootstrap.ROOT
counts={'footwear':46,'hosiery':96,'gloves':32};prefix={'footwear':'FW','hosiery':'SO','gloves':'GL'}
es=[]
for e in content.NEW_ENTRIES:
    counts[e['category']]+=1
    es.append(dict(e,id=prefix[e['category']]+f"{counts[e['category']]:03}"))
common='''Use case: product-mockup. Asset: a women's character-design reference sheet.
Create EXACTLY TWO COLUMNS by FOUR ROWS, eight LARGE WIDE rectangular cells, read left to right then down. The grid is2x4, NOT4x2. Canvas portrait approximately3:4. Thin straight gray rules separating the8 cells, no header or outer title. Label each cell with its EXACT short ID at top left. No other text, no brands or watermarks. Clean anime-adjacent realistic fashion product illustration, fine controlled outlines, precise material shading, pale warm ivory background, consistent diffuse studio lighting.
CRITICAL FRAMING: every COMPLETE product, heel, toe, sole, shaft opening, glove cuff and fingertip stays INSIDE its own cell with at least6percent blank margin on ALL sides, leaving space under the ID. Scale tall objects DOWN, NEVER crop them or let them cross grid rules. No floating disconnected straps, melted heels, extra fingers or feet. Show pairs where specified. Gray mannequins are smooth inanimate display forms, adult female sizing; no faces or whole people. Hosiery on gray forms has no anatomical crotch detail and no body posing. Technical-looking sports items are visual costume studies only. Do not reuse one product for several cells when recipes differ.
'''
jobs=[]
for key,cid,dim in content.GROUPS:
    group=[e for e in es if e['part_group']==key]
    prompt=common+'\nEight ordered cells:\n'+'\n'.join(f"Cell{i+1}, ID {e['id']}: {e['en']}. {e['illustration_recipe']}." for i,e in enumerate(group))
    jobs.append(dict(id='wardrobe-v44-'+key,category=cid,dimension=dim,title=dim+' · 8项',image=f"images/sheet-{group[0]['id'].lower()}-{group[-1]['id'].lower()}.png",columns=2,rows=4,edition=44,entries=[{k:e[k] for k in ['id','name','en']} for e in group],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==44}
for j in jobs:
    for k in ['image','column_boundaries','row_boundaries','edit_prompt','reference_image','edit_history']:
        if k in prior.get(j['id'],{}):j[k]=prior[j['id']][k]
p.write_text(json.dumps([j for j in old if j.get('edition')!=44]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/wardrobe-v44/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'entries':len(j['entries'])} for j in jobs]))
