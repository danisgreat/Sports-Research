"""Reconcile basketball regular-season finals from two independent lineages, then ingest the matches (REV-07).

Provider A is the ESPN site scoreboard (one request per date). Provider B is the Basketball-Reference monthly
schedule. They are separate collectors: ESPN is the rights-holder feed, Basketball-Reference compiles from league
box scores. A game is admitted only when both lineages agree on the participants, the final score and whether
overtime was played, and exactly one pair matches. ESPN's period scores give the regulation score. A newly captured
historical fact is known NOW, never on its game date, and ``final_at`` is the observed-final upper bound, so these
rows can train future models but cannot support any retrospective pregame claim.

    python -m ml.backfill_basketball --league nba --start 2023-10-01 --end 2024-06-30 \
        --cache <dir outside the repository> --out <new folder> --store research/learning_store

Raw HTTP bodies stay in the external cache; the committed projections and their hashes are the ingest evidence.
Only the stdlib, pandas and the repository's own helpers are used. No odds or market field is read or stored.
"""
from __future__ import annotations

import argparse
import html
import re
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from ml import primary as p, research_ingest as ri

LEAGUES = {  # slug on ESPN; competition label and endpoint match ml.config.SPORT_RULES["Basketball"]
    "nba": dict(espn="basketball/nba", competition="Basketball/NBA", endpoint="FULL_GAME_INCL_OT",
                br="https://www.basketball-reference.com/leagues/NBA_{year}_games-{month}.html", regulation_periods=4),
}
ALIASES = {"la clippers": "los angeles clippers"}  # ml.config.OVERRIDES["Basketball/NBA"]
UA = "SportsResearch result verification (research use; contact via repository owner)"
NEW_YORK = ZoneInfo("America/New_York")


def canonical(team: str) -> str:
    key = re.sub(r"\s+", " ", team.strip().lower())
    return ALIASES.get(key, key)


def display(team: str) -> str:
    return "Los Angeles Clippers" if canonical(team) == "los angeles clippers" else team.strip()


def fetch(url: str, cache: Path, suffix: str, pause: float = 0.0, tries: int = 3):
    cache.mkdir(parents=True, exist_ok=True)
    last = None
    for attempt in range(tries):
        try:
            if pause:
                time.sleep(pause)
            raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60).read()
            sha = p.digest(raw)
            (cache / (sha + suffix)).write_bytes(raw)
            return raw, dict(source_url=url, retrieved_at=datetime.now(timezone.utc).isoformat(), raw_sha256=sha,
                             raw_bytes=len(raw), external_raw_capture=str(cache / (sha + suffix)), error="")
        except Exception as exc:  # recorded, never hidden; the caller decides what a failed page means
            last = exc
            time.sleep(2 * (attempt + 1))
    return b"", dict(source_url=url, retrieved_at=datetime.now(timezone.utc).isoformat(), raw_sha256="", raw_bytes=0,
                     external_raw_capture="", error=type(last).__name__ + ": " + str(last))


def espn_rows(data: dict, requested_date: str, regulation_periods: int = 4) -> list[dict]:
    """Completed regular-season (season.type 2) events from one scoreboard payload."""
    rows = []
    for ev in data.get("events", []):
        if ev.get("season", {}).get("type") != 2 or not ev["status"]["type"].get("completed"):
            continue
        co = ev["competitions"][0]
        sides = {c["homeAway"]: c for c in co["competitors"]}
        if set(sides) != {"home", "away"}:
            continue
        periods = {s: [int(x["value"]) for x in sides[s].get("linescores", [])] for s in sides}
        hs, as_ = int(sides["home"]["score"]), int(sides["away"]["score"])
        if len(periods["home"]) != len(periods["away"]) or len(periods["home"]) < regulation_periods:
            continue
        if sum(periods["home"]) != hs or sum(periods["away"]) != as_:
            continue  # period scores must add to the final; otherwise the row is not trustworthy
        extra = len(periods["home"]) > regulation_periods
        rows.append(dict(date=requested_date, event_id="ESPN:" + str(ev["id"]), provider_id=str(ev["id"]),
                         event_at=ev["date"], home=display(sides["home"]["team"]["displayName"]),
                         away=display(sides["away"]["team"]["displayName"]), venue=co.get("venue", {}).get("fullName", ""),
                         hs=hs, as_=as_, reg_hs=sum(periods["home"][:regulation_periods]),
                         reg_as=sum(periods["away"][:regulation_periods]), decision="Overtime" if extra else "Regulation",
                         periods=len(periods["home"]), season=str(int(ev["season"]["year"]) - 1), neutral=bool(co.get("neutralSite"))))
    return rows


