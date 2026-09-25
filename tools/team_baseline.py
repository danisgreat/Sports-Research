#!/usr/bin/env python3
"""TB-1 — the team-strength baseline (added 2026-09-25(e)).

Why. `BASELINE_P` (C-BASELINE-SKILL) knows only home/away, so a card that "beats the baseline"
has cleared a very low bar, and a card that departs from it has no team-aware anchor. TB-1 is a
leak-free, population-fitted baseline that knows each team's season-to-date scoring. Its resolution
was measured out of sample on field-owner seasons (research/team_baseline_2026-09-25e/README.md).
It is informative for results and margins in NBA, WNBA, NBL, AFL, NFL, NRL and EPL, and for NBA,
WNBA and NFL totals. It is uninformative for MLB and NHL (sides and totals) and for NBL, AFL, NRL and EPL
totals: those targets print `TB1_NO_RESOLUTION:<target>`, so no card leans on them.

TB-1 is NOT a forecast of the card and reads no odds or market material. It fits nothing from the
prediction logs; its two constants per league (shrink k and carry-over r) were chosen on earlier
field-owner seasons, which are population data, not the framework's own results.

Model:
- a team's points for / against per game = (season sum + k · anchor) / (games + k), where the anchor
  is the league mean plus r × last season's deviation (r = 0: shrink to the league mean);
- total_hat  = (home PF + away PA)/2 + (away PF + home PA)/2;
- margin_hat = ((home PF − PA) − (away PF − PA))/2 + the league home edge to date (0 at a neutral site);
- width = the running residual SD of the same predictor this season (the league reference width
  from BASE_RATES_REGISTER.md §7 until 20 games have been predicted).

Commands:
    python tools/team_baseline.py predict --league nbl --home "Brisbane Bullets" --away "Illawarra Hawks" \\
        --date 2026-09-25 --total 188.5 --home-line -1.5
    python tools/team_baseline.py predict --league mlb --home "Pittsburgh Pirates" --away "St. Louis Cardinals" \\
        --date 2026-09-24 --total 6.5 --home-line -1.5

The date is the event's venue-local date: only games completed before it are used. Standard library
only. Network: ESPN site API (no browser User-Agent) or MLB statsapi, cached under .cache/team_baseline/.
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import math
import os
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
CACHE = REPO / ".cache" / "team_baseline"

# League constants. k and r were chosen on earlier seasons (research/team_baseline_2026-09-25e);
# default SDs are the BASE_RATES_REGISTER.md §7 reference widths. "resolution" is the out-of-sample
# verdict per target: True = informative beyond the population rate, False = print TB1_NO_RESOLUTION.
#
# Out-of-sample Brier on the latest season (research/team_baseline_2026-09-25e/README.md):
#   league  P(home win) TB-1 v base   P(total > league mean) TB-1 v base
#   NBL     0.2234 v 0.2546           0.2464 v 0.2505
#   WNBA    0.2157 v 0.2564           0.2324 v 0.2575
#   NBA     0.2158 v 0.2480           0.2395 v 0.2487   (k chosen on the same season; flat for k 0–10)
#   EPL     0.2308 v 0.2469           0.2584 v 0.2502   (totals worse than the base rate)
#   NHL     0.2477 v 0.2503           0.2490 v 0.2502   (no resolution)
#   MLB     0.2480 v 0.2497           0.2491 v 0.2500   (no resolution)
#   NFL     0.2311 v 0.2516           0.2456 v 0.2540   (2025 season; k chosen on 2024)
#   AFL     0.2015 v 0.2491           0.2483 v 0.2545   (2026 season; k chosen on 2025)
#   NRL     0.2403 v 0.2529           0.2518 v 0.2550   (2026 season; total RMSE worse than the league mean)
# A target is marked as having resolution when TB-1's Brier is at least 3% below the base rate's
# and its RMSE is lower too.
LEAGUES = {
    "nba":  {"espn": "basketball/nba",  "kind": "normal",  "k": 2,  "r": 0.0,  "sd_total": 19.4, "sd_margin": 15.1,
             "resolution": {"margin": True, "total": True}},
    "wnba": {"espn": "basketball/wnba", "kind": "normal",  "k": 2,  "r": 0.75, "sd_total": 19.5, "sd_margin": 13.3,
             "resolution": {"margin": True, "total": True}},
    "nbl":  {"espn": "basketball/nbl",  "kind": "normal",  "k": 5,  "r": 0.0,  "sd_total": 18.7, "sd_margin": 15.2,
             "resolution": {"margin": True, "total": False}},
    "nhl":  {"espn": "hockey/nhl",      "kind": "hockey",  "k": 20, "r": 0.0,  "sd_total": 2.29, "sd_margin": 2.57,
             "resolution": {"margin": False, "total": False}},
    "epl":  {"espn": "soccer/eng.1",    "kind": "poisson", "k": 2,  "r": 0.0,  "sd_total": 1.61, "sd_margin": 1.51,
             "resolution": {"margin": True, "total": False}},
    "mlb":  {"statsapi": True,          "kind": "baseball", "k": 20, "r": 0.0, "sd_total": 4.50, "sd_margin": 4.57,
             "resolution": {"margin": False, "total": False}},
    "nfl":  {"espn": "football/nfl",    "kind": "normal", "k": 2, "r": 0.0, "sd_total": 13.4, "sd_margin": 13.6,
             "resolution": {"margin": True, "total": True}},
    "afl":  {"espn": "australian-football/afl", "kind": "normal", "k": 2, "r": 0.0, "sd_total": 29.1,
             "sd_margin": 36.8, "resolution": {"margin": True, "total": False}},
    "nrl":  {"espn": "rugby-league/3",  "kind": "normal", "k": 2, "r": 0.0, "sd_total": 13.9, "sd_margin": 19.9,
             "resolution": {"margin": True, "total": False},
             "scoreboard_from": "02-20"},   # the NRL team-schedule endpoint returns HTTP 500: read the scoreboard
}
MIN_GAMES = 3        # below this many games for either team the row is flagged TB1_EARLY_SEASON
RESID_MIN = 20       # predicted games needed before the running residual SD replaces the reference width


class InsufficientData(RuntimeError):
    """Too few completed games to form a baseline: the card prints TEAM_BASELINE_P: NOT_YET_DERIVED."""


# ------------------------------------------------------------------ maths


def normal_cdf(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def _pois(k: int, lam: float) -> float:
    return math.exp(-lam + k * math.log(lam) - math.lgamma(k + 1))


def team_means(total: float, margin: float) -> tuple[float, float]:
    """Split a total and a home margin into two Poisson means (goals)."""
    return max(0.05, (total + margin) / 2), max(0.05, (total - margin) / 2)


def poisson_win(lh: float, la: float, cap: int = 15) -> float:
    """P(home goals > away goals) for independent Poissons."""
    return sum(_pois(i, lh) * _pois(j, la) for i in range(cap) for j in range(i))


def poisson_draw(lh: float, la: float, cap: int = 15) -> float:
    return sum(_pois(i, lh) * _pois(i, la) for i in range(cap))


def poisson_total_over(mu: float, line: float, cap: int = 40) -> float:
    return sum(_pois(k, mu) for k in range(cap) if k > line + 1e-9)


# ------------------------------------------------------------------ season state


class SeasonState:
    """Running, leak-free team ratings for one season. add() games in date order; predict() before add()."""

    def __init__(self, prior: dict | None = None, k: float = 5, carry: float = 0.0,
                 sd_total: float | None = None, sd_margin: float | None = None):
        self.k, self.carry = k, carry
        self.prior = prior or {}
        self.pf = defaultdict(float)
        self.pa = defaultdict(float)
        self.n = defaultdict(int)
        self.games = 0
        self.points = 0.0
        self.edges = []
        self.home_wins = 0
        self.over_hits = []
        self.res_t, self.res_m = [], []
        self.totals, self.margins = [], []
        self.sd_total0, self.sd_margin0 = sd_total, sd_margin

    # league quantities, to date
    def n_games(self, team) -> int:
        return self.n[team]

    def n_league_games(self) -> int:
        return self.games

    def league_team_mean(self) -> float:
        if self.games >= 10:
            return self.points / (2 * self.games)
        return self.prior.get("__league_team_mean__", self.points / (2 * self.games) if self.games else 0.0)

    def league_total_mean(self) -> float:
        return 2 * self.league_team_mean()

    def home_edge(self, neutral: bool = False) -> float:
        if neutral or not self.edges:
            return 0.0 if neutral or not self.prior else self.prior.get("__home_edge__", 0.0)
        return sum(self.edges) / len(self.edges)

    def home_win_rate(self) -> float:
        return self.home_wins / self.games if self.games else 0.5

    def abs_margin_share(self, at_least: int) -> float:
        """Share of decided games won by at least `at_least` (running, this season). Used for the
        low-scoring sports, whose margins are far from normal (MLB: 27.6% of games are one-run games)."""
        dec = [abs(m) for m in self.margins if m != 0]
        if len(dec) < 30:
            return {1: 1.0, 2: 0.72, 3: 0.52}.get(at_least, 0.4)
        return sum(1 for m in dec if m >= at_least) / len(dec)

    def over_rate(self) -> float:
        return sum(self.over_hits) / len(self.over_hits) if self.over_hits else 0.5

    def resid_sd(self) -> tuple[float, float]:
        def rms(xs):
            return math.sqrt(sum(x * x for x in xs) / len(xs))
        if len(self.res_m) >= RESID_MIN:
            return rms(self.res_m), rms(self.res_t)
        if self.sd_margin0 and self.sd_total0:
            return self.sd_margin0, self.sd_total0
        if len(self.margins) >= 10:
            mm, mt = sum(self.margins) / len(self.margins), sum(self.totals) / len(self.totals)
            return (math.sqrt(sum((x - mm) ** 2 for x in self.margins) / len(self.margins)),
                    math.sqrt(sum((x - mt) ** 2 for x in self.totals) / len(self.totals)))
        return 1.0, 1.0

    # ratings
    def _rating(self, team) -> tuple[float, float]:
        lm = self.league_team_mean()
        dev = self.prior.get(team)
        a_pf = lm + (self.carry * dev[0] if dev else 0.0)
        a_pa = lm + (self.carry * dev[1] if dev else 0.0)
        n = self.n[team]
        return (self.pf[team] + self.k * a_pf) / (n + self.k) if n + self.k else lm, \
               (self.pa[team] + self.k * a_pa) / (n + self.k) if n + self.k else lm

    def predict(self, home, away, neutral: bool = False) -> dict:
        hpf, hpa = self._rating(home)
        apf, apa = self._rating(away)
        total = (hpf + apa) / 2 + (apf + hpa) / 2
        margin = ((hpf - hpa) - (apf - apa)) / 2 + self.home_edge(neutral)
        return {"total": total, "margin": margin, "n_home": self.n[home], "n_away": self.n[away]}

    def add(self, g: dict) -> None:
        h, a, hs, as_ = g["home"], g["away"], float(g["hs"]), float(g["as"])
        if self.n[h] >= 1 and self.n[a] >= 1 and self.games >= 10:
            p = self.predict(h, a, neutral=g.get("neutral", False))
            self.res_t.append(hs + as_ - p["total"])
            self.res_m.append(hs - as_ - p["margin"])
        if self.games:
            self.over_hits.append(1 if hs + as_ > self.league_total_mean() else 0)
        self.pf[h] += hs
        self.pa[h] += as_
        self.pf[a] += as_
        self.pa[a] += hs
        self.n[h] += 1
        self.n[a] += 1
        self.games += 1
        self.points += hs + as_
        self.home_wins += 1 if hs > as_ else 0
        if not g.get("neutral", False):
            self.edges.append(hs - as_)
        self.totals.append(hs + as_)
        self.margins.append(hs - as_)

    def final_ratings(self) -> dict:
        """Each team's shrunk PF/PA deviation from the league mean, for next season's carry-over."""
        lm = self.league_team_mean()
        out = {t: (self._rating(t)[0] - lm, self._rating(t)[1] - lm) for t in self.n}
        out["__league_team_mean__"] = lm
        out["__home_edge__"] = self.home_edge()
        return out


# ------------------------------------------------------------------ data adapters


def _get_json(url: str, ttl: float | None = 3600) -> dict:
    """Cached GET. ttl None = never refetch (a scoreboard for a day that is over does not change)."""
    CACHE.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha1(url.encode()).hexdigest()
    path = CACHE / f"{key}.json"
    if path.exists() and (ttl is None or (dt.datetime.now().timestamp() - path.stat().st_mtime) < ttl):
        return json.loads(path.read_text(encoding="utf-8"))
    req = urllib.request.Request(url, headers={"Accept-Encoding": "gzip"})  # no browser UA (ESPN lane rule)
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    data = json.loads(raw.decode("utf-8"))
    path.write_text(json.dumps(data), encoding="utf-8")
    return data


def espn_teams(path: str) -> dict:
    d = _get_json(f"https://site.api.espn.com/apis/site/v2/sports/{path}/teams")
    out = {}
    for t in d["sports"][0]["leagues"][0]["teams"]:
        t = t["team"]
        out[t["id"]] = {k: t.get(k, "") for k in ("displayName", "shortDisplayName", "abbreviation", "location", "name")}
    return out


def espn_season_year(path: str, team_id) -> int | None:
    """ESPN's label for the current season (NBA/NBL use the END year, e.g. 2026-27 = 2027; WNBA the calendar year)."""
    try:
        d = _get_json(f"https://site.api.espn.com/apis/site/v2/sports/{path}/teams/{team_id}/schedule")
        return int(d.get("requestedSeason", {}).get("year") or d.get("season", {}).get("year"))
    except Exception:  # noqa: BLE001
        return None


