"""Verify the complete current portable file set, bytes and CRC."""
from pathlib import Path
import json, zipfile, sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _bootstrap
root = _bootstrap.ROOT
d = json.loads((root/'data/catalog.json').read_text('utf-8'))
assert d['meta']['version'] == '56.0' and len(d['entries']) == 6781
files = [p for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and '.work' not in p.parts and not any(part.startswith('verification') for part in p.parts) and p.suffix not in ['.lock','.tmp'] and 'preview' not in p.name]
expected = {p.relative_to(root.parent).as_posix(): p for p in files}
with zipfile.ZipFile(_bootstrap.PACKAGE) as package:
    names = package.namelist()
    assert len(names) == len(set(names)) and set(names) == set(expected)
    assert package.testzip() is None
    for name, p in expected.items(): assert package.read(name) == p.read_bytes(), name
report = dict(passed=True, files_exact=len(files), bytes=_bootstrap.PACKAGE.stat().st_size, entries=len(d['entries']), boards=len(d['boards']), crc_passed=True)
(root/'.work/verification/quadruped-v56/archive-report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
