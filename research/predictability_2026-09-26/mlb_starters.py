"""P1 — does the declared MLB starter term add skill? (preregistered in PREREGISTRATION.md, cc447c9)

Data (statsapi, cached in ./cache, git-ignored):
- schedule?sportId=1&gameType=R&hydrate=probablePitcher,linescore,venue for 2025 and 2026. The pre-game
  `probablePitcher` stays on completed games.
- people/{id}/stats?stats=gameLog&group=pitching&season=Y for every probable starter.

Models: A0 and A1 exactly as tools/mlb_model.py (PRIORS unchanged); A1S = A1 + the declared starter term, with
each starter's current-season lines dated strictly before the game; TB-1 (tools/team_baseline.py, k 20).
Rolling origin as mlb_model.validate (games strictly before the date; >= 300 prior games in the season).

Usage: python mlb_starters.py [--seasons 2025 2026]
Writes mlb_starters_results.json. Market-blind: statsapi schedule/people endpoints only.
"""
import argparse
import concurrent.futures as cf
import gzip
import hashlib
import json
import math
import os
import random
import sys
import time
import urllib.request
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools'))
import mlb_model as mm  # noqa: E402
import team_baseline as tb  # noqa: E402

CACHE = os.path.join(HERE, 'cache')
SCHED = ('https://statsapi.mlb.com/api/v1/schedule?sportId=1&gameType=R&startDate={s}&endDate={e}'
         '&hydrate=probablePitcher,linescore,venue')
GLOG = 'https://statsapi.mlb.com/api/v1/people/{pid}/stats?stats=gameLog&group=pitching&season={y}'
END = {2025: '2025-10-01', 2026: '2026-09-24'}
LINES = (7.5, 8.5, 9.5)


def get(url):
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest() + '.json')
    if os.path.exists(p):
        return json.load(open(p, encoding='utf-8'))
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip'})
            raw = urllib.request.urlopen(req, timeout=90).read()
            if raw[:2] == b'\x1f\x8b':
                raw = gzip.decompress(raw)
            d = json.loads(raw.decode('utf-8'))
            json.dump(d, open(p, 'w', encoding='utf-8'))
            return d
        except Exception:  # noqa: BLE001
            time.sleep(2 * (i + 1))
    raise RuntimeError(url)


def schedule(season):
    d = get(SCHED.format(s=f'{season}-03-01', e=END[season]))
    games = []
    for day in d['dates']:
        for g in day['games']:
            st = g['status']
            if st.get('abstractGameState') != 'Final' or st.get('detailedState') in ('Postponed', 'Cancelled'):
                continue
            h, a = g['teams']['home'], g['teams']['away']
            if 'score' not in h or 'score' not in a:
                continue
            games.append({'pk': g['gamePk'], 'date': g.get('officialDate') or day['date'],
                          'home': h['team']['name'], 'away': a['team']['name'],
                          'venue': (g.get('venue') or {}).get('id'), 'hr': int(h['score']), 'ar': int(a['score']),
                          'hsp': (h.get('probablePitcher') or {}).get('id'),
                          'asp': (a.get('probablePitcher') or {}).get('id')})
    games.sort(key=lambda x: (x['date'], x['pk']))
    return games


def game_logs(season, pids):
    out = {}

    def one(pid):
        d = get(GLOG.format(pid=pid, y=season))
        rows = []
        for blk in d.get('stats', []):
            for s in blk.get('splits', []):
                st = s.get('stat', {})
                rows.append({'date': s.get('date'), 'ip': mm.ip_to_float(st.get('inningsPitched', 0)),
                             'r': float(st.get('runs', st.get('earnedRuns', 0)) or 0),
                             'hr': float(st.get('homeRuns', 0) or 0), 'bb': float(st.get('baseOnBalls', 0) or 0),
                             'hbp': float(st.get('hitByPitch', 0) or 0), 'k': float(st.get('strikeOuts', 0) or 0),
                             'gs': float(st.get('gamesStarted', 0) or 0)})
        return pid, rows
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for pid, rows in ex.map(one, sorted(pids)):
            out[pid] = rows
    return out


