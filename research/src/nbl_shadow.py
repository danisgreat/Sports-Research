"""Freeze model-only NBL27 forecasts before fixtures, without card issuance."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

from .load import ROOT, sha
from .nbl_evaluate import MODEL_CODE, checked_data
from .nbl_model import fit, predict
from .model_custody import verify_model_build

PROCESSED = ROOT / "data/processed"
SHADOW = ROOT / "shadow/nbl27"


def freeze(now: datetime | None = None, window_hours: int = 48) -> list[Path]:
    now = now or datetime.now(timezone.utc)
    verify_model_build("NBL", "nbl-joint-0.1.0")
    if now.tzinfo is None or not 0 < window_hours <= 48:
        raise ValueError("shadow requires aware time and 1-48 hour window")
    holdout_path = ROOT / "runs/nbl_2025-26_holdout.json"
    report = json.loads(holdout_path.read_text(encoding="utf-8"))
    if report["lane_decision"] != "M2_PASS":
        raise RuntimeError("NBL holdout has not passed")
    lock = json.loads((ROOT / "runs/nbl_tuning_lock.json").read_text(encoding="utf-8"))
    if sha(MODEL_CODE) != lock["model_code_sha256"]:
        raise RuntimeError("NBL model code changed after the holdout lock")
    manifest_path = PROCESSED / "nbl_2026-27_current_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    snapshot = datetime.fromisoformat(manifest["snapshot_utc"])
    if not snapshot <= now or now-snapshot > timedelta(hours=24):
        raise ValueError("NBL score snapshot older than 24 hours")
    final_path = PROCESSED / "nbl_2026-27_current.parquet"
    fixtures_path = PROCESSED / "nbl_2026-27_fixtures.json"
    if sha(final_path) != manifest["parquet_sha256"] or sha(fixtures_path) != manifest["fixtures_sha256"]:
        raise RuntimeError("current NBL files changed after snapshot")
    history = checked_data()
    current = pd.read_parquet(final_path)
    if current.event_id.duplicated().any() or (current.kickoff_utc >= snapshot).any():
        raise ValueError("NBL current finals not strictly before snapshot")
    all_scores = pd.concat([history,current],ignore_index=True)
    if all_scores.event_id.duplicated().any():
        raise ValueError("NBL current and historic event IDs overlap")
    model = fit(all_scores,pd.Timestamp(snapshot),report["selected_half_life_days"])
    fixtures=json.loads(fixtures_path.read_text(encoding="utf-8"))
    selected=[]
    for fixture in fixtures:
        start=datetime.fromisoformat(fixture["kickoff_utc"])
        if now < start <= now+timedelta(hours=window_hours):
            if fixture["state"] != "UPCOMING":
                raise ValueError("NBL fixture is not pregame")
            selected.append(fixture)
    selected.sort(key=lambda f:(f["kickoff_utc"],f["event_id"]))
    if len({f["event_id"] for f in selected}) != len(selected):
        raise ValueError("duplicate NBL shadow fixture")
    pending=[]
    for fixture in selected:
        path=SHADOW/f"{fixture['event_id']}.json"
        if path.exists():
            previous=json.loads(path.read_text(encoding="utf-8"))
            if (previous.get("event_id")!=fixture["event_id"] or previous.get("home")!=fixture["home"]
                    or previous.get("away")!=fixture["away"]
                    or datetime.fromisoformat(previous["start_utc"])!=datetime.fromisoformat(fixture["kickoff_utc"])):
                raise ValueError("an existing NBL shadow event identity changed; audit without overwrite")
            continue
        pending.append((fixture,path))
    SHADOW.mkdir(parents=True,exist_ok=True)
    input_checksum=hashlib.sha256((sha(ROOT/"data/processed/nbl_matches.parquet")+sha(final_path)).encode()).hexdigest()
    for f,path in pending:
        joint,p_home=predict(model,f["home"],f["away"])
        row=dict(stage="MODEL_ONLY_SHADOW",shadow_only=True,performance_eligible=False,
                 event_id=f["event_id"],season="NBL27",official_event_url=f["source_url"],
                 home=f["home"],away=f["away"],start_utc=datetime.fromisoformat(f["kickoff_utc"]).isoformat(),
                 forecast_utc=now.astimezone(timezone.utc).isoformat(),
                 data_cutoff_utc=snapshot.astimezone(timezone.utc).isoformat(),
                 model_version=report["model_version"],
                 input_checksum=input_checksum,current_snapshot_sha256=sha(manifest_path),
                 holdout_report_sha256=sha(holdout_path),training_matches=model.training_matches,
                 effective_matches=model.effective_matches,
                 p_model_home_ml=p_home,p_model_away_ml=1-p_home,
                 joint_margin_total=dict(mean_margin=joint.mean_margin,mean_total=joint.mean_total,
                                         sd_margin=joint.sd_margin,sd_total=joint.sd_total,
                                         correlation=joint.correlation),
                 issuance_status="NO_CARD_ISSUED",adjustment_status="NOT_RESEARCHED")
        path.write_text(json.dumps(row,indent=2)+"\n",encoding="utf-8")
    return [path for _,path in pending]


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--window-hours",type=int,default=48)
    args=parser.parse_args()
    for path in freeze(window_hours=args.window_hours):
        print(path)
