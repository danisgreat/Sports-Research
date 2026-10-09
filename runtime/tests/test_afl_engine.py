"""AFL engine (DST-12, DST-01, DST-13)."""

import numpy as np
import pytest

from research.src import archive_std
from runtime.src.common.counts import count_moments
from runtime.src.common.errors import InsufficientData, MissingInputs, MissingScore, UnknownTeam
from runtime.src.common.leagues import get_profile
from runtime.src.sports.afl.engine import AFLEngine, points_matrix

AFL = get_profile("afl", "AFL")


def test_points_matrix_is_six_per_goal_one_per_behind():
    m = points_matrix(0.55)
    assert np.allclose(m.sum(axis=1), 1.0)
    assert (m[20] * np.arange(m.shape[1])).sum() == pytest.approx(20 * (0.55 * 6 + 0.45), abs=0.01)
    assert m[0, 0] == pytest.approx(1.0)
    assert m[1, 6] == pytest.approx(0.55) and m[1, 1] == pytest.approx(0.45)


def test_calibrated_engine_reproduces_profile_spread_and_negative_correlation():
    engine = AFLEngine(league=AFL)
    shots = AFL.extra("scoring_shots_mean")
    dist = engine.predict_distribution({"home_expected_shots": shots * 1.04, "away_expected_shots": shots * 0.96})
    mh, ma, vt, vm = count_moments(dist.grid)
    assert np.sqrt(vt) == pytest.approx(AFL.total_sd, rel=0.01) and np.sqrt(vm) == pytest.approx(AFL.margin_sd, rel=0.01)
    assert mh > ma
    assert (vt - vm) / 4.0 < 0                                          # scores are negatively dependent
    assert dist.p_home_win() > 0.5 and dist.grid.sum() == pytest.approx(1.0)


def test_period_rows_scale_the_structure_and_need_an_explicit_fraction():
    engine = AFLEngine(league=AFL)
    ctx = {"home_expected_shots": 23.0, "away_expected_shots": 23.0}
    full, half, quarter = engine.predict_distribution(ctx), engine.predict_period(ctx, 0.5), engine.predict_period(ctx, 0.25)
    assert sum(half.expected_scores()) == pytest.approx(0.5 * sum(full.expected_scores()), rel=0.02)
    assert sum(quarter.expected_scores()) == pytest.approx(0.25 * sum(full.expected_scores()), rel=0.02)
    with pytest.raises(ValueError):
        engine.predict_period(ctx, 1.5)
    with pytest.raises(ValueError):
        engine.predict_distribution(ctx, endpoint="regulation")


def test_finals_regime_multiplier_lowers_scoring():
    engine = AFLEngine(league=AFL)
    ctx = {"home_expected_shots": 23.0, "away_expected_shots": 23.0}
    assert sum(engine.predict_distribution({**ctx, "scoring_multiplier": 0.92}).expected_scores()) < sum(engine.predict_distribution(ctx).expected_scores())


def test_inputs_are_required_not_defaulted():
    with pytest.raises(MissingInputs, match="goal conversion"):
        AFLEngine(total_sd=29.0, margin_sd=41.0).predict_distribution({"home_expected_shots": 23, "away_expected_shots": 23})
    with pytest.raises(MissingInputs, match="total_sd"):
        AFLEngine(conversion=0.53).predict_distribution({"home_expected_shots": 23, "away_expected_shots": 23})


def test_archive_round_trip_matches_the_recorded_league():
    events = [e for e in archive_std.iter_events(sport="AFL", competition="AFL", seasons=range(2022, 2026), stages={"regular"})
              if e.home_behinds is not None and e.away_behinds is not None]
    assert len(events) > 500
    rows = [{"home_team": e.home, "away_team": e.away, "home_goals": e.home_goals, "away_goals": e.away_goals,
             "home_behinds": e.home_behinds, "away_behinds": e.away_behinds} for e in events]
    engine = AFLEngine().fit(rows)
    assert engine.conversion == pytest.approx(AFL.extra("goal_conversion"), abs=0.02)
    teams = sorted({e.home for e in events})
    dist = engine.predict_distribution({"home_team": teams[0], "away_team": teams[1]})
    mh, ma, vt, vm = count_moments(dist.grid)
    assert np.sqrt(vt) == pytest.approx(engine.total_sd, rel=0.01) and np.sqrt(vm) == pytest.approx(engine.margin_sd, rel=0.01)
    assert 70 < mh < 100 and 65 < ma < 95
    with pytest.raises(UnknownTeam):
        engine.predict_distribution({"home_team": teams[0], "away_team": "Nobody FC"})
    with pytest.raises(MissingScore):
        AFLEngine().fit(rows + [{**rows[0], "home_goals": None}])
    with pytest.raises(InsufficientData):
        AFLEngine().fit(rows[:20])
