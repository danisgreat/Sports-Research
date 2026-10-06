"""
build_odi_markdown_docs.py
Creates comprehensive historical support guides:
  - HISTORICAL_PLAYERS_AND_ROSTERS.md
  - VENUES_AND_LOCATIONS.md
in both:
  - Previous Sports Results/Cricket One-Day Format/ODI International/
  - Previous Sports Results/Cricket One-Day Format/Men's ODI International/
"""

import os

PREV1_DIR = os.path.join(os.getcwd(), "Previous Sports Results", "Cricket One-Day Format", "ODI International")
PREV2_DIR = os.path.join(os.getcwd(), "Previous Sports Results", "Cricket One-Day Format", "Men's ODI International")

os.makedirs(PREV1_DIR, exist_ok=True)
os.makedirs(PREV2_DIR, exist_ok=True)

PLAYERS_MD_CONTENT = """# One Day International (ODI) Cricket: Historical Players, Legends & Roster Evolution (1975–2025)

## 1. Overview & Evolution of Limited-Overs International Cricket
One Day International (ODI) cricket is a limited-overs format of international cricket played between Full Members of the International Cricket Council (ICC) and leading Associate Members with temporary or permanent ODI status. This document chronicles the prominent players, legendary captains, record holders, and roster transitions across 51 calendar years (1975 to 2025), specifically focusing on non-World Cup international tournaments (Asia Cup, ICC Champions Trophy, annual tri-series, Austral-Asia Cup, ICC CWC Super League, and bilateral tours).

---

## 2. Era-by-Era Iconic Players and Captains

### 2.1 The Pioneer Era (1975–1983)
* **Australia:** Ian Chappell, Greg Chappell, Dennis Lillee, Jeff Thomson, Rod Marsh, Doug Walters, Kim Hughes, Allan Border.
* **West Indies:** Clive Lloyd (Captain), Vivian Richards, Gordon Greenidge, Desmond Haynes, Alvin Kallicharran, Andy Roberts, Michael Holding, Joel Garner, Colin Croft.
* **England:** Tony Greig, Mike Brearley, Geoff Boycott, Graham Gooch, David Gower, Ian Botham, Bob Willis, Derek Underwood.
* **Pakistan:** Asif Iqbal, Majid Khan, Zaheer Abbas, Mushtaq Mohammad, Imran Khan, Javed Miandad, Sarfraz Nawaz.
* **India:** Srinivas Venkataraghavan, Sunil Gavaskar, Gundappa Viswanath, Kapil Dev, Mohinder Amarnath, Syed Kirmani.
* **New Zealand:** Glenn Turner, Bevan Congdon, Geoff Howarth, Richard Hadlee, John Wright, Lance Cairns.

### 2.2 The Subcontinent Expansion & Sharjah Era (1984–1995)
* **Pakistan:** Imran Khan (Captain), Javed Miandad (Sharjah last-ball six legend, 1986), Wasim Akram, Waqar Younis, Saleem Malik, Inzamam-ul-Haq, Rameez Raja, Aaqib Javed.
* **India:** Kapil Dev, Mohammad Azharuddin, Sachin Tendulkar (debut 1989), Ravi Shastri, Navjot Singh Sidhu, Dilip Vengsarkar, Manoj Prabhakar, Anil Kumble, Javagal Srinath.
* **Australia:** Allan Border (Captain), David Boon, Geoff Marsh, Dean Jones, Steve Waugh, Mark Waugh, Craig McDermott, Bruce Reid, Ian Healy.
* **West Indies:** Vivian Richards, Richie Richardson, Desmond Haynes, Curtly Ambrose, Courtney Walsh, Malcolm Marshall, Brian Lara, Carl Hooper.
* **Sri Lanka:** Duleep Mendis, Arjuna Ranatunga, Aravinda de Silva, Roshan Mahanama, Sanath Jayasuriya, Chaminda Vaas, Muttiah Muralitharan.
* **South Africa (Readmission 1991):** Kepler Wessels, Hansie Cronje, Peter Kirsten, Jonty Rhodes, Allan Donald, Brian McMillan, Andrew Hudson.
* **Zimbabwe (Full Member 1992):** Dave Houghton, Andy Flower, Grant Flower, Alistair Campbell, Heath Streak, Eddo Brandes.

### 2.3 The Modern Era & Powerplay Revolution (1996–2010)
* **Australia (Golden Generation):** Mark Taylor, Steve Waugh, Ricky Ponting, Adam Gilchrist, Matthew Hayden, Michael Bevan (the ultimate finisher), Glenn McGrath, Brett Lee, Shane Warne, Jason Gillespie, Michael Hussey, Andrew Symonds.
* **India:** Sachin Tendulkar ("Desert Storm" Sharjah 1998, first male double-century in 2010), Sourav Ganguly, Rahul Dravid, Virender Sehwag, Yuvraj Singh, MS Dhoni (debut 2004), Zaheer Khan, Harbhajan Singh.
* **Sri Lanka:** Arjuna Ranatunga, Sanath Jayasuriya, Romesh Kaluwitharana, Aravinda de Silva, Mahela Jayawardene, Kumar Sangakkara, Chaminda Vaas, Muttiah Muralitharan, Lasith Malinga.
* **South Africa:** Hansie Cronje, Shaun Pollock, Jacques Kallis, Herschelle Gibbs, Lance Klusener, Gary Kirsten, Mark Boucher, Makhaya Ntini, AB de Villiers, Dale Steyn.
* **Pakistan:** Wasim Akram, Waqar Younis, Saeed Anwar, Inzamam-ul-Haq, Shahid Afridi (37-ball century in 1996), Shoaib Akhtar, Yousuf Youhana (Mohammad Yousuf), Younis Khan, Saqlain Mushtaq, Abdul Razzaq.
* **England:** Nasser Hussain, Michael Vaughan, Alec Stewart, Marcus Trescothick, Andrew Flintoff, Kevin Pietersen, Paul Collingwood, James Anderson.
* **New Zealand:** Stephen Fleming, Nathan Astle, Craig McMillan, Chris Cairns, Daniel Vettori, Shane Bond, Brendon McCullum, Ross Taylor.
* **Bangladesh (Full Member 2000):** Habibul Bashar, Mohammad Rafique, Mashrafe Mortaza, Shakib Al Hasan, Tamim Iqbal, Mushfiqur Rahim.
* **Kenya & Associates:** Steve Tikolo, Maurice Odumbe, Thomas Odoyo, Ryan ten Doeschate (Netherlands).

### 2.4 The High-Scoring & Two-New-Balls Era (2011–2025)
* **India:** MS Dhoni (Captain), Virat Kohli (fastest to 10,000–14,000 ODI runs, 50 ODI centuries), Rohit Sharma (record three double-centuries, 264 highest score), Shikhar Dhawan, Ravindra Jadeja, Jasprit Bumrah, Mohammed Shami, Kuldeep Yadav, KL Rahul, Shubman Gill.
* **Australia:** Michael Clarke, Steven Smith, David Warner, Aaron Finch, Mitchell Starc, Pat Cummins, Josh Hazlewood, Glenn Maxwell, Travis Head, Adam Zampa.
* **England (White-Ball Renaissance):** Eoin Morgan (Captain), Jos Buttler, Joe Root, Ben Stokes, Jonny Bairstow, Jason Roy, Adil Rashid, Chris Woakes, Mark Wood, Jofra Archer.
* **South Africa:** AB de Villiers (fastest 31-ball ODI century), Hashim Amla, Faf du Plessis, Quinton de Kock, Kagiso Rabada, David Miller, Heinrich Klaasen, Keshav Maharaj.
* **New Zealand:** Brendon McCullum, Kane Williamson, Martin Guptill (237* in ODIs), Ross Taylor, Trent Boult, Tim Southee, Mitchell Santner, Matt Henry.
* **Pakistan:** Misbah-ul-Haq, Shahid Afridi, Babar Azam (multiple-year No. 1 ODI batter), Mohammad Rizwan, Shaheen Shah Afridi, Fakhar Zaman (210* double century), Haris Rauf, Shadab Khan.
* **Bangladesh:** Shakib Al Hasan (premier ODI all-rounder), Tamim Iqbal, Mushfiqur Rahim, Mahmudullah, Mustafizur Rahman, Taskin Ahmed, Mehidy Hasan Miraz.
* **Afghanistan (Full Member 2017):** Mohammad Nabi, Rashid Khan, Mujeeb Ur Rahman, Rahmanullah Gurbaz, Ibrahim Zadran, Fazalhaq Farooqi.
* **Ireland (Full Member 2017):** William Porterfield, Kevin O'Brien, Paul Stirling, Andy Balbirnie, George Dockrell, Josh Little, Harry Tector.
* **Leading Associates (CWC League 2):** Gerhard Erasmus (Namibia), Bilal Khan (Oman), Rohit Paudel (Nepal), Monank Patel (USA), Max O'Dowd (Netherlands), Richie Berrington (Scotland).

---

## 3. All-Time Statistical Benchmarks (Non-World Cup ODIs Context)
* **Highest Individual Scores:**
  * Rohit Sharma (India) – 264 vs Sri Lanka at Kolkata (Nov 13, 2014)
  * Martin Guptill (NZ) – 189* vs England at Southampton (Jun 2, 2013)
  * Vivian Richards (WI) – 189* vs England at Manchester (May 31, 1984)
  * Fakhar Zaman (PAK) – 210* vs Zimbabwe at Bulawayo (Jul 20, 2018)
  * Sanath Jayasuriya (SL) – 189 vs India at Sharjah (Oct 29, 2000)
* **Best Bowling Figures:**
  * Chaminda Vaas (SL) – 8/19 vs Zimbabwe at Colombo (Dec 8, 2001)
  * Shahid Afridi (PAK) – 7/12 vs West Indies at Providence (Jul 14, 2013)
  * Glenn McGrath (AUS) – 7/15 vs Namibia at Potchefstroom (2003)
  * Rashid Khan (AFG) – 7/18 vs West Indies at Gros Islet (Jun 9, 2017)
  * Anil Kumble (IND) – 6/12 vs West Indies at Kolkata (Hero Cup Final, Nov 27, 1993)
"""

