"""ONE-CHAT-v3: original requests, exact published blobs and current-average inference.

Use research/one_chat/RUNBOOK.md for the active operator flow. Code changes
use protected main; only immutable request/card data publish on forecast-seals.
The evaluator re-fetches server activity, replays imported values from exact
published blobs, accounts for the complete request population and re-hashes
settlement/first-play captures. Historical studies never become new forecasts
merely because they pass a later validator.

The primary confidence sequence targets the average conditional advantage
through the current game and allows drift. A successful assessed prefix and
continuing performance are reported separately. The first 100 are a secondary,
calendar-free descriptive checkpoint. See EVALUATION_PLAN_v27.0.md.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import re
import subprocess
import time
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from ml import picks as P
from ml import timing as T
from ml import forecast_integrity as F

ROOT = Path(__file__).resolve().parents[1]
RULE = "ONE-CHAT-v3"
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
NO_DIRECTION = 0.05         # H-NODIR: a stated p within this of 0.5 (flag only)
BANDS = (0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.9, 1.0)
DECISIVE, TERMINAL = ("WIN", "LOSS"), ("WIN", "LOSS", "PUSH", "VOID")

# Registered assessment constants (EVALUATION_PLAN_v28.0, with forecast_integrity.LAMBDAS). Changing any of them is a
# new registration. BET_CAP and PRIOR_VAR belong to the retired v26 e-process kept only for replay.
ALPHA = 0.05                # e-value threshold 1 / ALPHA = 20
PRACTICAL = 0.01            # running mean advantage required at the crossing
HORIZON = 600               # games after which, without a crossing, advantage is NOT_DEMONSTRATED (v28.0)
D_LOW, D_HIGH = -0.75, 0.25  # bounds of d = 0.25 - Brier
BET_CAP = 0.75              # fraction of the largest safe bet (simulated: about 1% false alarms on a mean-zero null)
PRIOR_VAR = 0.0625          # prior variance of d for the first bets
SPORT_SECTIONS = 11         # sport sections of prompt 1: per-sport claims use 1 / (ALPHA / 11)
SUPPORTED_SPORTS = ("Baseball","Basketball","Cricket","Soccer","Ice Hockey","Tennis","American Football",
                    "Australian Rules","Rugby League","Rugby Union","Other Sports")
COHORT_SIZE = 100
CRITERION = -0.01           # secondary fixed-100 test: mean Brier minus 0.25 at or below this, interval below zero

CARD_FIELDS = ("card_key", "game_id", "status", "problems", "file", "file_sha256", "file_saved_at", "block_sha256", "sport",
               "competition", "home", "away", "scheduled_start", "request_at", "research_start_at", "research_end_at",
               "not_started_source", "not_started_observed_at", "outcome_exposure", "facts_last_observed_at",
               "supplied_lines", "priced_lines", "facts_required", "facts_observed")
ROW_FIELDS = ("card_key", "game_id", "label", "family", "side", "line", "p", "lean", "centre", "availability_basis",
              "result_source", "favoured", "rank", "flags")
FACT_FIELDS = ("card_key", "game_id") + FACT_COLUMNS + ("status",)
INTAKE_FILES = ("CARDS.csv", "PICKS.csv", "FACTS.csv", "INTAKE_RECEIPT.csv")
OUTCOME_FIELDS = ("card_key", "label", "side", "grade", "event_id", "actual_start", "settled_at", "final_source",
                  "final_capture_sha256", "final_capture_path", "first_play_source", "first_play_capture_path",
                  "first_play_capture_sha256", "first_play_excerpt", "cancellation_at", "cancellation_excerpt")

SEALED = "research/one_chat/sealed"
SEALS = SEALED + "/SEALS.csv"
SEAL_FIELDS = ("card_key", "block_sha256", "file_sha256", "sealed_path", "sealed_at_client", "policy_sha256", "policy_commit")
PLAN = "research/external/EVALUATION_PLAN_v28.0.md"
RECEIPTS = SEALED + "/PUSH_RECEIPTS.csv"
RECEIPT_FIELDS = ("before", "after", "pushed_at_server", "ref", "source", "retrieved_at")
SCORES = "research/one_chat/scores"
SEAL_BRANCH = os.environ.get("ONE_CHAT_SEAL_BRANCH", "forecast-seals")
if SEAL_BRANCH != "forecast-seals" and not re.fullmatch(r"test-forecast-seals[A-Za-z0-9_-]*", SEAL_BRANCH):
    # Only the registered branch or an explicitly named rehearsal branch; a rehearsal never touches forecast-seals.
    raise SystemExit(f"ONE_CHAT_SEAL_BRANCH must be forecast-seals or test-forecast-seals*, not {SEAL_BRANCH!r}")
# Local staging and unpublished seal commits are kept per seal branch, so a rehearsal never mixes with the
# registered evaluation. The registered branch keeps the original names.
STAGING = "forecast-staging" if SEAL_BRANCH == "forecast-seals" else f"forecast-staging-{SEAL_BRANCH}"
PENDING_REFS = "refs/forecast-pending" if SEAL_BRANCH == "forecast-seals" else f"refs/forecast-pending-{SEAL_BRANCH}"
REQUEST_INDEX = "research/one_chat/REQUEST_INDEX.csv"
DISPOSITIONS = "research/one_chat/REQUEST_DISPOSITIONS.csv"
ELIGIBLE = "SEALED_PRE_START_SERVER"


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


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def game_id(meta: dict) -> str:
    """One identity per game, whichever chat carded it: sport, competition, the two sides and the start date as written."""
    day = T.clock(meta["scheduled_start"], "scheduled_start").astimezone(timezone.utc).isoformat()
    return "GAME-" + sha("\x1f".join((_slug(meta["sport"]), _slug(meta["competition"]), _slug(meta["home"]), _slug(meta["away"]), day)).encode())[:12].upper()


def required_facts(sport: str, root=ROOT) -> list[str]:
    rows = read_csv(Path(root) / DICTIONARY) if (Path(root) / DICTIONARY).exists() else read_csv(ROOT / DICTIONARY)
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
    if meta.get("sport") not in SUPPORTED_SPORTS:
        problems.append("header: use one of the eleven registered sport sections")
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
    window = None
    if len(clocks) == len(CLOCKS):
        if not clocks["request_at"] <= clocks["research_start_at"] <= clocks["research_end_at"]:
            problems.append("header: request, research start and research end must be in time order")
        elif not clocks["research_start_at"] <= clocks["not_started_observed_at"] <= clocks["research_end_at"]:
            problems.append("header: the not-started observation must be made during the research "
                            "(between research_start_at and research_end_at)")
        else:
            window = (clocks["research_start_at"], clocks["research_end_at"])
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
    seen, last = {}, None
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
                t = T.clock(r["observed_at"], "observed_at")
            except ValueError:
                problems.append(name + "an observed value needs an offset-aware observed_at")
                continue
            if window and not window[0] <= t <= window[1]:
                problems.append(name + "observed_at must fall within the research (between research_start_at and research_end_at)")
            last = t if last is None or t > last else last
    for side in ("HOME", "AWAY"):
        for f in required:
            if (side, f) not in seen:
                problems.append(f"FACTS {side} {f}: required for {meta.get('sport')}; write MISSING with the reason if not found")
    derived["_facts"] = dict(required=2 * len(required), last=last.isoformat() if last else "",
                             observed=sum(1 for (s, f), r in seen.items() if f in required and r["value"] not in ("", "MISSING")))
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


def card_blocks(text: str, root=ROOT):
    """Every block of a card file with its parse/check result: (key, block_sha256, meta, picks, facts, problems, derived)."""
    out = []
    for m in BLOCK.finditer(text.replace("\r\n", "\n")):
        key, body = m["key"], m["body"]
        try:
            meta, pk, fc = parse(body)
            problems, derived = check(meta, pk, fc, key, root)
        except OneChatError as exc:
            meta, pk, fc, problems, derived = {}, [], [], [str(exc)], {}
        out.append((key, sha(body.encode("utf-8")), meta, pk, fc, problems, derived))
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
        saved = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(timespec="seconds")
        base = dict(file=path.relative_to(drop).as_posix(), file_sha256=sha(data), file_saved_at=saved)
        blocks = card_blocks(data.decode("utf-8", errors="replace"), root)
        if not blocks:
            cards.append(dict(base, card_key="", game_id="", status="NO_BLOCK", problems="no ONECHAT_V1 block; retained as research without numbers"))
            continue
        for key, bsha, meta, pk, fc, problems, derived in blocks:
            row = dict(base, **{f: meta.get(f, "") for f in HEADER if f in CARD_FIELDS})
            row.update(card_key=key, block_sha256=bsha)
            if key in seen and seen[key] != bsha:
                problems = problems + ["card_key already used by a different block in this drop"]
            if problems:
                cards.append(dict(row, game_id="", status="REFUSED", problems=" | ".join(problems)))
                continue
            if key in seen:  # the same block saved in a later snapshot of the same mini: keep the earliest saved copy
                continue
            seen[key] = bsha
            gid = game_id(meta)
            mine = rows_for(key, gid, derived)
            labels = {r["label"] for r in mine}
            cards.append(dict(row, game_id=gid, status="ADMITTED", problems="", supplied_lines=len(labels),
                              priced_lines=len({r["label"] for r in mine if r["p"] != "UNPRICED"}),
                              facts_last_observed_at=derived["_facts"]["last"],
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
    summary = dict(rule=RULE, drop=str(drop), files=len(files), **counts, supplied_lines=lines_all, priced_lines=lines_priced,
                   recorded_at=_now())
    (out / "INTAKE_RECEIPT.csv").write_bytes(csv_bytes(tuple(summary), [summary]))
    manifest = [dict(file=name, sha256=sha((out / name).read_bytes())) for name in INTAKE_FILES]
    (out / "MANIFEST.csv").write_bytes(csv_bytes(("file", "sha256"), manifest))
    return summary


# ---------------------------------------------------------------------------------------------------------------- custody

def _git(root, *args, check=True) -> subprocess.CompletedProcess:
    res = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    if check and res.returncode:
        raise OneChatError(f"git {' '.join(args)} failed: {res.stderr.strip()[:300]}")
    return res


def _rel(path, root) -> str | None:
    try:
        return Path(path).resolve().relative_to(Path(root).resolve()).as_posix()
    except ValueError:
        return None


class Repo:
    """One read of the repository's custody state for a whole run: tracked and changed files, what origin/main holds,
    GitHub's first server push time for every commit, and every sealed file's first commit."""

    def __init__(self, root=ROOT, lookup=None):
        self.root = Path(root)
        self.tracked = set(_git(self.root, "ls-files", "-z", check=False).stdout.split("\0")) - {""}
        self.changed = set(_git(self.root, "diff", "--name-only", "-z", "HEAD", check=False).stdout.split("\0")) - {""}
        up = _git(self.root, "rev-parse", "--verify", "-q", "refs/remotes/origin/main", check=False).stdout.strip()
        seal_ref = _git(self.root, "rev-parse", "--verify", "-q", f"refs/remotes/origin/{SEAL_BRANCH}", check=False).stdout.strip()
        self.seal_ref = seal_ref
        self.upstream = set(_git(self.root, "rev-list", *[r for r in (up, seal_ref) if r], check=False).stdout.split()) if up or seal_ref else set()
        # A locally edited mirror is never independent timestamp evidence. GitHub's activity is fetched once, and only
        # when a server time is first needed; a failed fetch is recorded, never read as "no pushes".
        self._lookup = lookup
        self._receipts = None
        self.activity_error = ""
        self._pushed = {}
        self._ancestry = {}
        self._blob_cache = {}
        self._reader = None
        self._content_commits = {}
        raw_log = _git(self.root,"log","--all","--reverse","--format=@%H","--raw","--no-abbrev","--",SEALED,F.REQUEST_ROOT,PLAN,REQUEST_INDEX,check=False).stdout
        current = ""
        for ln in raw_log.splitlines():
            if ln.startswith("@"):
                current = ln[1:]
            elif ln.startswith(":") and "\t" in ln:
                info,name=ln.split("\t",1)
                self._content_commits.setdefault((name,info.split()[3]),[]).append(current)
        self.added = {}
        log = _git(self.root, "log", "--all", "--diff-filter=A", "--format=@%H %cI", "--name-only", "--", SEALED, check=False).stdout
        commit = None
        for line in log.splitlines():
            if line.startswith("@"):
                commit = line[1:].split()
            elif line.strip() and commit:
                self.added[line.strip()] = (commit[0], commit[1])     # log is newest first: the last write is the first add
        self.seals = []
        for ref in (seal_ref, "HEAD"):
            raw = self.blob(ref, SEALS) if ref else None
            if raw:
                self.seals += F.rows(raw)
        pending = request_staging(self.root) / "PENDING.csv"
        if pending.exists():
            self.seals += read_csv(pending)
        unique = {}
        for r in self.seals:
            unique[(r["card_key"], r["block_sha256"], r["sealed_path"])] = r
        self.seals = list(unique.values())
        raw_requests = self.blob(seal_ref, REQUEST_INDEX) if seal_ref else None
        self.requests = F.rows(raw_requests) if raw_requests else []
        raw_dispositions=self.blob(seal_ref,DISPOSITIONS) if seal_ref else None
        self.dispositions=F.rows(raw_dispositions) if raw_dispositions else []
        self.registry_problems = []
        for (path,oid),commits in self._content_commits.items():
            if path==SEALS:
                for c in commits:
                    if c in self.upstream:
                        earlier=self.blob(c,SEALS)
                        latest=self.blob(seal_ref,SEALS) if seal_ref else None
                        if earlier and latest and any(r not in F.rows(latest) for r in F.rows(earlier)):
                            self.registry_problems.append("Published seal registry was rewritten or omitted earlier records")
                            break

    def committed(self, path) -> bool:
        rel = _rel(path, self.root)
        return rel is not None and Path(path).is_file() and self.blob("HEAD", rel) == Path(path).read_bytes()

    def blob(self, commit, path):
        key=(commit,path)
        if key not in self._blob_cache:
            if any(x in commit+path for x in ("\n","\r","\0")):
                raise OneChatError("invalid git object path")
            if self._reader is None:
                self._reader=subprocess.Popen(["git","-C",str(self.root),"cat-file","--batch"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
            self._reader.stdin.write(f"{commit}:{path}\n".encode())
            self._reader.stdin.flush()
            header=self._reader.stdout.readline().decode().strip().split()
            if header[-1:] == ["missing"]:
                raw=None
            elif len(header)==3 and header[1]=="blob":
                raw=self._reader.stdout.read(int(header[2]))
                self._reader.stdout.read(1)
            else:
                raise OneChatError("invalid blob response from git")
            self._blob_cache[key]=raw
        return self._blob_cache[key]

    def __del__(self):
        reader=getattr(self,"_reader",None)
        if reader is not None:
            try:
                reader.stdin.close()
                reader.stdout.close()
                reader.wait(timeout=1)
            except (OSError,subprocess.TimeoutExpired):
                reader.kill()

    def first_content(self, path, digest):
        ref=self.seal_ref or "HEAD"
        raw=self.blob(ref,path)
        if path==PLAN:
            raw=self.blob("refs/remotes/origin/main",path)
        if raw is None or sha(raw)!=digest:
            # Pending, not-yet-pushed objects are still reportable, never eligible.
            refs=_git(self.root,"for-each-ref","--format=%(objectname)",PENDING_REFS,check=False).stdout.split()
            raw=next((self.blob(c,path) for c in refs if self.blob(c,path) is not None and sha(self.blob(c,path))==digest),None)
        if raw is None:
            return ""
        oid=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
        commits=self._content_commits.get((path,oid),[])
        unpublished = ""
        for commit in commits:
            raw = self.blob(commit, path)
            if raw is not None and sha(raw) == digest:
                if commit in self.upstream:
                    return commit
                unpublished = unpublished or commit
        return unpublished

    @property
    def receipts(self):
        if self._receipts is None:
            try:
                live = (self._lookup or github_push_activity)(self.root)
            except OneChatError as exc:
                self.activity_error, live = str(exc), []
            self.live_receipts = live
            self._receipts = sorted(((T.clock(r["pushed_at_server"], "pushed_at_server"), r) for r in live
                                     if r.get("ref") in ("refs/heads/main", f"refs/heads/{SEAL_BRANCH}")), key=lambda x: x[0])
        return self._receipts

    def pushed_at(self, commit: str, committed_at: str = "") -> str:
        """GitHub's server time of the first push to main or the seal branch that carried the commit ("" if none)."""
        if commit not in self._pushed:
            found = ""
            for when, r in self.receipts:
                if r["after"] not in self._ancestry:
                    self._ancestry[r["after"]]=set(_git(self.root,"rev-list",r["after"],check=False).stdout.split())
                if commit in self._ancestry[r["after"]]:
                    found = r["pushed_at_server"]
                    break
            self._pushed[commit] = found
        return self._pushed[commit]


