"""Separate the searchable browsing index from domain-specific entry details."""
import hashlib
import json
import unicodedata

# These fields drive cards, filters, comparison layouts and name-only prompt export.
# Keep maintenance and detailed explanation fields in the on-demand domain files.
INDEX_FIELDS = set('''id category category_name name en dimension description styles aliases
origin added_in accessory_anchor accessory_expansion_reference adult_measurement_reference
age_range age_stage anime_hairtie_reference anthro_reference art_style_reference
body_cord_reference body_dimension_reference body_shape_key body_shape_reference body_shape_view
bra_size bust_cm camera_reference changed_condition comparison_baseline comparison_figure
comparison_kind comparison_order comparison_reference comparison_set comparison_stature_cm
comparison_view cord_knot_anchor cord_view cosplay_reference cup_difference_cm cup_letter denier
dimension_case dimension_figure dimension_label dimension_order dimension_view eye_makeup_reference
facial_reference fashion_history_reference fixed_conditions fullbody_visual game_design_reference
growth_reference hair_accessory_anchor hair_accessory_name hair_accessory_view hair_tie_detail_inset
hair_tie_motif_name head_units headphone_anchor headphone_detail_inset headphone_reference
headphone_view height_cm hip_cm history_comparison_kind history_line history_line_name history_order
history_period history_region history_track hooded_cloak hosiery_reference length_cm life_stage_group
life_stage_reference makeup_finish makeup_placement makeup_view paired_shape_label pose_actors
pose_expansion_reference pose_phase pose_support pose_view presentation region season
seasonal_reference sequence_labels sequence_reference shoulder_width_cm stature_kind study_reference
styled_hair_reference underbust_cm view visual visual_language_reference waist_cm wearing_visual
wedding_reference'''.split())
VISUAL_FIELDS = ('visual', 'wearing_visual', 'fullbody_visual')


def compact_json(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def write_hashed(output, stem, text):
    fingerprint = hashlib.sha256(text.encode('utf-8')).hexdigest()[:12]
    relative = f'assets/{stem}-{fingerprint}.js'
    (output / relative).write_text(text, encoding='utf-8')
    return relative


def browsing_index(data, navigation):
    index = {key: value for key, value in data.items() if key not in {'entries', 'boards'}}
    category_names = {c['id']: c['name'] for c in data['categories']}
    domains = {category: group['id'] for group in navigation['groups'] for category in group['categories']}
    boards = {b['id']: b for b in data['boards']}
    chunks = {}
    entries = []
    normalize = lambda text: unicodedata.normalize('NFKC', str(text)).lower().strip()
    for entry in data['entries']:
        core = {key: value for key, value in entry.items() if key in INDEX_FIELDS and value is not False}
        # Comparison panels show their shared design note without opening a detail dialog.
        if entry.get('body_shape_reference'):
            core['design_tip'] = entry.get('design_tip', '')
        base = normalize(' '.join(str(entry.get(key, '')) for key in
                                  ['id', 'name', 'en', 'category_name', 'description']))
        base += ' ' + normalize(' '.join(entry.get('aliases', [])))
        base += ' ' + normalize(entry.get('history_line_name') or entry['dimension'])
        keywords = []
        for word in entry.get('keywords', []):
            if entry.get('history_line') and word == entry['dimension']:
                continue
            normal = normalize(word)
            if normal and normal not in base:
                keywords.append(word)
                base += ' ' + normal
        core['keywords'] = keywords
        if core.get('category_name') == category_names.get(entry['category']):
            core.pop('category_name', None)
        for field in VISUAL_FIELDS:
            if field not in core:
                continue
            visual = dict(core[field])
            board = boards[visual['board']]
            for key in ['image', 'columns', 'rows']:
                if visual.get(key) == board.get(key):
                    visual.pop(key, None)
            if visual.get('crop'):
                crop = dict(visual['crop'])
                for key, source in [('sheet_width', 'width'), ('sheet_height', 'height')]:
                    if crop.get(key) == board.get(source):
                        crop.pop(key, None)
                visual['crop'] = crop
            core[field] = visual
        entries.append(core)
        detail = {key: value for key, value in entry.items() if key not in INDEX_FIELDS}
        detail['id'] = entry['id']
        chunks.setdefault(domains.get(entry['category'], 'other'), []).append(detail)
    index['entries'] = entries
    # Labels and names are reconstructed from the entry index; authoring recipes stay out of boot data.
    index['boards'] = [{**{key: b[key] for key in
                          ['id', 'title', 'image', 'columns', 'rows', 'width', 'height'] if key in b},
                        'items': [[item['entry_id'], item['label']] for item in b['items']]}
                       for b in data['boards']]
    return index, chunks, domains


def write_runtime(output, data, navigation):
    index, chunks, domains = browsing_index(data, navigation)
    paths = {}
    for domain, entries in chunks.items():
        payload = 'globalThis.__atlasDetailChunks??={};\n'
        payload += 'globalThis.__atlasDetailChunks[' + compact_json(domain) + ']=' + compact_json(entries) + ';\n'
        paths[domain] = write_hashed(output, 'details-' + domain, payload)
    payload = 'window.ATLAS_WEB=' + compact_json({'data': index, 'navigation': navigation,
                                               'detailDomains': domains, 'detailChunks': paths}) + ';\n'
    payload += '''(()=>{const d=window.ATLAS_WEB.data,B=new Map(d.boards.map(b=>[b.id,b])),E=new Map(d.entries.map(e=>[e.id,e])),C=new Map(d.categories.map(c=>[c.id,c]));
for(const e of d.entries){e.category_name??=C.get(e.category)?.name;for(const key of ['visual','wearing_visual','fullbody_visual']){const v=e[key];if(!v)continue;const b=B.get(v.board);v.image??=b.image;v.columns??=b.columns;v.rows??=b.rows;if(v.crop){v.crop.sheet_width??=b.width;v.crop.sheet_height??=b.height}}}
for(const b of d.boards)b.items=b.items.map(([entry_id,label])=>({entry_id,label,name:E.get(entry_id)?.name||entry_id}));})();\n'''
    return write_hashed(output, 'runtime', payload), paths
