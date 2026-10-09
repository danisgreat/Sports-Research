"""Cricket engine: exact ball-by-ball resource model with phases, wickets, a chase stopping rule and overshoot (DST-11).

An innings is a Markov chain over (balls bowled, wickets lost, runs). Each ball has one of seven outcomes
(0, 1, 2, 3, 4, 6 runs or a wicket) drawn from a phase-specific distribution scaled by batting and bowling strength,
and the batting side's scoring declines with wickets lost. Everything is computed exactly by dynamic programming:

  * innings totals, and the runs (and wickets) after any ball, so powerplay and death-over rows come from the SAME
    simulation as the totals and the winner;
  * the chase: the second innings stops as soon as the target is reached, so the final score includes the boundary
    overshoot (needing 3 and hitting a six finishes on target + 3) rather than sitting exactly on the target;
  * the toss: who bats first is an explicit branch (known, or a probability), never assumed to be the home side.

No ball-by-ball data is retained in this repository, so the phase outcome probabilities are explicit inputs.
`CricketFormat.t20_illustrative()` is an UNFITTED scenario (roughly 160 runs, 8.7/6.8/10.1 runs per over by phase) for
mechanics and sensitivity analysis only; fit phase rates to Cricsheet before using them for a forecast.
Rain, reduced-overs and DLS targets are not part of the score grid (see `reduced_overs_chase`).
"""

from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Dict, Optional, Sequence, Tuple

import numpy as np
from scipy.optimize import brentq

from ..base import BaseSportEngine
from ...common.contracts import ScoreDistribution
from ...common.errors import InsufficientData, MissingInputs, NotFitted, UnknownTeam, finite_score

OUTCOME_RUNS = np.array([0, 1, 2, 3, 4, 6])           # run values of the six non-wicket outcomes
MAX_WICKETS = 10


@dataclass(frozen=True)
class PhaseRates:
    """Per-ball outcome probabilities (0, 1, 2, 3, 4, 6 runs, wicket) for balls [start, end) at league-average strength."""
    name: str
    start: int
    end: int
    pmf: Tuple[float, float, float, float, float, float, float]

    def __post_init__(self):
        if len(self.pmf) != 7 or min(self.pmf) < 0 or abs(sum(self.pmf) - 1.0) > 1e-9:
            raise ValueError(f"phase {self.name}: pmf must be seven non-negative probabilities summing to 1")


@dataclass(frozen=True)
class CricketFormat:
    name: str
    balls: int
    phases: Tuple[PhaseRates, ...]
    wicket_depth_effect: float          # fractional drop in scoring per wicket already lost (batting depth)
    max_runs: int

    def __post_init__(self):
        covered = sorted((p.start, p.end) for p in self.phases)
        if covered[0][0] != 0 or covered[-1][1] != self.balls or any(a[1] != b[0] for a, b in zip(covered, covered[1:])):
            raise ValueError("phases must tile the innings exactly")

    def phase_of(self, ball: int) -> PhaseRates:
        return next(p for p in self.phases if p.start <= ball < p.end)

    @staticmethod
    def t20_illustrative() -> "CricketFormat":
        return CricketFormat("t20", 120, (
            PhaseRates("powerplay", 0, 36, (0.370, 0.310, 0.060, 0.005, 0.145, 0.070, 0.040)),
            PhaseRates("middle", 36, 96, (0.395, 0.360, 0.070, 0.005, 0.085, 0.045, 0.040)),
            PhaseRates("death", 96, 120, (0.340, 0.260, 0.060, 0.005, 0.150, 0.115, 0.070))),
            wicket_depth_effect=0.04, max_runs=320)


def ball_pmf(rates: PhaseRates, wickets: int, depth_effect: float, run_multiplier: float, wicket_multiplier: float) -> np.ndarray:
    """Seven outcome probabilities for one ball given wickets lost and the sides' strengths."""
    p = np.array(rates.pmf, dtype=float)
    scale = run_multiplier * max(1.0 - depth_effect * wickets, 0.2)
    p[1:6] *= scale
    p[6] *= wicket_multiplier
    p[0] = 1.0 - p[1:].sum()
    if p[0] < 0.0:
        raise ValueError("strength multipliers push the boundary and wicket probabilities above one")
    return p


