"""NHL predictive engine modeling xG, goalie quality, and empty-net goal distribution."""

from typing import Any, Dict
import numpy as np
from scipy.stats import poisson
from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution


class NHLEngine(BaseSportEngine):
    """Predictive engine for Ice Hockey matches (NHL, KHL, SHL)."""

    def __init__(self):
        super().__init__("nhl")
        self.is_fitted = False
        self.league_avg_goals: float = 3.05
        self.home_ice_advantage: float = 0.25
        self.team_scoring_factors: Dict[str, float] = {}
        self.team_defense_factors: Dict[str, float] = {}

    def fit(self, train_data: Any) -> "NHLEngine":
        """Fit shot conversion and goaltending baselines from H0 MoneyPuck data."""
        if isinstance(train_data, list):
            goals_for: Dict[str, float] = {}
            goals_against: Dict[str, float] = {}
            games_played: Dict[str, int] = {}
            h_g_list = []
            a_g_list = []
            all_g = []

            for m in train_data:
                if not isinstance(m, dict):
                    continue
                h = m.get("home_team")
                a = m.get("away_team")
                h_g = float(m.get("home_goals") or m.get("home_score", 3.0))
                a_g = float(m.get("away_goals") or m.get("away_score", 2.8))

                h_g_list.append(h_g)
                a_g_list.append(a_g)
                all_g.extend([h_g, a_g])

                if h:
                    goals_for[h] = goals_for.get(h, 0.0) + h_g
                    goals_against[h] = goals_against.get(h, 0.0) + a_g
                    games_played[h] = games_played.get(h, 0) + 1
                if a:
                    goals_for[a] = goals_for.get(a, 0.0) + a_g
                    goals_against[a] = goals_against.get(a, 0.0) + h_g
                    games_played[a] = games_played.get(a, 0) + 1

            if len(all_g) >= 10:
                self.league_avg_goals = float(np.mean(all_g))
                if h_g_list and a_g_list:
                    self.home_ice_advantage = float(np.mean(h_g_list) - np.mean(a_g_list))

            for t, gp in games_played.items():
                if gp >= 3 and self.league_avg_goals > 0:
                    mean_for = goals_for[t] / gp
                    mean_against = goals_against[t] / gp
                    self.team_scoring_factors[t] = float(0.8 * (mean_for / self.league_avg_goals) + 0.2)
                    self.team_defense_factors[t] = float(0.8 * (mean_against / self.league_avg_goals) + 0.2)

        self.is_fitted = True
        return self

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint score matrix for 60-minute regulation hockey."""
        h_team = match_context.get("home_team")
        a_team = match_context.get("away_team")

        h_att = self.team_scoring_factors.get(h_team, 1.0)
        a_att = self.team_scoring_factors.get(a_team, 1.0)
        h_def = self.team_defense_factors.get(h_team, 1.0)
        a_def = self.team_defense_factors.get(a_team, 1.0)

        # Expected goals
        if "home_xg" in match_context:
            h_xg = float(match_context["home_xg"])
        else:
            h_xg = self.league_avg_goals * h_att * a_def + (self.home_ice_advantage / 2.0)

        if "away_xg" in match_context:
            a_xg = float(match_context["away_xg"])
        else:
            a_xg = self.league_avg_goals * a_att * h_def - (self.home_ice_advantage / 2.0)

        # Goalie save percentage adjustments
        h_goalie_adj = float(match_context.get("home_goalie_save_factor", 1.0))
        a_goalie_adj = float(match_context.get("away_goalie_save_factor", 1.0))

        # Empty net goal probability mass
        empty_net_rate = float(match_context.get("empty_net_rate", 0.22))

        lambda_h = max(0.1, h_xg / a_goalie_adj)
        lambda_a = max(0.1, a_xg / h_goalie_adj)

        max_goals = 14
        grid = np.zeros((max_goals + 1, max_goals + 1), dtype=float)

        p_h = poisson.pmf(np.arange(max_goals + 1), lambda_h)
        p_a = poisson.pmf(np.arange(max_goals + 1), lambda_a)

        for x in range(max_goals + 1):
            for y in range(max_goals + 1):
                prob = p_h[x] * p_a[y]
                
                # Apply empty net transition mass if leading by 1 or 2 late
                if x > y and x <= y + 2 and x < max_goals:
                    # Trailing away team pulls goalie: chance of home sealing with empty netter
                    prob_en = prob * empty_net_rate
                    grid[x + 1, y] += prob_en
                    grid[x, y] += prob * (1.0 - empty_net_rate)
                elif y > x and y <= x + 2 and y < max_goals:
                    # Trailing home team pulls goalie: chance of away sealing with empty netter
                    prob_en = prob * empty_net_rate
                    grid[x, y + 1] += prob_en
                    grid[x, y] += prob * (1.0 - empty_net_rate)
                else:
                    grid[x, y] += prob

        # Normalize truncated mass
        grid /= np.sum(grid)

        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_goals + 1),
            away_support=np.arange(max_goals + 1)
        )

