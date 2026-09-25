"""TB-1, the team-strength baseline: out-of-sample validation on field-owner seasons (2026-09-25(e)).

Question. `BASELINE_P` (C-BASELINE-SKILL) knows only home/away. Does a leak-free team-strength
baseline carry real information (resolution) beyond that, and in which leagues? If it does, the
card has a stronger anchor to depart from, and a stronger bar to beat.

Model (tools/team_baseline.py implements the same functions):
- each team's points for and against per game, season to date, shrunk toward the league mean
  by k pseudo-games; optionally seeded by last season's shrunk rating (carry-over) regressed by r;
- total_hat  = (home PF + away PA)/2 + (away PF + home PA)/2;
- margin_hat = ((home PF − PA) − (away PF − PA))/2 + home edge to date (0 at a neutral site);
- probabilities from a normal distribution with the running residual SD (basketball, MLB, NHL
  margins), or from two Poissons (EPL goals).

Leak-free: every prediction uses only games completed before that game's date. The league mean,
home edge and residual SD are running values too.

Metrics per league-season, over every regular-season game once both teams have >= 1 prior game:
- Brier of P(home win) against the running home-win rate (the population BASELINE_P);
- Brier of P(total > running league mean total) against the running frequency of that event;
- RMSE of total_hat and margin_hat against the running league means;
- the same split by early season (either team < 5 prior games) and later.
Parameters (k, carry-over r) are chosen on the earlier seasons and reported on the latest one.

Data: research/base_rates_2026-09-25/cache (ESPN site API, MLB statsapi). No odds are read.
Output: validation_results.json. Usage: python validate_team_baseline.py
"""
import json
import math
import os
import statistics as st
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
BR = os.path.join(REPO, 'research', 'base_rates_2026-09-25')
sys.path.insert(0, BR)
sys.path.insert(0, os.path.join(REPO, 'tools'))
os.chdir(BR)  # the research fetcher resolves its cache relative to its own folder
import analyze_leagues as al  # noqa: E402
import analyze_mlb  # noqa: E402
import team_baseline as tb  # noqa: E402
from pull_oval_specs import OVAL  # noqa: E402

al.SPEC.update(OVAL)
al.SPEC.update({
    'NBL 2024-25': ('basketball/nbl', '20240918', '20250331', 'bk'),
    'NBL 2023-24': ('basketball/nbl', '20230920', '20240331', 'bk'),
    'WNBA 2025': ('basketball/wnba', '20250510', '20251020', 'bk'),
    'WNBA 2024': ('basketball/wnba', '20240510', '20241020', 'bk'),
})
CHAINS = {  # league -> seasons oldest first (carry-over flows along the chain)
    'NBL': ['NBL 2023-24', 'NBL 2024-25', 'NBL 2025-26'],
    'WNBA': ['WNBA 2024', 'WNBA 2025', 'WNBA 2026'],
    'NBA': ['NBA 2025-26'],
    'NHL': ['NHL 2025-26 (ESPN)'],
    'EPL': ['EPL 2025-26'],
    'NFL': ['NFL 2024', 'NFL 2025'],
    'AFL': ['AFL 2025', 'AFL 2026'],
    'NRL': ['NRL 2025', 'NRL 2026'],
}
KIND = {'NBL': 'normal', 'WNBA': 'normal', 'NBA': 'normal', 'NHL': 'normal', 'EPL': 'poisson', 'MLB': 'normal',
        'NFL': 'normal', 'AFL': 'normal', 'NRL': 'normal'}


def load_chain(league):
    seasons = []
    for label in CHAINS[league]:
        games, _types, _kind = al.load(label)
        # NRL labels its regular season type 1 and finals type 2: use every completed game
        reg = games if label.startswith('NRL') else al.regular(games)
        seasons.append([{'date': g['date'], 'home': g['home'], 'away': g['away'], 'hs': g['hs'], 'as': g['as'],
                         'neutral': bool(g['neutral'])} for g in reg])
    return seasons


def load_mlb():
    return [[{'date': g['date'], 'home': g['home'], 'away': g['away'], 'hs': g['hs'], 'as': g['as'], 'neutral': False}
             for g in analyze_mlb.games()]]


def brier(ps, ys):
    return sum((p - y) ** 2 for p, y in zip(ps, ys)) / len(ys)


