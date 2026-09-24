"""Tennis 2026 (ESPN tennis scoreboard, 1 Jan – 24 Sep): total games and game-margin base rates for completed
singles matches. Retirements, walkovers and unfinished matches are excluded (their totals are censored).
Best-of-5 = men's singles main draw at the four Slams; everything else best-of-3."""
import json
import math
import re
import statistics as st
from collections import Counter, defaultdict

SLAMS = {'Australian Open', 'Roland Garros', 'Wimbledon', 'US Open'}

comps = {}
for tour in ('wta', 'atp'):
    comps.update(json.load(open(tour + '.json', encoding='utf-8')))


def is_qual(c):
    return 'qualif' in ((c.get('round') or {}).get('displayName') or '').lower()


def rows():
    out = []
    for cid, c in comps.items():
        if c['grouping'] not in ("Women's Singles", "Men's Singles"):
            continue
        if (c['status'] or {}).get('name') != 'STATUS_FINAL':
            continue
        cps = c['competitors']
        if len(cps) != 2:
            continue
        a = [x.get('value') for x in cps[0]['linescores']]
        b = [x.get('value') for x in cps[1]['linescores']]
        if not a or len(a) != len(b) or any(v is None for v in a + b):
            continue
        a, b = [int(v) for v in a], [int(v) for v in b]
        # sanity: every set must be a completed set score
        ok = all((max(x, y) == 6 and min(x, y) <= 4) or (max(x, y) == 7 and min(x, y) in (5, 6)) or
                 (max(x, y) >= 6 and abs(x - y) == 2) or (max(x, y) >= 7 and abs(x - y) >= 2) for x, y in zip(a, b))
        if not ok:
            continue
        men = c['grouping'] == "Men's Singles"
        bo5 = men and c['tournament'] in SLAMS and not is_qual(c)
        sets_won_a = sum(1 for x, y in zip(a, b) if x > y)
        sets_won_b = len(a) - sets_won_a
        need = 3 if bo5 else 2
        if max(sets_won_a, sets_won_b) != need:
            continue
        w_games = sum(a) if sets_won_a > sets_won_b else sum(b)
        l_games = sum(b) if sets_won_a > sets_won_b else sum(a)
        tb = sum(1 for x, y in zip(a, b) if {x, y} == {7, 6})
        out.append({'women': not men, 'bo5': bo5, 'slam': c['tournament'] in SLAMS, 'qual': is_qual(c),
                    'tournament': c['tournament'], 'sets': len(a), 'total': sum(a) + sum(b),
                    'margin': w_games - l_games, 'tb': tb})
    return out


def summarize(rs, label):
    n = len(rs)
    tot = [r['total'] for r in rs]
    mar = [r['margin'] for r in rs]
    deciding = [r for r in rs if r['sets'] == (5 if rs and rs[0]['bo5'] else 3)]
    q = st.quantiles(tot, n=10)
    res = {'label': label, 'n': n, 'total_mean': round(st.fmean(tot), 2), 'total_sd': round(st.stdev(tot), 2),
           'total_median': st.median(tot), 'total_p10_p90': (q[0], q[-1]),
           'P(deciding set)': round(len(deciding) / n, 4),
           'mean_total_straight': round(st.fmean(r['total'] for r in rs if r not in deciding), 2),
           'mean_total_deciding': round(st.fmean(r['total'] for r in deciding), 2) if deciding else None,
           'P(total>=k)': {k: round(sum(1 for t in tot if t >= k) / n, 4) for k in (18, 19, 20, 21, 22, 23, 24, 25)},
           'winner_margin_mean_sd': (round(st.fmean(mar), 2), round(st.stdev(mar), 2)),
           'P(winner margin>=k)': {k: round(sum(1 for m in mar if m >= k) / n, 4) for k in (2, 3, 4, 5, 6, 7, 8)},
           'P(any tiebreak)': round(sum(1 for r in rs if r['tb']) / n, 4)}
    se_p = lambda p: round(1.96 * math.sqrt(p * (1 - p) / n), 4)
    res['CI95_halfwidth_P(deciding)'] = se_p(res['P(deciding set)'])
    return res


if __name__ == '__main__':
    rs = rows()
    groups = {
        "Women's singles, all (best of 3)": [r for r in rs if r['women']],
        "Women's singles, main draw": [r for r in rs if r['women'] and not r['qual']],
        "Women's singles, qualifying": [r for r in rs if r['women'] and r['qual']],
        "Women's singles, Slams main draw": [r for r in rs if r['women'] and r['slam'] and not r['qual']],
        "Women's singles, non-Slam main draw": [r for r in rs if r['women'] and not r['slam'] and not r['qual']],
        "Men's singles, best of 3 (all non-Slam-main)": [r for r in rs if not r['women'] and not r['bo5']],
        "Men's singles, Slams main draw (best of 5)": [r for r in rs if r['bo5']],
    }
    out = {}
    for k, v in groups.items():
        out[k] = summarize(v, k)
        print(json.dumps(out[k]))
    tcount = Counter(r['tournament'] for r in rs if r['women'])
    out['n_tournaments_women'] = len(tcount)
    out['excluded_status'] = Counter((c['status'] or {}).get('name') for c in comps.values()
                                     if c['grouping'] in ("Women's Singles", "Men's Singles"))
    print('women tournaments', len(tcount), 'status', out['excluded_status'])
    json.dump(out, open('tennis_results.json', 'w', encoding='utf-8'), indent=1, default=str)
