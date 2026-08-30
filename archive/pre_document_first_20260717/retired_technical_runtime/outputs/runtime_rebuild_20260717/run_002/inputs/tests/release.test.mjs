import test from 'node:test';
import assert from 'node:assert/strict';
import { resolve } from 'node:path';
import { readJson } from '../src/canonical.mjs';
import { loadCoverageRegistry } from '../src/coverage.mjs';
import { validateReleaseManifest } from '../src/release.mjs';

const ROOT = resolve(import.meta.dirname, '..');
const release = readJson(resolve(ROOT, 'SPORTS_RELEASE_MANIFEST_v1.json'));
const coverage = loadCoverageRegistry(resolve(ROOT, 'SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv'));

test('current release is explicitly suspended and reconciles to zero ACTIVE scopes', () => {
  const report = validateReleaseManifest(release, coverage);
  assert.deepEqual(report.errors, []);
  assert.equal(report.active_count, 0);
});

test('an ACTIVE row cannot be smuggled into a suspended release', () => {
  const mutated = structuredClone(coverage);
  mutated[0].status = 'ACTIVE';
  const report = validateReleaseManifest(release, mutated);
  assert.equal(report.valid, false);
  assert.ok(report.errors.some((error) => error.includes('ACTIVE')));
});

test('OPERATIONAL cannot be declared without review and a release bundle hash', () => {
  const mutated = structuredClone(release);
  mutated.release_mode = 'OPERATIONAL';
  mutated.operational_status = 'OPERATIONAL_EXACT_SCOPES_ONLY';
  mutated.activation_authorized = true;
  const report = validateReleaseManifest(mutated, coverage);
  assert.equal(report.valid, false);
  assert.ok(report.errors.some((error) => error.includes('release_bundle_hash')));
});
