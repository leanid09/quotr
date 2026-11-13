# -*- coding: utf-8 -*-
"""Build Quotr Intelligence OS v2 from the v1 workbook.

Usage (from repo root):
  python3 content-os/build/build.py content-os/build/input/Quotr_Intelligence_OS_v1.xlsx content-os/Quotr_Intelligence_OS_v2.xlsx
Then recalculate formulas (LibreOffice or open in Excel) so cached values exist.
Edit the article list in articles_data.py, claims/prompts/refreshes in content_text.py,
schema/formats/channels/SOP in ref_sheets.py, and rebuild.
"""
import sys, re, json, copy, datetime as dt
from collections import defaultdict
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.utils import get_column_letter as L

import os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from articles_data import LANES, LANE_NAMES, PATTERN
from content_text import CLAIMS, PROMPTS, PERSONA_NAMES, CLUSTERS, REFRESH
from ref_sheets import SCHEMA, FORMATS, CHANNELS, LANE_CHANNELS, TIMELINE, QA_GATES, AI_PROMPTS, ROLES, SWAP_RULES, WEEKLY

SRC, OUT = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(SRC)

# ------------------------------------------------------------------ styles
FN = 'Carlito'
NAVY, TEAL, LIGHT, INPUT, CALC, DARK = '13243A', '087E8B', 'E9EFF5', 'FFF0C2', 'D9F2EF', '1E293B'
def font(b=False, c=None, sz=11, i=False): return Font(name=FN, size=sz, bold=b, color=c, italic=i)
def fill(c): return PatternFill('solid', fgColor=c)
WRAP = Alignment(wrap_text=True, vertical='top')
TOP = Alignment(vertical='top')

def style_row(ws, r, c1, c2, f=None, fl=None, al=None):
    for c in range(c1, c2 + 1):
        cell = ws.cell(r, c)
        if f: cell.font = f
        if fl: cell.fill = fl
        if al: cell.alignment = al

def title(ws, text, sub, ncols):
    for rng in list(ws.merged_cells.ranges):
        if rng.min_row <= 2: ws.unmerge_cells(str(rng))
    ws['A1'] = text; ws['A2'] = sub
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    ws['A1'].font = font(True, 'FFFFFF'); ws['A1'].fill = fill(NAVY); ws['A1'].alignment = Alignment(vertical='center')
    ws['A2'].font = font(False, DARK); ws['A2'].fill = fill(LIGHT); ws['A2'].alignment = Alignment(vertical='center')
    ws.row_dimensions[1].height = 35; ws.row_dimensions[2].height = 27; ws.row_dimensions[3].height = 10

def header(ws, r, heads, c0=1, color=TEAL):
    for i, h in enumerate(heads):
        c = ws.cell(r, c0 + i, h)
        c.font = font(True, 'FFFFFF'); c.fill = fill(color); c.alignment = Alignment(wrap_text=True, vertical='center')
    ws.row_dimensions[r].height = 30

def band(ws, r, text, ncols, color=TEAL):
    ws.cell(r, 1, text)
    style_row(ws, r, 1, ncols, font(True, 'FFFFFF'), fill(color))
    ws.row_dimensions[r].height = 22

def widths(ws, d):
    for k, v in d.items(): ws.column_dimensions[k].width = v

def put(ws, r, c, v, f=None, fl=None, al=None, fmt=None):
    cell = ws.cell(r, c, v)
    cell.font = f or font()
    if fl: cell.fill = fl
    if al: cell.alignment = al
    if fmt: cell.number_format = fmt
    return cell

def new_sheet(name, idx=None):
    if name in wb.sheetnames: del wb[name]
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = True
    return ws

def dv_list(ws, rng, items, allow_blank=True):
    dv = DataValidation(type='list', formula1='"' + ','.join(items) + '"', allow_blank=allow_blank)
    dv.add(rng); ws.add_data_validation(dv)

def q(s):  # excel string literal
    return '"' + s.replace('"', '""') + '"'

# ------------------------------------------------------------------ claims index
CLM = {}
for i, c in enumerate(CLAIMS, 1): CLM[i] = c
def cid(sub):
    for i, c in CLM.items():
        if sub.lower() in c[1].lower(): return f'CLM-{i:03d}'
    raise KeyError(sub)

C_PRICING = [cid('Lite plan costs'), cid('Plus plan costs'), cid('Enterprise pricing is custom'), cid('7-day free trial')]
C_SERVICE = [cid('$0.25 per sq ft'), cid('$0.10 per sq ft')]
C_LINES = [cid('three product lines')]
C_PROC = [cid('factory-direct materials from manufacturers in China'), cid('Procurement is optional')]
C_BAY = [cid('Myren Dr'), cid('Stratford Ct'), cid('Skyfarm Dr')]
C_TARIFF = [cid('25% Section 232'), cid('delayed to January 1, 2027'), cid('Anti-dumping and countervailing')]
C_RL = [cid('RL Electric says')]
C_ACC = [cid('95–99%'), cid('80–88%')]
C_IDENT = [cid('FLOZ Inc.'), cid('founded by Hanyang Liu'), cid('SkyDeck Batch 19'), cid('investors include'), cid('Funding amount')]
COMP_CLAIMS = {'Togal': cid("Togal.AI's Growth plan"), 'Handoff': cid('Handoff costs'), 'PlanSwift': cid('PlanSwift subscriptions'),
               'STACK': cid('STACK has about 1,400'), 'Kreo': cid('Kreo sells plans'), 'Beam': cid("Beam AI's done-for-you"),
               'On-Screen': cid('PlanSwift and On-Screen Takeoff are owned')}

# ------------------------------------------------------------------ schedule
EARLIEST = {'G0': 1, 'GE': 1, 'GF': 2, 'GA': 2, 'GQ': 3, 'GP': 3, 'GS': 4, 'GC': 4, 'GT': 4, 'GN': 6, 'GV': 7}
GATE_TEXT = {'G0': 'None — public sources + verified facts', 'GF': 'Fact sheet sign-off (FIX-01)', 'GP': 'Quotr procurement data / approval',
             'GS': 'Quotr Service data export + method owner', 'GC': 'Customer permission + approved numbers',
             'GE': 'Expert review (customs / tariff)', 'GT': 'Benchmark test complete (Benchmark Lab)',
             'GQ': 'Product confirmation (features / exports / browser / security)', 'GA': 'Multi-engine AI baseline complete',
             'GN': 'Native Spanish reviewer', 'GV': 'Customer survey fielded (n≥50)'}
def gate_text(g): return ' + '.join(GATE_TEXT[x] for x in g.split('+'))
def earliest(g): return max(EARLIEST[x] for x in g.split('+'))

queues = {k: list(v) for k, v in LANES.items()}
ARTS = []
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
for wk in range(1, 14):
    for di, day in enumerate(DAYS):
        for slot, lane in enumerate(PATTERN[day], 1):
            qq = queues[lane]
            if wk == 1 and day == 'Mon': pick = qq.pop(0)
            else:
                idx = next((i for i, a in enumerate(qq) if earliest(a['gate']) <= wk), 0)
                pick = qq.pop(idx)
            n = len(ARTS) + 1
            a = dict(pick); a.update(id=f'ART-{n:03d}', week=wk, day=day, dayidx=di, slot=slot, laneN=LANE_NAMES[lane])
            a['date'] = dt.date(2026, 11, 16) + dt.timedelta(days=7 * (wk - 1) + di)
            ARTS.append(a)
assert len(ARTS) == 195 and all(not v for v in queues.values())
BYID = {a['id']: a for a in ARTS}

AUTHOR_DEFAULT = {'CL01': 'Hanyang Liu', 'CL02': 'Hanyang Liu', 'CL03': 'Hanyang Liu', 'CL04': 'Hanyang Liu', 'CL14': 'Hanyang Liu',
                  'CL11': 'Hanyang Liu', 'CL10': 'Tianyi Zong'}
AUTHOR_SLUG = {'Hanyang Liu': 'hanyang-liu', 'Junzhe Shi, PhD': 'junzhe-shi', 'Tianyi Zong': 'tianyi-zong', 'Jati Ibloguen': 'jati-ibloguen'}
AUTHOR_SCHEMA = {'Hanyang Liu': 'Hanyang Liu', 'Junzhe Shi, PhD': 'Junzhe Shi', 'Tianyi Zong': 'Tianyi Zong', 'Jati Ibloguen': 'Jati Ibloguen'}
CLUSTER = {c[0]: c for c in CLUSTERS}
REGION_MAP = {'US (Spanish)': 'Spanish-language', 'CA vs FL': 'Florida'}

def mkslug(a):
    if a['slug']: return a['slug']
    t = a['title'].split(':')[0]
    t = re.sub(r'\([^)]*\)', '', t)
    t = t.replace('Quotr.ai', 'quotr').replace('Togal.AI', 'togal-ai').replace('&', 'and')
    t = re.sub(r'\b20\d\d\b', '', t)
    t = re.sub(r"[^A-Za-z0-9\s-]", '', t).strip().lower()
    words = t.split()
    s = '-'.join(words)
    while len(s) > 60 and len(words) > 3:
        words = words[:-1]; s = '-'.join(words)
    return s

for a in ARTS:
    a['author'] = a['author'] or AUTHOR_DEFAULT.get(a['cluster'], 'Junzhe Shi, PhD')
    a['region'] = REGION_MAP.get(a['region'], a['region'])
    a['slugv'] = mkslug(a)
    s = a['slugv']
    if s.startswith('es/'): a['path'] = f"/es/blog/{s[3:]}/"; a['section'] = ('Blog', '/es/blog/'); a['lang'] = 'es-US'
    elif a['lane'] == 'S': a['path'] = f"/research/{s}/"; a['section'] = ('Research', '/research/'); a['lang'] = 'en-US'
    elif a['lane'] == 'B': a['path'] = f"/benchmarks/{s}/"; a['section'] = ('Benchmarks', '/benchmarks/'); a['lang'] = 'en-US'
    elif a['fmt'] == 'HUB' and a['cluster'] in ('CL04',): a['path'] = f"/solutions/{s}/"; a['section'] = ('Solutions', '/solutions/'); a['lang'] = 'en-US'
    else: a['path'] = f"/blog/{s}/"; a['section'] = ('Blog', '/blog/'); a['lang'] = 'en-US'
slugs = [a['slugv'] for a in ARTS]
dups = {s for s in slugs if slugs.count(s) > 1}
assert not dups, dups

def short(t, n=60):
    t = t.split(':')[0]
    return t if len(t) <= n else t[:n - 1].rsplit(' ', 1)[0] + '…'

META = {'CMP': "Compared on pricing, AI features and fit, with dated sources and where each option is stronger.",
        'ALT': "Grouped by reason to switch, with dated prices and when to stay.",
        'BEST': "Selection criteria, a dated comparison table and honest limits for each tool.",
        'COST': "Dated ranges with sources, a worked example and what drives the price.",
        'HOW': "A step-by-step method, sourced rules of thumb and a worked example from real plans.",
        'HOWP': "The steps, costs, timelines and documents, with dated sources and a worked example.",
        'ANL': "The dated facts, what they mean for builders and subs, and what to do now.",
        'DATA': "Method, sample size, findings and a downloadable dataset from Quotr.ai.",
        'METH': "Test set, ground truth, scoring and limits, published before any results.",
        'CASE': "The problem, what changed and the results, with approved numbers.",
        'HUB': "The workflow, pricing and when Quotr.ai is not the right fit.",
        'EVAL': "A practical checklist with scoring and red flags.",
        'TPL': "A free template with step-by-step instructions and a worked example.",
        'PR': "", 'LOG': ""}
def head(t, n=90):
    t = t.split(':')[0]
    if '?' in t: t = t.split('?')[0] + '?'
    return t if len(t) <= n else t[:n - 1].rsplit(' ', 1)[0] + '…'
import glob as _g
DRAFT_META = {}
for _f in _g.glob(os.path.join(HERE, '..', 'articles', 'ART-*.md')):
    _id = _f.split('/')[-1][:7]
    for _l in open(_f):
        if _l.startswith('meta_description:'): DRAFT_META[_id] = _l.split(':', 1)[1].strip().strip('"'); break
def meta(a):
    if a.get('id') in DRAFT_META: return DRAFT_META[a['id']].replace('"', "'")
    if a['lang'] == 'es-US': return head(a['title'], 100) + '. Guía paso a paso con ejemplo práctico y fuentes con fecha.'
    key = 'HOWP' if (a['fmt'] in ('HOW', 'TPL') and a['cluster'] == 'CL01') else a['fmt']
    T = head(a['title'])
    tail = META[key]
    m = (T if T.endswith('?') or not tail else T + '.') + (' ' + tail if tail else '')
    if len(m) > 160: m = head(a['title'], 60) + ('' if head(a['title'], 60).endswith('?') else '.') + ' ' + tail
    return m.replace('"', "'").strip()

