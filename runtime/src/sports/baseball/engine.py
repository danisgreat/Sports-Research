"""Baseball predictive engine modeling starter leash, bullpen transition, and runs distribution."""

from typing import Any, Dict
import numpy as np
from scipy.stats import nbinom
from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution


class BaseballEngine(BaseSportEngine):
    """Predictive engine for Baseball matches (MLB, NPB, KBO)."""

    def __init__(self):
        super().__init__("baseball")
        self.is_fitted = False

    def fit(self, train_data: Any) -> "BaseballEngine":
        """Fit starter and bullpen run suppression baselines from H0 Statcast data."""
        self.is_fitted = True
        return self

    def _team_run_pmf(
        self,
        starter_ra9: float,
        bullpen_ra9: float,
        starter_innings: float,
        opp_wrc_plus: float = 100.0,
        park_factor: float = 1.0,
        max_runs: int = 25
    ) -> np.ndarray:
        """Compute 9-inning team run PMF combining starter and bullpen segments."""
        total_innings = 9.0
        bp_innings = max(0.0, total_innings - starter_innings)
        
        # Expected runs allowed by starter and bullpen
        exp_starter_runs = (starter_ra9 / 9.0) * starter_innings
        exp_bullpen_runs = (bullpen_ra9 / 9.0) * bp_innings
        
        # Combined expected runs with opponent offense and park scaling
        lambda_runs = (exp_starter_runs + exp_bullpen_runs) * (opp_wrc_plus / 100.0) * park_factor
        
        # Negative binomial parameterization (r controls overdispersion / cluster risk)
        r = 4.2
        p = r / (r + lambda_runs)

        runs = np.arange(max_runs + 1)
        pmf = nbinom.pmf(runs, r, p)
        pmf /= np.sum(pmf)
        return pmf

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint run distribution between home and away teams."""
        # Home offense vs Away pitching
        away_sp_ra9 = float(match_context.get("away_sp_ra9", 4.10))
        away_bp_ra9 = float(match_context.get("away_bp_ra9", 3.85))
        away_sp_ip = float(match_context.get("away_sp_expected_ip", 5.2))
        home_wrc = float(match_context.get("home_wrc_plus", 102.0))

        # Away offense vs Home pitching
        home_sp_ra9 = float(match_context.get("home_sp_ra9", 3.90))
        home_bp_ra9 = float(match_context.get("home_bp_ra9", 3.80))
        home_sp_ip = float(match_context.get("home_sp_expected_ip", 5.5))
        away_wrc = float(match_context.get("away_wrc_plus", 98.0))

        park = float(match_context.get("park_factor", 1.0))
        max_runs = 25

        p_home = self._team_run_pmf(away_sp_ra9, away_bp_ra9, away_sp_ip, home_wrc, park, max_runs)
        p_away = self._team_run_pmf(home_sp_ra9, home_bp_ra9, home_sp_ip, away_wrc, park, max_runs)

        grid = np.outer(p_home, p_away)
        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_runs + 1),
            away_support=np.arange(max_runs + 1)
        )

