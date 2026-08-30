import { readFileSync } from 'node:fs';
import { compareCanonicalStrings, computeSnapshotHash, hashObject, isSha256, parseUtc, readJson } from './canonical.mjs';
import { findExactActiveCoverage } from './coverage.mjs';
import { parseCsv } from './csv.mjs';
import { validateLinkedMarketCoherence, validateProbabilityVector } from './scoring.mjs';
import { validateReleaseManifest } from './release.mjs';
import { validateRuntimeControls } from './controls.mjs';
import Ajv2020 from 'ajv/dist/2020.js';

export const DECISION_PACKET_VERSION = 'SPORTS_DECISION_PACKET_V1';

const FORECAST_LIKE_NOTE = /(?:\bprobab(?:ility|le)\b|\bconfidence\b|\bedge\b|\bexpected\s+value\b|\bEV\b|\bstak(?:e|ing)\b|\bvalue\s+bet\b|\b\d+(?:\.\d+)?\s*%)/i;
const REQUIRED_ISSUE_REQUEST_FIELDS = [
  'event_id', 'sport_family', 'competition_id', 'event_start_utc', 'ruleset_id', 'market_id', 'market_family',
  'settlement_convention_id', 'analysis_mode', 'forecast_state', 'horizon_bucket_id', 'selection_mode',
  'candidate_universe_id', 'selection_policy_version',
];
// Fields that must be known before the workflow can distinguish a missing
// contract from a missing model. Candidate-universe and selection-policy
// identifiers are created later, so they must not make MODEL_UNAVAILABLE
// impossible for an otherwise fully scoped initial request.
const REQUIRED_PREMODEL_REQUEST_FIELDS = [
  'event_id', 'sport_family', 'competition_id', 'event_start_utc', 'ruleset_id', 'market_id', 'market_family',
  'settlement_convention_id', 'analysis_mode', 'forecast_state', 'horizon_bucket_id', 'selection_mode',
];
const REQUIRED_PREDICTION_FIELDS = [
  'prediction_id', 'snapshot_id', 'selected_candidate_id', 'forecast_distribution_id', 'model_id', 'model_version',
  'coverage_id', 'data_version', 'feature_version', 'code_commit_or_hash', 'model_artifact_hash',
  'feature_snapshot_hash', 'model_probability_raw', 'decision_probability', 'calibration_evidence_id',
  'baseline_id', 'baseline_version', 'baseline_probability', 'baseline_probability_delta', 'uncertainty_set_id',
  'invalidation_triggers', 'candidate_universe_id', 'source_packet_id', 'run_at_utc', 'calibration_status',
  'data_manifest_hash', 'calibration_artifact_hash',
];
const UNCERTAINTY_ASSESSMENTS = ['PARAMETER', 'INPUT_SCENARIO', 'STRUCTURAL_MODEL', 'CALIBRATION', 'TOTAL_PROBABILITY'];
const REQUEST_FIELDS = new Set([
  'request_id', 'primary_question_id', 'primary_question_text', 'raw_request_text', 'contract_status', 'request_timestamp_utc',
  'forecast_series_id', 'event_id', 'sport_family', 'competition_id', 'season_id', 'event_name', 'venue', 'event_start_utc',
  'ruleset_id', 'market_id', 'market_family', 'selection', 'line', 'settlement_convention_id', 'analysis_mode', 'forecast_state',
  'state_bucket_id', 'horizon_bucket_id', 'selection_mode', 'candidate_universe_id', 'selection_policy_version', 'user_cancelled', 'created_by',
]);
const SNAPSHOT_FIELDS = new Set([
  'snapshot_id', 'request_id', 'forecast_series_id', 'parent_snapshot_id', 'snapshot_sequence', 'frozen_at_utc', 'data_cutoff_utc',
  'decision', 'pass_reason', 'watch_reason', 'watch_expires_utc', 'price_evaluation_status', 'data_quality_grade', 'source_packet_id',
  'candidate_universe_id', 'missing_prerequisites', 'primary_failed_gate', 'gate_failure_evidence', 'research_note', 'snapshot_hash', 'created_by',
]);
const UNIVERSE_FIELDS = new Set([
  'candidate_universe_id', 'request_id', 'primary_question_id', 'universe_definition_version', 'selection_mode',
  'selection_policy_version', 'known_at_utc', 'frozen_at_utc', 'enumeration_manifest_hash', 'candidate_count',
  'universe_hash', 'candidates',
]);
const CANDIDATE_FIELDS = new Set([
  'candidate_id', 'candidate_universe_id', 'market_id', 'selection', 'line', 'market_outcome_space_id',
  'forecast_distribution_id', 'winning_state_ids', 'relationship_type', 'related_candidate_ids', 'complement_group_id',
  'overlap_group_id', 'is_primary_question', 'inclusion_source', 'candidate_status', 'rejection_reason', 'selection_score',
  'probability_generation_status', 'selected_for_issue', 'candidate_frozen_at_utc',
]);
const SOURCE_PACKET_FIELDS = new Set([
  'source_packet_id', 'request_id', 'snapshot_id', 'source_map_id', 'frozen_at_utc', 'observations', 'source_packet_hash',
]);
const SOURCE_OBSERVATION_FIELDS = new Set([
  'source_observation_id', 'source_packet_id', 'source_map_id', 'source_id', 'source_release_id', 'requested_url', 'final_url',
  'authority_class', 'fact_type', 'published_at_utc', 'modified_at_utc', 'first_seen_at_utc', 'known_at_utc', 'fetched_at_utc',
  'data_through_utc', 'applies_to_time', 'effective_from_utc', 'effective_to_utc', 'transport_type', 'retrieval_status',
  'freshness_status', 'verification_status', 'extracted_value', 'definition_or_unit', 'raw_snapshot_path', 'raw_hash',
  'extractor_version', 'conflict_set_id', 'supersedes_observation_id', 'historical_reconstruction', 'as_of_evidence_hash',
  'as_of_version_id',
]);
const PREDICTION_FIELDS = new Set([
  ...REQUIRED_PREDICTION_FIELDS, 'market_price_snapshot_id', 'market_edge', 'expected_return', 'ev_lower', 'ev_upper',
  'stake', 'realized_yield', 'realized_pnl', 'clv',
]);
const DISTRIBUTION_FIELDS = new Set([
  'forecast_distribution_id', 'market_outcome_space_id', 'joint_distribution_id', 'calibration_evidence_id',
  'frozen_at_utc', 'states', 'distribution_hash',
]);
const STATE_FIELDS = new Set([
  'settlement_state_id', 'forecast_distribution_id', 'market_outcome_space_id', 'state_label', 'branch_type',
  'raw_probability', 'decision_probability', 'baseline_probability', 'is_structural',
]);
const UNCERTAINTY_FIELDS = new Set([
  'uncertainty_component_id', 'uncertainty_set_id', 'prediction_id', 'uncertainty_type', 'uncertainty_status',
  'estimand', 'method_version', 'level', 'lower', 'upper', 'standard_error', 'scenario_or_model_weights',
  'evidence_artifact_hash', 'material', 'decision_robust',
]);
const PASS_REASON_GATE = {
  MODEL_UNAVAILABLE: 'GATE-MODEL-001', CONTRACT_UNRESOLVED: 'GATE-CONTRACT-001', MODE_UNRESOLVED: 'GATE-MODE-001',
  CUTOFF_FAILURE: 'GATE-CUTOFF-001', SOURCE_FAILURE: 'GATE-SOURCE-001', UNIVERSE_NOT_FROZEN: 'GATE-UNIVERSE-001',
  OUT_OF_SCOPE: 'GATE-MODEL-001', PROBABILITY_INVALID: 'GATE-PROB-001', UNCERTAINTY_UNRESOLVED: 'GATE-UNCERTAINTY-001',
  SYSTEM_NOT_READY: 'GATE-AUTH-001', USER_CANCELLED: 'GATE-CONTRACT-001', OTHER_DOCUMENTED: 'GATE-AUTH-001',
};
const TEMPLATE_SENTINEL = /^(?:REPLACE(?:_|\b)|UNRESOLVED$)/i;

function gate(id, passed, detail, applicability = true) {
  return {
    gate_id: id,
    status: applicability ? (passed ? 'PASS' : 'FAIL') : 'NOT_APPLICABLE',
    detail,
  };
}

