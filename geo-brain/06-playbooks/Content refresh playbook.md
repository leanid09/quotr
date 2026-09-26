---
type: playbook
description: 'How the whole blog is kept healthy: the monthly refresh loop, the health score in every article note, how to choose keep, update, rewrite, merge or retire, and the rules that protect rankings and trust.'
last_verified: 2026-09-26
verify_every_days: 180
---
# Content refresh playbook

> [!abstract] What this page is for
> This is the programme that keeps all 96 Quotr blog posts accurate, trusted and easy for search engines and AI engines to use. It explains the monthly loop, how every post gets its health score, how to choose the right action, and the rules that protect rankings. For the step-by-step edit of one page, use [[Page refresh checklist]].

> [!info]- Sources
> Vault notes: [[Page refresh checklist]], [[Optimize vs create]], [[GEO writing style guide]], [[Entity fact sheet]], [[Content priorities]], [[30-60-90 plan]], [[KPIs and dashboard]], [[Tracking set]], [[Tracking setup]], [[AI visibility baseline]], and tasks [[A1 Agree and sign off one fact sheet|A1]], [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]], [[A3 Fact-fix sweep, part 2 - every other conflicting fact|A3]], [[A6 Editorial sweep|A6]], [[A7 Named author bylines and author pages|A7]], [[A8 Put the Quotr name inside key facts on the pages AI already reads|A8]], [[A9 Sitemaps and lastmod dates|A9]], [[A12 Merge duplicate pages|A12]], [[A16 Add a human edit and fact-check step for AI-assisted drafts|A16]]. Companion pages: [[Blog health audit]], [[What went wrong]], [[Google search updates 2025-2026]], [[Search Console audit playbook]], [[Refresh plan Q4 2026]].
>
> Data files (read-only, 2026-09-26): the per-post dataset for the 96 posts and their article IDs; the blog statistics file; the 19 "what went wrong" findings (W-01 to W-19), using their evidence-check and fairness-check wording; the overlap map (20 groups of posts that answer the same buyer question); and the Google briefing with the Google claims file behind it (claim IDs such as RANK-21). RANK and GSC claims were found by live web search on 2026-09-26 and not re-checked. The other claim areas come from the 2026-09-25 research. No Quotr Search Console data has been seen yet.
>
> Codes such as C12, V1 or B4 name single AI test prompts from the 2026-09-25 test runs ([[AI visibility baseline]]).

---

## The short version

- Fix a few posts well every month. Do not try to rewrite all 96 at once.
- Every post has a health score out of 100, built from six areas. The same score sits in every article note, so you can sort and compare posts.
- Work in this order: old prices and wrong facts, then the posts AI already cites, then merges, then the rest.
- Change a post's date only after a real edit. Never bulk-rename "2026" to "2027".
- Hold merges, redirects and re-dating while a Google update is rolling out. The September 2026 spam update began on 2026-09-24 and may run to about 2026-10-08 (RANK-21).
- Every refresh ends with a Log line in the article note, a search check after 28 days and an AI re-test after 2-4 weeks.
- This page is the programme. The edit steps for one page live in [[Page refresh checklist]].

---

## How the refresh programme works

### The monthly loop

| Step | What happens | Who | Time needed |
|---|---|---|---|
| **1. Pick** | Open the Refresh queue (in "Order of work" below). Take posts from the top until the month's capacity is used. Skip merges while a Google update is rolling out. | GEO consultant with Quotr's marketing lead | Part of the monthly review early each month ([[30-60-90 plan]], working rhythm) |
| **2. Record the "before"** | Note the post's clicks, impressions and AI impressions in Search Console (Google's free report on how a site does in search), once Quotr gives access. Run the post's buyer questions in AI engines. Score the post. | GEO consultant | About 15 minutes to record, plus 10-15 minutes to score ([[Page refresh checklist]], Step 1 and §4) |
| **3. Fix** | Edit the post with [[Page refresh checklist]] Steps 2-7. For a merge, follow its section 5. | Quotr marketing (writer). Dev for redirects, schema and sitemap | See the Effort line in each article note. S = up to 2 working days; M = 3-10 working days (the scale in [[30-60-90 plan]]) |
| **4. Check** | A named editor checks the post against the [[Entity fact sheet]] and the pre-publish checklist in [[GEO writing style guide]] (task A16). A founder approves any new Quotr fact. | Named editor at Quotr | Our estimate: under an hour a post (not measured) |
| **5. Publish and ask for a re-crawl** | Publish. Ask Google and Bing to read the page again. Add a dated note (annotation) on the Search Console chart. | Quotr marketing or dev | Our estimate: a few minutes a post |
| **6. Log** | Update the article note and add a Log line (see "After each refresh"). Add one [[Changelog]] line for the batch. | GEO consultant | Our estimate: 5-10 minutes a post |
| **7. Measure** | Re-run the post's buyer questions after 2-4 weeks. Compare Search Console 28 days before and after. | GEO consultant | Part of the monthly tracking run ([[Tracking set]]) |

