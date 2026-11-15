"""CARD-TRAIN-v1: settled card records are ingested, admitted and used in a walk-forward training run.

Synthetic EXAMPLE rows only."""
import numpy as np
import pandas as pd
import pytest

from ml import card_training as C


def history(weeks=12, per_week=40, seed=3):
    rng = np.random.default_rng(seed)
    rows, start = [], pd.Timestamp("2026-08-03")
    for w in range(weeks):
        for i in range(per_week):
            day = start + pd.Timedelta(days=7 * w + i % 5)
            p = float(rng.uniform(.3, .8))
            win = rng.uniform() < p
            rows.append(dict(card=f"P-{w * per_week + i // 4 + 1:03d}", rank=str(i % 4 + 1), date=day.date().isoformat(),
                             week=f"2026-W{day.isocalendar().week:02d}", era="E4", sport=("Soccer", "Basketball")[i % 2],
                             family=("TOTAL", "HANDICAP")[i % 3 == 0], contract=("EXAMPLE Over 2.5", "EXAMPLE +3.5")[i % 2],
                             p="" if i % 5 == 0 else repr(round(p, 3)), grade="WIN" if win else "LOSS",
                             probability_role="", cohort="EXAMPLE", source="EXAMPLE.md:1"))
    rows += [dict(rows[0], grade="PUSH"), dict(rows[1], grade="UNRESOLVED"), dict(rows[2], date="", era="UNDATED")]
    return pd.DataFrame(rows)


def test_every_row_is_admitted_or_excluded_with_a_reason():
    rows = C.admit(history())
    assert len(rows) == 12 * 40 + 3
    assert set(rows.admission) == {"OUTCOME_AND_CALIBRATION", "OUTCOME_ONLY", "EXCLUDED"}
    assert set(rows[rows.admission == "EXCLUDED"].reason) == {"NOT_DECISIVE:PUSH", "NOT_DECISIVE:UNRESOLVED", "UNDATED"}
    assert (rows[rows.admission == "OUTCOME_ONLY"].reason == "NO_STATED_P").all()
    assert (rows[rows.admission != "EXCLUDED"].y.isin(["0", "1"])).all()


def test_walk_forward_never_trains_on_its_own_week_or_later():
    rows = C.admit(history())
    pred = C.walk_forward(rows)
    assert len(pred) > 0 and set(pred.row_id) <= set(rows.row_id)
    by_week = rows[rows.admission != "EXCLUDED"].copy()
    by_week["issued"] = pd.to_datetime(by_week.date, utc=True)
    for week, g in pred.groupby("week"):
        first = by_week[by_week.week == week].issued.min()
        monday = first.normalize() - pd.Timedelta(days=first.weekday())
        earlier = by_week[(by_week.issued < monday) & (by_week.issued + C.OUTCOME_LAG <= monday)]
        assert set(g.outcome_train_rows.astype(int)) == {len(earlier)}


def test_changing_a_later_outcome_cannot_change_an_earlier_prediction():
    rows = C.admit(history())
    before = C.walk_forward(rows)
    last = rows[rows.admission != "EXCLUDED"].date.max()
    flipped = rows.copy()
    mask = (flipped.date == last) & (flipped.admission != "EXCLUDED")
    flipped.loc[mask, "y"] = flipped.loc[mask, "y"].map({"0": "1", "1": "0"})
    after = C.walk_forward(flipped)
    early = before[before.week < before.week.max()].row_id
    cols = ["outcome_model", "cal_platt", "cal_sport_platt"]
    pd.testing.assert_frame_equal(before.set_index("row_id").loc[early, cols], after.set_index("row_id").loc[early, cols])


def test_scores_report_card_clustered_intervals():
    pred = C.walk_forward(C.admit(history()))
    s = C._scores(pred, "outcome_model", "outcome_base_rate")
    assert s["rows"] == len(pred) and s["cards"] == pred.card.nunique()
    assert s["interval_low"] <= s["card_mean_brier_difference"] <= s["interval_high"]


def test_run_output_is_immutable(tmp_path):
    (tmp_path / "RUN").mkdir()
    with pytest.raises(FileExistsError):
        C.run(tmp_path / "RUN")


def test_direction_reads_over_and_under():
    assert C.direction("Over 2.5 goals") == "OVER" and C.direction("Team Under 160.5") == "UNDER"
    assert C.direction("Home -3.5") == "OTHER"
