"""Endpoint layer: regulation grid -> full-game grid (DST-02).

A regulation score grid keeps its tied cells. A contract that settles on the full game
(overtime, shootout, extra innings) must be priced from a grid in which that tied mass has been
resolved by a sport-specific rule; otherwise "full-game" moneylines and spreads are incoherent.

Every function here conserves total probability exactly, removes tied mass wherever the rule
cannot end in a tie, and returns a new `ScoreDistribution` labelled `endpoint="full_game"`.

Parameters are explicit. Defaults that depend on a league (3-on-3 scoring rate, extra-inning run
distribution, shootout share) are fitted from the archive by `research.operations.build_league_profiles`
or supplied by the caller; none is hidden in the engines.
"""

from dataclasses import dataclass
from typing import Optional, Sequence

import numpy as np
from scipy.stats import norm

from .contracts import ScoreDistribution
from .errors import MissingInputs


def _tied_mass(grid: np.ndarray) -> np.ndarray:
    n = min(grid.shape)
    return np.diag(grid)[:n].copy()


def resolve_ties(dist: ScoreDistribution, p_home_given_tie: float, increment: int = 1) -> ScoreDistribution:
    """Resolve every regulation tie with a winner who gains `increment` points.

    Hockey overtime and shootout winners add exactly one goal to the tied score, so a 2-2
    regulation tie becomes 3-2 or 2-3 and full-game totals of those games are odd.
    """
    if not 0.0 <= p_home_given_tie <= 1.0:
        raise ValueError("p_home_given_tie must lie in [0, 1]")
    if increment < 1:
        raise ValueError("increment must be at least 1")
    if not (np.array_equal(dist.home_support, dist.away_support) and np.array_equal(dist.home_support, np.arange(len(dist.home_support)))):
        raise ValueError("tie resolution needs identical 0..N supports for both teams")
    grid = dist.grid
    n_h, n_a = grid.shape
    out = np.zeros((n_h + increment, n_a + increment))
    out[:n_h, :n_a] = grid
    tied = _tied_mass(grid)                               # snapshot: resolved mass is never reprocessed
    for k in range(len(tied)):
        mass = tied[k]
        if mass == 0.0:
            continue
        out[k, k] -= mass
        out[k + increment, k] += mass * p_home_given_tie
        out[k, k + increment] += mass * (1.0 - p_home_given_tie)
    return ScoreDistribution(out, np.arange(out.shape[0]), np.arange(out.shape[1]), endpoint="full_game",
                             metadata={**dist.metadata, "endpoint_rule": f"tie_winner_adds_{increment}"})


# ----------------------------------------------------------------------------- hockey

@dataclass(frozen=True)
class HockeyOvertime:
    """NHL-style tie-break: a sudden-death overtime, then a shootout.

    ot_minutes:         length of the regular-season overtime (None = playoff sudden death until a goal).
    ot_rate_multiplier: 3-on-3 per-minute scoring rate relative to the team's regulation rate.
    shootout_home_share: probability the home side wins a shootout.
    """
    ot_minutes: Optional[float] = 5.0
    ot_rate_multiplier: float = 2.0
    shootout_home_share: float = 0.5

    def p_home_given_tie(self, lambda_home: float, lambda_away: float) -> float:
        total = lambda_home + lambda_away
        if total <= 0:
            raise ValueError("expected goals must be positive")
        share_home_first = lambda_home / total
        if self.ot_minutes is None:
            return share_home_first
        rate = self.ot_rate_multiplier * total / 60.0
        p_goal = 1.0 - float(np.exp(-rate * self.ot_minutes))
        return p_goal * share_home_first + (1.0 - p_goal) * self.shootout_home_share

    def p_decided_in_overtime(self, lambda_total: float) -> float:
        if self.ot_minutes is None:
            return 1.0
        return 1.0 - float(np.exp(-self.ot_rate_multiplier * lambda_total / 60.0 * self.ot_minutes))


def fit_ot_multiplier(lambda_total: float, share_decided_in_overtime: float, ot_minutes: float = 5.0) -> float:
    """Multiplier m with 1 - exp(-m * lambda_total / 60 * ot_minutes) = the observed share of overtime games ended before the shootout."""
    if not 0.0 < share_decided_in_overtime < 1.0:
        raise ValueError("share must be strictly between 0 and 1")
    return float(-np.log(1.0 - share_decided_in_overtime) * 60.0 / (lambda_total * ot_minutes))


def hockey_full_game(dist: ScoreDistribution, lambda_home: float, lambda_away: float, rule: HockeyOvertime) -> ScoreDistribution:
    """Resolve regulation ties through overtime goals (proportional to scoring rates) and a shootout."""
    return resolve_ties(dist, rule.p_home_given_tie(lambda_home, lambda_away), increment=1)


