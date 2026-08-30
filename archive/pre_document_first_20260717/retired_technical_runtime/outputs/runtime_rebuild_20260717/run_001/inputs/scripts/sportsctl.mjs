#!/usr/bin/env node
import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import { hashFile, hashObject, readJson, writeJsonAtomic } from '../src/canonical.mjs';
import { loadCoverageRegistry, validateCoverageRegistry } from '../src/coverage.mjs';
import { appendDecisionPacket, appendEvaluation, appendSettlement, DEFAULT_JOURNAL, initializeJournal, recoverJournalAnchor, verifyJournal } from '../src/journal.mjs';
import { loadMachineControls, validateDecisionPacket } from '../src/packet.mjs';
import { brierLoss, expectedReturn, logLoss, SCORING_SPEC_VERSION } from '../src/scoring.mjs';
import { createInitialDecisionPacket } from '../src/workflow.mjs';
import { parseCsv } from '../src/csv.mjs';
import { validateReleaseManifest } from '../src/release.mjs';
import { validateRuntimeControls } from '../src/controls.mjs';
import { analyseLive, loadAnalysisAssets, validateAnalysisRegistry } from '../src/analysis.mjs';

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(SCRIPT_DIR, '..');
const DEFAULT_COVERAGE = resolve(ROOT, 'SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv');
const DEFAULT_STORE = resolve(ROOT, DEFAULT_JOURNAL);

function parseArgs(argv) {
  const [command = 'help', ...rest] = argv;
  const options = {};
  for (let index = 0; index < rest.length; index += 1) {
    const token = rest[index];
    if (!token.startsWith('--')) throw new Error(`unexpected argument ${token}`);
    const key = token.slice(2);
    if (rest[index + 1] && !rest[index + 1].startsWith('--')) {
      options[key] = rest[index + 1];
      index += 1;
    } else options[key] = true;
  }
  return { command, options };
}

function absolute(path, fallback) {
  return resolve(ROOT, path || fallback);
}

function runtimeContext() {
  const controls = loadMachineControls(ROOT.replaceAll('\\', '/'));
  const coverageRows = loadCoverageRegistry(DEFAULT_COVERAGE);
  const controlFiles = [
    'package.json',
    'package-lock.json',
    'SPORTS_RESEARCH_AUTHORITY_MANIFEST.md',
    'SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv',
    'SPORTS_MODEL_REGISTRY_v1.csv',
    'SPORTS_REGISTERED_SOURCES_v1.csv',
    'SPORTS_RELEASE_MANIFEST_v1.json',
    'schema/controlled_vocabularies_v1.json',
    'schema/competition_registry_v1.csv',
    'schema/contract_registry_v1.csv',
    'schema/source_maps_v1.csv',
    'schema/test_evaluations_v1.csv',
    'schema/decision_packet.schema.json',
    'schema/acceptance_traceability_v1.csv',
    'SPORTS_ANALYSIS_MODEL_REGISTRY_v1.json',
    'SPORTS_ACTIVE_ANALYSIS_MODELS_v1.md',
    'schema/analysis_request.schema.json',
    'schema/analysis_output.schema.json',
    'schema/analysis_acceptance_traceability_v1.csv',
    'schema/experiment_ledger_v1.csv',
    'src/canonical.mjs',
    'src/csv.mjs',
    'src/scoring.mjs',
    'src/coverage.mjs',
    'src/release.mjs',
    'src/controls.mjs',
    'src/packet.mjs',
    'src/workflow.mjs',
    'src/journal.mjs',
    'src/development.mjs',
    'src/analysis.mjs',
    'scripts/sportsctl.mjs',
  ];
  const controlHashes = Object.fromEntries(controlFiles.map((relative) => [relative, hashFile(resolve(ROOT, relative))]));
  const controlBundleHash = hashObject({ bundle_version: 'SPORTS_RUNTIME_CONTROL_BUNDLE_V1', control_hashes: controlHashes });
  return { controls, coverageRows, controlHashes, controlBundleHash };
}

function printValidation(report) {
  for (const row of report.gate_results) {
    process.stdout.write(`${row.status.padEnd(14)} ${row.gate_id.padEnd(30)} ${row.detail}\n`);
  }
  process.stdout.write(`\nvalid=${report.valid}; decision=${report.decision}; failures=${report.failure_count}\n`);
}

