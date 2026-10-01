"""Synthetic local source bodies exercise admission without issuing real cards."""
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path

import pytest

from research.src import eligibility, issue, ledger, pilot


class EvidenceFactory:
    """All publishers, audits, qualifications and dates here are test fixtures."""
    def __init__(self, root, monkeypatch):
        self.root = Path(root)
        self.clock = datetime(2030, 1, 1, 9, tzinfo=timezone.utc)
        owner = self
        class ClockDatetime(datetime):
            @classmethod
            def now(cls, tz=None):
                return owner.clock.astimezone(tz) if tz else owner.clock.replace(tzinfo=None)
        monkeypatch.setattr(eligibility, "datetime", ClockDatetime)
        monkeypatch.setattr(ledger, "datetime", ClockDatetime)
        monkeypatch.setattr(pilot, "_utc_now", lambda: owner.clock)
        monkeypatch.setattr(issue, "_utc_now", lambda: owner.clock)
        self.model_ref = self.ref("model.py", {"test_only": True})
        self.baseline_code_ref = self.ref("baseline.py", {"test_only": True, "method": "synthetic fixed population"})
        self.baseline_version = "fixture-population-1"
        self.baseline_approval = (self.clock-timedelta(days=90)).isoformat()
        self.baseline_definition = dict(schema_version="baseline-definition-1", status="APPROVED", lane="EPL", league="EPL",
            endpoint="REGULATION", families=["1X2", "TOTAL", "BTTS"], baseline_version=self.baseline_version,
            approved_utc=self.baseline_approval, reviewed_utc=self.baseline_approval, reviewed_by="SYNTHETIC TEST",
            basis="Fixed synthetic comparator, not a real baseline", code_artifacts=[self.baseline_code_ref])
        self.baseline_ref = self.ref("baseline-definition.json", self.baseline_definition)
        evidence = self.ref("lineage-basis.json", {"test_only": True, "basis": "Synthetic independent collection records"})
        self.sources = {"sources": {}}
        fields = {k: f"/event/{k}" for k in ("event_id", "league", "home", "away", "scheduled_start_utc", "actual_start_utc", "state", "endpoint", "score_home", "score_away")}
        for index, host in enumerate(("league.example", "club.example", "media.example")):
            sid = f"fixture-source-{index}"
            audit = self.ref(f"lineage-{index}.json", dict(independence_status="VERIFIED", source_id=sid,
                upstream_lineage_id=f"fixture-lineage-{index}", reviewed_utc=(self.clock-timedelta(days=60)).isoformat(),
                reviewed_by="SYNTHETIC TEST", basis="Separate synthetic collection", evidence_refs=[evidence]))
            parser_audit = self.ref(f"parser-{index}.json", dict(status="APPROVED", reviewed_by="SYNTHETIC TEST",
                basis="Static fields in synthetic publisher JSON", field_map=fields, actual_start_semantics="ACTUAL_START"))
            self.sources["sources"][sid] = dict(hostname=host, upstream_lineage_id=f"fixture-lineage-{index}",
                independence_status="VERIFIED", lineage_audit=audit, allowed_url_prefixes=[f"https://{host}/event/"],
                parser_id="REVIEWED_JSON_POINTER_V1", parser_audit=parser_audit, field_map=fields,
                endpoints=["REGULATION"], leagues=["EPL"], official=index == 0)
        self.sources_path = self.root/"sources_registry.json"
        self.write(self.sources_path, self.sources)
        holdout = self.ref("holdout.json", {"stage":"ONE_SHOT_HOLDOUT", "lane":"EPL", "league":"EPL", "model_version":"fixture-1", "endpoint":"REGULATION",
            "lane_decision": "M2_PASS", "validated_families": ["1X2", "TOTAL", "BTTS"],
            "baseline_version": self.baseline_version, "baseline_definition_ref": self.baseline_ref,
            "family_gates": {family:{"lane_decision":"M2_PASS","paired_logloss_ci95":[-.2,-.1]} for family in ("1X2","TOTAL","BTTS")}})
        shadow = self.ref("shadow.json", dict(independent_events=50,
            first_forecast_utc=(self.clock-timedelta(days=50)).isoformat(), last_forecast_utc=(self.clock-timedelta(days=20)).isoformat()))
        shadow_refs=[]
        for i in range(50):
            forecast=self.clock-timedelta(days=50)+timedelta(days=30*i/49)
            shadow_refs.append(self.ref(f"qualification-shadow-{i}.json",dict(event_id=f"qualification-fixture-{i}",lane="EPL",league="EPL",
                model_version="fixture-1",endpoint="REGULATION",model_artifacts=[self.model_ref],shadow_only=True,performance_eligible=False,
                baseline_version=self.baseline_version,baseline_definition_ref=self.baseline_ref,baseline_code_artifacts=[self.baseline_code_ref],
                forecast_utc=forecast.isoformat(),data_cutoff_utc=(forecast-timedelta(seconds=1)).isoformat(),start_utc=(forecast+timedelta(hours=1)).isoformat())))
        shadow_manifest=self.ref("shadow-manifest.json",dict(schema_version="shadow-manifest-1",receipts=shadow_refs))
        qualification = self.ref("qualification.json", dict(status="APPROVED", lane="EPL", league="EPL", model_version="fixture-1",
            endpoint="REGULATION", families=["1X2", "TOTAL", "BTTS"], reviewed_utc=(self.clock-timedelta(days=10)).isoformat(),
            reviewed_by="SYNTHETIC TEST", basis="Synthetic admission tests", holdout_ref=holdout, shadow_ref=shadow,
            issuer_ref=evidence, terminal_adapter_ref=evidence, shadow_manifest_ref=shadow_manifest,model_artifacts=[self.model_ref],
            baseline_version=self.baseline_version,baseline_definition_ref=self.baseline_ref))
        self.registry = {"admissions": [dict(lane="EPL", league="EPL", model_version="fixture-1", endpoint="REGULATION",
            families=["1X2", "TOTAL", "BTTS"], status="LIVE_QUALIFIED", qualified_utc=(self.clock-timedelta(days=9)).isoformat(),
            baseline_version=self.baseline_version,
            model_artifacts=[self.model_ref], qualification_artifacts=[{**qualification, "kind": "live_qualification"}],
            adjustment_methods=[dict(method_version="fixture-adjustment-1",status="APPROVED",approved_utc=(self.clock-timedelta(days=9)).isoformat(),artifact_ref=evidence)]) ],
            "baseline_definitions": [{k:self.baseline_definition[k] for k in ("baseline_version", "lane", "league", "endpoint", "families", "status", "approved_utc", "code_artifacts")}]}
        self.registry["baseline_definitions"][0]["definition_ref"] = self.baseline_ref
        self.registry_path = self.root/"admission_registry.json"
        self.write(self.registry_path, self.registry)
        self.ledger_path = self.root/"canonical.jsonl"
        self.part6 = self.root/"part6.md"
        self.part6.write_bytes(issue.PART6.read_bytes())
        self.reconciliation = self.root/"reconciliation.md"
        self.reconciliation.write_bytes(issue.RECONCILIATION.read_bytes())

    def write(self, path, value):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(eligibility.canonical_bytes(value)+b"\n")

    def ref(self, name, value):
        path = self.root/name
        self.write(path, value)
        return {"path": name, "sha256": eligibility.file_sha(path)}

    def refresh(self):
        self.write(self.registry_path, self.registry)
        self.write(self.sources_path, self.sources)

    def rehash_receipt(self, receipt):
        receipt["response_sha256"]=eligibility.file_sha(self.root/receipt["body_path"])
        ref=receipt["event_lineage_audit"]
        audit=json.loads((self.root/ref["path"]).read_text())
        audit["response_sha256"]=receipt["response_sha256"]
        receipt["event_lineage_audit"]=self.ref(ref["path"],audit)

    def bundle(self, event_id="event-1", when=None, adjustment="NONE"):
        when = when or self.clock
        cutoff, start = when-timedelta(seconds=1), when+timedelta(hours=1)
        artifact = {**self.ref(f"{event_id}-input.json", {"test_only": True, "known_before": cutoff.isoformat()}), "available_utc": cutoff.isoformat()}
        checksum = eligibility.digest([artifact])
        scores = [(2,1),(1,0),(0,1),(1,1),(0,0),(1,2)]
        mass = [.3,.2,.15,.2,.1,.05]
        masses = dict(model=mass, baseline=mass,
            card=[.8,.04,.04,.04,.04,.04] if adjustment == "GOOD" else [.04,.04,.8,.04,.04,.04] if adjustment == "BAD" else mass)
        distributions = {}
        for label, probs in masses.items():
            distributions[label] = self.ref(f"{event_id}-{label}.json", dict(schema_version="score-distribution-1", event_id=event_id,
                endpoint="REGULATION", model_version="fixture-1", baseline_version=self.baseline_version,
                baseline_definition_ref=self.baseline_ref,baseline_code_artifacts=[self.baseline_code_ref],data_cutoff_utc=cutoff.isoformat(),
                input_checksum=checksum, states=[dict(home=h,away=a,p=p) for (h,a),p in zip(scores,probs)]))
        contracts = [dict(market="1X2", side=s, line=None, endpoint="REGULATION") for s in ("HOME","DRAW","AWAY")]
        contracts += [dict(market="TOTAL", side=s, line=2.5, endpoint="REGULATION") for s in ("OVER","UNDER")]
        contracts += [dict(market="BTTS", side=s, line=None, endpoint="REGULATION") for s in ("YES","NO")]
        bundle = dict(schema_version=eligibility.SCHEMA_VERSION, event_id=event_id, lane="EPL", league="EPL", season="TEST2030",
            home="HOME", away="AWAY", endpoint="REGULATION", model_version="fixture-1", baseline_version=self.baseline_version,issued_utc=when.isoformat(),
            data_cutoff_utc=cutoff.isoformat(), scheduled_start_utc=start.isoformat(), input_artifacts=[artifact], input_checksum=checksum,
            registry_sha256=eligibility.file_sha(self.registry_path), sources_registry_sha256=eligibility.file_sha(self.sources_path),
            distributions=distributions, contracts=contracts, adjustment_type="NONE" if adjustment == "NONE" else "SYNTHETIC_TEST",
            adjustment_method_version="fixture-adjustment-1" if adjustment!="NONE" else None,
            adjustment_reason="Synthetic test only" if adjustment != "NONE" else "", adjustment_evidence=[{**self.model_ref,"available_utc":cutoff.isoformat()}] if adjustment != "NONE" else [])
        bundle["pregame_receipts"] = self.receipts(bundle, "PREGAME", cutoff)
        return bundle

    def receipts(self, bundle, state, retrieved, score=(2,1), actual=None):
        output=[]
        for sid, entry in self.sources["sources"].items():
            body = dict(event={k: bundle[k] for k in ("event_id","league","home","away","endpoint","scheduled_start_utc")})
            body["event"].update(state=state, actual_start_utc=actual.isoformat() if actual else None,
                                 score_home=score[0] if state=="FINAL" else None, score_away=score[1] if state=="FINAL" else None)
            ref = self.ref(f"{bundle['event_id']}-{sid}-{state}-{score[0]}-{score[1]}.json", body)
            event_audit=self.ref(f"{bundle['event_id']}-{sid}-{state}-{score[0]}-{score[1]}-audit.json",dict(event_id=bundle['event_id'],source_id=sid,
                upstream_lineage_id=entry["upstream_lineage_id"],response_sha256=ref["sha256"],independence_status="VERIFIED",
                reviewed_utc=retrieved.isoformat(),basis="Synthetic independent collection for this exact response",reviewed_by="SYNTHETIC TEST"))
            output.append(dict(source_id=sid, upstream_lineage_id=entry["upstream_lineage_id"], source_url=f"https://{entry['hostname']}/event/{bundle['event_id']}",
                retrieved_utc=retrieved.isoformat(), body_path=ref["path"], response_sha256=ref["sha256"],event_lineage_audit=event_audit))
        return output

    def terminal(self, bundle, score=(2,1), actual=None):
        actual = actual or eligibility.aware_time(bundle["scheduled_start_utc"])+timedelta(minutes=2)
        self.clock = max(self.clock, actual+timedelta(hours=2))
        result=deepcopy(bundle)
        result["terminal_receipts"] = self.receipts(bundle, "FINAL", self.clock, score, actual)
        return result

    def register(self, bundles):
        captured = min(eligibility.aware_time(b["issued_utc"]) for b in bundles)-timedelta(hours=1)
        events = [{k:b[k] for k in ("lane","league","season","event_id","home","away","scheduled_start_utc")} for b in bundles]
        native=[dict(id=e["event_id"],date=e["scheduled_start_utc"],status={"type":{"name":"STATUS_SCHEDULED","completed":False}}) for e in events]
        source = {**self.ref("universe-source.json", {"test_only": True, "events": native}),"parser_id":"ESPN_SCOREBOARD_V1","league":"EPL"}
        first=min(eligibility.aware_time(e["scheduled_start_utc"]) for e in events)
        last=max(eligibility.aware_time(e["scheduled_start_utc"]) for e in events)+timedelta(seconds=1)
        ref = self.ref("universe.json", dict(schema_version="event-universe-1", captured_utc=captured.isoformat(), events=events, source_refs=[source],
            population_rule=dict(league="EPL",season="TEST2030",from_utc=first.isoformat(),to_utc=last.isoformat(),state="PREGAME")))
        self.clock=captured
        ledger.register_universe(self.ledger_path, ref, evidence_root=self.root)
        self.universe_ref=ref
        return ref

    def issue(self, bundle):
        self.clock=eligibility.aware_time(bundle["issued_utc"])
        transaction=issue.prepare_issue(bundle,self.registry_path,sources_registry_path=self.sources_path,evidence_root=self.root,
            ledger_path=self.ledger_path,part6_path=self.part6,reconciliation_path=self.reconciliation)
        self.clock+=timedelta(milliseconds=1)
        result=issue.commit_issue(transaction,allow_real_issue=True)
        committed=ledger.committed_issues(ledger.read_records(self.ledger_path))[-1]
        return result, deepcopy(committed["bundle"])


