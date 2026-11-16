"""Adversarial custody, request coverage and nonstationary inference regressions."""

from pathlib import Path

import pytest

from ml import forecast_integrity as F
from ml import one_chat as O
from ml.tests import test_one_chat as M

repo = M.repo


def test_recommitted_and_rehashed_parsed_numbers_do_not_replace_published_forecast(
    repo, tmp_path
):
    intake = M.build(repo, tmp_path, [M.card()])
    outcomes = M.outcomes(repo, tmp_path / "cap", ["CHAT1-G0001"])
    M.commit_all(repo)
    rows = O.read_csv(intake / "PICKS.csv")
    for r in rows:
        r["p"] = (
            "0.99"
            if (r["label"], r["side"]) in (("L1", "AWAY"), ("L2", "OVER"))
            else "0.01"
        )
    (intake / "PICKS.csv").write_bytes(O.csv_bytes(O.ROW_FIELDS, rows))
    manifest = O.read_csv(intake / "MANIFEST.csv")
    for r in manifest:
        r["sha256"] = O.sha((intake / r["file"]).read_bytes())
    (intake / "MANIFEST.csv").write_bytes(O.csv_bytes(("file", "sha256"), manifest))
    M.commit_all(repo, "recomputed derivative hashes")
    result = M.run(repo, tmp_path, [intake], [outcomes], "edited")
    assert result["advantage"] == "NOT_ASSESSABLE"
    assert any(
        "exact published block" in r["problem"]
        for r in O.read_csv(repo / O.SCORES / "edited/CUSTODY_PROBLEMS.csv")
    )


def test_omitting_a_sealed_intake_is_not_assessable(repo, tmp_path):
    early = M.build(repo, tmp_path, [M.card(key="EARLY", home="Earlier")], name="early")
    later = M.build(
        repo,
        tmp_path,
        [M.card(key="LATER", home="Later", start="2026-11-20T09:00:00Z")],
        name="later",
    )
    outcomes = M.outcomes(
        repo, tmp_path / "cap", ["LATER"], start="2026-11-20T09:00:00Z"
    )
    M.commit_all(repo)
    all_inputs = M.run(repo, tmp_path, [early, later], [outcomes], "complete")
    omitted = M.run(repo, tmp_path, [later], [outcomes], "omitted")
    assert all_inputs["games_in_sequence"] == 0
    assert omitted["advantage"] == "NOT_ASSESSABLE" and omitted["custody_problems"] > 0


def test_local_push_receipt_forgery_is_not_server_evidence(repo, tmp_path):
    folder = M.build(repo, tmp_path, [M.card()], at="2026-11-20T10:00:00Z")
    outcomes = M.outcomes(repo, tmp_path / "cap", ["CHAT1-G0001"])
    public = list(M.LIVE_PUSHES[str(repo)])
    fake = [
        dict(
            r,
            pushed_at_server="2026-11-20T07:00:00Z",
            source="github-activity-api",
            retrieved_at="x",
        )
        for r in public
    ]
    path = repo / O.RECEIPTS
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(O.csv_bytes(O.RECEIPT_FIELDS, fake))
    M.commit_all(repo)
    result = M.run(repo, tmp_path, [folder], [outcomes], "forged")
    assert result["games_in_sequence"] == 0
    assert (
        O.read_csv(repo / O.SCORES / "forged/COVERAGE.csv")[0]["exclusion"]
        == "SEALED_AFTER_START"
    )


def test_published_request_and_seal_blobs_cannot_be_replaced(repo, tmp_path):
    folder = M.build(repo, tmp_path, [M.card()])
    ledger = O.Repo(repo).seals
    path = ledger[0]["sealed_path"]
    with pytest.raises(O.OneChatError, match="immutable"):
        O.publish_seal_tree(repo, {path: b"different numbers"})
    assert folder.exists()


def test_original_request_omission_addition_and_definition_are_checked(repo, tmp_path):
    drop = M.drop(tmp_path, [M.card()])
    files = list(drop.glob("*.md"))
    M.prepare_requests(repo, files)
    request = O.request_staging(repo) / F.request_path("CHAT1-G0001")
    payload = {name: (request / name).read_bytes() for name in F.REQUEST_FILES}
    meta, picks, facts = O.parse(O.BLOCK.search(M.card())["body"])
    assert F.request_problems(payload, meta, picks) == []
    assert any(
        "omits, adds or changes" in p
        for p in F.request_problems(payload, meta, picks[:-1])
    )
    payload["REQUEST.txt"] = b"not the original requested contracts"
    assert any("excerpt" in p for p in F.request_problems(payload, meta, picks))


def test_request_registration_is_idempotent_and_refuses_edits(repo, tmp_path):
    drop = M.drop(tmp_path, [M.card()])
    M.prepare_requests(repo, list(drop.glob("*.md")))
    folder = O.request_staging(repo) / F.request_path("CHAT1-G0001")
    source = tmp_path / "changed-request.txt"
    source.write_text(
        (folder / "REQUEST.txt").read_text() + "\nadditional original instruction",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="immutable"):
        F.register_request(
            source,
            folder / "EVENT.csv",
            folder / "CONTRACTS.csv",
            "CHAT1-G0001",
            O.request_staging(repo),
        )


