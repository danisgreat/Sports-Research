"""Reference model, tiers and width floors for every game card (REFMODEL-v1 / WIDTH-v1).

Every card starts from a frozen reference, produced BEFORE the analyst writes a number:

    Tier A  an active experimental cycle release exists for the competition (``research/cycle_releases/CURRENT_RELEASES.csv``)
            -> the reference is the release's model, frozen by ``python -m ml pregame reference``
    Tier B  verified history in the learning store (>= 100 final events) or a TB-1-MD league constant
            -> the reference is TB-1-MD from a dated standings table, or the league-only baseline
    Tier C  anything else -> the league-only baseline from a family prior (widths widened), or NONE

    python -m ml reference tier   --competition "Basketball/NBA"
    python -m ml reference width  --competition "Basketball/NBA"
    python -m ml reference run    --game GAME.csv --lines LINES.csv [--standings STANDINGS.csv] [--params ROW]
                                  --confirm-no-outcome-seen        (tier B / C stages; tier A uses ``pregame reference``)

TB-1-MD is the hand team baseline of PROBABILITY_TOOLKIT section 4, computed here without hand-copying; the constants
below are checked against ``ml.config.TB1_VALIDATED`` by a test. Every probability comes from one coherent score grid
(``ml.core.distributions.ScoreGrid``), so winner, handicap and total rows share one distribution, pushes are explicit and
masses sum to one. Nothing in this module reads a price, a line movement or a model other than the frozen release.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy import stats

from ml.core.distributions import ScoreGrid

ROOT = Path(__file__).resolve().parents[1]
RELEASES = "research/cycle_releases/CURRENT_RELEASES.csv"
PARAMETERS = "research/competition_parameters/COMPETITION_PARAMETERS.csv"
STORE_EVENTS = "research/learning_store/EVENTS.csv"
CHOICE = "research/competition_parameters/REFERENCE_CHOICE.csv"
MIN_STORE_EVENTS = 100          # tier B by verified history
STALE_AFTER_DAYS = 400          # a parameter row older than this is printed STALE_PROFILE

# PROBABILITY_TOOLKIT section 4.3 (NBA..MLB) and the four P6 soccer rows. kind: normal (points) or poisson (goals).
TB1_MD = {
    "NBA": dict(k=2, sd_margin=15.1, sd_total=19.4, he=1.71, kind="normal", ot_fraction=5 / 48, ties="overtime"),
    "WNBA": dict(k=2, sd_margin=13.3, sd_total=19.5, he=1.73, kind="normal", ot_fraction=5 / 40, ties="overtime"),
    "NBL": dict(k=5, sd_margin=15.2, sd_total=18.7, he=1.57, kind="normal", ot_fraction=5 / 40, ties="overtime"),
    "NFL": dict(k=2, sd_margin=13.6, sd_total=13.4, he=1.95, kind="normal", ot_fraction=10 / 60, ties="overtime_nfl"),
    "AFL": dict(k=2, sd_margin=36.8, sd_total=29.1, he=6.57, kind="normal", ot_fraction=0.0, ties="draw"),
    "NRL": dict(k=2, sd_margin=19.9, sd_total=13.9, he=1.91, kind="normal", ot_fraction=0.0, ties="golden_point"),
    "Premier League": dict(k=2, he=0.30, kind="poisson"),
    "La Liga": dict(k=2, he=0.45, kind="poisson"),
    "Bundesliga": dict(k=2, he=0.32, kind="poisson"),
    "Serie A": dict(k=2, he=0.13, kind="poisson"),
    "Ligue 1": dict(k=2, he=0.34, kind="poisson"),
}
LEAGUE_KEYS = {"nba": "NBA", "wnba": "WNBA", "nbl": "NBL", "nfl": "NFL", "afl": "AFL", "nrl": "NRL", "premier league": "Premier League",
               "epl": "Premier League", "la liga": "La Liga", "laliga": "La Liga", "bundesliga": "Bundesliga", "serie a": "Serie A",
               "ligue 1": "Ligue 1"}
NOT_TB1 = ("NHL", "MLB")        # toolkit 4.3: TB-1-MD has no resolution there; use the release or the baseline

PARAM_FIELDS = ("row_type", "competition", "model_dir", "engine", "family", "usable", "dev_rows", "dev_seasons", "dev_first_date",
                "dev_last_date", "mean_total", "mean_home_margin", "home_win_rate", "raw_margin_sd", "raw_total_sd",
                "resid_margin_sd", "resid_total_sd", "z_margin_sd", "z_total_sd", "store_final_events", "store_extra_time_rate",
                "store_mean_total", "store_mean_home_margin", "store_margin_sd", "store_total_sd", "members", "flags", "evidence_class")


class ReferenceError_(ValueError):
    pass


def _rows(path) -> list[dict]:
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def league_key(competition: str) -> str | None:
    name = competition.split("/")[-1].strip().lower()
    return LEAGUE_KEYS.get(name)


# ------------------------------------------------------------------ tiers
def reference_choice(competition: str, root=ROOT) -> dict | None:
    """The reference model declared for a competition and season, with its development evidence (REFSEL-v1)."""
    path = Path(root) / CHOICE
    for r in (_rows(path) if path.exists() else []):
        if r["competition"] == competition:
            return r
    return None


def tier(competition: str, root=ROOT) -> dict:
    """Deterministic tier: A active release; B store history or a TB-1-MD constant; C otherwise.

    ``reference`` names the reference model the card starts from: the declared choice if there is one, else the active
    release (tier A), else TB-2-MD / TB-1-MD from a dated standings table (tier B), else the league-only baseline (tier C)."""
    root = Path(root)
    choice = reference_choice(competition, root)
    active = [r for r in _rows(root / RELEASES) if r["competition"] == competition] if (root / RELEASES).exists() else []
    if active:
        release = active[0]["active_experimental_release"]
        return dict(competition=competition, tier="A", basis=f"active release {release}", release=release,
                    reference=choice["reference_model"] if choice else "RELEASE:" + release)
    events = 0
    path = root / STORE_EVENTS
    if path.exists():
        with open(path, newline="", encoding="utf-8") as fh:
            events = sum(1 for r in csv.DictReader(fh) if r["competition"] == competition)
    key = league_key(competition)
    if events >= MIN_STORE_EVENTS:
        return dict(competition=competition, tier="B", basis=f"{events} verified final events in the learning store", release="",
                    reference=(choice["reference_model"] if choice else ("TB2-MD" if key in TB1_MD and default_form(key) == "additive" else
                                                                         "TB1-MD" if key in TB1_MD else "BASELINE_ONLY")))
    if key in TB1_MD:
        return dict(competition=competition, tier="B", basis=f"TB-1-MD league constants ({key})", release="",
                    reference=choice["reference_model"] if choice else ("TB2-MD" if default_form(key) == "additive" else "TB1-MD"))
    return dict(competition=competition, tier="C", basis=f"{events} store events; no TB-1-MD constants", release="", reference="BASELINE_ONLY")


# ------------------------------------------------------------------ competition rows and width floors
def parameter_rows(root=ROOT) -> list[dict]:
    path = Path(root) / PARAMETERS
    return _rows(path) if path.exists() else []


def parameter_row(competition: str, root=ROOT) -> dict | None:
    for r in parameter_rows(root):
        if r["row_type"] == "COMPETITION" and r["competition"] == competition:
            return r
    return None


def family_prior(competition: str, root=ROOT) -> dict | None:
    """The FAMILY_PRIOR row for a competition without its own usable row (basketball: by rule-set family)."""
    sport = competition.split("/")[0].strip().lower()
    last = competition.split("/")[-1].strip().lower()
    key = {"basketball": "BASKETBALL_NBA48" if last in ("nba", "nba g league") else "BASKETBALL_FIBA40",
           "american football": "AMERICAN_FOOTBALL", "college football": "AMERICAN_FOOTBALL", "canadian football": "AMERICAN_FOOTBALL",
           "afl": "AFL", "state level afl": "AFL", "rugby league": "RUGBY_LEAGUE", "soccer": "SOCCER", "baseball": "BASEBALL",
           "ice hockey": "ICE_HOCKEY"}.get(sport)
    if not key:
        return None
    for r in parameter_rows(root):
        if r["row_type"] == "FAMILY_PRIOR" and r["competition"] == "FAMILY_PRIOR:" + key:
            return r
    return None


def width_floor(competition: str, quantity: str, root=ROOT) -> dict:
    """The smallest SD a card may print for MARGIN or TOTAL without a written exception (WIDTH-v1).

    Own usable row first; else the family prior widened by 10% (tier C rule); else NONE. A residual SD is the spread left
    after team strength, so a card centred on team strength may not undercut it.
    """
    column = {"MARGIN": "resid_margin_sd", "TOTAL": "resid_total_sd"}[quantity.upper()]
    row = parameter_row(competition, root)
    if row and row["usable"] == "USABLE_DEVELOPMENT" and row[column]:
        return dict(floor=float(row[column]), basis="COMPETITION_ROW", competition=competition, row_evidence=row["evidence_class"])
    prior = family_prior(competition, root)
    if prior and prior[column]:
        return dict(floor=round(float(prior[column]) * 1.10, 2), basis="FAMILY_PRIOR_PLUS_10_PERCENT",
                    competition=prior["competition"], row_evidence=prior["evidence_class"])
    return dict(floor=None, basis="NONE", competition=competition, row_evidence="")


# ------------------------------------------------------------------ grids
def _normal_grid(mean_h: float, mean_a: float, sd_margin: float, sd_total: float) -> ScoreGrid:
    """Joint normal on integers from margin/total SDs with Cov(T, M) = 0 (TB-1 convention)."""
    var_x = (sd_total ** 2 + sd_margin ** 2) / 4
    cov_xy = (sd_total ** 2 - sd_margin ** 2) / 4
    cov = np.array([[var_x, cov_xy], [cov_xy, var_x]])
    return ScoreGrid.bivariate_normal(mean_h, mean_a, cov)


def _resolve(grid: ScoreGrid, ties: str, margin: float, sd_margin: float, ot_fraction: float) -> ScoreGrid:
    if ties in ("draw", ""):
        return grid
    # An extra period is an ot_fraction of a game: its margin has mean margin*f and SD sd*sqrt(f).
    p_home = float(stats.norm.cdf(margin * math.sqrt(max(ot_fraction, 1e-9)) / sd_margin))
    bonus = 3 if ties == "overtime_nfl" else 1
    return grid.resolve_ties(p_home, 0.0, bonus)


LM_PRIOR_WEIGHT = 200.0     # team-games of prior-season league mean blended into a young season's league mean (totals only)


def tb1_inputs(rows: list[dict], league: str, lm_prior: float | None = None) -> dict:
    """STANDINGS.csv -> means. Columns role,team,pf,pa,n; roles HOME, AWAY and LEAGUE (pf and n summed over all teams).

    The league mean per team-game enters only the expected TOTAL (it cancels from every margin), and in the first weeks it
    rests on a handful of games. With ``lm_prior`` (the competition's verified mean points per team-game) the mean is
    blended as (n * current + 200 * prior) / (n + 200) and the flag LM_PRIOR_BLEND is printed; the weight is a starting value
    and not a tuned parameter."""
    by = {r["role"].strip().upper(): r for r in rows}
    for role in ("HOME", "AWAY", "LEAGUE"):
        if role not in by:
            raise ReferenceError_(f"STANDINGS.csv needs a {role} row")
    league_games = float(by["LEAGUE"]["n"])
    if league_games <= 0:
        raise ReferenceError_("LEAGUE row needs a positive n (sum of team games)")
    current = float(by["LEAGUE"]["pf"]) / league_games
    blended = current if lm_prior is None else (league_games * current + LM_PRIOR_WEIGHT * lm_prior) / (league_games + LM_PRIOR_WEIGHT)
    return dict(lm=blended, lm_current=current, lm_prior=lm_prior, lm_blended=lm_prior is not None, league_team_games=league_games,
                home=dict(team=by["HOME"]["team"], pf=float(by["HOME"]["pf"]), pa=float(by["HOME"]["pa"]), n=float(by["HOME"]["n"])),
                away=dict(team=by["AWAY"]["team"], pf=float(by["AWAY"]["pf"]), pa=float(by["AWAY"]["pa"]), n=float(by["AWAY"]["n"])))


FORMS = ("average", "additive")


def tb1_centre(spec: dict, data: dict, neutral: bool = False, form: str = "average") -> dict:
    """Attack/defence ratings shrunk by k, expected total T and home margin M.

    ``average`` is PROBABILITY_TOOLKIT 4.2 as published (TB-1-MD): each side's expected score is the MEAN of its own attack
    and the opponent's defence, which halves the margin signal. ``additive`` (TB-2-MD) adds the two deviations from the league
    mean instead: score = attack + opponent defence - league mean, so margin = (net_home - net_away) + home edge. With no fitted
    parameter, the additive form's calibration slope on 3,603 NBA games (walk-forward, 2023-26) is 1.04 against 2.12 for the
    average form (2026-10-22 framework change, research/verification/framework_change_2026-10-22-2/).
    """
    if form not in FORMS:
        raise ReferenceError_(f"form must be one of {FORMS}")
    k, lm = spec["k"], data["lm"]
    def rate(side, key):
        return (data[side][key] + k * lm) / (data[side]["n"] + k)
    oh, dh, oa, da = rate("home", "pf"), rate("home", "pa"), rate("away", "pf"), rate("away", "pa")
    edge = 0.0 if neutral else spec["he"]
    if form == "average":
        total = (oh + da) / 2 + (oa + dh) / 2
        margin = ((oh - dh) - (oa - da)) / 2 + edge
    else:
        total = (oh + da - lm) + (oa + dh - lm)
        margin = (oh - dh) - (oa - da) + edge
    flags = []
    if min(data["home"]["n"], data["away"]["n"]) < 3:
        flags.append("TB1_EARLY_SEASON")
    return dict(total=total, margin=margin, flags=flags, form=form)


def price_rows(grid: ScoreGrid, lines: list[dict]) -> list[dict]:
    """Unconditional W/P/L and decisive p = W/(W+L) for winner, handicap and total rows from one grid."""
    out = []
    for row in lines:
        family, side = row["family"].strip().lower(), row["side"].strip().upper()
        if family == "winner":
            probs = grid.winner()
            if side not in ("HOME", "DRAW", "AWAY"):
                raise ReferenceError_(f"{row['label']}: winner side must be HOME, DRAW or AWAY")
            w = probs[("HOME", "DRAW", "AWAY").index(side)]
            push, loss = 0.0, 1 - w  # a draw loses a three-way winner row (THREE_WAY_DRAW_LOSES)
        elif family in ("handicap", "total"):
            m = getattr(grid, family)(float(row["line"]), side)
            w, push, loss = m.win, m.push, m.loss
        else:
            raise ReferenceError_(f"{row['label']}: only winner, handicap and total rows come from a grid")
        out.append(dict(label=row["label"], family=family, side=side, line=row.get("line", ""), w=round(w, 6), p=round(push, 6),
                        l=round(loss, 6), p_decisive=round(w / (w + loss), 4) if w + loss > 0 else ""))
    return out


def default_form(key: str) -> str:
    """TB-2-MD (additive) for points leagues, where it was tested; TB-1-MD (average) for goal leagues, whose P6 validation stands."""
    return "additive" if TB1_MD[key]["kind"] == "normal" else "average"


def tb1_grid(competition: str, data: dict, neutral: bool = False, form: str | None = None) -> tuple[ScoreGrid, dict]:
    key = league_key(competition)
    if key is None:
        raise ReferenceError_(f"{competition}: no TB-1-MD constants (tier C)")
    spec = TB1_MD[key]
    form = form or default_form(key)
    centre = tb1_centre(spec, data, neutral, form)
    mean_h, mean_a = (centre["total"] + centre["margin"]) / 2, (centre["total"] - centre["margin"]) / 2
    if spec["kind"] == "poisson":
        grid = ScoreGrid.poisson(max(mean_h, 0.05), max(mean_a, 0.05))
        sd_m = sd_t = float("nan")
    else:
        grid = _resolve(_normal_grid(mean_h, mean_a, spec["sd_margin"], spec["sd_total"]), spec["ties"], centre["margin"],
                        spec["sd_margin"], spec["ot_fraction"])
        sd_m, sd_t = spec["sd_margin"], spec["sd_total"]
    return grid, dict(centre, key=key, sd_margin=sd_m, sd_total=sd_t, he=spec["he"], k=spec["k"])


def baseline_grid(competition: str, root=ROOT) -> tuple[ScoreGrid, dict]:
    """League-only distribution (BASELINE_LEAGUE_V1 shape) from the competition's parameter row or its family prior."""
    row = parameter_row(competition, root)
    status = "COMPETITION_ROW"
    if not row or row["usable"] not in ("USABLE_DEVELOPMENT",):
        row, status = family_prior(competition, root), "FAMILY_PRIOR"
    if not row or not row["mean_total"]:
        raise ReferenceError_(f"{competition}: no usable parameter row or family prior")
    total, margin = float(row["mean_total"]), float(row["mean_home_margin"])
    mean_h, mean_a = (total + margin) / 2, (total - margin) / 2
    engine = row.get("engine", "")
    sport = competition.split("/")[0].strip().lower()
    if sport in ("soccer",) or "dixon" in engine:
        return ScoreGrid.poisson(max(mean_h, 0.05), max(mean_a, 0.05)), dict(status=status, source=row["competition"], flags=[])
    if sport in ("baseball", "ice hockey") or engine == "count":
        raise ReferenceError_(f"{competition}: BASELINE_UNAVAILABLE for a count sport from mean and SD alone; use `python -m ml baseline`")
    sd_m, sd_t = float(row["raw_margin_sd"]), float(row["raw_total_sd"])
    ties = "overtime" if sport == "basketball" else "overtime_nfl" if sport in ("american football", "college football", "canadian football") else "draw"
    ot = {"nba": 5 / 48}.get(competition.split("/")[-1].strip().lower(), 5 / 40) if sport == "basketball" else 10 / 60
    grid = _resolve(_normal_grid(mean_h, mean_a, sd_m, sd_t), ties, margin, sd_m, ot)
    stale = False
    last = row.get("dev_last_date", "")
    if last:
        stale = (datetime.now(timezone.utc).date() - datetime.fromisoformat(last).date()).days > STALE_AFTER_DAYS
    return grid, dict(status=status, source=row["competition"], flags=["STALE_PROFILE"] if stale else [])


# ------------------------------------------------------------------ dated standings from the ESPN site API
ESPN_STANDINGS = {"NBA": "basketball/nba", "WNBA": "basketball/wnba", "NBL": "basketball/nbl", "NFL": "football/nfl",
                  "AFL": "australian-football/afl", "NRL": "rugby-league/3", "Premier League": "soccer/eng.1", "La Liga": "soccer/esp.1",
                  "Bundesliga": "soccer/ger.1", "Serie A": "soccer/ita.1", "Ligue 1": "soccer/fra.1"}


def espn_standings(competition: str, cache: Path | None = None) -> tuple[list[dict], dict]:
    """Regular-season points for/against and games played per team (the keyless ESPN standings feed, SOURCES 2.1)."""
    import json
    import urllib.request
    key = league_key(competition)
    if key not in ESPN_STANDINGS:
        raise ReferenceError_(f"{competition}: no standings feed mapped")
    url = f"https://site.api.espn.com/apis/v2/sports/{ESPN_STANDINGS[key]}/standings"
    raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "SportsResearch standings read"}), timeout=60).read()
    receipt = dict(source_url=url, retrieved_at=datetime.now(timezone.utc).isoformat(), raw_sha256=_sha(raw), raw_bytes=len(raw))
    if cache is not None:
        Path(cache).mkdir(parents=True, exist_ok=True)
        (Path(cache) / (receipt["raw_sha256"] + ".json")).write_bytes(raw)
    out = []

    def walk(node):
        for e in node.get("standings", {}).get("entries", []):
            s = {x["name"]: x.get("value") for x in e["stats"]}
            games = s.get("gamesPlayed")
            if games is None:
                games = sum(s.get(k) or 0 for k in ("wins", "losses", "ties", "otLosses"))
            out.append(dict(team=e["team"]["displayName"], pf=float(s["pointsFor"]), pa=float(s["pointsAgainst"]), n=float(games)))
        for child in node.get("children", []):
            walk(child)

    walk(json.loads(raw))
    if not out:
        raise ReferenceError_(f"{competition}: the standings feed returned no teams")
    return out, receipt