VENUES_MD_CONTENT = """# One Day International (ODI) Cricket: Venues, Stadiums & Geographies (1975–2025)

## 1. Geographical Distribution of ODI Cricket
One Day International cricket has been staged across six continents, spanning historic test grounds, multi-purpose colosseums, desert oasis floodlit venues, and regional boutique parks. This document details the venues, characteristics, pitch behaviors, and geographic evolution of ODI host locations from 1975 to 2025.

---

## 2. Major Venues by Region

### 2.1 Australia
* **Melbourne Cricket Ground (MCG), Melbourne:**
  * The birthplace of ODI cricket (Jan 5, 1971; ODI # 1).
  * Capacity: 100,024. Spacious boundaries, true drop-in pitch with reliable bounce, historic host of annual World Series Cup finals.
* **Sydney Cricket Ground (SCG), Sydney:**
  * Site of the first international day-night floodlit ODI under Kerry Packer (Nov 27, 1978).
  * Traditionally offers assistance to spin bowling while providing consistent stroke play.
* **Adelaide Oval, Adelaide:**
  * World-class drop-in surface known for short square boundaries and long straight boundaries.
* **The Gabba (Brisbane Cricket Ground), Brisbane:**
  * Renowned for steep pace, tennis-ball bounce, and humid conditions assisting early swing.
* **W.A.C.A. Ground & Optus Stadium, Perth:**
  * The W.A.C.A. was famed as the fastest pitch in world cricket; transitioned major matches to the 60,000-seat Optus Stadium in 2018.
* **Bellerive Oval (Blundstone Arena), Hobart:**
  * Picturesque Tasmanian ground with sea breezes off the Derwent River.

### 2.2 England & Wales
* **Lord's Cricket Ground, London:**
  * "The Home of Cricket", host of inaugural Prudential Trophy and NatWest Series finals. Features iconic slope (2.5 meters from north to south).
* **Kennington Oval (The Oval), London:**
  * True batting surface with good pace and bounce; host of 2004 & 2017 ICC Champions Trophy finals.
* **Edgbaston Cricket Ground, Birmingham:**
  * High-atmosphere ground; host of 2013 ICC Champions Trophy final.
* **Old Trafford Cricket Ground, Manchester:**
  * Traditional bouncy surface with reverse swing characteristics.
* **Headingley Cricket Ground, Leeds & Trent Bridge, Nottingham:**
  * Known for pronounced swing bowling conditions in overcast northern English skies; Trent Bridge became famous for ultra-high totals (481/6 by England vs Australia in 2018).
* **The Rose Bowl (Southampton), Sophia Gardens (Cardiff), Riverside (Chester-le-Street):**
  * Modern expansion venues built between 1995 and 2008.

### 2.3 The Indian Subcontinent
* **Sharjah Cricket Stadium, Sharjah (United Arab Emirates):**
  * World record holder for hosting the most ODIs at a single venue (over 240 matches). Host of the Asia Cup, Austral-Asia Cup, Champions Trophy, and Wills Trophy. Famed for flat pitches, short boundaries, and intense India-Pakistan clashes.
* **Eden Gardens, Kolkata (India):**
  * Colosseum of Indian cricket; capacity historic 100,000+ (now ~68,000). Host of the 1993 Hero Cup final and Rohit Sharma's 264 (2014).
* **Wankhede Stadium & Brabourne Stadium, Mumbai (India):**
  * Red-soil pitches offering good carry, true bounce, and evening dew factor off the Arabian Sea.
* **Arun Jaitley Stadium (Feroz Shah Kotla), Delhi (India):**
  * Low-bounce surface traditionally aiding spinners and cutters.
* **M. Chinnaswamy Stadium, Bengaluru (India):**
  * Small dimensions at high altitude (900m above sea level), leading to record-breaking six-hitting and high scoring.
* **Narendra Modi Stadium, Ahmedabad (India):**
  * Largest cricket stadium in the world (132,000 capacity).
* **Gaddafi Stadium (Lahore) & National Stadium (Karachi), Pakistan:**
  * Traditional powerhouses of Pakistani ODI cricket, known for batting paradises and reverse swing under dry heat.
* **R. Premadasa Stadium (RPS) & Sinhalese Sports Club (SSC), Colombo, Sri Lanka:**
  * Premadasa has hosted 140+ ODIs; notable for spinning conditions under floodlights with humid tropical weather.
* **Sher-e-Bangla National Cricket Stadium, Mirpur, Dhaka (Bangladesh):**
  * Home of Bangladesh cricket; black-soil pitches with low bounce, turn, and heavy dew in winter.

### 2.4 South Africa & Zimbabwe
* **Wanderers Stadium, Johannesburg (The "Bullring"):**
  * High altitude (1,753m above sea level), thin air, true bounce. Scene of the historic "438 Match" (Australia 434/4 vs South Africa 438/9 on March 12, 2006).
* **Newlands, Cape Town:**
  * Framed by Table Mountain; provides lateral seam movement off the pitch with afternoon sea breezes.
* **Kingsmead, Durban:**
  * Sub-tropical seaside venue where humid evening coastal breezes historically produced dramatic swing.
* **SuperSport Park, Centurion:**
  * Hard bouncy wicket favoring fast bowlers and aggressive stroke-makers.
* **Harare Sports Club (Harare) & Queens Sports Club (Bulawayo), Zimbabwe:**
  * Sun-baked pitches offering good batting conditions before taking spin in the second half.

### 2.5 West Indies
* **Kensington Oval, Bridgetown, Barbados:**
  * The premier Caribbean cricket ground; pace, bounce, and trade winds.
* **Queen's Park Oval, Port of Spain, Trinidad:**
  * Spin-friendly surface nestled against the Northern Range hills.
* **Sabina Park, Kingston, Jamaica & Bourda, Georgetown, Guyana:**
  * Historically fierce bounce at Sabina Park; Bourda was built below sea level on coastal clay.

### 2.6 Emerging & Associate Global Venues
* **Toronto Cricket, Skating and Curling Club, Toronto (Canada):**
  * Host of the historic Sahara Cup (India v Pakistan bilateral series, 1996–1998).
* **Malahide (Dublin) & Stormont (Belfast), Ireland:**
  * Lush green surfaces with cool temperatures and prolonged swing.
* **VRA Cricket Ground, Amstelveen (Netherlands):**
  * Premier Dutch venue, hosted England, Pakistan, Australia in bilateral tours.
* **Tribhuvan University Ground, Kirtipur (Nepal):**
  * Passionate mountain-valley venue regularly drawing 20,000+ spectators for CWC League 2 fixtures.
* **Oman Cricket Academy Ground (Al Amarat, Muscat) & Moosa Stadium (Pearland, USA):**
  * Modern purpose-built ODI hubs for ICC pathway competitions.
"""

for target_dir in [PREV1_DIR, PREV2_DIR]:
    with open(os.path.join(target_dir, "HISTORICAL_PLAYERS_AND_ROSTERS.md"), "w", encoding="utf-8") as f:
        f.write(PLAYERS_MD_CONTENT)
    with open(os.path.join(target_dir, "VENUES_AND_LOCATIONS.md"), "w", encoding="utf-8") as f:
        f.write(VENUES_MD_CONTENT)

print("Generated HISTORICAL_PLAYERS_AND_ROSTERS.md and VENUES_AND_LOCATIONS.md in both target directories.")
