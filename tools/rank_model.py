#!/usr/bin/env python3
"""RM-1 — the ranking-probability model (added 2026-09-25(e), user-authorised).

Why. Rank 1 and Rank 2 are chosen by probability, so the probability they are chosen by must be
the best available estimate. The full settled record (research/rank_model_2026-09-25e/README.md)
shows that the stated probabilities are informative but mis-stated in two pooled, repeatable ways:
1. They are too timid at the top and too generous in the middle. A logistic recalibration slope
   of about 1.5 on logit(stated p) fits the record: rows stated at 0.55 won about 53%, rows stated at
   0.75 won about 83%.
2. Underdog cushions (+k.5) outside baseball, hockey and soccer (basketball, NFL/NCAA, AFL, rugby,
   tennis games, cricket) are badly over-stated: 7 of 27 won at a stated ~0.58. The effect held
   in every time split (before P-420, after P-420, after P-450, after P-480).
RM-1 is exactly those two corrections: a logistic model of the outcome on logit(stated p), with one
unpenalised offset for that cushion class. In out-of-sample tests (leave-one-card-out and four
forward-in-time splits) it beat the stated probabilities on log loss in every split, and ranking
by it raised the held-out top-two win count (leave-one-card-out +0.068 wins per card, 95% interval
[+0.007, +0.128]; Rank 1 64.2% -> 68.9%), and Rank 1 and Rank 2 were never lower in any forward split.

A richer challenger (RM-1X: ridge-penalised sport slopes, sport offsets and market-class offsets)
was tested and FAILED: cross-validation drove its ridge weight to the maximum and it did not beat
RM-1. It is kept, switched off, so each 25-card review can re-test it (`fit --terms ...`).

Status. RM-1 is a USER-AUTHORISED exception to L-087 ("no coefficient from this log's own
results"), made on the user's instruction of 2026-09-25 to build a calibration or probability
model if one could be built. The safeguards that stand in for L-087 are in RULES_GENERAL.md
§"2026-09-25(e)": pooled terms only, pre-specified, validated out of sample and forward in time,
refitted only at the 25-card review, and the stated probability is always printed unchanged beside
the calibrated one. RM-1 reads no odds, prices or market material of any kind.

How a row is scored. Every binary row has a decision side, the side with stated p >= 0.5. For a row
stated below 0.5, RM-1 scores its complement (class mapped by complement_class) and returns 1 − q, so
a row and its complement always sum to one. A strongly biased class can therefore flip the
preferred side of a pair (flag SIDE_FLIP).

    logit(q) = a + b * logit(p) + c * [decision side is a +k.5 cushion outside baseball, hockey and soccer]

Commands:
    python tools/rank_model.py score --sport nbl --contract "Hawks +1.5" --p 0.54
    python tools/rank_model.py rank --sport mlb --row "Cardinals +1.5=0.602" --row "Over 6.5 Runs=0.596" \\
                                     --row "Pirates ML=0.558" --row "Under 6.5 Runs=0.404"
    python tools/rank_model.py fit --fitted 2026-09-25 --out tools/rank_model_coefficients.json
    python tools/rank_model.py show

Standard library only (CI runs on plain Python 3.12).
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_CSV = REPO / "research" / "settled_rows_2026-09-25" / "settled_rows.csv"
DEFAULT_COEF = Path(__file__).resolve().parent / "rank_model_coefficients.json"

SPORT_GROUPS = ["soccer", "mlb", "asia_bb", "basketball", "cricket", "tennis", "oval", "hockey"]
MARKET_CLASSES = ["phase_over", "phase_under", "tt_over", "tt_under", "corners", "total_over", "total_under",
                  "hcp_plus_low", "hcp_plus_soccer", "hcp_plus_nb", "hcp_minus", "ml", "dc", "other"]
COMPLEMENT = {"phase_over": "phase_under", "phase_under": "phase_over", "tt_over": "tt_under",
              "tt_under": "tt_over", "total_over": "total_under", "total_under": "total_over",
              "hcp_plus_low": "hcp_minus", "hcp_plus_soccer": "hcp_minus", "hcp_plus_nb": "hcp_minus",
              "hcp_minus": None, "ml": "ml", "dc": "ml", "corners": "corners", "other": "other"}

# Model terms. "cushion_nb" is the pre-specified RM-1 term. The others make up the ridge challenger
# RM-1X, which failed validation and is switched off.
TERMS = ("cushion_nb", "sport_slope", "sport", "class")
DEFAULT_TERMS = ("cushion_nb",)

# Selection tiers read off the calibrated probability q (RULES_GENERAL.md §"2026-09-25(e)").
# Held-out record by tier: STRONG decisions won 81% (as Rank 1, 73%); every tier below 0.70 won 52–63%.
TIERS = [(0.70, "STRONG"), (0.62, "SUPPORTED"), (0.55, "LEAN"), (0.0, "COIN_FLIP")]
FLIP_MARGIN = 0.05

# ------------------------------------------------------------------ classification

_SPORT_ALIASES = {
    "soccer": ["soccer", "football-soccer", "epl", "mls", "uefa", "ucl", "uel", "a-league", "laliga", "serie a",
               "bundesliga", "ligue 1", "eredivisie", "liga mx", "j1", "j-league", "k league", "nwsl", "wsl", "afc",
               "acl", "acle"],
    "mlb": ["mlb", "baseball-mlb"],
    "asia_bb": ["npb", "kbo", "cpbl", "baseball-npb/kbo/cpbl", "baseball-other", "baseball", "lmb-baseball"],
    "basketball": ["basketball", "nba", "wnba", "nbl", "fiba", "lkl", "lnbp", "euroleague", "eurocup", "bcl", "acb"],
    "cricket": ["cricket", "t20", "t20i", "odi", "ipl", "bbl", "cpl", "psl", "test"],
    "tennis": ["tennis", "atp", "wta", "itf", "challenger"],
    "oval": ["oval", "nfl", "ncaa", "american-football", "afl", "aflw", "nrl", "nrlw", "rugby", "rugby-league",
             "rugby-union", "super rugby"],
    "hockey": ["hockey", "ice-hockey", "nhl", "ahl", "khl", "shl", "aihl"],
}


def sport_group(sport: str) -> str:
    s = (sport or "").strip().lower()
    for g, names in _SPORT_ALIASES.items():
        if s == g or s in names:
            return g
    for g, names in _SPORT_ALIASES.items():
        if any(re.search(r"\b" + re.escape(n) + r"\b", s) for n in names):
            return g
    raise ValueError(f"unknown sport {sport!r}; use one of {', '.join(SPORT_GROUPS)} or a league name")


def classify_family(contract: str) -> str:
    """Same rules as research/settled_rows_2026-09-25/extract_settled_rows.py (a test keeps them in step)."""
    cl = contract.lower()
    if re.search(r"corner", cl):
        return "corners"
    if re.search(r"\bcards?\b|booking", cl):
        return "cards"
    if re.search(r"first half|\b1h\b|first 5\b|\bf5\b|first five|first 6|first six|powerplay|\bq[1-4]\b|quarter|first period|"
                 r"1st half|overs? 0\.1|first \d+ (legal )?overs|1st period|first innings|1st innings|after \d+ overs", cl):
        return "phase"
    if re.search(r"team total|\bto score\b", cl):
        return "team-total"
    if re.search(r"\bover\b|\bunder\b|\btotal\b", cl):
        return "total"
    if re.search(r"[+−–-]\s*\d+(\.\d+)?|run ?line|puck ?line|spread|handicap|cushion", cl):
        return "handicap"
    if re.search(r"\bml\b|moneyline|to win|winner|\bwin\b|draw no bet|double chance|\bdnb\b|\bdraw\b|\b1x\b|\bx2\b", cl):
        return "moneyline"
    if re.search(r"player|strikeouts?|\bhits?\b|assists|rebounds|shots|aces|sixes|fours", cl):
        return "prop"
    return "other"


def direction(contract: str) -> str:
    cl = contract.lower()
    if re.search(r"\bover\b", cl):
        return "Over"
    if re.search(r"\bunder\b", cl):
        return "Under"
    m = re.search(r"([+−–-])\s*(\d+(?:\.\d+)?)", contract)
    if m:
        return "plus" if m.group(1) == "+" else "minus"
    return ""


def market_class(group: str, family: str, dirn: str, contract: str) -> str:
    d = (dirn or "").lower()
    if family == "handicap":
        if d == "plus":
            if group in ("mlb", "asia_bb", "hockey"):
                # low-scoring sports: one-unit margins are common, so +1.5 is a real cushion
                # (MLB one-run games 27.6%; the RM-1 penalty's evidence holds 1 hockey row of 28)
                return "hcp_plus_low"
            if group == "soccer":
                # "+0.5 / 1X" is a double chance, not a cushion
                return "dc" if re.search(r"\+\s*0\.5\b", contract) else "hcp_plus_soccer"
            return "hcp_plus_nb"
        return "hcp_minus"
    if family in ("total", "phase", "team-total"):
        prefix = {"total": "total", "phase": "phase", "team-total": "tt"}[family]
        if d in ("over", "under"):
            return f"{prefix}_{d}"
        return "other"
    if family == "corners":
        return "corners"
    if family == "moneyline":
        if re.search(r"double chance|\b1x\b|\bx2\b|or draw|draw no bet|\bdnb\b", contract.lower()):
            return "dc"
        return "ml"
    return "other"


def complement_class(cls: str, group: str) -> str:
    c = COMPLEMENT[cls]
    if c is None:  # the complement of a favourite's −k.5 is the underdog's +k.5
        if group in ("mlb", "asia_bb", "hockey"):
            return "hcp_plus_low"
        return "hcp_plus_soccer" if group == "soccer" else "hcp_plus_nb"
    return c


# ------------------------------------------------------------------ design and fitting


def _logit(p: float) -> float:
    p = min(max(p, 1e-4), 1 - 1e-4)
    return math.log(p / (1 - p))


def _sig(x: float) -> float:
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    e = math.exp(x)
    return e / (1 + e)


def feature_names(terms=DEFAULT_TERMS) -> list[str]:
    names = ["intercept", "logit_p"]
    if "cushion_nb" in terms:
        names.append("cushion_nb")
    if "sport_slope" in terms:
        names += [f"slope:{g}" for g in SPORT_GROUPS]
    if "sport" in terms:
        names += [f"sport:{g}" for g in SPORT_GROUPS]
    if "class" in terms:
        names += [f"class:{c}" for c in MARKET_CLASSES]
    return names


def features(group: str, cls: str, p: float, terms=DEFAULT_TERMS) -> list[float]:
    lp = _logit(p)
    x = [1.0, lp]
    if "cushion_nb" in terms:
        x.append(1.0 if cls == "hcp_plus_nb" else 0.0)
    if "sport_slope" in terms:
        x += [lp if g == group else 0.0 for g in SPORT_GROUPS]
    if "sport" in terms:
        x += [1.0 if g == group else 0.0 for g in SPORT_GROUPS]
    if "class" in terms:
        x += [1.0 if c == cls else 0.0 for c in MARKET_CLASSES]
    return x


def penalty_vector(lam: float, terms=DEFAULT_TERMS) -> list[float]:
    """The intercept, the slope and the pre-specified cushion term are unpenalised; the challenger
    terms carry the ridge weight lam."""
    pen = [0.0, 0.0]
    if "cushion_nb" in terms:
        pen.append(0.0)
    for t, k in (("sport_slope", len(SPORT_GROUPS)), ("sport", len(SPORT_GROUPS)), ("class", len(MARKET_CLASSES))):
        if t in terms:
            pen += [lam] * k
    return pen


def _solve(a: list[list[float]], b: list[float]) -> list[float]:
    """Gaussian elimination with partial pivoting (the systems here are at most ~35 × 35)."""
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        m[col], m[piv] = m[piv], m[col]
        if abs(m[col][col]) < 1e-12:
            raise ArithmeticError("singular system")
        for r in range(col + 1, n):
            f = m[r][col] / m[col][col]
            if f:
                for k in range(col, n + 1):
                    m[r][k] -= f * m[col][k]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (m[r][n] - sum(m[r][k] * x[k] for k in range(r + 1, n))) / m[r][r]
    return x


def fit_logistic(xs: list[list[float]], ys: list[int], penalties: list[float], iters: int = 50,
                 init: list[float] | None = None) -> list[float]:
    """Ridge-penalised logistic regression by Newton–Raphson. penalties[j] is the L2 weight on w[j]
    (0 = unpenalised). A tiny jitter keeps an all-zero column (a term absent from the data) solvable."""
    k = len(xs[0])
    w = list(init) if init else [0.0] * k
    for _ in range(iters):
        grad = [-penalties[j] * w[j] for j in range(k)]
        hess = [[0.0] * k for _ in range(k)]
        for j in range(k):
            hess[j][j] = -penalties[j] - 1e-6
        for x, y in zip(xs, ys):
            mu = _sig(sum(wj * xj for wj, xj in zip(w, x)))
            r = y - mu
            v = mu * (1 - mu)
            nz = [j for j in range(k) if x[j] != 0.0]
            for j in nz:
                grad[j] += r * x[j]
                for l in nz:
                    hess[j][l] -= v * x[j] * x[l]
        step = _solve([[-h for h in row] for row in hess], grad)
        w = [wj + sj for wj, sj in zip(w, step)]
        if max(abs(s) for s in step) < 1e-9:
            break
    return w


def load_decision_rows(path: Path) -> list[dict]:
    """Settled rows with a stated p >= 0.5 and a W/L result, classified. Rows stated below 0.5 are
    the complements of decisions already present (forced pairs), so they are not refitted."""
    out = []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            res = (r.get("result") or "").strip().upper()[:1]
            p = (r.get("p") or "").strip()
            if res not in ("W", "L") or not p:
                continue
            pf = float(p)
            if not 0.5 <= pf < 1.0:
                continue
            try:
                g = sport_group(r.get("sport", ""))
            except ValueError:
                continue
            fam = r.get("family") or classify_family(r.get("contract", ""))
            cls = market_class(g, fam, r.get("direction", ""), r.get("contract", ""))
            num = str(r.get("num") or "")
            out.append({"card": r.get("card", ""), "num": int(num) if num.isdigit() else None,
                        "rank": int(r["rank"]) if str(r.get("rank", "")).isdigit() else None,
                        "group": g, "cls": cls, "p": pf, "y": 1 if res == "W" else 0,
                        "contract": r.get("contract", "")})
    return out


def fit(rows: list[dict], lam: float = 0.0, terms=DEFAULT_TERMS) -> dict:
    terms = tuple(t for t in TERMS if t in terms)
    xs = [features(r["group"], r["cls"], r["p"], terms) for r in rows]
    ys = [r["y"] for r in rows]
    # start at the identity map (q = p); the ridge shrinks challenger terms toward "no correction"
    init = [0.0, 1.0] + [0.0] * (len(xs[0]) - 2)
    w = fit_logistic(xs, ys, penalty_vector(lam, terms), init=init)
    return {"weights": dict(zip(feature_names(terms), w)), "terms": list(terms), "lam": lam, "n": len(rows),
            "cards": len({r["card"] for r in rows})}


# ------------------------------------------------------------------ prediction


def load_coef(path: Path = DEFAULT_COEF) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _q_decision(coef: dict, group: str, cls: str, p: float) -> float:
    w = coef["weights"]
    terms = tuple(coef.get("terms", DEFAULT_TERMS))
    x = features(group, cls, p, terms)
    return _sig(sum(w[name] * xi for name, xi in zip(feature_names(terms), x)))


Q_MIN, Q_MAX = 0.03, 0.97   # the record has too few rows beyond these to support a more extreme q


def calibrate(coef: dict, group: str, cls: str, p: float) -> float:
    """Calibrated probability q for a row of class cls stated at p (either side of 0.5)."""
    if not 0.0 < p < 1.0:
        raise ValueError("p must be strictly between 0 and 1")
    if abs(p - 0.5) < 1e-9:
        return 0.5          # an exact tie has no decision side; both rows stay at 0.5
    if p >= 0.5:
        q = _q_decision(coef, group, cls, p)
    else:
        q = 1.0 - _q_decision(coef, group, complement_class(cls, group), 1.0 - p)
    return min(max(q, Q_MIN), Q_MAX)


def tier(q: float) -> str:
    for lo, name in TIERS:
        if q >= lo:
            return name
    return "COIN_FLIP"


def score_row(coef: dict, sport: str, contract: str, p: float) -> dict:
    g = sport_group(sport)
    fam = classify_family(contract)
    cls = market_class(g, fam, direction(contract), contract)
    q = calibrate(coef, g, cls, p)
    flags = []
    t = tier(q)
    if (p > 0.5) != (q > 0.5) and abs(p - 0.5) > 1e-9:
        if abs(q - 0.5) >= FLIP_MARGIN:
            # A material flip. Held out, flips driven by the cushion term were calibrated (26 rows, mean q
            # 0.307, won 0.308); the side the model now prefers is capped at SUPPORTED because the card's own
            # evidence did not choose it.
            flags.append("SIDE_FLIP")
            if t == "STRONG":
                t = "SUPPORTED"
        else:
            flags.append("NEAR_TIED_FLIP")   # a flip within 0.05 of 0.5 is noise (held out: 27/57 won)
    if abs(q - p) >= 0.08:
        flags.append("LARGE_RECALIBRATION")
    if cls == "hcp_plus_nb" and p > 0.5:
        flags.append("CUSHION_NB")
    return {"contract": contract, "group": g, "class": cls, "p": p, "q": q, "tier": t, "flags": flags}


def rank_rows(coef: dict, sport: str, rows: list[tuple[str, float]]) -> list[dict]:
    """Score every row and order by q (ties keep the stated order)."""
    scored = [dict(score_row(coef, sport, c, p), stated_rank=i + 1) for i, (c, p) in enumerate(rows)]

    def key(r):
        # A NEAR_TIED_FLIP keeps its stated side: it sorts just above 0.5 if stated above 0.5, just below if not.
        q = r["q"]
        if "NEAR_TIED_FLIP" in r["flags"]:
            q = 0.5 + (0.001 if r["p"] > 0.5 else -0.001)
        return (-round(q, 6), r["stated_rank"])

    scored.sort(key=key)
    for i, r in enumerate(scored):
        r["rm1_rank"] = i + 1
    return scored


def top_two_statement(ranked: list[dict]) -> str:
    """The card-level TOP2_QUALITY line (RULES_GENERAL.md §"2026-09-25(e)")."""
    if len(ranked) < 2:
        return "TOP2_QUALITY: n/a (fewer than two rows)"
    q1, q2 = ranked[0]["q"], ranked[1]["q"]
    if q1 >= 0.70 and q2 >= 0.70:
        label = "TOP2_STRONG"
    elif q1 >= 0.62 and q2 >= 0.62:
        label = "TOP2_SUPPORTED"
    elif q1 >= 0.62:
        label = "TOP1_ONLY"
    else:
        label = "TOP2_COIN_FLIP"
    return (f"TOP2_QUALITY: {label} (R1 q {q1:.3f} {ranked[0]['tier']}; R2 q {q2:.3f} {ranked[1]['tier']}; "
            f"if independent: P(both win) {q1 * q2:.3f}, P(both lose) {(1 - q1) * (1 - q2):.3f})")


# ------------------------------------------------------------------ CLI


def _parse_row(s: str) -> tuple[str, float]:
    contract, sep, p = s.rpartition("=")
    if not sep:
        raise argparse.ArgumentTypeError(f"row must be 'contract=p', got {s!r}")
    return contract.strip(), float(p)


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--coef", type=Path, default=DEFAULT_COEF)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("score")
    s.add_argument("--sport", required=True)
    s.add_argument("--contract", required=True)
    s.add_argument("--p", type=float, required=True)
    r = sub.add_parser("rank")
    r.add_argument("--sport", required=True)
    r.add_argument("--row", action="append", type=_parse_row, required=True, help='"contract=p", in stated rank order')
    f = sub.add_parser("fit")
    f.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    f.add_argument("--lam", type=float, default=0.0, help="ridge weight on challenger terms (RM-1 has none)")
    f.add_argument("--terms", default=",".join(DEFAULT_TERMS), help=f"comma list from {', '.join(TERMS)}")
    f.add_argument("--fitted", default=None, help="date stamp written into the file, e.g. 2026-09-25")
    f.add_argument("--out", type=Path, default=None, help="write the coefficients here (default: print only)")
    sub.add_parser("show")
    args = ap.parse_args(argv)

    if args.cmd == "fit":
        terms = tuple(t.strip() for t in args.terms.split(",") if t.strip())
        bad = [t for t in terms if t not in TERMS]
        if bad:
            ap.error(f"unknown terms {bad}")
        c = fit(load_decision_rows(args.csv), args.lam, terms)
        c["model"] = "RM-1" if tuple(c["terms"]) == DEFAULT_TERMS else "RM-1X(" + "+".join(c["terms"]) + ")"
        c["fitted"] = args.fitted or "unstated"
        try:
            c["source_csv"] = args.csv.resolve().relative_to(REPO).as_posix()
        except ValueError:
            c["source_csv"] = str(args.csv)
        text = json.dumps(c, indent=2, sort_keys=True)
        if args.out:
            args.out.write_text(text + "\n", encoding="utf-8")
            print(f"wrote {args.out} (n={c['n']}, cards={c['cards']}, terms={c['terms']}, lam={c['lam']})")
        else:
            print(text)
        return 0

    coef = load_coef(args.coef)
    if args.cmd == "show":
        print(f"{coef.get('model', 'RM-1')} fitted {coef.get('fitted', '?')} on n={coef['n']} decision rows / "
              f"{coef['cards']} cards; terms {coef.get('terms')}; lam {coef['lam']}")
        for k, v in coef["weights"].items():
            print(f"  {k:22s} {v:+.3f}")
        return 0
    if args.cmd == "score":
        out = score_row(coef, args.sport, args.contract, args.p)
        print(f"{out['contract']}: group {out['group']}, class {out['class']}, stated p {out['p']:.3f} → "
              f"RM-1 q {out['q']:.3f} ({out['tier']}){' ' + ' '.join(out['flags']) if out['flags'] else ''}")
        return 0
    ranked = rank_rows(coef, args.sport, args.row)
    print("| RM-1 rank | Stated rank | Contract | Class | Stated p | RM-1 q | Tier | Flags |")
    print("|---:|---:|---|---|---:|---:|---|---|")
    for x in ranked:
        print(f"| {x['rm1_rank']} | {x['stated_rank']} | {x['contract']} | {x['class']} | {x['p']:.3f} | "
              f"{x['q']:.3f} | {x['tier']} | {' '.join(x['flags']) or '—'} |")
    print()
    print(top_two_statement(ranked))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
