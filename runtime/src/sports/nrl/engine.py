"""Rugby league engine: tries with negative home/away dependence, kicking, and a half-time distribution (DST-12)."""

from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import numpy as np
from scipy.optimize import least_squares
from scipy.stats import binom, poisson

from ..base import BaseSportEngine, _first
from ...common.contracts import ScoreDistribution
from ...common.counts import cmp_pmf, count_moments, split_total_grid
from ...common.errors import FitFailed, InsufficientData, MissingInputs, finite_score
from ...common.leagues import LeagueProfile
from ...common.strengths import AttackDefenceModel

MAX_TRIES = 14          # per team
MAX_POINTS = 120


@dataclass(frozen=True)
class NRLKicking:
    """Points per try beyond the four: goals (conversions + penalty goals, 2 each) and field goals (1 each)."""
    conversion_rate: float        # P(a try is converted)
    penalty_goals: float          # expected penalty goals per team per game
    field_goals: float            # expected field goals per team per game


@dataclass(frozen=True)
class NRLStructure:
    nu: float                     # Conway-Maxwell-Poisson dispersion of total tries (> 1: under-dispersed, as in rugby league)
    concentration: float          # beta-binomial concentration of the home share of tries (low = strongly negative dependence)


def points_matrix(kicking: NRLKicking, conversion_rate: Optional[float] = None) -> np.ndarray:
    """M[t, p] = P(points = p | t tries) with points = 4t + 2 (Bin(t, c) + Poisson(penalty goals)) + Poisson(field goals)."""
    c = kicking.conversion_rate if conversion_rate is None else conversion_rate
    pg = poisson.pmf(np.arange(0, 12), kicking.penalty_goals)
    fg = poisson.pmf(np.arange(0, 5), kicking.field_goals)
    matrix = np.zeros((MAX_TRIES + 1, MAX_POINTS + 1))
    for t in range(MAX_TRIES + 1):
        goals = np.convolve(binom.pmf(np.arange(t + 1), t, c), pg)
        pts = np.zeros(MAX_POINTS + 1)
        for g, pg_mass in enumerate(goals):
            for f, f_mass in enumerate(fg):
                p = 4 * t + 2 * g + f
                if p <= MAX_POINTS:
                    pts[p] += pg_mass * f_mass
        matrix[t] = pts / pts.sum()
    return matrix


def points_grid(tries_grid: np.ndarray, kicking: NRLKicking, conv_home: Optional[float] = None, conv_away: Optional[float] = None) -> np.ndarray:
    mh, ma = points_matrix(kicking, conv_home), points_matrix(kicking, conv_away)
    grid = mh.T @ tries_grid @ ma
    return grid / grid.sum()


