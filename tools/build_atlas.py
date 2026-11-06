"""Build the complete expanded atlas; refuses missing illustrations."""
import sys
from pathlib import Path
sys.pycache_prefix = str(Path(__file__).resolve().parents[1] / '.work/cache/python')
import _bootstrap
from build_atlas_v2 import build
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--partial', action='store_true')
    parser.add_argument('--skip-package', action='store_true', help='Build site/data without the large legacy ZIP')
    parser.add_argument('--no-image-exports', action='store_true', help='Skip offline sidecars (HTTP preview / source-only CI)')
    parser.add_argument('--check-generated', action='store_true', help='Check source/data/page consistency without an image pack')
    args = parser.parse_args()
    if args.check_generated:
        import json,re
        root=_bootstrap.ROOT
        expected=build(partial=True,package=False,image_exports=False,check_assets=False)
        actual=json.loads((root/'data/catalog.json').read_text(encoding='utf-8'))
        differing=[key for key in expected if key!='image_exports' and expected[key]!=actual.get(key)]
        for relative,key in [('data/illustrations.json','boards'),('data/references.json','references'),('data/combinations.json','combinations'),('data/example-coverage.json','example_coverage')]:
            if json.loads((root/relative).read_text(encoding='utf-8'))!=expected[key]:differing.append(relative)
        from navigation_v32_docs import build_navigation
        if json.loads((root/'data/navigation.json').read_text(encoding='utf-8'))!=build_navigation(root,expected):differing.append('data/navigation.json')
        strip=lambda text:re.sub(r'(<script id="atlas-data" type="application/json">).*?(</script>)',r'\1\2',text,flags=re.S)
        if strip((root/'.work/previews/index-v2-preview.html').read_text(encoding='utf-8'))!=strip((root/'index.html').read_text(encoding='utf-8')):
            differing.append('index.html/template')
        from contribution_tools import contribution_files
        from localization_delivery import localization_files
        for relative,text in localization_files(root,expected).items():
            path=root/relative
            if not path.exists() or path.read_text(encoding='utf-8')!=text:
                differing.append(relative)
        for relative,text in contribution_files(root,expected).items():
            path=root/relative
            if not path.exists() or path.read_text(encoding='utf-8')!=text:
                differing.append(relative)
        if differing:raise SystemExit('Generated files are stale: '+', '.join(differing)+'; rebuild before committing')
        print('Source, catalog and page are consistent; image existence not checked.')
    else:
        build(partial=args.partial, package=not args.skip_package, image_exports=not args.no_image_exports)
