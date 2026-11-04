"""Evidence checks for scoped code/content licensing; never grants a license."""
from collections import Counter
import hashlib


def summary(review):
    assets = review.get('assets', [])
    return {
        'assets': len(assets),
        'status': dict(Counter(item.get('status', 'missing') for item in assets)),
        'kind': dict(Counter(item.get('kind', 'missing') for item in assets)),
        'provenance': dict(Counter(item.get('provenance', {}).get('status', 'not-reviewed') for item in assets)),
        'targeted_visual_assets': sum(bool(item.get('visual_review')) for item in assets),
    }


def validate_rights(review, evidence, policy, root, resolver, *, assets=True, release=False):
    errors, warnings = [], []
    def issue(message):
        (errors if release else warnings).append(message)
    records = review.get('assets', [])
    paths = [record.get('path') for record in records]
    if None in paths or len(paths) != len(set(paths)):
        errors.append('Rights records contain missing or duplicate asset paths')
    sources = evidence.get('records', [])
    ids = [source.get('id') for source in sources]
    if None in ids or len(ids) != len(set(ids)):
        errors.append('Rights evidence contains missing or duplicate identifiers')
    by_id = {source.get('id'): source for source in sources}
    allowed_status = {'review-needed', 'pending-owner-license', 'needs-input-review', 'cleared'}
    project_categories = {'ai-catalog-declaration':'ai_images', 'ai-generated-reference':'ai_images',
                          'project-brand-asset':'brand_artwork'}
    for record in records:
        name = record.get('path', '(missing)')
        try:
            path = resolver(root, name)
        except (TypeError, ValueError) as error:
            errors.append('Invalid rights asset path: ' + str(error))
            continue
        if record.get('status') not in allowed_status:
            errors.append('Invalid rights status: ' + name)
        refs = record.get('evidence_ids', [])
        if not isinstance(refs, list) or any(ref not in by_id for ref in refs):
            errors.append('Unknown rights evidence: ' + name)
            refs = []
        provenance = record.get('provenance', {})
        observed = provenance.get('observed_sha256')
        if observed and observed != record.get('sha256'):
            errors.append('Provenance hash differs from reviewed asset: ' + name)
        if record.get('status') == 'cleared':
            if not record.get('license') or not refs or not provenance.get('status'):
                errors.append('Cleared asset requires a license and provenance evidence: ' + name)
            if not any(by_id[ref].get('permission_basis') for ref in refs):
                errors.append('Cleared asset lacks permission basis: ' + name)
            if not any(by_id[ref].get('local_sha256') == record.get('sha256')
                       and by_id[ref].get('license') == record.get('license') for ref in refs):
                errors.append('Cleared asset lacks asset-specific matching license evidence: ' + name)
            category = project_categories.get(record.get('kind'))
            selected = policy.get(category, {}) if category else {}
            if selected.get('status') == 'selected' and record.get('license') != selected.get('license'):
                errors.append('Asset license differs from selected project policy: ' + name)
            for ref in refs:
                grant = by_id[ref]
                if grant.get('kind') != 'owner-asset-license-grant':
                    continue
                decision = by_id.get(grant.get('authorization'), {})
                if not category:
                    errors.append('Project owner grant cannot clear third-party material: ' + name)
                if (grant.get('asset') != name or grant.get('local_sha256') != record.get('sha256')
                        or grant.get('license') != record.get('license')
                        or decision.get('kind') != 'owner-license-decision'
                        or decision.get('license') != record.get('license')):
                    errors.append('Owner grant does not match asset and license decision: ' + name)
        if assets and (release or observed):
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != record.get('sha256'):
                errors.append('Rights review checksum is stale: ' + name)
    code = policy.get('code', {})
    if code.get('status') != 'selected' or code.get('spdx') != 'MIT':
        issue('Code license has not been recorded as the owner-selected MIT license')
    for field in ['text', 'scope']:
        try:
            file = resolver(root, code.get(field, ''))
            if not file.is_file():
                issue('Missing code license ' + field)
        except (ValueError, TypeError):
            errors.append('Invalid code license ' + field)
    for category in ['editorial_content', 'ai_images', 'brand_artwork']:
        entry = policy.get(category, {})
        if entry.get('status') != 'selected' or not entry.get('license'):
            issue('Content license remains undecided: ' + category)
            continue
        try:
            text_path = resolver(root, entry.get('text', ''))
            if not text_path.is_file():
                issue('Missing content license text: ' + category)
            elif entry.get('text_sha256') and hashlib.sha256(text_path.read_bytes()).hexdigest() != entry['text_sha256']:
                errors.append('Content license text checksum is stale: ' + category)
        except (ValueError, TypeError):
            errors.append('Invalid content license text path: ' + category)
        if entry.get('decision_evidence'):
            decision = by_id.get(entry['decision_evidence'], {})
            if decision.get('kind') != 'owner-license-decision' or decision.get('license') != entry['license']:
                errors.append('Content policy lacks matching owner decision: ' + category)
    pending = sum(item.get('status') != 'cleared' for item in records)
    if pending:
        issue(f'{pending} asset distribution decisions remain pending; see docs/material-rights-audit.md')
    return errors, warnings
