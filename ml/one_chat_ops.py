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
import unicodedata
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
SCHEDULES = "research/one_chat/SCHEDULE_SOURCES.csv"   # competition,schedule_source: one official schedule page per competition
SEPARATOR = re.compile(r"^\s*[-_=*~.]{3,}\s*$")
PLACEHOLDER = re.compile(r"\b(Team|Player) [AB]\b|\bX\.X\b|Day Month Year|Time AM/PM|\bCompetition,")


class PrepareError(ValueError):
    pass


def _num(text: str) -> float:
    return float(text.replace("−", "-"))


def _line(value: float) -> str:
    return f"{value:g}" if value != int(value) else f"{int(value)}"


def split_messages(text: str) -> list[str]:
    """One message per game: each starts at a line beginning 'Upcoming'. Separator lines (-----) are not part of a game."""
    text = "\n".join("" if SEPARATOR.match(ln) else ln for ln in text.splitlines())
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


def _words(name: str) -> list[str]:
    plain = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii").lower()
    return re.findall(r"[a-z0-9]+", plain)


def _side(team: str, home: str, away: str) -> str:
    """Which side a line names: the full name, or a shortened one ("Dubai" for "BC Dubai", "lakers HC" for
    "Växjö Lakers HC") whose words all belong to exactly one of the two names in the header."""
    words = _words(team)
    # An exact full name wins first, so "Tennessee" against "Middle Tennessee" is not ambiguous.
    exact = [side for side, name in (("HOME", home), ("AWAY", away)) if words and words == _words(name)]
    if len(exact) == 1:
        return exact[0]
    matches = []
    for side, name in (("HOME", home), ("AWAY", away)):
        full = _words(name)
        if words and (words == full or all(w in full for w in words)):
            matches.append(side)
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise PrepareError(f"line names {team!r}, which is neither {home!r} nor {away!r} as written in the header")
    raise PrepareError(f"line names {team!r}, which fits both {home!r} and {away!r}; write the side's name in full")


def parse_message(message: str) -> dict:
    lines = [ln.strip() for ln in message.splitlines() if ln.strip() and not SEPARATOR.match(ln)]
    if PLACEHOLDER.search(message):
        raise PrepareError("the request still holds template placeholders (Team A/B, X.X, Day Month Year); fill them in or leave the game out")
    m = re.match(r"Upcoming\s+(?P<sport>.+?)\s+(?:Game|Match)\s*:\s*(?P<a>.+?)\s+(?P<sep>vs\.?|v|@|at)\s+(?P<b>.+?),\s*(?P<rest>.+?),?$",
                 lines[0], re.I)
    if not m:
        raise PrepareError("header is not 'Upcoming <Sport> Game: Team A vs Team B, Competition,' (or 'Away @ Home')")
    sport = SPORTS.get(m["sport"].strip().lower())
    if not sport:
        raise PrepareError(f"sport {m['sport']!r} has no request format; use the free-form route")
    a, b = m["a"].strip(), m["b"].strip()
    competition = m["rest"].split(",")[0].strip().rstrip(",")
    start = next((_start(ln) for ln in lines if ln.lower().startswith("estimated game time start")), None)
    if not start:
        raise PrepareError("no 'Estimated Game Time Start' line")
    # "Away @ Home" names the home side; with "vs" and no home line, HOME and AWAY are the first- and second-named sides.
    home, away = (b, a) if m["sep"].lower() in ("@", "at") else (a, b)
    venue = next((ln.split(":", 1)[1].strip() for ln in lines if ln.lower().startswith("home side")), "")
    if venue and not venue.lower().startswith("neutral"):
        named = _side(venue.split("(")[0], a, b)
        home, away = (a, b) if named == "HOME" else (b, a)
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
        m = re.match(r"^(?P<team>.+?)\s+(?:ML|Moneyline|ML/Spread)\s*:?\s*$", ln, re.I)
        if m:
            side_lines.setdefault("ML", []).append((_side(m["team"], home, away), None, ln))
            continue
        m = re.match(r"^(?P<team>.+?)\s+(?:(?:ML/Spread|Spread|Handicap|Games|Puck\s*Line|Run\s*Line|Line)\s*:?\s*)*"
                     + NUM + r"\s*(?:points|pts|games|goals|runs)?\s*$", ln, re.I)
        if m:
            side_lines.setdefault("SPREAD", []).append((_side(m["team"], home, away), _num(m[2]), ln))
            continue
        raise PrepareError(f"line not understood: {ln!r}")
    # v29.2: where no draw is possible and the spread is on the score that decides the match (points, goals with the
    # shootout goal, runs; never tennis games), "Side +0.5" and "Side -0.5" both settle as "Side wins", so half-point
    # spreads are the winner contract, registered once ("Americans -0.5" and "Crunch -0.5" were two labels for one result).
    if "SPREAD" in side_lines and all(abs(v) == 0.5 for _, v, _ in side_lines["SPREAD"]) and \
            F.winner_by_margin(sport, [dict(period=period, endpoint=endpoint, action="STANDARD", unit=unit)]):
        side_lines.setdefault("ML", []).extend((s, None, ln) for s, _, ln in side_lines.pop("SPREAD"))
    # "Team A ML" and "Team B +1.5" are two contracts, each priced on both sides (GAME_REQUEST_TEMPLATE §1b).
    if "ML" in side_lines:
        excerpt = side_lines["ML"][0][2]
        add("winner", "WINNER", [("HOME", ""), ("AWAY", "")], period, endpoint, unit, excerpt)
    if "SPREAD" in side_lines:
        spreads = side_lines["SPREAD"]
        given = {s: v for s, v, _ in spreads}
        if len(spreads) == 2 and len(given) == 2 and abs(given["HOME"] + given["AWAY"]) < 1e-9:
            spreads = spreads[:1]       # "A -3.5" and "B +3.5": both sides of one line, one contract
        # v29.2 (owner, 22 Nov 2026): different spreads ("Aktobe +4.5", "Torpedo -3.5") are asked for on purpose and are
        # different contracts, each priced on both sides under its own label.
        for side, value, excerpt in spreads:
            h = value if side == "HOME" else -value
            add(("handicap", h), "HANDICAP", [("HOME", _line(h)), ("AWAY", _line(-h))], period, endpoint, unit, excerpt)
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


