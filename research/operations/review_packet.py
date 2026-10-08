"""Validate retrospective-only packets without issuing cards or admitting grades.

Frozen source headings and local reservations are custody, not canonical issues.
Supplied research claims remain unadmitted until a separate field-level audit.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import os
import re


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def append_audit(projection, log_path, receipt_dir, ledger_path, following, fault=None):
    """Journal a recoverable diagnostic exhibit under the shared ledger lock.

    The exhibit consumes no ID and writes no canonical ledger record. A completed
    identical publication is a readback; an interrupted partial append resumes
    only when every byte matches the prepared prefix and intended projection.
    """
    from research.src.ledger import locked
    require(not re.search(rb'(?m)^(?:#{1,6}\s+(?:Prediction\s+|Game(?:\s+Card)?\s+)?P-\d+\b|<!-- BEGIN CANONICAL (?:ISSUE|RESEARCH) P-\d+)', projection),
            'Audit contains a canonical/local card heading or issue marker')
    log_path, receipt_dir, ledger_path = map(Path, (log_path, receipt_dir, ledger_path))
    receipt_dir.mkdir(parents=True, exist_ok=True)
    prepared, committed = receipt_dir/'append_prepared.json', receipt_dir/'append_receipt.json'
    with locked(ledger_path):
        raw = log_path.read_bytes()
        ledger = ledger_path.read_bytes() if ledger_path.exists() else b''
        if committed.exists():
            record = json.loads(committed.read_text(encoding='utf-8'))
            start = record['before_bytes']
            require(record['projection_sha256'] == sha(projection) and sha(raw[:start]) == record['before_sha256']
                    and raw[start:start + len(projection)] == projection, 'Completed audit custody changed')
            return {**record, 'duplicate': True}
        if prepared.exists():
            record = json.loads(prepared.read_text(encoding='utf-8'))
            require(record['projection_sha256'] == sha(projection), 'Prepared projection changed')
        else:
            record = dict(prepared_utc=datetime.now(timezone.utc).isoformat(), before_bytes=len(raw), before_sha256=sha(raw),
                          projection_bytes=len(projection), projection_sha256=sha(projection),
                          ledger_before_bytes=len(ledger), ledger_before_sha256=sha(ledger), next_id_before=following())
            with prepared.open('x', encoding='utf-8') as handle:
                json.dump(record, handle, indent=2); handle.write('\n'); handle.flush(); os.fsync(handle.fileno())
        start = record['before_bytes']
        require(len(raw) >= start and sha(raw[:start]) == record['before_sha256'], 'Pre-audit log prefix changed')
        require(len(ledger) == record['ledger_before_bytes'] and sha(ledger) == record['ledger_before_sha256'], 'Ledger changed during pending audit')
        require(projection.startswith(raw[start:]), 'Unrelated bytes follow pending audit')
        if fault == 'partial':
            with log_path.open('ab') as handle:
                handle.write(projection[len(raw) - start:len(raw) - start + 17]); handle.flush(); os.fsync(handle.fileno())
            raise RuntimeError('simulated interrupted audit')
        with log_path.open('ab') as handle:
            handle.write(projection[len(raw) - start:]); handle.flush(); os.fsync(handle.fileno())
        after = log_path.read_bytes()
        require(after == raw[:start] + projection, 'Audit append readback differs')
        require((ledger_path.read_bytes() if ledger_path.exists() else b'') == ledger, 'Audit changed canonical ledger')
        result = {**record, 'committed_utc': datetime.now(timezone.utc).isoformat(), 'after_sha256': sha(after),
                  'ledger_after_sha256': sha(ledger), 'next_id_after': following(), 'new_ids': [], 'new_formal_grades': 0}
        require(result['next_id_after'] == record['next_id_before'], 'Audit consumed an ID')
        with committed.open('x', encoding='utf-8') as handle:
            json.dump(result, handle, indent=2); handle.write('\n'); handle.flush(); os.fsync(handle.fileno())
        return {**result, 'duplicate': False}


def reference_class(card_id, committed_research_ids):
    if card_id in {f'P-{n}' for n in range(518, 523)}:
        return 'RESERVED_DOCUMENTARY_REFERENCE_NOT_COMMITTED'
    if card_id in committed_research_ids:
        return 'COMMITTED_RESEARCH_CARD_NOT_CERTIFIED'
    return 'HISTORICAL_DOCUMENTARY_REFERENCE_NOT_CERTIFIED'


def parse_reviews(supplement, expected_ids, excluded_ids=()):
    """Require one complete twelve-part review per selected ID, in supplied order."""
    headings = list(re.finditer(r'(?m)^### LOCAL SETTLEMENT REVIEW [^\n]*? (P-\d+) [^\n]*$', supplement))
    ids = [m[1] for m in headings]
    require(len(ids) == len(set(ids)), 'Duplicate retrospective ID')
    require(not set(ids) & set(excluded_ids), 'Excluded event has a retrospective')
    require(ids == list(expected_ids), 'Retrospective order or coverage differs from selected IDs')
    reviews = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(supplement)
        block = supplement[heading.start():end]
        # The final historical metric appendix is retained but is not R12 text.
        block = re.split(r'(?m)^## HISTORICAL RANK DIAGNOSTICS', block, maxsplit=1)[0]
        fields = list(re.finditer(r'\*\*R(1[0-2]|[1-9])\s+[^*]*\*\*', block))
        require([int(m[1]) for m in fields] == list(range(1, 13)), 'Missing, duplicate or reordered review section: ' + heading[1])
        parts = {}
        for number, field in enumerate(fields):
            boundary = fields[number + 1].start() if number + 1 < len(fields) else len(block)
            text = block[field.end():boundary].strip()
            require(bool(text), 'Empty review section: ' + heading[1])
            parts['R' + field[1]] = text
        reviews.append(dict(id=heading[1], source_text=block, source_sha256=sha(block.encode('utf-8')),
                            retrospective=parts, performance_eligible=False))
    return reviews


def validate_packet(inputs, selected_manifest, committed_research_ids):
    inputs = Path(inputs)
    manifest = json.loads((inputs/'P126_P549_SETTLEMENT_MANIFEST.json').read_text(encoding='utf-8'))
    receipts = []
    absent = []
    for name, expected in manifest['file_hashes'].items():
        filename = 'ORIGINAL_MINI_FROZEN.md' if name.startswith('ORIGINAL_MINI/') else name
        path = inputs/('P126_P549_' + filename)
        if not path.exists():
            require(name == 'README.md', 'Missing required supplied artifact: ' + name)
            absent.append(name)
            continue
        body = path.read_bytes()
        require(len(body) == expected['size_bytes'] and sha(body) == expected['sha256'], 'Supplied hash/size mismatch: ' + name)
        receipts.append(dict(path=path.name, bytes=len(body), sha256=sha(body)))
    for path in [inputs/'P126_P549_SETTLEMENT_MANIFEST.json']:
        body = path.read_bytes()
        receipts.append(dict(path=path.name, bytes=len(body), sha256=sha(body)))
    original = (inputs/'P126_P549_ORIGINAL_MINI_FROZEN.md').read_bytes()
    settled = (inputs/'P126_P549_PREDICTION_MINI_SETTLED_P-126_P-549.md').read_bytes()
    require(settled.startswith(original), 'Settled copy changed frozen original prefix')
    require(sha(original) == manifest['original_file']['sha256'], 'Original receipt mismatch')
    supplement = settled[len(original):].decode('utf-8')
    require('APPENDED LOCAL SETTLEMENT & RETROSPECTIVE SUPPLEMENT' in supplement, 'Missing supplement boundary')
    ids = manifest['scope']['ids']
    require(len(ids) == len(set(ids)), 'Duplicate scope ID')
    selected = {r['canonical_id']: r for r in selected_manifest['records']}
    require(set(ids) == set(selected), 'Packet and selected carryover do not cover the same events')
    with (inputs/'P126_P549_RECONCILIATION_INVENTORY.csv').open(encoding='utf-8', newline='') as handle:
        inventory = list(csv.DictReader(handle))
    require([r['id'] for r in inventory] == ids, 'Inventory order or coverage differs from scope')
    require(all(r['canonical_mapping'] == r['id'] and r['certification_open'] == 'True' for r in inventory),
            'Inventory remaps IDs or closes certification')
    require(all(r['current_state'] == selected[r['id']]['current_state'] for r in inventory), 'Supplied current state differs from selected carryover')
    require(sum(r['active_for_next_mini'] == 'True' for r in inventory) == manifest['counts']['active_sporting_contract'],
            'Sporting/contract count does not reconcile')
    require(manifest['counts']['new_local_cards'] == manifest['counts']['newly_fully_resolved'] == 0, 'Packet is not retrospective-only')
    grades = manifest['formal_new_grade_counts']
    require(all(grades[k] == 0 for k in ('WIN', 'LOSS', 'PUSH', 'VOID', 'NO_ACTION', 'TERMINAL_CENSORED'))
            and grades['UNRESOLVED'] == len(ids), 'Unexpected new grade or denominator')
    require(manifest['counts']['new_rank_metrics_denominator'] == 0, 'Historical diagnostic cohort recounted')
    excluded = manifest['scope']['explicitly_excluded']
    require(excluded == 'P-550' and excluded not in ids, 'Excluded local event changed')
    reviews = parse_reviews(supplement, ids, [excluded])
    for review in reviews:
        review['reference_class'] = reference_class(review['id'], committed_research_ids)
        review['source_claim_status'] = 'SUPPLIED_POST_EVENT_CLAIM_NOT_ADMITTED'
        review['new_formal_grade'] = None
    return dict(manifest=manifest, receipts=receipts, missing_optional_artifacts=absent, reviews=reviews,
                supplement=supplement, inventory=inventory, original_prefix_bytes=len(original),
                original_prefix_sha256=sha(original), new_grade_count=0, new_event_count=0)
