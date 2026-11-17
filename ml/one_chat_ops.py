"""Daily operations for several research chats at once (ONE-CHAT-v3 / v29.0).

    python -m ml one-chat prepare --message TODAY_CHAT1.txt --mini MINI7 --out PREP/MINI7 [--schedules SCHEDULES.csv]
    python -m ml one-chat register-requests --folder PREP/MINI7          register and publish every prepared request
    python -m ml one-chat seal --watch CHAT_MINIS                         seal each new card the moment it is saved
    python -m ml one-chat intake --from-seals --out research/one_chat/intake/<run>
    python -m ml one-chat templates --out research/external/templates

``prepare`` reads the owner's REQ-v5 messages exactly as written, one game per message, and drafts each game's request
(REQUEST.txt is the message itself), EVENT.csv, CONTRACTS.csv and a card skeleton whose card key, header names and
PICKS rows match the registered request, plus one CHAT_PACKET.md to paste into the chat. A message it cannot read is
listed in PREPARE_REPORT.csv with the reason; nothing is guessed. Nothing here prices, ranks or changes a card.
"""
from __future__ import annotations

import os
import re
import tempfile
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from ml import forecast_integrity as F
from ml import one_chat as O

TZ = {"AEDT": 11, "AEST": 10, "ACDT": 10.5, "ACST": 9.5, "AWST": 8, "NZDT": 13, "NZST": 12, "UTC": 0, "GMT": 0}
SPORTS = {"basketball": "Basketball", "soccer": "Soccer", "soccer/football": "Soccer", "football/soccer": "Soccer",
          "cricket": "Cricket", "tennis": "Tennis", "ice hockey": "Ice Hockey", "rugby league": "Rugby League",
          "rugby union": "Rugby Union", "american football": "American Football", "baseball": "Baseball",
          "australian rules": "Australian Rules", "afl": "Australian Rules", "aflw": "Australian Rules"}
# Settlement definitions per sport (GAME_REQUEST_TEMPLATE §1b and the sport rules): period, endpoint, unit.
ENDPOINTS = {
    "Basketball": ("FULL_GAME", "FULL_GAME_INCL_OT", "POINTS"),
    "Ice Hockey": ("FULL_GAME", "FULL_GAME_INCL_OT_SO", "GOALS"),
    "Rugby League": ("FULL_GAME", "FULL_GAME_INCL_GOLDEN_POINT", "POINTS"),
    "Rugby Union": ("FULL_GAME", "FULL_GAME_80_MINUTES", "POINTS"),
    "American Football": ("FULL_GAME", "FULL_GAME_INCL_OT", "POINTS"),
    "Australian Rules": ("FULL_GAME", "FULL_GAME_FINALS_INCL_EXTRA_TIME", "POINTS"),
    "Baseball": ("FULL_GAME", "FULL_GAME_INCL_EXTRAS", "RUNS"),
    "Tennis": ("FULL_MATCH", "COMPLETED_MATCH_RETIREMENT_PER_RULES_TENNIS_10_6", "GAMES"),
}
NUM = r"([+\-−]?\d+(?:\.\d+)?)"
REPORT_FIELDS = ("game", "card_key", "status", "detail")


class PrepareError(ValueError):
    pass


def _num(text: str) -> float:
    return float(text.replace("−", "-"))


def _line(value: float) -> str:
    return f"{value:g}" if value != int(value) else f"{int(value)}"


def split_messages(text: str) -> list[str]:
    """One message per game: each starts at a line beginning 'Upcoming'."""
    starts = [m.start() for m in re.finditer(r"(?mi)^\s*Upcoming\s", text)]
    return [text[a:b].strip("\n") for a, b in zip(starts, starts[1:] + [len(text)])]


