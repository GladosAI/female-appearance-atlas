"""Wide cells make the lower-body silhouettes readable without cropping."""
from pathlib import Path
import sys,json
sys.pycache_prefix=str(Path(__file__).resolve().parents[1]/'.work/cache/python')
import _bootstrap
from hybrid_forms_v42 import CATALOG,GROUPS
root=_bootstrap.ROOT;es=[e for e in CATALOG if e.get('hybrid_reference')]
for i,e in enumerate(es,1):e['id']=f'HY{i:03}'
common='''Use case: stylized-concept.
Asset type: original fantasy BODY MORPHOLOGY reference atlas, upper-humanoid lower-creature character designs.
Create a portrait canvas1536x2048 with exactly2 columns by4 rows =8 wide landscape cells. Thin medium-gray straight grid rules at x50% and y25%,50%,75%. All equal-size cells on warm ivory. Each cell contains ONE complete mature adult female fantasy being age25+, seen head to entire tail/tailfin/hooves/claws/roots. WIDE full-body side-three-quarter compositions: a long creature body extends sideways while human torso rises upright. Keep every appendage inside its own cell with at least20px free margins. Scale whole character down to fit wide lower body. Clean polished anime illustration, restrained shading, clear form boundaries. Ordinary fully opaque long-sleeve tops or jackets cover the ENTIRE HUMAN UPPER BODY from neck to waist; the garment stops at the waist so the anatomical transition is visible. Creature lower body is natural scales/fur/feathers/chitin/gel/wood, NOT a skirt, wearable tail, prop, costume or transformation scene. Upper torso continuous with the specified lower body. No human legs on tail-, quadruped- or root-bodied designs. Exactly one human head, only the listed appendages. Neutral reference pose; no other people, backgrounds, rock bases, action, large effects or extra inset images. Only text is the exact cell ID at the upper left of each cell in small black readable print. No names, titles, logos or watermark. All designs original, not existing fictional characters.
'''
directions={
 'serpent':'All8: full human adult face and upright clothed torso, two normal human arms, waist directly continues into ONE tapering legless snake body. Show ventral scale direction, a single continuous tail path and full tail tip; no second snake head. Coils loose enough to understand their continuation.',
 'aquatic':'All8: clothed human upper torso and human arms, waist directly continues into a single aquatic lower body. Mermaid tailfins or marine flukes must read as BODY structures, not mermaid-shaped dresses. Show every entire fin and tail tip; no human legs or concealed feet. Thin fin tissue may be translucent, all human clothing and torso fully opaque.',
 'terrestrial':'Cells1-6: upright human torso replaces the quadruped head/neck at the FRONT SHOULDERS of its horizontal animal body. FOUR animal legs are visible and rooted correctly, no second animal head and no human legs. Use clear three-quarter side view. Cell7: human arms + feathered bird lower body + TWO bird legs. Cell8: feathered wings REPLACE human arms, TWO bird legs below; do not add human arms.',
 'unusual':'Clearly separate the human torso/two normal arms from creature lower body. Arthropod cells show a compact thorax/abdomen, supported jointed limbs and no human legs. Tentacles are freely displayed lower-body anatomy only. Jellyfish bell, gel blob and root stump must be actual connected lower bodies, not clothes, props or scenery. Avoid making all8 look like long skirts.'}
jobs=[]
for kind,dim in GROUPS:
    group=[e for e in es if e['hybrid_group']==kind];assert len(group)==8
    prompt=common+directions[kind]+'\nOrdered cells left-to-right then downward:\n'+'\n'.join(f"Cell{i+1} ID {e['id']}: {e['name']} / {e['en']}. Connection: {e['hybrid_connection']}. Support: {e['hybrid_support']}. {e['illustration_recipe']}." for i,e in enumerate(group))
    jobs.append(dict(id='hybrid-v42-'+kind,category='hybrid_body_forms',dimension=dim,title=dim+' · 8项全身结构',image=f"images/sheet-{group[0]['id'].lower()}-{group[-1]['id'].lower()}.png",columns=2,rows=4,edition=42,entries=[{k:e[k] for k in ['id','name','en']} for e in group],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==42}
for j in jobs:
    for f in ['image','edit_prompt','reference_image','edit_history','column_boundaries','row_boundaries']:
        if f in prior.get(j['id'],{}):j[f]=prior[j['id']][f]
    if (root/j['image']).exists() and prior.get(j['id'],{}).get('prompt'):j['prompt']=prior[j['id']]['prompt']
p.write_text(json.dumps([j for j in old if j.get('edition')!=42]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/hybrid-v42/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'cells':len(j['entries'])} for j in jobs]))
