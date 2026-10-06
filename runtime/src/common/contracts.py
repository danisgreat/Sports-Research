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
    p_match_home_win: Optional[float] = None
    p_match_away_win: Optional[float] = None
    p_match_draw: Optional[float] = None

    def __post_init__(self):
        # Validate grid numerical validity and non-negativity
        if np.any(np.isnan(self.grid)) or np.any(np.isinf(self.grid)):
            raise ValueError("Score distribution grid contains NaN or Inf")
        if np.any(self.grid < -1e-12):
            raise ValueError("Score distribution grid cannot contain negative probability mass")

        self.grid = np.clip(self.grid, 0.0, None)
        total_mass = float(np.sum(self.grid))
        if total_mass <= 0 or not np.isfinite(total_mass):
            raise ValueError("Score distribution grid must have positive finite mass")

        # Always renormalize to unit probability
        self.grid = self.grid / total_mass

        if self.grid.shape != (len(self.home_support), len(self.away_support)):
            raise ValueError(
                f"Grid shape {self.grid.shape} does not match support lengths "
                f"({len(self.home_support)}, {len(self.away_support)})"
            )

        # Validate decoupled match win probabilities if provided
        for name, val in [
            ("p_match_home_win", self.p_match_home_win),
            ("p_match_away_win", self.p_match_away_win),
            ("p_match_draw", self.p_match_draw),
        ]:
            if val is not None:
                if val < -1e-12 or val > 1.0 + 1e-12 or not np.isfinite(val):
                    raise ValueError(f"{name} must be in [0, 1], got {val}")

        # Enforce consistency of match winner probability vector
        provided_wins = [x for x in [self.p_match_home_win, self.p_match_away_win] if x is not None]
        if len(provided_wins) == 2:
            p_h = self.p_match_home_win
            p_a = self.p_match_away_win
            p_d = self.p_match_draw if self.p_match_draw is not None else 0.0
            total_match_p = p_h + p_a + p_d
            if abs(total_match_p - 1.0) > 1e-5:
                raise ValueError(
                    f"Decoupled match win probabilities must sum to 1.0, got sum={total_match_p:.4f} "
                    f"(home={p_h}, away={p_a}, draw={p_d})"
                )

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
        """P(Home Score > Away Score) or decoupled match win probability."""
        if self.p_match_home_win is not None:
            return float(np.clip(self.p_match_home_win, 0.0, 1.0))
        home_col = self.home_support[:, np.newaxis]
        away_row = self.away_support[np.newaxis, :]
        return float(np.sum(self.grid[home_col > away_row]))

    def p_away_win(self) -> float:
        """P(Away Score > Home Score) or decoupled match win probability."""
        if self.p_match_away_win is not None:
            return float(np.clip(self.p_match_away_win, 0.0, 1.0))
        home_col = self.home_support[:, np.newaxis]
        away_row = self.away_support[np.newaxis, :]
        return float(np.sum(self.grid[away_row > home_col]))

    def p_draw(self) -> float:
        """P(Home Score == Away Score) or decoupled match draw probability."""
        if self.p_match_draw is not None:
            return float(np.clip(self.p_match_draw, 0.0, 1.0))
        home_col = self.home_support[:, np.newaxis]
        away_row = self.away_support[np.newaxis, :]
        return float(np.sum(self.grid[home_col == away_row]))

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
        home_col = self.home_support[:, np.newaxis]
        away_row = self.away_support[np.newaxis, :]
        tot_matrix = home_col + away_row
        return float(np.sum(self.grid[tot_matrix > line]))

    def p_under(self, line: float) -> float:
        """P(Home + Away < line)"""
        home_col = self.home_support[:, np.newaxis]
        away_row = self.away_support[np.newaxis, :]
        tot_matrix = home_col + away_row
        return float(np.sum(self.grid[tot_matrix < line]))

    def p_push_total(self, line: float) -> float:
        """P(Home + Away == line)"""
        home_col = self.home_support[:, np.newaxis]
        away_row = self.away_support[np.newaxis, :]
        tot_matrix = home_col + away_row
        return float(np.sum(self.grid[tot_matrix == line]))

    def p_home_cover(self, spread: float) -> float:
        """P(Home Score - Away Score + spread > 0)."""
        home_col = self.home_support[:, np.newaxis]
        away_row = self.away_support[np.newaxis, :]
        h_margin = home_col - away_row
        return float(np.sum(self.grid[h_margin + spread > 0]))

    def p_away_cover(self, spread: float) -> float:
        """P(Away Score - Home Score + spread > 0)."""
        home_col = self.home_support[:, np.newaxis]
        away_row = self.away_support[np.newaxis, :]
        a_margin = away_row - home_col
        return float(np.sum(self.grid[a_margin + spread > 0]))

    def p_push_spread(self, spread: float, side: str = "home") -> float:
        """P(Margin + spread == 0)."""
        home_col = self.home_support[:, np.newaxis]
        away_row = self.away_support[np.newaxis, :]
        if side.lower().strip() == "away":
            a_margin = away_row - home_col
            return float(np.sum(self.grid[a_margin + spread == 0]))
        else:
            h_margin = home_col - away_row
            return float(np.sum(self.grid[h_margin + spread == 0]))

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

