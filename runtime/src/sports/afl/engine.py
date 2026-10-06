"""AFL predictive engine modeling territory, scoring shots, and goal/behind distribution."""

from typing import Any, Dict
import numpy as np
from scipy.stats import binom, poisson
from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution


class AFLEngine(BaseSportEngine):
    """Predictive engine for Australian Rules Football (AFL, AFLW)."""

    def __init__(self):
        super().__init__("afl")
        self.is_fitted = False
        self.league_avg_shots: float = 23.5
        self.home_shot_advantage: float = 2.4
        self.league_conversion: float = 0.54
        self.team_attack_ratings: Dict[str, float] = {}
        self.team_defense_ratings: Dict[str, float] = {}
        self.team_conversions: Dict[str, float] = {}

    def fit(self, train_data: Any) -> "AFLEngine":
        """Fit scoring shot and conversion baselines from H0 fitzRoy data."""
        if isinstance(train_data, list):
            shot_for: Dict[str, float] = {}
            shot_against: Dict[str, float] = {}
            goals_for: Dict[str, float] = {}
            games_played: Dict[str, int] = {}
            home_shots_list = []
            away_shots_list = []

            for m in train_data:
                if not isinstance(m, dict):
                    continue
                h = m.get("home_team")
                a = m.get("away_team")
                h_s = float(m.get("home_shots") or (m.get("home_goals", 12) + m.get("home_behinds", 11)))
                a_s = float(m.get("away_shots") or (m.get("away_goals", 11) + m.get("away_behinds", 11)))
                h_g = float(m.get("home_goals", h_s * 0.54))
                a_g = float(m.get("away_goals", a_s * 0.54))

                home_shots_list.append(h_s)
                away_shots_list.append(a_s)

                if h:
                    shot_for[h] = shot_for.get(h, 0.0) + h_s
                    shot_against[h] = shot_against.get(h, 0.0) + a_s
                    goals_for[h] = goals_for.get(h, 0.0) + h_g
                    games_played[h] = games_played.get(h, 0) + 1
                if a:
                    shot_for[a] = shot_for.get(a, 0.0) + a_s
                    shot_against[a] = shot_against.get(a, 0.0) + h_s
                    goals_for[a] = goals_for.get(a, 0.0) + a_g
                    games_played[a] = games_played.get(a, 0) + 1

            if home_shots_list and away_shots_list:
                all_shots = home_shots_list + away_shots_list
                self.league_avg_shots = float(np.mean(all_shots))
                self.home_shot_advantage = float(np.mean(home_shots_list) - np.mean(away_shots_list))
                total_goals = sum(goals_for.values()) / 2.0
                total_shots = sum(shot_for.values()) / 2.0
                if total_shots > 0:
                    self.league_conversion = total_goals / total_shots

            for t, gp in games_played.items():
                if gp >= 3 and self.league_avg_shots > 0:
                    mean_for = shot_for[t] / gp
                    mean_against = shot_against[t] / gp
                    # Shrink towards 1.0
                    self.team_attack_ratings[t] = float(0.8 * (mean_for / self.league_avg_shots) + 0.2)
                    self.team_defense_ratings[t] = float(0.8 * (mean_against / self.league_avg_shots) + 0.2)
                    if shot_for[t] > 0:
                        raw_conv = goals_for[t] / shot_for[t]
                        self.team_conversions[t] = float(0.7 * raw_conv + 0.3 * self.league_conversion)

        self.is_fitted = True
        return self

    def _team_points_pmf(
        self,
        exp_scoring_shots: float,
        goal_conversion_rate: float = 0.54,
        max_points: int = 180
    ) -> np.ndarray:
        """Derive points distribution P(Points = 6G + B) via shot-conversion mixture."""
        points_pmf = np.zeros(max_points + 1, dtype=float)
        
        # Marginal shot count distribution via Poisson
        shot_support = np.arange(10, 45)
        p_shots = poisson.pmf(shot_support, exp_scoring_shots)
        p_shots /= np.sum(p_shots)

        for s_idx, s in enumerate(shot_support):
            weight_s = p_shots[s_idx]
            # Distribution of goals G ~ Binomial(s, goal_conversion_rate)
            goals = np.arange(s + 1)
            behinds = s - goals
            p_goals = binom.pmf(goals, s, goal_conversion_rate)
            
            pts = 6 * goals + behinds
            for g_idx, pt in enumerate(pts):
                if pt <= max_points:
                    points_pmf[pt] += weight_s * p_goals[g_idx]

        total = np.sum(points_pmf)
        if total > 0:
            points_pmf /= total
        return points_pmf

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint score distribution for AFL match."""
        h_team = match_context.get("home_team")
        a_team = match_context.get("away_team")

        h_att = self.team_attack_ratings.get(h_team, 1.0)
        a_def = self.team_defense_ratings.get(a_team, 1.0)
        a_att = self.team_attack_ratings.get(a_team, 1.0)
        h_def = self.team_defense_ratings.get(h_team, 1.0)

        # Expected scoring shots derived from fitted model or context
        if "home_expected_shots" in match_context:
            h_shots = float(match_context["home_expected_shots"])
        else:
            h_shots = self.league_avg_shots * h_att * a_def + (self.home_shot_advantage / 2.0)

        if "away_expected_shots" in match_context:
            a_shots = float(match_context["away_expected_shots"])
        else:
            a_shots = self.league_avg_shots * a_att * h_def - (self.home_shot_advantage / 2.0)

        h_conv = float(match_context.get("home_conversion_rate") or self.team_conversions.get(h_team, self.league_conversion))
        a_conv = float(match_context.get("away_conversion_rate") or self.team_conversions.get(a_team, self.league_conversion))

        max_pts = 180
        p_home = self._team_points_pmf(h_shots, h_conv, max_pts)
        p_away = self._team_points_pmf(a_shots, a_conv, max_pts)

        grid = np.outer(p_home, p_away)
        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_pts + 1),
            away_support=np.arange(max_pts + 1)
        )