def _start(line: str) -> str:
    m = re.search(r"Estimated Game Time Start:\s*(?P<when>.+?)\s*\b(?P<tz>" + "|".join(TZ) + r")\b", line, re.I)
    if not m:
        raise PrepareError("no 'Estimated Game Time Start: … AEDT' line")
    when = re.sub(r"^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*,?\s+", "", m["when"].strip().rstrip(","), flags=re.I)
    when = re.sub(r"(\d)(st|nd|rd|th)\b", r"\1", when)
    for fmt in ("%d %B %Y, %I:%M %p", "%d %B %Y %I:%M %p", "%d %b %Y, %I:%M %p", "%d %b %Y %I:%M %p", "%d %B %Y, %I:%M%p",
                "%d %B %Y %I:%M%p", "%d %B %Y, %H:%M", "%d %B %Y %H:%M", "%d %b %Y, %H:%M", "%d/%m/%Y %I:%M %p", "%d/%m/%Y %H:%M"):
        try:
            local = datetime.strptime(when, fmt)
            break
        except ValueError:
            continue
    else:
        raise PrepareError(f"start time not understood: {m['when']!r}")
    offset = timedelta(hours=TZ[m["tz"].upper()])
    return local.replace(tzinfo=timezone(offset)).isoformat()


def _side(team: str, home: str, away: str) -> str:
    t = team.strip().lower()
    if t == home.lower():
        return "HOME"
    if t == away.lower():
        return "AWAY"
    raise PrepareError(f"line names {team!r}, which is neither {home!r} nor {away!r} as written in the header")


def parse_message(message: str) -> dict:
    lines = [ln.strip() for ln in message.splitlines() if ln.strip()]
    m = re.match(r"Upcoming\s+(?P<sport>.+?)\s+(?:Game|Match)\s*:\s*(?P<a>.+?)\s+(?:vs\.?|v)\s+(?P<b>.+?),\s*(?P<rest>.+?),?$",
                 lines[0], re.I)
    if not m:
        raise PrepareError("header is not 'Upcoming <Sport> Game: Team A vs Team B, Competition,'")
    sport = SPORTS.get(m["sport"].strip().lower())
    if not sport:
        raise PrepareError(f"sport {m['sport']!r} has no request format; use the free-form route")
    a, b = m["a"].strip(), m["b"].strip()
    competition = m["rest"].split(",")[0].strip().rstrip(",")
    start = next((_start(ln) for ln in lines if ln.lower().startswith("estimated game time start")), None)
    if not start:
        raise PrepareError("no 'Estimated Game Time Start' line")
    home, away = a, b
    venue = next((ln.split(":", 1)[1].strip() for ln in lines if ln.lower().startswith("home side")), "")
    if venue and venue.split("(")[0].strip().lower() == b.lower():
        home, away = b, a
    elif venue and venue.split("(")[0].strip().lower() not in (a.lower(), "neutral") and not venue.lower().startswith("neutral"):
        raise PrepareError(f"home side {venue!r} is neither side named in the header")
    native = next((ln.split(":", 1)[1].strip() for ln in lines if re.match(r"(native|event)\s*id\s*:", ln, re.I)), "")
    schedule = next((ln.split(":", 1)[1].strip() for ln in lines if re.match(r"schedule\s*:", ln, re.I)), "")
    return dict(sport=sport, competition=competition, home=home, away=away, scheduled_start=start, native=native,
                schedule=schedule, neutral=venue.lower().startswith("neutral"), lines=lines[1:])


