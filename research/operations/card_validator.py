"""Rank-order and family-rule validation for cards (PRD-01, PRD-09, GOV-03), usable on new cards and as a historical replay.

New cards must rank by p_card (non-increasing), carry no q column beside p, draw every p from one declared distribution
object, and respect the family rules in runtime/config/selection_rules.json. `scan_markdown` replays the same table checks
over any retained log so historic q-ordered cards (P-519, P-521, P-522) are flagged without being edited.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
RULES_PATH = ROOT / 'runtime/config/selection_rules.json'
ID_RE = re.compile(r'P-\d{3,}')
P_HEADERS = {'p_card', 'p', 'distribution p', 'model p', 'p (distribution)', 'issued p'}
Q_HEADERS = {'q', 'rm-1 q', 'rm1 q', 'calibrated q', 'q (rm-1)', 'issued q'}
TOLERANCE = 1e-9


def rules(path: Path = RULES_PATH) -> dict:
    return json.loads(Path(path).read_text(encoding='utf-8'))


def _clean(cell: str) -> str:
    return cell.strip().strip('*').strip('`').strip()


def parse_number(cell: str) -> float | None:
    text = _clean(cell).replace('−', '-').replace(',', '')
    match = re.fullmatch(r'([+-]?\d*\.?\d+)\s*(%?)', text)
    if not match:
        return None
    value = float(match[1])
    return value / 100.0 if match[2] else value


def markdown_tables(text: str):
    """Yield (start_line_index, header_cells, rows) for each pipe table in `text`."""
    lines = text.replace('\r\n', '\n').split('\n')
    i = 0
    while i < len(lines) - 1:
        line = lines[i]
        if line.strip().startswith('|') and re.match(r'^\s*\|[\s:\-|]+\|\s*$', lines[i + 1]):
            header = [_clean(c) for c in line.strip().strip('|').split('|')]
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith('|'):
                rows.append([c.strip() for c in lines[j].strip().strip('|').split('|')])
                j += 1
            yield i, header, rows
            i = j
        else:
            i += 1


def _column(header: list[str], names: set[str]) -> int | None:
    for index, cell in enumerate(header):
        if cell.lower() in names:
            return index
    return None


def rank_table_checks(header: list[str], rows: list[list[str]]) -> list[dict]:
    """Findings for one table with a Rank column and a probability column; [] when the table is not a ranked probability table."""
    rank_at, p_at, q_at = _column(header, {'rank'}), _column(header, P_HEADERS), _column(header, Q_HEADERS)
    if rank_at is None or p_at is None:
        return []
    entries = []
    for row in rows:
        if len(row) <= max(rank_at, p_at):
            continue
        rank_text = _clean(row[rank_at])
        if not rank_text.isdigit():
            continue
        p = parse_number(row[p_at])
        q = parse_number(row[q_at]) if q_at is not None and len(row) > q_at else None
        entries.append((int(rank_text), p, q, row))
    entries.sort(key=lambda e: e[0])
    findings = []
    ps = [(r, p) for r, p, _, _ in entries if p is not None]
    inversions = [(a, b) for a, b in zip(ps, ps[1:]) if b[1] > a[1] + TOLERANCE]
    if inversions:
        findings.append({'kind': 'RANK_ORDER_INVERSION', 'detail': 'p is not non-increasing by rank: ' +
                         ', '.join(f'rank {a[0]} {a[1]:.3f} < rank {b[0]} {b[1]:.3f}' for a, b in inversions)})
        qs = [(r, q) for r, _, q, _ in entries if q is not None]
        if q_at is not None and len(qs) == len(entries) and all(b[1] <= a[1] + TOLERANCE for a, b in zip(qs, qs[1:])):
            findings.append({'kind': 'RANKED_BY_Q', 'detail': 'ranks follow q, which is never an event probability (Rule P4)'})
    if q_at is not None:
        findings.append({'kind': 'P_AND_Q_COLUMNS', 'detail': 'a p column and a q column share one ranked table; new cards print p_card only'})
    return findings


def check_tables(text: str) -> list[dict]:
    out = []
    for start, header, rows in markdown_tables(text):
        for finding in rank_table_checks(header, rows):
            out.append({**finding, 'line': start + 1})
    return out


def scan_markdown(path: Path) -> list[dict]:
    """Replay: every ranked table in a retained log with the P-ID it belongs to (heading context or the table's ID column)."""
    text = Path(path).read_text(encoding='utf-8')
    lines = text.replace('\r\n', '\n').split('\n')
    heading_at = []
    for i, line in enumerate(lines):
        found = ID_RE.search(line)
        if re.match(r'^#{1,6}\s', line) and found:
            heading_at.append((i, found[0]))
    results = []
    for start, header, rows in markdown_tables(text):
        id_col = next((n for n, h in enumerate(header) if h.lower() in {'card', 'id', 'p-id', 'canonical id'}), None)
        groups: dict[str, list[list[str]]] = {}
        if id_col is not None:
            for row in rows:
                match = ID_RE.search(row[id_col]) if len(row) > id_col else None
                if match:
                    groups.setdefault(match[0], []).append(row)
        else:
            current = None
            for i, pid_ in heading_at:
                if i < start:
                    current = pid_
            if current:
                groups[current] = rows
        for card_id, card_rows in groups.items():
            for finding in rank_table_checks(header, card_rows):
                results.append({'card': card_id, 'line': start + 1, **finding})
    return results


def replay(paths: list[Path], flag_kinds: set[str] | None = None) -> dict[str, list[dict]]:
    """card id -> findings, over several logs. `flag_kinds` restricts to the given finding kinds."""
    by_card: dict[str, list[dict]] = {}
    for path in paths:
        for finding in scan_markdown(path):
            if flag_kinds and finding['kind'] not in flag_kinds:
                continue
            by_card.setdefault(finding['card'], []).append({**finding, 'file': Path(path).name})
    return dict(sorted(by_card.items()))


# --------------------------------------------------------------------------- family rules (PRD-09)
def family_of(proposition: str, sport: str = '') -> str | None:
    """PRD-09 family of a proposition. Sport-specific families only apply to that sport."""
    text, sport = proposition.lower(), sport.lower()
    if re.search(r'corner', text):
        return 'corners'
    if re.search(r'(1st|first)[ -]half|\b1h\b', text) and re.search(r'over\s*0\.5|0\.5\s*over|at least one goal|1\+', text):
        return 'first_half_over_0_5'
    if 'tennis' in sport and re.search(r'\bgames?\b', text) and re.search(r'over|under|total|handicap|[+\-−]\s?\d', text):
        return 'tennis_games'
    if 'baseball' in sport and re.search(r'\+\s?1\.5\b', text):
        return 'baseball_plus_1_5'
    return None


def family_rule_findings(picks: list[dict], meta: dict[str, str], sport: str = '', rulebook: dict | None = None) -> list[str]:
    """Violations of the PRD-09 family rules. `picks` carry rank, proposition, p_card and optional status text."""
    book = (rulebook or rules())['family_rules']
    distribution = meta.get('Distribution object', '').lower()
    out = []
    for pick in picks:
        family = family_of(pick['proposition'], sport)
        if family is None:
            continue
        rule = book[family]
        label = f"rank {pick['rank']} ({family})"
        if 'rank1_p_min' in rule and pick['rank'] == 1 and (pick['p_card'] or 0) < rule['rank1_p_min']:
            out.append(f"{label}: not Rank 1 below p_card {rule['rank1_p_min']:.0%} ({rule['note']})")
        needed = rule.get('requires_distribution')
        if needed and needed not in distribution and needed not in (pick.get('status') or '').lower():
            out.append(f"{label}: {rule['note']}; the Distribution object does not name {needed!r}")
        if rule.get('requires_provider') and not re.search(r'provider\s*[:=]\s*\S+', meta.get('Settlement fields', ''), re.I):
            out.append(f"{label}: {rule['note']}; Settlement fields must name 'provider: <name>'")
    return out


def commit_gate(body: str, analysis_status: str = '') -> list[str]:
    """Problems that stop a new card being committed to the canonical ledger (log_card commit). Historic imports are exempt."""
    if analysis_status.upper().startswith('HISTORICAL'):
        return []
    problems = []
    for finding in check_tables(body):
        if finding['kind'] in {'RANK_ORDER_INVERSION', 'RANKED_BY_Q', 'P_AND_Q_COLUMNS'}:
            problems.append(f"line {finding['line']}: {finding['kind']}: {finding['detail']}")
    return problems


def main(argv: list[str] | None = None) -> int:
    import argparse
    parser = argparse.ArgumentParser(description='Replay the rank-order checks over retained logs (read-only).')
    parser.add_argument('paths', nargs='+', type=Path)
    args = parser.parse_args(argv)
    found = replay(args.paths)
    print(json.dumps({card: [f"{x['kind']}@{x['file']}:{x['line']}" for x in items] for card, items in found.items()}, indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())



# ----------------------------------------------------------------------- mini-log-3 card checks
REQUIRED_META_V3 = ('Distribution object', 'Regime flags', 'Retirement rule', 'Listed-pitcher rule', 'Abandonment rule',
                    'Settlement fields', 'Capture due', 'Evidence snapshots')
RULE_FIELDS = ('Retirement rule', 'Listed-pitcher rule', 'Abandonment rule')
ISO_OFFSET = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?(Z|[+-]\d{2}:\d{2})$')
SNAPSHOT_RE = re.compile(r'^sha256:([0-9a-f]{64})@(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2})?(?:Z|[+-]\d{2}:\d{2}))$')
REGIME_FLAGS = ('FINALS_COMPRESSION', 'EARLY_SEASON', 'CUP_ROTATION')
DECISION_HEADING = '### Decision block'
APPENDIX_HEADING = '### Appendix'
DECISION_BLOCK_HARD = 4096
DECISION_BLOCK_SOFT = 2560
CAPTURE_WINDOW_HOURS = 36
ADJUSTMENT_HEADER = ['Name', 'Target', 'Size', 'SD units', 'Prior basis']
PRIOR_BASES = {'fitted', 'archive_estimate', 'analyst_judgement'}


def _parse_iso(value: str):
    from datetime import datetime
    return datetime.fromisoformat(value.replace('Z', '+00:00'))


def distribution_id(meta: dict[str, str]) -> str | None:
    value = meta.get('Distribution object', '').strip()
    return value.split()[0].strip('`') if value else None


def decision_block(text: str) -> str | None:
    start = text.find(DECISION_HEADING)
    if start < 0:
        return None
    end = text.find(APPENDIX_HEADING, start)
    return text[start:end if end >= 0 else len(text)]


def adjustments_from(text: str) -> list[dict[str, Any]]:
    for _, header, rows in markdown_tables(text):
        if [h.lower() for h in header] == [h.lower() for h in ADJUSTMENT_HEADER]:
            out = []
            for row in rows:
                if len(row) == len(ADJUSTMENT_HEADER):
                    out.append({'name': _clean(row[0]), 'target': _clean(row[1]), 'size': parse_number(row[2]),
                                'sd_units': parse_number(row[3]), 'prior_basis': _clean(row[4]).lower()})
            return out
    return []


def check_v3_card(text: str, meta: dict[str, str], picks: list[dict[str, Any]], sport: str = '', scheduled_start: str = '') -> tuple[list[str], list[str]]:
    """Errors and warnings for the mini-log-3 additions (PRD-01/03/05/08/09, GOV-04, SRC-02/03)."""
    errors: list[str] = []
    warnings: list[str] = []
    book = rules()
    for key in REQUIRED_META_V3:
        if not meta.get(key):
            errors.append(f'missing metadata "- **{key}:**" (mini-log-3)')
    # one declared distribution; every p row says it came from there
    dist = distribution_id(meta)
    for pick in picks:
        status = (pick.get('status') or '').strip().strip('`')
        if dist and status != f'FROM_DISTRIBUTION:{dist}':
            errors.append(f'rank {pick["rank"]}: Probability status must read FROM_DISTRIBUTION:{dist} (one declared distribution object)')
        if 'TO_FILL' in (pick.get('evidence') or '') + (pick.get('failure_route') or '') + pick['proposition']:
            errors.append(f'rank {pick["rank"]}: a TO_FILL placeholder was left in the pick table')
    for finding in check_tables(text):
        if finding['kind'] in {'RANK_ORDER_INVERSION', 'RANKED_BY_Q', 'P_AND_Q_COLUMNS'}:
            errors.append(f"line {finding['line']}: {finding['kind']}: {finding['detail']}")
    # decision block (PRD-08)
    block = decision_block(text)
    if block is None:
        errors.append(f'missing "{DECISION_HEADING}" (the short decision page: distribution, picks, joint failure, gate, kill paths)')
    else:
        if APPENDIX_HEADING not in text:
            errors.append(f'missing "{APPENDIX_HEADING}" (full evidence goes below the decision block)')
        size = len(block.encode('utf-8'))
        if size > DECISION_BLOCK_HARD:
            errors.append(f'decision block is {size} bytes; the limit is {DECISION_BLOCK_HARD} (target {DECISION_BLOCK_SOFT}); move evidence to the appendix')
        elif size > DECISION_BLOCK_SOFT:
            warnings.append(f'decision block is {size} bytes; the target is {DECISION_BLOCK_SOFT}')
        if '| Rank | Role |' not in block:
            errors.append('the pick table must sit inside the decision block')
    # Rank-1 gate (PRD-03)
    gate = re.search(r'(?m)^\*\*Rank-1 gate:\*\*\s*(PASS|RANK1_UNSTABLE)\b.*$', text)
    if not gate:
        errors.append('missing "**Rank-1 gate:** PASS|RANK1_UNSTABLE — p_card x%; best non-complementary alternative y%; margin z points"')
    elif picks:
        percents = [float(x) / 100 for x in re.findall(r'(\d+(?:\.\d+)?)\s*%', gate[0])]
        g = book['rank1_gate']
        if len(percents) < 2:
            errors.append('Rank-1 gate line must state p_card and the best non-complementary alternative as percentages')
        else:
            if picks[0]['p_card'] is not None and abs(percents[0] - picks[0]['p_card']) > 5e-4:
                errors.append('Rank-1 gate p_card differs from the pick table')
            expect = 'PASS' if percents[0] >= g['p_min'] - 1e-9 and percents[0] - percents[1] >= g['margin_min'] - 1e-9 else 'RANK1_UNSTABLE'
            if gate[1] != expect:
                errors.append(f'Rank-1 gate states {gate[1]} but p_card {percents[0]:.1%} and margin {percents[0] - percents[1]:.1%} give {expect} '
                              f'(p_card >= {g["p_min"]:.0%} and margin >= {g["margin_min"]:.0%})')
    # adjustments (PRD-05)
    adjustments = adjustments_from(text)
    dependence = re.search(r'(?m)^\*\*Adjustment dependence:\*\*\s*(NONE|ADJUSTMENT_DEPENDENT)\b', text)
    if not dependence:
        errors.append('missing "**Adjustment dependence:** NONE|ADJUSTMENT_DEPENDENT"')
    elif not re.search(r'(?m)^\*\*Adjustments:\*\*\s*NONE\s*$', text) and not adjustments:
        errors.append('state "**Adjustments:** NONE" or give the adjustments table | Name | Target | Size | SD units | Prior basis |')
    for a in adjustments:
        if a['sd_units'] is None or a['size'] is None or a['prior_basis'] not in PRIOR_BASES:
            errors.append(f"adjustment {a['name']!r}: size, SD units and a prior basis ({sorted(PRIOR_BASES)}) are required")
    threshold = book['adjustment_threshold_sd']
    if dependence and any(abs(a['sd_units'] or 0) > threshold for a in adjustments):
        unadjusted = re.search(r'(?m)^\*\*Unadjusted top two:\*\*\s*(.+?)\s*$', text)
        if not unadjusted:
            errors.append(f'an adjustment above {threshold} SD needs "**Unadjusted top two:** <rank 1>; <rank 2>" so rank dependence can be checked')
        else:
            before = [x.strip().strip('*`') for x in unadjusted[1].split(';')]
            after = [p['proposition'] for p in picks[:2]]
            differs = before != after
            if differs and dependence[1] != 'ADJUSTMENT_DEPENDENT':
                errors.append('the unadjusted top two differs from the picks after an adjustment above 0.25 SD: label ADJUSTMENT_DEPENDENT')
            if not differs and dependence[1] == 'ADJUSTMENT_DEPENDENT':
                errors.append('labelled ADJUSTMENT_DEPENDENT but the unadjusted top two equals the picks')
    elif dependence and dependence[1] == 'ADJUSTMENT_DEPENDENT':
        errors.append('ADJUSTMENT_DEPENDENT requires an adjustment above 0.25 SD in the adjustments table')
    # contract definition capture (GOV-04), settlement fields (SRC-02), snapshots (SRC-03), regime flags (PRD-07)
    for key in RULE_FIELDS:
        value = meta.get(key, '')
        if value and not re.match(r'^(N/A|FRAMEWORK_DEFAULT:\s*\S.*|OPERATOR:\s*\S.*)$', value):
            errors.append(f'{key} must be N/A, "FRAMEWORK_DEFAULT: <rule>" or "OPERATOR: <name>: <rule>"')
    due = meta.get('Capture due', '')
    if due:
        if not ISO_OFFSET.match(due):
            errors.append('Capture due must be ISO 8601 with a UTC offset')
        elif scheduled_start and ISO_OFFSET.match(scheduled_start):
            hours = (_parse_iso(due) - _parse_iso(scheduled_start)).total_seconds() / 3600
            if hours <= 0:
                errors.append('Capture due must be after the scheduled start')
            elif hours > CAPTURE_WINDOW_HOURS:
                warnings.append(f'Capture due is {hours:.0f} h after the start; schedule capture within {CAPTURE_WINDOW_HOURS} h before routes rot')
    snapshots = meta.get('Evidence snapshots', '')
    if snapshots and snapshots != 'NONE':
        for item in [s.strip() for s in snapshots.split(';') if s.strip()]:
            if not SNAPSHOT_RE.match(item):
                errors.append(f'Evidence snapshots item {item!r} must read sha256:<64 hex>@<ISO time with offset>, items separated by ";"')
    elif snapshots == 'NONE':
        warnings.append('no pregame evidence snapshot retained; lineup/goalie/injury claims on this card cannot be audited')
    flags = meta.get('Regime flags', '')
    if flags and flags != 'NONE':
        for flag in [f.strip() for f in flags.split(',') if f.strip()]:
            if flag not in REGIME_FLAGS and not re.match(r'^RULE_CHANGE:\S+$', flag):
                errors.append(f'unknown regime flag {flag!r}; use {", ".join(REGIME_FLAGS)} or RULE_CHANGE:<name>')
    errors += family_rule_findings(picks, meta, sport, book)
    return errors, warnings
