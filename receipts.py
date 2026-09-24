#!/usr/bin/env python3
"""Pregame and settlement receipts from field-owner JSON (added 2026-09-25).

Why this exists: the recurring failures in LEARNING_REGISTER §"2026-09-25 audit closure" B are
retrieval failures, not modelling failures. Examples: M19/M25, lineups labelled "confirmed" that
were never retrieved; M30, city wind used instead of the gamefeed; M26, a process record that was
written, not read. This tool reads the record and prints every fact with its endpoint and
retrieval time. That is the receipt format required by C-PROCESS-RECORD-PROVENANCE, C-LINEUP-DIFF,
S-1 Rev 2 official-lineup precedence and the MLB gamefeed-weather rule.

Market-blind by construction: ESPN summary keys that carry prices or market-derived numbers are
deleted on load (QUARANTINED_KEYS) and never printed. The NHL score payload's `oddsPartners` key is
never read.

Usage:
  python receipts.py pregame mlb <gamePk>
  python receipts.py pregame espn <sport/league> <eventId>   e.g. basketball/wnba 401857213
  python receipts.py settle  mlb <gamePk> [--card-away "A;B;..."] [--card-home "..."] [--card-sp-away X] [--card-sp-home Y]
  python receipts.py settle  nhl <gameId> [--card-goalie-away X] [--card-goalie-home Y]
  python receipts.py settle  espn <sport/league> <eventId> [--card-away "..."] [--card-home "..."]
  --fixture PATH   read JSON from a file instead of the network (tests / offline replay)
  --now ISO        override the retrieval clock (tests)

It does not grade contracts or create a terminal lineage count on its own. The settlement gate
(CONTROLS.md C-FINAL3) still needs three independent lineages. The receipt is one lineage and
names it.
"""
from __future__ import annotations

import argparse
import gzip
import json
import re
import subprocess
import sys
import unicodedata
import urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

AEST = ZoneInfo("Australia/Brisbane")  # fixed UTC+10, the repository's "AEST" convention

QUARANTINED_KEYS = {"pickcenter", "odds", "againstTheSpread", "winprobability", "oddsPartners",
                    "predictor", "betting", "bettingOdds"}

MLB_FEED = "https://statsapi.mlb.com/api/v1.1/game/{pk}/feed/live"
NHL_BOX = "https://api-web.nhle.com/v1/gamecenter/{gid}/boxscore"
NHL_LANDING = "https://api-web.nhle.com/v1/gamecenter/{gid}/landing"
ESPN_SUMMARY = "https://site.api.espn.com/apis/site/v2/sports/{path}/summary?event={eid}"


# --------------------------------------------------------------------------- fetching

def _strip_quarantined(obj):
    if isinstance(obj, dict):
        return {k: _strip_quarantined(v) for k, v in obj.items() if k not in QUARANTINED_KEYS}
    if isinstance(obj, list):
        return [_strip_quarantined(x) for x in obj]
    return obj


def fetch_json(url: str, use_curl: bool = False) -> dict:
    """GET JSON. No browser User-Agent (ESPN rejects spoofed agents); NHL api-web needs curl."""
    if use_curl:
        r = subprocess.run(["curl", "-s", "--compressed", "-m", "60", url], capture_output=True, check=False)
        raw = r.stdout
    else:
        req = urllib.request.Request(url, headers={"Accept-Encoding": "gzip"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return _strip_quarantined(json.loads(raw.decode("utf-8")))


def load(url: str, fixture: str | None, use_curl: bool = False) -> dict:
    if fixture:
        with open(fixture, encoding="utf-8") as fh:
            return _strip_quarantined(json.load(fh))
    return fetch_json(url, use_curl=use_curl)


# --------------------------------------------------------------------------- helpers

def utc_iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def aest(dt: datetime) -> str:
    return dt.astimezone(AEST).strftime("%Y-%m-%d %H:%M AEST")


def parse_iso(s: str) -> datetime:
    s = s.replace("Z", "+00:00")
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}\+00:00", s):
        s = s.replace("+00:00", ":00+00:00")
    return datetime.fromisoformat(s)


def norm_name(name: str) -> str:
    """Casefold, strip accents and punctuation: 'Andrés Chaparro' -> 'andres chaparro'."""
    s = unicodedata.normalize("NFKD", name or "")
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"[^a-zA-Z ]+", " ", s).casefold()
    return re.sub(r"\s+", " ", s).strip()


