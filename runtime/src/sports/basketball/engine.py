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
        self.league_avg_score: float = 112.0
        self.home_court_points: float = 2.4
        self.empirical_sd: float = 11.2
        self.pace_correlation: float = 0.18
        self.team_off_ratings: Dict[str, float] = {}
        self.team_def_factors: Dict[str, float] = {}

    def fit(self, train_data: Any) -> "BasketballEngine":
        """Fit possessions and efficiency baselines from H0 Basketball data."""
        if isinstance(train_data, list):
            pts_for: Dict[str, float] = {}
            pts_against: Dict[str, float] = {}
            games_played: Dict[str, int] = {}
            h_pts_list = []
            a_pts_list = []
            all_pts = []

            for m in train_data:
                if not isinstance(m, dict):
                    continue
                h = m.get("home_team")
                a = m.get("away_team")
                h_p = float(m.get("home_score", 112.0))
                a_p = float(m.get("away_score", 109.0))

                h_pts_list.append(h_p)
                a_pts_list.append(a_p)
                all_pts.extend([h_p, a_p])

                if h:
                    pts_for[h] = pts_for.get(h, 0.0) + h_p
                    pts_against[h] = pts_against.get(h, 0.0) + a_p
                    games_played[h] = games_played.get(h, 0) + 1
                if a:
                    pts_for[a] = pts_for.get(a, 0.0) + a_p
                    pts_against[a] = pts_against.get(a, 0.0) + h_p
                    games_played[a] = games_played.get(a, 0) + 1

            if len(all_pts) >= 10:
                self.league_avg_score = float(np.mean(all_pts))
                self.empirical_sd = float(np.std(all_pts, ddof=1))
                if h_pts_list and a_pts_list:
                    self.home_court_points = float(np.mean(h_pts_list) - np.mean(a_pts_list))
                    if len(h_pts_list) >= 5:
                        r = float(np.corrcoef(h_pts_list, a_pts_list)[0, 1])
                        if np.isfinite(r) and -0.5 < r < 0.8:
                            self.pace_correlation = r

            for t, gp in games_played.items():
                if gp >= 3 and self.league_avg_score > 0:
                    mean_for = pts_for[t] / gp
                    mean_against = pts_against[t] / gp
                    self.team_off_ratings[t] = float(0.8 * (mean_for / self.league_avg_score) + 0.2)
                    self.team_def_factors[t] = float(0.8 * (mean_against / self.league_avg_score) + 0.2)

        self.is_fitted = True
        return self

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint score distribution from pace and offensive/defensive efficiency."""
        h_team = match_context.get("home_team")
        a_team = match_context.get("away_team")

        h_off = self.team_off_ratings.get(h_team, 1.0)
        a_off = self.team_off_ratings.get(a_team, 1.0)
        h_def = self.team_def_factors.get(h_team, 1.0)
        a_def = self.team_def_factors.get(a_team, 1.0)

        # Expected points
        if "home_expected_points" in match_context:
            mu_home = float(match_context["home_expected_points"])
        else:
            mu_home = self.league_avg_score * h_off * a_def + (self.home_court_points / 2.0)

        if "away_expected_points" in match_context:
            mu_away = float(match_context["away_expected_points"])
        else:
            mu_away = self.league_avg_score * a_off * h_def - (self.home_court_points / 2.0)

        sd_home = float(match_context.get("sd_home", self.empirical_sd))
        sd_away = float(match_context.get("sd_away", self.empirical_sd))
        rho = float(match_context.get("pace_correlation", self.pace_correlation))

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

