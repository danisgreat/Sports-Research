"""HPPV-v1 synthetic fixtures, plus the real all-card census and run regeneration."""

import copy
import json
import shutil
from pathlib import Path

import pytest

from ml import historical_pre_event as H
from ml import historical_pre_event_backtest as B


def capture(root, name, data):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = data.encode() if isinstance(data, str) else H.canonical(data).encode()
    path.write_bytes(raw)
    return dict(path=name, sha256=H.digest(raw), url="https://official.example/" + name)


def proof(root, name, **flags):
    return dict(
        capture=capture(root, name, "SYNTHETIC REVIEW " + name),
        reviewer="EXAMPLE independent reviewer",
        finding="EXAMPLE reviewed source",
        reviewed_at="2026-11-17T00:00:00Z",
        **flags,
    )


def fixture(root, **row_changes):
    row = dict(
        row_id="R00001",
        card="P-001",
        rank="1",
        contract="EXAMPLE Home -1.5 points",
        p="0.70",
        grade="WIN",
    )
    row.update(row_changes)
    identity = dict(
        event_id="EXAMPLE-GAME-1",
        market="HANDICAP",
        selection="HOME",
        line="-1.5",
        period="FULL_GAME",
        unit="POINTS",
        overtime="INCLUDED",
        probability_basis="CONDITIONAL_DECISIVE",
        origin="USER_SUPPLIED",
    )
    original_capture = capture(root, "original.txt", "EXAMPLE raw unchanged forecast")
    snapshot = dict(
        forecast={k: row[k] for k in H.SNAPSHOT_KEYS},
        identity=identity,
        method="EXAMPLE-METHOD-v1",
    )
    original = dict(
        capture=original_capture,
        transcription=capture(root, "transcription.txt", snapshot),
        integrity_review=proof(
            root,
            "integrity.txt",
            first_recoverable_unchanged=True,
            no_post_issue_information=True,
            information_cutoff="2026-01-01T09:00:00Z",
        ),
        publication=proof(
            root,
            "publication.txt",
            independent_timestamp=True,
            bound_original_sha256=original_capture["sha256"],
            issued_at="2026-01-01T10:00:00Z",
        ),
    )
    event = dict(
        event_id=identity["event_id"],
        actual_first_play="2026-01-01T11:00:00Z",
        teams=["EXAMPLE-H", "EXAMPLE-A"],
        competition="EXAMPLE-LEAGUE",
        proof=proof(root, "first-play.txt", actual_first_play_verified=True),
    )
    outcome = dict(
        identity=identity,
        grade=row["grade"],
        available_at="2026-01-01T14:00:00Z",
        grading_rule="EXAMPLE final home margin >1.5",
        proof=proof(root, "result.txt", independent_result=True),
    )
    recipe = dict(
        identity=identity,
        p="0.50",
        kind="RETROSPECTIVE_SPORTS_ONLY",
        information_cutoff="2026-01-01T09:00:00Z",
        feature_cutoff="2026-01-01T09:00:00Z",
        training_outcome_cutoff="2025-12-31T23:00:00Z",
        hyperparameter_cutoff="2025-12-01T00:00:00Z",
    )
    baseline = dict(
        recipe,
        recipe=capture(root, "recipe.txt", recipe),
        proof=proof(
            root,
            "baseline-review.txt",
            sports_only_market_blind=True,
            outcome_blind_reconstruction=True,
        ),
    )
    return row, dict(original=original, event=event, outcome=outcome, baseline=baseline)


def update_transcription(root, evidence, **changes):
    path = root / evidence["original"]["transcription"]["path"]
    snapshot = json.loads(path.read_text())
    snapshot.update(changes)
    evidence["original"]["transcription"] = capture(root, path.name, snapshot)


def test_tier_a_needs_original_timing_actual_first_play_and_independent_grade(tmp_path):
    row, evidence = fixture(tmp_path)
    d = H.assess(row, evidence, tmp_path, {})
    assert d["tier"] == "A" and d["accuracy"] and d["paired"]
    assert d["original_sha256"] == evidence["original"]["capture"]["sha256"]
    assert H.assess(row, {}, tmp_path, {})["tier"] == "C"
    e = copy.deepcopy(evidence)
    del e["original"]["publication"]
    del e["baseline"]
    assert H.assess(row, e, tmp_path, {})["tier"] == "B"
    del e["outcome"]
    del e["event"]
    assert H.assess(row, e, tmp_path, {})["tier"] == "B"