_ROW = re.compile(r"<tr\b[^>]*>(.*?)</tr>", re.S)
_CELL = re.compile(r"<t[hd]\b([^>]*)>(.*?)</t[hd]>", re.S)
_STAT, _CSK = re.compile(r'data-stat="([a-z_]+)"'), re.compile(r'csk="([^"]*)"')


def br_rows(page: str, year: int) -> list[dict]:
    """Played games from one Basketball-Reference schedule page (the page for a month that has not started is empty)."""
    rows = []
    for tr in _ROW.findall(page):
        cells = {}
        for attrs, body in _CELL.findall(tr):
            stat, csk = _STAT.search(attrs), _CSK.search(attrs)
            if stat:
                cells[stat.group(1)] = (csk.group(1) if csk else "", re.sub(r"<[^>]+>", "", body).strip())
        if "date_game" not in cells or not cells.get("visitor_pts", ("", ""))[1]:
            continue
        csk = cells["date_game"][0]
        try:
            day = datetime.strptime(html.unescape(cells["date_game"][1]), "%a, %b %d, %Y").date()
        except ValueError:
            continue  # a header row repeated inside the table body
        ot = html.unescape(cells.get("overtimes", ("", ""))[1])
        if not cells["visitor_pts"][1].isdigit() or not cells["home_pts"][1].isdigit():
            continue
        rows.append(dict(date=day.isoformat(), csk=csk, home=display(html.unescape(cells["home_team_name"][1])),
                         away=display(html.unescape(cells["visitor_team_name"][1])), hs=int(cells["home_pts"][1]),
                         as_=int(cells["visitor_pts"][1]), overtime=bool(ot), season_end_year=year))
    return rows


def reconcile(owner: list[dict], other: list[dict]) -> tuple[list[dict], list[dict]]:
    """Pairs of (provider A row, provider B row) that agree uniquely; plus a disposition for every provider-A game."""
    pairs, decisions, used = [], [], set()
    for r in owner:
        local = datetime.fromisoformat(r["event_at"].replace("Z", "+00:00")).astimezone(NEW_YORK).date()
        candidates = [s for s in other if canonical(s["home"]) == canonical(r["home"]) and canonical(s["away"]) == canonical(r["away"])
                      and abs((date.fromisoformat(s["date"]) - local).days) <= 1]
        agree = [s for s in candidates if (s["hs"], s["as_"]) == (r["hs"], r["as_"])]
        if len(agree) != 1:
            decisions.append(dict(event_id=r["event_id"], status="NOT_INGESTED",
                                  reason="NO_INDEPENDENT_MATCH" if not candidates else "SCORE_CONFLICT_OR_AMBIGUOUS", independent=""))
            continue
        s = agree[0]
        if s["overtime"] != (r["decision"] == "Overtime"):
            decisions.append(dict(event_id=r["event_id"], status="NOT_INGESTED", reason="OVERTIME_FLAG_CONFLICT", independent=s["csk"]))
            continue
        if s["csk"] in used:
            raise p.AdmissionError("independent game joined to more than one provider-A game")
        used.add(s["csk"])
        pairs.append((r, s))
        decisions.append(dict(event_id=r["event_id"], status="VERIFIED_FOR_FUTURE_TRAINING",
                              reason="TWO_LINEAGES_AGREE_ON_TEAMS_FINAL_AND_OVERTIME;FINAL_AT_OBSERVED_UPPER_BOUND;KNOWN_NOW",
                              independent=s["csk"]))
    return pairs, decisions


def br_page(day: date) -> tuple[int, str]:
    """Basketball-Reference files a game under its season's ending year and the month name of the (US Eastern) date."""
    return day.year + (1 if day.month >= 8 else 0), day.strftime("%B").lower()


def _days(start: str, end: str):
    day, stop = date.fromisoformat(start), date.fromisoformat(end)
    while day <= stop:
        yield day.isoformat()
        day += timedelta(days=1)


