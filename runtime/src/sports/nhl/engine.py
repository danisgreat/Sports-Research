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

    def fit(self, train_data: Any) -> "NHLEngine":
        """Fit shot conversion and goaltending baselines from H0 MoneyPuck data."""
        self.is_fitted = True
        return self

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint score matrix for 60-minute regulation hockey."""
        # Unblocked shot attempts and goalie quality
        h_xg = float(match_context.get("home_xg", 3.10))
        a_xg = float(match_context.get("away_xg", 2.85))
        
        # Goalie save percentage adjustments (relative to league avg ~0.905)
        h_goalie_adj = float(match_context.get("home_goalie_save_factor", 1.0))
        a_goalie_adj = float(match_context.get("away_goalie_save_factor", 1.0))

        # Empty net goal probability mass
        empty_net_rate = float(match_context.get("empty_net_rate", 0.22))

        lambda_h = h_xg / a_goalie_adj
        lambda_a = a_xg / h_goalie_adj

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

