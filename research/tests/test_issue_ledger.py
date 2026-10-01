"""Issuer transaction and source-backed revision tests use temporary copies."""
from copy import deepcopy
from datetime import timedelta
import json

import pytest

from research.src import eligibility, issue, ledger, pilot
from research.tests.test_eligibility import EvidenceFactory


@pytest.fixture
def evidence(tmp_path,monkeypatch):
    return EvidenceFactory(tmp_path,monkeypatch)


def prepare(evidence,bundle):
    evidence.clock=eligibility.aware_time(bundle["issued_utc"])
    return issue.prepare_issue(bundle,evidence.registry_path,sources_registry_path=evidence.sources_path,
        evidence_root=evidence.root,ledger_path=evidence.ledger_path,part6_path=evidence.part6,reconciliation_path=evidence.reconciliation)


def test_synthetic_fixture_ignores_later_production_cards(tmp_path,monkeypatch):
    production = tmp_path/"production.md"
    raw = issue.PART6.read_bytes()+b"\r\n## P-900 Synthetic future production card\r\n"
    production.write_bytes(raw)
    monkeypatch.setattr(issue,"PART6",production)
    evidence=EvidenceFactory(tmp_path/"fixture",monkeypatch)
    assert issue.next_card_id(evidence.part6,evidence.reconciliation,evidence.ledger_path)=="P-523"
    assert production.read_bytes()==raw


def test_preparation_is_read_only_and_real_issue_disabled_by_default(evidence):
    bundle=evidence.bundle();evidence.register([bundle])
    before=(evidence.part6.read_bytes(),evidence.ledger_path.read_bytes())
    draft=prepare(evidence,bundle)
    assert draft["status"]=="PREPARED_DRAFT_NOT_ISSUED" and draft["proposed_card_id"]=="P-523"
    assert "NOT_ISSUED" in draft["markdown_draft"]
    with pytest.raises(ValueError,match="disabled"):
        issue.commit_issue(draft)
    assert before==(evidence.part6.read_bytes(),evidence.ledger_path.read_bytes())


def test_commit_preserves_original_bytes_deduplicates_and_advances_counter(evidence):
    bundle=evidence.bundle();evidence.register([bundle]);original=evidence.part6.read_bytes()
    result,frozen=evidence.issue(bundle)
    assert result["card_id"]=="P-523" and evidence.part6.read_bytes().startswith(original)
    assert issue.next_card_id(evidence.part6,evidence.reconciliation,evidence.ledger_path)=="P-524"
    with pytest.raises(ValueError,match="already"):
        prepare(evidence,frozen)
    with pytest.raises(ValueError,match="checked issuer"):
        ledger.append_record(evidence.ledger_path,"ISSUE_COMMITTED",{})
    records=ledger.read_records(evidence.ledger_path)
    assert [r["record_type"] for r in records]==["EVENT_REGISTERED","ISSUE_PREPARED","ISSUE_COMMITTED"]


def test_changed_authority_or_transaction_rejects_commit(evidence):
    bundle=evidence.bundle();evidence.register([bundle]);draft=prepare(evidence,bundle)
    changed=deepcopy(draft);changed["proposed_card_id"]="P-999"
    with pytest.raises(ValueError,match="transaction changed"):
        issue.commit_issue(changed,allow_real_issue=True)
    with evidence.part6.open("ab") as handle:handle.write(b"\r\nAudited unrelated continuation\r\n")
    with pytest.raises(ValueError,match="changed since preparation"):
        issue.commit_issue(draft,allow_real_issue=True)
    assert len(ledger.read_records(evidence.ledger_path))==1


