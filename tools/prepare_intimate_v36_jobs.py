"""Prepare additional thematic apparel contact sheets, preserving published entries."""
import sys,json
from pathlib import Path
sys.pycache_prefix=str(Path(__file__).resolve().parents[1]/'.work/cache/python')
import _bootstrap
from intimate_expansion_v36 import CATALOG,GROUPS
root=_bootstrap.ROOT
entries=[e for e in CATALOG if e.get('intimate_theme_reference')]
for index,e in enumerate(entries,17):e['id']=f'IN{index:03}'
common='''Use case: product-mockup.
Asset type: original themed costume/apparel design atlas, presented on neutral adult tailoring mannequins.
Primary request: exactly16 DISTINCT complete apparel ensembles in the specified order, one per cell. Product-design presentation, with fashion construction and accessories clearly legible.
Layout: PORTRAIT 2048x3072 canvas, EXACTLY4 equal columns by4 equal rows. Tall equal cells separated by thin straight light-gray lines at the quarter axes. Row-major left to right, top to bottom. Each full mannequin from its blank oval head through both shoes fits entirely within its cell, with roomy margins. Head accessories, wings, capes and feet must not be cut off or overlap the next cell. Put ONLY the exact ID in small dark crisp sans-serif at the top left of each cell. No title, no footer, no extra panels, no descriptive text, no logos or watermarks.
Subject/display: featureless matte neutral-gray ADULT female-size clothing-display mannequins, mature adult proportions age25+ only. Smooth artificial material with no facial features or anatomical surface detail. Natural upright catalog standing pose, arms relaxed at the sides, symmetrical weight, no gestures or interactions. These are clothing products on stands, no living people, no erotic scene or seductive presentation.
Garments: every chest and pelvic garment is fully OPAQUE and lined. High-waisted tailored shorts or a fully covered bodysuit base in every ensemble, with the specified skirt/robe layer when present. Lace, mesh or clear PVC only as an outer layer over solid opaque clothing. No exposed breasts, nipples, genital detail, see-through underwear, restraints or suggestive poses. Clothing ribbons are sewn decorations, never binding the mannequin. Do not add props not requested.
Style: polished 2D anime/game fashion-design illustration, precise clean linework, readable seams, folds and material highlights, restrained cel shading, pale warm ivory background and consistent neutral lighting. Preserve the same mannequin scale across cells. Distinguish the themes by garment silhouette, headpiece, fabric, palette and small accessories, rather than minor color changes alone.
'''
directions={
 GROUPS[0]:'Romantic and retro evening themes: corsetry, opaque slip dresses, tailored shorts, decorative period-inspired collars, fabric panels and restrained themed trim. Original stage/fashion reinterpretations, not historical reconstructions. Every row must be visibly different.',
 GROUPS[1]:'Fantasy, festival and stage themes: distinguish small costume horns, wings, fairy leaf/petal panels, frost crowns, celestial embroidery and seasonal headpieces. All are removable fashion accessories on blank gray adult mannequins. Wings stay small enough to fit in each cell. No creatures, people, weapons, fantasy anatomy or backgrounds.',
 GROUPS[2]:'Urban profession-inspired and material-themed fashion: parody stage costume details, no real brands, official insignia or emblems. No tools, weapons or medical instruments. Distinguish collar/scarf/cap silhouettes, faux leather, denim, velvet, silver lame and clear outer PVC with an opaque bodysuit underneath.'}
jobs=[]
for dim in GROUPS:
    es=[e for e in entries if e['dimension']==dim];assert len(es)==16
    prompt=common+'Theme direction: '+directions[dim]+'\nOrdered cells:\n'+'\n'.join(f"Cell{i+1}, ID {e['id']}: {e['en']} / {e['name']}. Garments: {e['description']}" for i,e in enumerate(es))
    jobs.append(dict(id='intimate-v36-'+es[0]['id'].lower(),category='intimate_costumes',dimension=dim,title=dim+' · 16套',image=f"images/sheet-{es[0]['id'].lower()}-{es[-1]['id'].lower()}.png",columns=4,rows=4,edition=36,entries=[{k:e[k] for k in ['id','name','en']} for e in es],prompt=prompt))
path=root/'source/image-jobs.json';old=json.loads(path.read_text(encoding='utf-8'));previous={j['id']:j for j in old if j.get('edition')==36}
for job in jobs:
    for field in ['image','reference_image','edit_prompt','column_boundaries','row_boundaries']:
        if field in previous.get(job['id'],{}):job[field]=previous[job['id']][field]
path.write_text(json.dumps([j for j in old if j.get('edition')!=36]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
output=root/'.work/verification/intimate-v36/jobs.json';output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'image':j['image'],'count':len(j['entries'])} for j in jobs]))
