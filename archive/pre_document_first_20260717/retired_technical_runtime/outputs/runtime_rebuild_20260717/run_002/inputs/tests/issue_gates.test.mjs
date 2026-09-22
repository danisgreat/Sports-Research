import test from 'node:test';
import assert from 'node:assert/strict';

import { compareCanonicalStrings, hashObject } from '../src/canonical.mjs';
import { validateDecisionPacket } from '../src/packet.mjs';
import { gateStatus, makeValidIssueFixture, mutateAndFinalize } from './support/valid_issue_fixture.mjs';

const APPLICABLE_ISSUE_GATES = [
  'GATE-AUTH-001',
  'GATE-CONTRACT-001',
  'GATE-MODE-001',
  'GATE-CUTOFF-001',
  'GATE-SOURCE-001',
  'GATE-UNIVERSE-001',
  'GATE-MODEL-001',
  'GATE-TEST-001',
  'GATE-PROB-001',
  'GATE-COHERENCE-001',
  'GATE-UNCERTAINTY-001',
  'GATE-PRICE-001',
  'GATE-EXECUTION-001',
  'GATE-LEGACY-001',
];

function validateMutation(mutatePacket, mutateContext = () => {}) {
  const { packet, context } = makeValidIssueFixture();
  mutateContext(context);
  const mutated = mutateAndFinalize(packet, mutatePacket);
  return validateDecisionPacket(mutated, context);
}

function refreshUniverseHash(packet) {
  const universe = packet.candidate_universe;
  universe.candidate_count = universe.candidates.length;
  universe.universe_hash = hashObject({
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
    candidates: [...universe.candidates]
      .sort((left, right) => compareCanonicalStrings(left.candidate_id, right.candidate_id)),
  });
}

test('ISSUE-HAPPY-001 synthetic ACTIVE RESEARCH_ONLY packet passes every applicable packet gate', () => {
  const { packet, context } = makeValidIssueFixture();
  const report = validateDecisionPacket(packet, context);
  assert.equal(report.valid, true, JSON.stringify(report.gate_results, null, 2));
  assert.equal(report.decision, 'ISSUE');
  for (const gateId of APPLICABLE_ISSUE_GATES) assert.equal(gateStatus(report, gateId), 'PASS', gateId);
  assert.equal(gateStatus(report, 'GATE-SETTLEMENT-001'), 'NOT_APPLICABLE');
});

test('GATE-AUTH-001 rejects an ACTIVE packet under a suspended release manifest', () => {
  const report = validateMutation(() => {}, (context) => {
    context.controls.release.release_mode = 'SUSPENDED';
    context.controls.release.operational_status = 'SUSPENDED_NO_ACTIVE_MODELS';
    context.controls.release.activation_authorized = false;
    context.controls.release.expected_active_coverage_count = 0;
    context.controls.release.current_truth.active_models = 0;
    context.controls.release.current_truth.authorized_numeric_forecasts = false;
  });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-AUTH-001'), 'FAIL');
  assert.equal(gateStatus(report, 'GATE-CONTRACT-001'), 'PASS');
});

test('GATE-CONTRACT-001 fails when the otherwise-valid ISSUE loses its exact ACTIVE contract', () => {
  const report = validateMutation(() => {}, (context) => { context.controls.contracts = []; });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-CONTRACT-001'), 'FAIL');
  assert.equal(gateStatus(report, 'GATE-MODEL-001'), 'PASS');
});

test('GATE-CUTOFF-001 fails when a pregame ISSUE freezes at the event start', () => {
  const report = validateMutation((packet) => {
    packet.request.event_start_utc = packet.decision_snapshot.frozen_at_utc;
  });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-CUTOFF-001'), 'FAIL');
  assert.equal(gateStatus(report, 'GATE-UNIVERSE-001'), 'PASS');
});

test('GATE-UNIVERSE-001 fails on an isolated candidate_count mismatch', () => {
  const report = validateMutation((packet) => { packet.candidate_universe.candidate_count = 2; });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-UNIVERSE-001'), 'FAIL');
  assert.equal(gateStatus(report, 'GATE-SOURCE-001'), 'PASS');
});

test('GATE-UNIVERSE-001 rejects both zero and multiple primary questions with reconciled hashes', () => {
  const zeroPrimary = validateMutation((packet) => {
    packet.candidate_universe.candidates[0].is_primary_question = false;
    refreshUniverseHash(packet);
  });
  assert.equal(gateStatus(zeroPrimary, 'GATE-UNIVERSE-001'), 'FAIL');

  const multiplePrimary = validateMutation((packet) => {
    const second = structuredClone(packet.candidate_universe.candidates[0]);
    Object.assign(second, {
      candidate_id: 'CANDIDATE-AWAY',
      selection: 'SYNTHETIC_AWAY',
      selected_for_issue: false,
      candidate_status: 'REJECTED_PREMODEL',
      rejection_reason: 'Synthetic second primary used to prove rejection.',
      probability_generation_status: 'NOT_RUN',
      forecast_distribution_id: null,
      winning_state_ids: [],
    });
    packet.candidate_universe.candidates.push(second);
    refreshUniverseHash(packet);
  });
  assert.equal(gateStatus(multiplePrimary, 'GATE-UNIVERSE-001'), 'FAIL');
  assert.equal(gateStatus(multiplePrimary, 'GATE-PROB-001'), 'PASS');
});

