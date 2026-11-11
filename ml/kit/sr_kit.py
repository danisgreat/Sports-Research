"""Sports Research calculation kit for research chats (KIT-v1, CR-2026.11.11-R1).

ONE self-contained file: it needs Python 3.10+, numpy and scipy. Test the actual chat runtime; never assume availability.
Upload it with the parameter files of the same version (KIT_PARAMETERS_v24.15.csv and KIT_CRICKET_PHASES_v24.15.csv) and run
it; never retype its arithmetic by hand. Every run prints a KIT_RECEIPT block. The repository re-runs the receipt with
``python -m ml kit verify --receipt FILE``: an exact engine must reproduce every probability to 1e-9, a simulation (same
seed) to 3 Monte Carlo standard errors. A receipt that does not reproduce is not used.

One engine per sport; league differences are parameter rows and rule switches, never different code:

    points    basketball, AFL/AFLW, NRL, rugby union, NFL   joint normal on margin and total; overtime as real periods
                                                             (basketball), golden point (NRL), draws kept (AFL home-and-away,
                                                             union), NFL overtime by the repository's three-point rule
    soccer    every soccer competition                       Dixon-Coles Poisson; first-half goals from the competition's
                                                             first-half share; corners only from a measured row
    hockey    every ice-hockey competition                   Poisson regulation, then overtime and shootout
    baseball  every baseball competition                     negative-binomial runs; extra innings resolved
    tennis    every tennis tour                              exact point -> game -> set -> match recursion
    cricket   T20 and ODI first innings                      ball-by-ball innings simulation from measured phase tables

Usage inside a chat:

    import sr_kit as K
    params = K.load_params("KIT_PARAMETERS_v24.15.csv")
    row = K.row(params, "Basketball/B League")
    out = K.points_from_centre(row, total=173.0, margin=11.5, lines=[
        dict(label="Jets -14.5", family="handicap", side="HOME", line=-14.5),
        dict(label="Evessa +14.5", family="handicap", side="AWAY", line=14.5),
        dict(label="Over 173.5", family="total", side="OVER", line=173.5),
        dict(label="Under 173.5", family="total", side="UNDER", line=173.5)])
    print(K.receipt("points_from_centre", dict(competition=row["competition"], total=173.0, margin=11.5), out))

Market-blind: nothing here reads a price, a line movement or a tip. A supplied line is only the question asked.
"""
from __future__ import annotations

import csv
import hashlib
import math
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.signal import fftconvolve

KIT_VERSION = "SR-KIT-v24.15"


def convolve2d(a, b):
    """Same full convolution, without the dense extra-period runtime cost; remove FFT roundoff below zero."""
    return np.maximum(fftconvolve(a, b, mode="full"), 0.0)
MASS_TOL = 1e-9
CARD_MIN_N = 100_000


class KitError(ValueError):
    pass


