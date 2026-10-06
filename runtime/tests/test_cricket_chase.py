"""Unit tests for Cricket chase stopping rule."""

import numpy as np
import pytest

from runtime.src.sports.cricket.engine import CricketEngine


def test_cricket_chase_stopping_rule_bounds():
    engine = CricketEngine().fit({})
    # Predict distribution with stopping rule
    dist = engine.predict_distribution({
        "format": "t20",
        "home_batting_rating": 1.0,
        "away_batting_rating": 1.0,
        "apply_chase_stopping_rule": True
    })

    # Total grid probability mass must sum to 1.0
    assert np.isclose(np.sum(dist.grid), 1.0, atol=1e-3)

    # In a chase where Team 1 scores s1, Target is s1 + 1.
    # Therefore, Team 2's score s2 can NEVER exceed s1 + 1 under the stopping rule!
    # For every pair (s1, s2) where s2 > s1 + 1, grid[s1, s2] must be 0!
    for s1 in range(len(dist.home_support)):
        for s2 in range(s1 + 2, len(dist.away_support)):
            assert dist.grid[s1, s2] == 0.0, f"Violation: Team 2 scored {s2} chasing {s1+1} (prob: {dist.grid[s1, s2]})"


def test_cricket_unrestricted_comparison():
    engine = CricketEngine().fit({})
    # Without chase stopping rule (unrestricted)
    dist_unrestricted = engine.predict_distribution({
        "format": "t20",
        "apply_chase_stopping_rule": False
    })
    # In an unrestricted distribution, Away can score well above Home + 1
    # Check total probability mass where Away score s2 > Home score s1 + 1
    mask = dist_unrestricted.away_support > (dist_unrestricted.home_support[:, None] + 1)
    p_overshoot = float(np.sum(dist_unrestricted.grid[mask]))
    assert p_overshoot > 0.30, f"Unrestricted model should allow substantial mass where s2 > s1 + 1, got {p_overshoot}"
