---
type: guide
description: How ChatGPT, Google AI Overviews/AI Mode, Perplexity, Gemini, Claude and Copilot pick sources, and their crawlers.
last_verified: 2026-09-25
verify_every_days: 90
---
# How AI Engines Choose Their Sources

> [!abstract] What this page is for
> A plain-English explanation of how ChatGPT, Google AI Overviews, Google AI Mode, Perplexity, Gemini, Claude and Microsoft Copilot build their answers and pick the pages they cite, with each engine's crawlers and what blocking them does, and what it all means for Quotr.ai.

> [!info]- Sources
> Research notes [[geo_ai_citation_signals_2026]] (§1, §2, §4) as corrected by the fact-check [[verification_geo_evidence]] (its corrections win), [[geo_content_playbook_b2b]] (§1–§4), [[quotr_ai_visibility_tests]] (§6), and the final report [[Quotr GEO AEO strategy audit]]. Extra sources checked on 2026-09-25 through web search result summaries (pages not opened in full): Google's AI features doc and Google-Extended coverage, Perplexity's crawler docs, Anthropic's crawler docs, OpenAI's crawler docs and ChatGPT-User change, Bing's NOCACHE/NOARCHIVE controls, Microsoft's May 2026 "grounding index" post, Google's Gemini grounding docs and I/O 2026 coverage. Each is linked where used.

---

## Words used on this page

| Word | Plain meaning |
|---|---|
| **Training data / "parametric" knowledge** | What the AI model learned from a huge snapshot of the web before it was released. It answers from memory, with no live lookup. |
| **Live retrieval** | The AI runs a web search while you wait, reads some pages and uses them in the answer. |
| **Index** | The giant stored copy of web pages that a search engine keeps (Google's index, Bing's index, and so on). An AI can only retrieve what is in the index it uses. |
| **Grounding** | Tying the AI's answer to real pages it just retrieved, so it states facts it can point to. The links it shows are the "grounding" sources. |
| **Query fan-out** | The AI splits your one question into many smaller searches, then combines what it finds. |
| **Passage** | A section or paragraph of a page. AI engines usually pull passages, not whole pages. |
| **Citation** | The AI shows your page as a source (a footnote, link or card). |
| **Mention** | The AI says your brand's name in its answer text. A page can be cited without the brand being mentioned, and the reverse. |
| **Crawler / bot / user-agent** | A program that fetches web pages. Its "user-agent" is the name it announces (for example `GPTBot`). |
| **robots.txt** | A public file on a website that tells crawlers what they may fetch. Well-behaved crawlers follow it. |

More terms: [[GEO glossary]].

---

## The short version

1. **Every major AI engine answers from two places:** what the model already "knows" from training, and pages it fetches live from a search index. ChatGPT only searched the web on about a third of prompts in 2025–early 2026 (Nectiv ~31%; OtterlyAI 34.5% in Feb 2026; neither re-checked by the fact-check). For the rest, it answers from memory.
2. **Each engine leans on a different index.** Google's engines use Google's index. Copilot uses Bing. Claude's search uses Brave Search (plus possibly other layers). Perplexity has its own index plus partners. ChatGPT uses its own crawler plus unnamed "third-party search providers". **Being indexed well in Google, Bing and Brave is the entry ticket.**
3. **They "fan out".** One buyer question becomes many small searches. Pages that answer a precise sub-question well get picked.
4. **They pick passages, not pages.** A clear, self-contained section near the top of a page is easier to lift. But Google says you do not need to chop pages into tiny chunks.
5. **Being retrieved is not the same as being cited, and being cited is not the same as being named.** Quotr's own tests show this: Perplexity listed a quotr.ai page among its sources in 6 of 32 unbranded answers (and used it in the answer text in 4), but named Quotr in only 1 ([[Quotr GEO AEO strategy audit|report]]).
6. **Official guidance is simple.** Google (May 15, 2026): no special files, markup or chunking are needed; a page must be indexed and eligible to show a snippet, and "valuable, unique, non-commodity content" matters most. Microsoft's October 2025 guidance is more specific (clear headings, short single-idea sections, schema, fresh and consistent facts).
7. **Engines disagree with each other and change fast.** One analysis found 91% of AI citations appear in only one engine (Kevin Indig, H1 2026; not re-checked). Citation lists churn month to month.
8. **For Quotr:** keep every AI search crawler allowed (it already is), make sure Bing and Brave see the site, make facts consistent so engines stop hedging, and earn mentions on the third-party pages engines already pull from.

---

## 1. How an AI answer is put together

The steps below are a simplified picture that fits what Google, Microsoft, OpenAI and Anthropic have published. Exact details differ by engine and are not fully public.

