"""One chat per game: the chat's own card as the measured forecast (ONE-CHAT-v1, CR-2026.11.16-R2).

    python -m ml one-chat intake --drop FOLDER --out NEW_FOLDER      read every card file in an owner drop
    python -m ml one-chat score --intake FOLDER [FOLDER ...] --outcomes OUTCOMES.csv --out NEW_FOLDER
                                [--on-request | --cohort EARLIER/COHORT.csv] [--baseline BASELINE.csv]
    python -m ml one-chat template --sport Basketball                print an empty block for a chat to fill

The owner runs one research chat per game. Each card ends with one ``ONECHAT_V1`` block: header lines, a PICKS table
with a probability for both sides of every supplied line, and a FACTS table of the pregame figures the research found.
``intake`` parses the blocks without interpretation, records each file's hash and saved time, validates every row and
flags (never rewrites) the patterns the 16 November 2026 audit registered as hypotheses. ``score`` joins the settled
grades and reports the registered measure: the game-mean Brier score of the card's numbers on supplied lines against the
0.25 a constant 0.5 scores, with a t interval over games, calibration, ranks, timing and the hypothesis splits.

The comparator is computed here, never by the chat. Nothing in this module prices, ranks for the owner or changes a
card: ranks are a fixed function of the stated numbers (highest stated p first, one side per line). Sporting fields
only; a block that carries a price, odds or tip word is refused.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
import re
from datetime import datetime, timezone
from pathlib import Path

from ml import picks as P
from ml import timing as T

ROOT = Path(__file__).resolve().parents[1]
RULE = "ONE-CHAT-v1"
FORMAT = "ONECHAT_V1"
DICTIONARY = "research/learning_log/FEATURE_DICTIONARY.csv"
BLOCK = re.compile(r"<!-- BEGIN ONECHAT_V1 (?P<key>[^\s>]+) -->\s*\n(?P<body>.*?)\n\s*<!-- END ONECHAT_V1 (?P=key) -->", re.S)
HEADER = ("format", "card_key", "sport", "competition", "home", "away", "scheduled_start", "request_at", "research_start_at",
          "research_end_at", "not_started_source", "not_started_observed_at", "outcome_exposure")
CLOCKS = ("scheduled_start", "request_at", "research_start_at", "research_end_at", "not_started_observed_at")
PICK_COLUMNS = ("label", "family", "side", "line", "p", "lean", "centre", "availability_basis", "result_source")
FACT_COLUMNS = ("side", "field", "value", "source", "observed_at")
AVAILABILITY = ("NONE", "MEASURED", "UNMEASURED")
MARKET = re.compile(r"\b(odds|bookmaker|sportsbook|betting|wager|tipster|implied probability|price[sd]?|moneyline price)\b", re.I)
COHORT_SIZE = 100
CRITERION = -0.01           # registered practical improvement: game-mean Brier minus 0.25 at or below this, interval below zero
NO_DIRECTION = 0.05         # H-NODIR: a stated p within this of 0.5 (flag only)
BANDS = (0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.9, 1.0)
DECISIVE, TERMINAL = ("WIN", "LOSS"), ("WIN", "LOSS", "PUSH", "VOID")

CARD_FIELDS = ("card_key", "game_id", "status", "problems", "file", "file_sha256", "file_saved_at", "block_sha256", "sport",
               "competition", "home", "away", "scheduled_start", "request_at", "research_start_at", "research_end_at",
               "not_started_source", "not_started_observed_at", "outcome_exposure", "supplied_lines", "priced_lines",
               "facts_required", "facts_observed")
ROW_FIELDS = ("card_key", "game_id", "label", "family", "side", "line", "p", "lean", "centre", "availability_basis",
              "result_source", "favoured", "rank", "flags")
FACT_FIELDS = ("card_key", "game_id") + FACT_COLUMNS + ("status",)


class OneChatError(ValueError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def csv_bytes(fields, rows) -> bytes:
    out = io.StringIO(newline="")
    w = csv.DictWriter(out, fieldnames=list(fields), lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
    return out.getvalue().encode("utf-8")


def read_csv(path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def game_id(meta: dict) -> str:
    """One identity per game, whichever chat carded it: sport, competition, the two sides and the start date as written."""
    day = meta["scheduled_start"][:10]
    return "GAME-" + sha("\x1f".join((_slug(meta["sport"]), _slug(meta["competition"]), _slug(meta["home"]), _slug(meta["away"]), day)).encode())[:12].upper()


def required_facts(sport: str, root=ROOT) -> list[str]:
    rows = read_csv(Path(root) / DICTIONARY)
    mine = [r for r in rows if r["sport"] == sport] or [r for r in rows if r["sport"] == "TEAM_SPORT"]
    return [r["feature"] for r in mine if r["required"] == "Y"]


def _table(lines: list[str], columns, name: str) -> list[dict]:
    if not lines or [c.strip() for c in lines[0].split(",")] != list(columns):
        raise OneChatError(f"{name} must start with the header row {','.join(columns)}")
    rows = list(csv.DictReader(io.StringIO("\n".join(lines))))
    if any(None in r or None in r.values() for r in rows):
        raise OneChatError(f"{name} has a row with the wrong number of columns")
    return [{k: v.strip() for k, v in r.items()} for r in rows]


def parse(body: str) -> tuple[dict, list[dict], list[dict]]:
    """Header lines, then a line ``PICKS`` and its CSV, then a line ``FACTS`` and its CSV."""
    lines = [ln.rstrip() for ln in body.strip().splitlines() if not ln.strip().startswith("```")]
    try:
        i, j = lines.index("PICKS"), lines.index("FACTS")
    except ValueError:
        raise OneChatError("the block needs a PICKS line and a FACTS line") from None
    if not i < j:
        raise OneChatError("PICKS comes before FACTS")
    meta = {}
    for ln in (x for x in lines[:i] if x.strip()):
        if ":" not in ln:
            raise OneChatError(f"header line without a colon: {ln!r}")
        k, v = ln.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta, _table([x for x in lines[i + 1:j] if x.strip()], PICK_COLUMNS, "PICKS"), _table([x for x in lines[j + 1:] if x.strip()], FACT_COLUMNS, "FACTS")


def _p(value: str):
    try:
        p = float(value)
    except ValueError:
        return None
    return p if math.isfinite(p) and 0 < p < 1 else None


def _number(value: str):
    try:
        x = float(value)
        return x if math.isfinite(x) else None
    except ValueError:
        return None


def check(meta: dict, picks: list[dict], facts: list[dict], key: str, root=ROOT) -> tuple[list[str], dict]:
    """Problems refuse the card's numbers; ``derived`` carries favoured sides, ranks and flags for an admitted card."""
    problems = [f"header: missing {f}" for f in HEADER if not meta.get(f)]
    if meta.get("format") != FORMAT:
        problems.append(f"header: format must be {FORMAT}")
    if meta.get("card_key") != key:
        problems.append("header: card_key differs from the block markers")
    clocks = {}
    for f in CLOCKS:
        if meta.get(f):
            try:
                clocks[f] = T.clock(meta[f], f)
            except ValueError as exc:
                problems.append(str(exc))
    if len(clocks) == len(CLOCKS):
        if not clocks["request_at"] <= clocks["research_start_at"] <= clocks["research_end_at"]:
            problems.append("header: request, research start and research end must be in time order")
        if clocks["not_started_observed_at"] > clocks["research_end_at"]:
            problems.append("header: the not-started observation is after the research ended")
    if meta.get("not_started_source") and not re.match(r"https?://\S+$", meta["not_started_source"]):
        problems.append("header: not_started_source must be the page that showed the game had not started")
    words = re.sub(r"https?://\S+", " ", "\n".join(meta.values()) + "\n" + "\n".join(",".join(r.values()) for r in picks + facts))
    if MARKET.search(words):
        problems.append("block: sporting fields only; no odds, prices, bookmakers or tips")
    by_label: dict[str, list[dict]] = {}
    for r in picks:
        by_label.setdefault(r["label"], []).append(r)
    if not picks:
        problems.append("PICKS: no rows")
    derived = {}
    for label, rows in by_label.items():
        name = f"PICKS {label}: "
        family = rows[0]["family"]
        sides = [r["side"].upper() for r in rows]
        if any(r["family"] != family for r in rows) or family not in P.FAMILIES:
            problems.append(name + "one family from the allowed vocabulary per line")
            continue
        if any(s not in P.SIDES[family] for s in sides) or len(set(sides)) != len(sides):
            problems.append(name + f"sides must be distinct and from {'/'.join(P.SIDES[family])}")
            continue
        three_way = family == "WINNER" and "DRAW" in sides
        if len(rows) != (3 if three_way else 2) or (set(sides) not in ({"HOME", "AWAY"}, {"OVER", "UNDER"}, {"YES", "NO"}, {"HOME", "AWAY", "DRAW"})):
            problems.append(name + "both sides of the line are required (HOME/AWAY, OVER/UNDER, YES/NO, or HOME/AWAY/DRAW)")
            continue
        lines = [_number(r["line"]) if r["line"] else None for r in rows]
        if family == "WINNER":
            if any(r["line"] for r in rows):
                problems.append(name + "a winner row has no line")
        elif set(sides) == {"YES", "NO"}:
            if any(r["line"] for r in rows):
                problems.append(name + "a yes/no row has no line")
        elif any(x is None for x in lines):
            problems.append(name + "a numeric line is required on both rows")
            continue
        elif set(sides) == {"HOME", "AWAY"}:
            if abs(lines[0] + lines[1]) > 1e-9:
                problems.append(name + "the two handicap lines must be equal and opposite")
        elif lines[0] != lines[1]:
            problems.append(name + "both rows carry the same line")
        for r in rows:
            if r["availability_basis"] not in AVAILABILITY:
                problems.append(name + f"availability_basis must be one of {'/'.join(AVAILABILITY)}")
            if r["centre"] and _number(r["centre"]) is None:
                problems.append(name + "centre must be a number or empty")
            if not (r["result_source"] == "NONE_FOUND" or re.match(r"https?://\S+$", r["result_source"])):
                problems.append(name + "result_source is the page that will show this result, or NONE_FOUND")
            if r["lean"] not in ("", "LEAN"):
                problems.append(name + "lean is empty or LEAN")
        ps = [_p(r["p"]) for r in rows]
        unpriced = all(r["p"] == "UNPRICED" for r in rows)
        if unpriced:
            if sum(r["lean"] == "LEAN" for r in rows) > 1:
                problems.append(name + "at most one side of an UNPRICED line is the lean")
        elif any(x is None for x in ps):
            problems.append(name + "give a probability strictly between 0 and 1 for every side, or UNPRICED on every side")
            continue
        else:
            whole = lines[0] is not None and float(abs(lines[0])).is_integer()
            total = sum(ps)
            if not ((0.80 if whole else 0.98) <= total <= 1.02):
                problems.append(name + f"the sides' probabilities sum to {total:.3f}; they must sum to 1 (a whole-number line may leave room for a push)")
                continue
            if any(r["lean"] for r in rows):
                problems.append(name + "lean applies only to an UNPRICED line")
        derived[label] = dict(rows=rows, ps=ps, unpriced=unpriced, family=family, lines=lines)
    required = required_facts(meta.get("sport", ""), root) if meta.get("sport") else []
    seen = {}
    for r in facts:
        name = f"FACTS {r['side']} {r['field']}: "
        if r["side"].upper() not in ("HOME", "AWAY"):
            problems.append(name + "side is HOME or AWAY")
        if (r["side"].upper(), r["field"]) in seen:
            problems.append(name + "listed twice")
        seen[(r["side"].upper(), r["field"])] = r
        if not r["value"]:
            problems.append(name + "value is required; write MISSING and the reason in source when it could not be found")
        elif r["value"] != "MISSING":
            if not re.match(r"https?://\S+$", r["source"]):
                problems.append(name + "an observed value needs its source page")
            try:
                T.clock(r["observed_at"], "observed_at")
            except ValueError:
                problems.append(name + "an observed value needs an offset-aware observed_at")
    for side in ("HOME", "AWAY"):
        for f in required:
            if (side, f) not in seen:
                problems.append(f"FACTS {side} {f}: required for {meta.get('sport')}; write MISSING with the reason if not found")
    derived["_facts"] = dict(required=2 * len(required), observed=sum(1 for (s, f), r in seen.items() if f in required and r["value"] not in ("", "MISSING")))
    return problems, derived


