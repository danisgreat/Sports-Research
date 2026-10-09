"""Rating models: margin-aware Elo with season carry-over, Glicko uncertainty, surface-specific tennis Elo, and a draw-aware
Bradley-Terry model (ML-07, ML-02).

Elo stays a simple baseline: the aim is a rating-only reference that every fitted engine must beat, and a prior for engines
that have no player-level serve statistics.
"""

import math
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
from scipy.optimize import minimize

from .errors import InsufficientData, UnknownTeam, require_converged


def margin_multiplier(margin: float, winner_elo_diff: float) -> float:
    """Margin-of-victory multiplier for the Elo step: ln(|m| + 1) damped by the winner's rating edge.

    The damping (2.2 / (0.001 * edge + 2.2)) stops strong favourites from farming rating off routine blowouts. A draw
    (margin 0) returns 1.0 so drawn games use the plain K.
    """
    margin = abs(float(margin))
    if margin == 0.0:
        return 1.0
    return math.log(margin + 1.0) * 2.2 / (0.001 * max(float(winner_elo_diff), -2000.0) + 2.2)


class EloRatingEngine:
    """Elo with home advantage, an optional margin-of-victory multiplier, and season carry-over regression.

    `update(..., margin=m)` scales the step by `margin_multiplier`; omit it for the classic update. `regress_to_mean`
    pulls every rating toward the mean at a season boundary (`carry` is the fraction retained).
    """

    def __init__(self, base_rating: float = 1500.0, k_factor: float = 32.0, home_advantage: float = 65.0):
        if k_factor <= 0:
            raise ValueError("k_factor must be positive")
        self.base_rating = base_rating
        self.k_factor = k_factor
        self.home_advantage = home_advantage
        self.ratings: Dict[str, float] = {}

    def knows(self, entity: str) -> bool:
        return entity in self.ratings

    def get_rating(self, entity: str) -> float:
        """A new entity starts at the base rating by definition of Elo; use `knows` to tell it apart from a played one."""
        return self.ratings.get(entity, self.base_rating)

    def predict_prob(self, entity_a: str, entity_b: str, is_neutral: bool = False) -> float:
        """Win probability for entity_a against entity_b (a is the home side unless neutral)."""
        r_a = self.get_rating(entity_a) + (0.0 if is_neutral else self.home_advantage)
        r_b = self.get_rating(entity_b)
        return 1.0 / (1.0 + 10.0 ** ((r_b - r_a) / 400.0))

    def update(self, entity_a: str, entity_b: str, score_a: float, is_neutral: bool = False,
               margin: Optional[float] = None) -> Tuple[float, float]:
        """Update ratings post-match. score_a in {1.0 (win), 0.5 (draw), 0.0 (loss)}; `margin` is |score difference|."""
        if not 0.0 <= score_a <= 1.0:
            raise ValueError("score_a must lie in [0, 1]")
        p_a = self.predict_prob(entity_a, entity_b, is_neutral=is_neutral)
        multiplier = 1.0
        if margin is not None and score_a != 0.5:
            edge = (self.get_rating(entity_a) + (0.0 if is_neutral else self.home_advantage) - self.get_rating(entity_b))
            multiplier = margin_multiplier(margin, edge if score_a > 0.5 else -edge)
        step = self.k_factor * multiplier * (score_a - p_a)
        r_a, r_b = self.get_rating(entity_a), self.get_rating(entity_b)
        self.ratings[entity_a] = r_a + step
        self.ratings[entity_b] = r_b - step
        return self.ratings[entity_a], self.ratings[entity_b]

    def regress_to_mean(self, carry: float = 0.75, mean: Optional[float] = None) -> None:
        """Season boundary: rating <- mean + carry * (rating - mean); the mean defaults to the base rating."""
        if not 0.0 <= carry <= 1.0:
            raise ValueError("carry must lie in [0, 1]")
        centre = self.base_rating if mean is None else float(mean)
        self.ratings = {k: centre + carry * (v - centre) for k, v in self.ratings.items()}