def contracts_for(game: dict) -> list[dict]:
    """Contract rows (both sides of every supplied line) from the message's own lines; each excerpt is the exact line."""
    sport, home, away = game["sport"], game["home"], game["away"]
    items, seen = [], set()

    def add(key, family, sides_lines, period, endpoint, unit, excerpt):
        if key in seen:
            raise PrepareError(f"two lines describe the same contract: {excerpt!r}")
        seen.add(key)
        items.append((game["lines"].index(excerpt), family, sides_lines, period, endpoint, unit, excerpt))

    period, endpoint, unit = ENDPOINTS.get(sport, ("", "", ""))
    side_lines = {}
    for ln in game["lines"]:
        low = ln.lower()
        if low.startswith(("estimated", "home side", "rank", "run", "native", "event id", "schedule", "format")) or " bats:" in low:
            continue
        if sport == "Soccer":
            m = re.search(r"Combined (First Half Goals|Total Goals|Total Corners)\s*:\s*Over/Under\s*" + NUM, ln, re.I)
            if not m:
                raise PrepareError(f"line not understood for soccer: {ln!r}")
            what, line = m[1].lower(), _line(_num(m[2]))
            spec = {"first half goals": ("PERIOD", "FIRST_HALF", "FIRST_HALF_INCL_STOPPAGE", "GOALS"),
                    "total goals": ("TOTAL", "FULL_MATCH", "REGULATION_90", "GOALS"),
                    "total corners": ("CORNERS", "FULL_MATCH", "REGULATION_90", "CORNERS")}[what]
            add(what, spec[0], [("OVER", line), ("UNDER", line)], spec[1], spec[2], spec[3], ln)
            continue
        if sport == "Cricket":
            m = re.search(r"^(?P<team>.+?)\s+1st Innings Runs at (?:the )?end of (?:over )?(?P<n>\d+)\b.*?Over/Under\s*" + NUM, ln, re.I)
            if not m:
                raise PrepareError(f"line not understood for cricket: {ln!r}")
            team, n, line = m["team"].strip(), int(m["n"]), _line(_num(m[3]))
            _side(team, home, away)
            tag = O._slug(team).upper().replace("-", "_")
            if n in (20, 50):
                add(("innings", team), "TEAM_TOTAL", [("OVER", line), ("UNDER", line)], f"FIRST_INNINGS_{tag}",
                    f"SCHEDULED_{n}_OVERS_OR_ALL_OUT", "RUNS", ln)
            else:
                add(("checkpoint", team, n), "PERIOD", [("OVER", line), ("UNDER", line)], f"FIRST_INNINGS_{tag}_OVER_{n}",
                    f"END_OF_COMPLETED_OVER_{n}", "RUNS", ln)
            continue
        m = re.search(r"Combined Total(?: Points| Goals| Runs| Games)?\s*:\s*Over/Under\s*" + NUM, ln, re.I)
        if m:
            line = _line(_num(m[1]))
            add("total", "TOTAL", [("OVER", line), ("UNDER", line)], period, endpoint, unit, ln)
            continue
        m = re.match(r"^(?P<team>.+?)\s+(?:ML|Moneyline)\s*$", ln, re.I)
        if m:
            side_lines.setdefault("ML", []).append((_side(m["team"], home, away), None, ln))
            continue
        m = re.match(r"^(?P<team>.+?)\s+(?:Spread|Handicap Games|Handicap|Puck Line|Run Line|Line)?\s*" + NUM + r"\s*(?:points|games|goals|runs)?\s*$", ln, re.I)
        if m:
            side_lines.setdefault("SPREAD", []).append((_side(m["team"], home, away), _num(m[2]), ln))
            continue
        raise PrepareError(f"line not understood: {ln!r}")
    if "ML" in side_lines and "SPREAD" in side_lines:
        raise PrepareError("one side is written as ML and the other as a spread; write both sides the same way")
    if "ML" in side_lines:
        excerpt = side_lines["ML"][0][2]
        add("side", "WINNER", [("HOME", ""), ("AWAY", "")], period, endpoint, unit, excerpt)
    if "SPREAD" in side_lines:
        given = {s: v for s, v, _ in side_lines["SPREAD"]}
        if "HOME" in given and "AWAY" in given and abs(given["HOME"] + given["AWAY"]) > 1e-9:
            raise PrepareError("the two spreads are not equal and opposite")
        h = given["HOME"] if "HOME" in given else -given["AWAY"]
        excerpt = side_lines["SPREAD"][0][2]
        add("side", "HANDICAP", [("HOME", _line(h)), ("AWAY", _line(-h))], period, endpoint, unit, excerpt)
    if not items:
        raise PrepareError("no supplied line was found")
    rows = []
    # Labels follow the order of the lines in the owner's message.
    for n, (_, family, sides_lines, period, endpoint, unit, excerpt) in enumerate(sorted(items, key=lambda x: x[0]), start=1):
        for side, line in sides_lines:
            rows.append(dict(label=f"L{n}", family=family, side=side, line=line, period=period, endpoint=endpoint,
                             action="STANDARD", unit=unit, request_excerpt=excerpt, baseline_p="",
                             baseline_id="UNAVAILABLE:NO_FROZEN_LEAGUE_BASELINE"))
    return rows


