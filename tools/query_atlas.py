"""Query only catalog text; no network, image recognition or AI service required."""
import argparse
import csv
import io
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def search(records, query='', category=None, domain=None, ids=None):
    tokens = query.casefold().split()
    for record in records:
        if ids and record['id'] not in ids:
            continue
        if category and record['category'] != category:
            continue
        if domain and record.get('domain') != domain:
            continue
        text = ' '.join(str(record.get(key, '')) for key in
                        ['id', 'name', 'en', 'category_name', 'dimension', 'aliases']).casefold()
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
    parser.add_argument('--full', action='store_true', help='Include full descriptions and extension fields')
    args = parser.parse_args()
    if args.limit < 1 or args.limit > 1000 or args.offset < 0:
        parser.error('limit must be 1..1000; offset must be nonnegative')
    if args.list:
        nav = json.loads((ROOT / 'data/navigation.json').read_text(encoding='utf-8'))
        records = nav['groups'] if args.list == 'domains' else json.loads((ROOT / 'data/catalog.json').read_text(encoding='utf-8'))['categories']
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return
    records = [json.loads(line) for line in (ROOT / 'data/agent-index.jsonl').read_text(encoding='utf-8').splitlines() if line]
    matches = list(search(records, args.query, args.category, args.domain, set(args.ids or [])))
    selected = matches[args.offset:args.offset + args.limit]
    if args.full:
        entries = {entry['id']: entry for entry in json.loads((ROOT / 'data/catalog.json').read_text(encoding='utf-8'))['entries']}
        selected = [{**entry, **entries[entry['id']]} for entry in selected]
    if args.format == 'json':
        print(json.dumps({'total': len(matches), 'offset': args.offset, 'items': selected}, ensure_ascii=False, indent=2))
    elif args.format == 'jsonl':
        for entry in selected:
            print(json.dumps(entry, ensure_ascii=False))
    else:
        output = io.StringIO(newline='')
        columns = ['id', 'name', 'en', 'category', 'category_name', 'domain', 'dimension', 'detail_url']
        writer = csv.DictWriter(output, columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(selected)
        print(output.getvalue(), end='')


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    main()
