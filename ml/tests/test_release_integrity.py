"""Regression cases for real receipt custody, future feedback and probability limits."""
import hashlib
from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

from ml.core.metrics import log_loss
from ml.decision.bandit import LinTS
from ml.decision import lab
from ml.shadow import lane
from ml.tests.test_decision_and_lane import _setup_receipt


def test_literal_certainty_log_loss_is_zero_or_infinite_not_nan():
    score = log_loss([0, 1, 0, 1], [0, 1, 1, 0])
    assert score[:2].tolist() == [0, 0]
    assert np.isinf(score[2:]).all()
    assert not np.isnan(score).any()


def test_logged_propensity_is_the_distribution_actually_sampled(monkeypatch):
    b = LinTS(1, (0, 1), seed=1)
    monkeypatch.setattr(b, "_sample_scores", lambda x, n: np.tile([1.0, 0.0], (n, 1)))

    class Picker:
        def choice(self, count, p):
            self.actual = p.copy()
            return 1  # A legitimate, rare draw from the exploration mass.

    picker = Picker()
    b.rng = picker
    action, logged = b.choose(np.ones(1))
    assert action == 1
    np.testing.assert_array_equal(logged, picker.actual)
    assert logged[1] > 0


def test_bandit_rejects_invalid_context_or_sampling_count():
    b = LinTS(2)
    with pytest.raises(ValueError):
        b.choose(np.array([np.nan, 1]))
    with pytest.raises(ValueError):
        b.choose(np.ones(2), n_prop=0)


def test_working_only_receipt_does_not_establish_commit(tmp_path, monkeypatch):
    f = tmp_path / "SHADOW_FORECASTS_2026-W43.csv"
    f.write_text("event_key,line,scheduled_start_utc\nE1,2.5,2026-10-20T00:00:00Z\n", encoding="utf-8")
    start = datetime(2026, 10, 20, tzinfo=timezone.utc)
    _setup_receipt(tmp_path, monkeypatch, start, hashlib.sha256(f.read_bytes()).hexdigest(), commit=False)
    with pytest.raises(ValueError, match="committed receipt"):
        lane.reveal(f, "M-r1", start + timedelta(days=1))


def test_multi_event_reveal_waits_for_last_event(tmp_path, monkeypatch):
    f = tmp_path / "SHADOW_FORECASTS_2026-W43.csv"
    f.write_text("event_key,line,scheduled_start_utc\nE1,2.5,2026-10-20T00:00:00Z\n"
                 "E2,2.5,2026-10-21T00:00:00Z\n", encoding="utf-8")
    start = datetime(2026, 10, 20, tzinfo=timezone.utc)
    _setup_receipt(tmp_path, monkeypatch, start, hashlib.sha256(f.read_bytes()).hexdigest())
    with pytest.raises(ValueError, match="not all scheduled starts"):
        lane.reveal(f, "M-r1", start + timedelta(hours=1))
    assert lane.reveal(f, "M-r1", start + timedelta(days=1, minutes=1)).read_bytes() == f.read_bytes()


def test_uncommitted_receipt_edit_is_rejected(tmp_path, monkeypatch):
    f = tmp_path / "SHADOW_FORECASTS_2026-W43.csv"
    f.write_text("event_key,line,scheduled_start_utc\nE1,2.5,2026-10-20T00:00:00Z\n", encoding="utf-8")
    start = datetime(2026, 10, 20, tzinfo=timezone.utc)
    d = _setup_receipt(tmp_path, monkeypatch, start, hashlib.sha256(f.read_bytes()).hexdigest())
    with (d / "FREEZE_RECEIPTS.md").open("a", encoding="utf-8") as fh:
        fh.write("uncommitted correction\n")
    with pytest.raises(ValueError, match="differs from the committed"):
        lane.reveal(f, "M-r1", start + timedelta(days=1))


def test_partial_final_is_unresolved_and_duplicate_final_rejected():
    forecast = pd.DataFrame([{"shadow_row_id": "a", "event_key": "E1", "family": "TOTAL",
                              "orientation": "OVER", "line": 2.5}])
    final = pd.DataFrame([{"event_key": "E1", "hs": 3}])
    assert lane.settle_rows(forecast, final, "https://example.invalid", "A").iloc[0]["result"] == "UNRESOLVED"
    with pytest.raises(ValueError, match="duplicate final"):
        lane.settle_rows(forecast, pd.concat([final, final]), "https://example.invalid", "A")


