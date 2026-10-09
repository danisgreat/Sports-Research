"""Per sport x family calibration layer and beta calibration (ML-05)."""

import datetime as dt

import numpy as np
import pytest

from runtime.src.common.calibration import BetaCalibrator
from runtime.src.common.calibration_layer import CalibrationLayer
from runtime.src.common.errors import NotFitted
from runtime.src.common.uncertainty import cox_calibration


def stream(n=2400, seed=1, slope=0.5, start="2026-01-05", per_day=8):
    """Overconfident engine probabilities (true log-odds = slope * engine log-odds) over consecutive days."""
    rng = np.random.default_rng(seed)
    z = rng.normal(0, 1.4, n)
    p_engine = 1 / (1 + np.exp(-z))
    y = (rng.random(n) < 1 / (1 + np.exp(-slope * z))).astype(float)
    first = dt.date.fromisoformat(start)
    dates = [(first + dt.timedelta(days=i // per_day)).isoformat() for i in range(n)]
    return p_engine, y, dates


def test_beta_calibrator_fixes_asymmetric_miscalibration_and_is_monotone():
    rng = np.random.default_rng(3)
    p = rng.uniform(0.02, 0.98, 4000)
    truth = np.clip(p ** 1.6, 0, 1)                                   # under-predicts the top, a shape a logit slope cannot match
    y = (rng.random(4000) < truth).astype(float)
    cal = BetaCalibrator().fit(p, y)
    grid = np.linspace(0.05, 0.95, 50)
    out = cal.predict(grid)
    assert (np.diff(out) > 0).all() and cal.a >= 0 and cal.b >= 0
    assert np.abs(cal.predict(np.array([0.3, 0.6, 0.9])) - np.array([0.3, 0.6, 0.9]) ** 1.6).max() < 0.04
    with pytest.raises(NotFitted):
        BetaCalibrator().predict(grid)


def test_layer_restores_slope_out_of_sample_and_reports_status():
    p, y, dates = stream()
    raw_slope = cox_calibration(y[1200:], p[1200:])[1]
    assert raw_slope < 0.6
    layer = CalibrationLayer(method="auto", min_rows=100)
    entry = layer.fit("nba", "winner", p[:1200], y[:1200], dates[:1200])
    assert entry["status"] == "calibrated" and entry["method"] in ("platt", "beta", "isotonic") and entry["scores"]
    calibrated, status = layer.apply("nba", "winner", p[1200:])
    assert status == "calibrated" and 0.85 <= cox_calibration(y[1200:], calibrated)[1] <= 1.15
    reports = [r for r in CalibrationLayer.monitor(calibrated, y[1200:], dates[1200:], window_weeks=8) if r["status"] != "insufficient"]
    assert reports and 0.9 <= float(np.median([r["slope"] for r in reports])) <= 1.1
    assert all(r["slope_ci"][0] <= 1.0 <= r["slope_ci"][1] for r in reports)          # no window is distinguishable from calibrated
    assert all(r["status"] in ("ok", "watch") for r in reports)


def test_monitor_flags_a_drifting_engine_for_recalibration():
    p, y, dates = stream(n=1600, slope=0.5)
    reports = [r for r in CalibrationLayer.monitor(p, y, dates, window_weeks=6) if r["status"] != "insufficient"]
    assert reports and all(r["status"] in ("recalibrate", "watch") for r in reports)
    assert any(r["status"] == "recalibrate" for r in reports)


def test_thin_families_pass_through_with_an_explicit_status():
    p, y, dates = stream(n=60)
    layer = CalibrationLayer(min_rows=100)
    layer.fit("afl", "corners", p, y, dates)
    out, status = layer.apply("afl", "corners", p)
    np.testing.assert_array_equal(out, p)
    assert status == "identity_insufficient_data"
    with pytest.raises(NotFitted):
        layer.apply("afl", "never_fitted", p)


def test_recalibration_schedule_and_validation():
    p, y, dates = stream(n=300, per_day=10)
    layer = CalibrationLayer(method="platt", recalibrate_days=30)
    layer.fit("nhl", "total", p, y, dates)
    last = layer.entries["nhl|total"]["fit_date"]
    assert layer.needs_recalibration("nhl", "total", last) is False
    assert layer.needs_recalibration("nhl", "total", (dt.date.fromisoformat(last) + dt.timedelta(days=31)).isoformat()) is True
    assert layer.needs_recalibration("nhl", "unfitted", last) is True
    with pytest.raises(ValueError):
        CalibrationLayer(method="magic")
    with pytest.raises(ValueError):
        layer.fit("nhl", "x", p, y, dates[:5])


def test_layer_roundtrips_through_json_artifacts(tmp_path):
    from runtime.src.common import artifacts
    p, y, dates = stream(n=600)
    layer = CalibrationLayer(method="platt")
    layer.fit("mlb", "winner", p, y, dates)
    path = str(tmp_path / "layer.json")
    artifacts.save(layer, path, {"notes": "test"})
    loaded = artifacts.load(path)
    np.testing.assert_allclose(loaded.apply("mlb", "winner", p[:20])[0], layer.apply("mlb", "winner", p[:20])[0])
