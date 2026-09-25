---
type: plan
description: The GEO KPIs, their September 2026 baselines, 90-day and 6-month targets, and a monthly dashboard.
aliases:
- KPIs
last_verified: 2026-09-25
verify_every_days: 30
---
# GEO KPIs and Monthly Dashboard

> [!abstract] What this page is for
> The numbers Quotr uses to judge whether its GEO/AEO work is paying off. It covers what each number means, where it comes from, its September 2026 starting value, suggested 90-day and 6-month targets, and a one-page dashboard to fill in every month.

> [!info]- Sources
> Final report [[Quotr GEO AEO strategy audit]] (measurement section, six-number scorecard, 90-day plan). Research notes [[quotr_ai_visibility_tests]] (baseline, §5), [[geo_content_playbook_b2b]] (§4 measurement, §5 case studies, §7 top of funnel), [[geo_ai_citation_signals_2026]] (§4–5 traffic), [[verification_geo_evidence]] (claims 3, 6, 7, 21, 24; H1, H14; M1, M8; O5) and [[verification_quotr_and_competitors]]. Brain files [[AI visibility baseline]], [[Presence scorecard]], [[Off-site presence]], [[Tracking set]], [[Traffic and funnel impact]].

---

## 1. The short version

- **What we are trying to move:** how often AI answer engines **name** Quotr.ai when buyers ask open questions, whether they describe Quotr **correctly**, and whether that turns into **visits, demos and signups**.
- **Where Quotr starts (September 2026, Perplexity only):** named in **1 of 32** unbranded buyer questions (3.1%), while STACK, PlanSwift and Buildxact were each named in 10. Share of voice about **0.7%**, against about 6.5% each for those three. **5 of 8** branded answers contained an error. Perplexity already reads Quotr's pages (quotr.ai was in the source list for 6 of 32 answers), but it drops the name.
- **What we don't know yet:** anything from ChatGPT, Google AI Overviews / AI Mode, Gemini, Claude or Copilot, and all of Quotr's own traffic data (GA4, Search Console, Bing, CRM). These are **TO CONFIRM with Quotr**. October 2026 is the first month with a full baseline.
- **How to read progress:** by engine, month over month, and as **3-month trends**. AI answers change a lot from month to month, so one good or bad month proves little.

**Words used on this page**

| Term | Plain meaning |
|---|---|
| **KPI** | Key performance indicator: a number we track to see if the work is working. |
| **Leading KPI** | An early signal that moves first (for example, being named in AI answers). |
| **Lagging KPI** | A business result that moves later (for example, demos booked). |
| **L1–L10, G1–G5** | Short codes for the leading (L) and lagging, business-goal (G) KPIs below. "G2" here is a KPI code, not the G2 review site. |
| **Named / mentioned** | The AI answer says "Quotr" or "Quotr.ai" in its text. |
| **Cited** | The AI answer uses a quotr.ai page as a source link. |
| **Retrieved** | A quotr.ai page is in the answer's source list, but the answer does not use it. |
| **Unbranded prompt** | A question that does not name Quotr, such as "best AI takeoff software for subcontractors 2026". |
| **Share of voice (SOV)** | Quotr's share of all brand names mentioned across a set of AI answers. |
| **Engine** | One AI answer product: ChatGPT, Google AI Mode, Google AI Overviews, Gemini, Perplexity, Claude or Copilot. |
| **AI referral** | A website visit that arrives from a link inside an AI tool. |

---

## 2. The KPI tree

The tree reads from top to bottom. Business results (top) depend on AI visibility (middle). AI visibility depends on inputs Quotr controls (bottom).

