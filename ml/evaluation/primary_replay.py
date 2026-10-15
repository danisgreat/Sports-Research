"""Historical replay: how should the primary runtime turn its experts into ONE primary distribution?

Compares, on identical games and identical questions, using the primary runtime's exact experts
(ml.primary: RATINGS_FAST = half-life 90 d, RATINGS_SLOW = 365 d, ridge 8, covariance inflation 1.1;
LEAGUE_BASELINE = league-only):

  EXP3_SELECT   ml.primary's policy: Exp3 (gamma 0.10, reward 1 - loss of the selected expert, delayed feedback),
                one expert drawn at random per event. Scored by its EXACT expected loss, averaged over 200 seeds.
                Context = competition only (coarser than ml.primary's, which can only make it learn faster).
  FAST / SLOW / BASELINE   one expert always.
  HEDGE_MIX     full-information exponential weights over all three experts' frozen predictions; the primary
                distribution is the weighted MIXTURE of grids (a valid joint distribution, so still coherent).
                Learning rate eta chosen on tune seasons only, frozen for test seasons.
  EQUAL_MIX     0.5 FAST + 0.5 SLOW.

Evidence class: HISTORICAL_DEVELOPMENT (archive seasons opened before). Market-free. Nothing here is a card input.
"""
from __future__ import annotations

import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np
import pandas as pd

from ml.config import SHADOW_ROOT, League, discover
from ml.core.metrics import iso_week, paired_week_interval
from ml.data.archive import load_league
from ml.evaluation.backtest import _fit_window, _weeks, make_model
from ml.models.baseline import LeagueBaseline
from ml.models.common import FitError, residual_draw_share

ARMS = ("RATINGS_FAST", "RATINGS_SLOW", "LEAGUE_BASELINE")
GAMMA = 0.10          # ml.primary.GAMMA
ETAS = (0.5, 1, 2, 5, 10, 20, 50)
N_SEEDS = 200
OUT = SHADOW_ROOT / "PRIMARY_POLICY_REPLAY"


def _experts(lg: League, train: pd.DataFrame, as_of: pd.Timestamp):
    """The three experts exactly as ml.primary.fit_experts builds them (once per week instead of per event)."""
    fitting = train.copy()
    if lg.tie_rule != "draw":
        fitting["hs"], fitting["as_"] = train.reg_hs, train.reg_as

    def final_labels(model):
        if hasattr(model, "residual_draw") and hasattr(model, "sd_margin"):
            model.residual_draw = residual_draw_share(train, model.sd_margin)
        if hasattr(model, "p_home_extra"):
            extra = train[train.decision.isin(["Overtime", "Shootout", "EXTRAS"])]
            model.p_home_extra = float((extra.hs > extra.as_).mean()) if len(extra) >= 20 else .5
        return model

    out = {}
    for arm, days in zip(ARMS[:2], (90.0, 365.0)):
        params = dict(half_life_days=days, ridge=8.0)
        if lg.engine == "gaussian":
            params["cov_inflation"] = 1.1
        m = make_model(lg, params)
        m.fit(fitting, as_of) if lg.engine == "gaussian" else m.fit(fitting, as_of, int(train.season.max()))
        out[arm] = final_labels(m)
    out[ARMS[2]] = final_labels(LeagueBaseline(lg).fit(fitting))
    return out


def predictions(lg: League, seasons) -> pd.DataFrame:
    games, _ = load_league(lg)
    rows = []
    for season in seasons:
        sg = games[(games.season == season) & (games.stage.isin(lg.eval_stages))]
        for ws, block in _weeks(sg):
            train = _fit_window(games, lg, season, ws)
            try:
                ex = _experts(lg, train, ws)
            except FitError:
                continue
            base = ex[ARMS[2]]
            line = base.total_line
            bgrid = base.grid()
            known = set(train.home) | set(train.away)
            for r in block.itertuples():
                if r.home not in known or r.away not in known:
                    continue  # ml.primary refuses unseen participants
                row = {"season": season, "date": r.date, "event_id": r.event_id, "y_home": float(r.hs > r.as_),
                       "y_over": float(r.hs + r.as_ > line)}
                for arm in ARMS:
                    g = bgrid if arm == ARMS[2] else ex[arm].grid(r.home, r.away)[0]
                    row[f"{arm}_home"] = g.winner()[0]
                    row[f"{arm}_over"] = g.total(line).win
                rows.append(row)
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["week"] = iso_week(df["date"])
    for arm in ARMS:
        df[f"{arm}_loss"] = 0.5 * ((df[f"{arm}_home"] - df.y_home) ** 2 + (df[f"{arm}_over"] - df.y_over) ** 2)
    return df.sort_values(["date", "event_id"]).reset_index(drop=True)


