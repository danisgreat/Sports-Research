#!/usr/bin/env python3
"""Numerical A0/A1 models for every sport — C-SPORT-SHADOW (added 2026-09-26).

Why. The 2026-09-26 review found that the numerical programme (NUMERICAL_PROGRAM.md) existed only in
Markdown, and the user asked for a model for every sport, not only MLB. This file is the shared engine.
tools/mlb_model.py remains the MLB build (it adds probable starters); every other sport is here.

What each sport gets. A0 is the leak-free population baseline for the competition (what a card must
beat). A1 is a reduced-feature, interpretable challenger: team (or player) strength partially pooled
toward the league, with a sport-native score distribution. Neither reads odds, lines as predictive
inputs, prices, tipsters or any market material (MODEL_IMPLEMENTATION_RECIPES.md §2026-09-19(c)):
contract lines are only the thresholds that the frozen distribution is queried at.

  family    sports                              A1 distribution
  goals     soccer                              Poisson attack/defence ratings (Gamma-pooled, time-decayed),
                                                linked first-half/second-half split; A0 = league goal rates
  hockey    ice hockey                          regulation Poisson ratings + overtime/shootout resolution
                                                (race of scoring rates, then a coin flip); A0 = league rates
  points    basketball, American football,      ridge offence/defence ratings (time-decayed) with a
            AFL, rugby league, rugby union      discretised normal margin reshaped by the league's own
                                                key-number weights; widths from out-of-sample residuals
  baseball  NPB, KBO, CPBL (MLB: mlb_model.py)  shared-environment Gamma-Poisson joint (mlb_model) with
                                                the competition's tie rate where ties are allowed
  tennis    ATP, WTA                            surface-blended Elo -> serve/return point probabilities ->
                                                exact point/game/set/match Markov chain; A0 = overall Elo
                                                and the empirical total-games distribution
  cricket   limited-overs (T20, ODI, leagues)   Elo for the result; ridge batting/bowling/venue model for
                                                the first-innings total; A0 = 0.5 and the format's totals

Status. DECLARED PRIORS, NOT PROMOTED. Every constant below was declared before any validation run.
research/sport_models_2026-09-26/ holds the rolling-origin comparisons on the public results data
that could be reached; the result is recorded whichever way it went. Outputs are LEARNING_ONLY and
are never a card input (C-SPORT-SHADOW). A card may not cite a model probability.

Usage:
  python tools/sport_models.py leagues
  python tools/sport_models.py predict --league epl --home Arsenal --away Chelsea --date 2026-09-27 --total 2.5 --line -0.5
  python tools/sport_models.py predict --league atp --p1 "Jannik Sinner" --p2 "Carlos Alcaraz" --surface Hard --best-of 3 \\
      --date 2026-09-27 --total 22.5 --tml-dir DIR
  python tools/sport_models.py shadow --league nba --event 401234567 --card P-600 --total 221.5 --line -4.5
  python tools/sport_models.py settle
  python tools/sport_models.py score
  python tools/sport_models.py validate --league nfl --from 2025-09-01 --to 2026-02-15
  Any league can read results from a CSV instead of the network: --csv FILE with columns
  date,home,away,home_score,away_score[,neutral][,home_ht,away_ht][,finish][,venue][,season][,event_id]
  (finish: REG, OT or SO). Cricket reads a directory of cricsheet JSON files: --cricsheet DIR.

Standard library only. Network (predict/shadow/settle/validate without --csv): ESPN site API through
tools/sport_data.py, cached under .cache/sport_models/. LEARNING_ONLY.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import math
import random
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))
import mlb_model as mm  # noqa: E402  (shared-gamma joint, baseball ratings)

MODEL_VERSION = "SPORT-A1-shadow/2026-09-26"
SHADOW_DIR = REPO / "research" / "sport_shadow"

# --------------------------------------------------------------------------- declared constants
# Declared on 2026-09-26 before any validation run (NUMERICAL_PROGRAM §2: "Parameters/priors are
# explicit inputs; no default is described as fitted"). Units: kappa in goals, lam in games,
# half_life/window/resid_days in days, sd0 in points.

FAMILY_DEFAULTS = {
    "goals": {"kappa": 4.0, "home_prec": 50.0, "half_life": 365, "window": 730, "min_games": 40,
              "phase_kappa": 40.0, "h1_share_prior": 0.44, "h1_share_strength": 200.0, "draws": True},
    "hockey": {"kappa": 12.0, "home_prec": 50.0, "half_life": 180, "window": 540, "min_games": 60,
               "ot_decided_prior": 0.62, "ot_prior_strength": 50.0, "draws": False},
    "points": {"lam": 4.0, "lam_home": 1.0, "half_life": 300, "window": 800, "min_games": 40,
               "resid_days": 400, "resid_keep": 400, "sd_prior_n": 20.0, "shape_smooth": 5.0,
               "shape_min_games": 200, "shape_bounds": [0.25, 3.0], "draws": True, "key_numbers": False,
               "key_max": 20},
    "baseball": {"tie_prior": 0.02, "tie_prior_strength": 100.0, "min_games": 100, "draws": True},
    "tennis": {"k_num": 250.0, "k_offset": 5.0, "k_exp": 0.4, "init": 1500.0, "surface_blend": 0.5,
               "serve_prior": {"Hard": 0.64, "Clay": 0.62, "Grass": 0.67, "Carpet": 0.65},
               "serve_window_days": 730, "min_matches": 5, "games_window_days": 730},
    "cricket": {"elo_k": 24.0, "elo_init": 1500.0, "lam_team": 6.0, "lam_venue": 10.0, "half_life": 365,
                "window": 1095, "resid_keep": 300, "sd_prior_n": 20.0, "min_innings": 30},
}

# ESPN paths are the site-API sport/league paths used by team_baseline.py and slate_universe.py.
LEAGUES = {
    # soccer
    "epl": {"sport": "soccer", "family": "goals", "espn": "soccer/eng.1"},
    "championship": {"sport": "soccer", "family": "goals", "espn": "soccer/eng.2"},
    "laliga": {"sport": "soccer", "family": "goals", "espn": "soccer/esp.1"},
    "bundesliga": {"sport": "soccer", "family": "goals", "espn": "soccer/ger.1"},
    "seriea": {"sport": "soccer", "family": "goals", "espn": "soccer/ita.1"},
    "ligue1": {"sport": "soccer", "family": "goals", "espn": "soccer/fra.1"},
    "eredivisie": {"sport": "soccer", "family": "goals", "espn": "soccer/ned.1"},
    "primeira": {"sport": "soccer", "family": "goals", "espn": "soccer/por.1"},
    "spl": {"sport": "soccer", "family": "goals", "espn": "soccer/sco.1"},
    "aleague": {"sport": "soccer", "family": "goals", "espn": "soccer/aus.1"},
    "mls": {"sport": "soccer", "family": "goals", "espn": "soccer/usa.1"},
    "jleague": {"sport": "soccer", "family": "goals", "espn": "soccer/jpn.1"},
    "ucl": {"sport": "soccer", "family": "goals", "espn": "soccer/uefa.champions"},
    "uel": {"sport": "soccer", "family": "goals", "espn": "soccer/uefa.europa"},
    # ice hockey
    "nhl": {"sport": "ice-hockey", "family": "hockey", "espn": "hockey/nhl"},
    # basketball (no draws: overtime decides every game)
    "nba": {"sport": "basketball", "family": "points", "espn": "basketball/nba", "lam": 6.0, "half_life": 120,
            "window": 540, "resid_days": 150, "sd0_margin": 15.1, "sd0_total": 19.4, "draws": False},
    "wnba": {"sport": "basketball", "family": "points", "espn": "basketball/wnba", "lam": 5.0, "half_life": 120,
             "window": 540, "resid_days": 150, "sd0_margin": 13.3, "sd0_total": 19.5, "draws": False},
    "nbl": {"sport": "basketball", "family": "points", "espn": "basketball/nbl", "lam": 5.0, "half_life": 150,
            "window": 540, "resid_days": 200, "sd0_margin": 15.2, "sd0_total": 18.7, "draws": False},
    # American football
    "nfl": {"sport": "american-football", "family": "points", "espn": "football/nfl", "lam": 3.0,
            "sd0_margin": 13.6, "sd0_total": 13.4, "key_numbers": True, "key_max": 24},
    "ncaaf": {"sport": "american-football", "family": "points", "espn": "football/college-football", "lam": 3.0,
              "sd0_margin": 17.0, "sd0_total": 16.0, "key_numbers": True, "key_max": 24, "draws": False},
    # Australian football
    "afl": {"sport": "afl", "family": "points", "espn": "australian-football/afl",
            "sd0_margin": 36.8, "sd0_total": 29.1},
    # rugby league
    "nrl": {"sport": "rugby-league", "family": "points", "espn": "rugby-league/3",
            "sd0_margin": 19.9, "sd0_total": 13.9, "key_numbers": True},
    # rugby union: ESPN paths vary by competition; pass --espn-path or --csv
    "union": {"sport": "rugby-union", "family": "points", "espn": None,
              "sd0_margin": 16.0, "sd0_total": 14.0, "key_numbers": True},
    # baseball outside MLB (ties allowed after the extra-inning limit); MLB uses tools/mlb_model.py
    "npb": {"sport": "baseball", "family": "baseball", "espn": None, "ties": True},
    "kbo": {"sport": "baseball", "family": "baseball", "espn": None, "ties": True},
    "cpbl": {"sport": "baseball", "family": "baseball", "espn": None, "ties": True},
    "mlb-teamonly": {"sport": "baseball", "family": "baseball", "espn": None, "ties": False, "draws": False},
    # tennis
    "atp": {"sport": "tennis", "family": "tennis", "espn": "tennis/atp"},
    "wta": {"sport": "tennis", "family": "tennis", "espn": "tennis/wta"},
    # cricket (limited overs; cricsheet JSON)
    "t20": {"sport": "cricket", "family": "cricket", "overs": 20, "sd0_total": 30.0},
    "odi": {"sport": "cricket", "family": "cricket", "overs": 50, "sd0_total": 45.0},
}


def config(league: str) -> dict:
    if league not in LEAGUES:
        raise SystemExit(f"error: unknown league {league!r}; run `python tools/sport_models.py leagues`")
    cfg = dict(FAMILY_DEFAULTS[LEAGUES[league]["family"]])
    cfg.update(LEAGUES[league])
    cfg["league"] = league
    return cfg


def params_sha(cfg: dict) -> str:
    blob = json.dumps({k: v for k, v in sorted(cfg.items()) if k != "espn"}, sort_keys=True, default=str)
    return hashlib.sha256((MODEL_VERSION + blob).encode()).hexdigest()[:16]


# --------------------------------------------------------------------------- distributions

def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def normalise(pmf: dict) -> dict:
    s = math.fsum(pmf.values())
    if s <= 0:
        raise ValueError("empty distribution")
    return {k: v / s for k, v in pmf.items() if v > 0}


def poisson_vec(lam: float, tail: float = 1e-10) -> list[float]:
    lam = max(lam, 1e-9)
    kmax = int(lam + 12 * math.sqrt(lam) + 12)
    out = [math.exp(-lam + k * math.log(lam) - math.lgamma(k + 1)) for k in range(kmax + 1)]
    if 1.0 - math.fsum(out) > tail:
        raise ValueError(f"poisson support too small for mean {lam}")
    return out


def indep_joint(mu_h: float, mu_a: float) -> dict:
    ph, pa = poisson_vec(mu_h), poisson_vec(mu_a)
    return {(h, a): x * y for h, x in enumerate(ph) for a, y in enumerate(pa) if x * y > 1e-14}


def disc_normal(mu: float, sd: float, weight=None, floor0: bool = False) -> dict:
    """Integer PMF from a normal, optionally reshaped by weight(|k|) (key numbers; w(0)=0 forbids a tie)."""
    sd = max(sd, 1e-6)
    lo, hi = math.floor(mu - 8 * sd), math.ceil(mu + 8 * sd)
    if floor0:
        lo = max(lo, 0)
    pmf = {}
    for k in range(lo, hi + 1):
        p = normal_cdf((k + 0.5 - mu) / sd) - normal_cdf((k - 0.5 - mu) / sd)
        if weight is not None:
            p *= weight(abs(k))
        if p > 0:
            pmf[k] = p
    return normalise(pmf)


def marginals(joint: dict) -> tuple[dict, dict, dict, dict]:
    mar, tot, hm, aw = defaultdict(float), defaultdict(float), defaultdict(float), defaultdict(float)
    for (h, a), p in joint.items():
        mar[h - a] += p
        tot[h + a] += p
        hm[h] += p
        aw[a] += p
    return dict(mar), dict(tot), dict(hm), dict(aw)


def pmf_mean(pmf: dict) -> float:
    return math.fsum(k * p for k, p in pmf.items())


def p_gt(pmf: dict, x: float) -> float:
    return math.fsum(p for k, p in pmf.items() if k > x + 1e-9)


def p_eq(pmf: dict, x: float) -> float:
    return pmf.get(int(round(x)), 0.0) if abs(x - round(x)) < 1e-9 else 0.0


def rps(pmf: dict, y: int) -> float:
    """Ranked probability score on the integers (discrete CRPS). Lower is better."""
    ks = sorted(pmf)
    lo, hi = min(ks[0], y), max(ks[-1], y)
    cum, s = 0.0, 0.0
    for k in range(lo, hi + 1):
        cum += pmf.get(k, 0.0)
        s += (cum - (1.0 if y <= k else 0.0)) ** 2
    return s


class Forecast:
    """A frozen predictive distribution for one event. margin = home − away at the contract's endpoint."""

    def __init__(self, margin: dict, total: dict, home: dict | None = None, away: dict | None = None,
                 joint: dict | None = None, extra: dict | None = None, meta: dict | None = None):
        self.margin, self.total, self.home, self.away = margin, total, home, away
        self.joint, self.extra, self.meta = joint, extra or {}, meta or {}

    @classmethod
    def from_joint(cls, joint: dict, extra=None, meta=None) -> "Forecast":
        mar, tot, hm, aw = marginals(joint)
        return cls(mar, tot, hm, aw, joint, extra, meta)

    def probs(self, total: float | None = None, line: float | None = None, home_total: float | None = None,
              away_total: float | None = None) -> dict:
        m = self.margin
        out = {"p_home_win": p_gt(m, 0), "p_draw": m.get(0, 0.0), "p_away_win": math.fsum(p for k, p in m.items() if k < 0),
               "mean_margin": pmf_mean(m), "mean_total": pmf_mean(self.total)}
        if total is not None:
            out.update({"p_over": p_gt(self.total, total), "p_push": p_eq(self.total, total)})
            out["p_under"] = max(0.0, 1.0 - out["p_over"] - out["p_push"])
        if line is not None:  # the home side's handicap: home covers when margin + line > 0
            out.update({"p_home_cover": p_gt(m, -line), "p_line_push": p_eq(m, -line)})
            out["p_away_cover"] = max(0.0, 1.0 - out["p_home_cover"] - out["p_line_push"])
        for side, x in (("home", home_total), ("away", away_total)):
            pmf = self.home if side == "home" else self.away
            if x is not None and pmf is not None:
                out[f"p_{side}_over"] = p_gt(pmf, x)
                out[f"p_{side}_push"] = p_eq(pmf, x)
        if self.joint is not None:
            out["p_btts"] = math.fsum(p for (h, a), p in self.joint.items() if h > 0 and a > 0)
        for key, sub in self.extra.items():
            if isinstance(sub, Forecast):
                out[f"{key}_p_home_win"] = p_gt(sub.margin, 0)
                out[f"{key}_p_draw"] = sub.margin.get(0, 0.0)
                out[f"{key}_mean_total"] = pmf_mean(sub.total)
        return out


