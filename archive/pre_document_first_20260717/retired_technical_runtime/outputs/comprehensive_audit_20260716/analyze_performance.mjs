import fs from "node:fs";
import path from "node:path";

const ROOT = String.raw`C:\Users\danie\Desktop\Sports Research`;
const OUT = path.join(ROOT, "outputs", "comprehensive_audit_20260716");
const CSV_PATH = path.join(ROOT, "SPORTS_CALIBRATION_LEDGER_v2.csv");
const INSPECT_PATH = path.join(ROOT, "outputs", "settlement_20260713", "SPORTS_CALIBRATION_LEDGER_v2_settled.xlsx.inspect.ndjson");
const V2_PATH = path.join(ROOT, "PREDICTION_RESULTS_LOG_v2.md");
const V3_PATH = path.join(ROOT, "PREDICTION_RESULTS_LOG_v3.md");

function clean(value) {
  if (value === null || value === undefined) return "";
  if (typeof value === "boolean") return value ? "TRUE" : "FALSE";
  return String(value).trim();
}

function normText(value) {
  return clean(value)
    .toLowerCase()
    .replace(/[–—]/g, "-")
    .replace(/½/g, ".5")
    .replace(/[^a-z0-9+.-]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function truth(value) {
  const v = clean(value).toLowerCase();
  if (["true", "1", "yes", "y"].includes(v)) return true;
  if (["false", "0", "no", "n", ""].includes(v)) return false;
  return null;
}

function intOrNull(value) {
  const n = Number.parseInt(clean(value), 10);
  return Number.isFinite(n) ? n : null;
}

function numOrNull(value) {
  if (clean(value) === "") return null;
  const n = Number(clean(value));
  return Number.isFinite(n) ? n : null;
}

function parseCSV(text) {
  text = text.replace(/^\uFEFF/, "");
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"') {
        if (text[i + 1] === '"') {
          field += '"';
          i++;
        } else {
          quoted = false;
        }
      } else {
        field += ch;
      }
    } else if (ch === '"') {
      quoted = true;
    } else if (ch === ",") {
      row.push(field);
      field = "";
    } else if (ch === "\n") {
      row.push(field.replace(/\r$/, ""));
      rows.push(row);
      row = [];
      field = "";
    } else {
      field += ch;
    }
  }
  if (field !== "" || row.length) {
    row.push(field.replace(/\r$/, ""));
    rows.push(row);
  }
  return rows;
}

function readLedgerCSV(file) {
  const matrix = parseCSV(fs.readFileSync(file, "utf8"));
  const headers = matrix[0].map((x) => clean(x).replace(/^\uFEFF/, ""));
  return matrix.slice(1).filter((r) => r.some((x) => clean(x) !== "")).map((values, i) => {
    const row = {};
    headers.forEach((h, j) => row[h] = clean(values[j]));
    row._source = path.basename(file);
    row._row = i + 2;
    return row;
  });
}

function readInspect(file) {
  const lines = fs.readFileSync(file, "utf8").split(/\r?\n/);
  const tableLine = lines.find((line) => line.startsWith('{"kind":"table"'));
  if (!tableLine) throw new Error("No table row found in inspect NDJSON");
  const table = JSON.parse(tableLine);
  const headers = table.values[0].map((x) => clean(x).replace(/^\uFEFF/, "").replace(/^ï»¿/, ""));
  const rows = table.values.slice(1).map((values, i) => {
    const row = {};
    headers.forEach((h, j) => row[h] = clean(values[j]));
    row._source = "SPORTS_CALIBRATION_LEDGER_v2_settled.xlsx";
    row._row = i + 2;
    return row;
  });
  return { rows, table };
}

