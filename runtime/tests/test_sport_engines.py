"""Unit tests for all 8 sport predictive engines and contract derivation."""

import numpy as np
import pytest

from runtime.src.sports.cricket.engine import CricketEngine
from runtime.src.sports.basketball.engine import BasketballEngine
from runtime.src.sports.nfl.engine import NFLEngine
from runtime.src.sports.baseball.engine import BaseballEngine
from runtime.src.sports.afl.engine import AFLEngine
from runtime.src.sports.nrl.engine import NRLEngine
from runtime.src.sports.soccer.engine import SoccerEngine
from runtime.src.sports.nhl.engine import NHLEngine
from runtime.src.common.identity import ContractType


def test_cricket_engine():
    engine = CricketEngine().fit({})
    dist = engine.predict_distribution({"format": "t20", "pitch_run_factor": 1.05})
    assert np.isclose(np.sum(dist.grid), 1.0, atol=1e-3)

    contracts = engine.evaluate_contracts(dist, [
        {"type": "moneyline", "side": "home"},
        {"type": "total", "side": "over", "line": 330.5}
    ])
    assert len(contracts) == 2
    assert 0.0 < contracts[0].stated_prob < 1.0
    assert 0.0 < contracts[1].stated_prob < 1.0


def test_basketball_engine():
    engine = BasketballEngine().fit({})
    dist = engine.predict_distribution({"pace": 101.5, "home_off_rating": 1.15, "away_off_rating": 1.10})
    assert np.isclose(np.sum(dist.grid), 1.0, atol=1e-3)

    contracts = engine.evaluate_contracts(dist, [
        {"type": "spread", "side": "home", "line": -4.5},
        {"type": "total", "side": "under", "line": 228.5}
    ])
    assert len(contracts) == 2
    assert 0.0 < contracts[0].stated_prob < 1.0


def test_nfl_engine():
    engine = NFLEngine().fit({})
    dist = engine.predict_distribution({"home_p_td": 0.25, "home_p_fg": 0.18})
    assert np.isclose(np.sum(dist.grid), 1.0, atol=1e-3)

    contracts = engine.evaluate_contracts(dist, [
        {"type": "spread", "side": "home", "line": -3.5},
        {"type": "spread", "side": "home", "line": -6.5},
        {"type": "total", "side": "over", "line": 44.5}
    ])
    # Monotonicity check across key numbers: P(Home covers -3.5) >= P(Home covers -6.5)
    p_cov_3 = contracts[0].stated_prob
    p_cov_6 = contracts[1].stated_prob
    assert p_cov_6 <= p_cov_3 + 1e-9


def test_baseball_engine():
    engine = BaseballEngine().fit({})
    dist = engine.predict_distribution({"away_sp_ra9": 3.5, "home_sp_ra9": 4.2})
    assert np.isclose(np.sum(dist.grid), 1.0, atol=1e-3)

    contracts = engine.evaluate_contracts(dist, [
        {"type": "moneyline", "side": "home"},
        {"type": "spread", "side": "home", "line": 1.5},
        {"type": "total", "side": "under", "line": 8.5}
    ])
    p_home_ml = contracts[0].stated_prob
    p_home_plus_1_5 = contracts[1].stated_prob
    # Covering pair invariant: P(Home +1.5) >= P(Home ML)
    assert p_home_plus_1_5 >= p_home_ml - 1e-9


def test_afl_engine():
    engine = AFLEngine().fit({})
    dist = engine.predict_distribution({"home_expected_shots": 25.0, "away_expected_shots": 21.0})
    assert np.isclose(np.sum(dist.grid), 1.0, atol=1e-3)

    contracts = engine.evaluate_contracts(dist, [
        {"type": "moneyline", "side": "home"},
        {"type": "total", "side": "over", "line": 165.5}
    ])
    assert contracts[0].stated_prob > 0.50


def test_nrl_engine():
    engine = NRLEngine().fit({})
    dist = engine.predict_distribution({"home_expected_tries": 4.0, "away_expected_tries": 3.0})
    assert np.isclose(np.sum(dist.grid), 1.0, atol=1e-3)

    contracts = engine.evaluate_contracts(dist, [
        {"type": "moneyline", "side": "home"},
        {"type": "total", "side": "over", "line": 39.5}
    ])
    assert contracts[0].stated_prob > 0.50


def test_soccer_engine():
    engine = SoccerEngine().fit({})
    dist = engine.predict_distribution({"home_xg": 1.8, "away_xg": 0.9})
    assert np.isclose(np.sum(dist.grid), 1.0, atol=1e-3)

    contracts = engine.evaluate_contracts(dist, [
        {"type": "moneyline", "side": "home"},
        {"type": "moneyline", "side": "draw"},
        {"type": "moneyline", "side": "away"},
        {"type": "double_chance", "side": "1X"},
        {"type": "btts", "side": "yes"},
        {"type": "total", "side": "over", "line": 2.5}
    ])
    assert len(contracts) == 6
    p_h = contracts[0].stated_prob
    p_d = contracts[1].stated_prob
    p_1x = contracts[3].stated_prob
    assert np.isclose(p_1x, p_h + p_d, atol=1e-5)