# --------------------------------------------------------------------------- shared helpers

def to_date(s: str) -> dt.date:
    return dt.date.fromisoformat(str(s)[:10])


def decay(age_days: float, half_life: float) -> float:
    return 0.5 ** (max(age_days, 0.0) / half_life)


def weighted_rows(games: list[dict], asof: str, cfg: dict) -> list[tuple]:
    """(weight, game) for games strictly before `asof` inside the window, newest weighted most."""
    d0 = to_date(asof)
    out = []
    for g in games:
        age = (d0 - to_date(g["date"])).days
        if 0 < age <= cfg["window"]:
            out.append((decay(age, cfg["half_life"]), g))
    return out


# --------------------------------------------------------------------------- goals / hockey ratings

class PoissonRatings:
    """Multiplicative Poisson attack/defence model: mu_home = b·h·A_i·D_j, mu_away = b·A_j·D_i / h
    (h = 1 at a neutral venue). A and D have Gamma(kappa, kappa) priors (kappa in goals); log h has a
    normal prior of precision home_prec. Fitted by weighted coordinate ascent; time-decayed weights."""

    def __init__(self, rows: list[tuple], kappa: float, home_prec: float, init: "PoissonRatings | None" = None,
                 iters: int = 200, tol: float = 1e-7):
        # rows: (w, home, away, goals_home, goals_away, neutral)
        self.kappa, self.home_prec = kappa, home_prec
        teams = {r[1] for r in rows} | {r[2] for r in rows}
        wsum = math.fsum(r[0] for r in rows)
        self.b = math.fsum(r[0] * (r[3] + r[4]) for r in rows) / (2 * wsum) if wsum else 1.0
        self.lh = 0.0
        self.A = {t: 1.0 for t in teams}
        self.D = {t: 1.0 for t in teams}
        if init is not None:
            self.b, self.lh = init.b, init.lh
            for t in teams:
                self.A[t] = init.A.get(t, 1.0)
                self.D[t] = init.D.get(t, 1.0)
        self.b = max(self.b, 1e-3)
        for _ in range(iters):
            change = self._sweep(rows)
            if change < tol:
                break

    def _hf(self, neutral: bool) -> tuple[float, float]:
        return (1.0, 1.0) if neutral else (math.exp(self.lh), math.exp(-self.lh))

    def _sweep(self, rows) -> float:
        old = {**{("A", t): v for t, v in self.A.items()}, **{("D", t): v for t, v in self.D.items()}}
        num, den = defaultdict(float), defaultdict(float)
        for w, h, a, gh, ga, neu in rows:
            fh, fa = self._hf(neu)
            num[h] += w * gh
            den[h] += w * self.b * fh * self.D[a]
            num[a] += w * ga
            den[a] += w * self.b * fa * self.D[h]
        for t in self.A:
            self.A[t] = (num[t] + self.kappa) / (den[t] + self.kappa)
        num, den = defaultdict(float), defaultdict(float)
        for w, h, a, gh, ga, neu in rows:
            fh, fa = self._hf(neu)
            num[a] += w * gh
            den[a] += w * self.b * fh * self.A[h]
            num[h] += w * ga
            den[h] += w * self.b * fa * self.A[a]
        for t in self.D:
            self.D[t] = (num[t] + self.kappa) / (den[t] + self.kappa)
        for par in (self.A, self.D):  # identifiability: geometric mean 1, folded into b
            if par:
                g = math.exp(sum(math.log(v) for v in par.values()) / len(par))
                for t in par:
                    par[t] /= g
                self.b *= g
        goals = expct = 0.0
        grad = hess = 0.0
        for w, h, a, gh, ga, neu in rows:
            fh, fa = self._hf(neu)
            mh = self.b * fh * self.A[h] * self.D[a]
            ma = self.b * fa * self.A[a] * self.D[h]
            goals += w * (gh + ga)
            expct += w * (mh + ma)
            if not neu:
                grad += w * ((gh - mh) - (ga - ma))
                hess += w * (mh + ma)
        if expct > 0:
            self.b *= goals / expct
        grad -= self.home_prec * self.lh
        hess += self.home_prec
        if hess > 0:
            self.lh += grad / hess
        new = {**{("A", t): v for t, v in self.A.items()}, **{("D", t): v for t, v in self.D.items()}}
        return max((abs(math.log(v / old[k])) for k, v in new.items()), default=0.0)

    def means(self, home: str, away: str, neutral: bool = False) -> tuple[float, float]:
        fh, fa = self._hf(neutral)
        return (self.b * fh * self.A.get(home, 1.0) * self.D.get(away, 1.0),
                self.b * fa * self.A.get(away, 1.0) * self.D.get(home, 1.0))


def dc_tau(h: int, a: int, lh: float, la: float, rho: float) -> float:
    if h == 0 and a == 0:
        return 1 - lh * la * rho
    if h == 0 and a == 1:
        return 1 + lh * rho
    if h == 1 and a == 0:
        return 1 + la * rho
    if h == 1 and a == 1:
        return 1 - rho
    return 1.0


