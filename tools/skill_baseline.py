#!/usr/bin/env python3
"""Card-versus-baseline skill comparison (C-BASELINE-SKILL, added 2026-09-25(c)).

Reads the decision table in SKILL_BASELINE_LEDGER.md. Each row is one issued decision (a forced
pair counted once) with the card's issued probability, a leak-free population baseline
probability for the same contract, and the result (W/L; pushes remain excluded from this binary
ledger). The principal estimate first averages decisions within an event, then weights events
equally. It also reports a decision-weighted diagnostic and a paired 95% interval from an event-
cluster bootstrap.

This is a descriptive LEARNING_ONLY diagnostic, not a performance claim
(PERFORMANCE_ELIGIBILITY_POLICY.md). The preregistered decision rule is in LEARNING_REGISTER.md
§"2026-09-25(c)" (C-BASELINE-SKILL).

Usage: python tools/skill_baseline.py [SKILL_BASELINE_LEDGER.md] [--boot 10000] [--seed 20260925] [--section all|prospective|seed]

Sections (added 2026-09-26). Rows are tagged by the ledger heading they sit under. Only rows under the
"Prospective rows" heading that exactly join to a semantically verified record in
research/settled_rows_2026-09-28/prospective_records.json count toward the preregistered decision rule
(100 decisions from at least 30 cards); the hindsight "Seed rows" never do. A Markdown eligibility
label alone is not evidence. The default report prints the verified prospective section separately
from hindsight seed diagnostics.
"""
from __future__ import annotations

import argparse
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

import prospective_eligibility as pe

REPO = Path(__file__).resolve().parent.parent
HEADER = re.compile(r"^\|\s*Decision\s*\|", re.I)


CHECKPOINT_DECISIONS, CHECKPOINT_CARDS = 100, 30


def section_of(heading: str) -> str:
    h = heading.lower()
    return "prospective" if "prospective" in h else "seed" if "seed" in h else "other"


def parse(text: str) -> list[dict]:
    rows, cols, section = [], None, "other"
    for line in text.splitlines():
        if line.startswith("## "):
            section = section_of(line)
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
            eligible_text = (r.get("performance eligible") or r.get("eligible") or "").strip().casefold()
            rank_text = r.get("rank", "").strip()
            rows.append({"decision": r["decision"], "card": r["card"], "family": r["family"],
                         "p": float(r["card p"]), "b": float(r["baseline p"]), "result": r["result"].upper(),
                         "rank": int(rank_text) if rank_text.isdigit() else rank_text,
                         "contract": r.get("contract (as issued)", ""),
                         "eligibility_receipt": r.get("eligibility receipt", ""),
                         "event_cluster_id": r.get("event cluster id", ""),
                         "section": section, "eligible": eligible_text in ("eligible", "yes", "true", "1"),
                         "eligibility_status": eligible_text or "UNDECLARED"})
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
    event_key = lambda r: r.get("event_cluster_id") or f"CARD:{r['card']}"
    out = {"n": len(scored), "cards": len({r["card"] for r in scored}),
           "events": len({event_key(r) for r in scored}), "by_family": {}}
    if not scored:
        return out

    def block(rs):
        by_event = defaultdict(list)
        for r in rs:
            by_event[event_key(r)].append(r)
        event_values = [(sum(r["bc"] for r in group) / len(group),
                         sum(r["bb"] for r in group) / len(group)) for group in by_event.values()]
        event_card = sum(x[0] for x in event_values) / len(event_values)
        event_base = sum(x[1] for x in event_values) / len(event_values)
        decision_card = sum(r["bc"] for r in rs) / len(rs)
        decision_base = sum(r["bb"] for r in rs) / len(rs)
        return {"n": len(rs), "events": len(event_values), "card_brier": event_card,
                "baseline_brier": event_base, "diff": event_card - event_base,
                "decision_card_brier": decision_card, "decision_baseline_brier": decision_base,
                "decision_diff": decision_card - decision_base,
                "card_better_rows": sum(1 for r in rs if r["bc"] < r["bb"])}

    out.update(block(scored))
    fam = defaultdict(list)
    for r in scored:
        fam[r["family"]].append(r)
    out["by_family"] = {k: block(v) for k, v in sorted(fam.items())}
    by_event = defaultdict(list)
    for r in scored:
        by_event[event_key(r)].append(r)
    events = list(by_event)
    event_diff = {e: sum(r["bc"] - r["bb"] for r in group) / len(group)
                  for e, group in by_event.items()}
    rng = random.Random(seed)
    diffs = []
    for _ in range(boot):
        sample = [event_diff[rng.choice(events)] for _ in events]
        diffs.append(sum(sample) / len(sample))
    diffs.sort()
    out["ci95"] = (diffs[int(0.025 * boot)], diffs[int(0.975 * boot) - 1])
    return out


