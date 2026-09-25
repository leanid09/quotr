---
type: baseline
description: The September 2026 Perplexity test, prompt by prompt, with the method to repeat it.
aliases:
- Baseline
last_verified: 2026-09-25
verify_every_days: 30
---
# Quotr AI Visibility Baseline (Perplexity Tests, September 2026)

> [!abstract] What this page is for
> The dated record of whether AI answer engines mention, cite or recommend Quotr.ai when buyers ask questions, prompt by prompt. It includes the exact method, so the test can be repeated next month and compared like for like.
>
> *All tests were run on 2026-09-25.*

> [!info]- Sources
> Research notes [[quotr_ai_visibility_tests]] (main source: 40 prompts, 45 runs), [[verification_quotr_and_competitors]] (independent re-runs; its corrections override the other notes), [[competitor_geo_benchmark]] and [[quotr_offsite_presence]] (supplementary prompts). Measurement caveats from [[verification_geo_evidence]].

---

## Words used on this page

- **Prompt:** the question typed into the AI tool.
- **Named / mentioned:** the answer text says "Quotr" or "Quotr.ai".
- **Cited:** a quotr.ai page is used as a source link for something in the answer.
- **Retrieved:** a quotr.ai page appears in the answer's list of sources, but the answer does not actually use it.
- **Position:** where Quotr appears among all brands named, counted in order of first mention.
- **Share of voice (SOV):** Quotr's share of all brand mentions across a set of answers.
- **Unbranded prompt:** does not name Quotr. **Brand prompt:** names Quotr.
- **Categories:** **C** = category discovery ("best X software"), **V** = comparison / alternatives, **P** = problem / how-to (top-of-funnel education), **B** = brand.

---

## Headline results

| Metric (Perplexity Sonar, 2026-09-25) | Result |
|---|---|
| Unbranded prompts where Quotr is **named** | **1 of 32 (3.1%)** — only "Togal.AI alternatives", and low in the list |
| Unbranded prompts where a quotr.ai page is **cited in the answer** | **4 of 32 (12.5%)** |
| Unbranded prompts where a quotr.ai page is **in the source list** | **6 of 32 (18.8%)** |
| Category discovery prompts where Quotr is named | **0 of 15** |
| How-to prompts where Quotr is named | **0 of 8** |
| Brand prompts where Quotr is named | 8 of 8, but **5 of 8 had accuracy problems** |
| Quotr share of voice (unbranded) | **about 0.7%** (vs about 6.5% each for STACK, PlanSwift, Buildxact) |
| quotr.ai rank among most-cited domains | Tied 15th (in 6 of 32 prompts), level with reddit.com, kreo.net, getapp.com, projul.com |

**In plain words:** AI engines can find and read Quotr's pages, and sometimes use them as a source. But they almost never recommend Quotr by name when a buyer asks an open question. When Quotr's page is the only source for a fact, the engine often hides the brand ("one outsourced estimating service charges…"). The missing piece is **third-party corroboration**, not more retrieval.

---

## 1. Method (repeat this exactly next month)

### Engine and tool

- **Engine:** Perplexity, via the `mcp__Slashy__web_search` tool. Every response reported `"model": "sonar"`. This is Perplexity's **Sonar API model**, not the consumer Perplexity Pro app.
- **Not tested:** ChatGPT, Google AI Overviews / AI Mode, Gemini, Claude, Copilot. They could not be queried from the research environment. **Treat every result here as a Perplexity proxy only.**
- **Traditional-search cross-check:** 6 prompts were also run through a web search tool (as a stand-in for classic search), plus 4 site-restricted searches to see whether Quotr appears on the most-cited domains.

### Prompt set

- **40 unique prompts**, typed verbatim (exact wording in the table below):
  - 15 category discovery (C1–C15)
  - 10 comparison / alternatives (V1–V10)
  - 8 problem / how-to (P1–P8)
  - 7 brand (B1–B7)
- V2 ("Togal vs Quotr") names Quotr, so it is scored with the brand prompts. That leaves **32 unbranded prompts** (C1–C15, V1, V3–V10, P1–P8) and **8 brand prompts** (B1–B7 + V2).
- **Re-runs in the original session:** C1, V1, V3, B1, B3 were each run a second time (45 Perplexity runs in total).
- **Independent re-runs (fact-check, same day):** 9 original prompts plus 1 new top-of-funnel prompt were re-run by a separate researcher. 4 more re-runs (V1, V3, C13, P5) were refused by a permission filter and not retried, so **V1, V3, C13 and P5 results are single-session only**.

