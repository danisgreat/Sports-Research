"""Unit tests for probability calibration methods and diagnostics."""

import numpy as np
import pytest

from runtime.src.common.calibration import (
    PlattScaler,
    IsotonicCalibrator,
    TemperatureScaler,
    compute_ece,
    compute_calibration_slope
)


def test_platt_scaler():
    np.random.seed(42)
    # Synthetic uncalibrated probabilities (overconfident)
    raw_p = np.random.uniform(0.1, 0.9, size=200)
    # Binary outcomes generated with softer probability
    y = (np.random.rand(200) < (0.5 + 0.3 * (raw_p - 0.5))).astype(int)

    scaler = PlattScaler()
    scaler.fit(raw_p, y)
    cal_p = scaler.predict(raw_p)

    assert len(cal_p) == len(raw_p)
    assert np.all(cal_p >= 0.0)
    assert np.all(cal_p <= 1.0)


def test_isotonic_calibrator_monotonicity():
    probs = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    y = np.array([0, 0, 1, 0, 1, 1, 0, 1, 1])

    calibrator = IsotonicCalibrator()
    calibrator.fit(probs, y)
    cal_p = calibrator.predict(probs)

    # Check monotonicity
    for i in range(len(cal_p) - 1):
        assert cal_p[i] <= cal_p[i + 1] + 1e-9


def test_temperature_scaler():
    raw_p = np.array([0.05, 0.2, 0.5, 0.8, 0.95])
    y = np.array([0, 0, 1, 1, 1])

    ts = TemperatureScaler()
    ts.fit(raw_p, y)
    cal_p = ts.predict(raw_p)

    assert len(cal_p) == len(raw_p)
    assert ts.temperature > 0.0


def test_calibration_metrics():
    y_true = np.array([0, 0, 1, 1])
    y_prob = np.array([0.1, 0.2, 0.8, 0.9])

    ece = compute_ece(y_true, y_prob, n_bins=5)
    assert 0.0 <= ece <= 1.0

    alpha, beta = compute_calibration_slope(y_true, y_prob)
    # Slope should be positive for well-ordered predictions
    assert beta > 0.0

