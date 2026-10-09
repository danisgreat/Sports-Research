"""American football engine: a drive-by-drive scoring model with 0/2/3/6/7/8-point drives and key-number mass (DST-14)."""

from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import numpy as np
from scipy.optimize import least_squares
from scipy.stats import norm

from ..base import BaseSportEngine, collect_games
from ...common.contracts import ScoreDistribution
from ...common.errors import FitFailed, MissingInputs
from ...common.leagues import LeagueProfile
from ...common.strengths import AttackDefenceModel

MAX_SCORE = 80


@dataclass(frozen=True)
class DriveRules:
    """Scoring conventions that fix how a touchdown drive converts into 6, 7 or 8 points.

    These are reference values (extra point about 94%, two-point tries about 5% of touchdowns at roughly 48%);
    only touchdown and field-goal rates are fitted. A safety is an independent 2-point event.
    """
    extra_point: float = 0.94
    two_point_rate: float = 0.05
    two_point_success: float = 0.48
    safety: float = 0.012
    drives_mean: float = 11.0       # UNFITTED analyst reference: offensive drives per team
    drives_sd: float = 1.5


def drive_pmf(p_td: float, p_fg: float, rules: DriveRules) -> np.ndarray:
    """P(points on one drive) over 0..8: no score, safety (2), field goal (3), touchdown with 6, 7 or 8 points."""
    if p_td < 0 or p_fg < 0 or p_td + p_fg + rules.safety > 1.0:
        raise ValueError("drive outcome probabilities must be non-negative and sum to at most 1")
    pmf = np.zeros(9)
    pmf[2] = rules.safety
    pmf[3] = p_fg
    kick = 1.0 - rules.two_point_rate
    pmf[7] = p_td * kick * rules.extra_point
    pmf[6] = p_td * kick * (1.0 - rules.extra_point) + p_td * rules.two_point_rate * (1.0 - rules.two_point_success)
    pmf[8] = p_td * rules.two_point_rate * rules.two_point_success
    pmf[0] = 1.0 - pmf[1:].sum()
    return pmf


def drives_pmf(rules: DriveRules) -> Tuple[np.ndarray, np.ndarray]:
    support = np.arange(5, 19)
    edges = np.concatenate([[-np.inf], support[:-1] + 0.5, [np.inf]])
    weights = np.diff(norm.cdf(edges, loc=rules.drives_mean, scale=rules.drives_sd))
    return support, weights / weights.sum()


def team_points_pmf(p_td: float, p_fg: float, rules: DriveRules, size: int = MAX_SCORE + 1) -> np.ndarray:
    """Score distribution for one team: a mixture over the number of drives of the repeated convolution of the drive pmf."""
    support, weights = drives_pmf(rules)
    base = drive_pmf(p_td, p_fg, rules)
    out = np.zeros(size)
    current = np.zeros(size)
    current[0] = 1.0
    reached = 0
    for n in range(0, int(support.max()) + 1):
        if n >= support.min():
            out += weights[n - support.min()] * current
        nxt = np.convolve(current, base)[:size]
        nxt[size - 1] += np.convolve(current, base)[size:].sum() if len(np.convolve(current, base)) > size else 0.0
        current = nxt
        reached = n
    return out / out.sum()


def margin_weights(model_grid: np.ndarray, target_pmf: Dict[int, float], limit: int = 40, epsilon: float = 5e-4) -> np.ndarray:
    """Per-margin weights (index margin + limit) turning the model's margin pmf into the empirical one.

    Computed at a league-average matchup, the weights are the structural key-number uplift (3 and 7 are far likelier
    than independent drives produce, 0 is rarer because overtime resolves ties). They are capped to avoid noise.
    """
    size = model_grid.shape[0]
    h, a = np.meshgrid(np.arange(size), np.arange(model_grid.shape[1]), indexing="ij")
    idx = np.clip(h - a, -limit, limit) + limit
    model = np.bincount(idx.ravel(), weights=model_grid.ravel(), minlength=2 * limit + 1)
    target = np.array([target_pmf.get(m, 0.0) for m in range(-limit, limit + 1)])
    return np.clip((target + epsilon) / (model + epsilon), 0.1, 6.0)


