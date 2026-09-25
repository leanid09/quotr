---
type: playbook
description: Step-by-step checklist and scoring rubric for upgrading an existing page, and how to pick which first.
last_verified: 2026-09-25
verify_every_days: 180
---
# Page Refresh Checklist (GEO Upgrade of Existing Pages)

> [!abstract] What this page is for
> A step-by-step checklist and scoring rubric for upgrading an existing quotr.ai page so AI answer engines can find, trust and quote it, plus a method for choosing which pages to refresh first.

> [!info]- Sources
> [[geo_content_playbook_b2b]] (§2 "Optimizing existing content vs creating new", §4 measurement), [[quotr_onsite_content_audit]] (§1–6), [[verification_quotr_and_competitors]] (claims 4, 7, 13–18; gaps filled #2, #5), [[verification_geo_evidence]] (claims #1, #2, #7, #10; H6; M1), [[quotr_ai_visibility_tests]] (§1–5), [[competitor_geo_benchmark]] (§3–4).

---

## How to use this page

1. Use **Section 2** to build a shortlist of pages to refresh.
2. Score each shortlisted page with the **rubric in Section 4** (takes 10–15 minutes per page).
3. Work through the **checklist in Section 3** for each page, top to bottom.
4. Re-score after the refresh and log it (**Section 7**).

Write every change using [[GEO writing style guide]]. Check every Quotr fact against [[Entity fact sheet]].

**Plain-English terms:**
- **Refresh:** a real update to an existing URL (new facts, better structure, new sections). Not just a new date.
- **Consolidate:** merge two or more overlapping pages into one and redirect the others to it (a "301 redirect" sends visitors and search engines to the new address permanently).
- **Retrieved / cited / named:** an AI engine read a page / showed it as a source / said "Quotr.ai" in the answer.

---

## 1. Refresh or create? What the evidence says

- **Fix and consolidate first, then put most effort into genuinely new content.** The research notes originally said "refresh first". The fact-check softened that: Ahrefs' own freshness study author "suspect[s] most brands will see better results from creating new, high-quality content than from … extremely frequent content updating", and Google's May 2026 guide rewards "valuable, unique, non-commodity content" (`verification_geo_evidence.md` claim #10, claim #1, hype flag H6).
- **Refreshing is still the cheapest win for three kinds of page:** pages with wrong facts, pages AI engines already retrieve or cite, and thin pages on topics Quotr must own.
- **Real changes only.** AI-cited URLs are on average 25.7% "fresher" than Google results, and ChatGPT prefers recent content most (Ahrefs, ~17M citations). But date-only updates are discounted, and posts "lightly refreshed with '2026' in the title" were among the pages that lost visibility in early 2026 (`geo_content_playbook_b2b.md` §1–2; `verification_geo_evidence.md` claims #10, #19).
- **Volume does not help.** Site page count barely correlates with AI visibility (~0.194 across 75K brands, Ahrefs). Quotr already has 96 posts, 55 dictionary terms and 23 trade pages; making them better beats making more (`geo_content_playbook_b2b.md` §2; `verification_geo_evidence.md` claim #13).
- **Ranking is not required for citation, but it helps.** Only 38% of AI Overview citations came from top-10 results in Ahrefs' 2026 data; classic ranking still mattered most in the C-SEO Bench re-test (`verification_geo_evidence.md` claims #9, #14).

---

## 2. How to pick which pages to refresh first

### 2a. Data to pull (30–60 minutes)

| Source | What to export | Why |
|---|---|---|
| **Google Search Console → Performance** | Clicks and impressions per page, last 3 months vs previous 3 | Pages with impressions are already in Google's candidate set |
| **Google Search Console → Generative AI performance reports** (worldwide since Aug 31, 2026) | Impressions from AI Overviews and AI Mode, per page | First first-party Google data on AI visibility. Impressions only: no clicks, CTR or queries. Do not add to Web totals (`verification_geo_evidence.md` M1) |
| **Bing Webmaster Tools → AI Performance** (public preview since Feb 2026) | How often each URL is cited in Copilot and Bing AI answers, plus "grounding queries" | Shows which pages Microsoft's AI already uses and for which internal searches (`geo_ai_citation_signals_2026.md` §1; blog date corrected to Feb 10, 2026 in `verification_geo_evidence.md` claim #3) |
| **GA4** | Landing pages for the "AI Assistant" default channel (since May 13, 2026) **plus** a custom channel with a regex such as `chatgpt\.com\|chat\.openai\.com\|perplexity\.ai\|gemini\.google\.com\|copilot\.microsoft\.com\|claude\.ai` | Pages that already get AI referrals. Perplexity is **not** in GA4's AI channel, so keep the custom regex (`verification_geo_evidence.md` claim #7) |
| **Prompt tracking results** | Which quotr.ai URLs were cited or retrieved per prompt | See [[AI visibility baseline]] and [[Tracking set]] |
| **Fact-risk list** | Pages showing retired prices or conflicting facts | From [[Entity fact sheet]] §4 and [[Website audit]] |

### 2b. Priority score (use a spreadsheet)

Score each candidate page 0–3 on each line, then add them up.

| Factor | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Fact risk** (wrong or retired facts that AI repeats) | None | Minor | Outdated number | Wrong price, wrong competitor fact, or leftover brief text |
| **Already visible** (GSC impressions, AI impressions, Bing AI citations, or cited/retrieved in prompt tests) | None | Some impressions | Retrieved in tests or growing AI impressions | Cited first in an AI answer |
| **Business value** (how close to a sale) | Event recap, news | Top-of-funnel education | Comparison, trade page, cost guide | Pricing, product, service, procurement |
| **Prompt gap** (a High-priority prompt in the [[Prompt library\|prompt library]] points to this page with "(optimize)") | No | Low-priority prompt | Medium | High |
| **Effort** (subtract) | — | Days (subtract 1) | A week (subtract 2) | Needs new data or Quotr confirmation (subtract 3) |

**Rule of thumb:** any page with Fact risk = 3 goes to the top, whatever its other scores. Wrong facts spread: Nomic and Octopus Builds already copied Quotr's retired $299.90 entry price (verification file, claim 27).

### 2c. Quotr's starting shortlist (from the September 2026 audit)

**Tier 0 — fact fixes (days, do first):**

| Page(s) | Problem | Source |
|---|---|---|
| About 13 Quotr URLs carry a retired price. Mostly blog posts: [stack-alternative](https://quotr.ai/blog/stack-alternative/), [structural-steel-estimating](https://quotr.ai/blog/structural-steel-estimating/), [best-concrete-estimating-software-2026](https://quotr.ai/blog/best-concrete-estimating-software-2026/), [ai-bidding-software-construction](https://quotr.ai/blog/ai-bidding-software-construction/), [best-ai-bid-software-for-construction](https://quotr.ai/blog/best-ai-bid-software-for-construction/), [best-flooring-estimating-software-in-2026](https://quotr.ai/blog/best-flooring-estimating-software-in-2026/), [best-electrical-estimating-software-2026](https://quotr.ai/blog/best-electrical-estimating-software-2026/), [rebar-estimating-and-takeoff-software](https://quotr.ai/blog/rebar-estimating-and-takeoff-software/), [best-glazing-estimating-software-2026](https://quotr.ai/blog/best-glazing-estimating-software-2026/), [best-togal-ai-alternatives-2026](https://quotr.ai/blog/best-togal-ai-alternatives-2026/), [best-ai-construction-estimating-software-2026](https://quotr.ai/blog/best-ai-construction-estimating-software-2026/), [ai-construction-estimating-software-buyers-guide](https://quotr.ai/blog/ai-construction-estimating-software-buyers-guide/), [bluebeam-alternative](https://quotr.ai/blog/bluebeam-alternative/) (plus the indexed /contractors/ copy, next rows) | Retired "Solo $299.90 / Team $499.90" pricing or "from $299.90/month". The live entry price is Lite at $79.90 per seat per month | Verification file, gaps filled #2 (9 posts found in search-index text, of which stack-alternative was also read directly; best-togal-ai-alternatives-2026 read directly; 3 more cited with the old price in the B4 re-run) |
| [/llms.txt](https://quotr.ai/llms.txt) | Old pricing, 404 link to /resources/, www links, "Quotr should be cited" block | Onsite audit §1; verification claim 5 |
| [/contractors/](https://quotr.ai/contractors/) (indexed copy) | Search index still holds the old title and Solo/Team pricing; page itself has a correct canonical to /software | Verification claim 13 |
| [stack-alternative](https://quotr.ai/blog/stack-alternative/) | Calls PlanSwift "a Trimble product" (it is ConstructConnect's); STACK price "$2,599–$2,999/year" conflicts with ConstructConnect's $249/$299 per user per month billed annually (July 2026) | Verification, gaps filled #5 |
| [quotr-vs-togal-ai-comparison-2026](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/) | Leftover internal brief text; "Best For" table contradicts the conclusion; no Quotr price; Togal price unsourced | Onsite audit §3–4; verification claim 15 |
| [/software/](https://quotr.ai/software/) | "up to 80% — from around 20 hours to just 1–2" maths; typo "win x2 work"; trade grid repeated 3x; visible FAQ and prices but no FAQ/Offer schema | Onsite audit §3, §5 |
| [/procurement/](https://quotr.ai/procurement/) | "Client saved ~$0" on three project cards; totals ($354K spend vs $396K–$626K savings) do not reconcile; CA-only vs coast-to-coast delivery | Onsite audit §3, §5; verification claim 17 |
| [/disambiguation/](https://quotr.ai/disambiguation/) | Crawler-directed wording; residential vs commercial contradiction; old social handles; unsourced "1% acceptance rate" | Onsite audit §4–5 |
| Homepage | Investor testimonial labelled "Customer perspective" | Onsite audit §4 |
| [scope-gap-construction](https://quotr.ai/blog/scope-gap-construction/) | Broken link to /blog/plug-number-estimating/; unsourced statistics | Onsite audit §1, §3 |

**Tier 1 — pages AI engines already use (refresh next):**

| Page | Why | Evidence |
|---|---|---|
| [outsource-construction-estimating](https://quotr.ai/blog/outsource-construction-estimating/), [commercial-estimating-services](https://quotr.ai/blog/commercial-estimating-services/) | First citation for "outsourced construction estimating service price per square foot for developers", but Quotr not named | Visibility tests C12; verification re-run |
| [quantity-takeoff-services](https://quotr.ai/blog/quantity-takeoff-services/) | Cited for $0.03–$0.10/sq ft and $250–$2,500 per estimate | Competitor benchmark §3 |
| [how-to-estimate-plumbing-from-drawings](https://quotr.ai/blog/how-to-estimate-plumbing-from-drawings/) | First citation for "how to estimate plumbing from drawings", brand not named | Prompt library N2 (one extra run) |
| [best-planswift-alternatives-2026](https://quotr.ai/blog/best-planswift-alternatives-2026/) | Cited for PlanSwift facts; Quotr not recommended | Visibility tests V3 (two runs in one session; the fact-check re-run was refused, so not reproduced) |
| [best-togal-ai-alternatives-2026](https://quotr.ai/blog/best-togal-ai-alternatives-2026/) + [best-togal-ai-alternatives](https://quotr.ai/blog/best-togal-ai-alternatives/) | Both cited; near-duplicates → consolidate into one | Competitor benchmark §4 |
| [is-ai-takeoff-actually-accurate-yet](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/) | First citation for "how accurate is AI takeoff" (P5), brand not named; name Quotr in the key sentence; publish the method | Visibility tests P5 (single run; re-run refused); prompt library L-035 |
| [how-developers-source-building-materials](https://quotr.ai/blog/how-developers-source-building-materials/), [ddp-construction-materials](https://quotr.ai/blog/ddp-construction-materials/) | Factory-direct prompts: named 3rd of 6 on re-run (engine said Quotr emphasises sourcing more than AI takeoff); DDP post retrieved but unused | Verification re-run; visibility tests C10 |
| [/pricing/](https://quotr.ai/pricing/), [/faq/](https://quotr.ai/faq/), [/about-us/](https://quotr.ai/about-us/) | Cited on brand prompts; /faq/ names no integrations; /about-us/ has no founding year or HQ | Onsite audit §3 |

**Tier 2 — thin pages on strategic topics (refresh in batches):**

- **23 trade pages** under /software/trades/. The drywall page had about 25 words of unique copy (onsite audit §3). Some may have been expanded since (the structural-steel index copy looked richer), so re-check each first. Start with the trades that have High-priority prompts: drywall, flooring, roofing, framing (see [[Prompt library]] "Views by trade").
- **55 dictionary terms** (~200 words, no author, no sources, none updated since July 2026). Upgrade the ones tied to High prompts first: ai-takeoff, quantity-takeoff, bid-leveling, scope-gap, markup-vs-margin. Use [[Glossary entry template]].
- **Case studies:** [RL Electric](https://quotr.ai/case-studies/rl-electric/) shows no numbers on the page; the "20 hours → 1–2 hours" quote lives only on the homepage. Use [[Case study template]].
- **Tariff and cost posts** that feed High-priority tariff prompts (e.g., [tariff-impact-construction-costs-2026-steel-aluminum-copper](https://quotr.ai/blog/tariff-impact-construction-costs-2026-steel-aluminum-copper/)). Today tariff answers cite only government, association and media sources (competitor benchmark §3).

**Consolidation candidates:**

| Keep (suggested) | Merge into it and 301 redirect | Why |
|---|---|---|
| best-togal-ai-alternatives-2026 (or a new slug without the year) | best-togal-ai-alternatives | Same query; both cited (competitor benchmark §4) |
| One "outsourced construction estimating services" hub | construction-estimating-services, outsource-construction-estimating, commercial-estimating-services, preconstruction-services (review each first) | Overlapping service posts risk cannibalisation (onsite audit §2) — **decide with Quotr** which URL has the most traffic and links |

---

## 3. The refresh checklist (work top to bottom)

### Step 1. Before you edit (15 minutes)

- [ ] Record the page's baseline: GSC clicks/impressions (last 3 months), GSC generative-AI impressions, Bing AI citations, GA4 AI-channel sessions.
- [ ] List the 3–8 prompts this page should answer (from the [[Prompt library|prompt library]]). Run them in at least two engines and note: is Quotr named? Is this URL cited? Who is cited instead?
- [ ] Open the 2–3 pages that AI engines cite instead. Note what they have that Quotr's page lacks (a number, a table, a date, a step list, a definition).
- [ ] Score the page with the rubric in Section 4. Save the score.

### Step 2. Facts (fix these even if you change nothing else)

- [ ] Every Quotr fact matches [[Entity fact sheet]]: prices (Lite $79.90, Plus $299.90 per seat per month, Enterprise custom, 7-day trial), service rates ($0.25/$0.10 per sq ft), names (Quotr.ai; Quotr Software/Service/Procurement).
- [ ] Remove every retired plan name and price: "Solo", "Team", "1 User Plan", "2–10 Users Plan", "$499.90", "from $299.90/month".
- [ ] Remove or mark any "TO CONFIRM" fact: HQ city, founding year, funding, factory count (50+ vs 220+), savings %, turnaround, accuracy %.
- [ ] Check every competitor fact on the competitor's own site; add "as of [Month Year]". Fix known errors (PlanSwift is ConstructConnect's, not Trimble's).
- [ ] Check maths (percentages, totals, "X to Y hours").
- [ ] Remove leftover brief text: search for "should", "prompt", "AI search", "position", "win when the buyer".

### Step 3. Answer and structure

- [ ] Add or rewrite the **Quick answer** block (40–80 words) directly under the H1, with "Quotr.ai" inside the key fact sentence where Quotr is the subject.
- [ ] Rewrite the H1/title to match the main buyer question. Keep the URL if it already has traffic and links; only change a slug with a 301 redirect.
- [ ] Turn vague headings into buyer questions.
- [ ] Make each H2 section self-contained: open with a 1–2 sentence answer that names the subject.
- [ ] Add a table where readers compare things (prices, features, trades, manual vs AI).
- [ ] Add a short "Limitations / when this is not the right fit" section (comparison, product, accuracy pages).
- [ ] Add an FAQ of 4–8 real questions from the prompt library (see [[FAQ block template]]).
- [ ] Cut filler intros, repeated sections (e.g., the triple trade grid on /software/) and off-topic paragraphs.

### Step 4. Evidence and originality

- [ ] Every number has a primary-source link, a "Quotr data" label with method, or a named customer.
- [ ] Remove `utm_source=chatgpt.com` and other tracking parameters from outbound links.
- [ ] Add at least one thing AI cannot get elsewhere: Quotr's own dated numbers (service price table, procurement project costs, a worked example from a real plan set), a screenshot, a short video, or a customer quote. This is the "non-commodity" test in Google's guide.
- [ ] Add dated third-party proof where it exists (e.g., review counts "as of" date). Never invent it.

### Step 5. Authorship and dates

- [ ] Replace "By quotr.ai" with a named human author linked to an author page; add a reviewer for technical content if a real expert reviewed it.
- [ ] Show "Published" and "Last updated". Change "Last updated" only because of the real changes you just made.
- [ ] Make sure the visible date, the schema `dateModified` and the sitemap `lastmod` match.

### Step 6. Technical and schema

- [ ] Page is indexable (no `noindex`), returns 200, canonical points to itself (or to the right main page).
- [ ] Key content is in the HTML, not loaded only by JavaScript (e.g., the /procurement/ savings counters render "~$0" before the script runs).
- [ ] Add or fix schema from [[Schema markup kit]]: BlogPosting with the real author; FAQPage matching the visible FAQ; BreadcrumbList; SoftwareApplication/Offer on pricing and product pages. Validate it.
- [ ] Images have descriptive alt text; tables are real HTML tables.
- [ ] Page is in the right sitemap, and the blog sitemap is listed in robots.txt (it is not today; onsite audit §1).

### Step 7. Links

- [ ] 3–6 internal links out: the relevant trade page, dictionary terms, /pricing/, a case study.
- [ ] 2–5 internal links **in** from related pages (update older posts to point here).
- [ ] Fix any broken internal links on the page.
- [ ] For consolidated pages: 301 the old URLs here and update every internal link that pointed to them.

### Step 8. After publishing

- [ ] Request re-indexing: Google Search Console URL Inspection; Bing Webmaster Tools URL submission or IndexNow. (The verification file recommends this for all stale-pricing pages; gaps filled #2.)
- [ ] Update llms.txt if the page is linked there (low priority; llms.txt has no proven effect, but it must not be wrong).
- [ ] Re-promote: founder LinkedIn post, email, and links from new content (Ahrefs recommends re-promoting updated pages; `geo_content_playbook_b2b.md` §2).
- [ ] If third-party pages repeat the old fact, email them the correction (see [[Listicle and PR outreach]]).
- [ ] Re-run the page's prompts **2–4 weeks later**, then monthly. Do not judge on one run: 40–60% of cited domains change month to month for the same queries (Profound, `geo_content_playbook_b2b.md` §4).
- [ ] Re-score the page and fill in the refresh log.

---

## 4. Scoring rubric (0–24 points)

Score each of the 12 criteria 0, 1 or 2. Score before and after the refresh.

| # | Criterion | 0 points | 1 point | 2 points |
|---|---|---|---|---|
| 1 | **Answer first** | No direct answer in the first screen | Answer exists but after an intro | Clear 40–80 word answer right under the H1 |
| 2 | **Headings, title and slug** | Vague headings ("Overview"); generic title | Some question headings | Title, slug and H2s match real buyer questions |
| 3 | **Brand in fact sentences** | Quotr's facts written generically ("some firms charge…") | Brand named nearby but not in the key sentence | "Quotr.ai" sits inside the key fact sentences and table rows |
| 4 | **Fact accuracy** | Retired prices or wrong facts | Minor outdated details | Every fact matches the fact sheet and competitor sites (dated) |
| 5 | **Sources and dates on numbers** | Unsourced statistics | Some sourced | Every number sourced, labelled as Quotr data, or customer-attributed; "as of" dates on changing facts |
| 6 | **Structure** | Wall of text | Some lists or sections | Self-contained sections, at least one useful table, clean HTML |
| 7 | **Original value** | Could be written from any other site | Some Quotr specifics | Quotr's own data, examples, screenshots or video that no one else has |
| 8 | **Authorship** | "By quotr.ai" or none | Named author, no bio page | Named expert author with author page; reviewer where relevant |
| 9 | **Honest dates** | No dates, or dates that disagree (page vs schema vs sitemap) | Dates shown but inconsistent | Published + Last updated shown, consistent, and matching real changes |
| 10 | **Balance and limits** | Self-ranked #1, unsourced knocks on rivals, or leftover brief text | Mostly balanced | Clear limitations; competitors described fairly with dated facts |
| 11 | **Schema and technical** | No relevant schema, or schema that conflicts with the page | Some schema, not validated | Correct, validated schema matching visible content; indexable; in sitemap |
| 12 | **Internal links** | Orphan page or broken links | A few links | 3–6 relevant links out, 2+ links in, none broken |

**Bands:**

| Score | Action |
|---|---|
| 0–10 | **Rewrite or consolidate.** Consider merging into a stronger page. |
| 11–17 | **Refresh** using the checklist. |
| 18–24 | **Maintain.** Check facts when prices, competitors or data change. |

### Worked examples (scored from the September 2026 audit)

**[Quotr.ai vs Togal.AI](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/)** — about 12/24 → Refresh.

| # | Score | Reason |
|---|---|---|
| 1 | 2 | "## Quick Answer" block |
| 2 | 2 | Clear title; question-style FAQ |
| 3 | 1 | Positioning named, but no Quotr price ("See Quotr.ai pricing") |
| 4 | 0 | Contradictory "Best For" table; Togal price unsourced |
| 5 | 1 | Some tables; competitor figures unsourced |
| 6 | 2 | 23 H2s, 5 tables, clean HTML |
| 7 | 1 | Workflow detail, little Quotr data |
| 8 | 0 | "By quotr.ai"; schema author Person "quotr.ai" |
| 9 | 1 | datePublished = dateModified = 2026-05-12 |
| 10 | 0 | Leftover brief text ("Quotr.ai should win when the buyer is asking…") despite an "Honest Limitations" section |
| 11 | 1 | Article schema only; no FAQPage or BreadcrumbList |
| 12 | 1 | Links present; not checked in full |

**[Drywall trade page](https://quotr.ai/software/trades/drywall/)** — about 4/24 → Rewrite (use [[Product feature page template]] for trade pages). One sentence of unique copy, two blog links, no FAQ, no specifics, no examples (onsite audit §3). Re-check the live page first, since some trade pages may have been expanded.

---

## 5. How to consolidate two pages (step by step)

1. Pick the **keeper**: the URL with more clicks, impressions, AI citations and backlinks.
2. Copy the best unique parts of the other page into the keeper (a table, a section, FAQs).
3. Refresh the keeper with the checklist above.
4. Set a **301 redirect** from the old URL to the keeper.
5. Update every internal link that pointed to the old URL.
6. Remove the old URL from the sitemap; make sure the keeper is in it.
7. Request re-indexing of the keeper (Google Search Console, Bing Webmaster Tools / IndexNow).
8. If third-party pages link to the old URL, ask them to update the link (optional; the redirect covers it).

---

## 6. Refresh cadence (what to re-check, and when)

These cadences are **recommendations** (common practice and a hypothesis from the notes, not a proven effect; `verification_geo_evidence.md` H20).

| Page type | Re-check | Trigger for an immediate refresh |
|---|---|---|
| Pricing, plans, product pages | Monthly fact check | Any price or plan change |
| Comparison and alternatives pages | Quarterly | Competitor price, feature, funding or review-count change |
| Cost guides and original data | On the data schedule (quarterly or twice a year) | New data release; tariff change |
| Trade how-tos and glossary | Yearly | New Quotr feature for that trade; a reader or customer correction |
| Case studies | Yearly | New results from the customer |
| llms.txt, /disambiguation/, About | With every fact-sheet change | Any entity fact change |

Never change only the date. If nothing changed, leave the date alone.

---

## 7. Refresh log (copy into a spreadsheet)

| Date | URL | Tier | Score before | Main changes | Score after | Prompts re-tested (date) | Result 2–4 weeks later | Owner |
|---|---|---|---|---|---|---|---|---|
| 2026-__-__ | /blog/stack-alternative/ | 0 | _/24 | Pricing fixed; PlanSwift owner corrected; author added | _/24 | E-043, D-022 | Named? Cited? | |

---

## Related pages

- [[GEO writing style guide]] — how to write each section
- [[Schema markup kit]] — schema to add during a refresh
- [[Page templates]] — page-type templates for rewrites
- [[Website audit]] — full list of on-site issues
- [[Entity fact sheet]] — the facts to check against
- [[Optimize vs create]] — how refresh work fits the wider plan
- [[Tracking setup]] — GA4, Search Console and Bing setup
- [[Tracking set]] — prompts to re-test after a refresh