def committed(path, root=ROOT) -> bool:
    """The file is tracked by git and its working bytes equal HEAD's."""
    return Repo(root).committed(path)


def verify_intake(folder, root=ROOT, require_committed=True, repo=None) -> list[str]:
    folder = Path(folder)
    if not (folder / "MANIFEST.csv").exists():
        return [f"{folder}: no MANIFEST.csv; intakes written before v26.0 must be re-run"]
    problems = []
    rows = {r["file"]: r["sha256"] for r in read_csv(folder / "MANIFEST.csv")}
    if set(rows) != set(INTAKE_FILES):
        problems.append(f"{folder}: MANIFEST.csv must list {', '.join(INTAKE_FILES)}")
    for name, digest in rows.items():
        if not (folder / name).exists() or sha((folder / name).read_bytes()) != digest:
            problems.append(f"{folder}/{name}: bytes differ from MANIFEST.csv")
    if require_committed:
        repo = repo or Repo(root)
        for name in ("MANIFEST.csv", *INTAKE_FILES):
            if not repo.committed(folder / name):
                problems.append(f"{folder}/{name}: not committed, or changed since the last commit")
    return problems


def _remote_slug(root) -> str | None:
    url = _git(root, "remote", "get-url", "origin", check=False).stdout.strip()
    m = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?$", url)
    return f"{m[1]}/{m[2]}" if m else None


