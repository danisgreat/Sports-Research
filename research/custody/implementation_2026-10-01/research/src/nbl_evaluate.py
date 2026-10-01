"""Locked NBL22-25 tuning and one-shot NBL26 moneyline holdout."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from .load import ROOT, sha
from .nbl_model import fit, population_home, predict

DATA = ROOT / "data/processed/nbl_matches.parquet"
DATA_MANIFEST = ROOT / "data/processed/nbl_data_manifest.json"
RUNS = ROOT / "runs"
HALF_LIFE_GRID = (180, 365, 730)
BOOTSTRAP_REPS = 10000
SEED = 20260929
TUNING = ("NBL23", "NBL24", "NBL25")
HOLDOUT = "NBL26"
CODE = Path(__file__)
MODEL_CODE = Path(__file__).with_name("nbl_model.py")


def checked_data() -> pd.DataFrame:
    manifest = json.loads(DATA_MANIFEST.read_text(encoding="utf-8"))
    if manifest["games"] != 738 or manifest["unresolved"] != 0 or sha(DATA) != manifest["parquet_sha256"]:
        raise ValueError("NBL data manifest or source gate failed")
    df = pd.read_parquet(DATA)
    if len(df) != 738 or df.event_id.duplicated().any():
        raise ValueError("NBL event grain failed")
    if df.groupby("season").size().to_dict() != {"NBL22":148,"NBL23":140,"NBL24":140,
                                                  "NBL25":145,"NBL26":165}:
        raise ValueError("NBL season counts changed")
    if not df.score_validation_status.isin(("SECOND_SOURCE_AGREE", "ADJUDICATED_OFFICIAL")).all():
        raise ValueError("NBL uncorroborated score")
    return df


def week_groups(df: pd.DataFrame, seasons: tuple[str, ...]):
    subset = df.loc[df.season.isin(seasons)].copy()
    iso = subset.kickoff_utc.dt.isocalendar()
    subset["week_key"] = iso.year.astype(str) + "-W" + iso.week.astype(str).str.zfill(2)
    for week, block in subset.groupby("week_key", sort=True):
        cutoff = pd.Timestamp(block.kickoff_utc.min().date(), tz="UTC")
        yield week, cutoff, block.sort_values("kickoff_utc")


def forecast(df: pd.DataFrame, seasons: tuple[str, ...], half_life_days: int) -> pd.DataFrame:
    rows = []
    for week, cutoff, block in week_groups(df, seasons):
        model = fit(df, cutoff, half_life_days)
        m0 = population_home(df, cutoff)
        for game in block.itertuples():
            joint, m2 = predict(model, game.home, game.away)
            result = int(game.hg > game.ag)
            rec = dict(season=game.season, event_id=game.event_id, week_key=week,
                       cutoff_utc=cutoff.isoformat(), kickoff_utc=game.kickoff_utc.isoformat(),
                       home=game.home, away=game.away, hg=int(game.hg), ag=int(game.ag),
                       home_win=result, training_matches=model.training_matches,
                       effective_matches=model.effective_matches,
                       half_life_days=half_life_days,
                       mean_margin=joint.mean_margin, mean_total=joint.mean_total,
                       sd_margin=joint.sd_margin, sd_total=joint.sd_total,
                       margin_total_correlation=joint.correlation)
            for label, probability in (("m0", m0), ("m2", m2)):
                p = np.clip(probability, 1e-12, 1-1e-12)
                rec[f"{label}_p_home"] = probability
                rec[f"{label}_logloss"] = float(-np.log(p if result else 1-p))
                rec[f"{label}_brier"] = float((probability-result)**2)
            rows.append(rec)
    return pd.DataFrame(rows).sort_values("kickoff_utc").reset_index(drop=True)


def interval(frame: pd.DataFrame, reps: int = BOOTSTRAP_REPS) -> dict:
    blocks = frame.assign(delta=frame.m2_logloss-frame.m0_logloss).groupby("week_key").delta.agg(["sum", "count"])
    rng = np.random.default_rng(SEED)
    picks = rng.integers(0, len(blocks), size=(reps, len(blocks)))
    means = blocks["sum"].to_numpy()[picks].sum(axis=1) / blocks["count"].to_numpy()[picks].sum(axis=1)
    return dict(mean=float((frame.m2_logloss-frame.m0_logloss).mean()),
                ci95=[float(np.quantile(means,.025)),float(np.quantile(means,.975))],
                events=len(frame), week_blocks=len(blocks))


def calibration(frame: pd.DataFrame, label: str) -> list[dict]:
    p = frame[f"{label}_p_home"].to_numpy()
    y = frame.home_win.to_numpy()
    rows=[]
    for low in np.arange(0,1,.2):
        selected=(p>=low)&(p<(low+.2 if low<.8 else 1.01))
        rows.append(dict(bin=f"[{low:.1f},{low+.2:.1f})",n=int(selected.sum()),
                         mean_p_home=float(p[selected].mean()) if selected.any() else None,
                         home_win_rate=float(y[selected].mean()) if selected.any() else None))
    return rows


def tune() -> dict:
    df=checked_data()
    lock_path=RUNS/"nbl_tuning_lock.json"
    if lock_path.exists():
        raise RuntimeError("NBL tuning already locked; do not overwrite")
    results={}
    for half_life in HALF_LIFE_GRID:
        frame=forecast(df,TUNING,half_life)
        path=RUNS/f"nbl_tuning_half_life_{half_life}.csv"
        frame.to_csv(path,index=False,float_format="%.12g")
        results[str(half_life)]=dict(n=len(frame),mean_m2_logloss=float(frame.m2_logloss.mean()),
                                     forecast_sha256=sha(path))
    selected=min(HALF_LIFE_GRID,key=lambda h:(results[str(h)]["mean_m2_logloss"],-h))
    lock=dict(stage="TUNING_LOCK",created_utc=datetime.now(timezone.utc).isoformat(),
              model_version="nbl-joint-0.1.0",data_sha256=sha(DATA),
              data_manifest_sha256=sha(DATA_MANIFEST),
              evaluator_sha256=sha(CODE),model_code_sha256=sha(MODEL_CODE),
              tuning_seasons=TUNING,half_life_grid=HALF_LIFE_GRID,
              selected_half_life_days=selected,criterion="minimum mean moneyline log-loss",
              bootstrap_reps=BOOTSTRAP_REPS,seed=SEED,results=results)
    lock_path.write_text(json.dumps(lock,indent=2)+"\n",encoding="utf-8")
    return lock


def holdout() -> dict:
    path=RUNS/"nbl_2025-26_holdout.csv"
    report_path=RUNS/"nbl_2025-26_holdout.json"
    if path.exists() or report_path.exists():
        raise RuntimeError("one-shot NBL holdout already exists")
    lock_path=RUNS/"nbl_tuning_lock.json"
    lock=json.loads(lock_path.read_text(encoding="utf-8"))
    if (sha(DATA)!=lock["data_sha256"] or sha(DATA_MANIFEST)!=lock["data_manifest_sha256"]
            or sha(CODE)!=lock["evaluator_sha256"] or sha(MODEL_CODE)!=lock["model_code_sha256"]):
        raise RuntimeError("NBL data or code changed after tuning lock")
    df=checked_data()
    frame=forecast(df,(HOLDOUT,),lock["selected_half_life_days"])
    frame.to_csv(path,index=False,float_format="%.12g")
    delta=interval(frame)
    report=dict(stage="ONE_SHOT_HOLDOUT",created_utc=datetime.now(timezone.utc).isoformat(),
                holdout=HOLDOUT,n_events=len(frame),week_blocks=frame.week_key.nunique(),
                model_version=lock["model_version"],selected_half_life_days=lock["selected_half_life_days"],
                m0=dict(logloss=float(frame.m0_logloss.mean()),brier=float(frame.m0_brier.mean()),
                        calibration=calibration(frame,"m0")),
                m2=dict(logloss=float(frame.m2_logloss.mean()),brier=float(frame.m2_brier.mean()),
                        calibration=calibration(frame,"m2")),
                m2_minus_m0=delta,
                mean_margin_residual=float(((frame.hg-frame.ag)-frame.mean_margin).mean()),
                mean_total_residual=float(((frame.hg+frame.ag)-frame.mean_total).mean()),
                lane_decision="M2_PASS" if delta["ci95"][1]<0 else "STOP",
                data_sha256=lock["data_sha256"],tuning_lock_sha256=sha(lock_path),
                forecast_sha256=sha(path))
    report_path.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    return report


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("stage",choices=("tune","holdout"))
    args=parser.parse_args()
    print(json.dumps(tune() if args.stage=="tune" else holdout(),indent=2))
