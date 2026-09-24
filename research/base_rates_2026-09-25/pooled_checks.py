"""Pooled early-season total differences (within-season, 3 seasons) and the P-495..P-509 width z-scores."""
import math
import statistics as st
from collections import Counter

import analyze_leagues as al
import analyze_more  # noqa: F401  (registers the prior-season SPEC entries)


def early_diffs(label, first_n=3):
    games, _, _ = al.load(label)
    reg = al.regular(games)
    played = Counter()
    early, rest = [], []
    for g in sorted(reg, key=lambda x: x['date']):
        t = g['hs'] + g['as']
        (early if played[g['home']] < first_n and played[g['away']] < first_n else rest).append(t)
        played[g['home']] += 1
        played[g['away']] += 1
    d = st.fmean(early) - st.fmean(rest)
    var = st.variance(early) / len(early) + st.variance(rest) / len(rest)
    return d, var, len(early)


for league in ('NBL', 'WNBA'):
    labels = [k for k in al.SPEC if k.startswith(league + ' ')]
    labels = [l for l in labels if l in ('NBL 2025-26', 'NBL 2024-25', 'NBL 2023-24', 'WNBA 2026', 'WNBA 2025', 'WNBA 2024')]
    for n_first in (3, 5):
        rows = [early_diffs(l, n_first) for l in labels]
        w = [1 / v for _, v, _ in rows]
        pooled = sum(d * wi for (d, _, _), wi in zip(rows, w)) / sum(w)
        se = math.sqrt(1 / sum(w))
        print(league, f'first<{n_first}', [(l, round(d, 2), round(math.sqrt(v), 2), n) for l, (d, v, n) in zip(labels, rows)],
              'pooled', round(pooled, 2), 'CI', (round(pooled - 1.96 * se, 2), round(pooled + 1.96 * se, 2)),
              'n_early', sum(n for _, _, n in rows))

# Width z-scores, 2026-09-24 cohort (centre, width, actual) from the issued Field 3 lines and settled finals.
TOT = {'P-495': (20.07, 5.68, 26), 'P-496': (25.88, 5.92, 30), 'P-497': (176.91, 12.86, 183),
       'P-498': (167.30, 12.12, 163), 'P-499': (144.76, 15.99, 182), 'P-500': (8.40, 3.97, 6),
       'P-501': (9.82, 4.46, 6), 'P-502': (9.50, 4.35, 9), 'P-503': (5.24, 2.68, 2),
       'P-504': (171.38, 16.47, 148), 'P-505': (149.30, 15.00, 148), 'P-506': (8.01, 3.83, 11),
       'P-507': (9.59, 4.50, 5), 'P-508': (185.90, 17.60, 147), 'P-509': (179.75, 17.07, 195)}
# margin: (centre, width, actual) in the card's own sign convention
MAR = {'P-497': (3.94, 9.00, 15), 'P-498': (0.77, 8.42, 9), 'P-499': (23.36, 14.47, 20),
       'P-500': (0.61, 3.97, -2), 'P-501': (0.87, 4.48, 2), 'P-502': (0.85, 4.37, 1),
       'P-503': (1.43, 2.74, 2), 'P-504': (8.05, 16.28, 18), 'P-505': (3.70, 11.99, 6),
       'P-506': (0.13, 3.73, -1), 'P-507': (1.74, 4.56, 1), 'P-508': (1.66, 13.72, -25),
       'P-509': (1.44, 13.63, -1)}
BASK = {'P-497', 'P-498', 'P-499', 'P-504', 'P-505', 'P-508', 'P-509'}


def zs(d, keys=None):
    return {k: (a - c) / w for k, (c, w, a) in d.items() if keys is None or k in keys}


for name, d in (('total', TOT), ('margin', MAR)):
    z = zs(d)
    zb = zs(d, BASK)
    print(name, 'n', len(z), 'mean z', round(st.fmean(z.values()), 3), 'mean z^2', round(st.fmean(v * v for v in z.values()), 3),
          '| basketball n', len(zb), 'mean z^2', round(st.fmean(v * v for v in zb.values()), 3),
          '| |z|>1.645 count', sum(1 for v in z.values() if abs(v) > 1.645))
    print('  ', {k: round(v, 2) for k, v in z.items()})