function canonicalSport(sport) {
  const s = normText(sport);
  if (s.includes("afl")) return "AFL";
  if (s.includes("wnba")) return "WNBA";
  if (s.includes("nba") || s.includes("basketball") || s.includes("nbl") || s.includes("euroleague")) return "Basketball (other)";
  if (s.includes("mlb")) return "MLB";
  if (s.includes("kbo")) return "KBO";
  if (s.includes("npb")) return "NPB";
  if (s.includes("baseball")) return "Baseball (other)";
  if (["cricket", "t20", "odi", "mlc"].some((x) => s.includes(x))) return "Cricket";
  if (["soccer", "football", "fifa"].some((x) => s.includes(x))) return "Soccer";
  if (s.includes("nrl") || s.includes("rugby league")) return "Rugby league";
  if (s.includes("nhl") || s.includes("hockey")) return "Ice hockey";
  if (s.includes("tennis")) return "Tennis";
  return clean(sport) || "UNKNOWN";
}

function marketFamily(row) {
  const txt = normText([row.market_group, row.option, row.settlement_convention].join(" "));
  if (["shot on target", "sot", "player", "rebound", "assist", "runs scored by", "wickets by"].some((x) => txt.includes(x))) return "Player prop";
  if (["powerplay", "first six", "1h", "first half", "q1", "quarter", "innings"].some((x) => txt.includes(x)) && /\b(over|under)\b/.test(txt)) return "Phase/innings total";
  if (txt.includes("corners")) return "Corners";
  if (["moneyline", " ml ", "winner", "to win", "advance", "double chance", "or draw", "avoid loss"].some((x) => ` ${txt} `.includes(x))) return "Winner/non-loss";
  if (/(?:^|\s)[+-]\d/.test(txt) || ["handicap", "run line", "spread", "cushion"].some((x) => txt.includes(x))) return "Handicap/spread";
  if (/\b(over|under)\b/.test(txt) || txt.includes("total")) return "Full-game/team total";
  return "Other";
}

function isTemplate(row) {
  return row.card_id === "TEMPLATE" || row.date === "YYYY-MM-DD";
}

function status(row) {
  const v = clean(row.win_loss_push).toUpperCase();
  const aliases = { WIN: "W", LOSS: "L", PUSH: "P", UNGRADED: "VOID", "NO GRADE": "VOID" };
  return aliases[v] || v || "BLANK";
}

function naturalKey(row) {
  return JSON.stringify([clean(row.card_id), clean(row.rank), normText(row.option)]);
}

function groupBy(rows, fn) {
  const map = new Map();
  for (const row of rows) {
    const key = fn(row);
    if (!map.has(key)) map.set(key, []);
    map.get(key).push(row);
  }
  return map;
}

function countBy(items, fn = (x) => x) {
  const out = {};
  for (const item of items) {
    const key = String(fn(item));
    out[key] = (out[key] || 0) + 1;
  }
  return out;
}

function metricBlock(rows) {
  const statuses = countBy(rows, status);
  const W = statuses.W || 0;
  const L = statuses.L || 0;
  const P = statuses.P || 0;
  const decided = W + L;
  const known = new Set(["W", "L", "P", "VOID", "BLANK"]);
  return {
    rows: rows.length,
    W,
    L,
    P,
    VOID: statuses.VOID || 0,
    BLANK: statuses.BLANK || 0,
    other_statuses: Object.fromEntries(Object.entries(statuses).filter(([k]) => !known.has(k))),
    accuracy_ex_push: decided ? W / decided : null,
  };
}

function calibrationBlock(rows) {
  const valid = rows.map((r) => [numOrNull(r.stated_probability), status(r)]).filter(([p, s]) => p !== null && p >= 0 && p <= 1 && ["W", "L"].includes(s)).map(([p, s]) => [p, s === "W" ? 1 : 0]);
  if (!valid.length) return { n: 0 };
  const eps = 1e-15;
  const mean = (values) => values.reduce((a, b) => a + b, 0) / values.length;
  const meanP = mean(valid.map(([p]) => p));
  const observed = mean(valid.map(([, y]) => y));
  const brier = mean(valid.map(([p, y]) => (p - y) ** 2));
  const logLoss = -mean(valid.map(([p, y]) => y * Math.log(Math.max(eps, p)) + (1 - y) * Math.log(Math.max(eps, 1 - p))));
  return { n: valid.length, mean_probability: meanP, observed_rate: observed, bias_p_minus_observed: meanP - observed, brier, log_loss: logLoss };
}

