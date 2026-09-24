import copy
import unittest


from prediction_preflight import validate




def valid_manifest():
    evidence = []
    specs = [
        ("league-1", "League", "VALID_PRIMARY_FIELD_OWNER", True, "LEAGUE_API"),
        ("team-1", "Team", "VALID_PRIMARY_TEAM", False, "TEAM_RELEASE"),
        ("wire-1", "Reuters", "VALID_SECONDARY_INDEPENDENT", False, "REUTERS"),
    ]
    for source_id, provider, source_class, owner, lineage in specs:
        evidence.append({
            "source_id": source_id,
            "provider": provider,
            "domain": "example.org",
            "source_class": source_class,
            "field_name": "event_identity",
            "field_owner": owner,
            "upstream_lineage_id": lineage,
            "first_known_at": "2026-09-19T11:40:00+10:00",
            "retrieved_at": "2026-09-19T11:50:00+10:00",
            "freshness_status": "CURRENT",
            "critical": False,
        })
    return {
        "sport": "baseball",
        "method_version": "MDS-2026.09.19-v4.3",
        "control_revision": "CR-2026.09.21-3",
        "cutoff_at": "2026-09-19T12:00:00+10:00",
        "distribution_frozen_at": "2026-09-19T12:05:00+10:00",
        "line_compared_at": "2026-09-19T12:06:00+10:00",
        "line_visible_to_model": False,
        "user_line_used_as_feature": False,
        "event_identity": {
            "venue_city": "Tokyo",
            "venue_country": "Japan",
            "venue_timezone": "Asia/Tokyo",
            "scheduled_local_at": "2026-09-19T11:00:00+09:00",
            "scheduled_melbourne_at": "2026-09-19T12:00:00+10:00",
            "melbourne_timezone": "Australia/Melbourne",
            "melbourne_tz_abbr": "AEST",
            "calendar_date_rollover": False,
            "event_state": "PREGAME",
            "state_checked_at": "2026-09-19T11:50:00+10:00",
        },
        "contract": {"target_id": "TEST_FULL_GAME_TOTAL", "line": 8.5},
        "model_inputs": {"sport_feature": 1.0},
        "distribution": {"id": "dist-001", "hash": "abc123"},
        "evidence": evidence,
    }




