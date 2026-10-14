# Top-Tier Korean Basketball Research Dossier (1975–2025)
**Prepared for Data Engineering & Game Log Construction**

---

### Executive Overview
This research dossier details the complete historical landscape of top-tier men's basketball in South Korea from 1975 through 2025. It encompasses the pre-professional era (**National Business Basketball League / 실업농구연맹전** and **Basketball Festival / 농구대잔치**) and the professional era (**Korean Basketball League / KBL**, including regular seasons, playoffs, KBL Cup, All-Star Games, and the Pro-Am Tournament). Exact API endpoints, request schemas, season-by-season game counts, rule evolution, team lineage trees, and sample records are provided.

---

## 1. Historical Eras & League Structures (1975–2025)

### 1.1 Pre-KBL Era (1975–1996)
Before the establishment of the KBL in 1997, Korean top-flight basketball was dominated by corporate business teams (실업팀) and elite university powerhouses (대학팀).

#### A. National Business Basketball League (실업농구연맹전, 1975–1983) & National Championships
- **Governing Body:** Korea Business Basketball Confederation (한국실업농구연맹) and Korea Basketball Association (대한민국농구협회 / KBA).
- **Structure:** Competitions were held 2 to 3 times per calendar year (Spring / 춘계, Summer / 하계, Autumn / 추계 실업연맹전), alongside the National Basketball Championship (전국종별농구선수권대회 / 종합선수권).
- **Pioneering Teams:**
  - Corporate titans: Hyundai Electronics (현대전자, founded 1978), Samsung Electronics (삼성전자, founded 1978), Industrial Bank of Korea (중소기업은행 / 기업은행), Bank of Korea (한국은행), Korea Development Bank (한국산업은행), POSCO (포항제철), Haitai Confectionery (해태제과), and Sangmu (국군체육부대 / 육군 경리단).
- **Format:** 20-minute halves (전·후반 각 20분, 40-minute games), 30-second shot clock (FIBA standard), no 3-point line until the 1984–85 season.

#### B. Basketball Festival (농구대잔치 - Nonggu Daejanchi, 1983–1997)
- **Genesis:** Created in the winter of 1983 as the **Jumbo Series (점보시리즈)** to unify top business and collegiate teams into a nationwide winter circuit; rebranded as **농구대잔치** in 1984 under government cultural directives.
- **Tournament Structure (1983–1992):** 
  - Divided into 4 stages: 1st, 2nd, and 3rd divisional tourneys followed by the 4th Final Championship Tournament (최종 토너먼트).
- **Tournament Structure (1993–1997):**
  - Consolidated into a single unified full round-robin league (풀리그) followed by a top-4 or top-8 playoff tournament.
- **Key Powerhouses:**
  - **The Kia Dynasty (기아자동차):** Founded in 1986 under Kia Motors, featuring the legendary "Hur-Dong-Taek" trio (허재 Hur Jae, 강동희 Kang Dong-hee, 김유택 Kim Yoo-taek) plus Han Ki-bum (한기범). Kia captured 7 championships in 8 seasons (1988–89, 1989–90, 1990–91, 1991–92, 1992–93, 1994–95, 1995–96).
  - **Hyundai Electronics (현대전자):** Led by sharpshooter Lee Chung-hee (이충희) and Park Soo-kyo (박수교). Won titles in 1983–84, 1985–86, 1986–87.
  - **Samsung Electronics (삼성전자):** Led by Kim Hyun-jun (김현준) and Im Jeong-myeong (임정명). Won titles in 1984–85, 1987–88.
  - **Collegiate Giants:** 
    - **Yonsei University (연세대학교):** Sparked the 1990s basketball boom with Seo Jang-hoon (서장훈), Moon Kyung-eun (문경은), Lee Sang-min (이상민), Woo Ji-won (우지원), and Kim Hoon (김훈). In **1993–94**, Yonsei became the first college team in history to win the Nonggu Daejanchi national championship, repeated in **1996–97**.
    - **Korea University (고려대학교):** Fierce rivals of Yonsei, featuring Hyun Joo-yup (현주엽), Chun Hee-chul (전희철), Kim Byung-chul (김병철), and Shin Ki-sung (신기성).
    - **Chung-Ang University (중앙대학교):** Historically the collegiate powerhouse producing Hur Jae, Kang Dong-hee, and Kim Yoo-taek; runner-up in 1985–86 and 1986–87.