| Step | What happens | What decides whether Quotr gets in |
|---|---|---|
| 1. Read the question | The model reads the prompt (and, in some products, the user's history or preferences). | Nothing yet, except personalisation (see 1.8). |
| 2. Decide: memory or search? | The model decides whether it needs fresh facts. Short, factual or "best/compare/price" questions are more likely to trigger a search. | If no search happens, only **training data** matters: how widely and consistently Quotr was described on the web before the model's cut-off. |
| 3. Fan out | The question is split into several sub-queries (for example, a "best takeoff software for subs" question might also search pricing, reviews and trade-specific tools). | Pages that match a precise sub-query are more likely to be retrieved. |
| 4. Retrieve | The engine runs those searches in its index and gathers candidate pages. | Being **indexed** and **ranking** for the sub-queries in that engine's index. |
| 5. Pick passages | It pulls the passages that best answer each sub-query. | Clear, self-contained sections with specific facts (numbers, dates, names). |
| 6. Ground and write | The model writes an answer and attaches the sources it relied on. | Whether the passage **supports a claim** cleanly, and whether other sources agree. |
| 7. Show citations and names | Some sources become visible citations; some brands are named in the text. | Being named needs the brand attached to the fact, plus corroboration from other sites. |

### 1.1 Training knowledge vs live retrieval

- **Training knowledge** is a frozen snapshot. It is built from broad web text, so it reflects how often and how consistently a brand was described across many sites, not just on its own site. The fact-check and notes infer that this is why off-site presence matters beyond anything on-page ([[geo_ai_citation_signals_2026|signals notes §1]]).
- **How often ChatGPT searches:** Nectiv found web search ran on about **31%** of prompts (2025; [Search Engine Land](https://searchengineland.com/chatgpt-search-prompts-data-463407)). OtterlyAI (a vendor) found **34.5% in Feb 2026, down from 46% in late 2024**, with search-enabled prompts getting longer (4.7 → 8.7 words) ([OtterlyAI](https://otterly.ai/blog/how-often-does-chatgpt-trigger-a-web-search/)). Neither figure was re-checked by the fact-check.
- **What this means for Quotr:** training data may still carry the old name "Quotr.io" and old descriptions (for example the F6S listing still describes an old Revit plug-in; [[Off-site presence]]). Consistent facts on many third-party profiles are what slowly correct the model's "memory". Live retrieval is the faster lever, because fixed pages can be re-read within days or weeks.

### 1.2 Which index each engine searches

| Engine | Index it retrieves from | How sure are we? |
|---|---|---|
| Google AI Overviews, AI Mode | Google Search index | Official ([Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)) |
| Gemini app | Google Search ("Grounding with Google Search") | Official ([Gemini API docs](https://ai.google.dev/gemini-api/docs/google-search)) |
| Microsoft Copilot | Bing index | Official ([Microsoft Advertising, Oct 2025](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers); [Bing, May 2026](https://blogs.bing.com/search/May-2026/Evolving-role-of-the-index-From-ranking-pages-to-supporting-answers)) |
| ChatGPT search | OpenAI's own crawler (OAI-SearchBot) plus "third-party search providers" | Official that third parties are used; **which ones is not confirmed** by OpenAI ([OpenAI Publishers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)) |
| Claude | Brave Search is the only search provider on Anthropic's subprocessor list; secondary sources say turbopuffer was also added under "Web Search" by Sept 2026 | Brave: well supported, but Anthropic has not publicly said "Brave = index" ([[verification_geo_evidence\|verification claim #29]]; [Xponent21](https://xponent21.com/insights/claude-web-search-brave-turbopuffer/)) |
| Perplexity | Its own index built by PerplexityBot, plus search partners | Secondary summaries only ([LLM Pulse](https://llmpulse.ai/blog/how-perplexity-works/)) |

**So what:** a page that ranks in Google but is weak in Bing or Brave may never reach Copilot, ChatGPT (partly) or Claude. This is why the report lists "add the blog sitemap to robots.txt" and Bing Webmaster Tools as quick wins ([[Quotr GEO AEO strategy audit|report, 30-day plan]]).

### 1.3 Query fan-out

- **Google, officially:** AI Overviews and AI Mode "may use a query fan-out technique — issuing multiple related searches across subtopics and data sources — to develop a response". Google's example: "how to fix a lawn full of weeds" fans out to "best herbicides for lawns", "remove weeds without chemicals" and "how to prevent weeds in lawn" ([Google AI features doc](https://developers.google.com/search/docs/appearance/ai-features)).
- **ChatGPT:** 89.6% of search-triggering prompts produced 2+ extra searches beyond the user's wording (Nectiv data via [Search Engine Land](https://searchengineland.com/chatgpt-search-prompts-data-463407); not re-checked).
- **Titles that match sub-queries:** Ahrefs (1.4M ChatGPT prompts) found cited pages had titles more similar to ChatGPT's narrower fan-out sub-queries than pages it passed over. Pages with descriptive URL slugs were cited 89.78% of the times they appeared in results, vs 81.11% for less descriptive URLs ([Ahrefs](https://ahrefs.com/blog/why-chatgpt-cites-pages/); vendor study, correlation).
- **Microsoft shows its sub-queries:** Bing Webmaster Tools' AI Performance report (public preview, announced Feb 10, 2026) lists "grounding queries", the internal search phrases Copilot generated to find a site's pages ([Bing blog](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)).
- **The warning:** Google says creating separate pages for every fan-out variation, mainly to manipulate AI answers, can break its **scaled content abuse** spam policy. Genuine subtopic coverage is fine ([Google AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide); [[verification_geo_evidence|verification claim #2]]).

**For Quotr:** write pages whose titles and headings match precise buyer sub-questions ("AI takeoff pricing per seat", "landed cost of factory-direct cabinets"), but do not spin up near-duplicate "[trade] estimating services in [city]" pages. See [[Myths and risks]].

### 1.4 Passage-level retrieval

- **Microsoft (Oct 2025):** Copilot "parses content into smaller structured pieces" and assesses each for authority and relevance, then assembles answers from several sources ([Microsoft Advertising](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers)).
- **Microsoft (May 6, 2026):** its newer post says an index built for AI "grounding" must also check whether a page's meaning survives chunking, whether the source is clearly identified, whether the information is fresh enough, and whether key facts are actually retrievable ([Bing Search blog](https://blogs.bing.com/search/May-2026/Evolving-role-of-the-index-From-ranking-pages-to-supporting-answers), via [Search Engine Land](https://searchengineland.com/microsoft-ai-answers-index-476691)). The fact-check flagged this post as not yet read in full.
- **Where on the page citations come from:** Kevin Indig's "The Science Of How AI Pays Attention" (Growth Memo, Feb 2026; 1.2M ChatGPT answers analysed, 18,012 verified citations) found **44.2%** of ChatGPT citations come from the first 30% of a page ([Growth Memo](https://www.growth-memo.com/p/the-science-of-how-ai-pays-attention)). This describes where citations fall; it is not proof that moving text up causes citations ([[verification_geo_evidence|verification H9]]).
- **Google's counterpoint:** there is no need to "chunk" content into tiny pieces. Google's systems can handle several topics on one page and show the relevant part ([Google AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)).

**For Quotr:** keep the "Quick Answer" blocks, question headings and tables Quotr already uses ([[GEO tactics already used]]). Make each section make sense on its own, with the brand name inside key facts. Do not split pages into micro-pages.

### 1.5 Grounding and citation: retrieved ≠ cited ≠ named

- **Retrieved but not cited:** Ahrefs found about half of retrieved pages were cited in ChatGPT overall, and ChatGPT retrieves Reddit heavily but cites it only 1.93% of the time ([Ahrefs](https://ahrefs.com/blog/why-chatgpt-cites-pages/); [SEJ](https://www.searchenginejournal.com/chatgpt-often-retrieves-but-rarely-cites-reddit-pages-data-shows/572243/); vendor).
- **Cited but not named:** in a Semrush dataset (1,094 US categories, 600K+ ChatGPT citations, Jan–Jun 2026), Indig found the correlation between a domain's citations and its brand mentions was slightly **negative (−0.229)**. The most-cited domain was also the most-mentioned brand in only **20.8%** of cases ([Kevin Indig](https://substack.com/@kevinindig/note/c-298265127); not re-checked).
- **Quotr example:** for "outsourced construction estimating price per square foot", Perplexity used Quotr's blog as its **first source** twice and repeated Quotr's $0.25 and $0.10 per sq ft rates, but credited them to "one outsourced estimating service" and "some firms" ([[Quotr GEO AEO strategy audit|report]]; [[AI visibility baseline]]).
- **How many sources each engine shows:** Muck Rack (May 7, 2026; 25M+ links; vendor) found ChatGPT cites sources in **96%** of responses (about 5 each), Gemini in **82%** (about 8) and Claude in **55%** (about 13) ([Muck Rack](https://muckrack.com/blog/what-is-ai-reading-may-2026); read by the fact-check).
- **What grounding systems want:** Microsoft says grounding is "built around supportable facts with clear sourcing", because an AI commits to an answer while a search user can self-correct ([Bing, May 2026](https://blogs.bing.com/search/May-2026/Evolving-role-of-the-index-From-ranking-pages-to-supporting-answers) via [Search Engine Land](https://searchengineland.com/microsoft-ai-answers-index-476691)).

**For Quotr:** write sentences so the name travels with the fact ("Quotr.ai's Estimation Service charges $0.25 per sq ft for projects under 50,000 sq ft"), and give each claim a source or method. Details: [[GEO writing style guide]].

### 1.6 Recency (freshness)

- **Ahrefs (July 28, 2025; 16.975M cited URLs; vendor):** URLs cited by AI assistants (ChatGPT, Perplexity, Copilot, Gemini) averaged 1,064 days old, vs about 1,416–1,432 days for Google organic results (Ahrefs' own page gives both numbers). **ChatGPT showed the strongest recency preference; Google AI Overviews the weakest.** Cited pages still averaged **2.9 years** old ([Ahrefs](https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/); read by the fact-check).
- Ahrefs' author "suspect[s] most brands will see better results from creating new, high-quality content than … extremely frequent content updating", and Google's John Mueller warns against date-only updates (same source, per [[verification_geo_evidence|verification claim #10]]).
- Posts "lightly refreshed with '2026' in the title" were among pages that lost Google visibility in early 2026 (Lily Ray observation; [Substack, Feb 3, 2026](https://lilyraynyc.substack.com/p/is-google-finally-cracking-down-on)).

**For Quotr:** update pricing, comparison and benchmark pages when facts really change, and say what changed. Fix the main sitemap, where every URL claims it changed "today" ([[Website audit]]).

### 1.7 Volatility and disagreement between engines

| Finding | Source | Notes |
|---|---|---|
| 91% of AI citations appear in only one engine (ChatGPT, Perplexity, AI Overviews) | Kevin Indig, "The Consensus Gap", H1 2026 ([Growth Memo](https://www.growth-memo.com/p/the-consensus-gap)) | Not re-checked |
| 40–60% of cited domains change month to month for the same queries; one-month drift: AI Overviews 59.3%, ChatGPT 54.1%, Copilot 53.4%, Perplexity 40.5% | Profound, 240M ChatGPT citations ([Profound](https://www.tryprofound.com/blog/ai-search-volatility)) | Vendor |
| Only ~10.6% of 1,127 cited URLs were cited in all 3 waves; 33% retention over 28 days; Gemini lowest (11%) | Digital Authority Partners, 30 queries, 5 engines, 3 waves 14 days apart ([DAP](https://www.digitalauthority.me/resources/ai-visibility-study/)) | Agency study; numbers confirmed from index text |
| Reddit's share of ChatGPT citations fell from 3.83% to 0.52% within weeks (Jul 18–Aug 7 vs Aug 14–17, 2026) | Promptwatch ([Promptwatch](https://promptwatch.com/blog/chatgpt-stop-citing-reddit)); [Axios, Aug 20, 2026](https://www.axios.com/2026/08/20/chatgpt-reddit-citations-geo-strategy) | A separate, earlier collapse happened Aug–Sept 2025 (Semrush: ~60% → ~10% of responses) |
| ChatGPT and Gemini recommend a different #1 software in one of every three categories | Press-release headline, Aug 12, 2026 ([GlobeNewswire](https://www.globenewswire.com/news-release/2026/08/12/3343763/0/en/chatgpt-and-gemini-recommend-different-1-software-in-one-of-every-three-categories-new-study-finds.html)) | Headline only; method not seen |

**For Quotr:** never judge progress from one engine or one run. The monthly tracking set runs the 23 headline (Tier A) prompts twice and the rest once, on five engines every month (ChatGPT, Google AI Mode, Google AI Overviews, Perplexity, Gemini), with Claude and Copilot added each quarter ([[Tracking set]]).

### 1.8 Personalisation

- **Google Preferred Sources** (extended into AI Overviews and AI Mode on May 27, 2026): users can pick favourite sites, and Google says people are "twice as likely to click through to a Preferred Source"; 345,000+ sources had been selected ([Google blog](https://blog.google/products-and-platforms/products/search/original-high-quality-content-search/); [SE Roundtable](https://www.seroundtable.com/google-ai-preferred-sources-41394.html)). Critics say it favours established publishers.
- **Personal context:** a UK study of ChatGPT, Gemini, Claude and Perplexity (6 personas, 30 prompts) found personalisation can change which brands are recommended ([EIN Presswire](https://www.einpresswire.com/article/944542004/new-study-finds-ai-personalization-can-change-which-brands-chatgpt-and-gemini-recommend); press release, method not reviewed). Google reportedly extended "Personal Intelligence" to AI Mode and Gemini in March 2026 (aggregator report; not verified).
- **For Quotr:** tracking should use clean, logged-out or history-free sessions so months are comparable ([[Tracking set]]).

---

## 2. Crawlers and user-agents: who fetches Quotr's pages, and what blocking does

**Quotr today:** robots.txt is `User-agent: *` / `Allow: /` with no named-bot rules, so **every crawler below is allowed**. Cloudflare's "AI Labyrinth" bot trap is on (it only traps bots that ignore crawl rules). Whether Cloudflare's separate "Block AI bots" setting is off is **TO CONFIRM with Quotr** ([[Website audit|website-audit.md §1]]).

| Company / engine | User-agent (name in logs and robots.txt) | What it does | Follows robots.txt? | What blocking it does | Recommendation for Quotr |
|---|---|---|---|---|---|
| OpenAI / ChatGPT | **OAI-SearchBot** | Finds pages for ChatGPT search results, snippets and citations | Yes | Pages are not surfaced in ChatGPT search. OpenAI: do not block it if you want to be included. A disallowed page can still appear as a bare link and title if ChatGPT finds it through a third-party search provider, unless it is `noindex` ([OpenAI FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)) | **Allow** |
| OpenAI / ChatGPT | **GPTBot** | Collects training data for OpenAI models | Yes | Future content is kept out of model training. OpenAI treats it separately from OAI-SearchBot ([OpenAI crawler docs](https://developers.openai.com/api/docs/bots)) | **Allow** (Quotr wants to be in the model's "memory") |
| OpenAI / ChatGPT | **ChatGPT-User** | Fetches a page live when a user's chat, a Custom GPT or a GPT Action needs it | Since Dec 9, 2025 OpenAI says "because these actions are initiated by a user, robots.txt rules may not apply" ([PPC Land](https://ppc.land/openai-revises-chatgpt-crawler-documentation-with-significant-policy-changes/); [SEJ](https://www.searchenginejournal.com/openai-says-robots-txt-may-not-apply-to-chatgpts-fetch-bot/585864/)) | Blocking by robots.txt may not work; a firewall block would stop ChatGPT reading pages users ask about | **Allow** |
| OpenAI / ChatGPT ads | **OAI-AdsBot** | Visits landing pages submitted as ChatGPT ads to check ad policy and relevance; OpenAI says the data does not train its models | — | Can slow ad approval | Only relevant if Quotr runs ChatGPT ads ([SEJ](https://www.searchenginejournal.com/openais-crawler-docs-now-list-oai-adsbot-for-chatgpt-ads/572861/); [OpenAI Help](https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers)) |
| Google (Search, AI Overviews, AI Mode, Gemini grounding) | **Googlebot** | Builds the Google Search index | Yes | Removes the page from Google Search **and** from AI Overviews, AI Mode and Gemini's Search grounding | **Allow** |
| Google (Gemini, Vertex AI) | **Google-Extended** (a robots.txt token, not a separate crawler) | Controls whether content Google crawls may be used to train Gemini models **and to ground answers in the Gemini apps and Vertex AI** | Yes | Does **not** affect Google Search inclusion or ranking, including AI Overviews ([Google AI features doc](https://developers.google.com/search/docs/appearance/ai-features); [SEJ](https://www.searchenginejournal.com/google-updates-gemini-vertex-ai-user-agent-documentation/545409/)). It **can** reduce use in Gemini app answers | **Allow** |
| Microsoft (Bing, Copilot) | **Bingbot** | Builds the Bing index, which feeds Copilot and Bing AI answers (and, reportedly, part of ChatGPT; not confirmed) | Yes | Out of Bing and Copilot | **Allow**, and submit sitemaps in Bing Webmaster Tools |
| Anthropic (Claude) | **ClaudeBot** | Collects training data | Yes, including Crawl-delay | Future content excluded from training | **Allow** |
| Anthropic (Claude) | **Claude-SearchBot** | Indexes content to improve Claude's search results | Yes | "May reduce visibility and accuracy in Claude-powered search answers" | **Allow** |
| Anthropic (Claude) | **Claude-User** | Fetches a page when a Claude user's question needs it | Yes | Claude cannot fetch the page for users, which "may reduce your visibility in user-directed search responses" | **Allow** |
| Perplexity | **PerplexityBot** | Builds Perplexity's index; Perplexity says it is not used for model training | Yes (Allow/Disallow; reportedly ignores Crawl-delay) | Pages drop out of Perplexity's index (changes can take up to 24 hours) | **Allow** |
| Perplexity | **Perplexity-User** | Fetches pages live when a user's question needs fresh content or a user clicks a citation | Perplexity has said it is "an agent, not a bot", so it generally does not honour robots.txt (secondary sources) | robots.txt blocking may not work | **Allow** |
| Apple | **Applebot-Extended** | Controls use of content for Apple AI training | Yes | Kept out of Apple AI training | **Allow** |
| Common Crawl | **CCBot** | Open web crawl that many AI models use for training | Yes | Less presence in open training datasets | **Allow** |

Sources for the table: OpenAI ([Publishers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq), [crawler overview](https://developers.openai.com/api/docs/bots)); Anthropic ([Anthropic privacy center](https://privacy.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), [Search Engine Land](https://searchengineland.com/anthropic-claude-bots-470171), [SE Roundtable](https://www.seroundtable.com/anthropic-updates-its-crawler-docs-40978.html)); Perplexity ([Perplexity crawler docs](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), [51Degrees](https://51degrees.com/blog/perplexity-ai-2026)); Google ([AI features doc](https://developers.google.com/search/docs/appearance/ai-features)); Apple/Common Crawl descriptions from [[Website audit]]. On Aug 4, 2025, Cloudflare published a report saying Perplexity used undeclared crawlers that rotated user-agents and IPs to get around no-crawl rules (reported by [51Degrees](https://51degrees.com/blog/perplexity-ai-2026); Cloudflare's post not opened).

### Other controls (beyond robots.txt)

| Control | Engine | What it does | Quotr should… |
|---|---|---|---|
| `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex` | Google | These are the controls that limit how a page appears in AI Overviews and AI Mode ([Google AI features doc](https://developers.google.com/search/docs/appearance/ai-features)) | Not use them on marketing pages. Use `noindex` on staging copies such as test.quotr.io |
| **Search generative AI control** (Search Console) | Google | Property-level opt-out from AI Overviews, AI Mode and Discover's generative features. Announced June 3, 2026; worldwide since Aug 31, 2026. Opted-out sites get no traffic or impressions from those surfaces. Google says it is not a ranking signal and is separate from Google-Extended ([Search Console Help](https://support.google.com/webmasters/answer/16908024?hl=en); [SEJ](https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/)) | **Not** opt out ([[Quotr GEO AEO strategy audit\|report]]) |
| `NOCACHE` meta tag | Bing / Copilot | Only the URL, title and snippet may be shown in AI answers ([Bing blog, Sept 2023](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat)) | Not use |
| `NOARCHIVE` meta tag | Bing / Copilot | Content is not used in AI answers or linked from them, and not used for Microsoft model training; the page still appears in normal Bing results (same source; announced for "Bing Chat", now Copilot) | Not use |
| IndexNow | Bing, Yandex, Naver, Seznam, Yep (not Google) | Instantly tells participating engines a URL changed ([IndexNow.org](https://www.indexnow.org/)) | Use after fixing old prices, so Bing (and Copilot) re-read pages fast |

---

## 3. Engine by engine

Each section has: **at a glance**, **what is officially known**, **what studies show**, and **what it means for Quotr**. Quotr's own tests covered **Perplexity only**; everything about the other engines is general evidence, not a measurement of Quotr ([[AI visibility baseline|ai-visibility-baseline.md §10–11]]).

### 3.1 ChatGPT search (OpenAI)

**At a glance**

| Item | Detail |
|---|---|
| Index | OAI-SearchBot crawl plus unnamed third-party search providers |
| Crawlers | OAI-SearchBot (search), GPTBot (training), ChatGPT-User (live fetch), OAI-AdsBot (ads) |
| How often it searches | About 31–35% of prompts (2025–Feb 2026; not re-checked) |
| Referral tag | Adds `utm_source=chatgpt.com` to links ([OpenAI FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)) |
| Owner reporting | None first-party; use GA4 and prompt trackers |
| Market share | ChatGPT's share of AI-assistant web traffic fell from ~76% (June 2025) to ~53% (May 2026) (Similarweb; not re-checked). G2's survey says 63% of B2B software buyers use ChatGPT for this research (vendor survey) |

**Officially known**
- "Any public website can appear in ChatGPT search." Do not block OAI-SearchBot if you want to be included ([OpenAI FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)).
- OpenAI has **not** published how it weighs sources. Online "ranking weight" frameworks (for example "domain authority ~40%") are reverse-engineered guesses ([ZipTie.dev](https://ziptie.dev/blog/how-does-chatgpt-choose-its-sources/), which flags its own framework as speculative).
- **Branded links (May 7, 2026):** ChatGPT began linking brand names in answers straight to brand homepages. Profound (vendor) says OpenAI referrals to monitored brands "nearly doubled (~60–65%)" (Profound's own wording; the two figures do not quite match), the homepage share of those referrals rose from about 3.5% to ~24%, and **B2B software & SaaS was the biggest gainer, with daily OpenAI referrals up more than 200%** ([Profound](https://www.tryprofound.com/blog/chatgpt-referrals-branded-links); read by the fact-check). OpenAI can change this at any time.
- **Ads:** announced Jan 16, 2026; the US test began Feb 9, 2026; ads are labelled, separate from answers, and OpenAI says they **do not influence answers**. Advertiser-sponsored agents were tested in Sept 2026 ([OpenAI Help](https://help.openai.com/en/articles/20001047-ads-in-chatgpt); [Reuters](https://www.reuters.com/business/media-telecom/openai-tests-advertiser-sponsored-agents-expands-ai-tools-chatgpt-ads-2026-09-16/)).

**What studies show**
- **Freshest sources of any engine** (Ahrefs, 2025; see 1.6).
- **Page types:** "best X" listicles were **43.8%** of page types ChatGPT cited, and self-promotional lists that rank the publisher first were still cited (Ahrefs, 26,283 source URLs; [Ahrefs](https://ahrefs.com/blog/best-lists-research/)). HubSpot (vendor, June 2026) says ChatGPT favours comparison content (95% citation rate) and documentation (86%) ([HubSpot](https://blog.hubspot.com/marketing/content-format-types-that-earn-citations); directional, method not published).
- **SaaS sources:** in Aleyda Solis's SaaS data, ChatGPT favours structured written content (tech publications, review sites) and often cites homepages; video was only 1.0% of ChatGPT's cited sources vs 23.0% in AI Mode ([Aleyda Solis](https://www.aleydasolis.com/en/ai-search/saas-ai-search-optimization/); this article was not re-read by the fact-check).
- **Top domains:** Muck Rack (May 2026) still finds Wikipedia the top ChatGPT domain. Reddit's share collapsed twice (Aug–Sept 2025 and Aug 2026).
- **Brand factors:** in Ahrefs' 75,000-brand study, ChatGPT correlated more weakly with classic authority (branded search volume 0.352, Domain Rating 0.266) than Google's surfaces did ([Ahrefs](https://ahrefs.com/blog/ai-brand-visibility-correlations/); correlation).
- **Structure:** 44.2% of citations from the first 30% of a page (see 1.4). Indig also argues focused pages beat exhaustive guides in ChatGPT ([Growth Memo](https://www.growth-memo.com/p/shorter-focused-content-wins-in-chatgpt)).
- **Overlap with Google:** only 12% of links cited by ChatGPT, Gemini and Copilot appeared in Google's top 10 for the same prompt (Ahrefs, 15,000 prompts; [Ahrefs](https://ahrefs.com/blog/ai-search-overlap/); vendor).

**What it means for Quotr**
- ChatGPT could not be tested for this audit. **First job: a proper ChatGPT baseline** ([[Quotr GEO AEO strategy audit|report]]).
- Because ChatGPT may answer about two-thirds of prompts from memory (2025–early 2026 studies; not re-checked), Quotr needs consistent third-party descriptions (G2, Crunchbase, F6S, LinkedIn, press) under the name "Quotr.ai", with "Quotr.io" as a known former name.
- Since May 2026 every mention of "Quotr.ai" in a ChatGPT answer can be a clickable link to the homepage. The homepage must work for first-time visitors who arrive with a question.
- ChatGPT prefers fresh, focused pages: keep pricing and comparison pages current and correct (about 13 URLs still show the old "$299.90" entry price).
- Ads sit next to answers, not inside them. Treat them as a separate paid test ([[Traffic and funnel impact]]).

### 3.2 Google AI Overviews

**At a glance**

| Item | Detail |
|---|---|
| Index | Google Search index; crawler is Googlebot |
| Model | Upgraded to Gemini 3 globally in January 2026 ([SEJ](https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/)) |
| Scale | 2.5 billion monthly users (Google, I/O, May 19, 2026) ([Google blog](https://blog.google/products-and-platforms/products/search/search-io-2026/)) |
| Owner reporting | Search Console **Generative AI performance report**: impressions by page, country and date; **no clicks, CTR or queries**; worldwide since Aug 31, 2026 ([Google](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports); [SEJ](https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/)) |
| Opt-out | Search generative AI control (see section 2). Quotr should not use it |

**Officially known**
- "No additional requirements" to appear. To be a supporting link, a page must be **indexed and eligible to show in Search with a snippet** ([Google AI features doc](https://developers.google.com/search/docs/appearance/ai-features)).
- Google's **May 15, 2026 guide** says no AI text files (llms.txt), no special schema, no Markdown versions and no chunking are needed; its main positive advice is "valuable, unique, non-commodity content" ([Google guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide); [SEJ](https://www.searchenginejournal.com/googles-new-ai-search-guide-calls-aeo-and-geo-still-seo/575026/); confirmed by the fact-check).
- Fan-out is used (see 1.3). Making pages for every fan-out variation can break the scaled content abuse policy.
- **Since I/O 2026, AI Overviews and AI Mode are one flow:** a follow-up question on an AI Overview continues in AI Mode ([Google blog](https://blog.google/products-and-platforms/products/search/search-io-2026/)).
- **Preferred Sources** now badge favourite sites inside AI Overviews and AI Mode (May 27, 2026).

**What studies show**
- **Top-10 overlap is falling:** 38% of AI Overview citations ranked in the top 10 for the same query in 2026, down from 76% in July 2025 (Ahrefs, 863K keywords / 4M AIO URLs; Ahrefs says better citation detection explains part of the drop). BrightEdge's separate estimate is ~17% ([Ahrefs](https://ahrefs.com/blog/ai-overview-citations-top-10/); [SEJ](https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/)). Ranking helps but is neither necessary nor sufficient.
- **YouTube is the most-cited domain in AI Overviews**, up 34% in six months (Ahrefs, early 2026, via [SEJ](https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/)). Surfer (46M citations, May 2026) put YouTube at about 23.3% of AIO citations (secondary summary).
- **Big-brand bias:** Ahrefs reports Google's AI surfaces appear more biased toward big brands than ChatGPT and Perplexity ([Ahrefs](https://ahrefs.com/blog/branded-web-mentions-visibility-ai-search/)).
- **Least freshness-sensitive** engine (Ahrefs 2025).
- **When AI Overviews appear** (Seer Interactive, Apr 24, 2026; 53 brands, 5.47M queries): "X vs Y" comparison queries **95.4%** of the time, "best of" 81.3%, price/cost 83.4%; only 36% of informational, 8% of commercial and 5% of transactional queries ([Seer](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update); read by the fact-check).
- **Self-ranking risk:** Lily Ray observed B2B/SaaS sites that rank themselves #1 in "best X" lists losing 29–49% of Google visibility in Jan–Feb 2026, and found companies whose own list was cited in an AI Overview were left out of the recommendation **69%** of the time (June 17, 2026). Google has not confirmed a targeted update ([Lily Ray](https://lilyraynyc.substack.com/p/is-google-finally-cracking-down-on); [Lily Ray](https://lilyraynyc.substack.com/p/why-calling-yourself-the-best-could)).

**What it means for Quotr**
- Not tested yet. Add Search Console's Generative AI report to the monthly KPIs to see which Quotr pages already get AI impressions ([[KPIs and dashboard]]).
- Comparison queries almost always trigger an AI Overview, so the 5–8 head-to-head pages the report recommends keeping must be accurate, dated and balanced. Self-ranked "best X" lists carry risk here (see [[Myths and risks]]).
- YouTube is where Google's AI features look most. Perplexity never cited YouTube in any of Quotr's 45 test runs, so trade-by-trade videos are mainly a Google-side bet ([[Quotr GEO AEO strategy audit|report]]).
- Classic Google SEO (indexing, rankings, no stale pages) remains the base layer.

### 3.3 Google AI Mode

**At a glance**

| Item | Detail |
|---|---|
| Index | Google Search index (Googlebot); same eligibility rules as AI Overviews |
| Model | Gemini 3.5 Flash became the default in AI Mode and the Gemini app on May 19, 2026 (I/O coverage, e.g. [MarkTechPost](https://www.marktechpost.com/2026/05/20/google-introduces-gemini-3-5-flash-at-i-o-2026-a-faster-and-cheaper-model-for-ai-agents-and-coding/)) |
| Scale | 1 billion+ monthly users (Google, May 2026) |
| Owner reporting | Same Search Console Generative AI report |
| Clicks | The heaviest click-reducer of any Google surface (see below) |

**Officially known**
- A chat-style Google Search that uses query fan-out, with multi-turn follow-ups; since I/O 2026 it is joined to AI Overviews. Google also announced background "information agents" that monitor the web and send updates with links ([Google blog](https://blog.google/products-and-platforms/products/search/search-io-2026/); [[verification_geo_evidence|verification M2]]).
- Same eligibility rules and controls as AI Overviews (section 2).

**What studies show**
- **First randomized experiment** (arXiv 2608.18352, Aug 18, 2026; U. Pennsylvania and Northeastern; ~1,100 Google users, 956 completed): putting people into AI Mode cut external click-through by **18.8 percentage points**; neither AI Mode nor AI Overviews improved perceived usefulness or trust. Preprint, not yet peer-reviewed ([arXiv](https://arxiv.org/pdf/2608.18352v1)).
- Semrush (vendor; 69M US desktop sessions, May–July 2025): 93% of AI Mode sessions ended with no external click. Label this "mid-2025" ([Semrush](https://www.semrush.com/blog/google-ai-mode-seo-impact/)).
- **SaaS sources are social-heavy in AI Mode:** in Aleyda Solis's Aug 2026 study, social/community sources reached **74.6%** of SaaS top-cited sources in AI Mode; YouTube was the largest SaaS source domain overall, and Reddit appeared in all 15 SaaS panels ([Aleyda Solis](https://www.aleydasolis.com/en/ai-search/ai-search-citations/); read by the fact-check). Her separate SaaS article says AI Mode favours deeper content (guides, documentation, templates, integrations) plus video and creator content.
- **LinkedIn:** ChatGPT Search and AI Mode more often cite individual creators (59%) than company pages (Semrush, 325K prompts, Jan–Feb 2026; [Semrush](https://www.semrush.com/blog/linkedin-ai-visibility-study/); not re-checked).
- AI Mode queries are about 3x longer than classic search (Indig, H1 2026; not re-checked).

**What it means for Quotr**
- In AI Mode, being **named in the conversation** matters more than a single link, because many users never click.
- Founder LinkedIn articles, YouTube and honest community answers (r/estimators, Facebook estimator groups) are the channels AI Mode leans on for SaaS.
- Deeper resources (templates, calculators, integration pages) fit what AI Mode cites for SaaS. Quotr has an ROI calculator but no trade calculators or templates yet ([[Website audit]]).

### 3.4 Perplexity

**At a glance**

| Item | Detail |
|---|---|
| Index | Own index (PerplexityBot) plus search partners |
| Crawlers | PerplexityBot (index), Perplexity-User (live fetch) |
| Citations | Shows numbered sources on nearly every answer |
| Owner reporting | None first-party. Note: GA4's new "AI Assistant" channel does **not** include Perplexity, so add a custom rule ([[verification_geo_evidence\|verification claim #7]]) |
| Agentic browser | Comet had 48.12% of AI-agent traffic in HUMAN Security's April 2026 data (vendor) ([HUMAN](https://www.humansecurity.com/learn/blog/state-of-agentic-traffic-april-26/)) |

**Officially known**
- Crawler rules as in section 2 ([Perplexity docs](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)). Perplexity says PerplexityBot is not used for training.
- No first-party Perplexity documentation on how sources are ranked was verified. Secondary summaries say it weighs relevance, authority, recency and how directly a passage supports a claim ([LLM Pulse](https://llmpulse.ai/blog/how-perplexity-works/); [SearchScore](https://searchscore.io/guides/how-perplexity-cites-sources/)).

**What studies show**
- **Quotr's own tests (Perplexity Sonar API, Sept 25, 2026):** Capterra and G2 each fed 9 of 32 unbranded answers; "best of" lists came next (Construction Coverage 7, ConstructConnect's 2026 guide 7, The Digital Project Manager 6; ConstructConnect is itself a vendor); quotr.ai appeared in 6 source lists, the same as reddit.com; YouTube was never cited in 45 runs ([[Citation sources map]]; [[AI visibility baseline]]).
- **Perplexity discounts self-ranking:** it did not accept Quotr's "#1 Quotr.ai" lists, and it called some of Quotr's claims "vendor assertions". A plain search summary repeated them word for word ([[GEO tactics already used]]).
- HubSpot (vendor, June 2026): Perplexity favours product listing/landing pages (84% citation rate) ([HubSpot](https://blog.hubspot.com/marketing/content-format-types-that-earn-citations); directional).
- Perplexity cites LinkedIn **company pages** more often (59%) than creators (Semrush; not re-checked).
- Perplexity had the lowest monthly citation drift of the engines Profound tracked (40.5%). Historic Reddit dominance (46.7% of Perplexity's top-10 share, Aug 2024–Jun 2025, Profound) is **outdated**; use it as history only.

**What it means for Quotr**
- This is the one engine where Quotr has data: **named in 1 of 32 unbranded questions (about 3%)**, while STACK, PlanSwift and Buildxact were each named in 10. The fastest ways in are the sources Perplexity already reads: G2/Capterra reviews (one program now feeds G2, Capterra, GetApp and Software Advice), the F6S "AI-Assisted Takeoff" category page, and the editorial lists ([[Quotr GEO AEO strategy audit|report]]).
- Perplexity reads Quotr's blog closely, so stale prices and errors there go straight into answers. Fix them first.
- Perplexity cited a staging copy (test.quotr.io). Keep staging hosts out of indexes.

### 3.5 Gemini (the app)

**At a glance**

| Item | Detail |
|---|---|
| Index | Google Search, through "Grounding with Google Search" |
| Crawlers / controls | Googlebot; **Google-Extended** controls use for Gemini training and for grounding in Gemini apps |
| Model | Gemini 3.5 Flash default since May 19, 2026 |
| Scale | Gemini had more than 25% of AI-assistant web traffic by May 2026 (Similarweb; not re-checked). A "950M monthly users" figure circulates but was **not verified** against Alphabet |

**Officially known**
- With Search grounding, the model decides whether a Google Search would improve the answer, generates one or more search queries, reads results and writes a response with sources ([Gemini API docs](https://ai.google.dev/gemini-api/docs/google-search)).
- Gemini may show a Sources button or inline links, but not on every response. Its **"double-check"** feature shows content Search found to be similar to or different from a statement; those links are not necessarily what Gemini used (Google help, summarised by [Trakkr](https://trakkr.ai/article/check-if-gemini-cites-my-site); secondary).
- Google-Extended does not affect Google Search, but it does govern grounding in the Gemini apps ([SEJ](https://www.searchenginejournal.com/google-updates-gemini-vertex-ai-user-agent-documentation/545409/)).

**What studies show**
- Gemini cites sources in 82% of responses, about 8 sources each (Muck Rack, May 2026).
- Gemini had the lowest 28-day citation retention (11%) in the Digital Authority Partners study.
- Gemini's share of AI-search activity rose to about 30% in H1 2026 (Indig; not re-checked).

**What it means for Quotr**
- Keep Google-Extended allowed. Blocking it would not help Quotr and could remove it from Gemini app answers.
- Because Gemini uses Google Search, the Google work (indexing, fixing stale pages, YouTube) serves Gemini too.
- Gemini's citations churn fastest, so track it monthly and do not over-react to one month.

### 3.6 Claude (Anthropic)

**At a glance**

| Item | Detail |
|---|---|
| Index | Brave Search (only search provider on Anthropic's subprocessor list); secondary reports say turbopuffer was added by Sept 2026 |
| Crawlers | ClaudeBot (training), Claude-SearchBot (search index), Claude-User (live fetch); all follow robots.txt and Crawl-delay |
| Citations | Cites in about 55% of responses, but about 13 sources each (Muck Rack, May 2026) |
| Tooling | Anthropic released new web-search tool versions in 2026 (`web_search_20260209`, `web_search_20260318`) ([Claude docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)) |

**Officially known**
- The three crawlers and what blocking each does (section 2).
- Web search can be turned on in Claude's apps ([Claude support](https://support.claude.com/en/articles/10684626-enable-and-use-web-search)).

**What studies show**
- One small independent test found **86.7%** overlap between Claude's cited results and Brave's top organic results ([Ryan Doser](https://ryandoser.com/what-search-engine-does-claude-use/); blogger sample, not re-checked).
- Claude is the fastest-growing AI assistant by traffic (Similarweb) and reached about 10% of AI-search activity in H1 2026 (Indig). Neither was re-checked.
- **Caution on Claude as a B2B referral source:** an aggregator claims Claude sends 18.5% of B2B AI referrals, but its primary source was not found; Conductor's 2025 benchmark put Claude at about 2% of AI referrals ([[verification_geo_evidence|verification H17]]).
- The Claude Chrome extension had 17.33% of AI-agent traffic in April 2026 (HUMAN Security; vendor).

**What it means for Quotr**
- Check that Quotr's key pages appear in **Brave Search** (search brave.com for "Quotr.ai", "AI takeoff software" and the pricing page). This is cheap hygiene.
- Claude shows many sources per answer, so third-party lists and review pages that mention Quotr help here too.
- Do not call Claude a major Quotr traffic source until Quotr's GA4 shows it.

### 3.7 Microsoft Copilot (Bing)

**At a glance**

| Item | Detail |
|---|---|
| Index | Bing (Bingbot) |
| Controls | robots.txt for Bingbot; `NOCACHE` / `NOARCHIVE` meta tags for AI-answer use |
| Owner reporting | **Bing Webmaster Tools AI Performance report** (public preview since Feb 10, 2026): how often a site's URLs are cited in Copilot, Bing AI summaries and some partner integrations, plus the "grounding queries" Copilot used ([Bing blog](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)) |
| Fast updates | IndexNow |

**Officially known**
- **Microsoft's Oct 2025 guidance** for inclusion in AI answers: descriptive H1–H3 headings that mirror questions; short, single-idea sections; schema (FAQ, HowTo, Product, Review); direct factual language; alt text and clean HTML; fresh content consistent with authoritative sources ([Microsoft Advertising](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers)).
- **Microsoft's May 6, 2026 post** "Evolving role of the index: From ranking pages to supporting answers" says grounding uses the same crawlers and quality signals as search but adds a layer that checks facts, attribution and confidence: whether meaning survives chunking, the source is clearly identified, the information is fresh enough, and important facts are retrievable ([Bing Search blog](https://blogs.bing.com/search/May-2026/Evolving-role-of-the-index-From-ranking-pages-to-supporting-answers); via [Search Engine Land](https://searchengineland.com/microsoft-ai-answers-index-476691)). Read this newer post in full before quoting Microsoft's older advice ([[verification_geo_evidence|verification O12]]).

**What studies show**
- Copilot citations drift about 53.4% month to month (Profound; vendor).
- Only 12% of links cited by ChatGPT, Gemini and Copilot were in Google's top 10 (Ahrefs), so Bing rankings can matter on their own.

**What it means for Quotr**
- Set up **Bing Webmaster Tools** now: submit all three sitemaps (including the blog sitemap robots.txt currently omits), turn on IndexNow, and watch the AI Performance report for citations and grounding queries ([[Quotr GEO AEO strategy audit|report, 30-day plan]]).
- Microsoft is the one engine that openly recommends schema. Fixing Quotr's conflicting Organization schema is cheap hygiene that may help here ([[Schema markup kit]]).
- Copilot's "fresh and consistent with authoritative sources" test is exactly where Quotr's conflicting facts (price, HQ, factory count) hurt.

---

## 4. Side-by-side summary

| | ChatGPT | AI Overviews | AI Mode | Perplexity | Gemini app | Claude | Copilot |
|---|---|---|---|---|---|---|---|
| Main index | Own crawl + third parties | Google | Google | Own + partners | Google | Brave (+ possibly others) | Bing |
| Search crawler to allow | OAI-SearchBot | Googlebot | Googlebot | PerplexityBot | Googlebot + Google-Extended | Claude-SearchBot | Bingbot |
| Freshness preference | Strongest | Weakest | Not measured separately | Lists newer sources first (Ahrefs) | Not measured separately | Not measured | "Fresh content" recommended |
| Source mix leans toward | Written sources, Wikipedia, homepages, listicles | YouTube, big brands | Social/community, video, creators | Review sites, listicles, vendor pages (Quotr tests) | Google results | Many sources per answer | Bing results; structured pages |
| First-party reporting for site owners | None | Search Console (impressions only) | Search Console (impressions only) | None | None | None | Bing AI Performance (citations + grounding queries) |
| Tested for Quotr? | No | No | No | **Yes (1 of 32 unbranded)** | No | No | No |

---

## 5. What this means for Quotr (checklist)

1. **Keep all AI crawlers allowed.** Confirm in Cloudflare that "Block AI bots" is off and that AI search bots get normal 200 responses (TO CONFIRM with Quotr). See [[Website audit]].
2. **Be findable in three indexes:** Google (Search Console), Bing (Bing Webmaster Tools, IndexNow) and Brave (spot-check). Add the blog sitemap to robots.txt and use real lastmod dates.
3. **Fix the facts engines retrieve.** Old prices on about 13 URLs and llms.txt, conflicting HQ, funding and factory counts. One fact sheet: [[Entity fact sheet]].
4. **Attach the name to the fact** so retrieval turns into mentions ([[GEO writing style guide]]).
5. **Match sub-questions, don't multiply pages.** Precise titles and headings; no near-duplicate variation pages.
6. **Earn presence where each engine looks:** review sites and editorial lists (Perplexity, ChatGPT), YouTube (AI Overviews, AI Mode), LinkedIn and communities (AI Mode), press (all). See [[Citation sources map]] and [[Off-site earned media plan]].
7. **Measure per engine, monthly, with two runs for each headline prompt,** plus Search Console and Bing AI reports ([[Tracking set]]; [[Tracking setup]]).
8. **Do not opt out** of Google's AI features, and do not block Google-Extended.

---

## Open questions and gaps

- Which search providers ChatGPT uses is not confirmed by OpenAI.
- No first-party Perplexity or Gemini-app documentation on source ranking was verified.
- No published study covers how any engine answers **takeoff or estimating** software questions specifically ([[quotr_ai_visibility_tests|quotr_ai_visibility_tests.md §6]]).
- Whether Cloudflare lets every AI crawler through, and what status codes they receive, needs Quotr's Cloudflare dashboard or server logs (TO CONFIRM with Quotr).
- Microsoft's May 2026 grounding post and Google's May 2026 guide were read only through summaries in this research.

---

## Related pages

- [[Signals that matter]] — the evidence table of what gets brands cited and named
- [[Myths and risks]] — llms.txt, hidden text, self-ranking lists and other traps
- [[Traffic and funnel impact]] — what AI answers do to clicks and top-of-funnel reach
- [[GEO glossary]] — every term on this page in plain English
- [[Website audit]] — Quotr's robots.txt, sitemaps and schema today
- [[AI visibility baseline]] — the Perplexity test results
- [[Citation sources map]] — the exact third-party pages engines cite in Quotr's category
- [[Tracking set]] — the monthly multi-engine test
- [[Tracking setup]] — Search Console, Bing and GA4 setup
