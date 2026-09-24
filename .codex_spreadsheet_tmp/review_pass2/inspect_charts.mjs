import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const workspace = "C:/Users/danie/Desktop/Sports Research";
const workbookPath = path.join(
  workspace,
  "outputs/comprehensive_audit_20260716/SPORTS_RESEARCH_AUDIT_20260716.xlsx",
);
const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(workbookPath));

for (const sheetName of ["Sport Summary", "Rank Summary"]) {
  const sheet = workbook.worksheets.getItem(sheetName);
  console.log(`=== ${sheetName} ===`);
  console.log("used", sheet.getUsedRange().address);
  console.log("helper values", JSON.stringify(sheet.getRange("S4:T14").values));
  console.log("helper formulas", JSON.stringify(sheet.getRange("S4:T14").formulas));
  for (const chart of sheet.charts.items) {
    console.log(
      JSON.stringify(
        {
          chartName: chart.name,
          type: chart.type,
          title: chart.title,
          position: chart.position,
          series: chart.series.items.map((series) => ({
            name: series.name,
            categoryFormula: series.categoryFormula,
            formula: series.formula,
          })),
        },
        null,
        2,
      ),
    );
  }
  const styles = await workbook.inspect({
    kind: "computedStyle",
    sheetId: sheetName,
    range: "A4:I14",
    maxChars: 5000,
  });
  console.log(styles.ndjson);
}
