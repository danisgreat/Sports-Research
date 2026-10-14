"""Paired comparisons and the development verdict (ML_RL_IMPLEMENTATION_FRAMEWORK §9.5, first row)."""
from __future__ import annotations

import numpy as np
import pandas as pd

from ml.core.metrics import brier, brier_decomposition, calibration_fit, paired_week_interval, reliability_table

METRICS = [
    ("brier_home", "Home-win Brier (primary)"),
    ("logloss_home", "Home-win log loss"),
    ("brier_3way", "Three-way half-sum Brier"),
    ("crps_margin", "Margin CRPS"),
    ("crps_total", "Total CRPS"),
    ("brier_over", "Over the league-median line, Brier"),
]
COMPARATORS = [("BASE", "BASELINE_LEAGUE_V1"), ("TB1", "TEAM_BASELINE_P (TB-1)")]


def paired_table(df: pd.DataFrame, cand: str, seasons) -> pd.DataFrame:
    rows = []
    for comp, comp_name in COMPARATORS:
        for key, label in METRICS:
            a, b = f"{cand}_{key}", f"{comp}_{key}"
            if a not in df or b not in df:
                continue
            for season in [*seasons, "ALL"]:
                d = df if season == "ALL" else df[df["season"] == season]
                d = d[np.isfinite(d[a]) & np.isfinite(d[b])]
                if d.empty:
                    continue
                res = paired_week_interval(d[a] - d[b], d["event_id"], d["week"])
                rows.append({"comparator": comp_name, "metric": label, "season": season, "n_games": len(d),
                             "candidate": float(d[a].mean()), "comparator_value": float(d[b].mean()), **res})
    return pd.DataFrame(rows, columns=["comparator", "metric", "season", "n_games", "candidate", "comparator_value", "k_weeks", "n_events", "mean", "lo", "hi", "sd_w", "status"])


def development_verdict(pt: pd.DataFrame, seasons) -> dict:
    """PASS only if the primary metric's interval is below 0 against BOTH comparators in EVERY test season."""
    out = {}
    if pt.empty or not seasons:
        return {**{name: "NOT_COMPUTABLE" for _, name in COMPARATORS}, "overall": "FAIL_DEVELOPMENT"}
    for comp, comp_name in COMPARATORS:
        sub = pt[(pt["comparator"] == comp_name) & (pt["metric"] == METRICS[0][1]) & (pt["season"].isin(seasons))]
        if sub.empty:
            out[comp_name] = "NOT_COMPUTABLE"
            continue
        ok = all(s in set(sub["season"]) for s in seasons) and bool((sub["status"] == "BELOW_ZERO").all())
        out[comp_name] = "BELOW_ZERO_EVERY_SEASON" if ok else "NOT_EVERY_SEASON"
    out["overall"] = ("PASS_DEVELOPMENT" if all(v == "BELOW_ZERO_EVERY_SEASON" for k, v in out.items())
                      else "FAIL_DEVELOPMENT")
    return out


def calibration_block(df: pd.DataFrame, cand: str) -> dict:
    p, y = df[f"{cand}_p_home"].to_numpy(), df["y_home"].to_numpy()
    return {"fit": calibration_fit(p, y), "decomposition": brier_decomposition(p, y), "bins": reliability_table(p, y)}


def platt_by_previous_season(df: pd.DataFrame, cand: str, seasons) -> pd.DataFrame:
    """ML-CAL-WIN experiment: logistic recalibration of P(home win) fitted on the previous season's predictions only.

    Applied by reweighting the winner classes (ScoreGrid.reweight_winner), so the home-win mass is what changes;
    here only the home-win Brier is scored. Identity is kept when the previous season has < 200 games.
    """
    from scipy import optimize

    rows = []
    for s in seasons:
        earlier = df.loc[df["season"] < s, "season"]
        prev = df[df["season"] == earlier.max()] if len(earlier) else df.iloc[:0]
        cur = df[df["season"] == s].copy()
        prev = prev[np.isfinite(prev[f"{cand}_p_home"]) & np.isfinite(prev["y_home"])]
        cur = cur[np.isfinite(cur[f"{cand}_p_home"]) & np.isfinite(cur["y_home"])]
        if len(prev) < 200 or cur.empty:
            continue
        x = np.log(np.clip(prev[f"{cand}_p_home"], 1e-6, 1 - 1e-6) / (1 - np.clip(prev[f"{cand}_p_home"], 1e-6, 1 - 1e-6)))
        y = prev["y_home"].to_numpy()

        def nll(b):
            z = b[0] + b[1] * x
            return np.sum(np.logaddexp(0, z) - y * z)

        fitted = optimize.minimize(nll, np.array([0.0, 1.0]), method="BFGS")
        if not fitted.success or not np.isfinite(fitted.x).all():
            continue  # A failed calibrator is not applied; the deployed identity remains in place.
        b = fitted.x
        pc = np.clip(cur[f"{cand}_p_home"], 1e-6, 1 - 1e-6)
        xc = np.log(pc / (1 - pc))
        cur["CAL_p_home"] = 1 / (1 + np.exp(-(b[0] + b[1] * xc)))
        cur["CAL_brier_home"] = brier(cur["CAL_p_home"], cur["y_home"])
        res = paired_week_interval(cur["CAL_brier_home"] - cur[f"{cand}_brier_home"], cur["event_id"], cur["week"])
        rows.append({"season": s, "intercept": b[0], "slope": b[1], "n": len(cur),
                     "uncalibrated": cur[f"{cand}_brier_home"].mean(), "calibrated": cur["CAL_brier_home"].mean(), **res})
    return pd.DataFrame(rows)


def fmt(x, nd=4) -> str:
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "—"
    if isinstance(x, (int, np.integer)):
        return str(int(x))
    return f"{x:.{nd}f}"


def md_table(df: pd.DataFrame, cols: list[str], nd: int = 4) -> str:
    head = "| " + " | ".join(cols) + " |\n|" + "|".join("---" for _ in cols) + "|\n"
    body = ""
    for _, r in df.iterrows():
        body += "| " + " | ".join(fmt(r[c], nd) if not isinstance(r[c], str) else r[c] for c in cols) + " |\n"
    return head + body