def dixon_coles_joint(mu_h: float, mu_a: float, rho: float) -> dict:
    """Independent Poisson with the Dixon–Coles low-score factors (MODEL_IMPLEMENTATION_RECIPES §2).
    A negative factor is refused, never clipped."""
    j = indep_joint(mu_h, mu_a)
    for cell in ((0, 0), (0, 1), (1, 0), (1, 1)):
        f = dc_tau(cell[0], cell[1], mu_h, mu_a, rho)
        if f < 0:
            raise ValueError(f"Dixon-Coles factor negative at {cell} (rho {rho})")
        j[cell] = j.get(cell, 0.0) * f
    return normalise(j)


def estimate_rho(rows: list[tuple], rt: PoissonRatings, grid=None) -> float:
    """Training-window maximum-likelihood rho on a grid (a separate candidate build, never stacked by default)."""
    grid = grid or [x / 100 for x in range(-20, 11)]
    best, best_ll = 0.0, -float("inf")
    for rho in grid:
        ll = 0.0
        ok = True
        for w, h, a, gh, ga, neu in rows:
            if gh > 1 or ga > 1:
                continue
            mh, ma = rt.means(h, a, neu)
            t = dc_tau(gh, ga, mh, ma, rho)
            if t <= 0:
                ok = False
                break
            ll += w * math.log(t)
        if ok and ll > best_ll:
            best, best_ll = rho, ll
    return best


class GoalsModel:
    """Soccer. A1: Poisson ratings on full-time goals plus a partially pooled first-half share per team;
    the first half and the second half are independent Poisson periods, so one linked distribution supplies
    first-half, second-half and full-time contracts. A0: league home/away goal rates (and first-half shares)."""

    def __init__(self, games: list[dict], asof: str, cfg: dict, init: "GoalsModel | None" = None):
        self.cfg = cfg
        wr = weighted_rows(games, asof, cfg)
        self.n = len(wr)
        if self.n < cfg["min_games"]:
            raise ValueError(f"only {self.n} games in the window before {asof}")
        rows = [(w, g["home"], g["away"], g["hs"], g["as"], g.get("neutral", False)) for w, g in wr]
        self.rt = PoissonRatings(rows, cfg["kappa"], cfg["home_prec"], init.rt if init else None)
        # A0: league goal rates by venue role
        wh = [(w, g) for w, g in wr if not g.get("neutral")]
        sw = math.fsum(w for w, _ in wh) or 1.0
        self.a0_home = math.fsum(w * g["hs"] for w, g in wh) / sw
        self.a0_away = math.fsum(w * g["as"] for w, g in wh) / sw
        # first-half shares, partially pooled
        ht = [(w, g) for w, g in wr if g.get("hs_ht") is not None and g.get("as_ht") is not None]
        self.has_ht = len(ht) >= cfg["min_games"]
        k, s0 = cfg["h1_share_strength"], cfg["h1_share_prior"]
        self.s_home = (math.fsum(w * g["hs_ht"] for w, g in ht) + k * s0) / (math.fsum(w * g["hs"] for w, g in ht) + k)
        self.s_away = (math.fsum(w * g["as_ht"] for w, g in ht) + k * s0) / (math.fsum(w * g["as"] for w, g in ht) + k)
        num_a, den_a, num_d, den_d = (defaultdict(float) for _ in range(4))
        for w, g in ht:
            mh, ma = self.rt.means(g["home"], g["away"], g.get("neutral", False))
            num_a[g["home"]] += w * g["hs_ht"]
            den_a[g["home"]] += w * self.s_home * mh
            num_a[g["away"]] += w * g["as_ht"]
            den_a[g["away"]] += w * self.s_away * ma
            num_d[g["away"]] += w * g["hs_ht"]
            den_d[g["away"]] += w * self.s_home * mh
            num_d[g["home"]] += w * g["as_ht"]
            den_d[g["home"]] += w * self.s_away * ma
        kp = cfg["phase_kappa"]
        self.h1_att = {t: (num_a[t] + kp) / (den_a[t] + kp) for t in den_a}
        self.h1_def = {t: (num_d[t] + kp) / (den_d[t] + kp) for t in den_d}
        self.rows = rows

    def _phase(self, mu: float, share: float, att: float, dfn: float) -> float:
        return min(0.95 * mu, max(0.05 * mu, share * mu * att * dfn))

    def a1(self, home: str, away: str, neutral: bool = False, rho: float = 0.0) -> Forecast:
        mh, ma = self.rt.means(home, away, neutral)
        joint = dixon_coles_joint(mh, ma, rho) if rho else indep_joint(mh, ma)
        extra = {}
        if self.has_ht:
            h1h = self._phase(mh, self.s_home, self.h1_att.get(home, 1.0), self.h1_def.get(away, 1.0))
            h1a = self._phase(ma, self.s_away, self.h1_att.get(away, 1.0), self.h1_def.get(home, 1.0))
            extra["h1"] = Forecast.from_joint(indep_joint(h1h, h1a))
            extra["h2"] = Forecast.from_joint(indep_joint(mh - h1h, ma - h1a))
        return Forecast.from_joint(joint, extra, {"mu_home": mh, "mu_away": ma, "rho": rho})

    def a0(self, neutral: bool = False) -> Forecast:
        mh, ma = (self.a0_home, self.a0_away) if not neutral else ((self.a0_home + self.a0_away) / 2,) * 2
        extra = {}
        if self.has_ht:
            extra["h1"] = Forecast.from_joint(indep_joint(mh * self.s_home, ma * self.s_away))
            extra["h2"] = Forecast.from_joint(indep_joint(mh * (1 - self.s_home), ma * (1 - self.s_away)))
        return Forecast.from_joint(indep_joint(mh, ma), extra, {"mu_home": mh, "mu_away": ma})


class HockeyModel:
    """Ice hockey. Regulation goals are Poisson from team ratings; a regulation tie goes to overtime,
    decided in overtime with the league's rate (the home side wins OT in proportion to its scoring rate)
    and otherwise by shootout (0.5). The winner's final score gets +1 (NHL scoring of OT/SO wins).
    `margin`/`total` are the final (OT/SO included) route; extra['reg'] is the regulation three-way route."""

    def __init__(self, games: list[dict], asof: str, cfg: dict, init: "HockeyModel | None" = None):
        self.cfg = cfg
        wr = [(w, g) for w, g in weighted_rows(games, asof, cfg) if g.get("finish") in ("REG", "OT", "SO")]
        self.n = len(wr)
        if self.n < cfg["min_games"]:
            raise ValueError(f"only {self.n} games with a known finish before {asof}")
        rows = []
        for w, g in wr:
            rh, ra = reg_score(g)
            rows.append((w, g["home"], g["away"], rh, ra, g.get("neutral", False)))
        self.rt = PoissonRatings(rows, cfg["kappa"], cfg["home_prec"], init.rt if init else None)
        extra_games = [(w, g) for w, g in wr if g["finish"] in ("OT", "SO")]
        k, p0 = cfg["ot_prior_strength"], cfg["ot_decided_prior"]
        sw = math.fsum(w for w, _ in extra_games)
        self.p_ot_decided = (math.fsum(w for w, g in extra_games if g["finish"] == "OT") + k * p0) / (sw + k)
        self.p_home_extra = (math.fsum(w for w, g in extra_games if g["hs"] > g["as"]) + k * 0.5) / (sw + k)
        wh = [(w, h, a) for w, _, _, h, a, neu in rows if not neu]
        s = math.fsum(w for w, _, _ in wh) or 1.0
        self.a0_home = math.fsum(w * h for w, h, _ in wh) / s
        self.a0_away = math.fsum(w * a for w, _, a in wh) / s

    @staticmethod
    def _final(reg: dict, p_home_extra: float) -> dict:
        out = defaultdict(float)
        for (h, a), p in reg.items():
            if h != a:
                out[(h, a)] += p
            else:
                out[(h + 1, a)] += p * p_home_extra
                out[(h, a + 1)] += p * (1 - p_home_extra)
        return dict(out)

    def a1(self, home: str, away: str, neutral: bool = False) -> Forecast:
        mh, ma = self.rt.means(home, away, neutral)
        reg = indep_joint(mh, ma)
        p_home_extra = self.p_ot_decided * mh / (mh + ma) + (1 - self.p_ot_decided) * 0.5
        return Forecast.from_joint(self._final(reg, p_home_extra), {"reg": Forecast.from_joint(reg)},
                                   {"mu_home": mh, "mu_away": ma, "p_home_extra": p_home_extra})

    def a0(self, neutral: bool = False) -> Forecast:
        mh, ma = (self.a0_home, self.a0_away) if not neutral else ((self.a0_home + self.a0_away) / 2,) * 2
        reg = indep_joint(mh, ma)
        return Forecast.from_joint(self._final(reg, 0.5 if neutral else self.p_home_extra),
                                   {"reg": Forecast.from_joint(reg)}, {"mu_home": mh, "mu_away": ma})


def reg_score(g: dict) -> tuple[int, int]:
    """Regulation score of a hockey game: an OT/SO game was tied at the loser's final score."""
    if g.get("finish") in ("OT", "SO"):
        lo = min(g["hs"], g["as"])
        return lo, lo
    return g["hs"], g["as"]


# --------------------------------------------------------------------------- points family

