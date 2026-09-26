"""P3 (other leagues) — card p against A0/A1/TB-1 on the same contracts (preregistered, cc447c9).

Leagues: WNBA, NBL, NFL, AFL, NRL, EPL. The only NHL card (P-503) was a preseason game, and A1 is a
regular-season model, so it is excluded and counted.

Matching: the card's two teams (event text) against ESPN results dated 2025-03-01..2026-09-26 (in-season
ranges in SEASON_RANGES). A candidate
game must agree with every graded row on the card; this uses the settled results only to identify the game.
Two or more consistent candidates means the card is excluded.

Forecasts: tools/sport_models.TeamEngine.replay over the game's own date, the same leak-free code path as
`validate` (fit on games strictly before the date). Contracts: full-game winner, ±k.5 handicaps and
half-point totals; soccer adds the first-half total. Everything else is excluded and counted.

The ESPN day cache of research/base_rates_2026-09-25 seeds .cache/sport_models (the same URL hashes), with
market keys stripped by tools/sport_data._strip. Missing days are fetched. Writes p3_other_results.json.
"""
import csv
import datetime as dt
import glob
import hashlib
import json
import math
import os
import random
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools'))
import sport_data as sd  # noqa: E402
import sport_models as sm  # noqa: E402

LEAGUE_OF = [('wnba', r'\bWNBA\b'), ('nbl', r'\bNBL\b'), ('nfl', r'\bNFL\b'), ('afl', r'\bAFL\b(?!W)'),
             ('nrl', r'\bNRL\b(?!W)'), ('epl', r'Premier League|\bEPL\b'), ('nhl', r'\bNHL\b')]
BR_CACHE = os.path.join(REPO, 'research', 'base_rates_2026-09-25', 'cache')
WIN = ('2025-03-01', '2026-09-26')
# In-season ranges (history for the model window plus the cards' dates). Off-season dates hold no games, and
# fetching them one by one made the first run impractically slow.
SEASON_RANGES = {
    'wnba': [('2024-05-01', '2024-10-20'), ('2025-05-10', '2025-10-20'), ('2026-05-01', '2026-09-26')],
    'nbl': [('2024-09-18', '2025-03-31'), ('2025-09-18', '2026-03-31'), ('2026-09-01', '2026-09-26')],
    'nfl': [('2024-09-05', '2025-02-10'), ('2025-09-04', '2026-02-09'), ('2026-09-01', '2026-09-26')],
    'afl': [('2025-03-06', '2025-09-27'), ('2026-03-05', '2026-09-26')],
    'nrl': [('2025-03-01', '2025-10-05'), ('2026-02-26', '2026-09-26')],
    'epl': [('2025-08-15', '2026-05-24'), ('2026-08-01', '2026-09-26')],
}


def seed_cache():
    os.makedirs(sd.CACHE, exist_ok=True)
    n = 0
    for p in glob.glob(os.path.join(BR_CACHE, '*.json')):
        dst = os.path.join(sd.CACHE, os.path.basename(p))
        if os.path.exists(dst):
            continue
        try:
            data = json.load(open(p, encoding='utf-8'))
        except ValueError:
            continue
        if not isinstance(data, dict) or 'events' not in data:
            continue
        json.dump(sd._strip(data), open(dst, 'w', encoding='utf-8'))
        n += 1
    return n


def card_texts(ids):
    out = defaultdict(str)
    files = ['PREDICTION_LOG_COMBINED.md', 'PREDICTION_LOG_COMBINED_2.md', 'PREDICTION_LOG_COMBINED_3.md',
             'PREDICTION_LOG_COMBINED_4.md', 'PREDICTION_LOG_COMBINED_5.md']
    for f in files:
        lines = open(os.path.join(REPO, f), encoding='utf-8-sig').read().split('\n')
        for i, l in enumerate(lines):
            for c in ids:
                if re.search(r'\b' + c + r'\b', l):
                    out[c] += '\n'.join(lines[i:i + 60]) + '\n'
    return out


def norm_words(s):
    return set(sd.norm(s).split())


def name_contains(name, team):
    a, b = sd.norm(name), sd.norm(team)
    return bool(a) and bool(b) and (a in b or b in a)


def name_hits(name, team):
    a, b = sd.norm(name), sd.norm(team)
    return bool(a) and (a in b or b in a or (norm_words(name) & norm_words(team)) - {'fc', 'city', 'united', 'the'})


