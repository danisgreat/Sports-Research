"""Append a dated 2026-27 EPL result snapshot without touching the holdout."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from .load import BENCHMARK, OPENFOOTBALL, PROCESSED, ROOT, parse_openfootball, sha, team


def build(snapshot_utc: datetime | None = None) -> dict:
    now = snapshot_utc or datetime.now(timezone.utc)
    source = OPENFOOTBALL / "2026-27.txt"
    check = BENCHMARK / "2026-27.csv"
    if not source.exists() or not check.exists():
        raise FileNotFoundError("download current openfootball and Football-Data E0 snapshots first")
    frame = parse_openfootball(source, expected=None)
    frame = frame.loc[frame.kickoff_utc < now].copy()
    with check.open(newline="", encoding="utf-8-sig", errors="replace") as f:
        records = list(csv.DictReader(f))
    finals = {}
    for r in records:
        if not r.get("FTHG") or not r.get("FTAG"):
            continue
        key = (team(r["HomeTeam"]), team(r["AwayTeam"]))
        date = pd.to_datetime(r["Date"], dayfirst=True).date()
        clock = r.get("Time") or "12:00"
        scheduled = datetime.fromisoformat(f"{date}T{clock}:00").replace(tzinfo=ZoneInfo("Europe/London")).astimezone(timezone.utc)
        if scheduled >= now:
            raise ValueError("secondary source has a future final")
        if key in finals:
            raise ValueError("duplicate current fixture")
        finals[key] = dict(hg=int(r["FTHG"]), ag=int(r["FTAG"]),
                           kickoff_utc=scheduled, precision="EXACT" if r.get("Time") else "DATE_ONLY")
    primary = {(r.home,r.away): (r.hg,r.ag) for r in frame.itertuples()}
    secondary = {k:(v["hg"],v["ag"]) for k,v in finals.items()}
    if primary != secondary:
        raise ValueError(f"current EPL sources disagree: primary_only={len(primary.keys()-secondary.keys())}, secondary_only={len(secondary.keys()-primary.keys())}, scores={sum(primary[k]!=secondary[k] for k in primary.keys()&secondary.keys())}")
    frame["kickoff_utc"] = [finals[(r.home,r.away)]["kickoff_utc"] for r in frame.itertuples()]
    frame["kickoff_precision"] = [finals[(r.home,r.away)]["precision"] for r in frame.itertuples()]
    if frame.duplicated(["home","away"]).any() or len(set(frame.home)|set(frame.away)) > 20:
        raise ValueError("current fixture identities invalid")
    output = PROCESSED / "epl_2026-27_current.parquet"
    frame.sort_values("kickoff_utc").to_parquet(output,index=False)
    manifest = dict(snapshot_utc=now.isoformat(), results=len(frame),
                    openfootball_sha256=sha(source), football_data_sha256=sha(check),
                    parquet_sha256=sha(output), score_disagreements=0,
                    source_urls=["https://raw.githubusercontent.com/openfootball/england/master/2026-27/1-premierleague.txt",
                                 "https://www.football-data.co.uk/mmz4281/2627/E0.csv"],
                    market_fields_in_forecast_data=False)
    (PROCESSED / "epl_2026-27_current_manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    return manifest


if __name__ == "__main__":
    print(json.dumps(build(),indent=2))