@pytest.fixture
def evidence(tmp_path,monkeypatch):
    return EvidenceFactory(tmp_path,monkeypatch)


def test_full_cached_evidence_derives_probabilities_and_actual_start(evidence):
    bundle=evidence.bundle()
    result=eligibility.validate_evidence(bundle,evidence.registry_path,evidence_root=evidence.root)
    assert result.eligible, result.reasons
    assert result.verified["actual_start_utc"] is None
    home=next(r for r in result.verified["rows"] if r["market"]=="1X2" and r["selection"]=="HOME")
    assert home["p_model"]==pytest.approx(.5)
    settled=evidence.terminal(bundle)
    result=eligibility.validate_evidence(settled,evidence.registry_path,evidence_root=evidence.root,require_terminal=True)
    assert result.eligible, result.reasons
    assert result.verified["score_home"]==2


@pytest.mark.parametrize("change,phrase", [
    (lambda b: b.update(performance_eligible=True,schema_version=None),"versioned evidence"),
    (lambda b: b.update(issued_utc="2030-01-01T09:00:00"),"timezone aware"),
    (lambda b: b.update(data_cutoff_utc=b["issued_utc"]),"strict cutoff"),
    (lambda b: b.update(model_version="unknown"),"no unique admission"),
    (lambda b: b["contracts"][0].update(p_model=.99),"frozen distribution"),
    (lambda b: b["contracts"][0].update(endpoint="FINAL_SCORE"),"contract endpoint"),
    (lambda b: b.update(pregame_receipts=b["pregame_receipts"][:2]),"three verified independent"),
])
def test_missing_asserted_or_conflicting_evidence_fails_closed(evidence,change,phrase):
    bundle=evidence.bundle();change(bundle)
    result=eligibility.validate_evidence(bundle,evidence.registry_path,evidence_root=evidence.root)
    assert not result.eligible and phrase in result.reasons[0]


