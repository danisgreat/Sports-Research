import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const root = "C:/Users/danie/Desktop/Sports Research";
const outDir = `${root}/outputs/comprehensive_audit_20260716`;
const previewDir = `${outDir}/final_workbook_previews`;
const sourcePath = `${root}/outputs/settlement_20260713/SPORTS_CALIBRATION_LEDGER_v2_settled.xlsx`;
const outputPath = `${outDir}/SPORTS_RESEARCH_AUDIT_20260716.xlsx`;
const legacyCsvPath = `${root}/LEGACY_LEDGER_MIGRATION_AUDIT_20260716.csv`;
await fs.mkdir(previewDir, { recursive: true });

const COLORS = {
  navy: "#17324D",
  blue: "#2F75B5",
  teal: "#2A9D8F",
  amber: "#F4B942",
  red: "#C94C4C",
  green: "#4F8A5B",
  light: "#EEF3F7",
  paleBlue: "#DCEAF7",
  paleAmber: "#FFF3CD",
  paleRed: "#FCE8E6",
  paleGreen: "#E7F3E8",
  grey: "#5F6B76",
  line: "#CDD6DF",
  white: "#FFFFFF",
};

function normBool(v) {
  return String(v ?? "").trim().toUpperCase() === "TRUE";
}

function num(v) {
  const n = Number(v);
  return Number.isFinite(n) ? n : null;
}

function normalizeSport(raw) {
  const s = String(raw ?? "").toLowerCase();
  if (s.includes("afl") || s.includes("australian")) return "Australian football";
  if (s.includes("soccer") || s.includes("fifa") || s.includes("football/world cup")) return "Soccer";
  if (s.includes("cric") || s.includes("odi") || s.includes("t20")) return "Cricket";
  if (s.includes("mlb") || s.includes("kbo") || s.includes("npb") || s.includes("baseball")) return "Baseball";
  if (s.includes("wnba") || s.includes("nba") || s.includes("basketball") || s.includes("fiba")) return "Basketball";
  if (s.includes("nhl") || s.includes("hockey")) return "Ice hockey";
  if (s.includes("nrl") || s.includes("rugby league")) return "Rugby league";
  if (s.includes("nfl") || s.includes("ncaa football") || s.includes("american football")) return "American football";
  if (s.includes("tennis") || s.includes("atp") || s.includes("wta")) return "Tennis";
  if (s.includes("golf") || s.includes("pga")) return "Golf";
  return raw ? String(raw) : "Other";
}

function expectedBucketMismatch(bucket, probability) {
  if (probability === null || !bucket) return false;
  const b = String(bucket).trim();
  if (/^\d+\+$/.test(b)) return probability * 100 < Number(b.replace("+", ""));
  const m = b.match(/^(\d+)\s*-\s*(\d+)$/);
  if (!m) return false;
  const pct = probability * 100;
  return pct < Number(m[1]) || pct >= Number(m[2]) + 1;
}

function optionSideKey(option) {
  const text = String(option ?? "").toLowerCase().replace(/\s+/g, " ").trim();
  if (/\bover\b/.test(text)) return { type: "total", side: "over", key: text.replace(/\bover\b/g, "side") };
  if (/\bunder\b/.test(text)) return { type: "total", side: "under", key: text.replace(/\bunder\b/g, "side") };
  const spread = text.match(/([+-])(\d+(?:\.\d+)?)\b/);
  if (spread) return { type: "spread", side: spread[1], key: `spread:${spread[2]}` };
  return null;
}

