"""Prepare three supplemental historical-costume sheets without changing V38 jobs."""
from pathlib import Path
import sys,json,ast
sys.pycache_prefix=str(Path(__file__).resolve().parents[1]/'.work/cache/python')
import _bootstrap
from fashion_history_v39 import CATALOG,TRACKS
root=_bootstrap.ROOT
es=[e for e in CATALOG if e.get('fashion_history_extension')]
for i,e in enumerate(es,49):e['id']=f'FH{i:03}'
module=ast.parse((root/'tools/prepare_history_v38_jobs.py').read_text(encoding='utf-8'))
common=next(ast.literal_eval(n.value) for n in module.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='common' for t in n.targets))
common+='\nFraming is critical: leave at least 15px ivory margins beyond every side of the full garment, sleeves, headdress and hem. Reduce the whole figure scale when a robe is broad or crown is tall. Never cut off a skirt at the grid. No extra limbs or repeated knees. Use a different ORIGINAL adult model when appropriate to the region, with natural varied skin tones, without caricatures.\n'
directions={
 'china_more':'Chinese supplement: make the straight Han hem different from winding quju; distinguish tunic/trousers from skirts; show Tang half-sleeve BANBI over long sleeves; Liao round neck versus Yuan noble robe and tall gugu crown; Ming SLEEVELESS long bijia; Qing changyi OPEN-SIDE outer robe over fully covered inner robe; then jacket/trousers, qipao+jacket, and modern skirt suit. No generic modern hanfu for all16.',
 'japan_korea':'Two PARALLEL histories in one sheet: Japanese cells1,2,4,6,7,9,13,15; Korean cells3,5,8,10,11,12,14,16. Keep identities of garments precise: kimono/kosode are straight-cut with left front over right; uchikake is unbelted OUTER robe; obi width differs by era. Korean jeogori+chima are separate jacket and gathered skirt with white collar bands and goreum ties, NOT kimono or qipao. Dangui has longer curved front panels; wonsam has broad sleeves and cuff bands; hwarot is red embroidered formal robe; jeogui is deep blue ceremonial robe. All figures clearly mature adults, no anime schoolgirls.',
 'regional':'This is a curated REGIONAL SELECTION, NOT one chronological progression or stereotype of a culture. Read cells in given order; each outfit belongs to its own place and reference date. South Asian peshwaz/ghagra/sari/salwar must be visibly different. Entari reveals opaque blouse+trousers under open robe; bindalli is a closed velvet formal dress. Qajar SHORT skirt is worn OVER fully opaque LONG TROUSERS. Vietnamese ao ngu than and ao dai have long pants under long side panels, not bare-leg qipao. Kebaya front-open blouse has an OPAQUE underlayer, no see-through textile. Kente uses strip-woven cloth and an opaque blouse; no mens royal wrap. Mexican Tehuana square huipil+ruffled skirt differs from Panamanian white embroidered pollera. Adapted full-coverage inner layers are intentional for the reference style. Do not copy a sacred, royal or personal textile pattern; use original restrained motifs.'}
jobs=[]
for track in TRACKS:
 group=[e for e in es if e['history_track']==track['id']];assert len(group)==16
 base=common.replace('Read left to right then down chronologically.','Read left to right then down in the specified order.')
 prompt=base+'\nTrack: '+track['name']+'. Scope: '+track['scope']+'.\n'+directions[track['id']]+'\nOrdered cells:\n'+'\n'.join(f"Cell {i+1} ID {e['id']}: {e['name']} / {e['en']}. Reference period {e['history_period']}; region {e['history_region']}. {e['history_recipe']}" for i,e in enumerate(group))
 jobs.append(dict(id='history-v39-'+track['id'],category='fashion_history',dimension=track['name'],title=track['name']+' · 16项配图',image=f"images/sheet-{group[0]['id'].lower()}-{group[-1]['id'].lower()}.png",columns=4,rows=4,edition=39,entries=[{k:e[k] for k in ['id','name','en']} for e in group],prompt=prompt))
p=root/'source/image-jobs.json';old=json.loads(p.read_text(encoding='utf-8'));prior={j['id']:j for j in old if j.get('edition')==39}
for j in jobs:
 for f in ['image','edit_prompt','reference_image','edit_history','column_boundaries','row_boundaries']:
  if f in prior.get(j['id'],{}):j[f]=prior[j['id']][f]
p.write_text(json.dumps([j for j in old if j.get('edition')!=39]+jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=root/'.work/verification/history-v39/jobs.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(jobs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':j['id'],'cells':len(j['entries'])} for j in jobs]))
