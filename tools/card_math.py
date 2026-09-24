#!/usr/bin/env python3
"""Distribution → contract probabilities, baseline departure ledger (added 2026-09-25(d)).

Why. M14 ("total probability not derived from the card's own centre and width") and G-L8 require
every row's probability to be read off the card's own printed distribution. Hand arithmetic keeps
drifting from that. This module is the reference implementation of the queries. It is not a
fitted model: every parameter comes from the card itself (centre, width, family) or from a
population reference (BASE_RATES_REGISTER.md §7).

Distributions for a count or score variable X (a total, or a margin = side − opponent):
- "normal":   continuous normal(mean, sd), with a ±0.5 continuity correction for integer
  outcomes. For basketball points and cricket runs.
- "negbin":   negative binomial with the given mean and sd (sd² > mean). For baseball runs.
- "poisson":  Poisson(mean). For soccer/hockey goals, and corners.
- "skellam":  the difference of two Poissons (mu_side, mu_opp). For goal margins.
- no_zero:    for margins that can never finish level (basketball, MLB, NHL full game), the mass at
  0 is removed and the rest renormalised.

Queries (integer lines give push mass; half lines give none):
- p_over(L), p_under(L), p_push(L) for a total;
- p_cover(k) for "side +k" (margin + k > 0) and "side −k" (margin − k > 0);
- the joint probability of two threshold rows on the same variable (exact);
- logit departure from BASELINE_P, as a ledger of named mechanisms with their shares.

CLI examples:
    python tools/card_math.py total --dist negbin --mean 8.4 --sd 3.97 --line 7.5
    python tools/card_math.py total --dist normal --mean 179.75 --sd 17.07 --line 184.5
    python tools/card_math.py cover --dist normal --mean 1.44 --sd 13.63 --line -1.5 --no-zero
    python tools/card_math.py cover --dist skellam --mu 1.6 --mu-opp 1.1 --line 1.5
    python tools/card_math.py departure --p 0.613 --baseline 0.530 --mech "pace model:0.6" --mech "lineup:0.4"
"""
from __future__ import annotations

import argparse
import math
import sys

# ------------------------------------------------------------------ distributions


