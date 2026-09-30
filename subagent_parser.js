async () => {
  const years = [
    { year: 1988, title: "1988 National Panasonic Cup", comp: "National Panasonic Cup" },
    { year: 1989, title: "1989 Panasonic Cup (Australian rules football)", comp: "Panasonic Cup" },
    { year: 1990, title: "1990 Foster's Cup", comp: "Foster's Cup" },
    { year: 1991, title: "1991 Foster's Cup", comp: "Foster's Cup" },
    { year: 1992, title: "1992 Foster's Cup", comp: "Foster's Cup" },
    { year: 1993, title: "1993 Foster's Cup", comp: "Foster's Cup" },
    { year: 1994, title: "1994 Foster's Cup", comp: "Foster's Cup" },
    { year: 1995, title: "1995 Ansett Australia Cup", comp: "Ansett Australia Cup" },
    { year: 1996, title: "1996 Ansett Australia Cup", comp: "Ansett Australia Cup" },
    { year: 1997, title: "1997 Ansett Australia Cup", comp: "Ansett Australia Cup" },
    { year: 1998, title: "1998 Ansett Australia Cup", comp: "Ansett Australia Cup" },
    { year: 1999, title: "1999 Ansett Australia Cup", comp: "Ansett Australia Cup" },
    { year: 2000, title: "2000 Ansett Australia Cup", comp: "Ansett Australia Cup" },
    { year: 2001, title: "2001 Ansett Australia Cup", comp: "Ansett Australia Cup" },
    { year: 2002, title: "2002 Wizard Home Loans Cup", comp: "Wizard Home Loans Cup" },
    { year: 2003, title: "2003 Wizard Home Loans Cup", comp: "Wizard Home Loans Cup" },
    { year: 2004, title: "2004 Wizard Home Loans Cup", comp: "Wizard Home Loans Cup" },
    { year: 2005, title: "2005 Wizard Home Loans Cup", comp: "Wizard Home Loans Cup" },
    { year: 2006, title: "2006 NAB Cup", comp: "NAB Cup" },
    { year: 2007, title: "2007 NAB Cup", comp: "NAB Cup" },
    { year: 2008, title: "2008 NAB Cup", comp: "NAB Cup" },
    { year: 2009, title: "2009 NAB Cup", comp: "NAB Cup" },
    { year: 2010, title: "2010 NAB Cup", comp: "NAB Cup" },
    { year: 2011, title: "2011 NAB Cup", comp: "NAB Cup" },
    { year: 2012, title: "2012 NAB Cup", comp: "NAB Cup" },
    { year: 2013, title: "2013 NAB Cup", comp: "NAB Cup" },
  ];

  const parseScore = (str) => {
    const scoreMatch = str.match(/(\d+\.\d+(?:\.\d+)?)\s*\((\d+)\)/);
    const teamName = str.replace(/(\d+\.\d+(?:\.\d+)?)\s*\((\d+)\)/, '').replace(/\[\[.*?\|(.*?)\]\]/g, '$1').replace(/[\[\]]/g, '').trim();
    if (!scoreMatch) return null;
    return {
      team: teamName,
      score: scoreMatch[1],
      points: parseInt(scoreMatch[2], 10),
      raw: scoreMatch[0]
    };
  };

  const results = {};
  for (const item of years) {
    const resp = await fetch(`https://en.wikipedia.org/w/api.php?action=parse&page=${encodeURIComponent(item.title)}&prop=text&format=json`);
    const d = await resp.json();
    const div = document.createElement("div");
    div.innerHTML = d.parse.text['*'];

    const matches = [];
    const tables = Array.from(div.querySelectorAll("table"));
    for (const table of tables) {
      let roundName = "";
      let prev = table.previousElementSibling;
      while (prev && !roundName) {
        if (/^H[2-5]$/i.test(prev.tagName)) roundName = prev.innerText.replace(/\[edit\]/g, '').trim();
        prev = prev.previousElementSibling;
      }

      const rows = Array.from(table.querySelectorAll("tr"));
      for (const row of rows) {
        const cells = Array.from(row.querySelectorAll("th, td")).map(c => c.innerText.trim());
        const defIdx = cells.findIndex(c => c === "def." || c === "def. by" || c === "drew with");

        if (defIdx > 0) {
          const dateStr = defIdx >= 2 ? cells[defIdx - 2] : "";
          const t1Obj = parseScore(cells[defIdx - 1]);
          const resultWord = cells[defIdx];
          const t2Obj = parseScore(cells[defIdx + 1]);
          const venueStr = cells[defIdx + 2] || "";
          const crowdMatch = venueStr.match(/crowd:\s*([\d,]+)/i);
          const crowd = crowdMatch ? crowdMatch[1].replace(/,/g, '') : null;
          const cleanVenue = venueStr.replace(/\s*\(crowd:.*?\)/i, '').trim();

          if (t1Obj && t2Obj) {
            matches.push({
              year: item.year,
              comp: item.comp,
              round: roundName,
              date: dateStr,
              t1: t1Obj.team,
              s1: t1Obj.raw,
              p1: t1Obj.points,
              res: resultWord,
              t2: t2Obj.team,
              s2: t2Obj.raw,
              p2: t2Obj.points,
              venue: cleanVenue,
              crowd: crowd ? parseInt(crowd, 10) : null
            });
          }
        } else if (cells.length >= 6 && cells[1].includes("(") && cells[3].includes("(")) {
          const winTeam = cells[0];
          const winScoreObj = parseScore(cells[1]);
          const loseTeam = cells[2];
          const loseScoreObj = parseScore(cells[3]);
          const ground = cells[4] || "";
          const crowd = cells[5] ? parseInt(cells[5].replace(/[^\d]/g, ''), 10) || null : null;
          const dateStr = cells[6] || "";

          if (winScoreObj && loseScoreObj) {
            matches.push({
              year: item.year,
              comp: item.comp,
              round: roundName,
              date: dateStr,
              t1: winTeam,
              s1: winScoreObj.raw,
              p1: winScoreObj.points,
              res: "def.",
              t2: loseTeam,
              s2: loseScoreObj.raw,
              p2: loseScoreObj.points,
              venue: ground,
              crowd: crowd
            });
          }
        }
      }
    }
    results[item.year] = { count: matches.length, sample: matches.slice(0, 1) };
  }

  return results;
}