function validateSystem() {
  const required = [
    'package.json', 'SPORTS_RESEARCH_AUTHORITY_MANIFEST.md', 'SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv',
    'SPORTS_RELEASE_MANIFEST_v1.json',
    'SPORTS_MODEL_REGISTRY_v1.csv', 'SPORTS_REGISTERED_SOURCES_v1.csv', 'schema/controlled_vocabularies_v1.json',
    'schema/decision_packet.schema.json', 'schema/competition_registry_v1.csv', 'schema/contract_registry_v1.csv',
    'schema/source_maps_v1.csv', 'schema/test_evaluations_v1.csv', 'src/canonical.mjs', 'src/packet.mjs',
    'schema/acceptance_traceability_v1.csv',
    'SPORTS_ANALYSIS_MODEL_REGISTRY_v1.json', 'SPORTS_ACTIVE_ANALYSIS_MODELS_v1.md',
    'schema/analysis_request.schema.json', 'schema/analysis_output.schema.json', 'schema/analysis_acceptance_traceability_v1.csv', 'src/analysis.mjs',
    'src/journal.mjs', 'src/scoring.mjs', 'scripts/sportsctl.mjs', 'scripts/validate_v3_system.ps1',
  ];
  const checks = [];
  const missing = required.filter((relative) => !existsSync(resolve(ROOT, relative)));
  checks.push({ id: 'RUNTIME-FILES-001', status: missing.length ? 'FAIL' : 'PASS', detail: missing.length ? missing.join(', ') : `${required.length} required files exist` });

  let context;
  try {
    context = runtimeContext();
    checks.push({ id: 'RUNTIME-CONTROLS-001', status: 'PASS', detail: 'machine controls parse' });
  } catch (error) {
    checks.push({ id: 'RUNTIME-CONTROLS-001', status: 'FAIL', detail: error.message });
  }
  if (context) {
    const releaseReport = validateReleaseManifest(context.controls.release, context.coverageRows);
    checks.push({ id: 'RUNTIME-RELEASE-001', status: releaseReport.valid ? 'PASS' : 'FAIL', detail: releaseReport.errors.join('; ') || `${context.controls.release.release_mode}; active=${releaseReport.active_count}` });
    const suspended = context.controls.release.release_mode !== 'OPERATIONAL';
    const coverageErrors = validateCoverageRegistry(context.coverageRows, { suspended });
    checks.push({ id: 'RUNTIME-COVERAGE-001', status: coverageErrors.length ? 'FAIL' : 'PASS', detail: coverageErrors.join('; ') || `${context.coverageRows.length} rows; active=${releaseReport.active_count}` });
    const modelIds = new Set(context.controls.modelRegistry.map((row) => `${row.model_id}:${row.model_version}`));
    const orphanModels = context.coverageRows.filter((row) => row.status === 'DEVELOPMENT' && !modelIds.has(`${row.model_id}:${row.model_version}`));
    checks.push({ id: 'RUNTIME-MODEL-REGISTRY-001', status: orphanModels.length ? 'FAIL' : 'PASS', detail: orphanModels.length ? orphanModels.map((row) => row.coverage_id).join(', ') : `${modelIds.size} development models join` });
    const sources = parseCsv(readFileSync(resolve(ROOT, 'SPORTS_REGISTERED_SOURCES_v1.csv'), 'utf8'));
    const sourceIds = new Set(sources.map((row) => row.source_id));
    const sourceSports = new Set(sources.map((row) => row.sport_family));
    const requiredSports = new Set(context.coverageRows.filter((row) => row.coverage_id !== 'OTHER_SPORT_ALL').map((row) => row.sport_family));
    const missingSourceSports = [...requiredSports].filter((sport) => !sourceSports.has(sport));
    checks.push({ id: 'RUNTIME-SOURCE-REGISTRY-001', status: sourceIds.size === sources.length && missingSourceSports.length === 0 ? 'PASS' : 'FAIL', detail: `sources=${sources.length}; duplicate_ids=${sources.length - sourceIds.size}; missing_sports=${missingSourceSports.join('|') || 'none'}` });
    const controlReport = validateRuntimeControls(context.controls, context.coverageRows);
    checks.push({ id: 'RUNTIME-CONTROL-JOINS-001', status: controlReport.valid ? 'PASS' : 'FAIL', detail: controlReport.errors.join('; ') || 'release/coverage/model/contract/source/test joins reconcile' });
  }

  const fixturePass = Math.abs(brierLoss([0.7, 0.3], 0) - 0.09) < 1e-12
    && Math.abs(logLoss([0.7, 0.3], 1) - 1.2039728043259361) < 1e-12
    && Math.abs(brierLoss([0.55, 0.35, 0.10], 2) - 0.6175) < 1e-12
    && Math.abs(expectedReturn([0.45, 0.45, 0.10], [1, -1, 0])) < 1e-12;
  checks.push({ id: 'RUNTIME-SCORING-001', status: fixturePass ? 'PASS' : 'FAIL', detail: 'canonical Brier/log-loss/EV fixtures' });

  try {
    const analysis = validateAnalysisRegistry(loadAnalysisAssets(ROOT), ROOT);
    checks.push({
      id: 'RUNTIME-ANALYSIS-MODELS-001',
      status: analysis.valid ? 'PASS' : 'FAIL',
      detail: analysis.valid ? `active_analysis_only=${analysis.active_model_count}; numeric_forecast_authorized=false` : analysis.errors.join('; '),
    });
  } catch (error) {
    checks.push({ id: 'RUNTIME-ANALYSIS-MODELS-001', status: 'FAIL', detail: error.message });
  }

  try {
    const store = verifyJournal(DEFAULT_STORE);
    checks.push({ id: 'RUNTIME-JOURNAL-001', status: store.valid ? 'PASS' : 'FAIL', detail: store.valid ? `records=${store.record_count}; head=${store.head_hash}` : store.errors.join('; ') });
  } catch (error) {
    checks.push({ id: 'RUNTIME-JOURNAL-001', status: 'FAIL', detail: error.message });
  }

  const powershell = spawnSync('powershell', ['-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', resolve(ROOT, 'scripts/validate_v3_system.ps1')], {
    cwd: ROOT,
    encoding: 'utf8',
  });
  checks.push({ id: 'POWERSHELL-STATIC-001', status: powershell.status === 0 ? 'PASS' : 'FAIL', detail: powershell.status === 0 ? 'static specification validator passed' : `${powershell.stdout ?? ''}\n${powershell.stderr ?? ''}`.trim() });

  const nodeTests = spawnSync(process.execPath, ['--test', '--test-concurrency=1', 'tests/*.test.mjs'], { cwd: ROOT, encoding: 'utf8' });
  checks.push({ id: 'RUNTIME-TEST-SUITE-001', status: nodeTests.status === 0 ? 'PASS' : 'FAIL', detail: nodeTests.status === 0 ? 'implemented Node tests passed; this is not a claim that the full acceptance matrix is covered' : `${nodeTests.stdout ?? ''}\n${nodeTests.stderr ?? ''}`.slice(-4000) });

  const powerShellVersion = spawnSync('powershell', ['-NoProfile', '-Command', '$PSVersionTable.PSVersion.ToString()'], { encoding: 'utf8' }).stdout.trim();

  const report = {
    report_version: 'SPORTS_RUNTIME_SYSTEM_VALIDATION_V1',
    generated_at_utc: new Date().toISOString(),
    release_id: context?.controls.release.release_id ?? null,
    release_mode: context?.controls.release.release_mode ?? null,
    operational_status: context?.controls.release.operational_status ?? 'UNKNOWN',
    runtime_versions: { node: process.version, powershell: powerShellVersion },
    control_hashes: context?.controlHashes ?? null,
    control_bundle_hash: context?.controlBundleHash ?? null,
    valid: checks.every((check) => check.status === 'PASS'),
    checks,
  };
  for (const check of checks) process.stdout.write(`${check.status.padEnd(6)} ${check.id.padEnd(32)} ${check.detail}\n`);
  process.stdout.write(`\nsystem_valid=${report.valid}; operational_status=${report.operational_status}\n`);
  return report;
}