@pytest.mark.parametrize("issued", ["2026-01-01T11:00:00Z", "2026-01-01T11:00:01Z"])
def test_issue_at_or_after_first_play_is_d_even_if_scheduled_start_was_later(
    tmp_path, issued
):
    row, e = fixture(tmp_path)
    e["original"]["publication"]["issued_at"] = issued
    d = H.assess(row, e, tmp_path, {})
    assert d["tier"] == "D" and not d["paired"] and not d["accuracy"]


def test_evidence_exposure_overrides_pre_event_timestamp(tmp_path):
    row, e = fixture(tmp_path)
    e.update(known_outcome_exposed=True, exposure_proof=proof(tmp_path, "exposure.txt"))
    assert H.assess(row, e, tmp_path, {})["tier"] == "D"
    e["incomplete_reason"] = "EVENT_IDENTITY_UNRECOVERABLE"
    assert H.assess(row, e, tmp_path, {})["tier"] == "E"


@pytest.mark.parametrize(
    "key,value",
    [
        ("p", ".71"),
        ("rank", "2"),
        ("contract", "EXAMPLE Home +1.5 points"),
        ("card", "P-002"),
    ],
)
def test_original_probabilities_ranks_and_contracts_cannot_be_rewritten(
    tmp_path, key, value
):
    row, e = fixture(tmp_path)
    row[key] = value
    with pytest.raises(ValueError, match="altered"):
        H.assess(row, e, tmp_path, {})


@pytest.mark.parametrize(
    "key,value",
    [
        ("line", "+1.5"),
        ("unit", "GAMES"),
        ("period", "FIRST_HALF"),
        ("overtime", "EXCLUDED"),
        ("event_id", "OTHER-GAME"),
    ],
)
def test_baseline_cannot_change_sign_unit_period_overtime_or_event(
    tmp_path, key, value
):
    row, e = fixture(tmp_path)
    e["baseline"] = copy.deepcopy(e["baseline"])
    e["baseline"]["identity"][key] = value
    with pytest.raises(ValueError, match="endpoint"):
        H.assess(row, e, tmp_path, {})


def test_handicap_transcription_must_match_literal_original_sign(tmp_path):
    row, e = fixture(tmp_path)
    identity = dict(e["outcome"]["identity"], line="+1.5")
    update_transcription(tmp_path, e, identity=identity)
    with pytest.raises(ValueError, match="sign"):
        H.assess(row, e, tmp_path, {})


def test_frozen_benchmark_timestamp_must_bind_the_actual_recipe(tmp_path):
    row, e = fixture(tmp_path)
    baseline = e["baseline"]
    baseline["kind"] = "FROZEN_PRE_EVENT"
    recipe = {
        k: baseline[k]
        for k in (
            "identity",
            "p",
            "kind",
            "information_cutoff",
            "feature_cutoff",
            "training_outcome_cutoff",
            "hyperparameter_cutoff",
        )
    }
    baseline["recipe"] = capture(tmp_path, "recipe.txt", recipe)
    baseline["proof"].update(
        independent_timestamp=True, issued_at="2026-01-01T09:00:00Z"
    )
    with pytest.raises(ValueError, match="publication unverified"):
        H.assess(row, e, tmp_path, {})
    baseline["proof"]["bound_recipe_sha256"] = baseline["recipe"]["sha256"]
    assert H.assess(row, e, tmp_path, {})["paired"]


def test_probability_boundary_values_are_valid_and_log_loss_is_finite():
    assert H.probability("0") == 0 and H.probability("1") == 1
    for bad in ("nan", "inf", "-0.01", "1.01", ""):
        with pytest.raises(ValueError):
            H.probability(bad)
    assert H.log_loss(0, 1) > 30
    with pytest.raises(ValueError, match="timezone"):
        H.timestamp("2026-01-01T10:00:00")


