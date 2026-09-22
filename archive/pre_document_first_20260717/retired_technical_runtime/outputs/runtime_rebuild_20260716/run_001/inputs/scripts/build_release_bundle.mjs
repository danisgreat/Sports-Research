#!/usr/bin/env node
import {
  copyFileSync, existsSync, mkdirSync, readdirSync, statSync, writeFileSync,
} from 'node:fs';
import { dirname, relative, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import { hashFile, hashObject } from '../src/canonical.mjs';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const SKIP_DIRECTORIES = new Set(['node_modules', 'outputs', '.git']);

function parseArgs(argv) {
  const options = {};
  for (let index = 0; index < argv.length; index += 1) {
    if (!argv[index].startsWith('--')) throw new Error(`unexpected argument ${argv[index]}`);
    const name = argv[index].slice(2);
    const value = argv[index + 1];
    if (!value || value.startsWith('--')) throw new Error(`--${name} requires a value`);
    options[name] = value;
    index += 1;
  }
  return options;
}

function normalized(path) {
  return path.split(sep).join('/');
}

function filesUnder(directory, base = directory) {
  const result = [];
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    if (entry.isDirectory() && SKIP_DIRECTORIES.has(entry.name)) continue;
    const path = resolve(directory, entry.name);
    if (entry.isDirectory()) result.push(...filesUnder(path, base));
    else if (entry.isFile()) result.push(path);
  }
  return result;
}

