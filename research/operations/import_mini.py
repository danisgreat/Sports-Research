"""Canonical import of a settled local mini (format mini-log-2) into the active Combined Log.

Prompt 4 workflow. `plan` is read-only. `apply` re-plans, refuses any blocking issue, then
commits each new card through research.operations.log_card (ledger lock, journal, readback),
appends each pre-settlement ADDENDUM block (corrections, late news) and finally appends each
settlement as a dated addendum, all under the card's own canonical ID.

  python -B -m research.operations.import_mini plan  --frozen FROZEN.md --settled SETTLED.md --out DIR   (writes IMPORT_PLAN.json only)
  python -B -m research.operations.import_mini apply --frozen FROZEN.md --settled SETTLED.md --out DIR

Local working IDs are retained: before each commit the allocator's next ID must equal the
card's local ID, otherwise the import stops (collision). Nothing is renumbered.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

from research.operations import log_card, mini_log
from research.src.issue import CANONICAL_LEDGER, RECONCILIATION
from research.src.ledger import read_records

BLOCKING = {'IDENTITY_CONFLICT', 'ID_COLLISION', 'SOURCE_CUSTODY_UNRESOLVED', 'VALIDATION_FAILED'}
PACKET_FILES = ('SETTLEMENT_MANIFEST.json', 'LOCAL_ID_MAPPING.md', 'UNRESOLVED_CARRYOVER.md')


def check_manifest(settled_path: Path, frozen: bytes, settled: bytes, pending_ids):
    """Compare the local SETTLEMENT_MANIFEST.json (prompt 3), when present, with the actual files."""
    path = Path(settled_path).parent / 'SETTLEMENT_MANIFEST.json'
    if not path.exists():
        return [], ['no SETTLEMENT_MANIFEST.json beside the settled mini; hashes are taken from the files']
    try:
        manifest = json.loads(path.read_text(encoding='utf-8-sig'))
    except json.JSONDecodeError as exc:
        return [f'SETTLEMENT_MANIFEST.json is not valid JSON: {exc}'], []
    errors, warnings = [], []
    for key, raw in (('original', frozen), ('settled', settled)):
        recorded = str((manifest.get(key) or {}).get('sha256', 'NOT_COMPUTED'))
        if recorded.upper() == 'NOT_COMPUTED':
            warnings.append(f'manifest {key} SHA-256 NOT_COMPUTED; true value {sha(raw)}')
        elif recorded.lower() != sha(raw):
            errors.append(f'manifest {key} SHA-256 {recorded} does not match the file ({sha(raw)})')
    if 'pending_event_ids' in manifest and sorted(manifest['pending_event_ids']) != sorted(pending_ids):
        errors.append(f"manifest pending_event_ids {manifest['pending_event_ids']} differ from the settlement blocks {sorted(pending_ids)}")
    return errors, warnings


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _opts(options):
    options = dict(options or {})
    return (options.get('part6'), options.get('reconciliation', RECONCILIATION),
            options.get('ledger', CANONICAL_LEDGER), options.get('store'))


def plan(frozen_path: Path, settled_path: Path, options=None):
    part6, reconciliation, ledger, _ = _opts(options)
    frozen, settled = Path(frozen_path).read_bytes(), Path(settled_path).read_bytes()
    checked = mini_log.analyse_settled(frozen, settled)
    result = {'frozen_path': str(frozen_path), 'settled_path': str(settled_path),
              'frozen_sha256': sha(frozen), 'frozen_bytes': len(frozen),
              'settled_sha256': sha(settled), 'settled_bytes': len(settled),
              'validation_errors': checked['errors'], 'validation_warnings': checked['warnings'],
              'items': [], 'blocking': []}
    manifest_errors, manifest_warnings = check_manifest(settled_path, frozen, settled, checked['table']['pending_event_ids'])
    result['validation_errors'] += manifest_errors
    result['validation_warnings'] += manifest_warnings
    if result['validation_errors']:
        result['blocking'].append('VALIDATION_FAILED')
        return result, checked
    records = read_records(ledger)
    if log_card.pending(records):
        result['blocking'].append('SOURCE_CUSTODY_UNRESOLVED')
        result['items'].append({'id': '-', 'classification': 'SOURCE_CUSTODY_UNRESOLVED',
                                'reason': 'pending canonical transaction; run log_card recover first'})
        return result, checked
    cards = log_card.research_cards(records)
    by_key = {c['event_key']: c for c in cards}
    by_id = {c['card_id']: c for c in cards}
    addenda = log_card.research_addenda(records)
    next_id = log_card.next_id(part6, reconciliation, ledger)
    result['next_id_before'] = next_id
    expected = mini_log.pid(next_id)
    stopped = False
    settlements = {r['id']: r for r in checked['table']['records']}
    frozen_blocks = {b['id']: b for b in mini_log.blocks(frozen) if b['kind'] in ('CARD', 'CARRYOVER')}
    settle_blocks = {b['id']: b for b in mini_log.blocks(settled[len(frozen):]) if b['kind'] == 'SETTLEMENT'}
    for card in checked['frozen']['cards']:
        cid, meta = card['id'], card['meta']
        body = frozen_blocks[cid]['body']
        item = {'id': cid, 'kind': 'CARD', 'event_key': meta['Event key'], 'title': card['heading'],
                'card_sha256': sha(body), 'settlement_state': settlements.get(cid, {}).get('state')}
        old = by_key.get(meta['Event key'])
        if old:
            same = old['source_sha256'] == sha(body) and old['body_sha256'] == sha(body)
            if same and old['card_id'] == cid:
                item['classification'] = 'ALREADY_IMPORTED_EXACT'
            else:
                item['classification'] = 'IDENTITY_CONFLICT'
                item['reason'] = f"event key already canonical as {old['card_id']} with different id or bytes"
        elif cid in by_id:
            item['classification'] = 'IDENTITY_CONFLICT'
            item['reason'] = f"{cid} is already a different canonical event ({by_id[cid]['event_key']})"
        elif stopped or mini_log.pid(cid) != expected:
            item['classification'] = 'ID_COLLISION'
            item['reason'] = (f'allocator would assign P-{expected}, not {cid}' if not stopped
                              else 'an earlier card could not be imported; ordering forbids continuing')
            stopped = True
        else:
            item['classification'] = 'NEW_CANONICAL_EVENT'
            expected += 1
        result['items'].append(item)
    for carry in checked['frozen']['carryovers']:
        cid = carry['id']
        item = {'id': cid, 'kind': 'CARRYOVER', 'event_key': carry['meta'].get('Event key'),
                'settlement_state': settlements.get(cid, {}).get('state')}
        old = by_id.get(cid)
        if old is None or old['event_key'] != carry['meta'].get('Event key'):
            item['classification'] = 'SOURCE_CUSTODY_UNRESOLVED'
            item['reason'] = 'carryover must already be a canonical ledger card with the same event key'
        else:
            item['classification'] = 'CARRYOVER_REFERENCE_ONLY'
        result['items'].append(item)
    known = {i['id'] for i in result['items']
             if i['classification'] in {'NEW_CANONICAL_EVENT', 'ALREADY_IMPORTED_EXACT', 'CARRYOVER_REFERENCE_ONLY'}}
    result['addenda'] = []
    for n, block in enumerate(b for b in mini_log.blocks(frozen) if b['kind'] == 'ADDENDUM'):
        body = block['body']
        entry = {'id': block['id'], 'sequence': n + 1, 'addendum_sha256': sha(body)}
        if block['id'] in known or block['id'] in by_id:
            done = any(a['card_id'] == block['id'] and a['source_sha256'] == sha(body) for a in addenda)
            entry['status'] = 'ALREADY_COMMITTED' if done else 'TO_APPEND'
        elif any(i['id'] == block['id'] for i in result['items']):
            entry['status'] = 'PARENT_BLOCKED'
            entry['reason'] = 'its card is blocked above; resolve the card first'
        else:
            entry['status'] = 'SOURCE_CUSTODY_UNRESOLVED'
            entry['reason'] = 'addendum parent is neither imported by this mini nor a canonical ledger card'
        result['addenda'].append(entry)
    for item in result['items']:
        block = settle_blocks.get(item['id'])
        if item.get('settlement_state') == 'SETTLED' and block is not None:
            body = block['body']
            item['settlement_sha256'] = sha(body)
            done = any(a['card_id'] == item['id'] and a['source_sha256'] == sha(body) for a in addenda)
            item['addendum'] = 'ALREADY_COMMITTED' if done else 'TO_APPEND'
        else:
            item['addendum'] = 'NONE (PENDING_EVENT carried forward)' if item.get('settlement_state') == 'PENDING_EVENT' else 'NONE'
    result['blocking'] = sorted({i['classification'] for i in result['items'] if i['classification'] in BLOCKING}
                                | {a['status'] for a in result['addenda'] if a['status'] in BLOCKING})
    result['new_cards'] = [i['id'] for i in result['items'] if i['classification'] == 'NEW_CANONICAL_EVENT']
    result['expected_next_id_after'] = f'P-{expected}'
    return result, checked


def _write_inputs(out: Path, frozen_path: Path, settled_path: Path):
    inputs = out / 'inputs'
    inputs.mkdir(parents=True, exist_ok=True)
    for path in (frozen_path, settled_path):
        target = inputs / Path(path).name
        if target.exists():
            if target.read_bytes() != Path(path).read_bytes():
                raise ValueError(f'{target} exists with different bytes; never overwrite custody inputs')
        else:
            shutil.copyfile(path, target)
    for name in PACKET_FILES:
        source = Path(settled_path).parent / name
        target = inputs / name
        if source.exists() and not target.exists():
            shutil.copyfile(source, target)
    return inputs


def apply(frozen_path: Path, settled_path: Path, out: Path, options=None):
    part6, reconciliation, ledger, store = _opts(options)
    out = Path(out)
    result, checked = plan(frozen_path, settled_path, options)
    if result['blocking']:
        raise ValueError('import blocked: ' + ', '.join(result['blocking']))
    _write_inputs(out, frozen_path, settled_path)
    sources = out / 'sources'
    requests = out / 'requests'
    sources.mkdir(exist_ok=True)
    requests.mkdir(exist_ok=True)
    frozen = Path(frozen_path).read_bytes()
    settled = Path(settled_path).read_bytes()
    frozen_blocks = {b['id']: b for b in mini_log.blocks(frozen) if b['kind'] == 'CARD'}
    settle_blocks = {b['id']: b for b in mini_log.blocks(settled[len(frozen):]) if b['kind'] == 'SETTLEMENT'}
    cards = {c['id']: c for c in checked['frozen']['cards']}
    kwargs = {k: v for k, v in dict(part6=part6, reconciliation=reconciliation, ledger=ledger, store=store).items() if v is not None}
    transactions = []
    for item in result['items']:
        if item['classification'] != 'NEW_CANONICAL_EVENT':
            continue
        cid = item['id']
        meta = cards[cid]['meta']
        current = log_card.next_id(part6, reconciliation, ledger)
        if current != cid:
            raise ValueError(f'allocator moved: next ID is {current}, card is {cid}; stop and reconcile')
        body = frozen_blocks[cid]['body']
        source = sources / f'{cid}.card.txt'
        source.write_bytes(body)
        native = meta.get('Native event ID')
        request = {'event_key': meta['Event key'], 'title': cards[cid]['heading'], 'tracking_handle': meta['Tracking alias'],
                   'analysis_status': meta['Analysis status'], 'league': meta.get('League'),
                   'native_event_id': None if not native or native.upper().startswith('NOT_') else native,
                   'body': body.decode('utf-8'), 'source_path': str(source)}
        (requests / f'{cid}.card.json').write_text(json.dumps(request, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        committed = log_card.commit(request, **kwargs)
        if committed['card_id'] != cid or committed['duplicate']:
            raise ValueError(f'{cid}: allocator returned {committed}; stop and reconcile')
        transactions.append({'id': cid, 'type': 'CARD', **committed})
    addendum_blocks = [b for b in mini_log.blocks(frozen) if b['kind'] == 'ADDENDUM']
    for entry, block in zip(result['addenda'], addendum_blocks):
        if entry['status'] != 'TO_APPEND':
            continue
        cid = entry['id']
        source = sources / f"{cid}.addendum-{entry['sequence']}.txt"
        source.write_bytes(block['body'])
        request = {'card_id': cid, 'body': block['body'].decode('utf-8'), 'source_path': str(source)}
        (requests / f"{cid}.addendum-{entry['sequence']}.json").write_text(json.dumps(request, indent=1, ensure_ascii=False) + '\n',
                                                                           encoding='utf-8')
        appended = log_card.addendum(request, **kwargs)
        if appended['card_id'] != cid:
            raise ValueError(f'{cid}: addendum attached to {appended["card_id"]}')
        transactions.append({'id': cid, 'type': 'CARD_ADDENDUM', 'sequence': entry['sequence'], **appended})
    for item in result['items']:
        if item.get('addendum') != 'TO_APPEND':
            continue
        cid = item['id']
        body = settle_blocks[cid]['body']
        source = sources / f'{cid}.settlement.txt'
        source.write_bytes(body)
        request = {'card_id': cid, 'body': body.decode('utf-8'), 'source_path': str(source)}
        (requests / f'{cid}.addendum.json').write_text(json.dumps(request, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        appended = log_card.addendum(request, **kwargs)
        if appended['card_id'] != cid:
            raise ValueError(f'{cid}: addendum attached to {appended["card_id"]}')
        transactions.append({'id': cid, 'type': 'SETTLEMENT_ADDENDUM', **appended})
    after = log_card.next_id(part6, reconciliation, ledger)
    if after != result['expected_next_id_after']:
        raise ValueError(f'next ID after import is {after}, expected {result["expected_next_id_after"]}')
    for card in log_card.research_cards(read_records(ledger)):
        log_card.verify_projection(card, log_card.active_log(log_card.ROOT) if part6 is None else part6)
    result.update(applied_utc=datetime.now(timezone.utc).isoformat(), transactions=transactions, next_id_after=after,
                  mini_status='CANONICALLY_IMPORTED_AND_ARCHIVED')
    write_reports(out, result, checked['table'])
    return result


def write_reports(out: Path, result: dict, table: dict):
    out.mkdir(parents=True, exist_ok=True)
    (out / 'settlement_table.json').write_text(json.dumps(table, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    (out / 'CANONICAL_IMPORT_MANIFEST.json').write_text(json.dumps(result, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    with (out / 'CANONICAL_ID_MAPPING.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(['local_id', 'canonical_id', 'kind', 'classification', 'event_key', 'card_sha256', 'settlement_sha256', 'addendum'])
        for item in result['items']:
            canonical = item['id'] if item['classification'] in {'NEW_CANONICAL_EVENT', 'ALREADY_IMPORTED_EXACT', 'CARRYOVER_REFERENCE_ONLY'} else ''
            writer.writerow([item['id'], canonical, item['kind'], item['classification'], item.get('event_key', ''),
                             item.get('card_sha256', ''), item.get('settlement_sha256', ''), item.get('addendum', '')])
    s = table['summary']
    t = s['totals']
    pending = table.get('pending_event_ids', [])
    lines = ['# Canonical import report', '',
             f"Applied UTC: {result.get('applied_utc', 'NOT_APPLIED (plan only)')}.",
             f"Frozen mini SHA-256 `{result['frozen_sha256']}` ({result['frozen_bytes']:,} B); settled mini SHA-256 `{result['settled_sha256']}` ({result['settled_bytes']:,} B).",
             f"Next canonical ID before: **{result.get('next_id_before')}**; after: **{result.get('next_id_after', result.get('expected_next_id_after'))}**.", '',
             '| Local ID | Classification | Addendum | Event key |', '|---|---|---|---|']
    lines += [f"| {i['id']} | {i['classification']} | {i.get('addendum', '')} | `{i.get('event_key', '')}` |" for i in result['items']]
    if result.get('addenda'):
        lines += ['', '## Pre-settlement addenda (corrections and late news; forecasts unchanged)', '',
                  '| # | ID | Status | SHA-256 |', '|---:|---|---|---|']
        lines += [f"| {a['sequence']} | {a['id']} | {a['status']} | `{a['addendum_sha256'][:16]}…` |" for a in result['addenda']]
    lines += ['', '## Settlement diagnostics (Rule T2: only ranks 1–2 count)', '',
              f"Counted wins {t.get('counted_wins', 0)} / {t.get('counted_live_rows', 0)} live top-two rows; "
              f"Rank 1 {t.get('rank1_W', 0)} W / {t.get('rank1_L', 0)} L / {t.get('rank1_V', 0)} VOID; "
              f"Rank 2 {t.get('rank2_W', 0)} W / {t.get('rank2_L', 0)} L / {t.get('rank2_V', 0)} VOID; Hit@2 {t.get('hit_at_2', 0)}; "
              f"mean NDCG@2 {s['mean_ndcg_at_2'] if s['mean_ndcg_at_2'] is not None else 'n/a'}.",
              f"Rank-1 failure classes: {s['rank1_failure_classes'] or 'none'}.", '',
              '## Carried forward', '',
              (', '.join(pending) + ' — PENDING_EVENT; carry into the next mini.') if pending else 'None.', '',
              '## Status', '',
              'Imported records remain `RESEARCH_ONLY_NOT_CERTIFIED`: a verified sporting result is not operator certification or pregame performance eligibility.']
    (out / 'CANONICAL_IMPORT_REPORT.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    dup = ['# Duplicate reconciliation', '']
    dup += [f"- {i['id']}: {i['classification']}{' — ' + i['reason'] if i.get('reason') else ''}" for i in result['items']
            if i['classification'] != 'NEW_CANONICAL_EVENT'] or ['- No duplicate, alias or already-imported record.']
    (out / 'DUPLICATE_RECONCILIATION.md').write_text('\n'.join(dup) + '\n', encoding='utf-8')
    unresolved = ['# Unresolved after import', '']
    unresolved += [f'- {cid}: PENDING_EVENT — carry into the next mini.' for cid in pending] or ['- None.']
    unresolved += ['', 'Certification (operator settlement, actual start, independent terminal quorum) remains unestablished for every record.']
    (out / 'UNRESOLVED_POST_IMPORT.md').write_text('\n'.join(unresolved) + '\n', encoding='utf-8')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', choices=['plan', 'apply'])
    parser.add_argument('--frozen', type=Path, required=True)
    parser.add_argument('--settled', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == 'plan':
            # The plan is a proposal only: it never writes settlement_table.json, so an unapplied
            # plan can never be counted by the cohort review.
            result, checked = plan(args.frozen, args.settled)
            args.out.mkdir(parents=True, exist_ok=True)
            (args.out / 'IMPORT_PLAN.json').write_text(json.dumps(result, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        else:
            result = apply(args.frozen, args.settled, args.out)
    except ValueError as exc:
        print(json.dumps({'passed': False, 'error': str(exc)}, indent=2))
        return 1
    print(json.dumps({k: result.get(k) for k in ('blocking', 'new_cards', 'next_id_before', 'expected_next_id_after',
                                                 'next_id_after', 'validation_errors')}, indent=2))
    return 1 if result['blocking'] else 0


if __name__ == '__main__':
    sys.exit(main())
