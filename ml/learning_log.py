"""A structured learning log for every game, kept for teaching models later (LEARNLOG-v1, owner instruction 2026-11-09).

    python -m ml learning-log init  --mini M --key K --game GAME.csv     after the card is written (prompt 1)
    python -m ml learning-log check --key K --stage pregame              before the card's commit (prompt 1)
    python -m ml learning-log check --key K --stage settled              after OUTCOME and GRADES are written (prompt 3)
    python -m ml learning-log link  --key K --canonical P-639            when prompt 4 assigns the canonical ID
    python -m ml learning-log build --out NEW_FOLDER                     the training dataset (prompt 6)

Each game gets ``research/learning_log/<LOCAL_KEY>/`` with fixed CSVs:

    CARD.csv          identity, timing, reference and card version (one row)
    CONTRACTS.csv     every priced contract with reference, baseline and the card's final p, copied from PICKS_V2
    FEATURES.csv      the sport's required pregame features for both sides, each with its source and known-at time,
                      or MISSING with the reason (research/learning_log/FEATURE_DICTIONARY.csv)
    AVAILABILITY.csv  dated availability snapshots (starters, absences) as researched
    PRIOR_GAMES.csv   the prior games the research opened, with their sources
    OUTCOME.csv       the verified final (settlement)
    GRADES.csv        one grade per contract (settlement)

Rules: sporting fields only (no odds, prices or tips); a pregame value must have been public before the scheduled
start; a missing value stays MISSING with its reason and is never filled with a league average. Fitted-model output is
not written here (ML-SEP-v1): it lives in the shadow ledger. The log records research already done; it never changes a
card, a probability or a grade.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
from datetime import datetime, timezone
from pathlib import Path

from ml import picks as P

ROOT = Path(__file__).resolve().parents[1]
LOG = "research/learning_log"
DICTIONARY = LOG + "/FEATURE_DICTIONARY.csv"
RULE = "LEARNLOG-v1"

CARD = ("local_key", "canonical_id", "mini", "sport", "competition", "season", "native_event_id", "home", "away", "venue",
        "scheduled_start", "issued_at", "timing", "tier", "reference_id", "reference_status", "abstain", "card_block_sha256",
        "logged_at")
CONTRACTS = ("label", "family", "quantity", "side", "line", "line_source", "reference_p", "baseline_p", "final_p", "most_likely_rank")
FEATURES = ("side", "feature", "value", "unit", "window", "status", "missing_reason", "source_url", "published_at", "retrieved_at",
            "known_at")
AVAILABILITY = ("side", "team", "player", "role", "status", "confirmation", "source_url", "published_at", "retrieved_at", "known_at")
PRIOR_GAMES = ("side", "event_at", "competition", "opponent", "venue_role", "score_for", "score_against", "decision", "endpoint",
               "source_url", "retrieved_at", "known_at")
OUTCOME = ("status", "home_score", "away_score", "home_regulation", "away_regulation", "decision", "final_at", "source_url",
           "second_source_url", "retrieved_at", "evidence_grade")
GRADES = ("label", "grade", "basis")
FILES = {"CARD.csv": CARD, "CONTRACTS.csv": CONTRACTS, "FEATURES.csv": FEATURES, "AVAILABILITY.csv": AVAILABILITY,
         "PRIOR_GAMES.csv": PRIOR_GAMES}
SETTLED_FILES = {"OUTCOME.csv": OUTCOME, "GRADES.csv": GRADES}

SIDES = ("HOME", "AWAY")
FEATURE_STATUS = ("OBSERVED", "DERIVED", "MISSING")
ROLES = ("STARTER", "BENCH", "NOT_IN_SQUAD", "UNKNOWN")
AVAIL_STATUS = ("CONFIRMED_ACTIVE", "CONFIRMED_OUT", "DOUBTFUL", "QUESTIONABLE", "PROBABLE", "PROJECTED", "UNKNOWN")
CONFIRMATION = ("OFFICIAL_CONFIRMED", "REPORTED", "PROJECTED")
VENUE_ROLES = ("HOME", "AWAY", "NEUTRAL")
DECISIONS = ("WIN", "LOSS", "DRAW", "NO_RESULT")
OUTCOME_STATUS = ("FINAL", "ABANDONED", "POSTPONED", "CANCELLED", "FORFEIT", "AWARDED")
GRADE_VOCAB = ("WIN", "LOSS", "PUSH", "VOID", "UNRESOLVED", "UNATTAINABLE")
PLACEHOLDER = "NOT_YET_RESEARCHED"
MARKET = re.compile(r"\b(odds|bookmaker|sportsbook|betting|wager|tipster|implied probability|price)\b", re.I)
KEY = re.compile(r"LOCAL-[A-Z0-9]+-G[0-9]{4,}")


class LearningLogError(ValueError):
    pass


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _read(path: Path) -> tuple[tuple, list[dict]]:
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        return tuple(reader.fieldnames or ()), [dict(r) for r in reader]


def _write(path: Path, fields, rows) -> None:
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=list(fields), lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    path.write_bytes(buf.getvalue().encode("utf-8"))


def _time(value: str):
    try:
        t = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    return t if t.tzinfo is not None else None


def dictionary(root=ROOT) -> list[dict]:
    return _read(Path(root) / DICTIONARY)[1]


def required_features(sport: str, root=ROOT) -> list[dict]:
    """The sport's required features; a sport without its own rows uses the TEAM_SPORT rows."""
    rows = dictionary(root)
    own = [r for r in rows if r["sport"] == sport]
    return [r for r in (own or [r for r in rows if r["sport"] == "TEAM_SPORT"]) if r["required"] == "Y"]


