"""Tests for audit_card_controls.py (added 2026-09-25 audit closure).

Each test pins one repaired behaviour or one new field. The fixtures are synthetic
Markdown, not historical cards, so the tests validate the detector, not any forecast.
"""
import unittest

import audit_card_controls as a

FULL_ISSUE = """
- Outcome-state family table with masses: F1 0.40, F2 0.60.
- Centre 180, width 16, normalised edge 0.28.
- Complement decomposition stated.
- P(R1 ∧ R2) = 0.30; coupling positive.
- P(¬R1 ∧ ¬R2) = 0.20 (shared-failure state named).
- Over/Under labelled FORCED_PAIR; preferred side Under.
- Representative Rank-#1 outcome 90-86.
- Starting lineups CONFIRMED_OFFICIAL; bench and coaches listed.
- AGGREGATE_ONLY: none.
- Settlement route: field owner.
- REFERENCE_BASE_RATE: NOT_YET_DERIVED.
"""


def audit(text, settlement=False, strict=False):
    fields = list(a.FIELDS) + (a.SETTLEMENT_FIELDS if settlement else [])
    cards = a.split_cards(text, None)
    return {c.cid: a.audit_card(c, fields, {}, strict=strict) for c in cards}


class SegmentationTests(unittest.TestCase):
    def test_issue_time_status_line_is_not_settlement_boundary(self):
        text = "## Log\n\n#### P-494 — WTA live view\n\n**Status:** UNSETTLED — **LIVE-ISSUED VIEW**.\n" + FULL_ISSUE
        card = audit(text)["P-494"]
        self.assertFalse(card.is_settled)
        self.assertEqual(card.missing_blocking, [])

    def test_real_settlement_status_is_boundary(self):
        text = "#### P-600 — Game\n" + FULL_ISSUE + "\n**Status:** FINAL / SETTLED. Quarter scores 20-20.\n"
        card = audit(text, settlement=True)["P-600"]
        self.assertTrue(card.is_settled)

    def test_entry_heading_does_not_close_card(self):
        text = "#### P-601 — Match\n\nIntro.\n\n## Entry 2 — issued view\n" + FULL_ISSUE
        card = audit(text)["P-601"]
        self.assertEqual(card.missing_blocking, [])

    def test_verbatim_block_keeps_headings_inside_card(self):
        text = ("## Section\n<!-- BEGIN VERBATIM ISSUED RECORD: P-602 (heading levels demoted) -->\n"
                "#### P-602 — Game\n\n## Some inner heading\n" + FULL_ISSUE +
                "<!-- END VERBATIM ISSUED RECORD: P-602 -->\n\n## Next section\nText.\n")
        cards = audit(text)
        self.assertIn("P-602", cards)
        self.assertEqual(cards["P-602"].missing_blocking, [])

    def test_tmp_id_detected_from_verbatim_marker(self):
        text = ("<!-- BEGIN VERBATIM ISSUED RECORD: TMP-20260923-NPB-CHU-DB-G25 (R1 card) -->\n"
                "###### Same-event reforecast\n" + FULL_ISSUE +
                "<!-- END VERBATIM ISSUED RECORD: TMP-20260923-NPB-CHU-DB-G25 -->\n")
        self.assertIn("TMP-20260923-NPB-CHU-DB-G25", audit(text))

    def test_level_five_heading_detected(self):
        text = "##### P-493 - KBO - Kia Tigers @ Doosan Bears\n" + FULL_ISSUE
        self.assertIn("P-493", audit(text))

    def test_end_marker_closes_card(self):
        text = ("### P-603 — Game\n" + FULL_ISSUE +
                "<!-- END VERBATIM ISSUED RECORD: P-603 -->\n\nTrailing unrelated text with https://example.com\n")
        card = audit(text)["P-603"]
        self.assertNotIn("Trailing unrelated", card.body)


    def test_family_mass_table_with_sum_row_detected(self):
        text = ("#### P-604 — WTA live\n| Family (live, given completion) | Mass |\n|---|---:|\n"
                "| B1 A straight sets | 0.60 |\n| B2 B wins | 0.40 |\n| **Sum** | **1.0000** |\n"
                "Centre 19.9, width 5.7, normalised edge 0.24. P(¬R1 ∧ ¬R2) = 0.05. Lineup NOT_APPLICABLE; coaches listed.\n")
        card = audit(text)["P-604"]
        self.assertTrue(card.present["2"]["present"])


