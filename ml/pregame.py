"""Pregame model shadow, run in the repository after the analyst card is written (MLSCOPE-v2 / ENV-v2).

Prompt 1 now runs here. The card's p_card is the analyst's own (ANALYST_PRIMARY_V1); the model never feeds
it. Once the card is in the active mini, this command runs the competition's frozen cycle release on the
card's full-game contracts, freezes the model and league-baseline rows, and freezes the card's own p_card
for the same contracts beside them, so model, baseline and card can be compared on identical rows:

    python -m ml pregame run --mini research/active_minis/<MINI_KEY>.md --game GAME.csv --lines LINES.csv \
        --capture SOURCE.txt --confirm-no-outcome-seen
    python -m ml pregame status
    python -m ml pregame compare-card --release research/cycle_releases/<RELEASE>.csv --out OUT

GAME.csv uses the ml.chat columns. LINES.csv uses ``label,family,side,line`` plus optional ``card_p`` (the
card's printed p_card for that row) and ``card_rank``. Every card_p must appear verbatim in the card block.

A competition without an active release, a release frozen for other code, or an input the cycle refuses is
recorded as an honest NOT_RUN disposition: the card stands and nothing is invented. Every run writes a
receipt under research/pregame/<local key>/. Commit and push before the scheduled start to make the
freeze externally checkable.

``status`` reports each release's progress. A progress review is due when either 8 settled weeks or
50 settled paired events are reached; a model decision (prompt 6 / prompt 8) needs both, which the frozen
release and ``cycle evaluate`` already enforce.
"""
from __future__ import annotations

import argparse
import csv
import io
from pathlib import Path
import re
import shutil
import tempfile

from ml import chat

ROOT = chat.ROOT
RECEIPTS = "research/pregame"
CARD_MODEL = "ANALYST_PRIMARY_V1"
CARD_VERSION = "CARD"
RECEIPT_FIELDS = ("local_key", "status", "reason", "competition", "release", "mini_path", "mini_sha256",
                  "card_block_sha256", "scheduled_start", "run_at", "timing_at_generation", "attempt_path",
                  "ledger_model_rows", "ledger_card_rows")
REVIEW_WEEKS, REVIEW_EVENTS = 8, 50


class PregameError(ValueError):
    pass


def _rows(path) -> list[dict]:
    return chat._rows(path)


def card_block(mini: Path, local_key: str) -> str:
    """The card's exact text between its markers; the card must be written before the model runs."""
    text = Path(mini).read_text(encoding="utf-8")
    begin, end = f"<!-- BEGIN CARD {local_key} -->", f"<!-- END CARD {local_key} -->"
    if text.count(begin) != 1 or text.count(end) != 1 or text.index(begin) > text.index(end):
        raise PregameError(f"{mini} must hold exactly one complete card {local_key} before the model runs "
                           "(write and read back the card first; the model never feeds the card)")
    return text[text.index(begin): text.index(end) + len(end)]


def split_lines(path) -> tuple[list[dict], dict]:
    """LINES.csv for the cycle, plus {label: (card_p, card_rank)} for the card rows."""
    rows = _rows(path)
    if not rows:
        raise PregameError("LINES.csv needs at least one contract")
    extra = set(rows[0]) - set(chat.LINE_FIELDS)
    if not set(chat.LINE_FIELDS) <= set(rows[0]) or extra - {"card_p", "card_rank"}:
        raise PregameError("LINES.csv columns: " + ",".join(chat.LINE_FIELDS) + "[,card_p][,card_rank]")
    card = {}
    for row in rows:
        value = (row.get("card_p") or "").strip()
        if value:
            p = float(value)
            if not 0 <= p <= 1:
                raise PregameError(f"{row['label']}: card_p must be a probability")
            card[row["label"].strip()] = (value, (row.get("card_rank") or "").strip())
    return [{k: row[k] for k in chat.LINE_FIELDS} for row in rows], card


def _write_receipt(root: Path, rec: dict) -> Path:
    stamp = chat._now().strftime("%Y%m%dT%H%M%S%fZ")
    path = root / RECEIPTS / rec["local_key"] / f"{stamp}_PREGAME.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(chat._csv([rec], RECEIPT_FIELDS))
    return path


