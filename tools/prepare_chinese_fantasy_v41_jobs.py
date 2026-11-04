"""Create paired full-body Chinese-fantasy reference sheets."""
from pathlib import Path
import sys,json
sys.pycache_prefix=str(Path(__file__).resolve().parents[1]/'.work/cache/python')
import _bootstrap
from chinese_fantasy_v41 import CATALOG,GROUPS
root=_bootstrap.ROOT
common='''Use case: stylized-concept.
Asset type: Chinese fantasy female COSTUME reference contact sheet for a character design atlas.
Portrait canvas2048x3072 requested, exactly4 columns x4 rows of equal cells, 16 distinct figures. Warm ivory background, thin medium-gray straight grid lines exactly at quarters. Clean polished anime illustration with precise clothing layers, restrained shading and elegant mature adult women age25+. Every cell contains ONE full-body adult standing upright in neutral front or slight three-quarter view. Show head, hair ornaments, sleeves, hems, tails, wings, props and BOTH shoes completely inside each cell, with at least12px free margin at all boundaries. Reduce the whole figure when accessories are wide. Skirts end around the ankles so shoes remain visible. Hands normal and clear, arms resting down except for the listed small held props. Clothing opaque, complete torso coverage; Chinese crossover collars, layered long skirts or robe-and-trousers, pibo scarves and small hairpins. Keep designs varied and accurate to each listed recipe; no generic identical white gowns for everyone. These are ORIGINAL xianxia/fantasy costume designs, not historical reconstructions or copies of TV/anime characters. No Western fairy wings on immortals; only specifically requested animal features on spirits. No scenery, floating cloud bases, extra people, action combat or large glowing effects. Only text: exact cell ID at top left in small legible black type. No titles, names, watermarks or speech bubbles.
'''
jobs=[]
for kind,cid,name,dim in GROUPS:
    es=[e for e in CATALOG if e.get('chinese_fantasy_reference') and e['chinese_fantasy_kind']==kind]
    prefix='XI' if kind=='immortal' else 'YA'
    for i,e in enumerate(es,1):e['id']=f'{prefix}{i:03}'
    direction=('Immortal costume collection: elegant Chinese robes, sleeve-width variation, cloud collars, restrained jade/silver accessories, no animal ears or tails, no wings. Feitian-inspired cell is a fully covered standing dance-costume adaptation.' if kind=='immortal' else 'Chinese spirit-woman costume collection: retain complete HUMAN face, torso, two arms and two legs under complete Chinese clothing. Animal traits only where explicitly listed. Do not add Japanese shrine uniforms, kimono, animal pets or extra limbs. Nine-tail fox cell needs nine distinct compact fur tails with readable individual tips, contained behind the figure inside its own cell.')
    prompt=common+direction+'\nOrdered cells, left to right then top to bottom:\n'+'\n'.join(f"Cell{i+1} ID {e['id']}: {e['name']} / {e['en']}. {e['illustration_recipe']}." for i,e in enumerate(es))
    jobs.append(dict(id='chinese-fantasy-v41-'+kind,category=cid,dimension=dim,title=name+' · 16项配图',image=f"images/sheet-{es[0]['id'].lower()}-{es[-1]['id'].lower()}.png",columns=4,rows=4,edition=41,entries=[{k:e[k] for k in ['id','name','en']} for e in es],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==41}
for j in jobs:
    for f in ['image','edit_prompt','reference_image','edit_history','column_boundaries','row_boundaries']:
        if f in prior.get(j['id'],{}):j[f]=prior[j['id']][f]
    if (root/j['image']).exists() and prior.get(j['id'],{}).get('prompt'):j['prompt']=prior[j['id']]['prompt']
p.write_text(json.dumps([j for j in old if j.get('edition')!=41]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/chinese-fantasy-v41/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'cells':len(j['entries'])} for j in jobs]))
