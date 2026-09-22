import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

import { hashFile } from '../src/canonical.mjs';
import {
  appendDecisionPacket,
  appendEvaluation,
  appendSettlement,
  initializeJournal,
  verifyJournal,
} from '../src/journal.mjs';
import { SCORING_SPEC_VERSION } from '../src/scoring.mjs';
import { makeValidIssueFixture } from './support/valid_issue_fixture.mjs';

const ROOT = resolve(import.meta.dirname, '..');
const SOURCE_HASH = '9'.repeat(64);

function temporaryRecordedIssue() {
  const directory = mkdtempSync(join(tmpdir(), 'sports-settlement-'));
  const journal = join(directory, 'journal.jsonl');
  const { packet, context } = makeValidIssueFixture();
  initializeJournal(journal);
  appendDecisionPacket(journal, packet, context);
  return { directory, journal, packet };
}

function settlement(packet, overrides = {}) {
  return {
    settlement_id: 'SETTLEMENT-VALID-1',
    settlement_version: 1,
    prediction_id: packet.prediction.prediction_id,
    snapshot_id: packet.decision_snapshot.snapshot_id,
    settled_at_utc: '2026-07-18T00:10:00.000Z',
    official_event_status: 'FINAL',
    observed_outcome_branch_id: 'STATE-HOME-WIN',
    numeric_outcome: null,
    grade: 'WIN',
    settlement_source_url: 'https://example.test/official-result/1',
    settlement_source_hash: SOURCE_HASH,
    source_fetched_at_utc: '2026-07-18T00:05:00.000Z',
    rules_applied: packet.request.settlement_convention_id,
    reviewer: 'settlement-test-reviewer',
    prior_settlement_id: null,
    prior_settlement_version: null,
    correction_reason: null,
    ...overrides,
  };
}

test('GATE-SETTLEMENT-001 appends an exact frozen-branch settlement and verifies the store', () => {
  const { directory, journal, packet } = temporaryRecordedIssue();
  try {
    const result = appendSettlement(journal, settlement(packet));
    assert.equal(result.record.record_type, 'SETTLEMENT');
    const report = verifyJournal(journal);
    assert.equal(report.valid, true, report.errors.join('; '));
    assert.equal(report.settlement_count, 1);
  } finally { rmSync(directory, { recursive: true, force: true }); }
});

test('settlement rejects a grade that conflicts with the frozen candidate-state mapping', () => {
  const { directory, journal, packet } = temporaryRecordedIssue();
  try {
    assert.throws(() => appendSettlement(journal, settlement(packet, { grade: 'LOSS' })), /conflicts with frozen candidate-state mapping/);
    assert.equal(verifyJournal(journal).settlement_count, 0);
  } finally { rmSync(directory, { recursive: true, force: true }); }
});

test('settlement payload is closed and cannot smuggle frozen forecast fields', () => {
  const { directory, journal, packet } = temporaryRecordedIssue();
  try {
    assert.throws(() => appendSettlement(journal, settlement(packet, { model_probability: 0.99 })), /unknown field/);
    assert.equal(verifyJournal(journal).settlement_count, 0);
  } finally { rmSync(directory, { recursive: true, force: true }); }
});

test('settlement rejects a series-only or otherwise ambiguous prediction reference', () => {
  const { directory, journal, packet } = temporaryRecordedIssue();
  try {
    const ambiguous = settlement(packet, {
      prediction_id: null,
      snapshot_id: null,
      forecast_series_id: packet.request.forecast_series_id,
    });
    assert.throws(() => appendSettlement(journal, ambiguous), /unknown field.*forecast_series_id/);
    assert.throws(() => appendSettlement(journal, settlement(packet, {
      prediction_id: null,
      snapshot_id: null,
    })), /settlement missing: prediction_id, snapshot_id/);
    assert.throws(() => appendSettlement(journal, settlement(packet, { settlement_version: 'latest' })), /positive integer/);
    assert.equal(verifyJournal(journal).settlement_count, 0);
  } finally { rmSync(directory, { recursive: true, force: true }); }
});