def exp3_expected(df: pd.DataFrame, seed: int) -> np.ndarray:
    """Per-game action-probability vectors of ml.primary's Exp3 with weekly-delayed feedback (one seed)."""
    rng = np.random.default_rng(seed)
    logs = np.zeros(len(ARMS))
    probs = np.zeros((len(df), len(ARMS)))
    losses = df[[f"{a}_loss" for a in ARMS]].to_numpy()
    pending = []
    for wk, idx in df.groupby("week", sort=False).groups.items():
        for arm, p, reward in pending:  # feedback from earlier weeks becomes available
            logs[arm] += GAMMA * reward / (len(ARMS) * p)
            logs -= logs.max()
        pending = []
        w = np.exp(logs)
        p = (1 - GAMMA) * w / w.sum() + GAMMA / len(ARMS)
        for i in idx:
            probs[i] = p
            a = rng.choice(len(ARMS), p=p)
            pending.append((a, p[a], 1 - losses[i, a]))
    return probs


def hedge_weights(df: pd.DataFrame, eta: float) -> np.ndarray:
    """Full-information exponential weights; only weeks strictly before each game's week contribute."""
    losses = df[[f"{a}_loss" for a in ARMS]].to_numpy()
    cum = np.zeros(len(ARMS))
    out = np.zeros_like(losses)
    for wk, idx in df.groupby("week", sort=False).groups.items():
        z = -eta * (cum - cum.min())
        w = np.exp(z) / np.exp(z).sum()
        out[list(idx)] = w
        cum += losses[list(idx)].sum(axis=0)
    return out


def policy_scores(df: pd.DataFrame, eta: float) -> pd.DataFrame:
    res = pd.DataFrame({"season": df.season, "event_id": df.event_id, "week": df.week})
    P = {a: df[[f"{a}_home", f"{a}_over"]].to_numpy() for a in ARMS}
    y = df[["y_home", "y_over"]].to_numpy()

    def score(pmat):
        return 0.5 * ((pmat - y) ** 2).sum(axis=1), (pmat[:, 0] - y[:, 0]) ** 2

    for a, name in zip(ARMS, ("FAST", "SLOW", "BASELINE")):
        res[f"{name}_loss"], res[f"{name}_home"] = score(P[a])
    res["EQUAL_MIX_loss"], res["EQUAL_MIX_home"] = score(0.5 * P[ARMS[0]] + 0.5 * P[ARMS[1]])
    w = hedge_weights(df, eta)
    mix = sum(w[:, [k]] * P[a] for k, a in enumerate(ARMS))
    res["HEDGE_MIX_loss"], res["HEDGE_MIX_home"] = score(mix)
    res["HEDGE_w_baseline"] = w[:, 2]
    # Exp3: exact expected loss given its probabilities, averaged over seeds
    exp_loss = np.zeros(len(df))
    exp_home = np.zeros(len(df))
    w_base = np.zeros(len(df))
    arm_loss = np.column_stack([score(P[a])[0] for a in ARMS])
    arm_home = np.column_stack([score(P[a])[1] for a in ARMS])
    for s in range(N_SEEDS):
        pr = exp3_expected(df, 20261015 + s)
        exp_loss += (pr * arm_loss).sum(axis=1)
        exp_home += (pr * arm_home).sum(axis=1)
        w_base += pr[:, 2]
    res["EXP3_SELECT_loss"], res["EXP3_SELECT_home"] = exp_loss / N_SEEDS, exp_home / N_SEEDS
    res["EXP3_p_baseline"] = w_base / N_SEEDS
    return res


def replay(lg: League) -> dict:
    t0 = time.time()
    df = predictions(lg, tuple(sorted(set(lg.tune_seasons) | set(lg.test_seasons))))
    if df.empty:
        return {"competition": lg.path, "status": "NO_ROWS"}
    tune = df[df.season.isin(lg.tune_seasons)].reset_index(drop=True)
    eta_scores = {eta: policy_scores_fast(tune, eta) for eta in ETAS}
    eta = min(eta_scores, key=eta_scores.get)
    scores = policy_scores(df, eta)  # weights carry over from tune seasons (earlier data only)
    test = scores[scores.season.isin(lg.test_seasons)]
    return {"competition": lg.path, "model_id": lg.model_id, "eta": eta, "rows": test,
            "data_warnings": ";".join(lg.data_warnings), "n_test": len(test), "seconds": time.time() - t0}


def policy_scores_fast(df: pd.DataFrame, eta: float) -> float:
    w = hedge_weights(df, eta)
    P = np.stack([df[[f"{a}_home", f"{a}_over"]].to_numpy() for a in ARMS], axis=0)
    mix = np.einsum("nk,knj->nj", w, P)
    y = df[["y_home", "y_over"]].to_numpy()
    return float((0.5 * ((mix - y) ** 2).sum(axis=1)).mean())


def _worker(path: str) -> dict:
    from ml.config import get_league
    lg = get_league(path)
    try:
        return replay(lg)
    except Exception as e:  # recorded, never hidden
        return {"competition": path, "status": f"FAILED:{type(e).__name__}:{e}"[:200]}


