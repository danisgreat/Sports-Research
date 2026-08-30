import test from 'node:test';
import assert from 'node:assert/strict';
import { resolve } from 'node:path';
import { findExactActiveCoverage, loadCoverageRegistry, validateCoverageRegistry } from '../src/coverage.mjs';

const ROOT = resolve(import.meta.dirname, '..');

test('current coverage registry is valid and deliberately inactive', () => {
  const rows = loadCoverageRegistry(resolve(ROOT, 'SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv'));
  assert.equal(rows.filter((row) => row.status === 'ACTIVE').length, 0);
  assert.deepEqual(validateCoverageRegistry(rows, { suspended: true, now: Date.parse('2026-07-16T00:00:00Z') }), []);
});

test('single-scope ACTIVE row passes local registry checks and ALL scopes are rejected', () => {
  const active = {
    coverage_id: 'TEST_ACTIVE', sport_family: 'Soccer', competition_scope: 'EPL', market_scope: 'total',
    forecast_state: 'PREGAME_CONFIRMED', analysis_mode: 'RESEARCH_ONLY', status: 'ACTIVE', model_id: 'M', model_version: '1',
    source_map_id: 'SM', test_report_id: 'T', shadow_report_id: 'S', approved_by: 'A', approval_utc: '2026-07-01T00:00:00Z',
    expires_utc: '2027-01-01T00:00:00Z', reason: 'approved exact test fixture',
  };
  assert.deepEqual(validateCoverageRegistry([active], { suspended: false, now: Date.parse('2026-07-16T00:00:00Z') }), []);
  assert.equal(findExactActiveCoverage([active], {
    sport_family: 'Soccer', competition_id: 'EPL', market_family: 'total', forecast_state: 'PREGAME_CONFIRMED', analysis_mode: 'RESEARCH_ONLY',
  }, Date.parse('2026-07-16T00:00:00Z')).coverage_id, 'TEST_ACTIVE');
  for (const field of ['competition_scope', 'market_scope', 'forecast_state', 'analysis_mode']) {
    assert.ok(validateCoverageRegistry([{ ...active, [field]: 'ALL' }], { suspended: false })
      .some((error) => error.includes('cannot contain ALL')), field);
  }
});

test('ACTIVE coverage requires every local activation-evidence field and an unexpired approval', () => {
  const active = {
    coverage_id: 'TEST_ACTIVE', sport_family: 'Soccer', competition_scope: 'EPL', market_scope: 'total',
    forecast_state: 'PREGAME_CONFIRMED', analysis_mode: 'RESEARCH_ONLY', status: 'ACTIVE', model_id: 'M', model_version: '1',
    source_map_id: 'SM', test_report_id: 'T', shadow_report_id: 'S', approved_by: 'A', approval_utc: '2026-07-01T00:00:00Z',
    expires_utc: '2027-01-01T00:00:00Z', reason: 'synthetic fixture',
  };
  for (const field of ['model_id', 'model_version', 'source_map_id', 'test_report_id', 'shadow_report_id', 'approved_by', 'approval_utc', 'expires_utc']) {
    const errors = validateCoverageRegistry([{ ...active, [field]: '' }], { suspended: false, now: Date.parse('2026-07-16T00:00:00Z') });
    assert.ok(errors.some((error) => error.includes(field)), field);
  }
  assert.ok(validateCoverageRegistry([{ ...active, expires_utc: '2026-07-15T00:00:00Z' }], {
    suspended: false, now: Date.parse('2026-07-16T00:00:00Z'),
  }).some((error) => error.includes('expired')));
});

test('ACTIVE coverage rejects multi-token scopes such as EPL|UCL as non-exact', () => {
  const active = {
    coverage_id: 'TEST_ACTIVE_MULTISCOPE', sport_family: 'Soccer', competition_scope: 'EPL|UCL', market_scope: 'total',
    forecast_state: 'PREGAME_CONFIRMED', analysis_mode: 'RESEARCH_ONLY', status: 'ACTIVE', model_id: 'M', model_version: '1',
    source_map_id: 'SM', test_report_id: 'T', shadow_report_id: 'S', approved_by: 'A', approval_utc: '2026-07-01T00:00:00Z',
    expires_utc: '2027-01-01T00:00:00Z', reason: 'synthetic fixture',
  };
  assert.ok(validateCoverageRegistry([active], { suspended: false, now: Date.parse('2026-07-16T00:00:00Z') })
    .some((error) => error.includes('one exact value')));
});
