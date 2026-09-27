---
type: plan
description: 'Week-by-week plan to fix, merge and refresh the Quotr blog from October to December 2026, plus the January 2027 decision on "2026" in web addresses and titles.'
last_verified: 2026-09-26
verify_every_days: 14
---
# Refresh plan Q4 2026

> [!abstract] What this page is for
> The dated plan for the Quotr blog from 5 October to 31 December 2026. It says which posts to work on each week, in the order set by the blog health audit, and roughly how many hours each week takes. It also lists all 17 merges and sets up the January 2027 decision on "2026" in web addresses and titles.

> [!info]- Sources
> Vault notes: [[Content refresh playbook]] (the monthly loop, the rules and the order of work), [[Blog health audit]] (how the 96 posts were scored and the overlap map), [[Search Console audit playbook]], [[What went wrong]] (findings W-01 to W-19), [[Google search updates 2025-2026]], [[30-60-90 plan]] and the task notes, [[Retainer scope and value case]], [[KPIs and dashboard]], [[Page refresh checklist]], [[Optimize vs create]], [[Content roadmap]], [[Entity fact sheet]], [[Publishing patterns and correlations]], the 96 article notes (their `rank`, `status`, `action`, `priority`, `health` and "What to do" steps) and the open questions [[Q-49 Search Console and Bing set-up|Q-49]] to [[Q-60 Re-check Google claims against official sources|Q-60]].
>
> Data files (read-only, 2026-09-26): the final health review of all 96 posts (score, action, priority, effort, steps and advice on title and web address for each post, plus the overlap map of 20 groups and its merge order); the computed blog statistics (old prices, AI citations, web search checks); the 19 "what went wrong" findings, in their softened wording; the Google briefing and its claim register (claim IDs such as RANK-21).
>
> The hours on this page are our own rough conversion of the S, M and L effort labels. They are not measured.

---

## The short version

- **Old prices come off first.** In the week of 12 October, the retired prices come off the 16 posts on the list (13 confirmed, 3 possible), before any other post work (task A2).
- **25 posts are planned for full work in Q4:** 12 refreshes from the top of the queue and 13 merges. All but one go live by 18 December. The last refresh (BP-24) is drafted in December and goes live in the week of 4 January, with its address decision. One merge (BP-72) happens only if its case study is live by then. The other 4 merges wait until January 2027, when the page they merge into (the "keeper") gets its rewrite.
- **The pace is about 2 writer days a week** (our assumption): about 180 hours over the quarter, and no week above 20 hours.
- **Merges and address changes wait** until Google confirms its September spam update is over (expected around 8 October; RANK-21) and until Search Console data is pulled for both pages.
- **After Q4, 65 posts still need work:** about 490 writer hours at the same rough rates, or about 30 more weeks at this pace. The queue runs well into 2027.
- **By 18 December, decide post by post** what to do with "2026" in 27 web addresses and in titles. No bulk rename to 2027.
- **Progress shows itself.** Set each article note's status and add a Log line. The live tables update on their own.