class GlickoRating:
    """Glicko (Glickman 1999): a rating and a rating deviation (RD) per entity.

    `rate_period` updates every entity that played in a rating period from the ratings at its start (simultaneous
    update). Entities inactive for t periods have their RD inflated by `c * sqrt(t)` up to `max_rd`.
    """

    Q = math.log(10.0) / 400.0

    def __init__(self, base_rating: float = 1500.0, base_rd: float = 350.0, c: float = 34.6, max_rd: float = 350.0):
        self.base_rating, self.base_rd, self.c, self.max_rd = base_rating, base_rd, c, max_rd
        self.state: Dict[str, Tuple[float, float]] = {}          # entity -> (rating, rd)
        self.last_period: Dict[str, int] = {}
        self.period = 0

    @staticmethod
    def _g(rd: float) -> float:
        q = GlickoRating.Q
        return 1.0 / math.sqrt(1.0 + 3.0 * q * q * rd * rd / (math.pi ** 2))

    def knows(self, entity: str) -> bool:
        return entity in self.state

    def rating(self, entity: str) -> Tuple[float, float]:
        """(rating, rd) now, with the RD inflated for periods without games; a new entity is (base, base_rd)."""
        r, rd = self.state.get(entity, (self.base_rating, self.base_rd))
        idle = self.period - self.last_period.get(entity, self.period)
        if idle > 0:
            rd = min(math.sqrt(rd * rd + self.c * self.c * idle), self.max_rd)
        return r, rd

    def expected(self, a: str, b: str) -> float:
        """P(a beats b) accounting for both deviations."""
        (ra, rda), (rb, rdb) = self.rating(a), self.rating(b)
        g = self._g(math.sqrt(rda * rda + rdb * rdb))
        return 1.0 / (1.0 + 10.0 ** (-g * (ra - rb) / 400.0))

    def rate_period(self, games: Iterable[Tuple[str, str, float]]) -> None:
        """games: (entity_a, entity_b, score_a in {0, 0.5, 1}) played in one rating period."""
        by_entity: Dict[str, List[Tuple[str, float]]] = {}
        for a, b, score in games:
            if not 0.0 <= score <= 1.0:
                raise ValueError("score must lie in [0, 1]")
            by_entity.setdefault(a, []).append((b, score))
            by_entity.setdefault(b, []).append((a, 1.0 - score))
        start = {e: self.rating(e) for e in set(by_entity) | {o for g in by_entity.values() for o, _ in g}}
        q = self.Q
        updates: Dict[str, Tuple[float, float]] = {}
        for entity, results in by_entity.items():
            r, rd = start[entity]
            d2_inv, delta = 0.0, 0.0
            for opp, score in results:
                r_o, rd_o = start[opp]
                g = self._g(rd_o)
                e = 1.0 / (1.0 + 10.0 ** (-g * (r - r_o) / 400.0))
                d2_inv += q * q * g * g * e * (1.0 - e)
                delta += g * (score - e)
            denom = 1.0 / (rd * rd) + d2_inv
            updates[entity] = (r + q / denom * delta, math.sqrt(1.0 / denom))
        self.period += 1
        for entity, value in updates.items():
            self.state[entity] = value
            self.last_period[entity] = self.period


