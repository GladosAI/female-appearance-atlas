"""Connect the selected production logo and theme-aware tab icons to the page."""
import json,re

def apply_brand_assets(root,template):
    active=json.loads((root/'assets/brand/active.json').read_text(encoding='utf-8'))
    folder=active['directory']
    mark=(root/folder/'logo.svg').read_text(encoding='utf-8')
    mark=re.sub(r'<(?:title|desc)>[\s\S]*?</(?:title|desc)>','',mark)
    mark=mark.replace('<svg ','<svg class="brand-symbol" aria-hidden="true" focusable="false" ',1)
    palettes=json.loads((root/'tools/templates/theme_palettes.json').read_text(encoding='utf-8'))
    settings={p['id']:{'icon':folder+'/favicon-'+p['id']+'.svg','background':p['colors']['bg']} for p in palettes}
    fallbacks=['favicon.ico','favicon-32.png','favicon.svg','apple-touch-icon.png']
    assert all((root/p['icon']).is_file() for p in settings.values()),'Run node tools/builders/brand_assets.cjs to export brand icons.'
    assert all((root/folder/name).is_file() for name in fallbacks),'Production brand exports are incomplete.'
    head=f'''<meta name="application-name" content="女性之美">
<meta id="brand-theme-color" name="theme-color" content="{settings['light']['background']}">
<link id="site-favicon-ico" rel="icon" href="{folder}/favicon.ico" sizes="any">
<link id="site-favicon-png" rel="icon" type="image/png" sizes="32x32" href="{folder}/favicon-32.png">
<link id="site-favicon" rel="icon" type="image/svg+xml" sizes="any" href="{folder}/favicon.svg">
<link id="site-touch-icon" rel="apple-touch-icon" sizes="180x180" href="{folder}/apple-touch-icon.png">'''
    replacements={'__BRAND_HEAD__':head,'__BRAND_MARK__':mark,'__BRAND_THEME_SETTINGS__':json.dumps(settings,ensure_ascii=False,separators=(',',':'))}
    for key,value in replacements.items():template=template.replace(key,value)
    return template
