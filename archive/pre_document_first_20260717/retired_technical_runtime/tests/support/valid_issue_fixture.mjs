import { resolve } from 'node:path';

import { compareCanonicalStrings, hashObject } from '../../src/canonical.mjs';
import { finalizePacket, loadMachineControls } from '../../src/packet.mjs';
import { createInitialDecisionPacket } from '../../src/workflow.mjs';

const ROOT = resolve(import.meta.dirname, '..', '..');

export const FIXTURE_NOW = '2026-07-16T12:00:00.000Z';
export const FIXTURE_EVENT_START = '2026-07-17T09:00:00.000Z';

const hashes = Object.freeze({
  model: '1'.repeat(64),
  code: '2'.repeat(64),
  feature: '3'.repeat(64),
  raw: '4'.repeat(64),
  parser: '5'.repeat(64),
  test: '6'.repeat(64),
  shadow: '7'.repeat(64),
});

function activeControls() {
  const controls = loadMachineControls(ROOT.replaceAll('\\', '/'));
  controls.release = {
    schema_version: 'SPORTS_RELEASE_MANIFEST_V1',
    release_id: 'SYNTHETIC-OPERATIONAL-TEST-RELEASE',
    effective_at_utc: '2026-07-16T00:00:00.000Z',
    release_mode: 'OPERATIONAL',
    operational_status: 'OPERATIONAL_EXACT_SCOPES_ONLY',
    activation_authorized: true,
    expected_active_coverage_count: 1,
    expected_acceptance_requirement_count: 88,
    review_ticket_id: 'SYNTHETIC-TEST-REVIEW',
    reviewed_by: 'acceptance-test-reviewer',
    reviewed_at_utc: '2026-07-16T01:00:00.000Z',
    release_bundle_hash: '8'.repeat(64),
    current_truth: {
      active_models: 1,
      eligible_predictions: 0,
      authorized_numeric_forecasts: true,
      price_enabled_issue_supported: false,
      legacy_rows_eligible: false,
    },
  };
  controls.contracts = [{
    contract_id: 'CONTRACT_AFL_WINNER_V1',
    competition_id: 'AFL',
    ruleset_id: 'AFL_2026',
    settlement_convention_id: 'AFL_WINNER_REGULATION_V1',
    market_family: 'winner',
    forecast_state: 'PREGAME_CONFIRMED',
    status: 'ACTIVE',
    effective_from_utc: '2026-01-01T00:00:00.000Z',
    effective_to_utc: '2027-01-01T00:00:00.000Z',
    official_rules_source_id: 'AFL_LAWS',
    settlement_authority_source_id: 'AFL_FIXTURE',
    branch_definition_hash: 'b'.repeat(64),
    approved_by: 'fixture-contract-approver',
    approval_utc: '2026-07-01T00:00:00.000Z',
  }];
  controls.sourceMaps = [{
    source_map_id: 'SM_AFL_WINNER_V1',
    model_id: 'MODEL_AFL_WINNER',
    model_version: '1.0.0',
    sport_family: 'Australian football',
    competition_id: 'AFL',
    market_family: 'winner',
    forecast_state: 'PREGAME_CONFIRMED',
    horizon_bucket_id: 'T24H_TO_T0',
    fact_type: 'fixture',
    source_id: 'AFL_FIXTURE',
    required: 'TRUE',
    parser_id: 'SYNTHETIC_AFL_FIXTURE_PARSER',
    parser_version: '1.0.0',
    parser_hash: hashes.parser,
    max_observation_age_seconds: '86400',
    max_provider_lag_seconds: '3600',
    regression_test_report_id: 'PARSER_REPORT_AFL_V1',
    status: 'ACTIVE',
    approved_by: 'fixture-source-map-approver',
    approval_utc: '2026-07-01T00:00:00.000Z',
    expires_utc: '2027-01-01T00:00:00.000Z',
    map_hash: 'c'.repeat(64),
  }];
  controls.testEvaluations = [
    {
      test_evaluation_id: 'TEST_AFL_WINNER_V1',
      hypothesis_family_id: 'HF_AFL_WINNER_V1',
      model_id: 'MODEL_AFL_WINNER',
      model_version: '1.0.0',
      test_role: 'UNTOUCHED_TEST',
      start_utc: '2026-01-01T00:00:00.000Z',
      end_utc: '2026-03-01T00:00:00.000Z',
      event_manifest_hash: 'd'.repeat(64),
      test_status: 'SPENT',
      preregistered_rule_hash: 'e'.repeat(64),
      preregistered_at_utc: '2025-12-01T00:00:00.000Z',
      first_viewed_at_utc: '2026-03-02T00:00:00.000Z',
      viewed_by: 'fixture-test-viewer',
      independent_evaluator: 'fixture-independent-evaluator',
      effective_n: '100',
      decision_rule_passed: 'TRUE',
      results_artifact_hash: hashes.test,
    },
    {
      test_evaluation_id: 'SHADOW_AFL_WINNER_V1',
      hypothesis_family_id: 'HF_AFL_WINNER_V1',
      model_id: 'MODEL_AFL_WINNER',
      model_version: '1.0.0',
      test_role: 'PROSPECTIVE_SHADOW',
      start_utc: '2026-04-01T00:00:00.000Z',
      end_utc: '2026-06-01T00:00:00.000Z',
      event_manifest_hash: 'f'.repeat(64),
      test_status: 'SPENT',
      preregistered_rule_hash: 'a'.repeat(64),
      preregistered_at_utc: '2026-03-15T00:00:00.000Z',
      first_viewed_at_utc: '2026-06-02T00:00:00.000Z',
      viewed_by: 'fixture-shadow-viewer',
      independent_evaluator: 'fixture-independent-evaluator',
      effective_n: '80',
      decision_rule_passed: 'TRUE',
      results_artifact_hash: hashes.shadow,
    },
  ];
  controls.modelRegistry = [{
    model_id: 'MODEL_AFL_WINNER',
    model_version: '1.0.0',
    hypothesis_family_id: 'HF_AFL_WINNER_V1',
    status: 'ACTIVE',
    sport_family: 'Australian football',
    competition_scope: 'AFL',
    market_scope: 'winner',
    forecast_state: 'PREGAME_CONFIRMED',
    analysis_mode: 'RESEARCH_ONLY',
    owner: 'fixture-model-owner',
    approver: 'fixture-model-approver',
    change_ticket_id: 'SYNTHETIC-MODEL-CHANGE',
    approval_utc: '2026-07-01T00:00:00.000Z',
    expires_utc: '2027-01-01T00:00:00.000Z',
    data_manifest_hash: '0'.repeat(64),
    source_map_id: 'SM_AFL_WINNER_V1',
    test_report_id: 'TEST_AFL_WINNER_V1',
    shadow_report_id: 'SHADOW_AFL_WINNER_V1',
    model_artifact_hash: hashes.model,
    code_hash: hashes.code,
    calibration_artifact_hash: '9'.repeat(64),
  }];
  // The fixture models a hypothetical future release after every mandatory
  // acceptance item has executable evidence. The real workspace matrix keeps
  // its PARTIAL/NOT_IMPLEMENTED statuses and remains non-operational.
  controls.acceptanceTraceability = controls.acceptanceTraceability.map((row) => ({ ...row, status: 'COVERED' }));
  return controls;
}

