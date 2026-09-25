# GEO/AEO content strategy playbook for B2B SaaS (vertical and construction-tech focus), 2025–2026

Method note (read first): The research date is 2026-09-25. `mcp__Slashy__scrape_url` returned "Rate limit exceeded" on the first calls, so no full pages were read. Every finding below comes from WebSearch result summaries or Perplexity (`mcp__Slashy__web_search`) answers, and each links to the underlying URL. Numbers are copied as those summaries reported them. Before any figure goes on a slide, open the linked primary source to confirm it. Quality labels used below: **[Primary study]** = the organization that ran the analysis. **[Vendor/agency claim]** = a self-reported result from a company selling GEO services or tools. **[Secondary]** = an aggregator or blog restating someone else's data. **[Opinion]** = practitioner advice without published data.

---

## 1. Which content types earn AI citations and mentions in B2B SaaS

### Takeaway
The strongest data points to four formats: comparison/"vs" content, product and landing pages (including pricing and feature detail), list-style "best X" roundups, and pages carrying original, number-dense data. How they are built also matters: an answer near the top, clear titles and URLs, and dated specifics. However, 82–93% of SaaS citation weight comes from third-party domains, and self-serving "best X" listicles where the vendor ranks itself #1 were penalized in early 2026. Owned content is the "corroboration base", not the whole strategy.