def req_claims(a):
    ids = list(C_LINES)
    t = (a['title'] + ' ' + a['query'] + ' ' + (a['angle'] or '')).lower()
    if a['lane'] == 'C' or a['cluster'] in ('CL07', 'CL04') or a['fmt'] in ('CMP', 'ALT', 'BEST', 'EVAL', 'HUB'): ids += C_PRICING
    if a['cluster'] in ('CL10',) or 'service' in t or 'outsource' in t or 'per sq ft' in t or 'per square foot' in t: ids += C_SERVICE
    if a['cluster'] == 'CL01' or 'SRC' in a['trade'] or 'factory-direct' in t: ids += C_PROC
    if 'tariff' in t: ids += C_TARIFF
    if a['region'] == 'Bay Area' or 'bay area' in t or 'saratoga' in t: ids += C_BAY
    if 'rl electric' in t or a['trade'] == 'ELEC': ids += C_RL
    if a['cluster'] == 'CL13' or 'accura' in t: ids += C_ACC
    if a['fmt'] == 'PR': ids += C_IDENT
    for k, v in COMP_CLAIMS.items():
        if k.lower() in t: ids.append(v)
    seen = []
    for i in ids:
        if i not in seen: seen.append(i)
    return ', '.join(seen)

NEVER = {'CL07': "No retired Solo/Team pricing; write 'Quotr.ai Lite/Plus'; no self-ranking #1; every competitor fact dated + linked.",
         'CL04': "Only confirmed features; no self-ranking; honest 'not the right fit' section.",
         'CL01': "No savings % or factory count (TO CONFIRM); no 'any US port' delivery claim; not legal/customs advice; tariff dates re-verified in publish week.",
         'CL02': "No numbers without method, sample size and date range; no synthetic or modeled data presented as observed.",
         'CL03': "Every range dated + sourced; worked examples labeled 'illustrative' unless Quotr data.",
         'CL05': "Waste factors and rules of thumb must cite a source; no 'up to 80%' time-saved claim.",
         'CL06': "No unsourced industry statistics; no 'up to 80% / 90% faster'.",
         'CL09': "No metrics without customer permission; label investor quotes as investor; no review counts.",
         'CL10': "No turnaround time until approved; no '$1.2B+' or '300+ projects/month' without method.",
         'CL11': "Funding/HQ/founding year only after fact sheet sign-off; no '$190K seed'.",
         'CL13': "No accuracy % without approved figure + 'Quotr internal benchmarking' + method link; no synthetic results.",
         'CL14': "No individualized cost quotes; regional numbers dated + sourced; procurement delivery area TO CONFIRM."}
GLOBAL_NEVER = " Global: no Quotr Pro ratings, no reviews/awards/press claims, no text addressed to AI."

def ent(a, k, d=''): return a['ent'].get(k, d)

def outline(a):
    f = a['fmt']; e = a['ent']
    subj = ent(a, 'subject', short(a['title'], 70))
    if f == 'CMP':
        names = [e[k] for k in ('a', 'b', 'c', 'd') if k in e]
        if a['lane'] == 'R':
            A_, B_ = names[0], names[1]
            L_ = [f"Quick answer: why the same building prices differently in {A_} and {B_}", "Cost comparison at a glance (dated, sourced)", "Labor rates and availability",
                  "Codes and energy requirements", "Materials, logistics and climate-driven specs", "Worked example: one building priced in both states (illustrative, labeled)",
                  "What developers should adjust when moving between markets", "FAQ", "Sources"]
        elif a['slugv'].startswith('how-builders-buy'):
            L_ = ["Quick answer: which buying route fits which project", "The five routes at a glance (dated table: price level, lead time, minimums, QC, who handles duties)",
                  "Factory-direct: how it works, who it suits", "Local dealers and distributors", "Big-box retail and pro desks", "Sourcing agents", "Marketplaces (Alibaba and similar)",
                  "How to choose: decision tree by project size and timeline", "Where Quotr Procurement fits (and when it doesn't)", "FAQ", "Sources"]
        elif len(names) == 2:
            A_, B_ = names
            L_ = [f"Quick answer: {A_} vs {B_} in 60 words", f"{A_} vs {B_} at a glance (dated table: price, pricing model, AI takeoff, platform, trial, best for)",
                  f"What is {A_}, and who is it built for?", f"What is {B_}, and who is it built for?", f"How does pricing compare (as of [date])?",
                  f"Where {A_} is stronger", f"Where {B_} is stronger", "Which should you choose? (small sub / residential builder / GC / developer)"]
            if 'Quotr.ai' not in names and 'California' not in names: L_.append("Is there a third option? Where Quotr.ai fits (brief, fair)")
            L_ += ["FAQ", "Sources and last-checked dates"]
        else:
            lst = ', '.join(names[:-1]) + ' and ' + names[-1]
            L_ = [f"Quick answer: which of {lst} fits which buyer", "At-a-glance table (dated: price, model, AI features, platform, trial)"]
            L_ += [f"{n}: what it does well and where it falls short" for n in names]
            L_ += ["Best for residential plans / commercial plans / done-for-you", "How to test them on your own plans", "FAQ", "Sources and last-checked dates"]
    elif f == 'ALT':
        x = e['x']
        if x == 'Quotr.ai':
            L_ = ["Quick answer: when Quotr.ai fits and when it doesn't", "What Quotr.ai does (Quotr Software, Quotr Service, Quotr Procurement)",
                  "Choose something else if you need job management and invoicing", "Choose something else if you live in commercial bid boards",
                  "Choose something else if you need a free tier", "Alternatives at a glance (dated table)", "When Quotr.ai is the better fit", "FAQ", "Sources"]
        else:
            L_ = [f"Quick answer: the best {x} alternatives by situation", f"Why do teams look for {x} alternatives? (sourced reasons)",
                  f"{x} alternatives at a glance (dated table)", "Best for plan-based AI takeoff", "Best for residential builders",
                  "Best for done-for-you estimating", "Best for tight budgets", f"When should you stay with {x}?",
                  "How to test an alternative on your own plans (7-day trial checklist)", "FAQ", "Sources"]
    elif f == 'BEST':
        cat, tr, needs = e.get('cat', subj), e.get('trade', 'your trade'), e.get('needs', 'scope fit, price, accuracy')
        L_ = ["Quick answer: the shortlist by situation", f"How we chose: criteria for {tr} ({needs}); disclosure: Quotr.ai is our product",
              f"{cat[0].upper() + cat[1:]} at a glance (dated table)", "Tool by tool: best for, price, strengths, limits (5–7 tools; Quotr.ai not ranked #1)",
              f"What should {tr} buyers check before choosing?", "How to test a tool on your own plans", "FAQ", "Sources"]
    elif f == 'COST':
        L_ = [f"Quick answer: what {subj} typically runs and why (as of [date])", f"{subj[0].upper() + subj[1:]} at a glance (low / typical / high, with sources)",
              "What drives the cost?", "Worked example (Quotr data or clearly labeled illustrative)", "How to lower it without cutting quality",
              "Regional differences (where relevant)", "FAQ", "Sources and method"]
    elif f in ('HOW', 'TPL'):
        tr, unit = e.get('trade', subj), e.get('unit', 'quantities')
        if a['cluster'] == 'CL01':
            L_ = ["Quick answer (40–80 words): what it is and the steps in one line each", "Who this is for (and when not to do it)", "Step-by-step (H3 per step)",
                  "Costs, timelines and documents (sourced, dated)", "Worked example (Quotr process; numbers labeled)", "Where Quotr Procurement fits — and when to do it yourself",
                  "Common mistakes", "FAQ", "Sources (expert-reviewed where noted)"]
        else:
            L_ = ["Quick answer: the method in 4–6 steps", "What do you need before you start? (plans, scale, specs)",
                  f"Step by step: measuring {unit}", "Waste factors and rules of thumb (sourced)", "Worked example on a real plan (anonymized, Quotr-processed)",
                  "Doing it faster with AI takeoff: what Quotr.ai automates and what you still check", f"Common {tr} estimating mistakes", "FAQ", "Sources"]
        if f == 'TPL': L_.insert(1, "Download the template (no email gate)")
    elif f == 'ANL':
        L_ = [f"Quick answer: {short(a['title'], 80)}", "The facts (dated table with sources)", "Who is affected and how (by trade / persona)",
              "What to do now (checklist)", "Where Quotr.ai fits (one paragraph, no hype)", "FAQ", "Sources"]
    elif f == 'DATA':
        L_ = ["Headline finding, brand-attached ('Quotr.ai's [study] found…')", "Key numbers (3–5)", "Method: sample, date range, definitions, limits",
              "Findings by segment (tables + one chart)", f"What it means for {a['persona']}", "Download the data (CSV) and how to cite it", "FAQ", "Methodology appendix"]
    elif f == 'METH':
        L_ = ["What we measure and why", "Test set: drawings, licensing, complexity", "Ground truth and scoring", "Procedure: versions, settings, runs",
              "Limits and conflicts of interest (Quotr.ai is a vendor)", "How to reproduce or request the data", "Changelog"]
    elif f == 'CASE':
        L_ = ["Result in one sentence (customer-attributed)", "The customer: who, trade, size, region", "The problem before", "What changed in the workflow",
              "Results: numbers, timeframe, how measured", "In their words (approved quote)", "What didn't change / limits", "Similar teams and next steps"]
    elif f == 'HUB':
        L_ = [f"Who this is for: {subj}", "The workflow: plans → takeoff → estimate → proposal → buy", "What Quotr.ai does at each step (confirmed features)",
              "Pricing for this team (Quotr.ai Lite / Plus / Quotr Service)", "Proof: customers and examples", "When Quotr.ai is not the right fit", "FAQ"]
    elif f == 'EVAL':
        L_ = ["Quick answer", "The checklist (numbered, with why each item matters)", "How to score vendors (table)", "Red flags", "Download the checklist", "FAQ"]
    elif f == 'PR':
        L_ = ["Headline", "Dateline + lede (who, what, why now)", "Key facts (approved Claim Ledger rows only)", "Approved founder quote", "About Quotr.ai (fact-sheet boilerplate)", "Media contact"]
    else:  # LOG
        L_ = ["What's new (dated bullets, shipped only)", "Why it matters for estimators", "What's next (no promises)", "Links to docs and trial"]
    if a['lang'] == 'es-US': L_ = ["(Write in Spanish; native reviewer required)"] + L_
    return '\n'.join(f"{i}. {x}" for i, x in enumerate(L_, 1))

TRADE_CODES = {'DRY', 'ELEC', 'PLMB', 'HVAC', 'FLR', 'FRM', 'ROOF', 'CONC', 'CAB', 'TILE', 'PNT', 'INS', 'SID', 'WIN'}
TIMELY = ('tariff', 'price', 'cost', 'budget', 'wage', 'code', 'lumber', 'shortage')
def faqs(a):
    f = a['fmt']; e = a['ent']; subj = ent(a, 'subject', head(a['title'], 60))
    if a['lane'] == 'R' and f == 'CMP':
        Q = [f"Why does the same building cost more in {e['a']} than in {e['b']}?", "Which cost lines differ most?", "How should I adjust an estimate between the two states?"]
    elif f == 'CMP' and 'a' in e and 'b' in e and not a['slugv'].startswith('how-builders-buy'):
        A_, B_ = e['a'], e['b']
        Q = [f"Is {A_} cheaper than {B_}?", f"Which is better for residential estimating, {A_} or {B_}?", f"Do {A_} and {B_} offer free trials?",
             f"Can {A_} and {B_} do AI takeoff from PDF plans?", f"How hard is it to switch from {B_} to {A_}?"]
    elif f == 'CMP':
        Q = ["Which route is cheapest overall?", "Which route is fastest?", "Who handles duties and customs in each route?", "What are the minimum order sizes?"]
    elif f == 'ALT':
        x = e['x']; Q = [f"What is the best alternative to {x} for a small team?", f"Is there a cheaper alternative to {x}?",
                         f"Which {x} alternatives include AI takeoff?", "Which alternatives offer done-for-you estimating?"]
    elif f == 'BEST':
        cat = e.get('cat', subj)
        Q = [f"What is the best {cat} for a small team?", f"How much does {cat} cost?", "How accurate is AI on this kind of work, and how do I check it?",
             "What should I test during a free trial?"]
    elif f == 'COST':
        Q = ["What is the typical range right now, and what is it based on?", f"What drives {subj}?", "How can I lower it without cutting quality?", "How often are these numbers updated?"]
    elif f in ('HOW', 'TPL') and a['cluster'] == 'CL01':
        Q = ["How long does it take end to end?", "What documents do I need?", "What does it cost beyond the product price?", "When is it not worth doing?"]
    elif f in ('HOW', 'TPL') and a['trade'].split(',')[0].strip() in TRADE_CODES:
        tr = e.get('trade', subj)
        Q = [f"How long does the {tr} takeoff take for a typical house?", f"What waste factor should I use for {tr}?", f"Can AI do the {tr} takeoff accurately?",
             f"What is the most common {tr} estimating mistake?"]
    elif f in ('HOW', 'TPL'):
        Q = ["How long does this take on a typical project?", "Which numbers should I double-check?", "Which steps can software do for me?", "What is the most common mistake?"]
    elif f == 'ANL' and any(k in a['title'].lower() for k in TIMELY):
        Q = ["What changed, and when?", "Who is affected most?", "What should I do this month?", "Where can I check the current numbers?"]
    elif f == 'ANL':
        Q = ["What does this mean for a small team?", "What are the limits?", "How do I apply this on my next bid?", "What should I read next?"]
    elif f == 'DATA':
        Q = ["How was this data collected?", "How big is the sample?", "Can I use or cite this data?", "How often is it updated?"]
    elif f == 'METH':
        Q = ["Why publish the method before the results?", "Who checks the results?", "Can I submit plans for testing?", "Is Quotr.ai's own tool tested the same way?"]
    elif f == 'CASE':
        Q = ["What did the customer use Quotr.ai for?", "How were the results measured?", "Would this work for a smaller team?"]
    elif f == 'HUB':
        Q = ["What does Quotr.ai cost for this team?", "Do I have to use Quotr Procurement?", "Is there a free trial?", "When is Quotr.ai not the right fit?"]
    elif f == 'EVAL':
        Q = ["How long should an evaluation take?", "What should I test first?", "What is the biggest red flag?"]
    else:
        Q = ["(No FAQ for this format)"]
    if a['lang'] == 'es-US': Q = ["(write FAQ in Spanish)"] + Q
    return '\n'.join('• ' + x for x in Q)

