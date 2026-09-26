#!/usr/bin/env python3
"""v2 candidates for the two routes that failed in validation_results.json (2026-09-26).

Disclosure. The v1 failures (MLB team-only A1 overconfident; tennis serve-chain games route biased toward
close matches) were seen on the TEST windows before these candidates were written, so the TEST numbers for
v2 are NOT independent evidence — they show only that the tuned value does not overfit the TUNE window.
Independent evidence has to come from data neither version has seen: the 2025 MLB season
(`python tools/mlb_model.py validate --season 2025`, statsapi) and the prospective shadow lanes.

Protocol (declared before any v2 run):
  MLB    one parameter, team_prior_games (games of league-mean runs added to each team), grid
         20 (v1), 40, 60, 80, 120, 160. TUNE: the 2022 season only. Selection: lowest mean win log loss
         (the diagnosed failure is overconfidence). TEST: 2023–2024 with the selected value.
  tennis one parameter, gap_sd (SD of a match-level random effect on the serve-point gap), grid
         0 (v1), 0.03, 0.06, 0.09, 0.12. TUNE: ATP main-tour matches 2021–2022 (Elo warm-up from 2017).
         Selection: lowest mean total-games RPS (the failed metric). The winner probability is unchanged
         by construction. TEST: 2023-01-01 to 2026-09-20 with the selected value.

Usage: python research/sport_models_2026-09-26/tune_v2.py --sport mlb|atp --phase tune|test --value X
Writes parts_v2/<sport>_<phase>_<value>.json. LEARNING_ONLY.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import sport_models as sm  # noqa: E402
import validate_public as vp  # noqa: E402

WINDOWS = {("mlb", "tune"): ("2022-04-01", "2022-10-10"), ("mlb", "test"): ("2023-04-01", "2024-10-01"),
           ("atp", "tune"): ("2021-01-01", "2022-12-31"), ("atp", "test"): ("2023-01-01", "2026-09-20")}
GRID = {"mlb": [20, 40, 60, 80, 120, 160], "atp": [0.0, 0.03, 0.06, 0.09, 0.12]}
LEVELS = {"G", "M", "A", "F", "250", "500"}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sport", choices=["mlb", "atp"], required=True)
    ap.add_argument("--phase", choices=["tune", "test"], required=True)
    ap.add_argument("--value", type=float, required=True)
    ap.add_argument("--boot", type=int, default=1000)
    args = ap.parse_args(argv)
    frm, to = WINDOWS[(args.sport, args.phase)]
    t0 = time.time()
    if args.sport == "mlb":
        cfg = sm.config("mlb-teamonly")
        cfg["team_prior_games"] = args.value
        res = sm.validate_team(cfg, vp.mlb(), frm, to, tb1_league="mlb", boot=args.boot)
    else:
        cfg = sm.config("atp")
        cfg["gap_sd"] = args.value
        res = sm.validate_tennis(cfg, vp.tennis(), frm, to, levels=LEVELS, boot=args.boot)
    res.update({"value": args.value, "phase": args.phase, "seconds": round(time.time() - t0, 1)})
    out = HERE / "parts_v2"
    out.mkdir(exist_ok=True)
    (out / f"{args.sport}_{args.phase}_{args.value:g}.json").write_text(json.dumps(res, indent=1, sort_keys=True),
                                                                        encoding="utf-8")
    print(args.sport, args.phase, args.value, res["n"], res["seconds"], flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