def _norm_cdf(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


class Dist:
    """P(X = k) on integers via pmf(k); P(X <= x) via cdf(x)."""

    def __init__(self, kind: str, mean: float = 0.0, sd: float | None = None, mu: float | None = None,
                 mu_opp: float | None = None, integer: bool = True, no_zero: bool = False):
        self.kind, self.mean, self.sd, self.integer = kind, mean, sd, integer
        self.no_zero = no_zero  # margins that can never finish level (basketball, MLB, NHL full game): condition on X != 0
        self.mu, self.mu_opp = mu, mu_opp
        if kind == "normal":
            if not sd or sd <= 0:
                raise ValueError("normal needs sd > 0")
        elif kind == "negbin":
            if not sd or sd * sd <= mean:
                raise ValueError("negbin needs sd^2 > mean (over-dispersion); use poisson otherwise")
            self.r = mean * mean / (sd * sd - mean)
            self.q = mean / (sd * sd)          # success probability in the (r, q) parameterisation
        elif kind == "poisson":
            if mean <= 0:
                raise ValueError("poisson needs mean > 0")
        elif kind == "skellam":
            if mu is None or mu_opp is None or mu <= 0 or mu_opp <= 0:
                raise ValueError("skellam needs mu > 0 and mu_opp > 0")
            self.mean = mu - mu_opp
        else:
            raise ValueError(f"unknown distribution {kind}")

    def pmf(self, k: int) -> float:
        if self.no_zero:
            if k == 0:
                return 0.0
            return self._raw_pmf(k) / (1.0 - self._raw_pmf(0))
        return self._raw_pmf(k)

    def _raw_pmf(self, k: int) -> float:
        if self.kind == "normal":
            if not self.integer:
                return 0.0
            return _norm_cdf((k + 0.5 - self.mean) / self.sd) - _norm_cdf((k - 0.5 - self.mean) / self.sd)
        if self.kind == "negbin":
            if k < 0:
                return 0.0
            return math.exp(math.lgamma(k + self.r) - math.lgamma(self.r) - math.lgamma(k + 1)
                            + self.r * math.log(self.q) + k * math.log(1 - self.q))
        if self.kind == "poisson":
            if k < 0:
                return 0.0
            return math.exp(-self.mean + k * math.log(self.mean) - math.lgamma(k + 1))
        # skellam: sum over the opponent's goals
        total, j = 0.0, max(0, -k)
        while j < 60:
            i = k + j
            total += math.exp(-self.mu + i * math.log(self.mu) - math.lgamma(i + 1)) * \
                math.exp(-self.mu_opp + j * math.log(self.mu_opp) - math.lgamma(j + 1))
            j += 1
        return total

    def _support(self) -> range:
        if self.kind in ("negbin", "poisson"):
            hi = int(self.mean + 12 * (self.sd or math.sqrt(self.mean)) + 30)
            return range(0, hi)
        if self.kind == "skellam":
            return range(-40, 41)
        span = int(10 * self.sd + 10)
        c = int(round(self.mean))
        return range(c - span, c + span + 1)

    def cdf(self, x: float) -> float:
        """P(X <= x)."""
        if self.kind == "normal" and not self.integer:
            return _norm_cdf((x - self.mean) / self.sd)
        return sum(self.pmf(k) for k in self._support() if k <= x + 1e-9)


# ------------------------------------------------------------------ contract queries


def p_over(d: Dist, line: float) -> float:
    """P(X > line). Integer outcomes: P(X >= floor(line) + 1). Continuous: 1 − cdf(line)."""
    if not d.integer:
        return 1.0 - d.cdf(line)
    return 1.0 - d.cdf(math.floor(line + 1e-9))


def p_push(d: Dist, line: float) -> float:
    if not d.integer or abs(line - round(line)) > 1e-9:
        return 0.0
    return d.pmf(int(round(line)))


def p_under(d: Dist, line: float) -> float:
    return 1.0 - p_over(d, line) - p_push(d, line)


def p_cover(d: Dist, line: float) -> tuple[float, float]:
    """For a margin variable X (side − opponent) and a handicap line on the side: win iff X + line > 0,
    push iff X + line = 0. Returns (P(win), P(push))."""
    threshold = -line                  # win iff X > threshold
    win = p_over(d, threshold)
    push = p_push(d, threshold)
    return win, push


def joint_threshold(d: Dist, a: tuple[str, float], b: tuple[str, float]) -> float:
    """Exact P(row A wins and row B wins) for two threshold rows on the same variable,
    e.g. ('Over', 7.5) and ('Under', 10.5). Each row is ('Over' | 'Under', line)."""
    def wins(row, k):
        side, line = row
        return k > line if side == "Over" else k < line
    if d.kind == "normal" and not d.integer:
        raise ValueError("joint_threshold needs an integer-valued distribution")
    return sum(d.pmf(k) for k in d._support() if wins(a, k) and wins(b, k))


def normalised_edge(mean: float, sd: float, line: float) -> float:
    return abs(mean - line) / sd


# ------------------------------------------------------------------ baseline departure ledger


def logit(p: float) -> float:
    return math.log(p / (1 - p))


def departure_ledger(p: float, baseline: float, mechanisms: list[tuple[str, float]]) -> dict:
    """Attribute the card's log-odds departure from BASELINE_P to named mechanisms.

    Each mechanism carries a share (a signed fraction of the total departure). The shares should
    sum to about 1. An unattributed residual share (|1 − sum| > 0.1) is reported as
    UNEXPLAINED_DEPARTURE. This is a disclosure (C-DEPARTURE-LEDGER), not a coefficient: the card
    chooses its own shares."""
    if not (0 < p < 1 and 0 < baseline < 1):
        raise ValueError("p and baseline must be strictly between 0 and 1")
    total = logit(p) - logit(baseline)
    shares = sum(s for _, s in mechanisms)
    rows = [(name, s, s * total) for name, s in mechanisms]
    return {"p": p, "baseline": baseline, "logit_departure": total,
            "rows": rows, "share_sum": shares, "unexplained_share": 1 - shares,
            "flag": "UNEXPLAINED_DEPARTURE" if abs(1 - shares) > 0.1 and abs(total) > 0.05 else "OK"}


# ------------------------------------------------------------------ CLI


def _dist_from(args) -> Dist:
    if args.dist == "skellam":
        return Dist("skellam", mu=args.mu, mu_opp=args.mu_opp, no_zero=args.no_zero)
    return Dist(args.dist, mean=args.mean, sd=args.sd, integer=not args.continuous, no_zero=args.no_zero)


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("total", "cover"):
        s = sub.add_parser(name)
        s.add_argument("--dist", choices=["normal", "negbin", "poisson", "skellam"], required=True)
        s.add_argument("--mean", type=float, default=0.0)
        s.add_argument("--sd", type=float)
        s.add_argument("--mu", type=float)
        s.add_argument("--mu-opp", type=float)
        s.add_argument("--line", type=float, required=True, action="append")
        s.add_argument("--continuous", action="store_true", help="no integer outcomes (no push)")
        s.add_argument("--no-zero", action="store_true",
                       help="margin can never be 0 (overtime/extras decide): condition on X != 0")
    d = sub.add_parser("departure")
    d.add_argument("--p", type=float, required=True)
    d.add_argument("--baseline", type=float, required=True)
    d.add_argument("--mech", action="append", default=[], help='"name:share" (shares sum to about 1)')
    args = ap.parse_args(argv)
    if args.cmd == "departure":
        mechs = []
        for m in args.mech:
            name, _, share = m.rpartition(":")
            mechs.append((name, float(share)))
        led = departure_ledger(args.p, args.baseline, mechs)
        print(f"p {led['p']:.3f} v BASELINE_P {led['baseline']:.3f}: logit departure {led['logit_departure']:+.3f}")
        for name, s, v in led["rows"]:
            print(f"  {name}: share {s:+.2f} → {v:+.3f} logits")
        print(f"  unexplained share {led['unexplained_share']:+.2f} → {led['flag']}")
        return 0
    dist = _dist_from(args)
    for line in args.line:
        if args.cmd == "total":
            o, u, pu = p_over(dist, line), p_under(dist, line), p_push(dist, line)
            edge = f"; normalised edge {normalised_edge(dist.mean, args.sd, line):.3f}" if args.sd else ""
            print(f"line {line:g}: P(Over) {o:.4f}  P(Under) {u:.4f}  P(push) {pu:.4f}{edge}")
        else:
            w, pu = p_cover(dist, line)
            print(f"side {line:+g}: P(cover) {w:.4f}  P(push) {pu:.4f}  P(lose) {1 - w - pu:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