```
BUSINESS RESULTS (lagging)
├── G1 AI referral sessions (GA4)
├── G2 AI-referred demos and signups (GA4 key events + CRM)
├── G3 Branded search volume (Search Console)
└── G4 Self-reported "heard about us via ChatGPT / AI" (demo and trial forms)
        ▲
AI VISIBILITY (leading: what AI engines say)
├── L3 Mention rate on unbranded prompts (per engine)
├── L4 "Cited, not named" prompts turned into named ones
├── L5 Share of voice vs named competitors
├── L6 Accuracy of branded answers
└── L2 quotr.ai pages cited (tracking set + Search Console AI impressions + Bing AI citations)
        ▲
INPUTS AND PROOF (leading: what feeds AI engines)
├── L1 AI crawler access and hits (Cloudflare / server logs)
├── L7 Review count and rating (G2, Capterra, GetApp, Software Advice)
├── L8 Third-party list inclusions ("best of" lists AI cites)
├── L9 Fact consistency (stale prices and conflicting facts removed)
└── L10 Off-site mentions (press, YouTube, Reddit, LinkedIn)
```

Why this shape: the report found that Quotr's problem is not being read by AI but being **trusted and named** by it. Review sites fed 9 of 32 test answers, and independent "best of" lists fed most category answers. So reviews and list inclusions (bottom row) are the main levers for the mention rate (middle row) ([[Quotr GEO AEO strategy audit|report]]). Correct facts (L9) drive branded-answer accuracy (L6).

---

## 3. KPI definitions and September 2026 baseline

"Baseline" is the value on 2026-09-25. All AI-answer baselines come from **Perplexity Sonar (API model), one day**. Details and per-prompt results: [[AI visibility baseline]].

### 3.1 Leading KPIs (early signals)