# ====================================================================== the score grid
class Grid:
    """P(home = h0 + i, away = a0 + j). Every contract is read from one grid, so all rows are coherent."""

    def __init__(self, p, h0: int = 0, a0: int = 0):
        p = np.asarray(p, float)
        if p.ndim != 2 or p.size == 0 or not np.isfinite(p).all() or (p < -1e-15).any():
            raise KitError("a grid is a finite, non-negative two-dimensional array")
        s = p.sum()
        if abs(s - 1) > 1e-7:
            raise KitError(f"grid masses sum to {s}, not 1")
        self.p, self.h0, self.a0 = p, int(h0), int(a0)

    @classmethod
    def normal(cls, mean_h: float, mean_a: float, sd_margin: float, sd_total: float, n_sd: float = 6.5) -> "Grid":
        """Discretised bivariate normal with Cov(total, margin) = 0 (the repository's TB convention)."""
        if min(sd_margin, sd_total) <= 0:
            raise KitError("standard deviations must be positive")
        var = (sd_total ** 2 + sd_margin ** 2) / 4
        cov = (sd_total ** 2 - sd_margin ** 2) / 4
        c = np.array([[var, cov], [cov, var]])
        sh = sa = math.sqrt(var)
        h_lo, h_hi = max(0, int(np.floor(mean_h - n_sd * sh))), int(np.ceil(mean_h + n_sd * sh))
        a_lo, a_hi = max(0, int(np.floor(mean_a - n_sd * sa))), int(np.ceil(mean_a + n_sd * sa))
        hh, aa = np.meshgrid(np.arange(h_lo, h_hi + 1), np.arange(a_lo, a_hi + 1), indexing="ij")
        dens = stats.multivariate_normal(mean=[mean_h, mean_a], cov=c).pdf(np.stack([hh.ravel(), aa.ravel()], axis=1)).reshape(hh.shape)
        return cls(dens / dens.sum(), h_lo, a_lo)

    @classmethod
    def poisson(cls, lam_h: float, lam_a: float, rho: float = 0.0, max_goals: int | None = None) -> "Grid":
        """Poisson scores with the Dixon-Coles low-score correction tau(rho)."""
        if lam_h <= 0 or lam_a <= 0:
            raise KitError("Poisson means must be positive")
        lo, hi = max(-1 / lam_h, -1 / lam_a), min(1 / (lam_h * lam_a), 1.0)
        if not lo < rho < hi:
            raise KitError(f"rho {rho} lies outside its valid range ({lo:.3f}, {hi:.3f}) for these means")
        m = max_goals or int(max(10, np.ceil(max(lam_h, lam_a) + 8 * math.sqrt(max(lam_h, lam_a)))))
        k = np.arange(m + 1)
        g = np.outer(stats.poisson.pmf(k, lam_h), stats.poisson.pmf(k, lam_a))
        if rho:
            g[0, 0] *= 1 - lam_h * lam_a * rho
            g[0, 1] *= 1 + lam_h * rho
            g[1, 0] *= 1 + lam_a * rho
            g[1, 1] *= 1 - rho
        return cls(g / g.sum())

    @classmethod
    def negbin(cls, mu_h: float, mu_a: float, phi: float, max_runs: int | None = None) -> "Grid":
        """Independent negative-binomial scores, Var = mu + phi mu^2 (phi = 0 is Poisson)."""
        if min(mu_h, mu_a) <= 0 or phi < 0:
            raise KitError("means must be positive and dispersion non-negative")
        if phi <= 1e-9:
            return cls.poisson(mu_h, mu_a, 0.0, max_runs)
        m = max(mu_h, mu_a)
        top = max_runs or int(np.ceil(m + 10 * math.sqrt(m + phi * m * m)))
        k = np.arange(top + 1)
        n = 1 / phi
        g = np.outer(stats.nbinom.pmf(k, n, n / (n + mu_h)), stats.nbinom.pmf(k, n, n / (n + mu_a)))
        return cls(g / g.sum())

    def _hv(self):
        return np.arange(self.h0, self.h0 + self.p.shape[0])

    def _av(self):
        return np.arange(self.a0, self.a0 + self.p.shape[1])

    def margin_pmf(self):
        m = self._hv()[:, None] - self._av()[None, :]
        lo = int(m.min())
        out = np.zeros(int(m.max()) - lo + 1)
        np.add.at(out, (m - lo).ravel(), self.p.ravel())
        return np.arange(lo, lo + out.size), out

    def total_pmf(self):
        t = self._hv()[:, None] + self._av()[None, :]
        lo = int(t.min())
        out = np.zeros(int(t.max()) - lo + 1)
        np.add.at(out, (t - lo).ravel(), self.p.ravel())
        return np.arange(lo, lo + out.size), out

    def winner(self):
        m = self._hv()[:, None] - self._av()[None, :]
        return float(self.p[m > 0].sum()), float(self.p[m == 0].sum()), float(self.p[m < 0].sum())

    def handicap(self, line: float, side: str):
        mv, mp = self.margin_pmf()
        x = mv + line if side == "HOME" else -mv + line
        return float(mp[x > 0].sum()), float(mp[x == 0].sum()), float(mp[x < 0].sum())

    def total(self, line: float, side: str):
        tv, tp = self.total_pmf()
        x = tv - line if side == "OVER" else line - tv
        return float(tp[x > 0].sum()), float(tp[x == 0].sum()), float(tp[x < 0].sum())

    def team_total(self, line: float, side: str, team: str):
        marg = self.p.sum(axis=1) if team == "HOME" else self.p.sum(axis=0)
        v = self._hv() if team == "HOME" else self._av()
        x = v - line if side == "OVER" else line - v
        return float(marg[x > 0].sum()), float(marg[x == 0].sum()), float(marg[x < 0].sum())

    def summary(self) -> dict:
        tv, tp = self.total_pmf()
        mv, mp = self.margin_pmf()
        mt, mm = float(tv @ tp), float(mv @ mp)
        return dict(total_mean=mt, total_sd=float(math.sqrt(max(((tv - mt) ** 2) @ tp, 0))), margin_mean=mm,
                    margin_sd=float(math.sqrt(max(((mv - mm) ** 2) @ mp, 0))))

    def one_bonus(self, p_home_extra: float, bonus: int = 1) -> "Grid":
        """Move every tied state to a win by ``bonus`` for one side (the repository's NHL/NFL/NRL convention)."""
        g = np.zeros((self.p.shape[0] + bonus, self.p.shape[1] + bonus))
        g[: self.p.shape[0], : self.p.shape[1]] = self.p
        for i, h in enumerate(self._hv()):
            j = h - self.a0
            if 0 <= j < self.p.shape[1]:
                m = self.p[i, j]
                g[i, j] -= m
                g[i + bonus, j] += m * p_home_extra
                g[i, j + bonus] += m * (1 - p_home_extra)
        g[np.abs(g) < 1e-18] = 0
        return Grid(g / g.sum(), self.h0, self.a0)

    def periods(self, period: "Grid", max_periods: int = 8) -> "Grid":
        """Play every tied state through real extra periods (basketball overtime; identical to the repository's
        ScoreGrid.resolve_ties_periods)."""
        if period.h0 or period.a0:
            raise KitError("the extra-period grid starts at 0-0")
        g = period.p
        n = min(g.shape)
        tie = np.zeros_like(g)
        idx = np.arange(n)
        tie[idx, idx] = g[idx, idx]
        decided = g - tie
        if decided.sum() <= 0:
            raise KitError("an extra period that can never decide the game")
        resolved, carry = decided.copy(), tie.copy()
        for _ in range(max_periods - 1):
            step = convolve2d(carry, decided)
            grown = np.zeros((max(resolved.shape[0], step.shape[0]), max(resolved.shape[1], step.shape[1])))
            grown[: resolved.shape[0], : resolved.shape[1]] += resolved
            grown[: step.shape[0], : step.shape[1]] += step
            resolved = grown
            carry = convolve2d(carry, tie)
        resolved = resolved / resolved.sum()
        out = np.zeros((self.p.shape[0] + resolved.shape[0], self.p.shape[1] + resolved.shape[1]))
        out[: self.p.shape[0], : self.p.shape[1]] = self.p
        for i, h in enumerate(self._hv()):
            j = h - self.a0
            if 0 <= j < self.p.shape[1] and self.p[i, j] > 0:
                m = self.p[i, j]
                out[i, j] -= m
                out[i: i + resolved.shape[0], j: j + resolved.shape[1]] += m * resolved
        out[np.abs(out) < 1e-18] = 0.0
        return Grid(out / out.sum(), self.h0, self.a0)


