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


def test_handicap_away_covering_exact():
    """Verify that a 10-3 Home win yields exactly 0.0% P(Away cover 0 handicap) and 100% P(Home cover 0)."""
    grid = np.zeros((11, 11), dtype=float)
    grid[10, 3] = 1.0  # 100% probability to Home=10, Away=3
    dist = ScoreDistribution(
        grid=grid,
        home_support=np.arange(11),
        away_support=np.arange(11)
    )

    # Away covering zero handicap must be strictly 0.0
    assert dist.p_away_cover(0.0) == 0.0
    # Home covering zero handicap must be strictly 1.0
    assert dist.p_home_cover(0.0) == 1.0

    # With +7.5 handicap, Away covers (3 - 10 + 7.5 = +0.5 > 0)
    assert dist.p_away_cover(7.5) == 1.0
    # With +6.5 handicap, Away fails to cover (3 - 10 + 6.5 = -0.5 < 0)
    assert dist.p_away_cover(6.5) == 0.0

    # Push spread checks
    assert dist.p_push_spread(7.0, side="away") == 1.0
    assert dist.p_push_spread(-7.0, side="home") == 1.0
    assert dist.p_push_spread(0.0, side="away") == 0.0


def test_negative_mass_rejection():
    """Verify that grids containing negative probability mass are strictly rejected."""
    grid = np.zeros((5, 5), dtype=float)
    grid[0, 0] = 1.2
    grid[0, 1] = -0.2  # Negative mass

    with pytest.raises(ValueError, match="negative probability mass"):
        ScoreDistribution(
            grid=grid,
            home_support=np.arange(5),
            away_support=np.arange(5)
        )


def test_nan_and_inf_rejection():
    """Verify that grids containing NaN or Inf are strictly rejected."""
    grid = np.zeros((5, 5), dtype=float)
    grid[0, 0] = np.nan
    with pytest.raises(ValueError, match="NaN or Inf"):
        ScoreDistribution(grid=grid, home_support=np.arange(5), away_support=np.arange(5))

    grid[0, 0] = np.inf
    with pytest.raises(ValueError, match="NaN or Inf"):
        ScoreDistribution(grid=grid, home_support=np.arange(5), away_support=np.arange(5))


def test_decoupled_match_winner():
    """Verify decoupled match winner probabilities (e.g. tennis sets vs games)."""
    grid = np.zeros((5, 5), dtype=float)
    grid[1, 4] = 1.0  # Away has more score in grid (e.g. 1 vs 4)
    dist = ScoreDistribution(
        grid=grid,
        home_support=np.arange(5),
        away_support=np.arange(5),
        p_match_home_win=0.648,
        p_match_away_win=0.352,
        p_match_draw=0.0
    )

    # Moneyline queries return the decoupled match winner probabilities
    assert dist.p_home_win() == 0.648
    assert dist.p_away_win() == 0.352

    # Score-based margin contracts still evaluate on the grid
    assert dist.p_home_cover(0.0) == 0.0  # Home (1 - 4 = -3) does not cover 0
    assert dist.p_away_cover(0.0) == 1.0  # Away (4 - 1 = +3) covers 0