LEDE_TMPL = {
 'CMP': "40–80 words: who each tool is for, the one dated price difference, and the factor that decides it. Put 'Quotr.ai' inside the fact sentence where it appears.",
 'ALT': "40–80 words: the 3 best alternatives by situation in one sentence each; when to stay.",
 'BEST': "40–80 words: the shortlist by situation (not a ranking), with the date checked; disclose Quotr.ai is ours.",
 'COST': "40–80 words: the typical range with an 'as of' date and source, plus the 2 biggest cost drivers.",
 'HOW': "40–80 words: the method in one sentence per step, with the key number (waste factor / unit) and its source.",
 'TPL': "40–80 words: what the template does and the one decision it makes easier.",
 'ANL': "40–80 words: what changed (with date), who it affects, and the one action to take now.",
 'DATA': "40–80 words: the headline finding with 'Quotr.ai's [study] found…', sample size and date range.",
 'METH': "40–80 words: what is measured, how ground truth is set, and that results follow under this method.",
 'CASE': "40–80 words: the customer, the result (approved number), and the timeframe.",
 'HUB': "40–80 words: who it's for, what Quotr.ai does for them, the entry price (Quotr.ai Lite $79.90/seat/month).",
 'EVAL': "40–80 words: the 3 checks that matter most and why.",
 'PR': "Dateline + one-sentence news + one-sentence context, approved facts only.",
 'LOG': "One sentence: the most useful shipped change this month.",
}
LEDE_HOWP = "40–80 words: what it is, the process in one line per step, and the one cost, time or document that matters most (sourced)."
DRAFTED = {'ART-001', 'ART-002', 'ART-003'}
DRAFT_FILES = {'ART-001': 'ART-001-ai-takeoff-software-pricing-compared.md', 'ART-002': 'ART-002-kitchen-cabinet-vanity-tariffs.md',
               'ART-003': 'ART-003-bay-area-factory-direct-finish-materials.md'}

# siblings by cluster
by_cluster = defaultdict(list)
for a in ARTS: by_cluster[a['cluster']].append(a)
def links(a):
    cl = CLUSTER[a['cluster']]
    sib = [b for b in by_cluster[a['cluster']] if b['id'] != a['id']]
    sib.sort(key=lambda b: (abs((b['date'] - a['date']).days), b['id']))
    rel = '; '.join(f"{b['id']} {short(b['title'], 45)}" for b in sib[:2])
    return f"Pillar: {cl[2]}\nProduct: {cl[3]}\nRelated: {rel}"

# ================================================================== ARTICLE PIPELINE
ws = wb['Article Pipeline']
NEWH = ['Cluster', 'Primary query (buyer question)', 'Target prompts (T#)', 'Funnel', 'Persona', 'Trade', 'Format', 'Quotr-only angle (why only Quotr can write this)',
        'URL slug (no year)', 'Meta description', 'Schema graph', 'Author (byline)', 'Gate / dependency', 'Gated?', 'Priority', 'Roadmap ref', 'Target words', 'Adaptation set']
header(ws, 4, NEWH, 19)
ws['M4'] = 'Required claims (CLM IDs)'; ws['P4'] = 'Adaptations planned (non-owned)'; ws['R4'] = 'URL path'
title(ws, 'ORIGINAL ARTICLE PRODUCTION', '195 specified articles × 13 weeks: 3/business day, lane mix 4 competitor · 7 industry · 2 regional · 1 research · 1 benchmark per week. Gated rows publish only after the gate clears (swap rule: Production SOP).', 36)
for i, a in enumerate(ARTS):
    r = 5 + i
    assert ws.cell(r, 1).value == a['id'], (r, ws.cell(r, 1).value, a['id'])
    assert ws.cell(r, 2).value == a['week'] and ws.cell(r, 3).value == a['day'] and ws.cell(r, 4).value == a['slot']
    ws.cell(r, 6).value = a['laneN']
    ws.cell(r, 7).value = a['title']
    if a['id'] in DRAFTED: ws.cell(r, 9).value = 'Drafting'
    ws.cell(r, 11).value = ', '.join(PERSONA_NAMES[p.strip()] for p in a['persona'].split(','))
    ws.cell(r, 12).value = a['region']
    ws.cell(r, 13).value = req_claims(a)
    ws.cell(r, 16).value = f"=COUNTIF('Placement Log'!$D$5:$D$354,A{r})-COUNTIFS('Placement Log'!$D$5:$D$354,A{r},'Placement Log'!$C$5:$C$354,\"Quotr.ai*\")"
    if a['id'] in DRAFTED: ws.cell(r, 17).value = f"Full draft + JSON-LD + channel adaptations: content-os/articles/{DRAFT_FILES[a['id']]}"
    ws.cell(r, 18).value = a['path']
    fmtlabel = FORMATS[a['fmt']][0]
    vals = [f"{a['cluster']} {CLUSTER[a['cluster']][1]}", a['query'], a['prompts'], a['funnel'], a['persona'], a['trade'], fmtlabel,
            a['angle'] or '', a['slugv'], meta(a), FORMATS[a['fmt']][3], a['author'], gate_text(a['gate']),
            f'=IF(LEFT(AE{r},4)="None","No","Yes")', a['prio'], a['ref'], FORMATS[a['fmt']][2], ' · '.join(LANE_CHANNELS[a['laneN']])]
    for j, v in enumerate(vals):
        c = ws.cell(r, 19 + j, v); c.font = font()
    for c in range(1, 37): ws.cell(r, c).font = font();
    for c in (13, 26, 28, 31): ws.cell(r, c).alignment = Alignment(wrap_text=False, vertical='top')
widths(ws, {'S': 30, 'T': 46, 'U': 16, 'V': 9, 'W': 14, 'X': 10, 'Y': 20, 'Z': 60, 'AA': 36, 'AB': 50, 'AC': 26, 'AD': 18, 'AE': 36,
            'AF': 9, 'AG': 9, 'AH': 10, 'AI': 14, 'AJ': 40, 'M': 30, 'P': 14, 'R': 44})
ws.auto_filter.ref = 'A4:AJ199'
dv_list(ws, 'AG5:AG199', ['P1', 'P2', 'P3']); dv_list(ws, 'V5:V199', ['TOFU', 'MOFU', 'BOFU'])
ws.conditional_formatting.add('AF5:AF199', CellIsRule(operator='equal', formula=['"Yes"'], fill=fill('FDE2C8')))
ws.conditional_formatting.add('I5:I199', CellIsRule(operator='equal', formula=['"Published"'], fill=fill('C6EFCE')))
ws.conditional_formatting.add('I5:I199', CellIsRule(operator='equal', formula=['"Blocked"'], fill=fill('FFC7CE')))
ws.conditional_formatting.add('AG5:AG199', CellIsRule(operator='equal', formula=['"P1"'], font=Font(name=FN, bold=True, color='9C0006')))

# ================================================================== ARTICLE BRIEFS
wsb = new_sheet('Article Briefs')
title(wsb, 'ARTICLE BRIEFS + STRUCTURED DATA (one row per article)', 'Columns B–F, J, N, P–R pull live from Article Pipeline. Col. S builds BlogPosting + BreadcrumbList JSON-LD from the row — paste into the CMS or emit from the template. Set T to Ready at T-5.', 26)
BH = ['Article ID', 'Planned date', 'Lane', 'Working title', 'Format', 'Primary query', 'Answer-first lede (40–80 words)', 'H2 outline (question-led)', 'FAQ questions (visible FAQ → FAQPage)',
      'Required claims (Claim Ledger)', 'Must not say', 'Internal links', 'CTA', 'Author', 'Author slug', 'URL path', 'Meta description', 'Schema graph',
      'JSON-LD (BlogPosting + BreadcrumbList, auto-built)', 'Brief status', 'Brief owner', 'Breadcrumb section', 'Section URL', 'Schema date', 'Language', 'Author schema name']
header(wsb, 4, BH)
PIPE = "'Article Pipeline'!"
def look(col, r): return f"=INDEX({PIPE}${col}$5:${col}$199,MATCH($A{r},{PIPE}$A$5:$A$199,0))"
def esc(ref): return f'SUBSTITUTE({ref},CHAR(34),"\\"&CHAR(34))'
for i, a in enumerate(ARTS):
    r = 5 + i
    put(wsb, r, 1, a['id'])
    put(wsb, r, 2, look('E', r), fmt='mmm d, yyyy')
    put(wsb, r, 3, look('F', r)); put(wsb, r, 4, look('G', r)); put(wsb, r, 5, look('Y', r)); put(wsb, r, 6, look('T', r))
    tmpl = LEDE_HOWP if (a['fmt'] in ('HOW', 'TPL') and a['cluster'] == 'CL01') else LEDE_TMPL[a['fmt']]
    lede = ("DRAFTED — content-os/articles/" + DRAFT_FILES[a['id']] + " (use its answer-first paragraph)") if a['id'] in DRAFTED else tmpl
    put(wsb, r, 7, lede, fl=fill(INPUT))
    put(wsb, r, 8, outline(a)); put(wsb, r, 9, faqs(a))
    put(wsb, r, 10, look('M', r))
    put(wsb, r, 11, NEVER.get(a['cluster'], '') + GLOBAL_NEVER)
    put(wsb, r, 12, links(a)); put(wsb, r, 13, CLUSTER[a['cluster']][5])
    put(wsb, r, 14, look('AD', r)); put(wsb, r, 15, AUTHOR_SLUG[a['author']]); put(wsb, r, 16, look('R', r))
    put(wsb, r, 17, look('AB', r)); put(wsb, r, 18, look('AC', r))
    put(wsb, r, 20, 'Ready' if a['id'] in DRAFTED else ('Not started' if a['gate'] == 'G0' else 'Waiting on gate'), fl=fill(INPUT))
    put(wsb, r, 21, 'TKC', fl=fill(INPUT))
    put(wsb, r, 22, a['section'][0]); put(wsb, r, 23, a['section'][1])
    put(wsb, r, 24, f"=IF(COUNT(INDEX({PIPE}$H$5:$H$199,MATCH($A{r},{PIPE}$A$5:$A$199,0)))=0,B{r},INDEX({PIPE}$H$5:$H$199,MATCH($A{r},{PIPE}$A$5:$A$199,0)))", fmt='yyyy-mm-dd')
    put(wsb, r, 25, a['lang']); put(wsb, r, 26, AUTHOR_SCHEMA[a['author']])
    D, Q_, P, X, N, O, V, W, Y = f'D{r}', f'Q{r}', f'P{r}', f'X{r}', f'Z{r}', f'O{r}', f'V{r}', f'W{r}', f'Y{r}'
    parts = [q('{"@context":"https://schema.org","@graph":[{"@type":"BlogPosting","@id":"https://quotr.ai'), P,
             q('#article","mainEntityOfPage":"https://quotr.ai'), P, q('","headline":"'), esc(D), q('","description":"'), esc(Q_),
             q('","datePublished":"'), f'TEXT({X},"yyyy-mm-dd")', q('","dateModified":"'), f'TEXT({X},"yyyy-mm-dd")', q('","inLanguage":"'), Y,
             q('","author":{"@type":"Person","@id":"https://quotr.ai/authors/'), O, q('/#person","name":"'), N, q('","url":"https://quotr.ai/authors/'), O,
             q('/","worksFor":{"@id":"https://quotr.ai/#organization"}},"publisher":{"@id":"https://quotr.ai/#organization"},"isPartOf":{"@id":"https://quotr.ai/#website"}},{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://quotr.ai/"},{"@type":"ListItem","position":2,"name":"'),
             V, q('","item":"https://quotr.ai'), W, q('"},{"@type":"ListItem","position":3,"name":"'), esc(D), q('"}]}]}')]
    put(wsb, r, 19, '=' + '&'.join(parts))
    for c in (7, 8, 9, 11, 12): wsb.cell(r, c).alignment = WRAP
    wsb.row_dimensions[r].height = 150
