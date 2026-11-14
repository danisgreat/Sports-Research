"""Cross-path regressions for the two reproduced TIMING-v3 gaps; EXAMPLE data only."""
import pandas as pd
import pytest

from ml import primary as P, ledger as L, timing_corrections as T
from ml.tests.test_primary import inputs, run  # noqa: F401
from ml.tests.test_picks_ledger import KEY, render, mini, root  # noqa: F401
from ml.tests.test_timing_v3 import LATE


@pytest.mark.parametrize("change,needle", [
    ({}, "not_started_observed_at"),
    ({"not_started_observed_at": "2023-01-01T10:30:00Z"}, "not_started_source"),
    ({"not_started_observed_at": "2023-01-01T11:01:00Z", "not_started_source": "https://example.org/match/1"}, "actual first play"),
    ({"not_started_observed_at": "2023-01-01T09:30:00Z", "not_started_source": "https://example.org/match/1"}, "at or after"),
])
def test_primary_cannot_assign_pre_start_research_without_consistent_observation(inputs, change, needle):
    inputs[0].update(issue_at="2023-01-01T12:00:00Z", research_started_at="2023-01-01T10:00:00Z", **change)
    with pytest.raises(P.AdmissionError, match=needle):
        run(inputs)


def test_primary_accepts_the_same_consistent_declarations_as_the_card_checker(inputs):
    inputs[0].update(issue_at="2023-01-01T12:00:00Z", research_started_at="2023-01-01T10:00:00Z",
                     not_started_observed_at="2023-01-01T10:30:00Z", not_started_source="https://example.org/match/1")
    rec = run(inputs)
    assert rec["actual_issue_phase"] == "PRE_START_RESEARCH"
    P.verify_bundle(inputs[4] / "bundle")


@pytest.fixture
def settled(root, tmp_path):
    L.add(mini(tmp_path, render(LATE)), KEY, root=root)
    original = (root / L.LEDGER).read_bytes()
    ledger = L.read(root / L.LEDGER)
    results = root / "results.csv"
    pd.DataFrame([dict(local_key=KEY, label=x, grade="WIN", timing="POST_START_ISSUE") for x in ledger.label]).to_csv(results, index=False)
    evidence = root / "official-first-play.csv"
    evidence.write_bytes(T.csv_bytes(T.PROOF_FIELDS, [dict(local_key=KEY, actual_start="2026-10-22T10:00:00+00:00",
                         source_url="https://example.org/official/event-1", observed_at="2026-10-22T11:00:00+00:00", note="EXAMPLE official event sheet review")]))
    return root, results, evidence, original


def correction(settled, actual="2026-10-22T10:00:00+00:00", **kwargs):
    root, _, evidence, _ = settled
    if actual != "2026-10-22T10:00:00+00:00":
        evidence = root / ("official-first-play-" + actual.replace(":", "_") + ".csv")
        evidence.write_bytes(T.csv_bytes(T.PROOF_FIELDS, [dict(local_key=KEY, actual_start=actual,
                             source_url="https://example.org/official/event-1", observed_at="2026-10-22T11:00:00+00:00", note="EXAMPLE corrected official event sheet review")]))
    return T.correct(root / L.LEDGER, KEY, actual, "https://example.org/official/event-1", evidence.name,
                     "EXAMPLE reviewed official first-play record", root=root, at="2026-10-22T12:00:00+00:00", **kwargs)


def test_unreviewed_claim_is_quarantined_and_unbound_results_column_cannot_override_it(settled):
    root, results, _, original = settled
    report = L.score(root / L.LEDGER, results, root=root)
    assert {r["timing"] for r in report["effective_timing"]} == {"TIMING_UNVERIFIED"}
    assert all("timing=TIMING_UNVERIFIED" in r["stratum"] for r in report["scores"])
    assert (root / L.LEDGER).read_bytes() == original


def test_official_review_reaches_scores_and_contradiction_moves_every_contract_without_rewriting_original(settled):
    root, results, _, original = settled
    first = correction(settled)
    assert first["effective_timing"] == "PRE_START_RESEARCH"
    good = L.score(root / L.LEDGER, results, root=root)
    assert all("timing=PREGAME" in r["stratum"] for r in good["scores"])
    prefix = (root / T.PATH).read_bytes()
    assert correction(settled)["status"] == "ALREADY_EXISTS"
    assert (root / T.PATH).read_bytes() == prefix
    later = correction(settled, "2026-10-22T09:30:00+00:00")
    assert later["effective_timing"] == "POST_START_ISSUE"
    bad = L.score(root / L.LEDGER, results, root=root)
    assert {r["timing"] for r in bad["effective_timing"]} == {"POST_START_ISSUE"}
    assert all("timing=POST_START_ISSUE" in r["stratum"] for r in bad["scores"])
    assert (root / L.LEDGER).read_bytes() == original
    assert (root / T.PATH).read_bytes().startswith(prefix)


def test_changed_official_evidence_or_broken_revision_chain_refuses_scoring(settled):
    root, results, evidence, _ = settled
    correction(settled)
    original = evidence.read_bytes()
    evidence.write_text("Edited evidence after correction")
    with pytest.raises(ValueError, match="evidence hash"):
        L.score(root / L.LEDGER, results, root=root)
    evidence.write_bytes(original)
    path = root / T.PATH
    path.write_bytes(path.read_bytes().replace(b"PRE_START_RESEARCH", b"POST_START_ISSUE", 1))
    with pytest.raises(ValueError, match="chain mismatch"):
        L.score(root / L.LEDGER, results, root=root)


def test_timing_review_cannot_target_unknown_card_or_use_missing_evidence(settled):
    root, _, evidence, _ = settled
    with pytest.raises(ValueError, match="original PRE_START_RESEARCH"):
        T.correct(root / L.LEDGER, "LOCAL-EXAMPLE-G9999", "2026-10-22T10:00:00Z", "https://example.org/1", evidence.name,
                  "EXAMPLE", root=root)
    evidence.unlink()
    with pytest.raises(ValueError, match="evidence"):
        correction(settled)
