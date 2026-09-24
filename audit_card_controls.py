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
failure mode that actually recurs. **It checks presence, not truth**: a card can print a
lineup field that the official box later contradicts (2026-09-24(f): five of seven
diffable cards). The settlement fields `10l` (C-LINEUP-DIFF) and `10p`
(C-PROCESS-RECORD-PROVENANCE) exist so that the truth check is at least *recorded*.

Usage
-----
    python audit_card_controls.py <file.md> [<file.md> ...]
    python audit_card_controls.py <file.md> --section "2026-09-17(b)"
    python audit_card_controls.py <file.md> --json
    python audit_card_controls.py <file.md> --settlement
    python audit_card_controls.py <file.md> --settlement --strict

Options
-------
    --section TEXT   Only audit cards inside the dated section whose heading contains TEXT.
    --settlement     Also check the settlement fields (10, 10p, 10l, 10z), settlement passes only.
    --strict         Treat the 2026-09-24(f)/2026-09-25 controls as BLOCKING: 7r (S-1 Rev 2
                     receipt), T13 (tennis benchmark, RULES_TENNIS TE-P5), WB (reference
                     width, C-WIDTH-BENCHMARK), BP (BASELINE_P, C-BASELINE-SKILL; from
                     CONTROL_MANIFEST_2026-09-25-3), DL (departure ledger) and PC (non-baseball +k.5
                     cushion; both from CONTROL_MANIFEST_2026-09-25-4), HC (tennis handicap coherence), 10p
                     (process-record provenance), 10l (lineup diff) and 10z (standardised
                     miss, C-WIDTH-Z). Use it on every card issued or settled after the
                     2026-09-25 control manifest (WB, HC and 10z from CONTROL_MANIFEST_2026-09-25-2).
                     Without it these fields are reported as process defects only, so historical
                     cohorts are not failed retroactively for controls that postdate them.
    --json           Emit machine-readable JSON instead of the Markdown table.
    --quiet          Suppress the per-card table; print only the summary.
    --allow-empty    Exit 0 instead of 2 when no card is found (CI over an empty active mini log).

Exit codes
----------
    0  every audited card printed every BLOCKING field
    1  at least one card is missing a BLOCKING field
    2  usage or file error

BLOCKING fields (a missing one blocks issue under §16.8): 2, 3, 5a, 7; at settlement 10;
with --strict also 7r, T13, WB, BP, DL, PC, HC, 10p, 10l, 10z (each only where it applies).
Everything else is recorded as a process defect on that card without blocking.

