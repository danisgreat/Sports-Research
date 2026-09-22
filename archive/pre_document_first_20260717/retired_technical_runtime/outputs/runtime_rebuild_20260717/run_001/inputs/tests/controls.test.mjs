import test from 'node:test';
import assert from 'node:assert/strict';
import { resolve } from 'node:path';
import { loadCoverageRegistry } from '../src/coverage.mjs';
import { validateRuntimeControls } from '../src/controls.mjs';
import { loadMachineControls } from '../src/packet.mjs';
import { makeValidIssueFixture } from './support/valid_issue_fixture.mjs';

const ROOT = resolve(import.meta.dirname, '..');
const controls = loadMachineControls(ROOT.replaceAll('\\', '/'));
const coverageRows = loadCoverageRegistry(resolve(ROOT, 'SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv'));

test('all current machine controls reconcile while remaining suspended', () => {
  const report = validateRuntimeControls(controls, coverageRows, { now: Date.parse('2026-07-16T12:00:00.000Z') });
  assert.equal(report.valid, true, report.errors.join('; '));
  assert.equal(report.active_coverage_count, 0);
});

test('a model status cannot disagree with its coverage status', () => {
  const mutated = { ...controls, modelRegistry: structuredClone(controls.modelRegistry) };
  mutated.modelRegistry[0].status = 'ACTIVE';
  const report = validateRuntimeControls(mutated, coverageRows, { now: Date.parse('2026-07-16T12:00:00.000Z') });
  assert.equal(report.valid, false);
  assert.ok(report.errors.some((error) => error.includes('differs from coverage')));
});

test('an ACTIVE release cross-joins coverage to exact model, source-map, test, shadow and contract evidence', () => {
  const { context: active } = makeValidIssueFixture();
  const valid = validateRuntimeControls(active.controls, active.coverageRows, { now: Date.parse('2026-07-16T12:00:00.000Z') });
  assert.equal(valid.valid, true, valid.errors.join('; '));

  const wrongSourceMap = structuredClone(active.coverageRows);
  wrongSourceMap[0].source_map_id = 'SOURCE_MAP_DOES_NOT_EXIST';
  const invalid = validateRuntimeControls(active.controls, wrongSourceMap, { now: Date.parse('2026-07-16T12:00:00.000Z') });
  assert.equal(invalid.valid, false);
  assert.ok(invalid.errors.some((error) => error.includes('ACTIVE source map has no rows')));
});
