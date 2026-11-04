"""Prepare photographic framing studies and complete full-length group portraits."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent));import _bootstrap
import build_atlas_v2
import photo_poses_v55 as content
root=_bootstrap.ROOT;es=[dict(e,id=f'PP{i:03}') for i,e in enumerate(content.NEW_ENTRIES,1)]
common='''Use case: stylized-concept. Asset: photography posing reference atlas for adult female characters.
Create polished detailed 2D anime-adjacent illustrations with mature adult faces, natural adult proportions, clean readable linework and soft fabric shading, consistent warm ivory background and diffuse natural studio light. EXACT TWO COLUMNS by TWO ROWS, FOUR cells in row-major order, thin straight gray grid rules. Put ONLY exact short ID small black at TOP LEFT of its cell, no other text, inset or watermark. Each cell is ONE final posed composition, no explanatory camera icon, arrows, photographer or duplicated figure.
All people clearly ADULT age28–38, full opaque normal clothing, nonsexual fashion portrait context. Default single character: dark-brown low ponytail or loose low bun, opaque muted teal covered blouse, full charcoal straight trousers and flat closed shoes; modest covered dress only where specifically requested. Exactly two coherent arms and legs per person, correct joints and natural hands with believable occlusion. All visible fingers, held objects, heads, hair and arm outlines fit with generous margins. For cells marked MEDIUM SHOT intentionally frame head through mid-thigh, contain ALL raised arms and phone fully; legs below mid-thigh are outside intended portrait framing. For FULL LENGTH cells show ENTIRE people through complete shoes and every support contact, scale scene to fit all people and props in own cell. No extremity crosses grid lines.
For mirror selfies show ONLY the SINGLE reflected woman as the final image: NO additional real body outside mirror, NO repeated reflection and no second phone. Phone back and camera lenses face viewer in mirror poses. Keep eyes or the stated portion of face visible. For group photos, each person has distinct clearly adult face and own coherent body, all hands and feet belong to the correct person.\n'''
jobs=[]
for g in content.GROUPS:
    group=[e for e in es if e['photo_pose_group']==g['id']];assert len(group)==4
    shape='LANDSCAPE canvas approximately3:2 with four WIDE cells for complete multi-person group arrangements.' if g['actors']>1 else 'PORTRAIT canvas approximately2:3 with four tall portrait cells.'
    actors=f"EXACTLY {g['actors']} clearly adult women in EACH cell. "
    prompt=common+shape+'\n'+actors+'Ordered cells:\n'+'\n'.join(f"Cell{i+1}, ID {e['id']}: {'MEDIUM SHOT head through mid-thigh' if e['photo_framing']=='半身' else 'FULL LENGTH head through complete shoes'}. {e['en']}. {e['illustration_recipe']}. Camera height: {e['camera_height']}; gaze: {e['gaze_direction']}; support: {e['pose_support']}." for i,e in enumerate(group))
    jobs.append(dict(id='photo-v55-'+g['id'],category=content.CID,dimension=g['name'],title=g['name']+' · 4项',image=f"images/sheet-{group[0]['id'].lower()}-{group[-1]['id'].lower()}.png",columns=2,rows=2,edition=55,framing=g['framing'],actors=g['actors'],entries=[{k:e[k] for k in ['id','name','en']} for e in group],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==55}
for j in jobs:
    for k in ['image','column_boundaries','row_boundaries','edit_prompt','reference_image','edit_history','original_generation_prompt']:
        if k in prior.get(j['id'],{}):j[k]=prior[j['id']][k]
p.write_text(json.dumps([j for j in old if j.get('edition')!=55]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/photo-v55/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'entries':len(j['entries']),'framing':j['framing'],'actors':j['actors']} for j in jobs]))