@pytest.mark.parametrize(
    "key",
    [
        "information_cutoff",
        "feature_cutoff",
        "training_outcome_cutoff",
        "hyperparameter_cutoff",
    ],
)
def test_future_baseline_information_is_blocked(tmp_path, key):
    row, e = fixture(tmp_path)
    e["baseline"][key] = "2026-01-02T00:00:00Z"
    recipe = {
        k: e["baseline"][k]
        for k in (
            "identity",
            "p",
            "kind",
            "information_cutoff",
            "feature_cutoff",
            "training_outcome_cutoff",
            "hyperparameter_cutoff",
        )
    }
    e["baseline"]["recipe"] = capture(tmp_path, "recipe.txt", recipe)
    with pytest.raises(ValueError, match="leakage"):
        H.assess(row, e, tmp_path, {})


def test_hashes_or_document_dates_cannot_supply_publication_proof(tmp_path):
    row, e = fixture(tmp_path)
    e["original"]["publication"]["independent_timestamp"] = False
    with pytest.raises(ValueError, match="independently bound"):
        H.assess(row, e, tmp_path, {})
    e["original"]["publication"]["independent_timestamp"] = True
    (tmp_path / "original.txt").write_text("CHANGED")
    with pytest.raises(ValueError, match="hash mismatch"):
        H.assess(row, e, tmp_path, {})


def test_missing_outcome_source_blocks_scoring_and_unknown_origin_blocks_pairing(
    tmp_path,
):
    row, e = fixture(tmp_path)
    del e["outcome"]
    assert not H.assess(row, e, tmp_path, {})["accuracy"]
    row, e = fixture(tmp_path)
    e["outcome"]["proof"]["independent_result"] = False
    with pytest.raises(ValueError, match="independent outcome"):
        H.assess(row, e, tmp_path, {})
    row, e = fixture(tmp_path)
    identity = dict(e["outcome"]["identity"], origin="ANALYST_ALTERNATIVE")
    update_transcription(tmp_path, e, identity=identity)
    e["outcome"]["identity"] = identity
    e["baseline"]["identity"] = identity
    recipe = {
        k: e["baseline"][k]
        for k in (
            "identity",
            "p",
            "kind",
            "information_cutoff",
            "feature_cutoff",
            "training_outcome_cutoff",
            "hyperparameter_cutoff",
        )
    }
    e["baseline"]["recipe"] = capture(tmp_path, "recipe.txt", recipe)
    d = H.assess(row, e, tmp_path, {})
    assert d["accuracy"] and not d["paired"]


@pytest.mark.parametrize("grade", ["PUSH", "VOID", "UNATTAINABLE", "UNRESOLVED"])
def test_nondecisive_grades_never_become_binary_losses(tmp_path, grade):
    row, e = fixture(tmp_path, grade=grade)
    d = H.assess(row, e, tmp_path, {})
    assert d["tier"] == "A" and d["y"] == "" and not d["accuracy"] and not d["paired"]


def test_missing_probability_keeps_rank_accuracy_without_inventing_p(tmp_path):
    row, e = fixture(tmp_path, p="")
    d = H.assess(row, e, tmp_path, {})
    assert d["accuracy"] and not d["paired"] and d["p"] == ""


def test_settlement_revisions_preserve_original_and_corrected_grades(tmp_path):
    row, e = fixture(tmp_path)
    e["outcome"]["grade"] = "LOSS"
    e["outcome"]["settlement_revision"] = proof(
        tmp_path, "revision.txt", previous_grade="WIN", corrected_grade="LOSS"
    )
    d = H.assess(row, e, tmp_path, {})
    assert row["grade"] == "WIN" and d["verified_grade"] == "LOSS" and d["y"] == "0"


def scored_row(event="E1", **changes):
    row = dict(
        row_id="R1",
        card="P-001",
        rank="1",
        event_id=event,
        accuracy=True,
        paired=True,
        p="0.8",
        baseline_p="0.5",
        y="1",
        event_date="2026-01-01",
        competition="EXAMPLE",
        sport="Basketball",
        teams='["A","B"]',
    )
    row.update(changes)
    return row


