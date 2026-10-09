"""Roll the active Combined Prediction Log from Part N to Part N+1 without consuming an ID.

Prompt 5 workflow.
  python -B -m research.operations.rollover plan
  python -B -m research.operations.rollover apply --main-head <40-hex SHA>

`apply`:
1. refuses while a canonical transaction is pending, if Part N+1 exists, or if checks fail;
2. appends a dated closure block to Part N (prior bytes unchanged; Part N's header custody intact);
3. writes the Part N+1 header and registers it in research/current_combined_log.json while
   keeping every earlier per-part header receipt (Part 6 legacy custody is untouched);
4. adds a `-text` .gitattributes entry so Part N+1 bytes are identical on every platform;
5. proves: next ID unchanged, ledger bytes unchanged, every projection still verifies,
   legacy and active custody pass; then refreshes GAME_LOG_STATUS_CURRENT.md;
6. writes research/verification/rollover_<date>_part<N>_to_<N+1>/rollover_receipt.json.

A new versioned control manifest is still required afterwards (Part N leaves the freeze
exclusion and becomes controlled history); see research/prompts/5_START_THE_NEXT_COMBINED_LOG.md.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

from research.operations import log_card
from research.src.combined_log import active_log, configuration, custody
from research.src.issue import CANONICAL_LEDGER, RECONCILIATION, _custody
from research.src.ledger import locked, read_records

HEADER_END = '<!-- END ACTIVE COMBINED LOG HEADER -->'


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def crlf(text: str) -> bytes:
    return text.replace('\r\n', '\n').replace('\n', '\r\n').encode('utf-8')


def _atomic_write(path: Path, raw: bytes):
    temporary = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    with temporary.open('xb') as handle:
        handle.write(raw); handle.flush(); os.fsync(handle.fileno())
    os.replace(temporary, path)


def _method(root: Path):
    path = root / 'METHOD.md'
    text = path.read_text(encoding='utf-8-sig') if path.exists() else ''
    find = lambda pattern: (re.search(pattern, text) or [None, 'NOT_RECORDED'])[1]
    return {'method': find(r'Method \*\*([^*]+)\*\*'), 'control': find(r'Control revision \*\*([^*]+)\*\*'),
            'scoring': find(r'Scoring \*\*([^*]+)\*\*'), 'freeze': find(r'Active freeze:\s*\[([^\]]+)\]')}


def part_number(relative: str) -> int:
    match = re.fullmatch(r'prediction logs/PREDICTION_LOG_COMBINED_(\d+)\.md', relative)
    if not match:
        raise ValueError(f'unexpected combined-log path {relative}')
    return int(match[1])


def plan(root: Path | None = None, reconciliation=RECONCILIATION, ledger=CANONICAL_LEDGER):
    root = Path(root or log_card.ROOT)
    config = configuration(root)
    if config is None:
        raise ValueError('research/current_combined_log.json is required (Part 6 legacy mode cannot roll over here)')
    old_rel = config['active_log']
    n = part_number(old_rel)
    new_rel = f'prediction logs/PREDICTION_LOG_COMBINED_{n + 1}.md'
    records = read_records(ledger)
    cards = log_card.research_cards(records)
    contained = [c['card_id'] for c in cards if c.get('combined_log_path') == old_rel]
    return {'root': str(root), 'active_log': old_rel, 'new_log': new_rel, 'part': n, 'new_part': n + 1,
            'new_log_exists': (root / new_rel).exists(), 'pending': bool(log_card.pending(records)),
            'next_id': log_card.next_id(root / old_rel, reconciliation, ledger),
            'highest_committed': cards[-1]['card_id'] if cards else 'NONE',
            'first_in_active': contained[0] if contained else 'NONE', 'last_in_active': contained[-1] if contained else 'NONE',
            'cards_in_active': len(contained), 'ledger_sha256': sha(Path(ledger).read_bytes()) if Path(ledger).exists() else None,
            'config': config, **_method(root)}


def render_header(p: dict, main_head: str, opened_local: str, opened_utc: str, carryover: str) -> str:
    n, m = p['part'], p['new_part']
    rows = []
    for k in range(1, m):
        name = 'PREDICTION_LOG_COMBINED.md' if k == 1 else f'PREDICTION_LOG_COMBINED_{k}.md'
        scope = 'Immutable earlier combined history; original scopes retained'
        if k == 6:
            scope = 'P-518–P-522 reserved custody (legacy original-source block); P-523–P-549 research; dated addenda'
        if k == n:
            scope = f"Closed {opened_utc[:10]}: research cards {p['first_in_active']}–{p['last_in_active']} ({p['cards_in_active']}); dated addenda and settlements"
        rows.append(f'| {k} | [Combined log {k}]({name}) | {scope} |')
    return '\n'.join([
        f'# Combined Prediction Log {m}', '',
        '**Status: ACTIVE FOR NEW CANONICAL RESEARCH.** SPORTS_ONLY / MARKET_BLIND.', '',
        f'Opened: {opened_local}; UTC {opened_utc}.',
        f'Repository main at rollover: `{main_head}`.',
        f"Method: **{p['method']}**. Control: **{p['control']}**. Scoring: **{p['scoring']}**.",
        f"Selected freeze at opening: [{p['freeze']}](../{p['freeze']}) (a new freeze is issued after this rollover).",
        f"Previous active log: [Part {n}](PREDICTION_LOG_COMBINED_{n}.md); research cards {p['first_in_active']}–{p['last_in_active']}. "
        'P-518–P-522 remain reserved and the Part-6 original-source block remains immutable.',
        f"**Highest committed canonical ID: {p['highest_committed']}. Next available canonical ID: {p['next_id']}.** "
        'Creating this file consumes no ID. The first real committed new event receives the allocator\'s next ID; this header is not a forecast.',
        f'Unresolved carryover: {carryover}.',
        'Research IDs identify retained work independently of calibration and performance certification. A verified sporting result is not operator certification or pregame performance eligibility.',
        '', '## Continuity', '', '| Part | History | Scope |', '|---|---|---|', *rows, '',
        '## Canonical logging', '',
        'Cards arrive through the local-mini lifecycle (research/prompts/): a settled mini is imported with '
        '`python -B -m research.operations.import_mini plan|apply`, which commits each card through `research.operations.log_card` '
        'under its retained local working ID and appends its settlement as a dated addendum. Direct cards use `log_card next-id`, `commit card.json`, then `verify`.',
        'Resolve the active destination from `research/current_combined_log.json`; preserve every registered per-part header receipt and the Part-6 '
        'special original-source hash. Recover any pending append before allocation or another rollover.',
        'A duplicate event/source/body returns its existing ID. Changed delivered content is a dated `addendum` under the original ID. Addenda and carryover references never consume an ID. '
        'Never rewrite prior probabilities, ranks, cutoffs, native identities or operator terms. Only Rank 1 and Rank 2 count as wins (Rule T2).',
        '', HEADER_END, ''])


def apply(main_head: str, root: Path | None = None, reconciliation=RECONCILIATION, ledger=CANONICAL_LEDGER,
          carryover: str = 'none open; see research/current_settlement_register.json and the latest import report',
          receipt_dir: Path | None = None):
    if not re.fullmatch(r'[0-9a-f]{40}', main_head or ''):
        raise ValueError('--main-head must be the 40-hex main HEAD SHA read before rollover')
    root = Path(root or log_card.ROOT)
    with locked(ledger):
        p = plan(root, reconciliation, ledger)
        if p['pending']:
            raise ValueError('recover the pending canonical transaction before rollover')
        if p['new_log_exists']:
            raise ValueError(f"{p['new_log']} already exists; never overwrite a combined log")
        old_path, new_path = root / p['active_log'], root / p['new_log']
        before_old = old_path.read_bytes()
        ledger_before = Path(ledger).read_bytes() if Path(ledger).exists() else b''
        custody(old_path)
        now = datetime.now(timezone.utc)
        opened_utc = now.isoformat()
        opened_local = now.astimezone().isoformat()
        closure = crlf('\n'.join([
            '', f'<!-- BEGIN ROLLOVER CLOSURE PART {p["part"]} -->', f'## Rollover closure — Combined Prediction Log {p["part"]}', '',
            f'Closed for new canonical research at {opened_local} (UTC {opened_utc}). Repository main at rollover: `{main_head}`.',
            f"Research cards in this part: {p['first_in_active']}–{p['last_in_active']} ({p['cards_in_active']}). "
            f"Highest committed canonical ID: {p['highest_committed']}. Next available canonical ID: {p['next_id']} (unchanged by rollover).",
            f"New active log: [Part {p['new_part']}](PREDICTION_LOG_COMBINED_{p['new_part']}.md). "
            f"Method {p['method']} / control {p['control']} / freeze {p['freeze']}.",
            f'Bytes before this closure: {len(before_old):,}; SHA-256 `{sha(before_old)}`. Earlier cards, addenda and settlements are unchanged.',
            f'<!-- END ROLLOVER CLOSURE PART {p["part"]} -->', '']))
        header = crlf(render_header(p, main_head, opened_local, opened_utc, carryover))
        with new_path.open('xb') as handle:
            handle.write(header); handle.flush(); os.fsync(handle.fileno())
        with old_path.open('ab') as handle:
            handle.write(closure); handle.flush(); os.fsync(handle.fileno())
        if not old_path.read_bytes().startswith(before_old):
            raise ValueError('closure append altered earlier bytes')
        config = dict(p['config'])
        headers = dict(config.get('log_headers') or {config['active_log']: {'header_bytes': config['header_bytes'],
                                                                             'header_sha256': config['header_sha256']}})
        headers[p['new_log']] = {'header_bytes': len(header), 'header_sha256': sha(header)}
        config.update(active_log=p['new_log'], header_bytes=len(header), header_sha256=sha(header), log_headers=headers,
                      opened_utc=opened_utc, next_id_at_open=p['next_id'], highest_committed_at_open=p['highest_committed'],
                      previous_active_log=p['active_log'])
        _atomic_write(root / 'research/current_combined_log.json', (json.dumps(config, indent=2) + '\n').encode('utf-8'))
        attributes = root / '.gitattributes'
        entry = f'"{p["new_log"]}" -text whitespace=cr-at-eol'
        current = attributes.read_text(encoding='utf-8') if attributes.exists() else ''
        if entry not in current:
            _atomic_write(attributes, (current.rstrip('\n') + '\n' + entry + '\n').encode('utf-8'))
    after_next = log_card.next_id(new_path, reconciliation, ledger)
    ledger_after = Path(ledger).read_bytes() if Path(ledger).exists() else b''
    checks = {'next_id_unchanged': after_next == p['next_id'], 'ledger_unchanged': ledger_after == ledger_before,
              'active_resolves_to_new': active_log(root).resolve() == new_path.resolve()}
    custody(new_path); custody(old_path)
    if (root / 'prediction logs/PREDICTION_LOG_COMBINED_6.md').exists():
        _custody(root / 'prediction logs/PREDICTION_LOG_COMBINED_6.md')
    records = read_records(ledger)
    for item in log_card.research_cards(records) + log_card.research_addenda(records):
        log_card.verify_projection(item, new_path)
    checks['projections_verified'] = True
    if not all(checks.values()):
        raise ValueError(f'rollover verification failed: {checks}')
    log_card._sync_status(new_path, reconciliation, ledger)
    status = root / 'GAME_LOG_STATUS_CURRENT.md'
    checks['status_names_new_log'] = status.exists() and p['new_log'] in status.read_text(encoding='utf-8')
    receipt = {'previous_active': p['active_log'], 'new_active': p['new_log'], 'main_head': main_head,
               'opened_utc': opened_utc, 'highest_committed': p['highest_committed'], 'next_before': p['next_id'],
               'next_after': after_next, 'id_consumed_by_rollover': after_next != p['next_id'],
               'ledger_sha256_before': sha(ledger_before), 'ledger_sha256_after': sha(ledger_after),
               'previous_log_prefix_bytes': len(before_old), 'previous_log_prefix_sha256': sha(before_old),
               'closure_bytes': len(closure), 'closure_sha256': sha(closure),
               'new_header_bytes': len(header), 'new_header_sha256': sha(header), 'checks': checks,
               'follow_up': 'Generate a new versioned control manifest, select it in METHOD.md, refresh status, update living docs.'}
    folder = Path(receipt_dir) if receipt_dir else root / f"research/verification/rollover_{opened_utc[:10]}_part{p['part']}_to_{p['new_part']}"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'rollover_receipt.json').write_text(json.dumps(receipt, indent=1) + '\n', encoding='utf-8')
    return receipt


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', choices=['plan', 'apply'])
    parser.add_argument('--main-head')
    parser.add_argument('--carryover', default='none open; see research/current_settlement_register.json and the latest import report')
    args = parser.parse_args(argv)
    try:
        if args.command == 'plan':
            result = plan()
            result.pop('config', None)
        else:
            result = apply(args.main_head, carryover=args.carryover)
    except ValueError as exc:
        print(json.dumps({'passed': False, 'error': str(exc)}, indent=2))
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
