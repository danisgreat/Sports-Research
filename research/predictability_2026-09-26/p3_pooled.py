"""P3 pooled — every matched card contract (MLB + other leagues), card p against A1 (and A0).

Preregistered (cc447c9): the pooled card − model Brier with a card-cluster bootstrap, and a 50/50 logit blend
(exploratory). Added here and labelled EXPLORATORY (not preregistered): the disagreement split. When the card and
A1 differ by more than 0.10 on a contract, which one scored better?
Reads p3_mlb_results.json and p3_other_results.json; writes p3_pooled_results.json.
"""
import json
import math
import os
import random
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


def lg(x):
    x = min(max(x, 1e-4), 1 - 1e-4)
    return math.log(x / (1 - x))


def brier(k, rs):
    return sum((r[k] - r['y']) ** 2 for r in rs) / len(rs) if rs else float('nan')


def boot_diff(recs, a, b, n=2000, seed=20260926):
    by = defaultdict(list)
    for r in recs:
        by[r['card']].append(r)
    cards = list(by)
    rng = random.Random(seed)
    d = []
    for _ in range(n):
        s = [r for c in (rng.choice(cards) for _ in cards) for r in by[c]]
        d.append(brier(a, s) - brier(b, s))
    d.sort()
    return {'mean': round(brier(a, recs) - brier(b, recs), 4), 'ci95_card_cluster': [round(d[int(0.025 * n)], 4),
                                                                                    round(d[int(0.975 * n) - 1], 4)]}


def main():
    mlb = json.load(open(os.path.join(HERE, 'p3_mlb_results.json')))['records']
    oth = json.load(open(os.path.join(HERE, 'p3_other_results.json')))['records']
    recs = [{'card': r['card'], 'league': 'mlb', 'y': r['y'], 'card_p': r['card_p'], 'a0': r['a0'], 'a1': r['a1']}
            for r in mlb] + [{'card': r['card'], 'league': r['league'], 'y': r['y'], 'card_p': r['card_p'],
                              'a0': r['a0'], 'a1': r['a1']} for r in oth]
    for r in recs:
        r['blend'] = 1 / (1 + math.exp(-(lg(r['card_p']) + lg(r['a1'])) / 2))
    out = {'events': len(recs), 'cards': len({r['card'] for r in recs}),
           'brier': {k: round(brier(k, recs), 4) for k in ('card_p', 'a1', 'a0', 'blend')},
           'card_minus_a1': boot_diff(recs, 'card_p', 'a1'),
           'card_minus_a0': boot_diff(recs, 'card_p', 'a0'),
           'a1_minus_a0': boot_diff(recs, 'a1', 'a0'),
           'blend_minus_card (exploratory)': boot_diff(recs, 'blend', 'card_p')}
    dis = [r for r in recs if abs(r['card_p'] - r['a1']) > 0.10]
    agr = [r for r in recs if abs(r['card_p'] - r['a1']) <= 0.10]
    out['EXPLORATORY_disagreement_gt_0.10'] = {
        'n': len(dis), 'cards': len({r['card'] for r in dis}),
        'brier_card': round(brier('card_p', dis), 4), 'brier_a1': round(brier('a1', dis), 4),
        'card_closer_to_outcome': sum(abs(r['card_p'] - r['y']) < abs(r['a1'] - r['y']) for r in dis),
        'card_minus_a1': boot_diff(dis, 'card_p', 'a1') if dis else None}
    out['agreement_le_0.10'] = {'n': len(agr), 'brier_card': round(brier('card_p', agr), 4),
                                'brier_a1': round(brier('a1', agr), 4)}
    json.dump(out, open(os.path.join(HERE, 'p3_pooled_results.json'), 'w'), indent=2)
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