---

### 1.2 KBL Professional Era (1997–2025)

#### A. League Expansion & Game Count History
- **1997 Inaugural Season:** 
  - Ran from February 1 to May 1, 1997.
  - **8 founding teams:** Busan Kia Enterprise, Wonju Narae Blue Birds, Anyang SBS Stars, Daegu Tongyang Orions, Gwangju Nasan Flamans, Incheon Daewoo Securities Zeus, Daejeon Hyundai Dynat, Suwon Samsung Thunders.
  - Schedule: 3 rounds (21 games per team), **84 regular season games**.
  - Playoffs: 6-team bracket (Top 2 bye to semifinals, quarters best-of-5, semis best-of-5, finals best-of-7), **27 playoff games**.
- **1997–98 to 2000–01 (Seasons 2–5):**
  - Expanded to **10 teams** with 경남 LG 세이커스 (Gyeongnam LG Sakers) and 청주 SK 나이츠 (Cheongju SK Knights).
  - Schedule: 5 rounds (45 games per team), **225 regular season games** per year.
- **2001–02 to 2024–25 (Seasons 6–45):**
  - Expanded to 6 rounds (54 games per team), **270 regular season games** per year.
  - Standard 6-team playoff bracket: Quarterfinals (3 vs 6, 4 vs 5, best-of-5), Semifinals (1 vs QF winner, 2 vs QF winner, best-of-5), Championship Finals (best-of-7).

#### B. KBL Cup (KBL 컵대회, 2020–present)
Introduced in 2020 as an official preseason knockout/group tournament featuring all 10 KBL clubs plus Sangmu (국군체육부대):
- **2020 (Gunsan / 군산월명체육관):** Sept 20–27, 2020 (14 games). Champion: **고양 오리온** (94–81 vs 서울 SK). MVP: 이대성 (Lee Dae-sung).
- **2021 (Sangju / 상주실내체육관):** Sept 11–18, 2021 (14 games). Champion: **서울 SK** (90–82 vs 원주 DB). MVP: 김선형 (Kim Sun-hyung).
- **2022 (Tongyeong / 통영체육관):** Oct 1–8, 2022 (14 games). Champion: **수원 KT** (74–72 vs 울산 현대모비스). MVP: 이제이 아노시케 (EJ Anosike).
- **2023 (Gunsan / 군산월명체육관):** Oct 8–15, 2023 (14 games). Champion: **부산 KCC** (81–76 vs 울산 현대모비스). MVP: 알리제 존슨 (Alize Johnson).
- **2024 (Jecheon / 제천체육관):** Oct 5–13, 2024 (14 games). Champion: **원주 DB** (77–67 vs 수원 KT). MVP: 치나누 오누아쿠 (Chinanu Onuaku).

#### C. KBL-KBA Pro-Am Tournament (프로-아마 최강전, 2012–2016)
Official knockout tournament co-sanctioned by KBL and KBA pitting 10 KBL teams, top 5 college teams, and Sangmu (16 teams total):
- **2012 (Goyang):** Nov 28 – Dec 6, 2012. Champion: **국군체육부대 (Sangmu)** 65–61 인천 전자랜드. MVP: 윤호영 (Yoon Ho-young).
- **2013 (Seoul Jamsil Students):** Aug 15–22, 2013. Champion: **고려대학교 (Korea University)** 75–67 국군체육부대. MVP: 이종현 (Lee Jong-hyun).
- **2014:** Not held.
- **2015 (Seoul Jamsil Students):** Aug 15–22, 2015. Champion: **고양 오리온스** 93–68 고려대학교. MVP: 이승현 (Lee Seung-hyun).
- **2016 (Seoul Jamsil Students):** Aug 21–28, 2016. Champion: **신협 상무 (Sangmu)** 84–71 창원 LG. MVP: 김시래 (Kim Si-rae).

