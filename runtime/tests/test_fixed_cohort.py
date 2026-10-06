"""Unit tests for fixed-cohort comparative evaluation."""

import numpy as np
import pytest

from runtime.src.common.evaluation import FixedCohortEvaluator


def test_fixed_cohort_promotion_pass():
    np.random.seed(42)
    n = 100
    y_true = np.random.binomial(1, 0.6, size=n)
    
    # Baseline is noisy around 0.55
    p_base = np.clip(np.random.normal(0.55, 0.15, size=n), 0.1, 0.9)
    # Candidate has genuine skill and matches true probability
    p_cand = np.clip(y_true * 0.4 + 0.4 + np.random.normal(0, 0.05, size=n), 0.1, 0.9)

    res = FixedCohortEvaluator.evaluate(y_true, p_cand, p_base)
    assert res["n_samples"] == n
    assert res["delta_brier"] < -0.010
    assert res["delta_log_loss"] < 0.0
    assert res["is_promotable"] is True


def test_fixed_cohort_promotion_fail_on_log_loss():
    n = 50
    y_true = np.array([1] * 25 + [0] * 25)
    p_base = np.array([0.6] * 25 + [0.4] * 25)
    # Candidate makes one extreme overconfident wrong prediction
    p_cand = p_base.copy()
    p_cand[0] = 0.0001  # True is 1! Huge log loss explosion

    res = FixedCohortEvaluator.evaluate(y_true, p_cand, p_base)
    assert res["delta_log_loss"] > 0.0
    assert res["is_promotable"] is False
    assert any("LogLoss" in r for r in res["promotion_reasons"])
