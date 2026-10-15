"""Workshop runner: discover every competition in the archive, tune, evaluate and write outputs with receipts.

python -m ml discover                        list every competition folder with its status and reason
python -m ml run-all [--workers N]           every modellable competition, then card calibration, decision lab, STATUS
python -m ml competition "Basketball/NBL"    one or more competitions by archive path
python -m ml cards | decision-lab | index
Outputs: research/model_shadow/** (Markdown + market-free CSV). Full predictions go to the cache directory outside the
repository (env ML_CACHE, default ../Sports-Research-workshop-cache).
"""
from __future__ import annotations

import hashlib
import os
import sys
import time
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np
import pandas as pd

from ml.config import REPO_ROOT, League, discover
from ml.data.archive import load_league, snapshot_hash, seasons_available, training_frame
from ml.evaluation import backtest, report

CACHE = Path(os.environ.get("ML_CACHE", REPO_ROOT.parent / "Sports-Research-workshop-cache"))
EPL_PATH = "Soccer/Premier League"


def code_digest() -> str:
    h = hashlib.sha256()
    for p in sorted((REPO_ROOT / "ml").rglob("*.py")):
        if "tests" in p.parts:
            continue
        h.update(p.relative_to(REPO_ROOT).as_posix().encode())
        h.update(p.read_bytes().replace(b"\r\n", b"\n"))
    return h.hexdigest()


def receipt_base() -> dict:
    import subprocess

    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()
    return {"run_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "repo_head": head,
            "code_sha256": code_digest(), "python": sys.version.split()[0], "numpy": np.__version__,
            "pandas": pd.__version__, "scipy": __import__("scipy").__version__}


