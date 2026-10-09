"""Proper scoring rules and the uncertainty-aware promotion gate."""

from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

from .errors import FitFailed
from .uncertainty import block_indices, cox_calibration, group_rows, percentile_interval, power_summary


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


_METRIC_KEYS = ("brier_candidate", "brier_baseline", "delta_brier", "log_loss_candidate", "log_loss_baseline", "delta_log_loss",
                "hit_rate_candidate", "hit_rate_baseline", "cal_slope_beta", "cal_intercept_alpha")


def _refusal(n: int, reasons: List[str]) -> Dict[str, Any]:
    """A not-promotable result with no metrics (corrupt or empty inputs)."""
    out: Dict[str, Any] = {"n_samples": n, "is_promotable": False, "promotion_reasons": reasons}
    out.update({k: float("nan") for k in _METRIC_KEYS})
    return out


def _gate_from_bootstrap(boot: np.ndarray, min_effect: float, require_calibration: bool, level: float = 0.95):
    """Intervals and the CI-based gate for one resampling seed. `boot` has columns (d_brier, d_logloss, alpha, beta)."""
    intervals: Dict[str, Optional[Tuple[float, float]]] = {}
    for name, col in (("delta_brier", 0), ("delta_log_loss", 1), ("cal_intercept", 2), ("cal_slope", 3)):
        column = boot[:, col]
        finite = column[np.isfinite(column)]
        if len(finite) < 0.95 * len(column):
            intervals[name] = None
        else:
            intervals[name] = percentile_interval(finite, level)
    failures = []
    if intervals["delta_brier"] is None or intervals["delta_log_loss"] is None:
        failures.append("bootstrap intervals for the score differences could not be formed")
    else:
        if not intervals["delta_brier"][1] < -min_effect:
            failures.append(f"Delta Brier 95% CI upper bound {intervals['delta_brier'][1]:.4f} is not below {-min_effect:.4f}")
        if not intervals["delta_log_loss"][1] < 0.0:
            failures.append(f"Delta LogLoss 95% CI upper bound {intervals['delta_log_loss'][1]:.4f} is not below 0")
    if require_calibration:
        if intervals["cal_slope"] is None or intervals["cal_intercept"] is None:
            failures.append("calibration could not be estimated on the block resamples")
        else:
            lo, hi = intervals["cal_slope"]
            if not lo <= 1.0 <= hi:
                failures.append(f"calibration slope 95% CI [{lo:.3f}, {hi:.3f}] does not contain 1")
            lo, hi = intervals["cal_intercept"]
            if not lo <= 0.0 <= hi:
                failures.append(f"calibration intercept 95% CI [{lo:.3f}, {hi:.3f}] does not contain 0")
    return intervals, failures


