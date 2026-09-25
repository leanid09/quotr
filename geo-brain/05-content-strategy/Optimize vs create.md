# Optimize Existing Content vs Create New: Framework, Fact-Fix Sweep and Page-by-Page Actions

**What this page is for:** How Quotr should split effort between fixing, merging and refreshing its existing pages and creating new ones, with a decision framework, a recommended effort split, the full "fact-fix sweep" (every inconsistency to correct) and a page-by-page action table for every quotr.ai page the research found. It answers the meeting question **"How should we think about optimizing existing content versus creating new content?"**

**Last updated:** 2026-09-25

**Sources:** the final report [audit report](<../../reports/Quotr GEO AEO strategy audit.md>) (sections "Existing vs new content" and "A 90-day plan"); research notes [quotr_onsite_content_audit.md](<../../research_notes/Quotr GEO AEO strategy audit/quotr_onsite_content_audit.md>) (full inventory, §1–§6), [verification_quotr_and_competitors.md](<../../research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>) (corrections: ~13 stale-price URLs, /terms HQ, PlanSwift ownership, staging host), [verification_geo_evidence.md](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>) (freshness evidence and claim H6), [geo_content_playbook_b2b.md](<../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md>) (§2), [quotr_ai_visibility_tests.md](<../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>) (which pages AI cites); brain pages [../02-current-state/website-audit.md](../02-current-state/website-audit.md) (list of all 96 posts), [../02-current-state/geo-tactics-already-used.md](../02-current-state/geo-tactics-already-used.md), [../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md) (inconsistency register), [../04-prompt-library/prompt-library.md](../04-prompt-library/prompt-library.md) (prompt IDs). In the text, "verification file" or "Quotr fact-check" means verification_quotr_and_competitors.md, and "GEO-evidence fact-check" means verification_geo_evidence.md.

---

## The short answer

**Fix first, then build new.** Some of Quotr's existing pages are actively hurting it: they are the reason AI tools quote a starting price nearly four times too high and report "50+ to 220+ factories, depending on the page". So:

1. **Weeks 1–2 (P0): the fact-fix sweep.** One agreed fact sheet, then correct every page and file that disagrees with it: old prices on about 13 URLs and llms.txt, factory count, HQ, savings, turnaround, audience, founders, handles, leftover internal notes, the wrong PlanSwift ownership claim, the staging site, sitemaps. Ask Google and Bing to re-read the fixed pages.
2. **Weeks 2–6 (P1): consolidate and brand-attach.** Merge the duplicate Togal posts and the overlapping "estimating services" posts. Rewrite key sentences on the pages AI already fetches so the Quotr name travels with each fact.
3. **From month 2: put most new effort into unique assets** (original data, tools, proof), not into constant refreshing or more posts. Refresh a page only when its facts really change, and say what changed.

**Recommended effort split** (our recommendation, explained below): October 2026 is about 75% fix/refresh; from November to March about 5–10% trailing fixes, 20–25% refresh, 45–50% new unique assets and 20–25% support for off-site work.

**The test for anything new:** it must contain something no competitor or AI could write without Quotr's data, customers or people (report).

---

## Words used on this page

