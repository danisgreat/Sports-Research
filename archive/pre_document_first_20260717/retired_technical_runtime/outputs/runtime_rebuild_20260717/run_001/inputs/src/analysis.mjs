import Ajv2020 from 'ajv/dist/2020.js';
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  hashFile, hashObject, isSha256, parseUtc, readJson,
} from './canonical.mjs';
import { parseCsv } from './csv.mjs';

export const ANALYSIS_REQUEST_VERSION = 'SPORTS_ANALYSIS_REQUEST_V1';
export const ANALYSIS_OUTPUT_VERSION = 'SPORTS_ANALYSIS_OUTPUT_V1';
export const ANALYSIS_TIER = 'ACTIVE_ANALYSIS_ONLY';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const EXPECTED_SPORTS = new Set(['Baseball', 'Cricket', 'Soccer', 'Australian football', 'Rugby league']);
const PROHIBITED_CLAIMS = Object.freeze([
  'calibrated_probability', 'betting_edge', 'expected_value', 'stake', 'profitability',
]);

function clamp(value, lower = 0, upper = 1) {
  return Math.min(upper, Math.max(lower, value));
}

function activeModelFor(registry, sportFamily, competitionId) {
  return registry.models.find((model) => model.status === ANALYSIS_TIER
    && model.sport_family === sportFamily
    && (model.competition_scope.includes('*') || model.competition_scope.includes(competitionId)));
}

function assertParticipants(input) {
  const ids = input.participants.map((participant) => participant.participant_id);
  if (new Set(ids).size !== 2) throw new Error('participants must contain exactly two unique participant IDs');
  return new Set(ids);
}

function participant(ids, value, field) {
  if (!ids.has(value)) throw new Error(`${field} does not reference a declared participant`);
  return value;
}

function tossup(reasonCodes, stateSummary) {
  return {
    classification: 'TOSSUP', participant_id: null, strength: 'NONE', reason_codes: reasonCodes, state_summary: stateSummary,
  };
}

function sideLean(participantId, strength, reasonCodes, stateSummary) {
  return {
    classification: 'SIDE', participant_id: participantId, strength, reason_codes: reasonCodes, state_summary: stateSummary,
  };
}

function strengthFromRatio(ratio) {
  if (ratio >= 1.5) return 'STRONG';
  if (ratio >= 0.8) return 'MODERATE';
  return 'SLIGHT';
}

function analyseBaseball(state, ids) {
  const home = participant(ids, state.home_participant_id, 'home_participant_id');
  const away = participant(ids, state.away_participant_id, 'away_participant_id');
  if (home === away) throw new Error('baseball home and away participants must differ');
  const difference = state.home_runs - state.away_runs;
  const halfProgress = state.half === 'BOTTOM' ? 0.5 : 0;
  const progress = clamp(((state.inning - 1) + halfProgress) / state.scheduled_innings);
  const summary = `${state.away_runs}-${state.home_runs}; ${state.half} ${state.inning}; ${state.outs} out(s)`;

  if (difference === 0) {
    if (state.half === 'BOTTOM' && state.inning >= state.scheduled_innings && state.bases_occupied.length > 0) {
      return sideLean(home, 'SLIGHT', ['TIED_WALK_OFF_THREAT'], summary);
    }
    return tossup(['SCORE_TIED'], summary);
  }

  const leader = difference > 0 ? home : away;
  let leverage = Math.abs(difference) * (0.4 + 0.6 * progress);
  if (leader === away && state.half === 'BOTTOM' && state.inning >= state.scheduled_innings) {
    leverage -= 0.12 * state.bases_occupied.length;
  }
  const reasonCodes = [difference > 0 ? 'HOME_RUN_LEAD' : 'AWAY_RUN_LEAD'];
  if (progress >= 0.75) reasonCodes.push('LATE_INNINGS_LEVERAGE');
  return sideLean(leader, strengthFromRatio(Math.max(0.01, leverage)), reasonCodes, summary);
}