def test_game_means_not_contract_rows_are_primary_uncertainty_units():
    rows = [scored_row() for _ in range(100)] + [
        scored_row("E2", p="0.8", y="0", teams='["C","D"]')
    ]
    score, blocks, bins = H.metrics(rows, "ALL", "ALL")
    assert score["events"] == 2 and score["paired_rows"] == 101
    assert score["paired_brier_advantage"] == pytest.approx(-0.09)
    assert score["event_mean_brier"] == pytest.approx(0.34)
    assert next(b for b in blocks if b["block"] == "competition")["interval_low"] == ""
    assert next(b for b in bins if b["rows"])["observed"] == 0.5


def test_connected_team_sensitivity_and_single_game_uncertainty():
    rows = [
        scored_row("E1"),
        scored_row("E2", teams='["B","C"]'),
        scored_row("E3", teams='["C","D"]'),
    ]
    _, blocks, _ = H.metrics(rows, "ALL", "ALL")
    assert next(b for b in blocks if b["block"] == "teams")["blocks"] == 1
    assert H.metrics(rows[:1], "ALL", "ALL")[0]["interval_low"] == ""


def test_duplicate_contracts_across_pids_choose_earliest_issuance(tmp_path):
    row, e = fixture(tmp_path)
    first = dict(row, **H.assess(row, e, tmp_path, {}), sport="Basketball")
    later = dict(
        first,
        row_id="R00002",
        card="P-002",
        issued_at="2026-01-01T10:05:00+00:00",
        p="0.75",
    )
    identity = json.loads(later["identity"])
    identity["line"] = "-1.50"
    later["identity"] = H.canonical(identity)
    H.deduplicate([later, first])
    assert first["paired"] and not later["paired"]
    assert later["reason"].endswith("DUPLICATE_EVENT_CONTRACT")


def test_conflicting_duplicate_outcomes_are_not_silently_discarded(tmp_path):
    row, e = fixture(tmp_path)
    first = dict(row, **H.assess(row, e, tmp_path, {}), sport="Basketball")
    later = dict(first, row_id="R00002", y="0")
    with pytest.raises(ValueError, match="conflicting duplicate"):
        H.deduplicate([first, later])


@pytest.mark.parametrize(
    "events,mean,low,high,accuracy,status",
    [
        (0, "", "", "", 0, "HISTORICAL_EVIDENCE_INSUFFICIENT"),
        (0, "", "", "", 10, "HISTORICAL_PRE_EVENT_ACCURACY_MEASURED"),
        (99, 0.1, 0.02, 0.18, 99, "HISTORICAL_SKILL_INCONCLUSIVE"),
        (100, 0.02, 0.001, 0.039, 100, "HISTORICAL_PRE_EVENT_SKILL_SUPPORTED"),
        (100, 0.005, -0.001, 0.011, 100, "HISTORICAL_SKILL_INCONCLUSIVE"),
        (100, -0.02, -0.03, -0.01, 100, "HISTORICAL_PERFORMANCE_NOT_SUPPORTED"),
    ],
)
def test_historical_verdict_gates(events, mean, low, high, accuracy, status):
    assert (
        H.verdict(
            dict(
                events=events,
                paired_brier_advantage=mean,
                interval_low=low,
                interval_high=high,
            ),
            accuracy,
        )
        == status
    )


def test_qualification_does_not_depend_on_winning(tmp_path):
    r1, e1 = fixture(tmp_path / "win", grade="WIN")
    r2, e2 = fixture(tmp_path / "loss", grade="LOSS")
    assert (
        H.assess(r1, e1, tmp_path / "win", {})["tier"]
        == H.assess(r2, e2, tmp_path / "loss", {})["tier"]
    )


