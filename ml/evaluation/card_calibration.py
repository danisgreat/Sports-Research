"""Calibration audit of the issued cards' own stated probabilities (GAME_PREDICTION_RANK_LOG.csv).

Descriptive only: these are historical, partly ungated cards with dependent rows within a card, settled under
several scoring versions. Intervals resample whole cards. Nothing here recalibrates or relabels a card.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from ml.config import REPO_ROOT
from ml.core.metrics import brier_decomposition, calibration_fit, cluster_bootstrap_mean, reliability_table

RANK_LOG = REPO_ROOT / "GAME_PREDICTION_RANK_LOG.csv"


def load_rows() -> tuple[pd.DataFrame, dict]:
    r = pd.read_csv(RANK_LOG, encoding="utf-8-sig", dtype=str)
    n0 = len(r)
    r["p"] = pd.to_numeric(r["stated_p"], errors="coerce")
    r["rank_n"] = pd.to_numeric(r["rank"], errors="coerce")
    keep = r["p"].notna() & r["rank_pass_fail"].isin(["PASS", "FAIL"])
    info = {"rows": n0, "with_numeric_p": int(r["p"].notna().sum()), "decisive_with_p": int(keep.sum()),
            "excluded_statuses": r.loc[r["p"].notna() & ~keep, "rank_pass_fail"].value_counts().to_dict()}
    d = r[keep].copy()
    d["y"] = (d["rank_pass_fail"] == "PASS").astype(float)
    d["card_num"] = d["card_id"].str.extract(r"(\d+)").astype(float)
    return d, info


def audit() -> dict:
    d, info = load_rows()
    out = {"info": info}
    groups = {"ALL": d, "RANK_1_2": d[d["rank_n"] <= 2], "RANK_3_PLUS": d[d["rank_n"] >= 3],
              "P-001..P-299": d[d["card_num"] < 300], "P-300..P-499": d[(d["card_num"] >= 300) & (d["card_num"] < 500)],
              "P-500+": d[d["card_num"] >= 500]}
    rows = []
    for name, g in groups.items():
        if len(g) < 20:
            continue
        cf = calibration_fit(g["p"], g["y"])
        dec = brier_decomposition(g["p"], g["y"])
        gap = (g["p"] - g["y"]).to_numpy()
        lo, hi = cluster_bootstrap_mean(gap, g["card_id"].to_numpy())
        rows.append({"group": name, "rows": len(g), "cards": g["card_id"].nunique(), "mean_p": g["p"].mean(),
                     "hit_rate": g["y"].mean(), "cal_in_large": cf["cal_in_large"], "cil_card_lo": lo, "cil_card_hi": hi,
                     "slope": cf["slope"], "slope_se": cf["slope_se"], "intercept": cf["intercept"], "ece": cf["ece"],
                     "brier": dec["brier"], "reliability": dec["reliability"], "resolution": dec["resolution"],
                     "uncertainty": dec["uncertainty"]})
    out["groups"] = pd.DataFrame(rows)
    out["bins_all"] = reliability_table(d["p"], d["y"])
    out["bins_top2"] = reliability_table(d.loc[d["rank_n"] <= 2, "p"], d.loc[d["rank_n"] <= 2, "y"])
    return out