def render(s: dict) -> str:
    if not s["n"]:
        return "No scored decisions with a baseline yet."
    lines = [f"Scored decisions: {s['n']} across {s['cards']} cards and {s.get('events', s['cards'])} event clusters "
             "(forced pairs counted once; pushes excluded).",
             "",
             "| Scope | n | Forecast Brier (event-weighted) | Baseline Brier (event-weighted) | Forecast − baseline | Decisions where forecast Brier is lower |",
             "|---|---:|---:|---:|---:|---:|",
             f"| **All** | {s['n']} | {s['card_brier']:.4f} | {s['baseline_brier']:.4f} | **{s['diff']:+.4f}** | {s['card_better_rows']}/{s['n']} |"]
    for k, v in s["by_family"].items():
        lines.append(f"| {k} | {v['n']} | {v['card_brier']:.4f} | {v['baseline_brier']:.4f} | {v['diff']:+.4f} | "
                     f"{v['card_better_rows']}/{v['n']} |")
    lo, hi = s["ci95"]
    verdict = ("card better than baseline (interval below 0)" if hi < 0 else
               "card worse than baseline (interval above 0)" if lo > 0 else
               "no demonstrated difference (interval spans 0)")
    lines += ["", f"Event-cluster bootstrap 95% interval for (card − baseline): [{lo:+.4f}, {hi:+.4f}] — **{verdict}**.",
              f"Event-weighted Brier is primary; decision-weighted diagnostic: card {s.get('decision_card_brier', s['card_brier']):.4f}, "
              f"baseline {s.get('decision_baseline_brier', s['baseline_brier']):.4f}, "
              f"difference {s.get('decision_diff', s['diff']):+.4f}.",
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
    ap.add_argument("--section", choices=("all", "prospective", "seed"), default="all")
    ap.add_argument("--records", type=Path, default=pe.DEFAULT_RECORDS,
                    help="versioned structured records used to verify prospective ledger joins")
    args = ap.parse_args(argv)
    rows = parse(Path(args.ledger).read_text(encoding="utf-8-sig"))
    eligible, failures = pe.join_binary_baseline_rows(rows, args.records)
    eligible_ids = {r["decision"] for r in eligible}
    if args.section != "all":
        selected = [r for r in rows if r["section"] == args.section]
        if args.section == "prospective":
            selected = [r for r in selected if r["decision"] in eligible_ids]
        print(render(summarise(selected, args.boot, args.seed)))
        return 0
    print(report_sections(rows, args.boot, args.seed, eligible_ids, failures))
    return 0


def report_sections(rows: list[dict], boot: int = 10000, seed: int = 20260925,
                    eligible_ids: set[str] | None = None, failures: dict[str, list[str]] | None = None) -> str:
    prospective = [r for r in rows if r["section"] == "prospective"]
    eligible_ids = eligible_ids or set()
    eligible = [r for r in prospective if r["decision"] in eligible_ids]
    pro = summarise(eligible, boot, seed)
    excluded = len(prospective) - len(eligible)
    sd = summarise([r for r in rows if r["section"] == "seed"], boot, seed)
    n, c = pro["n"], pro["cards"]
    done = n >= CHECKPOINT_DECISIONS and c >= CHECKPOINT_CARDS
    failure_summary = ""
    if failures:
        reasons = defaultdict(int)
        for values in failures.values():
            for value in values:
                reasons[value] += 1
        if reasons:
            failure_summary = "\n\nJoin exclusions by reason: " + ", ".join(
                f"{key}={value}" for key, value in sorted(reasons.items())) + "."
    out = ["## Prospective rows (explicitly eligible rows only count toward C-BASELINE-SKILL)",
           f"Progress: {n}/{CHECKPOINT_DECISIONS} decisions from {c}/{CHECKPOINT_CARDS} cards — "
           + (("**checkpoint reached: apply the decision rule**." if done else "checkpoint not reached; no verdict.")
              + f" {excluded} unqualified row(s) excluded."),
           "", render(pro),
           "Eligibility requires an exact decision/card/contract/result/probability/baseline join to a valid structured record, passing source, time, identity and terminal checks."
           + failure_summary,
           "", "## Seed rows (hindsight; never counted)", "", render(sd)]
    return "\n".join(out)


if __name__ == "__main__":
    raise SystemExit(main())
