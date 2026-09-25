# GEO Glossary (AI Search, SEO and Measurement Terms)

**What this page is for:** Plain-English definitions of the GEO, AEO, SEO and AI-search terms used across this knowledge brain, each with a note on why it matters for Quotr.ai. Construction and estimating terms (takeoff, bid leveling, DDP and so on) are in [../04-prompt-library/construction-glossary.md](../04-prompt-library/construction-glossary.md).

**Last updated:** 2026-09-25

**Sources:** Definitions are written from the other pages in this folder and their sources: research notes [geo_ai_citation_signals_2026.md](<../../research_notes/Quotr GEO AEO strategy audit/geo_ai_citation_signals_2026.md>), [geo_content_playbook_b2b.md](<../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md>) and the fact-check [verification_geo_evidence.md](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>); the report [Quotr GEO AEO strategy audit.md](<../../reports/Quotr GEO AEO strategy audit.md>); Quotr-specific notes from [../02-current-state/website-audit.md](../02-current-state/website-audit.md) and [../02-current-state/geo-tactics-already-used.md](../02-current-state/geo-tactics-already-used.md). Platform facts (crawler names, dates, controls) are sourced on [how-ai-engines-choose-sources.md](how-ai-engines-choose-sources.md); a few are linked here directly.

**How to use:** terms are grouped by topic, then listed A–Z within each group. Use your browser's find (Ctrl+F / Cmd+F) to jump to a term.

---

## A. The basics

| Term | Plain-English meaning | Why it matters / Quotr example |
|---|---|---|
| **AEO (answer engine optimization)** | Making content easy for "answer engines" (AI chatbots, AI search, voice assistants) to find, trust and use in a direct answer. Used almost interchangeably with GEO. | Same goal as GEO: get Quotr named in answers. |
| **AI agent / agentic browser** | AI software that browses websites and takes actions for a user (compare products, fill forms). Examples: Perplexity Comet, ChatGPT Atlas, the Claude Chrome extension. | Agent traffic is still mostly media, ecommerce and travel; a watch item for Quotr. Clean pricing and product pages help agents too. |
| **AI answer engine** | A product that replies to a question with a written answer instead of (or on top of) a list of links: ChatGPT, Perplexity, Gemini, Claude, Copilot, Google AI Overviews and AI Mode. | The "places" where Quotr needs to be named. |
| **AI search** | Search where an AI writes the answer, usually after running web searches and citing sources. | Google AI Mode alone passed 1 billion monthly users (Google, May 2026). |
| **AI SEO / LLMO / LLM SEO** | Other names for GEO. LLMO = "large language model optimization". | Same thing; don't let naming debates distract. |
| **Chatbot / AI assistant** | A conversational AI product (ChatGPT, Gemini app, Claude, Copilot). | G2's survey (vendor): 51% of B2B software buyers start research in one. |
| **GEO (generative engine optimization)** | Getting a brand found, mentioned, cited and recommended inside AI-generated answers. The term comes from a 2023/2024 research paper ("GEO: Generative Engine Optimization"). | The report's summary: "GEO is mostly good SEO, plus getting other people to talk about you." |
| **Generative AI** | AI that creates text, images or video (as opposed to only sorting or ranking). | The engine behind every AI answer. |
| **Hallucination** | When an AI states something false with confidence. | In Quotr's tests, Perplexity presented the unrelated Quotr Pro app's "4.7/5" rating as Quotr.ai's (a mix-up of two brands rather than an invention, but the effect on buyers is the same). |
| **Knowledge cutoff (training cutoff)** | The date after which a model has no built-in knowledge; it must search to know newer facts. | Older models may still describe "Quotr.io" and old products. |
| **LLM (large language model)** | The AI model inside a chatbot, trained on huge amounts of text to predict and write language (GPT, Gemini, Claude models). | Understanding how LLMs pick sources explains what GEO can and cannot do. |
| **Prompt** | The question or instruction a user types into an AI tool. | Quotr's buyer prompts are listed in [../04-prompt-library/prompt-library.md](../04-prompt-library/prompt-library.md). |
| **SEO (search engine optimization)** | Making pages rank well in normal search results (Google, Bing). | Still the base layer: Google says AI features use the same index and eligibility rules. |
| **Training data** | The huge body of text a model learned from before release. | Consistent descriptions of Quotr across many sites slowly shape what models "remember". |

