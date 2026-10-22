"""Walk-forward development study of a competition's contextual model, before any prospective lane starts (REV-10).

    python -m ml context-study --competition "Basketball/NBA" --test-season 2025 --out NEW_FOLDER [--refit-days 7]

For every test-season week the three arms of the frozen cycle recipe (fast, slow, league-only) are fitted on the earlier
games only, using the store as it stood and the same point-in-time features the live cycle uses, and the next week's games are
predicted with the equal-weight mixture (the Hedge starting weights). The study reports, on identical games:

  * Brier of home win for the mixture, its league-only arm, and TB-1-MD (the hand reference, from the same earlier games);
  * the calibration slope and intercept of the mixture (REV-10 wants 0.9-1.1 before a lane starts);
  * z-SD and tail shares of the margin and total (the widths a card is held to);
  * the paired mixture-minus-comparator Brier with a week-block interval.

STUDY_PREDICTIONS.csv also carries the per-arm winner and total probabilities in the layout ``python -m ml hedge-study`` reads
(event_id, issued_at, available_at, week, y_home, y_over, p_home_<ARM>, p_over_<ARM>), so the online-weighting schedule can be
studied on the same walk-forward games (REV-19).

Evidence class HISTORICAL_DEVELOPMENT: the store's finals are current-capture labels, so each is treated as usable one day
after its game (an assumption of the study, not a verified fact), historical context features are all missing and therefore not
fitted (the live cycle behaves the same way), and this is not a pregame replay: it proves no prospective skill. It is the development step the lane protocol requires before a release is frozen.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np
import pandas as pd

from ml import cycle, primary as p, reference as R, research_ingest as ri
from ml.core import metrics as M
from ml.core.distributions import ScoreGrid
from ml.models.contextual import ContextModel, RECIPES

ROOT = Path(__file__).resolve().parents[1]
STORE = "research/learning_store"


def training_frame(competition: str, endpoint: str, store_path, horizon) -> pd.DataFrame:
    """Every verified final with its point-in-time features, built once through the cycle's own dataset function."""
    store = ri.load_store(store_path)
    sample = store.events[store.events.competition == competition].iloc[-1]
    request = dict(event_id="STUDY:NO-EVENT", competition=competition, endpoint=endpoint, home=sample.home, away=sample.away, venue="",
                   scheduled_start=pd.Timestamp(horizon).isoformat(), issue_at=pd.Timestamp(horizon).isoformat(),
                   outcome_exposure="NONE_RECORDED", candidate_recipe="DEVELOPMENT_STUDY")
    return cycle.dataset(store, request)


def tb1_probability(history: pd.DataFrame, home: str, away: str, competition: str, season, form: str = "average") -> float | None:
    """TB-1-MD (``average``) or TB-2-MD (``additive``) home-win probability from the same season's earlier games.

    Points leagues use the coherent grid of ``ml.reference``. NHL and MLB (toolkit 4.3 constants, k = 20) use the toolkit's own
    normal rule Phi(M / sd), because a continuous grid is a poor shape for low counts and the toolkit never priced them otherwise.
    """
    from ml.config import TB1_VALIDATED
    key = R.league_key(competition)
    label = competition.split("/")[-1]
    history = history[history.season.astype(str) == str(season)]
    if history.empty:
        return None
    games = pd.concat([history[["home", "hs", "as_"]].rename(columns={"home": "team", "hs": "pf", "as_": "pa"}),
                       history[["away", "as_", "hs"]].rename(columns={"away": "team", "as_": "pf", "hs": "pa"})])
    totals = games.groupby("team").agg(pf=("pf", "sum"), pa=("pa", "sum"), n=("pf", "size"))
    if home not in totals.index or away not in totals.index:
        return None
    data = dict(lm=float(games.pf.sum()) / float(len(games)),
                home=dict(team=home, **totals.loc[home].to_dict()), away=dict(team=away, **totals.loc[away].to_dict()))
    if key in R.TB1_MD and R.TB1_MD[key]["kind"] == "normal":
        grid, _ = R.tb1_grid(competition, data, form=form)
        w, _, l = grid.winner()
        return w / (w + l) if w + l else None
    if label in TB1_VALIDATED and not TB1_VALIDATED[label].poisson:
        from scipy import stats
        c = TB1_VALIDATED[label]
        spec = dict(k=c.k, he=c.home_edge)
        return float(stats.norm.cdf(R.tb1_centre(spec, data, False, form)["margin"] / c.sd_margin))
    return None


