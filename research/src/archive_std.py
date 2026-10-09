"""Standard per-sport event schema over the raw yearly archive (SRC-05).

The raw `Previous Sports Results/<sport>/<competition>/<year>/<year>_games.csv` files are
heterogeneous: some carry numeric home/away scores, overtime flags and line scores, others
only a score string. This module is a read-only adapter that maps each row onto one
`StdEvent` and records, for every row it cannot map, the reason. It never edits an archive
file, never reads odds or markets, and a row is accepted only when its declared totals and
margins agree with the scores it extracted.

  python -B -m research.src.archive_std coverage [--out DIR]    coverage report by competition/season
  python -B -m research.src.archive_std build --out DIR          one standard CSV per sport

`archive.py` remains the conservative canonical admission path (field-owner receipts); this
module is the broader modelling view used for league priors and the H0 training table.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Iterator, Optional

try:
    from .archive import parse_score, stage as stage_of, team_key
except ImportError:  # direct execution from research/src
    from archive import parse_score, stage as stage_of, team_key  # type: ignore

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE_ROOT = ROOT / "Previous Sports Results"

STD_FIELDS = [
    "sport", "competition", "season_year", "date", "stage", "home", "away", "home_score", "away_score",
    "overtime", "shootout", "innings", "extra_innings", "home_periods", "away_periods",
    "home_halftime", "away_halftime", "home_tries", "away_tries", "home_goals", "away_goals",
    "home_behinds", "away_behinds", "venue", "score_source", "origin_path", "origin_line",
]


@dataclass
class StdEvent:
    sport: str
    competition: str
    season_year: int
    date: str
    stage: str
    home: str
    away: str
    home_score: int
    away_score: int
    overtime: Optional[bool] = None
    shootout: Optional[bool] = None
    innings: Optional[int] = None
    extra_innings: Optional[bool] = None
    home_periods: Optional[str] = None
    away_periods: Optional[str] = None
    home_halftime: Optional[int] = None
    away_halftime: Optional[int] = None
    home_tries: Optional[int] = None
    away_tries: Optional[int] = None
    home_goals: Optional[int] = None
    away_goals: Optional[int] = None
    home_behinds: Optional[int] = None
    away_behinds: Optional[int] = None
    venue: Optional[str] = None
    score_source: str = "numeric_columns"
    origin_path: str = ""
    origin_line: int = 0

    def row(self) -> dict:
        return {k: ("" if v is None else v) for k, v in asdict(self).items()}


@dataclass
class Coverage:
    rows: int = 0
    accepted: int = 0
    reasons: dict = field(default_factory=dict)

    def reject(self, reason: str):
        self.reasons[reason] = self.reasons.get(reason, 0) + 1


def _int(value) -> Optional[int]:
    text = str(value if value is not None else "").strip()
    return int(text) if re.fullmatch(r"\d+", text) else None


def _flag(value) -> Optional[bool]:
    text = str(value if value is not None else "").strip().lower()
    if text in {"yes", "y", "true", "1"}:
        return True
    if text in {"no", "n", "false", "0"}:
        return False
    return None


def _find(raw: dict, *prefixes: str) -> str:
    """First non-empty value whose header starts with one of `prefixes` (headers vary by file)."""
    for key, value in raw.items():
        if key and any(key.startswith(p) for p in prefixes) and str(value or "").strip():
            return str(value)
    return ""


AFL_SEPARATOR = r"(?:def(?:eated)?\.?(?:\s+by)?|drew(?:\s+with)?|drawn(?:\s+with)?|tied(?:\s+with)?)"


def afl_goals_behinds(text: str) -> Optional[dict]:
    """{team_key: (goals, behinds)} from "Team G.B (points) def. Team G.B (points)"; None otherwise.

    The points in brackets must equal 6 * goals + behinds for both sides or the text is rejected.
    """
    match = re.fullmatch(r"(.+?)\s+(\d+)\.(\d+)\s*\((\d+)\)\s+" + AFL_SEPARATOR + r"\s+(.+?)\s+(\d+)\.(\d+)\s*\((\d+)\)",
                         (text or "").strip(), re.I)
    if not match:
        return None
    a, ga, ba, pa, b, gb, bb, pb = match.groups()
    if 6 * int(ga) + int(ba) != int(pa) or 6 * int(gb) + int(bb) != int(pb):
        return None
    return {team_key(a): (int(ga), int(ba)), team_key(b): (int(gb), int(bb))}


def competition_files(archive_root: Path = ARCHIVE_ROOT):
    """Yield (sport, competition, year, path) for every yearly games file with the standard layout."""
    for path in sorted(archive_root.glob("*/*/*/*_games.csv")):
        sport, competition, year = path.parts[-4], path.parts[-3], path.parts[-2]
        if year.isdigit() and not sport.startswith("_"):
            yield sport, competition, int(year), path


def normalise_row(raw: dict, sport: str, competition: str, year: int, origin: str, line: int) -> tuple[Optional[StdEvent], str]:
    """Map one raw CSV row to a StdEvent, or (None, reason)."""
    day = (raw.get("Date") or "").strip()
    try:
        date.fromisoformat(day)
    except ValueError:
        return None, "invalid_event_date"
    home = (raw.get("Home Team") or raw.get("Home") or "").strip()
    away = (raw.get("Away Team") or raw.get("Away") or "").strip()
    if not home or not away or team_key(home) == team_key(away):
        return None, "invalid_team_identity"
    home_score, away_score = _int(raw.get("Home Score")), _int(raw.get("Away Score"))
    source = "numeric_columns"
    if home_score is None or away_score is None:
        parsed = parse_score(raw.get("Game Score") or raw.get("Match Score") or "")
        if not parsed:
            return None, "unparseable_score"
        first, score_first, second, score_second = parsed
        owned = {team_key(first): score_first, team_key(second): score_second}
        if team_key(home) not in owned or team_key(away) not in owned or len(owned) != 2:
            return None, "score_team_identity_mismatch"
        home_score, away_score = owned[team_key(home)], owned[team_key(away)]
        source = "score_text"
    total = _int(_find(raw, "Total Points", "Total Runs", "Total Goals"))
    margin = _int(raw.get("Winning Margin"))
    if total is not None and total != home_score + away_score:
        return None, "declared_total_disagrees"
    if margin is not None and margin != abs(home_score - away_score):
        return None, "declared_margin_disagrees"
    game_type = _find(raw, "Season Phase") or _find(raw, "Game Type", "Match Type", "Tournament Round")
    decision = (raw.get("Decision Type") or "").strip().lower()
    overtime = _flag(raw.get("Overtime") or raw.get("Extra Time / Golden Point"))
    shootout = _flag(raw.get("Shootout"))
    if decision in {"overtime", "shootout"} and overtime is None:
        overtime = True
    if decision == "shootout" and shootout is None:
        shootout = True
    home_gb = away_gb = None
    if source == "score_text":
        both = afl_goals_behinds(raw.get("Game Score") or raw.get("Match Score") or "")
        if both and team_key(home) in both and team_key(away) in both:
            home_gb, away_gb = both[team_key(home)], both[team_key(away)]
    innings = _int(raw.get("Innings Played"))
    extra = _flag(raw.get("Extra Innings"))
    if extra is None and innings is not None and sport == "Baseball":
        extra = innings > 9
    event = StdEvent(
        sport=sport, competition=competition, season_year=year, date=day, stage=stage_of(game_type or ""),
        home=home, away=away, home_score=home_score, away_score=away_score,
        overtime=overtime, shootout=shootout, innings=innings, extra_innings=extra,
        home_periods=(raw.get("Home Line Score") or raw.get("Home Line Score (runs by inning)") or "").strip() or None,
        away_periods=(raw.get("Away Line Score") or raw.get("Away Line Score (runs by inning)") or "").strip() or None,
        home_halftime=_int(raw.get("Home Halftime Score")), away_halftime=_int(raw.get("Away Halftime Score")),
        home_tries=_int(raw.get("Home Tries")), away_tries=_int(raw.get("Away Tries")),
        home_goals=_int(raw.get("Home Goals")) if home_gb is None else home_gb[0],
        away_goals=_int(raw.get("Away Goals")) if away_gb is None else away_gb[0],
        home_behinds=None if home_gb is None else home_gb[1], away_behinds=None if away_gb is None else away_gb[1],
        venue=(raw.get("Venue") or "").strip() or None,
        score_source=source, origin_path=origin, origin_line=line)
    return event, ""


def iter_events(archive_root: Path = ARCHIVE_ROOT, sport: Optional[str] = None, competition: Optional[str] = None,
                seasons: Optional[range] = None, coverage: Optional[dict] = None,
                stages: Optional[set] = None) -> Iterator[StdEvent]:
    """Yield accepted events; per (sport, competition, year) outcomes accumulate in `coverage`."""
    for sport_name, comp, year, path in competition_files(archive_root):
        if sport and sport_name != sport:
            continue
        if competition and comp != competition:
            continue
        if seasons is not None and year not in seasons:
            continue
        stats = coverage.setdefault((sport_name, comp, year), Coverage()) if coverage is not None else Coverage()
        origin = path.relative_to(archive_root.parent).as_posix()
        with path.open(newline="", encoding="utf-8-sig") as handle:
            for line, raw in enumerate(csv.DictReader(handle), start=2):
                stats.rows += 1
                event, reason = normalise_row(raw, sport_name, comp, year, origin, line)
                if event is None:
                    stats.reject(reason)
                    continue
                if stages is not None and event.stage not in stages:
                    stats.reject("outside_requested_stage")
                    continue
                stats.accepted += 1
                yield event


def coverage_report(archive_root: Path = ARCHIVE_ROOT) -> dict:
    coverage: dict = {}
    for _ in iter_events(archive_root, coverage=coverage):
        pass
    by_competition: dict = {}
    for (sport, comp, year), stats in sorted(coverage.items()):
        entry = by_competition.setdefault(f"{sport}/{comp}", {"sport": sport, "competition": comp, "rows": 0, "accepted": 0,
                                                              "seasons_with_data": [], "reasons": {}})
        entry["rows"] += stats.rows
        entry["accepted"] += stats.accepted
        if stats.accepted:
            entry["seasons_with_data"].append(year)
        for reason, count in stats.reasons.items():
            entry["reasons"][reason] = entry["reasons"].get(reason, 0) + count
    competitions = [v for v in by_competition.values() if v["rows"]]
    for v in competitions:
        years = v["seasons_with_data"]
        v["first_season"], v["last_season"] = (years[0], years[-1]) if years else (None, None)
        v["accepted_share"] = round(v["accepted"] / v["rows"], 4) if v["rows"] else None
        v["seasons_with_data"] = len(years)
    return {"schema": "archive-std-coverage-1", "std_fields": STD_FIELDS, "competitions": competitions,
            "totals": {"rows": sum(v["rows"] for v in competitions), "accepted": sum(v["accepted"] for v in competitions)}}


def render_coverage(report: dict) -> str:
    lines = ["# Archive standard-schema coverage", "",
             f"{report['totals']['accepted']:,} of {report['totals']['rows']:,} raw rows map onto the standard event schema "
             "(declared totals and margins agree with the extracted scores). Rejected rows are listed by reason.", "",
             "| Sport | Competition | Rows | Accepted | Share | Seasons | First–last | Main rejection reasons |",
             "|---|---|---:|---:|---:|---:|---|---|"]
    for v in sorted(report["competitions"], key=lambda item: (item["sport"], -item["rows"])):
        reasons = ", ".join(f"{k} {n}" for k, n in sorted(v["reasons"].items(), key=lambda kv: -kv[1])[:3]) or "—"
        lines.append(f"| {v['sport']} | {v['competition']} | {v['rows']:,} | {v['accepted']:,} | {100 * (v['accepted_share'] or 0):.1f}% | "
                     f"{v['seasons_with_data']} | {v['first_season']}–{v['last_season']} | {reasons} |")
    return "\n".join(lines) + "\n"


def build(out: Path, archive_root: Path = ARCHIVE_ROOT) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    handles, writers, counts = {}, {}, {}
    try:
        for event in iter_events(archive_root):
            name = re.sub(r"[^a-z0-9]+", "_", event.sport.lower()).strip("_")
            if name not in writers:
                handles[name] = (out / f"{name}.csv").open("w", newline="", encoding="utf-8")
                writers[name] = csv.DictWriter(handles[name], fieldnames=STD_FIELDS)
                writers[name].writeheader()
            writers[name].writerow(event.row())
            counts[name] = counts.get(name, 0) + 1
    finally:
        for handle in handles.values():
            handle.close()
    return counts


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    cov = sub.add_parser("coverage")
    cov.add_argument("--out", type=Path)
    bld = sub.add_parser("build")
    bld.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.command == "coverage":
        report = coverage_report()
        if args.out:
            args.out.mkdir(parents=True, exist_ok=True)
            (args.out / "archive_std_coverage.json").write_text(json.dumps(report, indent=1) + "\n", encoding="utf-8")
            (args.out / "archive_std_coverage.md").write_text(render_coverage(report), encoding="utf-8")
        print(json.dumps(report["totals"]))
    else:
        print(json.dumps(build(args.out), indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
