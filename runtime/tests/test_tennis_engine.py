"""Unit tests for Tennis predictive engine."""

import numpy as np
import pytest

from runtime.src.sports.tennis.engine import TennisEngine
from runtime.src.common.contracts import DerivedContracts


def test_tennis_engine_hold_formula():
    # At p_serve = 0.50, hold prob should be 0.50
    assert np.isclose(TennisEngine.p_game_hold(0.50), 0.50, atol=1e-3)
    # Higher serve win prob implies higher hold prob
    assert TennisEngine.p_game_hold(0.65) > TennisEngine.p_game_hold(0.60)
    assert TennisEngine.p_game_hold(0.70) > 0.80


def test_tennis_engine_match_distribution():
    engine = TennisEngine().fit({})
    dist = engine.predict_distribution({
        "p_serve1": 0.67,
        "p_serve2": 0.61,
        "surface": "hard",
        "format": "best_of_3"
    })

    assert np.isclose(np.sum(dist.grid), 1.0, atol=1e-3)
    
    # Player 1 has higher serve rate -> should be favourite
    p_p1_win = dist.p_home_win()
    p_p2_win = dist.p_away_win()
    assert p_p1_win > p_p2_win

    # Derived contracts evaluation
    contracts = engine.evaluate_contracts(dist, [
        {"type": "moneyline", "side": "home"},
        {"type": "spread", "side": "home", "line": -2.5},
        {"type": "total", "side": "over", "line": 21.5}
    ])
    assert len(contracts) == 3
    assert 0.0 < contracts[0].stated_prob < 1.0
    assert 0.0 < contracts[1].stated_prob < 1.0
    assert 0.0 < contracts[2].stated_prob < 1.0

    # Covering pair check: P(Home +2.5 games) >= P(Home ML)
    p_plus_2_5 = dist.p_home_cover(2.5)
    assert p_plus_2_5 >= p_p1_win - 1e-9