def _flags(row: dict, p, favoured: bool, line) -> list[str]:
    flags = []
    if p is None:
        return ["UNPRICED"] + (["NO_RESULT_SOURCE"] if row["result_source"] == "NONE_FOUND" else [])
    if favoured and abs(p - 0.5) < NO_DIRECTION:
        flags.append("NO_DIRECTION")
    if row["availability_basis"] == "UNMEASURED":
        flags.append("UNMEASURED_AVAILABILITY_PRICED")
    centre = _number(row["centre"]) if row["centre"] else None
    side = row["side"].upper()
    if favoured and centre is not None and line is not None:
        if (side == "OVER" and centre < line) or (side == "UNDER" and centre > line):
            flags.append("CONTRADICTS_OWN_CENTRE")
        # centre on a side row is that side's expected margin; the side covers when its margin exceeds minus its line
        if side in ("HOME", "AWAY") and centre < -line:
            flags.append("CONTRADICTS_OWN_CENTRE")
    if favoured and side in ("HOME", "AWAY") and line is not None and line > 0:
        flags.append("PLUS_HANDICAP")
    if row["result_source"] == "NONE_FOUND":
        flags.append("NO_RESULT_SOURCE")
    return flags


def rows_for(card_key: str, gid: str, derived: dict) -> list[dict]:
    out, favoured = [], []
    for label, d in derived.items():
        if label == "_facts":
            continue
        best = None if d["unpriced"] else max(range(len(d["rows"])), key=lambda i: (d["ps"][i], -i))
        for i, r in enumerate(d["rows"]):
            p = None if d["unpriced"] else d["ps"][i]
            fav = best == i
            row = dict(card_key=card_key, game_id=gid, **{k: r[k] for k in PICK_COLUMNS}, favoured="Y" if fav else "", rank="",
                       flags=";".join(_flags(r, p, fav, d["lines"][i])))
            row["side"] = r["side"].upper()
            out.append(row)
            if fav:
                favoured.append((-p, label, row))
    # Rank is a fixed function of the stated numbers: highest stated p first, one side per line, label order on ties.
    for n, (_, _, row) in enumerate(sorted(favoured, key=lambda x: (x[0], x[1])), start=1):
        row["rank"] = str(n)
    return out