#### D. KBL All-Star Games (1997–present)
- **Game Code:** `gameCode = "10"` in KBL API.
- **Team Formats:**
  - 1997–2004: Central Selection (중부선발: Seoul, Wonju, Anyang, Incheon) vs Southern Selection (남부선발: Busan, Daegu, Changwon, Gwangju/Daejeon).
  - 2004–05 to 2014–15: Dream Team (드림팀: Dongbu, Mobis, LG, KT, Orions) vs Magic Team (매직팀: Samsung, SK, KCC, KGC, ET Land).
  - 2015–16 to 2016–17: Senior All-Stars vs Junior All-Stars (age-divided).
  - 2017–18 to 2022–23: Draft system by top vote-getters (e.g., Team Heo Ung vs Team Heo Hoon).
  - 2023–24 to 2024–25: Character branding ("크블몽 팀" Team KBL Mong vs "공아지 팀" Team Gong-A-Ji).
  - 2025–26: "팀 브라운" (Team Brown) vs "팀 코니" (Team Cony).
- **Side Competitions:** Dunk Contest (국내/외국인 덩크 콘테스트), 3-Point Contest (3점슛 콘테스트), Skills Challenge (스킬스 챌린지).

---

## 2. Exhaustive Data Sources, APIs & Scraper Blueprint

### 2.1 Primary Source: Official KBL Production API (`api.kbl.or.kr`)
The official KBL site runs on an open REST JSON API that archives every regular season, playoff, all-star, and cup game from February 1, 1997 to the present day.

#### Mandatory Request Headers
Requests to `https://api.kbl.or.kr` MUST include these three custom headers, otherwise a 400 error (`{"resultCode":"Fail","message":"필수 헤더 정보가 누락되었습니다."}`) is returned:
```http
teamcode: XX
lang: ko
channel: WEB
```

#### Core Endpoints

1. **Season Registry:**
   - **URL:** `GET https://api.kbl.or.kr/season/list?seasonCategory=R&gameCode=01&seasonGrade=1`
   - **Returns:** All 31 tier-1 KBL seasons with codes, dates, and keys.

2. **Match Calendar & Scores (Monthly/Range):**
   - **URL:** `GET https://api.kbl.or.kr/match/list?fromDate={YYYYMMDD}&toDate={YYYYMMDD}&tcodeList=all`
   - **Parameters:** `fromDate`, `toDate` (YYYYMMDD), `tcodeList=all`
   - **Returns:** Full list of matches in date range, including `gmkey`, teams, final score, arena, attendance (`crowds`), TV broadcaster.

3. **Single Game Summary & Box Score (Quarter/Period Scores):**
   - **URL:** `GET https://api.kbl.or.kr/match/{gmkey}`
   - **Returns:** Quarter-by-quarter points (`scoreq1`, `scoreq2`, `scoreq3`, `scoreq4`, `scoreeq` [overtimes]), coaching staffs, referees, venue details.

4. **Player Box Scores & Advanced Analytics:**
   - **URL:** `GET https://api.kbl.or.kr/match/{gmkey}/player-stat`
   - **Returns:** Individual player line: PTS, 2PT, 3PT, FT, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, +/- (`marginCn`), MP (`playMin`, `playSec`), starter status (`startFlag`), plus advanced stats (PER, TS%, eFG%, ORtg, DRtg, NetRtg, USG%, PIE, Pace).

5. **Team Aggregated Records:**
   - **URL:** `GET https://api.kbl.or.kr/match/{gmkey}/team-record`

6. **Season Standings:**
   - **URL:** `GET https://api.kbl.or.kr/league/rank/{glkey}`

7. **Playoff Brackets:**
   - **URL:** `GET https://api.kbl.or.kr/league/playoff/new/{glkey}`

#### `gmkey` Structure Decoded
- Format: `S{seasonCode}G{gameCode}N{gameNo}`
- Examples:
  - `S1G01N1`: Season 1 (1997), Regular Season (`01`), Game 1.
  - `S1G03N1`: Season 1, Quarterfinal/Semifinal Playoff (`03`), Game 1.
  - `S1G04N1`: Season 1, Championship Final (`04`), Game 1.
  - `S1G10N1`: Season 1, All-Star Game (`10`), Game 1.
  - `S43G13N1`: Season 43 (2023–24), KBL Cup (`13`), Game 1.

---