function activeCoverage() {
  return [{
    coverage_id: 'COV_AFL_WINNER_V1',
    sport_family: 'Australian football',
    competition_scope: 'AFL',
    market_scope: 'winner',
    forecast_state: 'PREGAME_CONFIRMED',
    analysis_mode: 'RESEARCH_ONLY',
    status: 'ACTIVE',
    model_id: 'MODEL_AFL_WINNER',
    model_version: '1.0.0',
    source_map_id: 'SM_AFL_WINNER_V1',
    test_report_id: 'TEST_AFL_WINNER_V1',
    shadow_report_id: 'SHADOW_AFL_WINNER_V1',
    approved_by: 'fixture-approver',
    approval_utc: '2026-07-01T00:00:00.000Z',
    expires_utc: '2099-01-01T00:00:00.000Z',
    reason: 'synthetic test fixture only',
  }];
}

function initialInput() {
  return {
    request_id: 'REQ-VALID-ISSUE-1',
    primary_question_id: 'QUESTION-VALID-ISSUE-1',
    forecast_series_id: 'SERIES-VALID-ISSUE-1',
    snapshot_id: 'SNAP-VALID-ISSUE-1',
    raw_request_text: 'Forecast the AFL regulation winner for this synthetic test event.',
    primary_question_text: 'Will the synthetic home team win in regulation?',
    created_by: 'acceptance-test',
    request_timestamp_utc: FIXTURE_NOW,
    event_id: 'AFL:SYNTHETIC:1',
    sport_family: 'Australian football',
    competition_id: 'AFL',
    season_id: '2026',
    event_name: 'Synthetic Home v Synthetic Away',
    venue: 'Synthetic Ground',
    event_start_utc: FIXTURE_EVENT_START,
    ruleset_id: 'AFL_2026',
    market_id: 'AFL:SYNTHETIC:1:WINNER',
    market_family: 'winner',
    selection: 'SYNTHETIC_HOME',
    line: null,
    settlement_convention_id: 'AFL_WINNER_REGULATION_V1',
    analysis_mode: 'RESEARCH_ONLY',
    forecast_state: 'PREGAME_CONFIRMED',
    horizon_bucket_id: 'T24H_TO_T0',
    selection_mode: 'USER_SUPPLIED',
  };
}