def test_append_preserves_older_decisions_and_detects_tampering(tmp_path):
    row, evidence = fixture(tmp_path)
    train = tmp_path / H.TRAIN
    train.parent.mkdir(parents=True)
    train.write_bytes(H.csv_bytes([row], list(row)))
    ledger = tmp_path / "ledger.csv"
    ledger.write_bytes(H.csv_bytes([], H.LEDGER_FIELDS))
    H.append_evidence(
        tmp_path, ledger, row["row_id"], evidence, "Reviewer A", "original recovered"
    )
    H.append_evidence(
        tmp_path, ledger, row["row_id"], {}, "Reviewer B", "timing review withdrawn"
    )
    revisions = H.load_ledger(ledger)
    assert [r["revision"] for r in revisions] == ["1", "2"]
    assert (
        H.assess(row, json.loads(revisions[0]["payload"]), tmp_path, {})["tier"] == "A"
    )
    assert (
        H.assess(row, json.loads(revisions[1]["payload"]), tmp_path, {})["tier"] == "C"
    )
    changed = ledger.read_bytes().replace(b"Reviewer A", b"Reviewer X")
    ledger.write_bytes(changed)
    with pytest.raises(ValueError, match="hash changed"):
        H.load_ledger(ledger)


@pytest.fixture(scope="module")
def real_build():
    return H.build(ledger_raw=(H.ROOT / H.BASE / "EVIDENCE_SNAPSHOT.csv").read_bytes())


def test_real_census_has_all_685_cards_all_rows_and_zero_inferred_tier_a(real_build):
    outputs, inputs, status = real_build
    census = list(
        __import__("csv").DictReader(
            __import__("io").StringIO(outputs["HISTORICAL_CENSUS.csv"].decode())
        )
    )
    qual = list(
        __import__("csv").DictReader(
            __import__("io").StringIO(outputs["HISTORICAL_QUALIFICATION.csv"].decode())
        )
    )
    assert len(census) == 685 and len(qual) == 3150
    assert {r["card"] for r in census} == {f"P-{i:03d}" for i in range(1, 686)}
    assert {r["tier"] for r in qual} == {"C"}
    assert all(r["paired"] == "False" for r in qual)
    assert status == "HISTORICAL_EVIDENCE_INSUFFICIENT"
    assert H.TRAIN in inputs and "EVIDENCE_SNAPSHOT.csv" in outputs
    assert not any("research/one_chat" in p for p in inputs)


def test_run_regenerates_and_catches_report_or_output_omission(tmp_path):
    folder = tmp_path / "run"
    assert H.run(folder) == H.verify(folder)
    with pytest.raises(FileExistsError):
        H.run(folder)
    (folder / "CALIBRATION.csv").unlink()
    with pytest.raises(ValueError, match="manifest mismatch"):
        H.verify(folder)


def test_run_verifies_from_frozen_evidence_snapshot_after_live_ledger_changes(
    tmp_path, monkeypatch
):
    out = tmp_path / "run"
    H.run(out)
    actual_build = H.build

    def snapshot_only(root, *, ledger_raw=None):
        assert ledger_raw is not None
        return actual_build(root, ledger_raw=ledger_raw)

    monkeypatch.setattr(H, "build", snapshot_only)
    assert H.verify(out) == "HISTORICAL_EVIDENCE_INSUFFICIENT"


def test_committed_assessment_rebuilds_identically():
    # The current run binds the current code; the initial run in BASE verifies at its own implementation commit.
    assert H.verify(H.ROOT / H.CURRENT_RUN) == "HISTORICAL_EVIDENCE_INSUFFICIENT"


def test_the_initial_run_differs_from_the_current_run_only_in_its_code_hash():
    import csv
    def rows(folder):
        return {(r["role"], r["path"]): r["sha256"] for r in csv.DictReader(open(H.ROOT / folder / "MANIFEST.csv", encoding="utf-8"))}
    initial, current = rows(H.BASE), rows(H.CURRENT_RUN)
    assert set(initial) == set(current)
    assert {k for k in initial if initial[k] != current[k]} == {("INPUT", "ml/historical_pre_event.py")}


def test_frozen_source_reads_ignore_later_working_log_changes(tmp_path):
    # Git object lookup is independent of append-only current log growth.
    reference = (
        "git:" + H.FROZEN_COMMIT + ":prediction logs/PREDICTION_LOG_COMBINED_11.md"
    )
    before = H.input_digest(H.ROOT, reference)
    assert before != "MISSING"
    with pytest.raises(ValueError, match="unregistered"):
        H.input_bytes(tmp_path, reference.replace(H.FROZEN_COMMIT, "a" * 40))