def folder(key: str, root=ROOT) -> Path:
    if not KEY.fullmatch(key):
        raise LearningLogError(f"{key!r} is not a local key (LOCAL-<MINI_KEY>-G0001)")
    return Path(root) / LOG / key


# ------------------------------------------------------------------ init (prompt 1, after the card is written)
def init(mini, key: str, game, *, sport: str, root=ROOT) -> Path:
    root = Path(root)
    out = folder(key, root)
    if out.exists():
        raise LearningLogError(f"{out} already exists; the log is appended to, never re-initialised")
    text = Path(mini).read_text(encoding="utf-8")
    picks_block = P.block(text, key)
    meta, rows = P.parse(picks_block)
    _, g = _read(Path(game))
    if len(g) != 1:
        raise LearningLogError("GAME.csv must hold exactly one event")
    g = g[0]
    if g.get("local_key", "").strip() != key:
        raise LearningLogError(f"GAME.csv is for {g.get('local_key')!r}, not {key}")
    if g.get("competition", "").strip() != meta["competition"]:
        raise LearningLogError("GAME.csv and the PICKS_V2 header name different competitions")
    if not required_features(sport, root):
        raise LearningLogError(f"no feature rows for sport {sport!r} in {DICTIONARY}")
    out.mkdir(parents=True)
    mini_path = Path(mini).resolve()
    rel = mini_path.relative_to(root.resolve()).as_posix() if mini_path.is_relative_to(root.resolve()) else str(mini)
    _write(out / "CARD.csv", CARD, [dict(
        local_key=key, canonical_id="", mini=rel, sport=sport, competition=meta["competition"], season=g.get("season", ""),
        native_event_id=g.get("native_event_id", ""), home=g.get("home", ""), away=g.get("away", ""), venue=g.get("venue", ""),
        scheduled_start=meta["scheduled_start"], issued_at=meta.get("issued_at", ""), timing=meta["timing"], tier=meta["tier"],
        reference_id=meta["reference_id"], reference_status=meta["reference_status"], abstain=meta["abstain"],
        card_block_sha256=hashlib.sha256(picks_block.encode("utf-8")).hexdigest(), logged_at=_now())])
    _write(out / "CONTRACTS.csv", CONTRACTS, [{k: r[k] for k in CONTRACTS} for r in rows])
    _write(out / "FEATURES.csv", FEATURES, [dict(side=side, feature=f["feature"], value="", unit=f["unit"], window=f["window"],
                                                 status="MISSING", missing_reason=PLACEHOLDER, source_url="", published_at="",
                                                 retrieved_at="", known_at="")
                                            for side in SIDES for f in required_features(sport, root)])
    _write(out / "AVAILABILITY.csv", AVAILABILITY, [])
    _write(out / "PRIOR_GAMES.csv", PRIOR_GAMES, [])
    return out


