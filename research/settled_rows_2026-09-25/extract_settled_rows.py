"""Extract every graded ranked row from the combined prediction logs (Parts 1–5) into one dataset.

Added 2026-09-25(d). LEARNING_ONLY: a descriptive dataset of the framework's own settled rows.
It is for diagnostics and prospective-test design, and never a source of fitted forecasting
coefficients (L-087).

Method:
1. **Rank tables.** A Markdown table with a "Rank" column. A table with a result-bearing column
   (Result / Operator settlement / Settlement / Outcome / Realised) contributes graded rows. A
   table with a probability column and no result contributes an issue-time probability lookup.
2. **Card attribution.** First, the nearest non-table line within 8 lines above the table that
   names exactly one card ID (P-### or TMP-...). Otherwise, the current heading's ID, but only if
   that heading names exactly one ID and is not an umbrella or range heading ("P-318–P-332
   imported", "Queue … before P-090", "Component import …"). Rows that can't be attributed are
   dropped and counted.
3. **Probability.** The graded table's `p` / probability / "Issued p" column, taking its first
   number (percentages divided by 100). If absent, the issue-time lookup for the same
   (card, rank) is used, but only when normalized contract text matches exactly.
4. **Duplicates.** Conflicting occurrences are quarantined. Exact-identical repeats are represented
   once with every source location retained. No "last occurrence wins" rule is used.
5. **Sport.** Classified from the canonical event name in GAME_LOG_STATUS_CURRENT.md, then the
   card heading, then the contract text.

Output defaults to the versioned `research/settled_rows_2026-09-28/generated/` folder. The older
2026-09-25 CSV remains a frozen historical artifact. Conflicts are quarantined, and approximate
contract-text matching is not used to join probabilities. Parsed legacy rows lack enough identity,
time, source and freeze evidence to enter prospective gates.
Usage: python research/settled_rows_2026-09-25/extract_settled_rows.py [--output-dir PATH]
"""
import argparse
import csv
import hashlib
import glob
import os
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = ['PREDICTION_LOG_COMBINED.md', 'PREDICTION_LOG_COMBINED_2.md', 'PREDICTION_LOG_COMBINED_3.md',
         'PREDICTION_LOG_COMBINED_4.md', 'PREDICTION_LOG_COMBINED_5.md']
# Active mini logs (2026-09-25(e)): cards settled there but not yet imported into Part 5. A card that is
# also in Part 5 must agree exactly; a conflicting occurrence is quarantined rather than silently
# choosing one source. P-510–P-515 were imported into Part 5 §"2026-09-25(f)".
MINI_LOGS = sorted(os.path.relpath(p, REPO) for p in glob.glob(
    os.path.join(REPO, 'Mini logs (to be sent to actual log later)', '*', '*.md')))
PARTS += MINI_LOGS
EXACT_RESULT_RE = re.compile(r'^(WIN|WON|LOSS|LOST|PUSH|VOID|W|L|P)$')
# Temporary IDs that later received canonical numbers (PREDICTION_LOG_COMBINED_5.md §"2026-09-26(a)").
# The issued records keep their temporary headings; the dataset reports the canonical ID.
ALIASES = {'TMP-20260923-NPB-CHU-DB-G25': 'P-516', 'TMP-20260923-NBL-CNS-TAS': 'P-517'}

ID_RE = re.compile(r'\b(P-\d{3}|TMP-\d{8}-[A-Z0-9-]+)\b')
RANGE_RE = re.compile(r'P-\d{3}\W{0,3}[–—-]\W{0,3}P-\d{3}')
UMBRELLA_RE = re.compile(r'\b(before|queue|component|imported|import|sweep|blocks|refresh|snapshot|continuation|'
                         r'reconciliation|rollover|consolidated|cohort|batch|appendix|audit|summary|register)\b', re.I)
