#!/usr/bin/env python3
"""Closing-line benchmark — scoring only, after settlement (C-MARKET-BENCHMARK, added 2026-09-26).

Why. The framework is market-blind by design: no price, line movement or tipster material may
inform a forecast, a rank, a rule or a retrospective. That firewall is unchanged. What it left
missing is the strongest public yardstick. A card that cannot beat a table of league outcome
rates (C-BASELINE-SKILL) has not yet shown skill. A card that beats that table but loses badly
to the closing market has shown only that it knows more than a table. The 2026-09-26 review
recommended recording the closing line **for scoring only, after the event is settled**, so the
framework can say where its probabilities stand against the market without the market ever
touching a card.

Firewall (enforced here and in MARKET_BENCHMARK_LEDGER.md):
- the operator enters the closing price after the event has settled; `Entered (UTC)` must be
  later than `Settled (UTC)`, or the row is INVALID_ENTRY_ORDER and excluded;
- only the no-vig closing probability and the de-vig method are stored, never the raw odds;
- agent sessions never fetch betting sites and never read this ledger while building a card
  (it is outside the reading gate); no rule, weight, rank or retrospective may cite it;
- nothing here is a value, ROI or performance claim (METHOD §1; PERFORMANCE_ELIGIBILITY_POLICY).

Commands:
  python tools/market_benchmark.py devig --odds 1.91 1.95 [--method multiplicative|power|shin]
  python tools/market_benchmark.py devig --american -110 -105
  python tools/market_benchmark.py report [MARKET_BENCHMARK_LEDGER.md] [--boot 10000]

`devig` prints no-vig probabilities for a complete market (both sides of a two-way market, all
three of a 1X2). It stores nothing. `report` gives the paired Brier (card − market; negative means
the card was better) overall and by family, with a bootstrap that resamples whole cards.
Standard library only; no network.
"""
from __future__ import annotations

import argparse
import datetime as dt
import math
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HEADER = re.compile(r"^\|\s*Decision\s*\|", re.I)
METHODS = ("multiplicative", "power", "shin")


# --------------------------------------------------------------------------- de-vig

def implied(odds: list[float]) -> list[float]:
    if len(odds) < 2 or any((not math.isfinite(o)) or o <= 1.0 for o in odds):
        raise ValueError("need at least two decimal odds, each > 1.0")
    return [1.0 / o for o in odds]


def american_to_decimal(a: float) -> float:
    if a == 0 or -100 < a < 100:
        raise ValueError(f"invalid American odds {a}")
    return 1 + (a / 100.0 if a > 0 else 100.0 / -a)


def _bisect(f, lo: float, hi: float, tol: float = 1e-12, it: int = 200) -> float:
    flo = f(lo)
    for _ in range(it):
        mid = (lo + hi) / 2
        fm = f(mid)
        if abs(fm) < tol or hi - lo < tol:
            return mid
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


def devig(odds: list[float], method: str = "multiplicative") -> list[float]:
    """No-vig probabilities for a complete market. The overround must be >= 0."""
    q = implied(odds)
    s = sum(q)
    if s < 1 - 1e-9:
        raise ValueError(f"implied probabilities sum to {s:.4f} < 1: not a complete market")
    if method == "multiplicative":
        p = [x / s for x in q]
    elif method == "power":
        k = _bisect(lambda k: sum(x ** k for x in q) - 1.0, 1.0, 50.0)
        p = [x ** k for x in q]
    elif method == "shin":
        if s - 1 < 1e-12:
            p = list(q)
        else:
            def shin_p(z):
                return [(math.sqrt(z * z + 4 * (1 - z) * x * x / s) - z) / (2 * (1 - z)) for x in q]
            z = _bisect(lambda z: sum(shin_p(z)) - 1.0, 0.0, 0.4999)
            p = shin_p(z)
    else:
        raise ValueError(f"unknown method {method}; use one of {METHODS}")
    t = sum(p)
    return [x / t for x in p]


# --------------------------------------------------------------------------- ledger

def parse_ts(s: str) -> dt.datetime | None:
    s = s.strip()
    if not s:
        return None
    try:
        t = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
    return t if t.tzinfo else None


def parse(text: str) -> list[dict]:
    rows, cols = [], None
    for line in text.splitlines():
        if HEADER.match(line):
            cols = [c.strip().lower() for c in line.strip().strip("|").split("|")]
            continue
        if cols is None or not line.startswith("|") or re.match(r"^\|\s*-", line):
            if cols is not None and not line.startswith("|") and line.strip():
                cols = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != len(cols):
            continue
        r = dict(zip(cols, cells))
        try:
            row = {"decision": r["decision"], "card": r["card"], "family": r["family"],
                   "p": float(r["card p"]), "m": float(r["market p (no-vig close)"]),
                   "method": r.get("method", ""), "result": r["result"].upper(),
                   "settled": parse_ts(r.get("settled (utc)", "")), "entered": parse_ts(r.get("entered (utc)", ""))}
        except (KeyError, ValueError):
            continue
        if not (0 < row["p"] < 1 and 0 < row["m"] < 1):
            continue
        rows.append(row)
    return rows


