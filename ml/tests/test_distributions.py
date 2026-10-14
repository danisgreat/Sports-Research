"""Coherence checks C-ML-01 to C-ML-05 (negative fixture + legitimate edge case each), plus scoring identities."""
import numpy as np
import pytest

from ml.core.distributions import CoherenceError, Masses, ScoreGrid, discrete_crps, normal_crps


# C-ML-01 masses sum to one
def test_c_ml_01_rejects_masses_not_summing_to_one():
    with pytest.raises(CoherenceError):
        ScoreGrid(np.array([[0.55, 0.10], [0.30, 0.0]]))


def test_c_ml_01_accepts_normalised_grid():
    g = ScoreGrid(np.array([[0.25, 0.25], [0.25, 0.25]]))
    assert abs(g.p.sum() - 1) < 1e-12


# C-ML-02 decisive probability
def test_c_ml_02_decisive_is_win_over_win_plus_loss():
    m = Masses(0.55, 0.10, 0.35)
    assert m.p_decisive == pytest.approx(11 / 18)
    assert m.p_decisive != pytest.approx(0.55)  # the negative fixture: W alone is not p_decisive


def test_c_ml_02_all_push_is_not_computed():
    assert Masses(0.0, 1.0, 0.0).p_decisive is None


# C-ML-03 lattice support and parity
def test_c_ml_03_negative_support_rejected():
    with pytest.raises(CoherenceError):
        ScoreGrid(np.array([[1.0]]), h0=-1)


def test_c_ml_03_parity_holds_on_lattice():
    g = ScoreGrid.poisson(1.4, 1.1, rho=-0.05)
    mv, mp = g.margin_pmf()
    tv, tp = g.total_pmf()
    assert mp[mv % 2 == 1].sum() == pytest.approx(tp[tv % 2 == 1].sum())  # T and M share parity
    assert g.winner()[1] > 0  # 0-0 style draws keep mass (edge case)


# C-ML-04 ladder monotonicity
def test_c_ml_04_total_ladder_monotone():
    g = ScoreGrid.bivariate_normal(110, 105, np.array([[140, 30], [30, 130]]))
    overs = [g.total(L).win for L in (200.5, 210.5, 215.5, 220.5, 230.5)]
    assert all(a >= b for a, b in zip(overs, overs[1:]))


def test_c_ml_04_equal_masses_where_no_support_between_lines():
    g = ScoreGrid.poisson(1.3, 1.0)
    assert g.total(2.25).win == pytest.approx(g.total(2.75).win)


# C-ML-05 covering pair
def test_c_ml_05_plus_handicap_covers_at_least_winner():
    g = ScoreGrid.bivariate_normal(100, 98, np.array([[150, 40], [40, 140]]))
    assert g.handicap(1.5).win >= g.winner()[0]
    assert g.handicap(-1.5).win <= g.winner()[0]


def test_whole_line_push_mass_is_exact():
    g = ScoreGrid.poisson(1.5, 1.2)
    m = g.handicap(0.0)
    assert m.push == pytest.approx(g.winner()[1])
    assert m.win + m.push + m.loss == pytest.approx(1.0)


def test_resolve_ties_conserves_mass_and_removes_draws():
    g = ScoreGrid.bivariate_normal(100, 100, np.array([[120, 30], [30, 120]]))
    r = g.resolve_ties(0.6, residual_draw=0.0, winner_bonus=3, both_bonus=10)
    assert r.p.sum() == pytest.approx(1.0)
    assert r.winner()[1] == pytest.approx(0.0, abs=1e-12)
    assert r.winner()[0] - g.winner()[0] == pytest.approx(0.6 * g.winner()[1], rel=1e-9)


def test_reweight_winner_hits_targets_and_moves_totals():
    p = np.zeros((3, 3))
    p[2, 0], p[1, 0], p[0, 1], p[1, 1] = 0.45, 0.25, 0.20, 0.10
    g = ScoreGrid(p)
    q = g.reweight_winner((0.60, 0.15, 0.25))
    assert q.winner() == pytest.approx((0.60, 0.15, 0.25))
    # the October 12 recommendation's example: Over 1.5 moves from 0.55 to 15/28
    assert g.total(1.5).win == pytest.approx(0.55)
    assert q.total(1.5).win == pytest.approx(15 / 28)


def test_reweight_refuses_mass_on_empty_class():
    g = ScoreGrid(np.array([[0.0, 0.0], [1.0, 0.0]]))
    with pytest.raises(CoherenceError):
        g.reweight_winner((0.5, 0.25, 0.25))


def test_discrete_crps_close_to_normal_crps():
    from scipy import stats
    k = np.arange(0, 301)
    pmf = np.diff(stats.norm.cdf(np.append(k, 301) - 0.5, 150, 20))
    assert discrete_crps(k, pmf / pmf.sum(), 171) == pytest.approx(float(normal_crps(150, 20, 171)), rel=0.03)


def test_dixon_coles_tau_rejects_invalid_rho():
    with pytest.raises(CoherenceError):
        ScoreGrid.poisson(3.0, 3.0, rho=0.2)


def test_dixon_coles_rho_clamped_into_valid_domain():
    lo, hi = ScoreGrid.rho_domain(5.0, 0.4)
    assert lo == pytest.approx(-0.2)
    g = ScoreGrid.poisson(5.0, 0.4, rho=-0.25, clamp_rho=True)  # legitimate edge: clamped, valid grid
    assert g.p.sum() == pytest.approx(1.0) and np.all(g.p >= 0)
    with pytest.raises(CoherenceError):
        ScoreGrid.poisson(5.0, 0.4, rho=-0.25)  # negative fixture: no silent repair without the flag path
