"""Inspect material audit records offline; does not publish or approve assets."""
import argparse
import json
from pathlib import Path
import sys

from rights_audit import summary, validate_rights
from validate_atlas import local_path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--status',choices=['review-needed','pending-owner-license','needs-input-review','cleared'])
    parser.add_argument('--path',help='Exact asset path to inspect')
    parser.add_argument('--metadata-only',action='store_true',help='Skip asset bytes; source-only checkout')
    args=parser.parse_args()
    read=lambda name:json.loads((ROOT/name).read_text(encoding='utf-8'))
    review=read('source/rights-review.json')
    errors,warnings=validate_rights(review,read('source/rights-evidence.json'),read('source/license-policy.json'),ROOT,local_path,assets=not args.metadata_only)
    result={'summary':summary(review),'errors':errors,'pending':warnings,'audit_scope':review.get('audit')}
    if args.status or args.path:
        result['assets']=[record for record in review['assets'] if (not args.status or record['status']==args.status) and (not args.path or record['path']==args.path)]
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 1 if errors else 0


if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
