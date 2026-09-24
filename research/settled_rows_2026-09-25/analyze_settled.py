"""Descriptive analysis of settled_rows.csv (2026-09-25(d)). LEARNING_ONLY; nothing here is fitted into forecasts (L-087).

Definitions:
- "p-rows" are graded W/L rows carrying an issued probability. Pushes and voids are excluded.
- A "decision" is a p-row with p >= 0.5: the preferred side. Rows below 0.5 are mostly exact
  complements of a preferred row, so decision-level metrics avoid double-counting forced pairs.
- Intervals are Wilson 95% for rates. The Brier comparison is against a constant 0.5 (0.25).
- Calibration slope/intercept: a logistic regression of the outcome on logit(p), by Newton-Raphson.
  A slope below 1 means stated probabilities are too extreme; above 1, too timid. It is
  descriptive only and is never applied.
"""
import csv
import json
import math
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, 'settled_rows.csv'), encoding='utf-8')))
for r in rows:
    r['y'] = 1 if r['result'] == 'W' else 0 if r['result'] == 'L' else None
    r['pf'] = float(r['p']) if r['p'] else None
    r['n'] = int(r['num']) if r['num'] else None
    r['rank'] = int(r['rank'])
graded = [r for r in rows if r['y'] is not None]
prow = [r for r in graded if r['pf'] is not None]
dec = [r for r in prow if r['pf'] >= 0.5]


def wilson(k, n):
    if n == 0:
        return (float('nan'),) * 3
    p = k / n
    z = 1.96
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return round(p, 3), round(c - h, 3), round(c + h, 3)


def brier(rs):
    return round(sum((r['pf'] - r['y']) ** 2 for r in rs) / len(rs), 4) if rs else None


def block(rs, label):
    n = len(rs)
    if not n:
        return {'label': label, 'n': 0}
    k = sum(r['y'] for r in rs)
    out = {'label': label, 'n': n, 'cards': len({r['card'] for r in rs}), 'wins': k, 'win_rate_ci': wilson(k, n)}
    ps = [r['pf'] for r in rs if r['pf'] is not None]
    if ps and len(ps) == n:
        out['mean_p'] = round(sum(ps) / n, 3)
        out['gap_(win-mean_p)'] = round(k / n - out['mean_p'], 3)
        out['brier'] = brier(rs)
    return out


def logistic_calibration(rs):
    xs = [math.log(r['pf'] / (1 - r['pf'])) for r in rs]
    ys = [r['y'] for r in rs]
    a, b = 0.0, 1.0
    for _ in range(50):
        g0 = g1 = h00 = h01 = h11 = 0.0
        for x, y in zip(xs, ys):
            p = 1 / (1 + math.exp(-(a + b * x)))
            g0 += y - p
            g1 += (y - p) * x
            w = p * (1 - p)
            h00 += w
            h01 += w * x
            h11 += w * x * x
        det = h00 * h11 - h01 * h01
        if abs(det) < 1e-12:
            break
        da = (h11 * g0 - h01 * g1) / det
        db = (-h01 * g0 + h00 * g1) / det
        a, b = a + da, b + db
        if abs(da) + abs(db) < 1e-10:
            break
    se_b = math.sqrt(h00 / det) if det > 0 else float('nan')
    return round(a, 3), round(b, 3), round(se_b, 3)


def best_shrink(rs):
    """Hindsight descriptive: the lambda in p' = 0.5 + lambda(p − 0.5) that minimises Brier. Never applied (L-087)."""
    best = None
    for k in range(0, 151):
        lam = k / 100
        b = sum((0.5 + lam * (r['pf'] - 0.5) - r['y']) ** 2 for r in rs) / len(rs)
        if best is None or b < best[1]:
            best = (lam, b)
    return round(best[0], 2), round(best[1], 4)


R = {}
R['overview'] = {
    'graded_rows': len(graded), 'cards': len({r['card'] for r in graded}),
    'p_rows': len(prow), 'p_cards': len({r['card'] for r in prow}), 'p_rows_brier': brier(prow),
    'decisions': len(dec), 'decision_brier': brier(dec), 'decision_win_rate': wilson(sum(r['y'] for r in dec), len(dec)),
    'decision_mean_p': round(sum(r['pf'] for r in dec) / len(dec), 3),
    'p_range': [min(r['n'] for r in prow if r['n']), max(r['n'] for r in prow if r['n'])],
}
# calibration bands (all p-rows and decisions)
bands = [(0, 0.4), (0.4, 0.5), (0.5, 0.55), (0.55, 0.6), (0.6, 0.65), (0.65, 0.7), (0.7, 0.8), (0.8, 1.01)]
R['calibration_all_p_rows'] = [block([r for r in prow if lo <= r['pf'] < hi], f'{lo:.2f}-{hi:.2f}') for lo, hi in bands]
R['logistic_calibration_all'] = dict(zip(('intercept', 'slope', 'se_slope'), logistic_calibration(prow)))
R['logistic_calibration_decisions'] = dict(zip(('intercept', 'slope', 'se_slope'), logistic_calibration(dec)))
R['hindsight_best_shrink_all'] = dict(zip(('lambda', 'brier'), best_shrink(prow)))
R['hindsight_best_shrink_decisions'] = dict(zip(('lambda', 'brier'), best_shrink(dec)))

