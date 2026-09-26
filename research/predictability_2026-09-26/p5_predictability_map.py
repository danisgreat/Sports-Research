"""P5 (EXPLORATORY, not preregistered; descriptive only) — how predictable is each sport, in Rank-1 terms?

For each league's latest season, replay the validated team model leak-free (every game forecast from games
strictly before its date; the same code path as validate) and report:
- result Brier of the model and of the league baseline A0 (the population);
- how often the model's favourite (side) reaches each probability band, and how often it won there;
- the same for the total at the league line (floor(mean of prior games) + 0.5): the more likely side;
- calibration of the >= 0.70 band (mean stated against win rate).
"STRONG" means the model's favourite at >= 0.70, the tier where Rank 1 was far more likely to win than lose
on the cards (research/rank_model_2026-09-25e).

Models: tools/sport_models.py A1 (constants unchanged) for the ESPN leagues; tools/mlb_model.py A1 team-only for
MLB. Data: the local caches only (research/base_rates_2026-09-25 ESPN scoreboards, parsed by
tools/sport_data.parse_espn_event; the MLB statsapi schedule cached by mlb_starters.py). Writes
p5_predictability_results.json.
"""
import datetime as dt
import json
import math
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
BR = os.path.join(REPO, 'research', 'base_rates_2026-09-25')
sys.path.insert(0, os.path.join(REPO, 'tools'))
sys.path.insert(0, BR)
sys.path.insert(0, HERE)
import sport_data as sd  # noqa: E402
import sport_models as sm  # noqa: E402
import mlb_model as mm  # noqa: E402
import mlb_starters as ms  # noqa: E402

cwd = os.getcwd()
os.chdir(BR)
from fetch import espn_scoreboard  # noqa: E402
from pull_oval_specs import OVAL  # noqa: E402
os.chdir(cwd)

# league -> (family, [ESPN seasons oldest first], test window = the latest season)
SPEC = {
    'nba': ('points', [('basketball/nba', '20251021', '20260620')], ('2025-12-01', '2026-06-20')),
    'wnba': ('points', [('basketball/wnba', '20240510', '20241020'), ('basketball/wnba', '20250510', '20251020'),
                        ('basketball/wnba', '20260501', '20260924')], ('2026-05-01', '2026-09-24')),
    'nbl': ('points', [('basketball/nbl', '20240918', '20250331'), ('basketball/nbl', '20250918', '20260331')],
            ('2025-09-01', '2026-04-30')),
    'nfl': ('points', [OVAL['NFL 2024'][:3], OVAL['NFL 2025'][:3]], ('2025-09-01', '2026-02-15')),
    'afl': ('points', [OVAL['AFL 2025'][:3], OVAL['AFL 2026'][:3]], ('2026-03-01', '2026-09-24')),
    'nrl': ('points', [OVAL['NRL 2025'][:3], OVAL['NRL 2026'][:3]], ('2026-03-01', '2026-09-24')),
    'nhl': ('hockey', [('hockey/nhl', '20251007', '20260620')], ('2025-12-01', '2026-06-20')),
    'epl': ('goals', [('soccer/eng.1', '20250815', '20260524')], ('2025-11-01', '2026-05-24')),
}
BANDS = [(0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 1.01)]


def espn_games(seasons, family):
    os.chdir(BR)
    seen, out = set(), []
    for path, s, e in seasons:
        for ev in espn_scoreboard(path, s, e)['events']:
            g = sd.parse_espn_event(ev, family)
            if g and g['completed'] and g['hs'] is not None and g['id'] not in seen:
                seen.add(g['id'])
                out.append(g)
    os.chdir(cwd)
    return sorted(out, key=lambda g: g['date'])


