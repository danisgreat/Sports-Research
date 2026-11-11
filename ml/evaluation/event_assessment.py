"""Event-equal ASSESS-100 scorer, outside the frozen legacy forecast-cycle import closure.

Reuses the original strict settlement join, proper scores, calibration and ranking
helpers. The dedicated event path has no calendar minimum and does not modify the
legacy week-based evaluator or invalidate its frozen code identity.
"""
from __future__ import annotations

import math
import numpy as np
import pandas as pd
from scipy import stats

from ml import primary as p
from ml.core import metrics as M
from ml.core.metrics import calibration_fit, iso_week
from ml.evaluation import prospective as P

_grade = P._grade
_ranking = P._ranking


def paired_event_interval(diff, event, week, conf: float = 0.95) -> dict:
    """Equal-weight games, with contracts averaged inside each game; no calendar gate.

    The t interval treats games as independent units. Shared-date/team dependence
    remains an explicit limitation; old registered week-block studies are unchanged.
    """
    frame = pd.DataFrame({"d": np.asarray(diff), "e": np.asarray(event), "w": np.asarray(week)}).dropna()
    frame = frame[np.isfinite(frame.d)]
    if frame.groupby("e").w.nunique().gt(1).any():
        raise p.AdmissionError("one event cannot belong to multiple calendar weeks")
    values = frame.groupby("e", sort=True).d.mean()
    n = len(values)
    mean = float(values.mean()) if n else math.nan
    sd = float(values.std(ddof=1)) if n > 1 else math.nan
    half = float(stats.t.ppf(0.5 + conf / 2, n - 1) * sd / math.sqrt(n)) if n > 1 else math.nan
    status = "NOT_COMPUTABLE" if n < 2 else "BELOW_ZERO" if mean + half < 0 else "ABOVE_ZERO" if mean - half > 0 else "SPANS_ZERO"
    return dict(n_events=n, k_weeks=int(frame.w.nunique()), mean=mean, lo=mean-half, hi=mean+half,
                sd_event=sd, sd_w=math.nan, status=status, analysis_unit="EVENT",
                interval_assumption="INDEPENDENT_EVENTS_SHARED_DATE_TEAM_DEPENDENCE_REQUIRES_AUDIT")


