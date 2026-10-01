"""Rebuild a conservative canonical archive without changing issued forecasts.

Raw yearly files remain evidence inputs. Exact field-owner result matches admit
historical labels under a prior-date-only contract. Narrative, season awards and
unverified participation are never pregame features. No market data is read.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import subprocess
import tempfile
from collections import Counter, defaultdict
from datetime import date, datetime, timezone
from pathlib import Path

try:
    from .archive_sources import EvidenceError, EvidenceIndex, atomic_bytes, sha256, read_receipt, audit_receipts
except ImportError:  # Direct CLI use from research/src.
    from archive_sources import EvidenceError, EvidenceIndex, atomic_bytes, sha256, read_receipt, audit_receipts

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE_ROOT = ROOT / "Previous Sports Results"
PARSER_VERSION = "archive-v1"
EVENT_FIELDS = ["event_id", "sport", "competition_id", "season_id", "event_date", "start_time_utc",
    "time_precision", "home_team_id", "home_team_name", "away_team_id", "away_team_name", "home_score",
    "away_score", "total_score", "margin_signed_home", "result", "result_endpoint", "result_period",
    "stage", "venue", "neutral_venue", "available_at_utc", "availability_rule", "retrieved_at_utc",
    "source_event_id", "source_url", "source_receipt_path", "source_body_sha256", "source_verified",
    "quality_status", "training_eligible", "exclusion_reasons", "origin_path", "origin_line",
    "origin_sha256", "parser_version", "data_snapshot_hash", "identity_repair_note", "source_parser_version"]
NARRATIVE_FIELDS = ["event_id", "origin_path", "origin_line", "notable_people", "comment", "temporal_role",
    "participation_verified", "pregame_feature_eligible", "exclusion_reason"]
PROVENANCE_FIELDS = ["event_id", "origin_path", "origin_line", "origin_sha256", "admission", "exclusion_reason", "duplicate_of"]
SEASON_FIELDS = ["sport", "competition", "competition_id", "season_folder", "origin_path", "origin_sha256",
    "rows", "unique_events", "verified_results", "training_eligible", "coverage_status", "lifecycle_status",
    "coverage_evidence", "excluded_rows", "issues", "source_final_games", "source_matched_games",
    "missing_source_games", "extra_unverified_games", "coverage_contract"]
ALIASES = {
    "kangaroos": "north melbourne", "north melbourne kangaroos": "north melbourne",
    "north melbourne tasmanian kangaroos": "north melbourne", "north melbourne tasmanian kangaroos w": "north melbourne",
    "south melbourne": "sydney", "sydney swans": "sydney", "sydney swans w": "sydney",
    "footscray": "western bulldogs", "bulldogs": "western bulldogs",
    "adelaide crows": "adelaide", "geelong cats": "geelong", "gws giants": "greater western sydney",
    "gws": "greater western sydney", "gold coast suns": "gold coast", "west coast eagles": "west coast",
    "st. kilda": "st kilda", "brisbane lions": "brisbane lions", "brisbane": "brisbane lions",
}
MLB_ALIASES = {"cleveland indians": "cleveland guardians", "tampa bay devil rays": "tampa bay rays",
    "florida marlins": "miami marlins", "montreal expos": "washington nationals",
    "anaheim angels": "los angeles angels", "los angeles angels of anaheim": "los angeles angels",
    "oakland athletics": "athletics", "sacramento athletics": "athletics"}
FIRST_SEASON = {"afl": 1897, "afl-grand-final": 1898, "aflw": 2017, "nfl": 1920,
    "super-bowl": 1967, "ufl": 2024, "ifaf-world-championship": 1999,
    "nba": 1946, "wnba": 1997, "nbl": 1979, "premier-league": 1992, "mlb": 1876}
LIFECYCLE_EVIDENCE = "COVERAGE_AND_BLANK_YEARS.md (historical guidance; held seasons need independent completeness checks)"


def team_key(name: str) -> str:
    """Exact aliases only; Melbourne and North Melbourne are distinct clubs."""
    key = re.sub(r"\s+", " ", (name or "").strip().lower().replace("’", "'"))
    return ALIASES.get(key, MLB_ALIASES.get(key, key))


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def competition_id(name: str) -> str:
    return {"AFL": "afl", "AFLW": "aflw", "NFL": "nfl", "MLB": "mlb"}.get(name, slug(name))


def canonical_competition(name: str) -> str:
    return {"AFL Grand Final": "afl", "Super Bowl": "nfl", "College Football": "ncaa-division-i-fbs"}.get(name, competition_id(name))


def stage(value: str) -> str:
    text = value.lower()
    if "not applicable" in text:
        return "not_applicable"
    if any(token in text for token in ["pre-season", "preseason", "spring", "exhibition", "all-star"]):
        return "preseason_or_exhibition"
    if any(token in text for token in ["final", "playoff", "postseason", "bowl", "wild card", "series"]):
        return "finals"
    if "regular" in text:
        return "regular"
    return "unknown"


def parse_score(text: str) -> tuple[str, int, str, int] | None:
    """Parse two endpoint scores, preserving team ownership and valid zeros."""
    separator = r"(?:def(?:eated)?\.?(?:\s+by)?|drew(?:\s+with)?|drawn(?:\s+with)?|tied(?:\s+with)?)"
    afl = re.fullmatch(r"(.+?)\s+(\d+)\.(\d+)\s*\((\d+)\)\s+" + separator +
                       r"\s+(.+?)\s+(\d+)\.(\d+)\s*\((\d+)\)", text.strip(), re.I)
    if afl:
        a, _, _, score_a, b, _, _, score_b = afl.groups()
        return a.strip(), int(score_a), b.strip(), int(score_b)
    regular = re.fullmatch(r"(.+?)\s+(\d+)\s+" + separator + r"\s+(.+?)\s+(\d+)", text.strip(), re.I)
    if regular:
        a, score_a, b, score_b = regular.groups()
        return a.strip(), int(score_a), b.strip(), int(score_b)
    return None


def numeric(value: str) -> int | None:
    return int(value) if re.fullmatch(r"\d+", str(value or "").strip()) else None


def snapshot(path: Path, archive_root: Path = ARCHIVE_ROOT) -> str:
    """Preserve exact bytes before an authorized repair or implementation replacement."""
    data = path.read_bytes()
    digest = sha256(data)
    target = archive_root / "_custody" / "originals" / digest / path.name
    if not target.exists():
        atomic_bytes(target, data)
    relative = str(path.relative_to(archive_root.parent)).replace("\\", "/")
    index_path = archive_root / "_custody" / "originals_index.jsonl"
    existing = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    key = {"path": relative, "sha256": digest, "backup": str(target.relative_to(archive_root.parent)).replace("\\", "/"), "bytes": len(data)}
    if not any(json.loads(line).get("path") == relative and json.loads(line).get("sha256") == digest
               for line in existing.splitlines() if line):
        with index_path.open("a", encoding="utf-8", newline="") as handle:
            handle.write(json.dumps(key, ensure_ascii=False) + "\n")
    return digest


def yearly_files(archive_root: Path) -> list[Path]:
    """Use rg for inventory; ignore custody snapshots and generated canonical exports."""
    try:
        output = subprocess.run(["rg", "--files", "-g", "*_games.csv", str(archive_root)],
                                capture_output=True, text=True, check=True).stdout
        files = [Path(line) for line in output.splitlines()]
    except (FileNotFoundError, subprocess.CalledProcessError):
        files = list(archive_root.rglob("*_games.csv"))
    files = [p for p in files if p.parent.name.isdigit() and
             not any(part in {"_custody", "_canonical"} for part in p.relative_to(archive_root).parts)]
    def order(p):
        competition = p.parent.parent.name
        rank = 2 if competition in {"College Football", "Super Bowl", "AFL Grand Final"} else 0
        return rank, str(p.relative_to(archive_root))
    return sorted(files, key=order)


def normalize_row(raw: dict, sport: str, competition: str, season: str, origin: str, line: int,
                  origin_hash: str, evidence: EvidenceIndex | None = None) -> dict:
    comp = canonical_competition(competition)
    home = raw.get("Home Team", raw.get("Home", "")).strip()
    away = raw.get("Away Team", raw.get("Away", "")).strip()
    day = raw.get("Date", "").strip()
    reasons = []
    home_score, away_score = numeric(raw.get("Home Score")), numeric(raw.get("Away Score"))
    parsed = parse_score(raw.get("Game Score", raw.get("Match Score", "")))
    if home_score is None or away_score is None:
        if parsed:
            first, score_first, second, score_second = parsed
            scores = {team_key(first): score_first, team_key(second): score_second}
            if team_key(home) in scores and team_key(away) in scores and team_key(home) != team_key(away):
                home_score, away_score = scores[team_key(home)], scores[team_key(away)]
            else:
                reasons.append("score_team_identity_mismatch")
    if home_score is None or away_score is None:
        reasons.append("missing_numeric_team_scores")
    if not home or not away or team_key(home) == team_key(away):
        reasons.append("invalid_team_identity")
    try:
        date.fromisoformat(day)
    except ValueError:
        reasons.append("invalid_event_date")
    raw_type = next((str(v or "") for k, v in raw.items() if k and ("Type" in k or "Round" in k)), "")
    match_stage = stage(raw.get("Season Phase", raw_type))
    first = FIRST_SEASON.get(competition_id(competition))
    if first and int(season) < first:
        # Pre-founding exhibitions are retained but never treated as league-season data.
        reasons.append("competition_not_founded" if match_stage != "preseason_or_exhibition" else "pre_foundation_exhibition")
    if match_stage == "not_applicable":
        reasons.append("not_applicable_record")
    if match_stage in {"preseason_or_exhibition", "unknown"}:
        reasons.append("outside_regular_or_finals_training_contract")
    if home_score is not None and away_score is not None:
        declared_total = numeric(raw.get("Total Points", raw.get("Total Runs", "")))
        declared_margin = numeric(raw.get("Winning Margin", ""))
        if declared_total is not None and declared_total != home_score + away_score:
            reasons.append("total_score_disagreement")
        if declared_margin is not None and declared_margin != abs(home_score - away_score):
            reasons.append("winning_margin_disagreement")
    source_id = raw.get("Game ID (MLB gamePk)", "")
    match = None
    if evidence and home_score is not None and away_score is not None and "invalid_event_date" not in reasons:
        match = evidence.match(comp, day, home, away, home_score, away_score, source_id)
    if not match:
        reasons.append("missing_exact_result_source")
    elif comp == "mlb":
        # Stable league event ID owns team identity; preserve season-era names separately.
        if team_key(home) != team_key(match["home_team"]) or team_key(away) != team_key(match["away_team"]):
            reasons.append("source_team_identity_disagreement")
    if match and comp != "mlb":
        # The field-owner result determines designated ordering and era-correct names.
        home, away = match["home_team"], match["away_team"]
        home_score, away_score = int(match["home_score"]), int(match["away_score"])
    if competition in {"College Football", "NCAA Division I FBS"}:
        reasons.append("curated_incomplete_season")
    start = match.get("start_time_utc", "") if match else raw.get("Start Time (UTC)", "")
    if start:
        try:
            start = datetime.fromisoformat(start.replace("Z", "+00:00")).astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
        except ValueError:
            start = ""
            reasons.append("invalid_source_start_time")
    season_id = match.get("season_id", season) if match else season
    if competition == "Super Bowl" and day:
        season_id = str(int(day[:4]) - 1)
    source_event_id = match["source_event_id"] if match else source_id
    identity = [comp, day, team_key(home), team_key(away), home_score, away_score]
    event_id = comp + ":" + (str(source_event_id) if source_event_id else sha256(json.dumps(identity).encode())[:24])
    venue = match.get("venue", "") if match else raw.get("Venue", "")
    neutral = match.get("neutral_venue", "") if match else ""
    if not neutral and raw.get("Neutral or Alternate Site"):
        neutral = "true" if raw["Neutral or Alternate Site"] in {"Y", "Neutral"} else "unknown"
    result = "" if home_score is None or away_score is None else "home_win" if home_score > away_score else "away_win" if away_score > home_score else "draw"
    home_id = match.get("home_team_source_id", "") if match else ""
    away_id = match.get("away_team_source_id", "") if match else ""
    return dict(zip(EVENT_FIELDS, [event_id, sport, comp, str(season_id), day, start,
        "timestamp" if start else "date", comp + ":" + (home_id or slug(team_key(home))), home,
        comp + ":" + (away_id or slug(team_key(away))), away, home_score if home_score is not None else "",
        away_score if away_score is not None else "", home_score + away_score if home_score is not None and away_score is not None else "",
        home_score - away_score if home_score is not None and away_score is not None else "", result,
        "final_score_including_extra_innings" if comp == "mlb" else "final_score_including_overtime", "full_game", match_stage, venue, neutral, "",
        "historical_result_label_prior_dates_only;publication_time_unknown", match.get("retrieved_at_utc", "") if match else "",
        source_event_id, match.get("source_url", "") if match else "", match.get("source_receipt_path", "") if match else "",
        match.get("source_body_sha256", "") if match else "", "true" if match else "false",
        "verified_result" if match and not reasons else "excluded", "true" if match and not reasons else "false",
        "|".join(sorted(set(reasons))), origin, line, origin_hash, PARSER_VERSION, "",
        match.get("identity_repair_note", "") if match else "", match.get("source_parser_version", "") if match else ""]))


def _csv(path: Path, fields: list[str], rows) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def repair(archive_root: Path = ARCHIVE_ROOT) -> dict:
    """Apply only exact field-owner corrections and append a byte-custodied journal."""
    evidence = EvidenceIndex(archive_root, team_key).load()
    journal_path = archive_root / "_custody" / "corrections.jsonl"
    changed_files, changed_rows = 0, 0
    for path in yearly_files(archive_root):
        competition = path.parent.parent.name
        if competition not in {"AFL", "AFLW", "NFL", "College Football", "NCAA Division I FBS"}:
            continue
        before = path.read_bytes()
        reader = csv.DictReader(io.StringIO(before.decode("utf-8-sig"), newline=""))
        fields, rows = reader.fieldnames, list(reader)
        changes = []
        for row_number, row in enumerate(rows, 2):
            day = row.get("Date", "")
            parsed = parse_score(row.get("Game Score", ""))
            if not parsed:
                continue
            a, sa, b, sb = parsed
            comment_key = next((key for key in row if "comment" in key.lower()), "Game comment")
            match = evidence.match(canonical_competition(competition), day, a, b, sa, sb)
            update, reason = {}, ""
            if competition in {"College Football", "NCAA Division I FBS"} and day == "2025-08-23" and {team_key(a), team_key(b)} == {"iowa state", "kansas state"}:
                match = evidence.match("ncaa-division-i-fbs", day, "Iowa State", "Kansas State", 24, 21)
                if match:
                    update = {"Game Score": "Iowa State 24 def. Kansas State 21", "Total Points": "45", "Winning Margin": "3",
                        "Home": "Iowa State", "Away": "Kansas State", "Notable Players": "",
                        comment_key: "Iowa State defeated Kansas State 24-21 at Aviva Stadium in Dublin.",
                        next((k for k in row if "Game Type" in k), "Game Type"): "Regular Season"}
                    reason = "official_boxscore_corrects_winner_score_and_stage;unsupported_people_and_comment_quarantined"
            elif competition == "NFL" and day == "2025-09-05" and {team_key(a), team_key(b)} == {"los angeles chargers", "kansas city chiefs"} and match:
                update = {"Venue": match["venue"],
                    comment_key: "Los Angeles Chargers defeated Kansas City Chiefs 27-21 at Corinthians Arena in São Paulo, Brazil."}
                reason = "official_gamebook_corrects_neutral_venue"
            elif competition == "AFLW" and match:
                parsed_teams = {team_key(a), team_key(b)}
                home, away = row.get("Home", ""), row.get("Away", "")
                if {team_key(home), team_key(away)} != parsed_teams:
                    new_home, new_away = match["home_team"], match["away_team"]
                    if team_key(new_home) == "north melbourne":
                        new_home = "North Melbourne"
                    if team_key(new_away) == "north melbourne":
                        new_away = "North Melbourne"
                    update = {"Team A": new_home, "Team B": new_away, "Home": new_home, "Away": new_away,
                        "Notable Players": "", comment_key: ""}
                    # Only manually verified reports own historical venue names.
                    if match.get("verification_method") == "manual_primary_source_event_and_fields":
                        update["Venue"] = match["venue"]
                    reason = "official_result_corrects_team_alias;unsupported_people_and_comment_quarantined"
            elif competition == "AFL" and path.parent.name == "1905" and day in {"1905-06-03", "1905-06-05"}:
                # The retired builder transposed two dates within a mixed-date round.
                # Require that the retained table owns this exact pair and scores
                # on the opposite date; this is not a general fuzzy-date match.
                correct_day = "1905-06-03" if {team_key(a), team_key(b)} == {"melbourne", "fitzroy"} else "1905-06-05" if {team_key(a), team_key(b)} == {"st kilda", "essendon"} else ""
                corrected_match = evidence.match("afl", correct_day, a, b, sa, sb) if correct_day else None
                if corrected_match and day != correct_day:
                    match = corrected_match
                    update = {"Date": correct_day, "Notable Players": "", comment_key: ""}
                    reason = "retained_match_table_corrects_transposed_1905_round_date;unsupported_people_and_comment_quarantined"
            elif competition == "AFL" and match and match.get("identity_repair_note"):
                for field in ["Team A", "Team B", "Home", "Away"]:
                    if team_key(row.get(field, "")) == "brisbane lions":
                        update[field] = "Brisbane Bears"
                score = row.get("Game Score", "")
                for name in [a, b]:
                    if team_key(name) == "brisbane lions":
                        score = re.sub(r"(?<!\w)" + re.escape(name) + r"(?=\s+\d)", "Brisbane Bears", score, count=1)
                update.update({"Game Score": score, "Notable Players": "", comment_key: ""})
                reason = "retained_field_owner_result_restores_bears_identity;unsupported_people_and_comment_quarantined"
            update = {key: str(value) for key, value in update.items() if str(row.get(key, "")) != str(value)}
            if update:
                old = {key: row.get(key, "") for key in update}
                row.update(update)
                changes.append({"origin_row": row_number, "event_date": day, "old_fields": old, "new_fields": update,
                    "reason": reason, "source_url": match["source_url"], "source_receipt_path": match["source_receipt_path"],
                    "source_body_sha256": match["source_body_sha256"]})
        if changes:
            digest = snapshot(path, archive_root)
            buffer = io.StringIO(newline="")
            writer = csv.DictWriter(buffer, fieldnames=fields)
            writer.writeheader(); writer.writerows(rows)
            after = buffer.getvalue().encode("utf-8-sig" if before.startswith(b"\xef\xbb\xbf") else "utf-8")
            atomic_bytes(path, after)
            with journal_path.open("a", encoding="utf-8", newline="") as journal:
                for change in changes:
                    change.update({"origin_path": str(path.relative_to(archive_root.parent)).replace("\\", "/"),
                        "original_sha256": digest, "corrected_sha256": sha256(after), "parser_version": PARSER_VERSION,
                        "corrected_at_utc": datetime.now(timezone.utc).isoformat()})
                    journal.write(json.dumps(change, ensure_ascii=False) + "\n")
            changed_files += 1; changed_rows += len(changes)
    return {"changed_files": changed_files, "changed_rows": changed_rows, "journal": str(journal_path)}


def refresh_supported(archive_root: Path = ARCHIVE_ROOT, year: int = 2026) -> dict:
    """Append absent completed MLB results from retained official schedule evidence.