class SurfaceElo:
    """Tennis Elo: an overall rating plus one per surface, blended for prediction (RULES_TENNIS ratings prior).

    Both ratings update on every match with K = 250 / (n + 5)^0.4 for a player with n matches (new players move fast, veterans
    slowly). `surface_weight` is the share given to the surface rating; `fit_surface_weight` chooses it by log loss on the
    training matches in order.
    """

    def __init__(self, base_rating: float = 1500.0, surface_weight: float = 0.5, k_scale: float = 250.0, k_offset: float = 5.0,
                 k_shape: float = 0.4):
        if not 0.0 <= surface_weight <= 1.0:
            raise ValueError("surface_weight must lie in [0, 1]")
        self.base_rating, self.surface_weight = base_rating, surface_weight
        self.k_scale, self.k_offset, self.k_shape = k_scale, k_offset, k_shape
        self.overall: Dict[str, float] = {}
        self.surface: Dict[Tuple[str, str], float] = {}
        self.matches: Dict[str, int] = {}

    def knows(self, player: str) -> bool:
        return player in self.overall

    def rating(self, player: str, surface: str, weight: Optional[float] = None) -> float:
        w = self.surface_weight if weight is None else weight
        o = self.overall.get(player, self.base_rating)
        s = self.surface.get((player, surface), o)             # a player's first match on a surface starts from his overall rating
        return (1.0 - w) * o + w * s

    def win_prob(self, a: str, b: str, surface: str, weight: Optional[float] = None) -> float:
        return 1.0 / (1.0 + 10.0 ** ((self.rating(b, surface, weight) - self.rating(a, surface, weight)) / 400.0))

    def _k(self, player: str) -> float:
        return self.k_scale / (self.matches.get(player, 0) + self.k_offset) ** self.k_shape

    def update(self, winner: str, loser: str, surface: str) -> None:
        p_w_overall = 1.0 / (1.0 + 10.0 ** ((self.overall.get(loser, self.base_rating) - self.overall.get(winner, self.base_rating)) / 400.0))
        sw, sl = (self.surface.get((winner, surface), self.overall.get(winner, self.base_rating)),
                  self.surface.get((loser, surface), self.overall.get(loser, self.base_rating)))
        p_w_surface = 1.0 / (1.0 + 10.0 ** ((sl - sw) / 400.0))
        kw, kl = self._k(winner), self._k(loser)
        ow, ol = self.overall.get(winner, self.base_rating), self.overall.get(loser, self.base_rating)
        self.overall[winner], self.overall[loser] = ow + kw * (1.0 - p_w_overall), ol - kl * (1.0 - p_w_overall)
        self.surface[(winner, surface)], self.surface[(loser, surface)] = sw + kw * (1.0 - p_w_surface), sl - kl * (1.0 - p_w_surface)
        self.matches[winner] = self.matches.get(winner, 0) + 1
        self.matches[loser] = self.matches.get(loser, 0) + 1

    def fit(self, matches: Sequence[Tuple[str, str, str]]) -> "SurfaceElo":
        """matches: chronological (winner, loser, surface)."""
        if len(matches) < 10:
            raise InsufficientData("need at least 10 chronological matches")
        for winner, loser, surface in matches:
            self.update(winner, loser, surface)
        return self

    @classmethod
    def fit_surface_weight(cls, matches: Sequence[Tuple[str, str, str]], grid: Sequence[float] = (0.0, 0.25, 0.5, 0.75, 1.0),
                           **kwargs) -> Tuple["SurfaceElo", Dict[float, float]]:
        """Walk-forward log loss for each blend weight (prediction before the update); returns the fitted model and the table."""
        if len(matches) < 50:
            raise InsufficientData("need at least 50 chronological matches to choose a surface weight")
        losses: Dict[float, float] = {}
        for w in grid:
            model = cls(surface_weight=w, **kwargs)
            total = 0.0
            for winner, loser, surface in matches:
                total -= math.log(min(max(model.win_prob(winner, loser, surface), 1e-6), 1 - 1e-6))
                model.update(winner, loser, surface)
            losses[w] = total / len(matches)
        best = min(losses, key=lambda w: losses[w])
        return cls(surface_weight=best, **kwargs).fit(matches), losses