def standings_csv(competition: str, home: str, away: str, cache: Path | None = None) -> tuple[bytes, dict]:
    """STANDINGS.csv (HOME, AWAY, LEAGUE rows) for ``run``. Team names must be ESPN's display names."""
    teams, receipt = espn_standings(competition, cache)
    by = {t["team"]: t for t in teams}
    for side, name in (("home", home), ("away", away)):
        if name not in by:
            import difflib
            near = difflib.get_close_matches(name, sorted(by), n=4, cutoff=0.3)
            raise ReferenceError_(f"{side} team {name!r} is not in the standings feed" + (f" (closest: {', '.join(near)})" if near else ""))
    rows = [dict(role="HOME", team=home, pf=by[home]["pf"], pa=by[home]["pa"], n=by[home]["n"]),
            dict(role="AWAY", team=away, pf=by[away]["pf"], pa=by[away]["pa"], n=by[away]["n"]),
            dict(role="LEAGUE", team="ALL", pf=sum(t["pf"] for t in teams), pa=sum(t["pa"] for t in teams), n=sum(t["n"] for t in teams))]
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=("role", "team", "pf", "pa", "n"), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode(), receipt


# ------------------------------------------------------------------ the tier B / C stage
def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run(game, lines, standings=None, *, confirmed=False, root=ROOT, now=None) -> dict:
    """Reference rows for tiers B and C from a dated standings table and/or the frozen competition row."""
    if not confirmed:
        raise ReferenceError_("pass --confirm-no-outcome-seen only if no live score, result or post-start report was opened")
    root = Path(root)
    g = _rows(game)
    if len(g) != 1:
        raise ReferenceError_("GAME.csv must hold exactly one event")
    g = g[0]
    for field in ("local_key", "competition", "home", "away", "scheduled_start"):
        if not g.get(field, "").strip():
            raise ReferenceError_(f"GAME.csv needs {field}")
    t = tier(g["competition"], root)
    if t["reference"].startswith("RELEASE:"):
        raise ReferenceError_(f"{g['competition']}: the declared reference is the release model ({t['basis']}): "
                              "run `python -m ml pregame reference`")
    lines_rows = _rows(lines)
    at = (now or datetime.now(timezone.utc)).isoformat()
    result = dict(local_key=g["local_key"], competition=g["competition"], tier=t["tier"], basis=t["basis"], generated_at=at,
                  scheduled_start=g["scheduled_start"], reference_id="NONE", status="", flags=[], rows=[], baseline_rows=[])
    inputs = [Path(game).read_bytes(), Path(lines).read_bytes()]
    # league-only baseline first (always attempted)
    try:
        bgrid, binfo = baseline_grid(g["competition"], root)
        result["baseline_rows"] = price_rows(bgrid, lines_rows)
        result["baseline_id"] = f"BASELINE_LEAGUE_V1:{binfo['status']}:{binfo['source']}"
        result["flags"] += binfo["flags"]
    except ReferenceError_ as exc:
        result["baseline_id"] = "BASELINE_UNAVAILABLE"
        result["flags"].append("BASELINE_UNAVAILABLE:" + str(exc)[:120])
    if standings is not None and league_key(g["competition"]) in TB1_MD:
        row = parameter_row(g["competition"], root)
        prior = None
        if row and TB1_MD[league_key(g["competition"])]["kind"] == "normal" and (row["store_mean_total"] or row["mean_total"]):
            prior = float(row["store_mean_total"] or row["mean_total"]) / 2
        data = tb1_inputs(_rows(standings), league_key(g["competition"]), prior)
        inputs.append(Path(standings).read_bytes())
        grid, info = tb1_grid(g["competition"], data, neutral=g.get("neutral", "").strip().lower() in ("1", "true", "yes"))
        result["rows"] = price_rows(grid, lines_rows)
        result.update(reference_id=("TB2-MD:" if info["form"] == "additive" else "TB1-MD:") + info["key"], status="EXECUTED", centre=dict(total=round(info["total"], 2), margin=round(info["margin"], 2)))
        untested = ["TB2_NOT_TESTED_FOR_COMPETITION"] if info["form"] == "additive" and reference_choice(g["competition"], root) is None else []
        key_numbers = ["KEY_NUMBERS_NOT_MODELLED"] if league_key(g["competition"]) == "NFL" else []     # margins 3 and 7: SIMULATION_PROTOCOL
        result["flags"] += untested + key_numbers + info["flags"] + (["LM_PRIOR_BLEND"] if data["lm_blended"] and LM_PRIOR_WEIGHT / (data["league_team_games"] + LM_PRIOR_WEIGHT) > 0.05 else [])
    elif standings is not None:
        result["status"] = "NOT_RUN_NO_TB1_CONSTANTS"
        result["flags"].append("NO_TB1_MD_CONSTANTS_FOR_COMPETITION")
    elif result["baseline_rows"]:
        result.update(rows=result["baseline_rows"], reference_id=result["baseline_id"], status="BASELINE_ONLY")
    else:
        result["status"] = "NOT_AVAILABLE"
    result["inputs_sha256"] = _sha(b"".join(inputs))
    return result