class NewFieldTests(unittest.TestCase):
    def test_projected_beat_without_receipt_flagged(self):
        text = "#### P-610 — Game\n" + FULL_ISSUE + "Lineups PROJECTED_BEAT_VERIFIED.\n"
        card = audit(text)["P-610"]
        self.assertFalse(card.present["7r"]["present"])
        self.assertFalse(card.present["7r"]["blocking"])
        strict = audit(text, strict=True)["P-610"]
        self.assertIn("7r", strict.missing_blocking)

    def test_projected_beat_with_receipt_passes(self):
        text = ("#### P-611 — Game\n" + FULL_ISSUE +
                "Lineups PROJECTED_BEAT_VERIFIED. S-1 Rev 2 receipt: Outlet A, Reporter, 17:05, \"quote\".\n")
        card = audit(text, strict=True)["P-611"]
        self.assertTrue(card.present["7r"]["present"])

    def test_receipt_not_applicable_without_projected_claim(self):
        card = audit("#### P-612 — Game\n" + FULL_ISSUE)["P-612"]
        self.assertTrue(card.present["7r"]["note"].startswith("n/a"))

    def test_tennis_benchmark_required_for_tennis_only(self):
        tennis = "#### P-620 — WTA 250 R32, total games 19.5\n" + FULL_ISSUE
        card = audit(tennis, strict=True)["P-620"]
        self.assertEqual(card.sport, "tennis")
        self.assertIn("T13", card.missing_blocking)
        with_elo = "#### P-621 — WTA 250 R32\n" + FULL_ISSUE + "Tennis Abstract Elo benchmark 74%.\n"
        self.assertTrue(audit(with_elo, strict=True)["P-621"].present["T13"]["present"])
        other = audit("#### P-622 — NBL basketball\n" + FULL_ISSUE, strict=True)["P-622"]
        self.assertTrue(other.present["T13"]["note"].startswith("n/a"))

    def test_team_sport_title_overrides_body_tennis_words(self):
        # Regression 2026-09-25: an NBL card's "full-game handicap" was mis-read as tennis.
        text = ("### TMP-20260923-NBL-CNS-TAS — NBL — Cairns v Tasmania\n" + FULL_ISSUE +
                "The full-game handicap and total include OT.\n")
        card = audit(text, strict=True)["TMP-20260923-NBL-CNS-TAS"]
        self.assertEqual(card.sport, "other")
        self.assertTrue(card.present["T13"]["note"].startswith("n/a"))

    def test_cricket_venue_window(self):
        cricket = "#### P-630 — CPL T20 powerplay\n" + FULL_ISSUE
        card = audit(cricket)["P-630"]
        self.assertEqual(card.sport, "cricket")
        self.assertFalse(card.present["CVW"]["present"])
        ok = cricket + "Venue window by innings order: bat-first 35.0, chasing 60.0.\n"
        self.assertTrue(audit(ok)["P-630"].present["CVW"]["present"])

    def test_settlement_provenance_and_lineup_diff(self):
        base = "#### P-640 — NBL basketball\n" + FULL_ISSUE + "\n**Status:** FINAL / SETTLED.\nQuarter scores 20-20.\n"
        card = audit(base, settlement=True, strict=True)["P-640"]
        self.assertIn("10p", card.missing_blocking)
        self.assertIn("10l", card.missing_blocking)
        good = base + "Read from https://site.api.espn.com/summary. C-LINEUP-DIFF: 5 of 5 named starters started.\n"
        card = audit(good, settlement=True, strict=True)["P-640"]
        self.assertTrue(card.present["10p"]["present"])
        self.assertTrue(card.present["10l"]["present"])

    def test_lineup_diff_not_applicable_to_tennis(self):
        text = ("#### P-650 — ATP Challenger, games handicap\n" + FULL_ISSUE + "Elo benchmark.\n"
                "\n**Status:** FINAL / SETTLED. https://www.itftennis.com draws page.\n")
        card = audit(text, settlement=True, strict=True)["P-650"]
        self.assertTrue(card.present["10l"]["note"].startswith("n/a"))

    def test_default_mode_keeps_new_fields_non_blocking(self):
        text = ("#### P-660 — NBL basketball\n" + FULL_ISSUE +
                "Lineups PROJECTED_BEAT_VERIFIED.\n\n**Status:** FINAL / SETTLED.\nQuarter scores.\n")
        card = audit(text, settlement=True, strict=False)["P-660"]
        self.assertEqual(card.missing_blocking, [])