class PreflightTests(unittest.TestCase):
    def codes(self, m):
        return {f.code for f in validate(m)}


    def test_valid_manifest_passes(self):
        self.assertEqual(validate(valid_manifest()), [])


    def test_fewer_than_three_lineages_blocked(self):
        m = valid_manifest()
        m["evidence"] = m["evidence"][:2]
        self.assertIn("PF-SOURCE-COUNT-3", self.codes(m))


    def test_duplicate_lineage_does_not_count(self):
        m = valid_manifest()
        m["evidence"][2]["upstream_lineage_id"] = "TEAM_RELEASE"
        self.assertIn("PF-SOURCE-COUNT-3", self.codes(m))


    def test_missing_field_owner_blocked(self):
        m = valid_manifest()
        m["evidence"][0]["field_owner"] = False
        m["evidence"][0]["source_class"] = "VALID_PRIMARY_TEAM"
        self.assertIn("PF-SOURCE-MIX-FIELD-OWNER", self.codes(m))


    def test_missing_independent_secondary_blocked(self):
        m = valid_manifest()
        m["evidence"][2]["source_class"] = "VALID_PRIMARY_TEAM"
        self.assertIn("PF-SOURCE-MIX-INDEPENDENT", self.codes(m))


    def test_wrong_melbourne_conversion_blocked(self):
        m = valid_manifest()
        m["event_identity"]["scheduled_melbourne_at"] = "2026-09-19T13:00:00+10:00"
        self.assertIn("PF-MELBOURNE-CONVERSION", self.codes(m))


    def test_wrong_melbourne_abbreviation_blocked(self):
        m = valid_manifest()
        m["event_identity"]["melbourne_tz_abbr"] = "AEDT"
        self.assertIn("PF-MELBOURNE-ABBR", self.codes(m))


    def test_bad_rollover_flag_blocked(self):
        m = valid_manifest()
        m["event_identity"]["calendar_date_rollover"] = True
        self.assertIn("PF-DATE-ROLLOVER", self.codes(m))


    def test_live_state_blocked_for_pregame_issue(self):
        m = valid_manifest()
        m["event_identity"]["event_state"] = "LIVE"
        self.assertIn("PF-EVENT-STATE", self.codes(m))


    def test_bad_venue_timezone_blocked(self):
        m = valid_manifest()
        m["event_identity"]["venue_timezone"] = "Not/A_Timezone"
        self.assertIn("PF-TIMEZONE-INVALID", self.codes(m))


    def test_fantasy_source_blocked(self):
        m = valid_manifest()
        m["evidence"][2]["provider"] = "RotoWire"
        self.assertIn("PF-1-SOURCE-TOKEN", self.codes(m))


    def test_post_cutoff_fact_blocked(self):
        m = valid_manifest()
        m["evidence"][0]["first_known_at"] = "2026-09-19T12:01:00+10:00"
        self.assertIn("PF-3-POST-CUTOFF", self.codes(m))


    def test_line_visibility_blocked(self):
        m = valid_manifest()
        m["line_visible_to_model"] = True
        self.assertIn("PF-2-LINE-VISIBILITY", self.codes(m))


    def test_market_input_key_blocked(self):
        m = valid_manifest()
        m["model_inputs"]["market_line"] = 8.5
        self.assertIn("PF-2-LINE-MARKET-INPUT", self.codes(m))


    def test_version_mismatch_blocked(self):
        m = valid_manifest()
        m["method_version"] = "MDS-2026.09.19-v4.2"
        self.assertIn("PF-7-METHOD-VERSION", self.codes(m))




    def test_missing_sport_blocked(self):
        m = valid_manifest()
        del m["sport"]
        self.assertIn("PF-SPORT", self.codes(m))


    def test_cricket_conditions_required(self):
        m = valid_manifest()
        m["sport"] = "cricket"
        self.assertIn("PF-CR-CONDITIONS", self.codes(m))


    def test_valid_cricket_conditions_pass(self):
        m = valid_manifest()
        m["sport"] = "cricket"
        m["cricket_conditions"] = {
            "toss_status": "NOT_VERIFIED_AFTER_SEARCH",
            "toss_search_complete": True,
            "strip_status": "NOT_FOUND_AFTER_SEARCH",
            "strip_search_complete": True,
            "venue_history_status": "INSUFFICIENT_VENUE_HISTORY",
            "automated_pitch_metadata_used_as_observation": False,
            "duplicate_pitch_lineages_counted_independently": False,
            "toss_decision_used_as_strip_report": False,
            "pre_or_post_toss": "PRE_TOSS",
            "final_conditions_refresh_at": "2026-09-19T12:04:00+10:00",
        }
        self.assertEqual(validate(m), [])


    def test_cricket_automated_pitch_metadata_as_observation_blocked(self):
        m = valid_manifest()
        m["sport"] = "cricket"
        m["cricket_conditions"] = {
            "toss_status": "VERIFIED",
            "toss_search_complete": True,
            "strip_status": "OBSERVED",
            "strip_search_complete": True,
            "venue_history_status": "COMPUTED",
            "automated_pitch_metadata_used_as_observation": True,
            "duplicate_pitch_lineages_counted_independently": False,
            "toss_decision_used_as_strip_report": False,
            "pre_or_post_toss": "POST_TOSS",
            "final_conditions_refresh_at": "2026-09-19T12:04:00+10:00",
        }
        self.assertIn("PF-CR-AUTO-PITCH", self.codes(m))


    def test_cricket_duplicate_pitch_lineage_blocked(self):
        m = valid_manifest()
        m["sport"] = "cricket"
        m["cricket_conditions"] = {
            "toss_status": "VERIFIED",
            "toss_search_complete": True,
            "strip_status": "OBSERVED",
            "strip_search_complete": True,
            "venue_history_status": "COMPUTED",
            "automated_pitch_metadata_used_as_observation": False,
            "duplicate_pitch_lineages_counted_independently": True,
            "toss_decision_used_as_strip_report": False,
            "pre_or_post_toss": "POST_TOSS",
            "final_conditions_refresh_at": "2026-09-19T12:04:00+10:00",
        }
        self.assertIn("PF-CR-LINEAGE-FINGERPRINT", self.codes(m))



    # --- 2026-09-24(f) / 2026-09-25 participant-state object ---------------------------

    def _receipt(self, outlet, published="2026-09-19T11:30:00+10:00"):
        return {"outlet": outlet, "reporter": "Named Reporter", "published_at": published,
                "quote": "Starting lineup: A, B, C, D, E"}

    def test_manifest_without_participants_still_passes(self):
        m = valid_manifest()
        self.assertNotIn("PF-LINEUP-STATE", self.codes(m))
        self.assertEqual([f for f in validate(m) if f.level == "BLOCK"], [])

    def test_projected_beat_verified_without_receipt_blocked(self):
        m = valid_manifest()
        m["participants"] = {"lineup_state": "PROJECTED_BEAT_VERIFIED"}
        self.assertIn("PF-LINEUP-RECEIPT", self.codes(m))

    def test_projected_beat_verified_with_two_outlet_receipt_passes(self):
        m = valid_manifest()
        m["participants"] = {"lineup_state": "PROJECTED_BEAT_VERIFIED",
                             "official_lineup_published_before_freeze": False,
                             "s1r2_receipt": [self._receipt("Outlet One"), self._receipt("Outlet Two")]}
        self.assertFalse({c for c in self.codes(m) if c.startswith("PF-LINEUP")})

    def test_single_outlet_receipt_blocked(self):
        m = valid_manifest()
        m["participants"] = {"lineup_state": "PROJECTED_BEAT_VERIFIED",
                             "s1r2_receipt": [self._receipt("Outlet One"), self._receipt("outlet one")]}
        self.assertIn("PF-LINEUP-RECEIPT", self.codes(m))

    def test_receipt_published_after_freeze_blocked(self):
        m = valid_manifest()
        m["participants"] = {"lineup_state": "PROJECTED_BEAT_VERIFIED",
                             "s1r2_receipt": [self._receipt("Outlet One"),
                                              self._receipt("Outlet Two", "2026-09-19T12:30:00+10:00")]}
        self.assertIn("PF-LINEUP-RECEIPT", self.codes(m))

    def test_official_lineup_precedence_blocks_projected_state(self):
        m = valid_manifest()
        m["participants"] = {"lineup_state": "PROJECTED_BEAT_VERIFIED",
                             "official_lineup_published_before_freeze": True,
                             "s1r2_receipt": [self._receipt("Outlet One"), self._receipt("Outlet Two")]}
        self.assertIn("PF-LINEUP-OFFICIAL-PRECEDENCE", self.codes(m))

    def test_confirmed_official_after_freeze_blocked(self):
        m = valid_manifest()
        m["participants"] = {"lineup_state": "CONFIRMED_OFFICIAL",
                             "official_lineup_published_before_freeze": True,
                             "official_lineup_retrieved_at": "2026-09-19T12:10:00+10:00"}
        self.assertIn("PF-LINEUP-TIME", self.codes(m))

    def test_confirmed_official_before_freeze_passes(self):
        m = valid_manifest()
        m["participants"] = {"lineup_state": "CONFIRMED_OFFICIAL",
                             "official_lineup_published_before_freeze": True,
                             "official_lineup_retrieved_at": "2026-09-19T11:55:00+10:00"}
        self.assertFalse({c for c in self.codes(m) if c.startswith("PF-LINEUP")})

    def test_unknown_lineup_state_blocked(self):
        m = valid_manifest()
        m["participants"] = {"lineup_state": "CONFIRMED"}
        self.assertIn("PF-LINEUP-STATE", self.codes(m))



if __name__ == "__main__":
    unittest.main()