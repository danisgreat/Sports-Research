"""Rolling top-two scoreboard (SCV-2026.10.09-v4): EVL-01 and EVL-05.

  python -B -m research.operations.scoreboard publish      # regenerate research/scoreboard/SCOREBOARD.{json,md}
  python -B -m research.operations.scoreboard verify       # fail if the published scoreboard is stale (run in CI)

Generated only from retained settlement tables (research/verification/**/settlement_table.json), the canonical ledger
(event dates) and GAME_PREDICTION_RANK_LOG.csv (legacy literal history). Deterministic: no clock, no randomness, sorted keys, so
the same inputs always give the same bytes and `verify` is a byte comparison.

Cohorts (EVL-05), never mixed in the headline:
  COUNTED        cards whose Rank 1 passed the Rank-1 gate (mini-log-3 `PASS`; before the gate existed: Rank-1 p_card >= 0.60 or unstated)
  RANK1_UNSTABLE cards labelled RANK1_UNSTABLE (or, before the gate, Rank-1 p_card < 0.60), scored separately
  INFORMATIONAL  ranks 3 and 4 of every card: calibration only, never wins
Counted wins use Rule T2: only Rank 1 and Rank 2, PUSH and VOID leave the denominators.
"""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

from research.operations import cohort_review, top_two
from research.src.custody_text import custody_bytes

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / 'research/scoreboard'
SCHEMA = 'scoreboard-1'
LEGACY_CSV = ROOT / 'GAME_PREDICTION_RANK_LOG.csv'
LEDGER = ROOT / 'research/canonical_ledger.jsonl'
DATE_SUFFIX = re.compile(r':(\d{4}-\d{2}-\d{2})$')
UNDATED = 'UNDATED'


def sha256_file(path: Path, root: Path = ROOT) -> str:
    """SHA-256 over custody bytes: identical on LF and CRLF checkouts for the files whose custody form is CRLF (GOV-02)."""
    return hashlib.sha256(custody_bytes(Path(path), root)).hexdigest()


def ledger_dates(ledger: Path = LEDGER) -> dict[str, str]:
    """card id -> event date from the canonical ledger's event key (only keys that end in :YYYY-MM-DD)."""
    dates: dict[str, str] = {}
    if not Path(ledger).exists():
        return dates
    for line in Path(ledger).read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        if record.get('record_type') != 'RESEARCH_LOG_PREPARED':
            continue
        payload = record['payload']
        match = DATE_SUFFIX.search(payload.get('event_key') or '')
        if match:
            dates[payload['card_id']] = match[1]
    return dates


def gate_cohort(card: dict) -> str:
    """COUNTED or RANK1_UNSTABLE for one card, with the legacy 0.60 rule where the gate did not exist."""
    gate = card.get('rank1_gate')
    if gate in ('PASS', 'RANK1_UNSTABLE'):
        return 'COUNTED' if gate == 'PASS' else 'RANK1_UNSTABLE'
    rank1 = next((r for r in card['rows'] if r[0] == 1), None)
    if rank1 is not None and rank1[2] is not None and rank1[2] < top_two.UNSTABLE_P:
        return 'RANK1_UNSTABLE'
    return 'COUNTED'


def _month(card: dict, dates: dict[str, str]) -> str:
    key = DATE_SUFFIX.search(card.get('event_key') or '')
    day = key[1] if key else dates.get(card['id'])
    return day[:7] if day else UNDATED


def _round(value: Any, places: int = 6) -> Any:
    if isinstance(value, float):
        return round(value, places)
    if isinstance(value, (list, tuple)):
        return [_round(v, places) for v in value]
    if isinstance(value, dict):
        return {k: _round(v, places) for k, v in value.items()}
    return value