def card_rows(attempt: Path, card: dict, issued_at: str) -> list[dict]:
    """Ledger rows for the card's own p_card on exactly the contracts the bundle priced."""
    from ml import cycle, primary as p
    from ml.evaluation import prospective as ps
    rec = cycle.verify_bundle(attempt / "BUNDLE")
    status = ps._status(issued_at, rec["scheduled_start"], p.clock(issued_at))
    base = ps._common(CARD_MODEL, CARD_VERSION, "CHAMPION", rec["event_id"], rec["competition"], rec["endpoint"],
                      issued_at, rec["scheduled_start"], "CARD_FROZEN_IN_MINI", CARD_MODEL, "NOT_APPLICABLE_ANALYST", status)
    out = []
    for row in p.read_rows(attempt / "BUNDLE" / "PREDICTIONS.csv"):
        if row["contract_key"] not in card:
            continue
        key = p.digest(p.csv_bytes([{k: row[k] for k in ("family", "side", "line", "endpoint", "definition", "action")}]))[:24]
        value, rank = card[row["contract_key"]]
        out.append(dict(forecast_id=rec["event_id"] + ":" + CARD_MODEL, contract_key=key, family=row["family"],
                        side=row["side"], line=row["line"], p=value, rank=rank, **base))
    missing = set(card) - {r["contract_key"] for r in p.read_rows(attempt / "BUNDLE" / "PREDICTIONS.csv")}
    if missing:
        raise PregameError("card rows the bundle did not price: " + ", ".join(sorted(missing)))
    return out


def run(mini, game, lines, capture, *, confirmed=False, root=ROOT, ledger=chat.LEDGER) -> dict:
    root = Path(root).resolve()
    if not confirmed:
        raise PregameError("pass --confirm-no-outcome-seen only if no live score, result or post-start report was opened")
    g = chat._one(_rows(game), chat.GAME_FIELDS, "GAME.csv")
    key = g["local_key"]
    if not chat.LOCAL_KEY.fullmatch(key):
        raise PregameError("local_key must be the card's stable key, e.g. LOCAL-<MINI_KEY>-G0001")
    block = card_block(mini, key)
    cycle_lines, card = split_lines(lines)
    for label, (value, _) in card.items():
        if not re.search(r"(?<![\d.])" + re.escape(value) + r"(?![\d])", block):
            raise PregameError(f"{label}: card_p {value} is not printed in card {key}; copy the card's own value")
    mini_path = Path(mini).resolve()
    rec = dict(local_key=key, status="", reason="", competition=g["competition"], release="",
               mini_path=mini_path.relative_to(root).as_posix() if mini_path.is_relative_to(root) else str(mini_path),
               mini_sha256=chat._sha(mini_path.read_bytes()), card_block_sha256=chat._sha(block.encode("utf-8")),
               scheduled_start=g["scheduled_start"], run_at=chat._now().isoformat(), timing_at_generation="",
               attempt_path="", ledger_model_rows="0", ledger_card_rows="0")
    current = [r for r in _rows(root / chat.CURRENT) if r["competition"] == g["competition"]]
    if not current:
        supported = ", ".join(sorted(r["competition"] for r in _rows(root / chat.CURRENT))) or "none"
        rec.update(status="NOT_RUN_NO_RELEASE", reason=f"no active release for this competition; active: {supported}")
        return dict(rec, receipt=str(_write_receipt(root, rec)), results=[])
    release = current[0]
    rec["release"] = release["active_experimental_release"]
    from ml import cycle
    frozen = _rows(root / release["release_path"])[0]["code_sha256"]
    if frozen != cycle.code_hash():
        rec.update(status="NOT_RUN_STALE_RELEASE",
                   reason="the release was frozen for other forecast code; prompt 8 must freeze a new release version")
        return dict(rec, receipt=str(_write_receipt(root, rec)), results=[])
    staging = Path(tempfile.mkdtemp(prefix="sr_pregame_"))
    try:
        lines_csv = staging / "LINES.csv"
        lines_csv.write_bytes(chat._csv(cycle_lines, chat.LINE_FIELDS))
        try:
            result = chat.run(game, lines_csv, capture, staging / "OUT", confirmed=True, root=root)
        except chat.ChatError as exc:
            rec.update(status="NOT_RUN_INPUT_REFUSED", reason=str(exc))
            return dict(rec, receipt=str(_write_receipt(root, rec)), results=[])
        accepted = chat.accept(result["upload"], key, freeze_basis="now", ledger=ledger, root=root)
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    attempt = root / accepted["attempt_path"]
    rec.update(status=accepted["status"], attempt_path=accepted["attempt_path"], ledger_model_rows=accepted["ledger_rows"],
               timing_at_generation=(result["results"][0]["timing_at_generation"] if result["results"] else ""))
    if accepted["status"] == "EXECUTED" and card:
        from ml.evaluation import prospective
        rows = card_rows(attempt, card, accepted["freeze_clock"])
        prospective.freeze(root / ledger, rows, now=accepted["freeze_clock"])
        rec["ledger_card_rows"] = str(len(rows))
    elif accepted["status"] != "EXECUTED":
        rec["reason"] = next((r["error"] for r in result["results"] if r["error"]), "attempt failed")
    return dict(rec, receipt=str(_write_receipt(root, rec)), results=result["results"])