function summarizeGroup(rows, fn) {
  return [...groupBy(rows, fn).entries()].sort((a, b) => String(a[0]).localeCompare(String(b[0]))).map(([group, values]) => {
    const cal = calibrationBlock(values);
    return { group, ...metricBlock(values), ...Object.fromEntries(Object.entries(cal).map(([k, v]) => [`cal_${k}`, v])) };
  });
}

const STOP_TOKENS = new Set(["over", "under", "combined", "total", "full", "game", "points", "runs", "goals", "point", "run", "goal", "the", "at", "line", "regulation", "market", "1st", "first", "20", "overs"]);

function directionAndSubject(row) {
  const option = normText(row.option);
  const matches = [...option.matchAll(/\b(over|under)\b/g)].map((m) => m[1]);
  if (!matches.length) return [null, new Set()];
  const tokens = new Set((option.match(/[a-z]+|\d+(?:\.\d+)?/g) || []).filter((t) => !STOP_TOKENS.has(t) && !/^\d+(?:\.\d+)?$/.test(t)));
  return [matches.at(-1), tokens];
}

function normalizedLine(row) {
  for (const raw of [normText(row.line_or_threshold), normText(row.option)]) {
    const nums = [...raw.matchAll(/[+-]?\d+(?:\.\d+)?/g)].map((m) => Number(m[0])).filter(Number.isFinite);
    if (nums.length) return Math.abs(nums.at(-1)).toFixed(4);
  }
  return normText(row.line_or_threshold);
}

function signedSpread(row) {
  for (const raw of [normText(row.option), normText(row.line_or_threshold)]) {
    const matches = [...raw.matchAll(/(^|\s)([+-])\s*(\d+(?:\.\d+)?)(?=\s|$)/g)];
    if (matches.length) {
      const match = matches.at(-1);
      return { sign: match[2], value: Number(match[3]) };
    }
  }
  return null;
}

function complementInfo(a, b) {
  const spreadA = signedSpread(a), spreadB = signedSpread(b);
  if (spreadA && spreadB && spreadA.sign !== spreadB.sign && Math.abs(spreadA.value - spreadB.value) < 1e-9) {
    return { similarity: 1, type: "spread" };
  }
  const [da, ta] = directionAndSubject(a);
  const [db, tb] = directionAndSubject(b);
  if (!((da === "over" && db === "under") || (da === "under" && db === "over"))) return { similarity: 0, type: null };
  if (normalizedLine(a) !== normalizedLine(b)) return { similarity: 0, type: null };
  const union = new Set([...ta, ...tb]);
  if (!union.size) return { similarity: 1, type: "over_under" };
  const intersection = [...ta].filter((x) => tb.has(x));
  return { similarity: intersection.length / union.size, type: "over_under" };
}

function findComplements(rows) {
  const cards = groupBy(rows, (r) => r.card_id);
  const pairs = [];
  const cardStats = [];
  for (const [cardId, cardRows] of cards) {
    const candidates = [];
    for (let i = 0; i < cardRows.length; i++) {
      for (let j = i + 1; j < cardRows.length; j++) {
        const { similarity, type } = complementInfo(cardRows[i], cardRows[j]);
        if (similarity >= 0.5) candidates.push({ similarity, type, i, j });
      }
    }
    candidates.sort((a, b) => b.similarity - a.similarity);
    const used = new Set();
    const selected = [];
    for (const c of candidates) {
      if (used.has(c.i) || used.has(c.j)) continue;
      used.add(c.i); used.add(c.j); selected.push(c);
    }
    for (const { similarity, type, i, j } of selected) {
      const a = cardRows[i], b = cardRows[j];
      const pa = numOrNull(a.stated_probability), pb = numOrNull(b.stated_probability);
      const sa = status(a), sb = status(b);
      const set = new Set([sa, sb]);
      const consistent = (set.size === 2 && set.has("W") && set.has("L")) || (sa === "P" && sb === "P") || (sa === "VOID" && sb === "VOID");
      pairs.push({
        card_id: cardId, date: a.date, sport: a.sport, match: a.match,
        rank_a: a.rank, option_a: a.option, status_a: sa, probability_a: pa, row_a: a._row,
        rank_b: b.rank, option_b: b.option, status_b: sb, probability_b: pb, row_b: b._row,
        complement_type: type, line: normalizedLine(a), subject_similarity: similarity,
        probability_sum: pa !== null && pb !== null ? pa + pb : null,
        outcome_consistent: consistent,
      });
    }
    cardStats.push({ card_id: cardId, rows: cardRows.length, complement_pairs: selected.length, rows_in_pairs: selected.length * 2, fully_complementary_four_pick: cardRows.length === 4 && selected.length === 2 });
  }
  return { pairs, cardStats };
}

