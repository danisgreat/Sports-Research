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
            total_span_days = (max_date - min_date).total_seconds() / 86400.0
            embargo_buffer_days = 3.0 * float(self.embargo_days)

            dt_series = pd.to_datetime(sorted_dates)
            unique_dates = np.sort(np.unique(dt_series))
            if len(unique_dates) < 4:
                raise ValueError(
                    f"Insufficient unique dates ({len(unique_dates)}) to partition into "
                    f"TRAIN, TUNE, CAL, and TEST folds without temporal leakage."
                )

            if self.embargo_days > 0:
                # Strictly enforce requested embargo separation between folds
                if total_span_days <= embargo_buffer_days:
                    raise ValueError(
                        f"Dataset span ({total_span_days:.1f} days) is insufficient to satisfy requested "
                        f"embargo of {self.embargo_days} days across 4 partitions (requires > {embargo_buffer_days:.1f} days)."
                    )

                active_days = total_span_days - embargo_buffer_days
                train_dur = timedelta(days=active_days * 0.50)
                tune_dur = timedelta(days=active_days * 0.20)
                cal_dur = timedelta(days=active_days * 0.15)
                test_dur = timedelta(days=active_days * 0.15)
                embargo_delta = timedelta(days=self.embargo_days)

                train_start = min_date
                train_end = train_start + train_dur
                tune_start = train_end + embargo_delta
                tune_end = tune_start + tune_dur
                cal_start = tune_end + embargo_delta
                cal_end = cal_start + cal_dur
                test_start = cal_end + embargo_delta
                test_end = max_date

                # Half-open intervals prevent shared boundary observations
                train_mask = (dt_series >= train_start) & (dt_series < train_end)
                tune_mask = (dt_series >= tune_start) & (dt_series < tune_end)
                cal_mask = (dt_series >= cal_start) & (dt_series < cal_end)
                test_mask = (dt_series >= test_start) & (dt_series <= test_end)
            else:
                # With zero embargo, partition strictly by unique date slices ensuring every fold is non-empty
                n_u = len(unique_dates)
                i1 = max(1, int(n_u * 0.50))
                i2 = max(i1 + 1, int(n_u * 0.70))
                i3 = max(i2 + 1, int(n_u * 0.85))
                if i3 >= n_u:
                    i3 = n_u - 1
                    i2 = min(i2, i3 - 1)
                    i1 = min(i1, i2 - 1)
                if i1 < 1 or i2 <= i1 or i3 <= i2:
                    i1, i2, i3 = 1, 2, 3

                u_train = set(unique_dates[0:i1])
                u_tune = set(unique_dates[i1:i2])
                u_cal = set(unique_dates[i2:i3])
                u_test = set(unique_dates[i3:n_u])

                train_mask = np.isin(dt_series, list(u_train))
                tune_mask = np.isin(dt_series, list(u_tune))
                cal_mask = np.isin(dt_series, list(u_cal))
                test_mask = np.isin(dt_series, list(u_test))

                train_start = pd.to_datetime(min(u_train))
                train_end = pd.to_datetime(max(u_train))
                tune_start = pd.to_datetime(min(u_tune))
                tune_end = pd.to_datetime(max(u_tune))
                cal_start = pd.to_datetime(min(u_cal))
                cal_end = pd.to_datetime(max(u_cal))
                test_start = pd.to_datetime(min(u_test))
                test_end = pd.to_datetime(max(u_test))

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

            # Mask boolean arrays using half-open intervals to strictly prevent sharing boundary observations
            dt_series = pd.to_datetime(sorted_dates)
            train_mask = (dt_series >= train_start) & (dt_series < train_end)
            tune_mask = (dt_series >= tune_start) & (dt_series < tune_end)
            cal_mask = (dt_series >= cal_start) & (dt_series < cal_end)
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

