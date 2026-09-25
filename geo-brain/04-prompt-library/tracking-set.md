# Monthly AI-Visibility Tracking Set

**What this page is for:** The fixed set of 53 prompts to re-run every month to see whether AI answer engines mention, cite and describe Quotr.ai correctly, with the September 2026 baseline for each prompt and step-by-step instructions (engines, number of runs, what to record, copy-paste templates).

**Last updated:** 2026-09-25

**Sources:** <../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md> (40 baseline prompts, 45 runs, method), <../../research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md> (independent re-runs; overrides the other notes), <../../research_notes/Quotr GEO AEO strategy audit/competitor_geo_benchmark.md> (S prompts), <../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md> (§4 measurement), <../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md> (measurement corrections and 2026 developments: claims 3, 6, 7, 8, 21; M1, M2, M8); six new baseline runs (N1–N6) made for this page on 2026-09-25 with Perplexity Sonar (`mcp__Slashy__web_search`). Prompt IDs link to [prompt-library.md](prompt-library.md) and [../02-current-state/ai-visibility-baseline.md](../02-current-state/ai-visibility-baseline.md).

---

## 1. At a glance

- **53 prompts.** The **core 40** are the September 2026 baseline prompts, kept word for word so every month compares like for like. The **extension 13** fill gaps in the core: 7 supplementary prompts already tested once in September (S4, S5, S6, S9, S10, S11, S12) and 6 new prompts (N1–N6) that were given a baseline run on 2026-09-25.
- **Two tiers.** **Tier A** (22 prompts) are the headline prompts: run them twice on every engine. **Tier B** (31 prompts): run once per engine.
- **Baseline is Perplexity only.** September 2026 results come from Perplexity Sonar. ChatGPT, Google AI Mode / AI Overviews, Gemini, Claude and Copilot have **no baseline yet**; October 2026 will be their first month.

### Balance of the set

| Dimension | Split |
|---|---|
| Funnel stage | Learn / problem: 15 · Compare / evaluate: 29 (category 17, comparison/alternatives 12) · Decide / brand: 9 |
| Branded vs unbranded | 9 prompts name Quotr (B1–B7, V2, S7 is not in the set) · 44 unbranded |
| Personas (a prompt can have several) | SUB 26 · RES 13 · DEV 10 · GC 7 · BUY 10 · SVC 3 · ALL 12 |
| Trades | Drywall (T04, T26), flooring (T05), electrical (T06), plumbing (T49), HVAC (T50), roofing (T51), framing/lumber (T53), cabinets/windows/flooring sourcing (T14, T48), general (the rest). Painting, concrete, siding, tile and insulation are covered in the full [prompt-library.md](prompt-library.md) but are not tracked monthly because they are low priority for Quotr. |
| Quotr product | Software 30 · Service 3 (T12, T44, T27 partly) · Procurement / sourcing 10 (T09, T10, T14, T28, T32, T42, T43, T46, T48, plus T41 for supplier bids) · Brand 9 |

### September 2026 baseline in one table (Perplexity Sonar, first runs)

