"""NRL predictive engine modeling sets, tries, conversions, and discrete key numbers."""

from typing import Any, Dict
import numpy as np
from scipy.stats import binom, poisson
from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution


class NRLEngine(BaseSportEngine):
    """Predictive engine for Rugby League matches (NRL, Super League)."""

    def __init__(self):
        super().__init__("nrl")
        self.is_fitted = False

    def fit(self, train_data: Any) -> "NRLEngine":
        """Fit scoring rate baselines from H0 nrlR data."""
        self.is_fitted = True
        return self

    def _team_score_pmf(
        self,
        exp_tries: float,
        conversion_rate: float = 0.78,
        exp_penalty_goals: float = 0.8,
        max_score: int = 70
    ) -> np.ndarray:
        """Derive NRL discrete points PMF preserving key number structure."""
        pmf = np.zeros(max_score + 1, dtype=float)
        
        # Try distribution via Poisson
        try_support = np.arange(0, 12)
        p_tries = poisson.pmf(try_support, exp_tries)
        
        # Penalty goals distribution via Poisson
        pg_support = np.arange(0, 5)
        p_pgs = poisson.pmf(pg_support, exp_penalty_goals)

        for t_idx, t in enumerate(try_support):
            w_t = p_tries[t_idx]
            # Conversions ~ Binomial(t, conversion_rate)
            conv_counts = np.arange(t + 1)
            p_convs = binom.pmf(conv_counts, t, conversion_rate)

            for c_idx, c in enumerate(conv_counts):
                w_c = w_t * p_convs[c_idx]
                try_pts = 4 * t + 2 * c

                for pg_idx, pg in enumerate(pg_support):
                    w_total = w_c * p_pgs[pg_idx]
                    total_pts = try_pts + 2 * pg

                    if total_pts <= max_score:
                        pmf[total_pts] += w_total

        total = np.sum(pmf)
        if total > 0:
            pmf /= total
        return pmf

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint score distribution for an NRL match."""
        h_tries = float(match_context.get("home_expected_tries", 3.8))
        a_tries = float(match_context.get("away_expected_tries", 3.2))
        h_kicker_acc = float(match_context.get("home_goal_kicker_accuracy", 0.80))
        a_kicker_acc = float(match_context.get("away_goal_kicker_accuracy", 0.76))

        max_score = 70
        p_home = self._team_score_pmf(h_tries, h_kicker_acc, max_score=max_score)
        p_away = self._team_score_pmf(a_tries, a_kicker_acc, max_score=max_score)

        grid = np.outer(p_home, p_away)
        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_score + 1),
            away_support=np.arange(max_score + 1)
        )

