"""Validate the complete catalog graph without depending on an AI runtime."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import struct
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
VISUALS = ('visual', 'wearing_visual', 'fullbody_visual')


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def local_path(root, relative):
    if not isinstance(relative, str) or '\\' in relative or re.search(r'[<>"\x00-\x1f]',relative):
        raise ValueError('Expected a portable relative POSIX path')
    path = PurePosixPath(relative)
    if path.is_absolute() or '..' in path.parts or ':' in relative:
        raise ValueError('Path escapes project: ' + relative)
    resolved = (root / relative).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError('Path escapes project: ' + relative)
    return resolved


def png_size(path):
    with path.open('rb') as stream:
        header = stream.read(24)
    if header[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError('Not a PNG: ' + str(path))
    return struct.unpack('>II', header[16:24])


def validate(data, navigation, root=ROOT, assets=True, registry=None):
    errors = []

    def check(ok, message):
        if not ok:
            errors.append(message)

    maps = {}
    for key in ['entries', 'categories', 'boards', 'references']:
        values = data.get(key, [])
        ids = [item.get('id') for item in values]
        check(len(ids) == len(set(ids)), key + ': duplicate identifiers')
        check(None not in ids, key + ': missing identifier')
        maps[key] = {item.get('id'): item for item in values}
    entries, cats, boards, refs = (maps[key] for key in ['entries', 'categories', 'boards', 'references'])
    styles={style['id'] for style in data.get('style_families',[])}
    for reference in refs.values():
        url=reference.get('url','')
        parsed=urlsplit(url)
        check(parsed.scheme in {'http','https'} and bool(parsed.netloc) and not re.search(r'[<>"\x00-\x20]',url),reference['id']+': invalid source URL')
    counts = Counter(entry.get('category') for entry in entries.values())
    for field, collection in [('entry_count', entries), ('category_count', cats), ('board_count', boards), ('reference_count', refs)]:
        check(data['meta'].get(field) == len(collection), 'meta.' + field + ': count mismatch')
    for category in cats.values():
        check(category.get('count') == counts[category['id']], category['id'] + ': count mismatch')
    membership = Counter(cid for group in navigation['groups'] for section in group['sections'] for cid in section['categories'])
    check(set(membership) == set(cats), 'navigation: categories missing or unknown')
    check(all(count == 1 for count in membership.values()), 'navigation: category belongs to multiple primary groups')
    for group in navigation['groups']:
        check(set(group['categories']) == {cid for section in group['sections'] for cid in section['categories']}, group['id'] + ': section membership mismatch')
        check(group['count'] == sum(counts[cid] for cid in group['categories']), group['id'] + ': count mismatch')
        for section in group['sections']:
            check(section['count'] == sum(counts[cid] for cid in section['categories']), section['id'] + ': count mismatch')
    for board in boards.values():
        bid = board['id']
        try:
            path = local_path(root, board['image'])
            if assets:
                check(path.is_file(), bid + ': missing image')
                if path.is_file() and path.suffix.lower() == '.png':
                    check(png_size(path) == (board['width'], board['height']), bid + ': sheet dimensions mismatch')
            check(board['columns'] > 0 and board['rows'] > 0, bid + ': invalid grid')
            check(len(board['items']) <= board['columns'] * board['rows'], bid + ': grid overflow')
            for axis, size in [('column_boundaries', board['width']), ('row_boundaries', board['height'])]:
                values = board.get(axis)
                if values:
                    expected = board['columns'] + 1 if axis.startswith('column') else board['rows'] + 1
                    check(len(values) == expected and 0 <= values[0] < values[-1] <= size
                          and all(a < b for a, b in zip(values, values[1:])), bid + ': invalid ' + axis)
            for item in board['items']:
                check(item['entry_id'] in entries, bid + ': unknown item ' + item['entry_id'])
        except (KeyError, TypeError, ValueError) as error:
            errors.append(bid + ': ' + str(error))
    for entry in entries.values():
        eid = entry['id']
        for field in ['id', 'name', 'en', 'category', 'dimension', 'description', 'design_tip']:
            check(isinstance(entry.get(field), str) and bool(entry[field].strip()), eid + ': missing/invalid ' + field)
        check(entry.get('category') in cats, eid + ': unknown category')
        check(isinstance(entry.get('aliases', []), list), eid + ': aliases must be a list')
        if entry.get('sequence_reference'):
            labels = entry.get('sequence_labels')
            check(isinstance(labels, list) and len(labels) == 3
                  and all(isinstance(label, str) and label.strip() for label in labels),
                  eid + ': storyboard requires three stage labels')
            check(entry.get('sequence_order') == 'left-to-right', eid + ': unsupported storyboard reading order')
        check(all(rid in refs for rid in entry.get('related_reading', [])), eid + ': unknown reading reference')
        check(all(style in styles for style in entry.get('styles',[])),eid+': unknown style')
        check(bool(entry.get('visual')), eid + ': missing primary visual')
        for field in VISUALS:
            visual = entry.get(field)
            if not visual:
                continue
            board = boards.get(visual.get('board'))
            check(board is not None, eid + ': unknown board')
            if not board:
                continue
            check(visual.get('image') == board.get('image'), eid + ': visual image/board mismatch')
            check(visual.get('columns') == board.get('columns') and visual.get('rows') == board.get('rows'), eid + ': visual grid mismatch')
            check(0 <= visual.get('column', -1) < board['columns'] and 0 <= visual.get('row', -1) < board['rows'], eid + ': visual grid position out of bounds')
            crop = visual.get('crop')
            if crop:
                check(crop['sheet_width'] == board['width'] and crop['sheet_height'] == board['height'], eid + ': crop sheet mismatch')
                check(crop['x'] >= 0 and crop['y'] >= 0 and crop['width'] > 0 and crop['height'] > 0
                      and crop['x'] + crop['width'] <= board['width'] and crop['y'] + crop['height'] <= board['height'], eid + ': crop out of bounds')
    for combo in data.get('combinations', []):
        check(all(eid in entries for eid in combo['entry_ids']), combo['name'] + ': unknown saved entry')
    active=[card for card in data.get('combinations',[]) if not card.get('archived')]
    if data.get('example_chapters'):
        chapters={chapter['id'] for chapter in data['example_chapters']}
        ids=[card.get('id') for card in active]
        check(None not in ids and len(ids)==len(set(ids)), 'examples: duplicate/missing stable identifier')
        check(data['meta'].get('combination_count')==len(active),'examples: active count mismatch')
        for card in active:
            check(card.get('chapter') in chapters,card['name']+': unknown character theme')
            check(4<=len(card['entry_ids'])<=8 and len(set(card['entry_ids']))==len(card['entry_ids']),card['name']+': example should be a small unique reference set')
            check(card.get('character_example') is True,card['name']+': missing character example marker')
            check(all(isinstance(card.get(field),str) and card[field].strip() for field in ['description','palette']),card['name']+': missing character description')
        coverage=data.get('example_coverage',{})
        used={entries[eid]['category'] for card in active for eid in card['entry_ids'] if eid in entries}
        check(coverage.get('covered_categories')==len(used),'examples: coverage count mismatch')
        check(set(coverage.get('uncovered_categories',[]))==set(cats)-used,'examples: uncovered category mismatch')
    if registry:
        locked = {record['id'] for record in registry['entries']}
        check(set(entries) <= locked, 'registry: unregistered public identifiers')
        check(len(locked) == len(registry['entries']), 'registry: duplicate identifier')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--metadata-only', action='store_true', help='No image pack needed')
    parser.add_argument('--release', action='store_true', help='Also require completed license and rights review')
    parser.add_argument('--report', default='.work/validation.json')
    args = parser.parse_args()
    data = load(ROOT / 'data/catalog.json')
    errors = validate(data, load(ROOT / 'data/navigation.json'), assets=not args.metadata_only,
                      registry=load(ROOT / 'source/id-registry.json'))
    from i18n_tools import validate_locales
    errors.extend(validate_locales(ROOT,data))
    from localization_delivery import localization_files
    try:
        for relative,text in localization_files(ROOT,data).items():
            file=local_path(ROOT,relative)
            if not file.is_file() or file.read_text(encoding='utf-8')!=text:
                errors.append('Generated locale file is stale: '+relative)
    except ValueError as error:
        errors.append(str(error))
    manifest=load(ROOT/'data/manifest.json')
    for relative,record in manifest['files'].items():
        path=local_path(ROOT,relative)
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=record['sha256']:
            errors.append('Generated data checksum mismatch: '+relative)
    index=[json.loads(line) for line in (ROOT/'data/agent-index.jsonl').read_text(encoding='utf-8').splitlines() if line]
    entries={entry['id']:entry for entry in data['entries']}
    if len(index)!=len(entries) or {entry['id'] for entry in index}!=set(entries):
        errors.append('Agent index identifiers differ from catalog')
    for record in index:
        entry=entries.get(record['id'])
        if entry and any(record.get(field)!=entry.get(field) for field in ['name','en','category','dimension','visual']):
            errors.append('Agent index is stale: '+record['id'])
    warnings = []
    rights = load(ROOT / 'source/rights-review.json')
    reviewed={item['path']:item for item in rights['assets']}
    required_assets={board['image'] for board in data['boards']} | {reference['image'] for reference in data['references'] if reference.get('image')}
    for relative in sorted(required_assets-set(reviewed)):
        (errors if args.release else warnings).append('Missing asset rights record: '+relative)
    from rights_audit import validate_rights
    evidence = load(ROOT / 'source/rights-evidence.json')
    policy = load(ROOT / 'source/license-policy.json')
    rights_errors, rights_warnings = validate_rights(rights, evidence, policy, ROOT, local_path,
                                                    assets=not args.metadata_only, release=args.release)
    errors.extend(rights_errors)
    warnings.extend(rights_warnings)
    report = {'passed': not errors, 'entries': len(data['entries']), 'boards': len(data['boards']),
              'asset_checks': not args.metadata_only, 'errors': errors, 'warnings': warnings}
    path = local_path(ROOT, args.report)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
