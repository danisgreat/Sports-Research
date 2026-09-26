#!/usr/bin/env python3
"""MLB A0/A1 shadow model — the numerical programme's first pilot (C-MLB-SHADOW, added 2026-09-26).

Why. The settled record shows the hand-built MLB card process has the lowest resolution of any
sport (0.0075; 58.6% of decisions won at a stated 0.596), and TB-1 found no resolution from team
scoring alone. NUMERICAL_PROGRAM.md §2 names MLB final runs as the first pilot and §6 says it is
where a disciplined model has the most room to add information. Until now it was Markdown only.
This tool implements the A0/A1 recipes (MODEL_IMPLEMENTATION_RECIPES.md §1, §5) as code, so the
pilot can start collecting **prospective shadow evidence** (NUMERICAL_PROGRAM stage S6).

Status: DESIGN IMPLEMENTED — NOT FIT, NOT VALIDATED. Every constant in PRIORS is a declared input,
not a fitted value. The model is never a card input, never cited as evidence on a card, and never a
rank or weight until its prospective test concludes (C-MLB-SHADOW; `L-087`).

Model (route A, reduced-form final score; RULES_BASEBALL control 37):
- A0: the league's own leak-free population to date (home-win rate; empirical total distribution).
- A1: partially pooled, park-neutral team offence (runs scored) and prevention (runs allowed) per game,
  a partially pooled park factor, league home/away split, and — only in shadow mode, where the
  probable starters are captured before first pitch — a starter term: the starter's pooled run
  prevention replaces his team's average prevention for his expected share of the innings. The two
  team means feed the shared-environment Gamma-Poisson joint (negative multinomial; recipes §5), with
  the shape estimated by moments from the season's totals. Ties are removed and the remainder
  renormalised: this is the recipe's labelled "conditional no-tie support" for completed games.
- Historical `validate` uses A1 **without** starters. Past probable starters cannot be reconstructed
  leak-free from box scores (NUMERICAL_PROGRAM §2), so the starter term is only ever judged prospectively.

Commands:
  predict   --date D --home "Team" --away "Team" [--venue-id N] [--total L] [--home-sp ID --away-sp ID]
  shadow    --gamepk PK --total L --card P-### [--log research/mlb_shadow/shadow_log.csv]
            Run straight **after** the card is frozen and before first pitch. Refuses a started game.
            Appends one frozen row; never edits an earlier row.
  settle    [--log …]   append finals for frozen games to research/mlb_shadow/shadow_results.csv
  score     [--log …]   Brier of A1 v A0 on frozen rows that have results (descriptive)
  validate  --season 2026 [--from-date D] [--to-date D]   rolling-origin, leak-free A0 v A1(team-only)
  --fixture-dir DIR   read statsapi JSON from DIR (schedule_<season>.json, feed_<pk>.json,
                      people_<id>.json) instead of the network (tests, replay)
  --now ISO           override the clock (tests)

Standard library only. Network: statsapi.mlb.com (schedule, game feed, pitcher stats by date range).
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import hashlib
import json
import math
import random
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SHADOW_DIR = REPO / "research" / "mlb_shadow"
MODEL_VERSION = "MLB-A1-shadow/2026-09-26b"   # b: team_prior_games 20 -> 120 (research/sport_models_2026-09-26)

# Declared inputs, not fitted values (NUMERICAL_PROGRAM §2: "Parameters/priors are explicit inputs").
PRIORS = {
    "team_prior_games": 120.0,    # games of league-mean runs added to each team's offence and prevention.
                                  # v1 used 20 and was overconfident on Retrosheet 2022-24 (P(home win) from
                                  # 0.08 to 0.90); 120 was selected on 2022 alone by win log loss, then scored
                                  # on 2023-24 (research/sport_models_2026-09-26/README.md §MLB). Not independent
                                  # evidence: the 2025 season and the shadow lane are.
    "park_prior_games": 60.0,     # games of neutral park added to each venue
    "home_prior_games": 200.0,    # games of an even home/away split added to the league home factor
    "starter_prior_ip": 40.0,     # innings of league-mean run prevention added to each starter
    "starter_prior_gs": 5.0,      # starts at the prior length added to each starter's innings per start
    "starter_prior_len": 5.3,     # innings per start at the prior
    "fip_weight": 0.5,            # weight on the FIP-based run estimate when its components exist
    "cfip": 3.15,                 # FIP constant (ERA scale)
    "ra_per_er": 1.08,            # runs per earned run, to put FIP on the RA9 scale
    "starter_mult_bounds": [0.6, 1.5],
    "min_games_env": 100,         # games needed before the shape is estimated from the season
    "default_shape": 7.0,         # shared-environment shape before that (2026 MLB moments give about 7)
    "support": 40,                # runs per team in the joint grid
}

STATSAPI = "https://statsapi.mlb.com"
SCHEDULE_URL = (STATSAPI + "/api/v1/schedule?sportId=1&startDate={start}&endDate={end}&gameType=R"
                "&hydrate=venue")
FEED_URL = STATSAPI + "/api/v1.1/game/{pk}/feed/live"
PITCHER_URL = (STATSAPI + "/api/v1/people/{pid}/stats?stats=byDateRange&group=pitching&season={season}"
               "&startDate={start}&endDate={end}")

LOG_FIELDS = ["row_id", "frozen_at_utc", "card", "game_pk", "official_date", "start_utc", "home", "away",
              "venue_id", "home_sp_id", "away_sp_id", "model_version", "params_sha", "n_prior_games",
              "mu_home", "mu_away", "shape", "line_total",
              "a1_p_over", "a1_p_push", "a1_p_under", "a1_p_home_win", "a1_p_home_m15", "a1_p_away_m15",
              "a0_p_over", "a0_p_push", "a0_p_under", "a0_p_home_win", "a0_p_home_m15", "a0_p_away_m15"]
RESULT_FIELDS = ["game_pk", "home_runs", "away_runs", "innings", "settled_at_utc", "source"]


# --------------------------------------------------------------------------- data access

class Source:
    """statsapi JSON, from the network or from a fixture directory."""

    def __init__(self, fixture_dir: str | None = None):
        self.fixture_dir = Path(fixture_dir) if fixture_dir else None

    def _get(self, url: str, fixture_name: str) -> dict:
        if self.fixture_dir:
            return json.loads((self.fixture_dir / fixture_name).read_text(encoding="utf-8"))
        req = urllib.request.Request(url, headers={"Accept-Encoding": "gzip"})
        with urllib.request.urlopen(req, timeout=90) as resp:
            raw = resp.read()
        if raw[:2] == b"\x1f\x8b":
            raw = gzip.decompress(raw)
        return json.loads(raw.decode("utf-8"))

    def season_games(self, season: int, before: str) -> list[dict]:
        """Completed regular-season games with officialDate strictly before `before` (leak-free)."""
        end = (dt.date.fromisoformat(before) - dt.timedelta(days=1)).isoformat()
        payload = self._get(SCHEDULE_URL.format(start=f"{season}-03-01", end=end), f"schedule_{season}.json")
        return [g for g in parse_schedule(payload) if g["date"] < before]

    def feed(self, pk: int) -> dict:
        return self._get(FEED_URL.format(pk=pk), f"feed_{pk}.json")

    def pitcher(self, pid: int, season: int, before: str) -> dict | None:
        end = (dt.date.fromisoformat(before) - dt.timedelta(days=1)).isoformat()
        try:
            payload = self._get(PITCHER_URL.format(pid=pid, season=season, start=f"{season}-03-01", end=end),
                                f"people_{pid}.json")
        except (OSError, ValueError):
            return None
        return parse_pitcher(payload)


def parse_schedule(payload: dict) -> list[dict]:
    out = []
    for d in payload.get("dates", []):
        for g in d.get("games", []):
            st = g.get("status", {})
            if st.get("abstractGameState") != "Final" or st.get("detailedState") in ("Postponed", "Cancelled"):
                continue
            h, a = g["teams"]["home"], g["teams"]["away"]
            if "score" not in h or "score" not in a:
                continue
            out.append({"pk": g["gamePk"], "date": g.get("officialDate") or d.get("date"),
                        "home": h["team"]["name"], "away": a["team"]["name"],
                        "venue": g.get("venue", {}).get("id"), "hr": int(h["score"]), "ar": int(a["score"])})
    out.sort(key=lambda g: (g["date"], g["pk"]))
    return out


def ip_to_float(s) -> float:
    """statsapi innings: '25.1' means 25⅓, '25.2' means 25⅔."""
    s = str(s)
    whole, _, frac = s.partition(".")
    return int(whole or 0) + {"": 0, "0": 0, "1": 1 / 3, "2": 2 / 3}.get(frac, 0)


def parse_pitcher(payload: dict) -> dict | None:
    for block in payload.get("stats", []):
        for sp in block.get("splits", []):
            st = sp.get("stat", {})
            ip = ip_to_float(st.get("inningsPitched", 0))
            if ip <= 0:
                return None
            return {"ip": ip, "r": float(st.get("runs", st.get("earnedRuns", 0))),
                    "hr": float(st.get("homeRuns", 0)), "bb": float(st.get("baseOnBalls", 0)),
                    "hbp": float(st.get("hitByPitch", 0)), "k": float(st.get("strikeOuts", 0)),
                    "gs": float(st.get("gamesStarted", 0))}
    return None


# --------------------------------------------------------------------------- probability primitives
# The shared-environment joint is the recipes' `shared_gamma_joint` (MODEL_IMPLEMENTATION_RECIPES §5).

def shared_gamma_joint(mu_h: float, mu_a: float, shape: float, support: int) -> dict:
    if min(mu_h, mu_a, shape) <= 0 or not all(map(math.isfinite, (mu_h, mu_a, shape))):
        raise ValueError("positive finite rates and shape required")
    den = shape + mu_h + mu_a
    base = math.lgamma(shape) - shape * math.log(shape / den)
    lh, la = math.log(mu_h / den), math.log(mu_a / den)
    raw = {}
    for h in range(support + 1):
        for a in range(support + 1):
            raw[h, a] = math.exp(math.lgamma(shape + h + a) - base - math.lgamma(h + 1) - math.lgamma(a + 1)
                                 + h * lh + a * la)
    mass = math.fsum(raw.values())
    if 1 - mass > 1e-6:
        raise ValueError(f"grid support too small: omitted mass {1 - mass:.2e}")
    return {k: v / mass for k, v in raw.items()}


def no_tie(joint: dict) -> dict:
    """Condition on a completed, non-tied final (recipe route A, labelled conditional support)."""
    tie = math.fsum(p for (h, a), p in joint.items() if h == a)
    return {k: p / (1 - tie) for k, p in joint.items() if k[0] != k[1]}


def queries(joint: dict, line: float | None) -> dict:
    q = {"p_home_win": math.fsum(p for (h, a), p in joint.items() if h > a),
         "p_home_m15": math.fsum(p for (h, a), p in joint.items() if h - a >= 2),
         "p_away_m15": math.fsum(p for (h, a), p in joint.items() if a - h >= 2),
         "mean_total": math.fsum((h + a) * p for (h, a), p in joint.items())}
    if line is not None:
        q["p_over"] = math.fsum(p for (h, a), p in joint.items() if h + a > line)
        q["p_push"] = math.fsum(p for (h, a), p in joint.items() if h + a == line)
        q["p_under"] = math.fsum(p for (h, a), p in joint.items() if h + a < line)
    return q


# --------------------------------------------------------------------------- A0 and A1

def a0(games: list[dict], line: float | None) -> dict:
    """League population to date: home-win rate and empirical total/margin frequencies (leak-free)."""
    n = len(games)
    if n == 0:
        raise ValueError("no prior games")
    q = {"p_home_win": sum(g["hr"] > g["ar"] for g in games) / n,
         "p_home_m15": sum(g["hr"] - g["ar"] >= 2 for g in games) / n,
         "p_away_m15": sum(g["ar"] - g["hr"] >= 2 for g in games) / n,
         "mean_total": sum(g["hr"] + g["ar"] for g in games) / n}
    if line is not None:
        tot = [g["hr"] + g["ar"] for g in games]
        q["p_over"] = sum(t > line for t in tot) / n
        q["p_push"] = sum(t == line for t in tot) / n
        q["p_under"] = sum(t < line for t in tot) / n
    return q


class Ratings:
    """Leak-free league state built from games before the forecast date."""

    def __init__(self, games: list[dict], priors: dict = PRIORS):
        self.p = priors
        n = len(games)
        if n == 0:
            raise ValueError("no prior games")
        self.n = n
        runs = sum(g["hr"] + g["ar"] for g in games)
        self.m = runs / (2 * n)                                   # runs per team-game
        kh = priors["home_prior_games"]
        self.home_f = (sum(g["hr"] for g in games) + kh * self.m) / ((n + kh) * self.m)
        self.away_f = (sum(g["ar"] for g in games) + kh * self.m) / ((n + kh) * self.m)
        # park factor, partially pooled toward 1
        vr, vg = defaultdict(float), defaultdict(int)
        for g in games:
            vr[g["venue"]] += g["hr"] + g["ar"]
            vg[g["venue"]] += 1
        kp = priors["park_prior_games"]
        self.park = {v: (vr[v] + kp * 2 * self.m) / ((vg[v] + kp) * 2 * self.m) for v in vg}
        self.team_home_venue = {}
        # park-neutral team offence and prevention, partially pooled toward the league mean
        rs, ra, gp = defaultdict(float), defaultdict(float), defaultdict(int)
        for g in games:
            pf = self.park.get(g["venue"], 1.0)
            rs[g["home"]] += g["hr"] / pf
            ra[g["home"]] += g["ar"] / pf
            rs[g["away"]] += g["ar"] / pf
            ra[g["away"]] += g["hr"] / pf
            gp[g["home"]] += 1
            gp[g["away"]] += 1
            self.team_home_venue.setdefault(g["home"], g["venue"])
        k = priors["team_prior_games"]
        self.off = {t: (rs[t] + k * self.m) / (gp[t] + k) for t in gp}
        self.dfn = {t: (ra[t] + k * self.m) / (gp[t] + k) for t in gp}
        totals = [g["hr"] + g["ar"] for g in games]
        mean = sum(totals) / n
        var = sum((t - mean) ** 2 for t in totals) / max(1, n - 1)
        if n >= priors["min_games_env"] and var > mean:
            self.shape = min(200.0, mean * mean / (var - mean))
        else:
            self.shape = priors["default_shape"]

    def starter_multiplier(self, sp: dict | None, opp_prevention: float) -> float:
        """Opponent-scoring multiplier from the starter: his pooled run prevention replaces his team's
        average prevention for his expected share of the innings. 1.0 when no starter data."""
        if not sp:
            return 1.0
        p = self.p
        m9 = self.m  # runs per nine innings ≈ runs per team-game
        prior_ip = p["starter_prior_ip"]
        ra9 = 9 * (sp["r"] + prior_ip * m9 / 9) / (sp["ip"] + prior_ip)
        est = ra9
        if all(k in sp for k in ("hr", "bb", "hbp", "k")) and sp["ip"] > 0:
            fip = (13 * sp["hr"] + 3 * (sp["bb"] + sp["hbp"]) - 2 * sp["k"]) / sp["ip"] + p["cfip"]
            fip_ra9 = fip * p["ra_per_er"]
            fip_pooled = (fip_ra9 * sp["ip"] + m9 * prior_ip) / (sp["ip"] + prior_ip)
            est = (1 - p["fip_weight"]) * ra9 + p["fip_weight"] * fip_pooled
        gs = sp.get("gs", 0.0)
        length = (sp["ip"] + p["starter_prior_gs"] * p["starter_prior_len"]) / (gs + p["starter_prior_gs"]) \
            if gs > 0 else p["starter_prior_len"]
        f = min(length, 9.0) / 9.0
        mult = (1 - f) + f * (est / opp_prevention)
        lo, hi = p["starter_mult_bounds"]
        return max(lo, min(hi, mult))

    def means(self, home: str, away: str, venue=None, home_sp: dict | None = None,
              away_sp: dict | None = None) -> tuple[float, float]:
        m = self.m
        off_h, off_a = self.off.get(home, m), self.off.get(away, m)
        def_h, def_a = self.dfn.get(home, m), self.dfn.get(away, m)
        pf = self.park.get(venue if venue is not None else self.team_home_venue.get(home), 1.0)
        mu_h = m * (off_h / m) * (def_a / m) * pf * self.home_f
        mu_a = m * (off_a / m) * (def_h / m) * pf * self.away_f
        mu_h *= self.starter_multiplier(away_sp, def_a)   # the away starter faces the home lineup
        mu_a *= self.starter_multiplier(home_sp, def_h)
        return mu_h, mu_a

    def joint(self, home: str, away: str, venue=None, home_sp=None, away_sp=None) -> tuple[dict, float, float]:
        mu_h, mu_a = self.means(home, away, venue, home_sp, away_sp)
        support = int(self.p["support"])
        while True:  # widen the grid until the omitted tail mass is below 1e-6 (recipes §5)
            try:
                return no_tie(shared_gamma_joint(mu_h, mu_a, self.shape, support)), mu_h, mu_a
            except ValueError as exc:
                if "support" not in str(exc) or support >= 160:
                    raise
                support *= 2

    def predict(self, home: str, away: str, line: float | None, venue=None, home_sp=None, away_sp=None) -> dict:
        joint, mu_h, mu_a = self.joint(home, away, venue, home_sp, away_sp)
        return {"mu_home": mu_h, "mu_away": mu_a, "shape": self.shape, **queries(joint, line)}


def params_sha(priors: dict = PRIORS) -> str:
    return hashlib.sha256(json.dumps(priors, sort_keys=True).encode()).hexdigest()[:16]


# --------------------------------------------------------------------------- shadow log

def append_row(path: Path, fields: list[str], row: dict) -> None:
    new = not path.exists()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        if new:
            w.writeheader()
        w.writerow({k: row.get(k, "") for k in fields})


def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def parse_iso(s: str) -> dt.datetime:
    t = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    if t.tzinfo is None:
        raise ValueError("timestamp needs a timezone")
    return t


def shadow(src: Source, pk: int, line: float, card: str, now: dt.datetime, log: Path) -> dict:
    feed = src.feed(pk)
    gd = feed["gameData"]
    state = gd.get("status", {}).get("abstractGameState")
    start = parse_iso(gd["datetime"]["dateTime"])
    if state != "Preview" or now >= start:
        raise SystemExit(f"STARTED_OR_NOT_PREGAME — no shadow row for {pk} (state {state}, start {start:%Y-%m-%dT%H:%MZ})")
    if any(r["game_pk"] == str(pk) and r["line_total"] == str(line) for r in read_rows(log)):
        raise SystemExit(f"error: game {pk} line {line} is already frozen in {log}; rows are never replaced")
    official = gd["datetime"].get("officialDate") or start.date().isoformat()
    season = int(official[:4])
    games = src.season_games(season, official)
    rt = Ratings(games)
    home, away = gd["teams"]["home"]["name"], gd["teams"]["away"]["name"]
    venue = gd.get("venue", {}).get("id")
    pp = gd.get("probablePitchers", {}) or {}
    hid, aid = (pp.get("home") or {}).get("id"), (pp.get("away") or {}).get("id")
    hsp = src.pitcher(hid, season, official) if hid else None
    asp = src.pitcher(aid, season, official) if aid else None
    a1 = rt.predict(home, away, line, venue, hsp, asp)
    b = a0(games, line)
    row = {"row_id": f"{pk}-{line}", "frozen_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "card": card,
           "game_pk": pk, "official_date": official, "start_utc": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
           "home": home, "away": away, "venue_id": venue, "home_sp_id": hid or "", "away_sp_id": aid or "",
           "model_version": MODEL_VERSION, "params_sha": params_sha(), "n_prior_games": len(games),
           "mu_home": f"{a1['mu_home']:.4f}", "mu_away": f"{a1['mu_away']:.4f}", "shape": f"{a1['shape']:.3f}",
           "line_total": line}
    for pre, q in (("a1_", a1), ("a0_", b)):
        for k in ("p_over", "p_push", "p_under", "p_home_win", "p_home_m15", "p_away_m15"):
            row[pre + k] = f"{q[k]:.4f}"
    append_row(log, LOG_FIELDS, row)
    return row


def settle(src: Source, log: Path, results: Path, now: dt.datetime) -> list[dict]:
    done = {r["game_pk"] for r in read_rows(results)}
    added = []
    for pk in sorted({r["game_pk"] for r in read_rows(log)} - done):
        feed = src.feed(int(pk))
        if feed["gameData"].get("status", {}).get("abstractGameState") != "Final":
            continue
        ls = feed.get("liveData", {}).get("linescore", {})
        teams = ls.get("teams", {})
        row = {"game_pk": pk, "home_runs": teams.get("home", {}).get("runs"), "away_runs": teams.get("away", {}).get("runs"),
               "innings": len(ls.get("innings", [])), "settled_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
               "source": FEED_URL.format(pk=pk)}
        if row["home_runs"] is None or row["away_runs"] is None:
            continue
        append_row(results, RESULT_FIELDS, row)
        added.append(row)
    return added


def score(log: Path, results: Path) -> dict:
    res = {r["game_pk"]: r for r in read_rows(results)}
    acc = defaultdict(lambda: {"a1": 0.0, "a0": 0.0, "n": 0})
    seen = set()   # the side and run-line targets are one per game, however many total lines were frozen
    for r in read_rows(log):
        f = res.get(r["game_pk"])
        if not f:
            continue
        h, a = int(f["home_runs"]), int(f["away_runs"])
        t, line = h + a, float(r["line_total"])
        targets = {}
        if r["game_pk"] not in seen:
            seen.add(r["game_pk"])
            targets = {"home_win": (h > a, "p_home_win"), "home_m15": (h - a >= 2, "p_home_m15"),
                       "away_m15": (a - h >= 2, "p_away_m15")}
        if t != line:
            targets["total_over"] = (t > line, "p_over")
        for name, (y, key) in targets.items():
            for m in ("a1", "a0"):
                p = float(r[f"{m}_{key}"])
                if key == "p_over":  # decisive probability when a push is possible
                    push = float(r[f"{m}_p_push"])
                    p = p / (1 - push) if push < 1 else 0.5
                acc[name][m] += (p - float(y)) ** 2
            acc[name]["n"] += 1
    return {k: {"n": v["n"], "a1_brier": v["a1"] / v["n"], "a0_brier": v["a0"] / v["n"],
                "a1_minus_a0": (v["a1"] - v["a0"]) / v["n"]} for k, v in acc.items() if v["n"]}


# --------------------------------------------------------------------------- historical validation

def validate(games: list[dict], from_date: str | None = None, to_date: str | None = None,
             lines=(6.5, 7.5, 8.5, 9.5, 10.5), min_prior: int = 300, boot: int = 2000, seed: int = 20260926) -> dict:
    """Rolling origin: each game is predicted from games strictly before its date. A1 is team-only."""
    by_date = defaultdict(list)
    for g in games:
        by_date[g["date"]].append(g)
    days = sorted(by_date)
    prior, per_day = [], []
    for d in days:
        eligible = len(prior) >= min_prior and (not from_date or d >= from_date) and (not to_date or d <= to_date)
        if eligible:
            rt = Ratings(prior)
            a0q = a0(prior, None)
            a0_over = {L: sum(x["hr"] + x["ar"] > L for x in prior) / len(prior) for L in lines}
            day = {"date": d, "n": 0, "a1": 0.0, "a0": 0.0}
            for g in by_date[d]:
                joint, _, _ = rt.joint(g["home"], g["away"], g["venue"])
                y = g["hr"] > g["ar"]
                t = g["hr"] + g["ar"]
                s1 = (queries(joint, None)["p_home_win"] - y) ** 2
                s0 = (a0q["p_home_win"] - y) ** 2
                for L in lines:
                    p1 = math.fsum(p for (h, a), p in joint.items() if h + a > L)
                    s1 += (p1 - (t > L)) ** 2
                    s0 += (a0_over[L] - (t > L)) ** 2
                day["n"] += 1
                day["a1"] += s1 / (1 + len(lines))
                day["a0"] += s0 / (1 + len(lines))
            per_day.append(day)
        prior += by_date[d]
    n = sum(d["n"] for d in per_day)
    if not n:
        return {"n_games": 0}
    diff = sum(d["a1"] - d["a0"] for d in per_day) / n
    rng = random.Random(seed)
    stats = []
    for _ in range(boot):
        s = [rng.choice(per_day) for _ in per_day]
        stats.append(sum(d["a1"] - d["a0"] for d in s) / sum(d["n"] for d in s))
    stats.sort()
    return {"n_games": n, "n_days": len(per_day), "targets": ["home_win"] + [f"over_{L}" for L in lines],
            "a1_brier": sum(d["a1"] for d in per_day) / n, "a0_brier": sum(d["a0"] for d in per_day) / n,
            "a1_minus_a0": diff, "ci95_day_block": [stats[int(0.025 * boot)], stats[int(0.975 * boot) - 1]],
            "model_version": MODEL_VERSION, "params_sha": params_sha(),
            "note": "A1 is team + park + home only (no starters). Mean Brier across the listed targets. "
                    "Negative a1_minus_a0 means A1 was better. Descriptive; not a promotion."}


# --------------------------------------------------------------------------- CLI

def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fixture-dir")
    ap.add_argument("--now")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pr = sub.add_parser("predict")
    pr.add_argument("--date", required=True)
    pr.add_argument("--home", required=True)
    pr.add_argument("--away", required=True)
    pr.add_argument("--venue-id", type=int)
    pr.add_argument("--total", type=float)
    pr.add_argument("--home-sp", type=int)
    pr.add_argument("--away-sp", type=int)
    sh = sub.add_parser("shadow")
    sh.add_argument("--gamepk", type=int, required=True)
    sh.add_argument("--total", type=float, required=True)
    sh.add_argument("--card", required=True, help="the card ID this shadow row follows (run after its freeze)")
    sh.add_argument("--log", default=str(SHADOW_DIR / "shadow_log.csv"))
    st = sub.add_parser("settle")
    st.add_argument("--log", default=str(SHADOW_DIR / "shadow_log.csv"))
    st.add_argument("--results", default=str(SHADOW_DIR / "shadow_results.csv"))
    sc = sub.add_parser("score")
    sc.add_argument("--log", default=str(SHADOW_DIR / "shadow_log.csv"))
    sc.add_argument("--results", default=str(SHADOW_DIR / "shadow_results.csv"))
    va = sub.add_parser("validate")
    va.add_argument("--season", type=int, required=True)
    va.add_argument("--from-date")
    va.add_argument("--to-date")
    va.add_argument("--out")
    args = ap.parse_args(argv)
    now = parse_iso(args.now) if args.now else dt.datetime.now(dt.timezone.utc)
    src = Source(args.fixture_dir)

    if args.cmd == "predict":
        season = int(args.date[:4])
        games = src.season_games(season, args.date)
        rt = Ratings(games)
        hsp = src.pitcher(args.home_sp, season, args.date) if args.home_sp else None
        asp = src.pitcher(args.away_sp, season, args.date) if args.away_sp else None
        q = rt.predict(args.home, args.away, args.total, args.venue_id, hsp, asp)
        b = a0(games, args.total)
        print(f"{MODEL_VERSION} — SHADOW, NOT A CARD INPUT. {len(games)} prior games; params {params_sha()}.")
        print(f"A1 means: home {q['mu_home']:.2f}, away {q['mu_away']:.2f}; shape {q['shape']:.2f}; "
              f"mean total {q['mean_total']:.2f} (A0 {b['mean_total']:.2f}).")
        for k in ("p_home_win", "p_home_m15", "p_away_m15", "p_over", "p_push", "p_under"):
            if k in q:
                print(f"  {k:<11} A1 {q[k]:.3f}   A0 {b[k]:.3f}")
        return 0
    if args.cmd == "shadow":
        row = shadow(src, args.gamepk, args.total, args.card, now, Path(args.log))
        print(f"Frozen shadow row {row['row_id']} at {row['frozen_at_utc']} for {row['away']} @ {row['home']}. "
              f"Blind: probabilities are in {Path(args.log).name}, read only at review. Never a card input.")
        return 0
    if args.cmd == "settle":
        added = settle(src, Path(args.log), Path(args.results), now)
        print(f"{len(added)} result(s) appended.")
        return 0
    if args.cmd == "score":
        s = score(Path(args.log), Path(args.results))
        if not s:
            print("No settled shadow rows yet.")
            return 0
        print("| Target | n | A1 Brier | A0 Brier | A1 − A0 |\n|---|---:|---:|---:|---:|")
        for k, v in s.items():
            print(f"| {k} | {v['n']} | {v['a1_brier']:.4f} | {v['a0_brier']:.4f} | {v['a1_minus_a0']:+.4f} |")
        print("\nDescriptive only (C-MLB-SHADOW). No promotion before the preregistered review.")
        return 0
    games = src.season_games(args.season, f"{args.season}-12-31")
    res = validate(games, args.from_date, args.to_date)
    text = json.dumps(res, indent=2)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
