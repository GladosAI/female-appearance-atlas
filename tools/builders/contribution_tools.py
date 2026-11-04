"""A local-only contribution form and a small searchable, non-reserving ID index."""
import json
import re


def next_identifier(prefix, identifiers):
    number=max((int(match[1]) for identifier in identifiers
                if (match:=re.fullmatch(re.escape(prefix)+r'(\d+)',identifier))),default=0)+1
    return prefix+str(number).zfill(3)


def contribution_files(root, data):
    from catalog_layout import PREFIX
    from theme_palettes import apply_theme_palettes
    from brand_assets import apply_brand_assets
    extensions=json.loads((root/'source/category-extensions.json').read_text(encoding='utf-8'))
    prefixes=[*PREFIX,*(category['prefix'] for category in extensions)]
    if len(prefixes)!=len(data['categories']):
        raise ValueError('Contribution index must use the complete canonical prefix table')
    registered={record['id'] for record in json.loads((root/'source/id-registry.json').read_text(encoding='utf-8'))['entries']}
    registered.update(entry['id'] for entry in data['entries'])
    payload={'schema':'female-appearance-contribution-index/v1','catalog_version':data['meta']['version'],
             'categories':[{'id':category['id'],'name':category['name'],'prefix':prefix,
                            'suggested_id':next_identifier(prefix,registered),
                            'dimensions':list(dict.fromkeys(e['dimension'] for e in data['entries'] if e['category']==category['id']))}
                           for category,prefix in zip(data['categories'],prefixes)],
             'entries':[{key:entry.get(key,[]) if key=='aliases' else entry[key]
                         for key in ['id','category','name','en','aliases']} for entry in data['entries']]}
    template=(root/'tools/templates/contribute.html').read_text(encoding='utf-8')
    template=template.replace('__CONTRIBUTE_SCRIPT__',(root/'tools/templates/contribute.js').read_text(encoding='utf-8'))
    template=apply_brand_assets(root,apply_theme_palettes(root,template))
    return {'contribute.html':template,'assets/contribution-index.js':
            'window.ATLAS_CONTRIBUTION='+json.dumps(payload,ensure_ascii=False,separators=(',',':'))+';\n'}


def write_contribution_tools(root,data):
    for relative,text in contribution_files(root,data).items():
        file=root/relative;file.parent.mkdir(parents=True,exist_ok=True)
        if not file.exists() or file.read_text(encoding='utf-8')!=text:
            file.write_text(text,encoding='utf-8')
