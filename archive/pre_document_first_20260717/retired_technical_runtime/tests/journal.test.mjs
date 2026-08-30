import test from 'node:test';
import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { mkdtempSync, readFileSync, rmSync, unlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { hashObject } from '../src/canonical.mjs';
import { loadCoverageRegistry } from '../src/coverage.mjs';
import { appendDecisionPacket, initializeJournal, recoverJournalAnchor, verifyJournal } from '../src/journal.mjs';
import { loadMachineControls } from '../src/packet.mjs';
import { createInitialDecisionPacket } from '../src/workflow.mjs';
import { makeValidIssueFixture, mutateAndFinalize } from './support/valid_issue_fixture.mjs';

const ROOT = resolve(import.meta.dirname, '..');
const context = {
  controls: loadMachineControls(ROOT.replaceAll('\\', '/')),
  coverageRows: loadCoverageRegistry(resolve(ROOT, 'SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv')),
  now: '2026-07-16T12:00:00.000Z',
  controlBundleHash: 'f'.repeat(64),
  controlHashes: { SYNTHETIC_TEST_CONTROLS: 'e'.repeat(64) },
};

function packet() {
  return createInitialDecisionPacket({
    raw_request_text: 'Forecast this match.', primary_question_text: 'Will the home team win?', created_by: 'test',
    event_id: 'MLB:TEST', sport_family: 'Baseball', competition_id: 'MLB', event_start_utc: '2026-07-17T00:00:00Z',
    ruleset_id: 'MLB_2026', market_id: 'MLB:TEST:WIN', market_family: 'winner', selection: 'HOME',
    settlement_convention_id: 'MLB_WINNER_V1', analysis_mode: 'RESEARCH_ONLY', forecast_state: 'PREGAME_CONFIRMED',
    horizon_bucket_id: 'T24H_TO_T0', selection_mode: 'USER_SUPPLIED',
  }, context);
}

function temporaryJournal() {
  const directory = mkdtempSync(join(tmpdir(), 'sports-journal-'));
  return { directory, journal: join(directory, 'journal.jsonl') };
}

function runIndependentAppender(journal) {
  const program = [
    "import { appendDecisionPacket } from './src/journal.mjs';",
    "import { makeValidIssueFixture } from './tests/support/valid_issue_fixture.mjs';",
    'const { packet, context } = makeValidIssueFixture();',
    'try { appendDecisionPacket(process.argv[1], packet, context); process.stdout.write(\'APPENDED\\n\'); }',
    'catch (error) { process.stderr.write(`${error.message}\\n`); process.exitCode = 2; }',
  ].join('\n');
  return new Promise((resolvePromise, rejectPromise) => {
    const child = spawn(process.execPath, ['--input-type=module', '--eval', program, journal], {
      cwd: ROOT,
      windowsHide: true,
      stdio: ['ignore', 'pipe', 'pipe'],
    });
    let stdout = '';
    let stderr = '';
    child.stdout.on('data', (chunk) => { stdout += chunk; });
    child.stderr.on('data', (chunk) => { stderr += chunk; });
    child.on('error', rejectPromise);
    child.on('close', (code) => resolvePromise({ code, stdout, stderr }));
  });
}

test('journal appends a validated packet and blocks a sequential duplicate snapshot_id', () => {
  const { directory, journal } = temporaryJournal();
  try {
    initializeJournal(journal);
    const frozen = packet();
    appendDecisionPacket(journal, frozen, context);
    assert.equal(verifyJournal(journal).record_count, 1);
    assert.throws(() => appendDecisionPacket(journal, frozen, context), /duplicate snapshot_id/);
    assert.equal(verifyJournal(journal).valid, true);
    assert.equal(verifyJournal(journal).record_count, 1);
  } finally { rmSync(directory, { recursive: true, force: true }); }
});

test('journal blocks a duplicate prediction_id even when snapshot_id is new', () => {
  const { directory, journal } = temporaryJournal();
  try {
    initializeJournal(journal);
    const { packet: first, context: issueContext } = makeValidIssueFixture();
    appendDecisionPacket(journal, first, issueContext);
    const successor = mutateAndFinalize(first, (packet) => {
      packet.decision_snapshot.parent_snapshot_id = first.decision_snapshot.snapshot_id;
      packet.decision_snapshot.snapshot_id = 'SNAP-VALID-ISSUE-2';
      packet.decision_snapshot.snapshot_sequence = 2;
      packet.prediction.snapshot_id = 'SNAP-VALID-ISSUE-2';
      const { source_packet_hash: _priorSourcePacketHash, ...sourcePacketHashMaterial } = packet.source_packet;
      sourcePacketHashMaterial.snapshot_id = 'SNAP-VALID-ISSUE-2';
      packet.source_packet = {
        ...sourcePacketHashMaterial,
        source_packet_hash: hashObject(sourcePacketHashMaterial),
      };
    });
    assert.throws(() => appendDecisionPacket(journal, successor, issueContext), /duplicate prediction_id/);
    assert.equal(verifyJournal(journal).record_count, 1);
  } finally { rmSync(directory, { recursive: true, force: true }); }
});

test('payload mutation and tail truncation are detected by chain/anchor', () => {
  const { directory, journal } = temporaryJournal();
  try {
    initializeJournal(journal);
    appendDecisionPacket(journal, packet(), context);
    const original = readFileSync(journal, 'utf8');
    writeFileSync(journal, original.replace('Forecast this match.', 'Forecast altered match.'), 'utf8');
    assert.equal(verifyJournal(journal).valid, false);
    writeFileSync(journal, '', 'utf8');
    const truncated = verifyJournal(journal);
    assert.equal(truncated.valid, false);
    assert.ok(truncated.errors.some((error) => error.includes('record_count')));
  } finally { rmSync(directory, { recursive: true, force: true }); }
});

test('two real concurrent appenders cannot both commit the same semantic record', async () => {
  const { directory, journal } = temporaryJournal();
  try {
    initializeJournal(journal);
    const results = await Promise.all([runIndependentAppender(journal), runIndependentAppender(journal)]);
    assert.deepEqual(results.map((result) => result.code).sort(), [0, 2], JSON.stringify(results, null, 2));
    assert.equal(results.filter((result) => result.stdout.includes('APPENDED')).length, 1);
    assert.ok(results.find((result) => result.code === 2).stderr.match(/locked|duplicate snapshot_id/));
    const report = verifyJournal(journal);
    assert.equal(report.valid, true, report.errors.join('; '));
    assert.equal(report.record_count, 1);
  } finally { rmSync(directory, { recursive: true, force: true }); }
});

test('missing anchor fails closed and recovery requires external head and count', () => {
  const { directory, journal } = temporaryJournal();
  try {
    initializeJournal(journal);
    appendDecisionPacket(journal, packet(), context);
    const before = verifyJournal(journal);
    unlinkSync(join(directory, 'head_anchor.json'));
    assert.throws(() => initializeJournal(journal), /no anchor/);
    assert.throws(() => recoverJournalAnchor(journal, { expectedHeadHash: '0'.repeat(64), expectedRecordCount: 0 }), /does not match/);
    assert.equal(recoverJournalAnchor(journal, { expectedHeadHash: before.head_hash, expectedRecordCount: before.record_count }).valid, true);
  } finally { rmSync(directory, { recursive: true, force: true }); }
});
