"""Settlement-time benchmark probabilities (BENCH-v1), kept behind the market firewall.

A benchmark is a probability for a card row that the research never saw: the no-vig closing probability of the exact
contract (NOVIG_CLOSE), or an external non-market model (SQUIGGLE, CLUBELO, TENNIS_ABSTRACT_ELO). It is entered by hand
AFTER the event is final, as a probability only. The loader rejects any column that could carry a price or a line
movement, any NOVIG_CLOSE row captured before the verified final, and any row for a card that is not in the ledger.
The line-implied benchmark (0.5 at a supplied two-way line) needs no file: the ledger writes it into every row.

    benchmarks file columns:  local_key,label,benchmark_id,p,method,source_url,retrieved_at,final_at
"""
from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd

FIELDS = ("local_key", "label", "benchmark_id", "p", "method", "source_url", "retrieved_at", "final_at")
IDS = ("NOVIG_CLOSE", "SQUIGGLE", "CLUBELO", "TENNIS_ABSTRACT_ELO", "EXTERNAL_OTHER")
NOVIG_METHODS = ("MULTIPLICATIVE", "POWER", "SHIN", "OO_EPC")


class BenchmarkError(ValueError):
    pass


def load(path) -> pd.DataFrame:
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        header = tuple(reader.fieldnames or ())
        rows = list(reader)
    if header != FIELDS:
        extra = sorted(set(header) - set(FIELDS))
        raise BenchmarkError("benchmark columns must be exactly " + ",".join(FIELDS)
                             + (f"; refused column(s) {', '.join(extra)} (no price, odds or line-movement field may enter the repository)" if extra else ""))
    out = []
    for r in rows:
        if r["benchmark_id"] not in IDS:
            raise BenchmarkError(f"{r['local_key']} {r['label']}: benchmark_id must be one of {', '.join(IDS)}")
        try:
            p = float(r["p"])
        except ValueError:
            raise BenchmarkError(f"{r['label']}: p must be a probability") from None
        if not 0 < p < 1:
            raise BenchmarkError(f"{r['label']}: p must lie strictly between 0 and 1")
        if not r["source_url"].startswith("https://"):
            raise BenchmarkError(f"{r['label']}: an HTTPS source is required")
        retrieved, final = pd.Timestamp(r["retrieved_at"]), pd.Timestamp(r["final_at"])
        if pd.isna(retrieved) or pd.isna(final) or retrieved.tzinfo is None or final.tzinfo is None:
            raise BenchmarkError(f"{r['label']}: retrieved_at and final_at need a UTC offset")
        if retrieved < final:
            raise BenchmarkError(f"{r['label']}: a benchmark is entered after the verified final, never before")
        if r["benchmark_id"] == "NOVIG_CLOSE" and r["method"] not in NOVIG_METHODS:
            raise BenchmarkError(f"{r['label']}: NOVIG_CLOSE needs a named de-vig method ({', '.join(NOVIG_METHODS)})")
        out.append(dict(r, p=p))
    frame = pd.DataFrame(out, columns=FIELDS)
    if frame.duplicated(["local_key", "label", "benchmark_id"]).any():
        raise BenchmarkError("duplicate benchmark rows")
    return frame
