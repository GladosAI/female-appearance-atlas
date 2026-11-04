"""Shared locations for the organized atlas and its portable build tools."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
for folder in [ROOT / 'tools' / 'builders', ROOT / 'source' / 'catalog']:
    sys.path.insert(0, str(folder))
sys.pycache_prefix = str(ROOT / '.work' / 'cache' / 'python')
for folder in ['.work/locks', '.work/previews', 'data', 'docs', 'prompts']:
    (ROOT / folder).mkdir(parents=True, exist_ok=True)
PACKAGE = ROOT / 'dist' / 'female-appearance-atlas.zip'
PACKAGE.parent.mkdir(parents=True, exist_ok=True)