### How much to do each month

- The vault recommends **8-12 pieces a month in total**, new and rebuilt together ([[Content priorities]]).
- **October 2026** is mostly clean-up: about 50% fixing facts and merging, 25% refreshing ([[Optimize vs create]]).
- **November-December 2026:** about 25% of the content team's time on refresh. **January-March 2027:** about 20% ([[Optimize vs create]]).
- These splits are planning guides, not measured best practice. Adjust them once Search Console data arrives.
- Fact fixes come on top of the monthly batch. They are small and urgent (our suggestion).

### A suggested month

| Week | Refresh work |
|---|---|
| 1 | Monthly AI tracking run and review. Pick this month's batch. Record the "before" numbers. |
| 2-3 | Edit, check and publish. Request re-crawls. Add annotations. |
| 4 | Log each post. Measure the posts refreshed 28 or more days ago. |

This calendar is our suggestion. It fits the 30-minute weekly check-in and the monthly review in [[30-60-90 plan]].

### Who does what

| Role | Refresh jobs |
|---|---|
| **GEO consultant** (Leanid) | Keeps the queue. Scores posts. Records before and after numbers. Re-tests buyer questions. Updates article notes and the [[Changelog]]. Reports each month. |
| **Quotr marketing** | Edits posts. Moves the best parts across in merges. Requests re-crawls. |
| **Named editor** (Quotr) | Signs off every refreshed post before it goes live (task A16). |
| **Founder** (CEO or CTO) | Approves any new Quotr fact or number (task A1). Named author or reviewer where they wrote or checked the post. |
| **Dev** | 301 redirects, schema dates, sitemap dates (task A9), robots.txt (the file that tells crawlers what they may read). |

Roles are suggestions, and names are TO CONFIRM with Quotr ([[30-60-90 plan]]). The consultant's share of this work is scoped in [[Retainer scope and value case]].

---

## How we score a post's health

Every article note has a health score. It shows how healthy the post is and lets you compare posts. Score six areas from **0** (very weak) to **5** (strong).

**Health score = sum of the six area scores ÷ 30 × 100**, rounded to a whole number.

| Area | What it asks | Example from Quotr's blog |
|---|---|---|
| **Freshness** | Are the prices, facts and dates current, and does every date tell the truth? | [[BP-43 best togal ai alternatives 2026\|BP-43]] shows "Last updated August 4, 2026", but its blog sitemap date is 2026-06-16. It also still gave "from $299.90/month" as Quotr's entry price after the 2026-09-14 price change. |
| **Accuracy** | Does every fact match the [[Entity fact sheet]] and each competitor's own website? | [[BP-51 stack alternative\|BP-51]] calls PlanSwift "a Trimble product". PlanSwift belongs to ConstructConnect. |
| **Trust** | Can a reader see who wrote it, where each number comes from, and that rivals are treated fairly? | [[BP-15 quotr vs togal ai comparison 2026\|BP-15]] is signed "By quotr.ai" and still carries brief text such as "Quotr.ai should win when the buyer is asking…". |
| **Structure** | Can a reader, or an AI engine, lift a clear answer: answer first, question headings, tables, and "Quotr.ai" inside each key fact? | BP-15 opens with a "Quick Answer" block and has 5 tables. But Perplexity used [[BP-82 outsource construction estimating\|BP-82]] as its first source and credited Quotr's rates to "one outsourced estimating service", probably because the sentence does not name Quotr (inference: the page was not re-read). |
| **Visibility** | Is the post indexed (stored by Google so it can be shown), found in search, and used by AI engines? | BP-82 was Perplexity's first source on both runs of the same question and on a re-check (test C12). [[BP-05 construction takeoff guide\|BP-05]] did not come back in 5 targeted searches with a web search tool. That tool is not Google, and the pass could not be repeated, so this is a lead to check in Search Console, not proof. |
| **Uniqueness** | Does it say something only Quotr can say, and is it the only Quotr post for its buyer question? | [[BP-32 best togal ai alternatives\|BP-32]] and BP-43 answer the same "Togal.AI alternatives" question. [[BP-23 tariff impact construction costs 2026 steel aluminum copper\|BP-23]] has no Quotr data in its record. In one Perplexity test on its tariff question (S11), the answer cited public, media and industry sources and no software vendor. |

### Bands

