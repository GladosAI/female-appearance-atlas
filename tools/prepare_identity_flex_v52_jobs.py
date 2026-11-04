"""Prepare paired identities, four-cell costumes and uncropped full-body flexibility studies."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent));import _bootstrap
import build_atlas_v2
import identity_flex_v52 as content
root=_bootstrap.ROOT;counts={'identity_status':8,'identity_duties':6,'identity_classic':6,'kungfu_outfits':0,'clown_outfits':0,'flexibility_poses':0};prefix={'identity_status':'IS','identity_duties':'ID','identity_classic':'IC','kungfu_outfits':'KU','clown_outfits':'CW','flexibility_poses':'PF'};es=[]
for e in content.NEW_ENTRIES:
    counts[e['category']]+=1;es.append(dict(e,id=prefix[e['category']]+f"{counts[e['category']]:03}"))
common='''Use case: stylized-concept. Asset: original adult female appearance and body-pose atlas.
Polished detailed anime-adjacent illustration, clean controlled outlines, readable mature adult faces, natural adult anatomy and rich opaque fabric shading. Pale warm ivory cell backgrounds and consistent diffuse studio lighting. Put each EXACT short ID at TOP LEFT of its own cell in small plain black text, no other text, title, logo or watermark. Thin straight gray grid separators. Exactly ONE clearly adult woman age25–36 in each cell. Correct two arms and two legs, normal joints, one thumb and four fingers per hand with believable occlusion. No additional insets or extra people.
Complete whole-body subject in every cell with GENEROUS clear margins around crown, hands, fingertips and all feet/toes/shoes. For floor poses adapt figure scale to the FULL horizontal reach; no hand, leg, hair or foot may touch or cross a cell border. Opaque clothing covers private areas, no sexual context or focus. No weapons, violence, wounds, gore or childlike body. This is original character-design and drawing reference.\n'''
frames={
 'paired_identity':'EXACTLY TWO COLUMNS, ONE ROW, two tall portrait cells side by side, wide landscape canvas approximately3:2. Full standing adult in each cell. The SAME adult woman in both cells, match face identity, skin tone, eye color, hair and signature details precisely. ',
 'full_body':'EXACTLY TWO COLUMNS, TWO ROWS, four portrait cells in row-major order, portrait canvas approximately2:3. Full standing adult, complete costume and both shoes in each cell. ',
 'standing_pose':'EXACTLY TWO COLUMNS, TWO ROWS, four portrait cells in row-major order, portrait canvas approximately2:3. Entire adult figure from topmost fingertips/crown through complete toes. Show the described graceful body line and support points. ',
 'floor_pose':'EXACTLY TWO COLUMNS, TWO ROWS, four spacious cells in row-major order, SQUARE canvas approximately1:1. Each cell must contain the ENTIRE floor pose, full crown, hands and both feet including toes. Show pelvis, shoulders and floor contact points with coherent anatomy, thin plain mat only. ',
 'wide_floor_pose':'EXACTLY TWO COLUMNS, TWO ROWS, four WIDE landscape cells in row-major order, LANDSCAPE canvas approximately3:2. Each cell must contain the ENTIRE horizontal pose, generous margins beyond all fingertips and toes. Show full anatomy and all floor/platform contact points; thin plain mat only unless a platform explicitly requested. Do not clip or hide limbs beyond frame. '}
jobs=[]
for key,cid,title,cols,rows,framing,character in content.GROUPS:
    group=[e for e in es if e.get('identity_pair')==key or e.get('expansion_group')==key];assert len(group)==cols*rows
    prompt=common+frames[framing]+('\nSame-character design: '+character if character else '')+'\nOrdered cells:\n'+'\n'.join(f"Cell{i+1}, ID {e['id']}: {e['en']}. {e['illustration_recipe']}." for i,e in enumerate(group))
    jobs.append(dict(id='identity-flex-v52-'+key,category=cid,dimension=title,title=title+(' · 双造型对照' if rows==1 else ' · 4项'),framing=framing,image=f"images/sheet-{group[0]['id'].lower()}-{group[-1]['id'].lower()}.png",columns=cols,rows=rows,edition=52,entries=[{k:e[k] for k in ['id','name','en']} for e in group],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==52}
for j in jobs:
    for k in ['image','column_boundaries','row_boundaries','edit_prompt','reference_image','edit_history']:
        if k in prior.get(j['id'],{}):j[k]=prior[j['id']][k]
p.write_text(json.dumps([j for j in old if j.get('edition')!=52]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/identity-flex-v52/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'entries':len(j['entries']),'framing':j['framing']} for j in jobs]))
