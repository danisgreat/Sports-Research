import assert from 'node:assert/strict';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import test from 'node:test';
import {
  analyseLive, loadAnalysisAssets, validateAnalysisRegistry,
} from '../src/analysis.mjs';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const HASH = 'a'.repeat(64);
const AS_OF = '2026-07-17T01:00:00.000Z';

function request({ sportFamily, competitionId, sourceId, sourceUrl, liveState, participants }) {
  return {
    schema_version: 'SPORTS_ANALYSIS_REQUEST_V1',
    analysis_id: `TEST-${sportFamily.replaceAll(' ', '-').toUpperCase()}-001`,
    sport_family: sportFamily,
    competition_id: competitionId,
    market_family: 'winner',
    forecast_state: 'LIVE',
    as_of_utc: AS_OF,
    participants,
    source_observations: [{
      source_id: sourceId,
      source_url: sourceUrl,
      observed_at_utc: '2026-07-17T00:59:00.000Z',
      fetched_at_utc: '2026-07-17T00:59:30.000Z',
      content_hash: HASH,
    }],
    live_state: liveState,
  };
}

const cricketRequest = () => request({
  sportFamily: 'Cricket',
  competitionId: 'ODI',
  sourceId: 'ICC_FIXTURES_RESULTS',
  sourceUrl: 'https://www.icc-cricket.com/fixtures-results',
  participants: [{ participant_id: 'IND', name: 'India' }, { participant_id: 'ENG', name: 'England' }],
  liveState: {
    first_batting_participant_id: 'IND',
    chasing_participant_id: 'ENG',
    innings_number: 2,
    target_basis: 'STANDARD',
    target_runs: 234,
    current_runs: 54,
    wickets_lost: 3,
    balls_bowled: 67,
    scheduled_balls: 300,
    max_wickets: 10,
    first_innings_runs: 233,
    first_innings_balls: 264,
    game_status: 'IN_PROGRESS',
  },
});

test('analysis registry has exactly five honest ACTIVE_ANALYSIS_ONLY models', () => {
  const report = validateAnalysisRegistry(loadAnalysisAssets(ROOT), ROOT);
  assert.deepEqual(report.errors, []);
  assert.equal(report.active_model_count, 5);
});

test('analysis registry expires models and overdue source access rather than staying active forever', () => {
  const assets = loadAnalysisAssets(ROOT);
  const report = validateAnalysisRegistry(assets, ROOT, { now: Date.parse('2027-02-01T00:00:00.000Z') });
  assert.equal(report.valid, false);
  assert.match(report.errors.join('; '), /expired|no currently usable approved source/);
});

test('cricket chase model reproduces the documented England live lean without a probability', () => {
  const output = analyseLive(cricketRequest(), { root: ROOT });
  assert.equal(output.model_id, 'ANALYSIS_CRICKET_CHASE_STATE_V1');
  assert.equal(output.lean.participant_id, 'ENG');
  assert.equal(output.lean.strength, 'SLIGHT');
  assert.equal(output.numeric_forecast_authorized, false);
  assert.equal(Object.hasOwn(output, 'probability'), false);
});

test('baseball model uses inning and score state', () => {
  const output = analyseLive(request({
    sportFamily: 'Baseball', competitionId: 'MLB', sourceId: 'MLB_SCHEDULE', sourceUrl: 'https://www.mlb.com/schedule',
    participants: [{ participant_id: 'AWAY', name: 'Away' }, { participant_id: 'HOME', name: 'Home' }],
    liveState: {
      away_participant_id: 'AWAY', home_participant_id: 'HOME', away_runs: 2, home_runs: 5,
      inning: 8, half: 'BOTTOM', outs: 1, scheduled_innings: 9, bases_occupied: ['FIRST'], game_status: 'IN_PROGRESS',
    },
  }), { root: ROOT });
  assert.equal(output.lean.participant_id, 'HOME');
  assert.equal(output.lean.strength, 'STRONG');
});

test('soccer model uses score, clock and red-card state', () => {
  const output = analyseLive(request({
    sportFamily: 'Soccer', competitionId: 'EPL', sourceId: 'PREMIER_LEAGUE_MATCHES', sourceUrl: 'https://www.premierleague.com/en/matches/premier-league',
    participants: [{ participant_id: 'HOME', name: 'Home' }, { participant_id: 'AWAY', name: 'Away' }],
    liveState: {
      home_participant_id: 'HOME', away_participant_id: 'AWAY', home_goals: 2, away_goals: 1,
      elapsed_minutes: 82, regulation_minutes: 90, home_red_cards: 0, away_red_cards: 0,
      period: 'SECOND_HALF', game_status: 'IN_PROGRESS',
    },
  }), { root: ROOT });
  assert.equal(output.lean.participant_id, 'HOME');
  assert.equal(output.lean.strength, 'STRONG');
});

