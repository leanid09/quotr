---
type: hub
description: The fixed 53 prompts to re-run monthly, with the September baseline, run rules and copy-paste templates.
last_verified: 2026-09-25
verify_every_days: 30
cssclasses:
- wide
---
# Monthly AI-Visibility Tracking Set

> [!abstract] What this page is for
> The fixed set of 53 prompts to re-run every month to see whether AI answer engines mention, cite and describe Quotr.ai correctly, with the September 2026 baseline for each prompt and step-by-step instructions (engines, number of runs, what to record, copy-paste templates).

> [!info]- Sources
> [[quotr_ai_visibility_tests]] (40 baseline prompts, 45 runs, method), [[verification_quotr_and_competitors]] (independent re-runs; overrides the other notes), [[competitor_geo_benchmark]] (S prompts), [[geo_content_playbook_b2b]] (§4 measurement), [[verification_geo_evidence]] (measurement corrections and 2026 developments: claims 3, 6, 7, 8, 21; M1, M2, M8); six new baseline runs (N1–N6) made for this page on 2026-09-25 with Perplexity Sonar (`mcp__Slashy__web_search`). Prompt IDs link to [[Prompt library]] and [[AI visibility baseline]].

---

## 1. At a glance

- **53 prompts.** The **core 40** are the September 2026 baseline prompts, kept word for word so every month compares like for like. The **extension 13** fill gaps in the core: 7 supplementary prompts already tested once in September (S4, S5, S6, S9, S10, S11, S12) and 6 new prompts (N1–N6) that were given a baseline run on 2026-09-25.
- **Two tiers.** **Tier A** (23 prompts) are the headline prompts: run them twice on every engine. **Tier B** (30 prompts): run once per engine.
- **Baseline is Perplexity only.** September 2026 results come from Perplexity Sonar. ChatGPT, Google AI Mode / AI Overviews, Gemini, Claude and Copilot have **no baseline yet**; October 2026 will be their first month.

### Balance of the set

| Dimension | Split |
|---|---|
| Funnel stage | Learn / problem: 14 · Compare / evaluate: 31 (21 category, service or supplier prompts; 10 alternatives or head-to-head) · Decide / brand: 8 |
| Branded vs unbranded | 8 prompts name Quotr (T17 and T34–T40) · 45 unbranded |
| Personas (a prompt can have several) | SUB 25 · RES 17 · DEV 11 · GC 9 · BUY 7 · SVC 2 · FUND 1 · ALL 10 |
| Trades | Drywall (T04, T26), flooring (T05), electrical (T06), plumbing (T49), HVAC (T50), roofing (T51), framing/lumber (T53), cabinets/windows/flooring sourcing (T14, T48), general (the rest). Painting, concrete, siding, tile and insulation are covered in the full [[Prompt library]] but are not tracked monthly because they are low priority for Quotr. |
| Quotr product | Software (takeoff, estimating, bidding): 30 · Estimating service and developer cost: 6 (T12, T28, T32, T44, T45, T47) · Procurement, sourcing and tariffs: 9 (T09, T10, T14, T29, T33, T42, T43, T46, T48) · Brand: 8 |

### September 2026 baseline in one table (Perplexity Sonar, first runs)