def test_unknown_and_shared_upstream_publishers_do_not_count_independence(evidence):
    evidence.sources["sources"]["fixture-source-1"]["independence_status"]="UNKNOWN";evidence.refresh()
    result=eligibility.validate_evidence(evidence.bundle(),evidence.registry_path,evidence_root=evidence.root)
    assert not result.eligible and "independence" in result.reasons[0]
    entry=evidence.sources["sources"]["fixture-source-1"]
    entry["independence_status"]="VERIFIED";entry["upstream_lineage_id"]="fixture-lineage-0"
    audit=json.loads((evidence.root/entry["lineage_audit"]["path"]).read_text());audit["upstream_lineage_id"]="fixture-lineage-0"
    entry["lineage_audit"]=evidence.ref("shared-lineage.json",audit);evidence.refresh()
    result=eligibility.validate_evidence(evidence.bundle(),evidence.registry_path,evidence_root=evidence.root)
    assert not result.eligible and "three verified independent" in result.reasons[0]


def test_rehashed_wrong_raw_event_is_rejected_and_schedule_cannot_supply_actual(evidence):
    bundle=evidence.bundle()
    receipt=bundle["pregame_receipts"][0];p=evidence.root/receipt["body_path"]
    obj=json.loads(p.read_text());obj["event"]["event_id"]="wrong";evidence.write(p,obj)
    evidence.rehash_receipt(receipt)
    result=eligibility.validate_evidence(bundle,evidence.registry_path,evidence_root=evidence.root)
    assert not result.eligible and "event_id mismatch" in result.reasons[0]
    bundle=evidence.bundle("other")
    settled=evidence.terminal(bundle)
    for r in settled["terminal_receipts"]:
        p=evidence.root/r["body_path"];obj=json.loads(p.read_text());obj["event"]["actual_start_utc"]=None;evidence.write(p,obj);evidence.rehash_receipt(r)
    settled["actual_start_utc"]=settled["scheduled_start_utc"]
    result=eligibility.validate_evidence(settled,evidence.registry_path,evidence_root=evidence.root,require_terminal=True)
    assert not result.eligible and "actual start is absent" in result.reasons[0]


