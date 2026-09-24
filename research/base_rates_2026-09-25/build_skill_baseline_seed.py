"""Build the seed rows of SKILL_BASELINE_LEDGER.md (2026-09-25(c)).

For each issued decision of the 2026-09-24 cohort whose competition has a population reference,
compute a leak-free population baseline probability: only games completed before the event's
start are used.
- Totals: the population P(total over/under the line).
- Moneylines and handicaps: the home/away margin distribution. Venue is known before the game,
  so this is fair pregame information.
- Tennis: no side information exists in the population, so a player's −k.5 baseline is
  0.5 × P(winner margin ≥ k+1) and the winner baseline is 0.5.

The card rows are copied from the issued Field 4 tables (C-SUMMARY-FROM-CARD). Exact
complements of a forced pair are counted once, as the higher-ranked row. A winner call is
included only when it is not already a ranked moneyline row.
Run from this folder: python build_skill_baseline_seed.py > seed_rows.md
"""
import datetime as dt
import json

import analyze_mlb as am
from analyze_leagues import load
import analyze_leagues as al
from fetch import espn_scoreboard

al.SPEC.update({
    'NBL 2025-26': ('basketball/nbl', '20250918', '20260331', 'bk'),
    'NBL 2026-27': ('basketball/nbl', '20260915', '20260924', 'bk'),
    'WNBA 2026': ('basketball/wnba', '20260501', '20260924', 'bk'),
})


def ts(s):
    s = s.replace('Z', '+00:00')
    if len(s) == 22:  # 2026-09-24T00:00+00:00
        s = s[:16] + ':00' + s[16:]
    return dt.datetime.fromisoformat(s)


def frac(n, d):
    return (n / d) if d else float('nan')


# ---------------------------------------------------------------- populations
MLB = am.games()


def mlb_prior(start):
    return [g for g in MLB if ts(g['date']) < start]


NHL_PRE = [g for g in json.load(open('nhl_pre.json', encoding='utf-8')).values()
           if g['gameType'] == 1 and g['gameState'] in ('OFF', 'FINAL')]


def nhl_prior(local_date):
    return [{'hs': g['homeTeam']['score'], 'as': g['awayTeam']['score']} for g in NHL_PRE if g['gameDate'] < local_date]


def espn_prior(labels, start):
    out = []
    for lab in labels:
        games, _, _ = load(lab)
        out += [g for g in games if ts(g['date']) < start]
    return out


TEN = {}
for tour in ('wta', 'atp'):
    TEN.update(json.load(open(tour + '.json', encoding='utf-8')))


def wta_prior(start):
    import analyze_tennis as at
    rows = []
    for cid, c in TEN.items():
        if c['grouping'] != "Women's Singles" or (c['status'] or {}).get('name') != 'STATUS_FINAL':
            continue
        if ts(c['date']) >= start:
            continue
        a = [x.get('value') for x in c['competitors'][0]['linescores']]
        b = [x.get('value') for x in c['competitors'][1]['linescores']]
        if not a or len(a) != len(b) or any(v is None for v in a + b):
            continue
        a, b = [int(v) for v in a], [int(v) for v in b]
        sa = sum(1 for x, y in zip(a, b) if x > y)
        if max(sa, len(a) - sa) != 2:
            continue
        w = sum(a) if sa > len(a) - sa else sum(b)
        l_ = sum(b) if sa > len(a) - sa else sum(a)
        rows.append({'total': sum(a) + sum(b), 'margin': w - l_})
    return rows


# ---------------------------------------------------------------- baseline functions
def p_total(games, line, side):
    n = len(games)
    over = sum(1 for g in games if g['hs'] + g['as'] > line)
    return (frac(over, n) if side == 'Over' else 1 - frac(over, n)), n


def p_side_margin(games, home_side, k):
    """P(side's margin > -k) for a +k line, or P(side's margin > k') for a -k' line: pass k as the line."""
    n = len(games)
    sign = 1 if home_side else -1
    hits = sum(1 for g in games if sign * (g['hs'] - g['as']) + k > 0)
    return frac(hits, n), n


