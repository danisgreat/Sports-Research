import test from 'node:test';
import assert from 'node:assert/strict';
import { resolve } from 'node:path';

import Ajv2020 from 'ajv/dist/2020.js';

import { readJson } from '../src/canonical.mjs';
import { makeValidIssueFixture } from './support/valid_issue_fixture.mjs';

const ROOT = resolve(import.meta.dirname, '..');

function compileDecisionPacketSchema() {
  const schema = readJson(resolve(ROOT, 'schema/decision_packet.schema.json'));
  return new Ajv2020({ allErrors: true, strict: true, allowUnionTypes: true, validateFormats: false }).compile(schema);
}

test('decision packet JSON Schema compiles and accepts the genuine ISSUE fixture', () => {
  const validate = compileDecisionPacketSchema();
  const { packet } = makeValidIssueFixture();
  assert.equal(validate(packet), true, JSON.stringify(validate.errors, null, 2));
});

test('decision packet JSON Schema rejects unknown root fields and missing ISSUE evidence', () => {
  const validate = compileDecisionPacketSchema();
  const { packet } = makeValidIssueFixture();
  assert.equal(validate({ ...packet, unregistered_root_field: true }), false);
  assert.ok(validate.errors.some((error) => error.keyword === 'additionalProperties'));

  const withoutPrediction = { ...packet, prediction: null };
  assert.equal(validate(withoutPrediction), false);
  assert.ok(validate.errors.some((error) => error.instancePath === '/prediction'));
});
