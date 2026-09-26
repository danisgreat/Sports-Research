"""P2 — coverage: validate the unchanged A1 models on NBL and NRL (preregistered, cc447c9).

Data: ESPN scoreboards cached by research/base_rates_2026-09-25 (retrieved 2026-09-25), read through that
folder's fetcher (cache hit only) and parsed with tools/sport_data.parse_espn_event, which reads no market
keys. Validation: tools/sport_models.validate_team with the constants as at 0e98a46, TB-1 alongside.
Writes p2_coverage_results.json.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
BR = os.path.join(REPO, 'research', 'base_rates_2026-09-25')
sys.path.insert(0, os.path.join(REPO, 'tools'))
sys.path.insert(0, BR)
import sport_data as sd  # noqa: E402
import sport_models as sm  # noqa: E402

os.chdir(BR)
from fetch import espn_scoreboard  # noqa: E402

SEASONS = {
    'nbl': [('basketball/nbl', '20230920', '20240331'), ('basketball/nbl', '20240918', '20250331'),
            ('basketball/nbl', '20250918', '20260331')],
    'nrl': [('rugby-league/3', '20250301', '20251005'), ('rugby-league/3', '20260226', '20260924')],
}
WINDOWS = {'nbl': [('2024-09-01', '2025-04-30'), ('2025-09-01', '2026-04-30')],
           'nrl': [('2026-03-01', '2026-09-24')]}


def games_for(league):
    seen, out = set(), []
    for path, s, e in SEASONS[league]:
        for ev in espn_scoreboard(path, s, e)['events']:
            g = sd.parse_espn_event(ev, 'points')
            if g and g['completed'] and g['hs'] is not None and g['id'] not in seen:
                seen.add(g['id'])
                out.append(g)
    return sorted(out, key=lambda g: g['date'])


def main():
    res = {}
    for lg in ('nbl', 'nrl'):
        games = games_for(lg)
        cfg = sm.config(lg)
        for a, b in WINDOWS[lg]:
            r = sm.validate_team(cfg, games, a, b, tb1_league=lg)
            res[f'{lg} {a}..{b}'] = r
            print(lg, a, b, json.dumps({k: r[k] for k in r if k not in ('rows',)})[:1500], flush=True)
        res[f'{lg} games'] = len(games)
    json.dump(res, open(os.path.join(HERE, 'p2_coverage_results.json'), 'w'), indent=2, default=str)


if __name__ == '__main__':
    main()