def p_win(games, home_side):
    n = len(games)
    hw = sum(1 for g in games if g['hs'] > g['as'])
    return (frac(hw, n) if home_side else 1 - frac(hw, n)), n


rows = []


def add(decision, card, rank, contract, family, p, base, ref, result):
    rows.append((decision, card, rank, contract, family, p, base, ref, result))


# ---- MLB (statsapi 2026 regular season, 9-inning Finals before first pitch)
mlb_cards = [
    ('P-500', ts('2026-09-23T17:10:00Z'), 'WSH', 'DET', [
        ('P-500-RL-WSH', '1', 'Nationals +1.5', 'handicap', 0.587, ('side', False, 1.5), 'W'),
        ('P-500-ML', '2', 'Tigers ML', 'moneyline', 0.562, ('win', True), 'L'),
        ('P-500-TOT', '3', 'Combined Total: Over 7.5 Runs', 'total', 0.536, ('total', 7.5, 'Over'), 'L')]),
    ('P-501', ts('2026-09-23T17:35:00Z'), 'TOR', 'BAL', [
        ('P-501-TOT', '1', 'Combined Total: Over 7.5 Runs', 'total', 0.662, ('total', 7.5, 'Over'), 'L'),
        ('P-501-ML', '2', 'Orioles ML', 'moneyline', 0.576, ('win', True), 'W'),
        ('P-501-RL-TOR', '3', 'Blue Jays +1.5', 'handicap', 0.554, ('side', False, 1.5), 'L')]),
    ('P-502', ts('2026-09-23T23:40:00Z'), 'CWS', 'KC', [
        ('P-502-RL-CWS', '1', 'White Sox +1.5', 'handicap', 0.700, ('side', False, 1.5), 'W'),
        ('P-502-RL-KC', '2', 'Royals +1.5', 'handicap', 0.558, ('side', True, 1.5), 'W'),
        ('P-502-TOT', '3', 'Combined Total: Over 8.5 Runs', 'total', 0.553, ('total', 8.5, 'Over'), 'W'),
        ('P-502-WIN', 'winner', 'Winner call: White Sox', 'moneyline', 0.576, ('win', False), 'L')]),
    ('P-506', ts('2026-09-24T02:10:00Z'), 'HOU', 'SEA', [
        ('P-506-RL-HOU', '1', 'Astros +1.5', 'handicap', 0.685, ('side', False, 1.5), 'W'),
        ('P-506-RL-SEA', '2', 'Mariners +1.5', 'handicap', 0.659, ('side', True, 1.5), 'W'),
        ('P-506-TOT', '3', 'Combined Total: Under 7.5 Runs', 'total', 0.506, ('total', 7.5, 'Under'), 'L'),
        ('P-506-WIN', 'winner', 'Winner call: Astros', 'moneyline', 0.511, ('win', False), 'L')]),
]


def base_for(games, spec):
    if spec[0] == 'total':
        return p_total(games, spec[1], spec[2])
    if spec[0] == 'side':
        return p_side_margin(games, spec[1], spec[2])
    return p_win(games, spec[1])


for card, start, _a, _h, items in mlb_cards:
    pop = mlb_prior(start)
    for dec, rank, contract, fam, p, spec, res in items:
        b, n = base_for(pop, spec)
        add(dec, card, rank, contract, fam, p, b, f'MLB 2026 before first pitch, n={n}', res)

# ---- NHL preseason (api-web score pages; 2025 preseason + 2026 preseason before the local date)
pop = nhl_prior('2026-09-23')
for dec, rank, contract, fam, p, spec, res in [
        ('P-503-ML', '1', 'Stars ML', 'moneyline', 0.708, ('win', True), 'W'),
        ('P-503-TOT', '2', 'Combined Total: Under 5.5 Goals', 'total', 0.605, ('total', 5.5, 'Under'), 'W'),
        ('P-503-RL-MIN', '3', 'Wild +1.5', 'handicap', 0.540, ('side', False, 1.5), 'L')]:
    b, n = base_for(pop, spec)
    add(dec, 'P-503', rank, contract, fam, p, b, f'NHL preseason 2025 + 2026 before 23 Sep, n={n}', res)

