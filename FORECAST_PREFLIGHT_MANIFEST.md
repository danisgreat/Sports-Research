# Forecast preflight manifest schema — 2026-09-21


Status: **ACTIVE companion to `prediction_preflight.py`** under METHOD **MDS-2026.09.19-v4.3** / CONTROLS **CR-2026.09.21-3**. This schema is a control artifact, not a fitted model.


A new forecast must produce a JSON manifest before normal issuance. The validator is fail-closed.


```json
{
  "sport": "baseball",
  "method_version": "MDS-2026.09.19-v4.3",
  "control_revision": "CR-2026.09.21-3",
  "cutoff_at": "2026-09-19T12:00:00+10:00",
  "distribution_frozen_at": "2026-09-19T12:05:00+10:00",
  "line_compared_at": "2026-09-19T12:06:00+10:00",
  "line_visible_to_model": false,
  "user_line_used_as_feature": false,
  "event_identity": {
    "venue_city": "Tokyo",
    "venue_country": "Japan",
    "venue_timezone": "Asia/Tokyo",
    "scheduled_local_at": "2026-09-19T18:00:00+09:00",
    "scheduled_melbourne_at": "2026-09-19T19:00:00+10:00",
    "melbourne_timezone": "Australia/Melbourne",
    "melbourne_tz_abbr": "AEST",
    "calendar_date_rollover": false,
    "event_state": "PREGAME",
    "state_checked_at": "2026-09-19T18:55:00+10:00"
  },
  "contract": {
    "target_id": "SPORT_PERIOD_MEASURE",
    "line": 8.5,
    "period": "full_game",
    "settlement_terms": "research endpoint"
  },
  "model_inputs": {
    "mechanism_feature_1": 0.0
  },
  "distribution": {
    "id": "dist-<forecast-id>",
    "hash": "sha256-of-frozen-distribution"
  },
  "evidence": [
    {
      "source_id": "stable-source-record-id",
      "provider": "field owner or admitted independent provider",
      "domain": "example.org",
      "source_class": "VALID_PRIMARY_FIELD_OWNER",
      "field_name": "starting_lineup",
      "field_owner": true,
      "upstream_lineage_id": "UPSTREAM-LINEAGE",
      "first_known_at": "2026-09-19T11:45:00+10:00",
      "retrieved_at": "2026-09-19T11:55:00+10:00",
      "freshness_status": "CURRENT",
      "critical": true
    }
  ]
}
```


## Admitted predictive source classes


- `VALID_PRIMARY_FIELD_OWNER`
- `VALID_PRIMARY_TEAM`
- `VALID_SECONDARY_INDEPENDENT`
- `HISTORICAL_STRUCTURED_CANDIDATE` only for non-live historical/model fields after normal source-card admission; it cannot establish a live critical state.


`DISCOVERY_ONLY`, any `PROHIBITED_*` class, unknown/unclassified classes and unknown lineage fail preflight.


## Critical timestamps


- `first_known_at <= cutoff_at`
- `retrieved_at <= distribution_frozen_at`
- `line_compared_at >= distribution_frozen_at`
- timestamps must be timezone-aware ISO-8601 strings.


## Critical-source rule


A critical dynamic field should come from its field owner. If it does not, at least two independent admitted upstream lineages are required. Shared mirrors of one upstream feed count once.


## Reserved model-input keys


The validator rejects market/contract/fantasy-derived keys such as requested/market/closing/opening line, odds/price/implied probability, market/betting consensus, line movement, fantasy/DFS projection, ownership or points. The model receives sporting features only.


## Output


`prediction_preflight.py manifest.json` returns exit code **0** only on PASS; **1** for blocking findings; **2** for malformed input/usage. `--json` emits machine-readable findings. A PASS proves governance compliance for the manifest, not forecast accuracy or calibration.


## CR-4 universal event-verification requirements (preserved under CR-2026.09.21-3)


A normal pregame manifest must satisfy all of the following:


- at least **three distinct admitted upstream source lineages** across `evidence`;
- at least one `VALID_PRIMARY_FIELD_OWNER` record with `field_owner=true`;
- at least one `VALID_SECONDARY_INDEPENDENT` lineage;
- `event_identity.venue_timezone` must be a valid IANA timezone;
- `scheduled_local_at` must match that venue timezone on the exact event date;
- `scheduled_melbourne_at` must be the same instant converted to `Australia/Melbourne`;
- `melbourne_tz_abbr` must match the exact-date Melbourne abbreviation (`AEST` or `AEDT`);
- `calendar_date_rollover` must correctly state whether the venue-local and Melbourne calendar dates differ;
- normal pregame issue requires `event_state` of `PREGAME` or `SCHEDULED`.


Search snippets/generated summaries do not count as predictive evidence or independent source lineages. Settlement uses the stricter three-source terminal-state rule in METHOD/CONTROLS and is not inferred from this pregame PASS.




## CR-2026.09.21-1 cricket source-state object (preserved under CR-2026.09.21-3)


Every manifest now includes a top-level `sport`. For `sport: "cricket"`, add:


```json
"cricket_conditions": {
  "toss_status": "VERIFIED",
  "toss_search_complete": true,
  "strip_status": "OBSERVED",
  "strip_search_complete": true,
  "venue_history_status": "COMPUTED",
  "automated_pitch_metadata_used_as_observation": false,
  "duplicate_pitch_lineages_counted_independently": false,
  "toss_decision_used_as_strip_report": false,
  "pre_or_post_toss": "POST_TOSS",
  "final_conditions_refresh_at": "2026-09-21T18:54:00+10:00"
}
```


Allowed toss states: `VERIFIED`, `NOT_VERIFIED_AFTER_SEARCH`, `NOT_YET_PUBLISHED`, `CONFLICTING`.


Allowed strip states: `OBSERVED`, `NOT_FOUND_AFTER_SEARCH`, `CONFLICTING`, `STALE_ONLY`.


Allowed venue-history states: `COMPUTED`, `INSUFFICIENT_VENUE_HISTORY`.


The validator blocks a cricket manifest that:
- omits the required toss/strip searches;
- relabels automated pitch metadata as an observed strip;
- counts duplicate/shared pitch-feed lineages independently;
- treats the captain's toss decision as the strip report;
- omits the final cricket conditions refresh timestamp.


An unknown toss or a genuinely unavailable same-format venue history is **not itself a universal no-forecast condition**. The sport rules control branching/evidence grade. This object proves that the missingness was represented honestly and that prohibited substitutions were not made.






## CR-2026.09.21-3 audit-precedence receipt


This revision does not change the preflight schema or predictive semantics. It records the all-sports historical-audit reconciliation in `AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md`: later verified corrections supersede incompatible older findings; redundant findings are not duplicated; rejected historical shortcuts remain non-operative. The source firewall, line quarantine, point-in-time, lineage, distribution-first, settlement, and cricket source-state controls are unchanged.