| Band | Health score | Sum of the six areas | Usual next step |
|---|---|---|---|
| **Good** | 75-100 | 23-30 | Keep. Update when a fact changes. |
| **Fair** | 55-74 | 17-22 | Update. |
| **Poor** | 35-54 | 11-16 | Update or rewrite. |
| **Critical** | 0-34 | 0-10 | Rewrite, merge or retire. |

The "usual next step" is a starting point. The decision table in "Choosing the action" makes the final call.

**Worked example (made-up numbers):** Freshness 2 + Accuracy 1 + Trust 2 + Structure 4 + Visibility 3 + Uniqueness 2 = 14. Then 14 ÷ 30 × 100 = 46.7, rounded to 47. The post is **Poor**.

### What 0 and 5 look like

| Area | 0 looks like | 5 looks like |
|---|---|---|
| Freshness | A retired price or out-of-date fact. Dates disagree, or were changed without an edit. | Every changing fact is current and dated "as of". The visible date, schema and sitemap agree. |
| Accuracy | A wrong fact about Quotr or a competitor. | Every fact matches the fact sheet and the competitor's own site. No conflict with other Quotr pages. |
| Trust | "By quotr.ai", unsourced numbers, leftover brief text, Quotr ranked #1 with no stated criteria. | A named author with an author page. Every number sourced, or labelled as Quotr data with a method. A fair "when to choose something else" section. |
| Structure | A wall of text. The answer is buried. The brand is missing from the key facts. | The answer comes first. Question headings, useful tables, and "Quotr.ai" inside the key fact sentences. |
| Visibility | Not indexed, never found in search, never used by AI. | Indexed. It ranks or has AI impressions, and AI cites it for its buyer question. |
| Uniqueness | Another Quotr post answers the same question. Generic content anyone could write. | The only Quotr page for its question, with Quotr's own data, examples or screenshots. |

**Notes on scoring**
- Score every post before and after each refresh.
- The first scores (2026-09-26) rest on limited evidence. The web search budget ran out, and few pages were read in full ([[Blog health audit]]). Re-score each post after reading the live page.
- [[Page refresh checklist]] has a more detailed 24-point rubric for one page. Use it while editing if it helps. The article notes store only the six-area score.

---

## Choosing the action

### The five actions

| Action | Plain meaning | Web address |
|---|---|---|
| **Keep** | No work now. Update only when a fact on the page changes. | Stays the same |
| **Update** | Fix specific problems: facts, prices, sources, author, dates, the brand inside key facts, a missing section. The page keeps its shape. | Stays the same |
| **Rewrite** | Rebuild the content because the page is weak but its buyer question matters. | Usually stays the same. A new address only if the old one holds a year or a number that is no longer true, with a 301. |
| **Merge** | Move the best parts into the stronger Quotr post that answers the same question. Then forward the old address. | Old address 301s to the keeper |
| **Retire** | Take down a post that no buyer needs and that no other post can absorb. Use this rarely. | 301 to the closest related page, or no redirect (see below) |

### The decision table

**Whatever the action, fix wrong facts and old prices first.** Do this even on a post you will merge later ([[Optimize vs create]]).

Then work down the questions. Stop at the first "yes".

| # | Question | If yes |
|---|---|---|
| 1 | Does another Quotr post answer the same buyer question for the same reader, and is that post stronger? | **Merge** into it |
| 2 | Is there no buyer question worth owning, and does Search Console show no clicks, no AI impressions and no links? | **Retire**, with Quotr's agreement |
| 3 | Is the health poor or critical, and does the buyer question matter (a tracked or High-priority prompt)? | **Rewrite** |
| 4 | Does it have wrong or old facts, missing sources, a company byline, or fair health? | **Update** |
| 5 | None of the above | **Keep** |

### How to pick the keeper in a merge

Use this order ([[Optimize vs create]]):
1. The page AI engines already cite in the tests.
2. The page with more Search Console clicks, impressions, AI impressions and backlinks (links from other websites).
3. The page with a year-free, descriptive web address.

Before any merge:
- Read both pages. Most pages in the overlap groups were never read in full (overlap map).
- Pull Search Console data for both web addresses.
- Posts under about 8 weeks old have little data. Decide on fit with the buyer question, not on traffic (overlap map).

### Examples from the overlap map