def starter_as_of(rows, date):
    """The pitcher's current-season line from appearances dated strictly before `date` (None if no innings)."""
    agg = defaultdict(float)
    for r in rows or []:
        if r['date'] and r['date'] < date:
            for k in ('ip', 'r', 'hr', 'bb', 'hbp', 'k', 'gs'):
                agg[k] += r[k]
    return dict(agg) if agg.get('ip', 0) > 0 else None


def scores(joint, g):
    y = 1 if g['hr'] > g['ar'] else 0
    t = g['hr'] + g['ar']
    q = mm.queries(joint, None)['p_home_win']
    q = min(max(q, 1e-6), 1 - 1e-6)
    out = {'win_brier': (q - y) ** 2, 'win_ll': -(y * math.log(q) + (1 - y) * math.log(1 - q))}
    for L in LINES:
        p = math.fsum(v for (h, a), v in joint.items() if h + a > L)
        out[f'over_{L}'] = (p - (t > L)) ** 2
    p_rl = math.fsum(v for (h, a), v in joint.items() if h - a >= 2)
    out['rl_home_-1.5'] = (p_rl - (g['hr'] - g['ar'] >= 2)) ** 2
    return out


def composite(s):
    return (s['win_brier'] + sum(s[f'over_{L}'] for L in LINES) + s['rl_home_-1.5']) / 5


def boot(per_day, key_a, key_b, n=2000, seed=20260926):
    rng = random.Random(seed)
    tot = sum(d['n'] for d in per_day)
    mean = sum(d[key_a] - d[key_b] for d in per_day) / tot
    st = []
    for _ in range(n):
        s = [rng.choice(per_day) for _ in per_day]
        st.append(sum(d[key_a] - d[key_b] for d in s) / sum(d['n'] for d in s))
    st.sort()
    return {'mean': round(mean, 5), 'ci95': [round(st[int(0.025 * n)], 5), round(st[int(0.975 * n) - 1], 5)]}


