"""TIMING-v3 (CR-2026.11.15-R1): research begun before the actual start counts with PREGAME cards.

Synthetic EXAMPLE competitions and LOCAL-EXAMPLE keys only."""
import pandas as pd
import pytest

from ml import ledger as L, picks as P
from ml.tests.test_picks_ledger import KEY, lint, mini, render, root  # noqa: F401  (root is a fixture)

# Scheduled 10:00, research began 09:40, not-started seen 09:58, card finished 10:20 (after the start).
LATE = dict(timing="PRE_START_RESEARCH", issued_at="2026-10-22T10:20:00+00:00", research_started_at="2026-10-22T09:40:00+00:00",
            not_started_observed_at="2026-10-22T09:58:00+00:00", not_started_source="https://example.org/match-centre/1",
            outcome_exposure="NONE_RECORDED")


def test_a_card_finished_after_the_start_lints_clean_when_research_began_before_it(root):
    assert lint(root, LATE) == []


@pytest.mark.parametrize("change,needle", [
    (dict(research_started_at=""), "requires research_started_at"),
    (dict(not_started_source=""), "requires not_started_source"),
    (dict(outcome_exposure="LIVE_OBSERVED"), "outcome_exposure NONE_RECORDED"),
    (dict(not_started_source="the live page"), "must be the URL"),
    (dict(not_started_observed_at="2026-10-22T09:30:00+00:00"), "at or after research_started_at"),
    (dict(research_started_at="2026-10-22T10:30:00+00:00", not_started_observed_at="2026-10-22T10:31:00+00:00"), "must not be after issued_at"),
    (dict(issued_at="2026-10-22T09:50:00+00:00"), "use PREGAME"),
])
def test_missing_or_inconsistent_declarations_are_refused(root, change, needle):
    problems = lint(root, dict(LATE, **change))
    assert any(needle in p for p in problems), (needle, problems)


def test_the_ledger_records_pre_start_research_with_its_evidence_and_scores_it_with_pregame(root, tmp_path):
    out = L.add(mini(tmp_path, render(LATE)), KEY, root=root)
    assert out["timing"] == "PRE_START_RESEARCH"
    frame = L.read(root / L.LEDGER)
    assert set(frame["timing_claimed"]) == {"PRE_START_RESEARCH"}
    assert set(frame["timing_evidence"]) == {"DECLARED_RESEARCH_START:2026-10-22T09:40:00+00:00"
                                             "|NOT_STARTED:https://example.org/match-centre/1@2026-10-22T09:58:00+00:00"}
    strata = L.stratum(pd.DataFrame(dict(timing=["PREGAME", "PRE_START_RESEARCH", "POST_START_ISSUE", "TIMING_UNVERIFIED"],
                                         fast_card=["NO"] * 4, line_source=["SUPPLIED"] * 4, reference_status=["EXECUTED"] * 4)))
    assert strata[0] == strata[1] and len(set(strata)) == 3


def test_an_inconsistent_claim_falls_back_to_timing_unverified():
    timing, evidence = L.derive_timing(dict(LATE, outcome_exposure="LIVE_OBSERVED"), "card", KEY, "MINI.md")
    assert timing == "TIMING_UNVERIFIED" and evidence.startswith("CLAIMED_PRE_START_RESEARCH:")
