"""Chronological out-of-fold stacking and probability mixtures with non-negative constraints."""

from typing import Dict, List, Optional
import numpy as np
from scipy.optimize import minimize


class ChronologicalStacker:
    """Non-negative constrained probability mixture blender for chronological ensembles.
    
    Fits weights on earlier out-of-fold calibration predictions (CAL):
    min_w sum (y - sum(w_m * p_m))^2 subject to w_m >= 0 and sum(w_m) = 1.
    """

    def __init__(self, loss_type: str = "brier"):
        self.loss_type = loss_type.lower()
        self.weights: np.ndarray = np.array([])
        self.model_names: List[str] = []

    def fit(
        self,
        oof_probs: np.ndarray,
        y_true: np.ndarray,
        model_names: Optional[List[str]] = None
    ) -> "ChronologicalStacker":
        """Fit ensemble weights on out-of-fold probability predictions.
        
        oof_probs: shape (N, M) where M is number of base models.
        y_true: shape (N,) binary outcome.
        """
        N, M = oof_probs.shape
        self.model_names = model_names or [f"model_{i}" for i in range(M)]

        if M == 1:
            self.weights = np.array([1.0])
            return self

        # Objective function
        def objective(w):
            p_blend = oof_probs @ w
            if self.loss_type == "logloss":
                p_blend = np.clip(p_blend, 1e-12, 1.0 - 1e-12)
                return -np.mean(y_true * np.log(p_blend) + (1.0 - y_true) * np.log(1.0 - p_blend))
            else:  # Brier score
                return np.mean((p_blend - y_true) ** 2)

        # Constraints: sum(w) = 1, w_i >= 0
        constraints = [{"type": "eq", "fun": lambda w: np.sum(w) - 1.0}]
        bounds = [(0.0, 1.0) for _ in range(M)]
        init_w = np.ones(M) / M

        res = minimize(objective, init_w, method="SLSQP", bounds=bounds, constraints=constraints)
        if res.success:
            self.weights = np.clip(res.x, 0.0, 1.0)
            self.weights /= np.sum(self.weights)
        else:
            self.weights = np.ones(M) / M

        return self

    def predict(self, test_probs: np.ndarray) -> np.ndarray:
        """Blend test probabilities using frozen weights."""
        test_probs = np.asarray(test_probs, dtype=float)
        return test_probs @ self.weights

    def get_weights_dict(self) -> Dict[str, float]:
        """Return dict of model weights."""
        return {name: float(w) for name, w in zip(self.model_names, self.weights)}
