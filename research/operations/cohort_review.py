"""Cohort retrospective over every retained settlement table (Prompt 6).

  python -B -m research.operations.cohort_review --out DIR [--from P-N] [--to P-M]

Discovers research/verification/**/settlement_table.json (schemas final-settlement-1 and
mini-settlement-2), keeps the latest settlement per canonical ID, and reports Rule T2 counted
metrics with Wilson intervals, rank-slot comparison (Rank 1, Rank 2, informational ranks 3-4),
sport and family breakdowns, Rank-1 failure classes, evidence grades and p_card calibration.
Read-only apart from the two report files it writes.
"""
from __future__ import annotations
import argparse
import collections
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from research.operations import top_two
from research.operations.mini_log import pid

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = {'final-settlement-1', 'mini-settlement-2'}


def _legacy_failure_classes(table_path: Path):
    """Failure classes recorded in the 2026-10-09 deep retrospections, if present beside that table."""
    module = table_path.parent / 'build' / 'rank1_retrospectives.py'
    if not module.exists():
        return {}
    spec = importlib.util.spec_from_file_location('_retro', module)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    out = {}
    for cid, text in loaded.R.items():
        match = re.search(r'\*\*Failure class\.\*\*\s*`?([A-Z0-9_]+)', text)
        out[cid] = match[1] if match else None
    return out


