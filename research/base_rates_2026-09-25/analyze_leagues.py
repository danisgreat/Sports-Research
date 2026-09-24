"""Descriptive base rates, width benchmarks and R-1 recency tests from ESPN season scoreboards.

Outputs JSON + a printed summary. Descriptive only: no fitted coefficient is produced for use on cards.
Regular season only (ESPN season.type == 2) unless a league has no type-2 games.
"""
import json
import math
import statistics as st
import sys
from collections import defaultdict

from fetch import espn_scoreboard

SPEC = {
    'WNBA 2026': ('basketball/wnba', '20260501', '20260924', 'bk'),
    'NBA 2025-26': ('basketball/nba', '20251021', '20260620', 'bk'),
    'NBL 2025-26': ('basketball/nbl', '20250918', '20260331', 'bk'),
    'NHL 2025-26 (ESPN)': ('hockey/nhl', '20251007', '20260620', 'hk'),
    'EPL 2025-26': ('soccer/eng.1', '20250815', '20260524', 'sc'),
}


def ci95(xs):
    n = len(xs)
    if n < 2:
        return (float('nan'), float('nan'), float('nan'))
    m = st.fmean(xs)
    se = st.stdev(xs) / math.sqrt(n)
    return (m, m - 1.96 * se, m + 1.96 * se)


def prop_ci(k, n):
    if n == 0:
        return (float('nan'),) * 3
    p = k / n
    se = math.sqrt(p * (1 - p) / n)
    return (p, max(0.0, p - 1.96 * se), min(1.0, p + 1.96 * se))


def load(label):
    path, s, e, kind = SPEC[label]
    evs = espn_scoreboard(path, s, e)['events']
    types = defaultdict(int)
    for ev in evs:
        types[(ev.get('season') or {}).get('type')] += 1
    games = []
    for ev in evs:
        if not ev['status']['type'].get('completed'):
            continue
        stype = (ev.get('season') or {}).get('type')
        comp = ev['competitions'][0]
        cps = comp['competitors']
        if len(cps) != 2:
            continue
        h = [c for c in cps if c.get('homeAway') == 'home']
        a = [c for c in cps if c.get('homeAway') == 'away']
        if not h or not a:
            continue
        h, a = h[0], a[0]
        try:
            hs, as_ = float(h['score']), float(a['score'])
        except (KeyError, TypeError, ValueError):
            continue
        hl = [x.get('value') for x in h.get('linescores', [])]
        al = [x.get('value') for x in a.get('linescores', [])]
        games.append({
            'id': ev['id'], 'date': ev['date'], 'stype': stype, 'neutral': comp.get('neutralSite', False),
            'home': h['team']['id'], 'away': a['team']['id'], 'hs': hs, 'as': as_,
            'hl': hl, 'al': al, 'period': ev['status'].get('period'),
            'detail': ev['status']['type'].get('detail') or ev['status']['type'].get('shortDetail'),
            'status_name': ev['status']['type'].get('name'),
        })
    return games, dict(types), kind


def regular(games):
    reg = [g for g in games if g['stype'] == 2]
    return reg if reg else games