# by family, sport, rank (decisions)
fam = defaultdict(list)
for r in dec:
    fam[r['family']].append(r)
R['decisions_by_family'] = [block(v, k) for k, v in sorted(fam.items(), key=lambda kv: -len(kv[1]))]
sp = defaultdict(list)
for r in dec:
    sp[r['sport']].append(r)
R['decisions_by_sport'] = [block(v, k) for k, v in sorted(sp.items(), key=lambda kv: -len(kv[1]))]
rk = defaultdict(list)
for r in dec:
    rk[r['rank']].append(r)
R['decisions_by_rank'] = [block(v, f'rank {k}') for k, v in sorted(rk.items())]

# totals direction (decisions, family total or team-total or phase)
tot = [r for r in dec if r['family'] in ('total', 'team-total', 'phase') and r['direction'] in ('Over', 'Under')]
R['totals_direction'] = [block([r for r in tot if r['direction'] == d], d) for d in ('Over', 'Under')]
for fam_name in ('total', 'phase', 'team-total'):
    R[f'direction_{fam_name}'] = [block([r for r in tot if r['family'] == fam_name and r['direction'] == d], d)
                                  for d in ('Over', 'Under')]
R['totals_direction_by_sport'] = []
for s in sorted({r['sport'] for r in tot}):
    for d in ('Over', 'Under'):
        b = block([r for r in tot if r['sport'] == s and r['direction'] == d], f'{s} {d}')
        if b['n'] >= 5:
            R['totals_direction_by_sport'].append(b)
# handicap sign (decisions)
hc = [r for r in dec if r['family'] == 'handicap' and r['direction'] in ('plus', 'minus')]
R['handicap_sign'] = [block([r for r in hc if r['direction'] == d], d) for d in ('plus', 'minus')]
R['handicap_sign_by_sport'] = [block([r for r in hc if r['sport'] == s and r['direction'] == d], f'{s} {d}')
                               for s in sorted({r['sport'] for r in hc}) for d in ('plus', 'minus')
                               if sum(1 for r in hc if r['sport'] == s and r['direction'] == d) >= 5]

# cohort trend (decisions)
cohorts = [(318, 344), (345, 371), (373, 423), (424, 451), (452, 481), (482, 509)]
R['trend_decisions'] = [block([r for r in dec if r['n'] and lo <= r['n'] <= hi], f'P-{lo}..{hi}') for lo, hi in cohorts]

# ordinal era and all graded: rank-slot win rates (all rows, including non-probability era)
R['rank_slot_all_graded'] = [block([r for r in graded if r['rank'] == k], f'rank {k}') for k in range(1, 6)]
R['rank_slot_ordinal_era'] = [block([r for r in graded if r['pf'] is None and r['rank'] == k], f'rank {k} (no p)') for k in range(1, 5)]
R['direction_all_graded'] = [block([r for r in graded if r['family'] in ('total', 'team-total', 'phase') and r['direction'] == d
                                    and r['rank'] <= 2], f'{d} rows ranked 1-2 (all eras)') for d in ('Over', 'Under')]

# top-two joint outcomes (cards with rank 1 and 2 graded)
bycard = defaultdict(dict)
for r in graded:
    bycard[r['card']][r['rank']] = r
both = [c for c in bycard.values() if 1 in c and 2 in c]
k_both_w = sum(1 for c in both if c[1]['y'] == 1 and c[2]['y'] == 1)
k_both_l = sum(1 for c in both if c[1]['y'] == 0 and c[2]['y'] == 0)
R['top_two'] = {'cards': len(both), 'both_win': k_both_w, 'both_lose': k_both_l, 'split': len(both) - k_both_w - k_both_l,
                'P(both lose)': wilson(k_both_l, len(both)),
                'P(R1 lose)*P(R2 lose) if independent': round((sum(1 for c in both if c[1]['y'] == 0) / len(both)) *
                                                              (sum(1 for c in both if c[2]['y'] == 0) / len(both)), 3)}
# phase vs full total at card level (decisions)
json.dump(R, open(os.path.join(HERE, 'analysis_results.json'), 'w', encoding='utf-8'), indent=1)
for k, v in R.items():
    print('==', k)
    if isinstance(v, list):
        for x in v:
            print('  ', json.dumps(x))
    else:
        print('  ', json.dumps(v))