def name_match(card_name: str, official: list[str]) -> str | None:
    """Return the official name matching a card name, by full normalised name, then surname + initial,
    then unique surname. None when no official name matches."""
    c = norm_name(card_name)
    if not c:
        return None
    offs = {norm_name(o): o for o in official}
    if c in offs:
        return offs[c]
    parts = c.split()
    sur = parts[-1]
    init = parts[0][0] if len(parts) > 1 else None
    cands = [o for n, o in offs.items() if n.split() and n.split()[-1] == sur]
    if init:
        narrowed = [o for o in cands if norm_name(o).split()[0][0] == init]
        if len(narrowed) == 1:
            return narrowed[0]
    if len(cands) == 1:
        return cands[0]
    return None


def lineup_diff(card: list[str], official: list[str]) -> dict:
    matched, missing = [], []
    for n in card:
        m = name_match(n, official)
        (matched if m else missing).append((n, m))
    return {"card_count": len(card), "matched": len(matched), "not_in_official": [n for n, _ in missing]}


def split_names(s: str | None) -> list[str]:
    return [x.strip() for x in (s or "").split(";") if x.strip()]


def game_state(kind: str, raw: str, start: datetime | None, now: datetime) -> str:
    """Map a feed status to PREGAME / LIVE / FINAL / POSTPONED / UNKNOWN (timezone game-state rule)."""
    r = (raw or "").upper()
    if kind == "mlb":
        if r in {"F", "O", "FINAL", "GAME OVER", "COMPLETED EARLY"} or r.startswith("FINAL"):
            return "FINAL"
        if r in {"D", "POSTPONED"} or "POSTPONED" in r or "SUSPENDED" in r:
            return "POSTPONED_OR_SUSPENDED"
        if r in {"I", "IN PROGRESS", "M", "MANAGER CHALLENGE"} or "PROGRESS" in r or "DELAY" in r:
            return "LIVE"
    if kind == "nhl":
        if r in {"FINAL", "OFF"}:
            return "FINAL"
        if r in {"LIVE", "CRIT"}:
            return "LIVE"
    if kind == "espn":
        if r in {"POST"}:
            return "FINAL"
        if r in {"IN"}:
            return "LIVE"
    if start is not None:
        return "PREGAME" if now < start else "START_CROSSED_STATUS_NOT_FINAL"
    return "UNKNOWN"


class Receipt:
    """Accumulates sourced facts; renders Markdown."""

    def __init__(self, title: str, now: datetime):
        self.title = title
        self.now = now
        self.lines: list[str] = []
        self.sources: list[str] = []

    def src(self, url: str) -> int:
        if url not in self.sources:
            self.sources.append(url)
        return self.sources.index(url) + 1

    def fact(self, label: str, value, url: str):
        k = self.src(url)
        self.lines.append(f"| {label} | {value} | [S{k}] |")

    def render(self) -> str:
        out = [f"#### {self.title}", "",
               f"Retrieved {utc_iso(self.now)} ({aest(self.now)}). Every fact below is read from the named "
               "endpoint (C-PROCESS-RECORD-PROVENANCE); none is typed from memory or a recap.", "",
               "| Fact | Value | Source |", "|---|---|---|"]
        out += self.lines
        out += ["", "Sources:"]
        out += [f"- [S{i}] `{u}` — retrieved {utc_iso(self.now)}" for i, u in enumerate(self.sources, 1)]
        return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- MLB

def _mlb_starters(team_box: dict) -> list[tuple[str, str, str]]:
    """(order slot, name, position) for players whose battingOrder ends in '00' (the starters)."""
    out = []
    for pid in team_box.get("battingOrder", []) or []:
        p = team_box["players"].get(f"ID{pid}", {})
        bo = str(p.get("battingOrder", ""))
        if bo.endswith("00"):
            out.append((bo[0], p["person"]["fullName"], (p.get("position") or {}).get("abbreviation", "")))
    # battingOrder holds the *current* occupant; recover replaced starters from players map
    have = {s for s, _, _ in out}
    for p in team_box.get("players", {}).values():
        bo = str(p.get("battingOrder", ""))
        if bo.endswith("00") and bo[0] not in have:
            out.append((bo[0], p["person"]["fullName"], (p.get("position") or {}).get("abbreviation", "")))
            have.add(bo[0])
    return sorted(out, key=lambda x: int(x[0]))