class ResearchFieldTests(unittest.TestCase):
    """Fields added 2026-09-25(b): WB (C-WIDTH-BENCHMARK), HC (C-HCP-COHERENCE), 10z (C-WIDTH-Z)."""

    def test_width_benchmark_required_when_width_printed(self):
        card = audit("#### P-670 — NBL basketball\n" + FULL_ISSUE, strict=True)["P-670"]
        self.assertIn("WB", card.missing_blocking)
        ok = "#### P-671 — NBL basketball\n" + FULL_ISSUE + "Reference width (BASE_RATES §7.1(b)) 18.7.\n"
        self.assertTrue(audit(ok, strict=True)["P-671"].present["WB"]["present"])
        nd = "#### P-672 — LKL basketball\n" + FULL_ISSUE + "REFERENCE_WIDTH_NOT_YET_DERIVED.\n"
        self.assertTrue(audit(nd, strict=True)["P-672"].present["WB"]["present"])

    def test_width_benchmark_not_applicable_without_width(self):
        text = ("#### P-673 — Match\nOutcome family table. P(total > 2.5) = 0.55. P(¬R1 ∧ ¬R2) = 0.2. "
                "Starting XIs CONFIRMED_OFFICIAL.\n")
        card = audit(text, strict=True)["P-673"]
        self.assertTrue(card.present["WB"]["note"].startswith("n/a"))

    def test_width_benchmark_is_issue_time_only(self):
        # A reference width written only in the settlement text does not satisfy WB.
        text = ("#### P-674 — NBL basketball\n" + FULL_ISSUE +
                "\n**Status:** FINAL / SETTLED.\nQuarter scores. Reference width 18.7 noted after the game.\n")
        card = audit(text, settlement=True, strict=True)["P-674"]
        self.assertIn("WB", card.missing_blocking)

    def test_standardised_miss_at_settlement(self):
        base = ("#### P-680 — NBL basketball\n" + FULL_ISSUE + "Reference width 18.7.\n"
                "\n**Status:** FINAL / SETTLED.\nQuarter scores. https://site.api.espn.com C-LINEUP-DIFF: 5 of 5 named starters started.\n")
        card = audit(base, settlement=True, strict=True)["P-680"]
        self.assertIn("10z", card.missing_blocking)
        good = base + "z_total = +0.89; z_margin = −0.18 (C-WIDTH-Z).\n"
        card = audit(good, settlement=True, strict=True)["P-680"]
        self.assertTrue(card.present["10z"]["present"])
        self.assertEqual(card.missing_blocking, [])

    def test_standardised_miss_not_applicable_when_unsettled(self):
        card = audit("#### P-681 — NBL basketball\n" + FULL_ISSUE, settlement=True, strict=True)["P-681"]
        self.assertTrue(card.present["10z"]["note"].startswith("n/a"))

    def test_tennis_handicap_coherence(self):
        text = ("#### P-690 — WTA 125 Tolentino, games handicap\n" + FULL_ISSUE +
                "Elo benchmark. Reference width 5.79. R1 Romero Gormaz −5.5 games.\n")
        card = audit(text, strict=True)["P-690"]
        self.assertIn("HC", card.missing_blocking)
        ok = text + "Implied P(margin ≥ 6 | win) = 0.70 v straight-sets reference 0.663 (C-HCP-COHERENCE).\n"
        self.assertTrue(audit(ok, strict=True)["P-690"].present["HC"]["present"])

    def test_handicap_coherence_not_applicable_to_team_sports(self):
        text = "#### P-691 — NBL basketball, United −2.5\n" + FULL_ISSUE
        card = audit(text, strict=True)["P-691"]
        self.assertTrue(card.present["HC"]["note"].startswith("n/a"))


if __name__ == "__main__":
    unittest.main()
