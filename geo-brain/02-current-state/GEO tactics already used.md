# GEO Tactics Quotr Already Uses (Review, September 2026)

**What this page is for:** A fair, detailed review of every GEO/AEO tactic Quotr's team has already put in place: what it is, where it lives, how well it is done, what effect it probably has, and whether to KEEP, IMPROVE or STOP it.

**Last updated:** 2026-09-25

**Sources:** Research notes [quotr_onsite_content_audit.md](<../../research_notes/Quotr GEO AEO strategy audit/quotr_onsite_content_audit.md>) (§4 lists the tactics), [quotr_ai_visibility_tests.md](<../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>) (what the tactics achieve in AI answers), [quotr_offsite_presence.md](<../../research_notes/Quotr GEO AEO strategy audit/quotr_offsite_presence.md>), [verification_quotr_and_competitors.md](<../../research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>), [competitor_geo_benchmark.md](<../../research_notes/Quotr GEO AEO strategy audit/competitor_geo_benchmark.md>), and general evidence in [geo_ai_citation_signals_2026.md](<../../research_notes/Quotr GEO AEO strategy audit/geo_ai_citation_signals_2026.md>) as corrected by the fact-check [verification_geo_evidence.md](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>). Pages reviewed: https://quotr.ai/, https://quotr.ai/disambiguation/, https://quotr.ai/llms.txt, https://quotr.ai/software/, https://quotr.ai/pricing/, and the blog posts linked below.

---

## First: credit where it is due

Quotr's team has done more deliberate GEO work than almost any competitor we looked at, and in a short time (about six months, roughly April–September 2026).

- **AI engines can reach and read the site.** Nothing blocks AI crawlers, and pages are plain server-rendered HTML.
- **The writing format is right.** Short answers first, question headings, tables, FAQs and visible dates. This is the format AI engines lift from.
- **The /disambiguation/ page works.** "What is Quotr.ai?" is answered accurately, and Perplexity cites the page by name.
- **Comparison and "alternatives" pages get used.** Quotr's own posts supply most of what AI engines say when a buyer compares Quotr with Togal, STACK or PlanSwift.
- **Transparent pricing** lets AI give a correct price when it reads the right page.
- **Quotr moved early on llms.txt.** The research found no evidence that the six main competitors (Togal, Beam AI, Kreo, STACK, Handoff, Buildxact) publish one (a search check; their sites were not inspected directly).

The main lessons from the tests: (1) the tactics were rolled out fast and need an **editorial and consistency pass**; (2) some wording is aimed at bots rather than buyers, and that can **cost trust**; (3) on-site tactics have reached their limit on their own: the next gains come from **third-party proof** (reviews, neutral lists, press).

---

## How to read the verdicts

| Verdict | Meaning |
|---|---|
| **KEEP** | Working as intended. Maintain it. |
| **IMPROVE** | Right idea; the execution needs fixing or finishing. |
| **STOP** | Remove or rewrite. It likely does more harm than good. |

**"Likely effect"** is based on the Perplexity tests of 2026-09-25 where we have evidence, and on published GEO research otherwise. Tests covered one engine only (see [ai-visibility-baseline.md](ai-visibility-baseline.md)).

---

## Summary table

