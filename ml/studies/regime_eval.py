"""Regime-row evaluation on walk-forward reference totals (REGIME-v2 / REGIME-v3, CR-2026.11.08-R2).

    python -m ml.studies.regime_eval --outputs research/verification/framework_change_2026-11-08-1/regime_study/outputs

Reads ``<LEAGUE>_WALKFORWARD_TOTALS.csv`` (one row per game: season, stage, day, forecast_total, actual_total) and writes:

- ``REGIME_SIZES.csv``: the pooled actual/forecast ratio per regime window with a season-block bootstrap interval;
- ``LOSO_HELD_OUT.csv``: leave-one-season-out (EXPLORATORY: each held-out season's multiplier is fitted on all other
  seasons, later ones included);
- ``CHRONOLOGICAL.csv``: the confirmation test. Each season's multiplier is fitted on EARLIER seasons only (an expanding
  window), so no evaluation uses information from its own future. Only this test can confirm a row.

Scores: CRPS of the reference's normal total and the Brier score of P(over) at three lines around the reference's own centre,
paired "with minus without"; negative favours the multiplier. Seeds are fixed (20261108).
"""
from __future__ import annotations

import argparse
import csv
import math
import random
from collections import defaultdict
from pathlib import Path

SD = {"NBA": 19.4, "MLB": 4.5, "AFL": 29.1, "NRL": 13.9}
WINDOWS = (("postseason", lambda r: r["stage"] == "PLAYOFFS"),
           ("early 28 days", lambda r: r["stage"] == "REGULAR" and r["day"] < 28),
           ("early 14 days", lambda r: r["stage"] == "REGULAR" and r["day"] < 14))
SEED, DRAWS = 20261108, 4000


def _cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def _pdf(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


def scores(mu: float, y: float, centre: float, sd: float) -> tuple[float, float]:
    """(CRPS, Brier at three lines around the reference centre) for a normal total with mean mu."""
    z = (y - mu) / sd
    line = (round(centre * 2) / 2) if sd > 10 else math.floor(centre) + 0.5
    step = 4 if sd > 10 else max(1.0, round(sd / 4))
    brier = sum((1 - _cdf((line + d - mu) / sd) - (1.0 if y > line + d else 0.0)) ** 2 for d in (-step, 0, step)) / 3
    return sd * (z * (2 * _cdf(z) - 1) + 2 * _pdf(z) - 1 / math.sqrt(math.pi)), brier


def load(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as fh:
        return [dict(r, forecast_total=float(r["forecast_total"]), actual_total=float(r["actual_total"]), day=int(r["day"]))
                for r in csv.DictReader(fh)]


def _ratio(rows) -> float:
    return sum(r["actual_total"] for r in rows) / sum(r["forecast_total"] for r in rows)


def _held_out(league: str, sub: list[dict], fit_seasons) -> dict | None:
    """Paired scores where each season's multiplier comes from ``fit_seasons(season, all_seasons)``."""
    seasons = sorted({r["season"] for r in sub})
    diffs, ms, n, b0, b1 = defaultdict(list), [], 0, 0.0, 0.0
    for s in seasons:
        train = [r for r in sub if r["season"] in fit_seasons(s, seasons)]
        if not train:
            continue
        m = _ratio(train)
        ms.append(m)
        for r in sub:
            if r["season"] != s:
                continue
            c0, br0 = scores(r["forecast_total"], r["actual_total"], r["forecast_total"], SD[league])
            c1, br1 = scores(r["forecast_total"] * m, r["actual_total"], r["forecast_total"], SD[league])
            diffs[s].append((c1 - c0, br1 - br0))
            n += 1
            b0 += r["actual_total"] - r["forecast_total"]
            b1 += r["actual_total"] - r["forecast_total"] * m
    scored = sorted(diffs)
    if not n or len(scored) < 2:
        return None
    rng, bc, bb = random.Random(SEED), [], []
    for _ in range(DRAWS):
        picks = [rng.choice(scored) for _ in scored]
        c = [d[0] for k in picks for d in diffs[k]]
        b = [d[1] for k in picks for d in diffs[k]]
        bc.append(sum(c) / len(c))
        bb.append(sum(b) / len(b))
    bc.sort()
    bb.sort()
    allc = [d[0] for k in scored for d in diffs[k]]
    allb = [d[1] for k in scored for d in diffs[k]]
    lo, hi = int(0.025 * DRAWS), int(0.975 * DRAWS) - 1
    return dict(seasons_scored=len(scored), n=n, multipliers=f"{min(ms):.4f}-{max(ms):.4f}", bias_without=round(b0 / n, 3),
                bias_with=round(b1 / n, 3), crps_diff=round(sum(allc) / n, 5), crps_ci=f"[{bc[lo]:.5f}, {bc[hi]:.5f}]",
                brier_diff=round(sum(allb) / n, 5), brier_ci=f"[{bb[lo]:.5f}, {bb[hi]:.5f}]",
                seasons_improved=f"{sum(1 for s in scored if sum(d[0] for d in diffs[s]) < 0)}/{len(scored)}",
                both_below_zero=bc[hi] < 0 and bb[hi] < 0)


def loso(league: str, sub: list[dict]) -> dict | None:
    return _held_out(league, sub, lambda s, seasons: [x for x in seasons if x != s])


def chronological(league: str, sub: list[dict]) -> dict | None:
    """Expanding window: a season is scored with a multiplier fitted on earlier seasons only (the first season is not scored)."""
    return _held_out(league, sub, lambda s, seasons: [x for x in seasons if x < s])


def sizes(league: str, sub: list[dict]) -> dict:
    by = defaultdict(list)
    for r in sub:
        by[r["season"]].append(r)
    keys, rng, boots = sorted(by), random.Random(SEED), []
    for _ in range(DRAWS):
        s = [r for k in (rng.choice(keys) for _ in keys) for r in by[k]]
        boots.append(_ratio(s))
    boots.sort()
    ratio = _ratio(sub)
    return dict(seasons=f"{keys[0]}..{keys[-1]} ({len(keys)})", n=len(sub), ratio=round(ratio, 4), ci_low=round(boots[int(0.025 * DRAWS)], 4),
                ci_high=round(boots[int(0.975 * DRAWS) - 1], 4), proportional_estimate=round(ratio - 1, 4))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--outputs", type=Path, required=True)
    args = parser.parse_args(argv)
    out = {"REGIME_SIZES.csv": [], "LOSO_HELD_OUT.csv": [], "CHRONOLOGICAL.csv": []}
    for league in SD:
        path = args.outputs / f"{league}_WALKFORWARD_TOTALS.csv"
        if not path.exists():
            continue
        rows = load(path)
        for window, pick in WINDOWS:
            sub = [r for r in rows if pick(r)]
            if not sub:
                continue
            out["REGIME_SIZES.csv"].append(dict(league=league, window=window, **sizes(league, sub)))
            for name, fn in (("LOSO_HELD_OUT.csv", loso), ("CHRONOLOGICAL.csv", chronological)):
                r = fn(league, sub)
                if r:
                    out[name].append(dict(league=league, window=window, **r))
    for name, rows in out.items():
        with open(args.outputs / name, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
    for r in out["CHRONOLOGICAL.csv"]:
        print(r)


if __name__ == "__main__":
    main()
