---
type: baseline
description: 'Health check of all 96 Quotr blog posts on 2026-09-26: scores, what to fix first, posts that compete with each other, what works and how we measured.'
last_verified: 2026-09-26
verify_every_days: 30
aliases:
- Blog health
---
# Blog health audit

> [!abstract] What this page is for
> This is the hub for the health check of all 96 Quotr blog posts. It shows how healthy the blog is, which posts to fix first, which posts compete with each other and what already works. Every post has its own article note with its score and next step; this page brings them together.

> [!info]- Sources
> Vault notes: [[What went wrong]], [[Content refresh playbook]], [[Publishing patterns and correlations]], [[AI visibility baseline]], [[Website audit]], [[Optimize vs create]], [[Entity fact sheet]], [[Tracking set]], [[Google search updates 2025-2026]], [[Search Console audit playbook]], [[Refresh plan Q4 2026]], the 96 article notes (BP-01 to BP-96), the task notes (A2, A8, A12 and others) and the open questions [[Q-49 Search Console and Bing set-up|Q-49]], [[Q-52 Real publish dates of six posts|Q-52]] and [[Q-59 Web search checks for 60 unchecked posts|Q-59]].
>
> Data files (read-only, 2026-09-26): the health review of all 96 posts (a score, findings, an action and steps for each post, each checked by a second reviewer); the overlap map (20 groups of posts that answer the same buyer question, checked by a skeptic reviewer); the computed blog statistics (volume, timing, themes, years in URLs, old prices, AI citations, web search checks, prompt coverage); the post-by-post data; and the 19 "what went wrong" findings, in their softened wording.
>
> Test codes such as C12, V1 or B4 name single prompts from the 2026-09-25 Perplexity tests ([[AI visibility baseline]]). T01-T53 are tracked prompts ([[Tracking set]]). Claim IDs such as RANK-21 come from the Google claims register ([[Google search updates 2025-2026]]).

---

## The short version