function analyseCricket(state, ids) {
  const first = participant(ids, state.first_batting_participant_id, 'first_batting_participant_id');
  const chasing = participant(ids, state.chasing_participant_id, 'chasing_participant_id');
  if (first === chasing) throw new Error('cricket batting participants must differ');
  if (state.balls_bowled >= state.scheduled_balls) throw new Error('LIVE chase must have balls remaining');
  if (state.wickets_lost >= state.max_wickets) throw new Error('LIVE chase must have wickets remaining');
  if (state.current_runs >= state.target_runs) throw new Error('target already reached; state is FINAL, not LIVE');
  if (state.target_runs !== state.first_innings_runs + 1) throw new Error('STANDARD target must equal first-innings runs plus one');
  if (state.first_innings_balls > state.scheduled_balls) throw new Error('first-innings balls cannot exceed scheduled balls');

  const ballsRemaining = state.scheduled_balls - state.balls_bowled;
  const runsRemaining = state.target_runs - state.current_runs;
  const wicketsRemaining = state.max_wickets - state.wickets_lost;
  const firstInningsRate = (state.first_innings_runs / state.first_innings_balls) * 6;
  const requiredRate = (runsRemaining / ballsRemaining) * 6;
  const ballsFraction = ballsRemaining / state.scheduled_balls;
  const wicketsFraction = wicketsRemaining / state.max_wickets;
  const rateSignal = Math.log(firstInningsRate / requiredRate);
  const resourceSignal = 0.65 * Math.log(wicketsFraction / Math.max(0.05, ballsFraction));
  const score = rateSignal + resourceSignal;
  const summary = `${state.current_runs}/${state.wickets_lost}, target ${state.target_runs}; ${runsRemaining} from ${ballsRemaining} ball(s)`;
  const reasons = [];
  reasons.push(rateSignal >= 0 ? 'CHASE_RATE_FAVOURS_CHASER' : 'CHASE_RATE_FAVOURS_DEFENDER');
  reasons.push(resourceSignal >= 0 ? 'WICKET_RESOURCE_FAVOURS_CHASER' : 'WICKET_RESOURCE_FAVOURS_DEFENDER');
  if (Math.abs(score) < 0.04) return tossup([...reasons, 'SIGNALS_NEAR_BALANCED'], summary);
  const leader = score > 0 ? chasing : first;
  const magnitude = Math.abs(score);
  const strength = magnitude >= 0.65 ? 'STRONG' : magnitude >= 0.25 ? 'MODERATE' : 'SLIGHT';
  return sideLean(leader, strength, reasons, summary);
}

function analyseSoccer(state, ids) {
  const home = participant(ids, state.home_participant_id, 'home_participant_id');
  const away = participant(ids, state.away_participant_id, 'away_participant_id');
  if (home === away) throw new Error('soccer home and away participants must differ');
  if (state.elapsed_minutes > state.regulation_minutes) throw new Error('analysis-only soccer scope excludes extra time');
  const difference = state.home_goals - state.away_goals;
  const progress = clamp(state.elapsed_minutes / state.regulation_minutes);
  const summary = `${state.home_goals}-${state.away_goals}; minute ${state.elapsed_minutes}; red cards ${state.home_red_cards}-${state.away_red_cards}`;

  if (difference === 0) {
    const redAdvantage = state.away_red_cards - state.home_red_cards;
    if (redAdvantage !== 0 && progress >= 0.25) {
      return sideLean(redAdvantage > 0 ? home : away, 'SLIGHT', ['SCORE_TIED', 'PLAYER_COUNT_ADVANTAGE'], summary);
    }
    return tossup(['SCORE_TIED'], summary);
  }
  const leader = difference > 0 ? home : away;
  let leverage = Math.abs(difference) * (0.6 + 1.4 * progress);
  const leaderRedCards = leader === home ? state.home_red_cards : state.away_red_cards;
  const trailerRedCards = leader === home ? state.away_red_cards : state.home_red_cards;
  leverage += 0.25 * (trailerRedCards - leaderRedCards);
  const reasons = ['GOAL_LEAD'];
  if (progress >= 0.75) reasons.push('LATE_MATCH_LEVERAGE');
  if (leaderRedCards !== trailerRedCards) reasons.push('PLAYER_COUNT_ADJUSTMENT');
  return sideLean(leader, strengthFromRatio(Math.max(0.01, leverage)), reasons, summary);
}

