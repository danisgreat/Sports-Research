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
import re
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


def fetch(url: str, permanent: bool, binary: bool = False, force: bool = False):
    """Cached GET (gzip-aware, no browser User-Agent). Permanent entries are not refetched unless force."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / (hashlib.sha1(url.encode()).hexdigest() + (".bin" if binary else ".json"))
    fresh = not force and path.exists() and (permanent or (dt.datetime.now().timestamp() - path.stat().st_mtime) < 1800)
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
            # extra time or penalties: the model's target is the 90-minute score. Settle on the first two
            # periods when ESPN gives them; otherwise the score is unknown (hs/as None) and the row is void.
            if any(k in detail for k in ("AET", "PEN", "EXTRA TIME")) or len(lh) > 2 or len(la) > 2:
                out["finish"] = "AET"
                try:
                    out["hs"] = int(sum(float(x["value"]) for x in lh[:2]))
                    out["as"] = int(sum(float(x["value"]) for x in la[:2]))
                    if len(lh) < 2 or len(la) < 2:
                        raise ValueError
                except (KeyError, TypeError, ValueError):
                    out["hs"] = out["as"] = None
    return out


def _all_final(events: list[dict]) -> bool:
    def state(ev):
        comp = (ev.get("competitions") or [{}])[0]
        return ((comp.get("status") or ev.get("status") or {}).get("type") or {}).get("state")
    groups = [c for ev in events for g in ev.get("groupings", []) for c in g.get("competitions", [])]
    return all(state(x) == "post" for x in (groups or events))


def espn_day(path: str, day: dt.date, force: bool = False) -> list[dict]:
    """One scoreboard date. A cached day is reused only when it is more than two days old AND every event in
    it was already final when cached; otherwise it is refetched (a stale pre-game snapshot never settles)."""
    url = ESPN.format(path=path, day=f"{day:%Y%m%d}")
    old = (dt.date.today() - day).days > 2
    data = fetch(url, permanent=old and not force, force=force)
    if old and not force and not _all_final(data.get("events", [])):
        data = fetch(url, permanent=False, force=True)
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


def espn_event(path: str, event_id: str, date: str, force: bool = False) -> dict:
    """One event, read from the scoreboard of its date (and the neighbouring dates for time-zone edges)."""
    d = dt.date.fromisoformat(date[:10])
    for day in (d, d - dt.timedelta(days=1), d + dt.timedelta(days=1)):
        for ev in espn_day(path, day, force=force):
            if str(ev.get("id")) == str(event_id):
                g = parse_espn_event(ev, "hockey" if path.startswith("hockey/") else
                                     "goals" if path.startswith("soccer/") else "points")
                if g is None:
                    break
                g["source"] = ESPN.format(path=path, day=f"{day:%Y%m%d}")
                return g
    raise SystemExit(f"error: event {event_id} not found on the {path} scoreboard around {date}")


# --------------------------------------------------------------------------- ESPN tennis and cricket

def _iso_z(s: str) -> str:
    return s[:-1] + ":00Z" if s and len(s) == 17 and s.endswith("Z") else s


def parse_tennis_comp(c: dict, source: str) -> dict:
    """One ESPN tennis competition (a singles match). Players are A and B in ESPN's order."""
    cps = c.get("competitors", [])
    if len(cps) != 2 or not all((x.get("athlete") or {}).get("displayName") for x in cps):
        raise SystemExit("error: not a singles match with two named players")
    stype = (c.get("status") or {}).get("type", {})
    detail = " ".join(str(stype.get(k, "")) for k in ("detail", "shortDetail", "description")).upper()
    sets = [[float(ls.get("value", 0) or 0) for ls in (x.get("linescores") or [])] for x in cps]
    best_of = ((c.get("format") or {}).get("regulation") or {}).get("periods")
    out = {"id": str(c.get("id")), "start_utc": _iso_z(c.get("date", "")), "date": c.get("date", "")[:10],
           "state": stype.get("state", ""), "completed": bool(stype.get("completed")),
           "a": cps[0]["athlete"]["displayName"], "b": cps[1]["athlete"]["displayName"],
           "best_of": ((c.get("format") or {}).get("regulation") or {}).get("periods"),
           "winner": "a" if cps[0].get("winner") else "b" if cps[1].get("winner") else None,
           "games_a": int(sum(sets[0])), "games_b": int(sum(sets[1])),
           "sets_a": sum(1 for x, y in zip(*sets) if x > y), "sets_b": sum(1 for x, y in zip(*sets) if y > x),
           "finish": "WO" if ("WALKOVER" in detail or "W/O" in detail) else
                     "RET" if ("RET" in detail or "RETIRED" in detail or "ABANDON" in detail) else "REG",
           "source": source}
    # a completed match is scored for games only when its sets form a legal finished match
    if out["finish"] == "REG" and out["completed"] and not legal_match(sets, best_of):
        out["finish"] = "WO" if out["games_a"] + out["games_b"] == 0 else "RET"
    return out


def legal_set(x: float, y: float) -> bool:
    hi, lo = max(x, y), min(x, y)
    return (hi >= 6 and hi - lo >= 2) or (hi == 7 and lo == 6)


