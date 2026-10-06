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
        self.league_avg_score: float = 22.5
        self.home_advantage: float = 1.8
        self.team_off_ratings: Dict[str, float] = {}
        self.team_def_factors: Dict[str, float] = {}

    def fit(self, train_data: Any) -> "NFLEngine":
        """Fit drive transition baselines from H0 nflfastR records."""
        if isinstance(train_data, list):
            pts_for: Dict[str, float] = {}
            pts_against: Dict[str, float] = {}
            games_played: Dict[str, int] = {}
            h_p_list = []
            a_p_list = []
            all_p = []

            for m in train_data:
                if not isinstance(m, dict):
                    continue
                h = m.get("home_team")
                a = m.get("away_team")
                h_p = float(m.get("home_score", 23))
                a_p = float(m.get("away_score", 20))

                h_p_list.append(h_p)
                a_p_list.append(a_p)
                all_p.extend([h_p, a_p])

                if h:
                    pts_for[h] = pts_for.get(h, 0.0) + h_p
                    pts_against[h] = pts_against.get(h, 0.0) + a_p
                    games_played[h] = games_played.get(h, 0) + 1
                if a:
                    pts_for[a] = pts_for.get(a, 0.0) + a_p
                    pts_against[a] = pts_against.get(a, 0.0) + h_p
                    games_played[a] = games_played.get(a, 0) + 1

            if len(all_p) >= 10:
                self.league_avg_score = float(np.mean(all_p))
                if h_p_list and a_p_list:
                    self.home_advantage = float(np.mean(h_p_list) - np.mean(a_p_list))

            for t, gp in games_played.items():
                if gp >= 3 and self.league_avg_score > 0:
                    mean_for = pts_for[t] / gp
                    mean_against = pts_against[t] / gp
                    self.team_off_ratings[t] = float(0.8 * (mean_for / self.league_avg_score) + 0.2)
                    self.team_def_factors[t] = float(0.8 * (mean_against / self.league_avg_score) + 0.2)

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
        h_team = match_context.get("home_team")
        a_team = match_context.get("away_team")

        h_off = self.team_off_ratings.get(h_team, 1.0)
        a_off = self.team_off_ratings.get(a_team, 1.0)
        h_def = self.team_def_factors.get(h_team, 1.0)
        a_def = self.team_def_factors.get(a_team, 1.0)

        n_drives_h = int(match_context.get("home_drives", 11))
        n_drives_a = int(match_context.get("away_drives", 11))

        # Drive success probabilities adjusted for team strength
        base_td = 0.22
        base_fg = 0.17
        h_mult = h_off * a_def * (1.0 + (self.home_advantage / 50.0))
        a_mult = a_off * h_def * (1.0 - (self.home_advantage / 50.0))

        h_td = float(match_context.get("home_p_td") or np.clip(base_td * h_mult, 0.08, 0.45))
        h_fg = float(match_context.get("home_p_fg") or np.clip(base_fg * h_mult, 0.08, 0.35))
        a_td = float(match_context.get("away_p_td") or np.clip(base_td * a_mult, 0.08, 0.45))
        a_fg = float(match_context.get("away_p_fg") or np.clip(base_fg * a_mult, 0.08, 0.35))

        p_home_scores = self._simulate_team_drives(n_drives_h, h_td, h_fg)
        p_away_scores = self._simulate_team_drives(n_drives_a, a_td, a_fg)

        grid = np.outer(p_home_scores, p_away_scores)
        max_score = len(p_home_scores) - 1

        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_score + 1),
            away_support=np.arange(max_score + 1)
        )