function analyseAfl(state, ids) {
  const home = participant(ids, state.home_participant_id, 'home_participant_id');
  const away = participant(ids, state.away_participant_id, 'away_participant_id');
  if (home === away) throw new Error('AFL home and away participants must differ');
  if (state.seconds_remaining_in_period > state.nominal_period_seconds) throw new Error('AFL period time remaining exceeds the supplied nominal period');
  const difference = state.home_points - state.away_points;
  const periodProgress = 1 - (state.seconds_remaining_in_period / state.nominal_period_seconds);
  const progress = clamp(((state.period_number - 1) + periodProgress) / 4);
  const uncertaintyMargin = Math.max(6, 30 * (1 - progress));
  const ratio = Math.abs(difference) / uncertaintyMargin;
  const summary = `${state.home_points}-${state.away_points}; Q${state.period_number} ${state.seconds_remaining_in_period}s remaining`;
  if (difference === 0 || ratio < 0.35) return tossup([difference === 0 ? 'SCORE_TIED' : 'MARGIN_WITHIN_LIVE_VARIANCE'], summary);
  const reasons = ['SCORE_LEAD'];
  if (progress >= 0.75) reasons.push('LATE_MATCH_LEVERAGE');
  return sideLean(difference > 0 ? home : away, strengthFromRatio(ratio), reasons, summary);
}

function analyseNrl(state, ids) {
  const home = participant(ids, state.home_participant_id, 'home_participant_id');
  const away = participant(ids, state.away_participant_id, 'away_participant_id');
  if (home === away) throw new Error('NRL home and away participants must differ');
  const difference = state.home_points - state.away_points;
  const progress = clamp(state.elapsed_minutes / state.regulation_minutes);
  const uncertaintyMargin = Math.max(4, 18 * (1 - progress));
  const ratio = Math.abs(difference) / uncertaintyMargin;
  const summary = `${state.home_points}-${state.away_points}; minute ${state.elapsed_minutes}`;
  if (difference === 0 || ratio < 0.3) return tossup([difference === 0 ? 'SCORE_TIED' : 'MARGIN_WITHIN_LIVE_VARIANCE'], summary);
  const reasons = ['SCORE_LEAD'];
  if (progress >= 0.75) reasons.push('LATE_MATCH_LEVERAGE');
  return sideLean(difference > 0 ? home : away, strengthFromRatio(ratio), reasons, summary);
}

const ANALYSERS = new Map([
  ['Baseball', analyseBaseball],
  ['Cricket', analyseCricket],
  ['Soccer', analyseSoccer],
  ['Australian football', analyseAfl],
  ['Rugby league', analyseNrl],
]);

export function loadAnalysisAssets(root = ROOT) {
  const registryPath = resolve(root, 'SPORTS_ANALYSIS_MODEL_REGISTRY_v1.json');
  const requestSchemaPath = resolve(root, 'schema/analysis_request.schema.json');
  const outputSchemaPath = resolve(root, 'schema/analysis_output.schema.json');
  const traceabilityPath = resolve(root, 'schema/analysis_acceptance_traceability_v1.csv');
  const registry = readJson(registryPath);
  const sources = parseCsv(readFileSync(resolve(root, 'SPORTS_REGISTERED_SOURCES_v1.csv'), 'utf8'));
  const ajv = new Ajv2020({ allErrors: true, strict: true, allowUnionTypes: true });
  return {
    registry,
    sources,
    traceability: parseCsv(readFileSync(traceabilityPath, 'utf8')),
    requestSchemaPath,
    outputSchemaPath,
    validateRequest: ajv.compile(readJson(requestSchemaPath)),
    validateOutput: ajv.compile(readJson(outputSchemaPath)),
  };
}