def test_selective_omissions_or_duplicate_ids_fail_closed(tmp_path):
    (tmp_path / H.TRAIN).parent.mkdir(parents=True)
    shutil.copy(H.ROOT / H.TRAIN, tmp_path / H.TRAIN)
    receipt = Path(H.TRAIN).parent / "RECEIPT.csv"
    shutil.copy(H.ROOT / receipt, tmp_path / receipt)
    (tmp_path / H.AUDIT).parent.mkdir(parents=True)
    rows = H.read_csv(H.ROOT / H.AUDIT)
    rows[-1] = dict(rows[0])
    (tmp_path / H.AUDIT).write_bytes(H.csv_bytes(rows, list(rows[0])))
    with pytest.raises(ValueError, match="duplicate canonical"):
        H.build(tmp_path)


def examples(n=35):
    return [
        dict(
            row_id=f"EX-{i}",
            event_id=f"EVENT-{i}",
            issued_at=f"2026-01-{i // 2 + 1:02d}T{'08' if i % 2 == 0 else '18'}:00:00Z",
            features_available_at=f"2026-01-{i // 2 + 1:02d}T07:00:00Z",
            outcome_available_at=f"2026-01-{i // 2 + 1:02d}T23:00:00Z",
            values=[float(i % 3)],
            y=str(i % 2),
        )
        for i in range(n)
    ]


def test_strict_backtest_future_labels_cannot_change_earlier_predictions():
    data = examples()
    before = B.walk_forward(data)
    data[-1]["y"] = "1" if data[-1]["y"] == "0" else "0"
    after = B.walk_forward(data)
    assert [r["model_p"] for r in before[:-1]] == [r["model_p"] for r in after[:-1]]
    assert any(r["model_p"] != "" for r in before)
    for r in before:
        cutoff = H.timestamp(r["issued_at"])
        expected = [
            e
            for e in data
            if H.timestamp(e["outcome_available_at"]) < cutoff
            and H.timestamp(e["issued_at"]) < cutoff
            and e["event_id"] != r["event_id"]
            and H.timestamp(e["features_available_at"]) < cutoff
        ]
        assert r["train_events"] == len({e["event_id"] for e in expected})


def test_strict_backtest_rejects_future_features_and_holds_out_whole_game():
    data = examples()
    data[-1]["features_available_at"] = "2027-01-01T00:00:00Z"
    with pytest.raises(ValueError, match="features were unavailable"):
        B.walk_forward(data)
    data = examples()
    data[-1]["event_id"] = data[0]["event_id"]
    result = B.walk_forward(data)[-1]
    assert result["train_events"] == 33