def load_tables(root: Path = ROOT):
    """Return normalised cards keyed by canonical ID (latest settlement wins) and the source list."""
    found = []
    for path in sorted((root / 'research/verification').glob('**/settlement_table.json')):
        try:
            table = json.loads(path.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            continue
        if table.get('schema') in SCHEMAS:
            found.append((table.get('created') or table.get('created_utc') or '', path, table))
    found.sort(key=lambda item: (item[0], str(item[1])))
    cards, sources = {}, []
    for created, path, table in found:
        classes = _legacy_failure_classes(path) if table['schema'] == 'final-settlement-1' else {}
        count = 0
        for record in table['records']:
            if table['schema'] == 'mini-settlement-2' and record.get('state') != 'SETTLED':
                continue
            winner = record.get('winner_call')
            winner = winner[1] if isinstance(winner, list) else (winner or 'NOT_AUDITED')
            rows = [(int(r[0]), top_two.grade_code(r[2]), r[5] if len(r) > 5 else None, r[1], r[3]) for r in record['rows']]
            cards[record['id']] = {'id': record['id'], 'sport': record.get('sport', 'UNKNOWN'), 'rows': rows,
                                   'no_forecast': bool(record.get('no_forecast')), 'winner_call': winner,
                                   'failure_class': record.get('failure_class') or classes.get(record['id']),
                                   'joint_failure': record.get('joint_failure'),
                                   'source': str(path.relative_to(root))}
            count += 1
        sources.append({'path': str(path.relative_to(root)), 'schema': table['schema'], 'records': count, 'created': created})
    return cards, sources


def review(cards: dict, first: str | None = None, last: str | None = None):
    chosen = [c for cid, c in sorted(cards.items(), key=lambda kv: pid(kv[0]))
              if (not first or pid(cid) >= pid(first)) and (not last or pid(cid) <= pid(last))]
    scoring = [{**c, 'rows': [(r[0], r[1], r[2], r[3]) for r in c['rows']]} for c in chosen]
    summary = top_two.summarise(scoring)
    slots = collections.Counter()
    evidence = collections.Counter()
    for card in chosen:
        if card['no_forecast']:
            continue
        for rank, grade, _p, _contract, ev in card['rows']:
            evidence[ev] += 1
            if grade in {'W', 'L'}:
                slot = 'rank1' if rank == 1 else 'rank2' if rank == 2 else 'ranks3plus'
                slots[f'{slot}_{grade}'] += 1
    comparison = {}
    for slot in ('rank1', 'rank2', 'ranks3plus'):
        w, l = slots[f'{slot}_W'], slots[f'{slot}_L']
        comparison[slot] = {'W': w, 'L': l, 'win_rate': w / (w + l) if w + l else None, 'ci95': top_two.wilson(w, w + l)}
    joint = [(c['joint_failure'], top_two.card_outcome([(r[0], r[1]) for r in c['rows']])[0])
             for c in chosen if not c['no_forecast'] and c.get('joint_failure') is not None
             and sum(r[0] in (1, 2) and r[1] in {'W', 'L'} for r in c['rows']) == 2]
    joint_check = {'cards': len(joint),
                   'mean_stated': sum(j for j, _ in joint) / len(joint) if joint else None,
                   'realised_all_lost': sum(o == 'TOP2_ALL_LOST' for _, o in joint) / len(joint) if joint else None,
                   'all_lost_ci95': top_two.wilson(sum(o == 'TOP2_ALL_LOST' for _, o in joint), len(joint))}
    stability = collections.Counter()
    for card in chosen:
        rank1 = next((r for r in card['rows'] if r[0] == 1), None)
        if card['no_forecast'] or rank1 is None or rank1[2] is None or rank1[1] not in {'W', 'L'}:
            continue
        group = 'unstable' if rank1[2] < top_two.UNSTABLE_P else 'stable'
        stability[f'{group}_{rank1[1]}'] += 1
    rank1_stability = {g: {'W': stability[f'{g}_W'], 'L': stability[f'{g}_L'],
                           'ci95': top_two.wilson(stability[f'{g}_W'], stability[f'{g}_W'] + stability[f'{g}_L'])}
                       for g in ('stable', 'unstable')}
    failures = [{'id': c['id'], 'sport': c['sport'], 'rank1': next((r[3] for r in c['rows'] if r[0] == 1), None),
                 'failure_class': top_two.failure_class(c['failure_class'])} for c in chosen
                if not c['no_forecast'] and any(r[0] == 1 and r[1] == 'L' for r in c['rows'])]
    return {'created_utc': datetime.now(timezone.utc).isoformat(), 'range': [first, last],
            'cards_considered': len(chosen), 'summary': summary, 'slot_comparison': comparison,
            'evidence_counts': dict(evidence), 'rank1_failures': failures,
            'joint_failure_check': joint_check, 'rank1_stability': rank1_stability,
            'calibration': top_two.calibration(scoring)}


def _pct(x):
    return 'n/a' if x is None else f'{100 * x:.1f}%'


def _ci(pair):
    return 'n/a' if pair[0] is None else f'{100 * pair[0]:.1f}–{100 * pair[1]:.1f}%'


def render(result: dict, sources: list) -> str:
    s, t = result['summary'], result['summary']['totals']
    lines = ['# Cohort retrospective (Rule T2 counted metrics)', '',
             f"Generated {result['created_utc']}. Range: {result['range'][0] or 'start'} – {result['range'][1] or 'end'}. "
             f"Cards considered: {result['cards_considered']} ({t.get('no_forecast_cards', 0)} no-forecast excluded).", '',
             '## Counted top-two result', '',
             f"- Counted wins: **{t.get('counted_wins', 0)} / {t.get('counted_live_rows', 0)}** ({_pct(s['counted_win_rate'])}; 95% CI {_ci(s['counted_win_rate_ci95'])}).",
             f"- Card classes: all won {t.get('TOP2_ALL_WON', 0)} · split {t.get('TOP2_SPLIT', 0)} · all lost {t.get('TOP2_ALL_LOST', 0)} · void {t.get('VOID', 0)}; Hit@2 {t.get('hit_at_2', 0)}.",
             f"- Mean full-slate NDCG@2: {s['mean_ndcg_at_2'] if s['mean_ndcg_at_2'] is not None else 'n/a'} over {s['ndcg_slates']} fully graded slates.",
             f"- Winner calls: {t.get('winner_CORRECT', 0)} correct / {t.get('winner_INCORRECT', 0)} incorrect.", '',
             '## Does each rank slot carry information?', '', '| Slot | W–L | Win rate | 95% CI |', '|---|---|---:|---|']
    for slot, label in (('rank1', 'Rank 1 (pick)'), ('rank2', 'Rank 2 (pick)'), ('ranks3plus', 'Ranks 3+ (informational)')):
        c = result['slot_comparison'][slot]
        lines.append(f"| {label} | {c['W']}–{c['L']} | {_pct(c['win_rate'])} | {_ci(c['ci95'])} |")
    lines += ['', 'Rank 2 should beat ranks 3+ with non-overlapping intervals once samples allow; otherwise Rank-2 selection is adding no information.', '']
    j = result['joint_failure_check']
    lines += ['## Joint top-two failure: stated vs realised', '',
              (f"{j['cards']} cards with two live picks and a stated joint failure: mean stated {_pct(j['mean_stated'])}; "
               f"realised TOP2_ALL_LOST {_pct(j['realised_all_lost'])} (95% CI {_ci(j['all_lost_ci95'])}).")
              if j['cards'] else 'No settled card in range records a stated joint failure (pre-mini-log-2 cards do not).', '',
              f'## Rank-1 stability gate (p_card < {top_two.UNSTABLE_P:.0%} = RANK1_UNSTABLE)', '',
              '| Group | W–L | Win rate 95% CI |', '|---|---|---|']
    for group, v in result['rank1_stability'].items():
        lines.append(f"| {group} | {v['W']}–{v['L']} | {_ci(v['ci95'])} |")
    lines += ['',
              '## By sport', '', '| Sport | Cards | Counted | Rank 1 W–L–V |', '|---|---:|---|---|']
    for sport, v in s['by_sport'].items():
        lines.append(f"| {sport} | {v.get('cards', 0)} | {v.get('counted_wins', 0)}/{v.get('counted_live_rows', 0)} | "
                     f"{v.get('rank1_W', 0)}–{v.get('rank1_L', 0)}–{v.get('rank1_V', 0)} |")
    lines += ['', '## Rank 1 by proposition family', '', '| Family | W | L |', '|---|---:|---:|']
    lines += [f"| {k} | {v.get('W', 0)} | {v.get('L', 0)} |" for k, v in s['rank1_by_family'].items()]
    lines += ['', '## Rank-1 failure classes', '', '| Class | Count |', '|---|---:|']
    lines += [f'| {k} | {v} |' for k, v in sorted(s['rank1_failure_classes'].items(), key=lambda kv: -kv[1])]
    lines += ['', '| ID | Sport | Rank-1 proposition | Class |', '|---|---|---|---|']
    lines += [f"| {f['id']} | {f['sport']} | {f['rank1']} | {f['failure_class'] or 'UNCLASSIFIED'} |" for f in result['rank1_failures']]
    cal = result['calibration']
    lines += ['', '## Calibration of stated p_card (all graded ranks with a probability)', '']
    if cal['n']:
        lines += [f"n = {cal['n']}; Brier {cal['brier']:.4f} vs climatology {cal['climatology_brier']:.4f} "
                  f"(skill {cal['brier_skill_score']:.3f}); log loss {cal['log_loss']:.4f}. "
                  + (f"Reliability line: win = {cal['reliability_intercept']:.3f} + {cal['reliability_slope']:.3f}·p "
                     "(perfect calibration 0 + 1·p; slope < 1 means over-confident spread)."
                     if cal['reliability_slope'] is not None else 'Reliability line: n/a (no spread in p).'), '',
                  '| Bin | n | Mean p | Win rate |', '|---|---:|---:|---:|']
        lines += [f"| {b['bin']} | {b['n']} | {_pct(b['mean_p'])} | {_pct(b['win_rate'])} |" for b in cal['bins']]
    else:
        lines.append('No settled rows carry a numeric p_card in this range.')
    lines += ['', '## Evidence grades', '', ', '.join(f'{k} {v}' for k, v in sorted(result['evidence_counts'].items())) or 'none', '',
              '## Sources', '', '| Settlement table | Schema | Records |', '|---|---|---:|']
    lines += [f"| `{src['path']}` | {src['schema']} | {src['records']} |" for src in sources]
    lines += ['', 'Learning diagnostics only: not certified prospective skill. Complementary rows are dependent, not independent trials.', '']
    return '\n'.join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--from', dest='first')
    parser.add_argument('--to', dest='last')
    args = parser.parse_args(argv)
    cards, sources = load_tables()
    result = review(cards, args.first, args.last)
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / 'COHORT_REVIEW.json').write_text(json.dumps({**result, 'sources': sources}, indent=1, ensure_ascii=False) + '\n',
                                                 encoding='utf-8')
    (args.out / 'COHORT_REVIEW.md').write_text(render(result, sources), encoding='utf-8')
    t = result['summary']['totals']
    print(json.dumps({'cards': result['cards_considered'], 'counted_wins': t.get('counted_wins', 0),
                      'counted_live_rows': t.get('counted_live_rows', 0), 'out': str(args.out)}, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
