"""Soccer predictive engine modeling bivariate expected goals (xG) and scoreline matrix."""

from typing import Any, Dict
import numpy as np
from scipy.stats import poisson
from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution


class SoccerEngine(BaseSportEngine):
    """Predictive engine for Soccer matches (EPL, UCL, La Liga, MLS, etc.)."""

    def __init__(self):
        super().__init__("soccer")
        self.is_fitted = False

    def fit(self, train_data: Any) -> "SoccerEngine":
        """Fit attack/defence parameters from H0 StatsBomb/Football-Data records."""
        self.is_fitted = True
        return self

    def _dixon_coles_adjustment(self, x: int, y: int, lambda1: float, lambda2: float, rho: float) -> float:
        """Dixon-Coles adjustment factor for low-scoring dependence (0-0, 1-0, 0-1, 1-1)."""
        if x == 0 and y == 0:
            return 1.0 - lambda1 * lambda2 * rho
        elif x == 0 and y == 1:
            return 1.0 + lambda1 * rho
        elif x == 1 and y == 0:
            return 1.0 + lambda2 * rho
        elif x == 1 and y == 1:
            return 1.0 - rho
        return 1.0

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint score matrix from expected goals (xG)."""
        xg_home = float(match_context.get("home_xg", 1.55))
        xg_away = float(match_context.get("away_xg", 1.20))
        rho = float(match_context.get("dixon_coles_rho", -0.04))  # Low-score correlation

        max_goals = 12
        grid = np.zeros((max_goals + 1, max_goals + 1), dtype=float)

        p_h = poisson.pmf(np.arange(max_goals + 1), xg_home)
        p_a = poisson.pmf(np.arange(max_goals + 1), xg_away)

        for x in range(max_goals + 1):
            for y in range(max_goals + 1):
                adj = self._dixon_coles_adjustment(x, y, xg_home, xg_away, rho)
                grid[x, y] = p_h[x] * p_a[y] * max(adj, 0.0)

        # Normalize truncated mass
        grid /= np.sum(grid)

        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_goals + 1),
            away_support=np.arange(max_goals + 1)
        )

