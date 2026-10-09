"""Distributional regression, Student-t joint scores and quantile reconstruction (ML-02, DST-15)."""

import numpy as np
import pytest
from scipy.stats import genpareto

from runtime.src.common.distributional import NegativeBinomialCountRegressor, QuantileDistributionReconstructor, StudentTJointScoreModel
from runtime.src.common.errors import FitFailed, InsufficientData, NotFitted


def synthetic(n=400, seed=42, r_true=5.0):
    rng = np.random.default_rng(seed)
    X = np.ones((n, 2))
    X[:, 1] = rng.uniform(0.5, 2.0, size=n)
    mu_true = np.exp(0.5 + 0.8 * X[:, 1])
    return X, rng.negative_binomial(r_true, r_true / (r_true + mu_true)), mu_true


def test_negative_binomial_regressor_recovers_mean_and_dispersion():
    X, y, mu_true = synthetic()
    model = NegativeBinomialCountRegressor(l2_reg=0.0).fit(X, y)
    assert model.coef[1] == pytest.approx(0.8, abs=0.15) and model.coef[0] == pytest.approx(0.5, abs=0.25)
    assert model.alpha == pytest.approx(1.0 / 5.0, rel=0.4)
    preds = model.predict_mean(X[:5])
    assert len(preds) == 5 and np.all(preds > 0.0)
    pmf = model.predict_pmf(X[0])
    assert pmf.sum() == pytest.approx(1.0) and (pmf * np.arange(len(pmf))).sum() == pytest.approx(preds[0], rel=1e-3)


def test_analytic_gradient_matches_finite_differences():
    from scipy.optimize import approx_fprime
    X, y, _ = synthetic(n=120)
    penalty = np.array([0.0, 0.3])
    params = np.array([0.4, 0.7, np.log(0.25)])
    _, grad = NegativeBinomialCountRegressor._objective(params, X, y, penalty)
    numeric = approx_fprime(params, lambda p: NegativeBinomialCountRegressor._objective(p, X, y, penalty)[0], 1e-6)
    np.testing.assert_allclose(grad, numeric, rtol=1e-4, atol=1e-4)


def test_intercept_is_unpenalised():
    X, y, _ = synthetic(n=200)
    heavy = NegativeBinomialCountRegressor(l2_reg=50.0).fit(X, y)
    assert abs(heavy.predict_mean(X).mean() - y.mean()) / y.mean() < 0.02      # the mean level survives a heavy ridge on the slope
    assert abs(heavy.coef[1]) < abs(NegativeBinomialCountRegressor(l2_reg=0.0).fit(X, y).coef[1])


def test_pmf_support_is_not_silently_truncated():
    X, y, _ = synthetic()
    model = NegativeBinomialCountRegressor().fit(X, y)
    big = np.array([1.0, 2.0])
    pmf = model.predict_pmf(big)
    assert pmf.sum() == pytest.approx(1.0, abs=1e-9) and 1.0 - pmf[:30].sum() > 1e-6          # the default support is wider than a fixed 30
    with pytest.raises(ValueError, match="drops"):
        model.predict_pmf(big, max_count=5)


def test_failures_are_loud_not_flat_models():
    with pytest.raises(NotFitted):
        NegativeBinomialCountRegressor().predict_mean(np.ones((1, 2)))
    with pytest.raises(InsufficientData):
        NegativeBinomialCountRegressor().fit(np.ones((3, 2)), np.array([1.0, 2.0, 3.0]))
    with pytest.raises(ValueError):
        NegativeBinomialCountRegressor().fit(np.ones((20, 2)), -np.ones(20))
    X, y, _ = synthetic(n=60)
    broken = NegativeBinomialCountRegressor()
    X_bad = X.copy()
    X_bad[:, 1] = 1e9                               # collinear with a giant scale: the optimiser cannot converge sensibly
    try:
        broken.fit(X_bad, y)
    except FitFailed:
        assert not broken.is_fitted
        with pytest.raises(NotFitted):
            broken.predict_mean(X[:1])


