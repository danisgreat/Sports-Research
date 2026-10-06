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
    
    The classical 3-term Murphy identity:
        Brier_binned = Reliability - Resolution + Uncertainty
    reconstructs the binned Brier score where predictions in bin k are approximated
    by their bin mean. For continuous predictions with finite bin width, the original
    exact Brier score differs from the binned reconstruction by within-bin variance.
    Both original_brier and binned_brier are explicitly reported.
    """
    y_t = np.asarray(y_true, dtype=float)
    y_p = np.asarray(y_prob, dtype=float)
    n = len(y_t)
    if n == 0:
        return {
            "brier": float("nan"),
            "original_brier": float("nan"),
            "binned_brier": float("nan"),
            "reliability": float("nan"),
            "resolution": float("nan"),
            "uncertainty": float("nan"),
            "within_bin_discrepancy": float("nan"),
        }

    original_brier = float(np.mean((y_p - y_t) ** 2))
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

    binned_brier = reliability - resolution + uncertainty
    discrepancy = original_brier - binned_brier
    return {
        "brier": original_brier,
        "original_brier": original_brier,
        "binned_brier": float(binned_brier),
        "reliability": float(reliability),
        "resolution": float(resolution),
        "uncertainty": float(uncertainty),
        "within_bin_discrepancy": float(discrepancy),
    }


class FixedCohortEvaluator:
    """Evaluates candidate vs baseline strictly on the exact same cohort of fixtures and supplied lines.
    
    Enforces the Multi-Metric Promotion Matrix:
    - Fixed fixture and line cohort identity (mandatory non-empty event_ids and lines).
    - Strict input validation: no empty sets, no NaNs/Infs, valid [0, 1] probabilities.
    - Binary outcome enforcement: y_true must be strictly {0, 1}.
    - Sample sufficiency: n >= min_sample_size (default 50).
    - Probabilistic accuracy: Delta Brier <= -0.010.
    - Information loss: Delta LogLoss <= 0.0.
    - Hit rate on same line: Hit Rate (Candidate) >= Hit Rate (Baseline).
    - Mandatory Cox calibration quality by default: beta in [0.90, 1.10], |alpha| <= 0.05.
    - Optimizer failure safety: failed calibration estimation fails promotion, never passes with default dummy values.
    """

    @staticmethod
    def evaluate(
        y_true: np.ndarray,
        p_cand: np.ndarray,
        p_base: np.ndarray,
        decision_threshold: float = 0.50,
        event_ids_cand: Optional[List[str]] = None,
        event_ids_base: Optional[List[str]] = None,
        lines_cand: Optional[List[float]] = None,
        lines_base: Optional[List[float]] = None,
        min_sample_size: int = 50,
        require_calibration: bool = True,
    ) -> Dict[str, Union[float, int, bool, List[str]]]:
        reasons = []
        is_promotable = True

        y_t = np.asarray(y_true, dtype=float) if y_true is not None else np.array([])
        p_c = np.asarray(p_cand, dtype=float) if p_cand is not None else np.array([])
        p_b = np.asarray(p_base, dtype=float) if p_base is not None else np.array([])
        n = len(y_t)

        # 1. Non-empty check
        if n == 0 or len(p_c) == 0 or len(p_b) == 0:
            return {
                "n_samples": 0,
                "brier_candidate": float("nan"),
                "brier_baseline": float("nan"),
                "delta_brier": float("nan"),
                "log_loss_candidate": float("nan"),
                "log_loss_baseline": float("nan"),
                "delta_log_loss": float("nan"),
                "hit_rate_candidate": float("nan"),
                "hit_rate_baseline": float("nan"),
                "cal_slope_beta": float("nan"),
                "cal_intercept_alpha": float("nan"),
                "is_promotable": False,
                "promotion_reasons": ["Empty dataset: sample size is 0"],
            }

        # Shape consistency check
        if len(p_c) != n or len(p_b) != n:
            return {
                "n_samples": n,
                "brier_candidate": float("nan"),
                "brier_baseline": float("nan"),
                "delta_brier": float("nan"),
                "log_loss_candidate": float("nan"),
                "log_loss_baseline": float("nan"),
                "delta_log_loss": float("nan"),
                "hit_rate_candidate": float("nan"),
                "hit_rate_baseline": float("nan"),
                "cal_slope_beta": float("nan"),
                "cal_intercept_alpha": float("nan"),
                "is_promotable": False,
                "promotion_reasons": [f"Length mismatch: y_true ({n}), p_cand ({len(p_c)}), p_base ({len(p_b)})"],
            }

        # 2. NaN / Inf check
        if np.any(np.isnan(p_c)) or np.any(np.isinf(p_c)):
            is_promotable = False
            reasons.append("Candidate probabilities contain NaN or Inf")
        if np.any(np.isnan(p_b)) or np.any(np.isinf(p_b)):
            is_promotable = False
            reasons.append("Baseline probabilities contain NaN or Inf")
        if np.any(np.isnan(y_t)) or np.any(np.isinf(y_t)):
            is_promotable = False
            reasons.append("True labels contain NaN or Inf")

        # Probability bound check [0, 1]
        if np.any(p_c < -1e-9) or np.any(p_c > 1.0 + 1e-9):
            is_promotable = False
            reasons.append("Candidate probabilities outside valid [0, 1] range")
        if np.any(p_b < -1e-9) or np.any(p_b > 1.0 + 1e-9):
            is_promotable = False
            reasons.append("Baseline probabilities outside valid [0, 1] range")

        # Binary labels enforcement
        unique_y = np.unique(y_t)
        if not np.all(np.isin(unique_y, [0.0, 1.0])):
            is_promotable = False
            reasons.append(f"True labels must be binary {{0, 1}}; found non-binary values {unique_y.tolist()}")

        # Immediate return if inputs are mathematically corrupt
        if not is_promotable:
            return {
                "n_samples": n,
                "brier_candidate": float("nan"),
                "brier_baseline": float("nan"),
                "delta_brier": float("nan"),
                "log_loss_candidate": float("nan"),
                "log_loss_baseline": float("nan"),
                "delta_log_loss": float("nan"),
                "hit_rate_candidate": float("nan"),
                "hit_rate_baseline": float("nan"),
                "cal_slope_beta": float("nan"),
                "cal_intercept_alpha": float("nan"),
                "is_promotable": False,
                "promotion_reasons": reasons,
            }

        # 3. Minimum sample sufficiency check
        if n < min_sample_size:
            is_promotable = False
            reasons.append(f"Sample size {n} is below minimum requirement of {min_sample_size}")

        # 4. Mandatory Cohort matching checks (prevent line selection fallacy)
        if event_ids_cand is None or event_ids_base is None or len(event_ids_cand) == 0 or len(event_ids_base) == 0:
            is_promotable = False
            reasons.append("Mandatory event IDs missing or empty; cannot verify fixed fixture cohort")
        elif len(event_ids_cand) != n or len(event_ids_base) != n:
            is_promotable = False
            reasons.append(f"Event IDs length ({len(event_ids_cand)}, {len(event_ids_base)}) does not match sample size ({n})")
        elif list(event_ids_cand) != list(event_ids_base):
            is_promotable = False
            reasons.append("Candidate and baseline event IDs do not match identically (fixed fixture cohort violated)")

        if lines_cand is None or lines_base is None or len(lines_cand) == 0 or len(lines_base) == 0:
            is_promotable = False
            reasons.append("Mandatory supplied lines missing or empty; cannot verify fixed line cohort")
        elif len(lines_cand) != n or len(lines_base) != n:
            is_promotable = False
            reasons.append(f"Supplied lines length ({len(lines_cand)}, {len(lines_base)}) does not match sample size ({n})")
        elif [float(x) for x in lines_cand] != [float(x) for x in lines_base]:
            is_promotable = False
            reasons.append("Candidate and baseline supplied lines do not match identically (line selection fallacy / fixed line cohort violated)")

        # 5. Core scoring metrics
        br_c = brier_score(y_t, p_c)
        br_b = brier_score(y_t, p_b)
        delta_brier = br_c - br_b

        ll_c = log_loss(y_t, p_c)
        ll_b = log_loss(y_t, p_b)
        delta_ll = ll_c - ll_b

        acc_c = float(np.mean((p_c >= decision_threshold) == y_t))
        acc_b = float(np.mean((p_b >= decision_threshold) == y_t))

        if delta_brier > -0.010:
            is_promotable = False
            reasons.append(f"Delta Brier {delta_brier:.4f} did not meet required threshold <= -0.010")

        if delta_ll > 0.0:
            is_promotable = False
            reasons.append(f"Delta LogLoss {delta_ll:.4f} deteriorated (> 0.0)")

        if acc_c < acc_b:
            is_promotable = False
            reasons.append(f"Candidate hit rate {acc_c:.4f} is lower than baseline {acc_b:.4f}")

        # 6. Cox calibration: logit(p_c) -> alpha + beta * logit(p_c)
        from scipy.optimize import minimize
        from scipy.special import logit
        p_c_clipped = np.clip(p_c, 1e-6, 1.0 - 1e-6)
        logit_p = logit(p_c_clipped)

        def cal_objective(params):
            a, b = params
            z = a + b * logit_p
            # Stable log-loss with logaddexp: log(1 + exp(z)) - y * z
            loss = np.sum(np.logaddexp(0.0, z) - y_t * z)
            loss += 1e-4 * (a ** 2 + (b - 1.0) ** 2)
            return loss

        cal_res = minimize(cal_objective, [0.0, 1.0], method="L-BFGS-B")
        if cal_res.success:
            alpha = float(cal_res.x[0])
            beta = float(cal_res.x[1])
        else:
            alpha = float("nan")
            beta = float("nan")
            if require_calibration:
                is_promotable = False
                reasons.append(f"Calibration optimization failed: {cal_res.message}")

        if require_calibration and cal_res.success:
            if beta < 0.90 or beta > 1.10:
                is_promotable = False
                reasons.append(f"Calibration slope beta={beta:.4f} outside acceptable range [0.90, 1.10]")

            if abs(alpha) > 0.05:
                is_promotable = False
                reasons.append(f"Calibration intercept |alpha|={abs(alpha):.4f} exceeds threshold 0.05")

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
            "cal_slope_beta": beta,
            "cal_intercept_alpha": alpha,
            "is_promotable": is_promotable,
            "promotion_reasons": reasons,
        }