def main(workers: int = 10) -> None:
    from ml.run import code_digest, receipt_base

    found = [d for d in discover() if d.status == "MODELLED" and d.league.engine != "cricket"]
    t0 = code_digest()
    results = []
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(_worker, d.path) for d in found]
        for f in as_completed(futs):
            r = f.result()
            results.append(r)
            print(f"  {r['competition']}: {r.get('status', 'OK')} n={r.get('n_test', 0)}", flush=True)
    if code_digest() != t0:
        raise RuntimeError("generating source changed during the replay; rerun from a stable checkout")
    write(results, receipt_base())


def write(results: list[dict], rec: dict) -> None:
    pols = ["EXP3_SELECT", "FAST", "SLOW", "BASELINE", "EQUAL_MIX", "HEDGE_MIX"]
    table, pooled = [], []
    for r in sorted(results, key=lambda r: r["competition"]):
        if "rows" not in r:
            table.append({"competition": r["competition"], "note": r.get("status", "")})
            continue
        t = r["rows"].copy()
        t["comp"] = r["competition"]
        pooled.append(t)
        iv = paired_week_interval(t.HEDGE_MIX_home - t.EXP3_SELECT_home, t.event_id, t.week)
        best_single = min(("FAST", "SLOW"), key=lambda n: t[f"{n}_home"].mean())
        iv2 = paired_week_interval(t.HEDGE_MIX_home - t[f"{best_single}_home"], t.event_id, t.week)
        table.append({"competition": r["competition"], "n_test": r["n_test"], "eta": r["eta"],
                      **{f"{p}": t[f"{p}_home"].mean() for p in pols},
                      "hedge_minus_exp3": iv["mean"], "lo": iv["lo"], "hi": iv["hi"], "status": iv["status"],
                      "best_single": best_single, "hedge_minus_best": iv2["mean"], "best_lo": iv2["lo"],
                      "best_hi": iv2["hi"], "best_status": iv2["status"],
                      "exp3_p_baseline": t.EXP3_p_baseline.mean(), "hedge_w_baseline": t.HEDGE_w_baseline.mean(),
                      "warnings": r.get("data_warnings", "")})
    tab = pd.DataFrame(table)
    allrows = pd.concat(pooled, ignore_index=True)
    allrows["wk2"] = allrows.comp + "|" + allrows.week
    pooled_iv = paired_week_interval(allrows.HEDGE_MIX_home - allrows.EXP3_SELECT_home, allrows.event_id, allrows.wk2)
    from ml.evaluation.report import md_table
    OUT.mkdir(parents=True, exist_ok=True)
    cols = ["competition", "n_test", "eta", *pols, "hedge_minus_exp3", "lo", "hi", "status", "best_single",
            "hedge_minus_best", "best_lo", "best_hi", "best_status", "exp3_p_baseline", "hedge_w_baseline", "warnings"]
    lines = [
        "# Primary policy replay: random expert selection (Exp3) versus a full-information mixture", "",
        "**Evidence class: `HISTORICAL_DEVELOPMENT`.** Market-free; not a card input. Question: given the primary "
        "runtime's own three experts (ml/primary.py), which way of producing ONE primary distribution is more accurate? "
        "Method and policies: module docstring of `ml/evaluation/primary_replay.py`. Every policy is scored on identical "
        "games (unseen teams excluded, as the runtime refuses them) and identical questions. Primary metric: home-win "
        "Brier per game (lower is better). Intervals: t-intervals over ISO-week means of game differences "
        "(SCORING_AND_VALIDATION §5); test seasons only; eta chosen on tune seasons only.", "",
        f"**Pooled over all competitions:** HEDGE_MIX − EXP3_SELECT = {pooled_iv['mean']:+.4f} "
        f"[{pooled_iv['lo']:+.4f}, {pooled_iv['hi']:+.4f}] over {pooled_iv['k_weeks']} competition-weeks "
        f"({pooled_iv['status']}).", "",
        "Why a mixture cannot lose to random selection with the same weights: Brier and log loss are convex in p, so the "
        "expected score of a randomly selected expert is never better than the score of the probability-weighted "
        "mixture (Jensen's inequality). Exp3 additionally ignores the other experts' observable losses, although every "
        "bundle freezes all three grids.", "",
        md_table(tab[cols] if "n_test" in tab else tab, cols, 4), "",
        "`exp3_p_baseline` is the average probability that Exp3 prices a primary card from the team-blind league "
        "baseline; `hedge_w_baseline` is the mixture weight the full-information policy gives it.", "",
        "## Receipt", "", "\n".join(f"- `{k}`: {v}" for k, v in rec.items())]
    (OUT / "RESULTS.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    tab.to_csv(OUT / "RESULTS.csv", index=False, lineterminator="\n")
    print(f"pooled HEDGE_MIX - EXP3_SELECT {pooled_iv}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 10)