def mixture(parts) -> Grid:
    """A declared scenario mixture [(weight, Grid), ...] with weights fixed before pricing (unconfirmed lineups)."""
    weights = np.array([w for w, _ in parts], float)
    if (weights < 0).any() or abs(weights.sum() - 1) > 1e-9:
        raise KitError("mixture weights are non-negative and sum to 1")
    h0 = min(g.h0 for _, g in parts)
    a0 = min(g.a0 for _, g in parts)
    nh = max(g.h0 + g.p.shape[0] for _, g in parts) - h0
    na = max(g.a0 + g.p.shape[1] for _, g in parts) - a0
    out = np.zeros((nh, na))
    for w, g in parts:
        out[g.h0 - h0: g.h0 - h0 + g.p.shape[0], g.a0 - a0: g.a0 - a0 + g.p.shape[1]] += w * g.p
    return Grid(out / out.sum(), h0, a0)


# ====================================================================== parameters
def load_params(path) -> dict:
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    versions = {r.get("kit_version", "") for r in rows}
    if versions != {KIT_VERSION}:
        raise KitError(f"parameter file is for {sorted(versions)}, this kit is {KIT_VERSION}: upload matching files")
    if len({r['competition'] for r in rows}) != len(rows):
        raise KitError("duplicate competition parameter rows are ambiguous")
    return {r["competition"]: r for r in rows}


def row(params: dict, competition: str) -> dict:
    """The competition's own row; otherwise its family prior (widths +10%), and say so."""
    if competition in params and params[competition]["status"] not in ("NOT_USABLE", "NOT_ESTIMATED", "NOT_COVERED"):
        return params[competition]
    sport, last = competition.split("/")[0].strip(), competition.split("/")[-1].strip().lower()
    family = {"Basketball": "FAMILY_PRIOR:BASKETBALL_NBA48" if last in ("nba", "nba g league") else "FAMILY_PRIOR:BASKETBALL_FIBA40",
              "AFL": "FAMILY_PRIOR:AFL", "State Level AFL": "FAMILY_PRIOR:AFL", "Australian Rules": "FAMILY_PRIOR:AFL",
              "American Football": "FAMILY_PRIOR:AMERICAN_FOOTBALL", "College Football": "FAMILY_PRIOR:AMERICAN_FOOTBALL",
              "Rugby League": "FAMILY_PRIOR:RUGBY_LEAGUE", "Rugby Union": "FAMILY_PRIOR:RUGBY_UNION", "Soccer": "FAMILY_PRIOR:SOCCER",
              "Baseball": "FAMILY_PRIOR:BASEBALL", "Ice Hockey": "FAMILY_PRIOR:ICE_HOCKEY"}.get(sport)
    if family not in params:
        raise KitError(f"{competition}: no row and no family prior; price qualitatively and say NOT_COVERED")
    out = dict(params[family])
    out["note"] = f"FAMILY_PRIOR for {competition} (widths +10%)"
    out["admission_status"] = "UNCALIBRATED_FAMILY_PROXY"
    for k in ("resid_margin_sd", "resid_total_sd", "raw_margin_sd", "raw_total_sd"):
        if out.get(k):
            out[k] = str(round(float(out[k]) * 1.10, 3))
    return out


def _f(r: dict, key: str, default=None):
    v = (r.get(key) or "").strip()
    if v == "":
        if default is None:
            raise KitError(f"{r.get('competition')}: parameter {key} is NOT_ESTIMATED")
        return default
    return float(v)


# ====================================================================== pricing
FAMILIES = ("winner", "regulation_winner", "handicap", "total", "team_total", "first_half_total", "corners_total", "set_handicap",
            "innings_total", "checkpoint_total")


def price(grid: Grid, lines, *, extra: dict | None = None) -> list[dict]:
    """W/P/L and p = W/(W+L) for every line from one grid. ``extra`` maps a family to its own grid (first-half, corners)."""
    out = []
    for ln in lines:
        fam, side = ln["family"], ln["side"].upper()
        g = (extra or {}).get(fam, grid)
        if fam in ("winner", "regulation_winner"):
            hw, dr, aw = g.winner()
            w = {"HOME": hw, "DRAW": dr, "AWAY": aw}[side]
            res = (w, 0.0, 1 - w)
        elif fam == "handicap":
            res = g.handicap(float(ln["line"]), side)
        elif fam in ("total", "first_half_total", "corners_total"):
            res = g.total(float(ln["line"]), side)
        elif fam == "team_total":
            res = g.team_total(float(ln["line"]), side, ln["team"].upper())
        else:
            raise KitError(f"{ln['label']}: family {fam} is not priced from a score grid")
        w, p, l = res
        out.append(dict(label=ln["label"], family=fam, side=side, line=ln.get("line", ""), w=w, p=p, l=l,
                        final_p=w / (w + l) if w + l > 0 else float("nan")))
    return out


