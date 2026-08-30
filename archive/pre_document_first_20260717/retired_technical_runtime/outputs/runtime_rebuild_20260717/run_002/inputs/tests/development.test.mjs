import test from 'node:test';
import assert from 'node:assert/strict';

import { hashObject } from '../src/canonical.mjs';
import {
  holmDecisions,
  pairedClusterBootstrap,
  riskCoverageCurve,
  validateDevelopmentPlan,
  validateExperimentLedger,
} from '../src/development.mjs';

const ROLES = ['TRAIN', 'TUNE', 'CALIBRATION', 'UNTOUCHED_TEST', 'PROSPECTIVE_SHADOW'];

function eventManifestHash(role, eventIds) {
  return hashObject({
    manifest_version: 'SPORTS_EVENT_ID_MANIFEST_V1',
    role,
    event_ids: [...eventIds].sort(),
  });
}

function validDevelopmentPlan() {
  const windows = [
    ['2025-01-01T00:00:00.000Z', '2025-01-31T00:00:00.000Z', '2025-01-31T12:00:00.000Z'],
    ['2025-02-01T00:00:00.000Z', '2025-02-28T00:00:00.000Z', '2025-02-28T12:00:00.000Z'],
    ['2025-03-01T00:00:00.000Z', '2025-03-31T00:00:00.000Z', '2025-03-31T12:00:00.000Z'],
    ['2025-04-01T00:00:00.000Z', '2025-04-30T00:00:00.000Z', '2025-04-30T12:00:00.000Z'],
    ['2025-05-01T00:00:00.000Z', '2025-05-31T00:00:00.000Z', '2025-05-31T12:00:00.000Z'],
  ];
  const partitions = ROLES.map((role, index) => {
    const eventIds = [`EVENT-${index + 1}`];
    return {
      role,
      start_utc: windows[index][0],
      end_utc: windows[index][1],
      labels_available_by_utc: windows[index][2],
      purge_rule_id: 'PURGE_BY_EVENT_AND_PARTICIPANT_V1',
      label_availability_rule: 'OFFICIAL_FINAL_ONLY_V1',
      event_manifest_hash: eventManifestHash(role, eventIds),
      event_ids: eventIds,
      test_status: ['UNTOUCHED_TEST', 'PROSPECTIVE_SHADOW'].includes(role) ? 'PLANNED_UNTOUCHED' : null,
    };
  });
  return {
    plan_version: 'SPORTS_DEVELOPMENT_PLAN_V1',
    hypothesis_family_id: 'HF-SYNTHETIC-1',
    model_id: 'MODEL-SYNTHETIC-1',
    model_version: '0.1.0',
    primary_metric: 'BRIER',
    scope: {
      sport_family: 'Australian football', competition_id: 'AFL', market_family: 'winner',
      forecast_state: 'PREGAME_CONFIRMED', horizon_bucket_id: 'T24H_TO_T0',
      settlement_convention_id: 'AFL_WINNER_REGULATION_V1',
    },
    partitions,
    baseline: { baseline_id: 'BASELINE-HISTORICAL-RATE', version: '1.0.0' },
    promotion_rule: {
      minimum_score_improvement: 0.005,
      minimum_effective_n: 50,
      confidence_level: 0.95,
      required_lower_bound: 0.005,
      point_weighting: 'ROW_EQUAL',
      resampling_unit: 'EVENT_CLUSTER',
    },
    calibration_guardrails: [{ metric: 'ECE', operator: 'LTE', threshold: 0.05, minimum_n: 50 }],
    tail_and_segment_guardrails: [{ metric: 'SEGMENT_SCORE_DELTA', operator: 'GTE', threshold: -0.01, minimum_n: 20 }],
    multiplicity: {
      hypothesis_family_definition: 'All variants informed by the same untouched test',
      confirmatory_method: 'HOLM', family_alpha: 0.05,
    },
    selective_policy: {
      coverage_denominator: 'ALL_ELIGIBLE_REQUESTS', primary_selective_metric: 'RISK_AT_FIXED_COVERAGE', target: 0.5,
    },
    monitoring: {
      integrity_failures: ['LEAKAGE', 'SCOPE_MISMATCH'], performance_window: { size: 100, unit: 'SETTLED_EVENTS' },
      minimum_settled_n: 50,
      alert_rule: { rule_id: 'ALERT_V1', metric: 'BRIER_DELTA', operator: 'LTE', threshold: 0, consecutive_windows: 2 },
      suspension_rule: { rule_id: 'SUSPEND_V1', metric: 'DATA_INTEGRITY_FAILURE_COUNT', operator: 'GTE', threshold: 1, consecutive_windows: 1 },
      restart_rule: { rule_id: 'NEW_VERSION_ONLY_V1', metric: 'REMEDIATION_EVIDENCE_COMPLETE', operator: 'EQ', threshold: 1, consecutive_windows: 1 },
    },
  };
}

