"""Register the extra portrait sheets and measured full-body sheet boundaries."""
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _bootstrap
import art_styles_v57 as old
import art_styles_v58 as new

root = _bootstrap.ROOT
prefixes = ['XA', 'XB', 'XC', 'XD', 'XE', 'XF', 'XG', 'XH', 'XK', 'XJ']
# Grid lines are measured from each generated file, not assumed to be at the canvas midpoint.
fullbody_split = [754, 744, 716, 729, 720, 738, 736, 734, 718, 733]
portrait_split = [501, 512, 511, 511]
fullbody_common = ('Create an ORIGINAL character art style study sheet, portrait canvas about 2:3, with EXACTLY 2 columns and 2 rows, FOUR equal tall rectangular panels, thin black lines exactly at the midpoints. Each panel shows ONE clearly adult woman, standing straight, front view, dark shoulder-length brown hair, simple opaque ivory shirt, ankle-length dark trousers, simple shoes, neutral plain background. Every panel MUST fit the ENTIRE figure including the top of head AND both complete shoes with clear blank space above and below, no cropped feet, no sitting, no closeup. Same wardrobe and pose in all four panels. No other people, no insets, no text, no watermarks. Purpose is to compare art styles. Visually distinct style in each panel, faithfully rendered in its given medium. ')
fullbody_recipes = [
    'TOP LEFT: clean Japanese anime cel shading, black ink contours and flat blocks of color and shadow. TOP RIGHT: retro 1990s hand-painted anime cel with mild film grain. BOTTOM LEFT: modern light novel illustration with delicate lines and glowing layered shading. BOTTOM RIGHT: chibi anime stylized full-body super-deformed character with large head and short limbs, complete miniature body and shoes.',
    'TOP LEFT: genuine crisp low resolution pixel art, large hard square pixels and limited colors, no smooth interpolation. TOP RIGHT: polished stylized 3D video game character render, sculpted smooth volumes. BOTTOM LEFT: painterly game concept art, expressive opaque brushstrokes. BOTTOM RIGHT: visual novel anime character full-body sprite with fine lineart and flat shading.',
    'TOP LEFT: natural daylight full-body portrait photograph effect. TOP RIGHT: black-and-white grainy analog film full-body photo effect. BOTTOM LEFT: high-key fashion photography studio full-body shot. BOTTOM RIGHT: warmly faded instant-film full-body portrait photo effect. All are generated simulations.',
    'TOP LEFT: transparent watercolor painting with visible watercolor paper and blooms. TOP RIGHT: impasto oil painting with thick canvas brushstrokes. BOTTOM LEFT: monochrome graphite pencil drawing with crosshatching on paper. BOTTOM RIGHT: Chinese ink wash figure painting on rice paper, expressive black ink brushwork.',
    'TOP LEFT: flat vector illustration with geometric shapes and solid colors. TOP RIGHT: limited two-color screen-printed full-body illustration, overlapping inks and halftone dots. BOTTOM LEFT: monochrome woodcut print with carved linework. BOTTOM RIGHT: torn and cut paper collage with clearly visible layered paper edges.',
    'TOP LEFT: soft colored dry pastel chalk painting with grainy pigment and paper. TOP RIGHT: black-and-white Japanese manga drawing with obvious halftone screentone texture and ink outlines. BOTTOM LEFT: soft digital airbrush with smooth gradients. BOTTOM RIGHT: low-poly 3D model with unmistakable large flat triangular facets.',
    'TOP LEFT: dramatic American superhero comic-book style, bold ink contours and graphic high contrast color. TOP RIGHT: Franco-Belgian bande dessinée clear-line style, precise even outlines and flat clear colors. BOTTOM LEFT: contemporary Korean webtoon illustration, vertical comic linework and polished soft color gradients. BOTTOM RIGHT: Chinese animation-inspired guoman digital ink-and-color full-body character illustration, elegant fine outlines and rich colors.',
    'TOP LEFT: colored pencil illustration with visible hand-drawn parallel strokes on paper. TOP RIGHT: gouache painting with matte opaque brush marks and poster-like color. BOTTOM LEFT: acrylic painting with recognizable energetic brush texture. BOTTOM RIGHT: alcohol marker fashion illustration with visible overlapping marker strokes and ink contours.',
    'TOP LEFT: painterly digital illustration with strong visible brushstrokes and soft edges. TOP RIGHT: semi-painted anime game illustration, clean fine linework, painterly shadows and natural volume. BOTTOM LEFT: neon cyberpunk illustration with cyan and magenta rim light and dark background. BOTTOM RIGHT: dark fantasy illustration with moody chiaroscuro, cool shadows and painterly texture.',
    'TOP LEFT: realistic three dimensional computer-generated full-body character with physically realistic materials, clearly 3D render. TOP RIGHT: handcrafted clay stop-motion puppet, visible sculpted clay texture and rounded shapes. BOTTOM LEFT: felted wool craft doll with visible fuzzy wool fibers and stitched details. BOTTOM RIGHT: pen and ink line drawing of full body with fine ink hatching, on pale paper.',
]
portrait_common = ('Create an ORIGINAL head-and-shoulders art style comparison reference sheet, LANDSCAPE 3:2 canvas with EXACTLY 2 columns and 2 rows, four equal panels separated by thin straight lines. In each panel one clear adult woman with brown shoulder-length hair and simple opaque pale blouse, complete head and shoulders within each panel, neutral plain background, same pose and wardrobe. No lettering, no watermark. Each quadrant visibly and accurately rendered in its specified distinct medium and style. ')
portrait_recipes = [
    'TOP LEFT: bold American superhero comic-book ink and high contrast graphic colors. TOP RIGHT: Franco-Belgian clear-line comics, clean uniform outlines and flat colors. BOTTOM LEFT: modern Korean webtoon illustration, clear thin lines and soft polished gradients. BOTTOM RIGHT: Chinese guoman digital character illustration, elegant fine outlines and rich color.',
    'TOP LEFT: colored pencil illustration with visible individual pencil strokes on paper. TOP RIGHT: matte opaque gouache with brush marks. BOTTOM LEFT: acrylic painting with substantial energetic brush texture. BOTTOM RIGHT: fashion illustration in alcohol marker with visible marker strokes and ink outlines.',
    'TOP LEFT: painterly digital painting with visible loose brush marks. TOP RIGHT: semi-painted anime game art with delicate linework and painterly volumetric shading. BOTTOM LEFT: neon cyberpunk illustration with magenta and cyan rim lighting on a dark background. BOTTOM RIGHT: dark fantasy illustration in dramatic cool chiaroscuro with painterly texture.',
    'TOP LEFT: realistically detailed 3D CGI character with natural physically realistic materials. TOP RIGHT: handmade clay stop-motion puppet with visible sculpted clay texture. BOTTOM LEFT: handmade felted wool doll with visible fuzzy wool fibers and stitching. BOTTOM RIGHT: monochrome pen-and-ink fine line drawing with hatching on paper.',
]
jobs, boards = [], []
def register(group, prefix, is_fullbody, split, prompt):
    cid, name, _, entries = group
    es = [dict(id=f'{prefix}{i:03}', name=e[0], en=e[1]) for i, e in enumerate(entries, 1)]
    suffix = 'fullbody' if is_fullbody else 'portrait'
    role = 'fullbody_reference' if is_fullbody else 'primary'
    width, height = (1024, 1536) if is_fullbody else (1536, 1024)
    xs, ys = [0, width//2, width], [0, split, height]
    title = name + (' · 全身对照' if is_fullbody else ' · 人像近景')
    job = dict(id=f'art-v58-{prefix.lower()}-{suffix}', category=cid, dimension=name, title=title,
               image=f'images/sheet-{prefix.lower()}001-{prefix.lower()}004-{suffix}.png',
               columns=2, rows=2, edition=58, role=role, column_boundaries=xs, row_boundaries=ys,
               entries=es, prompt=prompt)
    board = dict(**{k: job[k] for k in ['id', 'category', 'dimension', 'title', 'image', 'columns', 'rows', 'edition', 'role', 'column_boundaries', 'row_boundaries', 'prompt']},
                 width=width, height=height, origin='AI-generated style study; photography styles are simulated', qa_status='visually_reviewed',
                 items=[dict(label=e['id'], entry_id=e['id'], name=e['name']) for e in es])
    jobs.append(job); boards.append(board)

for i, group in enumerate(old.GROUPS + new.GROUPS):
    if i >= 6:
        register(group, prefixes[i], False, portrait_split[i-6], portrait_common + portrait_recipes[i-6])
    register(group, prefixes[i], True, fullbody_split[i], fullbody_common + fullbody_recipes[i])

for filename, records in [('image-jobs.json', jobs), ('extra-illustrations.json', boards)]:
    path = root / 'source' / filename
    before = json.loads(path.read_text(encoding='utf-8'))
    path.write_text(json.dumps([x for x in before if x.get('edition') != 58] + records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

path = root / 'source/navigation.json'
nav = json.loads(path.read_text(encoding='utf-8'))
group = next(g for g in nav['groups'] if g['id'] == 'art_styles')
additions = {'art_animation_game':['art_comics'], 'art_photo_media':['art_drawing_media'],
             'art_graphic_experiment':['art_digital_moods','art_craft_3d']}
for section in group['sections']:
    for cid in additions.get(section['id'], []):
        if cid not in section['categories']: section['categories'].append(cid)
group['categories'] = [cid for section in group['sections'] for cid in section['categories']]
path.write_text(json.dumps(nav, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Registered {len(boards)} illustrated sheets; {len(new.NEW_ENTRIES)} new styles and 40 full-body references.')
