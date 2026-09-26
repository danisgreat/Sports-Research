#!/usr/bin/env python3
"""Results adapters for tools/sport_models.py (added 2026-09-26).

Every adapter returns completed results only, in one shape:
  team sports  {"id", "date" (ISO), "season", "home", "away", "hs", "as", "neutral", "finish",
                "hs_ht", "as_ht", "venue"}
  tennis       {"date", "tourney_id", "round", "match_num", "winner", "loser", "surface", "best_of",
                "total_games", "sets_margin", "complete", "walkover", "serve_won", "serve_pts"}
  cricket      {"date", "team1", "team2", "winner", "venue", "first_innings_valid", "bat_first",
                "bowl_first", "first_innings_runs"}

Market-blind. ESPN payloads can carry odds, pick'em and win-probability blocks; they are dropped on
load (the QUARANTINED_KEYS of tools/slate_universe.py) and never parsed or stored. Sources:
  ESPN site API scoreboard, one date per call (ESPN rejects date ranges), cached under .cache/sport_models/
  CSV results files (any league):  date,home,away,home_score,away_score[,neutral][,home_ht,away_ht]
                                   [,finish][,venue][,season][,event_id]
  Tennis: TML-Database yearly ATP CSVs (github.com/Tennismylife/TML-Database) or any directory of
          CSVs in the same (Sackmann) column format, e.g. WTA files you hold locally
  Cricket: a directory (or .zip) of cricsheet.org JSON match files
Standard library only.
"""
from __future__ import annotations

import csv
import datetime as dt
import gzip
import hashlib
import io
import json
import sys
import unicodedata
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
CACHE = REPO / ".cache" / "sport_models"
sys.path.insert(0, str(HERE))
from slate_universe import QUARANTINED_KEYS  # noqa: E402

ESPN = "https://site.api.espn.com/apis/site/v2/sports/{path}/scoreboard?dates={day}"
TML_URL = "https://raw.githubusercontent.com/Tennismylife/TML-Database/master/{year}.csv"


def _strip(obj):
    if isinstance(obj, dict):
        return {k: _strip(v) for k, v in obj.items() if k not in QUARANTINED_KEYS}
    if isinstance(obj, list):
        return [_strip(x) for x in obj]
    return obj


