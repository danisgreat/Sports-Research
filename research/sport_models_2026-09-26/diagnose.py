#!/usr/bin/env python3
"""Diagnostics for the two failed comparisons in validation_results.json (2026-09-26). Descriptive only:
nothing here changes a model. Usage: python research/sport_models_2026-09-26/diagnose.py"""
import json
import math
import statistics as st
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import sport_models as sm  # noqa: E402
import validate_public as vp  # noqa: E402


def tennis():
    cfg = sm.config("atp")
    elo = sm.TennisElo(cfg)
    rows = []
    for m in sorted(vp.tennis(), key=sm.tennis_order):
        ok = ("2023-01-01" <= m["date"] <= "2026-09-20" and not m["walkover"] and m["level"] in {"G", "M", "A", "F", "250", "500"}
              and min(elo.n[m["winner"]], elo.n[m["loser"]]) >= cfg["min_matches"] and m["complete"] and m["best_of"] == 3)
        if ok:
            a, b = sorted([m["winner"], m["loser"]])
            _, g0, p1, f1 = elo.forecast(a, b, m["surface"], 3, m["date"])
            if g0 is not None:
                mu1 = sm.pmf_mean(f1.total)
                sd1 = math.sqrt(sum((k - mu1) ** 2 * p for k, p in f1.total.items()))
                rows.append((m["total_games"], mu1, sd1, sm.pmf_mean(g0.total), f1.extra["sets"].total.get(3, 0.0),
                             abs(m["sets_margin"]) == 1, abs(p1 - 0.5)))
        elo.update(m)
    act = [r[0] for r in rows]
    out = {"n_bo3": len(rows), "actual_mean": st.mean(act), "actual_sd": st.pstdev(act),
           "a1_mean_of_means": st.mean(r[1] for r in rows), "a1_mean_sd": st.mean(r[2] for r in rows),
           "a0_mean": st.mean(r[3] for r in rows), "a1_p_three_sets": st.mean(r[4] for r in rows),
           "actual_three_sets": sum(r[5] for r in rows) / len(rows)}
    # does the chain's games mean track the realised games across favourite strength?
    for lo, hi in ((0, 0.1), (0.1, 0.2), (0.2, 0.3), (0.3, 0.5)):
        sub = [r for r in rows if lo <= r[6] < hi]
        out[f"gap_{lo}_{hi}"] = {"n": len(sub), "actual": st.mean(r[0] for r in sub), "a1": st.mean(r[1] for r in sub)}
    return out


def mlb():
    cfg = sm.config("mlb-teamonly")
    eng = sm.TeamEngine(cfg, vp.mlb())
    p1, shapes = [], []
    for g, f0, f1 in eng.replay("2022-04-01", "2024-10-01"):
        p1.append(sm.p_gt(f1.margin, 0))
        shapes.append(f1.meta["shape"])
    return {"n": len(p1), "a1_p_home_sd": st.pstdev(p1), "a1_p_home_range": [min(p1), max(p1)],
            "shape_mean": st.mean(shapes), "shape_range": [min(shapes), max(shapes)]}


if __name__ == "__main__":
    res = {"tennis_bo3": tennis(), "mlb_team_only": mlb()}
    (HERE / "diagnostics.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps(res, indent=1))
