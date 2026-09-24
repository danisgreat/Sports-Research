#!/usr/bin/env python3
"""Calibration and resolution report for settled forecast rows (added 2026-09-25(d)).

Input: a CSV with at least the columns card, p, result (W/L/P/V), and optionally family,
sport, direction and rank. The default input is the dataset built by
research/settled_rows_2026-09-25/extract_settled_rows.py.

Output: a Markdown report containing
- a reliability table by stated-probability band, with Wilson intervals;
- the Murphy decomposition, Brier = reliability − resolution + uncertainty. Resolution is the
  skill that stated probabilities carry beyond the base rate; reliability is miscalibration;
- the logistic calibration slope and intercept of the outcome on logit(p). A slope below 1 means
  the probabilities are too extreme, above 1 too timid;
- the card-cluster bootstrap interval of (win rate − mean stated p) for each slice (by family,
  sport, direction and rank). Rows within a card are dependent, so whole cards are resampled.

"Decisions" are rows with p ≥ 0.5, the preferred sides. They avoid double-counting forced-pair
complements.

LEARNING_ONLY. The report describes the framework's own record. Nothing in it may be fitted back
into a forecast as a shrink, weight or cap (L-087, SCORING_AND_VALIDATION.md §14).

Usage:
    python tools/calibration_report.py [research/settled_rows_2026-09-25/settled_rows.csv] [--all-rows] [--min-n 10]
"""
from __future__ import annotations

import argparse
import csv
import math
import random
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT = REPO / "research" / "settled_rows_2026-09-25" / "settled_rows.csv"
BANDS = [(0.0, 0.4), (0.4, 0.5), (0.5, 0.55), (0.55, 0.6), (0.6, 0.65), (0.65, 0.7), (0.7, 0.8), (0.8, 1.0001)]


def load(path: Path) -> list[dict]:
    out = []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            res = (r.get("result") or "").strip().upper()[:1]
            p = (r.get("p") or "").strip()
            if res not in ("W", "L") or not p:
                continue
            pf = float(p)
            if not 0.0 < pf < 1.0:
                continue
            out.append({"card": r.get("card", ""), "p": pf, "y": 1 if res == "W" else 0,
                        "family": r.get("family", ""), "sport": r.get("sport", ""),
                        "direction": r.get("direction", ""), "rank": r.get("rank", "")})
    return out


def wilson(k: int, n: int) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    z, p = 1.96, k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (c - h, c + h)


def brier(rs: list[dict]) -> float:
    return sum((r["p"] - r["y"]) ** 2 for r in rs) / len(rs)


def murphy(rs: list[dict], bins: int = 10) -> dict:
    n = len(rs)
    obar = sum(r["y"] for r in rs) / n
    groups = defaultdict(list)
    for r in rs:
        groups[min(int(r["p"] * bins), bins - 1)].append(r)
    rel = sum(len(g) * (sum(x["p"] for x in g) / len(g) - sum(x["y"] for x in g) / len(g)) ** 2 for g in groups.values()) / n
    res = sum(len(g) * (sum(x["y"] for x in g) / len(g) - obar) ** 2 for g in groups.values()) / n
    unc = obar * (1 - obar)
    return {"reliability": rel, "resolution": res, "uncertainty": unc, "brier": brier(rs),
            "skill_vs_climatology": 1 - brier(rs) / unc if unc else float("nan")}


def logistic_calibration(rs: list[dict]) -> tuple[float, float, float]:
    xs = [math.log(r["p"] / (1 - r["p"])) for r in rs]
    ys = [r["y"] for r in rs]
    a, b, det, h00 = 0.0, 1.0, 0.0, 0.0
    for _ in range(100):
        g0 = g1 = h00 = h01 = h11 = 0.0
        for x, y in zip(xs, ys):
            q = 1 / (1 + math.exp(-(a + b * x)))
            g0 += y - q
            g1 += (y - q) * x
            w = q * (1 - q)
            h00 += w
            h01 += w * x
            h11 += w * x * x
        det = h00 * h11 - h01 * h01
        if abs(det) < 1e-12:
            break
        da = (h11 * g0 - h01 * g1) / det
        db = (-h01 * g0 + h00 * g1) / det
        a, b = a + da, b + db
        if abs(da) + abs(db) < 1e-10:
            break
    se = math.sqrt(h00 / det) if det > 0 else float("nan")
    return a, b, se