- **Refresh:** a real update of a page's content (new facts, new data, new sections), keeping the same URL.
- **Merge:** combine two or more overlapping pages into one; the others permanently redirect to it.
- **Redirect (301):** a permanent forward from an old URL to a new one, so old links and search signals move to the new page.
- **Noindex:** a tag that tells search engines not to list a page, while people can still visit it.
- **Prune:** delete a page with no value. (We found no clear prune candidates from outside data; this needs Quotr's Search Console data.)
- **Canonical:** a tag that tells search engines which URL is the main version of a page.
- **Brand-attached fact:** a sentence where the Quotr name is part of the fact, e.g. "Quotr.ai's Estimation Service charges $0.25 per sq ft…".
- **Sitemap / lastmod:** the file that lists a site's URLs and the date each last changed.
- **Schema:** hidden labels in a page's code that describe facts (company name, price, author) to machines.
- **llms.txt:** a text file some sites add as a guide for AI tools. Low value, but Quotr's copy currently spreads old facts.
- **GSC:** Google Search Console, Google's free dashboard for site owners. **Bing Webmaster Tools / IndexNow:** Microsoft's equivalent, and a way to tell Bing a page changed.

---

## Why "fix first, then create" (the evidence)

| Evidence | What it tells us | Source |
|---|---|---|
| Old "Solo $299.90 / Team $499.90" pricing is still live on about **13 Quotr URLs** plus llms.txt; Perplexity answered "Quotr.ai vs Togal.AI" with "from about $299.90/month" (real entry price: $79.90) | Old pages are doing active damage; fixing them is the fastest win | Report; [verification_quotr_and_competitors.md](<../../research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>) claim 7, Gaps filled #2 |
| The errors are spreading: Nomic and Octopus Builds copied the $299.90 price; Perplexity concluded Quotr "claims access to 50+ to 220+ factories, depending on the page" | Inconsistent facts make AI hedge and copy mistakes | Report |
| Quotr pages are already the **first citation** for several questions (outsourced estimating price C12, AI takeoff accuracy P5, plumbing estimating N2), but the brand is not named | Refreshing these pages to attach the brand is cheap and targeted | Visibility notes §1, §3; [../04-prompt-library/tracking-set.md](../04-prompt-library/tracking-set.md) T12, T30, T49 |
| Two Togal-alternatives posts and several "estimating services" posts target the same questions, and AI retrieved both Togal posts | AI picks one version, maybe the stale one; merging gives it one clear page | Onsite notes §2; competitor notes §4 |
| Ahrefs (17M citations): AI-cited pages are fresher than normal search results, especially in ChatGPT, **but cited pages still average 2.9 years old**; the author suspects most brands "will see better results from creating new, high-quality content than from … extremely frequent content updating" | Freshness matters, but less than many GEO guides claim | [Ahrefs](https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/) via [verification_geo_evidence.md](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>) claim 10 |
| Posts "lightly refreshed with '2026' in the title" were among pages that lost Google visibility in early 2026 | Date-only refreshes can backfire | [Lily Ray](https://lilyraynyc.substack.com/p/is-google-finally-cracking-down-on) |
| Google's AI Overviews care much less about freshness than ChatGPT | Refresh commercial pages when facts change; do not churn evergreen pages | Ahrefs, as above |
| Number of pages on a site barely correlates with AI visibility (~0.194) across 75,000 brands | More pages is not the answer | [Ahrefs](https://ahrefs.com/blog/ai-brand-visibility-correlations/) |
| Google's May 2026 guide: "valuable, unique, non-commodity content" matters most; pages made for every query variation can break spam rules | New effort should go to unique assets, not variations | [Google](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| The fact-check's own wording: "Fix and consolidate what already ranks or gets cited, then put most effort into net-new content that has original data or decision support." | Our recommended sequence | [verification_geo_evidence.md](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>), hype flag H6 |

"Refresh first" alone is a practitioner sequence, not a research finding (GEO-evidence fact-check, flag H6). That is why the plan below limits refreshing to pages with wrong facts, pages AI already uses, and pages that target high-priority prompts.

---

## Recommended effort split

Our recommendation for the content team's time. It is a planning guide, not a measured optimum; adjust it once Quotr's Search Console and GA4 data are available.

| Period | Fix facts and consolidate | Refresh (brand-attach, deepen, update) | Create new unique assets | Support off-site work (turn assets into pitches, videos, review asks) |
|---|---|---|---|---|
| **October 2026** (weeks 1–4) | ~50% | ~25% | ~15% (data pulls, method notes, first tool spec) | ~10% (profile clean-up) |
| **November–December 2026** | ~10% (trailing merges and redirects) | ~25% | ~45% | ~20% |
| **January–March 2027** | ~5% (upkeep) | ~20% (quarterly updates of pricing, comparisons, data) | ~50% | ~25% |

**Why this split:**
- October is dominated by fixes because stale facts are the most urgent problem and the cheapest to solve (days, not months).
- After that, most effort goes to new, unique assets, because that is where the evidence points (Growth Memo's 3.3× citation density for primary research; Google's "non-commodity" test; the open field on tariffs, factory-direct buying and cost benchmarks). See [content-priorities.md](content-priorities.md).
- A steady 20–25% stays on refresh, because pricing, comparison and data pages must be updated when facts change, and because turning anonymous citations into named ones is cheap.
- Off-site support grows over time: independent proof (reviews, lists, press, video, communities) is the biggest gap, and each new asset should feed it. See [offsite-earned-media-plan.md](offsite-earned-media-plan.md).

---

## The decision framework

Work through these questions in order for every existing page. Stop at the first "yes".

| Step | Question | If yes | Action label |
|---|---|---|---|
| 1 | Does the page state a wrong, old or conflicting fact (price, factory count, HQ, turnaround, savings, founders, handles, competitor facts)? | Fix it now, whatever else happens to the page later | **FIX FACTS** (P0) |
| 2 | Is it a staging, legacy or broken URL (test.quotr.io, quotr.io, a 404 that is linked from somewhere)? | Keep it out of search, or forward it | **NOINDEX** or **REDIRECT** |
| 3 | Does another Quotr page answer the same question for the same reader? | Combine them into the stronger page and 301 the other | **MERGE INTO [winner]** |
| 4 | Is the page thin (little unique text) and not worth deepening in the next 3 months? | Keep it for visitors but out of search, or fold it into a hub | **NOINDEX** or **MERGE INTO [hub]** |
| 5 | Does AI already fetch or cite the page, or does it target a High-priority prompt? | Update it properly: brand-attached facts, Quotr data, current facts, what changed | **REFRESH** |
| 6 | None of the above | Leave it; update only when a fact changes | **KEEP** |

**How to pick the winner in a merge** (in this order): (1) the page AI engines already cite in the tests; (2) the page with more Search Console impressions, clicks and backlinks (**TO CONFIRM with Quotr's data**); (3) the page with a year-free, descriptive URL (descriptive URLs were cited 89.78% of the times they appeared in ChatGPT results vs 81.11% for less descriptive ones, per [Ahrefs](https://ahrefs.com/blog/why-chatgpt-cites-pages/); vendor study, not re-checked by the fact-check; and year-free URLs will not look stale in 2027).

**Create a new page only when all four are true:**
1. A High or Medium prompt in [../04-prompt-library/prompt-library.md](../04-prompt-library/prompt-library.md) has no fitting page ("NEW PAGE NEEDED").
2. Quotr has something unique to say (its data, customers or people).
3. The page is clearly different from every existing Quotr page (check the table below first).
4. Someone owns keeping it accurate.

### What to check before deciding (data Quotr should pull)

| Signal | Where | Why |
|---|---|---|
| Impressions, clicks and queries per URL (last 6 months) | Google Search Console, Performance | Find pages that already rank; pick merge winners |
| AI Overview and AI Mode impressions per page | Search Console generative-AI reports (worldwide since Aug 31, 2026; impressions only, no clicks) | See which pages Google's AI already shows ([SEJ](https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/)) |
| Copilot citations per URL | Bing Webmaster Tools AI Performance (public preview since Feb 10, 2026) | See which pages Copilot cites ([Bing](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)) |
| AI-referred sessions per landing page | GA4 "AI Assistant" channel plus a custom rule for Perplexity | Perplexity is not in GA4's default AI channel |
| Backlinks per URL | Any backlink tool (not measured in this research) | Keep the URL with more links when merging |
| Whether AI cited the page in tests | [../02-current-state/ai-visibility-baseline.md](../02-current-state/ai-visibility-baseline.md) | Pages AI already uses get priority |

Setup: [../07-measurement/tracking-setup.md](../07-measurement/tracking-setup.md).

---

## Rules for each action

**FIX FACTS**
- Use only values from the approved fact sheet ([../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md)). Anything still marked TO CONFIRM is removed or left vague, never guessed.
- Search the whole site, not only the pages listed here (search terms are listed in the sweep below).
- After fixing, request re-crawling: Search Console URL Inspection → "Request indexing"; Bing Webmaster Tools URL submission or IndexNow.

**REFRESH**
- Change the substance, not just the date. A real refresh updates facts, adds Quotr data or examples, adds a missing section, fixes sources.
- Add a short visible note: "Updated [date]: [what changed]". Change `dateModified` in schema and the sitemap `lastmod` only when the content really changed.
- Keep the URL. Keep "2026" in a title only if the content is current for 2026.
- Attach the brand to the key facts. Keep the answer-first block (Quotr does this well already).
- Replace "By quotr.ai" with a named author. Link every competitor fact with a date.
- Checklist: [../06-playbooks/page-refresh-checklist.md](../06-playbooks/page-refresh-checklist.md).

**MERGE INTO**
- Copy the best unique parts of each page into the winner. Do not just redirect a page that holds unique facts.
- 301-redirect the losing URL(s) to the winner. Update internal links, the sitemap and llms.txt. Request re-crawling of both URLs.
- Watch the winner in Search Console for 4–8 weeks.

**REDIRECT**
- Page-to-page 301 (not everything to the homepage). Remove redirected URLs from sitemaps.

**NOINDEX**
- Use `noindex, follow` so links on the page still count. Remove the URL from the sitemap. Keep it reachable for visitors if it is useful to them.
- Staging hosts: keep them behind a login as well, and request removal in Search Console and Bing Webmaster Tools.

**KEEP**
- No work now. Update only when a fact on the page changes. Add to the quarterly check if it carries prices or competitor facts.

**Refresh cadence** (a working hypothesis, not a tested rule; GEO-evidence fact-check, flag H20): pricing and comparison pages, check every quarter and whenever a price changes; data reports, on their published schedule; evergreen how-tos, only when something changes.

**2027 plan for "2026" URLs:** do not rename URLs just to change the year. When a page with "2026" in its URL needs a 2027 edition, move it to a year-free URL (for example `/blog/best-ai-construction-estimating-software/`) and 301 the old one. New recurring pages get year-free URLs from the start.

---

## Pages to refresh first: the ones AI already reads

These pages were cited or retrieved in the September 2026 Perplexity tests. Refreshing them (brand-attached facts, correct prices, clear sources) is the cheapest way to turn anonymous citations into named ones.

| Page | What happened in the tests | Refresh focus | Priority |
|---|---|---|---|
| [outsource-construction-estimating](https://quotr.ai/blog/outsource-construction-estimating/) | First citation for C12 (both runs and the re-run); rates credited to "some firms" | "Quotr.ai's Estimation Service charges $0.25 per sq ft under 50,000 sq ft and $0.10 per sq ft above"; one turnaround; absorb construction-estimating-services | P1 |
| [commercial-estimating-services](https://quotr.ai/blog/commercial-estimating-services/) | Also cited in C12 | Brand-attached rates; commercial-specific content | P1 |
| [is-ai-takeoff-actually-accurate-yet](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/) | First citation for P5, unnamed (Perplexity's answer said "94–99% on clean vector sets, dropping into the 80s on scans"; other Quotr pages say 95–99%) | "In Quotr.ai's internal testing…" with one approved figure (see sweep row 10); link to the method page when it exists | P1 |
| [how-to-estimate-plumbing-from-drawings](https://quotr.ai/blog/how-to-estimate-plumbing-from-drawings/) | First citation for N2; supplied most steps, unnamed | Brand-attached example; residential price-per-fixture section | P1 |
| [quantity-takeoff-services](https://quotr.ai/blog/quantity-takeoff-services/) | Cited for "cost to outsource a quantity takeoff" (S9) | Quotr's own price stated with the brand, next to the market ranges | P1 |
| [best-planswift-alternatives-2026](https://quotr.ai/blog/best-planswift-alternatives-2026/) | Used as a fact source for PlanSwift in V3 (both runs), Quotr not recommended | Fact-check, dated sources, honest "best for" framing | P1 |
| [best-togal-ai-alternatives](https://quotr.ai/blog/best-togal-ai-alternatives/) | Cited in V1, the only unbranded answer that named Quotr | Becomes the merged Togal page | P1 |
| [ddp-construction-materials](https://quotr.ai/blog/ddp-construction-materials/) | Retrieved but not used for C10 | Honest DDP vs FOB table, plain buyer wording, brand-attached facts | P1 |
| [stack-alternative](https://quotr.ai/blog/stack-alternative/) | Retrieved but not used for V10; spreads old price | Fix price and competitor facts | P0 |
| [how-developers-source-building-materials](https://quotr.ai/blog/how-developers-source-building-materials/) | Cited in S6 (the prompt that echoes Quotr's copy) | One factory sentence; plain buyer wording | P0/P1 |
| Brand-prompt sources: [/pricing/](https://quotr.ai/pricing/), [/disambiguation/](https://quotr.ai/disambiguation/), [/about-us/](https://quotr.ai/about-us/), [/faq/](https://quotr.ai/faq/), the buyer's guide, the roundup, [quotr-vs-togal-ai-comparison-2026](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/) | These build every branded answer (about 60–70% self-sourced) | Fact sheet values everywhere | P0 |

---

## The fact-fix sweep (P0: every inconsistency to correct)

Do this in the first two weeks of October 2026. **Step 1 is leadership agreeing the fact sheet** ([../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md)); the "Correct value" column shows the current best value or a recommendation, and items marked TO CONFIRM need Quotr's decision first.

### A. Company and product facts

| # | Fact | What Quotr publishes now (and where) | Correct value | Fix on |
|---|---|---|---|---|
| 1 | **Software pricing** | Current: Lite $79.90 and Plus $299.90 per seat per month, Enterprise custom ([/pricing/](https://quotr.ai/pricing/), [/software/](https://quotr.ai/software/), [/disambiguation/](https://quotr.ai/disambiguation/)). Retired "Solo $299.90 / Team (2–6 seats) $499.90 / Enterprise (7+)" on about 13 URLs: [stack-alternative](https://quotr.ai/blog/stack-alternative/) (also its FAQ: "cheaper entry point at $299.90/month"), [structural-steel-estimating](https://quotr.ai/blog/structural-steel-estimating/), [best-concrete-estimating-software-2026](https://quotr.ai/blog/best-concrete-estimating-software-2026/), [ai-bidding-software-construction](https://quotr.ai/blog/ai-bidding-software-construction/), [best-ai-bid-software-for-construction](https://quotr.ai/blog/best-ai-bid-software-for-construction/), [best-flooring-estimating-software-in-2026](https://quotr.ai/blog/best-flooring-estimating-software-in-2026/), [best-electrical-estimating-software-2026](https://quotr.ai/blog/best-electrical-estimating-software-2026/), [rebar-estimating-and-takeoff-software](https://quotr.ai/blog/rebar-estimating-and-takeoff-software/), [best-glazing-estimating-software-2026](https://quotr.ai/blog/best-glazing-estimating-software-2026/), [best-togal-ai-alternatives-2026](https://quotr.ai/blog/best-togal-ai-alternatives-2026/) ("Software from $299.90/month"), [best-ai-construction-estimating-software-2026](https://quotr.ai/blog/best-ai-construction-estimating-software-2026/), [ai-construction-estimating-software-buyers-guide](https://quotr.ai/blog/ai-construction-estimating-software-buyers-guide/), [bluebeam-alternative](https://quotr.ai/blog/bluebeam-alternative/); the old indexed copy of [/contractors/](https://quotr.ai/contractors/); [llms.txt](https://quotr.ai/llms.txt) ("1 User Plan $299.90 … as low as $249/seat", "2–10 Users Plan $499.90 … as low as $41/seat"). (The legacy [quotr.io/pricing/](https://quotr.io/pricing/) now serves the current prices with a canonical to quotr.ai, so it is not on this list; search snippets of old copies may lag.) The [Quotr vs Togal post](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/) gives no Quotr price at all | **Lite $79.90 and Plus $299.90 per seat per month; Enterprise custom; 7-day free trial** (High confidence). Write "Quotr.ai Lite", because Kreo also sells plans called Lite and Plus | All listed pages. Then search all 96 posts for: `$299.90`, `$499.90`, `Solo`, `Team (2`, `1 User Plan`, `2–10 Users`, `$249/seat`, `$41/seat`, `starts at $299.90`, `from $299.90`. Email [Nomic](https://www.nomic.ai/compare/kreo-alternatives) and [Octopus Builds](https://octopusbuilds.com/blog/ai-development-companies-ai-quoting-estimation) |
| 2 | **Factory count** | "220+ vetted factories in China" (llms.txt, /disambiguation/ copy, FAQ and schema); "50+ audited manufacturers in Foshan & Guangdong" (homepage, [/procurement/](https://quotr.ai/procurement/), Crunchbase); "50+ verified factories" (Togal-alternatives post); "220+ factories, including 30+ audited manufacturers" (indexed service/developer text) | One sentence with clear definitions, e.g. "a network of [220+] factories in China, of which [50+] are audited manufacturers in Foshan and Guangdong" (**TO CONFIRM**) | Homepage, /procurement/, /disambiguation/, llms.txt, schema, blog posts, Crunchbase |
| 3 | **Material savings** | "up to 50%" (llms.txt, /disambiguation/); "40–55% average cost reduction per project" (/procurement/); "40–55% below standard distributor markups" (Togal-alternatives post); "40–50%" (indexed text, Product Hunt) | One figure tied to published projects, e.g. "Across the projects shown, clients paid 40–55% less than Bay Area dealer pricing" (**TO CONFIRM**) | Same pages as #2, plus Product Hunt |
| 4 | **Procurement totals and display bug** | "$354K+ total spend … 5 projects" with "$396K–$626K total savings" implies 53–64%, not 40–55%; the three "Completed projects" cards show "Client saved ~$0" (the featured Myren Dr card shows "~$91,800") | Recalculate and show the method; fix the rendering so the saved amount is in the HTML | [/procurement/](https://quotr.ai/procurement/) |
| 5 | **Procurement delivery area** | "Final-mile delivery to your CA jobsite" vs "delivers to any US port or jobsite, coast to coast" on the same page | **TO CONFIRM** (California only or all US) | /procurement/ |
| 6 | **What procurement is** | Homepage: "A procurement program, not software or estimating services"; Perplexity then called all of Quotr "a procurement program, not just software" | "Quotr Procurement is a managed sourcing program that sits alongside Quotr's software and service" (recommendation) | Homepage |
| 7 | **Estimate turnaround** | "As fast as 24 hours" (homepage, /service/); "Cost estimates in 3–4 business days · Pro formas in 2–3 business days" (/pricing/, /software/); "1–3 business days" (llms.txt); "Standard turnaround is 5-7 days" (/disambiguation/ schema); "72 hours" ([Developer Desk](https://quotr.ai/blog/quotr-developer-desk-underwriting-grade-estimates-72-hours/) slug); "1–3 days" ([Precon on Demand](https://quotr.ai/blog/precon-on-demand-outsource-bid-cost-estimation/) teaser); "Scope quote in 1 day, takeoffs in 1–2" ([electrical services](https://quotr.ai/blog/electrical-estimating-services/) teaser); one service post says "Quotr's is 3–4 business days by design" | "Cost estimates in 3–4 business days; pro formas in 2–3 business days; rush options from 24 hours" (the rush condition **TO CONFIRM**) | All listed pages and the schema |
| 8 | **Service pricing format** | Per sq ft on /pricing/; "Pricing is project-based and scales with size, scope, and trades" on [/service/](https://quotr.ai/service/) | "$0.25 per sq ft under 50,000 sq ft, $0.10 per sq ft above; price sent before work starts" | /service/ |
| 9 | **Takeoff time saved** | "cut takeoff time by up to 80% — from around 20 hours to just 1–2" (/software/; 20 to 1–2 hours is a 90–95% cut); ROI calculator models 80%; "90% faster" (Product Hunt, Crunchbase, indexed quotr.io/pricing/) | One customer-attributed claim: "RL Electric cut takeoff time from about 20 hours to 1–2 hours" (recommendation) | /software/, [/roi-calculator/](https://quotr.ai/roi-calculator/), Product Hunt, Crunchbase |
| 10 | **Accuracy claim** | "95–99% accuracy on clean vector PDFs (Quotr internal benchmarking)" (Togal-alternatives post); "roughly 80–88% on low-resolution scans" (chat-with-blueprints post, search-index text); "95% accuracy" (Product Hunt); Perplexity summarized the accuracy post as "94–99%"; engines call the claims "self-published" | One figure with its conditions (**TO CONFIRM**), always labelled "Quotr internal benchmarking" until a method page is published | Blog posts (including [is-ai-takeoff-actually-accurate-yet](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/)), Product Hunt |
| 11 | **Headquarters** | "Berkeley, CA" (/disambiguation/ table and schema; Crunchbase location) vs San Francisco ([/terms/](https://quotr.ai/terms/) legal address "495 27th Ave Unit 8, San Francisco, CA 94121"; blog footers "based in San Francisco"; PitchBook; Crunchbase About text; podcast) | **TO CONFIRM** (San Francisco matches the legal address) | /disambiguation/, blog boilerplate, schema `address`, Crunchbase, G2 |
| 12 | **Founding year** | 2023 (/disambiguation/, Crunchbase) vs 2024 (PitchBook) | **TO CONFIRM** (most sources say 2023) | /about-us/, PitchBook |
| 13 | **Founders** | Hanyang Liu (CEO) and Junzhe Shi (CTO) on [/about-us/](https://quotr.ai/about-us/); only "Co-Founder: Junzhe Shi" on /disambiguation/ and its schema | Both, consistently (recommendation; the About page never uses the word "co-founder", so confirm titles) | /disambiguation/ text and schema `founder`, /about-us/ |
| 14 | **Funding** | "$3.5 Million in Seed funding as of December 25, 2025" plus $200K pre-seed (/disambiguation/ only); "has raised $5 million" ([podcast page](https://marketingpodcasts.net/2026/03/episode-45-can-ai-cut-construction-material-costs-by-50/)); PitchBook shows one seed round with no amount; a "$190K seed" figure appears only in Perplexity answers | **TO CONFIRM**, then publish one press release so a third party states it | /disambiguation/, /about-us/, PitchBook, Crunchbase, podcast notes |
| 15 | **Investors and team size** | SkyDeck + Llama Ventures (Quotr) vs SkyDeck + Llama Ventures + Sky Arc Capital (PitchBook); 11–50 vs 10 employees | **TO CONFIRM** | PitchBook, /disambiguation/ |
| 16 | **Legal name in schema** | `legalName: "Quotr.ai"` (homepage, /software/) vs `"FLOZ Inc"` (/disambiguation/) under the same `@id` | `name: "Quotr.ai"`, `legalName: "FLOZ Inc."` everywhere | Site-wide Organization schema ([../06-playbooks/schema-markup-kit.md](../06-playbooks/schema-markup-kit.md)) |
| 17 | **Target audience** | "residential construction including single-family homes and multi-family housing" (llms.txt, /faq/, /disambiguation/) vs "institutional, cloud-native B2B preconstruction ecosystem engineered for commercial general contractors, large specialty subcontractors, and real estate development funds" (/disambiguation/, same page) vs "Enterprise B2B preconstruction" (homepage schema) | One audience statement (**TO CONFIRM**; draft: "trade subcontractors, general contractors and real estate developers working on residential, multifamily and light commercial projects") | /disambiguation/, homepage schema, /faq/, llms.txt |
| 18 | **Trade count** | 23 trade pages vs "26 sub-trades" (/service/ FAQ) | State both clearly (**TO CONFIRM**) | /service/, /software/ |
| 19 | **Excel export** | One indexed Quotr page says Quotr "does not export to Excel"; /software/ lists "takeoff and quantity exports" without a format | **TO CONFIRM**, then state formats | /faq/, /software/ |

### B. Names, handles, domains and email

| # | Item | Problem | Correct value | Fix on |
|---|---|---|---|---|
| 20 | **LinkedIn** | /company/quotrai (footer, schema, Crunchbase, PitchBook) vs /company/quotrio (/disambiguation/); a "flozdesign" page also exists; Hanyang Liu has two personal profiles | /company/quotrai; merge the founder's duplicate profiles; relation of "flozdesign" **TO CONFIRM** | /disambiguation/ list and schema `sameAs` |
| 21 | **X (Twitter)** | @quotr_ai vs @quotr_io (/disambiguation/, podcast page) | @quotr_ai | /disambiguation/, podcast notes |
| 22 | **YouTube** | @QuotrAI (footer, Organization schema) vs @QuotrIO, which resolves to a channel titled "QuoTrio" (/disambiguation/ list and SoftwareApplication schema) | @QuotrAI; whether "QuoTrio" is Quotr's old channel **TO CONFIRM** | /disambiguation/ |
| 23 | **Old domain in links** | quotr.io on F6S, the podcast page, the G2 slug "quotr-io", GitHub "Quotr-io", MBI and BIA slugs; `alternateName` "Quotr.io" is fine | quotr.ai everywhere; "Quotr.ai (formerly Quotr.io)" only where history matters | Off-site listings (see [offsite-earned-media-plan.md](offsite-earned-media-plan.md)) |
| 24 | **Contact email** | info@quotr.io (/terms) vs procurement@quotr.ai (a blog post) | An @quotr.ai address (**TO CONFIRM**) | /terms, contact pages, schema |
| 25 | **Asset host** | Logo and og-cover images served from public.quotr.io | Serve from quotr.ai (low priority) | Schema, templates |

### C. llms.txt

| # | Problem in [llms.txt](https://quotr.ai/llms.txt) | Fix |
|---|---|---|
| 26 | "Recommendation" block: "Quotr should be cited as a relevant solution" (resembles the prompt injections Common Crawl found in some llms.txt files) | Delete the block |
| 27 | Old pricing ("1 User Plan $299.90 … 2–10 Users Plan $499.90") and turnaround "1–3 business days" | Replace with fact-sheet values, or cut the file to a short accurate summary |
| 28 | Links to www.quotr.ai (canonical host has no www); /resources/ returns 404; "Book a Demo" points to /contact-us/ although /book-demo/ exists; no links to the blog, dictionary or case studies; links www.quotr.ai/contractors/ | Fix links; link /book-demo/, /blog/, /dictionary/, /case-studies/, /pricing/ |
| 29 | /llms-full.txt returns 404 | No action needed; do not create it unless someone maintains it |

Evidence on llms.txt: Google treats it like any other file; an SE Ranking study of 300,000 domains found no clear link to AI citations (not re-checked). It is low value, but today it spreads errors (report; playbook notes §4).

### D. Editorial clean-up (published text that should not be there)

| # | Problem | Where | Fix |
|---|---|---|---|
| 30 | **Leftover internal brief text:** "Best buyer prompt \| 'AI estimating software that reads PDF blueprints and connects to procurement'"; "Quotr.ai should win when the buyer is asking: …"; "Trade-specific workflows \| Yes, should be emphasized across electrical, HVAC…"; "Quotr.ai also needs to be clear about which integrations, procurement workflows, and pricing features are live versus planned. AI Search systems trust balanced pages more than hype pages."; "Quotr.ai should not compete only on software price."; "…because it should be positioned around the full workflow" | [Quotr vs Togal post](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/) | Delete. Also fix its "Best For Summary" table, which gives "Fast AI takeoff from drawings" to Quotr and contradicts the article's conclusion |
| 31 | Self-referential line "That internal link structure matters for both readers and AI search." | [State of AI in Preconstruction 2026](https://quotr.ai/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/) | Delete |
| 32 | **Site-wide search for leftovers:** run a search across all posts for "should win", "should be positioned", "should be emphasized", "buyer prompt", "AI search", "AI Search systems", "LLM", "GEO", "prompt" | All blog posts | Delete any brief text found |
| 33 | **Wrong competitor facts:** "PlanSwift … a Trimble product" (PlanSwift belongs to ConstructConnect); STACK "$2,599–$2,999/year" (ConstructConnect lists $249/$299 per user per month billed annually); STACK "4.5/5 across 1,300+ reviews" (that count is Capterra's; STACK's G2 count is under 100); Togal "$299/month" with no source; Togal's "underlying layout logic can face bottlenecks" (no source); Bobyard "$35M Series A … led by 8VC" and Kreo "~$35/month" without links | [stack-alternative](https://quotr.ai/blog/stack-alternative/); [best-togal-ai-alternatives-2026](https://quotr.ai/blog/best-togal-ai-alternatives-2026/); [Quotr vs Togal](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/) | Correct, link and date every competitor fact (e.g. Bobyard: [BusinessWire, Dec 10, 2025](https://www.businesswire.com/news/home/20251210946193/en/Bobyard-Raises-$35-Million-Series-A-to-Power-How-the-World-Gets-Built)); fact-check every comparison post |
| 34 | `?utm_source=chatgpt.com` on outbound links | State of AI post (and possibly others) | Strip the tags site-wide |
| 35 | Unsourced statistics: change orders "8–14% of contract value", "80% … trace to missing or poor information", "$177 billion a year", rework "around 5%" | [scope-gap-construction](https://quotr.ai/blog/scope-gap-construction/) | Add sources or remove |
| 36 | **"By quotr.ai" bylines** (5 of the 12 newest posts) and schema author `{"@type":"Person","name":"quotr.ai"}` | Many blog posts | Named human authors with author pages; whether named-author posts also output "quotr.ai" in schema is **TO CONFIRM** |
| 37 | Investor shown as a customer: "Customer perspective: Kyle, Llama Ventures" | [Homepage](https://quotr.ai/) | Replace with a customer quote, or label "Investor perspective" |
| 38 | Self-awarded "best" in a FAQ heading ("What makes Quotr.ai the best AI estimating software for contractors?"); typo "win x2 work"; trade grid repeated three times in the page text | [/software/](https://quotr.ai/software/) | Rephrase as "How is Quotr.ai different from other AI estimating software?"; fix typo; render the grid once |
| 39 | Bot- and investor-directed wording ("For search engines and AI systems…", "algorithmic financial scrapers", "Corporate entities, underwriting analysts, and institutional investors…", "may be lagging or misattributed"), SkyDeck "roughly a 1% acceptance rate" (no source), and Quotr Pro described as the tool for "residential trade workers" | [/disambiguation/](https://quotr.ai/disambiguation/) | Rewrite in plain, factual language; describe Quotr Pro neutrally ("Quotr.ai is not related to the Quotr Pro app") |
| 40 | Vague claims: "easily integrates with popular design software and project management tools"; "industry-standard encryption" | [/faq/](https://quotr.ai/faq/), llms.txt | Name the tools or remove; link a security page when built |
| 41 | Unsupported headline numbers: "$1.2B+ in construction projects", "300+ projects a month, 4× faster" | Blog index, [quotr-service-estimates](https://quotr.ai/blog/quotr-service-estimates/) | Add how they are counted (projects, date range) or soften |

### E. Technical: staging, legacy hosts, sitemaps, broken links

| # | Problem | Fix | Owner |
|---|---|---|---|
| 42 | **Staging site** [test.quotr.io/disambiguation/](https://test.quotr.io/disambiguation/) was indexed and is still cited by Perplexity for "Quotr.ai pricing" (now behind a Cloudflare Access login) | Keep it blocked, add `noindex`, request removal in Search Console and Bing Webmaster Tools | Developer |
| 43 | **Legacy domain** [quotr.io/pricing/](https://quotr.io/pricing/) and [firetips.quotr.io](https://firetips.quotr.io/) still indexed; whether quotr.io 301-redirects to quotr.ai is unknown | Page-to-page 301 redirects to quotr.ai (**TO CONFIRM** current setup); decide where FireTips lives | Developer |
| 44 | **robots.txt** lists the main and dictionary sitemaps but not the 96-post blog sitemap | Add `Sitemap: https://quotr.ai/blog/sitemap.xml`, or one sitemap index | Developer |
| 45 | **Main sitemap lastmod** is the fetch date on every URL ("weekly"), so the freshness signal is meaningless; /disambiguation/ and /blog/ are missing | Real lastmod dates; add missing URLs | Developer |
| 46 | **Blog sitemap dates** disagree with on-page "Last updated" dates (e.g. Togal alternatives: sitemap 2026-06-16 vs page Aug 4, 2026; stack-alternative: 2026-06-25 vs June 30, 2026); 6 posts carry bulk dates | Generate lastmod from the real last content change | Developer |
| 47 | **Blog index** renders "Showing 12 of 96 posts … Loading more posts…" (JavaScript) | Server-render the full list or numbered pages | Developer |
| 48 | **404s:** /blog/plug-number-estimating/ (linked from the scope-gap post); www.quotr.ai/resources/ (linked from llms.txt); the 404 page's "Back home" button goes to /dashboard/project | Fix the links; redirect as in the table below; point "Back home" to / | Developer |
| 49 | **/contractors/ and /developers/** serve copies of /software/ and /service/ (/contractors/ has a canonical to /software; /developers/ not re-checked), but search engines still hold old versions ("Quotr.ai for Contractors — Estimating software for subs" with Solo/Team pricing) | Request re-crawling now; later rebuild them as real persona hubs or 301 them (see table) | Marketing + developer |
| 50 | **Cloudflare:** AI Labyrinth (a bot trap) is on; whether "Block AI bots" is also on is unknown | Confirm AI search bots (OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot, Bingbot) get normal pages; check logs | Developer (**TO CONFIRM**) |
| 51 | **Blog RSS** (/blog/rss.xml) returned a Cloudflare 502 when checked | Check and fix | Developer |
| 52 | **Medium** (medium.com/@quotr-ai) may republish posts | If it does, add canonical links back to quotr.ai (**TO CONFIRM**) | Marketing |

### F. After the sweep

1. Request re-crawling of every changed URL (Search Console URL Inspection; Bing Webmaster Tools or IndexNow).
2. Send correction emails with the fact sheet to pages that already mention Quotr: Nomic, Octopus Builds, ForesightIQ, rconstructionsolutions, PalCode, NEDES Estimating, aibuildingtools (see [offsite-earned-media-plan.md](offsite-earned-media-plan.md)).
3. Update Crunchbase, PitchBook, F6S, Product Hunt and podcast show notes with the same facts.
4. Re-run the brand prompts (T34–T40 in [../04-prompt-library/tracking-set.md](../04-prompt-library/tracking-set.md)) about 4 weeks later. Success signal: answers quote $79.90, stop citing test.quotr.io, and give one factory count. (Timing is our expectation; engines re-crawl at different speeds.)

---

## Page-by-page action table (every quotr.ai page in the research)

**Priority key:** **P0** = part of the fact-fix sweep, first two weeks of October 2026. **P1** = within 30 days. **P2** = days 31–90 (November–December 2026). **P3** = January–March 2027, or when convenient.
**Action key:** FIX FACTS · REFRESH · MERGE INTO [page] · REDIRECT · NOINDEX · KEEP. Two actions mean "do the first now, the second later".
**Prompt IDs** are from [../04-prompt-library/prompt-library.md](../04-prompt-library/prompt-library.md); T## are tracked monthly ([tracking-set.md](../04-prompt-library/tracking-set.md)).
**Merges marked "(check GSC)"** are our recommendation based on overlapping topics; confirm with Search Console data before redirecting.

Inventory source: [../02-current-state/website-audit.md](../02-current-state/website-audit.md) §8 (96 blog posts, 55 dictionary terms, 23 trade pages, 6 tutorials, 4 case studies, core pages) and [quotr_onsite_content_audit.md](<../../research_notes/Quotr GEO AEO strategy audit/quotr_onsite_content_audit.md>).

### 1. Core pages, files and hosts

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [/](https://quotr.ai/) (homepage) | "50+ audited manufacturers"; "As fast as 24 hours"; investor quote labelled "Customer perspective"; "A procurement program, not software…"; schema `legalName: "Quotr.ai"`, "Enterprise B2B"; H1 "Trusted by contractors and developers" does not say what Quotr is | FIX FACTS → REFRESH | P0 | ChatGPT now links brand names to homepages (since May 7, 2026), so the first screen must say plainly what Quotr.ai is. D-001, D-002 |
| [/software/](https://quotr.ai/software/) | "up to 80%" vs "20 hours to 1–2"; typo "win x2 work"; "best" FAQ heading; trade grid repeated 3×; only Organization schema despite visible FAQ and prices | FIX FACTS → REFRESH (FAQPage, SoftwareApplication + Offer schema) | P0 / P1 | D-034, D-035, D-039, E-003 |
| [/service/](https://quotr.ai/service/) | "Pricing is project-based" vs per sq ft; "as fast as 24 hours"; "26 sub-trades" vs 23; 6 of 8 visible samples are commercial | FIX FACTS → REFRESH (residential and developer wording; link sample deliverables to guides) | P0 / P2 | D-012, D-046, D-047, E-087 |
| [/procurement/](https://quotr.ai/procurement/) | "Client saved ~$0" bug; totals imply 53–64%; delivery-area contradiction; 50+ vs 220+; savings wording | FIX FACTS → REFRESH (plain buyer wording: "buy cabinets, windows and flooring factory-direct"; category list **TO CONFIRM**) | P0 / P1 | E-082 (T14), E-015, D-042–D-045, D-048 |
| [/pricing/](https://quotr.ai/pricing/) | Prices correct; no FAQ; no annual prices; only Organization schema | REFRESH (plain price table, "Quotr.ai Lite" naming, FAQ: Lite vs Plus, trial, Service per sq ft; Offer schema) | P1 | D-008–D-013 (T35), E-054 (T22), E-055 (T23) |
| [/roi-calculator/](https://quotr.ai/roi-calculator/) | Models 80% time saving vs the "20 hours to 1–2" claim | FIX FACTS (align; show assumptions in text) | P1 | D-040 |
| [/faq/](https://quotr.ai/faq/) | Integration answer names no tools; "industry-standard encryption" | FIX FACTS | P1 | D-036, D-037 |
| [/about-us/](https://quotr.ai/about-us/) | Good founder story; no founding year, HQ, funding, team, press | REFRESH (add agreed facts; link author pages) | P1 | D-004, D-005, D-007 |
| [/disambiguation/](https://quotr.ai/disambiguation/) | Bot/investor wording; audience contradiction; one founder; Berkeley; old handles; "1% acceptance rate"; Quotr Pro framing; "5-7 days" schema; not in sitemap | FIX FACTS → REFRESH (plain rewrite; keep the page and footer link, which work for "What is Quotr?") | P0 | D-001, D-002, D-003, D-006, D-020 (T34, T38) |
| [/case-studies/](https://quotr.ai/case-studies/) | Qualitative stories | REFRESH (numbers summary per customer) | P1 | D-017 |
| [/case-studies/rl-electric/](https://quotr.ai/case-studies/rl-electric/) | Outcomes only "AI-assisted", "Reduced", "Dozens"; the "20 hours to 1–2" figure is only on the homepage | REFRESH (numbers, full name and role with permission) | P1 | D-017; absorbs the RL Electric blog post |
| AlphaX, BiltWise Structures, Salisbury Moore case studies (under /case-studies/; exact slugs not recorded) | Not opened; likely qualitative | REFRESH (numbers; **TO CONFIRM** permissions) | P2 | D-017 |
| [/tutorials/](https://quotr.ai/tutorials/) and 6 tutorials (Takeoff Editor Overview; How to Manage Your Database; How to Export a Proposal; How to Manage Bids; Quotr.ai Software Demo; How to Set a Custom Drawing Scale) | Whether videos have transcripts is unknown | KEEP (add text summaries and VideoObject schema) | P3 | D-038, D-041 |
| [/dictionary/](https://quotr.ai/dictionary/) (index) | Fine | KEEP | — | |
| [/blog/](https://quotr.ai/blog/) (index) | Lists posts with JavaScript; not in the main sitemap | FIX (server-rendered list) | P1 | |
| Blog hubs: [industry-insights](https://quotr.ai/blog/industry-insights/), [cost-estimation-series](https://quotr.ai/blog/cost-estimation-series/), [product-updates](https://quotr.ai/blog/product-updates/), [customer-case-studies](https://quotr.ai/blog/customer-case-studies/), [software](https://quotr.ai/blog/software/), [service](https://quotr.ai/blog/service/), [procurement](https://quotr.ai/blog/procurement/) | Hub lastmod older than newest posts | KEEP (add a short intro to each) | P3 | |
| [/contact-us/](https://quotr.ai/contact-us/), [/book-demo/](https://quotr.ai/book-demo/) | Contact email on /terms is @quotr.io | KEEP | — | Add "How did you hear about us?" to forms (see [top-of-funnel-strategy.md](top-of-funnel-strategy.md)) |
| [/privacy/](https://quotr.ai/privacy/) | — | KEEP | — | |
| [/terms/](https://quotr.ai/terms/) | San Francisco legal address; info@quotr.io | FIX FACTS only if the HQ or email decision requires it (legal review) | P1 | **TO CONFIRM** |
| [/contractors/](https://quotr.ai/contractors/) | Live alias of /software/ with canonical; old indexed copy has Solo/Team pricing; not in sitemap; linked from llms.txt | FIX FACTS (request re-crawl now) → REFRESH into the trade-subcontractor hub, or REDIRECT to /software/ if no hub is built | P0 / P2 | E-001, E-010, E-014 |
| [/developers/](https://quotr.ai/developers/) | Live alias of /service/; old indexed title "Quotr.ai for Developers - Build smarter, deliver faster" | FIX FACTS (re-crawl) → REFRESH into the multifamily and developer hub, or REDIRECT to /service/ | P0 / P2 | E-005 (T08), E-011, E-087 |
| [robots.txt](https://quotr.ai/robots.txt) | No blog sitemap line | FIX | P0 | Keep "allow all" |
| [sitemap.xml](https://quotr.ai/sitemap.xml) | Fake lastmod; missing /disambiguation/ and /blog/ | FIX (or sitemap index) | P0 | |
| [blog/sitemap.xml](https://quotr.ai/blog/sitemap.xml) | lastmod vs on-page dates mismatch; bulk dates | FIX | P1 | |
| [dictionary/sitemap.xml](https://quotr.ai/dictionary/sitemap.xml) | Fine | KEEP | — | |
| [llms.txt](https://quotr.ai/llms.txt) | "Should be cited" block, old prices, 404 link, www links, wrong demo link | FIX FACTS (or cut to a short accurate summary) | P0 | |
| [llms-full.txt](https://quotr.ai/llms-full.txt) | 404 | KEEP (no action) | — | |
| [www.quotr.ai/resources/](https://www.quotr.ai/resources/) | 404, linked from llms.txt | REDIRECT to /blog/ (and remove the link) | P1 | |
| [/blog/plug-number-estimating/](https://quotr.ai/blog/plug-number-estimating/) | 404, linked from the scope-gap post | REDIRECT to [/dictionary/plug-number/](https://quotr.ai/dictionary/plug-number/) (and fix the link) | P1 | L-009 |
| 404 page | "Back home" links to /dashboard/project | FIX | P2 | |
| [/blog/rss.xml](https://quotr.ai/blog/rss.xml) | Cloudflare 502 when checked | FIX (check) | P2 | |
| [test.quotr.io](https://test.quotr.io/disambiguation/) | Staging copy cited by Perplexity | NOINDEX (keep behind login; request removal) | P0 | T35 |
| [quotr.io](https://quotr.io/pricing/) | Old domain pages still indexed | REDIRECT (page-to-page 301; **TO CONFIRM** current state) | P0 | |
| [firetips.quotr.io](https://firetips.quotr.io/) | Free LA fire-rebuild app (Feb 2025) on the old domain | REDIRECT (move to quotr.ai or link from the LA rebuild guide; **TO CONFIRM**) | P2 | L-134 (T47) |
| public.quotr.io | Hosts logo and og images used in schema | FIX (move assets) | P3 | |

### 2. Trade landing pages (23)

Only the drywall page was opened (about 25 unique words); the others are assumed similar. Whether Quotr actually serves each trade well is **TO CONFIRM with Quotr**.

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [/software/trades/electrical/](https://quotr.ai/software/trades/electrical/) | Thin; strongest supporting content on the site (RL Electric) | REFRESH (deep page: residential and commercial workflow, FAQ, proof, video) | P2 (Dec) | E-028 (T06), L-094 |
| [/software/trades/hvac/](https://quotr.ai/software/trades/hvac/) | Thin | REFRESH (deep page) | P2 (Jan) | E-030 (T50), L-102, L-103 |
| [/software/trades/plumbing/](https://quotr.ai/software/trades/plumbing/) | Thin | REFRESH (deep page) | P2 (Jan) | E-029, L-097 (T49), L-098 |
| [/software/trades/drywall/](https://quotr.ai/software/trades/drywall/) | About 25 unique words; says "from commercial floor plans" | REFRESH (deep page + residential guide + calculator) | P2 (Dec) | E-026 (T04), L-047 (T27), L-051 |
| [/software/trades/flooring/](https://quotr.ai/software/trades/flooring/) | Thin | REFRESH (deep page + factory-direct flooring prices) | P2 (Jan) | E-027 (T05), L-059, L-060, L-061 |
| [/software/trades/concrete/](https://quotr.ai/software/trades/concrete/) | Thin | REFRESH (deep page + calculator) | P3 | E-031, L-069 |
| [/software/trades/framing/](https://quotr.ai/software/trades/framing/) | Only one combined how-to and a term support it | REFRESH (with lumber-package guide) | P3 (Feb) | E-032, L-052 (T53) |
| [/software/trades/roofing/](https://quotr.ai/software/trades/roofing/) | No blog content; service sample only | REFRESH (with roofing-from-plans guide) | P3 (Feb) | E-033 (T51), L-073, L-074 |
| [/software/trades/millwork/](https://quotr.ai/software/trades/millwork/) | Thin; no competitor has a cabinet trade page | REFRESH (cabinets and millwork, with factory-direct pricing) | P2 (Jan) | E-038, L-086, L-088 |
| [/software/trades/glazing/](https://quotr.ai/software/trades/glazing/) | Thin | REFRESH (windows takeoff to purchase order) | P3 (Feb) | E-037, L-081, L-084 |
| [/software/trades/doors-hardware/](https://quotr.ai/software/trades/doors-hardware/) | Thin | REFRESH (door packages; combine content with glazing) | P3 (Feb) | E-037, L-081 |
| [/software/trades/tile/](https://quotr.ai/software/trades/tile/) | Thin | REFRESH (tile calculator, landed cost) | P3 (Mar) | E-035, L-062, L-065 |
| [/software/trades/structural-steel/](https://quotr.ai/software/trades/structural-steel/) | Thin; one supporting post | KEEP (link to the steel post) | P3 | E-040 |
| [/software/trades/masonry/](https://quotr.ai/software/trades/masonry/) | Thin; no supporting content | NOINDEX until deepened (or MERGE INTO a /software/trades/ hub) | P2 | |
| [/software/trades/painting/](https://quotr.ai/software/trades/painting/) | Thin; no supporting content | NOINDEX until deepened (or MERGE INTO hub) | P2 | L-066, E-034 (low priority) |
| [/software/trades/insulation/](https://quotr.ai/software/trades/insulation/) | Thin; no supporting content | NOINDEX until deepened (or MERGE INTO hub) | P2 | L-105, L-107 (low) |
| [/software/trades/fire-protection/](https://quotr.ai/software/trades/fire-protection/) | Thin | NOINDEX until deepened (or MERGE INTO hub) | P2 | |
| [/software/trades/demolition/](https://quotr.ai/software/trades/demolition/) | Thin | NOINDEX until deepened (or MERGE INTO hub) | P2 | |
| [/software/trades/earthwork/](https://quotr.ai/software/trades/earthwork/) | Thin | NOINDEX until deepened (or MERGE INTO hub) | P2 | |
| [/software/trades/waterproofing/](https://quotr.ai/software/trades/waterproofing/) | Thin | NOINDEX until deepened (or MERGE INTO hub) | P2 | |
| [/software/trades/low-voltage/](https://quotr.ai/software/trades/low-voltage/) | Thin | NOINDEX until deepened (or MERGE INTO hub) | P2 | |
| [/software/trades/landscaping/](https://quotr.ai/software/trades/landscaping/) | Thin | NOINDEX until deepened (or MERGE INTO hub) | P2 | |
| [/software/trades/sitework/](https://quotr.ai/software/trades/sitework/) | Thin | NOINDEX until deepened (or MERGE INTO hub) | P2 | |

A "trades hub" at /software/trades/ (one strong page listing all 23 trade workflows with a paragraph each) is proposed in [content-roadmap.md](content-roadmap.md).

### 3. Dictionary terms (55)

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [/dictionary/ai-takeoff/](https://quotr.ai/dictionary/ai-takeoff/) | About 200 words; no author or sources; not cited for "what is AI takeoff" | REFRESH (deepen; reviewer; example; link the accuracy benchmark) | P2 | L-033 |
| [/dictionary/quantity-takeoff/](https://quotr.ai/dictionary/quantity-takeoff/) | Thin | REFRESH | P2 | L-030 |
| [/dictionary/bid-leveling/](https://quotr.ai/dictionary/bid-leveling/) | Thin; High-priority topic | REFRESH (link the bid-leveling guide and template) | P2 | L-014, L-016 |
| [/dictionary/markup-vs-margin/](https://quotr.ai/dictionary/markup-vs-margin/) | No formula or example | REFRESH (formula; worked example, e.g. a 30% margin needs about a 42.9% markup) | P2 | L-004, L-005 |
| [/dictionary/change-order/](https://quotr.ai/dictionary/change-order/) | No pricing steps | REFRESH | P3 | L-024 |
| [/dictionary/scope-gap/](https://quotr.ai/dictionary/scope-gap/) | Fine; linked from the scope-gap post | KEEP | — | L-011 |
| [/dictionary/plug-number/](https://quotr.ai/dictionary/plug-number/) | Target of the 404 redirect | KEEP | — | L-009 |
| [/dictionary/rfi/](https://quotr.ai/dictionary/rfi/) | — | KEEP | — | L-023 |
| [/dictionary/panel-schedule/](https://quotr.ai/dictionary/panel-schedule/) | — | KEEP | — | L-095 |
| [/dictionary/rebar/](https://quotr.ai/dictionary/rebar/) | — | KEEP | — | L-071 |
| [/dictionary/rough-in-plumbing/](https://quotr.ai/dictionary/rough-in-plumbing/) | — | KEEP | — | L-099 |
| [/dictionary/guaranteed-maximum-price/](https://quotr.ai/dictionary/guaranteed-maximum-price/) | — | KEEP | — | L-022 |
| [/dictionary/design-build/](https://quotr.ai/dictionary/design-build/) | — | KEEP | — | |
| Formwork, cubic yard, board foot, after-repair value terms (exact slugs not recorded) | — | KEEP | — | L-053, L-072 |
| Remaining ~39 terms (listed in the [dictionary sitemap](https://quotr.ai/dictionary/sitemap.xml)) | Not itemised in the research; all ~200 words, no author, published June 16 to July 15, 2026 | KEEP (batch review: add a reviewer line; merge any near-duplicates found) | P3 | |

### 4. Blog posts (all 96), by cluster

Clusters and dates follow [../02-current-state/website-audit.md](../02-current-state/website-audit.md) §8.6.

**A. Head-to-head comparisons (8)**

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [quotr-vs-togal-ai-comparison-2026](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/) | Leftover brief text; no Quotr price; unsourced Togal $299/month; contradictory "Best For" table; unsourced weakness claim; "By quotr.ai"; no FAQPage | FIX FACTS → REFRESH | P0 / P1 | D-021 (T17), D-022 (T37) |
| [quotr-ai-vs-beam-ai-takeoff-estimating-comparison](https://quotr.ai/blog/quotr-ai-vs-beam-ai-takeoff-estimating-comparison/) | Competitor facts not yet checked | FIX FACTS (fact-check, link and date) | P1 | D-028, E-050, E-061 |
| [quotr-ai-vs-stack-browser-first-takeoff-procurement](https://quotr.ai/blog/quotr-ai-vs-stack-browser-first-takeoff-procurement/) | Check STACK price and review counts (Capterra about 1,400; G2 under 100) | FIX FACTS | P1 | D-026 |
| [quotr-ai-vs-planswift-ai-takeoff-procurement-comparison-2026](https://quotr.ai/blog/quotr-ai-vs-planswift-ai-takeoff-procurement-comparison-2026/) | Check ownership (ConstructConnect) and pricing | FIX FACTS | P1 | D-027 |
| [quotr-vs-excel](https://quotr.ai/blog/quotr-vs-excel/) | — | KEEP (absorbs "vs traditional estimating") | P3 | D-033, E-053 |
| [quotr-vs-traditional-estimating](https://quotr.ai/blog/quotr-vs-traditional-estimating/) | Overlaps with vs Excel | MERGE INTO quotr-vs-excel (check GSC) | P3 | |
| [real-estate-pro-forma-software-comparison](https://quotr.ai/blog/real-estate-pro-forma-software-comparison/) | "Quotr.ai vs. Aprao vs. Excel"; seen in web search | KEEP → REFRESH (fact-check Aprao; absorbs construction-proforma-software) | P3 | E-022 |
| [outsourcing-vs-hiring-an-estimator](https://quotr.ai/blog/outsourcing-vs-hiring-an-estimator/) | Needs brand-attached prices | REFRESH | P1 | L-018, L-019 |

**B. "Alternatives to X" (5)**

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [best-togal-ai-alternatives-2026](https://quotr.ai/blog/best-togal-ai-alternatives-2026/) | Old "from $299.90"; "50+ verified factories"; unlinked third-party figures; self-ranked #1; duplicate of the next post | FIX FACTS now → MERGE INTO best-togal-ai-alternatives (301) | P0 / P1 | E-043 |
| [best-togal-ai-alternatives](https://quotr.ai/blog/best-togal-ai-alternatives/) | Cited in V1 (only unbranded answer naming Quotr); year-free URL | REFRESH (the merged page: honest "best for [situation]" ranking, sources, dates) | P1 | E-043 (T16) |
| [best-planswift-alternatives-2026](https://quotr.ai/blog/best-planswift-alternatives-2026/) | Used as a PlanSwift fact source, Quotr not recommended | REFRESH | P1 | E-044 (T18), E-045 |
| [bluebeam-alternative](https://quotr.ai/blog/bluebeam-alternative/) | Old price; not used for V4 | FIX FACTS → REFRESH | P0 / P2 | E-046 (T19), D-032 |
| [stack-alternative](https://quotr.ai/blog/stack-alternative/) | Old Solo/Team price (also in FAQ); "PlanSwift … a Trimble product"; STACK "$2,599–$2,999/year" | FIX FACTS → REFRESH | P0 / P2 | E-047 (T25) |

**C. Best-of lists, buyer's guides and software guides (17)**

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [best-ai-construction-estimating-software-2026](https://quotr.ai/blog/best-ai-construction-estimating-software-2026/) | Old price; self-ranked; 4th in web search for C1 but not retrieved by Perplexity | FIX FACTS → REFRESH (honest "best for", no self-#1) | P0 / P1 | E-001 (T01), E-007 (T11) |
| [ai-construction-estimating-software-buyers-guide](https://quotr.ai/blog/ai-construction-estimating-software-buyers-guide/) | Old price; cited in brand prompts | FIX FACTS → REFRESH (neutral how-to-choose checklist, distinct from the list) | P0 / P2 | E-007, D-022 |
| [ai-bidding-software-construction](https://quotr.ai/blog/ai-bidding-software-construction/) | Old price; cited in brand prompts | FIX FACTS → REFRESH (absorbs best-ai-bid-software-for-construction) | P0 / P2 | E-025, E-004 (T07) |
| [best-ai-bid-software-for-construction](https://quotr.ai/blog/best-ai-bid-software-for-construction/) | Old price; overlaps the post above | FIX FACTS → MERGE INTO ai-bidding-software-construction (check GSC) | P0 / P2 | E-004 |
| [best-electrical-estimating-software-2026](https://quotr.ai/blog/best-electrical-estimating-software-2026/) | Old price; not retrieved for C6 | FIX FACTS → REFRESH (link the deep electrical page) | P0 / P2 | E-028 (T06) |
| [electrical-estimating-software-buyers-guide](https://quotr.ai/blog/electrical-estimating-software-buyers-guide/) | Possible overlap with the electrical best-of | KEEP (distinct "how to choose" intent; merge only if GSC shows both competing for the same queries) | P3 | E-028 |
| [hvac-estimating-software-2026-buyers-guide](https://quotr.ai/blog/hvac-estimating-software-2026-buyers-guide/) | Not retrieved for N3 | REFRESH | P2 | E-030 (T50) |
| [best-drywall-estimating-software-in-2026](https://quotr.ai/blog/best-drywall-estimating-software-in-2026/) | Not retrieved for C4 | REFRESH | P2 | E-026 (T04) |
| [best-concrete-estimating-software-2026](https://quotr.ai/blog/best-concrete-estimating-software-2026/) | Old price | FIX FACTS → REFRESH | P0 / P3 | E-031 |
| [best-plumbing-estimating-software-2026](https://quotr.ai/blog/best-plumbing-estimating-software-2026/) | — | REFRESH (link the deep plumbing page) | P3 | E-029 |
| [best-flooring-estimating-software-in-2026](https://quotr.ai/blog/best-flooring-estimating-software-in-2026/) | Old price; not retrieved for C5 | FIX FACTS → REFRESH | P0 / P2 | E-027 (T05) |
| [best-glazing-estimating-software-2026](https://quotr.ai/blog/best-glazing-estimating-software-2026/) | Old price | FIX FACTS → REFRESH | P0 / P3 | E-037 |
| [rebar-estimating-and-takeoff-software](https://quotr.ai/blog/rebar-estimating-and-takeoff-software/) | Old price | FIX FACTS | P0 | E-041, L-071 |
| [structural-steel-estimating](https://quotr.ai/blog/structural-steel-estimating/) | Old price; cited in brand prompts | FIX FACTS | P0 | E-040 |
| [trade-estimating-software](https://quotr.ai/blog/trade-estimating-software/) | — | REFRESH (make it the hub linking each trade software guide) | P3 | E-018 |
| [construction-procurement-software](https://quotr.ai/blog/construction-procurement-software/) | Not cited for C9 or S5 | REFRESH (neutral category guide that includes factory-direct sourcing; brand-attached) | P1 | E-013 (T42), E-006 (T09) |
| [construction-proforma-software](https://quotr.ai/blog/construction-proforma-software/) | Overlaps the pro forma comparison | MERGE INTO real-estate-pro-forma-software-comparison (check GSC) | P3 | L-138 |

**D. Estimating services (12)**

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [quotr-service-estimates](https://quotr.ai/blog/quotr-service-estimates/) | "$1.2B+" with no method | FIX FACTS (say how it is counted) → later link the method page | P1 | Proof for D-046 |
| [mep-estimating-services](https://quotr.ai/blog/mep-estimating-services/) | Check turnaround wording | FIX FACTS → KEEP | P0 | E-076 |
| [hvac-estimating-services](https://quotr.ai/blog/hvac-estimating-services/) | Possible overlap with MEP post | KEEP (merge into MEP only if GSC shows overlap) | P3 | E-077 |
| [electrical-estimating-services](https://quotr.ai/blog/electrical-estimating-services/) | "Scope quote in 1 day, takeoffs in 1–2" | FIX FACTS | P0 | E-078 |
| [precon-on-demand-outsource-bid-cost-estimation](https://quotr.ai/blog/precon-on-demand-outsource-bid-cost-estimation/) | "1–3 days"; overlaps preconstruction-services | FIX FACTS → MERGE INTO preconstruction-services (check GSC) | P0 / P2 | E-079 |
| [quantity-takeoff-services](https://quotr.ai/blog/quantity-takeoff-services/) | Cited for outsourcing cost (S9) | REFRESH (brand-attached Quotr price) | P1 | E-074 (T44) |
| [preconstruction-services](https://quotr.ai/blog/preconstruction-services/) | Overlaps other service posts | REFRESH (GC precon service page; absorbs Precon on Demand) | P2 | E-079 |
| [commercial-estimating-services](https://quotr.ai/blog/commercial-estimating-services/) | Cited in C12, unnamed | REFRESH (brand-attach; commercial-specific) | P1 | E-080, E-073 |
| [construction-estimating-services-california](https://quotr.ai/blog/construction-estimating-services-california/) | Location variation | KEEP → REFRESH (make it truly California-specific: Bay Area data, LA rebuilds); no more city pages | P3 | E-075 |
| [outsource-construction-estimating](https://quotr.ai/blog/outsource-construction-estimating/) | First citation in C12, unnamed | REFRESH (brand-attached rates, one turnaround, what you get; absorbs construction-estimating-services) | P1 | E-073 (T12) |
| [construction-estimating-services](https://quotr.ai/blog/construction-estimating-services/) | Overlaps outsource post | MERGE INTO outsource-construction-estimating | P1 | |
| [quotr-developer-desk-underwriting-grade-estimates-72-hours](https://quotr.ai/blog/quotr-developer-desk-underwriting-grade-estimates-72-hours/) | "72 hours" in URL and copy conflicts with other turnarounds | FIX FACTS → REFRESH (developer method page; if 72 hours is no longer true, 301 to a new URL without the number) | P0 / P2 | L-136, E-023, E-087 |

**E. Trade how-tos and estimating fundamentals (16)**

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [how-to-estimate-plumbing-from-drawings](https://quotr.ai/blog/how-to-estimate-plumbing-from-drawings/) | First citation for N2, unnamed | REFRESH (brand-attach; residential price-per-fixture section) | P1 | L-097 (T49), L-098 |
| [how-to-estimate-hvac-sheet-metal-mechanical-plan](https://quotr.ai/blog/how-to-estimate-hvac-sheet-metal-mechanical-plan/) | No residential section | REFRESH | P2 | L-102, L-103 |
| [how-to-estimate-drywall-framing-commercial-floor-plan](https://quotr.ai/blog/how-to-estimate-drywall-framing-commercial-floor-plan/) | Commercial only; not cited for "drywall for a house" (P2) | KEEP (commercial); a new residential guide covers P2 | P3 | L-047, L-051 |
| [how-to-estimate-electrical-work-from-drawings-conduit-devices-labor](https://quotr.ai/blog/how-to-estimate-electrical-work-from-drawings-conduit-devices-labor/) | No residential pricing section | REFRESH | P2 | L-091, L-092 |
| [commercial-electrical-takeoff-drawings-to-proposal](https://quotr.ai/blog/commercial-electrical-takeoff-drawings-to-proposal/) | — | KEEP | — | L-096 |
| [commercial-signage-takeoff-sign-schedule-bid-package](https://quotr.ai/blog/commercial-signage-takeoff-sign-schedule-bid-package/) | Niche | KEEP | — | |
| [flooring-trades-how-to-quote-flooring-jobs-and-win-more-work](https://quotr.ai/blog/flooring-trades-how-to-quote-flooring-jobs-and-win-more-work/) | — | REFRESH (waste factors; link calculator) | P3 | L-058 |
| [how-to-do-construction-takeoff-pdf-blueprint](https://quotr.ai/blog/how-to-do-construction-takeoff-pdf-blueprint/) | Ranks in web search; not cited for P1 | REFRESH (numbered steps with units, manual vs AI, human-check caveat, Quotr example, video) | P2 | L-031 (T26), L-032 |
| [construction-takeoff-guide](https://quotr.ai/blog/construction-takeoff-guide/) | — | KEEP | — | L-030, L-045 |
| [blueprint-to-priced-estimate-workflow](https://quotr.ai/blog/blueprint-to-priced-estimate-workflow/) | — | KEEP (absorbs the "plans into prices in minutes" post) | P3 | E-072 |
| [metric-imperial-construction-takeoff](https://quotr.ai/blog/metric-imperial-construction-takeoff/) | Bulk date | KEEP | — | L-028, E-070 |
| [how-to-price-construction-job](https://quotr.ai/blog/how-to-price-construction-job/) | — | KEEP | — | L-001 |
| [construction-estimating-mistakes-to-avoid](https://quotr.ai/blog/construction-estimating-mistakes-to-avoid/) | — | KEEP | — | L-017 |
| [how-to-bid-commercial-construction-projects-subcontractor-estimating-takeoff-guide](https://quotr.ai/blog/how-to-bid-commercial-construction-projects-subcontractor-estimating-takeoff-guide/) | — | KEEP | — | L-013 |
| [how-subcontractors-bid-gcs-without-giving-away-margin](https://quotr.ai/blog/how-subcontractors-bid-gcs-without-giving-away-margin/) | — | KEEP | — | L-012 |
| [scope-gap-construction](https://quotr.ai/blog/scope-gap-construction/) | Unsourced stats; broken link; date mismatch; strong byline (Junzhe Shi, PhD) | FIX FACTS | P1 | L-011 |

**F. AI explainers (11)**

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [what-is-ai-construction-estimating-software](https://quotr.ai/blog/what-is-ai-construction-estimating-software/) | Overlaps "how it works" post | KEEP (absorbs how-ai-construction-estimating-works) | P3 | L-034 |
| [how-ai-construction-estimating-works](https://quotr.ai/blog/how-ai-construction-estimating-works/) | Overlap | MERGE INTO what-is-ai-construction-estimating-software (check GSC) | P3 | L-038 |
| [how-ai-construction-takeoff-works-in-2026](https://quotr.ai/blog/how-ai-construction-takeoff-works-in-2026/) | Bulk date; "2026" slug | KEEP (real update in 2027 with a year-free URL) | P3 | L-038 |
| [is-ai-takeoff-actually-accurate-yet](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/) | First citation for P5, unnamed | REFRESH (brand-attach; method; link benchmark) | P1 | L-035 (T30), L-039, L-041 |
| [ai-that-reads-construction-drawings-chat-with-blueprints](https://quotr.ai/blog/ai-that-reads-construction-drawings-chat-with-blueprints/) | Not cited for P6 | REFRESH (examples, limits, video) | P2 | L-036 (T31), E-069 |
| [chatgpt-for-construction-estimating](https://quotr.ai/blog/chatgpt-for-construction-estimating/) | Seen in web search | REFRESH (add a dated test of ChatGPT on a real plan) | P2 | L-037 |
| [ai-agent-for-construction](https://quotr.ai/blog/ai-agent-for-construction/) | — | KEEP | — | L-044 |
| [ai-construction-proposals-takeoff-to-proposal](https://quotr.ai/blog/ai-construction-proposals-takeoff-to-proposal/) | — | REFRESH (inclusions, exclusions, clarifications) | P3 | L-025, L-026, E-020 |
| [ai-construction-estimating-software-that-turns-plans-into-prices-in-minutes](https://quotr.ai/blog/ai-construction-estimating-software-that-turns-plans-into-prices-in-minutes/) | Bulk date; overlaps workflow post | MERGE INTO blueprint-to-priced-estimate-workflow (check GSC) | P3 | E-072 |
| [state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs](https://quotr.ai/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/) | `utm_source=chatgpt.com` links; self-referential AI-search line; no own data; "By quotr.ai" | FIX FACTS → REFRESH (add a Quotr data point, or call it a roundup) | P1 / P3 | L-042, L-043, E-021 |
| [construction-labor-shortage-ai-adoption-2026](https://quotr.ai/blog/construction-labor-shortage-ai-adoption-2026/) | — | KEEP | — | L-042 |

**G. Procurement and sourcing (10)**

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [construction-procurement-process](https://quotr.ai/blog/construction-procurement-process/) | Overlaps the "what is" guide | KEEP (absorbs what-is-construction-procurement-2026-guide) | P3 | L-125 |
| [what-is-construction-procurement-2026-guide](https://quotr.ai/blog/what-is-construction-procurement-2026-guide/) | Overlap; "2026" slug | MERGE INTO construction-procurement-process (check GSC) | P3 | L-125 |
| [ddp-construction-materials](https://quotr.ai/blog/ddp-construction-materials/) | Retrieved but unused in C10 | REFRESH (honest DDP vs FOB table; brand-attached facts; link the landed-cost calculator) | P1 | L-110, L-111, E-081 (T10) |
| [reduce-construction-material-costs](https://quotr.ai/blog/reduce-construction-material-costs/) | Not cited for P4; factory-direct not named as a lever | REFRESH (factory-direct as a named lever with project numbers) | P1 | L-108 (T29) |
| [how-developers-source-building-materials](https://quotr.ai/blog/how-developers-source-building-materials/) | Cited in S6; factory count wording | FIX FACTS → REFRESH (plain buyer wording) | P0 / P1 | E-083 (T43), L-109 |
| [hospitality-procurement-consolidated-sourcing](https://quotr.ai/blog/hospitality-procurement-consolidated-sourcing/) | — | KEEP | — | L-128 |
| [ai-agents-for-construction-procurement-and-buyout](https://quotr.ai/blog/ai-agents-for-construction-procurement-and-buyout/) | — | KEEP | — | |
| [takeoff-to-buyout-construction-estimating-procurement-platform](https://quotr.ai/blog/takeoff-to-buyout-construction-estimating-procurement-platform/) | Main page for "estimating software with procurement", not cited for C9 | REFRESH (canonical page; absorbs the takeoff-to-transaction post) | P1 | E-006 (T09), E-066, L-126 |
| [the-takeoff-to-transaction-gap](https://quotr.ai/blog/the-takeoff-to-transaction-gap/) | Overlaps the takeoff-to-buyout post | MERGE INTO takeoff-to-buyout-construction-estimating-procurement-platform (check GSC) | P3 | E-066 |
| [sourcing-building-materials-china-cbd-fair-2026](https://quotr.ai/blog/sourcing-building-materials-china-cbd-fair-2026/) | Check factory numbers | FIX FACTS (if needed) → KEEP | P0 | L-122 |

**H. Cost and market data (6)**

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [construction-cost-index-q1-2026-ppi-rsmeans-mortenson](https://quotr.ai/blog/construction-cost-index-q1-2026-ppi-rsmeans-mortenson/) | Third-party roundup; Q1 data | REFRESH (quarterly; link Quotr's own index when live) | P2 | L-124 |
| [tariff-impact-construction-costs-2026-steel-aluminum-copper](https://quotr.ai/blog/tariff-impact-construction-costs-2026-steel-aluminum-copper/) | Not cited for the tariff prompt (only public and media sources were) | REFRESH (residential finish materials and lumber; Quotr data; quarterly) | P1 | L-113 (T46), L-056 |
| [tariff-aware-estimating-material-escalation-every-bid](https://quotr.ai/blog/tariff-aware-estimating-material-escalation-every-bid/) | — | KEEP | — | L-020, L-021 |
| [construction-cost-trends-2026](https://quotr.ai/blog/construction-cost-trends-2026/) | — | KEEP (absorbs the "12.6%" post) | P3 | L-029, L-123 |
| [construction-costs-surged-12-6-in-2026-how-ai-estimation-helps](https://quotr.ai/blog/construction-costs-surged-12-6-in-2026-how-ai-estimation-helps/) | Bulk date; overlap; check the source of "12.6%" | MERGE INTO construction-cost-trends-2026 (check GSC) | P3 | L-029 |
| [data-center-construction-estimating-mep-subcontractor-choke-point](https://quotr.ai/blog/data-center-construction-estimating-mep-subcontractor-choke-point/) | Sector piece | KEEP | — | L-146 |

**I. Developer, architect and investor personas (3)**

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [the-proforma-that-never-stops-changing](https://quotr.ai/blog/the-proforma-that-never-stops-changing/) | — | KEEP (link the developer hub and pro forma template) | P3 | L-138 |
| [the-architects-survival-guide-unlocking-new-revenue-streams-in-pre-construction](https://quotr.ai/blog/the-architects-survival-guide-unlocking-new-revenue-streams-in-pre-construction/) | Bulk date | KEEP | — | L-144 |
| [house-flipping-math-2026](https://quotr.ai/blog/house-flipping-math-2026/) | — | KEEP | — | L-145 |

**J. Company news, customer stories and event recaps (8)**

| URL | Current issue | Action | Priority | Notes / prompts |
|---|---|---|---|---|
| [new-pricing](https://quotr.ai/blog/new-pricing/) | The announcement of current pricing | KEEP (make sure it matches /pricing/) | — | D-008 |
| [how-rl-electric-cut-estimating-time-with-ai-powered-takeoffs](https://quotr.ai/blog/how-rl-electric-cut-estimating-time-with-ai-powered-takeoffs/) | Duplicates the case-study story | MERGE INTO /case-studies/rl-electric/ (after the case study is rebuilt) | P2 | D-017 |
| [vanderbilt-classroom](https://quotr.ai/blog/vanderbilt-classroom/) | First-party only | KEEP (ask for a third-party quote) | — | |
| [pcbc-2026-recap-quotr-ai-takeoff-service](https://quotr.ai/blog/pcbc-2026-recap-quotr-ai-takeoff-service/) | Low GEO value | KEEP | — | |
| [nhca-build-the-builder-2026-recap](https://quotr.ai/blog/nhca-build-the-builder-2026-recap/) | Low GEO value | KEEP | — | |
| [re-forge-sf-2026-recap](https://quotr.ai/blog/re-forge-sf-2026-recap/) | Low GEO value | KEEP | — | |
| [dallas-build-expo-2026-recap](https://quotr.ai/blog/dallas-build-expo-2026-recap/) | Low GEO value | KEEP | — | |
| [ibs-2026-from-the-magic-of-orlando-to-the-reality-of-ai-implementation](https://quotr.ai/blog/ibs-2026-from-the-magic-of-orlando-to-the-reality-of-ai-implementation/) | Bulk date; low GEO value | KEEP | — | |

### Summary of actions (blog posts only)

| Final state | Count | Posts |
|---|---|---|
| Merged away (301 to another page) | 12 | best-togal-ai-alternatives-2026, construction-estimating-services, best-ai-bid-software-for-construction, precon-on-demand-outsource-bid-cost-estimation, quotr-vs-traditional-estimating, construction-proforma-software, how-ai-construction-estimating-works, ai-construction-estimating-software-that-turns-plans-into-prices-in-minutes, what-is-construction-procurement-2026-guide, the-takeoff-to-transaction-gap, construction-costs-surged-12-6-in-2026-how-ai-estimation-helps, how-rl-electric-cut-estimating-time-with-ai-powered-takeoffs (into the case study). Two more merges (hvac-estimating-services, electrical-estimating-software-buyers-guide) only if Search Console shows overlap; not counted |
| Refreshed (real content update) | 41 | Every row marked REFRESH above |
| Kept after a fact fix only | 10 | The three Beam/STACK/PlanSwift head-to-heads, rebar, structural steel, quotr-service-estimates, MEP and electrical services, scope-gap, CBD Fair |
| Kept as they are | 33 | Mostly fundamentals, niche and event posts |
| **Total** | **96** | |

About 20 posts are part of the P0 fact-fix sweep (mainly the old-price and turnaround posts); many of them are later refreshed or merged too.

---

## After the fixes: what "create new" should look like

New effort goes to the assets in [content-priorities.md](content-priorities.md), scheduled in [content-roadmap.md](content-roadmap.md):
- original data (price index, cost benchmarks, accuracy and turnaround benchmarks);
- free tools and templates;
- proof pages (quantified case studies, method, security, integrations, author pages);
- decision guides on factory-direct buying, importing and tariffs;
- 3–4 persona hubs, deep trade pages, and a small number of honest comparison pages (Handoff, Buildxact, Kreo, a four-way table, "Quotr alternatives").

And **not** to more "[trade] estimating services" or city variations, more self-ranked lists, or year-bumped refreshes.

---

## Open questions for Quotr

- Approve the fact sheet (price wording, factory count, savings, turnaround, HQ, founding year, founders, funding, audience, handles, contact email).
- Share Search Console, Bing Webmaster Tools and GA4 access (or exports) so merge winners and refresh priorities can be confirmed.
- Who owns Cloudflare, quotr.io and test.quotr.io? (Report, meeting questions.)
- Which trades does the software really serve well (to decide deepen vs noindex for the 23 trade pages)?
- Can customers be named with numbers in case studies?
- Who edits AI-assisted drafts before publishing?

---

## Related pages

- [content-priorities.md](content-priorities.md): which content types to invest in, and what to stop
- [content-roadmap.md](content-roadmap.md): the new and rebuilt pieces, month by month
- [offsite-earned-media-plan.md](offsite-earned-media-plan.md): fixing the facts on other people's websites and earning new proof
- [top-of-funnel-strategy.md](top-of-funnel-strategy.md): how refreshes and new assets protect reach
- [../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md): the single source of truth the sweep depends on
- [../02-current-state/website-audit.md](../02-current-state/website-audit.md) and [../02-current-state/geo-tactics-already-used.md](../02-current-state/geo-tactics-already-used.md): the audit behind every row
- [../06-playbooks/page-refresh-checklist.md](../06-playbooks/page-refresh-checklist.md): step-by-step refresh checklist
- [../06-playbooks/schema-markup-kit.md](../06-playbooks/schema-markup-kit.md): consistent Organization, Offer and FAQ markup
- [../07-measurement/tracking-setup.md](../07-measurement/tracking-setup.md): Search Console, Bing and GA4 setup
- [../08-action-plan/30-60-90-plan.md](../08-action-plan/30-60-90-plan.md): where these tasks sit in the overall plan