# ----------------------------------------------------------------------------- basketball

def _discrete_normal(mean: float, sd: float, size: int) -> np.ndarray:
    """Probability of 0..size-1 points: a normal discretised with continuity correction, clipped at 0."""
    edges = np.arange(size + 1) - 0.5
    cdf = norm.cdf(edges, loc=mean, scale=sd)
    pmf = np.diff(cdf)
    pmf[0] += cdf[0]                      # mass below -0.5 sits on zero points
    return pmf / pmf.sum()


def basketball_overtime(dist: ScoreDistribution, mean_home: float, mean_away: float, sd_home: float, sd_away: float,
                        regulation_minutes: float = 48.0, ot_minutes: float = 5.0, max_overtimes: int = 5,
                        ot_points_cap: int = 40) -> ScoreDistribution:
    """Resolve regulation ties by repeated overtime periods until one side leads.

    Each overtime scores `mean * ot_minutes / regulation_minutes` per team (variance scaled the same
    way, teams independent). Tied overtimes repeat; any mass still tied after `max_overtimes` is split
    evenly with a one-point winner (a probability of order 0.1^max_overtimes).
    """
    if regulation_minutes <= 0 or ot_minutes <= 0:
        raise ValueError("minutes must be positive")
    scale = ot_minutes / regulation_minutes
    f_h = _discrete_normal(mean_home * scale, sd_home * np.sqrt(scale), ot_points_cap + 1)
    f_a = _discrete_normal(mean_away * scale, sd_away * np.sqrt(scale), ot_points_cap + 1)
    joint = np.outer(f_h, f_a)
    tie_by_points = np.diag(joint).copy()                    # P(both score a points in an overtime)
    non_tie = joint - np.diag(tie_by_points)
    n_carry = (max_overtimes + 1) * ot_points_cap + 1
    carry = np.zeros(n_carry)                                # carry[c]: mass still tied after j overtimes, c points each
    carry[0] = 1.0
    final = np.zeros((n_carry + ot_points_cap, n_carry + ot_points_cap))
    for _ in range(max_overtimes):
        nxt = np.zeros(n_carry)
        for c in np.nonzero(carry)[0]:
            if carry[c] < 1e-18:
                continue
            final[c:c + ot_points_cap + 1, c:c + ot_points_cap + 1] += carry[c] * non_tie
            nxt[c:c + ot_points_cap + 1] += carry[c] * tie_by_points
        carry = nxt
    residual = carry                                         # still tied after the last allowed overtime
    grid = dist.grid
    n_h, n_a = grid.shape
    size = max(n_h, n_a) + final.shape[0] + 1
    out = np.zeros((size, size))
    out[:n_h, :n_a] = grid
    tied = _tied_mass(grid)
    for k in range(len(tied)):
        mass = tied[k]
        if mass == 0.0:
            continue
        out[k, k] -= mass
        out[k:k + final.shape[0], k:k + final.shape[1]] += mass * final
        for c in np.nonzero(residual)[0]:
            out[k + c + 1, k + c] += 0.5 * mass * residual[c]
            out[k + c, k + c + 1] += 0.5 * mass * residual[c]
    keep = int(np.max(np.nonzero(out.sum(axis=1) > 1e-16)[0])) + 1
    keep_a = int(np.max(np.nonzero(out.sum(axis=0) > 1e-16)[0])) + 1
    out = out[:keep, :keep_a]
    return ScoreDistribution(out, np.arange(out.shape[0]), np.arange(out.shape[1]), endpoint="full_game",
                             metadata={**dist.metadata, "endpoint_rule": "repeated_overtime_periods",
                                       "ot_minutes": ot_minutes, "max_overtimes": max_overtimes})


# ----------------------------------------------------------------------------- baseball