def cluster_gap_ci(rs: list[dict], boot: int = 4000, seed: int = 20260925) -> tuple[float, float]:
    by = defaultdict(list)
    for r in rs:
        by[r["card"]].append(r)
    cards = list(by)
    rng = random.Random(seed)
    vals = []
    for _ in range(boot):
        s = [x for c in (rng.choice(cards) for _ in cards) for x in by[c]]
        vals.append(sum(x["y"] for x in s) / len(s) - sum(x["p"] for x in s) / len(s))
    vals.sort()
    return vals[int(0.025 * boot)], vals[int(0.975 * boot) - 1]


def slice_row(label: str, rs: list[dict], boot: int) -> str:
    n, k = len(rs), sum(r["y"] for r in rs)
    mp = sum(r["p"] for r in rs) / n
    lo, hi = cluster_gap_ci(rs, boot)
    flag = " **over-confident**" if hi < 0 else (" **under-confident**" if lo > 0 else "")
    return (f"| {label} | {n} | {len({r['card'] for r in rs})} | {k / n:.3f} | {mp:.3f} | {k / n - mp:+.3f} "
            f"[{lo:+.3f}, {hi:+.3f}]{flag} | {brier(rs):.4f} |")


def report(rows: list[dict], all_rows: bool = False, min_n: int = 10, boot: int = 4000) -> str:
    dec = rows if all_rows else [r for r in rows if r["p"] >= 0.5]
    scope = "all graded rows with p" if all_rows else "decisions (p ≥ 0.5: preferred sides; complements not double-counted)"
    out = [f"### Calibration report — {scope}", "",
           f"Rows: {len(dec)} from {len({r['card'] for r in dec})} cards (input rows with p: {len(rows)}).", ""]
    m = murphy(rows)
    a, b, se = logistic_calibration(rows)
    out += ["**All graded rows with p:**",
            f"- Brier {m['brier']:.4f};",
            f"- Murphy decomposition: reliability {m['reliability']:.4f}, resolution {m['resolution']:.4f}, "
            f"uncertainty {m['uncertainty']:.4f};",
            f"- skill against climatology {m['skill_vs_climatology']:+.1%};",
            f"- logistic calibration slope {b:.2f} (SE {se:.2f}), intercept {a:+.2f}.",
            ""]
    out += ["| Stated band | n | cards | win rate (Wilson 95%) | mean p |", "|---|---:|---:|---|---:|"]
    for lo, hi in BANDS:
        g = [r for r in rows if lo <= r["p"] < hi]
        if g:
            k = sum(r["y"] for r in g)
            wl, wh = wilson(k, len(g))
            out.append(f"| {lo:.2f}–{min(hi, 1):.2f} | {len(g)} | {len({r['card'] for r in g})} | "
                       f"{k / len(g):.3f} ({wl:.3f}–{wh:.3f}) | {sum(r['p'] for r in g) / len(g):.3f} |")
    for key in ("family", "sport", "direction", "rank"):
        groups = defaultdict(list)
        for r in dec:
            if r[key]:
                groups[r[key]].append(r)
        shown = [(k, v) for k, v in sorted(groups.items(), key=lambda kv: -len(kv[1])) if len(v) >= min_n]
        if not shown:
            continue
        out += ["", f"**By {key}** (slices with n ≥ {min_n}; gap = win rate − mean p, with the card-cluster 95% interval)", "",
                "| Slice | n | cards | win rate | mean p | gap [95%] | Brier |", "|---|---:|---:|---:|---:|---|---:|"]
        out += [slice_row(str(k), v, boot) for k, v in shown]
    out += ["", "Descriptive and LEARNING_ONLY. Nothing here is a coefficient (L-087)."]
    return "\n".join(out)


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", nargs="?", default=str(DEFAULT))
    ap.add_argument("--all-rows", action="store_true")
    ap.add_argument("--min-n", type=int, default=10)
    ap.add_argument("--boot", type=int, default=4000)
    args = ap.parse_args(argv)
    rows = load(Path(args.csv))
    if not rows:
        print("no graded rows with probabilities")
        return 0
    print(report(rows, args.all_rows, args.min_n, args.boot))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