class PointsRatings:
    """Ridge offence/defence model on points: home = mu + hfa/2 + o_h − d_a; away = mu − hfa/2 + o_a − d_h
    (hfa = 0 at a neutral venue; o = points scored above average, d = points kept out, so strength = o + d).
    o and d have ridge penalty lam (in games); weighted block coordinate descent."""

    def __init__(self, rows: list[tuple], lam: float, lam_home: float, init: "PointsRatings | None" = None,
                 sweeps: int = 300, tol: float = 1e-6):
        # rows: (w, home, away, pts_home, pts_away, neutral)
        teams = {r[1] for r in rows} | {r[2] for r in rows}
        wsum = math.fsum(r[0] for r in rows)
        self.mu = math.fsum(r[0] * (r[3] + r[4]) for r in rows) / (2 * wsum)
        self.hfa = 0.0
        self.o = {t: 0.0 for t in teams}
        self.d = {t: 0.0 for t in teams}
        if init is not None:
            self.mu, self.hfa = init.mu, init.hfa
            for t in teams:
                self.o[t], self.d[t] = init.o.get(t, 0.0), init.d.get(t, 0.0)
        for _ in range(sweeps):
            if self._sweep(rows, lam, lam_home) < tol:
                break

    def _sweep(self, rows, lam, lam_home) -> float:
        before = (self.mu, self.hfa, dict(self.o), dict(self.d))
        num, den = defaultdict(float), defaultdict(float)
        for w, h, a, ph, pa, neu in rows:
            c = 0.0 if neu else 0.5
            num[h] += w * (ph - self.mu - c * self.hfa + self.d[a])
            den[h] += w
            num[a] += w * (pa - self.mu + c * self.hfa + self.d[h])
            den[a] += w
        for t in self.o:
            self.o[t] = num[t] / (den[t] + lam)
        num, den = defaultdict(float), defaultdict(float)
        for w, h, a, ph, pa, neu in rows:
            c = 0.0 if neu else 0.5
            num[a] += w * (self.mu + c * self.hfa + self.o[h] - ph)
            den[a] += w
            num[h] += w * (self.mu - c * self.hfa + self.o[a] - pa)
            den[h] += w
        for t in self.d:
            self.d[t] = num[t] / (den[t] + lam)
        s = sw = 0.0
        for w, h, a, ph, pa, neu in rows:
            c = 0.0 if neu else 0.5
            s += w * (ph - c * self.hfa - self.o[h] + self.d[a]) + w * (pa + c * self.hfa - self.o[a] + self.d[h])
            sw += 2 * w
        self.mu = s / sw
        s = sw = 0.0
        for w, h, a, ph, pa, neu in rows:
            if neu:
                continue
            s += w * 0.5 * (ph - self.mu - self.o[h] + self.d[a]) - w * 0.5 * (pa - self.mu - self.o[a] + self.d[h])
            sw += w * 0.5
        self.hfa = s / (sw + lam_home)
        delta = max([abs(self.mu - before[0]), abs(self.hfa - before[1])] +
                    [abs(v - before[2][t]) for t, v in self.o.items()] + [abs(v - before[3][t]) for t, v in self.d.items()])
        return delta

    def means(self, home: str, away: str, neutral: bool = False) -> tuple[float, float]:
        c = 0.0 if neutral else 0.5
        return (self.mu + c * self.hfa + self.o.get(home, 0.0) - self.d.get(away, 0.0),
                self.mu - c * self.hfa + self.o.get(away, 0.0) - self.d.get(home, 0.0))


def shape_weights(margins: list[int], cfg: dict):
    """Key-number weights w(|m|) = (observed + a)/(expected under a smooth normal + a), from the window's
    own margins (population data). Returns None when the league has no key numbers or too few games; a
    no-draw league always gets w(0) = 0."""
    draws = cfg.get("draws", True)
    if not cfg.get("key_numbers") or len(margins) < cfg["shape_min_games"]:
        return None if draws else (lambda k: 0.0 if k == 0 else 1.0)
    n = len(margins)
    m = sum(margins) / n
    s = math.sqrt(sum((x - m) ** 2 for x in margins) / max(1, n - 1))
    kmax, a = cfg["key_max"], cfg["shape_smooth"]
    lo, hi = cfg["shape_bounds"]
    obs = defaultdict(int)
    for x in margins:
        obs[abs(int(x))] += 1
    w = {}
    for k in range(0, kmax + 1):
        if k == 0:
            e = n * (normal_cdf((0.5 - m) / s) - normal_cdf((-0.5 - m) / s))
        else:
            e = n * (normal_cdf((k + 0.5 - m) / s) - normal_cdf((k - 0.5 - m) / s)
                     + normal_cdf((-k + 0.5 - m) / s) - normal_cdf((-k - 0.5 - m) / s))
        w[k] = min(hi, max(lo, (obs[k] + a) / (e + a)))
    if not draws:
        w[0] = 0.0
    return lambda k: w.get(k, 1.0)


class ResidualBook:
    """Out-of-sample residuals of A1 predictions made before the forecast date (never in-sample)."""

    def __init__(self, keep: int):
        self.keep = keep
        self.margin, self.total, self.team = [], [], []

    def add(self, g: dict, mh: float, ma: float) -> None:
        self.margin.append((g["hs"] - g["as"]) - (mh - ma))
        self.total.append((g["hs"] + g["as"]) - (mh + ma))
        self.team += [g["hs"] - mh, g["as"] - ma]
        self.margin, self.total, self.team = self.margin[-self.keep:], self.total[-self.keep:], self.team[-2 * self.keep:]

    @staticmethod
    def blend(res: list[float], sd0: float, n0: float) -> float:
        ss = math.fsum(r * r for r in res)
        return math.sqrt((ss + n0 * sd0 * sd0) / (len(res) + n0))


class PointsModel:
    """Basketball, American football, AFL, rugby league, rugby union."""

    def __init__(self, games: list[dict], asof: str, cfg: dict, book: ResidualBook | None = None,
                 init: "PointsModel | None" = None):
        self.cfg = cfg
        wr = weighted_rows(games, asof, cfg)
        self.n = len(wr)
        if self.n < cfg["min_games"]:
            raise ValueError(f"only {self.n} games in the window before {asof}")
        rows = [(w, g["home"], g["away"], g["hs"], g["as"], g.get("neutral", False)) for w, g in wr]
        self.rt = PointsRatings(rows, cfg["lam"], cfg["lam_home"], init.rt if init else None)
        margins = [g["hs"] - g["as"] for _, g in wr]
        self.weight = shape_weights(margins, cfg)
        # A0: league margin and total, weighted
        sw = math.fsum(w for w, _ in wr)
        wh = [(w, g) for w, g in wr if not g.get("neutral")]
        swh = math.fsum(w for w, _ in wh) or 1.0
        self.a0_margin = math.fsum(w * (g["hs"] - g["as"]) for w, g in wh) / swh
        self.a0_total = math.fsum(w * (g["hs"] + g["as"]) for w, g in wr) / sw
        self.a0_sd_margin = math.sqrt(math.fsum(w * ((g["hs"] - g["as"]) - self.a0_margin) ** 2 for w, g in wr) / sw)
        self.a0_sd_total = math.sqrt(math.fsum(w * ((g["hs"] + g["as"]) - self.a0_total) ** 2 for w, g in wr) / sw)
        self.a0_sd_team = math.sqrt(math.fsum(w * ((g["hs"] - self.a0_total / 2) ** 2 + (g["as"] - self.a0_total / 2) ** 2)
                                              for w, g in wr) / (2 * sw))
        book = book or ResidualBook(cfg["resid_keep"])
        n0 = cfg["sd_prior_n"]
        self.sd_margin = ResidualBook.blend(book.margin, cfg.get("sd0_margin", self.a0_sd_margin), n0)
        self.sd_total = ResidualBook.blend(book.total, cfg.get("sd0_total", self.a0_sd_total), n0)
        self.sd_team = ResidualBook.blend(book.team, cfg.get("sd0_total", self.a0_sd_total) / math.sqrt(2), n0)
        self.n_resid = len(book.margin)

    def _fc(self, mh: float, ma: float, sdm: float, sdt: float, sdteam: float, meta: dict) -> Forecast:
        return Forecast(disc_normal(mh - ma, sdm, self.weight), disc_normal(mh + ma, sdt, floor0=True),
                        disc_normal(mh, sdteam, floor0=True), disc_normal(ma, sdteam, floor0=True), meta=meta)

    def a1(self, home: str, away: str, neutral: bool = False) -> Forecast:
        mh, ma = self.rt.means(home, away, neutral)
        return self._fc(mh, ma, self.sd_margin, self.sd_total, self.sd_team,
                        {"mu_home": mh, "mu_away": ma, "sd_margin": self.sd_margin, "sd_total": self.sd_total,
                         "n_resid": self.n_resid})

    def a0(self, neutral: bool = False) -> Forecast:
        m = 0.0 if neutral else self.a0_margin
        mh, ma = (self.a0_total + m) / 2, (self.a0_total - m) / 2
        return self._fc(mh, ma, self.a0_sd_margin, self.a0_sd_total, self.a0_sd_team,
                        {"mu_home": mh, "mu_away": ma, "sd_margin": self.a0_sd_margin, "sd_total": self.a0_sd_total})


# --------------------------------------------------------------------------- baseball outside MLB

class BaseballModel:
    """Team + park + home shared-gamma joint (mlb_model.Ratings) on the current season's games. Where the
    competition allows ties (NPB, KBO, CPBL after the extra-inning limit) the final-score distribution keeps
    the league's tie rate: (1 − t)·no_tie(joint) + t·(the joint's tie cells). A0: the season's empirical
    total and margin distributions to date."""

    def __init__(self, games: list[dict], asof: str, cfg: dict, init=None):
        season = to_date(asof).year
        prior = [g for g in games if to_date(g["date"]).year == season and g["date"][:10] < asof[:10]]
        self.n = len(prior)
        if self.n < cfg["min_games"]:
            raise ValueError(f"only {self.n} games this season before {asof}")
        self.cfg = cfg
        mg = [{"hr": g["hs"], "ar": g["as"], "home": g["home"], "away": g["away"],
               "venue": g.get("venue") or g["home"]} for g in prior]
        self.rt = mm.Ratings(mg)
        ties = sum(1 for g in prior if g["hs"] == g["as"])
        k, t0 = cfg["tie_prior_strength"], cfg["tie_prior"]
        self.tie = (ties + k * t0) / (self.n + k) if cfg.get("ties") else 0.0
        self.emp_margin, self.emp_total = defaultdict(float), defaultdict(float)
        for g in prior:
            self.emp_margin[g["hs"] - g["as"]] += 1 / self.n
            self.emp_total[g["hs"] + g["as"]] += 1 / self.n

    def a1(self, home: str, away: str, neutral: bool = False, venue=None) -> Forecast:
        joint, mh, ma = self.rt.joint(home, away, venue or home)
        if self.tie > 0:
            raw = mm.shared_gamma_joint(mh, ma, self.rt.shape, int(mm.PRIORS["support"]) * 2)
            tied = {k: v for k, v in raw.items() if k[0] == k[1]}
            st = math.fsum(tied.values())
            joint = {k: v * (1 - self.tie) for k, v in joint.items()}
            for k, v in tied.items():
                joint[k] = joint.get(k, 0.0) + self.tie * v / st
        return Forecast.from_joint(joint, meta={"mu_home": mh, "mu_away": ma, "shape": self.rt.shape, "tie": self.tie})

    def a0(self, neutral: bool = False) -> Forecast:
        return Forecast(dict(self.emp_margin), dict(self.emp_total), meta={"n": self.n})


