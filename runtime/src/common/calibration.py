"""Probability calibration algorithms and calibration diagnostics."""

from typing import Tuple
import numpy as np
from scipy.optimize import minimize
from scipy.special import expit, logit

from .errors import NotFitted, require_converged


def _validated_pair(probs, y_true, model: str) -> Tuple[np.ndarray, np.ndarray]:
    p = np.asarray(probs, dtype=float)
    y = np.asarray(y_true, dtype=float)
    if p.ndim != 1 or p.shape != y.shape or p.size == 0:
        raise ValueError(f"{model}: probs and y_true must be non-empty 1-D arrays of equal length")
    if not (np.all(np.isfinite(p)) and np.all(np.isfinite(y))):
        raise ValueError(f"{model}: probs and y_true must be finite")
    if np.any(p < 0.0) or np.any(p > 1.0) or not np.all(np.isin(y, (0.0, 1.0))):
        raise ValueError(f"{model}: probs must lie in [0, 1] and y_true must be binary")
    return p, y


class PlattScaler:
    """Logistic calibration: P(Y=1 | p) = 1 / (1 + exp(-(a * logit(p) + b)))."""

    def __init__(self):
        self.a: float = 1.0
        self.b: float = 0.0

    def fit(self, probs: np.ndarray, y_true: np.ndarray) -> "PlattScaler":
        probs, y_true = _validated_pair(probs, y_true, "PlattScaler")
        p_clipped = np.clip(probs, 1e-6, 1.0 - 1e-6)
        z = logit(p_clipped)

        # Negative log-likelihood objective
        def loss(params):
            a, b = params
            p_cal = expit(a * z + b)
            p_cal = np.clip(p_cal, 1e-12, 1.0 - 1e-12)
            nll = -np.sum(y_true * np.log(p_cal) + (1.0 - y_true) * np.log(1.0 - p_cal))
            # Weak L2 regularization towards identity (a=1, b=0)
            reg = 0.01 * ((a - 1.0) ** 2 + b ** 2)
            return nll + reg

        res = minimize(loss, [1.0, 0.0], method="BFGS")
        require_converged(res, "PlattScaler", grad_tol=1e-3)
        self.a, self.b = (float(res.x[0]), float(res.x[1]))
        return self

    def predict(self, probs: np.ndarray) -> np.ndarray:
        p_clipped = np.clip(probs, 1e-6, 1.0 - 1e-6)
        z = logit(p_clipped)
        return expit(self.a * z + self.b)


def pava(values: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """Weighted pool-adjacent-violators: the non-decreasing least-squares fit of `values`.

    Stack based and linear time. A pooled block carries the weighted mean of its members,
    and each element's weight is counted exactly once (ML-01).
    """
    block_value, block_weight, block_size = [], [], []
    for v, w in zip(values, weights):
        block_value.append(float(v))
        block_weight.append(float(w))
        block_size.append(1)
        while len(block_value) > 1 and block_value[-2] > block_value[-1]:
            w2, v2, n2 = block_weight.pop(), block_value.pop(), block_size.pop()
            w1, v1, n1 = block_weight.pop(), block_value.pop(), block_size.pop()
            total = w1 + w2
            block_value.append((v1 * w1 + v2 * w2) / total)
            block_weight.append(total)
            block_size.append(n1 + n2)
    return np.repeat(np.array(block_value), np.array(block_size))


class IsotonicCalibrator:
    """Non-parametric monotonic probability calibration via the pool-adjacent-violators algorithm.

    Tied probabilities are merged first (weight = count, value = mean outcome), so the fit
    is a function of the probability and never depends on the order of tied rows.
    """

    def __init__(self):
        self.x_vals: np.ndarray = np.array([])
        self.y_vals: np.ndarray = np.array([])

    def fit(self, probs: np.ndarray, y_true: np.ndarray) -> "IsotonicCalibrator":
        probs, y_true = _validated_pair(probs, y_true, "IsotonicCalibrator")
        unique_x, inverse, counts = np.unique(probs, return_inverse=True, return_counts=True)
        sums = np.bincount(inverse, weights=y_true)
        fitted = pava(sums / counts, counts.astype(float))
        self.x_vals = unique_x
        self.y_vals = np.clip(fitted, 0.0, 1.0)
        return self

    def predict(self, probs: np.ndarray) -> np.ndarray:
        if len(self.x_vals) == 0:
            raise NotFitted("IsotonicCalibrator.predict called before fit")
        # Linear interpolation between block values with constant extrapolation
        return np.interp(np.asarray(probs, dtype=float), self.x_vals, self.y_vals,
                         left=self.y_vals[0], right=self.y_vals[-1])


class TemperatureScaler:
    """Temperature scaling: p_cal = sigmoid(logit(p) / T), with T > 0."""

    def __init__(self):
        self.temperature: float = 1.0

    def fit(self, probs: np.ndarray, y_true: np.ndarray) -> "TemperatureScaler":
        probs, y_true = _validated_pair(probs, y_true, "TemperatureScaler")
        p_clipped = np.clip(probs, 1e-6, 1.0 - 1e-6)
        z = logit(p_clipped)

        def loss(log_temp):
            t = np.exp(log_temp[0])
            p_cal = expit(z / t)
            p_cal = np.clip(p_cal, 1e-12, 1.0 - 1e-12)
            return -np.sum(y_true * np.log(p_cal) + (1.0 - y_true) * np.log(1.0 - p_cal))

        res = minimize(loss, [0.0], method="L-BFGS-B")
        require_converged(res, "TemperatureScaler", grad_tol=1e-3)
        self.temperature = float(np.exp(res.x[0]))
        return self

    def predict(self, probs: np.ndarray) -> np.ndarray:
        p_clipped = np.clip(probs, 1e-6, 1.0 - 1e-6)
        z = logit(p_clipped)
        return expit(z / self.temperature)


def compute_ece(y_true: np.ndarray, y_prob: np.ndarray, n_bins: int = 10) -> float:
    """Compute Expected Calibration Error (ECE)."""
    bins = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    total_samples = len(y_true)

    for i in range(n_bins):
        bin_lower = bins[i]
        bin_upper = bins[i + 1]
        mask = (y_prob >= bin_lower) & (y_prob < bin_upper if i < n_bins - 1 else y_prob <= bin_upper)
        bin_samples = np.sum(mask)

        if bin_samples > 0:
            acc = np.mean(y_true[mask])
            conf = np.mean(y_prob[mask])
            ece += (bin_samples / total_samples) * np.abs(acc - conf)

    return float(ece)


def compute_calibration_slope(y_true: np.ndarray, y_prob: np.ndarray) -> Tuple[float, float]:
    """Fit Cox calibration curve: logit(P(Y=1)) = alpha + beta * logit(p). Returns (alpha, beta).

    Raises `FitFailed` if the optimiser does not converge; no default (0, 1) is ever returned.
    """
    y_prob, y_true = _validated_pair(y_prob, y_true, "compute_calibration_slope")
    p_clipped = np.clip(y_prob, 1e-5, 1.0 - 1e-5)
    z = logit(p_clipped)

    def loss(params):
        alpha, beta = params
        p_hat = expit(alpha + beta * z)
        p_hat = np.clip(p_hat, 1e-12, 1.0 - 1e-12)
        return -np.sum(y_true * np.log(p_hat) + (1.0 - y_true) * np.log(1.0 - p_hat))

    res = minimize(loss, [0.0, 1.0], method="BFGS")
    require_converged(res, "compute_calibration_slope", grad_tol=1e-3)
    return (float(res.x[0]), float(res.x[1]))

