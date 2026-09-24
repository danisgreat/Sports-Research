"""Supplementary descriptive checks on settled_rows.csv (2026-09-25(d)); LEARNING_ONLY, never fitted (L-087)."""
import csv
import json
import math
import os
import random
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, 'settled_rows.csv'), encoding='utf-8')))
for r in rows:
    r['y'] = 1 if r['result'] == 'W' else 0 if r['result'] == 'L' else None
    r['pf'] = float(r['p']) if r['p'] else None
    r['rank'] = int(r['rank'])
prow = [r for r in rows if r['y'] is not None and r['pf'] is not None]
dec = [r for r in prow if r['pf'] >= 0.5]
BASEBALL = ('baseball-MLB', 'baseball-NPB/KBO/CPBL', 'baseball-other')


def rate(rs):
    n = len(rs)
    if not n:
        return {'n': 0}
    k = sum(r['y'] for r in rs)
    mp = sum(r['pf'] for r in rs) / n
    return {'n': n, 'cards': len({r['card'] for r in rs}), 'wins': k, 'win_rate': round(k / n, 3),
            'mean_p': round(mp, 3), 'gap': round(k / n - mp, 3),
            'brier': round(sum((r['pf'] - r['y']) ** 2 for r in rs) / n, 4)}


def murphy(rs, bins=10):
    """Brier = reliability - resolution + uncertainty (binned by stated p)."""
    n = len(rs)
    obar = sum(r['y'] for r in rs) / n
    groups = defaultdict(list)
    for r in rs:
        groups[min(int(r['pf'] * bins), bins - 1)].append(r)
    rel = sum(len(g) * ((sum(x['pf'] for x in g) / len(g)) - (sum(x['y'] for x in g) / len(g))) ** 2 for g in groups.values()) / n
    res = sum(len(g) * ((sum(x['y'] for x in g) / len(g)) - obar) ** 2 for g in groups.values()) / n
    unc = obar * (1 - obar)
    return {'reliability': round(rel, 4), 'resolution': round(res, 4), 'uncertainty': round(unc, 4),
            'brier_binned': round(rel - res + unc, 4)}


def cluster_ci_gap(rs, boot=5000, seed=7):
    by = defaultdict(list)
    for r in rs:
        by[r['card']].append(r)
    cards = list(by)
    rng = random.Random(seed)
    vals = []
    for _ in range(boot):
        s = [x for c in (rng.choice(cards) for _ in cards) for x in by[c]]
        vals.append(sum(x['y'] for x in s) / len(s) - sum(x['pf'] for x in s) / len(s))
    vals.sort()
    return round(vals[int(0.025 * boot)], 3), round(vals[int(0.975 * boot) - 1], 3)


S = {}
plus = [r for r in dec if r['family'] == 'handicap' and r['direction'] == 'plus']
S['plus_handicap_baseball'] = rate([r for r in plus if r['sport'] in BASEBALL])
S['plus_handicap_non_baseball'] = rate([r for r in plus if r['sport'] not in BASEBALL])
S['plus_handicap_non_baseball_gap_ci95_card_cluster'] = cluster_ci_gap([r for r in plus if r['sport'] not in BASEBALL])
S['plus_handicap_non_baseball_by_sport'] = {s: rate([r for r in plus if r['sport'] == s])
                                           for s in sorted({r['sport'] for r in plus if r['sport'] not in BASEBALL})}
S['minus_handicap_all'] = rate([r for r in dec if r['family'] == 'handicap' and r['direction'] == 'minus'])
S['decisions_0.50-0.65'] = rate([r for r in dec if r['pf'] < 0.65])
S['decisions_0.50-0.65_gap_ci95'] = cluster_ci_gap([r for r in dec if r['pf'] < 0.65])
S['decisions_0.65+'] = rate([r for r in dec if r['pf'] >= 0.65])
S['decisions_0.65+_gap_ci95'] = cluster_ci_gap([r for r in dec if r['pf'] >= 0.65])
S['murphy_all_p_rows'] = murphy(prow)
S['murphy_decisions'] = murphy(dec)
# resolution by sport (all p-rows)
S['murphy_by_sport'] = {s: {**murphy([r for r in prow if r['sport'] == s]), 'n': sum(1 for r in prow if r['sport'] == s)}
                        for s in sorted({r['sport'] for r in prow}) if sum(1 for r in prow if r['sport'] == s) >= 30}
# phase v full-total inside the same card (decisions)
by_card = defaultdict(list)
for r in dec:
    by_card[r['card']].append(r)
pairs = [(c, [r for r in rs if r['family'] == 'phase'], [r for r in rs if r['family'] == 'total'])
         for c, rs in by_card.items()]
pairs = [(c, ph, ft) for c, ph, ft in pairs if ph and ft]
S['same_card_phase_v_full'] = {'cards': len(pairs), 'phase': rate([x for _, ph, _ in pairs for x in ph]),
                               'full': rate([x for _, _, ft in pairs for x in ft])}
# sports with no demonstrated skill (decision Brier >= 0.25, n >= 10)
sp = defaultdict(list)
for r in dec:
    sp[r['sport']].append(r)
S['sports_decision_brier_ge_0.25'] = {k: rate(v) for k, v in sp.items() if len(v) >= 10 and rate(v)['brier'] >= 0.25}
# rank-1 decisions by family
r1 = [r for r in dec if r['rank'] == 1]
fam = defaultdict(list)
for r in r1:
    fam[r['family']].append(r)
S['rank1_by_family'] = {k: rate(v) for k, v in sorted(fam.items(), key=lambda kv: -len(kv[1]))}
json.dump(S, open(os.path.join(HERE, 'supplement_results.json'), 'w', encoding='utf-8'), indent=1)
for k, v in S.items():
    print('==', k)
    print('  ', json.dumps(v))
