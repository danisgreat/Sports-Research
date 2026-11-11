"""Count-triggered assessment: no elapsed-week wait, no contract-count inflation."""
from pathlib import Path

import pandas as pd
import pytest

from ml import external_evaluation as E, research_intake as I
from ml.evaluation import prospective as P, event_assessment as A
from ml.tests.test_learning_governance import _rows


def sample(tmp_path, n=100, contracts=1):
    ledger = tmp_path / "FORECASTS.csv"; outcomes = tmp_path / "OUTCOMES.csv"; labels = []
    # All one hundred games fit in one actual event day, and settle inside an unfinished ISO week.
    start = pd.Timestamp("2026-11-10T09:00:00Z")
    forecasts = []
    for i in range(n):
        for name, prob in (("SINGLE_RESEARCH", .51), ("FIVE_LANES", .65 if i % 2 else .35), ("REFERENCE", .5), ("BASELINE", .5)):
            for j in range(contracts):
                row = _rows(name, "v24.15", "CANDIDATE" if name == "FIVE_LANES" else "CHAMPION", f"EXAMPLE:{i:03}", start, prob, 1,
                            issued=start-pd.Timedelta(hours=1 if name == "FIVE_LANES" else 2))
                row["contract_key"] = "WIN-H-" + str(j); forecasts.append(row)
        for j in range(contracts):
            labels.append(dict(event_id=f"EXAMPLE:{i:03}", contract_key="WIN-H-" + str(j), result="WIN" if i % 2 else "LOSS",
                               final_at=(start+pd.Timedelta(hours=2)).isoformat(),
                               available_at=(start+pd.Timedelta(hours=3, seconds=i)).isoformat(), evidence_sha256="a"*64))
    P.freeze(ledger, forecasts, now=start-pd.Timedelta(minutes=30))
    outcomes.write_bytes(I.csv_bytes(P.OUTCOME_FIELDS, labels))
    return ledger, outcomes, labels


def test_100_games_can_be_assessed_in_one_day_without_waiting_for_week_end(tmp_path):
    ledger, outcomes, _ = sample(tmp_path)
    rows = E.evaluate(ledger, outcomes, tmp_path / "REPORT", as_of="2026-11-10T13:00:00Z")
    assert rows[0]["assessment_status"] == "READY" and rows[0]["paired_events"] == 100
    assert rows[0]["minimum_weeks"] == 0 and rows[0]["settled_weeks"] == 1
    assert rows[0]["analysis_unit"] == "EVENT"
    assert "weeks" not in rows[0]["reason"]
    assert I.read(tmp_path / "REPORT/COHORT_RECEIPT.csv")[0]["decision_window"] == "FROZEN_FIRST_100_SETTLED_EVENTS"


def test_99_games_are_not_enough_even_with_many_contracts(tmp_path):
    ledger, outcomes, _ = sample(tmp_path, n=99, contracts=3)
    rows = E.evaluate(ledger, outcomes, tmp_path / "REPORT", as_of="2026-11-10T13:00:00Z")
    assert rows[0]["paired_events"] == 99 and rows[0]["assessment_status"] != "READY"
    assert rows[0]["disposition"] == "INSUFFICIENT_EVIDENCE"


def test_only_complete_shared_contract_settlements_count(tmp_path):
    ledger, outcomes, labels = sample(tmp_path, contracts=2)
    labels[-1]["result"] = "UNRESOLVED"
    outcomes.write_bytes(I.csv_bytes(P.OUTCOME_FIELDS, labels))
    rows = E.evaluate(ledger, outcomes, tmp_path / "PARTIAL", as_of="2026-11-10T13:00:00Z")
    assert rows[0]["paired_events"] == 99
    labels[-1]["result"] = "PUSH"
    outcomes.write_bytes(I.csv_bytes(P.OUTCOME_FIELDS, labels))
    rows = E.evaluate(ledger, outcomes, tmp_path / "TERMINAL", as_of="2026-11-10T13:00:00Z")
    assert rows[0]["paired_events"] == 100 and rows[0]["assessment_status"] == "READY"


def test_future_unavailable_and_all_push_games_do_not_trigger_assessment(tmp_path):
    ledger, outcomes, labels = sample(tmp_path)
    labels[-1]["available_at"] = "2026-11-11T13:00:00Z"
    outcomes.write_bytes(I.csv_bytes(P.OUTCOME_FIELDS, labels))
    rows = E.evaluate(ledger, outcomes, tmp_path / "FUTURE", as_of="2026-11-10T13:00:00Z")
    assert rows[0]["paired_events"] == 99
    labels[-1]["available_at"] = "2026-11-10T12:01:39+00:00"; labels[-1]["result"] = "PUSH"
    outcomes.write_bytes(I.csv_bytes(P.OUTCOME_FIELDS, labels))
    rows = E.evaluate(ledger, outcomes, tmp_path / "PUSH", as_of="2026-11-10T13:00:00Z")
    assert rows[0]["paired_events"] == 99


def test_first_100_settled_cohort_is_fixed_and_can_be_reused(tmp_path):
    ledger, outcomes, labels = sample(tmp_path, n=105)
    # Game 0 settles last, so the first 100 eligible settled games are IDs 1..100.
    labels[0]["available_at"] = "2026-11-11T13:00:00Z"
    outcomes.write_bytes(I.csv_bytes(P.OUTCOME_FIELDS, labels))
    E.evaluate(ledger, outcomes, tmp_path / "FIRST", as_of="2026-11-10T13:00:00Z")
    cohort = tmp_path / "FIRST/COHORT.csv"
    ids = {r["event_id"] for r in I.read(cohort)}
    assert "EXAMPLE:000" not in ids and len(ids) == 100
    E.evaluate(ledger, outcomes, tmp_path / "LATER", as_of="2026-11-12T13:00:00Z", cohort=cohort)
    assert cohort.read_bytes() == (tmp_path / "LATER/COHORT.csv").read_bytes()
    cohort.write_bytes(cohort.read_bytes().replace(b"EXAMPLE:001", b"EXAMPLE:000"))
    with pytest.raises(ValueError, match="receipt/hash"):
        E.evaluate(ledger, outcomes, tmp_path / "TAMPERED", as_of="2026-11-12T13:00:00Z", cohort=cohort)


def test_event_interval_averages_contracts_without_inflating_games():
    iv = A.paired_event_interval(pd.Series([-.1, -.1, .1]), pd.Series(["A", "A", "B"]), pd.Series(["W1"]*3))
    assert iv["n_events"] == 2 and iv["mean"] == pytest.approx(0)
    assert iv["status"] == "SPANS_ZERO" and iv["k_weeks"] == 1


def test_legacy_week_mode_is_not_silently_changed(tmp_path):
    ledger, outcomes, _ = sample(tmp_path)
    rows = P.verify_ledger(ledger); labels = pd.read_csv(outcomes, dtype=str, keep_default_na=False)
    legacy = P.evaluate(rows, labels, E.MODELS[0], E.FIVE, delta=.01)
    assert legacy["disposition"] == "INSUFFICIENT_EVIDENCE" and "weeks" in legacy["reason"]
    current = A.evaluate(rows, labels, E.MODELS[0], E.FIVE, delta=.01, assessment_unit="EVENT")
    assert current["assessment_unit"] == "EVENT" and current["weeks_needed"] is None
    assert "weeks" not in current["reason"]
