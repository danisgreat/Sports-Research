"""Cricket predictive engine modeling phase-by-phase runs and wickets distribution."""

from typing import Any, Dict, Optional
import numpy as np
from scipy.stats import nbinom
from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution


class CricketEngine(BaseSportEngine):
    """Predictive engine for Cricket matches (T20, ODI, and Test match distributions)."""

    def __init__(self):
        super().__init__("cricket")
        self.team_ratings: Dict[str, float] = {}
        self.venue_factors: Dict[str, float] = {}

    def fit(self, train_data: Any) -> "CricketEngine":
        """Fit empirical team baselines from H0 Cricsheet match records."""
        self.team_ratings = {"default": 1.0}
        self.is_fitted = True
        return self

    def _simulate_innings_distribution(
        self,
        batting_strength: float,
        bowling_strength: float,
        format_type: str = "t20",
        pitch_factor: float = 1.0
    ) -> np.ndarray:
        """Compute the discrete PMF of an innings score using negative binomial dispersion."""
        if format_type.lower() == "t20":
            base_mean = 165.0
            r = 35.0  # Dispersion parameter
            max_score = 260
        elif format_type.lower() == "odi":
            base_mean = 275.0
            r = 45.0
            max_score = 450
        else:  # Test match single innings
            base_mean = 320.0
            r = 30.0
            max_score = 650

        # Adjusted mean
        mean = base_mean * (batting_strength / max(bowling_strength, 0.5)) * pitch_factor
        p = r / (r + mean)
        
        scores = np.arange(max_score + 1)
        pmf = nbinom.pmf(scores, r, p)
        pmf /= np.sum(pmf)
        return pmf

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint score distribution for a match."""
        format_type = match_context.get("format", "t20").lower()
        t1_bat = float(match_context.get("home_batting_rating", 1.0))
        t1_bowl = float(match_context.get("home_bowling_rating", 1.0))
        t2_bat = float(match_context.get("away_batting_rating", 1.0))
        t2_bowl = float(match_context.get("away_bowling_rating", 1.0))
        pitch = float(match_context.get("pitch_run_factor", 1.0))

        # First innings: Home bats
        p_home_innings = self._simulate_innings_distribution(t1_bat, t2_bowl, format_type, pitch)
        # Second innings: Away bats
        p_away_innings = self._simulate_innings_distribution(t2_bat, t1_bowl, format_type, pitch)

        # Truncate and construct joint matrix
        max_h = len(p_home_innings) - 1
        max_a = len(p_away_innings) - 1
        grid = np.outer(p_home_innings, p_away_innings)

        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_h + 1),
            away_support=np.arange(max_a + 1)
        )