test('AFL and NRL models use sport-specific margin/time scales', () => {
  const afl = analyseLive(request({
    sportFamily: 'Australian football', competitionId: 'AFL', sourceId: 'AFL_FIXTURE', sourceUrl: 'https://www.afl.com.au/fixture',
    participants: [{ participant_id: 'HOME', name: 'Home' }, { participant_id: 'AWAY', name: 'Away' }],
    liveState: {
      home_participant_id: 'HOME', away_participant_id: 'AWAY', home_points: 80, away_points: 60,
      period_number: 4, seconds_remaining_in_period: 300, nominal_period_seconds: 1200, game_status: 'IN_PROGRESS',
    },
  }), { root: ROOT });
  const nrl = analyseLive(request({
    sportFamily: 'Rugby league', competitionId: 'NRL', sourceId: 'NRL_DRAW', sourceUrl: 'https://www.nrl.com/draw/',
    participants: [{ participant_id: 'HOME', name: 'Home' }, { participant_id: 'AWAY', name: 'Away' }],
    liveState: {
      home_participant_id: 'HOME', away_participant_id: 'AWAY', home_points: 10, away_points: 20,
      elapsed_minutes: 70, regulation_minutes: 80, period: 'SECOND_HALF', game_status: 'IN_PROGRESS',
    },
  }), { root: ROOT });
  assert.equal(afl.lean.participant_id, 'HOME');
  assert.equal(afl.lean.strength, 'STRONG');
  assert.equal(nrl.lean.participant_id, 'AWAY');
  assert.equal(nrl.lean.strength, 'STRONG');
});

test('tied neutral state returns TOSSUP rather than inventing a side', () => {
  const output = analyseLive(request({
    sportFamily: 'Soccer', competitionId: 'FIFA', sourceId: 'FIFA_MATCH_CENTRE', sourceUrl: 'https://www.fifa.com/en/match-centre',
    participants: [{ participant_id: 'HOME', name: 'Home' }, { participant_id: 'AWAY', name: 'Away' }],
    liveState: {
      home_participant_id: 'HOME', away_participant_id: 'AWAY', home_goals: 1, away_goals: 1,
      elapsed_minutes: 60, regulation_minutes: 90, home_red_cards: 0, away_red_cards: 0,
      period: 'SECOND_HALF', game_status: 'IN_PROGRESS',
    },
  }), { root: ROOT });
  assert.equal(output.lean.classification, 'TOSSUP');
  assert.equal(output.lean.participant_id, null);
  assert.equal(output.lean.strength, 'NONE');
});

test('stale, wrong-host and unapproved sources fail closed', () => {
  const stale = cricketRequest();
  stale.source_observations[0].observed_at_utc = '2026-07-17T00:49:30.000Z';
  stale.source_observations[0].fetched_at_utc = '2026-07-17T00:50:00.000Z';
  assert.throws(() => analyseLive(stale, { root: ROOT }), /observed live state is stale|source snapshot is stale/);

  const wrongHost = cricketRequest();
  wrongHost.source_observations[0].source_url = 'https://example.com/live';
  assert.throws(() => analyseLive(wrongHost, { root: ROOT }), /host differs from registry/);

  const unapproved = cricketRequest();
  unapproved.source_observations[0].source_id = 'MLB_SCHEDULE';
  unapproved.source_observations[0].source_url = 'https://www.mlb.com/schedule';
  assert.throws(() => analyseLive(unapproved, { root: ROOT }), /not approved|not official/);

  const zeroHash = cricketRequest();
  zeroHash.source_observations[0].content_hash = '0'.repeat(64);
  assert.throws(() => analyseLive(zeroHash, { root: ROOT }), /content hash is invalid/);
});

test('closed request schemas reject smuggled model or price fields', () => {
  const input = cricketRequest();
  input.probability = 0.7;
  assert.throws(() => analyseLive(input, { root: ROOT }), /additional properties/);
});

test('unsupported competitions do not inherit an analysis model', () => {
  const input = cricketRequest();
  input.competition_id = 'TEST_CRICKET';
  assert.throws(() => analyseLive(input, { root: ROOT }), /no ACTIVE_ANALYSIS_ONLY model/);
});

test('cricket revised targets and inconsistent standard targets fail closed', () => {
  const revised = cricketRequest();
  revised.live_state.target_basis = 'REVISED_OFFICIAL';
  assert.throws(() => analyseLive(revised, { root: ROOT }), /target_basis/);

  const inconsistent = cricketRequest();
  inconsistent.live_state.target_runs = 240;
  assert.throws(() => analyseLive(inconsistent, { root: ROOT }), /must equal first-innings runs plus one/);
});

test('soccer extra time and impossible AFL period clocks remain out of scope', () => {
  const soccer = request({
    sportFamily: 'Soccer', competitionId: 'FIFA', sourceId: 'FIFA_MATCH_CENTRE', sourceUrl: 'https://www.fifa.com/en/match-centre',
    participants: [{ participant_id: 'HOME', name: 'Home' }, { participant_id: 'AWAY', name: 'Away' }],
    liveState: {
      home_participant_id: 'HOME', away_participant_id: 'AWAY', home_goals: 1, away_goals: 1,
      elapsed_minutes: 100, regulation_minutes: 90, home_red_cards: 0, away_red_cards: 0,
      period: 'SECOND_HALF', game_status: 'IN_PROGRESS',
    },
  });
  assert.throws(() => analyseLive(soccer, { root: ROOT }), /excludes extra time/);

  const afl = request({
    sportFamily: 'Australian football', competitionId: 'AFL', sourceId: 'AFL_FIXTURE', sourceUrl: 'https://www.afl.com.au/fixture',
    participants: [{ participant_id: 'HOME', name: 'Home' }, { participant_id: 'AWAY', name: 'Away' }],
    liveState: {
      home_participant_id: 'HOME', away_participant_id: 'AWAY', home_points: 20, away_points: 10,
      period_number: 1, seconds_remaining_in_period: 1300, nominal_period_seconds: 1200, game_status: 'IN_PROGRESS',
    },
  });
  assert.throws(() => analyseLive(afl, { root: ROOT }), /exceeds the supplied nominal period/);
});
