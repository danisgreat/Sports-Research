"""Prior NBL/WNBA seasons (early-season drift check) and EPL match summaries (1H goals, corners).
Summary payloads can carry odds/pickcenter keys: only boxscore team statistics, header competitors and
keyEvents/goal details are read by the analysis; nothing market-related is used."""
import json
import os

from fetch import espn_scoreboard, get_json

HERE = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    for label, path, s, e in [('NBL 2024-25', 'basketball/nbl', '20240918', '20250331'),
                              ('NBL 2023-24', 'basketball/nbl', '20230920', '20240331'),
                              ('WNBA 2025', 'basketball/wnba', '20250510', '20251020'),
                              ('WNBA 2024', 'basketball/wnba', '20240510', '20241020')]:
        d = espn_scoreboard(path, s, e)
        print(label, len(d['events']), 'failed', len(d['failed_days']), flush=True)
    evs = espn_scoreboard('soccer/eng.1', '20250815', '20260524')['events']
    rows = []
    for ev in evs:
        sm = get_json(f'https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/summary?event={ev["id"]}')
        teams = []
        for t in (sm.get('boxscore') or {}).get('teams', []):
            stats = {s_.get('name'): s_.get('displayValue') for s_ in t.get('statistics', [])}
            teams.append({'team': (t.get('team') or {}).get('id'), 'homeAway': t.get('homeAway'),
                          'wonCorners': stats.get('wonCorners'), 'totalShots': stats.get('totalShots'),
                          'shotsOnTarget': stats.get('shotsOnTarget'), 'yellowCards': stats.get('yellowCards'),
                          'redCards': stats.get('redCards'), 'foulsCommitted': stats.get('foulsCommitted')})
        goals = []
        for k in sm.get('keyEvents', []) or []:
            typ = (k.get('type') or {}).get('type') or (k.get('type') or {}).get('text')
            if k.get('scoringPlay'):
                goals.append({'clock': (k.get('clock') or {}).get('displayValue'),
                              'period': (k.get('period') or {}).get('number'), 'type': typ,
                              'team': (k.get('team') or {}).get('id')})
        rows.append({'id': ev['id'], 'date': ev['date'], 'teams': teams, 'goals': goals})
    with open(os.path.join(HERE, 'epl_summaries.json'), 'w', encoding='utf-8') as fh:
        json.dump(rows, fh)
    print('EPL summaries', len(rows))