def tb2_centre(row_: dict, home: dict, away: dict, *, neutral: bool = False, lm: float | None = None) -> tuple[float, float]:
    """TB-2-MD (points) centre from season-to-date points for/against and games: total and home margin.
    ``home``/``away`` = dict(pf=, pa=, n=). k and the home edge come from the row; the league mean per team-game ``lm``
    defaults to half the row's mean total."""
    k, he = _f(row_, "k"), (0.0 if neutral else _f(row_, "home_edge"))
    lm = lm if lm is not None else _f(row_, "mean_total") / 2
    rate = lambda s, x: (s[x] + k * lm) / (s["n"] + k)
    oh, dh, oa, da = rate(home, "pf"), rate(home, "pa"), rate(away, "pf"), rate(away, "pa")
    return (oh + da - lm) + (oa + dh - lm), (oh - dh) - (oa - da) + he


def points_from_centre(row_: dict, total: float, margin: float, lines, *, sd_margin: float | None = None, sd_total: float | None = None,
                       finals: bool = False) -> dict:
    """Points sports from a centre (the frozen reference plus logged adjustments). Widths default to the competition's
    residual SDs (the floor); a narrower width needs a written exception on the card."""
    sport = row_["sport"]
    # default widths: the repository reference's own SDs where it has them (TB-1-MD constants), else the residual floor
    sdm = sd_margin if sd_margin is not None else _f(row_, "ref_sd_margin", 0.0) or _f(row_, "resid_margin_sd")
    sdt = sd_total if sd_total is not None else _f(row_, "ref_sd_total", 0.0) or _f(row_, "resid_total_sd")
    mh, ma = (total + margin) / 2, (total - margin) / 2
    grid = Grid.normal(mh, ma, sdm, sdt)
    ties = row_["ties"]
    if finals and sport in ("AFL", "Australian Rules", "State Level AFL"):
        ties = "extra_time_afl"                 # AFL-ET-1: finals lines include extra time
    if ties == "overtime_periods":
        f = _f(row_, "ot_fraction")
        var = (sdt ** 2 + sdm ** 2) / 4 * f
        cov = (sdt ** 2 - sdm ** 2) / 4 * f
        period = _period_grid(max(mh * f, 0.5), max(ma * f, 0.5), np.array([[var, cov], [cov, var]]))
        grid = grid.periods(period)
    elif ties in ("overtime_nfl", "golden_point", "extra_time_afl"):
        f = _f(row_, "ot_fraction", 10 / 60 if ties == "overtime_nfl" else 0.1)
        p_home = float(stats.norm.cdf(margin * math.sqrt(f) / sdm))
        grid = grid.one_bonus(p_home, 3 if ties == "overtime_nfl" else 1)
    elif ties != "draw":
        raise KitError(f"unknown tie rule {ties}")
    return dict(grid=grid, rows=price(grid, lines), widths=dict(sd_margin=sdm, sd_total=sdt), ties=ties)


def _period_grid(mean_h: float, mean_a: float, cov) -> Grid:
    """One extra period's points, discretised on the same support rule as the repository (mean +/- 6.5 SD, cut at 0), with
    the cells below the support kept at zero so the grid starts at 0-0."""
    sh, sa = math.sqrt(cov[0, 0]), math.sqrt(cov[1, 1])
    lo_h, lo_a = max(0, int(np.floor(mean_h - 6.5 * sh))), max(0, int(np.floor(mean_a - 6.5 * sa)))
    hh, aa = np.meshgrid(np.arange(lo_h, int(np.ceil(mean_h + 6.5 * sh)) + 1), np.arange(lo_a, int(np.ceil(mean_a + 6.5 * sa)) + 1), indexing="ij")
    dens = stats.multivariate_normal(mean=[mean_h, mean_a], cov=cov).pdf(np.stack([hh.ravel(), aa.ravel()], axis=1)).reshape(hh.shape)
    full = np.zeros((lo_h + dens.shape[0], lo_a + dens.shape[1]))
    full[lo_h:, lo_a:] = dens / dens.sum()
    return Grid(full)


def soccer_from_means(row_: dict, lam_home: float, lam_away: float, lines, *, rho: float | None = None) -> dict:
    """Full-time goals (90 minutes plus stoppage) as Dixon-Coles Poisson; first-half goals as Poisson with the row's
    first-half share; corners only when the row has a measured corners mean and dispersion (else NOT_ESTIMATED)."""
    r = _f(row_, "dc_rho", 0.0) if rho is None else rho
    grid = Grid.poisson(lam_home, lam_away, r)
    extra = {}
    if any(ln["family"] == "first_half_total" for ln in lines):
        share = _f(row_, "first_half_share")
        extra["first_half_total"] = Grid.poisson(lam_home * share, lam_away * share)
    if any(ln["family"] == "corners_total" for ln in lines):
        mean, disp = _f(row_, "corners_mean"), _f(row_, "corners_disp")
        extra["corners_total"] = Grid.negbin(mean / 2, mean / 2, disp)
    return dict(grid=grid, rows=price(grid, lines, extra=extra), rho=r)


