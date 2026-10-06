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

    # Parameter rho must be strictly within valid empirical bounds [-0.25, 0.25]
    assert -0.25 <= engine.rho <= 0.25

    # Verify all 4 low-score adjustment factors are strictly positive
    lambda_h = np.exp(engine.attacks[engine.team_idx["ManCity"]] + engine.defences[engine.team_idx["Everton"]] + engine.home_adv)
    mu_a = np.exp(engine.attacks[engine.team_idx["Everton"]] + engine.defences[engine.team_idx["ManCity"]])
    for (x, y) in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        assert DixonColesEngine.tau(x, y, lambda_h, mu_a, engine.rho) > 0.0


def test_dixon_coles_rejects_invalid_tau():
    """Verify that predicting with invalid dependence parameters raises ValueError rather than clipping."""
    engine = DixonColesEngine()
    engine.teams = ["TeamA", "TeamB"]
    engine.team_idx = {"TeamA": 0, "TeamB": 1}
    engine.attacks = np.array([0.5, -0.5])
    engine.defences = np.array([0.5, -0.5])
    engine.home_adv = 0.5
    engine.rho = -2.5  # Grossly invalid rho that produces tau <= 0

    with pytest.raises(ValueError, match="Invalid Dixon-Coles parameters"):
        engine.predict_score_distribution("TeamA", "TeamB")

