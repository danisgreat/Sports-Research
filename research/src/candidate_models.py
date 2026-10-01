"""Versioned candidates selected on the frozen chronological development run.

These models are SHADOW_ONLY. Selection is not untouched holdout validation.
"""
from __future__ import annotations
import json
import numpy as np
import pandas as pd
from scipy.stats import norm
from .dixon_coles import fit_dc, predict, probabilities
from .model_diagnostics import tb1_matrix
from .nbl_model import fit as fit_nbl, predict as predict_nbl
from .load import ROOT, PROCESSED, sha
from .model_custody import verify_model_build

EPL_VERSION = "epl-coherent-ensemble-0.2.0"
NBL_VERSION = "nbl-oof-width-0.2.0"
DEVELOPMENT = ROOT/"runs/implementation_2026-10-01"


def checked_development():
    report = json.loads((DEVELOPMENT/"family_diagnostics.json").read_text(encoding="utf-8"))
    if report["status"] != "CHRONOLOGICAL_DEVELOPMENT_ONLY" or sha(DEVELOPMENT/"family_forecasts.csv") != report["forecasts_sha256"]:
        raise ValueError("candidate development receipt invalid")
    return report


def epl(df, season, cutoff, home, away):
    verify_model_build("EPL", EPL_VERSION)
    report = checked_development()
    if report["families"]["EPL:1X2"]["selected_on_earlier_periods"] != "coherent_DC_TB1_mixture_0.75":
        raise ValueError("candidate does not match frozen selection")
    dc = fit_dc(df, cutoff, .003)
    _, matrix, tail = predict(dc, home, away)
    baseline = tb1_matrix(df, season, cutoff, home, away)
    mixture = .75*matrix+.25*baseline
    if (mixture < 0).any() or abs(mixture.sum()-1)>1e-9:
        raise ValueError("candidate distribution incoherent")
    return probabilities(mixture), mixture, dict(model_version=EPL_VERSION,
            status="SHADOW_ONLY", admitted_live=False, family_scope=["1X2"],
            ensemble_weights={"Dixon-Coles":.75,"TB1-MD":.25},
            training_matches=dc.training_matches, tail_mass=tail,
            development_report_sha256=sha(DEVELOPMENT/"family_diagnostics.json"))


def nbl(df, cutoff, home, away):
    verify_model_build("NBL", NBL_VERSION)
    report = checked_development()
    if report["families"]["NBL:ML"]["selected_on_earlier_periods"] != "joint_with_chronological_residual_variance":
        raise ValueError("candidate does not match frozen selection")
    cutoff = pd.Timestamp(cutoff)
    if cutoff.tzinfo is None:
        raise ValueError("cutoff needs an offset")
    model = fit_nbl(df, cutoff, 180)
    joint, original = predict_nbl(model, home, away)
    prior = pd.read_csv(DEVELOPMENT/"family_forecasts.csv", dtype={"event_id":str})
    prior = prior.loc[(prior.lane=="NBL")&(prior.model=="joint_score_model")].copy()
    prior = prior.loc[pd.to_datetime(prior.kickoff_utc, utc=True)<cutoff]
    labels = df.loc[df.kickoff_utc<cutoff, ["event_id","hg","ag"]].copy()
    labels["event_id"] = labels.event_id.astype(str)
    merged = prior.merge(labels, on="event_id", validate="one_to_one")
    if len(merged)<100:
        raise ValueError("candidate requires 100 earlier out-of-fold residuals")
    residuals = merged.hg-merged.ag-merged.margin_mean
    sd = float(np.sqrt(np.mean(np.square(residuals))))
    if not np.isfinite(sd) or sd<=0:
        raise ValueError("invalid chronological residual width")
    p = float(norm.cdf(joint.mean_margin/sd))
    return p, dict(model_version=NBL_VERSION, status="SHADOW_ONLY", admitted_live=False,
                   family_scope=["ML"], mean_margin=joint.mean_margin, sd_margin=sd,
                   previous_sd_margin=joint.sd_margin, original_p_home=original,
                   oof_residual_n=len(merged), training_matches=model.training_matches,
                   width_source="STRICTLY_EARLIER_CHRONOLOGICAL_FORECAST_ERRORS",
                   development_report_sha256=sha(DEVELOPMENT/"family_diagnostics.json"))
