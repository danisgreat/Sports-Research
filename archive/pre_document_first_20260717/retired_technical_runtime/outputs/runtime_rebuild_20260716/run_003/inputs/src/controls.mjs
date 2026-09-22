import { isSha256, parseUtc } from './canonical.mjs';
import { validateCoverageRegistry } from './coverage.mjs';
import { validateReleaseManifest } from './release.mjs';

function duplicates(rows, key) {
  const seen = new Set();
  const duplicate = new Set();
  for (const row of rows) {
    const value = row[key];
    if (!value || seen.has(value)) duplicate.add(value || '<blank>');
    seen.add(value);
  }
  return [...duplicate];
}

function splitScope(value) {
  return String(value ?? '').split('|').filter(Boolean);
}

export function validateRuntimeControls(controls, coverageRows, { now = Date.now() } = {}) {
  const errors = [];
  const releaseReport = validateReleaseManifest(controls.release, coverageRows);
  errors.push(...releaseReport.errors.map((error) => `release: ${error}`));
  errors.push(...validateCoverageRegistry(coverageRows, {
    suspended: controls.release?.release_mode !== 'OPERATIONAL',
    now,
  }).map((error) => `coverage: ${error}`));
  const traceability = controls.acceptanceTraceability ?? [];
  const traceIds = new Set(traceability.map((row) => row.requirement_id));
  if (traceIds.size !== traceability.length || traceability.some((row) => !row.requirement_id)) errors.push('acceptance traceability requirement IDs must be unique and nonempty');
  if (traceability.length !== controls.release?.expected_acceptance_requirement_count) {
    errors.push(`acceptance traceability count ${traceability.length} differs from release expectation ${controls.release?.expected_acceptance_requirement_count}`);
  }
  if (traceability.some((row) => !['COVERED', 'PARTIAL', 'NOT_IMPLEMENTED'].includes(row.status)
    || !row.category || !row.test_file || !row.test_name || !row.notes)) errors.push('acceptance traceability contains an invalid/incomplete row');

  for (const [name, rows, key] of [
    ['coverage', coverageRows, 'coverage_id'], ['model', controls.modelRegistry, 'model_id'],
    ['source', controls.registeredSources, 'source_id'], ['competition', controls.competitions, 'competition_id'],
    ['contract', controls.contracts, 'contract_id'], ['test', controls.testEvaluations, 'test_evaluation_id'],
  ]) {
    const values = name === 'model'
      ? controls.modelRegistry.map((row) => ({ key: `${row.model_id}:${row.model_version}` }))
      : rows;
    const duplicateValues = duplicates(values, name === 'model' ? 'key' : key);
    if (duplicateValues.length) errors.push(`${name}: duplicate/blank key(s) ${duplicateValues.join('|')}`);
  }

  const coverageByModel = new Map(coverageRows.filter((row) => row.model_id)
    .map((row) => [`${row.model_id}:${row.model_version}`, row]));
  for (const model of controls.modelRegistry) {
    const key = `${model.model_id}:${model.model_version}`;
    const coverage = coverageByModel.get(key);
    if (!coverage) errors.push(`model ${key}: no coverage row`);
    if (coverage && (coverage.sport_family !== model.sport_family || coverage.competition_scope !== model.competition_scope
      || coverage.market_scope !== model.market_scope || coverage.forecast_state !== model.forecast_state
      || coverage.analysis_mode !== model.analysis_mode)) errors.push(`model ${key}: scope differs from coverage`);
    if (coverage && coverage.status !== model.status) errors.push(`model ${key}: status ${model.status} differs from coverage ${coverage.status}`);
    if (model.status === 'ACTIVE') {
      for (const field of ['owner', 'approver', 'change_ticket_id', 'approval_utc', 'expires_utc', 'source_map_id', 'test_report_id', 'shadow_report_id']) {
        if (!model[field]) errors.push(`model ${key}: ACTIVE missing ${field}`);
      }
      for (const field of ['data_manifest_hash', 'code_hash', 'model_artifact_hash', 'calibration_artifact_hash']) {
        if (!isSha256(model[field])) errors.push(`model ${key}: ACTIVE invalid ${field}`);
      }
      try {
        if (parseUtc(model.approval_utc, `${key}.approval_utc`) >= parseUtc(model.expires_utc, `${key}.expires_utc`)) errors.push(`model ${key}: approval must precede expiry`);
        if (parseUtc(model.expires_utc, `${key}.expires_utc`) <= now) errors.push(`model ${key}: approval expired`);
      } catch (error) { errors.push(error.message); }
    }
  }

  const sourceIds = new Set(controls.registeredSources.map((row) => row.source_id));
  const competitionIds = new Set(controls.competitions.map((row) => row.competition_id));
  for (const contract of controls.contracts) {
    if (!['DEVELOPMENT', 'ACTIVE', 'SUSPENDED', 'RETIRED'].includes(contract.status)) errors.push(`contract ${contract.contract_id}: invalid status`);
    if (!competitionIds.has(contract.competition_id)) errors.push(`contract ${contract.contract_id}: competition is not registered`);
    if (contract.status === 'ACTIVE') {
      if (!isSha256(contract.branch_definition_hash) || !contract.approved_by) errors.push(`contract ${contract.contract_id}: ACTIVE evidence incomplete`);
      if (!sourceIds.has(contract.official_rules_source_id) || !sourceIds.has(contract.settlement_authority_source_id)) errors.push(`contract ${contract.contract_id}: authority source missing`);
      try {
        const from = parseUtc(contract.effective_from_utc, `${contract.contract_id}.effective_from_utc`);
        const to = parseUtc(contract.effective_to_utc, `${contract.contract_id}.effective_to_utc`);
        if (from >= to || to <= now) errors.push(`contract ${contract.contract_id}: invalid/expired effective window`);
        parseUtc(contract.approval_utc, `${contract.contract_id}.approval_utc`);
      } catch (error) { errors.push(error.message); }
    }
  }

  const activeMaps = controls.sourceMaps.filter((row) => row.status === 'ACTIVE');
  for (const map of activeMaps) {
    const key = `${map.model_id}:${map.model_version}`;
    if (!sourceIds.has(map.source_id)) errors.push(`source map ${map.source_map_id}/${map.source_id}: source is not registered`);
    if (!coverageByModel.has(key)) errors.push(`source map ${map.source_map_id}: model is not registered`);
    if (!isSha256(map.parser_hash) || !isSha256(map.map_hash) || !map.regression_test_report_id) errors.push(`source map ${map.source_map_id}/${map.source_id}: parser evidence incomplete`);
    if (!['TRUE', 'FALSE'].includes(String(map.required).toUpperCase())) errors.push(`source map ${map.source_map_id}/${map.source_id}: required must be TRUE/FALSE`);
    if (!(Number(map.max_observation_age_seconds) >= 0) || !(Number(map.max_provider_lag_seconds) >= 0)) errors.push(`source map ${map.source_map_id}/${map.source_id}: freshness limits invalid`);
    try {
      if (parseUtc(map.expires_utc, `${map.source_map_id}.expires_utc`) <= now) errors.push(`source map ${map.source_map_id}: expired`);
      parseUtc(map.approval_utc, `${map.source_map_id}.approval_utc`);
    } catch (error) { errors.push(error.message); }
  }

  for (const coverage of coverageRows.filter((row) => row.status === 'ACTIVE')) {
    const model = controls.modelRegistry.find((row) => row.model_id === coverage.model_id && row.model_version === coverage.model_version);
    if (!model || model.status !== 'ACTIVE') errors.push(`coverage ${coverage.coverage_id}: exact ACTIVE model missing`);
    const maps = activeMaps.filter((row) => row.source_map_id === coverage.source_map_id);
    if (!maps.length) errors.push(`coverage ${coverage.coverage_id}: ACTIVE source map has no rows`);
    const test = controls.testEvaluations.find((row) => row.test_evaluation_id === coverage.test_report_id);
    const shadow = controls.testEvaluations.find((row) => row.test_evaluation_id === coverage.shadow_report_id);
    for (const [role, record, expectedRole] of [['test', test, 'UNTOUCHED_TEST'], ['shadow', shadow, 'PROSPECTIVE_SHADOW']]) {
      if (!record || record.test_role !== expectedRole || record.test_status !== 'SPENT' || record.decision_rule_passed !== 'TRUE'
        || !isSha256(record.event_manifest_hash) || !isSha256(record.preregistered_rule_hash) || !isSha256(record.results_artifact_hash)) {
        errors.push(`coverage ${coverage.coverage_id}: ${role} evidence is incomplete`);
      }
    }
    if (test && shadow) {
      try {
        if (parseUtc(test.end_utc, 'test.end_utc') >= parseUtc(shadow.start_utc, 'shadow.start_utc')) errors.push(`coverage ${coverage.coverage_id}: shadow is not later than untouched test`);
      } catch (error) { errors.push(error.message); }
      if (test.event_manifest_hash === shadow.event_manifest_hash) errors.push(`coverage ${coverage.coverage_id}: test and shadow reuse an event manifest`);
    }
    const contracts = controls.contracts.filter((row) => row.status === 'ACTIVE'
      && splitScope(coverage.competition_scope).includes(row.competition_id)
      && row.market_family === coverage.market_scope && row.forecast_state === coverage.forecast_state);
    if (!contracts.length) errors.push(`coverage ${coverage.coverage_id}: no exact ACTIVE contract`);
  }

  if (controls.release?.release_mode !== 'OPERATIONAL') {
    for (const [name, rows] of [['model', controls.modelRegistry], ['contract', controls.contracts], ['source map', controls.sourceMaps]]) {
      const active = rows.filter((row) => row.status === 'ACTIVE');
      if (active.length) errors.push(`${name}: ${active.length} ACTIVE row(s) are forbidden in a non-operational release`);
    }
  } else {
    if (!traceability.length) errors.push('acceptance traceability matrix is missing');
    const incomplete = traceability.filter((row) => row.status !== 'COVERED');
    if (incomplete.length) errors.push(`acceptance traceability has ${incomplete.length} non-COVERED requirement(s)`);
  }

  return { valid: errors.length === 0, errors, active_coverage_count: releaseReport.active_count };
}
