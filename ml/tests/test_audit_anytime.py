"""AUDIT-ANYTIME-v1 (CR-2026.11.15-R3): a comprehensive audit runs on request at any game count.

Synthetic EXAMPLE events only."""
from pathlib import Path

import pytest

from ml import external_evaluation as E, research_intake as I
from ml.tests.test_assessment_100 import sample

ROOT = Path(__file__).resolve().parents[2]
AS_OF = "2026-11-10T13:00:00Z"


def test_an_on_request_audit_runs_on_21_games_and_reports_its_scores(tmp_path):
    ledger, outcomes, _ = sample(tmp_path, n=21)
    rows = E.evaluate(ledger, outcomes, tmp_path / "AUDIT", as_of=AS_OF, on_request=True)
    assert {r["assessment_status"] for r in rows} == {"AUDITED_ON_REQUEST"}
    assert rows[0]["paired_events"] == 21 and rows[0]["mean_brier_difference"] != ""
    assert rows[0]["interval_low"] != "" and rows[0]["interval_high"] != ""
    receipt = I.read(tmp_path / "AUDIT/COHORT_RECEIPT.csv")[0]
    assert receipt["decision_window"] == "ON_REQUEST_ALL_ELIGIBLE_TO_DATE" and receipt["events"] == "21"
    assert "AUDIT-ANYTIME-v1" in (tmp_path / "AUDIT/README.md").read_text(encoding="utf-8")


def test_an_on_request_audit_covers_every_eligible_game_not_only_the_first_100(tmp_path):
    ledger, outcomes, _ = sample(tmp_path, n=105)
    rows = E.evaluate(ledger, outcomes, tmp_path / "ALL", as_of=AS_OF, on_request=True)
    assert rows[0]["paired_events"] == 105
    frozen = E.evaluate(ledger, outcomes, tmp_path / "FROZEN", as_of=AS_OF)
    assert frozen[0]["paired_events"] == 100 and frozen[0]["assessment_status"] == "READY"


def test_an_on_request_audit_never_decides_promotion(tmp_path, monkeypatch):
    ledger, outcomes, _ = sample(tmp_path, n=150)
    real = E.A.evaluate
    monkeypatch.setattr(E.A, "evaluate", lambda *a, **k: dict(real(*a, **k), disposition="PROMOTION_ELIGIBLE"))
    frozen = E.evaluate(ledger, outcomes, tmp_path / "FROZEN", as_of=AS_OF)
    assert frozen[0]["disposition"] == "PROMOTION_ELIGIBLE"  # the frozen first-100 cohort can still decide
    rows = E.evaluate(ledger, outcomes, tmp_path / "AUDIT", as_of=AS_OF, on_request=True)
    assert all(r["disposition"] != "PROMOTION_ELIGIBLE" for r in rows)


def test_on_request_cannot_replace_the_frozen_cohort(tmp_path):
    ledger, outcomes, _ = sample(tmp_path)
    E.evaluate(ledger, outcomes, tmp_path / "FIRST", as_of=AS_OF)
    with pytest.raises(ValueError, match="on-request"):
        E.evaluate(ledger, outcomes, tmp_path / "MIXED", as_of=AS_OF, cohort=tmp_path / "FIRST/COHORT.csv", on_request=True)


def test_the_command_line_accepts_on_request(tmp_path, capsys):
    ledger, outcomes, _ = sample(tmp_path, n=5)
    I.main(["evaluate", "--forecasts", str(ledger), "--outcomes", str(outcomes), "--out", str(tmp_path / "CLI"), "--on-request"])
    assert I.read(tmp_path / "CLI/COHORT_RECEIPT.csv")[0]["decision_window"] == "ON_REQUEST_ALL_ELIGIBLE_TO_DATE"


def test_prompt_6_and_the_rules_allow_an_audit_at_any_time():
    prompt = (ROOT / "research/prompts/6_COMBINED_LOG_RETROSPECTIVE.md").read_text(encoding="utf-8")
    assert "AUDIT-ANYTIME-v1" in prompt and "--on-request" in prompt and "at any number of settled games" in prompt
    for doc in ("CORE.md", "SCORING_AND_VALIDATION.md", "RULES_REFERENCE.md", "research/external/EVALUATION_PLAN_v24.19.md"):
        assert "AUDIT-ANYTIME-v1" in (ROOT / doc).read_text(encoding="utf-8"), doc
