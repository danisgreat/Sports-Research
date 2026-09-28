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

Rows with p ≥ 0.5 are not a safe proxy for the frozen preferred decision. Preferred-decision
reports require an explicit `preferred_at_issue` field. The default output is a legacy mixed-row
diagnostic only; it is not a decision-level or performance-eligible result.

LEARNING_ONLY. The report describes the framework's own record. Nothing in it may be fitted back
into a forecast as a shrink, weight or cap (L-087, SCORING_AND_VALIDATION.md §14).

Usage:
    python research/settled_rows_2026-09-25/extract_settled_rows.py
    python tools/calibration_report.py [research/settled_rows_2026-09-28/generated/settled_rows.csv]
        [--preferred-only] [--eligible-only] [--min-n 10]
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
sys.path.insert(0, str(Path(__file__).resolve().parent))
import prospective_eligibility as pe  # noqa: E402
DEFAULT = REPO / "research" / "settled_rows_2026-09-28" / "generated" / "settled_rows.csv"
BANDS = [(0.0, 0.4), (0.4, 0.5), (0.5, 0.55), (0.55, 0.6), (0.6, 0.65), (0.65, 0.7), (0.7, 0.8), (0.8, 1.0001)]


def _truth(value: object) -> bool:
    return str(value or "").strip().casefold() in ("true", "yes", "eligible", "verified", "1")


def load(path: Path, *, eligible_only: bool = False, records_path: Path = pe.DEFAULT_RECORDS) -> list[dict]:
    """Load descriptive CSV rows; eligible mode requires an exact structured-record join.

    CSV flags are useful for display but are not evidence. For the eligible view, recompute the
    record gate and RM-1 reproduction, then bind the CSV's decision/card/rank/contract/result and
    probabilities to that verified record. This intentionally excludes push/void vectors from
    the current binary report.
    """
    accepted_records: dict[str, dict] = {}
    if eligible_only:
        accepted_records, _ = pe.verified_records(records_path)
    out = []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            res = (r.get("result") or "").strip().upper()[:1]
            p = (r.get("p") or "").strip()
            if res not in ("W", "L") or not p:
                continue
            pf = float(p)
            if not 0.0 <= pf <= 1.0:
                continue
            preferred_text = (r.get("preferred_at_issue") or "").strip().casefold()
            preferred = True if preferred_text in ("true", "yes", "eligible", "1") else (
                False if preferred_text in ("false", "no", "0") else None)
            try:
                baseline_p = float(r["baseline_p"]) if r.get("baseline_p") not in (None, "") else None
            except ValueError:
                baseline_p = None
            baseline_match = (r.get("baseline_match_valid") or "").strip().casefold() in ("true", "yes", "1")
            decision = (r.get("decision_id") or "").strip()
            record = accepted_records.get(decision) if eligible_only else None
            if eligible_only:
                if record is None or not (_truth(r.get("performance_eligible")) and _truth(r.get("outcome_verified"))):
                    continue
                probs = record.get("probabilities", {})
                frozen_baseline = record.get("baseline", {})
                if (record.get("decision_id") != decision
                        or record.get("forecast_id") != r.get("forecast_id")
                        or record.get("event_id") != r.get("event_id")
                        or record.get("event_cluster_id") != r.get("event_cluster_id")
                        or record.get("target_id") != r.get("target_id")
                        or record.get("horizon") != r.get("horizon")
                        or record.get("input_cutoff_utc") != r.get("input_cutoff_utc")
                        or record.get("result") != res or record.get("card_id") != r.get("card")
                        or str(record.get("rank")) != str(r.get("rank", "")).strip()
                        or pe._contract_key(record.get("contract", "")) != pe._contract_key(r.get("contract", ""))
                        or record.get("preferred_at_issue") is not True
                        or probs.get("P", 0.0) > 1e-8 or probs.get("V", 0.0) > 1e-8
                        or abs(float(probs.get("W", -1)) - pf) > 1e-9
                        or not isinstance(frozen_baseline, dict)
                        or not isinstance(frozen_baseline.get("p"), (int, float))
                        or baseline_p is None or abs(frozen_baseline["p"] - baseline_p) > 1e-9):
                    continue
                if pe.rm1_blockers(record):
                    continue
                baseline_match = True
            eligible = _truth(r.get("performance_eligible"))
            outcome_verified = _truth(r.get("outcome_verified"))
            out.append({"card": r.get("card", ""), "p": pf, "y": 1 if res == "W" else 0,
                        "family": r.get("family", ""), "sport": r.get("sport", ""),
                        "direction": r.get("direction", ""), "rank": r.get("rank", ""),
                        "preferred_at_issue": preferred, "baseline_p": r.get("baseline_p", ""),
                        "baseline_match_valid": baseline_match,
                        "baseline_probability": baseline_p if baseline_p is not None and 0 <= baseline_p <= 1 else None,
                        "performance_eligible": eligible, "outcome_verified": outcome_verified,
                        "horizon": (record.get("horizon") if record else r.get("horizon", "UNKNOWN")),
                        "event_id": (record.get("event_id") if record else r.get("event_id", "")),
                        "event_cluster_id": (record.get("event_cluster_id") if record else r.get("event_cluster_id", "")),
                        "target_id": (record.get("target_id") if record else r.get("target_id", "")),
                        "contract_id": (record.get("contract_id") if record else r.get("contract_id", "")),
                        "input_cutoff_utc": (record.get("input_cutoff_utc") if record else r.get("input_cutoff_utc", "")),
                        "baseline_event_id": (record.get("baseline", {}).get("event_id") if record else r.get("baseline_event_id", "")),
                        "baseline_target_id": (record.get("baseline", {}).get("target_id") if record else r.get("baseline_target_id", "")),
                        "baseline_contract_id": (record.get("baseline", {}).get("contract_id") if record else r.get("baseline_contract_id", "")),
                        "baseline_horizon": (record.get("baseline", {}).get("horizon") if record else r.get("baseline_horizon", "")),
                        "baseline_input_cutoff_utc": (record.get("baseline", {}).get("input_cutoff_utc") if record else r.get("baseline_input_cutoff_utc", ""))})
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
    xs = [math.log(min(max(r["p"], 1e-9), 1 - 1e-9) / (1 - min(max(r["p"], 1e-9), 1 - 1e-9))) for r in rs]
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