| # | KPI | How to measure it (formula) | Tool / source | How often | September 2026 baseline |
|---|---|---|---|---|---|
| **L1** | **AI crawler access and hits** | (a) Do the AI search bots Quotr wants get normal pages (HTTP 200), not blocks or challenges? (b) Requests per month by bot. (c) Are key pages crawled (blog, /pricing/, fixed pages)? | Cloudflare AI Crawl Control or server logs ([[Tracking setup\|Tracking setup §5]]) | Weekly glance, monthly count | robots.txt lets every bot in (`User-agent: *` / `Allow: /`). Cloudflare's AI Labyrinth bot trap is on. Whether Cloudflare's "Block AI bots" setting is off, and actual bot hits, are **unknown (TO CONFIRM with Quotr)** ([[Website audit]]) |
| **L2** | **quotr.ai pages cited** | (a) Tracking set: unbranded prompts where a quotr.ai URL is cited in the answer ÷ unbranded prompts run. (b) Retrieval rate: prompts with quotr.ai anywhere in the source list ÷ prompts run. (c) Number of distinct quotr.ai pages cited. (d) Search Console AI impressions by page. (e) Bing AI citations by page | Monthly prompt tracking; Google Search Console Generative AI report; Bing Webmaster Tools AI Performance | Monthly | (a) **12.5%** (4 of 32). (b) **18.8%** (6 of 32); quotr.ai tied 15th among most-cited domains, level with reddit.com. (c) 5 pages in core prompts: [best-togal-ai-alternatives](https://quotr.ai/blog/best-togal-ai-alternatives/), [best-planswift-alternatives-2026](https://quotr.ai/blog/best-planswift-alternatives-2026/), [is-ai-takeoff-actually-accurate-yet](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/), [outsource-construction-estimating](https://quotr.ai/blog/outsource-construction-estimating/), [commercial-estimating-services](https://quotr.ai/blog/commercial-estimating-services/). (d) and (e) **TO CONFIRM with Quotr** |
| **L3** | **Mention rate on unbranded prompts** | Unbranded prompts where Quotr is named ÷ unbranded prompts run. Report **per engine** | Monthly prompt tracking ([[Tracking set]]) | Monthly | **3.1%** (1 of 32). By type: category discovery 0 of 15; comparison 1 of 9 ("Togal.AI alternatives", about 15th of 17 brands); how-to 0 of 8. Other engines: **no baseline yet** |
| **L4** | **"Cited, not named" converted** | Of the prompts where a quotr.ai page is a source but Quotr is not named, how many now name Quotr? | Monthly prompt tracking | Monthly | **3 prompts cited, not named** in the core set: C12 outsourced estimating price (reproduced by the fact-check), V3 PlanSwift alternatives and P5 AI takeoff accuracy (both from one session; the fact-check could not re-run them). Plus N2 plumbing estimating in the extension set; S9 (outsourced takeoff cost) also cited a Quotr page, but whether Quotr was named was not recorded ([[Tracking set]]). Converted: 0 |
| **L5** | **Share of voice vs named competitors** | Count each brand once per prompt when named. Quotr's count ÷ all brand mentions across the unbranded prompts | Monthly prompt tracking (or a tool, see [[AI visibility tools compared]]) | Monthly | **~0.7%** (1 of ~153 mentions). STACK, PlanSwift, Buildxact ~6.5% each; Togal.AI ~5.2%; Procore, Bluebeam, Kreo ~4.6% each |
| **L6** | **Accuracy of branded answers** | Brand prompts with at least one error from the checklist ÷ brand prompts run | Monthly prompt tracking; checklist in [[Tracking set\|Tracking set §3.6]] | Monthly | **5 of 8** had errors: stale "from $299.90" price (B4, V2); the unrelated Quotr Pro app's 37 ratings / 4.7 used as Quotr's (B3); Quotr listed 3rd of 4 "Quotr" apps (B5); funding conflict including a "$190K seed" figure (B6). "Quotr.ai pricing" (B2) was right but cited the staging site test.quotr.io |
| **L7** | **Review count and rating** | Number of genuine reviews and average rating, per site | G2, Capterra, GetApp, Software Advice profile pages | Monthly | G2 profile (`quotr-io`) reportedly **0 reviews** (Perplexity report; G2 blocked our tools, so unverified). **No** Capterra, GetApp or Software Advice listing found. Product Hunt: 0 upvotes. For comparison: Togal.AI 4.8 stars from 60 G2 reviews, Beam AI 4.9 from 30; STACK about 1,400 Capterra reviews ([[Quotr GEO AEO strategy audit\|report]]) |
| **L8** | **Third-party list inclusions** | Number of independent "best of", comparison or directory pages that name Quotr. Count separately: (a) any page; (b) pages AI engines cite repeatedly (list in [[Citation sources map]]) | Monthly prompt tracking ("3rd-party pages naming Quotr" field); manual checks | Monthly | (a) **3 pages**, none independent editorial: Nomic (Quotr 5th of 7; Nomic ranks itself first), Octopus Builds (2nd of 8; author ranks itself first; repeats old $299.90 price), ForesightIQ (sourced only from Quotr's blog). (b) **0**: not on Construction Coverage, The Digital Project Manager, ConstructConnect's 2026 guide, ContraVault or ConstructionPlacements (ConstructConnect's guide was read directly; the others were checked by site-restricted search because the pages could not be opened) |
| **L9** | **Fact consistency** | Count of Quotr-controlled URLs and profiles showing a retired or conflicting fact (price, HQ, funding, founders, factory count) | Site crawl or search; [[Entity fact sheet]] | Monthly until zero, then quarterly | Old $299.90 entry pricing on **about 13 Quotr URLs** (mostly blog posts, plus the old indexed copy of /contractors), and in llms.txt. HQ, funding, founders and factory count each appear in 2–3 versions ([[Quotr GEO AEO strategy audit\|report]]) |
| **L10** | **Off-site mentions** | New trade-press articles, YouTube videos and views, Reddit threads, LinkedIn articles that name Quotr | Google Alerts, YouTube Studio, manual search | Monthly | No trade-press coverage; no press release for the seed round; no Reddit threads naming Quotr found (Reddit could only be searched indirectly); Quotr has a YouTube channel, but Perplexity **never cited YouTube** in any of the 45 test runs; one marketing podcast episode with the CEO (March 2026) ([[Off-site presence]]) |

### 3.2 Lagging KPIs (business results)

| # | KPI | How to measure it | Tool / source | How often | September 2026 baseline |
|---|---|---|---|---|---|
| **G1** | **AI referral sessions** | Sessions from AI tools, by source (ChatGPT, Perplexity, Gemini, Copilot, Claude and others). Also as a share of all sessions, and by landing page | GA4 native "AI Assistant" channel **plus** a custom channel rule that also catches Perplexity ([[Tracking setup\|Tracking setup §1]]) | Weekly glance, monthly report | **TO CONFIRM with Quotr.** A custom GA4 channel group can be applied to past data, so the January–September 2026 history can be pulled on setup day. Outside reference only: Conductor put AI referrals at about 1.08% of all website traffic for enterprise sites (2025 data; not re-checked) |
| **G2** | **AI-referred demos and signups** | Key events (demo requests, trial signups) from the AI channel; AI channel conversion rate vs organic search | GA4 key events + CRM deal source | Monthly; conversion comparison quarterly | **TO CONFIRM with Quotr** (which events and CRM fields exist today is unknown) |
| **G3** | **Branded search volume** | Search Console clicks and impressions for queries containing "quotr" (or the branded-queries filter). Watch for namesake noise (Quotr Pro and others) | Google Search Console; Bing Webmaster Tools | Monthly; trend reviewed quarterly | **TO CONFIRM with Quotr** |
| **G4** | **Self-reported "heard about us via ChatGPT / AI"** | Share of demo and trial requests that pick an AI option in "How did you hear about us?" | Form field + CRM | Monthly | **No field found today (TO CONFIRM with Quotr)**, so no data |
| **G5** | **AI-sourced pipeline** (optional, from month 3) | Deals tagged AI-sourced (GA4 first touch or self-reported), their value and close rate | CRM | Quarterly | **TO CONFIRM with Quotr** |

**Why lagging numbers need care:** a buyer who reads "Quotr.ai" in a ChatGPT answer often searches the name later or types the URL. Analytics then records branded search or direct traffic, not AI. That is why G3 and G4 matter as much as G1 ([[Traffic and funnel impact]]). Also, clicks from Google AI Overviews and AI Mode arrive as ordinary Google organic traffic in GA4; only Search Console shows AI impressions, and it shows no AI clicks ([[Quotr GEO AEO strategy audit|report]]; [[Tracking setup|Tracking setup §2]]).

### 3.3 The report's six-number top-of-funnel scorecard

The report recommends tracking these six numbers every month as the simple view of top-of-funnel reach ([[Quotr GEO AEO strategy audit|report]]). They map onto the KPIs above.

| # | Scorecard number | KPI above |
|---|---|---|
| 1 | Share of AI answers that name Quotr | L3 (and L5) |
| 2 | AI impressions in Search Console | L2 (d) |
| 3 | Branded search volume | G3 |
| 4 | Review count | L7 |
| 5 | YouTube views | L10 |
| 6 | Demos that came from AI (GA4 plus self-reported) | G2 + G4 |

Keep total website sessions on the dashboard too, but not as the only top-of-funnel measure. AI summaries take clicks from educational pages, so traffic can fall while reach grows ([[Traffic and funnel impact]]).

---

## 4. Suggested targets (90 days and 6 months)

> **These targets are SUGGESTED by this knowledge base, not agreed with Quotr.** They are starting points for discussion. Set final targets after the October 2026 baseline adds ChatGPT, Google AI Mode / AI Overviews and Gemini, and after Quotr shares GA4, Search Console and CRM data.

- **90 days** = the day-90 review in **late December 2026** (the report's plan ends with a review at day 90).
- **6 months** = **late March 2027**.
- AI-answer targets use the **same 32 core unbranded prompts on Perplexity** as the baseline, so the comparison is like for like. With 32 prompts, **one prompt equals about 3 percentage points**, so a one-prompt change is within normal noise. Count a target as met only if it holds in **two monthly runs in a row**.

| # | KPI | Baseline (Sep 2026) | 90-day target (suggested) | 6-month target (suggested) | Why this level |
|---|---|---|---|---|---|
| L1 | AI crawler access | Unknown | All wanted AI search bots (OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot, Bingbot, Googlebot) get 200 responses on key pages; 0 blocked or challenged. Fixed pricing pages re-crawled by Googlebot and Bingbot | Same, plus new data and tool pages crawled within about 2 weeks of publishing | Access is a precondition; the report lists "confirm Cloudflare is not blocking AI search bots" as a day-1–30 task |
| L2 | Citation rate (Perplexity, core 32) | 12.5% (4/32) | Hold at 12.5% or better while duplicate pages are merged | 20% or more (7+ of 32) | AI already reads Quotr; merges may briefly shuffle which URL is cited. New unique assets (datasets, calculators) should add citations later |
| L2 | Search Console AI impressions / Bing AI citations | Unknown | Baseline recorded; 3 months of data | Rising 3-month trend; at least one new data or tool page among the top 10 pages by AI impressions | First-party data only exists from mid-2026 |
| L3 | Mention rate, unbranded (Perplexity, core 32) | 3.1% (1/32) | **9% or more (3+ of 32)** | **15% or more (5+ of 32)** | The three "cited, not named" prompts are the fastest wins: Quotr's page is already the source, so rewriting key sentences so the name travels with the fact could turn them into mentions. Getting beyond that needs reviews and list inclusions, which take months |
| L3 | Mention rate, other engines | No baseline | Set in November 2026 from the October baseline | Improve on October in at least 3 of the 4 monthly engines | Engines differ a lot; don't copy Perplexity targets |
| L4 | "Cited, not named" converted | 0 of 3 (plus N2) | At least 2 of C12, V3, P5 name Quotr | All 4 (C12, V3, P5, N2) name Quotr | Directly tests the "make the name part of the fact" fix ([[GEO writing style guide]]) |
| L5 | Share of voice (Perplexity, core 32) | ~0.7% | **~2% or more** (about 3 mentions) | **~3–4% or more** (about 5–6 mentions), close to Procore, Bluebeam and Kreo today (~4.6%) | Consistent with the mention-rate targets; STACK-level SOV (~6.5%) needs a large review and list footprint |
| L6 | Branded answers with errors | 5 of 8 | **2 of 8 or fewer.** No stale $299.90 entry price; no test.quotr.io citation; one funding figure | **1 of 8 or fewer** | The report's first proof point: once AI engines re-read the fixed pages, branded answers should quote $79.90. The Quotr Pro rating mix-up only fades as real Quotr reviews appear, so it may last longer |
| L7 | G2 reviews | ~0 (reported) | **10 or more genuine reviews** | **25–30 reviews**; Capterra / GetApp / Software Advice listings live under "Quotr.ai" | The report's review-drive goal is 10–30 honest reviews under G2's rules. Target the **count**, never the rating; ask all real customers, not only happy ones ([[Myths and risks]]) |
| L8 | Third-party lists naming Quotr | 3 (none independent); 0 repeatedly-cited lists | **2 or more** independent pages or directory categories that AI cites (for example F6S "AI-Assisted Takeoff" or SourceForge "AI takeoff"); Nomic and Octopus Builds show $79.90 | **5 or more** independent pages, including **at least 2** of the repeatedly-cited lists (Construction Coverage, TDPM, ConstructConnect, ContraVault, ConstructionPlacements) | These lists decide unbranded answers; outreach is a days-31–90 task in the report |
| L9 | Stale or conflicting facts | ~13 URLs + llms.txt with old prices; several facts in 2–3 versions | **0** stale-price URLs (a day-1–30 task in the report); one CEO-approved fact sheet used everywhere | 0, checked quarterly | Cheapest, fastest fix in the audit |
| L10 | Off-site mentions | No press, no Reddit, YouTube never cited | At least 1 trade-press pitch sent with the first dataset; founder posts started; YouTube series planned | At least 2 independent articles; YouTube series live; disclosed founder answers in r/estimators | Supports L3 and L5; proof from others is the main signal ([[Signals that matter]]) |
| G1 | AI referral sessions | Unknown | Baseline pulled (Jan–Sep 2026); monthly trend visible by source | About **double the October 2026 level** | Market reference only: Similarweb reported AI referral visits up 117.4% year over year (June 2025–May 2026; not re-checked). ChatGPT started linking brand names to homepages on May 7, 2026 (vendor data), which should help |
| G2 | AI-referred demos / signups | Unknown | Tracked as key events by channel; CRM field live | AI channel conversion rate compared with organic over one full quarter | The report says AI-visitor conversion for B2B is **unproven**: measure it, don't assume it |
| G3 | Branded search volume | Unknown | Baseline recorded (Oct–Dec 2026) | Rising 3-month trend (for example +25% vs the Oct–Dec 2026 average), after removing namesake queries | Being named in AI answers should show up as people searching "Quotr" later |
| G4 | Self-reported AI source | No field | Field live on demo and trial forms **within 30 days**; answered on 80% or more of demo requests | Share of AI answers tracked monthly and rising quarter over quarter | Quotr's own form data will be the best evidence of channel mix within 1–2 quarters (playbook inference) |

**About bigger numbers you may hear.** Vendor case studies report fast jumps, such as Ramp's AI visibility rising from 3.2% to 22.2% in one month. That figure is Profound's own metric on Profound's own prompt set, from March 2025, and is a vendor case study, not a benchmark ([[verification_geo_evidence|verification H14]]). No public GEO case study with numbers exists for construction tech ([[geo_content_playbook_b2b|playbook §5]]). The targets above are deliberately modest.

---

## 5. Reading the numbers without fooling yourself

| Rule | Why |
|---|---|
| **Report each engine on its own line.** Never blend engines into one score | Citations barely overlap across engines: one analysis found 91% of citations appear in only one of ChatGPT, Perplexity or AI Overviews (Kevin Indig, H1 2026; not re-checked) |
| **Look at 3-month trends, not single months** | Profound (a vendor) reports 40–60% of cited domains change month to month for the same question. A separate study found only about a third of cited pages were still cited 28 days later ([[Quotr GEO AEO strategy audit\|report]]) |
| **Run key prompts twice** | In the September tests, the source list stayed the same between runs but the order of brands changed. Position is noisy ([[AI visibility baseline\|AI visibility baseline §7]]) |
| **Keep the prompt wording fixed** | Changing words changes answers. Add new prompts; don't edit old ones ([[Tracking set\|Tracking set §5]]) |
| **Watch the control prompt (T43)** | It echoes Quotr's own marketing words. Being named there but not on plain buyer wording (T10, T14) is not real progress |
| **Don't add Search Console AI impressions to Web totals** | They are already inside the Web numbers; the AI report is a filtered view ([[verification_geo_evidence\|verification M1]]) |
| **Treat conversion claims as hypotheses** | Ahrefs saw AI visitors convert far better on its own site, but the only peer-reviewed study (973 online stores) found ChatGPT traffic converted below most traditional channels, with better results for complex products ([[verification_geo_evidence\|verification claim 24, H1]]). Measure Quotr's own numbers |
| **Separate correlation from cause** | Many GEO statistics (YouTube mentions, "cited pages get more clicks") are correlations. Use them to pick bets, not to promise results |
| **Log what changed** | Note each month which pages were fixed or published, and which tool or engine version was used. Otherwise you can't explain movements |

**When to act (suggested alert rules)**

| Signal | Action |
|---|---|
| Any wanted AI bot gets 403 / challenge responses | Fix Cloudflare settings the same week ([[Tracking setup\|Tracking setup §5]]) |
| An old error (for example $299.90) reappears in a branded answer | Search for the source page it cites and fix or request a correction |
| Mention rate falls on the same engine two months running | Check which cited sources changed; look for lost list placements or a competitor's new page |
| A new third-party page names Quotr | Log it in [[Off-site presence]]; check its facts; thank or correct the author |
| AI referral sessions jump or drop by half or more | Check the GA4 channel rules and ChatGPT link behaviour before celebrating or worrying |

---

## 6. One-page monthly dashboard (template)

Copy this block into a doc or spreadsheet each month. Fill the "This month" column, keep the baseline column fixed, and colour each row: **Green** = at or ahead of the target path; **Amber** = flat; **Red** = worse than last month or than baseline.

```
QUOTR GEO DASHBOARD — Month: ________   Prepared by: ________   Date run: ________
Engines run: [ ] ChatGPT  [ ] Google AI Mode  [ ] Google AI Overviews  [ ] Gemini  [ ] Perplexity (web)
             [ ] Perplexity Sonar API  [ ] Claude (quarterly)  [ ] Copilot (quarterly)
Prompts run: core 40 [ ]  extension 13 [ ]   Runs per Tier A prompt: ___   Tool used: ________
Changes this month that could affect numbers (pages fixed/published, tool or engine changes): ________

A. HEADLINE (3 lines max)
1. ________
2. ________
3. ________
```

**B. AI presence (one row per engine; Perplexity Sonar core 32 is the like-for-like line)**

| Engine | Mention rate (unbranded) | Citation rate | Retrieval rate | Cited-not-named (of C12, V3, P5, N2) | SOV | Branded answers with errors | vs last month | vs baseline | Status |
|---|---|---|---|---|---|---|---|---|---|
| Perplexity Sonar API (core 32) | | | | | | / 8 | | 3.1% · 12.5% · 18.8% · 0 of 4 · ~0.7% · 5/8 | |
| Perplexity (web app) | | | | | | / 8 | | no baseline | |
| ChatGPT (search) | | | | | | / 8 | | no baseline | |
| Google AI Mode | | | | | | / 8 | | no baseline | |
| Google AI Overviews (AIO shown on __ of __ prompts) | | | | | | / 8 | | no baseline | |
| Gemini | | | | | | / 8 | | no baseline | |

**C. First-party AI visibility and crawler health**

| Item | This month | Last month | Baseline | Notes |
|---|---|---|---|---|
| Search Console: AI impressions (AI Overviews + AI Mode), total | | | TO CONFIRM | Impressions only; no clicks |
| Search Console: top 5 pages by AI impressions | | | TO CONFIRM | |
| Bing: AI citations, total / cited pages | | | TO CONFIRM | Public preview report |
| Bing: top 5 grounding queries | | | TO CONFIRM | |
| AI crawler requests (OpenAI / Anthropic / Perplexity / Google / Microsoft) | | | TO CONFIRM | |
| Any wanted AI bot blocked or challenged? (Y/N) | | | Unknown | |

**D. Off-site proof**

| Item | This month | Last month | Baseline | Notes |
|---|---|---|---|---|
| G2 reviews (count / average rating) | | | ~0 (reported) | |
| Capterra / GetApp / Software Advice listed? | | | No | |
| Independent lists naming Quotr (total / new this month) | | | 0 independent | List the URLs |
| Repeatedly-cited lists naming Quotr (of 5) | | | 0 | |
| Trade-press articles naming Quotr (new) | | | 0 | |
| YouTube views (month) / new videos | | | TO CONFIRM | |
| Reddit / Facebook group / LinkedIn mentions (new) | | | 0 found | |
| Stale-price URLs remaining | | | ~13 + llms.txt | |

**E. Traffic and pipeline**

| Item | This month | Last month | 3-month trend | Notes |
|---|---|---|---|---|
| AI referral sessions (custom channel), total | | | | |
| … by source: chatgpt.com / perplexity.ai / gemini / copilot / claude / other | | | | |
| AI sessions as % of all sessions | | | | |
| Top landing pages from AI (homepage share) | | | | |
| AI-referred demo requests / trial signups (GA4 key events) | | | | |
| AI channel conversion rate vs organic search | | | | Quarterly comparison |
| Branded search clicks / impressions (Search Console, "quotr" queries) | | | | Note namesake noise |
| "How did you hear about us?" — AI answers / all answers | | | | |
| AI-sourced deals in CRM (count / value) | | | | From month 3 |

**F. Accuracy watch list (branded answers, any engine)**

| Known error | Seen this month? (engine) | Source page cited | Fix owner |
|---|---|---|---|
| Entry price "from $299.90" / Solo / Team plans | | | |
| Quotr Pro app ratings (37 ratings, 4.7) used as Quotr's | | | |
| test.quotr.io or other staging host cited | | | |
| Funding "$190K" or conflicting amounts | | | |
| Factory count "50+ to 220+" | | | |
| Described as Revit tool or "not software" | | | |
| Mixed up with Quotr Pro, getquotr.com, quotrhq.com, Quartr | | | |

**G. Actions**

```
What we shipped last month (pages fixed, published, reviews requested, pitches sent):
1.
2.
What we expect to move next month, and which prompts should show it:
1.
2.
Decisions or help needed from Quotr leadership:
1.
```

### Example: the baseline column filled in (September 2026)

| KPI | Value |
|---|---|
| Perplexity Sonar, core 32 unbranded: mention / citation / retrieval | 3.1% / 12.5% / 18.8% |
| Cited, not named | C12, V3, P5 (+ N2) |
| SOV | ~0.7% (STACK, PlanSwift, Buildxact ~6.5% each) |
| Branded answers with errors | 5 of 8 |
| G2 reviews | ~0 (reported, unverified) |
| Independent lists naming Quotr | 0 (3 vendor or aggregator pages) |
| Stale-price URLs | ~13 + llms.txt |
| Presence scorecard overall | 2.1 / 5 ([[Presence scorecard]]) |
| GA4, Search Console, Bing, CRM, form data | TO CONFIRM with Quotr |

---

## 7. Which lever moves which KPI

| If this KPI is weak… | …the main levers are | Where the plan lives |
|---|---|---|
| L6 branded accuracy | One fact sheet; fix ~13 stale-price URLs and llms.txt; rewrite /disambiguation/; request re-crawl; ask Nomic and Octopus Builds to update | [[Entity fact sheet]], [[Optimize vs create]] |
| L4 cited, not named | Rewrite key sentences so "Quotr.ai" travels with each fact on pages AI already cites | [[GEO writing style guide]], [[Page refresh checklist]] |
| L3 / L5 mention rate and SOV | Reviews, independent list inclusions, YouTube, community answers, press | [[Off-site earned media plan]], [[Citation sources map]] |
| L2 pages cited on top-of-funnel topics | Original data (factory-direct price index, cost per sq ft), free calculators | [[Content priorities]], [[White space]] |
| L1 crawler access | Cloudflare settings, sitemaps in robots.txt, real "last updated" dates | [[Tracking setup]], [[Website audit]] |
| G1–G4 business results | Homepage that converts first-time AI visitors (ChatGPT now links brand names to homepages); clear demo and trial paths; the "How did you hear about us?" field | [[Traffic and funnel impact]], [[Top-of-funnel strategy]] |

---

## 8. Open questions (TO CONFIRM with Quotr)

- GA4: is it installed on quotr.ai and the app sign-up flow? Which events are marked as key events (demo request, trial signup, contact)?
- Search Console and Bing Webmaster Tools: are quotr.ai and quotr.io verified? Who has access?
- CRM: which system, and is there a lead-source field?
- Forms: which tool runs /book-demo/, /contact-us/ and /sign-up? Can a required "How did you hear about us?" field be added?
- Cloudflare: who owns it, and is "Block AI bots" off?
- Budget and owner for a monthly AI-tracking tool (the report's meeting question on budget).
- Do any past demos or signups mention ChatGPT or Google AI? (Report meeting question.)
- Who owns this dashboard each month, and who receives it?

---

## Related pages

- [[Tracking setup]] — step-by-step setup of GA4, Search Console, Bing, crawler logs, forms and the monthly routine
- [[AI visibility tools compared]] — AI visibility tools, prices and the recommended setup for a seed-stage team
- [[Tracking set]] — the 53 prompts to re-run every month, with scoring rules and templates
- [[AI visibility baseline]] — the full September 2026 baseline
- [[Presence scorecard]] — the 17-area scorecard to re-score each month
- [[Traffic and funnel impact]] — why reach is now measured as presence, not just clicks
- [[30-60-90 plan]] — the plan these targets track
- [[Entity fact sheet]] — the correct facts for checking branded answers
