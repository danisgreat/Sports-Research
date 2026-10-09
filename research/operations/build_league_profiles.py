"""Build runtime/config/leagues/<sport>.json from the archive (DST-03, DST-13).

  python -B -m research.operations.build_league_profiles [--out DIR] [--seasons 3] [--min-games 100]

For every listed competition the most recent N seasons with at least `min-games` regular-season
games supply the scoring level, home advantage, dispersion and sport-specific extras (overtime,
shootout and one-run shares). Every input file is recorded with its SHA-256, so the profile can be
reproduced. Competitions whose archive folders are blank (B.LEAGUE, KBL, CBA) get no profile.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats

from research.src import archive_std

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "runtime/config/leagues"
BUILDER = "league-profile-v1"
GROUPS = {
    "basketball": ("Basketball", ["NBA", "WNBA", "NBL", "EuroLeague", "Greek Basket League", "BSL", "Austria Basketball Bundesliga"]),
    "ice_hockey": ("Ice Hockey", ["NHL", "Metal Ligaen"]),
    "baseball": ("Baseball", ["MLB", "NPB", "KBO"]),
    "rugby_league": ("Rugby League", ["NRL"]),
    "afl": ("AFL", ["AFL", "AFLW"]),
    "american_football": ("American Football", ["NFL"]),
}


# Plausibility gates. A profile that fails them is not published; it is listed under "excluded"
# with the reason, so a corrupted or duplicated archive folder can never become a prior.
LIMITS = {
    "basketball": {"team_mean": (55.0, 130.0), "home_advantage": (-1.0, 5.0), "total_sd": (10.0, 30.0), "overtime_share": (0.01, 0.10)},
    "ice_hockey": {"team_mean": (1.5, 4.5), "home_advantage": (-0.3, 0.6), "total_sd": (1.5, 3.2)},
    "baseball": {"team_mean": (2.5, 6.5), "home_advantage": (-0.6, 0.6), "total_sd": (3.0, 6.0)},
    "rugby_league": {"team_mean": (12.0, 40.0), "home_advantage": (-1.0, 6.0), "total_sd": (8.0, 22.0)},
    "afl": {"team_mean": (25.0, 120.0), "home_advantage": (-2.0, 15.0), "total_sd": (15.0, 40.0)},
    "american_football": {"team_mean": (15.0, 30.0), "home_advantage": (-1.0, 5.0), "total_sd": (8.0, 18.0)},
    "soccer": {"team_mean": (0.8, 2.2), "home_advantage": (-0.1, 0.8), "total_sd": (1.0, 2.2)},
}


# Playing-time rule facts (regulation minutes) written into the profiles; they are rules, not estimates.
REGULATION_MINUTES = {"NBA": 48.0, "WNBA": 40.0, "NBL": 40.0, "EuroLeague": 40.0, "Greek Basket League": 40.0}


def plausibility_problems(key: str, body: dict) -> list:
    lim, problems = LIMITS[key], []
    mean_team = 0.5 * (body["mean_home"] + body["mean_away"])
    advantage = body["mean_home"] - body["mean_away"]
    for name, value in (("team_mean", mean_team), ("home_advantage", advantage), ("total_sd", body["total_sd"])):
        low, high = lim[name]
        if not low <= value <= high:
            problems.append(f"{name} {value:.3f} outside plausible [{low}, {high}]")
    return problems


# Reference values that the repository records in BASE_RATES_REGISTER.md from sources outside the archive
# (ESPN match summaries). They are quoted with their source, never recomputed here, and flagged as references.
SOCCER_REFERENCE = {
    "EPL": {"source": "BASE_RATES_REGISTER.md section 7.3 (EPL 2025-26, n = 380, scoreboard plus match summaries)",
            "values": {"first_half_goal_share": 1.19 / 2.75, "p_first_half_goal": 0.716, "first_half_goals_mean": 1.19,
                       "corners_mean": 10.0, "corners_sd": 3.27, "corners_team_mean": 5.0, "corners_team_sd": 2.77}},
}
EPL_RESULTS = ROOT / "research/data/processed/league_csv/epl_results.csv"


def soccer_profile(seasons: int = 3, min_games: int = 100) -> dict | None:
    """EPL scoring profile from the retained openfootball results (full time, regulation)."""
    import csv
    if not EPL_RESULTS.exists():
        return None
    by_season = defaultdict(list)
    with EPL_RESULTS.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["home_score"] != "" and row["away_score"] != "" and row["endpoint"] == "REGULATION":
                by_season[row["season"]].append((int(row["home_score"]), int(row["away_score"])))
    usable = sorted(k for k, v in by_season.items() if len(v) >= min_games)[-seasons:]
    if not usable:
        return None
    pairs = np.array([p for k in usable for p in by_season[k]], dtype=float)
    home, away = pairs[:, 0], pairs[:, 1]
    reference = SOCCER_REFERENCE["EPL"]
    return {"n_games": len(pairs), "seasons": [int(usable[0][:4]), int(usable[-1][:4])], "mean_home": float(home.mean()),
            "mean_away": float(away.mean()), "total_sd": float((home + away).std(ddof=1)), "margin_sd": float((home - away).std(ddof=1)),
            "score_corr": float(np.corrcoef(home, away)[0, 1]),
            "extras": {"margin_excess_kurtosis": float(stats.kurtosis(home - away)), "draw_share": float(np.mean(home == away)),
                       **{k: round(v, 6) for k, v in reference["values"].items()}},
            "provenance": {"builder": BUILDER, "archive_seasons": usable, "stage": "regular",
                           "source_files": {EPL_RESULTS.relative_to(ROOT).as_posix(): sha256_file(EPL_RESULTS)},
                           "reference_extras_source": reference["source"]}}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# Sports whose margin distribution is stored for key-number calibration, with the number of seasons used. NFL uses the
# seasons since the 2015 extra-point change, so 11 rather than the default 3.
MARGIN_PMF = {"american_football": {"competition": "NFL", "seasons": 11, "limit": 40}}


def margin_pmf_for(sport_dir: str, competition: str, seasons: int, limit: int, archive_root: Path) -> dict | None:
    by_year = defaultdict(list)
    for event in archive_std.iter_events(archive_root, sport=sport_dir, competition=competition, stages={"regular"}):
        by_year[event.season_year].append(event.home_score - event.away_score)
    usable = sorted(y for y, v in by_year.items() if len(v) >= 100)[-seasons:]
    margins = np.array([m for y in usable for m in by_year[y]])
    if len(margins) < 500:
        return None
    clipped = np.clip(margins, -limit, limit)
    counts = np.bincount(clipped + limit, minlength=2 * limit + 1) / len(margins)
    return {"seasons": usable, "n_games": int(len(margins)), "pmf": {str(k - limit): float(counts[k]) for k in range(2 * limit + 1)}}


def park_environment_sigma(events) -> float | None:
    """Between-venue standard deviation of expected total runs as a share of the mean total (ANOVA variance component).

    Weather and umpire effects are not separated out, so this is the park component of the shared game
    environment only. Returns None when too few venues have enough games.
    """
    by_venue = defaultdict(list)
    for e in events:
        if e.venue:
            by_venue[e.venue].append(e.home_score + e.away_score)
    groups = [np.array(v, dtype=float) for v in by_venue.values() if len(v) >= 60]
    if len(groups) < 8:
        return None
    n_i = np.array([len(g) for g in groups], dtype=float)
    means = np.array([g.mean() for g in groups])
    n, k = n_i.sum(), len(groups)
    grand = float((n_i * means).sum() / n)
    ms_between = float((n_i * (means - grand) ** 2).sum() / (k - 1))
    ms_within = float(sum(((g - g.mean()) ** 2).sum() for g in groups) / (n - k))
    n0 = float((n - (n_i ** 2).sum() / n) / (k - 1))
    variance = max((ms_between - ms_within) / n0, 0.0)
    return float(np.sqrt(variance) / grand)


def profile_for(sport_dir: str, competition: str, seasons: int, min_games: int, archive_root: Path) -> dict | None:
    by_year = defaultdict(list)
    for event in archive_std.iter_events(archive_root, sport=sport_dir, competition=competition, stages={"regular"}):
        by_year[event.season_year].append(event)
    usable = sorted(y for y, events in by_year.items() if len(events) >= min_games)[-seasons:]
    if not usable:
        return None
    events = [e for y in usable for e in by_year[y]]
    home = np.array([e.home_score for e in events], dtype=float)
    away = np.array([e.away_score for e in events], dtype=float)
    n = len(events)
    extras = {}
    flagged = [e for e in events if e.overtime is not None]
    if flagged and len(flagged) >= 0.9 * n:
        extras["overtime_share"] = sum(bool(e.overtime) for e in flagged) / len(flagged)
        shoot = [e for e in flagged if e.shootout is not None]
        if shoot:
            extras["shootout_share"] = sum(bool(e.shootout) for e in shoot) / len(shoot)
            overtime_games = [e for e in shoot if e.overtime]
            if overtime_games:
                extras["overtime_decided_before_shootout"] = sum(not e.shootout for e in overtime_games) / len(overtime_games)
    margin = np.abs(home - away)
    extras["margin_excess_kurtosis"] = float(stats.kurtosis(home - away))
    if sport_dir == "Baseball":
        decided = margin > 0
        extras["one_run_share"] = float(np.mean(margin[decided] == 1))
        extras["home_win_share"] = float(np.mean(home[decided] > away[decided]))
        innings = [e for e in events if e.extra_innings is not None]
        if innings:
            extras["extra_innings_share"] = sum(bool(e.extra_innings) for e in innings) / len(innings)
        extras["tie_share"] = float(np.mean(margin == 0))
        runs = np.concatenate([home, away])
        extras["team_run_dispersion_phi"] = float(max((runs.var(ddof=1) - runs.mean()) / runs.mean() ** 2, 0.0))
        env = park_environment_sigma(events)
        if env is not None:
            extras["park_environment_sigma"] = env
        # Runs in a top-of-inning extra frame are unbiased by walk-offs, so they define the
        # per-half-inning run distribution used for extra-innings resolution (entries 0..5, 5 = "5 or more").
        counts = np.zeros(6)
        for e in events:
            if e.away_periods and e.innings and e.innings > 9:
                frames = [f for f in e.away_periods.split("-")]
                for frame in frames[9:]:
                    if frame.isdigit():
                        counts[min(int(frame), 5)] += 1
        if counts.sum() >= 100:
            for r, share in enumerate(counts / counts.sum()):
                extras[f"extra_inning_runs_p{r}"] = float(share)
            extras["extra_inning_frames"] = float(counts.sum())
    if sport_dir == "AFL":
        shots = [(e.home_goals + e.home_behinds, e.home_goals) for e in events if e.home_behinds is not None] + \
                [(e.away_goals + e.away_behinds, e.away_goals) for e in events if e.away_behinds is not None]
        if len(shots) >= 200:
            n_shots = np.array([x[0] for x in shots], dtype=float)
            goals = np.array([x[1] for x in shots], dtype=float)
            extras["scoring_shots_mean"] = float(n_shots.mean())
            extras["scoring_shots_dispersion_phi"] = float(max((n_shots.var(ddof=1) - n_shots.mean()) / n_shots.mean() ** 2, 0.0))
            extras["goal_conversion"] = float(goals.sum() / n_shots.sum())
    if sport_dir == "Rugby League":
        with_half = [e for e in events if e.home_halftime is not None and e.away_halftime is not None]
        if len(with_half) >= 200:
            ht = np.array([e.home_halftime + e.away_halftime for e in with_half], dtype=float)
            ft = np.array([e.home_score + e.away_score for e in with_half], dtype=float)
            extras["first_half_points_share"] = float(ht.sum() / ft.sum())
        tries = [(e.home_tries, e.home_goals) for e in events if e.home_tries is not None and e.home_goals is not None] + \
                [(e.away_tries, e.away_goals) for e in events if e.away_tries is not None and e.away_goals is not None]
        if len(tries) >= 200:
            t = np.array([x[0] for x in tries], dtype=float)
            g = np.array([x[1] for x in tries], dtype=float)
            extras["tries_mean"] = float(t.mean())
            extras["conversion_rate"] = float(min(g.sum() / t.sum(), 1.0))
    if sport_dir == "Ice Hockey":
        shootouts = [e for e in events if e.shootout]
        if len(shootouts) >= 100:
            extras["shootout_home_share"] = sum(e.home_score > e.away_score for e in shootouts) / len(shootouts)
        extras["margin_ge_2_share"] = float(np.mean(margin >= 2))
        extras["margin_ge_3_share"] = float(np.mean(margin >= 3))
    files = sorted({e.origin_path for e in events})
    provenance = {"builder": BUILDER, "archive_seasons": usable, "stage": "regular", "source_files": {
        f: sha256_file(archive_root.parent / f) for f in files}}
    return {"n_games": n, "seasons": [usable[0], usable[-1]], "mean_home": float(home.mean()), "mean_away": float(away.mean()),
            "total_sd": float((home + away).std(ddof=1)), "margin_sd": float((home - away).std(ddof=1)),
            "score_corr": float(np.corrcoef(home, away)[0, 1]),
            "extras": {k: round(v, 6) for k, v in extras.items()}, "provenance": provenance}


def build(out: Path = OUT, seasons: int = 3, min_games: int = 100, archive_root: Path = archive_std.ARCHIVE_ROOT) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    written = {}
    for key, (sport_dir, competitions) in GROUPS.items():
        leagues, excluded = {}, {}
        for competition in competitions:
            body = profile_for(sport_dir, competition, seasons, min_games, archive_root)
            if not body:
                excluded[competition] = ["no season with enough regular-season rows"]
                continue
            problems = plausibility_problems(key, body)
            numbers = (body["n_games"], round(body["mean_home"], 9), round(body["mean_away"], 9), round(body["total_sd"], 9))
            twin = next((name for name, other in leagues.items()
                         if numbers == (other["n_games"], round(other["mean_home"], 9), round(other["mean_away"], 9), round(other["total_sd"], 9))), None)
            if twin:
                problems.append(f"numerically identical to {twin}: duplicated archive folder")
            if problems:
                excluded[competition] = problems
                continue
            lo, hi = LIMITS[key].get("overtime_share", (None, None))
            if lo is not None and "overtime_share" in body["extras"] and not lo <= body["extras"]["overtime_share"] <= hi:
                body["provenance"]["omitted_extras"] = {"overtime_share": f"{body['extras'].pop('overtime_share'):.4f} outside plausible [{lo}, {hi}]; flag column unreliable"}
            spec = MARGIN_PMF.get(key)
            if spec and spec["competition"] == competition:
                margin = margin_pmf_for(sport_dir, competition, spec["seasons"], spec["limit"], archive_root)
                if margin:
                    body["margin_pmf"] = margin["pmf"]
                    body["provenance"]["margin_pmf_seasons"] = margin["seasons"]
                    body["provenance"]["margin_pmf_games"] = margin["n_games"]
            if key == "basketball" and competition in REGULATION_MINUTES:
                body["extras"]["regulation_minutes"] = REGULATION_MINUTES[competition]
            leagues[competition] = body
        if leagues or excluded:
            (out / f"{key}.json").write_text(json.dumps({"schema": "league-profiles-1", "sport": key, "leagues": leagues, "excluded": excluded},
                                                        indent=1, sort_keys=True) + "\n", encoding="utf-8")
            written[key] = {"published": sorted(leagues), "excluded": excluded}
    body = soccer_profile(seasons, min_games)
    if body:
        problems = plausibility_problems("soccer", body)
        leagues, excluded = ({}, {"EPL": problems}) if problems else ({"EPL": body}, {})
        (out / "soccer.json").write_text(json.dumps({"schema": "league-profiles-1", "sport": "soccer", "leagues": leagues, "excluded": excluded},
                                                    indent=1, sort_keys=True) + "\n", encoding="utf-8")
        written["soccer"] = {"published": sorted(leagues), "excluded": excluded}
    return written


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--seasons", type=int, default=3)
    parser.add_argument("--min-games", type=int, default=100)
    args = parser.parse_args(argv)
    print(json.dumps(build(args.out, args.seasons, args.min_games), indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
