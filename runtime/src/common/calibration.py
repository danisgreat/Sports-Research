"""Probability calibration algorithms and calibration diagnostics."""

from typing import Tuple
import numpy as np
from scipy.optimize import minimize
from scipy.special import expit, logit


class PlattScaler:
    """Logistic calibration: P(Y=1 | p) = 1 / (1 + exp(-(a * logit(p) + b)))."""

    def __init__(self):
        self.a: float = 1.0
        self.b: float = 0.0

    def fit(self, probs: np.ndarray, y_true: np.ndarray) -> "PlattScaler":
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
        if res.success:
            self.a, self.b = res.x
        return self

    def predict(self, probs: np.ndarray) -> np.ndarray:
        p_clipped = np.clip(probs, 1e-6, 1.0 - 1e-6)
        z = logit(p_clipped)
        return expit(self.a * z + self.b)


class IsotonicCalibrator:
    """Non-parametric monotonic probability calibration via Pool Adjacent Violators Algorithm (PAVA)."""

    def __init__(self):
        self.x_vals: np.ndarray = np.array([])
        self.y_vals: np.ndarray = np.array([])

    def fit(self, probs: np.ndarray, y_true: np.ndarray) -> "IsotonicCalibrator":
        order = np.argsort(probs)
        x_sort = probs[order]
        y_sort = y_true[order].astype(float)

        # PAVA implementation
        weights = np.ones_like(y_sort)
        v = y_sort.copy()

        i = 0
        while i < len(v) - 1:
            if v[i] > v[i + 1]:
                # Pool violators
                j = i
                while j >= 0 and v[j] > v[j + 1]:
                    w_sum = weights[j] + weights[j + 1]
                    v_avg = (v[j] * weights[j] + v[j + 1] * weights[j + 1]) / w_sum
                    v[j] = v_avg
                    v[j + 1] = v_avg
                    weights[j] = w_sum
                    weights[j + 1] = w_sum
                    j -= 1
                i = 0  # Re-scan from start
            else:
                i += 1

        self.x_vals = x_sort
        self.y_vals = np.clip(v, 0.0, 1.0)
        return self

    def predict(self, probs: np.ndarray) -> np.ndarray:
        if len(self.x_vals) == 0:
            return probs
        # Linear interpolation with constant extrapolation
        return np.interp(probs, self.x_vals, self.y_vals, left=self.y_vals[0], right=self.y_vals[-1])


class TemperatureScaler:
    """Temperature scaling: p_cal = sigmoid(logit(p) / T), with T > 0."""

    def __init__(self):
        self.temperature: float = 1.0

    def fit(self, probs: np.ndarray, y_true: np.ndarray) -> "TemperatureScaler":
        p_clipped = np.clip(probs, 1e-6, 1.0 - 1e-6)
        z = logit(p_clipped)

        def loss(log_temp):
            t = np.exp(log_temp[0])
            p_cal = expit(z / t)
            p_cal = np.clip(p_cal, 1e-12, 1.0 - 1e-12)
            return -np.sum(y_true * np.log(p_cal) + (1.0 - y_true) * np.log(1.0 - p_cal))

        res = minimize(loss, [0.0], method="L-BFGS-B")
        if res.success:
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
    """Fit Cox calibration curve: logit(P(Y=1)) = alpha + beta * logit(p). Returns (alpha, beta)."""
    p_clipped = np.clip(y_prob, 1e-5, 1.0 - 1e-5)
    z = logit(p_clipped)

    def loss(params):
        alpha, beta = params
        p_hat = expit(alpha + beta * z)
        p_hat = np.clip(p_hat, 1e-12, 1.0 - 1e-12)
        return -np.sum(y_true * np.log(p_hat) + (1.0 - y_true) * np.log(1.0 - p_hat))

    res = minimize(loss, [0.0, 1.0], method="BFGS")
    if res.success:
        return (float(res.x[0]), float(res.x[1]))
    return (0.0, 1.0)