def soccer_tb1_means(row_: dict, home: dict, away: dict, *, neutral: bool = False) -> tuple[float, float]:
    """TB-1-MD goal means (the average form the repository uses for goal leagues): each side's expected goals is the mean
    of its own attack and the opponent's defence, shrunk with k toward the league mean per team-game."""
    k, he, lm = _f(row_, "k"), (0.0 if neutral else _f(row_, "home_edge")), _f(row_, "mean_total") / 2
    rate = lambda s, x: (s[x] + k * lm) / (s["n"] + k)
    oh, dh, oa, da = rate(home, "pf"), rate(home, "pa"), rate(away, "pf"), rate(away, "pa")
    total = (oh + da) / 2 + (oa + dh) / 2
    margin = ((oh - dh) - (oa - da)) / 2 + he
    return max((total + margin) / 2, 0.05), max((total - margin) / 2, 0.05)


def hockey_from_means(row_: dict, lam_home: float, lam_away: float, lines, *, p_home_shootout: float = 0.5) -> dict:
    """Regulation Poisson; a regulation tie goes to overtime (home wins it in proportion to the regulation rates) or the
    shootout. The full-game score credits the winner one goal (H-R1)."""
    reg = Grid.poisson(lam_home, lam_away)
    ot_share = _f(row_, "ot_decided_share")            # of tied games, the share decided in overtime rather than a shootout
    p_home = ot_share * lam_home / (lam_home + lam_away) + (1 - ot_share) * p_home_shootout
    grid = reg.one_bonus(p_home, 1)
    return dict(grid=grid, regulation=reg, rows=price(grid, lines, extra={"regulation_winner": reg}))


def baseball_from_means(row_: dict, mu_home: float, mu_away: float, lines, *, phi: float | None = None, ties_allowed: bool = False) -> dict:
    """Negative-binomial runs; a nine-inning tie goes to extras (one-run margin, home by its run share) unless the competition
    allows ties (KBO, NPB). Run lines near ties are approximate: use the simulator only after its structural check passes."""
    d = _f(row_, "nb_dispersion") if phi is None else phi
    grid = Grid.negbin(mu_home, mu_away, d)
    if not ties_allowed:
        grid = grid.one_bonus(mu_home / (mu_home + mu_away), 1)
    return dict(grid=grid, rows=price(grid, lines))


# ====================================================================== tennis (exact)
def p_game(p: float) -> float:
    q = 1 - p
    return p ** 4 * (1 + 4 * q + 10 * q * q) + 20 * p ** 5 * q ** 3 / (1 - 2 * p * q)


def p_tiebreak(pa: float, pb: float, a_first: bool, to: int = 7) -> float:
    memo: dict = {}

    def server_is_a(k: int) -> bool:
        first = (k + 1) // 2 % 2 == 0
        return first if a_first else not first

    def go(a: int, b: int) -> float:
        if a >= to and a - b >= 2:
            return 1.0
        if b >= to and b - a >= 2:
            return 0.0
        if a + b >= 80:
            return 0.5
        if (a, b) in memo:
            return memo[(a, b)]
        pt = pa if server_is_a(a + b) else 1 - pb
        v = pt * go(a + 1, b) + (1 - pt) * go(a, b + 1)
        memo[(a, b)] = v
        return v

    return go(0, 0)


def set_pmf(pa: float, pb: float, a_first: bool, kind: str = "standard_tb") -> dict:
    if kind == "super_tb10":
        p = p_tiebreak(pa, pb, a_first, 10)
        return {(1, 0): p, (0, 1): 1 - p}
    ha, hb = p_game(pa), p_game(pb)
    memo: dict = {}

    def go(a: int, b: int) -> dict:
        if (a, b) in memo:
            return memo[(a, b)]
        if (a >= 6 and a - b >= 2) or (a == 7 and b == 5) or (b >= 6 and b - a >= 2) or (b == 7 and a == 5):
            res = {(a, b): 1.0}
        elif kind == "standard_tb" and a == 6 and b == 6:
            p = p_tiebreak(pa, pb, a_first, 7)
            res = {(7, 6): p, (6, 7): 1 - p}
        elif a + b >= 60:
            res = {(a, b): 1.0}
        else:
            a_serves = a_first if (a + b) % 2 == 0 else not a_first
            pw = ha if a_serves else 1 - hb
            res = {}
            for k, w in go(a + 1, b).items():
                res[k] = res.get(k, 0.0) + pw * w
            for k, w in go(a, b + 1).items():
                res[k] = res.get(k, 0.0) + (1 - pw) * w
        memo[(a, b)] = res
        return res

    out = go(0, 0)
    t = sum(out.values())
    return {k: v / t for k, v in out.items()}