function nonBlank(value) {
  return typeof value === 'string' && value.trim().length > 0;
}

function requireFields(object, fields) {
  return fields.filter((field) => object?.[field] === null || object?.[field] === undefined || object?.[field] === '');
}

function extraFields(object, allowed) {
  return object && typeof object === 'object' && !Array.isArray(object)
    ? Object.keys(object).filter((field) => !allowed.has(field)) : [];
}

function timestampOrder(left, right, leftName, rightName) {
  try {
    return { passed: parseUtc(left, leftName) <= parseUtc(right, rightName), detail: `${leftName}=${left}; ${rightName}=${right}` };
  } catch (error) {
    return { passed: false, detail: error.message };
  }
}

export function loadMachineControls(root) {
  const vocabularyDocument = readJson(`${root}/schema/controlled_vocabularies_v1.json`);
  const decisionPacketSchema = readJson(`${root}/schema/decision_packet.schema.json`);
  const ajv = new Ajv2020({ allErrors: true, strict: true, allowUnionTypes: true });
  return {
    vocabularies: Object.fromEntries(
      Object.entries(vocabularyDocument.vocabularies).map(([name, values]) => [name, new Set(values)]),
    ),
    contracts: parseCsv(readFileSync(`${root}/schema/contract_registry_v1.csv`, 'utf8')),
    sourceMaps: parseCsv(readFileSync(`${root}/schema/source_maps_v1.csv`, 'utf8')),
    testEvaluations: parseCsv(readFileSync(`${root}/schema/test_evaluations_v1.csv`, 'utf8')),
    modelRegistry: parseCsv(readFileSync(`${root}/SPORTS_MODEL_REGISTRY_v1.csv`, 'utf8')),
    registeredSources: parseCsv(readFileSync(`${root}/SPORTS_REGISTERED_SOURCES_v1.csv`, 'utf8')),
    competitions: parseCsv(readFileSync(`${root}/schema/competition_registry_v1.csv`, 'utf8')),
    acceptanceTraceability: parseCsv(readFileSync(`${root}/schema/acceptance_traceability_v1.csv`, 'utf8')),
    release: readJson(`${root}/SPORTS_RELEASE_MANIFEST_v1.json`),
    decisionPacketSchema,
    schemaValidator: ajv.compile(decisionPacketSchema),
  };
}

function exactContractExists(contracts, request) {
  return contracts.some((contract) => contract.status === 'ACTIVE'
    && contract.competition_id === request.competition_id
    && contract.ruleset_id === request.ruleset_id
    && contract.settlement_convention_id === request.settlement_convention_id
    && contract.market_family === request.market_family
    && contract.forecast_state === request.forecast_state);
}

function validateBase(packet, controls) {
  const results = [];
  const request = packet?.request ?? {};
  const snapshot = packet?.decision_snapshot ?? {};
  const vocab = controls.vocabularies;

  const jsonSchemaValid = controls.schemaValidator(packet);
  const jsonSchemaErrors = jsonSchemaValid ? [] : (controls.schemaValidator.errors ?? []).map((error) => `${error.instancePath || '/'} ${error.message}`);
  results.push(gate('RUNTIME-JSON-SCHEMA-001', jsonSchemaValid,
    jsonSchemaValid ? 'Draft 2020-12 decision-packet schema passes' : jsonSchemaErrors.join('; ')));

  const allowedTopLevel = new Set([
    'schema_version', 'request', 'decision_snapshot', 'candidate_universe', 'source_packet', 'live_state',
    'prediction', 'forecast_distributions', 'linked_market_relations', 'uncertainty_components', 'price_snapshot',
  ]);
  const requiredTopLevel = [...allowedTopLevel];
  const extraTopLevel = Object.keys(packet ?? {}).filter((key) => !allowedTopLevel.has(key));
  const missingTopLevel = requiredTopLevel.filter((key) => !Object.hasOwn(packet ?? {}, key));
  const topTypesValid = packet && typeof packet.request === 'object' && !Array.isArray(packet.request)
    && typeof packet.decision_snapshot === 'object' && !Array.isArray(packet.decision_snapshot)
    && Array.isArray(packet.forecast_distributions) && Array.isArray(packet.linked_market_relations)
    && Array.isArray(packet.uncertainty_components);
  const schemaShapeValid = packet?.schema_version === DECISION_PACKET_VERSION
    && extraTopLevel.length === 0 && missingTopLevel.length === 0 && topTypesValid;
  results.push(gate('RUNTIME-SCHEMA-001', schemaShapeValid,
    `version=${packet?.schema_version ?? '<missing>'}; missing=${missingTopLevel.join('|') || 'none'}; extra=${extraTopLevel.join('|') || 'none'}; types=${topTypesValid}`));

  const baseRequestMissing = requireFields(request, [
    'request_id', 'primary_question_id', 'primary_question_text', 'raw_request_text', 'contract_status',
    'request_timestamp_utc', 'forecast_series_id', 'created_by',
  ]);
  const requestTypeErrors = [];
  for (const field of ['request_id', 'primary_question_id', 'primary_question_text', 'raw_request_text', 'contract_status', 'request_timestamp_utc', 'forecast_series_id', 'created_by']) {
    if (!nonBlank(request[field]) || (['primary_question_text', 'raw_request_text', 'created_by'].includes(field) && TEMPLATE_SENTINEL.test(request[field]))) requestTypeErrors.push(field);
  }
  const requestExtra = Object.keys(request).filter((field) => !REQUEST_FIELDS.has(field));
  results.push(gate('RUNTIME-REQUEST-001', baseRequestMissing.length === 0 && requestTypeErrors.length === 0 && requestExtra.length === 0,
    `missing=${baseRequestMissing.join('|') || 'none'}; invalid_or_placeholder=${requestTypeErrors.join('|') || 'none'}; extra=${requestExtra.join('|') || 'none'}`));

  const baseSnapshotMissing = requireFields(snapshot, [
    'snapshot_id', 'request_id', 'forecast_series_id', 'snapshot_sequence', 'frozen_at_utc', 'data_cutoff_utc',
    'decision', 'price_evaluation_status', 'data_quality_grade', 'missing_prerequisites', 'snapshot_hash', 'created_by',
  ]);
  const snapshotExtra = Object.keys(snapshot).filter((field) => !SNAPSHOT_FIELDS.has(field));
  const snapshotTypesValid = Number.isInteger(snapshot.snapshot_sequence) && snapshot.snapshot_sequence >= 1
    && ['A', 'B', 'C', 'D'].includes(snapshot.data_quality_grade)
    && Array.isArray(snapshot.missing_prerequisites)
    && Array.isArray(snapshot.gate_failure_evidence)
    && nonBlank(snapshot.created_by) && !TEMPLATE_SENTINEL.test(snapshot.created_by);
  results.push(gate('RUNTIME-SNAPSHOT-001', baseSnapshotMissing.length === 0 && snapshotExtra.length === 0 && snapshotTypesValid,
    `missing=${baseSnapshotMissing.join('|') || 'none'}; extra=${snapshotExtra.join('|') || 'none'}; types=${snapshotTypesValid}`));

  const foreignKeysMatch = request.request_id === snapshot.request_id
    && request.forecast_series_id === snapshot.forecast_series_id;
  results.push(gate('RUNTIME-FOREIGN-KEY-001', foreignKeysMatch, 'request/snapshot identifiers must match'));

  const cutoffOrder = timestampOrder(snapshot.data_cutoff_utc, snapshot.frozen_at_utc, 'data_cutoff_utc', 'frozen_at_utc');
  let stateCutoffValid = true;
  let stateCutoffDetail = 'not an ISSUE publication';
  if (snapshot.decision === 'ISSUE') {
    try {
      const requestTime = parseUtc(request.request_timestamp_utc, 'request_timestamp_utc');
      const freezeTime = parseUtc(snapshot.frozen_at_utc, 'frozen_at_utc');
      stateCutoffValid = requestTime <= freezeTime;
      if (request.forecast_state === 'PREGAME_PROJECTED' || request.forecast_state === 'PREGAME_CONFIRMED') {
        const eventStart = parseUtc(request.event_start_utc, 'event_start_utc');
        stateCutoffValid = stateCutoffValid && freezeTime < eventStart;
        stateCutoffDetail = `request<=freeze<event_start and cutoff<=freeze=${stateCutoffValid}`;
      } else if (request.forecast_state === 'LIVE') {
        const live = packet.live_state;
        stateCutoffValid = stateCutoffValid && Boolean(live && live.event_id === request.event_id
          && nonBlank(live.state_schema_version) && isSha256(live.live_state_hash)
          && parseUtc(live.observed_at_utc, 'live_state.observed_at_utc') <= freezeTime
          && typeof live.remaining_exposure === 'object' && live.remaining_exposure !== null);
        stateCutoffDetail = `typed LIVE state at/before freeze=${stateCutoffValid}`;
      } else {
        stateCutoffValid = false;
        stateCutoffDetail = 'forecast_state is unresolved';
      }
    } catch (error) {
      stateCutoffValid = false;
      stateCutoffDetail = error.message;
    }
  }
  results.push(gate('GATE-CUTOFF-001', cutoffOrder.passed && stateCutoffValid, `${cutoffOrder.detail}; ${stateCutoffDetail}`));

  let requestTimeValid = true;
  let requestTimeDetail = 'request timestamp is valid UTC';
  try { parseUtc(request.request_timestamp_utc, 'request_timestamp_utc'); } catch (error) {
    requestTimeValid = false;
    requestTimeDetail = error.message;
  }
  results.push(gate('RUNTIME-TIME-001', requestTimeValid, requestTimeDetail));

  const vocabularyChecks = [
    ['contract_status', request.contract_status],
    ['decision', snapshot.decision],
    ['price_evaluation_status', snapshot.price_evaluation_status],
  ];
  if (request.analysis_mode !== null && request.analysis_mode !== undefined) vocabularyChecks.push(['analysis_mode', request.analysis_mode]);
  if (request.forecast_state !== null && request.forecast_state !== undefined) vocabularyChecks.push(['forecast_state', request.forecast_state]);
  if (request.selection_mode !== null && request.selection_mode !== undefined) vocabularyChecks.push(['selection_mode', request.selection_mode]);
  const invalidVocab = vocabularyChecks.filter(([name, value]) => !vocab[name]?.has(value));
  results.push(gate('RUNTIME-VOCAB-001', invalidVocab.length === 0,
    invalidVocab.length ? invalidVocab.map(([name, value]) => `${name}=${value}`).join('; ') : 'controlled values pass'));

  const expectedHash = computeSnapshotHash(packet);
  const hashValid = isSha256(snapshot.snapshot_hash) && snapshot.snapshot_hash === expectedHash;
  results.push(gate('RUNTIME-HASH-001', hashValid,
    hashValid ? `snapshot hash recomputed: ${expectedHash}` : `stored=${snapshot.snapshot_hash ?? '<missing>'}; recomputed=${expectedHash}`));

  return results;
}