---

## B. How AI answers are built

| Term | Plain-English meaning | Why it matters / Quotr example |
|---|---|---|
| **Chunk / chunking** | Splitting a page into smaller pieces that an AI can retrieve separately. | Google (May 2026) says you do **not** need to chunk pages for AI; write clear, self-contained sections instead. |
| **Citation** | The AI shows a page as a source (footnote number, link, card). | A quotr.ai page appeared in the source list of 6 of 32 unbranded Perplexity answers, and was used in the answer text in 4 of them. |
| **Citation drift / volatility** | How much the list of cited sources changes over time for the same question. | Profound (vendor) measured 40–60% month-to-month change; track monthly, not once. |
| **Consensus gap** | Different AI engines citing different sources for the same question. | Indig (H1 2026, not re-checked): 91% of citations appear in only one engine. Test several engines. |
| **Embedding / semantic similarity** | Turning text into numbers so a system can measure how close in meaning two texts are, even with different words. | Why matching the *meaning* of buyer sub-questions matters more than repeating exact keywords. |
| **Freshness / recency** | How new or recently updated a page is. | ChatGPT prefers fresher pages; Google AI Overviews care least (Ahrefs, 2025). Update when facts change, not just the date. |
| **Grounding** | Tying an AI answer to real, retrieved sources so it states supportable facts. | Microsoft (May 2026): grounding wants "supportable facts with clear sourcing". Consistent, sourced facts help Quotr. |
| **Grounding query** | The internal search phrase an AI generates to find sources. | Bing Webmaster Tools' AI Performance report shows the grounding queries that led to your pages. |
| **Live retrieval** | The AI runs a web search during the conversation and reads pages. | Fixed pages can influence answers within days or weeks once re-crawled. |
| **Mention** | The AI says your brand name in the answer text. | Different from a citation: Perplexity used Quotr's prices but wrote "one outsourced estimating service". |
| **Parametric knowledge** | What a model "knows" from training, without searching. | ChatGPT answered roughly two-thirds of prompts this way in 2025–early 2026 (studies not re-checked). |
| **Passage retrieval** | Pulling the specific paragraph or section that answers a question, not the whole page. | 44.2% of ChatGPT citations came from the first 30% of a page (Indig, Feb 2026; correlation). |
| **Personalization** | Answers change based on a user's history, location or chosen preferences. | Use clean sessions when tracking, so months compare fairly. |
| **Query fan-out** | The AI splits one question into many smaller searches and combines the results. | Google documents it for AI Overviews and AI Mode. Match precise sub-questions; don't make a page per variation. |
| **RAG (retrieval-augmented generation)** | The general method of fetching documents first and then having the model write an answer from them. | The technical name for how AI search works. |
| **Recommendation** | The AI suggests a brand as a good choice (often ranked first). | In one small AI Mode user study, 74% picked the first brand named (Indig). |
| **Source list** | The set of pages an AI shows it used for an answer. | Where review sites, lists and Reddit appear for Quotr's category. |
| **Sub-query** | One of the smaller searches created by query fan-out. | Page titles that match narrow sub-queries were cited more (Ahrefs, 1.4M prompts; vendor). |

---

## C. AI products and features