# ------------------------------------------------------------------ check
def _market(rows: list[dict], fields, name: str, problems: list[str]) -> None:
    for i, r in enumerate(rows, 2):
        for f in fields:
            if f.endswith("_url"):
                continue
            if MARKET.search(r.get(f) or ""):
                problems.append(f"{name} line {i}: {f} mentions a market term; the learning log holds sporting fields only")


def check(key: str, stage: str = "pregame", root=ROOT) -> list[str]:
    root = Path(root)
    out = folder(key, root)
    if stage not in ("pregame", "settled"):
        raise LearningLogError("stage must be pregame or settled")
    if not out.is_dir():
        return [f"{out}: no learning log; run `python -m ml learning-log init`"]
    problems: list[str] = []
    data = {}
    for name, fields in {**FILES, **(SETTLED_FILES if stage == "settled" else {})}.items():
        path = out / name
        if not path.exists():
            problems.append(f"{name}: missing")
            continue
        head, rows = _read(path)
        if head != tuple(fields):
            problems.append(f"{name}: columns must be exactly {','.join(fields)}")
            continue
        data[name] = rows
    if problems:
        return problems
    card = data["CARD.csv"]
    if len(card) != 1:
        return ["CARD.csv: exactly one row"]
    card = card[0]
    start = _time(card["scheduled_start"])
    if start is None:
        problems.append("CARD.csv: scheduled_start needs an ISO time with an offset")
    if card["local_key"] != key:
        problems.append("CARD.csv: local_key differs from the folder")
    if card["canonical_id"] and not re.fullmatch(r"P-\d{3,}", card["canonical_id"]):
        problems.append("CARD.csv: canonical_id must be blank or P-NNN")
    labels = [r["label"] for r in data["CONTRACTS.csv"]]
    if not labels or len(set(labels)) != len(labels):
        problems.append("CONTRACTS.csv: at least one contract, labels unique")
    for r in data["CONTRACTS.csv"]:
        try:
            p = float(r["final_p"])
            if not 0 <= p <= 1:
                raise ValueError
        except ValueError:
            problems.append(f"CONTRACTS.csv {r['label']}: final_p must be a probability")

    def pregame_time(name, i, r, field="known_at", required=True):
        t = _time(r.get(field) or "")
        if t is None:
            if required:
                problems.append(f"{name} line {i}: {field} needs an ISO time with an offset")
            return
        if start is not None and t >= start and card["timing"] == "PREGAME":
            problems.append(f"{name} line {i}: {field} {r[field]} is not before the scheduled start; a post-start fact is not a pregame feature")

    required = {(s, f["feature"]) for s in SIDES for f in required_features(card["sport"], root)}
    seen = set()
    for i, r in enumerate(data["FEATURES.csv"], 2):
        if r["side"] not in SIDES or r["status"] not in FEATURE_STATUS:
            problems.append(f"FEATURES.csv line {i}: side must be HOME/AWAY and status OBSERVED/DERIVED/MISSING")
            continue
        if (r["side"], r["feature"]) in seen:
            problems.append(f"FEATURES.csv line {i}: {r['side']} {r['feature']} appears twice")
        seen.add((r["side"], r["feature"]))
        if r["status"] == "MISSING":
            if r["value"]:
                problems.append(f"FEATURES.csv line {i}: a MISSING feature has no value (never a league-average fill)")
            if not r["missing_reason"] or r["missing_reason"] == PLACEHOLDER:
                problems.append(f"FEATURES.csv line {i}: {r['side']} {r['feature']} is still {PLACEHOLDER}: research it or give the reason it is missing")
            continue
        try:
            float(r["value"])
        except ValueError:
            problems.append(f"FEATURES.csv line {i}: value must be a number")
        if not r["source_url"].startswith("https://") and r["status"] == "OBSERVED":
            problems.append(f"FEATURES.csv line {i}: an OBSERVED feature needs its https source_url")
        pregame_time("FEATURES.csv", i, r)
        if _time(r["retrieved_at"]) is None:
            problems.append(f"FEATURES.csv line {i}: retrieved_at needs an ISO time with an offset")
    for side, feature in sorted(required - seen):
        problems.append(f"FEATURES.csv: required feature {side} {feature} is absent (write it, or MISSING with the reason)")
    for i, r in enumerate(data["AVAILABILITY.csv"], 2):
        if r["side"] not in SIDES or r["role"] not in ROLES or r["status"] not in AVAIL_STATUS or r["confirmation"] not in CONFIRMATION:
            problems.append(f"AVAILABILITY.csv line {i}: side/role/status/confirmation outside the vocabulary")
        if not r["source_url"].startswith("https://"):
            problems.append(f"AVAILABILITY.csv line {i}: needs an https source_url")
        pregame_time("AVAILABILITY.csv", i, r)
    for i, r in enumerate(data["PRIOR_GAMES.csv"], 2):
        if r["side"] not in SIDES or r["venue_role"] not in VENUE_ROLES or r["decision"] not in DECISIONS:
            problems.append(f"PRIOR_GAMES.csv line {i}: side/venue_role/decision outside the vocabulary")
        try:
            float(r["score_for"]), float(r["score_against"])
        except ValueError:
            problems.append(f"PRIOR_GAMES.csv line {i}: score_for and score_against must be numbers")
        if not r["source_url"].startswith("https://"):
            problems.append(f"PRIOR_GAMES.csv line {i}: needs an https source_url")
        pregame_time("PRIOR_GAMES.csv", i, r, "event_at")
        pregame_time("PRIOR_GAMES.csv", i, r)
    _market(data["FEATURES.csv"], FEATURES, "FEATURES.csv", problems)
    _market(data["AVAILABILITY.csv"], AVAILABILITY, "AVAILABILITY.csv", problems)
    _market(data["PRIOR_GAMES.csv"], PRIOR_GAMES, "PRIOR_GAMES.csv", problems)
    if stage == "settled":
        outcome = data["OUTCOME.csv"]
        if len(outcome) != 1:
            problems.append("OUTCOME.csv: exactly one row")
        else:
            o = outcome[0]
            if o["status"] not in OUTCOME_STATUS:
                problems.append("OUTCOME.csv: status outside the vocabulary")
            if o["status"] == "FINAL":
                for f in ("home_score", "away_score"):
                    try:
                        float(o[f])
                    except ValueError:
                        problems.append(f"OUTCOME.csv: {f} must be a number for a FINAL")
            if not o["source_url"].startswith("https://"):
                problems.append("OUTCOME.csv: needs an https source_url")
            if _time(o["retrieved_at"]) is None:
                problems.append("OUTCOME.csv: retrieved_at needs an ISO time with an offset")
        graded = {r["label"]: r for r in data["GRADES.csv"]}
        for r in data["GRADES.csv"]:
            if r["grade"] not in GRADE_VOCAB:
                problems.append(f"GRADES.csv {r['label']}: grade outside {'/'.join(GRADE_VOCAB)}")
        for label in labels:
            if label not in graded:
                problems.append(f"GRADES.csv: contract {label} has no grade")
        for label in graded:
            if label not in labels:
                problems.append(f"GRADES.csv: {label} is not a contract of this card")
    return problems


