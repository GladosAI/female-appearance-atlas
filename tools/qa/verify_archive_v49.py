"""Verify the portable V49 package matches the published atlas exactly."""
from pathlib import Path
import json,zipfile,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]));import _bootstrap
root=_bootstrap.ROOT;archive=_bootstrap.PACKAGE
d=json.loads((root/'data/catalog.json').read_text(encoding='utf-8'))
assert d['meta']['version']=='49.0' and len(d['entries'])==6513 and len(d['boards'])==502
files=[p for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and '.work' not in p.parts and not any(part.startswith('verification') for part in p.parts) and p.suffix not in ['.lock','.tmp'] and 'preview' not in p.name]
expected={str(p.relative_to(root.parent)).replace('\\','/'):p for p in files}
with zipfile.ZipFile(archive) as package:
    names=package.namelist();assert len(names)==len(set(names));assert set(names)==set(expected);assert package.testzip() is None
    for name,p in expected.items():assert package.read(name)==p.read_bytes(),name
report={'passed':True,'bytes':archive.stat().st_size,'files_exact':len(files),'entries':6513,'boards':502,'crc_passed':True}
(root/'.work/verification/persona-v49/archive-report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report))