def markdown(result: dict) -> str:
    """The card's Model shadow block (recorded after the decision block; it changes no rank)."""
    head = (f"**Model shadow (MLSCOPE-v2, frozen after this card):** `{result['status']}`"
            + (f" · release `{result['release']}`" if result["release"] else "")
            + (f" · {result['timing_at_generation']}" if result["timing_at_generation"] else "")
            + (f" · receipt `{Path(result['receipt']).relative_to(ROOT).as_posix()}`"
               if Path(result["receipt"]).is_relative_to(ROOT) else ""))
    if result["reason"]:
        head += f"\n\nReason: {result['reason']}"
    if not any(r.get("label") for r in result["results"]):
        return head + "\n"
    lines = ["| Contract | Model p | League baseline p | Model rank |", "|---|---:|---:|---:|"]
    for r in result["results"]:
        lines.append(f"| {r['label']} | {r['p_card']} | {r['baseline_p']} | {r['model_rank']} |")
    return head + "\n\n" + "\n".join(lines) + "\n\nThe card's p_card and ranks above are unchanged by this block.\n"


# ------------------------------------------------------------------ progress and card comparison
def _settlements(root: Path) -> list[dict]:
    out = []
    for path in sorted((root / chat.FEEDBACK).glob("*/SETTLEMENT.csv")) if (root / chat.FEEDBACK).is_dir() else []:
        out.extend(_rows(path))
    return out


def lane_state(events: int, weeks: int, minimum_events: int, minimum_weeks: int) -> str:
    """A progress review is due at 8 weeks or 50 events, whichever comes first; a decision needs both floors."""
    if events >= minimum_events and weeks >= minimum_weeks:
        return "DECISION_FLOOR_MET"
    if events >= REVIEW_EVENTS or weeks >= REVIEW_WEEKS:
        return "PROGRESS_REVIEW_DUE"
    return "ACCUMULATING"


def status(root=ROOT, ledger=chat.LEDGER) -> list[dict]:
    from ml import primary as p
    from ml.core.metrics import iso_week
    import pandas as pd
    from ml.evaluation import prospective as ps
    root = Path(root)
    rows = ps.verify_ledger(root / ledger)
    settled = {}
    for s in _settlements(root):
        settled.setdefault(s["release_sha256"], set()).add(s["event_id"])
    out = []
    for release in _rows(root / chat.CURRENT):
        config = _rows(root / release["release_path"])[0]
        sha = p.digest(p.csv_bytes([config]))
        model = [r for r in rows if r["model_version"] == config["version"] and r["role"] == "CANDIDATE"]
        clean = [r for r in model if r["evidence_status"] == "PRE_START_VERIFIED"]
        events = {r["event_id"]: r["scheduled_start"] for r in clean}
        done = {e: t for e, t in events.items() if e in settled.get(sha, set())}
        weeks = set(iso_week(pd.Series([p.clock(t).tz_localize(None) for t in done.values()]))) if done else set()
        card_events = {r["event_id"] for r in rows if r["model_id"] == CARD_MODEL and r["competition"] == config["competition"]
                       and r["evidence_status"] == "PRE_START_VERIFIED"}
        min_w, min_e = int(config["minimum_weeks"]), int(config["minimum_events"])
        n_e, n_w = len(done), len(weeks)
        state = lane_state(n_e, n_w, min_e, min_w)
        out.append(dict(competition=config["competition"], release=config["version"],
                        frozen_events=len({r["event_id"] for r in model}), pre_start_events=len(events),
                        settled_events=n_e, settled_weeks=n_w, card_paired_settled=len(card_events & set(done)),
                        minimum_events=min_e, minimum_weeks=min_w, state=state))
    return out