| Term | Plain-English meaning | Why it matters / Quotr example |
|---|---|---|
| **AI Mode** | Google's chat-style search, with follow-up questions. Passed 1B monthly users (Google, May 2026); default model Gemini 3.5 Flash since May 19, 2026. | The biggest click-reducer: −18.8 pp external clicks in a randomized experiment (Aug 2026 preprint). |
| **AI Overview (AIO)** | The AI summary at the top of some Google results pages. 2.5B monthly users (Google, May 2026). | Shows for 95% of "X vs Y" searches (Seer). Quotr's comparison pages feed it. |
| **Bing** | Microsoft's search engine and index. | Powers Copilot and reportedly part of ChatGPT (not confirmed). Quotr should use Bing Webmaster Tools. |
| **Branded links (ChatGPT)** | Since May 7, 2026, ChatGPT links brand names in answers straight to brand homepages. | Profound (vendor): B2B software referrals up >200%. Each "Quotr.ai" mention can become a visit. |
| **Brave Search** | An independent search engine with its own index. | Claude's web search uses it (Brave is Anthropic's listed search provider). |
| **ChatGPT ads** | Labelled sponsored placements next to ChatGPT answers (US test from Feb 9, 2026; sponsored agents tested Sept 2026). | OpenAI says ads do **not** influence answers. A separate paid channel. |
| **ChatGPT search** | ChatGPT's web-search mode that shows cited sources. | Quotr could not be tested there yet; first job of the baseline. |
| **Claude** | Anthropic's AI assistant; can search the web. | Cites in ~55% of responses but ~13 sources each (Muck Rack, May 2026). |
| **Copilot (Microsoft Copilot)** | Microsoft's AI assistant, grounded in Bing. | The only engine with a citation report for site owners (Bing AI Performance). |
| **Gemini** | Google's AI model family and its chatbot app. | Grounds answers in Google Search; Google-Extended governs its use of content. |
| **Perplexity** | An AI answer engine that shows numbered sources on nearly every answer. | The one engine tested for Quotr: named in 1 of 32 unbranded questions. |
| **Preferred Sources** | A Google feature (in AI Overviews and AI Mode since May 27, 2026) letting users pick favourite sites, which get a badge. | Google says people are twice as likely to click a Preferred Source. Favours brands with loyal audiences. |
| **Sonar** | Perplexity's developer (API) version, used for Quotr's September 2026 tests. | May differ slightly from the consumer app. |

---

## D. Crawlers and access

| Term | Plain-English meaning | Why it matters / Quotr example |
|---|---|---|
| **AI Labyrinth (Cloudflare)** | A Cloudflare feature that hides a trap link leading bots that ignore crawl rules into decoy pages. | On for quotr.ai. It should not affect well-behaved AI crawlers. |
| **Allow / Disallow** | robots.txt rules that permit or forbid a crawler from paths on a site. | quotr.ai has one rule: allow everything. |
| **Applebot-Extended** | Robots.txt token controlling use of content for Apple's AI training. | Allowed on quotr.ai. |
| **Bingbot** | Microsoft's crawler for the Bing index. | Blocking it would remove Quotr from Bing and Copilot. |
| **CCBot** | Common Crawl's crawler; its open dataset is used to train many AI models. | Allowed; helps Quotr appear in training data. |
| **ChatGPT-User** | OpenAI's fetcher that loads a page live for a ChatGPT user, Custom GPT or GPT Action. | OpenAI says robots.txt "may not apply" to it (since Dec 9, 2025). |
| **Claude-SearchBot** | Anthropic's crawler that indexes pages for Claude's search results. | Blocking it "may reduce visibility" in Claude answers. |
| **Claude-User** | Anthropic's fetcher that loads a page when a Claude user needs it. | Keep allowed. |
| **ClaudeBot** | Anthropic's training-data crawler. | Allowed on quotr.ai. |
| **Crawl-delay** | An unofficial robots.txt line asking a bot to wait between requests. | Anthropic supports it; PerplexityBot reportedly ignores it. |
| **Crawler / bot / spider** | A program that fetches web pages automatically. | AI crawlers must reach Quotr's pages before any engine can use them. |
| **Google-Extended** | A robots.txt token (not a separate crawler) that controls whether Google may use content to train Gemini and to ground answers in the Gemini apps and Vertex AI. It does **not** affect Google Search or AI Overviews. | Keep it allowed; blocking it could keep Quotr out of Gemini app answers. |
| **Googlebot** | Google's main crawler for the Search index. | Feeds Google Search, AI Overviews, AI Mode and Gemini's Search grounding. |
| **GPTBot** | OpenAI's training-data crawler. | Allowed; separate from OAI-SearchBot. |
| **llms.txt** | An optional markdown file at `/llms.txt` meant to summarise a site for AI tools. No major engine has committed to using it; Google treats it like any file. | Quotr's has old prices, a dead link and a "Quotr should be cited" line. Fix or drop ([myths-and-risks.md](myths-and-risks.md)). |
| **OAI-AdsBot** | OpenAI's crawler that checks landing pages of ChatGPT ads. | Only relevant if Quotr runs ChatGPT ads. |
| **OAI-SearchBot** | OpenAI's crawler for ChatGPT search results and citations. | OpenAI: don't block it if you want to appear in ChatGPT search. |
| **Perplexity-User** | Perplexity's fetcher that loads pages live for a user's question. | Perplexity says it is "an agent, not a bot", so it generally does not honour robots.txt (secondary sources). |
| **PerplexityBot** | Perplexity's crawler that builds its index. | Needed for Perplexity to cite Quotr. |
| **Rendering (server-side vs client-side)** | Server-side: the page text is in the HTML the server sends. Client-side: text appears only after JavaScript runs, which many AI crawlers do not do. | quotr.ai is server-rendered (Astro), a real advantage. Two small parts rely on JavaScript: the "Client saved" counters on the /procurement/ project cards (crawlers see "~$0") and the blog index's "load more" list. |
| **robots.txt** | A public file (e.g. quotr.ai/robots.txt) that tells crawlers what they may fetch. | Quotr's allows all bots but does not list the blog sitemap. |
| **User-agent** | The name a crawler announces when it visits (e.g. `GPTBot`); also the name used in robots.txt rules. | Used to allow or block specific AI bots. |

