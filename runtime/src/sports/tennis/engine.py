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
        self.tour_avg_serve: float = 0.64
        self.tour_avg_return: float = 0.36
        self.player_stats: Dict[str, Dict[str, float]] = {}

    def fit(self, train_data: Any) -> "TennisEngine":
        """Fit baseline player serve and return win percentages from historical match records."""
        self.player_stats: Dict[str, Dict[str, float]] = {}
        self.tour_avg_serve: float = 0.64
        self.tour_avg_return: float = 0.36

        if isinstance(train_data, list):
            accum: Dict[str, Dict[str, float]] = {}
            for m in train_data:
                if not isinstance(m, dict):
                    continue
                p1 = m.get("player1") or m.get("winner")
                p2 = m.get("player2") or m.get("loser")
                
                # Winner stats
                p1_sv_won = float(m.get("p1_serve_won") or m.get("w_1stWon", 0) + m.get("w_2ndWon", 0) or 0)
                p1_sv_tot = float(m.get("p1_serve_total") or m.get("w_svpt", 0) or 0)
                # Loser stats
                p2_sv_won = float(m.get("p2_serve_won") or m.get("l_1stWon", 0) + m.get("l_2ndWon", 0) or 0)
                p2_sv_tot = float(m.get("p2_serve_total") or m.get("l_svpt", 0) or 0)

                if p1:
                    if p1 not in accum:
                        accum[p1] = {"sv_won": 0.0, "sv_tot": 0.0, "ret_won": 0.0, "ret_tot": 0.0}
                    accum[p1]["sv_won"] += p1_sv_won
                    accum[p1]["sv_tot"] += p1_sv_tot
                    if p2_sv_tot > 0:
                        accum[p1]["ret_won"] += (p2_sv_tot - p2_sv_won)
                        accum[p1]["ret_tot"] += p2_sv_tot

                if p2:
                    if p2 not in accum:
                        accum[p2] = {"sv_won": 0.0, "sv_tot": 0.0, "ret_won": 0.0, "ret_tot": 0.0}
                    accum[p2]["sv_won"] += p2_sv_won
                    accum[p2]["sv_tot"] += p2_sv_tot
                    if p1_sv_tot > 0:
                        accum[p2]["ret_won"] += (p1_sv_tot - p1_sv_won)
                        accum[p2]["ret_tot"] += p1_sv_tot

            tot_sv_won = sum(s["sv_won"] for s in accum.values())
            tot_sv_tot = sum(s["sv_tot"] for s in accum.values())
            if tot_sv_tot >= 100:
                self.tour_avg_serve = tot_sv_won / tot_sv_tot
                self.tour_avg_return = 1.0 - self.tour_avg_serve

            for p, s in accum.items():
                p_sv = s["sv_won"] / s["sv_tot"] if s["sv_tot"] >= 10 else self.tour_avg_serve
                p_ret = s["ret_won"] / s["ret_tot"] if s["ret_tot"] >= 10 else self.tour_avg_return
                self.player_stats[p] = {
                    "serve_win_rate": p_sv,
                    "return_win_rate": p_ret
                }

        self.is_fitted = True
        return self

    @staticmethod
    def p_game_hold(p: float) -> float:
        """Exact probability of holding a 4-point advantage tennis service game."""
        p = float(np.clip(p, 1e-4, 1.0 - 1e-4))
        q = 1.0 - p
        p4 = p ** 4
        num = p4 * (15.0 - 34.0 * p + 28.0 * (p ** 2) - 8.0 * (p ** 3))
        denom = 1.0 - 2.0 * p * q
        return float(np.clip(num / denom, 0.0, 1.0))

    @staticmethod
    def p_tiebreak_win(p_s1: float, p_s2: float) -> float:
        """Exact 7-point tennis tiebreak win probability using Markov DP and deuce closed form.
        
        Serving order:
        Pt 0: P1 serves.
        Pts 1, 2: P2 serves.
        Pts 3, 4: P1 serves.
        Pts 5, 6: P2 serves, etc.
        """
        p_s1 = float(np.clip(p_s1, 0.05, 0.95))
        p_s2 = float(np.clip(p_s2, 0.05, 0.95))
        dp: Dict[Tuple[int, int], float] = {(0, 0): 1.0}
        p_win = 0.0

        for total_pts in range(12):
            # Determine server for point total_pts:
            # 0: S1, 1: S2, 2: S2, 3: S1, 4: S1, 5: S2, 6: S2, 7: S1, 8: S1, 9: S2, 10: S2, 11: S1
            server = 1 if (total_pts == 0 or ((total_pts - 1) // 2) % 2 == 1) else 2
            p_pt1 = p_s1 if server == 1 else (1.0 - p_s2)

            next_dp: Dict[Tuple[int, int], float] = {}
            for (i, j), prob in dp.items():
                if prob <= 0:
                    continue
                # Point to P1
                if i + 1 == 7 and j <= 5:
                    p_win += prob * p_pt1
                elif i + 1 < 7 or (i + 1 == 6 and j == 6):
                    next_dp[(i + 1, j)] = next_dp.get((i + 1, j), 0.0) + prob * p_pt1

                # Point to P2
                if j + 1 == 7 and i <= 5:
                    pass  # P2 wins
                elif j + 1 < 7 or (i == 6 and j + 1 == 6):
                    next_dp[(i, j + 1)] = next_dp.get((i, j + 1), 0.0) + prob * (1.0 - p_pt1)

            dp = next_dp

        # Closed form absorption from 6-6 deuce:
        # Over a 2-point cycle (one on P2 serve, one on P1 serve):
        p_6_6 = dp.get((6, 6), 0.0)
        if p_6_6 > 0:
            a = 1.0 - p_s2  # P1 wins on P2 serve
            b = p_s1        # P1 wins on P1 serve
            denom = a * b + (1.0 - a) * (1.0 - b)
            p_deuce_win = (a * b) / max(denom, 1e-12)
            p_win += p_6_6 * p_deuce_win

        return float(np.clip(p_win, 0.0, 1.0))

    def _simulate_set_distribution(
        self,
        p_hold1: float,
        p_hold2: float,
        p_s1: float = 0.65,
        p_s2: float = 0.63
    ) -> Dict[Tuple[int, int], float]:
        """Compute the probability of each final score in a single set (g1, g2) using exact tiebreaks."""
        dp = {}
        dp[(0, 0, 1)] = 1.0

        set_outcomes: Dict[Tuple[int, int], float] = {}

        for total_games in range(13):
            states = [s for s in dp if (s[0] + s[1] == total_games)]
            for (g1, g2, srv) in states:
                prob = dp[(g1, g2, srv)]
                if prob <= 0:
                    continue

                if (g1 >= 6 or g2 >= 6) and abs(g1 - g2) >= 2:
                    set_outcomes[(g1, g2)] = set_outcomes.get((g1, g2), 0.0) + prob
                    continue
                if g1 == 7 or g2 == 7:
                    set_outcomes[(g1, g2)] = set_outcomes.get((g1, g2), 0.0) + prob
                    continue

                if g1 == 6 and g2 == 6:
                    p_tb1 = self.p_tiebreak_win(p_s1, p_s2)
                    set_outcomes[(7, 6)] = set_outcomes.get((7, 6), 0.0) + prob * p_tb1
                    set_outcomes[(6, 7)] = set_outcomes.get((6, 7), 0.0) + prob * (1.0 - p_tb1)
                    continue

                p_win = p_hold1 if srv == 1 else (1.0 - p_hold2)
                next_srv = 2 if srv == 1 else 1

                next_state_1 = (g1 + 1, g2, next_srv)
                dp[next_state_1] = dp.get(next_state_1, 0.0) + prob * p_win

                next_state_2 = (g1, g2 + 1, next_srv)
                dp[next_state_2] = dp.get(next_state_2, 0.0) + prob * (1.0 - p_win)

        tot = sum(set_outcomes.values())
        if tot > 0:
            set_outcomes = {k: v / tot for k, v in set_outcomes.items()}

        return set_outcomes

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint games distribution (G1, G2) and exact set-based match win probabilities."""
        surface = match_context.get("surface", "hard").lower()
        format_type = match_context.get("format", "best_of_3").lower()
        surface_delta = self.surface_speed_factors.get(surface, 0.0)

        p1_name = match_context.get("player1") or match_context.get("home_team")
        p2_name = match_context.get("player2") or match_context.get("away_team")

        # Baseline serve and return rates
        p_serve1_base = match_context.get("p_serve1")
        p_ret1_base = match_context.get("p_return1")
        if hasattr(self, "player_stats") and p1_name in self.player_stats:
            if p_serve1_base is None:
                p_serve1_base = self.player_stats[p1_name]["serve_win_rate"]
            if p_ret1_base is None:
                p_ret1_base = self.player_stats[p1_name]["return_win_rate"]
        if p_serve1_base is None:
            p_serve1_base = self.tour_avg_serve
        if p_ret1_base is None:
            p_ret1_base = self.tour_avg_return

        p_serve2_base = match_context.get("p_serve2")
        p_ret2_base = match_context.get("p_return2")
        if hasattr(self, "player_stats") and p2_name in self.player_stats:
            if p_serve2_base is None:
                p_serve2_base = self.player_stats[p2_name]["serve_win_rate"]
            if p_ret2_base is None:
                p_ret2_base = self.player_stats[p2_name]["return_win_rate"]
        if p_serve2_base is None:
            p_serve2_base = self.tour_avg_serve
        if p_ret2_base is None:
            p_ret2_base = self.tour_avg_return

        # Opponent-adjusted serve winning probability (Klaassen & Magnus formulation):
        # P1 serving against P2: S1 - (R2 - R_tour)
        p_s1_adj = float(p_serve1_base) - (float(p_ret2_base) - self.tour_avg_return)
        p_s2_adj = float(p_serve2_base) - (float(p_ret1_base) - self.tour_avg_return)

        p_s1_adj = np.clip(p_s1_adj, 0.35, 0.85)
        p_s2_adj = np.clip(p_s2_adj, 0.35, 0.85)

        # Apply surface speed factor
        p_serve1 = float(expit(logit(p_s1_adj) + surface_delta))
        p_serve2 = float(expit(logit(p_s2_adj) + surface_delta))

        # Hold probabilities
        p_hold1 = self.p_game_hold(p_serve1)
        p_hold2 = self.p_game_hold(p_serve2)

        set_pmf = self._simulate_set_distribution(p_hold1, p_hold2, p_serve1, p_serve2)

        # P(P1 wins set)
        p_set1 = sum(prob for (g1, g2), prob in set_pmf.items() if g1 > g2)
        p_set2 = 1.0 - p_set1

        sets_needed = 3 if format_type == "best_of_5" else 2
        max_games = 75
        grid = np.zeros((max_games + 1, max_games + 1), dtype=float)

        # Convolve sets based on match tree (exact Markov chain on sets):
        # In tennis, the match winner is decided exclusively by sets won, NOT games won.
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

        # Explicit set-based match win probabilities
        p_match_p1 = sum(prob for (s1, s2, prob) in scenarios if s1 > s2)
        p_match_p2 = sum(prob for (s1, s2, prob) in scenarios if s2 > s1)

        # Condition set distributions into sets won by P1 and sets won by P2
        set_p1_win = {k: v for k, v in set_pmf.items() if k[0] > k[1]}
        set_p2_win = {k: v for k, v in set_pmf.items() if k[1] > k[0]}
        tot_w1 = sum(set_p1_win.values())
        tot_w2 = sum(set_p2_win.values())
        set_p1_win = {k: v / tot_w1 for k, v in set_p1_win.items()}
        set_p2_win = {k: v / tot_w2 for k, v in set_p2_win.items()}

        for (s1_won, s2_won, scen_prob) in scenarios:
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

        # Normalize games grid
        grid /= np.sum(grid)

        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_games + 1),
            away_support=np.arange(max_games + 1),
            p_match_home_win=p_match_p1,
            p_match_away_win=p_match_p2,
            p_match_draw=0.0
        )
