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
        self.league_avg_runs: float = 4.50
        self.home_run_advantage: float = 0.35
        self.dispersion_r: float = 4.20
        self.team_offense_ratings: Dict[str, float] = {}
        self.team_pitching_ratings: Dict[str, float] = {}

    def fit(self, train_data: Any) -> "BaseballEngine":
        """Fit starter and bullpen run suppression baselines from H0 Statcast data."""
        if isinstance(train_data, list):
            runs_for: Dict[str, float] = {}
            runs_against: Dict[str, float] = {}
            games_played: Dict[str, int] = {}
            all_runs = []
            h_runs_list = []
            a_runs_list = []

            for m in train_data:
                if not isinstance(m, dict):
                    continue
                h = m.get("home_team")
                a = m.get("away_team")
                h_r = float(m.get("home_runs") or m.get("home_score", 4.5))
                a_r = float(m.get("away_runs") or m.get("away_score", 4.2))

                h_runs_list.append(h_r)
                a_runs_list.append(a_r)
                all_runs.extend([h_r, a_r])

                if h:
                    runs_for[h] = runs_for.get(h, 0.0) + h_r
                    runs_against[h] = runs_against.get(h, 0.0) + a_r
                    games_played[h] = games_played.get(h, 0) + 1
                if a:
                    runs_for[a] = runs_for.get(a, 0.0) + a_r
                    runs_against[a] = runs_against.get(a, 0.0) + h_r
                    games_played[a] = games_played.get(a, 0) + 1

            if len(all_runs) >= 10:
                mu = float(np.mean(all_runs))
                var = float(np.var(all_runs, ddof=1))
                self.league_avg_runs = mu
                if var > mu:
                    self.dispersion_r = max(1.5, (mu ** 2) / (var - mu))
                if h_runs_list and a_runs_list:
                    self.home_run_advantage = float(np.mean(h_runs_list) - np.mean(a_runs_list))

            for t, gp in games_played.items():
                if gp >= 3 and self.league_avg_runs > 0:
                    mean_for = runs_for[t] / gp
                    mean_against = runs_against[t] / gp
                    self.team_offense_ratings[t] = float(0.8 * (mean_for / self.league_avg_runs) + 0.2)
                    self.team_pitching_ratings[t] = float(0.8 * (mean_against / self.league_avg_runs) + 0.2)

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
        
        # Negative binomial parameterization
        r = self.dispersion_r
        p = r / (r + lambda_runs)

        runs = np.arange(max_runs + 1)
        pmf = nbinom.pmf(runs, r, p)
        pmf /= np.sum(pmf)
        return pmf

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint run distribution between home and away teams."""
        h_team = match_context.get("home_team")
        a_team = match_context.get("away_team")

        h_off_factor = self.team_offense_ratings.get(h_team, 1.0)
        a_off_factor = self.team_offense_ratings.get(a_team, 1.0)
        h_pitch_factor = self.team_pitching_ratings.get(h_team, 1.0)
        a_pitch_factor = self.team_pitching_ratings.get(a_team, 1.0)

        # Home offense vs Away pitching
        away_sp_ra9 = float(match_context.get("away_sp_ra9", self.league_avg_runs * a_pitch_factor))
        away_bp_ra9 = float(match_context.get("away_bp_ra9", self.league_avg_runs * a_pitch_factor))
        away_sp_ip = float(match_context.get("away_sp_expected_ip", 5.2))
        home_wrc = float(match_context.get("home_wrc_plus", 100.0 * h_off_factor + (self.home_run_advantage * 10.0)))

        # Away offense vs Home pitching
        home_sp_ra9 = float(match_context.get("home_sp_ra9", self.league_avg_runs * h_pitch_factor))
        home_bp_ra9 = float(match_context.get("home_bp_ra9", self.league_avg_runs * h_pitch_factor))
        home_sp_ip = float(match_context.get("home_sp_expected_ip", 5.5))
        away_wrc = float(match_context.get("away_wrc_plus", 100.0 * a_off_factor - (self.home_run_advantage * 10.0)))

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

