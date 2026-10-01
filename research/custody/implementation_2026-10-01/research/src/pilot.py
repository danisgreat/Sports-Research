"""Prospective event-level composite scores; no scoring without a frozen lock."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
import pandas as pd

from .load import ROOT
from .emit_card import _outcome
from .sports.base import Contract


def _probabilities(rows: pd.DataFrame, prefix: str):
    by = {(r.market, r.selection, str(r.line)): float(getattr(r, prefix)) for r in rows.itertuples()}
    def get(market, side, line=""):
        return by[(market, side, line)]
    one = np.array([get("1X2",side) for side in ("HOME","DRAW","AWAY")])
    total = get("TOTAL","OVER","2.5")
    btts = get("BTTS","YES")
    if len(rows) != 7 or abs(one.sum()-1)>1e-6 or abs(total+get("TOTAL","UNDER","2.5")-1)>1e-6 or abs(btts+get("BTTS","NO")-1)>1e-6:
        raise ValueError("incomplete or incoherent fixed contract families")
    if (one<=0).any() or (one>=1).any() or not (0<total<1) or not (0<btts<1):
        raise ValueError("invalid forecast probability")
    return one,total,btts


def _score(one, total, btts, home: int, away: int):
    actual = 0 if home>away else 1 if home==away else 2
    over = float(home+away>2)
    yes = float(home>0 and away>0)
    logloss = (-np.log(one[actual]) - (over*np.log(total)+(1-over)*np.log(1-total))
               - (yes*np.log(btts)+(1-yes)*np.log(1-btts)))/3
    brier = (np.sum((one-np.eye(3)[actual])**2)/2 + (total-over)**2 + (btts-yes)**2)/3
    return float(logloss),float(brier)


def score_events(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path, dtype={"event_id":str,"line":str}).fillna({"line":""})
    out=[]
    for (lane,event_id),g in frame.groupby(["lane","event_id"]):
        if lane != "EPL":
            raise ValueError("pilot v1 scores EPL contract families only; other lanes need a versioned score contract")
        if g.lane_status.nunique()!=1 or g.lane_status.iloc[0]!="VALIDATED":
            continue
        if g.shadow.nunique()!=1 or str(g.shadow.iloc[0]).lower() != "false":
            continue
        if g.performance_eligible.nunique()!=1 or str(g.performance_eligible.iloc[0]).lower() != "true":
            continue
        if g["result"].isna().any() or g.score_home.isna().any() or g.score_away.isna().any():
            continue
        if any(g[c].nunique()!=1 for c in ("issued_utc","actual_start_utc","data_cutoff_utc","score_home","score_away","adjustment_type")):
            raise ValueError(f"event {event_id} has conflicting freeze or result")
        cutoff,issue,start = [pd.Timestamp(g[c].iloc[0]) for c in ("data_cutoff_utc","issued_utc","actual_start_utc")]
        if not cutoff <= issue < start:
            raise ValueError(f"event {event_id} not prospectively issued")
        h,a=int(g.score_home.iloc[0]),int(g.score_away.iloc[0])
        for row in g.itertuples():
            contract=Contract(str(event_id),row.market,row.selection,
                              None if row.line=="" else float(row.line),row.endpoint)
            win,push=_outcome(np.array([h]),np.array([a]),contract)
            expected="W" if win[0] else "P" if push[0] else "L"
            if row.result!=expected:
                raise ValueError(f"event {event_id} has a wrong settlement grade")
        model = _score(*_probabilities(g,"p_model"),h,a)
        card = _score(*_probabilities(g,"p_card"),h,a)
        out.append(dict(lane=lane,event_id=event_id,week=str(start.isocalendar().year)+"-W"+str(start.isocalendar().week).zfill(2),
                        adjusted=g.adjustment_type.iloc[0]!="NONE",model_logloss=model[0],card_logloss=card[0],
                        model_brier=model[1],card_brier=card[1]))
    return pd.DataFrame(out)


def paired_bootstrap(events: pd.DataFrame, weights: dict[str,float], metric: str, seed: int, reps: int = 10000):
    rng=np.random.default_rng(seed)
    estimates=[]
    for lane,weight in weights.items():
        subset=events.loc[events.lane==lane].copy()
        if subset.empty:
            raise ValueError(f"missing declared lane {lane}")
        grouped=(subset.card_logloss-subset.model_logloss if metric=="logloss" else subset.card_brier-subset.model_brier).groupby(subset.week).agg(["sum","count"])
        sums,counts=grouped["sum"].to_numpy(),grouped["count"].to_numpy()
        pick=rng.integers(0,len(sums),size=(reps,len(sums)))
        estimates.append((weight, float(sums.sum()/counts.sum()), sums[pick].sum(axis=1)/counts[pick].sum(axis=1)))
    mean=sum(w*m for w,m,_ in estimates)
    boot=sum(w*b for w,_,b in estimates)
    return dict(mean=float(mean),ci95=[float(np.quantile(boot,.025)),float(np.quantile(boot,.975))])


def decision(path: Path, lock_path: Path) -> dict:
    lock=json.loads(lock_path.read_text(encoding="utf-8"))
    if lock.get("status")!="FROZEN" or not lock.get("weights") or not lock.get("target_adjusted_events"):
        raise RuntimeError("pilot sample, lane weights and gate must be frozen before scoring")
    if abs(sum(lock["weights"].values())-1)>1e-9:
        raise ValueError("weights do not sum to one")
    events=score_events(path)
    adjusted=events.loc[events.adjusted]
    target=int(lock["target_adjusted_events"])
    if len(adjusted)>target:
        adjusted=adjusted.iloc[:target]
    summary=dict(eligible_events=len(events),adjusted_events=len(adjusted),target=target,
                 all_events_logloss=paired_bootstrap(events,lock["weights"],"logloss",lock["seed"]) if len(events) else None)
    interim=int(lock.get("futility_look_events") or -1)
    if interim <= 0 or interim >= target:
        raise ValueError("one fixed futility look before final sample is required")
    if len(adjusted)<interim:
        summary["verdict"]="WAIT_FOR_INTERIM"
        return summary
    if interim<len(adjusted)<target:
        summary["verdict"]="WAIT_FOR_FINAL_AFTER_SINGLE_INTERIM"
        return summary
    log=paired_bootstrap(adjusted,lock["weights"],"logloss",lock["seed"])
    brier=paired_bootstrap(adjusted,lock["weights"],"brier",lock["seed"])
    summary.update(adjusted_logloss=log,adjusted_brier=brier)
    if len(adjusted)==interim:
        summary["verdict"]="FUTILITY_STOP" if brier["ci95"][0]>-lock["mwi_brier"] else "WAIT_FOR_FINAL"
    else:
        summary["verdict"]="KEEP_ADJUSTMENTS" if log["ci95"][1]<0 and brier["ci95"][1]<-lock["mwi_brier"] else "DEFAULT_TO_MODEL"
    return summary


if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("ledger",type=Path)
    parser.add_argument("lock",type=Path)
    a=parser.parse_args()
    print(json.dumps(decision(a.ledger,a.lock),indent=2))
