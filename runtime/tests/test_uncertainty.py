"""Block bootstrap, Wilson, Cox calibration and power helpers."""

import numpy as np
import pytest

from runtime.src.common.calibration import compute_calibration_slope
from runtime.src.common.errors import FitFailed
from runtime.src.common.uncertainty import (
    block_bootstrap, block_indices, cox_calibration, group_rows, percentile_interval, power_summary, week_block_ids, wilson_interval,
)


def test_a_block_resample_is_a_union_of_whole_blocks():
    ids = np.array(["a"] * 3 + ["b"] * 5 + ["c"] * 2)
    groups = group_rows(ids)
    rng = np.random.default_rng(0)
    for _ in range(50):
        rows = block_indices(ids, rng, groups)
        counts = {label: int(np.sum(ids[rows] == label)) for label in "abc"}
        assert counts["a"] % 3 == 0 and counts["b"] % 5 == 0 and counts["c"] % 2 == 0          # blocks arrive intact
        assert set(counts) == {"a", "b", "c"}


def test_block_bootstrap_validates_lengths_and_is_reproducible():
    x = np.arange(20, dtype=float)
    ids = np.repeat(np.arange(5), 4)
    a = block_bootstrap(np.mean, [x], ids, 100, seed=3)
    b = block_bootstrap(np.mean, [x], ids, 100, seed=3)
    np.testing.assert_array_equal(a, b)
    assert abs(a.mean() - x.mean()) < 1.5
    with pytest.raises(ValueError):
        block_bootstrap(np.mean, [x[:10]], ids, 10)
    lo, hi = percentile_interval(a)
    assert lo < x.mean() < hi


def test_wilson_interval_matches_known_values():
    lo, hi = wilson_interval(8, 10)
    assert lo == pytest.approx(0.4902, abs=2e-3) and hi == pytest.approx(0.9433, abs=2e-3)       # standard Wilson 95% for 8/10
    assert wilson_interval(0, 0) == (0.0, 1.0)
    lo, hi = wilson_interval(0, 20)
    assert lo == 0.0 and 0.0 < hi < 0.2


def test_cox_calibration_agrees_with_the_bfgs_slope_and_never_returns_a_default():
    rng = np.random.default_rng(5)
    z = rng.normal(0, 1.2, 800)
    y = (rng.random(800) < 1 / (1 + np.exp(-0.5 * z))).astype(float)
    p = 1 / (1 + np.exp(-z))
    alpha, beta = cox_calibration(y, p)
    a2, b2 = compute_calibration_slope(y, p)
    assert beta == pytest.approx(b2, abs=0.02) and alpha == pytest.approx(a2, abs=0.02) and 0.3 < beta < 0.75
    with pytest.raises(FitFailed):
        cox_calibration(np.array([1.0, 1.0, 0.0]), np.array([0.5, 0.5, 0.5]), max_iter=0)


def test_power_summary():
    boot = np.random.default_rng(1).normal(-0.02, 0.01, 2000)
    summary = power_summary(-0.02, boot)
    assert summary["standard_error"] == pytest.approx(0.01, rel=0.1)
    assert summary["power_at_observed"] == pytest.approx(0.64, abs=0.08)             # z = 2 vs 1.645 critical value
    assert summary["minimum_detectable_delta"] == pytest.approx(-0.0249, abs=0.004)
    assert np.isnan(power_summary(0.0, np.zeros(10))["power_at_observed"])


def test_week_blocks_use_iso_weeks():
    assert list(week_block_ids(["2026-01-01", "2026-01-05"])) == ["2026-W01", "2026-W02"]