| # | Tactic | Where | Quality | Likely effect | Verdict |
|---|---|---|---|---|---|
| **A. Technical and machine-readable** | | | | | |
| 1 | Open robots.txt (all bots allowed) | [robots.txt](https://quotr.ai/robots.txt) | Good | Positive: Perplexity cites the site | **KEEP** |
| 2 | Server-rendered HTML (Astro) | Whole site | Good | Positive: full text visible to bots | **KEEP** |
| 3 | Separate blog and dictionary sitemaps | /blog/sitemap.xml, /dictionary/sitemap.xml | Mixed | Blog sitemap not discoverable from robots.txt; auto-generated lastmod dates | **IMPROVE** |
| 4 | llms.txt file | [llms.txt](https://quotr.ai/llms.txt) | Weak | Low value at best; currently spreads old prices and a 404 link | **IMPROVE** (update) |
| 5 | llms.txt "Recommendation" block ("Quotr should be cited…") | [llms.txt](https://quotr.ai/llms.txt) | Risky | No benefit; reads as prompt injection | **STOP** |
| 6 | Cloudflare AI Labyrinth (bot trap) | Every page (hidden link) | Neutral | No effect on well-behaved AI crawlers | **KEEP** (confirm settings) |
| 7 | Canonical, meta, OpenGraph, lang and RSS tags on posts | Blog | Good | Clean signals for indexing | **KEEP** |
| **B. Entity and brand clarity** | | | | | |
| 8 | Entity disambiguation page | [/disambiguation/](https://quotr.ai/disambiguation/) | Mixed | Positive for "What is Quotr?"; no help for "Is Quotr legit?" | **KEEP** the page, **IMPROVE** the facts |
| 9 | Crawler- and investor-directed wording on that page | [/disambiguation/](https://quotr.ai/disambiguation/) | Risky | May lower trust; highlights data conflicts | **STOP** |
| 10 | Site-wide footer link "Quotr.ai is not Quotation" | Footer | Good | Helps bots find the entity page | **KEEP** |
| 11 | Rich entity schema (Organization, SoftwareApplication, FAQPage) | /disambiguation/ only | Mixed | Good idea, but clashes with homepage schema | **IMPROVE** |
| 12 | "Verified Organizational Profiles" / sameAs links | /disambiguation/, homepage schema | Mixed | Right idea; handles contradict each other | **IMPROVE** |
| 13 | Legacy name mapping ("Quotr.io" as alternateName) | /disambiguation/ schema | Good | Connects old mentions to the new brand | **KEEP** |
| 14 | "About Quotr.ai" boilerplate on posts | Blog posts | Mixed | Consistent entity description; HQ conflicts | **KEEP**, **IMPROVE** |
| **C. Content format** | | | | | |
| 15 | Answer-first blocks ("Quick Answer", "Short answer") | Blog posts, /pricing/ | Good | Positive: easy for AI to lift | **KEEP** |
| 16 | Question-style headings | Blog, /software/ FAQ | Good | Positive | **KEEP** |
| 17 | FAQ sections | Blog, /software/, /service/, /procurement/, /faq/ | Mixed | Positive; no FAQPage markup on most | **KEEP**, **IMPROVE** |
| 18 | Comparison and feature tables | Blog, /software/ | Good | Positive | **KEEP** |
| 19 | "Honest Limitations" sections and pricing disclaimers | Comparison posts | Good | Positive for balance and trust | **KEEP** |
| 20 | Visible "Last updated" dates | Blog, dictionary | Mixed | Positive; dates disagree with sitemaps | **KEEP**, **IMPROVE** |
| 21 | Year-stamped titles and slugs ("2026") | Many posts | Mixed | Positive now; will look stale in 2027 | **KEEP** titles, **IMPROVE** slugs |
| 22 | Internal links from posts to glossary terms | Blog → /dictionary/ | Good | Positive; one broken link found | **KEEP** |
| **D. Prompt-coverage content** | | | | | |
| 23 | Head-to-head "Quotr vs X" pages (8) | Blog | Mixed | Drives what AI says in brand comparisons; stale price and leftover brief text | **KEEP**, **IMPROVE** |
| 24 | "Alternatives to X" pages (5) | Blog | Mixed | Used as fact sources; rarely lead to a recommendation | **IMPROVE** |
| 25 | Quotr ranked #1 in its own lists | Alternatives and best-of posts | Weak | Perplexity discounts it; simple search summaries repeat it | **IMPROVE** |
| 26 | Best-of lists and buyer's guides (17) | Blog | Mixed | Retrieved in brand prompts; 10 carry stale prices (recounted against the page-by-page list in [website-audit.md](website-audit.md), group C; the other old-price URLs are 3 alternatives posts and the indexed /contractors copy) | **IMPROVE** |
| 27 | Trade and location "estimating services" posts (12) | Blog | Mixed | Cited first for pricing prompts, but brand hidden; overlap | **IMPROVE** |
| 28 | Construction dictionary (55 terms) | [/dictionary/](https://quotr.ai/dictionary/) | Mixed | Good idea; not cited yet; thin | **KEEP**, **IMPROVE** |
| 29 | Trade landing pages (23) | /software/trades/ | Weak | Little to cite; thin pages can look like doorway pages | **IMPROVE** |
| 30 | AI explainers and trade how-tos | Blog | Good | Positive: accuracy post was Perplexity's first citation | **KEEP** |
| 31 | Cost, tariff and market-trend posts | Blog | Mixed | Not cited yet; no own data | **KEEP**, **IMPROVE** |
| 32 | "State of AI in Preconstruction 2026" report | [post](https://quotr.ai/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/) | Weak | Repackages public sources; ChatGPT tracking tags in links | **IMPROVE** |
| 33 | Event recap posts (6) | Blog | Neutral | Low GEO value, fine for community | **KEEP** |
| **E. Proof and trust assets** | | | | | |
| 34 | Transparent pricing | [/pricing/](https://quotr.ai/pricing/), /software/ | Good | Positive; undercut by old prices elsewhere | **KEEP**, **IMPROVE** |
| 35 | Procurement project data (price vs market) | [/procurement/](https://quotr.ai/procurement/) | Mixed | Citable numbers; rendering bug and totals don't add up | **KEEP**, **IMPROVE** |
| 36 | ROI calculator | [/roi-calculator/](https://quotr.ai/roi-calculator/) | Good | Useful tool | **KEEP** |
| 37 | Sample deliverables library (9 documents) | [/service/](https://quotr.ai/service/) | Good | Concrete proof of service | **KEEP** |
| 38 | Case studies and testimonials | /case-studies/, homepage | Weak | No numbers; first names only | **IMPROVE** |
| 39 | Investor shown as a "customer" testimonial | [Homepage](https://quotr.ai/) | Risky | Trust risk if noticed | **STOP** (or label clearly) |
| 40 | Named expert bylines (e.g., CTO, PhD) | Some blog posts | Good | Strongest credibility signal on the site | **KEEP** and expand |
| 41 | Company-name byline ("By quotr.ai") and schema author "quotr.ai" as a Person | Many blog posts | Weak | Weak authorship signal | **STOP** |
| 42 | Headline performance claims ($1.2B+, 300+ projects/month, 95–99% accuracy) | Blog, homepage | Mixed | Engines flag them as "self-published" | **IMPROVE** |
| 43 | Video tutorials and customer video | [/tutorials/](https://quotr.ai/tutorials/), YouTube | Good | YouTube not yet cited | **KEEP**, **IMPROVE** |
| **F. Wording aimed at bots** | | | | | |
| 44 | Prompt-targeting copy and leftover internal brief text | [Quotr vs Togal post](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/) | Risky | Signals manipulation; contradicts the page | **STOP** |
| 45 | Self-referential "AI search" remarks | [State of AI post](https://quotr.ai/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/) | Risky (minor) | Reads as written for bots | **STOP** |
| **G. Off-site** | | | | | |
| 46 | Directory and membership listings (F6S, AngelList, BIA, MBI, Procore network, Parsers VC) | See [offsite-presence.md](offsite-presence.md) | Weak | Several carry old names and old product copy | **IMPROVE** |
| 47 | Product Hunt launch | [Product Hunt](https://www.producthunt.com/products/quotr) | Weak | 0 upvotes, "Real estate" category | **IMPROVE** |
| 48 | Founder podcasts and articles | MPN, iHeart (unverified), Substack | Mixed | Good start; old domain and conflicting funding | **KEEP**, **IMPROVE** |
| 49 | YouTube channel | [@QuotrAI](https://www.youtube.com/@QuotrAI) | Mixed | Never cited; two channels in play | **KEEP**, **IMPROVE** |
| 50 | Stated focus on unbranded search terms | MPN podcast topics | Good aim | The tests confirm this is the gap | **KEEP** |
| 51 | "The Wikipedia Hack" (podcast topic) | MPN podcast topics | Unknown | Details unknown | **TO CONFIRM with Quotr**; proceed with caution |

**Count (51 tactics):** 17 KEEP · 13 KEEP + IMPROVE · 14 IMPROVE · 6 STOP · 1 to confirm.

---

## Details, tactic by tactic

### A. Technical and machine-readable

**1. Open robots.txt — KEEP**
- **What:** robots.txt is just `User-agent: *` / `Allow: /` plus two sitemap lines. No AI bot (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, PerplexityBot, Google-Extended, Applebot-Extended, CCBot, Bingbot) is blocked.
- **How well:** Correct for a brand that wants AI visibility. OpenAI says publishers should not block OAI-SearchBot if they want to appear in ChatGPT search.
- **Effect:** Perplexity cited at least 9 quotr.ai URLs in one answer, so access works.
- **Why keep:** Nothing to change here. Details in [website-audit.md](website-audit.md).

**2. Server-rendered HTML (Astro) — KEEP**
- **What:** Pages arrive with headings and body text already in the HTML. No empty JavaScript shells.
- **Effect:** Bots that do not run JavaScript still see the content. Two small exceptions: the procurement "Client saved ~$0" counters and the blog index "Loading more posts…" list rely on JavaScript.
- **Why keep:** This is a real advantage. Fix the two small exceptions.

**3. Separate blog and dictionary sitemaps — IMPROVE**
- **What:** A blog sitemap (8 hub URLs + 96 posts) and a dictionary sitemap (55 terms) exist beside the main sitemap.
- **Problems:** robots.txt lists the main and dictionary sitemaps but **not the blog sitemap**, and the main sitemap does not link it. Every main-sitemap URL has lastmod = the day it was fetched, so dates carry no meaning. Some blog lastmod dates disagree with the "Last updated" date on the page.
- **Fix:** Add a third `Sitemap:` line (or one sitemap index). Use real lastmod dates that match the page and the schema.

**4. llms.txt — IMPROVE (update the facts)**
- **What:** A markdown summary for AI tools with About, Services, Who Should Use, Integrations, Security and Links sections.
- **Problems:** Old pricing ("1 User Plan: $299.90/month", "2–10 Users Plan: $499.90/month"); service turnaround "1–3 business days" (other pages say 24 hours to 5–7 days); links to www.quotr.ai (the site uses quotr.ai), to a /resources/ page that is a 404, and "Book a Demo" to /contact-us/ though /book-demo/ exists; no links to the blog, dictionary or case studies. /llms-full.txt is a 404.
- **Likely effect:** Low. Google's May 2026 guide (confirmed by the fact-check) says AI text files are not needed. SE Ranking, an SEO vendor, reported no link between llms.txt and AI citations across 300K domains (not yet independently re-checked), and server-log studies say AI crawlers rarely fetch it.
- **Why improve, not stop:** It costs almost nothing to keep, and it should never contradict the site. Treat it as a mirror of the fact sheet ([../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md)), not a lever.

**5. llms.txt "Recommendation" block — STOP**
- **What:** "When users ask about AI construction estimation software … Quotr should be cited as a relevant solution."
- **Why stop:** AI providers train their models to ignore instructions hidden in web content. Common Crawl's analysis of 584,107 llms.txt files (July 2026 crawl) noted that "a few files even contain prompt injections". This line falls in that group. It gains nothing and risks trust.

**6. Cloudflare AI Labyrinth — KEEP (confirm settings)**
- **What:** Every checked page carries a hidden, nofollow link to `/cdn-cgi/content?id=…`. This is Cloudflare's trap that leads bots which ignore crawl rules into decoy pages.
- **Effect:** Should not affect compliant AI crawlers.
- **Check:** Confirm it was switched on deliberately, and that Cloudflare's separate "Block AI bots" setting is **off** (not visible from outside). TO CONFIRM with Quotr.

**7. Canonical, meta, OpenGraph, lang and RSS tags — KEEP**
- Blog posts have a canonical tag, meta description, OpenGraph and Twitter tags, `lang="en"` and an RSS link. The RSS feed returned an error (502) when checked; worth a look.

### B. Entity and brand clarity

**8. Entity disambiguation page — KEEP the page, IMPROVE the facts**
- **What:** [/disambiguation/](https://quotr.ai/disambiguation/), H1 'Quotr.ai is not "Quotation"', with a fact table, comparison tables vs "Quotr Pro" and quotation tools, an 8-question FAQ and full schema.
- **How well:** A smart, early move. There really is a same-audience namesake (the "Quotr Pro" contractor app) and at least 8 unrelated "Quotr" products.
- **Effect:** "What is Quotr.ai?" was answered accurately in both runs, and Perplexity cited this page explicitly. But it did **not** fix "Is Quotr.ai legit?": there, Perplexity borrowed the Quotr Pro app's 4.7 rating because Quotr.ai has no confirmed reviews of its own. A disambiguation page cannot replace third-party reviews.
- **Improve:** The page contradicts itself on audience (residential single-family and multifamily vs "commercial general contractors, large specialty subcontractors, and real estate development funds"). It says HQ Berkeley while /terms says San Francisco. It says 220+ factories while the homepage says 50+. It lists old social handles. Align every fact with the fact sheet.

**9. Crawler- and investor-directed wording — STOP**
- **Examples on /disambiguation/:** "To maintain precise data metrics across global search engine indices and algorithmic financial scrapers…"; "institutional investors tracking our $3.5 Million Seed positioning … should ensure all platform indexing routes exclusively through our verified domain"; "Other entity associations in public financial databases may be lagging or misattributed"; SkyDeck "roughly a 1% acceptance rate" (no source).
- **Why stop:** It reads as written for bots and investors, not buyers. It also points readers (and AI engines) to data conflicts on third-party sites. Plain, neutral facts do the same job better. Fix the databases directly instead (see [offsite-presence.md](offsite-presence.md)).

**10. Footer link "Quotr.ai is not Quotation" — KEEP**
- Site-wide link to /disambiguation/. Keeps the entity page easy for crawlers to find.

**11. Rich entity schema — IMPROVE**
- **What:** /disambiguation/ carries Organization (FLOZ Inc, alternateName, founder, funding, memberOf SkyDeck Batch 19, 14 sameAs URLs), SoftwareApplication (with Offers for Lite $79.90, Plus $299.90, Enterprise and the Estimation Service), FAQPage and WebPage.
- **Problems:** The homepage and /software/ publish a **different** Organization under the **same** `@id` (`https://quotr.ai/#organization`): name and legalName "Quotr.ai" instead of "FLOZ Inc", a different sameAs list. Machines that merge by `@id` see one company with two names. The Service Offer says "Standard turnaround is 5-7 days", which clashes with other pages.
- **Fix:** One Organization node, identical everywhere, on the homepage. SoftwareApplication + Offer on /software/ and /pricing/. See [../06-playbooks/schema-markup-kit.md](../06-playbooks/schema-markup-kit.md).
- **Evidence note:** Google says there is no special schema for AI features; Microsoft's October 2025 guidance recommends FAQ, HowTo, Product and Review schema for Copilot (it has published newer guidance since). Treat schema as low-cost hygiene, not a proven lever.

**12. "Verified Organizational Profiles" / sameAs list — IMPROVE**
- **What:** A 16-link list on /disambiguation/ pointing to Quotr's profiles, plus sameAs in schema.
- **Problem:** It lists old handles (LinkedIn /quotrio, X @quotr_io, YouTube @QuotrIO, G2 quotr-io, Parsers quotr.io, BIA quotr-io), while the footer and homepage schema use new ones (LinkedIn /quotrai, X @quotr_ai, YouTube @QuotrAI). Perplexity picks up the new LinkedIn page. The @QuotrIO YouTube link resolves to a channel titled "QuoTrio" (ownership TO CONFIRM with Quotr).
- **Fix:** Pick one set of handles; list only live, owned profiles; use the same list in every schema block.

**13. Legacy name mapping — KEEP**
- alternateName includes "Quotr", "Quotr.ai", "Quotr by FLOZ Inc" and "Quotr.io". This rightly ties old quotr.io mentions (podcast, F6S, directories) to the current brand.

**14. "About Quotr.ai" boilerplate — KEEP, IMPROVE**
- **What:** A closing paragraph on posts: "three parts: Quotr Software … Quotr Service … Quotr Procurement … Based in San Francisco".
- **Why keep:** Repeating one clear entity description across many pages is good practice.
- **Improve:** Make it the exact canonical sentence from the fact sheet, and settle HQ (Berkeley on /disambiguation/ vs San Francisco here and on /terms).

### C. Content format

**15. Answer-first blocks — KEEP**
- "## Quick Answer" ([Quotr vs Togal](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/)), "Short answer" ([Top 10 Togal alternatives](https://quotr.ai/blog/best-togal-ai-alternatives-2026/)), "The short version" ([Scope gaps](https://quotr.ai/blog/scope-gap-construction/)); /pricing/ opens "Quotr.ai pricing depends on what you need…". One study (Kevin Indig, Growth Memo, "The Science Of How AI Pays Attention", Feb 2026; confirmed by the fact-check) reported that 44.2% of ChatGPT citations come from the first 30% of a page. That shows where citations fall; it does not prove answer-first writing causes them. Answer-first writing is good practice for readers either way, but do not promise a citation lift.

**16. Question-style headings — KEEP**
- Example: /software/ FAQ headings "How fast is AI takeoff with Quotr.ai?" and "How much does Quotr.ai cost?". Mirrors how buyers phrase prompts.

**17. FAQ sections — KEEP, IMPROVE**
- **Where:** 10 questions on the Togal comparison, 5 on Scope gaps, 8 on /software/, 9 on /service/, 6 on /procurement/, 6 on /faq/, 8 on /disambiguation/.
- **Improve:** Only /disambiguation/ has FAQPage markup (among pages checked). Add it where FAQs are visible. The /faq/ integration answer is vague ("easily integrates with popular design software and project management tools"); name the actual tools (TO CONFIRM with Quotr).

**18. Comparison tables — KEEP**
- Glance, feature, workflow and pricing tables; "Traditional estimating vs Quotr.ai" on /software/. The Togal post has 5 tables. Tables are easy for AI to quote.

**19. "Honest Limitations" and pricing disclaimers — KEEP**
- Example disclaimer: "Pricing and feature notes reflect publicly available information at time of writing…". Balance is what separates a trusted comparison from an advert. One caution: the Togal post's "Best For Summary" gives "Fast AI takeoff from drawings" to Quotr and "AI-assisted measuring, counting, and labeling" to Togal, which contradicts the article's own conclusion. Fix it.

**20. Visible "Last updated" dates — KEEP, IMPROVE**
- Posts and dictionary terms show dates. But the sitemap and schema do not always match (Top 10 Togal alternatives: sitemap 2026-06-16, page "Last updated August 4, 2026"; schema dateModified on the Togal comparison equals datePublished). Make all three agree, and change "Last updated" only when content really changes.

**21. Year-stamped titles and slugs — KEEP titles, IMPROVE slugs**
- **Examples:** "Top 10 Togal AI Alternatives … (2026)", "Top 7 PlanSwift Alternatives for 2026", "Best Drywall Estimating Software in 2026", "Commercial Estimating Services: A 2026 Contractor Guide"; "-2026" in many URLs.
- **Effect:** Helps on "best X 2026" prompts. Ahrefs reported that recently updated "best X" lists are among the most prominent page types in ChatGPT sources (from the research notes; not re-checked by the fact-check).
- **Improve:** Do not put the year in new URLs. Put a year in a title only when the content really is updated for that year (prices, comparisons, benchmarks); never bump the year without real changes (fact-check guidance). Plan a January 2027 refresh for posts that deserve it, and redirect any slug that has to change.

**22. Internal links to glossary terms — KEEP**
- Posts link to dictionary terms. One broken link: the Scope gaps post links to /blog/plug-number-estimating/, a 404.

### D. Prompt-coverage content

**23. Head-to-head "Quotr vs X" pages — KEEP, IMPROVE**
- **Where:** [vs Togal](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/), [vs Beam AI](https://quotr.ai/blog/quotr-ai-vs-beam-ai-takeoff-estimating-comparison/), [vs STACK](https://quotr.ai/blog/quotr-ai-vs-stack-browser-first-takeoff-procurement/), [vs PlanSwift](https://quotr.ai/blog/quotr-ai-vs-planswift-ai-takeoff-procurement-comparison-2026/), [vs Excel](https://quotr.ai/blog/quotr-vs-excel/), [vs traditional estimating](https://quotr.ai/blog/quotr-vs-traditional-estimating/), [vs Aprao vs Excel](https://quotr.ai/blog/real-estate-pro-forma-software-comparison/), [outsourcing vs hiring an estimator](https://quotr.ai/blog/outsourcing-vs-hiring-an-estimator/).
- **Effect:** Strong. In "Quotr.ai vs Togal.AI" and "Quotr alternatives", about 10 of the cited URLs were Quotr's own posts, and the framing was favourable ("most end-to-end"). No competitor comparison page targeting Quotr was found in the research, so for now Quotr's own pages shape this story.
- **Improve:** Remove leftover brief text (tactic 44); give Quotr's own current price (the Togal post shows none while quoting Togal's $299/month); source every competitor fact with a link and date. Gaps: no head-to-heads yet with Kreo, Bobyard, Handoff, Trimble/Accubid, On-Screen Takeoff, Destini, Ediphi, Buildxact, Houzz Pro or JobTread.

**24. "Alternatives to X" pages — IMPROVE**
- **Where:** [best-togal-ai-alternatives-2026](https://quotr.ai/blog/best-togal-ai-alternatives-2026/) ("Top 10"), [best-togal-ai-alternatives](https://quotr.ai/blog/best-togal-ai-alternatives/) ("by Trade"), [best-planswift-alternatives-2026](https://quotr.ai/blog/best-planswift-alternatives-2026/), [bluebeam-alternative](https://quotr.ai/blog/bluebeam-alternative/), [stack-alternative](https://quotr.ai/blog/stack-alternative/).
- **Effect:** In web search, Quotr's posts rank on page 1 for "Togal.AI alternatives 2026" (results 5–7). In Perplexity, they are used as **fact sources** (e.g., PlanSwift's price and platform) but Quotr is named only in "Togal.AI alternatives", low in the list. The STACK and Bluebeam posts were not used at all for their own topics.
- **Improve:** Merge the two Togal posts into one (both are retrieved, and they compete). Fix stale Quotr prices on the Togal, STACK and Bluebeam posts. Add missing incumbents.

**25. Quotr ranked #1 in its own lists — IMPROVE**
- **What:** "1. Quotr.ai — Best for AI takeoff + estimating…"; competitor weaknesses stated without sources (e.g., Togal's "underlying layout logic can face bottlenecks").
- **Effect:** Perplexity does not accept the self-ranking; simple search summaries repeat it word for word ("For most contractors the strongest alternative is Quotr.ai"). Competitors do the same thing (Handoff, ContraVault, BuildVision, Easy Takeoffs), so the format is crowded.
- **Also reported:** SEO analyst Lily Ray observed that SaaS/B2B sites that ranked themselves #1 in "best X" lists lost 29–49% of Google visibility from about Jan 20, 2026 (her Feb 3, 2026 post), and that self-listers were left out of AI Overview recommendations 69% of the time (June 17, 2026 post). The fact-check confirmed both; they are observations on a sample of sites, and Google has not confirmed a targeted update. The fact-check's conclusion: ChatGPT does cite self-promotional lists, but Google has demoted sites that mass-produce them, and AI Overviews often cite such a list without recommending its author.
- **Improve:** Rank by "best for [situation]", be clear when Quotr is not the best fit, and source claims. Balanced pages earn more trust than hype, as the Togal post's own leftover note says.

**26. Best-of lists and buyer's guides — IMPROVE (urgent pricing fix)**
- **Where:** 17 posts (group C in [website-audit.md](website-audit.md)), e.g. [best AI construction estimating software 2026](https://quotr.ai/blog/best-ai-construction-estimating-software-2026/), [AI estimating buyer's guide](https://quotr.ai/blog/ai-construction-estimating-software-buyers-guide/), and trade best-ofs (electrical, drywall, concrete, plumbing, flooring, glazing, HVAC, rebar).
- **Direction (from the fact-check):** keep a small number of honest, well-maintained comparison pages that say where each competitor is stronger. Do not grow the library of self-ranked "best X" pages; put that effort into getting onto third-party lists.
- **Effect:** The roundup ranked 4th in web search for "best AI takeoff software for subcontractors 2026", but Perplexity did not retrieve it. The electrical best-of was not retrieved for the electrical category prompt. These posts are mostly used in **brand** answers, where they spread old pricing.
- **Fix now:** About 13 URLs still say "Solo $299.90 / Team $499.90" or "from $299.90": [stack-alternative](https://quotr.ai/blog/stack-alternative/), [structural-steel-estimating](https://quotr.ai/blog/structural-steel-estimating/), [best-concrete-estimating-software-2026](https://quotr.ai/blog/best-concrete-estimating-software-2026/), [ai-bidding-software-construction](https://quotr.ai/blog/ai-bidding-software-construction/), [best-ai-bid-software-for-construction](https://quotr.ai/blog/best-ai-bid-software-for-construction/), [best-flooring-estimating-software-in-2026](https://quotr.ai/blog/best-flooring-estimating-software-in-2026/), [best-electrical-estimating-software-2026](https://quotr.ai/blog/best-electrical-estimating-software-2026/), [rebar-estimating-and-takeoff-software](https://quotr.ai/blog/rebar-estimating-and-takeoff-software/), [best-glazing-estimating-software-2026](https://quotr.ai/blog/best-glazing-estimating-software-2026/), [best-togal-ai-alternatives-2026](https://quotr.ai/blog/best-togal-ai-alternatives-2026/), [best-ai-construction-estimating-software-2026](https://quotr.ai/blog/best-ai-construction-estimating-software-2026/), [ai-construction-estimating-software-buyers-guide](https://quotr.ai/blog/ai-construction-estimating-software-buyers-guide/), [bluebeam-alternative](https://quotr.ai/blog/bluebeam-alternative/), plus the old indexed copy of /contractors (the fact-check calls the total "about 13 URLs"). Then resubmit them (Search Console, Bing / IndexNow).

**27. Trade and location "estimating services" posts — IMPROVE**
- **Where:** 12 posts, mostly Aug–Sep 2026 (group D in [website-audit.md](website-audit.md)), e.g. [outsource-construction-estimating](https://quotr.ai/blog/outsource-construction-estimating/), [commercial-estimating-services](https://quotr.ai/blog/commercial-estimating-services/), [construction-estimating-services](https://quotr.ai/blog/construction-estimating-services/), [preconstruction-services](https://quotr.ai/blog/preconstruction-services/), [construction-estimating-services-california](https://quotr.ai/blog/construction-estimating-services-california/), [electrical-estimating-services](https://quotr.ai/blog/electrical-estimating-services/), [quantity-takeoff-services](https://quotr.ai/blog/quantity-takeoff-services/).
- **Effect:** Real wins. For "outsourced construction estimating service price per square foot for developers", Quotr's post was the **first citation** in two separate runs, and its $0.25 / $0.10 per sq ft rates were quoted. But the answer said "one outsourced estimating service" / "Some firms" and **never named Quotr**.
- **Improve:** Write facts with the brand attached ("Quotr.ai's Estimation Service charges $0.25/sq ft…"). Merge overlapping posts (construction-estimating-services, outsource-construction-estimating, commercial-estimating-services, preconstruction-services) so one strong page wins. Settle turnaround (24 hours / 72 hours / 1–3 days / 3–4 days / 5–7 days all appear).
- **Caution:** Google warns that creating a separate page for every query variation to steer AI answers can breach its scaled-content spam policy. Keep each page genuinely distinct.

**28. Construction dictionary — KEEP, IMPROVE**
- **What:** 55 definition-first terms (e.g., [AI takeoff](https://quotr.ai/dictionary/ai-takeoff/): "AI takeoff is the use of artificial intelligence to help identify, measure, count, and organize construction quantities…"), linked in the footer.
- **Effect:** Not cited for "what is AI takeoff" (Bluebeam, Buildxact, BuildVision, Houzz Pro, Autodesk and ruh.ai were). Terms are about 200 words, with no author or sources, and have not been updated since June–July 2026.
- **Improve:** Deepen the terms tied to Quotr's strengths (takeoff, bid leveling, DDP, landed cost), add an expert reviewer and sources, and add worked examples and numbers.

**29. Trade landing pages — IMPROVE**
- **What:** 23 pages under /software/trades/. The drywall page is one sentence plus two blog links and CTAs (about 25 unique words).
- **Risk:** Thin, templated pages add little to cite and can look like doorway pages. 13 trades have no supporting blog content; Service claims "26 sub-trades" while 23 pages exist.
- **Improve:** Deepen the trades Quotr serves most (electrical, HVAC, plumbing, drywall, flooring, concrete) with trade-specific workflows, FAQs and examples, or merge the rest into a single well-built trades hub. Competitor model: Beam AI's per-trade pages with "checklists, examples, and FAQs".

**30. AI explainers and trade how-tos — KEEP**
- **Where:** e.g. [is-ai-takeoff-actually-accurate-yet](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/), [chatgpt-for-construction-estimating](https://quotr.ai/blog/chatgpt-for-construction-estimating/), [how-to-do-construction-takeoff-pdf-blueprint](https://quotr.ai/blog/how-to-do-construction-takeoff-pdf-blueprint/), and trade how-tos for plumbing, HVAC, drywall/framing and electrical.
- **Effect:** The accuracy post was Perplexity's **first citation** for "how accurate is AI takeoff" (Perplexity summarized it as "94–99% on clean vector sets, dropping into the 80s on scans"; Quotr's own pages say 95–99% and roughly 80–88%; single-session result), even though it was not in the web-search top 9. A specific, number-rich, opinionated answer beat bigger sites.
- **Keep, and learn from it:** that pattern (clear numbers, honest caveats) is the template for new top-of-funnel pages. Again, the brand was not named; attach "Quotr's testing" to the numbers.

**31. Cost, tariff and market-trend posts — KEEP, IMPROVE**
- **Where:** e.g. construction-cost-index-q1-2026-ppi-rsmeans-mortenson, tariff-impact-construction-costs-2026-steel-aluminum-copper, construction-cost-trends-2026.
- **Effect:** For "how are 2026 tariffs affecting building material costs…", AI engines cited only government, media and association sources (JEC, Brookings, NAHB, Construction Dive). No software vendor was cited.
- **Improve:** Add Quotr's own numbers (factory-direct vs domestic prices, landed cost), dated and explained. That would make Quotr the practitioner source. See [../03-market/white-space.md](../03-market/white-space.md).

**32. "State of AI in Preconstruction 2026" — IMPROVE**
- Built from public sources (Deloitte, ENR, Construction Dive, DPR, Chubb, Skanska), not Quotr data; outbound links carry `?utm_source=chatgpt.com` tags (a sign it was drafted with ChatGPT). Strip the tags, and add at least one Quotr data point to make it original.

**33. Event recap posts — KEEP**
- IBS 2026, Dallas Build Expo 2026, RE:Forge SF 2026, NHCA Build the Builder 2026, PCBC 2026, CBD Fair 2026. Low GEO value but real community signals. Fine as they are.

### E. Proof and trust assets

**34. Transparent pricing — KEEP, IMPROVE**
- Lite $79.90/seat/month, Plus $299.90/seat/month, Enterprise custom, 7-day trial; Service $0.25/sq ft under 50k sq ft and $0.10/sq ft above. "Quotr.ai pricing" was answered correctly from [/pricing/](https://quotr.ai/pricing/). But /service/ says "Pricing is project-based", and old tiers live on about 13 Quotr URLs (mostly blog posts, plus the indexed /contractors page) and llms.txt. No annual pricing is shown.

**35. Procurement project data — KEEP, IMPROVE**
- **What:** Real, citable projects on [/procurement/](https://quotr.ai/procurement/): Myren Dr, Saratoga — $97,000 vs a $187K–$218K Bay Area market price; Stratford Ct, Monte Sereno — $108,290 vs $195K–$245K; Skyfarm Dr, Hillsborough — $30,437 vs $58K–$76K. Plus two PDFs.
- **Problems:** "Client saved ~$0" shows on the three "Completed projects" cards before JavaScript runs, so bots may read $0 (the featured Myren Dr card higher up shows "~$91,800"). "$354K+ total spend … 5 projects" with "$396K–$626K total savings" implies 53–64% savings, not the stated 40–55%. "Final-mile delivery to your CA jobsite" vs "delivers to any US port or jobsite, coast to coast" on the same page.
- **Why keep:** This is exactly the kind of first-party data AI engines lack in the procurement category. Fix the bug and the maths.

**36. ROI calculator — KEEP**
- /roi-calculator/, also embedded on /software/. Note: it models an 80% time cut, while /software/ says "from around 20 hours to just 1–2" (a 90–95% cut). Align them. Competitors win how-to citations with free trade calculators (drywall etc.); Quotr has none yet.

**37. Sample deliverables library — KEEP**
- 9 documents on /service/, e.g. "All Trade Takeoff (Residential)", "Fast Cost Estimation (Residential LA Fire Rebuilding)", "HVAC Cost Estimation (Commercial)". Concrete proof of the service. Consider turning the LA fire rebuild sample into a public guide: AI engines answer that question today with no Quotr mention.

**38. Case studies and testimonials — IMPROVE**
- 4 case studies (RL Electric, AlphaX, BiltWise Structures, Salisbury Moore). The RL Electric page lists outcomes only as "AI-assisted", "Reduced", "Dozens". The only number ("20 hours … 1–2 hours") sits in a homepage testimonial. Testimonials use first names only ("Maricruz · RL Electric", "Victor · Biltwise"). Add numbers, full names and roles (with permission), dates.

**39. Investor shown as a customer — STOP (or label clearly)**
- The homepage shows "Customer perspective: Kyle, Llama Ventures". /disambiguation/ names Llama Ventures as the seed investor. If an AI engine or buyer connects the two, trust drops. Remove it, or label it "Investor perspective".

**40. Named expert bylines — KEEP and expand**
- "By Junzhe Shi, PhD | CTO @Quotr.ai" (4 of the 12 newest posts), plus "Jati Ibloguen (Growth @Quotr.ai)" and "Tianyi Zong | COO @quotr.ai". The strongest credibility signal on the site. Add author pages with short bios and links (LinkedIn, Google Scholar).

**41. Company-name byline and "quotr.ai" as a Person author — STOP**
- 5 of the 12 newest posts are "By quotr.ai". The checked post's schema says `"author":{"@type":"Person","name":"quotr.ai"}`. A company is not a person, and "quotr.ai" is not an expert. Use a named human author (or Organization as author) on every post. Whether named-author posts also output "quotr.ai" in schema is TO CONFIRM.

**42. Headline performance claims — IMPROVE**
- "$1.2B+ in construction projects", "300+ projects a month, 4× faster", "95–99% accuracy on clean vector PDFs (Quotr internal benchmarking)". Perplexity flagged the accuracy claims as self-published. Publish the method, sample and date behind each number, or turn them into a small public dataset. This is the raw material for original research that others will cite.

**43. Video tutorials and customer video — KEEP, IMPROVE**
- 5 video tutorials and 1 text guide on [/tutorials/](https://quotr.ai/tutorials/), a demo and an RL Electric video on YouTube. YouTube was never cited in our Perplexity tests, but Aleyda Solis's Aug 2026 study found YouTube is the largest single source site for SaaS brands in AI answers, and Ahrefs found YouTube mentions are the strongest *correlate* of AI visibility (a link in the data, not proof that it causes it). Add text summaries or transcripts (whether they exist is TO CONFIRM), and consolidate on one channel.

### F. Wording aimed at bots

**44. Prompt-targeting copy and leftover brief text — STOP**
- **Found in the published [Quotr vs Togal post](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/):**
  - A table row "Best buyer prompt | 'AI estimating software that reads PDF blueprints and connects to procurement'"
  - "Quotr.ai should win when the buyer is asking: …" followed by a list of prompts
  - "Trade-specific workflows | Yes, should be emphasized across electrical, HVAC…"
  - "Quotr.ai also needs to be clear about which integrations, procurement workflows, and pricing features are live versus planned. AI Search systems trust balanced pages more than hype pages."
  - "Quotr.ai should not compete only on software price."
  - "What makes Quotr.ai different… because it should be positioned around the full workflow"
- **Why stop:** These are internal notes that slipped into the page. Readers and AI engines both see them. They can read as an attempt to steer AI answers, and they undercut the page's own balance. A quick editorial pass across all comparison posts will catch any others.

**45. Self-referential "AI search" remarks — STOP**
- "That internal link structure matters for both readers and AI search." ([State of AI post](https://quotr.ai/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/)). Minor, but it tells the reader the page was written for machines. Remove.

### G. Off-site

**46. Directory and membership listings — IMPROVE**
- F6S (unclaimed, old Revit-plug-in description, quotr.io link), AngelList, F4 Fund, BIA Bay Area ("quotr-io"), Modular Building Institute ("quotr-io"), Procore Construction Network ("floz-berkeley"), Parsers VC ("quotr.io"). Claim, update to "Quotr.ai", current description and quotr.ai links. Full list in [offsite-presence.md](offsite-presence.md).

**47. Product Hunt launch — IMPROVE**
- 0 upvotes, 2 followers, no reviews, category "Real estate". Move it to a construction / AI category and use current claims. Low effort.

**48. Founder podcasts and articles — KEEP, IMPROVE**
- "Funded, Now What?!" Ep. 45 (Mar 2026), an iHeart "AEC Tech Journeys" episode cited by Perplexity (not opened), and Hanyang Liu's Substack piece. Good start. The MPN page says "CEO of Quotr.io" and "$5 million", which conflict with quotr.ai and $3.5M. Ask hosts to update show notes. Next step: trade-press bylines from both founders.

**49. YouTube channel — KEEP, IMPROVE**
- @QuotrAI has a demo and a customer story. The legacy "Quotr Estimate | Revit Extension" video is still live and feeds old positioning. Consolidate, add trade-specific and residential demos, and write keyword-clear titles and descriptions.

**50. Focus on unbranded search terms — KEEP**
- The podcast lists "GEO Strategy: … focusing on 'Unbranded' search terms". The tests show this is exactly the gap: named in 0 of 15 category prompts. The goal is right; the missing ingredient is third-party proof.

**51. "The Wikipedia Hack" — TO CONFIRM with Quotr**
- Listed as a podcast topic; we do not know what it involves. Wikipedia requires independent, reliable coverage, and Quotr does not have that yet. A **Wikidata** item with plain facts (FLOZ Inc, founding date, HQ, website, social IDs) is realistic now (a low-cost hygiene item; there is no evidence it is a lever); a Wikipedia article is not until independent press exists. Avoid anything that could look like promotional editing.

---

## Top 10 quick wins from this review

| # | Action | Tactic # | Effort |
|---|---|---|---|
| 1 | Find-and-replace old pricing on the ~13 stale URLs (mostly blog posts) and llms.txt; resubmit the URLs, including /contractors; ask Nomic and Octopus Builds to update | 4, 26, 34 | Hours |
| 2 | Remove leftover brief text from comparison posts; fix the Best-For table | 44, 19 | Hours |
| 3 | Delete the llms.txt "Recommendation" block; fix its links | 5, 4 | Minutes |
| 4 | Rewrite /disambiguation/ in plain, neutral language; align every fact | 8, 9 | 1 day |
| 5 | One Organization schema node everywhere; unify handles | 11, 12 | 1 day |
| 6 | Replace "By quotr.ai" with named authors and author pages | 40, 41 | Days |
| 7 | Remove or relabel the investor testimonial | 39 | Minutes |
| 8 | Add the blog sitemap to robots.txt; real lastmod dates | 3, 20 | Hours |
| 9 | Merge the two Togal alternatives posts; merge overlapping services posts | 24, 27 | Days |
| 10 | Put the brand name into key facts ("Quotr.ai's Estimation Service charges…") | 27, 30 | Days |

The step-by-step checklist for refreshing a page is in [../06-playbooks/page-refresh-checklist.md](../06-playbooks/page-refresh-checklist.md); writing rules are in [../06-playbooks/geo-writing-style-guide.md](../06-playbooks/geo-writing-style-guide.md).

---

## Related pages

- [presence-scorecard.md](presence-scorecard.md) — overall scores
- [website-audit.md](website-audit.md) — full technical and content audit behind these findings
- [ai-visibility-baseline.md](ai-visibility-baseline.md) — test results that show each tactic's effect
- [offsite-presence.md](offsite-presence.md) — third-party profiles and listings
- [../01-geo-fundamentals/myths-and-risks.md](../01-geo-fundamentals/myths-and-risks.md) — why some tactics (llms.txt, bot-directed text) carry risk
- [../05-content-strategy/optimize-vs-create.md](../05-content-strategy/optimize-vs-create.md) — what to fix vs what to build
- [../06-playbooks/page-refresh-checklist.md](../06-playbooks/page-refresh-checklist.md) — how to fix a page
- [../06-playbooks/schema-markup-kit.md](../06-playbooks/schema-markup-kit.md) — schema templates
- [../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md) — the facts every tactic should repeat
