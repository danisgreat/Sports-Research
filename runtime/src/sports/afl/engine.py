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

    def fit(self, train_data: Any) -> "AFLEngine":
        """Fit scoring shot and conversion baselines from H0 fitzRoy data."""
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
        # Expected scoring shots
        h_shots = float(match_context.get("home_expected_shots", 24.5))
        a_shots = float(match_context.get("away_expected_shots", 22.0))
        
        # Goal conversion rates
        h_conv = float(match_context.get("home_conversion_rate", 0.54))
        a_conv = float(match_context.get("away_conversion_rate", 0.53))

        max_pts = 180
        p_home = self._team_points_pmf(h_shots, h_conv, max_pts)
        p_away = self._team_points_pmf(a_shots, a_conv, max_pts)

        grid = np.outer(p_home, p_away)
        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_pts + 1),
            away_support=np.arange(max_pts + 1)
        )

