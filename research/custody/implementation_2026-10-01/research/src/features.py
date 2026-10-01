"""Point-in-time M0 and framework TB-1-MD baseline features for EPL."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .dixon_coles import probabilities, score_matrix


def _past(df: pd.DataFrame, cutoff) -> pd.DataFrame:
    cutoff = pd.Timestamp(cutoff)
    if cutoff.tzinfo is None:
        raise ValueError("cutoff must be timezone aware")
    past = df.loc[df.kickoff_utc < cutoff]
    if not (past.kickoff_utc < cutoff).all():
        raise AssertionError("future leakage")
    return past


def population_1x2(df: pd.DataFrame, cutoff) -> dict[str, float]:
    past = _past(df, cutoff)
    if past.empty:
        raise ValueError("no past population")
    counts = np.array([(past.hg > past.ag).sum(), (past.hg == past.ag).sum(),
                       (past.hg < past.ag).sum()], dtype=float)
    counts += 1  # frozen Laplace prior prevents zero-mass event outcomes
    counts /= counts.sum()
    return dict(zip(("H", "D", "A"), counts.tolist()))


def tb1_md(df: pd.DataFrame, season: str, cutoff, home: str, away: str,
           k: float = 2) -> dict[str, float]:
    past = _past(df, cutoff)
    current = past.loc[past.season == season]
    prior_year = int(season[:4]) - 1
    previous = past.loc[past.season == f"{prior_year}-{str(prior_year+1)[-2:]}"]
    if len(previous) != 380:
        raise ValueError("previous completed season unavailable")
    prior_lm = float((previous.hg.sum()+previous.ag.sum())/(2*len(previous)))
    lm = float((current.hg.sum()+current.ag.sum())/(2*len(current))) if len(current) else prior_lm
    home_edge = float((previous.hg-previous.ag).mean())

    def rating(name: str) -> tuple[float, float]:
        at_home = current.loc[current.home == name]
        at_away = current.loc[current.away == name]
        n = len(at_home)+len(at_away)
        pf = at_home.hg.sum()+at_away.ag.sum()
        pa = at_home.ag.sum()+at_away.hg.sum()
        return (float((pf+k*lm)/(n+k)), float((pa+k*lm)/(n+k)))

    oh, dh = rating(home)
    oa, da = rating(away)
    total = (oh+da+oa+dh)/2
    margin = ((oh-dh)-(oa-da))/2 + home_edge
    lam, mu = (total+margin)/2, (total-margin)/2
    if lam <= 0 or mu <= 0:
        raise ValueError("TB-1-MD produced invalid goal rate")
    matrix, _ = score_matrix(lam, mu)
    return probabilities(matrix)