def compare_card(release_path, out, root=ROOT, ledger=chat.LEDGER) -> dict:
    """Prospective card-versus-model paired evaluation on identical frozen contracts (prompt 6)."""
    from ml import cycle, primary as p
    from ml.core.distributions import ScoreGrid
    from ml.evaluation import prospective as ps
    import numpy as np
    import pandas as pd
    root = Path(root)
    config = cycle.release(release_path, check_code=False)
    rows = [r for r in ps.verify_ledger(root / ledger) if r["competition"] == config["competition"]
            and r["endpoint"] == config["endpoint"]
            and ((r["model_id"] == cycle.POLICY and r["model_version"] == config["version"]) or r["model_id"] == CARD_MODEL)]
    frozen = p.digest(p.csv_bytes([config]))
    effective = {}
    for path in sorted((root / chat.FEEDBACK).glob("*/SETTLEMENT.csv")):
        row = cycle.verify_settlement(path.parent)
        if row["release_sha256"] != frozen:
            continue
        old = effective.get(row["event_id"])
        if old is None or int(row["result_revision"]) > int(old["result_revision"]):
            effective[row["event_id"]] = row
    outcomes = []
    for event, row in effective.items():
        final = ScoreGrid(np.ones((1, 1)), int(row["home_score"]), int(row["away_score"]))
        for contract in p.read_rows(Path(row["bundle"]) / "CONTRACTS.csv"):
            w, pu, _ = p.price(final, contract, row["endpoint"])
            key = p.digest(p.csv_bytes([{k: contract[k] for k in ("family", "side", "line", "endpoint", "definition", "action")}]))[:24]
            outcomes.append(dict(event_id=event, contract_key=key, result="PUSH" if pu else "WIN" if w else "LOSS",
                                 final_at=row["final_at"], available_at=row["available_at"], evidence_sha256=row["evidence_sha256"]))
    result = ps.evaluate(rows, pd.DataFrame(outcomes, columns=ps.OUTCOME_FIELDS), f"{CARD_MODEL}:{CARD_VERSION}",
                         f"{cycle.POLICY}:{config['version']}", delta=float(config["minimum_brier_effect"]))
    events = result.get("interval", {}).get("n_events", 0)
    if events < int(config["minimum_events"]):
        result.update(disposition="INSUFFICIENT_EVIDENCE", reason=f"{events} paired card events; frozen minimum {config['minimum_events']}")
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    summary = dict(release=config["version"], champion=f"{CARD_MODEL}:{CARD_VERSION}", candidate=f"{cycle.POLICY}:{config['version']}",
                   disposition=result["disposition"], reason=result["reason"], pairs=result.get("pairs", len(result.get("models", {}))),
                   events=events, k_weeks=result.get("interval", {}).get("k_weeks", 0),
                   mean_d_brier=result.get("interval", {}).get("mean", ""))
    (out / "CARD_COMPARISON.csv").write_bytes(chat._csv([summary], summary))
    return summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    rn = sub.add_parser("run", help="after the card is written: freeze the model, baseline and card rows")
    for name in ("mini", "game", "lines", "capture"):
        rn.add_argument("--" + name, type=Path, required=True)
    rn.add_argument("--confirm-no-outcome-seen", action="store_true")
    sub.add_parser("status", help="lane progress against the 8-week / 50-game floor")
    cc = sub.add_parser("compare-card", help="paired card-versus-model evaluation for one release")
    cc.add_argument("--release", type=Path, required=True)
    cc.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "run":
            if Path.cwd().resolve() != ROOT:
                raise PregameError("run from the repository root")
            result = run(args.mini, args.game, args.lines, args.capture, confirmed=args.confirm_no_outcome_seen)
            print(markdown(result))
        elif args.command == "status":
            rows = status()
            if not rows:
                print("no active releases")
            for r in rows:
                print(" ".join(f"{k}={v}" for k, v in r.items()))
        else:
            for k, v in compare_card(args.release, args.out).items():
                print(f"{k}: {v}")
    except (PregameError, chat.ChatError) as exc:
        print(f"REFUSED: {exc}")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
