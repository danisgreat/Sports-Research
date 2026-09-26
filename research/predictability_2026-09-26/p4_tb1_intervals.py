"""P4 input — week-block 95% intervals for TB-1 against its running base rate (the population A0).

research/team_baseline_2026-09-25e reported TB-1's latest-season Brier as point estimates only. The anchor rule
(PREREGISTRATION.md P4) needs "beat A0 with a 95% interval below 0". This re-runs that validation's own
evaluate() unchanged (same k and r per league) and bootstraps ISO-week blocks of the per-game difference.
Writes p4_tb1_intervals.json.
"""
import datetime as dt
import json
import os
import random
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'research', 'team_baseline_2026-09-25e'))
cwd = os.getcwd()
import validate_team_baseline as vtb  # noqa: E402  (chdirs into the base-rate folder)

PARAMS = {'NBL': (5, 0.0), 'WNBA': (2, 0.75), 'NBA': (0, 0.0), 'NHL': (20, 0.0), 'EPL': (2, 0.0),
          'NFL': (2, 0.0), 'AFL': (0, 0.0), 'NRL': (2, 0.0), 'MLB': (20, 0.0)}


def boot(rows, a, b, n=2000, seed=20260926):
    blocks = defaultdict(list)
    for r in rows:
        blocks[r['week']].append((r[a] - r[b]))
    keys = list(blocks)
    tot = sum(len(v) for v in blocks.values())
    mean = sum(sum(v) for v in blocks.values()) / tot
    rng = random.Random(seed)
    st = []
    for _ in range(n):
        s = [blocks[rng.choice(keys)] for _ in keys]
        st.append(sum(sum(v) for v in s) / sum(len(v) for v in s))
    st.sort()
    return {'mean': round(mean, 5), 'ci95': [round(st[int(0.025 * n)], 5), round(st[int(0.975 * n) - 1], 5)], 'n': tot}


def main():
    out = {}
    leagues = {lg: vtb.load_chain(lg) for lg in vtb.CHAINS}
    leagues['MLB'] = vtb.load_mlb()
    for lg, seasons in leagues.items():
        k, r = PARAMS[lg]
        per = vtb.run_chain(seasons, k, r, vtb.KIND[lg])
        latest_games = sorted(seasons[-1], key=lambda x: x['date'])
        # evaluate() appends rows in date order for eligible games; recover each row's week from the game list
        rows = per[-1]
        state = vtb.tb.SeasonState(prior=None, k=k, carry=r)
        weeks = []
        for g in latest_games:
            if min(state.n_games(g['home']), state.n_games(g['away'])) >= 1 and state.n_league_games() >= 10:
                weeks.append(dt.date.fromisoformat(g['date'][:10]).isocalendar()[:2])
            state.add(g)
        if len(weeks) != len(rows):   # carry-over seasons change nothing in eligibility; guard anyway
            weeks = weeks[:len(rows)] + [None] * (len(rows) - len(weeks))
        for row, w in zip(rows, weeks):
            row['week'] = str(w)
            row['bh'] = (row['p_home'] - row['y_home']) ** 2
            row['b0h'] = (row['base_home'] - row['y_home']) ** 2
            row['bo'] = (row['p_over'] - row['y_over']) ** 2
            row['b0o'] = (row['base_over'] - row['y_over']) ** 2
        out[lg] = {'season': vtb.CHAINS.get(lg, ['MLB 2026'])[-1], 'k': k, 'carry_r': r,
                   'home_win_TB1_minus_base': boot(rows, 'bh', 'b0h'),
                   'total_over_mean_TB1_minus_base': boot(rows, 'bo', 'b0o')}
        print(lg, json.dumps(out[lg]), flush=True)
    json.dump(out, open(os.path.join(HERE, 'p4_tb1_intervals.json'), 'w'), indent=2)


if __name__ == '__main__':
    main()