| Group | Posts | Decision | Why |
|---|---|---|---|
| **Togal.AI alternatives** (G01, high confidence) | [[BP-32 best togal ai alternatives\|BP-32]], [[BP-43 best togal ai alternatives 2026\|BP-43]], [[BP-15 quotr vs togal ai comparison 2026\|BP-15]] | Keep BP-32. Merge BP-43 into it. Keep BP-15 separate and update it. | BP-32 was cited in V1, the only core unbranded answer that named Quotr, and its address has no year. BP-43 holds newer text, so move its wider list across; do not just redirect it. BP-15 answers a different, brand question ("Togal vs Quotr"). Remove its brief text and add Quotr's current prices. |
| **Outsourced estimating services** (G02, high) | [[BP-82 outsource construction estimating\|BP-82]], [[BP-79 construction estimating services\|BP-79]], [[BP-85 commercial estimating services\|BP-85]], [[BP-87 quantity takeoff services\|BP-87]], [[BP-84 construction estimating services california\|BP-84]], [[BP-90 outsourcing vs hiring an estimator\|BP-90]] | Keep BP-82. Merge BP-79 into it. Keep BP-85 as a truly commercial page and BP-87 for quantities only. Keep BP-84 only if it gets real California content; otherwise merge it. Decide on BP-90 after reading both pages. | BP-82 was Perplexity's first source for the outsourced-estimating price question. BP-87 sells a different deliverable (quantities, not a priced estimate). BP-90 serves a different reader: GCs and subs asking "hire or outsource?". |
| **What AI estimating software is** (G09, medium) | [[BP-45 what is ai construction estimating software\|BP-45]], [[BP-11 how ai construction estimating works\|BP-11]], [[BP-71 how ai construction takeoff works in 2026\|BP-71]] | Keep BP-45. Merge BP-11. Merge BP-71 only if Search Console shows it earns nothing BP-45 cannot hold. | One page that answers "what is it" and "how does it work" is a better bet than three thin ones (inference). |
| **PlanSwift** (G15, medium) | [[BP-81 best planswift alternatives 2026\|BP-81]], [[BP-20 quotr ai vs planswift ai takeoff procurement comparison 2026\|BP-20]] | Keep both. Give each a clear role and link them. | "What instead of PlanSwift?" and "Quotr vs PlanSwift" are different questions. |
| **MEP, HVAC and electrical services** (G18, low) | [[BP-95 mep estimating services\|BP-95]], [[BP-94 hvac estimating services\|BP-94]], [[BP-91 electrical estimating services\|BP-91]] | Keep all three for now. | Trade service pages are normal. HVAC and MEP are the closest pair. Merge HVAC into MEP only if Search Console shows they share the same searches. All three went live in September, so wait for data. |

[[Page refresh checklist]] (section 2c, "Consolidation candidates") was written before the overlap map. It names BP-43 as the Togal keeper and suggests one hub for the service posts. Where the two pages differ, follow this page and the overlap map.

All 20 groups are in [[Blog health audit]]. The ones already marked for merging or retiring are in this view:

