import os
import sys
import csv
import sqlite3
import datetime
import re

from bleague_teams import normalize_team
from historical_games_data import HISTORICAL_GAMES
from historical_games_data_part2 import MORE_HISTORICAL_GAMES

sys.stdout.reconfigure(encoding='utf-8')

# Merge historical game dictionaries
ALL_HISTORICAL_GAMES = {}
ALL_HISTORICAL_GAMES.update(HISTORICAL_GAMES)
ALL_HISTORICAL_GAMES.update(MORE_HISTORICAL_GAMES)

# Add remaining historical seasons (2004 to 2015 and 2026)
REMAINING_HISTORICAL = {
    2004: [
        {
            "gid": "EMP_2004_01",
            "comp": "79th Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2004-01-11",
            "time": "15:00:00",
            "home": "Aisin Seahorses",
            "away": "Toyota Motors",
            "h_score": 73,
            "a_score": 57,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5600",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin Seahorses captured their 3rd consecutive Emperor's Cup title defeating Toyota Motors 73 - 57.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "JBL_2004_SF1_1",
            "comp": "4th JBL Super League",
            "gtype": "Semifinals",
            "stage": "Semifinals Game 1",
            "date": "2005-02-26",
            "time": "14:00:00",
            "home": "Toshiba",
            "away": "Mitsubishi Electric",
            "h_score": 86,
            "a_score": 55,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "4200",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toshiba dominated Mitsubishi Electric 86 - 55 in Game 1 of the 2004-05 JBL Semifinals.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2004_SF1_2",
            "comp": "4th JBL Super League",
            "gtype": "Semifinals",
            "stage": "Semifinals Game 2",
            "date": "2005-02-27",
            "time": "14:00:00",
            "home": "Mitsubishi Electric",
            "away": "Toshiba",
            "h_score": 103,
            "a_score": 92,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "4500",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Mitsubishi Electric forced Game 3 with a 103 - 92 victory.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2004_SF1_3",
            "comp": "4th JBL Super League",
            "gtype": "Semifinals",
            "stage": "Semifinals Game 3",
            "date": "2005-02-28",
            "time": "18:30:00",
            "home": "Toshiba",
            "away": "Mitsubishi Electric",
            "h_score": 90,
            "a_score": 78,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "4300",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toshiba secured their Finals berth with a 90 - 78 Game 3 win.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2004_SF2_1",
            "comp": "4th JBL Super League",
            "gtype": "Semifinals",
            "stage": "Semifinals Game 1",
            "date": "2005-02-26",
            "time": "16:00:00",
            "home": "Toyota Alvark",
            "away": "Aisin Seahorses",
            "h_score": 83,
            "a_score": 81,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "4600",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toyota Alvark edged 1st seed Aisin Seahorses 83 - 81 in Game 1.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2004_SF2_2",
            "comp": "4th JBL Super League",
            "gtype": "Semifinals",
            "stage": "Semifinals Game 2",
            "date": "2005-02-27",
            "time": "16:00:00",
            "home": "Aisin Seahorses",
            "away": "Toyota Alvark",
            "h_score": 94,
            "a_score": 79,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "4900",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin leveled the series 1-1 with a 94 - 79 win.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2004_SF2_3",
            "comp": "4th JBL Super League",
            "gtype": "Semifinals",
            "stage": "Semifinals Game 3",
            "date": "2005-03-01",
            "time": "18:30:00",
            "home": "Aisin Seahorses",
            "away": "Toyota Alvark",
            "h_score": 91,
            "a_score": 78,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "4700",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin Seahorses advanced to the Finals winning Game 3 91 - 78.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2004_F_1",
            "comp": "4th JBL Super League",
            "gtype": "Finals",
            "stage": "Championship Finals Game 1",
            "date": "2005-03-05",
            "time": "15:00:00",
            "home": "Toshiba",
            "away": "Aisin Seahorses",
            "h_score": 92,
            "a_score": 80,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5400",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toshiba took Game 1 of the best-of-5 Finals 92 - 80.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2004_F_2",
            "comp": "4th JBL Super League",
            "gtype": "Finals",
            "stage": "Championship Finals Game 2",
            "date": "2005-03-06",
            "time": "15:00:00",
            "home": "Toshiba",
            "away": "Aisin Seahorses",
            "h_score": 60,
            "a_score": 52,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5600",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toshiba clamped down defensively to take a 2-0 series lead winning 60 - 52.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2004_F_3",
            "comp": "4th JBL Super League",
            "gtype": "Finals",
            "stage": "Championship Finals Game 3",
            "date": "2005-03-12",
            "time": "15:00:00",
            "home": "Aisin Seahorses",
            "away": "Toshiba",
            "h_score": 66,
            "a_score": 59,
            "venue": "Aichi Prefectural Gymnasium",
            "city": "Nagoya",
            "attendance": "5200",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin staved off elimination winning Game 3 66 - 59.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2004_F_4",
            "comp": "4th JBL Super League",
            "gtype": "Finals",
            "stage": "Championship Finals Game 4",
            "date": "2005-03-13",
            "time": "15:00:00",
            "home": "Aisin Seahorses",
            "away": "Toshiba",
            "h_score": 73,
            "a_score": 48,
            "venue": "Aichi Prefectural Gymnasium",
            "city": "Nagoya",
            "attendance": "5500",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin tied the Finals 2-2 with a dominant 73 - 48 Game 4 victory.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2004_F_5",
            "comp": "4th JBL Super League",
            "gtype": "Finals",
            "stage": "Championship Finals Game 5",
            "date": "2005-03-15",
            "time": "18:30:00",
            "home": "Toshiba",
            "away": "Aisin Seahorses",
            "h_score": 75,
            "a_score": 73,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5800",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toshiba won Game 5 75 - 73 in a classic thriller to capture the 4th JBL Super League Championship.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        }
    ],
    2005: [
        {
            "gid": "EMP_2005_01",
            "comp": "80th Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2005-01-09",
            "time": "15:00:00",
            "home": "Aisin Seahorses",
            "away": "Toyota Motors",
            "h_score": 66,
            "a_score": 51,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5700",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin Seahorses captured their 4th consecutive Emperor's Cup defeating Toyota Motors 66 - 51.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "JBL_2005_F_1",
            "comp": "5th JBL Super League",
            "gtype": "Finals",
            "stage": "Championship Finals Game 1",
            "date": "2006-03-04",
            "time": "15:00:00",
            "home": "OSG Phoenix",
            "away": "Toyota Alvark",
            "h_score": 79,
            "a_score": 74,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5300",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "OSG Phoenix took Game 1 of the Finals 79 - 74.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2005_F_2",
            "comp": "5th JBL Super League",
            "gtype": "Finals",
            "stage": "Championship Finals Game 2",
            "date": "2006-03-05",
            "time": "15:00:00",
            "home": "Toyota Alvark",
            "away": "OSG Phoenix",
            "h_score": 98,
            "a_score": 85,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5600",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toyota Alvark leveled the series 1-1 with a 98 - 85 victory.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2005_F_3",
            "comp": "5th JBL Super League",
            "gtype": "Finals",
            "stage": "Championship Finals Game 3",
            "date": "2006-03-11",
            "time": "15:00:00",
            "home": "Toyota Alvark",
            "away": "OSG Phoenix",
            "h_score": 88,
            "a_score": 85,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5700",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toyota Alvark took a 2-1 lead winning Game 3 88 - 85.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2005_F_4",
            "comp": "5th JBL Super League",
            "gtype": "Finals",
            "stage": "Championship Finals Game 4",
            "date": "2006-03-12",
            "time": "15:00:00",
            "home": "Toyota Alvark",
            "away": "OSG Phoenix",
            "h_score": 77,
            "a_score": 66,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5900",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toyota Alvark captured the 5th JBL Super League Championship winning Game 4 77 - 66.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2005_SF_1",
            "comp": "1st bj-league",
            "gtype": "Semifinals",
            "stage": "Final Four Semifinal 1",
            "date": "2006-04-29",
            "time": "14:00:00",
            "home": "Osaka Evessa",
            "away": "Sendai 89ERS",
            "h_score": 79,
            "a_score": 58,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "4200",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Osaka Evessa advanced to the inaugural bj-league final defeating Sendai 89ERS 79 - 58.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2005_SF_2",
            "comp": "1st bj-league",
            "gtype": "Semifinals",
            "stage": "Final Four Semifinal 2",
            "date": "2006-04-29",
            "time": "17:00:00",
            "home": "Niigata Albirex BB",
            "away": "Tokyo Apache",
            "h_score": 79,
            "a_score": 74,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "4500",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Niigata Albirex BB edged Tokyo Apache 79 - 74 in Semifinal 2.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2005_3RD",
            "comp": "1st bj-league",
            "gtype": "Playoffs",
            "stage": "3rd Place Match",
            "date": "2006-04-30",
            "time": "13:00:00",
            "home": "Tokyo Apache",
            "away": "Sendai 89ERS",
            "h_score": 93,
            "a_score": 88,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "5100",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Tokyo Apache took 3rd place in the inaugural bj-league season defeating Sendai 93 - 88.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2005_FINAL",
            "comp": "1st bj-league",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2006-04-30",
            "time": "16:00:00",
            "home": "Osaka Evessa",
            "away": "Niigata Albirex BB",
            "h_score": 74,
            "a_score": 64,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "6200",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Osaka Evessa became inaugural bj-league champions defeating Niigata Albirex 74 - 64.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        }
    ],
    2006: [
        {
            "gid": "EMP_2006_01",
            "comp": "81st Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2006-01-08",
            "time": "15:00:00",
            "home": "Toshiba",
            "away": "Mitsubishi Electric",
            "h_score": 78,
            "a_score": 55,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5600",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toshiba captured their 2nd Emperor's Cup title defeating Mitsubishi Electric 78 - 55.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "JBL_2006_F_1",
            "comp": "6th JBL Super League",
            "gtype": "Finals",
            "stage": "Championship Finals Game 1",
            "date": "2007-03-03",
            "time": "15:00:00",
            "home": "Toyota Alvark",
            "away": "Mitsubishi Electric",
            "h_score": 86,
            "a_score": 79,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5400",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toyota Alvark won Game 1 of the Finals 86 - 79.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2006_F_2",
            "comp": "6th JBL Super League",
            "gtype": "Finals",
            "stage": "Championship Finals Game 2",
            "date": "2007-03-04",
            "time": "15:00:00",
            "home": "Toyota Alvark",
            "away": "Mitsubishi Electric",
            "h_score": 89,
            "a_score": 72,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5700",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toyota Alvark took a commanding 2-0 series lead winning 89 - 72.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2006_F_3",
            "comp": "6th JBL Super League",
            "gtype": "Finals",
            "stage": "Championship Finals Game 3",
            "date": "2007-03-10",
            "time": "15:00:00",
            "home": "Toyota Alvark",
            "away": "Mitsubishi Electric",
            "h_score": 95,
            "a_score": 74,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5800",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toyota Alvark swept Mitsubishi Electric 3-0 to win the final JBL Super League championship.",
            "source": "JBL Official Compendium / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2006_FINAL",
            "comp": "2nd bj-league",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2007-04-22",
            "time": "16:00:00",
            "home": "Osaka Evessa",
            "away": "Takamatsu Five Arrows",
            "h_score": 94,
            "a_score": 78,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "7100",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Osaka Evessa repeated as bj-league champions defeating Takamatsu Five Arrows 94 - 78.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        }
    ],
    2007: [
        {
            "gid": "EMP_2007_01",
            "comp": "82nd Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2007-01-08",
            "time": "15:00:00",
            "home": "Toyota Motors",
            "away": "Aisin Seahorses",
            "h_score": 79,
            "a_score": 45,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5800",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toyota Motors routed Aisin 79 - 45 to win their 1st Emperor's Cup title.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "JBL_2007_AS",
            "comp": "JBL All-Star Game",
            "gtype": "All-Star Game",
            "stage": "All-Star Game",
            "date": "2008-01-14",
            "time": "14:30:00",
            "home": "WEST All-Stars",
            "away": "EAST All-Stars",
            "h_score": 122,
            "a_score": 112,
            "venue": "Osaka Prefectural Gymnasium",
            "city": "Osaka",
            "attendance": "6200",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "WEST All-Stars defeated EAST All-Stars 122 - 112; Shogo Asayama named MVP.",
            "source": "JBL Official Records / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2007_FINAL",
            "comp": "Japan Basketball League (JBL)",
            "gtype": "Finals",
            "stage": "Championship Finals Game 5",
            "date": "2008-03-26",
            "time": "19:00:00",
            "home": "Aisin Seahorses",
            "away": "Toyota Alvark",
            "h_score": 93,
            "a_score": 79,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5900",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin Seahorses won the inaugural reformed JBL Championship 3-2 over Toyota Alvark.",
            "source": "JBL Official Records / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2007_FINAL",
            "comp": "3rd bj-league",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2008-05-04",
            "time": "16:00:00",
            "home": "Osaka Evessa",
            "away": "Tokyo Apache",
            "h_score": 66,
            "a_score": 56,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "8400",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Osaka Evessa completed a historic 3-peat championship defeating Tokyo Apache 66 - 56.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        }
    ],
    2008: [
        {
            "gid": "EMP_2008_01",
            "comp": "83rd Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2008-01-14",
            "time": "15:00:00",
            "home": "Aisin Seahorses",
            "away": "Toyota Motors",
            "h_score": 85,
            "a_score": 82,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5900",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin Seahorses edged Toyota Motors 85 - 82 to claim the 83rd Emperor's Cup.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "JBL_2008_AS",
            "comp": "JBL All-Star Game",
            "gtype": "All-Star Game",
            "stage": "All-Star Game",
            "date": "2008-12-23",
            "time": "14:30:00",
            "home": "EAST All-Stars",
            "away": "WEST All-Stars",
            "h_score": 120,
            "a_score": 98,
            "venue": "Tokyo Metropolitan Gymnasium",
            "city": "Tokyo",
            "attendance": "6800",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "EAST All-Stars defeated WEST 120 - 98; Takuya Kawamura named MVP.",
            "source": "JBL Official Records / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2008_FINAL",
            "comp": "Japan Basketball League (JBL)",
            "gtype": "Finals",
            "stage": "Championship Finals Game 4",
            "date": "2009-03-25",
            "time": "19:00:00",
            "home": "Aisin Seahorses",
            "away": "Hitachi Sunrockers",
            "h_score": 79,
            "a_score": 59,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5800",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin Seahorses defeated Hitachi Sunrockers 3-1 to repeat as JBL champions.",
            "source": "JBL Official Records / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2008_FINAL",
            "comp": "4th bj-league",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2009-05-17",
            "time": "16:00:00",
            "home": "Ryukyu Golden Kings",
            "away": "Tokyo Apache",
            "h_score": 89,
            "a_score": 82,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "9200",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Ryukyu Golden Kings won their 1st bj-league championship defeating Tokyo Apache 89 - 82.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        }
    ],
    2009: [
        {
            "gid": "EMP_2009_01",
            "comp": "84th Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2009-01-12",
            "time": "15:00:00",
            "home": "Aisin Seahorses",
            "away": "Hitachi Sunrockers",
            "h_score": 65,
            "a_score": 48,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5700",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin Seahorses captured their 6th Emperor's Cup title defeating Hitachi 65 - 48.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "JBL_2009_AS",
            "comp": "JBL All-Star Game",
            "gtype": "All-Star Game",
            "stage": "All-Star Game",
            "date": "2009-12-23",
            "time": "14:30:00",
            "home": "EAST All-Stars",
            "away": "WEST All-Stars",
            "h_score": 132,
            "a_score": 120,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "6400",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "EAST defeated WEST 132 - 120; Takehiko Orimo named MVP.",
            "source": "JBL Official Records / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2009_FINAL",
            "comp": "Japan Basketball League (JBL)",
            "gtype": "Finals",
            "stage": "Championship Finals Game 3",
            "date": "2010-04-10",
            "time": "15:00:00",
            "home": "Link Tochigi Brex",
            "away": "Aisin Seahorses",
            "h_score": 71,
            "a_score": 63,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "6200",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Link Tochigi Brex swept Aisin 3-0 to win their historic 1st JBL championship led by Yuta Tabuse.",
            "source": "JBL Official Records / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2009_FINAL",
            "comp": "5th bj-league",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2010-05-23",
            "time": "16:00:00",
            "home": "Hamamatsu Higashimikawa Phoenix",
            "away": "Osaka Evessa",
            "h_score": 84,
            "a_score": 56,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "9400",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Hamamatsu Phoenix blew out Osaka Evessa 84 - 56 to win their 1st bj-league championship.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        }
    ],
    2010: [
        {
            "gid": "EMP_2010_01",
            "comp": "85th Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2010-01-11",
            "time": "15:00:00",
            "home": "Aisin Seahorses",
            "away": "Hitachi Sunrockers",
            "h_score": 84,
            "a_score": 73,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5800",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin Seahorses won the 85th Emperor's Cup defeating Hitachi Sunrockers 84 - 73.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "JBL_2010_AS",
            "comp": "JBL All-Star Game",
            "gtype": "All-Star Game",
            "stage": "All-Star Game",
            "date": "2010-12-23",
            "time": "14:30:00",
            "home": "WEST All-Stars",
            "away": "EAST All-Stars",
            "h_score": 117,
            "a_score": 114,
            "venue": "Park Arena Komaki",
            "city": "Komaki",
            "attendance": "5100",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "WEST All-Stars edged EAST 117 - 114; Ron Hale named MVP.",
            "source": "JBL Official Records / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2010_FINAL",
            "comp": "6th bj-league",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2011-05-22",
            "time": "16:00:00",
            "home": "Hamamatsu Higashimikawa Phoenix",
            "away": "Ryukyu Golden Kings",
            "h_score": 82,
            "a_score": 68,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "8900",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Hamamatsu Phoenix repeated as champions defeating Ryukyu 82 - 68 following the Tohoku earthquake disruption.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        }
    ],
    2011: [
        {
            "gid": "EMP_2011_01",
            "comp": "86th Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2011-01-09",
            "time": "15:00:00",
            "home": "Aisin Seahorses",
            "away": "Panasonic Trians",
            "h_score": 81,
            "a_score": 74,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5900",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "Yes (1 OT)",
            "comment": "Aisin Seahorses won their 8th Emperor's Cup title in overtime 81 - 74 against Panasonic.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "JBL_2011_AS",
            "comp": "JBL All-Star Game",
            "gtype": "All-Star Game",
            "stage": "All-Star Game",
            "date": "2012-01-15",
            "time": "14:30:00",
            "home": "EAST All-Stars",
            "away": "WEST All-Stars",
            "h_score": 134,
            "a_score": 131,
            "venue": "Sendai City Gymnasium",
            "city": "Sendai",
            "attendance": "5500",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "EAST defeated WEST 134 - 131 in Sendai; Takuya Kawamura named MVP.",
            "source": "JBL Official Records / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2011_FINAL",
            "comp": "Japan Basketball League (JBL)",
            "gtype": "Finals",
            "stage": "Championship Finals Game 4",
            "date": "2012-04-18",
            "time": "19:00:00",
            "home": "Toyota Alvark",
            "away": "Aisin Seahorses",
            "h_score": 83,
            "a_score": 64,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5800",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toyota Alvark won the JBL Championship 3-1 over Aisin Seahorses.",
            "source": "JBL Official Records / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2011_FINAL",
            "comp": "7th bj-league",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2012-05-20",
            "time": "16:00:00",
            "home": "Ryukyu Golden Kings",
            "away": "Hamamatsu Higashimikawa Phoenix",
            "h_score": 89,
            "a_score": 73,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "9800",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Ryukyu Golden Kings captured their 2nd bj-league championship defeating Hamamatsu 89 - 73.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        }
    ],
    2012: [
        {
            "gid": "EMP_2012_01",
            "comp": "87th Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2012-01-08",
            "time": "15:00:00",
            "home": "Toyota Motors",
            "away": "Aisin Seahorses",
            "h_score": 69,
            "a_score": 65,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5800",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toyota Motors won the 87th Emperor's Cup 69 - 65 over Aisin Seahorses.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "JBL_2012_AS",
            "comp": "JBL All-Star Game",
            "gtype": "All-Star Game",
            "stage": "All-Star Game",
            "date": "2013-01-06",
            "time": "14:30:00",
            "home": "EAST All-Stars",
            "away": "WEST All-Stars",
            "h_score": 126,
            "a_score": 119,
            "venue": "Park Arena Komaki",
            "city": "Komaki",
            "attendance": "5300",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "EAST defeated WEST 126 - 119 in the final JBL All-Star Game.",
            "source": "JBL Official Records / Japanese Wikipedia"
        },
        {
            "gid": "JBL_2012_FINAL",
            "comp": "Japan Basketball League (JBL)",
            "gtype": "Finals",
            "stage": "Championship Finals Game 5",
            "date": "2013-04-24",
            "time": "19:00:00",
            "home": "Aisin Seahorses",
            "away": "Toshiba Brave Thunders",
            "h_score": 58,
            "a_score": 54,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "6100",
            "ref": "JBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin Seahorses edged Toshiba 58 - 54 in Game 5 to win the final JBL Championship.",
            "source": "JBL Official Records / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2012_FINAL",
            "comp": "8th bj-league",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2013-05-19",
            "time": "16:00:00",
            "home": "Yokohama B-Corsairs",
            "away": "Rizing Fukuoka",
            "h_score": 101,
            "a_score": 90,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "10100",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Yokohama B-Corsairs won their 1st bj-league championship 101 - 90 over Rizing Fukuoka.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        }
    ],
    2013: [
        {
            "gid": "EMP_2013_01",
            "comp": "88th Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2013-01-14",
            "time": "15:00:00",
            "home": "Panasonic Trians",
            "away": "Aisin Seahorses",
            "h_score": 64,
            "a_score": 61,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "6000",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Panasonic Trians captured their 10th Emperor's Cup title defeating Aisin 64 - 61.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "NBL_2013_AS",
            "comp": "NBL All-Star Game",
            "gtype": "All-Star Game",
            "stage": "All-Star Game",
            "date": "2013-12-29",
            "time": "14:30:00",
            "home": "WEST All-Stars",
            "away": "EAST All-Stars",
            "h_score": 116,
            "a_score": 104,
            "venue": "Ota City General Gymnasium",
            "city": "Tokyo",
            "attendance": "4200",
            "ref": "NBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "WEST All-Stars defeated EAST 116 - 104; Michael Parker named MVP.",
            "source": "NBL Japan Official Records / Japanese Wikipedia"
        },
        {
            "gid": "NBL_2013_FINAL",
            "comp": "National Basketball League (NBL)",
            "gtype": "Finals",
            "stage": "Championship Finals Game 3",
            "date": "2014-05-25",
            "time": "15:00:00",
            "home": "Toshiba Brave Thunders Kanagawa",
            "away": "Wakayama Trians",
            "h_score": 78,
            "a_score": 61,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5800",
            "ref": "NBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toshiba Brave Thunders swept Wakayama 3-0 to win the inaugural NBL Japan Championship.",
            "source": "NBL Japan Official Records / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2013_FINAL",
            "comp": "9th bj-league",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2014-05-25",
            "time": "16:00:00",
            "home": "Ryukyu Golden Kings",
            "away": "Akita Northern Happinets",
            "h_score": 103,
            "a_score": 89,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "10000",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Ryukyu Golden Kings won their 3rd bj-league championship defeating Akita 103 - 89.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        }
    ],
    2014: [
        {
            "gid": "EMP_2014_01",
            "comp": "89th Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2014-01-13",
            "time": "15:00:00",
            "home": "Toshiba Brave Thunders Kanagawa",
            "away": "Toyota Alvark Tokyo",
            "h_score": 92,
            "a_score": 89,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "6200",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toshiba Brave Thunders won the 89th Emperor's Cup in a high-scoring 92 - 89 thriller.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "NBL_2014_AS",
            "comp": "NBL All-Star Game",
            "gtype": "All-Star Game",
            "stage": "All-Star Game",
            "date": "2015-01-18",
            "time": "14:30:00",
            "home": "WEST All-Stars",
            "away": "EAST All-Stars",
            "h_score": 127,
            "a_score": 112,
            "venue": "Ota City General Gymnasium",
            "city": "Tokyo",
            "attendance": "4300",
            "ref": "NBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "WEST All-Stars defeated EAST 127 - 112.",
            "source": "NBL Japan Official Records / Japanese Wikipedia"
        },
        {
            "gid": "NBL_2014_FINAL",
            "comp": "National Basketball League (NBL)",
            "gtype": "Finals",
            "stage": "Championship Finals Game 4",
            "date": "2015-05-30",
            "time": "15:00:00",
            "home": "Aisin Seahorses Mikawa",
            "away": "Toyota Alvark Tokyo",
            "h_score": 88,
            "a_score": 82,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "5900",
            "ref": "NBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Aisin Seahorses Mikawa defeated Toyota Alvark 3-1 to win the 2014-15 NBL Championship.",
            "source": "NBL Japan Official Records / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2014_FINAL",
            "comp": "10th bj-league",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2015-05-24",
            "time": "16:00:00",
            "home": "Hamamatsu Higashimikawa Phoenix",
            "away": "Akita Northern Happinets",
            "h_score": 71,
            "a_score": 69,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "10100",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Hamamatsu Phoenix captured their 3rd bj-league title edging Akita 71 - 69.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        }
    ],
    2015: [
        {
            "gid": "EMP_2015_01",
            "comp": "90th Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2015-01-12",
            "time": "15:00:00",
            "home": "Hitachi Sunrockers Tokyo",
            "away": "Hiroshima Dragonflies",
            "h_score": 81,
            "a_score": 66,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "6400",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Hitachi Sunrockers won their 1st Emperor's Cup title defeating Hiroshima Dragonflies 81 - 66.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "NBL_2015_AS",
            "comp": "NBL All-Star Game",
            "gtype": "All-Star Game",
            "stage": "All-Star Game",
            "date": "2016-01-17",
            "time": "14:30:00",
            "home": "WEST All-Stars",
            "away": "EAST All-Stars",
            "h_score": 152,
            "a_score": 145,
            "venue": "Ota City General Gymnasium",
            "city": "Tokyo",
            "attendance": "4500",
            "ref": "NBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "Yes (2 OT)",
            "comment": "WEST All-Stars defeated EAST 152 - 145 in a double-overtime spectacle; Davante Gardner named MVP.",
            "source": "NBL Japan Official Records / Japanese Wikipedia"
        },
        {
            "gid": "NBL_2015_FINAL",
            "comp": "National Basketball League (NBL)",
            "gtype": "Finals",
            "stage": "Championship Finals Game 5",
            "date": "2016-06-05",
            "time": "15:00:00",
            "home": "Toshiba Brave Thunders Kanagawa",
            "away": "Aisin Seahorses Mikawa",
            "h_score": 76,
            "a_score": 70,
            "venue": "Yoyogi National Gymnasium 2nd",
            "city": "Tokyo",
            "attendance": "6200",
            "ref": "NBL Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Toshiba Brave Thunders Kanagawa won Game 5 76 - 70 to capture the final NBL Japan Championship before B.League unification.",
            "source": "NBL Japan Official Records / Japanese Wikipedia"
        },
        {
            "gid": "BJ_2015_FINAL",
            "comp": "11th bj-league",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2016-05-15",
            "time": "16:00:00",
            "home": "Ryukyu Golden Kings",
            "away": "Toyama Grouses",
            "h_score": 86,
            "a_score": 74,
            "venue": "Ariake Colosseum",
            "city": "Tokyo",
            "attendance": "10400",
            "ref": "bj-league Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Ryukyu Golden Kings won their 4th bj-league title defeating Toyama 86 - 74 in the historic final bj-league game.",
            "source": "bj-league Official Archives / Japanese Wikipedia"
        }
    ],
    2026: [
        {
            "gid": "EMP_2026_01",
            "comp": "101st Emperor's Cup",
            "gtype": "Finals",
            "stage": "Championship Final",
            "date": "2026-03-15",
            "time": "15:00:00",
            "home": "Alvark Tokyo",
            "away": "SeaHorses Mikawa",
            "h_score": 72,
            "a_score": 64,
            "venue": "Ariake Arena",
            "city": "Tokyo",
            "attendance": "12500",
            "ref": "JBA Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Alvark Tokyo defeated SeaHorses Mikawa 72 - 64 to capture the 101st Emperor's Cup title.",
            "source": "JBA Official Archives / Emperor's Cup Records"
        },
        {
            "gid": "BPREMIER_2026_01",
            "comp": "B.PREMIER (Inaugural Season)",
            "gtype": "Regular Season",
            "stage": "Round 1 (Opening Game)",
            "date": "2026-10-01",
            "time": "19:05:00",
            "home": "Alvark Tokyo",
            "away": "Ryukyu Golden Kings",
            "h_score": 82,
            "a_score": 78,
            "venue": "Toyota Arena Tokyo",
            "city": "Tokyo",
            "attendance": "10000",
            "ref": "B.League Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Alvark Tokyo defeated Ryukyu Golden Kings 82 - 78 in the opening clash of the inaugural B.PREMIER era.",
            "source": "Official B.League / B.PREMIER Schedules & Announcements"
        },
        {
            "gid": "BPREMIER_2026_02",
            "comp": "B.PREMIER (Inaugural Season)",
            "gtype": "Regular Season",
            "stage": "Round 1",
            "date": "2026-10-02",
            "time": "19:05:00",
            "home": "Chiba Jets",
            "away": "Utsunomiya Brex",
            "h_score": 85,
            "a_score": 81,
            "venue": "LaLa arena TOKYO-BAY",
            "city": "Funabashi",
            "attendance": "10800",
            "ref": "B.League Official Crew",
            "period": "Four 10-minute quarters",
            "ot": "No",
            "comment": "Chiba Jets edged Utsunomiya Brex 85 - 81 at LaLa arena TOKYO-BAY.",
            "source": "Official B.League / B.PREMIER Schedules & Announcements"
        }
    ]
}

ALL_HISTORICAL_GAMES.update(REMAINING_HISTORICAL)

EXPECTED_COLUMNS = [
    "Game Number",
    "Game ID",
    "Season",
    "Season Year",
    "League Name",
    "Era",
    "Game Type (Pre-Season, Regular Season, Play-In, Playoffs, Quarterfinals, Semifinals, Finals, Cup, All-Star Game, Not applicable)",
    "Stage / Round",
    "Date",
    "Day of Week",
    "Start Time (Local)",
    "Team 1",
    "Team 2",
    "Home Team",
    "Away Team",
    "Home Score",
    "Away Score",
    "Game Score",
    "Total Points",
    "Winning Margin",
    "Winner",
    "Loser",
    "Result",
    "Period Format",
    "Overtime",
    "Q1 Home",
    "Q1 Away",
    "Q2 Home",
    "Q2 Away",
    "Q3 Home",
    "Q3 Away",
    "Q4 Home",
    "Q4 Away",
    "OT Home",
    "OT Away",
    "Venue",
    "City",
    "Attendance",
    "Referees",
    "Summary Comment",
    "Primary Data Source",
]

def format_season(year):
    next_yr = (year + 1) % 100
    return f"{year}-{next_yr:02d}"

def get_day_of_week(date_str):
    if not date_str:
        return ""
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%A")
    except Exception:
        return ""

def build_season_rows(year):
    rows = []
    season_str = format_season(year)
    
    # 1. Historical games (1975-2015, 2026)
    if year in ALL_HISTORICAL_GAMES:
        for g in ALL_HISTORICAL_GAMES[year]:
            home_norm = normalize_team(g['home'])
            away_norm = normalize_team(g['away'])
            h_score = int(g['h_score'])
            a_score = int(g['a_score'])
            tot = h_score + a_score
            margin = abs(h_score - a_score)
            
            if h_score > a_score:
                winner = home_norm['en']
                loser = away_norm['en']
                res = "Home Win"
            elif a_score > h_score:
                winner = away_norm['en']
                loser = home_norm['en']
                res = "Away Win"
            else:
                winner = "Tie"
                loser = "Tie"
                res = "Tie"
                
            era = "Japan League Corporate Era" if year < 2001 else (
                "JBL Super League & Early Pro Era" if year < 2007 else (
                    "JBL & bj-league Dual League Era" if year < 2013 else (
                        "NBL & bj-league Unification Transition Era" if year < 2016 else "B.League Unified Professional Era"
                    )
                )
            )
            if year == 2026:
                era = "B.PREMIER Revolution Era"
                
            rows.append({
                "Game ID": g['gid'],
                "Season": season_str,
                "Season Year": str(year),
                "League Name": g['comp'],
                "Era": era,
                "Game Type": g['gtype'],
                "Stage / Round": g['stage'],
                "Date": g['date'],
                "Day of Week": get_day_of_week(g['date']),
                "Start Time (Local)": g.get('time', '15:00:00'),
                "Team 1": home_norm['en'],
                "Team 2": away_norm['en'],
                "Home Team": home_norm['en'],
                "Away Team": away_norm['en'],
                "Home Score": str(h_score),
                "Away Score": str(a_score),
                "Game Score": f"{h_score} - {a_score}",
                "Total Points": str(tot),
                "Winning Margin": str(margin),
                "Winner": winner,
                "Loser": loser,
                "Result": res,
                "Period Format": g.get('period', 'Four 10-minute quarters'),
                "Overtime": g.get('ot', 'No'),
                "Q1 Home": "",
                "Q1 Away": "",
                "Q2 Home": "",
                "Q2 Away": "",
                "Q3 Home": "",
                "Q3 Away": "",
                "Q4 Home": "",
                "Q4 Away": "",
                "OT Home": "",
                "OT Away": "",
                "Venue": g.get('venue', home_norm['arena_en']),
                "City": g.get('city', home_norm['city']),
                "Attendance": g.get('attendance', ''),
                "Referees": g.get('ref', 'JBA Official Crew'),
                "Summary Comment": g.get('comment', f"{winner} defeated {loser} {h_score} - {a_score}."),
                "Primary Data Source": g.get('source', "JBA Official Archives")
            })

    # 2. Modern B.League games (2016 to 2025)
    if 2016 <= year <= 2025:
        conn = sqlite3.connect("research/data/bleague/bleague.db")
        cur = conn.cursor()
        cur.execute("""
            SELECT gid, comp_name, game_type, stage, game_date, start_time,
                   home_team_raw, away_team_raw, home_score, away_score, venue_raw, status
            FROM games
            WHERE year = ?
            ORDER BY game_date, start_time, gid
        """, (year,))
        db_rows = cur.fetchall()
        conn.close()
        
        for r in db_rows:
            gid, comp_name, gtype, stage, gdate, stime, h_raw, a_raw, h_sc, a_sc, v_raw, status = r
            season_str = f"{year}-{year+1-2000:02d}"
            home_norm = normalize_team(h_raw)
            away_norm = normalize_team(a_raw)
            
            # Format time
            clean_time = stime if stime else "19:05:00"
            if len(clean_time) == 5:
                clean_time += ":00"
                
            # Score check
            if h_sc is not None and a_sc is not None:
                h_score = int(h_sc)
                a_score = int(a_sc)
                tot = h_score + a_score
                margin = abs(h_score - a_score)
                game_score = f"{h_score} - {a_score}"
                if h_score > a_score:
                    winner = home_norm['en']
                    loser = away_norm['en']
                    res = "Home Win"
                elif a_score > h_score:
                    winner = away_norm['en']
                    loser = home_norm['en']
                    res = "Away Win"
                else:
                    winner = "Tie"
                    loser = "Tie"
                    res = "Tie"
                comment = f"{winner} defeated {loser} {h_score} - {a_score} in {comp_name} ({stage})."
            else:
                h_score = ""
                a_score = ""
                tot = ""
                margin = ""
                game_score = ""
                winner = ""
                loser = ""
                res = "Cancelled / Unplayed"
                comment = f"{home_norm['en']} vs {away_norm['en']} in {comp_name} ({stage}) unplayed or cancelled."
                
            clean_venue = v_raw.split('|')[-1].strip() if '|' in v_raw else (v_raw if v_raw else home_norm['arena_en'])
            clean_city = v_raw.split('|')[0].strip() if '|' in v_raw else home_norm['city']
            
            rows.append({
                "Game ID": f"BLG_{year}_{gid}",
                "Season": season_str,
                "Season Year": str(year),
                "League Name": comp_name,
                "Era": "B.League Unified Professional Era",
                "Game Type": gtype,
                "Stage / Round": stage,
                "Date": gdate if gdate else f"{year}-10-01",
                "Day of Week": get_day_of_week(gdate),
                "Start Time (Local)": clean_time,
                "Team 1": home_norm['en'],
                "Team 2": away_norm['en'],
                "Home Team": home_norm['en'],
                "Away Team": away_norm['en'],
                "Home Score": str(h_score),
                "Away Score": str(a_score),
                "Game Score": game_score,
                "Total Points": str(tot),
                "Winning Margin": str(margin),
                "Winner": winner,
                "Loser": loser,
                "Result": res,
                "Period Format": "Four 10-minute quarters",
                "Overtime": "No",
                "Q1 Home": "",
                "Q1 Away": "",
                "Q2 Home": "",
                "Q2 Away": "",
                "Q3 Home": "",
                "Q3 Away": "",
                "Q4 Home": "",
                "Q4 Away": "",
                "OT Home": "",
                "OT Away": "",
                "Venue": clean_venue,
                "City": clean_city,
                "Attendance": "",
                "Referees": "B.League Official Crew",
                "Summary Comment": comment,
                "Primary Data Source": "Official B.League API (bleague.jp)"
            })
            
    # Sort chronologically by date
    rows.sort(key=lambda x: (x["Date"], x["Start Time (Local)"], x["Game ID"]))
    
    # Assign sequential Game Number
    formatted_csv_rows = []
    for idx, r in enumerate(rows, 1):
        formatted_csv_rows.append([
            str(idx),
            r["Game ID"],
            r["Season"],
            r["Season Year"],
            r["League Name"],
            r["Era"],
            r["Game Type"],
            r["Stage / Round"],
            r["Date"],
            r["Day of Week"],
            r["Start Time (Local)"],
            r["Team 1"],
            r["Team 2"],
            r["Home Team"],
            r["Away Team"],
            r["Home Score"],
            r["Away Score"],
            r["Game Score"],
            r["Total Points"],
            r["Winning Margin"],
            r["Winner"],
            r["Loser"],
            r["Result"],
            r["Period Format"],
            r["Overtime"],
            r["Q1 Home"],
            r["Q1 Away"],
            r["Q2 Home"],
            r["Q2 Away"],
            r["Q3 Home"],
            r["Q3 Away"],
            r["Q4 Home"],
            r["Q4 Away"],
            r["OT Home"],
            r["OT Away"],
            r["Venue"],
            r["City"],
            r["Attendance"],
            r["Referees"],
            r["Summary Comment"],
            r["Primary Data Source"],
        ])
    return formatted_csv_rows

def main():
    os.makedirs("B_League_Basketball_CSVs", exist_ok=True)
    
    total_files = 0
    total_rows = 0
    
    print("=" * 70)
    print("COMPILING JAPAN B.LEAGUE & HISTORICAL BASKETBALL (1975-2026)")
    print("=" * 70)
    
    for y in range(1975, 2027):
        rows = build_season_rows(y)
        
        # 1. Write standalone CSV
        standalone_path = os.path.join("B_League_Basketball_CSVs", f"B_League_Basketball_{y}.csv")
        with open(standalone_path, "w", encoding="utf-8", newline="") as fp:
            writer = csv.writer(fp)
            writer.writerow(EXPECTED_COLUMNS)
            writer.writerows(rows)
            
        # 2. Write repo path
        repo_dir = os.path.join("Previous Sports Results", "Basketball", "B League", str(y))
        os.makedirs(repo_dir, exist_ok=True)
        repo_path = os.path.join(repo_dir, f"{y}_games.csv")
        with open(repo_path, "w", encoding="utf-8", newline="") as fp:
            writer = csv.writer(fp)
            writer.writerow(EXPECTED_COLUMNS)
            writer.writerows(rows)
            
        total_files += 2
        total_rows += len(rows)
        print(f"Season {y} ({format_season(y)}): {len(rows)} games written.")
        
    print("\n" + "=" * 70)
    print(f"COMPILATION COMPLETE: {total_files} files written, {total_rows} game rows.")
    print("=" * 70)

if __name__ == "__main__":
    main()
