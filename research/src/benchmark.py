"""Post-settlement closing-odds comparison; never imported by forecast code."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from .load import BENCHMARK, ROOT, sha, team


def closing_1x2(season: str = "2025-26") -> dict:
    report_path = ROOT / "runs" / "epl_2025-26_holdout.json"
    forecast_path = ROOT / "runs" / "epl_2025-26_holdout.csv"
    if not report_path.exists() or not forecast_path.exists():
        raise RuntimeError("holdout with final scores must exist before market benchmark")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    if report.get("stage") != "ONE_SHOT_HOLDOUT" or report.get("holdout") != season:
        raise RuntimeError("not a settled historical holdout")
    forecasts = pd.read_csv(forecast_path)
    check = BENCHMARK / f"{season}.csv"
    with check.open(newline="", encoding="utf-8-sig", errors="replace") as f:
        rows = list(csv.DictReader(f))
    odds = {}
    for r in rows:
        key = (team(r["HomeTeam"]), team(r["AwayTeam"]))
        try:
            values = np.array([float(r[k]) for k in ("AvgCH", "AvgCD", "AvgCA")])
        except (KeyError, TypeError, ValueError):
            continue
        if not np.isfinite(values).all() or (values <= 1).any():
            continue
        implied = 1/values
        odds[key] = dict(zip(("H", "D", "A"), (implied/implied.sum()).tolist()))
    losses = []
    paired = []
    for game in forecasts.itertuples():
        key = (game.home, game.away)
        if key not in odds:
            continue
        if game.result not in {"H", "D", "A"}:
            raise ValueError("holdout result is not final")
        losses.append(-np.log(odds[key][game.result]))
        paired.append(game.m2_logloss)
    if not losses:
        raise ValueError("no available closing probabilities")
    output = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  settled_events=len(forecasts), closing_available=len(losses),
                  closing_missing=len(forecasts)-len(losses),
                  source_sha256=sha(check), source="Football-Data E0 AvgCH/AvgCD/AvgCA",
                  closing_logloss=float(np.mean(losses)),
                  m2_logloss_same_events=float(np.mean(paired)),
                  m2_minus_closing=float(np.mean(np.array(paired)-np.array(losses))),
                  informational_only=True)
    path = ROOT / "runs" / "epl_2025-26_closing_benchmark.json"
    path.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
    return output


if __name__ == "__main__":
    print(json.dumps(closing_1x2(), indent=2))
