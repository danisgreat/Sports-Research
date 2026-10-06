"""Unit tests for chronological rolling-origin splits with embargos."""

from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import pytest

from runtime.src.common.splits import PurgedRollingOriginSplit


def test_purged_rolling_split():
    # Construct 3 years of daily events
    base_date = datetime(2022, 1, 1)
    dates = [base_date + timedelta(days=i) for i in range(1000)]
    df = pd.DataFrame({
        "match_id": [f"m_{i}" for i in range(1000)],
        "match_date": dates
    })

    splitter = PurgedRollingOriginSplit(
        train_window_days=365,
        tune_window_days=60,
        cal_window_days=30,
        test_window_days=30,
        embargo_days=7,
        step_days=60
    )

    splits = list(splitter.split(df, "match_date"))
    assert len(splits) > 0

    for s in splits:
        # Check indices are disjoint
        all_idx = np.concatenate([s.train_indices, s.tune_indices, s.cal_indices, s.test_indices])
        assert len(all_idx) == len(np.unique(all_idx))

        # Check chronological ordering: max(train) < min(tune) < min(cal) < min(test)
        train_dates = pd.to_datetime(df.iloc[s.train_indices]["match_date"])
        tune_dates = pd.to_datetime(df.iloc[s.tune_indices]["match_date"])
        cal_dates = pd.to_datetime(df.iloc[s.cal_indices]["match_date"])
        test_dates = pd.to_datetime(df.iloc[s.test_indices]["match_date"])

        assert train_dates.max() < tune_dates.min()
        assert tune_dates.max() < cal_dates.min()
        assert cal_dates.max() < test_dates.min()

        # Check embargo buffer between cal and test
        assert (test_dates.min() - cal_dates.max()).days >= 7


def test_short_dataset_fallback():
    # Dataset shorter than rolling window
    base_date = datetime(2025, 1, 1)
    dates = [base_date + timedelta(days=i) for i in range(100)]
    df = pd.DataFrame({"match_id": [f"m_{i}" for i in range(100)], "match_date": dates})

    splitter = PurgedRollingOriginSplit()
    splits = list(splitter.split(df, "match_date"))
    assert len(splits) == 1
    assert len(splits[0].train_indices) > 0
    assert len(splits[0].test_indices) > 0