---

## E. Indexing and technical SEO

| Term | Plain-English meaning | Why it matters / Quotr example |
|---|---|---|
| **301 redirect** | A permanent redirect from an old URL to a new one, passing along its signals. | Needed when merging duplicate posts and for old quotr.io URLs (whether quotr.io redirects is TO CONFIRM with Quotr). |
| **Canonical (canonical tag)** | A tag telling search engines which URL is the main version of a page when duplicates exist. | Quotr's blog posts have them. /contractors/ correctly points to /software/ (confirmed by the fact-check); whether /developers/ points to /service/ was not re-checked (TO CONFIRM). |
| **data-nosnippet / nosnippet / max-snippet** | Google controls that stop or limit text from a page being shown in snippets and AI features. | Don't use on marketing pages; they reduce AI visibility. |
| **Index / indexing** | The stored copy of pages a search engine keeps; "indexed" means a page is in it. | Google's only requirement for AI features: indexed and snippet-eligible. |
| **IndexNow** | A protocol to instantly tell Bing (and Yandex, Naver, Seznam, Yep) that a URL changed. Google does not use it. | Use after fixing the ~13 Quotr URLs with old prices, so Bing and Copilot re-read them fast. |
| **lastmod** | The "last modified" date for each URL in a sitemap. | Quotr's main sitemap says every page changed "today", which makes the signal meaningless. |
| **noindex** | A tag telling search engines not to keep a page in their index. | Use on staging copies like test.quotr.io, which Perplexity still cited. |
| **NOCACHE / NOARCHIVE** | Bing meta tags that limit (NOCACHE) or block (NOARCHIVE) use of a page in Copilot/Bing AI answers. | Don't use on Quotr's public pages. |
| **Search generative AI control** | Google Search Console's property-level opt-out from AI Overviews, AI Mode and Discover's generative features (announced June 3, 2026; worldwide Aug 31, 2026). | Quotr should **not** opt out. |
| **SERP (search engine results page)** | The page of results a search engine shows. | Where AI Overviews appear. |
| **Sitemap** | An XML list of a site's URLs (with dates) that helps crawlers find pages. | Quotr has three; the 96-post blog sitemap is missing from robots.txt. |
| **Sitemap index** | A sitemap that lists other sitemaps. | A clean fix for Quotr's three separate sitemaps. |
| **Snippet** | The short text a search engine shows under a result; AI features need a page to be snippet-eligible. | Don't block snippets on pages Quotr wants cited. |
| **Staging site** | A test copy of a website. It should never be indexed. | test.quotr.io was indexed and cited for "Quotr.ai pricing". |

