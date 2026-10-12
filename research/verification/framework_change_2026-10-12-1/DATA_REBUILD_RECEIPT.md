# Data rebuild receipt — Czech and English top flights (audit R01–R07)

Executed 2026-10-12, 12:55–13:25 AEDT (UTC+11), base `eb1acf58b`. This file records what was done to the data, how, and what was checked. The per-field rules and the use rules are in each archive folder's `DATA_PROVENANCE.md` ([hockey](../../../Previous%20Sports%20Results/Ice%20Hockey/Czech%20Extraliga/DATA_PROVENANCE.md), [football](../../../Previous%20Sports%20Results/Soccer/Premier%20League/DATA_PROVENANCE.md)).

## 1. Containment (R01–R03, R06, R07)

**Preserved first, then moved out of the repository.** Destination: `C:\Users\danie\Desktop\Sports Research LOCAL_QUARANTINE_2026-10-12\`, a sibling of the repository folder. Its README lists the contents.

| Step | Evidence |
|---|---|
| `git status --porcelain` before any change | `git_status_before.txt`: 107 modified, 12 untracked |
| Full `git diff` of the modified tracked files | `tracked_modifications.patch`, 23,488,191 bytes |
| Byte copies of the 107 modified tracked files | `working_tree_copy/`, 107 files |
| Untracked local-only material moved (not deleted) | Two root export folders, two alias trees, four generated roster/venue .md, `research/src/` (16 .py plus caches), `research/data/czech_extraliga/` (51 .htm) and `research/data/premier_league/` (2 CSV plus 33 football-data CSV): 320 files in all |
| Tracked documents restored to base | `SOURCES.md` and the four roster/venue .md files restored from HEAD. The local SOURCES §3.34/§3.35 text is kept in `SOURCES_local_sections.patch` |
| Not moved | `AUDIT_RECOMMENDATIONS_2026-10-12.txt` (the user's audit, left in place; a copy is in this folder) |

**Faults confirmed by reading the quarantined builders:**
- **Hockey:** default date `{season}-09-15` / "Friday" when no date parsed; start time "17:30"; attendance "5,420" / "4,800"; a generic referee text; periods estimated as score ÷ 3 when absent; period 3 adjusted until the sum matched; a +1 overtime or shootout goal invented when no extra pair was printed.
- **Football:** half-time = full-time ÷ 2 when absent (1975–95 and the play-offs); kick-off "15:00", referee and attendance defaults ("38,500", "28,400", "25,000"); matchweek = row number ÷ 10 or 11; a hand-typed 51-row Community Shield table with scorers.
- **Both:** three identical output copies, and IDs built from row numbers.

**Additional parsing faults found in the quarantined hockey output** (season row counts against this rebuild):
- 1980-81 and 1981-82: 271 and 300 "Regular Season" rows against 264. Cup games were typed as league games.
- 2001-02: 603 rows against 405. Second-tier games leaked in.
- 2020-21: 371 regular-season games typed "Finals".
- 1983-84 and 1984-85: the promotion series is missing.

The quarantined football output had 20,791 rows. That is the 20,740 games rebuilt here plus 51 Community Shield rows, so its defects were in the field values, not the row set.

## 2. Rebuild (how it was executed)

The rebuild read the cached source files in the quarantine folder. They were **not** re-fetched; their capture times are about 02:05 AEDT for hockey and 02:24 AEDT for football.

The transformation was run with two short Python scripts in this session's temporary scratchpad, **outside the repository**. The repository stays Markdown/CSV/text only (CONTRIBUTING, CURRENT_RULES §0, R07). The scripts are not committed. Their complete rules are written out in prose in the two `DATA_PROVENANCE.md` files, field by field, so that the transformation can be reproduced or reviewed by hand from the source pages. Outputs were written as UTF-8 with LF line endings to the canonical paths only, matching the placeholder files they replaced.

**Iterations, disclosed:**

| Iteration | Change | Outcome |
|---|---|---|
| Hockey run 1 | Sections split at every anchor | Dropped the games after the inline anchors `Dresde` (2019-20) and `Shcherbak` (2022-23), giving 35 regular-season rows in 2022-23. Found by the per-season count check |
| Hockey run 2 | Inline anchors merged; `promrel`/`com`/`q` mapped | Correct counts |
| Hockey run 3 | Stop guard "I. liga" applied | Removed 1975–1990, where "I. liga" is the top flight. The guard was restricted to 1993 onward |
| Hockey run 3 (same step) | Removed a guessed "tie after OT in shootout era" check | It rested on an unsourced claim about when shootouts began |
| Hockey runs 4–5 | Combined date-and-venue brackets, `(le …)` and `(weekday d month)` notes, `*` and `K` markers, awards, forfeits, abandonment, malformed text handled | Duplicate-listing diagnostic added |
| Football run 1 | One game had no matching cross-check row | Found to be the 17 May 2016 postponement. A same-fixture fallback now reports `AGREE_SCORE_DATE_DIFFERS` |
| Both | A `lineterminator` edit through the shell inserted a literal newline into the scripts (the known shell-quoting trap) | Both scripts failed to start, so nothing was written. Fixed with the file editor and rerun |

## 3. Results

| Check | Hockey | Football |
|---|---|---|
| Seasons / rows | 51 / 18,752 | 51 / 20,740 (20,732 league + 8 play-off) |
| Duplicate IDs | 0 | 0 |
| Date filled | 16,909 (1,843 play-off/relegation games undated: round date lists only) | 20,740 |
| Date ↔ weekday disagreements | 0 | 0 |
| Quarantined default values present | 0 rows with start time, attendance or referee. 74 genuine 15 September dates (against 16,242) | 0 Community Shield rows, 0 odds columns, 0 default kick-offs or attendances |
| League-size check | Regular-season games per team equal in every season except the five documented source defects | Correct club count and equal games per club in all 51 seasons |
| Two-compiler cross-check | n/a (single compiler) | 11,943 of 11,944 agree on date and score (1993-94 to 2024-25, excluding 2022-23); 1 agrees on score with a 1-day date difference |
| External sample | 8 of 8: Czech Wikipedia 2023-24 play-offs | 9 of 9: ESPN site API, 2025-08-15, 2016-05-17, 2010-10-16 |
| Flagged rows | 145 (see DATA_PROVENANCE §4) | 9 (8 play-off labels, 1 date difference) |

## 4. Source fingerprints

**Hockey pages** (captured HTML):

| Season | Page | Bytes | SHA-256 |
|---|---|---:|---|
| 1975-76 | `Tchecoslovaquie1976.htm` | 30517 | `360420cd6c2d1c399a3aace8ba4c89032237d1c481716d62ce4e81584571afc8` |
| 1976-77 | `Tchecoslovaquie1977.htm` | 30587 | `df0ae6b3920fa6d22f8142b203dc6f13873e7b5449aabad14c3000f7a13ce6d0` |
| 1977-78 | `Tchecoslovaquie1978.htm` | 28735 | `623badca2a3bfc3ce369bc79d9e02db4ddac9137efede5e9f150eabfb36ed11c` |
| 1978-79 | `Tchecoslovaquie1979.htm` | 27556 | `78902e17e6b883a9d048fbc7c034746b8fd4df0509c4b9145541c9d32f0b0d23` |
| 1979-80 | `Tchecoslovaquie1980.htm` | 29066 | `a4773191b1e165ae8764764cca29d299125facb32461627a43f4693c3328a45c` |
| 1980-81 | `Tchecoslovaquie1981.htm` | 31787 | `9ce1186f303dfd4e9a0ceac65cb3811b93e8ee7eb880dedee63331d9acf06b3f` |
| 1981-82 | `Tchecoslovaquie1982.htm` | 30736 | `dcda6f989a7d0331c9466a5838408e43b613ae8d121c6bcdaa476a28f2100da7` |
| 1982-83 | `Tchecoslovaquie1983.htm` | 35956 | `0ea7cef09811465505bb722dde1aa3ff050af3a5f48e7098f2bf6969b9aff013` |
| 1983-84 | `Tchecoslovaquie1984.htm` | 34826 | `9adf46a6b5fbc02fda40204f947c1b8216f2b3bece156c4f629acfc9754f8482` |
| 1984-85 | `Tchecoslovaquie1985.htm` | 45512 | `97d948f437de7c51d184dca1dbd08b99ba27d7f063bdb29ce14f4b9c9ef9b011` |
| 1985-86 | `Tchecoslovaquie1986.htm` | 40029 | `2bddedb8eeb2f75cf24f38e3058972038cf78969f51cd9923f31498163009c6e` |
| 1986-87 | `Tchecoslovaquie1987.htm` | 32120 | `c99c391793cb86e5802f301a6bd61070779003e6402f2c1683fa22755e091c2b` |
| 1987-88 | `Tchecoslovaquie1988.htm` | 37626 | `adbbeda19866449c2325c0ccd5fc2056bd1c89413a8f5e3f1807e1e85873c2f2` |
| 1988-89 | `Tchecoslovaquie1989.htm` | 38650 | `a32e93ec5db2bec4e9322271234cfdefca85cfba35b951ce0fa5f85784ba7c88` |
| 1989-90 | `Tchecoslovaquie1990.htm` | 39323 | `1bc9bfda5de97e4d8a9167679ffe130cf49ebebdf2363381ba205b965d9194a0` |
| 1990-91 | `Tchecoslovaquie1991.htm` | 38038 | `a6cadb7a3f30672ab41e2881a355dad2ce308d826dc37cab931f3090ea4a7283` |
| 1991-92 | `Tchecoslovaquie1992.htm` | 34434 | `68e6ed054a1a33ca23e4cf7f92a24a12566ab7c46207810f719ee7087f9f1bd0` |
| 1992-93 | `Tchecoslovaquie1993.htm` | 47343 | `95b40c90145eb88777f2d063ea340f85ec840897908bb0f5b0d6034d3a8f0491` |
| 1993-94 | `Tcheque1994.htm` | 52848 | `3f9059c845bf42f72150fd9768ee46599057c9284f4c6f77d0a3c1db684f0ab9` |
| 1994-95 | `Tcheque1995.htm` | 70672 | `7a4141ae18c6a23cbeabf00314b1dd12b98c6eece404976a2d2b85e8bb48c1a7` |
| 1995-96 | `Tcheque1996.htm` | 37202 | `c3c27d4cc65443cc719c9467ff24af0df0590bafed4c90d467b194b3c5fe4641` |
| 1996-97 | `Tcheque1997.htm` | 50691 | `0421458bab4c7971554cf168d1a1b7226180177a231709e4ace99afd8ce4b003` |
| 1997-98 | `Tcheque1998.htm` | 46327 | `22cdb3515f3200bf8906f651d961308241131f5ceab5cd654653d9a19ef34180` |
| 1998-99 | `Tcheque1999.htm` | 73887 | `9565126c4e88e0eb7de3d7033d225d4309f14f4cfb412179a8bc9924cd5d6b30` |
| 1999-00 | `Tcheque2000.htm` | 58683 | `266aa037821e00de9a87cc857df57fb079bd6d42e3b36dfaba767eef3a65dca2` |
| 2000-01 | `Tcheque2001.htm` | 62894 | `2d9032fa8b547ed260ef8db972e51ec674b418c5cbbcda9d466a441bd1688a2f` |
| 2001-02 | `Tcheque2002.htm` | 56700 | `9558094f42b1b3fd582b458ab3d802e522610c078ee714a78c1bdc08acae0f09` |
| 2002-03 | `Tcheque2003.htm` | 56051 | `1790b47cd43e508ee04b79f5e7ce8cfebff403e5868af12c939ddb8c021ed91a` |
| 2003-04 | `Tcheque2004.htm` | 84503 | `2d8a0bce5a175f33cffb79f3802d56e9703ca3d7bf2d990a0f8e93f72162d2af` |
| 2004-05 | `Tcheque2005.htm` | 153538 | `397824f9e9978b211121981a1f21c30ea8b761691cce126d3e2f303f4db70eb5` |
| 2005-06 | `Tcheque2006.htm` | 143467 | `ea2f4f08a37da7f2e7698c8f6cf64d7ab3c2d1f4dee4949872503adc7aa382f8` |
| 2006-07 | `Tcheque2007.htm` | 148176 | `a698b462dba585629a3ace414a76a2f619945fcc0717eb781969c7ee7beea438` |
| 2007-08 | `Tcheque2008.htm` | 120769 | `75004f9a397d5b9ffc3753979e82ada8ab985d9d70838bbf5e86d61675fb6d86` |
| 2008-09 | `Tcheque2009.htm` | 113781 | `20b62c0cb6390fec99aedcadb9bb7b3644d77bb0f03651213f8a3d4174f820cb` |
| 2009-10 | `Tcheque2010.htm` | 102932 | `683552343bc92b192747dba87d8e8341328075b1305d57f5cc3483048c2164b5` |
| 2010-11 | `Tcheque2011.htm` | 106643 | `996c5ac37dd130b62a39124c17fe092dbf4d35af153b42b07cc3557ac22dcdc2` |
| 2011-12 | `Tcheque2012.htm` | 96426 | `c4f93edcfeeb910b88b73340880233a7281e42d417b6cdac9f3ebe2ec5c7258b` |
| 2012-13 | `Tcheque2013.htm` | 102995 | `3ad0a11b30123319be6b3f1fe8b7055deb359dfcbaf7af3c08bbb0ed6844c2b2` |
| 2013-14 | `Tcheque2014.htm` | 96379 | `0a4ae527e0162f85a304dcb9e90eea0a0e51ecb34364eb49a0f2264070460d1a` |
| 2014-15 | `Tcheque2015.htm` | 83763 | `42cc00a325ad5cfde350299b5030dc35f284cf0a53bab1494fc00926c266b37d` |
| 2015-16 | `Tcheque2016.htm` | 80459 | `cd33fa66473433c58ba6af109a0bc067c38ded848e730622ec68840231cf640d` |
| 2016-17 | `Tcheque2017.htm` | 109939 | `3f7cedd85b3e2348df7677c1bdee126a9bb4265d91a39616f80d1045bba16412` |
| 2017-18 | `Tcheque2018.htm` | 94099 | `93a0e924e2c94faa9f1f24d4e468c2aaa7cc2440d1cad7fcb04476f357888b22` |
| 2018-19 | `Tcheque2019.htm` | 97878 | `b5636a822ae4281e31d59e9481e0b643b42f85eb2e9754c4567ad449dcc2a8c4` |
| 2019-20 | `Tcheque2020.htm` | 91810 | `bdd344b68f02bb168a29a91d71a84cf954a38e18b172e66c07f15e00c5e4d37b` |
| 2020-21 | `Tcheque2021.htm` | 70924 | `000954e83eecf5528782a7e9c1cf3236a7393af1c43e5c9bee824f55b7b4857b` |
| 2021-22 | `Tcheque2022.htm` | 97517 | `6354948bfe1fef7316cbfd338f72ecdf6bad0730dc37a6f521efffc99f72d0bd` |
| 2022-23 | `Tcheque2023.htm` | 91975 | `0ee8341f4ff29fc4bebf93c5e2e4f535ea3c2ad1abd32da4999ec50dddbafa32` |
| 2023-24 | `Tcheque2024.htm` | 100439 | `f4d8714d14926636c625007f558486ee67f53b99f38635b32592bc71f9eff8a0` |
| 2024-25 | `Tcheque2025.htm` | 99608 | `c28c1e3bd067f5c6a7808905df2763d029ba034e864ef2fb255d3c246c4a01ed` |
| 2025-26 | `Tcheque2026.htm` | 102889 | `002f71badd834e5d39a2f998f5888c63bd3cca3ad0bb5649bb7e404f48e022c0` |

**Football source files** (captured CSV; football-data files contain odds and stay outside the repository):

| File | SHA-256 |
|---|---|
| `1993_9394_E0.csv` | `431f64f3272c82df9a25ba6abffc1c427b25947b6ff15c52b66ad77bb623c804` |
| `1994_9495_E0.csv` | `1a13a383905b009aa0fac6cd4c92da914c7f0aac2b18f4a3c3574879b623b65d` |
| `1995_9596_E0.csv` | `5fced3d4fdd55f2df953cfb55f45c3fc6a1a283a266f0be62b64016c85f631a8` |
| `1996_9697_E0.csv` | `9819155cefcbe480fa5f65f64c197598b6975d40f7156a160fa08868c8156e7e` |
| `1997_9798_E0.csv` | `edf7b268a490b1a5a5ae4d07d3ef4938d9ba2d85180f7efae0ae8f3646e55615` |
| `1998_9899_E0.csv` | `93461480fab8d180584d8b4be7edc58b6b4d861023b04af4a8f8614872aa5196` |
| `1999_9900_E0.csv` | `9e364370db2f58888f241af606f8075ad609a04b5526ddf2d79693c917e7f64c` |
| `2000_0001_E0.csv` | `e2a73bae006d9724b5343d3735a61f11d258955477e3d87b68346d017edaf46b` |
| `2001_0102_E0.csv` | `7a2e26a1a64de18d3b8fd47bca5329613db7b902ea19159817f8285859a1b981` |
| `2002_0203_E0.csv` | `32cb2daf8b3a121ad61601506e855a47f646df97252efed1ef83ffa1883c32a1` |
| `2003_0304_E0.csv` | `29daeb6ded985034f4cce391e476cf2639e9cff78ad8bf9792794b06de346464` |
| `2004_0405_E0.csv` | `85241d09c572dfdf0f03817ceebd9a07d113fd45b7dead1ab6e5a329fd920b2c` |
| `2005_0506_E0.csv` | `b497db70d969f2370f1b09d354ca23880e62f0e9b9a641b02591c40b22ab7971` |
| `2006_0607_E0.csv` | `947b2c56da7837ccd0d31fa65cf7bca7b78851ce32f7b820c98da0e9d8ee5ca8` |
| `2007_0708_E0.csv` | `5945e40bef4334a98f73e71b2e3fa9d075c2c2205d96eb611a1ae8e98511d7f2` |
| `2008_0809_E0.csv` | `b78dcd1c522feafb44bcce1c459eb09911618460787cfe9ab478b2957c7ae294` |
| `2009_0910_E0.csv` | `e8349af783aa262dddb1dbb84de088c15bf43e4fae85f6da4ec30a5c4d62c324` |
| `2010_1011_E0.csv` | `8f5d37651aca8498d8041088835e3a734b79e2fcc34f66ca8516c650970810ce` |
| `2011_1112_E0.csv` | `6cdb9963c311ca2e7d07eb429df721a2593cbd9c9fec55b9af82bca1a457b987` |
| `2012_1213_E0.csv` | `1df561d34a9b79ff8cb1fccd4fd279d183e74cd871063a307ecf18f01e0d622f` |
| `2013_1314_E0.csv` | `3cf16078fde2e0e6c6cb07ebdb20ca98d1a755c9508a18bbeb4ad6837fad2b42` |
| `2014_1415_E0.csv` | `76b7858051ff6b17f46f49f26fdc70c1f29537270492606f5cc63d67fad5d149` |
| `2015_1516_E0.csv` | `bd3502a18c38a1597fd9af62e2366b4015006d3528dd4d18b311bd6237bbc085` |
| `2016_1617_E0.csv` | `9625a7652b5f98fbd3e2e4d378c851fc246693f3343e34a72428d5b6e864d3e0` |
| `2017_1718_E0.csv` | `4f3389365ef3f7ac966764ed8ba67cf3b79f5aebed18dd224099c4b2c98bc67b` |
| `2018_1819_E0.csv` | `7c096b3c2ecd54c6993d22eeea73450c2bde11e3457238b226b8f43c62dfc35e` |
| `2019_1920_E0.csv` | `100037618b94f94057400bb02bf6bac4ef74ddaa58cde4b38370839c39caee61` |
| `2020_2021_E0.csv` | `5afe63f69401457b8354eaacee24f9a3e520b3c3af6329564a9783e20d789c62` |
| `2021_2122_E0.csv` | `335afcbabeb2939fa10ab39ba3e8215072d0b577cb8d0705c1e44c56e934e703` |
| `2022_2223_E0.csv` | `8442792d3b614c94ea3cf381bd2736805889cc1713169035368fff19c3d02380` |
| `2023_2324_E0.csv` | `b2e057b0ed959f198b0f63d2391c01239f3608e6de5db68edab3f88e04d07ff3` |
| `2024_2425_E0.csv` | `d0c8ce4a96d886cf60cf101f570f4a3893844226f91c7bd769eb568c49edbfa4` |
| `2025_2526_E0.csv` | `3e3a8352f9ada6789c508d6ca184424421fed56a30400904a4a327c583407e62` |
| `england.csv` | `4169e4ba8e4e828650c007ac19e0fd751acb098cea38d9be81dafdaf0a7fb1db` |
| `englandplayoffs.csv` | `d62c3e2d5c8d55b3c8a43efc12b8aee4554b54e6835651813754efc66574fbef` |

**Club-name aliases learnt from unambiguous date-and-score matches.** Every alias agreed on all of its matches:

| football-data name | england.csv name | Agreeing / total unambiguous matches |
|---|---|---|
| Arsenal | Arsenal | 915 / 915 |
| Aston Villa | Aston Villa | 779 / 779 |
| Barnsley | Barnsley | 24 / 24 |
| Birmingham | Birmingham City | 181 / 181 |
| Blackburn | Blackburn Rovers | 482 / 482 |
| Blackpool | Blackpool | 28 / 28 |
| Bolton | Bolton Wanderers | 359 / 359 |
| Bournemouth | AFC Bournemouth | 205 / 205 |
| Bradford | Bradford City | 49 / 49 |
| Brentford | Brentford | 90 / 90 |
| Brighton | Brighton & Hove Albion | 205 / 205 |
| Burnley | Burnley | 268 / 268 |
| Cardiff | Cardiff City | 53 / 53 |
| Charlton | Charlton Athletic | 218 / 218 |
| Chelsea | Chelsea | 900 / 900 |
| Coventry | Coventry City | 212 / 212 |
| Crystal Palace | Crystal Palace | 406 / 406 |
| Derby | Derby County | 186 / 186 |
| Everton | Everton | 896 / 896 |
| Fulham | Fulham | 456 / 456 |
| Huddersfield | Huddersfield Town | 60 / 60 |
| Hull | Hull City | 137 / 137 |
| Ipswich | Ipswich Town | 147 / 147 |
| Leeds | Leeds United | 381 / 381 |
| Leicester | Leicester City | 494 / 494 |
| Liverpool | Liverpool | 867 / 867 |
| Luton | Luton Town | 34 / 34 |
| Man City | Manchester City | 782 / 782 |
| Man United | Manchester United | 927 / 927 |
| Middlesbrough | Middlesbrough | 366 / 366 |
| Newcastle | Newcastle United | 825 / 825 |
| Norwich | Norwich City | 247 / 247 |
| Nott'm Forest | Nottingham Forest | 175 / 175 |
| Oldham | Oldham Athletic | 27 / 27 |
| Portsmouth | Portsmouth | 185 / 185 |
| QPR | Queens Park Rangers | 162 / 162 |
| Reading | Reading | 85 / 85 |
| Sheffield United | Sheffield United | 144 / 144 |
| Sheffield Weds | Sheffield Wednesday | 188 / 188 |
| Southampton | Southampton | 658 / 658 |
| Stoke | Stoke City | 273 / 273 |
| Sunderland | Sunderland | 439 / 439 |
| Swansea | Swansea City | 204 / 204 |
| Swindon | Swindon Town | 32 / 32 |
| Tottenham | Tottenham Hotspur | 904 / 904 |
| Watford | Watford | 233 / 233 |
| West Brom | West Bromwich Albion | 363 / 363 |
| West Ham | West Ham United | 813 / 813 |
| Wigan | Wigan Athletic | 221 / 221 |
| Wimbledon | Wimbledon | 196 / 196 |
| Wolves | Wolverhampton Wanderers | 285 / 285 |

## 5. Limits

- Single-compiler hockey data and pre-1993 football data are not cross-checked beyond the samples.
- An external sample (8 and 9 games) verifies only those games.
- Agreement between engsoccerdata and football-data is agreement between two compilers whose upstream sources were not audited (R29).
- Captured pages may have been corrected by their publishers since capture.
- The rebuild changes no profile row: LEAGUE_PROFILES is reviewed separately under R32.
