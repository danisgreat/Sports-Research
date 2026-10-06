"""Unit tests for Elo and Draw-Aware Bradley-Terry rating engines."""

import numpy as np
import pytest

from runtime.src.common.ratings import EloRatingEngine, BradleyTerryDrawEngine


def test_elo_engine_basic_updates():
    engine = EloRatingEngine(base_rating=1500.0, k_factor=32.0, home_advantage=50.0)
    
    # Pre-match probability with home advantage
    p_h = engine.predict_prob("TeamA", "TeamB", is_neutral=False)
    assert p_h > 0.50

    # TeamA wins
    r_a_new, r_b_new = engine.update("TeamA", "TeamB", score_a=1.0, is_neutral=False)
    assert r_a_new > 1500.0
    assert r_b_new < 1500.0


def test_bradley_terry_draw_engine():
    engine = BradleyTerryDrawEngine(l2_reg=0.05)
    matches = [
        {"home": "Arsenal", "away": "Chelsea", "result": "home"},
        {"home": "Liverpool", "away": "Arsenal", "result": "draw"},
        {"home": "Chelsea", "away": "Liverpool", "result": "away"},
        {"home": "Arsenal", "away": "Liverpool", "result": "home"},
        {"home": "Liverpool", "away": "Chelsea", "result": "home"},
        {"home": "Chelsea", "away": "Arsenal", "result": "draw"},
    ]
    engine.fit(matches)

    p_h, p_d, p_a = engine.predict_probs("Arsenal", "Chelsea")
    assert np.isclose(p_h + p_d + p_a, 1.0, atol=1e-5)
    assert 0.0 < p_d < 1.0
    assert p_h > p_a  # Arsenal won H2H and more games
