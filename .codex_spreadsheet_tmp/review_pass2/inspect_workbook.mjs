import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const workspace = "C:/Users/danie/Desktop/Sports Research";
const workbookPath = path.join(
  workspace,
  "outputs/comprehensive_audit_20260716/SPORTS_RESEARCH_AUDIT_20260716.xlsx",
);
const renderDir = path.join(
  workspace,
  ".codex_spreadsheet_tmp/review_pass2/renders",
);

await fs.mkdir(renderDir, { recursive: true });
const input = await FileBlob.load(workbookPath);
const workbook = await SpreadsheetFile.importXlsx(input);

const summary = await workbook.inspect({
  kind: "workbook,sheet,table,drawing",
  maxChars: 12000,
  tableMaxRows: 5,
  tableMaxCols: 8,
  tableMaxCellChars: 80,
});
console.log("=== SUMMARY ===");
console.log(summary.ndjson);

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "formula error scan",
  maxChars: 8000,
});
console.log("=== FORMULA ERRORS ===");
console.log(errors.ndjson);

const renderResults = [];
for (const sheet of workbook.worksheets.items) {
  const safeName = sheet.name.replace(/[^A-Za-z0-9_-]+/g, "_");
  const outputPath = path.join(renderDir, `${safeName}.png`);
  const preview = await workbook.render({
    sheetName: sheet.name,
    autoCrop: "all",
    scale: 1,
    format: "png",
  });
  await fs.writeFile(outputPath, new Uint8Array(await preview.arrayBuffer()));
  renderResults.push({ sheet: sheet.name, outputPath });
}
console.log("=== RENDERS ===");
console.log(JSON.stringify(renderResults, null, 2));