Card segmentation (repaired 2026-09-25; 2026-09-23(c) proposal)
---------------------------------------------------------------
A card starts at a `P-###` or `TMP-YYYYMMDD-…` heading (levels 2–6) or at a
`<!-- BEGIN VERBATIM ISSUED RECORD: <ID> … -->` marker. Inside a BEGIN/END verbatim block
no heading closes the card. `<!-- END VERBATIM ISSUED RECORD … -->` always closes it.
`## Entry N` headings never close a card. An issue-time line such as
"**Status:** UNSETTLED — LIVE-ISSUED VIEW" is not a settlement boundary (it truncated
P-494's audit on 2026-09-23/24).

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
from typing import Callable, Optional

# --------------------------------------------------------------------------------------
# Field definitions — RULES_GENERAL.md §16.8, as amended 2026-09-17(b), 2026-09-24(f)
# and 2026-09-25
# --------------------------------------------------------------------------------------


@dataclass
class Field:
    key: str
    label: str
    blocking: bool
    patterns: list  # any match => present
    origin: str = ""
    strict_blocking: bool = False  # becomes BLOCKING under --strict
    # applies(card) -> bool; None means "applies to every forecast card"
    applies: Optional[Callable] = None


TENNIS_RE = re.compile(
    r"\b(?:WTA|ATP|ITF|UTR)\b|Challenger|\bgames handicap|total games|straight sets|"
    r"\btiebreak\b|Grand Slam", re.I)
CRICKET_RE = re.compile(
    r"\b(?:T20|ODI|powerplay|wickets?|CPL|IPL|BBL|ETPL|WPL|PSL|The Hundred|"
    r"Sheffield Shield|Ranji|County Championship)\b|\btoss\b", re.I)
# A team-sport league named in the card title settles the sport before the body is scanned
# (2026-09-25: an NBL card's "full-game handicap" was mis-read as tennis).
TEAM_TITLE_RE = re.compile(
    r"\b(?:NBL|NBA|WNBA|MLB|NPB|KBO|CPBL|LMB|NHL|NFL|AFLW?|NRL|LKL|EuroLeague|FIBA|EPL|"
    r"Premier League|MLS|A-League|Bundesliga|LaLiga|Serie A|Ligue 1|UEFA|basketball|"
    r"baseball|soccer|football|hockey|rugby)\b", re.I)


def detect_sport(text: str, title: str = "") -> str:
    """Heuristic sport label used only to decide whether a sport-checklist field applies.

    The card title is checked first; the body scan is a fallback.
    """
    if title:
        if TENNIS_RE.search(title):
            return "tennis"
        if CRICKET_RE.search(title):
            return "cricket"
        if TEAM_TITLE_RE.search(title):
            return "other"
    head = text[:6000]
    if TENNIS_RE.search(head):
        return "tennis"
    if CRICKET_RE.search(head):
        return "cricket"
    return "other"


def _claims_projected_beat(card) -> bool:
    return bool(re.search(r"PROJECTED_BEAT_VERIFIED", card.issue_text))


def _is_tennis(card) -> bool:
    return card.sport == "tennis"


def _is_cricket(card) -> bool:
    return card.sport == "cricket"


def _team_sport_settled(card) -> bool:
    return card.is_settled and card.sport != "tennis"


# A card "prints a width" when a numeric SD/width appears in its issued text (2026-09-25(b)).
WIDTH_PRINTED_RE = re.compile(r"\bwidth\b[^\n]{0,20}?\d|\bSD\b\s*[=:≈]?\s*\d", re.I)


def _prints_width(card) -> bool:
    return bool(WIDTH_PRINTED_RE.search(card.issue_text))


def _settled_with_width(card) -> bool:
    return card.is_settled and _prints_width(card)


BASEBALL_RE = re.compile(r"\b(MLB|NPB|KBO|CPBL|baseball|run ?line|innings? pitched|starting pitcher)\b", re.I)
PLUS_CUSHION_RE = re.compile(r"(?<![\w.])\+\s?\d+\.5\b")


def _nonbaseball_plus_cushion(card) -> bool:
    """A +k.5 handicap row on a card that is not baseball (2026-09-25(d): 17/40 at a stated 0.642)."""
    head = card.title + " " + card.issue_text[:4000]
    return bool(PLUS_CUSHION_RE.search(card.issue_text)) and not BASEBALL_RE.search(head)


def _tennis_handicap(card) -> bool:
    return card.sport == "tennis" and bool(
        re.search(r"[−-]\s*\d+\.5\b[^\n]{0,40}(?:games|handicap)|games handicap|handicap[^\n]{0,20}[−-]\s*\d+\.5",
                  card.issue_text, re.I))


FIELDS = [
    Field(
        "1", "method version + controls by ID", False,
        [r"MDS-\d{4}\.\d{2}\.\d{2}-v[\d.]+", r"\bv4\.0\b"],
    ),
    Field(
        "2", "outcome-family table with masses (§16.5(a) G-L1)", True,
        [r"outcome[- ]state famil", r"outcome famil", r"state famil",
         r"(?:\|\s*\d{1,3}\s*%\s*\|.*){2,}", r"\b\d{1,2}\s*goals?:\s*\d{1,3}\s*%",
         r"probability geometry",
         # "| Family (live, given completion) | Mass |" with a "Sum | 1.0000" row (P-494).
         r"\|\s*(?:\*\*)?Family\b[^|\n]{0,60}\|\s*(?:\*\*)?(?:Probability )?Mass",
         r"\bSum\b\**\s*\|\s*\**\s*1\.0{2,4}\b"],
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
        [r"CONFIRMED_OFFICIAL", r"PROJECTED_BEAT_VERIFIED", r"LINEUPS_NOT_YET_PUBLISHED",
         r"SECONDARY_ONLY", r"NOT[_ ]RETRIEVED", r"RETRIEVAL_MISS",
         r"BENCH_NOT_RETRIEVED", r"\bstarting (?:line-?ups?|XIs?|five)\b",
         r"\bline-?ups?\b", r"\bbatting orders?\b", r"\bXIs?\b", r"\bsquads?\b",
         r"\bbench\b", r"\bcoach(?:es)?\b", r"\bmanagers?\b"],
    ),
    Field(
        "7r", "S-1 Rev 2 receipt (outlet, reporter, timestamp, verbatim quote, two sources) "
              "wherever PROJECTED_BEAT_VERIFIED is claimed (RULES_GENERAL 2026-09-24(f)(c))",
        False,
        [r"S-1 Rev 2 receipt", r"s1r2_receipt"],
        origin="P-500, P-501, P-503, P-504, P-508, P-509",
        strict_blocking=True, applies=_claims_projected_beat,
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
    Field(
        "BR", "REFERENCE_BASE_RATE (population, threshold, n) or NOT_YET_DERIVED recorded "
              "(sport §9.10/§10.10; R-7 of the 2026-09-22 audit)", False,
        [r"REFERENCE_BASE_RATE", r"NOT_YET_DERIVED", r"reference base rate",
         r"\bbase[- ]rate"],
        origin="P-482, P-483",
    ),
    Field(
        "T13", "tennis: dated independent Elo benchmark beside the winner mass "
               "(RULES_TENNIS TE-P5 / control 13)", False,
        [r"\bElo\b", r"benchmark"],
        origin="P-350, P-483", strict_blocking=True, applies=_is_tennis,
    ),
    Field(
        "CVW", "cricket: venue window by innings order, or INSUFFICIENT_VENUE_HISTORY "
               "(RULES_CRICKET §10.8; control 21)", False,
        [r"venue window", r"INSUFFICIENT_VENUE_HISTORY", r"by innings order",
         r"innings[- ]order", r"bat(?:ting)?[- ]first.{0,80}chas"],
        origin="P-482", applies=_is_cricket,
    ),
    Field(
        "WB", "width printed beside the competition's reference width, or "
              "REFERENCE_WIDTH_NOT_YET_DERIVED (C-WIDTH-BENCHMARK, RULES_GENERAL 2026-09-25(b)(a))",
        False,
        [r"C-WIDTH-BENCHMARK", r"reference width", r"REFERENCE_WIDTH_NOT_YET_DERIVED",
         r"width benchmark", r"benchmark width", r"WIDTH_BELOW_REFERENCE"],
        origin="P-497, P-498, P-508 (2026-09-24 cohort)", strict_blocking=True,
        applies=_prints_width,
    ),
    Field(
        "BP", "BASELINE_P printed beside each ranked row (naive leak-free population baseline), or "
              "BASELINE_P: NOT_YET_DERIVED (C-BASELINE-SKILL, RULES_GENERAL 2026-09-25(c))", False,
        [r"BASELINE_P", r"C-BASELINE-SKILL", r"\bbaseline p\b"],
        origin="2026-09-25(c) skill check (SKILL_BASELINE_LEDGER.md)", strict_blocking=True,
    ),
    Field(
        "DL", "departure ledger: the logit departure of each ranked row from BASELINE_P attributed to named "
              "mechanisms (C-DEPARTURE-LEDGER, RULES_GENERAL 2026-09-25(d))", False,
        [r"C-DEPARTURE-LEDGER", r"logit departure", r"departure (?:from|v\.?|vs\.?) BASELINE", r"UNEXPLAINED_DEPARTURE"],
        origin="2026-09-25(d) settled-row review", strict_blocking=True,
    ),
    Field(
        "PC", "non-baseball +k.5 cushion: population margin band, BASELINE_P, P(underdog wins) + P(loses by ≤ k) "
              "decomposition and the named reason it stays close (C-PLUS-CUSHION, RULES_GENERAL 2026-09-25(d))", False,
        [r"C-PLUS-CUSHION", r"margin band", r"loses by (?:≤|<=|at most)\s*\d", r"P\(\s*loses? by"],
        origin="2026-09-25(d): 17/40 won at a stated 0.642", strict_blocking=True,
        applies=_nonbaseball_plus_cushion,
    ),
    Field(
        "HC", "tennis games-handicap: P(win), implied P(margin ≥ k+1 | win) and the population "
              "conditional (C-HCP-COHERENCE, RULES_GENERAL 2026-09-25(b)(f))", False,
        [r"C-HCP-COHERENCE", r"HCP_CONDITIONAL", r"P\(\s*margin\s*(?:≥|>=)\s*\d+\s*\|\s*win",
         r"implied P\(margin", r"conditional on (?:the |her |his )?(?:win|winning)"],
        origin="P-495", strict_blocking=True, applies=_tennis_handicap,
    ),
]

SETTLEMENT_FIELDS = [
    Field(
        "10", "process record + disruption facts + process-vs-outcome classification "
              "(G-L23 §16.13(c); §16.11(o))", True,
        [r"\bshots?\b.{0,40}\bon target\b", r"\bshots?\b.{0,30}\bpossession\b",
         r"red card", r"sin bin", r"disruption fact", r"regulation (?:total|split|ended)",
         r"inning[- ]by[- ]inning", r"powerplay", r"quarter scores?", r"quarter lines?",
         r"process (?:read|record)"],
        origin="P-438",
    ),
    Field(
        "10p", "process facts carry the endpoint/URL they were read from "
               "(C-PROCESS-RECORD-PROVENANCE, 2026-09-24(f))", False,
        [r"https?://", r"\bstatsapi\b", r"site\.api", r"api-web", r"\bapi\.[a-z]",
         r"\b[a-z0-9-]+\.(?:com|org|net|jp|au|lt|kr|fr|cz|sv|io)(?:\.au)?(?:/|\b)"],
        origin="2026-09-24(e)", strict_blocking=True,
    ),
    Field(
        "10l", "lineup diff: card-named starters v official box, 'k of n started' "
               "(C-LINEUP-DIFF, 2026-09-24(f))", False,
        [r"C-LINEUP-DIFF", r"named starters? started", r"\b\d+\s*(?:of|/)\s*\d+\s*named",
         r"LINEUP_CLAIM_FALSE", r"lineup diff", r"\b\d\s*of\s*\d\b.{0,40}start"],
        origin="P-500, P-501, P-503, P-508", strict_blocking=True,
        applies=_team_sport_settled,
    ),
    Field(
        "10z", "standardised miss z = (actual − centre)/width for total and margin "
               "(C-WIDTH-Z, RULES_GENERAL 2026-09-25(b)(b))", False,
        [r"C-WIDTH-Z", r"\bz\s*(?:_?(?:total|margin|tot|mar))?\s*=\s*[−+-]?\s*\d",
         r"standardi[sz]ed (?:miss|residual|error)"],
        origin="2026-09-24 cohort (BASE_RATES_REGISTER §7.6)", strict_blocking=True,
        applies=_settled_with_width,
    ),
]

SETTLEMENT_KEYS = frozenset(f.key for f in SETTLEMENT_FIELDS)

ID_PATTERN = r"(?:P-\d{3}[A-Za-z0-9-]*|TMP-\d{8}-[A-Z0-9-]+)"

# A card heading looks like "### `P-438` — ...", "## P-438 [PROVISIONAL] — ...",
# "##### P-493 - KBO ..." or "### TMP-20260923-NBL-CNS-TAS — ...".
CARD_HEADING = re.compile(r"^#{2,6}\s+.{0,8}?`?(" + ID_PATTERN + r")`?(?![A-Za-z0-9])(.*)$")
SECTION_HEADING = re.compile(r"^##\s+(?!#)(.*)$")
ENTRY_HEADING = re.compile(r"^##\s+Entry\s+\d", re.I)
VERBATIM_BEGIN = re.compile(r"<!--\s*BEGIN VERBATIM ISSUED RECORD:\s*`?(" + ID_PATTERN + r")")
VERBATIM_END = re.compile(r"<!--\s*END VERBATIM ISSUED RECORD")

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
# An issue-time status line ("**Status:** UNSETTLED — LIVE-ISSUED VIEW", "**Status:**
# UPCOMING / PREGAME AT FREEZE") is NOT a settlement boundary (repaired 2026-09-25).
SETTLEMENT_BOUNDARY = re.compile(
    r"^#{2,5}\s*(?:Settlement|Settled|Settlement and (?:full )?retrospective|"
    r"P-\d+\s*—\s*Settlement)\b|"
    r"^\*\*Status:\*\*\s*(?!\**\s*(?:UNSETTLED|UPCOMING|PREGAME|LIVE|PENDING|OPEN|NOT\b|"
    r"SCHEDULED|ACTIVE))|"
    r"^\*\*Official (?:MLB )?final:\*\*",
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
    sport: str = "other"

    @property
    def issue_text(self) -> str:
        """The portion of the card printed before the event (fields 1–9)."""
        m = SETTLEMENT_BOUNDARY.search(self.body)
        return self.body[: m.start()] if m else self.body

    @property
    def settlement_text(self) -> str:
        """The portion appended at settlement (fields 10, 10p, 10l, 10z)."""
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
    in_verbatim = False

    def close():
        nonlocal cur, buf
        if cur is not None:
            cur.body = "\n".join(buf)
            cards.append(cur)
        cur, buf = None, []

    for line in lines:
        m_begin = VERBATIM_BEGIN.search(line)
        if m_begin:
            close()
            cur = Card(cid=m_begin.group(1), title="(verbatim issued record)", body="",
                       section=cur_section)
            buf = [line]
            in_verbatim = True
            continue

        if VERBATIM_END.search(line):
            if cur is not None:
                buf.append(line)
                close()
            in_verbatim = False
            continue

        if in_verbatim:
            # Inside a preserved record no heading closes the card.
            if cur is not None:
                buf.append(line)
            continue

        m_card = CARD_HEADING.match(line)
        m_sec = None if (m_card or ENTRY_HEADING.match(line)) else SECTION_HEADING.match(line)

        if m_card:
            close()
            cur = Card(cid=m_card.group(1), title=m_card.group(2).strip(" —-"),
                       body="", section=cur_section)
            buf = [line]
            continue

        if m_sec:
            # A new top-level "## " heading closes the current card.
            close()
            cur_section = m_sec.group(1).strip()
            continue

        if cur is not None:
            buf.append(line)

    close()

    # De-duplicate: keep the longest block per ID (a settlement block may repeat the ID).
    best: dict[str, Card] = {}
    for c in cards:
        if section_filter and section_filter.lower() not in c.section.lower():
            continue
        if c.cid not in best or len(c.body) > len(best[c.cid].body):
            best[c.cid] = c
    return [best[k] for k in sorted(best, key=lambda x: (len(x), x))]


def audit_card(card: Card, fields: list, doc_level: dict | None = None,
               strict: bool = False) -> Card:
    body = card.body
    if NO_FORECAST.search(body):
        card.kind = "no-forecast"
    elif NO_ACTION.search(body):
        card.kind = "no-action"
    card.sport = detect_sport(card.issue_text or body, card.title)

    doc_level = doc_level or {}

    for f in fields:
        blocking = f.blocking or (strict and f.strict_blocking)

        # A card that issued nothing is audited for identity and retrieval only.
        if card.kind == "no-forecast" and f.key not in ("1", "7", "9", "10", "10p", "10l"):
            card.present[f.key] = {"present": True, "blocking": False, "label": f.label,
                                   "note": "n/a — nothing issued"}
            continue

        # Settlement fields apply only to a settled card, and only against settlement text.
        if f.key in SETTLEMENT_KEYS:
            if not card.is_settled:
                card.present[f.key] = {"present": True, "blocking": False,
                                       "label": f.label, "note": "n/a — not yet settled"}
                continue
            scope = card.settlement_text
        else:
            scope = card.issue_text

        if f.applies is not None and not f.applies(card):
            card.present[f.key] = {"present": True, "blocking": False, "label": f.label,
                                   "note": "n/a — does not apply"}
            continue

        hit = any(re.search(p, scope, re.I | re.S) for p in f.patterns)

        # Some fields are declared once for a whole running log rather than per card
        # (the method-version banner is the standard case). Credit them document-wide.
        note = ""
        if not hit and doc_level.get(f.key):
            hit, note = True, "declared document-wide"

        card.present[f.key] = {"present": hit, "blocking": blocking, "label": f.label,
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
        miss = [c for c in cards
                if c.present.get(f.key) and not c.present[f.key]["present"]]
        if miss:
            tag = "**BLOCKING**" if any(c.present[f.key]["blocking"] for c in miss) \
                else "process defect"
            shown = ", ".join(f"`{m.cid}`" for m in miss[:12])
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
                    help="also check the settlement fields (10, 10p, 10l, 10z)")
    ap.add_argument("--strict", action="store_true",
                    help="treat the 2026-09-24(f)/2026-09-25 controls "
                         "(7r, T13, WB, BP, DL, PC, HC, 10p, 10l, 10z) as BLOCKING")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--allow-empty", action="store_true",
                    help="exit 0 (not 2) when the files contain no cards — for CI runs over an "
                         "active mini log that has not issued a card yet")
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
            print(f"warning: no `P-###`/`TMP-` card headings found in {path}", file=sys.stderr)
        doc_level = scan_doc_level(text, fields)
        all_cards.extend(audit_card(c, fields, doc_level, strict=args.strict) for c in cards)

    if not all_cards:
        if args.allow_empty:
            print("no cards to audit (--allow-empty): nothing issued yet")
            return 0
        print("error: no cards to audit", file=sys.stderr)
        return 2

    all_cards.sort(key=lambda c: c.cid)

    if args.json:
        print(json.dumps(
            [{"card": c.cid, "section": c.section, "kind": c.kind, "sport": c.sport,
              "fields": c.present, "missing_blocking": c.missing_blocking}
             for c in all_cards], indent=2, ensure_ascii=False))
    else:
        print(render_markdown(all_cards, fields, args.quiet))

    return 1 if any(c.missing_blocking for c in all_cards) else 0


if __name__ == "__main__":
    sys.exit(main())