def test_retrospective_status_cannot_issue_and_code_hash_change_blocks(evidence):
    evidence.registry["admissions"][0]["status"]="SHADOW_ONLY";evidence.refresh()
    result=eligibility.validate_evidence(evidence.bundle(),evidence.registry_path,evidence_root=evidence.root)
    assert not result.eligible and "not live qualified" in result.reasons[0]
    evidence.registry["admissions"][0]["status"]="LIVE_QUALIFIED";evidence.refresh()
    bundle=evidence.bundle();(evidence.root/evidence.model_ref["path"]).write_text("changed")
    result=eligibility.validate_evidence(bundle,evidence.registry_path,evidence_root=evidence.root)
    assert not result.eligible and "hash mismatch" in result.reasons[0]


def test_native_nbl_parser_checks_id_pagination_state_and_integer_score(tmp_path):
    source={"parser_id":"NBL_SCHEDULE_V1"}
    match=dict(id="native",season_type="regular",phase="upcoming",starts_at_ms=1893488400000,home={"team_code":"NZL"},away={"team_code":"CNS"})
    raw={"total":1,"matches":[match]}
    assert eligibility._parse_source(raw,source,"native",tmp_path)["state"]=="PREGAME"
    with pytest.raises(ValueError,match="absent"):
        eligibility._parse_source(raw,source,"wrong",tmp_path)
    raw["total"]=2
    with pytest.raises(ValueError,match="pagination"):
        eligibility._parse_source(raw,source,"native",tmp_path)
    raw["total"]=1;match.update(phase="complete",home_score=91.5,away_score=90)
    with pytest.raises(ValueError,match="invalid score"):
        eligibility._parse_source(raw,source,"native",tmp_path)