### Cited Findings
**Format-level citation data**
- HubSpot's State of AEO 2026 plus Wix Studio's AI Search Lab (over 1M AI citations combined) found that across AI Overviews, Gemini, ChatGPT and Perplexity only three content types average above a 65% citation rate: product listings/landing pages (68.5%), blog posts (66.75%) and listicles (66%). Comparison content is 4th at 62.75%. Documentation, PR, user reviews and news all average below 60%. **[Primary study, vendor-run]** — [HubSpot: On-page content formats answer engines favor](https://blog.hubspot.com/marketing/content-format-types-that-earn-citations)
- Per engine in the same data: ChatGPT favors comparison content (95% citation rate, the highest of any format on any engine) and documentation/resources (86%). Perplexity favors product listings/landing pages (84%). — [HubSpot](https://blog.hubspot.com/marketing/content-format-types-that-earn-citations)
- ZeroClick Labs: across industries, listicles take 33.8% of citation share, product pages 28% and homepages 11.3%. In B2B technology services, listicles take 61% of citations. Each industry has a distinct page-type "citation fingerprint". **[Vendor/agency study]** — [ZeroClick Labs AI SEO study](https://zeroclicklabs.ai/ai-seo-study-content-types-ai-search/)
- A B2B SaaS benchmark says every page ChatGPT cited used list structure, and roughly 3 in 4 had a year in the title (e.g., "…in 2026"). **[Vendor/agency study]** — [Averi B2B SaaS citation benchmarks 2026](https://www.averi.ai/how-to/chatgpt-vs.-perplexity-vs.-google-ai-mode-the-b2b-saas-citation-benchmarks-report-(2026))
- Evaluation-stage ChatGPT prompts cited product pages 24.1%, comparison content 13.3% and listicles 13.2% (via a GoGoChimp summary of Ten Speed data). "Best X" listicles were 43.8% of ChatGPT-cited page types in another dataset. **[Secondary]** — [GoGoChimp GEO for SaaS](https://www.gogochimp.com/blog/geo-for-saas)
- Technical documentation, integration guides and API references reportedly get 3× more AI citations than marketing blog posts (DerivateX, May 2026). **[Vendor/agency claim]** — [DerivateX AI search trends B2B SaaS](https://derivatex.agency/blog/ai-search-trends-b2b-saas/)
- Pricing pages: one compilation reports they are most cited on Perplexity (77.1%) and least on Google AI Overviews (38.1%). **[Secondary, weak methodology visibility]** — [SlateHQ](https://slatehq.com/blog/how-to-get-cited-by-chatgpt-perplexity-claude-and-gemini)

**Where citations actually come from (owned vs third-party)**
- Aleyda Solis analyzed 15 leading SaaS brands across 3 US subverticals (Semrush citation data for ChatGPT and Google AI Mode, plus Similarweb AI referral data). Third-party sources carry 84–93% of citation weight, e.g., 92.1% (ChatGPT) and 93.4% (AI Mode) in CRM/sales, and 83.6%/84.1% in accounting/finance. Brands' own domains hold only ~10–11% of the top 150 source slots but are "mention-dense". Her conclusion: AI search is "a 3rd-party citation problem with an on-page corroboration base" (published Aug 2026). **[Primary study]** — [Aleyda Solis: AI Search Is a 3rd-Party Citation Problem](https://www.aleydasolis.com/en/ai-search/ai-search-citations/); [Aleyda Solis: What It Takes for SaaS Brands to Win in AI Search](https://www.aleydasolis.com/en/ai-search/saas-ai-search-optimization/)
- In the same SaaS data, ChatGPT favors structured written content (tech publications, review sites) and often cites homepages and canonical brand pages. Google AI Mode favors deeper content (guides, documentation, templates, integrations) plus video, social and creator content. Video was 1.0% of cited sources in ChatGPT vs 23.0% in AI Mode; technology publications were 7.7% vs 0.5%. — [Aleyda Solis SaaS findings](https://www.aleydasolis.com/en/ai-search/saas-ai-search-optimization/)

**Original research and data**
- Growth Memo (Kevin Indig) looked at 301 pages that AI cited across 316 prompts and 7 verticals (1,075 citations). Only 8 pages were primary research, yet they earned 8.4% of citations: 11.3 citations per page vs 3.4 for everything else, about 3.3× the density. AI rewards "almost to the exclusion of everything else" one format: the benchmark that answers "which is best". **[Primary study]** — [Growth Memo: Why most original data never gets cited](https://www.growth-memo.com/p/why-most-original-data-never-gets); [Search Engine Land summary](https://searchengineland.com/why-most-original-data-never-gets-cited-481676)
- Growth Memo (June 29, 2026): proprietary data is "necessary but not sufficient". The entity types that best predict ChatGPT citations are DATE and NUMBER, and highly cited pages are dense with specific entities (a named methodology, a precise statistic, a named comparison). Winners have proprietary product, usage or pricing data, structure it for extraction, and keep building brand authority off-site. **[Primary study/analysis]** — [Growth Memo: Why proprietary data is your most defensible AI citation asset](https://www.growth-memo.com/p/why-proprietary-data-is-your-most)

**On-page structure signals**
- Across 1.2M AI answers and 18,012 verified citations, 44.2% of ChatGPT citations came from the first 30% of a page's content, 31.1% from the middle (30–70%), and deep content was about 2.5× less likely to be cited. This is the "ski ramp" pattern. The 10–20% band is where AI reads hardest, while the first 10% (nav and intro filler) is often skipped. **[Primary study]** — [Search Engine Land: 44% of ChatGPT citations come from the first third](https://searchengineland.com/chatgpt-citations-content-study-469483); [Growth Memo: The science of how AI picks its sources](https://www.growth-memo.com/p/the-science-of-how-ai-picks-its-sources)
- Ahrefs, 1.4M ChatGPT prompts: cited pages had titles more semantically similar to ChatGPT's internal fan-out sub-queries than pages it passed over. Matching the narrower sub-queries correlated more strongly than matching the broad prompt. Pages with descriptive URL slugs were cited 89.78% of the times they appeared in results vs 81.11% for less descriptive URLs. About half of retrieved pages were cited overall. (Date conflict: the summary mentions both "February 2025" and "ChatGPT 5.2 prompts".) **[Primary study]** — [Ahrefs: Why ChatGPT cites one page over another](https://ahrefs.com/blog/why-chatgpt-cites-pages/)
- Ahrefs, 75K brands: number of site pages barely correlates with AI visibility (~0.194). **[Primary study, correlation only]** — [Ahrefs: Top brand visibility factors in ChatGPT, AI Mode, AI Overviews](https://ahrefs.com/blog/ai-brand-visibility-correlations/)

**Risk: self-promotional "best X" listicles and scaled comparison pages**
- Lily Ray documented steep visibility drops at SaaS/B2B sites that rank themselves first in "best of" listicles. Organic visibility fell 30–50% within weeks; one B2B company lost 49% between Jan 21 and Feb 2, 2026, and others lost 43%, 42%, 38%, 34% and 29%. The hardest-hit patterns were mass-produced "best X" listicles, self-promotional comparison pages, scaled competitor "alternatives" pages, spammy structured data, and posts "lightly refreshed with '2026' in the title". — [Search Engine Land: Google may be cracking down on self-promotional listicles](https://searchengineland.com/google-cracking-down-self-promotional-best-of-listicles-468227); [ALM Corp summary](https://almcorp.com/blog/self-promotional-listicles-google-rankings-2026/)
- Follow-up (Lily Ray study as summarized by ALM Corp): when a company's own self-promotional listicle was cited in AI Overviews, that company was omitted from the actual recommendation 69% of the time. Ranking yourself #1 can end up helping competitors. **[Secondary summary of primary study]** — [ALM Corp: Ranking yourself #1 may help competitors in AI Overviews](https://almcorp.com/news/self-promotional-listicles-ai-overviews-help-competitors-lily-ray-study/)
- Visibility lost in Google can carry into ChatGPT, Perplexity and others that lean on Google's index for retrieval. — [Search Engine Land](https://searchengineland.com/google-cracking-down-self-promotional-best-of-listicles-468227)

**Free tools, calculators and templates**
- Claims that "tool-shaped pages are gaining share in assistant citations" appear only in blog commentary, with no dataset. **[Opinion]** — [BoilerplateHub: Engineering as marketing](https://boilerplatehub.com/blog/engineering-as-marketing-free-tools)
- Google AI Mode cites templates and integrations pages for SaaS (qualitative finding). — [Aleyda Solis SaaS findings](https://www.aleydasolis.com/en/ai-search/saas-ai-search-optimization/)

**Video**
- YouTube is about 23.3% of all Google AI Overview citations (Surfer, 46M citations, May 2026), ahead of Wikipedia (18.4%). BrightEdge puts YouTube at 29.5% of AIO citation share and reports a 25% rise in YouTube AIO citations since Jan 2024. **[Secondary summaries of primary studies]** — [BrightEdge: YouTube's growing impact on AI Overviews](https://www.brightedge.com/blog/youtubes-growing-impact-google-ai-overviews-what-marketers-need-know); [5W YouTube citation share report](https://www.5wpr.com/research/youtube-ai-citation-share-report-2026/)

### Inferences
- For Quotr, the evidence points to four owned priorities:
  - **Honest comparison/"vs" pages.** These already exist (e.g., "Quotr.ai vs Togal.AI"). Keep them factual, include tables, and state where the competitor is better. The Lily Ray data warns against scaled, self-ranked-#1 versions.
  - **Product, feature and pricing pages that answer the fan-out sub-queries.** Examples: "AI takeoff for residential framing", "takeoff software pricing per seat", "bid management for subcontractors". Descriptive titles and URL slugs matter.
  - **An original benchmark.** Quotr's estimation service and factory-direct procurement generate proprietary cost and pricing data, e.g., a quarterly "residential material cost per sq ft by trade/region" index or "takeoff time: manual vs AI" benchmarks. This is exactly the "which is best / what does it cost" benchmark format that Growth Memo found earns 3.3× citation density.
  - **Trade-specific how-to and documentation/tutorial content**, written answer-first.
- Do not build a library of "Best AI takeoff software 2026" listicles that rank Quotr #1 on quotr.ai. The early-2026 penalty and the 69% "omitted from own listicle" finding make this net-negative. Get onto third-party lists instead (section 3).
- Because third parties carry 82–93% of SaaS citation weight, owned content's main GEO job is to be the canonical, verifiable source of facts (what Quotr is, pricing, trades supported, integrations, accuracy claims) that third-party mentions and AI answers can corroborate.

### Gaps
- No construction-tech-specific study of which page types AI cites for "takeoff/estimating software" prompts was found. The sibling note `competitor_geo_benchmark.md` / `quotr_ai_visibility_tests.md` may cover observed citations.
- No dataset quantifies citation lift from free calculators or templates. Evidence is opinion only.
- Podcast and webinar transcript impact on AI citations: no data found.
- The HubSpot "citation rate" methodology (the denominator) was not visible in snippets, so treat its percentages as directional.

---

## 2. Optimizing existing content vs creating new

### Takeaway
Refresh first. Pages that already rank or are already retrieved are the cheapest wins: update the facts, move the answer to the top, and restructure into self-contained passages whose titles match sub-queries. Then create new assets only where prompt research shows a gap and the page offers something AI cannot synthesize elsewhere (original data, decision support, tools). Date-only "refreshes" and mass content volume do not work, and the date-only kind now carries penalty risk.

### Cited Findings
**Freshness evidence**
- Ahrefs, 17M citations across 7 AI platforms: AI-cited URLs are on average 25.7% "fresher" than Google organic results. ChatGPT shows the strongest recency preference: in-text references are 393 days newer and citations 458 days newer than organic results. Google AI Overviews cite the oldest content (average ~1,432 days). Time since last update: 909 days for AI-cited vs 1,047 for organic (13.1% gap). ChatGPT and Perplexity tend to list newer sources first. (Study published 2025.) **[Primary study]** — [Ahrefs: AI assistants prefer to cite fresher content](https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/)
- Roughly half of AI citations trace to content published or substantively updated in the last 13 weeks. Perplexity reportedly shows up to 142% higher citation rates for content updated within 30 days. **[Secondary; the original dataset is not identified]** — [Salespeak](https://salespeak.ai/aeo-news/content-freshness-ai-search/); [NoGood](https://nogood.io/blog/content-freshness-ai-citations/)
- Nuance: AI shows no generic preference for "new". It prefers content that matches queries whose answers have changed. Changing a publish date without changing the content "is increasingly discounted". **[Secondary/opinion]** — [NoGood](https://nogood.io/blog/content-freshness-ai-citations/); [Parse](https://parse.gl/blog/content-freshness-ai-visibility)

**How to refresh (practitioner guidance)**
- Ahrefs: avoid republishing with no real changes. A meaningful refresh replaces outdated stats with current sourced figures, swaps aged examples, adds emerging subtopics and updates screenshots. Start with the top 20% of pages by traffic, then declining pages with low keyword difficulty (Top Pages report / Search Console comparisons). Re-promote updated pages (email, social, internal links). **[Opinion from a data vendor]** — [Ahrefs: Republishing content for SEO & AI](https://ahrefs.com/blog/republishing-content/); [Ahrefs: Fresh content](https://ahrefs.com/blog/fresh-content/)
- Aleyda Solis's AI Search Optimization Checklist (updated Sep 2026) sequence:
  1. Define the prompts and journeys to influence.
  2. Measure current AI presence before changing anything.
  3. Diagnose gaps.
  4. Make priority pages retrievable and extractable: chunk-level, self-contained passages, with the direct answer in the first 1–2 sentences under each heading.
  5. Build decision-support content.
  **[Opinion/framework]** — [Aleyda Solis: AI Search Optimization Checklist](https://www.aleydasolis.com/en/ai-search/ai-search-optimization-checklist/)
- Aleyda Solis's Content Prioritization framework scores each content type on:
  - **Click resilience:** will users still need to visit after the AI answer, e.g., to interact, verify live details or complete an action?
  - **Citation potential:** does the page hold unique, verifiable, primary information?
  - **Brand mention potential:** is there a genuine reason to associate the brand with the topic?

  Another generic definition or templated guide "is unlikely to generate meaningful, incremental value". Sites still matter when users need an official source, original evidence, current or personalized info, decision help, or a place to act. **[Framework/opinion]** — [Aleyda Solis: Content prioritization in an AI search era](https://www.aleydasolis.com/en/ai-search/content-prioritization-ai-search/)

**Does ranking = citation? (which existing pages to prioritize)**
- Ahrefs: across 15,000 prompts, only 12% of links cited by ChatGPT, Gemini and Copilot appear in Google's top 10 for the same prompt. — [Ahrefs: Only 12% of AI cited URLs rank in Google's top 10](https://ahrefs.com/blog/ai-search-overlap/)
- Ahrefs: only 38% of AI Overview citations now come from top-10 pages, down from 76% in earlier analysis. — [Ahrefs: 38% of AI Overview citations pull from the top 10](https://ahrefs.com/blog/ai-overview-citations-top-10/); [SEJ coverage](https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/)
- BrightEdge (16 months of AIO data): AIO citation overlap with organic rankings grew from 32% to 54%, but only 16.7% of citations come from top-10 results. — [BrightEdge: AI Overview citations now 54% from organic rankings](https://www.brightedge.com/resources/weekly-ai-search-insights/rank-overlap-after-16-months-of-aio)
- The published overlap estimates range from 12% to 93%, so ranking is neither necessary nor sufficient. **[Secondary synthesis]** — [ALM Corp](https://almcorp.com/blog/google-ai-overview-citations-drop-top-ranking-pages-2026/)
- Ahrefs 1.4M prompts: title and URL match to ChatGPT's narrower fan-out queries predicts citation. Retitling and re-slugging existing pages to match sub-questions is therefore a refresh lever. — [Ahrefs](https://ahrefs.com/blog/why-chatgpt-cites-pages/)

**Evidence that new, purpose-built pages can move visibility quickly**
- Ramp (Profound case, March 2025): Profound data showed AI engines citing automation, AI and software-comparison content. Ramp then built pages specifically for AI pickup: "Accounts Payable Software for Small Businesses", "…for Large Businesses", "Top 6 Accounts Payable Automation Software" and "AI in Accounts Payable". AP visibility rose from 3.2% to 22.2% in 1 month (7×). **[Vendor case study]** — [Profound: How Ramp increased AI brand visibility 7x](https://www.tryprofound.com/customers/ramp-case-study)

**Volume is not the lever**
- Ahrefs, 75K brands: site page count correlates only ~0.194 with AI visibility. — [Ahrefs](https://ahrefs.com/blog/ai-brand-visibility-correlations/)
- The early-2026 penalties targeted mass-produced listicles and "2026"-in-title refreshes with little real update. — [Search Engine Land](https://searchengineland.com/google-cracking-down-self-promotional-best-of-listicles-468227)

### Inferences
- A practical sequence for Quotr (synthesized from Aleyda Solis, Ahrefs and Growth Memo):
  1. Build a prompt set of 50–150 buyer prompts by persona (sub, GC, developer) × trade × job-to-be-done (takeoff, estimate, bid, materials pricing).
  2. Baseline visibility and cited sources.
  3. Refresh existing pages that are retrieved or ranking. Put an answer-first summary in the top ~30%, add fresh dated numbers and comparison tables, give each H2 a self-contained passage, and use descriptive titles and URLs that mirror sub-queries.
  4. Consolidate thin or duplicate blog posts and "2026" retitles.
  5. Create net-new assets only where there are gaps: original cost benchmarks, trade-specific decision guides ("takeoff software for drywall subs"), persona pages (small sub vs multi-family developer), a pricing explainer and honest comparisons.
- Ramp's segmentation ("for small businesses" / "for large businesses") maps directly onto Quotr's personas, e.g., "AI takeoff software for small residential subcontractors" vs "…for multi-family developers".
- Because ChatGPT shows the strongest recency bias and AIO the weakest, a quarterly refresh cadence on commercial pages (pricing, comparisons, benchmarks) is more valuable than refreshing evergreen how-tos. This inference comes from the Ahrefs platform differences.

### Gaps
- No controlled study was found isolating the effect of adding FAQ blocks or FAQ schema on AI citations. Claims seen were agency anecdotes.
- No published data on consolidation/pruning's effect specifically on AI citations. Only the 2026 penalty evidence exists, which is indirect.
- The SEJ-reported "76%" earlier baseline for AIO top-10 overlap comes from a different Ahrefs dataset, so the two are not like-for-like.

---

## 3. Off-site / earned tactics and their evidence of impact on AI visibility

### Takeaway
Off-site signals are the strongest correlates of AI brand visibility: branded web mentions, YouTube mentions, earned media, review sites and professional content on LinkedIn. Community platforms matter, but their citation share swings violently. Reddit lost most of its ChatGPT citations twice (Sept 2025, Aug 2026). Build broad, genuine third-party presence rather than betting on one platform.

### Cited Findings
**Mentions and YouTube**
- Ahrefs, 75K brands (updated 2026):
  - YouTube mentions (in titles, transcripts and descriptions) are the strongest correlate of AI visibility (~0.737) across ChatGPT, AI Mode and AI Overviews.
  - Branded web mentions: 0.66–0.71.
  - ChatGPT correlates more weakly with classic authority: branded search volume 0.352, Domain Rating 0.266.
  - In the original AIO study, web mentions (0.664) far outweighed backlinks (0.218). Brands in the top quartile of web mentions earn up to 10× more AIO mentions than the next quartile.

  Spearman correlation, not causation. **[Primary study]** — [Ahrefs: Top brand visibility factors](https://ahrefs.com/blog/ai-brand-visibility-correlations/); [Ahrefs: AI Overview brand correlation](https://ahrefs.com/blog/ai-overview-brand-correlation/); [BusinessWire, May 26 2026](https://www.businesswire.com/news/home/20260526119691/en/Across-75000-Brands-YouTube-Mentions-Are-the-Strongest-Signal-of-AI-Visibility-New-Ahrefs-Report-Reveals)

**Earned media / digital PR**
- Muck Rack's "What Is AI Reading?" (May 2026, 25M+ links across ChatGPT, Claude and Gemini): earned media accounts for 84% of AI citations. That covers journalism, academic, government, encyclopedic and third-party corporate content. Journalism alone is 27%; paid/advertorial is 0.3%. The share has held between 82% and 89% since July 2025. **[Primary study, PR-vendor-run]** — [Muck Rack blog](https://muckrack.com/blog/what-is-ai-reading-may-2026); [GlobeNewswire release](https://www.globenewswire.com/news-release/2026/05/07/3290268/0/en/generative-pulse-earned-media-consistently-drives-ai-citations-holding-at-84.html)
- For B2B commercial queries, AI tends to pull from niche reviews, vendor pages, specialist publications and trusted community sources. Aggregate "Reddit and Wikipedia dominate" stats come from broad query sets and mislead for industry-specific buyer prompts. **[Opinion, Search Engine Land contributor]** — [Search Engine Land: Stop chasing Reddit and Wikipedia](https://searchengineland.com/reddit-wikipedia-what-drives-ai-recommendations-472580)

**Review platforms (G2/Capterra)**
- G2's March 2026 survey of 1,076 B2B software buyers: daily AI-chatbot "power users" cite review sites as their #1 confidence signal (50%). — [G2 2026 AI Search Insight Report](https://learn.g2.com/g2-2026-ai-search-insight-report); [G2 press release](https://www.prnewswire.com/news-releases/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots-302742807.html)
- Semrush citation data shows Perplexity emphasizing Reddit, LinkedIn and G2 for B2B queries. **[Secondary summary of Semrush]** — [Search Engine Land: AI search engines cite Reddit, YouTube, LinkedIn most](https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138)
- Growth Memo analysis for G2 (Feb 2026; ~35,000 ChatGPT citation URLs, US, Dec 2025): UGC platforms out-cite review sites at every stage of the buyer journey. **[Primary study, commissioned by G2]** — [Growth Memo: community signals](https://www.growth-memo.com/p/community-signals-are-ais-largest)

**Reddit and communities (high volatility)**
- Semrush (30M sources): Reddit was the most-cited domain across ChatGPT, AI Mode, Gemini, Perplexity and AIO, followed by YouTube and LinkedIn. — [Search Engine Land](https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138); [Semrush most-cited domains](https://www.semrush.com/blog/most-cited-domains-ai/)
- But Ahrefs (1.4M prompts) found ChatGPT retrieves Reddit heavily (a dedicated ref_type with 16M+ data points) yet cites it only 1.93% of the time. Reddit informs the answer but rarely gets credit. — [Ahrefs](https://ahrefs.com/blog/why-chatgpt-cites-pages/); [SEJ](https://www.searchenginejournal.com/chatgpt-often-retrieves-but-rarely-cites-reddit-pages-data-shows/572243/)
- Sept 2025: Reddit's share of ChatGPT citations collapsed. Figures vary by tracker: 29.2%→5.3%, 14%→2% (Promptwatch), or 14.29%→0.21% (Spotlight). This was linked to Google removing the num=100 parameter. — [Rocketblue](https://rocketblue.ai/articles/chatgpt-stopped-citing-reddit-in-september-what-this-means-for-your-ai-visibility-strategy/); [Seeking Alpha](https://seekingalpha.com/news/4500600-reddit-shares-fall-steeply-ahead-of-the-opening-bell)
- Aug 2026: Reddit fell from an average 3.83% of ChatGPT Search citations (Jul 18–Aug 7) to 0.52% by mid-August, an 86.4% drop per Promptwatch. Axios frames GEO as "a rapidly moving target" that requires presence on many channels. — [Axios, Aug 20 2026](https://www.axios.com/2026/08/20/chatgpt-reddit-citations-geo-strategy); [Promptwatch](https://promptwatch.com/blog/chatgpt-stop-citing-reddit)
- The Drum asked whether the brand rush to Reddit contributed to the drop. This is speculation. — [The Drum](https://www.thedrum.com/news/did-the-brand-rush-to-reddit-kill-the-platform-s-chatgpt-citations)

**LinkedIn (founder-led content)**
- Semrush (325,000 prompts, Jan–Feb 2026; 89K LinkedIn URLs cited by ChatGPT Search, AI Mode and Perplexity):
  - LinkedIn appears in 11% of AI responses on average, is #2 overall, and is #1 for professional topics.
  - LinkedIn *articles* are 50–66% of cited LinkedIn content; feed posts are 15–28%.
  - The median cited post has only 15–25 reactions and ≤1 comment, so relevance beats popularity.
  - 54–64% of cited posts share knowledge or practical advice.
  - ChatGPT Search and AI Mode more often cite individual creators (59%); Perplexity cites Company Pages (59%).

  **[Primary study]** — [Semrush LinkedIn AI visibility study](https://www.semrush.com/blog/linkedin-ai-visibility-study/)

**Wikipedia / Wikidata**
- Wikipedia is 47.9% of citations among ChatGPT's top-10 most-cited sources (Profound, 2025). — [Profound: AI platform citation patterns](https://www.tryprofound.com/blog/ai-platform-citation-patterns)
- Vendor opinion: Wikidata feeds Google's Knowledge Graph and has a lower notability bar than Wikipedia. A complete Wikidata entry is achievable and useful for entity recognition. **[Opinion]** — [Agility PR](https://www.agilitypr.com/pr-news/pr-tech-ai/wikipedia-now-accounts-for-nearly-half-of-chatgpts-top-citations-many-brands-are-getting-the-work-catastrophically-wrong/)
- A 2026 arXiv preprint surfaced in search reports higher LLM hallucination rates for entities without Wikipedia pages (118,785 outputs, 15 LLMs, 7,919 entities). The exact paper is unverified: it is one of [arXiv 2606.21595](https://arxiv.org/pdf/2606.21595) or [arXiv 2607.20925](https://arxiv.org/pdf/2607.20925).

**Cited-in-AI brands also win clicks**
- Seer Interactive (53 brands, 5.47M queries, 2.43B impressions, Jan 2025–Feb 2026): brands cited inside AI Overviews get 35% more organic clicks and 91% more paid clicks than non-cited brands on the same SERP. **[Primary study]** — [Seer: AIO impact on Google CTR 2026 update](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update)

### Inferences
- Off-site priorities for Quotr, ranked by evidence strength:
  1. **YouTube.** Trade-specific residential demos, "vs" walkthroughs and customer jobs with "Quotr" said aloud and in titles and descriptions. This targets the strongest correlate and AI Mode/AIO's heavy video citation.
  2. **Earned media in construction trade press.** For example ENR, Construction Dive, For Construction Pros, Pro Builder, JLC and Remodeling. Pitch original cost/benchmark data, not just funding news.
  3. **Third-party "best AI takeoff/estimating software" roundups and review sites.** G2, Capterra and Software Advice, with steady review generation.
  4. **Founder LinkedIn articles.** Long-form, practical advice; low engagement is fine.
  5. **Transparent, disclosed participation in r/estimators** and similar threads, treated as a trust and demand channel rather than a citation play, given the volatility.
  6. **A Wikidata entity.** Low cost, helps disambiguation from "Quotr Pro" and generic "quote".
- Integration marketplaces (e.g., a Procore App Marketplace listing, QuickBooks) are plausible third-party corroboration sources, but no data on their AI citation impact was found.

### Gaps
- No study quantifies AI visibility impact from podcasts or construction trade shows.
- No construction-specific breakdown of which third-party domains AI cites for takeoff/estimating prompts was found here. See the sibling `quotr_offsite_presence.md`.
- No causal (vs correlational) evidence for the YouTube and mentions findings.

---

## 4. Measuring GEO: tools, analytics, KPIs and cadence

### Takeaway
Use a three-layer stack:
1. **Prompt-level visibility:** mention rate, share of voice, citation rate and sentiment across engines, from a fixed prompt set tracked monthly.
2. **Traffic:** GA4's native AI Assistant channel (since May 2026) plus a custom regex channel, plus AI-crawler log analysis.
3. **Business impact:** self-reported attribution on demo/trial forms, CRM fields, branded search lift.

AI answers are highly volatile (40–60% of cited domains change month to month) and differ by engine (91% of citations appear on only one platform). Single snapshots mislead.

### Cited Findings
**Analytics**
- On May 13, 2026, Google Analytics 4 added a native "AI Assistant" channel to the Default Channel Group, assigning medium "ai-assistant" to recognized AI chatbot referrers. It is not retroactive, and some AI visits still land in Direct or Referral (in-app browsers, pasted links). — [Search Engine Journal](https://www.searchenginejournal.com/google-analytics-adds-ai-assistant-as-default-channel-group/574974/); [WebFX](https://www.webfx.com/blog/ai/google-analytics-ai-assistant-traffic/)
- Conflict on coverage: one summary says Google named ChatGPT, Gemini and Claude as examples. Another says the June 2026 docs list ChatGPT, Gemini, DeepSeek, Copilot and Grok, and that Perplexity still routes to "Referral". Verify in GA4 docs, and keep a custom channel group anyway. — [Brandon Caples](https://brandoncaples.com/2026/ga4-ai-assistant-channel); [Insightland](https://insightland.org/blog/how-to-track-chatgpt-perplexity-and-gemini-traffic-in-ga4-a-complete-2026-setup-guide/)
- Custom channel group: Admin → Data display → Channel groups. Use a regex such as `chatgpt\.com|chat\.openai\.com|perplexity\.ai|gemini\.google\.com|copilot\.microsoft\.com|claude\.ai` and drag the AI rule above Referral, because rules evaluate top to bottom. — [Swydo](https://www.swydo.com/blog/track-ai-traffic-in-ga4/); [Terminus](https://www.terminusapp.com/blog/ai-traffic-channel-in-ga4/)

**Benchmarks**
- Conductor 2026 AEO/GEO Benchmarks (13,770 enterprise domains, 3.3B sessions, released Nov 2025):
  - AI referral traffic = 1.08% of all website traffic, growing ~1% month over month; IT sector ~2.80%.
  - ChatGPT = 87.4% of AI referrals, then Perplexity 4.8%, Claude 2.1%, Gemini 1.9%.

  **[Primary study]** — [Conductor benchmarks](https://www.conductor.com/academy/aeo-geo-benchmarks-report/); [BusinessWire](https://www.businesswire.com/news/home/20251113364791/en/Conductor-Unveils-2026-AEO-GEO-Benchmarks-Report-How-AI-Shapes-Brand-Visibility-in-a-Zero-Click-World)
- Kevin Indig H1 2026: ChatGPT's share of AI-search activity fell from 78% to 56% in six months, while Gemini rose to 30% and Claude to 10%. 91% of citations appear in only one of ChatGPT, Perplexity or AIO. AI Mode reached 1B MAU with queries ~3× longer than classic search. The central H1 2026 theme is that "AI's impact kept growing faster than anyone's ability to measure it". — [Growth Memo: AI Halftime Report H1 2026](https://www.growth-memo.com/p/ai-halftime-report-h1-2026); [Search Engine Land](https://searchengineland.com/ai-halftime-report-h1-2026-483912)
- Conversion quality: Ahrefs' AI search visitors were 0.5% of its traffic but drove 12.1% of signups, about 23× the conversion of organic search. Semrush (2026) reports AI visitors convert at 4.4× organic across industries. — [Ahrefs](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/); [Averi summary](https://www.averi.ai/blog/ai-search-visitors-convert-23x-higher.-everyone-s-ignoring-it.)

**Volatility → cadence**
- Profound (240M ChatGPT citations): 40–60% of cited domains change month to month for identical queries. One-month domain drift: AIO 59.3%, ChatGPT 54.1%, Copilot 53.4%, Perplexity 40.5%. Over six months, 70–90% of cited domains differ. — [Profound: AI search volatility](https://www.tryprofound.com/blog/ai-search-volatility)
- Practitioner guidance: run a fixed set of 20–50 buyer-intent prompts across ChatGPT, Claude, Gemini, Perplexity and AI Mode monthly. Record mention, position, description and cited sources, and compare against the same prompt set. Weekly mostly measures noise, and changes take weeks to propagate. Core KPIs: presence/mention rate, share of voice, citation rate, average position, sentiment, AI-referred traffic, pipeline and revenue. **[Opinion]** — [Semrush: How to measure AI search visibility](https://www.semrush.com/blog/measure-ai-visibility/); [TrackMyVisibility KPI guide](https://trackmyvisibility.com/blogs/ai-visibility/guide-to-ai-visibility-kpis/)
- Aleyda Solis offers a 3-layer framework (AI presence, readiness, business impact) with a workbook, plus guidance on building a representative prompt library. **[Framework]** — [Aleyda Solis: 3-layer measurement framework](https://www.aleydasolis.com/en/ai-search/a-3-layer-framework-to-measure-ai-presence-readiness-and-business-impact-redefining-metrics-for-the-ai-search-era/); [Aleyda Solis: prompt library](https://www.aleydasolis.com/en/ai-search/ai-search-prompt-library/)

**Self-reported attribution**
- Asking "how did you hear about us" catches LLM influence that analytics miss. Tally is cited as letting users specify the queries they used. Pair this with Search Console, a GA4 AI channel and demo-form fields. **[Opinion]** — [Semrush measurement guide](https://www.semrush.com/blog/measure-ai-visibility/)
- An anecdotal B2B SaaS writeup claims $2.4M in qualified pipeline was previously misattributed until AI referrers were captured in GTM, GA4, CRM and self-reported fields. **[Unverified anecdote]** — [LinkedIn Pulse](https://www.linkedin.com/pulse/how-we-tracked-24m-hidden-ai-referred-revenue-b2b-saas-abbas-vilmf)

**Tools (pricing from third-party comparisons, verify before quoting)**
| Tool | Entry price | Positioning |
|---|---|---|
| Otterly.AI | from ~$29/mo | Cheapest; lightweight monitoring for small teams |
| Peec AI | ~€89–199/mo | Mid-market and agencies |
| Scrunch | from ~$250/mo | Enterprise-leaning; acquired by Sitecore in June 2026 for ~$225M |
| Profound | from ~$499/mo | Enterprise |
| Semrush AI Toolkit | — | Fits teams already on Semrush |

Sources: [Kime comparison](https://kime.ai/blog/best-ai-visibility-tools); [Ryze pricing compilation](https://www.get-ryze.ai/blog/ai-visibility-tools-pricing-compared-2026); [Sitecore press release](https://www.sitecore.com/company/newsroom/press-releases/2026/06/sitecore-acquires-scrunch-to-help-brands-influence-discovery--and-buying-decisions); [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-03/sitecore-said-to-acquire-scrunch-for-225-million)
- Other trackers: Ahrefs Brand Radar tracks any brand's AI visibility, and Semrush publishes an AI Visibility Index (126M prompts). — [Ahrefs Brand Radar](https://ahrefs.com/brand-radar); [Semrush AI Visibility Index release](https://www.semrush.com/news/463141-semrush-releases-expanded-2026-ai-visibility-index-analyzing-126-million-ai-search-prompts/)

**Crawler logs**
- Cloudflare-derived crawl-to-referral ratios, July 2026: ClaudeBot ~2,237:1, GPTBot ~217:1, Google ~4.6:1. Server logs show whether AI bots can reach and fetch key pages, but crawl volume says little about referrals. **[Secondary summary of Cloudflare Radar]** — [SEOmator](https://seomator.com/blog/crawl-to-refer-ratio-ai-crawlers-llm-bots); [Something Inc](https://somethinginc.com/blog/ai-crawler-economics-cloudflare-data/)
- llms.txt: an SE Ranking analysis of 300K domains found no measurable link to AI citations. An Ahrefs 137K-domain study found 97% of llms.txt files received no requests in a month. Google's docs say Search ignores it. Low priority. — [SEJ on SE Ranking study](https://www.searchenginejournal.com/llms-txt-shows-no-clear-effect-on-ai-citations-based-on-300k-domains/561542/); [SE Ranking](https://seranking.com/blog/llms-txt/)

### Inferences
- For a seed-stage team like Quotr:
  - **Tracking:** a mid-tier prompt tracker such as Peec or Otterly, or Semrush/Ahrefs if already licensed. Track about 50–100 prompts segmented by persona and trade, monthly, across ChatGPT, AI Mode/AIO, Gemini, Perplexity and Claude.
  - **Analytics:** GA4 native AI channel plus custom regex (to catch Perplexity).
  - **Forms:** a required "How did you hear about us?" field on demo/trial forms with ChatGPT, Google AI, YouTube, Reddit and Facebook group options.
  - **CRM:** tag AI-sourced deals.
  - **Quarterly report:** branded search trend in Google Search Console.
- Report KPIs by engine, not as one blended score. Citations barely overlap across engines, and ChatGPT's share is falling as Gemini/AI Mode grow.

### Gaps
- No published benchmark for AI referral share or AI visibility specifically for construction software. Conductor's "Industrials" page exists, but its figure was not retrieved: [Conductor Industrials benchmarks](https://www.conductor.com/academy/industrials-aeo-geo-benchmarks/).
- No verified vendor pricing pages were read. The prices above are from third-party comparisons.

---

## 5. Case studies (2024–2026) of B2B SaaS growing AI visibility or AI-referred pipeline

### Takeaway
Credible, numbers-backed public cases exist mainly for horizontal SaaS: Vercel, Ahrefs, Ramp and Webflow. Most "6×/3×" GEO case studies are agency self-reports with anonymized clients. No public construction-tech or vertical-contractor SaaS GEO case study with verified numbers was found. That absence is itself an opening for Quotr to publish its own.

### Cited Findings
- **Vercel** (founder tweets, 2025): ChatGPT referred 4.8% of new signups, "growing very fast" from <1% six months earlier. Shortly after, ChatGPT referred 10% of new signups, which had also accelerated. **[Primary, founder statement]** — [Guillermo Rauch on X (4.8%)](https://x.com/rauchg/status/1898122330653835656); [Guillermo Rauch on X (10%)](https://x.com/rauchg/status/1910093634445422639)
- **Ahrefs** (own data): AI search was 0.5% of visitors but 12.1% of signups (~23× conversion vs organic). **[Primary]** — [Ahrefs](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/)
- **Ramp** (Profound, Mar 2025): AP-category AI visibility went from 3.2% to 22.2% in one month (7×) after publishing segment pages ("AP software for small/large businesses"), a "Top 6 AP automation software" comparison and "AI in accounts payable". **[Vendor case study]** — [Profound Ramp case study](https://www.tryprofound.com/customers/ramp-case-study)
- **1840 & Co** (Profound): went "from invisible to top 5" with 11% AI visibility in remote staffing. **[Vendor case study; tactics not retrieved]** — [Profound 1840 & Co case](https://www.tryprofound.com/customers/1840-co-answer-engine-optimization-case-study)
- **Webflow:** 8% of signups from LLM traffic, converting 6× vs Google Search. **TestRail:** 2,000+ LLM referral visits and 25–30 qualified trial signups per month. **[Secondary via agency blog; primary source not located]** — [Virayo LLM SEO](https://virayo.com/blog/llm-seo/)
- **Anonymized B2B SaaS** (Discovered Labs): AI-referred trials went from 575 to 3,500+ in 7 weeks, with a "600% citation uplift" across ChatGPT, Claude and Perplexity. Tactics: 66 optimized articles, technical SEO fixes and Reddit seeding. **[Agency self-report]** — [Discovered Labs case](https://discoveredlabs.com/case-studies/b2b-saas-4x-ai-referred-trials-aeo-strategy)
- **Anonymized B2B SaaS** (Capston): AI-attributed trial signups went from 47/mo to 210/mo, and AI became 28% of pipeline. **[Agency self-report]** — [Capston case](https://capston.ai/case-study-b2b-saas-geo/)
- **Gumlet:** reportedly 20% of monthly inbound revenue from ChatGPT, Perplexity and Claude after entity-definition restructuring and category content. **REsimpli:** reportedly the #1 CRM recommended in ChatGPT for "real estate crm" within 90 days. **[Agency blog claims]** — [DerivateX](https://derivatex.agency/blog/losing-customers-to-chatgpt-recommendations/)
- **Construction-adjacent:** an agency case for a Denver general contractor (a services firm, not SaaS) rebuilt Organization, LocalBusiness, Project and Article schema and cleaned up construction-directory citations to grow AI mentions. The numbers were not visible in the snippet. **[Agency case]** — [Incrementors construction firm GEO case](https://www.incrementors.com/case-studies/construction-firm-geo/)
- **Negative case:** the SaaS/B2B sites in Lily Ray's early-2026 analysis lost 29–49% of organic visibility after scaling self-promotional listicles and alternatives pages. — [Search Engine Land](https://searchengineland.com/google-cracking-down-self-promotional-best-of-listicles-468227)

### Inferences
- The repeatable pattern across credible cases:
  1. Find the prompts and cited-source types where the brand is absent (Ramp).
  2. Publish segment-specific and comparison pages that answer those prompts directly.
  3. Instrument attribution (Vercel and Ahrefs could quantify because they tracked signup source).
- Quotr could run a Ramp-style 60–90-day sprint: 5–8 persona/trade pages plus 2–3 honest comparison pages plus one original benchmark, with before/after prompt tracking. That would produce its own case study, which is also PR fodder.

### Gaps
- No public GEO case study with numbers from construction tech was found: Procore, Buildertrend, JobTread, Togal, STACK, Kreo, ServiceTitan, Jobber and Housecall Pro all came up empty. A Perplexity query on this returned a 502 error and was not retried.
- The Webflow, TestRail, Gumlet and Mentimeter figures could not be traced to company-published primary sources.

---

## 6. How construction buyers (estimators, contractors, GCs, developers) use AI and research software, 2025–2026

### Takeaway
AI use among contractors roughly doubled into 2026:
- 52% of construction firms use AI tools (Houzz, mid-2026).
- 61% use AI or plan to increase investment (AGC/Sage, Jan 2026).
- 23–24% apply it to estimating (AGC/Sage; ServiceTitan).

Trust is mixed: Autodesk found construction trust in AI down 14 points, and data accuracy is the top concern. Across B2B software generally, half of buyers now start research in an AI chatbot. No construction-specific survey measuring chatbot use *for software research* was found. Peers, reviews, YouTube, communities and trade events remain the observed channels, but the evidence for the share each channel takes is thin.

### Cited Findings
**AI adoption among contractors**
- AGC/Sage 2026 Construction Hiring & Business Outlook (Jan 2026): 61% of firms use AI or plan to increase AI investment (up from 44%). Uses: 45% office/admin, 23% estimating, 20% design/preconstruction, 16% HR/recruiting/training. **[Primary survey]** — [AGC 2026 Outlook report (PDF)](https://www.agc.org/sites/default/files/users/user21902/2026%20Construction%20Hiring%20and%20Business%20Outlook%20Report_Final2.pdf); [AGC news release](https://www.agc.org/news/2026/01/08/contractors-have-dampened-expectations-2026-apart-data-centers-and-power-projects-amid-worries-about)
- Houzz 2026 survey (601 US construction and design businesses, June–July 2026):
  - 52% of construction firms use AI tools for business tasks (+20 pts vs 2025), 34% are exploring, 14% have no plans.
  - 80% of users use AI daily.
  - Top functions: sales and marketing 64%, planning and design 61%, project/client management 59%, admin 52%, operations 45%.
  - 52% save 3+ hours per week.

  **[Primary survey, via trade press]** — [Roofing Contractor: Houzz survey](https://www.roofingcontractor.com/articles/102644-ai-use-jumps-among-construction-firms-houzz-survey-finds); [Houzz 12 key takeaways](https://www.houzz.com/magazine/12-key-takeaways-on-ai-in-home-design-and-construction-stsetivw-vs~185587907)
- Unverified: a search summary attributed "ChatGPT 43.7%, Copilot 16.9%, Gemini 8.5%" tool adoption among construction pros to the Houzz report, but the origin is unclear. Do not use without checking. — [Roofing Contractor](https://www.roofingcontractor.com/articles/102644-ai-use-jumps-among-construction-firms-houzz-survey-finds)
- ServiceTitan 2026 Commercial Specialty Contractor Industry Report (1,000+ construction leaders, released Mar 30 2026): 38% report measurable business impact from AI (vs 17% in 2025). AI is applied to cost estimation/budgeting (24%) and bid management (22%). **[Primary survey, vendor-run]** — [ServiceTitan press release](https://www.servicetitan.com/press/servicetitan-report-finds-ai-adoption-more-than-doubles-among-commercial); [For Construction Pros](https://www.forconstructionpros.com/construction-technology/project-management/article/22963634/servicetitan-industry-report-finds-ai-adoption-accelerating-across-commercial-construction)
- Dodge Construction Network + CMiC "AI for Contractors" (235 GCs and trade contractors, Sep–Oct 2025; published Dec 2025):
  - 87% expect AI to have a meaningful impact, but only 19% have adapted workflows.
  - Concerns: data accuracy 57%, security 54%.
  - Only 26% rate their own data quality as high.
  - Automated proposal generation was rated 92% effective and contract risk review 86%.

  **[Primary survey]** — [BusinessWire](https://www.businesswire.com/news/home/20251205015633/en/New-Research-Reveals-Strong-Contractor-Optimism-About-AIs-Transformative-Impact-on-Construction-Industry); [Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/); [Dodge report page](https://www.construction.com/resource/ai-for-contractors/)
- Autodesk 2025 State of Design & Make: construction leaders' trust in AI fell 14 points year over year. 68% believe AI will enhance the industry, down from 80% in 2024. Concerns include cybersecurity, privacy and data control. **[Primary survey, 2025]** — [Autodesk Digital Builder](https://www.autodesk.com/blogs/construction/state-of-design-make-spotlight-construction/); [Autodesk AI hype cycle](https://www.autodesk.com/design-make/research/state-of-design-and-make-2025/ai-hype-cycle)

**B2B software buyers generally (not construction-specific)**
- G2 (March 2026 survey of 1,076 B2B software buyers):
  - 51% start software research with an AI chatbot more often than Google (up from 29% in April 2025), and 71% use chatbots somewhere in research.
  - 80%+ sourced a recommendation from a chatbot in the past two years.
  - 69% chose a different vendor than planned because of chatbot guidance, and one-third bought from a vendor they had never heard of.
  - 85% think more highly of a vendor mentioned by AI.
  - 40% say evaluation is now the longest stage.

  **[Primary survey, review-site-run]** — [G2 press release](https://www.prnewswire.com/news-releases/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots-302742807.html); [G2 Answer Economy](https://company.g2.com/news/g2-research-the-answer-economy); [G2 2026 Buyer Behavior Report](https://sell.g2.com/2026-buyer-behavior-report)

**Construction software buying behavior**
- Capterra construction software buyer insight: estimating is the most-requested feature among buyers, while accounting ranks most critical among actual users. Buyers expect to spend about $1,600–$4,000 per year. Pricing and ease of use dominate selection. (Report date not visible, probably 2024–2025.) — [Capterra Buyer Insight Report: Construction Software](https://www.capterra.com/resources/construction-software-buyer-insight/)
- Gartner Digital Markets (8,000+ advisor phone interactions with mostly SMB construction buyers, Aug 2023–Aug 2024): 45% of organizations handle operations manually, 30% use third-party software and 12% have no system. Buyers research on Capterra, GetApp and Software Advice (900+ construction tools listed). This sample is biased toward buyers who contacted Gartner. **[Primary, dated 2023–2024]** — [Gartner Digital Markets construction buyer insights](https://www.gartner.com/en/digital-markets/insights/stand-out-in-your-category-with-construction-buyer-insights)
- Software Advice: of 5,000+ conversations with construction software buyers in the past year, 72% asked about estimating. (Page date is 2026, but the underlying period is unclear.) — [Software Advice cost estimating software](https://www.softwareadvice.com/construction/cost-estimating-software-comparison/)
- The Farnsworth Group's Building Products Customer Guide (~2,000 DIYers and pros, 2025/2026 editions) covers online, social, in-person and manufacturer resources that specialty contractors, builders and remodelers use to evaluate products. An older Farnsworth survey of 413 pros found 76% have personal social media accounts (date not stated; treat as older). — [Farnsworth 2026 Building Products Customer Guide](https://www.thefarnsworthgroup.com/landing-page/building-products-customer-guide); [Farnsworth: Targeting contractors through social media](https://www.thefarnsworthgroup.com/blog/targeting-contractors-through-social-media)
- Construction workers largely learn technology informally from peers or online services; only 20% were trained by IT. (Older Construction Dive article, likely 2023.) — [Construction Dive](https://www.constructiondive.com/news/workers-give-construction-a-thumbs-down-for-tech/649625/)
- Reddit r/estimators threads in 2025–2026 ask whether AI takeoff tools work and are skeptical ("hit-or-miss"). This was observed in the sibling research note via Perplexity. — [r/estimators: is there an AI automated takeoff software tool](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/)
- Perplexity's synthesis says estimators use ChatGPT for "first-pass research and tool shortlisting". It says Facebook estimator groups, YouTube demos and trade shows (World of Concrete, IBS/NAHB) are common discovery venues, but it explicitly notes "no single survey quantifies the share" by channel. **[Inference by an AI engine; not survey-backed]** — [Civils.ai ChatGPT comparison](https://civils.ai/compare/chatgpt); [RICS AI in construction 2025](https://www.rics.org/news-insights/optimism-high-for-ai-in-construction-but-skills-shortages-and-integration-challenges-adoption)

### Inferences
- The addressable audience now uses AI daily (80% of Houzz AI users). "Sales and marketing" is the top AI use case, and estimating/bid management is the #2–3 operational use. Quotr's buyers are likely already asking ChatGPT or Gemini questions such as "best takeoff software for residential framing" or "how much does drywall cost per sq ft". This applies G2's cross-industry 51%/71% figures to a lagging but fast-moving industry.
- Construction buyers' stated trust concerns are data accuracy (57%) and falling trust in AI (Autodesk −14 pts). GEO content should therefore lead with verifiable accuracy evidence: side-by-side takeoff comparisons, error rates, customer job examples with numbers. That also matches the DATE/NUMBER entity finding.
- Capterra shows estimating is the most-searched need, with budgets around $1,600–$4,000 per year. Quotr's Lite tier ($79.90/seat/mo ≈ $959/yr) fits inside this range, which makes transparent pricing content a GEO asset.
- Given how thin the construction-specific channel data is, Quotr's own "How did you hear about us?" data (section 4) will be the best evidence on channel mix within 1–2 quarters.

### Gaps
- No construction-specific survey (AGC, Dodge, Procore, Autodesk, JBKnowledge, Deloitte, McKinsey) was found that measures how contractors research *software* or how often they use AI chatbots for vendor research. JBKnowledge's ConTech report appears discontinued after ~2021; not verified.
- No quantitative data on Facebook groups or YouTube channels as software discovery sources for estimators.
- Deloitte and McKinsey 2025–2026 construction AI reports were not retrieved in this pass.

---

## 7. Keeping and growing top-of-funnel reach while shifting to GEO

### Takeaway
Informational clicks are structurally lower where AI Overviews appear, but being cited in the AI answer recovers some clicks. AI referral traffic is still small (~1% of traffic) but converts far better. Protect top of funnel with two moves:
- Invest in "click-resilient" content (tools, original data, decision support) and in off-site reach (YouTube, LinkedIn, trade press, communities) that feeds both humans and AI.
- Re-baseline top-of-funnel KPIs from sessions to visibility: mentions, share of voice, branded search.

### Cited Findings
- Seer Interactive:
  - Organic CTR on queries with AI Overviews fell 61%, from 1.76% to 0.61% (3,119 informational queries).
  - In the larger 2026 dataset (53 brands, Jan 2025–Feb 2026), AIO organic CTR rebounded from 1.3% in Dec 2025 to 2.4% in Feb 2026, an 85% increase.
  - Cited brands get 35% more organic and 91% more paid clicks.

  Note: the summary also says 2.4% "is still a long way from the 1.76% baseline", which is internally inconsistent. The datasets and baselines likely differ; check the primary page. — [Seer Interactive 2026 update](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update)
- AI Overviews trigger on ~48% of tracked queries, up 58% year over year (BrightEdge data via secondary). **[Secondary]** — [BrightEdge weekly insights](https://www.brightedge.com/resources/weekly-ai-search-insights)
- AI referral traffic is ~1.08% of all site traffic, growing ~1% month over month (IT sector ~2.8%). — [Conductor 2026 benchmarks](https://www.conductor.com/academy/aeo-geo-benchmarks-report/)
- Growth Memo: "visibility, not raw referral traffic, is becoming the main currency of organic search". UGC (Reddit threads, YouTube demos, forums) absorbs roughly a third of the traffic AI Overviews leave behind. — [Growth Memo: community signals](https://www.growth-memo.com/p/community-signals-are-ais-largest)
- Aleyda Solis's "click resilience" dimension: prioritize content where users still need to visit, i.e., to interact, verify live details, inspect evidence or complete an action. De-prioritize generic definitions and guides that AI can fully summarize. — [Aleyda Solis content prioritization](https://www.aleydasolis.com/en/ai-search/content-prioritization-ai-search/)
- G2: buyers reach shortlists faster via AI, and one-third bought from a vendor they had never heard of before. AI inclusion can create awareness at the top of funnel. — [G2 press release](https://www.prnewswire.com/news-releases/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots-302742807.html)

### Inferences
- For Quotr, the top-of-funnel content most resilient to AI summarization:
  - interactive tools (e.g., a free residential material/area calculator or a "takeoff time saved" estimator)
  - regularly updated cost benchmarks from Quotr's procurement and estimation data
  - trade-specific video walkthroughs
  - honest comparison and decision guides

  Generic "what is a construction takeoff" explainers will lose clicks. Keep them only as short, answer-first corroboration pages that link to tools and benchmarks.
- Report top of funnel as AI share of voice on the priority prompt set, branded search volume, YouTube views and mentions, and review counts. Keep sessions alongside, but drop them as the sole KPI.

### Gaps
- No construction-vertical data on AIO prevalence or CTR loss for estimating/takeoff queries.