def run(season):
    games = schedule(season)
    pids = {g['hsp'] for g in games if g['hsp']} | {g['asp'] for g in games if g['asp']}
    logs = game_logs(season, pids)
    by_date = defaultdict(list)
    for g in games:
        by_date[g['date']].append(g)
    prior, per_day = [], []
    tbs = tb.SeasonState(k=tb.LEAGUES['mlb']['k'], sd_total=4.5, sd_margin=4.57)
    coverage = {'games': 0, 'both_starters': 0}
    for d in sorted(by_date):
        if len(prior) >= 300:
            rt = mm.Ratings(prior)
            a0w = sum(x['hr'] > x['ar'] for x in prior) / len(prior)
            a0o = {L: sum(x['hr'] + x['ar'] > L for x in prior) / len(prior) for L in LINES}
            a0rl = sum(x['hr'] - x['ar'] >= 2 for x in prior) / len(prior)
            day = defaultdict(float)
            for g in by_date[d]:
                y = 1 if g['hr'] > g['ar'] else 0
                t = g['hr'] + g['ar']
                j1, _, _ = rt.joint(g['home'], g['away'], g['venue'])
                hsp = starter_as_of(logs.get(g['hsp']), d) if g['hsp'] else None
                asp = starter_as_of(logs.get(g['asp']), d) if g['asp'] else None
                j2, _, _ = rt.joint(g['home'], g['away'], g['venue'], hsp, asp)
                s1, s2 = scores(j1, g), scores(j2, g)
                q0 = min(max(a0w, 1e-6), 1 - 1e-6)
                s0 = {'win_brier': (a0w - y) ** 2, 'win_ll': -(y * math.log(q0) + (1 - y) * math.log(1 - q0)),
                      'rl_home_-1.5': (a0rl - (g['hr'] - g['ar'] >= 2)) ** 2}
                for L in LINES:
                    s0[f'over_{L}'] = (a0o[L] - (t > L)) ** 2
                # TB-1
                pred = tbs.predict(g['home'], g['away'])
                sdm, sdt = tbs.resid_sd()
                pr = tb.contract_probs('mlb', pred, sdm, sdt, None, -1.5, state=tbs)
                qt = min(max(pr['home_win'], 1e-6), 1 - 1e-6)
                stb = {'win_brier': (pr['home_win'] - y) ** 2, 'win_ll': -(y * math.log(qt) + (1 - y) * math.log(1 - qt)),
                       'rl_home_-1.5': (pr['home_-1.5'] - (g['hr'] - g['ar'] >= 2)) ** 2}
                for L in LINES:
                    stb[f'over_{L}'] = (tb.contract_probs('mlb', pred, sdm, sdt, L, None, state=tbs)[f'over_{L:g}'] - (t > L)) ** 2
                day['n'] += 1
                coverage['games'] += 1
                coverage['both_starters'] += bool(hsp and asp)
                for tag, s in (('a0', s0), ('a1', s1), ('a1s', s2), ('tb1', stb)):
                    day[tag + '_ll'] += s['win_ll']
                    day[tag + '_wb'] += s['win_brier']
                    day[tag + '_comp'] += composite(s)
                    for k in s:
                        day[tag + ':' + k] += s[k]
            day['date'] = d
            per_day.append(dict(day))
        prior += by_date[d]
        for g in by_date[d]:
            tbs.add({'date': g['date'], 'home': g['home'], 'away': g['away'], 'hs': g['hr'], 'as': g['ar'], 'neutral': False})
    n = sum(x['n'] for x in per_day)
    res = {'season': season, 'games_scored': n, 'days': len(per_day), 'coverage': coverage,
           'model_version': mm.MODEL_VERSION, 'params_sha': mm.params_sha()}
    for tag in ('a0', 'a1', 'a1s', 'tb1'):
        res[tag] = {k.split(':', 1)[1]: round(sum(x.get(k, 0) for x in per_day) / n, 5)
                    for k in per_day[0] if k.startswith(tag + ':')}
    res['primary_A1S_minus_A1_win_logloss'] = boot(per_day, 'a1s_ll', 'a1_ll')
    res['secondary_A1S_minus_A1_composite_brier'] = boot(per_day, 'a1s_comp', 'a1_comp')
    res['A1S_minus_A0_win_logloss'] = boot(per_day, 'a1s_ll', 'a0_ll')
    res['A1S_minus_A0_composite_brier'] = boot(per_day, 'a1s_comp', 'a0_comp')
    res['A1S_minus_TB1_win_logloss'] = boot(per_day, 'a1s_ll', 'tb1_ll')
    res['A1S_minus_TB1_composite_brier'] = boot(per_day, 'a1s_comp', 'tb1_comp')
    res['A1_minus_A0_win_logloss'] = boot(per_day, 'a1_ll', 'a0_ll')
    # Brier-scale intervals for the anchor registry (tools/model_anchor.py EVIDENCE is on Brier)
    res['A1_minus_A0_win_brier'] = boot(per_day, 'a1_wb', 'a0_wb')
    res['A1_minus_TB1_win_brier'] = boot(per_day, 'a1_wb', 'tb1_wb')
    res['TB1_minus_A0_win_brier'] = boot(per_day, 'tb1_wb', 'a0_wb')
    for tag in ('a1', 'a1s', 'tb1'):
        for L in LINES:
            res[f'{tag.upper()}_minus_A0_over_{L}_brier'] = boot(per_day, f'{tag}:over_{L}', f'a0:over_{L}')
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seasons', nargs='*', type=int, default=[2025, 2026])
    a = ap.parse_args()
    out = {}
    for s in a.seasons:
        out[str(s)] = run(s)
        print(json.dumps(out[str(s)], indent=1), flush=True)
    path = os.path.join(HERE, 'mlb_starters_results.json')
    prev = json.load(open(path)) if os.path.exists(path) else {}
    prev.update(out)
    json.dump(prev, open(path, 'w'), indent=2)


if __name__ == '__main__':
    main()
