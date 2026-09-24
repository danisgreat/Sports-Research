"""Pull NHL api-web daily score pages (curl; urllib gets 403) and ESPN tennis scoreboards.

Market-blind: the NHL score payload carries an `oddsPartners` key and ESPN events can carry odds;
neither is read or stored beyond the raw cache, and no analysis script touches them.
"""
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import time

from fetch import CACHE, get_json


def curl_json(url):
    key = hashlib.sha1(url.encode()).hexdigest()
    path = os.path.join(CACHE, key + '.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as fh:
            return json.load(fh)
    for i in range(3):
        r = subprocess.run(['curl', '-s', '--compressed', '-m', '60', url], capture_output=True)
        try:
            data = json.loads(r.stdout.decode('utf-8'))
            with open(path, 'w', encoding='utf-8') as fh:
                json.dump(data, fh)
            time.sleep(0.15)
            return data
        except Exception:  # noqa: BLE001
            time.sleep(2 * (i + 1))
    raise RuntimeError('curl failed ' + url)


def nhl_season(start, end):
    s = dt.date.fromisoformat(start)
    e = dt.date.fromisoformat(end)
    games = {}
    while s <= e:
        d = curl_json(f'https://api-web.nhle.com/v1/score/{s:%Y-%m-%d}')
        for g in d.get('games', []):
            games[g['id']] = {k: g.get(k) for k in ('id', 'season', 'gameType', 'gameDate', 'gameState',
                                                      'awayTeam', 'homeTeam', 'periodDescriptor',
                                                      'gameOutcome', 'goals', 'venue', 'neutralSite')}
        s += dt.timedelta(days=1)
    return games


def tennis_season(tour, start, end, step_days=3):
    s = dt.date.fromisoformat(start)
    e = dt.date.fromisoformat(end)
    comps = {}
    while s <= e:
        d = get_json(f'https://site.api.espn.com/apis/site/v2/sports/tennis/{tour}/scoreboard?dates={s:%Y%m%d}')
        for ev in d.get('events', []):
            for grp in ev.get('groupings', []):
                gname = grp.get('grouping', {}).get('displayName')
                for c in grp.get('competitions', []):
                    comps[c['id']] = {
                        'tournament': ev.get('name'), 'tournament_id': ev.get('id'), 'major': ev.get('major'),
                        'grouping': gname, 'date': c.get('date'), 'status': c.get('status', {}).get('type', {}),
                        'format': c.get('format'), 'notes': c.get('notes'), 'round': c.get('round'),
                        'type': c.get('type'), 'venue': c.get('venue'),
                        'competitors': [{'name': cp.get('athlete', {}).get('displayName'), 'winner': cp.get('winner'),
                                         'linescores': cp.get('linescores', [])} for cp in c.get('competitors', [])],
                    }
        s += dt.timedelta(days=step_days)
    return comps


if __name__ == '__main__':
    what = sys.argv[1]
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{what}.json')
    if what == 'nhl':
        data = nhl_season('2025-10-07', '2026-06-20')
    elif what == 'wta':
        data = tennis_season('wta', '2026-01-01', '2026-09-24')
    elif what == 'atp':
        data = tennis_season('atp', '2026-01-01', '2026-09-24')
    with open(out, 'w', encoding='utf-8') as fh:
        json.dump(data, fh)
    print(what, len(data))