function isOperative(relativePath) {
  if (/^(src|scripts|schema|templates|tests|runtime\/store)\//u.test(relativePath)) return true;
  return /^(?:package(?:-lock)?\.json|README\.md|SPORTS_RESEARCH_AUTHORITY_MANIFEST\.md|SPORTS_RELEASE_MANIFEST_v1\.json|combined_sports_doc_v3\.md|SPORTS_(?:DATA_DICTIONARY|MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK|SOURCE_REGISTRY|SCORING_SPECIFICATION|ACCEPTANCE_TESTS)_v3\.md|SPORTS_(?:MODEL_COVERAGE_REGISTRY_v3|MODEL_REGISTRY_v1|REGISTERED_SOURCES_v1|CALIBRATION_LEDGER_v3|SETTLEMENTS_v3)\.csv|SPORTS_DEVELOPMENT_MODEL_CATALOG_v1\.md|NEXT_TIME_MODEL_DEVELOPMENT_PLAYBOOK_v1\.md|RESEARCH_RETROSPECTIVE_2026-07-16\.md|PRE_RUNTIME_PASS_MIGRATION_AUDIT_20260716\.csv|PREDICTION_RESULTS_LOG_v5\.md)$/u.test(relativePath);
}

function run(command, args, outputPath) {
  const result = spawnSync(command, args, { cwd: ROOT, encoding: 'utf8', windowsHide: true });
  const text = [
    `command: ${command} ${args.join(' ')}`,
    `exit_code: ${result.status ?? 'null'}`,
    '',
    '--- stdout ---',
    result.stdout ?? '',
    '--- stderr ---',
    result.stderr ?? '',
    result.error ? `--- spawn error ---\n${result.error.message}` : '',
  ].join('\n');
  writeFileSync(outputPath, text, { encoding: 'utf8', flag: 'wx' });
  return { exit_code: result.status, output_file: normalized(relative(ROOT, outputPath)) };
}

function version(command, args) {
  const result = spawnSync(command, args, { cwd: ROOT, encoding: 'utf8', windowsHide: true });
  return result.status === 0 ? String(result.stdout).trim() : `UNAVAILABLE: ${String(result.stderr || result.error?.message).trim()}`;
}

const options = parseArgs(process.argv.slice(2));
if (!options.output) throw new Error('usage: node scripts/build_release_bundle.mjs --output NEW_DIRECTORY');
const output = resolve(ROOT, options.output);
if (existsSync(output)) throw new Error(`refusing to overwrite existing release bundle ${output}`);
mkdirSync(output, { recursive: true });
mkdirSync(resolve(output, 'inputs'), { recursive: true });

const workspaceFiles = filesUnder(ROOT).filter((path) => !normalized(relative(ROOT, path)).startsWith('outputs/'));
const inventory = workspaceFiles.map((path) => {
  const relativePath = normalized(relative(ROOT, path));
  return {
    path: relativePath,
    size_bytes: statSync(path).size,
    sha256: hashFile(path),
    classification: isOperative(relativePath) ? 'OPERATIVE_OR_TEST_INPUT' : 'HISTORICAL_OR_RAW_EVIDENCE',
  };
}).sort((left, right) => left.path.localeCompare(right.path, 'en'));
writeFileSync(resolve(output, 'workspace_inventory.json'), `${JSON.stringify(inventory, null, 2)}\n`, { encoding: 'utf8', flag: 'wx' });

for (const item of inventory.filter((entry) => entry.classification === 'OPERATIVE_OR_TEST_INPUT')) {
  const destination = resolve(output, 'inputs', item.path);
  mkdirSync(dirname(destination), { recursive: true });
  copyFileSync(resolve(ROOT, item.path), destination, 0);
}

const commands = {
  node_tests: run('npm.cmd', ['test'], resolve(output, 'node_tests.txt')),
  static_validation: run('powershell', ['-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', resolve(ROOT, 'scripts/validate_v3_system.ps1')], resolve(output, 'static_validation.txt')),
  system_validation: run(process.execPath, ['scripts/sportsctl.mjs', 'validate-system', '--output', resolve(output, 'system_validation.json')], resolve(output, 'system_validation.txt')),
};

const evidenceFiles = filesUnder(output).filter((path) => !normalized(relative(output, path)).startsWith('inputs/'));
const evidence = evidenceFiles.map((path) => ({
  path: normalized(relative(output, path)), size_bytes: statSync(path).size, sha256: hashFile(path),
})).sort((left, right) => left.path.localeCompare(right.path, 'en'));

const manifest = {
  manifest_version: 'SPORTS_NO_CLOBBER_RELEASE_BUNDLE_V1',
  generated_at_utc: new Date().toISOString(),
  bundle_path: normalized(relative(ROOT, output)),
  no_clobber_enforced: true,
  status: Object.values(commands).every((item) => item.exit_code === 0) ? 'PASS' : 'FAIL',
  environment: {
    platform: process.platform,
    architecture: process.arch,
    node: process.version,
    npm: version('npm.cmd', ['--version']),
    powershell: version('powershell', ['-NoProfile', '-Command', '$PSVersionTable.PSVersion.ToString()']),
    git: version('git', ['--version']),
    repository_state: existsSync(resolve(ROOT, '.git')) ? 'GIT_METADATA_PRESENT' : 'NOT_A_GIT_REPOSITORY',
  },
  commands,
  inventory_file: 'workspace_inventory.json',
  inventory_entry_count: inventory.length,
  operative_input_count: inventory.filter((entry) => entry.classification === 'OPERATIVE_OR_TEST_INPUT').length,
  evidence,
  limitations: [
    'The bundle validates framework controls; it does not validate or activate a fitted sports model.',
    'Historical/raw evidence is hashed in the inventory but only operative/test inputs are copied into the bundle.',
    'The local journal anchor is tamper-evident, not an external immutable timestamp.',
  ],
};
manifest.bundle_manifest_hash = hashObject(manifest);
writeFileSync(resolve(output, 'run_manifest.json'), `${JSON.stringify(manifest, null, 2)}\n`, { encoding: 'utf8', flag: 'wx' });

process.stdout.write(`${manifest.status} ${manifest.bundle_path} ${manifest.bundle_manifest_hash}\n`);
if (manifest.status !== 'PASS') process.exitCode = 1;