def fetch(url: str, permanent: bool, binary: bool = False):
    """Cached GET (gzip-aware, no browser User-Agent). Permanent entries are never refetched."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / (hashlib.sha1(url.encode()).hexdigest() + (".bin" if binary else ".json"))
    fresh = path.exists() and (permanent or (dt.datetime.now().timestamp() - path.stat().st_mtime) < 1800)
    if fresh:
        raw = path.read_bytes()
    else:
        req = urllib.request.Request(url, headers={"Accept-Encoding": "gzip"})
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
        if raw[:2] == b"\x1f\x8b":
            raw = gzip.decompress(raw)
        if not binary:
            raw = json.dumps(_strip(json.loads(raw.decode("utf-8")))).encode("utf-8")
        path.write_bytes(raw)
    return raw if binary else json.loads(raw.decode("utf-8"))


# --------------------------------------------------------------------------- names

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode()
    return " ".join("".join(c.lower() if c.isalnum() else " " for c in s).split())


def match_name(name: str, candidates) -> str:
    """Exact (normalised) match first, then a unique substring match either way."""
    cands = list(candidates)
    n = norm(name)
    exact = [c for c in cands if norm(c) == n]
    if len(exact) == 1:
        return exact[0]
    hits = [c for c in cands if n and (n in norm(c) or norm(c) in n)]
    if len(hits) == 1:
        return hits[0]
    raise SystemExit(f"error: {name!r} matched {len(hits)} names; use the full name as the source prints it")


# --------------------------------------------------------------------------- ESPN team sports

def parse_espn_event(ev: dict, family: str) -> dict | None:
    comp = (ev.get("competitions") or [{}])[0]
    cps = comp.get("competitors", [])
    h = next((c for c in cps if c.get("homeAway") == "home"), None)
    a = next((c for c in cps if c.get("homeAway") == "away"), None)
    if not h or not a:
        return None
    st = (comp.get("status") or ev.get("status") or {})
    stype = st.get("type", {})
    out = {"id": str(ev.get("id")), "date": ev.get("date", ""), "start_utc": ev.get("date", ""),
           "season": (ev.get("season") or {}).get("year"), "home": h["team"].get("displayName", ""),
           "away": a["team"].get("displayName", ""), "neutral": bool(comp.get("neutralSite", False)),
           "state": stype.get("state", ""), "completed": bool(stype.get("completed")),
           "venue": (comp.get("venue") or {}).get("fullName") or h["team"].get("displayName", ""),
           "hs": None, "as": None, "finish": None, "hs_ht": None, "as_ht": None}
    if out["start_utc"] and len(out["start_utc"]) == 17:  # ESPN writes 2026-09-27T19:00Z
        out["start_utc"] = out["start_utc"][:-1] + ":00Z"
    if out["completed"]:
        try:
            out["hs"], out["as"] = int(float(h.get("score"))), int(float(a.get("score")))
        except (TypeError, ValueError):
            return out
        detail = f"{stype.get('shortDetail', '')} {stype.get('detail', '')}".upper()
        period = int(st.get("period") or 0)
        if family == "hockey":
            out["finish"] = "SO" if "SO" in detail or period >= 5 else "OT" if "OT" in detail or period == 4 else "REG"
        else:
            out["finish"] = "OT" if "OT" in detail else "REG"
        if family == "goals":
            lh, la = h.get("linescores") or [], a.get("linescores") or []
            if lh and la:
                try:
                    out["hs_ht"], out["as_ht"] = int(float(lh[0]["value"])), int(float(la[0]["value"]))
                except (KeyError, TypeError, ValueError, IndexError):
                    pass
    return out


def espn_day(path: str, day: dt.date) -> list[dict]:
    old = (dt.date.today() - day).days > 2
    data = fetch(ESPN.format(path=path, day=f"{day:%Y%m%d}"), permanent=old)
    return data.get("events", [])


def espn_results(path: str, start: str, end: str, family: str) -> list[dict]:
    """Completed games dated [start, end] (venue calendar per ESPN), de-duplicated by event id."""
    d, d1 = dt.date.fromisoformat(start[:10]), dt.date.fromisoformat(end[:10])
    seen, out, failed = set(), [], 0
    while d <= d1:
        try:
            events = espn_day(path, d)
        except Exception:  # noqa: BLE001 - a failed day is counted, never silently filled
            failed += 1
            d += dt.timedelta(days=1)
            continue
        for ev in events:
            g = parse_espn_event(ev, family)
            if g and g["completed"] and g["hs"] is not None and g["id"] not in seen:
                seen.add(g["id"])
                out.append(g)
        d += dt.timedelta(days=1)
    if failed:
        print(f"warning: {failed} scoreboard day(s) failed to load; results may be incomplete", file=sys.stderr)
    return sorted(out, key=lambda g: g["date"])


def espn_event(path: str, event_id: str, date: str) -> dict:
    """One event, read from the scoreboard of its date (and the neighbouring dates for time-zone edges)."""
    d = dt.date.fromisoformat(date[:10])
    for day in (d, d - dt.timedelta(days=1), d + dt.timedelta(days=1)):
        for ev in espn_day(path, day):
            if str(ev.get("id")) == str(event_id):
                g = parse_espn_event(ev, "hockey" if path.startswith("hockey/") else
                                     "goals" if path.startswith("soccer/") else "points")
                if g is None:
                    break
                g["source"] = ESPN.format(path=path, day=f"{day:%Y%m%d}")
                return g
    raise SystemExit(f"error: event {event_id} not found on the {path} scoreboard around {date}")


# --------------------------------------------------------------------------- CSV (any league)

def _int(x):
    return None if x in (None, "") else int(float(x))


def load_csv(path: str) -> list[dict]:
    out = []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for i, r in enumerate(csv.DictReader(fh)):
            if r.get("home_score", "") == "" or r.get("away_score", "") == "":
                continue
            out.append({"id": r.get("event_id") or f"csv{i}", "date": r["date"], "home": r["home"], "away": r["away"],
                        "hs": _int(r["home_score"]), "as": _int(r["away_score"]),
                        "neutral": str(r.get("neutral", "")).strip().lower() in ("1", "true", "yes", "y"),
                        "hs_ht": _int(r.get("home_ht")), "as_ht": _int(r.get("away_ht")),
                        "finish": (r.get("finish") or "REG").strip().upper(), "venue": r.get("venue") or None,
                        "season": r.get("season") or None})
    return sorted(out, key=lambda g: g["date"])


# --------------------------------------------------------------------------- tennis (Sackmann/TML format)

def tennis_rows(text: str) -> list[dict]:
    sys.path.insert(0, str(HERE))
    from sport_models import parse_tennis_score
    out = []
    for r in csv.DictReader(io.StringIO(text)):
        d = r.get("tourney_date", "")
        if len(d) != 8 or not r.get("winner_name") or not r.get("loser_name"):
            continue
        sc = parse_tennis_score(r.get("score", ""))
        wo = "W/O" in (r.get("score") or "").upper() or (r.get("score") or "").strip().upper() in ("W/O", "WO")
        m = {"date": f"{d[:4]}-{d[4:6]}-{d[6:]}", "tourney_id": r.get("tourney_id", ""), "round": r.get("round", ""),
             "level": r.get("tourney_level", ""),
             "match_num": r.get("match_num") or 0, "winner": r["winner_name"], "loser": r["loser_name"],
             "surface": r.get("surface") or "Hard", "best_of": int(r.get("best_of") or 3), "walkover": wo,
             "complete": bool(sc and sc["complete"]) and not wo,
             "total_games": sc["games_w"] + sc["games_l"] if sc else None,
             "games_margin": sc["games_w"] - sc["games_l"] if sc else None,
             "sets_w": sc["sets_w"] if sc else None, "sets_l": sc["sets_l"] if sc else None,
             "sets_margin": sc["sets_w"] - sc["sets_l"] if sc else None, "serve_won": None, "serve_pts": None}
        try:
            won = sum(int(float(r[k])) for k in ("w_1stWon", "w_2ndWon", "l_1stWon", "l_2ndWon"))
            pts = int(float(r["w_svpt"])) + int(float(r["l_svpt"]))
            if pts > 0:
                m["serve_won"], m["serve_pts"] = won, pts
        except (KeyError, TypeError, ValueError):
            pass
        out.append(m)
    return out


def load_tennis(league: str, date: str, tml_dir: str | None = None, csv_path: str | None = None,
                years: int = 6) -> list[dict]:
    if csv_path:
        return tennis_rows(Path(csv_path).read_text(encoding="utf-8-sig"))
    y1 = int(date[:4])
    out = []
    if tml_dir:
        for p in sorted(Path(tml_dir).glob("*.csv")):
            out += tennis_rows(p.read_text(encoding="utf-8-sig"))
        return out
    if league != "atp":
        raise SystemExit("error: WTA needs --tml-dir with WTA results CSVs in the same column format")
    for y in range(y1 - years, y1 + 1):
        raw = fetch(TML_URL.format(year=y), permanent=y < y1, binary=True)
        out += tennis_rows(raw.decode("utf-8-sig"))
    return out


# --------------------------------------------------------------------------- cricket (cricsheet JSON)

def cricsheet_match(js: dict, overs: int) -> dict | None:
    info = js.get("info", {})
    teams = info.get("teams") or []
    if len(teams) != 2 or not info.get("dates"):
        return None
    if int(info.get("overs") or 0) != overs:
        return None
    outcome = info.get("outcome", {})
    winner = outcome.get("winner")
    innings = js.get("innings", [])
    m = {"date": str(info["dates"][0]), "team1": teams[0], "team2": teams[1], "winner": winner,
         "venue": info.get("venue", ""), "first_innings_valid": False, "bat_first": None, "bowl_first": None,
         "first_innings_runs": None, "match_type": info.get("match_type")}
    if innings:
        inn = innings[0]
        bat = inn.get("team")
        runs = wkts = legal = 0
        for ov in inn.get("overs", []):
            for dv in ov.get("deliveries", []):
                runs += dv.get("runs", {}).get("total", 0)
                wkts += len(dv.get("wickets", []))
                ex = dv.get("extras", {})
                if "wides" not in ex and "noballs" not in ex:
                    legal += 1
        full = legal >= 6 * overs or wkts >= 10
        method = outcome.get("method") or outcome.get("result") == "no result"
        m.update({"bat_first": bat, "bowl_first": teams[1] if bat == teams[0] else teams[0], "first_innings_runs": runs,
                  "first_innings_valid": bool(bat) and full and not method and "super_over" not in inn})
    return m


def load_cricsheet(src: str, overs: int) -> list[dict]:
    p = Path(src)
    blobs = []
    if p.suffix == ".zip":
        with zipfile.ZipFile(p) as z:
            blobs = [z.read(n) for n in z.namelist() if n.endswith(".json")]
    else:
        blobs = [f.read_bytes() for f in sorted(p.glob("*.json"))]
    out = []
    for b in blobs:
        try:
            m = cricsheet_match(json.loads(b.decode("utf-8")), overs)
        except (ValueError, UnicodeDecodeError):
            continue
        if m:
            out.append(m)
    return sorted(out, key=lambda m: m["date"])