function validatePassOrWatch(packet, controls, coverageRows) {
  const snapshot = packet.decision_snapshot;
  const request = packet.request;
  const results = [];
  const isPass = snapshot.decision === 'PASS';
  const isWatch = snapshot.decision === 'WATCH';

  const reasonValid = isPass
    ? controls.vocabularies.pass_reason.has(snapshot.pass_reason)
    : nonBlank(snapshot.watch_reason) && nonBlank(snapshot.watch_expires_utc);
  results.push(gate('RUNTIME-ABSTENTION-001', reasonValid,
    isPass ? `pass_reason=${snapshot.pass_reason ?? '<missing>'}` : 'WATCH reason and expiry required'));

  const quantitativeAbsent = packet.prediction === null
    && packet.candidate_universe === null
    && packet.source_packet === null
    && packet.live_state === null
    && (packet.forecast_distributions?.length ?? 0) === 0
    && (packet.linked_market_relations?.length ?? 0) === 0
    && (packet.uncertainty_components?.length ?? 0) === 0
    && packet.price_snapshot === null;
  results.push(gate('RUNTIME-ABSTENTION-NULLS-001', quantitativeAbsent,
    'WATCH/PASS must have null prediction/price and empty distributions/uncertainty'));

  const noteValid = !snapshot.research_note || !FORECAST_LIKE_NOTE.test(snapshot.research_note);
  results.push(gate('RUNTIME-NONPROB-NOTE-001', noteValid,
    noteValid ? 'research note contains no probability/value language' : 'research note contains prohibited forecast-like language'));

  const prerequisitesValid = Array.isArray(snapshot.missing_prerequisites) && snapshot.missing_prerequisites.length > 0
    && snapshot.missing_prerequisites.every((item) => nonBlank(item));
  results.push(gate('RUNTIME-MISSING-PREREQUISITES-001', prerequisitesValid, 'WATCH/PASS requires a nonempty typed prerequisite list'));

  const requiredGate = isPass ? PASS_REASON_GATE[snapshot.pass_reason] : null;
  const evidence = snapshot.gate_failure_evidence ?? [];
  const evidenceValid = isPass
    ? snapshot.primary_failed_gate === requiredGate && evidence.length >= 1
      && evidence.every((item) => item.gate_id === requiredGate && nonBlank(item.code) && nonBlank(item.detail)
        && Array.isArray(item.evidence_refs) && item.evidence_refs.length > 0)
    : snapshot.primary_failed_gate === null && evidence.length === 0;
  results.push(gate('RUNTIME-FAILURE-EVIDENCE-001', evidenceValid,
    isPass ? `reason=${snapshot.pass_reason}; required_gate=${requiredGate}; stored_gate=${snapshot.primary_failed_gate}` : 'WATCH has no failed gate'));

  const missingIssueContract = requireFields(request, REQUIRED_PREMODEL_REQUEST_FIELDS);
  const registeredContract = missingIssueContract.length === 0 && exactContractExists(controls.contracts, request);
  const modesValid = controls.vocabularies.analysis_mode.has(request.analysis_mode) && controls.vocabularies.forecast_state.has(request.forecast_state);
  const active = modesValid && request.sport_family && request.competition_id && request.market_family
    ? findExactActiveCoverage(coverageRows, request) : null;
  let causeValid = true;
  let causeDetail = 'watch prerequisites pending after valid contract/model lookup';
  if (isPass) {
    switch (snapshot.pass_reason) {
      case 'CONTRACT_UNRESOLVED':
        causeValid = request.contract_status === 'UNRESOLVED' && (!registeredContract || missingIssueContract.length > 0);
        causeDetail = `contract_status=${request.contract_status}; registered=${registeredContract}; missing=${missingIssueContract.join('|') || 'none'}`;
        break;
      case 'MODE_UNRESOLVED':
        causeValid = !modesValid;
        causeDetail = `modes_valid=${modesValid}`;
        break;
      case 'MODEL_UNAVAILABLE':
        causeValid = request.contract_status === 'RESOLVED' && registeredContract && modesValid && active === null;
        causeDetail = `contract_registered=${registeredContract}; modes_valid=${modesValid}; active_coverage=${active?.coverage_id ?? 'none'}`;
        break;
      case 'USER_CANCELLED':
        causeValid = request.user_cancelled === true;
        causeDetail = `user_cancelled=${request.user_cancelled === true}`;
        break;
      case 'CUTOFF_FAILURE': {
        const observations = packet.source_packet?.observations ?? [];
        causeValid = observations.some((observation) => {
          try { return parseUtc(observation.known_at_utc, 'known_at_utc') > parseUtc(snapshot.data_cutoff_utc, 'data_cutoff_utc'); } catch { return true; }
        });
        causeDetail = `source_observations_with_cutoff_failure=${causeValid}`;
        break;
      }
      case 'SOURCE_FAILURE':
        causeValid = packet.source_packet === null || (packet.source_packet.observations ?? []).some((observation) => observation.retrieval_status !== 'SUCCESS' || observation.verification_status !== 'VERIFIED');
        causeDetail = `source_packet_failed_or_missing=${causeValid}`;
        break;
      case 'UNIVERSE_NOT_FROZEN':
        causeValid = packet.candidate_universe === null || !isSha256(packet.candidate_universe?.universe_hash);
        causeDetail = `universe_missing_or_unhashed=${causeValid}`;
        break;
      case 'OUT_OF_SCOPE':
        causeValid = !coverageRows.some((row) => row.sport_family === request.sport_family);
        causeDetail = `sport_registered=${!causeValid}`;
        break;
      case 'PROBABILITY_INVALID':
      case 'UNCERTAINTY_UNRESOLVED':
        causeValid = evidenceValid && evidence.every((item) => isSha256(item.artifact_hash));
        causeDetail = `external_diagnostic_artifacts=${causeValid}`;
        break;
      case 'SYSTEM_NOT_READY':
      case 'OTHER_DOCUMENTED':
        causeValid = evidenceValid && evidence.every((item) => item.code === 'AUTHORITY_CONFLICT' && isSha256(item.artifact_hash));
        causeDetail = `authority_conflict_artifact=${causeValid}`;
        break;
      default:
        causeValid = false;
        causeDetail = 'unsupported PASS reason';
    }
  } else {
    causeValid = request.contract_status === 'RESOLVED' && registeredContract && Boolean(active);
    causeDetail = `WATCH contract_registered=${registeredContract}; active_coverage=${active?.coverage_id ?? 'none'}`;
  }
  results.push(gate('RUNTIME-ABSTENTION-CAUSE-001', causeValid, causeDetail));

  if (isWatch) {
    let expiryValid = false;
    try { expiryValid = parseUtc(snapshot.watch_expires_utc, 'watch_expires_utc') > parseUtc(snapshot.frozen_at_utc, 'frozen_at_utc'); } catch { /* false */ }
    results.push(gate('RUNTIME-WATCH-EXPIRY-001', expiryValid, 'WATCH expiry must be after freeze'));
  }
  return results;
}

