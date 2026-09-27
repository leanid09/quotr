---
type: hub
description: The master list of 282 buyer prompts by funnel stage, persona and trade, each matched to a Quotr page.
last_verified: 2026-09-25
verify_every_days: 90
cssclasses:
- wide
---
# Quotr GEO Prompt Library

> [!abstract] What this page is for
> The master list of questions ("prompts") that Quotr's buyers type into ChatGPT, Google (AI Overviews and AI Mode), Perplexity, Gemini, Claude and Copilot. Each prompt is sorted by funnel stage, persona and trade, tagged with its intent and a priority for Quotr, and matched to the Quotr page that should answer it. Use it to plan content and to choose prompts for monthly AI-visibility tracking.

> [!info]- Sources
> - Research notes: [[quotr_ai_visibility_tests]] (40 tested prompts and results), [[competitor_geo_benchmark]] (extra tested prompts, white space), [[geo_content_playbook_b2b]] (§6 how construction buyers use AI), [[quotr_onsite_content_audit]] (Quotr URL inventory), [[quotr_offsite_presence]] (prompts O1–O6), [[verification_quotr_and_competitors]] and [[verification_geo_evidence]] (corrections, which override the other notes).
> - New research on 2026-09-25 (WebSearch and Perplexity Sonar): questions from ContractorTalk, Electrician Talk, PlumbingZone, HVAC-Talk, PaintTalk, Reddit (r/estimators, r/Construction, r/Flooring, r/HVAC, r/electricians, r/plumbers), YouTube video titles and "People also ask"-style search results. Every source link is listed trade by trade in [[Buyer questions by trade]].
> - Quotr page URLs come from the blog sitemap, main sitemap and dictionary pages as recorded in the notes, plus a WebSearch of quotr.ai/dictionary (2026-09-25). All Quotr links point to https://quotr.ai.

---

## How to use this page

### The three funnel stages

| Stage | What the buyer is doing | Example | What Quotr wants |
|---|---|---|---|
| **1. Learn / problem** (top of funnel) | Trying to understand or solve a problem. Often no software in mind yet. | "how to estimate drywall for a house" | A quotr.ai page is **cited** as a source, and the brand is named where it helps |
| **2. Compare / evaluate** (middle) | Looking for tools, services or suppliers and comparing them. | "Togal.AI alternatives" | Quotr is **named** in the shortlist, ideally in the top 5 |
| **3. Decide / brand** (bottom) | Checking Quotr itself: price, trust, fit, "Quotr vs X". | "Quotr.ai pricing" | The answer about Quotr is **accurate, current and favourable** |

### Column guide

- **#**: a stable ID. L = Learn, E = Evaluate/compare, D = Decide/brand. Do not renumber. Add new prompts at the end of a section with the next free number.
- **Prompt**: written the way people really type (short, informal, often with a year or trade). Prompts that were tested in September 2026 are copied **word for word** from the test, so they can be re-run exactly.
- **Persona** (who asks). Codes match [[Audiences and personas]]:

| Code | Persona |
|---|---|
| SUB | Trade subcontractor owner or estimator |
| GC | General contractor / preconstruction manager |
| RES | Residential builder, small GC or remodeler |
| DEV | Real estate developer (single-family, multifamily, ADU, rebuild) |
| FUND | Development fund, underwriter or lender's analyst |
| BUY | Materials buyer (procurement lead, owner-builder, finish supplier) |
| ARCH | Architect / design team |
| SVC | Anyone looking to outsource estimating (estimating-service buyer) |
| ALL | Any of the above |

- **Trade**: GEN (general / all trades), DRY (drywall), FRM (framing and lumber), FLR (flooring), TILE, PNT (painting), CONC (concrete), ROOF (roofing), SID (siding), WIN (windows and doors), CAB (cabinets and countertops), ELEC (electrical), PLMB (plumbing), HVAC, INS (insulation), SRC (material costs, sourcing, tariffs, importing).
- **Intent**:

| Code | Meaning |
|---|---|
| Learn | How to do something |
| Define | What a term means |
| Cost | Price, rate or cost benchmark |
| Tool | Find software or a category of tools |
| Alt | Alternatives to a named product |
| VS | Head-to-head comparison |
| Service | Hire someone to do it |
| Buy | Buy materials or find suppliers |
| Brand | Facts about Quotr |
| Price | Quotr pricing |
| Trust | Reviews, legitimacy, accuracy, security |
| Fit | Does Quotr do X / work for me |