class BradleyTerryDrawEngine:
    """Regularised Bradley-Terry model with a Rao-Davidson draw parameter and an optional home advantage.

    P(A wins) = pi_A / (pi_A + pi_B + nu * sqrt(pi_A * pi_B)); P(draw) = nu * sqrt(pi_A * pi_B) / (same denominator), with
    pi_i = exp(gamma_i) and the home side's gamma raised by `home_log_advantage` when `fit_home_advantage` is on.
    Fitted by vectorised maximum likelihood with its analytic gradient; failure raises `FitFailed` and an unknown team is
    refused unless `unknown_team="league_average"` (strength 0 = the mean).
    """

    def __init__(self, l2_reg: float = 0.1, fit_home_advantage: bool = False, unknown_team: str = "refuse"):
        if unknown_team not in ("refuse", "league_average"):
            raise ValueError("unknown_team must be 'refuse' or 'league_average'")
        self.l2_reg = l2_reg
        self.fit_home_advantage = fit_home_advantage
        self.unknown_team = unknown_team
        self.teams: List[str] = []
        self.team_indices: Dict[str, int] = {}
        self.log_strengths: np.ndarray = np.array([])
        self.log_nu: float = 0.0
        self.home_log_advantage: float = 0.0

    _RESULTS = {"home": 0, "1": 0, "draw": 1, "x": 1, "tie": 1, "away": 2, "2": 2}

    @staticmethod
    def _nll(params: np.ndarray, hi: np.ndarray, ai: np.ndarray, outcome: np.ndarray, n_teams: int, l2: float, use_home: bool):
        g = params[:n_teams]
        log_nu = params[n_teams]
        h = params[n_teams + 1] if use_home else 0.0
        gh, ga = g[hi] + h, g[ai]
        log_den = np.logaddexp(np.logaddexp(gh, ga), log_nu + 0.5 * (gh + ga))
        log_p = np.where(outcome == 0, gh, np.where(outcome == 2, ga, log_nu + 0.5 * (gh + ga))) - log_den
        nll = -np.sum(log_p) + 0.5 * l2 * (np.sum(g ** 2) + log_nu ** 2)
        # gradient: d(-log p) = d(log den) - d(numerator log)
        w_h, w_a = np.exp(gh - log_den), np.exp(ga - log_den)
        w_d = np.exp(log_nu + 0.5 * (gh + ga) - log_den)
        d_gh = w_h + 0.5 * w_d - np.where(outcome == 0, 1.0, np.where(outcome == 1, 0.5, 0.0))
        d_ga = w_a + 0.5 * w_d - np.where(outcome == 2, 1.0, np.where(outcome == 1, 0.5, 0.0))
        d_nu = w_d - (outcome == 1)
        grad = np.zeros_like(params)
        np.add.at(grad, hi, d_gh)
        np.add.at(grad, ai, d_ga)
        grad[:n_teams] += l2 * g
        grad[n_teams] = np.sum(d_nu) + l2 * log_nu
        if use_home:
            grad[n_teams + 1] = np.sum(d_gh)
        return nll, grad

    def fit(self, matches: List[Dict[str, Any]]) -> "BradleyTerryDrawEngine":
        """matches: [{"home": team, "away": team, "result": "home" | "draw" | "away"}]."""
        if not matches:
            raise InsufficientData("Bradley-Terry needs at least one match")
        teams = sorted({str(m["home"]) for m in matches} | {str(m["away"]) for m in matches})
        index = {t: i for i, t in enumerate(teams)}
        hi = np.array([index[str(m["home"])] for m in matches])
        ai = np.array([index[str(m["away"])] for m in matches])
        try:
            outcome = np.array([self._RESULTS[str(m["result"]).lower()] for m in matches])
        except KeyError as exc:
            raise ValueError(f"unrecognised result {exc.args[0]!r}; use home/draw/away") from None
        n_teams = len(teams)
        params0 = np.zeros(n_teams + 1 + (1 if self.fit_home_advantage else 0))
        result = minimize(self._nll, params0, args=(hi, ai, outcome, n_teams, self.l2_reg, self.fit_home_advantage), jac=True,
                          method="L-BFGS-B", options={"maxiter": 1000})
        require_converged(result, "BradleyTerryDrawEngine", grad_tol=1e-4 * max(1.0, float(len(matches))))
        self.teams, self.team_indices = teams, index
        self.log_strengths = result.x[:n_teams].copy()
        self.log_nu = float(result.x[n_teams])
        self.home_log_advantage = float(result.x[n_teams + 1]) if self.fit_home_advantage else 0.0
        return self

    def _strength(self, team: str) -> float:
        if team in self.team_indices:
            return float(self.log_strengths[self.team_indices[team]])
        if self.unknown_team == "league_average":
            return 0.0
        raise UnknownTeam(f"Bradley-Terry: no fitted strength for {team!r}")

    def predict_probs(self, team_home: str, team_away: str) -> Tuple[float, float, float]:
        """(p_home, p_draw, p_away)."""
        if len(self.log_strengths) == 0:
            raise UnknownTeam("Bradley-Terry: the model has not been fitted")
        gh, ga = self._strength(team_home) + self.home_log_advantage, self._strength(team_away)
        pi_h, pi_a = math.exp(gh), math.exp(ga)
        draw_mass = math.exp(self.log_nu) * math.sqrt(pi_h * pi_a)
        denom = pi_h + pi_a + draw_mass
        return (pi_h / denom, draw_mass / denom, pi_a / denom)
