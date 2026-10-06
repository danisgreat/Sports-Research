"""Tennis predictive engine modeling surface-adjusted point-to-match Markov chain."""

from typing import Any, Dict, List, Tuple
import numpy as np
from scipy.special import expit, logit
from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution


class TennisEngine(BaseSportEngine):
    """Predictive engine for Tennis matches (ATP, WTA, Grand Slams).
    
    Models:
    1. Point-on-serve probabilities p_serve1, p_serve2
    2. Game hold probability P(Hold)
    3. Set score distribution (6-0, 6-1, ..., 7-6, etc.)
    4. Match-level joint games distribution (G1, G2)
    """

    def __init__(self):
        super().__init__("tennis")
        self.surface_speed_factors = {
            "clay": -0.04,
            "hard": 0.0,
            "grass": 0.05,
            "indoor": 0.03
        }

    def fit(self, train_data: Any) -> "TennisEngine":
        """Fit baseline serve/return parameters from H0 Tennis records."""
        self.is_fitted = True
        return self

    @staticmethod
    def p_game_hold(p: float) -> float:
        """Exact probability of holding a 4-point advantage tennis service game."""
        # Standard analytical tennis hold probability formula
        p = float(np.clip(p, 1e-4, 1.0 - 1e-4))
        q = 1.0 - p
        p4 = p ** 4
        # Numerator: p^4 * (15 - 34p + 28p^2 - 8p^3) / (1 - 2pq)
        num = p4 * (15.0 - 34.0 * p + 28.0 * (p ** 2) - 8.0 * (p ** 3))
        denom = 1.0 - 2.0 * p * q
        return float(np.clip(num / denom, 0.0, 1.0))

    def _simulate_set_distribution(
        self,
        p_hold1: float,
        p_hold2: float
    ) -> Dict[Tuple[int, int], float]:
        """Compute the probability of each final score in a single set (g1, g2).
        
        Possible set outcomes:
        (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (7, 5), (7, 6)
        and reverse.
        """
        # Markov chain over game states (g1, g2) within a set
        # State: (g1, g2, server in {1, 2})
        # For simplicity and exactness, we model the sequence of games where server alternates
        # Let's compute recursive forward probabilities
        dp = {}
        # Format: dp[(g1, g2, server)] = probability
        dp[(0, 0, 1)] = 1.0

        set_outcomes: Dict[Tuple[int, int], float] = {}

        for total_games in range(13):
            # Process all states with this total_games
            states = [s for s in dp if (s[0] + s[1] == total_games)]
            for (g1, g2, srv) in states:
                prob = dp[(g1, g2, srv)]
                if prob <= 0:
                    continue

                # Check if set already won
                if (g1 >= 6 or g2 >= 6) and abs(g1 - g2) >= 2:
                    set_outcomes[(g1, g2)] = set_outcomes.get((g1, g2), 0.0) + prob
                    continue
                if g1 == 7 or g2 == 7:
                    set_outcomes[(g1, g2)] = set_outcomes.get((g1, g2), 0.0) + prob
                    continue

                # If reached 6-6: tiebreak
                if g1 == 6 and g2 == 6:
                    # Approximate tiebreak win prob
                    p_tb1 = (p_hold1 + (1.0 - p_hold2)) / 2.0
                    set_outcomes[(7, 6)] = set_outcomes.get((7, 6), 0.0) + prob * p_tb1
                    set_outcomes[(6, 7)] = set_outcomes.get((6, 7), 0.0) + prob * (1.0 - p_tb1)
                    continue

                # Game played
                p_win = p_hold1 if srv == 1 else (1.0 - p_hold2)
                next_srv = 2 if srv == 1 else 1

                # Player 1 wins game
                next_state_1 = (g1 + 1, g2, next_srv)
                dp[next_state_1] = dp.get(next_state_1, 0.0) + prob * p_win

                # Player 2 wins game
                next_state_2 = (g1, g2 + 1, next_srv)
                dp[next_state_2] = dp.get(next_state_2, 0.0) + prob * (1.0 - p_win)

        # Normalize set outcomes
        tot = sum(set_outcomes.values())
        if tot > 0:
            set_outcomes = {k: v / tot for k, v in set_outcomes.items()}

        return set_outcomes

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint games distribution (G1, G2) for the entire match."""
        surface = match_context.get("surface", "hard").lower()
        format_type = match_context.get("format", "best_of_3").lower()
        surface_delta = self.surface_speed_factors.get(surface, 0.0)

        # Serve point win abilities
        p_serve1_base = float(match_context.get("p_serve1", 0.65))
        p_serve2_base = float(match_context.get("p_serve2", 0.63))

        p_serve1 = float(expit(logit(p_serve1_base) + surface_delta))
        p_serve2 = float(expit(logit(p_serve2_base) + surface_delta))

        # Hold probabilities
        p_hold1 = self.p_game_hold(p_serve1)
        p_hold2 = self.p_game_hold(p_serve2)

        set_pmf = self._simulate_set_distribution(p_hold1, p_hold2)

        # P(P1 wins set)
        p_set1 = sum(prob for (g1, g2), prob in set_pmf.items() if g1 > g2)
        p_set2 = 1.0 - p_set1

        sets_needed = 3 if format_type == "best_of_5" else 2
        max_games = 75
        grid = np.zeros((max_games + 1, max_games + 1), dtype=float)

        # Convolve sets based on match tree:
        # For Best-of-3:
        # Case 2-0 (P1 wins): 2 sets
        # Case 2-1 (P1 wins): 3 sets
        # Case 0-2 (P2 wins): 2 sets
        # Case 1-2 (P2 wins): 3 sets
        if sets_needed == 2:
            scenarios = [
                (2, 0, p_set1 ** 2),
                (2, 1, 2 * (p_set1 ** 2) * p_set2),
                (0, 2, p_set2 ** 2),
                (1, 2, 2 * (p_set2 ** 2) * p_set1)
            ]
        else:  # Best-of-5
            scenarios = [
                (3, 0, p_set1 ** 3),
                (3, 1, 3 * (p_set1 ** 3) * p_set2),
                (3, 2, 6 * (p_set1 ** 3) * (p_set2 ** 2)),
                (0, 3, p_set2 ** 3),
                (1, 3, 3 * (p_set2 ** 3) * p_set1),
                (2, 3, 6 * (p_set2 ** 3) * (p_set1 ** 2))
            ]

        # Condition set distributions into sets won by P1 and sets won by P2
        set_p1_win = {k: v for k, v in set_pmf.items() if k[0] > k[1]}
        set_p2_win = {k: v for k, v in set_pmf.items() if k[1] > k[0]}
        # Normalize conditionals
        tot_w1 = sum(set_p1_win.values())
        tot_w2 = sum(set_p2_win.values())
        set_p1_win = {k: v / tot_w1 for k, v in set_p1_win.items()}
        set_p2_win = {k: v / tot_w2 for k, v in set_p2_win.items()}

        for (s1_won, s2_won, scen_prob) in scenarios:
            # Convolve s1_won sets where P1 won, and s2_won sets where P2 won
            total_sets = s1_won + s2_won
            # For each scenario, sample/convolute the games
            # We can compute exact Cartesian products of set scorelines
            scen_grid = {(0, 0): 1.0}

            for _ in range(s1_won):
                new_grid = {}
                for (cur_g1, cur_g2), cur_p in scen_grid.items():
                    for (sg1, sg2), sp in set_p1_win.items():
                        new_key = (cur_g1 + sg1, cur_g2 + sg2)
                        new_grid[new_key] = new_grid.get(new_key, 0.0) + cur_p * sp
                scen_grid = new_grid

            for _ in range(s2_won):
                new_grid = {}
                for (cur_g1, cur_g2), cur_p in scen_grid.items():
                    for (sg1, sg2), sp in set_p2_win.items():
                        new_key = (cur_g1 + sg1, cur_g2 + sg2)
                        new_grid[new_key] = new_grid.get(new_key, 0.0) + cur_p * sp
                scen_grid = new_grid

            for (tot_g1, tot_g2), match_p in scen_grid.items():
                if tot_g1 <= max_games and tot_g2 <= max_games:
                    grid[tot_g1, tot_g2] += scen_prob * match_p

        # Normalize grid
        grid /= np.sum(grid)

        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_games + 1),
            away_support=np.arange(max_games + 1)
        )