def validate(rows: list[dict]) -> tuple[list[dict], list[tuple[str, str]]]:
    ok, bad = [], []
    for r in rows:
        if r["settled"] is None or r["entered"] is None:
            bad.append((r["decision"], "MISSING_TIMESTAMP"))
        elif r["entered"] <= r["settled"]:
            bad.append((r["decision"], "INVALID_ENTRY_ORDER (entered before settlement)"))
        elif r["method"] not in METHODS:
            bad.append((r["decision"], "UNKNOWN_DEVIG_METHOD"))
        else:
            ok.append(r)
    return ok, bad


def summarise(rows: list[dict], boot: int = 10000, seed: int = 20260926) -> dict:
    seen, scored = set(), []
    for r in rows:
        if r["decision"] in seen or r["result"] not in ("W", "L"):
            continue
        seen.add(r["decision"])
        y = 1 if r["result"] == "W" else 0
        scored.append({**r, "y": y, "bc": (r["p"] - y) ** 2, "bm": (r["m"] - y) ** 2})
    out = {"n": len(scored), "cards": len({r["card"] for r in scored}), "by_family": {}}
    if not scored:
        return out

    def block(rs):
        n = len(rs)
        return {"n": n, "card_brier": sum(r["bc"] for r in rs) / n, "market_brier": sum(r["bm"] for r in rs) / n,
                "diff": sum(r["bc"] - r["bm"] for r in rs) / n,
                "card_better_rows": sum(1 for r in rs if r["bc"] < r["bm"]),
                "mean_gap": sum(r["p"] - r["m"] for r in rs) / n}

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
        diffs.append(sum(r["bc"] - r["bm"] for r in sample) / len(sample))
    diffs.sort()
    out["ci95"] = (diffs[int(0.025 * boot)], diffs[int(0.975 * boot) - 1])
    return out


def render(s: dict, bad: list[tuple[str, str]]) -> str:
    lines = []
    if bad:
        lines += ["Excluded rows (firewall):", *[f"- `{d}`: {why}" for d, why in bad], ""]
    if not s["n"]:
        return "\n".join(lines + ["No scored decisions with a closing-line probability yet."])
    lines += [f"Scored decisions: {s['n']} across {s['cards']} cards (forced pairs counted once; pushes excluded).", "",
              "| Scope | n | Card Brier | Market Brier | Card − market | Rows card better | Mean (p − market) |",
              "|---|---:|---:|---:|---:|---:|---:|",
              f"| **All** | {s['n']} | {s['card_brier']:.4f} | {s['market_brier']:.4f} | **{s['diff']:+.4f}** | "
              f"{s['card_better_rows']}/{s['n']} | {s['mean_gap']:+.3f} |"]
    for k, v in s["by_family"].items():
        lines.append(f"| {k} | {v['n']} | {v['card_brier']:.4f} | {v['market_brier']:.4f} | {v['diff']:+.4f} | "
                     f"{v['card_better_rows']}/{v['n']} | {v['mean_gap']:+.3f} |")
    lo, hi = s["ci95"]
    verdict = ("card better than the closing line (interval below 0)" if hi < 0 else
               "card worse than the closing line (interval above 0)" if lo > 0 else
               "no demonstrated difference from the closing line (interval spans 0)")
    lines += ["", f"Card-cluster bootstrap 95% interval for (card − market): [{lo:+.4f}, {hi:+.4f}] — **{verdict}**.",
              "Scoring-only and LEARNING_ONLY. Not a value, ROI or performance claim (C-MARKET-BENCHMARK)."]
    return "\n".join(lines)


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("devig")
    g = d.add_mutually_exclusive_group(required=True)
    g.add_argument("--odds", type=float, nargs="+", help="decimal odds for every outcome of the market")
    g.add_argument("--american", type=float, nargs="+", help="American odds for every outcome")
    d.add_argument("--method", choices=METHODS, default="multiplicative")
    r = sub.add_parser("report")
    r.add_argument("ledger", nargs="?", default=str(REPO / "MARKET_BENCHMARK_LEDGER.md"))
    r.add_argument("--boot", type=int, default=10000)
    r.add_argument("--seed", type=int, default=20260926)
    args = ap.parse_args(argv)
    if args.cmd == "devig":
        odds = args.odds if args.odds else [american_to_decimal(a) for a in args.american]
        p = devig(odds, args.method)
        over = sum(implied(odds)) - 1
        print(f"Method {args.method}; overround {over:+.2%}. No-vig probabilities (record these, not the odds):")
        for i, x in enumerate(p, 1):
            print(f"  outcome {i}: {x:.4f}")
        return 0
    rows = parse(Path(args.ledger).read_text(encoding="utf-8-sig"))
    ok, bad = validate(rows)
    print(render(summarise(ok, args.boot, args.seed), bad))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