---

## F. Entities and structured data

| Term | Plain-English meaning | Why it matters / Quotr example |
|---|---|---|
| **@id** | In JSON-LD, a unique identifier for a thing (e.g. `https://quotr.ai/#organization`) so machines can merge facts about it. | Quotr uses one @id for two different Organization descriptions (legal names "FLOZ Inc" and "Quotr.ai"). Fix. |
| **alternateName** | A schema property for other names of the same entity. | Quotr's lists "Quotr.io" and "Quotr by FLOZ Inc", which correctly ties old mentions to the brand. |
| **Entity** | A distinct "thing" machines can identify: a company, product, person or place. | AI must see Quotr.ai as one clear entity, separate from Quotr Pro, quotrhq.com and others. |
| **Entity consistency** | The same core facts (name, price, HQ, founders, funding) everywhere the entity appears. | Quotr's pages and profiles disagree on price, HQ, funding, factory count and more. One fact sheet fixes it: [../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md). |
| **Entity disambiguation** | Making clear which of several same-named things you mean. | Quotr's /disambiguation/ page ("Quotr.ai is not Quotation") helps "What is Quotr.ai?" answers. |
| **FAQPage** | Schema type marking up a list of questions and answers. | Only /disambiguation/ has it among checked pages, though many pages show FAQs. |
| **JSON-LD** | The most common format for adding schema to a page: a block of code in the page's HTML. | How Quotr's schema is written. |
| **Knowledge graph** | A search engine's database of entities and how they connect (Google's Knowledge Graph). | Where consistent facts about Quotr end up; source of Knowledge Panels. |
| **Knowledge Panel** | The fact box about an entity that Google sometimes shows beside results. | Whether Quotr has one was not checked (TO CONFIRM). Consistent profiles and a Wikidata entry are commonly recommended groundwork (practitioner opinion, not proven). |
| **Organization schema** | Schema describing a company: name, legal name, logo, founders, sameAs profiles. | Needs one consistent version on every Quotr page. |
| **Rich results** | Enhanced search listings (stars, FAQs, prices) that schema can make a page eligible for. | Google's main reason to use schema; not an AI-citation lever. |
| **sameAs** | A schema property listing the official profiles of an entity (LinkedIn, YouTube, Crunchbase, G2). | Quotr's lists mix old "quotr_io" and new "quotr_ai" handles. Use one set. |
| **Schema / schema.org / structured data** | A shared vocabulary of labels that describe page facts to machines (company, product, price, FAQ, author). | Google: no special schema for AI; Microsoft recommends it. Treat as hygiene: [../06-playbooks/schema-markup-kit.md](../06-playbooks/schema-markup-kit.md). |
| **SoftwareApplication / Offer** | Schema types for a software product and its prices. | Belongs on /software/ and /pricing/ (Lite $79.90, Plus $299.90 per seat per month). |
| **Wikidata** | A free, public database of facts about entities, used by many systems. | A low-cost hygiene item for Quotr, not a proven lever. |
| **Wikipedia notability** | Wikipedia's rule that a topic needs significant independent, reliable coverage to have an article. | Quotr has no independent press yet, so a Wikipedia article is premature. |

---

## G. Content, quality and trust