class FixedCohortEvaluator:
    """Evaluates candidate vs baseline strictly on the exact same cohort of fixtures and supplied lines.

    The promotion gate (EVL-02) is uncertainty-aware. A candidate is promotable only if all of these hold:
    - Fixed fixture and line cohort identity (non-empty event ids and lines that match exactly).
    - Valid inputs (finite, probabilities in [0, 1], labels in {0, 1}), n >= min_sample_size and at least `min_blocks` blocks.
    - The week-block (or match-day) bootstrap 95% CI of delta Brier and of delta log-loss lies entirely below 0 (shifted
      by `min_effect` for Brier when a practical minimum is wanted). Single rows are never resampled: `block_ids` are required.
    - Hit rate on the same line is not lower than the baseline.
    - Calibration (when required): the block-bootstrap CI of the Cox slope contains 1 and of the intercept contains 0.
    - The decision is identical under every resampling seed in `seeds`; otherwise the gate refuses rather than choose one.
    Calibration estimation failure fails promotion; nothing passes on default dummy values. Power at the observed n is reported.
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
        block_ids: Optional[Sequence] = None,
        min_blocks: int = 8,
        n_resamples: int = 1000,
        seeds: Sequence[int] = (11, 23, 37),
        min_effect: float = 0.0,
    ) -> Dict[str, Any]:
        reasons: List[str] = []
        is_promotable = True

        y_t = np.asarray(y_true, dtype=float) if y_true is not None else np.array([])
        p_c = np.asarray(p_cand, dtype=float) if p_cand is not None else np.array([])
        p_b = np.asarray(p_base, dtype=float) if p_base is not None else np.array([])
        n = len(y_t)

        if n == 0 or len(p_c) == 0 or len(p_b) == 0:
            return _refusal(0, ["Empty dataset: sample size is 0"])
        if len(p_c) != n or len(p_b) != n:
            return _refusal(n, [f"Length mismatch: y_true ({n}), p_cand ({len(p_c)}), p_base ({len(p_b)})"])

        if not np.isfinite(p_c).all():
            is_promotable = False
            reasons.append("Candidate probabilities contain NaN or Inf")
        if not np.isfinite(p_b).all():
            is_promotable = False
            reasons.append("Baseline probabilities contain NaN or Inf")
        if not np.isfinite(y_t).all():
            is_promotable = False
            reasons.append("True labels contain NaN or Inf")
        if np.any(p_c < -1e-9) or np.any(p_c > 1.0 + 1e-9):
            is_promotable = False
            reasons.append("Candidate probabilities outside valid [0, 1] range")
        if np.any(p_b < -1e-9) or np.any(p_b > 1.0 + 1e-9):
            is_promotable = False
            reasons.append("Baseline probabilities outside valid [0, 1] range")
        unique_y = np.unique(y_t)
        if not np.all(np.isin(unique_y, [0.0, 1.0])):
            is_promotable = False
            reasons.append(f"True labels must be binary {{0, 1}}; found non-binary values {unique_y.tolist()}")
        if not is_promotable:
            return _refusal(n, reasons)

        if n < min_sample_size:
            is_promotable = False
            reasons.append(f"Sample size {n} is below minimum requirement of {min_sample_size}")

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

        br_c, br_b = brier_score(y_t, p_c), brier_score(y_t, p_b)
        ll_c, ll_b = log_loss(y_t, p_c), log_loss(y_t, p_b)
        delta_brier, delta_ll = br_c - br_b, ll_c - ll_b
        acc_c = float(np.mean((p_c >= decision_threshold) == y_t))
        acc_b = float(np.mean((p_b >= decision_threshold) == y_t))
        if acc_c < acc_b:
            is_promotable = False
            reasons.append(f"Candidate hit rate {acc_c:.4f} is lower than baseline {acc_b:.4f}")

        alpha = beta = float("nan")
        try:
            alpha, beta = cox_calibration(y_t, p_c)
        except FitFailed as exc:
            if require_calibration:
                is_promotable = False
                reasons.append(f"Calibration optimization failed: {exc.reason}")

        result: Dict[str, Any] = {
            "n_samples": n, "brier_candidate": br_c, "brier_baseline": br_b, "delta_brier": delta_brier,
            "log_loss_candidate": ll_c, "log_loss_baseline": ll_b, "delta_log_loss": delta_ll,
            "hit_rate_candidate": acc_c, "hit_rate_baseline": acc_b, "cal_slope_beta": beta, "cal_intercept_alpha": alpha,
            "n_blocks": 0, "delta_brier_ci": None, "delta_log_loss_ci": None, "cal_slope_ci": None, "cal_intercept_ci": None,
            "power": None, "decision_stable": None,
        }

        blocks = None if block_ids is None else np.asarray(block_ids)
        if blocks is None or len(blocks) != n:
            is_promotable = False
            reasons.append("Mandatory block ids (week or match-day) missing or of the wrong length; the block bootstrap cannot be run")
        else:
            groups = group_rows(blocks)
            result["n_blocks"] = len(groups)
            if len(groups) < min_blocks:
                is_promotable = False
                reasons.append(f"Only {len(groups)} blocks; at least {min_blocks} are required for a block bootstrap")
            else:
                def one_resample(rows: np.ndarray) -> np.ndarray:
                    yy, pc, pb = y_t[rows], p_c[rows], p_b[rows]
                    try:
                        a, b = cox_calibration(yy, pc)
                    except FitFailed:
                        a = b = float("nan")
                    return np.array([brier_score(yy, pc) - brier_score(yy, pb), log_loss(yy, pc) - log_loss(yy, pb), a, b])

                decisions: List[Tuple[bool, List[str]]] = []
                primary: Optional[Tuple[np.ndarray, Dict[str, Optional[Tuple[float, float]]]]] = None
                for seed in seeds:
                    rng = np.random.default_rng(seed)
                    boot = np.array([one_resample(block_indices(blocks, rng, groups)) for _ in range(n_resamples)])
                    intervals, failures = _gate_from_bootstrap(boot, min_effect, require_calibration)
                    decisions.append((not failures, failures))
                    if primary is None:
                        primary = (boot, intervals)
                if primary is None:
                    raise ValueError("seeds must contain at least one resampling seed")
                boot, intervals = primary
                result.update({"delta_brier_ci": intervals["delta_brier"], "delta_log_loss_ci": intervals["delta_log_loss"],
                               "cal_slope_ci": intervals["cal_slope"], "cal_intercept_ci": intervals["cal_intercept"]})
                result["power"] = {"brier": power_summary(delta_brier, boot[:, 0]), "log_loss": power_summary(delta_ll, boot[:, 1])}
                passed = [d[0] for d in decisions]
                result["decision_stable"] = all(passed) or not any(passed)
                if not result["decision_stable"]:
                    is_promotable = False
                    reasons.append("Gate decision depends on the resampling seed; refusing to choose one (add data or resamples)")
                elif not passed[0]:
                    is_promotable = False
                    reasons.extend(decisions[0][1])

        result["is_promotable"] = is_promotable
        result["promotion_reasons"] = reasons
        return result