- **The blog is fixable, not broken.** The 96 posts average 54 out of 100. 1 post is good, 42 are fair, 53 are poor and none is critical.
- **The most common problem is overlap.** 59 posts sit in 20 groups where Quotr posts answer the same buyer question. 17 posts in all should be merged into a stronger sister page (16 inside the groups, plus one customer story).
- **The most urgent problem is old prices.** On 2026-09-25, 13 posts were recorded with the retired prices, and 3 more may carry them. Fix them now with task [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]].
- **Next, protect the posts AI already uses.** 8 posts were cited (used as sources) in the September AI tests, but AI rarely said "Quotr". Put the Quotr name inside their key facts.
- **Hold merges and address changes until Google's spam update ends,** around 2026-10-08 (RANK-21, found by web search on 2026-09-26, not re-checked). Fact fixes can go live now.
- **What works:** alternatives posts, service posts with clear prices and one step-by-step how-to get used by AI. The answer-first format is right.
- **How sure we are: medium.** We had no Search Console data (Google's free report on how a site does in search). The web search tool is not Google, and it ran out after 36 posts. Few pages were read in full. Treat the scores as a first pass.

---

## Scorecard

| Measure | Number | Source and how sure we are |
|---|---|---|
| Posts checked | **96** (every post in the blog sitemap, the site's list of pages for search engines) | Blog sitemap, 2026-09-25 audit. High. |
| Average health score | **54 out of 100** (poor band). Median 53. Lowest 37, highest 77. | Health review, 2026-09-26. Medium: few pages read in full. |
| Health bands | **1 good, 42 fair, 53 poor, 0 critical** | Bands from [[Content refresh playbook#How we score a post's health]]. The one good post is [[BP-82 outsource construction estimating\|BP-82]] (77). |
| Average by area (0-5) | Freshness 3.2 · Accuracy 2.7 · Structure 2.9 · Visibility 2.5 · Uniqueness 2.4 · Trust 2.4 | Health review. Trust and Uniqueness are the weakest areas. |
| Action | **52 update, 21 rewrite, 17 merge, 6 keep, 0 retire** | Health review and overlap map. Medium. |
| Priority | **36 high, 44 medium, 16 low** | Health review. |
| Effort | **37 small, 52 medium, 7 large** | Health review. Our estimates. |
| Old price still showing | **13 confirmed, 3 possible** | Confirmed = on the vault list from the 2026-09-25 fact-check. Only 2 were read on the live page. 4 more list posts were never checked ([[What went wrong#W-01 Old prices still showing after the September price change\|W-01]]). |
| Cited in the September AI tests | **8 posts cited** | Perplexity (an AI answer engine) tests of 2026-09-25, one engine. "Cited" here means used as a source for a buyer question that does not name Quotr. 2 more were only retrieved (looked at, not used). 2 appear in the test notes but were not cited. Data corrected on 2026-09-26 after a re-check of the test notes. |
| Found in web search | **36 checked: 21 found, 15 not found. 60 not checked.** | Targeted searches on 2026-09-25 and 2026-09-26. The tool is not Google, the sample was not random, and the search allowance ran out. Low to medium. |
| Posts that compete | **20 overlap groups (59 posts); 17 merges** | Overlap map, checked by a skeptic reviewer. 16 merges sit inside the groups. The 17th folds the RL Electric story ([[BP-72 how rl electric cut estimating time with ai powered takeoffs\|BP-72]]) into its case study page, once that page is rebuilt with numbers. |
| Year in the web address | **27 posts** have "2026" in the URL (web address) | Post data. About 15 are evergreen topics, about 5 are year-bound market pieces and 7 are events or editions ([[What went wrong#W-16 Date signals disagree, and years in evergreen URLs\|W-16]]). |
| Reset dates | **6 posts** share bulk dates (2026-07-15 or 2026-07-24); 2 more may | Blog sitemap. Their real publish dates are unknown ([[Q-52 Real publish dates of six posts\|Q-52]]). |
| Publishing pace | **Peak: 22 posts in May and 25 in June.** Then 17 in July, 11 in August and 7 in September so far (the month was not over when the sitemap was read). | Sitemap dates stand in for publish dates (90 posts with real dates). Busiest week: 7 posts. About 5.4 a week from mid-May to mid-July, 2.3 a week from August to late September. |
| Buyer questions covered | **106 of 282** library prompts have a matching Quotr post | Prompt library and post data. |

---

## What to fix first

The Refresh queue below shows the next 15 posts to work on. The order comes from this audit:
- High-priority posts come first, then medium, then low. Posts marked "keep" come last.
- Within each priority, a post moves up if AI cited it (this counts double), if it serves a tracked buyer question and if it shows the old price.
- Ties go to the lowest health score first.
- The "Order" number sits in each article note as `rank`.

![[Articles.base#Refresh queue]]

### The top 10

| Order | Post | What to do | Why |
|---|---|---|---|
| 1 | [[BP-81 best planswift alternatives 2026\|BP-81]] | Update. Fix the PlanSwift price, drop the self-ranking and put "Quotr.ai" inside the fact sentences. | Perplexity reads it for PlanSwift facts (V3) but never names Quotr. |
| 2 | [[BP-32 best togal ai alternatives\|BP-32]] | Rewrite as the one fair "Togal alternatives by use case" page. Keep its address. Take in [[BP-43 best togal ai alternatives 2026\|BP-43]] later. | It is behind V1, the only unbranded answer that named Quotr (low in the list). Tracked prompt T16. |
| 3 | [[BP-59 how developers source building materials\|BP-59]] | Update. Fix the factory count first. Add the words buyers use. | Cited in S6 (T43). AI already repeats Quotr's conflicting factory counts. |
| 4 | [[BP-12 is ai takeoff actually accurate yet\|BP-12]] | Update with small, careful edits. Add the Quotr name and a method for the figures. | Perplexity's first source for "how accurate is AI takeoff" (T30), without naming Quotr. |
| 5 | [[BP-87 quantity takeoff services\|BP-87]] | Update. Add Quotr's own confirmed takeoff price, with the brand in the same sentence. | Cited in S9 (T44) for market price ranges. |
| 6 | [[BP-56 how to estimate plumbing from drawings\|BP-56]] | Update. Change as little of the step text as possible. Add Quotr-only proof and per-fixture pricing. | Perplexity's first source for "how to estimate plumbing from drawings" (T49), without naming Quotr. |
| 7 | [[BP-82 outsource construction estimating\|BP-82]] | Update. Edit sentences, not structure. Put "Quotr.ai" in the price sentence. Merge [[BP-79 construction estimating services\|BP-79]] into it. | The first source in the answer for tracked prompt T12 (C12). Its prices appear without the Quotr name. The only post rated good (77). |
| 8 | [[BP-43 best togal ai alternatives 2026\|BP-43]] | Merge into [[BP-32 best togal ai alternatives\|BP-32]]. Fix the old price now, then redirect it. | A near-duplicate Togal list that ranks Quotr first. The old price is confirmed. It splits tracked prompt T16 with BP-32. Score 37. |
| 9 | [[BP-51 stack alternative\|BP-51]] | Rewrite. Fix the retired price and two wrong competitor facts now. Then aim it at small residential subcontractors. | The old price is confirmed on the page and in its FAQ. AI reads Quotr's comparison posts for facts about rivals, so errors spread. Perplexity looked at it for V10 but did not use it. Score 37. |
| 10 | [[BP-80 best ai bid software for construction\|BP-80]] | Merge into [[BP-47 ai bidding software construction\|BP-47]]. Fix the old price in both posts now, then redirect it. | A near-duplicate of BP-47. The old Solo/Team price is in its indexed text. Score 37. |

- **A note on the order.** The order was recomputed on 2026-09-26, after a re-check of the AI test notes corrected which posts were cited.
- **Timing.** Fact fixes (prices, wrong facts, leftover brief text) can go live now. Merges, redirects, new addresses and date changes wait until the spam update ends, around 2026-10-08 ([[Content refresh playbook]]).
- **Plan.** The week-by-week schedule is in [[Refresh plan Q4 2026]]. The full list, grouped by action, is below.

> [!example]- Full refresh plan (all posts with work to do)
> ![[Articles.base#Full refresh plan]]

---

## Health by cluster

A cluster is a group of posts on the same kind of topic. "Weakest area" is the lowest of the six scored areas, on average.

| Cluster | Posts | Average score | Weakest area | Most common problem | Usual action |
|---|---|---|---|---|---|
| Best-of lists and buyer guides | 17 | 49 | Accuracy (1.8) | Old price: 10 of 17 | Update (7) or rewrite (6); 4 merges |
| Trade how-tos and fundamentals | 16 | 58 | Visibility (2.0) | Not found in web search: 8 of the 10 checked | Update (9) |
| Estimating services | 12 | 60 | Uniqueness (2.3) | Shares a buyer question with a sister page: 10 of 12 | Update (9) |
| AI explainers | 11 | 51 | Visibility and Uniqueness (2.2) | Shares a buyer question: all 11 | Update (7) |
| Procurement and sourcing | 10 | 56 | Trust (2.0) | Shares a buyer question: 7 of 10 | Update (4) or rewrite (4) |
| Company news, customer stories and event recaps | 8 | 58 | Structure (2.1) | Year in the URL: 5 of 8; event recaps with little buyer value | Update (4) or keep (3) |
| Head-to-head comparisons | 8 | 50 | Trust (2.0) | Shares a buyer question: 7 of 8; not found in web search: 4 of 8 checked | Update (7) |
| Cost and market data | 6 | 51 | Freshness (2.0) | Year in the URL: 4 of 6; no Quotr data: 3 | Rewrite (3) |
| Alternatives to X | 5 | 43 | Accuracy (1.4) | Old price: 3 confirmed, 2 possible; Quotr ranked itself first: 3 | Rewrite (3) |
| Developer, architect and investor personas | 3 | 58 | Structure (2.3) | No problem shared by most of the group | Update (2) |

What stands out:
- **Lists and alternatives posts are the least healthy,** mostly because of old prices and self-ranking.
- **Their errors travel.** AI reads these pages for facts about Quotr's rivals, so a wrong price or claim gets repeated.
- **Service posts score best,** but 10 of 12 share a buyer question with a sister page.
- **Trade how-tos are accurate but hard to find.** 8 of the 10 we checked did not come back in web search. That is a lead to check in Search Console, not proof.

![[Articles.base#By cluster]]

---

## Posts that compete with each other

Some Quotr posts answer the same buyer question, so they compete for the same place in search and AI answers. The overlap map puts them in 20 groups (59 posts). In each group one post is the **keeper**. **Merge** means: move the best parts into the keeper, then forward the old address to it with a 301 redirect (a permanent forward). **Keep separate** means the post answers a different question or reader, so it stays, with a clearer role.

| Group | Buyer question | Keep | Merge | Keep separate | Confidence |
|---|---|---|---|---|---|
| G01 | What are the best alternatives to Togal.AI for construction takeoff? | [[BP-32 best togal ai alternatives\|BP-32]] | [[BP-43 best togal ai alternatives 2026\|BP-43]] | [[BP-15 quotr vs togal ai comparison 2026\|BP-15]] | High |
| G02 | What does an outsourced estimating service cost per square foot, and what do I get? | [[BP-82 outsource construction estimating\|BP-82]] | [[BP-79 construction estimating services\|BP-79]] | [[BP-85 commercial estimating services\|BP-85]], [[BP-87 quantity takeoff services\|BP-87]], [[BP-84 construction estimating services california\|BP-84]]; [[BP-90 outsourcing vs hiring an estimator\|BP-90]] (not decided yet) | High |
| G03 | Who can do outsourced preconstruction and bid estimating for a general contractor? | [[BP-86 preconstruction services\|BP-86]] | [[BP-89 precon on demand outsource bid cost estimation\|BP-89]] | — | Medium |
| G04 | What is the best AI bidding software for construction? | [[BP-47 ai bidding software construction\|BP-47]] | [[BP-80 best ai bid software for construction\|BP-80]] | [[BP-08 ai construction proposals takeoff to proposal\|BP-08]] | Medium |
| G05 | What is construction procurement, and what are the steps? | [[BP-69 construction procurement process\|BP-69]] | [[BP-60 what is construction procurement 2026 guide\|BP-60]] | — | Medium |
| G06 | Is there estimating software that goes from takeoff to material buyout and purchase orders? | [[BP-38 takeoff to buyout construction estimating procurement platform\|BP-38]] | [[BP-02 the takeoff to transaction gap\|BP-02]] | [[BP-50 construction procurement software\|BP-50]] | Medium |
| G07 | Why did construction costs rise so much in 2026, and what are they doing now? | [[BP-03 construction cost trends 2026\|BP-03]] | [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps\|BP-70]] | [[BP-35 construction cost index q1 2026 ppi rsmeans mortenson\|BP-35]], [[BP-23 tariff impact construction costs 2026 steel aluminum copper\|BP-23]] | Medium |
| G08 | What is the best software for a real estate development pro forma? | [[BP-22 real estate pro forma software comparison\|BP-22]] | [[BP-49 construction proforma software\|BP-49]] | [[BP-29 the proforma that never stops changing\|BP-29]] | Medium |
| G09 | What is AI construction estimating software, and how does AI takeoff work? | [[BP-45 what is ai construction estimating software\|BP-45]] | [[BP-11 how ai construction estimating works\|BP-11]]; [[BP-71 how ai construction takeoff works in 2026\|BP-71]] (only after a Search Console check shows the keeper can take its searches) | [[BP-12 is ai takeoff actually accurate yet\|BP-12]] | Medium |
| G10 | What is the best AI estimating and takeoff software, and how do I choose? | [[BP-24 best ai construction estimating software 2026\|BP-24]] | [[BP-19 ai construction estimating software buyers guide\|BP-19]] | [[BP-64 trade estimating software\|BP-64]] | Medium |
| G11 | What is the best estimating and takeoff software for electrical contractors? | [[BP-46 best electrical estimating software 2026\|BP-46]] | [[BP-37 electrical estimating software buyers guide\|BP-37]] | — | Low |
| G12 | How do I do a takeoff from PDF plans and turn it into a priced estimate? | [[BP-17 how to do construction takeoff pdf blueprint\|BP-17]] | [[BP-13 blueprint to priced estimate workflow\|BP-13]], [[BP-05 construction takeoff guide\|BP-05]] | [[BP-66 ai construction estimating software that turns plans into prices in minutes\|BP-66]] | Medium |
| G13 | How do I bid commercial work to GCs as a subcontractor without giving away my margin? | [[BP-28 how to bid commercial construction projects subcontractor estimating takeoff guide\|BP-28]] | [[BP-53 how subcontractors bid gcs without giving away margin\|BP-53]] | [[BP-04 how to price construction job\|BP-04]] | Medium |
| G14 | Should I keep estimating in Excel or switch to estimating software? | [[BP-26 quotr vs excel\|BP-26]] | [[BP-06 quotr vs traditional estimating\|BP-06]] | — | Medium |
| G15 | What should I use instead of PlanSwift, and is Quotr a good replacement? | [[BP-81 best planswift alternatives 2026\|BP-81]] | — | [[BP-20 quotr ai vs planswift ai takeoff procurement comparison 2026\|BP-20]] | Medium |
| G16 | How do I source or import building materials from China for a US project? | [[BP-88 sourcing building materials china cbd fair 2026\|BP-88]] | — | [[BP-59 how developers source building materials\|BP-59]], [[BP-62 ddp construction materials\|BP-62]] | Low |
| G17 | Can AI or ChatGPT read construction drawings and do a takeoff? | [[BP-18 ai that reads construction drawings chat with blueprints\|BP-18]] | — | [[BP-67 chatgpt for construction estimating\|BP-67]], [[BP-65 ai agent for construction\|BP-65]] | Low |
| G18 | Who can do outsourced MEP, HVAC or electrical estimating, and what does it cost? | [[BP-95 mep estimating services\|BP-95]] | — | [[BP-94 hvac estimating services\|BP-94]], [[BP-91 electrical estimating services\|BP-91]] | Low |
| G19 | Will AI replace construction estimators, and how are contractors using AI in 2026? | [[BP-27 state of ai in preconstruction 2026 adoption roi enr top 400 gcs\|BP-27]] | — | [[BP-16 construction labor shortage ai adoption 2026\|BP-16]] | Low |
| G20 | What should I use instead of STACK, and how does Quotr compare with STACK? | [[BP-51 stack alternative\|BP-51]] | — | [[BP-34 quotr ai vs stack browser first takeoff procurement\|BP-34]] | Low |

How to use this map:
- **Merges wait.** Do them after the spam update ends (around 2026-10-08). Read both pages and pull Search Console data for each address first (task [[A12 Merge duplicate pages|A12]]).
- **Fix prices before merging.** Run [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]] first, even on posts that will be merged.
- **Order of merges.** G01 to G04 first. Then G10, G12, G14, G05 to G08 and G09. G13 and G11 last.
- **Groups G15 to G20 have no merge.** Their job is to give each buyer question one main page and a clear role for the others.
- **One main page per buyer question.** Before writing a new post, check this map and the prompt library for an existing page to extend.
- **After each merge,** update internal links, the sitemap, llms.txt (a plain summary file of the site for AI tools) and the prompt notes that point to the old address. Then watch the keeper for 4-8 weeks.
- **37 posts sit outside the groups.** The reviewer found no shared buyer question and no search overlap for them.
- **Confidence** is how sure the overlap map is about the group and its keeper. Check low-confidence groups most carefully.

![[Articles.base#Merge or retire]]

---

## What is working

Credit where it is due. Several posts already do the job a GEO blog should do (GEO: getting named in AI answers).

**Posts AI already uses**
- **8 posts were cited** (used as a source) in the 2026-09-25 Perplexity tests: [[BP-12 is ai takeoff actually accurate yet|BP-12]], [[BP-32 best togal ai alternatives|BP-32]], [[BP-56 how to estimate plumbing from drawings|BP-56]], [[BP-59 how developers source building materials|BP-59]], [[BP-81 best planswift alternatives 2026|BP-81]], [[BP-82 outsource construction estimating|BP-82]], [[BP-85 commercial estimating services|BP-85]] and [[BP-87 quantity takeoff services|BP-87]].
- 2 more were only retrieved (looked at, not used): [[BP-51 stack alternative|BP-51]] and [[BP-62 ddp construction materials|BP-62]]. 2 appear in the test notes but were not cited: [[BP-17 how to do construction takeoff pdf blueprint|BP-17]] and [[BP-57 bluebeam alternative|BP-57]].
- **Why they work (our reading):** each answers one clear buyer question. Each gives something AI can lift: a price per square foot, a step list, an accuracy figure or a list of rivals' facts.
- **All 8 cited posts match a buyer prompt in the library.** None of the 14 posts with no matching prompt was cited.
- **Age did not decide it.** The 8 cited posts had been live a median of 64.5 days at the test date, the others 98.5 days. That gap could be chance (p = 0.16). If anything, newer posts were cited slightly more often.
- **No post with a confirmed old price was cited** for a question that does not name Quotr (0 of 13). The numbers are small, so this could be chance.
- **Questions that name Quotr are different.** There, Perplexity used many more Quotr posts, including ones with the retired price, and repeated that price in 2 of 8 brand answers ([[What went wrong#W-01 Old prices still showing after the September price change|W-01]]).
- **The catch:** AI used Quotr's facts but rarely said "Quotr". Only V1 named Quotr in an unbranded answer, low in the list. S6 named Quotr, but its prompt echoes Quotr's own wording. The fix is to put "Quotr.ai" inside each key fact ([[A8 Put the Quotr name inside key facts on the pages AI already reads|A8]]; [[What went wrong#W-04 AI uses Quotr's figures but drops the Quotr name|W-04]]).
- **One engine, small samples.** Only Perplexity was tested, with one or two runs per prompt.

The table below lists the 8 cited posts.

![[Articles.base#Cited by AI]]

**The 6 posts marked "keep"** (no work now beyond the site-wide sweeps)

| Post | Score | Why keep |
|---|---|---|
| [[BP-30 commercial electrical takeoff drawings to proposal\|BP-30]] | 67 | Commercial electrical workflow post. No known problem. Test its High-priority prompt L-096. |
| [[BP-40 commercial signage takeoff sign schedule bid package\|BP-40]] | 67 | Niche signage how-to. Spend on it only if Quotr says signage is a target trade. |
| [[BP-58 house flipping math 2026\|BP-58]] | 57 | Low-priority explainer for house flippers. Decide in January 2027 what to do about "2026" in its address. |
| [[BP-14 nhca build the builder 2026 recap\|BP-14]] | 57 | Short event recap. No known problems. |
| [[BP-09 re forge sf 2026 recap\|BP-09]] | 57 | Short event recap for developers. Use the organiser's spelling of the event name. |
| [[BP-07 dallas build expo 2026 recap\|BP-07]] | 57 | Timely event recap. Check the show dates and booth. |

**Other strengths** (from [[What went wrong#What Quotr got right]])
- The writing format is right: answer-first blocks, question headings, tables, FAQs and "Honest Limitations" sections.
- 106 of the 282 buyer prompts in the library now have a matching Quotr post.
- The only post rated good, [[BP-82 outsource construction estimating|BP-82]], was Perplexity's first source for tracked prompt T12 on two runs.

---

## Old prices still showing

Quotr changed its prices on 2026-09-14: Quotr.ai Lite $79.90 per seat per month, Plus $299.90, Enterprise custom ([[Entity fact sheet]]). On 2026-09-25, the audit recorded 13 posts that still showed the retired "Solo $299.90 / Team $499.90" plans or "from $299.90". The table below lists those 13.

![[Articles.base#Old price still showing]]

- **3 more may carry it:** [[BP-20 quotr ai vs planswift ai takeoff procurement comparison 2026|BP-20]], [[BP-32 best togal ai alternatives|BP-32]] and [[BP-81 best planswift alternatives 2026|BP-81]]. These were seen only in search summaries. Read them before counting them.
- **4 list posts were never checked:** [[BP-52 best plumbing estimating software 2026|BP-52]], [[BP-55 best drywall estimating software in 2026|BP-55]], [[BP-37 electrical estimating software buyers guide|BP-37]] and [[BP-64 trade estimating software|BP-64]].
- **Why it matters:** in 2 of 8 brand prompts, Perplexity repeated the old price. It said Quotr starts at about $299.90, about 3.75 times the real $79.90 entry price.
- **How sure:** only 2 of the 13 were read on the live page. Search copies can lag, so some pages may already be fixed.

**The fix: task [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]]** (October 2026, week 2)
1. Search all 96 posts for "Solo", "Team (2", "$499.90", "from $299.90", "starts at $299.90", "1 User Plan", "2–10 Users", "$249/seat" and "$41/seat".
2. Replace each hit with one dated line: "Quotr.ai Lite $79.90 per seat per month; Plus $299.90; Enterprise custom (as of [date]; see /pricing/)".
3. Ask Google and Bing to re-read each changed post (re-crawl).
4. Fix llms.txt ([[A4 Fix llms.txt|A4]]) and ask the two outside sites that copied the old price to correct it ([[B12 Follow up correction outreach|B12]]).
5. This is a fact fix, so it does not need to wait for the spam update.
6. Re-run the price prompts about four weeks later.

---

## Patterns and mistakes behind this

The detail is in [[Publishing patterns and correlations]] and [[What went wrong]]. In short:

- **Output grew faster than the editing check.** 47 of the 90 posts with real dates went out in May and June, up to 7 a week. Brief notes or lines written for bots reached at least 2 live posts ([[What went wrong#W-12 Output grew faster than the editing check|W-12]]).
- **Topics came in waves.** Best-of lists led June (10 of 25 posts), procurement led July, and Service posts led August and September. The Service wave produced several near-identical pages ([[What went wrong#W-06 The Service pivot was built as a dozen similar pages|W-06]]).
- **Prices were typed into each post.** When the price changed, nothing updated them. All 16 confirmed or possible cases are list or comparison posts ([[What went wrong#W-01 Old prices still showing after the September price change|W-01]]).
- **One buyer question often got a second page.** The two Togal lists went out 14 days apart ([[What went wrong#W-11 About 12 posts duplicate another Quotr page|W-11]]).
- **Date signals disagree.** 27 addresses carry "2026", and 6 posts lost their real publish date in a bulk reset ([[What went wrong#W-16 Date signals disagree, and years in evergreen URLs|W-16]]).
- **Fair context:** this is a young team that published 96 posts in about six months. Problems per post were flat by month, so the busy months were not worse post by post. There were just more posts.

---

## How we measured

**Data sources**
- The 2026-09-25 website audit and Perplexity AI tests (one engine, one or two runs per prompt).
- Targeted web searches on 2026-09-25 and 2026-09-26. The session's search allowance ran out, so only 36 of 96 posts were checked. The search tool is not Google.
- This session could not open quotr.ai itself (network block). So no page was re-read on 2026-09-26. Only about 6 posts were read end to end in the audit. Much of the evidence comes from search-index text (the copy a search engine stored) and AI answers, which can lag behind the live page.
- No Search Console (Google's free report on how a site does in search), Bing or analytics data.
- The blog sitemap date stands in for the publish date. 6 posts have reset dates and were left out of the timing figures.

**How each post was scored**
- Six areas, each scored 0 to 5: Freshness, Accuracy, Trust, Structure, Visibility and Uniqueness.
- Health score = the sum of the six ÷ 30 × 100. Bands: good 75+, fair 55-74, poor 35-54, critical below 35.
- The full rubric is in [[Content refresh playbook#How we score a post's health]].
- Each finding says where it comes from, for example "from 2026-09-25 audit", "from 2026-09-25 AI tests", "seen in search 2026-09-26" or "inferred".

**How we checked the work**
- For every post, one reviewer wrote the score, findings, action and steps. A second reviewer then checked each one.
- The overlap map was built first, then checked by a skeptic reviewer. That review changed several groups. For example, it moved [[BP-90 outsourcing vs hiring an estimator|BP-90]] from "merge" to "not decided yet", and added groups G18 to G20.
- A later re-check of the AI test notes corrected which posts were cited (8). The data and the queue order were updated on 2026-09-26.

**What to redo when access allows**
- **Search Console and Bing** ([[Q-49 Search Console and Bing set-up|Q-49]]): pull indexing status and clicks for every post. Re-score Visibility. Confirm the "not found" posts. How-to: [[Search Console audit playbook]].
- **Web search checks** ([[Q-59 Web search checks for 60 unchecked posts|Q-59]]): check the 60 unchecked posts, and re-read the posts flagged for old prices.
- **Real publish dates** ([[Q-52 Real publish dates of six posts|Q-52]]): restore the 6 reset dates, then redo the timing figures.
- **Read each page before editing it.** Re-score it after reading the live page ([[Page refresh checklist]]).

---

## What happens next

- **[[Refresh plan Q4 2026]]:** the week-by-week plan for October to December 2026.
- **[[Content refresh playbook]]:** the monthly refresh loop, how to choose each action and the rules that protect rankings.
- **[[Search Console audit playbook]]:** how to confirm or correct this audit once Search Console access arrives.
- **[[Retainer scope and value case]]:** how this work fits the year-long engagement.
- Tasks to start with: [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]] (old prices), [[A8 Put the Quotr name inside key facts on the pages AI already reads|A8]] (the Quotr name in cited posts), [[A12 Merge duplicate pages|A12]] (merges) and [[A15 Measurement setup and multi-engine baseline|A15]] (measurement).

---

## Every post

All 96 posts, oldest first. Open any post for its score, findings and next steps.

![[Articles.base#All articles]]
