import test from 'node:test';
import assert from 'node:assert/strict';
import { parseCsv } from '../src/csv.mjs';

test('CSV parser handles UTF-8 BOM and RFC4180 escaped quotes', () => {
  assert.deepEqual(parseCsv('\uFEFFa,b\r\n"x""y",z\r\n'), [{ a: 'x"y', b: 'z' }]);
});

test('CSV parser rejects malformed quotes, trailing text and blank control rows', () => {
  assert.throws(() => parseCsv('a,b\nfoo"bar,baz\n'), /quote inside/);
  assert.throws(() => parseCsv('a,b\n"foo"bar,baz\n'), /unexpected text/);
  assert.throws(() => parseCsv('a,b\n\nfoo,bar\n'), /blank CSV row/);
});
