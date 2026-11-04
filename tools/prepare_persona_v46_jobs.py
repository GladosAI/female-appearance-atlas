"""Prepare twelve four-cell adult styling and performance comparison sheets."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent));import _bootstrap
import build_atlas_v2
import persona_looks_v46 as content
root=_bootstrap.ROOT
counts={'persona_looks':48,'coverage_looks':8};prefix={'persona_looks':'QL','coverage_looks':'LC'}
es=[]
for e in content.NEW_ENTRIES:
    counts[e['category']]+=1
    es.append(dict(e,id=prefix[e['category']]+f"{counts[e['category']]:03}"))
common='''Use case: stylized-concept. Asset: original female character appearance atlas, full-body fashion and facial-acting reference.
Create EXACTLY TWO COLUMNS by TWO ROWS, four LARGE portrait cells, order top-left, top-right, bottom-left, bottom-right. Canvas portrait approximately2:3. Thin straight gray separator rules at center x and center y, no header or title. Label each cell with its EXACT short ID in small black plain text at top left, no other text, no watermarks or logos. Pale warm ivory cell background and consistent soft studio lighting. Polished detailed anime-adjacent adult fashion illustration, delicate controlled outlines, nuanced faces, crisp fabric construction, beautifully coherent color palettes, fully adult proportions and anatomy. Every character is CLEARLY an ADULT woman aged25–35, mature face, approximately7-head proportions. Cute or childish labels concern styling and acting by adults.
FRAMING: one complete standing adult woman per cell. Show entire hairstyle, both hands or naturally occluded hands, and COMPLETE shoes and feet. Leave at least6percent clear margin on ALL sides and space under ID. Do not cut hair, fingers, heel, toe or dress at grid lines. Keep figure large within margins; face readable. Each panel is an individual complete outfit. Exactly four people total. Natural correct hands, no extra limbs, no additional inset faces.
Express the requested impression through brow/eye/lip shape, gaze, hands, shoulders, posture and coordinated clothing; do not rely only on hair or body shape. Keep differences readable but tasteful and restrained. All garments are opaque at private areas, no explicit nudity or sexual activity, no sexualized posing. Neutral studio fashion-study presentation.
'''
jobs=[]
for key,cid,title in content.GROUPS:
    field='persona_group' if cid=='persona_looks' else 'coverage_group'
    group=[e for e in es if e.get(field)==key];assert len(group)==4
    prompt=common+'\nFour ordered panels:\n'+'\n'.join(f"Panel{i+1}, ID {e['id']}: {e['en']}. {e['illustration_recipe']}." for i,e in enumerate(group))
    jobs.append(dict(id='persona-v46-'+key,category=cid,dimension=title,title=title+' · 4项',image=f"images/sheet-{group[0]['id'].lower()}-{group[-1]['id'].lower()}.png",columns=2,rows=2,edition=46,entries=[{k:e[k] for k in ['id','name','en']} for e in group],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==46}
for j in jobs:
    for k in ['image','column_boundaries','row_boundaries','edit_prompt','reference_image','edit_history']:
        if k in prior.get(j['id'],{}):j[k]=prior[j['id']][k]
p.write_text(json.dumps([j for j in old if j.get('edition')!=46]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/persona-v46/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'entries':len(j['entries'])} for j in jobs]))
