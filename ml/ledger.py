"""Adjustment ledger and its settlement-time scoring (LEDGER-v1 / BENCH-v1 / WIDTH-v1).

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
"""
from __future__ import annotations

import argparse
import csv
import io
import math
from pathlib import Path

import numpy as np
import pandas as pd

from ml import benchmarks as B, picks
from ml.core import metrics as M

ROOT = Path(__file__).resolve().parents[1]
LEDGER = "research/adjustment_ledger/ADJUSTMENT_LEDGER.csv"
HEAD = ("local_key", "competition", "tier", "timing", "scheduled_start", "issued_at", "reference_id", "reference_status", "abstain", "fast_card")
FIELDS = HEAD + picks.COLUMNS
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


def add(mini, key: str, ledger=LEDGER, root=ROOT) -> dict:
    """Lint the card's PICKS_V2 block and append its rows. A card is ledgered once; later reforecasts are addenda."""
    root = Path(root)
    meta, rows, problems = picks.lint_card(mini, key, root)
    if problems:
        raise LedgerError("card does not lint clean, nothing appended:\n - " + "\n - ".join(problems))
    path = root / ledger
    existing = read(path)
    if (existing["local_key"] == key).any():
        raise LedgerError(f"{key} is already in the ledger; a changed forecast is a dated addendum, never a second ledger entry")
    new = [dict({k: meta.get(k, "") for k in HEAD if k != "local_key"}, local_key=key, **row) for row in rows]
    path.parent.mkdir(parents=True, exist_ok=True)
    if existing.empty and not path.exists():
        path.write_bytes(_csv(new, FIELDS))
    else:
        with open(path, "a", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=list(FIELDS), lineterminator="\n")
            writer.writerows(new)
    return dict(local_key=key, rows=len(new), tier=meta["tier"], abstain=meta["abstain"])


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
    return frame


def _paired(frame: pd.DataFrame, other: str, scope: str, label: str) -> dict | None:
    sub = frame.dropna(subset=["final_p_n", other])
    if sub.empty:
        return None
    d = M.brier(sub["final_p_n"], sub["y"]) - M.brier(sub[other], sub["y"])
    interval = M.paired_week_interval(pd.Series(d), sub["local_key"].reset_index(drop=True), sub["week"].reset_index(drop=True))
    return dict(comparison=f"final minus {label}", scope=scope, n_rows=len(sub), n_events=int(sub["local_key"].nunique()),
                brier_final=round(float(M.brier(sub["final_p_n"], sub["y"]).mean()), 4), brier_other=round(float(M.brier(sub[other], sub["y"]).mean()), 4),
                mean_diff=round(interval["mean"], 4) if not math.isnan(interval["mean"]) else "", k_weeks=interval["k_weeks"],
                lo=round(interval["lo"], 4) if not math.isnan(interval["lo"]) else "", hi=round(interval["hi"], 4) if not math.isnan(interval["hi"]) else "",
                status=interval["status"])


def score(ledger_path, results_path, benchmarks_path=None, root=ROOT) -> dict:
    """Paired scores of final p against every reference on identical decisive rows, by scope; plus lambda and calibration."""
    root = Path(root)
    ledger = read(Path(ledger_path))
    results = pd.read_csv(results_path, dtype=str)
    frame = _frame(ledger, results)
    if benchmarks_path:
        bench = B.load(benchmarks_path)
        wide = bench.pivot(index=["local_key", "label"], columns="benchmark_id", values="p").reset_index()
        frame = frame.merge(wide, on=["local_key", "label"], how="left")
    rows = []
    scopes = {"ALL": frame, **{f"TIER_{t}": frame[frame["tier"] == t] for t in sorted(frame["tier"].unique())},
              **{f"FAMILY_{f}": frame[frame["family"] == f] for f in sorted(frame["family"].unique())},
              "INFORMATION_ROWS": frame[frame["information_row"] == "Y"], "MOST_LIKELY_LIST": frame[frame["most_likely_rank"] != ""]}
    refs = [("reference_p_n", "reference"), ("baseline_p_n", "league baseline"), ("model_p_n", "frozen model"),
            ("line_implied_p_n", "line-implied 0.5")]
    refs += [(b, b) for b in B.IDS if b in frame.columns]
    for scope, sub in scopes.items():
        if sub.empty:
            continue
        for col, label in refs:
            r = _paired(sub, col, scope, label)
            if r:
                rows.append(r)
    adj = frame.dropna(subset=["reference_p_n"])
    lam = adjustment_lambda(adj["reference_p_n"], adj["final_p_n"], adj["y"])
    cal = M.calibration_fit(frame["final_p_n"], frame["y"]) if len(frame) >= 10 else {}
    return dict(scores=rows, lam=lam, calibration=cal, rows=len(frame), events=int(frame["local_key"].nunique()) if len(frame) else 0)


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
            frame = read(ROOT / LEDGER)
            print(f"ledger ok: {len(frame)} rows, {frame['local_key'].nunique()} cards")
        elif args.command == "score":
            result = score(ROOT / LEDGER, args.results, args.benchmarks)
            args.out.mkdir(parents=True, exist_ok=False)
            cols = ["comparison", "scope", "n_rows", "n_events", "brier_final", "brier_other", "mean_diff", "k_weeks", "lo", "hi", "status"]
            (args.out / "LEDGER_SCORES.csv").write_bytes(_csv(result["scores"], cols) if result["scores"] else (",".join(cols) + "\n").encode())
            (args.out / "ADJUSTMENT_LAMBDA.csv").write_bytes(_csv([result["lam"]], ["n", "status", "reason", "lam", "se"]))
            print(f"scored {result['rows']} decisive rows on {result['events']} cards; lambda {result['lam']['status']}")
        else:
            rows = coverage(ROOT / LEDGER, args.actuals)
            args.out.mkdir(parents=True, exist_ok=False)
            (args.out / "WIDTH_COVERAGE.csv").write_bytes(_csv(rows, ["quantity", "cards", "z_rms", "share_beyond_1", "share_beyond_2", "mean_z", "status"]))
            for r in rows:
                print(r)
    except (LedgerError, picks.PicksError, B.BenchmarkError, FileExistsError) as exc:
        print(f"REFUSED: {exc}")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