export function makeValidIssueFixture() {
  const controls = activeControls();
  const coverageRows = activeCoverage();
  const packet = createInitialDecisionPacket(initialInput(), { controls, coverageRows, now: FIXTURE_NOW });

  const candidateUniverseId = 'UNIVERSE-VALID-ISSUE-1';
  const candidate = {
    candidate_id: 'CANDIDATE-HOME',
    candidate_universe_id: candidateUniverseId,
    market_id: packet.request.market_id,
    selection: 'SYNTHETIC_HOME',
    line: null,
    market_outcome_space_id: 'OUTCOME-SPACE-AFL-WINNER-V1',
    forecast_distribution_id: 'DISTRIBUTION-WINNER-1',
    relationship_type: 'NONE',
    related_candidate_ids: [],
    complement_group_id: null,
    overlap_group_id: null,
    is_primary_question: true,
    inclusion_source: 'USER_PRIMARY_QUESTION',
    selected_for_issue: true,
    candidate_status: 'SELECTED',
    rejection_reason: null,
    selection_score: null,
    probability_generation_status: 'GENERATED',
    candidate_frozen_at_utc: FIXTURE_NOW,
    winning_state_ids: ['STATE-HOME-WIN'],
  };
  const enumerationManifestHash = hashObject({
    manifest_version: 'SYNTHETIC_ENUMERATION_MANIFEST_V1',
    request_id: packet.request.request_id,
    candidate_ids: [candidate.candidate_id],
  });
  const universeHashMaterial = {
    candidate_universe_id: candidateUniverseId,
    request_id: packet.request.request_id,
    primary_question_id: packet.request.primary_question_id,
    universe_definition_version: 'SYNTHETIC_UNIVERSE_V1',
    selection_mode: 'USER_SUPPLIED',
    selection_policy_version: 'SYNTHETIC_SELECTION_POLICY_V1',
    known_at_utc: FIXTURE_NOW,
    frozen_at_utc: FIXTURE_NOW,
    enumeration_manifest_hash: enumerationManifestHash,
    candidate_count: 1,
    candidates: [candidate],
  };

  packet.request.candidate_universe_id = candidateUniverseId;
  packet.request.selection_policy_version = 'SYNTHETIC_SELECTION_POLICY_V1';
  packet.decision_snapshot.decision = 'ISSUE';
  packet.decision_snapshot.pass_reason = null;
  packet.decision_snapshot.watch_reason = null;
  packet.decision_snapshot.watch_expires_utc = null;
  packet.decision_snapshot.price_evaluation_status = 'NOT_REQUESTED';
  packet.decision_snapshot.data_quality_grade = 'B';
  packet.decision_snapshot.source_packet_id = 'SOURCE-PACKET-VALID-ISSUE-1';
  packet.decision_snapshot.candidate_universe_id = candidateUniverseId;
  packet.decision_snapshot.missing_prerequisites = [];
  packet.decision_snapshot.primary_failed_gate = null;
  packet.decision_snapshot.gate_failure_evidence = [];

  packet.candidate_universe = {
    ...universeHashMaterial,
    universe_hash: hashObject(universeHashMaterial),
  };
  const sourceObservation = {
      source_observation_id: 'OBS-AFL-FIXTURE-1',
      source_packet_id: 'SOURCE-PACKET-VALID-ISSUE-1',
      source_map_id: 'SM_AFL_WINNER_V1',
      source_id: 'AFL_FIXTURE',
      source_release_id: 'AFL-FIXTURE-SYNTHETIC-20260716',
      requested_url: 'https://www.afl.com.au/fixture',
      final_url: 'https://www.afl.com.au/fixture',
      authority_class: 'A0',
      fact_type: 'fixture',
      known_at_utc: '2026-07-16T11:50:00.000Z',
      fetched_at_utc: '2026-07-16T11:55:00.000Z',
      transport_type: 'HTML',
      retrieval_status: 'SUCCESS',
      freshness_status: 'FRESH',
      verification_status: 'VERIFIED',
      extracted_value: 'Synthetic event identity and scheduled start',
      raw_hash: hashes.raw,
      extractor_version: 'SYNTHETIC_EXTRACTOR_V1',
      historical_reconstruction: false,
    };
  const sourcePacketHashMaterial = {
    source_packet_id: 'SOURCE-PACKET-VALID-ISSUE-1',
    request_id: packet.request.request_id,
    snapshot_id: packet.decision_snapshot.snapshot_id,
    source_map_id: 'SM_AFL_WINNER_V1',
    frozen_at_utc: FIXTURE_NOW,
    observations: [sourceObservation],
  };
  packet.source_packet = {
    ...sourcePacketHashMaterial,
    source_packet_hash: hashObject(sourcePacketHashMaterial),
  };
  packet.prediction = {
    prediction_id: 'PREDICTION-VALID-ISSUE-1',
    snapshot_id: packet.decision_snapshot.snapshot_id,
    candidate_universe_id: candidateUniverseId,
    source_packet_id: packet.source_packet.source_packet_id,
    run_at_utc: FIXTURE_NOW,
    selected_candidate_id: candidate.candidate_id,
    forecast_distribution_id: 'DISTRIBUTION-WINNER-1',
    model_id: 'MODEL_AFL_WINNER',
    model_version: '1.0.0',
    coverage_id: 'COV_AFL_WINNER_V1',
    data_version: 'SYNTHETIC_DATA_V1',
    feature_version: 'SYNTHETIC_FEATURES_V1',
    code_commit_or_hash: hashes.code,
    model_artifact_hash: hashes.model,
    feature_snapshot_hash: hashes.feature,
    data_manifest_hash: controls.modelRegistry[0].data_manifest_hash,
    calibration_artifact_hash: controls.modelRegistry[0].calibration_artifact_hash,
    model_probability_raw: 0.60,
    decision_probability: 0.60,
    calibration_evidence_id: 'CALIBRATION-SYNTHETIC-V1',
    calibration_status: 'IDENTITY_JUSTIFIED',
    baseline_id: 'BASELINE-HISTORICAL-RATE',
    baseline_version: '1.0.0',
    baseline_probability: 0.50,
    baseline_probability_delta: 0.10,
    uncertainty_set_id: 'UNCERTAINTY-SYNTHETIC-V1',
    invalidation_triggers: ['source revision', 'event postponement'],
    market_price_snapshot_id: null,
    market_edge: null,
    expected_return: null,
    ev_lower: null,
    ev_upper: null,
    stake: null,
    realized_yield: null,
    realized_pnl: null,
    clv: null,
  };
  const states = [
    {
      settlement_state_id: 'STATE-HOME-WIN',
      forecast_distribution_id: 'DISTRIBUTION-WINNER-1',
      market_outcome_space_id: 'OUTCOME-SPACE-AFL-WINNER-V1',
      state_label: 'Synthetic home wins in regulation',
      branch_type: 'WIN',
      is_structural: false,
      raw_probability: 0.60,
      decision_probability: 0.60,
      baseline_probability: 0.50,
    },
    {
      settlement_state_id: 'STATE-HOME-LOSS',
      forecast_distribution_id: 'DISTRIBUTION-WINNER-1',
      market_outcome_space_id: 'OUTCOME-SPACE-AFL-WINNER-V1',
      state_label: 'Synthetic home does not win in regulation',
      branch_type: 'LOSS',
      is_structural: false,
      raw_probability: 0.40,
      decision_probability: 0.40,
      baseline_probability: 0.50,
    },
  ];
  const distributionHashMaterial = {
    forecast_distribution_id: 'DISTRIBUTION-WINNER-1',
    market_outcome_space_id: 'OUTCOME-SPACE-AFL-WINNER-V1',
    joint_distribution_id: null,
    calibration_evidence_id: 'CALIBRATION-SYNTHETIC-V1',
    frozen_at_utc: FIXTURE_NOW,
    states: [...states].sort((left, right) => compareCanonicalStrings(left.settlement_state_id, right.settlement_state_id)),
  };
  packet.forecast_distributions = [{
    ...distributionHashMaterial,
    distribution_hash: hashObject(distributionHashMaterial),
  }];
  packet.linked_market_relations = [];
  packet.uncertainty_components = [
    {
      uncertainty_component_id: 'UNC-PARAMETER', uncertainty_set_id: 'UNCERTAINTY-SYNTHETIC-V1',
      prediction_id: 'PREDICTION-VALID-ISSUE-1', uncertainty_type: 'PARAMETER', uncertainty_status: 'QUANTIFIED',
      estimand: 'selected candidate win probability', method_version: 'SYNTHETIC_BOOTSTRAP_V1', level: 0.95,
      lower: 0.57, upper: 0.63, evidence_artifact_hash: '1'.repeat(64), material: true, decision_robust: true,
    },
    {
      uncertainty_component_id: 'UNC-INPUT', uncertainty_set_id: 'UNCERTAINTY-SYNTHETIC-V1',
      prediction_id: 'PREDICTION-VALID-ISSUE-1', uncertainty_type: 'INPUT_SCENARIO', uncertainty_status: 'QUANTIFIED',
      estimand: 'selected candidate win probability', method_version: 'SYNTHETIC_SCENARIOS_V1', level: 0.95,
      lower: 0.56, upper: 0.64, evidence_artifact_hash: '2'.repeat(64), material: true, decision_robust: true,
    },
    {
      uncertainty_component_id: 'UNC-STRUCTURAL', uncertainty_set_id: 'UNCERTAINTY-SYNTHETIC-V1',
      prediction_id: 'PREDICTION-VALID-ISSUE-1', uncertainty_type: 'STRUCTURAL_MODEL', uncertainty_status: 'NOT_MATERIAL_WITH_EVIDENCE',
      estimand: 'selected candidate win probability', method_version: 'SYNTHETIC_MODEL_COMPARISON_V1',
      evidence_artifact_hash: '3'.repeat(64), material: false, decision_robust: true,
    },
    {
      uncertainty_component_id: 'UNC-CALIBRATION', uncertainty_set_id: 'UNCERTAINTY-SYNTHETIC-V1',
      prediction_id: 'PREDICTION-VALID-ISSUE-1', uncertainty_type: 'CALIBRATION', uncertainty_status: 'QUANTIFIED',
      estimand: 'selected candidate win probability', method_version: 'SYNTHETIC_CALIBRATION_V1', level: 0.95,
      lower: 0.55, upper: 0.65, evidence_artifact_hash: '4'.repeat(64), material: true, decision_robust: true,
    },
    {
      uncertainty_component_id: 'UNC-TOTAL', uncertainty_set_id: 'UNCERTAINTY-SYNTHETIC-V1',
      prediction_id: 'PREDICTION-VALID-ISSUE-1', uncertainty_type: 'TOTAL_PROBABILITY', uncertainty_status: 'QUANTIFIED',
      estimand: 'selected candidate win probability', method_version: 'SYNTHETIC_TOTAL_UNCERTAINTY_V1', level: 0.95,
      lower: 0.54, upper: 0.66, evidence_artifact_hash: '5'.repeat(64), material: true, decision_robust: true,
    },
  ];
  packet.price_snapshot = null;

  const controlHashes = {
    release: hashObject(controls.release),
    contracts: hashObject(controls.contracts),
    source_maps: hashObject(controls.sourceMaps),
    test_evaluations: hashObject(controls.testEvaluations),
    model_registry: hashObject(controls.modelRegistry),
    coverage_registry: hashObject(coverageRows),
  };

  return {
    packet: finalizePacket(packet),
    context: {
      controls,
      coverageRows,
      controlHashes,
      controlBundleHash: hashObject(controlHashes),
    },
  };
}

export function mutateAndFinalize(packet, mutator) {
  const copy = structuredClone(packet);
  mutator(copy);
  return finalizePacket(copy);
}

export function gateStatus(report, gateId) {
  return report.gate_results.find((row) => row.gate_id === gateId)?.status;
}