def test_freeze_rejects_empty_late_or_naive_fixture_before_loading(tmp_path):
    lg = SimpleNamespace()
    with pytest.raises(ValueError, match="nonempty fixtures"):
        lane.freeze("M", lg, {}, pd.DataFrame(), tmp_path, "v1", "x", "x", "2026-01-01T00:00:00Z")
    fc = pd.DataFrame([{"event_key": "E1", "season": 2026, "stage": "REG", "home": "A", "away": "B",
                        "scheduled_start_utc": "2020-01-01T00:00:00Z"}])
    with pytest.raises(ValueError, match="precede every event"):
        lane.freeze("M", lg, {}, fc, tmp_path, "v1", "x", "x", "2020-01-01T00:00:00Z")
    with pytest.raises(ValueError, match="explicit timezone"):
        lane.freeze("M", lg, {}, fc, tmp_path, "v1", "x", "x", "2020-01-01")


def test_day_batched_feedback_and_feasible_warmup(monkeypatch):
    frames, prices = [], []
    for season in (2021, 2022, 2023):
        date = pd.Timestamp(f"{season}-08-01")
        for game in range(2):
            row = {"season": season, "date": date, "home": f"H{game}", "away": f"A{game}",
                   "event_id": f"E{season}-{game}", "outcome_idx": 0, "fit_date": date - pd.Timedelta(days=1),
                   "week": f"{season}-W30"}
            for pref in ("MODEL", "BASE", "TB1"):
                row.update({f"{pref}_p_home": .6, f"{pref}_p_draw": .2, f"{pref}_p_away": .2})
            frames.append(row)
            prices.append({"season": season, "date": date, "home": f"H{game}", "away": f"A{game}", "ftr": "H",
                           "o_H": 2., "o_D": 3., "o_A": 4., "c_H": 1.9, "c_D": 3., "c_A": 4.})
    monkeypatch.setattr(lab, "load_prices", lambda: pd.DataFrame(prices))

    class TimingSpy:
        def __init__(self, *args, **kwargs):
            self.choices = self.updates = 0

        def choose(self, x):
            expected_updates = self.choices - self.choices % 2
            assert self.updates == expected_updates  # No first game's close before same-day second action.
            self.choices += 1
            return 1, np.ones(3) / 3

        def update(self, *args):
            self.updates += 1

    class FullSpy:
        def __init__(self, *args, **kwargs):
            pass

        def choose(self, x):
            return 1

        def update_all(self, *args):
            pass

    monkeypatch.setattr(lab, "LinTS", TimingSpy)
    monkeypatch.setattr(lab, "FullInfoRidge", FullSpy)
    result = lab.run(pd.DataFrame(frames))
    assert result["warmup_seasons"] == [2021, 2022]
    assert result["evaluation_seasons"] == [2023]
    assert result["feedback_timing"].startswith("DATE_BATCHED")


def test_run_receipt_rejects_changed_generating_source(monkeypatch):
    from ml import run

    monkeypatch.setattr(run, "code_digest", lambda: "stable")
    rec = {"code_sha256": "stable", "run_utc": "2026-10-14T00:00:00Z"}
    assert "completed_utc" in run.finish_receipt(rec)
    monkeypatch.setattr(run, "code_digest", lambda: "changed")
    with pytest.raises(RuntimeError, match="source changed"):
        run.finish_receipt(rec)


@pytest.mark.parametrize("cross_start", [False, True])
def test_freeze_records_completion_and_refuses_fit_crossing_start(monkeypatch, tmp_path, cross_start):
    before = datetime(2026, 10, 14, 9, 0, tzinfo=timezone.utc)
    finish = before + timedelta(minutes=2 if cross_start else .5)
    ticks = iter([before, finish])

    class Clock(datetime):
        @classmethod
        def now(cls, tz=None):
            return next(ticks)

    class FailedFit:
        def fit(self, *args):
            raise lane.FitError("explicit fixture failure")

    monkeypatch.setattr(lane, "datetime", Clock)
    monkeypatch.setattr(lane, "load_league", lambda lg: (pd.DataFrame({"date": [pd.Timestamp("2026-10-13")], "season": [2026], "stage": ["REG"]}), None))
    monkeypatch.setattr(lane, "snapshot_hash", lambda *a: "data")
    monkeypatch.setattr(lane, "make_model", lambda *a: FailedFit())
    lg = SimpleNamespace(path="Example/Test", endpoint="FULL_GAME", history_seasons=3, engine="gaussian")
    fc = pd.DataFrame([{"event_key": "E1", "season": 2026, "stage": "REG", "home": "A", "away": "B", "scheduled_start_utc": "2026-10-14T09:01:00Z"}])
    args = ("M", lg, {}, fc, tmp_path, "v1", "x", "x", "2026-10-14T08:59:00Z")
    if cross_start:
        with pytest.raises(ValueError, match="completed after event start"):
            lane.freeze(*args)
        assert not list(tmp_path.rglob("*.csv"))
    else:
        result = lane.freeze(*args)
        rows = pd.read_csv(result["path"])
        assert rows.iloc[0]["frozen_utc"] == finish.strftime("%Y-%m-%dT%H:%M:%SZ")
        assert rows.iloc[0]["status"].startswith("NOT_ISSUED:FIT_FAILED")
