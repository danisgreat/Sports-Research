"""NRL predictive engine modeling sets, tries, conversions, and discrete key numbers."""

from typing import Any, Dict
import numpy as np
from scipy.stats import binom, poisson
from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution


class NRLEngine(BaseSportEngine):
    """Predictive engine for Rugby League matches (NRL, Super League)."""

    def __init__(self):
        super().__init__("nrl")
        self.is_fitted = False
        self.league_avg_tries: float = 3.6
        self.home_try_advantage: float = 0.5
        self.league_kicker_acc: float = 0.78
        self.team_attack_tries: Dict[str, float] = {}
        self.team_defense_tries: Dict[str, float] = {}
        self.team_kicker_accuracy: Dict[str, float] = {}

    def fit(self, train_data: Any) -> "NRLEngine":
        """Fit scoring rate baselines from H0 nrlR data."""
        if isinstance(train_data, list):
            tries_for: Dict[str, float] = {}
            tries_against: Dict[str, float] = {}
            conv_for: Dict[str, float] = {}
            games_played: Dict[str, int] = {}
            h_tries_list = []
            a_tries_list = []

            for m in train_data:
                if not isinstance(m, dict):
                    continue
                h = m.get("home_team")
                a = m.get("away_team")
                h_t = float(m.get("home_tries") or m.get("home_score", 20) // 5)
                a_t = float(m.get("away_tries") or m.get("away_score", 18) // 5)
                h_c = float(m.get("home_conversions") or (h_t * 0.78))
                a_c = float(m.get("away_conversions") or (a_t * 0.78))

                h_tries_list.append(h_t)
                a_tries_list.append(a_t)

                if h:
                    tries_for[h] = tries_for.get(h, 0.0) + h_t
                    tries_against[h] = tries_against.get(h, 0.0) + a_t
                    conv_for[h] = conv_for.get(h, 0.0) + h_c
                    games_played[h] = games_played.get(h, 0) + 1
                if a:
                    tries_for[a] = tries_for.get(a, 0.0) + a_t
                    tries_against[a] = tries_against.get(a, 0.0) + h_t
                    conv_for[a] = conv_for.get(a, 0.0) + a_c
                    games_played[a] = games_played.get(a, 0) + 1

            if h_tries_list and a_tries_list:
                all_t = h_tries_list + a_tries_list
                self.league_avg_tries = float(np.mean(all_t))
                self.home_try_advantage = float(np.mean(h_tries_list) - np.mean(a_tries_list))
                total_c = sum(conv_for.values()) / 2.0
                total_t = sum(tries_for.values()) / 2.0
                if total_t > 0:
                    self.league_kicker_acc = total_c / total_t

            for t, gp in games_played.items():
                if gp >= 3 and self.league_avg_tries > 0:
                    mean_for = tries_for[t] / gp
                    mean_against = tries_against[t] / gp
                    self.team_attack_tries[t] = float(0.8 * (mean_for / self.league_avg_tries) + 0.2)
                    self.team_defense_tries[t] = float(0.8 * (mean_against / self.league_avg_tries) + 0.2)
                    if tries_for[t] > 0:
                        raw_acc = conv_for[t] / tries_for[t]
                        self.team_kicker_accuracy[t] = float(0.7 * raw_acc + 0.3 * self.league_kicker_acc)

        self.is_fitted = True
        return self

    def _team_score_pmf(
        self,
        exp_tries: float,
        conversion_rate: float = 0.78,
        exp_penalty_goals: float = 0.8,
        max_score: int = 70
    ) -> np.ndarray:
        """Derive NRL discrete points PMF preserving key number structure."""
        pmf = np.zeros(max_score + 1, dtype=float)
        
        # Try distribution via Poisson
        try_support = np.arange(0, 12)
        p_tries = poisson.pmf(try_support, exp_tries)
        
        # Penalty goals distribution via Poisson
        pg_support = np.arange(0, 5)
        p_pgs = poisson.pmf(pg_support, exp_penalty_goals)

        for t_idx, t in enumerate(try_support):
            w_t = p_tries[t_idx]
            # Conversions ~ Binomial(t, conversion_rate)
            conv_counts = np.arange(t + 1)
            p_convs = binom.pmf(conv_counts, t, conversion_rate)

            for c_idx, c in enumerate(conv_counts):
                w_c = w_t * p_convs[c_idx]
                try_pts = 4 * t + 2 * c

                for pg_idx, pg in enumerate(pg_support):
                    w_total = w_c * p_pgs[pg_idx]
                    total_pts = try_pts + 2 * pg

                    if total_pts <= max_score:
                        pmf[total_pts] += w_total

        total = np.sum(pmf)
        if total > 0:
            pmf /= total
        return pmf

    def predict_distribution(self, match_context: Dict[str, Any]) -> ScoreDistribution:
        """Produce joint score distribution for an NRL match."""
        h_team = match_context.get("home_team")
        a_team = match_context.get("away_team")

        h_att = self.team_attack_tries.get(h_team, 1.0)
        a_def = self.team_defense_tries.get(a_team, 1.0)
        a_att = self.team_attack_tries.get(a_team, 1.0)
        h_def = self.team_defense_tries.get(h_team, 1.0)

        if "home_expected_tries" in match_context:
            h_tries = float(match_context["home_expected_tries"])
        else:
            h_tries = self.league_avg_tries * h_att * a_def + (self.home_try_advantage / 2.0)

        if "away_expected_tries" in match_context:
            a_tries = float(match_context["away_expected_tries"])
        else:
            a_tries = self.league_avg_tries * a_att * h_def - (self.home_try_advantage / 2.0)

        h_kicker_acc = float(match_context.get("home_goal_kicker_accuracy") or self.team_kicker_accuracy.get(h_team, self.league_kicker_acc))
        a_kicker_acc = float(match_context.get("away_goal_kicker_accuracy") or self.team_kicker_accuracy.get(a_team, self.league_kicker_acc))

        max_score = 70
        p_home = self._team_score_pmf(h_tries, h_kicker_acc, max_score=max_score)
        p_away = self._team_score_pmf(a_tries, a_kicker_acc, max_score=max_score)

        grid = np.outer(p_home, p_away)
        return ScoreDistribution(
            grid=grid,
            home_support=np.arange(max_score + 1),
            away_support=np.arange(max_score + 1)
        )