HEAD_RE = re.compile(r'^(#{1,6})\s+(.*)$')
MARK_RE = re.compile(r'<!--\s*BEGIN VERBATIM ISSUED RECORD:\s*`?(P-\d{3}|TMP-\d{8}-[A-Z0-9-]+)')
SEP_RE = re.compile(r'^\|\s*:?-{2,}')
RESULT_RE = re.compile(r'\b(WIN|WON|LOSS|LOST|PUSH|VOID|W|L|P)\b')
NUM_RE = re.compile(r'(\d+(?:\.\d+)?)\s*(%)?')
TOKEN_RE = re.compile(r'[a-z0-9.]+')
BULLET_RE = re.compile(r'^- \*\*`?(P-\d{3})`?\*\*')
SEG_RE = re.compile(r'(?:^|[:·]\s*|\)\s*)([1-8])\s+`([^`]+)`\s*(?:p\s?(0?\.\d+))?[^·]*?\*\*(W|L|P|WIN|LOSS|PUSH)\*\*')


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def pick_col(headers, keys, avoid=()):
    for k in keys:
        for i, h in enumerate(headers):
            hl = h.lower()
            if k in hl and not any(a in hl for a in avoid):
                return i
    return None


def prob_col(headers):
    c = pick_col(headers, ['issued p', 'probability', 'derived probability', '`p`', 'stated p', 'p ('],
                 avoid=('probability state',))
    if c is None:
        c = next((k for k, hh in enumerate(headers) if hh.strip('` *').lower() in ('p', 'p(win)')), None)
    return c


def parse_prob(s):
    s = s.replace('`', '').replace('*', '')
    for m in NUM_RE.finditer(s):
        v = float(m.group(1))
        if m.group(2) == '%':
            v /= 100.0
        if 0.0 < v < 1.0:
            return v
    return None


def parse_result(s):
    t = s.replace('*', '').upper()
    m = RESULT_RE.search(t)
    if not m:
        return None
    return {'WIN': 'W', 'WON': 'W', 'W': 'W', 'LOSS': 'L', 'LOST': 'L', 'L': 'L', 'PUSH': 'P', 'P': 'P',
            'VOID': 'V'}[m.group(1)]


def parse_bool(s):
    t = re.sub(r"[*`\s]", "", s or "").casefold()
    return True if t in ("yes", "true", "1", "preferred") else False if t in ("no", "false", "0", "notpreferred") else None


def tokens(s):
    return set(TOKEN_RE.findall(re.sub(r'[*`]', '', s.lower())))


def similar(a, b):
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return False
    return len(ta & tb) / min(len(ta), len(tb)) >= 0.5


def normalize_contract(s):
    """Conservative text key for exact issued/settled joins; never guess by token overlap."""
    s = unicodedata.normalize("NFKC", re.sub(r"[*`]", "", s or "")).casefold()
    s = s.translate(str.maketrans({"−": "-", "–": "-", "—": "-", "’": "'"}))
    return " ".join(re.sub(r"[^\w.+/'-]+", " ", s).split())


def exact_col(headers, names):
    wanted = {x.casefold().strip("` *") for x in names}
    return next((i for i, h in enumerate(headers) if h.casefold().strip("` *") in wanted), None)


def infer_horizon(text):
    t = (text or "").upper().replace("_", "-")
    if re.search(r"\b(LIVE-ISSUED|LIVE VIEW|ISSUED LIVE|IN PROGRESS|WARMUP|AFTER START|START CROSSED)\b", t):
        return "LIVE_ISSUED"
    if re.search(r"\b(PREGAME|PRE-GAME|PRESTART)\b", t) and not re.search(r"\bNOT PRE[- ]?GAME\b", t):
        return "PREGAME_LABEL_ONLY"
    return "UNKNOWN"


def horizon_map(parts):
    """Collect whole card sections so settlement rows inherit a horizon label where present."""
    text_by_card = defaultdict(list)
    for part in parts:
        path = Path(REPO) / part
        if not path.exists():
            continue
        active, active_level = None, 0
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            h = HEAD_RE.match(line)
            if h:
                level = len(h.group(1))
                sid = single_id(h.group(2))
                if sid and not UMBRELLA_RE.search(h.group(2)):
                    active, active_level = sid, level
                elif active and level <= active_level:
                    active = None
            marker = MARK_RE.search(line)
            if marker:
                active, active_level = marker.group(1), 0
            if active:
                text_by_card[active].append(line)
    return {card: infer_horizon("\n".join(lines)) for card, lines in text_by_card.items()}


