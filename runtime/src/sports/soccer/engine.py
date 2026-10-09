"""Soccer engine: Dixon-Coles scorelines, a half-time split and corners, with no hidden xG default (DST-13)."""

from typing import Any, Dict, List, Optional

import numpy as np

from ..base import BaseSportEngine, _first
from .halves import HalfSplit, half_distributions
from ...common.contracts import ScoreDistribution
from ...common.dixon_coles import DixonColesEngine, score_grid
from ...common.errors import InsufficientData, MissingInputs, MissingScore, NotFitted, finite_score
from ...common.leagues import LeagueProfile


class SoccerEngine(BaseSportEngine):
    """Predictive engine for association football (EPL, UCL, La Liga, MLS, ...).

    predict_distribution:  90-minute scoreline from the fitted Dixon-Coles model, or from explicit home_xg/away_xg.
    predict_halves:        first half, second half and a full-time grid built from them (needs a `HalfSplit`).
    """

    def __init__(self, xi: float = 0.002, l2_reg: float = 0.05, league: Optional[LeagueProfile] = None,
                 unknown_team_policy: str = "refuse", rho: Optional[float] = None, half_split: Optional[HalfSplit] = None):
        super().__init__("soccer", league, unknown_team_policy)
        self.dixon_coles = DixonColesEngine(xi=xi, l2_reg=l2_reg, unknown_team=unknown_team_policy)
        self.rho = rho
        self.half_split = half_split

    def fit(self, train_data: Any) -> "SoccerEngine":
        if hasattr(train_data, "to_dict") and hasattr(train_data, "columns"):
            records = train_data.to_dict("records")
        elif isinstance(train_data, (list, tuple)):
            records = list(train_data)
        else:
            raise ValueError("train_data must be a list of match dicts or a DataFrame; an engine is never 'fitted' on nothing")
        matches: List[Dict[str, Any]] = []
        for index, m in enumerate(records):
            if not isinstance(m, dict):
                raise ValueError(f"training record {index} is not a dict")
            home, away = _first(m, ("home", "home_team")), _first(m, ("away", "away_team"))
            if home is None or away is None:
                raise MissingInputs(f"training record {index} lacks home/away team names")
            matches.append({"home": str(home), "away": str(away), "home_goals": int(finite_score(m, "home_goals", "home_score")),
                            "away_goals": int(finite_score(m, "away_goals", "away_score")), "days_ago": float(m.get("days_ago", 0.0))})
        if len(matches) < self.dixon_coles.min_matches:
            raise InsufficientData(f"need at least {self.dixon_coles.min_matches} matches, got {len(matches)}")
        self.dixon_coles.fit(matches)
        self.is_fitted = True
        return self

    def _rho(self, ctx: Dict[str, Any]) -> float:
        if ctx.get("dixon_coles_rho") is not None:
            rho = float(ctx["dixon_coles_rho"])
        elif self.rho is not None:
            rho = self.rho
        elif self.is_fitted and self.dixon_coles.converged:
            rho = self.dixon_coles.rho
        else:
            raise MissingInputs("soccer: dixon_coles_rho is required when scorelines come from explicit xG on an unfitted engine")
        return float(np.clip(rho, -0.25, 0.25))

    def _expected_goals(self, ctx: Dict[str, Any]):
        home, away = ctx.get("home_team") or ctx.get("home"), ctx.get("away_team") or ctx.get("away")
        if ctx.get("home_xg") is not None and ctx.get("away_xg") is not None:
            return float(ctx["home_xg"]), float(ctx["away_xg"]), None
        if ctx.get("home_xg") is not None or ctx.get("away_xg") is not None:
            raise MissingInputs("soccer: give both home_xg and away_xg, or neither")
        if not self.is_fitted:
            raise NotFitted("soccer: fit the engine or pass home_xg and away_xg")
        lam, mu, warnings = self.dixon_coles._rates(home, away)
        return lam, mu, warnings

    def predict_distribution(self, match_context: Dict[str, Any], endpoint: str = "regulation") -> ScoreDistribution:
        if endpoint != "regulation":
            raise ValueError("soccer scorelines settle on the 90 minutes plus stoppage time; extra time and penalties are not modelled")
        home, away = match_context.get("home_team") or match_context.get("home"), match_context.get("away_team") or match_context.get("away")
        explicit = match_context.get("home_xg") is not None and match_context.get("away_xg") is not None
        if not explicit and self.is_fitted:
            return self.dixon_coles.predict_score_distribution(home, away)
        lam, mu, warnings = self._expected_goals(match_context)
        rho = self._rho(match_context)
        for (x, y) in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            if DixonColesEngine.tau(x, y, lam, mu, rho) <= 0.0:
                raise ValueError(f"Invalid Dixon-Coles parameters: tau({x},{y}) <= 0 for xg_home={lam}, xg_away={mu}, rho={rho}")
        return score_grid(lam, mu, rho, 12, "regulation", {"model": "dixon_coles_xg", "lambda_home": lam, "mu_away": mu, "rho": rho,
                                                           "warnings": warnings or []})

    def predict_halves(self, match_context: Dict[str, Any]) -> Dict[str, ScoreDistribution]:
        split = match_context.get("half_split", self.half_split)
        if split is None:
            raise MissingInputs("soccer: halves need a HalfSplit (first-half goal share); fit one with halves.fit_first_half_share")
        lam, mu, warnings = self._expected_goals(match_context)
        halves = half_distributions(lam, mu, split)
        halves["full_time"].metadata["warnings"] = warnings or []
        return halves
