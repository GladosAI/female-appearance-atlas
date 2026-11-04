"""Register requested art-style comparison sheets and measured panel bounds."""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _bootstrap
import art_styles_v59 as content

root = _bootstrap.ROOT
ids = ['XC005', 'XC006', 'XB005', 'XA005', 'XA006', 'XJ005', 'XJ006', 'XB006']
entries = [dict(id=entry_id, name=e['name'], en=e['en']) for entry_id, e in zip(ids, content.NEW_ENTRIES)]
prompts = [
    'Create an original female character visual-style atlas sheet, LANDSCAPE 3:2 image with 2 columns and 2 rows and four equal panels. Each panel is an individual adult woman bust portrait, fully clothed, simple neat hair, no words, no watermark. Distinguish styles: TOP LEFT Korean and Japanese fashion magazine beauty editorial, polished contemporary beauty styling and bright studio light; TOP RIGHT vintage COLOR 35mm film portrait, soft grain and faded warm tones; BOTTOM LEFT original 2.5D game character key art, anime-influenced forms with richly modeled semi-realistic 3D volume and painterly finish; BOTTOM RIGHT Japanese anime illustration, clean detailed anime lineart with bright cel-shaded and soft illustrative finish. Clearly differentiated aesthetic, no logos or IP characters.',
    'Create an original female character visual-style atlas sheet, LANDSCAPE 3:2 image with 2 columns and 2 rows, four equal panels. Every panel one clearly adult woman bust portrait, fully clothed. No text, logos, watermarks, copyrighted characters. TOP LEFT poetic Japanese animated film look, vivid blue sky, layered sunlit clouds, warm backlighting, fine animated-film linework and dramatic atmospheric light; TOP RIGHT next-generation 3D video-game character render, believable skin and cloth shaders, detailed realistic materials and cinematic light; BOTTOM LEFT collectible designer art toy figurine, stylized vinyl material, sculpted big head and clearly nonliving glossy surface; BOTTOM RIGHT original character design reference art, pure WHITE background, crisp neutral full-color lineart and clean flat coloring, no diagrams.',
    'Create an original female character art-style atlas sheet, PORTRAIT 2:3 image, 2 columns by 2 rows, four separate panels each with one adult woman standing front view, full body including top of head and both whole shoes completely visible with ample space, opaque tasteful blouse and full length dark pants, no logos, no text, no watermark. TOP LEFT polished Korean/Japanese fashion magazine editorial full-body studio photograph simulation, stylish posture and soft studio lighting; TOP RIGHT vintage color 35mm film look with subtle grain and faded warm colors; BOTTOM LEFT 2.5D video game key art mixing expressive anime features with sophisticated semi-realistic painterly volume; BOTTOM RIGHT Japanese anime illustration with fine lines and clean cel-shaded colors. Each panel visibly different.',
    'Create an original female character art-style atlas sheet, PORTRAIT 2:3 image, 2 columns by 2 rows, four separated panels each with one adult woman standing front view, FULL BODY from top of head through both complete shoes fully visible with margins, opaque tasteful blouse and full length dark pants. No lettering, logo, watermark, copyrighted character. TOP LEFT poetic Japanese animation film style with vivid sky, clouds, warm sunset backlight and atmospheric detail; TOP RIGHT next-generation 3D game character render with realistic skin, clothing material and fine geometry; BOTTOM LEFT stylish designer vinyl toy figurine full body, unmistakable glossy sculpted plastic and articulated shapes; BOTTOM RIGHT character design concept standing full-body isolated on a pure white background, simple exact outline and flat color, no diagrams.',
]
jobs, boards = [], []
for i, (group, kind, width, height, y) in enumerate([(0,'portrait',1536,1024,509), (1,'portrait',1536,1024,512), (0,'fullbody',1024,1536,716), (1,'fullbody',1024,1536,720)]):
    es = entries[group*4:group*4+4]
    role = 'fullbody_reference' if kind == 'fullbody' else 'primary'
    title = '画风补充 · ' + ('全身' if kind == 'fullbody' else '人像近景') + f' · {group+1}'
    j = dict(id=f'art-v59-{group+1}-{kind}', category='art_styles', dimension='画风补充', title=title,
             image=f'images/sheet-art-v59-{group+1}-{kind}.png', columns=2, rows=2,
             edition=59, role=role, column_boundaries=[0,width//2,width], row_boundaries=[0,y,height],
             entries=es, prompt=prompts[i])
    b = dict(**{k:j[k] for k in ['id','category','dimension','title','image','columns','rows','edition','role','column_boundaries','row_boundaries','prompt']},
             width=width,height=height,origin='AI-generated style study; photography styles are simulated',qa_status='visually_reviewed',
             items=[dict(label=e['id'],entry_id=e['id'],name=e['name']) for e in es])
    jobs.append(j);boards.append(b)
for filename, records in [('image-jobs.json',jobs),('extra-illustrations.json',boards)]:
    path = root/'source'/filename
    old = json.loads(path.read_text(encoding='utf-8'))
    path.write_text(json.dumps([x for x in old if x.get('edition')!=59]+records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Registered 8 art styles with 8 portraits and 8 full-body illustrations.')
