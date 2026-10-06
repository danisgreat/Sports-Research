"""Proper scoring rules and probability evaluation metrics."""

from typing import Dict, List, Union
import numpy as np


def brier_score(y_true: np.ndarray, y_prob: np.ndarray) -> float:
    """Mean Squared Error of binary probability forecasts: (1/N) sum (y_prob - y_true)^2."""
    y_t = np.asarray(y_true, dtype=float)
    y_p = np.asarray(y_prob, dtype=float)
    return float(np.mean((y_p - y_t) ** 2))


def multiclass_brier_score(y_true_onehot: np.ndarray, y_probs: np.ndarray) -> float:
    """Multiclass Brier score: (1/N) sum_i sum_k (p_{ik} - y_{ik})^2."""
    y_t = np.asarray(y_true_onehot, dtype=float)
    y_p = np.asarray(y_probs, dtype=float)
    return float(np.mean(np.sum((y_p - y_t) ** 2, axis=1)))


def log_loss(y_true: np.ndarray, y_prob: np.ndarray, eps: float = 1e-15) -> float:
    """Binary cross-entropy / log loss: - (1/N) sum (y*log(p) + (1-y)*log(1-p))."""
    y_t = np.asarray(y_true, dtype=float)
    y_p = np.clip(np.asarray(y_prob, dtype=float), eps, 1.0 - eps)
    return float(-np.mean(y_t * np.log(y_p) + (1.0 - y_t) * np.log(1.0 - y_p)))


def crps_score(y_true: np.ndarray, y_cdf_probs: np.ndarray, thresholds: np.ndarray) -> float:
    """Continuous Ranked Probability Score (CRPS) for discrete threshold approximations.
    
    CRPS = integral (F(t) - 1(y <= t))^2 dt.
    """
    y_t = np.asarray(y_true, dtype=float)
    # y_cdf_probs: shape (N, T) where T is number of thresholds
    thresh = np.asarray(thresholds, dtype=float)
    diffs = np.diff(thresh)
    
    n_samples = len(y_t)
    crps_vals = []

    for i in range(n_samples):
        obs = y_t[i]
        indicator = (thresh >= obs).astype(float)
        sq_err = (y_cdf_probs[i] - indicator) ** 2
        # Trapezoidal or Riemann sum integration over thresholds
        integral = np.sum(0.5 * (sq_err[:-1] + sq_err[1:]) * diffs)
        crps_vals.append(integral)

    return float(np.mean(crps_vals))


def murphy_decomposition(y_true: np.ndarray, y_prob: np.ndarray, n_bins: int = 10) -> Dict[str, float]:
    """Murphy's Brier Score Decomposition into Reliability, Resolution, and Uncertainty.
    
    Brier = Reliability - Resolution + Uncertainty
    """
    y_t = np.asarray(y_true, dtype=float)
    y_p = np.asarray(y_prob, dtype=float)
    n = len(y_t)
    base_rate = float(np.mean(y_t))
    uncertainty = base_rate * (1.0 - base_rate)

    bins = np.linspace(0.0, 1.0, n_bins + 1)
    reliability = 0.0
    resolution = 0.0

    for i in range(n_bins):
        bin_lower = bins[i]
        bin_upper = bins[i + 1]
        mask = (y_p >= bin_lower) & (y_p < bin_upper if i < n_bins - 1 else y_p <= bin_upper)
        n_k = np.sum(mask)

        if n_k > 0:
            obs_rate_k = float(np.mean(y_t[mask]))
            pred_rate_k = float(np.mean(y_p[mask]))
            weight = n_k / n

            reliability += weight * ((pred_rate_k - obs_rate_k) ** 2)
            resolution += weight * ((obs_rate_k - base_rate) ** 2)

    total_brier = reliability - resolution + uncertainty
    return {
        "brier": float(total_brier),
        "reliability": float(reliability),
        "resolution": float(resolution),
        "uncertainty": float(uncertainty)
    }


class FixedCohortEvaluator:
    """Evaluates candidate vs baseline strictly on the exact same cohort of fixtures and supplied lines."""

    @staticmethod
    def evaluate(
        y_true: np.ndarray,
        p_cand: np.ndarray,
        p_base: np.ndarray,
        decision_threshold: float = 0.50
    ) -> Dict[str, Union[float, int, bool, List[str]]]:
        y_t = np.asarray(y_true, dtype=float)
        p_c = np.asarray(p_cand, dtype=float)
        p_b = np.asarray(p_base, dtype=float)
        n = len(y_t)

        br_c = brier_score(y_t, p_c)
        br_b = brier_score(y_t, p_b)
        delta_brier = br_c - br_b

        ll_c = log_loss(y_t, p_c)
        ll_b = log_loss(y_t, p_b)
        delta_ll = ll_c - ll_b

        acc_c = float(np.mean((p_c >= decision_threshold) == y_t))
        acc_b = float(np.mean((p_b >= decision_threshold) == y_t))

        reasons = []
        is_promotable = True

        if delta_brier > -0.010:
            is_promotable = False
            reasons.append(f"Delta Brier {delta_brier:.4f} did not meet required threshold <= -0.010")

        if delta_ll > 0.0:
            is_promotable = False
            reasons.append(f"Delta LogLoss {delta_ll:.4f} deteriorated (> 0.0)")

        return {
            "n_samples": n,
            "brier_candidate": br_c,
            "brier_baseline": br_b,
            "delta_brier": delta_brier,
            "log_loss_candidate": ll_c,
            "log_loss_baseline": ll_b,
            "delta_log_loss": delta_ll,
            "hit_rate_candidate": acc_c,
            "hit_rate_baseline": acc_b,
            "is_promotable": is_promotable,
            "promotion_reasons": reasons
        }


