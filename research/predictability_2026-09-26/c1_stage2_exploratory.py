"""C1 Stage 2 on the NFL alone — EXPLORATORY (run after Stage 1 failed on the NRL; cannot justify a change).

Same fit/test as c1_band_check.py Stage 2: logit shrink s fitted on NFL 2021-2023 by win Brier, tested on 2024 and
2025 with week-block intervals. Written to c1_stage2_exploratory_results.json.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import c1_band_check as c1  # noqa: E402


def main():
    games = c1.vp.nfl()
    cfg = c1.sm.config('nfl')
    nfl = {}
    for season in (2021, 2022, 2023, 2024, 2025):
        rows = c1.replay_rows(cfg, [g for g in games if g['season'] <= season], f'{season}-09-01', f'{season + 1}-02-15')
        nfl[season] = [r for r in rows if r['season'] == season]
    train = [r for s in (2021, 2022, 2023) for r in nfl[s]]
    grid = [round(0.70 + 0.02 * i, 2) for i in range(16)]
    s_best = min(grid, key=lambda s: c1.brier(train, s))
    out = {'label': 'EXPLORATORY; not a basis for a MODEL_CHANGE', 's_fitted_2021_2023': s_best,
           'train_brier_s': round(c1.brier(train, s_best), 5), 'train_brier_1': round(c1.brier(train, 1.0), 5)}
    for season in (2024, 2025):
        rows = nfl[season]
        out[str(season)] = {'brier_s': round(c1.brier(rows, s_best), 5), 'brier_1': round(c1.brier(rows, 1.0), 5),
                            'diff': round(c1.brier(rows, s_best) - c1.brier(rows, 1.0), 5),
                            'ci95': c1.boot_ci(rows, lambda xs: c1.brier(xs, s_best) - c1.brier(xs, 1.0))}
    print(json.dumps(out, indent=1))
    json.dump(out, open(os.path.join(HERE, 'c1_stage2_exploratory_results.json'), 'w'), indent=2)


if __name__ == '__main__':
    main()
