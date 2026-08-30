import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";
const p = "C:/Users/danie/Desktop/Sports Research/outputs/settlement_20260713/SPORTS_CALIBRATION_LEDGER_v2_settled.xlsx";
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(p));
const ws = wb.worksheets.getItem("Calibration Ledger");
const vals = ws.getRange("A1:AU4").values;
console.log(JSON.stringify(vals));
