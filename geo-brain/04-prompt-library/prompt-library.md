# Quotr GEO Prompt Library

**What this page is for:** The master list of questions ("prompts") that Quotr's buyers type into ChatGPT, Google (AI Overviews and AI Mode), Perplexity, Gemini, Claude and Copilot. Each prompt is sorted by funnel stage, persona and trade, tagged with its intent and a priority for Quotr, and matched to the Quotr page that should answer it. Use it to plan content and to choose prompts for monthly AI-visibility tracking.

**Last updated:** 2026-09-25

**Sources:**
- Research notes: <../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md> (40 tested prompts and results), <../../research_notes/Quotr GEO AEO strategy audit/competitor_geo_benchmark.md> (extra tested prompts, white space), <../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md> (§6 how construction buyers use AI), <../../research_notes/Quotr GEO AEO strategy audit/quotr_onsite_content_audit.md> (Quotr URL inventory), <../../research_notes/Quotr GEO AEO strategy audit/quotr_offsite_presence.md> (prompts O1–O6), <../../research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md> and <../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md> (corrections, which override the other notes).
- New research on 2026-09-25 (WebSearch and Perplexity Sonar): questions from ContractorTalk, Electrician Talk, PlumbingZone, HVAC-Talk, PaintTalk, Reddit (r/estimators, r/Construction, r/Flooring, r/HVAC, r/electricians, r/plumbers), YouTube video titles and "People also ask"-style search results. Every source link is listed trade by trade in [buyer-questions-by-trade.md](buyer-questions-by-trade.md).
- Quotr page URLs come from the blog sitemap, main sitemap and dictionary pages as recorded in the notes, plus a WebSearch of quotr.ai/dictionary (2026-09-25). All Quotr links point to https://quotr.ai.

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
- **Persona** (who asks). Codes match [../00-quotr/audiences-and-personas.md](../00-quotr/audiences-and-personas.md):

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
  - A link = the best existing page. "(optimize)" means the page exists but needs work first (for example, stale pricing or thin copy). See [../06-playbooks/page-refresh-checklist.md](../06-playbooks/page-refresh-checklist.md).
  - **NEW PAGE NEEDED** = no suitable page exists. A short suggestion follows.
  - **Off-site** = the answer mostly comes from other websites (G2, Capterra, listicles, Reddit). An on-site page alone will not win it. See [../03-market/citation-sources-map.md](../03-market/citation-sources-map.md).
  - **TO CONFIRM with Quotr** = the page cannot be written until Quotr confirms a fact.
- **Tested / seen**: either the September 2026 test result, or a link to where the real question was seen.
  - Test IDs (C, V, P, B, S, O) match [../02-current-state/ai-visibility-baseline.md](../02-current-state/ai-visibility-baseline.md). **N1–N6** are six extra prompts run once for this library (same tool, same day) to give the new tracking prompts a baseline. All tests used **Perplexity Sonar only** on 2026-09-25.
  - Result words: **Absent** = Quotr not named and not cited. **Cited, not named** = a quotr.ai page was a source but the answer did not say "Quotr". **Retrieved only** = a quotr.ai page was in the source list but not used. **Named** = Quotr appeared in the answer text.
  - "Seen:" links = the forum thread, Reddit thread, YouTube video or search result where the question appeared (research on 2026-09-25).

### Three rules before you write anything

1. **Do not build one page per prompt.** Many prompts here share one answer page. Google's May 2026 AI-search guide warns that pages made mainly for every variation of a query can count as scaled content abuse (<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>, claim 2). Group prompts into strong pages.
2. **Category prompts ("best X software") are won mostly off-site.** Perplexity recommended brands that appear on independent listicles and G2/Capterra "alternatives" pages. It used Quotr's own "best of" posts as fact sources but did not recommend Quotr from them (<../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>, §2 and §5). Also, sites that ranked themselves #1 in "best X" lists lost Google visibility in early 2026 (verification_geo_evidence.md, claim 19). Use honest comparison pages, and put most effort into third-party listings.
3. **Keep tested prompts word for word.** Even small wording changes change the answer. Prompts that echo Quotr's own copy can make Quotr look more visible than it is (test S6: Quotr was named only because the prompt used Quotr's own words; buyer-style versions C10 and C14 did not surface Quotr).

---

## Summary

| Stage | Prompts | High | Med | Low | Tested in Sept 2026 | Existing page fits | Page exists but needs work "(optimize)" | NEW PAGE NEEDED |
|---|---|---|---|---|---|---|---|---|
| 1. Learn / problem | 146 | 51 | 57 | 38 | 15 | 58 | 26 | 62 |
| 2. Compare / evaluate | 88 | 41 | 36 | 11 | 36 | 37 | 30 | 21 |
| 3. Decide / brand | 48 | 30 | 15 | 3 | 13 | 33 | 7 | 8 |
| **Total** | **282** | **122** | **108** | **52** | **64** | **128** | **63** | **91** |

Notes on the numbers:
- "Existing page fits" counts rows that link a page with no "(optimize)" flag. It includes rows marked "Off-site" or "TO CONFIRM" where no new page is proposed.
- "Tested" = the prompt was run word for word on Perplexity Sonar on 2026-09-25: 40 baseline prompts (C/V/P/B), 12 supplementary S prompts and 6 off-site O prompts (58, results in [../02-current-state/ai-visibility-baseline.md](../02-current-state/ai-visibility-baseline.md)), plus 6 new N prompts run once for this library (64 in total).
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