KIT_PARAMS = "research/external/kit/v24.15/KIT_PARAMETERS_v24.15.csv"
KIT_SPORT = {"Australian Rules": "AFL"}


def kit_row_note(sport: str, competition: str, root=None) -> str:
    """Which kit parameter row this game's competition reaches (v29.2). The kit is unchanged; this names the row so the
    chat passes an exact key, and a family fallback ("NBA Cup group stage" reaching the 40-minute FIBA prior) is never silent."""
    path = Path(root or O.ROOT) / KIT_PARAMS
    if not path.exists():
        return ""
    from ml.kit import sr_kit as K
    params = K.load_params(path)
    prefix = KIT_SPORT.get(sport, sport)
    key = f"{prefix}/{competition}"

    def usable(k):
        return params[k]["status"] not in ("NOT_USABLE", "NOT_ESTIMATED", "NOT_COVERED")

    if key in params and usable(key):
        return f"Kit row: `{key}` (its own row, {params[key]['status']})."
    words = set(_words(competition))
    near = sorted(k for k in params if k.startswith(prefix + "/") and usable(k) and set(_words(k.split("/", 1)[1])) <= words)
    note = f"Kit row: no own row for `{key}`."
    if near:
        note += (" Rows named inside this competition's name: " + ", ".join(f"`{k}`" for k in near)
                 + ". Pass the one that is this competition to the kit, or say on the card why none is.")
    try:
        fallback = K.row(params, key).get("competition", "a family prior")
    except K.KitError:
        return note + " The kit has no row and no family prior for it: price from the research and say NOT_COVERED."
    return note + f" Otherwise the kit uses `{fallback}` (widths +10%, UNCALIBRATED_FAMILY_PROXY): say so on the card."


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
    routes = {}
    for path in [p for p in (O.ROOT / SCHEDULES, Path(schedules) if schedules else None) if p is not None and Path(p).exists()]:
        routes.update({r["competition"].strip().lower(): r["schedule_source"].strip() for r in O.read_csv(path) if r.get("schedule_source", "").strip()})
    needed = {}
    report, games = [], []
    for n, msg in enumerate(split_messages(text), start=first):
        key = f"{mini}-G{n:04d}"
        try:
            game = parse_message(msg)
            contracts = contracts_for(game)
            # The schedules file names a competition, or the start of one ("Challenger" covers "Challenger Monastir - SF").
            comp = game["competition"].lower()
            prefix = max((k for k in routes if comp == k or comp.startswith(k + " ")), key=len, default="")
            source = game["schedule"] or routes.get(prefix, "")
            if not re.match(r"https?://\S+$", source):
                needed[game["competition"]] = game["sport"]
                raise PrepareError(f"no official schedule page for {game['competition']!r}: add a 'Schedule: <url>' line "
                                   "or a row in the schedules file")
            event = dict(event_id=_event_id(game), sport=game["sport"], competition=game["competition"], home=game["home"],
                         away=game["away"], scheduled_start=game["scheduled_start"], schedule_source=source)
            payload = {"REQUEST.txt": (msg.strip("\n") + "\n").encode("utf-8"),
                       "EVENT.csv": F.csv_bytes(F.EVENT_FIELDS, [event]), "CONTRACTS.csv": F.csv_bytes(F.CONTRACT_FIELDS, contracts)}
            problems = F.request_problems(payload) or F.contract_problems(payload)
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
              "Follow ONE_CHAT_BRIEF_v29.2.md from the repository's main branch. Work the games in the order below (earliest start first).",
              "For each game: research, then fill the skeleton's FILL and ? fields, and hand over the finished card at once.",
              "Keep the card key, sport, competition, home, away, scheduled_start and every PICKS label, family, side and line exactly as given.",
              "HOME and AWAY are the sides named in each skeleton's home and away fields (the request's first- and second-named sides unless it names a home side or uses '@'); price them by name.",
              "Give both sides of every line a probability (they sum to 1), or write UNPRICED on both. Never change a card you have already handed over.", ""]
    for key, game, contracts, payload in ordered:
        kit = kit_row_note(game["sport"], game["competition"])
        packet += [f"## {key} · {game['home']} v {game['away']} · {game['competition']} · {game['scheduled_start']}", "",
                   *([kit, ""] if kit else []),
                   "Request as sent:", "", "```text", payload["REQUEST.txt"].decode("utf-8").rstrip("\n"), "```", "",
                   "Card skeleton:", "", "```text", skeleton(key, game, contracts).rstrip("\n"), "```", ""]
    (out / "CHAT_PACKET.md").write_text("\n".join(packet), encoding="utf-8")
    (out / "PREPARE_REPORT.csv").write_bytes(O.csv_bytes(REPORT_FIELDS, report))
    if needed:
        # Fill these once (official schedule pages), add them to research/one_chat/SCHEDULE_SOURCES.csv, and re-run.
        (out / "SCHEDULES_NEEDED.csv").write_bytes(O.csv_bytes(("competition", "sport", "schedule_source"),
                                                               [dict(competition=c, sport=s, schedule_source="") for c, s in sorted(needed.items())]))
    return dict(prepared=len(games), refused=sum(r["status"] == "REFUSED" for r in report), schedules_needed=len(needed), out=str(out))


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
    """One template per sport for a chat that cannot run this repository: the block's shape, the PICKS columns and
    every required FACTS row of the sport. The chat packet's skeleton, when there is one, takes precedence."""
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    written = []
    for sport in O.SUPPORTED_SPORTS:
        head = [f"{f}: {O.FORMAT if f == 'format' else sport if f == 'sport' else 'FILL'}" for f in O.HEADER]
        picks = ["L1,FAMILY?,SIDE?,LINE?,P?,,CENTRE?,BASIS?,RESULT_URL?", "L1,FAMILY?,SIDE?,LINE?,P?,,CENTRE?,BASIS?,RESULT_URL?"]
        facts = [f"{side},{f},VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?" for side in ("HOME", "AWAY") for f in O.required_facts(sport)]
        block = "\n".join(["<!-- BEGIN ONECHAT_V1 CARD_KEY -->", *head, "", "PICKS", ",".join(O.PICK_COLUMNS), *picks, "",
                           "FACTS", ",".join(O.FACT_COLUMNS), *facts, "<!-- END ONECHAT_V1 CARD_KEY -->"])
        text = (f"# ONECHAT_V1 template: {sport} (v29.0)\n\nUse the skeleton in your chat packet when you have one. "
                "Otherwise copy this block: the card key and the header values come from the owner's registered request; "
                "write one PICKS row per side of every supplied line (two rows per line, same label); keep every FACTS row, "
                "writing MISSING with the reason when a value cannot be found. Replace every FILL and every field ending "
                "in ?.\n\n```text\n" + block + "\n```\n")
        name = f"ONECHAT_V1_{sport.upper().replace(' ', '_')}_v29.0.md"
        (out / name).write_text(text, encoding="utf-8")
        written.append(name)
    return dict(templates=len(written), folder=str(out))