> [!warning] How sure we are
> - **No Search Console data yet** (Search Console is Google's free report on how a site does in search). The queue rests on the 2026-09-25 AI tests (one engine, Perplexity), one limited web search pass and a few page reads. Expect the order to change once task A17 brings Google's own numbers.
> - **Web search:** 36 posts were checked (21 found, 15 not). 60 were not checked, because the search limit ran out on 2026-09-26. The search tool is not Google, so "not found" is a lead, not proof.
> - **Dates:** the blog sitemap date stands in for the publish date. Six posts have reset dates ([[Q-52 Real publish dates of six posts|Q-52]]).
> - **Old prices:** 13 posts were confirmed by the 2026-09-25 fact-check, and 3 more were seen only in search summaries. Only 2 were read on the live page.
> - **Health scores** rest on limited evidence. Re-score each post after reading the live page ([[Content refresh playbook]]).
> - **Hours** are our assumption. Replace them with real times from the Log after the first two weeks.
> - **Google claims** such as RANK-21 were found by web search on 2026-09-26 and not re-checked ([[Q-60 Re-check Google claims against official sources|Q-60]]).

---

## Before we start

### 1. The price fix comes first (task A2)

- On 2026-09-25, about 13 posts still showed the retired "Solo $299.90 / Team $499.90" prices, 11 days after the 14 September price change. 3 more may ([[What went wrong]], W-01).
- In 2 of 8 brand questions, Perplexity said Quotr starts at about $299.90 a month. That is about 3.75 times the real $79.90 Lite price (W-01).
- Every refreshed post must use the current prices from the [[Entity fact sheet]], in the line the article notes use: "Quotr.ai Lite $79.90 per seat per month; Quotr.ai Plus $299.90; Enterprise custom; 7-day free trial". Write "Quotr.ai Lite", not just "Lite", because Kreo also sells plans called Lite and Plus.
- The fix goes live in the week of 12 October ([[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]]). It waits one week so the multi-engine AI baseline can be recorded first ([[A15 Measurement setup and multi-engine baseline|A15]]).
- Other Quotr facts (turnaround, factory count, accuracy) wait for the signed fact sheet ([[A1 Agree and sign off one fact sheet|A1]], then [[A3 Fact-fix sweep, part 2 - every other conflicting fact|A3]]). Until then, leave TO CONFIRM facts out of refreshed posts.

The 13 posts confirmed to show a retired price. The 3 possible ones ([[BP-81 best planswift alternatives 2026|BP-81]], [[BP-32 best togal ai alternatives|BP-32]] and [[BP-20 quotr ai vs planswift ai takeoff procurement comparison 2026|BP-20]]) are not in this table, so check them too:

![[Articles.base#Old price still showing]]

### 2. Access and answers from Quotr

| What we need | Why this plan needs it | Question | Needed by |
|---|---|---|---|
| Search Console and Bing Webmaster Tools access | Indexing checks, before-and-after numbers, and which page wins each merge. Every merge waits for it. | [[Q-49 Search Console and Bing set-up\|Q-49]], [[Q-40 Access and history\|Q-40]] | Fri 9 Oct |
| Who can edit posts and add 301 redirects (permanent forwards from an old web address to a new one), and how long a change takes | Every refresh and every merge | [[Q-55 Who can edit the blog and add redirects\|Q-55]] | Fri 9 Oct |
| Named owners and writer time | The pace on this page assumes about 2 writer days a week | [[Q-41 Owners and budget\|Q-41]], [[Q-53 Blog schedule and AI tools\|Q-53]] | Fri 9 Oct |
| A named editor who checks every post before it goes live | Brief notes and tracking tags reached live pages before (W-12) | [[Q-42 Process and plans\|Q-42]] (task A16) | Mon 19 Oct |
| Answers for single posts: turnaround, accuracy, what the DDP price includes, delivery area | BP-82, BP-89, BP-12 and BP-62 cannot state these facts until Quotr confirms them | [[Q-15 Turnaround\|Q-15]], [[Q-18 Accuracy\|Q-18]], [[Q-12 Offer details\|Q-12]], [[Q-11 Delivery area\|Q-11]] (through A1) | October call |
| An expert reviewer for trade and cost posts | "Reviewed by" lines on posts such as BP-62 and BP-56 | [[Q-56 Expert reviewer for trade and cost posts\|Q-56]] | Mon 2 Nov |
| Customer permission and measured hours for RL Electric | The BP-72 merge waits for the rebuilt case study (R-15) | [[Q-29 Permissions\|Q-29]], [[Q-19 Time saved\|Q-19]] | October call |
| Sources for statistics in posts | The "12.6%" in the BP-70 address, and other unsourced figures | [[Q-58 Sources for statistics in posts\|Q-58]] | Mon 7 Dec |

**Helpful, not blocking:** which posts bring leads ([[Q-50 Blog posts that bring leads|Q-50]]), Cloudflare crawler data ([[Q-51 Cloudflare crawler data and logs|Q-51]]), real publish dates ([[Q-52 Real publish dates of six posts|Q-52]]) and one shared block for prices, so the next price change is a one-line edit ([[Q-54 One shared block for prices and facts|Q-54]]).

**Our own checks:** re-run the web search checks for the 60 unchecked posts and re-read the old-price pages in week 1 ([[Q-59 Web search checks for 60 unchecked posts|Q-59]]). Re-check the Google claims before quoting them to Quotr ([[Q-60 Re-check Google claims against official sources|Q-60]]).

### 3. Who does what

| Role | Jobs in this plan |
|---|---|
| **GEO consultant** (Leanid) | Keeps the queue. Writes briefs. Records before-and-after numbers. Checks drafts. Updates the article notes and the [[Changelog]]. Reports each month. |
| **Quotr marketing** (writer) | Edits posts. Moves the best parts across in merges. Requests re-crawls (asks Google and Bing to read a page again). |
| **Named editor** (Quotr) | Signs off every post before it goes live (task A16). |
| **Founder** (CEO or CTO) | Approves any new Quotr fact or number (task A1). Named author or reviewer where they wrote or checked a post. |
| **Dev** | 301 redirects, address changes, sitemap and schema dates (task A9). |

Roles are suggestions, and names are TO CONFIRM with Quotr ([[30-60-90 plan]]). The consultant's share of this work is scoped in [[Retainer scope and value case]].

---

## The plan week by week

### How the order works

1. **Refreshes go in queue order.** That is the `rank` in each article note, set by the [[Blog health audit]]: high-priority posts first; within them, posts cited by AI, posts linked to a tracked buyer question and posts with the old price; then the lowest health score.
2. **A merge always comes before, or in the same release as, the rewrite of its keeper page** (the post that stays).
3. **Merges follow the overlap map's order** from late October: G01 to G04 first; then G10, G12, G05, G07 and G08; G11 and G13 last. The map also puts G14, G06 and G09 in the middle wave. Their keepers need a full rewrite first, so those merges move to January 2027.
4. **Exceptions:**
   - [[BP-82 outsource construction estimating|BP-82]] (queue no. 7) goes live on 2 November, ahead of no. 5 and 6, because task A12 releases it together with the BP-79 merge.
   - [[BP-62 ddp construction materials|BP-62]] (queue no. 25) stays in Q4, because the roadmap (R-07, P1 for October) and task B8 already plan it for this quarter. It takes the place of [[BP-48 best flooring estimating software in 2026|BP-48]] (no. 14), which moves to 2027.
   - A keeper goes live with its merge (rule 2), so [[BP-32 best togal ai alternatives|BP-32]] (no. 2) waits for 26 October and [[BP-46 best electrical estimating software 2026|BP-46]] (no. 11) for 7 December.
5. **No merges, redirects, new titles or address changes while a Google update is rolling out.** Single-page fact fixes may go ahead, with a note on the Search Console chart. If Google starts a new update, shift the merges, not the fact fixes ([[Google search updates 2025-2026]]).
6. **No redirects or address changes after Friday 18 December,** so nothing breaks over the holidays (our suggestion).
7. **Some roadmap dates move.** The roadmap planned [[R-05 Outsourced construction estimating|R-05]] (BP-82), [[R-07 DDP vs FOB for building materials - which is better, and when|R-07]] (BP-62) and [[R-06 Is AI takeoff accurate - What Quotr.ai's testing shows|R-06]] (BP-12) for October. This plan publishes R-06 on 26 October, as planned, and R-05 and R-07 on 2 and 9 November. [[R-13 Construction estimating software with material procurement|R-13]] (BP-38) moves from November to January 2027. Change the `month` of R-05, R-07 and R-13 once Quotr agrees this plan.

### Hours: our assumptions

- **Per post (writer time, including reading the live page):** S = about 3 hours, M = about 8 hours (one working day), L = about 20 hours (two and a half working days).
- **On top of that:** about 1 hour per post for the editor's check and publishing, and about 30 minutes of developer time per redirect.
- **Capacity:** about 16 writer hours a week on average (2 working days). About 12-14 in Thanksgiving week and 8 in Christmas week. Nothing goes live from 28 December to 1 January.
- **Busy weeks:** six weeks come to 17-20 hours, a little over 16. The light first two weeks (6 and 12 hours) leave time to get ahead, for example by reading the merge pages early. If a week still runs over, move its last merge to the catch-up slot in the week of 14 December.
- **Why smaller than the task scale:** the [[30-60-90 plan]] uses S = up to 2 working days and M = 3-10 working days for whole tasks, which often cover many pages. One post is smaller than a task.
- **What the hours count:** the posts in the tables below, including the A2 price fix and the merges. The other October tasks (A3, A6, A7, A8, A13, A14) also need Quotr time; the [[30-60-90 plan]] budgets them.
- Every extra writer day a week adds about one more M post a week. Pull the next posts forward in the same order.

### October 2026

| Week of | Post (queue no.) | Action | Effort · hours | Notes |
|---|---|---|---|---|
| **5 Oct** | The 16 posts on the old-price list | Read the live pages. Nothing goes live. | about 6 h | Record the AI baseline before any fix is re-crawled (A15). Start A17 the day access arrives. Google's spam update may still be running. |
| | **Week total** | | **about 6 h** | Tasks: A1, A4, A11, A15, A16, A17 |
| **12 Oct** | In queue order: [[BP-81 best planswift alternatives 2026\|BP-81]], [[BP-32 best togal ai alternatives\|BP-32]], [[BP-43 best togal ai alternatives 2026\|BP-43]], [[BP-51 stack alternative\|BP-51]], [[BP-80 best ai bid software for construction\|BP-80]], [[BP-46 best electrical estimating software 2026\|BP-46]], [[BP-57 bluebeam alternative\|BP-57]], [[BP-24 best ai construction estimating software 2026\|BP-24]], [[BP-48 best flooring estimating software in 2026\|BP-48]], [[BP-19 ai construction estimating software buyers guide\|BP-19]], [[BP-47 ai bidding software construction\|BP-47]], [[BP-54 best concrete estimating software 2026\|BP-54]], [[BP-76 best glazing estimating software 2026\|BP-76]], [[BP-83 rebar estimating and takeoff software\|BP-83]], [[BP-77 structural steel estimating\|BP-77]], [[BP-20 quotr ai vs planswift ai takeoff procurement comparison 2026\|BP-20]] | Price fix only (A2) | about 12 h (A2's own estimate: 1-2 days) | BP-81, BP-32 and BP-20 were seen only in search summaries: check them. A2 also searches all 96 posts for the old price, which covers 4 list posts nobody has checked yet: [[BP-37 electrical estimating software buyers guide\|BP-37]], [[BP-52 best plumbing estimating software 2026\|BP-52]], [[BP-55 best drywall estimating software in 2026\|BP-55]] and [[BP-64 trade estimating software\|BP-64]] (W-01). Status stays `todo`; add a Log line. |
| | **Week total** | | **about 12 h** | Tasks: A2, A3, A6, A9, A10 |
| **19 Oct** | [[BP-81 best planswift alternatives 2026\|BP-81]] (1) | Update | M · 8 h | Cited by AI (test V3). Keep the web address for now. |
| | [[BP-59 how developers source building materials\|BP-59]] (3) | Update | M · 8 h | Cited by AI. Its factory-count fix goes live earlier, with A3. Keep the web address. |
| | **Week total** | | **16 h** | Also: the A8 quick fix (Quotr's name inside the key facts) on BP-82, BP-85, BP-12, BP-81, BP-56 and BP-87. Read the first four merge pairs and pull their Search Console data. Tasks: A7, A8, A12, A18 |
| **26 Oct** | [[BP-12 is ai takeoff actually accurate yet\|BP-12]] (4) | Update (R-06) | M · 8 h | Cited by AI (P5, T30). Save a copy first, and keep the quoted answer near the top. |
| | [[BP-43 best togal ai alternatives 2026\|BP-43]] into BP-32 | Merge | S · 3 h | Merge first. The 301 goes live with BP-32's rewrite. |
| | [[BP-32 best togal ai alternatives\|BP-32]] (2) | Rewrite (R-04) | M · 8 h | Cited in V1, the only core unbranded answer that named Quotr. |
| | **Week total** | | **19 h** | Tasks: A7, A12, A13, A18 |

### November 2026

| Week of | Post (queue no.) | Action | Effort · hours | Notes |
|---|---|---|---|---|
| **2 Nov** | [[BP-79 construction estimating services\|BP-79]] into BP-82 | Merge | S · 3 h | Merge first, in the same release as BP-82, as A12 plans. |
| | [[BP-82 outsource construction estimating\|BP-82]] (7) | Update (R-05) | M · 8 h | Perplexity's first source for the outsourced-estimating price question (C12). Change sentences, not structure. |
| | [[BP-89 precon on demand outsource bid cost estimation\|BP-89]] into BP-86 | Merge | S · 3 h | Fix its "1-3 days" turnaround first (A3). Both pages were under 8 weeks old in September, so Search Console will have little data: decide on fit, not traffic. |
| | [[BP-80 best ai bid software for construction\|BP-80]] into BP-47 | Merge | S · 3 h | BP-47's own update waits for 2027. |
| | **Week total** | | **17 h** | A12 finishes about a week later than the 30-60-90 plan, so both pages of each pair can be read and checked in Search Console first. Tasks: A12, B3 (November AI test), B13, A18 |
| **9 Nov** | [[BP-62 ddp construction materials\|BP-62]] (25) | Rewrite (R-07) | L · 20 h | Retrieved only: Perplexity looked at it for T10 but did not cite it. Kept in Q4 for R-07 (rule 4 above). Needs Quotr's answers on the DDP offer and delivery area, and an expert reviewer. |
| | **Week total** | | **20 h** | Re-run B2, B4, V2 and T22, about four weeks after the price fix (W-01). Tasks: B8, A18 |
| **16 Nov** | [[BP-87 quantity takeoff services\|BP-87]] (5) | Update | M · 8 h | Cited by AI; tracked prompt T44. |
| | [[BP-56 how to estimate plumbing from drawings\|BP-56]] (6) | Update | M · 8 h | Cited first for its tracked prompt (N2). Change as little of the step text as possible. |
| | [[BP-19 ai construction estimating software buyers guide\|BP-19]] into BP-24 | Merge | S · 3 h | Move its "how to choose" checklist into BP-24. BP-24's own rewrite starts in the week of 30 November. |
| | **Week total** | | **19 h** | Tasks: B8, B13, A18 |
| **23 Nov** | [[BP-05 construction takeoff guide\|BP-05]] into BP-17 | Merge | S · 3 h | Fold its unique parts into BP-17 in the same release (step 4 of BP-17's note). The rest of BP-17's update waits for 2027 (queue no. 32). |
| | [[BP-13 blueprint to priced estimate workflow\|BP-13]] into BP-17 | Merge | S · 3 h | Carry over no unconfirmed speed or accuracy claim (Q-18). |
| | [[BP-51 stack alternative\|BP-51]] (9) | Rewrite | M · 8 h | Retrieved only: Perplexity looked at it (V10) but did not cite it. Wrong competitor facts (A6); its retired price comes off in October (A2). |
| | **Week total** | | **14 h** | Short week: Thanksgiving is Thursday 26 November, so publish by Wednesday. Tasks: B13, A18 |
| **30 Nov** | [[BP-57 bluebeam alternative\|BP-57]] (12) | Rewrite | M · 8 h | Tracked prompt T19 has no working Quotr page. Check its indexing in A17. |
| | [[BP-60 what is construction procurement 2026 guide\|BP-60]] into BP-69 | Merge | S · 3 h | Retires a "2026" web address. |
| | [[BP-24 best ai construction estimating software 2026\|BP-24]] (13) | Rewrite: first draft | L · 8 of 20 h | Tracked prompts T01 and T11. Use the checklist moved in from BP-19 on 16 November. |
| | **Week total** | | **19 h** | Tasks: B13, C9 (December AI test), A18 |

### December 2026

| Week of | Post (queue no.) | Action | Effort · hours | Notes |
|---|---|---|---|---|
| **7 Dec** | [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps\|BP-70]] into BP-03 | Merge | S · 3 h | Retires a "2026" web address with an unsourced number in it. |
| | [[BP-49 construction proforma software\|BP-49]] into BP-22 | Merge | S · 3 h | First give prompt L-138 a page (see the BP-49 note). Merge before the developer hub (R-22) links here. |
| | [[BP-37 electrical estimating software buyers guide\|BP-37]] into BP-46 | Merge | S · 3 h | Merge first. The 301 goes straight to BP-46's final address. |
| | [[BP-46 best electrical estimating software 2026\|BP-46]] (11) | Rewrite | M · 8 h | Tracked prompt T06. If every tool is re-checked, move it to a year-free web address with a 301. |
| | **Week total** | | **17 h** | Tasks: B13, C6, A18 |
| **14 Dec** | [[BP-53 how subcontractors bid gcs without giving away margin\|BP-53]] into BP-28 | Merge | S · 3 h | Add one question heading to BP-28 in the words of prompt L-012. |
| | [[BP-72 how rl electric cut estimating time with ai powered takeoffs\|BP-72]] into the RL Electric case study | Merge | M · 8 h | Only once R-15 is live (task B4). If it is not, move this to January. |
| | Catch-up | Anything that slipped | about 5 h | Most likely a merge still waiting for Search Console data. |
| | **Week total** | | **16 h** | Last week for redirects and address changes in 2026. Decide on "2026" in web addresses and titles (C11). Tasks: B13, B4, C11 |
| **21 Dec** | [[BP-24 best ai construction estimating software 2026\|BP-24]] (13) | Rewrite: second draft | L · 8 of 20 h | Publish in the week of 4 January, with its address decision (C11). |
| | **Week total** | | **8 h** | Christmas week. No redirects or address changes. Tasks: C9 (day-90 review) |
| **28 Dec** | Nothing goes live | Log and measure | — | Run the 28-day before-and-after checks on the October work. Prepare the January batch. |

**Quarter total:** about 183 writer hours. October about 53, November about 89, December about 41.

### What waits for January 2027

1. **Finish and publish [[BP-24 best ai construction estimating software 2026|BP-24]]** (about 4 more hours), with its address decision.
2. **The 4 merges that need their keeper's rewrite,** one release each (about 60 hours in all):
   - [[BP-06 quotr vs traditional estimating|BP-06]] with the update of [[BP-26 quotr vs excel|BP-26]].
   - [[BP-02 the takeoff to transaction gap|BP-02]] with the R-13 rebuild of [[BP-38 takeoff to buyout construction estimating procurement platform|BP-38]]. The roadmap plans R-13 for November, but no task schedules it, and this quarter has no room for another large (L) rewrite.
   - [[BP-11 how ai construction estimating works|BP-11]] and [[BP-71 how ai construction takeoff works in 2026|BP-71]] with the rewrite of [[BP-45 what is ai construction estimating software|BP-45]].
3. **Then the queue carries on:** [[BP-48 best flooring estimating software in 2026|BP-48]] (14), [[BP-85 commercial estimating services|BP-85]] (15), [[BP-47 ai bidding software construction|BP-47]] (17), [[BP-23 tariff impact construction costs 2026 steel aluminum copper|BP-23]] (18), [[BP-54 best concrete estimating software 2026|BP-54]] (19), [[BP-76 best glazing estimating software 2026|BP-76]] (20) and so on.
4. **[[BP-17 how to do construction takeoff pdf blueprint|BP-17]] (now no. 32) left the Q4 list.** It appears in test notes but was not cited, so it lost its AI boost in the queue. BP-05 and BP-13 still merge into it on 23 November; its own update waits for its turn.

**About task B8:** it plans three rebuilds for November: R-09 ([[BP-88 sourcing building materials china cbd fair 2026|BP-88]], queue no. 35), R-11 ([[BP-61 reduce construction material costs|BP-61]], no. 31) and R-12 (BP-23, no. 18). If Quotr finds extra writer time for B8, those three are done in November and leave this queue early. If not, they wait for their turn.

The live queue (the next 15 posts with status `todo` or `doing`):

![[Articles.base#Refresh queue]]

---

## Merges, in order

- **17 merges in all:** 16 from the overlap map, plus the RL Electric post, which moves into its case study.
- **13 happen in Q4. 4 wait for January 2027,** because their redirect must go live with the keeper's rewrite.
- A12 covers merges 1-3. The new task B13 covers the other 14.

**Before each merge**
- Read both live pages. Most pages in the overlap groups were never read in full.
- Pull Search Console data for both web addresses (clicks, impressions, AI impressions and links). Compare only periods that start on or after 2026-04-28.
- If the post being merged is clearly stronger, raise it with the consultant before redirecting.
- Check the text you move for retired prices and TO CONFIRM facts. Move only what the keeper lacks.

**After each 301:** update internal links, take the old address out of the blog sitemap, update llms.txt and the prompt notes' `quotr_url`, request a re-crawl of both addresses, and watch the keeper for 4-8 weeks ([[Content refresh playbook#When a 301 redirect is needed]]; [[Page refresh checklist]] §5).

| # | Merge this post | Into (keeper) | Redirect (301) | When | Check first |
|---|---|---|---|---|---|
| 1 | [[BP-43 best togal ai alternatives 2026\|BP-43]] | [[BP-32 best togal ai alternatives\|BP-32]] | /blog/best-togal-ai-alternatives-2026/ → /blog/best-togal-ai-alternatives/ | Week of 26 Oct, with BP-32's rewrite (A12) | Move only the buying checklist, the comparison table and the best FAQ answers. |
| 2 | [[BP-79 construction estimating services\|BP-79]] | [[BP-82 outsource construction estimating\|BP-82]] | /blog/construction-estimating-services/ → /blog/outsource-construction-estimating/ | 2 Nov, with BP-82's update (R-05, A12) | Carry over no turnaround except the one A1 approves (Q-15). |
| 3 | [[BP-89 precon on demand outsource bid cost estimation\|BP-89]] | [[BP-86 preconstruction services\|BP-86]] | /blog/precon-on-demand-outsource-bid-cost-estimation/ → /blog/preconstruction-services/ | 2 Nov (A12) | Ask Quotr whether "Precon on Demand" is still a named offer. |
| 4 | [[BP-80 best ai bid software for construction\|BP-80]] | [[BP-47 ai bidding software construction\|BP-47]] | /blog/best-ai-bid-software-for-construction/ → /blog/ai-bidding-software-construction/ | 2 Nov (B13) | Both posts carried the old price: fix both first (A2). |
| 5 | [[BP-19 ai construction estimating software buyers guide\|BP-19]] | [[BP-24 best ai construction estimating software 2026\|BP-24]] | /blog/ai-construction-estimating-software-buyers-guide/ → /blog/best-ai-construction-estimating-software-2026/ | 16 Nov (B13) | Keep it separate only if Search Console shows it earns its own "how to choose" searches (G10). If BP-24 later moves to a year-free address, point this redirect straight there. |
| 6 | [[BP-05 construction takeoff guide\|BP-05]] | [[BP-17 how to do construction takeoff pdf blueprint\|BP-17]] | /blog/construction-takeoff-guide/ → /blog/how-to-do-construction-takeoff-pdf-blueprint/ | 23 Nov (B13) | The oldest post in its group, so check it for links from other sites. |
| 7 | [[BP-13 blueprint to priced estimate workflow\|BP-13]] | [[BP-17 how to do construction takeoff pdf blueprint\|BP-17]] | /blog/blueprint-to-priced-estimate-workflow/ → /blog/how-to-do-construction-takeoff-pdf-blueprint/ | 23 Nov (B13) | Leave out "under 12 minutes" and "95-99%" unless Quotr confirms them. |
| 8 | [[BP-60 what is construction procurement 2026 guide\|BP-60]] | [[BP-69 construction procurement process\|BP-69]] | /blog/what-is-construction-procurement-2026-guide/ → /blog/construction-procurement-process/ | 30 Nov (B13) | Re-point the glossary link and prompt note L-125. |
| 9 | [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps\|BP-70]] | [[BP-03 construction cost trends 2026\|BP-03]] | /blog/construction-costs-surged-12-6-in-2026-how-ai-estimation-helps/ → /blog/construction-cost-trends-2026/ | 7 Dec (B13) | Find the source of "12.6%" (Q-58). |
| 10 | [[BP-49 construction proforma software\|BP-49]] | [[BP-22 real estate pro forma software comparison\|BP-22]] | /blog/construction-proforma-software/ → /blog/real-estate-pro-forma-software-comparison/ | 7 Dec (B13) | Give prompt L-138 a page first. |
| 11 | [[BP-37 electrical estimating software buyers guide\|BP-37]] | [[BP-46 best electrical estimating software 2026\|BP-46]] | /blog/electrical-estimating-software-buyers-guide/ → BP-46's final address | 7 Dec, with BP-46's rewrite (B13) | If BP-46 moves to /blog/best-electrical-estimating-software/, point this redirect there. |
| 12 | [[BP-53 how subcontractors bid gcs without giving away margin\|BP-53]] | [[BP-28 how to bid commercial construction projects subcontractor estimating takeoff guide\|BP-28]] | /blog/how-subcontractors-bid-gcs-without-giving-away-margin/ → /blog/how-to-bid-commercial-construction-projects-subcontractor-estimating-takeoff-guide/ | 14 Dec (B13) | If its "6-habit playbook" borrows Billd's framing, credit Billd. |
| 13 | [[BP-72 how rl electric cut estimating time with ai powered takeoffs\|BP-72]] | RL Electric case study | /blog/how-rl-electric-cut-estimating-time-with-ai-powered-takeoffs/ → /case-studies/rl-electric/ | 14 Dec, once R-15 is live (B4, B13) | Customer permission and measured hours (Q-29, Q-19). |
| 14 | [[BP-06 quotr vs traditional estimating\|BP-06]] | [[BP-26 quotr vs excel\|BP-26]] | /blog/quotr-vs-traditional-estimating/ → /blog/quotr-vs-excel/ | January 2027, with BP-26's update (B13) | Move "The ROI case" with approved figures only. |
| 15 | [[BP-02 the takeoff to transaction gap\|BP-02]] | [[BP-38 takeoff to buyout construction estimating procurement platform\|BP-38]] | /blog/the-takeoff-to-transaction-gap/ → /blog/takeoff-to-buyout-construction-estimating-procurement-platform/ | January 2027, with the R-13 rebuild of BP-38 (B13) | Keep the phrase "the takeoff-to-transaction gap" in the new section. |
| 16 | [[BP-71 how ai construction takeoff works in 2026\|BP-71]] | [[BP-45 what is ai construction estimating software\|BP-45]] | /blog/how-ai-construction-takeoff-works-in-2026/ → /blog/what-is-ai-construction-estimating-software/ | January 2027, with BP-45's rewrite (B13) | Merge only if Search Console shows it earns nothing BP-45 cannot hold. Until then, do not re-date or retitle it. |
| 17 | [[BP-11 how ai construction estimating works\|BP-11]] | [[BP-45 what is ai construction estimating software\|BP-45]] | /blog/how-ai-construction-estimating-works/ → /blog/what-is-ai-construction-estimating-software/ | January 2027, with BP-45's rewrite (B13) | Do not carry over its "80%" or "20 hours to 1-2" claims, or any retired price (A2, A3). |

Merge order follows the overlap map: G01 to G04 first (rows 1-4), then the middle wave (rows 5-10), with G11 and G13 last (rows 11-12). Row 13 (RL Electric) is not in the map; it waits for its case study. The map also puts G14, G06 and G09 (rows 14-17) in the middle wave, but they wait for their keepers' rewrites in January.

The live list of posts marked for merging:

![[Articles.base#Merge or retire]]

---

## January 2027: the year in URLs and titles

- **27 post web addresses contain "2026"** ([[What went wrong]], W-16).
- **At least 10 live titles contain "2026" too.** About 80 of the 96 live titles were never recorded, so there are probably more: check each page. 5 of the 10 are on posts with no year in the web address (last row of the table below).
- **Google has given no official guidance** on year-stamped web addresses at year end, as far as our claim set shows ([[Google search updates 2025-2026]]).
- **Practitioners reported** that posts "lightly refreshed with '2026' in the title" were among the pages that lost Google visibility in early 2026. Google has not confirmed this (FRESH-08, QUALITY-11).
- **The rule:** never bulk-rename "2026" to "2027". Decide post by post by Friday 18 December (task C11).

### What to decide

| Situation | Posts | What to do | When |
|---|---|---|---|
| **Retired by a Q4 merge** | [[BP-43 best togal ai alternatives 2026\|BP-43]], [[BP-60 what is construction procurement 2026 guide\|BP-60]], [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps\|BP-70]] | Nothing more. The 301 already retires the year address. | Done in Q4 |
| **Retired by a January merge** | [[BP-71 how ai construction takeoff works in 2026\|BP-71]] | The 301 into BP-45 retires it. If Search Console says keep it, move it to a year-free address at its first real update instead. | January 2027 |
| **Evergreen (still useful after 2026), refreshed in Q4** | [[BP-46 best electrical estimating software 2026\|BP-46]], [[BP-81 best planswift alternatives 2026\|BP-81]], [[BP-24 best ai construction estimating software 2026\|BP-24]] | Move to a year-free address with a 301 at the real update: BP-46 in its December release, if every tool was re-checked. BP-81 and BP-24 in early January, with a real 2027 update, after checking Search Console. | 7 Dec; 4-15 Jan |
| **Evergreen, not refreshed by January** | [[BP-48 best flooring estimating software in 2026\|BP-48]], [[BP-54 best concrete estimating software 2026\|BP-54]], [[BP-76 best glazing estimating software 2026\|BP-76]], [[BP-33 hvac estimating software 2026 buyers guide\|BP-33]], [[BP-55 best drywall estimating software in 2026\|BP-55]], [[BP-15 quotr vs togal ai comparison 2026\|BP-15]], [[BP-20 quotr ai vs planswift ai takeoff procurement comparison 2026\|BP-20]], [[BP-52 best plumbing estimating software 2026\|BP-52]] | Leave the address, title and dates alone for now. Move to a year-free address, with a 301, at the post's real refresh in 2027. | At each refresh |
| **Rebuilt as a lasting guide** | [[BP-88 sourcing building materials china cbd fair 2026\|BP-88]], [[BP-35 construction cost index q1 2026 ppi rsmeans mortenson\|BP-35]] | Move to a year-free address at the rebuild (R-09 for BP-88; the next data update for BP-35). The playbook lists both with the dated posts; the post-by-post review now suggests moving them, because the rebuild drops the event or quarter from the title. | At the rebuild |
| **About 2026, or worth moving only after a real update** | [[BP-03 construction cost trends 2026\|BP-03]], [[BP-23 tariff impact construction costs 2026 steel aluminum copper\|BP-23]], [[BP-27 state of ai in preconstruction 2026 adoption roi enr top 400 gcs\|BP-27]], [[BP-16 construction labor shortage ai adoption 2026\|BP-16]], [[BP-58 house flipping math 2026\|BP-58]] | Keep as a dated 2026 record, or give a real 2027 edition a year-free address and 301 the 2026 address to it. Check Search Console first. | Decide in December; act in 2027 |
| **Event recaps** | [[BP-07 dallas build expo 2026 recap\|BP-07]], [[BP-09 re forge sf 2026 recap\|BP-09]], [[BP-14 nhca build the builder 2026 recap\|BP-14]], [[BP-73 ibs 2026 from the magic of orlando to the reality of ai implementation\|BP-73]], [[BP-78 pcbc 2026 recap quotr ai takeoff service\|BP-78]] | Leave alone. The year is part of the subject. | — |
| **"2026" in the title only** (the web address has no year) | [[BP-32 best togal ai alternatives\|BP-32]], [[BP-82 outsource construction estimating\|BP-82]], [[BP-87 quantity takeoff services\|BP-87]], [[BP-85 commercial estimating services\|BP-85]], [[BP-86 preconstruction services\|BP-86]] | Keep the address. At the January review, drop "(2026)" from the title, or change the year only after a real update. BP-32 gets a new title in its October rewrite (R-04): keep "(2026)" only if every entry was re-checked. | Decide in December; change titles in January |

The first seven rows cover the 27 posts with "2026" in the web address: 3 + 1 + 3 + 8 + 2 + 5 + 5 = 27. The last row adds 5 posts with the year in the title only.

### How to decide

1. **Week of 14 December:** the consultant lists every post with "2026" in its web address or title, with what happened to it in Q4.
2. **For each post, answer three questions:**
   - Was every fact, price and entry re-checked this quarter?
   - What do Search Console clicks, impressions and links show? (Compare only periods that start on or after 2026-04-28.)
   - Is the page evergreen, or is it about 2026?
3. **Pick one row from the table above.** Write the decision as a Log line in the article note. Add one [[Changelog]] line for the batch.
4. **Titles:** keep "2026" only while every entry is checked for 2026. In January, drop the year, or re-check everything for 2027. Show a "Last checked [month year]" line in the body instead.
5. **Moves happen in the weeks of 4 and 11 January 2027,** and only if no Google update is rolling out. Use one hop: point older redirects (such as BP-19's and BP-37's) straight at the final address. Update internal links, the sitemap, llms.txt and the prompt notes' `quotr_url`. Request a re-crawl, and watch each page for 4-8 weeks.

More detail: [[Content refresh playbook]], rule 6 ("Years in titles and web addresses"), and the "Title" and "Web address" advice in each article note.

---

## How we track progress

### In each article note

| When | Set `status` to | Add a Log line like this (example) |
|---|---|---|
| Work starts | `doing` | — |
| Price fix only (A2) | leave it at `todo` | "2026-10-14: removed the retired Solo/Team prices; added the dated Lite/Plus/Enterprise line; re-crawl requested. Checked by [editor]." |
| Refresh live and checked | `done` | What changed, the new health score, who checked it. |
| Merge: the old post | `done` once the 301 is live | "Merged into BP-32; 301 live; links and sitemap updated." |
| Merge: the keeper | unchanged, unless it had its own refresh | "Received BP-43's checklist and FAQ." |
| Work dropped | `dropped` | Why. |

- After each refresh, re-score the six areas and update `health` and `health_score`. Remove flags that no longer apply. Set `old_pricing` to `no` once the live page shows no retired price ([[Content refresh playbook]], "After each refresh").
- The Log is append-only. Never delete an article note, even for a merged post.
- Add one [[Changelog]] line for each week's batch (vault rule 7).

### The live tables

They update by themselves as you change each note's status. Posts leave this table when they are set to `done`:

![[Articles.base#Full refresh plan]]

### The few numbers to report each month

| Number | Where it comes from | KPI | What this plan expects |
|---|---|---|---|
| **Posts done against plan** (refreshes and merges) | Article note status and Log lines | — | October: price fix on 16 posts, 4 refreshes, 1 merge. November: 6 refreshes, 7 merges. December: 1 refresh, 5 merges. January: BP-24 goes live. |
| **Posts still showing a retired price** | Site search; the "Old price still showing" view | L9 | 0 stale-price pages within 90 days (suggested target) |
| **Posts indexed**, out of the live posts | Search Console, Page indexing (task A17) | Suggested as a monthly KPI (W-10) | Baseline first, from A17 |
| **Refreshed posts: clicks and AI impressions, 28 days before vs after** | Search Console Performance and Generative AI report | L2 (d) | The direction of change; no target yet |
| **Tracked prompts for refreshed posts: cited, named, right price** | The monthly AI test (B3 in November, C9 in December) | L2, L3, L4, L6 | L4: at least 2 of C12, V3 and P5 name Quotr within 90 days. L6: 2 of 8 branded answers with errors, or fewer (suggested targets) |

- Targets come from [[KPIs and dashboard]] §4. They are suggested by this knowledge base, not agreed with Quotr.
- Do not measure across a Google update rollout. Count a change only if it holds in two monthly runs in a row ([[KPIs and dashboard]]).
- The monthly routine is in [[Content refresh playbook]] ("The monthly loop") and [[Search Console audit playbook]] ("How often").

---

## Tasks

| Task | Its part in this plan | When |
|---|---|---|
| [[A1 Agree and sign off one fact sheet\|A1]] | The facts every refreshed post copies | Week of 5 Oct |
| [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere\|A2]] | Price fix on the 16 posts | Week of 12 Oct |
| [[A3 Fact-fix sweep, part 2 - every other conflicting fact\|A3]] | Turnaround, factory count and other facts | October |
| [[A6 Editorial sweep\|A6]] | Leftover brief text and competitor facts | October |
| [[A7 Named author bylines and author pages\|A7]] | A named author on every refreshed post | October |
| [[A8 Put the Quotr name inside key facts on the pages AI already reads\|A8]] | Quick fix on six of the 8 cited posts | Week of 19 Oct |
| [[A9 Sitemaps and lastmod dates\|A9]] | Dates that change only with real edits | October |
| [[A12 Merge duplicate pages\|A12]] | Merges 1-3 (Togal and services) | 26 Oct to 6 Nov |
| [[A15 Measurement setup and multi-engine baseline\|A15]] | The "before" AI picture | Week of 5 Oct |
| [[A16 Add a human edit and fact-check step for AI-assisted drafts\|A16]] | A named editor signs off every post | Before 19 Oct |
| **New:** [[A17 First Search Console audit of the 96 blog posts\|A17]] | Indexing and Search Console numbers for every post | From the day access arrives |
| **New:** [[A18 Refresh the top of the blog queue, October to December\|A18]] | The 12 refreshes in this plan | 19 Oct to 24 Dec; BP-24 goes live in the week of 4 Jan |
| [[B3 Second monthly AI test; set engine-specific targets\|B3]] | Re-tests after the price fix and the October refreshes | November |
| [[B4 Proof pages - case studies with numbers\|B4]] | The RL Electric case study (R-15), before merge 13 | November |
| [[B8 Procurement and tariff decision guides\|B8]] | BP-62 (R-07); BP-88, BP-61 and BP-23 if built in November | November |
| **New:** [[B13 Finish the merges from the overlap map\|B13]] | Merges 4-17 | 2 Nov to 14 Dec; 4 in January |
| [[C6 Developer hub, deep electrical page, integrations page, one honest comparison\|C6]] | The developer hub links to the pro forma keeper after merge 10 | December |
| [[C9 Third monthly AI test and the day-90 review\|C9]] | December re-tests and the day-90 review of this plan | December |
| **New:** [[C11 Decide on 2026 in blog web addresses and titles\|C11]] | The January 2027 decision on "2026" | Decide 14-18 Dec; move 4-15 Jan |

What to do next, across all tasks:

![[Tasks.base#Next up]]

---

## Related pages

- [[Content refresh playbook]]: the monthly loop, the health score and the rules behind this plan
- [[Page refresh checklist]]: the step-by-step edit of one page
- [[Blog health audit]]: how the 96 posts were scored, and the full overlap map
- [[Search Console audit playbook]]: the Search Console checks, step by step
- [[What went wrong]]: the 19 findings behind the fixes
- [[Google search updates 2025-2026]]: when to hold merges and address changes
- [[Publishing patterns and correlations]]: how and when the posts were published
- [[30-60-90 plan]]: all tasks, owners and phases
- [[Retainer scope and value case]]: how this work fits the 12-month engagement