def reconcile_occurrences(graded, issued):
    """Keep only stable card/rank/contract/outcome groups; return detailed quarantine rows."""
    grouped = defaultdict(list)
    for row in graded:
        grouped[(row["card"], row["rank"])].append(row)
    final, conflicts = [], []
    for (card, rank), occurrences in sorted(grouped.items()):
        contracts = {normalize_contract(r.get("contract", "")) for r in occurrences}
        reasons = []
        if "" in contracts:
            reasons.append("MISSING_CONTRACT_IDENTITY")
        if len(contracts) > 1:
            reasons.append("MULTIPLE_CONTRACTS_FOR_CARD_RANK")
        for field in ("result", "p", "q", "baseline_p"):
            vals = {round(float(r[field]), 9) if field != "result" and r.get(field) is not None else r.get(field)
                    for r in occurrences if r.get(field) is not None}
            if len(vals) > 1:
                reasons.append("CONFLICTING_" + field.upper())
        if reasons:
            conflicts.append(_conflict_row(card, rank, occurrences, reasons))
            continue
        row = dict(occurrences[0])
        row["source_occurrences"] = " ; ".join(f"{r['part']}:{r['line']}" for r in occurrences)
        contract_key = next(iter(contracts))
        issue_rows = [x for x in issued.get((card, rank), [])
                      if normalize_contract(x.get("contract", "")) == contract_key]
        mismatch = None
        for field in ("p", "q", "baseline_p", "preferred_at_issue"):
            existing = {r.get(field) for r in occurrences if r.get(field) is not None}
            candidates = {x.get(field) for x in issue_rows if x.get(field) is not None}
            if len(existing) > 1 or len(candidates) > 1 or (existing and candidates and existing != candidates):
                mismatch = "ISSUE_SETTLEMENT_" + field.upper() + "_DISAGREEMENT"
                break
            if row.get(field) is None and len(candidates) == 1:
                row[field] = next(iter(candidates))
        if mismatch:
            conflicts.append(_conflict_row(card, rank, occurrences, [mismatch]))
            continue
        final.append(row)
    return final, conflicts


def _conflict_row(card, rank, occurrences, reasons):
    return {
        "card": card, "rank": rank, "occurrences": len(occurrences),
        "reason": ";".join(sorted(set(reasons))),
        "source_locations": " ; ".join(f"{r['part']}:{r['line']}" for r in occurrences),
        "contracts": " // ".join(r.get("contract", "")[:120] for r in occurrences),
        "results": "/".join(str(r.get("result", "")) for r in occurrences),
        "ps": "/".join("" if r.get("p") is None else f"{r['p']:.6f}" for r in occurrences),
        "qs": "/".join("" if r.get("q") is None else f"{r['q']:.6f}" for r in occurrences),
        "baseline_ps": "/".join("" if r.get("baseline_p") is None else f"{r['baseline_p']:.6f}" for r in occurrences),
    }


