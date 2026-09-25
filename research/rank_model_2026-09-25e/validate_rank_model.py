"""Out-of-sample validation of RM-1, the ranking-probability model (2026-09-25(e)).

Question: if Rank 1 and Rank 2 had been chosen by a calibrated probability instead of the stated
one, would they have won more often on cards the model had not seen?

Data: research/settled_rows_2026-09-25/settled_rows.csv, rebuilt 2026-09-25(e). The rebuild adds
the P-510+ mini log and corrects 17 mis-graded rows. Decision rows (stated p >= 0.5, W/L) train
each model; every graded row with a stated p is re-ranked on held-out cards.

Specifications compared (tools/rank_model.py):
- IDENTITY   q = stated p (the issued ranking).
- GLOBAL     logit(q) = a + b·logit(p).
- RM-1       GLOBAL + one unpenalised offset for non-baseball, non-soccer underdog cushions
             (pre-specified: the effect was documented in G-L12, C-UNDERDOG-SEPARATION and the
             2026-09-25(d) review before this test).
- RM-1X      RM-1 + ridge-penalised sport slopes, sport offsets and market-class offsets; the ridge
             weight is chosen by grouped CV.

Designs (all group whole cards, because rows inside a card are dependent):
1. Grouped 10-fold CV × 5 repeats: out-of-fold log loss and Brier of the decision rows.
2. Leave-one-card-out re-ranking: order each held-out card's rows by q; compare the Rank-1 and
   Rank-2 win rates, both-win and both-lose rates with the issued order; card-bootstrap interval of
   the per-card change in (R1 + R2) wins.
3. Forward in time: train on cards before P-T and test on P-T onward, T in {420, 450, 480, 495}.
   RM-1X's ridge weight is chosen inside the training cards only.
4. Held-out reliability of RM-1 q by selection tier, and the Rank-1 record by tier.
5. Ordinal era (P-001–P-317, no stated p): Rank-1/Rank-2 record of the cushion class in that
   earlier era.

Output: validation_results.json and a printed summary. Usage: python validate_rank_model.py
"""
import csv
import json
import math
import os
import random
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools'))
import rank_model as rm  # noqa: E402

CSV = os.path.join(REPO, 'research', 'settled_rows_2026-09-25', 'settled_rows.csv')
LAMS = [1, 4, 16, 64, 256]
SPECS = {'GLOBAL': ((), 0.0), 'RM-1': (('cushion_nb',), 0.0),
         'RM-1X': (('cushion_nb', 'sport_slope', 'sport', 'class'), None)}


def all_rows():
    out = []
    for r in csv.DictReader(open(CSV, encoding='utf-8-sig')):
        res = (r['result'] or '').strip().upper()[:1]
        if res not in ('W', 'L'):
            continue
        try:
            g = rm.sport_group(r['sport'])
        except ValueError:
            g = None
        p = float(r['p']) if r['p'] else None
        cls = rm.market_class(g, r['family'], r['direction'], r['contract']) if g else None
        out.append({'card': r['card'], 'num': int(r['num']) if r['num'] else None, 'rank': int(r['rank']),
                    'group': g, 'cls': cls, 'p': p, 'y': 1 if res == 'W' else 0, 'contract': r['contract']})
    return out


def logloss(ps, ys):
    return -sum(y * math.log(max(p, 1e-9)) + (1 - y) * math.log(max(1 - p, 1e-9)) for p, y in zip(ps, ys)) / len(ys)


def brier(ps, ys):
    return sum((p - y) ** 2 for p, y in zip(ps, ys)) / len(ys)


def folds(cards, k, seed):
    cs = sorted(cards)
    random.Random(seed).shuffle(cs)
    return [set(cs[i::k]) for i in range(k)]


def qfun(coef):
    return lambda r: rm.calibrate(coef, r['group'], r['cls'], r['p'])


def choose_lam(train, terms, k=5, reps=2):
    cards = {r['card'] for r in train}
    best = None
    for lam in LAMS:
        ps, ys = [], []
        for rep in range(reps):
            for f in folds(cards, k, 500 + rep):
                q = qfun(rm.fit([r for r in train if r['card'] not in f], lam, terms))
                for r in train:
                    if r['card'] in f:
                        ps.append(q(r))
                        ys.append(r['y'])
        ll = logloss(ps, ys)
        if best is None or ll < best[1]:
            best = (lam, ll)
    return best[0]


def fit_spec(name, train):
    terms, lam = SPECS[name]
    if lam is None:
        lam = choose_lam(train, terms)
    return rm.fit(train, lam, terms)


