import test from 'node:test';
import assert from 'node:assert/strict';
import { brierLoss, conditionalProbability, expectedReturn, logLoss, proportionalNoVig, validateLinkedMarketCoherence, validateProbabilityVector } from '../src/scoring.mjs';

test('canonical scoring fixtures reproduce exactly', () => {
  assert.ok(Math.abs(brierLoss([0.7, 0.3], 0) - 0.09) < 1e-12);
  assert.ok(Math.abs(brierLoss([0.7, 0.3], 1) - 0.49) < 1e-12);
  assert.ok(Math.abs(logLoss([0.7, 0.3], 0) - 0.35667494393873245) < 1e-12);
  assert.ok(Math.abs(logLoss([0.7, 0.3], 1) - 1.2039728043259361) < 1e-12);
  assert.ok(Math.abs(brierLoss([0.55, 0.35, 0.10], 2) - 0.6175) < 1e-12);
  assert.ok(Math.abs(logLoss([0.55, 0.35, 0.10], 2) - 2.3025850929940455) < 1e-12);
  assert.equal(logLoss([1, 0], 1), Number.POSITIVE_INFINITY);
});

test('push-aware EV and conditional market comparison do not use p*d-1', () => {
  const pushAware = expectedReturn([0.45, 0.45, 0.10], [1, -1, 0]);
  const invalidBinaryShortcut = 0.45 * 2 - 1;
  assert.ok(Math.abs(pushAware) < 1e-12);
  assert.ok(Math.abs(invalidBinaryShortcut - -0.1) < 1e-12);
  assert.notEqual(pushAware, invalidBinaryShortcut);
  assert.ok(Math.abs(expectedReturn([0.55, 0.45], [1, -1]) - 0.10) < 1e-12);
  assert.equal(conditionalProbability(0.45, [0.45, 0.45]), 0.5);
  const market = proportionalNoVig([2, 2]);
  assert.equal(market.no_vig_probabilities[0], 0.5);
  assert.equal(market.overround, 0);
});

test('structural boundary permission is branch-specific', () => {
  assert.deepEqual(validateProbabilityVector([0, 0.6, 0.4], 1e-9, { structuralMask: [true, false, false] }), []);
  assert.match(validateProbabilityVector([0, 0.6, 0.4], 1e-9, { structuralMask: [false, false, false] })[0], /non-structural/);
  assert.ok(validateProbabilityVector([1, 0], 1e-9, { structuralMask: [false, true] }).some((error) => error.includes('branch 0')));
});

test('linked-market coherence rejects an unknown constraint name', () => {
  const distributions = [
    { forecast_distribution_id: 'LEFT', states: [{ settlement_state_id: 'LEFT_WIN', decision_probability: 0.5 }] },
    { forecast_distribution_id: 'RIGHT', states: [{ settlement_state_id: 'RIGHT_WIN', decision_probability: 0.5 }] },
  ];
  const errors = validateLinkedMarketCoherence([{
    relation_id: 'UNKNOWN-CONSTRAINT', left_distribution_id: 'LEFT', left_winning_state_ids: ['LEFT_WIN'],
    right_distribution_id: 'RIGHT', right_winning_state_ids: ['RIGHT_WIN'], constraint: 'UNREGISTERED_RULE',
  }], distributions);
  assert.ok(errors.some((error) => error.includes('unknown constraint')));
});

test('linked-market coherence rejects empty or nonexistent winning-state ID sets', () => {
  const distributions = [
    { forecast_distribution_id: 'LEFT', states: [{ settlement_state_id: 'LEFT_WIN', decision_probability: 0.5 }] },
    { forecast_distribution_id: 'RIGHT', states: [{ settlement_state_id: 'RIGHT_WIN', decision_probability: 0.5 }] },
  ];
  const base = {
    relation_id: 'STATE-VALIDATION', left_distribution_id: 'LEFT', left_winning_state_ids: ['LEFT_WIN'],
    right_distribution_id: 'RIGHT', right_winning_state_ids: ['RIGHT_WIN'], constraint: 'EQUAL',
  };
  assert.ok(validateLinkedMarketCoherence([{ ...base, left_winning_state_ids: [] }], distributions)
    .some((error) => error.includes('winning-state sets must be nonempty')));
  assert.ok(validateLinkedMarketCoherence([{ ...base, right_winning_state_ids: ['MISSING_STATE'] }], distributions)
    .some((error) => error.includes('unknown state ids')));
});

test('nested-market contradiction fails coherence', () => {
  const distributions = [
    { forecast_distribution_id: 'LOW_LINE', states: [{ settlement_state_id: 'LOW_OVER', decision_probability: 0.45 }] },
    { forecast_distribution_id: 'HIGH_LINE', states: [{ settlement_state_id: 'HIGH_OVER', decision_probability: 0.55 }] },
  ];
  const errors = validateLinkedMarketCoherence([{
    relation_id: 'TOTAL_MONOTONIC',
    left_distribution_id: 'LOW_LINE',
    left_winning_state_ids: ['LOW_OVER'],
    right_distribution_id: 'HIGH_LINE',
    right_winning_state_ids: ['HIGH_OVER'],
    constraint: 'LEFT_GTE_RIGHT',
  }], distributions);
  assert.equal(errors.length, 1);
});
