"""Post-hoc calibration layer per sport x family, fitted on rolling CAL folds, with slope monitoring (ML-05).

Engine probabilities pass through `CalibrationLayer.apply` before ranking. A (sport, family) with too little CAL data is
passed through unchanged and reported as `identity_insufficient_data` - never silently treated as calibrated. Calibrators
are refitted when older than `recalibrate_days`; `monitor` reports the calibration slope and its week-block interval on
rolling windows (default 8 weeks), classifying each as ok / watch / recalibrate.
"""

import datetime as dt
from typing import Any, Dict, List, Sequence, Tuple

import numpy as np

from .calibration import BetaCalibrator, IsotonicCalibrator, PlattScaler, _validated_pair
from .errors import FitFailed, InsufficientData, NotFitted
from .evaluation import log_loss
from .uncertainty import cox_calibration, group_rows, percentile_interval, week_block_ids

METHODS = ("platt", "beta", "isotonic", "auto")
SLOPE_BAND = (0.90, 1.10)


def _make(method: str):
    return {"platt": PlattScaler, "beta": BetaCalibrator, "isotonic": IsotonicCalibrator}[method]()


def _date(value) -> dt.date:
    return dt.date.fromisoformat(str(value)[:10])


class CalibrationLayer:
    def __init__(self, method: str = "auto", min_rows: int = 100, isotonic_min_rows: int = 500, recalibrate_days: int = 30):
        if method not in METHODS:
            raise ValueError(f"method must be one of {METHODS}")
        self.method = method
        self.min_rows = min_rows
        self.isotonic_min_rows = isotonic_min_rows
        self.recalibrate_days = recalibrate_days
        self.entries: Dict[str, Dict[str, Any]] = {}

    @staticmethod
    def key(sport: str, family: str) -> str:
        return f"{sport}|{family}"

    # ----------------------------------------------------------------- fitting
    def select_method(self, probs: np.ndarray, y: np.ndarray, folds: int = 3) -> Tuple[str, Dict[str, float]]:
        """Method with the lowest expanding-window out-of-fold log loss on the (chronologically ordered) CAL rows."""
        n = len(y)
        candidates = ["platt", "beta"] + (["isotonic"] if n >= self.isotonic_min_rows else [])
        edges = np.linspace(n // 2, n, folds + 1).astype(int)
        scores: Dict[str, float] = {}
        for method in candidates:
            losses, weights = [], []
            for lo, hi in zip(edges[:-1], edges[1:]):
                if hi <= lo or lo < 30:
                    continue
                try:
                    fitted = _make(method).fit(probs[:lo], y[:lo])
                except FitFailed:
                    continue
                pred = np.clip(fitted.predict(probs[lo:hi]), 1e-6, 1 - 1e-6)
                losses.append(log_loss(y[lo:hi], pred))
                weights.append(hi - lo)
            if losses:
                scores[method] = float(np.average(losses, weights=weights))
        if not scores:
            raise FitFailed("CalibrationLayer", "no calibration method could be fitted on the CAL folds")
        return min(scores, key=lambda m: scores[m]), scores

    def fit(self, sport: str, family: str, probs: Sequence[float], y: Sequence[float], dates: Sequence[str]) -> Dict[str, Any]:
        """Fit on CAL rows ordered by date. Returns the stored entry (method, n, fit date, scores)."""
        p, yy = _validated_pair(probs, y, "CalibrationLayer")
        if len(dates) != len(yy):
            raise ValueError("dates must have one entry per row")
        order = np.argsort([str(d) for d in dates], kind="stable")
        p, yy = p[order], yy[order]
        ordered_dates = [str(dates[i])[:10] for i in order]
        entry: Dict[str, Any] = {"n": len(yy), "fit_date": ordered_dates[-1] if ordered_dates else None, "window_start": ordered_dates[0] if ordered_dates else None}
        if len(yy) < self.min_rows or len(set(yy.tolist())) < 2:
            entry.update({"status": "identity_insufficient_data", "method": "identity", "calibrator": None, "scores": {}})
        else:
            method, scores = (self.select_method(p, yy) if self.method == "auto" else (self.method, {}))
            if method == "isotonic" and len(yy) < self.isotonic_min_rows:
                raise InsufficientData(f"isotonic needs at least {self.isotonic_min_rows} rows, got {len(yy)}")
            entry.update({"status": "calibrated", "method": method, "calibrator": _make(method).fit(p, yy), "scores": scores})
        self.entries[self.key(sport, family)] = entry
        return entry

    # ---------------------------------------------------------------- applying
    def needs_recalibration(self, sport: str, family: str, as_of: str) -> bool:
        entry = self.entries.get(self.key(sport, family))
        if entry is None or entry["fit_date"] is None:
            return True
        return (_date(as_of) - _date(entry["fit_date"])).days > self.recalibrate_days

    def apply(self, sport: str, family: str, probs: Sequence[float]) -> Tuple[np.ndarray, str]:
        """(calibrated probabilities, status). Status is explicit: calibrated | identity_insufficient_data."""
        entry = self.entries.get(self.key(sport, family))
        if entry is None:
            raise NotFitted(f"CalibrationLayer: no calibration fitted for {sport}/{family}")
        p = np.asarray(probs, dtype=float)
        if entry["calibrator"] is None:
            return p.copy(), str(entry["status"])
        return np.clip(entry["calibrator"].predict(p), 0.0, 1.0), "calibrated"

    # -------------------------------------------------------------- monitoring
    @staticmethod
    def monitor(probs: Sequence[float], y: Sequence[float], dates: Sequence[str], window_weeks: int = 8, step_weeks: int = 1,
                min_rows: int = 60, n_resamples: int = 400, seed: int = 5) -> List[Dict[str, Any]]:
        """Rolling calibration slope/intercept with week-block bootstrap intervals.

        status: ok = slope inside [0.90, 1.10]; watch = outside the band but the interval still contains 1;
        recalibrate = outside the band and the interval excludes 1.
        """
        p, yy = _validated_pair(probs, y, "CalibrationLayer.monitor")
        weeks = week_block_ids(dates)
        ordered_weeks = sorted(set(weeks.tolist()))
        reports: List[Dict[str, Any]] = []
        for start in range(0, max(len(ordered_weeks) - window_weeks, 0) + 1, step_weeks):
            window = ordered_weeks[start:start + window_weeks]
            if len(window) < window_weeks:
                break
            rows = np.flatnonzero(np.isin(weeks, window))
            if len(rows) < min_rows or len(set(yy[rows].tolist())) < 2:
                reports.append({"weeks": (window[0], window[-1]), "n": int(len(rows)), "status": "insufficient"})
                continue
            alpha, beta = cox_calibration(yy[rows], p[rows])
            groups = group_rows(weeks[rows])
            labels = list(groups)
            rng = np.random.default_rng(seed)
            slopes = []
            for _ in range(n_resamples):
                draw = rng.integers(0, len(labels), len(labels))
                idx = rows[np.concatenate([groups[labels[i]] for i in draw])]
                try:
                    slopes.append(cox_calibration(yy[idx], p[idx])[1])
                except FitFailed:
                    continue
            lo, hi = percentile_interval(np.array(slopes)) if len(slopes) > 0.9 * n_resamples else (float("nan"), float("nan"))
            in_band = SLOPE_BAND[0] <= beta <= SLOPE_BAND[1]
            status = "ok" if in_band else ("watch" if lo <= 1.0 <= hi else "recalibrate")
            reports.append({"weeks": (window[0], window[-1]), "n": int(len(rows)), "slope": beta, "intercept": alpha,
                            "slope_ci": (lo, hi), "status": status})
        return reports
