"""Chronological rolling-origin splits with purged embargos.

Enforces:
1. Strict temporal ordering: TRAIN < TUNE < CAL < TEST.
2. Calibration split (CAL) strictly isolated for calibration parameters (Platt, Isotonic).
3. Embargo windows to eliminate temporal autocorrelation or multi-day event leakage.
4. Absolute prohibition of future-to-past data leakage.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Optional
import numpy as np
import pandas as pd


@dataclass(frozen=True)
class ChronologicalSplit:
    """Represents a single 4-stage chronological fold."""
    fold_idx: int
    train_indices: np.ndarray
    tune_indices: np.ndarray
    cal_indices: np.ndarray
    test_indices: np.ndarray
    train_range: tuple
    tune_range: tuple
    cal_range: tuple
    test_range: tuple


class PurgedRollingOriginSplit:
    """Generates rolling-origin chronological splits with embargo buffers."""

    def __init__(
        self,
        train_window_days: int = 365,
        tune_window_days: int = 60,
        cal_window_days: int = 30,
        test_window_days: int = 30,
        embargo_days: int = 7,
        step_days: int = 30
    ):
        self.train_window_days = train_window_days
        self.tune_window_days = tune_window_days
        self.cal_window_days = cal_window_days
        self.test_window_days = test_window_days
        self.embargo_days = embargo_days
        self.step_days = step_days

    def split(
        self,
        df: pd.DataFrame,
        date_col: str
    ) -> Generator[ChronologicalSplit, None, None]:
        """Generate rolling chronological splits over DataFrame sorted by date_col."""
        if date_col not in df.columns:
            raise KeyError(f"Date column '{date_col}' not found")

        # Create sorted date index
        dates = pd.to_datetime(df[date_col]).values
        sorted_order = np.argsort(dates)
        sorted_dates = dates[sorted_order]

        min_date = pd.to_datetime(sorted_dates[0])
        max_date = pd.to_datetime(sorted_dates[-1])

        # Initial test end target
        total_window = (
            timedelta(days=self.train_window_days)
            + timedelta(days=self.embargo_days)
            + timedelta(days=self.tune_window_days)
            + timedelta(days=self.embargo_days)
            + timedelta(days=self.cal_window_days)
            + timedelta(days=self.embargo_days)
            + timedelta(days=self.test_window_days)
        )

        if max_date - min_date < total_window:
            # If dataset is shorter than full rolling window, create a single proportional split
            # partitioned strictly by date intervals with purged embargos to prevent temporal leakage
            # and guarantee identical timestamps are never split across folds.
            total_span = (max_date - min_date).total_seconds()
            embargo_buffer_seconds = 3 * timedelta(days=self.embargo_days).total_seconds()

            dt_series = pd.to_datetime(sorted_dates)
            unique_dates = np.sort(np.unique(dt_series))
            if len(unique_dates) < 4:
                raise ValueError(
                    f"Insufficient unique dates ({len(unique_dates)}) to partition into "
                    f"TRAIN, TUNE, CAL, and TEST folds without temporal leakage."
                )

            if total_span > embargo_buffer_seconds and self.embargo_days > 0:
                active_seconds = total_span - embargo_buffer_seconds
                train_dur = active_seconds * 0.50
                tune_dur = active_seconds * 0.20
                cal_dur = active_seconds * 0.15
                test_dur = active_seconds * 0.15

                embargo_delta = timedelta(days=self.embargo_days)
                train_start = min_date
                train_end = train_start + timedelta(seconds=train_dur)

                tune_start = train_end + embargo_delta
                tune_end = tune_start + timedelta(seconds=tune_dur)

                cal_start = tune_end + embargo_delta
                cal_end = cal_start + timedelta(seconds=cal_dur)

                test_start = cal_end + embargo_delta
                test_end = max_date

                train_mask = (dt_series >= train_start) & (dt_series <= train_end)
                tune_mask = (dt_series >= tune_start) & (dt_series <= tune_end)
                cal_mask = (dt_series >= cal_start) & (dt_series <= cal_end)
                test_mask = (dt_series >= test_start) & (dt_series <= test_end)
            else:
                # If span is too tight for full multi-day embargos, partition strictly by unique date boundaries
                n_u = len(unique_dates)
                u_train = set(unique_dates[: max(1, int(n_u * 0.50))])
                u_tune = set(unique_dates[int(n_u * 0.50): max(int(n_u * 0.50) + 1, int(n_u * 0.70))])
                u_cal = set(unique_dates[int(n_u * 0.70): max(int(n_u * 0.70) + 1, int(n_u * 0.85))])
                u_test = set(unique_dates[int(n_u * 0.85):])

                # Ensure disjoint sets
                u_tune = u_tune - u_train
                u_cal = u_cal - u_train - u_tune
                u_test = u_test - u_train - u_tune - u_cal

                train_mask = np.isin(dt_series, list(u_train))
                tune_mask = np.isin(dt_series, list(u_tune))
                cal_mask = np.isin(dt_series, list(u_cal))
                test_mask = np.isin(dt_series, list(u_test))

                train_start = pd.to_datetime(min(u_train)) if u_train else min_date
                train_end = pd.to_datetime(max(u_train)) if u_train else min_date
                tune_start = pd.to_datetime(min(u_tune)) if u_tune else None
                tune_end = pd.to_datetime(max(u_tune)) if u_tune else None
                cal_start = pd.to_datetime(min(u_cal)) if u_cal else None
                cal_end = pd.to_datetime(max(u_cal)) if u_cal else None
                test_start = pd.to_datetime(min(u_test)) if u_test else None
                test_end = pd.to_datetime(max(u_test)) if u_test else max_date

            yield ChronologicalSplit(
                fold_idx=0,
                train_indices=sorted_order[train_mask],
                tune_indices=sorted_order[tune_mask],
                cal_indices=sorted_order[cal_mask],
                test_indices=sorted_order[test_mask],
                train_range=(train_start, train_end),
                tune_range=(tune_start, tune_end),
                cal_range=(cal_start, cal_end),
                test_range=(test_start, test_end)
            )
            return

        fold = 0
        current_test_end = min_date + total_window

        while current_test_end <= max_date + timedelta(days=self.step_days):
            test_start = current_test_end - timedelta(days=self.test_window_days)
            cal_end = test_start - timedelta(days=self.embargo_days)
            cal_start = cal_end - timedelta(days=self.cal_window_days)
            tune_end = cal_start - timedelta(days=self.embargo_days)
            tune_start = tune_end - timedelta(days=self.tune_window_days)
            train_end = tune_start - timedelta(days=self.embargo_days)
            train_start = train_end - timedelta(days=self.train_window_days)

            # Mask boolean arrays
            dt_series = pd.to_datetime(sorted_dates)
            train_mask = (dt_series >= train_start) & (dt_series <= train_end)
            tune_mask = (dt_series >= tune_start) & (dt_series <= tune_end)
            cal_mask = (dt_series >= cal_start) & (dt_series <= cal_end)
            test_mask = (dt_series >= test_start) & (dt_series <= current_test_end)

            if train_mask.sum() > 0 and test_mask.sum() > 0:
                yield ChronologicalSplit(
                    fold_idx=fold,
                    train_indices=sorted_order[train_mask],
                    tune_indices=sorted_order[tune_mask],
                    cal_indices=sorted_order[cal_mask],
                    test_indices=sorted_order[test_mask],
                    train_range=(train_start, train_end),
                    tune_range=(tune_start, tune_end),
                    cal_range=(cal_start, cal_end),
                    test_range=(test_start, current_test_end)
                )
                fold += 1

            current_test_end += timedelta(days=self.step_days)

