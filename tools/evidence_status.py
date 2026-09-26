#!/usr/bin/env python3
"""Evidence status — where every preregistered prospective gate stands (added 2026-09-26).

Why. The 2026-09-26 review found the method changing far faster than evidence arrives: six control
revisions on 2026-09-25 alone and no card issued under the current rules. C-RULE-FREEZE therefore
holds predictive rule changes until the two headline gates reach their checkpoints. This tool prints
those gates, and the new measurement lanes, in one table, so every session starts from the same
answer to "has anything been shown yet?".

Gates reported:
  C-BASELINE-SKILL     prospective rows in SKILL_BASELINE_LEDGER.md (100 decisions / 30 cards)
  T-RM1-PROSPECTIVE    settled cards issued under RM-1 (first RM-1 card P-518; checkpoint 25 cards),
                       read from research/settled_rows_2026-09-25/settled_rows.csv (rebuild it first)
  C-MARKET-BENCHMARK   valid rows in MARKET_BENCHMARK_LEDGER.md (100 decisions / 30 cards)
  C-EVENT-UNIVERSE     declared universes in universe/ and their coverage against the logs
  C-MLB-SHADOW         games frozen in research/mlb_shadow/shadow_log.csv and settled in shadow_results.csv
                       (150-game review point)
  C-RULE-FREEZE        IN FORCE until C-BASELINE-SKILL and T-RM1-PROSPECTIVE both reach checkpoint

Usage: python tools/evidence_status.py [--repo PATH] [--log FILE ...]
Standard library only; no network. LEARNING_ONLY: counts and progress, never a performance claim.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import market_benchmark as mb  # noqa: E402
import skill_baseline as sb  # noqa: E402
import slate_universe as su  # noqa: E402

FIRST_RM1_CARD = 518
RM1_CHECKPOINT_CARDS = 25
SHADOW_REVIEW_GAMES = 150
ACTIVE_LOG_GLOB = "Mini logs (to be sent to actual log later)/*/*.md"


def baseline_gate(repo: Path) -> dict:
    p = repo / "SKILL_BASELINE_LEDGER.md"
    rows = sb.parse(p.read_text(encoding="utf-8-sig")) if p.exists() else []
    s = sb.summarise([r for r in rows if r["section"] == "prospective"], boot=2000)
    done = s["n"] >= sb.CHECKPOINT_DECISIONS and s["cards"] >= sb.CHECKPOINT_CARDS
    verdict = ""
    if done:
        lo, hi = s["ci95"]
        verdict = "beats the naive baseline" if hi < 0 else "adds noise: open a method review" if lo > 0 else \
            "no demonstrated skill over the baseline"
    return {"gate": "C-BASELINE-SKILL", "checkpoint": f"{sb.CHECKPOINT_DECISIONS} decisions / {sb.CHECKPOINT_CARDS} cards",
            "progress": f"{s['n']} decisions / {s['cards']} cards", "done": done,
            "status": ("CHECKPOINT REACHED — " + verdict) if done else "ACCRUING"}


def rm1_gate(repo: Path) -> dict:
    p = repo / "research" / "settled_rows_2026-09-25" / "settled_rows.csv"
    cards = set()
    if p.exists():
        with p.open(encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                m = re.fullmatch(r"P-(\d+)", r.get("card", ""))
                if m and int(m.group(1)) >= FIRST_RM1_CARD and r.get("p"):
                    cards.add(int(m.group(1)))
    done = len(cards) >= RM1_CHECKPOINT_CARDS
    return {"gate": "T-RM1-PROSPECTIVE", "checkpoint": f"{RM1_CHECKPOINT_CARDS} settled cards from P-{FIRST_RM1_CARD}",
            "progress": f"{len(cards)} cards (dataset as last rebuilt)", "done": done,
            "status": "CHECKPOINT REACHED — score p against q" if done else "ACCRUING"}


def market_gate(repo: Path) -> dict:
    p = repo / "MARKET_BENCHMARK_LEDGER.md"
    ok, bad = mb.validate(mb.parse(p.read_text(encoding="utf-8-sig"))) if p.exists() else ([], [])
    s = mb.summarise(ok, boot=2000)
    done = s["n"] >= 100 and s["cards"] >= 30
    status = "CHECKPOINT REACHED — apply the ledger's decision rule" if done else "ACCRUING"
    if bad:
        status += f"; {len(bad)} row(s) excluded by the firewall"
    return {"gate": "C-MARKET-BENCHMARK", "checkpoint": "100 decisions / 30 cards",
            "progress": f"{s['n']} decisions / {s['cards']} cards", "done": done, "status": status}


def universe_gate(repo: Path, logs: list[Path]) -> dict:
    files = sorted((repo / "universe").glob("UNIVERSE_*.json"))
    texts = [p.read_text(encoding="utf-8-sig") for p in logs if p.exists()]
    n = carded = skipped = 0
    broken = []
    for f in files:
        try:
            u = su.load_universe(f)
        except SystemExit:
            broken.append(f.name)
            continue
        for r in su.coverage(u, texts):
            n += 1
            carded += r["status"] == "CARDED"
            skipped += r["status"].startswith("SKIPPED")
    missing = n - carded - skipped
    status = "NO UNIVERSE DECLARED YET" if not files else (
        f"coverage {carded / n:.0%} ({missing} missing)" if n else "declared, no events")
    if broken:
        status += f"; EDITED AFTER DECLARATION: {', '.join(broken)}"
    return {"gate": "C-EVENT-UNIVERSE", "checkpoint": "every declared event carded or skipped with a reason",
            "progress": f"{len(files)} universe(s), {n} events: {carded} carded, {skipped} skipped",
            "done": bool(files) and missing == 0 and not broken, "status": status}


def _csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def shadow_gate(repo: Path) -> dict:
    d = repo / "research" / "mlb_shadow"
    frozen = {r.get("game_pk") for r in _csv(d / "shadow_log.csv")}
    results = {r.get("game_pk") for r in _csv(d / "shadow_results.csv")}
    games, settled = len(frozen), len(frozen & results)
    return {"gate": "C-MLB-SHADOW", "checkpoint": f"{SHADOW_REVIEW_GAMES} settled games (review point, not proof)",
            "progress": f"{games} games frozen, {settled} settled", "done": settled >= SHADOW_REVIEW_GAMES,
            "status": "REVIEW DUE" if settled >= SHADOW_REVIEW_GAMES else "ACCRUING (never a card input)"}


def freeze_gate(base: dict, rm1: dict) -> dict:
    lifted = base["done"] and rm1["done"]
    return {"gate": "C-RULE-FREEZE", "checkpoint": "C-BASELINE-SKILL and T-RM1-PROSPECTIVE at checkpoint",
            "progress": f"baseline {'done' if base['done'] else 'open'}; RM-1 {'done' if rm1['done'] else 'open'}",
            "done": lifted,
            "status": "LIFTED at the next scheduled review" if lifted else
            "IN FORCE — integrity, retrieval and measurement fixes only; no new predictive rule, weight or cap"}


def collect(repo: Path, logs: list[Path] | None = None) -> list[dict]:
    if logs is None:
        logs = sorted(repo.glob(ACTIVE_LOG_GLOB)) + [repo / "PREDICTION_LOG_COMBINED_5.md"]
    base, rm1 = baseline_gate(repo), rm1_gate(repo)
    return [base, rm1, market_gate(repo), universe_gate(repo, logs), shadow_gate(repo), freeze_gate(base, rm1)]


def render(rows: list[dict]) -> str:
    out = ["| Gate | Checkpoint | Progress | Status |", "|---|---|---|---|"]
    out += [f"| `{r['gate']}` | {r['checkpoint']} | {r['progress']} | {r['status']} |" for r in rows]
    out += ["", "LEARNING_ONLY: progress counts, not performance claims. Sources: SKILL_BASELINE_LEDGER.md, "
            "MARKET_BENCHMARK_LEDGER.md, universe/, research/mlb_shadow/, research/settled_rows_2026-09-25/."]
    return "\n".join(out)


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=str(HERE.parent))
    ap.add_argument("--log", action="append", help="log file(s) to scan for universe coverage (default: active mini logs + Part 5)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    repo = Path(args.repo)
    rows = collect(repo, [Path(p) for p in args.log] if args.log else None)
    print(json.dumps(rows, indent=2) if args.json else render(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