test('GATE-SOURCE-001 rejects an observation known one millisecond after cutoff', () => {
  const report = validateMutation((packet) => {
    packet.source_packet.observations[0].known_at_utc = '2026-07-16T12:00:00.001Z';
  });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-SOURCE-001'), 'FAIL');
  // Current runtime classifies observation timing inside the source gate; the
  // traceability table keeps the broader cutoff requirement PARTIAL.
  assert.equal(gateStatus(report, 'GATE-CUTOFF-001'), 'PASS');
});

test('GATE-SOURCE-001 rejects a production observation fetched after the frozen snapshot', () => {
  const report = validateMutation((packet) => {
    packet.source_packet.observations[0].fetched_at_utc = '2026-07-16T12:00:00.001Z';
    const { source_packet_hash: _priorHash, ...hashMaterial } = packet.source_packet;
    packet.source_packet.source_packet_hash = hashObject(hashMaterial);
  });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-SOURCE-001'), 'FAIL');
  assert.match(report.gate_results.find((row) => row.gate_id === 'GATE-SOURCE-001').detail, /fetched after freeze/);
  assert.equal(gateStatus(report, 'GATE-CUTOFF-001'), 'PASS');
});

test('GATE-SOURCE-001 rejects a historical later fetch without versioned as-of evidence', () => {
  const report = validateMutation((packet) => {
    packet.source_packet.observations[0].historical_reconstruction = true;
    packet.source_packet.observations[0].fetched_at_utc = '2026-07-16T12:00:00.001Z';
    const { source_packet_hash: _priorHash, ...hashMaterial } = packet.source_packet;
    packet.source_packet.source_packet_hash = hashObject(hashMaterial);
  });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-SOURCE-001'), 'FAIL');
  assert.match(report.gate_results.find((row) => row.gate_id === 'GATE-SOURCE-001').detail, /lacks versioned as-of evidence/);
});

test('GATE-MODEL-001 rejects SHADOW model status with all other evidence intact', () => {
  const report = validateMutation(() => {}, (context) => { context.controls.modelRegistry[0].status = 'SHADOW'; });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-MODEL-001'), 'FAIL');
  assert.equal(gateStatus(report, 'GATE-TEST-001'), 'PASS');
});

test('GATE-TEST-001 rejects missing later prospective-shadow evidence', () => {
  const report = validateMutation(() => {}, (context) => {
    context.controls.testEvaluations = context.controls.testEvaluations.filter((row) => row.test_role !== 'PROSPECTIVE_SHADOW');
  });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-TEST-001'), 'FAIL');
  assert.equal(gateStatus(report, 'GATE-MODEL-001'), 'PASS');
});

test('GATE-PROB-001 rejects an out-of-tolerance probability vector', () => {
  const report = validateMutation((packet) => {
    const distribution = packet.forecast_distributions[0];
    const winningState = distribution.states.find((state) => state.settlement_state_id === 'STATE-HOME-WIN');
    winningState.raw_probability = 0.61;
    winningState.decision_probability = 0.61;
    packet.prediction.model_probability_raw = 0.61;
    packet.prediction.decision_probability = 0.61;
    packet.prediction.baseline_probability_delta = 0.11;
    const { distribution_hash: _priorHash, ...hashMaterial } = distribution;
    distribution.distribution_hash = hashObject(hashMaterial);
  });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-PROB-001'), 'FAIL');
  assert.equal(gateStatus(report, 'GATE-UNCERTAINTY-001'), 'PASS');
});

test('GATE-UNCERTAINTY-001 rejects a material NOT_ESTIMABLE component', () => {
  const report = validateMutation((packet) => {
    packet.uncertainty_components[0].uncertainty_status = 'NOT_ESTIMABLE';
  });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-UNCERTAINTY-001'), 'FAIL');
  assert.equal(gateStatus(report, 'GATE-PROB-001'), 'PASS');
});

test('GATE-PRICE-001 rejects an EV claim in RESEARCH_ONLY mode', () => {
  const report = validateMutation((packet) => { packet.prediction.expected_return = 0.05; });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-PRICE-001'), 'FAIL');
  assert.equal(gateStatus(report, 'GATE-EXECUTION-001'), 'PASS');
});

test('GATE-EXECUTION-001 rejects a stake without an execution record', () => {
  const report = validateMutation((packet) => { packet.prediction.stake = 1; });
  assert.equal(report.valid, false);
  assert.equal(gateStatus(report, 'GATE-EXECUTION-001'), 'FAIL');
  assert.equal(gateStatus(report, 'GATE-PRICE-001'), 'PASS');
});

test.todo('GATE-MODE-001 has an isolated invalid-mode mutation without a second schema/vocabulary failure');
test.todo('GATE-PRICE-001 recomputes and validates a complete PRICE_ENABLED packet');
test.todo('GATE-LEGACY-001 rejects legacy provenance without relying on an unknown-field failure');
