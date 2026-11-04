"""Register seven original outfit sheets with visually measured dividers."""
import json,sys
from collections import Counter
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import _bootstrap
import build_atlas_v2 as atlas
import costume_combinations_v64 as content

root=_bootstrap.ROOT
prompts=json.loads((root/'source/costume-v64-image-prompts.json').read_text(encoding='utf-8'))
row_bounds={'spring':750,'summer':750,'autumn':722,'winter':750,'resort':758,'sleep':767,'evening':743}
categories={c['id']:i for i,c in enumerate(atlas.CATEGORIES)}
counts=Counter();identified={}
for e in atlas.CATALOG:
    counts[e['category']]+=1
    if e.get('outfit_combination_v64'):
        identified[e['name']]=dict(e,id=atlas.PREFIX[categories[e['category']]]+f"{counts[e['category']]:03}")
jobs=[];boards=[]
for group,cid,dimension,records in content.GROUPS:
    es=[identified[x[0]] for x in records]
    title=dimension+' · 组合示意'
    job=dict(id='costume-v64-'+group,category=cid,dimension=dimension,title=title,
        image=f'images/sheet-costume-v64-{group}.png',columns=2,rows=2,edition=64,
        column_boundaries=[0,512,1024],row_boundaries=[0,row_bounds[group],1536],
        entries=[{k:e[k] for k in ['id','name','en']} for e in es],prompt=prompts[group])
    assert (root/job['image']).exists(),job['image']
    board=dict(**{k:job[k] for k in ['id','category','dimension','title','image','columns','rows','edition','column_boundaries','row_boundaries','prompt']},
        width=1024,height=1536,origin='Original AI-generated illustration; text-only inspiration, no source images reused',qa_status='visually_reviewed',
        items=[dict(label=e['id'],entry_id=e['id'],name=e['name']) for e in es])
    jobs.append(job);boards.append(board)
for file,records in [('image-jobs.json',jobs),('extra-illustrations.json',boards)]:
    p=root/'source'/file;old=json.loads(p.read_text(encoding='utf-8'))
    p.write_text(json.dumps([x for x in old if x.get('edition')!=64]+records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=root/'source/navigation.json';nav=json.loads(p.read_text(encoding='utf-8'))
doc={'name':'参考词条对照 · 14套原创搭配','path':'docs/costume-comparison-v64.md'}
nav['documents']=[doc]+[x for x in nav['documents'] if x['path']!=doc['path']]
p.write_text(json.dumps(nav,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Registered',sum(len(g[3]) for g in content.GROUPS),'outfits in',len(boards),'sheets')
