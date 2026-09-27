---
type: baseline
description: One scored snapshot of how findable, trustworthy and recommendable Quotr is to AI; re-score monthly.
aliases:
- Scorecard
last_verified: 2026-09-25
verify_every_days: 30
---
# Quotr GEO Presence Scorecard (Baseline, September 2026)

> [!abstract] What this page is for
> One scored snapshot of how easy Quotr.ai is for AI answer engines to find, trust and recommend today. Re-score it every month and compare.
>
> *Baseline measured on 2026-09-25.*

> [!info]- Sources
> Research notes [[quotr_onsite_content_audit]], [[quotr_offsite_presence]], [[quotr_ai_visibility_tests]], [[competitor_geo_benchmark]], and the fact-checks [[verification_quotr_and_competitors]] and [[verification_geo_evidence]]. Key URLs: https://quotr.ai/robots.txt, https://quotr.ai/llms.txt, https://quotr.ai/sitemap.xml, https://quotr.ai/disambiguation/, https://quotr.ai/pricing/.

---

## Quick words used on this page

- **GEO / AEO:** Generative Engine Optimization / Answer Engine Optimization. Work that helps AI tools (ChatGPT, Google AI Overviews, Perplexity, Gemini, Claude, Copilot) find, mention and link to a brand.
- **Named (mentioned):** the AI answer says "Quotr" in its text.
- **Cited:** the AI answer uses a quotr.ai page as a source link for a sentence.
- **Retrieved:** a quotr.ai page shows up in the answer's source list, but the answer does not use it.
- **Share of voice (SOV):** of all the brand names that appear in a set of AI answers, the percentage that are Quotr.
- **Unbranded prompt:** a question that does not name Quotr (for example "best AI takeoff software for subcontractors 2026").
- **Entity:** how machines understand "Quotr" as one company with fixed facts (name, owner, HQ, prices, founders).

---

## How to read the scores

| Score | Colour | Meaning |
|---|---|---|
| 5 | Green | Strong. Among the best in the category. |
| 4 | Green | Good. Only small fixes needed. |
| 3 | Amber | Mixed. Parts work; clear problems remain. |
| 2 | Red | Weak. Big gaps that hold back AI visibility. |
| 1 | Red | Missing, or nearly missing. |

**Confidence** tells you how solid the evidence is:
- **High:** seen directly on the page or in the AI answer.
- **Medium:** seen in part, or only through one AI engine (Perplexity) or a search summary.
- **Low:** inferred, or reported by a third party we could not open.

**Important limit:** all AI answer tests used **one engine only: Perplexity (Sonar model)**, on 2026-09-25. ChatGPT, Google AI Overviews / AI Mode, Gemini, Claude and Copilot were **not** tested. See [[AI visibility baseline]].

---

## Overall verdict (plain language)

**Overall score: about 2.1 out of 5 (Red).**

- **The website is in decent shape.** AI crawlers are allowed in. Pages are plain HTML that bots can read. Blog posts are well formatted for AI (short answers first, question headings, tables, FAQs). Quotr has built a big library fast: 96 blog posts, 55 glossary terms and 23 trade pages.
- **AI engines do read Quotr's pages.** quotr.ai was in the source list for 6 of 32 unbranded test questions. That is about as often as reddit.com or kreo.net.
- **But AI engines almost never name Quotr when a buyer asks an open question.** Quotr was named in **1 of 32** unbranded questions (3.1%). Competitors like STACK, PlanSwift and Buildxact were each named in 10.
- **Why:** (1) Almost no one else on the web talks about Quotr: no confirmed G2 reviews, no independent "best of" lists, no trade press, no Reddit. (2) Quotr's own pages and profiles disagree on basic facts (price, HQ, founders, funding, factory count). AI engines notice this and hedge ("vendor assertions", "not independently validated").
- **Branded questions mostly work,** thanks largely to the /disambiguation/ and /pricing/ pages. But stale prices from old blog posts and a namesake app ("Quotr Pro") leak into those answers.