def test_nhl_engine():
    engine = NHLEngine().fit({})
    dist = engine.predict_distribution({"home_xg": 3.2, "away_xg": 2.7, "empty_net_rate": 0.22})
    assert np.isclose(np.sum(dist.grid), 1.0, atol=1e-3)

    contracts = engine.evaluate_contracts(dist, [
        {"type": "moneyline", "side": "home"},
        {"type": "spread", "side": "home", "line": 1.5},
        {"type": "total", "side": "over", "line": 5.5}
    ])
    assert len(contracts) == 3
    assert contracts[1].stated_prob >= contracts[0].stated_prob - 1e-9


def test_soccer_engine_fit_and_serialization(tmp_path):
    """Verify fitting match records to SoccerEngine and persisting artifact."""
    engine = SoccerEngine(xi=0.002, l2_reg=0.05)
    train_matches = [
        {"home": "Liverpool", "away": "Chelsea", "home_goals": 2, "away_goals": 1, "days_ago": 5},
        {"home": "Chelsea", "away": "Liverpool", "home_goals": 1, "away_goals": 1, "days_ago": 20},
        {"home": "Arsenal", "away": "Liverpool", "home_goals": 0, "away_goals": 2, "days_ago": 15},
    ]
    engine.fit(train_matches)
    assert engine.is_fitted
    assert "Liverpool" in engine.dixon_coles.team_idx

    dist1 = engine.predict_distribution({"home_team": "Liverpool", "away_team": "Chelsea"})
    assert np.isclose(np.sum(dist1.grid), 1.0, atol=1e-4)

    # Test serialization roundtrip
    model_path = str(tmp_path / "soccer_dixon_coles.pkl")
    engine.save_artifact(model_path)

    loaded = SoccerEngine.load_artifact(model_path)
    assert loaded.is_fitted
    dist2 = loaded.predict_distribution({"home_team": "Liverpool", "away_team": "Chelsea"})
    np.testing.assert_allclose(dist1.grid, dist2.grid)


def test_sport_engines_empirical_fit_and_serialization(tmp_path):
    """Verify empirical parameter estimation and serialization across all sport engines."""
    # AFL
    afl_matches = [
        {"home_team": "Collingwood", "away_team": "Carlton", "home_shots": 26, "away_shots": 20, "home_goals": 15, "away_goals": 10},
        {"home_team": "Carlton", "away_team": "Collingwood", "home_shots": 22, "away_shots": 24, "home_goals": 11, "away_goals": 13},
    ] * 3
    afl = AFLEngine().fit(afl_matches)
    assert afl.is_fitted
    assert "Collingwood" in afl.team_attack_ratings
    p_afl = afl.save_artifact(str(tmp_path / "afl.pkl"))
    loaded_afl = AFLEngine.load_artifact(str(tmp_path / "afl.pkl"))
    assert loaded_afl.is_fitted

    # NRL
    nrl_matches = [
        {"home_team": "Penrith", "away_team": "Broncos", "home_tries": 5, "away_tries": 2, "home_conversions": 4, "away_conversions": 2},
        {"home_team": "Broncos", "away_team": "Penrith", "home_tries": 3, "away_tries": 4, "home_conversions": 2, "away_conversions": 3},
    ] * 3
    nrl = NRLEngine().fit(nrl_matches)
    assert nrl.is_fitted
    assert "Penrith" in nrl.team_attack_tries

    # Baseball
    bb_matches = [
        {"home_team": "NYY", "away_team": "BOS", "home_runs": 6, "away_runs": 3},
        {"home_team": "BOS", "away_team": "NYY", "home_runs": 4, "away_runs": 5},
    ] * 3
    bb = BaseballEngine().fit(bb_matches)
    assert bb.is_fitted
    assert "NYY" in bb.team_offense_ratings

    # Basketball
    bk_matches = [
        {"home_team": "LAL", "away_team": "BOS", "home_score": 118, "away_score": 112},
        {"home_team": "BOS", "away_team": "LAL", "home_score": 115, "away_score": 110},
    ] * 3
    bk = BasketballEngine().fit(bk_matches)
    assert bk.is_fitted
    assert "LAL" in bk.team_off_ratings

    # Cricket
    crick_matches = [
        {"format": "t20", "home_team": "IND", "away_team": "AUS", "runs": 185},
        {"format": "t20", "home_team": "AUS", "away_team": "IND", "runs": 175},
    ] * 3
    crick = CricketEngine().fit(crick_matches)
    assert crick.is_fitted
    assert "IND" in crick.team_batting_ratings

    # NHL
    nhl_matches = [
        {"home_team": "EDM", "away_team": "TOR", "home_goals": 4, "away_goals": 2},
        {"home_team": "TOR", "away_team": "EDM", "home_goals": 3, "away_goals": 4},
    ] * 3
    nhl = NHLEngine().fit(nhl_matches)
    assert nhl.is_fitted
    assert "EDM" in nhl.team_scoring_factors

    # NFL
    nfl_matches = [
        {"home_team": "KC", "away_team": "BUF", "home_score": 27, "away_score": 24},
        {"home_team": "BUF", "away_team": "KC", "home_score": 24, "away_score": 21},
    ] * 3
    nfl = NFLEngine().fit(nfl_matches)
    assert nfl.is_fitted
    assert "KC" in nfl.team_off_ratings