def _match(pa: float, pb: float, best_of: int, a_first: bool, final_set: str) -> dict:
    need = (best_of + 1) // 2
    frontier = {(0, 0, a_first): {(0, 0): 1.0}}
    won_a, won_b, sets = {}, {}, {}
    while frontier:
        nxt: dict = {}
        for (sa, sb, fa), games in frontier.items():
            kind = final_set if (sa == need - 1 and sb == need - 1) else "standard_tb"
            for (ga, gb), ws in set_pmf(pa, pb, fa, kind).items():
                nfa = (not fa) if (ga + gb) % 2 == 1 else fa
                a_won = ga > gb
                new = (sa + a_won, sb + (not a_won), nfa)
                bucket = (won_a if new[0] == need else won_b if new[1] == need else nxt).setdefault(new, {})
                for (xa, xb), w in games.items():
                    bucket[(xa + ga, xb + gb)] = bucket.get((xa + ga, xb + gb), 0.0) + w * ws
                if new[0] == need or new[1] == need:
                    sets[new[:2]] = sets.get(new[:2], 0.0) + sum(games.values()) * ws
        frontier = nxt
    pmf: dict = {}
    for table in (won_a, won_b):
        for games in table.values():
            for k, w in games.items():
                pmf[k] = pmf.get(k, 0.0) + w
    total = sum(pmf.values())
    top = max(max(k) for k in pmf) + 1
    grid = np.zeros((top, top))
    for (a, b), w in pmf.items():
        grid[a, b] = w / total
    return dict(p_a=sum(sum(g.values()) for g in won_a.values()) / total, sets={k: v / total for k, v in sets.items()}, grid=grid)


def tennis_match(pa: float, pb: float, lines, *, best_of: int = 3, final_set: str = "standard_tb", sigma: float = 0.0,
                 a_first: bool = True, nodes: int = 15) -> dict:
    """Exact match from each player's point-win probability on own serve; ``sigma`` integrates a match-level form shock
    (Gauss-Hermite, no Monte Carlo). Game totals and handicaps count a tie-break as one game. ``set_handicap`` rows read the
    exact set-score distribution."""
    if best_of not in (3, 5):
        raise KitError("best_of is 3 or 5")
    if sigma == 0:
        res = [(1.0, _match(pa, pb, best_of, a_first, final_set))]
    else:
        x, w = np.polynomial.hermite_e.hermegauss(nodes)
        w = w / w.sum()
        lg, ex = (lambda p: math.log(p / (1 - p))), (lambda v: 1 / (1 + math.exp(-v)))
        res = [(float(wt), _match(ex(lg(pa) + sigma * z), ex(lg(pb) - sigma * z), best_of, a_first, final_set)) for z, wt in zip(x, w)]
    size = max(r["grid"].shape[0] for _, r in res)
    grid = np.zeros((size, size))
    sets: dict = {}
    for wt, r in res:
        grid[: r["grid"].shape[0], : r["grid"].shape[1]] += wt * r["grid"]
        for k, v in r["sets"].items():
            sets[k] = sets.get(k, 0.0) + wt * v
    g = Grid(grid / grid.sum())
    p_a = sum(wt * r["p_a"] for wt, r in res)
    rows = []
    for ln in lines:
        fam, side = ln["family"], ln["side"].upper()
        if fam == "winner":
            w_ = p_a if side in ("HOME", "A") else 1 - p_a
            rows.append(dict(label=ln["label"], family=fam, side=side, line="", w=w_, p=0.0, l=1 - w_, final_p=w_))
        elif fam == "set_handicap":
            line = float(ln["line"])
            win = sum(p for (sa, sb), p in sets.items() if ((sa - sb) if side in ("HOME", "A") else (sb - sa)) + line > 0)
            push = sum(p for (sa, sb), p in sets.items() if ((sa - sb) if side in ("HOME", "A") else (sb - sa)) + line == 0)
            rows.append(dict(label=ln["label"], family=fam, side=side, line=line, w=win, p=push, l=1 - win - push,
                             final_p=win / (1 - push) if push < 1 else float("nan")))
        else:
            side_g = {"A": "HOME", "B": "AWAY"}.get(side, side)
            rows += price(g, [dict(ln, side=side_g)])
    return dict(grid=g, p_a=p_a, sets=sets, rows=rows)


def barnett_clarke(spw_a: float, rpw_a: float, spw_b: float, rpw_b: float, tour_spw: float) -> tuple[float, float]:
    """Each player's point-win probability on own serve against this opponent (Barnett & Clarke 2005): own serve points won
    above the tour average, minus the opponent's return points won above the tour average."""
    tour_rpw = 1 - tour_spw
    pa = tour_spw + (spw_a - tour_spw) - (rpw_b - tour_rpw)
    pb = tour_spw + (spw_b - tour_spw) - (rpw_a - tour_rpw)
    if not (0.3 < pa < 0.9 and 0.3 < pb < 0.9):
        raise KitError(f"implausible serve probabilities {pa:.3f}, {pb:.3f}: check the inputs")
    return pa, pb


# ====================================================================== cricket (simulation)
OUTCOMES = ("0", "1", "2", "3", "4", "6", "W", "X")
OUTCOME_RUNS = np.array([0, 1, 2, 3, 4, 6, 0, 1])


def load_phases(path, group: str, innings: int) -> np.ndarray:
    """Per-over outcome probabilities (rows = overs) for a competition group and innings, from KIT_CRICKET_PHASES."""
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            if r.get("kit_version") != KIT_VERSION:
                raise KitError("cricket phase file version differs from the kit")
            if r["group"] == group and int(r["innings"]) == innings:
                rows.append((int(r["over"]), [float(r["p_" + o]) for o in OUTCOMES]))
    if not rows:
        raise KitError(f"no phase rows for {group} innings {innings}")
    rows.sort()
    table = np.array([p for _, p in rows])
    return table / table.sum(axis=1, keepdims=True)


