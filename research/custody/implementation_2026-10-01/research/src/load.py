"""EPL result ingestion and second-publisher score cross-check.

Forecast code reads only processed score data. Football-Data source CSVs contain
odds and are quarantined under data/benchmark; this builder reads only five
score/identity columns after the season is terminal. No odds are copied out.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OPENFOOTBALL = ROOT / "data" / "raw" / "openfootball"
BENCHMARK = ROOT / "data" / "benchmark" / "football_data"
PROCESSED = ROOT / "data" / "processed"
SEASONS = [f"{y}-{str(y+1)[-2:]}" for y in range(2020, 2026)]
SOURCE_URL = "https://raw.githubusercontent.com/openfootball/england/master/{season}/1-premierleague.txt"
CHECK_URL = "https://www.football-data.co.uk/mmz4281/{yy}/E0.csv"

ALIASES = {
    "AFC Bournemouth": "Bournemouth", "Bournemouth": "Bournemouth",
    "Brighton & Hove Albion": "Brighton", "Brighton and Hove Albion": "Brighton",
    "Chelsea": "Chelsea", "Manchester City": "Man City",
    "Manchester United": "Man United", "Newcastle United": "Newcastle",
    "Nottingham Forest": "Nott'm Forest", "Tottenham Hotspur": "Tottenham",
    "West Ham United": "West Ham", "Wolverhampton Wanderers": "Wolves",
    "Leicester City": "Leicester", "Leeds United": "Leeds",
    "West Bromwich Albion": "West Brom", "Sheffield United": "Sheffield United",
    "Ipswich Town": "Ipswich", "Luton Town": "Luton",
    "Norwich City": "Norwich", "Cardiff City": "Cardiff",
    "Stoke City": "Stoke", "Swansea City": "Swansea",
    "Hull City": "Hull", "Huddersfield Town": "Huddersfield",
    "Hull City AFC": "Hull", "Coventry City": "Coventry", "Sunderland AFC": "Sunderland",
}
DATE_RE = re.compile(r"^(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+([A-Z][a-z]{2})\s+(\d{1,2})(?:\s+(\d{4}))?$", re.I)
MATCH_RE = re.compile(r"^\s*(?:(\d{1,2}:\d{2})\s+)?(.+?)\s+(\d+)-(\d+)(?:\s+\(\d+-\d+\))?\s+(.+?)\s*$")
V_MATCH_RE = re.compile(r"^\s*(?:(\d{1,2}:\d{2})\s+)?(.+?)\s+v\s+(.+?)\s+(\d+)-(\d+)(?:\s+\(\d+-\d+\))?\s*$")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def team(name: str) -> str:
    cleaned = re.sub(r"\s+FC$", "", name.strip())
    return ALIASES.get(cleaned, cleaned)


def parse_openfootball(path: Path, expected: int | None = 380) -> pd.DataFrame:
    start_year = int(path.stem[:4])
    current_date = None
    current_clock = None
    round_no = None
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if "Matchday " in line or "Regular Season - " in line:
            round_match = re.search(r"(?:Matchday|Regular Season - )\s*(\d+)", line)
            if round_match:
                round_no = int(round_match.group(1))
        date_match = DATE_RE.match(line.strip())
        if date_match:
            month, day, explicit_year = date_match.groups()
            month_no = datetime.strptime(month, "%b").month
            year = int(explicit_year) if explicit_year else start_year + (month_no < 7)
            current_date = datetime.strptime(f"{year}-{month_no:02}-{int(day):02}", "%Y-%m-%d").date()
            current_clock = None
            continue
        v_match = V_MATCH_RE.match(line)
        match = MATCH_RE.match(line) if not v_match else None
        if not v_match and not match:
            continue
        if current_date is None or round_no is None:
            raise ValueError(f"fixture has no date/round: {path}:{line_no}")
        if v_match:
            clock, home, away, hg, ag = v_match.groups()
        else:
            clock, home, hg, ag, away = match.groups()
        clock = clock or current_clock
        if clock is None:
            raise ValueError(f"fixture has no clock: {path}:{line_no}")
        current_clock = clock
        kickoff = datetime.fromisoformat(f"{current_date}T{clock}:00+00:00")
        rows.append(dict(season=path.stem, round=round_no, kickoff_utc=kickoff,
                         home=team(home), away=team(away), hg=int(hg), ag=int(ag),
                         source_line=line_no))
    df = pd.DataFrame(rows)
    if expected is not None and len(df) != expected:
        raise ValueError(f"{path.name}: expected {expected} matches, parsed {len(df)}")
    return df


def crosscheck(df: pd.DataFrame, path: Path) -> dict:
    london = ZoneInfo("Europe/London")
    def scheduled_utc(row: dict[str, str]) -> datetime:
        date = pd.to_datetime(row["Date"], dayfirst=True).date()
        clock = row.get("Time") or "12:00"
        return datetime.fromisoformat(f"{date}T{clock}:00").replace(tzinfo=london).astimezone(timezone.utc)
    with path.open(newline="", encoding="utf-8-sig", errors="replace") as f:
        reader = csv.DictReader(f)
        rows = [dict(home=team(r["HomeTeam"]), away=team(r["AwayTeam"]),
                     hg=int(r["FTHG"]), ag=int(r["FTAG"]),
                     kickoff_utc=scheduled_utc(r), time_status=("EXACT" if r.get("Time") else "DATE_ONLY"))
                for r in reader if r.get("FTHG") and r.get("FTAG")]
    if len(rows) != 380:
        raise ValueError(f"{path.name}: cross-check has {len(rows)} final matches")
    primary = {(r.home, r.away): (int(r.hg), int(r.ag)) for r in df.itertuples()}
    secondary = {(r["home"], r["away"]): (r["hg"], r["ag"]) for r in rows}
    if len(primary) != 380 or len(secondary) != 380:
        raise ValueError("duplicate fixture")
    if primary != secondary:
        missing = list(primary.keys() - secondary.keys())[:10]
        extra = list(secondary.keys() - primary.keys())[:10]
        scores = [(k, primary[k], secondary[k]) for k in primary.keys() & secondary.keys()
                  if primary[k] != secondary[k]][:10]
        raise ValueError(f"score cross-check failed: missing={missing}, extra={extra}, scores={scores}")
    teams = set(df.home) | set(df.away)
    if len(teams) != 20:
        raise ValueError(f"{path.name}: {len(teams)} teams")
    secondary_dates = {(r["home"], r["away"]): r["kickoff_utc"].date() for r in rows}
    date_differences = [(r.home, r.away) for r in df.itertuples()
                        if r.kickoff_utc.date() != secondary_dates[(r.home, r.away)]]
    if date_differences:
        raise ValueError(f"date cross-check failed: {date_differences[:10]}")
    schedule = {(r["home"], r["away"]): r for r in rows}
    df["kickoff_utc"] = [schedule[(r.home, r.away)]["kickoff_utc"] for r in df.itertuples()]
    df["kickoff_precision"] = [schedule[(r.home, r.away)]["time_status"] for r in df.itertuples()]
    return dict(matches=len(df), teams=sorted(teams), score_disagreements=0,
                date_disagreements=0, date_only_events=sum(r["time_status"] == "DATE_ONLY" for r in rows),
                openfootball_sha256=sha(OPENFOOTBALL / path.with_suffix(".txt").name),
                football_data_sha256=sha(path))


def build() -> dict:
    frames, checks = [], {}
    for season in SEASONS:
        source = OPENFOOTBALL / f"{season}.txt"
        check = BENCHMARK / f"{season}.csv"
        if not source.exists() or not check.exists():
            raise FileNotFoundError(f"missing score source for {season}")
        frame = parse_openfootball(source)
        checks[season] = crosscheck(frame, check)
        frames.append(frame)
    all_matches = pd.concat(frames, ignore_index=True).sort_values("kickoff_utc").reset_index(drop=True)
    if all_matches.duplicated(["season", "home", "away"]).any():
        raise ValueError("duplicate fixture across processed seasons")
    PROCESSED.mkdir(parents=True, exist_ok=True)
    output = PROCESSED / "matches.parquet"
    all_matches.to_parquet(output, index=False)
    manifest = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                    seasons=checks, matches=len(all_matches),
                    matches_parquet_sha256=sha(output),
                    forecast_input_columns=list(all_matches.columns),
                    crosscheck_source_is_benchmark_only=True)
    (PROCESSED / "data_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


if __name__ == "__main__":
    print(json.dumps(build(), indent=2))
