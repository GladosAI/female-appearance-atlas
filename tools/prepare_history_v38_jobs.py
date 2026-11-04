"""Prepare three chronological costume sheets, retaining prior saved revisions."""
from pathlib import Path
import sys,json
sys.pycache_prefix=str(Path(__file__).resolve().parents[1]/'.work/cache/python')
import _bootstrap
from fashion_history_v38 import CATALOG,TRACKS
root=_bootstrap.ROOT
entries=[e for e in CATALOG if e.get('fashion_history_reference')]
for i,e in enumerate(entries,1):e['id']=f'FH{i:03}'
common='''Use case: historical-scene / stylized-concept.
Asset type: a visual historical female clothing reference atlas for original anime/game character design.
Primary request: EXACTLY 16 complete adult women wearing SIXTEEN clearly distinct historical outfits, IN THE ORDER specified below. Costume structure is the subject. Same mature adult body proportions, calm face, stable natural standing pose and consistent scale throughout; historically appropriate hairstyles and a few helpful clothing accessories. NOT a modern fantasy costume lineup. Use the specified period features rather than mixing all eras together.
Canvas: portrait, 2048x3072 if available. EXACTLY 4 equal columns by 4 equal rows, thin continuous pale-gray grid rules at the exact quarter axes. Top left of each cell: ONLY its exact FH ID in small dark lettering; no other words, no dates, no heading, no text outside the cells. Read left to right then down chronologically. Generous margins: whole head, hair or hat, BOTH hands, entire garments, hem, both shoes, and any small train remain INSIDE the own cell. Never clip a skirt or hat at a grid boundary. Keep figures similar height even when skirts vary in width; scale widest skirts down as needed.
Style: high-quality original 2D anime historical-fashion illustration, mature adult women aged 25-35, precise clean lines, restrained cel shading, realistic garment layering and textile folds. Warm ivory background, subtle consistent ground contact, gentle studio lighting. Mostly front or three-quarter front view, except where profile makes the garment change more legible. Different muted costume colors aid comparison, not claims of exact archaeological fabric colors.
Coverage: fully opaque outer clothing and appropriate covered underlayers, no transparency, no nudity, no exposed underwear, no sexual poses. Historically lower necklines get a modest plausible opaque inset or fichu without changing the primary skirt/sleeve silhouette. Plain original fabrics, subtle small motifs only; no brands or copied artworks.
Anatomy: exactly two arms, two hands, two legs and two feet for every woman. Natural upright pose, hands separated from torso enough to read seams, no props obscuring the outfit. This is a clothing development comparison: prioritize waist placement, collar, sleeves, skirt support direction and hem length.
'''
jobs=[]
for track in TRACKS:
    es=[e for e in entries if e['history_track']==track['id']];assert len(es)==16
    direction='Chinese regional development: distinguish flat wrap robe, blouse/skirt separation, narrow versus broad Tang sleeves, Song OPEN straight beizi, Ming jackets and skirts, Qing Manchu long robe versus Han jacket/skirt, loose 1920s versus shaped 1930s qipao. No modern Japanese kimono obi or generic fantasy hanfu for every cell.' if track['id']=='china' else 'Costume history silhouette comparison: keep peplos overfold versus chiton pleating, medieval gowns versus farthingale cone, sideways pannier versus circular crinoline versus REAR bustle, then Edwardian blouse/skirt. Bustle cell MUST use side or 3/4 SIDE view to show rear volume, not another round hoop skirt.' if track['id']=='europe' else 'Modern chronology: columnar high waist, dropped waist, bias-cut drape, utility suit, New Look full skirt, sheath, shift, mini, flares, maxi, wrap, broad power shoulders, minimal, grunge, low rise denim, athleisure. Every cell must show the specified distinctive silhouette; avoid making all16 generic dresses or all16 skirts. These are mature adult women, no school or child styling.'
    prompt=common+'Track: '+track['name']+'. Scope: '+track['scope']+'.\n'+direction+'\nOrdered cells:\n'+'\n'.join(f"Cell {i+1} ID {e['id']}: {e['name']} / {e['en']}. Period {e['history_period']}; region {e['history_region']}. {e['history_recipe']}" for i,e in enumerate(es))
    jobs.append(dict(id='history-v38-'+track['id'],category='fashion_history',dimension=track['name'],title=track['name']+' · 16项时间顺序对照',image=f"images/sheet-{es[0]['id'].lower()}-{es[-1]['id'].lower()}.png",columns=4,rows=4,edition=38,entries=[{k:e[k] for k in ['id','name','en']} for e in es],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==38}
for j in jobs:
    for field in ['image','edit_prompt','reference_image','edit_history','column_boundaries','row_boundaries']:
        if field in prior.get(j['id'],{}):j[field]=prior[j['id']][field]
p.write_text(json.dumps([j for j in old if j.get('edition')!=38]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/history-v38/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'image':j['image'],'cells':len(j['entries'])} for j in jobs]))