def rerank(rows_by_card, q_by_card):
    tot = defaultdict(lambda: defaultdict(int))
    detail = []
    for card, rs in rows_by_card.items():
        if card not in q_by_card:
            continue
        issued = sorted(rs, key=lambda r: r['rank'])
        if len(issued) < 2 or issued[0]['rank'] != 1 or issued[1]['rank'] != 2:
            continue
        q = q_by_card[card]

        def key(r, q=q):
            # the tool's ordering (tools/rank_model.rank_rows): a NEAR_TIED_FLIP keeps its stated side
            qv = q(r)
            if (r['p'] > 0.5) != (qv > 0.5) and abs(r['p'] - 0.5) > 1e-9 and abs(qv - 0.5) < rm.FLIP_MARGIN:
                qv = 0.5 + (0.001 if r['p'] > 0.5 else -0.001)
            return (-round(qv, 6), r['rank'])
        new = sorted(issued, key=key)
        for key in ('ALL', issued[0]['group']):
            t = tot[key]
            t['cards'] += 1
            for tag, order in (('issued', issued), ('model', new)):
                a, b = order[0]['y'], order[1]['y']
                t[tag + '_r1'] += a
                t[tag + '_r2'] += b
                t[tag + '_both'] += a * b
                t[tag + '_none'] += (1 - a) * (1 - b)
            t['r1_changed'] += new[0] is not issued[0]
            t['r2_changed'] += new[1] is not issued[1]
        detail.append({'card': card, 'group': issued[0]['group'],
                       'issued': [(x['contract'][:40], x['y'], round(x['p'], 3)) for x in issued[:2]],
                       'model': [(x['contract'][:40], x['y'], round(q(x), 3)) for x in new[:2]]})
    out = {}
    for key, t in tot.items():
        n = t['cards']
        out[key] = {'cards': n,
                    'issued': {k: round(t['issued_' + k] / n, 3) for k in ('r1', 'r2', 'both', 'none')},
                    'model': {k: round(t['model_' + k] / n, 3) for k in ('r1', 'r2', 'both', 'none')},
                    'r1_changed': t['r1_changed'], 'r2_changed': t['r2_changed']}
    return out, detail


def boot(detail, reps=4000, seed=7):
    diffs = [sum(y for _, y, _ in d['model']) - sum(y for _, y, _ in d['issued']) for d in detail]
    n = len(diffs)
    if not n:
        return None
    rng = random.Random(seed)
    bs = sorted(sum(diffs[rng.randrange(n)] for _ in range(n)) / n for _ in range(reps))
    return {'mean_change_in_top2_wins_per_card': round(sum(diffs) / n, 4),
            'ci95': [round(bs[int(0.025 * reps)], 4), round(bs[int(0.975 * reps)], 4)],
            'cards_better': sum(d > 0 for d in diffs), 'cards_worse': sum(d < 0 for d in diffs), 'n': n}