# ---- WNBA 2026 (ESPN; all completed games before tip)
pop = espn_prior(['WNBA 2026'], ts('2026-09-24T00:00:00Z'))
for dec, rank, contract, fam, p, spec, res in [
        ('P-504-SPR', '1', 'Dream -4.5', 'handicap', 0.591, ('side', False, -4.5), 'W'),
        ('P-504-TOT', '2', 'Combined Total: Under 173.5 Points', 'total', 0.553, ('total', 173.5, 'Under'), 'W'),
        ('P-504-WIN', 'winner', 'Winner call: Dream', 'moneyline', 0.692, ('win', False), 'W')]:
    b, n = base_for(pop, spec)
    add(dec, 'P-504', rank, contract, fam, p, b, f'WNBA 2026 before tip, n={n}', res)

# ---- NBL (ESPN; 2025-26 all completed + 2026-27 before tip)
for card, start, items in [
        ('P-508', ts('2026-09-24T09:30:00Z'), [
            ('P-508-TOT', '1', 'Combined Total: Under 194.5 Points', 'total', 0.691, ('total', 194.5, 'Under'), 'W'),
            ('P-508-SPR', '2', 'Phoenix +2.5', 'handicap', 0.515, ('side', True, 2.5), 'L'),
            ('P-508-WIN', 'winner', 'Winner call: Melbourne United', 'moneyline', 0.549, ('win', False), 'W')]),
        ('P-509', ts('2026-09-24T11:30:00Z'), [
            ('P-509-TOT', '1', 'Combined Total: Under 184.5 Points', 'total', 0.613, ('total', 184.5, 'Under'), 'L'),
            ('P-509-SPR', '2', '36ers -1.5', 'handicap', 0.516, ('side', False, -1.5), 'L'),
            ('P-509-WIN', 'winner', 'Winner call: Adelaide 36ers', 'moneyline', 0.543, ('win', False), 'L')])]:
    pop = espn_prior(['NBL 2025-26', 'NBL 2026-27'], start)
    for dec, rank, contract, fam, p, spec, res in items:
        b, n = base_for(pop, spec)
        add(dec, card, rank, contract, fam, p, b, f'NBL 2025-26 + 2026-27 before tip, n={n}', res)

# ---- WTA (ESPN tennis; women's best-of-3 completed before the match; no side information)
pop = wta_prior(ts('2026-09-23T12:40:00Z'))
n = len(pop)
p_ge6 = frac(sum(1 for r in pop if r['margin'] >= 6), n)
p_under = frac(sum(1 for r in pop if r['total'] <= 19), n)
add('P-495-HCP', 'P-495', '1', 'Gormaz -5.5 Games Handicap', 'handicap', 0.591, 0.5 * p_ge6,
    f'WTA 2026 women best-of-3 before match, 0.5 x P(margin>=6)={p_ge6:.3f}, n={n}', 'L')
add('P-495-TOT', 'P-495', '2', 'Under 19.5 Total Games', 'total', 0.576, p_under,
    f'WTA 2026 women best-of-3 before match, n={n}', 'L')
add('P-495-WIN', 'P-495', 'winner', 'Winner call: Romero Gormaz', 'moneyline', 0.843, 0.5,
    'no side information: 0.5', 'L')

print('| Decision | Card | Rank | Contract (as issued) | Family | Card p | Baseline p | Baseline population (leak-free) | Result |')
print('|---|---|---|---|---|---:|---:|---|---|')
for r in rows:
    print(f'| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]:.3f} | {r[6]:.3f} | {r[7]} | {r[8]} |')