| Metric | Baseline |
|---|---|
| Unbranded prompts where Quotr is **named** | Core: 1 of 32 (3.1%). Extension: 1 of 13 (S6, a prompt that echoes Quotr's own wording) |
| Unbranded prompts where a quotr.ai page is **cited** in the answer | Core: 4 of 32 (12.5%). Extension: 3 of 13 (S6, S9, N2) |
| Unbranded prompts where a quotr.ai page is in the **source list** | Core: 6 of 32 (18.8%) |
| Quotr **share of voice**, unbranded core prompts | About 0.7% (STACK, PlanSwift, Buildxact about 6.5% each) |
| Brand prompts with an **accuracy problem** | 5 of 8 (B3 Quotr Pro conflation, B4 and V2 stale price, B5 namesakes, B6 funding conflict) |

Source: [[quotr_ai_visibility_tests]], §5, and N1–N6 runs on 2026-09-25.

**Two meanings of "cited" (read this before quoting the numbers).** "Cited **in the answer**" (4 of 32) means the answer text actually used a quotr.ai page as a footnoted source. "In the **source list**" (6 of 32) means a quotr.ai page appeared anywhere in the engine's list of sources, whether or not the answer used it. The audit report and the rest of this knowledge base quote the **6 of 32** figure ("a quotr.ai page appeared in the source list of 6 of 32 answers", the same count as reddit.com). Both numbers are correct; always say which one you mean.

---

## 2. The 53 prompts and their baselines

Copy the prompt text **exactly**, including capital letters and punctuation. Do not add context such as "I am a contractor". "Named in answer" lists the brands the engine recommended instead of Quotr, in the order it named them.

Result words: **Absent** = not named, not cited · **Cited, not named** = a quotr.ai page was a source but the answer did not say "Quotr" · **Retrieved only** = a quotr.ai page was in the source list but unused · **Named** = Quotr is in the answer text.

### 2a. Core 40 (September 2026 baseline prompts)

![[Prompts.base#Core 40]]

### 2b. Extension 13

![[Prompts.base#Extension 13]]

**Tier A (23 prompts):** T01, T02, T04, T08, T09, T11, T12, T13, T14, T16, T18, T22, T25, T29, T30, T33, T34, T35, T36, T37, T46, T48, T49. All others are Tier B. They were chosen to cover every persona, Quotr's three products, the brand-accuracy problems and the prompts where Quotr is closest to being named (cited or retrieved but not named).

---

## 3. How to run the tracking (step by step)

### 3.1 When

- **Once a month, in the first week** (for example, the first Tuesday–Thursday). Keep the same window each month.
- Monthly is the recommended cadence: AI citations change a lot from month to month, and weekly checks mostly measure noise ([[geo_content_playbook_b2b]], §4; Profound, a tracking vendor, reports 40–60% of cited domains changing month to month for the same query).
- One study found only about 10.6% of AI-cited URLs were still cited in all three waves 14 days apart, with 33% retention over 28 days (Digital Authority Partners; confirmed in [[verification_quotr_and_competitors]], claim 37). So **never judge progress from one month**; look at three-month trends.

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

**How the engines are counted.** Google AI Mode and Google AI Overviews are two different surfaces, but they are checked in the same signed-out Google session. So the table above lists five monthly surfaces, and the effort maths in 3.3 counts **four monthly engine runs** (ChatGPT, Google, Perplexity, Gemini), with the AI Overview recorded as a field ("AIO shown?") in each Google run.

**Where this departs from the audit report.** The report recommends re-running the questions every month in all six tools (ChatGPT, Google AI Mode, Gemini, Perplexity, Claude and Copilot). This set deliberately runs **Claude and Copilot quarterly** to keep the monthly workload manageable, because both send a small share of referrals today. To stay close to the report: run the **Full** routine (all six tools) in **October 2026** as the first multi-engine baseline, then every quarter (January, April, July). If a paid tracking tool is bought, move Claude and Copilot to monthly at no extra manual cost.

**Keep engines separate.** Report each engine on its own line. Do not blend them into one score: citations barely overlap across engines, and one study found ChatGPT and Gemini recommend a different #1 product in one of every three categories (headline only; [[quotr_ai_visibility_tests]], §6).

### 3.3 How many runs

| Option | What to run | Runs per month | Rough effort (our estimate) |
|---|---|---|---|
| **Lite** (manual, minimum) | Tier A (23) × ChatGPT, Google AI Mode, Perplexity × 1 run, plus all 53 × 2 runs on the Perplexity Sonar API (scripted) | 69 manual + 106 scripted | About 3 hours of manual work |
| **Standard** (recommended) | Tier A × 4 monthly engines × 2 runs; Tier B × 4 monthly engines × 1 run | 184 + 120 = 304 | 10–15 hours manually, so use a tracking tool |
| **Full** (quarterly) | Standard + Claude and Copilot (all 53 × 1 run each) | 304 + 106 = 410 | Tool only |

Why two runs for Tier A: the September tests showed the **list of sources stays about the same from run to run, but the order of brands changes**, so position is noisy ([[quotr_ai_visibility_tests]], §5). 2026 research papers also argue for repeated sampling rather than one-off checks (verification_geo_evidence.md, M8). Tools such as Otterly.AI, Peec AI, Semrush's AI toolkit, Ahrefs Brand Radar or Profound can automate runs; prices are in [[AI visibility tools compared]].

### 3.4 Session rules (so months are comparable)

1. Use logged-out or clean sessions. Personalisation (history, memory, location) can change which brands are recommended ([[quotr_ai_visibility_tests]], §6).
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
| Third-party pages naming Quotr | Any non-quotr.ai source that mentions Quotr (these are gold: log them in [[Off-site presence]]) |
| Evidence | Screenshot file name or share link |

### 3.6 Accuracy checklist for brand prompts (T17, T34–T40)

Flag an answer if it says any of these. All are known errors from September 2026; the correct facts are in [[Entity fact sheet]].

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

Use the same rules as the baseline ([[AI visibility baseline]], §1):

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
| GA4 → **AI Assistant** channel + a custom regex channel | Visits from AI tools | The native channel (May 13, 2026) does **not** include Perplexity, so keep a custom channel with a regex such as `chatgpt\.com\|chat\.openai\.com\|perplexity\.ai\|gemini\.google\.com\|copilot\.microsoft\.com\|claude\.ai` placed above Referral (verification_geo_evidence.md, claim 7; playbook §4). In this table the separators are shown as `\|`; in GA4 type a plain vertical bar without the backslash |
| Demo/trial form: "How did you hear about us?" | Self-reported AI influence | Options should include ChatGPT, Google AI, Perplexity, YouTube, Reddit, Facebook group (playbook §4) |

Setup details: [[Tracking setup]]. KPI dashboard: [[KPIs and dashboard]].

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

The set has 45 unbranded prompts (the core 32 plus the extension 13). Report the core 32 separately as well, so rates stay comparable with the September baseline.

```
| Month | Engine | Unbranded prompts run | Mention rate | Citation rate | Retrieval rate | Cited-not-named | SOV | Avg position | Brand accuracy errors | New 3rd-party pages naming Quotr | Change vs last month |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10 | Perplexity – Sonar API | 45 | | | | | | | | | |
| 2026-10 | ChatGPT – search | 45 | | | | | | | | | first month |
| 2026-10 | Google AI Mode | 45 | | | | | | | | | first month |
| 2026-10 | Google AI Overviews (where one appears) | 45 | | | | | | | | | first month |
| 2026-10 | Gemini | 45 | | | | | | | | | first month |
| 2026-10 | Claude (quarterly; Full run) | 45 | | | | | | | | | first month |
| 2026-10 | Copilot (quarterly; Full run) | 45 | | | | | | | | | first month |
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
5. **Review every quarter:** swap in up to 5 prompts from [[Prompt library]] where new Quotr pages have been published, so the set tests the pages the team is building.
6. **Watch the control prompt (T43).** It uses Quotr's own words. If Quotr is named there but not in T10 or T14, visibility has not really improved for buyer-style questions.

### Change log

| Date | Change |
|---|---|
| 2026-09-25 | Set created: core 40 (September baseline) + extension 13 (S4, S5, S6, S9, S10, S11, S12, N1–N6). N1–N6 given a first Perplexity Sonar run on 2026-09-25 |

---

## Related pages

- [[Prompt library]] — all 282 prompts, with priorities and the Quotr page for each
- [[Buyer questions by trade]] — real buyer questions by trade, with sources
- [[AI visibility baseline]] — full September 2026 results and method
- [[Entity fact sheet]] — correct facts to check brand answers against
- [[KPIs and dashboard]] — how these numbers roll into the KPI dashboard
- [[Tracking setup]] — GA4, Search Console and Bing setup
- [[AI visibility tools compared]] — tools that can automate these runs
