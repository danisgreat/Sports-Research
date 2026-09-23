#!/usr/bin/env python3
"""audit_card_controls.py — mechanical execution audit for the RULES_GENERAL.md §16.8
card completeness block.

Why this exists
---------------
`RULES_GENERAL.md` §16.8 and `EXTERNAL_LOGGING_WORKFLOW.md` both instruct the settlement
pass to run this script over a running log and record, per card, which completeness fields
were actually printed. A control that exists only as a list item behaves exactly like a
kill path that exists only as prose — that is the `M15` "listed but not executed" pattern,
and the `P-438`–`P-451` import produced four fresh instances of it (§16.11(o) disruption
facts, `G-L8` phase distribution, `G-L14` settlement-route lookup, `G-L17` joint failure
mass). This script is the remedy §16.8 names.

It is a *detector of printed fields*, not a judge of analysis quality. A field is "present"
when the card contains recognisable evidence that the field was printed. It cannot tell a
good width from a bad one; it can tell a printed width from a missing one, which is the
failure mode that actually recurs.

Usage
-----
    python audit_card_controls.py <file.md> [<file.md> ...]
    python audit_card_controls.py <file.md> --section "2026-09-17(b)"
    python audit_card_controls.py <file.md> --json
    python audit_card_controls.py <file.md> --settlement

Options
-------
    --section TEXT   Only audit cards inside the dated section whose heading contains TEXT.
    --settlement     Also check field 10 (process record), which only applies at settlement.
    --json           Emit machine-readable JSON instead of the Markdown table.
    --quiet          Suppress the per-card table; print only the summary.

Exit codes
----------
    0  every audited card printed every BLOCKING field
    1  at least one card is missing a BLOCKING field
    2  usage or file error

BLOCKING fields (a missing one blocks issue under §16.8): 2, 3, 5a, 7.
Everything else is recorded as a process defect on that card without blocking.

Detection is deliberately generous: it accepts any of several spellings, because the
purpose is to catch a field that was never printed at all, not to enforce one phrasing.
Generous detection means a PASS is weak evidence and a FAIL is strong evidence — which is
the correct asymmetry for an execution audit.
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
from dataclasses import dataclass, field as dc_field

# --------------------------------------------------------------------------------------
# Field definitions — RULES_GENERAL.md §16.8, as amended 2026-09-17(b)
# --------------------------------------------------------------------------------------


@dataclass
class Field:
    key: str
    label: str
    blocking: bool
    patterns: list  # any match => present
    origin: str = ""


FIELDS = [
    Field(
        "1", "method version + controls by ID", False,
        [r"MDS-\d{4}\.\d{2}\.\d{2}-v[\d.]+", r"\bv4\.0\b"],
    ),
    Field(
        "2", "outcome-family table with masses (§16.5(a) G-L1)", True,
        [r"outcome[- ]state famil", r"outcome famil", r"state famil",
         r"(?:\|\s*\d{1,3}\s*%\s*\|.*){2,}", r"\b\d{1,2}\s*goals?:\s*\d{1,3}\s*%",
         r"probability geometry"],
    ),
    Field(
        "3", "centre, numeric width, normalised edge — or an explicit derivation of each "
             "line's probability from the card's own printed distribution (§16.5(d) G-L8)",
        True,
        [r"normalis?ed edge", r"\bcentre\b.{0,80}\bwidth\b", r"\bwidth\b.{0,80}\bcentre\b",
         r"P\(\s*X\s*[<>]\s*L\s*\)", r"P\(total\s*[<>=]", r"\bpush\b.{0,40}\bmass\b",
         r"margin decomposition",
         # A printed discrete distribution plus explicit per-line derivation satisfies the
         # substance of G-L8 even without the centre/width wording — P-441 is the reference
         # example, and scoring it a miss would have been a false negative.
         r"Derived:\s*\n?.{0,120}(?:Over|Under)\s*[\d.]+\s*=\s*\d{1,3}\s*%",
         r"(?:Over|Under)\s*[\d.]+\s*=\s*\d{1,3}\s*%"],
    ),
    Field(
        "4", "complement decomposition for R1 and R2 (§16.5(e) G-L9)", False,
        [r"complement", r"losing states?", r"\bkill path", r"failure branch"],
    ),
    Field(
        "5", "P(R1 ∧ R2) with coupling label (§16.5(f) G-L10)", False,
        [r"P\(\s*R1\s*[∧&∩]", r"JOINT_UNQUANTIFIED", r"coupl", r"dependence",
         r"Fr[ée]chet"],
    ),
    Field(
        "5a", "P(¬R1 ∧ ¬R2) shared-failure mass; P(all fail) if 3+ rows share a driver "
              "(G-L17 §16.12(a); G-L21 §16.13(a))", True,
        [r"P\(\s*¬\s*R1", r"P\(\s*not\s*R1", r"shared[- ]failure", r"joint failure",
         r"both fail", r"all (?:of them )?fail", r"P\(all fail\)"],
        origin="P-427, P-438, P-444",
    ),
    Field(
        "5b", "every O/U row labelled FORCED_PAIR or FREE, preferred side named, push "
              "derived (G-L15 §16.11(n); G-L22 §16.13(b))", False,
        [r"FORCED_PAIR", r"\bFREE\b.{0,40}row", r"preferred (?:side|over/under|direction)"],
        origin="P-442–P-450",
    ),
    Field(
        "6", "one representative Rank-#1 outcome (§16.5(a))", False,
        [r"representative", r"central score", r"representative score"],
    ),
    Field(
        "7", "participant state per side: lineup / bench / coach (G14.2)", True,
        [r"CONFIRMED_OFFICIAL", r"SECONDARY_ONLY", r"NOT[_ ]RETRIEVED", r"RETRIEVAL_MISS",
         r"BENCH_NOT_RETRIEVED", r"\bstarting (?:line-?ups?|XIs?|five)\b",
         r"\bline-?ups?\b", r"\bbatting orders?\b", r"\bXIs?\b", r"\bsquads?\b",
         r"\bbench\b", r"\bcoach(?:es)?\b", r"\bmanagers?\b"],
    ),
    Field(
        "8", "AGGREGATE_ONLY flags and sampling-noise checks (§16.5(c),(g))", False,
        [r"AGGREGATE_ONLY", r"sampling noise", r"small[- ]sample", r"game log",
         r"numerator", r"denominator"],
    ),
    Field(
        "9", "settlement source/route for every row (G10.2, G-L14)", False,
        [r"settlement rout", r"settle(?:d|ment) (?:from|at)", r"field[- ]own",
         r"pre-?register"],
    ),
]

SETTLEMENT_FIELDS = [
    Field(
        "10", "process record + disruption facts + process-vs-outcome classification "
              "(G-L23 §16.13(c); §16.11(o))", True,
        [r"\bshots?\b.{0,40}\bon target\b", r"\bshots?\b.{0,30}\bpossession\b",
         r"red card", r"sin bin", r"disruption fact", r"regulation (?:total|split|ended)",
         r"inning[- ]by[- ]inning", r"powerplay", r"quarter scores?",
         r"process (?:read|record)"],
        origin="P-438",
    ),
]

# A card heading looks like "### `P-438` — ..." or "## P-438 [PROVISIONAL] — ..." etc.
CARD_HEADING = re.compile(r"^#{2,4}\s+.{0,8}?`?(P-\d{3}[A-Za-z0-9-]*)`?\b(.*)$")
SECTION_HEADING = re.compile(r"^##\s+(?!#)(.*)$")

# Cards that issued nothing are audited for identity only, not for forecast fields.
NO_FORECAST = re.compile(
    r"NO ISSUED FORECAST|NO PREDICTION|BLOCKED[ _]AT[ _]ISSUE|BK-P1\s*=\s*FAIL|"
    r"ADMINISTRATIVELY CLOSED|NO COMPLIANT FORECAST",
    re.I,
)
NO_ACTION = re.compile(r"CONDITION NOT MET|NO ACTION", re.I)


# Where a settled card's issued text ends and its settlement/retrospective text begins.
# Fields 1–9 are ISSUE-TIME fields: they must be satisfied by text the card printed before
# the event. Crediting them from settlement prose is the exact error this script exists to
# prevent — a retrospective that says "both top two lost to one state" is not the same
# object as a card that printed P(¬R1 ∧ ¬R2) beforehand.
SETTLEMENT_BOUNDARY = re.compile(
    r"^#{2,5}\s*(?:Settlement|Settled|Settlement and (?:full )?retrospective|"
    r"P-\d+\s*—\s*Settlement)\b|^\*\*(?:Status|Official (?:MLB )?final):\*\*",
    re.I | re.M,
)


@dataclass
class Card:
    cid: str
    title: str
    body: str
    section: str = ""
    present: dict = dc_field(default_factory=dict)
    kind: str = "forecast"  # forecast | no-forecast | no-action

    @property
    def issue_text(self) -> str:
        """The portion of the card printed before the event (fields 1–9)."""
        m = SETTLEMENT_BOUNDARY.search(self.body)
        return self.body[: m.start()] if m else self.body

    @property
    def settlement_text(self) -> str:
        """The portion appended at settlement (field 10)."""
        m = SETTLEMENT_BOUNDARY.search(self.body)
        return self.body[m.start():] if m else ""

    @property
    def is_settled(self) -> bool:
        return bool(SETTLEMENT_BOUNDARY.search(self.body))

    @property
    def missing_blocking(self):
        return [k for k, v in self.present.items() if not v["present"] and v["blocking"]]

    @property
    def missing_all(self):
        return [k for k, v in self.present.items() if not v["present"]]


def split_cards(text: str, section_filter: str | None):
    """Split a markdown document into card blocks, tracking the dated section each sits in."""
    lines = text.split("\n")
    cards: list[Card] = []
    cur_section = ""
    cur: Card | None = None
    buf: list[str] = []

    for line in lines:
        m_card = CARD_HEADING.match(line)
        m_sec = SECTION_HEADING.match(line) if not m_card else None

        if m_card:
            if cur is not None:
                cur.body = "\n".join(buf)
                cards.append(cur)
            cur = Card(cid=m_card.group(1), title=m_card.group(2).strip(" —-"),
                       body="", section=cur_section)
            buf = [line]
            continue

        if m_sec:
            # A new top-level "## " heading closes the current card.
            if cur is not None:
                cur.body = "\n".join(buf)
                cards.append(cur)
                cur = None
                buf = []
            cur_section = m_sec.group(1).strip()
            continue

        if cur is not None:
            buf.append(line)

    if cur is not None:
        cur.body = "\n".join(buf)
        cards.append(cur)

    # De-duplicate: keep the longest block per ID (a settlement block may repeat the ID).
    best: dict[str, Card] = {}
    for c in cards:
        if section_filter and section_filter.lower() not in c.section.lower():
            continue
        if c.cid not in best or len(c.body) > len(best[c.cid].body):
            best[c.cid] = c
    return [best[k] for k in sorted(best, key=lambda x: (len(x), x))]


def audit_card(card: Card, fields: list, doc_level: dict | None = None) -> Card:
    body = card.body
    if NO_FORECAST.search(body):
        card.kind = "no-forecast"
    elif NO_ACTION.search(body):
        card.kind = "no-action"

    doc_level = doc_level or {}

    for f in fields:
        # A card that issued nothing is audited for identity and retrieval only.
        if card.kind == "no-forecast" and f.key not in ("1", "7", "9", "10"):
            card.present[f.key] = {"present": True, "blocking": False, "label": f.label,
                                   "note": "n/a — nothing issued"}
            continue

        # Field 10 applies only to a settled card, and only against settlement text.
        if f.key == "10":
            if not card.is_settled:
                card.present[f.key] = {"present": True, "blocking": False,
                                       "label": f.label, "note": "n/a — not yet settled"}
                continue
            scope = card.settlement_text
        else:
            scope = card.issue_text

        hit = any(re.search(p, scope, re.I | re.S) for p in f.patterns)

        # Some fields are declared once for a whole running log rather than per card
        # (the method-version banner is the standard case). Credit them document-wide.
        note = ""
        if not hit and doc_level.get(f.key):
            hit, note = True, "declared document-wide"

        card.present[f.key] = {"present": hit, "blocking": f.blocking, "label": f.label,
                               "note": note}
    return card


# Fields that a running log may legitimately declare once for every card it contains.
DOC_LEVEL_KEYS = {"1"}


def scan_doc_level(text: str, fields: list) -> dict:
    """Detect fields declared once in a document preamble rather than per card."""
    preamble = text[: text.find("\n## ")] if "\n## " in text else text[:4000]
    out = {}
    for f in fields:
        if f.key in DOC_LEVEL_KEYS:
            out[f.key] = any(re.search(p, preamble, re.I | re.S) for p in f.patterns)
    return out


def render_markdown(cards: list, fields: list, quiet: bool) -> str:
    keys = [f.key for f in fields]
    out: list[str] = []
    if not quiet:
        out.append("| Card | " + " | ".join(keys) + " | Missing BLOCKING |")
        out.append("|---|" + "|".join([":-:"] * len(keys)) + "|---|")
        for c in cards:
            marks = []
            for k in keys:
                v = c.present.get(k)
                if v is None:
                    marks.append("·")
                elif v["note"].startswith("n/a"):
                    marks.append("–")
                elif v["note"] == "declared document-wide":
                    marks.append("d")
                elif v["present"]:
                    marks.append("Y")
                else:
                    marks.append("**N**" if v["blocking"] else "n")
            mb = ", ".join(c.missing_blocking) or "—"
            out.append(f"| `{c.cid}` | " + " | ".join(marks) + f" | {mb} |")
        out.append("")
        out.append("Y = printed · d = declared document-wide · n = missing (non-blocking) "
                   "· **N** = missing (BLOCKING) · – = not applicable")
        out.append("")

    forecast_cards = [c for c in cards if c.kind == "forecast"]
    out.append(f"**Cards audited:** {len(cards)} "
               f"({len(forecast_cards)} issued a forecast, "
               f"{len([c for c in cards if c.kind=='no-forecast'])} issued nothing, "
               f"{len([c for c in cards if c.kind=='no-action'])} no-action)")

    for f in fields:
        miss = [c.cid for c in cards
                if c.present.get(f.key) and not c.present[f.key]["present"]]
        if miss:
            tag = "**BLOCKING**" if f.blocking else "process defect"
            shown = ", ".join(f"`{m}`" for m in miss[:12])
            more = f" (+{len(miss)-12} more)" if len(miss) > 12 else ""
            out.append(f"- Field **{f.key}** ({f.label}) — {tag} — missing on "
                       f"{len(miss)}/{len(cards)}: {shown}{more}")

    bad = [c for c in cards if c.missing_blocking]
    out.append("")
    if bad:
        out.append(f"**RESULT: {len(bad)} card(s) missing a BLOCKING field** — "
                   + ", ".join(f"`{c.cid}`" for c in bad))
    else:
        out.append("**RESULT: every audited card printed every BLOCKING field.**")
    return "\n".join(out)


def main(argv=None) -> int:
    # The field labels carry ¬ ∧ é, and the default Windows console codepage is cp1252.
    # Force UTF-8 on stdout/stderr so the report is identical on every platform.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--section", default=None,
                    help="only audit cards inside the dated section matching this text")
    ap.add_argument("--settlement", action="store_true",
                    help="also check field 10 (process record), settlement passes only")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    fields = list(FIELDS) + (SETTLEMENT_FIELDS if args.settlement else [])
    all_cards: list[Card] = []

    for path in args.files:
        try:
            with io.open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as exc:
            print(f"error: cannot read {path}: {exc}", file=sys.stderr)
            return 2
        cards = split_cards(text, args.section)
        if not cards:
            print(f"warning: no `P-###` card headings found in {path}", file=sys.stderr)
        doc_level = scan_doc_level(text, fields)
        all_cards.extend(audit_card(c, fields, doc_level) for c in cards)

    if not all_cards:
        print("error: no cards to audit", file=sys.stderr)
        return 2

    all_cards.sort(key=lambda c: c.cid)

    if args.json:
        print(json.dumps(
            [{"card": c.cid, "section": c.section, "kind": c.kind,
              "fields": c.present, "missing_blocking": c.missing_blocking}
             for c in all_cards], indent=2, ensure_ascii=False))
    else:
        print(render_markdown(all_cards, fields, args.quiet))

    return 1 if any(c.missing_blocking for c in all_cards) else 0


if __name__ == "__main__":
    sys.exit(main())
