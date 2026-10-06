"""Prospective evaluation harness with uncertainty quantification and coverage reporting."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np

from .evaluation import FixedCohortEvaluator, brier_score, log_loss


@dataclass
class UncertaintyInterval:
    estimate: float
    std_error: float
    ci_lower_95: float
    ci_upper_95: float

    def to_dict(self) -> Dict[str, float]:
        return {
            "estimate": float(self.estimate),
            "std_error": float(self.std_error),
            "ci_lower_95": float(self.ci_lower_95),
            "ci_upper_95": float(self.ci_upper_95),
        }


@dataclass
class ProspectiveEvaluationReport:
    n_samples: int
    n_cohort_total: int
    coverage_rate: float
    lines_coverage_rate: float
    is_promotable: bool
    promotion_reasons: List[str]
    brier_candidate: float
    brier_baseline: float
    delta_brier: UncertaintyInterval
    log_loss_candidate: float
    log_loss_baseline: float
    delta_log_loss: UncertaintyInterval
    hit_rate_candidate: float
    hit_rate_baseline: float
    delta_hit_rate: UncertaintyInterval
    calibration_slope_beta: float
    calibration_intercept_alpha: float
    bootstrap_resamples: int = 1000

    def to_dict(self) -> Dict[str, Any]:
        return {
            "n_samples": self.n_samples,
            "n_cohort_total": self.n_cohort_total,
            "coverage_rate": self.coverage_rate,
            "lines_coverage_rate": self.lines_coverage_rate,
            "is_promotable": self.is_promotable,
            "promotion_reasons": self.promotion_reasons,
            "brier_candidate": self.brier_candidate,
            "brier_baseline": self.brier_baseline,
            "delta_brier": self.delta_brier.to_dict(),
            "log_loss_candidate": self.log_loss_candidate,
            "log_loss_baseline": self.log_loss_baseline,
            "delta_log_loss": self.delta_log_loss.to_dict(),
            "hit_rate_candidate": self.hit_rate_candidate,
            "hit_rate_baseline": self.hit_rate_baseline,
            "delta_hit_rate": self.delta_hit_rate.to_dict(),
            "calibration_slope_beta": self.calibration_slope_beta,
            "calibration_intercept_alpha": self.calibration_intercept_alpha,
            "bootstrap_resamples": self.bootstrap_resamples,
        }


class ProspectiveEvaluationHarness:
    """Rigorous evaluation harness for shadow and prospective model comparison.
    
    Guarantees:
    - Fixed fixture and line cohort identity.
    - Coverage reporting (evaluated samples relative to total supplied cohort).
    - Non-parametric bootstrap confidence intervals and standard errors for all delta metrics.
    - Cox calibration with parameter boundaries.
    - Strict promotion evaluation via FixedCohortEvaluator.
    """

    @staticmethod
    def _bootstrap_interval(
        metric_fn: Any,
        y: np.ndarray,
        p_c: np.ndarray,
        p_b: np.ndarray,
        n_resamples: int = 1000,
        rng_seed: int = 42,
    ) -> UncertaintyInterval:
        """Compute bootstrap standard error and 95% confidence interval for paired differences."""
        n = len(y)
        if n == 0:
            return UncertaintyInterval(float("nan"), float("nan"), float("nan"), float("nan"))

        base_val = float(metric_fn(y, p_c) - metric_fn(y, p_b))
        rng = np.random.default_rng(rng_seed)
        deltas = np.zeros(n_resamples, dtype=float)

        for b in range(n_resamples):
            indices = rng.integers(0, n, size=n)
            y_sample = y[indices]
            pc_sample = p_c[indices]
            pb_sample = p_b[indices]
            deltas[b] = metric_fn(y_sample, pc_sample) - metric_fn(y_sample, pb_sample)

        std_err = float(np.std(deltas, ddof=1))
        ci_lower = float(np.percentile(deltas, 2.5))
        ci_upper = float(np.percentile(deltas, 97.5))
        return UncertaintyInterval(
            estimate=base_val,
            std_error=std_err,
            ci_lower_95=ci_lower,
            ci_upper_95=ci_upper,
        )

    @classmethod
    def evaluate_cohort(
        cls,
        y_true: np.ndarray,
        p_cand: np.ndarray,
        p_base: np.ndarray,
        event_ids: List[str],
        lines: List[float],
        n_cohort_total: Optional[int] = None,
        min_sample_size: int = 50,
        bootstrap_resamples: int = 1000,
        require_calibration: bool = True,
    ) -> ProspectiveEvaluationReport:
        """Run prospective evaluation comparing candidate against baseline with uncertainty."""
        y_t = np.asarray(y_true, dtype=float) if y_true is not None else np.array([])
        p_c = np.asarray(p_cand, dtype=float) if p_cand is not None else np.array([])
        p_b = np.asarray(p_base, dtype=float) if p_base is not None else np.array([])
        n = len(y_t)

        total_cohort = n_cohort_total if n_cohort_total is not None else max(n, 1)
        coverage_rate = float(n / total_cohort) if total_cohort > 0 else 0.0

        valid_lines = [x for x in lines if x is not None and np.isfinite(x)] if lines else []
        lines_cov_rate = float(len(valid_lines) / max(len(lines or []), 1))

        # Evaluate through FixedCohortEvaluator
        eval_res = FixedCohortEvaluator.evaluate(
            y_true=y_t,
            p_cand=p_c,
            p_base=p_b,
            event_ids_cand=event_ids,
            event_ids_base=event_ids,
            lines_cand=lines,
            lines_base=lines,
            min_sample_size=min_sample_size,
            require_calibration=require_calibration,
        )

        is_promotable = bool(eval_res["is_promotable"])
        reasons = list(eval_res["promotion_reasons"])

        if n < 2 or not np.isfinite(eval_res["brier_candidate"]):
            nan_ui = UncertaintyInterval(float("nan"), float("nan"), float("nan"), float("nan"))
            return ProspectiveEvaluationReport(
                n_samples=n,
                n_cohort_total=total_cohort,
                coverage_rate=coverage_rate,
                lines_coverage_rate=lines_cov_rate,
                is_promotable=False,
                promotion_reasons=reasons or ["Insufficient valid evaluated samples"],
                brier_candidate=float("nan"),
                brier_baseline=float("nan"),
                delta_brier=nan_ui,
                log_loss_candidate=float("nan"),
                log_loss_baseline=float("nan"),
                delta_log_loss=nan_ui,
                hit_rate_candidate=float("nan"),
                hit_rate_baseline=float("nan"),
                delta_hit_rate=nan_ui,
                calibration_slope_beta=float("nan"),
                calibration_intercept_alpha=float("nan"),
                bootstrap_resamples=bootstrap_resamples,
            )

        # Compute bootstrap uncertainty intervals
        ui_brier = cls._bootstrap_interval(
            brier_score, y_t, p_c, p_b, n_resamples=bootstrap_resamples
        )
        ui_logloss = cls._bootstrap_interval(
            log_loss, y_t, p_c, p_b, n_resamples=bootstrap_resamples
        )

        def hit_rate_fn(y: np.ndarray, p: np.ndarray) -> float:
            return float(np.mean((p >= 0.50) == y))

        ui_hit_rate = cls._bootstrap_interval(
            hit_rate_fn, y_t, p_c, p_b, n_resamples=bootstrap_resamples
        )

        return ProspectiveEvaluationReport(
            n_samples=n,
            n_cohort_total=total_cohort,
            coverage_rate=coverage_rate,
            lines_coverage_rate=lines_cov_rate,
            is_promotable=is_promotable,
            promotion_reasons=reasons,
            brier_candidate=float(eval_res["brier_candidate"]),
            brier_baseline=float(eval_res["brier_baseline"]),
            delta_brier=ui_brier,
            log_loss_candidate=float(eval_res["log_loss_candidate"]),
            log_loss_baseline=float(eval_res["log_loss_baseline"]),
            delta_log_loss=ui_logloss,
            hit_rate_candidate=float(eval_res["hit_rate_candidate"]),
            hit_rate_baseline=float(eval_res["hit_rate_baseline"]),
            delta_hit_rate=ui_hit_rate,
            calibration_slope_beta=float(eval_res["cal_slope_beta"]),
            calibration_intercept_alpha=float(eval_res["cal_intercept_alpha"]),
            bootstrap_resamples=bootstrap_resamples,
        )