def github_push_activity(root=ROOT) -> list[dict]:
    """GitHub's own record of pushes to main and the seal branch (server timestamps), every page.

    Empty for a remote that is not on GitHub; raises OneChatError when GitHub cannot be read, so a failed fetch is never
    mistaken for an absence of pushes."""
    slug = _remote_slug(root)
    if not slug:
        return []
    res = subprocess.run(["gh", "api", "--paginate", "--slurp", f"repos/{slug}/activity?per_page=100"],
                         capture_output=True, text=True)
    if res.returncode:
        raise OneChatError("GitHub push activity could not be fetched (gh api): " + (res.stderr or "").strip()[:200])
    out = []
    for page in json.loads(res.stdout):
        for event in page:
            if event.get("activity_type") in ("push","pr_merge","merge_queue_merge") and event.get("ref") in ("refs/heads/main",f"refs/heads/{SEAL_BRANCH}"):
                out.append(dict(before=event["before"],after=event["after"],pushed_at_server=event["timestamp"],ref=event["ref"]))
    return out


def record_receipts(root=ROOT, lookup=None) -> int:
    """Append any push activity not yet recorded to PUSH_RECEIPTS.csv. Returns the number added."""
    root = Path(root)
    _git(root,"fetch","-q","origin",SEAL_BRANCH,check=False)
    path = root / RECEIPTS
    have = {(r["after"], r["pushed_at_server"]) for r in read_csv(path)} if path.exists() else set()
    found = (lookup or github_push_activity)(root)
    new = []
    for r in found:
        key = (r.get("after", ""), r.get("pushed_at_server", ""))
        if all(key) and key not in have:
            have.add(key)
            new.append(dict(r, source="github-activity-api", retrieved_at=_now()))
    if new:
        path.parent.mkdir(parents=True, exist_ok=True)
        data = path.read_bytes() if path.exists() else b""
        body = csv_bytes(RECEIPT_FIELDS, sorted(new, key=lambda r: r["pushed_at_server"]))
        path.write_bytes(data + (body.split(b"\n", 1)[1] if data else body))
    return len(new)


def request_staging(root):
    rel = _git(root, "rev-parse", "--git-path", STAGING).stdout.strip()
    path = Path(rel)
    return path if path.is_absolute() else Path(root) / path


def publish_seal_tree(root, payload, push=True):
    """Only declared data blobs are published; HEAD, the index and main are untouched."""
    _git(root, "fetch", "-q", "origin", SEAL_BRANCH, check=False)
    ref = f"refs/remotes/origin/{SEAL_BRANCH}"
    base = _git(root, "rev-parse", "--verify", "-q", ref, check=False).stdout.strip()
    if not base:
        base = _git(root, "rev-parse", "refs/remotes/origin/main").stdout.strip()
    with tempfile.TemporaryDirectory(prefix="forecast-index-") as temp:
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(temp) / "index"))
        def run(*args, data=None):
            r = subprocess.run(["git", "-C", str(root), *args], input=data, capture_output=True, env=env)
            if r.returncode:
                raise OneChatError(r.stderr.decode(errors="replace"))
            return r.stdout.decode().strip()
        run("read-tree", base)
        reader = Repo(root)
        sources=[]
        for i,(name, raw) in enumerate(payload.items()):
            old = reader.blob(base,name)
            if old is not None and old != raw and name not in (SEALS, REQUEST_INDEX,DISPOSITIONS):
                raise OneChatError("published request/card blobs are immutable: " + name)
            if old is not None and name in (SEALS,REQUEST_INDEX,DISPOSITIONS) and any(r not in F.rows(raw) for r in F.rows(old)):
                raise OneChatError("publication would drop or alter an earlier registry entry; refresh and retry")
            file=Path(temp)/f"blob-{i}"
            file.write_bytes(raw)
            sources.append(file.as_posix())
        blobs=run("hash-object","-w","--stdin-paths",data=("\n".join(sources)+"\n").encode()).splitlines()
        entries="".join(f"100644 {blob}\t{name}\n" for blob,name in zip(blobs,payload))
        run("update-index","--index-info",data=entries.encode())
        tree = run("write-tree")
        commit = run("commit-tree", tree, "-p", base, "-m", f"Publish immutable forecast data ({RULE})")
    _git(root, "update-ref", f"{PENDING_REFS}/{commit}", commit)
    if push:
        result = _git(root, "push", "origin", f"{commit}:refs/heads/{SEAL_BRANCH}", check=False)
        if result.returncode:
            raise OneChatError("seal push refused; no force or main push attempted: " + result.stderr.strip())
        _git(root, "fetch", "-q", "origin", SEAL_BRANCH)
    return commit


def publish_request(key, root=ROOT):
    return publish_requests([key],root)


def publish_requests(keys,root=ROOT):
    repo = Repo(root)
    index=list(repo.requests)
    payload={}
    changed=False
    for key in keys:
        folder=request_staging(root)/F.request_path(key)
        payload.update({F.request_path(key)+"/"+name:(folder/name).read_bytes() for name in (*F.REQUEST_FILES,"MANIFEST.csv")})
        event=F.rows(payload[F.request_path(key)+"/EVENT.csv"])[0]
        row=dict(card_key=key,event_id=event["event_id"],sport=event["sport"],competition=event["competition"],scheduled_start=event["scheduled_start"],
                 request_sha256=sha(payload[F.request_path(key)+"/REQUEST.txt"]),status="REQUESTED")
        if any(r["card_key"]==key and r!=row for r in index):
            raise OneChatError("request identity already registered")
        if row not in index:
            index.append(row)
            changed=True
    if not changed:
        return repo.seal_ref
    payload[REQUEST_INDEX] = csv_bytes(tuple(row),index)
    return publish_seal_tree(root,payload)


