import { readFileSync } from 'node:fs';
import { parseCsv } from './csv.mjs';
import { parseUtc } from './canonical.mjs';

export const COVERAGE_STATUSES = new Set(['UNSUPPORTED', 'DEVELOPMENT', 'SHADOW', 'ACTIVE', 'SUSPENDED', 'RETIRED']);
const REQUIRED_COLUMNS = [
  'coverage_id', 'sport_family', 'competition_scope', 'market_scope', 'forecast_state', 'analysis_mode', 'status',
  'model_id', 'model_version', 'source_map_id', 'test_report_id', 'shadow_report_id', 'approved_by', 'approval_utc',
  'expires_utc', 'reason',
];
const ACTIVE_EVIDENCE = ['model_id', 'model_version', 'source_map_id', 'test_report_id', 'shadow_report_id', 'approved_by', 'approval_utc', 'expires_utc'];

export function loadCoverageRegistry(path) {
  return parseCsv(readFileSync(path, 'utf8'));
}

function scopeContains(scope, value) {
  return scope.split('|').includes(value);
}

export function validateCoverageRegistry(rows, { suspended = true, now = Date.now() } = {}) {
  const errors = [];
  if (!rows.length) return ['coverage registry has no rows'];
  const actualColumns = Object.keys(rows[0]);
  for (const column of REQUIRED_COLUMNS) if (!actualColumns.includes(column)) errors.push(`missing coverage column ${column}`);
  const seen = new Set();
  for (const [index, row] of rows.entries()) {
    const label = row.coverage_id || `row ${index + 2}`;
    if (!row.coverage_id) errors.push(`row ${index + 2}: coverage_id is blank`);
    else if (seen.has(row.coverage_id)) errors.push(`${label}: duplicate coverage_id`);
    seen.add(row.coverage_id);
    if (!COVERAGE_STATUSES.has(row.status)) errors.push(`${label}: invalid status ${row.status}`);

    if (row.status === 'ACTIVE') {
      for (const field of ACTIVE_EVIDENCE) if (!row[field]) errors.push(`${label}: ACTIVE row missing ${field}`);
      for (const field of ['competition_scope', 'market_scope', 'forecast_state', 'analysis_mode']) {
        if (!row[field] || scopeContains(row[field], 'ALL') || row[field].includes('|')) errors.push(`${label}: ACTIVE ${field} must be one exact value and cannot contain ALL`);
      }
      try {
        if (parseUtc(row.expires_utc, `${label}.expires_utc`) <= now) errors.push(`${label}: ACTIVE approval is expired`);
        parseUtc(row.approval_utc, `${label}.approval_utc`);
      } catch (error) {
        errors.push(error.message);
      }
    }

    if (row.status === 'DEVELOPMENT') {
      if (!row.model_id || !row.model_version) errors.push(`${label}: DEVELOPMENT row requires model_id and model_version`);
      for (const field of ACTIVE_EVIDENCE.slice(2)) if (row[field]) errors.push(`${label}: DEVELOPMENT row must not contain ${field}`);
    }

    if (row.status === 'UNSUPPORTED' && (row.model_id || row.model_version)) {
      errors.push(`${label}: UNSUPPORTED row must not name a model`);
    }
  }
  const activeCount = rows.filter((row) => row.status === 'ACTIVE').length;
  if (suspended && activeCount !== 0) errors.push(`suspended release contains ${activeCount} ACTIVE coverage row(s)`);
  return errors;
}

export function findExactActiveCoverage(rows, scope, now = Date.now()) {
  return rows.find((row) => {
    if (row.status !== 'ACTIVE') return false;
    try {
      if (parseUtc(row.expires_utc, 'expires_utc') <= now) return false;
    } catch {
      return false;
    }
    return row.sport_family === scope.sport_family
      && scopeContains(row.competition_scope, scope.competition_id)
      && scopeContains(row.market_scope, scope.market_family)
      && scopeContains(row.forecast_state, scope.forecast_state)
      && scopeContains(row.analysis_mode, scope.analysis_mode);
  }) ?? null;
}
