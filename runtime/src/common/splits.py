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
            n = len(df)
            n_train = int(n * 0.50)
            n_tune = int(n * 0.15)
            n_cal = int(n * 0.15)
            
            train_idx = sorted_order[:n_train]
            tune_idx = sorted_order[n_train:n_train + n_tune]
            cal_idx = sorted_order[n_train + n_tune:n_train + n_tune + n_cal]
            test_idx = sorted_order[n_train + n_tune + n_cal:]

            yield ChronologicalSplit(
                fold_idx=0,
                train_indices=train_idx,
                tune_indices=tune_idx,
                cal_indices=cal_idx,
                test_indices=test_idx,
                train_range=(sorted_dates[0], sorted_dates[n_train - 1] if n_train > 0 else sorted_dates[0]),
                tune_range=(sorted_dates[n_train], sorted_dates[n_train + n_tune - 1]) if n_tune > 0 else (None, None),
                cal_range=(sorted_dates[n_train + n_tune], sorted_dates[n_train + n_tune + n_cal - 1]) if n_cal > 0 else (None, None),
                test_range=(sorted_dates[n_train + n_tune + n_cal], sorted_dates[-1]) if len(test_idx) > 0 else (None, None)
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