def markdown(result: dict) -> str:
    head = (f"**Reference (REFMODEL-v1, frozen before this card):** `{result['status'] or 'NOT_AVAILABLE'}` · tier {result['tier']} "
            f"({result['basis']}) · `{result['reference_id']}` · generated {result['generated_at']}")
    if result.get("flags"):
        head += "\n\nFlags: " + "; ".join(result["flags"])
    if not result["rows"]:
        return head + "\n\nNo reference probabilities: the card prices its own distribution and prints NONE in the reference column.\n"
    base = {r["label"]: r for r in result["baseline_rows"]}
    lines = ["| Contract | Reference p | W / P / L | League baseline p |", "|---|---:|---|---:|"]
    for r in result["rows"]:
        b = base.get(r["label"])
        lines.append(f"| {r['label']} | {r['p_decisive']} | {r['w']:.4f} / {r['p']:.4f} / {r['l']:.4f} | {b['p_decisive'] if b else 'missing'} |")
    centre = result.get("centre")
    extra = f"\n\nTB-1-MD centre: total {centre['total']}, home margin {centre['margin']}." if centre else ""
    return head + extra + "\n\n" + "\n".join(lines) + "\n\nThe analyst starts from these numbers; every departure goes in the adjustment ledger.\n"


def rows_csv(result: dict) -> bytes:
    fields = ("local_key", "label", "family", "side", "line", "reference_id", "reference_p", "w", "p", "l", "baseline_p")
    base = {r["label"]: r for r in result["baseline_rows"]}
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for r in result["rows"]:
        b = base.get(r["label"])
        writer.writerow(dict(local_key=result["local_key"], label=r["label"], family=r["family"], side=r["side"], line=r["line"],
                             reference_id=result["reference_id"], reference_p=r["p_decisive"], w=r["w"], p=r["p"], l=r["l"],
                             baseline_p=b["p_decisive"] if b else "MISSING:" + result["baseline_id"]))
    return out.getvalue().encode()


