# GEO/AEO/SEO benchmarks for B2B SaaS (2025–2026) and defensible 30/60/90-day targets for Quotr (as of 2026-11-23)

**How to read these notes**
- **Scope.** This file covers benchmarks and target-setting only. Quotr's own baseline (Perplexity, Sept 2026: named in 1 of 32 unbranded prompts, 3.1%; quotr.ai cited in 4 of 32, 12.5%; share of voice ~0.7%) and the existing KPI definitions are in `geo-brain/07-measurement/kpis-and-dashboard.md` and `research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md`. They are not repeated here.
- **Evidence labels.** Each finding is tagged:
  - **[Known]**: a primary or peer-reviewed source, or a fact-check in the earlier audit confirmed it.
  - **[Likely]**: a consistent vendor or secondary figure.
  - **[Speculative]**: an agency self-report, untraced, or a projection.
- **Source access.** In this session WebFetch could not reach searchengineland.com, conductor.com, sparktoro.com, clarity.microsoft.com or arxiv.org (DNS blocked). Figures marked "[search summary]" therefore come from search-engine summaries of those pages, not from reading the pages. Figures marked "[prior notes]" were fetched and fact-checked in the September 2026 audit.
- **Funding and bias.** Almost every GEO dataset comes from a vendor that sells GEO tools or services (Conductor, Ahrefs, Semrush, BrightEdge, AirOps, Profound, Gumshoe, G2, Previsible, Seer). The only peer-reviewed study (Kaiser & Schulze) and the only independent survey (Pew) are flagged as such.

---

## 1. AI referral traffic: share of site traffic, growth, and conversion vs organic

### Takeaway
AI referrals are still a **small share of traffic**:
- **~1% of sessions** across industries (Conductor, 13,000+ domains).
- **~2.8%** for the IT/software sector (Conductor).
- **0.13%** in Previsible's GA4 panel.

They are growing fast: roughly **+20% to +47% per quarter** depending on the panel. Conversion evidence **conflicts**:
- Microsoft Clarity (publishers) and single-company SaaS data (Ahrefs) show AI visitors converting 3x–23x better.
- The only peer-reviewed study (e-commerce) shows ChatGPT traffic converting **worse** than organic.

For Quotr, AI referrals can be a meaningful *signal* within 90 days, but not yet a meaningful *lead volume*.