def intake(drop, out, root=ROOT) -> dict:
    drop, out = Path(drop), Path(out)
    if out.exists():
        raise OneChatError(f"{out} already exists; an intake is written once")
    # Earliest saved first, so a card repeated in later snapshots of the same mini is taken from its first saved copy.
    files = sorted((p for p in drop.rglob("*") if p.is_file() and p.suffix.lower() in (".md", ".txt")), key=lambda p: (p.stat().st_mtime, p.as_posix()))
    cards, picks, facts, seen = [], [], [], {}
    for path in files:
        data = path.read_bytes()
        text = data.decode("utf-8", errors="replace").replace("\r\n", "\n")
        saved = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(timespec="seconds")
        base = dict(file=path.relative_to(drop).as_posix(), file_sha256=sha(data), file_saved_at=saved)
        blocks = list(BLOCK.finditer(text))
        if not blocks:
            cards.append(dict(base, card_key="", game_id="", status="NO_BLOCK", problems="no ONECHAT_V1 block; retained as research without numbers"))
            continue
        for m in blocks:
            key, body = m["key"], m["body"]
            row = dict(base, card_key=key, block_sha256=sha(body.encode("utf-8")))
            try:
                meta, pk, fc = parse(body)
                problems, derived = check(meta, pk, fc, key, root)
            except OneChatError as exc:
                cards.append(dict(row, game_id="", status="REFUSED", problems=str(exc)))
                continue
            row.update({f: meta.get(f, "") for f in HEADER if f in CARD_FIELDS})
            if key in seen and seen[key] != row["block_sha256"]:
                problems.append("card_key already used by a different block in this drop")
            if problems:
                cards.append(dict(row, game_id="", status="REFUSED", problems=" | ".join(problems)))
                continue
            if key in seen:  # the same block saved in a later snapshot of the same mini: keep the earliest saved copy
                continue
            seen[key] = row["block_sha256"]
            gid = game_id(meta)
            mine = rows_for(key, gid, derived)
            labels = {r["label"] for r in mine}
            cards.append(dict(row, game_id=gid, status="ADMITTED", problems="", supplied_lines=len(labels),
                              priced_lines=len({r["label"] for r in mine if r["p"] != "UNPRICED"}),
                              facts_required=derived["_facts"]["required"], facts_observed=derived["_facts"]["observed"]))
            picks += mine
            facts += [dict(card_key=key, game_id=gid, **{k: r[k] for k in FACT_COLUMNS}, status="MISSING" if r["value"] == "MISSING" else "OBSERVED") for r in fc]
    # One game, one card: when a second admitted card covers the same game, the earliest saved file is the card of record.
    first = {}
    for c in sorted((c for c in cards if c["status"] == "ADMITTED"), key=lambda c: (c["file_saved_at"], c["card_key"])):
        if c["game_id"] in first:
            c["status"], c["problems"] = "DUPLICATE_GAME", f"game already carded by {first[c['game_id']]}"
        else:
            first[c["game_id"]] = c["card_key"]
    out.mkdir(parents=True)
    (out / "CARDS.csv").write_bytes(csv_bytes(CARD_FIELDS, cards))
    (out / "PICKS.csv").write_bytes(csv_bytes(ROW_FIELDS, picks))
    (out / "FACTS.csv").write_bytes(csv_bytes(FACT_FIELDS, facts))
    counts = {s: sum(c["status"] == s for c in cards) for s in ("ADMITTED", "REFUSED", "NO_BLOCK", "DUPLICATE_GAME")}
    lines_all = sum(int(c.get("supplied_lines") or 0) for c in cards if c["status"] == "ADMITTED")
    lines_priced = sum(int(c.get("priced_lines") or 0) for c in cards if c["status"] == "ADMITTED")
    summary = dict(rule=RULE, files=len(files), **counts, supplied_lines=lines_all, priced_lines=lines_priced,
                   recorded_at=datetime.now(timezone.utc).isoformat(timespec="seconds"))
    (out / "INTAKE_RECEIPT.csv").write_bytes(csv_bytes(tuple(summary), [summary]))
    return summary


