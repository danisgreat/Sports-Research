"""Tennis engine: exact point-to-match tree with serve order, plus a match-level form shock (DST-04).

An i.i.d. point model over-states deciding sets (the retrospective reproduced P(three sets) = 0.50 for near-even players
against a 0.358 population rate): in real matches one player is simply having a better or worse day. Here each match draws a
relative form shock delta ~ N(0, sigma^2) that raises one player's serve-point probability and lowers the other's, and the
exact match distribution is integrated over delta by Gauss-Hermite quadrature.

Games, sets, tiebreaks and the serve order are exact: the set's first server alternates with the parity of games played in
the previous set, and a tiebreak is started by the player who would serve next.
"""

from functools import lru_cache
from typing import Any, Dict, Optional, Sequence, Tuple

import numpy as np
from scipy.optimize import brentq
from scipy.signal import convolve2d
from scipy.special import expit, logit

from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution
from ...common.errors import InsufficientData, MissingInputs, MissingScore, UnknownTeam
from ...common.ratings import SurfaceElo

FORM_NODES, FORM_WEIGHTS = np.polynomial.hermite_e.hermegauss(9)
FORM_WEIGHTS = FORM_WEIGHTS / FORM_WEIGHTS.sum()
SERVE_BOUNDS = (0.30, 0.90)


def p_game_hold(p: float) -> float:
    """Exact probability that a server holds a game (deuce and advantage included)."""
    p = float(np.clip(p, 1e-4, 1.0 - 1e-4))
    q = 1.0 - p
    num = p ** 4 * (15.0 - 34.0 * p + 28.0 * (p ** 2) - 8.0 * (p ** 3))
    return float(np.clip(num / (1.0 - 2.0 * p * q), 0.0, 1.0))