def _summary(cards: list[dict]) -> dict:
    scoring = [{**c, 'rows': [(r[0], r[1], r[2], r[3]) for r in c['rows']]} for c in cards]
    s = top_two.summarise(scoring)
    t = s['totals']
    live1, live2 = t.get('rank1_W', 0) + t.get('rank1_L', 0), t.get('rank2_W', 0) + t.get('rank2_L', 0)
    return {'cards': t.get('cards', 0), 'no_forecast': t.get('no_forecast_cards', 0),
            'counted_wins': t.get('counted_wins', 0), 'live_rows': t.get('counted_live_rows', 0),
            'counted_win_rate': s['counted_win_rate'], 'counted_ci95': list(s['counted_win_rate_ci95']),
            'rank1': {'W': t.get('rank1_W', 0), 'L': t.get('rank1_L', 0), 'P': t.get('rank1_P', 0), 'V': t.get('rank1_V', 0),
                      'rate': s['rank1_win_rate'], 'ci95': list(s['rank1_ci95']), 'live': live1},
            'rank2': {'W': t.get('rank2_W', 0), 'L': t.get('rank2_L', 0), 'P': t.get('rank2_P', 0), 'V': t.get('rank2_V', 0),
                      'rate': s['rank2_win_rate'], 'ci95': list(s['rank2_ci95']), 'live': live2},
            'card_classes': {k: t.get(k, 0) for k in ('TOP2_ALL_WON', 'TOP2_SPLIT', 'TOP2_ALL_LOST', 'VOID')},
            'hit_at_2': t.get('hit_at_2', 0), 'mean_ndcg_at_2': s['mean_ndcg_at_2'], 'ndcg_slates': s['ndcg_slates'],
            'failure_classes': dict(sorted(s['rank1_failure_classes'].items())),
            'winner_calls': {k[len('winner_'):]: v for k, v in sorted(t.items()) if k.startswith('winner_')}}


def _slot(cards: list[dict], ranks: tuple[int, ...]) -> dict:
    wins = losses = 0
    pairs = []
    for card in cards:
        if card['no_forecast']:
            continue
        for rank, grade, p, _contract, _ev in card['rows']:
            if rank in ranks and grade in ('W', 'L'):
                wins += grade == 'W'
                losses += grade == 'L'
                if p is not None and 0.0 < p < 1.0:
                    pairs.append((p, 1.0 if grade == 'W' else 0.0))
    n = wins + losses
    brier = sum((p - y) ** 2 for p, y in pairs) / len(pairs) if pairs else None
    mean_p = sum(p for p, _ in pairs) / len(pairs) if pairs else None
    base = sum(y for _, y in pairs) / len(pairs) if pairs else None
    return {'W': wins, 'L': losses, 'rate': wins / n if n else None, 'ci95': list(top_two.wilson(wins, n)), 'with_p': len(pairs),
            'mean_p': mean_p, 'observed_rate_of_those': base, 'brier': brier}


def _group(cards: list[dict], key) -> dict:
    groups: dict[str, list[dict]] = collections.defaultdict(list)
    for card in cards:
        groups[key(card)].append(card)
    return {k: _summary(v) for k, v in sorted(groups.items())}


def _rank1_family(cards: list[dict]) -> dict:
    out: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    for card in cards:
        rank1 = next((r for r in card['rows'] if r[0] == 1), None)
        if card['no_forecast'] or rank1 is None or rank1[1] not in ('W', 'L'):
            continue
        out[top_two.family(rank1[3])][rank1[1]] += 1
    return {k: {'W': v['W'], 'L': v['L'], 'ci95': list(top_two.wilson(v['W'], v['W'] + v['L']))} for k, v in sorted(out.items())}


def legacy_history(path: Path = LEGACY_CSV) -> dict:
    """Literal grades from the rank log, by rank slot. Provisional and later-corrected rows are included: a diagnostic, not a certificate."""
    if not Path(path).exists():
        return {}
    by_rank: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    cards = set()
    with open(path, encoding='utf-8-sig', newline='') as handle:
        for row in csv.DictReader(handle):
            cards.add(row['card_id'])
            result = row['logged_result'].strip().upper()
            if result in ('W', 'L'):
                by_rank[row['rank'].strip() or 'unranked'][result] += 1
    slots = {}
    for rank in ('1', '2', '3', '4'):
        w, l = by_rank[rank]['W'], by_rank[rank]['L']
        slots[rank] = {'W': w, 'L': l, 'rate': w / (w + l) if w + l else None, 'ci95': list(top_two.wilson(w, w + l))}
    return {'cards': len(cards), 'slots': slots, 'basis': 'literal logged_result W/L only; mixed grading eras'}


