"""Unit tests for distributional regression, Student-t joint scores, and quantile reconstruction."""

import numpy as np
import pytest

from runtime.src.common.distributional import (
    NegativeBinomialCountRegressor,
    StudentTJointScoreModel,
    QuantileDistributionReconstructor
)


def test_negative_binomial_count_regressor():
    np.random.seed(42)
    n = 150
    X = np.ones((n, 2))
    X[:, 1] = np.random.uniform(0.5, 2.0, size=n)
    
    # Generate overdispersed counts
    mu_true = np.exp(0.5 + 0.8 * X[:, 1])
    y = np.random.negative_binomial(5, 5 / (5 + mu_true))

    model = NegativeBinomialCountRegressor()
    model.fit(X, y)

    preds = model.predict_mean(X[:5])
    assert len(preds) == 5
    assert np.all(preds > 0.0)

    pmf = model.predict_pmf(X[0], max_count=20)
    assert np.isclose(np.sum(pmf), 1.0, atol=1e-3)


def test_student_t_joint_score_model():
    model = StudentTJointScoreModel(df=4.0)
    dist = model.generate_distribution(
        mu_h=105.0,
        mu_a=100.0,
        sigma_h=11.0,
        sigma_a=11.0,
        rho=0.20,
        min_score=60,
        max_score=150
    )

    assert np.isclose(np.sum(dist.grid), 1.0, atol=1e-3)
    p_h = dist.p_home_win()
    p_a = dist.p_away_win()
    assert p_h > p_a  # 105 > 100

    # Total over 204.5
    p_over = dist.p_over(204.5)
    assert 0.0 < p_over < 1.0


def test_quantile_distribution_reconstructor():
    reconstructor = QuantileDistributionReconstructor(quantiles=[0.10, 0.50, 0.90])
    
    # Crossed quantiles: 10th is higher than 50th
    crossed = np.array([45.0, 42.0, 55.0])
    fixed = reconstructor.fix_crossing(crossed)

    assert fixed[0] <= fixed[1] <= fixed[2]

    # Probability above threshold
    p_above_50 = reconstructor.to_probabilities_above(fixed, 50.0)
    assert 0.0 <= p_above_50 <= 1.0
