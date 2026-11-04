"""Register original hairstyle sheets with measured panel boundaries."""
import json,sys
from collections import Counter
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import _bootstrap
import build_atlas_v2 as atlas
import hair_comparison_v65 as content

root=_bootstrap.ROOT
prompts=json.loads((root/'source/hair-v65-image-prompts.json').read_text(encoding='utf-8'))
sizes={'short1':(1090,1443,545,721),'short2':(1024,1536,512,767),
       'short3':(1024,1536,512,767),'medium1':(1024,1536,512,728),
       'medium2':(1024,1536,512,757),'long':(1024,1536,512,767)}
categories={c['id']:i for i,c in enumerate(atlas.CATEGORIES)}
counts=Counter();identified={}
for e in atlas.CATALOG:
    counts[e['category']]+=1
    if e.get('hair_comparison_v65'):
        identified[e['name']]=dict(e,id=atlas.PREFIX[categories[e['category']]]+f"{counts[e['category']]:03}")
jobs=[];boards=[]
for group,dimension,records in content.GROUPS:
    es=[identified[x[0]] for x in records];assert len(es)==4
    w,h,x,y=sizes[group];cid='hair_combinations'
    job=dict(id='hair-v65-'+group,category=cid,dimension=dimension,title=dimension,
        image=f'images/sheet-hair-v65-{group}.png',columns=2,rows=2,edition=65,
        column_boundaries=[0,x,w],row_boundaries=[0,y,h],
        entries=[{k:e[k] for k in ['id','name','en']} for e in es],prompt=prompts[group])
    assert (root/job['image']).exists(),job['image']
    board=dict(**{k:job[k] for k in ['id','category','dimension','title','image','columns','rows','edition','column_boundaries','row_boundaries','prompt']},
        width=w,height=h,origin='Original AI-generated illustration; text-only inspiration, source images not consulted or reused',qa_status='visually_reviewed',
        items=[dict(label=e['id'],entry_id=e['id'],name=e['name']) for e in es])
    jobs.append(job);boards.append(board)
for file,records in [('image-jobs.json',jobs),('extra-illustrations.json',boards)]:
    p=root/'source'/file;old=json.loads(p.read_text(encoding='utf-8'))
    p.write_text(json.dumps([x for x in old if x.get('edition')!=65]+records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=root/'source/navigation.json';nav=json.loads(p.read_text(encoding='utf-8'))
doc={'name':'人像发型词条对照 · 24项原创补充','path':'docs/hair-comparison-v65.md'}
nav['documents']=[doc]+[x for x in nav['documents'] if x['path']!=doc['path']]
p.write_text(json.dumps(nav,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Registered',len(content.NEW_ENTRIES),'hairstyles in',len(boards),'original sheets')