def build(root: Path = ROOT) -> dict:
    cards, sources = cohort_review.load_tables(root)
    dates = ledger_dates(root / 'research/canonical_ledger.jsonl')
    ordered = [c for _, c in sorted(cards.items(), key=lambda kv: cohort_review.pid(kv[0]))]
    forecast = [c for c in ordered if not c['no_forecast']]
    cohorts = {name: [c for c in forecast if gate_cohort(c) == name] for name in ('COUNTED', 'RANK1_UNSTABLE')}
    result = {
        'schema': SCHEMA, 'scoring': 'SCV-2026.10.09-v4',
        'inputs': {'settlement_tables': [{'path': s['path'], 'schema': s['schema'], 'records': s['records'],
                                          'sha256': sha256_file(root / s['path'], root)} for s in sources],
                   'ledger_sha256': sha256_file(root / 'research/canonical_ledger.jsonl', root) if (root / 'research/canonical_ledger.jsonl').exists() else None,
                   'rank_log_sha256': sha256_file(root / 'GAME_PREDICTION_RANK_LOG.csv', root) if (root / 'GAME_PREDICTION_RANK_LOG.csv').exists() else None},
        'cards': len(ordered), 'forecast_cards': len(forecast), 'first_id': ordered[0]['id'] if ordered else None,
        'last_id': ordered[-1]['id'] if ordered else None,
        'headline_counted_cohort': _summary(cohorts['COUNTED']),
        'rank1_unstable_cohort': _summary(cohorts['RANK1_UNSTABLE']),
        'all_forecast_cards': _summary(forecast),
        'informational_ranks_3_4': _slot(forecast, (3, 4)),
        'slots': {'rank1': _slot(forecast, (1,)), 'rank2': _slot(forecast, (2,)), 'ranks_1_2': _slot(forecast, (1, 2))},
        'by_sport': _group(cohorts['COUNTED'], lambda c: c['sport']),
        'by_month': _group(cohorts['COUNTED'], lambda c: _month(c, dates)),
        'rank1_by_family': _rank1_family(cohorts['COUNTED']),
        'rank1_by_family_unstable': _rank1_family(cohorts['RANK1_UNSTABLE']),
        'evidence_grades': dict(sorted(collections.Counter(r[4] for c in forecast for r in c['rows']).items())),
        'evidence_grade_share_AB': None,
        'calibration': top_two.calibration([{**c, 'rows': [(r[0], r[1], r[2], r[3]) for r in c['rows']]} for c in forecast]),
        'legacy_history': legacy_history(root / 'GAME_PREDICTION_RANK_LOG.csv'),
    }
    grades = result['evidence_grades']
    total = sum(grades.values())
    result['evidence_grade_share_AB'] = (grades.get('A', 0) + grades.get('B', 0)) / total if total else None
    return _round(result)


def _pct(x: Any) -> str:
    return 'n/a' if x is None else f'{100 * x:.1f}%'


def _ci(pair: Any) -> str:
    return 'n/a' if not pair or pair[0] is None else f'{100 * pair[0]:.1f}–{100 * pair[1]:.1f}%'


def _row(label: str, s: dict) -> str:
    return (f"| {label} | {s['cards']} | {s['counted_wins']}/{s['live_rows']} | {_pct(s['counted_win_rate'])} | {_ci(s['counted_ci95'])} | "
            f"{s['rank1']['W']}–{s['rank1']['L']} | {s['rank2']['W']}–{s['rank2']['L']} | "
            f"{s['card_classes']['TOP2_ALL_WON']}/{s['card_classes']['TOP2_SPLIT']}/{s['card_classes']['TOP2_ALL_LOST']} |")


