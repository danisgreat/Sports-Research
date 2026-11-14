"""Adjustment ledger and its settlement-time scoring (LEDGER-v2 / BENCH-v1 / WIDTH-v1).

The ledger is an append-only CSV with one row per priced contract per card, copied from the card's PICKS_V2 block after it
lints clean. At settlement the same rows are scored against four references on identical rows: the frozen reference
(model or TB-1-MD), the league baseline, the line-implied 0.5 at supplied two-way lines, and any hand-entered benchmark
(no-vig close, external model). The paired Brier difference "final minus reference" is the measured value of the analyst's
adjustments; it is the test of whether research adds accuracy.

    python -m ml ledger add      --mini research/active_minis/<MINI_KEY>.md --key LOCAL-<MINI_KEY>-G0001
    python -m ml ledger verify
    python -m ml ledger score    --results RESULTS.csv [--benchmarks BENCHMARKS.csv] --out NEW_FOLDER
    python -m ml ledger coverage --actuals ACTUALS.csv --out NEW_FOLDER

RESULTS.csv: ``local_key,label,grade`` (WIN, LOSS, PUSH, VOID or UNRESOLVED). ACTUALS.csv: ``local_key,quantity,actual``
(home - away for MARGIN, home + away for TOTAL). Only WIN and LOSS rows are scored. No outcome is invented.

LEDGER-v2 (CR-2026.11.08-R2):

- **Timing is derived, not claimed.** A card that says PREGAME is ledgered PREGAME only with verified evidence: a pregame
  receipt for the same key whose card-block hash matches and whose run time is before the start, or the card header's
  ``issue_evidence: COMMIT:<sha>`` naming a commit that already holds this exact card block and was made before the start.
  Otherwise its rows are ledgered TIMING_UNVERIFIED, and the claim is kept in ``timing_claimed``.
- **TIMING-v3 (CR-2026.11.15-R1).** A card that says PRE_START_RESEARCH is ledgered so only when its header declares when
  research began, a not-started observation (URL and time) at or after that moment, and outcome_exposure NONE_RECORDED, all
  consistent with the issue time. Its evidence string names the observation; the declaration is checked again at
  settlement against the official actual first play. Scoring pools PRE_START_RESEARCH with PREGAME.
- **Adjustments are structured data.** A card's ``ADJUSTMENTS_V1`` block becomes immutable, hash-chained rows in
  ADJUSTMENTS.csv, keyed by card and effect-table row version. Each row holds the fact, its source and times, the applied
  size and the frozen counterfactual p of every affected row without that adjustment. Sizes are checked against
  EFFECT_TABLES.csv at the entry size the row's status allows, and a MEASURED_NULL row cannot be used.
- **Scoring keeps strata apart:** timing, fast or full card, supplied or derived line, and reference executed or baseline
  only. Individual-effect scores (final against each adjustment's counterfactual) are reported apart from the aggregate.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
import re
import subprocess
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

from ml import benchmarks as B, picks
from ml.core import metrics as M

ROOT = Path(__file__).resolve().parents[1]
LEDGER = "research/adjustment_ledger/ADJUSTMENT_LEDGER.csv"
ADJUSTMENTS = "research/adjustment_ledger/ADJUSTMENTS.csv"
EFFECTS = "research/effect_tables/EFFECT_TABLES.csv"
SUPERSEDED = "research/effect_tables/SUPERSEDED.csv"
HEAD = ("local_key", "competition", "tier", "timing", "timing_claimed", "timing_evidence", "scheduled_start", "issued_at",
        "reference_id", "reference_status", "abstain", "fast_card")
FIELDS = HEAD + picks.COLUMNS
ADJ_BEGIN, ADJ_END = "<!-- BEGIN ADJUSTMENTS_V1 {key} -->", "<!-- END ADJUSTMENTS_V1 {key} -->"
ADJ_COLUMNS = ("adjustment_id", "effect_row_id", "fact", "target", "unit", "applied_size", "entry", "source_url", "published_at",
               "retrieved_at", "corroboration", "overlap_check", "centre_before", "centre_after", "counterfactual")
ADJ_FIELDS = ("local_key",) + ADJ_COLUMNS + ("effect_status", "effect_estimate", "effect_version", "added_at", "previous_sha256",
                                             "row_sha256")
ENTRY_BY_STATUS = {"MEASURED_CONFIRMED": ("FULL", 1.0), "MEASURED_NOT_CONFIRMED": ("HALF", 0.5), "LITERATURE_START": ("HALF", 0.5),
                   "NOT_ESTIMATED": ("SCENARIO", None)}
SIZE_TOLERANCE = 1e-6
MIN_LAMBDA_ROWS = 40
COVERAGE_BAND = (0.85, 1.15)
MIN_COVERAGE_CARDS = 40


class LedgerError(ValueError):
    pass


def _csv(rows: list[dict], fields) -> bytes:
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=list(fields), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode("utf-8")


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _time(value: str, name: str) -> datetime:
    try:
        t = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        raise LedgerError(f"{name} {value!r} is not an ISO 8601 time") from None
    if t.tzinfo is None:
        raise LedgerError(f"{name} {value!r} needs a UTC offset")
    return t


def read(path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        return pd.DataFrame(columns=FIELDS)
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise LedgerError("ledger header changed; it is append-only with a fixed schema")
        frame = pd.DataFrame(list(reader), columns=FIELDS)
    if frame.duplicated(["local_key", "label"]).any():
        raise LedgerError("duplicate (local_key, label) rows in the ledger")
    return frame


def _card_text(mini, key: str) -> str:
    text = Path(mini).read_text(encoding="utf-8")
    begin, end = f"<!-- BEGIN CARD {key} -->", f"<!-- END CARD {key} -->"
    if text.count(begin) != 1 or text.count(end) != 1:
        raise LedgerError(f"{mini} must hold exactly one complete card {key}")
    return text[text.index(begin): text.index(end) + len(end)]


def derive_timing(meta: dict, card: str, key: str, mini, root=ROOT) -> tuple[str, str]:
    """(timing, evidence). PREGAME only when a pregame receipt or a commit proves the card existed before the start."""
    claimed = meta["timing"]
    if claimed == "PRE_START_RESEARCH":
        problems = picks.pre_start_research_problems(meta)
        if problems:
            return "TIMING_UNVERIFIED", "CLAIMED_PRE_START_RESEARCH:" + problems[0].removeprefix("header: ")
        return "PRE_START_RESEARCH", (f"DECLARED_RESEARCH_START:{meta['research_started_at']}"
                                      f"|NOT_STARTED:{meta['not_started_source']}@{meta['not_started_observed_at']}")
    if claimed != "PREGAME":
        return claimed, "CLAIM_NOT_PREGAME"
    root = Path(root)
    start, block_sha = _time(meta["scheduled_start"], "scheduled_start"), _sha(card.encode("utf-8"))
    evidence = meta.get("issue_evidence", "")
    if evidence.startswith("COMMIT:"):
        sha = evidence.split(":", 1)[1]
        try:
            rel = Path(mini).resolve().relative_to(root.resolve()).as_posix()
            blob = subprocess.run(["git", "show", f"{sha}:{rel}"], cwd=root, capture_output=True, check=True).stdout.decode("utf-8")
            when = subprocess.run(["git", "show", "-s", "--format=%cI", sha], cwd=root, capture_output=True,
                                  check=True).stdout.decode().strip()
        except (subprocess.CalledProcessError, ValueError, OSError):
            return "TIMING_UNVERIFIED", f"CLAIMED_PREGAME:{evidence}:COMMIT_NOT_READABLE"
        if card in blob and _time(when, "commit time") < start:
            return "PREGAME", evidence
        return "TIMING_UNVERIFIED", f"CLAIMED_PREGAME:{evidence}:CARD_NOT_IN_COMMIT_OR_COMMIT_LATE"
    if evidence.startswith("PREGAME_RECEIPT:"):
        receipts = [root / evidence.split(":", 1)[1]]
    else:
        folder = root / "research" / "pregame" / key
        receipts = sorted(folder.glob("*_PREGAME.csv")) if folder.is_dir() else []
    for path in receipts:
        if not path.is_file():
            continue
        with open(path, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                if r.get("local_key") == key and r.get("status") == "EXECUTED" and r.get("card_block_sha256") == block_sha \
                        and r.get("run_at") and _time(r["run_at"], "receipt run_at") < start:
                    return "PREGAME", "PREGAME_RECEIPT:" + path.relative_to(root).as_posix()
    return "TIMING_UNVERIFIED", "CLAIMED_PREGAME:NO_VERIFIED_RECEIPT_OR_COMMIT"


def effect_rows(root=ROOT) -> dict:
    """EFFECT_TABLES.csv rows by id, each with a version hash of its exact content (the effect version an adjustment used)."""
    with open(Path(root) / EFFECTS, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    return {r["row_id"]: dict(r, version=_sha(_csv([r], list(r)))) for r in rows}


def superseded(root=ROOT) -> dict:
    """row_id -> superseding row_id. EFFECT_TABLES.csv is append-only, so a re-estimate retires its old row here."""
    path = Path(root) / SUPERSEDED
    if not path.exists():
        return {}
    with open(path, newline="", encoding="utf-8") as fh:
        return {r["row_id"]: r["superseded_by"] for r in csv.DictReader(fh)}


def parse_adjustments(card: str, key: str) -> list[dict]:
    begin, end = ADJ_BEGIN.format(key=key), ADJ_END.format(key=key)
    if card.count(begin) == 0 and card.count(end) == 0:
        return []
    if card.count(begin) != 1 or card.count(end) != 1 or card.index(begin) > card.index(end):
        raise LedgerError(f"card must hold at most one complete ADJUSTMENTS_V1 block for {key}")
    body = card[card.index(begin) + len(begin): card.index(end)]
    lines = [ln for ln in body.strip().splitlines() if ln.strip() and not ln.strip().startswith("```")]
    reader = csv.DictReader(io.StringIO("\n".join(lines)))
    if tuple(reader.fieldnames or ()) != ADJ_COLUMNS:
        raise LedgerError("ADJUSTMENTS_V1 columns must be exactly: " + ",".join(ADJ_COLUMNS))
    return [dict(r) for r in reader]


def check_adjustments(adjustments: list[dict], meta: dict, rows: list[dict], root=ROOT) -> list[str]:
    """Every adjustment names a real effect row at the entry size its status allows, with sourced, pre-issue times."""
    problems, labels = [], {r["label"] for r in rows}
    effects = effect_rows(root) if adjustments else {}
    retired = superseded(root) if adjustments else {}
    issued, seen = _time(meta["issued_at"], "issued_at"), set()
    for a in adjustments:
        name = a["adjustment_id"] or "<unnamed>"
        if not re.fullmatch(r"A\d+", a["adjustment_id"]) or a["adjustment_id"] in seen:
            problems.append(f"{name}: adjustment_id must be A<n> and unique")
        seen.add(a["adjustment_id"])
        effect = effects.get(a["effect_row_id"])
        if a["effect_row_id"] in retired:
            problems.append(f"{name}: {a['effect_row_id']} is superseded by {retired[a['effect_row_id']]}; use the current row")
            continue
        if a["effect_row_id"] == "SCENARIO_NO_TABLE":
            status = "NOT_ESTIMATED"
        elif effect is None:
            problems.append(f"{name}: effect row {a['effect_row_id']!r} is not in EFFECT_TABLES.csv")
            continue
        else:
            status = effect["status"]
            if effect["competition"] != meta["competition"] and effect["competition"].strip().lower() != "all":
                problems.append(f"{name}: effect competition {effect['competition']!r} does not match {meta['competition']!r}; use an explicitly scoped effect")
            effect_target = effect["target"].strip().lower()
            compatible = {"MARGIN": ("margin",), "TOTAL": ("total",), "TEAM_TOTAL": ("team rating", "team runs", "team goals"),
                          "PERIOD": ("period",), "COUNT": ("count", "corner")}
            if not any(word in effect_target for word in compatible.get(a["target"], ())):
                problems.append(f"{name}: effect target {effect['target']!r} is incompatible with {a['target']!r}")
            source_unit, applied_unit = effect["unit"].lower(), a["unit"].strip().lower()
            expected_unit = ("proportion" if "proportion" in source_unit else "points" if "point" in source_unit
                             else "goals" if "goal" in source_unit else "runs" if "run" in source_unit
                             else "probability" if "probability" in source_unit else source_unit.strip())
            if applied_unit != expected_unit:
                problems.append(f"{name}: effect unit {expected_unit!r} does not match applied unit {applied_unit!r}")
        if status == "MEASURED_NULL":
            problems.append(f"{name}: {a['effect_row_id']} is MEASURED_NULL; no adjustment may use it")
            continue
        if status not in ENTRY_BY_STATUS:
            problems.append(f"{name}: effect status {status!r} has no entry rule")
            continue
        entry, factor = ENTRY_BY_STATUS[status]
        if a["entry"] != entry:
            problems.append(f"{name}: {status} enters {entry}, not {a['entry']}")
        try:
            size = float(a["applied_size"])
        except ValueError:
            problems.append(f"{name}: applied_size must be a number")
            size = None
        if size is not None and not math.isfinite(size):
            problems.append(f"{name}: applied_size must be finite")
        if size is not None and factor is not None and effect and effect.get("estimate", "") != "":
            want = float(effect["estimate"]) * factor
            if abs(size - want) > SIZE_TOLERANCE:
                problems.append(f"{name}: applied_size {size} is not the table estimate {effect['estimate']} at {entry} ({want:.6g})")
        if not a["source_url"].startswith(("http://", "https://", "research/")):
            problems.append(f"{name}: source_url must be a URL or a repository capture path")
        try:
            published, retrieved = _time(a["published_at"], "published_at"), _time(a["retrieved_at"], "retrieved_at")
            if not published <= retrieved <= issued:
                problems.append(f"{name}: times must satisfy published_at <= retrieved_at <= issued_at")
        except LedgerError as exc:
            problems.append(f"{name}: {exc}")
        if not a["overlap_check"].strip():
            problems.append(f"{name}: overlap_check must name what the reference already contains (or NONE_FOUND)")
        parts = [s for s in a["counterfactual"].split("|") if s.strip()]
        if not parts:
            problems.append(f"{name}: counterfactual must give the frozen p of each affected row without this adjustment")
        for part in parts:
            label, _, value = part.partition("=")
            if label not in labels:
                problems.append(f"{name}: counterfactual names {label!r}, not a PICKS_V2 row")
                continue
            try:
                v = float(value)
            except ValueError:
                v = math.nan
            if not 0 <= v <= 1:
                problems.append(f"{name}: counterfactual p for {label} must be in [0, 1]")
    moved = [r["label"] for r in rows if r["reference_p"].strip() not in ("", "NONE")
             and abs(float(r["final_p"]) - float(r["reference_p"])) > 1e-9]
    if moved and not adjustments:
        problems.append("rows differ from the reference (" + ", ".join(moved) + ") but the card has no ADJUSTMENTS_V1 block")
    covered = {part.partition("=")[0] for a in adjustments for part in a["counterfactual"].split("|")}
    uncovered = set(moved) - covered
    if adjustments and uncovered:
        problems.append("moved rows lack an adjustment counterfactual: " + ", ".join(sorted(uncovered)))
    return problems


def read_adjustments(path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        return pd.DataFrame(columns=ADJ_FIELDS)
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if tuple(reader.fieldnames or ()) != ADJ_FIELDS:
            raise LedgerError("ADJUSTMENTS.csv header changed; it is append-only with a fixed schema")
        frame = pd.DataFrame(list(reader), columns=ADJ_FIELDS)
    previous = ""
    for r in frame.to_dict("records"):
        body = {k: r[k] for k in ADJ_FIELDS if k != "row_sha256"}
        if r["previous_sha256"] != previous or r["row_sha256"] != _sha(_csv([body], list(body))):
            raise LedgerError(f"ADJUSTMENTS.csv chain broken at {r['local_key']} {r['adjustment_id']}: rows are immutable")
        previous = r["row_sha256"]
    return frame


def add(mini, key: str, ledger=LEDGER, root=ROOT, adjustments_path=ADJUSTMENTS, now=None) -> dict:
    """Lint the card, derive its timing from evidence, check its adjustments, and append rows to both tables once."""
    root = Path(root)
    meta, rows, problems = picks.lint_card(mini, key, root)
    if problems:
        raise LedgerError("card does not lint clean, nothing appended:\n - " + "\n - ".join(problems))
    card = _card_text(mini, key)
    adjustments = parse_adjustments(card, key)
    problems = check_adjustments(adjustments, meta, rows, root)
    if problems:
        raise LedgerError("adjustments do not check, nothing appended:\n - " + "\n - ".join(problems))
    path = root / ledger
    existing = read(path)
    if (existing["local_key"] == key).any():
        raise LedgerError(f"{key} is already in the ledger; a changed forecast is a dated addendum, never a second ledger entry")
    apath = root / adjustments_path
    prior = read_adjustments(apath)
    if (prior["local_key"] == key).any():
        raise LedgerError(f"{key} already has adjustment rows; they are immutable")
    timing, evidence = derive_timing(meta, card, key, mini, root)
    head = {k: meta.get(k, "") for k in HEAD if k not in ("local_key", "timing", "timing_claimed", "timing_evidence")}
    head.update(timing=timing, timing_claimed=meta["timing"], timing_evidence=evidence)
    new = [dict(head, local_key=key, **row) for row in rows]
    path.parent.mkdir(parents=True, exist_ok=True)
    if existing.empty and not path.exists():
        path.write_bytes(_csv(new, FIELDS))
    else:
        with open(path, "a", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=list(FIELDS), lineterminator="\n")
            writer.writerows(new)
    if adjustments:
        previous = prior["row_sha256"].iloc[-1] if len(prior) else ""
        effects, stamp, out = effect_rows(root), (now or datetime.now().astimezone()).isoformat(), []
        for a in adjustments:
            eff = effects.get(a["effect_row_id"], {})
            body = dict(local_key=key, **a, effect_status=eff.get("status", "NOT_ESTIMATED"), effect_estimate=eff.get("estimate", ""),
                        effect_version=eff.get("version", "SCENARIO_NO_TABLE"), added_at=stamp, previous_sha256=previous)
            body["row_sha256"] = previous = _sha(_csv([body], list(body)))
            out.append(body)
        if not apath.exists():
            apath.write_bytes(_csv(out, ADJ_FIELDS))
        else:
            with open(apath, "a", newline="", encoding="utf-8") as fh:
                csv.DictWriter(fh, fieldnames=list(ADJ_FIELDS), lineterminator="\n").writerows(out)
    return dict(local_key=key, rows=len(new), tier=meta["tier"], abstain=meta["abstain"], timing=timing, timing_evidence=evidence,
                adjustments=len(adjustments))


def _logit(p):
    p = np.clip(np.asarray(p, float), 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


def adjustment_lambda(reference, final, outcome, min_rows: int = MIN_LAMBDA_ROWS) -> dict:
    """lambda in logit P = logit(reference) + lambda * (logit(final) - logit(reference)).

    1 means the analyst's adjustments were worth their full size, 0 that they added nothing, above 1 that they were too
    timid. Estimated by Newton-Raphson from the rows the analyst actually moved; NOT_ESTIMATED below ``min_rows``.
    """
    ref, fin, y = (np.asarray(x, float) for x in (reference, final, outcome))
    keep = np.isfinite(ref) & np.isfinite(fin) & np.isfinite(y) & (np.abs(_logit(fin) - _logit(ref)) > 1e-9)
    n = int(keep.sum())
    if n < min_rows:
        return dict(n=n, status="NOT_ESTIMATED", reason=f"{n} adjusted rows; {min_rows} needed", lam=float("nan"), se=float("nan"))
    offset, delta, y = _logit(ref[keep]), (_logit(fin[keep]) - _logit(ref[keep])), y[keep]
    lam = 0.0
    for _ in range(50):
        q = 1 / (1 + np.exp(-(offset + lam * delta)))
        grad, hess = float(np.sum((y - q) * delta)), float(np.sum(q * (1 - q) * delta * delta))
        if hess <= 0:
            break
        step = grad / hess
        lam += step
        if abs(step) < 1e-9:
            break
    q = 1 / (1 + np.exp(-(offset + lam * delta)))
    hess = float(np.sum(q * (1 - q) * delta * delta))
    return dict(n=n, status="ESTIMATED", reason="", lam=lam, se=math.sqrt(1 / hess) if hess > 0 else float("nan"))


def _frame(ledger: pd.DataFrame, results: pd.DataFrame) -> pd.DataFrame:
    if not {"local_key", "label", "grade"} <= set(results.columns):
        raise LedgerError("RESULTS.csv needs local_key,label,grade")
    frame = ledger.merge(results[["local_key", "label", "grade"]], on=["local_key", "label"], how="inner", validate="one_to_one")
    frame = frame[frame["grade"].isin(["WIN", "LOSS"])].copy()
    frame["y"] = (frame["grade"] == "WIN").astype(float)
    for col in ("final_p", "reference_p", "baseline_p", "model_p", "line_implied_p"):
        frame[col + "_n"] = pd.to_numeric(frame[col], errors="coerce")
    frame["week"] = M.iso_week(pd.to_datetime(frame["scheduled_start"], utc=True)) if len(frame) else pd.Series(dtype=str)
    frame["stratum"] = stratum(frame) if len(frame) else pd.Series(dtype=str)
    return frame


def stratum(frame: pd.DataFrame) -> pd.Series:
    """SCORING_AND_VALIDATION §12: timing, fast or full card, supplied or derived line, reference executed or baseline only."""
    ref = frame["reference_status"].map(lambda s: "EXECUTED" if s == "EXECUTED" else "BASELINE_ONLY" if s == "BASELINE_ONLY" else "NONE")
    card = frame["fast_card"].map(lambda f: "FAST" if f == "YES" else "FULL")
    timing = frame["timing"].map(lambda t: "PREGAME" if t in picks.PRE_START_COHORT else t)  # TIMING-v3 pools the two
    return "timing=" + timing + "|card=" + card + "|line=" + frame["line_source"] + "|reference=" + ref


def _paired(frame: pd.DataFrame, other: str, scope: str, label: str, stratum_name: str) -> dict | None:
    sub = frame.dropna(subset=["final_p_n", other])
    if sub.empty:
        return None
    d = M.brier(sub["final_p_n"], sub["y"]) - M.brier(sub[other], sub["y"])
    interval = M.paired_week_interval(pd.Series(d), sub["local_key"].reset_index(drop=True), sub["week"].reset_index(drop=True))
    return dict(stratum=stratum_name, comparison=f"final minus {label}", scope=scope, n_rows=len(sub),
                n_events=int(sub["local_key"].nunique()), brier_final=round(float(M.brier(sub["final_p_n"], sub["y"]).mean()), 4),
                brier_other=round(float(M.brier(sub[other], sub["y"]).mean()), 4),
                mean_diff=round(interval["mean"], 4) if not math.isnan(interval["mean"]) else "", k_weeks=interval["k_weeks"],
                lo=round(interval["lo"], 4) if not math.isnan(interval["lo"]) else "",
                hi=round(interval["hi"], 4) if not math.isnan(interval["hi"]) else "", status=interval["status"])


def effect_scores(frame: pd.DataFrame, adjustments: pd.DataFrame) -> list[dict]:
    """Per effect row: final p against the frozen counterfactual without that adjustment, on the same decisive rows."""
    if adjustments.empty or frame.empty:
        return []
    keyed = frame.set_index(["local_key", "label"])
    rows = []
    for a in adjustments.to_dict("records"):
        for part in [s for s in a["counterfactual"].split("|") if s.strip()]:
            label, _, value = part.partition("=")
            if (a["local_key"], label) in keyed.index:
                r = keyed.loc[(a["local_key"], label)]
                rows.append(dict(effect_row_id=a["effect_row_id"], effect_version=a["effect_version"], local_key=a["local_key"],
                                 label=label, final=float(r["final_p_n"]), counterfactual=float(value), y=float(r["y"]),
                                 week=r["week"], stratum=r["stratum"]))
    if not rows:
        return []
    df = pd.DataFrame(rows)
    out = []
    for (effect, version, strat), g in df.groupby(["effect_row_id", "effect_version", "stratum"]):
        d = M.brier(g["final"], g["y"]) - M.brier(g["counterfactual"], g["y"])
        iv = M.paired_week_interval(pd.Series(d), g["local_key"].reset_index(drop=True), g["week"].reset_index(drop=True))
        out.append(dict(effect_row_id=effect, effect_version=version[:16], stratum=strat, n_rows=len(g), n_events=int(g["local_key"].nunique()),
                        mean_diff=round(iv["mean"], 4) if not math.isnan(iv["mean"]) else "", k_weeks=iv["k_weeks"], status=iv["status"]))
    return out


def score(ledger_path, results_path, benchmarks_path=None, root=ROOT, adjustments_path=None) -> dict:
    """Paired scores of final p against every reference on identical decisive rows, within each stratum; never pooled across."""
    root = Path(root)
    ledger = read(Path(ledger_path))
    results = pd.read_csv(results_path, dtype=str)
    frame = _frame(ledger, results)
    if benchmarks_path:
        bench = B.load(benchmarks_path)
        wide = bench.pivot(index=["local_key", "label"], columns="benchmark_id", values="p").reset_index()
        frame = frame.merge(wide, on=["local_key", "label"], how="left")
    refs = [("reference_p_n", "reference"), ("baseline_p_n", "league baseline"), ("model_p_n", "frozen model"),
            ("line_implied_p_n", "line-implied 0.5")]
    refs += [(b, b) for b in B.IDS if b in frame.columns]
    rows, lams = [], []
    for name, part in (frame.groupby("stratum") if len(frame) else []):
        scopes = {"ALL_IN_STRATUM": part, **{f"TIER_{t}": part[part["tier"] == t] for t in sorted(part["tier"].unique())},
                  **{f"FAMILY_{f}": part[part["family"] == f] for f in sorted(part["family"].unique())},
                  "INFORMATION_ROWS": part[part["information_row"] == "Y"], "MOST_LIKELY_LIST": part[part["most_likely_rank"] != ""]}
        for scope, sub in scopes.items():
            if sub.empty:
                continue
            for col, label in refs:
                r = _paired(sub, col, scope, label, name)
                if r:
                    rows.append(r)
        adj = part.dropna(subset=["reference_p_n"])
        lams.append(dict(stratum=name, **adjustment_lambda(adj["reference_p_n"], adj["final_p_n"], adj["y"])))
    cal = M.calibration_fit(frame["final_p_n"], frame["y"]) if len(frame) >= 10 else {}
    adjustments = read_adjustments(Path(adjustments_path)) if adjustments_path else pd.DataFrame(columns=ADJ_FIELDS)
    lam = lams[0] if len(lams) == 1 else dict(n=sum(l["n"] for l in lams), status="BY_STRATUM", reason="see lambda_by_stratum",
                                               lam=float("nan"), se=float("nan"))
    return dict(scores=rows, lam=lam, lambda_by_stratum=lams, calibration=cal, rows=len(frame),
                events=int(frame["local_key"].nunique()) if len(frame) else 0, effects=effect_scores(frame, adjustments))


def coverage(ledger_path, actuals_path) -> list[dict]:
    """z = (actual - centre) / sd per card and quantity: RMS and the share beyond 1 and 2 SD, against the 0.85-1.15 band."""
    ledger = read(Path(ledger_path))
    actuals = pd.read_csv(actuals_path, dtype={"local_key": str, "quantity": str})
    first = ledger[ledger["quantity"].isin(["MARGIN", "TOTAL"])].drop_duplicates(["local_key", "quantity"])
    merged = first.merge(actuals, on=["local_key", "quantity"], how="inner")
    merged["z"] = (pd.to_numeric(merged["actual"]) - pd.to_numeric(merged["centre"])) / pd.to_numeric(merged["sd"])
    out = []
    for (quantity, family), sub in [(("ALL", "ALL"), merged)] + [((q, "ALL"), g) for q, g in merged.groupby("quantity")]:
        if quantity == "ALL" and family == "ALL":
            sub = merged
        z = sub["z"].to_numpy(float)
        if not len(z):
            continue
        rms = float(np.sqrt(np.mean(z ** 2)))
        out.append(dict(quantity=quantity, cards=len(z), z_rms=round(rms, 3), share_beyond_1=round(float(np.mean(np.abs(z) > 1)), 3),
                        share_beyond_2=round(float(np.mean(np.abs(z) > 2)), 3), mean_z=round(float(z.mean()), 3),
                        status=("INSUFFICIENT_EVIDENCE" if len(z) < MIN_COVERAGE_CARDS else
                                "WITHIN_BAND" if COVERAGE_BAND[0] <= rms <= COVERAGE_BAND[1] else "OUTSIDE_BAND")))
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    ad = sub.add_parser("add")
    ad.add_argument("--mini", type=Path, required=True)
    ad.add_argument("--key", required=True)
    sub.add_parser("verify")
    sc = sub.add_parser("score")
    sc.add_argument("--results", type=Path, required=True)
    sc.add_argument("--benchmarks", type=Path)
    sc.add_argument("--out", type=Path, required=True)
    cv = sub.add_parser("coverage")
    cv.add_argument("--actuals", type=Path, required=True)
    cv.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "add":
            print(add(args.mini, args.key))
        elif args.command == "verify":
            frame, adjustments = read(ROOT / LEDGER), read_adjustments(ROOT / ADJUSTMENTS)
            print(f"ledger ok: {len(frame)} rows, {frame['local_key'].nunique()} cards; adjustments chain ok: {len(adjustments)} rows")
        elif args.command == "score":
            result = score(ROOT / LEDGER, args.results, args.benchmarks, adjustments_path=ROOT / ADJUSTMENTS)
            args.out.mkdir(parents=True, exist_ok=False)
            cols = ["stratum", "comparison", "scope", "n_rows", "n_events", "brier_final", "brier_other", "mean_diff", "k_weeks", "lo", "hi",
                    "status"]
            (args.out / "LEDGER_SCORES.csv").write_bytes(_csv(result["scores"], cols) if result["scores"] else (",".join(cols) + "\n").encode())
            (args.out / "ADJUSTMENT_LAMBDA.csv").write_bytes(_csv(result["lambda_by_stratum"], ["stratum", "n", "status", "reason", "lam", "se"]))
            ecols = ["effect_row_id", "effect_version", "stratum", "n_rows", "n_events", "mean_diff", "k_weeks", "status"]
            (args.out / "EFFECT_SCORES.csv").write_bytes(_csv(result["effects"], ecols))
            print(f"scored {result['rows']} decisive rows on {result['events']} cards in {len(result['lambda_by_stratum'])} strata; "
                  f"{len(result['effects'])} effect rows")
        else:
            rows = coverage(ROOT / LEDGER, args.actuals)
            args.out.mkdir(parents=True, exist_ok=False)
            (args.out / "WIDTH_COVERAGE.csv").write_bytes(_csv(rows, ["quantity", "cards", "z_rms", "share_beyond_1", "share_beyond_2", "mean_z",
                                                                      "status"]))
            for r in rows:
                print(r)
    except (LedgerError, picks.PicksError, B.BenchmarkError, FileExistsError) as exc:
        print(f"REFUSED: {exc}")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
