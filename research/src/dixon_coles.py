"""Time-decayed Dixon-Coles goal model with analytic likelihood gradient."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import poisson


@dataclass(frozen=True)
class DCModel:
    teams: tuple[str, ...]
    params: np.ndarray
    promoted_att: float
    promoted_def: float
    as_of: pd.Timestamp
    xi: float
    training_matches: int


def fit_dc(df: pd.DataFrame, as_of, xi: float = 0.0019) -> DCModel:
    cutoff = pd.Timestamp(as_of)
    if cutoff.tzinfo is None:
        raise ValueError("as_of must be timezone aware")
    d = df.loc[df.kickoff_utc < cutoff].copy()
    if len(d) < 300:
        raise ValueError("insufficient strictly pre-cutoff history")
    teams = tuple(sorted(set(d.home) | set(d.away)))
    n = len(teams)
    ix = {name: i for i, name in enumerate(teams)}
    hi = d.home.map(ix).to_numpy(dtype=int)
    ai = d.away.map(ix).to_numpy(dtype=int)
    x, y = d.hg.to_numpy(dtype=int), d.ag.to_numpy(dtype=int)
    days = (cutoff - d.kickoff_utc).dt.total_seconds().to_numpy() / 86400
    if np.any(days <= 0):
        raise AssertionError("future leakage")
    w = np.exp(-xi * days)

    def objective(p):
        att, dfn = p[:n], p[n:2*n]
        base, hadv, rho = p[-3:]
        lam = np.exp(np.clip(base + att[hi] + dfn[ai] + hadv, -5, 5))
        mu = np.exp(np.clip(base + att[ai] + dfn[hi], -5, 5))
        tau = np.ones(len(d))
        dlam = np.zeros(len(d)); dmu = np.zeros(len(d)); drho = np.zeros(len(d))
        m00 = (x == 0) & (y == 0)
        m01 = (x == 0) & (y == 1)
        m10 = (x == 1) & (y == 0)
        m11 = (x == 1) & (y == 1)
        tau[m00] = 1 - lam[m00]*mu[m00]*rho
        tau[m01] = 1 + lam[m01]*rho
        tau[m10] = 1 + mu[m10]*rho
        tau[m11] = 1 - rho
        if np.any(tau <= 1e-8):
            return 1e12, np.zeros_like(p)
        dlam[m00] = -mu[m00]*rho/tau[m00]
        dmu[m00] = -lam[m00]*rho/tau[m00]
        drho[m00] = -lam[m00]*mu[m00]/tau[m00]
        dlam[m01] = rho/tau[m01]
        drho[m01] = lam[m01]/tau[m01]
        dmu[m10] = rho/tau[m10]
        drho[m10] = mu[m10]/tau[m10]
        drho[m11] = -1/tau[m11]
        ll = np.log(tau) + poisson.logpmf(x, lam) + poisson.logpmf(y, mu)
        regularize = .12*(np.sum(att**2) + np.sum(dfn**2)) + 100*(att.sum()**2 + dfn.sum()**2)
        loss = -np.dot(w, ll) + regularize
        gl = w*(x-lam + lam*dlam)
        gm = w*(y-mu + mu*dmu)
        grad = np.zeros_like(p)
        np.add.at(grad, hi, -gl)
        np.add.at(grad, ai, -gm)
        np.add.at(grad, n+ai, -gl)
        np.add.at(grad, n+hi, -gm)
        grad[:n] += .24*att + 200*att.sum()
        grad[n:2*n] += .24*dfn + 200*dfn.sum()
        grad[-3] = -(gl+gm).sum()
        grad[-2] = -gl.sum()
        grad[-1] = -np.dot(w, drho)
        return float(loss), grad

    away_mean = max(.5, float(d.ag.mean()))
    home_ratio = max(.5, float(d.hg.mean()) / away_mean)
    p0 = np.r_[np.zeros(2*n), np.log(away_mean), np.log(home_ratio), -.05]
    bounds = [(-2.5, 2.5)]*(2*n) + [(-1.5, 1.5), (-.5, .7), (-.1, .03)]
    result = minimize(objective, p0, jac=True, method="L-BFGS-B", bounds=bounds,
                      options={"maxiter": 400, "ftol": 1e-8})
    if not result.success:
        raise RuntimeError(f"Dixon-Coles fit failed: {result.message}")
    season_order = sorted(d.season.unique())
    first_season = season_order[0]
    later_entrants = [name for name in teams if d.loc[(d.home == name) | (d.away == name), "season"].min() > first_season]
    if not later_entrants:
        # First model origin has one completed season. These are its promoted
        # entrants relative to the 2019-20 fixture set, fixed before 2021-22.
        later_entrants = [name for name in ("Fulham", "Leeds", "West Brom") if name in ix]
    if not later_entrants:
        raise ValueError("no historical promoted-side prior")
    promoted_att = float(np.mean([result.x[ix[name]] for name in later_entrants]))
    promoted_def = float(np.mean([result.x[n+ix[name]] for name in later_entrants]))
    return DCModel(teams, result.x, promoted_att, promoted_def, cutoff, xi, len(d))


def rates(model: DCModel, home: str, away: str) -> tuple[float, float]:
    ix = {name: i for i, name in enumerate(model.teams)}
    n = len(ix)
    p = model.params
    ah = p[ix[home]] if home in ix else model.promoted_att
    aa = p[ix[away]] if away in ix else model.promoted_att
    dh = p[n+ix[home]] if home in ix else model.promoted_def
    da = p[n+ix[away]] if away in ix else model.promoted_def
    base, hadv = p[-3:-1]
    return float(np.exp(base+ah+da+hadv)), float(np.exp(base+aa+dh))


def score_matrix(lam: float, mu: float, rho: float = 0, g: int = 20) -> tuple[np.ndarray, float]:
    if lam <= 0 or mu <= 0 or g < 5:
        raise ValueError("invalid rates or grid")
    mass = np.outer(poisson.pmf(np.arange(g+1), lam), poisson.pmf(np.arange(g+1), mu))
    mass[0,0] *= 1-lam*mu*rho
    mass[0,1] *= 1+lam*rho
    mass[1,0] *= 1+mu*rho
    mass[1,1] *= 1-rho
    if (mass < 0).any():
        raise ValueError("invalid Dixon-Coles correction")
    tail = float(1-mass.sum())
    if tail > 1e-6:
        raise ValueError(f"score grid loses material tail mass: {tail}")
    return mass/mass.sum(), tail


def probabilities(matrix: np.ndarray) -> dict[str, float]:
    goals = np.arange(matrix.shape[0])
    total = np.add.outer(goals, goals)
    return {"H": float(np.tril(matrix, -1).sum()),
            "D": float(np.trace(matrix)),
            "A": float(np.triu(matrix, 1).sum()),
            "O2.5": float(matrix[total > 2].sum()),
            "U2.5": float(matrix[total < 3].sum()),
            "BTTS_Y": float(matrix[1:,1:].sum()),
            "BTTS_N": float(1-matrix[1:,1:].sum())}


def predict(model: DCModel, home: str, away: str) -> tuple[dict[str, float], np.ndarray, float]:
    lam, mu = rates(model, home, away)
    matrix, tail = score_matrix(lam, mu, float(model.params[-1]))
    return probabilities(matrix), matrix, tail