### 2.2 Secondary Source: Korea Basketball Association Archive (`koreabasketball.or.kr`)
The KBA hosts historical archives for the **농구대잔치 (1983–2017)** and collegiate championships:
- **Standings & Results URL:** `https://www.koreabasketball.or.kr/game/record_01.php?sch_div=7&sch_season_gu={season_code}&sch_game_type=01`
  - `sch_div=7`: 농구대잔치 (Basketball Festival)
  - `sch_season_gu`: `001` (1983) through `036` (2017)
  - `sch_game_type`: `01` (남자부 Men's), `11` (여자부 Women's)
- **Player Stats URL:** `https://www.koreabasketball.or.kr/game/record_04.php?sch_div=7&sch_season_gu={season_code}&sch_game_type=01`

---

### 2.3 Tertiary Sources: Korean Wikipedia & Namuwiki
- **Wikipedia Season Articles:** `https://ko.wikipedia.org/wiki/한국프로농구_{시즌}` (e.g., `한국프로농구 1997`, `한국프로농구 1997-98` ... `한국프로농구 2024-25`).
- **Wikipedia Cup & Pro-Am Articles:** `KBL 컵대회`, `프로-아마농구 최강전`.
- **Namuwiki Pages:** High granular detail on roster transactions, foreigner drafts (트라이아웃 / 자유선발), uniform changes, and referee controversies.

---

## 3. Historical Anomalies, Shortened Seasons & Rule Evolutions

### 3.1 Period Format & Timing Rules
- **Pre-KBL Era (1975–1996):**
  - Two 20-minute halves (전·후반 각 20분, 40-minute total).
  - FIBA 30-second shot clock.
  - Overtime: 5-minute extra periods.
- **KBL Era (1997–present):**
  - Four 10-minute quarters (10분 4쿼터).
  - Adopted the NBA-style **24-second shot clock** and **8-second frontcourt rule** immediately at its 1997 founding.
  - Overtime: 5 minutes per OT period; unlimited OTs until winner is determined (no ties).

### 3.2 Court Dimensions & Distance Shifts
- **3-Point Arc Distance:**
  - 1984 to 2008–09: **6.25 meters** (original FIBA line).
  - 2009–10 season to present: Moved back to **6.75 meters** in compliance with FIBA rule revisions.
- **Defensive 3-Seconds Rule:**
  - Enforced from the early KBL seasons (modeled after the NBA illegal defense rule).
  - **Abolished in the 2012–13 season** to align with FIBA zone defense guidelines.

### 3.3 Foreign Player System Evolution
- 1997 to 2007–08: Draft Tryout System (2 players allowed on court simultaneously in certain quarters).
- 2008–09 to 2011–12: Height restrictions adjusted; 2 players on roster, 1 on court.
- 2015–16 to 2017–18: Split-tier height limits (Long player ≤ 193cm, Short player ≤ 186cm).
- 2019–20 to present: Height restrictions fully abolished; Asian Quarter player system (아시아 쿼터제) introduced in 2020–21 (initially Philippines/Japan).

### 3.4 Shortened Seasons & League Anomalies
1. **1997 Inaugural Season:** Transitional spring season (Feb 1 – May 1, 1997; 21 games/team, 84 regular season games).
2. **2019–20 COVID-19 Abrupt Cancellation:**
   - On **March 24, 2020**, KBL officially terminated the season early following suspension on Feb 29.
   - Regular season frozen at Round 5: Teams played 42 or 43 games (total 213 regular season games).
   - **Wonju DB Promy** and **Seoul SK Knights** were tied at 28–15 and declared **co-first place winners (공동 1위)**.
   - Playoffs and Finals were **completely cancelled**.
3. **2020–21 All-Star Game Cancellation:** Cancelled due to social distancing regulations.
4. **Dayone Sports Scandal (2022–23):**
   - Goyang Carrot Jumpers operated under severe financial insolvency.
   - Expelled from KBL on June 16, 2023. The roster was rescued and absorbed by Sono International to establish the **Goyang Sono Skygunners**.