# ---------------------------------------------------------------------------------------------------------------- scoring

OUTCOME_FIELDS = ("card_key", "label", "side", "grade", "actual_start", "settled_at", "final_source", "final_capture_sha256")


def _mean_interval(values: list[float]) -> dict:
    n = len(values)
    mean = sum(values) / n if n else float("nan")
    if n < 2:
        return dict(n=n, mean=mean, lo=float("nan"), hi=float("nan"))
    from scipy import stats
    sd = math.sqrt(sum((v - mean) ** 2 for v in values) / (n - 1))
    half = float(stats.t.ppf(0.975, n - 1)) * sd / math.sqrt(n)
    return dict(n=n, mean=mean, lo=mean - half, hi=mean + half)


def _slope(ps: list[float], ys: list[int]):
    """Calibration slope and intercept: logistic regression of the outcome on the logit of the stated p (1 is calibrated)."""
    if len(ps) < 20 or len(set(ys)) < 2:
        return None
    import numpy as np
    x = np.log(np.clip(ps, 1e-6, 1 - 1e-6) / (1 - np.clip(ps, 1e-6, 1 - 1e-6)))
    X, y, b = np.column_stack([np.ones_like(x), x]), np.array(ys, float), np.zeros(2)
    for _ in range(50):
        mu = 1 / (1 + np.exp(-X @ b))
        H = X.T @ (X * (mu * (1 - mu))[:, None]) + 1e-9 * np.eye(2)
        step = np.linalg.solve(H, X.T @ (y - mu))
        b += step
        if abs(step).max() < 1e-9:
            break
    return dict(intercept=float(b[0]), slope=float(b[1]))