def request_registration(repo,key,payload):
    """First independently published index entry carrying these exact request bytes."""
    cache=getattr(repo,"_request_cache",{})
    identity=(key,sha(payload["MANIFEST.csv"]))
    if identity in cache:
        return cache[identity]
    matches=[]
    for (path,_),commits in repo._content_commits.items():
        if path!=REQUEST_INDEX:
            continue
        for commit in commits:
            if commit not in repo.upstream:
                continue
            index=repo.blob(commit,REQUEST_INDEX)
            if not index or not any(r["card_key"]==key and r["request_sha256"]==sha(payload["REQUEST.txt"]) for r in F.rows(index)):
                continue
            if any(repo.blob(commit,F.request_path(key)+"/"+name)!=raw for name,raw in payload.items()):
                continue
            when=repo.pushed_at(commit)
            if when:
                matches.append((T.clock(when,"request publication"),commit,when))
    result=min(matches) if matches else None
    cache[identity]=result
    repo._request_cache=cache
    return result


def request_disposition(key,status,reason,root=ROOT):
    repo=Repo(root)
    if key not in {r["card_key"] for r in repo.requests} or not reason.strip():
        raise OneChatError("a registered request and an explicit disposition reason are required")
    if key in {r["card_key"] for r in repo.seals}:
        raise OneChatError("a sealed forecast cannot be removed by a request disposition; intake and settle it")
    row=dict(card_key=key,status=status,reason=reason)
    if any(r["card_key"]==key and r!=row for r in repo.dispositions):
        raise OneChatError("an earlier terminal request disposition is immutable")
    rows=repo.dispositions if row in repo.dispositions else repo.dispositions+[row]
    return publish_seal_tree(root,{DISPOSITIONS:csv_bytes(tuple(row),rows)})


def seal(files, root=ROOT, *, push=True, lookup=None, wait=(0, 3, 6, 12)) -> dict:
    """Publish exact card and original-request blobs on the data-only branch."""
    root = Path(root)
    repo = Repo(root, lookup=lookup)
    existing = {r["file_sha256"] for r in repo.seals}
    rows, payload = [], {}
    old = {r["block_sha256"]: r for r in repo.seals}
    plan=repo.blob("refs/remotes/origin/main",PLAN)
    if plan is None:
        raise OneChatError("publish the current evaluation registration on main before sealing forecasts")
    policy_commit=repo.first_content(PLAN,sha(plan))
    policy_time=repo.pushed_at(policy_commit) if policy_commit else ""
    if not policy_time:
        raise OneChatError("current registration has no independently verified main publication time"
                           + (f" ({repo.activity_error})" if repo.activity_error else ""))
    for file in map(Path, files):
        raw = file.read_bytes()
        blocks = card_blocks(raw.decode("utf-8"), root)
        if not blocks or any(x[5] for x in blocks):
            raise OneChatError("not sealed: incomplete or invalid card")
        digest = sha(raw)
        if digest in existing:
            continue
        path = f"{SEALED}/{digest}.md"
        payload[path] = raw
        for key, block_sha, meta, pk, fc, problems, derived in blocks:
            if any(r["card_key"]==key and r["block_sha256"]!=block_sha for r in repo.seals):
                raise OneChatError(key+": an earlier forecast is already sealed; never replace its block")
            folder = request_staging(root) / F.request_path(key)
            if not folder.exists():
                folder = root / F.request_path(key)
            request = {name: (folder / name).read_bytes() for name in (*F.REQUEST_FILES, "MANIFEST.csv") if (folder / name).exists()}
            if len(request) != 4:
                raise OneChatError(f"{key}: register the unchanged original request and contract definitions before sealing")
            problems = F.request_problems(request, meta, pk)
            if problems:
                raise OneChatError("not sealed: " + " | ".join(problems))
            registration=request_registration(repo,key,request)
            if (registration is None or registration[0]>T.clock(meta["research_start_at"],"research start")
                    or registration[0]<T.clock(policy_time,"policy publication")):
                raise OneChatError(key+": request must be independently published after the policy and before research starts")
            for name, data in request.items():
                payload[F.request_path(key) + "/" + name] = data
            if block_sha not in old:
                rows.append(dict(card_key=key, block_sha256=block_sha, file_sha256=digest,
                                 sealed_path=path, sealed_at_client=_now(),policy_sha256=sha(plan),policy_commit=policy_commit))
    if not rows:
        return dict(sealed=0, commit="", pushed=False, server_time="", note="nothing new to seal")
    all_rows = list(old.values()) + rows
    payload[SEALS] = csv_bytes(SEAL_FIELDS, all_rows)
    commit = publish_seal_tree(root, payload, push)
    staging = request_staging(root)
    staging.mkdir(parents=True, exist_ok=True)
    (staging / "PENDING.csv").write_bytes(csv_bytes(SEAL_FIELDS, all_rows))
    result = dict(sealed=len(rows), commit=commit, pushed=push, server_time="", branch=SEAL_BRANCH)
    if push:
        for delay in wait:
            if delay:
                time.sleep(delay)
            t = Repo(root, lookup=lookup).pushed_at(commit)
            if t:
                result["server_time"] = t
                break
    return result


def server_time(root, commit: str) -> str:
    """GitHub's server time of the first push that carried the commit, fetched live (never from the receipts mirror)."""
    return Repo(root).pushed_at(commit)


def seal_evidence(repo, block_sha: str) -> dict:
    """How the card's exact block was sealed: class, time and its basis."""
    rows = [r for r in repo.seals if r["block_sha256"] == block_sha]
    if not rows:
        return dict(seal="UNSEALED", seal_time="", seal_basis="")
    for r in rows:
        f = repo.root / r["sealed_path"]
        commit = repo.first_content(r["sealed_path"], r["file_sha256"])
        if not commit:
            return dict(seal="SEALED_NOT_COMMITTED", seal_time="", seal_basis="")
        raw = repo.blob(commit, r["sealed_path"])
        if raw is None or block_sha not in {x[1] for x in card_blocks(raw.decode("utf-8"), repo.root)}:
            continue
        committed_at = _git(repo.root, "show", "-s", "--format=%cI", commit).stdout.strip()
        original_seals = repo.blob(commit, SEALS)
        if original_seals is None or not any(x["block_sha256"] == block_sha and x["file_sha256"] == r["file_sha256"]
                                              and x["sealed_path"] == r["sealed_path"] for x in F.rows(original_seals)):
            return dict(seal="SEAL_METADATA_NOT_BOUND", seal_time="", seal_basis="")
        key, _, meta, pk, fc, problems, derived = next(x for x in card_blocks(raw.decode("utf-8"), repo.root) if x[1] == block_sha)
        request = {name: repo.blob(commit, F.request_path(key) + "/" + name) for name in (*F.REQUEST_FILES, "MANIFEST.csv")}
        if any(v is None for v in request.values()):
            return dict(seal="NO_ORIGINAL_REQUEST", seal_time="", seal_basis="")
        manifest = {x["file"]: x["sha256"] for x in F.rows(request["MANIFEST.csv"])}
        if set(manifest) != set(F.REQUEST_FILES) or any(sha(request[name]) != manifest[name] for name in F.REQUEST_FILES):
            return dict(seal="REQUEST_CHANGED", seal_time="", seal_basis="")
        problems += F.request_problems(request, meta, pk)
        if problems:
            return dict(seal="REQUEST_OR_CARD_INVALID", seal_time="", seal_basis="")
        if commit not in repo.upstream:
            return dict(seal="SEALED_NOT_PUSHED", seal_time=committed_at, seal_basis="COMMITTER_TIME", seal_commit=commit)
        pushed = repo.pushed_at(commit, committed_at)
        policy=repo.blob(r.get("policy_commit",""),PLAN) if r.get("policy_commit") else None
        policy_time=repo.pushed_at(r["policy_commit"]) if policy is not None else ""
        if (policy is None or sha(policy)!=r.get("policy_sha256") or not policy_time
                or (pushed and T.clock(policy_time,"policy publication")>T.clock(pushed,"forecast publication"))):
            return dict(seal="REGISTRATION_NOT_PREDECLARED",seal_time="",seal_basis="")
        registration=request_registration(repo,key,request)
        if (registration is None or registration[0]>T.clock(meta["research_start_at"],"research start")
                or registration[0]<T.clock(policy_time,"policy publication")):
            return dict(seal="REQUEST_NOT_PUBLISHED_BEFORE_RESEARCH",seal_time="",seal_basis="")
        return dict(seal="SEALED", seal_time=pushed or committed_at, seal_basis="SERVER_PUSH_TIME" if pushed else "COMMITTER_TIME", seal_commit=commit,
                    verified_meta=meta, verified_picks=pk, verified_derived=derived, verified_facts=fc,
                    request_contracts=F.rows(request["CONTRACTS.csv"]), request_event=F.rows(request["EVENT.csv"])[0])
    return dict(seal="SEAL_FILE_CHANGED", seal_time="", seal_basis="")


