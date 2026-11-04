"""Keep theme persistence, dropdown choices and CSS on the same palette list."""
import html,json,re

def apply_theme_palettes(root,template):
    palettes=json.loads((root/'tools/templates/theme_palettes.json').read_text(encoding='utf-8'))
    ids=[p['id'] for p in palettes]
    assert ids[0]=='light' and 'dark' in ids and len(ids)==len(set(ids))
    required={'bg','surface','ink','muted','line','accent','soft','gold','support','support-soft','accent-ink','sidebar-bg','field-bg','field-line','backdrop'}
    blocks=[];options={'light':[],'dark':[]}
    system_declarations={}
    for p in palettes:
        mode=p['mode']
        assert mode in options and re.fullmatch(mode+r'(?:-[a-z]+)?',p['id']) and set(p['colors'])==required
        assert all(re.fullmatch(r'#[0-9a-f]{6}(?:[0-9a-f]{2})?',v) for v in p['colors'].values())
        shadow='#0004' if mode=='dark' else '#30252c0b'
        declarations=''.join('--'+k+':'+v+';' for k,v in p['colors'].items())+'--shadow:0 8px 30px '+shadow+';color-scheme:'+mode+';'
        if p['id']=='light':blocks.append(':root{'+declarations+'}')
        blocks.append(':root[data-theme="'+p['id']+'"]{'+declarations+'}')
        if p['id'] in ('light','dark'):system_declarations[mode]=declarations
        name=html.escape(p['name'])
        options[mode].append('<option value="'+p['id']+'">'+name+'</option>')
    blocks.append(':root[data-theme="system"]{'+system_declarations['light']+'}')
    blocks.append('@media(prefers-color-scheme:dark){:root[data-theme="system"]{'+system_declarations['dark']+'}}')
    replacements={
        '__THEME_IDS__':json.dumps(['system',*ids],separators=(',',':')),
        '__PALETTE_STYLES__':'\n'.join(blocks),
        '__THEME_OPTIONS__':'<option value="system">跟随系统</option><optgroup label="浅色配色">'+''.join(options['light'])+'</optgroup><optgroup label="深色配色">'+''.join(options['dark'])+'</optgroup>',
    }
    for key,value in replacements.items():template=template.replace(key,value)
    return template
