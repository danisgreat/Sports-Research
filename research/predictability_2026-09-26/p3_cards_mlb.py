"""P3 (MLB) — the cards' own probabilities against the models on the same contracts (preregistered, cc447c9).

Matching: each MLB card in the settled-row dataset is matched to one completed 2026 game. It must have the
card's away and home teams (event text), and a date inside 2026-09-01..2026-09-26. Ties are broken by the
probable starters' surnames appearing in the card's own text, then by the dates the card text names most
often. A card that still has two candidates is excluded and counted.

Contracts: full-game moneyline, ±1.5 run line and half-point totals only (integer totals, team totals, phase
rows and rows with no contract text are excluded and counted). Each row becomes one canonical binary event
('home_win', 'rl_home' = home wins by 2+, 'rl_away' = away wins by 2+, 'over_L'), and each (card, event) is
scored once.

Probabilities: card p (as issued), RM-1 q (tools/rank_model.py), A0, A1, A1S (tools/mlb_model.py, PRIORS
unchanged, probable starters' current-season lines before the date) and TB-1, all as of the game date
(games strictly before). Brier, card-cluster bootstrap (2,000). Writes p3_mlb_results.json.
"""
import csv
import json
import math
import os
import random
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, 'tools'))
import mlb_starters as ms  # noqa: E402
import mlb_model as mm  # noqa: E402
import team_baseline as tb  # noqa: E402
import rank_model as rmod  # noqa: E402
import sport_data as sd  # noqa: E402

LOGS = ['PREDICTION_LOG_COMBINED_3.md', 'PREDICTION_LOG_COMBINED_4.md', 'PREDICTION_LOG_COMBINED_5.md']


def card_texts(ids):
    out = defaultdict(str)
    for f in LOGS:
        lines = open(os.path.join(REPO, f), encoding='utf-8-sig').read().split('\n')
        for i, l in enumerate(lines):
            for c in ids:
                if re.search(r'\b' + c + r'\b', l):
                    out[c] += '\n'.join(lines[i:i + 80]) + '\n'
    return out


def canonical(contract, home, away):
    """(event, side_is_event) or (None, reason)."""
    c = contract.lower()
    if not c.strip():
        return None, 'no contract text'
    if re.search(r'team total|first|1st|f5|inning', c):
        return None, 'team total / phase'
    m = re.search(r'\b(over|under)\s+(\d+(?:\.\d+)?)', c)
    if m:
        L = float(m.group(2))
        if abs(L - round(L)) < 1e-9:
            return None, 'integer total (push-capable)'
        return (f'over_{L}', m.group(1) == 'over'), None
    team = None
    for name in (home, away):
        nick = name.split()[-1].lower()
        city = name.lower().rsplit(' ', 1)[0]
        abbr = {'Washington Nationals': 'wsh', 'San Diego Padres': 'sd', 'Toronto Blue Jays': 'blue jays',
                'Chicago White Sox': 'white sox', 'Boston Red Sox': 'red sox'}.get(name, '§')
        if nick in c or abbr in c or (city and city in c and len(city) > 4):
            team = name if team is None else 'BOTH'
    if team in (None, 'BOTH'):
        return None, 'side not identified'
    m = re.search(r'([+−–-])\s*1\.5', contract)
    if m:
        plus = m.group(1) == '+'
        if team == home:
            return (('rl_away', False) if plus else ('rl_home', True)), None
        return (('rl_home', False) if plus else ('rl_away', True)), None
    if re.search(r'\bml\b|moneyline|match winner|to win', c):
        return ('home_win', team == home), None
    return None, 'unsupported contract'


