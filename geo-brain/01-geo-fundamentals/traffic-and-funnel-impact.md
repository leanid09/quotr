# Traffic and Funnel Impact of AI Search

**What this page is for:** What AI answers do to clicks, how much traffic AI engines send and how well it converts, what this means for B2B software buyers, what "top of funnel" means now, and how Quotr.ai should think about keeping and growing its top-of-funnel reach.

**Last updated:** 2026-09-25

**Sources:** Research notes [geo_ai_citation_signals_2026.md](<../../research_notes/Quotr GEO AEO strategy audit/geo_ai_citation_signals_2026.md>) (§4, §5), [geo_content_playbook_b2b.md](<../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md>) (§4, §5, §6, §7), corrected by [verification_geo_evidence.md](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>) (claims #5–#8, #21–#28; H1, H8, H13–H15, H17–H18; O1–O7; M1–M5, M9; these override the notes); the report [Quotr GEO AEO strategy audit.md](<../../reports/Quotr GEO AEO strategy audit.md>) (section "Top-of-funnel reach now means being named, not just clicked"). Studies are linked where used.

---

## Words used on this page

| Word | Plain meaning |
|---|---|
| **CTR (click-through rate)** | The share of people who see a result and click it. |
| **Zero-click search** | A search where the person gets what they need on the results page and clicks nothing. |
| **Referral traffic** | Visits that arrive by clicking a link on another site or app (here: from ChatGPT, Perplexity and so on). |
| **Conversion** | A visitor doing something valuable: booking a demo, starting a trial, buying. |
| **Top / middle / bottom of funnel (TOFU / MOFU / BOFU)** | Early research ("how do I estimate drywall?") / comparing options ("best AI takeoff software") / ready to buy ("Quotr.ai pricing"). |
| **Share of voice** | Of all the brand names AI answers mention for a set of questions, the share that are yours. |
| **Self-reported attribution** | Asking buyers "How did you hear about us?" instead of relying only on analytics. |
| **Percentage points (pp)** | The plain difference between two percentages (from 30% to 20% is −10 pp). |

---

## The short version

1. **AI answers take clicks away.** The first randomized experiment (Aug 2026, preprint) found Google's AI Mode cut clicks to outside websites by **18.8 percentage points**; removing AI Overviews **raised** clicks by 8.8 points. Observational studies agree: fewer clicks where AI summaries appear.
2. **Most Google searches already end without a click:** about **68%** in the US in Jan–Apr 2026 (SparkToro).
3. **Being cited helps but does not undo the loss.** Pages cited in an AI Overview got 120% more clicks per impression than uncited ones, but still 38% fewer than on searches with no AI Overview (Seer, correlation).
4. **AI referral traffic is small but growing fast:** about 1% of site traffic in most datasets (higher in IT), ~770M visits a month worldwide, +117% a year (Similarweb). ChatGPT's May 2026 branded links sent B2B software referrals up sharply (Profound, vendor).
5. **Does AI traffic convert better? Unproven for B2B.** One SaaS company's own data says yes (Ahrefs); the only peer-reviewed study (973 online stores) says ChatGPT traffic converts below most traditional channels, but better for complex products.
6. **B2B buyers are using AI to shortlist.** G2's own survey: 51% of software buyers start research in a chatbot more often than Google (G2 is an interested party).
7. **Top of funnel now means "being named in the answer",** then brand search, direct visits and self-reported attribution, not only blog sessions.
8. **For Quotr:** show up by name on topics no rival owns (factory-direct, tariffs, cost benchmarks), build assets people still click (tools, datasets, video), be present on the third-party sites AI reads, and measure presence, not just sessions.

---

## 1. What AI answers do to clicks

### 1.1 Causal evidence (the strongest)

- **"AI in Search Reduces Publisher Referrals Without Improving User Experience: Experimental Evidence"** (arXiv 2608.18352, **Aug 18, 2026**; University of Pennsylvania and Northeastern). A preregistered field experiment with about 1,100 Google users (956 completed the survey).
  - Putting people into **AI Mode** cut external click-through by **18.8 percentage points** (95% CI −22.2 to −15.3).
  - **Removing AI Overviews** raised click-through by **8.8 pp**.
  - Neither AI Mode nor AI Overviews improved perceived usefulness or trust.
  - It is a **preprint, not yet peer-reviewed**. [arXiv](https://arxiv.org/pdf/2608.18352v1); [SEJ](https://www.searchenginejournal.com/research-shows-google-ai-mode-sends-less-clicks-is-a-poor-user-experience/590221/)
- **Why it matters:** earlier studies could only show that clicks were lower where AI appeared. This one shows the AI features themselves cause the drop.

### 1.2 Observational CTR studies

| Study | Date and sample | Finding | Quality notes |
|---|---|---|---|
| **Pew Research Center** | Published July 22, 2025; 900+ US adults, 68,879 Google searches, **March 2025** | Clicked a link on **8%** of visits with an AI summary vs **15%** without; only **1%** clicked a link inside the summary; sessions ended on 26% of pages with a summary vs 16% without | Independent. **Dated:** before AI Mode reached 1B users and before Gemini 3 in AI Overviews. Not re-read by the fact-check. [Pew](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) |
| **Ahrefs** | Dec 2025 data, 300K keywords (published Feb 2026) | AI Overviews cut position-1 CTR by **58%** | Vendor, observational. Replaces its own April 2025 figure (34.5%). [Ahrefs](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/) |
| **Seer Interactive (2026 update)** | Apr 24, 2026; 53 brands, 5.47M queries, 2.43B impressions, Jan 2025–Feb 2026 | Organic CTR on AI Overview queries fell from 3.19% (Jan 2025) to 1.31% (Dec 2025), then rebounded to 2.36% (Feb 2026), still below the start. On informational queries **without** an AI Overview, organic CTR **rose** (2.93% → 3.97%) | Agency data; read by the fact-check. [Seer](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update) |
| **Seer (2026) on being cited** | Same dataset | Cited = **+120%** organic clicks per impression vs not cited, but **−38%** vs queries with no AI Overview (informational) | Seer: "We cannot claim causation. Higher-authority brands are also more likely to be cited." (The "+35% organic / +91% paid" figure in some notes is **not** in this update; don't use it.) |
| **Seer (Sept 2025 update)** | Informational-only cohort, 42 organisations | 1.76% → 0.61% | **Don't compare** with the 2026 figures (different dataset; also the drop is 65%, not the "61%" often quoted). [Seer](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update) |
| **Semrush (AI Mode)** | May 1–July 5, 2025; 69M US desktop sessions | **93%** of AI Mode sessions ended with no external click, vs 83% with an AI Overview and ~60% for standard search | Vendor; label as **mid-2025**. [Semrush](https://www.semrush.com/blog/google-ai-mode-seo-impact/) |

### 1.3 Zero-click searches

- **SparkToro (2026):** **68.01%** of US Google searches ended without a click in Jan–Apr 2026 (Similarweb panel), up from 60.45% in 2024. "Less than one-third of Google searches still send a click." The 2024 figure may come from a different data provider, so the comparison is approximate ([SparkToro](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/); 68.01% confirmed by the fact-check).

### 1.4 Which searches get an AI answer

- **By intent (Seer, 2026):** "X vs Y" comparison queries trigger an AI Overview **95.4%** of the time, "best of" 81.3%, price/cost 83.4%. Only 36% of informational, 8% of commercial and 5% of transactional queries show one ([Seer](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update)).
- **Overall prevalence** varies hugely by tracker and method (compilations of vendor data; [Searchlab](https://searchlab.nl/en/statistics/ai-overviews-sge-statistics-2026); [SERPs.io](https://serps.io/blog/ai-overview-prevalence-by-industry)):

| Tracker | When | Share of queries with an AI Overview |
|---|---|---|
| Semrush | Jan 2025 | 6.49% |
| Semrush | Jul 2025 (peak) | ~25% |
| Semrush | Nov 2025 | 15.69% |
| Conductor | Q1 2026 (21.9M queries) | 25.11% |
| BrightEdge | Mar 2026 (9 industries) | 48% |
| Xponent21 | Apr 2026 (US) | 60.32% |

  B2B tech and education reportedly crossed 80%; shopping keywords sit at 13–14%.
- **Scale:** Google said at I/O (May 19, 2026) that **AI Mode passed 1 billion monthly users** and **AI Overviews reached 2.5 billion**; the two became one flow ([Google](https://blog.google/products-and-platforms/products/search/search-io-2026/)).

### 1.5 Google's position

- Liz Reid (Aug 2025): "total organic click volume from Google Search to websites has been relatively stable year-over-year" and "average click quality has increased" ([Google blog](https://blog.google/products-and-platforms/products/search/ai-search-driving-more-queries-higher-quality-clicks/)). Google later pushed a "bounce clicks" explanation ([SEJ](https://www.searchenginejournal.com/google-pushes-bounce-clicks-explanation-for-ai-overview-traffic-loss/572986/)). Google has published no data outsiders can test ([Press Gazette](https://pressgazette.co.uk/platforms/google-search-clicks-traffic-2025-ai-overviews/)).
- **New reporting (2026):** Search Console's Generative AI performance reports (worldwide since Aug 31, 2026) show **impressions** from AI Overviews, AI Mode and Discover's generative features by page, country and date, but **no clicks, CTR or queries**. The data is a filtered view of Web data, so don't add it to Web totals. The UK CMA wants click data and page-level opt-out controls by March 2027 ([SEJ](https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/); [Google](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports); [verification M1](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>)).

---

## 2. AI referral traffic: how much

| Data point | Source | Notes |
|---|---|---|
| **770.7M** AI referral visits a month worldwide (Jun 2025–May 2026), **+117.4%** year on year | Similarweb ([Similarweb](https://www.similarweb.com/blog/marketing/geo/gen-ai-stats/)) | Vendor; not re-checked |
| AI referrals = **1.08%** of all website traffic, growing ~1% a month; IT sector ~**2.80%**; ChatGPT = 87.4% of AI referrals | Conductor 2026 AEO/GEO Benchmarks (13,770 enterprise domains, 3.3B sessions; released Nov 13, 2025) ([Conductor](https://www.conductor.com/academy/aeo-geo-benchmarks-report/)) | Vendor; the ChatGPT share is **2025 data** and outdated |
| AI search = **0.5%** of Ahrefs' own visits (up from 0.3%) | Ahrefs ([Ahrefs](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/)) | One company's first-party data |
| ChatGPT referrals **< 0.2%** of total traffic, ~**200x smaller** than Google organic, across 973 online stores | Kaiser & Schulze coverage ([Search Engine Land](https://searchengineland.com/llms-google-referral-conversion-study-463747)) | From coverage of the working paper |
| **ChatGPT branded links (May 7, 2026):** OpenAI referrals to monitored brands nearly doubled (~60–65%); homepage share ~3.5% → ~24%; **B2B software & SaaS the biggest gainer, daily OpenAI referrals up >200%**; ecommerce flat | Profound (published May 19, 2026) ([Profound](https://www.tryprofound.com/blog/chatgpt-referrals-branded-links)) | Vendor; read by the fact-check. OpenAI "can move this number again at any time" (Profound). Similarweb ("near triples") and SE Ranking ("all-time high in May 2026") point the same way, not re-checked |
| ChatGPT referred **4.8%**, then **10%**, of Vercel's new signups | Guillermo Rauch on X, Mar 7 and Apr 9, **2025** ([X](https://x.com/rauchg/status/1898122330653835656); [X](https://x.com/rauchg/status/1910093634445422639)) | Founder statements; early 2025; a developer-tool audience |
| Google organic still **47–190x** larger than AI referrals; ChatGPT 62.6% / Claude 18.5% / Gemini 10.6% / Perplexity 7.3% of B2B AI referrals | Aggregators ([Demand Local](https://www.demandlocal.com/blog/ai-referral-traffic-conversion-rate-statistics/)) | **Primary sources not found. Don't headline** ([verification H17](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>)) |

**Which assistants are growing:** ChatGPT's share of AI-assistant web traffic fell from about 76% (June 2025) to about 53% (May 2026) as Gemini passed 25% and Claude grew fastest (Similarweb; not re-checked). This measures traffic **to** the assistants, not referrals **from** them to websites ([verification X13](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>)).

**Plain English:** AI engines send a small slice of traffic today, but it is growing, and since May 2026 a ChatGPT mention of a brand name can link straight to its homepage.

---

## 3. Does AI referral traffic convert better? (Contested)

| Evidence | Direction | Quality |
|---|---|---|
| **Ahrefs' own site:** AI search was 0.5% of visits but **12.1% of signups**, about **23x** organic's conversion rate; AI visitors viewed 50% more pages ([Ahrefs](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/)) | Better | One SaaS company, first-party. Not re-checked. Ahrefs separately found AI visitors visit fewer pages and bounce more ([Ahrefs](https://ahrefs.com/blog/ai-traffic-quality-study/)), which conflicts |
| **Semrush:** an AI visitor is worth **4.4x** an organic visitor; AI search could overtake traditional search by 2028 ([Semrush](https://www.semrush.com/blog/ai-search-seo-traffic-study/)) | Better | **A model/projection published June 2025**, not observed conversions |
| "Opollo: 312 B2B firms, 14.2% vs 2.8%"; "ChatGPT 15.9%, Perplexity 10.5%, Claude 5.0%" | Better | **Primary sources not verified.** Don't use |
| Webflow (8% of signups, 6x), TestRail, Discovered Labs, Capston, Gumlet, REsimpli | Better | Agency self-reports or untraceable; **don't use** ([verification H13](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>)) |
| **Kaiser (U. Hamburg) & Schulze (Frankfurt School), "Frontiers: ChatGPT Referrals to E-Commerce Websites", *Marketing Science*** (peer-reviewed; published online **Apr 21, 2026**; 973 e-commerce sites, $20B revenue, 12 months, 50K+ ChatGPT transactions vs 164M from other channels) | **Worse, but improving** | The most rigorous study. ChatGPT traffic's conversion rate and revenue per session are "above paid social but below all other traditional channels"; results are **stronger in complex product categories**; conversion is rising over time; the channel "does not yet function as a broad conversion channel". (Figures of "−13% vs organic" and "affiliate 86% more likely" come from coverage of the working paper, not the abstract.) [INFORMS](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0489); [Digiday](https://digiday.com/marketing/e-commerce-sites-see-low-sales-from-chatgpt-traffic-new-study-finds/) |

**Verdict (fact-check H1):** "Unproven for B2B. Measure it in Quotr's own GA4 and CRM." Construction software is a complex, considered purchase, which the peer-reviewed study suggests is the kinder case, but this has not been tested for B2B.

---

## 4. B2B implications: how software buyers use AI

### 4.1 B2B software buyers in general

**G2, "The Answer Economy"** (surveyed March 2026, published April 2026; 1,076 B2B software buyers in North America, EMEA and APAC). **G2 is an interested party:** it sells reviews, and "review sites matter" helps it ([G2](https://company.g2.com/news/g2-research-the-answer-economy); [PR Newswire](https://www.prnewswire.com/news-releases/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots-302742807.html)).
- **51%** start software research in an AI chatbot more often than in Google (up from 29% in April 2025); 71% use chatbots somewhere in research.
- **69%** chose a different vendor than planned because of chatbot guidance; about **one-third** bought from a vendor they had never heard of before.
- **85%** think more highly of a vendor mentioned by AI.
- **45%** say a review-site citation is the most confidence-inspiring signal in an AI answer (50% of daily power users).
- ChatGPT is the dominant chatbot for this research (**63%**).
- 40% say evaluation is now the longest stage.

**Counter-evidence to keep beside it:** Growth Memo's G2-commissioned study found user-generated content out-cites review sites at every buyer stage, and Aleyda Solis's SaaS data puts news/review at about 10% of top sources ([verification H10](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>)).

### 4.2 Construction buyers specifically

- **AI use is rising:** 52% of construction firms use AI tools for business tasks, +20 points vs 2025; 80% of users use AI daily; top use is sales and marketing, 64% (Houzz, 601 US construction and design businesses, June–July 2026; via [Roofing Contractor](https://www.roofingcontractor.com/articles/102644-ai-use-jumps-among-construction-firms-houzz-survey-finds)). 61% of firms use AI or plan to increase investment; 23% use it for estimating (AGC/Sage, Jan 2026; [AGC](https://www.agc.org/news/2026/01/08/contractors-have-dampened-expectations-2026-apart-data-centers-and-power-projects-amid-worries-about)). 24% apply AI to cost estimation and 22% to bid management (ServiceTitan, 1,000+ commercial specialty contractors, Mar 30, 2026; vendor; [ServiceTitan](https://www.servicetitan.com/press/servicetitan-report-finds-ai-adoption-more-than-doubles-among-commercial)).
- **Trust is mixed:** data accuracy (57%) and security (54%) are top concerns (Dodge + CMiC, 235 contractors, Dec 2025; [Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/)); construction leaders' trust in AI fell 14 points (Autodesk, 2025; [Autodesk](https://www.autodesk.com/blogs/construction/state-of-design-make-spotlight-construction/)).
- **Gap:** no construction-specific survey measures how often contractors use AI chatbots to research **software** ([playbook §6](<../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md>)). No construction-specific CTR or AI-referral benchmark was found either.
- **Where estimators talk:** r/estimators threads ask whether AI takeoff tools work and are sceptical ([example thread](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/)). Facebook estimator groups, YouTube demos and trade shows are commonly named discovery venues, but no survey quantifies their share.

More on personas: [../00-quotr/audiences-and-personas.md](../00-quotr/audiences-and-personas.md).

### 4.3 What this means for B2B marketing (in plain words)

- Shortlists are increasingly formed **inside** the AI answer. If a brand is not named there, the buyer may never visit its site.
- Educational ("how do I…") content loses the most clicks, because AI summarises it. Comparison and pricing questions almost always show an AI Overview.
- Buyers still click when they need to **do** something (use a calculator, download a template, check live prices, book a demo) or **verify** something (original data, proof, reviews).
- Being the brand the AI names first matters: in one small AI Mode user study, 74% of participants chose the brand ranked first in the AI answer (Indig; sample size not captured; [Kevin Indig](https://substack.com/@kevinindig/note/c-298265127)).

---

## 5. What "top of funnel" means now

| | Old model (2024) | New model (2026) |
|---|---|---|
| Goal | Rank for educational keywords and get the click | **Be named** (and cited) when buyers ask AI early questions, then be remembered |
| Main metric | Organic sessions to blog posts | Share of AI answers that name Quotr, plus AI impressions in Search Console and Bing citations |
| Proof it worked | Traffic up | Branded search up, direct visits up, "heard about you from ChatGPT/Google AI" on demo forms, AI referrals that convert |
| Content that wins | Long generic guides | Original data, tools, decision support, honest comparisons, video; generic definitions only as short support pages |
| Where it happens | Your blog | Your site **and** the third-party pages AI reads (reviews, lists, YouTube, Reddit, LinkedIn, press) |

**Why brand search and direct traffic rise (inference):** a buyer reads "Quotr.ai" in an answer, then later searches the name or types the URL. Analytics records that as branded search or direct traffic, not as AI. That is why self-reported attribution matters. Growth Memo puts it this way: "visibility, not raw referral traffic, is becoming the main currency of organic search" ([Growth Memo](https://www.growth-memo.com/p/community-signals-are-ais-largest)).

### How to measure the new top of funnel

| Measure | Tool | Notes |
|---|---|---|
| Share of AI answers naming Quotr (by engine) | Monthly prompt tracking, 2+ runs per prompt, six engines | [../04-prompt-library/tracking-set.md](../04-prompt-library/tracking-set.md) |
| AI impressions per page | Search Console Generative AI performance report | Impressions only; no clicks. Don't add to Web totals |
| AI citations and grounding queries | Bing Webmaster Tools AI Performance (public preview since Feb 10, 2026) | Copilot and Bing AI answers ([Bing](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)) |
| AI referral sessions and conversions | GA4 "AI Assistant" default channel (added May 13, 2026) **plus** a custom channel rule that also catches Perplexity (not included in Google's channel) | Regex below, placed above Referral ([Google](https://support.google.com/analytics/answer/9164320); [playbook §4](<../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md>)). ChatGPT tags links with `utm_source=chatgpt.com` |
| Branded search volume | Search Console (queries containing "quotr") | Watch for namesakes (Quotr Pro etc.) |
| Self-reported attribution | "How did you hear about us?" on demo and trial forms | Options: ChatGPT, Google AI, YouTube, Reddit, Facebook group, other |
| Off-site proof | Review counts, list inclusions, YouTube views | Leading indicators |

Example source regex for the custom GA4 AI channel (Admin → Data display → Channel groups; drag the AI rule above Referral, because rules run top to bottom):

```
chatgpt\.com|chat\.openai\.com|perplexity\.ai|gemini\.google\.com|copilot\.microsoft\.com|claude\.ai
```

Setup details: [../07-measurement/tracking-setup.md](../07-measurement/tracking-setup.md); KPIs: [../07-measurement/kpis-and-dashboard.md](../07-measurement/kpis-and-dashboard.md).

---

## 6. How Quotr should think about keeping and growing top-of-funnel reach

### 6.1 Quotr's starting point

- **AI already reads Quotr, but rarely names it.** quotr.ai was in the source list of 6 of 32 unbranded Perplexity answers (as often as reddit.com), but Quotr was named in only **1 of 32** ([report](<../../reports/Quotr GEO AEO strategy audit.md>)).
- **Named in 0 of 8 problem/how-to questions,** even ones where Quotr's post was the first source ("how accurate is AI takeoff") or where Quotr sells the exact service (LA fire-rebuild cost estimates) ([presence-scorecard.md](../02-current-state/presence-scorecard.md)).
- **Top-of-funnel white space exists:** on factory-direct buying, tariffs and landed costs, multifamily cost benchmarks and residential rebuild costs, almost no software company is cited today ([white-space.md](../03-market/white-space.md)).
- **No traffic data yet.** Quotr's GA4, Search Console and CRM numbers were not available to this research (TO CONFIRM with Quotr).
- **Expect informational clicks to keep falling** even if rankings hold (fact-check and notes inference). Quotr's dictionary (55 short definitions) and generic explainers are the most exposed.

### 6.2 Three ways to grow reach (from the report)

1. **Show up by name on unclaimed topics.** Factory-direct buying, tariffs and landed cost, multifamily and residential cost per sq ft, rebuild costs, using Quotr's own project and pricing data.
2. **Build assets people still click through to.** Trade material calculators, a landed-cost calculator, estimate and bid templates, a dated cost dataset, trade-by-trade videos.
3. **Be present where AI reads beyond quotr.ai.** Reviews (G2 feeds Capterra, GetApp, Software Advice), independent "best of" lists, YouTube, r/estimators, Facebook estimator groups, founder LinkedIn articles, trade press.

### 6.3 Rate content by "click resilience"

Aleyda Solis's content-prioritisation framework scores content on **click resilience** (will people still need to visit after the AI answer?), **citation potential** (unique, verifiable, primary information?) and **brand-mention potential** (a real reason to link the brand to the topic?) ([Aleyda Solis](https://www.aleydasolis.com/en/ai-search/content-prioritization-ai-search/); framework, not data). Applied to Quotr's content types:

| Content type | Click resilience | Citation potential | Brand-mention potential | What to do |
|---|---|---|---|---|
| Generic definitions (55 dictionary terms) | Low | Low (not cited in tests) | Low | Keep short and accurate; deepen only terms tied to Quotr's strengths (takeoff, bid leveling, DDP, landed cost) |
| Generic how-to guides | Low–medium | Medium | Low | Answer-first, with Quotr's own numbers and a link to a tool |
| Number-rich explainers (e.g. AI takeoff accuracy post) | Medium | **High** (Perplexity's first source) | Medium, if the name travels with the numbers | Attach "Quotr's testing" to the figures |
| Original cost/price datasets | Medium–high | **High** | **High** | Top priority; publish method, sample and date |
| Free calculators and templates | **High** | Medium–high (calculators dominate how-to answers) | Medium | Build 1–2 in the next 90 days |
| Honest comparison pages | Medium | High (95% of "X vs Y" queries show an AI Overview) | High | Keep 5–8; accurate and dated |
| YouTube videos | High (people watch) | High in Google AI features | High | One trade per video, "Quotr" said aloud |
| Case studies with numbers | Medium | Medium | High | Named customers, real figures |

### 6.4 Make each mention count

- **Attach the name to the fact** so citations become mentions ("Quotr.ai's Estimation Service charges $0.25 per sq ft…"). See [../06-playbooks/geo-writing-style-guide.md](../06-playbooks/geo-writing-style-guide.md).
- **Prepare the homepage for AI visitors.** Since May 2026, ChatGPT can link a brand name straight to the homepage. First-time visitors arrive mid-question, so the homepage should say plainly what Quotr is, who it is for, the entry price and the next step.
- **Consistent facts everywhere,** so AI can name Quotr with confidence and tell it apart from Quotr Pro and other namesakes ([../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md)).

### 6.5 The six-number scorecard (from the report)

Track monthly: (1) share of AI answers that name Quotr, (2) AI impressions in Search Console, (3) branded search volume, (4) review count, (5) YouTube views, (6) demos that came from AI (self-reported plus GA4). Keep sessions alongside, but stop using them as the only top-of-funnel measure.

### 6.6 Hypotheses to test in Quotr's own data (not assumptions)

| Hypothesis | How to test |
|---|---|
| AI-referred visitors convert better than organic for Quotr | GA4 AI channel + Perplexity rule, compared with organic, over 1–2 quarters |
| Buyers who mention ChatGPT or Google AI on demo forms close at a different rate | CRM field from the "How did you hear about us?" question |
| Original data pages earn more AI mentions than new blog posts | Tracking-set results before and after the first dataset |
| Fixing prices changes branded answers within weeks | Branded answers should start quoting $79.90 after re-crawl (report's first proof point) |

### 6.7 Paid options (watch, don't assume)

ChatGPT ads (US test from Feb 9, 2026; self-serve, CPA bidding; sponsored agents tested Sept 2026) sit **next to** answers, not inside them; OpenAI says ads do not influence answers. Treat them as a separate paid channel and test only if self-serve access and cost per action make sense ([OpenAI Help](https://help.openai.com/en/articles/20001047-ads-in-chatgpt); [Reuters](https://www.reuters.com/business/media-telecom/openai-tests-advertiser-sponsored-agents-expands-ai-tools-chatgpt-ads-2026-09-16/); [verification H18](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>)).

### 6.8 What not to do

- Don't opt out of Google's AI features to "protect" clicks; Quotr needs the visibility.
- Don't answer falling blog traffic with more generic posts; page volume barely correlates with AI visibility.
- Don't read one month or one engine as a trend.

---

## Gaps

- No construction/AEC-specific data on AI Overview prevalence, CTR loss or AI referral share was found.
- Seer's 2026 rebound covers only Dec 2025–Feb 2026; whether it held through Sept 2026 is unknown.
- Several widely repeated B2B conversion figures have no traceable primary source.
- Quotr's own GA4, Search Console and CRM data were not available (TO CONFIRM with Quotr).
- Axios (Sept 19, 2026) and Comscore/Digiday pieces on AI referrals splintering beyond ChatGPT were found but not read ([Axios](https://www.axios.com/media-trends-membership/2026/09/19/ai-search-traffic-referrals-news-sites); [Digiday](https://digiday.com/media/comscore-data-shows-how-ai-discovery-is-splintering-beyond-chatgpt/)).

---

## Related pages

- [how-ai-engines-choose-sources.md](how-ai-engines-choose-sources.md) — how each engine picks and shows sources
- [signals-that-matter.md](signals-that-matter.md) — what gets a brand named
- [myths-and-risks.md](myths-and-risks.md) — tactics to avoid
- [geo-glossary.md](geo-glossary.md) — plain-English definitions
- [../05-content-strategy/top-of-funnel-strategy.md](../05-content-strategy/top-of-funnel-strategy.md) — Quotr's top-of-funnel plan
- [../03-market/white-space.md](../03-market/white-space.md) — topics no competitor owns in AI answers
- [../07-measurement/kpis-and-dashboard.md](../07-measurement/kpis-and-dashboard.md) — the KPI set and dashboard
- [../07-measurement/tracking-setup.md](../07-measurement/tracking-setup.md) — GA4, Search Console and Bing setup
- [../02-current-state/ai-visibility-baseline.md](../02-current-state/ai-visibility-baseline.md) — Quotr's September 2026 baseline
