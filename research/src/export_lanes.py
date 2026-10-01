"""Export reconciled active-league histories as usable sports-only CSVs.

Provider-derived EPL keys remain separate from unknown official event IDs.
This is a lossless view of frozen processed histories, not new source truth.
"""
from __future__ import annotations
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd
from .load import ROOT, sha
from .nbl_evaluate import checked_data

OUTPUT=ROOT/"data/processed/league_csv"


def export(output=OUTPUT):
    output=Path(output)
    if output.exists():raise FileExistsError("league exports already exist; use a new versioned output")
    output.mkdir(parents=True,exist_ok=False)
    reports={}
    for lane in ("EPL","NBL"):
        source=ROOT/"data/processed"/("matches.parquet" if lane=="EPL" else "nbl_matches.parquet")
        holdout=json.loads((ROOT/"runs"/("epl_2025-26_holdout.json" if lane=="EPL" else "nbl_2025-26_holdout.json")).read_text())
        if sha(source)!=holdout["data_sha256"]:raise ValueError("processed source differs from frozen evaluated history")
        frame=pd.read_parquet(source) if lane=="EPL" else checked_data()
        input_checksum=sha(source)
        if frame.duplicated(["season","home","away","kickoff_utc"]).any():raise ValueError("duplicate league fixture")
        records=[]
        for row in frame.itertuples():
            official=str(row.event_id) if lane=="NBL" else ""
            key=official or f"EPL:{row.season}:{row.home}:{row.away}"
            records.append(dict(league=lane,season=row.season,event_key=key,official_event_id=official,
                home=row.home,away=row.away,scheduled_start_utc=row.kickoff_utc.isoformat(),
                time_precision=getattr(row,"kickoff_precision","SCHEDULED_TIME"),actual_start_utc="",available_at_utc="",
                home_score=int(row.hg),away_score=int(row.ag),total_score=int(row.hg+row.ag),margin_signed_home=int(row.hg-row.ag),
                endpoint="REGULATION" if lane=="EPL" else "INCL_OT",period="FULL_GAME",neutral_venue="",
                source_url=(f"https://raw.githubusercontent.com/openfootball/england/master/{row.season}/1-premierleague.txt" if lane=="EPL" else row.source_url),
                processed_input_sha256=input_checksum,evidence_status="RECONCILED_HISTORICAL_SNAPSHOT; ACTUAL_START_AND_PREGAME_AVAILABILITY_UNKNOWN"))
        path=output/(lane.lower()+"_results.csv")
        with path.open("x",encoding="utf-8",newline="") as handle:
            writer=csv.DictWriter(handle,fieldnames=list(records[0]));writer.writeheader();writer.writerows(records)
        reports[lane]=dict(rows=len(records),seasons=frame.groupby("season").size().to_dict(),input_sha256=sha(source),csv_sha256=sha(path))
    report=dict(created_utc=datetime.now(timezone.utc).isoformat(),leagues=reports,market_fields=False,
        limitation="Frozen processed score views. Exact source reconciliation remains in original data receipts; export hashes do not independently certify result truth, source independence or historical availability. No official EPL IDs or neutral venues are inferred.")
    with (output/"manifest.json").open("x",encoding="utf-8") as handle:json.dump(report,handle,indent=2);handle.write("\n")
    return report


if __name__=="__main__":
    print(json.dumps(export(),indent=2))