def summarise(rows):
    """rows: dicts with fav_p, fav_won, tot_p, tot_won, b1, b0 (result Brier of model and A0)."""
    n = len(rows)
    out = {'games': n, 'result_brier_model': round(sum(r['b1'] for r in rows) / n, 4),
           'result_brier_A0': round(sum(r['b0'] for r in rows) / n, 4)}
    for key, won, label in (('fav_p', 'fav_won', 'side'), ('tot_p', 'tot_won', 'total')):
        bands = {}
        for lo, hi in BANDS:
            sub = [r for r in rows if r.get(key) is not None and lo <= r[key] < hi]
            if sub:
                bands[f'{lo:.1f}-{min(hi, 1):.1f}'] = {'share': round(len(sub) / n, 3), 'n': len(sub),
                                                       'won': round(sum(r[won] for r in sub) / len(sub), 3),
                                                       'mean_p': round(sum(r[key] for r in sub) / len(sub), 3)}
        strong = [r for r in rows if r.get(key) is not None and r[key] >= 0.70]
        out[label] = {'bands': bands, 'strong_share': round(len(strong) / n, 3),
                      'strong_won': round(sum(r[won] for r in strong) / len(strong), 3) if strong else None,
                      'strong_mean_p': round(sum(r[key] for r in strong) / len(strong), 3) if strong else None}
    return out


def team_league(lg):
    family, seasons, (a, b) = SPEC[lg]
    games = espn_games(seasons, family)
    cfg = sm.config(lg)
    eng = sm.TeamEngine(cfg, games)
    hist = [g for g in eng.games if g['date'][:10] < a]
    recent = hist[-min(len(hist), 1000):]
    line = math.floor(sum(g['hs'] + g['as'] for g in recent) / len(recent)) + 0.5
    warm = (dt.date.fromisoformat(a) - dt.timedelta(days=cfg.get('resid_days') or 0)).isoformat()
    rows = []
    for g, f0, f1 in eng.replay(a, b, warm_from=warm):
        q1, q0 = f1.probs(total=line), f0.probs()
        ph, pa = q1['p_home_win'], q1['p_away_win']
        home_fav = ph >= pa
        fav_p = max(ph, pa)
        y_home, y_away = int(g['hs'] > g['as']), int(g['as'] > g['hs'])
        over = int(g['hs'] + g['as'] > line)
        po = q1['p_over']
        rows.append({'fav_p': fav_p, 'fav_won': y_home if home_fav else y_away,
                     'tot_p': max(po, q1['p_under']), 'tot_won': over if po >= q1['p_under'] else int(not over and
                                                                                                    g['hs'] + g['as'] != line),
                     'b1': (ph - y_home) ** 2, 'b0': (q0['p_home_win'] - y_home) ** 2})
    res = summarise(rows)
    res.update({'window': [a, b], 'total_line': line, 'model': 'A1 ' + sm.MODEL_VERSION})
    return res


def mlb():
    games = ms.schedule(2026)
    by = defaultdict(list)
    for g in games:
        by[g['date']].append(g)
    prior, rows = [], []
    for d in sorted(by):
        if len(prior) >= 300:
            rt = mm.Ratings(prior)
            a0w = sum(x['hr'] > x['ar'] for x in prior) / len(prior)
            line = math.floor(sum(x['hr'] + x['ar'] for x in prior) / len(prior)) + 0.5
            for g in by[d]:
                j, _, _ = rt.joint(g['home'], g['away'], g['venue'])
                ph = mm.queries(j, None)['p_home_win']
                po = math.fsum(v for (h, a), v in j.items() if h + a > line)
                y = int(g['hr'] > g['ar'])
                over = int(g['hr'] + g['ar'] > line)
                rows.append({'fav_p': max(ph, 1 - ph), 'fav_won': y if ph >= 0.5 else 1 - y,
                             'tot_p': max(po, 1 - po), 'tot_won': over if po >= 0.5 else 1 - over,
                             'b1': (ph - y) ** 2, 'b0': (a0w - y) ** 2})
        prior += by[d]
    res = summarise(rows)
    res.update({'window': ['2026 season, after 300 games', '2026-09-24'], 'model': 'A1 team-only ' + mm.MODEL_VERSION})
    return res


def main():
    out = {}
    for lg in SPEC:
        out[lg] = team_league(lg)
        print(lg, json.dumps({k: out[lg][k] for k in ('games', 'result_brier_model', 'result_brier_A0')}),
              'side STRONG', out[lg]['side']['strong_share'], out[lg]['side']['strong_won'],
              'total STRONG', out[lg]['total']['strong_share'], out[lg]['total']['strong_won'], flush=True)
    out['mlb'] = mlb()
    print('mlb', out['mlb']['result_brier_model'], out['mlb']['side']['strong_share'], out['mlb']['side']['strong_won'])
    json.dump(out, open(os.path.join(HERE, 'p5_predictability_results.json'), 'w'), indent=2)


if __name__ == '__main__':
    main()