@pytest.mark.parametrize("change",[
    lambda r:r.update(stage="CHRONOLOGICAL_DEVELOPMENT_ONLY"),
    lambda r:r.update(model_version="new-unseen-model"),
    lambda r:r.update(validated_families=["1X2"]),
    lambda r:r["family_gates"]["BTTS"].update(paired_logloss_ci95=[-.1,.1]),
])
def test_generic_old_or_development_holdout_cannot_qualify_new_scope(evidence,change):
    report=json.loads((evidence.root/"holdout.json").read_text());change(report)
    holdout=evidence.ref("changed-holdout.json",report)
    qualification=json.loads((evidence.root/"qualification.json").read_text());qualification["holdout_ref"]=holdout
    ref=evidence.ref("changed-qualification.json",qualification)
    evidence.registry["admissions"][0]["qualification_artifacts"]=[{**ref,"kind":"live_qualification"}];evidence.refresh()
    result=eligibility.validate_evidence(evidence.bundle(),evidence.registry_path,evidence_root=evidence.root)
    assert not result.eligible and ("holdout" in result.reasons[0] or "family" in result.reasons[0])


def test_adjustment_method_and_evidence_must_be_available_before_cutoff(evidence):
    bundle=evidence.bundle(adjustment="GOOD");bundle["adjustment_method_version"]="unapproved"
    result=eligibility.validate_evidence(bundle,evidence.registry_path,evidence_root=evidence.root)
    assert not result.eligible and "method version" in result.reasons[0]
    bundle=evidence.bundle("late-evidence",adjustment="GOOD")
    bundle["adjustment_evidence"][0]["available_utc"]=(evidence.clock+timedelta(seconds=1)).isoformat()
    result=eligibility.validate_evidence(bundle,evidence.registry_path,evidence_root=evidence.root)
    assert not result.eligible and "unavailable at cutoff" in result.reasons[0]


