"""Point-in-time team features from the learning store (FEAT-v1), with true sample sizes and missingness.

Every feature for a target is computed from the store "as of" the forecast horizon: only FINAL results whose
reviewed availability (valid_from) is at or before the horizon, from games on an earlier UTC day, and only team
statistics and availability snapshots published by then. Adding later games, later corrections or later team news
to the store therefore cannot change an earlier feature vector (tested).

Windows L5/L10/L15/L20 are counted in games, report their true n and are never padded. A missing input is NaN with
an explicit indicator, never a league average and never "all players available". Possessions use the reported
POSSESSIONS statistic, else the standard estimate FGA - ORB + TOV + 0.44 FTA (labelled DERIVED), else missing.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np
import pandas as pd

from ml import primary as p
from ml import research_ingest as ri

SPEC_VERSION = "FEAT-2026.10.16-v1"
WINDOWS = (5, 10, 15, 20)
DECAY_HALF_LIFE_GAMES = 8.0
DECAY_MAX_GAMES = 40
OPPONENT_GAMES = 20
LEAGUE_DAYS = 365
STARTERS = {"Basketball": 5, "Soccer": 11, "Ice Hockey": 6, "Rugby League": 13, "Rugby Union": 15,
            "Australian Rules": 18, "American Football": 22, "Baseball": 9}
POSSESSION_PARTS = ("FGA", "ORB", "TOV", "FTA")
GAME_COLUMNS = ["team", "opp", "event_uid", "event_at", "season", "pf", "pa", "is_home", "poss", "poss_status"]


def team_games(store: ri.Store, competition: str, endpoint: str, as_of) -> pd.DataFrame:
    """One row per (team, prior game) visible at ``as_of``; sorted newest first within team."""
    limit = p.clock(as_of)
    res = ri.effective_results(store, limit)
    if res.empty:
        return pd.DataFrame(columns=GAME_COLUMNS)
    ev = store.events.set_index("event_uid")
    res = res[res.status.isin(ri.FINAL_STATUSES)]
    res = res.join(ev[["competition", "endpoint", "event_at", "season", "home", "away"]], on="event_uid")
    res = res[(res.competition == competition) & (res.endpoint == endpoint)]
    if res.empty:
        return pd.DataFrame(columns=GAME_COLUMNS)
    res = res.copy()
    res["t_at"] = res.event_at.map(p.clock)
    res = res[(res.t_at < limit.normalize()) & res.final_at.map(lambda t: p.clock(t) <= limit)]
    stats = ri.effective_stats(store, limit)
    lookup = {(r.event_uid, r.team, r.stat): float(r.value) for r in stats.itertuples()}

    def possessions(uid, team):
        if (uid, team, "POSSESSIONS") in lookup:
            return lookup[(uid, team, "POSSESSIONS")], "OBSERVED"
        parts = [lookup.get((uid, team, s)) for s in POSSESSION_PARTS]
        if all(x is not None for x in parts):
            fga, orb, tov, fta = parts
            return fga - orb + tov + 0.44 * fta, "DERIVED"
        return math.nan, "MISSING"

    rows = []
    for r in res.itertuples():
        hs, as_ = int(r.hs), int(r.as_)
        for team, opp, pf, pa, home in ((r.home, r.away, hs, as_, 1), (r.away, r.home, as_, hs, 0)):
            ph, sh = possessions(r.event_uid, team)
            po, so = possessions(r.event_uid, opp)
            # Possessions per game are shared by both sides; average both teams' estimates where both exist.
            vals = [x for x in (ph, po) if not math.isnan(x)]
            rows.append(dict(team=team, opp=opp, event_uid=r.event_uid, event_at=r.t_at, season=r.season, pf=pf, pa=pa,
                             is_home=home, poss=float(np.mean(vals)) if vals else math.nan,
                             poss_status="OBSERVED" if "OBSERVED" in (sh, so) else ("DERIVED" if vals else "MISSING")))
    if not rows:
        return pd.DataFrame(columns=GAME_COLUMNS)
    out = pd.DataFrame(rows, columns=GAME_COLUMNS)
    return out.sort_values(["team", "event_at", "event_uid"], ascending=[True, False, True]).reset_index(drop=True)


def _mean(values) -> float:
    values = [v for v in values if not (isinstance(v, float) and math.isnan(v))]
    return float(np.mean(values)) if values else math.nan


def build(store: ri.Store, competition: str, endpoint: str, home: str, away: str, as_of, *,
          target_event_uid: str = "", season: str = "") -> dict:
    """Ordered feature dictionary: values, ``<name>__n`` sample sizes and ``<name>__missing`` indicators."""
    limit = p.clock(as_of)
    games = team_games(store, competition, endpoint, limit)
    sport = competition.split("/", 1)[0]
    feats: dict = {"spec_version": SPEC_VERSION, "as_of": limit.isoformat()}

    def put(name, value, n):
        value = float(value) if value is not None else math.nan
        feats[name] = value
        feats[name + "__n"] = int(n)
        feats[name + "__missing"] = int(math.isnan(value))

    # Opponent strength: each team's mean margin over its last OPPONENT_GAMES visible games.
    strength = {}
    for team, g in games.groupby("team", sort=True):
        recent = g.head(OPPONENT_GAMES)
        strength[team] = float((recent.pf - recent.pa).mean())

    for side, team in (("home", home), ("away", away)):
        g = games[games.team == team]
        for n in WINDOWS:
            w = g.head(n)
            k = len(w)
            put(f"{side}_L{n}_pf", w.pf.mean() if k else math.nan, k)
            put(f"{side}_L{n}_pa", w.pa.mean() if k else math.nan, k)
            put(f"{side}_L{n}_net", (w.pf - w.pa).mean() if k else math.nan, k)
            full_poss = k > 0 and w.poss.notna().all()
            if full_poss:
                poss = w.poss.sum()
                put(f"{side}_L{n}_ortg", 100 * w.pf.sum() / poss, k)
                put(f"{side}_L{n}_drtg", 100 * w.pa.sum() / poss, k)
                put(f"{side}_L{n}_pace", w.poss.mean(), k)
            else:
                for stat in ("ortg", "drtg", "pace"):
                    put(f"{side}_L{n}_{stat}", math.nan, int(w.poss.notna().sum()) if k else 0)
        d = g.head(DECAY_MAX_GAMES)
        if len(d):
            wts = 0.5 ** (np.arange(len(d)) / DECAY_HALF_LIFE_GAMES)
            put(f"{side}_decay_pf", float(np.average(d.pf, weights=wts)), len(d))
            put(f"{side}_decay_pa", float(np.average(d.pa, weights=wts)), len(d))
            put(f"{side}_decay_net", float(np.average(d.pf - d.pa, weights=wts)), len(d))
        else:
            for stat in ("pf", "pa", "net"):
                put(f"{side}_decay_{stat}", math.nan, 0)
        w = g.head(10)
        adj = [(r.pf - r.pa) + strength.get(r.opp, math.nan) for r in w.itertuples()]
        put(f"{side}_oppadj_L10_net", _mean(adj), sum(not math.isnan(x) for x in adj))
        this_season = season or (str(g.iloc[0].season) if len(g) else "")
        s = g[g.season.astype(str) == this_season] if this_season else g.iloc[0:0]
        put(f"{side}_season_net", (s.pf - s.pa).mean() if len(s) else math.nan, len(s))
        venue = g[g.is_home == (1 if side == "home" else 0)].head(20)
        put(f"{side}_venue_L20_net", (venue.pf - venue.pa).mean() if len(venue) else math.nan, len(venue))
        rest = (limit.normalize() - g.iloc[0].event_at.normalize()).days if len(g) else math.nan
        put(f"{side}_rest_days", rest, int(len(g) > 0))

        avail = ri.availability_as_of(store, target_event_uid, limit) if target_event_uid else pd.DataFrame()
        a = avail[avail.team == team] if len(avail) else avail
        starters = int(((a.role == "STARTER") & (a.confirmation == "OFFICIAL_CONFIRMED") &
                        (a.status == "CONFIRMED_ACTIVE")).sum()) if len(a) else 0
        out = int((a.status == "CONFIRMED_OUT").sum()) if len(a) else 0
        if len(a):
            put(f"{side}_confirmed_starters", starters, len(a))
            put(f"{side}_confirmed_out", out, len(a))
            need = STARTERS.get(sport)
            put(f"{side}_lineup_confirmed", float(starters >= need) if need else math.nan, len(a))
        else:  # Unknown availability stays unknown: never zero absences or a healthy roster.
            for stat in ("confirmed_starters", "confirmed_out", "lineup_confirmed"):
                put(f"{side}_{stat}", math.nan, 0)

    recent = games[(games.is_home == 1) & games.event_at.map(lambda t: (limit - t).days <= LEAGUE_DAYS)]
    put("league_mean_total", (recent.pf + recent.pa).mean() if len(recent) else math.nan, len(recent))
    put("league_home_margin", (recent.pf - recent.pa).mean() if len(recent) else math.nan, len(recent))
    for stem in [f"L{n}_net" for n in WINDOWS] + ["decay_net", "oppadj_L10_net", "season_net", "rest_days"]:
        h, a = feats[f"home_{stem}"], feats[f"away_{stem}"]
        put(f"diff_{stem}", h - a, min(feats[f"home_{stem}__n"], feats[f"away_{stem}__n"]))
    return feats


def value_names(feats: dict) -> list[str]:
    return [k for k in feats if k not in ("spec_version", "as_of") and not k.endswith(("__n", "__missing"))]


def snapshot_rows(forecast_id: str, event: str, feats: dict, store: ri.Store) -> list[dict]:
    digest = ri.store_digest(store)
    return [dict(forecast_id=forecast_id, event_uid=event, as_of=feats["as_of"], spec_version=feats["spec_version"],
                 store_view_seq=store.view_seq, store_digest=digest, feature=name,
                 value=repr(feats[name]), n=feats[name + "__n"],
                 status="MISSING" if feats[name + "__missing"] else "OBSERVED")
            for name in value_names(feats)]


def write_snapshot(path: Path, rows: list[dict]) -> None:
    """Append-only FEATURE_SNAPSHOTS.csv; a forecast ID can be written once."""
    path = Path(path)
    if path.exists():
        existing = pd.read_csv(path, dtype=str, keep_default_na=False)
        if rows and rows[0]["forecast_id"] in set(existing.forecast_id):
            raise p.AdmissionError("feature snapshot already frozen for this forecast ID")
    ri._append(path, tuple(rows[0]), rows)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--store", type=Path, required=True)
    for name in ("competition", "endpoint", "home", "away", "as-of"):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--event-uid", default="")
    parser.add_argument("--forecast-id", default="")
    parser.add_argument("--snapshot", type=Path, help="append the frozen snapshot to this FEATURE_SNAPSHOTS.csv")
    args = parser.parse_args(argv)
    store = ri.load_store(args.store)
    feats = build(store, args.competition, args.endpoint, args.home, args.away, args.as_of,
                  target_event_uid=args.event_uid)
    for name in value_names(feats):
        print(f"{name}={feats[name]!r} n={feats[name + '__n']}")
    if args.snapshot:
        if not args.forecast_id.strip():
            raise SystemExit("--forecast-id required with --snapshot")
        write_snapshot(args.snapshot, snapshot_rows(args.forecast_id, args.event_uid, feats, store))


if __name__ == "__main__":
    main()
