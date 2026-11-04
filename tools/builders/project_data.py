"""Portable, additive contribution data and permanent public identifiers."""
import copy
import hashlib
import json
import re
from pathlib import Path


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, indent=2) + '\n'
    if not path.exists() or path.read_text(encoding='utf-8') != text:
        path.write_text(text, encoding='utf-8')


def contribution_data(root):
    result = {key: [] for key in ('categories', 'entries', 'boards', 'references')}
    for path in sorted((root / 'source/contributions').glob('*.json')):
        payload = read_json(path)
        if payload.get('schema') != 'female-appearance-contribution/v1':
            raise ValueError(f'{path.name}: unsupported contribution schema')
        for key in result:
            result[key].extend(copy.deepcopy(payload.get(key, [])))
        for entry in payload.get('entries', []):
            if not entry.get('stable_id'):
                raise ValueError(f'{path.name}: each contributed entry needs stable_id')
    return result


def source_key(entry):
    return entry.get('source_key') or '|'.join(entry[key] for key in ('category', 'name', 'en'))


def assign_ids(root, entries, categories, prefixes):
    path = root / 'source/id-registry.json'
    registry = read_json(path)
    by_key = {record['source_key']: record for record in registry['entries']}
    by_id = {record['id']: record for record in registry['entries']}
    if len(by_key) != len(by_id):
        raise ValueError('Duplicate ID or source_key in id-registry.json')
    prefix_for = dict(zip((category['id'] for category in categories), prefixes))
    seen = set()
    for entry in entries:
        key = source_key(entry)
        explicit = entry.pop('stable_id', None)
        record = by_key.get(key)
        if explicit:
            record = by_id.get(explicit)
            if record and record['source_key'] != key:
                by_key.pop(record['source_key'], None)
                record['source_key'] = key
        if record is None:
            prefix = prefix_for.get(entry['category'])
            if not prefix:
                raise ValueError('No ID prefix for ' + entry['category'])
            number = max((int(identifier[len(prefix):]) for identifier in by_id
                          if re.fullmatch(re.escape(prefix) + r'\d+', identifier)), default=0) + 1
            identifier = explicit or f'{prefix}{number:03}'
            if not re.fullmatch(re.escape(prefix) + r'\d{3,}', identifier):
                raise ValueError('A new stable_id must use its category prefix: ' + identifier)
            if not re.fullmatch(r'[A-Z][A-Z0-9_]*\d{3,}', identifier):
                raise ValueError('Invalid stable_id: ' + identifier)
            record = {'id': identifier, 'source_key': key}
            registry['entries'].append(record)
            by_id[identifier] = record
        if explicit and record['id'] != explicit:
            raise ValueError('stable_id does not match registered source_key: ' + key)
        if record['id'] in seen:
            raise ValueError('Duplicate public ID: ' + record['id'])
        by_key[key] = record
        seen.add(record['id'])
        entry['id'] = record['id']
    # Records are never removed: retired IDs cannot be reassigned to a new term.
    return registry


def export_collaboration_data(root, data, navigation):
    domain = {cid: group for group in navigation['groups'] for cid in group['categories']}
    records = []
    for entry in data['entries']:
        group = domain.get(entry['category'], {})
        records.append({key: value for key, value in {
            'id': entry['id'], 'name': entry['name'], 'en': entry['en'],
            'category': entry['category'], 'category_name': entry['category_name'],
            'domain': group.get('id'), 'domain_name': group.get('name'),
            'dimension': entry['dimension'], 'aliases': entry.get('aliases', []),
            'styles': entry.get('styles', []), 'visual': entry.get('visual'),
            'fullbody_visual': entry.get('fullbody_visual'), 'wearing_visual': entry.get('wearing_visual'),
            'detail_url': f"index.html?section={entry['category']}&entry={entry['id']}",
        }.items() if value is not None})
    path = root / 'data/agent-index.jsonl'
    path.write_text(''.join(json.dumps(record, ensure_ascii=False, separators=(',', ':')) + '\n'
                            for record in records), encoding='utf-8')
    fields = {}
    for entry in data['entries']:
        for key, value in entry.items():
            item = fields.setdefault(key, {'count': 0, 'types': []})
            item['count'] += 1
            kind = type(value).__name__
            if kind not in item['types']:
                item['types'].append(kind)
    write_json(root / 'data/field-inventory.json', {
        'schema': 'female-appearance-field-inventory/v1',
        'entry_count': len(records), 'fields': dict(sorted(fields.items()))})
    manifest = {'schema': 'female-appearance-data-manifest/v1', 'catalog_version': data['meta']['version'],
                'files': {}}
    for relative in ['data/catalog.json', 'data/navigation.json', 'data/agent-index.jsonl']:
        content = (root / relative).read_bytes()
        manifest['files'][relative] = {'bytes': len(content), 'sha256': hashlib.sha256(content).hexdigest()}
    write_json(root / 'data/manifest.json', manifest)