def main():
    rows = all_rows()
    prob = [r for r in rows if r['p'] is not None and r['group']]
    dec = [r for r in prob if r['p'] >= 0.5]
    by_card = defaultdict(list)
    for r in prob:
        by_card[r['card']].append(r)
    ys = [r['y'] for r in dec]
    res = {'data': {'decision_rows': len(dec), 'cards': len({r['card'] for r in dec}), 'prob_rows': len(prob),
                    'decision_win_rate': round(sum(ys) / len(ys), 4)}}

    # 1. grouped CV
    cards = {r['card'] for r in dec}
    cv = {'IDENTITY': {'logloss': round(logloss([r['p'] for r in dec], ys), 4),
                       'brier': round(brier([r['p'] for r in dec], ys), 4)}}
    for name in SPECS:
        preds = defaultdict(list)
        for rep in range(5):
            for f in folds(cards, 10, 1000 + rep):
                q = qfun(fit_spec(name, [r for r in dec if r['card'] not in f]))
                for r in dec:
                    if r['card'] in f:
                        preds[id(r)].append(q(r))
        ps = [sum(preds[id(r)]) / len(preds[id(r)]) for r in dec]
        cv[name] = {'logloss': round(logloss(ps, ys), 4), 'brier': round(brier(ps, ys), 4)}
    res['grouped_cv'] = cv

    # 2. leave-one-card-out re-ranking (RM-1X is too slow for LOCO with inner CV; it uses 10-fold)
    res['loco'] = {}
    oof_rm1 = {}
    for name in ('GLOBAL', 'RM-1'):
        q_by_card = {c: qfun(fit_spec(name, [r for r in dec if r['card'] != c])) for c in by_card}
        summ, det = rerank(by_card, q_by_card)
        res['loco'][name] = {'rerank': summ, 'bootstrap': boot(det)}
        if name == 'RM-1':
            res['loco_rm1_changed_cards'] = [d for d in det if d['issued'] != [(a, b, c) for a, b, c in d['issued']] or
                                             [x[0] for x in d['issued']] != [x[0] for x in d['model']]]
            for c, rs in by_card.items():
                for r in rs:
                    oof_rm1[id(r)] = q_by_card[c](r)
            r1tier = defaultdict(lambda: [0, 0, 0.0])
            for d in det:
                qv = d['model'][0][2]
                t = rm.tier(qv)
                r1tier[t][0] += d['model'][0][1]
                r1tier[t][1] += 1
                r1tier[t][2] += qv
            res['loco_rm1_rank1_by_tier'] = {t: {'won': v[0], 'n': v[1], 'rate': round(v[0] / v[1], 3),
                                                 'mean_q': round(v[2] / v[1], 3)} for t, v in r1tier.items()}
    f10 = {}
    for fold in folds(set(by_card), 10, 77):
        coef = fit_spec('RM-1X', [r for r in dec if r['card'] not in fold])
        for c in fold:
            f10[c] = qfun(coef)
    summ, det = rerank(by_card, f10)
    res['loco']['RM-1X (10-fold)'] = {'rerank': summ, 'bootstrap': boot(det)}

    # 4. held-out reliability of RM-1 by tier (all decision rows)
    rel = defaultdict(lambda: [0, 0, 0.0, 0.0])
    for r in dec:
        qv = oof_rm1[id(r)]
        t = rm.tier(qv)
        rel[t][0] += r['y']
        rel[t][1] += 1
        rel[t][2] += qv
        rel[t][3] += r['p']
    res['loco_rm1_reliability_by_tier'] = {t: {'won': v[0], 'n': v[1], 'rate': round(v[0] / v[1], 3),
                                               'mean_q': round(v[2] / v[1], 3), 'mean_stated_p': round(v[3] / v[1], 3)}
                                           for t, v in rel.items()}

    # 3. forward in time
    fwd = {}
    for t in (420, 450, 480, 495):
        train = [r for r in dec if r['num'] is not None and r['num'] < t]
        test = {c: rs for c, rs in by_card.items() if rs[0]['num'] is not None and rs[0]['num'] >= t}
        tdec = [r for rs in test.values() for r in rs if r['p'] >= 0.5]
        tys = [r['y'] for r in tdec]
        row = {'train_decisions': len(train), 'test_cards': len(test), 'test_decisions': len(tdec),
               'IDENTITY': {'logloss': round(logloss([r['p'] for r in tdec], tys), 4),
                            'brier': round(brier([r['p'] for r in tdec], tys), 4)}}
        for name in SPECS:
            coef = fit_spec(name, train)
            q = qfun(coef)
            summ, det = rerank(test, {c: q for c in test})
            row[name] = {'logloss': round(logloss([q(r) for r in tdec], tys), 4),
                         'brier': round(brier([q(r) for r in tdec], tys), 4),
                         'rerank': summ.get('ALL'), 'bootstrap': boot(det),
                         'weights': {k: round(v, 3) for k, v in coef['weights'].items()} if name != 'RM-1X' else None,
                         'lam': coef['lam']}
        fwd[t] = row
    res['forward'] = fwd

    # 5. cushion class across eras
    era = defaultdict(lambda: [0, 0])
    for r in rows:
        if r['cls'] == 'hcp_plus_nb' and r['rank'] in (1, 2):
            key = 'ordinal era (no p), R1/R2' if r['p'] is None else 'probability era, R1/R2'
            era[key][0] += r['y']
            era[key][1] += 1
    res['cushion_nb_by_era'] = {k: {'won': v[0], 'n': v[1], 'rate': round(v[0] / v[1], 3)} for k, v in era.items()}

    final = rm.fit(dec, 0.0, ('cushion_nb',))
    res['final_rm1'] = {k: round(v, 4) for k, v in final['weights'].items()}

    with open(os.path.join(HERE, 'validation_results.json'), 'w', encoding='utf-8') as fh:
        json.dump(res, fh, indent=2, default=str)

    print('data', res['data'])
    print('grouped CV', cv)
    for name, v in res['loco'].items():
        print('LOCO', name, 'ALL', v['rerank']['ALL'], 'boot', v['bootstrap'])
    for g, v in res['loco']['RM-1']['rerank'].items():
        if g != 'ALL':
            print('   RM-1 by sport', g, v)
    print('RM-1 held-out reliability by tier', res['loco_rm1_reliability_by_tier'])
    print('RM-1 held-out Rank-1 by tier', res['loco_rm1_rank1_by_tier'])
    for t, v in fwd.items():
        print('forward', t, 'train', v['train_decisions'], 'test cards', v['test_cards'], 'IDENTITY', v['IDENTITY'])
        for name in SPECS:
            print('   ', name, {k: v[name][k] for k in ('logloss', 'brier', 'lam')}, 'rerank', v[name]['rerank'],
                  'boot', v[name]['bootstrap'])
    print('cushion by era', res['cushion_nb_by_era'])
    print('final RM-1', res['final_rm1'])


if __name__ == '__main__':
    main()