def mlb_receipt(pk: str, mode: str, args, now: datetime) -> str:
    url = MLB_FEED.format(pk=pk)
    d = load(url, args.fixture)
    gd, ld = d["gameData"], d["liveData"]
    away, home = gd["teams"]["away"], gd["teams"]["home"]
    start = parse_iso(gd["datetime"]["dateTime"])
    status = gd["status"]
    state = game_state("mlb", status.get("codedGameState") if status.get("codedGameState") in {"F", "O", "D"}
                       else status.get("detailedState", ""), start, now)
    r = Receipt(f"{'Pregame' if mode == 'pregame' else 'Settlement'} receipt — MLB gamePk {pk}: "
                f"{away.get('name')} @ {home.get('name')}", now)
    r.fact("Scheduled first pitch", f"{utc_iso(start)} / {aest(start)} (venue: {gd['venue'].get('name')})", url)
    r.fact("Feed status", f"{status.get('detailedState')} (`{status.get('codedGameState')}`) → **{state}**", url)
    pp = gd.get("probablePitchers", {})
    r.fact("Probable / starting pitchers", f"{(pp.get('away') or {}).get('fullName', 'NOT_LISTED')} (away) v "
           f"{(pp.get('home') or {}).get('fullName', 'NOT_LISTED')} (home)", url)
    w = gd.get("weather") or {}
    r.fact("Gamefeed weather", (f"{w.get('condition', '?')}, {w.get('temp', '?')}°F, wind {w.get('wind', '?')}"
                                if w else "WEATHER_NOT_YET_PUBLISHED (retry nearer first pitch; do not substitute a city forecast)"), url)
    box = ld.get("boxscore", {}).get("teams", {})
    for side, team in (("away", away), ("home", home)):
        st = _mlb_starters(box.get(side, {})) if box else []
        r.fact(f"Starting lineup — {team.get('abbreviation', side)}",
               "; ".join(f"{s}. {n} {p}" for s, n, p in st) if st else
               "LINEUPS_NOT_YET_PUBLISHED — a card may not label any lineup reported/confirmed (S-1 Rev 2)", url)
    offs = ld.get("boxscore", {}).get("officials", [])
    if offs:
        r.fact("Umpires", "; ".join(f"{o['officialType']}: {o['official']['fullName']}" for o in offs), url)
    if mode == "settle":
        ls = ld.get("linescore", {})
        t = ls.get("teams", {})
        inn = ls.get("innings", [])
        r.fact("Final score", f"{away.get('abbreviation')} {t.get('away', {}).get('runs')} – "
               f"{t.get('home', {}).get('runs')} {home.get('abbreviation')}; innings played {ls.get('currentInning')} "
               f"(scheduled {ls.get('scheduledInnings')})", url)
        r.fact("Linescore (away/home by inning)",
               " ".join(f"{i['num']}:{i['away'].get('runs', '-')}/{i['home'].get('runs', '-')}" for i in inn), url)
        if inn and len(inn) > (ls.get("scheduledInnings") or 9):
            sch = ls.get("scheduledInnings") or 9
            a9 = sum(i["away"].get("runs", 0) or 0 for i in inn[:sch])
            h9 = sum(i["home"].get("runs", 0) or 0 for i in inn[:sch])
            r.fact("Score after regulation", f"{a9}–{h9} (extras played; a regulation-only contract settles here)", url)
        dec = ld.get("decisions", {})
        if dec:
            r.fact("Decisions", "; ".join(f"{k}: {v.get('fullName')}" for k, v in dec.items()), url)
        info = {x.get("label"): x.get("value") for x in ld.get("boxscore", {}).get("info", [])}
        for lab in ("Weather", "Wind", "First pitch", "T"):
            if info.get(lab):
                r.fact(f"Box info — {lab}", info[lab].rstrip("."), url)
        for side, team, card_arg, sp_arg in (("away", away, args.card_away, args.card_sp_away),
                                             ("home", home, args.card_home, args.card_sp_home)):
            official = [n for _, n, _ in _mlb_starters(box.get(side, {}))]
            if card_arg:
                dff = lineup_diff(split_names(card_arg), official)
                r.fact(f"C-LINEUP-DIFF — {team.get('abbreviation')}",
                       f"{dff['matched']}/{dff['card_count']} card-named starters started; not in official lineup: "
                       f"{', '.join(dff['not_in_official']) or 'none'}", url)
            if sp_arg:
                sp_id = (box.get(side, {}).get("pitchers") or [None])[0]
                sp = box.get(side, {}).get("players", {}).get(f"ID{sp_id}", {}).get("person", {}).get("fullName")
                ok = bool(sp and name_match(sp_arg, [sp]))
                r.fact(f"C-LINEUP-DIFF — {team.get('abbreviation')} starting pitcher",
                       f"card {sp_arg} / official {sp or 'UNKNOWN'} → {'MATCH' if ok else '**MISMATCH (LINEUP_CLAIM_FALSE if a Rank-1 driver)**'}", url)
    return r.render()


