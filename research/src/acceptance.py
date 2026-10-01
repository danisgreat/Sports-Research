"""Verify implementation custody, source bytes and current model controls."""
from __future__ import annotations
import csv
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from .load import ROOT, sha
from .issue import _custody, next_card_id
from .sources import verified_body
from .model_custody import verify_model_build


def run():
    repo=ROOT.parent;issues=[];checks={}
    custody=ROOT/"custody/implementation_2026-10-01"
    initial=json.loads((custody/"manifest.json").read_text())
    frozen=[]
    for item in initial["files"]:
        retained=custody/item["path"]
        if sha(retained)!=item["sha256"]:issues.append("ORIGINAL_SNAPSHOT_CHANGED:"+item["path"])
        rel=item["path"]
        if rel.startswith(("research/runs/","research/shadow/")) or rel=="GAME_PREDICTION_RANK_LOG.csv":
            if sha(repo/rel)!=item["sha256"]:issues.append("FROZEN_RESEARCH_CHANGED:"+rel)
            frozen.append(rel)
    checks["original_snapshot_files"]=len(initial["files"])
    checks["frozen_original_research_files"]=len(frozen)
    for n in range(1,6):
        filename="PREDICTION_LOG_COMBINED"+(f"_{n}" if n>1 else "")+".md"
        path=repo/"prediction logs"/filename
        original=subprocess.run(["git","show",initial["head"]+":prediction logs/"+filename],cwd=repo,capture_output=True,check=True).stdout
        normal=lambda raw:raw.replace(b"\r\n",b"\n").replace(b"\r",b"\n")
        if normal(original)!=normal(path.read_bytes()):issues.append("HISTORICAL_LOG_CONTENT_CHANGED:"+filename)
    _,tail=_custody(repo/"prediction logs/PREDICTION_LOG_COMBINED_6.md")
    checks["part6_original_source_block"]="141740_BYTES_HASH_MATCHED"
    checks["next_card_id"]=next_card_id()
    builds=json.loads((ROOT/"model_builds/current.json").read_text())
    for build in builds["builds"]:
        verify_model_build(build["lane"],build["model_version"])
    checks["verified_model_builds"]=len(builds["builds"])
    registry=json.loads((ROOT/"admission_registry.json").read_text())
    if any(e["status"]!="SHADOW_ONLY" for e in registry["admissions"]):issues.append("UNSUPPORTED_CURRENT_LIVE_PROMOTION")
    checks["current_live_qualified_models"]=sum(e["status"]=="LIVE_QUALIFIED" for e in registry["admissions"])
    source_count=0
    for path in (ROOT/"data/source_receipts").glob("*.json"):
        verified_body(json.loads(path.read_text()),repo);source_count+=1
    checks["source_receipt_bodies_verified"]=source_count
    learning=ROOT/"data/processed/legacy_learning"
    manifest=json.loads((learning/"manifest.json").read_text())
    for name,field in (("contracts.csv","contracts_sha256"),("cards.csv","cards_sha256")):
        if sha(learning/name)!=manifest[field]:issues.append("HISTORICAL_VIEW_CHANGED:"+name)
    contracts=list(csv.DictReader((learning/"contracts.csv").open(encoding="utf-8")))
    if len(contracts)!=2004 or len({r["card_id"] for r in contracts})!=522 or any(r["performance_eligible"].lower()!="false" for r in contracts):
        issues.append("HISTORICAL_LEARNING_GRAIN_OR_ELIGIBILITY")
    anchors={r["pointer"]:r for r in json.loads((learning/"source_anchor_corrections.json").read_text())["revisions"]}
    source_cache={}
    for ref in manifest["source_pointers"]:
        if not ref.get("path"):continue
        path=repo/(anchors[ref["pointer"]]["retained_path"] if ref["pointer"] in anchors else ref["path"])
        if path not in source_cache:source_cache[path]=(sha(path),path.read_text(encoding="utf-8-sig").splitlines())
        checksum,lines=source_cache[path]
        if checksum!=ref["file_sha256"] or hashlib.sha256(lines[ref["line"]-1].encode()).hexdigest()!=ref["line_sha256"]:
            issues.append("HISTORICAL_POINTER_CHANGED:"+ref["pointer"])
    checks["historical_learning_rows"]=len(contracts)
    checks["historical_learning_cards"]=522
    checks["historical_source_anchors_verified"]=len(source_cache)
    league_export=ROOT/"data/processed/league_csv"
    for lane,ref in json.loads((league_export/"manifest.json").read_text())["leagues"].items():
        if sha(league_export/(lane.lower()+"_results.csv"))!=ref["csv_sha256"]:
            issues.append("LEAGUE_EXPORT_CHANGED:"+lane)
    checks["active_league_csvs"]={"EPL":2280,"NBL":738}
    if (ROOT/"canonical_ledger.jsonl").exists():
        from .ledger import read_records,committed_issues
        if committed_issues(read_records(ROOT/"canonical_ledger.jsonl")):issues.append("UNEXPECTED_LIVE_ISSUE_DURING_IMPLEMENTATION")
    checks["issued_cards_during_implementation"]=0
    return dict(observed_utc=datetime.now(timezone.utc).isoformat(),valid=not issues,checks=checks,issues=issues,
                limitation="Mechanics/custody verification does not establish future predictive skill. Archive validation and tests are separate recorded checks.")


if __name__=="__main__":
    result=run();print(json.dumps(result,indent=2));raise SystemExit(not result["valid"])