# ---------------------------------------------------------------------------------------------------------------- scoring

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


def e_process(ds: list[float], m: float = 0.0) -> list[dict]:
    """Legacy conditional-mean diagnostic, retained for replay; not the v27 decision.

    Wealth E_n = prod (1 + lambda_i (d_i - m)); lambda_i is chosen from earlier games only (predictable plug-in), between 0
    and BET_CAP / (m - D_LOW), so every factor stays positive. Under H0 the wealth is a nonnegative supermartingale, and by
    Ville's inequality the chance that it ever reaches 1/alpha is at most alpha, however often it is looked at.
    """
    cap = BET_CAP / (m - D_LOW)
    wealth, n, total, squares, mean, var, out = 1.0, 0, 0.0, 0.0, m, PRIOR_VAR, []
    for d in ds:
        edge = mean - m
        lam = min(max(edge / (var + edge * edge), 0.0), cap)
        wealth *= 1 + lam * (d - m)
        n, total, squares = n + 1, total + d, squares + d * d
        # predictable estimates for the next bet: shrunk toward m with one pseudo-game of prior variance
        mean = (m + total) / (n + 1)
        var = max((PRIOR_VAR + squares - 2 * mean * total + n * mean * mean) / (n + 1), 1e-12)
        out.append(dict(game=n, bet=lam, e_value=wealth))
    return out


def lower_bound(ds: list[float], alpha: float = ALPHA, step: float = 0.0005) -> float | None:
    """95% lower confidence bound for the current average conditional advantage."""
    path = F.confidence_path(ds, alpha)
    return path[-1]["lower_bound_95"] if path else None


def advantage(ds: list[float], alpha: float = ALPHA) -> dict:
    """The registered decision on a fixed sequence of game advantages d."""
    path = F.confidence_path(ds, alpha)
    crossing, running = None, 0.0
    for i, r in enumerate(path):
        running += ds[i]
        r["mean_d"] = running / (i + 1)
        if crossing is None and i < HORIZON and r["e_value"] >= 1 / alpha and r["mean_d"] >= PRACTICAL:
            crossing = i + 1
    if crossing:
        verdict = "DEMONSTRATED"
    elif len(ds) >= HORIZON:
        verdict = "NOT_DEMONSTRATED"
    else:
        verdict = "NOT_YET_DEMONSTRATED"
    return dict(verdict=verdict, games=len(ds), crossed_at_game=crossing or "", e_value=path[-1]["e_value"] if path else 1.0,
                max_e_value=max((r["e_value"] for r in path), default=1.0), mean_d=path[-1]["mean_d"] if path else float("nan"),
                 lower_bound_95=path[-1]["lower_bound_95"] if path else None,
                 assessed_prefix_mean=path[crossing-1]["mean_d"] if crossing else None,
                 assessed_prefix_lower_bound=path[crossing-1]["lower_bound_95"] if crossing else None, path=path)


def timing_label(card: dict, actual_start: str, seal: dict) -> str:
    """TIMING-v3 plus custody: research before first play, nothing of the outcome seen, and a seal GitHub timed before play."""
    try:
        start = T.clock(actual_start, "actual_start")
        began, seen = T.clock(card["research_start_at"], "research_start_at"), T.clock(card["not_started_observed_at"], "not_started_observed_at")
        ended = T.clock(card["research_end_at"], "research_end_at")
        last = T.clock(card["facts_last_observed_at"], "facts_last_observed_at") if card.get("facts_last_observed_at") else ended
    except ValueError:
        return "TIMING_UNKNOWN"
    if card["outcome_exposure"].strip().upper() != "NONE":
        return "OUTCOME_EXPOSED"
    if max(began, seen, ended, last) > start:
        return "POST_START"
    if seal["seal"] != "SEALED":
        return seal["seal"]
    sealed = T.clock(seal["seal_time"], "seal_time")
    if sealed < ended:
        return "CLOCK_INCONSISTENT"
    if sealed > start:
        return "SEALED_AFTER_START"
    return "SEALED_PRE_START_SERVER" if seal["seal_basis"] == "SERVER_PUSH_TIME" else "SEALED_PRE_START_CLIENT"


def _conditional(rows: list[dict]) -> dict:
    """p of each side given that the line is decided (no push): p / (sum of the line's priced sides)."""
    total = {}
    for r in rows:
        if r["p"] != "UNPRICED":
            total[r["label"]] = total.get(r["label"], 0.0) + float(r["p"])
    return {(r["label"], r["side"]): float(r["p"]) / total[r["label"]] for r in rows if r["p"] != "UNPRICED"}


def _read_outcomes(paths, repo, captures, require_committed) -> tuple[dict, list[str]]:
    grades, problems, digests = {}, [], {}
    for path in ([paths] if isinstance(paths, (str, Path)) else list(paths)):
        if require_committed and not repo.committed(path):
            problems.append(f"{path}: outcomes file not committed, or changed since the last commit")
        for r in read_csv(path):
            if r["grade"] not in TERMINAL + ("UNRESOLVED",):
                raise OneChatError(f"outcome grade {r['grade']!r} is not WIN, LOSS, PUSH, VOID or UNRESOLVED")
            if r["grade"] in TERMINAL:
                if not (re.match(r"https?://\S+$", r.get("final_source", "")) and re.fullmatch(r"[0-9a-f]{64}", r.get("final_capture_sha256", ""))):
                    raise OneChatError(f"{r['card_key']} {r['label']}: a settled grade needs its result page and the SHA-256 of the saved capture")
                cap = Path(r.get("final_capture_path", ""))
                if not r.get("final_capture_path"):
                    raise OneChatError(f"{r['card_key']} {r['label']}: final_capture_path is required (the saved result page)")
                if not cap.is_absolute():
                    cap = Path(captures) / cap
                if cap not in digests:
                    digests[cap] = sha(cap.read_bytes()) if cap.exists() else ""
                if digests[cap] != r["final_capture_sha256"]:
                    raise OneChatError(f"{r['card_key']} {r['label']}: capture {cap} is missing or its SHA-256 differs from the outcome row")
                cancelled=r["grade"]=="VOID" and not r.get("actual_start","")
                proof = Path(r.get("first_play_capture_path", ""))
                if not proof.is_absolute():
                    proof = Path(captures) / proof
                raw = proof.read_bytes() if proof.is_file() else b""
                if cancelled:
                    excerpt=r.get("cancellation_excerpt","")
                    if not excerpt or excerpt not in cap.read_text(encoding="utf-8",errors="replace") or not r.get("cancellation_at"):
                        raise OneChatError(r["card_key"]+": captured cancellation evidence is required for a game that never started")
                    if T.clock(r["cancellation_at"],"cancelled at")>T.clock(r["settled_at"],"settled at"):
                        raise OneChatError("cancellation evidence cannot follow its settlement")
                elif not (re.match(r"https?://\S+$", r.get("first_play_source", ""))
                        and raw and sha(raw) == r.get("first_play_capture_sha256")
                        and r.get("first_play_excerpt", "") and r["first_play_excerpt"] in raw.decode("utf-8", errors="replace")):
                    raise OneChatError(f"{r['card_key']}: verified first-play capture, source and exact excerpt are required")
                if not r.get("event_id", "").strip():
                    raise OneChatError(f"{r['card_key']} {r['label']}: event_id (the competition's native match identity) is required")
            key = (r["card_key"], r["label"], r["side"].upper())
            if key in grades and grades[key]["grade"] != r["grade"]:
                raise OneChatError(f"{key}: two outcome rows give different grades")
            grades[key] = r
    cancelled_keys={r["card_key"] for r in grades.values() if r["grade"]=="VOID" and not r.get("actual_start")}
    if any(r["grade"]!="VOID" for r in grades.values() if r["card_key"] in cancelled_keys):
        raise OneChatError("a never-started cancellation must void every contract of the game")
    return grades, problems


