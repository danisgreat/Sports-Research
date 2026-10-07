"""Append requested research cards to the active combined log regardless of calibration.

Canonical IDs identify retained cards. RESEARCH_LOG records do not impersonate
certified ISSUE records or confer prospective performance eligibility.
Run: py -3.14 -m research.operations.log_card commit card.json
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PureWindowsPath
import re
import uuid
from research.src.issue import PART6, RECONCILIATION, CANONICAL_LEDGER, _custody
from research.operations.canonical_issue import next_card_id
from research.src.ledger import _append_locked, locked, read_records
from research.src.combined_log import active_log, custody

ROOT = PART6.parents[1]
PREPARED = "RESEARCH_LOG_PREPARED"
COMMITTED = "RESEARCH_LOG_COMMITTED"
ADDENDUM_PREPARED = 'RESEARCH_ADDENDUM_PREPARED'
ADDENDUM_COMMITTED = 'RESEARCH_ADDENDUM_COMMITTED'

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def pending(records):
    done = {r['payload']['transaction_id'] for r in records if r['record_type'] in {COMMITTED, ADDENDUM_COMMITTED}}
    return [r for r in records if r['record_type'] in {PREPARED, ADDENDUM_PREPARED} and r['payload']['transaction_id'] not in done]

def research_addenda(records):
    preparations = {r['payload']['transaction_id']:r for r in records if r['record_type'] == ADDENDUM_PREPARED}
    cards = {c['card_id']:c for c in research_cards(records)}
    out, seen = [], set()
    for r in records:
        if r['record_type'] != ADDENDUM_COMMITTED: continue
        p = r['payload']; prep = preparations.get(p['transaction_id'])
        if prep is None or p['prepared_record_sha256'] != prep['record_sha256']:
            raise ValueError('addendum commit has no matching preparation')
        core = prep['payload']
        if any(p[k] != core[k] for k in ['card_id','event_key','projection_sha256']):
            raise ValueError('addendum identity or projection changed')
        if core['card_id'] not in cards or cards[core['card_id']]['event_key'] != core['event_key'] or p['transaction_id'] in seen:
            raise ValueError('addendum parent absent or duplicated')
        seen.add(p['transaction_id']); out.append(core)
    return out

def research_cards(records):
    preparations = {r['payload']['transaction_id']:r for r in records if r['record_type'] == PREPARED}
    out, ids, events = [], set(), set()
    for r in records:
        if r['record_type'] != COMMITTED: continue
        p = r['payload']; earlier = preparations.get(p['transaction_id'])
        if earlier is None or p['prepared_record_sha256'] != earlier['record_sha256']:
            raise ValueError('research commit has no matching preparation')
        core = earlier['payload']
        if any(p[k] != core[k] for k in ['card_id','event_key','projection_sha256']):
            raise ValueError('research commit identity or projection changed')
        if core['card_id'] in ids or core['event_key'] in events:
            raise ValueError('duplicate research ID or event')
        ids.add(core['card_id']); events.add(core['event_key'])
        out.append({**core, 'commit_sha256':r['record_sha256']})
    return out

def retained_path(value):
    """Resolve the ledger's historical store paths after checkout relocation.

    Existing absolute paths remain valid. Only the exact canonical research
    store suffix may be relocated; its immutable hash is checked by callers.
    """
    parts = PureWindowsPath(value).parts
    if '..' in parts: raise ValueError('retained path traversal')
    path = Path(value)
    if path.is_absolute() and path.exists(): return path
    if len(parts) >= 3 and parts[-3:-1] == ('research', 'issued_research'):
        return ROOT/'research'/'issued_research'/parts[-1]
    raise ValueError('retained path outside canonical research store')

def stored_path(path):
    try:
        relative = path.relative_to(ROOT).as_posix()
        return relative if relative.startswith('research/issued_research/') else str(path)
    except ValueError: return str(path)

def projection_log(card, fallback):
    value = card.get('combined_log_path')
    if value:
        path = Path(value)
        if not path.is_absolute():
            if '..' in path.parts or not value.startswith('prediction logs/'):
                raise ValueError('invalid retained combined log path')
            path = ROOT / path
        return path
    # Historical preparations always remain in Part 6 after a rollover.
    if Path(fallback).resolve() == active_log(ROOT).resolve():
        return PART6
    return Path(fallback)

def verify_projection(card, part6):
    raw, _ = custody(projection_log(card, part6))
    projection = retained_path(card['projection_path']).read_bytes()
    if sha(projection) != card['projection_sha256'] or raw.count(projection) != 1:
        raise ValueError('canonical research projection missing, duplicated or changed')
    if sha(retained_path(card['source_path']).read_bytes()) != card['source_sha256']:
        raise ValueError('retained original research source changed')
    return projection

def next_id(part6=None, reconciliation=RECONCILIATION, ledger=CANONICAL_LEDGER):
    part6 = Path(part6) if part6 is not None else active_log(ROOT)
    records = read_records(ledger)
    if pending(records): raise ValueError('recover pending research append before another ID')
    for card in research_cards(records): verify_projection(card, part6)
    for addendum in research_addenda(records): verify_projection(addendum, part6)
    return next_card_id(part6, reconciliation, ledger)

def _sync_status(part6, reconciliation, ledger):
    """Refresh the living register after commitment/recovery; keep old history."""
    if Path(part6).resolve() not in {PART6.resolve(), active_log(ROOT).resolve()}: return
    cards=research_cards(read_records(ledger))
    following=next_id(part6,reconciliation,ledger)
    path=ROOT/'GAME_LOG_STATUS_CURRENT.md'
    old=path.read_bytes() if path.exists() else b''
    begin=b'<!-- BEGIN CURRENT RESEARCH QUEUE -->'
    end=b'<!-- END CURRENT RESEARCH QUEUE -->'
    if old.startswith(begin):
        boundary=old.index(end)+len(end)
        old=old[boundary:].lstrip(b'\r\n')
    history='## Historical status snapshots — superseded for current queue'.encode('utf-8')
    while old.startswith(history):
        old=old[len(history):].lstrip(b'\r\n')
    method=(ROOT/'METHOD.md').read_text(encoding='utf-8-sig') if (ROOT/'METHOD.md').exists() else ''
    match=re.search(r'Active freeze:\s*\[([^\]]+)\]',method)
    freeze=match[1] if match else 'NOT_RECORDED'
    receipt=ROOT/freeze
    freeze_sha=sha(receipt.read_text(encoding='utf-8-sig').replace('\r\n','\n').replace('\r','\n').replace('\n','\r\n').encode('utf-8')) if receipt.exists() else 'NOT_RECORDED'
    lines=[begin.decode(),'# Current canonical research queue','',
           f'**Next canonical ID: {following}.** All requested cards go directly to the active combined log, regardless of calibration. Canonical IDs identify retained cards; performance certification and live/late timing are separate labels.',
           f'Active Combined Log: `{active_log(ROOT).relative_to(ROOT).as_posix()}`.',
           f'Current selected freeze: `{freeze}`; normalized-CRLF SHA-256 `{freeze_sha}`. Current authority: METHOD.md and CURRENT_RULES.md.','',
           '| ID | Event | Tracking alias | Status |','|---|---|---|---|']
    # The frozen legacy extractor reads plain P-ID rows as its 517-slot index.
    # Research queue IDs are ledger-owned and formatted distinctly from that index.
    lines += [f"| **{c['card_id']}** | {c['title']} | `{c['tracking_handle']}` | {c['analysis_status']} |" for c in cards]
    closure=ROOT/'research/verification/closure_2026-10-05/mini_archive_manifest.json'
    if closure.exists():
        archive=json.loads(closure.read_text(encoding='utf-8'))
        lines += ['',f"Highest canonical research ID: **{cards[-1]['card_id']}**. Active Combined Log: `{active_log(ROOT).relative_to(ROOT).as_posix()}`.",
                  'Archived mini references: '+', '.join('`'+a['archive_path']+'`' for a in archive['archives'])+'.',
                  'Unresolved carryover P-523–P-537: `research/verification/closure_2026-10-05/carryover.json` and `carryover.md`. Eleven diagnostic settlements and twelve-part retrospectives are retained in Part 6; formal certification remains unresolved.']
    from research.operations.settlement_register import selected
    current=selected(ROOT)
    if current:
        manifest=current['manifest']
        lines += ['', '**Current all-log settlement register:** `'+current['manifest_path']+'`.',
                  f"{manifest['event_count']} event records retain specific settlement/certification requirements; {manifest['documentary_repairs']} older rank/contract mappings were repaired. The earlier 15-record closure is a historical snapshot. New sporting reviews and existing retrospective pointers are recorded in the current register; operator or source gaps remain literal.",
                  'Local working files are the authority. GitHub main is their publication destination; fetch comparisons do not replace local authoritative files.']
    lines += ['', 'P-518–P-522 remain reserved. Mini logs are reference/fallback copies. Run `research.operations.log_card verify` to verify actual projections, source hashes and next ID.',
              '', end.decode(),'','## Historical status snapshots — superseded for current queue','']
    new='\r\n'.join(lines).encode('utf-8')+old
    temporary=path.with_name(path.name+'.'+uuid.uuid4().hex+'.tmp')
    with temporary.open('xb') as handle:handle.write(new);handle.flush();os.fsync(handle.fileno())
    os.replace(temporary,path)

def _finish(preparation, ledger, part6):
    p = preparation['payload']
    projection = retained_path(p['projection_path']).read_bytes()
    if sha(projection) != p['projection_sha256'] or sha(retained_path(p['source_path']).read_bytes()) != p['source_sha256']:
        raise ValueError('pending transaction retained source/projection changed')
    part6 = projection_log(p, part6)
    raw, _ = custody(part6)
    before = p['part6_before_bytes']
    if len(raw) < before or sha(raw[:before]) != p['part6_before_sha256']:
        raise ValueError('Combined log changed outside the pending append; manual audit required')
    tail = raw[before:]
    if not projection.startswith(tail):
        raise ValueError('unrelated bytes follow pending append; manual audit required')
    with Path(part6).open('ab') as handle:
        handle.write(projection[len(tail):]); handle.flush(); os.fsync(handle.fileno())
    verify_projection(p, part6)
    kind = ADDENDUM_COMMITTED if preparation['record_type'] == ADDENDUM_PREPARED else COMMITTED
    return _append_locked(ledger, kind, {
        'transaction_id':p['transaction_id'], 'prepared_record_sha256':preparation['record_sha256'],
        'card_id':p['card_id'], 'event_key':p['event_key'], 'projection_sha256':p['projection_sha256'],
        'performance_status':'RESEARCH_ONLY_NOT_CERTIFIED'})

def recover(*, part6=None, ledger=CANONICAL_LEDGER):
    part6 = Path(part6) if part6 is not None else active_log(ROOT)
    with locked(ledger):
        records = read_records(ledger); todo = pending(records)
        if len(todo) > 1: raise ValueError('multiple pending appends require audit')
        result = _finish(todo[0], ledger, part6) if todo else None
        for card in research_cards(read_records(ledger)): verify_projection(card, part6)
        for addendum in research_addenda(read_records(ledger)): verify_projection(addendum, part6)
        _sync_status(part6, RECONCILIATION, ledger)
        return result

def commit(card, *, part6=None, reconciliation=RECONCILIATION, ledger=CANONICAL_LEDGER,
           store=None, fault=None):
    """Retain immutable originals, journal, append, read back, then commit.

    Existing event requests return their ID. Changed content requires an explicit
    dated addendum, rather than silently reissuing or editing the earlier card.
    fault is solely an interruption hook used by recovery tests.
    """
    if not all(isinstance(card.get(k), str) and card[k].strip() for k in
               ['event_key','title','tracking_handle','analysis_status','body','source_path']):
        raise ValueError('card needs explicit identity, title, status, body and original source')
    if re.search(r'(?m)^#{1,6}\s+(?:Prediction\s+|Game(?:\s+Card)?\s+)?P-\d+\b', card['body']):
        raise ValueError('nested canonical ID heading would consume extra IDs')
    part6 = Path(part6) if part6 is not None else active_log(ROOT)
    source = Path(card['source_path']).resolve().read_bytes()
    with locked(ledger):
        records = read_records(ledger)
        if pending(records): raise ValueError('recover pending research append first')
        old = next((c for c in research_cards(records) if c['event_key'] == card['event_key']), None)
        if old:
            verify_projection(old, part6)
            if old['source_sha256'] != sha(source) or old['body_sha256'] != sha(card['body'].encode('utf-8')):
                raise ValueError('event already logged with different text; use a dated addendum')
            _sync_status(part6,reconciliation,ledger)
            return {'card_id':old['card_id'], 'duplicate':True, 'record_sha256':old['commit_sha256']}
        if any(r['record_type'] in {'ISSUE_PREPARED','ISSUE_COMMITTED'} and
               r['payload'].get('event_id') == card.get('native_event_id') and
               r['payload'].get('league') == card.get('league') for r in records):
            raise ValueError('event already has certified issuance; append to its existing ID')
        card_id = next_id(part6, reconciliation, ledger)
        transaction_id = uuid.uuid4().hex
        stamp = datetime.now(timezone.utc).isoformat()
        text = (f"## {card_id} — {card['title']}\n\n"
                f"**CANONICAL RESEARCH CARD / {card['analysis_status']}.** SPORTS_ONLY / MARKET_BLIND.\n\n"
                f"Tracking alias: `{card['tracking_handle']}`. Logged UTC: {stamp}. "
                "This ID records the card; calibration and prospective certification are separate labels.\n\n"
                + card['body'].rstrip() + '\n')
        projection = (f'\r\n<!-- BEGIN CANONICAL RESEARCH {card_id} {transaction_id} -->\r\n'
                      + text.replace('\r\n','\n').replace('\n','\r\n')
                      + f'<!-- END CANONICAL RESEARCH {card_id} {transaction_id} -->\r\n').encode('utf-8')
        storage = Path(store or ROOT/'research/issued_research').resolve()
        storage.mkdir(parents=True, exist_ok=True)
        base = f'{card_id}-{transaction_id}'
        original = storage/(base+'.original.txt'); frozen = storage/(base+'.md')
        for path, raw in [(original, source), (frozen, projection)]:
            with path.open('xb') as handle:
                handle.write(raw); handle.flush(); os.fsync(handle.fileno())
        before, _ = custody(part6)
        payload = {k:card.get(k) for k in ['event_key','title','tracking_handle','analysis_status','league','native_event_id']}
        payload.update(combined_log_path=part6.relative_to(ROOT).as_posix() if part6.is_relative_to(ROOT/'prediction logs') else str(part6.resolve()),
                       transaction_id=transaction_id, card_id=card_id, logged_utc=stamp,
                       projection_path=stored_path(frozen), projection_sha256=sha(projection),
                       source_path=stored_path(original), source_sha256=sha(source),
                       body_sha256=sha(card['body'].encode('utf-8')),
                       part6_before_bytes=len(before), part6_before_sha256=sha(before),
                       performance_status='RESEARCH_ONLY_NOT_CERTIFIED')
        prepared = _append_locked(ledger, PREPARED, payload)
        if fault == 'prepared': raise RuntimeError('simulated interruption after preparation')
        if fault == 'partial':
            with Path(part6).open('ab') as handle: handle.write(projection[:71])
            raise RuntimeError('simulated partial append')
        result = _finish(prepared, ledger, part6)
        _sync_status(part6,reconciliation,ledger)
        return {'card_id':card_id, 'duplicate':False, 'record_sha256':result['record_sha256']}

def addendum(card, *, part6=None, reconciliation=RECONCILIATION, ledger=CANONICAL_LEDGER, store=None, fault=None):
    """Append a dated revision under its existing ID; never edit its forecast."""
    part6 = Path(part6) if part6 is not None else active_log(ROOT)
    if not all(isinstance(card.get(k),str) and card[k].strip() for k in ['card_id','body','source_path']):
        raise ValueError('addendum needs existing ID, body and retained original source')
    if re.search(r'(?m)^#{1,6}\s+(?:Prediction\s+|Game(?:\s+Card)?\s+)?P-\d+\b',card['body']):
        raise ValueError('nested canonical ID heading would consume extra IDs')
    source = Path(card['source_path']).read_bytes()
    with locked(ledger):
        records = read_records(ledger)
        if pending(records): raise ValueError('recover pending research append first')
        parent = next((c for c in research_cards(records) if c['card_id']==card['card_id']),None)
        if parent is None: raise ValueError('addendum parent absent')
        verify_projection(parent,part6)
        for old in research_addenda(records):
            if old['card_id']==card['card_id'] and old['source_sha256']==sha(source) and old['body_sha256']==sha(card['body'].encode('utf-8')):
                verify_projection(old,part6)
                return dict(card_id=card['card_id'],duplicate=True)
        tx = uuid.uuid4().hex; stamp = datetime.now(timezone.utc).isoformat(); cid=card['card_id']
        text = f'\n<!-- BEGIN RESEARCH ADDENDUM {cid} {tx} -->\n### Dated addendum for {cid}\n\nLogged UTC: {stamp}. Original forecast unchanged.\n\n'+card['body'].rstrip()+f'\n<!-- END RESEARCH ADDENDUM {cid} {tx} -->\n'
        projection = text.replace('\r\n','\n').replace('\n','\r\n').encode('utf-8')
        storage = Path(store or ROOT/'research/issued_research').resolve(); storage.mkdir(parents=True,exist_ok=True)
        original=storage/f'{cid}-{tx}.addendum.original.txt'; frozen=storage/f'{cid}-{tx}.addendum.md'
        for path, raw in [(original,source),(frozen,projection)]:
            with path.open('xb') as handle: handle.write(raw);handle.flush();os.fsync(handle.fileno())
        before,_=custody(part6)
        payload=dict(card_id=cid,event_key=parent['event_key'],transaction_id=tx,logged_utc=stamp,
            projection_path=stored_path(frozen),projection_sha256=sha(projection),source_path=stored_path(original),source_sha256=sha(source),
            body_sha256=sha(card['body'].encode('utf-8')),part6_before_bytes=len(before),part6_before_sha256=sha(before),
            combined_log_path=part6.relative_to(ROOT).as_posix() if part6.is_relative_to(ROOT/'prediction logs') else str(part6.resolve()),
            performance_status='RESEARCH_ONLY_NOT_CERTIFIED')
        prep=_append_locked(ledger,ADDENDUM_PREPARED,payload)
        if fault=='prepared': raise RuntimeError('simulated interruption after addendum preparation')
        result=_finish(prep,ledger,part6);_sync_status(part6,reconciliation,ledger)
        return dict(card_id=cid,duplicate=False,record_sha256=result['record_sha256'])

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['commit','addendum','recover','verify','next-id','refresh-status'])
    parser.add_argument('card', type=Path, nargs='?')
    args = parser.parse_args()
    if args.command in {'commit','addendum'}:
        if not args.card: parser.error('commit/addendum needs card.json')
        operation = addendum if args.command=='addendum' else commit
        result = operation(json.loads(args.card.read_text(encoding='utf-8')))
    elif args.command == 'recover': result = recover()
    else:
        if args.command == 'refresh-status': _sync_status(active_log(ROOT),RECONCILIATION,CANONICAL_LEDGER)
        cards = research_cards(read_records(CANONICAL_LEDGER))
        result = {'cards':[c['card_id'] for c in cards], 'next_id':next_id()}
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__': main()
