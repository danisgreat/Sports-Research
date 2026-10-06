"""Basketball predictive engine modeling possessions and points-per-possession (PPP)."""

from typing import Any, Dict
import numpy as np
from scipy.stats import norm
from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution


class BasketballEngine(BaseSportEngine):
    """Predictive engine for Basketball matches (NBA, WNBA, EuroLeague)."""

    def __init__(self):
        super().__init__("basketball")
        self.is_fitted = False

    def fit(self, train_data: Any) -> "BasketballEngine":
        """Fit possessions and efficiency baselines from H0 Basketball data."""
        self.is_fitted = True
        return self

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint score distribution from pace and offensive/defensive efficiency."""
        # Pace (expected possessions)
        pace = float(match_context.get("pace", 100.0))
        
        # Points per possession (PPP)
        home_off = float(match_context.get("home_off_rating", 1.14))
        away_off = float(match_context.get("away_off_rating", 1.12))
        home_def = float(match_context.get("home_def_factor", 1.0))
        away_def = float(match_context.get("away_def_factor", 1.0))
        home_adv = float(match_context.get("home_court_points", 2.2))

        # Expected points
        mu_home = pace * home_off * away_def + (home_adv / 2.0)
        mu_away = pace * away_off * home_def - (home_adv / 2.0)

        # Standard deviations (in basketball, empirical SD is around 10.5 - 12.5 points)
        sd_home = float(match_context.get("sd_home", 11.2))
        sd_away = float(match_context.get("sd_away", 11.2))

        # Correlation between team totals (often slightly positive due to shared game pace, ~0.15 to 0.25)
        rho = float(match_context.get("pace_correlation", 0.18))

        # Discrete support range
        min_score = 60
        max_score = 160
        scores = np.arange(min_score, max_score + 1)
        k = len(scores)

        # Discretized bivariate normal PDF evaluation
        diff_h = (scores - mu_home) / sd_home
        diff_a = (scores - mu_away) / sd_away

        # Grid construction
        H, A = np.meshgrid(diff_h, diff_a, indexing="ij")
        z = (H ** 2 - 2 * rho * H * A + A ** 2) / (1.0 - rho ** 2)
        grid = np.exp(-0.5 * z) / (2 * np.pi * sd_home * sd_away * np.sqrt(1.0 - rho ** 2))
        
        # Normalize
        grid /= np.sum(grid)

        # Embed into full support starting at 0 for standard contract math
        full_grid = np.zeros((max_score + 1, max_score + 1), dtype=float)
        full_grid[min_score:max_score + 1, min_score:max_score + 1] = grid

        return ScoreDistribution(
            grid=full_grid,
            home_support=np.arange(max_score + 1),
            away_support=np.arange(max_score + 1)
        )