def score(intakes, outcomes, out, *, root=ROOT, captures=None, cohort=None, baseline=None, on_request=False,
          require_committed=True) -> dict:
    root, out = Path(root), Path(out)
    captures = Path(captures) if captures else root.parent / "one_chat_captures"
    if out.exists():
        raise OneChatError(f"{out} already exists; a score report is written once")
    custody = []
    if not require_committed:
        custody.append("Diagnostic run without committed-input enforcement; never confirmatory")
    repo = Repo(root)
    custody += repo.registry_problems
    cards, picks, facts = {}, [], {}
    for folder in intakes:
        custody += verify_intake(folder, root, require_committed, repo)
        for c in read_csv(Path(folder) / "CARDS.csv"):
            if c["status"] == "ADMITTED":
                if c["card_key"] in cards:
                    raise OneChatError(f"card {c['card_key']} appears in two intakes")
                cards[c["card_key"]] = c
        picks += read_csv(Path(folder) / "PICKS.csv")
        for r in read_csv(Path(folder) / "FACTS.csv"):
            facts.setdefault(r["card_key"],[]).append(r)
    grades, problems = _read_outcomes(outcomes, repo, captures, require_committed)
    custody += problems
    if baseline is not None:
        raise OneChatError("Freeze sporting baseline probabilities and provenance in the original request CONTRACTS.csv before sealing; post-result comparator files are not admitted")
    base = {}
    seals = {k: seal_evidence(repo, c["block_sha256"]) for k, c in cards.items()}
    # Regenerating a derivative's manifest cannot change the forecast of record.
    for key, card in cards.items():
        seal = seals[key]
        if seal["seal"]=="SEALED" and seal["seal_basis"]!="SERVER_PUSH_TIME":
            custody.append(key+": server publication is not independently verifiable; do not omit it from the registered sequence")
        earlier=[r for r in repo.seals if r["card_key"]==key]
        if earlier and earlier[0]["block_sha256"]!=card["block_sha256"]:
            custody.append(key+": an earlier published block is the forecast of record")
        if seal["seal"] != "SEALED":
            continue
        mine = [r for r in picks if r["card_key"] == key and r["game_id"] == card["game_id"]]
        expected = rows_for(key, card["game_id"], seal["verified_derived"])
        canonical = lambda rs: csv_bytes(ROW_FIELDS, sorted(rs, key=lambda r: (r["label"], r["side"])))
        if canonical(mine) != canonical(expected):
            custody.append(f"{key}: parsed probabilities/contracts/ranks differ from the exact published block")
        expected_facts = [dict(card_key=key,game_id=card["game_id"],**r,status="MISSING" if r["value"]=="MISSING" else "OBSERVED") for r in seal["verified_facts"]]
        fc_csv = lambda rs:csv_bytes(FACT_FIELDS,sorted(rs,key=lambda r:(r["side"],r["field"])))
        if fc_csv(facts.get(key,[]))!=fc_csv(expected_facts):
            custody.append(f"{key}: parsed research facts differ from the published block")
        if any(card.get(f, "") != seal["verified_meta"].get(f, "") for f in HEADER if f in CARD_FIELDS):
            custody.append(f"{key}: intake header differs from the exact published block")
        if card["facts_last_observed_at"] != seal["verified_derived"]["_facts"]["last"]:
            custody.append(f"{key}: intake fact clocks differ from the published block")
        events = {g["event_id"] for (ck, _, _), g in grades.items() if ck == key and g["grade"] in TERMINAL}
        if events and events != {seal["request_event"]["event_id"]}:
            custody.append(f"{key}: settled event identity differs from the frozen original request")
        for r in seal["request_contracts"]:
            if r["baseline_p"]:
                base[(key,r["label"],r["side"].upper())]=float(r["baseline_p"])
    if repo.activity_error:
        custody.append(repo.activity_error)
    missing_sealed = sorted({r["card_key"] for r in repo.seals} - set(cards))
    if missing_sealed:
        custody.append("Sealed games omitted from supplied intakes: " + ", ".join(missing_sealed))
    for r in repo.requests:
        if r["card_key"] not in cards and r["card_key"] not in {d["card_key"] for d in repo.dispositions}:
            custody.append(r["card_key"]+": registered request has no accounted-for card/disposition intake")

    # One game, one card across every intake: the same game identity, or the same native event identity in the outcomes.
    owner = {}
    def find(k):
        while owner.get(k, k) != k:
            k = owner[k]
        return k
    def join(a, b):
        owner[find(a)] = find(b)
    first_by = {}
    for key, c in cards.items():
        mine = [g for (ck, _, _), g in grades.items() if ck == key]
        events = {g["event_id"].strip() for g in mine if g.get("event_id", "").strip()}
        if len(events) > 1:
            raise OneChatError(f"{key}: outcome rows name more than one event_id ({', '.join(sorted(events))})")
        ids = [("game", c["game_id"])] + [("event", e) for e in events]
        for ident in ids:
            if ident in first_by:
                join(key, first_by[ident])
            else:
                first_by[ident] = key
    groups = {}
    for key in cards:
        groups.setdefault(find(key), []).append(key)
    def rank_key(k):
        s = seals[k]
        return (0 if s["seal"] == "SEALED" else 1, s.get("seal_time") or "9999", cards[k]["file_saved_at"], k)
    duplicate = {}
    for members in groups.values():
        keep = min(members, key=rank_key)
        for k in members:
            if k != keep:
                duplicate[k] = keep

    games, coverage = [], []
    for key, card in cards.items():
        mine = [r for r in picks if r["card_key"] == key and card["game_id"] == r["game_id"]]
        lined = [r for r in mine if r["line"] != ""]
        priced = [r for r in lined if r["p"] != "UNPRICED"]
        got = [grades.get((key, r["label"], r["side"])) for r in mine]
        starts = {g["actual_start"] for g in got if g}
        label = timing_label(card, next(iter(starts)), seals[key]) if len(starts) == 1 else "TIMING_UNKNOWN"
        terminal = all(g is not None and g["grade"] in TERMINAL for g in got) and bool(got)
        reason = ""
        if key in duplicate:
            reason = f"DUPLICATE_GAME_OF_{duplicate[key]}"
        elif not lined:
            reason = "NO_LINED_CONTRACT"
        elif len(priced) < len(lined):
            reason = "UNPRICED_SUPPLIED_LINE"
        elif not terminal:
            reason = "NOT_FULLY_SETTLED"
        elif not any(grades[(key, r["label"], r["side"])]["grade"] in DECISIVE for r in priced):
            reason = "NO_DECISIVE_CONTRACT"
        elif label != ELIGIBLE:
            reason = label
        settled = max((g["settled_at"] for g in got if g), key=lambda s: T.clock(s, "settled_at"), default="")
        coverage.append(dict(card_key=key, game_id=card["game_id"], sport=card["sport"], competition=card["competition"],
                             scheduled_start=card["scheduled_start"], timing=label, seal=seals[key]["seal"],
                             seal_time=seals[key].get("seal_time", ""), seal_basis=seals[key].get("seal_basis", ""),
                             supplied_lines=card["supplied_lines"], priced_lines=card["priced_lines"], settled_at=settled,
                             eligible="Y" if not reason else "", exclusion=reason,
                             candidate="Y" if key not in duplicate and seals[key]["seal"] == "SEALED" and lined and len(priced) == len(lined) else ""))
        if reason:
            continue
        cond = _conditional(mine)
        rows = []
        for r in mine:
            if r["p"] == "UNPRICED":
                continue
            g = grades[(key, r["label"], r["side"])]["grade"]
            if g in DECISIVE:
                rows.append(dict(r, y=1 if g == "WIN" else 0, pf=cond[(r["label"], r["side"])], baseline=base.get((key, r["label"], r["side"]))))
        lined_rows = [r for r in rows if r["line"] != ""]
        d = 0.25 - sum((r["pf"] - r["y"]) ** 2 for r in lined_rows) / len(lined_rows)
        games.append(dict(card_key=key, game_id=card["game_id"], sport=card["sport"], timing=label, settled_at=settled,
                          scheduled_start=card["scheduled_start"], rows=rows, d=d))

    for req in repo.requests:
        key=req["card_key"]
        if key not in cards:
            d=next((r for r in repo.dispositions if r["card_key"]==key),{})
            raw=repo.blob(repo.seal_ref,F.request_path(key)+"/CONTRACTS.csv")
            count=len({r["label"] for r in F.rows(raw)}) if raw else 0
            coverage.append(dict(card_key=key,game_id="NATIVE-"+sha(req["event_id"].encode())[:12],sport=req["sport"],competition=req["competition"],
                scheduled_start=req["scheduled_start"],timing="NO_FORECAST",seal="UNSEALED",seal_time="",seal_basis="",
                supplied_lines=count,priced_lines=0,settled_at="",eligible="",exclusion=d.get("status","REQUEST_NOT_ACCOUNTED_FOR")+":"+d.get("reason",""),candidate=""))
    # One fixed sequence, ordered by scheduled start, cut at the first pending candidate.
    order = lambda c: (T.clock(c["scheduled_start"], "scheduled_start"), c["game_id"], c["card_key"])
    pending = sorted((c for c in coverage if c["candidate"] and c["exclusion"] == "NOT_FULLY_SETTLED"), key=order)
    cut = order(pending[0]) if pending else None
    by_key = {g["card_key"]: g for g in games}
    sequence = [by_key[c["card_key"]] for c in sorted((c for c in coverage if c["eligible"]), key=order)
                if cut is None or order(c) < cut]
    held_back = len(games) - len(sequence)
    ds = [g["d"] for g in sequence]
    decision = advantage(ds)
    if custody:
        decision["verdict"] = "NOT_ASSESSABLE"

    # Secondary: the first 100 games of the sequence, frozen once, with a fixed-sample t interval.
    frozen = sorted((root / SCORES).glob("*/COHORT.csv")) if (root / SCORES).exists() else []
    if cohort:
        cohort = Path(cohort)
        receipt = cohort.with_name("COHORT_RECEIPT.csv")
        rec = read_csv(receipt)[0] if receipt.exists() else {}
        wanted = [r["game_id"] for r in read_csv(cohort)]
        if rec.get("cohort_sha256") != sha(cohort.read_bytes()) or int(rec.get("games", 0)) != COHORT_SIZE:
            raise OneChatError("the cohort file does not match its COHORT_RECEIPT.csv (hash and 100 games)")
        if len(set(wanted)) != COHORT_SIZE or len(wanted) != COHORT_SIZE:
            raise OneChatError("a frozen cohort holds exactly 100 distinct games")
        if wanted != [g["game_id"] for g in sequence[:COHORT_SIZE]]:
            raise OneChatError("cohort is not the first 100 games of the complete registered sequence")
        if require_committed and not (repo.committed(cohort) and repo.committed(receipt)):
            custody.append(f"{cohort}: cohort not committed, or changed since the last commit")
        have = {g["game_id"]: g for g in sequence}
        missing = [w for w in wanted if w not in have]
        if missing:
            raise OneChatError("frozen cohort games are no longer in the eligible sequence: " + ", ".join(missing[:5]))
        chosen, cohort_status = [have[w] for w in wanted], "FROZEN_COHORT_REUSED"
    elif len(sequence) >= COHORT_SIZE:
        if frozen:
            raise OneChatError(f"a cohort is already frozen ({frozen[0]}); pass --cohort to reuse it")
        chosen, cohort_status = sequence[:COHORT_SIZE], "COHORT_FROZEN_NOW"
    else:
        chosen, cohort_status = sequence, "COHORT_NOT_YET_FULL"
    fixed = _mean_interval([-g["d"] for g in chosen])
    finding = "NOT_ASSESSED"
    if cohort_status != "COHORT_NOT_YET_FULL" and not custody:
        finding = "MEETS_REGISTERED_CRITERION" if fixed["mean"] <= CRITERION and fixed["hi"] < 0 else "DOES_NOT_MEET_REGISTERED_CRITERION"

    rows = [r for g in sequence for r in g["rows"]]
    fav = [r for r in rows if r["favoured"] == "Y"]
    tables = []

    def add(table, stratum, sel):
        if not sel:
            return
        ps, ys = [r["pf"] for r in sel], [r["y"] for r in sel]
        grouped={}
        for r in sel:
            grouped.setdefault(r["card_key"],[]).append((r["pf"]-r["y"])**2)
        interval=_mean_interval([sum(v)/len(v) for v in grouped.values()])
        tables.append(dict(table=table, stratum=stratum, rows=len(sel), games=len({r["card_key"] for r in sel}),
                           mean_stated_p=round(sum(ps) / len(ps), 4), win_rate=round(sum(ys) / len(ys), 4),
                            brier=round(sum((p - y) ** 2 for p, y in zip(ps, ys)) / len(ps), 4),
                            log_loss=sum(-math.log(p if y else 1-p) for p,y in zip(ps,ys))/len(ps),
                            game_mean_brier=interval["mean"],game_mean_brier_lo=interval["lo"],game_mean_brier_hi=interval["hi"]))

    for lo, hi in zip(BANDS, BANDS[1:]):
        add("calibration_band_favoured", f"[{lo:.2f},{hi:.2f})", [r for r in fav if lo <= r["pf"] < hi])
    for n in ("1", "2"):
        add("rank", n, [r for r in fav if r["rank"] == n])
    for fam in sorted({r["family"] for r in fav}):
        add("family_favoured", fam, [r for r in fav if r["family"] == fam])
    for sp in sorted({g["sport"] for g in sequence}):
        keys = {g["card_key"] for g in sequence if g["sport"] == sp}
        add("sport_all_rows", sp, [r for r in rows if r["card_key"] in keys])
    for flag in ("NO_DIRECTION", "UNMEASURED_AVAILABILITY_PRICED", "CONTRADICTS_OWN_CENTRE", "PLUS_HANDICAP"):
        add("hypothesis_flag_favoured", flag, [r for r in fav if flag in r["flags"].split(";")])
        add("hypothesis_flag_favoured", "NOT_" + flag, [r for r in fav if flag not in r["flags"].split(";")])
    sports = []
    for sp in sorted({g["sport"] for g in sequence}):
        sd = [g["d"] for g in sequence if g["sport"] == sp]
        res = advantage(sd, ALPHA / SPORT_SECTIONS)
        if custody:
            res["verdict"] = "NOT_ASSESSABLE"
        sports.append(dict(sport=sp, games=res["games"], verdict=res["verdict"], crossed_at_game=res["crossed_at_game"],
                           e_value=res["e_value"], threshold=SPORT_SECTIONS / ALPHA, mean_d=res["mean_d"], lower_bound=res["lower_bound_95"]))
    paired = [r for r in rows if r["baseline"] is not None]
    by_game = {}
    for r in paired:
        by_game.setdefault(r["card_key"], []).append((r["pf"] - r["y"]) ** 2 - (r["baseline"] - r["y"]) ** 2)
    secondary = _mean_interval([sum(v) / len(v) for v in by_game.values()])
    slope = _slope([r["pf"] for r in fav], [r["y"] for r in fav])
    all_lines = sum(int(c["supplied_lines"] or 0) for c in coverage)
    priced_lines = sum(int(c["priced_lines"] or 0) for c in coverage)
    summary = dict(rule=RULE, run_label="ON_REQUEST" if on_request else "ROUTINE", advantage=decision["verdict"],
                   games_in_sequence=decision["games"], games_held_back_by_unsettled_earlier_game=held_back,
                   crossed_at_game=decision["crossed_at_game"], e_value=decision["e_value"], max_e_value=decision["max_e_value"],
                   e_threshold=1 / ALPHA, practical_mean_d=PRACTICAL, horizon_games=HORIZON, mean_d=decision["mean_d"],
                   lower_bound_95=decision["lower_bound_95"], custody_problems=len(custody),
                    assessed_prefix_mean=decision["assessed_prefix_mean"],
                    assessed_prefix_lower_bound=decision["assessed_prefix_lower_bound"],
                    statistical_rule=F.STATISTICAL_RULE,
                   cohort_status=cohort_status, cohort_games=len(chosen), cohort_finding=finding,
                   cohort_brier_minus_quarter_mean=fixed["mean"], cohort_brier_minus_quarter_lo=fixed["lo"],
                   cohort_brier_minus_quarter_hi=fixed["hi"], criterion=CRITERION,
                   admitted_cards=len(cards), duplicate_cards=len(duplicate),
                    registered_requests=len(repo.requests),request_dispositions=len(repo.dispositions),
                   sealed_pre_start_server=sum(c["timing"] == ELIGIBLE for c in coverage),
                   sealed_pre_start_client_only=sum(c["timing"] == "SEALED_PRE_START_CLIENT" for c in coverage),
                   unsealed=sum(c["seal"] == "UNSEALED" for c in coverage),
                   baseline_paired_games=secondary["n"], card_minus_baseline_mean=secondary["mean"],
                   card_minus_baseline_lo=secondary["lo"], card_minus_baseline_hi=secondary["hi"],
                   calibration_intercept="" if slope is None else slope["intercept"], calibration_slope="" if slope is None else slope["slope"],
                   supplied_lines=all_lines, priced_lines=priced_lines, priced_share=priced_lines / all_lines if all_lines else float("nan"),
                   settlement_days=len({g["settled_at"][:10] for g in sequence}),
                   note="The e-value test is valid whenever it is read; the t interval assumes independent games. "
                        "Whole-number lines are scored on the probability given no push.")
    out.mkdir(parents=True)
    (out / "SUMMARY.csv").write_bytes(csv_bytes(tuple(summary), [summary]))
    (out / "CUSTODY_PROBLEMS.csv").write_bytes(csv_bytes(("problem",), [dict(problem=p) for p in custody]))
    (out / "COVERAGE.csv").write_bytes(csv_bytes(tuple(coverage[0]) if coverage else ("card_key",), coverage))
    (out / "SEQUENCE.csv").write_bytes(csv_bytes(("game", "card_key", "game_id", "sport", "scheduled_start", "d", "bet", "e_value", "mean_d"),
                                                 [dict(g, game=i + 1, **{k: decision["path"][i][k] for k in ("bet", "e_value", "mean_d")})
                                                  for i, g in enumerate(sequence)]))
    (out / "SPORT_EVIDENCE.csv").write_bytes(csv_bytes(("sport", "games", "verdict", "crossed_at_game", "e_value", "threshold", "mean_d", "lower_bound"), sports))
    (out / "TABLES.csv").write_bytes(csv_bytes(("table", "stratum", "rows", "games", "mean_stated_p", "win_rate", "brier", "log_loss", "game_mean_brier","game_mean_brier_lo","game_mean_brier_hi"), tables))
    if cohort_status == "COHORT_FROZEN_NOW" and not custody:
        data = csv_bytes(("card_key", "game_id", "scheduled_start", "settled_at"), chosen)
        (out / "COHORT.csv").write_bytes(data)
        (out / "COHORT_RECEIPT.csv").write_bytes(csv_bytes(("cohort_sha256", "games", "frozen_at", "rule"),
                                                           [dict(cohort_sha256=sha(data), games=len(chosen), frozen_at=_now(), rule=RULE)]))
    return {k: v for k, v in summary.items() if k != "note"}