dv_list(wsb, 'T5:T199', ['Not started', 'Waiting on gate', 'In brief', 'Ready', 'Drafted', 'Published'])
widths(wsb, {'A': 10, 'B': 12, 'C': 16, 'D': 42, 'E': 16, 'F': 32, 'G': 40, 'H': 58, 'I': 44, 'J': 22, 'K': 40, 'L': 44, 'M': 26, 'N': 16, 'O': 13,
             'P': 30, 'Q': 40, 'R': 22, 'S': 40, 'T': 14, 'U': 10, 'V': 11, 'W': 12, 'X': 11, 'Y': 9, 'Z': 14})
wsb.freeze_panes = 'E5'
wsb.auto_filter.ref = 'A4:Z199'
wsb.conditional_formatting.add('T5:T199', CellIsRule(operator='equal', formula=['"Ready"'], fill=fill('C6EFCE')))
wsb.conditional_formatting.add('T5:T199', CellIsRule(operator='equal', formula=['"Waiting on gate"'], fill=fill('FDE2C8')))

# ================================================================== CLAIM LEDGER
ws = wb['Claim Ledger']
title(ws, 'CLAIM VERIFICATION LEDGER', f'{len(CLAIMS)} claims pre-loaded from the GEO brain fact sheet (Sept 25, 2026). In review = sourced, awaiting a named Quotr reviewer. TO CONFIRM rows block publication. NEVER USE rows are rejected wording. Target 30–40 NEW verified claims/week.', 16)
ws['M4'] = 'Articles requiring this claim (count)'
for i, c in enumerate(CLAIMS):
    r = 5 + i
    typ, claim, src, sdate, entity, status, conf, note, first, recheck, disc = c
    vals = {2: typ, 3: claim, 4: src, 5: sdate, 6: entity, 7: status, 10: conf, 11: note, 12: first, 14: recheck, 15: disc,
            16: 'Quotr approver' if typ in ('TO CONFIRM',) else 'TKC'}
    for col, v in vals.items(): ws.cell(r, col).value = v
    ws.cell(r, 13).value = f'=COUNTIF({PIPE}$M$5:$M$199,"*"&A{r}&"*")'
    for col in range(1, 17): ws.cell(r, col).font = font()
ws.conditional_formatting.add('B5:B204', CellIsRule(operator='equal', formula=['"TO CONFIRM"'], fill=fill('FDE2C8')))
ws.conditional_formatting.add('B5:B204', CellIsRule(operator='equal', formula=['"NEVER USE"'], fill=fill('FFC7CE')))

# ================================================================== AI PROMPT BANK + CHECKS
ws = wb['AI Prompt Bank']
title(ws, '53-PROMPT AI SEARCH TRACKER (real Sept 2026 tracking set)', 'PR-01–PR-32 = the 32 unbranded core prompts (weekly, 4 engines → AI Answer Checks). PR-33–PR-53 = brand + extension prompts (monthly). Copy prompts exactly. Source: geo-brain/04-prompt-library/tracking-set.md', 13)
header(ws, 4, ['Prompt ID', 'Prompt (verbatim — copy exactly)', 'ICP', 'Geo context', 'Stage', 'Tracking cadence', 'Sept 2026 baseline (Perplexity)', 'Owner',
               'Named instead / watch for', 'Tracking ID', 'Tier', 'Pages targeting (new + refresh)'])
proto = [copy.copy(ws.cell(36, c)._style) for c in range(1, 10)]
for i, p in enumerate(PROMPTS):
    r = 5 + i
    t, txt, stage, per, tier, base, named, geo = p
    vals = [f'PR-{i + 1:02d}', txt, ', '.join(PERSONA_NAMES[x.strip()] for x in per.split(',')), geo, stage,
            'Weekly core (4 engines)' if i < 32 else 'Monthly (brand / extension)', base, 'TKC', named, t, tier,
            f'=COUNTIF({PIPE}$U$5:$U$199,"*"&J{r}&"*")+COUNTIF(\'Refresh Queue\'!$F$5:$F$40,"*"&J{r}&"*")']
    for j, v in enumerate(vals):
        c = ws.cell(r, j + 1, v); c.font = font()
widths(ws, {'J': 11, 'K': 6, 'L': 14, 'G': 40, 'I': 50})
ws.conditional_formatting.add('L5:L57', CellIsRule(operator='equal', formula=['0'], fill=fill('FDE2C8')))
wsc = wb['AI Answer Checks']
for r in range(5, 1669):
    wsc.cell(r, 6).value = f"=INDEX('AI Prompt Bank'!$B$5:$B$57,MATCH($C{r},'AI Prompt Bank'!$A$5:$A$57,0))"
wsc['A2'] = '13 weekly cycles × 32 core prompts × 4 assistants = 1,664 planned tests; prompt text pulls live from AI Prompt Bank. Weekly results are noisy (40–60% of cited domains change month to month): judge 4-week rolling trends.'

# ================================================================== COMPETITORS
ws = wb['Competitors']
COMP = [
 ("Togal.AI", "AI takeoff", "togal.ai", "https://www.togal.ai/sitemap.xml (verify)", "Growth $299/user/mo billed yearly; Business custom 4+ users (togal.ai/pricing, Sept 2026). Named in 8/32 unbranded Perplexity answers. Quotr's Togal-alternatives post was cited in T16."),
 ("STACK", "Takeoff / estimating", "stackct.com", "https://www.stackct.com/sitemap.xml (verify)", "Free tier; ~1,400 Capterra / <100 G2 reviews. Named in 10/32 — the default all-rounder. Quotr's stack-alternative post spreads an old price (refresh REF-03)."),
 ("PlanSwift", "Takeoff / estimating", "planswift.com", "https://www.planswift.com/sitemap.xml (verify)", "ConstructConnect-owned (not Trimble). From ~$2,000 first seat/yr (CC, Jul 2026) vs $1,749 in Quotr's post — re-check. Windows desktop. Named in 10/32."),
 ("Kreo", "AI construction takeoff", "kreo.net", "https://www.kreo.net/sitemap.xml (verify)", "Plans named Lite ($35) and Plus ($70) — clash with Quotr.ai plan names; AI tools priced higher. Nomic's Kreo-alternatives list names Quotr.ai #5 with a stale price."),
 ("Beam AI", "AI quantity takeoff", "ibeam.ai", "https://www.ibeam.ai/sitemap.xml (verify)", "Done-for-you ~$15–25K/yr per trade (ConstructConnect). 21 compare pages (strongest comparison hub). Engines confuse it with trybeam.com."),
 ("Handoff", "AI estimating", "handoff.ai", "https://www.handoff.ai/sitemap.xml (verify)", "Flex $119 / Pro $239 / Scale $719 per mo billed annually; 7-day trial. Residential remodelers/builders; Lowe's purchasing; AI takeoff limited to residential plans ≤5,000 sq ft."),
 ("On-Screen Takeoff", "Digital takeoff", "oncenter.com", "https://www.oncenter.com/sitemap.xml (verify)", "ConstructConnect-owned legacy desktop. Togal's peer-reviewed study benchmarks against it."),
 ("Buildxact", "Residential builder platform", "buildxact.com", "https://www.buildxact.com/sitemap.xml (verify)", "Named in 10/32 — as often as STACK. Dealer pricing + Home Depot ordering. 98% of Capterra reviewers are small businesses."),
 ("Bluebeam", "PDF markup + takeoff", "bluebeam.com", "https://www.bluebeam.com/sitemap.xml (verify)", "Basics $260 / Core $330 / Complete $440 / Max $590 per user/yr (search summary, re-check); Max AI tier May 2026. No estimating database or procurement."),
]
title(ws, 'COMPETITOR WATCH (7 core + 2 adjacent)', 'Monitoring design: hourly sitemap polling target, daily analyst brief, independent source verification. Facts from geo-brain/03-market/competitors (Sept 2026) — re-verify before use in articles.', 13)
for i, (n_, cat, dom, sm, note) in enumerate(COMP):
    r = 5 + i
    if r >= 12:
        for c in range(1, 14): ws.cell(r, c)._style = copy.copy(ws.cell(11, c)._style)
        ws.cell(r, 5).value = 60; ws.cell(r, 6).value = 'Candidate'; ws.cell(r, 7).value = 'P2'; ws.cell(r, 8).value = 'TKC'
    ws.cell(r, 1).value = n_; ws.cell(r, 2).value = cat; ws.cell(r, 3).value = dom; ws.cell(r, 4).value = sm; ws.cell(r, 12).value = note
    ws.cell(r, 11).value = f"=COUNTIF('Change Monitor'!$C$5:$C$124,A{r})"
    ws.cell(r, 12).alignment = WRAP; ws.row_dimensions[r].height = 48
for dv in ws.data_validations.dataValidation:
    s = str(dv.sqref)
    if s == 'F5:F11': dv.sqref = openpyxl.worksheet.cell_range.MultiCellRange('F5:F13')
    if s == 'G5:G11': dv.sqref = openpyxl.worksheet.cell_range.MultiCellRange('G5:G13')

# ================================================================== REGIONAL GEO
ws = wb['Regional GEO']
REG = {
 'Bay Area': ("Three published /procurement/ projects (Saratoga, Monte Sereno, Hillsborough) + Quotr Service estimates", "Approved project data; dates; cost scope; 'Client saved ~$0' bug fixed (FIX-28)", "/cost-guides/bay-area/ (proposed)", "No tracked prompt yet — add 'cost per square foot to build a house Bay Area'"),
 'Los Angeles': ("Line-item fire-rebuild costs from Quotr's LA rebuild sample + FireTips history (Feb 2025)", "Anonymized rebuild estimate; current city/county sources", "/cost-guides/los-angeles-fire-rebuild/ (proposed)", "T47 Absent (Sept 2026 Perplexity); Bloomberg + local GCs cited"),
 'California': ("Statewide code-driven cost (Title 24, CALGreen, prevailing wage) + finish-level cost per sq ft", "Cited code sections and dated cost sources", "/cost-guides/california/ (proposed regional hub)", "T45 Absent (multifamily cost/sq ft); no CA-specific prompt tracked"),
 'Florida': ("CA vs FL cost comparison; hurricane-code windows (procurement tie-in)", "Apples-to-apples sources; procurement delivery area confirmed", "/cost-guides/florida/ (proposed)", "Not tested"),
 'Spanish-language': ("Pilot 3 highest-intent Spanish pages (takeoff, drywall, AI estimating software)", "Native review; buyer-language prompt test first", "/es/blog/ (proposed)", "Not tested"),
}
ws['H4'] = 'Planned articles / week (from pipeline)'; ws['I4'] = 'Page / hub URL'; ws['J4'] = 'AI baseline (Sept 2026)'
for r in range(5, 10):
    m = ws.cell(r, 1).value
    d, e_, url, base = REG[m]
    ws.cell(r, 4).value = d; ws.cell(r, 5).value = e_; ws.cell(r, 9).value = url; ws.cell(r, 10).value = base
    ws.cell(r, 8).value = f"=COUNTIFS({PIPE}$F$5:$F$199,\"Regional GEO\",{PIPE}$L$5:$L$199,A{r})/Settings!$B$7"
    ws.cell(r, 8).number_format = '0.0'
    for c in (4, 5, 10): ws.cell(r, c).alignment = WRAP
    ws.row_dimensions[r].height = 45
widths(ws, {'J': 40})

# ================================================================== AUDIT FIXES
ws = wb['Audit Fixes']
NEWFIX = [
 ("Replace retired Solo/Team pricing on ~13 URLs + llms.txt; request re-crawls", "Facts", "Critical", "TKC + developer", "Week 1", "AI answers quote 'from $299.90'"),
 ("Delete the 'Quotr should be cited' block from llms.txt; fix its links", "Technical SEO", "High", "Quotr developer", "Week 1", "Resembles prompt injection"),
 ("Rewrite /disambiguation/ as a plain company-facts page; one Organization @id", "Entity", "High", "TKC + developer", "Days 1–30", "Refresh Queue REF-02"),
 ("Keep test.quotr.io noindexed + removal requests; quotr.io page-level 301s", "Technical SEO", "High", "Quotr developer", "Week 1", "Staging host still cited"),
 ("Fix the 'Client saved ~$0' display bug on /procurement/", "Facts", "High", "Quotr developer", "Week 1", "Blocks ART-003"),
 ("Editorial sweep: leftover brief text, utm_source=chatgpt.com, unsourced stats, investor quote labelled as customer", "Editorial", "High", "TKC", "Days 1–30", "Sweep rows 30–41"),
 ("Correct competitor facts in old posts (PlanSwift ownership, STACK price/reviews, Togal price)", "Claims", "High", "TKC", "Days 1–30", "Claim Ledger competitor rows"),
 ("Merge duplicate Togal posts and estimating-services posts (301)", "Content recovery", "High", "TKC + developer", "Days 1–30", "Refresh Queue REF-04, REF-06"),
 ("Create author pages (Hanyang Liu; Junzhe Shi, PhD) with ProfilePage schema", "Structured data", "Medium", "Developer + TKC", "Days 1–30", "Schema Library SCH-07"),
 ("Send correction emails with the fact sheet to Nomic, Octopus Builds, ForesightIQ", "Off-site authority", "Medium", "TKC", "Days 1–30", "Pages repeat stale pricing"),
 ("Emit BlogPosting + Breadcrumb JSON-LD from the blog template front matter", "Structured data", "High", "Quotr developer", "Days 1–30", "Article Briefs col. S"),
]
for i, (act, ws_, sev, team, ph, note) in enumerate(NEWFIX):
    r = 28 + i
    for c in range(1, 13): ws.cell(r, c)._style = copy.copy(ws.cell(27, c)._style)
    vals = {1: f'FIX-{24 + i}', 2: act, 3: ws_, 4: sev, 5: team, 6: ph, 7: 'Open', 11: note}
    for c, v in vals.items(): ws.cell(r, c).value = v
