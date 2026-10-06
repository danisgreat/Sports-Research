"""Elo and Draw-Aware Bradley-Terry rating models."""

from typing import Dict, List, Optional, Tuple
import numpy as np
from scipy.optimize import minimize


class EloRatingEngine:
    """Dynamic Elo rating engine with surface and home-advantage adjustments."""

    def __init__(self, base_rating: float = 1500.0, k_factor: float = 32.0, home_advantage: float = 65.0):
        self.base_rating = base_rating
        self.k_factor = k_factor
        self.home_advantage = home_advantage
        self.ratings: Dict[str, float] = {}

    def get_rating(self, entity: str) -> float:
        return self.ratings.get(entity, self.base_rating)

    def predict_prob(self, entity_a: str, entity_b: str, is_neutral: bool = False) -> float:
        """Win probability for entity_a against entity_b."""
        r_a = self.get_rating(entity_a) + (0.0 if is_neutral else self.home_advantage)
        r_b = self.get_rating(entity_b)
        return 1.0 / (1.0 + 10.0 ** ((r_b - r_a) / 400.0))

    def update(self, entity_a: str, entity_b: str, score_a: float, is_neutral: bool = False) -> Tuple[float, float]:
        """Update ratings post-match. score_a in {1.0 (win), 0.5 (draw), 0.0 (loss)}."""
        p_a = self.predict_prob(entity_a, entity_b, is_neutral=is_neutral)
        p_b = 1.0 - p_a

        r_a = self.get_rating(entity_a)
        r_b = self.get_rating(entity_b)

        r_a_new = r_a + self.k_factor * (score_a - p_a)
        r_b_new = r_b + self.k_factor * ((1.0 - score_a) - p_b)

        self.ratings[entity_a] = r_a_new
        self.ratings[entity_b] = r_b_new
        return r_a_new, r_b_new


class BradleyTerryDrawEngine:
    """Regularized Bradley-Terry model with Rao-Davidson draw parameter.
    
    P(A wins) = pi_A / (pi_A + pi_B + nu * sqrt(pi_A * pi_B))
    P(Draw)   = (nu * sqrt(pi_A * pi_B)) / (pi_A + pi_B + nu * sqrt(pi_A * pi_B))
    P(B wins) = pi_B / (pi_A + pi_B + nu * sqrt(pi_A * pi_B))
    where pi_i = exp(gamma_i).
    """

    def __init__(self, l2_reg: float = 0.1):
        self.l2_reg = l2_reg
        self.teams: List[str] = []
        self.team_indices: Dict[str, int] = {}
        self.log_strengths: np.ndarray = np.array([])
        self.log_nu: float = 0.0  # log(draw_parameter)

    def fit(self, matches: List[Dict[str, any]]) -> "BradleyTerryDrawEngine":
        """Fit parameters via maximum likelihood on a list of matches.
        
        matches format: [{"home": "teamA", "away": "teamB", "result": "home" | "draw" | "away"}]
        """
        # Collect distinct teams
        all_teams = sorted(list(set(m["home"] for m in matches).union(set(m["away"] for m in matches))))
        self.teams = all_teams
        self.team_indices = {t: idx for idx, t in enumerate(all_teams)}
        n_teams = len(all_teams)

        if n_teams == 0:
            return self

        # Objective function
        def neg_log_likelihood(params):
            log_strengths = params[:n_teams]
            log_nu = params[n_teams]
            nu = np.exp(log_nu)

            # Identification constraint: mean of log strengths is 0
            nll = 0.0
            for m in matches:
                idx_h = self.team_indices[m["home"]]
                idx_a = self.team_indices[m["away"]]
                pi_h = np.exp(log_strengths[idx_h])
                pi_a = np.exp(log_strengths[idx_a])
                draw_mass = nu * np.sqrt(pi_h * pi_a)
                denom = pi_h + pi_a + draw_mass

                res = m["result"].lower()
                if res in ("home", "1"):
                    p = pi_h / denom
                elif res in ("draw", "x", "tie"):
                    p = draw_mass / denom
                else:  # away, 2
                    p = pi_a / denom

                nll -= np.log(max(p, 1e-12))

            # Regularization penalty
            nll += 0.5 * self.l2_reg * np.sum(log_strengths ** 2)
            nll += 0.5 * self.l2_reg * (log_nu ** 2)
            return nll

        init_params = np.zeros(n_teams + 1)
        res = minimize(neg_log_likelihood, init_params, method="BFGS")
        if res.success:
            self.log_strengths = res.x[:n_teams]
            self.log_nu = float(res.x[n_teams])
        else:
            self.log_strengths = np.zeros(n_teams)
            self.log_nu = 0.0

        return self

    def predict_probs(self, team_home: str, team_away: str) -> Tuple[float, float, float]:
        """Returns (p_home, p_draw, p_away)."""
        idx_h = self.team_indices.get(team_home)
        idx_a = self.team_indices.get(team_away)
        if idx_h is None or idx_a is None or len(self.log_strengths) == 0:
            return (1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0)

        pi_h = np.exp(self.log_strengths[idx_h])
        pi_a = np.exp(self.log_strengths[idx_a])
        nu = np.exp(self.log_nu)
        draw_mass = nu * np.sqrt(pi_h * pi_a)
        denom = pi_h + pi_a + draw_mass

        return (float(pi_h / denom), float(draw_mass / denom), float(pi_a / denom))
