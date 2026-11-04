"""Register a saved generated contact sheet with an atomic, locked metadata write."""
from pathlib import Path
import sys,json,struct,os,msvcrt
sys.pycache_prefix = str(Path(__file__).resolve().parents[1] / '.work/cache/python')
import _bootstrap
ROOT = _bootstrap.ROOT
ident=sys.argv[1]
jobs=json.loads((ROOT/'source/image-jobs.json').read_text(encoding='utf-8'))
job=next(j for j in jobs if j['id']==ident)
path=ROOT/job['image'];raw=path.read_bytes()
assert raw[:8]==b'\x89PNG\r\n\x1a\n',ident
w,h=struct.unpack('>II',raw[16:24])
board={k:job[k] for k in ['id','category','dimension','title','image','columns','rows','prompt']}
for field in ['role','edition']:
    if field in job:board[field]=job[field]
board.update(width=w,height=h,origin='AI-generated concept illustration',qa_status='unreviewed',items=[{'label':e['id'],'entry_id':e['id'],'name':e['name']} for e in job['entries']])
for field,size,count in [('column_boundaries',w,job['columns']),('row_boundaries',h,job['rows'])]:
    if field in job:
        bounds=job[field]
        assert len(bounds)==count+1 and bounds[0]==0 and bounds[-1]==size
        assert all(a<b for a,b in zip(bounds,bounds[1:]))
        board[field]=bounds
with (ROOT/'.work/locks/illustration-manifest.lock').open('a+b') as lock:
    if lock.seek(0,2)==0:lock.write(b'0');lock.flush()
    lock.seek(0);msvcrt.locking(lock.fileno(),msvcrt.LK_LOCK,1)
    try:
        p=ROOT/'source/extra-illustrations.json'
        old=json.loads(p.read_text(encoding='utf-8')) if p.exists() else []
        updated=[b for b in old if b['id']!=ident]+[board]
        tmp=ROOT/'.work/locks'/('manifest-'+str(os.getpid())+'.tmp')
        tmp.write_text(json.dumps(updated,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        os.replace(tmp,p)
    finally:
        lock.seek(0);msvcrt.locking(lock.fileno(),msvcrt.LK_UNLCK,1)
print(json.dumps({'saved':ident,'cells':len(board['items']),'size':[w,h]}))