def legal_match(sets: list[list[float]], best_of) -> bool:
    """Every set is a finished set and the winner reached best_of//2 + 1 sets (best of 3 when unknown)."""
    need = int(best_of or 3) // 2 + 1
    pairs = list(zip(*sets)) if len(sets) == 2 else []
    if not pairs or not all(legal_set(x, y) for x, y in pairs):
        return False
    wa, wb = sum(1 for x, y in pairs if x > y), sum(1 for x, y in pairs if y > x)
    return max(wa, wb) == need


def espn_tennis_match(tour: str, comp_id: str, date: str, force: bool = False) -> dict:
    d = dt.date.fromisoformat(date[:10])
    for day in (d, d - dt.timedelta(days=1), d + dt.timedelta(days=1)):
        for ev in espn_day(f"tennis/{tour}", day, force=force):
            for grp in ev.get("groupings", []):
                for c in grp.get("competitions", []):
                    if str(c.get("id")) == str(comp_id):
                        return parse_tennis_comp(c, ESPN.format(path=f"tennis/{tour}", day=f"{day:%Y%m%d}"))
    raise SystemExit(f"error: tennis match {comp_id} not found on the {tour} scoreboard around {date}")


CRICKET_SCORE_RE = re.compile(r"^\s*(\d+)(?:/(\d+))?\s*(?:\((.*)\))?")


def parse_cricket_score(s: str) -> dict | None:
    """ESPN cricket competitor score: '169/7', '160/8 (20 ov, target 170)', '142 (18.3 ov)' (no wickets
    shown = all out). Returns runs, wickets, overs (None when not shown) and whether it was a chase."""
    m = CRICKET_SCORE_RE.match(str(s or ""))
    if not m:
        return None
    paren = (m.group(3) or "").lower()
    ov = re.search(r"([\d.]+)\s*ov", paren)
    return {"runs": int(m.group(1)), "wkts": int(m.group(2)) if m.group(2) is not None else 10,
            "overs": float(ov.group(1)) if ov else None, "chase": "target" in paren}


def parse_cricket_event(ev: dict, scheduled_overs: int, source: str) -> dict:
    comp = (ev.get("competitions") or [{}])[0]
    cps = comp.get("competitors", [])
    if len(cps) != 2:
        raise SystemExit("error: cricket event without two competitors")
    stype = (comp.get("status") or ev.get("status") or {}).get("type", {})
    text = " ".join(str(stype.get(k, "")) for k in ("detail", "shortDetail", "description")).upper()
    sc = [parse_cricket_score(x.get("score")) for x in cps]
    out = {"id": str(ev.get("id")), "start_utc": _iso_z(ev.get("date", "")), "date": ev.get("date", "")[:10],
           "state": stype.get("state", ""), "completed": bool(stype.get("completed")),
           "a": cps[0]["team"].get("displayName", ""), "b": cps[1]["team"].get("displayName", ""),
           "winner": "a" if cps[0].get("winner") else "b" if cps[1].get("winner") else None,
           "no_result": "NO RESULT" in text or "ABANDON" in text, "tie": "TIED" in text or "TIE" in text.split(),
           "first_innings_runs": None, "first_innings_team": None, "first_innings_valid": False, "source": source}
    # first innings = the side that did not chase; ambiguous (both or neither chasing) = unknown
    firsts = [i for i in (0, 1) if sc[i] and not sc[i]["chase"]]
    if len(firsts) == 1 and sc[1 - firsts[0]] and sc[1 - firsts[0]]["chase"]:
        f, ch = sc[firsts[0]], sc[1 - firsts[0]]
        dls = any(k in text for k in ("DLS", "D/L", "DUCKWORTH", "REDUCED"))
        # Uncensored and full-length, conservatively: all out; or its overs are shown and complete; or its
        # overs are not shown but the chase batted the full scheduled overs (so the match was not shortened).
        # A DLS or reduced-overs note invalidates any innings that was not all out. Anything else: unscored.
        if f["wkts"] >= 10:
            full = True
        elif f["overs"] is not None:
            full = abs(f["overs"] - scheduled_overs) < 1e-9 and not dls
        else:
            full = ch["overs"] is not None and abs(ch["overs"] - scheduled_overs) < 1e-9 and not dls
        out.update({"first_innings_runs": f["runs"], "first_innings_team": "a" if firsts[0] == 0 else "b",
                    "first_innings_valid": full})
    return out


def espn_cricket_match(path: str, event_id: str, date: str, scheduled_overs: int, force: bool = False) -> dict:
    d = dt.date.fromisoformat(date[:10])
    for day in (d, d - dt.timedelta(days=1), d + dt.timedelta(days=1)):
        for ev in espn_day(path, day, force=force):
            if str(ev.get("id")) == str(event_id):
                return parse_cricket_event(ev, scheduled_overs, ESPN.format(path=path, day=f"{day:%Y%m%d}"))
    raise SystemExit(f"error: cricket event {event_id} not found on the {path} scoreboard around {date}")


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
