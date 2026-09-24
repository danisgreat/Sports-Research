"""Extra descriptive tests: rest-days effect, monthly scoring drift, NBL/WNBA total drift.
Uses the same leak-free season-to-date predictor as analyze_leagues.width_benchmark and reports
the mean residual by rest state (a named-mechanism reference, not a coefficient)."""
import datetime as dt
import json
import math
import statistics as st
import sys
from collections import defaultdict

from analyze_leagues import SPEC, load, regular, ci95


def parse(d):
    return dt.datetime.fromisoformat(d.replace('Z', '+00:00'))


def rest_effect(games, kind, min_prior=10):
    hist = defaultdict(list)
    last_date = {}
    home_edge = []
    by_rest = defaultdict(list)       # margin residual from the team's perspective, by (own rest, opp rest)
    tot_by_b2b = defaultdict(list)    # total residual by number of teams on 0 days rest
    for g in sorted(games, key=lambda x: x['date']):
        t = parse(g['date'])
        # local-day approximation: subtract 5h (Americas) for NBA/WNBA/NHL, +10h for NBL
        shift = dt.timedelta(hours=10) if kind == 'nbl' else dt.timedelta(hours=-5)
        day = (t + shift).date()
        rest = {}
        for tm in (g['home'], g['away']):
            rest[tm] = (day - last_date[tm]).days - 1 if tm in last_date else None
        h, a = hist[g['home']], hist[g['away']]
        if len(h) >= min_prior and len(a) >= min_prior and None not in rest.values():
            hpf, hpa = st.fmean(x[0] for x in h), st.fmean(x[1] for x in h)
            apf, apa = st.fmean(x[0] for x in a), st.fmean(x[1] for x in a)
            that = (hpf + apa) / 2 + (apf + hpa) / 2
            he = st.fmean(home_edge) if home_edge else 0.0
            mhat = ((hpf - hpa) - (apf - apa)) / 2 + he
            rm = (g['hs'] - g['as']) - mhat
            rt = (g['hs'] + g['as']) - that
            rh = min(rest[g['home']], 3)
            ra = min(rest[g['away']], 3)
            by_rest[(rh, ra)].append(rm)          # home perspective
            by_rest[('A', ra, rh)].append(-rm)     # away perspective keyed separately
            nb2b = int(rest[g['home']] == 0) + int(rest[g['away']] == 0)
            tot_by_b2b[nb2b].append(rt)
        hist[g['home']].append((g['hs'], g['as']))
        hist[g['away']].append((g['as'], g['hs']))
        last_date[g['home']] = day
        last_date[g['away']] = day
        if not g['neutral']:
            home_edge.append(g['hs'] - g['as'])
    # Team on 0 days' rest v an opponent with >= 1 day, from the tired team's perspective. Only this
    # asymmetric contrast is reported: a symmetric state (both rested, both tired) pools each game
    # from both perspectives, so its mean margin residual is 0 by construction and says nothing.
    b2b_v_rested = []
    for k, v in by_rest.items():
        if k[0] == 'A':
            own, opp = k[1], k[2]
        else:
            own, opp = k[0], k[1]
        if own == 0 and opp >= 1:
            b2b_v_rested.extend(v)
    return {
        'b2b_vs_rested_margin_resid': (len(b2b_v_rested), ci95(b2b_v_rested)),
        'total_resid_by_n_teams_on_b2b': {k: (len(v), ci95(v)) for k, v in sorted(tot_by_b2b.items())},
    }


def monthly(games):
    m = defaultdict(list)
    for g in games:
        m[g['date'][:7]].append(g['hs'] + g['as'])
    return {k: (len(v), round(st.fmean(v), 2)) for k, v in sorted(m.items())}


if __name__ == '__main__':
    out = {}
    for label in sys.argv[1:]:
        games, types, kind = load(label)
        reg = regular(games)
        k2 = 'nbl' if 'NBL' in label else kind
        r = {'monthly_total_mean': monthly(reg)}
        if kind in ('bk', 'hk'):
            r['rest'] = rest_effect(reg, k2)
        out[label] = r
        print('=' * 10, label)
        print(json.dumps(r, default=str))
    with open('extra_results.json', 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, default=str)