export function validateAnalysisRegistry(assets, root = ROOT, { now = Date.now() } = {}) {
  const errors = [];
  const { registry, sources } = assets;
  if (registry?.schema_version !== 'SPORTS_ANALYSIS_MODEL_REGISTRY_V1') errors.push('invalid analysis registry schema version');
  if (registry?.tier_status !== ANALYSIS_TIER) errors.push('analysis registry tier is not ACTIVE_ANALYSIS_ONLY');
  if (registry?.numeric_forecast_authorized !== false) errors.push('analysis registry must prohibit numeric forecasts');
  if (!Array.isArray(registry?.models)) errors.push('analysis registry models must be an array');
  const traceability = assets.traceability ?? [];
  const traceabilityIds = new Set(traceability.map((row) => row.requirement_id));
  if (traceability.length !== registry?.expected_acceptance_requirement_count) errors.push('analysis acceptance requirement count mismatch');
  if (traceabilityIds.size !== traceability.length || traceability.some((row) => !row.requirement_id)) errors.push('analysis acceptance requirement IDs must be unique and nonempty');
  if (traceability.some((row) => row.status !== 'COVERED' || !row.test_file || !row.test_name || !row.notes)) errors.push('analysis acceptance traceability contains an incomplete requirement');
  const models = Array.isArray(registry?.models) ? registry.models : [];
  const modelIds = new Set(models.map((model) => model.model_id));
  const sports = new Set(models.map((model) => model.sport_family));
  if (modelIds.size !== models.length) errors.push('analysis model IDs must be unique');
  if (models.length !== EXPECTED_SPORTS.size || [...EXPECTED_SPORTS].some((sport) => !sports.has(sport))) {
    errors.push('exactly one analysis model is required for baseball, cricket, soccer, AFL and NRL');
  }
  const sourcesById = new Map(sources.map((source) => [source.source_id, source]));
  const codeHash = hashFile(resolve(root, 'src/analysis.mjs'));
  const requestSchemaHash = hashFile(assets.requestSchemaPath);
  const outputSchemaHash = hashFile(assets.outputSchemaPath);
  for (const model of models) {
    if (model.status !== ANALYSIS_TIER) errors.push(`${model.model_id}: status is not ACTIVE_ANALYSIS_ONLY`);
    if (model.forecast_state !== 'LIVE' || model.market_family !== 'winner') errors.push(`${model.model_id}: only LIVE winner analysis is authorized`);
    if (!Number.isInteger(model.max_source_age_seconds) || model.max_source_age_seconds <= 0) errors.push(`${model.model_id}: invalid source freshness limit`);
    if (!Array.isArray(model.approved_source_ids) || model.approved_source_ids.length === 0) errors.push(`${model.model_id}: no approved source IDs`);
    let usableSourceCount = 0;
    for (const sourceId of model.approved_source_ids ?? []) {
      const source = sourcesById.get(sourceId);
      if (!source) errors.push(`${model.model_id}: source ${sourceId} is not registered`);
      else {
        if (source.sport_family !== model.sport_family || source.official_status !== 'OFFICIAL') errors.push(`${model.model_id}: source ${sourceId} is not an official sport match`);
        try {
          if (source.sport_family === model.sport_family && source.official_status === 'OFFICIAL'
            && ['OPENED', 'DYNAMIC', 'PDF_OK'].includes(source.access_state)
            && parseUtc(source.next_retest_due, `${sourceId}.next_retest_due`) > now) usableSourceCount += 1;
        } catch (error) { errors.push(error.message); }
      }
    }
    if (usableSourceCount === 0) errors.push(`${model.model_id}: no currently usable approved source remains`);
    if (model.code_hash !== codeHash) errors.push(`${model.model_id}: code hash mismatch`);
    if (model.request_schema_hash !== requestSchemaHash) errors.push(`${model.model_id}: request schema hash mismatch`);
    if (model.output_schema_hash !== outputSchemaHash) errors.push(`${model.model_id}: output schema hash mismatch`);
    try {
      const activated = parseUtc(model.activated_at_utc, `${model.model_id}.activated_at_utc`);
      const expires = parseUtc(model.expires_utc, `${model.model_id}.expires_utc`);
      if (activated >= expires) {
        errors.push(`${model.model_id}: activation must precede expiry`);
      }
      if (expires <= now) errors.push(`${model.model_id}: analysis activation has expired`);
    } catch (error) { errors.push(error.message); }
  }
  return { valid: errors.length === 0, errors, active_model_count: models.filter((model) => model.status === ANALYSIS_TIER).length };
}