@dataclass
class InningsTable:
    """Exact state probabilities of an innings: P[b, w, r] after b balls, plus the transition mass into each score by k runs."""
    fmt: CricketFormat
    states: np.ndarray                    # (balls + 1, wickets + 1, max_runs + 1)
    landing: np.ndarray                   # (len(OUTCOME_RUNS), max_runs + 1): mass of live states moving by k runs and landing on x

    def runs_pmf(self, after_balls: Optional[int] = None) -> np.ndarray:
        """P(runs) after `after_balls` balls (all-out sides keep their runs); the final innings total by default."""
        b = self.fmt.balls if after_balls is None else after_balls
        return self.states[b].sum(axis=0)

    def wickets_pmf(self, after_balls: int) -> np.ndarray:
        return self.states[after_balls].sum(axis=1)

    def first_passage(self, target: int) -> np.ndarray:
        """P(the innings first reaches `target` or more with a final tally x) for x >= target (the boundary overshoot)."""
        out = np.zeros(self.fmt.max_runs + 1)
        for idx, k in enumerate(OUTCOME_RUNS):
            if k == 0:
                continue
            lo, hi = max(target, 0), min(target + k - 1, self.fmt.max_runs)
            if lo <= hi:
                out[lo:hi + 1] += self.landing[idx, lo:hi + 1]
        return out


def run_innings(fmt: CricketFormat, run_multiplier: float = 1.0, wicket_multiplier: float = 1.0, balls: Optional[int] = None) -> InningsTable:
    """Exact forward dynamic program for one innings (optionally truncated to `balls` for a reduced-overs innings).

    Results are memoised; treat the returned arrays as read-only.
    """
    return _run_innings(fmt, round(float(run_multiplier), 9), round(float(wicket_multiplier), 9), balls)


@lru_cache(maxsize=256)
def _run_innings(fmt: CricketFormat, run_multiplier: float, wicket_multiplier: float, balls: Optional[int]) -> InningsTable:
    n_balls = fmt.balls if balls is None else balls
    if not 0 < n_balls <= fmt.balls:
        raise ValueError("balls must lie in 1..format balls")
    R = fmt.max_runs
    state = np.zeros((n_balls + 1, MAX_WICKETS + 1, R + 1))
    state[0, 0, 0] = 1.0
    landing = np.zeros((len(OUTCOME_RUNS), R + 1))
    for b in range(n_balls):
        rates = fmt.phase_of(b)
        state[b + 1, MAX_WICKETS] += state[b, MAX_WICKETS]                   # all out: the innings is over
        for w in range(MAX_WICKETS):
            current = state[b, w]
            if not current.any():
                continue
            p = ball_pmf(rates, w, fmt.wicket_depth_effect, run_multiplier, wicket_multiplier)
            for idx, k in enumerate(OUTCOME_RUNS):
                moved = current * p[idx]
                if k == 0:
                    state[b + 1, w] += moved
                else:
                    state[b + 1, w, k:] += moved[:R + 1 - k]
                    landing[idx, k:] += moved[:R + 1 - k]
            state[b + 1, w + 1] += current * p[6]
    return InningsTable(fmt, state, landing)


def calibrate_run_multiplier(fmt: CricketFormat, target_mean: float, wicket_multiplier: float = 1.0) -> float:
    """Run multiplier at which the expected innings total equals `target_mean` (memoised)."""
    return _calibrate(fmt, round(float(target_mean), 6), round(float(wicket_multiplier), 9))


@lru_cache(maxsize=256)
def _calibrate(fmt: CricketFormat, target_mean: float, wicket_multiplier: float) -> float:
    values = np.arange(fmt.max_runs + 1)

    def gap(m: float) -> float:
        return float(values @ run_innings(fmt, m, wicket_multiplier).runs_pmf()) - target_mean

    # the largest multiplier that keeps every ball's outcome probabilities valid (dot-ball mass stays non-negative)
    limit = min((1.0 - ph.pmf[6] * wicket_multiplier) / sum(ph.pmf[1:6]) for ph in fmt.phases)
    low, high = 0.4, min(1.9, 0.999 * limit)
    if gap(low) > 0 or gap(high) < 0:
        raise ValueError(f"expected total {target_mean:.0f} is outside what the phase rates can produce")
    return float(brentq(gap, low, high, xtol=1e-6))


def chase_grid(first: InningsTable, second: InningsTable) -> np.ndarray:
    """Joint (first-innings score, second-innings score) grid under the chase stopping rule.

    Second-innings finals below the target are the unrestricted finals; at or above the target the innings stops on
    the ball that reaches it, so the final tally is the first-passage landing (target ... target + 5).
    """
    R = first.fmt.max_runs
    finals = second.runs_pmf()
    grid = np.zeros((R + 1, R + 1))
    for s1, p1 in enumerate(first.runs_pmf()):
        if p1 < 1e-14:
            continue
        target = s1 + 1
        grid[s1, :min(target, R + 1)] = p1 * finals[:min(target, R + 1)]
        if target <= R:
            reach = second.first_passage(target)
            grid[s1, target:] += p1 * reach[target:]
    return grid


