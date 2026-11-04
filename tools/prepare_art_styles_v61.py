"""Register new style sheets and measured image grid boundaries."""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _bootstrap
import art_styles_v61 as content

root = _bootstrap.ROOT
ids = ['XB009','XB010','XB011','XB012','XA010','XA011','XD008','XD009',
       'XC011','XC012','XE007','XE008','XJ008','XJ009','XK005','XK006']
entries = [dict(id=i,name=e['name'],en=e['en']) for i,e in zip(ids,content.NEW_ENTRIES)]
portrait = ('Create an original character art-style atlas sheet, LANDSCAPE 3:2, four equal panels in exactly 2 columns by 2 rows with clear dividing lines. In each panel a clearly adult woman shown in a portrait from the shoulders up, head fully inside its panel. No writing, no watermark, no logos. Render each panel distinctly as assigned: ')
fullbody = ('Create an original character art-style atlas sheet, PORTRAIT 2:3, four equal panels in exactly 2 columns by 2 rows with clear dividing lines. In each panel one fully clothed adult woman, full-body standing, crown to both complete shoes fully within panel with ample blank margins. Simple ivory blouse, opaque dark trousers, shoes. No text, logos, watermarks. Render each panel distinctly as assigned: ')
styles = [
 'TOP LEFT very coarse 16x16-sprite-inspired pixel art, severely simplified head and body with huge clear square pixels and very few colors; TOP RIGHT 32x32-sprite-inspired pixel art, larger square pixel clusters and limited colors but slightly more detail; BOTTOM LEFT 64x64-sprite-inspired pixel art, medium square pixels with clear eyes and color shading; BOTTOM RIGHT 128x128-sprite-inspired pixel art, fine visible square pixels and richer detail. Preserve hard pixel edges and an obvious gradual change in pixel density, do not use smooth photorealism.',
 'TOP LEFT Japanese shonen action manga ink with dynamic hatching, strong angular black outlines and screentone; TOP RIGHT futuristic city anime illustration with bold hand-drawn 1980s science fiction cel animation styling and luminous city; BOTTOM LEFT black charcoal drawing on textured paper with smudges and strong powdery strokes; BOTTOM RIGHT oil pastel crayon drawing with bright waxy color and irregular thick strokes.',
 'TOP LEFT concert spotlight stage portrait photograph simulation, isolated subject lit by a dramatic single warm spotlight with dark backdrop; TOP RIGHT rainy night cinematic street photo simulation with wet pavement reflections and soft neon highlights; BOTTOM LEFT 1960s pop art comic halftone with bold flat primaries and strong black outlines; BOTTOM RIGHT art deco poster, geometric symmetrical metallic gold and dark shapes, flat clean decorative composition.',
 'TOP LEFT jointed articulated ball-jointed fashion doll, clearly visible separate joints at elbows and knees on the full figure, smooth sculpted resin; TOP RIGHT porcelain doll with glossy glazed porcelain head and smoothly glazed material; BOTTOM LEFT modern digital East Asian ink-wash illustration with visible gestural brush strokes and subtle color washes; BOTTOM RIGHT monochrome playful ink doodle character art, rough freehand sketched outlines and expressive crosshatching.',
]
portrait_y = [511,510,509,511]
fullbody_y = [767,749,719,737]
jobs, boards = [], []
for group in range(4):
    for kind in ['portrait','fullbody']:
        is_full=kind=='fullbody'
        role='fullbody_reference' if is_full else 'primary'
        width,height=(1024,1536) if is_full else (1536,1024)
        y=fullbody_y[group] if is_full else portrait_y[group]
        es=entries[group*4:group*4+4]
        title=('像素密度对照' if group==0 else f'画风扩充 {group+1}')+' · '+('全身' if is_full else '人像近景')
        job=dict(id=f'art-v61-{group+1}-{kind}',category='art_styles',dimension='像素尺寸对照' if group==0 else '画风扩充',title=title,
                 image=f'images/sheet-art-v61-{group+1}-{kind}.png',columns=2,rows=2,edition=61,role=role,
                 column_boundaries=[0,width//2,width],row_boundaries=[0,y,height],entries=es,
                 prompt=(fullbody if is_full else portrait)+styles[group])
        board=dict(**{k:job[k] for k in ['id','category','dimension','title','image','columns','rows','edition','role','column_boundaries','row_boundaries','prompt']},
                   width=width,height=height,origin='AI-generated style study; pixel dimensions and photographic effects are simulated',qa_status='visually_reviewed',
                   items=[dict(label=e['id'],entry_id=e['id'],name=e['name']) for e in es])
        jobs.append(job);boards.append(board)
for filename,records in [('image-jobs.json',jobs),('extra-illustrations.json',boards)]:
    path=root/'source'/filename
    old=json.loads(path.read_text(encoding='utf-8'))
    path.write_text(json.dumps([x for x in old if x.get('edition')!=61]+records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Registered 16 new styles with portrait and full-body sheets.')
