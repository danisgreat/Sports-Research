"""Chronological stacking: linear and logit (geometric) pooling, per-family weights, fitted on CAL only (ML-10, ML-02).

A stack is used only if it beats the best single model chosen on CAL when both are scored on TEST (`evaluate_stack`).
An optimiser failure raises `FitFailed`; equal weights are never substituted silently.
"""

from typing import Any, Dict, List, Optional, Sequence

import numpy as np
from scipy.optimize import minimize
from scipy.special import expit, logit

from .errors import FitFailed, InsufficientData, NotFitted
from .evaluation import brier_score, log_loss
from .uncertainty import block_bootstrap, percentile_interval

METHODS = ("linear", "logit")


def _clip(p: np.ndarray) -> np.ndarray:
    return np.clip(p, 1e-6, 1.0 - 1e-6)


class ChronologicalStacker:
    """Non-negative, sum-to-one weights over base-model probabilities.

    method="linear":  p = sum_m w_m p_m            (mixture)
    method="logit":   p = sigmoid(sum_m w_m logit(p_m))   (geometric / log-odds pooling; keeps agreement sharp)
    The weights minimise Brier or log loss on earlier out-of-fold calibration predictions (CAL).
    """

    def __init__(self, loss_type: str = "brier", method: str = "linear"):
        if loss_type.lower() not in ("brier", "logloss"):
            raise ValueError("loss_type must be 'brier' or 'logloss'")
        if method not in METHODS:
            raise ValueError(f"method must be one of {METHODS}")
        self.loss_type = loss_type.lower()
        self.method = method
        self.weights: np.ndarray = np.array([])
        self.model_names: List[str] = []

    @property
    def is_fitted(self) -> bool:
        return len(self.weights) > 0

    def _blend(self, probs: np.ndarray, w: np.ndarray) -> np.ndarray:
        if self.method == "logit":
            return expit(logit(_clip(probs)) @ w)
        return probs @ w

    def _loss(self, p: np.ndarray, y: np.ndarray) -> float:
        return log_loss(y, p) if self.loss_type == "logloss" else brier_score(y, p)

    def fit(self, oof_probs: np.ndarray, y_true: np.ndarray, model_names: Optional[Sequence[str]] = None) -> "ChronologicalStacker":
        """oof_probs: (N, M) out-of-fold probabilities of M base models; y_true: (N,) binary outcomes."""
        probs = np.asarray(oof_probs, dtype=float)
        y = np.asarray(y_true, dtype=float)
        if probs.ndim != 2 or y.shape != (probs.shape[0],):
            raise ValueError("oof_probs must be (N, M) and y_true (N,)")
        if not (np.isfinite(probs).all() and np.isfinite(y).all()) or probs.min() < 0 or probs.max() > 1 or not np.isin(y, (0.0, 1.0)).all():
            raise ValueError("probabilities must be finite in [0, 1] and outcomes binary")
        n, m = probs.shape
        if n < 20:
            raise InsufficientData(f"need at least 20 CAL rows to fit stacking weights, got {n}")
        names = list(model_names) if model_names is not None else [f"model_{i}" for i in range(m)]
        if len(names) != m:
            raise ValueError("model_names must have one entry per column")
        if m == 1:
            self.weights, self.model_names = np.array([1.0]), names
            return self
        result = minimize(lambda w: self._loss(self._blend(probs, w), y), np.full(m, 1.0 / m), method="SLSQP", bounds=[(0.0, 1.0)] * m,
                          constraints=[{"type": "eq", "fun": lambda w: np.sum(w) - 1.0}])
        if not result.success:
            raise FitFailed("ChronologicalStacker", str(result.message))
        w = np.clip(result.x, 0.0, 1.0)
        self.weights, self.model_names = w / w.sum(), names
        return self

    def predict(self, test_probs: np.ndarray) -> np.ndarray:
        if not self.is_fitted:
            raise NotFitted("ChronologicalStacker: fit before predicting")
        probs = np.asarray(test_probs, dtype=float)
        if probs.ndim != 2 or probs.shape[1] != len(self.weights):
            raise ValueError(f"test_probs must have {len(self.weights)} columns")
        return self._blend(probs, self.weights)

    def get_weights_dict(self) -> Dict[str, float]:
        return {name: float(w) for name, w in zip(self.model_names, self.weights)}


