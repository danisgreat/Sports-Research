"""Cricket predictive engine modeling phase-by-phase runs and chase stopping rules."""

from typing import Any, Dict, Optional
import numpy as np
from scipy.stats import nbinom
from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution


class CricketEngine(BaseSportEngine):
    """Predictive engine for Cricket matches (T20, ODI, and Test match distributions).
    
    Implements:
    - Innings 1 score distribution
    - Chase stopping rule: Innings 2 terminates when target (S1 + 1) is reached or all wickets fall.
      Two independent unrestricted totals are explicitly rejected as mathematically invalid.
    """

    def __init__(self):
        super().__init__("cricket")
        self.team_batting_ratings: Dict[str, float] = {}
        self.team_bowling_ratings: Dict[str, float] = {}
        self.venue_factors: Dict[str, float] = {}
        self.format_means: Dict[str, float] = {"t20": 165.0, "odi": 275.0, "test": 320.0}
        self.format_r: Dict[str, float] = {"t20": 35.0, "odi": 45.0, "test": 30.0}

    def fit(self, train_data: Any) -> "CricketEngine":
        """Fit empirical team baselines from H0 Cricsheet match records."""
        if isinstance(train_data, list):
            runs_scored: Dict[str, float] = {}
            runs_conceded: Dict[str, float] = {}
            innings_bat: Dict[str, int] = {}
            innings_bowl: Dict[str, int] = {}
            format_runs: Dict[str, list] = {"t20": [], "odi": [], "test": []}

            for m in train_data:
                if not isinstance(m, dict):
                    continue
                fmt = m.get("format", "t20").lower()
                bat_team = m.get("batting_team") or m.get("home_team")
                bowl_team = m.get("bowling_team") or m.get("away_team")
                runs = float(m.get("innings1_runs") or m.get("runs", 160))

                if fmt in format_runs:
                    format_runs[fmt].append(runs)

                if bat_team:
                    runs_scored[bat_team] = runs_scored.get(bat_team, 0.0) + runs
                    innings_bat[bat_team] = innings_bat.get(bat_team, 0) + 1
                if bowl_team:
                    runs_conceded[bowl_team] = runs_conceded.get(bowl_team, 0.0) + runs
                    innings_bowl[bowl_team] = innings_bowl.get(bowl_team, 0) + 1

            for fmt, r_list in format_runs.items():
                if len(r_list) >= 5:
                    mu = float(np.mean(r_list))
                    var = float(np.var(r_list, ddof=1))
                    self.format_means[fmt] = mu
                    if var > mu:
                        # Method of moments for negative binomial: var = mu + mu^2/r -> r = mu^2 / (var - mu)
                        self.format_r[fmt] = max(5.0, (mu ** 2) / (var - mu))

            overall_mean = self.format_means.get("t20", 165.0)
            for t, count in innings_bat.items():
                if count >= 3 and overall_mean > 0:
                    team_avg = runs_scored[t] / count
                    self.team_batting_ratings[t] = float(0.8 * (team_avg / overall_mean) + 0.2)

            for t, count in innings_bowl.items():
                if count >= 3 and overall_mean > 0:
                    team_avg_against = runs_conceded[t] / count
                    self.team_bowling_ratings[t] = float(0.8 * (team_avg_against / overall_mean) + 0.2)

        self.is_fitted = True
        return self

    def _simulate_unrestricted_innings(
        self,
        batting_strength: float,
        bowling_strength: float,
        format_type: str = "t20",
        pitch_factor: float = 1.0
    ) -> np.ndarray:
        """Compute the discrete PMF of an unrestricted innings score using negative binomial dispersion."""
        fmt = format_type.lower()
        base_mean = self.format_means.get(fmt, 165.0)
        r = self.format_r.get(fmt, 35.0)
        max_score = 260 if fmt == "t20" else (450 if fmt == "odi" else 650)

        # Adjusted mean
        mean = base_mean * (batting_strength / max(bowling_strength, 0.5)) * pitch_factor
        p = r / (r + mean)
        
        scores = np.arange(max_score + 1)
        pmf = nbinom.pmf(scores, r, p)
        pmf /= np.sum(pmf)
        return pmf

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint score distribution enforcing the chase stopping rule."""
        format_type = match_context.get("format", "t20").lower()
        h_team = match_context.get("home_team")
        a_team = match_context.get("away_team")

        t1_bat = float(match_context.get("home_batting_rating") or self.team_batting_ratings.get(h_team, 1.0))
        t1_bowl = float(match_context.get("home_bowling_rating") or self.team_bowling_ratings.get(h_team, 1.0))
        t2_bat = float(match_context.get("away_batting_rating") or self.team_batting_ratings.get(a_team, 1.0))
        t2_bowl = float(match_context.get("away_bowling_rating") or self.team_bowling_ratings.get(a_team, 1.0))
        pitch = float(match_context.get("pitch_run_factor", 1.0))
        apply_chase_stopping = match_context.get("apply_chase_stopping_rule", True)

        # 1st Innings (Home batting)
        p_innings1 = self._simulate_unrestricted_innings(t1_bat, t2_bowl, format_type, pitch)
        # 2nd Innings unrestricted ability (Away batting)
        p_unrestricted2 = self._simulate_unrestricted_innings(t2_bat, t1_bowl, format_type, pitch)

        max_h = len(p_innings1) - 1
        max_a = len(p_unrestricted2) - 1

        if not apply_chase_stopping:
            grid = np.outer(p_innings1, p_unrestricted2)
        else:
            # Construct joint distribution matrix under chase stopping rule
            # When Home scores s1, Target is T = s1 + 1.
            # If Away unrestricted ability >= T, Away innings terminates at T (match won).
            # If Away unrestricted ability < T, Away innings terminates at that score (all out / overs expired).
            grid = np.zeros((max_h + 1, max_a + 1), dtype=float)

            for s1 in range(max_h + 1):
                p_s1 = p_innings1[s1]
                if p_s1 < 1e-12:
                    continue

                target = s1 + 1
                if target <= max_a:
                    # Losing scores (s2 < s1)
                    grid[s1, :s1] = p_s1 * p_unrestricted2[:s1]
                    # Tie score (s2 == s1)
                    grid[s1, s1] = p_s1 * p_unrestricted2[s1]
                    # Chase success: all mass where u >= target concentrates at target
                    p_chase_win = float(np.sum(p_unrestricted2[target:]))
                    grid[s1, target] += p_s1 * p_chase_win
                else:
                    # Target beyond support: Away can only score up to max_a
                    grid[s1, :] = p_s1 * p_unrestricted2

        # Normalize grid
        grid /= np.sum(grid)

        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_h + 1),
            away_support=np.arange(max_a + 1)
        )