function parseMarkdown(pathname) {
  const lines = fs.readFileSync(pathname, "utf8").replace(/^\uFEFF/, "").split(/\r?\n/);
  const tableRows = [];
  for (let i = 0; i < lines.length; i++) {
    if (!/^\|\s*20\d{2}-\d{2}-\d{2}\s*\|/.test(lines[i])) continue;
    const cells = lines[i].trim().replace(/^\||\|$/g, "").split("|").map((x) => x.trim());
    tableRows.push({ file: path.basename(pathname), line: i + 1, cells, raw: lines[i] });
  }
  const keyed = groupBy(tableRows.filter((r) => r.cells.length >= 3), (r) => JSON.stringify([normText(r.cells[0]), normText(r.cells[1]), normText(r.cells[2])]));
  const duplicates = [...keyed.entries()].filter(([, v]) => v.length > 1).map(([key, v]) => ({ key: JSON.parse(key), lines: v.map((x) => x.line) }));
  const parsed = tableRows.map((r) => {
    const c = r.cells;
    const outcome = c[6] || "";
    let wl = null;
    for (const regex of [/(?:listed|card|selected(?: card)?|main card|settled|top four)[^\d]{0,30}(\d+)\s*-\s*(\d+)/i, /\b(\d+)\s*-\s*(\d+)\s*(?:card|listed|with|;|,|$)/i]) {
      const m = outcome.match(regex);
      if (m) { wl = [Number(m[1]), Number(m[2])]; break; }
    }
    return { file: r.file, line: r.line, date: c[0] || "", sport: c[1] || "", match: c[2] || "", market_group: c[3] || "", ranked_picks: c[4] || "", result: c[5] || "", card_outcome: outcome, parsed_wins: wl?.[0] ?? null, parsed_losses: wl?.[1] ?? null, cell_count: c.length };
  });
  return { tableRows, parsed, duplicates, outcome_counts: countBy(parsed.filter((r) => r.parsed_wins !== null), (r) => `${r.parsed_wins}-${r.parsed_losses}`) };
}

