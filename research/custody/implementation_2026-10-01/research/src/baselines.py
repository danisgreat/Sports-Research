"""Three-season pre-2026-27 EPL population probabilities for fixed pilot targets."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

from .emit_card import price, states
from .load import PROCESSED, ROOT, sha
from .sports.base import Contract

SEASONS = ("2023-24", "2024-25", "2025-26")
CONTRACTS = [Contract("EPL_POP", "1X2", side, None, "REGULATION") for side in ("HOME", "DRAW", "AWAY")]
CONTRACTS += [Contract("EPL_POP", "TOTAL", side, 2.5, "REGULATION") for side in ("OVER", "UNDER")]
CONTRACTS += [Contract("EPL_POP", "BTTS", side, None, "REGULATION") for side in ("YES", "NO")]


def build() -> list[dict]:
    df = pd.read_parquet(PROCESSED / "matches.parquet")
    prior = df.loc[df.season.isin(SEASONS)].copy()
    if len(prior) != 1140:
        raise ValueError("three complete 380-match seasons required")
    counts = prior.groupby(["hg", "ag"]).size()
    grid = [dict(home=h, away=a, p=float(counts.get((h,a),0)/len(prior)))
            for h in range(21) for a in range(21)]
    pop = states(grid)
    if (prior.hg > 20).any() or (prior.ag > 20).any():
        raise ValueError("population outcome outside score grid")
    distribution_path = ROOT / "data/processed/epl_2026-27_population_states.json"
    distribution_path.write_text(json.dumps(dict(seasons=SEASONS, n=len(prior),
                                                 source_parquet_sha256=sha(PROCESSED / "matches.parquet"),
                                                 states=grid), indent=2)+"\n", encoding="utf-8")
    rows = []
    for c in CONTRACTS:
        p = price(pop,c)
        rows.append(dict(sport="soccer", league="EPL", seasons=";".join(SEASONS),
                         as_of="2026-06-01T00:00:00Z", market=c.market,
                         line="" if c.line is None else c.line, side=c.side,
                         endpoint=c.endpoint, n=len(prior), wins=round(p["w"]*len(prior)),
                         pushes=round(p["p"]*len(prior)), baseline_p=p["conditional_win"],
                         source_sha256=sha(PROCESSED / "matches.parquet")))
    output = ROOT / "baselines.csv"
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader(); writer.writerows(rows)
    return rows


if __name__ == "__main__":
    print(json.dumps(build(), indent=2))
