"""Bivariate margin/total candidate for NBL and other point sports.

This is shared mathematics only. Each league needs its own fit, data audit and
holdout before its probabilities can be labelled VALIDATED.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ...sports.base import Contract


@dataclass(frozen=True)
class MarginTotal:
    mean_margin: float
    mean_total: float
    sd_margin: float
    sd_total: float
    correlation: float
    residual_sample: int

    def __post_init__(self) -> None:
        if min(self.sd_margin, self.sd_total) <= 0 or abs(self.correlation) >= 1:
            raise ValueError("invalid covariance")
        if self.residual_sample < 30:
            raise ValueError("residual width is unsupported")


def simulate_scores(model: MarginTotal, n: int = 200_000, seed: int = 0):
    rng = np.random.default_rng(seed)
    covariance = [[model.sd_margin**2, model.correlation*model.sd_margin*model.sd_total],
                  [model.correlation*model.sd_margin*model.sd_total, model.sd_total**2]]
    margin, total = rng.multivariate_normal([model.mean_margin, model.mean_total], covariance, n).T
    home = np.rint((total+margin)/2).astype(int)
    away = np.rint((total-margin)/2).astype(int)
    if (home < 0).any() or (away < 0).any():
        raise ValueError("normal model generated negative score; fit a bounded distribution")
    # A full-game basketball contract cannot settle as a tie. Continuous
    # margin sign chooses the winner for draws introduced only by rounding.
    tied = home == away
    home[tied & (margin >= 0)] += 1
    away[tied & (margin < 0)] += 1
    return home, away


def outcome(home: np.ndarray, away: np.ndarray, contract: Contract):
    if contract.market == "ML":
        value = home-away if contract.side == "HOME" else away-home
    elif contract.market == "SPREAD":
        value = (home-away if contract.side == "HOME" else away-home)+contract.line
    elif contract.market == "TOTAL":
        value = (home+away-contract.line)*(1 if contract.side == "OVER" else -1)
    else:
        raise ValueError("unsupported margin/total market")
    return value > 0, value == 0


def price(home: np.ndarray, away: np.ndarray, contract: Contract) -> dict[str,float]:
    win, push = outcome(home, away, contract)
    p_push = float(push.mean())
    if p_push == 1:
        raise ValueError("all draws push")
    return dict(win=float(win.mean()), push=p_push,
                loss=float((~win & ~push).mean()), conditional_win=float(win.mean()/(1-p_push)))


def both_lose(home: np.ndarray, away: np.ndarray, a: Contract, b: Contract) -> float:
    wa, pa = outcome(home, away, a)
    wb, pb = outcome(home, away, b)
    return float(((~wa & ~pa) & (~wb & ~pb)).mean())