def test_first_play_capture_is_required_and_rehashed(repo, tmp_path):
    folder = M.build(repo, tmp_path, [M.card()])
    outcomes = M.outcomes(repo, tmp_path / "cap", ["CHAT1-G0001"])
    rows = O.read_csv(outcomes)
    for r in rows:
        r["first_play_capture_sha256"] = "0" * 64
    outcomes.write_bytes(O.csv_bytes(O.OUTCOME_FIELDS, rows))
    M.commit_all(repo)
    with pytest.raises(O.OneChatError, match="first-play capture"):
        M.run(repo, tmp_path, [folder], [outcomes], "bad-clock")


def test_seal_uses_data_branch_without_changing_main_or_publishing_unrelated_work(
    repo, tmp_path
):
    initial = M.git(repo, "rev-parse", "HEAD")
    secret = repo / "unrelated.txt"
    secret.write_text("owner work", encoding="utf-8")
    M.git(repo, "add", "unrelated.txt")
    d = M.drop(tmp_path, [M.card()])
    result = M.seal(repo, list(d.glob("*.md")))
    assert result["branch"] == O.SEAL_BRANCH
    assert M.git(repo, "rev-parse", "HEAD") == initial
    assert M.git(repo, "rev-parse", "refs/remotes/origin/main") == initial
    assert M.git(repo, "diff", "--cached", "--name-only") == "unrelated.txt"
    assert "unrelated.txt" not in M.git(
        repo, "ls-tree", "-r", "--name-only", f"refs/remotes/origin/{O.SEAL_BRANCH}"
    )


def test_current_average_bound_does_not_reuse_an_earlier_positive_crossing():
    result = O.advantage([0.2] * 50 + [-0.7] * 350)
    assert result["lower_bound_95"] < 0
    assert result["lower_bound_95"] <= result["mean_d"]
    assert result["assessed_prefix_lower_bound"] > 0
    assert result["assessed_prefix_mean"] > 0


def test_confidence_path_is_prefix_predictable_and_rejects_invalid_observations():
    ds = [0.1, -0.1, 0.05, 0.2]
    assert F.confidence_path(ds)[:3] == F.confidence_path(ds[:3])
    with pytest.raises(ValueError):
        F.confidence_path([float("nan")])
    with pytest.raises(ValueError):
        F.confidence_path([0.3])


def test_actual_historical_census_accounts_for_all_685_cards():
    from ml.evidence_status import historical_summary

    summary, audit, exclusions = historical_summary(
        O.ROOT / "research/card_training/2026-11-16-1"
    )
    assert summary["historical_cards"] == 685 and len(audit) == 685
    assert summary["probability_rows"] == 1291
    assert summary["admitted_contract_rows"] == 3082
    assert sum(r["rows"] for r in exclusions) == 68
    assert all(
        r["prospective_admission"] == "NOT_INFERRED_FROM_LATER_RULE_CHECKS"
        for r in audit
    )


def test_registered_request_can_be_accounted_for_without_inventing_a_forecast(
    repo, tmp_path
):
    d = M.drop(tmp_path, [M.card()])
    M.prepare_requests(repo, list(d.glob("*.md")))
    O.publish_request("CHAT1-G0001", repo)
    with pytest.raises(O.OneChatError, match="reason"):
        O.request_disposition("CHAT1-G0001", "NO_FORECAST", "", repo)
    O.request_disposition(
        "CHAT1-G0001", "NO_FORECAST", "Research could not be completed", repo
    )
    assert O.Repo(repo).dispositions[0]["status"] == "NO_FORECAST"


def test_numeric_line_cannot_disagree_with_original_request_excerpt(repo, tmp_path):
    d = M.drop(tmp_path, [M.card()])
    M.prepare_requests(repo, list(d.glob("*.md")))
    folder = O.request_staging(repo) / F.request_path("CHAT1-G0001")
    payload = {name: (folder / name).read_bytes() for name in F.REQUEST_FILES}
    contracts = F.rows(payload["CONTRACTS.csv"])
    contracts[0]["line"] = "-9.5"
    payload["CONTRACTS.csv"] = F.csv_bytes(F.CONTRACT_FIELDS, contracts)
    assert any("numeric line" in p for p in F.request_problems(payload))


def test_typed_feature_builder_keeps_missingness_and_flags_invalid_boolean(
    repo, tmp_path
):
    from ml.evidence_status import typed_features

    folder = M.build(repo, tmp_path, [M.card()])
    # The fixture's literal 10 for a 0/1 feature is deliberately invalid.
    features, issues, coverage = typed_features([folder], repo)
    assert len(coverage) == 1
    assert any(r["reason"] == "VALUE_OUTSIDE_DEFINITION" for r in issues)
    assert any(r["admission"] == "EXCLUDED" for r in features)


def test_protected_main_merge_publications_are_valid_independent_server_events(
    monkeypatch, tmp_path
):
    import json
    from types import SimpleNamespace

    events = [
        dict(
            before="a",
            after="b",
            timestamp="2026-11-17T01:00:00Z",
            ref="refs/heads/main",
            activity_type="pr_merge",
        ),
        dict(
            before="b",
            after="c",
            timestamp="2026-11-17T02:00:00Z",
            ref="refs/heads/forecast-seals",
            activity_type="push",
        ),
        dict(
            before="c",
            after="d",
            timestamp="2026-11-17T03:00:00Z",
            ref="refs/heads/main",
            activity_type="branch_creation",
        ),
    ]
    monkeypatch.setattr(O, "_remote_slug", lambda root: "example/repo")
    monkeypatch.setattr(
        O.subprocess,
        "run",
        lambda *a, **kw: SimpleNamespace(returncode=0, stdout=json.dumps([events])),
    )
    result = O.github_push_activity(tmp_path)
    assert [r["after"] for r in result] == ["b", "c"]
