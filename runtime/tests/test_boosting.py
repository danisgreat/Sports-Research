"""Dependency-free gradient boosting for distribution parameters (ML-06)."""

import numpy as np
import pytest

from runtime.src.common import artifacts
from runtime.src.common.boosting import Binner, GaussianBoost, LogVarianceBoost, PoissonBoost
from runtime.src.common.distributional import NegativeBinomialCountRegressor
from runtime.src.common.errors import InsufficientData, NotFitted


def interaction_data(n=4000, seed=0):
    rng = np.random.default_rng(seed)
    X = rng.normal(0, 1, (n, 4))
    log_mu = 0.3 + 0.6 * X[:, 0] * (X[:, 1] > 0) - 0.5 * (X[:, 2] > 0.5)           # a threshold and an interaction a linear model misses
    y = rng.poisson(np.exp(log_mu)).astype(float)
    return X, y, np.exp(log_mu)


def poisson_deviance(y, mu):
    return float(np.mean(mu - y * np.log(np.maximum(mu, 1e-12))))


def test_poisson_boost_beats_a_linear_count_model_on_nonlinear_data():
    X, y, mu_true = interaction_data()
    Xtr, ytr, Xte, yte, mu_te = X[:3000], y[:3000], X[3000:], y[3000:], mu_true[3000:]
    boost = PoissonBoost(n_estimators=300, learning_rate=0.08, max_depth=3, seed=1).fit(Xtr, ytr)
    glm = NegativeBinomialCountRegressor(l2_reg=0.01).fit(np.column_stack([np.ones(3000), Xtr]), ytr)
    glm_mu = glm.predict_mean(np.column_stack([np.ones(len(Xte)), Xte]))
    boost_mu = boost.predict(Xte)
    assert poisson_deviance(yte, boost_mu) < poisson_deviance(yte, glm_mu) - 0.01
    assert np.corrcoef(boost_mu, mu_te)[0, 1] > 0.85 and boost_mu.min() > 0
    assert 5 < boost.best_iteration <= 300 and len(boost.validation_curve) >= boost.best_iteration


def test_early_stopping_uses_the_last_rows_chronologically_and_stops():
    rng = np.random.default_rng(3)
    X = rng.normal(0, 1, (2000, 3))
    y = rng.poisson(np.full(2000, 2.0)).astype(float)                              # pure noise: nothing to learn
    boost = PoissonBoost(n_estimators=500, learning_rate=0.1, patience=10, seed=0).fit(X, y)
    assert boost.best_iteration < 60 and len(boost.validation_curve) < 100


def test_gaussian_mean_and_heteroscedastic_width():
    rng = np.random.default_rng(5)
    n = 6000
    X = rng.uniform(-1, 1, (n, 3))
    sd_true = 5.0 + 6.0 * (X[:, 0] > 0)
    y = 100 + 8 * X[:, 1] + rng.normal(0, sd_true)
    mean = GaussianBoost(n_estimators=200, learning_rate=0.08, seed=2).fit(X[:4500], y[:4500])
    mu_tr = mean.predict(X[:4500])
    width = LogVarianceBoost(n_estimators=200, learning_rate=0.08, seed=2).fit(X[:4500], (y[:4500] - mu_tr) ** 2)
    sd_te = width.predict_sd(X[4500:])
    assert abs(float(np.mean(mean.predict(X[4500:]) - y[4500:]))) < 0.5
    high, low = sd_te[X[4500:, 0] > 0].mean(), sd_te[X[4500:, 0] <= 0].mean()
    assert high > 1.5 * low and high == pytest.approx(11.0, rel=0.25) and low == pytest.approx(5.0, rel=0.25)


def test_determinism_and_artifact_roundtrip(tmp_path):
    X, y, _ = interaction_data(n=1500)
    a = PoissonBoost(n_estimators=40, seed=7).fit(X, y)
    b = PoissonBoost(n_estimators=40, seed=7).fit(X, y)
    np.testing.assert_array_equal(a.predict(X[:50]), b.predict(X[:50]))
    path = str(tmp_path / "boost.json")
    artifacts.save(a, path, {"notes": "test"})
    loaded = artifacts.load(path)
    np.testing.assert_allclose(loaded.predict(X[:50]), a.predict(X[:50]))


def test_missing_values_have_their_own_bin_and_inputs_are_validated():
    X, y, _ = interaction_data(n=2000)
    X_nan = X.copy()
    X_nan[::7, 0] = np.nan
    boost = PoissonBoost(n_estimators=30, seed=1).fit(X_nan, y)
    assert np.isfinite(boost.predict(X_nan[:100])).all()
    binned = Binner().fit(X_nan).transform(X_nan)
    assert (binned[::7, 0] == 0).all() and (binned[1::7, 0] > 0).all()
    with pytest.raises(NotFitted):
        PoissonBoost().predict(X[:5])
    with pytest.raises(InsufficientData):
        PoissonBoost().fit(X[:50], y[:50])
    with pytest.raises(ValueError):
        PoissonBoost().fit(X, -np.abs(y) - 1)
    with pytest.raises(ValueError):
        PoissonBoost(learning_rate=0)
    with pytest.raises(ValueError):
        LogVarianceBoost().fit(X, -np.ones(len(X)))


def test_offset_lets_the_boost_correct_an_existing_model():
    X, y, mu_true = interaction_data(n=4000, seed=4)
    offset = np.log(np.full(len(y), 1.2))                                          # a crude engine rate
    plain = PoissonBoost(n_estimators=200, learning_rate=0.08, seed=1).fit(X[:3000], y[:3000], offset[:3000])
    corrected = plain.predict(X[3000:], offset[3000:])
    assert poisson_deviance(y[3000:], corrected) < poisson_deviance(y[3000:], np.full(1000, 1.2)) - 0.01
