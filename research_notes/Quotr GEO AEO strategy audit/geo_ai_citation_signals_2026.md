# What signals AI answer engines use to surface, mention and cite content: evidence as of September 2026

*How these notes were gathered (read this first):* The Slashy `scrape_url` tool hit a rate limit on its first call ("Retry after 2447 seconds"). WebFetch returned EGRESS_BLOCKED for developers.google.com. So **no full page was read directly in this session.** Every finding below comes from search-engine result summaries (WebSearch) or from Perplexity Sonar answers (Slashy `web_search`) that cite the URLs given. The numbers match across several independent summaries, but the report writer should treat exact figures as "reported by X", not as quotes checked against the full text. "Vendor" marks studies from companies that sell AI-visibility, SEO or review products, since they have a commercial interest in the result. Today's date is 2026-09-25.

---

## 1. Mechanics: how each engine retrieves, grounds and cites, and what the platforms themselves say

### Takeaway
Every major engine grounds its answers in a conventional search index: Google in its own index, Copilot in Bing, ChatGPT in its own crawl plus "third-party search providers", Claude in Brave Search, and Perplexity in its own index plus partners. They then break the user's prompt into many sub-queries (query fan-out) and pull passages from the results. Google's official position (May 2026) is that there is "no separate strategy": pages need only be indexed and snippet-eligible, with no special files, markup or chunking. Microsoft is more prescriptive, recommending headings, short single-idea sections and schema. ChatGPT searches the web on only about a third of prompts. The rest are answered from training-data (parametric) knowledge, so brand presence in that knowledge still matters.

### Cited Findings