# ------------------------------------------------------------------ link (prompt 4)
def link(key: str, canonical: str, root=ROOT) -> None:
    if not re.fullmatch(r"P-\d{3,}", canonical):
        raise LearningLogError("canonical must be P-NNN")
    path = folder(key, root) / "CARD.csv"
    head, rows = _read(path)
    if rows[0]["canonical_id"] not in ("", canonical):
        raise LearningLogError(f"{key} is already linked to {rows[0]['canonical_id']}")
    rows[0]["canonical_id"] = canonical
    _write(path, head, rows)


# ------------------------------------------------------------------ build (prompt 6)
def build(out, root=ROOT) -> dict:
    root, out = Path(root), Path(out)
    out.mkdir(parents=True, exist_ok=False)
    base = root / LOG
    contracts, features, availability, prior, receipt = [], [], [], [], []
    for path in sorted(p for p in base.iterdir() if p.is_dir() and KEY.fullmatch(p.name)) if base.is_dir() else []:
        key = path.name
        settled = (path / "OUTCOME.csv").exists()
        problems = check(key, "settled" if settled else "pregame", root)
        receipt.append(dict(local_key=key, stage="settled" if settled else "pregame", admitted="NO" if problems else "YES",
                            problems=" | ".join(problems)[:2000]))
        if problems:
            continue
        card = _read(path / "CARD.csv")[1][0]
        feats = _read(path / "FEATURES.csv")[1]
        wide = {}
        for f in feats:
            col = f"{f['side'].lower()}__{f['feature']}"
            wide[col] = f["value"] if f["status"] != "MISSING" else ""
            wide[col + "__missing"] = "1" if f["status"] == "MISSING" else "0"
        outcome = _read(path / "OUTCOME.csv")[1][0] if settled else {}
        grades = {r["label"]: r["grade"] for r in _read(path / "GRADES.csv")[1]} if settled else {}
        for c in _read(path / "CONTRACTS.csv")[1]:
            contracts.append({**{k: card[k] for k in ("local_key", "canonical_id", "sport", "competition", "season", "native_event_id",
                                                      "home", "away", "scheduled_start", "timing", "tier", "reference_id")},
                              **c, "grade": grades.get(c["label"], ""), "outcome_status": outcome.get("status", ""),
                              "home_score": outcome.get("home_score", ""), "away_score": outcome.get("away_score", ""), **wide})
        features += [dict(local_key=key, **f) for f in feats]
        availability += [dict(local_key=key, **r) for r in _read(path / "AVAILABILITY.csv")[1]]
        prior += [dict(local_key=key, **r) for r in _read(path / "PRIOR_GAMES.csv")[1]]
    cols = []
    for r in contracts:
        cols += [k for k in r if k not in cols]
    for name, fields, rows in (("DATASET_CONTRACTS.csv", cols, contracts), ("DATASET_FEATURES.csv", ("local_key",) + FEATURES, features),
                               ("DATASET_AVAILABILITY.csv", ("local_key",) + AVAILABILITY, availability),
                               ("DATASET_PRIOR_GAMES.csv", ("local_key",) + PRIOR_GAMES, prior)):
        _write(out / name, fields or ("local_key",), rows)
    _write(out / "BUILD_RECEIPT.csv", ("local_key", "stage", "admitted", "problems"), receipt)
    return dict(games=len(receipt), admitted=sum(r["admitted"] == "YES" for r in receipt),
                settled=sum(r["admitted"] == "YES" and r["stage"] == "settled" for r in receipt), contracts=len(contracts))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("init")
    a.add_argument("--mini", required=True, type=Path)
    a.add_argument("--key", required=True)
    a.add_argument("--game", required=True, type=Path)
    a.add_argument("--sport", required=True, help="sport as in FEATURE_DICTIONARY.csv, e.g. Basketball")
    c = sub.add_parser("check")
    c.add_argument("--key", required=True)
    c.add_argument("--stage", choices=("pregame", "settled"), default="pregame")
    lk = sub.add_parser("link")
    lk.add_argument("--key", required=True)
    lk.add_argument("--canonical", required=True)
    b = sub.add_parser("build")
    b.add_argument("--out", required=True, type=Path)
    args = parser.parse_args(argv)
    if args.cmd == "init":
        print(f"{RULE} learning log written: {init(args.mini, args.key, args.game, sport=args.sport)}")
    elif args.cmd == "check":
        problems = check(args.key, args.stage)
        for p in problems:
            print("PROBLEM", p)
        print(f"{RULE} {args.stage} check {'PASSED' if not problems else 'FAILED'}: {args.key}")
        if problems:
            raise SystemExit(1)
    elif args.cmd == "link":
        link(args.key, args.canonical)
        print(f"{args.key} linked to {args.canonical}")
    else:
        print(build(args.out))


if __name__ == "__main__":
    main()
