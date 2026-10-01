"""Chronological, family-specific development experiments; never live admission.

The opened historical holdouts are development data for this new protocol.
All candidates use one coherent score distribution per event. Calibration is
diagnostic: no calibrator is fitted on the observations it is scored against.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import norm, poisson

from .dixon_coles import fit_dc, probabilities, predict, score_matrix
from .evaluate import groups
from .features import _past
from .load import PROCESSED, ROOT, sha
from .nbl_evaluate import checked_data, week_groups
from .nbl_model import fit as fit_nbl, population_home, predict as predict_nbl

RUN = ROOT / "runs/implementation_2026-10-01"
SEED = 20261001


def wilson(successes: int, n: int) -> list[float] | None:
    if n == 0:
        return None
    z = norm.ppf(.975)
    p = successes / n
    center = (p + z*z/(2*n))/(1+z*z/n)
    radius = z*np.sqrt(p*(1-p)/n + z*z/(4*n*n))/(1+z*z/n)
    return [float(max(0, center-radius)), float(min(1, center+radius))]


def reliability(p, y) -> dict:
    p, y = np.asarray(p, dtype=float), np.asarray(y, dtype=float)
    if len(p) == 0 or not np.isfinite(p).all() or ((p <= 0)|(p >= 1)).any():
        raise ValueError("finite nondegenerate probability observations required")
    bins = []
    for i in range(5):
        selected = (p >= i/5) & (p < (i+1)/5 if i < 4 else p <= 1)
        n = int(selected.sum())
        wins = int(y[selected].sum())
        bins.append(dict(bin=[i/5, (i+1)/5], n=n,
                         mean_p=float(p[selected].mean()) if n else None,
                         observed_rate=wins/n if n else None,
                         observed_rate_ci95=wilson(wins, n)))
    x = np.log(p/(1-p))
    def loss(v):
        eta = v[0] + v[1]*x
        return float(np.logaddexp(0, eta).sum() - np.dot(y, eta))
    fitted = minimize(loss, [0., 1.], method="BFGS") if len(np.unique(y)) == 2 else None
    return dict(bins=bins, intercept=float(fitted.x[0]) if fitted and fitted.success else None,
                slope=float(fitted.x[1]) if fitted and fitted.success else None,
                coefficient_status="DESCRIPTIVE_IN_SAMPLE_NOT_A_CALIBRATOR",
                calibration_fit_success=bool(fitted and fitted.success))


def paired(frame, candidate, baseline, reps=10000) -> dict:
    a = frame.loc[frame.model == candidate, ["event_id", "week", "logloss"]]
    b = frame.loc[frame.model == baseline, ["event_id", "logloss"]]
    merged = a.merge(b, on="event_id", validate="one_to_one", suffixes=("_candidate", "_baseline"))
    if len(merged) != len(a) or len(merged) != len(b) or merged.empty:
        raise ValueError("comparisons require identical event populations")
    blocks = merged.assign(delta=merged.logloss_candidate-merged.logloss_baseline).groupby("week").delta.agg(["sum", "count"])
    rng = np.random.default_rng(SEED)
    picks = rng.integers(0, len(blocks), size=(reps, len(blocks)))
    boot = blocks["sum"].to_numpy()[picks].sum(axis=1)/blocks["count"].to_numpy()[picks].sum(axis=1)
    return dict(events=len(merged), blocks=len(blocks), mean=float((merged.logloss_candidate-merged.logloss_baseline).mean()),
                ci95=np.quantile(boot, [.025, .975]).tolist())


def tb1_matrix(df, season, cutoff, home, away):
    past = _past(df, cutoff)
    current = past.loc[past.season == season]
    year = int(season[:4])-1
    previous = past.loc[past.season == f"{year}-{str(year+1)[-2:]}"]
    if len(previous) != 380:
        raise ValueError("complete prior season required")
    ref = current if len(current) else previous
    lm = float((ref.hg.sum()+ref.ag.sum())/(2*len(ref)))
    def rating(name):
        h, a = current.loc[current.home == name], current.loc[current.away == name]
        n = len(h)+len(a)
        return ((h.hg.sum()+a.ag.sum()+2*lm)/(n+2), (h.ag.sum()+a.hg.sum()+2*lm)/(n+2))
    oh, dh = rating(home); oa, da = rating(away)
    total = (oh+da+oa+dh)/2
    margin = ((oh-dh)-(oa-da))/2 + float((previous.hg-previous.ag).mean())
    return score_matrix(float((total+margin)/2), float((total-margin)/2))[0]


def empirical_matrix(df, cutoff):
    past = _past(df, cutoff)
    if past.empty or (past[["hg", "ag"]] > 20).any().any():
        raise ValueError("invalid empirical score population")
    prior, _ = score_matrix(float(past.hg.mean()), float(past.ag.mean()))
    counts = np.zeros_like(prior)
    np.add.at(counts, (past.hg.to_numpy(dtype=int), past.ag.to_numpy(dtype=int)), 1)
    return (counts+prior)/(len(past)+1)


def family_rows(meta, model_name, matrix, hg, ag):
    p = probabilities(matrix)
    outcome = 0 if hg > ag else 1 if hg == ag else 2
    families = {"1X2": ([p[k] for k in ("H", "D", "A")], outcome),
                "TOTAL_2_5": ([p["O2.5"], p["U2.5"]], 0 if hg+ag > 2 else 1),
                "BTTS": ([p["BTTS_Y"], p["BTTS_N"]], 0 if hg > 0 and ag > 0 else 1)}
    output = []
    for family, (ps, actual) in families.items():
        vector = np.asarray(ps)
        if not np.isfinite(vector).all() or (vector <= 0).any() or abs(vector.sum()-1) > 1e-9:
            raise ValueError("incoherent or degenerate family probability")
        output.append(dict(**meta, model=model_name, family=family, outcome=actual,
                           probabilities=json.dumps(ps), logloss=float(-np.log(vector[actual])),
                           brier=float(np.square(vector-np.eye(len(ps))[actual]).sum()/(2 if len(ps)==3 else 2))))
    return output


def epl_forecasts(df, seasons):
    rows = []
    for week, cutoff, block in groups(df, tuple(seasons)):
        dc = fit_dc(df, cutoff, .003)
        population = empirical_matrix(df, cutoff)
        for game in block.itertuples():
            _, m2, _ = predict(dc, game.home, game.away)
            m1 = tb1_matrix(df, game.season, cutoff, game.home, game.away)
            meta = dict(lane="EPL", season=game.season, week=week,
                        event_id=f"EPL:{game.season}:{game.home}:{game.away}",
                        home=game.home, away=game.away, cutoff_utc=cutoff.isoformat(),
                        kickoff_utc=game.kickoff_utc.isoformat())
            for label, matrix in (("population", population), ("TB1-MD", m1), ("Dixon-Coles", m2),
                                  ("coherent_DC_TB1_mixture_0.75", .75*m2+.25*m1),
                                  ("coherent_DC_TB1_mixture_0.5", .5*m2+.5*m1)):
                rows.extend(family_rows(meta, label, matrix, int(game.hg), int(game.ag)))
    return pd.DataFrame(rows)


def elo_probability(df, cutoff, home, away):
    past = df.loc[df.kickoff_utc < cutoff].sort_values(["kickoff_utc", "event_id"])
    ratings = {}
    for game in past.itertuples():
        rh, ra = ratings.get(game.home, 1500.), ratings.get(game.away, 1500.)
        expected = 1/(1+10**(-(rh+70-ra)/400))
        update = 20*(int(game.hg > game.ag)-expected)
        ratings[game.home], ratings[game.away] = rh+update, ra-update
    if home not in ratings or away not in ratings:
        raise ValueError("Elo team has no observed history")
    return float(1/(1+10**(-(ratings[home]+70-ratings[away])/400)))


def nbl_forecasts(df, seasons):
    rows, prior_residuals = [], []
    for week, cutoff, block in week_groups(df, tuple(seasons)):
        model = fit_nbl(df, cutoff, 180)
        population = population_home(df, cutoff)
        residuals = np.asarray(prior_residuals)
        scale = float(np.sqrt(np.mean(residuals**2))) if len(residuals) >= 100 else None
        pending = []
        for game in block.itertuples():
            joint, m2 = predict_nbl(model, game.home, game.away)
            label = int(game.hg > game.ag)
            candidates = {"population": population, "Elo_fixed_K20_home70": elo_probability(df, cutoff, game.home, game.away),
                          "joint_score_model": m2}
            # OOF width uses only errors from prior blocks; early observations
            # explicitly retain the original width, rather than invent history.
            candidates["joint_with_chronological_residual_variance"] = float(norm.cdf(joint.mean_margin/(scale or joint.sd_margin)))
            for name, p in candidates.items():
                if not 0 < p < 1:
                    raise ValueError("degenerate candidate probability")
                rows.append(dict(lane="NBL", season=game.season, week=week, event_id=str(game.event_id),
                                 home=game.home, away=game.away, cutoff_utc=cutoff.isoformat(),
                                 kickoff_utc=game.kickoff_utc.isoformat(), model=name, family="ML", outcome=1-label,
                                 probabilities=json.dumps([p, 1-p]), logloss=float(-np.log(p if label else 1-p)),
                                 brier=float((p-label)**2), oof_width_status="PRIOR_BLOCK_RESIDUALS" if scale else "WARMUP_ORIGINAL_WIDTH",
                                 margin_mean=joint.mean_margin, margin_sd=(scale or joint.sd_margin)))
            pending.append(float((game.hg-game.ag)-joint.mean_margin))
        prior_residuals.extend(pending)
    return pd.DataFrame(rows)


def summarize(frame, protocol):
    report = dict(status="CHRONOLOGICAL_DEVELOPMENT_ONLY", live_admission=False,
                  note="Opened historical holdouts are not untouched validation for these changes.", families={})
    for (lane, family), part in frame.groupby(["lane", "family"]):
        entry = {"models": {}, "comparisons": {}, "periods": {}}
        for name, group in part.groupby("model"):
            vectors = np.stack(group.probabilities.map(json.loads))
            targets = group.outcome.to_numpy(dtype=int)
            entry["models"][name] = dict(n=len(group), logloss=float(group.logloss.mean()), brier=float(group.brier.mean()),
                calibration={str(k): reliability(vectors[:, k], targets == k) for k in range(vectors.shape[1])})
        comparators = ["population", "TB1-MD" if lane == "EPL" else "Elo_fixed_K20_home70"]
        for name in part.model.unique():
            for base in comparators:
                if name != base:
                    entry["comparisons"][f"{name}_minus_{base}"] = paired(part, name, base)
        for period in ("selection_periods", "later_development_check_periods"):
            selected = part.loc[part.season.isin(protocol[period][lane])]
            candidates = {name:float(g.logloss.mean()) for name,g in selected.groupby("model")}
            entry["periods"][period] = {"seasons":protocol[period][lane], "mean_logloss":candidates}
        selected_name = min(entry["periods"]["selection_periods"]["mean_logloss"], key=entry["periods"]["selection_periods"]["mean_logloss"].get)
        entry["selected_on_earlier_periods"] = selected_name
        later = part.loc[part.season.isin(protocol["later_development_check_periods"][lane])]
        entry["later_selected_comparisons"] = {base:paired(later, selected_name, base) for base in comparators if base != selected_name}
        report["families"][f"{lane}:{family}"] = entry
    return report


def run():
    protocol_path = RUN / "development_protocol.json"
    protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    output, report_path = RUN / "family_forecasts.csv", RUN / "family_diagnostics.json"
    if output.exists() or report_path.exists():
        raise FileExistsError("immutable development run already exists; create a new protocol version")
    for name, digest in protocol["data_receipts"].items():
        if sha(PROCESSED/name) != digest:
            raise ValueError("data changed after protocol freeze: "+name)
    epl = pd.read_parquet(PROCESSED / "matches.parquet")
    frame = pd.concat([epl_forecasts(epl, protocol["folds"]["EPL"]), nbl_forecasts(checked_data(), protocol["folds"]["NBL"])], ignore_index=True)
    if frame.duplicated(["lane", "event_id", "model", "family"]).any():
        raise ValueError("duplicate evaluation observation")
    if not (pd.to_datetime(frame.cutoff_utc, utc=True) < pd.to_datetime(frame.kickoff_utc, utc=True)).all():
        raise ValueError("evaluation cutoff leakage")
    report = summarize(frame, protocol)
    report.update(created_utc=datetime.now(timezone.utc).isoformat(), protocol_sha256=sha(protocol_path),
                  evaluator_sha256=sha(Path(__file__)), code_inputs={p.name:sha(p) for p in [Path(__file__), Path(__file__).with_name("dixon_coles.py"),Path(__file__).with_name("nbl_model.py")]})
    with output.open("x", newline="", encoding="utf-8") as handle:
        frame.to_csv(handle, index=False, float_format="%.12g")
    report["forecasts_sha256"] = sha(output)
    with report_path.open("x", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, allow_nan=False); handle.write("\n")
    return report


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    result = run()
    print(json.dumps({k:{"selection":v["selected_on_earlier_periods"],"later":v["later_selected_comparisons"]} for k,v in result["families"].items()}, indent=2))
