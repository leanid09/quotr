---
type: guide
description: Evidence-rated table of what drives AI citations and mentions (September 2026), with vendor-bias flags.
last_verified: 2026-09-25
verify_every_days: 90
---
# Signals That Matter for AI Visibility (Evidence Table, September 2026)

> [!abstract] What this page is for
> One evidence-rated list of the factors linked to a brand being cited, mentioned or recommended by AI answer engines: how strong the evidence is, which studies say so (date, publisher, sample, link), whether the study comes from a vendor, and whether the factor is rising or falling in importance. It ends with what matters more in 2026 than in 2024, and what this means for Quotr.ai.

> [!info]- Sources
> Research notes [[geo_ai_citation_signals_2026]] (§2–§4), [[geo_content_playbook_b2b]] (§1–§3), corrected by [[verification_geo_evidence]] (claims #9–#20, hype flags H1–H20, outdated items O1–O12, new items M1–M10; these corrections override the notes); Quotr test results from [[quotr_ai_visibility_tests]]; the final report [[Quotr GEO AEO strategy audit]] (section "Signals: proof from others now beats on-page tricks"). Studies are linked in each row.

---

## How to read this page

**Strength of evidence**

| Label | Meaning |
|---|---|
| **Strong** | Official platform statements, or several large independent datasets pointing the same way. |
| **Moderate** | Consistent but mostly observational (correlation) data, or one strong dataset. |
| **Weak** | Thin, mixed or conflicting data; or only practitioner opinion. |
| **Myth** | Evidence points the other way, or the platform itself says it does not matter. |

**Vendor flag.** "Vendor" means the study comes from a company that sells SEO, AI-visibility, review or PR products, so it has a commercial interest in the result. Vendor studies are not wrong by default, but treat them as directional.

**Correlation is not causation.** Nearly all large studies below are observational: they show that brands with X also tend to have AI visibility, not that adding X causes it. Big brands tend to have more of everything ([[verification_geo_evidence|verification H7]]).

**Trend** compares 2026 with 2024–25: **rising** (matters more), **stable**, **falling** (matters less).

**Checked?** Items marked "[read]" or "confirmed" were re-checked by the fact-check file on 2026-09-25. Items marked "not re-checked" come from the research notes only. Do not headline them without opening the source.

---

## The short version

- **Best-supported:** other people talking about you (brand mentions, community, video, reviews, independent lists) and plain good SEO (being indexed and ranking). Google says there is no separate "AI trick" beyond valuable, unique content; a peer-reviewed benchmark (C-SEO Bench, NeurIPS 2025) found most on-page GEO tricks "largely ineffective".
- **Rising:** YouTube, community/social sources, original data with specific numbers and dates, being **named** (not just footnoted), consistent entity facts.
- **Falling or weak:** backlinks as a stand-alone signal, page volume, keyword density, schema as an AI lever, llms.txt, date bumps, self-ranking listicles, betting on one platform.

---

## 1. Evidence summary table

| # | Factor | Strength | Key evidence (short) | Vendor study? | Trend |
|---|---|---|---|---|---|
| 1 | **Brand mentions on other sites** | **Strong** (correlation) | Ahrefs 75K brands: branded web mentions 0.656–0.709, far above backlinks; Aleyda Solis: 82.3% of SaaS top-cited sources are third-party | Mostly yes (Ahrefs); Aleyda is a consultant | **Rising** |
| 2 | **YouTube presence and mentions** | **Moderate–strong** (correlation) | Ahrefs: YouTube mentions ~0.737, strongest correlate; YouTube most-cited domain in AI Overviews; largest SaaS source domain (Aleyda) | Yes (Ahrefs) | **Rising** |
| 3 | **Reddit and community (UGC)** | **Moderate**, very volatile | Peec AI 30M sources: Reddit #1 domain; Aleyda: social/community 45.7% of SaaS sources; ChatGPT's Reddit share collapsed twice | Yes | **Stable overall, falling in ChatGPT** |
| 4 | **Reviews (G2, Capterra etc.)** | **Moderate** | Quotr tests: Capterra and G2 each fed 9 of 32 answers; G2 survey: 45% trust review-site citations most (G2 is interested); Aleyda: news/review only 10.4% | Yes (G2 has a direct interest) | **Stable to rising** for software prompts |
| 5 | **Third-party "best X" lists** | **Moderate–strong** for category prompts | Ahrefs: "best X" listicles = 43.8% of page types ChatGPT cites; Quotr tests: the same few editorial lists recur | Yes (Ahrefs) | **Stable** (third-party); **falling** for self-published ones |
| 6 | **Backlinks / domain authority** | **Weak–moderate** | Ahrefs: backlinks 0.218 and Domain Rating 0.266–0.326, well below mentions | Yes | **Falling** (relative to mentions) |
| 7 | **Classic search visibility (indexed, ranking)** | **Strong** (official + peer-reviewed) | Google: indexed + snippet-eligible is the requirement; C-SEO Bench: traditional SEO "significantly more effective"; 38% of AIO citations rank top 10 | Mixed (Google official; Ahrefs vendor; C-SEO academic) | **Stable** as the base; top-10 overlap **falling** |
| 8 | **Branded search volume** | **Moderate** (correlation) | Ahrefs: 0.392 (AIO), 0.352 (ChatGPT) | Yes | **Stable** |
| 9 | **Freshness (real updates)** | **Moderate**, engine-dependent | Ahrefs 17M citations: AI-cited URLs ~25.7% fresher; ChatGPT strongest, AI Overviews weakest; cited pages still ~2.9 years old | Yes | **Stable** (rising in ChatGPT) |
| 10 | **Structure (answer-first, headings, tables)** | **Moderate** as good practice; unproven as a lever | Indig: 44.2% of ChatGPT citations from the first 30% of a page; Microsoft recommends headings and short sections; Google says no chunking needed | Mixed | **Stable** |
| 11 | **Original data, specific numbers and dates** | **Moderate**, rising | Google's guide: "non-commodity content"; Growth Memo: primary research pages got 3.3x more citations per page; DATE and NUMBER entities best predict ChatGPT citations | Growth Memo is an independent analyst | **Rising** |
| 12 | **Adding statistics, quotations, source citations (GEO-paper tactics)** | **Weak** as a trick | GEO paper (KDD 2024): up to ~40% in a lab benchmark; C-SEO Bench (NeurIPS 2025): such methods "largely ineffective", gains shrink as competitors copy | No (academic) | **Falling** |
| 13 | **Schema / structured data** | **Weak** for AI citation | Google: no special schema; Microsoft: recommends it; SSRN study: negative pooled association, likely confounded | Mixed | **Stable** (hygiene) |
| 14 | **Author expertise / E-E-A-T signals** | **Weak** (no direct AI data) | No robust study found linking bylines or E-E-A-T markup to AI citation | — | **Unknown** |
| 15 | **Entity consistency (same facts everywhere)** | **Moderate** (our inference, supported by Quotr's tests) | Perplexity hedged on Quotr's factory count and funding because sources disagreed | No (own tests) | **Rising** |
| 16 | **Wikipedia / Wikidata** | **Moderate** for Wikipedia (big share, but hard to get); **weak** for Wikidata | Wikipedia top ChatGPT domain (Muck Rack, May 2026); share swung sharply in 2025; Wikidata benefit is opinion only | Yes | **Falling / volatile** in ChatGPT |
| 17 | **LinkedIn (especially founder articles)** | **Moderate** | Semrush 325K prompts: LinkedIn in 11% of AI responses, #2 domain overall; articles are 50–66% of cited LinkedIn content | Yes | **Rising** |
| 18 | **Earned media / press** | **Moderate** | Muck Rack 25M+ links: "earned" sources 84% of citations, journalism ~27%; for SaaS, news/review only 10.4% (Aleyda) | Yes (PR vendor) | **Stable** |
| 19 | **Content length** | **Weak** (both work) | Long pages collect more citations in total; focused pages win per query; Ahrefs: "both work" | Mixed | **Stable** |
| 20 | **Content volume (number of pages)** | **Myth** | Ahrefs 75K brands: page count ~0.194, "almost no relationship"; Google spam policy on scaled content | Yes (Ahrefs) | **Falling** |
| 21 | **Multimedia beyond YouTube (images, podcasts)** | **Weak** (no solid data) | No quantitative study found | — | **Unknown** |
| 22 | **Crawler access and rendering** | **Strong** (prerequisite) | OpenAI: don't block OAI-SearchBot to be included; Anthropic: blocking Claude-SearchBot may reduce visibility; Google: must be indexed | No (official) | **Stable** |
| 23 | **llms.txt** | **Myth** (for citations) | SE Ranking 300K domains: no correlation; Google: not needed, treated like any file | Yes (SE Ranking) | **Falling** |

---

## 2. Evidence details, factor by factor

### 1. Brand mentions on other sites — Strong (correlation) · Rising

- **Ahrefs, "Top Brand Visibility Factors in ChatGPT, AI Mode, and AI Overviews"** (Dec 12, 2025; press release May 26, 2026; 75,000 brands; vendor). Branded web mentions correlated **0.656–0.709** with AI visibility depending on the surface; Domain Rating 0.266–0.326; page count ~0.194. Spearman correlation. Confirmed by the fact-check. [Ahrefs](https://ahrefs.com/blog/ai-brand-visibility-correlations/); [BusinessWire](https://www.businesswire.com/news/home/20260526119691/en/Across-75000-Brands-YouTube-Mentions-Are-the-Strongest-Signal-of-AI-Visibility-New-Ahrefs-Report-Reveals)
- **Ahrefs, "An Analysis of AI Overview Brand Visibility Factors"** (2025; 75,000 brands; vendor). Web mentions 0.664, branded anchors 0.527, branded search volume 0.392, backlinks 0.218. Top-quartile brands for mentions averaged 169 AIO mentions vs 14 for the next quartile. **Not re-read by the fact-check.** [Ahrefs](https://ahrefs.com/blog/ai-overview-brand-correlation/)
- **Aleyda Solis, "AI Search Is a 3rd-Party Citation Problem"** (Aug 2, 2026; 15 brands across SaaS, ecommerce and finance; top-10 cited domains in AI Mode, Gemini and ChatGPT using Semrush Enterprise data). For SaaS, **82.3%** of top cited sources were third-party (owned 17.7%); social/community **45.7%**; news/review **10.4%**; competitor domains 8.1%. Read by the fact-check. [Aleyda Solis](https://www.aleydasolis.com/en/ai-search/ai-search-citations/)
- **Chen, Wang, Chen & Koudas, "Generative Engine Optimization: How to Dominate AI Search"** (arXiv 2509.08919, Sept 10, 2025; University of Toronto; controlled experiments across verticals and languages; academic). AI search shows a "systematic and overwhelming bias towards Earned media" and a "big brand bias". Not re-read by the fact-check. [arXiv](https://arxiv.org/abs/2509.08919v1)
- **Plain English:** the more often other websites talk about a brand, the more AI talks about it. Links alone matter much less.

### 2. YouTube presence and mentions — Moderate–strong (correlation) · Rising

- **Ahrefs** (Dec 2025 study above): **YouTube mentions ~0.737**, the strongest single correlate. [Ahrefs](https://ahrefs.com/blog/ai-brand-visibility-correlations/)
- **Ahrefs via Search Engine Journal** (early 2026): YouTube became the most-cited domain in AI Overviews, up 34% in six months. [SEJ](https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/)
- **Surfer** (46M citations, May 2026; vendor; secondary summary): YouTube ~23.3% of AI Overview citations, ahead of Wikipedia (18.4%). BrightEdge puts YouTube at 29.5% of AIO citation share. [BrightEdge](https://www.brightedge.com/blog/youtubes-growing-impact-google-ai-overviews-what-marketers-need-know)
- **Aleyda Solis** (Aug 2026): YouTube is the largest single source domain for SaaS brands. [Aleyda Solis](https://www.aleydasolis.com/en/ai-search/ai-search-citations/)
- **Meltwater** (July 2026; vendor): citations shifting further toward YouTube, LinkedIn and Reddit. [Meltwater](https://www.meltwater.com/en/blog/ai-search-visibility-report-july-2026)
- **Counterpoint:** Perplexity never cited YouTube in Quotr's 45 test runs ([[AI visibility baseline]]). The payoff is likely in Google's AI features.
- **Plain English:** "strongest correlate, plausible but unproven lever" (fact-check wording). Worth doing because buyers also watch demos.

### 3. Reddit and community (UGC) — Moderate, volatile · Stable overall, falling in ChatGPT

- **Peec AI** (30M sources; vendor): Reddit the #1 cited domain across ChatGPT, AI Mode, Gemini, Perplexity and AIO, then YouTube, LinkedIn, Wikipedia, Forbes. (Some notes credit Semrush; the fact-check says it is Peec AI.) [Peec AI](https://peec.ai/blog/top-domains-cited-by-ai-search-analysis-based-on-30m-sources); [Search Engine Land](https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138)
- **Growth Memo for G2** (Feb 2026; ~35,000 ChatGPT citation URLs, US, Dec 2025; commissioned by G2): user-generated content platforms out-cite review sites at every stage of the buyer journey. [Growth Memo](https://www.growth-memo.com/p/community-signals-are-ais-largest)
- **Ahrefs** (1.4M prompts; vendor): ChatGPT retrieves Reddit heavily but cites it only 1.93% of the time. [Ahrefs](https://ahrefs.com/blog/why-chatgpt-cites-pages/)
- **Volatility:** Semrush (230K+ prompts, 13 weeks, 2025; vendor): ChatGPT cited Reddit in ~60% of responses in early Aug 2025, ~10% by mid-Sept 2025 (not re-checked) ([Semrush](https://www.semrush.com/blog/most-cited-domains-ai/)). Promptwatch: 3.83% → 0.52% of ChatGPT Search citations in Aug 2026 (confirmed) ([Promptwatch](https://promptwatch.com/blog/chatgpt-stop-citing-reddit)).
- **Quotr tests:** reddit.com (mostly r/estimators) was in 6 of 32 unbranded source lists; no Reddit thread naming Quotr was found ([[Citation sources map]]).
- **Plain English:** communities matter a lot, but any one platform's share can collapse overnight. Take part honestly and spread effort.

### 4. Reviews on software review sites — Moderate · Stable to rising

- **Quotr tests** (Perplexity, Sept 25, 2026): Capterra and G2 each fed **9 of 32** unbranded answers; SourceForge 8, Software Advice 7, GetApp 6 ([[Citation sources map]]).
- **G2, "The Answer Economy"** (surveyed March 2026, published April 2026; 1,076 B2B software buyers; **G2 has a direct interest**). 51% start software research in an AI chatbot more often than Google; 45% say a review-site citation is the most confidence-inspiring signal in an AI answer (50% of daily power users). Confirmed. [G2](https://company.g2.com/news/g2-research-the-answer-economy)
- **Counter-evidence:** Aleyda Solis puts news/review at only 10.4% of SaaS top sources; Growth Memo found UGC out-cites review sites ([[verification_geo_evidence|verification H10]]).
- **Presenc AI** (vendor): top-20 G2/Capterra brands cited 3.1x more for "best [category]" queries. Method unverified; **drop or label as vendor** (H12). [Presenc AI](https://presenc.ai/research/does-g2-capterra-reviews-improve-ai-visibility-2026)
- **Market change:** in January 2026, G2 agreed to buy Capterra, GetApp and Software Advice from Gartner, so one review program can feed all four ([PR Newswire](https://www.prnewswire.com/news-releases/g2-to-acquire-capterra-software-advice-and-getapp-from-gartner-302673901.html)).
- **Plain English:** in Quotr's category, review directories are among the most-read sources, and list writers rank tools by review counts. Quotr's G2 profile reportedly has 0 reviews (a Perplexity report; G2 blocked direct checks), and no Capterra listing was found.

### 5. Third-party "best X" lists — Moderate–strong for category prompts · Stable (falling for self-published)

- **Ahrefs, "Do Self-Promotional 'Best' Lists Boost ChatGPT Visibility?"** (26,283 source URLs; vendor): "best X" listicles were **43.8%** of page types ChatGPT cited; self-promotional lists were still cited. [Ahrefs](https://ahrefs.com/blog/best-lists-research/)
- **ZeroClick Labs** (vendor/agency): listicles take 61% of citations in B2B technology services. [ZeroClick Labs](https://zeroclicklabs.ai/ai-seo-study-content-types-ai-search/)
- **HubSpot, State of AEO 2026** (June 3, 2026; vendor; method not published): product/landing pages 68.5%, blog posts 66.75%, listicles 66% average citation rate across AIO, Gemini, ChatGPT and Perplexity. (Some notes credit AirOps; the fact-check says HubSpot.) [HubSpot](https://blog.hubspot.com/marketing/content-format-types-that-earn-citations)
- **Quotr tests:** the same few "best of" lists recur (Construction Coverage 7 of 32, ConstructConnect's 2026 guide 7, The Digital Project Manager 6; ConstructConnect is itself a vendor, and two of the nine tools in its guide are its own). Quotr was not found on any of them (checked by site-restricted search; the pages could not be opened) ([[Citation sources map]]).
- **Self-published lists are the risk:** see [[Myths and risks]] (Lily Ray: 29–49% visibility losses; 69% omission).
- **Plain English:** being **on** other people's lists is one of the most direct routes into "best X" answers. Publishing your own self-ranked lists is not.

### 6. Backlinks and domain authority — Weak–moderate · Falling (relative)

- **Ahrefs** (2025 AIO study): backlinks **0.218** vs web mentions 0.664 (not re-read). **Ahrefs** (Dec 2025): Domain Rating **0.266–0.326** (confirmed).
- **Concentration:** Indig, "The science of how AI picks its sources" (21K+ citations): top 10 domains captured 46% of citations in a topic, top 30 captured 67% ([Growth Memo](https://www.growth-memo.com/p/the-science-of-how-ai-picks-its-sources); not re-checked).
- **Big-brand bias:** Ahrefs says Google's AI surfaces appear more biased toward big brands than ChatGPT and Perplexity ([Ahrefs](https://ahrefs.com/blog/branded-web-mentions-visibility-ai-search/)).
- **Plain English:** authority still helps (partly because it helps rankings), but a brand that is talked about beats a brand that is only linked to.

### 7. Classic search visibility (being indexed and ranking) — Strong · Stable base, top-10 overlap falling

- **Google** (docs and May 15, 2026 guide): a page only needs to be indexed and snippet-eligible; no separate AI strategy. [Google AI features](https://developers.google.com/search/docs/appearance/ai-features); [Google guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- **C-SEO Bench** (Puerto et al., NeurIPS 2025 Datasets & Benchmarks; peer-reviewed): "traditional SEO strategies … are significantly more effective" than content-level GEO tricks. [arXiv](https://arxiv.org/abs/2506.11097); [GitHub](https://github.com/parameterlab/c-seo-bench)
- **Ahrefs** (2026; 863K keywords / 4M AIO URLs; vendor): **38%** of AI Overview citations rank top 10 for the same query, down from **76%** (July 2025); part of the drop is better detection in Ahrefs' tooling. BrightEdge (Feb 2026; vendor): ~17% top-10 overlap; a broader "54% from organic rankings" measure counts any ranking. [Ahrefs](https://ahrefs.com/blog/ai-overview-citations-top-10/); [BrightEdge](https://www.brightedge.com/resources/weekly-ai-search-insights/rank-overlap-after-16-months-of-aio)
- **Ahrefs** (15,000 prompts): only 12% of links cited by ChatGPT, Gemini and Copilot were in Google's top 10. **Digital Authority Partners:** 60% of AI-cited URLs were outside the top 20 on Google or Bing. [Ahrefs](https://ahrefs.com/blog/ai-search-overlap/); [DAP](https://www.digitalauthority.me/resources/ai-visibility-study/)
- **Knock-on effect:** visibility lost in Google can carry into engines that lean on Google-like retrieval ([Search Engine Land](https://searchengineland.com/google-cracking-down-self-promotional-best-of-listicles-468227)).
- **Plain English:** SEO is still the foundation. A top-10 ranking helps but does not guarantee a citation, and Bing and Brave rankings matter for other engines.

### 8. Branded search volume — Moderate (correlation) · Stable

- Ahrefs: 0.392 with AIO visibility (2025, not re-read); 0.352 for ChatGPT (Dec 2025).
- **Plain English:** people searching for "Quotr" is both a sign and a result of being known. It is also a key top-of-funnel KPI ([[Traffic and funnel impact]]).

### 9. Freshness — Moderate, engine-dependent · Stable (rising in ChatGPT)

- **Ahrefs, "Do AI assistants prefer to cite fresh content?"** (July 28, 2025; 16.975M cited URLs; vendor; read by the fact-check). AI-cited URLs averaged 1,064 days old vs ~1,416–1,432 days for organic results (Ahrefs' page gives both numbers); **ChatGPT** most recency-biased (citations 458 days newer than organic); **Google AI Overviews** least; cited pages still average **2.9 years**. [Ahrefs](https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/)
- Microsoft recommends "fresh content consistent with authoritative sources" and its grounding index checks whether information is "fresh enough" ([Microsoft](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers)).
- **Drop these claims:** "half of AI citations are from content updated in the last 13 weeks" and "Perplexity +142% for content updated within 30 days" (source dataset not identified; H5).
- **Plain English:** update when facts change. Date bumps without real changes can backfire ([[Myths and risks]]).

### 10. Structure (answer-first, headings, tables, self-contained sections) — Moderate as practice · Stable

- **Indig, "The Science Of How AI Pays Attention"** (Growth Memo, Feb 2026; 1.2M ChatGPT answers analysed, 18,012 verified citations): 44.2% of citations from the first 30% of a page; 31.1% from the middle. Describes where citations fall; not an experiment (H9). [Growth Memo](https://www.growth-memo.com/p/the-science-of-how-ai-pays-attention); [Search Engine Land](https://searchengineland.com/chatgpt-citations-content-study-469483)
- **Ahrefs** (1.4M ChatGPT prompts; vendor): titles similar to fan-out sub-queries and descriptive URL slugs (89.78% vs 81.11% cited when retrieved). [Ahrefs](https://ahrefs.com/blog/why-chatgpt-cites-pages/)
- **Microsoft** (Oct 2025): headings that mirror questions, short single-idea sections. **Google** (May 2026): no need to chunk.
- **Drop:** "every page ChatGPT cited used list structure" (Averi, no method; H3) and "technical docs get 3x more citations" (agency claim; H4).
- **Plain English:** clear, scannable pages are good for buyers and machines. Don't promise a citation lift from formatting alone.

### 11. Original data, specific numbers and dates — Moderate · Rising

- **Google's May 2026 guide:** the most important factor is "valuable, unique, non-commodity content" (confirmed).
- **Growth Memo, "Why most original data never gets cited"** (301 pages, 316 prompts, 7 verticals, 1,075 citations): only 8 primary-research pages, but **3.3x** the citations per page (11.3 vs 3.4); the format AI rewards is the benchmark that answers "which is best". [Growth Memo](https://www.growth-memo.com/p/why-most-original-data-never-gets)
- **Growth Memo, "Why proprietary data is your most defensible AI citation asset"** (June 29, 2026): DATE and NUMBER entities best predict ChatGPT citations; proprietary data is "necessary but not sufficient". [Growth Memo](https://www.growth-memo.com/p/why-proprietary-data-is-your-most)
- **Quotr tests:** small rivals Meltplan and Exayard get cited next to RSMeans for cost-per-sq-ft pages; Quotr's number-rich AI-accuracy post was Perplexity's first source for "how accurate is AI takeoff" (one session; the fact-check could not repeat this prompt) ([[AI visibility baseline]]; [[Quotr GEO AEO strategy audit|report]]).
- **Plain English:** publish facts only Quotr can know, with the method and date.

### 12. Adding statistics, quotations and cited sources as a tactic — Weak · Falling

- **Aggarwal et al., "GEO: Generative Engine Optimization"** (KDD 2024; arXiv 2311.09735; GEO-bench lab benchmark): adding citations, quotations and statistics raised visibility by **up to ~40%**. The upper bound, not an average. A ~22% figure on live Perplexity circulates but is **unverified**. [arXiv](https://arxiv.org/abs/2311.09735); [GitHub README](https://raw.githubusercontent.com/GEO-optim/GEO/main/README.md)
- **C-SEO Bench** (NeurIPS 2025): "most current C-SEO methods are largely ineffective, contrary to reported results in the literature"; gains shrink as more actors adopt them ("congested and zero-sum"). [arXiv](https://arxiv.org/abs/2506.11097)
- **Plain English:** real data and sources make pages more useful and citable. Sprinkling in stats and quotes to game AI does not reliably work (H2).

### 13. Schema / structured data — Weak for AI citation · Stable (hygiene)

- **Google** (May 2026): structured data is not required and there is "no special schema.org markup" for AI features; still useful for rich results.
- **Microsoft** (Oct 2025): recommends FAQ, HowTo, Product and Review schema for Copilot.
- **Fischman, SSRN** (cross-platform study; author runs a GEO agency): pooled **negative** association between schema and AI citation (OR = 0.546, p < .001), attributed to a confound; conclusion: schema is "an amplifier, not a driver". [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6284518)
- **Plain English:** make schema correct and consistent; don't expect it to win citations on its own. Kit: [[Schema markup kit]].

### 14. Author expertise / E-E-A-T — Weak (no direct evidence) · Unknown

- The research found **no robust quantitative study** showing that author bylines or E-E-A-T markup directly affect AI citation ([[geo_ai_citation_signals_2026|signals notes §2 gaps]]).
- Indirect: Perplexity labelled Quotr's unsourced claims "vendor assertions", and Growth Memo finds cited pages are dense with specific entities such as a named methodology ([[Quotr GEO AEO strategy audit|report]]).
- **Plain English:** named human authors with real credentials are basic trust for buyers. Treat them as hygiene, not a proven AI lever.

### 15. Entity consistency — Moderate (inference supported by tests) · Rising

- **Quotr tests:** when Quotr's pages disagreed, Perplexity hedged: "Quotr claims access to 50+ to 220+ factories, depending on the page"; it also mixed up funding figures and borrowed the unrelated "Quotr Pro" app's ratings ([[Quotr GEO AEO strategy audit|report]]).
- Microsoft's grounding index checks whether facts are clearly sourced and consistent with authoritative sources.
- A 2026 preprint reportedly found higher hallucination rates for entities without Wikipedia pages (15 LLMs, 7,919 entities); the exact paper is **unverified** ([[geo_content_playbook_b2b|playbook §3]]).
- **Plain English:** when the facts match everywhere, AI can state them confidently and tell Quotr apart from namesakes.

### 16. Wikipedia and Wikidata — Moderate (Wikipedia) / Weak (Wikidata) · Falling / volatile in ChatGPT

- Profound (Aug 2024–Jun 2025; vendor): Wikipedia = 47.9% of ChatGPT's top-10 source share. **Outdated** (O4); use as history.
- Semrush (2025): ChatGPT's Wikipedia share fell from ~55% to under 20% of responses (not re-checked). Muck Rack (May 2026) still finds Wikipedia the top ChatGPT domain.
- Wikidata's benefit for entity recognition is PR-agency opinion (H16).
- **Plain English:** Wikipedia needs independent press first. A Wikidata entry is cheap hygiene, not a lever.

### 17. LinkedIn (founder-led content) — Moderate · Rising

- **Semrush LinkedIn AI visibility study** (325,000 prompts, Jan–Feb 2026; 89K LinkedIn URLs; vendor; not re-checked): LinkedIn appears in 11% of AI responses, #2 domain overall and #1 for professional topics; LinkedIn **articles** are 50–66% of cited LinkedIn content; the median cited post has only 15–25 reactions. [Semrush](https://www.semrush.com/blog/linkedin-ai-visibility-study/)
- **Plain English:** practical founder articles can be cited even with low engagement.

### 18. Earned media and press — Moderate · Stable

- **Muck Rack, "What Is AI Reading?"** (May 7, 2026; 25M+ links; ChatGPT, Claude, Gemini; 17 industries; PR vendor; read by the fact-check): "earned" sources 84% of citations (82–89% since July 2025), journalism ~27%, paid 0.3%. "Earned" is defined broadly, so this does **not** mean 84% of citations are press coverage (H11). [Muck Rack](https://muckrack.com/blog/what-is-ai-reading-may-2026)
- For SaaS, news/review sources were only 10.4% of top sources (Aleyda Solis).
- **Quotr tests:** for a tariff question, Perplexity cited only government reports, trade groups, news media and large industry firms (for example Congress's Joint Economic Committee and NAHB); no software vendor was cited ([[Quotr GEO AEO strategy audit|report]]).
- **Plain English:** press is the best route to independent validation of facts, especially with original data as the hook.

### 19. Content length — Weak (both work) · Stable

- Indig (21K+ citations): pages over 20,000 characters averaged 10.18 citations vs 2.39 for pages under 500 characters. Indig also found focused pages win in ChatGPT. Ahrefs: "Short vs. Long Content in AI Overviews: The Data Says Both Work". [Growth Memo](https://www.growth-memo.com/p/the-science-of-how-ai-picks-its-sources); [Growth Memo](https://www.growth-memo.com/p/shorter-focused-content-wins-in-chatgpt); [Ahrefs](https://ahrefs.com/blog/short-vs-long-content-in-ai-overviews/)
- **Resolution (fact-check X16):** long pages hold more passages, so they collect more citations in total; for any single question, focused pages win. Length is not a target.

### 20. Content volume (number of pages) — Myth · Falling

- Ahrefs (Dec 2025; 75K brands): page count ~0.194, "almost no relationship between the number of site pages and AI visibility". [The Next Web](https://thenextweb.com/news/ahrefs-youtube-mentions-ai-visibility-brand-search)
- Google: many pages made mainly to manipulate rankings or AI answers can break the scaled content abuse policy.
- **Quotr:** 96 blog posts in about six months; AI engines read them but rarely name Quotr ([[Quotr GEO AEO strategy audit|report]]).

### 21. Multimedia beyond YouTube — Weak (no data) · Unknown

- No solid quantitative data was found for images, podcasts or webinars ([[geo_ai_citation_signals_2026|signals notes §2 gaps]]; [[geo_content_playbook_b2b|playbook §3 gaps]]).
- Video in Google AI Mode: 23.0% of SaaS cited sources vs 1.0% in ChatGPT (Aleyda Solis SaaS article; not re-read).
- **Plain English:** video is worth it mainly through YouTube. Transcripts and text summaries make video content readable by engines that do not watch video.

### 22. Crawler access and rendering — Strong (prerequisite) · Stable

- OpenAI: don't block OAI-SearchBot if you want to appear. Anthropic: blocking Claude-SearchBot "may reduce visibility". Google: must be indexed. Many AI crawlers do not run JavaScript, so server-rendered text is safer ([[Website audit]]).
- Full crawler table: [[How AI engines choose sources]].

### 23. llms.txt — Myth for citations · Falling

- SE Ranking (300K domains; vendor; not re-checked): no correlation with AI citations. Google: AI text files not needed. Details in [[Myths and risks]].

---

## 3. What matters more in 2026 than in 2024

In plain words, eleven shifts:

1. **Being talked about beats being linked to.** In 2024 the SEO playbook centred on backlinks. The 2025–26 data shows brand mentions, YouTube and community discussion track AI visibility far more closely than links (Ahrefs 75K brands).
2. **Other people's sites carry most of the weight.** For SaaS, about 82% of top cited sources are third-party (Aleyda Solis, Aug 2026). Your own site is the "corroboration base", not the whole strategy.
3. **YouTube and communities rose; trade press and review sites matter, but less than many assumed for SaaS.** YouTube became the most-cited domain in AI Overviews. Social/community sources are 45.7% of SaaS top sources (74.6% in AI Mode).
4. **Being named now pays directly.** Since May 7, 2026, ChatGPT links brand names to homepages, and B2B software gained the most (Profound, vendor). A mention in the answer text is now a doorway, not just a footnote.
5. **Original, specific data wins over "GEO tricks".** Google's May 2026 guide asks for "non-commodity" content; C-SEO Bench (2025) found most tricks ineffective; Growth Memo found primary data earns 3.3x the citations per page.
6. **Search is multi-engine.** ChatGPT's share of AI-assistant traffic fell from ~76% to ~53% (June 2025 to May 2026; Similarweb, not re-checked) as Gemini and Claude grew. Engines rarely agree on sources.
7. **Search became a conversation.** AI Mode passed 1 billion monthly users and AI Overviews 2.5 billion (May 2026), and the two became one flow. Fan-out sub-queries decide which pages get read.
8. **Ranking in Google's top 10 is still the base, but not the guarantee.** Only 38% of AI Overview citations came from the top 10 in 2026, vs 76% in 2025 (Ahrefs, with a tooling caveat).
9. **Penalties for shortcuts arrived.** Self-promotional "best X" lists, scaled "alternatives" pages and "2026" year bumps were hit in early 2026 (Lily Ray observations). Google's guide warns against fan-out page spam.
10. **Volatility is the norm.** Reddit's ChatGPT share collapsed twice (2025 and 2026); only about a third of cited pages were still cited 28 days later (DAP).
11. **First-party measurement exists.** Bing AI Performance (Feb 2026) and Search Console's Generative AI reports (worldwide Aug 31, 2026) now show AI citations and impressions.

**What matters less than people think:** llms.txt, schema as an AI lever, page volume, keyword density, stat/quote stuffing, date bumps, and any single platform.

---

## 4. What this means for Quotr

Quotr's situation (from the [[Quotr GEO AEO strategy audit|report]] and [[Presence scorecard]]): strong on-site formatting and crawlability, 96 posts that Perplexity already reads, but **named in 1 of 32 unbranded Perplexity questions (about 3%)** against 10 each for STACK, PlanSwift and Buildxact, almost no third-party proof, and conflicting facts on its own pages. Only Perplexity was tested; ChatGPT, Google AI Overviews / AI Mode, Gemini, Claude and Copilot still need a baseline.

- **Shift effort from pages to proof.** The weakest signals (page volume, llms.txt, schema) are where Quotr has invested most; the strongest (mentions, reviews, lists, YouTube, communities) are where it scores lowest (entity and off-site trust 1.4 of 5).
- **Start a G2 review drive.** Review sites fed 9 of 32 answers in Quotr's category, and one program now feeds G2, Capterra, GetApp and Software Advice. Aim for 10–30 honest reviews under G2's rules.
- **Get on the lists engines already read:** Construction Coverage, The Digital Project Manager, ConstructionPlacements, ContraVault, the F6S "AI-Assisted Takeoff" category ([[Citation sources map]]).
- **Make YouTube a Google-side bet:** one trade per video on real residential plans, with "Quotr" said aloud and in titles.
- **Show up in communities honestly:** founders answering in r/estimators and Facebook estimator groups, with clear disclosure; founder LinkedIn articles.
- **Publish original data:** a factory-direct vs US price index with tariffs, residential/multifamily cost per sq ft by trade, an LA fire-rebuild cost guide. These are topics where no software vendor is cited today ([[White space]]).
- **Fix entity consistency first:** one fact sheet for price, HQ, founders, funding, factory count, turnaround and handles ([[Entity fact sheet]]).
- **Keep the SEO base healthy:** Google and Bing indexing, blog sitemap in robots.txt, real lastmod dates, no stale prices, staging hosts out of the index.
- **Keep the good formatting, stop the tricks:** keep answer-first blocks and tables; remove the llms.txt "should be cited" line and bot-directed wording; stop growing self-ranked lists ([[Myths and risks]]).
- **Measure across engines and over time**, not from one snapshot ([[KPIs and dashboard]]).

---

## Related pages

- [[How AI engines choose sources]] — how each engine retrieves and cites
- [[Myths and risks]] — tactics that waste effort or carry risk
- [[Traffic and funnel impact]] — clicks, referrals and top-of-funnel reach
- [[GEO glossary]] — plain-English definitions
- [[Presence scorecard]] — how Quotr scores on these signals today
- [[Off-site presence]] — Quotr's reviews, lists, press and communities
- [[Citation sources map]] — the sources engines cite in Quotr's category
- [[Content priorities]] — which content to build first
- [[Off-site earned media plan]] — the off-site plan