def run(league: str, start: str, end: str, cache: Path, out: Path, store: Path, pause: float = 3.5) -> dict:
    spec = LEAGUES[league]
    out, cache = Path(out), Path(cache)
    out.mkdir(parents=True, exist_ok=False)
    espn_url = "https://site.api.espn.com/apis/site/v2/sports/" + spec["espn"] + "/scoreboard?dates={d}&limit=100"

    def one(day):
        raw, rec = fetch(espn_url.format(d=day.replace("-", "")), cache, ".json")
        if rec["error"]:
            return [], rec
        import json
        return espn_rows(json.loads(raw), day, spec["regulation_periods"]), rec

    with ThreadPoolExecutor(max_workers=6) as pool:
        espn = list(pool.map(one, list(_days(start, end))))
    owner = [r for rows, _ in espn for r in rows]
    first, last = date.fromisoformat(start), date.fromisoformat(end)
    pages = sorted({br_page(first + timedelta(days=i)) for i in range((last - first).days + 2)})
    other, br_receipts = [], []
    for year, month in pages:
        raw, rec = fetch(spec["br"].format(year=year, month=month), cache, ".html", pause=pause)
        br_receipts.append(rec)
        if not rec["error"]:
            other += br_rows(raw.decode("utf-8", "replace"), year)
    owner = [r for r in owner if start <= r["date"] <= end]
    other = [s for s in other if start <= s["date"] <= (last + timedelta(days=1)).isoformat()]
    receipts = [r for _, r in espn] + br_receipts
    if not owner or not other:
        raise p.AdmissionError("no provider-A or provider-B finals: preserve diagnostics; do not ingest")
    pairs, decisions = reconcile(owner, other)
    owner_path, other_path = out / "ESPN_RESULTS.csv", out / "BKREF_RESULTS.csv"
    owner_path.write_bytes(p.csv_bytes(owner))
    other_path.write_bytes(p.csv_bytes(other))
    (out / "HTTP_RECEIPTS.csv").write_bytes(p.csv_bytes(receipts))
    (out / "RECONCILIATION.csv").write_bytes(p.csv_bytes(decisions))
    owner_digest, other_digest = p.digest(owner_path.read_bytes()), p.digest(other_path.read_bytes())
    by_url = {r["source_url"]: r for r in receipts}
    games = []
    for r, s in pairs:
        espn_receipt = by_url[espn_url.format(d=r["date"].replace("-", ""))]
        year, month = br_page(date.fromisoformat(s["date"]))
        br_receipt = by_url[spec["br"].format(year=year, month=month)]
        known = max(espn_receipt["retrieved_at"], br_receipt["retrieved_at"])
        values = dict(competition=spec["competition"], endpoint=spec["endpoint"], native_event_id=r["event_id"], season=r["season"],
                      event_at=r["event_at"], home=r["home"], away=r["away"], venue=r["venue"], status="FINAL",
                      hs=str(r["hs"]), as_=str(r["as_"]), reg_hs=str(r["reg_hs"]), reg_as=str(r["reg_as"]), decision=r["decision"],
                      final_at=known, source_kind="WEB_RECOVERED", published_at="", retrieved_at=known, known_at=known,
                      review_status="RESEARCH_INPUT_REVIEWED", collected_by="SOURCE_BACKFILL_CURRENT_CAPTURE_FINAL_UPPER_BOUND")
        games.append(dict(values, source_url=espn_receipt["source_url"], capture_path=owner_path.as_posix(), capture_sha256=owner_digest))
        games.append(dict(values, source_url=br_receipt["source_url"], capture_path=other_path.as_posix(), capture_sha256=other_digest))
    export = out / "EXPORT"
    export.mkdir()
    for filename, fields in ri.EXPORT_FILES.items():
        (export / filename).write_bytes(p.csv_bytes(games) if filename == "GAME_OBSERVATIONS.csv" and games else (",".join(fields) + "\n").encode())
    rec = ri.ingest(export, Path(store))
    (out / "INGEST.csv").write_bytes(p.csv_bytes([rec]))
    (out / "README.md").write_text(
        "# Verified basketball backfill\n\nProvider A (ESPN scoreboard, one request per date, regular season only) and provider B "
        "(Basketball-Reference monthly schedule) are separate lineages. A game is ingested only when both agree on the participants, "
        "the final score and whether overtime was played, and the pair is unique. Regulation comes from ESPN's period scores. "
        "`final_at` is the current observed-final upper bound and `known_at` is the later of the two retrievals, so these rows cannot "
        "enter a historical pregame replay. Raw HTTP bodies stay in the external cache named in HTTP_RECEIPTS.csv. Every provider-A "
        "game has a disposition in RECONCILIATION.csv. No odds, lines or market fields are read.\n", encoding="utf-8")
    return dict(rec, owner_games=len(owner), independent_games=len(other), verified=len(pairs), not_ingested=len(decisions) - len(pairs))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--league", choices=sorted(LEAGUES), required=True)
    for name in ("start", "end", "cache", "out", "store"):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--pause", type=float, default=3.5)
    args = parser.parse_args(argv)
    print(run(args.league, args.start, args.end, Path(args.cache), Path(args.out), Path(args.store), args.pause))


if __name__ == "__main__":
    main()