function help() {
  process.stdout.write(`Sports Research fail-closed CLI\n\n`);
  process.stdout.write(`  validate-system [--output FILE]\n`);
  process.stdout.write(`  analyse-live --input FILE [--output FILE]\n`);
  process.stdout.write(`  init-store [--journal FILE]\n`);
  process.stdout.write(`  new-request --input FILE --output FILE [--record] [--journal FILE]\n`);
  process.stdout.write(`  validate-packet --input FILE\n`);
  process.stdout.write(`  record --input FILE [--journal FILE]\n`);
  process.stdout.write(`  settle --input FILE [--journal FILE]\n`);
  process.stdout.write(`  evaluate --input FILE [--journal FILE]\n`);
  process.stdout.write(`  verify-store [--journal FILE]\n`);
  process.stdout.write(`  recover-anchor --journal FILE --expected-head HASH --expected-count N\n`);
}

async function main() {
  const { command, options } = parseArgs(process.argv.slice(2));
  if (command === 'help' || command === '--help') return help();

  if (command === 'validate-system') {
    const report = validateSystem();
    if (options.output) writeJsonAtomic(absolute(options.output), report);
    if (!report.valid) process.exitCode = 1;
    return;
  }

  if (command === 'analyse-live') {
    if (!options.input) throw new Error('analyse-live requires --input');
    const output = analyseLive(readJson(absolute(options.input)), { root: ROOT });
    if (options.output) writeJsonAtomic(absolute(options.output), output);
    process.stdout.write(`${JSON.stringify(output, null, 2)}\n`);
    return;
  }

  if (command === 'init-store') {
    const report = initializeJournal(absolute(options.journal, DEFAULT_JOURNAL));
    process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
    return;
  }

  if (command === 'verify-store') {
    const report = verifyJournal(absolute(options.journal, DEFAULT_JOURNAL));
    process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
    if (!report.valid) process.exitCode = 1;
    return;
  }

  if (command === 'recover-anchor') {
    if (!options.journal || !options['expected-head'] || !options['expected-count']) throw new Error('recover-anchor requires journal, expected-head and expected-count');
    const report = recoverJournalAnchor(absolute(options.journal), {
      expectedHeadHash: options['expected-head'],
      expectedRecordCount: Number(options['expected-count']),
    });
    process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
    return;
  }

  if (command === 'new-request') {
    if (!options.input || !options.output) throw new Error('new-request requires --input and --output');
    const context = runtimeContext();
    const packet = createInitialDecisionPacket(readJson(absolute(options.input)), context);
    const report = validateDecisionPacket(packet, context);
    printValidation(report);
    if (!report.valid) throw new Error('generated packet did not pass fail-closed validation');
    writeJsonAtomic(absolute(options.output), packet);
    if (options.record) {
      initializeJournal(absolute(options.journal, DEFAULT_JOURNAL));
      appendDecisionPacket(absolute(options.journal, DEFAULT_JOURNAL), packet, context);
    }
    return;
  }

  if (command === 'validate-packet') {
    if (!options.input) throw new Error('validate-packet requires --input');
    const report = validateDecisionPacket(readJson(absolute(options.input)), runtimeContext());
    printValidation(report);
    if (!report.valid) process.exitCode = 1;
    return;
  }

  if (command === 'record') {
    if (!options.input) throw new Error('record requires --input');
    const journal = absolute(options.journal, DEFAULT_JOURNAL);
    initializeJournal(journal);
    const result = appendDecisionPacket(journal, readJson(absolute(options.input)), runtimeContext());
    process.stdout.write(`recorded sequence=${result.record.sequence}; hash=${result.record.record_hash}\n`);
    return;
  }

  if (command === 'settle') {
    if (!options.input) throw new Error('settle requires --input');
    const journal = absolute(options.journal, DEFAULT_JOURNAL);
    initializeJournal(journal);
    const result = appendSettlement(journal, readJson(absolute(options.input)));
    process.stdout.write(`recorded settlement sequence=${result.record.sequence}; hash=${result.record.record_hash}\n`);
    return;
  }

  if (command === 'evaluate') {
    if (!options.input) throw new Error('evaluate requires --input');
    const journal = absolute(options.journal, DEFAULT_JOURNAL);
    initializeJournal(journal);
    const input = readJson(absolute(options.input));
    if (!input.scoring_code_hash) input.scoring_code_hash = hashFile(resolve(ROOT, 'src/scoring.mjs'));
    if (!input.scoring_spec_version) input.scoring_spec_version = SCORING_SPEC_VERSION;
    const result = appendEvaluation(journal, input);
    process.stdout.write(`${JSON.stringify(result.record.payload, null, 2)}\n`);
    return;
  }

  throw new Error(`unknown command ${command}`);
}

main().catch((error) => {
  process.stderr.write(`ERROR: ${error.message}\n`);
  process.exitCode = 1;
});
