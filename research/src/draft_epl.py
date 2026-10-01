"""Build a non-issued EPL shadow draft from frozen model and event receipts.

The event receipt is independently researched before this script runs. No
market data or pregame bookmaker endpoint is called by this module.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd

from .dixon_coles import fit_dc, rates, score_matrix
from .emit_card import build, markdown
from .load import PROCESSED, ROOT, sha
from .model_custody import verify_model_build


def _states(matrix):
    return [dict(home=i,away=j,p=float(matrix[i,j]))
            for i in range(matrix.shape[0]) for j in range(matrix.shape[1])]


def draft(event_path: Path, output: Path, now: datetime | None = None) -> dict:
    now=now or datetime.now(timezone.utc)
    build_receipt=verify_model_build("EPL", "epl-dc-0.1.0")
    event=json.loads(event_path.read_text(encoding="utf-8"))
    if event.get("state")!="PREGAME":
        raise ValueError("event is not confirmed pregame")
    sources=event.get("identity_sources",[])
    if len({urlparse(url).netloc for url in sources if url.startswith("https://")})<3:
        raise ValueError("three distinct identity/state publishers are required")
    historical_path=PROCESSED/"matches.parquet"
    current_path=PROCESSED/"epl_2026-27_current.parquet"
    report=json.loads((ROOT/"runs/epl_2025-26_holdout.json").read_text(encoding="utf-8"))
    if report.get("lane_decision")!="M2_PASS":
        raise RuntimeError("EPL holdout is not passed")
    current_receipt=json.loads((PROCESSED/"epl_2026-27_current_manifest.json").read_text(encoding="utf-8"))
    snapshot=datetime.fromisoformat(current_receipt["snapshot_utc"])
    if not snapshot<=now or now-snapshot>timedelta(hours=24):
        raise ValueError("current-season score snapshot must be refreshed within 24 hours")
    if sha(historical_path)!=report["data_sha256"] or sha(current_path)!=current_receipt["parquet_sha256"]:
        raise RuntimeError("score input changed since its receipt")
    old=pd.read_parquet(historical_path)
    current=pd.read_parquet(current_path)
    history=pd.concat([old,current],ignore_index=True)
    model=fit_dc(history,pd.Timestamp(snapshot),float(report["xi"]))
    home,away=event["home"],event["away"]
    if home not in set(current.home)|set(current.away) or away not in set(current.home)|set(current.away):
        raise ValueError("event team not in current EPL season")
    lam,mu=rates(model,home,away)
    base_matrix,_=score_matrix(lam,mu,float(model.params[-1]))
    factors=event.get("adjustment_factors",{"home":1.0,"away":1.0})
    fh,fa=float(factors["home"]),float(factors["away"])
    if not .7<=fh<=1.3 or not .7<=fa<=1.3:
        raise ValueError("adjustment factor outside preregisterable review range")
    adjusted=(fh!=1.0 or fa!=1.0)
    card_matrix,_=score_matrix(lam*fh,mu*fa,float(model.params[-1])) if adjusted else (base_matrix,0)
    prior=json.loads((PROCESSED/"epl_2026-27_population_states.json").read_text(encoding="utf-8"))
    if prior["source_parquet_sha256"]!=sha(historical_path):
        raise RuntimeError("population baseline input changed")
    checksum=hashlib.sha256((sha(historical_path)+sha(current_path)).encode()).hexdigest()
    evidence_times=[datetime.fromisoformat(event[key].replace("Z","+00:00"))
                    for key in ("lineup_retrieved_utc","state_retrieved_utc","recency_retrieved_utc")]
    if any(t.tzinfo is None or t>now for t in evidence_times):
        raise ValueError("an evidence retrieval time is missing, naive or in the future")
    cutoff=max(snapshot,*evidence_times)
    spec=dict(official_event_id=str(event["official_event_id"]),card_id=event.get("card_id","DRAFT"),
              start_utc=event["start_utc"],data_cutoff_utc=cutoff.isoformat(),
              state_source_url=event["state_source_url"],model_version="epl-dc-0.1.0",
              data_checksum=checksum,model_states=_states(base_matrix),
              card_states=_states(card_matrix),baseline_states=prior["states"],
              lane_status="UNVALIDATED",lineup_status=event["lineup_status"],
              lineup_source_url=event["lineup_source_url"],
              lineup_retrieved_utc=event["lineup_retrieved_utc"],
              recency_check=event["recency_check"],
              adjustment_type=event.get("adjustment_type","NONE") if adjusted else "NONE",
              adjustment_reason=event.get("adjustment_reason","") if adjusted else "",
              adjustment_parameters=factors if adjusted else {},
              contracts=[dict(market="1X2",side=side,line=None,endpoint="REGULATION") for side in ("HOME","DRAW","AWAY")]
              +[dict(market="TOTAL",side=side,line=2.5,endpoint="REGULATION") for side in ("OVER","UNDER")]
              +[dict(market="BTTS",side=side,line=None,endpoint="REGULATION") for side in ("YES","NO")])
    output_data=build(spec,now)
    output_data["model_rates"]=dict(home=lam,away=mu,home_factor=fh,away_factor=fa)
    output_data["identity_sources"]=sources
    output_data["event_receipt_sha256"]=sha(event_path)
    output_data["shadow_only"]=True
    output_data["issuance_status"]="READ_ONLY_DRAFT / NOT_ISSUED"
    output_data["performance_eligible"]=False
    output_data["model_build_receipt_sha256"]=sha(ROOT/"model_builds/current.json")
    output_data["qualified_families"]=build_receipt.get("retrospective_families", [])
    output_data["unvalidated_families"]=["TOTAL_2_5", "BTTS"]
    output.parent.mkdir(parents=True,exist_ok=True)
    if output.exists() or output.with_suffix(".md").exists():
        raise FileExistsError("draft output already exists; use a new immutable name")
    output.write_text(json.dumps(output_data,indent=2)+"\n",encoding="utf-8")
    output.with_suffix(".md").write_text(markdown(output_data),encoding="utf-8")
    return output_data


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("event_receipt",type=Path)
    parser.add_argument("output_json",type=Path)
    a=parser.parse_args()
    result=draft(a.event_receipt,a.output_json)
    print(result["card_distribution_sha256"])