No boxscore, people, conditions or period statistics are filled without evidence.
Existing rows are preserved, and the complete original file is byte-custodied.
"""
    path = archive_root / "Baseball" / "MLB" / str(year) / f"{year}_games.csv"
    if not path.exists():
        raise EvidenceError("This refresh supports an existing MLB season input only")
    before = path.read_bytes()
    reader = csv.DictReader(io.StringIO(before.decode("utf-8-sig"), newline=""))
    fields, rows = reader.fieldnames, list(reader)
    required = {"Game Number", "Game ID (MLB gamePk)", "Season", "Season Phase", "Game Type", "Date",
        "Start Time (UTC)", "Home Team", "Away Team", "Venue", "Home Score", "Away Score", "Total Runs",
        "Winning Margin", "Winning Team", "Losing Team", "Result", "Game Score", "Primary Data Source",
        "Independent Check (Retrosheet or ESPN)", "Check Details"}
    if not fields or not required.issubset(fields):
        raise EvidenceError("MLB refresh input lacks the registered result/provenance schema")
    known = {row["Game ID (MLB gamePk)"] for row in rows}
    evidence = EvidenceIndex(archive_root, team_key).load()
    missing = [event for event in evidence.mlb.values() if event["source_year"] == str(year)
               and event["stage"] in {"R", "F", "D", "L", "W"} and event["source_event_id"] not in known]
    missing.sort(key=lambda event: (event["start_time_utc"], event["source_event_id"]))
    if not missing:
        return {"appended_results": 0, "year": year}
    additions = []
    for event in missing:
        hs, aws = int(event["home_score"]), int(event["away_score"])
        home, away = event["home_team"], event["away_team"]
        winner, loser = (home, away) if hs > aws else (away, home) if aws > hs else ("", "")
        score = f"{winner} {max(hs, aws)} def. {loser} {min(hs, aws)}" if winner else f"{home} {hs} tied with {away} {aws}"
        row = {field: "" for field in fields}
        row.update({"Game Number": str(len(rows) + len(additions) + 1), "Game ID (MLB gamePk)": event["source_event_id"],
            "Season": str(year), "Season Phase": "Regular Season" if event["stage"] == "R" else "Postseason",
            "Game Type": {"R": "Regular Season", "F": "Wild Card Series", "D": "Division Series", "L": "League Championship Series", "W": "World Series"}[event["stage"]],
            "Date": event["event_date"], "Start Time (UTC)": event["start_time_utc"], "Home Team": home, "Away Team": away,
            "Venue": event["venue"], "Home Score": str(hs), "Away Score": str(aws), "Total Runs": str(hs + aws),
            "Winning Margin": str(abs(hs - aws)), "Winning Team": winner, "Losing Team": loser,
            "Result": "Home Win" if hs > aws else "Away Win" if aws > hs else "Tie", "Game Score": score,
            "Primary Data Source": "MLB Stats API schedule", "Independent Check (Retrosheet or ESPN)": "Single source (retained official schedule; metadata incomplete)",
            "Check Details": "Appended missing completed result from " + event["source_url"] + "; source body SHA-256 " + event["source_body_sha256"]})
        additions.append(row)
    digest = snapshot(path, archive_root)
    rows.extend(additions)
    rows.sort(key=lambda row: (row["Start Time (UTC)"], row["Game ID (MLB gamePk)"]))
    for index, row in enumerate(rows, 1):
        row["Game Number"] = str(index)
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields)
    writer.writeheader(); writer.writerows(rows)
    after = buffer.getvalue().encode("utf-8-sig" if before.startswith(b"\xef\xbb\xbf") else "utf-8")
    atomic_bytes(path, after)
    with (archive_root / "_custody/corrections.jsonl").open("a", encoding="utf-8", newline="") as journal:
        for event, row in zip(missing, additions):
            journal.write(json.dumps({"origin_path": str(path.relative_to(archive_root.parent)).replace("\\", "/"),
                "original_sha256": digest, "corrected_sha256": sha256(after), "old_fields": {},
                "new_fields": {key: value for key, value in row.items() if value}, "reason": "append_missing_primary_completed_result;unsourced_metadata_left_blank",
                "source_url": event["source_url"], "source_receipt_path": event["source_receipt_path"],
                "source_body_sha256": event["source_body_sha256"], "parser_version": PARSER_VERSION,
                "corrected_at_utc": datetime.now(timezone.utc).isoformat()}, ensure_ascii=False) + "\n")
    return {"appended_results": len(additions), "year": year, "game_ids": [event["source_event_id"] for event in missing]}


def build(archive_root: Path = ARCHIVE_ROOT) -> dict:
    output = archive_root / "_canonical"
    output.mkdir(parents=True, exist_ok=True)
    evidence = EvidenceIndex(archive_root, team_key).load()
    expected_by_season = defaultdict(set)
    for source_event in evidence.mlb.values():
        if source_event.get("stage") in {"R", "F", "D", "L", "W"}:
            expected_by_season[("mlb", source_event["source_year"])].add(source_event["source_event_id"])
    for (comp, _), source_events in evidence.by_match.items():
        for source_event in source_events:
            if "afltables.com/afl/seas/" in source_event["source_url"] or "api.afl.com.au/" in source_event["source_url"]:
                source_year = source_event.get("source_year", source_event["event_date"][:4])
                expected_by_season[(comp, source_year)].add(source_event["source_event_id"])
    inputs = []
    events = {}
    narratives = []
    provenance = []
    seasons = []
    counters = Counter()
    for path in yearly_files(archive_root):
        data = path.read_bytes()
        digest = sha256(data)
        origin = str(path.relative_to(archive_root.parent)).replace("\\", "/")
        parts = path.relative_to(archive_root).parts
        sport, competition, season = parts[0], path.parent.parent.name, path.parent.name
        inputs.append({"path": origin, "sha256": digest, "bytes": len(data)})
        reader = csv.DictReader(io.StringIO(data.decode("utf-8-sig"), newline=""))
        counts = Counter()
        matched_source_ids = set()
        previous_line = 1
        for raw in reader:
            origin_line = previous_line + 1
            previous_line = reader.line_num
            counters["raw_rows"] += 1
            counts["rows"] += 1
            row = normalize_row(raw, sport, competition, season, origin, origin_line, digest, evidence)
            if row["source_verified"] == "true" and row["stage"] in {"regular", "finals"}:
                matched_source_ids.add(str(row["source_event_id"]))
            event_id = row["event_id"]
            reason = ""
            if competition == "College Football":
                reason = "mirrored_collection"
            elif competition in {"AFL Grand Final", "Super Bowl"}:
                reason = "subset_collection"
            elif event_id in events:
                reason = "duplicate_event"
            if reason:
                counters[reason] += 1
                counts["excluded_rows"] += 1
                # Keep traceability for subset-only games without making them training rows.
                if event_id not in events:
                    row["training_eligible"] = "false"
                    row["quality_status"] = "excluded"
                    row["exclusion_reasons"] = "|".join(filter(None, [row["exclusion_reasons"], reason]))
                    events[event_id] = row
            else:
                events[event_id] = row
                counts["unique_events"] += 1
                counts["verified_results"] += row["source_verified"] == "true"
                counts["training_eligible"] += row["training_eligible"] == "true"
                counts["excluded_rows"] += row["training_eligible"] != "true"
            provenance.append(dict(zip(PROVENANCE_FIELDS, [event_id, origin, origin_line, digest,
                "excluded" if reason or row["training_eligible"] != "true" else "historical_result_label",
                reason or row["exclusion_reasons"], event_id if reason else ""])))
            comment = next((str(v or "") for k, v in raw.items() if k and ("comment" in k.lower() or k == "Game Summary")), "")
            if raw.get("Notable Players") or comment:
                narratives.append(dict(zip(NARRATIVE_FIELDS, [event_id, origin, origin_line, raw.get("Notable Players", ""),
                    comment, "postgame_or_unspecified", "false", "false", "narrative_awards_and_participation_unverified_for_pregame"])))
        counters["yearly_files"] += 1
        counters["header_only_files"] += not bool(counts["rows"])
        name_id = competition_id(competition)
        founded = FIRST_SEASON.get(name_id)
        lifecycle = "not_founded" if founded and int(season) < founded else "competition_exists_edition_unverified" if founded else "unknown"
        if name_id == "afl-grand-final" and season == "1924":
            lifecycle = "not_held"
        coverage = "not_founded" if lifecycle == "not_founded" and not counts["rows"] else "not_held" if lifecycle == "not_held" else "data_unavailable_lifecycle_unknown" if not counts["rows"] else "partial_unverified"
        if competition in {"College Football", "NCAA Division I FBS"} and counts["rows"]:
            coverage = "curated_subset"
        expected = expected_by_season.get((name_id, season), set())
        missing = expected - matched_source_ids
        matched_count = len(expected & matched_source_ids)
        if expected and not missing and int(season) < 2026:
            coverage = "complete_verified_result_scope"
        elif expected:
            coverage = "partial_source_scope" if missing else "live_season_snapshot_only"
        season_record = dict(zip(SEASON_FIELDS, [sport, competition, name_id, season, origin, digest,
            counts["rows"], counts["unique_events"], counts["verified_results"], counts["training_eligible"], coverage, lifecycle,
            LIFECYCLE_EVIDENCE if founded else "no independently verified season lifecycle registered",
            counts["excluded_rows"], "source_or_completeness_not_verified" if coverage in {"partial_unverified", "data_unavailable_lifecycle_unknown", "curated_subset", "partial_source_scope"} else "",
            len(expected) if expected else "", matched_count if expected else "", len(missing) if expected else "",
            counts["rows"] - counts["verified_results"],
            "completed_regular_and_finals_results_in_retained_source_snapshot;excludes_exhibitions" if expected else "no_complete_source_population_registered"]))
        seasons.append(season_record)
    # Immutable input snapshot identity is independent of build/retrieval wall time.
    inputs.sort(key=lambda item: item["path"])
    snapshot_hash = sha256(json.dumps(inputs, sort_keys=True, separators=(",", ":")).encode())
    ordered_events = sorted(events.values(), key=lambda row: (row["competition_id"], row["event_date"], row["event_id"]))
    for row in ordered_events:
        row["data_snapshot_hash"] = snapshot_hash
    counters["canonical_events"] = len(ordered_events)
    counters["verified_results"] = sum(row["source_verified"] == "true" for row in ordered_events)
    counters["training_eligible"] = sum(row["training_eligible"] == "true" for row in ordered_events)
    counters["narratives_excluded_from_pregame"] = len(narratives)
    counters["source_receipt_errors"] = len(evidence.errors)
    manifest = {"schema_version": PARSER_VERSION, "mode": "SPORTS_ONLY / MARKET_BLIND",
        "data_snapshot_hash": snapshot_hash, "counts": dict(counters), "inputs": inputs,
        "receipts": evidence.receipts_used, "source_errors": evidence.errors,
        "training_contract": "verified full-game result labels only; features use strictly earlier event dates; no narrative, awards or actual same-game statistics",
        "historical_available_at": "unknown; retrieved_at never means pregame publication",
        "coverage_claim": "partial; completed result-scope matches do not prove all metadata, all phases or live-season completion",
        "implementation_hashes": {str(p.relative_to(ROOT)).replace("\\", "/"): sha256(p.read_bytes()) for p in [Path(__file__), Path(__file__).with_name("archive_sources.py")]}}
    all_custody = audit_receipts(archive_root)
    if all_custody["errors"]:
        raise EvidenceError("Archive has corrupt source custody; previous exports preserved")
    manifest["all_source_custody"] = all_custody
    auxiliary = [archive_root / "_football_research/afl_api.json", archive_root / "_custody/verified_facts.json",
                 archive_root / "_custody/originals_index.jsonl", archive_root / "_custody/corrections.jsonl"]
    manifest["transformation_inputs"] = {str(p.relative_to(archive_root.parent)).replace("\\", "/"): sha256(p.read_bytes()) for p in auxiliary if p.exists()}
    # Publish each complete file, then a manifest commit marker. Readers must verify hashes.
    with tempfile.TemporaryDirectory(prefix="archive-build-", dir=output) as temp:
        stage_dir = Path(temp)
        _csv(stage_dir / "events.csv", EVENT_FIELDS, ordered_events)
        _csv(stage_dir / "narratives.csv", NARRATIVE_FIELDS, narratives)
        _csv(stage_dir / "provenance.csv", PROVENANCE_FIELDS, provenance)
        _csv(stage_dir / "seasons.csv", SEASON_FIELDS, seasons)
        manifest["outputs"] = {name: {"sha256": sha256((stage_dir / name).read_bytes()), "bytes": (stage_dir / name).stat().st_size}
                               for name in ["events.csv", "narratives.csv", "provenance.csv", "seasons.csv"]}
        atomic_bytes(stage_dir / "manifest.json", (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode())
        for name in ["events.csv", "narratives.csv", "provenance.csv", "seasons.csv", "manifest.json"]:
            os.replace(stage_dir / name, output / name)
    return manifest


def read_events(path: Path | None = None, eligible_only: bool = True, verify: bool = True) -> list[dict]:
    path = Path(path or ARCHIVE_ROOT / "_canonical" / "events.csv")
    data = path.read_bytes()
    if verify:
        manifest = json.loads((path.parent / "manifest.json").read_text(encoding="utf-8"))
        expected = manifest["outputs"][path.name]["sha256"]
        if sha256(data) != expected:
            raise EvidenceError("Canonical export does not match the committed manifest")
    rows = list(csv.DictReader(io.StringIO(data.decode("utf-8"), newline="")))
    return [row for row in rows if row["training_eligible"] == "true"] if eligible_only else rows


def validate(archive_root: Path = ARCHIVE_ROOT) -> dict:
    output = archive_root / "_canonical"
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    issues = []
    for relative, digest in manifest.get("implementation_hashes", {}).items():
        if sha256((ROOT / relative).read_bytes()) != digest:
            issues.append("implementation_hash_mismatch:" + relative)
    for relative, digest in manifest.get("transformation_inputs", {}).items():
        if sha256((archive_root.parent / relative).read_bytes()) != digest:
            issues.append("transformation_input_hash_mismatch:" + relative)
    custody_index = archive_root / "_custody/originals_index.jsonl"
    original_count = 0
    if custody_index.exists():
        for line in custody_index.read_text(encoding="utf-8").splitlines():
            item = json.loads(line)
            original_count += 1
            backup = archive_root.parent / item["backup"]
            if not backup.exists() or sha256(backup.read_bytes()) != item["sha256"]:
                issues.append("original_backup_hash_mismatch:" + item["path"])
    for item in manifest["inputs"]:
        path = archive_root.parent / item["path"]
        if not path.is_file() or sha256(path.read_bytes()) != item["sha256"]:
            issues.append("input_hash_mismatch:" + item["path"])
    for name, receipt in manifest["outputs"].items():
        if sha256((output / name).read_bytes()) != receipt["sha256"]:
            issues.append("output_hash_mismatch:" + name)
    rows = read_events(output / "events.csv", eligible_only=False)
    ids = Counter(row["event_id"] for row in rows)
    issues.extend("duplicate_event_id:" + event_id for event_id, count in ids.items() if count > 1)
    for row in rows:
        if row["home_score"] and row["away_score"]:
            hs, aws = int(row["home_score"]), int(row["away_score"])
            if int(row["total_score"]) != hs + aws or int(row["margin_signed_home"]) != hs - aws:
                issues.append("arithmetic:" + row["event_id"])
        if row["training_eligible"] == "true":
            if row["source_verified"] != "true" or row["exclusion_reasons"] or not row["source_receipt_path"]:
                issues.append("invalid_training_admission:" + row["event_id"])
    for path, digest in manifest["receipts"].items():
        receipt, _ = read_receipt(archive_root.parent / path)
        if receipt["stored_sha256"] != digest:
            issues.append("receipt_hash_mismatch:" + path)
    receipt_audit = audit_receipts(archive_root)
    issues.extend("source_custody_error:" + item["receipt"] for item in receipt_audit["errors"])
    if receipt_audit["receipts"] != manifest.get("all_source_custody", {}).get("receipts", {}):
        issues.append("all_source_custody_snapshot_changed")
    audit_summary = {key: value for key, value in receipt_audit.items() if key != "receipts"}
    return {"valid": not issues, "issues": issues, "counts": manifest["counts"], "data_snapshot_hash": manifest["data_snapshot_hash"],
        "used_receipt_count": len(manifest["receipts"]), "all_source_receipts": audit_summary, "original_backups_checked": original_count,
        "input_files_checked": len(manifest["inputs"]), "implementation_files_checked": len(manifest.get("implementation_hashes", {}))}


def inventory(archive_root: Path = ARCHIVE_ROOT) -> dict:
    """Measure actual raw files independently of the canonical manifest or source claims."""
    totals = Counter()
    competitions = defaultdict(Counter)
    inputs = []
    for path in yearly_files(archive_root):
        body = path.read_bytes()
        reader = csv.DictReader(io.StringIO(body.decode("utf-8-sig"), newline=""))
        count = sum(1 for _ in reader)
        key = "/".join(path.relative_to(archive_root).parts[:-2])
        counts = competitions[key]
        for aggregate in [totals, counts]:
            aggregate["files"] += 1
            aggregate["rows"] += count
            aggregate["header_only"] += count == 0
            aggregate["populated_files"] += count > 0
        inputs.append({"path": str(path.relative_to(archive_root.parent)).replace("\\", "/"), "sha256": sha256(body), "bytes": len(body)})
    inputs.sort(key=lambda item: item["path"])
    digest = sha256(json.dumps(inputs, sort_keys=True, separators=(",", ":")).encode())
    manifest_path = archive_root / "_canonical/manifest.json"
    stored = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    return {"counts": dict(totals), "competitions": {key: dict(value) for key, value in sorted(competitions.items())},
        "data_snapshot_hash": digest, "canonical_input_snapshot_current": digest == stored.get("data_snapshot_hash"),
        "count_limit": "raw rows include mirrors, subsets, duplicate and not-applicable records"}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["build", "validate", "inventory", "repair", "refresh-supported"])
    parser.add_argument("--archive-root", type=Path, default=ARCHIVE_ROOT)
    args = parser.parse_args(argv)
    if args.command == "repair":
        print(json.dumps(repair(args.archive_root), indent=2))
        return 0
    if args.command == "refresh-supported":
        print(json.dumps(refresh_supported(args.archive_root), indent=2))
        return 0
    if args.command == "inventory":
        print(json.dumps(inventory(args.archive_root), indent=2))
        return 0
    if args.command == "build":
        manifest = build(args.archive_root)
        print(json.dumps({"counts": manifest["counts"], "data_snapshot_hash": manifest["data_snapshot_hash"]}, indent=2))
        return 0
    result = validate(args.archive_root)
    atomic_bytes(args.archive_root / "_canonical/validation.json", (json.dumps(result, indent=2) + "\n").encode())
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