test('settlement correction requires exact prior lineage and preserves the frozen subject', () => {
  const { directory, journal, packet } = temporaryRecordedIssue();
  try {
    appendSettlement(journal, settlement(packet));
    const correction = settlement(packet, {
      settlement_version: 2,
      observed_outcome_branch_id: 'STATE-HOME-LOSS',
      grade: 'LOSS',
      prior_settlement_id: 'SETTLEMENT-VALID-1',
      prior_settlement_version: 1,
      correction_reason: 'Official result was corrected.',
      settlement_source_url: 'https://example.test/official-result/1-correction',
      settlement_source_hash: 'a'.repeat(64),
      settled_at_utc: '2026-07-18T01:10:00.000Z',
      source_fetched_at_utc: '2026-07-18T01:05:00.000Z',
    });
    assert.throws(() => appendSettlement(journal, { ...correction, prior_settlement_version: 99 }), /exact immediate prior/);
    assert.throws(() => appendSettlement(journal, { ...correction, correction_reason: null }), /exact immediate prior.*give a reason/);
    appendSettlement(journal, correction);
    assert.equal(verifyJournal(journal).settlement_count, 2);
  } finally { rmSync(directory, { recursive: true, force: true }); }
});

test('evaluation derives proper scores once and blocks a duplicate natural key', () => {
  const { directory, journal, packet } = temporaryRecordedIssue();
  try {
    appendSettlement(journal, settlement(packet));
    const request = {
      evaluation_id: 'EVALUATION-VALID-1',
      prediction_id: packet.prediction.prediction_id,
      settlement_id: 'SETTLEMENT-VALID-1',
      settlement_version: 1,
      scoring_spec_version: SCORING_SPEC_VERSION,
      scoring_code_hash: hashFile(resolve(ROOT, 'src/scoring.mjs')),
      evaluated_at_utc: '2026-07-18T00:20:00.000Z',
      report_artifact_hash: null,
    };
    const first = appendEvaluation(journal, request).record.payload;
    assert.ok(Math.abs(first.brier_loss - 0.16) < 1e-12);
    assert.ok(Math.abs(first.log_loss - -Math.log(0.60)) < 1e-12);
    assert.ok(Math.abs(first.baseline_brier_loss - 0.25) < 1e-12);
    assert.ok(first.brier_score_delta > 0);
    assert.throws(() => appendEvaluation(journal, { ...request, evaluation_id: 'EVALUATION-VALID-2' }), /duplicate evaluation natural key/);
    assert.equal(verifyJournal(journal).evaluation_count, 1);
  } finally { rmSync(directory, { recursive: true, force: true }); }
});

test('settlement rejects attempts to carry mutable probability model or rationale fields', () => {
  const { directory, journal, packet } = temporaryRecordedIssue();
  try {
    for (const [field, value] of [
      ['decision_probability', 0.99],
      ['model_id', 'REWRITTEN_MODEL'],
      ['rationale', 'retrospective rewrite'],
    ]) {
      assert.throws(() => appendSettlement(journal, settlement(packet, { [field]: value })), new RegExp(`unknown field.*${field}`));
    }
    assert.equal(verifyJournal(journal).settlement_count, 0);
  } finally { rmSync(directory, { recursive: true, force: true }); }
});
test.todo('VOID settlement is recorded as EXCLUDED_VOID rather than ELIGIBLE_V3 and scored');
test('FINAL plus PENDING is rejected by an explicit status-grade matrix', () => {
  const { directory, journal, packet } = temporaryRecordedIssue();
  try {
    assert.throws(() => appendSettlement(journal, settlement(packet, {
      grade: 'PENDING',
      settlement_source_url: null,
      settlement_source_hash: null,
      source_fetched_at_utc: null,
    })), /FINAL event status cannot have a PENDING grade/);
    assert.equal(verifyJournal(journal).settlement_count, 0);
  } finally { rmSync(directory, { recursive: true, force: true }); }
});
test.todo('phase-market settlement cannot infer a phase result from a full-event result');