5. **Major Franchise Relocations:**
   - 2001: Suwon Samsung -> Seoul Samsung; Cheongju SK -> Seoul SK; Busan Kia -> Ulsan Mobis.
   - 2011: Daegu Orions relocated abruptly to Goyang.
   - 2021: Busan KT relocated to Suwon (Suwon KT Sonicboom).
   - 2021: Incheon Electroland sold to KOGAS and moved to Daegu (Daegu KOGAS Pegasus).
   - 2023: Jeonju KCC relocated to Busan (Busan KCC Egis) after arena renovation disputes with Jeonju municipality.

---

## 4. Franchise Lineage Matrix (The 10 Active Teams)

| # | Current Franchise (2025–26) | Founding Year | Lineage & Rebranding History | Home Cities |
|---|-----------------------------|---------------|------------------------------|-------------|
| 1 | **울산 현대모비스 피버스**<br>(Ulsan Hyundai Mobis) | 1986 | 기아자동차 (1986) -> 부산 기아 엔터프라이즈 (1997) -> 울산 모비스 오토몬스 (2001) -> 울산 모비스 피버스 (2004) -> 울산 현대모비스 (2017) | Busan (1997–01) -> Ulsan (2001–pres.) |
| 2 | **서울 삼성 썬더스**<br>(Seoul Samsung Thunders) | 1978 | 삼성전자 (1978) -> 수원 삼성 썬더스 (1997) -> 서울 삼성 썬더스 (2001) | Suwon (1997–01) -> Seoul (2001–pres.) |
| 3 | **원주 DB 프로미**<br>(Wonju DB Promy) | 1996 | 나래이동통신 (1996) -> 원주 나래 블루버드 (1997) -> 원주 삼보 엑써스 (1999) -> 원주 TG 엑써스 (2002) -> 원주 TG삼보 (2003) -> 원주 동부 프로미 (2005) -> 원주 DB 프로미 (2017) | Wonju (1997–pres.) |
| 4 | **부산 KCC 이지스**<br>(Busan KCC Egis) | 1978 | 현대전자 (1978) -> 대전 현대 다이넷 (1997) -> 대전 현대 걸리버스 (1999) -> 전주 KCC 이지스 (2001) -> 부산 KCC 이지스 (2023) | Daejeon (1997–01) -> Jeonju (2001–23) -> Busan (2023–pres.) |
| 5 | **창원 LG 세이커스**<br>(Changwon LG Sakers) | 1997 | LG반도체 (1997) -> 경남 LG 세이커스 (1997) -> 창원 LG 세이커스 (1998) | Changwon (1997–pres.) |
| 6 | **수원 KT 소닉붐**<br>(Suwon KT Sonicboom) | 1997 | 광주 나산 플라망스 (1997) -> 광주 골드뱅크 (1999) -> 여수 골드뱅크 (2000) -> 여수/부산 코리아텐더 (2001–03) -> 부산 KTF 매직윙스 (2003) -> 부산 KT 소닉붐 (2009) -> 수원 KT 소닉붐 (2021) | Gwangju -> Yeosu -> Busan -> Suwon |
| 7 | **고양 소노 스카이거너스**<br>(Goyang Sono Skygunners) | 1996 | 동양제과 (1996) -> 대구 동양 오리온스 (1997) -> 대구 오리온스 (2003) -> 고양 오리온스 (2011) -> 고양 캐롯/데이원 점퍼스 (2022–23) -> 고양 소노 스카이거너스 (2023) | Daegu (1997–11) -> Goyang (2011–pres.) |
| 8 | **안양 정관장 레드부스터스**<br>(Anyang Jung Kwan Jang) | 1992 | SBS 농구단 (1992) -> 안양 SBS 스타즈 (1997) -> 안양 KT&G 카이츠 (2005) -> 안양 KGC인삼공사 (2010) -> 안양 정관장 레드부스터스 (2023) | Anyang (1997–pres.) |
| 9 | **대구 한국가스공사 페가수스**<br>(Daegu KOGAS Pegasus) | 1994 | 대우증권 (1994) -> 인천 대우증권 제우스 (1997) -> 인천 신세기 빅스 (1999) -> 인천 SK 빅스 (2001) -> 인천 전자랜드 블랙슬래머/엘리펀츠 (2003–21) -> 대구 한국가스공사 (2021) | Incheon (1997–21) -> Daegu (2021–pres.) |
| 10 | **서울 SK 나이츠**<br>(Seoul SK Knights) | 1997 | 청주 SK 나이츠 (1997) -> 서울 SK 나이츠 (2001) | Cheongju (1997–01) -> Seoul (2001–pres.) |

