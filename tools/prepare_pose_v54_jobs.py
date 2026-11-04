"""Prepare legible four-cell whole-body pose sheets without changing prior PO IDs."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent));import _bootstrap
import build_atlas_v2
import pose_v54 as content
root=_bootstrap.ROOT
es=[dict(e,id=f'PO{i:03}') for i,e in enumerate(content.NEW_ENTRIES,237)]
common='''Use case: stylized-concept. Asset: original adult female full-body pose-reference atlas.
Style: polished detailed 2D anime-adjacent illustration, clean precise linework and restrained fabric shading, natural adult anatomy, mature readable faces, warm pale ivory backgrounds and even diffuse light. Simple gray furniture/supports ONLY where specified. Exactly TWO COLUMNS by TWO ROWS, FOUR distinct cells in row-major order, thin straight gray separators. Put ONLY each exact short ID at the TOP LEFT of its own cell in small plain black text, no other text, titles, insets, logo or watermark.
Whole-body framing: contain COMPLETE head/hair, both hands including fingertips, both legs and all shoes/feet, all requested furniture/props and support contact points, with generous margins in EACH cell. Scale to fit full horizontal or vertical reach. No limb may cross a cell border. Exactly two anatomically coherent arms and legs per person, believable shoulder/hip/knee/elbow connections and natural hands. Clearly show each stated contact/support; no feet floating unless specifically airborne. Each cell is ONE action frame, no ghost silhouettes or motion sequence. Opaque complete clothing and natural proportions, ordinary nonsexual drawing reference, no underwear, no nudity, no violence.\n'''
outfits={
 'casual':'One clearly adult woman age28–35 per cell, mature oval face, dark-brown low ponytail, opaque muted teal long-sleeve casual blouse/knit, full charcoal straight trousers, simple flat closed shoes; modify clothing only if cell explicitly specifies. ',
 'sport':'One clearly adult woman age28–35 per cell, mature face, dark tied hair, opaque muted teal long-sleeve athletic top, full charcoal athletic trousers/leggings and plain flat sneakers; no bare feet unless requested. ',
 'home':'One clearly adult woman age28–35 per cell, mature face, dark low bun, opaque muted teal long-sleeve sweater, full charcoal soft trousers and plain opaque socks, no shoes on furniture. ',
 'dress':'One clearly adult woman age28–35 per cell, mature face and dark tied hair, opaque covered long-sleeve calf or ankle dress and low closed shoes as specified. ',
 'fantasy':'One clearly adult woman age28–35 per cell, mature face and dark tied hair, fully opaque covered fantasy calf tunic over full trousers and closed flat boots, restrained original style with no copied franchise motifs. '}
jobs=[]
for g in content.GROUPS:
    group=[e for e in es if e['pose_group']==g['id']];assert len(group)==4
    framing='LANDSCAPE canvas approximately3:2, four WIDE cells with ample horizontal room for the complete floor pose, sofa or pair.' if g['layout']=='wide' else 'PORTRAIT canvas approximately2:3, four TALL cells for complete standing or seated figures.'
    people='Each cell contains exactly TWO mature adult women age28–35 with the appearances specified, four arms and four legs total. Use simple fully opaque casual tops, full trousers and closed flat shoes. Clearly separate their limbs and show all four feet.' if g['actors']==2 else outfits[g['outfit']]
    prompt=common+framing+'\n'+people+'\nOrdered cells:\n'+'\n'.join(f"Cell{i+1}, ID {e['id']}: {e['en']}. {e['illustration_recipe']}. Camera: {e['pose_view']}; support: {e['pose_support']}; phase: {e['pose_phase']}." for i,e in enumerate(group))
    jobs.append(dict(id='pose-v54-'+g['id'],category='pose',dimension=g['name'],title=g['name']+' · 4项',image=f"images/sheet-{group[0]['id'].lower()}-{group[-1]['id'].lower()}.png",columns=2,rows=2,edition=54,framing=g['layout'],actors=g['actors'],entries=[{k:e[k] for k in ['id','name','en']} for e in group],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==54}
for j in jobs:
    for k in ['image','column_boundaries','row_boundaries','edit_prompt','reference_image','edit_history','original_generation_prompt']:
        if k in prior.get(j['id'],{}):j[k]=prior[j['id']][k]
p.write_text(json.dumps([j for j in old if j.get('edition')!=54]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/pose-v54/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'entries':len(j['entries']),'framing':j['framing']} for j in jobs]))