# --------------------------------------------------------------------------- NHL

def nhl_receipt(gid: str, args, now: datetime) -> str:
    burl, lurl = NHL_BOX.format(gid=gid), NHL_LANDING.format(gid=gid)
    fx_box = fx_land = None
    if args.fixture:
        with open(args.fixture, encoding="utf-8") as fh:
            both = json.load(fh)
        fx_box, fx_land = both["boxscore"], both["landing"]
    b = _strip_quarantined(fx_box) if fx_box else fetch_json(burl, use_curl=True)
    l = _strip_quarantined(fx_land) if fx_land else fetch_json(lurl, use_curl=True)
    start = parse_iso(b["startTimeUTC"])
    state = game_state("nhl", b.get("gameState", ""), start, now)
    a, h = b["awayTeam"], b["homeTeam"]
    r = Receipt(f"Settlement receipt — NHL game {gid}: {a.get('abbrev')} @ {h.get('abbrev')} "
                f"(gameType {b.get('gameType')}: 1 = preseason, 2 = regular, 3 = playoffs)", now)
    r.fact("Scheduled start", f"{utc_iso(start)} / {aest(start)}", burl)
    r.fact("Feed status", f"{b.get('gameState')} → **{state}**", burl)
    r.fact("Final score", f"{a.get('abbrev')} {a.get('score')} – {h.get('score')} {h.get('abbrev')}; "
           f"decided in {(b.get('gameOutcome') or {}).get('lastPeriodType', '?')}", burl)
    reg_a = reg_h = 0
    en = []
    for p in l.get("summary", {}).get("scoring", []):
        pd = p.get("periodDescriptor", {})
        goals = p.get("goals", [])
        txt = []
        for g in goals:
            ta = g.get("teamAbbrev")
            ta = ta.get("default") if isinstance(ta, dict) else ta
            who = (g.get("name") or {}).get("default") if isinstance(g.get("name"), dict) else g.get("name")
            mod = g.get("goalModifier")
            txt.append(f"{ta} {g.get('timeInPeriod')} {who} ({g.get('strength')}{', EMPTY-NET' if mod == 'empty-net' else ''})")
            if mod == "empty-net":
                en.append(f"{ta} P{pd.get('number')} {g.get('timeInPeriod')}")
            if pd.get("periodType") == "REG":
                if ta == a.get("abbrev"):
                    reg_a += 1
                elif ta == h.get("abbrev"):
                    reg_h += 1
        r.fact(f"Goals — period {pd.get('number')} ({pd.get('periodType')})", "; ".join(txt) or "none", lurl)
    r.fact("Score after regulation (60 min)", f"{reg_a}–{reg_h}", lurl)
    r.fact("Empty-net goals", ", ".join(en) or "none", lurl)
    pbs = b.get("playerByGameStats", {})
    for side, team, card_g in (("awayTeam", a, args.card_goalie_away), ("homeTeam", h, args.card_goalie_home)):
        gl = pbs.get(side, {}).get("goalies", [])
        played = [(g["name"]["default"], g.get("toi")) for g in gl if g.get("toi") not in (None, "00:00")]
        r.fact(f"Goalies who played — {team.get('abbrev')}", "; ".join(f"{n} {t}" for n, t in played) or "none", burl)
        if card_g:
            ok = any(name_match(card_g, [n]) for n, _ in played)
            r.fact(f"C-LINEUP-DIFF — {team.get('abbrev')} goalie",
                   f"card {card_g} → {'PLAYED' if ok else '**DID NOT PLAY (LINEUP_CLAIM_FALSE if a Rank-1 driver)**'}", burl)
    return r.render()


# --------------------------------------------------------------------------- ESPN (basketball, soccer, hockey, NBL, WNBA ...)

