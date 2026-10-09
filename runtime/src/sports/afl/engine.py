"""AFL engine: scoring shots with negative dependence, goal conversion, and period fractions (DST-12)."""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from scipy.optimize import least_squares
from scipy.stats import binom

from ..base import BaseSportEngine, _first
from ...common.contracts import ScoreDistribution
from ...common.counts import cmp_pmf, count_moments, split_total_grid
from ...common.errors import FitFailed, InsufficientData, MissingInputs, finite_score
from ...common.leagues import LeagueProfile
from ...common.strengths import AttackDefenceModel

MAX_SHOTS = 55          # per team
MAX_POINTS = 6 * 40 + 20


@dataclass(frozen=True)
class AFLStructure:
    nu: float
    concentration: float


def points_matrix(conversion: float) -> np.ndarray:
    """M[n, p] = P(points = p | n scoring shots): each shot is a goal (6) with probability `conversion`, else a behind (1)."""
    matrix = np.zeros((MAX_SHOTS + 1, MAX_POINTS + 1))
    for n in range(MAX_SHOTS + 1):
        goals = binom.pmf(np.arange(n + 1), n, conversion)
        for g, mass in enumerate(goals):
            p = n + 5 * g                                   # 6 g + (n - g)
            if p <= MAX_POINTS:
                matrix[n, p] += mass
        matrix[n] /= matrix[n].sum()
    return matrix


def points_grid(shots_grid: np.ndarray, conv_home: float, conv_away: float) -> np.ndarray:
    grid = points_matrix(conv_home).T @ shots_grid @ points_matrix(conv_away)
    return grid / grid.sum()