def espn_games(path: str, team_ids, season: int | None = None) -> list[dict]:
    """Completed regular-season games of the listed teams (their union is the league when all teams are listed)."""
    seen, out = set(), []
    # Soccer schedules carry no regular-season type on ESPN, so they are read without the filter.
    stypes = (None,) if path.startswith("soccer/") else (2,)
    for tid in team_ids:
        for stype in stypes:
            url = f"https://site.api.espn.com/apis/site/v2/sports/{path}/teams/{tid}/schedule"
            params = ([f"seasontype={stype}"] if stype else []) + ([f"season={season}"] if season else [])
            if params:
                url += "?" + "&".join(params)
            try:
                d = _get_json(url)
            except Exception:  # noqa: BLE001 - a missing season page is simply no games
                continue
            for ev in d.get("events", []):
                comp = ev["competitions"][0]
                if not comp.get("status", {}).get("type", {}).get("completed") or ev["id"] in seen:
                    continue
                cps = comp.get("competitors", [])
                h = next((c for c in cps if c.get("homeAway") == "home"), None)
                a = next((c for c in cps if c.get("homeAway") == "away"), None)
                if not h or not a:
                    continue
                try:
                    hs = float(h["score"]["value"] if isinstance(h.get("score"), dict) else h["score"])
                    as_ = float(a["score"]["value"] if isinstance(a.get("score"), dict) else a["score"])
                except (KeyError, TypeError, ValueError):
                    continue
                seen.add(ev["id"])
                out.append({"date": ev["date"], "home": h["team"]["id"], "away": a["team"]["id"], "hs": hs, "as": as_,
                            "neutral": bool(comp.get("neutralSite", False))})
    return sorted(out, key=lambda g: g["date"])


