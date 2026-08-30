import { newId, utcNow } from './canonical.mjs';
import { findExactActiveCoverage } from './coverage.mjs';
import { finalizePacket } from './packet.mjs';

const REQUIRED_SCOPE = ['sport_family', 'competition_id', 'market_family', 'analysis_mode', 'forecast_state'];
const REQUIRED_CONTRACT = [
  'event_id', 'event_start_utc', 'ruleset_id', 'market_id', 'settlement_convention_id', 'horizon_bucket_id',
  'selection_mode',
];

function provided(value) {
  return value !== null && value !== undefined && String(value).trim() !== '' && !String(value).includes('REPLACE_');
}

function plusMinutes(iso, minutes) {
  return new Date(Date.parse(iso) + minutes * 60_000).toISOString();
}

function activeContractExists(contracts, input) {
  return contracts.some((contract) => contract.status === 'ACTIVE'
    && contract.competition_id === input.competition_id
    && contract.ruleset_id === input.ruleset_id
    && contract.settlement_convention_id === input.settlement_convention_id
    && contract.market_family === input.market_family
    && contract.forecast_state === input.forecast_state);
}

export function createInitialDecisionPacket(input, { controls, coverageRows, now = utcNow() }) {
  if (!provided(input.raw_request_text) || !provided(input.primary_question_text) || !provided(input.created_by)) {
    throw new Error('raw_request_text, primary_question_text and created_by must be verbatim/non-placeholder values');
  }
  const requestId = input.request_id ?? newId('REQ');
  const primaryQuestionId = input.primary_question_id ?? newId('QUESTION');
  const forecastSeriesId = input.forecast_series_id ?? newId('SERIES');
  const snapshotId = input.snapshot_id ?? newId('SNAP');
  const missingScope = REQUIRED_SCOPE.filter((field) => !provided(input[field]));
  const modeInvalid = !provided(input.analysis_mode) || !controls.vocabularies.analysis_mode.has(input.analysis_mode)
    || !provided(input.forecast_state) || !controls.vocabularies.forecast_state.has(input.forecast_state);
  const activeCoverage = missingScope.length === 0 ? findExactActiveCoverage(coverageRows, input, Date.parse(now)) : null;
  const missingContract = REQUIRED_CONTRACT.filter((field) => !provided(input[field]));
  const contractRegistered = missingContract.length === 0 && activeContractExists(controls.contracts, input);

  let decision = 'PASS';
  let passReason = 'SYSTEM_NOT_READY';
  let watchReason = null;
  let watchExpires = null;
  let missingPrerequisites = [];
  let dataQualityGrade = 'D';
  let primaryFailedGate = null;

  if (input.user_cancelled === true) {
    passReason = 'USER_CANCELLED';
    missingPrerequisites = ['request cancelled before analysis'];
  } else if (modeInvalid) {
    passReason = 'MODE_UNRESOLVED';
    missingPrerequisites = ['valid analysis_mode and forecast_state'];
  } else if (missingScope.length > 0 || missingContract.length > 0) {
    passReason = 'CONTRACT_UNRESOLVED';
    missingPrerequisites = [
      ...(!provided(input.raw_request_text) ? ['raw_request_text'] : []),
      ...(!provided(input.primary_question_text) ? ['primary_question_text'] : []),
      ...missingScope,
      ...missingContract,
    ];
  } else if (!contractRegistered) {
    passReason = 'CONTRACT_UNRESOLVED';
    missingPrerequisites = ['exact ACTIVE ruleset and settlement contract'];
  } else if (!activeCoverage) {
    passReason = 'MODEL_UNAVAILABLE';
    missingPrerequisites = ['exact ACTIVE coverage row', 'ACTIVE fitted model and activation evidence'];
    dataQualityGrade = 'C';
  } else {
    decision = 'WATCH';
    passReason = null;
    watchReason = 'SOURCE_PACKET_AND_CANDIDATE_UNIVERSE_PENDING';
    watchExpires = input.watch_expires_utc ?? plusMinutes(now, 30);
    missingPrerequisites = ['approved point-in-time source packet', 'frozen candidate universe', 'model run and uncertainty artifact'];
    dataQualityGrade = 'C';
  }

  if (decision === 'PASS') {
    primaryFailedGate = {
      CONTRACT_UNRESOLVED: 'GATE-CONTRACT-001', MODE_UNRESOLVED: 'GATE-MODE-001', MODEL_UNAVAILABLE: 'GATE-MODEL-001',
      SYSTEM_NOT_READY: 'GATE-AUTH-001', USER_CANCELLED: 'GATE-CONTRACT-001',
    }[passReason] ?? 'GATE-AUTH-001';
  }

  const contractStatus = missingContract.length === 0 && contractRegistered ? 'RESOLVED' : 'UNRESOLVED';
  const priceStatus = input.analysis_mode === 'PRICE_ENABLED'
    ? (decision === 'PASS' ? 'PRICE_UNAVAILABLE' : 'PENDING') : 'NOT_REQUESTED';
  const packet = {
    schema_version: 'SPORTS_DECISION_PACKET_V1',
    request: {
      request_id: requestId,
      primary_question_id: primaryQuestionId,
      primary_question_text: input.primary_question_text,
      raw_request_text: input.raw_request_text,
      contract_status: contractStatus,
      request_timestamp_utc: input.request_timestamp_utc ?? now,
      forecast_series_id: forecastSeriesId,
      event_id: provided(input.event_id) ? input.event_id : null,
      sport_family: provided(input.sport_family) ? input.sport_family : null,
      competition_id: provided(input.competition_id) ? input.competition_id : null,
      season_id: provided(input.season_id) ? input.season_id : null,
      event_name: provided(input.event_name) ? input.event_name : null,
      venue: provided(input.venue) ? input.venue : null,
      event_start_utc: provided(input.event_start_utc) ? input.event_start_utc : null,
      ruleset_id: provided(input.ruleset_id) ? input.ruleset_id : null,
      market_id: provided(input.market_id) ? input.market_id : null,
      market_family: provided(input.market_family) ? input.market_family : null,
      selection: provided(input.selection) ? input.selection : null,
      line: input.line ?? null,
      settlement_convention_id: provided(input.settlement_convention_id) ? input.settlement_convention_id : null,
      analysis_mode: provided(input.analysis_mode) ? input.analysis_mode : null,
      forecast_state: provided(input.forecast_state) ? input.forecast_state : null,
      state_bucket_id: provided(input.state_bucket_id) ? input.state_bucket_id : null,
      horizon_bucket_id: provided(input.horizon_bucket_id) ? input.horizon_bucket_id : null,
      selection_mode: provided(input.selection_mode) ? input.selection_mode : null,
      candidate_universe_id: null,
      selection_policy_version: null,
      user_cancelled: input.user_cancelled === true,
      created_by: input.created_by ?? 'sportsctl',
    },
    decision_snapshot: {
      snapshot_id: snapshotId,
      request_id: requestId,
      forecast_series_id: forecastSeriesId,
      parent_snapshot_id: input.parent_snapshot_id ?? null,
      snapshot_sequence: input.snapshot_sequence ?? 1,
      frozen_at_utc: now,
      data_cutoff_utc: input.data_cutoff_utc ?? now,
      decision,
      pass_reason: passReason,
      watch_reason: watchReason,
      watch_expires_utc: watchExpires,
      price_evaluation_status: priceStatus,
      data_quality_grade: dataQualityGrade,
      source_packet_id: null,
      candidate_universe_id: null,
      missing_prerequisites: missingPrerequisites,
      primary_failed_gate: primaryFailedGate,
      gate_failure_evidence: decision === 'PASS' ? [{
        gate_id: primaryFailedGate,
        code: passReason,
        detail: missingPrerequisites.join('; '),
        evidence_refs: ['request', 'coverage_registry', 'contract_registry'],
      }] : [],
      research_note: input.research_note ?? null,
      snapshot_hash: '0'.repeat(64),
      created_by: input.created_by ?? 'sportsctl',
    },
    candidate_universe: null,
    source_packet: null,
    live_state: null,
    prediction: null,
    forecast_distributions: [],
    linked_market_relations: [],
    uncertainty_components: [],
    price_snapshot: null,
  };
  return finalizePacket(packet);
}