| Term | Plain-English meaning | Why it matters / Quotr example |
|---|---|---|
| **Alternatives page** | A page listing substitutes for a named product ("Togal.AI alternatives"). | Quotr has 5; they are used as fact sources but rarely lead AI to recommend Quotr. |
| **Answer-first** | Putting the direct answer in the first sentences of a page or section. | Quotr's "Quick Answer" blocks do this well. Good for readers; not a guaranteed citation lever. |
| **Click resilience** | Whether people still need to visit a page after reading an AI answer (to use a tool, check live data, act). | Calculators, datasets and templates are click-resilient; generic definitions are not. |
| **Cloaking** | Showing search engines different content from what people see. A Google spam-policy violation. | Never do it. |
| **Comparison page ("X vs Y")** | A page comparing two products head to head. | 95% of "X vs Y" searches show an AI Overview (Seer). Keep 5–8 honest ones. |
| **Content refresh** | Updating an existing page with real new facts, examples or data. | Update when facts change; date-only "refreshes" can backfire. |
| **Doorway page** | Thin pages made mainly to rank for variations of a search and funnel users elsewhere. | Quotr's thinnest trade pages risk looking like this. |
| **E-E-A-T** | Google's quality idea: Experience, Expertise, Authoritativeness, Trustworthiness. | No study links it directly to AI citations, but named expert authors build buyer trust. Replace "By quotr.ai" bylines. |
| **Earned media** | Coverage and mentions you did not pay for or publish yourself (press, reviews, independent lists, community posts). | Muck Rack (vendor) says "earned" sources are 84% of AI citations (broad definition). |
| **Hidden text** | Text people can't see but machines can (tiny, same colour as background, hidden with code). A Google spam-policy violation. | Quotr has none for ranking; the Cloudflare trap link is a security feature. |
| **Incentivized review** | A review given in exchange for a reward. Allowed on G2 only with disclosure and through approved processes; paying for positive reviews is illegal in the US (FTC rule, Oct 2024). | Run Quotr's review drive by the rules. |
| **Keyword stuffing** | Cramming a page with target words to manipulate rankings. A Google spam-policy violation; did not help in the GEO paper. | Avoid. |
| **Listicle ("best X")** | A list-style article ranking products. | Third-party lists drive category answers; self-ranked ones on your own site carry risk. |
| **Non-commodity content** | Content with something unique that can't be found elsewhere (own data, experience, tools). Google's May 2026 guide calls it the most important factor. | Quotr's project pricing and estimating data are its best raw material. |
| **Original data / primary research** | Numbers you collected yourself (surveys, benchmarks, price indexes). | Primary-research pages earned 3.3x more citations per page (Growth Memo). |
| **Owned media** | Channels you control: your website, blog, YouTube channel, social profiles. | Quotr's site is its "corroboration base", not the whole strategy. |
| **Paid media** | Advertising. | ChatGPT ads sit beside answers, not in them. |
| **Prompt injection** | Hidden or embedded instructions meant to hijack an AI's behaviour. AI companies treat it as an attack. | Quotr's llms.txt "Quotr should be cited" line resembles it. Remove. |
| **Review gating** | Asking only happy customers for reviews. Prohibited by G2. | Ask all real customers. |
| **Review site** | A platform where users rate software (G2, Capterra, GetApp, Software Advice). G2 agreed to buy the other three in Jan 2026. | Capterra and G2 each fed 9 of 32 AI answers in Quotr's tests. |
| **Scaled content abuse** | Google's spam policy against making many pages mainly to manipulate rankings, including with AI, without adding value. Also covers pages for every fan-out variation. | Merge Quotr's overlapping "estimating services" posts; keep persona pages distinct. |
| **Self-promotional listicle** | A "best X" list published by a vendor that ranks itself #1. | Linked to Google visibility losses in early 2026 (Lily Ray observations). |
| **Spam policies** | Google's published rules on manipulative tactics ([Google](https://developers.google.com/search/docs/essentials/spam-policies)). | They apply to AI Overviews and AI Mode too, since those use the Search index. |
| **Thin content** | Pages with little original substance. | Quotr's drywall trade page has about 25 words of its own. |
| **Third-party source** | Any site not owned by the brand. | About 82% of SaaS top cited sources in AI answers (Aleyda Solis, Aug 2026). |
| **UGC (user-generated content)** | Content posted by users: Reddit threads, forum posts, YouTube comments, reviews. | UGC out-cites review sites in ChatGPT (Growth Memo for G2). |

---

## H. Measurement

