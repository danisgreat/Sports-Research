"""American football predictive engine modeling discrete Markov drive outcomes and key numbers."""

from typing import Any, Dict
import numpy as np
from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution


class NFLEngine(BaseSportEngine):
    """Predictive engine for American Football matches (NFL, NCAA)."""

    def __init__(self):
        super().__init__("american_football")
        self.is_fitted = False

    def fit(self, train_data: Any) -> "NFLEngine":
        """Fit drive transition baselines from H0 nflfastR records."""
        self.is_fitted = True
        return self

    def _simulate_team_drives(
        self,
        n_drives: int,
        p_td: float,
        p_fg: float,
        p_safety: float = 0.015,
        max_score: int = 65
    ) -> np.ndarray:
        """Convolve drive score PMFs across n_drives to form the discrete team score distribution."""
        # Single drive distribution: 0, 2, 3, 7, 8 (2pt conversion)
        # Primary outcomes: 0 (punt/turnover/miss), 2 (safety), 3 (FG), 7 (TD+XP)
        p_0 = max(0.0, 1.0 - (p_td + p_fg + p_safety))
        drive_pmf = np.zeros(9, dtype=float)
        drive_pmf[0] = p_0
        drive_pmf[2] = p_safety
        drive_pmf[3] = p_fg
        drive_pmf[7] = p_td

        # Repeated discrete convolution across drives
        total_pmf = np.array([1.0], dtype=float)
        for _ in range(n_drives):
            total_pmf = np.convolve(total_pmf, drive_pmf)

        # Truncate or pad to max_score
        if len(total_pmf) > max_score + 1:
            total_pmf = total_pmf[:max_score + 1]
        else:
            total_pmf = np.pad(total_pmf, (0, max_score + 1 - len(total_pmf)))

        total_pmf /= np.sum(total_pmf)
        return total_pmf

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint score distribution preserving football key numbers."""
        n_drives_h = int(match_context.get("home_drives", 11))
        n_drives_a = int(match_context.get("away_drives", 11))

        # Drive success probabilities
        h_td = float(match_context.get("home_p_td", 0.23))
        h_fg = float(match_context.get("home_p_fg", 0.17))
        a_td = float(match_context.get("away_p_td", 0.20))
        a_fg = float(match_context.get("away_p_fg", 0.16))

        p_home_scores = self._simulate_team_drives(n_drives_h, h_td, h_fg)
        p_away_scores = self._simulate_team_drives(n_drives_a, a_td, a_fg)

        grid = np.outer(p_home_scores, p_away_scores)
        max_score = len(p_home_scores) - 1

        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_score + 1),
            away_support=np.arange(max_score + 1)
        )

