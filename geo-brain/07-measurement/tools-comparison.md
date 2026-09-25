# AI Visibility Tools Compared

**What this page is for:** A plain comparison of the tools that track how AI answer engines mention and cite brands, with prices where known, how well each fits a seed-stage company like Quotr, and a recommended setup that includes a free manual fallback.

**Last updated:** 2026-09-25 (prices seen on this date; they change often)

**Sources:** Research notes <../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md> (§4 tools table and seed-stage recommendation; §5 case studies), <../../research_notes/Quotr GEO AEO strategy audit/geo_ai_citation_signals_2026.md> (§2, §4 vendor data), <../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md> (section D: tool pricing and the Scrunch/Sitecore deal value were **not** re-checked; H14, H20; M10), <../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md> (§6 tracker sites). Pricing checks made on 2026-09-25 with web search: vendor pages [otterly.ai/pricing](https://otterly.ai/pricing) and [help.otterly.ai](https://help.otterly.ai/pricing-of-otterlyai), [peec.ai/pricing](https://peec.ai/pricing), [semrush.com/pricing/ai](https://www.semrush.com/pricing/ai/) and [Semrush KB](https://www.semrush.com/kb/1493-ai-visibility-toolkit), [ahrefs.com/brand-radar](https://ahrefs.com/brand-radar) and [Ahrefs pricing](https://ahrefs.com/pricing), [Similarweb AI Brand Visibility](https://aisearch.similarweb.com/ai-brand-visibility/); third-party review pages [Trakkr on Profound](https://trakkr.ai/reviews/profound-review/pricing), [Trakkr on Scrunch](https://trakkr.ai/reviews/scrunch-review/pricing), [Ryze on Peec](https://www.get-ryze.ai/blog/peec-ai-review-pricing-2026), [Ryze on Ahrefs Brand Radar](https://www.get-ryze.ai/blog/ahrefs-brand-radar-pricing-2026), [SE Ranking on Otterly](https://visible.seranking.com/blog/otterly-ai-review/), [EchoWi on Similarweb](https://echowi.ai/blog/similarweb-ai-search-review/). Full pages were not opened (the page reader was rate-limited); figures come from search-result extracts.

---

## 1. The short version

- **Start free.** Quotr can get most of what it needs in October 2026 from free tools (Google Search Console, Bing Webmaster Tools, GA4, Cloudflare) plus a monthly manual prompt check. Setup: [tracking-setup.md](tracking-setup.md).
- **Then add one low-cost tracker** when there is budget (roughly **$100–$250 a month**). **Otterly.AI** or **Peec AI** fit a seed-stage team best. Pick one after a free trial and stick with it for at least six months, so trends stay comparable.
- **Use Semrush or Ahrefs only if Quotr already pays for them.** Their AI add-ons are good value on top of an existing plan.
- **Skip enterprise tools for now** (Profound, Scrunch, Conductor, BrightEdge). They cost more than a seed-stage team needs.
- **Every price below needs a re-check before buying.** Most came from third-party review sites, and sources disagree. The research fact-check did not verify any tool prices ([verification §D](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>)).

---

## 2. What these tools do (and don't do)

**What they do.** An AI visibility tool (also called a prompt tracker) sends a fixed list of questions ("prompts") to AI engines on a schedule. It saves the answers and reports:
- **mention rate**: how often your brand is named;
- **citations**: which web pages the answer used as sources;
- **share of voice**: your share of brand mentions compared with named competitors;
- often **position** (where you appear in a list) and **sentiment** (positive, neutral or negative).

This is the same job as Quotr's manual monthly routine in [../04-prompt-library/tracking-set.md](../04-prompt-library/tracking-set.md), but automated and repeated more often.

**What they don't do.**
- **They don't see real users' answers.** Tools usually ask from clean sessions or through APIs (developer access). Real users get personalised answers. A 2026 study found that personalisation can change which brands ChatGPT and Gemini recommend ([visibility notes §6](<../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>)).
- **API answers can differ from the app.** Quotr's September baseline used Perplexity's Sonar API model, which may differ from the consumer Perplexity app ([report](<../../reports/Quotr GEO AEO strategy audit.md>)).
- **They don't measure traffic or sales.** For that you need GA4, Search Console, Bing Webmaster Tools and CRM data ([tracking-setup.md](tracking-setup.md)).
- **Different tools give different numbers** for the same brand, because they use different prompts, engines, run counts and scoring. Compare trends inside one tool, not numbers across tools.
- **Single runs mislead.** AI answers change a lot: Profound (a vendor) reports 40–60% of cited domains change month to month for the same question, and 2026 research papers argue for repeated sampling rather than one-off checks ([playbook §4](<../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md>); [verification M8](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>)).

**A note on vendor research.** Several tool makers also publish the studies used elsewhere in this brain. Examples: Profound (ChatGPT branded links, AI search volatility), Peec AI (30M-source citation study), Semrush (AI Visibility Index), Ahrefs (brand-visibility correlations), Similarweb (AI referral traffic), Promptwatch (Reddit citation drop in August 2026). Their data is useful, but they sell tools, so treat their headline claims as directional ([verification H14, H20](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>)).

---

## 3. Comparison table

Engine short names: **ChatGPT**; **AIO** = Google AI Overviews; **AI Mode** = Google AI Mode; **Gemini**; **Perplexity**; **Copilot** = Microsoft Copilot; **Claude**; **Grok**.

Prices are **per month in US dollars unless marked €**, as seen on 2026-09-25. "Check current pricing" means sources disagree or the figure came only from a third party.

| Tool | What it tracks | Engines covered (as reported) | Entry price and tiers (date, source) | Fit for a seed-stage company | Notes |
|---|---|---|---|---|---|
| **Otterly.AI** | Your own prompt list: brand mentions, citations, share of voice; GEO page audits | Base: ChatGPT, AIO, Perplexity, Copilot. Add-ons: AI Mode, Gemini (third-party review) | **Lite $29** (15 prompts) · **Standard $189** (100 prompts) · **Premium $489** (400 prompts); monthly or annual; free trial (vendor help pages, Sept 2026). Add-on engines reported at $9 / $59 / $149 by tier; extra 100-prompt packs on Standard and up (third-party). Research notes (2026 compilations): "from ~$29" | **Good.** Cheapest credible option. Lite is too small for Quotr's 53-prompt set; **Standard (100 prompts)** covers it with room | The playbook calls it "cheapest; lightweight monitoring for small teams". Publishes its own AI-search research (for example, how often ChatGPT searches the web) |
| **Peec AI** | Your own prompt list: visibility, position, sentiment, sources; competitor benchmarking | Choose 3 engines per plan from ChatGPT, Perplexity, AI Mode, AIO (vendor page); reviews also list Gemini and Copilot; extra engines are paid add-ons | **Starter** (50 prompts) · **Pro** (150) · **Advanced** (350) · Enterprise. Vendor page extract: **$95 / $245 / $495**. Third-party review (Aug 2026): **€85 / €205 / €425** monthly, lower on annual billing. Research notes: "~€89–199". **Check current pricing** | **Good.** Clean reporting; unlimited seats (vendor). Starter fits Quotr's 23 Tier A prompts; Pro fits all 53 | The playbook lists it as "mid-market and agencies". Peec published the 30M-source study showing Reddit as the most-cited domain across engines ([verification claim 16](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>)) |
| **Semrush AI Visibility Toolkit** | Custom prompts with daily tracking; brand mentions; AI competitor analysis; prompt research; AI-readiness site audit | ChatGPT, Google AI (AIO / AI Mode), Gemini, Perplexity (third-party review) | **$99 per month per domain** as an add-on to a Semrush plan (vendor KB); reported to include **25 custom prompts** (third-party). **Semrush One** (SEO + AI toolkits) from **$199** (vendor). **Check current pricing** | **Only if Quotr already uses Semrush.** 25 prompts covers roughly Tier A only | The playbook says it "fits teams already on Semrush". Semrush also publishes an AI Visibility Index (126M prompts) |
| **Ahrefs Brand Radar** | A large ready-made index of AI answers, so you can see any brand's AI visibility without writing prompts; custom prompts cost extra | AIO, ChatGPT, Perplexity and other indexes, including Grok (added April 2026) and newer AI indexes (vendor changelog) | Add-on to an Ahrefs plan. Vendor page extract: AIO, ChatGPT and Perplexity indexes **$99 each**, Grok $199, **all indexes $699**. Third-party reviews say **$199 per index** and $699 for all, with custom-prompt packs of $50–$250. **Check current pricing** | **Only if Quotr already uses Ahrefs.** Strong for benchmarking competitors (STACK, Togal.AI, Buildxact) across many questions | Ahrefs ran the 75,000-brand study linking brand and YouTube mentions to AI visibility (a correlation) |
| **Similarweb** (AI Brand Visibility; AI Chatbot Traffic) | Prompt-based brand visibility, plus **estimated AI referral traffic** to any website, including competitors, and the landing pages AI sends people to | Brand visibility: ChatGPT, AI Mode, Gemini, Perplexity. Traffic estimates also cover Claude, Copilot and Grok (vendor pages) | "AEO Intelligence" package reported at **$99 per month billed annually or $129 monthly** (150 prompts, 1 seat); larger bundles $399 and $649 (third-party review). **Check current pricing** | **Medium.** Useful to estimate competitors' AI traffic; traffic numbers are panel estimates, not Quotr's real data | Similarweb data is behind the market figure of 770.7M monthly AI referral visits, +117.4% year over year (June 2025–May 2026; not re-checked) |
| **Profound** | Enterprise AI visibility: prompts, citations, share of voice across many engines | Up to 9 engines on Enterprise (third-party) | Research notes (2026 compilations): "**from ~$499**, enterprise". A third-party review dated September 2026 says Profound **dropped its $99 Starter and $399 Growth plans in mid-September 2026**, leaving a limited free trial (10 prompts, ChatGPT only) and custom Enterprise pricing. **Unverified; check current pricing** | **Low for now.** Built and priced for large brands | Publishes widely cited studies (AI search volatility; ChatGPT branded links, May 2026) and vendor case studies such as Ramp (3.2% → 22.2% AI visibility in one month, March 2025, measured on Profound's own metric) ([verification H14](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>)) |
| **Scrunch** (now part of Sitecore) | Enterprise AI visibility: prompts, personas, page audits; crawler analytics reported | ChatGPT, Claude, Gemini, Perplexity, AIO (third-party) | Research notes: "**from ~$250**, enterprise-leaning". Third-party review (Aug 2026): Starter **$300 monthly or $250 annual** (350 custom prompts, 3 seats), Growth **$500 / $417** (700 prompts). **Check current pricing** | **Low–medium.** Capable but priced above a seed budget; long-term direction tied to Sitecore | Sitecore announced the acquisition in **June 2026**; Bloomberg reported about **$225M** ("said to"; not re-checked) ([Sitecore](https://www.sitecore.com/company/newsroom/press-releases/2026/06/sitecore-acquires-scrunch-to-help-brands-influence-discovery--and-buying-decisions); [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-03/sitecore-said-to-acquire-scrunch-for-225-million)) |

### Other tools and data sources mentioned in the research

| Name | What it is | Relevance to Quotr |
|---|---|---|
| **Promptwatch** | AI-visibility tracker; its data showed Reddit's share of ChatGPT citations falling from 3.83% to 0.52% in August 2026 | Alternative tracker; pricing not checked |
| **SE Ranking** | SEO suite; published the 300K-domain llms.txt study and ChatGPT referral reports; also sells an AI visibility tracker | Alternative if Quotr uses SE Ranking; not reviewed here |
| **Conductor**, **BrightEdge** | Enterprise SEO platforms that publish AI benchmarks (Conductor: AI referrals ~1.08% of traffic, 2025 data; BrightEdge: AI Overview prevalence) | Enterprise pricing; not needed now |
| **Muck Rack**, **Meltwater** | PR monitoring companies that publish AI-citation research ("What Is AI Reading?", May 2026; July 2026 AI visibility report) | Worth a look only if Quotr buys a PR tool for its press push |
| **Evertune** | Vendor with a 200M-prompt citation dataset | Enterprise; not needed now |
| **Trakkr, parse.gl, checkthat.ai** | Public "what AI recommends" pages by software category. They show Procore leading construction project-management answers (about 31–32% of AI mentions) | Free, directional look at a neighbouring category. Methods are opaque ([visibility notes §6](<../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>)) |

### Free first-party tools (use these first)

| Tool | What it gives | Cost |
|---|---|---|
| **Google Search Console, Generative AI performance report** | Impressions in AI Overviews and AI Mode by page, country, date and device. Worldwide since Aug 31, 2026. No clicks, CTR or queries | Free |
| **Bing Webmaster Tools, AI Performance** | How often Copilot and Bing AI answers cite Quotr's pages, which pages, and the "grounding queries" Copilot used. Public preview since February 2026 | Free |
| **GA4** (native AI Assistant channel + custom channel rule) | Visits and conversions from AI tools | Free |
| **Cloudflare AI Crawl Control** | Which AI crawlers visit quotr.ai, how often, which pages, and what response they get; allow or block per crawler | Included in Cloudflare |
| **Perplexity Sonar API** | The same model used for Quotr's September baseline, for like-for-like re-runs by script | Pay per use (check current pricing) |

How to set these up: [tracking-setup.md](tracking-setup.md).

---

## 4. How to choose (checklist for a trial)

Most trackers offer a free trial. Before paying, test the shortlisted tool against Quotr's own October manual run of the Tier A prompts ([tracking-set.md](../04-prompt-library/tracking-set.md)).

| Question | Why it matters for Quotr |
|---|---|
| Does it cover **ChatGPT, Google AI Mode, AI Overviews, Gemini and Perplexity**? What do extra engines cost? | These are the five monthly engines. Claude and Copilot can stay quarterly |
| Can it hold **53 prompts** (or at least the 23 Tier A prompts)? | The tracking set is fixed; you need room for all of it |
| Does it run each prompt **more than once** and show variation? | Brand order changes between runs; one run is a weak baseline |
| Does it save the **full answer text and all cited URLs**? | You need to spot "cited, not named" cases and third-party pages that name Quotr |
| Can you name **competitors** (STACK, PlanSwift, Buildxact, Togal.AI, Procore, Bluebeam, Kreo, Beam AI, Handoff) and get share of voice? | SOV is a core KPI ([kpis-and-dashboard.md](kpis-and-dashboard.md)) |
| Does it tell **Quotr.ai** apart from Quotr Pro, getquotr.com, quotrhq.com and "Quartr"? | Name collisions already confuse AI answers; a tool that counts the wrong "Quotr" inflates numbers |
| Can you **export** raw data (CSV or API)? | Keeps the history if you switch tools |
| Do its results **match your manual checks** on the same prompts, same week? | If not, find out why before trusting its trend lines |
| Is it priced by **prompts**, **engines**, **seats** or **domains**? | Compare the cost of the full 53-prompt, 5-engine setup, not the headline price |

---

## 5. Recommendation for Quotr

### Phase 1: now to November 2026 (cost: $0 plus about 3 hours a month)

1. Set up the free stack: Search Console Generative AI report, Bing AI Performance, GA4 AI channel with a Perplexity rule, Cloudflare AI Crawl Control, and a "How did you hear about us?" field ([tracking-setup.md](tracking-setup.md)).
2. Run the **Lite** manual routine each month: the 23 Tier A prompts in ChatGPT, Google AI Mode and Perplexity, once each, plus all 53 prompts twice through the Perplexity Sonar API for comparison with September ([tracking-set.md §3.3](../04-prompt-library/tracking-set.md)).
3. Record results in the spreadsheet template in [tracking-set.md §4](../04-prompt-library/tracking-set.md) and the dashboard in [kpis-and-dashboard.md](kpis-and-dashboard.md).

### Phase 2: from November or December 2026, if budget allows (about $100–$250 a month)

- **First choice: Otterly.AI Standard** (about $189 a month for 100 prompts, plus the AI Mode and Gemini add-on). It covers the whole 53-prompt set and the main engines at the lowest cost. **Check current pricing.**
- **Alternative: Peec AI Starter or Pro** (Starter about $95 or €85 for 50 prompts; Pro about $245 or €205 for 150 prompts; 3 engines included). Choose it if the team prefers its reports or needs unlimited seats. **Check current pricing.**
- Run both free trials in the **same week** as a manual check, and pick the one whose results match the manual runs best.
- Keep the **Perplexity Sonar API** re-run alongside any tool, so the September baseline stays comparable.

### Only if already licensed

- **Semrush customers:** add the AI Visibility Toolkit (about $99 per domain per month) and load the Tier A prompts.
- **Ahrefs customers:** add Brand Radar indexes for ChatGPT, AI Overviews and Perplexity to benchmark competitors across a large ready-made prompt set.

### Not now

- **Profound, Scrunch, Conductor, BrightEdge.** Revisit when AI becomes a measurable source of pipeline (see G2 and G5 in [kpis-and-dashboard.md](kpis-and-dashboard.md)), or if Quotr hires an agency that already licenses one.

### Rules that apply whatever tool is chosen

- **One tool, at least six months.** Switching tools breaks the trend line.
- **Keep engines separate** in every report.
- **Keep the manual check.** Spot-check 5 prompts by hand every month to catch tool errors and name mix-ups.
- **Tools don't replace first-party data.** Business results come from GA4, Search Console, Bing, forms and CRM.

The report lists budget for "a monthly AI-tracking tool" as an open question for the meeting. **Budget and owner: TO CONFIRM with Quotr.**

---

## 6. Cheap manual fallback (if no tool is bought)

This is enough to run Quotr's GEO measurement properly at seed stage.

| Step | What to do | Time (estimate) |
|---|---|---|
| 1 | Open a clean, logged-out or temporary session in each engine. Run from a US location | — |
| 2 | Paste each Tier A prompt exactly as written in [tracking-set.md](../04-prompt-library/tracking-set.md) into ChatGPT (with web search), Google AI Mode and Perplexity. Note whether Google shows an AI Overview for the same query | About 2 hours |
| 3 | Record: Quotr named (Y/N), position, how Quotr is described, quotr.ai URLs cited, competitors named, top cited domains, any third-party page naming Quotr, and a screenshot | Included above |
| 4 | Re-run all 53 prompts twice through the Perplexity Sonar API with a small script (a developer can set this up once) | Automated |
| 5 | Score with the formulas in [tracking-set.md §3.7](../04-prompt-library/tracking-set.md): mention rate, citation rate, retrieval rate, SOV, brand accuracy | About 30 minutes |
| 6 | Add Search Console, Bing, GA4 and form numbers to the dashboard | About 30 minutes |
| 7 | Quarterly: add Gemini, Claude and Copilot runs | Extra 2–3 hours per quarter |

Effort figures are this knowledge base's estimates. The **Standard** routine in [tracking-set.md](../04-prompt-library/tracking-set.md) (all prompts, four engines, two runs for Tier A) takes 10–15 hours by hand, which is the point where a paid tool starts to pay for itself.

---

## Related pages

- [kpis-and-dashboard.md](kpis-and-dashboard.md) — the KPIs these tools feed, baselines, targets and the monthly dashboard
- [tracking-setup.md](tracking-setup.md) — free first-party tracking setup (GA4, Search Console, Bing, Cloudflare, forms) and reporting cadence
- [../04-prompt-library/tracking-set.md](../04-prompt-library/tracking-set.md) — the 53 prompts to load into any tool
- [../02-current-state/ai-visibility-baseline.md](../02-current-state/ai-visibility-baseline.md) — the September 2026 baseline to compare against
- [../03-market/competitor-landscape.md](../03-market/competitor-landscape.md) — the competitors to add to share-of-voice tracking
- [../01-geo-fundamentals/myths-and-risks.md](../01-geo-fundamentals/myths-and-risks.md) — why vendor claims need care
