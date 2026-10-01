"""Conservative one-row-per-ID reconstruction of the historical register.

This deliberately does not parse grades from narrative. An absent value is blank.
The source register is historical and every row is ineligible for prospective skill.
"""

from __future__ import annotations

import csv
import re
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
REGISTER = REPO / "GAME_LOG_STATUS_CURRENT.md"
OUTPUT = REPO / "research" / "SETTLED_OUTCOMES_LEDGER.csv"
CORRECTIONS = REPO / "research" / "SETTLED_OUTCOMES_CORRECTIONS.csv"

RANK_FIELDS = [f"rk{rank}_{field}" for rank in range(1, 5)
               for field in ("contract", "family", "tier", "p", "q", "baseline_p", "result")]
FIELDS = [
    "card_id", "event", "sport", "event_date", "event_date_basis",
    "register_status", "record_status", "issue_timing", "performance_eligible",
    "n_ranked_rows_graded", "wins", "losses", "pushes", *RANK_FIELDS,
    "lower_ranks", "rank1_hit", "top2_hits", "top2_pair_type", "top2_both_failed",
    "best_winning_rank", "rank_pairs_concordant", "rank_pairs_discordant",
    "rank_order_verdict", "ranking_right", "mean_brier_p", "n_rows_with_p",
    "comment", "comment_basis", "data_flags", "source_lines",
]
CORRECTION_FIELDS = ["revision_id", "card_id", "field", "old_value", "new_value",
                     "reason", "source_url", "retrieved_utc", "response_sha256"]
FLAGS = {
    26: "ROWS_MAY_BE_MISATTRIBUTED", 35: "RANKS_UNRELIABLE",
    112: "SUMMARY_CONFLICT", 136: "RANKS_UNRECOVERABLE",
    216: "RANKS_UNRECOVERABLE", 366: "ROWS_GARBLED",
    492: "RANKS_UNRECOVERABLE", 496: "GRADES_CORRECTED",
    126: "OPEN", 418: "OPEN",
}
RESERVED = {
    518: ("New York Mets @ Washington Nationals", "MLB", "LIVE_ISSUED"),
    519: ("Gold Coast SUNS v St Kilda", "AFLW", "LIVE_ISSUED"),
    520: ("Hanwha Eagles @ Lotte Giants", "KBO", "PREGAME_LABEL_ONLY"),
    521: ("Rio Breogan v Joventut", "ACB", "LIVE_ISSUED"),
    522: ("Tenerife v Zaragoza", "ACB", "LIVE_ISSUED"),
}


def extract() -> list[dict[str, str]]:
    rows: dict[int, dict[str, str]] = {}
    for line_no, line in enumerate(REGISTER.read_text(encoding="utf-8").splitlines(), 1):
        match = re.match(r"^\| P-(\d{3}) \|", line)
        if not match:
            continue
        n = int(match.group(1))
        if n in rows:
            raise ValueError(f"duplicate P-{n:03} in register")
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        event = cells[1] if len(cells) > 1 else ""
        status = cells[2] if len(cells) > 2 else ""
        summary = cells[3] if len(cells) > 3 else ""
        row = dict.fromkeys(FIELDS, "")
        row.update(card_id=f"P-{n:03}", event=event, register_status=status,
                   record_status=("RESERVED_UNUSED" if "RESERVED / UNUSED" in event else "REGISTER_SUMMARY_ONLY"), issue_timing="UNKNOWN",
                   performance_eligible="false", comment=summary,
                   comment_basis="LOG_STATUS", data_flags=FLAGS.get(n, ""),
                   source_lines=f"GAME_LOG_STATUS_CURRENT.md:{line_no}",
                   event_date_basis="NOT_EXTRACTED")
        rows[n] = row
    missing = set(range(1, 518)) - set(rows)
    if missing:
        raise ValueError(f"missing historical IDs: {sorted(missing)}")
    if len(rows) != 517:
        raise ValueError(f"unexpected register size {len(rows)}")
    for n, (event, sport, timing) in RESERVED.items():
        row = dict.fromkeys(FIELDS, "")
        row.update(card_id=f"P-{n:03}", event=event, sport=sport,
                   event_date_basis="NOT_EXTRACTED", register_status="RESERVED",
                   record_status="RESERVED_UNDER_RECONCILIATION", issue_timing=timing,
                   performance_eligible="false", data_flags="OPEN_RECONCILIATION",
                   source_lines="P518_P522_RECONCILIATION.md:7-14",
                   comment="Official result partly checked; issue and settlement not certified.",
                   comment_basis="RECONCILIATION")
        rows[n] = row
    return [rows[n] for n in range(1, 523)]


def write_initial(path: Path = OUTPUT) -> None:
    rows = extract()
    if path.exists():
        with path.open(newline="", encoding="utf-8") as f:
            old = list(csv.DictReader(f))
        if old != rows:
            raise RuntimeError("ledger is immutable; use append-only corrections")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    if not CORRECTIONS.exists():
        with CORRECTIONS.open("w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(CORRECTION_FIELDS)


def append_correction(correction: dict[str, str]) -> None:
    if set(correction) != set(CORRECTION_FIELDS):
        raise ValueError("correction fields do not match schema")
    if correction["field"] not in FIELDS or correction["field"] in {"card_id", "performance_eligible"}:
        raise ValueError("identity and historical eligibility cannot be corrected here")
    if not re.fullmatch(r"P-\d{3}", correction["card_id"]) or not 1 <= int(correction["card_id"][2:]) <= 522:
        raise ValueError("invalid historical ID")
    if not correction["revision_id"] or not correction["reason"] or not correction["source_url"].startswith("https://"):
        raise ValueError("revision needs reason and source")
    if not re.fullmatch(r"[0-9a-f]{64}", correction["response_sha256"]):
        raise ValueError("revision needs a response hash")
    timestamp=datetime.fromisoformat(correction["retrieved_utc"].replace("Z","+00:00"))
    if timestamp.tzinfo is None:
        raise ValueError("revision time needs UTC offset")
    with OUTPUT.open(newline="",encoding="utf-8") as f:
        base={row["card_id"]:row for row in csv.DictReader(f)}
    with CORRECTIONS.open(newline="",encoding="utf-8") as f:
        revisions=list(csv.DictReader(f))
    if correction["revision_id"] in {r["revision_id"] for r in revisions}:
        raise ValueError("duplicate correction revision")
    current=base[correction["card_id"]][correction["field"]]
    for r in revisions:
        if r["card_id"]==correction["card_id"] and r["field"]==correction["field"]:
            current=r["new_value"]
    if correction["old_value"]!=current:
        raise ValueError("correction does not quote the current effective value")
    with CORRECTIONS.open("a",newline="",encoding="utf-8") as f:
        csv.DictWriter(f,fieldnames=CORRECTION_FIELDS).writerow(correction)


if __name__ == "__main__":
    write_initial()