def main():
    rows = [r for r in csv.DictReader(open(os.path.join(REPO, 'research', 'settled_rows_2026-09-25', 'settled_rows.csv'),
                                           encoding='utf-8')) if r['sport'] == 'baseball-MLB' and r['p'] and r['result'] in ('W', 'L')]
    ids = sorted({r['card'] for r in rows})
    texts = card_texts(ids)
    games = ms.schedule(2026)
    pids = {g['hsp'] for g in games if g['hsp']} | {g['asp'] for g in games if g['asp']}
    logs = ms.game_logs(2026, pids)
    names = {}
    for pid in pids:
        d = ms.get(f'https://statsapi.mlb.com/api/v1/people/{pid}')
        names[pid] = (d.get('people') or [{}])[0].get('lastName', '')
    teams = sorted({g['home'] for g in games} | {g['away'] for g in games})
    excl = defaultdict(int)
    matched = {}
    for c in ids:
        ev = next(r['event'] for r in rows if r['card'] == c)
        m = re.search(r'([A-Za-z .]+?)\s*(?:\([^)]*\))?\s+@\s+([A-Za-z .]+?)(?:\s*\(|\s+—|$)', ev.replace('Baseball / MLB — ', '').replace('MLB — ', ''))
        if not m:
            excl['event text not parsed'] += 1
            continue
        try:
            away = sd.match_name(m.group(1).strip(), teams)
            home = sd.match_name(m.group(2).strip(), teams)
        except SystemExit:
            excl['team names not matched'] += 1
            continue
        cands = [g for g in games if g['home'] == home and g['away'] == away and '2026-09-01' <= g['date'] <= '2026-09-26']
        # identification only: a candidate must agree with every graded row of the card (a lost Under 10.5
        # means the game went to 11+). The settled results pick the game; they are not scored here.
        card_rows = [r for r in rows if r['card'] == c]

        def consistent(g):
            for r in card_rows:
                ce, _ = canonical(r['contract'], g['home'], g['away'])
                if ce is None:
                    continue
                event, same = ce
                happened = outcome(g, event)
                if (1 if r['result'] == 'W' else 0) != (happened if same else 1 - happened):
                    return False
            return True
        cands = [g for g in cands if consistent(g)]
        txt = texts.get(c, '')
        if len(cands) > 1:
            def score(g):
                s = sum(1 for pid in (g['hsp'], g['asp']) if pid and names.get(pid) and names[pid] in txt)
                return (s, txt.count(g['date']))
            cands.sort(key=score, reverse=True)
            if score(cands[0]) == score(cands[1]):
                excl['ambiguous game'] += 1
                continue
        if not cands:
            excl['no consistent game in window'] += 1
            continue
        matched[c] = cands[0]
    # model state per date
    by_date = defaultdict(list)
    for g in games:
        by_date[g['date']].append(g)
    need = {g['date'] for g in matched.values()}
    prior, states = [], {}
    tbs = tb.SeasonState(k=tb.LEAGUES['mlb']['k'], sd_total=4.5, sd_margin=4.57)
    for d in sorted(by_date):
        if d in need:
            states[d] = (mm.Ratings(list(prior)), list(prior), tb_snapshot(tbs))
        prior += by_date[d]
        for g in by_date[d]:
            tbs.add({'date': g['date'], 'home': g['home'], 'away': g['away'], 'hs': g['hr'], 'as': g['ar'], 'neutral': False})
    recs = []
    seen = set()
    for r in rows:
        c = r['card']
        if c not in matched:
            continue
        g = matched[c]
        ce, why = canonical(r['contract'], g['home'], g['away'])
        if ce is None:
            excl['row: ' + why] += 1
            continue
        event, same = ce
        if (c, event) in seen:
            continue
        seen.add((c, event))
        p = float(r['p'])
        y_row = 1 if r['result'] == 'W' else 0
        pc = p if same else 1 - p
        y = y_row if same else 1 - y_row
        q = rmod.score_row(rmod.load_coef(), 'mlb', r['contract'], p)['q']
        qc = q if same else 1 - q
        rt, pr, tbstate = states[g['date']]
        hsp = ms.starter_as_of(logs.get(g['hsp']), g['date']) if g['hsp'] else None
        asp = ms.starter_as_of(logs.get(g['asp']), g['date']) if g['asp'] else None
        out = {'card': c, 'event': event, 'y': y, 'card_p': pc, 'rm1_q': qc}
        for tag, (hs_, as_) in (('a1', (None, None)), ('a1s', (hsp, asp))):
            j, _, _ = rt.joint(g['home'], g['away'], g['venue'], hs_, as_)
            out[tag] = prob(j, event)
        out['a0'] = a0_prob(pr, event)
        out['tb1'] = tb1_prob(tbstate, g, event)
        recs.append(out)
    res = {'cards_matched': len(matched), 'cards_total': len(ids), 'exclusions': dict(excl), 'events': len(recs),
           'matches': {c: f"{g['date']} {g['away']} @ {g['home']} ({g['pk']})" for c, g in sorted(matched.items())}}
    res.update(compare(recs))
    json.dump({'summary': res, 'records': recs}, open(os.path.join(HERE, 'p3_mlb_results.json'), 'w'), indent=1)
    print(json.dumps(res, indent=1))