class FamilyStacker:
    """One stacker per contract family (winner, total, handicap, half-time, corners, ...), with an explicit global fallback.

    A family with fewer than `min_rows` CAL rows uses the global weights and is listed in `fallback_families`, so a thin
    family never gets weights fitted to a handful of games without anyone noticing.
    """

    def __init__(self, loss_type: str = "brier", method: str = "linear", min_rows: int = 60):
        self.loss_type, self.method, self.min_rows = loss_type, method, min_rows
        self.global_stacker = ChronologicalStacker(loss_type, method)
        self.by_family: Dict[str, ChronologicalStacker] = {}
        self.fallback_families: List[str] = []

    def fit(self, oof_probs: np.ndarray, y_true: np.ndarray, families: Sequence[str],
            model_names: Optional[Sequence[str]] = None) -> "FamilyStacker":
        probs, y, fam = np.asarray(oof_probs, dtype=float), np.asarray(y_true, dtype=float), np.asarray(families)
        if len(fam) != len(y):
            raise ValueError("families must have one entry per row")
        self.global_stacker.fit(probs, y, model_names)
        self.by_family, self.fallback_families = {}, []
        for family in sorted(set(fam.tolist())):
            rows = fam == family
            if int(rows.sum()) < self.min_rows:
                self.fallback_families.append(family)
                continue
            self.by_family[family] = ChronologicalStacker(self.loss_type, self.method).fit(probs[rows], y[rows], model_names)
        return self

    def predict(self, test_probs: np.ndarray, families: Sequence[str]) -> np.ndarray:
        probs, fam = np.asarray(test_probs, dtype=float), np.asarray(families)
        out = np.empty(len(probs))
        for family in set(fam.tolist()):
            rows = fam == family
            stacker = self.by_family.get(family, self.global_stacker)
            out[rows] = stacker.predict(probs[rows])
        return out


def evaluate_stack(cal_probs: np.ndarray, cal_y: np.ndarray, test_probs: np.ndarray, test_y: np.ndarray, test_blocks: Sequence,
                   model_names: Optional[Sequence[str]] = None, method: str = "linear", loss_type: str = "brier",
                   n_resamples: int = 1000, seed: int = 7) -> Dict[str, Any]:
    """Fit on CAL, compare on TEST with the best single model *as chosen on CAL*, and decide whether to use the stack.

    The stack is used only if the block-bootstrap 95% CI of (stack - best single) in the chosen loss lies below 0.
    Choosing the best single model on TEST would flatter the comparison, so it is never done here.
    """
    cal_probs, test_probs = np.asarray(cal_probs, dtype=float), np.asarray(test_probs, dtype=float)
    cal_y, test_y = np.asarray(cal_y, dtype=float), np.asarray(test_y, dtype=float)
    stacker = ChronologicalStacker(loss_type, method).fit(cal_probs, cal_y, model_names)
    loss = log_loss if loss_type == "logloss" else brier_score
    cal_losses = [loss(cal_y, cal_probs[:, j]) for j in range(cal_probs.shape[1])]
    best = int(np.argmin(cal_losses))
    stack_test = stacker.predict(test_probs)
    single_test = test_probs[:, best]
    deltas = block_bootstrap(lambda yy, ps, pb: loss(yy, ps) - loss(yy, pb), (test_y, stack_test, single_test), np.asarray(test_blocks), n_resamples, seed)
    lo, hi = percentile_interval(deltas)
    delta = float(loss(test_y, stack_test) - loss(test_y, single_test))
    return {"weights": stacker.get_weights_dict(), "best_single_on_cal": stacker.model_names[best], "stack_test_loss": float(loss(test_y, stack_test)),
            "single_test_loss": float(loss(test_y, single_test)), "delta": delta, "delta_ci": (lo, hi), "use_stack": bool(hi < 0.0),
            "loss": loss_type, "method": method}