def baseball_extra_innings(dist: ScoreDistribution, runs_per_half_inning: Sequence[float], innings_cap: Optional[int] = None,
                           walk_off_overshoot_share: float = 0.275, runaway_cap: int = 12) -> ScoreDistribution:
    """Resolve a tie after nine innings with extra half-innings.

    `runs_per_half_inning[r]` is P(a team scores r runs in an extra half-inning) with the final
    entry meaning "that many or more". The away side bats first. If the home side then outscores
    the visitors it wins at once; a completed bottom half with fewer runs loses with the exact
    score; equal runs continue.

    A walk-off ends the game when the winning run scores, so the final margin is usually one run
    but sometimes more (a home run). `walk_off_overshoot_share` is the probability that the home
    side is credited with the full inning's runs rather than a one-run win; 0.275 reproduces the
    reference 68.5% one-run share after extras in RULES_BASEBALL (use `fit_walk_off_overshoot` to refit).

    innings_cap: number of extra innings allowed (None = play until decided, as in MLB). Leagues
    that permit ties (KBO, NPB) keep the remaining tied mass as a tie. With no cap, mass still tied
    after `runaway_cap` innings is split evenly with a one-run winner.
    """
    if not 0.0 <= walk_off_overshoot_share <= 1.0:
        raise ValueError("walk_off_overshoot_share must lie in [0, 1]")
    q = np.asarray(runs_per_half_inning, dtype=float)
    if q.ndim != 1 or len(q) < 2 or abs(q.sum() - 1.0) > 1e-9 or np.any(q < 0):
        raise MissingInputs("extra-inning run distribution must be a probability vector with at least two entries")
    r_max = len(q) - 1
    innings = innings_cap if innings_cap is not None else runaway_cap
    phi = walk_off_overshoot_share
    p_tie_inning = float(np.sum(q * q))
    pairs_home_wins, pairs_away_wins = [], []                  # (away runs a, home runs h, probability)
    tie_runs = np.zeros(r_max + 1)                             # tie with both scoring a
    for a in range(r_max + 1):
        for h in range(r_max + 1):
            p = q[a] * q[h]
            if h > a:
                pairs_home_wins.append((a, h, p))
            elif h == a:
                tie_runs[a] += p
            else:
                pairs_away_wins.append((a, h, p))
    grid = dist.grid
    n_h, n_a = grid.shape
    pad = innings * r_max + r_max + 2
    out = np.zeros((n_h + pad, n_a + pad))
    out[:n_h, :n_a] = grid
    tied = _tied_mass(grid)
    for k in range(len(tied)):
        mass = tied[k]
        if mass == 0.0:
            continue
        out[k, k] -= mass
        carry = {0: mass}                                      # accumulated tied runs c -> mass
        for _ in range(innings):
            nxt = {}
            for c, m in carry.items():
                for a, h, p in pairs_home_wins:
                    out[k + c + a + 1, k + c + a] += m * p * (1.0 - phi)
                    out[k + c + h, k + c + a] += m * p * phi
                for a, h, p in pairs_away_wins:
                    out[k + c + h, k + c + a] += m * p
                for a in range(r_max + 1):
                    if tie_runs[a] > 0:
                        nxt[c + a] = nxt.get(c + a, 0.0) + m * tie_runs[a]
            carry = nxt
        for c, m in carry.items():
            if innings_cap is not None:
                out[k + c, k + c] += m                         # the league allows the tie to stand
            else:
                out[k + c + 1, k + c] += 0.5 * m
                out[k + c, k + c + 1] += 0.5 * m
    keep_h = int(np.max(np.nonzero(out.sum(axis=1) > 1e-16)[0])) + 1
    keep_a = int(np.max(np.nonzero(out.sum(axis=0) > 1e-16)[0])) + 1
    out = out[:keep_h, :keep_a]
    rule = "extra_innings_play_until_decided" if innings_cap is None else f"extra_innings_cap_{innings_cap}_tie_allowed"
    return ScoreDistribution(out, np.arange(out.shape[0]), np.arange(out.shape[1]), endpoint="full_game",
                             metadata={**dist.metadata, "endpoint_rule": rule, "p_tie_after_nine": float(tied.sum()),
                                       "p_tie_per_extra_inning": p_tie_inning, "walk_off_overshoot_share": phi})


def extras_margin_one_share(runs_per_half_inning: Sequence[float], walk_off_overshoot_share: float, innings_cap: Optional[int] = None) -> float:
    """P(final margin is exactly one run | the game went to extra innings) under the extras model."""
    n = 60
    tie_at_zero = np.zeros((n, n))
    tie_at_zero[4, 4] = 1.0
    d = baseball_extra_innings(ScoreDistribution(tie_at_zero, np.arange(n), np.arange(n)), runs_per_half_inning,
                               innings_cap=innings_cap, walk_off_overshoot_share=walk_off_overshoot_share)
    home, away = np.meshgrid(d.home_support, d.away_support, indexing="ij")
    decided = d.grid[home != away].sum()
    return float(d.grid[np.abs(home - away) == 1].sum() / decided)


def fit_walk_off_overshoot(runs_per_half_inning: Sequence[float], target_margin_one_share: float) -> float:
    """Overshoot share at which the extras model reproduces an observed one-run share after extras."""
    low, high = extras_margin_one_share(runs_per_half_inning, 1.0), extras_margin_one_share(runs_per_half_inning, 0.0)
    if not low <= target_margin_one_share <= high:
        raise ValueError(f"target {target_margin_one_share:.3f} is outside the attainable range [{low:.3f}, {high:.3f}]")
    return float((high - target_margin_one_share) / (high - low))      # the one-run share is linear in the overshoot share