test('risk-coverage includes the abstention denominator and computes selective risk', () => {
  const result = riskCoverageCurve([
    { request_id: 'A', selector_score: 0.9, loss: 0.1 },
    { request_id: 'B', selector_score: 0.8, loss: 0.3 },
    { request_id: 'C', selector_score: 0.2, loss: 0.8 },
  ]);
  assert.equal(result.curve[0].coverage, 1 / 3);
  assert.equal(result.curve[1].selective_risk, 0.2);
  assert.equal(result.eligible_count, 3);
});

test('risk-coverage emits only implementable complete tie blocks', () => {
  const result = riskCoverageCurve([
    { request_id: 'A', selector_score: 0.9, loss: 0.1 },
    { request_id: 'B', selector_score: 0.9, loss: 0.3 },
    { request_id: 'C', selector_score: 0.2, loss: 0.8 },
  ]);
  assert.equal(result.curve.length, 2);
  assert.equal(result.curve[0].tie_block_size, 2);
  assert.equal(result.curve[0].coverage, 2 / 3);
});

test('paired event-cluster bootstrap is reproducible and discloses weighting', () => {
  const rows = [
    { cluster_id: 'E1', model_loss: 0.2, baseline_loss: 0.3 },
    { cluster_id: 'E1', model_loss: 0.3, baseline_loss: 0.35 },
    { cluster_id: 'E2', model_loss: 0.4, baseline_loss: 0.45 },
    { cluster_id: 'E3', model_loss: 0.1, baseline_loss: 0.25 },
  ];
  const first = pairedClusterBootstrap(rows, { seed: 7, resamples: 200, pointWeighting: 'ROW_EQUAL' });
  const second = pairedClusterBootstrap(rows, { seed: 7, resamples: 200, pointWeighting: 'ROW_EQUAL' });
  assert.deepEqual(first, second);
  assert.equal(first.cluster_count, 3);
  assert.equal(first.point_weighting, 'ROW_EQUAL');
  assert.match(first.cluster_size_concentration_note, /not a dependence-adjusted effective sample size/);
});

test('Holm procedure stops after first retained hypothesis and rejects invalid inputs', () => {
  const decisions = holmDecisions([
    { hypothesis_id: 'A', p_value: 0.001 },
    { hypothesis_id: 'B', p_value: 0.04 },
    { hypothesis_id: 'C', p_value: 0.03 },
  ], 0.05);
  assert.equal(decisions.find((row) => row.hypothesis_id === 'A').reject, true);
  assert.equal(decisions.find((row) => row.hypothesis_id === 'B').reject, false);
  assert.throws(() => holmDecisions([{ hypothesis_id: 'A', p_value: 0.1 }, { hypothesis_id: 'A', p_value: 0.2 }]), /unique/);
  assert.throws(() => holmDecisions([{ hypothesis_id: 'A', p_value: 1.1 }]), /\[0,1\]/);
});

test('a fully populated development plan passes and a real chronological overlap fails', () => {
  const plan = validDevelopmentPlan();
  assert.deepEqual(validateDevelopmentPlan(plan), []);
  plan.partitions[1].start_utc = '2025-01-15T00:00:00.000Z';
  const errors = validateDevelopmentPlan(plan);
  assert.ok(errors.some((error) => error.includes('partitions overlap')), errors.join('; '));
});

test('experiment ledger detects spent-test manifest reuse in the same hypothesis family', () => {
  const common = {
    hypothesis_family_id: 'HF', model_id: 'M', model_version: '1', model_config_hash: '1'.repeat(64),
    event_manifest_hash: '2'.repeat(64), preregistered_rule_hash: '3'.repeat(64),
    preregistered_at_utc: '2025-12-01T00:00:00.000Z',
  };
  const errors = validateExperimentLedger([
    { ...common, experiment_id: 'E1', test_status: 'SPENT', first_viewed_at_utc: '2026-01-01T00:00:00.000Z' },
    { ...common, experiment_id: 'E2', test_status: 'PLANNED_UNTOUCHED' },
  ]);
  assert.ok(errors.some((error) => error.includes('reuse')), errors.join('; '));
});

test('pairedClusterBootstrap rejects confidenceLevel outside (0,1)', () => {
  const rows = [
    { cluster_id: 'E1', model_loss: 0.2, baseline_loss: 0.3 },
    { cluster_id: 'E2', model_loss: 0.3, baseline_loss: 0.4 },
  ];
  assert.throws(() => pairedClusterBootstrap(rows, { confidenceLevel: 1.1 }), /confidenceLevel/);
});

test('BETWEEN development guardrail requires lower and upper thresholds', () => {
  const plan = validDevelopmentPlan();
  plan.calibration_guardrails = [{ metric: 'ECE', operator: 'BETWEEN', threshold: 0.05, minimum_n: 50 }];
  assert.ok(validateDevelopmentPlan(plan).some((error) => error.includes('calibration guardrail')));
});
