"""Verify all bytes and CRC of the current V42 offline package."""
from pathlib import Path
import json,zipfile,sys
sys.pycache_prefix=str(Path(__file__).resolve().parents[2]/'.work/cache/python')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]));import _bootstrap
root=_bootstrap.ROOT;archive=_bootstrap.PACKAGE
data=json.loads((root/'data/catalog.json').read_text(encoding='utf-8'))
assert data['meta']['version']=='42.0' and len(data['entries'])==6093 and len(data['boards'])==419
files=[p for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and '.work' not in p.parts and not any(part.startswith('verification') for part in p.parts) and p.suffix not in ['.lock','.tmp'] and 'preview' not in p.name]
expected={str(p.relative_to(root.parent)).replace('\\','/'):p for p in files}
with zipfile.ZipFile(archive) as package:
    names=package.namelist();assert len(names)==len(set(names));assert set(names)==set(expected);assert package.testzip() is None
    for name,p in expected.items():assert package.read(name)==p.read_bytes(),name
report={'passed':True,'bytes':archive.stat().st_size,'files_exact':len(files),'entries':6093,'boards':419,'crc_passed':True}
(root/'.work/verification/hybrid-v42/archive-report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report))
