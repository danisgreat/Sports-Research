"""NHL predictive engine: opponent-adjusted goal rates, goalie adjustment, late-game state model and a rules-correct OT/SO endpoint."""

from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional

import numpy as np
from scipy.stats import poisson

from ..base import BaseSportEngine, collect_games
from ...common.contracts import ScoreDistribution
from ...common.endpoints import HockeyOvertime, fit_ot_multiplier, hockey_full_game
from ...common.errors import MissingInputs, NotFitted
from ...common.leagues import LeagueProfile
from ...common.strengths import AttackDefenceModel

MAX_GOALS = 14


@dataclass(frozen=True)
class HockeyLateGame:
    """Goalie-pull and empty-net dynamics for the last minutes of regulation (DST-10).

    The trailing team pulls its goalie once the time remaining falls to `pull_minutes_by_deficit[deficit]`
    (a deficit with no entry never pulls). While pulled, the trailing team scores at `pulled_scoring_multiplier`
    times its normal rate and the leader scores into the empty net at `empty_net_rate_per_minute`.
    These values must be fitted on play-by-play before they are relied on; `ILLUSTRATIVE` is an unfitted
    scenario for mechanics and sensitivity analysis only.
    """
    pull_minutes_by_deficit: Mapping[int, float]
    pulled_scoring_multiplier: float
    empty_net_rate_per_minute: float
    step_minutes: float = 0.25

    ILLUSTRATIVE = None  # assigned below the class body


HockeyLateGame.ILLUSTRATIVE = HockeyLateGame(pull_minutes_by_deficit={1: 1.75, 2: 3.0}, pulled_scoring_multiplier=2.0,
                                             empty_net_rate_per_minute=0.30)


def late_game_grid(lambda_home: float, lambda_away: float, late: HockeyLateGame, max_goals: int = MAX_GOALS) -> np.ndarray:
    """Regulation score grid with the final minutes simulated step by step under goalie-pull dynamics."""
    horizon = max(late.pull_minutes_by_deficit.values())
    steps = int(round(horizon / late.step_minutes))
    early_minutes = 60.0 - steps * late.step_minutes
    grid = np.outer(poisson.pmf(np.arange(max_goals + 1), lambda_home * early_minutes / 60.0),
                    poisson.pmf(np.arange(max_goals + 1), lambda_away * early_minutes / 60.0))
    grid /= grid.sum()
    h_idx, a_idx = np.meshgrid(np.arange(max_goals + 1), np.arange(max_goals + 1), indexing="ij")
    deficit = h_idx - a_idx                                            # positive: home leads
    for step in range(steps):
        remaining = horizon - step * late.step_minutes                  # minutes left at the start of this step
        rate_h = np.full(grid.shape, lambda_home / 60.0)
        rate_a = np.full(grid.shape, lambda_away / 60.0)
        for lead, minutes in late.pull_minutes_by_deficit.items():
            if remaining <= minutes:
                away_pulled, home_pulled = deficit == lead, deficit == -lead
                rate_a = np.where(away_pulled, rate_a * late.pulled_scoring_multiplier, rate_a)
                rate_h = np.where(away_pulled, late.empty_net_rate_per_minute, rate_h)
                rate_h = np.where(home_pulled, rate_h * late.pulled_scoring_multiplier, rate_h)
                rate_a = np.where(home_pulled, late.empty_net_rate_per_minute, rate_a)
        p_h = 1.0 - np.exp(-rate_h * late.step_minutes)
        p_a = 1.0 - np.exp(-rate_a * late.step_minutes)
        new = grid * (1 - p_h) * (1 - p_a)
        new[1:, :] += (grid * p_h * (1 - p_a))[:-1, :]
        new[:, 1:] += (grid * (1 - p_h) * p_a)[:, :-1]
        new[1:, 1:] += (grid * p_h * p_a)[:-1, :-1]
        new[-1, :] += (grid * p_h * (1 - p_a))[-1, :]                  # mass at the cap stays at the cap
        new[:, -1] += (grid * (1 - p_h) * p_a)[:, -1]
        new[-1, -1] += (grid * p_h * p_a)[-1, -1]
        grid = new
    return grid / grid.sum()


