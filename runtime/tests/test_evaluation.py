"""Unit tests for evaluation metrics and proper scoring rules."""

import numpy as np

from runtime.src.common.evaluation import (
    brier_score,
    multiclass_brier_score,
    log_loss,
    crps_score,
    murphy_decomposition
)


def test_brier_score():
    y_true = np.array([1, 0, 1, 0])
    y_prob = np.array([0.9, 0.1, 0.8, 0.2])
    # Errors: 0.1^2, 0.1^2, 0.2^2, 0.2^2 -> sum = 0.01 + 0.01 + 0.04 + 0.04 = 0.10 / 4 = 0.025
    assert np.isclose(brier_score(y_true, y_prob), 0.025)


def test_multiclass_brier():
    y_onehot = np.array([[1, 0, 0], [0, 1, 0]])
    y_probs = np.array([[0.7, 0.2, 0.1], [0.1, 0.8, 0.1]])
    score = multiclass_brier_score(y_onehot, y_probs)
    assert score >= 0.0


def test_log_loss():
    y_true = np.array([1, 0])
    y_prob = np.array([0.9, 0.1])
    loss = log_loss(y_true, y_prob)
    assert loss > 0.0
    assert np.isclose(loss, -np.log(0.9))


def test_crps_score():
    y_true = np.array([3.0, 5.0])
    thresholds = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    # Dummy CDF (monotonic non-decreasing)
    y_cdf = np.array([
        [0.1, 0.2, 0.5, 0.8, 0.9, 1.0],
        [0.0, 0.1, 0.2, 0.4, 0.7, 1.0]
    ])
    crps = crps_score(y_true, y_cdf, thresholds)
    assert crps >= 0.0


def test_murphy_decomposition():
    np.random.seed(123)
    y_true = np.random.binomial(1, 0.6, size=200)
    y_prob = np.random.uniform(0.3, 0.9, size=200)

    decomp = murphy_decomposition(y_true, y_prob, n_bins=5)
    # Binned Brier reconstruction = Reliability - Resolution + Uncertainty
    reconstructed = decomp["reliability"] - decomp["resolution"] + decomp["uncertainty"]
    assert np.isclose(decomp["binned_brier"], reconstructed, atol=1e-5)
    assert np.isclose(decomp["original_brier"], brier_score(y_true, y_prob), atol=1e-5)
    assert "within_bin_discrepancy" in decomp

