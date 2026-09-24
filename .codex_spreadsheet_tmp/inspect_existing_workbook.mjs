import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const root = "C:/Users/danie/Desktop/Sports Research";
const inputPath = `${root}/outputs/settlement_20260713/SPORTS_CALIBRATION_LEDGER_v2_settled.xlsx`;
const outputDir = `${root}/outputs/comprehensive_audit_20260716/pre_audit_workbook`;
await fs.mkdir(outputDir, { recursive: true });

const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(inputPath));
const summary = await workbook.inspect({
  kind: "workbook,sheet,table,drawing",
  include: "id,name,values,formulas",
  maxChars: 12000,
  tableMaxRows: 8,
  tableMaxCols: 12,
  tableMaxCellChars: 100,
});
await fs.writeFile(`${outputDir}/inspection.ndjson`, summary.ndjson, "utf8");
console.log(summary.ndjson);

for (const sheet of workbook.worksheets.items) {
  const safeName = sheet.name.replace(/[^A-Za-z0-9_-]+/g, "_");
  const ranges = ["A1:L30", "M1:X30", "Y1:AU30", "A420:L451", "Y420:AU451"];
  for (let i = 0; i < ranges.length; i += 1) {
    const preview = await workbook.render({
      sheetName: sheet.name,
      range: ranges[i],
      scale: 0.8,
      format: "png",
    });
    await fs.writeFile(`${outputDir}/${safeName}_${i + 1}.png`, new Uint8Array(await preview.arrayBuffer()));
  }
}

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "existing workbook formula error scan",
});
await fs.writeFile(`${outputDir}/formula_errors.ndjson`, errors.ndjson, "utf8");
console.log(errors.ndjson);
