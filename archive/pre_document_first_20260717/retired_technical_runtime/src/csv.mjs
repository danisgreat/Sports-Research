export function parseCsv(text) {
  text = text.replace(/^\uFEFF/, '');
  const rows = [];
  let row = [];
  let field = '';
  let quoted = false;
  let afterQuote = false;

  for (let index = 0; index < text.length; index += 1) {
    const character = text[index];
    if (quoted) {
      if (character === '"' && text[index + 1] === '"') {
        field += '"';
        index += 1;
      } else if (character === '"') {
        quoted = false;
        afterQuote = true;
      } else {
        field += character;
      }
      continue;
    }

    if (afterQuote && ![',', '\r', '\n'].includes(character)) throw new Error('unexpected text after closing CSV quote');
    if (character === '"') {
      if (field.length > 0 || afterQuote) throw new Error('quote inside unquoted CSV field');
      quoted = true;
    } else if (character === ',') {
      row.push(field);
      field = '';
      afterQuote = false;
    } else if (character === '\n') {
      row.push(field.replace(/\r$/, ''));
      rows.push(row);
      row = [];
      field = '';
      afterQuote = false;
    } else if (character === '\r' && afterQuote) {
      // Allowed only as the CR of CRLF; the following LF closes the row.
      if (text[index + 1] !== '\n') throw new Error('bare CR after quoted CSV field');
    } else {
      field += character;
    }
  }

  if (quoted) throw new Error('unterminated quoted CSV field');
  if (field.length > 0 || row.length > 0) {
    row.push(field.replace(/\r$/, ''));
    rows.push(row);
  }

  if (rows.some((candidate) => candidate.every((value) => value === ''))) throw new Error('blank CSV row is not allowed in a machine control');
  if (rows.length === 0) return [];
  const header = rows[0];
  if (new Set(header).size !== header.length) throw new Error('duplicate CSV header');
  return rows.slice(1).map((values, rowIndex) => {
    if (values.length !== header.length) {
      throw new Error(`CSV row ${rowIndex + 2} has ${values.length} fields; expected ${header.length}`);
    }
    return Object.fromEntries(header.map((name, index) => [name, values[index]]));
  });
}

export function quoteCsv(value) {
  if (value === null || value === undefined) return '';
  const text = String(value);
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

export function stringifyCsv(rows, columns) {
  const output = [columns.map(quoteCsv).join(',')];
  for (const row of rows) output.push(columns.map((column) => quoteCsv(row[column])).join(','));
  return `${output.join('\r\n')}\r\n`;
}