function validateSources(input, model, sources) {
  const errors = [];
  const asOf = parseUtc(input.as_of_utc, 'as_of_utc');
  const sourcesById = new Map(sources.map((source) => [source.source_id, source]));
  for (const observation of input.source_observations) {
    const source = sourcesById.get(observation.source_id);
    if (!source) {
      errors.push(`${observation.source_id}: source is not registered`);
      continue;
    }
    if (!model.approved_source_ids.includes(observation.source_id)) errors.push(`${observation.source_id}: source is not approved for this analysis model`);
    if (source.sport_family !== input.sport_family || source.official_status !== 'OFFICIAL') errors.push(`${observation.source_id}: source is not official for ${input.sport_family}`);
    if (!['OPENED', 'DYNAMIC', 'PDF_OK'].includes(source.access_state)) errors.push(`${observation.source_id}: source access state is not usable`);
    try {
      const registeredHost = new URL(source.direct_url_or_template).hostname.toLowerCase();
      const observedHost = new URL(observation.source_url).hostname.toLowerCase();
      if (registeredHost !== observedHost) errors.push(`${observation.source_id}: source URL host differs from registry`);
    } catch { errors.push(`${observation.source_id}: source URL is invalid`); }
    try {
      const observedAt = parseUtc(observation.observed_at_utc, `${observation.source_id}.observed_at_utc`);
      const fetchedAt = parseUtc(observation.fetched_at_utc, `${observation.source_id}.fetched_at_utc`);
      if (parseUtc(source.next_retest_due, `${observation.source_id}.next_retest_due`) <= asOf) errors.push(`${observation.source_id}: source access retest is overdue`);
      if (observedAt > fetchedAt || fetchedAt > asOf) errors.push(`${observation.source_id}: observation/fetch/as-of order is invalid`);
      if ((asOf - observedAt) / 1000 > model.max_source_age_seconds) errors.push(`${observation.source_id}: observed live state is stale`);
      if ((asOf - fetchedAt) / 1000 > model.max_source_age_seconds) errors.push(`${observation.source_id}: source snapshot is stale`);
    } catch (error) { errors.push(error.message); }
    if (!isSha256(observation.content_hash) || /^0{64}$/u.test(observation.content_hash)) errors.push(`${observation.source_id}: content hash is invalid`);
  }
  if (new Set(input.source_observations.map((item) => item.source_id)).size !== input.source_observations.length) errors.push('source observations contain duplicate source IDs');
  return errors;
}

export function analyseLive(input, { root = ROOT } = {}) {
  const assets = loadAnalysisAssets(root);
  const registryReport = validateAnalysisRegistry(assets, root);
  if (!registryReport.valid) throw new Error(`analysis registry invalid: ${registryReport.errors.join('; ')}`);
  if (!assets.validateRequest(input)) {
    const detail = (assets.validateRequest.errors ?? []).map((error) => `${error.instancePath || '/'} ${error.message}`).join('; ');
    throw new Error(`analysis request schema invalid: ${detail}`);
  }
  const model = activeModelFor(assets.registry, input.sport_family, input.competition_id);
  if (!model) throw new Error(`no ACTIVE_ANALYSIS_ONLY model for ${input.sport_family}/${input.competition_id}`);
  const sourceErrors = validateSources(input, model, assets.sources);
  if (sourceErrors.length) throw new Error(`source packet invalid: ${sourceErrors.join('; ')}`);
  const ids = assertParticipants(input);
  const analyser = ANALYSERS.get(input.sport_family);
  const lean = analyser(input.live_state, ids);
  const output = {
    schema_version: ANALYSIS_OUTPUT_VERSION,
    analysis_id: input.analysis_id,
    analysis_tier: ANALYSIS_TIER,
    model_id: model.model_id,
    model_version: model.model_version,
    sport_family: input.sport_family,
    competition_id: input.competition_id,
    market_family: 'winner',
    forecast_state: 'LIVE',
    as_of_utc: input.as_of_utc,
    numeric_forecast_authorized: false,
    lean,
    input_hash: hashObject(input),
    source_snapshot_hash: hashObject(input.source_observations),
    model_code_hash: model.code_hash,
    limitations: [
      model.limitation,
      'Deterministic live-state heuristic; not empirically calibrated and not a substitute for an ACTIVE quantitative forecast model.',
      'A source update, correction, weather interruption, injury or dismissal can change the lean immediately.',
    ],
    prohibited_claims: [...PROHIBITED_CLAIMS],
  };
  if (!assets.validateOutput(output)) {
    const detail = (assets.validateOutput.errors ?? []).map((error) => `${error.instancePath || '/'} ${error.message}`).join('; ');
    throw new Error(`analysis output schema invalid: ${detail}`);
  }
  return output;
}