def espn_scoreboard_games(path: str, start: str, end: str) -> tuple[list[dict], dict]:
    """Completed games from the day-by-day scoreboard (one date per call; ESPN rejects date ranges).
    Used where the team-schedule endpoint fails (NRL returns HTTP 500 on 2026-09-25). Days more than
    two days old are cached permanently. Returns (games, teams)."""
    d0 = dt.date.fromisoformat(start)
    d1 = dt.date.fromisoformat(end)
    today = dt.date.today()
    games, teams, seen = [], {}, set()
    day = d0
    while day <= d1:
        url = f"https://site.api.espn.com/apis/site/v2/sports/{path}/scoreboard?dates={day:%Y%m%d}"
        try:
            data = _get_json(url, ttl=None if (today - day).days > 2 else 1800)
        except Exception:  # noqa: BLE001 - a failed day is skipped and reported by the count
            day += dt.timedelta(days=1)
            continue
        for ev in data.get("events", []):
            comp = ev["competitions"][0]
            cps = comp.get("competitors", [])
            for c in cps:
                t = c["team"]
                teams[t["id"]] = {k: t.get(k, "") for k in ("displayName", "shortDisplayName", "abbreviation",
                                                              "location", "name")}
            if not ev.get("status", {}).get("type", {}).get("completed") or ev["id"] in seen:
                continue
            h = next((c for c in cps if c.get("homeAway") == "home"), None)
            a = next((c for c in cps if c.get("homeAway") == "away"), None)
            if not h or not a:
                continue
            try:
                hs, as_ = float(h["score"]), float(a["score"])
            except (KeyError, TypeError, ValueError):
                continue
            seen.add(ev["id"])
            games.append({"date": ev["date"], "home": h["team"]["id"], "away": a["team"]["id"], "hs": hs, "as": as_,
                          "neutral": bool(comp.get("neutralSite", False))})
        day += dt.timedelta(days=1)
    return sorted(games, key=lambda g: g["date"]), teams