class NRLEngine(BaseSportEngine):
    """Predictive engine for rugby league (NRL, Super League).

    Tries come from opponent-adjusted strengths; the two teams' tries share an under-dispersed (Conway-Maxwell-Poisson)
    total split by a beta-binomial, so the strong negative home/away score correlation (about -0.3) is reproduced.
    The dispersion and the split concentration are solved so that the modelled points reproduce the total and margin SDs.
    """

    def __init__(self, league: Optional[LeagueProfile] = None, unknown_team_policy: str = "refuse",
                 kicking: Optional[NRLKicking] = None, total_sd: Optional[float] = None, margin_sd: Optional[float] = None,
                 first_half_share: Optional[float] = None):
        super().__init__("nrl", league, unknown_team_policy)
        self.kicking = kicking
        self.total_sd = total_sd
        self.margin_sd = margin_sd
        self.first_half_share = first_half_share
        self.model: Optional[AttackDefenceModel] = None
        self._structures: Dict[Tuple[float, ...], NRLStructure] = {}

    # ------------------------------------------------------------------ fitting
    def fit(self, train_data: Any) -> "NRLEngine":
        if hasattr(train_data, "to_dict") and hasattr(train_data, "columns"):
            records = train_data.to_dict("records")
        elif isinstance(train_data, (list, tuple)):
            records = list(train_data)
        else:
            raise ValueError("train_data must be a list of game dicts or a DataFrame; an engine is never 'fitted' on nothing")
        games, tries, goals, extra_points = [], [], [], []
        for index, m in enumerate(records):
            home, away = _first(m, ("home_team", "home")), _first(m, ("away_team", "away"))
            if home is None or away is None:
                raise MissingInputs(f"training record {index} lacks home/away team names")
            row = []
            for side in ("home", "away"):
                t = finite_score(m, f"{side}_tries")
                g = finite_score(m, f"{side}_goals", f"{side}_conversions")
                pts = finite_score(m, f"{side}_score", f"{side}_points")
                fg = pts - 4 * t - 2 * g
                if fg < 0:
                    raise ValueError(f"training record {index}: {side} points {pts} are fewer than 4*tries + 2*goals")
                row.append((t, g, fg))
            games.append((str(home), str(away), row[0][0], row[1][0]))
            for t, g, fg in row:
                tries.append(t)
                goals.append(g)
                extra_points.append(fg)
        if len(games) < 100:
            raise InsufficientData(f"need at least 100 games to fit rugby league kicking and spread, got {len(games)}")
        self.model = AttackDefenceModel().fit(games)
        tries_a, goals_a = np.array(tries), np.array(goals)
        c = float(np.clip(np.cov(tries_a, goals_a)[0, 1] / tries_a.var(ddof=1), 0.5, 0.99))      # goals rise with tries at the conversion rate
        pg = float(max(goals_a.mean() - c * tries_a.mean(), 0.0))
        self.kicking = NRLKicking(conversion_rate=c, penalty_goals=pg, field_goals=float(np.mean(extra_points)))
        total_res, margin_res = [], []
        for (home, away, _, _), rec in zip(games, records):
            mu_h, mu_a = self.model.expected(home, away)
            exp_h = 4 * mu_h + 2 * (c * mu_h + pg) + self.kicking.field_goals
            exp_a = 4 * mu_a + 2 * (c * mu_a + pg) + self.kicking.field_goals
            hs, as_ = finite_score(rec, "home_score", "home_points"), finite_score(rec, "away_score", "away_points")
            total_res.append((hs + as_) - (exp_h + exp_a))
            margin_res.append((hs - as_) - (exp_h - exp_a))
        self.total_sd = float(np.sqrt(np.mean(np.square(total_res))))
        self.margin_sd = float(np.sqrt(np.mean(np.square(margin_res))))
        self.is_fitted = True
        return self

    # ------------------------------------------------------------------- inputs
    def _kicking(self, ctx: Dict[str, Any]) -> NRLKicking:
        if self.kicking is None:
            raise MissingInputs("rugby league: pass an NRLKicking (conversion rate, penalty goals, field goals) or fit the engine on "
                                "try/goal/score records; the archive profile cannot separate penalty goals from conversions")
        return self.kicking

    def _tries_means(self, ctx: Dict[str, Any]) -> Tuple[float, float]:
        if ctx.get("home_expected_tries") is not None and ctx.get("away_expected_tries") is not None:
            return float(ctx["home_expected_tries"]), float(ctx["away_expected_tries"])
        if self.is_fitted and self.model is not None:
            home, away = self._teams(ctx)
            for team in (home, away):
                if not self.model.knows(team):
                    self._warn(f"unknown team {team!r}: league-average strength used; uncertainty not modelled")
            return self.model.expected(home, away, unknown="average" if self.unknown_team_policy == "league_average" else "refuse")
        self._need_fit_or_profile()
        raise MissingInputs("rugby league: pass home_expected_tries/away_expected_tries, or fit the engine")

    def _targets(self, ctx: Dict[str, Any]) -> Tuple[float, float]:
        total_sd = ctx.get("total_sd", self.total_sd if self.total_sd is not None else (self.league.total_sd if self.league else None))
        margin_sd = ctx.get("margin_sd", self.margin_sd if self.margin_sd is not None else (self.league.margin_sd if self.league else None))
        if total_sd is None or margin_sd is None:
            raise MissingInputs("rugby league: total_sd and margin_sd are required (pass them, fit the engine, or use a league profile)")
        return float(total_sd), float(margin_sd)

    # ---------------------------------------------------------------- structure
    def _structure(self, mean_h: float, mean_a: float, kicking: NRLKicking, total_sd: float, margin_sd: float) -> NRLStructure:
        key = (round(mean_h, 4), round(mean_a, 4), round(kicking.conversion_rate, 4), round(kicking.penalty_goals, 4),
               round(kicking.field_goals, 4), round(total_sd, 4), round(margin_sd, 4))
        if key in self._structures:
            return self._structures[key]

        def tries_grid(nu, log_kappa, scale=1.0):
            return split_total_grid(mean_h * scale, mean_a * scale, 0.0, float(np.exp(log_kappa)), MAX_TRIES + 1,
                                    total_pmf=cmp_pmf((mean_h + mean_a) * scale, nu, 2 * MAX_TRIES + 2))

        def residuals(x):
            _, _, vt, vm = count_moments(points_grid(tries_grid(x[0], x[1]), kicking))
            return np.array([vt / total_sd ** 2 - 1.0, vm / margin_sd ** 2 - 1.0])

        fit = least_squares(residuals, [1.5, np.log(10.0)], bounds=([0.3, np.log(0.5)], [6.0, np.log(1e5)]), xtol=1e-10, ftol=1e-10, diff_step=1e-3)
        if float(np.max(np.abs(fit.fun))) > 0.01:
            raise FitFailed("NRLEngine", f"score spread did not reach its targets (worst relative error {np.max(np.abs(fit.fun)):.4f})")
        structure = NRLStructure(nu=float(fit.x[0]), concentration=float(np.exp(fit.x[1])))
        self._structures[key] = structure
        return structure

    # --------------------------------------------------------------- prediction
    def _distribution(self, ctx: Dict[str, Any], scale: float, endpoint: str) -> ScoreDistribution:
        mean_h, mean_a = self._tries_means(ctx)
        multiplier = float(ctx.get("scoring_multiplier", 1.0))                 # explicit regime adjustment (finals compression, ...)
        mean_h, mean_a = mean_h * multiplier, mean_a * multiplier
        kicking = self._kicking(ctx)
        total_sd, margin_sd = self._targets(ctx)
        base_h, base_a = (mean_h, mean_a)
        structure = self._structure(base_h, base_a, kicking, total_sd, margin_sd)
        conv_h = float(ctx["home_goal_kicker_accuracy"]) if ctx.get("home_goal_kicker_accuracy") is not None else None
        conv_a = float(ctx["away_goal_kicker_accuracy"]) if ctx.get("away_goal_kicker_accuracy") is not None else None
        part = NRLKicking(kicking.conversion_rate, kicking.penalty_goals * scale, kicking.field_goals * scale)
        tries = split_total_grid(mean_h * scale, mean_a * scale, 0.0, structure.concentration, MAX_TRIES + 1,
                                 total_pmf=cmp_pmf((mean_h + mean_a) * scale, structure.nu, 2 * MAX_TRIES + 2))
        grid = points_grid(tries, part, conv_h, conv_a)
        support = np.arange(MAX_POINTS + 1)
        return ScoreDistribution(grid, support, support, endpoint=endpoint,
                                 metadata={"model": "nrl_tries_split", "tries_mean_home": mean_h, "tries_mean_away": mean_a,
                                           "nu": structure.nu, "concentration": structure.concentration,
                                           "period_scale": scale, "warnings": self._take_warnings()})

    def predict_distribution(self, match_context: Dict[str, Any], endpoint: str = "full_game") -> ScoreDistribution:
        """Final score including any golden point (as the archive records it)."""
        if endpoint != "full_game":
            raise ValueError("the rugby league engine settles on the recorded final score (golden point included)")
        return self._distribution(match_context, 1.0, "full_game")

    def predict_halftime(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Half-time score: the same tries structure scaled to the first half's share of points."""
        share = match_context.get("first_half_share", self.first_half_share)
        if share is None and self.league is not None and "first_half_points_share" in self.league.extras:
            share = self.league.extras["first_half_points_share"]
        if share is None:
            raise MissingInputs("rugby league: first_half_share is required for half-time rows (pass it or use a league profile)")
        return self._distribution(match_context, float(share), "first_half")