def test_interrupted_append_is_recovered_once_and_blocks_new_ids(evidence,monkeypatch):
    bundle=evidence.bundle();evidence.register([bundle]);draft=prepare(evidence,bundle)
    original=issue._append_locked
    def interrupted(path,kind,payload,**kwargs):
        if kind=="ISSUE_COMMITTED":raise RuntimeError("simulated power loss after projection")
        return original(path,kind,payload,**kwargs)
    monkeypatch.setattr(issue,"_append_locked",interrupted)
    with pytest.raises(RuntimeError,match="power loss"):
        issue.commit_issue(draft,allow_real_issue=True)
    core=evidence.part6.read_bytes()
    with pytest.raises(ValueError,match="pending"):
        issue.next_card_id(evidence.part6,evidence.reconciliation,evidence.ledger_path)
    monkeypatch.setattr(issue,"_append_locked",original)
    repaired=issue.recover_issue(evidence.ledger_path,draft["transaction_id"],allow_real_issue=True)
    assert repaired["status"]=="RECOVERED" and evidence.part6.read_bytes()==core
    assert issue.recover_issue(evidence.ledger_path,draft["transaction_id"],allow_real_issue=True)["status"]=="ALREADY_COMMITTED"
    assert len(ledger.committed_issues(ledger.read_records(evidence.ledger_path)))==1


def test_settlement_revisions_preserve_forecasts_and_prior_receipts(evidence):
    bundle=evidence.bundle();evidence.register([bundle]);_,frozen=evidence.issue(bundle)
    first=evidence.terminal(frozen)
    initial=ledger.append_settlement_revision(evidence.ledger_path,first,evidence.registry_path,reason="Synthetic first final",evidence_root=evidence.root)
    prefix=evidence.ledger_path.read_bytes()
    later=evidence.terminal(frozen,score=(3,1))
    revision=ledger.append_settlement_revision(evidence.ledger_path,later,evidence.registry_path,reason="Synthetic source correction",evidence_root=evidence.root)
    assert evidence.ledger_path.read_bytes().startswith(prefix)
    assert revision["payload"]["previous_revision_sha256"]==initial["record_sha256"]
    assert revision["payload"]["forecast_core_sha256"]==initial["payload"]["forecast_core_sha256"]
    assert initial["payload"]["verified"]["score_home"]==2 and revision["payload"]["verified"]["score_home"]==3
    with pytest.raises(ValueError,match="duplicate settlement"):
        ledger.append_settlement_revision(evidence.ledger_path,later,evidence.registry_path,reason="duplicate",evidence_root=evidence.root)
    scored=pilot.score_events(evidence.ledger_path,evidence.registry_path,evidence_root=evidence.root)
    assert len(scored)==1,scored.attrs["exclusions"]
    assert scored.attrs["scored_events"]==1


def test_conflicting_terminal_and_forecast_rewrites_fail_closed(evidence):
    bundle=evidence.bundle();evidence.register([bundle]);_,frozen=evidence.issue(bundle)
    settled=evidence.terminal(frozen)
    receipt=settled["terminal_receipts"][1];p=evidence.root/receipt["body_path"]
    obj=json.loads(p.read_text());obj["event"]["score_home"]=4;evidence.write(p,obj);evidence.rehash_receipt(receipt)
    with pytest.raises(ValueError,match="scores disagree"):
        ledger.append_settlement_revision(evidence.ledger_path,settled,evidence.registry_path,reason="bad",evidence_root=evidence.root)
    settled=evidence.terminal(frozen);settled["adjustment_reason"]="retroactive text"
    with pytest.raises(ValueError,match="rewrite"):
        ledger.append_settlement_revision(evidence.ledger_path,settled,evidence.registry_path,reason="bad",evidence_root=evidence.root)


def test_abstentions_and_unsettled_events_are_visible_and_corruption_blocks(evidence):
    first=evidence.bundle("forecast");second=evidence.bundle("abstain",when=evidence.clock+timedelta(hours=1))
    evidence.register([first,second]);evidence.issue(first)
    ledger.record_abstention(evidence.ledger_path,{k:second[k] for k in ("lane","league","season","event_id")},"missing lineup",
        evidence_refs=[],evidence_root=evidence.root)
    scores=pilot.score_events(evidence.ledger_path,evidence.registry_path,evidence_root=evidence.root)
    assert scores.empty and list(scores.columns)==pilot.EVENT_COLUMNS
    assert {e["reason"] for e in scores.attrs["exclusions"]}=={"UNSETTLED","ABSTENTION"}
    raw=evidence.ledger_path.read_bytes();evidence.ledger_path.write_bytes(raw.replace(b'"HOME"',b'"EVIL"',1))
    with pytest.raises(ValueError,match="chain"):
        ledger.read_records(evidence.ledger_path)