# --------------------------------------------------------------------------- team-sport engine

FAMILY_MODELS = {"goals": GoalsModel, "hockey": HockeyModel, "points": PointsModel, "baseball": BaseballModel}


class TeamEngine:
    """Replays a league in date order. On each date it fits A0/A1 on games strictly before that date
    (warm-starting from the previous fit) and forecasts that date's games; residuals of those forecasts
    feed later widths. The same code path serves live `predict` (replay, then forecast one event) and
    `validate` (replay, forecasting and scoring every game in the range)."""

    def __init__(self, cfg: dict, games: list[dict]):
        self.cfg = cfg
        self.games = sorted([g for g in games if g.get("hs") is not None], key=lambda g: (g["date"], str(g.get("id", ""))))
        self.book = ResidualBook(cfg.get("resid_keep", 400))
        self.model = None

    def fit(self, asof: str):
        cls = FAMILY_MODELS[self.cfg["family"]]
        kw = {"book": self.book} if cls is PointsModel else {}
        self.model = cls(self.games, asof, self.cfg, init=self.model, **kw) if cls is not BaseballModel \
            else cls(self.games, asof, self.cfg)
        return self.model

    def forecast(self, g: dict, rho: float = 0.0) -> tuple[Forecast, Forecast]:
        m, neu = self.model, g.get("neutral", False)
        if isinstance(m, GoalsModel):
            return m.a0(neu), m.a1(g["home"], g["away"], neu, rho)
        if isinstance(m, BaseballModel):
            return m.a0(neu), m.a1(g["home"], g["away"], neu, g.get("venue"))
        return m.a0(neu), m.a1(g["home"], g["away"], neu)

    def replay(self, start: str | None, end: str | None, warm_from: str | None = None, dc: bool = False):
        """Yield (game, a0, a1[, a1_dc]) for games dated in [start, end]; games from warm_from build the
        residual book without being yielded."""
        by_date = defaultdict(list)
        for g in self.games:
            by_date[g["date"][:10]].append(g)
        first = warm_from or start
        for d in sorted(by_date):
            if end and d > end:
                break
            if first and d < first:
                continue
            try:
                self.fit(d)
            except ValueError:
                continue
            rho = estimate_rho(self.model.rows, self.model.rt) if dc and isinstance(self.model, GoalsModel) else 0.0
            for g in by_date[d]:
                f0, f1 = self.forecast(g)
                if isinstance(self.model, PointsModel):
                    mh, ma = self.model.rt.means(g["home"], g["away"], g.get("neutral", False))
                    self.book.add(g, mh, ma)
                if start is None or d >= start:
                    out = (g, f0, f1)
                    if dc:
                        out += (self.forecast(g, rho)[1] if isinstance(self.model, GoalsModel) else f1,)
                    yield out

    def predict(self, home: str, away: str, date: str, neutral: bool = False, venue=None) -> tuple[Forecast, Forecast]:
        resid_days = self.cfg.get("resid_days")
        if resid_days:
            warm = (to_date(date) - dt.timedelta(days=resid_days)).isoformat()
            last = (to_date(date) - dt.timedelta(days=1)).isoformat()
            for _ in self.replay(None, last, warm_from=warm):
                pass
        self.fit(date)
        return self.forecast({"home": home, "away": away, "neutral": neutral, "venue": venue})


# --------------------------------------------------------------------------- tennis

ROUND_ORDER = {r: i for i, r in enumerate(["Q1", "Q2", "Q3", "Q4", "ER", "RR", "R128", "R64", "R32", "R16",
                                           "QF", "SF", "BR", "F"])}


def hold_prob(p: float) -> float:
    """P(server wins a standard game) when he wins each service point with probability p."""
    q = 1 - p
    deuce = p * p / (1 - 2 * p * q)
    return p ** 4 * (1 + 4 * q + 10 * q * q) + 20 * p ** 3 * q ** 3 * deuce