def canonical(contract, home, away, league):
    c = contract.lower()
    if not c.strip():
        return None, 'no contract text'
    half = bool(re.search(r'1st half|first half|\b1h\b', c))
    if re.search(r'team total|corner|card|double chance|\b1x\b|\bx2\b|or draw|quarter|\bq[1-4]\b|btts|both teams', c):
        return None, 'unsupported market'
    m = re.search(r'\b(over|under)\s+(\d+(?:\.\d+)?)', c)
    if m:
        L = float(m.group(2))
        if abs(L - round(L)) < 1e-9:
            return None, 'integer total (push-capable)'
        if half and league != 'epl':
            return None, 'phase outside soccer'
        return ((('h1_over_' if half else 'over_') + str(L)), m.group(1) == 'over'), None
    if half:
        return None, 'phase outside soccer'
    side = [t for t in (home, away) if name_hits(re.split(r'\s[+−–-]\d|\sml\b|\smatch|\sto win', contract, flags=re.I)[0], t)]
    if len(side) != 1:
        return None, 'side not identified'
    team = side[0]
    m = re.search(r'([+−–-])\s*(\d+\.5)', contract)
    if m:
        k = float(m.group(2)) * (1 if m.group(1) == '+' else -1)
        if team == home:
            return (f'home_cover_{k:+g}', True), None
        return (f'home_cover_{-k:+g}', False), None
    if re.search(r'\bml\b|moneyline|match winner|to win|\bwinner\b', c):
        if league == 'epl':
            return ('home_win' if team == home else 'away_win', True), None
        return ('home_win', team == home), None
    return None, 'unsupported contract'


def outcome(g, event):
    hs, as_ = g['hs'], g['as']
    if event == 'home_win':
        return int(hs > as_)
    if event == 'away_win':
        return int(as_ > hs)
    if event.startswith('home_cover_'):
        return int(hs - as_ + float(event.split('_')[-1]) > 0)
    if event.startswith('h1_over_'):
        if g.get('hs_ht') is None:
            return None
        return int(g['hs_ht'] + g['as_ht'] > float(event.split('_')[-1]))
    return int(hs + as_ > float(event.split('_')[-1]))


def prob(fc, event):
    if event == 'home_win':
        return fc.probs()['p_home_win']
    if event == 'away_win':
        return fc.probs()['p_away_win']
    if event.startswith('home_cover_'):
        return fc.probs(line=float(event.split('_')[-1]))['p_home_cover']
    if event.startswith('h1_over_'):
        sub = fc.extra.get('h1')
        return sm.p_gt(sub.total, float(event.split('_')[-1])) if sub else None
    return sm.p_gt(fc.total, float(event.split('_')[-1]))


