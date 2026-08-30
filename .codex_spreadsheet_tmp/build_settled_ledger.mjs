import fs from "node:fs/promises";
import { Workbook, SpreadsheetFile } from "@oai/artifact-tool";

const root = "C:/Users/danie/Desktop/Sports Research";
const csvText = await fs.readFile(`${root}/SPORTS_CALIBRATION_LEDGER_v2.csv`, "utf8");
const workbook = await Workbook.fromCSV(csvText, { sheetName: "Calibration Ledger" });
const sheet = workbook.worksheets.getItem("Calibration Ledger");
const used = sheet.getUsedRange(true);
const values = used.values;
const headers = values[0].map((v) => String(v).replace(/^\uFEFF/, ""));
const startRow = values.length;

const base = {
  date: "2026-07-13",
  governing_body: "Official league",
  press_signal_class: "NONE/UNKNOWN",
  press_signal_quote_logged: false,
  source_confidence_score: 5,
  ruleset_error: false,
  availability_or_eligibility_error: false,
  settlement_convention_error: false,
  source_status_error: false,
};

const specs = [];
function addCard(common, picks) {
  for (const p of picks) specs.push({ ...base, ...common, ...p });
}

addCard({
  card_id: "MLB-20260713-MIL-PIT",
  sport: "MLB",
  match: "Milwaukee Brewers @ Pittsburgh Pirates",
  competition: "MLB regular season",
  governing_body: "MLB",
  rulebook_or_playing_conditions: "2026 MLB Official Baseball Rules",
  settlement_convention: "Full game including extras; +1.5 run line; 8.5 total",
  market_group: "Both +1.5 run lines and total 8.5",
  frequency_count_base: "MIL/PIT L5-L20 plus starter and bullpen workloads",
  projection_band: "PIT 4-3 / 5-3; total centre 8.3",
  settlement_source: "https://statsapi.mlb.com/api/v1.1/game/823358/feed/live",
  phase_source: "MLB official inning and box-score feed",
  form_delta_verdict: "Gasser short-window improvement refuted; Pittsburgh high-total windows confirmed",
  form_anchor_window: "L5/L10/L15/L20 plus starter L5",
  officials_named: "Alfonso Marquez",
  officials_source_timestamp: "MLB Gameday pregame 2026-07-13 AEST",
  source_disagreement_note: "No final-score disagreement",
  similar_condition_form: "Split-doubleheader aftermath and replacement starter",
  role_replacement_bench_verdict: "Replacement starter and early bridge failed",
  style_fit_note: "Pittsburgh damage was asymmetric against MIL staff",
  volatility_stability_note: "Early bridge variance materially understated",
  prediction_triggers: "Gasser early exit; thinned fourth-to-sixth bridge; Pittsburgh rolling scoring",
}, [
  { rank: 1, option: "Pirates +1.5", stated_probability_bucket: "70-79", stated_probability: 0.73, line_or_threshold: "+1.5", result: "Pittsburgh 14 Milwaukee 5", win_loss_push: "W", top_pick_loss: false, bottom_pick_win: false, top_half_sweep_exemption: false, penalty_applied: false, projection_error: false, rank_slot_calibration_error: false, notes: "Top side and winner direction correct." },
  { rank: 2, option: "Brewers +1.5", stated_probability_bucket: "60-69", stated_probability: 0.66, line_or_threshold: "+1.5", result: "Milwaukee lost by 9", win_loss_push: "L", top_pick_loss: false, bottom_pick_win: false, top_half_sweep_exemption: false, penalty_applied: false, projection_error: true, rank_slot_calibration_error: true, notes: "Asymmetric starter/bridge collapse destroyed cushion." },
  { rank: 3, option: "Combined Total Under 8.5", stated_probability_bucket: "50-59", stated_probability: 0.54, line_or_threshold: "8.5", result: "Total 19", win_loss_push: "L", top_pick_loss: false, bottom_pick_win: false, top_half_sweep_exemption: false, penalty_applied: false, projection_error: true, rank_slot_calibration_error: true, notes: "Recent Gasser ERA overweighted versus staff-failure paths." },
  { rank: 4, option: "Combined Total Over 8.5", stated_probability_bucket: "40-49", stated_probability: 0.46, line_or_threshold: "8.5", result: "Total 19", win_loss_push: "W", top_pick_loss: false, bottom_pick_win: true, top_half_sweep_exemption: false, penalty_applied: true, projection_error: true, rank_slot_calibration_error: true, notes: "Bottom-slot leak; Pittsburgh scored 14 after Gasser and Koenig collapse." },
]);

