"""Snapshot NBL27 official results and fixtures, with a second score check."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

import pandas as pd

from .load import ROOT, sha
from .nbl_load import TEAM_NAMES

OFFICIAL_URL = "https://schedule.nbl.com.au/api/calendar/schedule?league=NBL&limit=500&offset=0&year=2026"
SECONDARY_URL = "https://fixturedownload.com/feed/json/nbl-2026"
RAW = ROOT / "data/raw/nbl_official"
LOCAL = ROOT / "data/benchmark/nbl_fixturedownload"
PROCESSED = ROOT / "data/processed"


def _fetch(url: str) -> bytes:
    with urlopen(Request(url, headers={"User-Agent":"Mozilla/5.0"}), timeout=30) as response:
        return response.read()


def build(now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError("NBL snapshot time must be timezone aware")
    official_raw, second_raw = _fetch(OFFICIAL_URL), _fetch(SECONDARY_URL)
    official, second = json.loads(official_raw), json.loads(second_raw)
    if official.get("total") != len(official.get("matches", [])) or not isinstance(second, list):
        raise ValueError("NBL snapshot pagination or schema changed")
    raw_name = "nbl27_" + now.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + ".json"
    official_path = RAW / raw_name
    second_path = LOCAL / raw_name
    if official_path.exists() or second_path.exists():
        raise FileExistsError("NBL snapshot already exists; use a new timestamp")
    official_path.parent.mkdir(parents=True, exist_ok=True)
    second_path.parent.mkdir(parents=True, exist_ok=True)
    official_path.write_bytes(official_raw)
    second_path.write_bytes(second_raw)
    crosscheck={}
    for row in second:
        if row.get("HomeTeamScore") is None or row.get("AwayTeamScore") is None:
            continue
        kickoff=datetime.fromisoformat(row["DateUtc"].replace(" ","T").replace("Z","+00:00"))
        key=(kickoff,TEAM_NAMES[row["HomeTeam"]],TEAM_NAMES[row["AwayTeam"]])
        if key in crosscheck:
            raise ValueError("duplicate current NBL secondary fixture")
        crosscheck[key]=(int(row["HomeTeamScore"]),int(row["AwayTeamScore"]))
    finals=[]; upcoming=[]; identities=set()
    for m in official["matches"]:
        if m.get("season_type")!="regular":
            continue
        event_id=str(m["id"])
        if event_id in identities:
            raise ValueError("duplicate current NBL event ID")
        identities.add(event_id)
        kickoff=datetime.fromtimestamp(m["starts_at_ms"]/1000,timezone.utc)
        home,away=m["home"]["team_code"],m["away"]["team_code"]
        key=(kickoff,home,away)
        base=dict(season="NBL27",event_id=event_id,kickoff_utc=kickoff,
                  round=int(m["round_label"]),home=home,away=away,
                  source_url=f"https://schedule.nbl.com.au/match?league=NBL&match={event_id}")
        if m.get("phase")=="complete":
            if kickoff>=now or m.get("home_score") is None or m.get("away_score") is None:
                raise ValueError("current NBL feed has impossible final")
            actual=(int(m["home_score"]),int(m["away_score"]))
            if crosscheck.get(key)!=actual:
                raise ValueError(f"NBL27 final not confirmed by second publisher: {event_id}")
            finals.append({**base,"hg":actual[0],"ag":actual[1]})
        elif m.get("phase")=="upcoming":
            if kickoff<=now:
                raise ValueError(f"past NBL event still marked upcoming: {event_id}")
            upcoming.append({**base,"state":"UPCOMING"})
        else:
            raise ValueError(f"unexpected NBL event phase: {m.get('phase')}")
    if len(finals)+len(upcoming)!=len(identities) or len(crosscheck)!=len(finals):
        raise ValueError("current NBL source coverage mismatch")
    final_path=PROCESSED/"nbl_2026-27_current.parquet"
    fixture_path=PROCESSED/"nbl_2026-27_fixtures.json"
    pd.DataFrame(finals).sort_values("kickoff_utc").to_parquet(final_path,index=False)
    fixture_path.write_text(json.dumps(upcoming,indent=2,default=str)+"\n",encoding="utf-8")
    receipt=dict(snapshot_utc=now.astimezone(timezone.utc).isoformat(),
                 official_url=OFFICIAL_URL,second_source_url=SECONDARY_URL,
                 official_raw_path=str(official_path.relative_to(ROOT)).replace("\\","/"),
                 official_raw_sha256=hashlib.sha256(official_raw).hexdigest(),
                 second_raw_sha256=hashlib.sha256(second_raw).hexdigest(),
                 completed=len(finals),upcoming=len(upcoming),
                 score_disagreements=0,parquet_sha256=sha(final_path),
                 fixtures_sha256=sha(fixture_path),market_fields_in_forecast_data=False)
    (PROCESSED/"nbl_2026-27_current_manifest.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    return receipt


if __name__=="__main__":
    print(json.dumps(build(),indent=2))