**Google (AI Overviews / AI Mode / Gemini), first-party**
- Google published "Google's Guide to Optimizing for Generative AI Features on Google Search" on Search Central on **May 15, 2026**. — [Google Search Central](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide); coverage: [Search Engine Journal: "Google's New AI Search Guide Calls AEO And GEO 'Still SEO'"](https://www.searchenginejournal.com/googles-new-ai-search-guide-calls-aeo-and-geo-still-seo/575026/), [Semrush](https://www.semrush.com/blog/google-publishes-generative-ai-search-guide/)
- Per Google's docs, there are **no additional requirements** to appear in AI Overviews or AI Mode. To be eligible as a supporting link, a page need only be **indexed and eligible to show in Search with a snippet**. — [Google: AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features)
- AI Overviews and AI Mode "may use a **query fan-out** technique — issuing multiple related searches across subtopics and data sources — to develop a response". Google's example: "how to fix a lawn full of weeds" fans out to "best herbicides for lawns", "remove weeds without chemicals" and "how to prevent weeds in lawn". — [Google: AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features) (as summarised in search results)
- The May 2026 guide says site owners **do not need machine-readable files, AI text files, special markup or Markdown** to appear in generative AI search, and that Google may crawl such files "without treating them in any special way". — [Google AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), via [Averi summary](https://www.averi.ai/blog/google-s-ai-guide-just-killed-4-geo-myths-(and-validated-3)) and [TechWyse](https://www.techwyse.com/news/ai-search/google-ai-search-optimization-guide-llms-txt-lighthouse-audit)
- The guide says there is **no need to "chunk" content** into tiny pieces: Google's systems can handle multiple topics on a page and show the relevant part. — same sources as above
- The guide says **structured data is not required and there is "no special schema.org markup"** for generative AI features. Google still recommends it for rich-result eligibility. — same sources
- The guide warns that **creating separate content for every fan-out variation**, or targeting fan-out queries mainly to manipulate AI responses, **violates the scaled content abuse spam policy**. — [Google: AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features) (as summarised)
- AI Overviews were upgraded to **Gemini 3 globally in January 2026**, which Ahrefs cites as context for its citation-overlap changes. — [Search Engine Journal](https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/)
- On **May 27, 2026**, Google extended **Preferred Sources** (user-selected favourite sites) into AI Overviews and AI Mode. Links from preferred sites get a badge, and by Google's own figures this **doubles click-through**. Critics say it favours established publishers with loyal audiences. — [PPC Land](https://ppc.land/google-extends-preferred-sources-into-ai-mode-as-new-sites-lose-ground/); [SE Roundtable](https://www.seroundtable.com/google-ai-preferred-sources-41394.html); [Google blog: new controls for website owners](https://blog.google/products-and-platforms/products/search/new-controls-website-owners/)

**Microsoft (Bing / Copilot), first-party**
- Microsoft's October 2025 post "Optimizing Your Content for Inclusion in AI Search Answers" says Copilot **parses content into smaller structured pieces** and assesses each for authority and relevance. Answers are then assembled from multiple sources. Recommendations: descriptive H1–H3 headings that mirror questions, short single-idea sections, **schema markup (FAQ, HowTo, Product, Review)**, direct factual language, alt text and clean HTML, and fresh content consistent with authoritative sources. — [Microsoft Advertising blog (Oct 2025)](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers); [Search Engine World](https://www.searchengineworld.com/microsoft-shares-exact-signals-ai-uses-to-choose-content-for-search-answers)
- On **Feb 11, 2026**, Bing Webmaster Tools launched an **AI Performance report** (public preview). It shows how often a site's URLs are cited in Copilot, Bing AI summaries and some partner integrations, plus **"grounding queries"**: the internal search phrases Copilot generates to retrieve content. It is the first first-party citation-reporting tool from a major engine. — [Bing Webmaster blog](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview); [Search Engine Land](https://searchengineland.com/bing-webmaster-tools-ai-performance-report-468751); [Bing help page](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c)

**OpenAI (ChatGPT search), first-party**
- OpenAI's Publishers & Developers FAQ describes three crawlers:
  - **OAI-SearchBot**: surfaces pages in ChatGPT search results, snippets and citations. Publishers should not block it if they want to be included.
  - **GPTBot**: training-data collection.
  - **ChatGPT-User**: fetches pages on demand during a user's conversation.
  
  The FAQ says **"any public website can appear in ChatGPT search"**. — [OpenAI Help: Publishers and Developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)
- The same FAQ says ChatGPT may get URLs from **third-party search providers**. If a disallowed page is relevant, ChatGPT may still show its link and title unless it is `noindex`ed. — [OpenAI Help FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) (via Perplexity summary). *Note: the summary did not show the FAQ naming Bing, and I could not verify reports that OpenAI uses scraped Google results.*
- ChatGPT adds **`utm_source=chatgpt.com`** to referral links, so the traffic shows up in analytics. — [OpenAI Help FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq); [OpenAI Help: ChatGPT search](https://help.openai.com/en/articles/9237897-chatgpt-search)
- OpenAI has **not published a weighting of source-selection factors**. Frameworks circulating online (e.g., "domain authority ~40%") are reverse-engineered and unconfirmed. — [ZipTie.dev](https://ziptie.dev/blog/how-does-chatgpt-choose-its-sources/) (flagged as speculative in its own text)

**Anthropic (Claude), first-party plus secondary**
- Anthropic documents three crawlers:
  - **ClaudeBot**: training.
  - **Claude-SearchBot**: improves search result quality.
  - **Claude-User**: fetches pages on demand for users.
  
  All respect robots.txt, and Anthropic supports Crawl-delay. — [SE Roundtable on Anthropic crawler docs](https://www.seroundtable.com/anthropic-updates-its-crawler-docs-40978.html)
- Claude's web search uses **Brave Search**. Brave is listed as a "Web Search" vendor on Anthropic's subprocessor page, and one independent test found **86.7% overlap** between Claude's cited results and Brave's top organic results. — [Profound: Claude web search explained](https://www.tryprofound.com/blog/what-is-claude-web-search-explained); [Ryan Doser](https://ryandoser.com/what-search-engine-does-claude-use/) (independent test, small sample; vendor/blogger)

**Perplexity**
- Perplexity uses **its own index built by PerplexityBot plus search partners**, then selects citations by relevance, authority, recency and how directly a passage supports a claim. Perplexity says PerplexityBot is not used for model training. — [LLM Pulse](https://llmpulse.ai/blog/how-perplexity-works/); [SearchScore](https://searchscore.io/guides/how-perplexity-cites-sources/). *Secondary summaries only; I did not verify Perplexity first-party docs this session.*

**Live retrieval vs. parametric (training-data) knowledge**
- ChatGPT runs a web search on about **31% of prompts** (Nectiv study, 2025). — [Search Engine Land](https://searchengineland.com/chatgpt-search-prompts-data-463407)
- A second clickstream analysis found ChatGPT searched on **34.5% of queries in Feb 2026, down from 46% in late 2024**. Search-enabled sessions fell every month from Nov 2025 to Feb 2026. Average prompt length for search-enabled queries rose from **4.7 to 8.7 words**; for non-search prompts it fell from 24.9 to 13.5 words. — [OtterlyAI (vendor)](https://otterly.ai/blog/how-often-does-chatgpt-trigger-a-web-search/); related [Semrush clickstream analysis](https://www.semrush.com/blog/chatgpt-search-insights/)
- ChatGPT also fans out: **89.6% of search-triggering prompts produced 2+ follow-up searches** beyond the user's wording. — [Search Engine Land (Nectiv data)](https://searchengineland.com/chatgpt-search-prompts-data-463407) (as summarised)

**Where the answer comes from on a page (passage-level retrieval)**
- **44.2% of ChatGPT citations come from the first 30% of a page.** Source: Kevin Indig, "The science of how AI pays attention", 1.2M search results / 18,012 verified citations. — [Growth Memo](https://www.growth-memo.com/p/the-science-of-how-ai-pays-attention)

### Inferences
- The index behind each engine differs: Google, Bing (Copilot and part of ChatGPT), Brave (Claude) and Perplexity's own. Being indexed and ranking well in **Bing and Brave, not just Google**, is a precondition for non-Google engines. Brave is especially relevant for Claude, whose share of B2B referrals is growing (see section 5).
- Because only about a third of ChatGPT prompts trigger search, a brand's presence in training data drives the rest. That knowledge is built from broad web mentions, so off-site presence matters beyond anything on-page.
- Google and Microsoft disagree on schema: Google says it has no special AI role, Microsoft recommends it. Low-cost schema remains sensible "hygiene", but it is not a proven lever for AI citations.

### Gaps
- Could not read Google's May 2026 guide or OpenAI's FAQ in full (tool limits), so direct quotations are unavailable.
- No first-party Perplexity or Gemini-app documentation on source selection was verified.
- Whether ChatGPT currently uses Bing, Google-derived results, its own index, or a mix is not confirmed by OpenAI beyond "third-party search providers".
- Google Search Console's handling of AI Mode/AIO data (whether it is separated from regular Web data) was not verified this session.

---

## 2. Evidence on factors that correlate with being cited or mentioned

### Takeaway
The strongest quantitative signals are **off-site**: brand web mentions, and especially **YouTube mentions**, correlate with AI visibility far more than backlinks (Ahrefs, 75K brands). Academic work finds AI search is strongly biased toward **earned third-party media** over brand-owned content and toward big brands. On-page, the evidence favours **front-loaded answers**, content that is **fresh and actually updated**, **"best X" listicles and comparison pages**, and adding **statistics, quotations and cited sources** (GEO paper). Citation patterns differ sharply between engines and shift quickly, and **being cited is not the same as being mentioned or recommended**.

### Cited Findings

**Brand mentions vs. backlinks / authority (Ahrefs; vendor, but large-sample)**
- Ahrefs, "An Analysis of AI Overview Brand Visibility Factors" (**75,000 brands**, 2025) looked at what correlates with brand visibility in AI Overviews:

  | Signal | Correlation |
  |---|---|
  | Branded web mentions | **0.664** |
  | Branded anchors | 0.527 |
  | Branded search volume | 0.392 |
  | Backlinks | **0.218** |

  Brands in the top quartile for web mentions averaged **169 AIO mentions**, versus **14** for the next quartile and **0–3** for the bottom half. — [Ahrefs](https://ahrefs.com/blog/ai-overview-brand-correlation/)
- A follow-up (Dec 2025; press release **May 26, 2026**) extended the analysis to ChatGPT, AI Mode and AIO across 75K brands. **YouTube mentions were the strongest single correlate (~0.737).** The study also found **"almost no relationship between the number of site pages and AI visibility"**, which undercuts programmatic, volume-driven content. — [BusinessWire press release](https://www.businesswire.com/news/home/20260526119691/en/Across-75000-Brands-YouTube-Mentions-Are-the-Strongest-Signal-of-AI-Visibility-New-Ahrefs-Report-Reveals); [The Next Web](https://thenextweb.com/news/ahrefs-youtube-mentions-ai-visibility-brand-search); [Ahrefs: brand visibility correlations](https://ahrefs.com/blog/ai-brand-visibility-correlations/)
- Ahrefs also reports **Google (AIO/AI Mode) appears more biased toward big brands than ChatGPT and Perplexity.** — [Ahrefs](https://ahrefs.com/blog/branded-web-mentions-visibility-ai-search/)
- **Caution: citations are not the same as mentions.** Kevin Indig analysed a Semrush dataset (1,094 US categories, 600K+ ChatGPT citations, Jan–Jun 2026):
  - the correlation between a domain's citations and brand mentions was **slightly negative (-0.229)**;
  - the most-cited domain was also the most-mentioned brand in only **20.8%** of cases;
  - the most-mentioned brand still picked up at least one citation in **69.9%** of cases.
  
  — [Kevin Indig on Substack](https://substack.com/@kevinindig/note/c-298265127)

**Earned media bias / big-brand bias (academic)**
- Chen, Wang, Chen & Koudas, "Generative Engine Optimization: How to Dominate AI Search" (arXiv:2509.08919, **Sept 10, 2025**, University of Toronto). Controlled experiments across verticals, languages and paraphrases found AI search shows a **"systematic and overwhelming bias towards Earned media"** (third-party, authoritative sources) over brand-owned and social content, in contrast to Google's more balanced mix. The authors recommend:
  1. machine-scannable, justifiable content;
  2. building earned media;
  3. engine- and language-specific strategies;
  4. strategies for niche players to overcome **"big brand bias"**.
  
  — [arXiv](https://arxiv.org/abs/2509.08919v1)

**Content-level tactics: the GEO paper**
- Aggarwal et al., "GEO: Generative Engine Optimization" (KDD 2024; arXiv:2311.09735; **dated 2023/2024**). Adding **citations, quotations from relevant sources, and statistics** raised source visibility by **up to ~40%** (Position-Adjusted Word Count) on the GEO-bench benchmark.
  - Secondary summaries report about **22%** gains on the live Perplexity test.
  - The 40% figure is an **upper bound** for specific conditions, not an average.
  - "Cite sources" helped lower-ranked pages most.
  
  — [arXiv](https://arxiv.org/abs/2311.09735); [ar5iv full text](https://ar5iv.labs.arxiv.org/html/2311.09735); [geo.wiki summary](https://geo.wiki/papers/aggarwal-geo-benchmark-2024); [critique summary, blckalpaca](https://blckalpaca.at/en/knowledge-base/seo-geo/geo-generative-engine-optimization/the-princeton-geo-study-methodology-results-and-critique)
- No independent peer-reviewed **replication** of the GEO paper's lift figures was found in this session (Perplexity Sonar also found none).

**Freshness / recency**
- Ahrefs (**~17M citations**, 2025): AI-cited URLs averaged **1,064 days old vs 1,432 days** for Google organic results, i.e. **25.7% "fresher"**. Cited pages were also more recently *updated*.
  - **ChatGPT showed the strongest recency preference.**
  - **AI Overviews leaned toward older content** than other AI systems.
  
  — [Ahrefs](https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/); [Ahrefs: fresh content](https://ahrefs.com/blog/fresh-content/)
- Ahrefs found **recently updated "best X" lists** were the most prominent page type among ChatGPT sources (see listicles below). — [Ahrefs best-lists study](https://ahrefs.com/blog/best-lists-research/)

**Page types: listicles, "best X", comparison and product pages**
- Ahrefs, "Do Self-Promotional 'Best' Lists Boost ChatGPT Visibility?" (**26,283 source URLs**) found:
  - "best X" listicles made up **43.8% of page types cited by ChatGPT**;
  - self-promotional lists that rank the publisher's own brand #1 were still cited.
  
  — [Ahrefs](https://ahrefs.com/blog/best-lists-research/)
- AirOps (vendor) found that across AIO, Gemini, ChatGPT and Perplexity, only three content types exceeded a 65% average citation rate:
  - product listing / landing pages (**68.5%**);
  - blog posts (**66.75%**);
  - listicles (**66%**).
  
  — [AirOps](https://www.airops.com/blog/page-types-earn-ai-citations); see also [HubSpot research on formats](https://blog.hubspot.com/marketing/content-format-types-that-earn-citations)

**Content length / structure**
- Indig, "The science of how AI picks its sources" (**21K+ citations**):
  - pages over **20,000 characters averaged 10.18 citations vs 2.39** for pages under 500 characters;
  - top 10 domains captured **46%** of citations in a topic, and top 30 captured **67%**.
  
  — [Growth Memo](https://www.growth-memo.com/p/the-science-of-how-ai-picks-its-sources)
- Indig's related "Shorter, focused content wins in ChatGPT" argues that **focused, front-loaded pages with fewer subtopics** beat exhaustive guides in ChatGPT. **This partly conflicts** with the length finding above. — [Growth Memo](https://www.growth-memo.com/p/shorter-focused-content-wins-in-chatgpt)
- Ahrefs: "Short vs. Long Content in AI Overviews: **The Data Says Both Work**." — [Ahrefs](https://ahrefs.com/blog/short-vs-long-content-in-ai-overviews/)

**Relationship to organic rankings**
- Ahrefs found the share of AIO citations that also rank top-10 for the same query fell from **76% (July 2025) to 38% (2026)**. Details:
  - **863K keywords / 4M AIO URLs**;
  - the rest split between positions 11–100 (31.2%) and beyond 100 (31.0%);
  - Ahrefs says part of the drop reflects **better citation detection in its own tooling**, so the two waves are not fully comparable.
  
  — [Ahrefs update](https://ahrefs.com/blog/ai-overview-citations-top-10/); [Ahrefs original](https://ahrefs.com/blog/search-rankings-ai-citations/); [SEJ](https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/)
- BrightEdge (Feb 2026, vendor) found only **~17%** overlap between AIO citations and the organic top 10. — reported in [SEJ](https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/). **This conflicts with Ahrefs' 38%**; differences in method and keyword set are likely.

**Which domains get cited (platform concentration)**
- Profound (vendor; **680M+ citations**, Aug 2024–Jun 2025):
  - **Wikipedia = 47.9%** of ChatGPT's top-10 source share;
  - **Reddit = 46.7%** of Perplexity's top-10 share.
  
  — [Profound](https://www.tryprofound.com/blog/ai-platform-citation-patterns)
- Semrush (vendor; **230K+ prompts over 13 weeks** across ChatGPT, AI Mode and Perplexity, 2025):
  - ChatGPT cited **Reddit in ~60% of responses in early Aug 2025, falling to ~10% by mid-Sept 2025**;
  - Wikipedia fell from ~55% to <20%;
  - AI Mode and Perplexity stayed stable.
  
  A separate Semrush post reports Reddit's ChatGPT citation share falling from **3.8% to 0.5%**. — [Semrush 3-month study](https://www.semrush.com/blog/most-cited-domains-ai/); [Semrush Reddit drop](https://www.semrush.com/blog/reddits-citations-in-chatgpt-fall/)
- Peec AI (vendor; **30M sources**) ranks **Reddit #1** across ChatGPT, AI Mode, Gemini, Perplexity and AIO, followed by **YouTube, LinkedIn, Wikipedia and Forbes**. — [Peec AI](https://peec.ai/blog/top-domains-cited-by-ai-search-analysis-based-on-30m-sources); [Search Engine Land](https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138)
- Ahrefs says **YouTube has become the most-cited domain in AI Overviews**, up 34% over six months (reported early 2026). — [SEJ](https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/)
- Evertune (**200M prompts**, vendor): even the most-cited domain rarely exceeds **5%** of a platform's citations. — cited in [Contently](https://contently.com/2026/04/29/top-sources-llms-cite/)
- **Engines rarely agree on sources.** Indig, "The Consensus Gap" (H1 2026): **91% of AI citations appear in only one engine** (ChatGPT, Perplexity, AIO). — [Growth Memo](https://www.growth-memo.com/p/the-consensus-gap); [H1 2026 halftime report](https://www.growth-memo.com/p/ai-halftime-report-h1-2026)
- Ahrefs: top-mentioned sources are **not shared across AI assistants**. — [Ahrefs](https://ahrefs.com/blog/top-mentioned-sources-are-not-shared-across-ai-assistants/)

**Review-site presence (B2B software)**
- G2, "The Answer Economy: 2026 AI Search Insight Report" (**vendor with direct interest**; survey of **1,076 B2B software buyers, March 2026**):
  - **51%** now start software research in an AI chatbot more often than in Google (up from 29%);
  - **45%** say a review-site citation is the most confidence-inspiring signal in an AI answer;
  - nearly **7 in 10** chose a different vendor than expected because of AI chatbot guidance;
  - ChatGPT is the dominant chatbot for this research (**63%**).
  
  — [G2 report](https://learn.g2.com/g2-2026-ai-search-insight-report); [PR Newswire](https://www.prnewswire.com/news-releases/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots-302742807.html); [G2 press](https://company.g2.com/news/buyer-behavior-2026)
- Presenc AI (vendor): brands in the top 20 of G2/Capterra for their category are cited about **3.1x more often** for "best [category]" queries. A separate analysis says the **evidence on G2/Capterra feeding AI answers conflicts**. — [Presenc AI](https://presenc.ai/research/does-g2-capterra-reviews-improve-ai-visibility-2026); [Strive Labs](https://strivelabs.ai/blog/g2-capterra-ai-answers/)

**AI-generated content / authorship**
- Ahrefs (**1M SERPs with AIOs**):
  - only **25.8%** of top-3 cited links were "pure human", and **71.7%** mixed AI and human writing;
  - the correlation between AI-content share and citation order was **~0**, i.e. no evident penalty or reward.
  
  — [Ahrefs](https://ahrefs.com/blog/ai-overviews-cite-ai-generated-content-more-than-human-writing/)
- A separate Ahrefs study of 600K pages found AI-generated content **does not hurt Google rankings**. — [Ahrefs](https://ahrefs.com/blog/ai-generated-content-does-not-hurt-your-google-rankings/)

**User behaviour inside AI answers**
- Indig's AI Mode user study found **64%** of participants clicked nothing during their task, and **74%** chose the brand ranked **first** in the AI answer. — [Kevin Indig on Substack](https://substack.com/@kevinindig/note/c-298265127) (small-sample usability study; sample size not captured)

### Inferences
- For a small, niche B2B brand like Quotr, the evidence points first to **earning third-party mentions**:
  - YouTube videos (own channel and creators);
  - Reddit and trade-forum discussions;
  - review sites (G2/Capterra);
  - trade press;
  - "best construction takeoff software" listicles on other domains.
  
  Page count on its own site is unlikely to help much. The Ahrefs finding of almost no relationship between page count and visibility argues against mass programmatic pages.
- The strongest on-page levers are:
  1. answer-first intros (content in the first 30% of a page is most-cited);
  2. regularly and genuinely updated "best / vs / alternatives" and pricing pages (freshness plus the listicle format);
  3. original statistics and data (the GEO paper's strongest levers, and a way to earn citations from others).
- Engines rarely agree on sources, and ChatGPT's source mix swung sharply in 2025. Measurement should cover several engines and track trends; any single-engine snapshot will mislead.
- Being mentioned or recommended as the #1 brand in the answer text matters more to users than a footnote citation (the 74% first-brand choice).

### Gaps
- All the large correlation studies are observational and mostly from vendors (Ahrefs, Semrush, Profound, Peec, AirOps, BrightEdge, G2). None establishes causation.
- No study specific to **construction / AEC software** queries was found.
- No robust quantitative study was found showing that **author bylines / E-E-A-T markup** directly affect AI citation. The evidence here is thin.
- Could not verify from the paper itself (tool limits) how "keyword stuffing" performed in the original GEO paper.
- Multimedia beyond YouTube (images, podcasts) had no solid quantitative data.
- Sample size for Indig's AI Mode user study was not captured.

---

## 3. Myths and weak evidence

### Takeaway
The evidence runs against **llms.txt**:
- no correlation with citations across 300K domains;
- Google explicitly says it gives it no special treatment;
- no major engine has committed to using it.

On **schema as a direct citation factor**, Google says no and Microsoft says it helps; independent data is mixed and confounded. **Hidden or AI-only pages** and **fan-out keyword spam** are called out by Google as unnecessary or spam. The GEO paper's 40% figure is often overstated as a universal lift.

### Cited Findings
- **llms.txt, SE Ranking (vendor; 300K domains):**
  - **10.13%** of domains had llms.txt;
  - there was **no correlation** with AI citation frequency, and **removing the llms.txt feature improved** their XGBoost model's accuracy;
  - only **one of the 50 most AI-cited domains** had the file.
  
  — [SE Ranking](https://seranking.com/blog/llms-txt/); [Search Engine Journal](https://www.searchenginejournal.com/llms-txt-shows-no-clear-effect-on-ai-citations-based-on-300k-domains/561542/)
- **llms.txt, Google:**
  - Gary Illyes said in July 2025 that Google doesn't support llms.txt and isn't planning to;
  - John Mueller compared it to the keywords meta tag;
  - the May 2026 guide says AI text files and Markdown versions are not needed.
  
  — [Ariashaw evidence roundup](https://ariashaw.com/does-llms-txt-actually-work) (secondary); [Google AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- **llms.txt, crawler logs:** server-log analyses report that GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot and Google-Extended rarely fetch /llms.txt. Most requests for it come from **SEO audit tools**. As of Q1 2026, no major AI company had publicly committed to using it in production. — [Ariashaw](https://ariashaw.com/does-llms-txt-actually-work); [OtterlyAI llms.txt experiment (vendor)](https://otterly.ai/blog/the-llms-txt-experiment/) (secondary / vendor)
- **Possible counter-signal:** coverage mentions a Chrome/Lighthouse "llms.txt audit" alongside Google's guide. Details were not verified. — [TechWyse](https://www.techwyse.com/news/ai-search/google-ai-search-optimization-guide-llms-txt-lighthouse-audit)
- **Schema as a citation factor:**
  - Google: not required, and no special schema exists. — [Google guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
  - Microsoft: schema recommended. — [Microsoft](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers)
  - An SSRN cross-platform study (Fischman; author runs a GEO agency) found a pooled **negative** association between schema and AI citation (OR = 0.546, p < .001). The author attributes this to a confound, since top-10 organic results carry more schema, and concludes schema is **an amplifier, not a driver**. — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6284518)
- **Chunking / AI-only formatting:** Google says content does not need to be broken into tiny pieces. — [Google guide via Averi](https://www.averi.ai/blog/google-s-ai-guide-just-killed-4-geo-myths-(and-validated-3))
- **Fan-out spam / pages for every variation:** Google classifies this as a scaled content abuse violation. — [Google AI features doc](https://developers.google.com/search/docs/appearance/ai-features)
- **The "GEO +40%" figure:** it is an upper bound on a synthetic benchmark. The live Perplexity test showed about 22%. — [geo.wiki](https://geo.wiki/papers/aggarwal-geo-benchmark-2024); [blckalpaca critique](https://blckalpaca.at/en/knowledge-base/seo-geo/geo-generative-engine-optimization/the-princeton-geo-study-methodology-results-and-critique)
- **Reverse-engineered "ChatGPT ranking weights":** OpenAI has not confirmed any such weighting. — [ZipTie.dev](https://ziptie.dev/blog/how-does-chatgpt-choose-its-sources/)
- **"Mass content wins":** Ahrefs' Dec 2025 study found almost no relationship between site page count and AI visibility. — [The Next Web on Ahrefs](https://thenextweb.com/news/ahrefs-youtube-mentions-ai-visibility-brand-search)
- **Manipulation research:** a 2026 arXiv paper studies exploiting LLM biases to manipulate AI search overviews. This shows such manipulation is possible, which makes crackdowns by the engines more likely. — [arXiv 2605.00012](https://arxiv.org/pdf/2605.00012) (not read in full)

### Inferences
- Quotr's `/disambiguation/` page, written "for search engines and AI systems", is a form of AI-targeted page.
  - Google says no special AI files are needed and treats them like any other content, so the page's value depends on whether it also helps **human** readers.
  - It should read as a genuine brand/FAQ page, not hidden or crawler-only content.
  - Real entity clarity comes from consistent third-party profiles (G2, LinkedIn, Crunchbase, YouTube) using the current name "Quotr.ai" and the old "Quotr.io" alias.
- Treat llms.txt as a zero-to-low-value, low-cost optional item. Don't sell it as a lever.

### Gaps
- No controlled experiment (A/B on otherwise identical pages) on schema or llms.txt from a platform was found.
- Hidden-text effects are not studied quantitatively beyond Google's spam policies. The main documented risk is prompt injection / manipulation research.

---

## 4. What changed in 2025–2026 and what is trending up

### Takeaway
The main shifts from 2025 to 2026:
- AI surfaces became mass-market (Gemini 3 in AIO, AI Mode rolled out globally).
- **ChatGPT started linking prominently to brand homepages (May 7, 2026)**, roughly doubling to tripling its referrals.
- **Ads arrived in ChatGPT** (Jan 2026 test, then self-serve, CPA bidding and "click-to-chat" agent ads).
- Agentic browsers grew quickly.
- Google added personalisation (Preferred Sources, Personal Intelligence).
- First-party citation measurement arrived (Bing AI Performance).
- **YouTube** became the most-cited domain in AIO and the strongest brand-visibility correlate.
- ChatGPT's traffic share is fragmenting toward Gemini and Claude.

### Cited Findings
- **ChatGPT "Branded Link Update" (May 7, 2026):**
  - Profound (vendor): OpenAI referral traffic to monitored brand sites **roughly doubled overnight (~60–65%)**, with brand homepage URLs embedded inline about **5x more often**; the homepage share of OpenAI referrals went from about **3.5% to ~24%**. — [Profound](https://www.tryprofound.com/blog/chatgpt-referrals-branded-links)
  - Similarweb: ChatGPT referral traffic **"near triples"**; homepage referrals rose from about 26–32% to about 60% of ChatGPT referrals. — [Similarweb](https://www.similarweb.com/blog/insights/ai-news/chatgpt-referral-traffic-triples/)
  - SE Ranking: referral traffic from ChatGPT hit an **all-time high in May 2026**. — [SE Ranking](https://seranking.com/blog/chatgpt-referral-traffic-may-2026/)
- **Ads in ChatGPT:**
  - OpenAI began **testing ads for logged-in adult Free and Go users in the US on Jan 16, 2026**. Ads are contextual, labelled "Sponsored" and separated from answers, and OpenAI says ads **do not influence answers**. — [OpenAI: Testing ads in ChatGPT](https://openai.com/index/testing-ads-in-chatgpt/)
  - Later milestones, per Digiday: US self-serve Ads Manager with **CPA bidding** and third-party measurement; expansion to Europe; a **"click to chat, not to site"** Sponsored Agent format that opens a branded chat inside ChatGPT (Wayfair pilot). — [Digiday: Ads Manager US](https://digiday.com/marketing/openai-opens-up-chatgpt-ads-manager-to-the-u-s-while-promising-third-party-measurement-cpa-bidding/); [Digiday: CPA ads](https://digiday.com/marketing/openai-turns-on-cost-per-action-ads-inside-chatgpt/); [Digiday: Europe](https://digiday.com/marketing/openais-ads-business-hits-europe-at-the-six-month-mark/); [Digiday: click-to-chat](https://digiday.com/marketing/openais-next-chatgpt-ad-format-click-to-chat-not-to-site/)
  - Secondary sites give specific dates (US pilot Feb 9, self-serve May 5, UK/MX/BR/JP/KR Aug 11, 31 EU countries from Aug 23, 2026). **These were not verified against OpenAI.** — [Segwise](https://segwise.ai/blog/chatgpt-ads-2026-guide); [tech-insider.org](https://tech-insider.org/chatgpt-ads-rollout-2026/) (low reliability)
- **Agentic browsing:**
  - HUMAN Security, "State of Agentic Traffic – April 2026" (vendor): among agents, **Perplexity Comet 48.12%**, **ChatGPT Atlas 21.33%**, **Claude Chrome extension 17.33%**, **ChatGPT Agent 8.55%**. Browser-based agents accounted for about 71% of agent activity.
  - Agent requests are up **6,900% since July 2025**.
  - **Media (45.6%), ecommerce (38.2%) and travel (14.1%)** receive 98% of agentic traffic, so B2B SaaS is not yet a major target.
  
  — [HUMAN Security](https://www.humansecurity.com/learn/blog/state-of-agentic-traffic-april-26/)
  - Other claims (not verified; low-reliability or single sources): Claude for Chrome passed 10M installs by June 2026; ChatGPT Atlas "stopped functioning as a browser" on Aug 9, 2026; Comet launched on Android on Aug 19, 2026; Google folded Project Mariner into Gemini Agent / Chrome Auto Browse on May 4, 2026. — [HUMAN Security](https://www.humansecurity.com/learn/blog/state-of-agentic-traffic-april-26/); [tech-insider.org](https://tech-insider.org/comet-vs-gemini-agent-vs-chatgpt-atlas-2026/); [SearchVIU](https://www.searchviu.com/en/ai-browsers-2026-compared/)
- **Google scale and personalisation:**
  - AI Overviews has **2B+ monthly users** (Alphabet earnings commentary). *Date is uncertain: the 2B figure was first reported in 2025, and the Perplexity answer attributing it to Q2 2026 appears to mix up the years.* — [Seeking Alpha transcript](https://seekingalpha.com/article/4924442-alphabet-inc-googl-q2-2026-earnings-call-transcript)
  - Aggregators claim AI Mode has **1B+ MAU** and the Gemini app **950M MAU** (Q2 2026). **Not verified against Alphabet.** — [dev.to](https://dev.to/alifar/google-reports-950-million-gemini-app-users-as-ai-mode-passes-1-billion-3hc6)
  - Personal Intelligence was reportedly extended to AI Mode, Gemini and Gemini in Chrome in **March 2026** (aggregator). — [gradually.ai](https://www.gradually.ai/en/gemini-statistics/)
  - Preferred Sources in AIO/AI Mode, **May 27, 2026** (see section 1). — [PPC Land](https://ppc.land/google-extends-preferred-sources-into-ai-mode-as-new-sites-lose-ground/)
- **AI Overview prevalence:** estimates vary widely by method.

  | Tracker | Measurement | Share of queries with AIO |
  |---|---|---|
  | Semrush | Jan 2025 | 6.49% |
  | Semrush | Jul 2025 (peak) | ~25% |
  | Semrush | Nov 2025 | 15.69% |
  | Conductor | Q1 2026 (21.9M queries) | 25.11% |
  | BrightEdge | Mar 2026 (9 industries) | 48% |
  | Xponent21 | Apr 2026 (US) | 60.32% |

  **B2B tech and education reportedly crossed 80%.** Shopping keywords sit at only 13–14%. — [Searchlab compilation](https://searchlab.nl/en/statistics/ai-overviews-sge-statistics-2026); [SERPs.io](https://serps.io/blog/ai-overview-prevalence-by-industry) (compilations of vendor data)
- **AI platform traffic fragmentation (Similarweb):**
  - ChatGPT's share of AI-assistant web traffic fell from about **76% (June 2025) to ~53% (May 2026)**.
  - Gemini is above 25%, and Claude is the fastest-growing.
  - AI referral traffic averaged **770.7M monthly visits** worldwide from June 2025 to May 2026, **+117.4% YoY**.
  
  — [Similarweb AI stats](https://www.similarweb.com/blog/marketing/geo/gen-ai-stats/); [PPC Land](https://ppc.land/chatgpt-drops-to-52-7-as-claude-triples-its-ai-traffic-share/)
- **YouTube / video:**
  - YouTube is now the most-cited domain in AIO, up 34% in six months (Ahrefs). — [SEJ](https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/)
  - YouTube mentions are the strongest AI-visibility correlate (~0.737). — [BusinessWire](https://www.businesswire.com/news/home/20260526119691/en/Across-75000-Brands-YouTube-Mentions-Are-the-Strongest-Signal-of-AI-Visibility-New-Ahrefs-Report-Reveals)
- **Volatility:** ChatGPT's Reddit and Wikipedia citation shares collapsed within weeks in Aug–Sept 2025. — [Semrush](https://www.semrush.com/blog/most-cited-domains-ai/)
- **First-party measurement:** Bing AI Performance report (Feb 2026). — [Bing](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)

### Inferences
- The May 2026 ChatGPT change makes **brand entity recognition** (being named as a brand in the answer) directly clickable through to the homepage. That raises the value of being **mentioned**, not just cited as a footnote, and of a homepage that converts first-time AI visitors.
- The growth of Claude and Gemini supports multi-engine monitoring and Brave/Bing indexing hygiene.
- ChatGPT ads (CPA bidding, click-to-chat) give Quotr a paid route into AI answers alongside organic GEO.
- Agentic traffic is concentrated in media, ecommerce and travel. For B2B construction SaaS it is a watch item, not a priority. Clean, accessible pricing and product pages still future-proof for agents.

### Gaps
- No verified first-party figure for AI Mode MAU in 2026.
- Current status of ChatGPT Atlas and ChatGPT shopping / Instant Checkout / Agentic Commerce Protocol could not be verified.
- The effect of ChatGPT memory/personalisation on brand recommendations is unquantified.
- Axios (Sept 19, 2026) and Comscore/Digiday pieces on AI referral splintering were found but not read. — [Axios](https://www.axios.com/media-trends-membership/2026/09/19/ai-search-traffic-referrals-news-sites); [Digiday/Comscore](https://digiday.com/media/comscore-data-shows-how-ai-discovery-is-splintering-beyond-chatgpt/)

---

## 5. Traffic impact: CTR decline, zero-click, and the volume and conversion of AI referral traffic

### Takeaway
AI Overviews clearly reduce organic CTR:
- Pew: 8% vs 15% click rate.
- Ahrefs: position-1 CTR down 58% (Dec 2025 data).
- Seer: down 61%, with a partial 2026 rebound.

Zero-click Google searches rose to about **68%** (SparkToro/Similarweb, 2026), and AI Mode sessions are about 93% zero-click (Semrush, 2025). Google disputes the harm and says total clicks are stable and of higher quality. AI referral traffic is still small (<1% of site traffic in most datasets) but growing fast. Its conversion quality is **contested**:
- For B2B SaaS, single-company data (Ahrefs) and modelled estimates (Semrush 4.4x) point higher.
- The only peer-reviewed study (e-commerce, 973 sites) finds ChatGPT traffic converts **worse** than organic.

**Being cited inside an AIO partly offsets the loss** (Seer: +35% organic clicks for cited brands).

### Cited Findings
**Clicks and CTR**
- **Pew Research Center** (July 22, 2025; **900+ US adults, 68,879 Google searches, March 2025**):
  - users clicked a link on **8%** of visits to pages with an AI summary, vs **15%** without;
  - only **1%** clicked a link inside the summary;
  - sessions ended on **26%** of pages with an AI summary vs **16%** without.
  
  — [Pew Research](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)
- **Ahrefs** (vendor):
  - AIOs cut position-1 CTR by **34.5%** (April 2025 study);
  - an update using **Dec 2025 data on 300K keywords** found a **58%** reduction (published Feb 2026; press release May 18, 2026).
  
  — [Ahrefs 34.5%](https://ahrefs.com/blog/ai-overviews-reduce-clicks/); [Ahrefs update](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update); [BusinessWire](https://www.businesswire.com/news/home/20260518322756/en/New-Research-Googles-AI-Overviews-Now-Cost-Websites-58-of-Their-Clicks)
- **Seer Interactive** (agency):
  - Sept 2025 update: organic CTR on AIO queries fell from **1.76% (2024) to 0.61% (2025)**, a **-61%** change. — [Seer Sept 2025](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update)
  - 2026 update (**53 brands, 5.47M queries, 2.43B impressions, Jan 2025–Feb 2026**): CTR on AIO queries **rebounded from 1.3% (Dec 2025) to 2.4% (Feb 2026)**, still below pre-AIO levels; Seer calls this a possible "new normal". — [Seer 2026 update](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update)
  - **Brands cited inside the AIO get 35% more organic clicks and 91% more paid clicks** than non-cited brands on the same SERP. — [Seer 2026 update](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update)
- **Zero-click:**
  - SparkToro (2026) found **68.01%** of US Google searches ended without a click in Jan–Apr 2026 (Similarweb panel), up from **60.45%** in 2024 (Datos). Less than a third of searches now send a click anywhere. — [SparkToro](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/)
  - *Note: the 2024 and 2026 figures come from different data providers, so the comparison is approximate.*
- **AI Mode:** Semrush (vendor; **69M US desktop sessions, May 1–July 5, 2025**) found:
  - **93%** of AI Mode sessions ended with no external click, vs 83% with an AIO and ~60% for standard search;
  - AI Mode grew from 0.25% to 1% of sessions over the period.
  
  Secondary summaries add that transactional AI Mode searches still sent about 69% of users to websites (not verified). — [Semrush](https://www.semrush.com/blog/google-ai-mode-seo-impact/)
- **Google's position:**
  - Liz Reid (Aug 2025): "total organic click volume from Google Search to websites has been relatively stable year-over-year" and "average click quality has increased". Quality clicks are defined as clicks where users don't quickly return. — [Google blog](https://blog.google/products-and-platforms/products/search/ai-search-driving-more-queries-higher-quality-clicks/)
  - Google later pushed a **"bounce clicks"** explanation for lost traffic. — [SEJ](https://www.searchenginejournal.com/google-pushes-bounce-clicks-explanation-for-ai-overview-traffic-loss/572986/)
  - Google has published no data that would let outsiders test this. — [Press Gazette](https://pressgazette.co.uk/platforms/google-search-clicks-traffic-2025-ai-overviews/)

**AI referral volume**
- Similarweb: 770.7M monthly AI referral visits worldwide (Jun 2025–May 2026), +117.4% YoY. — [Similarweb](https://www.similarweb.com/blog/marketing/geo/gen-ai-stats/)
- Kaiser & Schulze (see below): ChatGPT referrals were **<0.2% of total traffic**, about **200x smaller than Google organic**. — [Search Engine Land](https://searchengineland.com/llms-google-referral-conversion-study-463747)
- Ahrefs' own site: AI search was **0.5%** of visits (up from 0.3%). — [Ahrefs](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/)
- Secondary aggregations say Google organic remains **47–190x larger** than AI referral traffic, and that ChatGPT's share of B2B AI referrals fell to **62.6%** (Claude 18.5%, Gemini 10.6%, Perplexity 7.3%) by Mar–Apr 2026. **The primary source was not identified.** — [Demand Local](https://www.demandlocal.com/blog/ai-referral-traffic-conversion-rate-statistics/); [AirOps](https://www.airops.com/blog/ai-referral-traffic-conversion-rates)

**AI referral conversion: conflicting evidence**
- **Pro (SaaS-specific, single company):** Ahrefs: **0.5% of visits drove 12.1% of signups**, about **23x** the conversion rate of organic. AI visitors viewed 50% more pages. — [Ahrefs](https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/)
- **Pro (modelled):** Semrush (June 9, 2025; 500+ marketing/SEO topics) estimates an AI visitor is worth **4.4x** a traditional organic visitor. It projects AI search traffic could overtake traditional search by **2028**. These are **projections, not observed data.** — [Semrush](https://www.semrush.com/blog/ai-search-seo-traffic-study/); [PPC Land](https://ppc.land/ai-search-visitors-worth-4-4x-more-than-traditional-organic-traffic/)
- **Pro (unverified):** "Opollo, 312 B2B firms: 14.2% vs 2.8%" and "ChatGPT 15.9%, Perplexity 10.5%, Claude 5.0%" conversion rates circulate in aggregators. **Primary sources not verified.** — [Demand Local](https://www.demandlocal.com/blog/ai-referral-traffic-conversion-rate-statistics/)
- **Con (peer-reviewed, e-commerce):** Kaiser (U. Hamburg) & Schulze (Frankfurt School), *Marketing Science* (2025): **973 e-commerce sites, $20B combined revenue, 12 months of first-party data**. ChatGPT referrals converted **worse** than Google organic (**~13% lower**) and paid, and affiliate links were **86% more likely to convert**. Engagement (bounce, depth) was relatively high. — [INFORMS Marketing Science](https://pubsonline.informs.org/doi/10.1287/mksc.2025.0489); [Search Engine Land](https://searchengineland.com/llms-google-referral-conversion-study-463747); [Digiday](https://digiday.com/marketing/e-commerce-sites-see-low-sales-from-chatgpt-traffic-new-study-finds/)
- **Con/nuance:** Ahrefs separately found AI visitors **visit fewer pages and bounce more** than search visitors. This conflicts with its earlier finding of 50% more pages. — [Ahrefs AI traffic quality study](https://ahrefs.com/blog/ai-traffic-quality-study/)

**Buyer behaviour (B2B software)**
- G2 (vendor survey, March 2026, n = 1,076): **51%** of B2B software buyers start research with an AI chatbot more often than Google, and about **70%** changed their vendor choice because of AI guidance. — [PR Newswire](https://www.prnewswire.com/news-releases/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots-302742807.html)

### Inferences
- For "maintaining top-of-funnel reach", the data suggests redefining reach from **clicks** to **presence in answers**: being mentioned or recommended and being cited. Informational blog traffic is where AIO and AI Mode losses concentrate, and B2B tech queries have among the highest AIO prevalence. Quotr should expect informational/educational clicks to keep declining even if its rankings hold.
- Being cited inside the AIO partly offsets the loss (Seer +35%), and the May 2026 ChatGPT update routes more AI clicks to homepages. Measurement should therefore track:
  - AI citations (Bing AI Performance, third-party trackers);
  - branded search growth;
  - `utm_source=chatgpt.com` / AI referrals and their conversion;
  - demo and signup attribution ("how did you hear about us" fields).
  
  Raw sessions alone will understate impact.
- Conversion evidence for B2B SaaS is favourable but thin: one company's data plus vendor models. The only rigorous study (e-commerce) is negative. Quotr should present "AI traffic converts better" as a hypothesis to test in its own analytics, not a given.
- Google organic still dwarfs AI referrals (roughly 50–200x). SEO fundamentals remain the base layer, and Google says they are also what qualifies content for AI features.

### Gaps
- No AEC/construction-software-specific CTR or AI-referral benchmark was found.
- Primary sources for several widely repeated B2B conversion stats (Opollo; per-platform conversion rates; the B2B referral share split) were not located.
- Seer's 2026 rebound covers only two months (Dec 2025–Feb 2026). Whether it persisted through Sept 2026 is unknown.
- Pew's study reflects March 2025 behaviour, before the AI Mode rollout and the Gemini 3 AIO upgrade. No 2026 Pew update was found.