### Cited Findings
**Share of traffic**
- **Conductor "2026 AEO/GEO Benchmarks Report"** (Nov 13, 2025; **3.3B sessions, 13,000+ domains**; US data, May–Sept 2025) **[Likely; vendor, enterprise-skewed sample; search summary]**:
  - AI referrals were **1.08%** of all website traffic across 10 industries.
  - Information Technology was highest at **2.80%**, Industrials **1.25%**, Real Estate **1.01%** and Financials **0.48%**.
  - Sources: [Conductor report](https://conductor.com/academy/aeo-geo-benchmarks-report/); [Conductor IT](https://www.conductor.com/academy/information-technology-aeo-geo-benchmarks/); [Conductor Industrials](https://www.conductor.com/academy/industrials-aeo-geo-benchmarks/); [BusinessWire](https://www.businesswire.com/news/home/20251113364791/en/Conductor-Unveils-2026-AEO-GEO-Benchmarks-Report-How-AI-Shapes-Brand-Visibility-in-a-Zero-Click-World)
  - A secondary write-up gives **3.37%** for "software and services" against the same 1.08% average, so the sector definition matters. — [Georankers](https://blog.georankers.ai/ai-search-visibility-benchmarks-b2b-saas/) **[search summary]**
- **Conductor webinar page** claims ChatGPT drives **90%+** of AI referral traffic and that AI referrals convert **2x** better than all other sources combined. This is **promotional framing; no method given.** — [Conductor webinar](https://www.conductor.com/events/webinars/the-new-metrics-of-the-web-aeo-/-geo-benchmarks-to-shape-your-2026-strategy/)
- **Previsible "2025 State of AI Discovery"** (agency; **19 GA4 properties**; 1.96M LLM sessions) **[Likely; small panel]**:
  - AI-sourced sessions rose from **17,076 to 107,100** (Jan–May 2024 vs Jan–May 2025), a **+527%** change.
  - AI was **0.13% of total sessions**.
  - ChatGPT was **84.2%** of AI referrals, growing 3.26x year on year. Copilot grew 25.2x and Claude 12.8x, both from small bases.
  - Sources: [Previsible](https://previsible.com/seo-strategy/ai-seo-study-2025/); [Search Engine Land](https://searchengineland.com/ai-traffic-up-seo-rewritten-459954)
  - Later Previsible data (secondary, **not opened**): ChatGPT reached **92.4%** of standalone LLM referrals. Monthly LLM sessions **fell ~50% in November 2025** and recovered in December. A 166-site panel shows AI sessions compounding at about **13.6% per month** (Nov 2024–May 2026). — [Driven Metrics](https://driven-metrics.com/blog/ai-referral-traffic-statistics/); [Scalevise](https://scalevise.com/resources/chatgpt-ai-referral-traffic-previsible-study/) **[search summary; it was not confirmed which secondary page carries which number]**
- **Similarweb**: **770.7M** monthly AI referral visits worldwide (Jun 2025–May 2026), **+117.4% YoY**. — [Similarweb](https://www.similarweb.com/blog/marketing/geo/gen-ai-stats/) **[prior notes]**
- **Ahrefs' own site**: AI search was **0.5%** of visits, up from 0.3%. — [Ahrefs](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/) **[prior notes; single company]**
- **Usermaven**: B2B SaaS AI share of **0.88%** of sessions. Vendor pages also claim **5–15%** for "actively optimised" B2B SaaS companies, which reads as a selected sample. — [Georankers](https://blog.georankers.ai/ai-search-visibility-benchmarks-b2b-saas/); [Webtonic](https://www.webtonic.io/blog/b2b-saas-and-tech-generative-engine-optimization-aeo-statistics) **[Speculative; search summary]**

**Conversion: conflicting evidence**
- **Microsoft Clarity** (Microsoft; **1,277 publisher/news domains**; one-month "smart events" snapshot) **[Likely for publishers; not B2B SaaS; search summary]**:
  - AI referrals were **<1% of traffic** but converted at **3x** the rate of search and social.
  - Sign-up conversion was **1.66% for AI vs 0.15% for search** (the "~11x" framing).
  - Copilot referrals converted to subscriptions at **17x** direct and **15x** search; Perplexity at **7x**.
  - Microsoft owns Copilot and Bing, which is a conflict of interest for the Copilot finding.
  - Sources: [Clarity blog](https://clarity.microsoft.com/blog/ai-traffic-converts-at-3x-the-rate-of-other-channels-study/); [PPC Land](https://ppc.land/microsoft-clarity-reveals-how-ai-assistants-are-reshaping-website-traffic-patterns/)
- **Ahrefs** (SaaS, single company): AI visitors were **0.5% of visits but 12.1% of signups**, about **23x** organic. — [Ahrefs](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/) **[prior notes]**
  - A separate Ahrefs study found AI visitors **view fewer pages and bounce more**. — [Ahrefs AI traffic quality](https://ahrefs.com/blog/ai-traffic-quality-study/) **[prior notes]**
- **Semrush** (June 2025, **modelled**): an AI visitor is worth **4.4x** an organic visitor. — [Semrush](https://www.semrush.com/blog/ai-search-seo-traffic-study/) **[prior notes; projection, not observed]**
- **Similarweb**: AI referrals to transactional sites converted at about **7%** in 2025. — [PPC Land summary](https://ppc.land/ai-referral-traffic/) **[search summary; primary not opened]**
- **Kaiser (U. Hamburg) & Schulze (Frankfurt School)**, *Marketing Science* (2025) **[Known; peer-reviewed; e-commerce only]**:
  - **973 e-commerce sites, 12 months** of first-party data.
  - ChatGPT referrals converted **~13% worse** than Google organic, and worse than every channel except paid social.
  - Sources: [INFORMS](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0489); [prior notes]
- **AirOps** aggregates the same conflicting figures and warns that "conversion" means different things across studies. — [AirOps](https://www.airops.com/blog/ai-referral-traffic-conversion-rates)
- **Adobe**: no 2026 Adobe Analytics AI-traffic conversion dataset was found in this session (see Gaps).

**Buyer behaviour**
- **G2 survey** (vendor, March 2026, **n = 1,076**): **51%** of B2B software buyers start research with an AI chatbot more often than with Google. — [PR Newswire](https://www.prnewswire.com/news-releases/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots-302742807.html) **[prior notes; vendor survey]**

### Inferences
- **Realistic AI share for Quotr** is **0.3%–3% of sessions**. The low end matches Previsible's mixed panel and the Ahrefs pre-2026 figure. The high end matches Conductor's IT sector. Anything above ~3% within 90 days would put Quotr in the vendor-claimed "actively optimised" bracket, which is not a defensible base case.
- **Market drift alone grows AI referrals ~20–47% per quarter.** These are my calculations:
  - Similarweb's +117% YoY compounds to **+21%** over 3 months.
  - Previsible's 13.6%/month compounds to **+47%** over 3 months.
  
  So a day-90 target of "+25% AI referral sessions" could be met with **no work at all**. Targets must beat drift, or be expressed relative to competitors and share of sessions.
- **AI referrals cannot move a day-90 lead KPI much.** Illustrative arithmetic, not Quotr data:
  - At 10,000 sessions a month, 1% AI share is **100 AI sessions**.
  - At a ~2% site conversion rate (Section 5), that is **~2 leads/month**.
  - Even at Clarity's 3x it is **~6 leads/month**; at Kaiser's −13% it is **~1.7**.
  - So "AI-referred qualified leads" is a *measure-and-learn* KPI for 90 days, not a primary target.
- **Do not promise "AI traffic converts better".** For B2B SaaS the evidence is one company (Ahrefs) plus vendor models; the one rigorous study points the other way. Quotr should test it in its own GA4 and CRM.

### Gaps
- No construction-tech or AEC-software AI-referral share or conversion benchmark exists in any source found.
- Adobe Digital Insights 2025–2026 AI-traffic conversion data was not found; a targeted search on Adobe's own site would be needed.
- Webflow and Vercel figures (Webflow "8% of signups, 6x conversion"; Vercel "10% of signups from ChatGPT", Mar–Apr 2025) were covered in the prior notes. Only Vercel's is first-party, and it is early 2025.
- Conductor's 1.08% / 2.80% figures cover May–Sept 2025. No 2026 refresh was found.
- The primary pages for the Previsible 166-site panel and the Usermaven 0.88% figure were not opened.

---

## 2. Google organic CTR impact of AI Overviews / AI Mode, zero-click rates, and what it means for TOFU blog traffic

### Takeaway
All major datasets agree that AI Overviews (AIO) cut organic CTR on informational queries, but the size differs:
- Amsive: −15% average, −20% non-branded.
- BrightEdge: ~−30% across sectors.
- Ahrefs: −58% for position 1.
- Seer: −61%, with a partial 2026 rebound.

The share of queries showing an AIO is rising fastest in **B2B technology** (BrightEdge: 36% to 82% of tracked B2B tech keywords in 12 months). Zero-click Google searches are about **68%**. For Quotr this means **informational blog traffic should be budgeted flat to down even if rankings improve**. Branded queries are the exception and can gain CTR.

### Cited Findings
- **Pew Research Center** (independent; **900+ US adults, 68,879 searches**, March 2025) **[Known]**:
  - Users clicked a result on **8%** of visits to pages with an AI summary vs **15%** without.
  - **1%** clicked a link inside the summary.
  - Source: [Pew](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) **[prior notes]**
- **Ahrefs** (vendor) **[Likely]**:
  - AIO cut position-1 CTR by **34.5%** (April 2025).
  - The update on **300K keywords** (Dec 2025 data) found **−58%**.
  - Sources: [Ahrefs update](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update) **[prior notes]**
- **Seer Interactive** (agency; **53 brands, 5.47M queries**) **[Likely]**:
  - Organic CTR on AIO queries fell **1.76% to 0.61%** (2024 to 2025), then **rebounded to 2.4%** by Feb 2026.
  - Brands **cited in the AIO get +35% organic clicks**.
  - Source: [Seer 2026 update](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update) **[prior notes]**
- **Amsive** (agency; **700,000 keywords across 10 sites**; April 2025; often misdated as 2026 in aggregators) **[Likely; search summary, Amsive page not opened]**:
  - Average CTR change when an AIO was present: **−15.49%**.
  - **Non-branded −19.98%**; **branded +18.68%**.
  - **AIO plus featured snippet −37.04%**.
  - Sources: [WordsAtScale aggregation](https://wordsatscale.com/ai-overviews-ctr-statistics-2026/); [Omnibound](https://www.omnibound.ai/blog/google-ai-overviews-statistics)
- **BrightEdge** (vendor) **[Likely; search summary]**:
  - AIOs appeared on **48% of searches in Feb 2026**, up from ~30% in Feb 2025.
  - **B2B technology keywords triggering AIOs rose from 36% to 82%** (Feb 2025 to Feb 2026).
  - Year-one review: impressions **+49%**, click-throughs **down nearly 30%**.
  - Nov 6, 2026: AIOs appeared on **64% of 282 tracked US brand/product-name searches**, up from 19% in August.
  - Sources: [BrightEdge one-year PDF](https://videos.brightedge.com/assets/SGE-Guide/BrightEdge%20Report%20-%20AIO%20Overviews%20One%20Year%20Review%20Research%20Paper%20and%20Deep%20Dive%20.pdf); [Web Traffic News](https://webtrafficnews.com/briefs/brightedge-finds-ai-overviews-on-brand-searches-now-reach-64); [Marqeable B2B summary](https://www.marqeable.com/blog/ai-overviews-b2b-traffic/)
  - **Conflict:** AIO prevalence estimates vary a lot by panel: Semrush ~15.7% (late 2025) vs Xponent21 ~60.3% (US, April 2026). — [Omnibound](https://www.omnibound.ai/blog/google-ai-overviews-statistics) **[search summary]**
- **Zero-click**: **68.01%** of US Google searches ended without a click (Jan–Apr 2026, Similarweb panel), vs 60.45% in 2024 (Datos; a different provider). — [SparkToro](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/) **[prior notes]**
- **AI Mode**: **93%** of AI Mode sessions ended with no external click (Semrush, 69M sessions, 2025). — [Semrush](https://www.semrush.com/blog/google-ai-mode-seo-impact/) **[prior notes]**
- **Google's position**: total organic clicks are "relatively stable" year over year, and click quality has risen. No data was released to back this. — [Google blog](https://blog.google/products-and-platforms/products/search/ai-search-driving-more-queries-higher-quality-clicks/) **[prior notes]**
- **Gartner** (Feb 19, 2024) predicted traditional search-engine volume would **drop 25% by 2026**. This is a **prediction**, criticised at the time. No source found in this session confirms it came true. — [Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-02-19-gartner-predicts-search-engine-volume-will-drop-25-percent-by-2026-due-to-ai-chatbots-and-other-virtual-agents); [SEJ critique](https://www.searchenginejournal.com/why-prediction-of-25-search-volume-drop-due-to-chatbots-fails-scrutiny/511270)

### Inferences
- **TOFU blog sessions are a structurally falling metric.** With B2B tech AIO coverage near 80% and non-branded CTR down 15–60%, a flat informational-traffic number is likely a *good* outcome. **Leanid should not accept "blog sessions up X%" as his TOFU KPI.** Better TOFU measures:
  - Search Console **impressions** (reach is still being delivered);
  - **AI mention/citation rate**;
  - **branded search impressions**;
  - **non-blog landing-page sessions** (pricing, comparison, product).
- **Branded demand is the protected asset.** Amsive's +18.7% branded CTR and BrightEdge's 64% AIO coverage on brand names together mean Quotr should make sure AIOs on "Quotr" queries are accurate. This links to the earlier finding that 5 of 8 branded answers had errors.
- **Being cited inside AIOs is worth tracking:** Seer finds +35% organic clicks for cited brands. Search Console's AI impressions and Bing AI citations are the first-party proxies.

### Gaps
- No construction-specific CTR or AIO-prevalence study was found.
- Seer's 2026 rebound covers only Dec 2025–Feb 2026. Whether it persisted to Nov 2026 is unknown.
- No 2026 Pew update was found.
- Amsive's and BrightEdge's primary pages were not opened in this session.

---

## 3. AI share-of-voice / mention-rate benchmarks, realistic 90-day improvement for a challenger, and run-to-run volatility

### Takeaway
AI answers are **highly variable run to run**:
- The same brand *list* repeats <1% of the time (SparkToro/Gumshoe).
- Only ~30% of brands stay visible from one answer to the next (AirOps).

*Inclusion frequency* over many runs is more stable than *rank*. A single run per prompt (Quotr's Sept 2026 baseline) has a 95% interval of roughly **0.6%–15.7%** around the 3.1% point estimate. A credible measurement needs **3–5+ runs per prompt across 3+ engines**. SparkToro suggests 60–100 runs per prompt to map one prompt's full recommendation set.

No credible public case study shows a challenger B2B brand going from ~3% to competitor parity (~30%) in 90 days. Published "12% to 71%" style jumps are agency self-reports. A defensible 90-day goal is **roughly 2–3x the baseline mention rate (to ~6–10%)**, with ~15% as stretch.

### Cited Findings
**Volatility studies**
- **SparkToro and Gumshoe.ai** (Rand Fishkin with Patrick O'Donnell; published **Jan 28, 2026**; data Nov–Dec 2025) **[Likely; search summaries; not peer-reviewed; Gumshoe sells AI-visibility tracking]**:
  - Design: **~600 volunteers** ran **12 prompts** a total of **2,961 times** on ChatGPT, Claude and Google AI (AIO/AI Mode).
  - ChatGPT and Google AI returned the **same brand list <1%** of the time and the **same list in the same order ~0.1%** of the time. Claude was only slightly more consistent.
  - List length ranged from 2–3 brands to 10+.
  - **Rank position was the least stable** ("effectively meaningless"). **Visibility % across many runs was more consistent.**
  - Sources: [SEJ](https://www.searchenginejournal.com/ai-recommendations-change-with-nearly-every-query-sparktoro/566242); [Search Engine Land](https://searchengineland.com/ai-recommendation-lists-rarely-repeat-study-468076); [MediaPost](https://www.mediapost.com/publications/article/412364/ai-brand-recommendations-chaotic-inconsistent.html)
  - Fishkin suggests **60–100 runs per prompt** to know an AI's recommendation set for that prompt. The authors disclosed the commercial tie and called for larger follow-up work. — [Intelligent Resourcing](https://intelligentresourcing.co/blogs/aeo-red-flags-evidence); [AuthorityTech](https://authoritytech.io/curated/ai-rank-is-noise-consideration-set-is-real-2026) **[search summary, secondary]**
- **Conductor counter-analysis** (vendor; **14,000 API calls**, 10 industries, 7 intent types, 4 LLMs, 5 simulated personas): concludes AI brand recommendations are **"not random"**. The method differs (API calls rather than consumer apps), so the results are not directly comparable. — [Conductor](https://www.conductor.com/academy/ai-recommendation-consistency-analysis/) **[Likely; search summary]**
- **AirOps** (vendor; reportedly ~800 queries and ~45,000 citations) **[Likely; search summary]**:
  - **~30% of brands stayed visible from one answer to the next**; **~20% stayed visible across five consecutive runs**.
  - **57%** of pages that disappeared later resurfaced.
  - Brands that were **both mentioned and cited** were **40% more likely to resurface**; only ~28% of answers do both for the same brand.
  - Sources: [AirOps volatility](https://www.airops.com/blog/ai-search-volatility-why-brand-visibility-constantly-fluctuates-in-answer-engines); [AirOps 2026 State of AI Search](https://www.airops.com/report/the-2026-state-of-ai-search); [AirOps citations & mentions](https://www.airops.com/report/how-citations-mentions-impact-visibility-in-ai-search)
- **RanketAI** (vendor, July 2026): **one follow-up question removes ~62%** of a brand's AI picks. — [RanketAI](https://www.ranketai.com/en/blog/deep-dive-ai-recommendation-volatility-2026-07-08) **[Speculative; title/summary only]**
- An academic paper, "**Don't Measure Once: Measuring Visibility in AI Search (GEO)**" (arXiv 2604.07585, April 2026), addresses repeated measurement. **Not opened (arxiv.org blocked).** — [arXiv](https://arxiv.org/pdf/2604.07585)

**Mention-rate improvement case studies (credibility ranked)**
- **Ramp** (Profound case): AI visibility rose from **3.2% to 22.2% in one month** (March 2025). This is Profound's metric on its own prompt set. — [prior notes, verification H14] **[Speculative/vendor]**
- **Over The Top SEO "ProjectFlow"** (agency self-report; pseudonymous B2B software client; **50 queries**): citation rate went from **12% to 28% (month 1), 71% (month 3) and 87% (month 4)**. — [Over The Top SEO](https://www.overthetopseo.com/?p=59864) **[Speculative: unverifiable client, small prompt set, author sells the service]**
- **Avenue Z** (agency pilot): mention share reached **28%** over ~90 days, and the brand climbed to #4 among tracked competitors. Measurement windows were inconsistent (121 vs ~90 days). — [Noble summary](https://thatsnoble.com/resources/how-avenue-z-increased-ai-visibility-by-250-and-outpaced-every-competitor-in-the-category) **[Speculative]**
- **AdsX** (DTC home goods, not B2B): **+340% AI mentions in 90 days** from an **8%** starting mention rate. The post-period rate was not stated in the summary. — [AdsX](https://www.adsx.com/blog/how-we-increased-ai-mentions-340-percent-case-study) **[Speculative]**
- **Victorious** study: **89% of brands never appeared** in AI category answers. — [SEJ coverage](https://searchenginejournal.com/ai-brand-mention-study-victorious-spa/582765) **[Likely; search summary]**
- Prior notes found **no public construction-tech GEO case study with verified numbers**. — [prior notes, playbook §5]

**Quotr's baseline precision** (my calculation, Wilson 95% intervals) **[Known arithmetic]**:

| Observed | n (prompt-runs) | Point | 95% CI |
|---|---|---|---|
| 1 of 32 (Quotr, Sept 2026) | 32 | 3.1% | **0.6%–15.7%** |
| 10 of 32 (top competitor level) | 32 | 31% | 18%–49% |
| 3 of 32 (prior 90-day target) | 32 | 9.4% | 3.2%–24.2% |
| 15 of 160 (32 prompts × 5 runs, 1 engine) | 160 | 9.4% | 5.8%–14.9% |
| 43 of 480 (32 prompts × 5 runs × 3 engines) | 480 | 9.0% | 6.7%–11.8% |

- Sample size needed to detect a move from 3% to 9% (two-proportion test, α = 0.05, power 80%): **~245 prompt-runs per period**. To detect 3% to 6%: **~750**. Runs of the same prompt are correlated, so the effective sample is smaller than this; treat these as lower bounds.

### Inferences
- **Measurement protocol (must be agreed before targets are binding):**
  - A **fixed panel of 32–50 unbranded prompts**.
  - Each run **3–5 times** on **at least 3 engines**: ChatGPT (search on), Perplexity, and Google AI Mode/AIO. Gemini and Copilot are optional.
  - Same month window; logged-out or clean sessions; same location (US).
  - That gives ~300–750 prompt-runs a month, enough to tell a 3% to 9% move from noise.
  - Report **inclusion rate with a confidence interval**, **never rank position**.
  - Re-baseline at day 0 with this protocol. The September single-run 3.1% is directionally useful but too noisy to be the contract baseline.
- **A realistic 90-day improvement for a challenger** (inference from weak evidence):
  - **Fast wins (weeks):** prompts where quotr.ai is already *cited but not named*. 3 such prompts are on record.
  - **Branded answer accuracy:** a quick fix once pages are re-crawled.
  - **Slow wins (months):** category prompts, which depend on third-party lists and reviews (Section 6).
  
  So mention rate should roughly **double or triple** (3% to 6–10%) by day 90. **15%+ is stretch**. **~30% (competitor parity) is not a 90-day outcome**: no credible evidence supports it, and the cases that claim it are self-reported.
- **Share of voice moves more slowly than mention rate.** Competitors are named in many answers, so even 3–5 Quotr mentions lift SOV only from ~0.7% to ~2–4%. This is consistent with the existing KPI doc.
- **Any agency report based on 1 run per prompt, or on "rank #1 in ChatGPT" screenshots, should be rejected as evidence.** The SparkToro and AirOps data show single runs are mostly noise.

### Gaps
- The SparkToro, Conductor and arXiv primary pages could not be opened (blocked hosts). The 60–100 runs recommendation and AirOps sample sizes come from secondary summaries.
- No study gives engine-specific, run-to-run variance for B2B *software* prompts in particular.
- A search summary mentioned an eight-week study with **~39% average weekly domain churn** across ChatGPT, AI Mode and Perplexity. The primary source was not identified, so it is not used above.
- No independent (non-vendor) longitudinal study of challenger-brand mention-rate growth exists.

---

## 4. Content velocity: is 186 articles in 90 days (~15/week) advisable for a small B2B site?

### Takeaway
Google has **published no velocity threshold**. Its scaled content abuse policy targets *many pages made mainly to manipulate rankings*, **however they are produced**. Velocity is not penalised in itself, but a sudden 4x jump in output on a small site, at a price that implies near-unedited AI drafting, is the textbook risk profile.

The evidence also says volume has **low marginal return**:
- Only **1.7%–6.1%** of new pages reach Google's top 10 within a year (Ahrefs).
- **~35–62%** of pages may not be indexed at all, or not within 30 days (IndexCheckr; biased sample).
- Purely AI-written articles hold **#1 only ~7–10%** of the time (Graphite, Semrush).

**Recommendation:** cap net-new articles at roughly **1.5–2x Quotr's current pace (~6–8/week max, ideally fewer)**, each passing a quality bar, and move the rest of the budget into refreshing and merging the existing 96 posts, comparison pages, original data, reviews and list outreach.

### Cited Findings
**Policy (primary)**
- **Google, March 2024 core update and spam policies** **[Known]**:
  - Scaled content abuse = "many pages are generated for the primary purpose of manipulating Search rankings and not helping users". It applies whether content comes from **automation, human efforts, or some combination**.
  - Enforcement began **May 5, 2024**.
  - Google reported **45% less** low-quality, unoriginal content in results after the rollout (originally projected 40%).
  - Sources: [Google Search Central blog](https://developers.google.com/search/blog/2024/03/core-update-spam-policies); [Google blog](https://blog.google/products/search/google-search-update-march-2024/)
- **Google's "AI features and your website" guidance**: creating separate content for every query fan-out variation violates the scaled content abuse policy. — [Google](https://developers.google.com/search/docs/appearance/ai-features) **[prior notes]**
- **Hobo Web** analysis of the leaked attribute **"QualityCopiaFireflySiteSignal"**: reportedly tracks new-page creation in 30-day windows, with sudden jumps a likely flag. — [Hobo Web](https://www.hobo-web.co.uk/firefly/) **[Speculative: leak interpretation, unverified by Google]**
- **Practitioner guidance**: about **1 page/week for brand-new sites**, up to **~1/day for established sites**, several per day only for large sites with real demand; "Google has never published a threshold". — [TJ Robertson](https://tjrobertson.com/how-much-content-is-too-much/) **[Speculative: opinion]**

**Indexing rates**
- **IndexCheckr** (index-checking vendor; **~16M pages**; Feb 2025) **[Likely; biased sample of user-monitored pages, often low-quality or link pages; search summary]**:
  - **61.94%** of tracked pages were **never indexed**.
  - Of pages that were indexed, **93.2%** were indexed within 6 months.
  - Secondary summary: **14.0%** indexed within 7 days, **64.86% within 30 days**, 76.81% within 3 months.
  - **13.7%** of indexed pages were deindexed within 3 months; the overall deindex rate was **21.29%**.
  - Indexing tools succeeded only **29.37%** of the time.
  - A later figure from users' own sites: **~72%** of pages indexed.
  - Sources: [IndexCheckr](https://indexcheckr.com/resources/google-indexing); [SEJ](https://www.searchenginejournal.com/data-suggests-google-indexing-rates-are-improving/540700/)

**Time to rank (Ahrefs, vendor)** **[Likely]**:
- Only **1.74%** of **1M random URLs** first seen in Sept 2023 reached the **top 10 within a year**, down from 5.7% in the 2017 study.
- For non-empty English content (**2M URLs**, Oct 2023): **6.11%**.
- Of pages that did reach the top 10, **40.82% got there within 1 month**.
- **13.7%** of top-10 pages were under 1 year old (22% in 2017).
- Source: [Ahrefs](https://ahrefs.com/blog/how-long-does-it-take-to-rank/) **[search summary]**

**AI-generated content performance**
- **Graphite** (Oct 2025; **31,493 keywords**, 10 categories; June 2025 data; Surfer detector) **[Likely; vendor, detector-dependent]**:
  - About **14%** of ranking articles were AI-generated, and only **7% of #1 results**.
  - AI wrote **49.9%** of new English articles in Q1 2026.
  - Heavily edited AI-assisted content was **not evaluated**.
  - Sources: [Graphite](https://graphite.io/five-percent/ai-content-in-search-and-llms); [Axios](https://www.axios.com/2025/10/14/ai-generated-writing-humans)
- **Semrush** (**42,000 blog pages**, Nov 2025; April 2026 update): purely AI content held **#1 ~9–10%** of the time vs **~80%** for human-written. Its 2024 study had found near parity. — [Launchcodex summary](https://launchcodex.com/blog/seo-geo-ai/ai-content-trap-seo/) **[search summary; Semrush page not opened]**
- **AirOps**: pages **not updated within 90 days are 3x more likely to lose AI citations**. — [AirOps 2026 State of AI Search](https://www.airops.com/report/the-2026-state-of-ai-search) **[Likely; vendor]**

**Quotr context** [prior notes]:
- About **96 posts in ~6 months** (~3.7/week).
- The audit found duplicate or overlapping pages to merge, and ~13 URLs carrying a stale price.
- The agency proposal is **186 website articles in 90 days (~14.5/week, ~3.9x the current pace)** plus 124 LinkedIn/X articles.

### Inferences
- **Is 186 in 90 days advisable? No, not as a volume target** (inference):
  1. **Pace:** ~4x Quotr's current pace on a small domain is exactly the kind of jump a velocity-sensitive classifier would notice. The Firefly evidence is unverified, but the downside is site-wide.
  2. **Ranking odds:** with 1.7–6% top-10 odds per new page, 186 pages would yield roughly **3–11 top-10 pages within a year**. Most would land after day 90.
  3. **Indexing:** indexing loss (benchmark ~35% not indexed within 30 days) wastes much of the volume.
  4. **Cost per asset:** at **~$53 per asset** (Section 7), the content is almost certainly lightly edited AI output, the category Graphite and Semrush show rarely wins #1.
  5. **Cannibalisation:** Quotr's own audit already found overlap among its 96 posts. Adding 186 more on the same clusters raises keyword cannibalisation and dilutes "cited but not named" pages.
- **Suggested velocity for days 1–90** (inference; no published optimum exists):
  - **Net-new:** **≤6–8 articles/week max, ideally 3–5/week**, each with a named expert, original data or a worked example, and a unique angle (comparison, per-trade, pricing).
  - **Refresh/merge:** **10–20 existing posts per month**, covering stale prices, answer-first rewrites and name-in-the-fact edits.
  - **Proof assets:** **1 original data asset by day 60–90**.
  - **LinkedIn:** founder and employee posts, not 124 long articles (Section 5).
- **Quality acceptance criteria to put in the contract** (so "content output" means something):
  - Unique information gain;
  - fact-checked against the Quotr fact sheet;
  - expert reviewer named;
  - no duplicate primary keyword with an existing URL;
  - indexed within 30 days, or the agency fixes or replaces it.

### Gaps
- No published Google threshold for velocity exists, and none is expected.
- No study isolates "velocity jump" as a cause of ranking loss on small B2B sites; the risk is inferred from policy plus the leak.
- The IndexCheckr 7/30-day figures come from a secondary summary, and its sample over-represents hard-to-index pages. A healthy small site with sitemaps and internal links probably indexes faster (unverified).
- No 2025–2026 study of indexing rates specifically for small B2B SaaS blogs was found.
- No study on the 2025–2026 core updates (e.g., the June 2025 or 2026 core updates) and AI content at scale was retrieved in this session.

---

## 5. B2B SaaS funnel benchmarks and LinkedIn organic benchmarks

### Takeaway
The most-cited (but methodologically opaque) benchmarks put B2B SaaS **organic visitor-to-lead conversion at ~2.1%**, **lead-to-MQL ~41%** and **MQL-to-SQL ~51% for SEO-sourced leads** (First Page Sage). Construction is **~1.9%** visitor-to-lead (First Page Sage) or **4.9%** under a broader lead definition (Ruler Analytics).

On LinkedIn, company-page organic reach has collapsed to **~2–5% of followers**. **Personal or founder posts get 2–10x the reach** and ~1.6–1.8x the engagement rate of company pages. This argues against 124 company-page "LinkedIn articles" and for founder-led posting.

### Cited Findings
**Website funnel**
- **First Page Sage** (SEO agency; data from its client base; definitions vary across its reports) **[Likely, opaque methodology; search summary]**:
  - B2B SaaS **SEO visitor-to-lead 2.1%**, **lead-to-MQL 41%**, **MQL-to-SQL 51%**. PPC-sourced MQL-to-SQL is 26%.
  - MQL-to-SQL ranges **28–46%** by vertical.
  - Site-wide B2B SaaS conversion is **1.1%** (demo, pricing and contact submissions per unique visitor).
  - Construction visitor-to-lead is **1.9%**.
  - Sources: [First Page Sage](https://firstpagesage.com/seo-blog/conversion-rate-benchmarks/); [Derivatex summary](https://derivatex.agency/blog/b2b-saas-seo-statistics/)
- **Ruler Analytics** 2026: **construction and engineering 4.9%** (broader definition including calls and qualified leads). — [Octo Agency summary](https://www.octoagency.io/blog/b2b-website-conversion-rate/) **[search summary]**
- Several secondary sites repeat 2.1–2.2% without new data, which suggests circular sourcing. — [Octo Agency](https://www.octoagency.io/blog/b2b-saas-website-conversion-rate-statistics/); [Kingmaker](https://kingmakersearch.com/blog/saas-seo-benchmarks-2026) **[search summary]**

**LinkedIn**
- Company-page organic reach is **down ~60–66% from 2024 to early 2026**. Current reach is about **2%** of followers, down from ~7%; another vendor says **2–5%** initial distribution. — [Ordinal](https://www.tryordinal.com/blog/the-declining-reach-of-linkedin-company-pages); [Updately](https://updately.ai/blog/linkedin-organic-reach-drop-pipeline-2026) **[Likely; vendor; search summary]**
- **Metricool 2026** (**673,658 posts**): engagement rate **~2.60% personal vs ~1.60% company pages**. Personal profiles lead mainly **below ~10K followers**, and posts with links get **~27% fewer impressions**. — [Contentin summary](https://contentin.io/blog/linkedin-content-statistics/) **[Likely; search summary]**
- **Socialinsider 2026**: **3.85% personal vs 2.10% company**. One roundup instead shows near-identical means (2.95% vs 2.89%), skewed by viral posts. — [Contentin](https://contentin.io/blog/linkedin-content-statistics/); [SocialNexis](https://socialnexis.com/guides/linkedin-company-page-vs-personal) **[search summary]**
- Claimed personal-vs-page reach multiples range from **2–5x**, to **5–10x**, to **"561%"**. — [Empanada](https://www.empanada.social/blog/linkedin-reach-benchmark-employee-posts-vs-company-pages-2026); [ViralBrain](https://www.viralbrain.ai/blog/linkedin-personal-brand-vs-company-page) **[Speculative; vendor claims]**

### Inferences
- **Translating the funnel into Quotr numbers** (illustrative; Quotr's own traffic is unknown):
  - Each **+1,000 organic sessions/month** yields about **19–21 leads**, ~8 MQLs and **~4 SQLs** at First Page Sage rates.
  - Getting +1,000 sessions/month from new content within 90 days is unlikely given Section 4 (few new pages rank within 90 days) and Section 2 (falling informational CTR).
  - So the **day-90 qualified-lead lift from new content alone will probably be small: single digits to low tens of leads.** Faster lead levers: conversion-rate work on existing traffic, comparison/alternatives pages, and branded-answer accuracy.
- **The baseline period is a seasonality trap.** Comparing a Dec–Feb day-90 window against a **June–October** baseline mixes seasons. Construction activity is seasonal in North America; whether Quotr's lead flow is higher or lower in winter is unknown. Use **year-over-year** data if available. Otherwise use **share-of-pipeline by source** or a **seasonally matched** comparison, and state the seasonality assumption in writing.
- **LinkedIn:** 124 long-form "LinkedIn/X articles" from a company page will reach ~2–5% of followers. A **founder-led cadence (3–4 posts/week by the CEO or Leanid, links in comments)** is better supported by the benchmarks. LinkedIn KPI: impressions and engagement rate per founder post vs the 2.6–3.9% personal benchmark; profile visits; demo mentions in "how did you hear about us".

### Gaps
- No construction-tech-specific MQL-to-SQL or demo-request benchmark was found. First Page Sage's construction column definitions could not be verified.
- No HubSpot, Databox or OpenView/High Alpha 2026 benchmark with organic-to-lead rates was retrieved in this session.
- No LinkedIn-published (first-party) reach benchmark exists; all figures are vendor panels.
- Quotr's own monthly sessions, leads and demo counts for June–October 2026 are needed to turn the rates above into absolute targets (TO CONFIRM with Quotr).

---

## 6. Third-party signals: review counts of category leaders vs Quotr, and how review count relates to AI recommendation

### Takeaway
Category leaders have **dozens to ~1,400 reviews**; Quotr has **~0**:
- STACK: ~1,396 Capterra and ~52–78 G2.
- PlanSwift: ~399 Capterra and ~33 G2.
- Buildxact: ~165–174 Capterra.
- Togal.AI: ~60 G2, ~0 Capterra.

Independent analyses find review **count and score barely predict *rank*** in ChatGPT answers (correlations −0.16 to +0.02). However, nearly **every tool ChatGPT names has review profiles (99–100%)**. Reviews work as an **inclusion gate**, not a ranking lever, so the goal is **"enough credible reviews to be eligible" (10–30), not parity with STACK**.

### Cited Findings
**Competitor review counts**
- **STACK** **[Known for Capterra; G2 conflicting]**:
  - Capterra: **1,396 verified reviews, 4.5** (page updated Feb 27, 2026); 1,393 on a March 2026 comparison page.
  - G2: **78** reviews (4.5) on one page vs **52** (4.4) on a comparison page, so the snapshot dates differ.
  - Sources: [Capterra STACK](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/); [Capterra compare](https://www.capterra.com/compare/70808-147181/PlanSwift-vs-STACK-Takeoff); [G2 STACK review](https://www.g2.com/products/stack-takeoff-estimate/reviews/stack-takeoff-estimate-review-4612863); [G2 compare](https://g2.com/compare/planswift-vs-stack-takeoff-estimate) **[search summary]**
- **PlanSwift**: Capterra **399 (4.3)**, G2 **33 (4.3)**. — [Capterra compare](https://www.capterra.com/compare/70808-147181/PlanSwift-vs-STACK-Takeoff); [G2 compare](https://g2.com/compare/planswift-vs-stack-takeoff-estimate) **[search summary]**
- **Togal.AI**: G2 **4.8 from ~60 reviews** [prior notes]; Capterra **0 reviews**. — [Capterra UK compare](https://www.capterra.co.uk/compare/147181/1038933/stack-takeoff/vs/togal-ai) **[search summary]**
- **Buildxact**: Capterra **4.6 from ~165–174 reviews**. — [prior notes, competitor benchmark §2]
- **Quotr**: G2 reportedly **0 reviews**; no Capterra, GetApp or Software Advice listing. — [prior notes]
- In Quotr's Sept 2026 test, review sites fed **9 of 32** answers. — [prior notes]

**Review count vs AI recommendation**
- **Quoleady** (agency, March 2026) **[Likely; search summary]**:
  - Near-zero correlation between **review score** and ChatGPT rank.
  - **Review count** correlation was **+0.02 (Capterra)** and **−0.11 (G2)**. Another write-up gives −0.21 Capterra and −0.16 G2.
  - **100%** of tools ChatGPT named had Capterra reviews and **99%** had G2 reviews.
  - Sources: [Quoleady](https://www.quoleady.com/llmo-research/); [Promptwatch](https://promptwatch.com/blog/do-g2-capterra-help-chatgpt-recommendations)
  - It was not confirmed which of the two pages carries the 100%/99% figure.
- **G2's own research** (~30k citations; G2 sells reviews, so it is conflicted): categories with **10% more reviews have ~2% more citations**. G2 calls this correlation, not cause. — [G2](https://learn.g2.com/do-more-g2-reviews-mean-more-ai-visibility) **[Likely; vendor]**
- **Discovered Labs**: correlation of **0.030** between customer ratings and how AI describes **921 brands**. — [Discovered Labs](https://discoveredlabs.com/blog/do-g2-reviews-change-ai-perception) **[Likely; agency]**
- A third-party claim that review profiles make brands "3.4x more likely" to be mentioned has **no clear methodology**. — [Loudmink](https://loudmink.ai/blog/how-many-g2-reviews-before-ai-recommends-you) **[Speculative]**
- Prior notes: YouTube and branded web mentions correlate more strongly with AI visibility than link metrics (Ahrefs brand-mention study). — [prior notes, citation signals §2]

### Inferences
- **Reviews are a threshold signal for Quotr.** Going from 0 to ~10–30 genuine reviews on G2 and Capterra plausibly matters more than any count beyond that. It also fixes the "Quotr Pro" rating mix-up in branded answers.
- **Realistic 90-day review targets depend on Quotr's paying-customer count (unknown).** A small startup running a structured ask through G2's or Capterra's own programmes can reasonably get **5–15 genuine reviews in 90 days**; **20+ is stretch**. Rating is not a target: incentive rules apply, and the evidence shows rating doesn't drive rank.
- **List inclusions on the cited "best of" pages** (Construction Coverage, ConstructConnect, ContraVault, etc.) likely move category mention rate more than reviews do. These are outreach KPIs, not content-volume KPIs.

### Gaps
- No live G2 page was read in this session (G2 blocked tools in September too). STACK's G2 count conflicts between pages.
- No study isolates the review count needed for AI inclusion in a niche B2B category.
- PlanSwift and Buildxact G2 counts were not refreshed in this session.

---

## 7. Agency and retainer benchmarks: is $5,500/month for this scope cheap, market, or expensive?

### Takeaway
**$5,500/month is market-rate to slightly below market for a GEO retainer** (survey median ~$7,200/month; typical bands $3k–7k for monitoring and reporting, $7k–15k when content production is included). It is **extremely cheap per content asset**: **~$53 per asset** ($16,500 / 310), or ~$89 per website article if the whole fee went to articles. Freelance B2B SaaS articles cost **$150–$1,000+**.

The price is not the problem; **what the price implies about quality** is. Standard deliverables and KPIs in market offers are audits, prompt tracking, technical fixes, a modest number of high-quality pages, digital PR/listicle outreach and monthly reporting, not hundreds of articles.

### Cited Findings
**GEO/AEO agency pricing** (all from vendors or agencies selling GEO, so directional only) **[Likely/Speculative; search summary]**:
- Headline range: **$1,500 to $50,000+/month**. — [WebFX](https://www.webfx.com/blog/seo/generative-engine-optimization-cost/); [WebFX pricing](https://www.webfx.com/seo/pricing/ai-search-optimization)
- "Standard" retainer **$3,000–$7,000/month** (monitoring plus monthly reporting); "advanced" **$7,000–$15,000/month** (adds content production and technical implementation). Small-business retainers are **$2,000–$6,000/month**. — [Nutshell](https://www.nutshell.com/blog/geo-costs); [eSEOspace](https://eseospace.com/blog/geo-aeo-services-cost/); [dev.to Searchless](https://dev.to/searchless_ai/geo-pricing-guide-how-much-does-generative-engine-optimization-cost-in-2026-7i0) (the exact page for each band was not confirmed)
- Agency survey **[sample size not seen]**:
  - **68%** of agencies price GEO/AEO as a monthly retainer.
  - **Median custom retainer $7,200/month**, typical term **6 months**.
  - **Project/sprint median $14,500**, often used to test an agency.
  - Source: [Digital Agency Network](https://digitalagencynetwork.com/geo-pricing/); [Demand Local](https://www.demandlocal.com/blog/how-to-price-geo-services/) (attribution not confirmed)
- Engagement ranges of **$2,000–$25,000+/month**; four common models: tripwire audit, retainer, hybrid SEO+GEO add-on, white-label. — [Digital Agency Network](https://digitalagencynetwork.com/geo-pricing/) **[search summary]**
- **Tools** (DIY monitoring): **$10–$1,000+/month**. Otterly.AI is **$29/month for 15 prompts** (Lite) and **$489** (Premium). — [WebFX](https://www.webfx.com/blog/seo/generative-engine-optimization-cost/)

**Content cost**
- Freelance B2B posts **[Likely; vendor guides; some survey data dated 2022]**:
  - **$150–$400** for a ~1,000-word post from a qualified writer;
  - **$600–$1,000+** for technical subject-matter experts;
  - **$300–$900** for SaaS specialists;
  - **$350–$700** for a 1,200-word SaaS article.
  - Sources: [eesel](https://www.eesel.ai/blog/blog-writing-rates); [Superpath](https://superpath.co/blog/freelance-writers-rates)
- A serious B2B SaaS content programme costs **$5,000–$15,000/month**; managed content for seed teams **$1,500–$5,000/month**. — [The Rank Masters](https://www.therankmasters.com/insights/service-playbooks/saas-content-marketing-pricing) **[search summary]**

### Inferences
- **Unit economics** (my calculation):
  - $5,500 × 3 = **$16,500**.
  - Over 310 assets that is **$53/asset**. If all of it went to the 186 website articles, **$89/article**, with nothing left for monitoring, research, local GEO or competitor tracking.
  - Market freelance rates imply **$28k–$186k** for 186 articles at $150–$1,000 each.
  - The proposal can only be delivered profitably with mostly automated drafting. That is the scaled-content risk profile in Section 4.
- **"Original research" at this price** is likely a light survey or a desk compilation; real proprietary datasets cost more. **"Local GEO"** has low relevance for a national B2B SaaS unless Quotr sells regionally (for example, factory-direct materials logistics). Ask for the rationale.
- **Verdict:** the fee sits in the normal band for a small-company GEO retainer. Leanid should **renegotiate scope rather than price**:
  - **cut volume** to ~30–60 high-quality net-new pieces plus 30–60 refreshes over 90 days;
  - **add** a review-generation programme, outreach to the 5–8 AI-cited "best of" lists, 1 real data study, and multi-run, multi-engine monitoring with confidence intervals;
  - **tie the agency's KPIs to inputs and quality** (indexed, accepted, refreshed, outreach placements), with leading AI-visibility indicators as shared goals.
- **Standard agency KPIs** in the material found are: AI visibility/mention rate on a tracked prompt set, citation count, share of voice, AI referral sessions, branded search, and implementation milestones. Revenue or pipeline guarantees are rare, and guarantees of "#1 in ChatGPT" are a red flag. — [Intelligent Resourcing](https://intelligentresourcing.co/blogs/aeo-red-flags-evidence) **[search summary]**

### Gaps
- The agency pricing survey's sample size and author were not confirmed (pages not opened).
- No published price page from a construction-tech-specialist GEO agency was found.
- The proposal's internal split of the $5,500 between content and monitoring is unknown (TO CONFIRM with the agency).

---

## 8. Time-to-impact: how long until GEO changes show up in ChatGPT, Perplexity and AI Overviews, vs classic SEO

### Takeaway
No controlled study measures publish-to-citation latency. Vendor and practitioner estimates converge:
- **Perplexity:** ~1–5 weeks (retrieval at query time; fast recrawl).
- **ChatGPT search:** ~5–12 weeks.
- **Google AIO/AI Mode:** follows Google indexing and ranking, so weeks to months.
- **Unprompted "parametric" mentions** (from model training): **1–3+ quarters**, so not a 90-day lever.

Classic SEO: of new pages that reach the top 10 at all, ~41% do so within a month, but **most new pages never do**. Day-90 targets should therefore weight **fixes to existing, already-crawled pages** and **off-site inclusions**, not new-page volume.

### Cited Findings
- **GEO latency estimates** (vendors/agencies; none controlled) **[Speculative/Likely; search summary]**:
  - Perplexity can cite new content within **1–2 weeks**; ChatGPT **6–12 weeks**.
  - Another estimate: citations follow recrawl of key pages, typically **1–4 weeks**.
  - Another: Perplexity **3–5 weeks**, ChatGPT **5–8 weeks**, unprompted mentions after model retraining **1–3 quarters**.
  - Most clients see first citations in **8–12 weeks**.
  - Sources: [Frase](https://www.frase.io/blog/what-is-generative-engine-optimization-geo); [Growfusely](https://growfusely.com/blog/how-long-does-geo-take/); [VisibilityStack](https://www.visibilitystack.ai/signals/article/get-brand-cited-chatgpt-perplexity-answers); [Norvax](https://norvax.nl/en/blog/geo-getting-cited-by-chatgpt) (attribution of each figure to a specific page was not confirmed)
- **OpenAI** reportedly says robots.txt changes reach its search systems in **~24 hours**. That covers crawl access, not citation. — [Growfusely](https://growfusely.com/blog/how-long-does-geo-take/) **[search summary; OpenAI doc not opened]**
- **Cloudflare crawl-to-refer ratios** (Radar) **[Known for the July 2025 launch figures; 2026 figures secondary]**:
  - At the July 2025 launch: **Anthropic ~50,000:1, OpenAI 887:1, Perplexity 118:1** crawls per referral.
  - In 2026, a third-party tracker reports Perplexity rising from **296:1 (Jan 2026) to 2,373:1 (Sept 2026)** and Anthropic falling to **482:1 (Oct 2026)**.
  - Radar revised its crawl-purpose classification in 2026.
  - Sources: [Cloudflare blog](https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar); [Cloudflare crawl-to-click](https://blog.cloudflare.com/crawlers-click-ai-bots-training/); [SEOmator](https://seomator.com/blog/crawl-to-refer-ratio-ai-crawlers-llm-bots)
- **Classic SEO**: of new pages reaching the top 10, **40.82% did so within 1 month**, but only 1.74–6.11% of new pages reach the top 10 within a year. — [Ahrefs](https://ahrefs.com/blog/how-long-does-it-take-to-rank/) **[search summary]**
- **Indexing**: ~65% of tracked pages indexed within 30 days, ~77% within 3 months (IndexCheckr; biased sample). — [IndexCheckr](https://indexcheckr.com/resources/google-indexing) **[search summary]**
- **AirOps**: pages not refreshed in 90 days are 3x more likely to lose citations, so recency is an ongoing input. — [AirOps](https://www.airops.com/report/the-2026-state-of-ai-search)

### Inferences
- **Sequencing for days 1–90:**
  - **Days 1–30:** fix crawl access, stale facts and branded pages. Perplexity and ChatGPT will reflect these first, within ~1–6 weeks.
  - **Days 15–60:** rewrite "cited, not named" pages, launch comparison pages, start the review drive and list outreach.
  - **Days 45–90:** data asset and PR.
  - **Day-90 measurable effects:** mostly Perplexity/ChatGPT mention rate and branded accuracy, not Google rankings for new posts and not parametric mentions.
- Crawl-to-refer ratios show AI crawlers take far more than they send back. That is a further reason not to judge GEO by referral sessions alone.

### Gaps
- No controlled publish-to-citation latency study was found. The arXiv measurement papers could not be read.
- No engine publishes its index refresh frequency for ChatGPT search, Perplexity or Gemini grounding.

---

## 9. Benchmark summary table set (at a glance)

### Takeaway
The tables below put every key number from Sections 1–8 in one place, with source, sample, funder and confidence. Use **Known/Likely** rows in conversations with Quotr leadership; label **Speculative** rows as such if used at all.

### Cited Findings

**Table A: Traffic and conversion**

| Metric | Benchmark | Source (funder) | Sample / date | Confidence |
|---|---|---|---|---|
| AI referral share of all traffic | **1.08%** avg; **2.80%** IT sector | [Conductor](https://conductor.com/academy/aeo-geo-benchmarks-report/) (AEO vendor) | 3.3B sessions, 13k domains, US, May–Sep 2025 | Likely |
| AI referral share, mixed panel | **0.13%** of sessions | [Previsible](https://previsible.com/seo-strategy/ai-seo-study-2025/) (agency) | 19 GA4 properties, Jan–May 2025 | Likely (small panel) |
| AI referral share, B2B SaaS | **0.88%** | Usermaven via [Georankers](https://blog.georankers.ai/ai-search-visibility-benchmarks-b2b-saas/) | n/a | Speculative |
| AI referral growth | **+117% YoY** (≈ +21%/quarter) | [Similarweb](https://www.similarweb.com/blog/marketing/geo/gen-ai-stats/) | Global, Jun 2025–May 2026 | Likely |
| AI referral growth | **+527%** YoY; ~13.6%/month (≈ +47%/quarter) | [Previsible](https://previsible.com/seo-strategy/ai-seo-study-2025/); [secondary](https://driven-metrics.com/blog/ai-referral-traffic-statistics/) | 19 → 166 sites | Likely / secondary |
| ChatGPT share of AI referrals | **84–92%** | Previsible; Conductor | 2025–2026 | Likely |
| AI vs search conversion | **3x** (sign-ups 1.66% vs 0.15%) | [Microsoft Clarity](https://clarity.microsoft.com/blog/ai-traffic-converts-at-3x-the-rate-of-other-channels-study/) (owns Copilot) | 1,277 publisher sites, 1 month | Likely (publishers only) |
| AI vs organic conversion, SaaS | **23x** (0.5% of visits, 12.1% of signups) | [Ahrefs](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/) | Ahrefs only | Known (n = 1 company) |
| AI visitor value | **4.4x** organic (modelled) | [Semrush](https://www.semrush.com/blog/ai-search-seo-traffic-study/) | Projection | Speculative |
| ChatGPT vs organic conversion | **~13% worse** | [Kaiser & Schulze, Marketing Science](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0489) (academic) | 973 e-commerce sites, 12 months | **Known (peer-reviewed; e-commerce)** |
| B2B SaaS SEO visitor → lead | **2.1%**; site-wide 1.1% | [First Page Sage](https://firstpagesage.com/seo-blog/conversion-rate-benchmarks/) (agency) | Client data, opaque | Likely |
| Construction visitor → lead | **1.9%** (FPS) / **4.9%** broad (Ruler) | FPS; [Ruler via Octo](https://www.octoagency.io/blog/b2b-website-conversion-rate/) | 2025–2026 | Likely / conflicting definitions |
| Lead → MQL → SQL (SEO) | **41% → 51%** | First Page Sage | 2025 | Likely |

**Table B: Search CTR and zero-click**

| Metric | Benchmark | Source (funder) | Sample / date | Confidence |
|---|---|---|---|---|
| Click rate with vs without AI summary | **8% vs 15%** | [Pew](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) (independent) | 900 adults, 68,879 searches, Mar 2025 | **Known** |
| Pos-1 CTR loss with AIO | **−34.5% → −58%** | [Ahrefs](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update) | 300K keywords, Dec 2025 | Likely |
| CTR on AIO queries | **1.76% → 0.61% → 2.4%** (rebound) | [Seer](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update) (agency) | 53 brands, Jan 2025–Feb 2026 | Likely |
| CTR change with AIO | **−15.5%** avg; non-brand −20%; **brand +18.7%** | Amsive via [WordsAtScale](https://wordsatscale.com/ai-overviews-ctr-statistics-2026/) | 700K keywords, 10 sites, Apr 2025 | Likely |
| AIO prevalence, B2B tech keywords | **36% → 82%** (Feb 2025–Feb 2026) | BrightEdge via [Marqeable](https://www.marqeable.com/blog/ai-overviews-b2b-traffic/) | BrightEdge panel | Likely |
| AIO prevalence, brand searches | **64%** of 282 brands (Nov 2026) | BrightEdge via [Web Traffic News](https://webtrafficnews.com/briefs/brightedge-finds-ai-overviews-on-brand-searches-now-reach-64) | Nov 2026 | Likely |
| Zero-click Google searches (US) | **68%** | [SparkToro/Similarweb](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/) | Jan–Apr 2026 | Likely |
| AI Mode zero-click | **93%** | [Semrush](https://www.semrush.com/blog/google-ai-mode-seo-impact/) | 69M sessions, 2025 | Likely |

**Table C: AI visibility, volatility, reviews**

| Metric | Benchmark | Source (funder) | Sample / date | Confidence |
|---|---|---|---|---|
| Same brand list across runs | **<1%**; same order ~0.1% | SparkToro + Gumshoe ([SEJ](https://www.searchenginejournal.com/ai-recommendations-change-with-nearly-every-query-sparktoro/566242)) | 600 people, 12 prompts, 2,961 runs, Nov–Dec 2025 | Likely (commercial tie) |
| Runs per prompt to map recommendation set | **60–100** | Fishkin via [secondary](https://intelligentresourcing.co/blogs/aeo-red-flags-evidence) | — | Likely |
| Brand persists to next answer / 5 runs | **~30% / ~20%** | [AirOps](https://www.airops.com/blog/ai-search-volatility-why-brand-visibility-constantly-fluctuates-in-answer-engines) (vendor) | ~800 queries | Likely |
| Recommendations "not random" | — | [Conductor](https://www.conductor.com/academy/ai-recommendation-consistency-analysis/) (vendor) | 14,000 API calls | Likely (conflicts with SparkToro framing) |
| Challenger mention-rate gains | 3.2% → 22.2% in 1 month; 12% → 71% in 3 months | Profound/Ramp; [OTT SEO](https://www.overthetopseo.com/?p=59864) | Vendor/agency self-reports | **Speculative** |
| Brands absent from AI category answers | **89%** | Victorious via [SEJ](https://searchenginejournal.com/ai-brand-mention-study-victorious-spa/582765) | — | Likely |
| Review count ↔ ChatGPT rank | r ≈ **−0.16 to +0.02** | [Quoleady](https://www.quoleady.com/llmo-research/) (agency) | Mar 2026 | Likely |
| Named tools with review profiles | **99–100%** | Quoleady/[Promptwatch](https://promptwatch.com/blog/do-g2-capterra-help-chatgpt-recommendations) | 2026 | Likely |
| +10% reviews → citations | **+2%** | [G2](https://learn.g2.com/do-more-g2-reviews-mean-more-ai-visibility) (conflicted) | ~30k citations | Likely (vendor) |
| STACK reviews | Capterra **~1,396**; G2 **52–78** | [Capterra](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/); G2 | Feb–Mar 2026 | Known (Capterra) |
| PlanSwift reviews | Capterra **399**; G2 **33** | [Capterra compare](https://www.capterra.com/compare/70808-147181/PlanSwift-vs-STACK-Takeoff) | Mar 2026 | Likely |
| Togal.AI reviews | G2 **~60 (4.8)**; Capterra **0** | prior notes; Capterra | 2026 | Likely |
| Buildxact reviews | Capterra **~165–174 (4.6)** | prior notes | 2026 | Likely |
| Quotr reviews | G2 **~0**; no Capterra | prior notes | Sept 2026 | Likely |

**Table D: Content, indexing, time-to-impact, pricing**

| Metric | Benchmark | Source (funder) | Sample / date | Confidence |
|---|---|---|---|---|
| New pages reaching top 10 within 1 year | **1.74%** (random) / **6.11%** (real English content) | [Ahrefs](https://ahrefs.com/blog/how-long-does-it-take-to-rank/) | 1M / 2M URLs, 2023–2025 | Likely |
| Top-10 achievers ranking within 1 month | **40.8%** | Ahrefs | same | Likely |
| Pages indexed within 30 days | **~65%**; never indexed 62% (biased sample) | [IndexCheckr](https://indexcheckr.com/resources/google-indexing) (vendor) | ~16M pages, Feb 2025 | Likely (sample bias) |
| AI-generated share of #1 results | **7%** (Graphite); **~9–10%** (Semrush) | [Graphite](https://graphite.io/five-percent/ai-content-in-search-and-llms); Semrush | 31k keywords; 42k pages | Likely |
| Low-quality content reduction after Mar 2024 | **45%** | [Google](https://blog.google/products/search/google-search-update-march-2024/) | — | Known (Google claim) |
| Perplexity / ChatGPT time to first citation | **~1–5 wks / ~5–12 wks** | Vendor guides ([Growfusely](https://growfusely.com/blog/how-long-does-geo-take/)) | none controlled | Speculative |
| GEO retainer median | **$7,200/month**; bands $3k–7k (monitoring), $7k–15k (with content) | [Digital Agency Network](https://digitalagencynetwork.com/geo-pricing/); [Nutshell](https://www.nutshell.com/blog/geo-costs) | Agency survey, n unknown | Speculative/Likely |
| Freelance B2B SaaS article | **$150–$1,000+** | [eesel](https://www.eesel.ai/blog/blog-writing-rates); [Superpath](https://superpath.co/blog/freelance-writers-rates) | 2022–2026 | Likely |
| LinkedIn company-page reach | **~2–5%** of followers | [Ordinal](https://www.tryordinal.com/blog/the-declining-reach-of-linkedin-company-pages) | 2026 | Likely (vendor) |
| LinkedIn engagement, personal vs page | **2.6% vs 1.6%** (Metricool); **3.85% vs 2.10%** (Socialinsider) | [Contentin](https://contentin.io/blog/linkedin-content-statistics/) | 673,658 posts | Likely |

### Inferences
- Taken together, these benchmarks suggest Quotr's 90-day story should be built on **AI visibility (measured properly), branded accuracy, reviews and list inclusions**, with **qualified pipeline as a shared outcome**. Blog sessions and article counts should not be the headline.

### Gaps
- See the Gaps in each section above. The biggest: no construction-tech benchmarks exist for AI share, AI conversion or GEO case studies, and Quotr's own GA4, Search Console and CRM baselines are still TO CONFIRM.

---

## 10. Recommended KPI tree, conservative/base/stretch targets at day 30/60/90, and what Leanid should and should not own

### Takeaway
Leanid should **own measurement integrity and the leading TOFU indicators**:
- AI mention and citation rate (multi-run, multi-engine);
- branded-answer accuracy;
- reviews and list inclusions;
- branded search;
- AI referral sessions above market drift.

He should **share** the qualified-inbound outcome, defined against a seasonally fair baseline. He should **refuse** sole accountability for raw article counts, blog sessions, single-run AI rankings, competitor parity in 90 days, and revenue. Targets below are **inferences from Sections 1–9**, scaled for a small construction-tech SaaS. They should be re-based once day-0 measurement (protocol in Section 3) and Quotr's GA4, Search Console and CRM data are in.

### Cited Findings
- Benchmarks used are from Sections 1–8 and their sources: market drift of +21–47% per quarter in AI referrals; single-run CI of 0.6–15.7%; review inclusion-gate evidence; new-page ranking odds of 1.7–6%; first-citation latency of ~1–12 weeks.
- The prior KPI framework (L1–L10, G1–G5) and the suggested 90-day targets come from `geo-brain/07-measurement/kpis-and-dashboard.md` [prior notes]. The targets below stay consistent with it (for example, 90-day unbranded mention rate ≥9% on Perplexity) and add conservative and stretch bands plus 30/60-day checkpoints.

### Inferences

**KPI tree** (Day 0 = contract start, assumed early Dec 2026; Day 90 ≈ early Mar 2027)

```
OUTCOME (shared: Leanid + sales/founders)
└── O1 Qualified inbound leads / SQLs (ICP-fit demo requests) vs seasonally fair baseline
     └── O2 AI-influenced pipeline (GA4 AI channel first touch + "heard via ChatGPT/AI" self-report)

TOFU REACH (Leanid owns)
├── R1 Unbranded AI mention rate (fixed panel, 3–5 runs × ≥3 engines, with 95% CI)
├── R2 quotr.ai citation rate (same panel) + Search Console AI impressions / Bing AI citations
├── R3 Share of voice vs named competitors (same panel)
├── R4 Branded search impressions (GSC, namesakes filtered)
├── R5 AI referral sessions and share of sessions (GA4 custom channel), judged vs market drift
└── R6 Non-blog organic landing sessions (pricing, comparison, product) + GSC impressions (not blog clicks)

TRUST / ELIGIBILITY INPUTS (Leanid owns; agency executes part)
├── T1 Genuine reviews (G2 + Capterra/GetApp count; rating NOT a target)
├── T2 Independent "best of" / directory inclusions on AI-cited pages
├── T3 Branded-answer accuracy (errors on 8 brand prompts)
└── T4 Stale/conflicting facts on Quotr URLs (target 0)

PRODUCTION INPUTS (agency accountable; Leanid approves)
├── P1 Accepted assets meeting the QA rubric (not raw count)
├── P2 Indexed within 30 days of publish (GSC)
├── P3 Existing posts refreshed/merged ("cited-not-named" first)
└── P4 Monitoring delivered per protocol (raw run logs, not screenshots)
```

**Targets by checkpoint (conservative / base / stretch)**

*AI panel = fixed 32–50 unbranded prompts × 3–5 runs × ChatGPT + Perplexity + Google AI Mode/AIO; pooled rate with 95% CI. The Day-0 value is re-measured with this protocol. Perplexity single-run Sept 2026 was 3.1% mentioned / 12.5% cited / ~0.7% SOV.*

| KPI | Owner | Day 30 (C / B / S) | Day 60 (C / B / S) | Day 90 (C / B / S) | Rationale |
|---|---|---|---|---|---|
| **R1** Unbranded mention rate (pooled) | Leanid | Protocol live + Day-0 re-baseline / same / +1 "cited-not-named" prompt converted | Day-0 +1pp / +3pp / +5pp | **≥5–6% / ≥9% / ≥15%** | 2–3x baseline is plausible from converting cited-not-named prompts plus branded fixes. ~30% parity has no credible 90-day evidence (§3) |
| **R1a** Perplexity-only, core 32 | Leanid | — | 2 / 3 / 4 of 32 prompts (majority of runs) | **2 / 3 / 5 of 32** (6% / 9% / 16%) | Matches prior KPI doc (≥9% base). Perplexity reflects changes fastest (§8) |
| **R2** quotr.ai citation rate (Perplexity core 32) | Leanid | Hold ≥ baseline | ≥12% / ≥15% / ≥18% | **≥12% / ≥16% / ≥22%** | Merges may briefly shuffle cited URLs; new comparison and data pages add citations later |
| **R3** Share of voice | Leanid | — | ≥1% / ≥1.5% / ≥2.5% | **≥1.5% / ≥2–3% / ≥4–5%** | Competitors fill most answer slots; SOV lags mention rate |
| **R4** Branded search impressions (GSC) vs same-length prior period | Leanid | Baseline + namesake filter | Flat / +5% / +15% | **Flat / +10% / +25%** | Being named in AI answers shows up later as branded search; seasonality caveat |
| **R5** AI referral sessions vs Day-0 3-month average | Leanid | Channel live; Jan–Nov 2026 history pulled | +10% / +20% / +35% | **+25% / +50% / +100%** | Market drift alone is about +21–47% per quarter (§1); conservative ≈ drift, base beats drift |
| **R5a** AI share of sessions | Leanid | Measured | — | **≥0.5% / ≥1% / ≥2%** | Conductor all-industry 1.08%, IT 2.8%; Previsible 0.13% |
| **R6** Organic sessions, non-blog landing pages | Leanid | Baseline | Flat / +5% / +10% | **Flat / +10% / +20%** | Comparison and pricing pages convert. Blog sessions: **monitor only**, accept −15% to flat |
| **T1** Genuine reviews (G2 + Capterra) | Leanid (+ CS/founders) | Capterra/GetApp listing live; 2 / 3 / 5 reviews | 4 / 7 / 12 | **6 / 10 / 20** | Inclusion gate, not rank lever (§6). Depends on customer count (TO CONFIRM) |
| **T2** Independent AI-cited list/directory inclusions | Leanid (agency outreach) | Outreach list of 5–8 cited pages sent | 0 / 1 / 2 | **1 / 2–3 / 5** | Lists decide unbranded category answers (prior audit) |
| **T3** Brand prompts with errors (of 8) | Leanid | 4 / 3 / 2 | 3 / 2 / 1 | **3 / ≤2 / ≤1** | Stale-price fix shows in Perplexity within weeks; the Quotr Pro mix-up fades only as real reviews appear |
| **T4** Stale/conflicting-fact URLs | Leanid | **0** stale-price URLs (all bands) | 0 | 0 | Cheapest, fastest fix (prior audit) |
| **P1** Accepted net-new assets meeting the QA rubric | Agency | 8 / 12 / 16 | 20 / 30 / 40 cumulative | **30 / 45 / 60 cumulative** (not 186) | ≤~4–6/week of real quality beats ~15/week (§4) |
| **P2** Indexed ≤30 days after publish | Agency | ≥70% / ≥80% / ≥90% | same | same | IndexCheckr benchmark ~65% (biased low); a healthy small site should beat it |
| **P3** Existing posts refreshed/merged | Agency + Leanid | 10 / 15 / 20 | 25 / 35 / 45 | **35 / 50 / 60** (of 96) | Refresh beats new for AI citations (AirOps 3x churn on stale pages) |
| **O1** Qualified inbound (SQL/ICP demos), monthly, vs seasonally fair baseline | **Shared** | No target (too early) | No decline beyond seasonality / +5% / +10% | **Hold / +10–15% / +25–30%** | Few new pages rank in 90 days (§4); AI channel adds only a handful of leads (§1). Faster lift comes from CRO plus comparison pages |
| **O2** AI-influenced demos (GA4 + self-report) | Shared | "How did you hear" field live, ≥80% answered | Counted | **Counted and trended**; no volume target | Conversion of AI traffic unproven for B2B (§1) |

**Accountability: what Leanid should accept**
- **Measurement integrity:**
  - the protocol;
  - the GA4 AI channel;
  - the form field;
  - CRM source fields;
  - a monthly dashboard with confidence intervals.
- **Leading TOFU indicators R1–R6 and trust inputs T1–T4**, with targets expressed as ranges and judged over **two consecutive monthly readings**.
- **Agency management:** P1–P4 acceptance, and the quality rubric.
- **Shared ownership of O1**, provided the baseline is seasonally fair (year over year, or matched months) and sales owns qualification and follow-up speed.

**What Leanid should NOT accept accountability for (or should accept only as "monitor")**
- **Raw content output** (186/310 assets) as a success metric. It is an agency input; volume has low or negative marginal value (§4).
- **Blog/informational session growth.** It is structurally declining under AIO/AI Mode (§2): monitor it and explain it, but don't commit to growth.
- **"Rank #1 in ChatGPT/Perplexity"** or any single-run screenshot metric. Rank is noise (§3).
- **Competitor-parity share of voice (~30%) within 90 days.** No credible evidence supports it.
- **AI-referred lead volume targets** in the first 90 days. The volume is too small and conversion evidence conflicts (§1).
- **Revenue or closed-won within 90 days, MQL-to-SQL and SQL-to-win rates.** Sales cycle, pricing, product and sales process are outside marketing's control. Track them, don't own them.
- **Review star rating.** Can't be controlled ethically; it doesn't drive AI rank.
- **Google AIO CTR and zero-click rates.** These are platform-controlled.
- **Day-90 lead comparison against a June–October baseline without a seasonality adjustment.**

**Contract implications for the agency** (derived from the above):
- Month-1 KPI: replace "content output + indexing" with **"accepted assets (QA rubric) + ≥80% indexed within 30 days + fact cleanup complete + measurement protocol live"**.
- Day-90 KPI: replace sole "qualified inbound vs Jun–Oct baseline" with:
  - **R1/R2/T2 leading targets** (agency share);
  - plus **O1 as a shared, seasonally adjusted** goal.
- Require **raw prompt-run logs** (prompt, engine, date, run #, brands named, URLs cited), not dashboards alone.

### Gaps
- All absolute targets above need Quotr's own data to become numbers: monthly sessions by channel, GSC branded impressions, demos/SQLs for June–October 2026 and the prior year, and paying-customer count (for the review targets). All are TO CONFIRM.
- Construction-software lead seasonality is unknown. No benchmark was found, so the "seasonally fair baseline" rule is a method, not a number.
- The R1 percentage-point bands assume a Day-0 pooled baseline near 3–5%. If the multi-engine re-baseline comes in materially higher (for example, ChatGPT names Quotr more often than Perplexity), keep the *relative* multipliers (≈1.5x / 2–3x / 4–5x) rather than the absolute numbers.
