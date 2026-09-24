"""NHL 2025-26 from api-web score pages: empty-net goals, regulation margin bands, OT/SO, preseason v regular.
Reads only games/goals fields (the payload's oddsPartners key is never read)."""
import json
import math
import statistics as st
from collections import Counter, defaultdict

G = json.load(open('nhl.json', encoding='utf-8'))


def pci(k, n):
    p = k / n if n else float('nan')
    se = math.sqrt(p * (1 - p) / n) if n else float('nan')
    return round(p, 4), round(max(0, p - 1.96 * se), 4), round(min(1, p + 1.96 * se), 4), n


def summarize(games, label):
    n = len(games)
    out = {'label': label, 'n': n}
    tot, en_games, en_goals = [], 0, 0
    reg_decided = [g for g in games if (g['gameOutcome'] or {}).get('lastPeriodType') == 'REG']
    ot = [g for g in games if (g['gameOutcome'] or {}).get('lastPeriodType') == 'OT']
    so = [g for g in games if (g['gameOutcome'] or {}).get('lastPeriodType') == 'SO']
    out['reg_decided'] = pci(len(reg_decided), n)
    out['ot'] = pci(len(ot), n)
    out['so'] = pci(len(so), n)
    margins_reg = Counter()
    en_in_2goal = 0
    en_in_3plus = 0
    margin_before_en = Counter()
    goals_3rd = []
    for g in games:
        hs, as_ = g['homeTeam'].get('score'), g['awayTeam'].get('score')
        tot.append(hs + as_)
        goals = g.get('goals') or []
        ens = [x for x in goals if x.get('goalModifier') == 'empty-net']
        if ens:
            en_games += 1
        en_goals += len(ens)
        goals_3rd.append(sum(1 for x in goals if (x.get('periodDescriptor') or {}).get('number') == 3))
    for g in reg_decided:
        hs, as_ = g['homeTeam'].get('score'), g['awayTeam'].get('score')
        m = abs(hs - as_)
        margins_reg[min(m, 5)] += 1
        goals = g.get('goals') or []
        ens = [x for x in goals if x.get('goalModifier') == 'empty-net']
        if m == 2 and ens:
            en_in_2goal += 1
        if m >= 3 and ens:
            en_in_3plus += 1
        # margin excluding empty-net goals
        m_ex = abs((hs - sum(1 for x in ens if x.get('teamAbbrev') == g['homeTeam'].get('abbrev')))
                   - (as_ - sum(1 for x in ens if x.get('teamAbbrev') == g['awayTeam'].get('abbrev'))))
        margin_before_en[min(m_ex, 5)] += 1
    nr = len(reg_decided)
    out['total_mean_sd'] = (round(st.fmean(tot), 3), round(st.stdev(tot), 3))
    out['games_with_EN_goal'] = pci(en_games, n)
    out['EN_goals_per_game'] = round(en_goals / n, 3)
    out['reg_margin_dist'] = {k: pci(v, nr)[0] for k, v in sorted(margins_reg.items())}
    out['reg_margin_dist_excl_EN'] = {k: pci(v, nr)[0] for k, v in sorted(margin_before_en.items())}
    out['P(margin>=2 | reg decided)'] = pci(sum(v for k, v in margins_reg.items() if k >= 2), nr)
    out['P(margin>=2 | all games)'] = pci(sum(v for k, v in margins_reg.items() if k >= 2), n)
    out['share of 2-goal reg wins containing EN'] = pci(en_in_2goal, margins_reg[2])
    out['3rd period goals mean'] = round(st.fmean(goals_3rd), 3)
    # total distribution cumulative
    c = Counter(tot)
    out['P(total<=k)'] = {k: round(sum(v for t, v in c.items() if t <= k) / n, 4) for k in range(3, 9)}
    return out


if __name__ == '__main__':
    games = list(G.values())
    games = [g for g in games if g.get('gameState') in ('OFF', 'FINAL')]
    by_type = defaultdict(list)
    for g in games:
        by_type[g['gameType']].append(g)
    print({k: len(v) for k, v in by_type.items()})
    res = {}
    for gt, label in ((2, 'regular'), (1, 'preseason'), (3, 'playoffs')):
        if by_type.get(gt):
            res[label] = summarize(by_type[gt], label)
            print(json.dumps(res[label]))
    json.dump(res, open('nhl_results.json', 'w', encoding='utf-8'), indent=1)
