"""Prospective evaluation harness: week-block bootstrap uncertainty and coverage reporting (EVL-03)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence

import numpy as np

from .evaluation import FixedCohortEvaluator, brier_score, log_loss
from .uncertainty import block_bootstrap, percentile_interval


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


NAN_INTERVAL = UncertaintyInterval(float("nan"), float("nan"), float("nan"), float("nan"))


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
    n_blocks: int = 0
    power: Optional[Dict[str, Dict[str, float]]] = None

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
            "n_blocks": self.n_blocks,
            "power": self.power,
            "bootstrap_unit": "block",
        }


def hit_rate(y: np.ndarray, p: np.ndarray) -> float:
    return float(np.mean((p >= 0.50) == y))


class ProspectiveEvaluationHarness:
    """Rigorous evaluation harness for shadow and prospective model comparison.

    Guarantees:
    - Fixed fixture and line cohort identity, and coverage reporting against the supplied cohort size.
    - Block bootstrap (an ISO week or a match day per block) for every standard error and interval; rows are never
      resampled singly because same-week forecasts are correlated.
    - Strict promotion evaluation via `FixedCohortEvaluator` (CI-based gate, calibration CIs, seed stability, power).
    """

    @staticmethod
    def _interval(metric_fn: Any, y: np.ndarray, p_c: np.ndarray, p_b: np.ndarray, block_ids: np.ndarray,
                  n_resamples: int, seed: int = 42) -> UncertaintyInterval:
        """Block-bootstrap standard error and 95% interval of metric(y, p_c) - metric(y, p_b)."""
        if len(y) == 0:
            return NAN_INTERVAL
        estimate = float(metric_fn(y, p_c) - metric_fn(y, p_b))
        deltas = block_bootstrap(lambda yy, pc, pb: metric_fn(yy, pc) - metric_fn(yy, pb), (y, p_c, p_b), block_ids, n_resamples, seed)
        lo, hi = percentile_interval(deltas)
        return UncertaintyInterval(estimate, float(np.std(deltas, ddof=1)), lo, hi)

    @staticmethod
    def _iid_interval(metric_fn: Any, y: np.ndarray, p_c: np.ndarray, p_b: np.ndarray, n_resamples: int = 1000,
                      seed: int = 42) -> UncertaintyInterval:
        """Row-level bootstrap, kept only to show how much the independence assumption would understate the uncertainty."""
        rng = np.random.default_rng(seed)
        n = len(y)
        deltas = np.empty(n_resamples)
        for i in range(n_resamples):
            rows = rng.integers(0, n, size=n)
            deltas[i] = metric_fn(y[rows], p_c[rows]) - metric_fn(y[rows], p_b[rows])
        lo, hi = percentile_interval(deltas)
        return UncertaintyInterval(float(metric_fn(y, p_c) - metric_fn(y, p_b)), float(np.std(deltas, ddof=1)), lo, hi)

    @classmethod
    def evaluate_cohort(
        cls,
        y_true: np.ndarray,
        p_cand: np.ndarray,
        p_base: np.ndarray,
        event_ids: List[str],
        lines: List[float],
        block_ids: Optional[Sequence] = None,
        n_cohort_total: Optional[int] = None,
        min_sample_size: int = 50,
        bootstrap_resamples: int = 1000,
        require_calibration: bool = True,
        min_blocks: int = 8,
    ) -> ProspectiveEvaluationReport:
        """Run prospective evaluation comparing candidate against baseline with block-bootstrap uncertainty."""
        y_t = np.asarray(y_true, dtype=float) if y_true is not None else np.array([])
        p_c = np.asarray(p_cand, dtype=float) if p_cand is not None else np.array([])
        p_b = np.asarray(p_base, dtype=float) if p_base is not None else np.array([])
        n = len(y_t)

        total_cohort = n_cohort_total if n_cohort_total is not None else max(n, 1)
        coverage_rate = float(n / total_cohort) if total_cohort > 0 else 0.0
        valid_lines = [x for x in lines if x is not None and np.isfinite(x)] if lines else []
        lines_cov_rate = float(len(valid_lines) / max(len(lines or []), 1))

        res = FixedCohortEvaluator.evaluate(
            y_true=y_t, p_cand=p_c, p_base=p_b, event_ids_cand=event_ids, event_ids_base=event_ids,
            lines_cand=lines, lines_base=lines, min_sample_size=min_sample_size, require_calibration=require_calibration,
            block_ids=block_ids, min_blocks=min_blocks, n_resamples=bootstrap_resamples,
        )
        reasons = list(res["promotion_reasons"])
        blocks = None if block_ids is None else np.asarray(block_ids)

        if n < 2 or not np.isfinite(res["brier_candidate"]) or blocks is None or len(blocks) != n:
            return ProspectiveEvaluationReport(
                n_samples=n, n_cohort_total=total_cohort, coverage_rate=coverage_rate, lines_coverage_rate=lines_cov_rate,
                is_promotable=False, promotion_reasons=reasons or ["Insufficient valid evaluated samples"],
                brier_candidate=float(res["brier_candidate"]), brier_baseline=float(res["brier_baseline"]), delta_brier=NAN_INTERVAL,
                log_loss_candidate=float(res["log_loss_candidate"]), log_loss_baseline=float(res["log_loss_baseline"]),
                delta_log_loss=NAN_INTERVAL, hit_rate_candidate=float(res["hit_rate_candidate"]),
                hit_rate_baseline=float(res["hit_rate_baseline"]), delta_hit_rate=NAN_INTERVAL,
                calibration_slope_beta=float(res["cal_slope_beta"]), calibration_intercept_alpha=float(res["cal_intercept_alpha"]),
                bootstrap_resamples=bootstrap_resamples, n_blocks=int(res.get("n_blocks", 0)), power=None)

        ui_brier = cls._interval(brier_score, y_t, p_c, p_b, blocks, bootstrap_resamples)
        ui_logloss = cls._interval(log_loss, y_t, p_c, p_b, blocks, bootstrap_resamples)
        ui_hit = cls._interval(hit_rate, y_t, p_c, p_b, blocks, bootstrap_resamples)
        return ProspectiveEvaluationReport(
            n_samples=n, n_cohort_total=total_cohort, coverage_rate=coverage_rate, lines_coverage_rate=lines_cov_rate,
            is_promotable=bool(res["is_promotable"]), promotion_reasons=reasons,
            brier_candidate=float(res["brier_candidate"]), brier_baseline=float(res["brier_baseline"]), delta_brier=ui_brier,
            log_loss_candidate=float(res["log_loss_candidate"]), log_loss_baseline=float(res["log_loss_baseline"]),
            delta_log_loss=ui_logloss, hit_rate_candidate=float(res["hit_rate_candidate"]),
            hit_rate_baseline=float(res["hit_rate_baseline"]), delta_hit_rate=ui_hit,
            calibration_slope_beta=float(res["cal_slope_beta"]), calibration_intercept_alpha=float(res["cal_intercept_alpha"]),
            bootstrap_resamples=bootstrap_resamples, n_blocks=int(res["n_blocks"]), power=res.get("power"))
