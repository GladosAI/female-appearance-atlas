"""Query only catalog text; no network, image recognition or AI service required."""
import argparse
import csv
import io
import json
from pathlib import Path
import sys
from i18n_tools import load_locales, localize_entry, localized_text, normalize

ROOT = Path(__file__).resolve().parents[1]


def search(records, query='', category=None, domain=None, ids=None, locales=None):
    tokens = normalize(query).split()
    for record in records:
        if ids and record['id'] not in ids:
            continue
        if category and record['category'] != category:
            continue
        if domain and record.get('domain') != domain:
            continue
        parts = [str(record.get(key, '')) for key in
                 ['id', 'name', 'en', 'category_name', 'dimension', 'aliases']]
        for pack in (locales or {}).values():
            translated = pack.get('entries', {}).get(record['id'], {})
            parts.extend(str(translated.get(key, '')) for key in ['name', 'aliases'])
            parts.extend(localized_text(record.get(key, ''), pack) for key in
                         ['category_name', 'dimension', 'domain_name'])
        text = normalize(' '.join(parts))
        if all(token in text for token in tokens):
            yield record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='?', default='')
    parser.add_argument('--category')
    parser.add_argument('--domain')
    parser.add_argument('--id', action='append', dest='ids')
    parser.add_argument('--list', choices=['domains', 'categories'])
    parser.add_argument('--limit', type=int, default=20)
    parser.add_argument('--offset', type=int, default=0)
    parser.add_argument('--format', choices=['json', 'jsonl', 'csv'], default='json')
    parser.add_argument('--lang', choices=['zh', 'en', 'ja'], default='zh',
                        help='Display language; searches names/aliases across all three languages')
    parser.add_argument('--full', action='store_true', help='Include full descriptions and extension fields')
    args = parser.parse_args()
    if args.limit < 1 or args.limit > 1000 or args.offset < 0:
        parser.error('limit must be 1..1000; offset must be nonnegative')
    locales = load_locales(ROOT)
    if args.list:
        nav = json.loads((ROOT / 'data/navigation.json').read_text(encoding='utf-8'))
        records = nav['groups'] if args.list == 'domains' else json.loads((ROOT / 'data/catalog.json').read_text(encoding='utf-8'))['categories']
        if args.lang != 'zh':
            pack = locales.get(args.lang, {})
            records = [{**record, 'source_name': record['name'],
                        'name': localized_text(record['name'], pack)} for record in records]
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return
    records = [json.loads(line) for line in (ROOT / 'data/agent-index.jsonl').read_text(encoding='utf-8').splitlines() if line]
    matches = list(search(records, args.query, args.category, args.domain, set(args.ids or []), locales))
    selected = matches[args.offset:args.offset + args.limit]
    if args.full:
        entries = {entry['id']: entry for entry in json.loads((ROOT / 'data/catalog.json').read_text(encoding='utf-8'))['entries']}
        selected = [{**entry, **entries[entry['id']]} for entry in selected]
    selected = [localize_entry(entry, args.lang, locales) for entry in selected]
    if args.format == 'json':
        print(json.dumps({'total': len(matches), 'offset': args.offset, 'items': selected}, ensure_ascii=False, indent=2))
    elif args.format == 'jsonl':
        for entry in selected:
            print(json.dumps(entry, ensure_ascii=False))
    else:
        output = io.StringIO(newline='')
        columns = ['id', 'name', 'en', 'category', 'category_name', 'domain', 'dimension', 'detail_url']
        if args.lang != 'zh':
            columns.extend(['source_name', 'source_category_name', 'dimension_label',
                            'locale', 'name_locale', 'translation_fallback'])
        writer = csv.DictWriter(output, columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(selected)
        print(output.getvalue(), end='')


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    main()
