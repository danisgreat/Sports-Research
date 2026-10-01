"""Immutable daily score snapshots, complete fixture coverage and model shadows.

This command never issues a card or makes a performance-eligible record. Fresh
single-publisher observations are explicitly provisional, even when official.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from .load import ROOT, DATE_RE, MATCH_RE, V_MATCH_RE, parse_openfootball, team, sha
from .sources import fetch_source, verified_body, read_registry
from .candidate_models import epl, nbl, EPL_VERSION, NBL_VERSION

DAILY = ROOT / "daily"


def put_json(path, obj):
    with Path(path).open("x", encoding="utf-8") as handle:
        json.dump(obj, handle, indent=2, default=str, allow_nan=False)
        handle.write("\n")


def parse_nbl(obj, observed):
    if obj.get("total") != len(obj.get("matches", [])):
        raise ValueError("NBL pagination/schema incomplete")
    finals, fixtures, excluded, seen = [], [], [], set()
    for match in obj["matches"]:
        if match.get("season_type") != "regular":
            continue
        event_id = str(match["id"])
        if not event_id or event_id in seen:
            raise ValueError("duplicate/missing official NBL identity")
        seen.add(event_id)
        start = datetime.fromtimestamp(match["starts_at_ms"]/1000, timezone.utc)
        base = dict(season="NBL27", event_id=event_id, official_event_id=event_id,
                    kickoff_utc=start, kickoff_precision="SCHEDULED_TIME",
                    home=match["home"]["team_code"], away=match["away"]["team_code"],
                    round=match["round_label"],
                    source_url=f"https://schedule.nbl.com.au/match?league=NBL&match={event_id}")
        phase = match.get("phase")
        if phase == "complete":
            h, a = match.get("home_score"), match.get("away_score")
            if start >= observed or any(isinstance(v, bool) or not isinstance(v, int) or v < 0 for v in (h, a)) or h == a:
                raise ValueError("impossible NBL final")
            finals.append({**base, "hg":h, "ag":a, "state":"FINAL"})
        elif phase == "upcoming" and start > observed:
            fixtures.append({**base, "state":"PREGAME"})
        else:
            excluded.append({**base, "state":str(phase), "reason":"NOT_FRESH_PREGAME_OR_TERMINAL"})
    return pd.DataFrame(finals), fixtures, excluded


def parse_epl_fixtures(path, observed):
    """Keep provider identities separate from official IDs; never guess an ID."""
    fixtures, excluded, seen = [], [], set()
    current_date = clock = round_no = None
    year = int(Path(path).stem[:4])
    for line_no, line in enumerate(Path(path).read_text(encoding="utf-8-sig").splitlines(), 1):
        round_match = re.search(r"Matchday\s+(\d+)", line)
        if round_match:
            round_no = int(round_match.group(1))
        date_match = DATE_RE.match(line.strip())
        if date_match:
            month, day, explicit = date_match.groups()
            month_no = datetime.strptime(month, "%b").month
            current_date = datetime(int(explicit) if explicit else year+(month_no<7), month_no, int(day))
            clock = None
            continue
        if MATCH_RE.match(line) or V_MATCH_RE.match(line):
            continue
        match = re.match(r"^\s*(?:(\d{1,2}:\d{2})\s+)?(.+?)\s+v\s+(.+?)\s*$", line)
        if not match:
            continue
        stamp, home, away = match.groups()
        if stamp:
            clock = stamp
        identity = (team(home), team(away))
        if identity in seen:
            raise ValueError("duplicate EPL scheduled fixture")
        seen.add(identity)
        base = dict(home=identity[0], away=identity[1], season="2026-27", round=round_no,
                    official_event_id=None, source_line=line_no, source_id="openfootball")
        if current_date is None or clock is None:
            excluded.append({**base,"reason":"SCHEDULE_TIME_MISSING","state":"UNKNOWN"})
            continue
        hh, mm = map(int, clock.split(":"))
        start = current_date.replace(hour=hh, minute=mm, tzinfo=ZoneInfo("Europe/London")).astimezone(timezone.utc)
        base.update(kickoff_utc=start, kickoff_precision="PUBLISHER_SCHEDULED_TIME",
                    event_id=f"OF:2026-27:{current_date.date()}:{identity[0]}:{identity[1]}")
        if start <= observed:
            excluded.append({**base,"reason":"PAST_FIXTURE_WITHOUT_TERMINAL_SCORE","state":"UNKNOWN"})
        else:
            fixtures.append({**base,"state":"PUBLISHER_SCHEDULED; OFFICIAL_ID_UNVERIFIED"})
    return fixtures, excluded


def snapshot(lane, directory):
    source_id = "nbl_official" if lane == "NBL" else "openfootball"
    receipt = fetch_source(source_id, read_registry()[source_id]["probe_url"])
    raw = verified_body(receipt)
    observed = datetime.fromisoformat(receipt["retrieved_utc"])
    if lane == "NBL":
        frame, fixtures, exclusions = parse_nbl(json.loads(raw), observed)
    else:
        source = directory/"2026-27.txt"
        with source.open("xb") as handle:
            handle.write(raw)
        frame = parse_openfootball(source, expected=None)
        # The legacy parser stores its displayed local clock in a UTC column;
        # historical crosscheck() corrects it. This fresh primary-only snapshot
        # must do the explicit Europe/London conversion itself.
        frame["kickoff_utc"] = [stamp.to_pydatetime().replace(tzinfo=ZoneInfo("Europe/London")).astimezone(timezone.utc)
                                for stamp in frame.kickoff_utc]
        frame["event_id"] = [f"OF:2026-27:{r.kickoff_utc.date()}:{r.home}:{r.away}" for r in frame.itertuples()]
        if (frame.kickoff_utc >= observed).any():
            raise ValueError("EPL primary has a future final")
        fixtures, exclusions = parse_epl_fixtures(source, observed)
    if frame.empty or frame.event_id.duplicated().any():
        raise ValueError("empty/duplicate current final snapshot")
    frame["source_verified"] = True
    frame["corroboration_status"] = "SINGLE_PUBLISHER_PROVISIONAL"
    frame["available_at_utc"] = observed.isoformat()
    output = directory/"scores.parquet"
    frame.sort_values("kickoff_utc").to_parquet(output, index=False)
    put_json(directory/"fixtures.json", fixtures)
    put_json(directory/"excluded_fixtures.json", exclusions)
    manifest = dict(lane=lane, snapshot_utc=observed.isoformat(), receipt=receipt,
                    completed=len(frame), upcoming=len(fixtures), excluded=len(exclusions),
                    scores_sha256=sha(output), fixtures_sha256=sha(directory/"fixtures.json"),
                    corroboration_status="SINGLE_PUBLISHER_PROVISIONAL",
                    live_admissible=False, market_fields_in_forecast_data=False)
    put_json(directory/"snapshot.json", manifest)
    return frame, fixtures, manifest


def freeze(lane, current, fixtures, manifest, directory, now, hours):
    history_path = ROOT/"data/processed"/("nbl_matches.parquet" if lane=="NBL" else "matches.parquet")
    history = pd.read_parquet(history_path)
    expected = json.loads((ROOT/"runs"/("nbl_2025-26_holdout.json" if lane=="NBL" else "epl_2025-26_holdout.json")).read_text())
    if sha(history_path) != expected["data_sha256"]:
        raise ValueError("historical input differs from evaluated input")
    if "event_id" not in history.columns:
        history["event_id"] = [f"OF:{r.season}:{r.kickoff_utc.date()}:{r.home}:{r.away}" for r in history.itertuples()]
    data = pd.concat([history, current], ignore_index=True)
    if data.event_id.duplicated().any():
        raise ValueError("historic/current identity overlap")
    coverage = []
    cutoff = pd.Timestamp(manifest["snapshot_utc"])
    if not cutoff.to_pydatetime() < now:
        raise ValueError("cutoff must strictly precede freeze")
    for fixture in sorted(fixtures, key=lambda x:(str(x["kickoff_utc"]), x["event_id"])):
        start = pd.Timestamp(fixture["kickoff_utc"]).to_pydatetime()
        base = dict(event_id=fixture["event_id"], start_utc=start.isoformat(), home=fixture["home"], away=fixture["away"])
        if not now < start <= now+timedelta(hours=hours):
            coverage.append({**base,"status":"OUTSIDE_SHADOW_WINDOW"})
            continue
        try:
            if lane == "NBL":
                p, metadata = nbl(data, cutoff, fixture["home"], fixture["away"])
                probabilities = [p, 1-p]; family="ML"; endpoint="INCL_OT"
                states = None
            else:
                _, matrix, metadata = epl(data, "2026-27", cutoff, fixture["home"], fixture["away"])
                probabilities = [float(np.tril(matrix,-1).sum()), float(np.trace(matrix)), float(np.triu(matrix,1).sum())]
                family="1X2"; endpoint="REGULATION"
                states = matrix.tolist()
            if min(probabilities)<=0 or max(probabilities)>=1 or abs(sum(probabilities)-1)>1e-9:
                raise ValueError("invalid probability vector")
            name = re.sub(r"[^A-Za-z0-9._-]", "_", fixture["event_id"])+".json"
            row = dict(**base, lane=lane, official_event_id=fixture.get("official_event_id"),
                       stage="MODEL_ONLY_SHADOW", issuance_status="NO_CARD_ISSUED",
                       performance_eligible=False, family=family, endpoint=endpoint,
                       forecast_utc=now.isoformat(), data_cutoff_utc=cutoff.isoformat(),
                       probabilities=probabilities, model_version=metadata["model_version"],
                       model_metadata=metadata, score_states=states,
                       model_build_receipt_sha256=sha(ROOT/"model_builds/current.json"),
                       historical_input_sha256=sha(history_path), current_input_sha256=manifest["scores_sha256"],
                       source_receipt=manifest["receipt"],
                       input_quality="SINGLE_PUBLISHER_PROVISIONAL; NOT_LIVE_ADMISSIBLE",
                       adjustment_status="NONE", lineup_status="NOT_RESEARCHED")
            put_json(directory/name, row)
            coverage.append({**base,"status":"SHADOW_FROZEN","path":name})
        except (ValueError, KeyError, RuntimeError) as exc:
            coverage.append({**base,"status":"NO_FORECAST","reason":str(exc)})
    put_json(directory/"coverage.json", coverage)
    return coverage


def grade_nbl_shadows(finals, source_receipt, directory):
    """Append diagnostic grades; one official response cannot certify settlement."""
    by_id = {str(row.event_id):row for row in finals.itertuples()}
    outcomes = []
    paths = list((ROOT/"shadow/nbl27").glob("*.json"))
    paths += list(DAILY.glob("*/NBL/shadows/*.json"))
    for path in paths:
        if path.name=="coverage.json":
            continue
        record = json.loads(path.read_text(encoding="utf-8"))
        event_id = str(record.get("event_id"))
        if event_id not in by_id:
            continue
        final = by_id[event_id]
        cutoff = pd.Timestamp(record["data_cutoff_utc"])
        issue = pd.Timestamp(record["forecast_utc"])
        start = pd.Timestamp(record["start_utc"])
        p = record.get("p_model_home_ml", (record.get("probabilities") or [None])[0])
        if any(t.tzinfo is None for t in (cutoff,issue,start)) or not cutoff<issue<start or not isinstance(p,(int,float)) or not 0<p<1:
            continue
        if record.get("home")!=final.home or record.get("away")!=final.away or start!=final.kickoff_utc:
            outcomes.append(dict(event_id=event_id,status="IDENTITY_OR_RESCHEDULE_CONFLICT",shadow_path=path.relative_to(ROOT.parent).as_posix()))
            continue
        y = int(final.hg>final.ag)
        outcomes.append(dict(event_id=event_id,status="MODEL_ONLY_DIAGNOSTIC_GRADE",performance_eligible=False,
                             official_final_verified=True, certified_settlement=False,
                             shadow_path=path.relative_to(ROOT.parent).as_posix(), shadow_sha256=sha(path),
                             final_home=int(final.hg),final_away=int(final.ag),p_home=p,
                             brier=(p-y)**2,logloss=float(-np.log(p if y else 1-p)),
                             receipt=source_receipt, reason="SINGLE_TERMINAL_PUBLISHER; ACTUAL_START_AND_INDEPENDENT_LINEAGES_NOT_CERTIFIED"))
    put_json(directory/"nbl_shadow_diagnostic_grades.json", outcomes)
    return outcomes


def run(window_hours=48):
    if not 1<=window_hours<=48:
        raise ValueError("window must be between 1 and 48 hours")
    created = datetime.now(timezone.utc)
    directory=DAILY/created.strftime("%Y%m%dT%H%M%S%fZ")
    directory.mkdir(parents=True, exist_ok=False)
    result=dict(created_utc=created.isoformat(), status="RUNNING", no_cards_issued=True, lanes={})
    for lane in ("EPL","NBL"):
        target=directory/lane; target.mkdir()
        try:
            current, fixtures, manifest = snapshot(lane, target)
            shadows=target/"shadows"; shadows.mkdir()
            coverage=freeze(lane,current,fixtures,manifest,shadows,datetime.now(timezone.utc),window_hours)
            grades=grade_nbl_shadows(current,manifest["receipt"],target) if lane=="NBL" else []
            result["lanes"][lane]=dict(status="SHADOW_ONLY", completed=len(current), upcoming=len(fixtures),
                frozen=sum(r["status"]=="SHADOW_FROZEN" for r in coverage),
                abstained=sum(r["status"]=="NO_FORECAST" for r in coverage),diagnostic_grades=len(grades))
        except Exception as exc:
            result["lanes"][lane]=dict(status="FAILED_CLOSED",reason=f"{type(exc).__name__}: {exc}")
    result["status"]="COMPLETE" if all(v["status"]=="SHADOW_ONLY" for v in result["lanes"].values()) else "PARTIAL_FAILURE"
    put_json(directory/"run.json",result)
    return directory, result


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--window-hours",type=int,default=48)
    args=parser.parse_args()
    path, result=run(args.window_hours)
    print(path)
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if result["status"]=="COMPLETE" else 1)