def test_strict_study_runs_with_reviewed_real_time_contracts_and_hashes_outputs(
    tmp_path, monkeypatch
):
    def relocate(value, prefix):
        if isinstance(value, dict):
            if {"path", "sha256", "url"} <= value.keys():
                value["path"] = prefix + "/" + value["path"]
            else:
                for child in value.values():
                    relocate(child, prefix)
        elif isinstance(value, list):
            for child in value:
                relocate(child, prefix)

    rows, evidence = [], []
    for i in (1, 2):
        home = tmp_path / f"game{i}"
        row, e = fixture(home, row_id=f"R{i:05d}", card=f"P-{i:03d}")
        identity = dict(e["outcome"]["identity"], event_id=f"EVENT-{i}")
        update_transcription(home, e, identity=identity)
        e["event"]["event_id"] = f"EVENT-{i}"
        e["event"]["actual_first_play"] = f"2026-01-0{i}T11:00:00Z"
        e["original"]["publication"]["issued_at"] = f"2026-01-0{i}T10:00:00Z"
        e["outcome"].update(identity=identity, available_at=f"2026-01-0{i}T14:00:00Z")
        e["outcome"]["proof"]["availability_time_verified"] = True
        e.pop("baseline")
        relocate(e, f"game{i}")
        rows.append(dict(row, sport="Basketball"))
        evidence.append(e)
    train = tmp_path / H.TRAIN
    train.parent.mkdir(parents=True)
    train.write_bytes(H.csv_bytes(rows, list(rows[0])))
    ledger = tmp_path / H.BASE / "EVIDENCE_REVISIONS.csv"
    ledger.parent.mkdir(parents=True)
    ledger.write_bytes(H.csv_bytes([], H.LEDGER_FIELDS))
    for row, e in zip(rows, evidence):
        H.append_evidence(
            tmp_path, ledger, row["row_id"], e, "EXAMPLE reviewer", "SYNTHETIC evidence"
        )
    for name in ("historical_pre_event_backtest.py", "card_training.py"):
        (tmp_path / "ml").mkdir(exist_ok=True)
        shutil.copy(H.ROOT / "ml" / name, tmp_path / "ml" / name)

    def synthetic_census(root, **kwargs):
        inputs = {}
        decisions = [
            dict(row, **H.assess(row, e, root, inputs))
            for row, e in zip(rows, evidence)
        ]
        H.deduplicate(decisions)
        return (
            {"ORIGINAL_FORECASTS.csv": H.csv_bytes(decisions, list(decisions[0]))},
            inputs,
            "SYNTHETIC",
        )

    monkeypatch.setattr(H, "build", synthetic_census)
    monkeypatch.setattr(B, "MIN_TRAIN_EVENTS", 1)
    features = []
    for row in rows:
        ref = capture(
            tmp_path,
            row["row_id"] + "-features.txt",
            dict(
                row_id=row["row_id"],
                available_at="2026-01-01T09:00:00Z",
                values={"x": 1.0},
            ),
        )
        review = proof(
            tmp_path,
            row["row_id"] + "-features-review.txt",
            pre_event_data_verified=True,
        )
        features.append(
            dict(
                row_id=row["row_id"],
                capture=H.canonical(ref),
                proof=H.canonical(review),
            )
        )
    table = tmp_path / "features.csv"
    table.write_bytes(H.csv_bytes(features, ("row_id", "capture", "proof")))
    out = tmp_path / "study"
    assert B.run(table, out, tmp_path)["events"] == 1
    predictions = H.read_csv(out / "PREDICTIONS.csv")
    assert predictions[0]["model_p"] == "" and predictions[1]["model_p"] != ""
    for row in H.read_csv(out / "MANIFEST.csv"):
        if row["role"] == "OUTPUT":
            assert H.digest((out / row["path"]).read_bytes()) == row["sha256"]


def test_feature_subset_cannot_promote_a_later_census_duplicate(tmp_path, monkeypatch):
    train = tmp_path / H.TRAIN
    train.parent.mkdir(parents=True)
    train.write_bytes(
        H.csv_bytes([dict(row_id="R00001"), dict(row_id="R00002")], ("row_id",))
    )
    ledger = tmp_path / H.BASE / "EVIDENCE_REVISIONS.csv"
    ledger.parent.mkdir(parents=True)
    ledger.write_bytes(H.csv_bytes([], H.LEDGER_FIELDS))
    (tmp_path / "ml").mkdir()
    for name in ("historical_pre_event_backtest.py", "card_training.py"):
        shutil.copy(H.ROOT / "ml" / name, tmp_path / "ml" / name)
    # Full-census admission has already selected R00001. Only R00002 has features.
    decisions = [
        dict(row_id="R00001", accuracy=True, reason="VERIFIED"),
        dict(row_id="R00002", accuracy=False, reason="DUPLICATE_EVENT_CONTRACT"),
    ]
    output = H.csv_bytes(decisions, list(decisions[0]))
    monkeypatch.setattr(
        H,
        "build",
        lambda root, **kwargs: ({"ORIGINAL_FORECASTS.csv": output}, {}, "SYNTHETIC"),
    )
    features = tmp_path / "later-only-features.csv"
    features.write_bytes(H.csv_bytes([dict(row_id="R00002")], ("row_id",)))
    with pytest.raises(ValueError, match="DUPLICATE_EVENT_CONTRACT"):
        B.run(features, tmp_path / "study", tmp_path)