for dv in ws.data_validations.dataValidation:
    if str(dv.sqref) == 'G5:G27': dv.sqref = openpyxl.worksheet.cell_range.MultiCellRange('G5:G40')
ws['A2'] = '34 actionable issues (23 from the November audit + 11 from the GEO brain fact-fix sweep), organized for week-one triage and 90-day closure.'
wb['Dashboard']['D17'] = "=COUNTIF('Audit Fixes'!G5:G40,\"Closed\")"

# ================================================================== SETTINGS additions
ws = wb['Settings']
band(ws, 24, 'CONTENT MACHINE (v2) — lane mix, publishing, capacity', 8)
S_ROWS = [
 (25, 'Competitor / alternatives per week', 4, 'Was 5/wk; reduced — the "X alternatives" space is saturated (white-space.md)', True),
 (26, 'Industry analysis per week', 7, 'Trade how-tos, procurement/tariffs, estimating explainers, proof pages', True),
 (27, 'Regional GEO per week', 2, 'Was 3/wk; only where regional evidence exists (doorway-page risk)', True),
 (28, 'Original research per week', 1, 'Data-gated after week 1 (public-data compilations first)', True),
 (29, 'Benchmark analysis per week', 1, 'Method + public-claims analysis first; results only after tests', True),
 (30, 'Lane mix total (must equal B8)', '=SUM(B25:B29)', 'Check: Dashboard I13', False),
 (31, 'Gate swap threshold (business days before slot)', 5, 'Swap a gated article if not cleared by then', True),
 (32, 'Publish slot 1 time (PT)', '09:00', 'Competitor or industry slot', True),
 (33, 'Publish slot 2 time (PT)', '11:00', '', True),
 (34, 'Publish slot 3 time (PT)', '14:00', '', True),
 (35, 'Hours per article — brief', 0.5, 'Assumption (TKC to calibrate after week 2)', True),
 (36, 'Hours per article — evidence & claims', 0.75, 'Assumption', True),
 (37, 'Hours per article — AI-assisted draft + writer pass', 1.5, 'Assumption', True),
 (38, 'Hours per article — fact check + edit', 1.0, 'Assumption', True),
 (39, 'Hours per article — schema, links, CMS', 0.4, 'Assumption', True),
 (40, 'Hours per article — adaptations', 0.6, 'Assumption', True),
 (41, 'Hours per article (total)', '=SUM(B35:B40)', 'Calculated', False),
 (42, 'Productive hours per FTE per day', 6, 'Assumption', True),
 (43, 'FTE required at current throughput', '=B6*B41/B42', 'Calculated: articles/day × hours/article ÷ productive hours', False),
 (44, 'AI answer-check cadence', 'Weekly core (128)', 'Tracking set recommends monthly; weekly results are noisy — judge 4-week trends', True),
 (45, 'Content OS version', 'v2 — 2026-11-13', 'Built from v1 + geo-brain (Sept 25, 2026)', False),
]
for r, lab, val, note, inp in S_ROWS:
    put(ws, r, 1, lab); c = put(ws, r, 2, val, fl=fill(INPUT if inp else CALC)); put(ws, r, 3, note)
    if isinstance(val, float) or r in (41, 43): c.number_format = '0.00'
band(ws, 47, 'US HOLIDAYS IN THE 13-WEEK WINDOW (Daily Capacity flags these)', 8)
HOL = [(dt.date(2026, 11, 26), 'Thanksgiving'), (dt.date(2026, 11, 27), 'Day after Thanksgiving'), (dt.date(2026, 12, 24), 'Christmas Eve'),
       (dt.date(2026, 12, 25), 'Christmas'), (dt.date(2026, 12, 31), "New Year's Eve"), (dt.date(2027, 1, 1), "New Year's Day"), (dt.date(2027, 1, 18), 'MLK Day')]
for i, (d, n_) in enumerate(HOL):
    put(ws, 48 + i, 1, n_); put(ws, 48 + i, 2, d, fl=fill(INPUT), fmt='mmm d, yyyy'); put(ws, 48 + i, 3, 'Produce the prior week; pre-schedule in CMS')
ws['B21'] = '=COUNTA(Competitors!A5:A13)'; ws['C21'] = 'Calculated from Competitors (7 core + Buildxact, Bluebeam)'
ws['B12'] = 32; ws['C12'] = 'Real Sept 2026 tracking set: 32 unbranded core prompts (AI Prompt Bank PR-01–PR-32); 21 more run monthly'

# ================================================================== DAILY CAPACITY holiday column
ws = wb['Daily Capacity']
header(ws, 4, ['Holiday / note'], 12)
for r in range(5, 70):
    put(ws, r, 12, f'=IF(COUNTIF(Settings!$B$48:$B$54,B{r})>0,"US holiday — pre-schedule","")')
ws.column_dimensions['L'].width = 26
ws.conditional_formatting.add('L5:L69', FormulaRule(formula=['LEN(L5)>0'], fill=fill('FDE2C8')))

# ================================================================== PLACEMENT LOG pre-plan (weeks 1–4, base plan)
ws = wb['Placement Log']
header(ws, 4, ['Planned date'], 14)
ws.column_dimensions['N'].width = 14
ws['A2'] = 'One row per placement. Weeks 1–4 are pre-planned to the BASE plan (15 owned + 5 LinkedIn + 1 Medium + 0.5 Substack per week = 21.5). Set Status/Date/URL when live; original article count is never derived from placements.'
OWNED = {'C': 'Quotr.ai blog', 'I': 'Quotr.ai blog', 'R': 'Quotr.ai blog', 'S': 'Quotr.ai research', 'B': 'Quotr.ai benchmarks'}
PL = []
for wk in range(1, 5):
    wa = [a for a in ARTS if a['week'] == wk]
    for a in wa: PL.append((a, OWNED[a['lane']], 'Original article', 0, 'Canonical: ', ''))
    li = [a for a in wa if a['lane'] in 'SB'] + sorted([a for a in wa if a['lane'] not in 'SB' and a['prio'] == 'P1'], key=lambda x: x['id'])
    li += [a for a in wa if a not in li]
    for a in li[:5]: PL.append((a, 'LinkedIn company', 'Native post (≤1,300 chars)', 0, 'LinkedIn company: ', 'linkedin'))
    med = next(a for a in wa if a['lane'] == 'S')
    PL.append((med, 'Medium', 'Edited adaptation + canonical', 3, 'Medium adaptation: ', 'medium'))
    if wk % 2 == 0:
        PL.append((med, 'Substack', 'Research issue (2 weeks)', 4 - med['dayidx'], 'Substack issue: ', 'substack'))
for i, (a, dest, fmt_, off, pre, src) in enumerate(PL):
    r = 5 + i
    ws.cell(r, 3).value = dest; ws.cell(r, 4).value = a['id']
    ws.cell(r, 5).value = f"={q(pre)}&INDEX({PIPE}$G$5:$G$199,MATCH(D{r},{PIPE}$A$5:$A$199,0))"
    ws.cell(r, 7).value = 'TKC'; ws.cell(r, 9).value = fmt_
    ws.cell(r, 10).value = (f'="utm_source={src}&utm_medium=social&utm_campaign="&D{r}' if src else 'canonical')
    ws.cell(r, 11).value = f"=INDEX({PIPE}$M$5:$M$199,MATCH(D{r},{PIPE}$A$5:$A$199,0))"
    ws.cell(r, 14).value = f"=INDEX({PIPE}$E$5:$E$199,MATCH(D{r},{PIPE}$A$5:$A$199,0))+{off}"
    ws.cell(r, 14).number_format = 'mmm d, yyyy'
    for c in range(1, 15): ws.cell(r, c).font = font()
N_PL = len(PL)

# ================================================================== ECONOMICS additions
ws = wb['Economics']
band(ws, 28, 'UNIT ECONOMICS OF THE REVISED 3-ARTICLES/DAY SCOPE (edit hours in Settings B35:B42)', 10)
ECO = [
 (29, 'Original articles per 4-week cycle', '=Settings!B9', '0', 'Linked'),
 (30, 'Base fee per month (USD)', '=Settings!B15', '$#,##0', 'Linked'),
 (31, 'Fee per original article (USD)', '=B30/B29', '$#,##0.00', 'Before distribution, research, monitoring, MCP'),
 (32, 'Production hours per article', '=Settings!B41', '0.00', 'Settings assumption'),
 (33, 'Production hours per 4-week cycle', '=B29*B32', '#,##0', 'Articles only; excludes AI checks, outreach, monitoring'),
 (34, 'Implied revenue per production hour (USD)', '=B30/B33', '$#,##0.00', 'If this is below loaded cost, the scope is underpriced'),
 (35, 'FTE required for articles alone', '=Settings!B43', '0.0', 'Linked'),
 (36, 'Target loaded cost per hour (USD) — input', 45, '$#,##0', 'ASSUMPTION — replace with TKC\'s real loaded cost'),
 (37, 'Fee needed to cover article production at target rate (USD/month)', '=B33*B36', '$#,##0', 'Production cost only, no margin'),
 (38, 'Gap vs current base fee (USD/month)', '=B37-B30', '$#,##0;($#,##0);-', 'Positive = revised scope needs a price amendment'),
]
for r, lab, f_, nf, note in ECO:
    put(ws, r, 1, lab); put(ws, r, 2, f_, fl=fill(INPUT if r == 36 else CALC), fmt=nf); put(ws, r, 3, note)

# ================================================================== DASHBOARD block
ws = wb['Dashboard']
widths(ws, {'F': 30, 'G': 14, 'H': 28, 'I': 16, 'K': 26, 'L': 11, 'M': 11, 'N': 11})
put(ws, 4, 6, 'CONTENT MACHINE', font(True, 'FFFFFF'), fill(TEAL));
for c in (7, 8, 9): ws.cell(4, c).fill = fill(TEAL)
DB = [
 (5, 'Articles specified', "=COUNTA('Article Pipeline'!G5:G199)", 'Ungated (ready to brief)', "=COUNTIF('Article Pipeline'!AF5:AF199,\"No\")", None, None),
 (7, 'Briefs Ready', "=COUNTIF('Article Briefs'!T5:T199,\"Ready\")", 'Articles drafting', "=COUNTIF('Article Pipeline'!I5:I199,\"Drafting\")", None, None),
 (9, 'Claims in review', "=COUNTIF('Claim Ledger'!G5:G204,\"In review\")", 'Facts Quotr must confirm', "=COUNTIF('Claim Ledger'!B5:B204,\"TO CONFIRM\")", None, None),
 (11, 'Prompts tracked', "=COUNTA('AI Prompt Bank'!A5:A57)", 'Refreshes done', "=COUNTIF('Refresh Queue'!I5:I40,\"Done\")", None, None),
 (13, 'Placements planned', "=COUNTIF('Placement Log'!H5:H354,\"Planned\")-(350-COUNTA('Placement Log'!C5:C354))", 'Lane mix check', "=IF(Settings!B30=Settings!B8,\"OK\",\"Fix Settings B25:B29\")", None, None),
 (15, 'Revenue per production hour', '=Economics!B34', 'FTE required (articles)', '=Settings!B43', '$#,##0.00', '0.0'),
 (17, 'P1 articles', "=COUNTIF('Article Pipeline'!AG5:AG199,\"P1\")", 'P1 articles still gated', "=COUNTIFS('Article Pipeline'!AG5:AG199,\"P1\",'Article Pipeline'!AF5:AF199,\"Yes\")", None, None),
 (19, 'Monthly scope gap vs fee', '=Economics!B38', 'Prompts with no page planned', "=COUNTIF('AI Prompt Bank'!L5:L57,0)", '$#,##0', None),
]
for r, l1, f1, l2, f2, nf1, nf2 in DB:
    put(ws, r, 6, l1, font(True, DARK), fill(LIGHT)); put(ws, r, 7, f1, font(True, NAVY), fill(CALC), Alignment(horizontal='center'), nf1)
    put(ws, r, 8, l2, font(True, DARK), fill(LIGHT)); put(ws, r, 9, f2, font(True, NAVY), fill(CALC), Alignment(horizontal='center'), nf2)
