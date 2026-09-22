import test from 'node:test';
import assert from 'node:assert/strict';
import { canonicalStringify, hashObject, parseJsonStrict, parseUtc } from '../src/canonical.mjs';

test('canonical JSON is stable across input key order', () => {
  assert.equal(canonicalStringify({ z: 1, a: { d: 2, c: 3 } }), canonicalStringify({ a: { c: 3, d: 2 }, z: 1 }));
  assert.equal(hashObject({ b: 2, a: 1 }), hashObject({ a: 1, b: 2 }));
});

test('canonical JSON rejects non-finite numbers and normalized-key collisions', () => {
  assert.throws(() => canonicalStringify({ value: Number.NaN }), /non-finite/);
  assert.throws(() => canonicalStringify({ '\u00e9': 1, 'e\u0301': 2 }), /key collision/);
});

test('UTC parser rejects offsets and local timestamps', () => {
  assert.equal(parseUtc('2026-07-16T00:00:00Z'), Date.parse('2026-07-16T00:00:00Z'));
  assert.throws(() => parseUtc('2026-07-16T10:00:00+10:00'), /ending in Z/);
  assert.throws(() => parseUtc('2026-07-16 00:00:00'), /ending in Z/);
  assert.throws(() => parseUtc('2026-02-30T00:00:00Z'), /non-existent/);
  assert.throws(() => parseUtc('2026-07-16T24:00:00Z'), /non-existent/);
});

test('canonical ordering is UTF-8 based even for integer-like keys', () => {
  assert.equal(canonicalStringify({ 2: 'two', 10: 'ten', a: 'a' }), '{"10":"ten","2":"two","a":"a"}');
});

test('strict JSON rejects duplicate/colliding keys and safely retains __proto__', () => {
  assert.throws(() => parseJsonStrict('{"a":1,"a":2}'), /duplicate/);
  assert.throws(() => parseJsonStrict('{"é":1,"e\\u0301":2}'), /colliding/);
  const parsed = parseJsonStrict('{"__proto__":{"polluted":true}}');
  assert.equal(Object.hasOwn(parsed, '__proto__'), true);
  assert.equal({}.polluted, undefined);
});

test('canonical serializer rejects lone UTF-16 surrogates', () => {
  assert.throws(() => canonicalStringify({ value: '\uD800' }), /lone high surrogate/);
});