def test_native_espn_and_mlb_do_not_invent_actual_start(tmp_path):
    espn={"header":{"competitions":[{"id":"12","date":"2030-01-01T10:00:00Z","status":{"type":{"name":"STATUS_FINAL","completed":True}},
        "competitors":[{"homeAway":"home","score":"2","team":{"displayName":"HOME"}},{"homeAway":"away","score":"1","team":{"displayName":"AWAY"}}]}]}}
    row=eligibility._parse_source(espn,{"parser_id":"ESPN_SUMMARY_V1"},"12",tmp_path)
    assert row["endpoint"]=="FINAL_SCORE" and "actual_start_utc" not in row
    mlb={"gameData":{"game":{"pk":45},"datetime":{"dateTime":"2030-01-01T10:00:00Z"},
        "status":{"abstractGameState":"Final","detailedState":"Final"},"teams":{"home":{"name":"HOME"},"away":{"name":"AWAY"}}},
        "liveData":{"linescore":{"teams":{"home":{"runs":3},"away":{"runs":1}}},"plays":{"allPlays":[{"about":{"startTime":"2030-01-01T10:05:00Z"}}]}}}
    row=eligibility._parse_source(mlb,{"parser_id":"MLB_STATSAPI_V1"},"45",tmp_path)
    assert row["score_home"]==3 and "actual_start_utc" not in row


def test_universe_cannot_omit_a_native_fixture(evidence):
    first=evidence.bundle("first");second=evidence.bundle("second",when=evidence.clock+timedelta(hours=1))
    ref=evidence.register([first,second])
    universe=json.loads((evidence.root/ref["path"]).read_text());universe["events"]=universe["events"][:1]
    incomplete=evidence.ref("incomplete-universe.json",universe)
    with pytest.raises(ValueError,match="omits/adds"):
        ledger.validate_universe(incomplete,evidence_root=evidence.root)


@pytest.mark.parametrize("too_short",[True,False])
def test_shadow_needs_both_fifty_events_and_four_weeks(evidence,too_short):
    manifest=json.loads((evidence.root/"shadow-manifest.json").read_text())
    report=json.loads((evidence.root/"shadow.json").read_text())
    if too_short:
        first=eligibility.aware_time(report["first_forecast_utc"])
        refs=[]
        for i,ref in enumerate(manifest["receipts"]):
            row=json.loads((evidence.root/ref["path"]).read_text());forecast=first+timedelta(days=i/49)
            row.update(forecast_utc=forecast.isoformat(),data_cutoff_utc=(forecast-timedelta(seconds=1)).isoformat(),start_utc=(forecast+timedelta(hours=1)).isoformat())
            refs.append(evidence.ref(ref["path"],row))
        manifest["receipts"]=refs;report["last_forecast_utc"]=(first+timedelta(days=1)).isoformat()
    else:
        manifest["receipts"]=[manifest["receipts"][0],manifest["receipts"][-1]];report["independent_events"]=2
    qualification=json.loads((evidence.root/"qualification.json").read_text())
    qualification["shadow_manifest_ref"]=evidence.ref("changed-shadow-manifest.json",manifest)
    qualification["shadow_ref"]=evidence.ref("changed-shadow.json",report)
    qref=evidence.ref("changed-shadow-qualification.json",qualification)
    evidence.registry["admissions"][0]["qualification_artifacts"]=[{**qref,"kind":"live_qualification"}];evidence.refresh()
    result=eligibility.validate_evidence(evidence.bundle(),evidence.registry_path,evidence_root=evidence.root)
    assert not result.eligible and "duration/sample" in result.reasons[0]
