"""H0 point-in-time features: no result can reach an earlier or same-day row."""
import copy
import math
from datetime import date, timedelta

import numpy as np
import pytest

from research.src import h0_features
from research.src.archive_std import StdEvent


def season(year=2025, teams=6, rounds=3, seed=1):
    rng = np.random.default_rng(seed)
    names = [f'T{i}' for i in range(teams)]
    events, day = [], date(year, 9, 1)
    for _ in range(rounds):
        for i in range(teams):
            for j in range(teams):
                if i != j:
                    events.append(StdEvent(sport='Ice Hockey', competition='X', season_year=year, date=day.isoformat(), stage='regular',
                                           home=names[i], away=names[j], home_score=int(rng.poisson(3.1)), away_score=int(rng.poisson(2.8))))
                    if len(events) % 3 == 0:
                        day += timedelta(days=1)
    return events


def test_features_use_only_earlier_dates_and_ignore_the_future():
    events = season()
    base = h0_features.build_rows(events)
    cut = len(events) // 2
    cut_date = sorted(e.date for e in events)[cut]
    mutated = copy.deepcopy(events)
    for e in mutated:
        if e.date >= cut_date:
            e.home_score, e.away_score = 9, 0                         # rewrite every result from the cut date onward
    changed = h0_features.build_rows(mutated)
    for a, b in zip(base, changed):
        if a['date'] <= cut_date:
            for name in h0_features.FEATURES:
                assert (a[name] == b[name]) or (math.isnan(a[name]) and math.isnan(b[name])), (a['date'], name)


def test_same_day_games_do_not_see_each_other():
    events = season()
    by_day = {}
    for e in events:
        by_day.setdefault(e.date, []).append(e)
    day = next(d for d, g in by_day.items() if len(g) >= 2 and d > min(by_day))
    mutated = copy.deepcopy(events)
    for e in mutated:
        if e.date == day:
            e.home_score, e.away_score = 11, 0
    base, changed = h0_features.build_rows(events), h0_features.build_rows(mutated)
    for a, b in zip(base, changed):
        if a['date'] == day:
            assert a['home_gf5'] == b['home_gf5'] or (math.isnan(a['home_gf5']) and math.isnan(b['home_gf5']))
            assert a['elo_diff'] == b['elo_diff']


def test_known_at_is_after_the_latest_contributing_game_and_missing_history_is_nan():
    rows = h0_features.build_rows(season())
    first = rows[0]
    assert first['known_at'] is None and math.isnan(first['home_gf5']) and first['home_rest'] == -1.0
    for r in rows:
        if r['known_at']:
            assert r['known_at'] <= r['date']                      # known_at <= cutoff: the feature-store invariant of H0_DATASET_CARD.md
    none_rows = [i for i, r in enumerate(rows) if r['known_at'] is None]
    assert none_rows == list(range(len(none_rows))) and len(none_rows) <= 3        # only the opening games, before any history exists


def test_matrix_shape_nan_and_elo_learns_strength():
    events = season(rounds=8)
    # make T0 strong
    for e in events:
        if e.home == 'T0':
            e.home_score += 2
        if e.away == 'T0':
            e.away_score += 2
    rows = h0_features.build_rows(events)
    X = h0_features.matrix(rows)
    assert X.shape == (len(rows), len(h0_features.FEATURES)) and np.isnan(X[0]).any()
    late = [r for r in rows if r['home'] == 'T0'][-5:]
    assert all(r['home_elo'] > 1500 for r in late)
    assert h0_features.matrix([rows[0]], ['home_rest']).tolist() == [[-1.0]]
