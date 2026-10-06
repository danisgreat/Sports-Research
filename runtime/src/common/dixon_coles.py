"""Dixon-Coles Poisson regression model with time-decay and low-score dependency."""

from typing import Dict, List, Optional, Tuple
import numpy as np
from scipy.optimize import minimize
from scipy.stats import poisson
from .contracts import ScoreDistribution


class DixonColesEngine:
    """Full implementation of the Dixon & Coles (1997) model for association football.
    
    Estimates:
    - Team attack parameters alpha_i
    - Team defence parameters beta_j
    - Home ground advantage gamma
    - Low-score dependence parameter rho
    - Exponential time-decay weighting exp(-xi * (t_now - t_match))
    """

    def __init__(self, xi: float = 0.002, l2_reg: float = 0.05):
        self.xi = xi  # Daily decay rate (xi = 0.002 corresponds to half-life ~346 days)
        self.l2_reg = l2_reg
        self.teams: List[str] = []
        self.team_idx: Dict[str, int] = {}
        self.attacks: np.ndarray = np.array([])
        self.defences: np.ndarray = np.array([])
        self.home_adv: float = 0.25
        self.rho: float = -0.04

    @staticmethod
    def tau(x: int, y: int, lambda_h: float, mu_a: float, rho: float) -> float:
        """Dixon-Coles low-score dependency factor."""
        if x == 0 and y == 0:
            return 1.0 - lambda_h * mu_a * rho
        elif x == 0 and y == 1:
            return 1.0 + lambda_h * rho
        elif x == 1 and y == 0:
            return 1.0 + mu_a * rho
        elif x == 1 and y == 1:
            return 1.0 - rho
        return 1.0

    def fit(self, matches: List[Dict[str, any]], current_time_days: Optional[float] = None) -> "DixonColesEngine":
        """Fit parameters via weighted maximum likelihood.
        
        matches format: [{
            "home": "Arsenal", "away": "Chelsea",
            "home_goals": 2, "away_goals": 1,
            "days_ago": 14.0 (optional)
        }]
        """
        all_teams = sorted(list(set(m["home"] for m in matches).union(set(m["away"] for m in matches))))
        self.teams = all_teams
        self.team_idx = {t: i for i, t in enumerate(all_teams)}
        n_teams = len(all_teams)

        if n_teams < 2:
            return self

        # Precompute weights from days_ago
        weights = []
        for m in matches:
            days = float(m.get("days_ago", 0.0))
            w = np.exp(-self.xi * days)
            weights.append(w)
        weights = np.array(weights)

        # Parameter vector: [alphas (n_teams), betas (n_teams), home_adv, rho]
        # Dimension: 2 * n_teams + 2
        def objective(params):
            alphas = params[:n_teams]
            betas = params[n_teams:2 * n_teams]
            gamma = params[2 * n_teams]
            rho = params[2 * n_teams + 1]

            nll = 0.0
            for k, m in enumerate(matches):
                i = self.team_idx[m["home"]]
                j = self.team_idx[m["away"]]
                hg = int(m["home_goals"])
                ag = int(m["away_goals"])

                lambda_h = np.exp(alphas[i] + betas[j] + gamma)
                mu_a = np.exp(alphas[j] + betas[i])

                p_base = poisson.pmf(hg, lambda_h) * poisson.pmf(ag, mu_a)
                adj = self.tau(hg, ag, lambda_h, mu_a, rho)
                p_joint = max(p_base * adj, 1e-12)

                nll -= weights[k] * np.log(p_joint)

            # Identification and regularization: mean(alpha) = 0 constraint
            nll += 100.0 * (np.sum(alphas) ** 2)
            nll += 0.5 * self.l2_reg * (np.sum(alphas ** 2) + np.sum(betas ** 2))
            nll += 0.5 * self.l2_reg * (gamma ** 2 + rho ** 2)
            return nll

        init_params = np.zeros(2 * n_teams + 2)
        init_params[2 * n_teams] = 0.25  # Initial home advantage
        init_params[2 * n_teams + 1] = -0.04  # Initial rho

        res = minimize(objective, init_params, method="BFGS")
        if res.success:
            self.attacks = res.x[:n_teams]
            self.defences = res.x[n_teams:2 * n_teams]
            self.home_adv = float(res.x[2 * n_teams])
            self.rho = float(res.x[2 * n_teams + 1])
        else:
            self.attacks = np.zeros(n_teams)
            self.defences = np.zeros(n_teams)
            self.home_adv = 0.25
            self.rho = -0.04

        return self

    def predict_score_distribution(
        self,
        home_team: str,
        away_team: str,
        max_goals: int = 12
    ) -> ScoreDistribution:
        """Produce joint score distribution ScoreDistribution."""
        idx_h = self.team_idx.get(home_team)
        idx_a = self.team_idx.get(away_team)

        if idx_h is None or idx_a is None:
            # Neutral baseline ~ 1.35 goals per team
            lambda_h = 1.45
            mu_a = 1.20
        else:
            lambda_h = np.exp(self.attacks[idx_h] + self.defences[idx_a] + self.home_adv)
            mu_a = np.exp(self.attacks[idx_a] + self.defences[idx_h])

        grid = np.zeros((max_goals + 1, max_goals + 1), dtype=float)
        p_h = poisson.pmf(np.arange(max_goals + 1), lambda_h)
        p_a = poisson.pmf(np.arange(max_goals + 1), mu_a)

        for x in range(max_goals + 1):
            for y in range(max_goals + 1):
                adj = self.tau(x, y, lambda_h, mu_a, self.rho)
                grid[x, y] = p_h[x] * p_a[y] * max(adj, 0.0)

        grid /= np.sum(grid)
        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_goals + 1),
            away_support=np.arange(max_goals + 1)
        )