def apply_margin_weights(grid: np.ndarray, weights: np.ndarray, limit: int = 40, rounds: int = 40, tolerance: float = 1e-6) -> np.ndarray:
    """Move the margin distribution to `weights` x model, keeping each team's score marginal (iterative proportional fitting).

    The target margin pmf is fixed once (the model's own margin pmf times the weights, normalised); each round rescales
    cells so the margin pmf matches it and then restores the row and column marginals.
    """
    size_h, size_a = grid.shape
    h, a = np.meshgrid(np.arange(size_h), np.arange(size_a), indexing="ij")
    idx = np.clip(h - a, -limit, limit) + limit
    n_margin = 2 * limit + 1
    row_target, col_target = grid.sum(axis=1), grid.sum(axis=0)
    margin_target = np.bincount(idx.ravel(), weights=grid.ravel(), minlength=n_margin) * weights
    margin_target /= margin_target.sum()
    out = grid.copy()
    for _ in range(rounds):
        current = np.bincount(idx.ravel(), weights=out.ravel(), minlength=n_margin)
        factor = np.divide(margin_target, current, out=np.zeros_like(current), where=current > 0)
        out = out * factor[idx]
        rows = out.sum(axis=1)
        out = out * np.divide(row_target, rows, out=np.zeros_like(rows), where=rows > 0)[:, None]
        cols = out.sum(axis=0)
        out = out * np.divide(col_target, cols, out=np.zeros_like(cols), where=cols > 0)[None, :]
        error = float(np.abs(np.bincount(idx.ravel(), weights=out.ravel(), minlength=n_margin) - margin_target).max())
        if error < tolerance:
            break
    return out / out.sum()