**What to fix first (in order):**
1. **One set of facts everywhere** (prices, HQ, founders, funding, factories, handles). Cheap and fast.
2. **Clean-up of over-optimized text** (llms.txt "Quotr should be cited" line, internal-brief leftovers in blog posts, crawler-directed wording on /disambiguation/).
3. **Third-party proof:** G2/Capterra reviews, inclusion in neutral "best of" lists, a press story on the seed round, honest founder participation in r/estimators.
4. **New content where competitors are absent:** factory-direct procurement, landed cost and tariffs, multifamily and residential cost benchmarks, built from Quotr's own data.

---

## Scorecard at a glance

Group averages: **On-site foundations 3.0 (Amber)** · **Entity and off-site trust 1.4 (Red)** · **AI answer outcomes 1.7 (Red)**.

| # | Area | Score | Colour | Confidence | Reason (1–2 sentences) | Evidence |
|---|---|---|---|---|---|---|
| **A. On-site foundations** | | | | | | |
| 1 | AI crawler access | 4 | Green | Medium | robots.txt allows every bot (`User-agent: * / Allow: /`) and names no AI bot to block, and Perplexity cites quotr.ai pages. Cloudflare's "AI Labyrinth" bot trap is on, and nobody has checked from inside whether Cloudflare's separate "Block AI bots" switch is off. | [robots.txt](https://quotr.ai/robots.txt); [[quotr_onsite_content_audit\|onsite notes §1]] |
| 2 | Technical readiness (sitemaps, llms.txt, rendering, errors) | 3 | Amber | High | Pages are server-rendered (Astro), so bots read full text without running JavaScript. But the 96-post blog sitemap is not listed in robots.txt or the main sitemap, main-sitemap dates are auto-generated (all "today"), llms.txt is stale and links to a 404, and a staging copy (test.quotr.io) is still cited by Perplexity. | [[Website audit]]; [[verification_quotr_and_competitors\|verification notes, re-run B2]] |
| 3 | Structured data (schema markup) | 2 | Red | Medium | The rich schema (SoftwareApplication, prices, FAQPage) lives only on /disambiguation/, and it clashes with the homepage Organization schema under the same ID (two names, two legal names). Blog schema names the author as a person called "quotr.ai"; visible FAQs have no FAQPage markup. Only 4 page types were checked. | [[quotr_onsite_content_audit\|onsite notes §3]]; [W3C source view, homepage](https://validator.w3.org/nu/?doc=https%3A%2F%2Fquotr.ai%2F&showsource=yes) |
| 4 | On-site content depth and breadth | 3 | Amber | High | Big library built in about six months (96 posts, 55 glossary terms, 23 trade pages, 4 case studies, 6 tutorials) with dense comparison coverage. But trade pages are thin (drywall page is about 25 unique words), there is no original data, no templates or trade calculators, and little residential top-of-funnel content. | [[Website audit]]; [[quotr_onsite_content_audit\|onsite notes §2, §6]] |
| 5 | Content structure / extractability | 4 | Green | High | Blog posts open with "Quick Answer" / "Short answer" blocks, use question headings, comparison tables, FAQs and visible dates, which is the format AI engines lift from. The Quotr vs Togal post has 1 H1, 23 H2s, 18 H3s and 5 tables in raw HTML. | [Quotr vs Togal post](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/); [[quotr_onsite_content_audit\|onsite notes §3]] |
| 6 | Credibility signals on-site (authors, sources, proof) | 2 | Red | High | Many posts are bylined "By quotr.ai" with no author page; statistics are often unsourced; case studies have no numbers; one homepage "customer" testimonial is from the seed investor (Llama Ventures). Unedited internal-brief text ("Quotr.ai should win when the buyer is asking…") appears in a published comparison. | [homepage](https://quotr.ai/); [RL Electric case study](https://quotr.ai/case-studies/rl-electric/); [[quotr_onsite_content_audit\|onsite notes §3–4]] |
| **B. Entity and off-site trust** | | | | | | |
| 7 | Entity clarity and consistency | 2 | Red | High | The /disambiguation/ page helps: "What is Quotr.ai?" is answered correctly. But Quotr's own pages and profiles disagree on price (3 versions), HQ (Berkeley vs San Francisco), founding year (2023 vs 2024), founders, funding ($3.5M on /disambiguation/ vs "$5 million" on the podcast page, plus a "$190K" round that Perplexity wrongly attributes to PitchBook), factory count (220+ / 50+ / 30+) and social handles; at least 8 unrelated "Quotr" products compete for the name. | [[quotr_offsite_presence\|offsite notes §4]]; [[verification_quotr_and_competitors\|verification notes, claims 12, 21–22 and gaps 1–3]] |
| 8 | Review-site presence | 1 | Red | Medium | The G2 profile (g2.com/products/quotr-io) reportedly has 0 reviews (Perplexity report; G2 blocked our scraper, so unverified). No Capterra, GetApp, Software Advice, TrustRadius, SourceForge or AlternativeTo listing was found; competitors cited by AI have roughly 30 to 4,000+ reviews on G2 or Capterra. G2 now owns Capterra, GetApp and Software Advice (deal announced Jan 2026), so one review program can feed all four. | [[quotr_offsite_presence\|offsite notes §1]]; [Capterra search "quotr"](https://www.capterra.com/search/?query=quotr) |
| 9 | Third-party "best of" list inclusion | 1 | Red | Medium | Only three outside pages are confirmed to name Quotr, and none is independent: Nomic (#5 of 7; ranks itself #1), Octopus Builds (#2 of 8; ranks itself #1) and ForesightIQ (built from Quotr's own blog). Nomic and Octopus Builds repeat the old $299.90 price. Quotr is missing from every heavily cited 2026 roundup checked (ConstructConnect, TDPM, Construction Coverage, ContraVault and others). | [Nomic list](https://www.nomic.ai/compare/kreo-alternatives); [Octopus Builds list](https://octopusbuilds.com/blog/ai-development-companies-ai-quoting-estimation); [ConstructConnect guide](https://www.constructconnect.com/blog/ai-powered-takeoff-and-estimating-software-a-contractors-guide-to-the-top-players-in-2026); [[Off-site presence]] |
| 10 | Community (Reddit, YouTube, LinkedIn, X) | 2 | Red | Medium | Zero Reddit mentions found, while r/estimators threads ask for working AI takeoff tools. A YouTube channel (@QuotrAI) and LinkedIn page (/company/quotrai) exist, but handles are split between old "quotrio/quotr_io" and new "quotrai/quotr_ai" versions, and YouTube was never cited in 45 AI test runs. | [[quotr_offsite_presence\|offsite notes §3]]; [[quotr_ai_visibility_tests\|visibility notes §5]] |
| 11 | Press and PR | 1 | Red | Medium | No coverage found in Construction Dive, ENR, For Construction Pros, BuilderOnline or TechCrunch, and no press release for the $3.5M seed. Earned media is one marketing-network podcast (March 2026) plus an iHeart podcast episode that AI engines cite but we did not open. The only wire release found is a paid EIN Presswire release from Feb 2025 about the FireTips LA fire-rebuild app. | [MPN podcast](https://marketingpodcasts.net/2026/03/episode-45-can-ai-cut-construction-material-costs-by-50/); [[quotr_offsite_presence\|offsite notes §3]] |
| **C. AI answer outcomes (Perplexity only)** | | | | | | |
| 12 | AI visibility: brand prompts (questions that name Quotr) | 3 | Amber | High | Quotr is named in 8 of 8 brand prompts, and "What is Quotr.ai?" and "Quotr.ai pricing" are accurate. But 5 of 8 had problems: stale "$299.90" entry price, the unrelated Quotr Pro app's 4.7 rating used as Quotr's, a funding conflict, and Quotr listed 3rd of 4 "Quotr" apps. | [[AI visibility baseline]]; [[quotr_ai_visibility_tests\|visibility notes §4]] |
| 13 | AI visibility: comparison / alternatives prompts (unbranded) | 1 | Red | Medium | Named in 1 of 9 ("Togal.AI alternatives"), and low in the list (about 15th of 17 brands, or 8th of 9). For "PlanSwift alternatives 2026" Perplexity used Quotr's blog as a fact source but did not recommend Quotr. | [[quotr_ai_visibility_tests\|visibility notes §2]] |
| 14 | AI visibility: category discovery prompts | 1 | Red | High | Named in 0 of 15, re-confirmed in the fact-check re-runs (C1, C9, C11). Even Quotr's core differentiator prompt ("estimating software with material procurement") returned Buildertrend, Procore, Buildxact, esti-mate and ConWize. | [[verification_quotr_and_competitors\|verification notes, re-runs]] |
| 15 | AI visibility: problem / how-to prompts | 1 | Red | Medium | Named in 0 of 8. Cited once ("how accurate is AI takeoff": Quotr's article was the first source, but the brand was not named). A new test on LA fire rebuild costs also returned no Quotr, even though Quotr sells that exact estimate. | [[quotr_ai_visibility_tests\|visibility notes §3]]; [[verification_quotr_and_competitors\|verification notes]] |
| 16 | Content retrieval (quotr.ai pages used as sources) | 3 | Amber | High | quotr.ai was in the source list for 6 of 32 unbranded prompts (18.8%) and cited in the answer text in 4 (12.5%), tying for 15th among all cited domains. The content is being found; it is just not turning into brand mentions ("one outsourced estimating service charges $0.25/sq ft"). | [[quotr_ai_visibility_tests\|visibility notes §5]] |
| 17 | Share of voice vs competitors | 1 | Red | Medium | Quotr has about 0.7% of brand mentions across 32 unbranded prompts. STACK, PlanSwift and Buildxact have about 6.5% each; Togal.AI 5.2%; Procore, Bluebeam and Kreo about 4.6% each. | [[AI visibility baseline]] |

**Averages:** A (rows 1–6) = 18 / 6 = **3.0**. B (rows 7–11) = 7 / 5 = **1.4**. C (rows 12–17) = 10 / 6 = **1.7**. All 17 rows = 35 / 17 = **2.1**.

---

## Sub-scores worth tracking separately

### Community, by platform

| Platform | Score | Status on 2026-09-25 | Evidence |
|---|---|---|---|
| Reddit | 1 | No posts naming Quotr found in r/estimators, r/Construction or r/Contractor (Perplexity check; WebSearch cannot reach Reddit). Reddit r/estimators appeared in the sources of 6 of 32 test prompts. | [[quotr_offsite_presence\|offsite notes §3]]; [r/estimators thread](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/) |
| YouTube | 2 | Channel "QuotrAI" at youtube.com/@QuotrAI with a demo and an RL Electric customer video. The older handle Quotr lists (@QuotrIO) resolves to a channel titled "QuoTrio"; ownership TO CONFIRM with Quotr. Subscriber and view counts not retrieved. Never cited in 45 test runs. | [YouTube @QuotrAI](https://www.youtube.com/@QuotrAI); [demo video](https://www.youtube.com/watch?v=I0dsjz7Y_kc) |
| LinkedIn | 2 | Company page linkedin.com/company/quotrai (Perplexity reported about 1,077 followers; unverified). Quotr's /disambiguation/ page links a different slug (/company/quotrio). Founders have personal profiles. | [LinkedIn quotrai](https://www.linkedin.com/company/quotrai) |
| X (Twitter) | 1 | Two handles in use: @quotr_io (disambiguation page, podcast) and @quotr_ai (Product Hunt, PitchBook, homepage schema). Activity and followers not retrieved. | [[quotr_offsite_presence\|offsite notes §3]] |

### AI visibility, by prompt type (Perplexity Sonar, first runs)

| Prompt type | Prompts | Quotr named | quotr.ai cited in answer | quotr.ai in source list |
|---|---|---|---|---|
| Category discovery | 15 | 0 (0%) | 1 | 2 |
| Comparison / alternatives (unbranded) | 9 | 1 (11%) | 2 | 3 |
| Problem / how-to | 8 | 0 (0%) | 1 | 1 |
| **All unbranded** | **32** | **1 (3.1%)** | **4 (12.5%)** | **6 (18.8%)** |
| Brand prompts | 8 | 8 (100%) | 8 | 8 (5 of 8 with accuracy problems) |

Full per-prompt table: [[AI visibility baseline]].

---

## What would move each red or amber score up one point

| Area | Next step that would earn +1 | Where the plan lives |
|---|---|---|
| Technical readiness | Add the blog sitemap to robots.txt (or make a sitemap index); fix lastmod dates; update llms.txt; take test.quotr.io and quotr.io pages out of search indexes. | [[Website audit]] |
| Structured data | One Organization node (same name and legal name everywhere) on the homepage; SoftwareApplication + Offer on /software/ and /pricing/; FAQPage where FAQs are visible; real Person authors on posts. | [[Schema markup kit]] |
| Content depth | Publish original data (Quotr service jobs, procurement price vs market); deepen the priority trade pages; add residential cost pages. | [[Content priorities]] |
| Credibility | Named expert bylines with author pages; sources for every statistic; numbers in case studies; remove the investor testimonial or label it. | [[Page refresh checklist]] |
| Entity consistency | One fact sheet, copied to site, schema, llms.txt, blog boilerplate, Crunchbase, PitchBook, F6S, Product Hunt, LinkedIn. | [[Entity fact sheet]] |
| Reviews | 10–30 genuine G2 reviews; claim Capterra / GetApp / Software Advice listings. | [[Off-site earned media plan]] |
| List inclusion | Pitch accurate data and a demo account to editors of the lists AI engines cite most. | [[Citation sources map]] |
| Community | Founder-disclosed, helpful answers in r/estimators; one YouTube channel; one set of handles. | [[Off-site presence]] |
| Press | Wire release and trade-press pitch for the seed round plus a quantified customer result. | [[Off-site earned media plan]] |
| AI visibility and SOV | All of the above, then track monthly with the same prompt set. | [[Tracking set]] |

---

## How to re-score next month

1. Re-run the prompt set exactly as described in [[AI visibility baseline]] (same wording, same engine, plus any new engines you can access). Record which engines were used.
2. Re-check the facts in [[Website audit]] (robots.txt, llms.txt, sitemaps, schema, pricing on the ~13 stale URLs).
3. Re-check the platforms in [[Off-site presence]] (G2 review count, new list inclusions, press, Reddit).
4. Fill in the table below. Only change a score when the evidence changes. Keep the old column so the trend is visible.

| # | Area | 2026-09-25 | Next check | Change | Note |
|---|---|---|---|---|---|
| 1 | AI crawler access | 4 | | | |
| 2 | Technical readiness | 3 | | | |
| 3 | Structured data | 2 | | | |
| 4 | Content depth | 3 | | | |
| 5 | Structure / extractability | 4 | | | |
| 6 | Credibility on-site | 2 | | | |
| 7 | Entity consistency | 2 | | | |
| 8 | Review sites | 1 | | | |
| 9 | Third-party lists | 1 | | | |
| 10 | Community | 2 | | | |
| 11 | Press / PR | 1 | | | |
| 12 | Brand prompts | 3 | | | |
| 13 | Comparison prompts | 1 | | | |
| 14 | Category prompts | 1 | | | |
| 15 | How-to prompts | 1 | | | |
| 16 | Content retrieval | 3 | | | |
| 17 | Share of voice | 1 | | | |
| | **Overall** | **2.1** | | | |

**Baseline numbers to beat:** unbranded named rate 3.1% (1/32) · unbranded cited rate 12.5% (4/32) · in-source-list rate 18.8% (6/32) · SOV about 0.7% · G2 reviews 0 (reported, unverified) · independent list inclusions 0 (3 vendor/aggregator pages) · stale-price URLs about 13 plus llms.txt.

---

## Open questions (TO CONFIRM with Quotr)

- Is Cloudflare's "Block AI bots" / managed robots setting off? Is AI Labyrinth switched on on purpose? Server or Cloudflare logs for GPTBot, OAI-SearchBot, ClaudeBot and PerplexityBot would settle this.
- What does the G2 profile actually show (reviews, categories, name)?
- Which HQ, founding year, founder list and funding figure are correct? (See [[Entity fact sheet]].)
- Does Quotr have first-party AI data? GA4 AI referrals (e.g., `utm_source=chatgpt.com`, perplexity.ai referrers), Google Search Console's Generative AI performance report (AI Overviews / AI Mode impressions by page, available to all sites worldwide since Aug 31, 2026) and Bing Webmaster Tools' AI Performance report (Copilot citations). Any of these would add an impressions or traffic line to this scorecard.

---

## Related pages

- [[Website audit]] — full technical and content audit of quotr.ai
- [[Off-site presence]] — every third-party platform and mention found
- [[AI visibility baseline]] — per-prompt AI test results and method
- [[GEO tactics already used]] — what Quotr already does, with keep / improve / stop advice
- [[Entity fact sheet]] — the facts that should be consistent everywhere
- [[Competitor landscape]] — who wins AI answers instead
- [[KPIs and dashboard]] — how these scores feed the KPI dashboard
- [[30-60-90 plan]] — the action plan built on this baseline
