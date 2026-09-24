"""MLB 2026 regular season (statsapi): all-park total distributions, first-five-innings rates, width benchmark."""
import json
import math
import statistics as st
from collections import defaultdict

from fetch import get_json

URL = ('https://statsapi.mlb.com/api/v1/schedule?sportId=1&startDate=2026-03-25&endDate=2026-09-24'
       '&gameType=R&hydrate=linescore,venue')


def games():
    d = get_json(URL)
    out = []
    for dt_ in d['dates']:
        for g in dt_['games']:
            if g['status'].get('codedGameState') != 'F':
                continue
            ls = g.get('linescore') or {}
            inn = ls.get('innings') or []
            if (ls.get('scheduledInnings') or 9) != 9 or len(inn) < 9:
                continue
            a = g['teams']['away'].get('score')
            h = g['teams']['home'].get('score')
            if a is None or h is None:
                continue
            f5a = sum((i.get('away') or {}).get('runs', 0) or 0 for i in inn[:5])
            f5h = sum((i.get('home') or {}).get('runs', 0) or 0 for i in inn[:5])
            out.append({'pk': g['gamePk'], 'date': g['gameDate'], 'venue': g['venue']['name'],
                        'home': g['teams']['home']['team']['id'], 'away': g['teams']['away']['team']['id'],
                        'hs': h, 'as': a, 'f5': f5a + f5h, 'f5m': f5h - f5a, 'extras': len(inn) > 9})
    return out


def width(gs, min_prior=15):
    hist = defaultdict(list)
    rt, rm = [], []
    for g in sorted(gs, key=lambda x: x['date']):
        h, a = hist[g['home']], hist[g['away']]
        if len(h) >= min_prior and len(a) >= min_prior:
            hpf, hpa = st.fmean(x[0] for x in h), st.fmean(x[1] for x in h)
            apf, apa = st.fmean(x[0] for x in a), st.fmean(x[1] for x in a)
            rt.append(g['hs'] + g['as'] - ((hpf + apa) / 2 + (apf + hpa) / 2))
            rm.append(g['hs'] - g['as'] - ((hpf - hpa) - (apf - apa)) / 2)
        hist[g['home']].append((g['hs'], g['as']))
        hist[g['away']].append((g['as'], g['hs']))
    return {'n': len(rt), 'total_resid_sd': round(st.pstdev(rt), 3), 'total_resid_bias': round(st.fmean(rt), 3),
            'margin_resid_sd': round(st.pstdev(rm), 3)}


if __name__ == '__main__':
    gs = games()
    n = len(gs)
    tot = [g['hs'] + g['as'] for g in gs]
    out = {'n': n, 'total_mean': round(st.fmean(tot), 3), 'total_sd': round(st.stdev(tot), 3),
           'width': width(gs)}
    f5 = [g['f5'] for g in gs]
    out['f5'] = {'mean': round(st.fmean(f5), 3), 'sd': round(st.stdev(f5), 3),
                 'P(f5<=k)': {k: round(sum(1 for x in f5 if x <= k) / n, 4) for k in (3, 4, 5, 6)},
                 'P(tied after 5)': round(sum(1 for g in gs if g['f5m'] == 0) / n, 4),
                 'share_of_total': round(sum(f5) / sum(tot), 4)}
    by_v = defaultdict(list)
    for g in gs:
        by_v[g['venue']].append(g['hs'] + g['as'])
    rows = []
    for v, ts in by_v.items():
        if len(ts) < 30:
            continue
        m = st.fmean(ts)
        rows.append({'venue': v, 'n': len(ts), 'mean': round(m, 2), 'median': st.median(ts),
                     'se_mean': round(st.stdev(ts) / math.sqrt(len(ts)), 2),
                     'P(<=7)': round(sum(1 for t in ts if t <= 7) / len(ts), 3),
                     'P(>=10)': round(sum(1 for t in ts if t >= 10) / len(ts), 3),
                     'P(>=12)': round(sum(1 for t in ts if t >= 12) / len(ts), 3)})
    rows.sort(key=lambda r: -r['mean'])
    out['venues'] = rows
    out['small_venues'] = {v: len(ts) for v, ts in by_v.items() if len(ts) < 30}
    print(json.dumps({k: out[k] for k in ('n', 'total_mean', 'total_sd', 'width', 'f5', 'small_venues')}))
    for r in rows:
        print(r)
    json.dump(out, open('mlb_results.json', 'w', encoding='utf-8'), indent=1)
