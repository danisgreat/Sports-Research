"""C1 — would shrinking the team model's 0.70-0.80 favourites make it better? (preregistered in this docstring,
2026-09-27, before any run; the user's bar: "do a model change only if it is absolutely going to make it better")

Origin: P5 (exploratory) found the NFL 2025 and NRL 2026 favourite bands at 0.70-0.80 won about 67% at a stated
0.74-0.75. Those seasons revealed the pattern, so they cannot confirm it.

Stage 1 — replication on windows that played no part in finding it:
- NFL regular seasons 2021, 2022, 2023, 2024 (nflverse games.csv, the validate_public.py loader; results only);
- NRL 2025 (ESPN scoreboard cache; forecasts from 2025-04-15, earlier 2025 games as history).
Model: tools/sport_models.py A1, constants unchanged, rolling origin, leak-free (TeamEngine.replay).
Statistic: gap = win rate - mean stated probability over favourites stated in [0.70, 0.80); 95% ISO-week block
bootstrap (2,000 draws, seed 20260927).
PASS only if the pooled NFL 2021-24 gap AND the NRL 2025 gap are both below 0 with their intervals excluding 0.

Stage 2 — run only if Stage 1 passes (NFL):
- fit one logit shrink factor s in {0.70, 0.72, ..., 1.00} on NFL 2021-2023 by win Brier over every game;
- test on NFL 2024 and on NFL 2025 separately: Brier(s) - Brier(1) with the week-block interval.
A MODEL_CHANGE is proposed only if s < 1 and BOTH test intervals lie entirely below 0.

Anything short of that: no change. Market-blind: only teams, dates and scores are read.
"""
import json
import math
import os
import random
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools'))
sys.path.insert(0, os.path.join(REPO, 'research', 'sport_models_2026-09-26'))
sys.path.insert(0, HERE)
import sport_models as sm  # noqa: E402
import validate_public as vp  # noqa: E402

BOOT, SEED = 2000, 20260927
LO, HI = 0.70, 0.80


def replay_rows(cfg, games, start, end):
    eng = sm.TeamEngine(cfg, games)
    warm = None
    rows = []
    for item in eng.replay(start, end, warm_from=warm):
        g, _f0, f1 = item[:3]
        q = f1.probs()
        ph, pa = q['p_home_win'], q['p_away_win']
        if g['hs'] == g['as']:
            continue                      # ties (rare in both codes) have no side winner
        y = int(g['hs'] > g['as'])
        p2 = ph + pa
        ph_n = ph / p2 if p2 > 0 else 0.5   # two-way home probability (a draw's mass removed)
        rows.append({'week': sm.iso_week(g['date'][:10]), 'season': g.get('season'), 'p': ph_n, 'y': y})
    return rows


def boot_ci(rows, stat):
    by = defaultdict(list)
    for r in rows:
        by[r['week']].append(r)
    weeks = sorted(by)
    rng = random.Random(SEED)
    vals = []
    for _ in range(BOOT):
        sample = [r for w in (rng.choice(weeks) for _ in weeks) for r in by[w]]
        v = stat(sample)
        if v is not None:
            vals.append(v)
    vals.sort()
    return [round(vals[int(0.025 * len(vals))], 4), round(vals[int(0.975 * len(vals)) - 1], 4)]


def band_gap(rows):
    sub = []
    for r in rows:
        fp = max(r['p'], 1 - r['p'])
        if LO <= fp < HI:
            sub.append((fp, r['y'] if r['p'] >= 0.5 else 1 - r['y']))
    if not sub:
        return None
    return sum(w for _, w in sub) / len(sub) - sum(p for p, _ in sub) / len(sub)


def band_summary(rows):
    sub = [(max(r['p'], 1 - r['p']), r['y'] if r['p'] >= 0.5 else 1 - r['y']) for r in rows
           if LO <= max(r['p'], 1 - r['p']) < HI]
    return {'games': len(rows), 'band_n': len(sub),
            'band_mean_p': round(sum(p for p, _ in sub) / len(sub), 4) if sub else None,
            'band_won': round(sum(w for _, w in sub) / len(sub), 4) if sub else None,
            'gap': round(band_gap(rows), 4) if sub else None,
            'gap_ci95': boot_ci(rows, band_gap) if sub else None}


def shrink(p, s):
    p = min(max(p, 1e-6), 1 - 1e-6)
    return 1 / (1 + math.exp(-s * math.log(p / (1 - p))))


def brier(rows, s):
    return sum((shrink(r['p'], s) - r['y']) ** 2 for r in rows) / len(rows)


def main():
    out = {'preregistered': 'docstring of this file, 2026-09-27, before any run', 'band': [LO, HI]}
    nfl_games = vp.nfl()
    cfg = sm.config('nfl')
    nfl = {}
    for season in (2021, 2022, 2023, 2024, 2025):
        rows = replay_rows(cfg, [g for g in nfl_games if g['season'] <= season],
                           f'{season}-09-01', f'{season + 1}-02-15')
        nfl[season] = [r for r in rows if r['season'] == season]
        out[f'nfl_{season}'] = band_summary(nfl[season])
        print('nfl', season, out[f'nfl_{season}'], flush=True)
    pooled = [r for s in (2021, 2022, 2023, 2024) for r in nfl[s]]
    out['nfl_2021_2024_pooled'] = band_summary(pooled)
    print('nfl pooled', out['nfl_2021_2024_pooled'], flush=True)

    # NRL 2025 from the ESPN cache (the P5 loader), forecasts from 2025-04-15
    import p5_predictability_map as p5
    nrl_games = p5.espn_games([p5.OVAL['NRL 2025'][:3]], 'points')
    nrl_rows = replay_rows(sm.config('nrl'), nrl_games, '2025-04-15', '2025-10-06')
    out['nrl_2025'] = band_summary(nrl_rows)
    print('nrl 2025', out['nrl_2025'], flush=True)

    def below(ci):
        return ci is not None and ci[1] < 0
    stage1 = below(out['nfl_2021_2024_pooled']['gap_ci95']) and below(out['nrl_2025']['gap_ci95'])
    out['stage1_pass'] = stage1
    if stage1:
        train = [r for s in (2021, 2022, 2023) for r in nfl[s]]
        grid = [round(0.70 + 0.02 * i, 2) for i in range(16)]
        s_best = min(grid, key=lambda s: brier(train, s))
        out['stage2'] = {'s_fitted_2021_2023': s_best}
        ok = s_best < 1
        for season in (2024, 2025):
            rows = nfl[season]
            d = brier(rows, s_best) - brier(rows, 1.0)
            ci = boot_ci(rows, lambda xs: brier(xs, s_best) - brier(xs, 1.0))
            out['stage2'][str(season)] = {'brier_diff': round(d, 5), 'ci95': ci}
            ok = ok and ci[1] < 0
        out['stage2']['pass'] = ok
    out['verdict'] = ('MODEL_CHANGE supported' if stage1 and out['stage2']['pass']
                      else 'NO CHANGE: the preregistered bar was not met')
    print(out['verdict'])
    json.dump(out, open(os.path.join(HERE, 'c1_band_check_results.json'), 'w'), indent=2)


if __name__ == '__main__':
    main()