def p_tiebreak_win(p_s1: float, p_s2: float) -> float:
    """Exact 7-point tiebreak win probability for player 1 when player 1 serves the first point.

    Serving: point 0 by player 1, points 1-2 by player 2, points 3-4 by player 1, and so on. From 6-6 the rest is
    absorbed in closed form over two-point cycles.
    """
    p_s1 = float(np.clip(p_s1, 0.05, 0.95))
    p_s2 = float(np.clip(p_s2, 0.05, 0.95))
    dp: Dict[Tuple[int, int], float] = {(0, 0): 1.0}
    p_win = 0.0
    for total_pts in range(12):
        server = 1 if (total_pts == 0 or ((total_pts - 1) // 2) % 2 == 1) else 2
        p_pt1 = p_s1 if server == 1 else (1.0 - p_s2)
        next_dp: Dict[Tuple[int, int], float] = {}
        for (i, j), prob in dp.items():
            if prob <= 0:
                continue
            if i + 1 == 7 and j <= 5:
                p_win += prob * p_pt1
            elif i + 1 < 7 or (i + 1 == 6 and j == 6):
                next_dp[(i + 1, j)] = next_dp.get((i + 1, j), 0.0) + prob * p_pt1
            if j + 1 == 7 and i <= 5:
                pass
            elif j + 1 < 7 or (i == 6 and j + 1 == 6):
                next_dp[(i, j + 1)] = next_dp.get((i, j + 1), 0.0) + prob * (1.0 - p_pt1)
        dp = next_dp
    p_6_6 = dp.get((6, 6), 0.0)
    if p_6_6 > 0:
        a, b = 1.0 - p_s2, p_s1
        p_win += p_6_6 * (a * b) / max(a * b + (1.0 - a) * (1.0 - b), 1e-12)
    return float(np.clip(p_win, 0.0, 1.0))


def set_outcomes(p_s1: float, p_s2: float, p1_serves_first: bool) -> Dict[Tuple[int, int], float]:
    """P(final games (g1, g2)) for one set; the first server alternates by game, a 6-6 tiebreak starts with the first server."""
    hold1, hold2 = p_game_hold(p_s1), p_game_hold(p_s2)
    tb_p1 = p_tiebreak_win(p_s1, p_s2) if p1_serves_first else 1.0 - p_tiebreak_win(p_s2, p_s1)

    @lru_cache(maxsize=None)
    def games(g1: int, g2: int) -> Tuple[Tuple[Tuple[int, int], float], ...]:
        if (g1 >= 6 and g1 - g2 >= 2) or g1 == 7 or (g2 >= 6 and g2 - g1 >= 2) or g2 == 7:
            return (((g1, g2), 1.0),)
        if g1 == 6 and g2 == 6:
            return (((7, 6), tb_p1), ((6, 7), 1.0 - tb_p1))
        p1_serving = ((g1 + g2) % 2 == 0) == p1_serves_first
        p_win = hold1 if p1_serving else 1.0 - hold2
        out: Dict[Tuple[int, int], float] = {}
        for key, v in games(g1 + 1, g2):
            out[key] = out.get(key, 0.0) + p_win * v
        for key, v in games(g1, g2 + 1):
            out[key] = out.get(key, 0.0) + (1.0 - p_win) * v
        return tuple(out.items())

    return dict(games(0, 0))


def _kernels(p_s1: float, p_s2: float, p1_first: bool):
    """Set-outcome arrays split by winner and by parity of games (which fixes the next set's first server)."""
    arrays = {(w, par): np.zeros((8, 8)) for w in (1, 2) for par in (0, 1)}
    for (g1, g2), p in set_outcomes(p_s1, p_s2, p1_first).items():
        arrays[(1 if g1 > g2 else 2, (g1 + g2) % 2)][g1, g2] += p
    return arrays


def _end_state_probabilities(p_s1: float, p_s2: float, sets_to_win: int) -> Dict[Tuple[int, int], float]:
    """P(final sets score (sets1, sets2)) from set-win and parity masses only (no games grid, so it is cheap)."""
    masses = {first: {key: float(arr.sum()) for key, arr in _kernels(p_s1, p_s2, first).items()} for first in (True, False)}
    states: Dict[Tuple[int, int, bool], float] = {(0, 0, True): 0.5, (0, 0, False): 0.5}
    for total_sets in range(2 * sets_to_win - 1):
        for (s1, s2, first), prob in list(states.items()):
            if s1 + s2 != total_sets or s1 == sets_to_win or s2 == sets_to_win:
                continue
            for winner in (1, 2):
                for parity in (0, 1):
                    key = (s1 + (winner == 1), s2 + (winner == 2), first if parity == 0 else not first)
                    states[key] = states.get(key, 0.0) + prob * masses[first][(winner, parity)]
    out: Dict[Tuple[int, int], float] = {}
    for (s1, s2, _), prob in states.items():
        if s1 == sets_to_win or s2 == sets_to_win:
            out[(s1, s2)] = out.get((s1, s2), 0.0) + prob
    return out


def _decider_probability(p_s1: float, p_s2: float, sets_to_win: int) -> float:
    """P(the match reaches its deciding set)."""
    return float(sum(p for (s1, s2), p in _end_state_probabilities(p_s1, p_s2, sets_to_win).items() if s1 + s2 == 2 * sets_to_win - 1))


def match_win_probability(p_s1: float, p_s2: float, sets_to_win: int, form_sigma: float = 0.0) -> float:
    """P(player 1 wins the match), integrated over the form shock when form_sigma > 0."""
    def one(a: float, b: float) -> float:
        return float(sum(p for (s1, _), p in _end_state_probabilities(a, b, sets_to_win).items() if s1 == sets_to_win))
    if form_sigma == 0:
        return one(p_s1, p_s2)
    return float(sum(w * one(float(np.clip(p_s1 + form_sigma * z, *SERVE_BOUNDS)), float(np.clip(p_s2 - form_sigma * z, *SERVE_BOUNDS)))
                     for z, w in zip(FORM_NODES, FORM_WEIGHTS)))


def serve_probabilities_from_win_prob(p_win: float, tour_avg_serve: float, sets_to_win: int, form_sigma: float) -> Tuple[float, float]:
    """Serve-point probabilities (base + d, base - d) whose match-win probability for player 1 equals `p_win` (a rating prior).

    Only the strength difference is pinned; both players keep the tour-average serve level, so a prior from ratings says
    nothing about big-serving matchups (that needs player serve statistics).
    """
    if not 0.01 < p_win < 0.99:
        raise ValueError("p_win must lie in (0.01, 0.99)")
    limit = min(tour_avg_serve - SERVE_BOUNDS[0], SERVE_BOUNDS[1] - tour_avg_serve) - 0.02
    f = lambda d: match_win_probability(tour_avg_serve + d, tour_avg_serve - d, sets_to_win, form_sigma) - p_win
    if f(-limit) > 0 or f(limit) < 0:
        raise ValueError(f"p_win={p_win:.3f} is outside what serve differences within +-{limit:.2f} can reach")
    d = brentq(f, -limit, limit, xtol=1e-7)
    return float(tour_avg_serve + d), float(tour_avg_serve - d)


def match_distribution(p_s1: float, p_s2: float, sets_to_win: int) -> Tuple[np.ndarray, float, float, float]:
    """Exact (games grid, P(player 1 wins), P(player 2 wins), P(deciding set)) for constant serve-point probabilities.

    The first server of set one is a coin toss; each later set is started by the player who received in the last game
    of the previous set.
    """
    grid, _, p1, p2, dec = _match_core(p_s1, p_s2, sets_to_win)
    return grid, p1, p2, dec


def _match_core(p_s1: float, p_s2: float, sets_to_win: int) -> Tuple[np.ndarray, np.ndarray, float, float, float]:
    """(games grid, the part of that grid where player 1 won, P(p1 wins), P(p2 wins), P(deciding set))."""
    kernels = {True: _kernels(p_s1, p_s2, True), False: _kernels(p_s1, p_s2, False)}
    size = (2 * sets_to_win - 1) * 13 + 1                       # a set has at most 13 games for a player
    grid = np.zeros((size, size))
    grid_p1 = np.zeros((size, size))
    p1_win = p2_win = decider = 0.0
    # state (sets1, sets2, p1_serves_first_next_set) -> games array
    start = np.zeros((size, size))
    start[0, 0] = 0.5
    states: Dict[Tuple[int, int, bool], np.ndarray] = {(0, 0, True): start.copy(), (0, 0, False): start.copy()}
    for total_sets in range(2 * sets_to_win - 1):
        for (s1, s2, first), games in list(states.items()):
            if s1 + s2 != total_sets or s1 == sets_to_win or s2 == sets_to_win:
                continue
            for winner in (1, 2):
                for parity in (0, 1):
                    moved = convolve2d(games, kernels[first][(winner, parity)], mode="full")[:size, :size]
                    if not moved.any():
                        continue
                    key = (s1 + (winner == 1), s2 + (winner == 2), first if parity == 0 else not first)
                    states[key] = states.get(key, 0.0) + moved
    for (s1, s2, _), games in states.items():
        if s1 == sets_to_win:
            p1_win += games.sum()
            grid += games
            grid_p1 += games
        elif s2 == sets_to_win:
            p2_win += games.sum()
            grid += games
        else:
            continue
        if s1 + s2 == 2 * sets_to_win - 1:
            decider += games.sum()
    total = grid.sum()
    return grid / total, grid_p1 / total, p1_win / total, p2_win / total, decider / total


def mix_over_form_joint(p_s1: float, p_s2: float, sets_to_win: int, form_sigma: float) -> Tuple[np.ndarray, np.ndarray, float, float, float]:
    """`mix_over_form` that also returns the part of the games grid where player 1 won (for winner-aware pricing)."""
    if form_sigma < 0:
        raise ValueError("form_sigma must be non-negative")
    if form_sigma == 0:
        return _match_core(p_s1, p_s2, sets_to_win)
    size = (2 * sets_to_win - 1) * 13 + 1
    grid = np.zeros((size, size))
    grid_p1 = np.zeros((size, size))
    p1 = p2 = dec = 0.0
    for z, w in zip(FORM_NODES, FORM_WEIGHTS):
        delta = form_sigma * z
        g, g1, a, b, d = _match_core(float(np.clip(p_s1 + delta, *SERVE_BOUNDS)), float(np.clip(p_s2 - delta, *SERVE_BOUNDS)), sets_to_win)
        grid += w * g
        grid_p1 += w * g1
        p1, p2, dec = p1 + w * a, p2 + w * b, dec + w * d
    total = grid.sum()
    return grid / total, grid_p1 / total, p1, p2, dec


def mix_over_form(p_s1: float, p_s2: float, sets_to_win: int, form_sigma: float) -> Tuple[np.ndarray, float, float, float]:
    """The match distribution integrated over the relative form shock delta ~ N(0, sigma^2): +delta for player 1's serve, -delta for player 2's."""
    grid, _, p1, p2, dec = mix_over_form_joint(p_s1, p_s2, sets_to_win, form_sigma)
    return grid, p1, p2, dec


def calibrate_form_sigma(matchups: Sequence[Tuple[float, float]], target_deciding_rate: float, sets_to_win: int = 2,
                         upper: float = 0.12) -> float:
    """Form-shock size at which the average P(deciding set) over `matchups` equals an observed population rate.

    `matchups` must represent the population (the spread of serve strengths between real opponents), because part of the
    gap to the i.i.d. model is genuine mismatch rather than form. Bisection: the rate falls as sigma grows.
    """
    if not matchups:
        raise InsufficientData("calibrate_form_sigma needs matchups that represent the population")

    def rate(sigma: float) -> float:
        total = 0.0
        for a, b in matchups:
            if sigma == 0:
                total += _decider_probability(a, b, sets_to_win)
                continue
            total += sum(w * _decider_probability(float(np.clip(a + sigma * z, *SERVE_BOUNDS)), float(np.clip(b - sigma * z, *SERVE_BOUNDS)), sets_to_win)
                         for z, w in zip(FORM_NODES, FORM_WEIGHTS))
        return total / len(matchups)

    high_rate, low_rate = rate(upper), rate(0.0)
    if not high_rate <= target_deciding_rate <= low_rate:
        raise ValueError(f"target {target_deciding_rate:.3f} is outside the attainable range [{high_rate:.3f}, {low_rate:.3f}]")
    lo, hi = 0.0, upper
    for _ in range(30):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if rate(mid) > target_deciding_rate else (lo, mid)
    return 0.5 * (lo + hi)


class TennisEngine(BaseSportEngine):
    """Predictive engine for tennis (ATP, WTA, Grand Slams).

    Serve-point probabilities come from the context (match-specific, used as given) or from fitted player serve and return
    rates adjusted for the opponent (Klaassen-Magnus) and for the surface. `form_sigma` is mandatory: pass 0.0 to knowingly
    accept the i.i.d. model, or a value from `calibrate_form_sigma`.
    """

    def __init__(self, unknown_team_policy: str = "refuse", form_sigma: Optional[float] = None,
                 surface_effects: Optional[Dict[str, float]] = None, tour_avg_serve: Optional[float] = None,
                 shrinkage_points: float = 100.0, elo: Optional[SurfaceElo] = None):
        super().__init__("tennis", None, unknown_team_policy)
        self.elo = elo
        self.form_sigma = form_sigma
        self.surface_effects = dict(surface_effects or {"hard": 0.0})      # logit shifts relative to hard courts; explicit, not assumed
        self.tour_avg_serve = tour_avg_serve
        self.shrinkage_points = shrinkage_points
        self.player_stats: Dict[str, Dict[str, float]] = {}

    # Kept as static helpers for callers and tests.
    p_game_hold = staticmethod(p_game_hold)
    p_tiebreak_win = staticmethod(p_tiebreak_win)

    @property
    def tour_avg_return(self) -> Optional[float]:
        return None if self.tour_avg_serve is None else 1.0 - self.tour_avg_serve

    # ------------------------------------------------------------------ fitting
    @staticmethod
    def _serve_record(m: dict, side: str) -> Tuple[str, float, float]:
        """(player, serve points won, serve points played) for one side; an absent field raises, nothing is defaulted."""
        if side == "p1":
            name, won_keys, total_keys = m.get("player1") or m.get("winner"), ("p1_serve_won",), ("p1_serve_total",)
            sack_won, sack_total = ("w_1stWon", "w_2ndWon"), "w_svpt"
        else:
            name, won_keys, total_keys = m.get("player2") or m.get("loser"), ("p2_serve_won",), ("p2_serve_total",)
            sack_won, sack_total = ("l_1stWon", "l_2ndWon"), "l_svpt"
        if not name:
            raise MissingScore(f"training match lacks the {side} player name")
        if m.get(won_keys[0]) is not None and m.get(total_keys[0]) is not None:
            won, total = float(m[won_keys[0]]), float(m[total_keys[0]])
        elif all(m.get(k) is not None for k in (*sack_won, sack_total)):
            won, total = float(m[sack_won[0]]) + float(m[sack_won[1]]), float(m[sack_total])
        else:
            raise MissingScore(f"training match lacks serve-point statistics for {side}")
        if not (0 <= won <= total) or total <= 0:
            raise MissingScore(f"invalid serve statistics for {name}: {won}/{total}")
        return str(name), won, total

    def fit(self, train_data: Any) -> "TennisEngine":
        if not isinstance(train_data, (list, tuple)):
            raise ValueError("train_data must be a list of match dicts; an engine is never 'fitted' on nothing")
        accum: Dict[str, Dict[str, float]] = {}
        for m in train_data:
            (n1, w1, t1), (n2, w2, t2) = self._serve_record(m, "p1"), self._serve_record(m, "p2")
            for name, won, total, opp_won, opp_total in ((n1, w1, t1, w2, t2), (n2, w2, t2, w1, t1)):
                s = accum.setdefault(name, {"sv_won": 0.0, "sv_tot": 0.0, "ret_won": 0.0, "ret_tot": 0.0})
                s["sv_won"] += won
                s["sv_tot"] += total
                s["ret_won"] += opp_total - opp_won
                s["ret_tot"] += opp_total
        total_points = sum(s["sv_tot"] for s in accum.values())
        if total_points < 100:
            raise InsufficientData(f"need at least 100 serve points to fit tour averages, got {total_points:.0f}")
        self.tour_avg_serve = sum(s["sv_won"] for s in accum.values()) / total_points
        tour_return = 1.0 - self.tour_avg_serve
        k = self.shrinkage_points
        self.player_stats = {p: {"serve_win_rate": (s["sv_won"] + k * self.tour_avg_serve) / (s["sv_tot"] + k),
                                 "return_win_rate": (s["ret_won"] + k * tour_return) / (s["ret_tot"] + k)} for p, s in accum.items()}
        self.is_fitted = True
        return self

    # ------------------------------------------------------------------- inputs
    def _elo_probabilities(self, ctx: Dict[str, Any], p_win: float, sets_to_win: int, sigma: float) -> Tuple[float, float]:
        if self.tour_avg_serve is None:
            raise MissingInputs("tennis: a rating prior needs the tour-average serve level (fit the engine or set tour_avg_serve)")
        return serve_probabilities_from_win_prob(p_win, self.tour_avg_serve, sets_to_win, sigma)

    def _serve_probabilities(self, ctx: Dict[str, Any], sets_to_win: int = 2, sigma: float = 0.0) -> Tuple[float, float, str]:
        """Order of evidence: match-specific serve probabilities, an explicit rating win probability, fitted player statistics
        (both players known), the surface Elo prior (both known), then the unknown-player policy."""
        if ctx.get("p_serve1") is not None and ctx.get("p_serve2") is not None:
            return float(ctx["p_serve1"]), float(ctx["p_serve2"]), "match_specific"
        if ctx.get("p_match_elo") is not None:
            return (*self._elo_probabilities(ctx, float(ctx["p_match_elo"]), sets_to_win, sigma), "elo_prior")
        player1, player2 = ctx.get("player1") or ctx.get("home_team"), ctx.get("player2") or ctx.get("away_team")
        if player1 is None or player2 is None:
            raise MissingInputs("tennis: give player1 and player2, or p_serve1 and p_serve2")
        names = (str(player1), str(player2))
        known_stats = self.tour_avg_serve is not None and all(n in self.player_stats for n in names)
        if not known_stats and self.elo is not None and all(self.elo.knows(n) for n in names):
            surface = str(ctx.get("surface", "hard")).lower()
            return (*self._elo_probabilities(ctx, self.elo.win_prob(names[0], names[1], surface), sets_to_win, sigma), "elo_prior")
        if self.tour_avg_serve is None:
            raise MissingInputs("tennis: give p_serve1 and p_serve2, or fit the engine (tour averages come from data)")
        stats = []
        for name in names:
            if name in self.player_stats:
                stats.append(self.player_stats[name])
            elif self.unknown_team_policy == "league_average":
                self._warn(f"unknown player {name!r}: tour-average serve and return used; uncertainty not modelled")
                stats.append({"serve_win_rate": self.tour_avg_serve, "return_win_rate": 1.0 - self.tour_avg_serve})
            else:
                raise UnknownTeam(f"tennis: no fitted serve/return record for {name!r}; pass p_serve1/p_serve2 or set unknown_team_policy")
        surface = str(ctx.get("surface", "hard")).lower()
        if surface not in self.surface_effects:
            raise MissingInputs(f"tennis: no surface effect registered for {surface!r}; pass surface_effects explicitly")
        shift = self.surface_effects[surface]
        tour_return = 1.0 - self.tour_avg_serve
        adj1 = float(np.clip(stats[0]["serve_win_rate"] - (stats[1]["return_win_rate"] - tour_return), *SERVE_BOUNDS))
        adj2 = float(np.clip(stats[1]["serve_win_rate"] - (stats[0]["return_win_rate"] - tour_return), *SERVE_BOUNDS))
        return float(expit(logit(adj1) + shift)), float(expit(logit(adj2) + shift)), "player_stats"

    # --------------------------------------------------------------- prediction
    def predict_distribution(self, match_context: Dict[str, Any], endpoint: str = "completed_match") -> ScoreDistribution:
        """Games grid (player 1, player 2) for a completed match, with set-based winner probabilities."""
        if endpoint != "completed_match":
            raise ValueError("the tennis grid settles on a completed match; retirements void games rows by convention")
        sigma = match_context.get("form_sigma", self.form_sigma)
        if sigma is None:
            raise MissingInputs("tennis: form_sigma is required (0.0 knowingly accepts the i.i.d. model, which over-states deciding sets; "
                                "otherwise use calibrate_form_sigma)")
        fmt = str(match_context.get("format", "best_of_3")).lower()
        if fmt not in ("best_of_3", "best_of_5"):
            raise ValueError("format must be 'best_of_3' or 'best_of_5'")
        sets_to_win = 3 if fmt == "best_of_5" else 2
        p1, p2, basis = self._serve_probabilities(match_context, sets_to_win, float(sigma))
        grid, grid_p1, win1, win2, decider = mix_over_form_joint(p1, p2, sets_to_win, float(sigma))
        with np.errstate(divide="ignore", invalid="ignore"):
            home_win_given_cell = np.where(grid > 0, grid_p1 / grid, 0.5)
        support = np.arange(grid.shape[0])
        return ScoreDistribution(grid, support, support, p_match_home_win=win1, p_match_away_win=win2, p_match_draw=0.0,
                                 endpoint="completed_match",
                                 metadata={"model": "tennis_exact_tree_form_shock", "p_serve1": p1, "p_serve2": p2, "serve_basis": basis,
                                           "form_sigma": float(sigma), "format": fmt, "p_deciding_set": decider,
                                           "home_win_given_cell": home_win_given_cell,
                                           "warnings": self._take_warnings()})