def _event_id(game: dict) -> str:
    if game["native"]:
        return game["native"] if ":" in game["native"] else f"NATIVE:{game['native']}"
    utc = O.T.clock(game["scheduled_start"], "scheduled_start").astimezone(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
    return "REQ:" + ":".join(O._slug(x) for x in (game["sport"], game["competition"], game["home"], game["away"])) + ":" + utc


def skeleton(key: str, game: dict, contracts: list[dict]) -> str:
    """The card's ONECHAT_V1 block with everything the request fixes already filled in; the chat fills the rest."""
    head = dict(format=O.FORMAT, card_key=key, sport=game["sport"], competition=game["competition"], home=game["home"],
                away=game["away"], scheduled_start=game["scheduled_start"], request_at="FILL", research_start_at="FILL",
                research_end_at="FILL", not_started_source="FILL", not_started_observed_at="FILL", outcome_exposure="NONE")
    picks = [f"{r['label']},{r['family']},{r['side']},{r['line']},P?,,CENTRE?,BASIS?,RESULT_URL?" for r in contracts]
    facts = [f"{side},{f},VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?" for side in ("HOME", "AWAY")
             for f in O.required_facts(game["sport"])]
    body = [f"{k}: {v}" for k, v in head.items()] + ["", "PICKS", ",".join(O.PICK_COLUMNS), *picks, "", "FACTS",
                                                     ",".join(O.FACT_COLUMNS), *facts]
    return f"<!-- BEGIN ONECHAT_V1 {key} -->\n" + "\n".join(body) + f"\n<!-- END ONECHAT_V1 {key} -->\n"


def prepare(message, mini: str, out, *, schedules=None, first: int = 1) -> dict:
    out = Path(out)
    if out.exists():
        raise O.OneChatError(f"{out} already exists")
    if not re.fullmatch(r"[A-Za-z0-9_]+", mini):
        raise O.OneChatError("the mini key uses letters, digits and _ only")
    text = Path(message).read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    routes = {r["competition"].strip().lower(): r["schedule_source"].strip() for r in O.read_csv(schedules)} if schedules else {}
    report, games = [], []
    for n, msg in enumerate(split_messages(text), start=first):
        key = f"{mini}-G{n:04d}"
        try:
            game = parse_message(msg)
            contracts = contracts_for(game)
            source = game["schedule"] or routes.get(game["competition"].lower(), "")
            if not re.match(r"https?://\S+$", source):
                raise PrepareError(f"no official schedule page for {game['competition']!r}: add a 'Schedule: <url>' line "
                                   "or a row in the schedules file")
            event = dict(event_id=_event_id(game), sport=game["sport"], competition=game["competition"], home=game["home"],
                         away=game["away"], scheduled_start=game["scheduled_start"], schedule_source=source)
            payload = {"REQUEST.txt": (msg.strip("\n") + "\n").encode("utf-8"),
                       "EVENT.csv": F.csv_bytes(F.EVENT_FIELDS, [event]), "CONTRACTS.csv": F.csv_bytes(F.CONTRACT_FIELDS, contracts)}
            problems = F.request_problems(payload)
            if problems:
                raise PrepareError(" | ".join(problems))
            games.append((key, game, contracts, payload))
            report.append(dict(game=n, card_key=key, status="PREPARED", detail=f"{game['home']} v {game['away']}, {game['scheduled_start']}"))
        except (PrepareError, ValueError) as exc:
            report.append(dict(game=n, card_key=key, status="REFUSED", detail=str(exc)))
    out.mkdir(parents=True)
    for key, game, contracts, payload in games:
        folder = out / key
        folder.mkdir()
        for name, raw in payload.items():
            (folder / name).write_bytes(raw)
        (folder / "SKELETON.md").write_text(skeleton(key, game, contracts), encoding="utf-8")
    ordered = sorted(games, key=lambda g: O.T.clock(g[1]["scheduled_start"], "scheduled_start"))
    packet = [f"# Chat packet {mini}: {len(ordered)} games", "",
              "Follow ONE_CHAT_BRIEF_v29.0.md from the repository's main branch. Work the games in the order below (earliest start first).",
              "For each game: research, then fill the skeleton's FILL and ? fields, and hand over the finished card at once.",
              "Keep the card key, sport, competition, home, away, scheduled_start and every PICKS label, family, side and line exactly as given.",
              "Give both sides of every line a probability (they sum to 1), or write UNPRICED on both. Never change a card you have already handed over.", ""]
    for key, game, contracts, payload in ordered:
        packet += [f"## {key} · {game['home']} v {game['away']} · {game['competition']} · {game['scheduled_start']}", "",
                   "Request as sent:", "", "```text", payload["REQUEST.txt"].decode("utf-8").rstrip("\n"), "```", "",
                   "Card skeleton:", "", "```text", skeleton(key, game, contracts).rstrip("\n"), "```", ""]
    (out / "CHAT_PACKET.md").write_text("\n".join(packet), encoding="utf-8")
    (out / "PREPARE_REPORT.csv").write_bytes(O.csv_bytes(REPORT_FIELDS, report))
    return dict(prepared=len(games), refused=sum(r["status"] == "REFUSED" for r in report), out=str(out))


def register_folder(folder, root=O.ROOT) -> dict:
    """Register every prepared request in the folder and publish them together (one push)."""
    folder, root = Path(folder), Path(root)
    keys, results = [], []
    for sub in sorted(p for p in folder.iterdir() if p.is_dir()):
        if not all((sub / n).exists() for n in F.REQUEST_FILES):
            continue
        try:
            outcome = F.register_request(sub / "REQUEST.txt", sub / "EVENT.csv", sub / "CONTRACTS.csv", sub.name, O.request_staging(root))
            keys.append(sub.name)
            results.append(f"{sub.name}: {outcome['status']}")
        except ValueError as exc:
            results.append(f"{sub.name}: REFUSED {exc}")
    commit = O.publish_requests(keys, root) if keys else ""
    return dict(registered=len(keys), commit=commit or "", branch=O.SEAL_BRANCH, detail=results,
                note="start research only after GitHub shows this publication")


def intake_from_seals(out, root=O.ROOT) -> dict:
    """Intake built from the first sealed version of every sealed card, so a later copy can never replace it."""
    root = Path(root)
    repo = O.Repo(root)
    first = {}
    for r in repo.seals:
        first.setdefault(r["card_key"], r)
    with tempfile.TemporaryDirectory(prefix="sealed-cards-") as temp:
        for key, r in sorted(first.items()):
            raw = None
            for ref in (repo.seal_ref, "HEAD"):
                raw = repo.blob(ref, r["sealed_path"]) if ref else None
                if raw is not None:
                    break
            if raw is None:
                commit = repo.first_content(r["sealed_path"], r["file_sha256"])
                raw = repo.blob(commit, r["sealed_path"]) if commit else None
            if raw is None:
                raise O.OneChatError(f"{key}: the sealed file {r['sealed_path']} is not available; fetch {O.SEAL_BRANCH}")
            text = raw.decode("utf-8", errors="replace").replace("\r\n", "\n")
            match = next((m for m in O.BLOCK.finditer(text) if m["key"] == key and O.sha(m["body"].encode("utf-8")) == r["block_sha256"]), None)
            if match is None:
                raise O.OneChatError(f"{key}: the sealed block is not in its sealed file")
            target = Path(temp) / f"{key}.md"
            target.write_text(match.group(0) + "\n", encoding="utf-8")
            os.utime(target, (0, 0))
        return O.intake(temp, out, root)


def watch(folder, *, every: int = 120, once: bool = False, push: bool = True, root=O.ROOT, lookup=None, log=print) -> list:
    """Seal every new card saved in the folder, pass after pass, until stopped (Ctrl+C)."""
    folder = Path(folder)
    history = []
    while True:
        files = sorted(p for p in folder.glob("*") if p.is_file() and p.suffix.lower() in (".md", ".txt"))
        try:
            result = O.seal(files, root, push=push, lookup=lookup) if files else dict(sealed=0, refused=[])
        except O.OneChatError as exc:
            result = dict(sealed=0, refused=[dict(file="", card_key="", reason=str(exc))])
        stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        if result.get("sealed"):
            log(f"{stamp} sealed {result['sealed']}: {result.get('cards', '')} (GitHub time {result.get('server_time') or 'pending'})")
        for r in result.get("refused", []):
            log(f"{stamp} NOT SEALED {r['card_key'] or r['file']}: {r['reason']}")
        history.append(result)
        if once:
            return history
        time.sleep(every)


def write_templates(out) -> dict:
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    written = []
    for sport in O.SUPPORTED_SPORTS:
        name = f"ONECHAT_V1_{sport.upper().replace(' ', '_')}_v29.0.md"
        text = (f"# ONECHAT_V1 template: {sport} (v29.0)\n\nCopy the block, use the card key and header values from your "
                "request packet, and fill every empty field. Every FACTS row stays; write MISSING with the reason when a "
                "value cannot be found.\n\n```text\n" + O.template(sport) + "\n```\n")
        (out / name).write_text(text, encoding="utf-8")
        written.append(name)
    return dict(templates=len(written), folder=str(out))