function csvCell(value) {
  if (value === null || value === undefined) return "";
  const text = typeof value === "object" ? JSON.stringify(value) : String(value);
  return /[",\r\n]/.test(text) ? `"${text.replace(/"/g, '""')}"` : text;
}

function writeCSV(file, rows) {
  if (!rows.length) { fs.writeFileSync(file, "", "utf8"); return; }
  const fields = [];
  for (const row of rows) for (const key of Object.keys(row)) if (!fields.includes(key)) fields.push(key);
  const text = "\uFEFF" + [fields.map(csvCell).join(","), ...rows.map((r) => fields.map((f) => csvCell(r[f])).join(","))].join("\r\n") + "\r\n";
  fs.writeFileSync(file, text, "utf8");
}

function fileMeta(file) {
  const stat = fs.statSync(file);
  return { path: file, modified: stat.mtime.toISOString(), bytes: stat.size };
}

fs.mkdirSync(OUT, { recursive: true });
const csvAll = readLedgerCSV(CSV_PATH);
const { rows: xlsxAll, table: xlsxTable } = readInspect(INSPECT_PATH);
const csvRows = csvAll.filter((r) => !isTemplate(r));
const xlsxRows = xlsxAll.filter((r) => !isTemplate(r));
const headers = Object.keys(csvAll[0]).filter((k) => !k.startsWith("_"));

const csvKeyed = groupBy(csvAll, naturalKey);
const xlsxKeyed = groupBy(xlsxAll, naturalKey);
const diffRows = [];
const keys = new Set([...csvKeyed.keys(), ...xlsxKeyed.keys()]);
for (const key of [...keys].sort()) {
  const c = csvKeyed.get(key) || [], x = xlsxKeyed.get(key) || [];
  const [cardId, rank] = JSON.parse(key);
  if (!c.length) x.forEach((r) => diffRows.push({ kind: "xlsx_only", card_id: cardId, rank, option: r.option, csv_row: "", xlsx_row: r._row }));
  else if (!x.length) c.forEach((r) => diffRows.push({ kind: "csv_only", card_id: cardId, rank, option: r.option, csv_row: r._row, xlsx_row: "" }));
  else {
    const mismatches = headers.filter((h) => clean(c[0][h]) !== clean(x[0][h]));
    if (mismatches.length) diffRows.push({ kind: "field_mismatch", card_id: cardId, rank, option: c[0].option, csv_row: c[0]._row, xlsx_row: x[0]._row, fields: mismatches.join(";") });
  }
}

const exactGroups = groupBy(csvAll, (r) => JSON.stringify(headers.map((h) => clean(r[h]))));
const exactDupGroups = [...exactGroups.values()].filter((g) => g.length > 1);
const duplicateNaturalKeys = [...csvKeyed.entries()].filter(([, g]) => g.length > 1).map(([key, g]) => {
  const [cardId, rank, option] = JSON.parse(key);
  return { card_id: cardId, rank, normalized_option: option, count: g.length, rows: g.map((r) => r._row).join(";"), statuses: g.map(status).join(";") };
});

const crossEvent = groupBy(csvRows, (r) => JSON.stringify([r.date, canonicalSport(r.sport), normText(r.match), normText(r.option), normalizedLine(r)]));
const crossCardRepeats = [];
for (const [key, group] of crossEvent) {
  const ids = [...new Set(group.map((r) => r.card_id))];
  if (ids.length > 1) {
    const [date, sport, match, option, line] = JSON.parse(key);
    crossCardRepeats.push({ date, sport, match, option, line, count: group.length, card_ids: ids.sort().join(";"), rows: group.map((r) => r._row).join(";"), statuses: group.map(status).join(";") });
  }
}

const cards = groupBy(csvRows, (r) => r.card_id);
const issueRows = [];
for (const [cardId, group] of cards) {
  const ranks = group.map((r) => intOrNull(r.rank));
  const numeric = ranks.filter((x) => x !== null);
  const expected = numeric.length ? Array.from({ length: Math.max(...numeric) }, (_, i) => i + 1) : [];
  if (ranks.some((x) => x === null) || JSON.stringify([...numeric].sort((a, b) => a - b)) !== JSON.stringify(expected)) issueRows.push({ issue: "rank_sequence_defect", card_id: cardId, rows: group.map((r) => r._row).join(";"), detail: `ranks=${JSON.stringify(ranks)}, expected=${JSON.stringify(expected)}` });
  for (const field of ["date", "sport", "match", "competition", "market_group"]) {
    const values = [...new Set(group.map((r) => clean(r[field])))];
    if (values.length > 1) issueRows.push({ issue: "card_field_conflict", card_id: cardId, rows: group.map((r) => r._row).join(";"), detail: `${field}=${JSON.stringify(values.sort())}` });
  }
  const pByRank = group.map((r) => [intOrNull(r.rank), numOrNull(r.stated_probability), r]).filter(([rank, p]) => rank !== null && p !== null).sort((a, b) => a[0] - b[0]);
  for (let i = 1; i < pByRank.length; i++) {
    const [ra, pa, rowA] = pByRank[i - 1], [rb, pb, rowB] = pByRank[i];
    if (pb > pa + 1e-9) issueRows.push({ issue: "rank_probability_inversion", card_id: cardId, rows: `${rowA._row};${rowB._row}`, detail: `rank ${ra} p=${pa.toFixed(3)} < rank ${rb} p=${pb.toFixed(3)}` });
  }
}

for (const r of csvRows) {
  const s = status(r), rank = intOrNull(r.rank), p = numOrNull(r.stated_probability), bucket = clean(r.stated_probability_bucket), row = r._row;
  if (!["W", "L", "P", "VOID"].includes(s)) issueRows.push({ issue: "invalid_or_blank_status", card_id: r.card_id, rows: row, detail: s });
  if (["W", "L", "P"].includes(s) && !clean(r.result)) issueRows.push({ issue: "settled_missing_result", card_id: r.card_id, rows: row, detail: r.option });
  if (["W", "L", "P"].includes(s) && !clean(r.settlement_source)) issueRows.push({ issue: "settled_missing_source", card_id: r.card_id, rows: row, detail: r.option });
  if (p === null || p < 0 || p > 1) issueRows.push({ issue: "invalid_or_missing_probability", card_id: r.card_id, rows: row, detail: r.stated_probability });
  else if (/^\d{2}-\d{2}$/.test(bucket)) {
    const [lo, hi] = bucket.split("-").map(Number), pct = p * 100;
    if (!(pct >= lo - 1e-9 && pct < hi + 1 + 1e-9)) issueRows.push({ issue: "probability_bucket_mismatch", card_id: r.card_id, rows: row, detail: `bucket=${bucket}, p=${p}` });
  }
  const topFlag = truth(r.top_pick_loss), expectedTop = rank === 1 && s === "L";
  if (topFlag !== null && topFlag !== expectedTop) issueRows.push({ issue: "top_pick_loss_flag_mismatch", card_id: r.card_id, rows: row, detail: `rank=${rank}, status=${s}, flag=${topFlag}, expected=${expectedTop}` });
  const group = cards.get(r.card_id) || [];
  const maxRank = Math.max(...group.map((x) => intOrNull(x.rank) ?? -1));
  const bottomFlag = truth(r.bottom_pick_win), expectedBottom = rank === maxRank && s === "W" && group.length > 1;
  if (bottomFlag !== null && bottomFlag !== expectedBottom) issueRows.push({ issue: "bottom_pick_win_flag_mismatch", card_id: r.card_id, rows: row, detail: `rank=${rank}/${maxRank}, status=${s}, flag=${bottomFlag}, expected=${expectedBottom}` });
}

const { pairs: complementPairs, cardStats } = findComplements(csvRows);
for (const pair of complementPairs) {
  if (!pair.outcome_consistent) issueRows.push({ issue: "complement_outcome_contradiction", card_id: pair.card_id, rows: `${pair.row_a};${pair.row_b}`, detail: `${pair.status_a}/${pair.status_b}: ${pair.option_a} <> ${pair.option_b}` });
  if (pair.probability_sum !== null && Math.abs(pair.probability_sum - 1) > 0.03) issueRows.push({ issue: "complement_probability_sum", card_id: pair.card_id, rows: `${pair.row_a};${pair.row_b}`, detail: `p sum=${pair.probability_sum.toFixed(3)}` });
}

const leakagePattern = /\b(final|settled|won|lost|result|finished|confirmed by final|after the game|postgame)\b/i;
const possibleLeakage = [];
for (const r of csvRows) for (const field of ["frequency_count_base", "projection_band", "line_or_threshold", "option"]) if (leakagePattern.test(clean(r[field]))) possibleLeakage.push({ card_id: r.card_id, row: r._row, field, value: r[field] });

const coverageFields = ["stated_probability", "frequency_count_base", "projection_band", "line_or_threshold", "result", "settlement_source", "phase_source", "form_delta_verdict", "form_anchor_window", "press_signal_class", "press_signal_quote_logged", "officials_named", "officials_source_timestamp", "source_confidence_score", "source_disagreement_note", "similar_condition_form", "role_replacement_bench_verdict", "style_fit_note", "volatility_stability_note", "prediction_triggers"];
const coverage = Object.fromEntries(coverageFields.map((field) => [field, { nonblank: csvRows.filter((r) => clean(r[field])).length, total: csvRows.length }]));
const flagFields = ["ruleset_error", "availability_or_eligibility_error", "settlement_convention_error", "source_status_error", "projection_error", "rank_slot_calibration_error"];
const flags = Object.fromEntries(flagFields.map((field) => [field, csvRows.filter((r) => truth(r[field]) === true).length]));
const flagCombinations = countBy(csvRows, (r) => { const active = flagFields.filter((f) => truth(r[f]) === true); return active.length ? active.join("+") : "none"; });

const v2 = parseMarkdown(V2_PATH), v3 = parseMarkdown(V3_PATH);
const allLogRows = [...v2.parsed, ...v3.parsed];
const jsonInventory = fs.readdirSync(ROOT).filter((f) => f.endsWith(".json")).sort().map((f) => {
  const file = path.join(ROOT, f), stat = fs.statSync(file);
  try {
    const text = fs.readFileSync(file, "utf8").replace(/^\uFEFF/, ""), obj = JSON.parse(text);
    const topType = Array.isArray(obj) ? "array" : typeof obj === "object" && obj !== null ? "object" : typeof obj;
    const topKeys = topType === "object" ? Object.keys(obj).slice(0, 30) : [];
    const sample = text.slice(0, 100000);
    return { file: f, bytes: stat.size, modified: stat.mtime.toISOString(), top_type: topType, top_size: topType === "array" ? obj.length : topType === "object" ? Object.keys(obj).length : null, top_keys: topKeys, mentions_final: /"(?:status|state|type|detail)"\s*:\s*"[^"]*(?:final|complete|postponed)/i.test(sample), mentions_odds: /odds|moneyline|spread|overunder/i.test(sample) };
  } catch (error) { return { file: f, error: String(error) }; }
});

const sportSummary = summarizeGroup(csvRows, (r) => canonicalSport(r.sport));
const exactSportSummary = summarizeGroup(csvRows, (r) => clean(r.sport) || "UNKNOWN");
const rankSummary = summarizeGroup(csvRows, (r) => clean(r.rank) || "BLANK");
const marketSummary = summarizeGroup(csvRows, marketFamily);
const bucketSummary = summarizeGroup(csvRows, (r) => clean(r.stated_probability_bucket) || "BLANK");
const xlsxSportSummary = summarizeGroup(xlsxRows, (r) => canonicalSport(r.sport));
const xlsxRankSummary = summarizeGroup(xlsxRows, (r) => clean(r.rank) || "BLANK");
const recentWindows = Object.fromEntries([
  ["2026-07-01_plus", xlsxRows.filter((r) => r.date >= "2026-07-01")],
  ["2026-07-10_plus", xlsxRows.filter((r) => r.date >= "2026-07-10")],
  ["2026-07-12_plus", xlsxRows.filter((r) => r.date >= "2026-07-12")],
].map(([label, rows]) => [label, {
  overall: metricBlock(rows),
  calibration: calibrationBlock(rows),
  ranks: summarizeGroup(rows, (r) => clean(r.rank) || "BLANK"),
  sports: summarizeGroup(rows, (r) => canonicalSport(r.sport)),
  unique_cards: new Set(rows.map((r) => r.card_id)).size,
}]));
const liveRows = xlsxRows.filter((r) => /live/i.test(`${r.card_id} ${r.sport} ${r.market_group} ${r.settlement_convention}`));
const nonLiveRows = xlsxRows.filter((r) => !liveRows.includes(r));
const fullyComplementary = cardStats.filter((x) => x.fully_complementary_four_pick);
const pairedRows = new Set(complementPairs.flatMap((p) => [p.row_a, p.row_b]));
const dated = csvRows.map((r) => r.date).filter((d) => /^\d{4}-\d{2}-\d{2}$/.test(d)).sort();

const summary = {
  generated: new Date().toISOString(),
  sources: {
    csv: { ...fileMeta(CSV_PATH), rows_including_template: csvAll.length, data_rows: csvRows.length },
    xlsx: { ...fileMeta(INSPECT_PATH), rows_including_template: xlsxAll.length, data_rows: xlsxRows.length, table_address: xlsxTable.address },
    v2: { ...fileMeta(V2_PATH), dated_table_rows: v2.tableRows.length },
    v3: { ...fileMeta(V3_PATH), dated_table_rows: v3.tableRows.length },
  },
  csv_overall: metricBlock(csvRows),
  csv_calibration: calibrationBlock(csvRows),
  xlsx_overall: metricBlock(xlsxRows),
  xlsx_calibration: calibrationBlock(xlsxRows),
  xlsx_sports: xlsxSportSummary,
  xlsx_ranks: xlsxRankSummary,
  xlsx_recent_windows: recentWindows,
  xlsx_live_split: {
    live: { overall: metricBlock(liveRows), calibration: calibrationBlock(liveRows), unique_cards: new Set(liveRows.map((r) => r.card_id)).size },
    non_live: { overall: metricBlock(nonLiveRows), calibration: calibrationBlock(nonLiveRows), unique_cards: new Set(nonLiveRows.map((r) => r.card_id)).size },
  },
  unique_cards: cards.size,
  card_size_distribution: countBy([...cards.values()], (g) => g.length),
  date_range: [dated[0], dated.at(-1)],
  sports: sportSummary,
  exact_sports: exactSportSummary,
  ranks: rankSummary,
  markets: marketSummary,
  probability_buckets: bucketSummary,
  complements: {
    pairs: complementPairs.length,
    cards_with_pairs: new Set(complementPairs.map((p) => p.card_id)).size,
    rows_in_pairs: pairedRows.size,
    share_rows_in_pairs: pairedRows.size / csvRows.length,
    fully_complementary_four_pick_cards: fullyComplementary.length,
    fully_complementary_rows: fullyComplementary.reduce((a, b) => a + b.rows, 0),
    outcome_contradictions: complementPairs.filter((p) => !p.outcome_consistent).length,
    probability_sum_outside_0_97_1_03: complementPairs.filter((p) => p.probability_sum !== null && Math.abs(p.probability_sum - 1) > 0.03).length,
  },
  duplicates: {
    exact_duplicate_groups: exactDupGroups.length,
    exact_duplicate_extra_rows: exactDupGroups.reduce((a, g) => a + g.length - 1, 0),
    duplicate_natural_keys: duplicateNaturalKeys.length,
    cross_card_same_event_option_groups: crossCardRepeats.length,
    cross_card_same_event_option_extra_rows: crossCardRepeats.reduce((a, g) => a + g.count - 1, 0),
  },
  csv_xlsx_diff: { diff_records: diffRows.length, by_kind: countBy(diffRows, (r) => r.kind) },
  issues: { count: issueRows.length, by_type: countBy(issueRows, (r) => r.issue) },
  possible_outcome_language_in_input_fields: { count: possibleLeakage.length, by_field: countBy(possibleLeakage, (r) => r.field) },
  coverage,
  error_flags: flags,
  error_flag_combinations: flagCombinations,
  logs: {
    v2_outcome_counts: v2.outcome_counts, v3_outcome_counts: v3.outcome_counts,
    v2_duplicate_date_sport_match_keys: v2.duplicates.length, v3_duplicate_date_sport_match_keys: v3.duplicates.length,
    parsed_rows_with_wl: allLogRows.filter((r) => r.parsed_wins !== null).length,
  },
  json_inventory: jsonInventory,
};

fs.writeFileSync(path.join(OUT, "performance_summary.json"), JSON.stringify(summary, null, 2) + "\n", "utf8");
writeCSV(path.join(OUT, "sport_summary.csv"), sportSummary);
writeCSV(path.join(OUT, "exact_sport_summary.csv"), exactSportSummary);
writeCSV(path.join(OUT, "rank_summary.csv"), rankSummary);
writeCSV(path.join(OUT, "market_summary.csv"), marketSummary);
writeCSV(path.join(OUT, "calibration_buckets.csv"), bucketSummary);
writeCSV(path.join(OUT, "complement_pairs.csv"), complementPairs);
writeCSV(path.join(OUT, "ledger_issue_records.csv"), issueRows);
writeCSV(path.join(OUT, "cross_card_repeats.csv"), crossCardRepeats);
writeCSV(path.join(OUT, "duplicate_natural_keys.csv"), duplicateNaturalKeys);
writeCSV(path.join(OUT, "csv_xlsx_diff.csv"), diffRows);
writeCSV(path.join(OUT, "possible_outcome_language.csv"), possibleLeakage);
writeCSV(path.join(OUT, "log_rows.csv"), allLogRows);
writeCSV(path.join(OUT, "json_inventory.csv"), jsonInventory);
console.log(JSON.stringify(summary, null, 2));