class CricketEngine(BaseSportEngine):
    """Predictive engine for limited-overs cricket (T20; other formats via a `CricketFormat`).

    Team strength enters as a run multiplier (calibrated so that the team's expected total matches a supplied or fitted
    figure) and a wicket multiplier. Context keys: `format`, `bat_first` ("home"/"away") or `p_home_bats_first`,
    `home_expected_runs`/`away_expected_runs` (or fitted team averages), `home_wicket_rate`/`away_wicket_rate`.
    """

    def __init__(self, formats: Optional[Dict[str, CricketFormat]] = None, unknown_team_policy: str = "refuse"):
        super().__init__("cricket", None, unknown_team_policy)
        self.formats: Dict[str, CricketFormat] = dict(formats or {})
        self.team_runs: Dict[str, float] = {}          # fitted mean first-or-second-innings total per team and format key "fmt|team"
        self.team_allowed: Dict[str, float] = {}
        self.format_means: Dict[str, float] = {}

    def fit(self, train_data: Any) -> "CricketEngine":
        """Fit team batting and bowling ratios from matches: {format, home_team, away_team, home_runs, away_runs}."""
        if not isinstance(train_data, (list, tuple)):
            raise ValueError("train_data must be a list of match dicts; an engine is never 'fitted' on nothing")
        scored: Dict[str, Dict[str, list]] = {}
        allowed: Dict[str, Dict[str, list]] = {}
        by_format: Dict[str, list] = {}
        for index, m in enumerate(train_data):
            fmt = str(m.get("format", "")).lower()
            if not fmt:
                raise MissingInputs(f"training record {index} lacks a format")
            home, away = m.get("home_team"), m.get("away_team")
            if home is None or away is None:
                raise MissingInputs(f"training record {index} lacks team names")
            hr, ar = finite_score(m, "home_runs", "innings1_runs"), finite_score(m, "away_runs", "innings2_runs")
            for team, runs, conceded in ((home, hr, ar), (away, ar, hr)):
                scored.setdefault(fmt, {}).setdefault(team, []).append(runs)
                allowed.setdefault(fmt, {}).setdefault(team, []).append(conceded)
            by_format.setdefault(fmt, []).extend([hr, ar])
        for fmt, runs in by_format.items():
            if len(runs) < 20:
                raise InsufficientData(f"format {fmt!r} needs at least 10 matches, got {len(runs) // 2}")
            self.format_means[fmt] = float(np.mean(runs))
            k = 8.0                                                         # shrinkage in innings, not a fixed blend
            for team, values in scored[fmt].items():
                n = len(values)
                self.team_runs[f"{fmt}|{team}"] = (np.sum(values) + k * self.format_means[fmt]) / (n + k)
                self.team_allowed[f"{fmt}|{team}"] = (np.sum(allowed[fmt][team]) + k * self.format_means[fmt]) / (n + k)
        self.is_fitted = True
        return self

    # ------------------------------------------------------------------- inputs
    def _format(self, ctx: Dict[str, Any]) -> CricketFormat:
        name = str(ctx.get("format", "")).lower()
        if not name:
            raise MissingInputs("cricket: the context needs a format")
        if name not in self.formats:
            raise MissingInputs(f"cricket: no CricketFormat registered for {name!r}; register one (for example CricketFormat.t20_illustrative())")
        return self.formats[name]

    def _expected_runs(self, ctx: Dict[str, Any], fmt_name: str) -> Tuple[float, float]:
        if ctx.get("home_expected_runs") is not None and ctx.get("away_expected_runs") is not None:
            return float(ctx["home_expected_runs"]), float(ctx["away_expected_runs"])
        home, away = ctx.get("home_team"), ctx.get("away_team")
        if not self.is_fitted:
            raise NotFitted("cricket: pass home_expected_runs/away_expected_runs, or fit the engine on match records")
        out = []
        for team, opp in ((home, away), (away, home)):
            kt, ko = f"{fmt_name}|{team}", f"{fmt_name}|{opp}"
            if kt not in self.team_runs or ko not in self.team_allowed:
                if self.unknown_team_policy != "league_average" or fmt_name not in self.format_means:
                    raise UnknownTeam(f"cricket: no fitted batting/bowling record for {team!r} or {opp!r} in {fmt_name!r}")
                self._warn(f"unknown team in {team!r} v {opp!r}: format-average used; uncertainty not modelled")
            mean = self.format_means[fmt_name]
            bat = self.team_runs.get(kt, mean)
            bowl = self.team_allowed.get(ko, mean)
            out.append(mean * (bat / mean) * (bowl / mean))
        return out[0], out[1]

    # --------------------------------------------------------------- prediction
    def innings_tables(self, ctx: Dict[str, Any]) -> Tuple[InningsTable, InningsTable, CricketFormat]:
        fmt = self._format(ctx)
        mu_h, mu_a = self._expected_runs(ctx, fmt.name)
        pitch = float(ctx.get("pitch_run_factor", 1.0))
        wk_h, wk_a = float(ctx.get("home_wicket_rate", 1.0)), float(ctx.get("away_wicket_rate", 1.0))
        home = run_innings(fmt, calibrate_run_multiplier(fmt, mu_h * pitch, wk_h), wk_h)
        away = run_innings(fmt, calibrate_run_multiplier(fmt, mu_a * pitch, wk_a), wk_a)
        return home, away, fmt

    def predict_distribution(self, match_context: Dict[str, Any], endpoint: str = "regulation") -> ScoreDistribution:
        """Joint (home runs, away runs) with the chase stopping rule; a tie cell is a tied score (super over)."""
        if endpoint != "regulation":
            raise ValueError("the grid settles on the full-length match; use reduced_overs_chase for rain-affected targets")
        home, away, fmt = self.innings_tables(match_context)
        p_home_first = self._p_home_first(match_context)
        R = fmt.max_runs
        grid = np.zeros((R + 1, R + 1))
        if p_home_first > 0.0:
            grid += p_home_first * chase_grid(home, away)                       # (home score, away score)
        if p_home_first < 1.0:
            grid += (1.0 - p_home_first) * chase_grid(away, home).T             # away bat first: transpose to (home, away)
        support = np.arange(R + 1)
        return ScoreDistribution(grid, support, support, endpoint="regulation",
                                 metadata={"model": "cricket_ball_by_ball_dp", "format": fmt.name, "p_home_bats_first": p_home_first,
                                           "warnings": self._take_warnings()})

    @staticmethod
    def _p_home_first(ctx: Dict[str, Any]) -> float:
        if ctx.get("p_home_bats_first") is not None:
            p = float(ctx["p_home_bats_first"])
            if not 0.0 <= p <= 1.0:
                raise ValueError("p_home_bats_first must lie in [0, 1]")
            return p
        side = ctx.get("bat_first")
        if side not in ("home", "away"):
            raise MissingInputs("cricket: say who bats first (bat_first='home'|'away') or give p_home_bats_first; the toss is never assumed")
        return 1.0 if side == "home" else 0.0

    def phase_runs(self, ctx: Dict[str, Any], team: str, after_balls: int) -> np.ndarray:
        """P(runs scored after `after_balls` balls) for the home or away side, from the same simulation as the totals."""
        home, away, _ = self.innings_tables(ctx)
        table = home if team == "home" else away
        return table.runs_pmf(after_balls)

    def reduced_overs_chase(self, ctx: Dict[str, Any], overs_second_innings: int, resource_ratio: float, team: str = "away") -> Dict[str, float]:
        """Win probabilities for a rain-shortened chase with an explicit revised target.

        The side batting second faces `overs_second_innings` overs with target floor(first-innings score * resource_ratio) + 1,
        where `resource_ratio` (second-innings resources / first-innings resources) is supplied by the user from the DLS
        table in force; this engine does not embed the official tables. Returns P(chasing side wins), P(defending side wins).
        """
        if not 0.0 < resource_ratio <= 1.5:
            raise ValueError("resource_ratio must lie in (0, 1.5]")
        home, away, fmt = self.innings_tables(ctx)
        first, second = (home, away) if team == "away" else (away, home)
        mult = (calibrate_run_multiplier(fmt, self._expected_runs(ctx, fmt.name)[1 if team == "away" else 0]),)
        short = run_innings(fmt, mult[0], 1.0, balls=overs_second_innings * 6)
        win = 0.0
        for s1, p1 in enumerate(first.runs_pmf()):
            if p1 < 1e-14:
                continue
            target = int(np.floor(s1 * resource_ratio)) + 1
            win += p1 * float(short.first_passage(target).sum()) if target <= fmt.max_runs else 0.0
        return {"chasing_side_wins": win, "defending_side_wins": 1.0 - win}