def study(competition: str, test_season: str, refit_days: int = 7, root=ROOT, endpoint: str | None = None) -> dict:
    root = Path(root)
    from ml.config import SPORT_RULES
    sport = competition.split("/", 1)[0]
    endpoint = endpoint or SPORT_RULES[sport]["endpoint"]
    store_path = root / STORE
    frame = training_frame(competition, endpoint, store_path, pd.Timestamp.now(tz="UTC") + pd.Timedelta(days=1))
    # DEVELOPMENT CONVENTION: the store's labels were captured today, so their recorded availability is today. A walk-forward
    # needs each final to be usable one day after its game; that is an assumption of this study, not a verified fact.
    frame["label_available_at"] = frame.event_at.map(lambda v: (p.clock(v) + pd.Timedelta(days=1)).isoformat())
    frame["day"] = frame.event_at.map(lambda v: p.clock(v).tz_convert("UTC").normalize())
    frame = frame.sort_values("event_at").reset_index(drop=True)
    test = frame[frame.season.astype(str) == str(test_season)]
    if test.empty:
        raise ValueError(f"no events for season {test_season}")
    fast, slow, ridge = RECIPES[sport]
    config = dict(feedback_half_life_events=20.0, eta_cap=0.5, weight_floor=0.05)   # the frozen release defaults (cycle.freeze_release)
    feedback: list[dict] = []
    scale = max(1.0, float(np.std(frame.hs.astype(float) - frame.as_.astype(float))))
    rows = []
    start, end = test.day.min(), test.day.max()
    cutoff = start
    while cutoff <= end:
        window_end = cutoff + pd.Timedelta(days=refit_days)
        target = test[(test.day >= cutoff) & (test.day < window_end)]
        history = frame[(frame.event_at.map(p.clock) < cutoff) & (frame.label_available_at.map(p.clock) <= cutoff)]
        if len(target) and len(history) >= 200:
            usable = [r for r in feedback if p.clock(r["available_at"]) <= cutoff]
            weights = cycle.adaptive_weights(usable, config)[0] if usable else np.ones(3) / 3
            week_rows = []
            models = {"fast": ContextModel(competition, endpoint, fast, ridge).fit(history, cutoff),
                      "slow": ContextModel(competition, endpoint, slow, ridge).fit(history, cutoff),
                      "league": ContextModel(competition, endpoint, slow, ridge, baseline=True).fit(history, cutoff)}
            for _, g in target.iterrows():
                row = pd.DataFrame([g.to_dict()])
                try:
                    grids = {k: m.grid(row) for k, m in models.items()}
                except Exception:
                    continue    # an unseen participant has no explicit cold-start model; the live cycle refuses it too
                mixed = p.mix_grids([grids["fast"], grids["slow"], grids["league"]], np.ones(3) / 3)
                learned = p.mix_grids([grids["fast"], grids["slow"], grids["league"]], weights)
                week_rows.append(dict(event_id=g.event_id, available_at=(p.clock(g.event_at) + pd.Timedelta(days=1)).isoformat(),
                                      **{"loss_" + a: cycle.loss(grids[k], g.hs, g.as_, scale) for a, k in zip(cycle.ARMS, ("fast", "slow", "league"))}))
                margin_mu = mixed.means()[0] - mixed.means()[1]
                summary = mixed.summary()
                y = 1.0 if g.hs > g.as_ else 0.0
                w = lambda grid: (lambda t: t[0] / (t[0] + t[2]))(grid.winner())
                line = float(np.floor(history.hs.astype(float).add(history.as_.astype(float)).mean())) + 0.5
                over = {k: (lambda m: m.win / (m.win + m.loss))(grids[k].total(line, "OVER")) for k in grids}
                arm_cols = {f"p_home_{a}": w(grids[k]) for a, k in zip(cycle.ARMS, ("fast", "slow", "league"))}
                arm_cols.update({f"p_over_{a}": over[k] for a, k in zip(cycle.ARMS, ("fast", "slow", "league"))})
                rows.append(dict(event_id=g.event_id, event_at=g.event_at, issued_at=p.clock(g.event_at).isoformat(),
                                 available_at=(p.clock(g.event_at) + pd.Timedelta(days=1)).isoformat(), y_home=y, y_over=float(g.hs + g.as_ > line),
                                 over_line=line, **arm_cols,
                                 week=pd.Timestamp(g.event_at).strftime("%G-W%V"), y=y,
                                 p_mix=w(mixed), p_hedge=w(learned), w_fast=weights[0], w_slow=weights[1], w_league=weights[2], p_league=w(grids["league"]), p_tb1=tb1_probability(history, g.home, g.away, competition, g.season, "average"),
                                 p_tb2=tb1_probability(history, g.home, g.away, competition, g.season, "additive"),
                                 z_margin=((g.hs - g.as_) - margin_mu) / summary["sd_margin"],
                                 z_total=((g.hs + g.as_) - (summary["mean_home"] + summary["mean_away"])) / summary["sd_total"]))
            feedback.extend(week_rows)
        cutoff = window_end
    return dict(frame=pd.DataFrame(rows), competition=competition, test_season=str(test_season), train_rows=len(frame))


