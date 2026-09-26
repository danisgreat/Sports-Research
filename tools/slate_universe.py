#!/usr/bin/env python3
"""Event universe — declare the day's slate before any card (C-EVENT-UNIVERSE, added 2026-09-26).

Why. Every card so far was for an event the operator happened to ask about. The settled record
is therefore a self-selected sample: its calibration and skill figures describe the events that
were chosen, not a competition. The 2026-09-26 review named this the largest untested design
gap (C-NT-ALL-UNIVERSE had a count of 0). A declared universe fixes the population *before*
anything is known about the events beyond the official schedule, so every scored figure can be
reported against it, and events that were never carded are visible as SKIPPED or MISSING rather
than silently absent.

What it does.
  declare  Fetch the official schedule for each league on one venue-local date, keep the events
           that have not started, optionally draw a seeded random sample per league, and write
           universe/UNIVERSE_<date>[_<tag>].json with a SHA-256 of the declaration. Nothing in
           the declaration may be edited afterwards; `status` re-verifies the hash.
  skip     Append a skip record (event, reason, UTC time) to the universe file. Only the "skips"
           list changes; the declaration hash is unaffected.
  status   Report coverage: CARDED (the event ID appears in a named log), SKIPPED (with its
           reason) or MISSING. Coverage below 100% is reported, never hidden.

Market-blind by construction: only schedule fields are read. ESPN keys that carry prices are
dropped on load (the same QUARANTINED_KEYS as receipts.py).

Usage:
  python tools/slate_universe.py declare --date 2026-09-27 --league mlb --league epl [--max-per-league 4] [--seed 20260927] [--tag am]
  python tools/slate_universe.py skip universe/UNIVERSE_2026-09-27.json --event mlb:824703 --reason GATE_FAIL:BB-P2
  python tools/slate_universe.py status universe/UNIVERSE_2026-09-27.json --log "Mini logs (to be sent to actual log later)/<active>/<log>.md"
  --fixture-dir DIR   read schedule JSON from DIR/<league>_<YYYYMMDD>.json instead of the network (tests, replay)
  --now ISO           override the clock (tests)

Standard library only. Network: MLB statsapi schedule; ESPN site API scoreboard (one date per call,
no browser User-Agent).
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import random
import re
import sys
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
UNIVERSE_DIR = REPO / "universe"

QUARANTINED_KEYS = {"pickcenter", "odds", "againstTheSpread", "winprobability", "oddsPartners",
                    "predictor", "betting", "bettingOdds"}

MLB_SCHEDULE = "https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={date}&hydrate=venue"
ESPN_SCOREBOARD = "https://site.api.espn.com/apis/site/v2/sports/{path}/scoreboard?dates={ymd}"

# League key -> ESPN path. "mlb" uses statsapi. Any other ESPN path can be passed as espn:<path>.
ESPN_LEAGUES = {
    "nba": "basketball/nba", "wnba": "basketball/wnba", "nbl": "basketball/nbl",
    "nhl": "hockey/nhl", "epl": "soccer/eng.1", "ucl": "soccer/uefa.champions",
    "uel": "soccer/uefa.europa", "nfl": "football/nfl", "ncaaf": "football/college-football",
    "afl": "australian-football/afl", "nrl": "rugby-league/3",
}

SKIP_REASONS = ("STARTED_BEFORE_FREEZE", "POSTPONED", "CANCELLED", "GATE_FAIL", "SOURCE_UNAVAILABLE",
                "OPERATOR_CAPACITY", "OTHER")


# --------------------------------------------------------------------------- fetching

def _strip(obj):
    if isinstance(obj, dict):
        return {k: _strip(v) for k, v in obj.items() if k not in QUARANTINED_KEYS}
    if isinstance(obj, list):
        return [_strip(x) for x in obj]
    return obj


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return _strip(json.loads(raw.decode("utf-8")))


def load_schedule(league: str, date: str, fixture_dir: str | None) -> dict:
    ymd = date.replace("-", "")
    if fixture_dir:
        path = Path(fixture_dir) / f"{league.replace(':', '_').replace('/', '_')}_{ymd}.json"
        return _strip(json.loads(path.read_text(encoding="utf-8")))
    if league == "mlb":
        return fetch_json(MLB_SCHEDULE.format(date=date))
    return fetch_json(ESPN_SCOREBOARD.format(path=espn_path(league), ymd=ymd))


def espn_path(league: str) -> str:
    if league.startswith("espn:"):
        return league[len("espn:"):]
    if league in ESPN_LEAGUES:
        return ESPN_LEAGUES[league]
    raise SystemExit(f"error: unknown league {league!r}; use one of {sorted(ESPN_LEAGUES) + ['mlb']} or espn:<path>")


# --------------------------------------------------------------------------- parsing

def parse_iso(s: str) -> dt.datetime:
    s = s.replace("Z", "+00:00")
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}\+00:00", s):
        s = s.replace("+00:00", ":00+00:00")
    t = dt.datetime.fromisoformat(s)
    if t.tzinfo is None:
        raise ValueError(f"timestamp without a timezone: {s}")
    return t


def events_from(league: str, payload: dict) -> list[dict]:
    """Normalise a schedule payload to [{id, league, start_utc, home, away, venue, state}]."""
    out = []
    if league == "mlb":
        for d in payload.get("dates", []):
            for g in d.get("games", []):
                state = {"Preview": "pre", "Live": "in", "Final": "post"}.get(
                    g.get("status", {}).get("abstractGameState", ""), "unknown")
                detailed = g.get("status", {}).get("detailedState", "")
                if detailed in ("Postponed", "Cancelled", "Suspended"):
                    state = detailed.lower()
                out.append({"id": f"mlb:{g['gamePk']}", "league": league,
                            "start_utc": parse_iso(g["gameDate"]).strftime("%Y-%m-%dT%H:%M:%SZ"),
                            "home": g["teams"]["home"]["team"]["name"],
                            "away": g["teams"]["away"]["team"]["name"],
                            "venue": g.get("venue", {}).get("name", ""), "state": state})
        return out
    for ev in payload.get("events", []):
        comp = (ev.get("competitions") or [{}])[0]
        teams = {c.get("homeAway"): c.get("team", {}).get("displayName", "") for c in comp.get("competitors", [])}
        state = ev.get("status", {}).get("type", {}).get("state", "unknown")
        detail = ev.get("status", {}).get("type", {}).get("name", "")
        if detail in ("STATUS_POSTPONED", "STATUS_CANCELED", "STATUS_CANCELLED"):
            state = "postponed" if "POSTPONED" in detail else "cancelled"
        out.append({"id": f"{league}:{ev['id']}", "league": league,
                    "start_utc": parse_iso(ev["date"]).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "home": teams.get("home", ""), "away": teams.get("away", ""),
                    "venue": comp.get("venue", {}).get("fullName", ""), "state": state})
    return out


# --------------------------------------------------------------------------- declaration

def declaration_digest(decl: dict) -> str:
    """SHA-256 over the declaration only (not the skips), in a canonical JSON form."""
    body = json.dumps({k: decl[k] for k in ("date", "leagues", "seed", "max_per_league", "declared_at_utc",
                                            "events", "excluded")},
                      sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def declare(date: str, leagues: list[str], now: dt.datetime, seed: int | None, max_per_league: int | None,
            fixture_dir: str | None) -> dict:
    events, excluded = [], []
    seed = seed if seed is not None else int(date.replace("-", ""))
    rng = random.Random(seed)
    for lg in leagues:
        evs = events_from(lg, load_schedule(lg, date, fixture_dir))
        eligible = []
        for e in evs:
            if e["state"] != "pre":
                excluded.append({**e, "why": f"STATE_{e['state'].upper()}"})
            elif parse_iso(e["start_utc"]) <= now:
                excluded.append({**e, "why": "START_TIME_PASSED"})
            else:
                eligible.append(e)
        eligible.sort(key=lambda e: (e["start_utc"], e["id"]))
        if max_per_league and len(eligible) > max_per_league:
            chosen = sorted(rng.sample(eligible, max_per_league), key=lambda e: (e["start_utc"], e["id"]))
            for e in eligible:
                if e not in chosen:
                    excluded.append({**e, "why": "NOT_SAMPLED"})
            eligible = chosen
        events += eligible
    decl = {"schema": "C-EVENT-UNIVERSE/1", "date": date, "leagues": leagues, "seed": seed,
            "max_per_league": max_per_league, "declared_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "events": events, "excluded": excluded, "skips": []}
    decl["declaration_sha256"] = declaration_digest(decl)
    return decl


def write_new(path: Path, decl: dict) -> None:
    if path.exists():
        raise SystemExit(f"error: {path} already exists; a declared universe is never overwritten (use --tag)")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(decl, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_universe(path: Path) -> dict:
    u = json.loads(path.read_text(encoding="utf-8"))
    if declaration_digest(u) != u.get("declaration_sha256"):
        raise SystemExit(f"error: {path} declaration was edited after it was declared (hash mismatch)")
    return u


def add_skip(path: Path, event: str, reason: str, now: dt.datetime, note: str = "") -> dict:
    u = load_universe(path)
    ids = {e["id"] for e in u["events"]}
    if event not in ids:
        raise SystemExit(f"error: {event} is not in the declared universe")
    head = reason.split(":", 1)[0]
    if head not in SKIP_REASONS:
        raise SystemExit(f"error: reason must start with one of {SKIP_REASONS}")
    u["skips"].append({"id": event, "reason": reason, "note": note,
                       "recorded_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ")})
    path.write_text(json.dumps(u, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return u


def coverage(u: dict, log_texts: list[str]) -> list[dict]:
    blob = "\n".join(log_texts)
    skips = {}
    for s in u.get("skips", []):
        skips.setdefault(s["id"], s)
    rows = []
    for e in u["events"]:
        raw_id = e["id"].split(":", 1)[1]
        # An event counts as carded when its native ID appears as a whole token in a log.
        carded = re.search(rf"(?<![0-9A-Za-z]){re.escape(raw_id)}(?![0-9A-Za-z])", blob) is not None
        if carded:
            status = "CARDED"
        elif e["id"] in skips:
            status = "SKIPPED: " + skips[e["id"]]["reason"]
        else:
            status = "MISSING"
        rows.append({**e, "status": status})
    return rows


def render_declaration(u: dict) -> str:
    lines = [f"Universe {u['date']} — leagues {', '.join(u['leagues'])}; seed {u['seed']}; "
             f"max per league {u['max_per_league'] or 'all'}; declared {u['declared_at_utc']}",
             f"Declaration SHA-256: `{u['declaration_sha256']}`", "",
             "| Event | League | Start (UTC) | Away @ Home | Venue |", "|---|---|---|---|---|"]
    for e in u["events"]:
        lines.append(f"| `{e['id']}` | {e['league']} | {e['start_utc']} | {e['away']} @ {e['home']} | {e['venue']} |")
    lines.append(f"\nIn scope: {len(u['events'])}. Excluded at declaration: {len(u['excluded'])} "
                 "(already started, postponed, or not sampled).")
    return "\n".join(lines)


def render_status(rows: list[dict], u: dict) -> str:
    n = len(rows)
    carded = sum(r["status"] == "CARDED" for r in rows)
    skipped = sum(r["status"].startswith("SKIPPED") for r in rows)
    missing = n - carded - skipped
    lines = [f"Universe {u['date']} (`{u['declaration_sha256'][:12]}…`): {n} events — "
             f"**{carded} carded, {skipped} skipped, {missing} missing**; coverage "
             f"{(carded / n if n else 0):.0%}.", "",
             "| Event | Away @ Home | Status |", "|---|---|---|"]
    for r in rows:
        lines.append(f"| `{r['id']}` | {r['away']} @ {r['home']} | {r['status']} |")
    if missing:
        lines.append("\nEvery MISSING event needs a card or a `skip` record with a reason (C-EVENT-UNIVERSE).")
    return "\n".join(lines)


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--now", help="override the clock (ISO, with timezone)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("declare")
    d.add_argument("--date", required=True, help="venue-local date YYYY-MM-DD")
    d.add_argument("--league", action="append", required=True)
    d.add_argument("--max-per-league", type=int)
    d.add_argument("--seed", type=int)
    d.add_argument("--tag", default="")
    d.add_argument("--fixture-dir")
    d.add_argument("--out-dir", default=str(UNIVERSE_DIR))
    s = sub.add_parser("skip")
    s.add_argument("universe")
    s.add_argument("--event", required=True)
    s.add_argument("--reason", required=True)
    s.add_argument("--note", default="")
    st = sub.add_parser("status")
    st.add_argument("universe")
    st.add_argument("--log", action="append", default=[])
    args = ap.parse_args(argv)
    now = parse_iso(args.now) if args.now else dt.datetime.now(dt.timezone.utc)

    if args.cmd == "declare":
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
            raise SystemExit("error: --date must be YYYY-MM-DD")
        u = declare(args.date, args.league, now, args.seed, args.max_per_league, args.fixture_dir)
        name = f"UNIVERSE_{args.date}{'_' + args.tag if args.tag else ''}.json"
        out = Path(args.out_dir) / name
        write_new(out, u)
        print(render_declaration(u))
        print(f"\nWritten: {out}")
        return 0
    if args.cmd == "skip":
        u = add_skip(Path(args.universe), args.event, args.reason, now, args.note)
        print(f"Skip recorded for {args.event}: {args.reason} ({len(u['skips'])} skip record(s)).")
        return 0
    u = load_universe(Path(args.universe))
    texts = [Path(p).read_text(encoding="utf-8-sig") for p in args.log]
    print(render_status(coverage(u, texts), u))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
