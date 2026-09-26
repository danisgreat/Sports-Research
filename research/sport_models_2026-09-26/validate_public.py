#!/usr/bin/env python3
"""Rolling-origin validation of tools/sport_models.py (and the MLB team-only A1) on public results data.

Run on 2026-09-26 with the priors declared in commit ac6fdc5 ("declare A0/A1 engines and priors for every
sport before validation"). Nothing in tools/sport_models.py was tuned on these results; if a constant
changes later, this file is re-run and both results are kept (NUMERICAL_PROGRAM §1: preserve failed
comparisons).

Sources (only those reachable from the session that ran this; each file's SHA-256 is recorded):
  soccer   openfootball/football.json  (public domain; scores and half-time scores)
  NFL      nflverse/nfldata games.csv  (ONLY season, game_type, gameday, teams, scores, location are read;
                                        the file also carries betting columns, which are never read, printed
                                        or stored — the raw file stays in the git-ignored cache)
  AFL      akareen/AFL-Data-Analysis   match tables (goals and behinds; team_1 treated as the home side)
  NBA      fivethirtyeight/data nba-elo (seasons to 2015 only; ONLY dates, teams, points, venue role and
                                        the playoff flag are read — 538's own forecast column is never read)
  tennis   Tennismylife/TML-Database   ATP match results with serve totals
  MLB      chadwickbureau/retrosheet   game logs. "The information used here was obtained free of charge
                                        from and is copyrighted by Retrosheet. Interested parties may
                                        contact Retrosheet at www.retrosheet.org."
Not reachable from that session, so NOT validated here: NHL, WNBA, NBL, NRL, rugby union, cricket,
NPB/KBO/CPBL. `python tools/sport_models.py validate --league <key> --from … --to …` runs the same
comparison from ESPN wherever the network allows.

Usage: python research/sport_models_2026-09-26/validate_public.py [--only soccer,nfl,...] [--boot 2000]
Writes validation_results.json and provenance.json beside this file. LEARNING_ONLY; descriptive.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "tools"))
import sport_data as sd  # noqa: E402
import sport_models as sm  # noqa: E402

RAW = "https://raw.githubusercontent.com/"
CACHE = HERE / "cache"
PROVENANCE: dict = {}


def get(url: str) -> bytes:
    CACHE.mkdir(exist_ok=True)
    path = CACHE / hashlib.sha1(url.encode()).hexdigest()
    if not path.exists():
        with urllib.request.urlopen(urllib.request.Request(url), timeout=120) as r:
            path.write_bytes(r.read())
    raw = path.read_bytes()
    PROVENANCE[url] = {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
    return raw


# --------------------------------------------------------------------------- loaders

SOCCER = {"epl": "en.1", "bundesliga": "de.1", "laliga": "es.1", "seriea": "it.1", "ligue1": "fr.1"}
SOCCER_SEASONS = ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]


def soccer(league: str) -> list[dict]:
    out = []
    for s in SOCCER_SEASONS:
        js = json.loads(get(f"{RAW}openfootball/football.json/master/{s}/{SOCCER[league]}.json"))
        for i, m in enumerate(js.get("matches", [])):
            sc = m.get("score") or {}
            if isinstance(sc, list):          # some 2025-26 rows carry a bare full-time [home, away] pair
                sc = {"ft": sc}
            ft = sc.get("ft")
            if not ft or len(ft) != 2 or not m.get("date"):
                continue
            ht = sc.get("ht") or [None, None]
            out.append({"id": f"{s}-{i}", "date": m["date"], "season": int(s[:4]), "home": m["team1"], "away": m["team2"],
                        "hs": int(ft[0]), "as": int(ft[1]), "hs_ht": ht[0], "as_ht": ht[1], "neutral": False})
    return sorted(out, key=lambda g: g["date"])


def nfl() -> list[dict]:
    text = get(f"{RAW}nflverse/nfldata/master/data/games.csv").decode("utf-8")
    keep = ("season", "game_type", "gameday", "home_team", "away_team", "home_score", "away_score", "location", "game_id")
    out = []
    for r in csv.DictReader(io.StringIO(text)):
        r = {k: r.get(k, "") for k in keep}          # every other column (including betting columns) is dropped here
        if r["game_type"] != "REG" or r["home_score"] == "" or int(r["season"]) < 2018:
            continue
        out.append({"id": r["game_id"], "date": r["gameday"], "season": int(r["season"]), "home": r["home_team"],
                    "away": r["away_team"], "hs": int(r["home_score"]), "as": int(r["away_score"]),
                    "neutral": r["location"].strip().lower() == "neutral"})
    return sorted(out, key=lambda g: g["date"])


def afl() -> list[dict]:
    out = []
    for y in range(2018, 2026):
        text = get(f"{RAW}akareen/AFL-Data-Analysis/main/data/matches/matches_{y}.csv").decode("utf-8-sig")
        for i, r in enumerate(csv.DictReader(io.StringIO(text))):
            try:
                hs = 6 * int(r["team_1_final_goals"]) + int(r["team_1_final_behinds"])
                as_ = 6 * int(r["team_2_final_goals"]) + int(r["team_2_final_behinds"])
            except (KeyError, ValueError):
                continue
            out.append({"id": f"{y}-{i}", "date": r["date"][:10], "season": y, "home": r["team_1_team_name"],
                        "away": r["team_2_team_name"], "hs": hs, "as": as_, "neutral": False, "venue": r.get("venue")})
    return sorted(out, key=lambda g: g["date"])


def nba538() -> list[dict]:
    text = get(f"{RAW}fivethirtyeight/data/master/nba-elo/nbaallelo.csv").decode("utf-8")
    keep = ("game_id", "lg_id", "_iscopy", "year_id", "date_game", "is_playoffs", "team_id", "pts", "opp_id",
            "opp_pts", "game_location")
    out = []
    for r in csv.DictReader(io.StringIO(text)):
        r = {k: r.get(k, "") for k in keep}          # 538's elo and forecast columns are dropped here, unread
        if r["lg_id"] != "NBA" or r["_iscopy"] != "0" or r["is_playoffs"] != "0" or int(r["year_id"]) < 2010:
            continue
        mth, day, yr = (int(x) for x in r["date_game"].split("/"))
        loc = r["game_location"]
        t, o, pt, po = r["team_id"], r["opp_id"], int(r["pts"]), int(r["opp_pts"])
        h, a, hs, as_ = (t, o, pt, po) if loc in ("H", "N") else (o, t, po, pt)
        out.append({"id": r["game_id"], "date": f"{yr:04d}-{mth:02d}-{day:02d}", "season": int(r["year_id"]),
                    "home": h, "away": a, "hs": hs, "as": as_, "neutral": loc == "N", "finish": "REG"})
    return sorted(out, key=lambda g: g["date"])


def tennis() -> list[dict]:
    out = []
    for y in range(2017, 2027):
        out += sd.tennis_rows(get(f"{RAW}Tennismylife/TML-Database/master/{y}.csv").decode("utf-8-sig"))
    return out


def mlb() -> list[dict]:
    out = []
    for y in range(2021, 2025):
        name = f"gl{y}.txt" if y >= 2024 else f"GL{y}.TXT"      # the repository's file-name case changes in 2024
        text = get(f"{RAW}chadwickbureau/retrosheet/master/seasons/{y}/{name}").decode("latin-1")
        for i, f in enumerate(csv.reader(io.StringIO(text))):
            d = f[0]
            out.append({"id": f"{d}-{f[6]}-{f[1]}", "date": f"{d[:4]}-{d[4:6]}-{d[6:]}", "season": y, "home": f[6],
                        "away": f[3], "hs": int(f[10]), "as": int(f[9]), "venue": f[16], "neutral": False})
    return sorted(out, key=lambda g: (g["date"], g["id"]))


# ----- second pass (2026-09-26(d)): sportsdataverse parquet files and an IPL dataset. These need pyarrow
# (research only: `pip install pyarrow`); tools/ stays standard-library. Only the named columns are read.

SDV = RAW + "sportsdataverse/"


def _parquet(url: str, columns: list[str]) -> list[dict]:
    import pyarrow.parquet as pq  # research-only dependency
    return pq.read_table(io.BytesIO(get(url)), columns=columns).to_pylist()


def espn_sdv(repo: str, league: str, seasons) -> list[dict]:
    """ESPN schedules as compiled by sportsdataverse (hoopR/wehoop): regular season (type 2), completed."""
    cols = ["game_id", "game_date", "season", "season_type", "neutral_site", "status_type_completed",
            "status_type_short_detail", "home_display_name", "away_display_name", "home_score", "away_score"]
    out = []
    for s in seasons:
        for r in _parquet(f"{SDV}{repo}/main/{league}/schedules/parquet/{league}_schedule_{s}.parquet", cols):
            if r["season_type"] != 2 or not r["status_type_completed"] or r["home_score"] in (None, ""):
                continue
            out.append({"id": str(r["game_id"]), "date": str(r["game_date"])[:10], "season": int(r["season"]),
                        "home": r["home_display_name"], "away": r["away_display_name"], "hs": int(r["home_score"]),
                        "as": int(r["away_score"]), "neutral": bool(r["neutral_site"]),
                        "finish": "OT" if "OT" in str(r["status_type_short_detail"] or "").upper() else "REG"})
    return sorted(out, key=lambda g: (g["date"], g["id"]))


def nhl() -> list[dict]:
    """fastRhockey NHL game_info (final scores, the shootout winner's +1 included) and scoring (period type of
    every goal: an 'SO' row marks a shootout, an 'OT' row an overtime winner). The linescore file's
    has_shootout flag is False for every game in these files, so it is not used."""
    base = f"{SDV}fastRhockey-nhl-data/main/nhl"
    out = []
    for s in range(2022, 2027):
        goals = _parquet(f"{base}/scoring/parquet/scoring_{s}.parquet", ["game_id", "period_type"])
        so = {r["game_id"] for r in goals if r["period_type"] == "SO"}
        ot = {r["game_id"] for r in goals if r["period_type"] == "OT"}
        for r in _parquet(f"{base}/game_info/parquet/game_info_{s}.parquet",
                          ["game_id", "season", "game_type", "game_date", "home_team_abbr", "away_team_abbr",
                           "home_score", "away_score", "game_state"]):
            if r["game_type"] != "R" or r["game_state"] not in ("OFF", "FINAL") or r["home_score"] is None:
                continue
            gid = r["game_id"]
            finish = "SO" if gid in so else "OT" if gid in ot else "REG"
            out.append({"id": str(gid), "date": str(r["game_date"])[:10], "season": s, "home": r["home_team_abbr"],
                        "away": r["away_team_abbr"], "hs": int(r["home_score"]), "as": int(r["away_score"]),
                        "neutral": False, "finish": finish})
    return sorted(out, key=lambda g: (g["date"], g["id"]))


IPL_RENAMES = {"Delhi Daredevils": "Delhi Capitals", "Kings XI Punjab": "Punjab Kings",
               "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
               "Rising Pune Supergiants": "Rising Pune Supergiant"}


def ipl() -> list[dict]:
    """IPL results and first innings from ritesh-ojha/IPL-DATASET. A first innings is valid (uncensored) when
    it faced all 120 legal balls or lost 10 wickets; a rain-shortened first innings is excluded."""
    ren = lambda s: IPL_RENAMES.get(s, s)  # noqa: E731
    info = {r["match_number"]: r for r in csv.DictReader(io.StringIO(
        get(f"{RAW}ritesh-ojha/IPL-DATASET/main/csv/Match_Info.csv").decode("utf-8")))}
    inn = {}
    for r in csv.DictReader(io.StringIO(get(f"{RAW}ritesh-ojha/IPL-DATASET/main/csv/Ball_By_Ball_Match_Data.csv")
                                        .decode("utf-8"))):
        if r["Innings"] != "1":
            continue
        d = inn.setdefault(r["ID"], {"team": r["BattingTeam"], "runs": 0, "legal": 0, "wkts": 0})
        d["runs"] += int(r["TotalRun"])
        d["wkts"] += r["IsWicketDelivery"] == "1"
        d["legal"] += r["ExtraType"] not in ("wides", "noballs")
    out = []
    for mid, r in info.items():
        t1, t2 = ren(r["team1"]), ren(r["team2"])
        res = r["result"].strip().lower()
        m = {"date": r["match_date"], "team1": t1, "team2": t2, "winner": ren(r["winner"]) if res == "win" else None,
             "venue": r["venue"].split(",")[0].strip(), "first_innings_valid": False, "bat_first": None,
             "bowl_first": None, "first_innings_runs": None}
        f = inn.get(mid)
        if f:
            bat = ren(f["team"])
            m.update({"bat_first": bat, "bowl_first": t2 if bat == t1 else t1, "first_innings_runs": f["runs"],
                      "first_innings_valid": res != "no result" and (f["legal"] >= 120 or f["wkts"] >= 10)})
        out.append(m)
    return sorted(out, key=lambda m: m["date"])


# --------------------------------------------------------------------------- runs

RUNS = {
    # key: (loader, sport_models league, from, to, TB-1 league or None)
    "epl": (lambda: soccer("epl"), "epl", "2022-08-01", "2026-06-30", "epl"),
    "bundesliga": (lambda: soccer("bundesliga"), "bundesliga", "2022-08-01", "2026-06-30", None),
    "laliga": (lambda: soccer("laliga"), "laliga", "2022-08-01", "2026-06-30", None),
    "seriea": (lambda: soccer("seriea"), "seriea", "2022-08-01", "2026-06-30", None),
    "ligue1": (lambda: soccer("ligue1"), "ligue1", "2022-08-01", "2026-06-30", None),
    "nfl": (nfl, "nfl", "2021-09-01", "2026-02-15", "nfl"),
    "afl": (afl, "afl", "2021-03-01", "2025-10-01", "afl"),
    "nba": (nba538, "nba", "2012-10-01", "2015-04-30", "nba"),
    "mlb": (mlb, "mlb-teamonly", "2022-04-01", "2024-10-01", "mlb"),
    # second pass, 2026-09-26(d): constants as frozen in commit 0872a36, not changed for these runs
    "nhl": (nhl, "nhl", "2023-10-01", "2026-06-30", "nhl"),
    "nba_recent": (lambda: espn_sdv("hoopR-nba-data", "nba", range(2021, 2027)), "nba", "2023-10-01", "2026-06-30", "nba"),
    "wnba": (lambda: espn_sdv("wehoop-wnba-data", "wnba", range(2020, 2027)), "wnba", "2022-05-01", "2026-09-20", "wnba"),
}


def run_one(key: str, boot: int) -> dict:
    t0 = time.time()
    if key == "ipl":
        res = sm.validate_cricket(sm.config("t20"), ipl(), "2016-01-01", "2026-09-20", boot=boot)
    elif key == "atp":
        res = sm.validate_tennis(sm.config("atp"), tennis(), "2023-01-01", "2026-09-20",
                                 levels={"G", "M", "A", "F", "250", "500"}, boot=boot)
    else:
        loader, league, frm, to, tb1 = RUNS[key]
        games = loader()
        cfg = sm.config(league)
        res = sm.validate_team(cfg, games, frm, to, tb1_league=tb1, dc=cfg["family"] == "goals", boot=boot)
        res["n_games_loaded"] = len(games)
    res["seconds"] = round(time.time() - t0, 1)
    res["provenance"] = dict(PROVENANCE)
    return res


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", help="comma-separated run keys (default: every key in RUNS, then atp)")
    ap.add_argument("--boot", type=int, default=2000)
    ap.add_argument("--merge", action="store_true", help="combine parts/*.json into validation_results.json")
    args = ap.parse_args(argv)
    parts = HERE / "parts"
    parts.mkdir(exist_ok=True)
    if not args.merge:
        keys = args.only.split(",") if args.only else list(RUNS) + ["atp", "ipl"]
        for key in keys:
            res = run_one(key, args.boot)
            (parts / f"{key}.json").write_text(json.dumps(res, indent=1, sort_keys=True), encoding="utf-8")
            print(key, res["n"], f"{res['seconds']}s", flush=True)
        if args.only:
            return 0
    results, prov = {"v1": {}, "v2": {}}, {}
    for f in sorted(parts.glob("*.json")):
        res = json.loads(f.read_text(encoding="utf-8"))
        prov.update(res.pop("provenance", {}))
        results["v1"][f.stem] = res
    for f in sorted((HERE / "parts_v2").glob("*.json")):   # tune_v2.py (MLB and tennis re-selection)
        res = json.loads(f.read_text(encoding="utf-8"))
        res.pop("provenance", None)
        results["v2"][f.stem] = res
    results["_meta"] = {"merged_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                        "declared_priors_commit": "ac6fdc5",
                        "v1": "priors as declared in ac6fdc5 (SPORT-A1-shadow/2026-09-26); MLB run = team_prior_games 20",
                        "v2": "tune_v2.py: MLB team_prior_games and tennis gap_sd re-selected on earlier TUNE windows",
                        "note": "A1 − A0 < 0 means A1 scored better (all metrics are losses). ci95_block is a "
                                "block bootstrap (ISO weeks; tournaments for tennis). Descriptive, not a promotion."}
    (HERE / "validation_results.json").write_text(json.dumps(results, indent=1, sort_keys=True), encoding="utf-8")
    (HERE / "provenance.json").write_text(json.dumps(prov, indent=1, sort_keys=True), encoding="utf-8")
    return 0


if __name__ == "__main__":
    code = main()
    sys.stdout.flush()
    os._exit(code)   # pyarrow's worker threads can abort a normal interpreter shutdown after the files are written