addCard({
  card_id: "MLB-20260713-HOU-TEX",
  sport: "MLB",
  match: "Houston Astros @ Texas Rangers",
  competition: "MLB regular season",
  governing_body: "MLB",
  rulebook_or_playing_conditions: "2026 MLB Official Baseball Rules",
  settlement_convention: "Full game including extras; total 9.0 pushes exactly nine",
  market_group: "Astros +1.5, Rangers ML and total 9.0",
  frequency_count_base: "HOU/TEX L5-L20 plus starter-role and bullpen workloads",
  projection_band: "TEX 5-4 / 6-4; total centre 9.6",
  settlement_source: "https://statsapi.mlb.com/api/v1.1/game/822876/feed/live",
  phase_source: "MLB official inning and box-score feed",
  form_delta_verdict: "Short-start and high-total mechanisms confirmed",
  form_anchor_window: "L5/L10/L15/L20 plus current pitcher role",
  officials_named: "Adrian Johnson",
  officials_source_timestamp: "MLB Gameday pregame 2026-07-13 AEST",
  source_disagreement_note: "No final-score disagreement",
  similar_condition_form: "Closed-roof short-start/bullpen game",
  role_replacement_bench_verdict: "Javier correctly treated as short starter",
  style_fit_note: "One-run corridor supported cushion and home winner",
  volatility_stability_note: "Bullpen tail correctly elevated",
  prediction_triggers: "Javier workload; Gore length; bullpen exposure; whole-number push",
}, [
  { rank: 1, option: "Astros +1.5", stated_probability_bucket: "60-69", stated_probability: 0.64, line_or_threshold: "+1.5", result: "Texas 6 Houston 5", win_loss_push: "W", top_pick_loss: false, bottom_pick_win: false, top_half_sweep_exemption: true, penalty_applied: false, projection_error: false, rank_slot_calibration_error: false, notes: "Houston stayed inside one run." },
  { rank: 2, option: "Combined Total Over 9.0", stated_probability_bucket: "40-49", stated_probability: 0.49, line_or_threshold: "9.0", result: "Total 11", win_loss_push: "W", top_pick_loss: false, bottom_pick_win: false, top_half_sweep_exemption: true, penalty_applied: false, projection_error: false, rank_slot_calibration_error: false, notes: "Short starts and bullpen innings produced 11." },
  { rank: 3, option: "Rangers ML", stated_probability_bucket: "50-59", stated_probability: 0.55, line_or_threshold: "ML", result: "Texas won 6-5", win_loss_push: "W", top_pick_loss: false, bottom_pick_win: false, top_half_sweep_exemption: true, penalty_applied: false, projection_error: false, rank_slot_calibration_error: false, notes: "Nimmo walk-off; winner lean correct." },
  { rank: 4, option: "Combined Total Under 9.0", stated_probability_bucket: "30-39", stated_probability: 0.38, line_or_threshold: "9.0", result: "Total 11", win_loss_push: "L", top_pick_loss: false, bottom_pick_win: false, top_half_sweep_exemption: true, penalty_applied: false, projection_error: false, rank_slot_calibration_error: false, notes: "Expected bottom loss; no penalty." },
]);

addCard({
  card_id: "WNBA-20260713-SEA-WAS-LIVE",
  sport: "WNBA",
  match: "Seattle Storm @ Washington Mystics",
  competition: "WNBA regular season",
  governing_body: "WNBA",
  rulebook_or_playing_conditions: "2026 WNBA rules; four 10-minute quarters",
  settlement_convention: "Q1 and 1H regulation phases; full game includes OT; Q1 41 pushes exactly 41",
  market_group: "Live-start Q1 41.0, 1H 83.5 and full 162.5",
  frequency_count_base: "Both teams L5/L10/L15/L20 phase totals and 2026 H2H",
  projection_band: "Q1 44-47; half 80-86; full 156-164",
  settlement_source: "https://site.api.espn.com/apis/site/v2/sports/basketball/wnba/summary?event=401857061",
  phase_source: "ESPN/WNBA official quarter splits",
  form_delta_verdict: "Seattle 1H Over window should have controlled after fast live start",
  form_anchor_window: "Live 10-4 at 7:26 Q1 plus both-team L5-L20",
  officials_named: "Angelica Suffren; Marcy Williams; Tyler Mirkovich",
  officials_source_timestamp: "ESPN game feed 2026-07-13 AEST",
  source_disagreement_note: "ESPN and WNBA final agreed",
  similar_condition_form: "Live fast-Q1 state",
  role_replacement_bench_verdict: "Magbegor/Mair out; no new settlement availability issue",
  style_fit_note: "Fast first three quarters, slow Q4",
  volatility_stability_note: "Half/full half-point margins; correct-but-fragile Q1 Over",
  prediction_triggers: "14 points in 2:34; Q2 requirement; Seattle L5 1H Over 4/5",
}, [
  { rank: 1, option: "Q1 Over 41.0", stated_probability_bucket: "70-79", stated_probability: 0.72, line_or_threshold: "41.0", result: "Q1 total 42", win_loss_push: "W", top_pick_loss: false, bottom_pick_win: false, top_half_sweep_exemption: false, penalty_applied: false, projection_error: false, rank_slot_calibration_error: false, notes: "Won by one; correct but fragile." },
  { rank: 2, option: "Full Game Under 162.5", stated_probability_bucket: "50-59", stated_probability: 0.55, line_or_threshold: "162.5", result: "Full total 163", win_loss_push: "L", top_pick_loss: false, bottom_pick_win: false, top_half_sweep_exemption: false, penalty_applied: false, projection_error: true, rank_slot_calibration_error: true, notes: "Lost by 0.5; Q3 total 47 offset Q4 total 31." },
  { rank: 3, option: "First Half Under 83.5", stated_probability_bucket: "50-59", stated_probability: 0.53, line_or_threshold: "83.5", result: "Halftime total 85", win_loss_push: "L", top_pick_loss: false, bottom_pick_win: false, top_half_sweep_exemption: false, penalty_applied: false, projection_error: true, rank_slot_calibration_error: true, notes: "Failed to propagate elevated Q1 projection into half." },
  { rank: 4, option: "First Half Over 83.5", stated_probability_bucket: "40-49", stated_probability: 0.48, line_or_threshold: "83.5", result: "Halftime total 85", win_loss_push: "W", top_pick_loss: false, bottom_pick_win: true, top_half_sweep_exemption: false, penalty_applied: true, projection_error: true, rank_slot_calibration_error: true, notes: "Should have ranked above Under after live start and SEA L5 4/5 Over." },
]);