def finish_receipt(rec: dict, input_checks=()) -> dict:
    """Refuse to stamp a completed run after its generating source changed on disk."""
    if code_digest() != rec["code_sha256"]:
        raise RuntimeError("generating source changed during run; preserve diagnostics and rerun from a stable checkout")
    for label, expected, current in input_checks:
        if current() != expected:
            raise RuntimeError(f"{label} changed during run; rerun from stable inputs")
    return {**rec, "completed_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}


def run_competition(lg: League, log=print) -> dict:
    """Tune, evaluate and write one score-model competition; returns its STATUS row."""
    from ml.evaluation.writers import write_league

    rec = receipt_base()
    archive_digest = lambda: snapshot_hash(lg, seasons_available(lg))
    rec["archive_snapshot_sha256"] = archive_digest()
    t0 = time.time()
    games, load = load_league(lg)
    best, tune_table = backtest.tune(lg, games, log=lambda *a: None)
    best = {k: (bool(v) if isinstance(v, (bool, np.bool_)) else float(v)) for k, v in best.items()}
    variants = {}
    if lg.sport in ("American Football", "Canadian Football", "College Football"):
        variants["KEYNUM"] = {**best, "key_numbers": True}
    seasons = tuple(sorted({lg.tune_seasons[-1], *lg.test_seasons} | (set(lg.tune_seasons) if lg.path == EPL_PATH else set())))
    pred = backtest.evaluate(lg, best, seasons, games, extra_variants=variants, log=lambda *a: None)
    test = pred[pred["season"].isin(lg.test_seasons)]
    pt = report.paired_table(test, "MODEL", lg.test_seasons)
    verdict = report.development_verdict(pt, lg.test_seasons)
    extra = {}
    if variants:
        extra["KEYNUM_vs_MODEL"] = pd.DataFrame([
            {"metric": label, "season": s, **report.paired_week_interval(
                (d[f"KEYNUM_{key}"] - d[f"MODEL_{key}"]), d["event_id"], d["week"])}
            for key, label in report.METRICS if f"KEYNUM_{key}" in test
            for s in [*lg.test_seasons, "ALL"]
            for d in [test if s == "ALL" else test[test["season"] == s]]])
    cal = report.platt_by_previous_season(pred, "MODEL", lg.test_seasons)
    calib = report.calibration_block(test, "MODEL")
    last = games["date"].max()
    as_of = last + pd.Timedelta(days=1)
    season_last = int(games.loc[games["date"] == last, "season"].iloc[0])
    tr = training_frame(games)
    tr = tr[(tr["date"] < as_of) & (tr["season"] >= season_last - lg.history_seasons)]
    final = backtest.make_model(lg, best)
    final.fit(tr, as_of, season_last) if lg.engine != "gaussian" else final.fit(tr, as_of)
    res = {"league": lg, "best": best, "tune_table": tune_table, "pred": pred, "paired": pt, "verdict": verdict,
           "extra": extra, "calibration_experiment": cal, "calibration": calib, "load": load, "final_model": final,
           "final_as_of": as_of, "final_season": season_last,
           "data_sha": rec["archive_snapshot_sha256"], "seconds": time.time() - t0}
    prediction_bytes = pred.to_csv(index=False, lineterminator="\n").encode("utf8")
    rec["prediction_source_sha256"] = hashlib.sha256(prediction_bytes).hexdigest()
    completed_receipt = finish_receipt(rec, [("archive inputs", rec["archive_snapshot_sha256"], archive_digest)])
    CACHE.mkdir(parents=True, exist_ok=True)
    (CACHE / f"{lg.model_id}_predictions.csv").write_bytes(prediction_bytes)
    (CACHE / f"{lg.model_id}_predictions_RECEIPT.md").write_text("# Development prediction cache receipt\n\n" + "\n".join(f"- `{key}`: {value}" for key, value in completed_receipt.items()) + "\n", encoding="utf8", newline="\n")
    row = write_league(res, completed_receipt)
    log(f"[{lg.model_id}] {verdict['overall']} ({time.time() - t0:.0f}s)")
    return row


def run_cricket(lg: League, log=print) -> dict:
    from ml.evaluation.writers import write_cricket
    from ml.models.cricket import tune_and_evaluate

    rec = receipt_base()
    archive_digest = lambda: snapshot_hash(lg, seasons_available(lg))
    rec["archive_snapshot_sha256"] = archive_digest()
    t0 = time.time()
    res = tune_and_evaluate(lg, log=lambda *a: None)
    res["league"] = lg
    res["seconds"] = time.time() - t0
    row = write_cricket(res, finish_receipt(rec, [("archive inputs", rec["archive_snapshot_sha256"], archive_digest)]))
    log(f"[{lg.model_id}] {row['development_verdict']} ({time.time() - t0:.0f}s)")
    return row


def _worker(lg: League) -> dict:
    try:
        return run_cricket(lg) if lg.engine == "cricket" else run_competition(lg)
    except Exception as e:  # recorded, never hidden
        return {"model_id": lg.model_id, "competition": lg.path, "engine": lg.engine, "status": "RUN_FAILED",
                "development_verdict": "NOT_COMPUTED", "detail": f"{type(e).__name__}: {e}"[:300],
                "test_seasons": ",".join(map(str, lg.test_seasons)), "tb1": lg.tb1_label,
                "data_warnings": ";".join(lg.data_warnings),
                "traceback": traceback.format_exc()}


def not_modelled_rows(found) -> list[dict]:
    return [{"model_id": d.league.model_id if d.league else "", "competition": d.path,
             "engine": d.league.engine if d.league else "", "status": "NOT_MODELLED", "development_verdict": "",
             "detail": d.reason, "test_seasons": "", "tb1": "",
             "data_warnings": ";".join(d.league.data_warnings) if d.league else ""} for d in found if d.status != "MODELLED"]


def run_all(workers: int, only: list[str] | None = None, log=print) -> list[dict]:
    if not isinstance(workers, int) or workers < 1:
        raise ValueError("workers must be a positive integer")
    found = discover()
    if only is not None:
        eligible = {d.path for d in found if d.status == "MODELLED"}
        if not only or any(path not in eligible for path in only):
            raise ValueError("competition request must name existing modellable paths: " + ", ".join(only))
    todo = [d.league for d in found if d.status == "MODELLED" and (only is None or d.path in only)]
    log(f"discovered {len(found)} competition folders; modelling {len(todo)} with {workers} workers")
    rows = []
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(_worker, lg): lg for lg in todo}
        for f in as_completed(futs):
            r = f.result()
            rows.append({k: v for k, v in r.items() if k != "traceback"})
            log(f"  done {r['model_id']}: {r['status']} {r.get('development_verdict', '')} {r.get('detail', '')[:120]}")
            if r["status"] == "RUN_FAILED":
                log(r.get("traceback", ""))
    return rows + (not_modelled_rows(found) if only is None else [])