def render(data: dict) -> str:
    h = data['headline_counted_cohort']
    head = '| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |\n|---|---:|---|---:|---|---|---|---|'
    lines = ['# Top-two scoreboard (SCV-2026.10.09-v4)', '',
             f"Generated deterministically from {len(data['inputs']['settlement_tables'])} settlement tables; cards {data['first_id']}–{data['last_id']} "
             f"({data['forecast_cards']} with forecasts). Regenerate with `python -B -m research.operations.scoreboard publish`; CI fails if it is stale.", '',
             '## Counted cohort (Rank-1 gate passed)', '', head, _row('All counted', h), '',
             f"Rule T2: only Ranks 1–2 count; PUSH/VOID leave the denominators. Hit@2 {h['hit_at_2']} of {h['cards']}. "
             f"Mean NDCG@2 {h['mean_ndcg_at_2'] if h['mean_ndcg_at_2'] is not None else 'n/a'} over {h['ndcg_slates']} slates.", '',
             '## Cohorts shown separately (EVL-05)', '', head, _row('COUNTED (gate passed)', h),
             _row('RANK1_UNSTABLE', data['rank1_unstable_cohort']), _row('All forecast cards', data['all_forecast_cards']), '']
    info = data['informational_ranks_3_4']
    lines += ['Informational ranks 3–4 (calibration only; never wins): '
              f"{info['W']}–{info['L']} ({_pct(info['rate'])}, 95% CI {_ci(info['ci95'])}); mean stated p {_pct(info['mean_p'])}, Brier {info['brier'] if info['brier'] is not None else 'n/a'}.", '',
              '## Does Rank 2 carry information?', '', '| Slot | W–L | Rate | 95% CI |', '|---|---|---:|---|']
    for key, label in (('rank1', 'Rank 1'), ('rank2', 'Rank 2'), ('ranks_1_2', 'Ranks 1–2')):
        s = data['slots'][key]
        lines.append(f"| {label} | {s['W']}–{s['L']} | {_pct(s['rate'])} | {_ci(s['ci95'])} |")
    lines += [f"| Ranks 3–4 | {info['W']}–{info['L']} | {_pct(info['rate'])} | {_ci(info['ci95'])} |", '', '## By sport (counted cohort)', '', head]
    lines += [_row(k, v) for k, v in data['by_sport'].items()]
    lines += ['', '## By month (counted cohort; month from the event key, else UNDATED)', '', head]
    lines += [_row(k, v) for k, v in data['by_month'].items()]
    lines += ['', '## Rank 1 by proposition family', '', '| Family | Counted W–L | 95% CI | RANK1_UNSTABLE W–L |', '|---|---|---|---|']
    fam = data['rank1_by_family']
    unstable = data['rank1_by_family_unstable']
    for name in sorted(set(fam) | set(unstable)):
        a, b = fam.get(name, {'W': 0, 'L': 0, 'ci95': [None, None]}), unstable.get(name, {'W': 0, 'L': 0})
        lines.append(f"| {name} | {a['W']}–{a['L']} | {_ci(a['ci95'])} | {b['W']}–{b['L']} |")
    lines += ['', '## Rank-1 failure classes (counted cohort)', '', '| Class | Count |', '|---|---:|']
    lines += [f'| {k} | {v} |' for k, v in sorted(h['failure_classes'].items(), key=lambda kv: (-kv[1], kv[0]))]
    lines += ['', '## Evidence grades (all forecast cards)', '',
              ', '.join(f'{k} {v}' for k, v in data['evidence_grades'].items()) + f"; A/B share {_pct(data['evidence_grade_share_AB'])} (target 95%).", '']
    cal = data['calibration']
    if cal['n']:
        lines += ['## Calibration of stated p_card', '', f"n = {cal['n']}; Brier {cal['brier']}; climatology {cal['climatology_brier']}; skill {cal['brier_skill_score']}; "
                  f"reliability slope {cal['reliability_slope']}.", '']
    legacy = data['legacy_history']
    if legacy:
        lines += ['## Legacy literal history (diagnostic only)', '', f"{legacy['cards']} cards; {legacy['basis']}.", '', '| Rank | W–L | Rate | 95% CI |', '|---|---|---:|---|']
        lines += [f"| {r} | {s['W']}–{s['L']} | {_pct(s['rate'])} | {_ci(s['ci95'])} |" for r, s in legacy['slots'].items()]
        lines.append('')
    lines += ['Learning diagnostics, not certified prospective skill. Complementary rows are dependent, not independent trials.', '']
    return '\n'.join(lines)


def publish(root: Path = ROOT, out: Path | None = None) -> dict:
    out = Path(out or (root / 'research/scoreboard'))
    data = build(root)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'SCOREBOARD.json').write_text(json.dumps(data, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    (out / 'SCOREBOARD.md').write_text(render(data), encoding='utf-8', newline='\n')
    return data


def verify(root: Path = ROOT, out: Path | None = None) -> list[str]:
    out = Path(out or (root / 'research/scoreboard'))
    data = build(root)
    problems = []
    for name, want in (('SCOREBOARD.json', json.dumps(data, indent=1, sort_keys=True, ensure_ascii=False) + '\n'), ('SCOREBOARD.md', render(data))):
        path = out / name
        if not path.exists():
            problems.append(f'{name} is missing; run `python -B -m research.operations.scoreboard publish`')
        elif path.read_bytes().replace(b'\r\n', b'\n') != want.encode('utf-8'):
            problems.append(f'{name} is stale; run `python -B -m research.operations.scoreboard publish` after the latest settlement')
    return problems


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', choices=['publish', 'verify'])
    args = parser.parse_args(argv)
    if args.command == 'publish':
        data = publish()
        h = data['headline_counted_cohort']
        print(json.dumps({'cards': data['cards'], 'counted': f"{h['counted_wins']}/{h['live_rows']}", 'out': str(OUT_DIR)}, indent=2))
        return 0
    problems = verify()
    print(json.dumps({'passed': not problems, 'problems': problems}, indent=2))
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
