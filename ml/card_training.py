"""Every settled card record ingested, admitted and used in a training run (CARD-TRAIN-v1).

Owner instruction, 15 November 2026 (CR-2026.11.15-R4): all the records and settled game logs must be
ingested, admitted and used in an actual training run.

    python -m ml card-training run --out research/card_training/<RUN_ID>
    python -m ml card-training verify --run research/card_training/<RUN_ID>

1. INGEST. The effective card history (``ml.evaluation.card_history.build_rows``): every committed combined
   log, the rank log, every mini-import inventory and every validated settlement revision, P-001 onward.
   One row per settled contract row, original ranks and grades retained. Input files are hash-bound.
2. ADMIT. Each row gets one admission status and, when excluded, one reason:
     OUTCOME_AND_CALIBRATION  decisive (WIN/LOSS), dated, stated probability in (0,1)
     OUTCOME_ONLY             decisive and dated, no usable stated probability (reason NO_STATED_P)
     EXCLUDED                 NOT_DECISIVE:<grade> (push, void, unresolved, unattainable, conflict) or UNDATED
3. TRAIN, walk-forward by ISO week. For each week, models are fitted only on rows issued before that week's
   Monday whose outcome was available by then, and scored on that week's rows. Nothing sees its own week.
     CALIBRATION  IDENTITY (the stated p as written), PLATT (logistic recalibration shrunk to identity) and
                  SPORT_PLATT (per-sport Platt shrunk to the pooled fit): one calibrator per sport family,
                  never per league (league-agnostic rule).
     OUTCOME      L2-regularised logistic regression on sport, proposition family, rank, contract direction
                  (over/under/other) and logit(stated p) with a missing indicator; baseline = the training
                  base rate.
   Scores: Brier and log loss per row; paired differences averaged within card, then a t-interval over cards
   (rows in one card are dependent).

Evidence class HISTORICAL_OUTCOME_EXPOSED_STUDY. Timing is approximate: issued_at is the card date at 00:00 UTC
and the outcome is treated as available two days later (per-row settlement times are not recorded in the
history). ML-SEP-v1: nothing here is applied to a card, pick, probability or rank; a fitted model becomes a
reference only through ML_PROMOTIONS.csv and the owner's decision.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
import secrets
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import optimize, stats

VERSION = "CARD-TRAIN-v1"
EVIDENCE_CLASS = "HISTORICAL_OUTCOME_EXPOSED_STUDY"
MIN_CAL_TRAIN = 100
MIN_OUTCOME_TRAIN = 200
OUTCOME_LAG = pd.Timedelta(days=2)
ROW_FIELDS = ("row_id", "card", "rank", "date", "week", "era", "sport", "family", "direction", "contract", "p", "grade",
              "y", "probability_role", "cohort", "source", "admission", "reason")
PRED_FIELDS = ("row_id", "card", "week", "sport", "family", "y", "p_stated", "cal_identity", "cal_platt", "cal_sport_platt",
               "outcome_base_rate", "outcome_model", "cal_train_rows", "outcome_train_rows")


def _csv(fields, rows) -> bytes:
    out = io.StringIO(newline="")
    w = csv.DictWriter(out, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return out.getvalue().encode("utf-8")


def _digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def direction(contract: str) -> str:
    text = f" {str(contract).lower()} "
    if " over " in text or text.strip().startswith("over"):
        return "OVER"
    if " under " in text or text.strip().startswith("under"):
        return "UNDER"
    return "OTHER"


def admit(rows: pd.DataFrame) -> pd.DataFrame:
    """One admission status and reason per ingested row (pure function of the effective history)."""
    out = []
    for i, r in enumerate(rows.itertuples(index=False), 1):
        try:
            prob = float(r.p)
        except (TypeError, ValueError):
            prob = math.nan
        grade = str(r.grade)
        dated = bool(str(r.date).strip()) and str(r.era) != "UNDATED"
        if grade not in ("WIN", "LOSS"):
            status, reason = "EXCLUDED", "NOT_DECISIVE:" + (grade or "BLANK")
        elif not dated:
            status, reason = "EXCLUDED", "UNDATED"
        elif math.isfinite(prob) and 0 < prob < 1:
            status, reason = "OUTCOME_AND_CALIBRATION", ""
        else:
            status, reason = "OUTCOME_ONLY", "NO_STATED_P"
        out.append(dict(row_id=f"R{i:05d}", card=r.card, rank=r.rank, date=r.date, week=r.week, era=r.era, sport=r.sport,
                        family=r.family, direction=direction(r.contract), contract=r.contract,
                        p="" if not math.isfinite(prob) else repr(prob), grade=grade,
                        y="1" if grade == "WIN" else "0" if grade == "LOSS" else "", probability_role=r.probability_role,
                        cohort=r.cohort, source=r.source, admission=status, reason=reason))
    return pd.DataFrame(out, columns=list(ROW_FIELDS))


def _logit(p):
    p = np.clip(np.asarray(p, float), 1e-6, 1 - 1e-6)
    return np.log(p / (1 - p))


def _sigmoid(z):
    return 1 / (1 + np.exp(-z))


def fit_logistic(X: np.ndarray, y: np.ndarray, *, l2: float = 1.0, centre: np.ndarray | None = None) -> np.ndarray:
    """MAP logistic regression with a Gaussian prior (precision ``l2``) centred on ``centre`` (default zero)."""
    centre = np.zeros(X.shape[1]) if centre is None else np.asarray(centre, float)

    def nll(beta):
        z = X @ beta
        return np.sum(np.logaddexp(0, z) - y * z) + l2 * np.sum((beta - centre) ** 2) / 2

    def grad(beta):
        return X.T @ (_sigmoid(X @ beta) - y) + l2 * (beta - centre)

    return optimize.minimize(nll, centre.copy(), jac=grad, method="L-BFGS-B").x


def _platt(p, y, centre=(0.0, 1.0)):
    X = np.column_stack([np.ones(len(p)), _logit(p)])
    return fit_logistic(X, np.asarray(y, float), centre=np.asarray(centre, float))


def _apply_platt(beta, p):
    return _sigmoid(beta[0] + beta[1] * _logit(p))


def _design(frame: pd.DataFrame, levels: dict) -> np.ndarray:
    cols = [np.ones(len(frame))]
    for name, values in levels.items():
        for v in values[1:]:  # first level is the reference
            cols.append((frame[name].astype(str) == v).to_numpy(float))
    has_p = frame["p"].astype(str) != ""
    lp = np.where(has_p, _logit(pd.to_numeric(frame["p"], errors="coerce").fillna(0.5)), 0.0)
    cols += [lp, has_p.to_numpy(float)]
    return np.column_stack(cols)


def _rank_bucket(rank) -> str:
    try:
        r = int(float(rank))
    except (TypeError, ValueError):
        return "OTHER"
    return "1" if r == 1 else "2" if r == 2 else "3+"


def walk_forward(admitted: pd.DataFrame) -> pd.DataFrame:
    """Weekly refits on earlier rows only; returns one prediction row per decisive dated row once training suffices."""
    d = admitted[admitted.admission != "EXCLUDED"].copy()
    d["issued_at"] = pd.to_datetime(d.date, utc=True)
    d["available_at"] = d.issued_at + OUTCOME_LAG
    d["rank_bucket"] = d["rank"].map(_rank_bucket)
    d["yv"] = d.y.astype(float)
    d["monday"] = d.issued_at.dt.normalize() - pd.to_timedelta(d.issued_at.dt.weekday, unit="D")
    out = []
    for monday in sorted(d.monday.unique()):
        train = d[(d.issued_at < monday) & (d.available_at <= monday)]
        test = d[d.monday == monday]
        if len(train) < MIN_OUTCOME_TRAIN:
            continue
        levels = {k: sorted(train[k].astype(str).unique()) for k in ("sport", "family", "rank_bucket", "direction")}
        known = test.copy()
        for k, values in levels.items():  # unseen categories fall to the reference level, never invented
            known[k] = known[k].where(known[k].astype(str).isin(values), values[0])
        beta = fit_logistic(_design(train, levels), train.yv.to_numpy())
        outcome = _sigmoid(_design(known, levels) @ beta)
        base = float(train.yv.mean())
        ctrain = train[train.admission == "OUTCOME_AND_CALIBRATION"]
        cal_ok = len(ctrain) >= MIN_CAL_TRAIN
        if cal_ok:
            cp = ctrain.p.astype(float).to_numpy()
            pooled = _platt(cp, ctrain.yv.to_numpy())
            by_sport = {s: _platt(g.p.astype(float).to_numpy(), g.yv.to_numpy(), centre=pooled)
                        for s, g in ctrain.groupby("sport")}
        for (_, r), o in zip(test.iterrows(), outcome):
            has = r.admission == "OUTCOME_AND_CALIBRATION"
            pv = float(r.p) if has else math.nan
            row = dict(row_id=r.row_id, card=r.card, week=r.week, sport=r.sport, family=r.family, y=int(r.yv),
                       p_stated=repr(pv) if has else "", cal_identity="", cal_platt="", cal_sport_platt="",
                       outcome_base_rate=repr(base), outcome_model=repr(float(o)),
                       cal_train_rows=len(ctrain), outcome_train_rows=len(train))
            if has and cal_ok:
                row["cal_identity"] = repr(pv)
                row["cal_platt"] = repr(float(_apply_platt(pooled, pv)))
                row["cal_sport_platt"] = repr(float(_apply_platt(by_sport.get(r.sport, pooled), pv)))
            out.append(row)
    return pd.DataFrame(out, columns=list(PRED_FIELDS))


def _scores(pred: pd.DataFrame, model: str, baseline: str) -> dict:
    sub = pred[(pred[model] != "") & (pred[baseline] != "")]
    if sub.empty:
        return dict(model=model, baseline=baseline, rows=0, cards=0)
    y = sub.y.astype(float).to_numpy()
    pm, pb = sub[model].astype(float).to_numpy(), sub[baseline].astype(float).to_numpy()
    bm, bb = (pm - y) ** 2, (pb - y) ** 2
    lm = -(y * np.log(pm) + (1 - y) * np.log(1 - pm))
    lb = -(y * np.log(pb) + (1 - y) * np.log(1 - pb))
    per_card = pd.DataFrame(dict(card=sub.card.to_numpy(), d=bm - bb)).groupby("card").d.mean()
    k = len(per_card)
    mean = float(per_card.mean())
    se = float(per_card.std(ddof=1) / math.sqrt(k)) if k > 1 else math.nan
    t = stats.t.ppf(0.975, k - 1) if k > 1 else math.nan
    return dict(model=model, baseline=baseline, rows=len(sub), cards=k, weeks=sub.week.nunique(),
                model_brier=float(bm.mean()), baseline_brier=float(bb.mean()),
                model_log_loss=float(lm.mean()), baseline_log_loss=float(lb.mean()),
                card_mean_brier_difference=mean, interval_low=mean - t * se if k > 1 else math.nan,
                interval_high=mean + t * se if k > 1 else math.nan)


SCORE_PAIRS = (("cal_platt", "cal_identity"), ("cal_sport_platt", "cal_identity"), ("outcome_model", "outcome_base_rate"),
               ("outcome_model", "p_stated"), ("cal_identity", "outcome_base_rate"))
SCORE_FIELDS = ("model", "baseline", "rows", "cards", "weeks", "model_brier", "baseline_brier", "model_log_loss",
                "baseline_log_loss", "card_mean_brier_difference", "interval_low", "interval_high")


def run(out: Path) -> dict:
    from ml import primary as p
    from ml.evaluation import card_history as ch, effective_settlement as es
    out = Path(out)
    if out.exists():
        raise FileExistsError(out)
    code = p.source_hash()
    inventories, logs = ch.import_inventories(), ch.combined_logs()
    stale = es.unmatched_revisions(ch.ROOT)
    if stale:
        raise ValueError(f"settlement revisions match no imported row: {stale}")
    inputs = ch.reporting_inputs(ch.RANK_LOG, inventories=inventories, logs=logs)
    hashes = {f: _digest(f.read_bytes()) if f.exists() else "MISSING" for f in inputs}
    history, _ = ch.build_rows(ch.RANK_LOG, inventories=inventories, logs=logs)
    rows = admit(history)
    pred = walk_forward(rows)
    if code != p.source_hash() or any((_digest(f.read_bytes()) if f.exists() else "MISSING") != h for f, h in hashes.items()):
        raise ValueError("inputs or generating code changed during the run; rerun from a stable snapshot")
    scores = [_scores(pred, m, b) for m, b in SCORE_PAIRS]
    counts = rows.groupby(["admission", "reason"]).size().reset_index(name="rows").to_dict("records")
    receipt = dict(version=VERSION, evidence_class=EVIDENCE_CLASS, deployment="NONE_STUDY_ONLY (ML-SEP-v1)",
                   cards=int(rows.card.nunique()), ingested_rows=len(rows),
                   admitted_outcome_rows=int((rows.admission != "EXCLUDED").sum()),
                   admitted_calibration_rows=int((rows.admission == "OUTCOME_AND_CALIBRATION").sum()),
                   excluded_rows=int((rows.admission == "EXCLUDED").sum()), scored_rows=len(pred),
                   rows_sha256=_digest(_csv(ROW_FIELDS, rows.to_dict("records"))),
                   predictions_sha256=_digest(_csv(PRED_FIELDS, pred.to_dict("records"))),
                   code_sha256=code, repository_head=p.repository_head(), generated_at=datetime.now(timezone.utc).isoformat())
    tmp = out.parent / ("." + out.name + "." + secrets.token_hex(6))
    tmp.mkdir(parents=True)
    (tmp / "ROWS.csv").write_bytes(_csv(ROW_FIELDS, rows.to_dict("records")))
    (tmp / "PREDICTIONS.csv").write_bytes(_csv(PRED_FIELDS, pred.to_dict("records")))
    (tmp / "SCORES.csv").write_bytes(_csv(SCORE_FIELDS, scores))
    (tmp / "ADMISSION.csv").write_bytes(_csv(("admission", "reason", "rows"), counts))
    (tmp / "INPUTS.csv").write_bytes(_csv(("path", "sha256"), [dict(path=f.relative_to(ch.ROOT).as_posix() if f.is_relative_to(ch.ROOT) else str(f), sha256=h)
                                                               for f, h in hashes.items()]))
    (tmp / "RECEIPT.csv").write_bytes(_csv(tuple(receipt), [receipt]))
    tmp.rename(out)
    return dict(receipt=receipt, scores=scores, counts=counts)


def verify(folder: Path) -> dict:
    """Rebuild admissions and walk-forward predictions from the recorded rows; require identical bytes."""
    folder = Path(folder)
    with (folder / "RECEIPT.csv").open(encoding="utf-8", newline="") as f:
        receipt = next(csv.DictReader(f))
    rows_raw = (folder / "ROWS.csv").read_bytes()
    if _digest(rows_raw) != receipt["rows_sha256"]:
        raise ValueError("ROWS.csv differs from its receipt")
    rows = pd.read_csv(folder / "ROWS.csv", dtype=str, keep_default_na=False)
    pred = walk_forward(rows)
    if _digest(_csv(PRED_FIELDS, pred.to_dict("records"))) != receipt["predictions_sha256"]:
        raise ValueError("walk-forward predictions do not rebuild identically")
    return receipt


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    r = sub.add_parser("run")
    r.add_argument("--out", type=Path, required=True)
    v = sub.add_parser("verify")
    v.add_argument("--run", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.command == "run":
        res = run(args.out)
        rec = res["receipt"]
        print(f"{rec['cards']} cards, {rec['ingested_rows']} rows ingested; {rec['admitted_outcome_rows']} admitted "
              f"({rec['admitted_calibration_rows']} with stated p); {rec['scored_rows']} scored walk-forward -> {args.out}")
        for s in res["scores"]:
            if s["rows"]:
                print(f"  {s['model']} vs {s['baseline']}: Brier {s['model_brier']:.4f} vs {s['baseline_brier']:.4f} "
                      f"on {s['rows']} rows / {s['cards']} cards; card-mean diff {s['card_mean_brier_difference']:+.4f} "
                      f"[{s['interval_low']:+.4f}, {s['interval_high']:+.4f}]")
    else:
        rec = verify(args.run)
        print(f"verified {args.run}: {rec['scored_rows']} predictions rebuild identically")


if __name__ == "__main__":
    main()
