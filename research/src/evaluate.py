"""Chronological league holdout and week-block paired evaluation."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from .dixon_coles import fit_dc, predict
from .features import population_1x2, tb1_md
from .load import PROCESSED, sha

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
TUNING_SEASONS = ("2021-22", "2022-23", "2023-24", "2024-25")
HOLDOUT = "2025-26"
XI_GRID = (0.001, 0.0019, 0.003)
BOOTSTRAP_REPS = 10000
SEED = 20260929


def groups(df: pd.DataFrame, seasons: tuple[str, ...]):
    subset = df.loc[df.season.isin(seasons)].copy()
    iso = subset.kickoff_utc.dt.isocalendar()
    subset["week_key"] = iso.year.astype(str) + "-W" + iso.week.astype(str).str.zfill(2)
    for week_key, block in subset.groupby("week_key", sort=True):
        first_day = block.kickoff_utc.min().date()
        cutoff = pd.Timestamp(first_day, tz="UTC")
        yield week_key, cutoff, block.sort_values("kickoff_utc")


def forecast(df: pd.DataFrame, seasons: tuple[str, ...], xi: float,
             output: Path | None = None) -> pd.DataFrame:
    rows = []
    for week_no, (week, cutoff, block) in enumerate(groups(df, seasons), 1):
        model = fit_dc(df, cutoff, xi)
        m0 = population_1x2(df, cutoff)
        for game in block.itertuples():
            m2, _, tail = predict(model, game.home, game.away)
            m1 = tb1_md(df, game.season, cutoff, game.home, game.away)
            outcome = "H" if game.hg > game.ag else "A" if game.ag > game.hg else "D"
            rec = dict(season=game.season, week_key=week,
                       cutoff_utc=cutoff.isoformat(), kickoff_utc=game.kickoff_utc.isoformat(),
                       home=game.home, away=game.away, hg=game.hg, ag=game.ag,
                       result=outcome, training_matches=model.training_matches,
                       xi=xi, grid_tail=tail)
            for label, probs in (("m0", m0), ("m1", m1), ("m2", m2)):
                if abs(sum(probs[k] for k in ("H", "D", "A"))-1) > 1e-9:
                    raise AssertionError("noncoherent 1X2")
                for key in ("H", "D", "A"):
                    rec[f"{label}_{key}"] = probs[key]
                rec[f"{label}_logloss"] = float(-np.log(probs[outcome]))
                rec[f"{label}_brier"] = float(sum((probs[k] - (k == outcome))**2 for k in ("H", "D", "A")))
            rows.append(rec)
        if output and week_no % 10 == 0:
            print(f"{output.name}: {week_no} weeks, {len(rows)} matches", flush=True)
    result = pd.DataFrame(rows).sort_values("kickoff_utc").reset_index(drop=True)
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        result.to_csv(output, index=False, float_format="%.12g")
    return result


def paired_interval(frame: pd.DataFrame, a: str, b: str,
                    metric: str = "logloss", reps: int = BOOTSTRAP_REPS) -> dict:
    col_a, col_b = f"{a}_{metric}", f"{b}_{metric}"
    grouped = frame.assign(delta=frame[col_a]-frame[col_b]).groupby("week_key").delta.agg(["sum", "count"])
    sums = grouped["sum"].to_numpy()
    counts = grouped["count"].to_numpy()
    rng = np.random.default_rng(SEED)
    picks = rng.integers(0, len(sums), size=(reps, len(sums)))
    boot = sums[picks].sum(axis=1) / counts[picks].sum(axis=1)
    return dict(mean=float((frame[col_a]-frame[col_b]).mean()),
                ci95=[float(np.quantile(boot, .025)), float(np.quantile(boot, .975))],
                blocks=len(sums), events=len(frame))


def calibration(frame: pd.DataFrame, label: str) -> list[dict]:
    probs = frame[[f"{label}_{x}" for x in ("H", "D", "A")]].to_numpy()
    best = probs.argmax(axis=1)
    confidence = probs[np.arange(len(probs)), best]
    correct = np.array([("H", "D", "A")[i] == o for i, o in zip(best, frame.result)])
    output = []
    for lo, hi in ((0, .4), (.4, .5), (.5, .6), (.6, .7), (.7, 1.01)):
        selected = (confidence >= lo) & (confidence < hi)
        output.append(dict(bin=f"[{lo:.1f},{min(hi,1):.1f})", n=int(selected.sum()),
                           mean_confidence=float(confidence[selected].mean()) if selected.any() else None,
                           accuracy=float(correct[selected].mean()) if selected.any() else None))
    return output


def summarize(frame: pd.DataFrame) -> dict:
    return dict(n_matches=len(frame), n_week_blocks=frame.week_key.nunique(),
                models={x: dict(logloss=float(frame[f"{x}_logloss"].mean()),
                                multiclass_brier=float(frame[f"{x}_brier"].mean()),
                                calibration=calibration(frame, x)) for x in ("m0", "m1", "m2")},
                m2_minus_m0=paired_interval(frame, "m2", "m0"),
                m2_minus_m1=paired_interval(frame, "m2", "m1"),
                m1_minus_m0=paired_interval(frame, "m1", "m0"))


def run_tuning() -> dict:
    lock_path = RUNS / "epl_tuning_lock.json"
    if lock_path.exists() or any(RUNS.glob("epl_tuning_xi_*.csv")):
        raise RuntimeError("EPL tuning already locked; create a new versioned development protocol, never overwrite")
    df = pd.read_parquet(PROCESSED / "matches.parquet")
    RUNS.mkdir(exist_ok=True)
    results = {}
    for xi in XI_GRID:
        filename = RUNS / f"epl_tuning_xi_{str(xi).replace('.', '_')}.csv"
        frame = forecast(df, TUNING_SEASONS, xi, filename)
        results[str(xi)] = dict(mean_m2_logloss=float(frame.m2_logloss.mean()),
                                n=len(frame), output_sha256=sha(filename))
    best = min(XI_GRID, key=lambda x: (results[str(x)]["mean_m2_logloss"], x))
    manifest = dict(stage="TUNING_LOCK", created_utc=datetime.now(timezone.utc).isoformat(),
                    data_sha256=sha(PROCESSED / "matches.parquet"), seasons=TUNING_SEASONS,
                    xi_grid=XI_GRID, selected_xi=best, criterion="minimum mean 1X2 log-loss",
                    model_version="epl-dc-0.1.0", fixed_bootstrap_reps=BOOTSTRAP_REPS,
                    seed=SEED, results=results,
                    code_sha256={str(p.relative_to(ROOT.parent)).replace('\\','/'):sha(p)
                        for p in (Path(__file__), Path(__file__).with_name("dixon_coles.py"),
                                  Path(__file__).with_name("features.py"), Path(__file__).with_name("load.py"))})
    with lock_path.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(manifest, indent=2)+"\n")
    return manifest


def run_holdout() -> dict:
    result_path = RUNS / "epl_2025-26_holdout.csv"
    report_path = RUNS / "epl_2025-26_holdout.json"
    if result_path.exists() or report_path.exists():
        raise RuntimeError("one-shot holdout already exists; do not overwrite")
    lock_path = RUNS / "epl_tuning_lock.json"
    if not lock_path.exists():
        raise RuntimeError("tuning lock is required before holdout")
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    if sha(PROCESSED / "matches.parquet") != lock["data_sha256"]:
        raise RuntimeError("data changed after tuning lock")
    if not lock.get("code_sha256"):
        raise RuntimeError("new holdouts require code hashes frozen before evaluation; historical lock is read-only")
    for name, digest in lock["code_sha256"].items():
        if sha(ROOT.parent / name) != digest:
            raise RuntimeError("code changed after tuning lock: "+name)
    df = pd.read_parquet(PROCESSED / "matches.parquet")
    frame = forecast(df, (HOLDOUT,), lock["selected_xi"], result_path)
    report = summarize(frame)
    report.update(stage="ONE_SHOT_HOLDOUT", created_utc=datetime.now(timezone.utc).isoformat(),
                  holdout=HOLDOUT, xi=lock["selected_xi"], tuning_lock_sha256=sha(lock_path),
                  data_sha256=lock["data_sha256"], forecasts_sha256=sha(result_path))
    if report["m2_minus_m0"]["ci95"][1] < 0:
        report["lane_decision"] = "M2_PASS"
    elif report["m1_minus_m0"]["ci95"][1] < 0:
        report["lane_decision"] = "M1_ONLY_PASS"
    else:
        report["lane_decision"] = "STOP"
    with report_path.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(report, indent=2)+"\n")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=("tune", "holdout"))
    args = parser.parse_args()
    print(json.dumps(run_tuning() if args.stage == "tune" else run_holdout(), indent=2))