def timing_label(card: dict, actual_start: str) -> str:
    """TIMING-v3: research that began, and saw the game not started, before the first play is a forecast of record."""
    try:
        start = T.clock(actual_start, "actual_start")
        began, seen = T.clock(card["research_start_at"], "research_start_at"), T.clock(card["not_started_observed_at"], "not_started_observed_at")
    except ValueError:
        return "TIMING_UNKNOWN"
    if card["outcome_exposure"].strip().upper() != "NONE":
        return "OUTCOME_EXPOSED"
    if began > start or seen > start:
        return "POST_START"
    saved = T.clock(card["file_saved_at"], "file_saved_at")
    return "PRE_START_SAVED" if saved <= start else "PRE_START_RESEARCH_SAVED_LATER"


def score(intakes, outcomes, out, *, on_request=False, cohort=None, baseline=None) -> dict:
    out = Path(out)
    if out.exists():
        raise OneChatError(f"{out} already exists; a score report is written once")
    if on_request and cohort:
        raise OneChatError("--on-request audits every eligible game and cannot be combined with --cohort")
    cards, picks = {}, []
    for folder in intakes:
        for c in read_csv(Path(folder) / "CARDS.csv"):
            if c["status"] == "ADMITTED":
                if c["card_key"] in cards:
                    raise OneChatError(f"card {c['card_key']} appears in two intakes")
                cards[c["card_key"]] = c
        picks += read_csv(Path(folder) / "PICKS.csv")
    grades = {}
    for r in [x for path in ([outcomes] if isinstance(outcomes, (str, Path)) else list(outcomes)) for x in read_csv(path)]:
        if r["grade"] not in TERMINAL + ("UNRESOLVED",):
            raise OneChatError(f"outcome grade {r['grade']!r} is not WIN, LOSS, PUSH, VOID or UNRESOLVED")
        if r["grade"] in TERMINAL and not (re.match(r"https?://\S+$", r["final_source"]) and re.fullmatch(r"[0-9a-f]{64}", r["final_capture_sha256"])):
            raise OneChatError(f"{r['card_key']} {r['label']}: a settled grade needs its result page and the SHA-256 of the saved capture")
        grades[(r["card_key"], r["label"], r["side"].upper())] = r
    base = {(r["card_key"], r["label"], r["side"].upper()): float(r["baseline_p"]) for r in read_csv(baseline)} if baseline else {}
    games, coverage = [], []
    for key, card in cards.items():
        mine = [r for r in picks if r["card_key"] == key and card["game_id"] == r["game_id"]]
        lined = [r for r in mine if r["line"] != ""]                    # supplied two-way lines: the registered measure
        priced = [r for r in lined if r["p"] != "UNPRICED"]
        got = [grades.get((key, r["label"], r["side"])) for r in mine]
        reason = ""
        if not lined:
            reason = "NO_LINED_CONTRACT"
        elif len(priced) < len(lined):
            reason = "UNPRICED_SUPPLIED_LINE"
        elif any(g is None or g["grade"] not in TERMINAL for g in got):
            reason = "NOT_FULLY_SETTLED"
        elif not any(grades[(key, r["label"], r["side"])]["grade"] in DECISIVE for r in priced):
            reason = "NO_DECISIVE_CONTRACT"
        starts = {g["actual_start"] for g in got if g}
        label = timing_label(card, next(iter(starts))) if len(starts) == 1 else "TIMING_UNKNOWN"
        if not reason and label not in ("PRE_START_SAVED", "PRE_START_RESEARCH_SAVED_LATER"):
            reason = label
        settled = max((g["settled_at"] for g in got if g), key=lambda s: T.clock(s, "settled_at"), default="")
        coverage.append(dict(card_key=key, game_id=card["game_id"], sport=card["sport"], competition=card["competition"], timing=label,
                             supplied_lines=card["supplied_lines"], priced_lines=card["priced_lines"], settled_at=settled,
                             eligible="Y" if not reason else "", exclusion=reason))
        if reason:
            continue
        rows = []
        for r in mine:
            if r["p"] == "UNPRICED":
                continue
            g = grades[(key, r["label"], r["side"])]["grade"]
            if g in DECISIVE:
                rows.append(dict(r, y=1 if g == "WIN" else 0, pf=float(r["p"]), baseline=base.get((key, r["label"], r["side"]))))
        games.append(dict(card_key=key, game_id=card["game_id"], sport=card["sport"], timing=label, settled_at=settled, rows=rows))
    games.sort(key=lambda g: (T.clock(g["settled_at"], "settled_at"), g["card_key"]))
    if cohort:
        wanted = [r["card_key"] for r in read_csv(cohort)]
        missing = [k for k in wanted if k not in {g["card_key"] for g in games}]
        if missing:
            raise OneChatError("frozen cohort games are no longer eligible: " + ", ".join(missing[:5]))
        chosen, status = [g for g in games if g["card_key"] in wanted], "READY"
    elif on_request:
        chosen, status = games, "AUDITED_ON_REQUEST"
    elif len(games) >= COHORT_SIZE:
        chosen, status = games[:COHORT_SIZE], "READY"
    else:
        chosen, status = games, "PROGRESS"

    def lined_rows(g):
        return [r for r in g["rows"] if r["line"] != ""]

    diffs = [sum((r["pf"] - r["y"]) ** 2 for r in lined_rows(g)) / len(lined_rows(g)) - 0.25 for g in chosen if lined_rows(g)]
    primary = _mean_interval(diffs)
    rows = [r for g in chosen for r in g["rows"]]
    fav = [r for r in rows if r["favoured"] == "Y"]
    finding = "NOT_ASSESSED"
    if status == "READY":
        finding = "MEETS_REGISTERED_CRITERION" if primary["mean"] <= CRITERION and primary["hi"] < 0 else "DOES_NOT_MEET_REGISTERED_CRITERION"
    tables = []

    def add(table, stratum, sel):
        if not sel:
            return
        ps, ys = [r["pf"] for r in sel], [r["y"] for r in sel]
        tables.append(dict(table=table, stratum=stratum, rows=len(sel), games=len({r["card_key"] for r in sel}),
                           mean_stated_p=round(sum(ps) / len(ps), 4), win_rate=round(sum(ys) / len(ys), 4),
                           brier=round(sum((p - y) ** 2 for p, y in zip(ps, ys)) / len(ps), 4)))

    for lo, hi in zip(BANDS, BANDS[1:]):
        add("calibration_band_favoured", f"[{lo:.2f},{hi:.2f})", [r for r in fav if lo <= r["pf"] < hi])
    for n in ("1", "2"):
        add("rank", n, [r for r in fav if r["rank"] == n])
    for fam in sorted({r["family"] for r in fav}):
        add("family_favoured", fam, [r for r in fav if r["family"] == fam])
    for sp in sorted({g["sport"] for g in chosen}):
        keys = {g["card_key"] for g in chosen if g["sport"] == sp}
        add("sport_all_rows", sp, [r for r in rows if r["card_key"] in keys])
    for tm in sorted({g["timing"] for g in chosen}):
        keys = {g["card_key"] for g in chosen if g["timing"] == tm}
        add("timing_all_rows", tm, [r for r in rows if r["card_key"] in keys])
    for flag in ("NO_DIRECTION", "UNMEASURED_AVAILABILITY_PRICED", "CONTRADICTS_OWN_CENTRE", "PLUS_HANDICAP"):
        add("hypothesis_flag_favoured", flag, [r for r in fav if flag in r["flags"].split(";")])
        add("hypothesis_flag_favoured", "NOT_" + flag, [r for r in fav if flag not in r["flags"].split(";")])
    paired = [r for r in rows if r["baseline"] is not None]
    by_game = {}
    for r in paired:
        by_game.setdefault(r["card_key"], []).append((r["pf"] - r["y"]) ** 2 - (r["baseline"] - r["y"]) ** 2)
    secondary = _mean_interval([sum(v) / len(v) for v in by_game.values()])
    slope = _slope([r["pf"] for r in fav], [r["y"] for r in fav])
    all_lines = sum(int(c["supplied_lines"] or 0) for c in cards.values())
    priced_lines = sum(int(c["priced_lines"] or 0) for c in cards.values())
    summary = dict(rule=RULE, assessment_status=status, finding=finding,
                   decision_window={"READY": f"FIRST_{COHORT_SIZE}_ELIGIBLE_BY_SETTLEMENT", "AUDITED_ON_REQUEST": "ON_REQUEST_ALL_ELIGIBLE_TO_DATE", "PROGRESS": "ALL_ELIGIBLE_TO_DATE"}[status],
                   admitted_cards=len(cards), eligible_games=len(games), games_scored=len(diffs), cohort_size=COHORT_SIZE,
                   brier_minus_quarter_mean=primary["mean"], brier_minus_quarter_lo=primary["lo"], brier_minus_quarter_hi=primary["hi"],
                   criterion=CRITERION, baseline_paired_games=secondary["n"], card_minus_baseline_mean=secondary["mean"],
                   card_minus_baseline_lo=secondary["lo"], card_minus_baseline_hi=secondary["hi"],
                   calibration_intercept="" if slope is None else slope["intercept"], calibration_slope="" if slope is None else slope["slope"],
                   supplied_lines=all_lines, priced_lines=priced_lines, priced_share=priced_lines / all_lines if all_lines else float("nan"),
                   settlement_days=len({g["settled_at"][:10] for g in chosen}),
                   note="Intervals assume independent games; shared dates, teams and competitions make them optimistic. "
                        "An on-request audit never decides the registered assessment.")
    out.mkdir(parents=True)
    (out / "SUMMARY.csv").write_bytes(csv_bytes(tuple(summary), [summary]))
    (out / "COVERAGE.csv").write_bytes(csv_bytes(tuple(coverage[0]) if coverage else ("card_key",), coverage))
    (out / "TABLES.csv").write_bytes(csv_bytes(("table", "stratum", "rows", "games", "mean_stated_p", "win_rate", "brier"), tables))
    (out / "GAME_SCORES.csv").write_bytes(csv_bytes(("card_key", "game_id", "sport", "timing", "settled_at", "lined_rows", "brier_minus_quarter"),
                                                    [dict(g, lined_rows=len(lined_rows(g)), brier_minus_quarter=sum((r["pf"] - r["y"]) ** 2 for r in lined_rows(g)) / len(lined_rows(g)) - 0.25)
                                                     for g in chosen if lined_rows(g)]))
    if status == "READY" and not cohort:
        (out / "COHORT.csv").write_bytes(csv_bytes(("card_key", "game_id", "settled_at"), chosen))
    return summary