def tiebreak_prob(pa: float, pb: float, first7: int = 7) -> float:
    """P(A wins a tiebreak to `first7` (win by 2) when A serves the first point; serve alternates after
    point 1 and then every two points."""
    from functools import lru_cache

    def a_serves(n: int) -> bool:  # n = points played so far
        return n == 0 or ((n - 1) // 2) % 2 == 1

    @lru_cache(maxsize=None)
    def f(i: int, j: int) -> float:
        if i >= first7 and i - j >= 2:
            return 1.0
        if j >= first7 and j - i >= 2:
            return 0.0
        if i == j and i >= first7 - 1:
            # tied from 6-6 on: the next two points are served one each, so the race is exact
            w = pa * (1 - pb)
            l = (1 - pa) * pb
            return w / (w + l)
        p = pa if a_serves(i + j) else 1 - pb
        return p * f(i + 1, j) + (1 - p) * f(i, j + 1)
    return f(0, 0)


def set_outcomes(pa: float, pb: float, a_serves_first: bool) -> list[tuple]:
    """Exact distribution of set results: (a_won, games_a, games_b, a_serves_next_set_first, prob).
    Standard set: first to 6 games with a 2-game lead, tiebreak at 6-6 (counted 7-6)."""
    ga, gb = hold_prob(pa), hold_prob(pb)
    states = {(0, 0): 1.0}
    out = []
    while states:
        nxt = defaultdict(float)
        for (i, j), p in states.items():
            n = i + j
            a_srv = (n % 2 == 0) == a_serves_first
            if i == 6 and j == 6:
                tb_first_a = a_srv
                pt = tiebreak_prob(pa, pb) if tb_first_a else 1 - tiebreak_prob(pb, pa)
                # after a tiebreak the player who received first in the tiebreak serves first next set
                nxt_first_a = not tb_first_a
                out.append((True, 7, 6, nxt_first_a, p * pt))
                out.append((False, 6, 7, nxt_first_a, p * (1 - pt)))
                continue
            pw = ga if a_srv else 1 - gb
            for di, dj, q in ((1, 0, pw), (0, 1, 1 - pw)):
                a, b = i + di, j + dj
                if (a >= 6 and a - b >= 2) or (b >= 6 and b - a >= 2):
                    games = a + b
                    nxt_first_a = (games % 2 == 0) == a_serves_first
                    out.append((a > b, a, b, nxt_first_a, p * q))
                else:
                    nxt[(a, b)] += p * q
        states = nxt
    return out


def match_distribution(pa: float, pb: float, best_of: int) -> dict:
    """{(sets_a, sets_b, games_a, games_b): prob}. The first server is a coin flip."""
    need = best_of // 2 + 1
    cache = {}

    def so(first_a):
        if first_a not in cache:
            cache[first_a] = set_outcomes(pa, pb, first_a)
        return cache[first_a]
    states = {(0, 0, 0, 0, True): 0.5, (0, 0, 0, 0, False): 0.5}
    done = defaultdict(float)
    while states:
        nxt = defaultdict(float)
        for (sa, sb, xa, xb, fa), p in states.items():
            for a_won, g1, g2, nfa, q in so(fa):
                key = (sa + a_won, sb + (not a_won), xa + g1, xb + g2)
                if key[0] == need or key[1] == need:
                    done[key] += p * q
                else:
                    nxt[key + (nfa,)] += p * q
        states = nxt
    return dict(done)


def match_win_prob(pa: float, pb: float, best_of: int) -> float:
    """P(A wins the match); winner-only recursion over sets (fast path used by the bisection)."""
    trans = {}
    for first_a in (True, False):
        agg = defaultdict(float)
        for a_won, _, _, nfa, q in set_outcomes(pa, pb, first_a):
            agg[(a_won, nfa)] += q
        trans[first_a] = agg
    need = best_of // 2 + 1
    states = {(0, 0, True): 0.5, (0, 0, False): 0.5}
    win = 0.0
    while states:
        nxt = defaultdict(float)
        for (sa, sb, fa), p in states.items():
            for (a_won, nfa), q in trans[fa].items():
                na, nb = sa + a_won, sb + (not a_won)
                if na == need:
                    win += p * q
                elif nb < need:
                    nxt[(na, nb, nfa)] += p * q
        states = nxt
    return win


def serve_probs_for(p_match: float, p_serve_avg: float, best_of: int) -> tuple[float, float]:
    """Point-level serve probabilities (pa, pb) with mean p_serve_avg whose match-win probability equals p_match."""
    lo, hi = -0.45, 0.45
    lo = max(lo, 2 * (0.02 - p_serve_avg))
    hi = min(hi, 2 * (0.98 - p_serve_avg))
    target = min(max(p_match, 1e-4), 1 - 1e-4)
    for _ in range(28):
        mid = (lo + hi) / 2
        if match_win_prob(p_serve_avg + mid / 2, p_serve_avg - mid / 2, best_of) < target:
            lo = mid
        else:
            hi = mid
    d = (lo + hi) / 2
    return p_serve_avg + d / 2, p_serve_avg - d / 2


def tennis_forecast(dist: dict) -> Forecast:
    """Forecast whose 'margin' is games_a − games_b and 'total' is total games; extra['sets'] holds the
    set-score distribution (margin = sets_a − sets_b)."""
    gm, gt, sm, st = defaultdict(float), defaultdict(float), defaultdict(float), defaultdict(float)
    ga_pmf, gb_pmf = defaultdict(float), defaultdict(float)
    for (sa, sb, xa, xb), p in dist.items():
        gm[xa - xb] += p
        gt[xa + xb] += p
        sm[sa - sb] += p
        st[sa + sb] += p
        ga_pmf[xa] += p
        gb_pmf[xb] += p
    p_a = math.fsum(p for (sa, sb, _, _), p in dist.items() if sa > sb)
    return Forecast(dict(gm), dict(gt), dict(ga_pmf), dict(gb_pmf),
                    extra={"sets": Forecast(dict(sm), dict(st))}, meta={"p_a_win": p_a})


class TennisElo:
    """Overall and surface Elo with the FiveThirtyEight K schedule K = k_num/(n + k_offset)^k_exp.
    A0 = overall Elo for the winner and the empirical total-games distribution for the best-of format;
    A1 = the surface-blended Elo mapped to serve/return point probabilities and the exact match chain."""

    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.r, self.rs = defaultdict(lambda: cfg["init"]), defaultdict(lambda: cfg["init"])
        self.n, self.ns = defaultdict(int), defaultdict(int)
        self.serve = []   # (date, surface, points_won_on_serve, serve_points)
        self.games_hist = []  # (date, best_of, total_games, sets_margin_abs)

    def k(self, n: int) -> float:
        c = self.cfg
        return c["k_num"] / (n + c["k_offset"]) ** c["k_exp"]

    @staticmethod
    def elo_p(d: float) -> float:
        return 1.0 / (1.0 + 10 ** (-d / 400.0))

    def p_overall(self, a: str, b: str) -> float:
        return self.elo_p(self.r[a] - self.r[b])

    def p_blend(self, a: str, b: str, surface: str) -> float:
        w = self.cfg["surface_blend"]
        d = (1 - w) * (self.r[a] - self.r[b]) + w * (self.rs[(a, surface)] - self.rs[(b, surface)])
        return self.elo_p(d)

    def serve_avg(self, surface: str, asof: str) -> float:
        d0 = to_date(asof)
        win = self.cfg["serve_window_days"]
        rows = [(w, n) for d, s, w, n in self.serve if s == surface and 0 < (d0 - d).days <= win]
        prior = self.cfg["serve_prior"].get(surface, 0.64)
        won, pts = sum(w for w, _ in rows), sum(n for _, n in rows)
        return (won + 2000 * prior) / (pts + 2000)

    def a0_games(self, best_of: int, asof: str) -> Forecast | None:
        d0 = to_date(asof)
        win = self.cfg["games_window_days"]
        tots = [t for d, bo, t, _ in self.games_hist if bo == best_of and 0 < (d0 - d).days <= win]
        if len(tots) < 50:
            return None
        pmf = defaultdict(float)
        for t in tots:
            pmf[t] += 1 / len(tots)
        return Forecast({0: 1.0}, dict(pmf))

    def forecast(self, a: str, b: str, surface: str, best_of: int, asof: str) -> tuple[float, Forecast | None, float, Forecast]:
        p0 = self.p_overall(a, b)
        p1 = self.p_blend(a, b, surface)
        pa, pb = serve_probs_for(p1, self.serve_avg(surface, asof), best_of)
        f1 = tennis_forecast(match_distribution(pa, pb, best_of))
        f1.meta.update({"p_serve_a": pa, "p_serve_b": pb})
        return p0, self.a0_games(best_of, asof), p1, f1

    def update(self, m: dict) -> None:
        w, l, s = m["winner"], m["loser"], m.get("surface") or "Hard"
        if m.get("walkover"):
            return
        e = self.p_overall(w, l)
        kw, kl = self.k(self.n[w]), self.k(self.n[l])
        self.r[w] += kw * (1 - e)
        self.r[l] -= kl * (1 - e)
        es = self.elo_p(self.rs[(w, s)] - self.rs[(l, s)])
        ksw, ksl = self.k(self.ns[(w, s)]), self.k(self.ns[(l, s)])
        self.rs[(w, s)] += ksw * (1 - es)
        self.rs[(l, s)] -= ksl * (1 - es)
        self.n[w] += 1
        self.n[l] += 1
        self.ns[(w, s)] += 1
        self.ns[(l, s)] += 1
        d = to_date(m["date"])
        if m.get("serve_won") is not None and m.get("serve_pts"):
            self.serve.append((d, s, m["serve_won"], m["serve_pts"]))
        if m.get("complete") and m.get("total_games") is not None:
            self.games_hist.append((d, m.get("best_of", 3), m["total_games"], m.get("sets_margin", 0)))


def parse_tennis_score(score: str) -> dict | None:
    """'6-4 3-6 7-6(5)' -> winner/loser games and sets. None for an unparseable or incomplete score."""
    if not score:
        return None
    s = score.upper()
    incomplete = any(x in s for x in ("RET", "W/O", "DEF", "ABD", "UNFINISHED", "WO"))
    gw = gl = sw = sl = 0
    for part in score.split():
        base = part.split("(")[0].replace("[", "").replace("]", "")
        if "-" not in base:
            continue
        try:
            x, y = (int(v) for v in base.split("-", 1))
        except ValueError:
            continue
        if x >= 10 or y >= 10:  # a match tiebreak recorded as points counts as one game (7-6 / 6-7)
            x, y = (1, 0) if x > y else (0, 1)
        gw += x
        gl += y
        sw += x > y
        sl += y > x
    if gw + gl == 0:
        return None
    return {"games_w": gw, "games_l": gl, "sets_w": sw, "sets_l": sl, "complete": not incomplete}


def tennis_order(m: dict) -> tuple:
    return (m["date"], str(m.get("tourney_id", "")), ROUND_ORDER.get(m.get("round", ""), 50), int(m.get("match_num") or 0))


# --------------------------------------------------------------------------- cricket

class CricketModel:
    """Limited-overs cricket. Result: Elo (no home term; cricsheet does not mark a home side) against the
    A0 of 0.5. First-innings total: ridge batting/bowling/venue model on uncensored, full-length first
    innings (reduced-overs and no-result matches are excluded), width from out-of-sample residuals;
    A0 = the format's first-innings mean and SD. Second innings are target-censored and not modelled."""

    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.elo = defaultdict(lambda: cfg["elo_init"])
        self.innings = []   # (date, bat, bowl, venue, runs)
        self.resid = []

    def p_win(self, a: str, b: str) -> float:
        return 1.0 / (1.0 + 10 ** (-(self.elo[a] - self.elo[b]) / 400.0))

    def fit_totals(self, asof: str) -> dict | None:
        d0 = to_date(asof)
        rows = [(decay((d0 - d).days, self.cfg["half_life"]), bat, bowl, v, r) for d, bat, bowl, v, r in self.innings
                if 0 < (d0 - d).days <= self.cfg["window"]]
        if len(rows) < self.cfg["min_innings"]:
            return None
        sw = math.fsum(w for w, *_ in rows)
        mu = math.fsum(w * r for w, *_, r in rows) / sw
        bat, bowl, ven = defaultdict(float), defaultdict(float), defaultdict(float)
        lt, lv = self.cfg["lam_team"], self.cfg["lam_venue"]
        for _ in range(100):
            prev = (mu, dict(bat), dict(bowl), dict(ven))
            for par, key, lam, sign in ((bat, 1, lt, 1), (bowl, 2, lt, -1), (ven, 3, lv, 1)):
                num, den = defaultdict(float), defaultdict(float)
                for row in rows:
                    w, r = row[0], row[4]
                    pred = mu + bat[row[1]] - bowl[row[2]] + ven[row[3]]
                    own = par[row[key]] * sign
                    num[row[key]] += w * (r - (pred - own)) * sign
                    den[row[key]] += w
                for t in den:
                    par[t] = num[t] / (den[t] + lam)
            mu = math.fsum(w * (r - bat[b] + bowl[o] - ven[v]) for w, b, o, v, r in rows) / sw
            delta = max([abs(mu - prev[0])] + [abs(bat[t] - prev[1].get(t, 0.0)) for t in bat])
            if delta < 1e-5:
                break
        sd_a0 = math.sqrt(math.fsum(w * (r - mu) ** 2 for w, *_, r in rows) / sw)
        return {"mu": mu, "bat": bat, "bowl": bowl, "ven": ven, "sd_a0": sd_a0,
                "mean_a0": math.fsum(w * r for w, *_, r in rows) / sw}

    def forecast(self, bat: str, bowl: str, venue: str, asof: str) -> tuple[Forecast, Forecast] | None:
        fit = self.fit_totals(asof)
        if fit is None:
            return None
        mu = fit["mu"] + fit["bat"].get(bat, 0.0) - fit["bowl"].get(bowl, 0.0) + fit["ven"].get(venue, 0.0)
        sd1 = ResidualBook.blend(self.resid[-self.cfg["resid_keep"]:], self.cfg.get("sd0_total", fit["sd_a0"]),
                                 self.cfg["sd_prior_n"])
        f0 = Forecast({0: 1.0}, disc_normal(fit["mean_a0"], fit["sd_a0"], floor0=True), meta={"mu": fit["mean_a0"]})
        f1 = Forecast({0: 1.0}, disc_normal(mu, sd1, floor0=True), meta={"mu": mu, "sd": sd1})
        return f0, f1

    def update(self, m: dict, first_innings_pred: float | None = None) -> None:
        a, b = m["team1"], m["team2"]
        if m.get("winner") in (a, b):
            e = self.p_win(a, b)
            y = 1.0 if m["winner"] == a else 0.0
            k = self.cfg["elo_k"]
            self.elo[a] += k * (y - e)
            self.elo[b] -= k * (y - e)
        if m.get("first_innings_valid"):
            if first_innings_pred is not None:
                self.resid.append(m["first_innings_runs"] - first_innings_pred)
            self.innings.append((to_date(m["date"]), m["bat_first"], m["bowl_first"], m.get("venue", ""),
                                 m["first_innings_runs"]))


# --------------------------------------------------------------------------- scoring and validation

def outcome_scores(fc: Forecast, g: dict, draws: bool) -> dict:
    y = g["hs"] - g["as"]
    ph = p_gt(fc.margin, 0)
    pd = fc.margin.get(0, 0.0) if draws else 0.0
    pa = max(0.0, 1 - ph - pd)
    s = {"win_brier": (ph - (1.0 if y > 0 else 0.0)) ** 2}
    p_real = ph if y > 0 else (pa if y < 0 else pd)
    s["win_logloss"] = -math.log(max(p_real, 1e-12))
    if draws:  # ordered three-way RPS: away, draw, home
        c1, c2 = pa, pa + pd
        o1, o2 = (1.0 if y < 0 else 0.0), (1.0 if y <= 0 else 0.0)
        s["result_rps3"] = ((c1 - o1) ** 2 + (c2 - o2) ** 2) / 2
    s["margin_rps"] = rps(fc.margin, int(y))
    s["total_rps"] = rps(fc.total, int(g["hs"] + g["as"]))
    return s


def block_bootstrap(per_block: dict, key: str, boot: int = 2000, seed: int = 20260926) -> list[float]:
    blocks = [v for v in per_block.values() if v["n"]]
    rng = random.Random(seed)
    stats = []
    for _ in range(boot):
        smp = [rng.choice(blocks) for _ in blocks]
        n = sum(b["n"] for b in smp)
        stats.append(sum(b[key] for b in smp) / n)
    stats.sort()
    return [stats[int(0.025 * boot)], stats[int(0.975 * boot) - 1]]


def summarise_pairs(rows: list[dict], metrics: list[str], block_key: str = "block", boot: int = 2000) -> dict:
    """rows: {'block', 'a0': {metric: v}, 'a1': {...}, ...}. Paired A1 − A0 means with block-bootstrap CIs."""
    out = {"n": len(rows)}
    for m in metrics:
        pairs = [(r["a0"][m], r["a1"][m], r[block_key]) for r in rows if m in r["a0"] and m in r["a1"]]
        if not pairs:
            continue
        per = defaultdict(lambda: {"n": 0, "d": 0.0})
        for x0, x1, b in pairs:
            per[b]["n"] += 1
            per[b]["d"] += x1 - x0
        n = len(pairs)
        out[m] = {"n": n, "a0": sum(p[0] for p in pairs) / n, "a1": sum(p[1] for p in pairs) / n,
                  "a1_minus_a0": sum(p[1] - p[0] for p in pairs) / n,
                  "ci95_block": block_bootstrap(per, "d", boot)}
        for extra in ("tb1", "a1dc"):
            both = [(r["a1"][m], r[extra][m], r[block_key]) for r in rows if extra in r and m in r[extra] and m in r["a1"]]
            if not both:
                continue
            per2 = defaultdict(lambda: {"n": 0, "d": 0.0})
            for x1, xe, b in both:
                per2[b]["n"] += 1
                per2[b]["d"] += x1 - xe
            ne = len(both)
            out[m][extra] = {"n": ne, "a1": sum(x[0] for x in both) / ne, extra: sum(x[1] for x in both) / ne,
                             "a1_minus_" + extra: sum(x[0] - x[1] for x in both) / ne,
                             "ci95_block": block_bootstrap(per2, "d", boot)}
    return out


def iso_week(d: str) -> str:
    y, w, _ = to_date(d).isocalendar()
    return f"{y}-W{w:02d}"


def validate_team(cfg: dict, games: list[dict], start: str, end: str, warm_days: int | None = None,
                  tb1_league: str | None = None, dc: bool = False, total_line: float | None = None,
                  boot: int = 2000) -> dict:
    """Rolling origin over [start, end]: every game forecast from games strictly before its date.
    Scores: win Brier/log loss, three-way RPS where draws exist, margin and total RPS, total Brier at a
    line fixed from the pre-start history (floor(mean)+0.5), soccer first-half total RPS and BTTS,
    hockey regulation three-way. Blocks for the bootstrap are ISO weeks."""
    eng = TeamEngine(cfg, games)
    hist = [g for g in eng.games if g["date"][:10] < start]
    if total_line is None and hist:
        recent = hist[-min(len(hist), 1000):]
        total_line = math.floor(sum(g["hs"] + g["as"] for g in recent) / len(recent)) + 0.5
    warm = (to_date(start) - dt.timedelta(days=warm_days or cfg.get("resid_days") or 0)).isoformat()
    tb1 = tb1_scores(tb1_league, eng.games, total_line) if tb1_league else None
    rows = []
    draws = cfg.get("draws", True) and cfg["family"] != "hockey"
    for item in eng.replay(start, end, warm_from=warm, dc=dc):
        g, f0, f1 = item[:3]
        r = {"block": iso_week(g["date"]), "date": g["date"][:10]}
        for name, fc in (("a0", f0), ("a1", f1)) + ((("a1dc", item[3]),) if dc else ()):
            s = outcome_scores(fc, g, draws)
            t = g["hs"] + g["as"]
            s["total_brier_line"] = (p_gt(fc.total, total_line) - (1.0 if t > total_line else 0.0)) ** 2
            if "h1" in fc.extra and g.get("hs_ht") is not None:
                s["h1_total_rps"] = rps(fc.extra["h1"].total, int(g["hs_ht"] + g["as_ht"]))
            if fc.joint is not None and cfg["family"] == "goals":
                s["btts_brier"] = (fc.probs()["p_btts"] - (1.0 if g["hs"] > 0 and g["as"] > 0 else 0.0)) ** 2
            if "reg" in fc.extra and g.get("finish") in ("REG", "OT", "SO"):
                rh, ra = reg_score(g)
                sub = fc.extra["reg"]
                ph, pd = p_gt(sub.margin, 0), sub.margin.get(0, 0.0)
                pa = 1 - ph - pd
                y = rh - ra
                s["reg_rps3"] = ((pa - (y < 0)) ** 2 + (pa + pd - (y <= 0)) ** 2) / 2
            r[name] = s
        if tb1 is not None and game_key(g) in tb1:
            r["tb1"] = tb1[game_key(g)]
        rows.append(r)
    metrics = ["win_brier", "win_logloss", "result_rps3", "margin_rps", "total_rps", "total_brier_line",
               "h1_total_rps", "btts_brier", "reg_rps3"]
    res = summarise_pairs(rows, metrics, boot=boot)
    res.update({"league": cfg["league"], "from": start, "to": end, "total_line": total_line,
                "model_version": MODEL_VERSION, "params_sha": params_sha(cfg)})
    return res


def game_key(g: dict) -> tuple:
    return (g["date"][:10], g["home"], g["away"], g.get("id", ""))


def tb1_scores(league: str, games: list[dict], total_line: float | None) -> dict:
    """TB-1 (tools/team_baseline.py) replayed on the same games, season by season, scored on win Brier and
    the total at the fixed line. Returns {game_key: scores}; games TB-1 cannot yet price are absent."""
    import team_baseline as tb
    cfg = tb.LEAGUES[league]
    out, season, st = {}, None, None
    for g in sorted(games, key=lambda x: x["date"]):
        s = g.get("season") or to_date(g["date"]).year
        if s != season:
            season, st = s, tb.SeasonState(k=cfg["k"], sd_total=cfg["sd_total"], sd_margin=cfg["sd_margin"])
        if st.n_league_games() >= 10 and st.n_games(g["home"]) >= 1 and st.n_games(g["away"]) >= 1:
            pred = st.predict(g["home"], g["away"], neutral=g.get("neutral", False))
            sdm, sdt = st.resid_sd()
            pr = tb.contract_probs(league, pred, sdm, sdt, total_line, None, state=st)
            y = g["hs"] - g["as"]
            sc = {"win_brier": (pr["home_win"] - (1.0 if y > 0 else 0.0)) ** 2}
            if total_line is not None:
                t = g["hs"] + g["as"]
                sc["total_brier_line"] = (pr[f"over_{total_line:g}"] - (1.0 if t > total_line else 0.0)) ** 2
            out[game_key(g)] = sc
        st.add({"home": g["home"], "away": g["away"], "hs": g["hs"], "as": g["as"], "neutral": g.get("neutral", False)})
    return out


# --------------------------------------------------------------------------- shadow lane

LOG_FIELDS = ["row_id", "frozen_at_utc", "card", "league", "event_id", "event_date", "start_utc", "home", "away",
              "neutral", "model_version", "params_sha", "n_prior_games", "line_total", "line_home",
              "a1_mu_home", "a1_mu_away",
              "a1_p_home_win", "a1_p_draw", "a1_p_away_win", "a1_p_over", "a1_p_push", "a1_p_home_cover", "a1_p_line_push",
              "a0_p_home_win", "a0_p_draw", "a0_p_away_win", "a0_p_over", "a0_p_push", "a0_p_home_cover", "a0_p_line_push"]
RESULT_FIELDS = ["row_id", "event_id", "home_score", "away_score", "finish", "settled_at_utc", "source"]


def shadow_row(cfg: dict, event: dict, fc0: Forecast, fc1: Forecast, n_prior: int, card: str,
               total: float | None, line: float | None, now: dt.datetime) -> dict:
    row = {"row_id": f"{cfg['league']}:{event['id']}:{total}:{line}", "frozen_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
           "card": card, "league": cfg["league"], "event_id": event["id"], "event_date": event["date"][:10],
           "start_utc": event.get("start_utc", ""), "home": event["home"], "away": event["away"],
           "neutral": int(bool(event.get("neutral"))), "model_version": MODEL_VERSION, "params_sha": params_sha(cfg),
           "n_prior_games": n_prior, "line_total": "" if total is None else total, "line_home": "" if line is None else line,
           "a1_mu_home": f"{fc1.meta.get('mu_home', float('nan')):.4f}", "a1_mu_away": f"{fc1.meta.get('mu_away', float('nan')):.4f}"}
    for pre, fc in (("a1_", fc1), ("a0_", fc0)):
        q = fc.probs(total=total, line=line)
        for k in ("p_home_win", "p_draw", "p_away_win", "p_over", "p_push", "p_home_cover", "p_line_push"):
            row[pre + k] = f"{q[k]:.4f}" if k in q else ""
    return row


def append_row(path: Path, fields: list[str], row: dict) -> None:
    mm.append_row(path, fields, row)


def score_shadow(log: Path, results: Path) -> dict:
    res = {r["row_id"]: r for r in mm.read_rows(results)}
    acc = defaultdict(lambda: defaultdict(lambda: {"a0": 0.0, "a1": 0.0, "n": 0}))
    for r in mm.read_rows(log):
        f = res.get(r["row_id"])
        if not f:
            continue
        h, a = int(float(f["home_score"])), int(float(f["away_score"]))
        lg = r["league"]
        targets = {"home_win": (1.0 if h > a else 0.0, "p_home_win", None)}
        if r["line_total"] != "" and (h + a) != float(r["line_total"]):
            targets["total_over"] = (1.0 if h + a > float(r["line_total"]) else 0.0, "p_over", "p_push")
        if r["line_home"] != "" and (h - a + float(r["line_home"])) != 0:
            targets["home_cover"] = (1.0 if h - a + float(r["line_home"]) > 0 else 0.0, "p_home_cover", "p_line_push")
        for name, (y, key, push) in targets.items():
            for m in ("a0", "a1"):
                p = float(r[f"{m}_{key}"])
                if push:
                    pu = float(r[f"{m}_{push}"] or 0)
                    p = p / (1 - pu) if pu < 1 else 0.5
                acc[lg][name][m] += (p - y) ** 2
            acc[lg][name]["n"] += 1
    return {lg: {k: {"n": v["n"], "a1_brier": v["a1"] / v["n"], "a0_brier": v["a0"] / v["n"],
                     "a1_minus_a0": (v["a1"] - v["a0"]) / v["n"]} for k, v in d.items() if v["n"]}
            for lg, d in acc.items()}


# --------------------------------------------------------------------------- CLI

def load_games(cfg: dict, args, end_date: str, start_date: str | None = None) -> list[dict]:
    import sport_data as sd
    if getattr(args, "csv", None):
        return sd.load_csv(args.csv)
    path = getattr(args, "espn_path", None) or cfg.get("espn")
    if not path:
        raise SystemExit(f"error: {cfg['league']} has no network source here; pass --csv FILE")
    days = cfg.get("window", 730) + (cfg.get("resid_days") or 0) + 5
    start = start_date or (to_date(end_date) - dt.timedelta(days=days)).isoformat()
    return sd.espn_results(path, start, end_date, cfg["family"])


def print_probs(label: str, q: dict) -> None:
    keys = [k for k in q if k.startswith("p_") or k.endswith("_p_home_win") or k.endswith("_p_draw")
            or k.startswith("mean") or k.endswith("mean_total")]
    print(f"{label}: " + ", ".join(f"{k}={q[k]:.4f}" for k in keys))


def cmd_predict(args) -> int:
    cfg = config(args.league)
    if cfg["family"] == "tennis":
        import sport_data as sd
        matches = sd.load_tennis(cfg["league"], args.date, tml_dir=args.tml_dir, csv_path=args.csv)
        elo = TennisElo(cfg)
        for m in sorted(matches, key=tennis_order):
            if m["date"] < args.date:
                elo.update(m)
        a = sd.match_name(args.p1, elo.n)
        b = sd.match_name(args.p2, elo.n)
        p0, g0, p1, f1 = elo.forecast(a, b, args.surface, args.best_of, args.date)
        print(f"{a} v {b} ({args.surface}, best of {args.best_of}) — LEARNING_ONLY, never a card input")
        print(f"A0 overall Elo: P({a} wins) = {p0:.4f}")
        q = f1.probs(total=args.total, line=args.line)
        print(f"A1 surface-blended Elo + serve chain: P({a} wins) = {p1:.4f}; serve points {f1.meta['p_serve_a']:.3f} / "
              f"{f1.meta['p_serve_b']:.3f}; mean games {q['mean_total']:.2f}")
        if args.total is not None:
            print(f"  total games {args.total}: over {q['p_over']:.4f}, push {q['p_push']:.4f}, under {q['p_under']:.4f}"
                  + (f" (A0 over {g0.probs(total=args.total)['p_over']:.4f})" if g0 else ""))
        if args.line is not None:
            print(f"  {a} games {args.line:+g}: cover {q['p_home_cover']:.4f}, push {q['p_line_push']:.4f}")
        sets = f1.extra["sets"].probs(line=-1.5)
        print(f"  sets: {a} −1.5 {sets['p_home_cover']:.4f}")
        return 0
    if cfg["family"] == "cricket":
        import sport_data as sd
        if not args.cricsheet:
            raise SystemExit("error: cricket reads cricsheet JSON; pass --cricsheet DIR")
        matches = sd.load_cricsheet(args.cricsheet, cfg["overs"])
        cm_ = CricketModel(cfg)
        for m in sorted(matches, key=lambda x: x["date"]):
            if m["date"] < args.date:
                cm_.update(m)
        a = sd.match_name(args.home, cm_.elo)
        b = sd.match_name(args.away, cm_.elo)
        print(f"{a} v {b} — LEARNING_ONLY, never a card input")
        print(f"A0: P({a} wins) = 0.5000; A1 Elo: P({a} wins) = {cm_.p_win(a, b):.4f}")
        for bat, bowl in ((a, b), (b, a)):
            fc = cm_.forecast(bat, bowl, args.venue or "", args.date)
            if fc:
                q0, q1 = fc[0].probs(total=args.total), fc[1].probs(total=args.total)
                extra = f"; over {args.total}: A1 {q1['p_over']:.4f} / A0 {q0['p_over']:.4f}" if args.total is not None else ""
                print(f"  {bat} batting first: A1 mean {q1['mean_total']:.1f} (A0 {q0['mean_total']:.1f}){extra}")
        return 0
    games = load_games(cfg, args, args.date)
    eng = TeamEngine(cfg, [g for g in games if g["date"][:10] < args.date])
    import sport_data as sd
    teams = sorted({g["home"] for g in eng.games} | {g["away"] for g in eng.games})
    home, away = sd.match_name(args.home, teams), sd.match_name(args.away, teams)
    f0, f1 = eng.predict(home, away, args.date, args.neutral)
    print(f"{cfg['league']}: {home} v {away} on {args.date} — {eng.model.n} prior games in the window; "
          f"LEARNING_ONLY, never a card input")
    kw = {"total": args.total, "line": args.line}
    print_probs("A1", f1.probs(**kw))
    print_probs("A0", f0.probs(**kw))
    return 0


def cmd_shadow(args) -> int:
    import sport_data as sd
    cfg = config(args.league)
    if cfg["family"] not in FAMILY_MODELS:
        raise SystemExit("error: the shadow lane covers the team sports; tennis and cricket are predict/validate only "
                         "until a settlement feed is admitted")
    now = dt.datetime.now(dt.timezone.utc)
    path = args.espn_path or cfg.get("espn")
    if not path:
        raise SystemExit(f"error: {cfg['league']} has no ESPN path; pass --espn-path")
    ev = sd.espn_event(path, args.event, args.date)
    if ev["state"] != "pre" or now >= mm.parse_iso(ev["start_utc"]):
        raise SystemExit(f"STARTED_OR_NOT_PREGAME — no shadow row for {args.event} (state {ev['state']})")
    log = Path(args.log)
    row_id = f"{cfg['league']}:{ev['id']}:{args.total}:{args.line}"
    if any(r["row_id"] == row_id for r in mm.read_rows(log)):
        raise SystemExit(f"error: {row_id} is already frozen in {log}; rows are never replaced")
    games = load_games(cfg, args, ev["date"][:10])
    eng = TeamEngine(cfg, [g for g in games if g["date"][:10] < ev["date"][:10]])
    f0, f1 = eng.predict(ev["home"], ev["away"], ev["date"][:10], ev.get("neutral", False))
    row = shadow_row(cfg, ev, f0, f1, eng.model.n, args.card, args.total, args.line, now)
    append_row(log, LOG_FIELDS, row)
    print(json.dumps(row, indent=2))
    return 0


def cmd_settle(args) -> int:
    import sport_data as sd
    log, results = Path(args.log), Path(args.results)
    done = {r["row_id"] for r in mm.read_rows(results)}
    now = dt.datetime.now(dt.timezone.utc)
    added = 0
    for r in mm.read_rows(log):
        if r["row_id"] in done:
            continue
        cfg = config(r["league"])
        path = cfg.get("espn") or args.espn_path
        ev = sd.espn_event(path, r["event_id"], r["event_date"])
        if ev["state"] != "post" or ev.get("hs") is None:
            continue
        append_row(results, RESULT_FIELDS, {"row_id": r["row_id"], "event_id": r["event_id"], "home_score": ev["hs"],
                                            "away_score": ev["as"], "finish": ev.get("finish", ""),
                                            "settled_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "source": ev["source"]})
        done.add(r["row_id"])
        added += 1
    print(f"settled {added} row(s)")
    return 0


def cmd_validate(args) -> int:
    cfg = config(args.league)
    if cfg["family"] in ("tennis", "cricket"):
        raise SystemExit("error: tennis and cricket validation run from research/sport_models_2026-09-26/validate_public.py")
    games = load_games(cfg, args, args.to, start_date=(to_date(args.frm) - dt.timedelta(
        days=cfg.get("window", 730) + (cfg.get("resid_days") or 0))).isoformat())
    res = validate_team(cfg, games, args.frm, args.to, dc=cfg["family"] == "goals")
    print(json.dumps(res, indent=2))
    return 0


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("leagues")
    p = sub.add_parser("predict")
    p.add_argument("--league", required=True)
    p.add_argument("--date", required=True, help="venue-local event date; only earlier results are used")
    p.add_argument("--home")
    p.add_argument("--away")
    p.add_argument("--p1")
    p.add_argument("--p2")
    p.add_argument("--surface", default="Hard")
    p.add_argument("--best-of", type=int, default=3)
    p.add_argument("--venue")
    p.add_argument("--neutral", action="store_true")
    p.add_argument("--total", type=float, help="total threshold to query (games for tennis, first-innings runs for cricket)")
    p.add_argument("--line", type=float, help="home (or player 1) handicap, e.g. -1.5")
    p.add_argument("--csv")
    p.add_argument("--espn-path")
    p.add_argument("--tml-dir")
    p.add_argument("--cricsheet")
    s = sub.add_parser("shadow")
    s.add_argument("--league", required=True)
    s.add_argument("--event", required=True, help="ESPN event id")
    s.add_argument("--date", required=True, help="the event's scoreboard date YYYY-MM-DD")
    s.add_argument("--card", required=True, help="the card this row follows (run after that card is frozen)")
    s.add_argument("--total", type=float)
    s.add_argument("--line", type=float)
    s.add_argument("--espn-path")
    s.add_argument("--csv")
    s.add_argument("--log", default=str(SHADOW_DIR / "shadow_log.csv"))
    t = sub.add_parser("settle")
    t.add_argument("--log", default=str(SHADOW_DIR / "shadow_log.csv"))
    t.add_argument("--results", default=str(SHADOW_DIR / "shadow_results.csv"))
    t.add_argument("--espn-path")
    c = sub.add_parser("score")
    c.add_argument("--log", default=str(SHADOW_DIR / "shadow_log.csv"))
    c.add_argument("--results", default=str(SHADOW_DIR / "shadow_results.csv"))
    v = sub.add_parser("validate")
    v.add_argument("--league", required=True)
    v.add_argument("--from", dest="frm", required=True)
    v.add_argument("--to", required=True)
    v.add_argument("--csv")
    v.add_argument("--espn-path")
    args = ap.parse_args(argv)
    if args.cmd == "leagues":
        for k, v_ in LEAGUES.items():
            print(f"{k:14s} {v_['sport']:18s} {v_['family']:9s} {v_.get('espn') or '(csv / local files)'}")
        print("mlb            baseball           (tools/mlb_model.py — adds probable starters)")
        return 0
    if args.cmd == "predict":
        return cmd_predict(args)
    if args.cmd == "shadow":
        return cmd_shadow(args)
    if args.cmd == "settle":
        return cmd_settle(args)
    if args.cmd == "score":
        print(json.dumps(score_shadow(Path(args.log), Path(args.results)), indent=2))
        return 0
    return cmd_validate(args)


if __name__ == "__main__":
    raise SystemExit(main())