![[Articles.base#Merge or retire]]

### When a 301 redirect is needed

A **301 redirect** is a permanent forward from an old web address to a new one. It passes visitors and search engines to the new page.

| Situation | 301 needed? |
|---|---|
| Merge: the old post into the keeper | **Yes.** Old address to the keeper, page to page. |
| A rewrite moves the post to a new address (for example to drop a year, or a number that stops being true, such as the "72 hours" in [[BP-25 quotr developer desk underwriting grade estimates 72 hours\|BP-25]] if Quotr confirms a different turnaround) | **Yes.** Old address to the new one. |
| Retire a post that has a close relative | **Yes.** To that relative. |
| Retire a post with no relative | **No.** Either keep it for visitors with "noindex, follow" (a tag that asks search engines not to show the page), or remove it. |
| Update or rewrite on the same address | **No.** |
| Keep | **No.** |

**Never** forward everything to the homepage ([[Optimize vs create]]).

**After every 301:**
- Update every internal link that pointed to the old address.
- Take the old address out of the sitemap (a list of a site's pages for search engines). Make sure the keeper is in it.
- Update llms.txt (a plain-text summary of the site for AI tools) if it lists the old address.
- Update the `quotr_url` in the prompt notes that pointed to the old address.
- Request a re-crawl of both addresses.
- Watch the keeper in Search Console for 4-8 weeks ([[Optimize vs create]]).

**Timing:** do not add redirects while a Google update is rolling out (see rule 8 below).

---

## Rules that protect rankings and trust

### 1. Change dates only after real changes

- Change the visible "Last updated" date only when the content really changed.
- The same goes for **dateModified** (the "last changed" date in the page's hidden code, called schema).
- **Real changes:** a corrected fact or price, a new source, a new section, new Quotr data.
- **Not real changes:** a typo fix, new wording with the same facts, a new year in the title.
- Google's May 2026 AI guide names "valuable, unique, non-commodity content" as the main factor (FRESH-12, QUALITY-06). A new date on its own adds none of that (inference).
- Google's John Mueller has warned against date-only updates, as relayed by Ahrefs (FRESH-06, QUALITY-14; second-hand, low confidence).
- Posts "lightly refreshed with '2026' in the title" were among the pages that lost Google visibility in early 2026 (FRESH-08, QUALITY-11). This is a practitioner observation; Google has not confirmed it.
- Make three dates agree: the visible "Last updated", schema dateModified and the sitemap **lastmod** (the "last changed" date in the sitemap). Task A9 fixes the site side.
- Today they disagree. On 2026-09-25 the main sitemap showed the fetch day for every page (FRESH-15). BP-43's page date and sitemap date are 49 days apart (W-16).
- Add a short visible note: "Updated [date]: [what changed]" ([[Optimize vs create]]).
- The price fix is a real change, so it may move the date (W-01).

### 2. Keep one source for prices

- Prices were typed into each post by hand. Quotr changed its prices on 2026-09-14.
- On 2026-09-25, eleven days later, about 13 posts on the vault's list still showed the retired prices. 3 more may (W-01).
- Only 2 of them were read on the live page. The rest were seen in search-index text and AI answers, which can lag (W-01).
- In fairness, the old price was right when most posts were written, and 11 days is a short window (W-01).
- Use one approved line from the [[Entity fact sheet]]: "Quotr.ai Lite $79.90 per seat per month; Plus $299.90; Enterprise custom (as of [date]; see /pricing/)".
- Write "Quotr.ai Lite", not just "Lite". Kreo also sells plans called Lite and Plus (task A2).
- Better still: pull the price from one shared block or CMS field (CMS = the tool used to edit the website). Then one change updates every post (W-01).
- Do the same for other repeated facts: the "About Quotr.ai" text, turnaround and factory count (W-03).
- **When a price changes:** on the same day, update the posts, llms.txt and schema. Request re-crawls. Email third-party sites that copied the old price (W-01).

### 3. Use named authors

- Replace "By quotr.ai" with a real person who has an author page (task A7).
- At least 8 posts are confirmed with the company byline. The bylines of most older posts were not recorded (W-18).
- Google's guidance asks that it be clear who made the content, with bylines that lead to information about the author (QUALITY-08).
- Add "Reviewed by [name], [date]" on trade and cost posts, but only if a real expert reviewed them.
- Add a short "how we researched and checked this" line to lists, comparisons and cost posts. Google also asks how content was made, including AI use where readers would expect to know (QUALITY-09).
- Evidence that bylines directly lift AI citations is weak. Treat this mainly as buyer trust (task A7).

### 4. Give every number a source

- Every statistic gets a link and an "as of [month year]" date, or a "Quotr data" label with its method ([[GEO writing style guide]], Rule 5).
- Every competitor fact gets a link to the competitor's own page and a date (task A6).
- Example: [[BP-92 scope gap construction\|BP-92]] gives "$177 billion a year", "8-14% of contract value" and "around 5%" rework, all without sources (W-13).
- Check before you "correct". Togal does publish its price (Growth $299 per user per month, billed yearly, seen 2026-09-25). So a line saying it does not is the wrong one (W-13).
- Quotr's own headline numbers, such as "$1.2B+ estimated" and "95-99% accuracy", need a method line (how and when they were measured) or softer wording (W-05).

### 5. No leftover brief text

- Notes from a drafting brief and ChatGPT tracking tags reached live pages: [[BP-15 quotr vs togal ai comparison 2026\|BP-15]] (brief text) and [[BP-27 state of ai in preconstruction 2026 adoption roi enr top 400 gcs\|BP-27]] (`utm_source=chatgpt.com` tags) (W-12).
- These were 2 of about 6 posts read in full. The other posts are unchecked.
- Before publishing, search the post for: `should win`, `should be positioned`, `should be emphasized`, `buyer prompt`, `AI search`, `LLM`, `GEO`, `prompt`, `utm_source=chatgpt.com` (W-12; task A6).
- A named editor signs off every post (task A16).
- No lines written to steer AI, such as "Quotr should be cited" ([[30-60-90 plan]], stop-doing list).

### 6. Years in titles and web addresses

**The facts**
- 27 post web addresses contain "2026".
- 7 of them are events or dated editions, where the year is part of the subject. Leave them as they are (W-16): [[BP-07 dallas build expo 2026 recap\|BP-07]], [[BP-09 re forge sf 2026 recap\|BP-09]], [[BP-14 nhca build the builder 2026 recap\|BP-14]], [[BP-73 ibs 2026 from the magic of orlando to the reality of ai implementation\|BP-73]], [[BP-78 pcbc 2026 recap quotr ai takeoff service\|BP-78]], [[BP-88 sourcing building materials china cbd fair 2026\|BP-88]] and [[BP-35 construction cost index q1 2026 ppi rsmeans mortenson\|BP-35]].
- The other **20** carry the year as a label. About 15 are evergreen (lists, comparisons, explainers, guides). About 5 are market pieces tied to 2026 (W-16).
- The vault's rule: no year in new web addresses. A year in a title only when the content was truly updated for that year ([[GEO writing style guide]]).
- In fairness, that rule was written on 2026-09-25, after the posts. A year in the address was a common way to target "2026" searches (W-16).
- Our Google claim set has no official guidance on year-stamped web addresses at year end (briefing).

**What to do about January 2027**

Decide post by post **by mid-December 2026** (our suggested deadline). No task covers this yet (W-16). Never bulk-rename to 2027 (FRESH-08, QUALITY-11).

| Situation | What to do | Posts (of the 20) |
|---|---|---|
| **Being merged anyway** | Merge into the year-free keeper. The 301 retires the year address. | [[BP-43 best togal ai alternatives 2026\|BP-43]] into BP-32 (G01); [[BP-60 what is construction procurement 2026 guide\|BP-60]] into [[BP-69 construction procurement process\|BP-69]] (G05); [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps\|BP-70]] into [[BP-03 construction cost trends 2026\|BP-03]] (G07); [[BP-71 how ai construction takeoff works in 2026\|BP-71]] into BP-45 if confirmed (G09) |
| **Evergreen, and it gets a real refresh** (every entry, price and fact re-checked) | Move it to a year-free address with a 301 at the time of that refresh. Put "2027" in the title only if every entry was re-checked for 2027. | Lists and guides: [[BP-24 best ai construction estimating software 2026\|BP-24]], [[BP-33 hvac estimating software 2026 buyers guide\|BP-33]], [[BP-46 best electrical estimating software 2026\|BP-46]], [[BP-48 best flooring estimating software in 2026\|BP-48]], [[BP-52 best plumbing estimating software 2026\|BP-52]], [[BP-54 best concrete estimating software 2026\|BP-54]], [[BP-55 best drywall estimating software in 2026\|BP-55]], [[BP-76 best glazing estimating software 2026\|BP-76]]. Alternatives and comparisons: [[BP-81 best planswift alternatives 2026\|BP-81]], [[BP-15 quotr vs togal ai comparison 2026\|BP-15]], [[BP-20 quotr ai vs planswift ai takeoff procurement comparison 2026\|BP-20]]. Other: [[BP-58 house flipping math 2026\|BP-58]] |
| **Market piece tied to 2026** | Keep it as a dated 2026 record. If Quotr publishes a 2027 edition, give the new edition a year-free address and 301 the 2026 address to it ([[Optimize vs create]]). | [[BP-03 construction cost trends 2026\|BP-03]], [[BP-16 construction labor shortage ai adoption 2026\|BP-16]], [[BP-23 tariff impact construction costs 2026 steel aluminum copper\|BP-23]], [[BP-27 state of ai in preconstruction 2026 adoption roi enr top 400 gcs\|BP-27]] |
| **Not re-checked by January** | Leave the address, title and dates alone. Put the post in the first 2027 batch. | Any of the above |

- One vendor benchmark says about 3 in 4 B2B software pages cited by ChatGPT had a year in the title (QUALITY-17: no published method, low confidence). So a year in the title is fine when it is earned.
- Do not move addresses while a Google update is rolling out (rule 8).

### 7. Do not publish near-duplicate pages

- **One buyer question, one main page.** Before writing a new post, check the [[Prompt library]] and the article notes for a page to extend instead (W-11).
- Google's spam policies count "using generative AI tools to generate many pages without adding value" as scaled content abuse (mass-produced pages with little value) (QUALITY-01).
- They also count "creating many pages with search keywords that make little sense to readers" (QUALITY-02). Both quotes come from the vault's notes and were not re-read live.
- Google's May 2026 AI guide adds: making separate content for every variation of a question, mainly to manipulate AI answers, can break that policy. Genuine subtopics are fine (QUALITY-05, INDEX-06, AI-07).
- The overlap map found 20 groups with 59 posts and proposes 16 merges.
- The overlapping estimating-services posts are the closest fit to the keyword-variant pattern: 11 went live in about seven weeks (briefing; inference).
- Stop adding more "[trade] estimating services" pages, city-by-city versions and self-ranked "best X" lists ([[30-60-90 plan]], stop-doing list).
- Cover sub-questions inside one strong page instead (AI-07).

### 8. Time big changes around Google updates

- While a Google core update (a broad change to how Google ranks pages) or spam update is rolling out, hold merges, redirects, retitles, re-dating and batch publishing.
- This keeps cause and effect readable. It is measurement hygiene, not a Google rule (inference in the briefing).
- Single-page fact fixes can go ahead, with a Search Console annotation.
- **Now:** the September 2026 spam update began on 2026-09-24 and may run to about 2026-10-08 (RANK-21).
- The last broad core update (May 2026) ended on 2026-06-02. No new one had been announced by 2026-09-26. One may come before the end of 2026, but that is an inference from past gaps (RANK-22).
- Timeline and details: [[Google search updates 2025-2026]].

---

## Order of work

| # | What | Why first | Task | When |
|---|---|---|---|---|
| 1 | **Old prices and wrong facts.** About 13 posts show retired prices, possibly 16 (only 2 were read on the live page). Others carry wrong competitor facts, conflicting Quotr facts or brief text. | In the September tests, Perplexity repeated the old entry price in 2 of 8 brand answers (W-01). These fixes are cheap. They can go ahead during the spam update. | A2, A3 (after the fact sheet sign-off, A1), A6 | October 2026 |
| 2 | **Posts AI already cites.** The dataset flags 12. A later check found 8 were really used in an answer: [[BP-12 is ai takeoff actually accurate yet\|BP-12]], [[BP-32 best togal ai alternatives\|BP-32]], [[BP-56 how to estimate plumbing from drawings\|BP-56]], [[BP-59 how developers source building materials\|BP-59]], [[BP-81 best planswift alternatives 2026\|BP-81]], [[BP-82 outsource construction estimating\|BP-82]], [[BP-85 commercial estimating services\|BP-85]], [[BP-87 quantity takeoff services\|BP-87]]. [[BP-51 stack alternative\|BP-51]] and [[BP-62 ddp construction materials\|BP-62]] were only retrieved. The flags on [[BP-17 how to do construction takeoff pdf blueprint\|BP-17]] and [[BP-57 bluebeam alternative\|BP-57]] are wrong (overlap map). | These pages are already sources. Putting "Quotr.ai" inside their key facts is a cheap test that may get Quotr named. It is not a guaranteed fix (W-04). | A8 | October 2026 |
| 3 | **Merges.** 16 proposed in the overlap map. Order: G01, G02, G03, G04 first; then G10, G12, G14, G05 to G08 and G09; G13 and G11 last. | Fewer, stronger pages. Less risk of scaled content abuse. | A12 | After the spam update completes (about 2026-10-08), once both pages are read and Search Console data is pulled |
| 4 | **The rest.** Lists, comparisons and service pages first, then worst health first. | Lists, comparisons and service pages should be improved before the next core update, if possible (briefing). | Monthly loop | November 2026 onward |

The Refresh queue shows the next 15 posts with status `todo` or `doing`. It is sorted by the Order column that the [[Blog health audit]] set: high-priority posts first, and within them posts cited by AI, posts linked to a tracked buyer question and posts with the old price, then the lowest health score.

![[Articles.base#Refresh queue]]

Dated plan for October to December 2026: [[Refresh plan Q4 2026]].

---

## After each refresh

### 1. Update the article note

| Property | What to set |
|---|---|
| `status` | `doing` when work starts. `done` when the change is live and re-checked. `ok` if the post needs nothing more. `dropped` if you decide not to do the planned work (say why in the Log). |
| `health` and `health_score` | Re-score the six areas after the change. Update the band and the score. |
| `flags` | Remove flags that no longer apply (for example `old price`). Add new ones from Search Console, such as `not indexed (GSC)`, `shares queries (GSC)` or `dropped after update (GSC)` ([[Search Console audit playbook]]). |
| `old_pricing` | Set to `no` once the live page shows no retired price. |
| `updated_shown` | The "Last updated" date the page now shows. |
| `action` and `merge_into` | Change only if the decision changed. For a merge, keep `action: merge` and the link to the keeper. |
| `ai_cited` and `cited_in` | Leave as they are. They record the September 2026 tests. New AI results go in new test-run notes. |

Then add one line under `## Log`, in this form:

```
- YYYY-MM-DD: what changed, who checked it.
```

Examples (made up):

```
- 2026-10-07: removed the retired Solo/Team prices; added the dated Lite/Plus/Enterprise line; re-crawl requested; annotation added. Score 47 to 63. Checked by [editor name].
- 2026-10-20: merged into BP-32; 301 live; internal links and sitemap updated. Checked by [editor name].
```

- The Log is append-only. Add a new line. Never edit an old one.
- For a merge, add a Log line to both notes: the old post and the keeper.
- Never delete an article note, even for a merged or retired post. Change its status instead, as vault rule 5 does for other records.
- Add one line for the batch at the top of [[Changelog]] (vault rule 7).

### 2. Re-check in search

| When | What to check | How |
|---|---|---|
| **Same day** | Ask Google to read the page again (URL Inspection, then Request indexing). Submit it to Bing, or use IndexNow (a way to tell Bing a page has changed). Add a Search Console annotation. | [[Tracking setup#3.5 After fixing pages: ask Google to re-read them]]. Annotations hold up to 120 characters and are deleted after 500 days, so the Log line is the permanent record (GSC-06). |
| **About 10 days later** (our suggestion) | URL Inspection shows a crawl after the edit date. Google picked the post itself as the main version (the canonical). For a merge, the old address forwards to the keeper. | [[Search Console audit playbook]] |
| **28 days later** | Compare clicks, impressions and AI impressions with the 28 days before. Do not measure across a Google update rollout. | [[Search Console audit playbook]] |
| **Merges: 4-8 weeks** | Watch the keeper's clicks and impressions. | [[Optimize vs create]] |

### 3. Re-test in AI engines

- If the post serves buyer questions in the [[Tracking set]] (its `target_prompts`), re-run them 2-4 weeks after the change. Then check them in each monthly run ([[Page refresh checklist]], Step 8).
- Record each run as a new test-run note. Never edit an old one (vault rule 5).
- Run key prompts twice. Count a change only if it holds in two monthly runs in a row ([[KPIs and dashboard]]).
- Why so careful: 40-60% of cited domains change from month to month for the same questions (Profound, a vendor; quoted in [[Page refresh checklist]]).
- Planned re-tests: about four weeks after the price fix, re-run B2, B4, V2 and T22 (W-01). After the brand-in-fact rewrites, re-run C12, P5, N2 and V3, twice each (W-04).
- Posts with no tracked buyer question need no AI re-test. Use their Search Console AI impressions instead.

---

## Measuring results

Watch a few numbers each month. The how-to is in [[Search Console audit playbook]]. Targets are in [[KPIs and dashboard]] (suggested, not yet agreed with Quotr).

| Number | What it tells you | Where it comes from | KPI |
|---|---|---|---|
| **Posts indexed**, out of the live posts | Can Google show and cite them at all? A post must be indexed to be a source link in AI Overviews or AI Mode (INDEX-05). | Search Console, Page indexing | Suggested as a monthly KPI in W-10 |
| **Posts with a retired price or wrong fact** | Fact health. Suggested target: 0 stale-price pages within 90 days. | Site search; the "Old price still showing" view in Articles.base | L9 |
| **Clicks per refreshed post**, 28 days before vs after | Did the refresh help in Google search? | Search Console, Performance | — |
| **AI impressions per post** | Does Google's AI show the post? Impressions only, no clicks. Data starts on 2026-05-18 (GSC-14). | Search Console, Generative AI report | L2 (d) |
| **Named and cited in AI answers** for the post's buyer questions | Does AI use the post, and does it name Quotr? | Monthly [[Tracking set]] run | L2, L3, L4 |
| **Health bands**: posts in each band, and the average score per cluster | Is the blog getting healthier overall? | The "By cluster" view in Articles.base shows the average score | — |
| **Posts refreshed that passed the quality bar** | Real output, not post count (W-12). | Article note Log lines | — |

**Reading the numbers without fooling yourself**
- Only compare Search Console periods that start on or after 2026-04-28. Impressions were over-counted before then (GSC-12).
- Do not add AI impressions to the normal Web totals. They are already inside them (briefing; GSC-02).
- If AI impressions look low for 2026-08-13 to 2026-08-17, treat that as a Google logging error. Reports say the data was restored around 2026-08-21 (GSC-19).
- Annotate every refresh, merge and Google update on the Search Console chart (GSC-06).
- Look at 3-month trends, not single months ([[KPIs and dashboard]]).
- AI answers take clicks, so judge the blog on AI impressions, citations, naming, branded search and demos, not visits alone. Agree this with Quotr at the start (briefing).

---

## Related pages

- [[Page refresh checklist]]: the step-by-step edit of one page
- [[Blog health audit]]: how the 96 posts were scored, and the full overlap map
- [[Refresh plan Q4 2026]]: the dated plan for October to December 2026
- [[What went wrong]]: the 19 findings behind these rules
- [[Google search updates 2025-2026]]: Google's updates and what they mean for Quotr
- [[Search Console audit playbook]]: the Search Console checks, step by step
- [[Optimize vs create]]: when to fix and when to create new
- [[GEO writing style guide]]: how to write each section
- [[Entity fact sheet]]: the facts to check against
- [[KPIs and dashboard]]: targets and the monthly dashboard
- [[Tracking set]]: the buyer questions to re-test
