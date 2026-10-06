"""Event-first distribution modeling and contract derivation engine.

Guarantees logical monotonicity and coherence across all derived betting markets
by pricing every contract from a single underlying score probability distribution.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import numpy as np


@dataclass
class ScoreDistribution:
    """Joint discrete score probability distribution matrix P(Home = s1, Away = s2)."""
    grid: np.ndarray  # Shape: (max_home + 1, max_away + 1)
    home_support: np.ndarray  # 1D array of possible home scores [0, 1, ..., H]
    away_support: np.ndarray  # 1D array of possible away scores [0, 1, ..., A]

    def __post_init__(self):
        # Ensure valid probability distribution
        total_mass = float(np.sum(self.grid))
        if not np.isclose(total_mass, 1.0, atol=1e-3):
            # Normalize to 1.0 if minor numerical drift
            if total_mass > 0:
                self.grid = self.grid / total_mass
            else:
                raise ValueError("Score distribution grid must have non-zero probability mass")

    @classmethod
    def from_independent_marginals(cls, p_home: np.ndarray, p_away: np.ndarray) -> "ScoreDistribution":
        """Construct joint distribution assuming independence (Kronecker outer product)."""
        grid = np.outer(p_home, p_away)
        home_supp = np.arange(len(p_home))
        away_supp = np.arange(len(p_away))
        return cls(grid=grid, home_support=home_supp, away_support=away_supp)

    @classmethod
    def from_bivariate_poisson(
        cls,
        lambda1: float,
        lambda2: float,
        lambda3: float = 0.0,
        max_score: int = 15
    ) -> "ScoreDistribution":
        """Bivariate Poisson with covariance parameter lambda3 (e.g. Holgate / Karlis-Ntzoufras)."""
        from scipy.stats import poisson
        grid = np.zeros((max_score + 1, max_score + 1), dtype=float)

        if lambda3 == 0.0:
            p1 = poisson.pmf(np.arange(max_score + 1), lambda1)
            p2 = poisson.pmf(np.arange(max_score + 1), lambda2)
            grid = np.outer(p1, p2)
        else:
            # Full Holgate bivariate Poisson joint PMF
            for x in range(max_score + 1):
                for y in range(max_score + 1):
                    prob = 0.0
                    for k in range(min(x, y) + 1):
                        prob += (
                            poisson.pmf(x - k, lambda1)
                            * poisson.pmf(y - k, lambda2)
                            * poisson.pmf(k, lambda3)
                        )
                    grid[x, y] = prob

        # Normalize truncated mass
        grid /= np.sum(grid)
        return cls(
            grid=grid,
            home_support=np.arange(max_score + 1),
            away_support=np.arange(max_score + 1)
        )

    def p_home_win(self) -> float:
        """P(Home Score > Away Score)"""
        mask = np.greater.outer(self.home_support, self.away_support)
        return float(np.sum(self.grid[mask]))

    def p_away_win(self) -> float:
        """P(Away Score > Home Score)"""
        mask = np.less.outer(self.home_support, self.away_support)
        return float(np.sum(self.grid[mask]))

    def p_draw(self) -> float:
        """P(Home Score == Away Score)"""
        mask = np.equal.outer(self.home_support, self.away_support)
        return float(np.sum(self.grid[mask]))

    def p_double_chance(self, selection: str) -> float:
        """Selections: '1X' (Home or Draw), 'X2' (Draw or Away), '12' (Home or Away)."""
        sel = selection.upper().strip()
        if sel == "1X":
            return self.p_home_win() + self.p_draw()
        elif sel == "X2":
            return self.p_away_win() + self.p_draw()
        elif sel == "12":
            return self.p_home_win() + self.p_away_win()
        else:
            raise ValueError(f"Unknown double chance selection '{selection}'")

    def p_draw_no_bet(self, side: str) -> float:
        """P(Side wins | No Draw)"""
        p_h = self.p_home_win()
        p_a = self.p_away_win()
        denom = p_h + p_a
        if denom == 0:
            return 0.5
        side_clean = side.lower().strip()
        if side_clean == "home":
            return float(p_h / denom)
        elif side_clean == "away":
            return float(p_a / denom)
        else:
            raise ValueError(f"Unknown DNB side '{side}'")

    def p_over(self, line: float) -> float:
        """P(Home + Away > line)"""
        tot_matrix = np.add.outer(self.home_support, self.away_support)
        return float(np.sum(self.grid[tot_matrix > line]))

    def p_under(self, line: float) -> float:
        """P(Home + Away < line)"""
        tot_matrix = np.add.outer(self.home_support, self.away_support)
        return float(np.sum(self.grid[tot_matrix < line]))

    def p_push_total(self, line: float) -> float:
        """P(Home + Away == line)"""
        tot_matrix = np.add.outer(self.home_support, self.away_support)
        return float(np.sum(self.grid[tot_matrix == line]))

    def p_home_cover(self, spread: float) -> float:
        """P(Home Score - Away Score + spread > 0)."""
        margin_matrix = np.subtract.outer(self.home_support, self.away_support)
        return float(np.sum(self.grid[margin_matrix + spread > 0]))

    def p_away_cover(self, spread: float) -> float:
        """P(Away Score - Home Score + spread > 0)."""
        margin_matrix = np.subtract.outer(self.away_support, self.home_support)
        return float(np.sum(self.grid[margin_matrix + spread > 0]))

    def p_push_spread(self, spread: float) -> float:
        """P(Home Score - Away Score + spread == 0)."""
        margin_matrix = np.subtract.outer(self.home_support, self.away_support)
        return float(np.sum(self.grid[margin_matrix + spread == 0]))

    def p_team_total_over(self, team: str, line: float) -> float:
        """P(Team score > line)"""
        if team.lower().strip() == "home":
            p_home_marginal = np.sum(self.grid, axis=1)
            return float(np.sum(p_home_marginal[self.home_support > line]))
        elif team.lower().strip() == "away":
            p_away_marginal = np.sum(self.grid, axis=0)
            return float(np.sum(p_away_marginal[self.away_support > line]))
        else:
            raise ValueError(f"Unknown team '{team}'")

    def p_team_total_under(self, team: str, line: float) -> float:
        """P(Team score < line)"""
        if team.lower().strip() == "home":
            p_home_marginal = np.sum(self.grid, axis=1)
            return float(np.sum(p_home_marginal[self.home_support < line]))
        elif team.lower().strip() == "away":
            p_away_marginal = np.sum(self.grid, axis=0)
            return float(np.sum(p_away_marginal[self.away_support < line]))
        else:
            raise ValueError(f"Unknown team '{team}'")

    def p_btts_yes(self) -> float:
        """Both Teams to Score (Home > 0 AND Away > 0)"""
        subgrid = self.grid[1:, 1:]
        return float(np.sum(subgrid))

    def p_btts_no(self) -> float:
        return 1.0 - self.p_btts_yes()

    def expected_scores(self) -> Tuple[float, float]:
        """Expected home and away scores (mu_home, mu_away)."""
        p_home = np.sum(self.grid, axis=1)
        p_away = np.sum(self.grid, axis=0)
        mu_h = float(np.sum(self.home_support * p_home))
        mu_a = float(np.sum(self.away_support * p_away))
        return (mu_h, mu_a)


class DerivedContracts:
    """Helper to verify mathematical invariants on derived contracts."""

    @staticmethod
    def verify_totals_monotonicity(score_dist: ScoreDistribution, lines: List[float]) -> bool:
        """Verify P(Over L1) >= P(Over L2) for all L1 < L2."""
        sorted_lines = sorted(lines)
        over_probs = [score_dist.p_over(l) for l in sorted_lines]
        for i in range(len(over_probs) - 1):
            if over_probs[i] < over_probs[i + 1] - 1e-9:
                return False
        return True

    @staticmethod
    def verify_spread_monotonicity(score_dist: ScoreDistribution, spreads: List[float]) -> bool:
        """Verify P(Cover S1) <= P(Cover S2) for S1 < S2 (giving fewer points to underdog or taking more from favorite)."""
        sorted_spreads = sorted(spreads)
        cover_probs = [score_dist.p_home_cover(s) for s in sorted_spreads]
        for i in range(len(cover_probs) - 1):
            if cover_probs[i] > cover_probs[i + 1] + 1e-9:
                return False
        return True

    @staticmethod
    def verify_covering_pair(score_dist: ScoreDistribution, positive_spread: float) -> bool:
        """Verify P(Home +k) >= P(Home ML) for any k >= 0."""
        if positive_spread < 0:
            raise ValueError("Spread must be non-negative for positive handicap invariant check")
        p_cover = score_dist.p_home_cover(positive_spread)
        p_ml = score_dist.p_home_win()
        return p_cover >= (p_ml - 1e-9)

