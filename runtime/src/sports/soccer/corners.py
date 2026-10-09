"""Soccer corners: negative-binomial totals split between the teams with negative dependence (DST-06).

Corner counts are over-dispersed, and the two teams' counts are negatively correlated (a team that dominates
territory wins corners while the other defends). The model keeps this structure explicit:

  total   T ~ NegativeBinomial(mean mu_h + mu_a, dispersion phi)
  home | T ~ BetaBinomial(T, p = mu_h / (mu_h + mu_a) shifted for score state, concentration c)

so totals, team totals and corner handicaps all come from one grid. Team means come from opponent-adjusted
corners-for/against strengths (`AttackDefenceModel`), phi and c from the residual variances.
Corner data is not part of the repository's archive; the model is fitted when a provider supplies it (SRC-02).
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional, Sequence

import numpy as np
from ...common.contracts import ScoreDistribution
from ...common.counts import nb_pmf, split_total_grid
from ...common.errors import InsufficientData, MissingInputs
from ...common.strengths import AttackDefenceModel

MAX_CORNERS = 40


def nb_total_pmf(mean_total: float, phi: float, size: int = MAX_CORNERS + 1) -> np.ndarray:
    if mean_total <= 0:
        raise ValueError("mean total must be positive")
    return nb_pmf(mean_total, phi, size)


def corner_grid(mean_home: float, mean_away: float, phi: float, concentration: float,
                expected_goal_margin: float = 0.0, score_state_beta: float = 0.0) -> np.ndarray:
    """Joint (home, away) corner grid.

    expected_goal_margin: home minus away expected goals; score_state_beta shifts the home share of corners by
    -beta * margin (the trailing side wins more corners). beta = 0 switches the adjustment off.
    """
    return split_total_grid(mean_home, mean_away, phi, concentration, MAX_CORNERS + 1, share_shift=score_state_beta * expected_goal_margin)


def concentration_from_team_sd(mean_total: float, total_sd: float, team_sd: float, share: float = 0.5) -> float:
    """Beta-binomial concentration c reproducing a per-team variance given the total's variance.

    Var(h) = share^2 Var(T) + share(1-share)/(1+c) * (Var(T) + E[T]^2 + c E[T])  =>  c = (V + m^2 - A) / (A - m).
    """
    v_total = total_sd ** 2
    a_term = (team_sd ** 2 - share ** 2 * v_total) / (share * (1.0 - share))
    if a_term <= mean_total:
        raise ValueError("team variance is too small for a negative-binomial split of this total")
    return float((v_total + mean_total ** 2 - a_term) / (a_term - mean_total))


@dataclass
class CornersModel:
    """Fitted corners model: opponent-adjusted team means plus total dispersion and split concentration."""
    strengths: Optional[AttackDefenceModel] = None
    phi: Optional[float] = None
    concentration: Optional[float] = None
    score_state_beta: float = 0.0

    def fit(self, games: Sequence[Dict[str, Any]]) -> "CornersModel":
        """games: [{"home": .., "away": .., "home_corners": int, "away_corners": int, "home_goals"?, "away_goals"?}]"""
        if len(games) < 100:
            raise InsufficientData(f"corners model needs at least 100 matches with a corners provider, got {len(games)}")
        tuples = [(g["home"], g["away"], float(g["home_corners"]), float(g["away_corners"])) for g in games]
        self.strengths = AttackDefenceModel().fit(tuples)
        totals, resid_h, means_t = [], [], []
        for (home, away, hc, ac), g in zip(tuples, games):
            mu_h, mu_a = self.strengths.expected(home, away)
            totals.append(hc + ac)
            means_t.append(mu_h + mu_a)
            resid_h.append(hc - mu_h)
        totals_a, means_a = np.array(totals), np.array(means_t)
        self.phi = float(max(np.sum((totals_a - means_a) ** 2 - means_a) / np.sum(means_a ** 2), 0.0))
        total_var = float(np.mean((totals_a - means_a) ** 2))
        team_var = float(np.mean(np.square(resid_h)))
        mean_total = float(np.mean(means_a))
        try:
            self.concentration = concentration_from_team_sd(mean_total, np.sqrt(total_var), np.sqrt(team_var))
        except ValueError:
            self.concentration = 1e6                                    # splits are binomial-like: negligible extra share dispersion
        goals = [g for g in games if g.get("home_goals") is not None and g.get("away_goals") is not None]
        if len(goals) >= 100:                                           # score-state coefficient: share ~ share0 - beta * goal margin
            share_resid = np.array([(g["home_corners"] / max(g["home_corners"] + g["away_corners"], 1)) -
                                    self.strengths.expected(g["home"], g["away"])[0] /
                                    sum(self.strengths.expected(g["home"], g["away"])) for g in goals])
            margin = np.array([g["home_goals"] - g["away_goals"] for g in goals], dtype=float)
            if margin.var() > 0:
                self.score_state_beta = float(-np.cov(share_resid, margin)[0, 1] / margin.var())
        return self

    def distribution(self, home: Optional[str] = None, away: Optional[str] = None, mean_home: Optional[float] = None,
                     mean_away: Optional[float] = None, expected_goal_margin: float = 0.0,
                     phi: Optional[float] = None, concentration: Optional[float] = None) -> ScoreDistribution:
        if mean_home is None or mean_away is None:
            if self.strengths is None:
                raise MissingInputs("corners: give mean_home/mean_away, or fit the model on provider data")
            if home is None or away is None:
                raise MissingInputs("corners: give home and away team names to look up fitted strengths")
            mean_home, mean_away = self.strengths.expected(home, away)
        phi = self.phi if phi is None else phi
        concentration = self.concentration if concentration is None else concentration
        if phi is None or concentration is None:
            raise MissingInputs("corners: phi and concentration are required (fit the model or pass them)")
        grid = corner_grid(mean_home, mean_away, phi, concentration, expected_goal_margin, self.score_state_beta)
        support = np.arange(MAX_CORNERS + 1)
        return ScoreDistribution(grid, support, support, endpoint="corners_90",
                                 metadata={"model": "corners_nb_betabinomial", "mean_home": mean_home, "mean_away": mean_away,
                                           "phi": phi, "concentration": concentration, "score_state_beta": self.score_state_beta})
