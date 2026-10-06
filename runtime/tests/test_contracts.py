"""Unit tests for event-first score distribution and derived contracts."""

import numpy as np
import pytest

from runtime.src.common.contracts import ScoreDistribution, DerivedContracts


def test_bivariate_poisson_score_distribution():
    # Construct soccer-like bivariate Poisson distribution
    dist = ScoreDistribution.from_bivariate_poisson(lambda1=1.6, lambda2=1.1, lambda3=0.1, max_score=10)
    
    p_h = dist.p_home_win()
    p_a = dist.p_away_win()
    p_d = dist.p_draw()

    # Probability partition must sum to 1.0
    assert np.isclose(p_h + p_a + p_d, 1.0, atol=1e-5)
    assert p_h > p_a  # Lambda1 > Lambda2

    # Double chance checks
    assert np.isclose(dist.p_double_chance("1X"), p_h + p_d)
    assert np.isclose(dist.p_double_chance("X2"), p_a + p_d)
    assert np.isclose(dist.p_double_chance("12"), p_h + p_a)

    # Draw No Bet checks
    dnb_h = dist.p_draw_no_bet("home")
    dnb_a = dist.p_draw_no_bet("away")
    assert np.isclose(dnb_h + dnb_a, 1.0)
    assert dnb_h > dnb_a


def test_monotonicity_and_covering_pair():
    dist = ScoreDistribution.from_bivariate_poisson(lambda1=2.0, lambda2=1.5, max_score=12)

    # Totals monotonicity across multiple lines
    lines = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
    assert DerivedContracts.verify_totals_monotonicity(dist, lines)

    # Spreads monotonicity
    spreads = [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5]
    assert DerivedContracts.verify_spread_monotonicity(dist, spreads)

    # Covering pair invariant: P(Home +1.5) >= P(Home ML)
    assert DerivedContracts.verify_covering_pair(dist, positive_spread=1.5)
    assert DerivedContracts.verify_covering_pair(dist, positive_spread=0.5)


def test_total_push_sum():
    dist = ScoreDistribution.from_bivariate_poisson(lambda1=1.5, lambda2=1.5, max_score=10)
    line = 3.0
    p_over = dist.p_over(line)
    p_under = dist.p_under(line)
    p_push = dist.p_push_total(line)

    assert np.isclose(p_over + p_under + p_push, 1.0, atol=1e-5)