header(ws, 4, ['Lane', 'Planned', 'Published', 'Gated'], 11)
for i, ln in enumerate(['Competitor / alternatives', 'Industry analysis', 'Regional GEO', 'Original research', 'Benchmark analysis']):
    r = 5 + i
    put(ws, r, 11, ln)
    put(ws, r, 12, f"=COUNTIF('Article Pipeline'!$F$5:$F$199,K{r})", al=Alignment(horizontal='center'))
    put(ws, r, 13, f"=COUNTIFS('Article Pipeline'!$F$5:$F$199,K{r},'Article Pipeline'!$I$5:$I$199,\"Published\")", al=Alignment(horizontal='center'))
    put(ws, r, 14, f"=COUNTIFS('Article Pipeline'!$F$5:$F$199,K{r},'Article Pipeline'!$AF$5:$AF$199,\"Yes\")", al=Alignment(horizontal='center'))
put(ws, 10, 11, 'Total', font(True));
for c, col in ((12, 'L'), (13, 'M'), (14, 'N')): put(ws, 10, c, f'=SUM({col}5:{col}9)', font(True), al=Alignment(horizontal='center'))
ws['A2'] = 'Targets update from Settings; actuals update from evidence-backed logs. Right block: content-machine readiness (specs, briefs, gates, claims, economics).'

