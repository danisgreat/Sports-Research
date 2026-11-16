"""Deep loss register (DEEPLOSS-v1 register, CR-2026.11.16-R2): one CSV row per deep loss review.

    python -m ml deep-loss check             validate research/deep_loss/DEEP_LOSS_REGISTER.csv
    python -m ml deep-loss tally [--out F]   reviews per registered failure class; three or more is a pattern for prompt 8

The reviews themselves stay prose in their settlement documents. The register carries what the pattern rule needs to be
run mechanically: the card, the trigger, the verdict and one registered failure class (RULES_REFERENCE Part B section 8),
with a printed alias where the review used its own name. Rows are appended, never edited.
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = "research/deep_loss/DEEP_LOSS_REGISTER.csv"
RULES = "RULES_REFERENCE.md"
FIELDS = ("review_id", "canonical_id", "contract", "trigger", "verdict", "registered_class", "alias", "class_basis", "source", "recorded_at")
VERDICTS = ("ERROR", "MODEL_LIMIT", "VARIANCE", "MIXED")
TRIGGERS = ("TOP_SIDE", "TOP_TOTAL", "RANK_1", "TOP_SIDE_AND_RANK_1", "TOP_TOTAL_AND_RANK_1", "NOT_RECORDED")
PATTERN = 3


class DeepLossError(ValueError):
    pass


def classes(root=ROOT) -> tuple:
    text = (Path(root) / RULES).read_text(encoding="utf-8")
    m = re.search(r"^## 8\. Failure classes\s*\n\s*\n(.+?)\n", text, re.M)
    if not m:
        raise DeepLossError("RULES_REFERENCE section 8 (Failure classes) not found")
    names = re.findall(r"[A-Z][A-Z0-9_]{2,}", m.group(1))
    return tuple(dict.fromkeys(names))


def read(root=ROOT) -> list[dict]:
    path = Path(root) / REGISTER
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise DeepLossError("register columns must be " + ",".join(FIELDS))
        return list(reader)


def problems(root=ROOT) -> list[str]:
    known, out, seen = classes(root), [], set()
    for n, r in enumerate(read(root), start=2):
        name = f"row {n} {r['review_id']}: "
        if not r["review_id"] or r["review_id"] in seen:
            out.append(name + "review_id must be present and unique")
        seen.add(r["review_id"])
        if not re.fullmatch(r"P-\d{3,}", r["canonical_id"]):
            out.append(name + "canonical_id is a P-ID")
        if r["verdict"] not in VERDICTS:
            out.append(name + "verdict is one of " + "/".join(VERDICTS))
        if r["trigger"] not in TRIGGERS:
            out.append(name + "trigger is one of " + "/".join(TRIGGERS))
        if r["registered_class"] not in known:
            out.append(name + "registered_class must be a class of RULES_REFERENCE section 8")
        if r["registered_class"] == "OTHER" and not r["alias"]:
            out.append(name + "OTHER needs an alias that names the failure")
        if not r["source"] or not (Path(root) / r["source"]).exists():
            out.append(name + "source is the settlement document that holds the review")
        if not r["recorded_at"]:
            out.append(name + "recorded_at is required")
    return out


def tally(root=ROOT) -> list[dict]:
    """Reviews per failure name (the alias when one is printed, else the registered class); VARIANCE is never a pattern."""
    groups = defaultdict(list)
    for r in read(root):
        groups[(r["alias"] or r["registered_class"], r["registered_class"])].append(r)
    rows = []
    for (name, cls), items in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        games = sorted({r["canonical_id"] for r in items})
        rows.append(dict(failure=name, registered_class=cls, reviews=len(items), games=len(games),
                         status="CLASS_NOT_RECORDED" if name.endswith("_NO_CLASS_RECORDED") else
                         "PATTERN_ROUTE_TO_PROMPT_8" if len(items) >= PATTERN and cls != "VARIANCE" else "BELOW_PATTERN",
                         canonical_ids=" ".join(games)))
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    t = sub.add_parser("tally")
    t.add_argument("--out", type=Path)
    args = parser.parse_args(argv)
    bad = problems()
    if bad:
        raise SystemExit("DEEPLOSS register: " + " | ".join(bad))
    if args.cmd == "check":
        print(f"{len(read())} reviews; register valid")
        return
    rows = tally()
    for r in rows:
        print(f"{r['reviews']:3d} reviews / {r['games']:2d} games  {r['status']:26} {r['failure']} ({r['registered_class']})  {r['canonical_ids']}")
    if args.out:
        if args.out.exists():
            raise SystemExit(f"{args.out} already exists")
        with open(args.out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(rows)


if __name__ == "__main__":
    main()
