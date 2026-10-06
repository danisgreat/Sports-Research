"""Unit tests for Dixon-Coles model."""

import numpy as np
import pytest

from runtime.src.common.dixon_coles import DixonColesEngine


def test_dixon_coles_fitting_and_distribution():
    engine = DixonColesEngine(xi=0.002, l2_reg=0.05)
    matches = [
        {"home": "ManCity", "away": "Everton", "home_goals": 3, "away_goals": 0, "days_ago": 10},
        {"home": "Everton", "away": "ManCity", "home_goals": 0, "away_goals": 2, "days_ago": 40},
        {"home": "Arsenal", "away": "Everton", "home_goals": 2, "away_goals": 1, "days_ago": 15},
        {"home": "ManCity", "away": "Arsenal", "home_goals": 1, "away_goals": 1, "days_ago": 25},
        {"home": "Arsenal", "away": "ManCity", "home_goals": 0, "away_goals": 0, "days_ago": 60},
    ]
    engine.fit(matches)

    score_dist = engine.predict_score_distribution("ManCity", "Everton")
    grid = score_dist.grid

    # Probability mass must sum to 1.0
    assert np.isclose(np.sum(grid), 1.0, atol=1e-4)

    # City at home vs Everton should heavily favor City
    p_h = score_dist.p_home_win()
    p_a = score_dist.p_away_win()
    assert p_h > p_a

    # Low-score adjustment check
    tau_00 = DixonColesEngine.tau(0, 0, 1.5, 1.2, -0.04)
    assert tau_00 > 1.0  # - rho * lambda * mu increases 0-0 probability when rho is negative
