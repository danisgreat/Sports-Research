"""Local mini running log (format mini-log-2): create, append, validate, settle-check and score.

The mini is a local working file written by an external chat agent (GitHub read-only) or by
this tool. Cards keep stable LOCAL working IDs until a separate canonical import. The format
is specified in CARD_AND_LOG_TEMPLATES.md; the six lifecycle prompts are in research/prompts/.

Commands (run from the repository root):
  python -B -m research.operations.mini_log new --dir DIR [--previous SETTLED_MINI] [--first-id P-N]
  python -B -m research.operations.mini_log append MINI CARD_BLOCK.md
  python -B -m research.operations.mini_log addendum MINI ADDENDUM_BLOCK.md
  python -B -m research.operations.mini_log next-id MINI [--repo-next P-N]
  python -B -m research.operations.mini_log verify MINI
  python -B -m research.operations.mini_log join FROZEN SETTLEMENT_SECTION.md --out SETTLED
  python -B -m research.operations.mini_log verify-settled FROZEN SETTLED [--out DIR]

Nothing here writes to the canonical ledger or a Combined Prediction Log.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from research.operations import top_two

ROOT = Path(__file__).resolve().parents[2]
FORMAT_TAG = '<!-- MINI-LOG-FORMAT: mini-log-2 -->'
SETTLEMENT_TAG = '<!-- SETTLEMENT-FORMAT: mini-settlement-2 -->'
CARDS_HEADING = '# NEW LOCAL EVENT CARDS'
FOOTER_BEGIN = '<!-- BEGIN FOOTER -->'
FOOTER_END = '<!-- END FOOTER -->'
ID_RE = r'P-\d{3,}'
NESTED_ID_HEADING = re.compile(r'(?m)^#{1,6}\s+(?:Prediction\s+|Game(?:\s+Card)?\s+)?P-\d+\b')
BLOCK_RE = re.compile(rb'<!-- BEGIN (CARD|CARRYOVER|ADDENDUM|SETTLEMENT) (P-\d{3,}) -->\r?\n(.*?)<!-- END \1 \2 -->', re.S)
META_RE = re.compile(r'(?m)^- \*\*([^*]+?):\*\*\s*(.+?)\s*$')
REQUIRED_META = ('Working ID', 'Event key', 'Native event ID', 'Sport', 'League', 'Tracking alias',
                 'Analysis status', 'Timing state', 'Research completed', 'Scheduled start', 'Endpoint')
TIMING_STATES = {'PREGAME', 'LATE_START_UNVERIFIED', 'LIVE_OBSERVED'}
PICK_HEADER = ['Rank', 'Role', 'Tag', 'Proposition', 'p_card', 'Probability status', 'Evidence', 'Failure route']
SETTLE_HEADER = ['Rank', 'Proposition', 'p_card', 'Grade', 'Counts toward wins', 'Evidence', 'Basis']
ROLES = {1: 'PICK', 2: 'PICK', 3: 'INFORMATIONAL', 4: 'INFORMATIONAL'}
TAGS = ('SUPPLIED', 'ANALYST_DERIVED')
DEGENERATE_P = 0.90
UNSTABLE_P = top_two.UNSTABLE_P
JOINT_FAILURE_WARN = 0.35
R_SECTIONS = [f'R{n}.' for n in range(1, 13)]
DEEP_PARTS = ('Claim', 'What happened', 'Distribution check', 'Knowability', 'Verdict',
              'Own-top-two counterfactual', 'Failure class', 'Proposed correction')
CARD_STATES = {'SETTLED', 'PENDING_EVENT'}


class MiniLogError(ValueError):
    """Structural error that blocks settlement or import."""


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def pid(value: str) -> int:
    if not re.fullmatch(ID_RE, value):
        raise MiniLogError(f'invalid P-ID {value!r}')
    return int(value[2:])


def strip_ticks(value: str) -> str:
    return value.strip().strip('`').strip()


def parse_percent(text: str):
    match = re.search(r'(\d+(?:\.\d+)?)\s*%', text)
    return float(match[1]) / 100.0 if match else None


def table_rows(text: str, header: list[str]):
    """Return the data rows of the first Markdown table whose header cells equal `header`."""
    lines = text.replace('\r\n', '\n').split('\n')
    for i, line in enumerate(lines):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if line.strip().startswith('|') and [c.strip('* ') for c in cells] == header:
            rows = []
            for row in lines[i + 2:]:
                if not row.strip().startswith('|'):
                    break
                rows.append([c.strip() for c in row.strip().strip('|').split('|')])
            return rows
    return None


def blocks(raw: bytes):
    """All marker-delimited blocks as dicts with kind, id, exact body bytes and byte span."""
    out = []
    for m in BLOCK_RE.finditer(raw):
        out.append({'kind': m[1].decode(), 'id': m[2].decode(), 'body': m[3], 'start': m.start(), 'end': m.end()})
    return out


def parse_card(block: dict):
    text = block['body'].decode('utf-8')
    errors, warnings = [], []
    meta = {k.strip(): strip_ticks(v) for k, v in META_RE.findall(text)}
    heading = re.match(r'## Card · (P-\d{3,}) · (.+?)\s*$', text.split('\n', 1)[0])
    if not heading:
        errors.append('first line must be "## Card · P-NNN · SPORT / LEAGUE · Event · YYYY-MM-DD"')
    elif heading[1] != block['id']:
        errors.append(f'heading ID {heading[1]} differs from marker {block["id"]}')
    if NESTED_ID_HEADING.search(text):
        errors.append('a heading starting with a P-ID would be read as a new canonical card')
    for key in REQUIRED_META:
        if not meta.get(key):
            errors.append(f'missing metadata "- **{key}:**"')
    working = meta.get('Working ID', '')
    if working and not working.startswith(block['id']):
        errors.append(f'Working ID {working!r} does not start with {block["id"]}')
    if working and 'PENDING_CANONICAL_IMPORT' not in working:
        errors.append('Working ID must read "P-NNN — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT"')
    key = meta.get('Event key', '')
    if key and not re.search(r':\d{4}-\d{2}-\d{2}$', key):
        errors.append('Event key must end with :YYYY-MM-DD')
    timing = meta.get('Timing state', '')
    if timing and timing not in TIMING_STATES:
        errors.append(f'Timing state must be one of {sorted(TIMING_STATES)}')
    picks = []
    rows = table_rows(text, PICK_HEADER)
    if rows is None:
        errors.append('missing pick table with header | ' + ' | '.join(PICK_HEADER) + ' |')
    else:
        if len(rows) != 4:
            errors.append(f'pick table must have exactly 4 candidates, found {len(rows)}')
        for n, row in enumerate(rows, 1):
            if len(row) != len(PICK_HEADER):
                errors.append(f'pick row {n} has {len(row)} cells, expected {len(PICK_HEADER)}')
                continue
            rank_text, role, tag, proposition, p_text = (c.strip('* ') for c in row[:5])
            try:
                rank = int(rank_text)
            except ValueError:
                errors.append(f'pick row {n} rank {rank_text!r} is not an integer')
                continue
            p = parse_percent(p_text)
            if rank != n:
                errors.append(f'pick row {n} has rank {rank}; ranks must be 1, 2, 3, 4 in order')
            if ROLES.get(rank) and not role.upper().startswith(ROLES[rank]):
                errors.append(f'rank {rank} role must be {ROLES[rank]}')
            if not tag.upper().startswith(TAGS):
                errors.append(f'rank {rank} tag must start with SUPPLIED or ANALYST_DERIVED')
            if p is None:
                errors.append(f'rank {rank} p_card must be a percentage (probabilities are mandatory)')
            elif not 0.0 < p <= DEGENERATE_P:
                errors.append(f'rank {rank} p_card {p:.1%} outside (0%, 90%]; degenerate propositions are excluded')
            if not proposition:
                errors.append(f'rank {rank} proposition is empty')
            picks.append({'rank': rank, 'role': role, 'tag': tag, 'proposition': proposition, 'p_card': p})
        ps = [x['p_card'] for x in picks if x['p_card'] is not None]
        if len(ps) == len(picks) and any(a < b - 1e-9 for a, b in zip(ps, ps[1:])):
            errors.append('ranks must be non-increasing in p_card (Rule P4: rank by p_card, never by q)')
        if picks and picks[0]['p_card'] is not None and picks[0]['p_card'] < UNSTABLE_P and 'RANK1_UNSTABLE' not in text:
            warnings.append(f'Rank 1 p_card {picks[0]["p_card"]:.1%} < {UNSTABLE_P:.0%}: label the card RANK1_UNSTABLE')
    winner = re.search(r'(?m)^\*\*Potential winner:\*\*\s*(.+?)\s*$', text)
    if not winner:
        errors.append('missing "**Potential winner:** <name> — <p>% (<endpoint>)" line')
    joint = re.search(r'(?m)^\*\*P\(Rank 1 and Rank 2 both lose\):\*\*\s*(.+?)\s*$', text)
    joint_p = parse_percent(joint[1]) if joint else None
    if joint_p is None:
        errors.append('missing "**P(Rank 1 and Rank 2 both lose):** <p>%" line')
    elif joint_p > JOINT_FAILURE_WARN:
        warnings.append(f'joint top-two failure {joint_p:.1%} > {JOINT_FAILURE_WARN:.0%}: consider a less correlated Rank 2')
    return {'id': block['id'], 'meta': meta, 'picks': picks, 'winner': winner[1] if winner else None,
            'joint_failure': joint_p, 'heading': heading[2] if heading else None, 'errors': errors, 'warnings': warnings}


def parse_carryover(block: dict):
    text = block['body'].decode('utf-8')
    errors = []
    if not re.match(r'### Carryover · (P-\d{3,}) · ', text):
        errors.append('carryover must start with "### Carryover · P-NNN · Event"')
    if NESTED_ID_HEADING.search(text):
        errors.append('a heading starting with a P-ID would be read as a new canonical card')
    meta = {k.strip(): strip_ticks(v) for k, v in META_RE.findall(text)}
    for key in ('Canonical ID', 'Event key', 'Carryover class', 'Remaining requirement'):
        if not meta.get(key):
            errors.append(f'carryover missing "- **{key}:**"')
    rows = table_rows(text, PICK_HEADER)
    picks = []
    if rows is None:
        errors.append('carryover must copy the original pick table verbatim')
    else:
        for row in rows:
            if len(row) == len(PICK_HEADER):
                try:
                    picks.append({'rank': int(row[0].strip('* ')), 'proposition': row[3].strip('* '),
                                  'p_card': parse_percent(row[4])})
                except ValueError:
                    errors.append('carryover pick table rank is not an integer')
    return {'id': block['id'], 'meta': meta, 'picks': picks, 'errors': errors, 'warnings': []}


def parse_addendum(block: dict):
    """A dated correction or late-news note under an existing ID; it never consumes an ID."""
    text = block['body'].decode('utf-8')
    errors = []
    head = re.match(r'### Addendum · (P-\d{3,}) · (.+?)\s*$', text.split('\n', 1)[0])
    if not head:
        errors.append('addendum must start with "### Addendum · P-NNN · <ISO 8601 time with offset>"')
    elif head[1] != block['id']:
        errors.append(f'addendum heading ID {head[1]} differs from marker {block["id"]}')
    elif not re.match(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?(Z|[+-]\d{2}:\d{2})$', strip_ticks(head[2])):
        errors.append('addendum time must be ISO 8601 with a UTC offset, e.g. 2026-10-10T18:05:00+11:00')
    if NESTED_ID_HEADING.search(text):
        errors.append('a heading starting with a P-ID would be read as a new canonical card')
    if not text.split('\n', 1)[1:] or not text.split('\n', 1)[1].strip():
        errors.append('addendum body is empty')
    if table_rows(text, PICK_HEADER) is not None:
        errors.append('an addendum must not contain a new pick table; the original card is what gets graded')
    return {'id': block['id'], 'errors': errors, 'warnings': [], 'start': block['start']}


def pick_table_text(text: str) -> str:
    """The exact pick-table lines (header, separator, rows) of a card."""
    lines = text.replace('\r\n', '\n').split('\n')
    for i, line in enumerate(lines):
        cells = [c.strip('* ') for c in line.strip().strip('|').split('|')]
        if line.strip().startswith('|') and cells == PICK_HEADER:
            out = [line, lines[i + 1]]
            for row in lines[i + 2:]:
                if not row.strip().startswith('|'):
                    break
                out.append(row)
            return '\n'.join(out)
    raise MiniLogError('card has no pick table to carry forward')


def footer_values(text: str):
    if FOOTER_BEGIN not in text or FOOTER_END not in text:
        return None
    segment = text.split(FOOTER_BEGIN, 1)[1].split(FOOTER_END, 1)[0]
    values = {}
    for line in segment.split('\n'):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) == 2 and cells[0] not in ('Field', '---'):
            values[cells[0]] = strip_ticks(cells[1])
    return values


def analyse(raw: bytes):
    """Parse an active (unsettled) mini and return a report with errors and warnings."""
    text = raw.decode('utf-8')
    errors, warnings = [], []
    if FORMAT_TAG not in text:
        errors.append(f'missing format tag {FORMAT_TAG}')
    if CARDS_HEADING not in text:
        errors.append(f'missing "{CARDS_HEADING}" section')
    found = blocks(raw)
    cards = [parse_card(b) for b in found if b['kind'] == 'CARD']
    carry = [parse_carryover(b) for b in found if b['kind'] == 'CARRYOVER']
    settle = [b for b in found if b['kind'] == 'SETTLEMENT']
    addenda = [parse_addendum(b) for b in found if b['kind'] == 'ADDENDUM']
    for item in cards + carry + addenda:
        errors += [f"{item['id']}: {e}" for e in item['errors']]
        warnings += [f"{item['id']}: {w}" for w in item['warnings']]
    ids = [c['id'] for c in cards]
    if len(ids) != len(set(ids)):
        errors.append('duplicate working P-ID among cards')
    numbers = [pid(i) for i in ids]
    if numbers != sorted(numbers):
        errors.append('cards must appear in increasing working-ID order')
    if any(b - a != 1 for a, b in zip(numbers, numbers[1:])):
        warnings.append('working IDs are not consecutive; record why IDs were skipped')
    keys = [c['meta'].get('Event key') for c in cards + carry]
    if len([k for k in keys if k]) != len({k for k in keys if k}):
        errors.append('the same Event key appears more than once (one event = one P-ID)')
    carry_ids = {c['id'] for c in carry}
    snapshot = re.search(r'(?m)^\| First working P-ID for this mini \| `?(P-\d{3,})`? \|', text)
    first = snapshot[1] if snapshot else None
    if carry_ids & set(ids):
        errors.append('a carryover ID is reused by a new card')
    if carry_ids and numbers and max(pid(i) for i in carry_ids) >= min(numbers):
        errors.append('carryover IDs must be lower than every new card ID')
    if cards and raw.find(CARDS_HEADING.encode()) > min(b['start'] for b in found if b['kind'] == 'CARD'):
        errors.append(f'cards must follow the "{CARDS_HEADING}" heading')
    card_start = {b['id']: b['start'] for b in found if b['kind'] == 'CARD'}
    for item in addenda:
        if item['start'] < raw.find(CARDS_HEADING.encode()):
            errors.append(f"{item['id']}: addenda belong after the \"{CARDS_HEADING}\" heading")
        if item['id'] in card_start:
            if item['start'] < card_start[item['id']]:
                errors.append(f"{item['id']}: addendum must follow the card it amends")
        elif item['id'] in carry_ids:
            pass
        elif first and pid(item['id']) >= pid(first):
            errors.append(f"{item['id']}: addendum for an ID that is not a card in this mini")
        else:
            warnings.append(f"{item['id']}: addendum under an earlier canonical ID; the importer checks it against the ledger")
    footer_at = raw.find(b'\n# RUNNING FOOTER')
    if footer_at >= 0 and any(b['start'] > footer_at for b in found if b['kind'] in ('CARD', 'ADDENDUM')):
        errors.append('cards and addenda must come before the running footer')
    footer = footer_values(text)
    if not snapshot:
        errors.append('authority snapshot missing "| First working P-ID for this mini | P-NNN |"')
    elif numbers and numbers[0] != pid(first):
        errors.append(f'first card {ids[0]} differs from the declared first working ID {first}')
    highest = ids[-1] if ids else None
    expected_next = f'P-{(numbers[-1] if numbers else pid(first) - 1) + 1}' if first else None
    if footer is None:
        errors.append('missing running footer block')
    else:
        want = {'Highest local working P-ID actually used': highest or 'NONE',
                'Next local working P-ID': expected_next,
                'New event cards': str(len(cards)), 'Active carryovers': str(len(carry))}
        for field, value in want.items():
            if footer.get(field) != value:
                errors.append(f'footer "{field}" is {footer.get(field)!r}, expected {value!r}')
        if footer.get('GitHub writes performed') not in ('NO', None):
            warnings.append('footer records GitHub writes; a local mini never writes to GitHub')
    return {'cards': cards, 'carryovers': carry, 'addenda': addenda, 'settlements': settle, 'first_id': first,
            'highest_id': highest, 'next_id': expected_next, 'footer': footer,
            'errors': errors, 'warnings': warnings, 'sha256': sha(raw), 'bytes': len(raw)}


def parse_settlement(block: dict, original_picks):
    text = block['body'].decode('utf-8')
    errors, warnings = [], []
    head = re.match(r'### Settlement · (P-\d{3,}) · (.+?)\s*$', text.split('\n', 1)[0])
    if not head or head[1] != block['id']:
        errors.append('settlement must start with "### Settlement · P-NNN · Event"')
    if NESTED_ID_HEADING.search(text):
        errors.append('a heading starting with a P-ID would be read as a new canonical card')
    state = re.search(r'(?m)^\*\*Card state:\*\*\s*`?([A-Z_]+)`?', text)
    state = state[1] if state else None
    if state not in CARD_STATES:
        errors.append(f'"**Card state:**" must be one of {sorted(CARD_STATES)}')
    record = {'id': block['id'], 'state': state, 'rows': [], 'winner_call': None, 'failure_class': None,
              'final': None, 'errors': errors, 'warnings': warnings}
    if state != 'SETTLED':
        return record
    final = re.search(r'(?m)^\*\*Final event:\*\*\s*(.+?)\s*$', text)
    record['final'] = final[1] if final else None
    if not final:
        errors.append('missing "**Final event:**" line')
    rows = table_rows(text, SETTLE_HEADER)
    if rows is None:
        errors.append('missing settlement table | ' + ' | '.join(SETTLE_HEADER) + ' |')
        rows = []
    by_rank = {p['rank']: p for p in original_picks}
    for row in rows:
        if len(row) != len(SETTLE_HEADER):
            errors.append(f'settlement row has {len(row)} cells, expected {len(SETTLE_HEADER)}')
            continue
        try:
            rank = int(row[0].strip('* '))
            grade = top_two.grade_code(row[3])
        except ValueError as exc:
            errors.append(f'settlement row {row[0]}: {exc}')
            continue
        evidence = row[5].strip('*` ').split()[0] if row[5].strip('*` ') else ''
        if evidence not in top_two.EVIDENCE:
            errors.append(f'rank {rank} evidence {evidence!r} must be one of {sorted(top_two.EVIDENCE)}')
        if evidence == 'X' and grade != 'V':
            errors.append(f'rank {rank}: evidence X (no data) must be graded VOID')
        if not row[6].strip():
            errors.append(f'rank {rank}: basis is empty')
        original = by_rank.get(rank)
        proposition = row[1].strip('* ')
        p = parse_percent(row[2])
        if original is None:
            errors.append(f'rank {rank} was not issued on the original card')
        else:
            if proposition != original['proposition']:
                errors.append(f'rank {rank} proposition differs from the original card')
            if original['p_card'] is not None and (p is None or abs(p - original['p_card']) > 1e-9):
                errors.append(f'rank {rank} p_card differs from the original card')
        counts = row[4].strip('* ').upper()
        expect = 'YES' if rank in (1, 2) and grade == 'W' else 'NO'
        if not counts.startswith(expect):
            errors.append(f'rank {rank}: "Counts toward wins" must start with {expect} (Rule T2)')
        record['rows'].append({'rank': rank, 'contract': proposition, 'grade': grade, 'evidence': evidence,
                               'basis': row[6], 'p_card': p})
    if sorted(r['rank'] for r in record['rows']) != sorted(by_rank):
        errors.append('every originally ranked row must be settled exactly once')
    outcome, wins, live = top_two.card_outcome([(r['rank'], r['grade']) for r in record['rows']])
    result = re.search(r'(?m)^\*\*Top-two result:\*\*\s*`?([A-Z0-9_]+)`?.*?(\d+) counted win\(s\) of (\d+)', text)
    if not result or (result[1], int(result[2]), int(result[3])) != (outcome, wins, live):
        errors.append(f'"**Top-two result:**" must read {outcome} — {wins} counted win(s) of {live} live top-two row(s)')
    winner = re.search(r'(?m)^\*\*Winner call:\*\*\s*(.+?):\s*`?(CORRECT|INCORRECT|NOT_ISSUED|UNRESOLVED)`?', text)
    if not winner:
        errors.append('missing "**Winner call:** <name>: CORRECT|INCORRECT|NOT_ISSUED|UNRESOLVED"')
    else:
        record['winner_call'] = winner[2]
    for label in R_SECTIONS:
        if not re.search(rf'(?m)^\*\*{re.escape(label)}', text):
            errors.append(f'missing retrospective section **{label} …**')
    rank1 = next((r for r in record['rows'] if r['rank'] == 1), None)
    if rank1 and rank1['grade'] == 'L':
        if '**Deep Rank-1 retrospection' not in text:
            errors.append('Rank 1 lost: the deep Rank-1 retrospection (Rule R1) is mandatory')
        for part in DEEP_PARTS:
            if not re.search(rf'\*\*{re.escape(part)}[.:]?\*\*', text):
                errors.append(f'deep Rank-1 retrospection missing **{part}.**')
        fc = re.search(r'\*\*Failure class[.:]?\*\*\s*`?([A-Z0-9_]+)`?', text)
        if not fc or fc[1] not in top_two.FAILURE_CLASSES:
            errors.append(f'Failure class must be one of {", ".join(top_two.FAILURE_CLASSES)}')
        else:
            record['failure_class'] = fc[1]
    return record


def analyse_settled(frozen: bytes, settled: bytes):
    """Validate a settled mini against its frozen original and build the settlement table."""
    errors, warnings = [], []
    if not settled.startswith(frozen):
        errors.append('settled mini must start with the exact bytes of the frozen original')
    base = analyse(frozen)
    errors += [f'frozen: {e}' for e in base['errors']]
    warnings += [f'frozen: {w}' for w in base['warnings']]
    tail = settled[len(frozen):] if settled.startswith(frozen) else settled
    if SETTLEMENT_TAG.encode() not in tail:
        errors.append(f'appended settlement section must carry {SETTLEMENT_TAG}')
    recorded = re.search(rb'(?m)^\| Frozen original SHA-256 \| `?([0-9A-Za-z_]+)`? \|', tail)
    if not recorded:
        errors.append('settlement header must record "| Frozen original SHA-256 | <sha256> |" (or NOT_COMPUTED)')
    elif recorded[1] == b'NOT_COMPUTED':
        warnings.append('frozen original SHA-256 NOT_COMPUTED; the importer records the true hash')
    elif recorded[1].decode().lower() != sha(frozen):
        errors.append('recorded frozen original SHA-256 does not match the frozen file')
    if any(b['kind'] != 'SETTLEMENT' for b in blocks(tail)):
        errors.append('the appended settlement section may contain only SETTLEMENT blocks')
    found = [b for b in blocks(tail) if b['kind'] == 'SETTLEMENT']
    by_id = {}
    for b in found:
        if b['id'] in by_id:
            errors.append(f"{b['id']}: settled more than once")
        by_id[b['id']] = b
    issued = {c['id']: c for c in base['cards']}
    carried = {c['id']: c for c in base['carryovers']}
    records = []
    for cid, item in list(issued.items()) + list(carried.items()):
        block = by_id.get(cid)
        if block is None:
            errors.append(f'{cid}: no settlement block (use Card state PENDING_EVENT to carry it forward)')
            continue
        rec = parse_settlement(block, item['picks'])
        errors += [f'{cid}: {e}' for e in rec['errors']]
        warnings += [f'{cid}: {w}' for w in rec['warnings']]
        meta = item['meta']
        records.append({'id': cid, 'origin': 'CARD' if cid in issued else 'CARRYOVER', 'state': rec['state'],
                        'event': item.get('heading') or meta.get('Event key'), 'event_key': meta.get('Event key'),
                        'sport': meta.get('Sport', 'UNKNOWN'), 'league': meta.get('League'),
                        'final': rec['final'], 'winner_call': rec['winner_call'], 'failure_class': rec['failure_class'],
                        'joint_failure': item.get('joint_failure'),
                        'rows': [[r['rank'], r['contract'], r['grade'], r['evidence'], r['basis'], r['p_card']]
                                 for r in rec['rows']]})
    for cid in by_id:
        if cid not in issued and cid not in carried:
            errors.append(f'{cid}: settlement for an ID that is neither a card nor a carryover in this mini')
    settled_records = [r for r in records if r['state'] == 'SETTLED']
    cards_for_summary = [{'id': r['id'], 'sport': r['sport'], 'winner_call': r['winner_call'] or 'NOT_AUDITED',
                          'failure_class': r['failure_class'],
                          'rows': [(row[0], row[2], row[5], row[1]) for row in r['rows']]} for r in settled_records]
    table = {'schema': 'mini-settlement-2', 'created_utc': datetime.now(timezone.utc).isoformat(),
             'frozen_sha256': sha(frozen), 'frozen_bytes': len(frozen),
             'settled_sha256': sha(settled), 'settled_bytes': len(settled),
             'first_id': base['first_id'], 'highest_id': base['highest_id'], 'next_local_id': base['next_id'],
             'records': records,
             'pending_event_ids': [r['id'] for r in records if r['state'] == 'PENDING_EVENT'],
             'summary': top_two.summarise(cards_for_summary), 'calibration': top_two.calibration(cards_for_summary)}
    return {'errors': errors, 'warnings': warnings, 'table': table, 'frozen': base}


# ---------------------------------------------------------------- creation and append

def _repo_snapshot(root: Path = ROOT):
    method = (root / 'METHOD.md').read_text(encoding='utf-8-sig')
    find = lambda pattern: (re.search(pattern, method) or [None, 'NOT_RECORDED'])[1]
    config = json.loads((root / 'research/current_combined_log.json').read_text(encoding='utf-8'))
    try:
        head = subprocess.run(['git', '-C', str(root), 'rev-parse', 'HEAD'], capture_output=True, text=True,
                              check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        head = 'NOT_RECORDED'
    from research.operations.log_card import next_id, research_cards
    from research.src.ledger import read_records
    from research.src.issue import CANONICAL_LEDGER
    cards = research_cards(read_records(CANONICAL_LEDGER))
    return {'head': head, 'method': find(r'Method \*\*([^*]+)\*\*'), 'control': find(r'Control revision \*\*([^*]+)\*\*'),
            'scoring': find(r'Scoring \*\*([^*]+)\*\*'), 'manifest': find(r'Active freeze:\s*\[([^\]]+)\]'),
            'active_log': config['active_log'], 'highest': cards[-1]['card_id'] if cards else 'NONE',
            'next': next_id()}


def render_new(snapshot: dict, first_id: str, highest_local: str, carryovers: list[str], opened: str):
    rows = [('Repository', 'https://github.com/danisgreat/Sports-Research'), ('Branch', 'main'),
            ('GitHub HEAD SHA', f"`{snapshot['head']}`"), ('Method', snapshot['method']),
            ('Control revision', snapshot['control']), ('Active manifest', snapshot['manifest']),
            ('Scoring version', snapshot['scoring']), ('Active Combined Log', f"`{snapshot['active_log']}`"),
            ('Highest committed repository P-ID', snapshot['highest']),
            ('Repository next-ID snapshot', snapshot['next']),
            ('Highest local working P-ID before creation', highest_local), ('First working P-ID for this mini', first_id),
            ('Mini opened', opened), ('Mode', 'LOCAL_MINI_STAGING')]
    out = [FORMAT_TAG, f'# Prediction Mini Running Log — {first_id} onward', '',
           '## A. Authority snapshot', '', '| Field | Value |', '|---|---|']
    out += [f'| {k} | {v} |' for k, v in rows]
    out += ['', 'SPORTS_ONLY / MARKET_BLIND · PERFORMANCE_ELIGIBILITY: NOT_CERTIFIED · CANONICAL_IMPORT_STATUS: PENDING', '',
            '## B. Local ID rules', '',
            '- Creating this mini consumes no P-ID. One unique sporting event = one working P-ID.',
            '- A working ID advances only after a complete new card is written and verified locally.',
            '- Addenda, corrections, duplicates and aliases keep the original ID and consume none.',
            '- Working IDs never change once issued; GitHub being behind does not invalidate them.',
            '- Canonical import (prompt 4) is separate; the importer retains these IDs or stops on a collision.', '',
            '## C. Active carryover', '']
    out += carryovers or ['None.', '']
    out += [CARDS_HEADING, '', footer(None, snapshot['next'], len(carryovers), 0, first_id)]
    return '\n'.join(out)


def footer(highest, repo_next, carry_count, card_count, first_id):
    nxt = f'P-{pid(highest) + 1}' if highest else first_id
    lines = ['# RUNNING FOOTER', '', FOOTER_BEGIN, '| Field | Value |', '|---|---|',
             f'| Highest local working P-ID actually used | {highest or "NONE"} |', f'| Next local working P-ID | {nxt} |',
             f'| Repository next-ID snapshot when mini opened | {repo_next} |', f'| Active carryovers | {carry_count} |',
             f'| New event cards | {card_count} |', '| Local mini status | ACTIVE |', '| Canonical import | PENDING |',
             '| GitHub writes performed | NO |', FOOTER_END, '']
    return '\n'.join(lines)


def carryover_from_pending(settled_table: dict, frozen_text: str):
    """Rebuild carryover blocks for PENDING_EVENT cards of a previous settled mini."""
    blocks_out = []
    raw = frozen_text.encode('utf-8')
    cards = {b['id']: parse_card(b) for b in blocks(raw) if b['kind'] == 'CARD'}
    carries = {b['id']: b for b in blocks(raw) if b['kind'] == 'CARRYOVER'}
    for cid in settled_table.get('pending_event_ids', []):
        if cid in carries:
            body = carries[cid]['body'].decode('utf-8')
            blocks_out.append(f'<!-- BEGIN CARRYOVER {cid} -->\n{body}<!-- END CARRYOVER {cid} -->\n')
            continue
        card = cards[cid]
        text = next(b for b in blocks(raw) if b['kind'] == 'CARD' and b['id'] == cid)['body'].decode('utf-8')
        table = pick_table_text(text)
        meta = card['meta']
        blocks_out.append('\n'.join([f'<!-- BEGIN CARRYOVER {cid} -->', f"### Carryover · {cid} · {card['heading']}", '',
                                     f"- **Canonical ID:** `{cid}` (verify against the ledger before settlement)",
                                     f"- **Event key:** `{meta.get('Event key')}`", f"- **Sport:** `{meta.get('Sport')}`",
                                     f"- **League:** `{meta.get('League')}`", '- **Carryover class:** `ACTIVE_SPORTING_CARRYOVER`',
                                     '- **Remaining requirement:** event not yet terminal (PENDING_EVENT at prior settlement)', '',
                                     table, '', 'DO NOT SETTLE UNTIL THE EVENT IS TERMINAL.', f'<!-- END CARRYOVER {cid} -->', '']))
    return blocks_out


def new(directory: Path, previous: Path | None = None, first_id: str | None = None, root: Path = ROOT):
    snapshot = _repo_snapshot(root)
    highest_local = 'NONE'
    carry = []
    if previous is not None:
        settled = previous.read_bytes()
        prior_dir = previous.parent
        frozen_candidates = sorted((prior_dir / 'ORIGINAL_MINI').glob('*.md'))
        if not frozen_candidates:
            raise MiniLogError('previous settled mini needs its ORIGINAL_MINI/ frozen copy beside it')
        frozen = frozen_candidates[0].read_bytes()
        result = analyse_settled(frozen, settled)
        if result['errors']:
            raise MiniLogError('previous settled mini fails validation:\n' + '\n'.join(result['errors']))
        highest_local = result['table']['highest_id'] or highest_local
        carry = carryover_from_pending(result['table'], frozen.decode('utf-8'))
    candidates = [pid(snapshot['next'])]
    if highest_local != 'NONE':
        candidates.append(pid(highest_local) + 1)
    chosen = f'P-{max(candidates)}'
    if first_id and pid(first_id) < pid(chosen):
        raise MiniLogError(f'--first-id {first_id} would reuse an ID; first unused is {chosen}')
    first = first_id or chosen
    opened = datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')
    text = render_new(snapshot, first, highest_local, carry, opened)
    stamp = datetime.now().strftime('%Y-%m-%d')
    folder = Path(directory) / f'Mini Prediction Log - {first} onward - {stamp}'
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f'PREDICTION_MINI_RUNNING_LOG_{first}_ONWARD.md'
    if path.exists():
        raise MiniLogError(f'{path} already exists; never overwrite a mini')
    path.write_text(text, encoding='utf-8')
    report = analyse(path.read_bytes())
    if report['errors']:
        raise MiniLogError('new mini failed validation:\n' + '\n'.join(report['errors']))
    return path, report


def append(mini: Path, card_path: Path):
    """Insert one complete card block before the footer and refresh the footer."""
    raw = mini.read_bytes()
    report = analyse(raw)
    if report['errors']:
        raise MiniLogError('mini fails validation before append:\n' + '\n'.join(report['errors']))
    block_raw = card_path.read_bytes()
    found = blocks(block_raw)
    if len(found) != 1 or found[0]['kind'] != 'CARD':
        raise MiniLogError('card file must contain exactly one <!-- BEGIN CARD P-NNN --> … <!-- END CARD P-NNN --> block')
    card = parse_card(found[0])
    if card['errors']:
        raise MiniLogError('card fails validation:\n' + '\n'.join(card['errors']))
    if card['id'] != report['next_id']:
        raise MiniLogError(f"card uses {card['id']} but the next local working ID is {report['next_id']}")
    keys = {c['meta'].get('Event key') for c in report['cards'] + report['carryovers']}
    if card['meta'].get('Event key') in keys:
        raise MiniLogError('event already present in this mini; use an addendum under its existing ID')
    text = raw.decode('utf-8')
    footer_start = text.index('# RUNNING FOOTER')
    block = block_raw.decode('utf-8').strip('\n') + '\n\n'
    snapshot = re.search(r'(?m)^\| Repository next-ID snapshot \| `?(P-\d{3,})`? \|', text)
    new_footer = footer(card['id'], snapshot[1] if snapshot else 'NOT_RECORDED', len(report['carryovers']),
                        len(report['cards']) + 1, report['first_id'])
    updated = text[:footer_start] + block + new_footer
    if not updated.startswith(text[:footer_start]):
        raise MiniLogError('append would alter earlier bytes')
    after = analyse(updated.encode('utf-8'))
    if after['errors']:
        raise MiniLogError('mini fails validation after append:\n' + '\n'.join(after['errors']))
    mini.write_bytes(updated.encode('utf-8'))
    return after


def add_addendum(mini: Path, addendum_path: Path):
    """Insert one addendum block before the footer; the footer and every earlier byte stay unchanged."""
    raw = mini.read_bytes()
    report = analyse(raw)
    if report['errors']:
        raise MiniLogError('mini fails validation before addendum:\n' + '\n'.join(report['errors']))
    block_raw = addendum_path.read_bytes()
    found = blocks(block_raw)
    if len(found) != 1 or found[0]['kind'] != 'ADDENDUM':
        raise MiniLogError('addendum file must contain exactly one <!-- BEGIN ADDENDUM P-NNN --> … <!-- END ADDENDUM P-NNN --> block')
    item = parse_addendum(found[0])
    if item['errors']:
        raise MiniLogError('addendum fails validation:\n' + '\n'.join(item['errors']))
    text = raw.decode('utf-8')
    footer_start = text.index('# RUNNING FOOTER')
    updated = text[:footer_start] + block_raw.decode('utf-8').strip('\n') + '\n\n' + text[footer_start:]
    after = analyse(updated.encode('utf-8'))
    if after['errors']:
        raise MiniLogError('mini fails validation after addendum:\n' + '\n'.join(after['errors']))
    mini.write_bytes(updated.encode('utf-8'))
    return after


def join(frozen_path: Path, section_path: Path, out_path: Path):
    """Build the settled mini byte-exactly: frozen original + appended settlement section.

    Use this when the settlement section was written separately. A recorded frozen SHA of
    NOT_COMPUTED is replaced by the true hash. The result is validated before it is written.
    """
    frozen, section = Path(frozen_path).read_bytes(), Path(section_path).read_bytes()
    if section.startswith(frozen):
        settled = section
    else:
        if FORMAT_TAG.encode() in section:
            raise MiniLogError('the section contains a mini header but does not start with the frozen bytes; '
                               'the frozen part was edited or re-saved')
        settled = frozen + (b'' if section.startswith((b'\n', b'\r\n')) else b'\n') + section
    tail = settled[len(frozen):]
    for pattern in (b'| Frozen original SHA-256 | `NOT_COMPUTED` |', b'| Frozen original SHA-256 | NOT_COMPUTED |'):
        tail = tail.replace(pattern, b'| Frozen original SHA-256 | `' + sha(frozen).encode() + b'` |', 1)
    settled = frozen + tail
    outcome = analyse_settled(frozen, settled)
    if outcome['errors']:
        raise MiniLogError('settled mini fails validation:\n' + '\n'.join(outcome['errors']))
    out_path = Path(out_path)
    if out_path.exists() and out_path.read_bytes() != settled:
        raise MiniLogError(f'{out_path} exists with different bytes; never overwrite a settled mini')
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(settled)
    return outcome


def local_next_id(mini_report: dict, repo_next: str | None):
    candidates = [pid(mini_report['next_id'])] if mini_report.get('next_id') else []
    if repo_next:
        candidates.append(pid(repo_next))
    return f'P-{max(candidates)}'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('new'); p.add_argument('--dir', type=Path, required=True)
    p.add_argument('--previous', type=Path); p.add_argument('--first-id')
    p = sub.add_parser('append'); p.add_argument('mini', type=Path); p.add_argument('card', type=Path)
    p = sub.add_parser('addendum'); p.add_argument('mini', type=Path); p.add_argument('block', type=Path)
    p = sub.add_parser('next-id'); p.add_argument('mini', type=Path); p.add_argument('--repo-next')
    p = sub.add_parser('verify'); p.add_argument('mini', type=Path)
    p = sub.add_parser('join'); p.add_argument('frozen', type=Path); p.add_argument('section', type=Path)
    p.add_argument('--out', type=Path, required=True)
    p = sub.add_parser('verify-settled'); p.add_argument('frozen', type=Path); p.add_argument('settled', type=Path)
    p.add_argument('--out', type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == 'new':
            path, report = new(args.dir, args.previous, args.first_id)
            result = {'path': str(path), 'first_id': report['first_id'], 'next_id': report['next_id'],
                      'carryovers': len(report['carryovers']), 'warnings': report['warnings']}
        elif args.command == 'append':
            report = append(args.mini, args.card)
            result = {'highest_id': report['highest_id'], 'next_id': report['next_id'], 'warnings': report['warnings']}
        elif args.command == 'addendum':
            report = add_addendum(args.mini, args.block)
            result = {'addenda': [a['id'] for a in report['addenda']], 'next_id': report['next_id'], 'warnings': report['warnings']}
        elif args.command == 'next-id':
            report = analyse(args.mini.read_bytes())
            result = {'local_next': report['next_id'], 'repo_next': args.repo_next,
                      'next_working_id': local_next_id(report, args.repo_next), 'errors': report['errors']}
        elif args.command == 'verify':
            report = analyse(args.mini.read_bytes())
            result = {'passed': not report['errors'], 'cards': [c['id'] for c in report['cards']],
                      'carryovers': [c['id'] for c in report['carryovers']], 'addenda': [a['id'] for a in report['addenda']],
                      'next_id': report['next_id'],
                      'sha256': report['sha256'], 'errors': report['errors'], 'warnings': report['warnings']}
        elif args.command == 'join':
            outcome = join(args.frozen, args.section, args.out)
            result = {'passed': True, 'settled': str(args.out), 'settled_sha256': outcome['table']['settled_sha256'],
                      'frozen_sha256': outcome['table']['frozen_sha256'], 'warnings': outcome['warnings'],
                      'pending_event_ids': outcome['table']['pending_event_ids']}
        else:
            outcome = analyse_settled(args.frozen.read_bytes(), args.settled.read_bytes())
            result = {'passed': not outcome['errors'], 'errors': outcome['errors'], 'warnings': outcome['warnings'],
                      'summary': outcome['table']['summary'], 'pending_event_ids': outcome['table']['pending_event_ids']}
            if args.out and not outcome['errors']:
                args.out.mkdir(parents=True, exist_ok=True)
                (args.out / 'settlement_table.json').write_text(json.dumps(outcome['table'], indent=1, ensure_ascii=False) + '\n',
                                                                 encoding='utf-8')
                result['settlement_table'] = str(args.out / 'settlement_table.json')
    except MiniLogError as exc:
        result = {'passed': False, 'errors': str(exc).split('\n')}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get('passed', True) and not result.get('errors') else 1


if __name__ == '__main__':
    sys.exit(main())