def template(sport: str, root=ROOT) -> str:
    facts = required_facts(sport, root)
    lines = ["<!-- BEGIN ONECHAT_V1 <MINI_KEY>-G0001 -->", *[f"{f}: " + (FORMAT if f == "format" else "<MINI_KEY>-G0001" if f == "card_key" else sport if f == "sport" else "")
                                                             for f in HEADER], "", "PICKS", ",".join(PICK_COLUMNS),
             "L1,HANDICAP,HOME,-3.5,0.47,,2.1,NONE,https://", "L1,HANDICAP,AWAY,3.5,0.53,,-2.1,NONE,https://",
             "L2,TOTAL,OVER,158.5,0.55,,160.2,NONE,https://", "L2,TOTAL,UNDER,158.5,0.45,,160.2,NONE,https://", "", "FACTS", ",".join(FACT_COLUMNS)]
    lines += [f"{side},{f},,," for side in ("HOME", "AWAY") for f in facts]
    return "\n".join(lines + ["<!-- END ONECHAT_V1 <MINI_KEY>-G0001 -->"])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("intake")
    a.add_argument("--drop", required=True, type=Path)
    a.add_argument("--out", required=True, type=Path)
    s = sub.add_parser("score")
    s.add_argument("--intake", required=True, nargs="+", type=Path)
    s.add_argument("--outcomes", required=True, nargs="+", type=Path)
    s.add_argument("--out", required=True, type=Path)
    s.add_argument("--on-request", action="store_true")
    s.add_argument("--cohort", type=Path)
    s.add_argument("--baseline", type=Path)
    t = sub.add_parser("template")
    t.add_argument("--sport", required=True)
    args = parser.parse_args(argv)
    try:
        if args.cmd == "intake":
            print(intake(args.drop, args.out))
        elif args.cmd == "score":
            print(score(args.intake, args.outcomes, args.out, on_request=args.on_request, cohort=args.cohort, baseline=args.baseline))
        else:
            print(template(args.sport))
    except OneChatError as exc:
        raise SystemExit(f"{RULE}: {exc}")


if __name__ == "__main__":
    main()