class NFLEngine(BaseSportEngine):
    """Predictive engine for American football (NFL, NCAA).

    Expected points per team come from opponent-adjusted strengths. A league-level drive structure (touchdown and
    field-goal rates at league average) is solved so the score distribution reproduces the league's per-team mean and
    variance; each game scales those rates to its expected points. Key margins (3, 6, 7, 10, 14) then emerge from
    the discrete scoring instead of a smoothed normal. Independent drives still under-produce the margin-3 spike
    (overtime and late-game clock management create dependence between the teams), so when the league profile carries
    an empirical margin distribution the grid is reweighted to it at the league-average matchup (`margin_weights`)
    and each team's score marginal is restored.
    """

    def __init__(self, league: Optional[LeagueProfile] = None, unknown_team_policy: str = "refuse",
                 rules: Optional[DriveRules] = None, team_sd: Optional[float] = None, margin_pmf: Optional[Dict[int, float]] = None):
        super().__init__("american_football", league, unknown_team_policy)
        self.rules = rules or DriveRules()
        self.team_sd = team_sd
        self.margin_pmf = margin_pmf
        self.model: Optional[AttackDefenceModel] = None
        self._structures: Dict[Tuple[Any, ...], Any] = {}

    def fit(self, train_data: Any) -> "NFLEngine":
        games = collect_games(train_data, ("home_score", "home_points"), ("away_score", "away_points"))
        self.model = AttackDefenceModel().fit(games)
        residuals = []
        for home, away, hs, as_ in games:
            mu_h, mu_a = self.model.expected(home, away)
            residuals += [hs - mu_h, as_ - mu_a]
        self.team_sd = float(np.sqrt(np.mean(np.square(residuals))))
        self.is_fitted = True
        return self

    # ------------------------------------------------------------------- inputs
    def _expected_points(self, ctx: Dict[str, Any]) -> Tuple[float, float]:
        if ctx.get("home_expected_points") is not None and ctx.get("away_expected_points") is not None:
            return float(ctx["home_expected_points"]), float(ctx["away_expected_points"])
        home, away = ctx.get("home_team"), ctx.get("away_team")
        if self.is_fitted and self.model is not None:
            for team in (home, away):
                if not self.model.knows(team):
                    self._warn(f"unknown team {team!r}: league-average strength used; uncertainty not modelled")
            return self.model.expected(home, away, unknown="average" if self.unknown_team_policy == "league_average" else "refuse")
        self._need_fit_or_profile()
        raise MissingInputs("american football: pass home_expected_points/away_expected_points, or fit the engine")

    def _team_sd(self, ctx: Dict[str, Any]) -> float:
        if ctx.get("team_sd") is not None:
            return float(ctx["team_sd"])
        if self.team_sd is not None:
            return float(self.team_sd)
        if self.league is not None:
            return float(self.league.team_sd)
        raise MissingInputs("american football: team_sd is required (pass it, fit the engine, or use a league profile)")

    def _structure(self, mean_points: float, team_sd: float) -> Tuple[float, float]:
        """(touchdown rate, field-goal rate) per drive for a team averaging `mean_points` with the given score SD."""
        key = (round(mean_points, 3), round(team_sd, 3), self.rules.drives_mean, self.rules.drives_sd, self.rules.safety,
               self.rules.extra_point, self.rules.two_point_rate, self.rules.two_point_success)
        if key in self._structures:
            return self._structures[key]
        values = np.arange(MAX_SCORE + 1)

        def residuals(x):
            pmf = team_points_pmf(x[0], x[1], self.rules)
            mean = float(values @ pmf)
            var = float(((values - mean) ** 2) @ pmf)
            return np.array([mean / mean_points - 1.0, var / team_sd ** 2 - 1.0])

        fit = least_squares(residuals, [0.2, 0.15], bounds=([0.02, 0.0], [0.6, 0.45]), xtol=1e-12, ftol=1e-12, diff_step=1e-4)
        if float(np.max(np.abs(fit.fun))) > 0.01:
            raise FitFailed("NFLEngine", f"drive structure did not reach its targets (worst relative error {np.max(np.abs(fit.fun)):.4f})")
        self._structures[key] = (float(fit.x[0]), float(fit.x[1]))
        return self._structures[key]

    def _margin_weights(self, margin_pmf, league_mean: float, team_sd: float) -> np.ndarray:
        """Key-number weights from a league-average matchup (home edge from the margin distribution's own mean)."""
        key = ("w", round(league_mean, 3), round(team_sd, 3), round(sum(m * p for m, p in margin_pmf.items()), 5))
        if key in self._structures:
            return self._structures[key]
        edge = sum(m * p for m, p in margin_pmf.items())
        td0, fg0 = self._structure(league_mean, team_sd)
        values = np.arange(MAX_SCORE + 1)
        base = team_points_pmf(td0, fg0, self.rules)
        base_mean = float(values @ base)
        pmfs = []
        for target in (league_mean + edge / 2.0, league_mean - edge / 2.0):
            td, fg = td0 * target / base_mean, fg0 * target / base_mean
            for _ in range(20):
                pmf = team_points_pmf(float(np.clip(td, 0.01, 0.6)), float(np.clip(fg, 0.0, 0.45)), self.rules)
                got = float(values @ pmf)
                if abs(got / target - 1.0) < 1e-4:
                    break
                td, fg = td * target / got, fg * target / got
            pmfs.append(pmf)
        weights = margin_weights(np.outer(pmfs[0], pmfs[1]), dict(margin_pmf))
        self._structures[key] = weights
        return weights

    # --------------------------------------------------------------- prediction
    def predict_distribution(self, match_context: Dict[str, Any], endpoint: str = "full_game") -> ScoreDistribution:
        """Final score including overtime as recorded."""
        if endpoint != "full_game":
            raise ValueError("the NFL engine settles on the recorded final score")
        mean_h, mean_a = self._expected_points(match_context)
        multiplier = float(match_context.get("scoring_multiplier", 1.0))
        mean_h, mean_a = mean_h * multiplier, mean_a * multiplier
        team_sd = self._team_sd(match_context)
        league_mean = self.league.mean_team_score if self.league is not None else 0.5 * (mean_h + mean_a)
        td0, fg0 = self._structure(league_mean, team_sd)
        base = team_points_pmf(td0, fg0, self.rules)
        values = np.arange(MAX_SCORE + 1)
        base_mean = float(values @ base)
        pmfs, rates = [], []
        for target in (mean_h, mean_a):
            scale = target / base_mean
            td, fg = float(np.clip(td0 * scale, 0.01, 0.6)), float(np.clip(fg0 * scale, 0.0, 0.45))
            # re-solve the single scale so the mean is exact after clipping
            for _ in range(20):
                pmf = team_points_pmf(td, fg, self.rules)
                got = float(values @ pmf)
                if abs(got / target - 1.0) < 1e-4:
                    break
                td, fg = float(np.clip(td * target / got, 0.01, 0.6)), float(np.clip(fg * target / got, 0.0, 0.45))
            pmfs.append(pmf)
            rates.append((td, fg))
        grid = np.outer(pmfs[0], pmfs[1])
        grid /= grid.sum()
        calibrated = False
        margin_pmf = match_context.get("margin_pmf", self.margin_pmf if self.margin_pmf is not None else
                                       (self.league.margin_pmf if self.league is not None else None))
        if margin_pmf is not None and match_context.get("margin_calibration", True):
            weights = self._margin_weights(margin_pmf, league_mean, team_sd)
            grid = apply_margin_weights(grid, weights)
            calibrated = True
        return ScoreDistribution(grid, values, values, endpoint="full_game",
                                 metadata={"model": "nfl_drive_convolution", "td_rate_home": rates[0][0], "fg_rate_home": rates[0][1],
                                           "td_rate_away": rates[1][0], "fg_rate_away": rates[1][1], "drives_mean": self.rules.drives_mean, "margin_calibrated": calibrated,
                                           "warnings": self._take_warnings()})
