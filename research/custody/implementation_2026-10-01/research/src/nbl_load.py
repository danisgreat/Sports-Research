"""Official NBL regular-season results, checked against independent scores.

FixtureDownload snapshots are local-only under data/benchmark because the
publisher restricts redistribution. ESPN is retained as a diagnostic lineage;
its missing NBL22 coverage and erroneous scores are never training labels.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

import pandas as pd

from .load import ROOT, sha

OFFICIAL = ROOT / "data/raw/nbl_official"
ESPN = ROOT / "data/benchmark/nbl_espn"
FIXTURES = ROOT / "data/benchmark/nbl_fixturedownload"
PROCESSED = ROOT / "data/processed"
SEASONS = range(2021, 2026)
CODE_MAP = {"HWK": "ILL", "PNX": "SEM"}
TEAM_NAMES = {
    "Adelaide 36ers": "ADL", "Brisbane Bullets": "BRI",
    "Cairns Taipans": "CNS", "Illawarra Hawks": "ILL",
    "Melbourne United": "MEL", "New Zealand Breakers": "NZL",
    "Perth Wildcats": "PER", "South East Melbourne Phoenix": "SEM",
    "Sydney Kings": "SYD", "Tasmania JackJumpers": "TAS",
}
# An independent club or league report resolves each FixtureDownload error.
# Exact season, event, teams, date and scores are checked before applying it.
ADJUDICATIONS = {
    ("NBL23", "CNS", "PER", "2022-10-10"): {
        "official": [76, 105], "fixtures": [76, 103],
        "source_url": "https://www.wildcats.com.au/news/wildcats-with-a-record-breaking-night-in-cairns",
        "source_name": "Perth Wildcats game report",
    },
    ("NBL26", "SYD", "TAS", "2026-01-22"): {
        "official": [105, 94], "fixtures": [103, 94],
        "source_url": "https://www.nbl.com.au/news/kings-take-care-of-wounded-jackjumpers",
        "source_name": "NBL game report",
    },
}


def _get(url: str, path: Path) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as response:
            path.write_bytes(response.read())
    return json.loads(path.read_text(encoding="utf-8"))


def fixture_index(year: int) -> tuple[dict, dict]:
    """Read the local secondary snapshot at exact match grain.

    Unscored cancelled fixtures are excluded; duplicate keys or unknown team
    names block the build instead of silently choosing a row.
    """
    url = f"https://fixturedownload.com/feed/json/nbl-{year}"
    path = FIXTURES / f"nbl{str(year+1)[-2:]}.json"
    rows = _get(url, path)
    if not isinstance(rows, list):
        raise ValueError(f"bad FixtureDownload schema for {year}")
    indexed = {}
    cancelled = 0
    for row in rows:
        if row.get("HomeTeamScore") is None or row.get("AwayTeamScore") is None:
            cancelled += 1
            continue
        try:
            home, away = TEAM_NAMES[row["HomeTeam"]], TEAM_NAMES[row["AwayTeam"]]
            kickoff = datetime.fromisoformat(row["DateUtc"].replace(" ", "T").replace("Z", "+00:00"))
            score = [int(row["HomeTeamScore"]), int(row["AwayTeamScore"])]
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"bad FixtureDownload row for {year}") from exc
        if kickoff.utcoffset() is None or min(score) < 0:
            raise ValueError(f"invalid FixtureDownload time or score for {year}")
        key = (kickoff, home, away)
        if key in indexed:
            raise ValueError(f"duplicate FixtureDownload match {key}")
        indexed[key] = score
    return indexed, dict(url=url, sha256=sha(path), scored=len(indexed), unscored=cancelled)


def build() -> dict:
    rows = []
    sources = {}
    secondary = {}
    fixture_conflicts = []
    adjudicated = []
    seen_adjudications = set()
    for year in SEASONS:
        url = f"https://schedule.nbl.com.au/api/calendar/schedule?league=NBL&limit=500&offset=0&year={year}"
        path = OFFICIAL / f"nbl{str(year+1)[-2:]}.json"
        obj = _get(url, path)
        fixture_rows, fixture_receipt = fixture_index(year)
        secondary[f"NBL{str(year+1)[-2:]}"] = fixture_receipt
        if obj.get("total") != len(obj.get("matches", [])):
            raise ValueError(f"official NBL schedule pagination needed for {year}")
        count = 0
        used_fixture_keys = set()
        for match in obj["matches"]:
            if match.get("season_type") != "regular" or not re.fullmatch(r"\d+", str(match.get("round_label"))):
                continue
            if match.get("phase") != "complete" or match.get("home_score") is None or match.get("away_score") is None:
                raise ValueError(f"incomplete historical NBL match {match['id']}")
            season = f"NBL{str(year+1)[-2:]}"
            kickoff = datetime.fromtimestamp(match["starts_at_ms"]/1000, timezone.utc)
            home, away = match["home"]["team_code"], match["away"]["team_code"]
            official_score = [int(match["home_score"]), int(match["away_score"])]
            key = (kickoff, home, away)
            checked_score = fixture_rows.get(key)
            if checked_score is not None:
                used_fixture_keys.add(key)
            status = "SECOND_SOURCE_AGREE"
            if checked_score != official_score:
                exception = dict(event_id=match["id"], season=season,
                                 kickoff_utc=kickoff.isoformat(), home=home, away=away,
                                 official=official_score, fixtures=checked_score)
                if checked_score is None:
                    fixture_conflicts.append(exception)
                    status = "UNRESOLVED"
                else:
                    adjudication_key = (season, home, away, kickoff.date().isoformat())
                    adjudication = ADJUDICATIONS.get(adjudication_key)
                    if (adjudication is None or adjudication["official"] != official_score
                            or adjudication["fixtures"] != checked_score):
                        fixture_conflicts.append(exception)
                        status = "UNRESOLVED"
                    else:
                        seen_adjudications.add(adjudication_key)
                        adjudicated.append({**exception, **adjudication})
                        status = "ADJUDICATED_OFFICIAL"
            rows.append(dict(season=season, event_id=match["id"], kickoff_utc=kickoff,
                             round=int(match["round_label"]), home=home, away=away,
                             hg=official_score[0], ag=official_score[1],
                             source_url=f"https://schedule.nbl.com.au/match?league=NBL&match={match['id']}",
                             score_validation_status=status,
                             second_source_url=fixture_receipt["url"]))
            count += 1
        extra = set(fixture_rows) - used_fixture_keys
        if extra:
            fixture_conflicts.extend(dict(season=f"NBL{str(year+1)[-2:]}",
                                          reason="extra scored FixtureDownload event",
                                          kickoff_utc=k[0].isoformat(), home=k[1], away=k[2],
                                          fixtures=fixture_rows[k]) for k in sorted(extra))
        sources[f"NBL{str(year+1)[-2:]}"] = dict(official_url=url, sha256=sha(path), matches=count)
    if seen_adjudications != set(ADJUDICATIONS):
        raise ValueError("stale NBL adjudication; recheck exception list")
    df = pd.DataFrame(rows).sort_values("kickoff_utc").reset_index(drop=True)
    if df.event_id.duplicated().any() or (df.hg < 0).any() or (df.ag < 0).any():
        raise ValueError("duplicate official event or negative score")
    # ESPN is a second result lineage. The raw responses may include odds and
    # stay in benchmark quarantine. Only scores/identity below are compared.
    checks = {}
    for calendar_year in range(2021, 2027):
        url = f"https://site.api.espn.com/apis/site/v2/sports/basketball/nbl/scoreboard?dates={calendar_year}&limit=500"
        path = ESPN / f"{calendar_year}.json"
        obj = _get(url, path)
        checks[str(calendar_year)] = sha(path)
    espn = []
    for calendar_year in range(2021, 2027):
        obj = json.loads((ESPN / f"{calendar_year}.json").read_text(encoding="utf-8"))
        for event in obj.get("events", []):
            competition = event["competitions"][0]
            if not competition["status"]["type"].get("completed"):
                continue
            opponents = {c["homeAway"]: c for c in competition["competitors"]}
            if set(opponents) != {"home", "away"}:
                continue
            def code(which):
                return CODE_MAP.get(opponents[which]["team"]["abbreviation"], opponents[which]["team"]["abbreviation"])
            espn.append(dict(date=pd.Timestamp(event["date"]).date(), home=code("home"), away=code("away"),
                             hg=int(float(opponents["home"]["score"])),
                             ag=int(float(opponents["away"]["score"]))))
    mismatches = []
    matched = 0
    for game in df.itertuples():
        candidates = [x for x in espn if x["home"] == game.home and x["away"] == game.away
                      and abs((x["date"]-game.kickoff_utc.date()).days) <= 1]
        if len(candidates) != 1 or (candidates[0]["hg"], candidates[0]["ag"]) != (game.hg,game.ag):
            mismatches.append(dict(event_id=game.event_id, season=game.season, home=game.home,
                                   away=game.away, official=[game.hg,game.ag], espn=candidates))
        else:
            matched += 1
    source_manifest = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                           official_seasons=sources, fixture_response_hashes=secondary,
                           espn_response_hashes=checks, regular_season_games=len(df),
                           fixture_agree=int((df.score_validation_status == "SECOND_SOURCE_AGREE").sum()),
                           fixture_adjudicated=len(adjudicated),
                           fixture_unresolved=len(fixture_conflicts),
                           espn_agree=matched,
                           espn_missing=sum(not r["espn"] for r in mismatches),
                           espn_score_conflicts=sum(len(r["espn"]) == 1 for r in mismatches),
                           status="BLOCKED" if fixture_conflicts else "CROSSCHECK_PASS_WITH_ADJUDICATIONS")
    (PROCESSED / "nbl_source_manifest.json").write_text(json.dumps(source_manifest,indent=2)+"\n",encoding="utf-8")
    (PROCESSED / "nbl_crosscheck_disagreements.json").write_text(json.dumps(mismatches, indent=2, default=str)+"\n", encoding="utf-8")
    (PROCESSED / "nbl_fixture_adjudications.json").write_text(json.dumps(adjudicated, indent=2)+"\n", encoding="utf-8")
    (PROCESSED / "nbl_fixture_unresolved.json").write_text(json.dumps(fixture_conflicts, indent=2)+"\n", encoding="utf-8")
    if fixture_conflicts:
        raise ValueError(f"NBL independent cross-check failed on {len(fixture_conflicts)} games")
    path = PROCESSED / "nbl_matches.parquet"
    df.to_parquet(path, index=False)
    manifest = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                    seasons=sources, fixture_response_hashes=secondary,
                    games=len(df), second_source_agree=source_manifest["fixture_agree"],
                    adjudicated=len(adjudicated), unresolved=0, parquet_sha256=sha(path),
                    forecast_input_columns=list(df.columns))
    (PROCESSED / "nbl_data_manifest.json").write_text(json.dumps(manifest, indent=2)+"\n", encoding="utf-8")
    return manifest


if __name__ == "__main__":
    print(json.dumps(build(), indent=2))
