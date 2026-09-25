---
type: playbook
description: House writing rules for any Quotr page or script, plus a safe AI-drafting prompt and pre-publish checklist.
aliases:
- Style guide
last_verified: 2026-09-25
verify_every_days: 180
---
# GEO Writing Style Guide for Quotr.ai

> [!abstract] What this page is for
> The house rules for writing any Quotr.ai page, post, profile or script so that people understand it and AI answer engines (ChatGPT, Google AI Overviews and AI Mode, Perplexity, Gemini, Claude, Copilot) can find, quote and credit it correctly.

> [!info]- Sources
> [[geo_content_playbook_b2b]] (§1–2, §7), [[geo_ai_citation_signals_2026]] (§1–3), [[quotr_onsite_content_audit]] (§3–5), [[competitor_geo_benchmark]] (§3), [[quotr_ai_visibility_tests]] (§1, §3), [[verification_geo_evidence]] and [[verification_quotr_and_competitors]] (corrections override the other notes); Google Search Central: [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), [AI optimization guide (May 2026)](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [Spam policies](https://developers.google.com/search/docs/essentials/spam-policies) (checked via WebSearch, 2026-09-25).

---

## How to use this guide

- **Who it is for:** anyone writing for Quotr.ai: the marketing team, the founders, freelance writers, and the GEO consultant. It also works as instructions for an AI writing tool. Paste this whole file into the tool before you ask it to draft.
- **When to use it:** before you write a new page, and whenever you refresh an old one (with the [[Page refresh checklist]]).
- **Facts come from one place.** Every Quotr fact (prices, names, numbers) must match [[Entity fact sheet]]. If a fact is not there, or is marked "TO CONFIRM with Quotr", do not publish it.

**Key terms (plain English):**

| Term | Meaning |
|---|---|
| **GEO / AEO** | Generative Engine Optimization / Answer Engine Optimization. Work that helps a brand get named and cited inside AI answers. |
| **Cited** | A quotr.ai page is shown as a source link under an AI answer. |
| **Named / mentioned** | The answer text itself says "Quotr.ai". This matters more to buyers than a footnote link. |
| **Query fan-out** | AI engines split one question into many smaller searches (for example "best AI takeoff software" → "AI takeoff pricing", "AI takeoff for drywall", "AI takeoff accuracy"). Google documents this for AI Overviews and AI Mode. |
| **Passage** | One section of a page (a heading plus the text under it). AI engines often lift a single passage, not the whole page. |
| **Entity** | The company as one "thing" that search engines recognise: its name, founders, location, website and profiles. |

**Evidence labels used in this guide:**

- **Evidence:** backed by a study in the research notes (usually observational, meaning it shows a pattern, not proof of cause).
- **Platform guidance:** what Google, Microsoft or OpenAI say themselves.
- **Common practice:** what good practitioners do. Sensible, but not proven to raise AI citations.

---

## 1. What the evidence says about writing for AI answers (one table)

Read this first. It stops the team from over-promising.

| Writing choice | What we know | Strength | Source |
|---|---|---|---|
| Put the answer near the top of the page | 44.2% of ChatGPT citations came from the first 30% of a page's text (1.2M ChatGPT answers analysed; 18,012 verified citations). This shows *where* citations fall; it is not an experiment. | Evidence (pattern) | Growth Memo, "The Science of How AI Pays Attention" (Feb 2026), per `verification_geo_evidence.md` claim #11 and hype flag H9 |
| Titles and URLs that match the narrower sub-questions | Ahrefs (1.4M ChatGPT prompts): cited pages had titles closer to ChatGPT's fan-out sub-queries. Pages with descriptive URL slugs were cited 89.78% of the times they were retrieved vs 81.11% for less descriptive slugs. | Evidence (vendor, correlation; not re-checked in the verification pass) | `geo_content_playbook_b2b.md` §1, [Ahrefs](https://ahrefs.com/blog/why-chatgpt-cites-pages/) |
| Specific numbers, dates and named methods | Growth Memo (June 2026): DATE and NUMBER entities best predicted ChatGPT citations; highly cited pages are dense with specific entities. | Evidence (analysis; not re-checked) | `geo_content_playbook_b2b.md` §1, [Growth Memo](https://www.growth-memo.com/p/why-proprietary-data-is-your-most) |
| Original data | 8 primary-research pages in a 301-page sample earned 11.3 citations each vs 3.4 for other pages (about 3.3x). | Evidence (small sample; not re-checked) | `geo_content_playbook_b2b.md` §1, [Growth Memo](https://www.growth-memo.com/p/why-most-original-data-never-gets) |
| Adding statistics, quotations and sources | The 2023/2024 GEO paper found up to ~40% lift on a lab benchmark. A 2025 peer-reviewed re-test (C-SEO Bench, NeurIPS 2025) found most such tricks "largely ineffective" and classic ranking "significantly more effective". | Mixed | `verification_geo_evidence.md` claim #9, M3, hype flag H2 |
| Freshness | AI-cited URLs were on average 25.7% "fresher" than Google organic results (Ahrefs, ~17M citations, July 2025). ChatGPT shows the strongest recency preference; Google the weakest. Google's John Mueller warns against date-only updates. | Evidence (vendor, correlation) | `verification_geo_evidence.md` claim #10 |
| Chunking content into tiny pieces | Google's May 15, 2026 guide says content does **not** need to be chunked. Microsoft (Oct 2025) recommends short single-idea sections and question-style headings. | Platform guidance (they disagree) | `geo_ai_citation_signals_2026.md` §1, §3; `verification_geo_evidence.md` H19 |
| "Valuable, unique, non-commodity content" | Google's May 2026 guide names this as the most important factor for its generative AI features. | Platform guidance | `verification_geo_evidence.md` claim #1 |
| Special AI files, AI-only pages, llms.txt | Google says no special files, Markdown copies or markup are needed. An SE Ranking study of 300K domains found no link between llms.txt and AI citations. | Platform guidance + evidence (SE Ranking is a vendor; its study was not re-checked in the verification pass) | `geo_ai_citation_signals_2026.md` §3; `verification_geo_evidence.md` section D |
| Author bylines and credentials | No robust study shows bylines directly raise AI citations. Google "strongly encourages" accurate bylines where readers expect them. | Platform guidance; no direct evidence | `geo_ai_citation_signals_2026.md` §2 Gaps; [Google helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) |
| AI-assisted drafting | Ahrefs (1M SERPs with AI Overviews): 71.7% of top-cited pages mixed AI and human writing; no penalty or reward was visible. | Evidence (vendor) | `geo_ai_citation_signals_2026.md` §2 |
| Page length | Long pages collect more citations in total; for a single question ChatGPT favours focused pages. Write focused pages that fully answer one job. Length is not a target. | Evidence (resolved conflict) | `verification_geo_evidence.md` X16 |

**Bottom line:** good GEO writing is mostly good, specific, honest writing. There is no trick that forces a citation. Clear, answer-first, well-sourced pages help both people and machines. The biggest levers for Quotr are **off-site** (reviews, third-party lists, YouTube, press). See [[Off-site earned media plan]].

---

## 2. The 12 writing rules

### Rule 1. Answer first

- Start the page, and every major section, with the direct answer in 1–2 sentences. Then explain.
- Put a short "Quick answer" block (40–80 words) right after the H1 on guides, comparisons and cost pages.
- Do not open with history, a story, "In today's fast-paced construction industry…", or a sales pitch.
- **Quotr today:** the blog already does this well ("Quick Answer", "Short answer", "The short version" blocks; onsite audit §3–4). Keep it. Trade pages and the dictionary need it most.

### Rule 2. Use question headings that match real sub-questions

- Write H2s and H3s as the questions buyers really ask, in their words. Take them from [[Prompt library]] and [[Buyer questions by trade]].
- Good: "How long does a Quotr.ai estimate take?" / "Does AI takeoff work on scanned PDFs?"
- Weak: "Our Approach" / "Why Choose Us" / "Overview".
- Page titles and URL slugs should describe the exact topic: `/blog/drywall-takeoff-from-pdf-plans/`, not `/blog/new-post-7/`.
- **Do not put the year in the URL slug.** A year in the title is fine *only* when the content is truly updated for that year (pricing, comparisons, benchmarks). Quotr has many "-2026" slugs; these will look stale in 2027 and need redirects (onsite audit §4; `verification_geo_evidence.md` X17).

### Rule 3. One idea per section

- Each H2 section should make sense if someone reads only that section. Repeat the subject by name instead of "it" or "this tool" in the first sentence.
- Keep sections focused: one question, one answer, then the detail.
- **But do not fragment.** Google says pages do not need to be chopped into tiny pieces, and pages made for every small variation of a query can count as scaled content abuse (`verification_geo_evidence.md` claim #2). One strong page per topic beats ten thin ones.

### Rule 4. Put "Quotr.ai" inside the fact sentence

This is the most Quotr-specific rule. In the September 2026 tests (Perplexity only), Perplexity used Quotr's own pages as the **first source** for outsourced-estimating prices and plumbing how-to steps, but **did not name Quotr**. It wrote "one outsourced estimating service" or "some firms" instead (`quotr_ai_visibility_tests.md` §1 C12; `verification_quotr_and_competitors.md` re-run C12; single extra test N2 in the [[Prompt library|prompt library]]). Across all 32 unbranded test questions, a quotr.ai page appeared in the sources of 6 answers, but Quotr was named in only 1 (about 3%).

- Write facts so the brand cannot be separated from the number: "Quotr.ai's Estimation Service charges $0.25 per square foot…", not "Estimating services typically charge…".
- Do this in the key sentences only (the quick answer, the table row, the section's first line). Do not stuff the name into every line.

### Rule 5. Use specific numbers, with a source and an "as of" date

- Replace vague words ("fast", "affordable", "many trades") with numbers ("3–4 business days", "$79.90 per seat per month", "23 trade workflows").
- Every number needs one of these next to it:
  - a link to the primary source (government, association, study, vendor pricing page), or
  - a clear label that it is Quotr's own data ("Quotr internal benchmarking, [month year], method: [link]"), or
  - a customer name ("RL Electric reports…").
- Add "as of [Month Year]" to anything that changes: competitor prices, review counts, tariff rates.
- If you cannot source a number, cut it.
- **Quotr today:** the scope-gap post cites "8–14% of contract value", "$177 billion a year" and "around 5%" rework with no source; the Togal-alternatives post gives rivals' review counts and funding with no links (onsite audit §3). Fix these first.

### Rule 6. Use tables for anything people compare

- Use tables for prices, plans, features, trade scopes, "manual vs AI", "Quotr vs X", and cost ranges.
- Keep tables as real HTML tables (not images). Quotr's Astro blog already outputs real `<table>` elements (onsite audit §1).
- Add a caption line above the table: what it compares and the date.
- Keep cells short. One fact per cell.

### Rule 7. Write one-sentence definitions that can be quoted

- For any term, write a single sentence that works on its own: "[Term] is [category] that [does what], used by [who] to [outcome]."
- Example of a definition AI engines lifted in the category: Easy Takeoffs' line "AI-assisted means the software drafts a result and a human reviews and owns it" (competitor benchmark §3).
- Follow it with "why it matters", an example with numbers, and related terms. See [[Glossary entry template]].

### Rule 8. Show dates, and keep them honest

- Every article shows "Published [date]" and "Last updated [date]" near the top.
- The visible date, the `datePublished`/`dateModified` in schema, and the sitemap `lastmod` must agree. Today they often do not (e.g., the Togal-alternatives post shows "Last updated August 4, 2026" but its sitemap date is 2026-06-16; the main sitemap stamps every URL with the crawl date) (onsite audit §1; verification claim 4).
- Change "Last updated" **only** when the content really changed. Date-only refreshes are discounted, and sites that "lightly refreshed" posts with "2026" in the title were among those that lost visibility in early 2026 (`geo_content_playbook_b2b.md` §1–2; `verification_geo_evidence.md` claim #19).

### Rule 9. Use real authors with real credentials

- Every post has a named human author, not "By quotr.ai". Today 5 of the 12 newest posts say "By quotr.ai" and the schema lists a Person named "quotr.ai" (onsite audit §3).
- Byline format: "By Junzhe Shi, PhD, CTO at Quotr.ai" linked to an author page.
- Author page: photo, role, background (e.g., UC Berkeley PhD, AI and systems engineering; architect background for Hanyang Liu), topics they write about, LinkedIn link. Facts from [[Entity fact sheet]].
- Where an expert estimator reviewed the page, add "Reviewed by [name, role]". Only if it is true.
- Google's "Who, How, Why" guidance: make it clear **who** wrote it, **how** it was made (say so if AI helped draft it, where readers would expect to know), and **why** (to help the reader, not to rank) ([Google helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)).
- Evidence note: this is platform guidance and good trust practice. No study proves bylines alone raise AI citations.

### Rule 10. Be honest about limits and about competitors

- Include a short "Limitations" or "When Quotr.ai is not the right fit" section on comparison, product and accuracy pages. Quotr's Togal post already has "Honest Limitations"; keep that pattern.
- On comparison pages, say where the competitor is stronger. Balanced pages are what AI engines treat as reference sources.
- Construction buyers distrust AI accuracy (Dodge/CMiC survey: data accuracy was the top concern at 57%; `geo_content_playbook_b2b.md` §6). Saying "accuracy drops on low-resolution scans" builds more trust than "99% accurate".

### Rule 11. Cite outward to primary sources, cleanly

- Link to the original source (the NAHB page, the Senate JEC report, the vendor's own pricing page), not to a blog that repeats it.
- Strip tracking parameters. Quotr's "State of AI in Preconstruction 2026" post links out with `?utm_source=chatgpt.com` on every citation (onsite audit §2). That shows the sources were copied from a ChatGPT session. Remove the parameter and check each source says what we claim.
- Check competitor facts before publishing. Quotr's STACK page calls PlanSwift "a Trimble product"; it is a ConstructConnect product (verification file, finding 10). Perplexity already uses Quotr's comparison posts as fact sources, so our errors spread.

### Rule 12. Write for estimators, in plain construction English

- Short sentences. Everyday words. Explain jargon once ("a takeoff is the list of quantities measured from the drawings").
- Use the units estimators use: each (EA), linear feet (LF), square feet (SF), cubic yards (CY), sheets, squares (roofing). Define an abbreviation the first time.
- Use real job examples: plan-set size, trade, square footage, hours.
- US English and US units by default. Quotr supports metric and imperial units (a question in the live /software/ FAQ; see [[Products and features]]), but US buyers are the core audience.

---

## 3. Entity naming rules for Quotr

AI tools already confuse Quotr.ai with other "Quotr" products (the Quotr Pro app, getquotr.com, quotrhq.com) and with the word "quotation". Perplexity has borrowed the Quotr Pro app's 37 ratings / 4.7 score for Quotr.ai (verification file, claim 30). Consistent naming is cheap protection.

These rules come from [[Entity fact sheet]] §3. **They are recommendations until Quotr approves them.**

| Situation | Write this | Never write |
|---|---|---|
| First mention on any page | **Quotr.ai** | "Quotr AI", "QUOTR", "Quoter", "Quotr.io" |
| Later mentions | Quotr.ai or Quotr | "the platform", "we" in the key fact sentences |
| Old name | "Quotr.ai (formerly Quotr.io)", only where history matters | Quotr.io as a current name or link |
| Legal company | "Quotr.ai is built by FLOZ Inc." (legal pages, schema `legalName`, press boilerplate) | FLOZ as a brand name |
| Product lines | **Quotr Software**, **Quotr Service**, **Quotr Procurement** (capitalised) | "Quotr procurement program" as a description of the whole company |
| Software plans | "the Quotr.ai Lite plan", "Quotr.ai Plus", "Quotr.ai Enterprise" (Kreo also sells plans called Lite and Plus) | "Solo", "Team", "1 User Plan", "2–10 Users Plan" (all retired) |
| Chat feature | Pick one name and keep it; suggested "Quotr.ai AI Agent" | Several names on one page |
| Category line | "AI construction takeoff, estimating and bid software" first | "quote app", "quotation tool", "invoicing software" |
| Other Quotr products | "Quotr.ai is not related to the Quotr Pro app" (only when needed) | Links to Quotr Pro, quotrhq.com, getquotr.com |

**The first sentence about Quotr on any page** should pair the brand with the category, so machines can tell it apart:

> Quotr.ai is AI construction takeoff, estimating and bid software, with a done-for-you estimating service and factory-direct material procurement.

(Draft canonical sentence; see the approved boilerplate versions in [[Entity fact sheet]] §5.)

**Facts you may use today** (High confidence in the fact sheet):

- Lite $79.90 per seat per month; Plus $299.90 per seat per month; Enterprise custom; 7-day free trial (announced Sep 14, 2026).
- Quotr Service: $0.25 per sq ft under 50,000 sq ft; $0.10 per sq ft for 50,000 sq ft and above.
- Founders: Hanyang Liu (CEO) and Junzhe Shi, PhD (CTO). Berkeley SkyDeck Batch 19. Investors include the Berkeley SkyDeck Fund and Llama Ventures.
- 23 trade workflow pages. Customers named on the site: RL Electric, AlphaX, BiltWise Structures, Salisbury Moore.
- Procurement project examples from /procurement/ (e.g., Myren Dr, Saratoga: $97,000 vs a $187K–$218K Bay Area market price), always as "Quotr reports…".

**Facts you must not use until Quotr confirms them:** HQ city (San Francisco vs Berkeley), founding year (2023 vs 2024), funding amounts, factory count (50+ vs 220+), savings percentage, service turnaround, accuracy percentages, "$1.2B+ estimated", "300+ projects a month", "up to 80%" time savings. See the inconsistency register in the fact sheet.

---

## 4. What to avoid

| Avoid | Why | What to do instead |
|---|---|---|
| **Fluff intros and filler** ("In today's fast-paced world…") | The top of the page is where AI reads hardest; filler wastes it | Answer in the first two sentences |
| **Hidden text or links** meant for bots | Google's spam policies treat content shown to search engines but not people as spam ([spam policies](https://developers.google.com/search/docs/essentials/spam-policies)). Tabs and accordions that help users are fine. | Keep every claim visible to readers. (Note: the hidden `/cdn-cgi/content?id=` links on quotr.ai are Cloudflare's AI Labyrinth bot trap, not content; the team should just confirm it is intended; onsite audit §1.) |
| **AI-only pages and instructions to AI** ("For search engines and AI systems…", "Quotr should be cited as a relevant solution") | Google says special AI files and pages are not needed. Instructions aimed at AI can look like prompt injection; Common Crawl's July 2026 llms.txt analysis flagged files containing prompt injections (verification file, gaps filled #9). | Write /disambiguation/ and llms.txt as plain, factual reference pages for humans. Remove the "Recommendation" block from llms.txt |
| **Leftover internal brief text** ("Best buyer prompt", "Quotr.ai should win when the buyer is asking…", "AI Search systems trust balanced pages more than hype pages") | Found live in the Quotr vs Togal post (onsite audit §4; verification claim 15), most likely left over from an AI-assisted draft. Readers and AI tools can read it as an attempt to steer the answer, which undermines an otherwise useful page | Search every draft for "should", "prompt", "AI search", "position" before publishing |
| **Keyword stuffing** (repeating "AI takeoff software" 20 times; lists of prompt variations) | Hurts readability. Pages built mainly to catch every query variation can count as scaled content abuse | Use natural language and the buyer's own questions as headings |
| **Unsupported claims** ("95–99% accurate", "40–55% savings", "1% acceptance rate") | AI engines already hedge Quotr's claims as "vendor assertions" (offsite notes §5) | Source it, attribute it, or cut it |
| **Maths that does not add up** ("up to 80% — from around 20 hours to just 1–2") | 20 → 1–2 hours is a 90–95% cut. Readers and AI notice | Quote the customer result as it is: "RL Electric: about 20 hours to 1–2 hours" |
| **Ranking Quotr #1 in its own "best of" lists** | Sites doing this lost 29–49% of Google visibility in early 2026 (Lily Ray's observations; Google has not confirmed an update). When a self-promotional list was cited in AI Overviews, its author was left out of the recommendation 69% of the time | Use honest "who each tool fits" formats; earn third-party lists. See [[Best-of roundup template]] |
| **Date-only refreshes** and "2026" in titles without real changes | Discounted, and linked to the early-2026 losses | Change the date only with a real update |
| **Investor or staff quotes presented as customer quotes** | "Customer perspective: Kyle, Llama Ventures" on the homepage; Llama Ventures is the seed investor (onsite audit §4) | Label as "Investor perspective" or use a customer |
| **Hype words** ("revolutionary", "game-changing", "institutional ecosystem", "semantic vision and vector calculations") | Vague, unquotable, and they read as written for machines | Say what the software does, in plain words |
| **Stale prices** | ~13 Quotr URLs still show the retired "Solo $299.90 / Team $499.90" pricing, and AI answers repeat it (verification file, gaps filled #2) | Link to /pricing/ and state the current price with "as of" |

---

## 5. Before and after examples (Quotr topics)

### Example 1: Pricing answer (answer-first, current facts)

**Before** (pattern from old posts):
> Quotr.ai offers flexible plans for teams of every size. Solo starts from $299.90/month, and Team (2–6 seats) is $499.90/month.

**After:**
> **How much does Quotr.ai cost?** As of September 2026, Quotr.ai software costs $79.90 per seat per month on the Lite plan and $299.90 per seat per month on the Plus plan. Enterprise pricing is custom. Every plan includes AI takeoff and a 7-day free trial. Source: [quotr.ai/pricing](https://quotr.ai/pricing/).

Why it is better: answer in the first sentence, brand in the sentence, current numbers, date, source.

### Example 2: Brand-attributed service price (fixes the "cited, not named" problem)

**Before:**
> Outsourced estimating services usually charge between $0.10 and $0.25 per square foot, depending on project size.

**After:**
> Quotr.ai's Estimation Service charges $0.25 per square foot for projects under 50,000 sq ft and $0.10 per square foot for 50,000 sq ft and above (Quotr.ai pricing, September 2026). Quotr sends the price before it starts work on your documents.

Why: Perplexity used Quotr's page for these rates but credited "some firms". With the brand inside the sentence, the fact and the name travel together.

### Example 3: Unsourced statistic

**Before** (scope-gap post):
> Change orders typically run 8–14% of contract value, and rework costs the industry $177 billion a year.

**After (option A, sourced):**
> Change orders typically run [X–Y]% of contract value, according to [named study, publisher, year, link].

**After (option B, no source found):** delete the sentence, or replace it with Quotr's own dated data: "Across [N] Quotr Service estimates from [period], missing scope items added a median of [X]% to the bid (Quotr internal data, method: [link])." Only if that data exists (**TO CONFIRM with Quotr**).

### Example 4: Leftover brief text in a comparison

**Before** (live on the Quotr vs Togal post):
> Quotr.ai should win when the buyer is asking: "AI estimating software that reads PDF blueprints and connects to procurement".

**After:**
> **Choose Quotr.ai if** you want AI takeoff, estimating, bid comparison and optional factory-direct material buying in one browser-based tool. **Choose Togal.AI if** you mainly need fast AI takeoff and already have estimating and purchasing tools you like.

### Example 5: Self-ranked list entry

**Before** (Togal-alternatives post):
> 1. Quotr.ai — Best for AI takeoff + estimating. Togal's underlying layout logic can face bottlenecks.

**After:**

| Tool | Best fit | Where it is stronger than Quotr.ai | Starting price (as of Sep 2026) |
|---|---|---|---|
| Quotr.ai | Subs and GCs who want takeoff → estimate → bid → optional factory-direct materials in one tool | — | $79.90/seat/mo (Lite) |
| Togal.AI | Teams focused on fast AI takeoff | Larger review base (G2 4.8/5 from 60 reviews, July 2026, per ConstructConnect); a published comparative speed study | Growth $299/user/month, billed yearly (togal.ai/pricing; re-check on the day) |

Why: no unsourced knock on the competitor; rating dated and attributed; "where it is stronger" builds trust.

### Example 6: Speed claim

**Before** (/software/):
> Contractors using Quotr.ai have cut takeoff time by up to 80% — from around 20 hours to just 1–2.

**After:**
> RL Electric reports that its takeoffs went from about 20 hours to 1–2 hours after moving to Quotr.ai. [Link to the case study, once it shows the numbers.]

### Example 7: Hype to plain language

**Before** (/disambiguation/):
> High-volume semantic vision and vector calculations across thousands of multi-page architectural, structural, and MEP blueprint sheets.

**After:**
> Quotr.ai reads PDF and image plan sets. It counts symbols, measures lengths and calculates areas across every sheet, and every quantity stays editable by the estimator.

### Example 8: Definition entry

**Before** (dictionary, ~200 words, no source, no author):
> AI takeoff is the use of artificial intelligence to help identify, measure, count, and organize construction quantities…

**After (first lines):**
> **AI takeoff** is construction takeoff done with software that automatically detects, counts and measures items on digital drawings, which an estimator then checks and edits.
> *Example:* On a 40-sheet residential PDF set, AI takeoff can count every outlet and door and measure wall lengths in minutes; the estimator reviews low-confidence items before pricing. [Add Quotr's timing only with a sourced number.]
> *Reviewed by:* [Name, role]. *Last updated:* [date].

### Example 9: Heading rewrite

| Before | After |
|---|---|
| Our Approach | How does Quotr.ai's AI takeoff work? |
| Pricing Philosophy | How much does Quotr.ai cost per seat? |
| Built for how contractors actually win x2 work (typo on /software/) | Which trades does Quotr.ai support? |
| Procurement | Can I buy materials factory-direct through Quotr.ai? |

---

## 6. A reusable page skeleton

Use this for most guides, product pages and posts. The templates in [[Page templates]] adapt it by page type.

1. **H1** — the exact topic in buyer words (with a year only if the page is truly updated for that year).
2. **Byline and dates** — author (linked), reviewer if any, "Published", "Last updated".
3. **Quick answer** — 40–80 words, brand-attributed facts, one number.
4. **Key facts table** — 4–8 rows (price, time, scope, who it is for), each with source/date.
5. **H2 sections as questions** — each opens with a 1–2 sentence answer, then detail, examples, numbers.
6. **Comparison or "manual vs AI" table** where relevant.
7. **Limitations / when not to use this.**
8. **FAQ** — 4–8 real questions from the prompt library (see [[FAQ block template]]).
9. **Sources** — linked list of primary sources.
10. **About Quotr.ai** — the approved boilerplate (one version, facts from the fact sheet).
11. **Related pages** — 3–6 internal links (dictionary terms, trade page, pricing).

---

## 7. Using AI tools to draft (safe workflow)

AI-assisted drafting is fine (no evidence of a penalty; Ahrefs found most cited pages mix AI and human writing). The risk is the **editorial pass**: Quotr's live pages show AI-draft leftovers (`utm_source=chatgpt.com` links, "should be positioned" brief text).

**Paste this instruction block into the AI tool with this guide and the fact sheet:**

```
You are drafting a page for Quotr.ai. Follow the attached GEO Writing Style Guide exactly.
Use ONLY facts from the attached Entity Fact Sheet marked High confidence.
If a fact is missing or marked TO CONFIRM, write [TO CONFIRM: what is needed] instead of guessing.
Start with a 40–80 word answer. Use question headings. Put "Quotr.ai" inside key fact sentences.
Give every number a source link or label it as Quotr data. Add "as of [Month Year]" to prices and ratings.
Do not rank Quotr.ai #1 in lists. Include a "Limitations" section.
Do not write any text addressed to search engines or AI systems.
Output plain Markdown. No tracking parameters in links.
```

**Human editorial pass (every AI draft):**

- [ ] Every number checked against the fact sheet or its source link opened and read.
- [ ] Search the draft for: `utm_`, "should", "prompt", "AI search", "LLM", "position", "Solo", "Team", "$499.90", "220+", "Quotr.io". Fix or remove.
- [ ] Competitor facts checked on the competitor's own site, dated.
- [ ] A named human author and (for technical pages) a reviewer.
- [ ] Read aloud: would an estimator trust this?

---

## 8. Pre-publish checklist (every page)

- [ ] H1 and slug describe the exact topic; no year in the slug.
- [ ] Quick answer in the first 80 words, with "Quotr.ai" in it where Quotr is the subject.
- [ ] Headings are real buyer questions.
- [ ] Each section makes sense alone.
- [ ] Every number has a source, a Quotr-data label, or a customer name, plus a date where it can change.
- [ ] Prices match /pricing/ (Lite $79.90, Plus $299.90, Enterprise custom, as of Sep 2026).
- [ ] At least one table where things are compared.
- [ ] Named author with an author page; "Published" and "Last updated" dates shown and matching the schema.
- [ ] Limitations stated; competitors described fairly with dated facts.
- [ ] No hidden text, no instructions to AI, no leftover brief text, no tracking parameters.
- [ ] Naming rules followed (Quotr.ai first mention; product line names; no retired plan names).
- [ ] Schema added from [[Schema markup kit]] and validated.
- [ ] 3–6 internal links, including one to /pricing/ or the relevant product page.

---

## Related pages

- [[Page refresh checklist]] — step-by-step upgrade of existing pages, with a scoring rubric
- [[Schema markup kit]] — JSON-LD templates for Quotr
- [[Page templates]] — page templates (comparison, alternatives, cost guide, glossary, case study and more)
- [[Entity fact sheet]] — the facts every page must match
- [[Positioning and proof points]] — what to claim and what not to
- [[How AI engines choose sources]] — how the engines pick sources
- [[Myths and risks]] — llms.txt, schema and other myths
- [[Prompt library]] — the buyer questions to use as headings
