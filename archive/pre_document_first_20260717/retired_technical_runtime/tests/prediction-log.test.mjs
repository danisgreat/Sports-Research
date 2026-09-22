import assert from 'node:assert/strict';
import { mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import test from 'node:test';
import { hashObject } from '../src/canonical.mjs';
import { appendAnalysisOutput, appendDecisionPacket, appendPublication, initializeJournal, verifyJournal } from '../src/journal.mjs';
import { renderPredictionLog } from '../src/prediction-log.mjs';
import { loadCoverageRegistry } from '../src/coverage.mjs';
import { loadMachineControls } from '../src/packet.mjs';
import { createInitialDecisionPacket } from '../src/workflow.mjs';
import { resolve } from 'node:path';

const ROOT = resolve(import.meta.dirname, '..');
const context = {
  controls: loadMachineControls(ROOT.replaceAll('\\', '/')),
  coverageRows: loadCoverageRegistry(resolve(ROOT, 'SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv')),
  now: '2026-07-17T02:00:00.000Z',
  controlBundleHash: 'f'.repeat(64),
  controlHashes: { SYNTHETIC_TEST_CONTROLS: 'e'.repeat(64) },
};

function passPacket() {
  return createInitialDecisionPacket({
    raw_request_text: 'Research this event and record the decision.',
    primary_question_text: 'Is an issued forecast supported?',
    created_by: 'test',
    sport_family: 'Baseball',
    competition_id: 'LMB',
    event_name: 'Away at Home',
    event_start_utc: '2026-07-17T03:00:00.000Z',
    analysis_mode: 'RESEARCH_ONLY',
    forecast_state: 'LIVE',
    selection_mode: 'USER_SUPPLIED',
    research_note: 'No exact registered contract was available, so the request was recorded as an abstention.',
  }, context);
}

function qualitativeRecord() {
  const input = {
    analysis_id: 'ANALYSIS-TEST-001',
    participants: [{ participant_id: 'A', name: 'Away' }, { participant_id: 'H', name: 'Home' }],
    source_observations: [{ source_id: 'TEST', source_url: 'https://example.test/live', content_hash: 'a'.repeat(64) }],
  };
  const output = {
    schema_version: 'SPORTS_ANALYSIS_OUTPUT_V1',
    analysis_id: input.analysis_id,
    analysis_tier: 'ACTIVE_ANALYSIS_ONLY',
    model_id: 'ANALYSIS_TEST_V1',
    model_version: '1.0.0',
    sport_family: 'Baseball',
    competition_id: 'MLB',
    market_family: 'winner',
    forecast_state: 'LIVE',
    as_of_utc: '2026-07-17T01:59:00.000Z',
    numeric_forecast_authorized: false,
    lean: { classification: 'SIDE', participant_id: 'H', strength: 'MODERATE', reason_codes: ['TEST'], state_summary: 'Home leads late.' },
    input_hash: hashObject(input),
    source_snapshot_hash: hashObject(input.source_observations),
    model_code_hash: 'b'.repeat(64),
  };
  return { input, output };
}

test('copy-friendly prediction log renders every decision and qualitative analysis record', () => {
  const directory = mkdtempSync(join(tmpdir(), 'sports-prediction-log-'));
  const journal = join(directory, 'journal.jsonl');
  const log = join(directory, 'predictions.md');
  try {
    initializeJournal(journal);
    const decision = passPacket();
    appendDecisionPacket(journal, decision, context);
    appendPublication(journal, {
      publication_id: 'PUBLICATION-TEST-001',
      published_at_utc: '2026-07-17T02:01:00.000Z',
      snapshot_id: decision.decision_snapshot.snapshot_id,
      analysis_id: null,
      headline: 'Away at Home ranked markets',
      ranked_selections: [{ rank: 1, selection: 'Over 8.5', verdict: 'PASS', rationale: 'No active model.' }],
      potential_winner: 'Home',
      public_summary: 'No formal forecast was issued.',
      created_by: 'test',
    });
    const qualitative = qualitativeRecord();
    appendAnalysisOutput(journal, qualitative.input, qualitative.output);
    const report = renderPredictionLog(journal, log);
    const text = readFileSync(log, 'utf8');
    assert.equal(report.rendered_entry_count, 2);
    assert.match(text, /Away at Home/);
    assert.match(text, /ANALYSIS LEAN: Home — MODERATE/);
    assert.match(text, /DECISION: PASS \/ CONTRACT_UNRESOLVED/);
    assert.match(text, /PICK 1: Over 8.5 — PASS — No active model\./);
    assert.equal(verifyJournal(journal).analysis_count, 1);
    assert.equal(verifyJournal(journal).publication_count, 1);
    assert.throws(() => appendAnalysisOutput(journal, qualitative.input, qualitative.output), /duplicate analysis_id/);
  } finally {
    rmSync(directory, { recursive: true, force: true });
  }
});