---

## 5. Season-by-Season Game Count Matrix (KBL Era 1997–2025)

| Season Code | Season Name | Teams | Reg Games/Tm | Total Reg Games | Playoff Games | All-Star | KBL Cup | Total Tier-1 Games | Regular Season 1st Place | Championship Winner |
|:-----------:|:-----------:|:-----:|:------------:|:---------------:|:-------------:|:--------:|:-------:|:------------------:|:------------------------:|:-------------------:|
| **S1** | 1997 | 8 | 21 | 84 | 27 | 1 | — | **112** | 부산 기아 | 부산 기아 |
| **S2** | 1997–98 | 10 | 45 | 225 | 23 | 1 | — | **249** | 대전 현대 | 대전 현대 |
| **S3** | 1998–99 | 10 | 45 | 225 | 21 | 1 | — | **247** | 대전 현대 | 대전 현대 |
| **S4** | 1999–00 | 10 | 45 | 225 | 21 | 1 | — | **247** | 대전 현대 | 청주 SK |
| **S5** | 2000–01 | 10 | 45 | 225 | 23 | 1 | — | **249** | 수원 삼성 | 수원 삼성 |
| **S6** | 2001–02 | 10 | 54 | 270 | 21 | 1 | — | **292** | 대구 동양 | 대구 동양 |
| **S7** | 2002–03 | 10 | 54 | 270 | 18 | 1 | — | **289** | 대구 동양 | 원주 TG |
| **S8** | 2003–04 | 10 | 54 | 270 | 20 | 1 | — | **292** | 원주 TG삼보 | 전주 KCC |
| **S9** | 2004–05 | 10 | 54 | 270 | 21 | 1 | — | **292** | 원주 TG삼보 | 원주 TG삼보 |
| **S10** | 2005–06 | 10 | 54 | 270 | 18 | 1 | — | **289** | 울산 모비스 | 서울 삼성 |
| **S11** | 2006–07 | 10 | 54 | 270 | 21 | 1 | — | **292** | 울산 모비스 | 울산 모비스 |
| **S12** | 2007–08 | 10 | 54 | 270 | 19 | 1 | — | **290** | 원주 동부 | 원주 동부 |
| **S13** | 2008–09 | 10 | 54 | 270 | 23 | 1 | — | **294** | 울산 모비스 | 전주 KCC |
| **S15** | 2009–10 | 10 | 54 | 270 | 22 | 1 | — | **293** | 울산 모비스 | 울산 모비스 |
| **S17** | 2010–11 | 10 | 54 | 270 | 22 | 1 | — | **293** | 부산 KT | 전주 KCC |
| **S19** | 2011–12 | 10 | 54 | 270 | 20 | 1 | — | **291** | 원주 동부 | 안양 KGC |
| **S21** | 2012–13 | 10 | 54 | 270 | 18 | 1 | — | **289** | 서울 SK | 울산 모비스 |
| **S23** | 2013–14 | 10 | 54 | 270 | 18 | 1 | — | **289** | 창원 LG | 울산 모비스 |
| **S25** | 2014–15 | 10 | 54 | 270 | 20 | 1 | — | **291** | 울산 모비스 | 울산 모비스 |
| **S27** | 2015–16 | 10 | 54 | 270 | 20 | 1 | — | **291** | 전주 KCC | 고양 오리온 |
| **S29** | 2016–17 | 10 | 54 | 270 | 20 | 1 | — | **291** | 안양 KGC | 안양 KGC |
| **S31** | 2017–18 | 10 | 54 | 270 | 22 | 1 | — | **293** | 원주 DB | 서울 SK |
| **S33** | 2018–19 | 10 | 54 | 270 | 20 | 1 | — | **291** | 울산 현대모비스 | 울산 현대모비스 |
| **S35** | 2019–20 | 10 | 42–43 | **213** *(COVID)* | **0** *(Cancelled)* | 1 | — | **214** | 원주 DB / 서울 SK (공동) | *None* |
| **S37** | 2020–21 | 10 | 54 | 270 | 19 | **0** *(COVID)* | 14 | **303** | 전주 KCC | 안양 KGC |
| **S39** | 2021–22 | 10 | 54 | 270 | 17 | 1 | 14 | **302** | 서울 SK | 서울 SK |
| **S41** | 2022–23 | 10 | 54 | 270 | 22 | 1 | 14 | **307** | 안양 KGC | 안양 KGC |
| **S43** | 2023–24 | 10 | 54 | 270 | 21 | 1 | 14 | **306** | 원주 DB | 부산 KCC |
| **S45** | 2024–25 | 10 | 54 | 270 | 21 | 1 | 14 | **306** | 서울 SK | 서울 SK |
| **S47** | 2025–26 | 10 | 54 | 270 | 21 | 1 | 14 | **306** | 창원 LG | 창원 LG |