class AFLEngine(BaseSportEngine):
    """Predictive engine for Australian rules football (AFL, AFLW).

    Scoring shots come from opponent-adjusted strengths and share an under- or over-dispersed total that is split by a
    beta-binomial (teams trade possession, so scores correlate at about -0.3). Each shot is a goal with the team's
    conversion rate. Dispersion and split are solved so that points reproduce the total and margin SDs.
    """

    def __init__(self, league: Optional[LeagueProfile] = None, unknown_team_policy: str = "refuse",
                 conversion: Optional[float] = None, total_sd: Optional[float] = None, margin_sd: Optional[float] = None):
        super().__init__("afl", league, unknown_team_policy)
        self.conversion = conversion
        self.total_sd = total_sd
        self.margin_sd = margin_sd
        self.model: Optional[AttackDefenceModel] = None
        self.team_conversion: Dict[str, float] = {}
        self._structures: Dict[Tuple[float, ...], AFLStructure] = {}

    def fit(self, train_data: Any) -> "AFLEngine":
        if hasattr(train_data, "to_dict") and hasattr(train_data, "columns"):
            records = train_data.to_dict("records")
        elif isinstance(train_data, (list, tuple)):
            records = list(train_data)
        else:
            raise ValueError("train_data must be a list of game dicts or a DataFrame; an engine is never 'fitted' on nothing")
        games: List[Tuple[str, str, float, float]] = []
        goals_for: Dict[str, float] = {}
        shots_for: Dict[str, float] = {}
        all_goals = all_shots = 0.0
        points = []
        for index, m in enumerate(records):
            home, away = _first(m, ("home_team", "home")), _first(m, ("away_team", "away"))
            if home is None or away is None:
                raise MissingInputs(f"training record {index} lacks home/away team names")
            sides = []
            for side in ("home", "away"):
                goals = finite_score(m, f"{side}_goals")
                behinds = finite_score(m, f"{side}_behinds")
                sides.append((goals, goals + behinds))
            games.append((str(home), str(away), sides[0][1], sides[1][1]))
            for team, (goals, shots) in ((str(home), sides[0]), (str(away), sides[1])):
                goals_for[team] = goals_for.get(team, 0.0) + goals
                shots_for[team] = shots_for.get(team, 0.0) + shots
                all_goals += goals
                all_shots += shots
            points.append((6 * sides[0][0] + (sides[0][1] - sides[0][0]), 6 * sides[1][0] + (sides[1][1] - sides[1][0])))
        if len(games) < 100:
            raise InsufficientData(f"need at least 100 games to fit the AFL engine, got {len(games)}")
        self.model = AttackDefenceModel().fit(games)
        self.conversion = all_goals / all_shots
        # team conversion shrunk toward the league rate in proportion to the shots observed (no fixed 70/30 blend)
        k = 150.0
        self.team_conversion = {t: float((goals_for[t] + k * self.conversion) / (shots_for[t] + k)) for t in shots_for}
        total_res, margin_res = [], []
        for (home, away, _, _), (hp, ap) in zip(games, points):
            mu_h, mu_a = self.model.expected(home, away)
            eh = 6 * self.conversion * mu_h + (1 - self.conversion) * mu_h
            ea = 6 * self.conversion * mu_a + (1 - self.conversion) * mu_a
            total_res.append((hp + ap) - (eh + ea))
            margin_res.append((hp - ap) - (eh - ea))
        self.total_sd = float(np.sqrt(np.mean(np.square(total_res))))
        self.margin_sd = float(np.sqrt(np.mean(np.square(margin_res))))
        self.is_fitted = True
        return self

    # ------------------------------------------------------------------- inputs
    def _shots_means(self, ctx: Dict[str, Any]) -> Tuple[float, float]:
        if ctx.get("home_expected_shots") is not None and ctx.get("away_expected_shots") is not None:
            return float(ctx["home_expected_shots"]), float(ctx["away_expected_shots"])
        if self.is_fitted and self.model is not None:
            home, away = self._teams(ctx)
            for team in (home, away):
                if not self.model.knows(team):
                    self._warn(f"unknown team {team!r}: league-average strength used; uncertainty not modelled")
            return self.model.expected(home, away, unknown="average" if self.unknown_team_policy == "league_average" else "refuse")
        self._need_fit_or_profile()
        raise MissingInputs("afl: pass home_expected_shots/away_expected_shots, or fit the engine")

    def _conversions(self, ctx: Dict[str, Any]) -> Tuple[float, float]:
        league = self.conversion if self.conversion is not None else (
            self.league.extras.get("goal_conversion") if self.league is not None else None)
        if league is None:
            raise MissingInputs("afl: goal conversion is required (fit the engine, pass it, or use a league profile)")
        home = ctx.get("home_conversion_rate")
        away = ctx.get("away_conversion_rate")
        if home is None:
            home = self.team_conversion.get(str(ctx.get("home_team")), league)
        if away is None:
            away = self.team_conversion.get(str(ctx.get("away_team")), league)
        return float(home), float(away)

    def _targets(self, ctx: Dict[str, Any]) -> Tuple[float, float]:
        total_sd = ctx.get("total_sd", self.total_sd if self.total_sd is not None else (self.league.total_sd if self.league else None))
        margin_sd = ctx.get("margin_sd", self.margin_sd if self.margin_sd is not None else (self.league.margin_sd if self.league else None))
        if total_sd is None or margin_sd is None:
            raise MissingInputs("afl: total_sd and margin_sd are required (pass them, fit the engine, or use a league profile)")
        return float(total_sd), float(margin_sd)

    def _structure(self, mean_h, mean_a, conv_h, conv_a, total_sd, margin_sd) -> AFLStructure:
        key = tuple(round(v, 4) for v in (mean_h, mean_a, conv_h, conv_a, total_sd, margin_sd))
        if key in self._structures:
            return self._structures[key]

        def residuals(x):
            shots = split_total_grid(mean_h, mean_a, 0.0, float(np.exp(x[1])), MAX_SHOTS + 1,
                                     total_pmf=cmp_pmf(mean_h + mean_a, x[0], 2 * MAX_SHOTS + 2))
            _, _, vt, vm = count_moments(points_grid(shots, conv_h, conv_a))
            return np.array([vt / total_sd ** 2 - 1.0, vm / margin_sd ** 2 - 1.0])

        fit = least_squares(residuals, [1.0, np.log(10.0)], bounds=([0.2, np.log(0.5)], [8.0, np.log(1e5)]), xtol=1e-10, ftol=1e-10, diff_step=1e-3)
        if float(np.max(np.abs(fit.fun))) > 0.01:
            raise FitFailed("AFLEngine", f"score spread did not reach its targets (worst relative error {np.max(np.abs(fit.fun)):.4f})")
        structure = AFLStructure(nu=float(fit.x[0]), concentration=float(np.exp(fit.x[1])))
        self._structures[key] = structure
        return structure

    # --------------------------------------------------------------- prediction
    def _distribution(self, ctx: Dict[str, Any], fraction: float, endpoint: str) -> ScoreDistribution:
        mean_h, mean_a = self._shots_means(ctx)
        multiplier = float(ctx.get("scoring_multiplier", 1.0))                       # explicit regime adjustment (finals compression)
        mean_h, mean_a = mean_h * multiplier, mean_a * multiplier
        conv_h, conv_a = self._conversions(ctx)
        total_sd, margin_sd = self._targets(ctx)
        structure = self._structure(mean_h, mean_a, conv_h, conv_a, total_sd, margin_sd)
        shots = split_total_grid(mean_h * fraction, mean_a * fraction, 0.0, structure.concentration, MAX_SHOTS + 1,
                                 total_pmf=cmp_pmf((mean_h + mean_a) * fraction, structure.nu, 2 * MAX_SHOTS + 2))
        grid = points_grid(shots, conv_h, conv_a)
        support = np.arange(MAX_POINTS + 1)
        return ScoreDistribution(grid, support, support, endpoint=endpoint,
                                 metadata={"model": "afl_shots_split", "shots_home": mean_h, "shots_away": mean_a, "conversion_home": conv_h,
                                           "conversion_away": conv_a, "nu": structure.nu, "concentration": structure.concentration,
                                           "period_fraction": fraction, "warnings": self._take_warnings()})

    def predict_distribution(self, match_context: Dict[str, Any], endpoint: str = "full_game") -> ScoreDistribution:
        if endpoint != "full_game":
            raise ValueError("the AFL engine settles on the final score; use predict_period for quarter or half rows")
        return self._distribution(match_context, 1.0, "full_game")

    def predict_period(self, match_context: Dict[str, Any], period_fraction: float) -> ScoreDistribution:
        """Quarter or half rows: the same structure with shots scaled to `period_fraction` of the match.

        The archive holds no quarter scores, so the fraction (0.5 for a half, 0.25 for a quarter) is an explicit analyst
        input and the period spread is the full-match structure scaled, not a fitted period model.
        """
        if not 0.0 < period_fraction < 1.0:
            raise ValueError("period_fraction must lie in (0, 1)")
        return self._distribution(match_context, float(period_fraction), f"period_{period_fraction:g}")
