"""Prepare the three V35 lip-reference sheets without modifying any earlier IDs."""
import sys,json
from pathlib import Path
sys.pycache_prefix=str(Path(__file__).resolve().parents[1]/'.work/cache/python')
import _bootstrap
from lips_expansion_v35 import CATALOG
root=_bootstrap.ROOT
rows=[e for e in CATALOG if e.get('lip_reference')]
counts={}
for e in rows:
    cid=e['category'];counts[cid]=counts.get(cid,0)+1;e['id']=('LP' if cid=='lips' else 'LM')+f'{counts[cid]:03}'
common='''Use case: stylized-concept.
Asset type: original anime/game adult female facial-design atlas, detailed lower-face studies.
Primary request: EXACTLY sixteen distinct labeled examples, one per equal cell.
Layout: square 2048x2048 canvas, EXACTLY4 columns x4 rows, equal square cells, thin straight light-gray grid at quarter axes. Row-major left to right then down. NO heading, footer, inset, products, hands, or extra images. Only the exact cell ID, small crisp dark sans serif at its top left. No other text, no logos, no watermark.
Subject: original mature ADULT women age25-45 only. Each cell shows a calm lower-face portrait from the base of the nose to the entire chin, with cheek context. The complete mouth and both corners must stay fully within the cell with generous margins. Nonsexual editorial cosmetics/anatomy drawing, neutral resting closed lips unless specified, no tongue, exaggerated pouting or expressions. Warm neutral ivory background and soft consistent studio light.
Style: polished professional 2D anime reference drawing, clean fine outlines, subtle cel shading plus precise cosmetic sheen; believable lip volume and fine texture. Same original adult model and same scale in all cells except explicitly noted skin-tone or profile examples. Actual visible differences are essential; do not substitute identical generic lips.
'''
directions={
 '自然唇形与正侧面轮廓':'Natural unpainted muted rose-brown lips. Cells1-13 are FRONTAL; use neutral closed mouths and distinguish morphology without facial acting. Cells14-16 are STRICT SIDE PROFILE, the whole lower nose, lips and chin visible, facing left. No makeup, gloss, liner, or cosmetic exaggeration. Compare thickness, upper/lower balance, cupid bow, central tubercle, width and resting corners exactly.',
 '唇色与表面质感':'FRONTAL lips in all cells, medium balanced shape held identical. Cells1-8 compare the specified individual lipstick shades and finishes. Cells9-16 compare clear sheen, matte, satin, mirror lacquer, translucent jelly, fine pearl, metallic foil, micro-glitter. Particularly differentiate finish cells10-16 using the same muted ROSE-RED base: matte has no highlights, satin broad soft reflection, mirror has crisp bright streaks, jelly is translucent, pearl evenly shimmers, metallic has foil-like bands, glitter has separate tiny points. NO products or swatches outside the lips.',
 '唇线边界与画法':'FRONTAL lips in all cells. These are techniques applied to medium lips: precise original outline, blurred edges, center-deep and rim-deep gradients, liner contrast, subtle central overline and reduced contour, rounded or sharpened cupid bow, upper/lower and left/right split colors, localized gloss and sheer stain. Make each technique visibly distinct. Cell7 subtle overline, not exaggerated swelling. Cell16 is an adult woman with deep-brown skin. No diagrams, arrows, guide lines or explanatory text.'}
jobs=[]
for dim,direction in directions.items():
    es=[e for e in rows if e['dimension']==dim];assert len(es)==16
    prompt=common+'Specific direction: '+direction+'\nOrdered cells:\n'+'\n'.join(f"Cell{i+1}, ID {e['id']}: {e['en']} / {e['name']}. Visible: {e['description']}" for i,e in enumerate(es))
    jobs.append(dict(id='lips-v35-'+es[0]['id'].lower(),category=es[0]['category'],dimension=dim,title=dim+' · 16项',image=f"images/sheet-{es[0]['id'].lower()}-{es[-1]['id'].lower()}.png",columns=4,rows=4,edition=35,entries=[{k:e[k] for k in ['id','name','en']} for e in es],prompt=prompt))
path=root/'source/image-jobs.json';existing=json.loads(path.read_text(encoding='utf-8'));previous={j['id']:j for j in existing if j.get('edition')==35}
for job in jobs:
    for field in ['image','reference_image','edit_prompt','column_boundaries','row_boundaries']:
        if field in previous.get(job['id'],{}):job[field]=previous[job['id']][field]
existing=[j for j in existing if j.get('edition')!=35];path.write_text(json.dumps(existing+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
output=root/'.work/verification/lips-v35/jobs.json';output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'image':j['image'],'count':len(j['entries'])} for j in jobs]))