def paired_baseline_summary(rows: list[dict], boot: int = 4000, seed: int = 20260925) -> dict:
    """Paired Brier difference only for explicitly certified, same-target baseline matches."""
    paired = [r for r in rows if r.get("baseline_match_valid") is True
              and r.get("baseline_probability") is not None
              and r.get("event_id") and r.get("target_id")
              and r.get("event_cluster_id") and r.get("contract_id") and r.get("horizon")
              and r.get("input_cutoff_utc")
              and r.get("baseline_event_id") == r.get("event_id")
              and r.get("baseline_target_id") == r.get("target_id")
              and r.get("baseline_contract_id") == r.get("contract_id")
              and r.get("baseline_horizon") == r.get("horizon")
              and r.get("baseline_input_cutoff_utc") == r.get("input_cutoff_utc")]
    by_event = defaultdict(list)
    for r in paired:
        y = r["y"]
        by_event[r["event_cluster_id"]].append((r["p"] - y) ** 2 - (r["baseline_probability"] - y) ** 2)
    if not paired:
        return {"n": 0, "excluded": len(rows)}
    event_means = [sum(vals) / len(vals) for vals in by_event.values()]
    macro = sum(event_means) / len(event_means)
    rng = random.Random(seed)
    boot_values = [sum(rng.choice(event_means) for _ in event_means) / len(event_means) for _ in range(boot)]
    boot_values.sort()
    return {"n": len(paired), "events": len(event_means), "event_weighted": macro,
            "ci95": (boot_values[int(0.025 * boot)], boot_values[int(0.975 * boot) - 1]),
            "excluded": len(rows) - len(paired)}


def slice_row(label: str, rs: list[dict], boot: int) -> str:
    n, k = len(rs), sum(r["y"] for r in rs)
    mp = sum(r["p"] for r in rs) / n
    lo, hi = cluster_gap_ci(rs, boot)
    flag = " **over-confident**" if hi < 0 else (" **under-confident**" if lo > 0 else "")
    return (f"| {label} | {n} | {len({r['card'] for r in rs})} | {k / n:.3f} | {mp:.3f} | {k / n - mp:+.3f} "
            f"[{lo:+.3f}, {hi:+.3f}]{flag} | {brier(rs):.4f} |")