def mlb_games(start: str, end: str) -> tuple[list[dict], dict]:
    d = _get_json(f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&startDate={start}&endDate={end}&gameType=R")
    games, names = [], {}
    for day in d.get("dates", []):
        for g in day.get("games", []):
            names[g["teams"]["home"]["team"]["id"]] = g["teams"]["home"]["team"]["name"]
            names[g["teams"]["away"]["team"]["id"]] = g["teams"]["away"]["team"]["name"]
            if g["status"].get("codedGameState") != "F":
                continue
            a, h = g["teams"]["away"].get("score"), g["teams"]["home"].get("score")
            if a is None or h is None:
                continue
            games.append({"date": g["gameDate"], "home": g["teams"]["home"]["team"]["id"],
                          "away": g["teams"]["away"]["team"]["id"], "hs": h, "as": a, "neutral": False})
    return sorted(games, key=lambda x: x["date"]), {k: {"displayName": v} for k, v in names.items()}


def match_team(name: str, teams: dict):
    n = name.strip().lower()
    for tid, t in teams.items():
        if any(n == str(v).lower() for v in t.values() if v):
            return tid
    hits = [tid for tid, t in teams.items() if any(n in str(v).lower() or str(v).lower() in n
                                                     for v in (t.get("displayName"), t.get("location")) if v)]
    if len(hits) == 1:
        return hits[0]
    raise ValueError(f"team {name!r} not matched uniquely ({len(hits)} candidates)")


# ------------------------------------------------------------------ contract probabilities


def contract_probs(league: str, pred: dict, sd_margin: float, sd_total: float, total_line=None, home_line=None,
                   state: "SeasonState | None" = None) -> dict:
    """P(home win), P(away win), [P(draw)], P(Over/Under total_line), P(home covers home_line) from TB-1.
    Baseball and hockey handicaps use the season's running share of wins by >= k (their margins are
    not normal); every other margin is read off the fitted distribution."""
    sys.path.insert(0, str(HERE))
    import card_math as cm  # noqa: E402
    kind = LEAGUES[league]["kind"]
    out = {}
    m, t = pred["margin"], pred["total"]
    if kind == "poisson":
        lh, la = team_means(t, m)
        out["home_win"], out["draw"] = poisson_win(lh, la), poisson_draw(lh, la)
        out["away_win"] = 1 - out["home_win"] - out["draw"]
        tot = cm.Dist("poisson", mean=lh + la)
        mar = cm.Dist("skellam", mu=lh, mu_opp=la)
    else:
        # No full-game tie: basketball, MLB and NHL cannot tie, and overtime/golden point settles almost
        # every NFL and NRL game (draw rates 0–0.5% in 2024–26; AFL 0.5–1.5%), so TB-1 ignores the draw.
        no_zero = kind in ("normal", "baseball", "hockey")
        mar = cm.Dist("normal", mean=m, sd=sd_margin, no_zero=no_zero)
        if kind == "baseball" and sd_total * sd_total > t:
            tot = cm.Dist("negbin", mean=t, sd=sd_total)
        elif kind == "hockey":
            tot = cm.Dist("poisson", mean=t)
        else:
            tot = cm.Dist("normal", mean=t, sd=sd_total)
        out["home_win"] = cm.p_over(mar, 0)
        out["away_win"] = 1 - out["home_win"]
    if total_line is not None:
        out[f"over_{total_line:g}"] = cm.p_over(tot, total_line)
        out[f"under_{total_line:g}"] = cm.p_under(tot, total_line)
        out[f"push_{total_line:g}"] = cm.p_push(tot, total_line)
    if home_line is not None:
        if kind in ("baseball", "hockey") and abs(home_line - round(home_line)) > 1e-9:
            need = math.floor(abs(home_line)) + 1          # −1.5 needs a 2+ win
            share = state.abs_margin_share(need) if state else {2: 0.72, 3: 0.52}.get(need, 0.4)
            if home_line < 0:
                w = out["home_win"] * share
            else:
                w = 1 - out["away_win"] * share
            pu = 0.0
        else:
            w, pu = cm.p_cover(mar, home_line)
        out[f"home_{home_line:+g}"] = w
        out[f"away_{-home_line:+g}"] = 1 - w - pu
        out[f"push_{home_line:+g}"] = pu
    return out


def predict_event(league: str, home: str, away: str, date: str, total_line=None, home_line=None,
                  neutral: bool = False) -> dict:
    cfg = LEAGUES[league]
    cutoff = date  # games strictly before the venue-local event date
    if cfg.get("statsapi"):
        year = int(date[:4])
        games, teams = mlb_games(f"{year}-03-01", date)
        prev, _ = mlb_games(f"{year - 1}-03-01", f"{year - 1}-11-30") if cfg["r"] else ([], {})
    elif cfg.get("scoreboard_from"):
        start = f"{date[:4]}-{cfg['scoreboard_from']}"
        last = (dt.date.fromisoformat(date) - dt.timedelta(days=1)).isoformat()
        games, teams = espn_scoreboard_games(cfg["espn"], start, last)
        prev = []
    else:
        teams = espn_teams(cfg["espn"])
        games = espn_games(cfg["espn"], list(teams))
        prev = []
        if cfg["r"]:
            year = espn_season_year(cfg["espn"], next(iter(teams)))
            prev = espn_games(cfg["espn"], list(teams), season=year - 1) if year else []
    hid, aid = match_team(home, teams), match_team(away, teams)
    games = [g for g in games if g["date"][:10] < cutoff]
    prior = None
    if prev:
        ps = SeasonState(k=cfg["k"])
        for g in prev:
            ps.add(g)
        prior = ps.final_ratings()
    st = SeasonState(prior=prior, k=cfg["k"], carry=cfg["r"], sd_total=cfg["sd_total"], sd_margin=cfg["sd_margin"])
    for g in games:
        st.add(g)
    if st.n_league_games() < 10 and not prior:
        raise InsufficientData(f"TB1 NOT_YET_DERIVED: {st.n_league_games()} completed league games before {date} "
                               f"and no prior season; print TEAM_BASELINE_P: NOT_YET_DERIVED")
    pred = st.predict(hid, aid, neutral=neutral)
    sd_m, sd_t = st.resid_sd()
    flags = []
    if min(pred["n_home"], pred["n_away"]) < MIN_GAMES:
        flags.append("TB1_EARLY_SEASON")
    for target, ok in cfg["resolution"].items():
        if not ok:
            flags.append(f"TB1_NO_RESOLUTION:{target}")
    return {"league": league, "home": teams[hid].get("displayName"), "away": teams[aid].get("displayName"),
            "date": date, "games_used": len(games), "n_home": pred["n_home"], "n_away": pred["n_away"],
            "total_hat": pred["total"], "margin_hat": pred["margin"], "sd_total": sd_t, "sd_margin": sd_m,
            "league_total_mean": st.league_total_mean(), "home_edge": st.home_edge(neutral),
            "probs": contract_probs(league, pred, sd_m, sd_t, total_line, home_line, state=st), "flags": flags,
            "k": cfg["k"], "carry_r": cfg["r"]}


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("predict")
    p.add_argument("--league", required=True, choices=sorted(LEAGUES))
    p.add_argument("--home", required=True)
    p.add_argument("--away", required=True)
    p.add_argument("--date", required=True, help="venue-local event date YYYY-MM-DD; only earlier games are used")
    p.add_argument("--total", type=float)
    p.add_argument("--home-line", type=float, help="the home side's handicap, e.g. -1.5")
    p.add_argument("--neutral", action="store_true")
    p.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    try:
        r = predict_event(args.league, args.home, args.away, args.date, args.total, args.home_line, args.neutral)
    except InsufficientData as exc:
        print(exc)
        return 2
    if args.json:
        print(json.dumps(r, indent=2))
        return 0
    print(f"TB-1 {r['league'].upper()} {r['away']} @ {r['home']} ({r['date']}; {r['games_used']} prior league games; "
          f"home {r['n_home']} / away {r['n_away']} team games; k {r['k']}, carry r {r['carry_r']})")
    print(f"  total_hat {r['total_hat']:.2f} (league mean {r['league_total_mean']:.2f}, width {r['sd_total']:.2f}); "
          f"home margin_hat {r['margin_hat']:+.2f} (home edge {r['home_edge']:+.2f}, width {r['sd_margin']:.2f})")
    for k, v in r["probs"].items():
        print(f"  TEAM_BASELINE_P {k}: {v:.4f}")
    if r["flags"]:
        print("  flags: " + " ".join(r["flags"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
