"""Population base rates for NFL, AFL and NRL (2026-09-25(e)). REFERENCE / LEARNING_ONLY.

Until now every NFL, AFL and NRL card printed `REFERENCE_BASE_RATE: NOT_YET_DERIVED`, and those
sports carry the framework's worst Rank-1/Rank-2 record (12 W / 20 L in the probability era), mostly
underdog cushions (+k.5) and totals. This script derives, per league and season, from field-owner
scores (ESPN site API; no odds are read):
- home-win and draw rates (neutral-site games excluded from the home figures);
- total mean, SD and quantiles; margin SD; P(|margin| = k) and P(|margin| <= k);
- NFL key-number masses at 3 and 7 (G-L12 residual benchmark);
- the population cover rate of the TB-1 underdog at +k.5 for common k, where the underdog is the
  side with the lower leak-free TB-1 margin (the market is never used to define a favourite);
- TB-1 residual SDs (the reference widths).
The same underdog-cushion table is also computed for the cached NBA, WNBA and NBL seasons.
Output: oval_base_rates.json. Usage: python oval_base_rates.py
"""
import json
import math
import os
import statistics as st
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
BR = os.path.join(REPO, 'research', 'base_rates_2026-09-25')
sys.path.insert(0, BR)
sys.path.insert(0, os.path.join(REPO, 'tools'))
os.chdir(BR)
import analyze_leagues as al  # noqa: E402
import team_baseline as tb  # noqa: E402
from pull_oval_specs import OVAL  # noqa: E402

KS = {'fb': [1.5, 2.5, 3.5, 6.5, 7.5, 10.5, 13.5], 'afl': [6.5, 12.5, 18.5, 24.5, 30.5],
      'nrl': [1.5, 2.5, 4.5, 6.5, 8.5, 12.5], 'bk': [1.5, 2.5, 3.5, 5.5, 7.5, 9.5]}
# Basketball seasons already in the cache (research/base_rates_2026-09-25), for the cushion table only.
BASKETBALL = {
    'NBA 2025-26': ('basketball/nba', '20251021', '20260620', 'bk'),
    'WNBA 2026': ('basketball/wnba', '20260501', '20260924', 'bk'),
    'WNBA 2025': ('basketball/wnba', '20250510', '20251020', 'bk'),
    'NBL 2025-26': ('basketball/nbl', '20250918', '20260331', 'bk'),
    'NBL 2024-25': ('basketball/nbl', '20240918', '20250331', 'bk'),
}


def games_of(label):
    al.SPEC[label] = OVAL.get(label) or BASKETBALL[label]
    games, _t, _k = al.load(label)
    # NRL labels its regular season type 1 and finals type 2: use every completed game
    reg = games if label.startswith('NRL') else al.regular(games)
    return [{'date': g['date'], 'home': g['home'], 'away': g['away'], 'hs': g['hs'], 'as': g['as'],
             'neutral': bool(g['neutral'])} for g in reg]


def rates(games, kind, k_shrink=5):
    n = len(games)
    nn = [g for g in games if not g['neutral']]
    tot = [g['hs'] + g['as'] for g in games]
    mar = [g['hs'] - g['as'] for g in games]
    absm = [abs(m) for m in mar]
    q = sorted(tot)
    out = {'n': n, 'n_non_neutral': len(nn),
           'home_win': round(sum(g['hs'] > g['as'] for g in nn) / len(nn), 4) if nn else None,
           'draw': round(sum(m == 0 for m in mar) / n, 4),
           'total_mean': round(st.fmean(tot), 2), 'total_sd': round(st.stdev(tot), 2),
           'total_q10_50_90': [q[int(0.1 * n)], q[n // 2], q[int(0.9 * n)]],
           'home_margin_mean': round(st.fmean(m for m in (g['hs'] - g['as'] for g in nn)), 2) if nn else None,
           'margin_sd': round(st.stdev(mar), 2)}
    if kind == 'bk':
        for k in (2, 4, 6, 10):
            out[f'P(|margin|<={k})'] = round(sum(a <= k for a in absm) / n, 4)
    elif kind == 'fb':
        out['P(|margin|=3)'] = round(sum(a == 3 for a in absm) / n, 4)
        out['P(|margin|=7)'] = round(sum(a == 7 for a in absm) / n, 4)
        out['P(|margin|<=3)'] = round(sum(a <= 3 for a in absm) / n, 4)
        out['P(|margin|<=7)'] = round(sum(a <= 7 for a in absm) / n, 4)
    else:
        for k in (6, 12, 18, 24) if kind == 'afl' else (2, 4, 6, 8, 12):
            out[f'P(|margin|<={k})'] = round(sum(a <= k for a in absm) / n, 4)
    # TB-1 underdog cushion rates, leak-free
    state = tb.SeasonState(k=k_shrink)
    cover = {k: [0, 0] for k in KS[kind]}
    dog_win = [0, 0]
    res_t, res_m = [], []
    for g in sorted(games, key=lambda x: x['date']):
        if state.n_games(g['home']) >= 2 and state.n_games(g['away']) >= 2 and state.n_league_games() >= 10:
            p = state.predict(g['home'], g['away'], neutral=g['neutral'])
            res_t.append(g['hs'] + g['as'] - p['total'])
            res_m.append(g['hs'] - g['as'] - p['margin'])
            if abs(p['margin']) >= 0.5:
                dog_margin = (g['as'] - g['hs']) if p['margin'] > 0 else (g['hs'] - g['as'])
                dog_win[0] += dog_margin > 0
                dog_win[1] += 1
                for k in KS[kind]:
                    cover[k][0] += dog_margin + k > 0
                    cover[k][1] += 1
        state.add(g)
    out['tb1_underdog_win'] = round(dog_win[0] / dog_win[1], 4) if dog_win[1] else None
    out['tb1_underdog_cover'] = {f'+{k}': round(v[0] / v[1], 4) for k, v in cover.items() if v[1]}
    out['tb1_underdog_n'] = dog_win[1]
    if res_t:
        out['tb1_resid_sd_total'] = round(math.sqrt(sum(x * x for x in res_t) / len(res_t)), 2)
        out['tb1_resid_sd_margin'] = round(math.sqrt(sum(x * x for x in res_m) / len(res_m)), 2)
    return out


def main():
    out = {}
    for label, spec in list(OVAL.items()) + list(BASKETBALL.items()):
        try:
            gs = games_of(label)
        except Exception as exc:  # noqa: BLE001
            out[label] = {'error': str(exc)}
            continue
        if not gs:
            out[label] = {'error': 'no completed games'}
            continue
        out[label] = rates(gs, spec[3])
        print(label, json.dumps(out[label]))
    with open(os.path.join(HERE, 'oval_base_rates.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=2)


if __name__ == '__main__':
    main()
