"""Chronological enrollment, persistent interim and immutable custody tests."""
from datetime import timedelta
import json

import pytest

from research.src import eligibility, ledger, pilot
from research.tests.test_eligibility import EvidenceFactory


@pytest.fixture
def evidence(tmp_path,monkeypatch):
    return EvidenceFactory(tmp_path,monkeypatch)


def locked_cohort(evidence,adjustments):
    first=evidence.clock+timedelta(hours=2)
    bundles=[evidence.bundle(f"z-{99-i}",when=first+timedelta(days=7*i),adjustment=adjustment)
             for i,adjustment in enumerate(adjustments)]
    universe=evidence.register(bundles)
    basis=evidence.ref("precision-basis.json",{"test_only":True,"observed_block_differences":[-.1,.1,-.05,.05]})
    power=evidence.ref("power-plan.json",dict(target_adjusted_events=8,futility_look_events=4,mwi_brier=.01,
        minimum_week_blocks=4,method="Synthetic tests only: four interim and eight final week blocks",basis_refs=[basis]))
    definition=dict(cohort_version="SYNTHETIC_TEST_ONLY",weights={"EPL":1.0},target_adjusted_events=8,
        model_versions={"EPL":"fixture-1"},baseline_versions={"EPL":evidence.baseline_version},
        endpoints={"EPL":"REGULATION"},league_seasons={"EPL":{"league":"EPL","season":"TEST2030"}},
        futility_look_events=4,mwi_brier=.01,minimum_week_blocks=4,seed=1,bootstrap_reps=10000,
        cohort_issue_from_utc=(first-timedelta(minutes=1)).isoformat(),cohort_issue_to_utc=(first+timedelta(days=100)).isoformat(),
        inclusion_rule="FIRST_CHRONOLOGICAL_ADJUSTED_ISSUES",power_plan_ref=power,universe_refs=[universe])
    lock_path=evidence.root/"pilot-lock.json"
    pilot.freeze_lock(lock_path,definition,ledger_path=evidence.ledger_path,registry_path=evidence.registry_path,
        sources_registry_path=evidence.sources_path,evidence_root=evidence.root)
    return bundles,lock_path,definition


def issue_and_settle(evidence,bundle):
    _,frozen=evidence.issue(bundle)
    terminal=evidence.terminal(frozen)
    ledger.append_settlement_revision(evidence.ledger_path,terminal,evidence.registry_path,reason="Synthetic final",evidence_root=evidence.root)
    return frozen


def test_bare_flags_retrospective_lock_and_nonfinite_probabilities_fail_closed(tmp_path):
    csv=tmp_path/"fake.csv";csv.write_text("performance_eligible\ntrue\n")
    with pytest.raises(ValueError,match="eligibility flags"):
        pilot.score_events(csv)
    lock=tmp_path/"old-lock.json";lock.write_text(json.dumps({"status":"FROZEN","weights":{"EPL":1},"target_adjusted_events":10}))
    with pytest.raises(ValueError,match="versioned immutable"):
        pilot.decision(csv,lock)


def test_futility_stop_is_terminal_even_after_more_good_outcomes(evidence):
    bundles,lock,_=locked_cohort(evidence,["BAD"]*4+["GOOD"]*4)
    for b in bundles[:4]:issue_and_settle(evidence,b)
    stopped=pilot.decision(evidence.ledger_path,lock)
    assert stopped["verdict"]=="FUTILITY_STOP"
    for b in bundles[4:]:issue_and_settle(evidence,b)
    again=pilot.decision(evidence.ledger_path,lock)
    assert again["verdict"]=="FUTILITY_STOP" and again["terminal"]
    records=ledger.read_records(evidence.root/"pilot-lock.custody.jsonl")
    assert [r["record_type"] for r in records]==["PILOT_LOCK","PILOT_INTERIM"]


def test_batch_skipping_exact_interim_still_evaluates_first_prefix(evidence):
    bundles,lock,_=locked_cohort(evidence,["BAD"]*4+["GOOD"]*4)
    for b in bundles:issue_and_settle(evidence,b)
    result=pilot.decision(evidence.ledger_path,lock)
    assert result["verdict"]=="FUTILITY_STOP" and result["interim"]["adjusted_brier"]["events"]==4
    assert [m["identity"][-1] for m in result["interim"]["membership"]]==[b["event_id"] for b in bundles[:4]]


def test_membership_is_issue_chronology_not_event_id_and_is_frozen(evidence):
    bundles,lock,_=locked_cohort(evidence,["GOOD"]*10)
    for b in bundles[:8]:issue_and_settle(evidence,b)
    result=pilot.decision(evidence.ledger_path,lock)
    assert result["verdict"]=="KEEP_ADJUSTMENTS",result
    original=result["membership_sha256"]
    assert [m["identity"][-1] for m in result["cohort_membership"]]==[b["event_id"] for b in bundles[:8]]
    for b in bundles[8:]:issue_and_settle(evidence,b)
    later=pilot.decision(evidence.ledger_path,lock)
    assert later["membership_sha256"]==original and later["verdict"]=="KEEP_ADJUSTMENTS"
    assert [r["record_type"] for r in ledger.read_records(evidence.root/"pilot-lock.custody.jsonl")]==["PILOT_LOCK","PILOT_INTERIM","PILOT_FINAL"]


def test_missing_early_settlement_cannot_be_dropped_for_later_results(evidence):
    bundles,lock,_=locked_cohort(evidence,["GOOD"]*5)
    evidence.issue(bundles[0])
    for b in bundles[1:]:issue_and_settle(evidence,b)
    result=pilot.decision(evidence.ledger_path,lock)
    assert result["verdict"]=="WAIT_FOR_INTERIM_SETTLEMENT"
    assert result["missing_members"][0][-1]==bundles[0]["event_id"]
    assert not any(r["record_type"]=="PILOT_INTERIM" for r in ledger.read_records(evidence.root/"pilot-lock.custody.jsonl"))


def test_lock_overwrite_edit_and_registry_drift_are_detected(evidence):
    _,lock,definition=locked_cohort(evidence,["GOOD"]*8)
    with pytest.raises(FileExistsError,match="do not overwrite"):
        pilot.freeze_lock(lock,definition,ledger_path=evidence.ledger_path,registry_path=evidence.registry_path,
            sources_registry_path=evidence.sources_path,evidence_root=evidence.root)
    original=lock.read_bytes();edited=json.loads(original);edited["seed"]=999;evidence.write(lock,edited)
    with pytest.raises(ValueError,match="custody"):
        pilot.decision(evidence.ledger_path,lock)
    lock.write_bytes(original);evidence.registry["admissions"][0]["reason"]="changed";evidence.refresh()
    with pytest.raises(ValueError,match="registry changed"):
        pilot.decision(evidence.ledger_path,lock)


def test_actual_default_registries_cannot_start_a_live_pilot(evidence):
    bundles,_,definition=locked_cohort(evidence,["GOOD"]*8)
    with pytest.raises(ValueError,match="no live-qualified"):
        pilot.freeze_lock(evidence.root/"real-default-refused.json",definition,ledger_path=evidence.ledger_path,
            registry_path=eligibility.REGISTRY,evidence_root=evidence.root)