def evaluate(ledger: list[dict], outcomes: pd.DataFrame, champion: str, candidate: str, *, delta: float,
             slope_band=(0.8, 1.25), coverage_tolerance: float = 0.05,
             assessment_unit: str = "EVENT", minimum_events: int | None = None) -> dict:
    """``champion``/``candidate`` are 'model_id:model_version'. ``delta`` is the preregistered Brier improvement."""
    if not math.isfinite(delta) or delta <= 0 or champion == candidate:
        raise p.AdmissionError("distinct model versions and finite positive preregistered effect required")
    if assessment_unit != "EVENT":
        raise p.AdmissionError("event assessor supports EVENT only; use the legacy scorer for registered week studies")
    floor = 100 if minimum_events is None else minimum_events
    if not isinstance(floor, int) or floor <= 0:
        raise p.AdmissionError("positive integer event floor required")
    interval = paired_event_interval
    if not ledger:
        return dict(disposition="INSUFFICIENT_EVIDENCE", reason="no frozen forecasts", pairs=0)
    frame = pd.DataFrame(ledger)
    frame["tag"] = frame.model_id + ":" + frame.model_version
    if frame.duplicated(["tag", "event_id", "contract_key"]).any():
        raise p.AdmissionError("duplicate model/event/contract")
    for _, g in frame.groupby("tag"):
        if any(g[c].nunique() != 1 for c in ("code_sha256", "param_version")):
            raise p.AdmissionError("model version changed source or parameters within prospective cohort")
    eligible = frame[(frame.evidence_status == "PRE_START_VERIFIED") &
                     (frame.issued_at.map(p.clock) < frame.scheduled_start.map(p.clock))]
    graded = _grade(eligible, outcomes)
    champ, cand = graded[graded.tag == champion], graded[graded.tag == candidate]
    keys = ["event_id", "contract_key"]
    union = len(pd.concat([champ[keys], cand[keys]]).drop_duplicates())
    pair = champ.merge(cand, on=keys, suffixes=("_c", "_k"))
    for column in ("competition", "endpoint", "family", "side", "line", "scheduled_start"):
        if (pair[column+"_c"] != pair[column+"_k"]).any():
            raise p.AdmissionError("identical-contract comparison mismatch: " + column)
    pair = pair[pair.y_c.notna()]
    if pair.empty:
        return dict(disposition="INSUFFICIENT_EVIDENCE", reason="no settled identical pre-start contracts", pairs=0)
    pair["week"] = iso_week(pair.scheduled_start_c.map(lambda t: p.clock(t).tz_localize(None)))
    pc, pk, y = pair.p_c.astype(float), pair.p_k.astype(float), pair.y_c.astype(float)
    # One shared scoring implementation (ml.core.metrics): no hidden probability floor anywhere (SCORING §3).
    pair["d_brier"] = M.brier(pk, y) - M.brier(pc, y)
    iv = interval(pair.d_brier, pair.event_id, pair.week)
    lk, lc = M.log_loss(pk, y), M.log_loss(pc, y)
    with np.errstate(invalid="ignore"):
        pair["d_log_loss"] = lk - lc
    log_iv = _log_interval(pair, lk, lc, assessment_unit=assessment_unit)
    need = P.weeks_needed(iv["sd_event"], delta)
    per = {}
    for tag, rows in ((champion, champ), (candidate, cand)):
        coverage_rows = rows[rows.y.notna()]
        # Both probability, loss and calibration summaries use the very same paired rows.
        rows = coverage_rows.merge(pair[keys], on=keys, how="inner", validate="one_to_one")
        q = rows.p.astype(float)
        fit = calibration_fit(q, rows.y)
        per[tag] = dict(rows=len(rows), events=rows.event_id.nunique(), coverage=len(coverage_rows) / union if union else math.nan,
                        brier=float(M.brier(q, rows.y.astype(float)).mean()),
                        log_loss=float(M.log_loss(q, rows.y.astype(float)).mean()),
                        slope=fit["slope"], intercept=fit["intercept"], **_ranking(rows))
    breakdown = []
    for by in ("competition_c", "family_c", "endpoint_c"):
        for value, g in pair.groupby(by):
            biv = interval(g.d_brier, g.event_id, g.week)
            breakdown.append(dict(dimension=by[:-2], value=value, contracts=len(g), events=g.event_id.nunique(),
                                  mean_d_brier=biv["mean"], k_weeks=biv["k_weeks"], status=biv["status"]))
    unsettled = graded.y.isna().mean()
    c, k = per[champion], per[candidate]
    if unsettled > 0.2:
        disposition, reason = "DATA_REPAIR_REQUIRED", f"{unsettled:.0%} of eligible rows unsettled"
    elif iv["n_events"] < floor:
        disposition, reason = "INSUFFICIENT_EVIDENCE", f"{iv['n_events']} paired games; minimum {floor}"
    elif iv["status"] == "BELOW_ZERO" and iv["mean"] <= -delta:
        # PROMO-v2: the declared minimum improvement itself, never a fraction of it (review 2026-11-08: 0.0064 passed a 0.01 rule).
        guard = (slope_band[0] <= k["slope"] <= slope_band[1]) and k["coverage"] >= c["coverage"] - coverage_tolerance
        disposition = "PROMOTION_ELIGIBLE" if guard else "CALIBRATION_STUDY"
        reason = "candidate better on paired Brier" + ("" if guard else "; calibration/coverage guard failed")
    elif iv["status"] == "ABOVE_ZERO":
        disposition, reason = "NO_CHANGE", "candidate worse on paired Brier"
    else:
        disposition, reason = "NO_CHANGE", "no resolvable difference at the registered effect size"
    return dict(disposition=disposition, reason=reason, pairs=len(pair), interval=iv, log_loss_interval=log_iv,
                weeks_needed=None, events_needed=need,
                assessment_unit=assessment_unit,
                models=per, unsettled_share=float(unsettled), breakdown=pd.DataFrame(breakdown))


def _log_interval(pair: pd.DataFrame, lk, lc, *, assessment_unit="EVENT") -> dict:
    """Paired log-loss interval. A wrong literal 0 or 1 is an infinite loss (SCORING §3): reported, never clipped or dropped."""
    inf_k, inf_c = int(np.isinf(lk).sum()), int(np.isinf(lc).sum())
    if inf_k or inf_c:
        mean = math.inf if inf_k and not inf_c else -math.inf if inf_c and not inf_k else math.nan
        status = "ABOVE_ZERO" if mean == math.inf else "BELOW_ZERO" if mean == -math.inf else "NOT_COMPUTABLE"
        return {"k_weeks": int(pair.week.nunique()), "n_events": int(pair.event_id.nunique()), "mean": mean, "lo": mean, "hi": mean,
                "sd_w": math.nan, "status": status, "infinite_candidate": inf_k, "infinite_champion": inf_c}
    interval = paired_event_interval
    return dict(interval(pair.d_log_loss, pair.event_id, pair.week), infinite_candidate=0, infinite_champion=0)