---

## 6. Sample API Payloads & JSON Schemas

### Sample 1: Historic First KBL Game (`S1G01N1` — Feb 1, 1997)
- **URL:** `GET https://api.kbl.or.kr/match/S1G01N1`
```json
{
  "game": {
    "gmkey": "S1G01N1",
    "glkey": "S1G01",
    "seasonCode": 1,
    "seasonGrade": 1,
    "seasonCategoryName": "정규시즌",
    "gameCode": "01",
    "gameNo": 1,
    "gameDate": "19970201",
    "tcodeH": "40",
    "tcodeA": "25",
    "tnameH": "안양SBS",
    "tnameA": "인천대우증권",
    "tnameFH": "안양 SBS 스타즈",
    "tnameFA": "인천 대우증권 제우스",
    "seasonName": "1997",
    "gameStart": "1600",
    "gameEnd": "1730",
    "gameTime": 130,
    "crowds": 6066,
    "stadiumnameF": "올림픽제2체육관",
    "judges": {
      "main": { "name": "신현수" },
      "sub": [{ "name": "한규돈" }, { "name": "기형환" }]
    }
  },
  "teams": {
    "home": {
      "tcode": "40",
      "tname": "안양SBS",
      "staffs": { "manager": { "name": "김동광" }, "coaches": [{ "name": "강정수" }] }
    },
    "away": {
      "tcode": "25",
      "tname": "인천대우증권",
      "staffs": { "manager": { "name": "최종규" }, "coaches": [{ "name": "유재학" }] }
    }
  },
  "teamrecords": {
    "home": { "scoreq1": 34, "scoreq2": 25, "scoreq3": 22, "scoreq4": 27, "scoreeq": [] },
    "away": { "scoreq1": 30, "scoreq2": 24, "scoreq3": 24, "scoreq4": 29, "scoreeq": [] }
  }
}
```

### Sample 2: Player Box Score with Advanced Metrics (`https://api.kbl.or.kr/match/{gmkey}/player-stat`)
```json
{
  "player": {
    "pcode": "291091",
    "pname": "양홍석",
    "ename": "YANG HONG SEOK",
    "tcode": "50",
    "tname": "창원 LG",
    "backNum": "11",
    "pos": "FD",
    "playerFlag": "0",
    "img": "https://kbl.or.kr/files/kbl/players-photo/291091.png"
  },
  "records": {
    "score": 22,
    "playMin": 31,
    "playSec": 39,
    "fg": 7,
    "fgA": 12,
    "fgt": 8,
    "fgtA": 16,
    "threep": 1,
    "threepA": 4,
    "ft": 5,
    "ftA": 5,
    "offr": 3,
    "defr": 3,
    "rb": 6,
    "ast": 6,
    "stl": 0,
    "bs": 0,
    "to": 3,
    "foul": 2,
    "marginCn": 20,
    "per": 25.7,
    "offrtg": 120.9,
    "defrtg": 86.2,
    "netrtg": 34.7,
    "efgRt": 53.1,
    "tsRt": 60.4,
    "astRt": 24.5,
    "usgRt": 30.4,
    "pace": 46.6,
    "pie": 18.8
  },
  "homeAway": "2",
  "startFlag": 1
}
```

---

### Session Recording Notice
*The recording of this investigation session is preserved and accessible within the conversation artifacts.*