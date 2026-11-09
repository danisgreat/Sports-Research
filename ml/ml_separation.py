"""Fitted models stay separate from the cards until one is promoted (ML-SEP-v1, owner instruction 2026-11-09).

The owner's instruction: while the machine-learning models have not shown that they improve the predictions, keep
their predictions separate from the rest of the framework. So, for every competition without a row in
``research/model_registry/ML_PROMOTIONS.csv``:

- a fitted release is never a card's declared reference (``reference.tier`` falls back to TB-2-MD, TB-1-MD or the
  league-only baseline);
- ``pregame reference`` (the model frozen *before* the card) refuses to run;
- a card's PICKS_V2 block carries ``model_p NONE``, and its Model shadow block prints status and receipt only;
- the model still runs as a shadow after the card (``pregame run``) and in the league-day lane, into its own ledger,
  where it is scored against the card and the reference on identical rows.

A promotion row is written only by prompt 8, after a lane reached its decision floor (50 settled paired games and
8 settled weeks) with a paired interval below zero against the current reference, and with the owner's decision.
"""
from __future__ import annotations

import csv
from pathlib import Path

RULE = "ML-SEP-v1"
PROMOTIONS = "research/model_registry/ML_PROMOTIONS.csv"
FIELDS = ("competition", "release", "promoted_at", "lane_evidence", "paired_interval", "owner_decision")


def promotions(root) -> list[dict]:
    path = Path(root) / PROMOTIONS
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        missing = [f for f in FIELDS if not (r.get(f) or "").strip()]
        if missing:
            raise ValueError(f"{PROMOTIONS}: promotion row for {r.get('competition')!r} lacks {', '.join(missing)}")
    return rows


def promoted(competition: str, root) -> bool:
    """True only when the owner has promoted a fitted model for this competition (an evidenced row)."""
    return any(r["competition"] == competition for r in promotions(root))


def is_model_reference(reference_id: str) -> bool:
    """A declared reference or reference_id that names a fitted model release."""
    ref = (reference_id or "").strip().upper()
    return ref.startswith("RELEASE") or "-CYCLE-" in ref