function validateIssue(packet, controls, coverageRows, controlBundleHash) {
  const request = packet.request;
  const snapshot = packet.decision_snapshot;
  const prediction = packet.prediction ?? {};
  const results = [];

  const releaseReport = validateReleaseManifest(controls.release, coverageRows);
  const controlReport = validateRuntimeControls(controls, coverageRows, { now: parseUtc(snapshot.frozen_at_utc, 'snapshot.frozen_at_utc') });
  const authorityValid = releaseReport.valid && controlReport.valid && controls.release.release_mode === 'OPERATIONAL'
    && controls.release.activation_authorized === true && isSha256(controlBundleHash);
  results.push(gate('GATE-AUTH-001', authorityValid,
    authorityValid ? `release=${controls.release.release_id}; mode=OPERATIONAL`
      : `release_mode=${controls.release?.release_mode ?? '<missing>'}; release_errors=${releaseReport.errors.join('|') || 'none'}; control_errors=${controlReport.errors.join('|') || 'none'}; activation_authorized=${controls.release?.activation_authorized === true}; control_bundle_hash=${isSha256(controlBundleHash)}`));

  const missingContract = requireFields(request, REQUIRED_ISSUE_REQUEST_FIELDS);
  const contract = controls.contracts.find((item) => item.status === 'ACTIVE'
    && item.competition_id === request.competition_id && item.ruleset_id === request.ruleset_id
    && item.settlement_convention_id === request.settlement_convention_id && item.market_family === request.market_family
    && item.forecast_state === request.forecast_state);
  const contractErrors = [];
  if (!contract) contractErrors.push('exact ACTIVE contract is absent');
  else {
    if (!contract.contract_id || !isSha256(contract.branch_definition_hash) || !contract.approved_by) contractErrors.push('contract identity/branch/approval evidence is incomplete');
    const sourceIds = new Set((controls.registeredSources ?? []).map((source) => source.source_id));
    if (!sourceIds.has(contract.official_rules_source_id) || !sourceIds.has(contract.settlement_authority_source_id)) {
      contractErrors.push('contract authority sources are not registered');
    }
    try {
      const cutoff = parseUtc(snapshot.data_cutoff_utc, 'data_cutoff_utc');
      if (parseUtc(contract.effective_from_utc, 'contract.effective_from_utc') > cutoff) contractErrors.push('contract is not yet effective at cutoff');
      if (contract.effective_to_utc && parseUtc(contract.effective_to_utc, 'contract.effective_to_utc') <= cutoff) contractErrors.push('contract expired by cutoff');
      if (parseUtc(contract.approval_utc, 'contract.approval_utc') > cutoff) contractErrors.push('contract approval occurred after cutoff');
    } catch (error) { contractErrors.push(error.message); }
  }
  const competitionActive = (controls.competitions ?? []).some((item) => item.competition_id === request.competition_id
    && ['ACTIVE', 'DEVELOPMENT'].includes(item.status));
  if (!competitionActive) contractErrors.push('competition_id is not registered');
  const contractRegistered = missingContract.length === 0 && request.contract_status === 'RESOLVED' && contractErrors.length === 0;
  results.push(gate('GATE-CONTRACT-001', contractRegistered,
    `missing=${missingContract.join('|') || 'none'}; errors=${contractErrors.join('|') || 'none'}`));

  const modeValid = controls.vocabularies.analysis_mode.has(request.analysis_mode)
    && controls.vocabularies.forecast_state.has(request.forecast_state);
  results.push(gate('GATE-MODE-001', modeValid, `analysis_mode=${request.analysis_mode}; forecast_state=${request.forecast_state}`));

  const universe = packet.candidate_universe;
  const candidates = universe?.candidates ?? [];
  const onePrimary = candidates.filter((candidate) => candidate.is_primary_question === true).length === 1;
  const oneSelected = candidates.filter((candidate) => candidate.selected_for_issue === true).length === 1;
  const universeMissing = requireFields(universe, [
    'candidate_universe_id', 'request_id', 'primary_question_id', 'universe_definition_version', 'selection_mode',
    'selection_policy_version', 'known_at_utc', 'frozen_at_utc', 'enumeration_manifest_hash', 'candidate_count', 'universe_hash', 'candidates',
  ]);
  const universeExtra = extraFields(universe, UNIVERSE_FIELDS);
  const countMatches = universe && Number.isInteger(universe.candidate_count) && universe.candidate_count === candidates.length;
  const uniqueCandidateIds = new Set(candidates.map((candidate) => candidate.candidate_id)).size === candidates.length;
  const candidateForeignKeys = candidates.every((candidate) => candidate.candidate_universe_id === universe?.candidate_universe_id);
  const universeForeignKeys = universe?.request_id === request.request_id
    && universe?.primary_question_id === request.primary_question_id
    && universe?.candidate_universe_id === request.candidate_universe_id
    && universe?.candidate_universe_id === snapshot.candidate_universe_id
    && universe?.selection_mode === request.selection_mode
    && universe?.selection_policy_version === request.selection_policy_version;
  const candidateErrors = [];
  for (const candidate of candidates) {
    const missing = requireFields(candidate, [
      'candidate_id', 'candidate_universe_id', 'market_id', 'selection', 'market_outcome_space_id', 'relationship_type',
      'related_candidate_ids', 'is_primary_question', 'inclusion_source', 'candidate_status', 'probability_generation_status',
      'selected_for_issue', 'candidate_frozen_at_utc',
    ]);
    if (missing.length) candidateErrors.push(`${candidate.candidate_id ?? '<missing>'}: missing ${missing.join('|')}`);
    const extra = extraFields(candidate, CANDIDATE_FIELDS);
    if (extra.length) candidateErrors.push(`${candidate.candidate_id ?? '<missing>'}: extra ${extra.join('|')}`);
    if (!controls.vocabularies.candidate_status.has(candidate.candidate_status)) candidateErrors.push(`${candidate.candidate_id}: invalid candidate_status`);
    if (!controls.vocabularies.probability_generation_status.has(candidate.probability_generation_status)) candidateErrors.push(`${candidate.candidate_id}: invalid probability_generation_status`);
    if (!controls.vocabularies.candidate_relationship_type.has(candidate.relationship_type)) candidateErrors.push(`${candidate.candidate_id}: invalid relationship_type`);
    if (!Array.isArray(candidate.related_candidate_ids) || typeof candidate.is_primary_question !== 'boolean'
      || typeof candidate.selected_for_issue !== 'boolean') candidateErrors.push(`${candidate.candidate_id}: candidate arrays/booleans invalid`);
    if (candidate.probability_generation_status === 'GENERATED'
      && (!nonBlank(candidate.forecast_distribution_id) || !Array.isArray(candidate.winning_state_ids) || candidate.winning_state_ids.length === 0)) {
      candidateErrors.push(`${candidate.candidate_id}: GENERATED requires distribution and winning states`);
    }
    if (candidate.selected_for_issue === true && (candidate.candidate_status !== 'SELECTED' || candidate.probability_generation_status !== 'GENERATED')) {
      candidateErrors.push(`${candidate.candidate_id}: selected candidate must be SELECTED and GENERATED`);
    }
    if (String(candidate.candidate_status).startsWith('REJECTED') && !nonBlank(candidate.rejection_reason)) {
      candidateErrors.push(`${candidate.candidate_id}: rejected candidate requires rejection_reason`);
    }
  }
  const primaryCandidate = candidates.find((candidate) => candidate.is_primary_question === true);
  const selectedUniverseCandidate = candidates.find((candidate) => candidate.selected_for_issue === true);
  const primaryIsSelected = primaryCandidate?.candidate_id === selectedUniverseCandidate?.candidate_id;
  const canonicalCandidates = [...candidates].sort((left, right) => compareCanonicalStrings(String(left.candidate_id), String(right.candidate_id)));
  const recomputedUniverseHash = universe ? hashObject({
    candidate_universe_id: universe.candidate_universe_id,
    request_id: universe.request_id,
    primary_question_id: universe.primary_question_id,
    universe_definition_version: universe.universe_definition_version,
    selection_mode: universe.selection_mode,
    selection_policy_version: universe.selection_policy_version,
    known_at_utc: universe.known_at_utc,
    frozen_at_utc: universe.frozen_at_utc,
    enumeration_manifest_hash: universe.enumeration_manifest_hash,
    candidate_count: universe.candidate_count,
    candidates: canonicalCandidates,
  }) : null;
  const universeHashMatches = universe && isSha256(universe.universe_hash) && isSha256(universe.enumeration_manifest_hash)
    && universe.universe_hash === recomputedUniverseHash;
  let universeBeforeCutoff = false;
  try { universeBeforeCutoff = parseUtc(universe.known_at_utc, 'universe.known_at_utc') <= parseUtc(universe.frozen_at_utc, 'universe.frozen_at_utc')
    && parseUtc(universe.frozen_at_utc, 'universe.frozen_at_utc') <= parseUtc(snapshot.data_cutoff_utc, 'data_cutoff_utc'); } catch { /* false */ }
  let candidateTimesValid = true;
  for (const candidate of candidates) {
    try {
      if (parseUtc(candidate.candidate_frozen_at_utc, 'candidate_frozen_at_utc') > parseUtc(universe.frozen_at_utc, 'universe.frozen_at_utc')) candidateTimesValid = false;
    } catch { candidateTimesValid = false; }
  }
  results.push(gate('GATE-UNIVERSE-001', Boolean(universe && universeMissing.length === 0 && universeExtra.length === 0
    && onePrimary && oneSelected && primaryIsSelected && countMatches && uniqueCandidateIds && candidateErrors.length === 0
    && candidateForeignKeys && universeForeignKeys && universeHashMatches && universeBeforeCutoff && candidateTimesValid),
  `count=${candidates.length}; missing=${universeMissing.join('|') || 'none'}; extra=${universeExtra.join('|') || 'none'}; primary_selected=${primaryIsSelected}; unique=${uniqueCandidateIds}; foreign_keys=${universeForeignKeys && candidateForeignKeys}; hash=${universeHashMatches}; frozen_by_cutoff=${universeBeforeCutoff}; candidate_errors=${candidateErrors.join('~') || 'none'}`));

  const observations = packet.source_packet?.observations ?? [];
  const sourceTimingErrors = [];
  const sourcePacket = packet.source_packet;
  const sourcePacketMissing = requireFields(sourcePacket, ['source_packet_id', 'request_id', 'snapshot_id', 'source_map_id', 'frozen_at_utc', 'observations', 'source_packet_hash']);
  const sourcePacketExtra = extraFields(sourcePacket, SOURCE_PACKET_FIELDS);
  const observationIds = new Set();
  const registeredSourceById = new Map((controls.registeredSources ?? []).map((source) => [source.source_id, source]));
  for (const observation of observations) {
    const missing = requireFields(observation, [
      'source_observation_id', 'source_packet_id', 'source_map_id', 'source_id', 'source_release_id', 'requested_url', 'final_url',
      'authority_class', 'fact_type', 'known_at_utc', 'fetched_at_utc', 'transport_type', 'retrieval_status', 'freshness_status',
      'verification_status', 'extracted_value', 'raw_hash', 'extractor_version', 'historical_reconstruction',
    ]);
    if (missing.length) sourceTimingErrors.push(`${observation.source_observation_id ?? '<unknown>'}: missing ${missing.join('|')}`);
    const extra = extraFields(observation, SOURCE_OBSERVATION_FIELDS);
    if (extra.length) sourceTimingErrors.push(`${observation.source_observation_id ?? '<unknown>'}: extra ${extra.join('|')}`);
    if (observationIds.has(observation.source_observation_id)) sourceTimingErrors.push(`${observation.source_observation_id}: duplicate observation ID`);
    observationIds.add(observation.source_observation_id);
    const registeredSource = registeredSourceById.get(observation.source_id);
    if (!registeredSource || registeredSource.authority_class !== observation.authority_class) sourceTimingErrors.push(`${observation.source_observation_id}: registered source/authority mismatch`);
    if (observation.source_packet_id !== sourcePacket?.source_packet_id || observation.source_map_id !== sourcePacket?.source_map_id) {
      sourceTimingErrors.push(`${observation.source_observation_id}: source packet/map foreign key mismatch`);
    }
    if (observation.retrieval_status !== 'SUCCESS' || observation.verification_status !== 'VERIFIED' || observation.freshness_status !== 'FRESH') {
      sourceTimingErrors.push(`${observation.source_observation_id}: source is not SUCCESS/FRESH/VERIFIED`);
    }
    try {
      if (parseUtc(observation.known_at_utc, 'known_at_utc') > parseUtc(snapshot.data_cutoff_utc, 'data_cutoff_utc')) {
        sourceTimingErrors.push(`${observation.source_observation_id}: known after cutoff`);
      }
      if (observation.historical_reconstruction !== true
        && parseUtc(observation.fetched_at_utc, 'fetched_at_utc') > parseUtc(snapshot.frozen_at_utc, 'frozen_at_utc')) {
        sourceTimingErrors.push(`${observation.source_observation_id}: fetched after freeze`);
      }
      if (observation.historical_reconstruction === true
        && (!isSha256(observation.as_of_evidence_hash) || !nonBlank(observation.as_of_version_id))) {
        sourceTimingErrors.push(`${observation.source_observation_id}: reconstruction lacks versioned as-of evidence`);
      }
      if (!isSha256(observation.raw_hash)) sourceTimingErrors.push(`${observation.source_observation_id}: raw_hash invalid`);
    } catch (error) {
      sourceTimingErrors.push(`${observation.source_observation_id ?? '<unknown>'}: ${error.message}`);
    }
  }
  const activeCoverage = findExactActiveCoverage(coverageRows, request);
  const activeMapRows = activeCoverage
    ? controls.sourceMaps.filter((row) => row.source_map_id === activeCoverage.source_map_id && row.status === 'ACTIVE')
    : [];
  const sourceMapErrors = [];
  for (const item of activeMapRows) {
    if (item.model_id !== activeCoverage.model_id || item.model_version !== activeCoverage.model_version
      || item.sport_family !== request.sport_family || item.competition_id !== request.competition_id
      || item.market_family !== request.market_family || item.forecast_state !== request.forecast_state
      || item.horizon_bucket_id !== request.horizon_bucket_id) sourceMapErrors.push(`${item.source_id}: source-map scope/model mismatch`);
    if (!item.parser_id || !item.parser_version || !isSha256(item.parser_hash) || !item.regression_test_report_id || !isSha256(item.map_hash)) {
      sourceMapErrors.push(`${item.source_id}: parser/map evidence incomplete`);
    }
    if (!Number.isFinite(Number(item.max_observation_age_seconds)) || Number(item.max_observation_age_seconds) < 0
      || !Number.isFinite(Number(item.max_provider_lag_seconds)) || Number(item.max_provider_lag_seconds) < 0) {
      sourceMapErrors.push(`${item.source_id}: invalid freshness/lag limits`);
    }
    try {
      if (parseUtc(item.expires_utc, 'source_map.expires_utc') <= parseUtc(snapshot.frozen_at_utc, 'frozen_at_utc')) sourceMapErrors.push(`${item.source_id}: source-map approval expired`);
      if (parseUtc(item.approval_utc, 'source_map.approval_utc') > parseUtc(snapshot.frozen_at_utc, 'frozen_at_utc')) sourceMapErrors.push(`${item.source_id}: source-map approved after freeze`);
    } catch (error) { sourceMapErrors.push(`${item.source_id}: ${error.message}`); }
  }
  for (const item of activeMapRows.filter((row) => String(row.required).toUpperCase() === 'TRUE')) {
    const matches = observations.filter((observation) => observation.source_map_id === item.source_map_id
      && observation.source_id === item.source_id && observation.fact_type === item.fact_type);
    if (matches.length === 0) sourceMapErrors.push(`missing required ${item.fact_type}/${item.source_id}`);
    if (!item.regression_test_report_id || !item.parser_hash) sourceMapErrors.push(`${item.fact_type}/${item.source_id}: parser evidence incomplete`);
  }
  for (const observation of observations) {
    if (!activeMapRows.some((item) => item.source_id === observation.source_id && item.fact_type === observation.fact_type)) {
      sourceMapErrors.push(`${observation.source_observation_id}: observation is not declared in the ACTIVE source map`);
    }
  }
  if (activeCoverage && activeMapRows.length === 0) sourceMapErrors.push(`approved source_map_id ${activeCoverage.source_map_id} has no ACTIVE items`);
  const sourcePacketForeignKeys = sourcePacket?.request_id === request.request_id && sourcePacket?.snapshot_id === snapshot.snapshot_id
    && sourcePacket?.source_map_id === activeCoverage?.source_map_id;
  let sourcePacketFrozen = false;
  try { sourcePacketFrozen = parseUtc(sourcePacket?.frozen_at_utc, 'source_packet.frozen_at_utc') <= parseUtc(snapshot.data_cutoff_utc, 'data_cutoff_utc'); } catch { /* false */ }
  const sourcePacketHash = sourcePacket ? hashObject({
    source_packet_id: sourcePacket.source_packet_id,
    request_id: sourcePacket.request_id,
    snapshot_id: sourcePacket.snapshot_id,
    source_map_id: sourcePacket.source_map_id,
    frozen_at_utc: sourcePacket.frozen_at_utc,
    observations: [...observations].sort((left, right) => compareCanonicalStrings(String(left.source_observation_id), String(right.source_observation_id))),
  }) : null;
  const sourcePacketHashValid = isSha256(sourcePacket?.source_packet_hash) && sourcePacket.source_packet_hash === sourcePacketHash;
  const sourceValid = sourcePacket && sourcePacketMissing.length === 0 && sourcePacketExtra.length === 0 && observations.length > 0
    && sourcePacketForeignKeys && sourcePacketFrozen && sourcePacketHashValid && sourceTimingErrors.length === 0 && sourceMapErrors.length === 0;
  results.push(gate('GATE-SOURCE-001', sourceValid,
    sourceValid ? `${observations.length} observations pass temporal/hash/source-map checks`
      : ([`packet_missing=${sourcePacketMissing.join('|') || 'none'}`, `packet_extra=${sourcePacketExtra.join('|') || 'none'}`,
        `foreign_keys=${sourcePacketForeignKeys}`, `packet_frozen=${sourcePacketFrozen}`, `packet_hash=${sourcePacketHashValid}`,
        ...sourceTimingErrors, ...sourceMapErrors].join('; ') || 'source packet is empty')));

  const registryModel = controls.modelRegistry.find((row) => row.model_id === prediction.model_id && row.model_version === prediction.model_version);
  let modelEvidenceValid = Boolean(registryModel);
  if (registryModel) {
    modelEvidenceValid = registryModel.status === 'ACTIVE'
      && registryModel.sport_family === request.sport_family
      && registryModel.competition_scope === request.competition_id
      && registryModel.market_scope === request.market_family
      && registryModel.forecast_state === request.forecast_state
      && registryModel.analysis_mode === request.analysis_mode
      && nonBlank(registryModel.owner) && nonBlank(registryModel.approver) && nonBlank(registryModel.change_ticket_id)
      && isSha256(registryModel.data_manifest_hash) && isSha256(registryModel.code_hash)
      && isSha256(registryModel.model_artifact_hash) && isSha256(registryModel.calibration_artifact_hash);
    try {
      modelEvidenceValid = modelEvidenceValid
        && parseUtc(registryModel.approval_utc, 'model.approval_utc') <= parseUtc(snapshot.frozen_at_utc, 'frozen_at_utc')
        && parseUtc(registryModel.expires_utc, 'model.expires_utc') > parseUtc(snapshot.frozen_at_utc, 'frozen_at_utc');
    } catch { modelEvidenceValid = false; }
  }
  const modelValid = activeCoverage
    && activeCoverage.coverage_id === prediction.coverage_id
    && activeCoverage.model_id === prediction.model_id
    && activeCoverage.model_version === prediction.model_version
    && modelEvidenceValid
    && registryModel.source_map_id === activeCoverage.source_map_id
    && registryModel.test_report_id === activeCoverage.test_report_id
    && registryModel.shadow_report_id === activeCoverage.shadow_report_id
    && registryModel.model_artifact_hash === prediction.model_artifact_hash
    && registryModel.code_hash === prediction.code_commit_or_hash;
  results.push(gate('GATE-MODEL-001', Boolean(modelValid),
    modelValid ? `coverage/model join=${activeCoverage.coverage_id}` : 'exact ACTIVE model and coverage join failed'));

  const testReport = controls.testEvaluations.find((row) => row.test_evaluation_id === activeCoverage?.test_report_id
    && row.hypothesis_family_id === registryModel?.hypothesis_family_id && row.test_role === 'UNTOUCHED_TEST'
    && row.model_id === registryModel?.model_id && row.model_version === registryModel?.model_version
    && row.test_status === 'SPENT' && isSha256(row.event_manifest_hash) && isSha256(row.preregistered_rule_hash)
    && isSha256(row.results_artifact_hash) && row.decision_rule_passed === 'TRUE');
  const shadowReport = controls.testEvaluations.find((row) => row.test_evaluation_id === activeCoverage?.shadow_report_id
    && row.hypothesis_family_id === registryModel?.hypothesis_family_id && row.test_role === 'PROSPECTIVE_SHADOW'
    && row.model_id === registryModel?.model_id && row.model_version === registryModel?.model_version
    && row.test_status === 'SPENT' && isSha256(row.event_manifest_hash) && isSha256(row.preregistered_rule_hash)
    && isSha256(row.results_artifact_hash) && row.decision_rule_passed === 'TRUE');
  let testValid = false;
  if (testReport && shadowReport) {
    try {
      const testStart = parseUtc(testReport.start_utc, 'test.start_utc');
      const testEnd = parseUtc(testReport.end_utc, 'test.end_utc');
      const shadowStart = parseUtc(shadowReport.start_utc, 'shadow.start_utc');
      const shadowEnd = parseUtc(shadowReport.end_utc, 'shadow.end_utc');
      testValid = testStart < testEnd && testEnd < shadowStart && shadowStart < shadowEnd
        && parseUtc(testReport.preregistered_at_utc, 'test.preregistered_at_utc') < testStart
        && parseUtc(shadowReport.preregistered_at_utc, 'shadow.preregistered_at_utc') < shadowStart
        && parseUtc(testReport.first_viewed_at_utc, 'test.first_viewed_at_utc') >= testEnd
        && parseUtc(shadowReport.first_viewed_at_utc, 'shadow.first_viewed_at_utc') >= shadowEnd
        && nonBlank(testReport.viewed_by) && nonBlank(shadowReport.viewed_by)
        && nonBlank(testReport.independent_evaluator) && nonBlank(shadowReport.independent_evaluator)
        && Number(testReport.effective_n) > 0 && Number(shadowReport.effective_n) > 0
        && testReport.event_manifest_hash !== shadowReport.event_manifest_hash;
    } catch { testValid = false; }
  }
  results.push(gate('GATE-TEST-001', testValid,
    testValid ? `spent test ${testReport.test_evaluation_id}; later shadow ${shadowReport.test_evaluation_id}`
      : 'hypothesis-family spent-test and later prospective-shadow evidence do not join'));

  const predictionMissing = requireFields(prediction, REQUIRED_PREDICTION_FIELDS);
  const predictionExtra = extraFields(prediction, PREDICTION_FIELDS);
  let predictionRunAtValid = false;
  try { predictionRunAtValid = parseUtc(prediction.run_at_utc, 'prediction.run_at_utc') <= parseUtc(snapshot.frozen_at_utc, 'snapshot.frozen_at_utc'); } catch { /* false */ }
  const predictionForeignKeys = prediction.snapshot_id === snapshot.snapshot_id
    && prediction.candidate_universe_id === universe?.candidate_universe_id
    && prediction.source_packet_id === sourcePacket?.source_packet_id
    && prediction.selected_candidate_id === selectedUniverseCandidate?.candidate_id;
  const predictionArtifactsValid = isSha256(prediction.code_commit_or_hash) && isSha256(prediction.model_artifact_hash)
    && isSha256(prediction.feature_snapshot_hash) && isSha256(prediction.data_manifest_hash)
    && isSha256(prediction.calibration_artifact_hash)
    && prediction.data_manifest_hash === registryModel?.data_manifest_hash
    && prediction.calibration_artifact_hash === registryModel?.calibration_artifact_hash
    && controls.vocabularies.calibration_status.has(prediction.calibration_status)
    && Array.isArray(prediction.invalidation_triggers) && prediction.invalidation_triggers.length > 0
    && prediction.invalidation_triggers.every((item) => nonBlank(item));
  results.push(gate('RUNTIME-PREDICTION-001', predictionMissing.length === 0 && predictionExtra.length === 0
    && predictionRunAtValid && predictionForeignKeys && predictionArtifactsValid,
  `missing=${predictionMissing.join('|') || 'none'}; extra=${predictionExtra.join('|') || 'none'}; run_at=${predictionRunAtValid}; foreign_keys=${predictionForeignKeys}; artifacts=${predictionArtifactsValid}`));

  const distributions = packet.forecast_distributions ?? [];
  const distributionErrors = [];
  const distributionIds = new Set();
  for (const distribution of distributions) {
    const states = distribution.states ?? [];
    const missing = requireFields(distribution, [
      'forecast_distribution_id', 'market_outcome_space_id', 'calibration_evidence_id', 'frozen_at_utc', 'states', 'distribution_hash',
    ]);
    if (missing.length) distributionErrors.push(`${distribution.forecast_distribution_id ?? '<missing>'}: missing ${missing.join('|')}`);
    const extra = extraFields(distribution, DISTRIBUTION_FIELDS);
    if (extra.length) distributionErrors.push(`${distribution.forecast_distribution_id ?? '<missing>'}: extra ${extra.join('|')}`);
    if (distributionIds.has(distribution.forecast_distribution_id)) distributionErrors.push(`${distribution.forecast_distribution_id}: duplicate distribution ID`);
    distributionIds.add(distribution.forecast_distribution_id);
    const stateIds = new Set();
    for (const state of states) {
      const stateMissing = requireFields(state, [
        'settlement_state_id', 'forecast_distribution_id', 'market_outcome_space_id', 'state_label', 'branch_type',
        'raw_probability', 'decision_probability', 'baseline_probability', 'is_structural',
      ]);
      if (stateMissing.length) distributionErrors.push(`${distribution.forecast_distribution_id}: state missing ${stateMissing.join('|')}`);
      const stateExtra = extraFields(state, STATE_FIELDS);
      if (stateExtra.length) distributionErrors.push(`${distribution.forecast_distribution_id}: state extra ${stateExtra.join('|')}`);
      if (stateIds.has(state.settlement_state_id)) distributionErrors.push(`${distribution.forecast_distribution_id}: duplicate state ${state.settlement_state_id}`);
      stateIds.add(state.settlement_state_id);
      if (state.forecast_distribution_id !== distribution.forecast_distribution_id
        || state.market_outcome_space_id !== distribution.market_outcome_space_id) distributionErrors.push(`${state.settlement_state_id}: distribution/outcome-space foreign key mismatch`);
      if (!controls.vocabularies.branch_type.has(state.branch_type) || typeof state.is_structural !== 'boolean') {
        distributionErrors.push(`${state.settlement_state_id}: invalid branch_type/is_structural`);
      }
    }
    distributionErrors.push(...validateProbabilityVector(states.map((state) => state.decision_probability), 1e-9, {
      structuralMask: states.map((state) => state.is_structural === true),
    }).map((error) => `${distribution.forecast_distribution_id}: ${error}`));
    distributionErrors.push(...validateProbabilityVector(states.map((state) => state.raw_probability), 1e-9, {
      structuralMask: states.map((state) => state.is_structural === true),
    }).map((error) => `${distribution.forecast_distribution_id} raw: ${error}`));
    const baselineErrors = validateProbabilityVector(states.map((state) => state.baseline_probability), 1e-9, { allowStructuralBoundary: true });
    distributionErrors.push(...baselineErrors.map((error) => `${distribution.forecast_distribution_id} baseline: ${error}`));
    let distributionFrozen = false;
    try { distributionFrozen = parseUtc(distribution.frozen_at_utc, 'distribution.frozen_at_utc') <= parseUtc(snapshot.frozen_at_utc, 'snapshot.frozen_at_utc'); } catch { /* false */ }
    if (!distributionFrozen) distributionErrors.push(`${distribution.forecast_distribution_id}: distribution frozen after snapshot or invalid`);
    const recomputedDistributionHash = hashObject({
      forecast_distribution_id: distribution.forecast_distribution_id,
      market_outcome_space_id: distribution.market_outcome_space_id,
      joint_distribution_id: distribution.joint_distribution_id ?? null,
      calibration_evidence_id: distribution.calibration_evidence_id,
      frozen_at_utc: distribution.frozen_at_utc,
      states: [...states].sort((left, right) => compareCanonicalStrings(String(left.settlement_state_id), String(right.settlement_state_id))),
    });
    if (!isSha256(distribution.distribution_hash) || distribution.distribution_hash !== recomputedDistributionHash) {
      distributionErrors.push(`${distribution.forecast_distribution_id}: distribution hash mismatch`);
    }
  }
  const selectedDistribution = distributions.find((distribution) => distribution.forecast_distribution_id === prediction.forecast_distribution_id);
  const selectedCandidate = candidates.find((candidate) => candidate.candidate_id === prediction.selected_candidate_id);
  const derivedProbability = selectedDistribution && selectedCandidate
    ? selectedDistribution.states
      .filter((state) => selectedCandidate.winning_state_ids?.includes(state.settlement_state_id))
      .reduce((sum, state) => sum + state.decision_probability, 0)
    : Number.NaN;
  if (!Number.isFinite(derivedProbability) || Math.abs(derivedProbability - prediction.decision_probability) > 1e-12) {
    distributionErrors.push('selected decision_probability does not equal the WIN-state aggregate');
  }
  const derivedRawProbability = selectedDistribution && selectedCandidate
    ? selectedDistribution.states.filter((state) => selectedCandidate.winning_state_ids?.includes(state.settlement_state_id))
      .reduce((sum, state) => sum + state.raw_probability, 0) : Number.NaN;
  const derivedBaselineProbability = selectedDistribution && selectedCandidate
    ? selectedDistribution.states.filter((state) => selectedCandidate.winning_state_ids?.includes(state.settlement_state_id))
      .reduce((sum, state) => sum + state.baseline_probability, 0) : Number.NaN;
  if (!Number.isFinite(derivedRawProbability) || Math.abs(derivedRawProbability - prediction.model_probability_raw) > 1e-12) {
    distributionErrors.push('selected model_probability_raw does not equal the raw WIN-state aggregate');
  }
  if (!Number.isFinite(derivedBaselineProbability) || Math.abs(derivedBaselineProbability - prediction.baseline_probability) > 1e-12
    || Math.abs(prediction.baseline_probability_delta - (prediction.decision_probability - prediction.baseline_probability)) > 1e-12) {
    distributionErrors.push('baseline probability/delta does not reconcile to the selected WIN-state aggregate');
  }
  if (selectedDistribution?.calibration_evidence_id !== prediction.calibration_evidence_id
    || selectedCandidate?.forecast_distribution_id !== prediction.forecast_distribution_id) {
    distributionErrors.push('selected candidate/distribution/calibration foreign keys do not reconcile');
  }
  const probabilityChanged = Number.isFinite(prediction.model_probability_raw) && Number.isFinite(prediction.decision_probability)
    && Math.abs(prediction.model_probability_raw - prediction.decision_probability) > 1e-15;
  if ((probabilityChanged && prediction.calibration_status !== 'VALIDATED')
    || (!probabilityChanged && !['VALIDATED', 'IDENTITY_JUSTIFIED'].includes(prediction.calibration_status))) {
    distributionErrors.push('calibration status does not justify raw-to-decision mapping');
  }
  results.push(gate('GATE-PROB-001', distributions.length > 0 && distributionErrors.length === 0,
    distributionErrors.length ? distributionErrors.join('; ') : `${distributions.length} distribution(s) reconcile`));

  const coherenceErrors = validateLinkedMarketCoherence(packet.linked_market_relations ?? [], distributions);
  if (distributions.length > 1) {
    const jointIds = new Set(distributions.map((distribution) => distribution.joint_distribution_id).filter(nonBlank));
    if (jointIds.size !== 1 || distributions.some((distribution) => !nonBlank(distribution.joint_distribution_id))) {
      coherenceErrors.push('multiple linked distributions require one shared nonempty joint_distribution_id');
    }
    if ((packet.linked_market_relations ?? []).length === 0) coherenceErrors.push('multiple distributions require declared coherence relations');
  }
  results.push(gate('GATE-COHERENCE-001', coherenceErrors.length === 0,
    coherenceErrors.length ? coherenceErrors.join('; ') : 'declared linked-market constraints pass'));

  const components = packet.uncertainty_components ?? [];
  const uncertaintyErrors = [];
  const componentIds = new Set();
  const typesSeen = new Set();
  for (const component of components) {
    const missing = requireFields(component, [
      'uncertainty_component_id', 'uncertainty_set_id', 'prediction_id', 'uncertainty_type', 'uncertainty_status',
      'estimand', 'method_version', 'evidence_artifact_hash', 'material', 'decision_robust',
    ]);
    if (missing.length) uncertaintyErrors.push(`${component.uncertainty_component_id ?? '<missing>'}: missing ${missing.join('|')}`);
    const extra = extraFields(component, UNCERTAINTY_FIELDS);
    if (extra.length) uncertaintyErrors.push(`${component.uncertainty_component_id ?? '<missing>'}: extra ${extra.join('|')}`);
    if (componentIds.has(component.uncertainty_component_id)) uncertaintyErrors.push(`${component.uncertainty_component_id}: duplicate component ID`);
    componentIds.add(component.uncertainty_component_id);
    if (typesSeen.has(component.uncertainty_type)) uncertaintyErrors.push(`${component.uncertainty_type}: duplicate uncertainty assessment`);
    typesSeen.add(component.uncertainty_type);
    if (component.uncertainty_set_id !== prediction.uncertainty_set_id || component.prediction_id !== prediction.prediction_id) uncertaintyErrors.push(`${component.uncertainty_component_id}: uncertainty foreign key mismatch`);
    if (!controls.vocabularies.uncertainty_type.has(component.uncertainty_type)
      || !controls.vocabularies.uncertainty_status.has(component.uncertainty_status)) uncertaintyErrors.push(`${component.uncertainty_component_id}: invalid uncertainty vocabulary`);
    if (!isSha256(component.evidence_artifact_hash) || typeof component.material !== 'boolean' || typeof component.decision_robust !== 'boolean') {
      uncertaintyErrors.push(`${component.uncertainty_component_id}: evidence/material/robustness invalid`);
    }
    if (component.uncertainty_status === 'QUANTIFIED') {
      if (!(Number.isFinite(component.lower) && Number.isFinite(component.upper) && component.lower <= component.upper
        && Number.isFinite(component.level) && component.level > 0 && component.level < 1)) uncertaintyErrors.push(`${component.uncertainty_component_id}: quantified interval invalid`);
    }
    if (component.material === true && component.decision_robust !== true) uncertaintyErrors.push(`${component.uncertainty_component_id}: material uncertainty flips the decision`);
  }
  const missingAssessments = UNCERTAINTY_ASSESSMENTS.filter((type) => !components.some((component) => component.uncertainty_type === type));
  const materialUnknown = components.filter((component) => component.uncertainty_status === 'NOT_ESTIMABLE' && component.material !== false);
  const total = components.find((component) => component.uncertainty_type === 'TOTAL_PROBABILITY');
  const totalValid = total?.uncertainty_status === 'QUANTIFIED'
    && typeof total.lower === 'number' && typeof total.upper === 'number'
    && total.lower >= 0 && total.upper <= 1
    && total.lower <= prediction.decision_probability && prediction.decision_probability <= total.upper;
  results.push(gate('GATE-UNCERTAINTY-001', missingAssessments.length === 0 && materialUnknown.length === 0
    && uncertaintyErrors.length === 0 && totalValid,
  `missing=${missingAssessments.join('|') || 'none'}; material_not_estimable=${materialUnknown.length}; total_valid=${totalValid}; errors=${uncertaintyErrors.join('~') || 'none'}`));

  const priceApplicable = request.analysis_mode === 'PRICE_ENABLED';
  if (priceApplicable) {
    const price = packet.price_snapshot;
    const quoteCount = price?.outcome_quotes?.length ?? 0;
    const pricePublicationEnabled = controls.release.current_truth?.price_enabled_issue_supported === true;
    const priceValid = pricePublicationEnabled && (snapshot.price_evaluation_status === 'PRICE_UNAVAILABLE'
      ? packet.price_snapshot === null && prediction.market_price_snapshot_id == null && prediction.market_edge == null
        && prediction.expected_return == null && prediction.ev_lower == null && prediction.ev_upper == null
      : Boolean(price && price.complete_outcome_set === true && quoteCount >= 2 && isSha256(price.snapshot_hash)));
    results.push(gate('GATE-PRICE-001', priceValid,
      !pricePublicationEnabled ? 'PRICE_ENABLED ISSUE is disabled by the reviewed release manifest'
        : snapshot.price_evaluation_status === 'PRICE_UNAVAILABLE'
        ? 'price evaluation unavailable; forecast may remain ISSUE but all edge/EV fields must be null'
        : `complete price quotes=${quoteCount}`));
  } else {
    const priceNull = packet.price_snapshot === null
      && prediction.market_price_snapshot_id == null
      && prediction.market_edge == null
      && prediction.expected_return == null
      && snapshot.price_evaluation_status === 'NOT_REQUESTED';
    results.push(gate('GATE-PRICE-001', priceNull, 'RESEARCH_ONLY requires null price/edge/EV fields'));
  }

  const executionClaimsAbsent = prediction.stake == null && prediction.realized_yield == null
    && prediction.realized_pnl == null && prediction.clv == null;
  results.push(gate('GATE-EXECUTION-001', executionClaimsAbsent, 'decision packet cannot contain execution-only claims'));
  results.push(gate('GATE-SETTLEMENT-001', true, 'settlement is a later append-only record', false));
  results.push(gate('GATE-LEGACY-001', packet.migration_status === undefined && request.legacy_source !== true,
    'legacy or migrated rows cannot be issued'));

  return results;
}

export function validateDecisionPacket(packet, { controls, coverageRows, controlBundleHash }) {
  const results = validateBase(packet, controls);
  const decision = packet?.decision_snapshot?.decision;
  if (decision === 'PASS' || decision === 'WATCH') results.push(...validatePassOrWatch(packet, controls, coverageRows));
  else if (decision === 'ISSUE') results.push(...validateIssue(packet, controls, coverageRows, controlBundleHash));
  else results.push(gate('RUNTIME-DECISION-001', false, `unknown decision ${decision}`));

  const failures = results.filter((result) => result.status === 'FAIL');
  return {
    valid: failures.length === 0,
    decision,
    gate_results: results,
    failure_count: failures.length,
  };
}

export function finalizePacket(packet) {
  const copy = structuredClone(packet);
  if (!copy.decision_snapshot) throw new Error('decision_snapshot is required');
  copy.decision_snapshot.snapshot_hash = '0'.repeat(64);
  copy.decision_snapshot.snapshot_hash = computeSnapshotHash(copy);
  return copy;
}
