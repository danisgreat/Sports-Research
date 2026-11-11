"""External research lanes: shared event key, lane returns, checks and the merge (EXT-v1, CR-2026.11.11-R1).

The owner runs several ChatGPT research chats on one game. Each chat works one LANE and returns one LANE_RETURN block;
the repository agent saves each return byte for byte under ``research/active_minis/received/<event key>/`` and merges them
here. The card itself is still made, linted, ledgered and frozen in this repository (EXTERNAL_RESEARCH_PROTOCOL).

    python -m ml external event-key --sport Basketball --date 2026-11-10 --a "Chiba Jets" --b "Osaka Evessa"
    python -m ml external check  --return FILE
    python -m ml external merge  --event-key EV-... --returns DIR_OR_FILES... --out NEW_FOLDER [--do-not-open LIST.csv]

Lanes (EXTERNAL_RESEARCH_PROTOCOL section 2): L1 availability and late changes; L2 both sides' results and form windows;
L3 venue, weather, officials, rest, travel and rules; L4 independent re-check of L1's decisive facts from other sources;
L5 pricing from the merged evidence with the kit; FULL a whole-card replicate (the owner's older one-chat-does-all route).

The return block:

    <!-- BEGIN LANE_RETURN -->
    event_key: EV-20261110-BKB-CHIBAJETS-OSAKAEVESS
    lane: L1
    chat_label: CHAT-1
    profile_version: v24.15
    commit: <the 40-character commit the chat read>
    reader: CHATGPT_BROWSING
    started_at: 2026-11-10T08:00:00+11:00
    completed_at: 2026-11-10T08:40:00+11:00

    [EVIDENCE]
    side,field,value,source_url,source_class,published_at,retrieved_at,confirmation,notes
    [PROBABILITIES]
    label,family,side,line,line_source,w,p,l,final_p,kit_receipt_sha256
    [ACCESS_LOG]
    url,result,checked_at,notes
    <!-- END LANE_RETURN -->

Merge rules: evidence is pooled by (side, field, value); a fact is CORROBORATED only with two reviewed original collector IDs
(two pages or domains using one copied feed are one collector); a single-valued field with two values is a CONFLICT the card must
resolve or price as a scenario. Pricing returns (L5, FULL) are pooled per contract: median, minimum, maximum and spread;
a contract is EXTERNAL_DISAGREEMENT when the runs fall on both sides of 0.5 or the spread exceeds 0.10, and the card may not
rank it. Market terms anywhere in a return are refused.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
import re
import statistics
import unicodedata
import urllib.parse
from datetime import datetime
from pathlib import Path

PROFILE_VERSION = "v24.15"
SPORT_CODES = {"Basketball": "BKB", "Soccer": "SOC", "Cricket": "CRI", "Tennis": "TEN", "Ice Hockey": "IHO", "Rugby League": "RGL",
               "Rugby Union": "RGU", "American Football": "AMF", "Baseball": "BSB", "Australian Rules": "AUS"}
EVENT_KEY = re.compile(r"(?:EV-\d{8}-[A-Z0-9]+-[A-Z0-9]+-[A-Z0-9]+|EV2-[A-F0-9]{32})")
LANES = ("L1", "L2", "L3", "L4", "L5", "L6", "FULL")
PRICING_LANES = ("L5", "FULL")
READERS = ("CHATGPT_BROWSING", "CLAUDE_AGENT", "OWNER")
SIDES = ("HOME", "AWAY", "EVENT")
SOURCE_CLASSES = ("FIELD_OWNER", "LEAGUE", "CLUB", "OFFICIAL_SOCIAL", "PROVIDER", "MEDIA", "REPORTER_SOCIAL", "OWNER_CAPTURE")
CONFIRMATION = ("OFFICIAL_CONFIRMED", "REPORTED", "PROJECTED", "NOT_APPLICABLE")
ACCESS_RESULTS = ("OPENED", "BLOCKED_BY_RULES", "RULES_UNKNOWN", "ON_DO_NOT_OPEN_LIST", "TECHNICAL_FAILURE", "NOT_FOUND")
SINGLE_VALUED = ("venue", "scheduled_start", "home_team", "starting_goalie", "starting_pitcher", "starting_qb", "referee",
                 "umpire_crew", "toss_winner", "toss_decision", "temperature_c", "wind_kph", "rain_probability_pct", "lineup_status",
                 "surface", "best_of", "final_set_rule", "court", "endpoint_rule", "neutral_venue", "stage", "rest_days", "travel")
HEADER = ("event_key", "lane", "chat_label", "profile_version", "commit", "reader", "started_at", "completed_at")
SECTIONS = {"EVIDENCE": ("side", "field", "value", "source_url", "source_class", "published_at", "retrieved_at", "confirmation", "notes"),
            "PROBABILITIES": ("label", "family", "side", "line", "line_source", "w", "p", "l", "final_p", "kit_receipt_sha256"),
            "ACCESS_LOG": ("url", "result", "checked_at", "notes")}
OPTIONAL_SECTIONS = {"REQUIREMENTS": ("requirement_id", "status", "reason"),
                     "UNPRICED": ("label", "status", "reason")}
MARKET = re.compile(r"\b(odds|bookmaker|sportsbook|betting|wager|tipster|implied probability|moneyline price|line movement)\b", re.I)
DISAGREE_SPREAD = 0.10
TWO_LABEL_SUFFIXES = ("co.uk", "com.au", "org.au", "net.au", "co.nz", "co.jp", "or.jp", "co.kr", "com.br", "com.ar", "co.za",
                      "com.mx", "com.cn", "com.tr", "org.uk", "ac.uk", "gov.au")


class ExternalError(ValueError):
    pass


def slug(name: str, size: int = 10) -> str:
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().upper()
    out = re.sub(r"[^A-Z0-9]", "", text)[:size]
    if not out:
        raise ExternalError(f"{name!r} gives an empty key part")
    return out


def event_key(sport: str, date: str, a: str, b: str, *, competition: str = "", native_event_id: str = "", game_number: str = "") -> str:
    """EV-YYYYMMDD-SPORT-A-B: the AEDT date of the request's estimated start and the two sides in REQUEST order (not home first),
    so every chat derives the same key from the same request without looking anything up."""
    if sport not in SPORT_CODES:
        raise ExternalError(f"sport must be one of {', '.join(SPORT_CODES)}")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ExternalError("date is YYYY-MM-DD (the AEDT date of the estimated start in the request)")
    if competition or native_event_id:
        if not competition or not native_event_id:
            raise ExternalError("competition and native_event_id are both required for an authoritative EV2 key")
        # Native identity remains stable across reschedules and participant aliases. The manifest binds the exact sides.
        identity = "\x1f".join((sport, competition.strip(), native_event_id.strip(), str(game_number))).encode()
        return "EV2-" + hashlib.sha256(identity).hexdigest()[:32].upper()
    # Legacy discovery keys are never admitted by EXT-v2 (research_intake requires an EV2 manifest).
    return f"EV-{date.replace('-', '')}-{SPORT_CODES[sport]}-{slug(a)}-{slug(b)}"


def domain(url: str) -> str:
    """Registrable domain (approximate): the last two labels, or three for common two-label public suffixes."""
    host = (urllib.parse.urlparse(url).hostname or "").lower()
    parts = host.split(".")
    if len(parts) >= 3 and ".".join(parts[-2:]) in TWO_LABEL_SUFFIXES:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


def _time_ok(value: str) -> bool:
    from datetime import datetime
    try:
        return datetime.fromisoformat(value.strip().replace("Z", "+00:00")).tzinfo is not None
    except ValueError:
        return False


def parse(text: str) -> dict:
    """One LANE_RETURN block -> header and the three CSV sections (raises ExternalError on a malformed block)."""
    matches = list(re.finditer(r"<!-- BEGIN LANE_RETURN -->(.*?)<!-- END LANE_RETURN -->", text, re.S))
    if len(matches) != 1:
        raise ExternalError("no complete LANE_RETURN block")
    m = matches[0]
    body = [ln.rstrip("\r") for ln in m.group(1).strip().splitlines()]
    header, i = {}, 0
    while i < len(body) and body[i].strip() and not body[i].startswith("["):
        name, sep, value = body[i].partition(":")
        if not sep:
            raise ExternalError(f"header line without a colon: {body[i]!r}")
        if name.strip() in header:
            raise ExternalError(f"duplicate header {name.strip()}")
        header[name.strip()] = value.strip()
        i += 1
    sections, current, lines = {}, None, []
    for ln in body[i:] + ["[END]"]:
        tag = re.fullmatch(r"\[([A-Z_]+)\]", ln.strip())
        if tag:
            if current:
                if current in sections:
                    raise ExternalError(f"duplicate section {current}")
                sections[current] = lines
            current, lines = tag.group(1), []
        elif current and ln.strip():
            lines.append(ln)
    out = dict(header=header, raw_sha256=hashlib.sha256(m.group(0).encode("utf-8")).hexdigest())
    for name, fields in dict(SECTIONS, **OPTIONAL_SECTIONS).items():
        rows = sections.get(name, [])
        if not rows:
            out[name] = []
            continue
        reader = csv.DictReader(io.StringIO("\n".join(rows)))
        if tuple(reader.fieldnames or ()) != fields:
            raise ExternalError(f"[{name}] columns must be exactly: {','.join(fields)}")
        out[name] = [dict(r) for r in reader]
        if any(set(r) != set(fields) or any(v is None for v in r.values()) for r in out[name]):
            raise ExternalError(f"[{name}] malformed CSV row")
    return out


def check(ret: dict, do_not_open: set | None = None) -> list[str]:
    problems = []
    h = ret["header"]
    for k in HEADER:
        if not h.get(k):
            problems.append(f"header: missing {k}")
    if problems:
        return problems
    if not EVENT_KEY.fullmatch(h["event_key"]):
        problems.append("header: event_key must be EV-YYYYMMDD-SPORT-A-B (python -m ml external event-key)")
    if h["lane"] not in LANES:
        problems.append(f"header: lane must be one of {', '.join(LANES)}")
    if h["reader"] not in READERS:
        problems.append(f"header: reader must be one of {', '.join(READERS)}")
    if not re.fullmatch(r"[0-9a-f]{40}", h["commit"]):
        problems.append("header: commit is the full 40-character commit the chat read (REF-v2)")
    if h["profile_version"] != PROFILE_VERSION:
        problems.append(f"header: profile_version must be {PROFILE_VERSION}; legacy returns are diagnostic only")
    for k in ("started_at", "completed_at"):
        if not _time_ok(h[k]):
            problems.append(f"header: {k} needs an ISO time with an offset")
    clock = lambda s: datetime.fromisoformat(s.replace("Z", "+00:00"))
    if all(_time_ok(h[k]) for k in ("started_at", "completed_at")) and clock(h["started_at"]) > clock(h["completed_at"]):
        problems.append("header: completed_at precedes started_at")
    if not ret["EVIDENCE"] and h["lane"] not in PRICING_LANES and not ret.get("REQUIREMENTS"):
        problems.append("research lane is empty: return evidence or explicit requirement dispositions")
    for i, r in enumerate(ret["EVIDENCE"], 2):
        where = f"EVIDENCE line {i}"
        if r["side"] not in SIDES:
            problems.append(f"{where}: side must be HOME, AWAY or EVENT")
        if not r["field"].strip() or not r["value"].strip():
            problems.append(f"{where}: field and value are required (unknown stays out of EVIDENCE and goes to notes elsewhere)")
        if not r["source_url"].startswith("https://") and r["source_class"] != "OWNER_CAPTURE":
            problems.append(f"{where}: an https source_url is required (an owner capture names its received file instead)")
        if r["source_class"] not in SOURCE_CLASSES:
            problems.append(f"{where}: source_class must be one of {', '.join(SOURCE_CLASSES)}")
        if r["confirmation"] not in CONFIRMATION:
            problems.append(f"{where}: confirmation must be one of {', '.join(CONFIRMATION)}")
        if not _time_ok(r["retrieved_at"]):
            problems.append(f"{where}: retrieved_at needs an ISO time with an offset")
        if r["published_at"] and r["published_at"] != "UNKNOWN" and not _time_ok(r["published_at"]):
            problems.append(f"{where}: published_at is an ISO time with an offset, or UNKNOWN")
        if _time_ok(r["retrieved_at"]) and _time_ok(h["completed_at"]):
            if clock(r["retrieved_at"]) > clock(h["completed_at"]):
                problems.append(f"{where}: retrieval is after completion")
            if _time_ok(r["published_at"]) and clock(r["published_at"]) > clock(r["retrieved_at"]):
                problems.append(f"{where}: publication is after retrieval")
        if not any(a["url"] == r["source_url"] and a["result"] == "OPENED" for a in ret["ACCESS_LOG"]):
            problems.append(f"{where}: evidence has no OPENED access record (owner captures require a recorded intake access)")
        if do_not_open and domain(r["source_url"]) in do_not_open:
            problems.append(f"{where}: {domain(r['source_url'])} is on the chats' do-not-open list; this fact cannot be used")
    if h["lane"] in PRICING_LANES and not ret["PROBABILITIES"] and not ret.get("UNPRICED"):
        problems.append("PROBABILITIES: a pricing lane (L5 or FULL) returns every supplied contract")
    if h["lane"] not in PRICING_LANES and (ret["PROBABILITIES"] or ret.get("UNPRICED")):
        problems.append("PROBABILITIES: only L5 and FULL price; research lanes return evidence")
    labels = [r["label"] for r in ret["PROBABILITIES"]]
    if len(labels) != len(set(labels)):
        problems.append("PROBABILITIES: duplicate contract labels in one run")
    for i, r in enumerate(ret["PROBABILITIES"], 2):
        where = f"PROBABILITIES line {i}"
        try:
            w, p, l, fp = (float(r[k]) for k in ("w", "p", "l", "final_p"))
        except ValueError:
            problems.append(f"{where}: w, p, l and final_p must be numbers")
            continue
        if not all(math.isfinite(v) and 0 <= v <= 1 for v in (w, p, l, fp)):
            problems.append(f"{where}: probabilities must be finite in [0,1]")
            continue
        if min(w, p, l) < -1e-9 or abs(w + p + l - 1) > 0.002:
            problems.append(f"{where}: W/P/L must be non-negative and sum to 1")
        if w + l > 0 and abs(fp - w / (w + l)) > 0.002:
            problems.append(f"{where}: final_p must equal W/(W+L)")
        if w + l <= 0:
            problems.append(f"{where}: all-push contracts have no decisive probability")
        from ml.kit.sr_kit import FAMILIES
        family_sides = {"handicap": ("HOME", "AWAY"), "set_handicap": ("HOME", "AWAY", "A", "B"),
                        "winner": ("HOME", "AWAY", "DRAW", "A", "B"), "regulation_winner": ("HOME", "AWAY", "DRAW")}
        if r["family"] not in FAMILIES or r["side"] not in family_sides.get(r["family"], ("OVER", "UNDER")):
            problems.append(f"{where}: undefined contract family or side")
        if r["line"]:
            try:
                if not math.isfinite(float(r["line"])): raise ValueError()
            except ValueError:
                problems.append(f"{where}: line must be finite")
        elif r["family"] not in ("winner", "regulation_winner"):
            problems.append(f"{where}: this contract requires a line")
        if r["line_source"] not in ("SUPPLIED", "ANALYST_DERIVED"):
            problems.append(f"{where}: line_source must be SUPPLIED or ANALYST_DERIVED")
        if not re.fullmatch(r"[0-9a-f]{64}", r["kit_receipt_sha256"]):
            problems.append(f"{where}: kit_receipt_sha256 names the KIT_RECEIPT block the number came from (a hand number is refused)")
    for i, r in enumerate(ret["ACCESS_LOG"], 2):
        if not _time_ok(r["checked_at"]):
            problems.append(f"ACCESS_LOG line {i}: checked_at needs an ISO time with offset")
        if r["result"] not in ACCESS_RESULTS:
            problems.append(f"ACCESS_LOG line {i}: result must be one of {', '.join(ACCESS_RESULTS)}")
        if r["result"] == "OPENED" and do_not_open and domain(r["url"]) in do_not_open:
            problems.append(f"ACCESS_LOG line {i}: {domain(r['url'])} is on the do-not-open list but was opened")
    for name in ("EVIDENCE", "ACCESS_LOG"):
        for i, r in enumerate(ret[name], 2):
            for k, v in r.items():
                if k not in ("source_url", "url") and MARKET.search(v or ""):
                    problems.append(f"{name} line {i}: {k} mentions a market term; returns hold sporting facts only")
    return problems


def _single(field: str) -> bool:
    return field in SINGLE_VALUED or field.startswith("status:")


def merge(returns: list[dict], key: str, *, source_reviews: list[dict] | None = None) -> dict:
    if not EVENT_KEY.fullmatch(key):
        raise ExternalError("event key must be EV-YYYYMMDD-SPORT-A-B")
    used = [r for r in returns if r["header"].get("event_key") == key]
    if not used:
        raise ExternalError(f"no return carries event_key {key}")
    hashes = [r["raw_sha256"] for r in used]
    runs = [(r["header"]["lane"], r["header"]["chat_label"]) for r in used]
    if len(set(hashes)) != len(hashes) or len(set(runs)) != len(runs):
        raise ExternalError("duplicate return or lane/chat run; use explicit versioned replacement intake")
    commits = sorted({r["header"]["commit"] for r in used})
    if len(commits) != 1:
        raise ExternalError("mixed commits are refused; all lanes must read the same pinned release")
    reviews = {r["source_url"]: r for r in (source_reviews or []) if r.get("lineage_status") == "VERIFIED"
               and r.get("collector_id") and re.fullmatch(r"[0-9a-f]{64}", r.get("review_evidence_sha256", ""))}
    groups: dict = {}
    for r in used:
        for e in r["EVIDENCE"]:
            k = (e["side"], e["field"].strip(), e["value"].strip().casefold())
            g = groups.setdefault(k, dict(side=e["side"], field=e["field"].strip(), value=e["value"].strip(), lanes=set(), domains=set(),
                                          classes=set(), confirmations=set(), urls=set(), collectors=set(), earliest_published=""))
            g["lanes"].add(r["header"]["lane"] + ":" + r["header"]["chat_label"])
            g["domains"].add(domain(e["source_url"]) if e["source_url"].startswith("http") else "OWNER_CAPTURE")
            g["classes"].add(e["source_class"])
            g["confirmations"].add(e["confirmation"])
            g["urls"].add(e["source_url"])
            if e["source_url"] in reviews:
                g["collectors"].add(reviews[e["source_url"]]["collector_id"])
            if _time_ok(e["published_at"]) and (not g["earliest_published"] or clock_time(e["published_at"]) < clock_time(g["earliest_published"])):
                g["earliest_published"] = e["published_at"]
    evidence = []
    for g in groups.values():
        evidence.append(dict(side=g["side"], field=g["field"], value=g["value"], corroboration="CORROBORATED" if len(g["collectors"]) >= 2 else "SINGLE_SOURCE" if len(g["domains"]) <= 1 else "INDEPENDENCE_UNVERIFIED",
                             n_domains=len(g["domains"]), domains="|".join(sorted(g["domains"])), source_classes="|".join(sorted(g["classes"])),
                             confirmations="|".join(sorted(g["confirmations"])), lanes="|".join(sorted(g["lanes"])),
                             earliest_published=g["earliest_published"], urls=" ".join(sorted(g["urls"]))))
    evidence.sort(key=lambda e: (e["side"], e["field"], e["value"]))
    conflicts = []
    by_field: dict = {}
    for e in evidence:
        if _single(e["field"]):
            by_field.setdefault((e["side"], e["field"]), []).append(e)
    for (side, field), items in by_field.items():
        if len(items) > 1:
            conflicts.append(dict(side=side, field=field, values=" || ".join(f"{i['value']} [{i['domains']}]" for i in items),
                                  resolution="RESOLVE_AT_FIELD_OWNER_OR_PRICE_AS_SCENARIO"))
    prices: dict = {}
    for r in used:
        if r["header"]["lane"] not in PRICING_LANES:
            continue
        for p in r["PROBABILITIES"]:
            k = (p["label"], p["family"], p["side"], p["line"])
            prices.setdefault(k, []).append(float(p["final_p"]))
    probabilities = []
    for (label, family, side, line), ps in sorted(prices.items()):
        lo, hi = min(ps), max(ps)
        disagree = (lo < 0.5 < hi) or (hi - lo) > DISAGREE_SPREAD
        probabilities.append(dict(label=label, family=family, side=side, line=line, n_runs=len(ps), median_p=round(statistics.median(ps), 4),
                                  min_p=round(lo, 4), max_p=round(hi, 4), spread=round(hi - lo, 4),
                                  status="EXTERNAL_DISAGREEMENT" if disagree and len(ps) > 1 else "CONSISTENT" if len(ps) > 1 else "SINGLE_RUN"))
    access = [dict(lane=r["header"]["lane"], chat_label=r["header"]["chat_label"], reader=r["header"]["reader"], **a)
              for r in used for a in r["ACCESS_LOG"]]
    return dict(event_key=key, n_returns=len(used), commits=commits, mixed_commits=len(commits) > 1,
                admission="DIAGNOSTIC_ONLY_UNTIL_MANIFEST_INTAKE",
                lanes=sorted(r["header"]["lane"] + ":" + r["header"]["chat_label"] for r in used), evidence=evidence, conflicts=conflicts,
                probabilities=probabilities, access=access,
                disagreement=[p["label"] for p in probabilities if p["status"] == "EXTERNAL_DISAGREEMENT"],
                inputs=[dict(lane=r["header"]["lane"], chat_label=r["header"]["chat_label"], raw_sha256=r["raw_sha256"]) for r in used])


def clock_time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _csv(rows: list[dict], fields=None) -> bytes:
    buf = io.StringIO(newline="")
    if not rows and not fields:
        return b""
    w = csv.DictWriter(buf, fieldnames=list(fields or rows[0]), lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue().encode("utf-8")


def do_not_open_domains(path) -> set:
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return {domain("https://" + r["host"] + "/") for r in csv.DictReader(fh) if r.get("chatgpt_browsing") in ("BLOCKED", "RULES_UNKNOWN")}


def _files(items) -> list[Path]:
    out = []
    for item in items:
        p = Path(item)
        out += sorted(p.glob("*.md")) + sorted(p.glob("*.txt")) if p.is_dir() else [p]
    return out


def main(argv=None):
    if argv is None:
        import sys
        argv = sys.argv[1:]
    if argv and argv[0] in ("init", "packet", "intake", "status", "admit", "bind-card", "append-card", "append-research", "review-source", "evaluate", "package-check"):
        from ml.research_intake import main as intake_main
        return intake_main(argv)
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    ek = sub.add_parser("event-key")
    ek.add_argument("--sport", required=True)
    ek.add_argument("--date", required=True, help="AEDT date of the estimated start, YYYY-MM-DD")
    ek.add_argument("--a", required=True, help="the first side as written in the request")
    ek.add_argument("--b", required=True, help="the second side as written in the request")
    ek.add_argument("--competition", required=True)
    ek.add_argument("--native-event-id", required=True)
    ek.add_argument("--game-number", default="")
    ck = sub.add_parser("check")
    ck.add_argument("--return", dest="ret", type=Path, required=True)
    ck.add_argument("--do-not-open", type=Path)
    mg = sub.add_parser("merge")
    mg.add_argument("--event-key", required=True)
    mg.add_argument("--returns", nargs="+", required=True)
    mg.add_argument("--out", type=Path, required=True)
    mg.add_argument("--do-not-open", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "event-key":
            print(event_key(args.sport, args.date, args.a, args.b, competition=args.competition,
                            native_event_id=args.native_event_id, game_number=args.game_number))
            return
        dno = do_not_open_domains(args.do_not_open) if args.do_not_open else None
        if args.command == "check":
            problems = check(parse(args.ret.read_text(encoding="utf-8")), dno)
            if problems:
                print(f"LANE_RETURN CHECK FAILED ({len(problems)}):")
                for p in problems:
                    print(" -", p)
                raise SystemExit(1)
            print("STRUCTURAL_CHECK_PASSED / NOT_ADMITTED: use external intake --event DIR --return FILE")
            return
        returns, refused = [], []
        for f in _files(args.returns):
            try:
                ret = parse(f.read_text(encoding="utf-8"))
            except ExternalError as exc:
                refused.append(dict(file=str(f), problems=str(exc)))
                continue
            problems = check(ret, dno)
            if problems:
                refused.append(dict(file=str(f), problems=" | ".join(problems)))
            else:
                returns.append(ret)
        res = merge(returns, args.event_key)
        print("DIAGNOSTIC_ONLY: no manifest, requirement or receipt admission; use external admit for issuance")
        args.out.mkdir(parents=True, exist_ok=False)
        (args.out / "MERGED_EVIDENCE.csv").write_bytes(_csv(res["evidence"], ("side", "field", "value", "corroboration", "n_domains", "domains",
                                                                              "source_classes", "confirmations", "lanes", "earliest_published", "urls")))
        (args.out / "CONFLICTS.csv").write_bytes(_csv(res["conflicts"], ("side", "field", "values", "resolution")))
        (args.out / "MERGED_PROBABILITIES.csv").write_bytes(_csv(res["probabilities"], ("label", "family", "side", "line", "n_runs", "median_p",
                                                                                       "min_p", "max_p", "spread", "status")))
        (args.out / "ACCESS_LOG.csv").write_bytes(_csv(res["access"], ("lane", "chat_label", "reader", "url", "result", "checked_at", "notes")))
        (args.out / "MERGE_RECEIPT.csv").write_bytes(_csv(res["inputs"] + [dict(lane="REFUSED", chat_label=r["file"], raw_sha256=r["problems"])
                                                                             for r in refused], ("lane", "chat_label", "raw_sha256")))
        print(f"merged {res['n_returns']} return(s) for {res['event_key']}: {len(res['evidence'])} facts, {len(res['conflicts'])} conflict(s), "
              f"{len(res['probabilities'])} priced contract(s); refused {len(refused)}")
        if res["mixed_commits"]:
            print("WARNING: the returns read different commits:", ", ".join(res["commits"]))
        print("picks header lines:")
        print(f"event_key: {res['event_key']}")
        print(f"external_runs: {sum(1 for r in returns if r['header']['lane'] in PRICING_LANES) or len(returns)}")
        if res["disagreement"]:
            print("external_disagreement: " + "|".join(res["disagreement"]))
    except ExternalError as exc:
        print(f"REFUSED: {exc}")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