SPORT_RULES = [
    ('tennis', r'\b(WTA|ATP|ITF|UTR|Challenger|tennis|US Open (Women|men|Men|R\d|20\d\d|Qualifying)|Roland|Wimbledon|Australian Open|sets?|games handicap|total games)\b'),
    ('cricket', r'\b(T20I?|ODI|CPL|WCPL|Knight Riders|Amazon Warriors|IPL|BBL|WPL|PSL|Hundred|cricket|Test|ETPL|European T20|Blast|Sheffield|One Day Cup|'
                r'Asia Cup|innings|overs|wickets?|powerplay)\b'),
    ('american-football', r'\b(NFL|NCAA|FCS|FBS|college football)\b'),
    ('AFL', r'\bAFLW?\b'),
    ('rugby', r'\b(NRLW?|Super Rugby|rugby|Top 14|Premiership Rugby|URC|NPC|Hilux|Rugby Championship|State of Origin)\b'),
    ('ice-hockey', r'\b(NHL|AHL|KHL|SHL|AIHL|hockey|Metal Ligaen|puck ?line|Goodall Cup)\b'),
    ('baseball-MLB', r'\bMLB\b'),
    # An explicit basketball league word beats a shared nickname (P-514 "Illawarra Hawks" is not SoftBank).
    ('basketball', r'\b(Basketball|NBL|NBA|WNBA)\b'),
    ('baseball-NPB/KBO/CPBL', r'\b(NPB|KBO|CPBL|Fighters|Seibu|Eagles|Buffaloes|Hawks|Marines|Dragons|Hanshin|Tigers \(NPB\)|Yomiuri|'
                              r'Giants \(NPB\)|Swallows|Carp|DeNA|BayStars|Doosan|KT Wiz|LG Twins|NC Dinos|Kia|Samsung|Lotte|Hanwha|'
                              r'Kiwoom|SSG|Monkeys|Brothers|Guardians \(CPBL\)|Uni-President|Wei-Chuan|TSG)\b'),
    ('baseball-MLB', r'\b(Yankees|Red Sox|Dodgers|Mets|Cubs|Guardians|Tigers|Orioles|Rays|Astros|Mariners|Rangers|Royals|White Sox|'
                     r'Twins|Angels|Athletics|Blue Jays|Braves|Phillies|Marlins|Nationals|Pirates|Reds|Brewers|Cardinals|Giants|'
                     r'Padres|Diamondbacks|Rockies)\b'),
    ('basketball', r'\b(NBA|WNBA|NBL|BCL|Basket|LKL|EuroLeague|EuroCup|FIBA|basketball|LNBP|LMB|BSL|ACB|BBL basketball|Liberty|Aces|Sky|Dream|'
                   r'Fever|Mercury|Lynx|Sparks|Storm|Wings|Sun|Mystics|Valkyries|Tempo|Wildcats|36ers|Breakers|Taipans|JackJumpers)\b'),
    ('soccer', r'\b(EPL|Slovnaft|Cup R\d+|Premier League|UEFA|Champions League|Europa|Conference League|MLS|A-League|Bundesliga|LaLiga|Serie A|'
               r'Ligue|Eredivisie|Allsvenskan|Superliga|Liga MX|J1|K League|Saudi|ACL2?|ACLE|FA Cup|Copa|World Cup qualif|'
               r'Leagues Cup|Clausura|Apertura|CSL|S-League|Division|ASEAN|AFC|CONCACAF|Libertadores|Sudamericana|Primeira|'
               r'Championship|Femenil|NWSL|WSL|or Draw|1X|X2|corners?|clean sheet|both teams)\b'),
]


def classify_sport(event, title, contracts):
    for text in (event, title, ' '.join(contracts)):
        for sport, pat in SPORT_RULES:
            if text and re.search(pat, text, re.I if sport not in ('baseball-MLB',) else 0):
                return sport
    joined = ' '.join(contracts).lower()
    if re.search(r'\bruns?\b|run line', joined):
        return 'baseball-other'
    if re.search(r'\bgoals?\b', joined):
        return 'soccer'
    return 'unclassified'


def classify_family(c):
    cl = c.lower()
    if re.search(r'corner', cl):
        return 'corners'
    if re.search(r'\bcards?\b|booking', cl):
        return 'cards'
    if re.search(r'first half|\b1h\b|first 5\b|\bf5\b|first five|first 6|first six|powerplay|\bq[1-4]\b|quarter|first period|'
                 r'1st half|overs? 0\.1|first \d+ (legal )?overs|1st period|first innings|1st innings|after \d+ overs', cl):
        return 'phase'
    if re.search(r'team total|\bto score\b', cl):
        return 'team-total'
    if re.search(r'\bover\b|\bunder\b|\btotal\b', cl):
        return 'total'
    if re.search(r'[+−–-]\s*\d+(\.\d+)?|run ?line|puck ?line|spread|handicap|cushion', cl):
        return 'handicap'
    if re.search(r'\bml\b|moneyline|to win|winner|\bwin\b|draw no bet|double chance|\bdnb\b|\bdraw\b|\b1x\b|\bx2\b', cl):
        return 'moneyline'
    if re.search(r'player|strikeouts?|\bhits?\b|assists|rebounds|shots|aces|sixes|fours', cl):
        return 'prop'
    return 'other'


def direction(c):
    cl = c.lower()
    if re.search(r'\bover\b', cl):
        return 'Over'
    if re.search(r'\bunder\b', cl):
        return 'Under'
    m = re.search(r'([+−–-])\s*(\d+(?:\.\d+)?)', c)
    if m:
        return 'plus' if m.group(1) == '+' else 'minus'
    return ''


