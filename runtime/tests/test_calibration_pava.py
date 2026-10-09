"""ML-01 / ML-02: the isotonic calibrator is a correct weighted PAVA and fits fail loudly."""

import numpy as np
import pytest

from runtime.src.common import calibration
from runtime.src.common.calibration import IsotonicCalibrator, PlattScaler, TemperatureScaler, compute_calibration_slope, pava
from runtime.src.common.errors import FitFailed, NotFitted


def minmax_isotonic(y, w):
    """Independent reference: the max-min formula for the isotonic regression solution."""
    n = len(y)
    out = np.empty(n)
    for i in range(n):
        best = -np.inf
        for s in range(i + 1):
            low = np.inf
            for t in range(i, n):
                avg = np.sum(w[s:t + 1] * y[s:t + 1]) / np.sum(w[s:t + 1])
                low = min(low, avg)
            best = max(best, low)
        out[i] = best
    return out


def test_the_documented_counterexample_gives_one_third():
    # y = [1, 0, 0] against increasing p: the old routine returned 0.382, PAVA gives 1/3.
    cal = IsotonicCalibrator().fit(np.array([0.2, 0.5, 0.8]), np.array([1, 0, 0]))
    assert cal.y_vals == pytest.approx([1 / 3, 1 / 3, 1 / 3], abs=1e-12)


def test_matches_reference_on_1000_random_fits_and_is_monotone():
    rng = np.random.default_rng(20261009)
    for _ in range(1000):
        n = int(rng.integers(2, 25))
        values = rng.random(n).round(int(rng.integers(1, 4)))     # frequent ties in x
        outcomes = (rng.random(n) < rng.random()).astype(float)
        cal = IsotonicCalibrator().fit(values, outcomes)
        assert np.all(np.diff(cal.y_vals) >= -1e-15)
        # reference on the merged (unique-x) problem
        ux, inv, counts = np.unique(values, return_inverse=True, return_counts=True)
        mean_y = np.bincount(inv, weights=outcomes) / counts
        assert cal.x_vals == pytest.approx(ux, abs=0)
        assert cal.y_vals == pytest.approx(minmax_isotonic(mean_y, counts.astype(float)), abs=1e-12)
        assert np.all(np.diff(cal.predict(np.sort(values))) >= -1e-12)


def test_pava_weights_are_counted_once_and_reduce_to_the_mean():
    fitted = pava(np.array([1.0, 0.0, 0.0, 0.0]), np.ones(4))
    assert fitted == pytest.approx([0.25] * 4, abs=1e-15)
    fitted = pava(np.array([0.9, 0.1, 0.5]), np.array([1.0, 3.0, 1.0]))
    assert fitted == pytest.approx([0.3, 0.3, 0.5], abs=1e-15)


def test_tied_probabilities_are_order_independent():
    p = np.array([0.3, 0.3, 0.3, 0.7, 0.7])
    a = IsotonicCalibrator().fit(p, np.array([1, 0, 0, 1, 1]))
    b = IsotonicCalibrator().fit(p, np.array([0, 0, 1, 1, 1]))
    assert a.y_vals == pytest.approx(b.y_vals, abs=1e-15)


def test_predict_before_fit_raises_and_bad_inputs_are_rejected():
    with pytest.raises(NotFitted):
        IsotonicCalibrator().predict(np.array([0.5]))
    with pytest.raises(ValueError):
        IsotonicCalibrator().fit(np.array([0.2, 1.4]), np.array([0, 1]))
    with pytest.raises(ValueError):
        IsotonicCalibrator().fit(np.array([0.2, 0.4]), np.array([0, 2]))
    with pytest.raises(ValueError):
        PlattScaler().fit(np.array([]), np.array([]))


class _Failed:
    success = False
    message = "forced failure"
    x = np.zeros(2)
    jac = np.array([5.0, 5.0])


@pytest.mark.parametrize("fit", [
    lambda: PlattScaler().fit(np.array([0.2, 0.6, 0.8]), np.array([0, 1, 1])),
    lambda: TemperatureScaler().fit(np.array([0.2, 0.6, 0.8]), np.array([0, 1, 1])),
    lambda: compute_calibration_slope(np.array([0, 1, 1]), np.array([0.2, 0.6, 0.8])),
])
def test_optimiser_failure_raises_instead_of_returning_defaults(monkeypatch, fit):
    monkeypatch.setattr(calibration, "minimize", lambda *a, **k: _Failed())
    with pytest.raises(FitFailed, match="forced failure"):
        fit()