class NHLEngine(BaseSportEngine):
    """Predictive engine for ice hockey (NHL, KHL, SHL).

    fit(games):            opponent-adjusted goal rates by chronological-CV ridge (DST-05).
    late_game:             optional `HockeyLateGame` (None = plain regulation Poisson).
    predict_distribution:  endpoint "regulation" (60 minutes) or "full_game" (OT then shootout; DST-02).
    """

    def __init__(self, league: Optional[LeagueProfile] = None, unknown_team_policy: str = "refuse",
                 late_game: Optional[HockeyLateGame] = None, overtime: Optional[HockeyOvertime] = None):
        super().__init__("nhl", league, unknown_team_policy)
        self.late_game = late_game
        self.overtime = overtime
        self.model: Optional[AttackDefenceModel] = None

    def fit(self, train_data: Any) -> "NHLEngine":
        games = collect_games(train_data, ("home_goals", "home_score"), ("away_goals", "away_score"))
        self.model = AttackDefenceModel().fit(games)
        self.is_fitted = True
        return self

    # ------------------------------------------------------------------ inputs
    def overtime_rule(self, playoffs: bool = False) -> HockeyOvertime:
        """The overtime rule: explicit, else derived from the league profile's archive rates."""
        if self.overtime is not None:
            return self.overtime
        if self.league is None:
            raise MissingInputs("nhl: full_game endpoint needs an explicit HockeyOvertime rule or a league profile")
        if playoffs:
            return HockeyOvertime(ot_minutes=None)
        m = fit_ot_multiplier(self.league.mean_total, self.league.extra("overtime_decided_before_shootout"), 5.0)
        return HockeyOvertime(ot_minutes=5.0, ot_rate_multiplier=m, shootout_home_share=self.league.extra("shootout_home_share"))

    def _expected_goals(self, ctx: Dict[str, Any]):
        if ctx.get("home_xg") is not None and ctx.get("away_xg") is not None:
            return float(ctx["home_xg"]), float(ctx["away_xg"])
        if ctx.get("home_xg") is not None or ctx.get("away_xg") is not None:
            raise MissingInputs("nhl: give both home_xg and away_xg, or neither")
        home, away = ctx.get("home_team"), ctx.get("away_team")
        if self.is_fitted and self.model is not None:
            unknown = "average" if self.unknown_team_policy == "league_average" else "refuse"
            for team in (home, away):
                if not self.model.knows(team):
                    self._warn(f"unknown team {team!r}: league-average strength used; uncertainty not modelled")
            return self.model.expected(home, away, unknown=unknown)
        if self.league is not None and self.unknown_team_policy == "league_average":
            self._warn("no fitted team strengths: league-average expected goals from the profile")
            return self.league.mean_home, self.league.mean_away
        self._need_fit_or_profile()
        raise MissingInputs("nhl: pass home_xg/away_xg, or fit the engine, or use unknown_team_policy='league_average' with a league profile")

    # -------------------------------------------------------------- prediction
    def predict_distribution(self, match_context: Dict[str, Any], endpoint: str = "regulation") -> ScoreDistribution:
        if endpoint not in ("regulation", "full_game"):
            raise ValueError("endpoint must be 'regulation' or 'full_game'")
        if match_context.get("empty_net_rate") is not None:
            raise ValueError("the fixed empty_net_rate was removed; pass a HockeyLateGame instead")
        h_xg, a_xg = self._expected_goals(match_context)
        h_save = float(match_context.get("home_goalie_save_factor", 1.0))      # >1: stronger goalie, fewer goals against
        a_save = float(match_context.get("away_goalie_save_factor", 1.0))
        lam_h, lam_a = max(0.1, h_xg / a_save), max(0.1, a_xg / h_save)
        late = match_context.get("late_game", self.late_game)
        if late is None:
            p_h = poisson.pmf(np.arange(MAX_GOALS + 1), lam_h)
            p_a = poisson.pmf(np.arange(MAX_GOALS + 1), lam_a)
            grid = np.outer(p_h, p_a)
            grid /= grid.sum()
        else:
            grid = late_game_grid(lam_h, lam_a, late)
        meta = {"model": "nhl_poisson", "lambda_home": lam_h, "lambda_away": lam_a,
                "late_game": "none" if late is None else "state_model", "warnings": self._take_warnings()}
        dist = ScoreDistribution(grid, np.arange(MAX_GOALS + 1), np.arange(MAX_GOALS + 1), endpoint="regulation", metadata=meta)
        if endpoint == "regulation":
            return dist
        return hockey_full_game(dist, lam_h, lam_a, self.overtime_rule(bool(match_context.get("playoffs", False))))
