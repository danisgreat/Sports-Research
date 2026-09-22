import test from 'node:test';
import assert from 'node:assert/strict';
import { resolve } from 'node:path';
import { loadCoverageRegistry } from '../src/coverage.mjs';
import { finalizePacket, loadMachineControls, validateDecisionPacket } from '../src/packet.mjs';
import { createInitialDecisionPacket } from '../src/workflow.mjs';

const ROOT = resolve(import.meta.dirname, '..');
const context = {
  controls: loadMachineControls(ROOT.replaceAll('\\', '/')),
  coverageRows: loadCoverageRegistry(resolve(ROOT, 'SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv')),
  now: '2026-07-16T12:00:00.000Z',
};

const fullInput = {
  raw_request_text: 'Forecast the AFL match winner.',
  primary_question_text: 'Will Geelong win in regulation?',
  created_by: 'test',
  event_id: 'AFL:TEST:1',
  sport_family: 'Australian football',
  competition_id: 'AFL',
  season_id: '2026',
  event_name: 'Geelong v St Kilda',
  venue: 'Test Venue',
  event_start_utc: '2026-07-17T09:00:00Z',
  ruleset_id: 'AFL_2026',
  market_id: 'AFL:TEST:WINNER',
  market_family: 'winner',
  selection: 'Geelong',
  settlement_convention_id: 'AFL_WINNER_REGULATION_V1',
  analysis_mode: 'RESEARCH_ONLY',
  forecast_state: 'PREGAME_CONFIRMED',
  horizon_bucket_id: 'T24H_TO_T0',
  selection_mode: 'USER_SUPPLIED',
};

test('registered contract with no ACTIVE model freezes an evidenced MODEL_UNAVAILABLE PASS', () => {
  const modelUnavailableContext = {
    ...context,
    controls: { ...context.controls, contracts: [{
      status: 'ACTIVE', competition_id: 'AFL', ruleset_id: 'AFL_2026', settlement_convention_id: 'AFL_WINNER_REGULATION_V1',
      market_family: 'winner', forecast_state: 'PREGAME_CONFIRMED',
    }] },
  };
  const packet = createInitialDecisionPacket(fullInput, modelUnavailableContext);
  assert.equal(packet.decision_snapshot.decision, 'PASS');
  assert.equal(packet.decision_snapshot.pass_reason, 'MODEL_UNAVAILABLE');
  assert.equal(packet.decision_snapshot.primary_failed_gate, 'GATE-MODEL-001');
  assert.ok(packet.decision_snapshot.missing_prerequisites.length > 0);
  assert.equal(packet.decision_snapshot.gate_failure_evidence[0].gate_id, 'GATE-MODEL-001');
  assert.equal(packet.prediction, null);
  const report = validateDecisionPacket(packet, modelUnavailableContext);
  assert.equal(report.valid, true);
});

test('counterfeit RESOLVED contract status cannot validate a CONTRACT_UNRESOLVED PASS', () => {
  let packet = createInitialDecisionPacket(fullInput, context);
  assert.equal(packet.decision_snapshot.pass_reason, 'CONTRACT_UNRESOLVED');
  packet.request.contract_status = 'RESOLVED';
  packet = finalizePacket(packet);
  const report = validateDecisionPacket(packet, context);
  assert.equal(report.valid, false);
  assert.equal(report.gate_results.find((row) => row.gate_id === 'RUNTIME-ABSTENTION-CAUSE-001').status, 'FAIL');
});

test('packet mutation breaks canonical snapshot hash', () => {
  const packet = createInitialDecisionPacket(fullInput, context);
  packet.request.primary_question_text = 'Changed after freeze';
  const report = validateDecisionPacket(packet, context);
  assert.equal(report.valid, false);
  assert.equal(report.gate_results.find((row) => row.gate_id === 'RUNTIME-HASH-001').status, 'FAIL');
});

test('abstention note cannot smuggle a probability', () => {
  const packet = createInitialDecisionPacket({ ...fullInput, research_note: 'The selection is about 62% likely.' }, context);
  const report = validateDecisionPacket(packet, context);
  assert.equal(report.valid, false);
  assert.equal(report.gate_results.find((row) => row.gate_id === 'RUNTIME-NONPROB-NOTE-001').status, 'FAIL');
});

test('abstention cannot smuggle a quantitative child object', () => {
  let packet = createInitialDecisionPacket(fullInput, context);
  packet.candidate_universe = { issued_probability: 0.99 };
  packet = finalizePacket(packet);
  const report = validateDecisionPacket(packet, context);
  assert.equal(report.valid, false);
  assert.equal(report.gate_results.find((row) => row.gate_id === 'RUNTIME-ABSTENTION-NULLS-001').status, 'FAIL');
});

test('workflow rejects unfilled template sentinels instead of freezing them as evidence', () => {
  assert.throws(() => createInitialDecisionPacket({
    ...fullInput,
    raw_request_text: 'REPLACE_WITH_THE_VERBATIM_REQUEST',
  }, context), /verbatim\/non-placeholder/);
});

test('dummy ISSUE cannot bypass model, source, test, probability or uncertainty gates', () => {
  let packet = createInitialDecisionPacket(fullInput, context);
  packet.decision_snapshot.decision = 'ISSUE';
  packet.decision_snapshot.pass_reason = null;
  packet.prediction = {};
  packet = finalizePacket(packet);
  const report = validateDecisionPacket(packet, context);
  assert.equal(report.valid, false);
  const failed = new Set(report.gate_results.filter((row) => row.status === 'FAIL').map((row) => row.gate_id));
  for (const id of ['GATE-CONTRACT-001', 'GATE-UNIVERSE-001', 'GATE-SOURCE-001', 'GATE-MODEL-001', 'GATE-TEST-001', 'GATE-PROB-001', 'GATE-UNCERTAINTY-001']) assert.ok(failed.has(id), id);
});
