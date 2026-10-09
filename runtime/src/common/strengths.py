"""Opponent-adjusted team strengths with data-driven shrinkage (DST-05).

Replaces the fixed `0.8 * (raw mean / league mean) + 0.2` rule, which ignored opponent quality and
shrank every team by the same amount regardless of games played.

Model (quasi-Poisson log-linear, valid for goals, runs, tries, shots and points alike):

    log E[home score]  = m + h + att[home] + def[away]
    log E[away score]  = m +     att[away] + def[home]

`att` is a team's scoring strength and `def` the strength of the opponent it concedes to (a larger
value means that team concedes more). Both carry a ridge penalty, so a team with few games stays
near the league mean (shrinkage grows as games shrink) and the ridge strength is chosen by
chronological cross-validation: no fixed constant.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
from scipy.optimize import minimize

from .errors import FitFailed, InsufficientData, UnknownTeam, require_converged

Game = Tuple[str, str, float, float]          # home, away, home score, away score
DEFAULT_RIDGE_GRID = (0.3, 1.0, 3.0, 10.0, 30.0, 100.0, 300.0, 1000.0, 3000.0)


@dataclass
class AttackDefenceModel:
    ridge: Optional[float] = None
    ridge_grid: Sequence[float] = DEFAULT_RIDGE_GRID
    cv_folds: int = 4
    min_games: int = 20
    teams: List[str] = field(default_factory=list)
    log_base: float = 0.0           # m
    log_home: float = 0.0           # h
    att: np.ndarray = field(default_factory=lambda: np.array([]))
    defn: np.ndarray = field(default_factory=lambda: np.array([]))
    games_played: Dict[str, int] = field(default_factory=dict)
    cv_scores: Dict[float, float] = field(default_factory=dict)
    ridge_used: float = 0.0

    # ------------------------------------------------------------------ fitting
    @staticmethod
    def _arrays(games: Sequence[Game], index: Dict[str, int]) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        home = np.array([index[g[0]] for g in games], dtype=int)
        away = np.array([index[g[1]] for g in games], dtype=int)
        hs = np.array([g[2] for g in games], dtype=float)
        as_ = np.array([g[3] for g in games], dtype=float)
        return home, away, hs, as_

    @staticmethod
    def _solve(home, away, hs, as_, n_teams: int, ridge: float, start: Optional[np.ndarray] = None) -> np.ndarray:
        league = max(float(np.mean(np.concatenate([hs, as_]))), 1e-9)

        def unpack(theta):
            return theta[0], theta[1], theta[2:2 + n_teams], theta[2 + n_teams:]

        def objective(theta):
            m, h, att, defn = unpack(theta)
            eta_h = m + h + att[home] + defn[away]
            eta_a = m + att[away] + defn[home]
            mu_h, mu_a = np.exp(eta_h), np.exp(eta_a)
            nll = np.sum(mu_h - hs * eta_h) + np.sum(mu_a - as_ * eta_a)
            nll += 0.5 * ridge * (np.sum(att ** 2) + np.sum(defn ** 2))
            r_h, r_a = mu_h - hs, mu_a - as_
            g_att = np.bincount(home, weights=r_h, minlength=n_teams) + np.bincount(away, weights=r_a, minlength=n_teams) + ridge * att
            g_def = np.bincount(away, weights=r_h, minlength=n_teams) + np.bincount(home, weights=r_a, minlength=n_teams) + ridge * defn
            grad = np.concatenate([[np.sum(r_h) + np.sum(r_a), np.sum(r_h)], g_att, g_def])
            return nll, grad

        theta0 = start if start is not None else np.concatenate([[np.log(league), 0.0], np.zeros(2 * n_teams)])
        result = minimize(objective, theta0, jac=True, method="L-BFGS-B", options={"maxiter": 2000, "maxfun": 4000})
        require_converged(result, "AttackDefenceModel", grad_tol=1e-3 * max(1.0, float(np.sum(hs) + np.sum(as_))) ** 0.5)
        return result.x

    @staticmethod
    def _deviance(home, away, hs, as_, theta, n_teams: int) -> float:
        m, h, att, defn = theta[0], theta[1], theta[2:2 + n_teams], theta[2 + n_teams:]
        mu_h = np.exp(m + h + att[home] + defn[away])
        mu_a = np.exp(m + att[away] + defn[home])
        total = 0.0
        for y, mu in ((hs, mu_h), (as_, mu_a)):
            with np.errstate(divide="ignore", invalid="ignore"):
                term = np.where(y > 0, y * np.log(y / mu), 0.0) - (y - mu)
            total += 2.0 * float(np.sum(term))
        return total

    def _validate(self, games: Sequence[Game]) -> None:
        if len(games) < self.min_games:
            raise InsufficientData(f"AttackDefenceModel needs at least {self.min_games} games, got {len(games)}")
        for g in games:
            if not (np.isfinite(g[2]) and np.isfinite(g[3])) or g[2] < 0 or g[3] < 0:
                raise ValueError(f"invalid score in game {g}")
            if g[0] == g[1]:
                raise ValueError(f"a team cannot play itself: {g}")

    def choose_ridge(self, games: Sequence[Game]) -> float:
        """Expanding-window CV over the chronologically ordered `games`: lowest held-out deviance wins."""
        teams = sorted({g[0] for g in games} | {g[1] for g in games})
        index = {t: i for i, t in enumerate(teams)}
        n_games = len(games)
        folds = max(2, self.cv_folds)
        # fold k trains on the first (k+1)/(folds+1) of the games and tests on the next block
        cuts = [int(round(n_games * (k + 1) / (folds + 1))) for k in range(folds + 1)]
        scores = {}
        for ridge in self.ridge_grid:
            total, used = 0.0, 0
            for k in range(folds):
                train, test = games[:cuts[k]], games[cuts[k]:cuts[k + 1]]
                if len(train) < self.min_games or not test:
                    continue
                known = {t for g in train for t in g[:2]}
                test = [g for g in test if g[0] in known and g[1] in known]    # unseen teams carry no fold information
                if not test:
                    continue
                th = self._solve(*self._arrays(train, index), len(teams), ridge)
                total += self._deviance(*self._arrays(test, index), th, len(teams))
                used += len(test)
            if used:
                scores[float(ridge)] = total / used
        if not scores:
            raise InsufficientData("no usable cross-validation fold; supply `ridge` explicitly or more games")
        self.cv_scores = scores
        return min(scores, key=lambda r: scores[r])

    def fit(self, games: Sequence[Game]) -> "AttackDefenceModel":
        games = list(games)
        self._validate(games)
        ridge = self.ridge if self.ridge is not None else self.choose_ridge(games)
        self.teams = sorted({g[0] for g in games} | {g[1] for g in games})
        index = {t: i for i, t in enumerate(self.teams)}
        theta = self._solve(*self._arrays(games, index), len(self.teams), ridge)
        n = len(self.teams)
        self.log_base, self.log_home = float(theta[0]), float(theta[1])
        self.att, self.defn = theta[2:2 + n].copy(), theta[2 + n:].copy()
        self.ridge_used = float(ridge)
        counts: Dict[str, int] = {}
        for g in games:
            counts[g[0]] = counts.get(g[0], 0) + 1
            counts[g[1]] = counts.get(g[1], 0) + 1
        self.games_played = counts
        return self

    # --------------------------------------------------------------- prediction
    def knows(self, team: str) -> bool:
        return team in self.teams

    def expected(self, home: str, away: str, unknown: str = "refuse") -> Tuple[float, float]:
        """Expected (home, away) scores. An unknown team raises unless `unknown="average"` (strength 0 = league average)."""
        if not self.teams:
            raise FitFailed("AttackDefenceModel", "predict called before fit")
        if unknown not in ("refuse", "average"):
            raise ValueError("unknown must be 'refuse' or 'average'")
        missing = [t for t in (home, away) if t not in self.teams]
        if missing and unknown == "refuse":
            raise UnknownTeam(f"no fitted strength for {missing}")
        a_h = self.att[self.teams.index(home)] if home in self.teams else 0.0
        d_h = self.defn[self.teams.index(home)] if home in self.teams else 0.0
        a_a = self.att[self.teams.index(away)] if away in self.teams else 0.0
        d_a = self.defn[self.teams.index(away)] if away in self.teams else 0.0
        mu_h = float(np.exp(self.log_base + self.log_home + a_h + d_a))
        mu_a = float(np.exp(self.log_base + a_a + d_h))
        return mu_h, mu_a

    def league_means(self) -> Tuple[float, float]:
        """Expected (home, away) score for two average teams."""
        return float(np.exp(self.log_base + self.log_home)), float(np.exp(self.log_base))

    def factors(self) -> Tuple[Dict[str, float], Dict[str, float]]:
        """Multiplicative scoring and conceding factors relative to the league (1.0 = average)."""
        return ({t: float(np.exp(a)) for t, a in zip(self.teams, self.att)},
                {t: float(np.exp(d)) for t, d in zip(self.teams, self.defn)})
