"""Append six illustrated beauty-reference sheets, preserving all prior job IDs."""
import sys,json
from pathlib import Path
from collections import Counter
sys.pycache_prefix=str(Path(__file__).resolve().parents[1]/'.work/cache/python')
import _bootstrap
import beauty_expansion_v34
root=_bootstrap.ROOT
old=json.loads((root/'data/catalog.json').read_text(encoding='utf-8'))
counts=Counter(e['category'] for e in old['entries'] if not e.get('beauty_expansion_reference'))
prefix={e['category']:e['id'][:2] for e in old['entries']}
rows=[]
for entry in beauty_expansion_v34.CATALOG:
    if not entry.get('beauty_expansion_reference'):continue
    counts[entry['category']]+=1
    rows.append({**entry,'id':prefix[entry['category']]+f"{counts[entry['category']]:03}"})
titles={'hair_texture':'发丝质地、粗细与蓬松层次','hair_color':'自然色阶与染色细分','gaze_laugh':'凝视与憋笑','micro_expression':'日常情绪与细微表情','everyday_makeup':'底妆、腮红与唇妆组合','creative_makeup':'风格妆面与创意彩妆'}
directions={
 'hair_texture':'Full head, all hair and upper shoulders of mature adult women. Hair occupies most of each cell; show fine versus coarse strands, airy versus heavy density, sheen, frizz and curl texture exactly. Dark-brown hair in every cell reduces color distraction. Vary hair shape only as necessary to show the listed surface. Plain opaque high-neck clothing. Leave ample margins around the complete hair silhouette.',
 'hair_color':'Same adult female model and same simple mid-long loose hairstyle in every cell, head and shoulders. Hair occupies most of each cell. Precisely distinguish the named subtle undertones and strand-level color mixes. All hair colors must be clearly different and preserve hair texture. Consistent neutral studio light; no colored light or accessories. Plain opaque high-neck clothing.',
 'gaze_laugh':'Full mature adult female face, eyebrows, both eyes, nose, mouth and chin visible, upper shoulders only. Cells1-8 are GAZE studies: direction and eyelids clearly show each listed gaze. Cells9-16 are SUPPRESSED LAUGHTER: the person is trying not to laugh, raised cheeks and amused eyes with restrained mouth, NOT angry pouting or big open-mouth laughter. Cell11 includes one anatomically correct hand covering the mouth. Neutral dark-brown hair and minimal cosmetics. Every mouth and chin stays inside the cell.',
 'micro_expression':'Full mature adult female facial acting portraits. Clearly coordinate brows, eye direction, eyelids, cheeks and restrained mouth shapes. Show the individual subtle emotional differences from the list; no repeated generic smiles. Full forehead, brows, both eyes and chin must fit inside each cell. Neutral dark-brown hair, minimal makeup and plain opaque high-neck clothing.',
 'everyday_makeup':'FULL FACE cosmetics on mature adult women, forehead through chin with a little collar context, clean hair pulled back. Show the exact foundation finish, blush placement, lip color and lip finish described. Faces large enough to clearly see each blush/lip distinction. Cells1-15 same light-medium neutral skin and same adult model; cell16 deep-brown skin with complementary gold/copper cosmetics. Plain opaque high-neck clothing. No objects or cosmetic products.',
 'creative_makeup':'FULL FACE creative cosmetics on mature adult women, forehead through chin with a little collar context, hair pulled back. Every listed creative placement and color scheme visible, including lips, brows, cheeks and jewels when specified. No masks hiding the makeup. Tiny pearls/rhinestones/foil only in specified cells, delicately placed. Clear sophisticated fashion illustration, no gore, no branded character costume or resemblance.'}
common='''Use case: stylized-concept.
Asset type: original anime/game female character-design atlas contact sheet.
Primary request: illustrate EXACTLY 16 DISTINCT ordered catalog examples faithfully.
Layout: SQUARE 2048x2048 canvas, EXACTLY 4 EQUAL COLUMNS by 4 EQUAL ROWS. Thin straight light-gray grid rules at exactly quarter axes; regular equal cells with generous internal margins. Row-major reading left to right then down. NO title, NO footer, NO extra inset panels. Put only the exact ID in small dark crisp sans-serif at top left of each cell; no other text.
Style: polished professional 2D anime reference drawing, clean fine outlines, restrained cel shading, warm ivory backgrounds, natural adult facial anatomy. Original mature ADULT women age25-45 only, nonsexual everyday reference portraits. Fine details remain legible at thumbnail scale. No watermark or logos, no generic symbols, no overlapping cells. Each named difference must actually be observable.
'''
jobs=[]
for kind,title in titles.items():
    entries=[e for e in rows if e['beauty_kind']==kind];assert len(entries)==16
    prompt=common+'Subject direction: '+directions[kind]+'\nSpecific ordered cells:\n'+'\n'.join(f"Cell {i+1}, label {e['id']}: {e['en']} / {e['name']}. Visible feature: {e['description']}" for i,e in enumerate(entries))+'\nCritical: correct ID, exact row-major sequence and equal4x4 grid; full feature fits within its own cell. These are individual vocabulary illustrations, not one scene.'
    jobs.append({'id':'beauty-v34-'+kind.replace('_','-'),'category':'face_emotions' if kind=='gaze_laugh' else entries[0]['category'],'dimension':title,'title':title+' · 16项','image':f"images/sheet-{entries[0]['id'].lower()}-{entries[-1]['id'].lower()}.png",'columns':4,'rows':4,'edition':34,'entries':[{k:e[k] for k in ['id','name','en']} for e in entries],'prompt':prompt})
path=root/'source/image-jobs.json';existing=json.loads(path.read_text(encoding='utf-8'));existing=[j for j in existing if j.get('edition')!=34];path.write_text(json.dumps(existing+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
output=root/'.work/verification/v34/jobs.json';output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'image':j['image'],'entries':[e['id'] for e in j['entries']]} for j in jobs]))
