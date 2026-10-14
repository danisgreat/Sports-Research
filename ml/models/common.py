"""Shared model utilities: time-decay weights, errors, and the tie (extra-time) policy per league."""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from ml.config import League
from ml.core.distributions import ScoreGrid


class FitError(RuntimeError):
    """A fit failed. Callers record NOT_ISSUED:FIT_FAILED; no default parameters are ever substituted."""


def decay_weights(dates: pd.Series, as_of: pd.Timestamp, half_life_days: float) -> np.ndarray:
    age = (as_of - pd.to_datetime(dates)).dt.days.to_numpy(dtype=float)
    if np.any(age < 0):
        raise FitError("training data contains games on or after the fit date (leakage)")
    return 0.5 ** (age / half_life_days)


def apply_tie_rule(grid: ScoreGrid, lg: League, extra: dict) -> ScoreGrid:
    """Resolve tied regulation mass according to the league's endpoint.

    ``extra`` carries the per-fit quantities: p_home_extra, residual_draw, both_bonus, winner_bonus.
    """
    if lg.tie_rule == "draw":
        return grid
    return grid.resolve_ties(p_home_extra=extra["p_home_extra"], residual_draw=extra.get("residual_draw", 0.0),
                             winner_bonus=extra.get("winner_bonus", lg.winner_bonus),
                             both_bonus=extra.get("both_bonus", 0))


def normal_extra(lg: League, mean_margin: float, sd_margin: float, mean_total: float, residual_draw: float) -> dict:
    """Extra-time branch for points sports from the regulation normal.

    Basketball: one extra period of length r (share of regulation); margin ~ N(r*mu, r*sigma^2), each team scores
    about r*mean_total/2. NFL/NRL: sudden-death style, winner gets ``winner_bonus`` (3 or 1); a fitted share of
    tied games stays drawn (residual_draw).
    """
    if lg.tie_rule == "overtime":
        r = lg.extra_fraction
        p = float(stats.norm.cdf(mean_margin * np.sqrt(r) / sd_margin))
        w = max(1, int(round(sd_margin * np.sqrt(r) * np.sqrt(2 / np.pi))))
        both = max(0, int(round(mean_total * r / 2 - w / 2)))
        return {"p_home_extra": p, "residual_draw": 0.0, "winner_bonus": w, "both_bonus": both}
    if lg.tie_rule == "overtime_residual":
        r = lg.extra_fraction or 1 / 8
        p = float(stats.norm.cdf(mean_margin * np.sqrt(r) / sd_margin))
        return {"p_home_extra": p, "residual_draw": residual_draw, "winner_bonus": lg.winner_bonus, "both_bonus": 0}
    return {}


def residual_draw_share(train: pd.DataFrame, sd_margin: float) -> float:
    """Method of moments: observed draw rate / mean regulation tie mass of a N(mu, sigma) margin (capped to [0, 1])."""
    if len(train) == 0:
        return 0.0
    draws = float((train["hs"] == train["as_"]).mean())
    tie_mass = 1.0 / (sd_margin * np.sqrt(2 * np.pi))
    return float(np.clip(draws / tie_mass, 0.0, 1.0))
