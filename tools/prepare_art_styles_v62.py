"""Register v62 portrait and full-body style sheets with measured grid bounds."""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _bootstrap
import art_styles_v62 as content
root=_bootstrap.ROOT
ids=['XG005','XK007','XK008','XE009','XD010','XE010','XG006','XG007',
     'XB013','XB014','XB015','XB016','XA012','XA013','XA014','XA015']
entries=[dict(id=i,name=e['name'],en=e['en']) for i,e in zip(ids,content.NEW_ENTRIES)]
portrait='Create an ORIGINAL character art style reference sheet, LANDSCAPE 3:2 canvas divided by straight black lines into exactly 2 columns and 2 rows (four panels), each panel one clearly adult woman shown as a head-and-shoulders portrait. All heads completely inside each panel, simple clothing, no text, no logos, no watermark, no preexisting character. Each panel independently rendered in its assigned visual approach: '
full='Create an ORIGINAL character art style reference sheet, PORTRAIT 2:3 canvas divided by straight black lines into exactly 2 columns and 2 rows (four panels), each panel one clearly adult woman standing, complete figure from crown to both complete shoes fully visible with margin, opaque simple ivory blouse and dark full-length trousers. No text, no logos, no watermark, no preexisting character. Each panel independently rendered in its assigned visual approach: '
styles=[
 'TOP LEFT colorful flat-colored comic artwork, simple ink outlines, solid flat color fills and minimal shadows; TOP RIGHT Korean fantasy game illustration with rich painterly thickly layered soft brushwork and dramatic fantasy colors; BOTTOM LEFT hand-drawn dark gothic illustration with expressive black ink, muted colors, melancholy mood and ornamental details; BOTTOM RIGHT warm children\'s illustrated storybook style with soft brushwork, handmade paper texture, simplified gentle forms and warm tones.',
 'TOP LEFT delicate Japanese picture-book watercolor illustration, transparent color washes and paper texture; TOP RIGHT textured editorial illustration made from grainy opaque color shapes and paper grain, understated palette; BOTTOM LEFT vintage newspaper comic-strip style with crisp ink outlines, limited slightly misregistered colors and aged newsprint texture; BOTTOM RIGHT monochrome Japanese ink-brush manga with energetic hand-brushed black strokes and expressive hatching, no screentone dots.',
 'TOP LEFT 2.5D stylized video-game character with believable three-dimensional volume and unmistakable watercolor-painted texture; TOP RIGHT 2.5D pixel-art character mixing clearly visible square pixel-art textures with dimensional three-dimensional game lighting; BOTTOM LEFT 2.5D game character created from layered cut paper with visible stacked depth and soft 3D shadow; BOTTOM RIGHT 2.5D fantasy character key art combining anime face design, detailed fantasy clothing, painterly materials and realistic soft three-dimensional lighting.',
]
ratio_portrait='Create an ORIGINAL LANDSCAPE 3:2 character portrait comparison sheet with EXACTLY four equally sized panels, 2 columns and 2 rows, divided by simple straight dark grid lines. Each panel shows ONE FACE AND UPPER SHOULDERS ONLY, close-up portrait, fully clothed, same mature adult female character design, brunette hair in a simple bun and plain white shirt, plain warm white background; head entirely inside own panel; NO FULL BODY, NO LEGS, NO TEXT, no watermark, no logos. TOP LEFT chibi stylization meant for an adult character with two-head-tall body proportions, extremely enlarged face, very simplified huge expressive eyes. TOP RIGHT mature adult chibi face for three-head-tall body proportions, large expressive eyes but more detailed than top left. BOTTOM LEFT mature adult stylized face for five-head-tall proportions, moderately enlarged eyes and delicately simplified features. BOTTOM RIGHT mature adult face for realistic eight-head-tall fashion proportions, smaller naturalistic eyes and realistic adult facial structure. Show a gradual shift from extreme chibi to semi-realistic, as clear face references for an adult character design atlas.'
ratio_full='Original stylized character-proportion art atlas, portrait 2:3 sheet with four independent equal tall cells in 2 columns and 2 rows, exact thin straight divider lines. All four panels feature the SAME fully clothed adult woman character design, brunette hair tied back, modest long sleeve white top, charcoal trousers and closed shoes, straight-on standing arms relaxed, pure warm-white background. No text, no labels, no insets, no measuring sticks, no logos. Each COMPLETE person is visible top of head through soles entirely within panel with generous margins, no truncated feet or head. TOP LEFT: extremely stylized adult chibi exactly about 2 heads tall, large head equals half entire height; TOP RIGHT: adult chibi about 3 heads tall, head equals one third entire height; BOTTOM LEFT: stylized adult about 5 heads tall, head equals about one fifth of entire height; BOTTOM RIGHT: realistic FASHION ILLUSTRATION proportion about 8 heads tall, distinctly tiny normal-sized head equals one eighth of total height, very long legs and tall adult proportions. The adult fourth figure should have a much smaller head relative to body than the third figure. Comparable simple standing pose, fully opaque clothes. Nonsexual proportion reference, cartoon stylization does not represent age.'
portrait_y=[511,507,511,503]
full_y=[742,730,732,727]
jobs=[];boards=[]
for group in range(4):
    for kind in ['portrait','fullbody']:
        is_full=kind=='fullbody'; role='fullbody_reference' if is_full else 'primary'
        width,height=(1024,1536) if is_full else (1536,1024); y=full_y[group] if is_full else portrait_y[group]
        es=entries[group*4:group*4+4]
        title=('成年角色头身比对照' if group==3 else f'插画漫画与2.5D {group+1}')+' · '+('全身' if is_full else '人像近景')
        prompt=(ratio_full if is_full else ratio_portrait) if group==3 else (full if is_full else portrait)+styles[group]
        j=dict(id=f'art-v62-{group+1}-{kind}',category='art_styles',dimension='头身比画风' if group==3 else '画风扩充',title=title,
               image=f'images/sheet-art-v62-{group+1}-{kind}.png',columns=2,rows=2,edition=62,role=role,
               column_boundaries=[0,width//2,width],row_boundaries=[0,y,height],entries=es,prompt=prompt)
        b=dict(**{k:j[k] for k in ['id','category','dimension','title','image','columns','rows','edition','role','column_boundaries','row_boundaries','prompt']},
               width=width,height=height,origin='AI-generated style study; proportions are approximate',qa_status='visually_reviewed',
               items=[dict(label=e['id'],entry_id=e['id'],name=e['name']) for e in es])
        jobs.append(j);boards.append(b)
for filename,records in [('image-jobs.json',jobs),('extra-illustrations.json',boards)]:
    p=root/'source'/filename;old=json.loads(p.read_text(encoding='utf-8'))
    p.write_text(json.dumps([x for x in old if x.get('edition')!=62]+records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Registered 16 additional art styles, including four approximate adult head proportions.')