def outcome(g, event):
    if event == 'home_win':
        return 1 if g['hr'] > g['ar'] else 0
    if event == 'rl_home':
        return 1 if g['hr'] - g['ar'] >= 2 else 0
    if event == 'rl_away':
        return 1 if g['ar'] - g['hr'] >= 2 else 0
    return 1 if g['hr'] + g['ar'] > float(event.split('_')[1]) else 0


def tb_snapshot(st):
    import copy
    return copy.deepcopy(st)


def prob(j, event):
    if event == 'home_win':
        return mm.queries(j, None)['p_home_win']
    if event == 'rl_home':
        return math.fsum(v for (h, a), v in j.items() if h - a >= 2)
    if event == 'rl_away':
        return math.fsum(v for (h, a), v in j.items() if a - h >= 2)
    L = float(event.split('_')[1])
    return math.fsum(v for (h, a), v in j.items() if h + a > L)


def a0_prob(prior, event):
    n = len(prior)
    if event == 'home_win':
        return sum(x['hr'] > x['ar'] for x in prior) / n
    if event == 'rl_home':
        return sum(x['hr'] - x['ar'] >= 2 for x in prior) / n
    if event == 'rl_away':
        return sum(x['ar'] - x['hr'] >= 2 for x in prior) / n
    L = float(event.split('_')[1])
    return sum(x['hr'] + x['ar'] > L for x in prior) / n


def tb1_prob(st, g, event):
    pred = st.predict(g['home'], g['away'])
    sdm, sdt = st.resid_sd()
    if event == 'home_win':
        return tb.contract_probs('mlb', pred, sdm, sdt, None, None, state=st)['home_win']
    if event == 'rl_home':
        return tb.contract_probs('mlb', pred, sdm, sdt, None, -1.5, state=st)['home_-1.5']
    if event == 'rl_away':
        return 1 - tb.contract_probs('mlb', pred, sdm, sdt, None, 1.5, state=st)['home_+1.5']
    L = float(event.split('_')[1])
    return tb.contract_probs('mlb', pred, sdm, sdt, L, None, state=st)[f'over_{L:g}']


def compare(recs, boot=2000, seed=20260926):
    def brier(k, rs):
        return sum((r[k] - r['y']) ** 2 for r in rs) / len(rs)
    by_card = defaultdict(list)
    for r in recs:
        by_card[r['card']].append(r)
    cards = list(by_card)
    out = {'brier': {k: round(brier(k, recs), 4) for k in ('card_p', 'rm1_q', 'a0', 'a1', 'a1s', 'tb1')}}
    for r in recs:
        lp = lambda x: math.log(min(max(x, 1e-4), 1 - 1e-4) / (1 - min(max(x, 1e-4), 1 - 1e-4)))  # noqa: E731
        r['blend'] = 1 / (1 + math.exp(-(lp(r['card_p']) + lp(r['a1s'])) / 2))
    out['brier']['blend_card_a1s (exploratory)'] = round(brier('blend', recs), 4)
    rng = random.Random(seed)
    for other in ('a0', 'a1', 'a1s', 'tb1', 'rm1_q'):
        diffs = []
        for _ in range(boot):
            s = [r for c in (rng.choice(cards) for _ in cards) for r in by_card[c]]
            diffs.append(brier('card_p', s) - brier(other, s))
        diffs.sort()
        out[f'card_minus_{other}'] = {'mean': round(brier('card_p', recs) - brier(other, recs), 4),
                                      'ci95_card_cluster': [round(diffs[int(0.025 * boot)], 4), round(diffs[int(0.975 * boot) - 1], 4)]}
    by_ev = defaultdict(list)
    for r in recs:
        by_ev[r['event'].split('_')[0]].append(r)
    out['by_market'] = {k: {'n': len(v), **{m: round(brier(m, v), 4) for m in ('card_p', 'a0', 'a1s', 'tb1')}} for k, v in by_ev.items()}
    return out


if __name__ == '__main__':
    main()
