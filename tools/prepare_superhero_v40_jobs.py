"""Prepare two illustrated superhero sheets with stable IDs."""
from pathlib import Path
import sys, json
sys.pycache_prefix = str(Path(__file__).resolve().parents[1]/'.work/cache/python')
import _bootstrap
from superhero_expansion_v40 import CATALOG, CLASSIC, ORIGINAL
root = _bootstrap.ROOT
entries = [e for e in CATALOG if e.get('superhero_reference')]
for i,e in enumerate(entries,1): e['id'] = f'SH{i:03}'
common = '''Use case: stylized-concept.
Asset type: illustrated female superhero COSTUME reference atlas contact sheet.
Create a portrait 4-column by 4-row grid, exactly16 distinct full-body figures on warm ivory. Thin medium-gray straight dividing rules at the quarters; identical cell sizes. Read left to right, top to bottom. Clean polished anime/comic illustration with accurate clothing construction, restrained shading, varied mature adult women, upright neutral three-quarter or front views. No actor likeness. Each figure head to toe INCLUDING cape, hat, wings, props and boots must fit with at least12px empty margin on all four sides; scale down broad wings and long capes. All figures stand, hands clearly formed and normally down or on hip. No scene, pedestal, action combat, foreground props, other people or large effects. Clothes opaque, normal superhero costume fitting, no sexual posing or exaggerated anatomy. Keep EACH costume distinct; do not blend adjacent characters. Only printed text is the exact cell ID in small readable black type at top left. No title, names, watermark or explanatory text. High clarity for individual cropped cards. Requested canvas2048x3072.
'''
jobs=[]
for kind,dim in [('silhouette',CLASSIC),('original',ORIGINAL)]:
    es=[e for e in entries if e['superhero_kind']==kind]
    direction = 'All32 designs are ORIGINAL adult superhero costume archetypes. Use only the specified original clothes and original symbols, no existing franchise emblems or actor likenesses.'
    prompt=common+direction+'\nOrdered cells:\n'+'\n'.join(f"Cell {i+1}, ID {e['id']}: {e['name']} / {e['en']}. {e['illustration_recipe']}." for i,e in enumerate(es))
    jobs.append(dict(id='superhero-v40-'+kind,category='superhero_outfits',dimension=dim,title=dim+' · 16项配图',image=f"images/sheet-{es[0]['id'].lower()}-{es[-1]['id'].lower()}.png",columns=4,rows=4,edition=40,entries=[{k:e[k] for k in ['id','name','en']} for e in es],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==40}
for j in jobs:
    for field in ['image','edit_prompt','reference_image','edit_history','column_boundaries','row_boundaries']:
        if field in prior.get(j['id'],{}):j[field]=prior[j['id']][field]
    if (root/j['image']).exists() and prior.get(j['id'],{}).get('prompt'):
        j['prompt']=prior[j['id']]['prompt']
p.write_text(json.dumps([j for j in old if j.get('edition')!=40]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/superhero-v40/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'cells':len(j['entries'])} for j in jobs]))
