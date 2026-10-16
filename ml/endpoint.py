"""Explicit score coordinates; an unobserved regulation score is never a final score."""
from __future__ import annotations

import math

EXTRA_DECISIONS = {"Overtime", "Shootout", "EXTRAS"}
MISSING = {"", "NOT_OBSERVED", "UNKNOWN"}


def regulation_pair(row):
    values = [str(row.get(k, "")).strip() for k in ("reg_hs", "reg_as")]
    if any(v in MISSING for v in values):
        if not all(v in MISSING for v in values):
            raise ValueError("both regulation coordinates must be observed or missing")
        return None
    pair = tuple(float(v) for v in values)
    final = tuple(float(row[k]) for k in ("hs", "as_"))
    if any(not math.isfinite(v) or v < 0 or v != int(v) for v in pair):
        raise ValueError("regulation scores must be nonnegative integers")
    if any(r > f for r, f in zip(pair, final)):
        raise ValueError("regulation score exceeds final score")
    if row.get("decision") in EXTRA_DECISIONS and (pair[0] != pair[1] or pair == final):
        raise ValueError("extra-time regulation must be an observed tie before final scoring")
    return tuple(int(v) for v in pair)