- **Pri** (priority for Quotr):
  - **High** = close to what Quotr sells and where AI answers are open (factory-direct procurement, tariffs and landed cost, developer estimates and service pricing, residential takeoff-to-procurement, AI takeoff accuracy), or a brand prompt where AI tools get Quotr wrong today.
  - **Med** = relevant and winnable, but crowded (for example, trade how-tos where free calculators win).
  - **Low** = relevant to buyers but far from Quotr's product, or a simple definition that AI can answer without clicking.
- **Quotr page that should answer it**:
  - A link = the best existing page. "(optimize)" means the page exists but needs work first (for example, stale pricing or thin copy). See [[Page refresh checklist]].
  - **NEW PAGE NEEDED** = no suitable page exists. A short suggestion follows.
  - **Off-site** = the answer mostly comes from other websites (G2, Capterra, listicles, Reddit). An on-site page alone will not win it. See [[Citation sources map]].
  - **TO CONFIRM with Quotr** = the page cannot be written until Quotr confirms a fact.
- **Tested / seen**: either the September 2026 test result, or a link to where the real question was seen.
  - Test IDs (C, V, P, B, S, O) match [[AI visibility baseline]]. **N1–N6** are six extra prompts run once for this library (same tool, same day) to give the new tracking prompts a baseline. All tests used **Perplexity Sonar only** on 2026-09-25.
  - Result words: **Absent** = Quotr not named and not cited. **Cited, not named** = a quotr.ai page was a source but the answer did not say "Quotr". **Retrieved only** = a quotr.ai page was in the source list but not used. **Named** = Quotr appeared in the answer text.
  - "Seen:" links = the forum thread, Reddit thread, YouTube video or search result where the question appeared (research on 2026-09-25).

### Three rules before you write anything

1. **Do not build one page per prompt.** Many prompts here share one answer page. Google's May 2026 AI-search guide warns that pages made mainly for every variation of a query can count as scaled content abuse ([[verification_geo_evidence]], claim 2). Group prompts into strong pages.
2. **Category prompts ("best X software") are won mostly off-site.** Perplexity recommended brands that appear on independent listicles and G2/Capterra "alternatives" pages. It used Quotr's own "best of" posts as fact sources but did not recommend Quotr from them ([[quotr_ai_visibility_tests]], §2 and §5). Also, the SEO analyst Lily Ray observed that sites ranking themselves #1 in "best X" lists lost Google visibility in early 2026; Google has not confirmed a targeted update (verification_geo_evidence.md, claim 19). Use honest comparison pages, and put most effort into third-party listings.
3. **Keep tested prompts word for word.** Even small wording changes change the answer. Prompts that echo Quotr's own copy can make Quotr look more visible than it is (test S6: Quotr was named only because the prompt used Quotr's own words; buyer-style versions C10 and C14 did not surface Quotr).

---

## Summary

| Stage | Prompts | High | Med | Low | Tested in Sept 2026 | Existing page fits | Page exists but needs work "(optimize)" | NEW PAGE NEEDED |
|---|---|---|---|---|---|---|---|---|
| 1. Learn / problem | 146 | 51 | 57 | 38 | 15 | 57 | 27 | 62 |
| 2. Compare / evaluate | 88 | 41 | 36 | 11 | 36 | 37 | 30 | 21 |
| 3. Decide / brand | 48 | 30 | 15 | 3 | 13 | 33 | 7 | 8 |
| **Total** | **282** | **122** | **108** | **52** | **64** | **127** | **64** | **91** |