def write_receipt(result: dict, root=ROOT) -> Path:
    stamp = datetime.fromisoformat(result["generated_at"]).strftime("%Y%m%dT%H%M%S%fZ")
    folder = Path(root) / "research" / "pregame" / result["local_key"]
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{stamp}_REFERENCE_ROWS.csv"
    path.write_bytes(rows_csv(result))
    meta = folder / f"{stamp}_REFERENCE.csv"
    fields = ("local_key", "status", "tier", "basis", "reference_id", "baseline_id", "generated_at", "scheduled_start", "inputs_sha256",
              "rows_sha256", "flags")
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerow(dict(local_key=result["local_key"], status=result["status"] or "NOT_AVAILABLE", tier=result["tier"], basis=result["basis"],
                         reference_id=result["reference_id"], baseline_id=result.get("baseline_id", ""), generated_at=result["generated_at"],
                         scheduled_start=result["scheduled_start"], inputs_sha256=result["inputs_sha256"], rows_sha256=_sha(path.read_bytes()),
                         flags=";".join(result["flags"])))
    meta.write_bytes(out.getvalue().encode())
    return meta


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sd = sub.add_parser("standings", help="write STANDINGS.csv for a game from the ESPN standings feed")
    sd.add_argument("--competition", required=True)
    sd.add_argument("--home", required=True)
    sd.add_argument("--away", required=True)
    sd.add_argument("--out", type=Path, required=True)
    sd.add_argument("--cache", type=Path, help="folder OUTSIDE the repository for the raw feed body")
    tr = sub.add_parser("tier")
    tr.add_argument("--competition", required=True)
    wf = sub.add_parser("width")
    wf.add_argument("--competition", required=True)
    rn = sub.add_parser("run")
    rn.add_argument("--game", type=Path, required=True)
    rn.add_argument("--lines", type=Path, required=True)
    rn.add_argument("--standings", type=Path)
    rn.add_argument("--confirm-no-outcome-seen", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command == "tier":
            print(" ".join(f"{k}={v}" for k, v in tier(args.competition).items()))
        elif args.command == "standings":
            data, receipt = standings_csv(args.competition, args.home, args.away, args.cache)
            args.out.write_bytes(data)
            print(f"wrote {args.out}; source {receipt['source_url']} retrieved {receipt['retrieved_at']} raw sha256 {receipt['raw_sha256']}")
        elif args.command == "width":
            for q in ("MARGIN", "TOTAL"):
                print(q, " ".join(f"{k}={v}" for k, v in width_floor(args.competition, q).items()))
        else:
            result = run(args.game, args.lines, args.standings, confirmed=args.confirm_no_outcome_seen)
            receipt = write_receipt(result)
            print(markdown(result))
            print(f"receipt: {receipt.relative_to(ROOT).as_posix() if receipt.is_relative_to(ROOT) else receipt}")
    except (ReferenceError_, ValueError, KeyError) as exc:
        print(f"REFUSED: {exc}")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