def summarise(result: dict) -> list[dict]:
    d = result["frame"]
    out = []
    base = dict(competition=result["competition"], test_season=result["test_season"], games=len(d))
    for col, label in (("p_mix", "equal-weight mixture"), ("p_hedge", "online-Hedge mixture")):
        cal = M.calibration_fit(d[col], d.y)
        out.append(dict(base, metric=f"calibration_slope_{label}", value=round(cal["slope"], 3),
                        detail=f"se {cal['slope_se']:.3f}; intercept {cal['intercept']:.3f}; ECE {cal['ece']:.4f}"))
    for col, label in (("p_mix", "equal-weight mixture"), ("p_hedge", "online-Hedge mixture"), ("p_league", "league-only arm"), ("p_tb1", "TB-1-MD (season to date)"), ("p_tb2", "TB-2-MD additive (season to date)")):
        sub = d.dropna(subset=[col])
        out.append(dict(base, metric=f"brier_{label}", value=round(float(M.brier(sub[col], sub.y).mean()), 4), detail=f"n {len(sub)}"))
    for col, label in (("p_tb1", "TB-1-MD (season to date)"), ("p_league", "league-only arm")):
        sub = d.dropna(subset=["p_tb2", col])
        diff = M.brier(sub.p_tb2, sub.y) - M.brier(sub[col], sub.y)
        interval = M.paired_week_interval(pd.Series(np.asarray(diff)), sub.event_id.reset_index(drop=True), sub.week.reset_index(drop=True))
        out.append(dict(base, metric=f"paired_brier_TB-2-MD_minus_{label}", value=round(interval["mean"], 4),
                        detail=f"[{interval['lo']:.4f}, {interval['hi']:.4f}] over {interval['k_weeks']} weeks: {interval['status']}"))
    cal = M.calibration_fit(d.dropna(subset=["p_tb2"]).p_tb2, d.dropna(subset=["p_tb2"]).y)
    out.append(dict(base, metric="calibration_slope_TB-2-MD", value=round(cal["slope"], 3), detail=f"se {cal['slope_se']:.3f}; intercept {cal['intercept']:.3f}"))
    cal = M.calibration_fit(d.dropna(subset=["p_tb1"]).p_tb1, d.dropna(subset=["p_tb1"]).y)
    out.append(dict(base, metric="calibration_slope_TB-1-MD", value=round(cal["slope"], 3), detail=f"se {cal['slope_se']:.3f}; intercept {cal['intercept']:.3f}"))
    for mine, mlabel in (("p_mix", "equal-weight mixture"), ("p_hedge", "online-Hedge mixture")):
        for col, label in (("p_league", "league-only arm"), ("p_tb1", "TB-1-MD (season to date)"), ("p_tb2", "TB-2-MD additive (season to date)")):
            sub = d.dropna(subset=[col])
            diff = M.brier(sub[mine], sub.y) - M.brier(sub[col], sub.y)
            interval = M.paired_week_interval(pd.Series(np.asarray(diff)), sub.event_id.reset_index(drop=True), sub.week.reset_index(drop=True))
            out.append(dict(base, metric=f"paired_brier_{mlabel}_minus_{label}", value=round(interval["mean"], 4),
                            detail=f"[{interval['lo']:.4f}, {interval['hi']:.4f}] over {interval['k_weeks']} weeks: {interval['status']}"))
    for col in ("z_margin", "z_total"):
        z = d[col].to_numpy(float)
        out.append(dict(base, metric=f"{col}_sd", value=round(float(z.std()), 3),
                        detail=f"mean {z.mean():.3f}; beyond 1 SD {np.mean(np.abs(z) > 1):.3f}; beyond 2 SD {np.mean(np.abs(z) > 2):.3f}"))
    out.append(dict(base, metric="mean_hedge_weights_fast_slow_league", value="",
                    detail=f"{d.w_fast.mean():.3f} / {d.w_slow.mean():.3f} / {d.w_league.mean():.3f}"))
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--competition", required=True)
    parser.add_argument("--test-season", required=True)
    parser.add_argument("--refit-days", type=int, default=7)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    result = study(args.competition, args.test_season, args.refit_days)
    args.out.mkdir(parents=True, exist_ok=False)
    result["frame"].to_csv(args.out / "STUDY_PREDICTIONS.csv", index=False, lineterminator="\n")
    summary = pd.DataFrame(summarise(result))
    summary.to_csv(args.out / "STUDY_SUMMARY.csv", index=False, lineterminator="\n")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