def evaluate(season, prev_ratings, k, r, kind, min_prior=1):
    """Walk one season in date order; predict each game from prior games only."""
    rows = []
    state = tb.SeasonState(prior=prev_ratings, k=k, carry=r)
    for g in sorted(season, key=lambda x: x['date']):
        nh, na = state.n_games(g['home']), state.n_games(g['away'])
        if min(nh, na) >= min_prior and state.n_league_games() >= 10:
            pred = state.predict(g['home'], g['away'], neutral=g['neutral'])
            sd_m, sd_t = state.resid_sd()
            tot_ref = state.league_total_mean()
            if kind == 'poisson':
                lh, la = tb.team_means(pred['total'], pred['margin'])
                p_home = tb.poisson_win(lh, la)
                p_over = tb.poisson_total_over(lh + la, tot_ref)
            else:
                p_home = tb.normal_cdf(pred['margin'] / sd_m)
                p_over = 1 - tb.normal_cdf((tot_ref - pred['total']) / sd_t)
            rows.append({'early': min(nh, na) < 5, 'p_home': p_home, 'y_home': 1 if g['hs'] > g['as'] else 0,
                         'base_home': state.home_win_rate(), 'p_over': p_over,
                         'y_over': 1 if g['hs'] + g['as'] > tot_ref else 0, 'base_over': state.over_rate(),
                         'tot_err': g['hs'] + g['as'] - pred['total'], 'tot_err0': g['hs'] + g['as'] - tot_ref,
                         'mar_err': g['hs'] - g['as'] - pred['margin'],
                         'mar_err0': g['hs'] - g['as'] - state.home_edge(neutral=g['neutral'])})
        state.add(g)
    return rows, state.final_ratings()


def summarise(rows):
    if not rows:
        return None
    def rmse(key):
        return math.sqrt(sum(r[key] ** 2 for r in rows) / len(rows))
    yh = [r['y_home'] for r in rows]
    yo = [r['y_over'] for r in rows]
    # draws (EPL) count as "not a home win"; the base rate handles them the same way
    return {'n': len(rows),
            'home_win': {'brier_model': round(brier([r['p_home'] for r in rows], yh), 4),
                         'brier_base': round(brier([r['base_home'] for r in rows], yh), 4)},
            'total_over_league_mean': {'brier_model': round(brier([r['p_over'] for r in rows], yo), 4),
                                       'brier_base': round(brier([r['base_over'] for r in rows], yo), 4)},
            'total_rmse': {'model': round(rmse('tot_err'), 3), 'league_mean': round(rmse('tot_err0'), 3)},
            'margin_rmse': {'model': round(rmse('mar_err'), 3), 'home_edge_only': round(rmse('mar_err0'), 3)}}


def run_chain(seasons, k, r, kind):
    prev = None
    out = []
    for s in seasons:
        rows, prev = evaluate(s, prev, k, r, kind)
        out.append(rows)
    return out


def main():
    results = {}
    grid_k = [0, 2, 5, 10, 20]
    grid_r = [0.0, 0.5, 0.75]
    leagues = dict((lg, load_chain(lg)) for lg in CHAINS)
    leagues['MLB'] = load_mlb()
    for lg, seasons in leagues.items():
        kind = KIND[lg]
        # choose (k, r) on the earlier seasons when there are any, else on the season itself (flagged)
        tune = []
        for k in grid_k:
            for r in (grid_r if len(seasons) > 1 else [0.0]):
                per = run_chain(seasons, k, r, kind)
                rows = [x for s in per[:-1] for x in s] if len(seasons) > 1 else per[-1]
                if not rows:
                    continue
                score = brier([x['p_home'] for x in rows], [x['y_home'] for x in rows])
                tune.append((score, k, r))
        tune.sort()
        _, k_best, r_best = tune[0]
        per = run_chain(seasons, k_best, r_best, kind)
        latest = per[-1]
        results[lg] = {'seasons': CHAINS.get(lg, ['MLB 2026']), 'kind': kind, 'k': k_best, 'carry_r': r_best,
                       'tuned_on': 'earlier seasons' if len(seasons) > 1 else 'SAME season (no earlier season cached)',
                       'latest_all': summarise(latest),
                       'latest_early(<5 prior games)': summarise([x for x in latest if x['early']]),
                       'latest_later': summarise([x for x in latest if not x['early']])}
        if len(seasons) > 1:
            no_carry = run_chain(seasons, k_best, 0.0, kind)[-1]
            results[lg]['latest_early_without_carry'] = summarise([x for x in no_carry if x['early']])
        print(lg, json.dumps(results[lg], indent=None))
    with open(os.path.join(HERE, 'validation_results.json'), 'w', encoding='utf-8') as fh:
        json.dump(results, fh, indent=2)


if __name__ == '__main__':
    main()
