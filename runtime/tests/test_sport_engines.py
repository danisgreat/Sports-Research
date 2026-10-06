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

