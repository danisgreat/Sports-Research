import { mkdirSync, renameSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { readJournal, verifyJournal } from './journal.mjs';

export const DEFAULT_PREDICTION_LOG = 'PREDICTION_RESULTS_LOG_v5.md';

function clean(value) {
  if (value === null || value === undefined || value === '') return 'N/A';
  return String(value).replaceAll('\r', ' ').replaceAll('\n', ' ').trim();
}

function participantName(input, participantId) {
  if (!participantId) return 'TOSSUP';
  return input.participants?.find((participant) => participant.participant_id === participantId)?.name ?? participantId;
}

function publicationLines(publication) {
  if (!publication) return ['RECORDED USER-FACING RANKING: NOT CAPTURED IN A STRUCTURED PUBLICATION RECORD'];
  return [
    `PUBLICATION: ${clean(publication.headline)}`,
    ...publication.ranked_selections
      .toSorted((left, right) => left.rank - right.rank)
      .map((item) => `PICK ${item.rank}: ${clean(item.selection)} — ${clean(item.verdict)} — ${clean(item.rationale)}`),
    `POTENTIAL WINNER: ${clean(publication.potential_winner)}`,
    `PUBLIC SUMMARY: ${clean(publication.public_summary)}`,
    `PUBLICATION ID: ${publication.publication_id}`,
  ];
}

function decisionEntry(record, settlements, evaluations, publications) {
  const packet = record.payload.packet;
  const request = packet.request;
  const snapshot = packet.decision_snapshot;
  const prediction = packet.prediction;
  const relatedSettlements = prediction
    ? settlements.filter((item) => item.payload.prediction_id === prediction.prediction_id)
    : [];
  const latestSettlement = relatedSettlements.at(-1)?.payload;
  const relatedEvaluations = prediction
    ? evaluations.filter((item) => item.payload.prediction_id === prediction.prediction_id)
    : [];
  const latestEvaluation = relatedEvaluations.at(-1)?.payload;
  const publication = publications.find((item) => item.payload.snapshot_id === snapshot.snapshot_id)?.payload;
  const formalSelection = prediction
    ? `${clean(request.selection)}${request.line === null ? '' : ` ${clean(request.line)}`}`
    : 'NONE — abstained';
  return [
    `## Entry ${record.sequence} — ${clean(request.event_name ?? request.event_id)}`,
    '',
    '```text',
    `JOURNAL SEQUENCE: ${record.sequence}`,
    `RECORDED UTC: ${record.recorded_at_utc}`,
    `SPORT / COMPETITION: ${clean(request.sport_family)} / ${clean(request.competition_id)}`,
    `EVENT: ${clean(request.event_name ?? request.event_id)}`,
    `EVENT START UTC: ${clean(request.event_start_utc)}`,
    `MARKET: ${clean(request.market_family)} (${clean(request.market_id)})`,
    `STATE / CUTOFF UTC: ${clean(request.forecast_state)} / ${clean(snapshot.data_cutoff_utc)}`,
    `USER REQUEST: ${clean(request.raw_request_text)}`,
    `PRIMARY QUESTION: ${clean(request.primary_question_text)}`,
    `DECISION: ${snapshot.decision}${snapshot.pass_reason ? ` / ${snapshot.pass_reason}` : ''}`,
    `FORMAL SELECTION: ${formalSelection}`,
    ...publicationLines(publication),
    `RESEARCH / PICKS NOTE: ${clean(snapshot.research_note)}`,
    `RESULT: ${latestSettlement ? `${latestSettlement.grade} (${latestSettlement.official_event_status})` : 'PENDING OR NOT ELIGIBLE'}`,
    `EVALUATION: ${latestEvaluation ? clean(latestEvaluation.evaluation_id) : 'NOT AVAILABLE'}`,
    `REQUEST ID: ${request.request_id}`,
    `SNAPSHOT ID: ${snapshot.snapshot_id}`,
    `PREDICTION ID: ${clean(prediction?.prediction_id)}`,
    `RECORD HASH: ${record.record_hash}`,
    '```',
    '',
  ].join('\n');
}

function analysisEntry(record, publications) {
  const { input, output } = record.payload;
  const sources = input.source_observations.map((source) => source.source_url).join(' | ');
  const publication = publications.find((item) => item.payload.analysis_id === output.analysis_id)?.payload;
  return [
    `## Entry ${record.sequence} — ${input.participants.map((participant) => participant.name).join(' vs ')}`,
    '',
    '```text',
    `JOURNAL SEQUENCE: ${record.sequence}`,
    `RECORDED UTC: ${record.recorded_at_utc}`,
    `SPORT / COMPETITION: ${output.sport_family} / ${output.competition_id}`,
    `EVENT: ${input.participants.map((participant) => participant.name).join(' vs ')}`,
    `MARKET / STATE: ${output.market_family} / ${output.forecast_state}`,
    `AS OF UTC: ${output.as_of_utc}`,
    `ANALYSIS LEAN: ${participantName(input, output.lean.participant_id)} — ${output.lean.strength}`,
    `STATE SUMMARY: ${clean(output.lean.state_summary)}`,
    `REASON CODES: ${output.lean.reason_codes.join(', ')}`,
    `MODEL: ${output.model_id} ${output.model_version}`,
    ...publicationLines(publication),
    `SOURCES: ${sources}`,
    'NUMERIC FORECAST: NOT AUTHORIZED',
    'RESULT: PENDING / QUALITATIVE ANALYSIS ONLY',
    `ANALYSIS ID: ${output.analysis_id}`,
    `INPUT HASH: ${output.input_hash}`,
    `RECORD HASH: ${record.record_hash}`,
    '```',
    '',
  ].join('\n');
}

export function renderPredictionLog(journalPath, outputPath = DEFAULT_PREDICTION_LOG) {
  const verification = verifyJournal(journalPath);
  if (!verification.valid) throw new Error(`cannot render prediction log from invalid journal: ${verification.errors.join('; ')}`);
  const records = readJournal(journalPath);
  const decisions = records.filter((record) => record.record_type === 'DECISION_PACKET');
  const analyses = records.filter((record) => record.record_type === 'ANALYSIS_OUTPUT');
  const settlements = records.filter((record) => record.record_type === 'SETTLEMENT');
  const evaluations = records.filter((record) => record.record_type === 'EVALUATION');
  const publications = records.filter((record) => record.record_type === 'PUBLICATION');
  const entries = records
    .filter((record) => record.record_type === 'DECISION_PACKET' || record.record_type === 'ANALYSIS_OUTPUT')
    .map((record) => record.record_type === 'DECISION_PACKET'
      ? decisionEntry(record, settlements, evaluations, publications)
      : analysisEntry(record, publications));
  const markdown = [
    '# Prediction results log v5',
    '',
    'Status: GENERATED, COPY-FRIENDLY VIEW',
    '',
    'This document contains every recorded decision packet and every recorded qualitative live analysis. The verified append-only journal remains the machine source of truth; regenerate this file instead of hand-editing it.',
    '',
    '## Current verified state',
    '',
    `- Journal records: ${verification.record_count}`,
    `- Decision packets: ${decisions.length}`,
    `- Qualitative live analyses: ${analyses.length}`,
    `- Structured user-facing publications: ${publications.length}`,
    `- Quantitative ISSUE records: ${decisions.filter((record) => record.payload.packet.decision_snapshot.decision === 'ISSUE').length}`,
    `- Settlements: ${settlements.length}`,
    `- Evaluations: ${evaluations.length}`,
    `- Journal head: \`${verification.head_hash}\``,
    '',
    '## Copy-and-paste entries',
    '',
    ...(entries.length ? entries : ['No recorded predictions or analysis decisions.', '']),
    '## Historical boundary',
    '',
    'Legacy v2–v4 rows remain historical and are not silently imported into this verified view. They may be consulted only as labelled retrospective evidence.',
    '',
  ].join('\n');
  const absoluteOutput = resolve(outputPath);
  mkdirSync(dirname(absoluteOutput), { recursive: true });
  const temporary = `${absoluteOutput}.tmp-${process.pid}-${Date.now()}`;
  writeFileSync(temporary, markdown, { encoding: 'utf8', flag: 'wx' });
  renameSync(temporary, absoluteOutput);
  return { output_path: absoluteOutput, ...verification, rendered_entry_count: entries.length };
}