| Metric | Baseline |
|---|---|
| Unbranded prompts where Quotr is **named** | Core: 1 of 32 (3.1%). Extension: 1 of 13 (S6, a prompt that echoes Quotr's own wording) |
| Unbranded prompts where a quotr.ai page is **cited** in the answer | Core: 4 of 32 (12.5%). Extension: 2 more (S9, N2) |
| Unbranded prompts where a quotr.ai page is in the **source list** | Core: 6 of 32 (18.8%) |
| Quotr **share of voice**, unbranded core prompts | About 0.7% (STACK, PlanSwift, Buildxact about 6.5% each) |
| Brand prompts with an **accuracy problem** | 5 of 8 (B3 Quotr Pro conflation, B4 and V2 stale price, B5 namesakes, B6 funding conflict) |

Source: <../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>, §5, and N1–N6 runs on 2026-09-25.

---

## 2. The 53 prompts and their baselines

Copy the prompt text **exactly**, including capital letters and punctuation. Do not add context such as "I am a contractor". "Named in answer" lists the brands the engine recommended instead of Quotr, in the order it named them.

Result words: **Absent** = not named, not cited · **Cited, not named** = a quotr.ai page was a source but the answer did not say "Quotr" · **Retrieved only** = a quotr.ai page was in the source list but unused · **Named** = Quotr is in the answer text.

### 2a. Core 40 (September 2026 baseline prompts)

| T# | Test ID | Library ID | Prompt (verbatim) | Stage | Persona | Tier | Sept 2026 baseline (Perplexity) | Named in answer / watch for |
|---|---|---|---|---|---|---|---|---|
| T01 | C1 | E-001 | best AI takeoff software for subcontractors 2026 | Compare | SUB | A | Absent (2 runs + independent re-run) | Togal.AI, STACK, PlanSwift, Beam AI. Sources: ConstructConnect, ContraVault, constructioncoverage, TDPM, SourceForge, F6S category |
| T02 | C2 | E-002 | best construction estimating software for residential contractors | Compare | RES | A | Absent | Clear Estimates, Buildxact, Houzz Pro, Buildertrend, JobTread, QuickBooks |
| T03 | C3 | E-003 | AI construction takeoff software | Compare | ALL | B | Absent | Ruh AI, Beam AI, eTakeoff, Bobyard, Kreo, MeltPlan, Togal, Civils.ai, CountBricks, Procore |
| T04 | C4 | E-026 | best takeoff software for drywall contractors | Compare | SUB | A | Absent | STACK, The EDGE, QuoteIQ, Bluebeam, Houzz Pro, Buildxact, PlanSwift |
| T05 | C5 | E-027 | best takeoff software for flooring contractors | Compare | SUB | B | Absent | The EDGE, MeasureSquare, PlanSwift, STACK, Autodesk Takeoff, QuoteIQ |
| T06 | C6 | E-028 | best takeoff software for electrical contractors | Compare | SUB | B | Absent (Quotr's electrical post not retrieved) | ConEst IntelliBid, Countfire, PlanSwift, Trimble AccuBid, McCormick |
| T07 | C7 | E-004 | construction bid management software for general contractors | Compare | GC | B | Absent | ConstructConnect, BuildingConnected, SmartBid, PlanHub, Procore, Kahua, Dodge |
| T08 | C8 | E-005 | software for multifamily developers to estimate construction costs | Compare | DEV | A | Absent | ConstructionOnline, RSMeans, Autodesk Forma Estimate, Procore, STACK, RIB CostX, Trimble |
| T09 | C9 | E-006 | construction estimating software with material procurement | Compare | ALL, BUY | A | Absent (reproduced) | Buildertrend, Procore, Buildxact, esti-mate, ConWize |
| T10 | C10 | E-081 | buy construction materials direct from factories overseas platform | Compare | BUY | B | Retrieved only ([ddp-construction-materials](https://quotr.ai/blog/ddp-construction-materials/)) | Alibaba, Global Trade Plaza, Port2Site, AGTS, Marteu, BRKZ, ZeroGap, Commervia |
| T11 | C11 | E-007 | best AI construction estimating software 2026 | Compare | ALL | A | Absent (reproduced) | Togal.AI, Handoff, Buildxact, Procore AI, Bluebeam |
| T12 | C12 | E-073 | outsourced construction estimating service price per square foot for developers | Compare | SVC, DEV | A | Cited, not named: Quotr post was the **first citation**; rates credited to "some firms" (reproduced) | No brand named. Watch for: does the answer say "Quotr.ai charges $0.25/sq ft…"? |
| T13 | C13 | E-008 | AI estimating software for residential general contractors that goes from plans to proposal | Compare | RES | A | Absent (single session) | Handoff, BuildVision AI, Houzz Pro, Buildxact, Beam (trybeam) |
| T14 | C14 | E-082 | where can US contractors buy cabinets, windows and flooring factory direct at wholesale prices | Compare | BUY, RES | A | Absent | Build Source, Platinum Direct, Floor Daddy Depot, Shop At Home Cabinets and other local "factory direct" dealers |
| T15 | C15 | E-009 | best takeoff and estimating software for Mac users | Compare | SUB | B | Absent | STACK, Easy Takeoffs, Square Takeoff, Bluebeam, Buildxact |
| T16 | V1 | E-043 | Togal.AI alternatives | Compare | SUB, GC | A | **Named, low**: about 15th of 17 (run 1), 8th of 9 (run 2); single session | Procore, Autodesk Forma, Bluebeam lead (from G2/Capterra alternatives pages) |
| T17 | V2 | D-021 | Togal vs Quotr | Decide | SUB, GC | B | Named; positioning accurate; **stale price** ("$299.90 Solo / $499.90 Team") | Watch for: correct Lite $79.90 / Plus $299.90 prices |
| T18 | V3 | E-044 | PlanSwift alternatives 2026 | Compare | SUB | A | Cited, not named (both runs; single session) | STACK, Bluebeam, Procore, Autodesk, ProEst, Groundplan, Kreo, Togal |
| T19 | V4 | E-046 | Bluebeam alternatives for takeoff | Compare | SUB, GC | B | Absent | PlanSwift, STACK, On-Screen Takeoff, Togal.AI, Easy Takeoffs, Buildxact, Acrobat Pro |
| T20 | V5 | E-057 | Kreo vs Togal | Compare | SUB | B | Absent (only the two brands) | Kreo, Togal.AI |
| T21 | V6 | E-058 | STACK vs PlanSwift | Compare | SUB | B | Absent (only the two brands) | STACK, PlanSwift |
| T22 | V7 | E-054 | cheapest AI takeoff software | Compare | SUB, RES | A | Absent (Lite $79.90 not mentioned) | Kreo (~$35), Easy Takeoffs ($39), Pilars, QuoteIQ ($29.99) |
| T23 | V8 | E-055 | AI takeoff software with free trial | Compare | SUB | B | Absent (7-day trial not mentioned) | On-Screen Takeoff, PlanSwift, Kreo, Eano, eTakeoff, Intuitive Takeoff, BuildVision, Buildxact, Canaveral |
| T24 | V9 | E-059 | Beam AI vs Togal AI vs Kreo which is best for residential estimating | Compare | RES, SUB | B | Absent (engine merged Beam AI with trybeam.com) | Beam AI, Togal AI, Kreo |
| T25 | V10 | E-047 | STACK takeoff alternatives for small residential subcontractors | Compare | SUB, RES | A | Retrieved only ([stack-alternative](https://quotr.ai/blog/stack-alternative/)) | Easy Takeoffs, Buildxact, Square Takeoff, PlanSwift, Bluebeam, eTakeoff |
| T26 | P1 | L-031 | how to do a quantity takeoff from PDF plans | Learn | SUB, RES | B | Absent | No brand; Bluebeam, Autodesk, BuildVision, Kreo pages cited |
| T27 | P2 | L-047 | how to estimate drywall for a house | Learn | RES, SUB | B | Absent | No brand; calculators (HomeAdvisor, Easy Takeoffs, Procore, BuildVision, CertainTeed) cited |
| T28 | P3 | L-129 | how to estimate construction costs for a multifamily project | Learn | DEV | B | Absent | No brand; RSMeans, Brookings, RAND, lenders cited |
| T29 | P4 | L-108 | how to reduce building material costs | Learn | RES, DEV, BUY | A | Absent (factory-direct not mentioned as a lever) | NAHB, Autodesk, Buildertrend, Buildxact, Trimble, HUD cited |
| T30 | P5 | L-035 | how accurate is AI takeoff | Learn | SUB, GC | A | Cited, not named: Quotr post was the **first citation** (single session) | Watch for: is Quotr named next to its accuracy figures? |
| T31 | P6 | L-036 | can AI read construction drawings | Learn | ALL | B | Absent | helonic, nomic.ai, Bluebeam, mastt, ENR cited |
| T32 | P7 | L-006 | how long does a construction estimate take | Learn | SUB, GC, DEV | B | Absent | Estimating-service firms, Projul, r/estimators cited |
| T33 | P8 | L-109 | how to import building materials from China for a construction project | Learn | BUY, DEV, RES | A | Absent | Only sourcing agents and logistics firms cited |
| T34 | B1 | D-001 | What is Quotr.ai? | Decide | ALL | A | Named, **accurate** (both runs) | Watch for: "built by FLOZ Inc", "not a quotation app", disambiguation page cited |
| T35 | B2 | D-008 | Quotr.ai pricing | Decide | ALL | A | Named, accurate (Lite $79.90, Plus $299.90, Enterprise, 7-day trial, Service $0.25/$0.10 per sq ft); **flags legacy Solo/Team**; cites test.quotr.io (reproduced) | Watch for: Solo/Team mentions; staging host citations |
| T36 | B3 | D-014 | Is Quotr.ai legit? Quotr reviews | Decide | ALL | A | Named, but **uses the unrelated Quotr Pro app's 37 ratings / 4.7** as Quotr's; "not independently well-validated" (reproduced) | Watch for: Quotr Pro conflation; any G2/Capterra review count for Quotr.ai |
| T37 | B4 | D-022 | Quotr.ai vs Togal.AI | Decide | SUB, GC | A | Named; positioning accurate; **stale "from $299.90"** (reproduced) | Watch for: correct entry price |
| T38 | B5 | D-003 | Quotr app | Decide | ALL | B | Named **3rd of 4** "Quotr" apps | Watch for: Quotr.ai listed first |
| T39 | B6 | D-004 | Quotr construction software funding founders | Decide | ALL | B | Named; **funding conflict** ($3.5M seed vs a "$190K" figure that appears only in Perplexity answers) (reproduced) | Watch for: the $190K figure; founder names |
| T40 | B7 | D-023 | Quotr alternatives | Decide | ALL | B | Named ("the most end-to-end option"); about 10 of 18 citations are Quotr's own; retrieves G2 "Quartr" (a different company) | Watch for: share of third-party citations |

### 2b. Extension 13

| T# | Test ID | Library ID | Prompt (verbatim) | Stage | Persona | Tier | Sept 2026 baseline (Perplexity) | Named in answer / watch for |
|---|---|---|---|---|---|---|---|---|
| T41 | S4 | E-012 | best software for a GC to compare subcontractor and supplier bids / bid leveling for residential | Compare | GC, RES | B | Absent | Buildertrend, Buildxact, SmartBid, Procore Bid Management, Contractor Foreman |
| T42 | S5 | E-013 | best construction materials procurement software platforms for contractors and builders 2026 | Compare | BUY, GC | B | Absent | Procore, Archdesk, Trimble Materials, Buildertrend, Field Materials AI, Precoro |
| T43 | S6 | E-083 | where can home builders and multifamily developers buy building materials factory-direct from overseas manufacturers with AI takeoff and procurement | Compare | DEV, RES | B | Named: 1st in the original run, **3rd of 6** on re-run ("emphasize sourcing … more than AI takeoff") | Control prompt: it echoes Quotr's own wording, so it overstates visibility. Compare with T10 and T14 |
| T44 | S9 | E-074 | how much does it cost to outsource a quantity takeoff | Compare | SVC, SUB | B | Cited ([quantity-takeoff-services](https://quotr.ai/blog/quantity-takeoff-services/)); whether Quotr was named was not recorded | constructem, powerkh, takeoffmonkey, Bobyard also cited |
| T45 | S10 | L-130 | cost per sq ft to build multifamily 2026, material breakdown | Learn | DEV, FUND | B | Absent | Meltplan and Exayard cost pages cited next to RSMeans |
| T46 | S11 | L-113 | how are 2026 tariffs affecting building material costs for home builders and multifamily developers | Learn | RES, DEV | A | Absent; **no software vendor cited at all** | JEC, Brookings, NAHB, Construction Dive, Skanska, Cushman & Wakefield |
| T47 | S12 | L-134 | how much does it cost to rebuild a house after the LA fires per square foot 2026 | Learn | RES, DEV | B | Absent | Bloomberg and local GCs (Benson Construction, Amerbuild, UBIC, Vaisman) |
| T48 | N1 | L-114 | what tariffs apply to kitchen cabinets and vanities imported from China in 2026 | Learn | BUY, RES, DEV | A | Absent; no vendor named | White House, CNN, C.H. Robinson, Clark Hill, STR, Allyn cited |
| T49 | N2 | L-097 | how to estimate plumbing from drawings | Learn | SUB | A | **Cited, not named**: Quotr's [plumbing post](https://quotr.ai/blog/how-to-estimate-plumbing-from-drawings/) was the **first citation** and supplied most steps | RSMeans, Easy Takeoffs, ServiceTitan, Anvilfield also cited. Watch for: brand named |
| T50 | N3 | E-030 | best HVAC estimating software 2026 | Compare | SUB | B | Absent (Quotr's HVAC guide not retrieved) | QuoteIQ, ServiceTitan, FieldPulse, WenDuct |
| T51 | N4 | E-033 | best roofing takeoff software for new construction from plans | Compare | SUB | B | Absent | STACK, Beam AI, On-Screen Takeoff + Quick Bid, Buildxact |
| T52 | N5 | E-051 | Handoff alternatives for residential contractors | Compare | RES | B | Absent | Foreman, SimplyWise, Houzz Pro, Buildertrend, Buildxact, JobTread, Jobber, Contractor Foreman |
| T53 | N6 | L-052 | how to estimate a lumber package for a new house | Learn | RES, SUB | B | Absent; no software named | Angi, HomeAdvisor, Buildxact, Exayard and calculator sites cited |

**Tier A (22 prompts):** T01, T02, T04, T08, T09, T11, T12, T13, T14, T16, T18, T22, T25, T29, T30, T33, T34, T35, T36, T37, T46, T48, T49 minus one is not needed; the exact list is: T01, T02, T04, T08, T09, T11, T12, T13, T14, T16, T18, T22, T25, T29, T30, T33, T34, T35, T36, T37, T46, T48, T49 — see the "Tier" column, which is the source of truth.

---

## 3. How to run the tracking (step by step)

### 3.1 When

- **Once a month, in the first week** (for example, the first Tuesday–Thursday). Keep the same window each month.
- Monthly is the recommended cadence: AI citations change a lot from month to month, and weekly checks mostly measure noise (<../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md>, §4; Profound, a tracking vendor, reports 40–60% of cited domains changing month to month for the same query).
- One study found only about 10.6% of AI-cited URLs were still cited in all three waves 14 days apart, with 33% retention over 28 days (Digital Authority Partners; confirmed in <../../research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>, claim 37). So **never judge progress from one month**; look at three-month trends.

### 3.2 Which engines

| Engine | Cadence | How to run it | Why |
|---|---|---|---|
| **ChatGPT** (chatgpt.com, with web search) | Monthly | Logged out, or a **temporary chat** with memory off. If the answer does not search the web, re-ask with "search the web" and note it | Largest AI assistant; since May 2026 it links brand names to their homepages, which makes being named more valuable (verification_geo_evidence.md, claim 6) |
| **Google AI Mode** | Monthly | Signed out, private window, US location. Use the AI Mode tab | Google says AI Mode passed 1 billion monthly users and AI Overviews reached 2.5 billion (Google I/O, May 2026; verification_geo_evidence.md, claim 8) |
| **Google AI Overviews** | Monthly | Same private window, normal Google search. Record whether an AI Overview appears at all | AIOs appear on some queries only. Seer found "X vs Y" searches show an AIO 95.4% of the time, "best of" 81.3%, price/cost 83.4% (verification_geo_evidence.md, claim 21) |
| **Perplexity** | Monthly | (a) perplexity.ai, logged out, default mode; (b) the **Sonar API** (the tool used for the September baseline) for like-for-like comparison | The only engine with a baseline |
| **Gemini** (gemini.google.com) | Monthly | A clean Google account with no history, or a fresh session | Growing share of AI search activity (reported by Kevin Indig for H1 2026; not re-checked) |
| **Claude** (claude.ai, web search on) | Quarterly | A clean account or project, memory off | Smaller share of referrals today; cheap to add later |
| **Copilot** (copilot.microsoft.com) | Quarterly | Logged out | Bing-based; pairs with Bing Webmaster Tools data |

**Keep engines separate.** Report each engine on its own line. Do not blend them into one score: citations barely overlap across engines, and one study found ChatGPT and Gemini recommend a different #1 product in one of every three categories (headline only; <../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>, §6).

### 3.3 How many runs

| Option | What to run | Runs per month | Rough effort (our estimate) |
|---|---|---|---|
| **Lite** (manual, minimum) | Tier A (22) × ChatGPT, Google AI Mode, Perplexity × 1 run, plus all 53 × 2 runs on the Perplexity Sonar API (scripted) | 66 manual + 106 scripted | About 3 hours of manual work |
| **Standard** (recommended) | Tier A × 4 monthly engines × 2 runs; Tier B × 4 monthly engines × 1 run | 176 + 124 = 300 | 10–15 hours manually, so use a tracking tool |
| **Full** (quarterly) | Standard + Claude and Copilot (all 53 × 1 run) | 300 + 106 | Tool only |

Why two runs for Tier A: the September tests showed the **list of sources stays about the same from run to run, but the order of brands changes**, so position is noisy (<../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>, §5). 2026 research papers also argue for repeated sampling rather than one-off checks (verification_geo_evidence.md, M8). Tools such as Otterly.AI, Peec AI, Semrush's AI toolkit, Ahrefs Brand Radar or Profound can automate runs; prices are in [../07-measurement/tools-comparison.md](../07-measurement/tools-comparison.md).

### 3.4 Session rules (so months are comparable)

1. Use logged-out or clean sessions. Personalisation (history, memory, location) can change which brands are recommended (<../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>, §6).
2. Run from a US location. Write the location down.
3. Paste the prompt exactly. Do not ask follow-up questions in the same chat (except the "search the web" nudge for ChatGPT, which you must note).
4. Start a new chat for every prompt and every run.
5. Record the model or mode name the engine shows (for example "sonar", "GPT-…", "AI Mode").
6. Save the full answer and all source links, plus a screenshot or share link.

### 3.5 What to record for every run

| Field | How to fill it |
|---|---|
| Date | YYYY-MM-DD |
| Engine and mode | e.g. "ChatGPT – search", "Google AI Mode", "Google AIO", "Perplexity – web", "Perplexity – Sonar API" |
| Model shown | As displayed, or "not shown" |
| Session | "logged out", "temporary chat", "clean account" |
| T# and run | e.g. T01, run 1 |
| AIO shown? | Google AIO only: Yes / No |
| Quotr named? | Y / N. Count "Quotr", "Quotr.ai" or "Quotr.io" in the answer text |
| Position | Order of first mention among all brands (1 = first). "—" if not named |
| How Quotr is described | Copy the sentence (max 25 words) |
| Sentiment | + (recommended or positive), 0 (neutral mention), − (negative or doubtful) |
| Accuracy problems | Tick any from the checklist in 3.6 |
| quotr.ai cited? | Y / N, and the URL(s) used in the answer text |
| quotr.ai retrieved only? | Y / N (in the source list but not used) |
| Competitors named | In order, comma-separated |
| Top cited domains | The first 5–10 domains in the source list |
| Third-party pages naming Quotr | Any non-quotr.ai source that mentions Quotr (these are gold: log them in [../02-current-state/offsite-presence.md](../02-current-state/offsite-presence.md)) |
| Evidence | Screenshot file name or share link |

### 3.6 Accuracy checklist for brand prompts (T17, T34–T40)

Flag an answer if it says any of these. All are known errors from September 2026; the correct facts are in [../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md).

- [ ] Price "from $299.90", "Solo $299.90", "Team $499.90", "1 User Plan" or "2–10 Users Plan" (retired; current: Lite $79.90, Plus $299.90 per seat per month, Enterprise custom)
- [ ] Uses the **Quotr Pro – AI Estimate Maker** app (37 ratings, 4.7) or other namesake apps as evidence about Quotr.ai
- [ ] Cites test.quotr.io or another staging/legacy host
- [ ] Funding stated as "$190K seed (Oct 2024)" or any figure not confirmed by Quotr
- [ ] Factory count quoted as a conflict ("50+ to 220+") or a single number Quotr has not confirmed
- [ ] Describes Quotr as a Revit tool for architects, or as "a procurement program, not software"
- [ ] Says Quotr has no independent reviews (true today, but track when it changes)
- [ ] Mixes Quotr up with getquotr.com, quotrhq.com, "Quartr" or quotation/invoicing apps
- [ ] Any other wrong fact (write it down)

### 3.7 How to score each month

Use the same rules as the baseline (<../02-current-state/ai-visibility-baseline.md>, §1):

| KPI | Formula | Baseline (Perplexity, core 32 unbranded) |
|---|---|---|
| Mention rate | Unbranded prompts where Quotr is named ÷ unbranded prompts run | 3.1% |
| Citation rate | Unbranded prompts where a quotr.ai URL is cited in the answer ÷ unbranded prompts | 12.5% |
| Retrieval rate | Unbranded prompts with quotr.ai anywhere in the source list ÷ unbranded prompts | 18.8% |
| "Cited, not named" count | Prompts where Quotr is cited but not named | 3 (C12, V3, P5) |
| Share of voice | Quotr brand mentions ÷ all brand mentions (count each brand once per prompt) | ~0.7% |
| Average position | Mean position where named | Only V1 (~15th and 8th) |
| Brand accuracy | Brand prompts with ≥1 checklist error ÷ brand prompts | 5 of 8 |
| Third-party corroboration | Count of distinct non-quotr.ai pages naming Quotr in any answer | Octopus Builds, ForesightIQ, Nomic seen in September (all vendor or aggregator pages) |

Use the **first run** for the headline numbers, as the baseline did. Use the second run to check stability: if a result flips between runs, mark it "unstable".

### 3.8 Add first-party data to the same monthly report

| Source | What it shows | Note |
|---|---|---|
| Google Search Console → **Generative AI performance** reports | Impressions from AI Overviews and AI Mode by page, country and date | Rolled out worldwide on Aug 31, 2026. Shows **no clicks, CTR or queries**. Do not add to Web totals (verification_geo_evidence.md, M1) |
| Bing Webmaster Tools → **AI Performance** | Copilot/Bing AI citations | Public preview announced Feb 10, 2026 (verification_geo_evidence.md, claim 3) |
| GA4 → **AI Assistant** channel + a custom regex channel | Visits from AI tools | The native channel (May 13, 2026) does **not** include Perplexity, so keep a custom channel with a regex such as `chatgpt\.com|chat\.openai\.com|perplexity\.ai|gemini\.google\.com|copilot\.microsoft\.com|claude\.ai` placed above Referral (verification_geo_evidence.md, claim 7; playbook §4) |
| Demo/trial form: "How did you hear about us?" | Self-reported AI influence | Options should include ChatGPT, Google AI, Perplexity, YouTube, Reddit, Facebook group (playbook §4) |

Setup details: [../07-measurement/tracking-setup.md](../07-measurement/tracking-setup.md). KPI dashboard: [../07-measurement/kpis-and-dashboard.md](../07-measurement/kpis-and-dashboard.md).

---

## 4. Copy-paste templates

### 4.1 Run log (one row per run)

Markdown version:

```
| Date | Engine / mode | Model shown | Session | T# | Run | AIO shown? | Quotr named? | Position | How Quotr is described | Sentiment | Accuracy problems | quotr.ai cited (URLs) | Retrieved only? | Competitors named (in order) | Top cited domains | 3rd-party pages naming Quotr | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-06 | ChatGPT – search | | temporary chat | T01 | 1 | n/a | N | — | | | | | | | | | |
```

CSV header for a spreadsheet:

```
date,engine_mode,model_shown,session,t_id,run,aio_shown,quotr_named,position,quotr_description,sentiment,accuracy_problems,quotr_cited_urls,quotr_retrieved_only,competitors_named,top_cited_domains,third_party_pages_naming_quotr,evidence
```

### 4.2 Monthly summary (one row per engine)

```
| Month | Engine | Unbranded prompts run | Mention rate | Citation rate | Retrieval rate | Cited-not-named | SOV | Avg position | Brand accuracy errors | New 3rd-party pages naming Quotr | Change vs last month |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10 | Perplexity – Sonar API | 44 | | | | | | | | | |
| 2026-10 | ChatGPT – search | 44 | | | | | | | | | first month |
| 2026-10 | Google AI Mode | 44 | | | | | | | | | first month |
| 2026-10 | Gemini | 44 | | | | | | | | | first month |
```

### 4.3 Prompt-level trend (for the Tier A prompts)

```
| T# | Prompt | Engine | Sep-26 | Oct-26 | Nov-26 | Dec-26 | Jan-27 | Feb-27 | Notes |
|---|---|---|---|---|---|---|---|---|---|
| T01 | best AI takeoff software for subcontractors 2026 | Perplexity | Absent | | | | | | |
```

Use these short codes in the trend table: **N#** = named at position # · **C** = cited, not named · **R** = retrieved only · **A** = absent · **!** = accuracy problem.

### 4.4 Monthly note (5 lines, for the team)

```
Month:
1. Biggest change this month (prompt, engine, what changed):
2. New third-party pages that named Quotr:
3. Brand accuracy problems still showing (checklist items):
4. Pages published or fixed last month that we expected to move:
5. Action for next month:
```

---

## 5. Rules for changing the set

1. **Never edit a tracked prompt's wording.** If a better wording is needed, add it as a new prompt and keep the old one for at least three months.
2. **Add new prompts in a dated "Added" block** below 2b, with the next T number. Give each a first-run baseline before counting it in rates.
3. **Keep core 40 rates separate** from extension rates, so the September 2026 comparison stays clean.
4. **Year in prompts:** prompts containing "2026" should be kept as they are until January 2027. Then add a "2027" twin (for example, "best AI takeoff software for subcontractors 2027") and track both for three months.
5. **Review every quarter:** swap in up to 5 prompts from [prompt-library.md](prompt-library.md) where new Quotr pages have been published, so the set tests the pages the team is building.
6. **Watch the control prompt (T43).** It uses Quotr's own words. If Quotr is named there but not in T10 or T14, visibility has not really improved for buyer-style questions.

### Change log

| Date | Change |
|---|---|
| 2026-09-25 | Set created: core 40 (September baseline) + extension 13 (S4, S5, S6, S9, S10, S11, S12, N1–N6). N1–N6 given a first Perplexity Sonar run on 2026-09-25 |

---

## Related pages

- [prompt-library.md](prompt-library.md) — all 282 prompts, with priorities and the Quotr page for each
- [buyer-questions-by-trade.md](buyer-questions-by-trade.md) — real buyer questions by trade, with sources
- [../02-current-state/ai-visibility-baseline.md](../02-current-state/ai-visibility-baseline.md) — full September 2026 results and method
- [../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md) — correct facts to check brand answers against
- [../07-measurement/kpis-and-dashboard.md](../07-measurement/kpis-and-dashboard.md) — how these numbers roll into the KPI dashboard
- [../07-measurement/tracking-setup.md](../07-measurement/tracking-setup.md) — GA4, Search Console and Bing setup
- [../07-measurement/tools-comparison.md](../07-measurement/tools-comparison.md) — tools that can automate these runs