def history(rows_csv, out) -> dict:
    """The same anytime-valid test over historical settled cards (card-level, date order). Context only: these cards were
    not sealed, their lines mix supplied and analyst-chosen, and the question was asked after the results were known."""
    import pandas as pd
    out = Path(out)
    if out.exists():
        raise OneChatError(f"{out} already exists")
    r = pd.read_csv(rows_csv)
    r = r[(r.admission != "EXCLUDED") & r.p.notna()]
    res = []
    for name, sel in (("ALL_CARDS_WITH_STATED_P", r), ("CHAT_RESEARCH_SUPPLIED_LINES_P639_ON", r[r.card.str[2:].astype(int) >= 639])):
        cards = (sel.assign(b=(sel.p - sel.y) ** 2).groupby("card").agg(date=("date", "min"), brier=("b", "mean"))
                 .assign(d=lambda f: 0.25 - f.brier).reset_index().sort_values(["date", "card"]))
        a = advantage(list(cards.d))
        res.append(dict(cohort=name, cards=a["games"], verdict_if_it_were_prospective=a["verdict"], crossed_at_card=a["crossed_at_game"],
                        max_e_value=a["max_e_value"], mean_d=a["mean_d"], lower_bound_95=a["lower_bound_95"],
                        evidence_class="HISTORICAL_UNSEALED_OUTCOME_EXPOSED_NOT_CONFIRMATORY"))
    out.mkdir(parents=True)
    (out / "HISTORICAL_EVIDENCE.csv").write_bytes(csv_bytes(tuple(res[0]), res))
    return {r_["cohort"]: (r_["cards"], r_["verdict_if_it_were_prospective"], round(r_["max_e_value"], 2), r_["lower_bound_95"]) for r_ in res}


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
    se = sub.add_parser("seal")
    se.add_argument("--card", required=True, nargs="+", type=Path)
    se.add_argument("--no-push", action="store_true")
    sub.add_parser("receipts")
    request = sub.add_parser("register-request")
    request.add_argument("--source", required=True, type=Path)
    request.add_argument("--event", required=True, type=Path)
    request.add_argument("--contracts", required=True, type=Path)
    request.add_argument("--card-key", required=True)
    disposition=sub.add_parser("disposition")
    disposition.add_argument("--card-key",required=True)
    disposition.add_argument("--status",choices=("NO_FORECAST","CANCELLED","LATE_UNSEALED","UNPRICED"),required=True)
    disposition.add_argument("--reason",required=True)
    s = sub.add_parser("score")
    s.add_argument("--intake", required=True, nargs="+", type=Path)
    s.add_argument("--outcomes", required=True, nargs="+", type=Path)
    s.add_argument("--out", required=True, type=Path)
    s.add_argument("--captures", type=Path)
    s.add_argument("--on-request", action="store_true")
    s.add_argument("--cohort", type=Path)
    s.add_argument("--baseline", type=Path)
    h = sub.add_parser("history")
    h.add_argument("--rows", required=True, type=Path)
    h.add_argument("--out", required=True, type=Path)
    pw = sub.add_parser("power", help="the registered decision's error rate and power, by simulation")
    pw.add_argument("--out", required=True, type=Path)
    pw.add_argument("--runs", type=int, default=200)
    pw.add_argument("--null-runs", type=int, default=400)
    t = sub.add_parser("template")
    t.add_argument("--sport", required=True)
    args = parser.parse_args(argv)
    try:
        if args.cmd == "intake":
            print(intake(args.drop, args.out))
        elif args.cmd == "seal":
            print(seal(args.card, push=not args.no_push))
        elif args.cmd == "receipts":
            print(f"{record_receipts()} new push receipts")
        elif args.cmd == "register-request":
            print(F.register_request(args.source, args.event, args.contracts, args.card_key, request_staging(ROOT)))
            print("request publication: " + publish_request(args.card_key))
        elif args.cmd == "disposition":
            print(request_disposition(args.card_key,args.status,args.reason))
        elif args.cmd == "score":
            print(score(args.intake, args.outcomes, args.out, captures=args.captures, on_request=args.on_request,
                        cohort=args.cohort, baseline=args.baseline))
        elif args.cmd == "power":
            if args.out.exists():
                raise OneChatError(f"{args.out} already exists")
            rows = F.power_study(horizon=HORIZON, runs=args.runs, null_runs=args.null_runs, alpha=ALPHA, practical=PRACTICAL)
            args.out.mkdir(parents=True)
            (args.out / "POWER.csv").write_bytes(csv_bytes(tuple(rows[0]), rows))
            for r in rows:
                print(r)
        elif args.cmd == "history":
            print(history(args.rows, args.out))
        else:
            print(template(args.sport))
    except (OneChatError,ValueError,OSError) as exc:
        raise SystemExit(f"{RULE}: {exc}")


if __name__ == "__main__":
    main()