function csvEscape(value) {
  if (value === null || value === undefined) return "";
  const text = String(value);
  if (/[",\r\n]/.test(text)) return `"${text.replace(/"/g, '""')}"`;
  return text;
}

function excelCol(n) {
  let x = n;
  let s = "";
  while (x > 0) {
    const r = (x - 1) % 26;
    s = String.fromCharCode(65 + r) + s;
    x = Math.floor((x - 1) / 26);
  }
  return s;
}

function addTitle(sheet, title, subtitle, endCol) {
  sheet.showGridLines = false;
  sheet.getRange(`A1:${endCol}1`).merge();
  sheet.getRange("A1").values = [[title]];
  sheet.getRange(`A1:${endCol}1`).format = {
    fill: COLORS.navy,
    font: { bold: true, color: COLORS.white, size: 18 },
    verticalAlignment: "center",
  };
  sheet.getRange(`A1:${endCol}1`).format.rowHeight = 30;
  sheet.getRange(`A2:${endCol}2`).merge();
  sheet.getRange("A2").values = [[subtitle]];
  sheet.getRange(`A2:${endCol}2`).format = {
    fill: COLORS.paleBlue,
    font: { color: COLORS.navy, italic: true, size: 10 },
    wrapText: true,
    verticalAlignment: "center",
  };
  sheet.getRange(`A2:${endCol}2`).format.rowHeight = 34;
}

function styleHeader(range) {
  range.format = {
    fill: COLORS.blue,
    font: { bold: true, color: COLORS.white },
    wrapText: true,
    verticalAlignment: "center",
    borders: { preset: "all", style: "thin", color: COLORS.line },
  };
}

function styleBody(range) {
  range.format = {
    borders: { preset: "all", style: "thin", color: COLORS.line },
    verticalAlignment: "top",
  };
}

function setColumnWidths(sheet, widths, rowEnd = 100) {
  widths.forEach((width, i) => {
    const col = excelCol(i + 1);
    sheet.getRange(`${col}1:${col}${rowEnd}`).format.columnWidth = width;
  });
}

const imported = await SpreadsheetFile.importXlsx(await FileBlob.load(sourcePath));
const importedSheet = imported.worksheets.getItem("Calibration Ledger");
const sourceValues = importedSheet.getRange("A1:AU451").values;
const headers = sourceValues[0].map((v) => String(v ?? ""));
const idx = Object.fromEntries(headers.map((h, i) => [h, i]));
const sourceRows = sourceValues.slice(1).filter((r) => {
  const id = String(r[idx.card_id] ?? "").trim();
  return id && id.toUpperCase() !== "TEMPLATE";
});

const groups = new Map();
for (const row of sourceRows) {
  const id = String(row[idx.card_id] ?? "");
  if (!groups.has(id)) groups.set(id, []);
  groups.get(id).push(row);
}
const complementCards = new Set();
const complementSelections = new Set();
for (const [cardId, rows] of groups.entries()) {
  const totalSides = new Map();
  const spreads = new Map();
  for (const row of rows) {
    const parsed = optionSideKey(row[idx.option]);
    if (!parsed) continue;
    const map = parsed.type === "total" ? totalSides : spreads;
    if (!map.has(parsed.key)) map.set(parsed.key, []);
    map.get(parsed.key).push({ side: parsed.side, row });
  }
  for (const entries of totalSides.values()) {
    const sides = new Set(entries.map((e) => e.side));
    if (sides.has("over") && sides.has("under")) {
      complementCards.add(cardId);
      entries.forEach((e) => complementSelections.add(e.row));
    }
  }
  for (const entries of spreads.values()) {
    const sides = new Set(entries.map((e) => e.side));
    if (sides.has("+") && sides.has("-")) {
      complementCards.add(cardId);
      entries.forEach((e) => complementSelections.add(e.row));
    }
  }
}

const legacyRows = sourceRows.map((row, i) => {
  const cardId = String(row[idx.card_id] ?? "");
  const probability = num(row[idx.stated_probability]);
  const status = String(row[idx.win_loss_push] ?? "").trim().toUpperCase();
  const binary = status === "W" ? 1 : status === "L" ? 0 : null;
  const brier = binary === null || probability === null ? null : (probability - binary) ** 2;
  const settlementSource = String(row[idx.settlement_source] ?? "");
  const base = String(row[idx.frequency_count_base] ?? "");
  const leakage = /(final|settlement|results? log|scorecard|post-event|settled|full[- ]time)/i.test(base);
  const flags = [];
  if (normBool(row[idx.projection_error])) flags.push("projection_error");
  if (normBool(row[idx.rank_slot_calibration_error])) flags.push("rank_error");
  if (normBool(row[idx.source_status_error])) flags.push("source_error");
  if (normBool(row[idx.ruleset_error])) flags.push("ruleset_error");
  if (normBool(row[idx.availability_or_eligibility_error])) flags.push("availability_error");
  if (normBool(row[idx.settlement_convention_error])) flags.push("settlement_rule_error");
  if (leakage) flags.push("potential_post_event_input_text");
  if (complementSelections.has(row)) flags.push("exact_complement_selection");
  return {
    legacy_row: i + 1,
    card_id: cardId,
    date: String(row[idx.date] ?? ""),
    sport_family: normalizeSport(row[idx.sport]),
    sport_raw: String(row[idx.sport] ?? ""),
    match: String(row[idx.match] ?? ""),
    competition: String(row[idx.competition] ?? ""),
    market_group: String(row[idx.market_group] ?? ""),
    rank: num(row[idx.rank]),
    option: String(row[idx.option] ?? ""),
    line: row[idx.line_or_threshold] ?? "",
    probability,
    status,
    binary,
    brier,
    complement_card: complementSelections.has(row),
    probability_bucket: String(row[idx.stated_probability_bucket] ?? ""),
    bucket_mismatch: expectedBucketMismatch(String(row[idx.stated_probability_bucket] ?? ""), probability),
    settlement_source: settlementSource,
    source_has_url: /https?:\/\//i.test(settlementSource),
    potential_post_event_input: leakage,
    eligible_v3: false,
    exclusion_reason: "LEGACY_UNVERIFIED_SNAPSHOT: no immutable cutoff/model/source packet",
    audit_note: flags.join("; ") || "legacy schema only",
  };
});

const legacyCsvHeaders = [
  "legacy_row","card_id","date","sport_family","sport_raw","match","competition","market_group","rank","option","line",
  "stated_probability","status","binary_outcome","brier_component","exact_complement_selection","probability_bucket","bucket_mismatch",
  "settlement_source","settlement_has_url","potential_post_event_input","eligible_for_v3_evaluation","exclusion_reason","audit_note",
];
const legacyCsvLines = [legacyCsvHeaders.join(",")];
for (const r of legacyRows) {
  legacyCsvLines.push([
    r.legacy_row,r.card_id,r.date,r.sport_family,r.sport_raw,r.match,r.competition,r.market_group,r.rank,r.option,r.line,
    r.probability,r.status,r.binary,r.brier,r.complement_card,r.probability_bucket,r.bucket_mismatch,r.settlement_source,
    r.source_has_url,r.potential_post_event_input,r.eligible_v3,r.exclusion_reason,r.audit_note,
  ].map(csvEscape).join(","));
}
await fs.writeFile(legacyCsvPath, legacyCsvLines.join("\r\n") + "\r\n", "utf8");

const wb = Workbook.create();
const readme = wb.worksheets.add("Read Me");
const dashboard = wb.worksheets.add("Dashboard");
const sport = wb.worksheets.add("Sport Summary");
const rank = wb.worksheets.add("Rank Summary");
const calibration = wb.worksheets.add("Calibration");
const issues = wb.worksheets.add("Issue Register");
const legacy = wb.worksheets.add("Legacy Audit");
const sources = wb.worksheets.add("Source Map");
const raw = wb.worksheets.add("Raw Manifest");
const predictionTemplate = wb.worksheets.add("Prediction Template");
const settlementTemplate = wb.worksheets.add("Settlement Template");

// Read Me
addTitle(readme, "Sports Research Audit Workbook", "Generated 2026-07-16 AEST. This workbook documents the repair; it is not proof of a profitable or validated forecasting system.", "H");
const readmeRows = [
  ["Operational status", "SUSPENDED — NO ACTIVE MODELS", "Meaning", "Only MODEL UNAVAILABLE / PASS is permitted until a scoped model passes prospective validation."],
  ["Historical record", "Legacy / unverified lock", "Meaning", "The recorded probabilities were not backed by immutable cutoff, model, data and source-packet versions."],
  ["Gross reconciliation", "253-190-2 in latest structured XLSX", "Later narrative", "257-194-2 after eight additional decisions; neither is a certified KPI."],
  ["ROI", "Not computable", "Reason", "No complete odds, price timestamps, stakes, execution or payout trail."],
  ["Primary defect", "Complement distortion", "Evidence", "At least 150 exact pairs occupy 300 of 437 CSV rows; later XLSX rows add more."],
  ["Canonical manual", "combined_sports_doc_v3.md", "Source rules", "SPORTS_SOURCE_REGISTRY_v3.md"],
  ["Data contract", "SPORTS_DATA_DICTIONARY_v3.md", "Validation", "SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md"],
  ["Legacy audit", "Legacy Audit sheet / migration CSV", "Restriction", "Every legacy row is excluded from official v3 evaluation."],
];
readme.getRange(`A4:D${3 + readmeRows.length}`).values = readmeRows;
styleBody(readme.getRange(`A4:D${3 + readmeRows.length}`));
readme.getRange(`A4:D${3 + readmeRows.length}`).format.wrapText = true;
readme.getRange("A4:A11").format = { fill: COLORS.paleBlue, font: { bold: true, color: COLORS.navy } };
readme.getRange("C4:C11").format = { fill: COLORS.light, font: { bold: true, color: COLORS.navy } };
readme.getRange("A14:H14").merge();
readme.getRange("A14").values = [["How to read the workbook"]];
readme.getRange("A14:H14").format = { fill: COLORS.teal, font: { bold: true, color: COLORS.white } };
readme.getRange("A15:H19").merge(true);
readme.getRange("A15:A19").values = [
  ["Dashboard: high-level failure evidence and current controls."],
  ["Sport / Rank / Calibration: retrospective descriptive views only; correlation and selection bias remain."],
  ["Issue Register: root causes, evidence and implemented controls."],
  ["Legacy Audit: row-level migration flags and formula-derived Brier components."],
  ["Templates / Source Map / Raw Manifest: safe forward structure and evidence boundaries."],
];
readme.getRange("A15:H19").format = { wrapText: true, borders: { preset: "all", style: "thin", color: COLORS.line } };
setColumnWidths(readme, [20, 31, 18, 52, 4, 4, 4, 4], 25);
readme.getRange("A4:D11").format.autofitRows();

// Legacy Audit data and formulas
addTitle(legacy, "Legacy Ledger Migration Audit", "449 non-template rows from the latest structured XLSX. All remain excluded from v3 evaluation because the original forecast lock cannot be proven.", "X");
const legacyHeaders = [
  "Legacy row","Card ID","Date","Sport family","Sport raw","Match","Competition","Market group","Rank","Option","Line",
  "Stated p","Status","Binary","Brier","Exact complement row","Probability bucket","Bucket mismatch","Settlement source","Source has URL",
  "Potential post-event input","Eligible v3","Exclusion reason","Audit note",
];
legacy.getRange("A4:X4").values = [legacyHeaders];
styleHeader(legacy.getRange("A4:X4"));
const legacyValueRows = legacyRows.map((r) => [
  r.legacy_row,r.card_id,r.date,r.sport_family,r.sport_raw,r.match,r.competition,r.market_group,r.rank,r.option,r.line,r.probability,
    r.status,null,null,r.complement_card ? "YES" : "NO",r.probability_bucket,r.bucket_mismatch ? "YES" : "NO",r.settlement_source,null,r.potential_post_event_input ? "YES" : "NO",
    r.eligible_v3 ? "YES" : "NO",r.exclusion_reason,r.audit_note,
]);
const legacyStart = 5;
const legacyEnd = legacyStart + legacyValueRows.length - 1;
legacy.getRange(`A${legacyStart}:X${legacyEnd}`).values = legacyValueRows;
legacy.getRange(`N${legacyStart}`).formulas = [[`=IF(M${legacyStart}="W",1,IF(M${legacyStart}="L",0,""))`]];
legacy.getRange(`N${legacyStart}:N${legacyEnd}`).fillDown();
legacy.getRange(`O${legacyStart}`).formulas = [[`=IF(OR(M${legacyStart}="W",M${legacyStart}="L"),(L${legacyStart}-N${legacyStart})^2,"")`]];
legacy.getRange(`O${legacyStart}:O${legacyEnd}`).fillDown();
legacy.getRange(`T${legacyStart}`).formulas = [[`=IF(IFERROR(ISNUMBER(SEARCH("http",S${legacyStart})),FALSE),"YES","NO")`]];
legacy.getRange(`T${legacyStart}:T${legacyEnd}`).fillDown();
styleBody(legacy.getRange(`A${legacyStart}:X${legacyEnd}`));
legacy.getRange(`L${legacyStart}:L${legacyEnd}`).format.numberFormat = "0.0%";
legacy.getRange(`O${legacyStart}:O${legacyEnd}`).format.numberFormat = "0.0000";
legacy.getRange(`C${legacyStart}:C${legacyEnd}`).format.numberFormat = "yyyy-mm-dd";
legacy.getRange(`F${legacyStart}:H${legacyEnd}`).format.wrapText = true;
legacy.getRange(`J${legacyStart}:J${legacyEnd}`).format.wrapText = true;
legacy.getRange(`S${legacyStart}:X${legacyEnd}`).format.wrapText = true;
legacy.getRange(`P${legacyStart}:P${legacyEnd}`).conditionalFormats.add("containsText", { text: "YES", format: { fill: COLORS.paleAmber, font: { color: "#7A5200" } } });
legacy.getRange(`R${legacyStart}:R${legacyEnd}`).conditionalFormats.add("containsText", { text: "YES", format: { fill: COLORS.paleRed, font: { color: COLORS.red } } });
legacy.getRange(`U${legacyStart}:U${legacyEnd}`).conditionalFormats.add("containsText", { text: "YES", format: { fill: COLORS.paleRed } });
legacy.getRange(`V${legacyStart}:V${legacyEnd}`).conditionalFormats.add("containsText", { text: "NO", format: { fill: COLORS.paleRed, font: { color: COLORS.red, bold: true } } });
const legacyTable = legacy.tables.add(`A4:X${legacyEnd}`, true, "LegacyAuditTable");
legacyTable.style = "TableStyleMedium2";
legacy.freezePanes.freezeRows(4);
legacy.freezePanes.freezeColumns(2);
setColumnWidths(legacy, [10,30,12,20,20,28,25,22,8,45,11,11,10,10,12,14,16,14,44,13,18,12,44,38], legacyEnd);

// Dashboard
addTitle(dashboard, "Comprehensive Process Audit", "Formula-driven summary of the latest structured legacy workbook. Metrics are retrospective diagnostics, not certified prospective performance.", "P");
dashboard.getRange("A4:D4").values = [["Metric","Value","Interpretation","Status"]];
styleHeader(dashboard.getRange("A4:D4"));
const metricLabels = [
  ["Structured selections", null, "Non-template rows in latest settled XLSX", "LEGACY"],
  ["Decisive W/L", null, "Excludes pushes, voids and unresolved", "LEGACY"],
  ["Wins", null, "Raw count; correlated selections included", "LEGACY"],
  ["Losses", null, "Raw count; correlated selections included", "LEGACY"],
  ["Pushes", null, "Recorded P status", "LEGACY"],
  ["Raw hit rate", null, "Not an edge or ROI measure", "CAUTION"],
  ["Apparent Brier", null, "Unverified lock; do not call calibrated", "CAUTION"],
  ["Exact complement rows", null, "Rows belonging to a detected over/under or opposite-spread pair", "FAIL"],
  ["Exact complement share", null, "Mechanically inflates all-selection summaries", "FAIL"],
  ["Settlement rows with URL", null, "Legacy settlement source fields mostly contain prose", "FAIL"],
  ["Eligible for v3 evaluation", null, "Requires immutable cutoff/model/source packet", "FAIL"],
];
dashboard.getRange("A5:D15").values = metricLabels;
dashboard.getRange("B5:B15").formulas = [
  [`=COUNTA('Legacy Audit'!$B$${legacyStart}:$B$${legacyEnd})`],
  [`=COUNTIF('Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"W")+COUNTIF('Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"L")`],
  [`=COUNTIF('Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"W")`],
  [`=COUNTIF('Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"L")`],
  [`=COUNTIF('Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"P")`],
  ["=IF(B6=0,\"\",B7/B6)"],
  [`=AVERAGE('Legacy Audit'!$O$${legacyStart}:$O$${legacyEnd})`],
  [`=COUNTIF('Legacy Audit'!$P$${legacyStart}:$P$${legacyEnd},"YES")`],
  ["=IF(B5=0,\"\",B12/B5)"],
  [`=COUNTIF('Legacy Audit'!$T$${legacyStart}:$T$${legacyEnd},"YES")`],
  [`=COUNTIF('Legacy Audit'!$V$${legacyStart}:$V$${legacyEnd},"YES")`],
];
styleBody(dashboard.getRange("A5:D15"));
dashboard.getRange("A5:D15").format.wrapText = true;
dashboard.getRange("B10:B10").format.numberFormat = "0.0%";
dashboard.getRange("B11:B11").format.numberFormat = "0.0000";
dashboard.getRange("B13:B13").format.numberFormat = "0.0%";
dashboard.getRange("D5:D15").conditionalFormats.add("containsText", { text: "FAIL", format: { fill: COLORS.paleRed, font: { color: COLORS.red, bold: true } } });
dashboard.getRange("D5:D15").conditionalFormats.add("containsText", { text: "CAUTION", format: { fill: COLORS.paleAmber, font: { color: "#7A5200", bold: true } } });

dashboard.getRange("F4:P4").merge();
dashboard.getRange("F4").values = [["What failed and what replaced it"]];
dashboard.getRange("F4:P4").format = { fill: COLORS.teal, font: { bold: true, color: COLORS.white } };
const findings = [
  ["Old process", "Observed defect", "Replacement control"],
  ["Four/long ranked cards", "Opposite outcomes counted as separate picks; many cards guaranteed 2-2", "One declared decision per market; alternatives logged as candidates"],
  ["Mutable ledger row", "Pregame probability, result and postmortem co-located", "Immutable publication snapshot plus append-only settlement"],
  ["Penalty/exemption economy", "Custom accounting obscured raw ranking performance", "Proper scores, baselines, event-clustered uncertainty"],
  ["Fixed L5/L10/L15/L20 ritual", "Overlapping windows encouraged selection and recency bias", "Predeclared sport/market features tested chronologically"],
  ["All-sport confidence language", "No validated model cards for several named sports", "Coverage registry; unsupported scopes must PASS"],
  ["Poisson/simulation precision", "Assumed parameters and independent counts looked more certain than warranted", "Validated distribution, typed uncertainty, MCSE and convergence"],
  ["Research-only cards", "No prices, stakes or executions, so value/ROI claims were impossible", "Separate research and price modes; execution required for P&L/CLV"],
  ["Immediate rule after each miss", "Single-event narratives caused rule accretion and overfit", "Batch review, preregistered change ticket, new untouched test"],
];
dashboard.getRange("F5:H13").values = findings;
styleHeader(dashboard.getRange("F5:H5"));
styleBody(dashboard.getRange("F6:H13"));
dashboard.getRange("F5:H13").format.wrapText = true;
dashboard.getRange("F16:P16").merge();
dashboard.getRange("F16").values = [["Current publication rule: SUSPENDED — NO ACTIVE MODELS. A numerical probability is prohibited unless an ACTIVE, in-scope model passes the acceptance suite and prospective shadow gate."]];
dashboard.getRange("F16:P16").format = { fill: COLORS.paleRed, font: { bold: true, color: COLORS.red }, wrapText: true };
dashboard.getRange("F16:P16").format.rowHeight = 44;
setColumnWidths(dashboard, [25,15,48,14,3,23,42,48,3,3,3,3,3,3,3,3], 35);
dashboard.getRange("A5:D15").format.autofitRows();
dashboard.getRange("F5:H13").format.autofitRows();

// Sport Summary
addTitle(sport, "Legacy Performance by Sport Family", "Formula-derived from the latest structured legacy rows. No segment is activated by these retrospective figures.", "Q");
const sportFamilies = ["Australian football","Baseball","Basketball","Cricket","Soccer","Ice hockey","American football","Rugby league","Tennis","Golf"];
sport.getRange("A4:I4").values = [["Sport family","Decisions","W","L","P","Hit rate","Mean stated p","Apparent Brier","Operational status"]];
styleHeader(sport.getRange("A4:I4"));
sport.getRange(`A5:A${4 + sportFamilies.length}`).values = sportFamilies.map((s) => [s]);
sport.getRange(`I5:I${4 + sportFamilies.length}`).values = sportFamilies.map(() => ["UNSUPPORTED"]);
for (let i = 0; i < sportFamilies.length; i++) {
  const r = 5 + i;
  sport.getRange(`B${r}:H${r}`).formulas = [[
    `=COUNTIFS('Legacy Audit'!$D$${legacyStart}:$D$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"W")+COUNTIFS('Legacy Audit'!$D$${legacyStart}:$D$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"L")`,
    `=COUNTIFS('Legacy Audit'!$D$${legacyStart}:$D$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"W")`,
    `=COUNTIFS('Legacy Audit'!$D$${legacyStart}:$D$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"L")`,
    `=COUNTIFS('Legacy Audit'!$D$${legacyStart}:$D$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"P")`,
    `=IF(B${r}=0,"",C${r}/B${r})`,
    `=IF(B${r}=0,"",(SUMIFS('Legacy Audit'!$L$${legacyStart}:$L$${legacyEnd},'Legacy Audit'!$D$${legacyStart}:$D$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"W")+SUMIFS('Legacy Audit'!$L$${legacyStart}:$L$${legacyEnd},'Legacy Audit'!$D$${legacyStart}:$D$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"L"))/B${r})`,
    `=IF(B${r}=0,"",SUMIFS('Legacy Audit'!$O$${legacyStart}:$O$${legacyEnd},'Legacy Audit'!$D$${legacyStart}:$D$${legacyEnd},$A${r})/B${r})`,
  ]];
}
styleBody(sport.getRange(`A5:I${4 + sportFamilies.length}`));
sport.getRange(`F5:G${4 + sportFamilies.length}`).format.numberFormat = "0.0%";
sport.getRange(`H5:H${4 + sportFamilies.length}`).format.numberFormat = "0.000";
sport.getRange(`I5:I${4 + sportFamilies.length}`).format = { fill: COLORS.paleRed, font: { color: COLORS.red, bold: true } };
sport.tables.add(`A4:I${4 + sportFamilies.length}`, true, "SportSummaryTable").style = "TableStyleMedium2";
const chartSportCount = 5;
sport.getRange("S4:T4").values = [["Sport family","Hit rate"]];
for (let i = 0; i < chartSportCount; i++) {
  const r = 5 + i;
  sport.getRange(`S${r}:T${r}`).formulas = [[`=A${r}`, `=F${r}`]];
}
const sportChart = sport.charts.add("bar", sport.getRange(`S4:T${4 + chartSportCount}`));
sportChart.title = "Legacy hit rate by sport (descriptive only)";
sportChart.hasLegend = false;
sportChart.yAxis = { numberFormatCode: "0%", min: 0, max: 1 };
sportChart.setPosition("K4", "Q19");
sport.freezePanes.freezeRows(4);
setColumnWidths(sport, [23,12,9,9,9,12,15,16,20,3,12,12,12,12,12,12,12], 25);

// Rank Summary
addTitle(rank, "Legacy Performance by Rank Slot", "The old rank hierarchy failed its own targets and is retired. Rank is not an active v3 field.", "Q");
rank.getRange("A4:H4").values = [["Legacy rank","Decisions","W","L","P","Hit rate","Mean stated p","Interpretation"]];
styleHeader(rank.getRange("A4:H4"));
for (let i = 1; i <= 8; i++) {
  const r = 4 + i;
  rank.getRange(`A${r}`).values = [[i]];
  rank.getRange(`B${r}:G${r}`).formulas = [[
    `=COUNTIFS('Legacy Audit'!$I$${legacyStart}:$I$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"W")+COUNTIFS('Legacy Audit'!$I$${legacyStart}:$I$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"L")`,
    `=COUNTIFS('Legacy Audit'!$I$${legacyStart}:$I$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"W")`,
    `=COUNTIFS('Legacy Audit'!$I$${legacyStart}:$I$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"L")`,
    `=COUNTIFS('Legacy Audit'!$I$${legacyStart}:$I$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"P")`,
    `=IF(B${r}=0,"",C${r}/B${r})`,
    `=IF(B${r}=0,"",(SUMIFS('Legacy Audit'!$L$${legacyStart}:$L$${legacyEnd},'Legacy Audit'!$I$${legacyStart}:$I$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"W")+SUMIFS('Legacy Audit'!$L$${legacyStart}:$L$${legacyEnd},'Legacy Audit'!$I$${legacyStart}:$I$${legacyEnd},$A${r},'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd},"L"))/B${r})`,
  ]];
  rank.getRange(`H${r}`).values = [[i === 1 ? "Below former 80% target" : i === 4 ? "Bottom slot won too often" : i >= 6 ? "Severe ordering inversion / small n" : "Retrospective only"]];
}
styleBody(rank.getRange("A5:H12"));
rank.getRange("F5:G12").format.numberFormat = "0.0%";
rank.getRange("H5:H12").format.wrapText = true;
rank.tables.add("A4:H12", true, "RankSummaryTable").style = "TableStyleMedium2";
rank.getRange("S4:T4").values = [["Legacy rank","Hit rate"]];
for (let i = 1; i <= 8; i++) {
  const r = 4 + i;
  rank.getRange(`S${r}:T${r}`).formulas = [[`=A${r}`, `=F${r}`]];
}
const rankChart = rank.charts.add("bar", rank.getRange("S4:T12"));
rankChart.title = "Legacy hit rate by rank";
rankChart.hasLegend = false;
rankChart.yAxis = { numberFormatCode: "0%", min: 0, max: 1 };
rankChart.setPosition("J4", "Q18");
rank.freezePanes.freezeRows(4);
setColumnWidths(rank, [14,12,9,9,9,12,15,38,3,12,12,12,12,12,12,12,12], 22);

// Calibration
addTitle(calibration, "Legacy Reliability View", "Fixed deciles are shown only as a descriptive diagnostic. The lock is unverified and selections are correlated; this is not evidence of production calibration.", "R");
calibration.getRange("A4:H4").values = [["Bucket","Low","High","N","Wins","Mean p","Observed","Brier"]];
styleHeader(calibration.getRange("A4:H4"));
for (let i = 0; i < 10; i++) {
  const r = 5 + i;
  const low = i / 10;
  const high = (i + 1) / 10;
  const op = i === 9 ? "<=" : "<";
  calibration.getRange(`A${r}:C${r}`).values = [[`${i * 10}-${i * 10 + 9}%`, low, high]];
  const rangeP = `'Legacy Audit'!$L$${legacyStart}:$L$${legacyEnd}`;
  const rangeS = `'Legacy Audit'!$M$${legacyStart}:$M$${legacyEnd}`;
  const rangeB = `'Legacy Audit'!$O$${legacyStart}:$O$${legacyEnd}`;
  const lowCrit = `">=${low}"`;
  const highCrit = `"${op}${high}"`;
  const w = `COUNTIFS(${rangeP},${lowCrit},${rangeP},${highCrit},${rangeS},"W")`;
  const l = `COUNTIFS(${rangeP},${lowCrit},${rangeP},${highCrit},${rangeS},"L")`;
  const sumPW = `SUMIFS(${rangeP},${rangeP},${lowCrit},${rangeP},${highCrit},${rangeS},"W")`;
  const sumPL = `SUMIFS(${rangeP},${rangeP},${lowCrit},${rangeP},${highCrit},${rangeS},"L")`;
  const sumB = `SUMIFS(${rangeB},${rangeP},${lowCrit},${rangeP},${highCrit})`;
  calibration.getRange(`D${r}:H${r}`).formulas = [[
    `=${w}+${l}`,
    `=${w}`,
    `=IF(D${r}=0,"",(${sumPW}+${sumPL})/D${r})`,
    `=IF(D${r}=0,"",E${r}/D${r})`,
    `=IF(D${r}=0,"",${sumB}/D${r})`,
  ]];
}
styleBody(calibration.getRange("A5:H14"));
calibration.getRange("B5:C14").format.numberFormat = "0%";
calibration.getRange("F5:G14").format.numberFormat = "0.0%";
calibration.getRange("H5:H14").format.numberFormat = "0.0000";
calibration.tables.add("A4:H14", true, "CalibrationTable").style = "TableStyleMedium2";
calibration.getRange("J4:L4").values = [["Bucket","Mean predicted","Observed"]];
for (let i = 0; i < 10; i++) {
  const r = 5 + i;
  calibration.getRange(`J${r}:L${r}`).formulas = [[`=A${r}`, `=F${r}`, `=G${r}`]];
}
const calChart = calibration.charts.add("line", calibration.getRange("J4:L14"));
calChart.title = "Legacy predicted vs observed";
calChart.hasLegend = true;
calChart.yAxis = { numberFormatCode: "0%", min: 0, max: 1 };
calChart.xAxis = { axisType: "textAxis" };
calChart.setPosition("J4", "R20");
calibration.getRange("A17:H18").merge(true);
calibration.getRange("A17:A18").values = [
  ["Warning: apparent Brier/log loss cannot be accepted as prospective calibration because publication timestamps, model versions and immutable source snapshots are missing."],
  ["Use CORP/reliability analysis with event-clustered uncertainty only after an eligible locked forward sample exists."],
];
calibration.getRange("A17:H18").format = { fill: COLORS.paleAmber, font: { color: "#7A5200" }, wrapText: true };
calibration.freezePanes.freezeRows(4);
setColumnWidths(calibration, [13,10,10,9,9,13,13,12,3,13,16,14,3,3,3,3,3,3], 22);

// Issue register
addTitle(issues, "Issue Register and Corrective Controls", "Severity reflects whether the defect invalidates performance claims or can directly contaminate a forecast.", "F");
const issueRows = [
  ["S0","No immutable publication lock","No cutoff/model/data/source hashes in legacy ledger","Cannot prove outcome-blind probabilities","New snapshot/source-packet schema; legacy excluded","IMPLEMENTED IN SPEC"],
  ["S0","Complementary picks counted separately","150 exact pairs / 300 of 437 CSV rows; 37 four-pick cards are two pairs","Mechanical 2-2 cards distort hit rate","One decision per market; full branches stay candidates","IMPLEMENTED IN SPEC"],
  ["S0","No active validated models","No model cards or untouched forward tests for any sport-market-state","Numeric confidence was unsupported","Coverage registry defaults to UNSUPPORTED; PASS gate","SUSPENDED"],
  ["S0","Source-of-truth divergence","CSV 437, XLSX 449, narrative log later","Counts and statuses conflict","Single append-only stores and generated reports","REPLACED"],
  ["S0","No price/execution trail","No operator, quote time, stake, payout or commission","ROI, CLV and betting edge impossible","Separate price snapshot and execution entities","BLOCKED UNTIL DATA"],
  ["S0","Post-event field contamination","At least 60 legacy frequency bases contain final/settlement language","Leakage cannot be ruled out","Known-at temporal joins and immutable source packet","LEGACY QUARANTINE"],
  ["S1","Ranking inversion","Latest XLSX rank 1: 69-34; rank 4: 46-52; recent rank 4: 10-3","Old hierarchy did not separate outcomes","Retire ranks; evaluate one declared decision","RETIRED"],
  ["S1","Near-coin-flip largest market family","Phase/innings totals 131-126 with two pushes","No demonstrated directional edge","No active model; sport/market validation required","SUSPENDED"],
  ["S1","Penalty/exemption accounting","Flags mix card and row semantics","Bookkeeping not reproducible","Proper scores and versioned evaluation only","REMOVED"],
  ["S1","Manual probability buckets","Ten XLSX/CSV mismatches found","Calibration bins can be wrong","Derive display buckets from numeric p","CONTROL ADDED"],
  ["S1","Incomplete source citations","Zero legacy settlement_source cells contain HTTP URLs","Settlement cannot be reproduced efficiently","Direct official URL required for non-pending settlement","CONTROL ADDED"],
  ["S1","Fixed recency windows","Universal L5/L10/L15/L20 encouraged overlap and selection bias","Overfit and false completeness","Predeclared features inside chronological validation","REMOVED"],
  ["S1","Poisson misuse","Assumed rates, independence and simulation repeatability overstated certainty","Tail and dependence errors","Distribution diagnostics, sensitivity, MCSE, convergence","CONTROL ADDED"],
  ["S1","Current MLC under failure","MI New York 266/9; powerplay 100 after precise provisional unders","Recent pace/variance prior was badly wrong","Provisional numeric watchlists prohibited without active model","RECORDED / PARTIAL FINAL"],
  ["S2","Fragmented sport taxonomy","Many raw labels for the same family","Unsafe pooling and broken joins","Controlled sport/competition/market vocabularies","CONTROL ADDED"],
  ["S2","Unsupported sports implied covered","No meaningful ledger sample for NFL/NHL/NRL/tennis/golf","All-sport claims exceeded evidence","Per-scope coverage registry and expiry","CONTROL ADDED"],
];
issues.getRange("A4:F4").values = [["Severity","Issue","Evidence","Impact","Corrective control","Status"]];
styleHeader(issues.getRange("A4:F4"));
issues.getRange(`A5:F${4 + issueRows.length}`).values = issueRows;
styleBody(issues.getRange(`A5:F${4 + issueRows.length}`));
issues.getRange(`A5:F${4 + issueRows.length}`).format.wrapText = true;
issues.getRange(`A5:A${4 + issueRows.length}`).conditionalFormats.add("containsText", { text: "S0", format: { fill: COLORS.paleRed, font: { color: COLORS.red, bold: true } } });
issues.getRange(`A5:A${4 + issueRows.length}`).conditionalFormats.add("containsText", { text: "S1", format: { fill: COLORS.paleAmber, font: { color: "#7A5200", bold: true } } });
issues.tables.add(`A4:F${4 + issueRows.length}`, true, "IssueRegisterTable").style = "TableStyleMedium2";
issues.freezePanes.freezeRows(4);
setColumnWidths(issues, [10,27,45,38,45,22], 30);

// Source map
addTitle(sources, "Verified Primary Source Map", "High-level entry points verified during the 2026-07-16 sweep. Exact event pages, effective dates and point-in-time captures are still required per forecast.", "E");
const sourceRowsMap = [
  ["Australian football","AFL","Fixtures/results/rules","https://www.afl.com.au/fixture","Use official match centre/team sheet; variant rules by competition"],
  ["Baseball","MLB","Schedule, lineups, stats, rules","https://www.mlb.com/schedule","Gameday/gamebook controls; public StatsAPI is undocumented"],
  ["Baseball","NPB","Games, starters, registration","https://npb.jp/eng/","Clubs supply many injury facts"],
  ["Baseball","KBO","GameCenter and records","https://www.koreabaseball.com/Schedule/Schedule.aspx","MyKBO/Naver are secondary"],
  ["Basketball","NBA/WNBA","Schedule/stats/rules","https://official.nba.com/","Season-specific injury reports; Summer League separate"],
  ["Basketball","FIBA","Event reports/rules","https://about.fiba.basketball/en/services/resource-hub/downloads","2026 changes effective 2026-10-01; 2024 baseline until then"],
  ["Cricket","ICC/MCC","Fixtures, conditions, Laws","https://www.icc-cricket.com/about/cricket/rules-and-regulations/playing-conditions","MCC 2026 Laws effective 2026-10-01 unless adopted earlier"],
  ["Rugby league","NRL","Draw, stats, team lists","https://www.nrl.com/draw/","2026 final 19 at T-90m; verify actual 17 at kickoff"],
  ["Soccer","FIFA/IFAB","Match Centre and Laws","https://www.fifa.com/en/match-centre","Pair IFAB with exact competition regulations"],
  ["Ice hockey","NHL/IIHF","Schedule, Game Centre, official documents","https://www.nhl.com/schedule","Projected goalies remain projected until final evidence"],
  ["American football","NFL/NCAA","Schedule, inactives, rulebooks","https://www.nfl.com/inactives/","2026 NFL proposals are not the final rulebook"],
  ["Tennis","ATP/WTA/ITF/tournament","Draw/order/results/rules","https://www.atptour.com/en/corporate/rulebook","Entry does not prove fitness"],
  ["Golf","PGA Tour / major organiser","Field, tee times, leaderboard","https://www.pgatour.com/leaderboard","Major organiser controls its event"],
  ["Weather","Government service","Point forecast/nowcast","https://www.weather.gov/","Use jurisdiction authority and separate roof state"],
];
sources.getRange("A4:E4").values = [["Sport","Publisher","Fact classes","Entry URL","Critical qualification"]];
styleHeader(sources.getRange("A4:E4"));
sources.getRange(`A5:E${4 + sourceRowsMap.length}`).values = sourceRowsMap;
styleBody(sources.getRange(`A5:E${4 + sourceRowsMap.length}`));
sources.getRange(`C5:E${4 + sourceRowsMap.length}`).format.wrapText = true;
sources.tables.add(`A4:E${4 + sourceRowsMap.length}`, true, "SourceMapTable").style = "TableStyleMedium2";
sources.freezePanes.freezeRows(4);
setColumnWidths(sources, [23,22,30,58,48], 25);

// Raw manifest
addTitle(raw, "Raw JSON Manifest", "Unprovenanced workspace JSON is quarantined. It is not training, calibration or settlement evidence until event identity, cutoff, source URL, retrieval time and hash are established.", "F");
const jsonFiles = (await fs.readdir(root)).filter((f) => f.toLowerCase().endsWith(".json")).sort();
const manifest = [];
for (const file of jsonFiles) {
  const p = path.join(root, file);
  const st = await fs.stat(p);
  let keys = "";
  let parse = "OK";
  try {
    const obj = JSON.parse(await fs.readFile(p, "utf8"));
    keys = Array.isArray(obj) ? `array[${obj.length}]` : Object.keys(obj).slice(0, 12).join("; ");
  } catch (e) {
    parse = "PARSE ERROR";
    keys = String(e.message).slice(0, 100);
  }
  manifest.push([file, st.size, st.mtime.toISOString(), parse, keys, "QUARANTINED — provenance/cutoff/hash absent"]);
}
raw.getRange("A4:F4").values = [["File","Bytes","Modified UTC","Parse","Top-level shape/keys","Audit status"]];
styleHeader(raw.getRange("A4:F4"));
if (manifest.length) raw.getRange(`A5:F${4 + manifest.length}`).values = manifest;
styleBody(raw.getRange(`A5:F${4 + manifest.length}`));
raw.getRange(`E5:F${4 + manifest.length}`).format.wrapText = true;
raw.getRange(`C5:C${4 + manifest.length}`).format.numberFormat = "yyyy-mm-dd hh:mm";
raw.getRange(`F5:F${4 + manifest.length}`).format = { fill: COLORS.paleAmber, font: { color: "#7A5200", bold: true } };
raw.tables.add(`A4:F${4 + manifest.length}`, true, "RawManifestTable").style = "TableStyleMedium2";
raw.freezePanes.freezeRows(4);
setColumnWidths(raw, [28,13,25,14,55,42], 25);
raw.getRange(`A5:F${4 + manifest.length}`).format.autofitRows();

// Forward templates
addTitle(predictionTemplate, "Forward Request / Prediction Template", "A request row always exists. MODEL UNAVAILABLE or PASS must leave model/probability fields blank and state the reason. An ISSUE needs an ACTIVE in-scope model.", "D");
const predFields = [
  ["request_id","All","Unique immutable research request"],
  ["primary_question_id","All","Separates the user's primary question from secondary claims"],
  ["snapshot_id / prediction_id","All publications","New ID for every frozen publication"],
  ["forecast_series_id","All publications","Stable lineage across later snapshots"],
  ["parent_snapshot_id","Updates","Exact prior immutable snapshot"],
  ["selection_mode","All","USER_SUPPLIED | FIXED_UNIVERSE | MODEL_SELECTED"],
  ["candidate_universe_version","All","Version of the complete inspected market universe"],
  ["selection_policy_version","All","Eligibility/ranking/abstention policy frozen before results"],
  ["analysis_mode","All","RESEARCH_ONLY | PRICE_ENABLED"],
  ["forecast_state","All","PREGAME_PROJECTED | PREGAME_CONFIRMED | LIVE"],
  ["exact_horizon_or_state_bucket","All","Sport-native horizon and, for live, typed clock/exposure"],
  ["event_id / market_id","All","Official event identity and exact market definition"],
  ["event_start_utc","All","Official scheduled start at cutoff"],
  ["data_cutoff_utc / published_at_utc","All","Every source/feature known_at must be <= cutoff <= publication"],
  ["decision_status","All","MODEL_UNAVAILABLE | PASS | WATCH | ISSUE"],
  ["pass_reason / missing prerequisites","MODEL_UNAVAILABLE/PASS","Required; numeric probability language prohibited"],
  ["model_card_id / activation","ISSUE","Must join to ACTIVE exact sport/competition/market/state/horizon scope"],
  ["decision_probability","ISSUE/WATCH only if policy permits","Do not call calibrated without registered OOS calibration evidence"],
  ["outcome branches","Quantitative publication","One row per mutually exclusive WIN/LOSS/PUSH/VOID branch; reconcile"],
  ["uncertainty_artifact_id","ISSUE","Typed method, level, target, interval, scenarios and sensitivity"],
  ["source_packet_id / snapshot_hash","All publications","Point-in-time evidence and immutable record hash"],
  ["price_snapshot_id","PRICE_ENABLED only","Complete contemporaneous outcome prices and de-vig method"],
  ["expected_return","PRICE_ENABLED ISSUE","p_win*(d-1)-p_loss, net of commission; push/void zero profit"],
  ["invalidation_triggers","Quantitative publication","Facts/state changes requiring a new snapshot"],
];
predictionTemplate.getRange("A4:D4").values = [["Field","Required for","Rule","Example/value"]];
styleHeader(predictionTemplate.getRange("A4:D4"));
predictionTemplate.getRange(`A5:C${4 + predFields.length}`).values = predFields;
styleBody(predictionTemplate.getRange(`A5:D${4 + predFields.length}`));
predictionTemplate.getRange(`C5:D${4 + predFields.length}`).format.wrapText = true;
predictionTemplate.freezePanes.freezeRows(4);
setColumnWidths(predictionTemplate, [32,28,75,42], 35);

addTitle(settlementTemplate, "Append-only Settlement / Evaluation Template", "Settlement records facts only. A separate reproducible evaluation run calculates scores and eligibility against one immutable prediction snapshot.", "D");
const settleFields = [
  ["settlement_id","Settlement","Unique append-only version ID"],
  ["prediction_id / snapshot_id","Settlement","Exact frozen publication, never the series alone"],
  ["settlement_version / prior_id","Settlement","Corrections append and link; never overwrite"],
  ["official_event_status","Settlement","FINAL | POSTPONED | ABANDONED | SUSPENDED | CANCELLED | UNDER_REVIEW"],
  ["numeric_outcome / grade","Settlement","Exact state and WIN | LOSS | PUSH | VOID | UNGRADABLE | PENDING"],
  ["settlement_source_url","Non-pending settlement","Direct official gamebook/scorecard/result when available"],
  ["source_fetched_at_utc","Non-pending settlement","Verification time"],
  ["rules_applied","Settlement","Versioned settlement convention and exceptional branch"],
  ["evaluation_run_id","Evaluation","Versioned code, scoring spec, settlement version and eligible cohort"],
  ["eligible_for_v3_evaluation","Evaluation","Fails closed for legacy/unlocked/out-of-scope rows"],
  ["proper_score / baseline_delta","Evaluation","Brier/log/CRPS/RPS per versioned scoring convention"],
  ["cluster_id / effective_n","Evaluation","Event first; additional time/team blocks when justified"],
  ["execution_id","P&L/CLV only","Actual accepted transaction; otherwise P&L, yield and CLV prohibited"],
  ["correction_reason / reviewer","Correction","Required for settlement version > 1"],
];
settlementTemplate.getRange("A4:D4").values = [["Field","Entity","Rule","Example/value"]];
styleHeader(settlementTemplate.getRange("A4:D4"));
settlementTemplate.getRange(`A5:C${4 + settleFields.length}`).values = settleFields;
styleBody(settlementTemplate.getRange(`A5:D${4 + settleFields.length}`));
settlementTemplate.getRange(`C5:D${4 + settleFields.length}`).format.wrapText = true;
settlementTemplate.freezePanes.freezeRows(4);
setColumnWidths(settlementTemplate, [32,24,82,42], 25);

// Workbook-level verification and export
const summary = await wb.inspect({
  kind: "workbook,sheet,table,drawing",
  include: "id,name,values,formulas",
  maxChars: 20000,
  tableMaxRows: 6,
  tableMaxCols: 10,
  tableMaxCellChars: 100,
});
await fs.writeFile(`${outDir}/final_workbook_inspection.ndjson`, summary.ndjson, "utf8");

const errors = await wb.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 500 },
  summary: "final audit workbook formula-error scan",
});
await fs.writeFile(`${outDir}/final_workbook_formula_errors.ndjson`, errors.ndjson, "utf8");

const renderSpecs = [
  ["Read Me", "A1:H20"],
  ["Dashboard", "A1:P18"],
  ["Sport Summary", "A1:Q19"],
  ["Rank Summary", "A1:Q18"],
  ["Calibration", "A1:R20"],
  ["Issue Register", `A1:F${4 + issueRows.length}`],
  ["Legacy Audit", "A1:X28"],
  ["Legacy Audit", `A${Math.max(legacyStart, legacyEnd - 24)}:X${legacyEnd}`],
  ["Source Map", `A1:E${4 + sourceRowsMap.length}`],
  ["Raw Manifest", `A1:F${4 + manifest.length}`],
  ["Prediction Template", `A1:D${4 + predFields.length}`],
  ["Settlement Template", `A1:D${4 + settleFields.length}`],
];
for (let i = 0; i < renderSpecs.length; i++) {
  const [sheetName, range] = renderSpecs[i];
  const image = await wb.render({ sheetName, range, scale: 0.78, format: "png" });
  const safe = `${String(i + 1).padStart(2, "0")}_${sheetName.replace(/[^A-Za-z0-9]+/g, "_")}`;
  await fs.writeFile(`${previewDir}/${safe}.png`, new Uint8Array(await image.arrayBuffer()));
}

const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(outputPath);
console.log(JSON.stringify({ outputPath, legacyCsvPath, legacyRows: legacyRows.length, complementCards: complementCards.size, complementSelections: complementSelections.size, formulaErrors: errors.ndjson }));