def base_rates(games, kind):
    tot = [g['hs'] + g['as'] for g in games]
    mar = [g['hs'] - g['as'] for g in games]
    n = len(games)
    out = {'n': n, 'total_mean': st.fmean(tot), 'total_sd': st.stdev(tot), 'total_median': st.median(tot),
           'home_margin_mean': ci95(mar), 'margin_sd': st.stdev(mar),
           'home_win': prop_ci(sum(1 for m in mar if m > 0), n)}
    absm = [abs(m) for m in mar]
    if kind == 'bk':
        reg_periods = 4
        ot = [g for g in games if len(g['hl']) > reg_periods]
        out['ot_rate'] = prop_ci(len(ot), n)
        out['abs_margin_le'] = {k: prop_ci(sum(1 for m in absm if m <= k), n)[0] for k in (3, 5, 7, 10, 15)}
        out['abs_margin_ge'] = {k: prop_ci(sum(1 for m in absm if m >= k), n)[0] for k in (10, 15, 20)}
        # first-half share: sum of first two periods
        h1 = [sum(g['hl'][:2]) + sum(g['al'][:2]) for g in games if len(g['hl']) >= 4 and len(g['al']) >= 4]
        reg_tot = [sum(g['hl'][:4]) + sum(g['al'][:4]) for g in games if len(g['hl']) >= 4 and len(g['al']) >= 4]
        out['h1_mean'] = st.fmean(h1)
        out['h1_sd'] = st.stdev(h1)
        out['h1_share'] = st.fmean([a / b for a, b in zip(h1, reg_tot) if b])
        q = [[g['hl'][i] + g['al'][i] for g in games if len(g['hl']) >= 4 and len(g['al']) >= 4] for i in range(4)]
        out['quarter_means'] = [st.fmean(x) for x in q]
        out['quarter_sd'] = [st.stdev(x) for x in q]
        ot_added = [sum(g['hl'][4:]) + sum(g['al'][4:]) for g in ot]
        out['ot_points_added_mean'] = st.fmean(ot_added) if ot_added else None
    elif kind == 'hk':
        ot = [g for g in games if len(g['hl']) > 3]
        so = [g for g in ot if (g['detail'] or '').upper().find('SO') >= 0]
        out['ot_or_so_rate'] = prop_ci(len(ot), n)
        out['so_rate'] = prop_ci(len(so), n)
        out['total_dist'] = {k: sum(1 for t in tot if t == k) / n for k in range(0, 13)}
        out['abs_margin_dist'] = {k: sum(1 for m in absm if m == k) / n for k in range(0, 8)}
    elif kind == 'sc':
        dist = defaultdict(int)
        for t in tot:
            dist[int(t)] += 1
        out['total_dist'] = {k: dist[k] / n for k in sorted(dist)}
        out['draw'] = prop_ci(sum(1 for m in mar if m == 0), n)
        out['away_win'] = prop_ci(sum(1 for m in mar if m < 0), n)
        out['btts'] = prop_ci(sum(1 for g in games if g['hs'] > 0 and g['as'] > 0), n)
        out['over_2_5'] = prop_ci(sum(1 for t in tot if t >= 3), n)
        out['over_1_5'] = prop_ci(sum(1 for t in tot if t >= 2), n)
        out['over_3_5'] = prop_ci(sum(1 for t in tot if t >= 4), n)
        h1 = [g['hl'][0] + g['al'][0] for g in games if g['hl'] and g['al'] and g['hl'][0] is not None]
        if h1:
            out['h1_n'] = len(h1)
            out['h1_mean'] = st.fmean(h1)
            out['h1_dist'] = {k: sum(1 for x in h1 if x == k) / len(h1) for k in range(0, 6)}
        out['abs_margin_dist'] = {k: sum(1 for m in absm if m == k) / n for k in range(0, 6)}
    return out


def team_games(games):
    """Per-team chronological list of (date, pts_for, pts_against, opp, is_home)."""
    tg = defaultdict(list)
    for g in sorted(games, key=lambda x: x['date']):
        tg[g['home']].append((g['date'], g['hs'], g['as'], g['away'], True, g['id']))
        tg[g['away']].append((g['date'], g['as'], g['hs'], g['home'], False, g['id']))
    return tg


def recency(games, kind):
    """R-1 tests on team points/goals scored."""
    tg = team_games(games)
    # 1. bounce-back vs own leave-two-out mean
    low_q = {'bk': 0.2, 'hk': 0.2, 'sc': 0.2}[kind]
    res = {}
    pairs = []  # (prev, next, baseline)
    lag_pairs = []
    for team, lst in tg.items():
        pts = [x[1] for x in lst]
        n = len(pts)
        if n < 10:
            continue
        tot = sum(pts)
        mu = tot / n
        for i in range(n - 1):
            base = (tot - pts[i] - pts[i + 1]) / (n - 2)
            pairs.append((pts[i] - base, pts[i + 1] - base, pts[i], pts[i + 1], base, mu))
            lag_pairs.append((pts[i] - mu, pts[i + 1] - mu))
    # low previous game = previous residual in bottom quintile of residuals
    resid_prev = sorted(p[0] for p in pairs)
    cut_lo = resid_prev[int(low_q * len(resid_prev))]
    cut_hi = resid_prev[int((1 - low_q) * len(resid_prev))]
    lo = [p[1] for p in pairs if p[0] <= cut_lo]
    hi = [p[1] for p in pairs if p[0] >= cut_hi]
    res['after_bottom_quintile'] = {'n': len(lo), 'cut_resid': cut_lo, 'next_minus_base': ci95(lo)}
    res['after_top_quintile'] = {'n': len(hi), 'cut_resid': cut_hi, 'next_minus_base': ci95(hi)}
    xs = [a for a, b in lag_pairs]
    ys = [b for a, b in lag_pairs]
    res['lag1_autocorr'] = {'n': len(lag_pairs), 'r': st.correlation(xs, ys)}
    # 2. out-of-sample: predict next team points using only prior games
    league_prior = []  # running league mean from all earlier games
    all_team_games = sorted(((x[0], team, i) for team, lst in tg.items() for i, x in enumerate(lst)))
    # Build per-date league running mean (points per team-game) from strictly earlier dates
    by_date = defaultdict(list)
    for team, lst in tg.items():
        for x in lst:
            by_date[x[0][:10]].append(x[1])
    dates = sorted(by_date)
    run_sum = run_n = 0
    league_before = {}
    for d in dates:
        league_before[d] = run_sum / run_n if run_n else None
        run_sum += sum(by_date[d])
        run_n += len(by_date[d])
    # opponent defence to date
    def_before = {}
    for team, lst in tg.items():
        allowed = []
        for x in lst:
            def_before[(team, x[5])] = (st.fmean(allowed) if allowed else None, len(allowed))
            allowed.append(x[2])
    preds = defaultdict(list)
    min_prior = {'bk': 10, 'hk': 10, 'sc': 8}[kind]
    for team, lst in tg.items():
        for i, x in enumerate(lst):
            if i < min_prior:
                continue
            lb = league_before.get(x[0][:10])
            if lb is None:
                continue
            prior = [y[1] for y in lst[:i]]
            actual = x[1]
            opp_def, opp_n = def_before.get((x[3], x[5]), (None, 0))
            if opp_def is None or opp_n < min_prior:
                continue
            preds['league_constant'].append((lb, actual))
            std = st.fmean(prior)
            preds['season_to_date'].append((std, actual))
            for w in (10, 5, 3, 1):
                preds[f'last_{w}'].append((st.fmean(prior[-w:]), actual))
            preds['std_plus_opp_def'].append((std + opp_def - lb, actual))
            # shrunk: half-way between season-to-date and league
            preds['std_shrunk_50'].append((0.5 * std + 0.5 * lb, actual))
    oos = {}
    for k, v in preds.items():
        err = [p - a for p, a in v]
        oos[k] = {'n': len(v), 'mae': st.fmean(abs(e) for e in err), 'rmse': math.sqrt(st.fmean(e * e for e in err)),
                  'bias': st.fmean(err)}
    res['oos'] = oos
    return res


