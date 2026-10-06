"""Unit tests for chronological stacking and probability mixtures."""

import numpy as np
import pytest

from runtime.src.common.stacking import ChronologicalStacker


def test_chronological_stacker_weights():
    np.random.seed(42)
    n = 200
    y = np.random.binomial(1, 0.5, size=n)

    # Model 1 is good, Model 2 is random noise
    p1 = np.clip(y * 0.4 + 0.3 + np.random.normal(0, 0.1, size=n), 0.05, 0.95)
    p2 = np.random.uniform(0.1, 0.9, size=n)

    oof_probs = np.column_stack([p1, p2])

    stacker = ChronologicalStacker(loss_type="brier")
    stacker.fit(oof_probs, y, model_names=["good_model", "noise_model"])

    weights = stacker.get_weights_dict()
    assert np.isclose(sum(weights.values()), 1.0, atol=1e-5)
    assert weights["good_model"] > weights["noise_model"]
    assert np.all(stacker.weights >= 0.0)

    # Test forward predict
    p_test = stacker.predict(oof_probs[:5])
    assert len(p_test) == 5
    assert np.all(p_test >= 0.0) and np.all(p_test <= 1.0)