### Scoring rules

1. Use the **first run** of each prompt for the tables and rates.
2. **Named** = Quotr appears in the answer text. **Cited** = a quotr.ai URL is used as an inline citation. **Retrieved** = a quotr.ai URL is in the citation list but not referenced.
3. **Position** = order of first mention among all brands in the answer.
4. **Share of voice:** count each brand **once per prompt** when it is named in the answer text (including when it is the subject of the prompt). Add up all brand mentions across the 32 unbranded prompts (about 153 at baseline). SOV = a brand's count ÷ total. Counts were hand-tallied (±1 per brand).
5. **Cited domains:** list the main domains in each answer's citation array. A domain counts once per prompt.

### How to repeat it next month

1. Use the same tool and model if possible, and write down the model name the tool reports.
2. Paste each prompt **exactly** as written in the table below. Do not add context.
3. Save the full answer text and the full citation list for every prompt (a spreadsheet row per prompt).
4. Run each prompt **twice**. Research showed the source list tends to stay the same day-to-day, but the order of brands changes, so position is noisy.
5. Score with the rules above. Compare against the baseline tables on this page.
6. Add other engines (ChatGPT with search, Google AI Overviews / AI Mode, Gemini, Claude, Copilot) when you can, using logged-out or fresh sessions. Record them as separate columns. Do not mix them into the Perplexity baseline numbers.
7. Add first-party data where Quotr has access: Google Search Console's **Generative AI performance reports** (announced June 3, 2026; available to all sites worldwide since Aug 31, 2026: impressions in AI Overviews and AI Mode by page, country and date; no clicks, CTR or queries), and Bing Webmaster Tools' **AI Performance** report (Copilot citations; launched Feb 10, 2026 and still a public preview). Source: [[verification_geo_evidence]] (M1 and claim 3).
8. Keep the prompt list stable. Add new prompts as a separate "added" block so the core 40 stay comparable. The tracked set lives in [[Tracking set]]; tooling options are in [[Tracking setup]].

---

## 2. Full per-prompt results (Perplexity Sonar, 2026-09-25, first run unless noted)

Each row is a test-run note in the `07-measurement/test-runs` folder; open one to see every brand named (in order), all cited domains and the fact-check detail. "Competitors named" is in the order the answer named them. "Cited domains" are the main domains in the citation list. "Fact-check re-run" shows whether the independent re-run gave the same result.