def espn_receipt(path: str, eid: str, mode: str, args, now: datetime) -> str:
    url = ESPN_SUMMARY.format(path=path, eid=eid)
    d = load(url, args.fixture)
    comp = d["header"]["competitions"][0]
    start = parse_iso(comp.get("date") or d["header"].get("date"))
    stt = comp.get("status", {}).get("type", {})
    state = game_state("espn", stt.get("state", ""), start, now)
    cps = {c["homeAway"]: c for c in comp["competitors"]}
    aw, hm = cps.get("away", {}), cps.get("home", {})
    r = Receipt(f"{'Pregame' if mode == 'pregame' else 'Settlement'} receipt — ESPN {path} event {eid}: "
                f"{aw.get('team', {}).get('displayName')} @ {hm.get('team', {}).get('displayName')}", now)
    r.fact("Scheduled start", f"{utc_iso(start)} / {aest(start)}", url)
    r.fact("Feed status", f"{stt.get('name')} ({stt.get('detail')}) → **{state}**", url)
    if mode == "pregame":
        inj = d.get("injuries") or []
        rows = []
        for t in inj:
            for x in t.get("injuries", []):
                ath = (x.get("athlete") or {}).get("displayName")
                rows.append(f"{(t.get('team') or {}).get('abbreviation')}: {ath} — {x.get('status')} ({x.get('date', '')[:10]})")
        r.fact("Injury report", "; ".join(rows) or "none listed (absence of a listing is not confirmation of availability)", url)
        offs = (d.get("gameInfo") or {}).get("officials") or []
        if offs:
            r.fact("Officials", "; ".join(o.get("displayName", "") for o in offs), url)
        return r.render()
    r.fact("Final score", f"{aw.get('team', {}).get('abbreviation')} {aw.get('score')} – {hm.get('score')} "
           f"{hm.get('team', {}).get('abbreviation')}", url)
    for side, c in (("away", aw), ("home", hm)):
        r.fact(f"Period scores — {c.get('team', {}).get('abbreviation')}",
               " ".join(str(x.get("displayValue")) for x in c.get("linescores", [])) or "not published", url)
    for t in (d.get("boxscore") or {}).get("players", []) or []:
        abbr = t["team"]["abbreviation"]
        stats = (t.get("statistics") or [{}])[0]
        names = stats.get("names") or stats.get("labels") or []
        mi = names.index("MIN") if "MIN" in names else None
        starters, dnp = [], []
        for a in stats.get("athletes", []):
            nm = a["athlete"]["displayName"]
            if a.get("didNotPlay"):
                dnp.append(f"{nm} ({a.get('reason') or 'no reason given'})")
            elif a.get("starter"):
                mins = a.get("stats", [None] * (mi + 1 if mi is not None else 1))[mi] if mi is not None and a.get("stats") else "?"
                starters.append(f"{nm} {mins}m")
        r.fact(f"Starters (minutes) — {abbr}", "; ".join(starters) or "not published", url)
        r.fact(f"Did not play — {abbr}", "; ".join(dnp) or "none", url)
        side = "away" if abbr == aw.get("team", {}).get("abbreviation") else "home"
        card_arg = args.card_away if side == "away" else args.card_home
        if card_arg:
            official = [s.rsplit(" ", 1)[0] for s in starters]
            dff = lineup_diff(split_names(card_arg), official)
            r.fact(f"C-LINEUP-DIFF — {abbr}", f"{dff['matched']}/{dff['card_count']} card-named starters started; "
                   f"not in official starters: {', '.join(dff['not_in_official']) or 'none'}", url)
    return r.render()


# --------------------------------------------------------------------------- CLI

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["pregame", "settle"])
    ap.add_argument("lane", choices=["mlb", "nhl", "espn"])
    ap.add_argument("ids", nargs="+", help="gamePk | NHL gameId | <sport/league> <eventId>")
    ap.add_argument("--card-away")
    ap.add_argument("--card-home")
    ap.add_argument("--card-sp-away")
    ap.add_argument("--card-sp-home")
    ap.add_argument("--card-goalie-away")
    ap.add_argument("--card-goalie-home")
    ap.add_argument("--fixture")
    ap.add_argument("--now")
    args = ap.parse_args(argv)
    now = parse_iso(args.now) if args.now else datetime.now(timezone.utc)
    if args.lane == "mlb":
        out = mlb_receipt(args.ids[0], args.mode, args, now)
    elif args.lane == "nhl":
        if args.mode != "settle":
            ap.error("nhl pregame is not supported: NHL starting goalies are not published by the API before puck drop")
        out = nhl_receipt(args.ids[0], args, now)
    else:
        if len(args.ids) != 2:
            ap.error("espn lane needs <sport/league> <eventId>")
        out = espn_receipt(args.ids[0], args.ids[1], args.mode, args, now)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
