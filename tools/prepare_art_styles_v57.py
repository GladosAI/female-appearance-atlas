"""Register the original four-panel art-style sheets and their stable IDs."""
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _bootstrap
import art_styles_v57 as content

root = _bootstrap.ROOT
prefixes = ['XA', 'XB', 'XC', 'XD', 'XE', 'XF']
common = ('Create an ORIGINAL art-style comparison reference sheet, a LANDSCAPE 3:2 canvas with EXACTLY 2 columns and 2 rows of FOUR equal panels separated by thin dark gray straight lines, no inset or additional panels. Each panel has one clear head-and-shoulders portrait of a fully clothed adult woman with brown shoulder length hair, pale simple blouse, neutral background, framed comfortably with entire head inside its panel. The SAME subject and composition in all four panels: the purpose is to compare the medium and rendering, not the outfit. No words, no lettering, no numbers, no logos, no watermark. Each quadrant must be independently and accurately rendered in its prescribed visually distinct style; do not blend the four styles into a common realistic rendering. ')
recipes = [
    'TOP LEFT cel-shaded Japanese animation, clear ink outlines and 2 or 3 flat blocks of shadow, saturated solid color; TOP RIGHT 1990s hand-painted cel anime with vintage slightly grainy painted-cell surface, bold contour and soft pastel film appearance; BOTTOM LEFT modern anime light-novel illustration with fine linework and radiant translucent colored highlights, layered precise detail; BOTTOM RIGHT chibi super-deformed anime with large head, small body, graphic simple outlines and flat colors.',
    'TOP LEFT crisp low-resolution pixel art with large square stepped pixels, small limited palette, no antialiasing; TOP RIGHT high-end stylized 3D game character render with sculpted rounded volumes, polished materials, soft studio lighting; BOTTOM LEFT painterly game concept art, visible broad brush strokes, designed edges and tonal composition; BOTTOM RIGHT graphic visual-novel sprite art with clean delicate outlines, flat-color cel shading and clear front-facing bust.',
    'TOP LEFT natural window-light photographic portrait, true skin texture, realistic lens depth; TOP RIGHT black-and-white film photography, visible grain, analog tonal range, no color; BOTTOM LEFT editorial studio fashion photography, high-key white seamless backdrop and sculpted softbox light; BOTTOM RIGHT instant-film photograph, soft faded warm color, subtle film texture and gentle washed highlights.',
    'TOP LEFT transparent watercolor illustration, translucent pigment washes, soft pigment bleeds and textured paper; TOP RIGHT oil painting on canvas with unmistakable thick impasto brush texture and rich opaque colors; BOTTOM LEFT graphite pencil drawing on white paper with precise contour and soft gray crosshatching, no color; BOTTOM RIGHT traditional Chinese ink-wash portrait with black ink and faint muted wash on fibrous rice paper, expressive brush lines.',
    'TOP LEFT flat vector poster art with sharp geometric blocks, limited bold palette and no gradients; TOP RIGHT vintage screen print with two-color overlapping ink and visible halftone dots; BOTTOM LEFT woodcut relief engraving with strong hand-carved black-and-white lines and dense hatching; BOTTOM RIGHT paper collage illustration with visibly layered torn colored paper edges and cut shapes.',
    'TOP LEFT soft pastel chalk artwork with dusty dry pigment texture on colored paper; TOP RIGHT Japanese manga black-and-white ink drawing with crisp contours and prominent screentone dot patterns; BOTTOM LEFT soft digital airbrush painting with smooth light gradients and subtle glowing color; BOTTOM RIGHT stylized low-poly 3D character made of clearly visible large polygon facets and flat triangular faces.',
]
jobs = []
boards = []
for (cid, name, guide, entries), prefix, recipe in zip(content.GROUPS, prefixes, recipes):
    items = [dict(id=f'{prefix}{i:03}', name=e[0], en=e[1]) for i, e in enumerate(entries, 1)]
    job = dict(id='art-v57-' + cid, category=cid, dimension=name, title=name + ' · 4项',
               image=f'images/sheet-{prefix.lower()}001-{prefix.lower()}004.png', columns=2, rows=2,
               edition=57, column_boundaries=[0, 768, 1536], row_boundaries=[0, 512, 1024],
               entries=items, prompt=common + recipe)
    jobs.append(job)
    boards.append(dict(id=job['id'], category=cid, dimension=name, title=job['title'], image=job['image'],
                       columns=2, rows=2, prompt=job['prompt'], edition=57, width=1536, height=1024,
                       origin='AI-generated style study; photography styles are simulated',
                       qa_status='visually_reviewed', column_boundaries=job['column_boundaries'],
                       row_boundaries=job['row_boundaries'],
                       items=[dict(label=e['id'], entry_id=e['id'], name=e['name']) for e in items]))

for filename, records in [('image-jobs.json', jobs), ('extra-illustrations.json', boards)]:
    path = root / 'source' / filename
    old = json.loads(path.read_text(encoding='utf-8'))
    path.write_text(json.dumps([x for x in old if x.get('edition') != 57] + records,
                               ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

path = root / 'source/navigation.json'
nav = json.loads(path.read_text(encoding='utf-8'))
sections = [
    dict(id='art_animation_game', name='动漫与游戏', categories=['art_animation', 'art_game']),
    dict(id='art_photo_media', name='摄影与传统绘画', categories=['art_photography', 'art_traditional']),
    dict(id='art_graphic_experiment', name='平面印刷与实验表现', categories=['art_graphic', 'art_mixed']),
]
group = dict(id='art_styles', name='画风与视觉表现',
             note='按动画、游戏、摄影、绘画和印刷等表现手法比较角色图像；与服装风格分开。摄影类为生成模拟图。',
             categories=[c for s in sections for c in s['categories']], sections=sections)
nav['groups'] = [g for g in nav['groups'] if g['id'] != group['id']] + [group]
path.write_text(json.dumps(nav, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Registered {len(boards)} sheets and {sum(len(g[3]) for g in content.GROUPS)} art styles')