Notes on the numbers:
- "Existing page fits" counts rows that link a page with no "(optimize)" flag. It includes rows marked "Off-site" or "TO CONFIRM" where no new page is proposed.
- "Tested" = the prompt was run word for word on Perplexity Sonar on 2026-09-25: 40 baseline prompts (C/V/P/B), 12 supplementary S prompts and 6 off-site O prompts (58, results in [[AI visibility baseline]]), plus 6 new N prompts run once for this library (64 in total).
- Of the 64 tested prompts, Quotr was **named in 14**: 12 brand prompts that already contain the word "Quotr" (B1–B7, V2, S7, O1–O3), V1 ("Togal.AI alternatives", near the bottom of the list) and S6 (a prompt that echoes Quotr's own wording). On ordinary buyer prompts it is almost invisible. No other engine (ChatGPT, Google AI Mode/AI Overviews, Gemini, Claude, Copilot) has been tested yet.

Prompts per persona (a prompt can have more than one persona):

| Persona | Prompts tagged |
|---|---|
| SUB (trade sub / estimator) | 153 |
| GC (precon) | 52 |
| RES (builder / remodeler) | 74 |
| DEV (developer) | 57 |
| FUND (lender / fund) | 7 |
| BUY (materials buyer) | 34 |
| ARCH (architect) | 5 |
| SVC (outsourcing buyer) | 14 |
| ALL (any persona) | 27 |

Trade coverage: every one of the 14 trades has at least 4 prompts; see [[#Views by trade|Views by trade]].

---

> [!tip] These tables are live
> Every prompt is now its own note in the `prompts` folder. The tables below read those notes, so they are always current. Click an ID to open a prompt with its test history and the content planned for it. Use **Sort**, **Filter** and **Search** above each table. The full library in one table: [[Prompts.base|All prompts]].

## Stage 1 — Learn / problem (top of funnel)

At this stage AI answers usually cite sources but rarely name software brands. In September 2026, Quotr was **named in 0 of 8** tested how-to prompts and **cited in 1** (P5, accuracy of AI takeoff). Free calculators, cost-guide sites, Bluebeam/Autodesk/Procore guides, estimating-service firms and logistics firms won most citations ([[quotr_ai_visibility_tests]], §3). An extra test run for this library on the same day (N2, "how to estimate plumbing from drawings") showed the same pattern: Quotr's plumbing post was the **first citation** and supplied most of the steps, but the answer never said "Quotr". Specific, step-by-step trade how-tos get used; the brand name still has to be written into the key sentences.

### 1.1 General estimating and bidding

![[Prompts.base#1.1 General estimating and bidding]]

### 1.2 Takeoff and AI

![[Prompts.base#1.2 Takeoff and AI]]

### 1.3 Trade questions

Real questions behind these prompts, with links, are in [[Buyer questions by trade]].

![[Prompts.base#1.3 Trade questions]]

### 1.4 Material costs, sourcing, tariffs and importing

This is Quotr's clearest white space. In September 2026, tariff and importing answers cited only government, media and logistics sources, and **no software vendor at all** ([[competitor_geo_benchmark]], §3 and §5).

![[Prompts.base#1.4 Material costs, sourcing, tariffs and importing]]

### 1.5 Developer, preconstruction and residential cost questions

![[Prompts.base#1.5 Developer, preconstruction and residential cost questions]]

---
## Stage 2 — Compare / evaluate (middle of funnel)

This is where Quotr loses most today. In September 2026, Quotr was **named in 0 of 15** category prompts and **1 of 9** unbranded comparison prompts (only "Togal.AI alternatives", near the bottom). Perplexity built these answers from independent listicles (constructioncoverage.com, thedigitalprojectmanager.com, ConstructConnect, ContraVault), G2/Capterra/SourceForge "alternatives" pages and competitors' own listicles. Quotr's own comparison posts were used as fact sources but did not get Quotr recommended ([[quotr_ai_visibility_tests]], §1, §2, §5). Seer found "X vs Y" searches show a Google AI Overview 95.4% of the time ([[verification_geo_evidence]], claim 21), so comparison pages are almost always read by AI.

### 2.1 Category prompts (all trades and personas)

![[Prompts.base#2.1 Category prompts (all trades and personas)]]

### 2.2 Category prompts by trade

![[Prompts.base#2.2 Category prompts by trade]]

### 2.3 Alternatives prompts

![[Prompts.base#2.3 Alternatives prompts]]

### 2.4 Head-to-head prompts (competitors only)

![[Prompts.base#2.4 Head-to-head prompts (competitors only)]]

### 2.5 Feature and fit prompts (unbranded)

![[Prompts.base#2.5 Feature and fit prompts (unbranded)]]

### 2.6 Services and procurement comparisons

![[Prompts.base#2.6 Services and procurement comparisons]]

---

## Stage 3 — Decide / brand (bottom of funnel)

Brand answers are mostly built from Quotr's own pages (about 60–70% self-sourced), so engines hedge ("not independently validated"). **5 of 8** brand prompts had accuracy problems in September 2026: the unrelated Quotr Pro app's ratings used as Quotr's, stale "from $299.90" pricing (the real entry price is Lite at $79.90 per seat per month), namesake apps, and a funding conflict ([[quotr_ai_visibility_tests]], §4; [[verification_quotr_and_competitors]]). Canonical facts: [[Entity fact sheet]].

### 3.1 Brand facts

![[Prompts.base#3.1 Brand facts]]

### 3.2 Pricing

![[Prompts.base#3.2 Pricing]]

### 3.3 Trust, reviews and accuracy

![[Prompts.base#3.3 Trust, reviews and accuracy]]

### 3.4 Quotr vs a named competitor

![[Prompts.base#3.4 Quotr vs a named competitor]]

### 3.5 Product fit and how to use it

![[Prompts.base#3.5 Product fit and how to use it]]

### 3.6 Quotr Procurement and Quotr Service specifics

![[Prompts.base#3.6 Quotr Procurement and Quotr Service specifics]]

---

## Views by persona

Prompt IDs grouped by who asks. Use these when writing for one persona. A prompt can appear under more than one persona. "ALL" prompts apply to everyone.

| Persona | Learn | Compare | Decide |
|---|---|---|---|
| SUB (trade sub / estimator) | L-001–L-007, L-009, L-011–L-013, L-017, L-018, L-020, L-021, L-024–L-028, L-031, L-032, L-035, L-037, L-039–L-042, L-044, L-046, L-047, L-049–L-054, L-057–L-059, L-062–L-064, L-066–L-081, L-085, L-086, L-089, L-091, L-092, L-094–L-099, L-102–L-105, L-107, L-123, L-127, L-146 | E-001, E-009, E-010, E-014, E-017–E-020, E-025–E-050, E-053–E-059, E-061–E-065, E-067–E-072, E-074 | D-009–D-011, D-013, D-019, D-021, D-022, D-024–D-028, D-031–D-040 |
| GC (precon) | L-002, L-006, L-007, L-009–L-011, L-014–L-022, L-024, L-029, L-035, L-040, L-042–L-044, L-123–L-127, L-140, L-146 | E-004, E-012, E-013, E-016, E-021, E-025, E-043, E-046, E-066, E-069, E-071, E-076, E-079, E-080 | D-009, D-013, D-019, D-021, D-022, D-026, D-032, D-037, D-040 |
| RES (builder / remodeler) | L-001, L-004, L-005, L-014, L-015, L-020, L-027, L-029, L-031, L-037, L-046–L-048, L-050, L-052, L-054–L-057, L-060, L-062, L-067, L-069, L-075, L-078, L-081, L-083, L-086–L-089, L-093, L-098–L-100, L-104, L-106, L-108, L-109, L-113, L-114, L-120, L-132–L-134, L-139, L-145 | E-002, E-008, E-010–E-012, E-014, E-018, E-032, E-047, E-051–E-054, E-056, E-059, E-060, E-063, E-065, E-066, E-072, E-082, E-083, E-085 | D-029, D-030, D-033, D-043 |
| DEV (developer) | L-006, L-022, L-029, L-056, L-060, L-061, L-065, L-081–L-084, L-087, L-088, L-090, L-093, L-108–L-110, L-112–L-114, L-118, L-120, L-121, L-124, L-125, L-128–L-140, L-142 | E-005, E-011, E-022, E-023, E-066, E-073, E-083, E-084, E-087, E-088 | D-012, D-042–D-044, D-046–D-048 |
| FUND (lender / fund) | L-130, L-135, L-137, L-141, L-142 | E-023, E-086 | — |
| BUY (materials buyer) | L-061, L-065, L-082, L-084, L-087, L-090, L-101, L-108–L-112, L-114–L-119, L-121, L-122, L-127, L-128 | E-013, E-015, E-067, E-081, E-082, E-084, E-085 | D-042–D-045, D-048 |
| ARCH (architect) | L-140, L-143, L-144 | E-024 | D-036 |
| SVC (outsourcing buyer) | L-018, L-019 | E-073–E-080, E-088 | D-012, D-046, D-047 |
| ALL (any persona) | L-008, L-023, L-030, L-033, L-034, L-036, L-038, L-045 | E-003, E-006, E-007 | D-001–D-008, D-014–D-018, D-020, D-023, D-041 |

## Views by trade

A prompt tagged with several trades is counted under each.

| Trade | Prompt IDs | Count |
|---|---|---|
| Drywall (DRY) | L-047–L-051, E-026 | 6 |
| Framing and lumber (FRM) | L-052–L-056, E-032 | 6 |
| Flooring (FLR) | L-057–L-061, E-027 | 6 |
| Tile (TILE) | L-062–L-065, E-035 | 5 |
| Painting (PNT) | L-066–L-068, E-034 | 4 |
| Concrete (CONC) | L-069–L-072, E-031, E-041 | 6 |
| Roofing (ROOF) | L-073–L-076, E-033 | 5 |
| Siding (SID) | L-077–L-079, E-036 | 4 |
| Windows and doors (WIN) | L-080–L-084, E-037 | 6 |
| Cabinets and countertops (CAB) | L-085–L-090, L-114, E-038 | 8 |
| Electrical (ELEC) | L-091–L-096, E-028, E-042, E-076, E-078, D-034 | 11 |
| Plumbing (PLMB) | L-097–L-101, E-029, E-042, E-076 | 8 |
| HVAC | L-102–L-104, E-030, E-042, E-076, E-077, D-034 | 8 |
| Insulation (INS) | L-105–L-107, E-039 | 4 |
| Sourcing, tariffs, importing (SRC) | L-020, L-021, L-029, L-108–L-113, L-115–L-128, E-006, E-013, E-015, E-066, E-067, E-081–E-085, D-042–D-045, D-048 | 38 |
| General / all trades (GEN) | All other prompts | 162 |

---

## New pages this library calls for (roll-up)

Many "NEW PAGE NEEDED" rows point to the same page. Grouped, the library calls for about 25 new assets. The order below follows the white-space evidence ([[competitor_geo_benchmark]], §5); final priorities belong in [[Content priorities]].

| New asset | Prompts it answers | Why |
|---|---|---|
| Landed-cost and tariff hub for residential finish materials (cabinet/vanity tariff explainer, landed-cost calculator, lead-time tracker, certification FAQ, honest "is importing worth it") | L-065, L-082, L-083, L-087, L-090, L-101, L-109, L-112, L-114–L-121, E-084, E-085 | No software vendor is cited on these questions today; fits Quotr Procurement |
| Residential builders hub + residential GC page (plans → takeoff → proposal → materials) | E-002, E-008, E-010, E-014, E-063, E-051, E-059 | Handoff and Buildxact own residential answers; Quotr is absent from all of them |
| Developer hub + multifamily cost benchmark + ADU/LA rebuild/California $/sq ft pages | L-129–L-134, L-136, L-137, L-139, L-142, E-005, E-011 | Meltplan/Exayard cost pages get cited next to RSMeans; Quotr has service data but no benchmark |
| Bid-leveling guide + free template + bid/supplier-quote comparison page | L-014, L-015, E-012, E-067 | Answers name Buildertrend/Buildxact/SmartBid with thin content |
| Estimating time benchmark (by project size, from Quotr Service jobs) + AI takeoff accuracy method page | L-006, L-007, L-040, L-046, D-019 | Original data is the most citable format; accuracy was contractors' top AI worry in one survey (Dodge/CMiC; not re-checked) |
| Free trade calculators (drywall, flooring waste, tile, concrete, framing) | L-047, L-048, L-055, L-057, L-062, L-069 | Calculators won the drywall how-to (P2) for three software vendors |
| Residential trade-cost benchmarks (electrical, plumbing, HVAC, insulation per sq ft / per fixture / per ton) | L-093, L-098, L-100, L-104, L-106 | Answers today come from HomeGuide, Angi, Fixr-type sites |
| Trade guides where Quotr has no content: roofing from plans, siding, framing/lumber, drywall pricing, concrete pricing | L-049, L-050, L-052, L-054, L-070, L-074, L-077, E-032, E-033 | Roofing has only a thin trade page; siding has none |
| Browser/Mac page | E-009, E-017 | Quotr is browser-based but absent from Mac prompts |
| Honest comparison pages: Quotr alternatives; Quotr vs Handoff, Buildxact, Kreo; four-way AI takeoff table; On-Screen Takeoff, Kreo, Handoff, Buildxact alternatives | D-023, D-024, D-029–D-031, E-048, E-049, E-051, E-052, E-057, E-060 | Missing head-to-heads with named rivals (onsite audit §6) |
| Customer reviews hub, security page, integrations page | D-014, D-037, E-071 | Trust prompts fail today; facts TO CONFIRM with Quotr |
| Estimating basics: Estimating 101 hub, plan-reading guide, overhead and profit guide, RFQ how-to, value engineering, lender budget review, hard vs soft costs | L-002, L-003, L-027, L-127, L-135, L-140, L-141 | Lower priority; mostly definitional |

---

## Related pages

- [[Tracking set]] — the 53 prompts to re-run every month, with baselines and instructions
- [[Buyer questions by trade]] — the real questions behind these prompts, with source links
- [[Construction glossary]] — plain-English definitions of the terms used in these prompts
- [[AI visibility baseline]] — full September 2026 test results
- [[Audiences and personas]] — persona profiles
- [[White space]] — where Quotr can win
- [[Content priorities]] — what to build first
- [[Page refresh checklist]] — how to fix the "(optimize)" pages