def event_map():
    ev = {}
    for fn in ('GAME_LOG_STATUS_INDEX_2026-09-05.md', 'GAME_LOG_STATUS_CURRENT.md'):
        p = os.path.join(REPO, fn)
        if not os.path.exists(p):
            continue
        for line in open(p, encoding='utf-8-sig'):
            m = re.match(r'^\|\s*(P-\d{3}|TMP-\d{8}-[A-Z0-9-]+)\s*\|\s*([^|]+)\|', line)
            if m:
                ev[m.group(1)] = m.group(2).strip()
    return ev


def single_id(text):
    ids = set(ID_RE.findall(text))
    if len(ids) != 1 or RANGE_RE.search(text):
        return None
    return ids.pop()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output-dir", type=Path,
                    default=Path(REPO) / "research" / "settled_rows_2026-09-28" / "generated")
    args = ap.parse_args(argv)
    events = event_map()
    graded, issued = [], defaultdict(list)
    titles = {}
    unattributed = []
    card_horizons = horizon_map(PARTS)
    for part in PARTS:
        lines = open(os.path.join(REPO, part), encoding='utf-8-sig').read().split('\n')
        heading_card, card_level = None, 0
        i = 0
        while i < len(lines):
            ln = lines[i].rstrip('\r')
            h = HEAD_RE.match(ln)
            if h:
                level = len(h.group(1))
                if ID_RE.search(h.group(2)):
                    sid = single_id(h.group(2))
                    heading_card = sid if (sid and not UMBRELLA_RE.search(h.group(2))) else None
                    card_level = level
                    if heading_card:
                        t = h.group(2)
                        if not re.search(r'settlement|retrospective|audit|correction', t, re.I):
                            titles.setdefault(heading_card, t[:200])
                elif heading_card and level <= card_level:
                    heading_card = None      # a sibling/parent heading ends the card's section
                i += 1
                continue
            mk = MARK_RE.search(ln)
            if mk:
                heading_card = mk.group(1)
                i += 1
                continue
            bl = BULLET_RE.match(ln)
            if bl:
                # P-318–P-344 cohort format: "- **`P-335`** (...): 1 `WSH +1.5` p0.59 **W** (0.1681) · 2 `Over 8.0` p0.52 **L** …"
                for seg in SEG_RE.finditer(ln):
                    res = parse_result(seg.group(4))
                    if res:
                        graded.append({'part': part, 'line': i + 1, 'card': bl.group(1), 'rank': int(seg.group(1)),
                                       'contract': seg.group(2)[:160],
                                       'p': float(seg.group(3)) if seg.group(3) else None, 'q': None,
                                       'baseline_p': None, 'preferred_at_issue': None, 'result': res})
                i += 1
                continue
            if ln.startswith('|') and i + 1 < len(lines) and SEP_RE.match(lines[i + 1].rstrip('\r')):
                # attribute: look back for a line naming exactly one ID
                card = None
                k, seen = i - 1, 0
                while k >= 0 and seen < 8:
                    prev = lines[k].rstrip('\r')
                    if prev.strip() and not prev.startswith('|'):
                        seen += 1
                        sid = single_id(prev)
                        if sid and not (HEAD_RE.match(prev) and UMBRELLA_RE.search(prev)):
                            card = sid
                            break
                        if HEAD_RE.match(prev):
                            break
                    k -= 1
                card = card or heading_card
                headers = cells(ln)
                card_c = next((k for k, hh in enumerate(headers)
                               if hh.strip('` *').lower() in ('card', 'id', 'card id', 'canonical id', 'record')), None)
                rank_c = pick_col(headers, ['rank'])
                res_c = pick_col(headers, ['result', 'operator settlement', 'settlement', 'outcome', 'realised'],
                                 avoid=('route', 'source', 'endpoint', 'note'))
                # Every result-bearing column. A cell that is exactly a result token ("**WIN**") beats a
                # narrative cell ("STL lost 1–2 (margin -1)"), which can describe the game, not the row.
                res_cols = [k for k, hh in enumerate(headers)
                            if any(t in hh.lower() for t in ('result', 'settlement', 'outcome', 'realised'))
                            and not any(a in hh.lower() for a in ('route', 'source', 'endpoint', 'note'))]
                p_c = prob_col(headers)
                q_c = exact_col(headers, ('rm-1 q', 'q', 'ranking q', 'calibrated q'))
                baseline_c = exact_col(headers, ('baseline_p', 'baseline p', 'naive baseline p'))
                preferred_c = exact_col(headers, ('preferred_at_issue', 'preferred at issue', 'preferred decision'))
                con_c = pick_col(headers, ['contract', 'pick', 'selection', 'frozen issued row', 'issued row', 'row', 'option'],
                                 avoid=('contract id',))
                j = i + 2
                while j < len(lines) and lines[j].startswith('|'):
                    cs = cells(lines[j].rstrip('\r'))
                    row_card = card
                    if card_c is not None and len(cs) == len(headers):
                        row_card = single_id(cs[card_c])
                    if rank_c is not None and len(cs) == len(headers):
                        card_saved, card = card, row_card
                        rk = re.search(r'\b([1-8])\b', cs[rank_c].replace('*', ''))
                        contract = re.sub(r'[*`]', '', cs[con_c]) if con_c is not None else ''
                        p = parse_prob(cs[p_c]) if p_c is not None else None
                        q = parse_prob(cs[q_c]) if q_c is not None else None
                        baseline_p = parse_prob(cs[baseline_c]) if baseline_c is not None else None
                        preferred = parse_bool(cs[preferred_c]) if preferred_c is not None else None
                        if rk:
                            if res_c is not None:
                                exact = [cs[k] for k in res_cols
                                         if EXACT_RESULT_RE.match(re.sub(r'[*`\s]', '', cs[k]).upper())]
                                res = parse_result(exact[0]) if exact else parse_result(cs[res_c])
                                if res:
                                    if card:
                                        graded.append({'part': part, 'line': j + 1, 'card': card, 'rank': int(rk.group(1)),
                                                       'contract': contract[:160], 'p': p, 'q': q, 'baseline_p': baseline_p,
                                                       'preferred_at_issue': preferred, 'result': res})
                                    else:
                                        unattributed.append({'part': part, 'line': j + 1, 'reason': 'CARD_ID_NOT_UNIQUE',
                                                             'row': lines[j][:500]})
                                elif card and (p is not None or q is not None or baseline_p is not None or preferred is not None):
                                    # Tables often carry a blank Result column at issue time. Preserve
                                    # these frozen values as lookups instead of silently dropping them.
                                    issued[(card, int(rk.group(1)))].append({'contract': contract, 'p': p, 'q': q,
                                                                             'baseline_p': baseline_p,
                                                                             'preferred_at_issue': preferred,
                                                                             'part': part, 'line': j + 1})
                            elif card and (p is not None or q is not None or baseline_p is not None or preferred is not None):
                                issued[(card, int(rk.group(1)))].append({'contract': contract, 'p': p, 'q': q,
                                                                         'baseline_p': baseline_p,
                                                                         'preferred_at_issue': preferred,
                                                                         'part': part, 'line': j + 1})
                        card = card_saved
                    j += 1
                i = j
                continue
            i += 1
    final, conflicts = reconcile_occurrences(graded, issued)
    by_card = defaultdict(list)
    for r in final:
        by_card[r['card']].append(r)
    out = []
    for card, rs in by_card.items():
        ev = events.get(card, '') or events.get(ALIASES.get(card, ''), '')
        sport = classify_sport(ev, titles.get(card, ''), [r['contract'] for r in rs])
        source_card = card
        card = ALIASES.get(card, card)
        for r in sorted(rs, key=lambda x: x['rank']):
            source = f"{r['part']}:{r['line']}"
            p = r.get('p')
            q = r.get('q')
            base = r.get('baseline_p')
            horizon = card_horizons.get(source_card, "UNKNOWN")
            reason = ("LIVE_ISSUED_EXCLUDED" if horizon == "LIVE_ISSUED" else
                      "LEGACY_ROW_MISSING_EVENT_FORECAST_TARGET_IDS_TIMES_SOURCE_LINEAGES_AND_FREEZE_HASHES")
            contract_fp = hashlib.sha256(normalize_contract(r['contract']).encode('utf-8')).hexdigest()
            revision_basis = "|".join((r.get("source_occurrences", source), r["result"], str(p), str(q), str(base)))
            revision_fp = hashlib.sha256(revision_basis.encode("utf-8")).hexdigest()
            out.append({'card': card, 'num': int(card[2:5]) if card.startswith('P-') else '', 'sport': sport,
                        'rank': r['rank'], 'n_ranks': len(rs), 'contract': r['contract'],
                        'family': classify_family(r['contract']), 'direction': direction(r['contract']),
                        'event_id': '', 'event_cluster_id': '', 'forecast_id': '', 'decision_id': '',
                        'target_id': '', 'contract_fingerprint': contract_fp,
                        'p': '' if p is None else f"{p:.6f}",
                        'q': '' if q is None else f"{q:.6f}",
                        'q_semantics': 'ROW_CALIBRATED_NOT_JOINT' if q is not None else 'UNKNOWN',
                        'baseline_p': '' if base is None else f"{base:.6f}",
                        'baseline_match_valid': '',
                        'preferred_at_issue': '' if r.get('preferred_at_issue') is None else str(r['preferred_at_issue']).lower(),
                        'result': r['result'], 'outcome_verified': 'false', 'horizon': horizon,
                        'input_cutoff_utc': '', 'issued_at_utc': '', 'event_start_utc': '',
                        'method_sha256': '', 'control_sha256': '', 'manifest_sha256': '',
                        'performance_eligible': 'false', 'eligibility_reasons': reason,
                        'settlement_revision_fingerprint': revision_fp,
                        'source': source, 'source_occurrences': r['source_occurrences'],
                        'event': (ev or titles.get(source_card, ''))[:120]})
    out.sort(key=lambda x: (x['num'] if x['num'] != '' else 9999, x['card'], x['rank']))
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    out_fields = ['card', 'num', 'sport', 'rank', 'n_ranks', 'contract', 'family', 'direction',
                  'event_id', 'event_cluster_id', 'forecast_id', 'decision_id', 'target_id',
                  'contract_fingerprint', 'p', 'q', 'q_semantics', 'baseline_p', 'preferred_at_issue',
                  'baseline_match_valid',
                  'result', 'outcome_verified', 'horizon', 'input_cutoff_utc', 'issued_at_utc',
                  'event_start_utc', 'method_sha256', 'control_sha256', 'manifest_sha256',
                  'performance_eligible', 'eligibility_reasons', 'settlement_revision_fingerprint',
                  'source', 'source_occurrences', 'event']
    with open(output_dir / 'settled_rows.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=out_fields)
        w.writeheader()
        w.writerows(out)
    conflict_fields = ['card', 'rank', 'occurrences', 'reason', 'source_locations', 'contracts',
                       'results', 'ps', 'qs', 'baseline_ps']
    with open(output_dir / 'conflicts.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=conflict_fields)
        w.writeheader()
        w.writerows(conflicts)
    with open(output_dir / 'unattributed_rows.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=['part', 'line', 'reason', 'row'])
        w.writeheader()
        w.writerows(unattributed)
    with_p = [r for r in out if r['p']]
    cov = [f"legacy rows retained after exact conflict checks: {len(out)} from {len({r['card'] for r in out})} cards; rows with p: {len(with_p)}",
           f"raw graded occurrences: {len(graded)}; unattributed rows retained for review: {len(unattributed)}; quarantined card/rank groups: {len(conflicts)}",
           f"prospective-eligible rows: {sum(r['performance_eligible'] == 'true' for r in out)} (legacy extraction cannot certify eligibility)",
           "Identity policy: exact contract text only; no approximate joins; conflicts do not enter the scored CSV.",
           f"sports among retained rows: {dict(sorted(((s, sum(1 for r in out if r['sport'] == s)) for s in {r['sport'] for r in out}), key=lambda x: -x[1]))}"]
    (output_dir / 'coverage.txt').write_text('\n'.join(cov) + '\n', encoding='utf-8')
    print('\n'.join(cov))


if __name__ == '__main__':
    main()