Trade coverage: every one of the 14 trades has at least 4 prompts; see [Views by trade](#views-by-trade).

---

## Stage 1 — Learn / problem (top of funnel)

At this stage AI answers usually cite sources but rarely name software brands. In September 2026, Quotr was **named in 0 of 8** tested how-to prompts and **cited in 1** (P5, accuracy of AI takeoff). Free calculators, cost-guide sites, Bluebeam/Autodesk/Procore guides, estimating-service firms and logistics firms won most citations (<../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>, §3). An extra test run for this library on the same day (N2, "how to estimate plumbing from drawings") showed the same pattern: Quotr's plumbing post was the **first citation** and supplied most of the steps, but the answer never said "Quotr". Specific, step-by-step trade how-tos get used; the brand name still has to be written into the key sentences.

### 1.1 General estimating and bidding

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| L-001 | how to estimate a construction job step by step | SUB, RES | GEN | Learn | Med | [/blog/how-to-price-construction-job/](https://quotr.ai/blog/how-to-price-construction-job/) | Seen: [YouTube "Construction Estimating: The Complete Step-by-Step Guide"](https://www.youtube.com/watch?v=qThAWmHIe3U) |
| L-002 | how do I learn construction estimating as a beginner | SUB, GC | GEN | Learn | Low | NEW PAGE NEEDED: "Estimating 101" hub linking the guides and dictionary | Seen: [r/estimators "best tools to learn estimating"](https://www.reddit.com/r/estimators/comments/1bclnno/best_tools_to_learn_estimating/), [r/estimators "tips for a new estimator"](https://www.reddit.com/r/estimators/comments/1ua6phd/tips_for_a_new_estimator/) |
| L-003 | how much overhead and profit should a subcontractor add to a bid | SUB | GEN | Cost | Med | NEW PAGE NEEDED: overhead and profit guide for subs (link to markup-vs-margin) | Seen: search results led by [markupandprofit.com](https://www.markupandprofit.com/articles/markup-on-subs/), [buildingadvisor.com](https://buildingadvisor.com/project-management/bidding/pricing-the-job-overhead-markup/) |
| L-004 | what is the difference between markup and margin in construction | SUB, RES | GEN | Define | Med | [/dictionary/markup-vs-margin/](https://quotr.ai/dictionary/markup-vs-margin/) | Seen: common r/Contractor topic; answer cites Procore, JobTread, Projul, Groundplan (Perplexity, 2026-09-25) |
| L-005 | what markup do I need to get a 30% profit margin | SUB, RES | GEN | Learn | Low | [/dictionary/markup-vs-margin/](https://quotr.ai/dictionary/markup-vs-margin/) (optimize: add the formula and a worked example) | Seen: same Perplexity answer (30% margin = about 42.9% markup) |
| L-006 | how long does a construction estimate take | SUB, GC, DEV | GEN | Learn | Med | NEW PAGE NEEDED: "How long an estimate takes, by project size" using Quotr Service job data | **P7 · Absent** (estimating-service firms and r/estimators cited) |
| L-007 | how fast should an estimator be able to do a takeoff | SUB, GC | GEN | Learn | Med | Same new benchmark page as L-006 | Seen: [r/estimators "how fast do you estimate"](https://www.reddit.com/r/estimators/comments/1j7h8eu/how_fast_do_you_estimate/) |
| L-008 | what is unit cost in construction estimating | ALL | GEN | Define | Low | [/dictionary/unit-price/](https://quotr.ai/dictionary/unit-price/) | — |
| L-009 | what is a plug number in an estimate | SUB, GC | GEN | Define | Low | [/dictionary/plug-number/](https://quotr.ai/dictionary/plug-number/) and [/blog/plug-number-estimating/](https://quotr.ai/blog/plug-number-estimating/) | — |
| L-010 | what is a cost code in construction | GC | GEN | Define | Low | [/dictionary/cost-code/](https://quotr.ai/dictionary/cost-code/) | — |
| L-011 | what is a scope gap and how do I avoid it between trades | GC, SUB | GEN | Learn | Med | [/blog/scope-gap-construction/](https://quotr.ai/blog/scope-gap-construction/) and [/dictionary/scope-gap/](https://quotr.ai/dictionary/scope-gap/) | Seen: r/ConstructionManagers topic; answers cite Piper, Struvia, Meltplan, Exayard (Perplexity, 2026-09-25) |
| L-012 | how do subcontractors bid GCs without giving away margin | SUB | GEN | Learn | Med | [/blog/how-subcontractors-bid-gcs-without-giving-away-margin/](https://quotr.ai/blog/how-subcontractors-bid-gcs-without-giving-away-margin/) | — |
| L-013 | how to bid commercial construction projects as a subcontractor | SUB | GEN | Learn | Med | [/blog/how-to-bid-commercial-construction-projects-subcontractor-estimating-takeoff-guide/](https://quotr.ai/blog/how-to-bid-commercial-construction-projects-subcontractor-estimating-takeoff-guide/) | — |
| L-014 | how to level subcontractor bids | GC, RES | GEN | Learn | High | [/dictionary/bid-leveling/](https://quotr.ai/dictionary/bid-leveling/) (optimize) + NEW PAGE NEEDED: full bid-leveling guide | Seen: [YouTube "How to Level Subcontractor Bids"](https://www.youtube.com/watch?v=TnhV7biCNTU) |
| L-015 | free bid leveling spreadsheet template for construction | GC, RES | GEN | Learn | High | NEW PAGE NEEDED: downloadable bid-leveling template (Struvia, Meltplan and Downtobid already publish templates) | Seen: Perplexity answer citing [struvia.co](https://struvia.co/blog/construction-bid-leveling-spreadsheet), [meltplan.com](https://www.meltplan.com/blogs/how-to-build-a-bid-leveling-spreadsheet-from-scratch), [downtobid.com](https://downtobid.com/blog/bid-leveling-template) |
| L-016 | what is the difference between bid tabulation and bid leveling | GC | GEN | Define | Low | [/dictionary/bid-leveling/](https://quotr.ai/dictionary/bid-leveling/) | Seen: [piper-ai.com](https://piper-ai.com/resources/bid-tabulation-vs-bid-leveling-vs-bid-evaluation) cited |
| L-017 | most common construction estimating mistakes | SUB, GC | GEN | Learn | Med | [/blog/construction-estimating-mistakes-to-avoid/](https://quotr.ai/blog/construction-estimating-mistakes-to-avoid/) | — |
| L-018 | should I hire an estimator or outsource estimating | SUB, GC, SVC | GEN | Service | High | [/blog/outsourcing-vs-hiring-an-estimator/](https://quotr.ai/blog/outsourcing-vs-hiring-an-estimator/) | — |
| L-019 | how much does a full-time construction estimator cost compared to outsourcing | SVC, GC | GEN | Cost | High | [/blog/outsourcing-vs-hiring-an-estimator/](https://quotr.ai/blog/outsourcing-vs-hiring-an-estimator/) (optimize: add brand-attributed prices, e.g. "Quotr.ai Service charges $0.25/sq ft…") | — |
| L-020 | how to protect a bid from material price increases (escalation clause) | SUB, GC, RES | SRC | Learn | High | [/blog/tariff-aware-estimating-material-escalation-every-bid/](https://quotr.ai/blog/tariff-aware-estimating-material-escalation-every-bid/) | Seen: AGC Jan 2026 survey coverage: 40% of contractors raised bids because of tariffs, 32% bought early (via Perplexity, [agc.org](https://www.agc.org/news/2026/01/14/construction-costs-rise-fastest-rate-january-2023-november-outpacing-increases-contractors-bid)) |
| L-021 | how long should a construction bid be valid when prices keep changing | SUB, GC | SRC | Learn | Med | [/blog/tariff-aware-estimating-material-escalation-every-bid/](https://quotr.ai/blog/tariff-aware-estimating-material-escalation-every-bid/) | — |
| L-022 | what is a GMP contract in construction | GC, DEV | GEN | Define | Low | [/dictionary/guaranteed-maximum-price/](https://quotr.ai/dictionary/guaranteed-maximum-price/) | — |
| L-023 | what is an RFI in construction | ALL | GEN | Define | Low | [/dictionary/rfi/](https://quotr.ai/dictionary/rfi/) | — |
| L-024 | how do I price a change order | SUB, GC | GEN | Learn | Low | [/dictionary/change-order/](https://quotr.ai/dictionary/change-order/) (optimize: add pricing steps) | — |
| L-025 | how to write a construction bid proposal that wins | SUB | GEN | Learn | Med | [/blog/ai-construction-proposals-takeoff-to-proposal/](https://quotr.ai/blog/ai-construction-proposals-takeoff-to-proposal/) | Seen: [YouTube "Construction Bidding and Proposals – Step-by-Step Guide"](https://www.youtube.com/watch?v=mNKTMHBmSmE) |
| L-026 | what should a subcontractor proposal include (inclusions, exclusions, clarifications) | SUB | GEN | Learn | Med | [/blog/ai-construction-proposals-takeoff-to-proposal/](https://quotr.ai/blog/ai-construction-proposals-takeoff-to-proposal/) (optimize) | — |
| L-027 | how to read construction drawings for estimating | SUB, RES | GEN | Learn | Med | NEW PAGE NEEDED: plan-reading guide for estimators (sheets, scales, schedules) | Seen: r/estimators beginner threads (L-002 links) |
| L-028 | metric vs imperial units in construction takeoff | SUB | GEN | Learn | Low | [/blog/metric-imperial-construction-takeoff/](https://quotr.ai/blog/metric-imperial-construction-takeoff/) | — |
| L-029 | why did construction costs go up so much in 2026 | GC, DEV, RES | SRC | Learn | Med | [/blog/construction-costs-surged-12-6-in-2026-how-ai-estimation-helps/](https://quotr.ai/blog/construction-costs-surged-12-6-in-2026-how-ai-estimation-helps/) and [/blog/construction-cost-trends-2026/](https://quotr.ai/blog/construction-cost-trends-2026/) | Seen: AGC reports input costs up 8.9% Aug 2025–Aug 2026 (via Perplexity, [agc.org](https://www.agc.org/news/2026/09/10/construction-input-costs-climb-89-between-august-2025-and-august-2026-association-survey-finds-war)) |

### 1.2 Takeoff and AI

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| L-030 | what is a construction takeoff | ALL | GEN | Define | Med | [/dictionary/quantity-takeoff/](https://quotr.ai/dictionary/quantity-takeoff/) and [/blog/construction-takeoff-guide/](https://quotr.ai/blog/construction-takeoff-guide/) | Seen: search results led by [STACK](https://www.stackct.com/blog/what-is-a-construction-takeoff/), [Buildxact](https://www.buildxact.com/us/blog/what-is-a-takeoff-in-construction/), [Procore](https://www.procore.com/library/construction-material-takeoff) |
| L-031 | how to do a quantity takeoff from PDF plans | SUB, RES | GEN | Learn | High | [/blog/how-to-do-construction-takeoff-pdf-blueprint/](https://quotr.ai/blog/how-to-do-construction-takeoff-pdf-blueprint/) (optimize) | **P1 · Absent** (Bluebeam, Autodesk, BuildVision cited) |
| L-032 | how do I do a quantity takeoff from PDF plans / what is AI takeoff | SUB | GEN | Learn | High | [/blog/how-to-do-construction-takeoff-pdf-blueprint/](https://quotr.ai/blog/how-to-do-construction-takeoff-pdf-blueprint/) and [/dictionary/ai-takeoff/](https://quotr.ai/dictionary/ai-takeoff/) | **S8 · Absent** (Quotr pages exist and rank in web search, but were not cited) |
| L-033 | what is AI takeoff | ALL | GEN | Define | Med | [/dictionary/ai-takeoff/](https://quotr.ai/dictionary/ai-takeoff/) | — |
| L-034 | what is AI construction estimating software | ALL | GEN | Define | Med | [/blog/what-is-ai-construction-estimating-software/](https://quotr.ai/blog/what-is-ai-construction-estimating-software/) | — |
| L-035 | how accurate is AI takeoff | SUB, GC | GEN | Trust | High | [/blog/is-ai-takeoff-actually-accurate-yet/](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/) (optimize: name Quotr in the key sentence, publish the test method) | **P5 · Cited, not named** (Quotr's post was the first citation; single-session result) |
| L-036 | can AI read construction drawings | ALL | GEN | Learn | High | [/blog/ai-that-reads-construction-drawings-chat-with-blueprints/](https://quotr.ai/blog/ai-that-reads-construction-drawings-chat-with-blueprints/) | **P6 · Absent** |
| L-037 | can ChatGPT do a construction takeoff | SUB, RES | GEN | Learn | High | [/blog/chatgpt-for-construction-estimating/](https://quotr.ai/blog/chatgpt-for-construction-estimating/) | — |
| L-038 | how does AI construction takeoff work | ALL | GEN | Learn | Med | [/blog/how-ai-construction-takeoff-works-in-2026/](https://quotr.ai/blog/how-ai-construction-takeoff-works-in-2026/) and [/blog/how-ai-construction-estimating-works/](https://quotr.ai/blog/how-ai-construction-estimating-works/) | — |
| L-039 | does AI takeoff work on scanned PDFs | SUB | GEN | Trust | Med | [/blog/is-ai-takeoff-actually-accurate-yet/](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/) (optimize: scanned vs vector section) | — |
| L-040 | how much time does AI takeoff actually save | SUB, GC | GEN | Cost | High | NEW PAGE NEEDED: published time-saved benchmark (the [/roi-calculator/](https://quotr.ai/roi-calculator/) models 80% but shows no data) | — |
| L-041 | are there actually any AI takeoff tools that work | SUB | GEN | Trust | High | [/blog/is-ai-takeoff-actually-accurate-yet/](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/) + Off-site (honest r/estimators participation) | Seen: [r/estimators "are there actually any AI-based takeoff software"](https://www.reddit.com/r/estimators/comments/1kadwx5/are_there_actually_any_aibased_takeoff_software/), [r/estimators "is there an AI automated takeoff software tool"](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/) |
| L-042 | will AI replace construction estimators | SUB, GC | GEN | Learn | Med | [/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/](https://quotr.ai/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/) and [/blog/construction-labor-shortage-ai-adoption-2026/](https://quotr.ai/blog/construction-labor-shortage-ai-adoption-2026/) | Seen: [YouTube "AI Estimating Software Tested – What They Don't Tell You"](https://www.youtube.com/watch?v=4vFOfHAPpYw) |
| L-043 | how are GCs using AI in preconstruction | GC | GEN | Learn | Med | [/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/](https://quotr.ai/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/) | — |
| L-044 | what is an AI agent for construction | GC, SUB | GEN | Define | Med | [/blog/ai-agent-for-construction/](https://quotr.ai/blog/ai-agent-for-construction/) | — |
| L-045 | what is the difference between a takeoff and an estimate | ALL | GEN | Define | Low | [/blog/construction-takeoff-guide/](https://quotr.ai/blog/construction-takeoff-guide/) | Seen: [STACK "What is a construction takeoff"](https://www.stackct.com/blog/what-is-a-construction-takeoff/) (takeoff excludes labour and overhead costs) |
| L-046 | how long does a takeoff take for a house | RES, SUB | GEN | Learn | Med | Same new benchmark page as L-006 / L-040 | Seen: FAQ pages by [McCormick](https://www.mccormicksys.com/blog/frequently-asked-questions-about-construction-takeoff/) and [The EDGE](https://www.estimatingedge.com/8-common-questions-about-construction-takeoff/) |

### 1.3 Trade questions

Real questions behind these prompts, with links, are in [buyer-questions-by-trade.md](buyer-questions-by-trade.md).

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| L-047 | how to estimate drywall for a house | RES, SUB | DRY | Learn | High | NEW PAGE NEEDED: free drywall calculator + [/blog/how-to-estimate-drywall-framing-commercial-floor-plan/](https://quotr.ai/blog/how-to-estimate-drywall-framing-commercial-floor-plan/) | **P2 · Absent** (calculators from HomeAdvisor, Easy Takeoffs, Procore, BuildVision, CertainTeed won) |
| L-048 | how many sheets of drywall do I need for a 2,000 sq ft house | RES | DRY | Cost | Med | NEW PAGE NEEDED: drywall calculator | Seen: Perplexity answer citing [HomeAdvisor](https://www.homeadvisor.com/cost/walls-and-ceilings/sheetrock-drywall-prices/) (area ÷ 32 per 4×8 sheet, +10% waste) |
| L-049 | how much should I charge per sheet to hang and finish drywall | SUB | DRY | Cost | Med | NEW PAGE NEEDED: drywall pricing guide | Seen: [CT "Newbie… How to bid drywall jobs"](https://www.contractortalk.com/threads/newbie-how-to-bid-drywall-jobs.274761/), [r/Construction "what should it cost to hang and finish drywall"](https://www.reddit.com/r/Construction/comments/y2pbdf/what_should_it_cost_to_hang_and_finish_drywall/) |
| L-050 | drywall labor and material cost per square foot 2026 | SUB, RES | DRY | Cost | Med | NEW PAGE NEEDED: drywall pricing guide | Seen: [CT "Drywall estimating and bidding"](https://www.contractortalk.com/threads/drywall-estimating-and-bidding.21199/) |
| L-051 | how to do a drywall takeoff from blueprints | SUB | DRY | Learn | High | [/software/trades/drywall/](https://quotr.ai/software/trades/drywall/) (optimize: thin page) + [/blog/how-to-estimate-drywall-framing-commercial-floor-plan/](https://quotr.ai/blog/how-to-estimate-drywall-framing-commercial-floor-plan/) | Seen: [YouTube "How To Do A Drywall Quantity Takeoff"](https://www.youtube.com/watch?v=fZejqlj-eyU) |
| L-052 | how to estimate a lumber package for a new house | RES, SUB | FRM | Learn | Med | [/software/trades/framing/](https://quotr.ai/software/trades/framing/) (optimize) + NEW PAGE NEEDED: framing and lumber takeoff guide | **N6 · Absent** (Angi, HomeAdvisor, Buildxact, Exayard and calculator sites cited; no software named) |
| L-053 | how to calculate board feet for framing lumber | SUB | FRM | Define | Low | Dictionary "board foot" term (named in the onsite audit; exact URL TO CONFIRM) | Seen: [Easy Takeoffs framing calculator](https://easytakeoffs.com/calculators/framing-lumber) |
| L-054 | framing labor cost per square foot 2026 | SUB, RES | FRM | Cost | Med | NEW PAGE NEEDED: framing pricing guide | Seen: [CT "Framing costs per sqft for labor"](https://www.contractortalk.com/threads/framing-costs-per-sqft-for-labor.459646/), [CT "Bidding framing job"](https://www.contractortalk.com/threads/bidding-framing-job.460347/) |
| L-055 | how many studs per linear foot of wall | RES | FRM | Learn | Low | NEW PAGE NEEDED (low): framing calculator | Seen: Autodesk guide above (wall length × 0.75, plus corners) |
| L-056 | how are tariffs on Canadian lumber affecting framing costs in 2026 | RES, DEV | FRM | Cost | High | [/blog/tariff-impact-construction-costs-2026-steel-aluminum-copper/](https://quotr.ai/blog/tariff-impact-construction-costs-2026-steel-aluminum-copper/) (optimize: add lumber) | Seen: AGC: lumber and plywood prices up 9.9% year over year by July 2026 (via Perplexity, [agc.org](https://www.agc.org/news/2026/08/13/construction-input-costs-climb-71-percent-between-july-2025-and-july-2026-impacts-war-and-tariffs)); [CT Public, 2026-09-11](https://www.ctpublic.org/news/2026-09-11/ct-new-home-construction-impacted-by-50-tariffs-on-canadian-wood-supplies) |
| L-057 | how much flooring waste should I add for LVP | SUB, RES | FLR | Learn | Med | NEW PAGE NEEDED: flooring waste-factor guide and calculator | Seen: [r/Flooring "LVP install waste"](https://www.reddit.com/r/Flooring/comments/1f8gn7x/lvp_install_waste/), [r/Flooring "how much wastage is normal"](https://www.reddit.com/r/Flooring/comments/1hhuc15/how_much_wastage_is_normal_on_a_professional/) |
| L-058 | how to price flooring installation per square foot | SUB | FLR | Cost | Med | [/blog/flooring-trades-how-to-quote-flooring-jobs-and-win-more-work/](https://quotr.ai/blog/flooring-trades-how-to-quote-flooring-jobs-and-win-more-work/) | Seen: [Housecall Pro flooring price guide](https://www.housecallpro.com/resources/flooring-price-guide/), [Quora thread](https://www.quora.com/How-do-contractors-price-a-flooring-job-Is-it-by-the-square-ft-of-the-actual-floor-they-are-installing-or-is-it-by-the-square-feet-of-the-material-they-are-using) |
| L-059 | how to do a flooring takeoff from plans by room and material | SUB | FLR | Learn | High | [/software/trades/flooring/](https://quotr.ai/software/trades/flooring/) (optimize) | Seen: [Togal flooring takeoff webinar](https://www.youtube.com/watch?v=TPN8_322B0s) (competitor video) |
| L-060 | LVP vs tile vs engineered hardwood cost for a new build | RES, DEV | FLR | Cost | High | NEW PAGE NEEDED: finish-material cost comparison using Quotr procurement prices | — |
| L-061 | how to buy flooring direct from the manufacturer for a development | DEV, BUY | FLR | Buy | High | [/procurement/](https://quotr.ai/procurement/) (optimize) + NEW PAGE NEEDED: factory-direct flooring guide | — |
| L-062 | how to estimate tile, thinset and grout for a bathroom | SUB, RES | TILE | Learn | Med | NEW PAGE NEEDED: tile materials calculator | Seen: calculators win this topic ([Easy Takeoffs tile calculator](https://easytakeoffs.com/calculators/tile), [Inch Calculator](https://www.inchcalculator.com/tile-calculator/)) |
| L-063 | tile installation labor cost per square foot 2026 | SUB | TILE | Cost | Low | NEW PAGE NEEDED (low): tile pricing guide | Seen: [CT "Commercial tile install per SF price"](https://www.contractortalk.com/threads/commercial-tile-install-per-sf-price.125029/) |
| L-064 | should I bid a tile shower per square foot or per job | SUB | TILE | Cost | Low | NEW PAGE NEEDED (low) | Seen: [DoItYourself "tile installation costs: bid vs per foot price?"](https://www.doityourself.com/forum/wall-flooring-indoor-tiling/405927-tile-installation-costs-bid-vs-per-foot-price.html) |
| L-065 | how to import porcelain tile from China and what duties apply | BUY, DEV | TILE | Buy | High | NEW PAGE NEEDED: tile import and landed-cost guide (whether tile is a Quotr procurement category is TO CONFIRM with Quotr) | Related: [/blog/sourcing-building-materials-china-cbd-fair-2026/](https://quotr.ai/blog/sourcing-building-materials-china-cbd-fair-2026/) |
| L-066 | how to estimate a painting job interior and exterior | SUB | PNT | Learn | Low | [/software/trades/painting/](https://quotr.ai/software/trades/painting/) (optimize) | Seen: [CT "How to estimate paint jobs"](https://www.contractortalk.com/threads/how-to-estimate-paint-jobs.97242/), [PaintTalk "How to do estimates for interior painting"](https://www.painttalk.com/threads/how-to-do-estimates-for-interior-painting.93337/) |
| L-067 | how many gallons of paint do I need per square foot of wall | RES, SUB | PNT | Learn | Low | NEW PAGE NEEDED (low): paint calculator | Seen: [Jobber painting estimate guide](https://www.getjobber.com/academy/painting/how-to-estimate-a-painting-job/) |
| L-068 | commercial painting estimate from drawings per square foot | SUB | PNT | Cost | Low | [/software/trades/painting/](https://quotr.ai/software/trades/painting/) (optimize) | Seen: [PaintTalk "Commercial estimating (exterior)"](https://www.painttalk.com/threads/commercial-estimating-exterior.2497/) |
| L-069 | how to estimate concrete for a slab in cubic yards | SUB, RES | CONC | Learn | Med | NEW PAGE NEEDED: concrete calculator + [/software/trades/concrete/](https://quotr.ai/software/trades/concrete/) | Seen: STACK publishes free concrete content ([stackct.com](https://www.stackct.com/blog/free-concrete-estimating-software-cloud-based-no-download/)) |
| L-070 | how to bid concrete flatwork per square foot | SUB | CONC | Cost | Med | NEW PAGE NEEDED: concrete pricing guide | Seen: [CT "New construction flatwork price?"](https://www.contractortalk.com/threads/new-construction-flatwork-price.88489/) |
| L-071 | how to estimate rebar for a foundation | SUB | CONC | Learn | Med | [/blog/rebar-estimating-and-takeoff-software/](https://quotr.ai/blog/rebar-estimating-and-takeoff-software/) (fix stale pricing) + [/dictionary/rebar/](https://quotr.ai/dictionary/rebar/) | — |
| L-072 | how to calculate formwork for footings and walls | SUB | CONC | Learn | Low | Dictionary "formwork" term (named in the onsite audit; exact URL TO CONFIRM) | — |
| L-073 | how to estimate a roof in squares with pitch and waste | SUB | ROOF | Learn | Med | [/software/trades/roofing/](https://quotr.ai/software/trades/roofing/) (optimize: roofing has no blog content) | Seen: [CT "Total squares for bid? How do you come up with your total?"](https://www.contractortalk.com/threads/total-squares-for-bid-how-do-you-guys-come-up-with-your-total.37342/), [YouTube "How to Write Roofing Estimates Using Roof Measurements"](https://www.youtube.com/watch?v=O5QycPWhnLA) |
| L-074 | how to do a roofing takeoff from plans for new construction | SUB | ROOF | Learn | High | NEW PAGE NEEDED: plan-based roofing takeoff guide (satellite reports can struggle with new construction, so plans are the source) | Seen: Perplexity summary of EagleView vs Hover sources: aerial reports "can struggle with trees/new construction" ([roofingsoftwareguide.com](https://roofingsoftwareguide.com/roundups/best-roofing-aerial-imagery-software/)) |
| L-075 | roofing cost per square 2026 labor and materials | SUB, RES | ROOF | Cost | Low | NEW PAGE NEEDED (low) | Seen: [build-folio roofing pricing guide](https://build-folio.com/contractor-guides/roofing-pricing-guide/) |
| L-076 | EagleView vs Hover vs manual roof measurements | SUB | ROOF | VS | Low | None needed (low fit). Mention inside the L-074 page | Seen: r/Roofing topic; [theroofingbrief.com](https://theroofingbrief.com/eagleview-vs-hover-vs-roofsnap/) cited |
| L-077 | how to estimate siding squares from elevation drawings | SUB | SID | Learn | Med | NEW PAGE NEEDED: siding takeoff guide (Quotr has no siding trade page) | Seen: [Hover "How to bid a siding job"](https://hover.to/blog/how-to-bid-a-siding-job) |
| L-078 | vinyl siding cost per square installed 2026 | SUB, RES | SID | Cost | Low | NEW PAGE NEEDED (low) | Seen: [CT "Vinyl siding cost per square installed"](https://www.contractortalk.com/threads/vinyl-siding-cost-per-square-installed.33064/) |
| L-079 | should I charge for siding by the square or by the job | SUB | SID | Cost | Low | NEW PAGE NEEDED (low) | Seen: [CT "Siding installation: charge by square or by job?"](https://www.contractortalk.com/threads/siding-installation-charge-by-square-or-by-job.148615/) |
| L-080 | how much should I charge to install a replacement window | SUB | WIN | Cost | Low | NEW PAGE NEEDED (low) | Seen: [CT "What would you charge for labor on a replacement window?"](https://www.contractortalk.com/threads/what-would-you-charge-for-labor-on-a-replacement-window.65275/) |
| L-081 | how to do a window and door schedule takeoff from plans | SUB, RES, DEV | WIN | Learn | High | [/software/trades/glazing/](https://quotr.ai/software/trades/glazing/) and [/software/trades/doors-hardware/](https://quotr.ai/software/trades/doors-hardware/) (optimize) | — |
| L-082 | do imported windows need NFRC certification | BUY, DEV | WIN | Learn | High | NEW PAGE NEEDED: certification FAQ (NFRC, CARB, cUPC). Quotr's DDP price says it includes certification documents (index-only text; TO CONFIRM with Quotr) | — |
| L-083 | what is the lead time for windows in 2026 | RES, DEV | WIN | Learn | High | NEW PAGE NEEDED: lead-time tracker by material | — |
| L-084 | how much can I save on windows buying factory direct | DEV, BUY | WIN | Cost | High | [/procurement/](https://quotr.ai/procurement/) (optimize: show window line items) | Seen: [YouTube short "Saved $50k with windows from China…"](https://www.youtube.com/shorts/eUEi-uEzSj8) |
| L-085 | how to price cabinet installation per linear foot | SUB | CAB | Cost | Low | NEW PAGE NEEDED (low) | Seen: [CT "pricing cabinet install"](https://www.contractortalk.com/threads/pricing-cabinet-install.75922/), [CT "Cabinet install pricing"](https://www.contractortalk.com/threads/cabinet-instal-pricing.20149/) |
| L-086 | what markup do contractors put on cabinets | RES, SUB | CAB | Cost | Med | NEW PAGE NEEDED: cabinet buying guide for builders | Seen: [Houzz "contractor mark up on cabinets?"](https://www.houzz.com/discussions/2687506/contractor-mark-up-on-cabinets), [CT "Bidding on kitchen remodels"](https://www.contractortalk.com/threads/bidding-on-kitchen-remodels.337881/) |
| L-087 | kitchen cabinet tariffs 2026 what builders need to know | RES, DEV, BUY | CAB | Cost | High | NEW PAGE NEEDED: cabinet and vanity tariff explainer | Seen: [NextDAY Cabinets 2026 tariff guide](https://nextdaycabinets.com/kitchen-cabinet-tariffs-in-2026-what-contractors-and-builders-need-to-know-about-section-232-tariff-updates/) (a supplier already targets this question) |
| L-088 | RTA vs custom vs factory-direct cabinets cost per linear foot | RES, DEV | CAB | Cost | High | NEW PAGE NEEDED: cabinet cost comparison with Quotr procurement prices | — |
| L-089 | how to estimate countertop square footage and slab count | SUB, RES | CAB | Learn | Low | NEW PAGE NEEDED (low) | Seen: [SlabWise contractor pricing sheet](https://slabwise.com/checklist/contractor-pricing-sheet) |
| L-090 | are imported cabinets CARB Phase 2 / TSCA Title VI compliant | BUY, DEV | CAB | Learn | High | NEW PAGE NEEDED: certification FAQ (same page as L-082) | — |
| L-091 | how to estimate electrical work from drawings | SUB | ELEC | Learn | High | [/blog/how-to-estimate-electrical-work-from-drawings-conduit-devices-labor/](https://quotr.ai/blog/how-to-estimate-electrical-work-from-drawings-conduit-devices-labor/) | Seen: [r/estimators "how do you estimate electrical"](https://www.reddit.com/r/estimators/comments/1mkde6w/how_do_you_estimate_electrical/), [r/electricians "how do you estimate/bid on jobs"](https://www.reddit.com/r/electricians/comments/2cpo3y/how_do_you_estimatebid_on_jobs/) |
| L-092 | residential electrical pricing per opening vs per square foot | SUB | ELEC | Cost | Med | [/blog/how-to-estimate-electrical-work-from-drawings-conduit-devices-labor/](https://quotr.ai/blog/how-to-estimate-electrical-work-from-drawings-conduit-devices-labor/) (optimize: add residential pricing section) | Seen: [Electrician Talk "Pricing sq. ft. vs. per opening"](https://www.electriciantalk.com/threads/pricing-sq-ft-vs-per-opening.5112/), [r/electricians "bidding houses"](https://www.reddit.com/r/electricians/comments/1r4z3qj/bidding_houses/) |
| L-093 | electrical cost per square foot for new home construction 2026 | RES, DEV | ELEC | Cost | Med | NEW PAGE NEEDED: residential trade-cost benchmarks (one page for all trades) | Seen: [Electrician Talk "How to bid new homes"](https://www.electriciantalk.com/threads/how-to-bid-new-homes.212025/) |
| L-094 | is there an AI tool that can count electrical symbols on a PDF | SUB | ELEC | Tool | High | [/software/trades/electrical/](https://quotr.ai/software/trades/electrical/) | — |
| L-095 | what is a panel schedule | SUB | ELEC | Define | Low | [/dictionary/panel-schedule/](https://quotr.ai/dictionary/panel-schedule/) | — |
| L-096 | how to do a commercial electrical takeoff from drawings to proposal | SUB | ELEC | Learn | High | [/blog/commercial-electrical-takeoff-drawings-to-proposal/](https://quotr.ai/blog/commercial-electrical-takeoff-drawings-to-proposal/) | Seen: [YouTube "Electrical Estimating for New Residential Construction Simplified"](https://www.youtube.com/watch?v=Mp_Vvpm2ybo) |
| L-097 | how to estimate plumbing from drawings | SUB | PLMB | Learn | High | [/blog/how-to-estimate-plumbing-from-drawings/](https://quotr.ai/blog/how-to-estimate-plumbing-from-drawings/) | **N2 · Cited, not named** (Quotr's post was the first citation and supplied most steps; RSMeans, Easy Takeoffs, ServiceTitan, Anvilfield also cited). Seen: [r/plumbers "help with estimates"](https://www.reddit.com/r/plumbers/comments/128c749/help_with_estimates/) |
| L-098 | plumbing price per fixture for new construction 2026 | SUB, RES | PLMB | Cost | Med | [/blog/how-to-estimate-plumbing-from-drawings/](https://quotr.ai/blog/how-to-estimate-plumbing-from-drawings/) (optimize) or the trade-cost benchmark page (L-093) | Seen: [PlumbingZone "Going rate per fixture – new construction"](https://www.plumbingzone.com/threads/going-rate-per-fixture-new-construction.82414/), [r/askaplumber "bidding for new construction plumbing"](https://www.reddit.com/r/askaplumber/comments/1nto7zy/bidding_for_new_construction_plumbing/) |
| L-099 | what is rough-in plumbing and how is it priced | SUB, RES | PLMB | Define | Low | [/dictionary/rough-in-plumbing/](https://quotr.ai/dictionary/rough-in-plumbing/) | Seen: [Fine Homebuilding "new construction rough-in plumbing costs"](https://www.finehomebuilding.com/forum/new-construction-rough-in-plumbing-costs) |
| L-100 | how much does it cost to plumb a 2,000 sq ft house | RES | PLMB | Cost | Low | Trade-cost benchmark page (L-093) | Seen: [digitalestimating.com](https://digitalestimating.com/what-is-the-cost-to-plumb-a-2000-sq-ft-house/) |
| L-101 | do imported plumbing fixtures need cUPC certification | BUY | PLMB | Learn | High | NEW PAGE NEEDED: certification FAQ (same page as L-082) | — |
| L-102 | how to estimate HVAC ductwork from a mechanical plan | SUB | HVAC | Learn | High | [/blog/how-to-estimate-hvac-sheet-metal-mechanical-plan/](https://quotr.ai/blog/how-to-estimate-hvac-sheet-metal-mechanical-plan/) | — |
| L-103 | how do you bid new construction residential HVAC (Manual J, price per ton) | SUB | HVAC | Cost | Med | [/blog/how-to-estimate-hvac-sheet-metal-mechanical-plan/](https://quotr.ai/blog/how-to-estimate-hvac-sheet-metal-mechanical-plan/) (optimize: add a residential section) | Seen: [r/HVAC "at what point do you do the Manual J"](https://www.reddit.com/r/HVAC/comments/avh37t/at_what_point_do_you_guys_do_the_manual_j/), [HVAC-Talk "New construction HVAC bid questions"](https://hvac-talk.com/vbb/threads/1803581-New-Construction-HVAC-bid-questions) |
| L-104 | HVAC cost per ton for new construction 2026 | SUB, RES | HVAC | Cost | Low | Trade-cost benchmark page (L-093) | Seen: [Simpro "How to estimate HVAC jobs"](https://www.simprogroup.com/blog/how-to-bid-hvac-jobs) |
| L-105 | how to estimate spray foam insulation in board feet | SUB | INS | Learn | Low | [/software/trades/insulation/](https://quotr.ai/software/trades/insulation/) (optimize) | Seen: [CT "How much is spray foam per square foot?"](https://www.contractortalk.com/answers/how-much-is-spray-foam-per-square-foot/) |
| L-106 | blown-in cellulose vs spray foam cost per square foot 2026 | RES | INS | Cost | Low | Trade-cost benchmark page (L-093) | Seen: [CT "spray foam cost?"](https://www.contractortalk.com/threads/spray-foam-cost.94282/) |
| L-107 | how to do an insulation takeoff from plans | SUB | INS | Learn | Med | [/software/trades/insulation/](https://quotr.ai/software/trades/insulation/) (optimize) | — |

### 1.4 Material costs, sourcing, tariffs and importing

This is Quotr's clearest white space. In September 2026, tariff and importing answers cited only government, media and logistics sources, and **no software vendor at all** (<../../research_notes/Quotr GEO AEO strategy audit/competitor_geo_benchmark.md>, §3 and §5).

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| L-108 | how to reduce building material costs | RES, DEV, BUY | SRC | Learn | High | [/blog/reduce-construction-material-costs/](https://quotr.ai/blog/reduce-construction-material-costs/) (optimize: add factory-direct as a named lever with project numbers) | **P4 · Absent** (NAHB, Autodesk, Buildertrend, Buildxact, Trimble, HUD cited; factory-direct not mentioned) |
| L-109 | how to import building materials from China for a construction project | BUY, DEV, RES | SRC | Learn | High | [/blog/how-developers-source-building-materials/](https://quotr.ai/blog/how-developers-source-building-materials/) (optimize) + NEW PAGE NEEDED: neutral step-by-step importing guide | **P8 · Absent** (only sourcing agents and logistics firms cited) |
| L-110 | what does DDP mean when buying building materials | BUY, DEV | SRC | Define | High | [/blog/ddp-construction-materials/](https://quotr.ai/blog/ddp-construction-materials/) | — |
| L-111 | DDP vs FOB for importing building materials, which is better | BUY | SRC | Learn | High | [/blog/ddp-construction-materials/](https://quotr.ai/blog/ddp-construction-materials/) (optimize: honest FOB vs DDP table) | Seen: guides by [Gerudo Logistics](https://www.gerudologistics.com/shipping-guides/how-to-ship-building-materials-from-china) and [SinoEuro Ruida](https://www.snrida.com/blog/complete-guide-importing-building-materials-china) say FOB is the norm and warn about DDP duty allocation |
| L-112 | how to calculate landed cost for imported cabinets or windows | BUY, DEV | SRC | Cost | High | NEW PAGE NEEDED: landed-cost calculator | Seen: a WebSearch summary of 2026 importing guides (e.g. [chinabestbuying.com](https://chinabestbuying.com/import-building-materials-china-us/), [gerudologistics.com](https://www.gerudologistics.com/shipping-guides/how-to-ship-building-materials-from-china)) put landed cost at 1.3–1.7× the FOB price; the exact source page was not isolated, so check before quoting |
| L-113 | how are 2026 tariffs affecting building material costs for home builders and multifamily developers | RES, DEV | SRC | Learn | High | [/blog/tariff-impact-construction-costs-2026-steel-aluminum-copper/](https://quotr.ai/blog/tariff-impact-construction-costs-2026-steel-aluminum-copper/) (optimize: residential finish materials, quarterly update) | **S11 · Absent** (JEC, Brookings, NAHB, Construction Dive, Skanska, Cushman & Wakefield; no vendor) |
| L-114 | what tariffs apply to kitchen cabinets and vanities imported from China in 2026 | BUY, RES, DEV | CAB | Cost | High | NEW PAGE NEEDED: cabinet and vanity tariff explainer (same page as L-087) | **N1 · Absent** (no vendor named; White House, CNN, C.H. Robinson, Clark Hill, STR cited). Facts: Section 232 tariff of 25% since Oct 14, 2025; rise to 50% delayed to Jan 1, 2027 ([Thompson Hine SmarTrade](https://www.thompsonhinesmartrade.com/2026/01/president-trump-delays-section-232-tariff-increase-on-wood-furniture-cabinets-and-vanities/)); separate AD/CVD orders since 2020 ([Federal Register](https://www.federalregister.gov/documents/2020/04/21/2020-08544/wooden-cabinets-and-vanities-and-components-thereof-from-the-peoples-republic-of-china-antidumping)) |
| L-115 | what is an HTS code and how do I find it for building materials | BUY | SRC | Define | Med | NEW PAGE NEEDED: importing glossary + HTS lookup how-to (see [construction-glossary.md](construction-glossary.md)) | Seen: [USITC HTS search](https://hts.usitc.gov/) |
| L-116 | do I need a customs broker to import building materials | BUY | SRC | Learn | Med | NEW PAGE NEEDED: importing guide (same as L-109) | — |
| L-117 | what is an ISF filing for importing | BUY | SRC | Define | Low | Glossary page | Seen: [CBP ISF help article](https://www.help.cbp.gov/s/article/Article-1868) |
| L-118 | how long does it take to ship building materials from China to California | BUY, DEV | SRC | Learn | High | NEW PAGE NEEDED: lead-time page (Quotr's indexed copy says delivery "typically within about 90 days"; TO CONFIRM with Quotr) | — |
| L-119 | how much does it cost to ship a 40ft container of building materials from China in 2026 | BUY | SRC | Cost | Med | NEW PAGE NEEDED: landed-cost calculator (L-112) | — |
| L-120 | is it still worth importing building materials from China after tariffs | RES, DEV | SRC | Learn | High | NEW PAGE NEEDED: honest "when factory-direct pays and when it doesn't" page, with /procurement/ project numbers | Seen: [Handoff "Local vs imported materials: a GC's guide to navigating the tariffs"](https://www.handoff.ai/blog/local-vs-imported-materials-a-gcs-guide-to-navigating-the-tariffs) (a competitor already covers this) |
| L-121 | how to check quality of building materials from Chinese factories | BUY, DEV | SRC | Learn | High | [/procurement/](https://quotr.ai/procurement/) (optimize) + NEW PAGE NEEDED: QC and inspection explainer | — |
| L-122 | what to know before sourcing building materials in Foshan | BUY | SRC | Learn | Med | [/blog/sourcing-building-materials-china-cbd-fair-2026/](https://quotr.ai/blog/sourcing-building-materials-china-cbd-fair-2026/) | Seen: [YouTube "How We Source High-End Building Materials in China"](https://www.youtube.com/watch?v=Fp94HFjPlSg) |
| L-123 | how are contractors handling material price escalation in 2026 | GC, SUB | SRC | Learn | Med | [/blog/construction-cost-trends-2026/](https://quotr.ai/blog/construction-cost-trends-2026/) | Seen: AGC surveys (L-020, L-029) |
| L-124 | construction materials price index 2026 (PPI) | GC, DEV | SRC | Cost | Med | [/blog/construction-cost-index-q1-2026-ppi-rsmeans-mortenson/](https://quotr.ai/blog/construction-cost-index-q1-2026-ppi-rsmeans-mortenson/) (optimize: update every quarter) | Seen: [ENR cost data](https://www.enr.com/economics/current_costs) |
| L-125 | what is the construction procurement process | GC, DEV | SRC | Learn | Med | [/blog/construction-procurement-process/](https://quotr.ai/blog/construction-procurement-process/) and [/blog/what-is-construction-procurement-2026-guide/](https://quotr.ai/blog/what-is-construction-procurement-2026-guide/) | — |
| L-126 | what is buyout in construction | GC | SRC | Define | Med | [/blog/takeoff-to-buyout-construction-estimating-procurement-platform/](https://quotr.ai/blog/takeoff-to-buyout-construction-estimating-procurement-platform/) | — |
| L-127 | how to get and compare supplier quotes for a construction project | SUB, GC, BUY | SRC | Learn | Med | NEW PAGE NEEDED: RFQ how-to (links to the /software/ bid-comparison feature) | — |
| L-128 | how to source hotel FF&E and finishes in one consolidated order | BUY, DEV | SRC | Learn | Low | [/blog/hospitality-procurement-consolidated-sourcing/](https://quotr.ai/blog/hospitality-procurement-consolidated-sourcing/) | — |

### 1.5 Developer, preconstruction and residential cost questions

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| L-129 | how to estimate construction costs for a multifamily project | DEV | GEN | Learn | High | NEW PAGE NEEDED: multifamily cost-estimating guide built from Quotr Service data | **P3 · Absent** (RSMeans, Brookings, RAND, lenders cited) |
| L-130 | cost per sq ft to build multifamily 2026, material breakdown | DEV, FUND | GEN | Cost | High | NEW PAGE NEEDED: multifamily $/sq ft benchmark (Meltplan and Exayard already win this) | **S10 · Absent** |
| L-131 | cost per unit to build a garden-style apartment in California 2026 | DEV | GEN | Cost | High | NEW PAGE NEEDED: same benchmark page, per-unit view | Seen: r/RealEstateDevelopment topic; answer cites [propertybuild.com](https://propertybuild.com/multifamily-construction/), [innergyintegral.com](https://innergyintegral.com/resources/multifamily-proforma-construction-costs/) (Perplexity, 2026-09-25) |
| L-132 | how much does it cost to build a house per square foot in California 2026 | RES, DEV | GEN | Cost | High | NEW PAGE NEEDED: residential $/sq ft by region | — |
| L-133 | how much does it cost to build an ADU in California 2026 | DEV, RES | GEN | Cost | High | NEW PAGE NEEDED: ADU cost guide (Bay Area focus, where Quotr's procurement projects are) | Seen: builder pages such as [cali-adu.com](https://cali-adu.com/blog/cost-to-build-adu/), [greatbuildz.com](https://www.greatbuildz.com/blog/cost-to-build-an-adu-in-los-angeles/) rank for this |
| L-134 | how much does it cost to rebuild a house after the LA fires per square foot 2026 | RES, DEV | GEN | Cost | High | NEW PAGE NEEDED: LA rebuild cost guide (reuse the "Fast Cost Estimation (Residential LA Fire Rebuilding)" sample and the FireTips app) | **S12 · Absent** (Bloomberg and local GCs cited) |
| L-135 | hard costs vs soft costs in real estate development | DEV, FUND | GEN | Define | Med | NEW PAGE NEEDED: developer glossary entry + guide | Seen: [adventuresincre.com](https://www.adventuresincre.com/glossary/hard-costs/), [dealworthit.com](https://dealworthit.com/blog/hard-costs-vs-soft-costs-real-estate-development) cited |
| L-136 | how do developers estimate construction costs before buying land | DEV | GEN | Learn | High | [/blog/quotr-developer-desk-underwriting-grade-estimates-72-hours/](https://quotr.ai/blog/quotr-developer-desk-underwriting-grade-estimates-72-hours/) (optimize: a method page, not a product post) | Seen: r/RealEstateDevelopment topic; answer cites [multifamily.loans](https://www.multifamily.loans/apartment-finance-blog/hard-vs-soft-construction-costs-for-multifamily-developers/) (Perplexity, 2026-09-25) |
| L-137 | how accurate are early-stage construction cost estimates | DEV, FUND | GEN | Trust | Med | NEW PAGE NEEDED: estimate classes and accuracy ranges | Seen: [multifamily.loans](https://www.multifamily.loans/apartment-finance-blog/hard-vs-soft-construction-costs-for-multifamily-developers/) gives 30–50% (early) to 5–15% (late) accuracy ranges |
| L-138 | how to build a development pro forma for a small multifamily project | DEV | GEN | Learn | High | [/blog/construction-proforma-software/](https://quotr.ai/blog/construction-proforma-software/) and [/blog/the-proforma-that-never-stops-changing/](https://quotr.ai/blog/the-proforma-that-never-stops-changing/) (optimize) | — |
| L-139 | how to budget a spec home build | RES, DEV | GEN | Learn | Med | NEW PAGE NEEDED: spec-home budget guide | — |
| L-140 | what is value engineering and how do I do it when bids come in high | DEV, GC, ARCH | GEN | Learn | Med | NEW PAGE NEEDED | — |
| L-141 | how to check a developer's construction budget as a lender | FUND | GEN | Learn | Med | NEW PAGE NEEDED: budget-review method page | — |
| L-142 | how much contingency should I carry in a construction budget | DEV, FUND | GEN | Cost | Med | NEW PAGE NEEDED | — |
| L-143 | how to get a construction cost estimate from a Revit model | ARCH | GEN | Learn | Low | TO CONFIRM with Quotr (is the Revit add-in still sold?) | — |
| L-144 | how can architects estimate construction cost during design | ARCH | GEN | Learn | Low | [/blog/the-architects-survival-guide-unlocking-new-revenue-streams-in-pre-construction/](https://quotr.ai/blog/the-architects-survival-guide-unlocking-new-revenue-streams-in-pre-construction/) | — |
| L-145 | house flipping renovation budget math 2026 | RES | GEN | Cost | Low | [/blog/house-flipping-math-2026/](https://quotr.ai/blog/house-flipping-math-2026/) | — |
| L-146 | how to estimate MEP costs on a data center project | SUB, GC | GEN | Learn | Low | [/blog/data-center-construction-estimating-mep-subcontractor-choke-point/](https://quotr.ai/blog/data-center-construction-estimating-mep-subcontractor-choke-point/) | — |

---
## Stage 2 — Compare / evaluate (middle of funnel)

This is where Quotr loses most today. In September 2026, Quotr was **named in 0 of 15** category prompts and **1 of 9** unbranded comparison prompts (only "Togal.AI alternatives", near the bottom). Perplexity built these answers from independent listicles (constructioncoverage.com, thedigitalprojectmanager.com, ConstructConnect, ContraVault), G2/Capterra/SourceForge "alternatives" pages and competitors' own listicles. Quotr's own comparison posts were used as fact sources but did not get Quotr recommended (<../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>, §1, §2, §5). Seer found "X vs Y" searches show a Google AI Overview 95.4% of the time (<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>, claim 21), so comparison pages are almost always read by AI.

### 2.1 Category prompts (all trades and personas)

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| E-001 | best AI takeoff software for subcontractors 2026 | SUB | GEN | Tool | High | [/blog/best-ai-construction-estimating-software-2026/](https://quotr.ai/blog/best-ai-construction-estimating-software-2026/) (optimize: honest, not self-ranked; fix stale price) + Off-site (constructioncoverage, TDPM, ConstructConnect, F6S "AI-Assisted Takeoff" category) | **C1 · Absent** (both runs and fact-check re-run; Togal.AI, STACK, PlanSwift, Beam AI named) |
| E-002 | best construction estimating software for residential contractors | RES | GEN | Tool | High | NEW PAGE NEEDED: residential builders hub | **C2 · Absent** (Clear Estimates, Buildxact, Houzz Pro, Buildertrend, JobTread, QuickBooks) |
| E-003 | AI construction takeoff software | ALL | GEN | Tool | High | [/software/](https://quotr.ai/software/) + Off-site | **C3 · Absent** (10 vendors named, mostly from their homepages) |
| E-004 | construction bid management software for general contractors | GC | GEN | Tool | Med | [/blog/best-ai-bid-software-for-construction/](https://quotr.ai/blog/best-ai-bid-software-for-construction/) (optimize: stale pricing) | **C7 · Absent** (ConstructConnect, BuildingConnected, SmartBid, PlanHub, Procore) |
| E-005 | software for multifamily developers to estimate construction costs | DEV | GEN | Tool | High | NEW PAGE NEEDED: developer hub (today /developers/ only mirrors [/service/](https://quotr.ai/service/)) | **C8 · Absent** (ConstructionOnline, RSMeans, Autodesk Forma, Procore, STACK) |
| E-006 | construction estimating software with material procurement | ALL | SRC | Tool | High | [/blog/takeoff-to-buyout-construction-estimating-procurement-platform/](https://quotr.ai/blog/takeoff-to-buyout-construction-estimating-procurement-platform/) (optimize) + Off-site (G2/Capterra procurement categories) | **C9 · Absent** (reproduced; Buildertrend, Procore, Buildxact, esti-mate, ConWize) |
| E-007 | best AI construction estimating software 2026 | ALL | GEN | Tool | High | [/blog/best-ai-construction-estimating-software-2026/](https://quotr.ai/blog/best-ai-construction-estimating-software-2026/) (optimize) + Off-site | **C11 · Absent** (reproduced; Togal.AI, Handoff, Buildxact, Procore AI, Bluebeam) |
| E-008 | AI estimating software for residential general contractors that goes from plans to proposal | RES | GEN | Tool | High | NEW PAGE NEEDED: residential GC page ("plans → takeoff → proposal → materials") | **C13 · Absent** (Handoff, BuildVision AI, Houzz Pro, Buildxact, Beam; single-session) |
| E-009 | best takeoff and estimating software for Mac users | SUB | GEN | Tool | High | NEW PAGE NEEDED: "Browser-based takeoff for Mac and PC" (browser support needs official confirmation; TO CONFIRM with Quotr) | **C15 · Absent** (STACK, Easy Takeoffs, Square Takeoff, Bluebeam, Buildxact) |
| E-010 | best AI construction takeoff and estimating software in 2026 for residential subcontractors and general contractors | RES, SUB | GEN | Tool | High | Residential hub (E-002) | **S1 · Absent** (Handoff, Buildxact, STACK, Togal.AI) |
| E-011 | best takeoff and estimating software for multifamily developers and residential general contractors 2026 | DEV, RES | GEN | Tool | High | Developer hub (E-005) | **S2 · Absent** (Autodesk Takeoff / Forma Estimate, STACK, PlanSwift, Togal.AI) |
| E-012 | best software for a GC to compare subcontractor and supplier bids / bid leveling for residential | GC, RES | GEN | Tool | High | NEW PAGE NEEDED: bid leveling and supplier-quote comparison page | **S4 · Absent** (Buildertrend, Buildxact, SmartBid, Procore, Contractor Foreman) |
| E-013 | best construction materials procurement software platforms for contractors and builders 2026 | BUY, GC | SRC | Tool | High | [/blog/construction-procurement-software/](https://quotr.ai/blog/construction-procurement-software/) (optimize) + Off-site | **S5 · Absent** (Procore, Archdesk, Trimble Materials, Field Materials AI, Precoro) |
| E-014 | Best AI construction takeoff and estimating tools for residential subcontractors in 2026 | SUB, RES | GEN | Tool | High | Residential hub (E-002) | **O4 · Absent** (Handoff, Buildxact, Togal.AI, STACK, Kreo) |
| E-015 | Best construction material procurement software… factory-direct 2026 | BUY | SRC | Tool | High | [/procurement/](https://quotr.ai/procurement/) + Off-site | **O5 · Absent** ("no single platform explicitly marketed as a factory-direct marketplace") |
| E-016 | best preconstruction software for general contractors 2026 | GC | GEN | Tool | Med | NEW PAGE NEEDED: GC / preconstruction page | Seen: [Meltplan "best preconstruction software for GCs 2026"](https://www.meltplan.com/blogs/best-preconstruction-software-for-general-contractors-2026) cited in bid-leveling answers |
| E-017 | best online takeoff software that runs in a browser with no download | SUB | GEN | Tool | High | Same page as E-009 | Seen: [r/estimators "Recommended takeoff software"](https://www.reddit.com/r/estimators/comments/1okx6vu/recommended_takeoff_software/) (browser users pointed to Zztakeoff) |
| E-018 | best estimating software for small contractors 2026 | SUB, RES | GEN | Tool | Med | [/blog/trade-estimating-software/](https://quotr.ai/blog/trade-estimating-software/) (optimize) | Seen: [r/estimators "looking for takeoff/estimating software"](https://www.reddit.com/r/estimators/comments/1f7gazl/looking_for_takeoffestimating_software/) |
| E-019 | best construction estimating software with a built-in cost database | SUB | GEN | Tool | Med | [/software/](https://quotr.ai/software/) (optimize: explain where zip-code cost data comes from; TO CONFIRM with Quotr) | — |
| E-020 | best software to create construction bid proposals for subcontractors | SUB | GEN | Tool | Med | [/blog/ai-construction-proposals-takeoff-to-proposal/](https://quotr.ai/blog/ai-construction-proposals-takeoff-to-proposal/) | — |
| E-021 | AI tools for preconstruction teams in 2026 | GC | GEN | Tool | Med | [/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/](https://quotr.ai/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/) | — |
| E-022 | best real estate development pro forma software | DEV | GEN | Tool | Med | [/blog/real-estate-pro-forma-software-comparison/](https://quotr.ai/blog/real-estate-pro-forma-software-comparison/) | Seen: WebSearch surfaced this Quotr page (visibility tests §5) |
| E-023 | AI tools for real estate underwriting of construction costs | FUND, DEV | GEN | Tool | Med | [/blog/quotr-developer-desk-underwriting-grade-estimates-72-hours/](https://quotr.ai/blog/quotr-developer-desk-underwriting-grade-estimates-72-hours/) | — |
| E-024 | Revit add-in for cost estimating | ARCH | GEN | Tool | Low | TO CONFIRM with Quotr (Revit add-in status) | — |
| E-025 | AI bidding software for construction 2026 | SUB, GC | GEN | Tool | Med | [/blog/ai-bidding-software-construction/](https://quotr.ai/blog/ai-bidding-software-construction/) (optimize: stale Solo/Team pricing) | — |

### 2.2 Category prompts by trade

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| E-026 | best takeoff software for drywall contractors | SUB | DRY | Tool | High | [/blog/best-drywall-estimating-software-in-2026/](https://quotr.ai/blog/best-drywall-estimating-software-in-2026/) + [/software/trades/drywall/](https://quotr.ai/software/trades/drywall/) (optimize) | **C4 · Absent** (STACK, The EDGE, QuoteIQ, Bluebeam, Houzz Pro, Buildxact, PlanSwift) |
| E-027 | best takeoff software for flooring contractors | SUB | FLR | Tool | High | [/blog/best-flooring-estimating-software-in-2026/](https://quotr.ai/blog/best-flooring-estimating-software-in-2026/) (optimize: stale pricing) | **C5 · Absent** (The EDGE, MeasureSquare, PlanSwift, STACK, Autodesk, QuoteIQ) |
| E-028 | best takeoff software for electrical contractors | SUB | ELEC | Tool | High | [/blog/best-electrical-estimating-software-2026/](https://quotr.ai/blog/best-electrical-estimating-software-2026/) (optimize: stale pricing) | **C6 · Absent** (ConEst IntelliBid, Countfire, PlanSwift, Trimble AccuBid, McCormick; Quotr's post not retrieved) |
| E-029 | best plumbing estimating software 2026 | SUB | PLMB | Tool | Med | [/blog/best-plumbing-estimating-software-2026/](https://quotr.ai/blog/best-plumbing-estimating-software-2026/) | Seen: [YouTube "Best Plumbing Takeoff Software for Contractors"](https://www.youtube.com/watch?v=MAWJZ95NOMk) |
| E-030 | best HVAC estimating software 2026 | SUB | HVAC | Tool | Med | [/blog/hvac-estimating-software-2026-buyers-guide/](https://quotr.ai/blog/hvac-estimating-software-2026-buyers-guide/) | **N3 · Absent** (QuoteIQ, ServiceTitan, FieldPulse, WenDuct named; QuoteIQ's own lists, BuildVision, Software Advice, TDPM, GetApp cited; Quotr's HVAC guide not retrieved) |
| E-031 | best concrete estimating software 2026 | SUB | CONC | Tool | Med | [/blog/best-concrete-estimating-software-2026/](https://quotr.ai/blog/best-concrete-estimating-software-2026/) (optimize: stale pricing) | — |
| E-032 | best framing takeoff software for lumber packages | SUB, RES | FRM | Tool | Med | NEW PAGE NEEDED: framing page (Kreo already has a framing trade page) | — |
| E-033 | best roofing takeoff software for new construction from plans | SUB | ROOF | Tool | Med | NEW PAGE NEEDED (with L-074) | **N4 · Absent** (STACK, Beam AI, On-Screen Takeoff + Quick Bid, Buildxact named; worldmetrics, BuildVision, ibeam.ai, oncenter, zztakeoff cited) |
| E-034 | best painting estimating software for commercial painters | SUB | PNT | Tool | Low | [/software/trades/painting/](https://quotr.ai/software/trades/painting/) (optimize) | — |
| E-035 | best estimating app for tile contractors | SUB | TILE | Tool | Low | [/software/trades/tile/](https://quotr.ai/software/trades/tile/) (optimize) | Seen: [SimplyWise "Best estimating app for tile contractors"](https://www.simplywise.com/blog/best-estimating-app-tile-contractors/) |
| E-036 | best siding estimating software | SUB | SID | Tool | Low | NEW PAGE NEEDED (low) | — |
| E-037 | best door hardware and window takeoff software | SUB | WIN | Tool | Med | [/software/trades/doors-hardware/](https://quotr.ai/software/trades/doors-hardware/) + [/blog/best-glazing-estimating-software-2026/](https://quotr.ai/blog/best-glazing-estimating-software-2026/) (optimize: stale pricing) | — |
| E-038 | best millwork and cabinet estimating software | SUB | CAB | Tool | Low | [/software/trades/millwork/](https://quotr.ai/software/trades/millwork/) (optimize) | — |
| E-039 | best insulation estimating software | SUB | INS | Tool | Low | [/software/trades/insulation/](https://quotr.ai/software/trades/insulation/) (optimize) | — |
| E-040 | best structural steel estimating software 2026 | SUB | GEN | Tool | Low | [/blog/structural-steel-estimating/](https://quotr.ai/blog/structural-steel-estimating/) (optimize: stale pricing) | — |
| E-041 | best rebar takeoff software | SUB | CONC | Tool | Low | [/blog/rebar-estimating-and-takeoff-software/](https://quotr.ai/blog/rebar-estimating-and-takeoff-software/) (optimize: stale pricing) | — |
| E-042 | best MEP estimating software for subcontractors | SUB | HVAC, PLMB, ELEC | Tool | Med | NEW PAGE NEEDED: MEP software page (Quotr's MEP post is about services) | — |

### 2.3 Alternatives prompts

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| E-043 | Togal.AI alternatives | SUB, GC | GEN | Alt | High | [/blog/best-togal-ai-alternatives-2026/](https://quotr.ai/blog/best-togal-ai-alternatives-2026/) (optimize: merge with the near-duplicate /blog/best-togal-ai-alternatives/; fix "from $299.90") + Off-site (G2/Capterra Togal alternatives pages) | **V1 · Named, low** (about 15th of 17 in run 1; 8th of 9 in run 2; single-session) |
| E-044 | PlanSwift alternatives 2026 | SUB | GEN | Alt | High | [/blog/best-planswift-alternatives-2026/](https://quotr.ai/blog/best-planswift-alternatives-2026/) | **V3 · Cited, not named** (used for PlanSwift facts only; single-session) |
| E-045 | best PlanSwift alternatives in 2026 | SUB | GEN | Alt | High | Same as E-044 | **S3 · Cited, not named** |
| E-046 | Bluebeam alternatives for takeoff | SUB, GC | GEN | Alt | High | [/blog/bluebeam-alternative/](https://quotr.ai/blog/bluebeam-alternative/) (optimize: stale pricing) | **V4 · Absent** (Quotr post not retrieved) |
| E-047 | STACK takeoff alternatives for small residential subcontractors | SUB, RES | GEN | Alt | High | [/blog/stack-alternative/](https://quotr.ai/blog/stack-alternative/) (optimize: stale "Solo $299.90" pricing and the "PlanSwift is a Trimble product" error) | **V10 · Retrieved only** |
| E-048 | On-Screen Takeoff alternatives | SUB | GEN | Alt | Med | NEW PAGE NEEDED | Seen: [Easy Takeoffs "best On-Screen Takeoff alternatives"](https://easytakeoffs.com/blog/best-on-screen-takeoff-alternatives) (competitor page) |
| E-049 | Kreo alternatives | SUB | GEN | Alt | Med | NEW PAGE NEEDED (Nomic's Kreo-alternatives list shows Quotr #5 with the stale $299.90 price) | Seen: [nomic.ai Kreo alternatives](https://www.nomic.ai/compare/kreo-alternatives) |
| E-050 | Beam AI alternatives | SUB | GEN | Alt | Med | [/blog/quotr-ai-vs-beam-ai-takeoff-estimating-comparison/](https://quotr.ai/blog/quotr-ai-vs-beam-ai-takeoff-estimating-comparison/) | — |
| E-051 | Handoff alternatives for residential contractors | RES | GEN | Alt | High | NEW PAGE NEEDED (Handoff owns residential answers today) | **N5 · Absent** (Foreman, SimplyWise, Houzz Pro, Buildertrend, Buildxact, JobTread, Jobber, Contractor Foreman named; SimplyWise, Foreman, SourceForge, GetApp, G2, Capterra alternatives pages cited) |
| E-052 | Buildxact alternatives | RES | GEN | Alt | Med | NEW PAGE NEEDED | — |
| E-053 | Excel alternatives for construction estimating | SUB, RES | GEN | Alt | Med | [/blog/quotr-vs-excel/](https://quotr.ai/blog/quotr-vs-excel/) | Seen: [r/estimators "looking for takeoff/estimating software"](https://www.reddit.com/r/estimators/comments/1f7gazl/looking_for_takeoffestimating_software/) (BidScreen XL suggested for Excel users) |
| E-054 | cheapest AI takeoff software | SUB, RES | GEN | Alt | High | [/pricing/](https://quotr.ai/pricing/) (optimize: add Offer schema and a plain price table) + Off-site | **V7 · Absent** (Kreo ~$35, Easy Takeoffs $39, Pilars, QuoteIQ $29.99; Quotr Lite $79.90 not named) |
| E-055 | AI takeoff software with free trial | SUB | GEN | Alt | High | [/pricing/](https://quotr.ai/pricing/) + [/software/](https://quotr.ai/software/) (7-day trial) | **V8 · Absent** |
| E-056 | free construction takeoff software | SUB, RES | GEN | Tool | Med | [/pricing/](https://quotr.ai/pricing/) (Quotr has a trial, not a free plan; be honest) | Seen: STACK ranks with a free-software post ([stackct.com](https://www.stackct.com/blog/free-construction-cost-estimating-software/)) |

### 2.4 Head-to-head prompts (competitors only)

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| E-057 | Kreo vs Togal | SUB | GEN | VS | Med | NEW PAGE NEEDED: neutral AI takeoff comparison table (Kreo, Togal, Beam, Quotr) | **V5 · Absent** (only the two brands discussed) |
| E-058 | STACK vs PlanSwift | SUB | GEN | VS | Low | [/blog/quotr-ai-vs-stack-browser-first-takeoff-procurement/](https://quotr.ai/blog/quotr-ai-vs-stack-browser-first-takeoff-procurement/) (partial fit) | **V6 · Absent** (only the two brands) |
| E-059 | Beam AI vs Togal AI vs Kreo which is best for residential estimating | RES, SUB | GEN | VS | High | NEW PAGE NEEDED: residential AI takeoff comparison | **V9 · Absent** (engine confused Beam AI with trybeam.com) |
| E-060 | Handoff vs Buildxact for residential estimating | RES | GEN | VS | Med | NEW PAGE NEEDED | — |
| E-061 | Togal vs Beam AI | SUB | GEN | VS | Med | [/blog/quotr-ai-vs-beam-ai-takeoff-estimating-comparison/](https://quotr.ai/blog/quotr-ai-vs-beam-ai-takeoff-estimating-comparison/) | — |
| E-062 | Bluebeam vs PlanSwift for takeoff | SUB | GEN | VS | Low | [/blog/bluebeam-alternative/](https://quotr.ai/blog/bluebeam-alternative/) | Seen: [r/estimators "Bluebeam vs other estimating softwares"](https://www.reddit.com/r/estimators/comments/1ekpil5/bluebeam_vs_other_estimating_softwares/) |

### 2.5 Feature and fit prompts (unbranded)

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| E-063 | which AI takeoff tools work on residential plans | RES, SUB | GEN | Tool | High | Residential hub (E-002) | — |
| E-064 | AI takeoff tool that shows confidence scores so I can review counts | SUB | GEN | Tool | Med | [/software/](https://quotr.ai/software/) (optimize: name and explain "Smart Matching"; name TO CONFIRM with Quotr) | — |
| E-065 | estimating software that uses local material prices by zip code | SUB, RES | GEN | Tool | Med | [/software/](https://quotr.ai/software/) (optimize) | — |
| E-066 | software that goes from takeoff all the way to purchase order | GC, RES, DEV | SRC | Tool | High | [/blog/takeoff-to-buyout-construction-estimating-procurement-platform/](https://quotr.ai/blog/takeoff-to-buyout-construction-estimating-procurement-platform/) and [/blog/the-takeoff-to-transaction-gap/](https://quotr.ai/blog/the-takeoff-to-transaction-gap/) | — |
| E-067 | software to compare supplier quotes for construction materials | SUB, BUY | SRC | Tool | High | [/software/](https://quotr.ai/software/) (optimize: bid-comparison section) + E-012 page | — |
| E-068 | can I export an AI takeoff to Excel | SUB | GEN | Fit | Med | [/faq/](https://quotr.ai/faq/) (TO CONFIRM with Quotr: export formats) | — |
| E-069 | is there a ChatGPT for blueprints | SUB, GC | GEN | Tool | High | [/blog/ai-that-reads-construction-drawings-chat-with-blueprints/](https://quotr.ai/blog/ai-that-reads-construction-drawings-chat-with-blueprints/) | — |
| E-070 | AI takeoff software that handles metric and imperial | SUB | GEN | Fit | Low | [/blog/metric-imperial-construction-takeoff/](https://quotr.ai/blog/metric-imperial-construction-takeoff/) | — |
| E-071 | does AI estimating software train on my drawings, is my bid data secure | GC, SUB | GEN | Trust | Med | NEW PAGE NEEDED: security and data page (TO CONFIRM with Quotr: SOC 2, data use) | Contractors' top AI worries: accuracy 57%, security 54% (Dodge/CMiC, playbook §6) |
| E-072 | AI plans-to-estimate software that turns drawings into prices in minutes | SUB, RES | GEN | Tool | Med | [/blog/ai-construction-estimating-software-that-turns-plans-into-prices-in-minutes/](https://quotr.ai/blog/ai-construction-estimating-software-that-turns-plans-into-prices-in-minutes/) and [/blog/blueprint-to-priced-estimate-workflow/](https://quotr.ai/blog/blueprint-to-priced-estimate-workflow/) | — |

### 2.6 Services and procurement comparisons

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| E-073 | outsourced construction estimating service price per square foot for developers | SVC, DEV | GEN | Service | High | [/blog/outsource-construction-estimating/](https://quotr.ai/blog/outsource-construction-estimating/) (optimize: brand-attributed price sentence) + [/pricing/](https://quotr.ai/pricing/) | **C12 · Cited, not named** (first citation; rates credited to "some firms"; reproduced) |
| E-074 | how much does it cost to outsource a quantity takeoff | SVC, SUB | GEN | Cost | High | [/blog/quantity-takeoff-services/](https://quotr.ai/blog/quantity-takeoff-services/) | **S9 · Cited** ($0.03–$0.10/sq ft and $250–$2,500 per estimate quoted; naming not recorded) |
| E-075 | best construction estimating services in California | SVC | GEN | Service | High | [/blog/construction-estimating-services-california/](https://quotr.ai/blog/construction-estimating-services-california/) | — |
| E-076 | MEP estimating services cost | SVC, GC | HVAC, PLMB, ELEC | Service | High | [/blog/mep-estimating-services/](https://quotr.ai/blog/mep-estimating-services/) | — |
| E-077 | HVAC estimating services for contractors | SVC | HVAC | Service | Med | [/blog/hvac-estimating-services/](https://quotr.ai/blog/hvac-estimating-services/) | — |
| E-078 | electrical takeoff services near me | SVC | ELEC | Service | Med | [/blog/electrical-estimating-services/](https://quotr.ai/blog/electrical-estimating-services/) | — |
| E-079 | preconstruction estimating services for general contractors | GC, SVC | GEN | Service | High | [/blog/preconstruction-services/](https://quotr.ai/blog/preconstruction-services/) and [/blog/precon-on-demand-outsource-bid-cost-estimation/](https://quotr.ai/blog/precon-on-demand-outsource-bid-cost-estimation/) | — |
| E-080 | commercial construction estimating services cost | SVC, GC | GEN | Service | Med | [/blog/commercial-estimating-services/](https://quotr.ai/blog/commercial-estimating-services/) (consolidate with overlapping service posts) | Cited in C12 |
| E-081 | buy construction materials direct from factories overseas platform | BUY | SRC | Buy | High | [/procurement/](https://quotr.ai/procurement/) + [/blog/ddp-construction-materials/](https://quotr.ai/blog/ddp-construction-materials/) | **C10 · Retrieved only** (DDP post in sources, not used; Alibaba, Port2Site and others named) |
| E-082 | where can US contractors buy cabinets, windows and flooring factory direct at wholesale prices | BUY, RES | SRC | Buy | High | [/procurement/](https://quotr.ai/procurement/) (optimize: use plain buyer wording, name the categories, add prices) | **C14 · Absent** (local "factory direct" dealers such as Build Source named) |
| E-083 | where can home builders and multifamily developers buy building materials factory-direct from overseas manufacturers with AI takeoff and procurement | DEV, RES | SRC | Buy | High | [/blog/how-developers-source-building-materials/](https://quotr.ai/blog/how-developers-source-building-materials/) | **S6 · Named** (1st in original run, 3rd of 6 on re-run; prompt echoes Quotr's own wording) |
| E-084 | sourcing agent vs procurement platform for importing building materials | BUY, DEV | SRC | VS | Med | NEW PAGE NEEDED | — |
| E-085 | Alibaba vs sourcing agent vs managed procurement for construction materials | BUY, RES | SRC | VS | High | NEW PAGE NEEDED (honest comparison of the three routes) | Alibaba named in C10 |
| E-086 | third-party construction cost review for lenders | FUND | GEN | Service | Med | NEW PAGE NEEDED: service page for funds and lenders | — |
| E-087 | who can do a fast construction cost estimate for a land deal | DEV | GEN | Service | High | [/service/](https://quotr.ai/service/) (optimize: developer wording) + [/blog/quotr-developer-desk-underwriting-grade-estimates-72-hours/](https://quotr.ai/blog/quotr-developer-desk-underwriting-grade-estimates-72-hours/) | — |
| E-088 | are AI-assisted estimating services accurate | SVC, DEV | GEN | Trust | Med | [/service/](https://quotr.ai/service/) (optimize: method and QA page) | — |

---

## Stage 3 — Decide / brand (bottom of funnel)

Brand answers are mostly built from Quotr's own pages (about 60–70% self-sourced), so engines hedge ("not independently validated"). **5 of 8** brand prompts had accuracy problems in September 2026: the unrelated Quotr Pro app's ratings used as Quotr's, stale "from $299.90" pricing (the real entry price is Lite at $79.90 per seat per month), namesake apps, and a funding conflict (<../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>, §4; <../../research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>). Canonical facts: [../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md).

### 3.1 Brand facts

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| D-001 | What is Quotr.ai? | ALL | GEN | Brand | High | [/disambiguation/](https://quotr.ai/disambiguation/) + [/about-us/](https://quotr.ai/about-us/) | **B1 · Named, accurate** (both runs) |
| D-002 | What is Quotr? | ALL | GEN | Brand | High | [/disambiguation/](https://quotr.ai/disambiguation/) | **O2 · Named after namesakes** ("the most likely match is Quotr.ai") |
| D-003 | Quotr app | ALL | GEN | Brand | High | [/disambiguation/](https://quotr.ai/disambiguation/) | **B5 · Named, 3rd of 4 "Quotr" apps** |
| D-004 | Quotr construction software funding founders | ALL | GEN | Brand | Med | [/about-us/](https://quotr.ai/about-us/) (optimize: add founding year, HQ, funding; all TO CONFIRM with Quotr) | **B6 · Named, funding conflict** ($3.5M seed vs a Perplexity-only "$190K" figure) |
| D-005 | who owns Quotr.ai / what is FLOZ Inc | ALL | GEN | Brand | Med | [/about-us/](https://quotr.ai/about-us/) (optimize) | — |
| D-006 | is Quotr.io the same company as Quotr.ai | ALL | GEN | Brand | High | [/disambiguation/](https://quotr.ai/disambiguation/) (optimize: add a dated rename line; date TO CONFIRM with Quotr) | Legacy quotr.io and test.quotr.io still appear in AI citations (B2) |
| D-007 | where is Quotr.ai headquartered | ALL | GEN | Brand | Med | [/about-us/](https://quotr.ai/about-us/) (HQ TO CONFIRM with Quotr: Berkeley vs San Francisco) | — |

### 3.2 Pricing

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| D-008 | Quotr.ai pricing | ALL | GEN | Price | High | [/pricing/](https://quotr.ai/pricing/) | **B2 · Named, accurate** (flags legacy Solo/Team tiers; cites the staging host test.quotr.io; reproduced) |
| D-009 | how much does Quotr cost per user per month | SUB, GC | GEN | Price | High | [/pricing/](https://quotr.ai/pricing/) | — |
| D-010 | does Quotr.ai have a free trial | SUB | GEN | Price | High | [/pricing/](https://quotr.ai/pricing/) (7-day free trial) | — |
| D-011 | Quotr Lite vs Plus, what is the difference | SUB | GEN | Price | High | [/pricing/](https://quotr.ai/pricing/) (optimize: explain Plus "takeoff credits"; TO CONFIRM with Quotr) | — |
| D-012 | how much does Quotr's estimating service cost per square foot | DEV, SVC | GEN | Price | High | [/pricing/](https://quotr.ai/pricing/) + [/service/](https://quotr.ai/service/) | — |
| D-013 | does Quotr.ai offer annual pricing | SUB, GC | GEN | Price | Med | [/pricing/](https://quotr.ai/pricing/) (TO CONFIRM with Quotr) | — |

### 3.3 Trust, reviews and accuracy

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| D-014 | Is Quotr.ai legit? Quotr reviews | ALL | GEN | Trust | High | Off-site (G2/Capterra reviews under "Quotr.ai") + [/case-studies/](https://quotr.ai/case-studies/) (optimize) + NEW PAGE NEEDED: customer-reviews hub | **B3 · Named, mixed up with Quotr Pro app** (borrowed its 37 ratings / 4.7; reproduced) |
| D-015 | What is Quotr.ai? Is it legit? reviews | ALL | GEN | Trust | High | Same as D-014 | **O1 · Named** ("I did not find independent third-party reviews") |
| D-016 | Quotr.ai G2 reviews | ALL | GEN | Trust | High | Off-site: G2 profile (status TO CONFIRM with Quotr; G2 blocked checks) | Site-restricted search found no Quotr G2 page (visibility tests §4) |
| D-017 | who uses Quotr.ai, case studies | ALL | GEN | Trust | High | [/case-studies/](https://quotr.ai/case-studies/) (optimize: add numbers) + [/case-studies/rl-electric/](https://quotr.ai/case-studies/rl-electric/) | — |
| D-018 | Which third-party articles or review sites mention Quotr | ALL | GEN | Trust | Med | Off-site | **O6 · Inventory prompt** (found only F6S and Nomic; everything else was Quotr's own site, app-store pages or namesakes) |
| D-019 | how accurate is Quotr's AI takeoff | SUB, GC | GEN | Trust | High | NEW PAGE NEEDED: accuracy method page (the "95–99% on clean vector PDFs" claim is self-reported with no method) | Both B3 runs flagged Quotr's accuracy claims as self-published |
| D-020 | is Quotr Pro the same as Quotr.ai | ALL | GEN | Brand | High | [/disambiguation/](https://quotr.ai/disambiguation/) | Quotr Pro (a different developer, quotr.pro) is conflated in B3 |

### 3.4 Quotr vs a named competitor

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| D-021 | Togal vs Quotr | SUB, GC | GEN | VS | High | [/blog/quotr-vs-togal-ai-comparison-2026/](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/) (optimize: state the current Quotr price) | **V2 · Named** (positioning accurate; price stated as "$299.90 Solo / $499.90 Team", which is stale) |
| D-022 | Quotr.ai vs Togal.AI | SUB, GC | GEN | VS | High | Same as D-021 | **B4 · Named** (stale "from $299.90"; reproduced) |
| D-023 | Quotr alternatives | ALL | GEN | Alt | High | NEW PAGE NEEDED: honest "Quotr alternatives and when to choose them" page | **B7 · Named** ("the most end-to-end option"; about 10 of 18 citations were Quotr's own) |
| D-024 | Quotr.ai vs Togal.AI vs Beam AI vs Kreo | SUB | GEN | VS | High | NEW PAGE NEEDED: honest four-way comparison (with E-057) | **S7 · Named** ("most all-in-one"; mostly Quotr's own blog cited) |
| D-025 | Quotr.ai vs Togal.AI vs Beam AI | SUB | GEN | VS | High | Same as D-024 | **O3 · Named** ("if you want takeoff plus estimating, proposals, and procurement in one workflow") |
| D-026 | Quotr vs STACK | SUB, GC | GEN | VS | High | [/blog/quotr-ai-vs-stack-browser-first-takeoff-procurement/](https://quotr.ai/blog/quotr-ai-vs-stack-browser-first-takeoff-procurement/) | — |
| D-027 | Quotr vs PlanSwift | SUB | GEN | VS | High | [/blog/quotr-ai-vs-planswift-ai-takeoff-procurement-comparison-2026/](https://quotr.ai/blog/quotr-ai-vs-planswift-ai-takeoff-procurement-comparison-2026/) | — |
| D-028 | Quotr vs Beam AI | SUB | GEN | VS | Med | [/blog/quotr-ai-vs-beam-ai-takeoff-estimating-comparison/](https://quotr.ai/blog/quotr-ai-vs-beam-ai-takeoff-estimating-comparison/) | — |
| D-029 | Quotr vs Handoff for residential builders | RES | GEN | VS | High | NEW PAGE NEEDED | — |
| D-030 | Quotr vs Buildxact | RES | GEN | VS | Med | NEW PAGE NEEDED | — |
| D-031 | Quotr vs Kreo | SUB | GEN | VS | Med | NEW PAGE NEEDED | — |
| D-032 | Quotr vs Bluebeam | SUB, GC | GEN | VS | Med | [/blog/bluebeam-alternative/](https://quotr.ai/blog/bluebeam-alternative/) | — |
| D-033 | Quotr vs Excel for estimating | SUB, RES | GEN | VS | Low | [/blog/quotr-vs-excel/](https://quotr.ai/blog/quotr-vs-excel/) | — |

### 3.5 Product fit and how to use it

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| D-034 | does Quotr.ai work for electrical, HVAC and other specialty trades | SUB | ELEC, HVAC | Fit | High | [/software/](https://quotr.ai/software/) (live FAQ answers this) + trade pages | — |
| D-035 | does Quotr work on Mac | SUB | GEN | Fit | High | [/software/](https://quotr.ai/software/) (TO CONFIRM with Quotr: official browser/Mac statement) | — |
| D-036 | what file types does Quotr.ai accept (PDF, DWG, Revit) | SUB, ARCH | GEN | Fit | Med | [/faq/](https://quotr.ai/faq/) (TO CONFIRM with Quotr) | — |
| D-037 | does Quotr integrate with Procore or QuickBooks | GC, SUB | GEN | Fit | Med | NEW PAGE NEEDED: integrations page (TO CONFIRM with Quotr) | — |
| D-038 | how do I export a proposal from Quotr | SUB | GEN | Fit | Low | [/tutorials/](https://quotr.ai/tutorials/) | — |
| D-039 | is procurement required to use Quotr.ai | SUB | GEN | Fit | Med | [/software/](https://quotr.ai/software/) (live FAQ: "No. Procurement is fully optional") | — |
| D-040 | how much time and money will Quotr save my estimating team | SUB, GC | GEN | Fit | Med | [/roi-calculator/](https://quotr.ai/roi-calculator/) | — |
| D-041 | Quotr.ai software demo | ALL | GEN | Fit | Low | [/tutorials/](https://quotr.ai/tutorials/) + [/book-demo](https://quotr.ai/book-demo) | — |

### 3.6 Quotr Procurement and Quotr Service specifics

| # | Prompt | Persona | Trade | Intent | Pri | Quotr page that should answer it | Tested / seen |
|---|---|---|---|---|---|---|---|
| D-042 | how does Quotr procurement work and what is included in the DDP price | BUY, DEV | SRC | Buy | High | [/procurement/](https://quotr.ai/procurement/) | — |
| D-043 | what materials can I buy through Quotr procurement | BUY, RES, DEV | SRC | Buy | High | [/procurement/](https://quotr.ai/procurement/) (category list TO CONFIRM with Quotr) | — |
| D-044 | does Quotr procurement deliver outside California | BUY, DEV | SRC | Buy | High | [/procurement/](https://quotr.ai/procurement/) (conflicting copy; TO CONFIRM with Quotr) | — |
| D-045 | how many factories does Quotr work with | BUY | SRC | Brand | Med | [/procurement/](https://quotr.ai/procurement/) (50+ vs 220+ vs 30+ on Quotr's own pages; TO CONFIRM with Quotr) | Perplexity already reports the conflict |
| D-046 | how long does Quotr take to deliver a cost estimate | DEV, SVC | GEN | Service | High | [/service/](https://quotr.ai/service/) (turnaround conflicts: 24 hours to 5–7 days; TO CONFIRM with Quotr) | — |
| D-047 | Quotr sample estimate deliverable | DEV, SVC | GEN | Service | Med | [/service/](https://quotr.ai/service/) (9 sample deliverables) | — |
| D-048 | Quotr procurement project examples and savings | DEV, BUY | SRC | Trust | High | [/procurement/](https://quotr.ai/procurement/) (optimize: fix the "Client saved ~$0" display bug) | — |

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

Many "NEW PAGE NEEDED" rows point to the same page. Grouped, the library calls for about 25 new assets. The order below follows the white-space evidence (<../../research_notes/Quotr GEO AEO strategy audit/competitor_geo_benchmark.md>, §5); final priorities belong in [../05-content-strategy/content-priorities.md](../05-content-strategy/content-priorities.md).

| New asset | Prompts it answers | Why |
|---|---|---|
| Landed-cost and tariff hub for residential finish materials (cabinet/vanity tariff explainer, landed-cost calculator, lead-time tracker, certification FAQ, honest "is importing worth it") | L-065, L-082, L-083, L-087, L-090, L-101, L-109, L-112, L-114–L-121, E-084, E-085 | No software vendor is cited on these questions today; fits Quotr Procurement |
| Residential builders hub + residential GC page (plans → takeoff → proposal → materials) | E-002, E-008, E-010, E-014, E-063, E-051, E-059 | Handoff and Buildxact own residential answers; Quotr is absent from all of them |
| Developer hub + multifamily cost benchmark + ADU/LA rebuild/California $/sq ft pages | L-129–L-134, L-136, L-137, L-139, L-142, E-005, E-011 | Meltplan/Exayard cost pages get cited next to RSMeans; Quotr has service data but no benchmark |
| Bid-leveling guide + free template + bid/supplier-quote comparison page | L-014, L-015, E-012, E-067 | Answers name Buildertrend/Buildxact/SmartBid with thin content |
| Estimating time benchmark (by project size, from Quotr Service jobs) + AI takeoff accuracy method page | L-006, L-007, L-040, L-046, D-019 | Original data is the most citable format; accuracy is buyers' #1 AI worry |
| Free trade calculators (drywall, flooring waste, tile, concrete, framing) | L-047, L-048, L-055, L-057, L-062, L-069 | Calculators won the drywall how-to (P2) for three software vendors |
| Residential trade-cost benchmarks (electrical, plumbing, HVAC, insulation per sq ft / per fixture / per ton) | L-093, L-098, L-100, L-104, L-106 | Answers today come from HomeGuide, Angi, Fixr-type sites |
| Trade guides where Quotr has no content: roofing from plans, siding, framing/lumber, drywall pricing, concrete pricing | L-049, L-050, L-052, L-054, L-070, L-074, L-077, E-032, E-033 | Roofing has only a thin trade page; siding has none |
| Browser/Mac page | E-009, E-017 | Quotr is browser-based but absent from Mac prompts |
| Honest comparison pages: Quotr alternatives; Quotr vs Handoff, Buildxact, Kreo; four-way AI takeoff table; On-Screen Takeoff, Kreo, Handoff, Buildxact alternatives | D-023, D-024, D-029–D-031, E-048, E-049, E-051, E-052, E-057, E-060 | Missing head-to-heads with named rivals (onsite audit §6) |
| Customer reviews hub, security page, integrations page | D-014, D-037, E-071 | Trust prompts fail today; facts TO CONFIRM with Quotr |
| Estimating basics: Estimating 101 hub, plan-reading guide, overhead and profit guide, RFQ how-to, value engineering, lender budget review, hard vs soft costs | L-002, L-003, L-027, L-127, L-135, L-140, L-141 | Lower priority; mostly definitional |

---

## Related pages

- [tracking-set.md](tracking-set.md) — the ~50 prompts to re-run every month, with baselines and instructions
- [buyer-questions-by-trade.md](buyer-questions-by-trade.md) — the real questions behind these prompts, with source links
- [construction-glossary.md](construction-glossary.md) — plain-English definitions of the terms used in these prompts
- [../02-current-state/ai-visibility-baseline.md](../02-current-state/ai-visibility-baseline.md) — full September 2026 test results
- [../00-quotr/audiences-and-personas.md](../00-quotr/audiences-and-personas.md) — persona profiles
- [../03-market/white-space.md](../03-market/white-space.md) — where Quotr can win
- [../05-content-strategy/content-priorities.md](../05-content-strategy/content-priorities.md) — what to build first
- [../06-playbooks/page-refresh-checklist.md](../06-playbooks/page-refresh-checklist.md) — how to fix the "(optimize)" pages