# ================================================================== CONTEXT PACK
wsx = new_sheet('Context Pack')
title(wsx, 'QUOTR CONTEXT PACK — the only facts writers and AI tools may use', 'Source: geo-brain/ai-context-pack.md + entity-fact-sheet.md (verified Sept 25, 2026). Anything missing → write [TO CONFIRM: …]. Paste the AI briefing cell (bottom of this sheet) into any AI tool before drafting.', 3)
CTX = [
 ("WHAT QUOTR.AI IS", None),
 ("Name / entity", "Quotr.ai (short form 'Quotr'), formerly Quotr.io. Built by FLOZ Inc., a Delaware corporation. Website https://quotr.ai/ (no www)."),
 ("Category line", "AI construction takeoff, estimating and bid software, with a done-for-you estimating service and factory-direct material procurement."),
 ("Quotr Software", "AI takeoff from PDF plans (symbol counts, lengths, areas), estimating, bid management, supplier price comparison, proposals, and the Quotr.ai AI Agent that answers questions about the drawings."),
 ("Quotr Service", "Done-for-you takeoffs, cost estimates and pro formas. $0.25 per sq ft under 50,000 sq ft; $0.10 per sq ft at 50,000 sq ft and above; price sent before work starts."),
 ("Quotr Procurement", "Factory-direct materials from manufacturers in China, delivered duty-paid. Categories (TO CONFIRM): windows and doors, cabinetry and millwork, flooring, bath and plumbing fixtures. Optional — the software works without it."),
 ("Software pricing", "Quotr.ai Lite $79.90 and Quotr.ai Plus $299.90 per seat per month; Enterprise custom; 7-day free trial (live since Sep 14, 2026). Plus adds advanced AI, full Quotr database, 2 h onboarding, project sharing, 2,000 sq ft takeoff credits/month, 10% off procurement."),
 ("TEAM, PROOF, POSITION", None),
 ("Founders", "Hanyang Liu (CEO; trained architect) and Junzhe Shi, PhD (CTO; AI and systems engineering at Apple and UC Berkeley). Friends since middle school. Other bylines (titles TO CONFIRM): Tianyi Zong (COO), Jati Ibloguen (Growth)."),
 ("Backing", "Berkeley SkyDeck Batch 19; investors include the Berkeley SkyDeck Fund and Llama Ventures. Funding amount TO CONFIRM."),
 ("Usable proof", "Named customers: RL Electric, AlphaX, BiltWise Structures, Salisbury Moore (names only). RL Electric testimonial: takeoffs from about 20 hours to 1–2 hours. Quotr reports: Saratoga $97,000 vs $187K–$218K; Monte Sereno $108,290 vs $195K–$245K; Hillsborough $30,437 vs $58K–$76K. FireTips free LA rebuild app (Feb 2025)."),
 ("Differentiators (ranked)", "1) Only AI takeoff + estimating platform found that also sells factory-direct materials, delivered duty-paid. 2) Three ways to buy: do it yourself (Software), done for you (Service), buy the materials (Procurement). 3) Transparent low entry price ($79.90/seat/month) and published per-sq-ft service prices. 4) AI Agent for plain-English drawing questions (supporting). 5) Founder story: an architect and an engineer closing the design-to-cost gap."),
 ("Audiences (codes)", "SUB trade subcontractors (core Software buyer: electrical, drywall, flooring, plumbing, HVAC…) · GC general contractors / precon · RES residential builders, small GCs, remodelers · DEV real estate developers (Service + Procurement path) · FUND funds / lenders · BUY materials buyers · SVC estimating-service buyers."),
 ("RULES", None),
 ("Naming", "First mention 'Quotr.ai'. Never 'Quotr AI', 'QUOTR', 'Quoter', 'Quotr.io' (except 'formerly Quotr.io'). Write 'Quotr.ai Lite plan', never 'Lite' alone (Kreo sells Lite/Plus). Use 'Quotr Software / Quotr Service / Quotr Procurement'. Quotr.ai is not a quote/invoicing app and not the Quotr Pro app."),
 ("Never say", "Retired plans (Solo, Team, 1 User, 2–10 Users, 'from $299.90'); Quotr Pro ratings; '$190K seed'; SkyDeck '1% acceptance'; 'up to 80%' or '90% faster'; 'easily integrates'; 'industry-standard encryption'; 'a procurement program, not software'; any reviews, awards or press; self-ranked #1 lists; text addressed to AI or search engines."),
 ("TO CONFIRM (never state)", "HQ (San Francisco vs Berkeley); founding year (2023 vs 2024); funding; factory count; savings %; service turnaround; procurement delivery area (CA vs all US); accuracy figure (95–99% vector / 80–88% scans, internal); annual pricing; Mac/browser support; export formats and integrations; 23 vs 26 trades; procurement lead time (~90 days)."),
 ("Content rules", "Answer first (40–80 words) under the H1; question H2s; self-contained sections; tables for comparisons; 'Quotr.ai' inside key fact sentences; every number sourced + dated ('as of'); named human author; honest limits; something only Quotr could write (data, customers, people); no year in slugs; change dates only with real changes."),
 ("GEO evidence (1 line)", "GEO is mostly good SEO plus other people talking about you: Google (May 2026) says no special markup or files are needed; C-SEO Bench found most GEO tricks 'largely ineffective'; 82.3% of top-cited SaaS sources are third-party; YouTube mentions are the strongest correlate of AI visibility; llms.txt and AI-specific schema are weak signals."),
 ("AI visibility baseline", "Sept 2026, Perplexity only: Quotr named in 1 of 32 unbranded prompts (~3%); STACK, PlanSwift, Buildxact 10 each; Togal 8. A quotr.ai page was in the source list of 6/32 and cited in the answer of 4/32 (read but not credited). Branded answers repeat stale pricing, Quotr Pro ratings and funding conflicts."),
 ("White space", "Tariffs and landed cost; factory-direct procurement as a category; multifamily/developer precon; outsourced estimating price transparency with Quotr's name; LA rebuild and residential cost questions; a public AI-takeoff accuracy benchmark."),
]
r = 4
for k, v in CTX:
    if v is None: band(wsx, r, k, 3); r += 1; continue
    put(wsx, r, 1, k, font(True, DARK), fill(LIGHT), TOP); put(wsx, r, 2, v, al=WRAP)
    wsx.row_dimensions[r].height = max(30, 15 * (len(v) // 95 + 1)); r += 1
r += 1; band(wsx, r, 'AUTHOR ROSTER (bylines → /authors/ pages, Schema SCH-07)', 3); r += 1
header(wsx, r, ['Author', 'Expertise / assigned clusters', 'Status']); r += 1
for au, exp, st in [("Junzhe Shi, PhD — CTO", "AI takeoff, accuracy, benchmarks, comparisons, trade how-tos (CL05, CL06, CL07, CL13)", "Confirmed (about page); author page to create"),
                    ("Hanyang Liu — CEO", "Procurement, tariffs, cost guides, developers, regional (CL01–CL04, CL11, CL14); design-to-cost founder voice", "Confirmed; pick one LinkedIn (hanyang-liu1)"),
                    ("Tianyi Zong — COO", "Quotr Service operations (CL10)", "Title TO CONFIRM"),
                    ("Jati Ibloguen — Growth", "Changelog / company news", "Title TO CONFIRM")]:
    put(wsx, r, 1, au, font(True)); put(wsx, r, 2, exp, al=WRAP); put(wsx, r, 3, st, al=WRAP); r += 1
r += 1
band(wsx, r, 'PASTE-READY AI BRIEFING (copy cell B below into ChatGPT / Claude / Gemini before any drafting task)', 3); r += 1
brief = ("You are writing for Quotr.ai. Use ONLY the facts below. If a needed fact is missing or marked TO CONFIRM, write [TO CONFIRM: what is needed]. "
         "Do not invent numbers, customers, reviews, awards or press. Date every price ('as of …').\n\n" +
         '\n'.join(f"{k.upper()}: {v}" for k, v in CTX if v) +
         "\n\nOUTPUT RULES: answer-first 40–80 words; question H2s; tables for comparisons; plain practitioner voice; no hype; few em dashes; no self-ranking; cite and date every number.")
put(wsx, r, 1, 'AI briefing', font(True)); put(wsx, r, 2, brief, fl=fill(CALC), al=WRAP)
wsx.row_dimensions[r].height = 409
CTX_BRIEF_CELL = f'B{r}'
widths(wsx, {'A': 26, 'B': 120, 'C': 34})
wsx.freeze_panes = 'A4'

# ================================================================== FORMAT PLAYBOOK
wsf = new_sheet('Format Playbook')
title(wsf, 'FORMAT PLAYBOOK — skeletons, quality bars and schema per article format', 'Each pipeline row has a Format; its outline in Article Briefs follows these skeletons. Templates live in geo-brain/06-playbooks/templates/.', 12)
header(wsf, 4, ['Code', 'Format', 'Template (geo-brain/)', 'When to use', 'Target words', 'H2 skeleton', 'Quality bar (publish blocker)', 'Schema graph', 'Adaptation pattern', 'Common failure', 'Articles planned', 'P1'])
for i, (code, v) in enumerate(FORMATS.items()):
    r = 5 + i
    lab, tpl, words, sch, when, skel, qbar, adapt, fail = v
    for j, val in enumerate([code, lab, tpl, when, words, skel, qbar, sch, adapt, fail]):
        put(wsf, r, j + 1, val, al=WRAP)
    put(wsf, r, 11, f"=COUNTIF({PIPE}$Y$5:$Y$199,B{r})", al=Alignment(horizontal='center', vertical='top'))
    put(wsf, r, 12, f"=COUNTIFS({PIPE}$Y$5:$Y$199,B{r},{PIPE}$AG$5:$AG$199,\"P1\")", al=Alignment(horizontal='center', vertical='top'))
    wsf.row_dimensions[r].height = 120
put(wsf, 5 + len(FORMATS), 10, 'Total', font(True)); put(wsf, 5 + len(FORMATS), 11, f'=SUM(K5:K{4 + len(FORMATS)})', font(True))
widths(wsf, {'A': 7, 'B': 22, 'C': 30, 'D': 30, 'E': 12, 'F': 60, 'G': 40, 'H': 22, 'I': 36, 'J': 26, 'K': 10, 'L': 6})
wsf.freeze_panes = 'C5'

# ================================================================== SCHEMA LIBRARY
wss = new_sheet('Schema Library')
title(wss, 'STRUCTURED DATA LIBRARY — JSON-LD blocks, rules and where each goes', 'Schema is hygiene, not a citation lever (Google, May 2026). Biggest win = one consistent Organization @id. Never put a TO CONFIRM value in schema. Templates: geo-brain/06-playbooks/schema-markup-kit.md', 8)
header(wss, 4, ['ID', 'Block', 'Use on', 'Required properties', 'Never include', 'Status in 2026', 'JSON-LD template (valid JSON; replace [brackets])', 'Validation'])
for i, s in enumerate(SCHEMA):
    r = 5 + i
    compact = json.dumps(json.loads(s['tpl']), ensure_ascii=False, separators=(', ', ': '))
    for j, v in enumerate([s['id'], s['block'], s['use'], s['req'], s['never'], s['status'], compact, s['val']]):
        put(wss, r, j + 1, v, al=WRAP)
    wss.cell(r, 7).font = Font(name='Liberation Mono', size=9)
    wss.row_dimensions[r].height = min(409, 60 + 14 * (len(compact) // 85))
r = 6 + len(SCHEMA)
band(wss, r, 'FORMAT → SCHEMA MAP and DEPLOY STEPS', 8); r += 1
for k, v in FORMATS.items():
    put(wss, r, 1, k); put(wss, r, 2, v[0]); put(wss, r, 3, v[3]); r += 1
r += 1
for step in ["1. Fill templates only with Claim Ledger rows that are In review/Verified; delete any line you cannot confirm.",
             "2. Put Organization + WebSite in the Astro base layout once (SCH-01); remove the second Organization on /disambiguation/.",
             "3. Blog template emits SCH-02 from front matter (title, description, dates, author slug) — Article Briefs col. S shows the expected output per article.",
             "4. Validate in Google Rich Results Test + validator.schema.org before and after deploy; recheck after every template change.",
             "5. dateModified = visible 'Last updated' = sitemap lastmod; never bump dates without content change."]:
    put(wss, r, 1, step); wss.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8); r += 1
widths(wss, {'A': 9, 'B': 30, 'C': 36, 'D': 32, 'E': 34, 'F': 32, 'G': 90, 'H': 30})
wss.freeze_panes = 'C5'

# ================================================================== ADAPTATION KIT
wsa = new_sheet('Adaptation Kit')
title(wsa, 'ADAPTATION KIT — turning one article into platform-native placements', 'Every placement must stand alone (no link-only posts), carry a UTM, and point canonical to quotr.ai. Base/expansion volumes pull live from Channel Registry.', 12)
header(wsa, 4, ['Channel', 'Registry name', 'Role', 'Spec', 'Hook pattern', 'Link policy', 'Canonical / duplicate rule', 'Disclosure', 'Lanes', 'Base / wk', 'Add-on / wk', 'Full / wk'])
for i, ch in enumerate(CHANNELS):
    r = 5 + i
    for j, v in enumerate(ch): put(wsa, r, j + 1, v, al=WRAP)
    for j, col in enumerate(['E', 'F', 'G']):
        put(wsa, r, 10 + j, f"=IFERROR(INDEX('Channel Registry'!${col}$5:${col}$134,MATCH(B{r},'Channel Registry'!$A$5:$A$134,0)),\"—\")", al=Alignment(horizontal='center', vertical='top'))
    wsa.row_dimensions[r].height = 75
r = 6 + len(CHANNELS)
band(wsa, r, 'LANE → CHANNEL MATRIX (● = default adaptation for that lane)', 12); r += 1
allch = []
for v in LANE_CHANNELS.values():
    for c in v:
        if c not in allch: allch.append(c)
header(wsa, r, ['Lane'] + allch); r += 1
for ln, chs in LANE_CHANNELS.items():
    put(wsa, r, 1, ln, font(True))
    for j, c in enumerate(allch): put(wsa, r, 2 + j, '●' if c in chs else '', al=Alignment(horizontal='center'))
    r += 1
r += 1
band(wsa, r, 'UTM CONVENTION', 12); r += 1
for line in ["utm_source = channel (linkedin, x, medium, substack, reddit, quora, youtube, newsletter)", "utm_medium = social | community | email | referral",
             "utm_campaign = the Article ID (e.g. ART-001) so GA4 ties sessions and leads back to the article", "utm_content = variant (company | founder | thread | short) when testing hooks"]:
    put(wsa, r, 1, line); wsa.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8); r += 1
widths(wsa, {'A': 26, 'B': 18, 'C': 24, 'D': 30, 'E': 34, 'F': 28, 'G': 30, 'H': 22, 'I': 26, 'J': 9, 'K': 10, 'L': 9})

# ================================================================== PRODUCTION SOP
wsp = new_sheet('Production SOP')
title(wsp, 'PRODUCTION SOP — how the 3-articles-a-day machine runs', '15 articles in flight at any time (5-day lead). Every article moves Brief → Evidence → Draft → Verify → Approve → Publish → Adapt → Measure. Gates and swap rules prevent publishing placeholders.', 7)
r = 4
band(wsp, r, 'A. ARTICLE TIMELINE (T = publish day)', 7); r += 1
header(wsp, r, ['When', 'Stage', 'What happens', 'Workbook tab', 'Owner', 'Done when']); r += 1
for row in TIMELINE:
    for j, v in enumerate(row): put(wsp, r, j + 1, v, al=WRAP)
    wsp.row_dimensions[r].height = 45; r += 1
r += 1; band(wsp, r, 'B. WEEKLY RHYTHM', 7); r += 1
header(wsp, r, ['When', 'Ritual', 'Output']); r += 1
for row in WEEKLY:
    for j, v in enumerate(row): put(wsp, r, j + 1, v, al=WRAP)
    r += 1
r += 1; band(wsp, r, 'C. ROLES', 7); r += 1
header(wsp, r, ['Role', 'Responsibility', 'RACI']); r += 1
for row in ROLES:
    for j, v in enumerate(row): put(wsp, r, j + 1, v, al=WRAP)
    r += 1
r += 1; band(wsp, r, 'D. PUBLISH QA GATES (all must pass)', 7); r += 1
header(wsp, r, ['#', 'Check', 'Pass?']); r += 1
for i, g in enumerate(QA_GATES, 1):
    put(wsp, r, 1, i); put(wsp, r, 2, g, al=WRAP); put(wsp, r, 3, '', fl=fill(INPUT)); r += 1
r += 1; band(wsp, r, 'E. AI PROMPT CHAIN (paste Context Pack first: ' + "'Context Pack'!" + CTX_BRIEF_CELL + ')', 7); r += 1
header(wsp, r, ['Prompt', 'Text (replace {placeholders} from the Article Pipeline / Briefs row)']); r += 1
for name, txt in AI_PROMPTS:
    put(wsp, r, 1, name, font(True), al=TOP); put(wsp, r, 2, txt, al=WRAP)
    wsp.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
    wsp.row_dimensions[r].height = 15 * (txt.count('\n') + len(txt) // 120 + 2); r += 1
r += 1; band(wsp, r, 'F. CAPACITY MODEL (inputs in Settings B35:B42)', 7); r += 1
CAP = [('Articles per day', '=Settings!B6', '0'), ('Hours per article', '=Settings!B41', '0.00'), ('Production hours per day', f'=B{r}*B{r + 1}', '0.0'),
       ('FTE required', '=Settings!B43', '0.0'), ('Production hours per 4-week cycle', '=Economics!B33', '#,##0'), ('Revenue per production hour', '=Economics!B34', '$#,##0.00'),
       ('Articles in flight (5-day lead × articles/day)', f'=5*B{r}', '0')]
for lab, f_, nf in CAP:
    put(wsp, r, 1, lab); put(wsp, r, 2, f_, fl=fill(CALC), fmt=nf); r += 1
r += 1; band(wsp, r, 'G. SWAP & BLOCK RULES', 7); r += 1
for s_ in SWAP_RULES:
    put(wsp, r, 1, '•'); put(wsp, r, 2, s_, al=WRAP); wsp.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
    wsp.row_dimensions[r].height = 32; r += 1
widths(wsp, {'A': 26, 'B': 40, 'C': 60, 'D': 30, 'E': 22, 'F': 34, 'G': 10})

# ================================================================== REFRESH QUEUE
wsr = new_sheet('Refresh Queue')
title(wsr, 'REFRESH QUEUE — existing URLs AI already reads (6/month, outside the 3 new/day)', 'Fixing pages engines already retrieve is the cheapest way to turn anonymous citations into named ones (optimize-vs-create.md). Only bump dateModified with real changes.', 13)
header(wsr, 4, ['Refresh ID', 'URL', 'Test evidence (Sept 2026)', 'Refresh focus', 'Priority', 'Target prompts', 'Planned week', 'Planned date', 'Status', 'Owner', 'Real dateModified set?', 'Re-test date', 'Roadmap ref'])
for i, (url, ev, focus, pr, tp, wk, ref) in enumerate(REFRESH):
    r = 5 + i
    vals = [f'REF-{i + 1:02d}', url, ev, focus, pr, tp, wk, f'=Settings!$B$4+7*(G{r}-1)+3', 'Not started', 'TKC', '', f'=H{r}+28', ref]
    for j, v in enumerate(vals):
        c = put(wsr, r, j + 1, v, al=WRAP if j in (1, 2, 3) else TOP)
        if j in (7, 11): c.number_format = 'mmm d, yyyy'
        if j in (8, 9, 10): c.fill = fill(INPUT)
    wsr.row_dimensions[r].height = 45
dv_list(wsr, 'I5:I40', ['Not started', 'In progress', 'Done', 'Blocked']); dv_list(wsr, 'K5:K40', ['Yes', 'No'])
widths(wsr, {'A': 9, 'B': 44, 'C': 40, 'D': 46, 'E': 8, 'F': 14, 'G': 9, 'H': 13, 'I': 12, 'J': 8, 'K': 12, 'L': 13, 'M': 9})
wsr.freeze_panes = 'C5'
wsr.conditional_formatting.add('I5:I40', CellIsRule(operator='equal', formula=['"Done"'], fill=fill('C6EFCE')))

# ================================================================== TOPIC CLUSTERS
wst = new_sheet('Topic Clusters')
title(wst, 'TOPIC CLUSTERS & INTERNAL-LINK MAP', 'Each article links to its pillar + product page + 2 siblings (Article Briefs col. L). Pillars marked "proposed" need a URL decision from Quotr.', 11)
header(wst, 4, ['Cluster', 'Name', 'Pillar page', 'Product page', 'Why this cluster', 'CTA', 'Articles planned', 'P1', 'Gated', 'Published', 'Owner'])
for i, (cid_, nm, pil, prod, why, cta) in enumerate(CLUSTERS):
    r = 5 + i
    for j, v in enumerate([cid_, nm, pil, prod, why, cta]): put(wst, r, j + 1, v, al=WRAP)
    put(wst, r, 7, f'=COUNTIF({PIPE}$S$5:$S$199,A{r}&"*")', al=Alignment(horizontal='center', vertical='top'))
    put(wst, r, 8, f'=COUNTIFS({PIPE}$S$5:$S$199,A{r}&"*",{PIPE}$AG$5:$AG$199,"P1")', al=Alignment(horizontal='center', vertical='top'))
    put(wst, r, 9, f'=COUNTIFS({PIPE}$S$5:$S$199,A{r}&"*",{PIPE}$AF$5:$AF$199,"Yes")', al=Alignment(horizontal='center', vertical='top'))
    put(wst, r, 10, f'=COUNTIFS({PIPE}$S$5:$S$199,A{r}&"*",{PIPE}$I$5:$I$199,"Published")', al=Alignment(horizontal='center', vertical='top'))
    put(wst, r, 11, 'TKC')
    wst.row_dimensions[r].height = 45
rt = 5 + len(CLUSTERS)
put(wst, rt, 6, 'Total', font(True))
for c in 'GHIJ': put(wst, rt, ord(c) - 64, f'=SUM({c}5:{c}{rt - 1})', font(True), al=Alignment(horizontal='center'))
widths(wst, {'A': 8, 'B': 30, 'C': 40, 'D': 18, 'E': 50, 'F': 32, 'G': 10, 'H': 6, 'I': 8, 'J': 10, 'K': 8})

# ================================================================== SOURCES additions
ws = wb['Sources']
SRCS = [
 ("GEO brain: entity fact sheet", "geo-brain/00-quotr/entity-fact-sheet.md", "2026-09-25", "Every Quotr fact in Context Pack + Claim Ledger", "Facts marked TO CONFIRM need Quotr sign-off"),
 ("GEO brain: AI context pack", "geo-brain/ai-context-pack.md", "2026-09-25", "Context Pack sheet + AI briefing cell", "Short, verified-only summary"),
 ("GEO brain: monthly tracking set", "geo-brain/04-prompt-library/tracking-set.md", "2026-09-25", "AI Prompt Bank (53 real prompts + Sept baseline)", "Replaces the illustrative v1 prompts"),
 ("GEO brain: content roadmap", "geo-brain/05-content-strategy/content-roadmap.md", "2026-09-25", "Roadmap refs (R-##) and cluster structure in Article Pipeline", "68-item roadmap expanded to 195 slots"),
 ("GEO brain: optimize vs create", "geo-brain/05-content-strategy/optimize-vs-create.md", "2026-09-25", "Refresh Queue + Audit Fixes FIX-24–34", "Fact-fix sweep rows cited"),
 ("GEO brain: white space", "geo-brain/03-market/white-space.md", "2026-09-25", "Lane mix decisions; saturated topics avoided", ""),
 ("GEO brain: schema markup kit", "geo-brain/06-playbooks/schema-markup-kit.md", "2026-09-25", "Schema Library SCH-01–SCH-13", "Dataset/ItemList/NewsArticle/CollectionPage added in v2"),
 ("GEO brain: competitor files", "geo-brain/03-market/competitors/*.md", "2026-09-25", "Competitors sheet notes; competitor claims", "Re-verify prices at publish"),
 ("Section 232 cabinet tariff delay", "https://www.thompsonhinesmartrade.com/2026/01/president-trump-delays-section-232-tariff-increase-on-wood-furniture-cabinets-and-vanities/", "2026-01", "ART-002 tariff claims", "Re-verify before Jan 1, 2027"),
 ("FAQ rich results removed", "https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/", "2026-05-07", "Schema Library status notes", ""),
 ("Content OS v2 article drafts", "content-os/articles/ (ART-001–ART-003)", "2026-11-13", "First three full drafts + JSON-LD + channel adaptations", "Drafts — need editor, claim check and gates"),
]
for i, row in enumerate(SRCS):
    r = 11 + i
    for c in range(1, 10): ws.cell(r, c)._style = copy.copy(ws.cell(10, c)._style)
    for j, v in enumerate(row): ws.cell(r, j + 1).value = v

# ================================================================== READ ME rewrite
ws = wb['Read Me']
for row in ws.iter_rows(min_row=4, max_row=60):
    for c in row: c.value = None
title(ws, 'QUOTR INTELLIGENCE OS — v2 CONTENT MACHINE', 'GEO / AEO / research / 3-articles-per-day operating workbook, now with 195 specified articles, briefs, claims, structured data and adaptations', 10)
RM = [
 ("START HERE", "1) Settings (dates, lane mix, hours) → 2) Context Pack (the only facts allowed) → 3) Article Pipeline (195 specified articles) → 4) Article Briefs (outline, FAQ, claims, links, JSON-LD) → 5) Production SOP (how a day runs) → 6) Placement Log (adaptations) → 7) Weekly Scorecard + Dashboard."),
 ("WHAT'S NEW IN v2", "Every article slot now has a title, buyer query, tracked prompts, persona, format, Quotr-only angle, slug, meta description, schema, author, gate and priority. New tabs: Context Pack, Article Briefs, Format Playbook, Schema Library, Adaptation Kit, Production SOP, Refresh Queue, Topic Clusters. Claim Ledger pre-loaded (" + str(len(CLAIMS)) + " claims). AI Prompt Bank holds the real 53-prompt tracking set with Sept 2026 baselines. Placement Log pre-planned for weeks 1–4."),
 ("FIRST 3 ARTICLES", "ART-001 (AI takeoff pricing compared), ART-002 (cabinet & vanity tariffs before Jan 1, 2027) and ART-003 (three Bay Area factory-direct projects) are fully drafted with JSON-LD and channel adaptations in content-os/articles/. They still need editor review, claim sign-off and their gates (expert review for ART-002; /procurement/ bug fix for ART-003)."),
 ("LANE MIX CHANGE", "4 competitor · 7 industry · 2 regional · 1 research · 1 benchmark per week (was 5 · 5 · 3 · 1 · 1). Reason: 'X alternatives' pages are saturated and 39 regional pages risks doorway content; industry how-tos and procurement/tariff pieces are where Quotr is already cited or where no vendor is cited (white space)."),
 ("GATES", "75 of 195 articles depend on something only Quotr can provide (data, approvals, tests, permissions). The scheduler placed them no earlier than their gate allows; if a gate isn't cleared 5 business days before the slot, swap per Production SOP §G. Never publish with placeholders."),
 ("KEY DEFINITIONS", "Article = verified original long-form piece. Placement = one publication on one destination. Claim = independently supported factual assertion. Gate = a dependency that blocks publication."),
 ("CONTRACT BOUNDARY", "The Nov 12 pilot promised 60+ mixed assets/month for $3,500. Three original articles each business day PLUS expanded distribution is a revised scope. Economics rows 28–38 show the production hours this implies vs the fee — use it to price the amendment."),
 ("WHAT IS NOT REAL-TIME", "No integrations, monitoring jobs, MCP server, autoposting or live search are installed by this spreadsheet. Registries and logs are operating templates; JSON-LD is generated text to paste or template."),
 ("MEASUREMENT RULE", "Only mark claims Verified with evidence URL and named reviewer. Only mark articles Published with a live URL and date. Judge AI visibility on 4-week trends, not single weeks."),
 ("STRUCTURED DATA", "Schema Library holds 13 JSON-LD blocks (Organization, SoftwareApplication, Service, BlogPosting, FAQPage, Dataset, ItemList…). Article Briefs col. S auto-builds each article's BlogPosting + BreadcrumbList from its row. Schema is hygiene, not a citation lever."),
 ("MAIN TABS", "Dashboard → Settings → Context Pack → Production SOP → Daily Capacity → Article Pipeline → Article Briefs → Format Playbook → Schema Library → Adaptation Kit → Channel Registry → Placement Log → Claim Ledger → Weekly Scorecard."),
 ("OPERATIONS", "Refresh Queue → Topic Clusters → Competitors + Change Monitor → AI Prompt Bank + AI Answer Checks → Regional GEO → Benchmark Lab → Earned Media → Audit Fixes → Economics → Sources → MCP Roadmap → System Map."),
 ("SOURCES", "Nov 12 audit and pilot proposal; user-confirmed 3-articles/day; the Quotr GEO brain in this repo (geo-brain/, verified Sept 25, 2026). Re-verify prices and tariffs in the week of publishing."),
]
for i, (k, v) in enumerate(RM):
    r = 4 + i
    put(ws, r, 1, k, font(True, DARK), fill(LIGHT), TOP); put(ws, r, 2, v, al=WRAP)
    ws.row_dimensions[r].height = 48

# ================================================================== SYSTEM MAP rewrite
ws = wb['System Map']
for rng in list(ws.merged_cells.ranges): ws.unmerge_cells(str(rng))
for row in ws.iter_rows(min_row=1, max_row=60):
    for c in row: c.value = None; c._style = copy.copy(ws['K60']._style)
title(ws, 'DATA FLOW & ENTITY RELATIONSHIP MAP (v2)', 'Joined by stable IDs: CLM (claims), ART (articles), PLC (placements), PR/T# (prompts), EVT (competitor changes), REF (refreshes), SCH (schema), CL (clusters).', 9)
header(ws, 4, ['Stage', 'Producer', 'Trigger / cadence', 'Output ID', 'Downstream destination', 'Approval gate', 'Business purpose', 'Dashboard measure', 'Ownership'])
SM = [
 ("00 Context", "Context Pack + fact sheet", "Once; on any fact change", "CTX", "Every brief, draft and schema", "Quotr approver sign-off (FIX-01)", "One source of truth", "Facts to confirm", "Quotr + TKC"),
 ("01 Intake", "Product / sales / research", "Access + daily sync", "SRC", "Claim Ledger", "Rights and completeness", "Approved knowledge", "Claims in review", "Quotr + TKC"),
 ("02 Monitor", "Competitor sites & sitemaps", "Hourly target; changes verified", "EVT", "Change Monitor + Claim Ledger", "Original URL / snapshot", "Market awareness", "Verified changes", "TKC"),
 ("03 Validate", "Editors / Quotr approver", "Each proposed factual claim", "CLM", "Article Briefs + Benchmark Lab", "Reviewer + evidence + date", "Fact integrity", "New verified claims/week", "TKC + Quotr"),
 ("04 Detect demand", "AI Prompt Bank (53 real prompts)", "Weekly core / monthly brand", "PR / T#", "AI Answer Checks → Article Pipeline col. U", "Clean-session protocol", "Unbranded discovery opportunities", "Named share; prompts with no article", "TKC"),
 ("05 Specify", "Article Pipeline", "13-week plan; weekly re-plan", "ART", "Article Briefs", "Gate column AE cleared", "Create only useful, Quotr-only assets", "Ungated / gated counts", "TKC"),
 ("06 Brief", "Article Briefs + Format Playbook", "T-5 days", "BRIEF", "Writers / AI prompt P1–P2", "Brief status = Ready", "Consistent structure", "Briefs Ready", "TKC"),
 ("07 Produce", "Content factory (3/day)", "T-3 to T-1", "ART", "quotr.ai /blog, /research, /benchmarks", "Claim pass, expert/legal review, editorial approval (15 QA gates)", "Search + AI-answer content", "Published articles", "TKC"),
 ("08 Structure", "Schema Library + Briefs col. S", "At every publish", "SCH", "CMS template JSON-LD", "Validator pass; matches visible page", "Machine-readable entities", "Schema validated", "Developer + TKC"),
 ("09 Link", "Topic Clusters", "At every publish", "CL / URL", "Pillar + product + 2 siblings", "No orphans (≥3 links in)", "Knowledge discovery", "Orphan count", "TKC + developer"),
 ("10 Adapt + distribute", "Adaptation Kit → Placement Log", "T0 to T+3", "PLC", "LinkedIn, X, Medium, Substack, communities", "Account/brand/platform rules; disclosure", "Reach + third-party mentions", "Placements/week", "TKC + Quotr"),
 ("11 Earn citations", "Publisher outreach", "Per data asset; 10/month base", "PITCH", "Editorial publications / list editors", "Human editor acceptance", "Independent authority", "Earned references", "TKC"),
 ("12 Publish research", "Benchmark Lab", "When testing is complete", "BENCH", "quotr.ai/benchmarks, GitHub, Hugging Face", "Reproducible, permitted, disclosed", "Citable open evidence", "Released benchmarks", "Quotr + TKC"),
 ("13 Refresh", "Refresh Queue", "6/month", "REF", "Existing URLs AI already reads", "Real changes only", "Turn anonymous citations into named ones", "Refreshes done", "TKC"),
 ("14 Attribute", "Web analytics + CRM (UTM = ART ID)", "Daily ingestion / weekly review", "LEAD", "Weekly Scorecard", "Qualified lead definition", "Revenue attribution", "Qualified inbound leads", "Quotr + TKC"),
 ("15 Optimize", "Weekly scorecard + T+28 re-checks", "Weekly / monthly", "DEC", "Next week's slots, swaps, refreshes", "Compare outcomes with cost", "Reallocate production", "Lead and visibility trend", "TKC + Quotr"),
]
for i, row in enumerate(SM):
    for j, v in enumerate(row): put(ws, 5 + i, j + 1, v, al=WRAP)
    ws.row_dimensions[5 + i].height = 32
r = 6 + len(SM)
band(ws, r, 'FLOW: CONTEXT → CLAIMS → PROMPT DEMAND → SPEC → BRIEF → 3 ARTICLES/DAY → SCHEMA + LINKS → ADAPT → MEASURE (T+28) → REFRESH / REPRIORITIZE', 9)
r += 2
header(ws, r, ['Link type', 'Primary key', 'Foreign key', 'Where stored', 'Validation']); r += 1
for row in [("Claim → Article", "CLM-###", "ART-###", "Article Pipeline!M / Claim Ledger!M (count)", "Only In review/Verified claims may be presented as factual"),
            ("Article → Brief → Schema", "ART-###", "Brief row + JSON-LD", "Article Briefs!A / S", "JSON-LD must match the visible page"),
            ("Article → Placement", "ART-###", "PLC-###", "Placement Log!D (UTM campaign = ART ID)", "External posts inherit canonical/source reference"),
            ("Prompt → Article", "T## / PR-##", "ART-###", "Article Pipeline!U ↔ AI Prompt Bank!J/L", "One page per real question, not per wording"),
            ("Competitor → Claim", "EVT-###", "CLM-###", "Change Monitor → Claim Ledger", "Page changed ≠ fact verified"),
            ("Cluster → Article", "CL##", "ART-###", "Topic Clusters ↔ Article Pipeline!S", "Every article links to its pillar"),
            ("Research → MCP", "BENCH/source ID", "MCP tool response", "Benchmark Lab → MCP Roadmap", "Only public approved version exposed")]:
    for j, v in enumerate(row): put(ws, r, j + 1, v, al=WRAP)
    r += 1
widths(ws, {'A': 20, 'B': 30, 'C': 26, 'D': 12, 'E': 38, 'F': 36, 'G': 32, 'H': 28, 'I': 16})

# ================================================================== sheet order
ORDER = ['Settings', 'Read Me', 'Dashboard', 'Context Pack', 'Production SOP', 'Weekly Scorecard', 'Daily Capacity', 'Article Pipeline', 'Article Briefs',
         'Format Playbook', 'Schema Library', 'Adaptation Kit', 'Refresh Queue', 'Topic Clusters', 'Channel Registry', 'Placement Log', 'Claim Ledger',
         'Competitors', 'Change Monitor', 'AI Prompt Bank', 'AI Answer Checks', 'Regional GEO', 'Benchmark Lab', 'Earned Media', 'Audit Fixes',
         'Economics', 'Sources', 'MCP Roadmap', 'System Map']
assert sorted(ORDER) == sorted(wb.sheetnames), set(wb.sheetnames) ^ set(ORDER)
wb._sheets = [wb[n] for n in ORDER]
wb.active = ORDER.index('Dashboard')
for w in wb.worksheets: w.sheet_view.tabSelected = (w.title == 'Dashboard')
for n_, col in [('Context Pack', '087E8B'), ('Production SOP', '087E8B'), ('Article Pipeline', '13243A'), ('Article Briefs', '13243A'),
                ('Format Playbook', '087E8B'), ('Schema Library', '087E8B'), ('Adaptation Kit', '087E8B'), ('Refresh Queue', '087E8B'), ('Topic Clusters', '087E8B')]:
    wb[n_].sheet_properties.tabColor = col

wb.save(OUT)
json.dump([{k: (str(v) if isinstance(v, dt.date) else v) for k, v in a.items() if k not in ('ent',)} for a in ARTS],
          open(os.path.join(HERE, 'arts_schedule.json'), 'w'), indent=1)
print('saved', OUT, 'placements', N_PL, 'claims', len(CLAIMS))
