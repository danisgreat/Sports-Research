"""Soccer half-time model: separate first- and second-half goal rates, each with its own low-score correction (DST-07).

A single full-time Dixon-Coles grid cannot price first-half rows or the "0-0 at half-time" path. Here the match's goals
are split with `first_half_share` (the share of goals scored before the interval); each half is an independent
Dixon-Coles grid, and full time is their convolution. The EPL share is about 0.433 (1.19 of 2.75 goals).
"""

from dataclasses import dataclass
from typing import Dict, Sequence

import numpy as np
from scipy.optimize import brentq, least_squares
from scipy.signal import fftconvolve

from ...common.contracts import ScoreDistribution
from ...common.dixon_coles import score_grid


@dataclass(frozen=True)
class HalfSplit:
    first_half_share: float          # fraction of expected goals scored in the first half, in (0, 1)
    rho: float                       # Dixon-Coles low-score dependence applied inside each half
    max_goals_per_half: int = 8

    def __post_init__(self):
        if not 0.0 < self.first_half_share < 1.0:
            raise ValueError("first_half_share must lie in (0, 1)")
        if not -0.25 <= self.rho <= 0.25:
            raise ValueError("rho must lie in [-0.25, 0.25]")


def half_distributions(lambda_home: float, lambda_away: float, split: HalfSplit) -> Dict[str, ScoreDistribution]:
    """{"first_half", "second_half", "full_time"} for expected 90-minute goals (lambda_home, lambda_away)."""
    if lambda_home <= 0 or lambda_away <= 0:
        raise ValueError("expected goals must be positive")
    s = split.first_half_share
    n = split.max_goals_per_half
    first = score_grid(lambda_home * s, lambda_away * s, split.rho, n, endpoint="first_half")
    second = score_grid(lambda_home * (1.0 - s), lambda_away * (1.0 - s), split.rho, n, endpoint="second_half")
    full = np.clip(fftconvolve(first.grid, second.grid), 0.0, None)
    full /= full.sum()
    support = np.arange(full.shape[0])
    meta = {"model": "dixon_coles_halves", "first_half_share": s, "rho": split.rho,
            "lambda_home": lambda_home, "lambda_away": lambda_away}
    return {"first_half": first, "second_half": second,
            "full_time": ScoreDistribution(full, support, support, endpoint="regulation", metadata=meta)}


def p_goal_in_first_half(lambda_total: float, split: HalfSplit) -> float:
    dist = half_distributions(lambda_total / 2.0, lambda_total / 2.0, split)["first_half"]
    return 1.0 - float(dist.grid[0, 0])


def fit_first_half_share(lambda_total: float, target_p_first_half_goal: float, rho: float) -> float:
    """First-half share at which P(at least one first-half goal) equals the observed rate (e.g. 0.716 in the EPL)."""
    def gap(share: float) -> float:
        return p_goal_in_first_half(lambda_total, HalfSplit(share, rho)) - target_p_first_half_goal
    lo, hi = 0.05, 0.95
    if gap(lo) > 0 or gap(hi) < 0:
        raise ValueError(f"target {target_p_first_half_goal:.3f} is not reachable for lambda_total={lambda_total:.2f}")
    return float(brentq(gap, lo, hi, xtol=1e-10))


def half_goal_pmf(lambda_home: float, lambda_away: float, split: HalfSplit, bins: int = 5) -> np.ndarray:
    """P(first-half goals = 0, 1, ..., bins-2, bins-1 or more)."""
    first = half_distributions(lambda_home, lambda_away, split)["first_half"]
    pmf = np.bincount(np.add.outer(first.home_support, first.away_support).ravel(), weights=first.grid.ravel())
    return np.concatenate([pmf[:bins - 1], [pmf[bins - 1:].sum()]])


def fit_half_split(lambda_home: float, lambda_away: float, observed_pmf: Sequence[float]) -> HalfSplit:
    """First-half share and low-score rho that best reproduce an observed first-half goal distribution.

    `observed_pmf` holds P(0), P(1), ..., P(k or more) first-half goals. The EPL register gives
    0.284/0.382/0.224/0.084/0.026; the fit selects a share near 0.45 and a small positive rho, because
    first-half goal counts are slightly under-dispersed relative to a Poisson.
    """
    target = np.asarray(observed_pmf, dtype=float)
    if abs(target.sum() - 1.0) > 1e-6 or len(target) < 3:
        raise ValueError("observed_pmf must be a probability vector with at least three bins")

    def residuals(x):
        return half_goal_pmf(lambda_home, lambda_away, HalfSplit(float(x[0]), float(x[1])), len(target)) - target

    fit = least_squares(residuals, [0.45, 0.0], bounds=([0.05, -0.25], [0.95, 0.25]), xtol=1e-12, ftol=1e-12)
    return HalfSplit(first_half_share=float(fit.x[0]), rho=float(fit.x[1]))
