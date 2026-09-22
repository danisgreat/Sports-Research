import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';

import { parseCsv } from '../src/csv.mjs';

const ROOT = resolve(import.meta.dirname, '..');
const MATRIX_PATH = resolve(ROOT, 'schema/acceptance_traceability_v1.csv');
const ACCEPTANCE_PATH = resolve(ROOT, 'SPORTS_ACCEPTANCE_TESTS_v3.md');
const ALLOWED_STATUSES = new Set(['COVERED', 'PARTIAL', 'NOT_IMPLEMENTED']);

function rangeIds(prefix, count) {
  return Array.from({ length: count }, (_, index) => `${prefix}-${String(index + 1).padStart(3, '0')}`);
}

test('acceptance traceability is complete unique machine-readable and honest about gaps', () => {
  const rows = parseCsv(readFileSync(MATRIX_PATH, 'utf8'));
  assert.deepEqual(Object.keys(rows[0]), ['requirement_id', 'category', 'status', 'test_file', 'test_name', 'notes']);
  assert.equal(rows.length, 88, 'all canonical acceptance requirements must be mapped');

  const ids = rows.map((row) => row.requirement_id);
  assert.equal(new Set(ids).size, ids.length, 'requirement_id values must be unique');
  for (const row of rows) {
    assert.ok(row.requirement_id, 'blank requirement_id');
    assert.ok(row.category, `${row.requirement_id}: blank category`);
    assert.ok(ALLOWED_STATUSES.has(row.status), `${row.requirement_id}: invalid status ${row.status}`);
    assert.ok(row.test_name, `${row.requirement_id}: blank test_name or planned test`);
    assert.ok(row.notes, `${row.requirement_id}: blank notes`);
    if (row.status !== 'NOT_IMPLEMENTED') {
      for (const file of row.test_file.split(' | ')) {
        assert.ok(file && existsSync(resolve(ROOT, file)), `${row.requirement_id}: missing evidence file ${file}`);
      }
    }
  }

  const acceptanceText = readFileSync(ACCEPTANCE_PATH, 'utf8');
  const explicitlyNamed = new Set(acceptanceText.match(/(?:SPEC|GATE|SCORE|EV|EVAL|DRIFT|INCIDENT|ROLLBACK)-[A-Z0-9-]+/g) ?? []);
  const narrativeNegativeIds = [
    ...rangeIds('NEG-ID', 4),
    ...rangeIds('NEG-CMC', 7),
    ...rangeIds('NEG-SEL', 5),
    ...rangeIds('NEG-MTS', 9),
    ...rangeIds('NEG-PUC', 7),
    ...rangeIds('NEG-PEX', 5),
    ...rangeIds('NEG-SET', 6),
  ];
  const goLiveIds = rangeIds('GO-LIVE', 6);
  const expectedAcceptanceIds = new Set([...explicitlyNamed, ...narrativeNegativeIds, ...goLiveIds]);
  assert.equal(expectedAcceptanceIds.size, 88, 'acceptance inventory changed; update the stable mapping deliberately');
  for (const id of expectedAcceptanceIds) assert.ok(ids.includes(id), `unmapped acceptance requirement ${id}`);
  assert.deepEqual(ids.filter((id) => !expectedAcceptanceIds.has(id)), []);

  assert.equal(rows.filter((row) => row.requirement_id.startsWith('NEG-')).length, 43);
  assert.equal(rows.filter((row) => row.requirement_id.startsWith('GO-LIVE-')).length, 6);
  assert.ok(rows.some((row) => row.status === 'NOT_IMPLEMENTED'), 'matrix must not imply complete acceptance while gaps remain');
});
