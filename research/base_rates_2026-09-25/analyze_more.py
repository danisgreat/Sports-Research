"""Multi-season early-season total check (NBL, WNBA); EPL 1H goals and corners; season-level base rates
for prior seasons (for stability of the 2025-26 figures)."""
import json
import math
import re
import statistics as st
from collections import Counter, defaultdict

import analyze_leagues as al
from fetch import espn_scoreboard

SEASONS = {
    'NBL 2025-26': ('basketball/nbl', '20250918', '20260331', 'bk'),
    'NBL 2024-25': ('basketball/nbl', '20240918', '20250331', 'bk'),
    'NBL 2023-24': ('basketball/nbl', '20230920', '20240331', 'bk'),
    'WNBA 2026': ('basketball/wnba', '20260501', '20260924', 'bk'),
    'WNBA 2025': ('basketball/wnba', '20250510', '20251020', 'bk'),
    'WNBA 2024': ('basketball/wnba', '20240510', '20241020', 'bk'),
}
al.SPEC.update(SEASONS)


def ci(xs):
    m = st.fmean(xs)
    se = st.stdev(xs) / math.sqrt(len(xs))
    return round(m, 2), round(m - 1.96 * se, 2), round(m + 1.96 * se, 2), len(xs)


def early_vs_rest(games, first_n_team_games=3):
    """Game total in games where BOTH teams have played < first_n games v the rest of the regular season."""
    played = Counter()
    early, rest = [], []
    for g in sorted(games, key=lambda x: x['date']):
        t = g['hs'] + g['as']
        if played[g['home']] < first_n_team_games and played[g['away']] < first_n_team_games:
            early.append(t)
        else:
            rest.append(t)
        played[g['home']] += 1
        played[g['away']] += 1
    return {'early': ci(early), 'rest': ci(rest), 'diff': round(st.fmean(early) - st.fmean(rest), 2)}


def season_block(label):
    games, types, kind = al.load(label)
    reg = al.regular(games)
    b = al.base_rates(reg, kind)
    w = al.width_benchmark(reg, kind)
    return {'n': len(reg), 'total_mean': round(b['total_mean'], 2), 'total_sd': round(b['total_sd'], 2),
            'margin_sd': round(b['margin_sd'], 2), 'home_margin': [round(x, 2) for x in b['home_margin_mean']],
            'home_win': round(b['home_win'][0], 3), 'ot_rate': round(b['ot_rate'][0], 3),
            'abs_margin_le5': round(b['abs_margin_le'][5], 3), 'abs_margin_le3': round(b['abs_margin_le'][3], 3),
            'total_resid_sd': round(w['total_resid_sd'], 2), 'margin_resid_sd': round(w['margin_resid_sd'], 2),
            'total_resid_bias': round(w['total_resid_bias'], 2),
            'early3': early_vs_rest(reg, 3), 'early5': early_vs_rest(reg, 5),
            'h1_share': round(b['h1_share'], 4), 'quarter_means': [round(x, 2) for x in b['quarter_means']]}


def minute(clock):
    m = re.match(r"(\d+)'(?:\+(\d+))?", clock or '')
    return int(m.group(1)) if m else None


def epl():
    rows = json.load(open('epl_summaries.json', encoding='utf-8'))
    h1, h2, corners, corner_team, shots = [], [], [], [], []
    missing_goals = 0
    evs = {e['id']: e for e in espn_scoreboard('soccer/eng.1', '20250815', '20260524')['events']}
    for r in rows:
        ev = evs[r['id']]
        cps = ev['competitions'][0]['competitors']
        total = sum(int(c['score']) for c in cps)
        goals = r['goals']
        if len(goals) != total:
            missing_goals += 1
            continue
        p1 = sum(1 for g in goals if g['period'] == 1)
        h1.append(p1)
        h2.append(total - p1)
        cs = [t['wonCorners'] for t in r['teams']]
        if all(c not in (None, '') for c in cs) and len(cs) == 2:
            cs = [int(float(c)) for c in cs]
            corners.append(sum(cs))
            corner_team.extend(cs)
    n = len(h1)
    out = {'n_1h': n, 'excluded_goal_count_mismatch': missing_goals,
           'h1_mean': round(st.fmean(h1), 3), 'h2_mean': round(st.fmean(h2), 3),
           'h1_dist': {k: round(sum(1 for x in h1 if x == k) / n, 4) for k in range(0, 5)},
           'P(1H>=1)': round(sum(1 for x in h1 if x >= 1) / n, 4), 'P(1H>=2)': round(sum(1 for x in h1 if x >= 2) / n, 4),
           'P(1H>=3)': round(sum(1 for x in h1 if x >= 3) / n, 4)}
    if corners:
        nc = len(corners)
        out.update({'n_corners': nc, 'corners_mean': round(st.fmean(corners), 2), 'corners_sd': round(st.stdev(corners), 2),
                    'corners_median': st.median(corners),
                    'P(corners>=k)': {k: round(sum(1 for c in corners if c >= k) / nc, 4) for k in (8, 9, 10, 11, 12)},
                    'team_corners_mean_sd': (round(st.fmean(corner_team), 2), round(st.stdev(corner_team), 2))})
    return out


if __name__ == '__main__':
    res = {}
    for label in SEASONS:
        res[label] = season_block(label)
        print(label, json.dumps(res[label]))
    res['EPL 2025-26 summaries'] = epl()
    print('EPL', json.dumps(res['EPL 2025-26 summaries']))
    json.dump(res, open('more_results.json', 'w', encoding='utf-8'), indent=1)