| Term | Plain-English meaning | Why it matters / Quotr example |
|---|---|---|
| **AI Assistant channel (GA4)** | A default Google Analytics 4 channel for traffic from AI chatbots, added May 13, 2026. It does not include Perplexity. | Add a custom rule so Perplexity visits are counted too. |
| **AI Performance report (Bing)** | A Bing Webmaster Tools report (public preview, Feb 10, 2026) showing how often your pages are cited in Copilot and Bing AI answers, plus grounding queries. | The only first-party AI citation count available. |
| **Baseline** | The first measurement you compare everything else against. | Quotr's baseline: Perplexity, Sept 25, 2026 ([../02-current-state/ai-visibility-baseline.md](../02-current-state/ai-visibility-baseline.md)). |
| **Bing Webmaster Tools** | Microsoft's free dashboard for site owners (indexing, sitemaps, IndexNow, AI Performance). | Quotr should set it up in the first 30 days. |
| **Branded prompt** | A question that names the brand ("Quotr.ai pricing", "Is Quotr.ai legit?"). | Quotr was named in all 8 branded Perplexity prompts, but 5 of the 8 answers carried an error (for example the old $299.90 entry price). |
| **Citation rate** | The share of tested answers that use your pages as sources in the answer text. (If your page is only in the source list, that counts toward the "retrieval rate".) | quotr.ai: cited in 4 of 32 unbranded Perplexity answers (12.5%); in the source list of 6 of 32 (18.8%). |
| **Correlation vs causation** | Correlation: two things rise together. Causation: one causes the other. Most GEO studies show only correlation. | Read "YouTube mentions correlate 0.737" as a clue, not proof. |
| **Custom channel group (GA4)** | Your own rules for grouping traffic sources in GA4. | Where the AI regex rule goes, above Referral. |
| **GA4 (Google Analytics 4)** | Google's website analytics tool. | Needed to measure AI referral visits and conversions (Quotr's data TO CONFIRM). |
| **Generative AI performance report (Search Console)** | Search Console reports showing impressions from AI Overviews, AI Mode and Discover's generative features, by page, country and date; no clicks or queries. Worldwide since Aug 31, 2026. | First-party Google data on Quotr's AI visibility. Add to the KPI set. |
| **Google Search Console (GSC)** | Google's free dashboard for site owners (indexing, queries, clicks, now AI impressions). | Also used to request re-crawls after fixes. |
| **Mention rate** | The share of tested answers that name your brand. | Quotr: 1 of 32 unbranded Perplexity answers (about 3%). |
| **Prompt library / prompt set** | A structured list of buyer questions to target and test. | [../04-prompt-library/prompt-library.md](../04-prompt-library/prompt-library.md). |
| **Prompt tracking** | Re-running a fixed set of prompts on a schedule across engines and recording mentions, citations, position and accuracy. | Quotr's plan: monthly on five engines (Claude and Copilot quarterly), two runs for each headline prompt ([../04-prompt-library/tracking-set.md](../04-prompt-library/tracking-set.md)). |
| **Retrieval rate** | The share of tested answers that list one of your pages anywhere in their sources, whether or not the answer text uses it. | quotr.ai: 6 of 32 unbranded Perplexity answers (18.8%), level with reddit.com. |
| **Self-reported attribution** | Asking buyers how they found you (a form field) instead of relying only on analytics. | Catches AI influence that analytics miss (e.g. a buyer who later types the URL). |
| **Sentiment** | Whether an AI describes a brand positively, neutrally or negatively. | Perplexity describes some Quotr claims as "vendor assertions". |
| **Share of voice (SOV)** | Your share of all brand mentions across a prompt set. | Quotr ~0.7% vs ~6.5% each for STACK, PlanSwift and Buildxact (32 unbranded Perplexity prompts). |
| **Spearman correlation** | A statistic (from −1 to 1) showing how closely two rankings move together. Used in Ahrefs' brand studies. | A 0.7 correlation is strong but still not proof of cause. |
| **Tracking tools** | Paid tools that run prompts and report AI visibility (e.g. Otterly.AI, Peec AI, Scrunch, Profound, Semrush AI Toolkit, Ahrefs Brand Radar). | Compared in [../07-measurement/tools-comparison.md](../07-measurement/tools-comparison.md). |
| **Unbranded prompt** | A question that does not name the brand ("best AI takeoff software for subcontractors"). | Where Quotr is missing: named in 1 of 32. The main GEO goal. |
| **UTM parameter** | A tag added to a link to show where a visit came from (e.g. `utm_source=chatgpt.com`, which ChatGPT adds). | Helps GA4 attribute ChatGPT visits. Strip such tags from links inside Quotr's own posts. |
| **Vendor study** | Research published by a company that sells related products (SEO tools, review sites, PR software). | Useful but directional; this brain flags them. |
| **Visibility score** | A tracking tool's combined score of how often and how prominently a brand appears. | Definitions differ by tool; compare like with like. |

