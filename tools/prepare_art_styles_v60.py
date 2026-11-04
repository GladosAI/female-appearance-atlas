"""Register generated art-style sheets with individually measured panel boundaries."""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _bootstrap
import art_styles_v60 as content

root = _bootstrap.ROOT
ids = ['XA007','XA008','XB007','XJ007','XD005','XD006','XD007','XE005',
       'XC007','XC008','XC009','XC010','XB008','XE006','XH005','XA009']
entries = [dict(id=i,name=e['name'],en=e['en']) for i,e in zip(ids,content.NEW_ENTRIES)]
portrait = ('Original character art-style atlas. Create a LANDSCAPE 3:2 image exactly 2 columns by 2 rows with a fine separating line, four distinct panels in reading order. In each panel one clearly adult woman, portrait head and shoulders with full head in frame, modest opaque simple clothes, no writing, no watermark, no recognizable existing characters. Render each panel unmistakably in its assigned style. ')
fullbody = ('Original character art-style atlas. PORTRAIT 2:3 canvas with EXACTLY 2 columns and 2 rows, four distinct tall panels. Each cell depicts one clearly adult woman standing, entire body from crown to complete shoes shown inside cell with margin; simple modest white blouse, dark trousers and shoes. All limbs remain within cell. No lettering, no logo, no watermark, no copyrighted characters. Render each panel unmistakably in its assigned style. ')
styles = [
 'TOP LEFT nostalgic Japanese shojo manga, large sparkling eyes, elaborate ink lashes, flowers and screen tone; TOP RIGHT expressive Western hand-drawn 2D television cartoon with simplified graphic features and clean bold ink outlines; BOTTOM LEFT strict black-and-white 1-bit pixel art of character with large crisp square pixels and limited checkerboard dithering, no gray gradients; BOTTOM RIGHT 3D anime-style cel-shaded game render with simplified clear hard-edged shadow bands, visibly three-dimensional volumes.',
 'TOP LEFT traditional Chinese gongbi fine brush painting, deliberate delicate ink contour and carefully layered mineral colors on fibrous silk, intricate yet natural; TOP RIGHT Japanese ukiyo-e woodblock inspired illustration with flat colors, bold carved outlines, paper and visible woodblock print grain; BOTTOM LEFT impressionist oil painting in distinct broken brushstrokes and lively reflected daylight, painterly not photo; BOTTOM RIGHT Art Nouveau decorative illustration with elegant organic curves, floral ornamental border, graceful linework and subdued jewel colors.',
 'TOP LEFT film noir photographic style simulated black and white with dramatically directional high-contrast studio lighting and deep shadows; TOP RIGHT candid street-fashion editorial photograph simulation with urban backdrop and natural daylight; BOTTOM LEFT dreamy soft-focus pastel portrait photography simulation, diffused light, delicate hazy glow and gentle color; BOTTOM RIGHT false-color infrared photographic simulation with pale white foliage and unexpected crimson foliage tones, clearly photographic but surreal color.',
 'TOP LEFT voxel art, a visibly 3D character constructed from chunky cubic blocks and blocky silhouette; TOP RIGHT luminous stained glass artwork, lead cames outlining separate translucent colored glass pieces; BOTTOM LEFT blue ballpoint pen drawing on white paper with distinctly blue hatched strokes; BOTTOM RIGHT Western feature-animation inspired stylized 3D character with expressive exaggerated face and soft polished 3D volumes, visibly different from voxel.',
]
# Each source grid was measured; illustrations are not necessarily split at 50%.
portrait_y = [512,513,511,512]
fullbody_y = [755,718,725,748]
jobs, boards = [], []
for group in range(4):
    for kind in ['portrait','fullbody']:
        is_full = kind=='fullbody'
        role = 'fullbody_reference' if is_full else 'primary'
        width,height = (1024,1536) if is_full else (1536,1024)
        y = fullbody_y[group] if is_full else portrait_y[group]
        es = entries[group*4:group*4+4]
        title = f'画风扩充 {group+1} · ' + ('全身' if is_full else '人像近景')
        job = dict(id=f'art-v60-{group+1}-{kind}',category='art_styles',dimension='画风扩充',title=title,
                   image=f'images/sheet-art-v60-{group+1}-{kind}.png',columns=2,rows=2,
                   edition=60,role=role,column_boundaries=[0,width//2,width],row_boundaries=[0,y,height],
                   entries=es,prompt=(fullbody if is_full else portrait)+styles[group])
        board = dict(**{k:job[k] for k in ['id','category','dimension','title','image','columns','rows','edition','role','column_boundaries','row_boundaries','prompt']},
                     width=width,height=height,origin='AI-generated style study; photography is simulated',qa_status='visually_reviewed',
                     items=[dict(label=e['id'],entry_id=e['id'],name=e['name']) for e in es])
        jobs.append(job);boards.append(board)
for filename,records in [('image-jobs.json',jobs),('extra-illustrations.json',boards)]:
    path=root/'source'/filename
    old=json.loads(path.read_text(encoding='utf-8'))
    path.write_text(json.dumps([x for x in old if x.get('edition')!=60]+records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Registered 16 new styles with portrait and full-body sheets.')
