"""Soccer predictive engine modeling bivariate expected goals (xG) and scoreline matrix."""

from typing import Any, Dict, List
import numpy as np
from scipy.stats import poisson
from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution
from ...common.dixon_coles import DixonColesEngine


class SoccerEngine(BaseSportEngine):
    """Predictive engine for Soccer matches (EPL, UCL, La Liga, MLS, etc.)."""

    def __init__(self, xi: float = 0.002, l2_reg: float = 0.05):
        super().__init__("soccer")
        self.dixon_coles = DixonColesEngine(xi=xi, l2_reg=l2_reg)
        self.is_fitted = False

    def fit(self, train_data: Any) -> "SoccerEngine":
        """Fit attack/defence parameters and Dixon-Coles dependency from match records."""
        matches: List[Dict[str, Any]] = []
        if isinstance(train_data, list):
            for m in train_data:
                if isinstance(m, dict):
                    matches.append({
                        "home": m.get("home") or m.get("home_team"),
                        "away": m.get("away") or m.get("away_team"),
                        "home_goals": int(m.get("home_goals") if m.get("home_goals") is not None else m.get("home_score", 0)),
                        "away_goals": int(m.get("away_goals") if m.get("away_goals") is not None else m.get("away_score", 0)),
                        "days_ago": float(m.get("days_ago", 0.0))
                    })
        elif hasattr(train_data, "iterrows"):
            for _, row in train_data.iterrows():
                matches.append({
                    "home": row.get("home") or row.get("home_team"),
                    "away": row.get("away") or row.get("away_team"),
                    "home_goals": int(row.get("home_goals") if "home_goals" in row else row.get("home_score", 0)),
                    "away_goals": int(row.get("away_goals") if "away_goals" in row else row.get("away_score", 0)),
                    "days_ago": float(row.get("days_ago", 0.0))
                })

        if matches:
            self.dixon_coles.fit(matches)

        self.is_fitted = True
        return self

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint score matrix from Dixon-Coles model or expected goals (xG)."""
        home_team = match_context.get("home_team") or match_context.get("home")
        away_team = match_context.get("away_team") or match_context.get("away")

        # If fitted and teams known in Dixon-Coles dictionary, use Dixon-Coles prediction
        if (
            self.is_fitted
            and home_team in self.dixon_coles.team_idx
            and away_team in self.dixon_coles.team_idx
            and "home_xg" not in match_context
        ):
            return self.dixon_coles.predict_score_distribution(home_team, away_team)

        # Otherwise use contextual expected goals (xG) with validated rho
        xg_home = float(match_context.get("home_xg", 1.55))
        xg_away = float(match_context.get("away_xg", 1.20))
        rho = float(match_context.get("dixon_coles_rho", getattr(self.dixon_coles, "rho", -0.04)))
        rho = float(np.clip(rho, -0.25, 0.25))

        # Check tau validity
        for (x, y) in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            factor = DixonColesEngine.tau(x, y, xg_home, xg_away, rho)
            if factor <= 0.0:
                raise ValueError(
                    f"Invalid Dixon-Coles parameters: tau({x},{y})={factor} <= 0 "
                    f"for xg_home={xg_home}, xg_away={xg_away}, rho={rho}"
                )

        max_goals = 12
        grid = np.zeros((max_goals + 1, max_goals + 1), dtype=float)

        p_h = poisson.pmf(np.arange(max_goals + 1), xg_home)
        p_a = poisson.pmf(np.arange(max_goals + 1), xg_away)

        for x in range(max_goals + 1):
            for y in range(max_goals + 1):
                adj = DixonColesEngine.tau(x, y, xg_home, xg_away, rho)
                grid[x, y] = p_h[x] * p_a[y] * adj

        grid /= np.sum(grid)
        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_goals + 1),
            away_support=np.arange(max_goals + 1)
        )