def main():
    print('seeded', seed_cache(), 'cached days', flush=True)
    rows = [r for r in csv.DictReader(open(os.path.join(REPO, 'research', 'settled_rows_2026-09-25', 'settled_rows.csv'),
                                           encoding='utf-8')) if r['p'] and r['result'] in ('W', 'L')]
    by_league = defaultdict(lambda: defaultdict(list))
    for r in rows:
        for lg, pat in LEAGUE_OF:
            if re.search(pat, r['event']):
                by_league[lg][r['card']].append(r)
                break
    excl = defaultdict(int)
    recs, matches = [], {}
    texts = card_texts({c for lg in by_league.values() for c in lg})
    for lg, cards in by_league.items():
        if lg == 'nhl':
            excl['nhl preseason card (A1 is a regular-season model)'] += len(cards)
            continue
        cfg = sm.config(lg)
        seen_ids, games = set(), []
        for a_, b_ in SEASON_RANGES[lg]:   # in-season days only: off-season dates carry no games
            for g_ in sd.espn_results(cfg['espn'], a_, b_, cfg['family']):
                if g_['id'] not in seen_ids:
                    seen_ids.add(g_['id'])
                    games.append(g_)
        games.sort(key=lambda g_: g_['date'])
        print(lg, len(games), 'games', flush=True)
        for c, crs in cards.items():
            # the matchup is the ' — '-separated segment that contains 'vs', 'v' or '@'
            segs = [x for x in re.split(r'\s+—\s+', crs[0]['event']) if re.search(r'\s(?:vs\.?|v|@)\s', x)]
            ev = re.sub(r'\s*[(,].*$', '', segs[0]) if segs else ''
            parts = re.split(r'\s+(?:vs\.?|v|@)\s+', ev)
            if len(parts) < 2:
                excl['event text not parsed'] += 1
                continue
            a, b = parts[0].strip(), parts[1].strip()
            # strict containment first ("Adelaide Crows" must not match "Port Adelaide"); word overlap only as a fallback
            cands = []
            for hit in (name_contains, name_hits):
                cands = [g for g in games if WIN[0] <= g['date'][:10] <= WIN[1] and
                         ((hit(a, g['home']) and hit(b, g['away'])) or (hit(a, g['away']) and hit(b, g['home'])))]
                if cands:
                    break

            def consistent(g):
                for r in crs:
                    ce, _ = canonical(r['contract'], g['home'], g['away'], lg)
                    if ce is None:
                        continue
                    o = outcome(g, ce[0])
                    if o is None:
                        continue
                    if (1 if r['result'] == 'W' else 0) != (o if ce[1] else 1 - o):
                        return False
                return True
            cands = [g for g in cands if consistent(g)]
            if len(cands) > 1:   # tie-break: the dates the card's own text names (venue date, ±1 day for AEST)
                txt = texts.get(c, '')

                def dscore(g):
                    d0 = dt.date.fromisoformat(g['date'][:10])
                    return sum(txt.count(d.isoformat()) + txt.count(f"{d.day} Sep") + txt.count(f"{d.day} September")
                               for d in (d0 - dt.timedelta(days=1), d0, d0 + dt.timedelta(days=1)))
                cands.sort(key=dscore, reverse=True)
                if dscore(cands[0]) == dscore(cands[1]):
                    excl['no unique consistent game'] += 1
                    continue
                cands = cands[:1]
            if len(cands) != 1:
                excl['no consistent game (not this league, or outside the window)'] += 1
                continue
            g = cands[0]
            matches[c] = f"{lg} {g['date'][:10]} {g['away']} @ {g['home']} ({g['id']})"
            eng = sm.TeamEngine(cfg, [x for x in games if x['date'][:10] <= g['date'][:10]])
            warm = (dt.date.fromisoformat(g['date'][:10]) - dt.timedelta(days=cfg.get('resid_days') or 0)).isoformat()
            f0 = f1 = None
            for item in eng.replay(g['date'][:10], g['date'][:10], warm_from=warm):
                if item[0]['id'] == g['id']:
                    f0, f1 = item[1], item[2]
            if f1 is None:
                excl['model could not forecast'] += 1
                continue
            tb1 = sm.tb1_scores(lg, [x for x in games if x['date'][:10] <= g['date'][:10]], None) if False else None
            seen = set()
            for r in crs:
                ce, why = canonical(r['contract'], g['home'], g['away'], lg)
                if ce is None:
                    excl['row: ' + why] += 1
                    continue
                event, same = ce
                if event in seen:
                    continue
                y = outcome(g, event)
                p0, p1 = prob(f0, event), prob(f1, event)
                if y is None or p1 is None or p0 is None:
                    excl['row: outcome or model probability unavailable'] += 1
                    continue
                seen.add(event)
                p = float(r['p'])
                recs.append({'league': lg, 'card': c, 'event': event, 'y': y,
                             'card_p': p if same else 1 - p, 'a0': p0, 'a1': p1})
    res = {'cards_matched': len(matches), 'events': len(recs), 'exclusions': dict(excl), 'matches': matches}
    res.update(compare(recs))
    json.dump({'summary': res, 'records': recs}, open(os.path.join(HERE, 'p3_other_results.json'), 'w'), indent=1)
    print(json.dumps(res, indent=1))


def compare(recs, boot=2000, seed=20260926):
    if not recs:
        return {}

    def brier(k, rs):
        return sum((r[k] - r['y']) ** 2 for r in rs) / len(rs)
    by_card = defaultdict(list)
    for r in recs:
        by_card[r['card']].append(r)
    cards = list(by_card)
    out = {'brier': {k: round(brier(k, recs), 4) for k in ('card_p', 'a0', 'a1')}}
    rng = random.Random(seed)
    for other in ('a0', 'a1'):
        d = []
        for _ in range(boot):
            s = [r for c in (rng.choice(cards) for _ in cards) for r in by_card[c]]
            d.append(brier('card_p', s) - brier(other, s))
        d.sort()
        out[f'card_minus_{other}'] = {'mean': round(brier('card_p', recs) - brier(other, recs), 4),
                                      'ci95_card_cluster': [round(d[int(0.025 * boot)], 4), round(d[int(0.975 * boot) - 1], 4)]}
    by_lg = defaultdict(list)
    for r in recs:
        by_lg[r['league']].append(r)
    out['by_league'] = {k: {'n': len(v), 'cards': len({r['card'] for r in v}),
                            **{m: round(brier(m, v), 4) for m in ('card_p', 'a0', 'a1')}} for k, v in by_lg.items()}
    return out


if __name__ == '__main__':
    main()
