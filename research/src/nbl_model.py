"""Point-in-time NBL joint home/away score model, preregistered before tuning."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.stats import norm

from .sports.basketball.joint import MarginTotal


@dataclass(frozen=True)
class NBLFit:
    teams: tuple[str, ...]
    coefficients: np.ndarray
    residual_covariance: np.ndarray
    training_matches: int
    effective_matches: float
    half_life_days: int
    cutoff_utc: pd.Timestamp


def fit(df: pd.DataFrame, cutoff_utc: pd.Timestamp, half_life_days: int) -> NBLFit:
    cutoff = pd.Timestamp(cutoff_utc)
    if cutoff.tzinfo is None:
        raise ValueError("NBL cutoff must have a UTC offset")
    if half_life_days not in (180, 365, 730):
        raise ValueError("half-life outside preregistered grid")
    past = df.loc[df.kickoff_utc < cutoff].copy()
    if len(past) < 100:
        raise ValueError("NBL model needs 100 prior matches")
    if past.event_id.duplicated().any() or (past[["hg", "ag"]].to_numpy() < 0).any():
        raise ValueError("invalid NBL training scores or event IDs")
    teams = tuple(sorted(set(past.home) | set(past.away)))
    ix = {team: i for i, team in enumerate(teams)}
    n = len(past)
    p = 2 + 2 * len(teams)
    design = np.zeros((2*n, p))
    labels = np.empty(2*n)
    w = np.empty(2*n)
    ages = (cutoff - past.kickoff_utc).dt.total_seconds().to_numpy() / 86400
    game_weights = np.exp(-np.log(2) * ages / half_life_days)
    effective = float(game_weights.sum()**2 / np.square(game_weights).sum())
    if effective < 30:
        raise ValueError("NBL effective training sample below 30")
    for j, game in enumerate(past.itertuples()):
        hi, ai = ix[game.home], ix[game.away]
        design[2*j, (0, 1, 2+hi, 2+len(teams)+ai)] = 1
        design[2*j+1, (0, 2+ai, 2+len(teams)+hi)] = 1
        labels[2*j:2*j+2] = (game.hg, game.ag)
        w[2*j:2*j+2] = game_weights[j]
    ridge = np.zeros(p)
    ridge[2:] = 8.0 * (game_weights.sum() / n)
    xtw = design.T * w
    coefficients = np.linalg.solve(xtw @ design + np.diag(ridge), xtw @ labels)
    residuals = (labels - design @ coefficients).reshape(n, 2)
    centered = residuals - np.average(residuals, axis=0, weights=game_weights)
    covariance = (centered * game_weights[:, None]).T @ centered / game_weights.sum()
    if np.linalg.eigvalsh(covariance).min() <= 0:
        raise ValueError("non-positive NBL score covariance")
    return NBLFit(teams, coefficients, covariance, n, effective, half_life_days, cutoff)


def predict(model: NBLFit, home: str, away: str) -> tuple[MarginTotal, float]:
    if home == away or home not in model.teams or away not in model.teams:
        raise ValueError("unknown or identical NBL teams")
    ix = {team: i for i, team in enumerate(model.teams)}
    n = len(model.teams)
    p = model.coefficients
    mean_home = p[0] + p[1] + p[2+ix[home]] + p[2+n+ix[away]]
    mean_away = p[0] + p[2+ix[away]] + p[2+n+ix[home]]
    transform = np.array([[1., -1.], [1., 1.]])
    mt_cov = transform @ model.residual_covariance @ transform.T
    sd_margin, sd_total = np.sqrt(np.diag(mt_cov))
    correlation = float(mt_cov[0, 1] / (sd_margin*sd_total))
    joint = MarginTotal(float(mean_home-mean_away), float(mean_home+mean_away),
                        float(sd_margin), float(sd_total), correlation,
                        model.training_matches)
    p_home = float(norm.cdf(joint.mean_margin / joint.sd_margin))
    if not 0 < p_home < 1:
        raise ValueError("degenerate NBL moneyline probability")
    return joint, p_home


def population_home(df: pd.DataFrame, cutoff_utc: pd.Timestamp) -> float:
    past = df.loc[df.kickoff_utc < cutoff_utc]
    if len(past) < 100:
        raise ValueError("NBL population needs 100 prior matches")
    if (past.hg == past.ag).any():
        raise ValueError("NBL full-game score cannot be tied")
    return float(((past.hg > past.ag).sum() + 1) / (len(past) + 2))