const rows = specs.map((obj) => headers.map((h) => obj[h] ?? ""));
sheet.getRangeByIndexes(startRow, 0, rows.length, headers.length).values = rows;
sheet.freezePanes.freezeRows(1);
sheet.showGridLines = false;
sheet.getRangeByIndexes(0, 0, 1, headers.length).format = {
  fill: "#0F4C5C",
  font: { bold: true, color: "#FFFFFF" },
  wrapText: true,
};
sheet.getRangeByIndexes(0, 0, startRow + rows.length, headers.length).format.autofitColumns();
sheet.getRangeByIndexes(0, 0, startRow + rows.length, headers.length).format.columnWidth = 18;
sheet.getRangeByIndexes(0, 0, startRow + rows.length, headers.length).format.wrapText = true;
sheet.getRangeByIndexes(0, 0, startRow + rows.length, 1).format.columnWidth = 27;
sheet.getRangeByIndexes(0, 1, startRow + rows.length, 1).format.columnWidth = 12;
sheet.getRangeByIndexes(0, 2, startRow + rows.length, 1).format.columnWidth = 10;
sheet.getRangeByIndexes(0, 3, startRow + rows.length, 1).format.columnWidth = 34;
sheet.getRangeByIndexes(0, 4, startRow + rows.length, 1).format.columnWidth = 21;
sheet.getRangeByIndexes(0, 5, startRow + rows.length, 1).format.columnWidth = 12;
sheet.getRangeByIndexes(0, 6, startRow + rows.length, 1).format.columnWidth = 30;
sheet.getRangeByIndexes(0, 7, startRow + rows.length, 1).format.columnWidth = 40;
sheet.getRangeByIndexes(0, 8, startRow + rows.length, 1).format.columnWidth = 34;
sheet.getRangeByIndexes(0, 10, startRow + rows.length, 1).format.columnWidth = 28;
sheet.getRangeByIndexes(0, 13, startRow + rows.length, 1).format.columnWidth = 34;
sheet.getRangeByIndexes(0, 14, startRow + rows.length, 1).format.columnWidth = 28;
sheet.getRangeByIndexes(0, 16, startRow + rows.length, 1).format.columnWidth = 28;
sheet.getRangeByIndexes(0, 28, startRow + rows.length, 1).format.columnWidth = 46;
sheet.getRangeByIndexes(0, 29, startRow + rows.length, 1).format.columnWidth = 36;
sheet.getRangeByIndexes(0, 30, startRow + rows.length, 1).format.columnWidth = 46;
sheet.getRangeByIndexes(startRow, 0, rows.length, headers.length).format.autofitRows();

const outcomeCol = headers.indexOf("win_loss_push");
if (outcomeCol >= 0) {
  const outcomeRange = sheet.getRangeByIndexes(1, outcomeCol, startRow + rows.length - 1, 1);
  outcomeRange.conditionalFormats.add("containsText", { text: "W", format: { fill: "#DCFCE7", font: { color: "#166534", bold: true } } });
  outcomeRange.conditionalFormats.add("containsText", { text: "L", format: { fill: "#FEE2E2", font: { color: "#991B1B", bold: true } } });
}

const inspection = await workbook.inspect({
  kind: "table",
  range: `Calibration Ledger!A${startRow + 1}:AT${startRow + rows.length}`,
  include: "values,formulas",
  tableMaxRows: 15,
  tableMaxCols: 46,
  maxChars: 10000,
});
console.log(inspection.ndjson);
const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 100 },
  summary: "formula error scan",
});
console.log(errors.ndjson);

const preview = await workbook.render({
  sheetName: "Calibration Ledger",
  range: `A${startRow + 1}:H${startRow + rows.length}`,
  scale: 1,
  format: "png",
});
await fs.writeFile(`${root}/outputs/settlement_20260713/calibration_preview.png`, new Uint8Array(await preview.arrayBuffer()));
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(`${root}/outputs/settlement_20260713/SPORTS_CALIBRATION_LEDGER_v2_settled.xlsx`);
