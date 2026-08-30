import { closeSync, existsSync, fsyncSync, mkdirSync, openSync, readFileSync, renameSync, unlinkSync, writeFileSync, writeSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { canonicalStringify, computeSnapshotHash, hashFile, hashObject, isSha256, parseJsonStrict, parseUtc, readJson, utcNow } from './canonical.mjs';
import { validateDecisionPacket } from './packet.mjs';
import { brierLoss, logLoss, SCORING_SPEC_VERSION } from './scoring.mjs';
import { newId } from './canonical.mjs';

export const JOURNAL_VERSION = 'SPORTS_APPEND_ONLY_JOURNAL_V1';
export const GENESIS_HASH = '0'.repeat(64);
export const DEFAULT_JOURNAL = 'runtime/store/journal.jsonl';
const RECORD_TYPES = new Set(['DECISION_PACKET', 'SETTLEMENT', 'EVALUATION']);
const OFFICIAL_EVENT_STATUSES = new Set(['FINAL', 'POSTPONED', 'ABANDONED', 'SUSPENDED', 'CANCELLED', 'UNDER_REVIEW']);
const SETTLEMENT_GRADES = new Set(['WIN', 'LOSS', 'PUSH', 'VOID', 'UNGRADABLE', 'PENDING']);
const SCORING_CODE_HASH = hashFile(new URL('./scoring.mjs', import.meta.url));
const SETTLEMENT_FIELDS = new Set([
  'settlement_id', 'settlement_version', 'prediction_id', 'snapshot_id', 'settled_at_utc', 'official_event_status',
  'observed_outcome_branch_id', 'numeric_outcome', 'grade', 'settlement_source_url', 'settlement_source_hash',
  'source_fetched_at_utc', 'secondary_source_url', 'rules_applied', 'reviewer', 'prior_settlement_id',
  'prior_settlement_version', 'correction_reason',
]);
const EVALUATION_REQUEST_FIELDS = new Set([
  'evaluation_id', 'prediction_id', 'settlement_id', 'settlement_version', 'scoring_spec_version',
  'scoring_code_hash', 'evaluated_at_utc', 'report_artifact_hash',
]);

function anchorPath(journalPath) {
  return resolve(dirname(resolve(journalPath)), 'head_anchor.json');
}

function writeAnchor(journalPath, verification) {
  const path = anchorPath(journalPath);
  const anchor = {
    anchor_version: 'SPORTS_JOURNAL_HEAD_ANCHOR_V1',
    record_count: verification.record_count,
    head_hash: verification.head_hash,
    anchored_at_utc: utcNow(),
  };
  anchor.anchor_hash = hashObject(anchor);
  const temporary = `${path}.tmp-${process.pid}-${Date.now()}`;
  writeFileSync(temporary, `${JSON.stringify(anchor, null, 2)}\n`, { encoding: 'utf8', flag: 'wx' });
  renameSync(temporary, path);
  return anchor;
}

function recordMaterial(record) {
  return {
    journal_version: record.journal_version,
    sequence: record.sequence,
    record_type: record.record_type,
    recorded_at_utc: record.recorded_at_utc,
    previous_record_hash: record.previous_record_hash,
    payload_hash: record.payload_hash,
    payload: record.payload,
  };
}

export function readJournal(path = DEFAULT_JOURNAL) {
  if (!existsSync(path)) return [];
  const text = readFileSync(path, 'utf8');
  if (!text.trim()) return [];
  return text.split(/\r?\n/).filter(Boolean).map((line, index) => {
    try { return parseJsonStrict(line, `journal line ${index + 1}`); } catch (error) {
      throw new Error(`journal line ${index + 1}: ${error.message}`);
    }
  });
}

export function verifyJournal(path = DEFAULT_JOURNAL, { checkAnchor = true } = {}) {
  const errors = [];
  const records = readJournal(path);
  let previousHash = GENESIS_HASH;
  const snapshotIds = new Set();
  const predictionIds = new Set();
  const settlementKeys = new Set();
  const evaluationIds = new Set();

  records.forEach((record, index) => {
    const line = index + 1;
    if (record.journal_version !== JOURNAL_VERSION) errors.push(`line ${line}: wrong journal version`);
    if (record.sequence !== line) errors.push(`line ${line}: sequence=${record.sequence}; expected ${line}`);
    if (record.previous_record_hash !== previousHash) errors.push(`line ${line}: hash-chain predecessor mismatch`);
    if (!isSha256(record.payload_hash) || record.payload_hash !== hashObject(record.payload)) {
      errors.push(`line ${line}: payload hash mismatch`);
    }
    const expectedRecordHash = hashObject(recordMaterial(record));
    if (!isSha256(record.record_hash) || record.record_hash !== expectedRecordHash) {
      errors.push(`line ${line}: record hash mismatch`);
    }
    try { parseUtc(record.recorded_at_utc, `line ${line}.recorded_at_utc`); } catch (error) { errors.push(error.message); }

    if (record.record_type === 'DECISION_PACKET') {
      const packet = record.payload?.packet;
      const snapshotId = packet?.decision_snapshot?.snapshot_id;
      const predictionId = packet?.prediction?.prediction_id;
      if (!snapshotId) errors.push(`line ${line}: decision packet lacks snapshot_id`);
      else if (snapshotIds.has(snapshotId)) errors.push(`line ${line}: duplicate snapshot_id ${snapshotId}`);
      snapshotIds.add(snapshotId);
      if (predictionId) {
        if (predictionIds.has(predictionId)) errors.push(`line ${line}: duplicate prediction_id ${predictionId}`);
        predictionIds.add(predictionId);
      }
      const expectedSnapshotHash = packet ? computeSnapshotHash(packet) : null;
      if (packet?.decision_snapshot?.snapshot_hash !== expectedSnapshotHash) {
        errors.push(`line ${line}: snapshot hash mismatch`);
      }
      if (record.payload?.validation_report?.valid !== true) errors.push(`line ${line}: invalid decision packet was recorded`);
    } else if (record.record_type === 'SETTLEMENT') {
      const settlement = record.payload;
      const key = `${settlement.settlement_id}:${settlement.settlement_version}`;
      if (settlementKeys.has(key)) errors.push(`line ${line}: duplicate settlement version ${key}`);
      settlementKeys.add(key);
      if (!predictionIds.has(settlement.prediction_id)) errors.push(`line ${line}: settlement references unknown prior prediction`);
    } else if (record.record_type === 'EVALUATION') {
      if (evaluationIds.has(record.payload.evaluation_id)) errors.push(`line ${line}: duplicate evaluation_id ${record.payload.evaluation_id}`);
      evaluationIds.add(record.payload.evaluation_id);
      if (!predictionIds.has(record.payload.prediction_id)) errors.push(`line ${line}: evaluation references unknown prior prediction`);
    } else {
      errors.push(`line ${line}: unknown record_type ${record.record_type}`);
    }
    previousHash = record.record_hash;
  });

  if (checkAnchor) {
    if (!existsSync(anchorPath(path))) errors.push('head anchor is missing');
    else try {
      const anchor = readJson(anchorPath(path));
      const storedAnchorHash = anchor.anchor_hash;
      delete anchor.anchor_hash;
      if (storedAnchorHash !== hashObject(anchor)) errors.push('head anchor hash mismatch');
      if (anchor.record_count !== records.length) errors.push(`head anchor record_count=${anchor.record_count}; journal=${records.length}`);
      if (anchor.head_hash !== (records.at(-1)?.record_hash ?? GENESIS_HASH)) errors.push('head anchor does not match journal head');
    } catch (error) {
      errors.push(`head anchor unreadable: ${error.message}`);
    }
  }

  return {
    valid: errors.length === 0,
    record_count: records.length,
    decision_count: records.filter((record) => record.record_type === 'DECISION_PACKET').length,
    settlement_count: records.filter((record) => record.record_type === 'SETTLEMENT').length,
    evaluation_count: records.filter((record) => record.record_type === 'EVALUATION').length,
    head_hash: records.at(-1)?.record_hash ?? GENESIS_HASH,
    errors,
  };
}

function withLock(journalPath, callback) {
  const lockPath = `${resolve(journalPath)}.lock`;
  mkdirSync(dirname(resolve(journalPath)), { recursive: true });
  let descriptor;
  try {
    descriptor = openSync(lockPath, 'wx');
  } catch {
    throw new Error(`journal is locked: ${lockPath}`);
  }
  try { return callback(); } finally {
    closeSync(descriptor);
    unlinkSync(lockPath);
  }
}

export function initializeJournal(path = DEFAULT_JOURNAL) {
  const absolute = resolve(path);
  mkdirSync(dirname(absolute), { recursive: true });
  const created = !existsSync(absolute);
  if (created) writeFileSync(absolute, '', { encoding: 'utf8', flag: 'wx' });
  const verification = verifyJournal(absolute, { checkAnchor: false });
  if (!existsSync(anchorPath(absolute))) {
    if (!created) throw new Error('existing journal has no anchor; explicit externally verified recovery is required');
    writeAnchor(absolute, verification);
  }
  return verifyJournal(absolute);
}

function appendJournalRecord(path, recordType, payload, { semanticPreflight } = {}) {
  return withLock(path, () => {
    if (!RECORD_TYPES.has(recordType)) throw new Error(`unsupported journal record type ${recordType}`);
    const before = verifyJournal(path);
    if (!before.valid) throw new Error(`journal verification failed before append: ${before.errors.join('; ')}`);
    const existingRecords = readJournal(path);
    let effectivePayload = payload;
    if (semanticPreflight) {
      const replacementPayload = semanticPreflight(existingRecords);
      if (replacementPayload !== undefined) effectivePayload = replacementPayload;
    }
    const record = {
      journal_version: JOURNAL_VERSION,
      sequence: before.record_count + 1,
      record_type: recordType,
      recorded_at_utc: utcNow(),
      previous_record_hash: before.head_hash,
      payload_hash: hashObject(effectivePayload),
      payload: effectivePayload,
    };
    record.record_hash = hashObject(recordMaterial(record));
    if (record.previous_record_hash !== before.head_hash || record.sequence !== before.record_count + 1
      || record.payload_hash !== hashObject(effectivePayload) || record.record_hash !== hashObject(recordMaterial(record))) {
      throw new Error('prospective journal record failed internal verification');
    }
    const descriptor = openSync(path, 'a');
    try {
      writeSync(descriptor, `${canonicalStringify(record)}\n`, null, 'utf8');
      fsyncSync(descriptor);
    } finally {
      closeSync(descriptor);
    }
    const unanchored = verifyJournal(path, { checkAnchor: false });
    if (!unanchored.valid) throw new Error(`journal verification failed after append: ${unanchored.errors.join('; ')}`);
    writeAnchor(path, unanchored);
    const after = verifyJournal(path);
    if (!after.valid) throw new Error(`journal verification failed after append: ${after.errors.join('; ')}`);
    return { record, verification: after };
  });
}

export function recoverJournalAnchor(path, { expectedHeadHash, expectedRecordCount }) {
  const verification = verifyJournal(path, { checkAnchor: false });
  if (!verification.valid) throw new Error(`journal chain is invalid: ${verification.errors.join('; ')}`);
  if (verification.head_hash !== expectedHeadHash || verification.record_count !== expectedRecordCount) {
    throw new Error('journal does not match the externally retained expected head/count');
  }
  writeAnchor(path, verification);
  return verifyJournal(path);
}

export function appendDecisionPacket(path, packet, validationContext) {
  return appendJournalRecord(path, 'DECISION_PACKET', null, {
    semanticPreflight(existing) {
      const validationReport = validateDecisionPacket(packet, validationContext);
      if (!validationReport.valid) throw new Error(`refusing invalid packet: ${validationReport.gate_results.filter((row) => row.status === 'FAIL').map((row) => row.gate_id).join(', ')}`);
      const snapshotId = packet.decision_snapshot.snapshot_id;
      const predictionId = packet.prediction?.prediction_id;
      for (const record of existing.filter((candidate) => candidate.record_type === 'DECISION_PACKET')) {
        if (record.payload.packet.decision_snapshot.snapshot_id === snapshotId) throw new Error(`duplicate snapshot_id ${snapshotId}`);
        if (predictionId && record.payload.packet.prediction?.prediction_id === predictionId) throw new Error(`duplicate prediction_id ${predictionId}`);
      }
      if (!isSha256(validationContext.controlBundleHash) || !validationContext.controlHashes
        || Object.keys(validationContext.controlHashes).length === 0) throw new Error('decision append requires a complete hashed runtime control bundle');
      return {
        packet,
        validation_report: validationReport,
        control_bundle_hash: validationContext.controlBundleHash,
        control_hashes: validationContext.controlHashes,
      };
    },
  });
}

export function appendSettlement(path, settlement) {
  return appendJournalRecord(path, 'SETTLEMENT', settlement, {
    semanticPreflight(records) {
      const extra = Object.keys(settlement).filter((field) => !SETTLEMENT_FIELDS.has(field));
      if (extra.length) throw new Error(`settlement contains unknown field(s): ${extra.join(', ')}`);
      const required = [
        'settlement_id', 'settlement_version', 'prediction_id', 'snapshot_id', 'settled_at_utc', 'official_event_status',
        'grade', 'rules_applied', 'reviewer',
      ];
      const missing = required.filter((field) => settlement[field] === null || settlement[field] === undefined || settlement[field] === '');
      if (missing.length) throw new Error(`settlement missing: ${missing.join(', ')}`);
      if (!OFFICIAL_EVENT_STATUSES.has(settlement.official_event_status)) throw new Error('official_event_status is not controlled');
      if (!SETTLEMENT_GRADES.has(settlement.grade)) throw new Error('grade is not controlled');
      if (settlement.numeric_outcome !== null && settlement.numeric_outcome !== undefined
        && !Number.isFinite(settlement.numeric_outcome)) throw new Error('numeric_outcome must be finite or null');
      if (settlement.secondary_source_url && !/^https:\/\//i.test(settlement.secondary_source_url)) throw new Error('secondary_source_url must use HTTPS');
      if (settlement.official_event_status === 'FINAL' && settlement.grade === 'PENDING') throw new Error('FINAL event status cannot have a PENDING grade');
      if (['POSTPONED', 'SUSPENDED', 'UNDER_REVIEW'].includes(settlement.official_event_status)
        && !['PENDING', 'UNGRADABLE'].includes(settlement.grade)) {
        throw new Error(`${settlement.official_event_status} cannot be graded ${settlement.grade}`);
      }
      const settledTime = parseUtc(settlement.settled_at_utc, 'settled_at_utc');
      if (!Number.isInteger(settlement.settlement_version) || settlement.settlement_version < 1) throw new Error('settlement_version must be a positive integer');
      if (settlement.grade !== 'PENDING') {
        if (!settlement.settlement_source_url || !/^https:\/\//i.test(settlement.settlement_source_url)
          || !settlement.source_fetched_at_utc || !isSha256(settlement.settlement_source_hash)) {
          throw new Error('non-pending settlement requires a direct HTTPS source URL, fetch time and immutable source hash');
        }
        if (parseUtc(settlement.source_fetched_at_utc, 'source_fetched_at_utc') > settledTime) throw new Error('source_fetched_at_utc cannot be after settled_at_utc');
      }
      const packetRecord = records.find((record) => record.record_type === 'DECISION_PACKET'
        && record.payload.packet.prediction?.prediction_id === settlement.prediction_id);
      if (!packetRecord) throw new Error(`prediction_id ${settlement.prediction_id} does not exist`);
      const packet = packetRecord.payload.packet;
      if (packet.decision_snapshot.snapshot_id !== settlement.snapshot_id) throw new Error('settlement snapshot_id does not match prediction');
      if (settlement.rules_applied !== packet.request.settlement_convention_id) throw new Error('rules_applied does not match frozen settlement convention');
      if (packet.request.event_start_utc && settledTime < parseUtc(packet.request.event_start_utc, 'event_start_utc')) {
        throw new Error('settlement cannot predate event start');
      }
      const distribution = packet.forecast_distributions.find((item) => item.forecast_distribution_id === packet.prediction.forecast_distribution_id);
      const branchIds = new Set((distribution?.states ?? []).map((state) => state.settlement_state_id));
      if (!['PENDING', 'UNGRADABLE'].includes(settlement.grade) && !branchIds.has(settlement.observed_outcome_branch_id)) {
        throw new Error('observed_outcome_branch_id is absent from the frozen distribution');
      }
      if (!['PENDING', 'UNGRADABLE'].includes(settlement.grade)) {
        const observedState = distribution.states.find((state) => state.settlement_state_id === settlement.observed_outcome_branch_id);
        const selectedCandidate = packet.candidate_universe.candidates.find((candidate) => candidate.candidate_id === packet.prediction.selected_candidate_id);
        const expectedGrade = selectedCandidate.winning_state_ids.includes(observedState.settlement_state_id)
          ? 'WIN'
          : (observedState.branch_type === 'PUSH' ? 'PUSH' : (observedState.branch_type === 'VOID' ? 'VOID' : 'LOSS'));
        if (settlement.grade !== expectedGrade) throw new Error(`settlement grade ${settlement.grade} conflicts with frozen candidate-state mapping ${expectedGrade}`);
      }
      const prior = records.filter((record) => record.record_type === 'SETTLEMENT' && record.payload.settlement_id === settlement.settlement_id);
      const anotherChain = records.find((record) => record.record_type === 'SETTLEMENT'
        && record.payload.prediction_id === settlement.prediction_id && record.payload.settlement_id !== settlement.settlement_id);
      if (anotherChain) throw new Error(`prediction already belongs to settlement chain ${anotherChain.payload.settlement_id}`);
      if (settlement.settlement_version !== prior.length + 1) throw new Error(`next settlement_version must be ${prior.length + 1}`);
      if (settlement.settlement_version > 1) {
        const immediatePrior = prior.at(-1)?.payload;
        if (settlement.prior_settlement_id !== immediatePrior?.settlement_id
          || settlement.prior_settlement_version !== immediatePrior?.settlement_version || !settlement.correction_reason) {
          throw new Error('settlement correction must link the exact immediate prior version and give a reason');
        }
        if (settlement.prediction_id !== immediatePrior.prediction_id || settlement.snapshot_id !== immediatePrior.snapshot_id
          || settlement.rules_applied !== immediatePrior.rules_applied) {
          throw new Error('settlement correction cannot change prediction, snapshot or frozen rules');
        }
      }
      return structuredClone(settlement);
    },
  });
}

export function appendEvaluation(path, request) {
  return appendJournalRecord(path, 'EVALUATION', null, {
    semanticPreflight(records) {
      const extra = Object.keys(request).filter((field) => !EVALUATION_REQUEST_FIELDS.has(field));
      if (extra.length) throw new Error(`evaluation request contains unknown field(s): ${extra.join(', ')}`);
      const packetRecord = records.find((record) => record.record_type === 'DECISION_PACKET'
        && record.payload.packet.prediction?.prediction_id === request.prediction_id);
      if (!packetRecord) throw new Error(`prediction_id ${request.prediction_id} does not exist`);
      const settlementRecord = records.find((record) => record.record_type === 'SETTLEMENT'
        && record.payload.settlement_id === request.settlement_id
        && record.payload.settlement_version === request.settlement_version);
      if (!settlementRecord) throw new Error('exact settlement version does not exist');
      if (settlementRecord.payload.prediction_id !== request.prediction_id) throw new Error('settlement belongs to a different prediction');
      if (['PENDING', 'UNGRADABLE'].includes(settlementRecord.payload.grade)) throw new Error('pending/ungradable settlement cannot be scored');
      const packet = packetRecord.payload.packet;
      const distribution = packet.forecast_distributions.find((item) => item.forecast_distribution_id === packet.prediction.forecast_distribution_id);
      const observedIndex = distribution.states.findIndex((state) => state.settlement_state_id === settlementRecord.payload.observed_outcome_branch_id);
      if (observedIndex < 0) throw new Error('observed branch is absent from distribution');
      const probabilities = distribution.states.map((state) => state.decision_probability);
      const baseline = distribution.states.map((state) => state.baseline_probability);
      const modelBrier = brierLoss(probabilities, observedIndex);
      const baselineBrier = brierLoss(baseline, observedIndex);
      const modelLog = logLoss(probabilities, observedIndex);
      const baselineLog = logLoss(baseline, observedIndex);
      const evaluation = {
        evaluation_id: request.evaluation_id ?? newId('EVAL'),
        prediction_id: request.prediction_id,
        snapshot_id: packet.decision_snapshot.snapshot_id,
        settlement_id: request.settlement_id,
        settlement_version: request.settlement_version,
        scoring_spec_version: request.scoring_spec_version,
        scoring_code_hash: request.scoring_code_hash,
        evaluated_at_utc: request.evaluated_at_utc ?? utcNow(),
        eligibility: 'ELIGIBLE_V3',
        exclusion_reason: null,
        forecast_distribution_id: distribution.forecast_distribution_id,
        observed_outcome_branch_id: settlementRecord.payload.observed_outcome_branch_id,
        brier_loss: modelBrier,
        log_loss: modelLog,
        baseline_brier_loss: baselineBrier,
        baseline_log_loss: baselineLog,
        brier_score_delta: baselineBrier - modelBrier,
        log_score_delta: baselineLog - modelLog,
        event_cluster_id: packet.request.event_id,
        report_artifact_hash: request.report_artifact_hash ?? null,
      };
      parseUtc(evaluation.evaluated_at_utc, 'evaluated_at_utc');
      if (evaluation.scoring_spec_version !== SCORING_SPEC_VERSION || evaluation.scoring_code_hash !== SCORING_CODE_HASH) {
        throw new Error(`scoring spec/code must exactly match ${SCORING_SPEC_VERSION}/${SCORING_CODE_HASH}`);
      }
      if (evaluation.report_artifact_hash !== null && !isSha256(evaluation.report_artifact_hash)) {
        throw new Error('report_artifact_hash must be null or SHA-256');
      }
      if (records.some((record) => record.record_type === 'EVALUATION' && record.payload.evaluation_id === evaluation.evaluation_id)) {
        throw new Error(`duplicate evaluation_id ${evaluation.evaluation_id}`);
      }
      if (records.some((record) => record.record_type === 'EVALUATION'
        && record.payload.prediction_id === evaluation.prediction_id
        && record.payload.settlement_id === evaluation.settlement_id
        && record.payload.settlement_version === evaluation.settlement_version
        && record.payload.scoring_spec_version === evaluation.scoring_spec_version
        && record.payload.scoring_code_hash === evaluation.scoring_code_hash)) {
        throw new Error('duplicate evaluation natural key for prediction/settlement/scoring version');
      }
      return evaluation;
    },
  });
}