def report(rows: list[dict], preferred_only: bool = False, min_n: int = 10, boot: int = 4000) -> str:
    if preferred_only and any(r.get("preferred_at_issue") is None for r in rows):
        raise ValueError("preferred-only report requires an explicit preferred_at_issue value on every row")
    scored = [r for r in rows if not preferred_only or r.get("preferred_at_issue") is True]
    scope = ("explicit frozen preferred decisions" if preferred_only else
             "LEGACY_MIXED_DIAGNOSTIC — all extracted binary W/L rows")
    by_card = defaultdict(list)
    for r in scored:
        by_card[r["card"]].append(r)
    equal_card_brier = (sum(brier(rs) for rs in by_card.values()) / len(by_card)) if by_card else float("nan")
    baseline = paired_baseline_summary(scored, boot)
    out = [f"### Calibration report — {scope}", "",
           f"Rows: {len(scored)} from {len(by_card)} card clusters (input binary W/L rows with p: {len(rows)}).", ""]
    m = murphy(scored) if scored else None
    if not scored:
        return "\n".join(out + ["No rows meet this report's explicit selection and eligibility requirements."])
    a, b, se = logistic_calibration(scored)
    out += ["**Binary row-weighted diagnostic (pushes excluded; complementary rows may remain):**",
            f"- Brier {m['brier']:.4f};",
            f"- Murphy decomposition: reliability {m['reliability']:.4f}, resolution {m['resolution']:.4f}, "
            f"uncertainty {m['uncertainty']:.4f};",
            f"- skill against climatology {m['skill_vs_climatology']:+.1%};",
            f"- logistic calibration slope {b:.2f} (SE {se:.2f}), intercept {a:+.2f};",
            f"- equal-card-weighted Brier proxy {equal_card_brier:.4f} ({len(by_card)} card clusters).",
            (f"- matched frozen baseline: n={baseline['n']} rows / {baseline['events']} event clusters; "
             f"event-weighted Brier difference {baseline['event_weighted']:+.4f} "
             f"[95% event-cluster bootstrap {baseline['ci95'][0]:+.4f}, {baseline['ci95'][1]:+.4f}]."
             if baseline["n"] else
             f"- matched frozen baseline: no paired result; {baseline['excluded']} row(s) lack an explicit valid match."),
            "- this legacy parser has no validated event/decision identity; this is not a performance claim.",
            ""]
    out += ["| Stated band | n | cards | win rate (Wilson 95%) | mean p |", "|---|---:|---:|---|---:|"]
    for lo, hi in BANDS:
        g = [r for r in scored if lo <= r["p"] < hi]
        if g:
            k = sum(r["y"] for r in g)
            wl, wh = wilson(k, len(g))
            out.append(f"| {lo:.2f}–{min(hi, 1):.2f} | {len(g)} | {len({r['card'] for r in g})} | "
                       f"{k / len(g):.3f} ({wl:.3f}–{wh:.3f}) | {sum(r['p'] for r in g) / len(g):.3f} |")
    for key in ("family", "sport", "direction", "rank"):
        groups = defaultdict(list)
        for r in scored:
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
    ap.add_argument("--preferred-only", action="store_true",
                    help="require and use the explicit frozen preferred_at_issue field")
    ap.add_argument("--eligible-only", action="store_true",
                    help="keep only exact joins to semantically verified structured records with RM-1 reproduction")
    ap.add_argument("--records", type=Path, default=pe.DEFAULT_RECORDS,
                    help="versioned structured records used to verify eligible rows")
    ap.add_argument("--min-n", type=int, default=10)
    ap.add_argument("--boot", type=int, default=4000)
    args = ap.parse_args(argv)
    rows = load(Path(args.csv), eligible_only=args.eligible_only, records_path=args.records)
    if not rows:
        print("no rows pass the verified eligibility gate" if args.eligible_only else "no graded rows with probabilities")
        return 0
    try:
        print(report(rows, args.preferred_only, args.min_n, args.boot))
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
