#!/usr/bin/env python3
"""Card-versus-baseline skill comparison (C-BASELINE-SKILL, added 2026-09-25(c)).

Reads the decision table in SKILL_BASELINE_LEDGER.md. Each row is one issued decision (a forced
pair counted once) with the card's issued probability, a leak-free population baseline
probability for the same contract, and the result (W/L; P = push, which is excluded). It reports
the Brier score of each and their paired difference (card − baseline; negative = card better),
overall and by family. It also gives a 95% interval from a bootstrap that resamples whole cards,
because rows inside one card are not independent.

This is a descriptive LEARNING_ONLY diagnostic, not a performance claim
(PERFORMANCE_ELIGIBILITY_POLICY.md). The preregistered decision rule is in LEARNING_REGISTER.md
§"2026-09-25(c)" (C-BASELINE-SKILL).

Usage: python tools/skill_baseline.py [SKILL_BASELINE_LEDGER.md] [--boot 10000] [--seed 20260925]
"""
from __future__ import annotations

import argparse
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HEADER = re.compile(r"^\|\s*Decision\s*\|", re.I)


def parse(text: str) -> list[dict]:
    rows, cols = [], None
    for line in text.splitlines():
        if HEADER.match(line):
            cols = [c.strip().lower() for c in line.strip().strip("|").split("|")]
            continue
        if cols is None or not line.startswith("|") or re.match(r"^\|\s*-", line):
            if cols is not None and not line.startswith("|"):
                cols = None if line.strip() else cols
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != len(cols):
            continue
        r = dict(zip(cols, cells))
        try:
            rows.append({"decision": r["decision"], "card": r["card"], "family": r["family"],
                         "p": float(r["card p"]), "b": float(r["baseline p"]), "result": r["result"].upper()})
        except (KeyError, ValueError):
            continue
    return rows


def brier(p: float, y: int) -> float:
    return (p - y) ** 2


def summarise(rows: list[dict], boot: int = 10000, seed: int = 20260925) -> dict:
    seen, scored = set(), []
    for r in rows:
        if r["decision"] in seen or r["result"] not in ("W", "L"):
            continue
        seen.add(r["decision"])
        y = 1 if r["result"] == "W" else 0
        scored.append({**r, "y": y, "bc": brier(r["p"], y), "bb": brier(r["b"], y)})
    out = {"n": len(scored), "cards": len({r["card"] for r in scored}), "by_family": {}}
    if not scored:
        return out

    def block(rs):
        n = len(rs)
        bc = sum(r["bc"] for r in rs) / n
        bb = sum(r["bb"] for r in rs) / n
        return {"n": n, "card_brier": bc, "baseline_brier": bb, "diff": bc - bb,
                "card_better_rows": sum(1 for r in rs if r["bc"] < r["bb"])}

    out.update(block(scored))
    fam = defaultdict(list)
    for r in scored:
        fam[r["family"]].append(r)
    out["by_family"] = {k: block(v) for k, v in sorted(fam.items())}
    by_card = defaultdict(list)
    for r in scored:
        by_card[r["card"]].append(r)
    cards = list(by_card)
    rng = random.Random(seed)
    diffs = []
    for _ in range(boot):
        sample = [r for c in (rng.choice(cards) for _ in cards) for r in by_card[c]]
        diffs.append(sum(r["bc"] - r["bb"] for r in sample) / len(sample))
    diffs.sort()
    out["ci95"] = (diffs[int(0.025 * boot)], diffs[int(0.975 * boot) - 1])
    return out


def render(s: dict) -> str:
    if not s["n"]:
        return "No scored decisions with a baseline yet."
    lines = [f"Scored decisions: {s['n']} across {s['cards']} cards (forced pairs counted once; pushes excluded).",
             "",
             "| Scope | n | Card Brier | Baseline Brier | Card − baseline | Rows card better |",
             "|---|---:|---:|---:|---:|---:|",
             f"| **All** | {s['n']} | {s['card_brier']:.4f} | {s['baseline_brier']:.4f} | **{s['diff']:+.4f}** | {s['card_better_rows']}/{s['n']} |"]
    for k, v in s["by_family"].items():
        lines.append(f"| {k} | {v['n']} | {v['card_brier']:.4f} | {v['baseline_brier']:.4f} | {v['diff']:+.4f} | "
                     f"{v['card_better_rows']}/{v['n']} |")
    lo, hi = s["ci95"]
    verdict = ("card better than baseline (interval below 0)" if hi < 0 else
               "card worse than baseline (interval above 0)" if lo > 0 else
               "no demonstrated difference (interval spans 0)")
    lines += ["", f"Card-cluster bootstrap 95% interval for (card − baseline): [{lo:+.4f}, {hi:+.4f}] — **{verdict}**.",
              "Descriptive and LEARNING_ONLY; see C-BASELINE-SKILL for the preregistered decision rule."]
    return "\n".join(lines)


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ledger", nargs="?", default=str(REPO / "SKILL_BASELINE_LEDGER.md"))
    ap.add_argument("--boot", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=20260925)
    args = ap.parse_args(argv)
    rows = parse(Path(args.ledger).read_text(encoding="utf-8-sig"))
    print(render(summarise(rows, args.boot, args.seed)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