def run_cards() -> None:
    from ml.evaluation.card_calibration import audit
    from ml.evaluation.writers import write_cards

    rec = receipt_base()
    rec["rank_log_sha256"] = hashlib.sha256((REPO_ROOT / "GAME_PREDICTION_RANK_LOG.csv").read_bytes()).hexdigest()
    rank_digest = lambda: hashlib.sha256((REPO_ROOT / "GAME_PREDICTION_RANK_LOG.csv").read_bytes()).hexdigest()
    write_cards(audit(), finish_receipt(rec, [("rank log", rec["rank_log_sha256"], rank_digest)]))


def run_decision_lab() -> None:
    from ml.config import get_league
    from ml.decision.lab import run
    from ml.evaluation.writers import write_decision_lab

    lg = get_league(EPL_PATH)
    path = CACHE / f"{lg.model_id}_predictions.csv"
    if not path.exists():
        raise SystemExit(f"run the {EPL_PATH} competition first (the lab reads {path.name})")
    rec = receipt_base()
    rec["prediction_source_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    from ml.decision.lab import FD_DIR
    def market_digest():
        market_hash = hashlib.sha256()
        for market_file in sorted(FD_DIR.glob("*.csv")):
            market_hash.update(market_file.name.encode())
            market_hash.update(hashlib.sha256(market_file.read_bytes()).digest())
        return market_hash.hexdigest()
    rec["local_market_capture_sha256"] = market_digest()
    pred = pd.read_csv(path, parse_dates=["date", "fit_date"])
    prediction_digest = lambda: hashlib.sha256(path.read_bytes()).hexdigest()
    write_decision_lab(run(pred, model_id=lg.model_id), finish_receipt(rec, [("prediction inputs", rec["prediction_source_sha256"], prediction_digest), ("market inputs", rec["local_market_capture_sha256"], market_digest)]))


def main(argv: list[str]) -> None:
    if argv and argv[0] == "primary":
        from ml.primary import main as primary_main
        primary_main(argv[1:])
        return
    from ml.evaluation.writers import write_index

    if not argv:
        print(__doc__)
        return
    cmd, rest = argv[0], argv[1:]
    workers = 6
    if "--workers" in rest:
        i = rest.index("--workers")
        workers = int(rest[i + 1])
        rest = rest[:i] + rest[i + 2:]
    if cmd == "discover":
        for d in discover():
            lg = d.league
            print(f"{d.status:13} {d.path:55} {lg.model_id if lg else '':40} "
                  f"tune={list(lg.tune_seasons) if lg else ''} test={list(lg.test_seasons) if lg else ''} "
                  f"tb1={lg.tb1_label if lg else ''} warn={';'.join(lg.data_warnings) if lg else ''} | {d.reason}")
    elif cmd == "competition":
        for r in run_all(workers, only=rest):
            print(r)
    elif cmd == "run-all":
        rows = run_all(workers)
        write_index(receipt_base(), rows)
        run_cards()
        run_decision_lab()
        write_index(receipt_base())
    elif cmd == "cards":
        run_cards()
    elif cmd == "decision-lab":
        run_decision_lab()
    elif cmd == "index":
        write_index(receipt_base())
    else:
        raise SystemExit(f"unknown command {cmd}")