def width_benchmark(games, kind):
    """Residual SD of game total and home margin around a leak-free season-to-date predictor.
    Predictor: total_hat = (home off + away def)/2 + (away off + home def)/2 on prior games;
    margin_hat = (home net rating − away net rating)/2 ... simple: home pf-pa to date vs away pf-pa to date, plus
    league home edge to date. Descriptive benchmark for card widths, not a model."""
    tg = team_games(games)
    hist = defaultdict(list)  # team -> list of (pf, pa)
    home_edge = []
    rt, rm = [], []
    min_prior = {'bk': 10, 'hk': 10, 'sc': 8}[kind]
    for g in sorted(games, key=lambda x: x['date']):
        h, a = hist[g['home']], hist[g['away']]
        if len(h) >= min_prior and len(a) >= min_prior:
            hpf, hpa = st.fmean(x[0] for x in h), st.fmean(x[1] for x in h)
            apf, apa = st.fmean(x[0] for x in a), st.fmean(x[1] for x in a)
            that = (hpf + apa) / 2 + (apf + hpa) / 2
            he = st.fmean(home_edge) if home_edge else 0.0
            mhat = ((hpf - hpa) - (apf - apa)) / 2 + he
            rt.append((g['hs'] + g['as']) - that)
            rm.append((g['hs'] - g['as']) - mhat)
        hist[g['home']].append((g['hs'], g['as']))
        hist[g['away']].append((g['as'], g['hs']))
        if not g['neutral']:
            home_edge.append(g['hs'] - g['as'])
    tot = [g['hs'] + g['as'] for g in games]
    mar = [g['hs'] - g['as'] for g in games]
    return {'n_scored': len(rt), 'total_resid_sd': st.pstdev(rt) if rt else None,
            'total_resid_bias': st.fmean(rt) if rt else None, 'total_raw_sd': st.stdev(tot),
            'margin_resid_sd': st.pstdev(rm) if rm else None, 'margin_resid_bias': st.fmean(rm) if rm else None,
            'margin_raw_sd': st.stdev(mar),
            'total_resid_abs_le_half_sd': (sum(1 for r in rt if abs(r) <= 0.5 * st.pstdev(rt)) / len(rt)) if rt else None}


def main(labels):
    allout = {}
    for label in labels:
        games, types, kind = load(label)
        reg = regular(games)
        out = {'season_types_all_events': types, 'completed': len(games), 'regular_completed': len(reg),
               'first': reg[0]['date'] if reg else None, 'last': reg[-1]['date'] if reg else None,
               'base': base_rates(reg, kind), 'width': width_benchmark(reg, kind), 'recency': recency(reg, kind)}
        allout[label] = out
        print('=' * 20, label, json.dumps({k: out[k] for k in ('season_types_all_events', 'completed', 'regular_completed', 'first', 'last')}))
        print('BASE', json.dumps(out['base'], default=str))
        print('WIDTH', json.dumps(out['width']))
        print('RECENCY', json.dumps(out['recency']))
    with open('league_results.json', 'w', encoding='utf-8') as fh:
        json.dump(allout, fh, indent=1, default=str)


if __name__ == '__main__':
    main(sys.argv[1:] or list(SPEC))