def cricket_innings(table: np.ndarray, lines, *, n: int = CARD_MIN_N, seed: int = 20261111, run_scale: float = 1.0,
                    wicket_scale: float = 1.0, target: int | None = None, scale_sd: float = 0.0, card: bool = True,
                    keep_samples: bool = False) -> dict:
    """``n`` innings ball by ball from the per-over table (one row per over; outcomes 0,1,2,3,4,6,W,X where X is a wide or
    no-ball: one run, not a legal ball). ``run_scale`` multiplies the scoring outcomes (team and venue strength, from the
    card's centre), ``wicket_scale`` the wicket rate. ``target`` makes it a chase that stops at the winning run.
    ``scale_sd`` is the innings-level shock (pitch, conditions, form): each simulated innings draws its own scoring multiplier
    exp(N(0, scale_sd^2) - scale_sd^2/2); ball-by-ball outcomes alone are far too narrow (SIM-VALID-v1). Use the group's
    fitted value from the parameter file.
    Lines: innings_total (runs at the end of the innings) or checkpoint_total with ``over`` (runs after that many overs;
    an innings that ended earlier keeps its final score)."""
    if int(n) != n or n < 1 or (card and n < CARD_MIN_N):
        raise KitError(f"N must be at least {CARD_MIN_N} for a card")
    g = np.random.default_rng(int(seed))
    overs = table.shape[0]
    shock = np.exp(g.normal(0.0, scale_sd, n) - scale_sd ** 2 / 2) if scale_sd > 0 else np.ones(n)
    base = np.repeat(table[None, :, :], 1, axis=0)[0].copy()
    base[:, 6] *= wicket_scale
    checkpoints = sorted({int(ln["over"]) for ln in lines if ln["family"] == "checkpoint_total"})
    runs = np.zeros(n, np.int32)
    wk = np.zeros(n, np.int16)
    legal = np.zeros(n, np.int32)
    marks = {c: np.full(n, -1, np.int32) for c in checkpoints}
    active = np.ones(n, bool)
    for _ in range(overs * 6 * 2 + 40):
        if not active.any():
            break
        idx = np.flatnonzero(active)
        over = np.minimum(legal[idx] // 6, overs - 1)
        w = base[over].copy()
        w[:, 1:6] *= (run_scale * shock[idx])[:, None]
        cum = np.cumsum(w / w.sum(axis=1, keepdims=True), axis=1)
        u = g.random(idx.size)
        o = (u[:, None] > cum).sum(axis=1).clip(max=7)
        runs[idx] += OUTCOME_RUNS[o]
        wk[idx] += (o == 6)
        legal[idx] += (o != 7)
        for c in checkpoints:
            hit = (legal[idx] == c * 6) & (marks[c][idx] < 0)
            marks[c][idx[hit]] = runs[idx[hit]]
        done = (wk[idx] >= 10) | (legal[idx] >= overs * 6)
        if target is not None:
            done |= runs[idx] >= target
        active[idx[done]] = False
    for c in checkpoints:                   # ended before the checkpoint: the final score counts there
        miss = marks[c] < 0
        marks[c][miss] = runs[miss]
    rows = []
    for ln in lines:
        x = runs if ln["family"] == "innings_total" else marks[int(ln["over"])]
        line, side = float(ln["line"]), ln["side"].upper()
        w = float(((x > line) if side == "OVER" else (x < line)).mean())
        p = float((x == line).mean())
        l = 1 - w - p
        fp = w / (w + l) if w + l > 0 else float("nan")
        se = math.sqrt(fp * (1 - fp) / (n * (w + l))) if w + l > 0 else float("nan")
        rows.append(dict(label=ln["label"], family=ln["family"], side=side, line=line, w=w, p=p, l=l, final_p=fp, mc_se=se))
    out = dict(rows=rows, n=n, seed=seed, mean=float(runs.mean()), sd=float(runs.std()), all_out=float((wk >= 10).mean()))
    if keep_samples:                     # for validation only; a receipt never carries samples
        out.update(runs=runs, checkpoints=marks)
    return out


# ====================================================================== receipt
def file_sha256(path=None) -> str:
    path = Path(path or __file__)
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def receipt_sha256(text: str) -> str:
    """The hash a LANE_RETURN probability row cites: SHA-256 of the printed receipt text (line endings normalised)."""
    return hashlib.sha256(text.replace("\r\n", "\n").strip().encode("utf-8")).hexdigest()


def _fmt(v) -> str:
    if isinstance(v, float):
        return repr(round(v, 12))
    return str(v)


def receipt(engine: str, inputs: dict, result: dict, *, params_sha256: str = "", phases_sha256: str = "") -> str:
    """The text block a chat pastes back. The repository re-runs ``engine`` with ``inputs`` and must reproduce the rows."""
    lines = [f"<!-- BEGIN KIT_RECEIPT {engine} -->", f"kit_version: {KIT_VERSION}", f"kit_sha256: {file_sha256()}",
             f"params_sha256: {params_sha256 or 'NOT_USED'}", f"phases_sha256: {phases_sha256 or 'NOT_USED'}", f"engine: {engine}"]
    lines += [f"purpose: {inputs.get('purpose', 'PRIMARY')}", f"parameter_basis: {result.get('parameter_basis', 'CALLER_INPUTS')}",
              f"qualification: {result.get('qualification', 'MATHEMATICAL_ARITHMETIC_NOT_CALIBRATION')}"]
    for k in sorted(inputs):
        lines.append(f"input.{k}: {_fmt(inputs[k]) if not isinstance(inputs[k], (list, dict)) else repr(inputs[k])}")
    if "n" in result:
        lines += [f"sim.n: {result['n']}", f"sim.seed: {result['seed']}"]
    lines.append("rows:")
    lines.append("label,family,side,line,w,p,l,final_p" + (",mc_se" if any("mc_se" in r for r in result["rows"]) else ""))
    for r in result["rows"]:
        vals = [r["label"], r["family"], r["side"], _fmt(r["line"]), *(f"{r[k]:.10f}" for k in ("w", "p", "l", "final_p"))]
        if "mc_se" in r:
            vals.append(f"{r['mc_se']:.10f}")
        import csv, io
        buf = io.StringIO(newline="")
        csv.writer(buf, lineterminator="").writerow(vals)
        lines.append(buf.getvalue())
    lines.append(f"<!-- END KIT_RECEIPT {engine} -->")
    return "\n".join(lines)


ENGINES = ("points_from_centre", "soccer_from_means", "hockey_from_means", "baseball_from_means", "tennis_match", "cricket_innings")


def run(engine: str, inputs: dict, *, params_path=None, phases_path=None) -> tuple[dict, str]:
    """Run one engine and return (result, receipt). Use this, not the engine directly, so that the receipt records exactly
    the inputs used. ``inputs`` holds plain values only: numbers, strings, booleans and the ``lines`` list of dicts.
    ``competition`` selects the parameter row (points, soccer, hockey, baseball); ``group`` and ``innings`` select the
    cricket phase table."""
    if engine not in ENGINES:
        raise KitError(f"engine must be one of {ENGINES}")
    purpose = inputs.get("purpose", "PRIMARY")
    if purpose not in ("PRIMARY", "SENSITIVITY"):
        raise KitError("purpose must be PRIMARY or SENSITIVITY")
    if purpose == "PRIMARY" and (engine == "cricket_innings" or (engine == "tennis_match" and float(inputs.get("sigma", 0)) > 0)):
        raise KitError("NOT_VALIDATED: cricket simulation and tennis form shock are SENSITIVITY only; primary admission needs an exact-scope validation release")
    args = {k: v for k, v in inputs.items() if k not in ("competition", "lines", "group", "innings", "purpose")}
    lines = inputs["lines"]
    if not lines or len({r.get("label") for r in lines}) != len(lines) or any(not r.get("label") for r in lines):
        raise KitError("run needs nonempty unique contract labels")
    sides = {"winner": ("HOME", "AWAY", "DRAW", "A", "B"), "regulation_winner": ("HOME", "AWAY", "DRAW"),
             "handicap": ("HOME", "AWAY"), "set_handicap": ("HOME", "AWAY", "A", "B")}
    for ln in lines:
        family, side = ln.get("family"), str(ln.get("side", "")).upper()
        if family not in FAMILIES or side not in sides.get(family, ("OVER", "UNDER")):
            raise KitError("undefined contract family or side")
        if family not in ("winner", "regulation_winner"):
            try:
                if not math.isfinite(float(ln.get("line"))): raise ValueError()
            except (TypeError, ValueError): raise KitError("contract line must be finite") from None
    params_sha = phases_sha = ""
    if engine in ("points_from_centre", "soccer_from_means", "hockey_from_means", "baseball_from_means"):
        if params_path is None:
            raise KitError("this engine needs params_path (KIT_PARAMETERS file of this kit version)")
        params_sha = file_sha256(params_path)
        r = row(load_params(params_path), inputs["competition"])
        fn = {"points_from_centre": points_from_centre, "soccer_from_means": soccer_from_means, "hockey_from_means": hockey_from_means,
              "baseball_from_means": baseball_from_means}[engine]
        positional = {"points_from_centre": ("total", "margin"), "soccer_from_means": ("lam_home", "lam_away"),
                      "hockey_from_means": ("lam_home", "lam_away"), "baseball_from_means": ("mu_home", "mu_away")}[engine]
        result = fn(r, *(args.pop(k) for k in positional), lines, **args)
        result.update(parameter_basis=r.get("note", r["competition"]), qualification=r.get("admission_status", "REFERENCE_ARITHMETIC_UNCALIBRATED"))
    elif engine == "tennis_match":
        result = tennis_match(args.pop("pa"), args.pop("pb"), lines, **args)
    else:
        if phases_path is None:
            raise KitError("cricket needs phases_path (KIT_CRICKET_PHASES file of this kit version)")
        phases_sha = file_sha256(phases_path)
        result = cricket_innings(load_phases(phases_path, inputs["group"], int(inputs["innings"])), lines, **args)
    for r in result["rows"]:
        if not all(math.isfinite(r[k]) and 0 <= r[k] <= 1 for k in ("w", "p", "l", "final_p")) or abs(r["w"] + r["p"] + r["l"] - 1) > 1e-8:
            raise KitError("undefined/nonfinite output probability; retain a nonnumeric contract disposition")
    return result, receipt(engine, inputs, result, params_sha256=params_sha, phases_sha256=phases_sha)