![[Test runs.base#Sept 2026 core 40]]

### 2a. Supplementary prompts (single runs from other research notes, same day)

These are not part of the 40-prompt baseline rates. Keep them as extra tracking prompts.

![[Test runs.base#Sept 2026 supplementary]]

---

## 3. Mention rates by category (Perplexity, first runs)

| Category | Prompts | Quotr named | quotr.ai cited in answer text | quotr.ai in citation list (incl. retrieved-only) |
|---|---|---|---|---|
| Category discovery (C1–C15) | 15 | 0 (0%) | 1 (C12) | 2 (C10, C12) |
| Comparison / alternatives, unbranded (V1, V3–V10) | 9 | 1 (11%, V1) | 2 (V1, V3) | 3 (V1, V3, V10) |
| Problem / how-to (P1–P8) | 8 | 0 (0%) | 1 (P5) | 1 (P5) |
| **All unbranded** | **32** | **1 (3.1%)** | **4 (12.5%)** | **6 (18.8%)** |
| Brand prompts (B1–B7 + V2) | 8 | 8 (100%) | 8 | 8 — accuracy problems in 5: B3 (Quotr Pro mix-up), B4 and V2 (stale pricing), B5 (namesakes), B6 (funding conflict) |

---

## 4. Share of voice vs competitors (32 unbranded prompts)

Each brand counted once per prompt when named in the answer text. Total brand mentions: about 153.

| Brand | Prompts named in | SOV (of ~153) |
|---|---|---|
| STACK | 10 (C1, C4, C5, C8, C15, V1, V3, V4, V6, V10) | ~6.5% |
| PlanSwift | 10 (C1, C4, C5, C6, V1, V3, V4, V6, V8, V10) | ~6.5% |
| Buildxact | 10 (C2, C4, C9, C11, C13, C15, V1, V4, V8, V10) | ~6.5% |
| Togal.AI | 8 (C1, C3, C11, V1, V3, V4, V5, V9) | ~5.2% |
| Procore | 7 (C3, C7, C8, C9, C11, V1, V3) | ~4.6% |
| Bluebeam | 7 (C4, C11, C15, V1, V3, V4, V10) | ~4.6% |
| Kreo | 7 (C3, V1, V3, V5, V7, V8, V9) | ~4.6% |
| Beam AI (ibeam / Attentive; incl. trybeam mix-up) | 5 (C1, C3, C13, V1, V9) | ~3.3% |
| Houzz Pro | 5 (C2, C4, C8, C13, V1) | ~3.3% |
| On-Screen Takeoff / On Center | 5 (C5, V1, V3, V4, V8) | ~3.3% |
| Autodesk (Takeoff / Forma / BuildingConnected) | 5 (C5, C7, C8, V1, V3) | ~3.3% |
| Easy Takeoffs | 5 (C15, V3, V4, V7, V10) | ~3.3% |
| eTakeoff | 4 (C3, V3, V8, V10) | ~2.6% |
| Buildertrend, QuoteIQ, BuildVision AI | 3 each | ~2.0% each |
| Handoff, The EDGE, Groundplan, Countfire, Square Takeoff | 2 each | ~1.3% each |
| **Quotr.ai** | **1 (V1)** | **~0.7%** |

Competitor profiles: [[Competitor landscape]].

---

## 5. Most-cited domains (the sources AI engines lean on)

Number of the 32 unbranded prompts whose citation list contains the domain.

| Rank | Domain | Prompts | Page type |
|---|---|---|---|
| 1 | capterra.com (+ .in / .co.uk / .ca) | 9 | Review directory; alternatives and compare pages |
| 2 | g2.com (+ learn.g2.com) | 9 | Review directory; alternatives and compare pages |
| 3 | sourceforge.net (+ slashdot.org, 3) | 8 | Directory; alternatives and compare pages |
| 4 | buildvisionai.com | 8 | Competitor: listicle, calculators, feature pages |
| 5 | procore.com | 8 | Vendor: library, calculators, product pages |
| 6 | constructioncoverage.com | 7 | Independent listicle ("takeoff software", "estimating software") |
| 7 | constructconnect.com | 7 | Vendor-network blog ("Top players in 2026" guide) |
| 8 | softwareadvice.com | 7 | Review directory (owned by G2 since the Capterra/GetApp/Software Advice deal announced Jan 2026) |
| 9 | easytakeoffs.com | 7 | Competitor: alternatives posts, calculators |
| 10 | ibeam.ai | 7 | Competitor: homepage, trade pages, vs-pages |
| 11 | stackct.com | 7 | Competitor: trade landing pages |
| 12 | buildxact.com | 7 | Competitor: trade landing pages and blog |
| 13 | autodesk.com / construction.autodesk.com | 7 | Vendor blog and workflow guides |
| 14 | gitnux.org / worldmetrics.org / zipdo.co | 7 (combined) | Low-quality, AI-generated "best X" list farms |
| 15 | thedigitalprojectmanager.com | 6 | Independent listicle ("10 Best AI Estimating Software") |
| =15 | getapp.com, projul.com, reddit.com (r/estimators), kreo.net, **quotr.ai** | 6 each | Directory / competitor blog / forum / vendor / Quotr's own blog |

**Patterns observed:**
- **Alternatives and comparison prompts** draw mainly on review-directory alternatives pages (G2, Capterra, GetApp, SourceForge, SelectHub, SoftwareSuggest) and competitor-owned "alternatives" posts.
- **Category prompts** draw on independent or semi-independent listicles (Construction Coverage, TDPM, Construction Placements, Dan Cumberland Labs, ContraVault) plus competitor listicles and trade pages.
- **How-to prompts** draw on calculators, vendor guides and estimating-service FAQs. How-to answers rarely name any software brand.
- **Reddit r/estimators** appeared in 6 prompts. **YouTube was never cited** in any of the 45 runs. Trade press was cited only rarely.

### Recurring third-party pages (where Quotr most needs to appear)

| Page | Cited in |
|---|---|
| [constructioncoverage.com/takeoff-software](https://constructioncoverage.com/takeoff-software) | C1 (both runs), C3, C4, C6, C15, V10 |
| [TDPM best AI estimating software](https://thedigitalprojectmanager.com/tools/best-ai-estimating-software/) | C1, C11, V1, V5, V7, V8 (sister page [best AI construction estimating](https://thedigitalprojectmanager.com/tools/best-ai-construction-estimating-software/) in C11) |
| [ConstructConnect "top players in 2026" guide](https://www.constructconnect.com/blog/ai-powered-takeoff-and-estimating-software-a-contractors-guide-to-the-top-players-in-2026) | C1, C3, C4, C11, P5, B4 |
| [ContraVault 10 best AI takeoff tools 2026](https://www.contravault.com/blog/10-best-ai-takeoff-software-tools-for-construction-in-2026) | C1, C11, V4 (sibling pages in V4, V7) |
| G2 pages: [Togal alternatives](https://www.g2.com/products/togal-ai/competitors/alternatives), [PlanSwift alternatives](https://www.g2.com/products/planswift/competitors/alternatives), [PlanSwift vs STACK](https://www.g2.com/compare/planswift-vs-stack-takeoff-estimate), [STACK alternatives](https://www.g2.com/products/stack-takeoff-estimate/competitors/alternatives) | Comparison prompts |
| Capterra / GetApp / Software Advice: [Togal alternatives](https://www.capterra.com/p/10001876/Togal-AI/alternatives/), [PlanSwift alternatives](https://www.capterra.com/p/70808/PlanSwift/alternatives/), [takeoff category](https://www.capterra.com/takeoff-software/), [GetApp Togal alternatives](https://www.getapp.com/construction-software/a/togal-ai/alternatives/), [Software Advice takeoff comparison](https://www.softwareadvice.com/construction/takeoff-software-comparison/) | Comparison and category prompts |
| [SourceForge AI takeoff category](https://sourceforge.net/software/ai-takeoff/), [SourceForge Togal alternatives](https://sourceforge.net/software/product/Togal.AI/alternatives) | C1, V7 |
| [Handoff 6 best AI estimating 2026](https://www.handoff.ai/blog/6-best-ai-construction-estimating-software-2026-picks-compared); [Construction Placements best AI estimating](https://www.constructionplacements.com/best-ai-estimating-software-construction/) | C11, C13, V7; C1, C11, C13 |
| [helonic Togal alternatives](https://helonic.com/compare/togal-ai-alternatives); [nomic.ai best AI for cost estimation](https://www.nomic.ai/compare/best-ai-for-cost-estimation) | V1; C11, B2, B4 |
| [ForesightIQ Togal landscape](https://www.foresightiq.co/competitive-landscape/togalai) | V1 run 2 — the only third-party page seen getting Quotr named in an unbranded answer. Note: the fact-check found its only source for Quotr is Quotr's own blog, so it is not independent proof |
| Reddit r/estimators: [drywall](https://www.reddit.com/r/estimators/comments/1gl3bi8/best_takeoff_software_for_a_drywall_contractor/), [Bluebeam vs others](https://www.reddit.com/r/estimators/comments/1ekpil5/bluebeam_vs_other_estimating_softwares/), [cheap takeoff](https://www.reddit.com/r/estimators/comments/1so58vb/cheap_takeoff_software_for_casual_side_use/), [AI takeoff real?](https://www.reddit.com/r/estimators/comments/1kadwx5/are_there_actually_any_aibased_takeoff_software/), [Mac takeoff](https://www.reddit.com/r/estimators/comments/1rpfwg0/macos_takeoff_app_that_actually_works/) | 6 prompts |

A site-restricted web search returned **no Quotr page or mention** on G2, Capterra, GetApp, Software Advice, SourceForge, Slashdot, Construction Coverage, TDPM, ConstructConnect, ContraVault, Construction Placements or Easy Takeoffs. This is a search check, not proof: Quotr does have a G2 profile under the old slug `quotr-io`, which the search did not surface. Full map: [[Citation sources map]].

---

## 6. Which Quotr pages AI engines use

| Use | Pages |
|---|---|
| **Cited in unbranded answers** | [best-togal-ai-alternatives](https://quotr.ai/blog/best-togal-ai-alternatives/) (V1); [best-planswift-alternatives-2026](https://quotr.ai/blog/best-planswift-alternatives-2026/) (V3, S3); [is-ai-takeoff-actually-accurate-yet](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/) (P5); [outsource-construction-estimating](https://quotr.ai/blog/outsource-construction-estimating/) and [commercial-estimating-services](https://quotr.ai/blog/commercial-estimating-services/) (C12); [quantity-takeoff-services](https://quotr.ai/blog/quantity-takeoff-services/) (S9); [how-developers-source-building-materials](https://quotr.ai/blog/how-developers-source-building-materials/) (S6) |
| **Retrieved but not used** | [ddp-construction-materials](https://quotr.ai/blog/ddp-construction-materials/) (C10); [stack-alternative](https://quotr.ai/blog/stack-alternative/) (V10) |
| **Brand prompts only — main site** | [/](https://quotr.ai/), [/about-us](https://quotr.ai/about-us), [/software](https://quotr.ai/software), [/service](https://quotr.ai/service), [/pricing](https://quotr.ai/pricing), [/faq/](https://quotr.ai/faq/), [/terms](https://quotr.ai/terms), [/disambiguation/](https://quotr.ai/disambiguation/) |
| **Brand prompts only — comparison and buyer posts** | [quotr-vs-togal-ai-comparison-2026](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/), [quotr-ai-vs-planswift-ai-takeoff-procurement-comparison-2026](https://quotr.ai/blog/quotr-ai-vs-planswift-ai-takeoff-procurement-comparison-2026/), [quotr-ai-vs-beam-ai-takeoff-estimating-comparison](https://quotr.ai/blog/quotr-ai-vs-beam-ai-takeoff-estimating-comparison/), [ai-construction-estimating-software-buyers-guide](https://quotr.ai/blog/ai-construction-estimating-software-buyers-guide/) (stale pricing), [best-ai-construction-estimating-software-2026](https://quotr.ai/blog/best-ai-construction-estimating-software-2026/), [bluebeam-alternative](https://quotr.ai/blog/bluebeam-alternative/), [best-togal-ai-alternatives-2026](https://quotr.ai/blog/best-togal-ai-alternatives-2026/) |
| **Brand prompts only — other posts** | [best-electrical-estimating-software-2026](https://quotr.ai/blog/best-electrical-estimating-software-2026/), [structural-steel-estimating](https://quotr.ai/blog/structural-steel-estimating/), [ai-bidding-software-construction](https://quotr.ai/blog/ai-bidding-software-construction/), [new-pricing](https://quotr.ai/blog/new-pricing/) |
| **Staging host (should not be cited)** | [test.quotr.io/disambiguation/](https://test.quotr.io/disambiguation/) (B2 and its re-run) |
| **Seen only in web search results** | [real-estate-pro-forma-software-comparison](https://quotr.ai/blog/real-estate-pro-forma-software-comparison/), [chatgpt-for-construction-estimating](https://quotr.ai/blog/chatgpt-for-construction-estimating/) |

**Two near-duplicate Togal posts were both retrieved** ([/best-togal-ai-alternatives/](https://quotr.ai/blog/best-togal-ai-alternatives/) and [/best-togal-ai-alternatives-2026/](https://quotr.ai/blog/best-togal-ai-alternatives-2026/)). See [[Website audit]].

---

## 7. Reproducibility: do results hold on a second run?

### 7a. Same-session re-runs (original researcher)

| Prompt | Run 1 | Run 2 | Difference |
|---|---|---|---|
| C1 best AI takeoff software for subcontractors 2026 | Togal, STACK, PlanSwift, Beam AI; no Quotr | Same 4 brands, reordered (1. Togal 2. STACK 3. Beam AI 4. PlanSwift); no Quotr | Citation list identical (same 20 URLs, same order); only brand order changed |
| V1 Togal.AI alternatives | Quotr in table row "AI-focused takeoff" (about 15th of 17) | Quotr gets its own bullet (#8 of 9), attributed to "ForesightIQ and Quotr's own materials" | Same citation list; Quotr slightly more prominent |
| V3 PlanSwift alternatives 2026 | Quotr blog cited for PlanSwift facts; Quotr not named | Same, plus the "$1,749/user/year" fact from Quotr's post; Buildxact and CostLogic added | Stable: "cited, not named" |
| B1 What is Quotr.ai? | Accurate; FLOZ Inc; disambiguation cited | Accurate; adds Software / Service / Procurement breakdown | Stable, positive |
| B3 Is Quotr.ai legit? | Uses Quotr Pro's 37 ratings / 4.7 as a Quotr signal | Same mix-up, plus "G2 shows 0 reviews for QUOTR" | Stable, negative |

### 7b. Independent fact-check re-runs (separate researcher, same day)

| Prompt | Reproduces? | Detail |
|---|---|---|
| C1 | **Yes** | Togal.AI, Beam AI, STACK, PlanSwift; no Quotr in answer or 20 citations |
| C9 | **Yes** (identical brand set) | esti-mate, Buildertrend, Procore, Buildxact, ConWize; no Quotr in 19 citations |
| C11 | **Yes** (SimplyWise added) | No Quotr; no quotr.ai URL in 20 citations; nomic.ai cited again |
| C12 | **Yes** | Quotr post again first citation; rates credited to "Some firms"; Quotr not named |
| B2 | **Yes** | Accurate pricing; again notes older Solo/Team packaging; again cites test.quotr.io |
| B3 | **Yes** | Quotr Pro app's 37 ratings and 4.7/5 again presented as Quotr's (that app belongs to a different developer) |
| B4 | **Yes** | "From about $299.90/month" again; "many of the comparison claims come from Quotr.ai's own blog content" |
| B6 | **Yes** | Same founders; $200K + $3.5M; "PitchBook also showing a $190K seed round in Oct. 2024" (that figure is not on the live PitchBook page) |
| S6 factory-direct (competitor-note prompt) | **Partly** | Quotr named **3rd of 6** (not 1st), described as a sourcing service rather than an AI takeoff platform |
| S12 LA fire rebuild cost (new) | n/a | No Quotr |
| V1, V3, C13, P5 | **Not re-run** | Refused by a permission filter; treat as single-session results |

**Takeaways:**
- The headline findings hold: Quotr is absent from unbranded category prompts; its content is used without its name on pricing prompts; brand answers still repeat the stale $299.90 entry price, borrow the Quotr Pro app's ratings, and cite the staging host.
- **Correction to earlier notes:** do not say Quotr "wins" the factory-direct query. It surfaces only when the prompt closely matches Quotr's own copy, and its rank is unstable.
- The source list tends to be stable on repeat runs; the order and emphasis of brands changes. One run is a fair test of "is Quotr in the candidate set?", but position data is noisy.

---

## 8. Perplexity vs traditional search (cross-check)

| Prompt | Traditional search result | Perplexity result |
|---|---|---|
| C1 best AI takeoff software for subcontractors 2026 | Quotr's [roundup](https://quotr.ai/blog/best-ai-construction-estimating-software-2026/) ranked **4th of 9**; the search summary still recommended Won2Build, Beam AI, Togal.AI and STACK | Not retrieved in either run |
| C2 residential estimating software | No Quotr page in top 9 | No Quotr |
| V1 Togal.AI alternatives | [Quotr vs Togal](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/) ranked **6th of 9**; summary listed Quotr under "Specialized AI Takeoff Alternatives" | Named, low in list |
| V3 PlanSwift alternatives 2026 | Quotr post ranked **6th of 9**; the summary **repeated Quotr's own claim** "For most contractors the strongest alternative is Quotr.ai" | Used only as a fact source; Quotr not recommended |
| P5 how accurate is AI takeoff | Quotr **not in top 9** | Quotr article was the **first citation** (brand not named) |
| "Quotr.ai reviews" | #1 result: the unrelated **Quotr Pro app**; #2: Crunchbase with an outdated "Revit / architects" description; the rest quotr.ai pages | (see B3) |
| "Togal.AI alternatives 2026" (offsite notes) | Results 5–7 were Quotr's own posts; the summary repeated "Quotr.ai is the best Togal.AI alternative in 2026" | — |
| "best construction takeoff software 2026" and "best construction estimating software for subcontractors 2026" (offsite notes) | Quotr absent | — |

**What this shows:** simple search summaries can pass Quotr's self-ranking straight through; Perplexity does not. Good organic rank does not guarantee AI citation, and the reverse is also true (P5).

---

## 9. How AI engines describe Quotr today (accuracy check)

"Correct / current" is what Quotr's own live pages said on 2026-09-25. Where Quotr's pages disagree with each other, the fact is marked TO CONFIRM with Quotr.

| Topic | What the AI said | Correct / current | Verdict | Likely cause |
|---|---|---|---|---|
| What Quotr is (B1) | "AI construction estimating and procurement platform for contractors, subcontractors and developers… built by FLOZ Inc… not a generic quotation or invoicing app" | Matches /disambiguation/ and /software/ | **Accurate** | /disambiguation/ page works for definitions |
| Product lines (B1 run 2) | Software, Service, Procurement | Matches site | **Accurate** | — |
| Pricing (B2) | Lite $79.90/seat/mo, Plus $299.90/seat/mo, Enterprise custom, 7-day trial, Service $0.25/sq ft (<50k sq ft) and $0.10/sq ft (>50k) | Matches [/pricing/](https://quotr.ai/pricing/) | **Accurate** | — |
| Pricing (B4, V2, offsite test, Nomic) | "From $299.90/mo"; "Solo $299.90 / Team (2–6 seats) $499.90 / Enterprise (7+)" | Entry plan is Lite at $79.90 since the Sep 14, 2026 pricing change | **Stale** — makes Quotr's entry price look nearly four times higher than it is | About 13 Quotr URLs (mostly blog posts, plus the indexed /contractors page) and llms.txt still carry old tiers |
| Reviews / trust (B3) | Quotr Pro app's "37 ratings" and "4.7/5" given as Quotr's | Quotr Pro is an unrelated app by another developer | **Wrong (mix-up)** | No confirmed reviews of Quotr.ai anywhere; the engine borrows a namesake's |
| G2 (B3 run 2) | "G2 shows 0 reviews for QUOTR" | **UNVERIFIED** (G2 blocked every direct check) | Plausible | Apparently empty G2 profile |
| Trust summary (B3, O1) | "plausibly legitimate but not independently well-validated"; "vendor assertions"; "I did not find independent third-party reviews" | Fair description of the evidence | Accurate, but unhelpful | Brand answers are about 60–70% self-sourced |
| Funding (B6) | $200K pre-seed + $3.5M seed, but "PitchBook also showing a $190K seed round in Oct. 2024"; Caplight "does not fully agree" | TO CONFIRM with Quotr. The live PitchBook page shows one seed round dated 01-Jan-2025 with **no amount**, so the "$190K" figure is not from PitchBook as far as we can see (verification file, claim 22) | **Conflict flagged; part of it is wrong** | Databases and podcast notes disagree with /disambiguation/ |
| Founders (B6) | Hanyang Liu and Junzhe Shi | Matches /about-us/; /disambiguation/ lists only Junzhe Shi | Mostly accurate | Quotr's own pages differ |
| Factory network (offsite test) | "Quotr publicly claims access to 50+ to 220+ factories, depending on the page" | TO CONFIRM with Quotr (site says 220+, 50+ and 30+ in different places) | **Hedged** | Quotr's own inconsistency |
| Overall positioning (offsite test) | "positioned as a procurement program, not just software" | Quotr is software + service + procurement | **Misread** | Homepage says procurement is "A procurement program, not software or estimating services" |
| Factory-direct (S6 re-run) | "Quotr.ai and FBM Sourcing emphasize sourcing and procurement more than AI takeoff" | Quotr offers both | **Partial** | Procurement content not linked to takeoff in citable text |
| HQ (search summary) | "based in San Francisco" | TO CONFIRM with Quotr (/disambiguation/ says Berkeley; /terms and blog say San Francisco) | **Conflict** | Quotr's own pages differ |
| Legacy description (search summary) | "an AI assistant providing real-time cost estimation and Revit integration to help architects save time" | Old product positioning | **Outdated** | Crunchbase / LinkedIn / F6S legacy copy |
| Founder profile (search summary) | "raised a $4.2M seed round led by Initialized Capital and released … zerank-1" | No Quotr source supports this | **Wrong (merged with another startup)** | Thin, inconsistent entity data |
| "Quotr app" (B5) | Lists 4 "Quotr" apps; Quotr.ai is 3rd | Quotr.ai has no consumer app | **Confused** | Name collisions |
| Comparison framing (B4, V2, B7, S7, O3) | Quotr = takeoff → estimate → bid → procurement; "most end-to-end", "most all-in-one" | Matches Quotr's positioning | Accurate but self-sourced | Built from Quotr's own blog |
| Accuracy claims (B3) | Quotr's 95–99% accuracy flagged as self-published | Claim is from "Quotr internal benchmarking" | Accurate framing | No third-party benchmark |

Canonical facts belong in [[Entity fact sheet]].

---

## 10. Context: what published studies say about other engines

We could not test ChatGPT, Google AI Overviews / AI Mode, Gemini or Claude. No published study was found on how they answer **takeoff or estimating** questions. The general findings below come from the visibility notes (§6) and tell us how to measure, not how Quotr performs.

- **Citations churn fast.** A Digital Authority Partners study tracked 1,127 URLs cited by ChatGPT, Perplexity, Gemini, Copilot and Google AI Overviews across 30 queries in 3 waves 14 days apart. Only 119 URLs (about 10.6%) were cited in all three waves; average citation retention was 33% over 28 days; 60% of AI-cited URLs did not rank in the top 20 organic results. (The fact-check confirmed the 1,127 / 119 / 33% figures from a search-index summary of [the study](https://www.digitalauthority.me/resources/ai-visibility-study/), which also says Gemini had the lowest retention, 11%. The 60% figure was not re-checked, and the page itself was not opened.)
- **Construction project-management answers:** vendor-run tracker sites say Procore leads across ChatGPT Search and Google AI Mode (about 31–32% of AI mentions in two trackers). Directional only ([trakkr](https://trakkr.ai/ai-recommends/project-management/construction), [parse.gl](https://parse.gl/markets/construction/construction-industry-software-and-services)).
- **Engines disagree:** a press-release headline (2026-08-12) says ChatGPT and Gemini recommend a different #1 software in one of every three categories ([GlobeNewswire](https://www.globenewswire.com/news-release/2026/08/12/3343763/0/en/chatgpt-and-gemini-recommend-different-1-software-in-one-of-every-three-categories-new-study-finds.html); headline only).
- **Togal markets a ChatGPT tie-in** ([Togal blog](https://www.togal.ai/blog/chatgpt-togal-ai-takeoff-construction-software); date not verified).

**So:** measure per engine, monthly, and expect one-off placements to fade unless refreshed. More in [[How AI engines choose sources]].

---

## 11. Limitations (read before comparing numbers)

- **One engine (Perplexity Sonar API), one day.** Not the consumer app, not ChatGPT, not Google AI Overviews / AI Mode, not Gemini, Claude or Copilot.
- **Mostly single runs.** Only 5 prompts were run twice in-session and 10 were re-run independently. Answers vary between runs, especially brand order. The GEO-evidence fact-check calls a single run per prompt "a weak baseline" and points to 2026 research on measurement variance ("Don't Measure Once", arXiv 2604.07585; listing seen, not read). Run each prompt at least twice from now on.
- **Hand-tallied SOV** (±1 per brand).
- **Pages not opened:** the scraper was rate-limited for about 45 minutes. Whether the most-cited listicles list Quotr (Construction Coverage, TDPM, ContraVault, the G2/Capterra alternatives pages, nomic.ai's cost-estimation page, octopusbuilds) was checked with site-restricted search, not by reading them. The ConstructConnect guide and Nomic's Kreo-alternatives list were read directly (see [[Off-site presence]]).
- **Reddit** could not be searched with the web search tool.
- **4 fact-check re-runs refused** (V1, V3, C13, P5).
- **Pricing on some Quotr blog posts** was seen through AI answers and search snippets, not by opening every page.
- **No traffic or impression data.** Whether AI answers show Quotr's pages, or send visits or leads, is unknown. Quotr's GA4 (AI channel), Search Console Generative AI performance report and Bing Webmaster AI Performance report would fill this gap (TO CONFIRM with Quotr).
- **Fact-check status:** the verification file is complete, and its corrections have been applied on this page (for example: the $190K "PitchBook" seed figure appears only in Perplexity answers; G2 now owns Capterra, GetApp and Software Advice).

---

## Related pages

- [[Presence scorecard]] — scores built from these results
- [[Off-site presence]] — the third-party sources that explain these results
- [[Website audit]] — the on-site issues behind stale pricing and staging-host citations
- [[GEO tactics already used]] — which of Quotr's tactics show up in these answers
- [[Tracking set]] — the prompt set to re-run monthly
- [[Prompt library]] — the wider library of buyer prompts
- [[Citation sources map]] — where AI engines get their answers
- [[Competitor landscape]] — the brands that win these answers
- [[Tracking setup]] — how to set up ongoing tracking
- [[KPIs and dashboard]] — KPIs based on this baseline
