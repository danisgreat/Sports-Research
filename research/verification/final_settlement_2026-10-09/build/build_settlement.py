"""Validate the final settlement table and compute top-two-rule diagnostics.

Run from the repository root:
    python -B research/verification/final_settlement_2026-10-09/build/build_settlement.py

Reads settlement_table.json, writes summary.json beside it. Pure function of the
table: no network, no ledger or log writes.
"""
from __future__ import annotations
import collections
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
TABLE = HERE / 'settlement_table.json'
SUMMARY = HERE / 'summary.json'
GRADES = {'W', 'L', 'P', 'V'}
EVIDENCE = {'A', 'B', 'C', 'E', 'OP', 'X'}


def family(contract: str) -> str:
    c = contract.lower()
    if 'corner' in c:
        return 'corners'
    if '1st half' in c or 'first half' in c:
        return 'first_half_goals'
    if 'outs' in c:
        return 'player_prop'
    if 'games' in c:
        return 'tennis_games'
    if re.search(r'team (total|goals)', c):
        return 'team_total'
    if 'both teams' in c:
        return 'btts'
    if re.search(r'\b(over|under)\b', c):
        return 'match_total'
    if re.search(r'[+-]\d', c) or '+0.5' in c or 'x2' in c or '1x' in c or 'or draw' in c:
        return 'side_cushion_or_handicap'
    if 'moneyline' in c or 'winner' in c or ' win' in c:
        return 'side_winner'
    return 'other'


def validate(records):
    ids = [r['id'] for r in records]
    assert len(ids) == len(set(ids)), 'duplicate record'
    for r in records:
        ranks = [row[0] for row in r['rows']]
        assert ranks == sorted(ranks) and len(ranks) == len(set(ranks)), r['id']
        for rank, contract, grade, evidence, basis in r['rows']:
            assert grade in GRADES and evidence in EVIDENCE and basis.strip(), (r['id'], rank)
            if evidence == 'X':
                assert grade == 'V', (r['id'], rank)


def card_outcome(r):
    """Top-two rule: only ranks 1 and 2 can count as wins."""
    top = {row[0]: row[2] for row in r['rows'] if row[0] in (1, 2)}
    live = [g for g in top.values() if g in {'W', 'L'}]
    wins = sum(g == 'W' for g in live)
    if r.get('no_forecast'):
        return 'NO_FORECAST', wins, len(live)
    if not live:
        return 'VOID', 0, 0
    if wins == len(live):
        return 'TOP2_ALL_WON', wins, len(live)
    if wins == 0:
        return 'TOP2_ALL_LOST', wins, len(live)
    return 'TOP2_SPLIT', wins, len(live)


def main():
    data = json.loads(TABLE.read_text(encoding='utf-8'))
    records = data['records']
    validate(records)
    out = {'records': len(records), 'per_record': {}, 'totals': {}, 'by_sport': {}, 'rank1_by_family': {},
           'top2_by_family': {}, 'evidence_counts': {}, 'rank1_failures': [], 'informational_ranks_3plus': {}}
    totals = collections.Counter()
    sport = collections.defaultdict(collections.Counter)
    fam1 = collections.defaultdict(collections.Counter)
    fam2 = collections.defaultdict(collections.Counter)
    evidence = collections.Counter()
    info = collections.Counter()
    for r in records:
        outcome, wins, live = card_outcome(r)
        rank = {row[0]: row for row in r['rows']}
        r1 = rank.get(1, [None, None, 'V'])[2]
        r2 = rank.get(2, [None, None, 'V'])[2]
        out['per_record'][r['id']] = {'card_outcome': outcome, 'counted_wins': wins, 'counted_live_rows': live,
                                      'rank1': r1, 'rank2': r2, 'winner_call': r['winner_call'][1]}
        for row in r['rows']:
            evidence[row[3]] += 1
            if row[0] >= 3:
                info[row[2]] += 1
        if r.get('no_forecast'):
            totals['no_forecast_cards'] += 1
            continue
        totals['cards'] += 1
        totals[outcome] += 1
        totals['counted_wins'] += wins
        totals['counted_live_rows'] += live
        totals['rank1_' + r1] += 1
        totals['rank2_' + r2] += 1
        wc = r['winner_call'][1]
        totals['winner_' + wc] += 1
        s = sport[r['sport']]
        s['cards'] += 1
        s['rank1_' + r1] += 1
        s['counted_wins'] += wins
        s['counted_live_rows'] += live
        for rk, store in ((1, fam1), (2, fam2)):
            if rk in rank and rank[rk][2] in {'W', 'L'}:
                store[family(rank[rk][1])][rank[rk][2]] += 1
        if r1 == 'L':
            out['rank1_failures'].append(r['id'])
    hit = sum(1 for v in out['per_record'].values() if v['card_outcome'] in {'TOP2_ALL_WON', 'TOP2_SPLIT'})
    totals['hit_at_2'] = hit
    out['totals'] = dict(totals)
    out['by_sport'] = {k: dict(v) for k, v in sorted(sport.items())}
    out['rank1_by_family'] = {k: dict(v) for k, v in sorted(fam1.items())}
    out['top2_by_family'] = {k: dict(v) for k, v in sorted(fam2.items())}
    out['evidence_counts'] = dict(evidence)
    out['informational_ranks_3plus'] = dict(info)
    SUMMARY.write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({k: out[k] for k in ('totals', 'by_sport', 'rank1_by_family', 'evidence_counts', 'rank1_failures')}, indent=1))


if __name__ == '__main__':
    main()
