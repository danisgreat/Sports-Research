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

    s = splits[0]
    train_dates = pd.to_datetime(df.iloc[s.train_indices]["match_date"])
    tune_dates = pd.to_datetime(df.iloc[s.tune_indices]["match_date"])
    cal_dates = pd.to_datetime(df.iloc[s.cal_indices]["match_date"])
    test_dates = pd.to_datetime(df.iloc[s.test_indices]["match_date"])

    # Strict chronological ordering
    assert train_dates.max() < tune_dates.min()
    assert tune_dates.max() < cal_dates.min()
    assert cal_dates.max() < test_dates.min()

    # Embargo buffer strictly enforced between folds
    assert (tune_dates.min() - train_dates.max()).days >= 7
    assert (cal_dates.min() - tune_dates.max()).days >= 7
    assert (test_dates.min() - cal_dates.max()).days >= 7


def test_splits_never_separate_identical_timestamps():
    """Verify that multiple observations sharing the exact same timestamp are never split across folds."""
    # 5 events per day across 30 days (150 rows)
    base_date = datetime(2025, 3, 1)
    dates = []
    for day in range(30):
        d = base_date + timedelta(days=day)
        dates.extend([d] * 5)  # 5 rows sharing the exact timestamp

    df = pd.DataFrame({
        "match_id": [f"m_{i}" for i in range(len(dates))],
        "match_date": dates
    })

    splitter = PurgedRollingOriginSplit(embargo_days=3)
    splits = list(splitter.split(df, "match_date"))
    assert len(splits) == 1

    s = splits[0]
    train_d = set(pd.to_datetime(df.iloc[s.train_indices]["match_date"]))
    tune_d = set(pd.to_datetime(df.iloc[s.tune_indices]["match_date"]))
    cal_d = set(pd.to_datetime(df.iloc[s.cal_indices]["match_date"]))
    test_d = set(pd.to_datetime(df.iloc[s.test_indices]["match_date"]))

    # Date sets must have zero overlap
    assert len(train_d.intersection(tune_d)) == 0
    assert len(tune_d.intersection(cal_d)) == 0
    assert len(cal_d.intersection(test_d)) == 0
    assert len(train_d.intersection(test_d)) == 0


def test_ten_daily_with_seven_day_embargo_raises():
    """Verify that requesting 7-day embargo on 10 consecutive daily observations raises ValueError."""
    base_date = datetime(2025, 1, 1)
    dates = [base_date + timedelta(days=i) for i in range(10)]
    df = pd.DataFrame({"match_id": [f"m_{i}" for i in range(10)], "match_date": dates})

    splitter = PurgedRollingOriginSplit(embargo_days=7)
    with pytest.raises(ValueError, match="insufficient to satisfy requested embargo"):
        list(splitter.split(df, "match_date"))


def test_four_unique_dates_non_empty_cal():
    """Verify that 4 unique dates partition into non-empty TRAIN, TUNE, CAL, and TEST folds."""
    base_date = datetime(2025, 1, 1)
    dates = [base_date + timedelta(days=i) for i in range(4)]
    df = pd.DataFrame({"match_id": [f"m_{i}" for i in range(4)], "match_date": dates})

    splitter = PurgedRollingOriginSplit(embargo_days=0)
    splits = list(splitter.split(df, "match_date"))
    assert len(splits) == 1
    s = splits[0]
    assert len(s.train_indices) >= 1
    assert len(s.tune_indices) >= 1
    assert len(s.cal_indices) >= 1
    assert len(s.test_indices) >= 1


def test_zero_embargo_disjoint_boundaries():
    """Verify that adjacent partitions never share boundary observations when embargo is zero."""
    base_date = datetime(2020, 1, 1)
    dates = [base_date + timedelta(days=i) for i in range(800)]
    df = pd.DataFrame({"match_id": [f"m_{i}" for i in range(800)], "match_date": dates})

    splitter = PurgedRollingOriginSplit(
        train_window_days=180,
        tune_window_days=60,
        cal_window_days=30,
        test_window_days=30,
        embargo_days=0,
        step_days=30
    )
    splits = list(splitter.split(df, "match_date"))
    assert len(splits) > 0
    for s in splits:
        train_set = set(s.train_indices)
        tune_set = set(s.tune_indices)
        cal_set = set(s.cal_indices)
        test_set = set(s.test_indices)

        assert len(train_set & tune_set) == 0
        assert len(tune_set & cal_set) == 0
        assert len(cal_set & test_set) == 0
        assert len(train_set & test_set) == 0



