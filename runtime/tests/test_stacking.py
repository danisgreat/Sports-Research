"""Chronological stacking: linear/logit pooling, per-family weights, CAL-only fitting, use-only-if-better (ML-10, ML-02)."""

import numpy as np
import pytest
from scipy.optimize import OptimizeResult

from runtime.src.common.errors import FitFailed, InsufficientData, NotFitted
from runtime.src.common.stacking import ChronologicalStacker, FamilyStacker, evaluate_stack


def make_models(n=400, seed=42, noise=(0.10, 0.10, 1.0)):
    rng = np.random.default_rng(seed)
    z = rng.normal(0, 1.0, n)
    y = (rng.random(n) < 1 / (1 + np.exp(-z))).astype(float)
    cols = [np.clip(1 / (1 + np.exp(-(z + rng.normal(0, s, n)))), 0.02, 0.98) if s < 1 else rng.uniform(0.1, 0.9, n) for s in noise]
    return np.column_stack(cols), y


def test_weights_favour_the_good_model_and_sum_to_one():
    probs, y = make_models(noise=(0.1, 1.0, 1.0))
    for method in ("linear", "logit"):
        stacker = ChronologicalStacker("brier", method).fit(probs[:, :2], y, ["good", "noise"])
        w = stacker.get_weights_dict()
        assert sum(w.values()) == pytest.approx(1.0) and w["good"] > w["noise"] and (stacker.weights >= 0).all()
        out = stacker.predict(probs[:5, :2])
        assert out.shape == (5,) and ((out >= 0) & (out <= 1)).all()


def test_logit_pooling_is_geometric_and_differs_from_the_mixture():
    probs = np.array([[0.9, 0.7], [0.2, 0.4]] * 20)
    y = np.array([1.0, 0.0] * 20)
    lin = ChronologicalStacker("logloss", "linear")
    lin.weights, lin.model_names = np.array([0.5, 0.5]), ["a", "b"]
    geo = ChronologicalStacker("logloss", "logit")
    geo.weights, geo.model_names = np.array([0.5, 0.5]), ["a", "b"]
    assert lin.predict(probs[:1])[0] == pytest.approx(0.8)
    expected = 1 / (1 + np.exp(-(0.5 * np.log(9) + 0.5 * np.log(7 / 3))))
    assert geo.predict(probs[:1])[0] == pytest.approx(expected) and geo.predict(probs[:1])[0] != pytest.approx(0.8)
    assert y.shape == (40,)


def test_validation_and_loud_failures(monkeypatch):
    probs, y = make_models()
    with pytest.raises(NotFitted):
        ChronologicalStacker().predict(probs[:, :2])
    with pytest.raises(InsufficientData):
        ChronologicalStacker().fit(probs[:10], y[:10])
    with pytest.raises(ValueError):
        ChronologicalStacker().fit(probs * 2, y)
    with pytest.raises(ValueError):
        ChronologicalStacker("rmse")
    with pytest.raises(ValueError):
        ChronologicalStacker(method="vote")
    import runtime.src.common.stacking as stacking
    monkeypatch.setattr(stacking, "minimize", lambda *a, **k: OptimizeResult(success=False, message="forced", x=np.ones(3)))
    stacker = ChronologicalStacker()
    with pytest.raises(FitFailed):
        stacker.fit(probs, y)
    assert not stacker.is_fitted                                          # no silent equal weights


def test_family_stacker_falls_back_explicitly_for_thin_families():
    probs, y = make_models(n=500)
    families = np.array(["winner"] * 300 + ["total"] * 190 + ["corners"] * 10)
    stacker = FamilyStacker(min_rows=60).fit(probs, y, families, ["a", "b", "c"])
    assert set(stacker.by_family) == {"winner", "total"} and stacker.fallback_families == ["corners"]
    out = stacker.predict(probs, families)
    assert out.shape == (500,) and ((out >= 0) & (out <= 1)).all()
    corners_rows = families == "corners"
    np.testing.assert_allclose(out[corners_rows], stacker.global_stacker.predict(probs[corners_rows]))


def test_stack_is_used_only_when_it_beats_the_best_single_model_on_test():
    # complementary models: each sees half of the signal, so pooling them genuinely helps
    rng = np.random.default_rng(9)
    n = 3000
    a, b = rng.normal(0, 1, n), rng.normal(0, 1, n)
    y = (rng.random(n) < 1 / (1 + np.exp(-(a + b)))).astype(float)
    probs = np.column_stack([1 / (1 + np.exp(-a)), 1 / (1 + np.exp(-b))])
    blocks = np.array([f"W{i // 20:03d}" for i in range(n)])
    out = evaluate_stack(probs[:1500], y[:1500], probs[1500:], y[1500:], blocks[1500:], ["a", "b"], method="logit", loss_type="logloss", n_resamples=400)
    assert out["use_stack"] is True and out["delta"] < 0 and out["delta_ci"][1] < 0
    assert out["best_single_on_cal"] in ("a", "b")
    # one model is already best and the other is noise: the stack gains nothing and is not used
    probs2, y2 = make_models(n=3000, noise=(0.05, 1.0, 1.0))
    out2 = evaluate_stack(probs2[:1500, :2], y2[:1500], probs2[1500:, :2], y2[1500:], blocks[1500:], ["good", "noise"], n_resamples=400)
    assert out2["use_stack"] is False and out2["best_single_on_cal"] == "good"
