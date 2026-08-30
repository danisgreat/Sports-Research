import { createHash, randomUUID } from 'node:crypto';
import { readFileSync, renameSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { mkdirSync } from 'node:fs';

export const CANONICAL_SERIALIZATION_VERSION = 'SPORTS_CANONICAL_JSON_V1';
export const SHA256_PATTERN = /^[a-f0-9]{64}$/;
export const UTC_PATTERN = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{3})?Z$/;

function assertUnicodeScalars(value, path) {
  for (let index = 0; index < value.length; index += 1) {
    const code = value.charCodeAt(index);
    if (code >= 0xD800 && code <= 0xDBFF) {
      const next = value.charCodeAt(index + 1);
      if (!(next >= 0xDC00 && next <= 0xDFFF)) throw new TypeError(`${path}: lone high surrogate is prohibited`);
      index += 1;
    } else if (code >= 0xDC00 && code <= 0xDFFF) throw new TypeError(`${path}: lone low surrogate is prohibited`);
  }
}

export function compareCanonicalStrings(left, right) {
  assertUnicodeScalars(left, 'canonical key');
  assertUnicodeScalars(right, 'canonical key');
  return Buffer.compare(Buffer.from(left.normalize('NFC'), 'utf8'), Buffer.from(right.normalize('NFC'), 'utf8'));
}

function serializeCanonical(value, path = '$') {
  if (value === null || typeof value === 'boolean') return JSON.stringify(value);
  if (typeof value === 'string') {
    assertUnicodeScalars(value, path);
    return JSON.stringify(value.normalize('NFC'));
  }
  if (typeof value === 'number') {
    if (!Number.isFinite(value)) throw new TypeError(`${path}: non-finite numbers are not canonical JSON`);
    return JSON.stringify(Object.is(value, -0) ? 0 : value);
  }
  if (Array.isArray(value)) return `[${value.map((item, index) => serializeCanonical(item, `${path}[${index}]`)).join(',')}]`;
  if (typeof value === 'object') {
    const keys = Object.keys(value).map((original) => ({ original, normalized: original.normalize('NFC') }));
    keys.sort((left, right) => compareCanonicalStrings(left.normalized, right.normalized));
    const seen = new Set();
    const members = [];
    for (const { original, normalized } of keys) {
      assertUnicodeScalars(original, `${path} key`);
      if (seen.has(normalized)) throw new TypeError(`${path}: Unicode-normalized key collision for ${normalized}`);
      seen.add(normalized);
      if (value[original] === undefined) throw new TypeError(`${path}.${original}: undefined is not canonical JSON`);
      members.push(`${JSON.stringify(normalized)}:${serializeCanonical(value[original], `${path}.${original}`)}`);
    }
    return `{${members.join(',')}}`;
  }
  throw new TypeError(`${path}: unsupported canonical JSON type ${typeof value}`);
}

export function canonicalStringify(value) {
  return serializeCanonical(value);
}

export function sha256Text(text) {
  return createHash('sha256').update(text, 'utf8').digest('hex');
}

export function hashObject(value) {
  return sha256Text(canonicalStringify(value));
}

export function hashFile(path) {
  return createHash('sha256').update(readFileSync(path)).digest('hex');
}

export function parseUtc(value, field = 'timestamp') {
  if (typeof value !== 'string' || !UTC_PATTERN.test(value)) {
    throw new TypeError(`${field}: expected an ISO-8601 UTC timestamp ending in Z`);
  }
  const milliseconds = Date.parse(value);
  if (!Number.isFinite(milliseconds)) throw new TypeError(`${field}: invalid timestamp`);
  const canonical = new Date(milliseconds).toISOString();
  const expected = value.includes('.') ? value : value.replace(/Z$/, '.000Z');
  if (canonical !== expected) throw new TypeError(`${field}: non-existent or non-canonical UTC timestamp`);
  return milliseconds;
}

export function utcNow() {
  return new Date().toISOString();
}

export function newId(prefix) {
  return `${prefix}-${randomUUID()}`;
}

export function parseJsonStrict(text, source = 'JSON') {
  let index = 0;
  const fail = (message) => { throw new SyntaxError(`${source} at offset ${index}: ${message}`); };
  const whitespace = () => { while (/\s/u.test(text[index] ?? '')) index += 1; };
  const parseString = () => {
    if (text[index] !== '"') fail('expected string');
    const start = index;
    index += 1;
    while (index < text.length) {
      const character = text[index];
      if (character === '"') {
        index += 1;
        try { return JSON.parse(text.slice(start, index)); } catch { fail('invalid string escape'); }
      }
      if (character === '\\') index += 2;
      else {
        if (character.charCodeAt(0) < 0x20) fail('unescaped control character');
        index += 1;
      }
    }
    fail('unterminated string');
  };
  const parseValue = () => {
    whitespace();
    const character = text[index];
    if (character === '"') return parseString();
    if (character === '{') {
      index += 1;
      whitespace();
      const object = Object.create(null);
      const keys = new Set();
      if (text[index] === '}') { index += 1; return object; }
      while (true) {
        whitespace();
        const key = parseString();
        const normalizedKey = key.normalize('NFC');
        if (keys.has(normalizedKey)) fail(`duplicate or NFC-colliding key ${normalizedKey}`);
        keys.add(normalizedKey);
        whitespace();
        if (text[index] !== ':') fail('expected colon');
        index += 1;
        Object.defineProperty(object, normalizedKey, { value: parseValue(), enumerable: true, configurable: true, writable: true });
        whitespace();
        if (text[index] === '}') { index += 1; return object; }
        if (text[index] !== ',') fail('expected comma or object end');
        index += 1;
      }
    }
    if (character === '[') {
      index += 1;
      whitespace();
      const array = [];
      if (text[index] === ']') { index += 1; return array; }
      while (true) {
        array.push(parseValue());
        whitespace();
        if (text[index] === ']') { index += 1; return array; }
        if (text[index] !== ',') fail('expected comma or array end');
        index += 1;
      }
    }
    for (const [token, value] of [['true', true], ['false', false], ['null', null]]) {
      if (text.startsWith(token, index)) { index += token.length; return value; }
    }
    const match = text.slice(index).match(/^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/);
    if (match) {
      index += match[0].length;
      const number = Number(match[0]);
      if (!Number.isFinite(number)) fail('number is not finite');
      return number;
    }
    fail('invalid JSON value');
  };
  const value = parseValue();
  whitespace();
  if (index !== text.length) fail('trailing content');
  return value;
}

export function readJson(path) {
  const text = readFileSync(path, 'utf8').replace(/^\uFEFF/, '');
  return parseJsonStrict(text, path);
}

export function writeJsonAtomic(path, value) {
  const absolute = resolve(path);
  mkdirSync(dirname(absolute), { recursive: true });
  const temporary = `${absolute}.tmp-${process.pid}-${Date.now()}`;
  writeFileSync(temporary, `${JSON.stringify(value, null, 2)}\n`, { encoding: 'utf8', flag: 'wx' });
  renameSync(temporary, absolute);
}

export function packetHashMaterial(packet) {
  const copy = structuredClone(packet);
  if (copy?.decision_snapshot) delete copy.decision_snapshot.snapshot_hash;
  delete copy.packet_hash;
  return {
    canonical_serialization_version: CANONICAL_SERIALIZATION_VERSION,
    packet: copy,
  };
}

export function computeSnapshotHash(packet) {
  return hashObject(packetHashMaterial(packet));
}

export function isSha256(value) {
  return typeof value === 'string' && SHA256_PATTERN.test(value);
}