---

## I. Traffic and funnel

| Term | Plain-English meaning | Why it matters / Quotr example |
|---|---|---|
| **AI referral traffic** | Visits that arrive by clicking links in AI answers. | About 1% of all website traffic in Conductor's enterprise benchmark (2025 data; vendor), growing fast. |
| **Branded search** | Searches that include your brand name ("quotr ai pricing"). | A key sign that AI mentions are building awareness. |
| **Conversion** | A visitor taking a valuable action (demo, trial, purchase). | Whether AI visitors convert better is unproven for B2B; measure it. |
| **CTR (click-through rate)** | The share of people who see a result and click it. | Falls sharply where AI Overviews appear (Ahrefs: −58% for position 1; vendor). |
| **Direct traffic** | Visits where the person typed the URL or analytics can't tell the source. | Often rises when AI names a brand without a click. |
| **Funnel: TOFU / MOFU / BOFU** | Top (learning about a problem), middle (comparing options), bottom (ready to buy). | Quotr's biggest AI gaps are TOFU and MOFU unbranded questions. |
| **Percentage point (pp)** | The simple difference between two percentages. | AI Mode cut clicks by 18.8 pp in the Aug 2026 experiment. |
| **Referral traffic** | Visits arriving from links on other sites or apps. | Perplexity visits often land here in GA4 unless you add a rule. |
| **Top of funnel reach (2026 meaning)** | Being named in AI answers, plus brand search, direct visits and self-reported "heard about you from AI", not only blog sessions. | See [traffic-and-funnel-impact.md](traffic-and-funnel-impact.md). |
| **Zero-click search** | A search that ends without any click. | About 68% of US Google searches in Jan–Apr 2026 (SparkToro). |

---

## J. Research names you will see cited

| Term | Plain-English meaning | Why it matters |
|---|---|---|
| **C-SEO Bench** | A peer-reviewed benchmark (Puerto et al., NeurIPS 2025) that re-tested GEO-style content tricks. Found most "largely ineffective" and classic SEO "significantly more effective". | The best counter to "GEO hacks" claims. |
| **GEO paper / GEO-bench** | Aggarwal et al., "GEO: Generative Engine Optimization" (KDD 2024), and its test set. Reported up to ~40% visibility gains from adding statistics, quotations and citations in a lab setting. | Often over-quoted; the 40% is an upper bound. |
| **Position-Adjusted Word Count** | The GEO paper's main metric: how much of an AI answer comes from a source, weighted by how early it appears. | Explains what "40% more visibility" measured. |

**Count:** 150+ terms across groups A–J.

---

## Related pages

- [how-ai-engines-choose-sources.md](how-ai-engines-choose-sources.md) — the engines, crawlers and controls in detail
- [signals-that-matter.md](signals-that-matter.md) — the evidence behind the terms
- [myths-and-risks.md](myths-and-risks.md) — llms.txt, hidden text, prompt injection and other traps
- [traffic-and-funnel-impact.md](traffic-and-funnel-impact.md) — CTR, zero-click and top-of-funnel measurement
- [../04-prompt-library/construction-glossary.md](../04-prompt-library/construction-glossary.md) — construction and estimating terms
- [../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md) — Quotr's canonical facts
- [../07-measurement/tracking-setup.md](../07-measurement/tracking-setup.md) — setting up the measurement tools named here