def test_student_t_joint_score_model():
    dist = StudentTJointScoreModel(df=4.0).generate_distribution(105.0, 100.0, 11.0, 11.0, 0.20, 30, 180, endpoint="full_game")
    assert dist.grid.sum() == pytest.approx(1.0, abs=1e-9) and dist.endpoint == "full_game"
    assert dist.p_home_win() > dist.p_away_win() and 0.0 < dist.p_over(204.5) < 1.0
    with pytest.raises(ValueError, match="widen"):
        StudentTJointScoreModel(df=3.0).generate_distribution(105.0, 100.0, 11.0, 11.0, 0.2, 90, 120)
    with pytest.raises(ValueError):
        StudentTJointScoreModel(df=2.0)
    with pytest.raises(ValueError):
        StudentTJointScoreModel().generate_distribution(100.0, 100.0, 11.0, 11.0, 1.0, 0, 200)


def test_rearrangement_removes_crossing():
    rec = QuantileDistributionReconstructor([0.10, 0.50, 0.90])
    fixed = rec.fix_crossing(np.array([45.0, 42.0, 55.0]))
    assert list(fixed) == [42.0, 45.0, 55.0]


def test_exponential_tail_is_exact_for_exponential_data():
    taus = [0.05, 0.25, 0.5, 0.75, 0.95]
    q = -np.log(1.0 - np.array(taus))                     # Exp(1) quantiles
    rec = QuantileDistributionReconstructor(taus)
    for t in (3.2, 4.0, 6.0):
        assert rec.survival(q, t) == pytest.approx(np.exp(-t), rel=1e-6)
    assert rec.survival(q, q[-1]) == pytest.approx(0.05, abs=1e-12)                                  # continuous at the knot


def test_gpd_tail_follows_the_stated_shape():
    taus = [0.5, 0.8, 0.9, 0.95]
    dist = genpareto(c=0.25, scale=2.0)
    q = dist.ppf(taus)
    rec = QuantileDistributionReconstructor(taus, tail_shape=0.25)
    for t in (dist.ppf(0.98), dist.ppf(0.995)):
        assert rec.survival(q, float(t)) == pytest.approx(float(dist.sf(t)), rel=0.02)
    exp_rec = QuantileDistributionReconstructor(taus)
    assert exp_rec.survival(q, float(dist.ppf(0.999))) < rec.survival(q, float(dist.ppf(0.999)))      # heavier tail is heavier


def test_tails_are_monotone_continuous_and_two_sided():
    taus = [0.1, 0.5, 0.9]
    q = np.array([40.0, 50.0, 62.0])
    for shape in (0.0, 0.2, -0.2):
        rec = QuantileDistributionReconstructor(taus, tail_shape=shape)
        grid = np.linspace(10.0, 120.0, 2001)
        s = np.array([rec.survival(q, float(t)) for t in grid])
        assert (np.diff(s) <= 1e-12).all() and 0.0 <= s.min() and s.max() <= 1.0
        assert np.abs(np.diff(s)).max() < 0.02                                                       # no jumps at the knots
        assert rec.survival(q, 40.0) == pytest.approx(0.9, abs=1e-12) and rec.survival(q, 62.0) == pytest.approx(0.1, abs=1e-12)
        assert s[0] > 0.9 and s[-1] < 0.1
    assert QuantileDistributionReconstructor(taus).to_probabilities_above(q, 50.0) == pytest.approx(0.5)


def test_ties_and_bad_levels():
    taus = [0.1, 0.5, 0.9]
    rec = QuantileDistributionReconstructor(taus)
    flat_top = np.array([40.0, 50.0, 50.0])
    assert 0.0 <= rec.survival(flat_top, 51.0) <= 0.5
    with pytest.raises(ValueError):
        QuantileDistributionReconstructor([0.5])
    with pytest.raises(ValueError):
        QuantileDistributionReconstructor([0.0, 0.5])
    with pytest.raises(ValueError):
        QuantileDistributionReconstructor(taus, tail_shape=1.5)
    with pytest.raises(ValueError):
        rec.survival(np.array([1.0, 2.0]), 1.5)
