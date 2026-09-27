---
type: baseline
description: 'How Quotr publishes (pace, timing, topics) and the 13 patterns that held up when we tested the blog against AI answers, buyer questions and the tracking set.'
last_verified: 2026-09-26
verify_every_days: 30
aliases:
- Publishing patterns
- Blog correlations
---
# Publishing patterns and correlations

> [!abstract] What this page is for
> This page shows how Quotr's blog has been published: how fast, on which days and on which topics. It then lists the 13 patterns that held up when three separate reviewers tried to knock them down, and the leads that did not. Use it to set a realistic pace, to choose what to write or fix next, and to spot gaps in how we measure progress.

> [!info]- Sources
> - **Blog dates:** the blog sitemap (the list of pages a site gives to search engines), read on 2026-09-25. Its "last changed" date stands in for the publish date.
> - **Website audit:** the 2026-09-25 audit of quotr.ai ([[Website audit]]) and the 2026-09-26 health check of all 96 posts ([[Blog health audit]]).
> - **AI tests:** the 64 Perplexity test runs of 2026-09-25 ([[AI visibility baseline]]).
> - **Web search checks:** targeted searches for single posts on 2026-09-25 and 2026-09-26. 36 of 96 posts were checked ([[Q-59 Web search checks for 60 unchecked posts|Q-59]]).
> - **Buyer questions:** the 282 prompts in the [[Prompt library]] and the 53 tracked prompts in the [[Tracking set]].
> - **Competitors:** the competitor publishing data in [[Competitor publishing benchmark]] and [[Publishing beyond the blog]].
> - **Post data:** one record per post (date, topic, format, year in the address, old price, AI citation, web search result, matching prompts), built on 2026-09-26.
> - **Test codes** such as C12, V1 or P5 name single prompts from the 2026-09-25 Perplexity tests. T01-T53 are tracked prompts. E-###, L-### and D-### are prompt library IDs.

> [!note]- Words used on this page
> - **Retrieved / cited / named:** the AI looked at a Quotr page / used it as a source in its answer / said "Quotr" in the answer text.
> - **Cited post:** a post used as a source in an answer to a buyer question that does not name Quotr. 8 posts were cited on 2026-09-25.
> - **Unbranded prompt:** a question that does not name Quotr. **Brand prompt:** one that does.
> - **Source list:** the links an AI answer shows as its sources.
> - **Funnel stages:** Learn (how-to and explainer questions), Compare (which tool or service to pick), Decide (questions about Quotr itself). In the post data, TOFU, MOFU and BOFU mean top, middle and bottom of the funnel.
> - **Slug:** the last part of a web address, for example `best-togal-ai-alternatives-2026`.
> - **p-value:** the chance of seeing a gap this big by luck alone. Below 0.05 is the usual bar. With small samples, treat even a low p-value with care.
> - **Correction for many tests:** when you run many tests, a few will pass the 0.05 bar by luck. A correction raises the bar to allow for that.
> - **Significant:** passes the 0.05 bar above.
> - **Median:** the middle value when items are sorted.
> - **Core prompts:** the 40 prompts of the September baseline (C, P, V and B codes). 32 of them do not name Quotr. The 51 unbranded answers on this page add 19 extra prompts (N, S and O codes). Pages that say "1 of 32" count the core set only.
> - **Category prompt:** a generic "best X software" question.
> - **Head-to-head:** a "Quotr vs X" post.
> - **Source slot:** one link in an answer's source list.
> - **Persona:** the type of buyer a post is written for.
> - **Bottom of the funnel:** buyers close to a decision.
> - **Freshness stamp:** a year put in an address or title to look current.
> - **Hub:** a main page that links to all pages on one topic.
> - **Redirect (301):** a permanent forward from an old web address to a new one.
> - **Web index:** the store of pages a search engine can show. "Came back in web search" means a targeted search found the post.
> - **Search Console:** Google's free report on how a site does in search.
> - **KPI:** a number we track every month ([[KPIs and dashboard]]).
> - **(inference):** our reading of the evidence, not a tested result.
> - **How sure (Strong / Moderate / Weak):** Strong = the numbers held and other explanations were ruled out. Moderate = it holds, but a small sample or another cause may explain part of it. Weak = a hint only. The points are the review score (see [[#How we tested]]).
> - **IDs on this page:** K-01 to K-13 are the 13 findings. C-01 to C-45 are review candidates. C12, V1 and P5 are test prompts. A2, B2 and C11 are tasks. BP-## are blog posts, R-## roadmap items, Q-## open questions, and W-## items in [[What went wrong]].

---

## The short version

- **Output more than halved in mid-July and has stayed lower.** The blog ran at about 5.6 posts a week from May to mid-July. Since then it has held at 2-3 a week, about 10 a month. Plan the roadmap around that number ([[#K-01 Output more than halved in mid-July and has stayed lower|K-01]]).
- **Fair context:** a young team published 96 posts in about six months. The current pace of about 10 a month sits inside the 8-12 pieces a month the plan recommends ([[What went wrong#W-12 Output grew faster than the editing check|W-12]]).
- **Topics came in waves, and the latest wave is service pages.** Since August, 11 of 18 posts are estimating-service pages. Agree the service-page plan with Quotr's team before more are added ([[#K-02 From June, one topic led each month, ending in a push on service pages|K-02]]).
- **A post is a start, not a result.** 17 of 25 tracked prompts with a matching Quotr post got no Quotr presence at all. Most losses happen before the answer is written: the page is not picked as a source ([[#K-05 A matching post is a start, not a result|K-05]], [[#K-06 Most losses happen before the answer is written|K-06]]).
- **The type of question matters most.** Quotr was absent from all 22 generic "best X software" answers. It showed up in 4 of 5 service and sourcing answers. Quotr's own ranked lists are unlikely to win these answers. Third-party lists and review sites look like the better route, but that is not yet tested ([[#K-07 Quotr was absent from every generic best-software answer|K-07]], [[#K-08 Rival and alternatives answers lean on review directories|K-08]]).
- **AI uses Quotr's pages but rarely says "Quotr".** Quotr was named in 2 of 51 unbranded answers; Buildxact in 17 and STACK in 14. On Perplexity, how-to answers named no brand at all, so judge how-to posts on citations ([[#K-09 How-to answers name no brand, so Learn posts can win citations but rarely mentions|K-09]], [[#K-10 Rivals are named far more often than Quotr|K-10]]).
- **Finish trades have almost no posts.** Only 3 of 42 finish and envelope trade prompts (cabinets, windows, roofing, tile and similar) have a post. Almost no post is written for residential buyers; whether they are a target market is still open ([[#K-04 The blog is written for commercial buyers; finish trades are the clear gap|K-04]], [[Q-26 Primary audience|Q-26]]).
- **Our own measuring has blind spots.** The tracking set barely watches the service line or the how-to questions, and the prompt map cannot see duplicate posts. Add a few prompts before the October merges ([[#K-11 The service line, now most new posts, is barely tracked|K-11]] to [[#K-13 The prompt map cannot see duplicate posts|K-13]]).
- **32 other candidates did not pass review.** 31 are listed below: 16 leads worth re-testing and 15 we ruled out. The last one, C-03 (weekday batches), is covered under [[#Weekdays and same-day batches]]. None of them is a finding.

> [!warning] How sure we are
> - **Dates are stand-ins.** We used the blog sitemap date as the publish date. 6 posts had their dates reset in bulk on 2026-07-15 and 2026-07-24, so they are left out of all timing figures ([[Q-52 Real publish dates of six posts|Q-52]]).
> - **One AI engine, one day.** All AI results come from Perplexity on 2026-09-25, mostly one run per prompt. Other engines may behave differently.
> - **Small samples.** Many results rest on 3 to 30 tests. A single changed result can move a percentage a lot.
> - **Many comparisons.** We tested 45 candidate patterns and many numbers inside each. A few "significant" results could be luck.
> - **Correlation is not cause.** Two things moving together does not show that one causes the other.
> - **No fresh page reads.** quotr.ai could not be opened on 2026-09-26 (network block), so no page was re-read that day.
> - **Web search is partial.** 60 of 96 posts were not checked in web search, and the search tool is not Google. We had no Search Console data.

---

## How Quotr publishes

### Posts by month

| Month | Posts in the sitemap | With real dates | Leading topic (real-dated posts) |
|---|---|---|---|
| Dec 2025 | 1 | 1 | Customer story (Vanderbilt) |
| Mar 2026 | 1 | 1 | Procurement and sourcing |
| Apr 2026 | 6 | 6 | Trade how-tos (2 of 6) |
| May 2026 | 22 | 22 | Trade how-tos (6) and AI explainers (5) |
| Jun 2026 | 25 | 25 | Best-of lists and buyer guides (10 of 25) |
| Jul 2026 | 23 | 17 | Procurement and sourcing (7 of 17) |
| Aug 2026 | 11 | 11 | Estimating services (7 of 11) |
| Sep 2026 (to the 24th) | 7 | 7 | Estimating services (4 of 7) |
| **Total** | **96** | **90** | |

- The 6 July posts without real dates are the bulk-reset posts.
- The first post is from 19 December 2025. The next came 95 days later, on 24 March 2026.
- The sitemap was read on 25 September. Its newest post is dated 24 September, so September is a part month.

### Three speeds

| Phase | Dates | Real-dated posts | Pace |
|---|---|---|---|
| Slow start | 1 Apr to 4 May | 6 in 34 days | about 1.2 a week |
| Sprint | 5 May to 16 Jul | 58 in 73 days | about 5.6 a week |
| Slower pace | 17 Jul to 24 Sep | 24 in 70 days | about 2.4 a week |

- The sprint was about 2.3 times faster than the pace since.
- Other pages quote about 5.4 and 2.3 posts a week ([[Blog health audit]], [[What went wrong#W-12 Output grew faster than the editing check|W-12]]). They use slightly different date windows. The drop is the same.
- Since late July the pace has been steady at 2-3 posts a week. It is not clearly still falling.
- The switch was not sharp. 17 July fits best, but a steady slide from mid-June fits almost as well. Details in [[#K-01 Output more than halved in mid-July and has stayed lower|K-01]].

### Weekdays and same-day batches

| Weekday | Posts | Days with at least one post |
|---|---|---|
| Monday | 6 | 6 |
| Tuesday | 32 | 20 |
| Wednesday | 15 | 14 |
| Thursday | 24 | 19 |
| Friday | 13 | 12 |
| Saturday and Sunday | 0 | 0 |

- **Weekdays only.** None of the 90 real-dated posts went out at a weekend.
- **Tuesday was the batch day during the sprint.** Across all real-dated posts, 16 days had 2 or more posts (35 posts, 39%), and 10 of those 16 were Tuesdays. 13 of the 16 fell in the May to mid-July sprint, and 9 of those 13 were Tuesdays. Three days had 3 posts: 2026-05-07, 2026-06-02 and 2026-07-07.
- **Count days, not posts.** Tuesday's lead in posts comes from batching. Counted by publishing day, Tuesday (20) and Thursday (19) are level.
- **Since 15 July there is no clear weekday pattern** (26 posts: Tuesday 7, Friday 7, Wednesday 6, Thursday 5, Monday 1). Fewer batches is what the slower pace would produce anyway.
- **No link to AI citation.** Batch-day posts were cited 4 of 35 times, single-day posts 4 of 55 (p = 0.71).
- **The dates may be deploy times.** They may show when the site was updated, not when an editor chose to publish. [[Q-53 Blog schedule and AI tools|Q-53]] asks Quotr.
- This was tested as a pattern and did not pass (C-03). It is context only.

### Topic campaigns and the move to service pages

| Period | Leading topic | Share of that period's posts |
|---|---|---|
| Apr-May | A mix: trade how-tos, AI explainers, head-to-heads | 8, 6 and 5 of 28 |
| June | Best-of lists and buyer guides | 10 of 25 (40%) |
| July | Procurement and sourcing | 7 of 17 (41%) |
| Aug-Sep | Estimating services | 11 of 18 (61%) |

- **Bottom-of-funnel posts arrived last.** They were 1 of 66 posts in April to July, and 11 of 17 in August and September (brand posts left out). All 11 are service pages.
- **Only three topics came in one clear burst:** best-of lists, procurement and services. Trade how-tos ran from 16 April to 10 September.
- **Most topics got a later post.** 7 of 10 topics had a new post after a pause of 30 days or more.
- Details in [[#K-02 From June, one topic led each month, ending in a push on service pages|K-02]].

### The year in the web address

- 27 of 96 slugs contain "2026".
- By month (real-dated posts): April 2 of 6, May 8 of 22, June 8 of 25, July 4 of 17, August 2 of 11, September 0 of 7.
- The fall after July comes from the move to service pages, which never carry a year in the slug. It is not a new habit.
- Details in [[#K-03 The 2026 in web addresses follows the format and showed no citation gain|K-03]].

### Every post by month

![[Articles.base#By month]]

---

## 13 patterns that held up

Each pattern below went through three reviews (numbers recomputed, other explanations checked, usefulness checked). Each kept its numbers and scored at least 2 of 3 points, so some reviewers still rated it weak. Where a reviewer said the first wording went too far, we use the softer version. The review ID (C-01 to C-45) is the candidate's number in the review data, a file outside the vault. It is not a test code such as C12 or a task such as C11.

### K-01 Output more than halved in mid-July and has stayed lower

**Quotr's blog went from about 5.6 posts a week to about 2.4 a week, and has held there since late July.**

**What we see**
- 5 May to 16 July: 58 posts in 73 days. 17 July to 24 September: 24 posts in 70 days. With the 6 reset posts left out, output fell about 57%.
- In working days (Monday to Friday), 1.06 posts a day (1 May to 14 July) against 0.46 (1 August to 24 September). p = 0.0014.
- This second test leaves out 15 to 31 July, when the switch happened.
- Even if all 6 bulk-reset posts really came out after mid-July, output still fell 46% (p = 0.005).
- August (11 posts) and September (7 to the 24th) ran at the same pace (p = 0.81). 11 of the last 18 posts are service pages.

**How sure:** Strong (C-01, 3 of 3 points). Why output fell is not known. A site rebuild, the service-line push, staffing or a deliberate choice would all look the same in this data.

**What it means for Quotr**
- About 10 posts a month is Quotr's current rate. That is a planning number, not a verdict on the team.
- The [[Content roadmap]] plans 68 items from October 2026 to March 2027: 62 written pieces and 6 videos. Some pieces are rebuilds of existing pages.
- By month that is 7, 12, 11, 12, 12 and 14, about 11 on average. Only October is below the current pace of about 10 posts a month.

**What to do**
- Agree who writes what: either the engagement supplies the extra writing, or lower-priority roadmap items wait ([[Retainer scope and value case]]).
- Count posts once a month. A month with 5 or fewer would be a real further drop; at the current pace that happens by chance only about 7% of the time. Ask why output changed ([[Q-53 Blog schedule and AI tools|Q-53]]).

### K-02 From June, one topic led each month, ending in a push on service pages

**From June the blog worked through one main topic at a time. Since August it has been almost only estimating-service pages.**

**What we see**
- Best-of lists led June (10 of 25), procurement led July (7 of 17), and services led August and September (11 of 18). April and May were a mix.
- Service pages: 11 of 18 posts from 4 August to 24 September, against 1 of 70 from April to July (p below 0.0001).
- Only three topics came in one clear burst (lists, procurement, services). "Moving down the funnel" is the same fact as the service push.
- The shift did not change how often new posts match a tracked prompt (4 of 18 against 22 of 70, p = 0.57).

**How sure:** Strong for the move to service pages (C-02, 2 of 3 points). Moderate for "one topic at a time", which holds for only 3 of 10 topics.

**What it means for Quotr**
- Since August the blog has published almost only service pages. Three of them are already cited by AI: [[BP-82 outsource construction estimating|BP-82]], [[BP-85 commercial estimating services|BP-85]] and [[BP-87 quantity takeoff services|BP-87]].
- The roadmap's own service items ([[R-05 Outsourced construction estimating|R-05]], [[R-52 Quotr Service by the numbers|R-52]]) could collide with this series.

**What to do**
- Agree the service-page structure with Quotr's team now: one Service hub (the rebuilt [[R-05 Outsourced construction estimating|R-05]] page) plus 3-4 clearly different pages. See [[What went wrong#W-06 The Service pivot was built as a dozen similar pages|W-06]].

### K-03 The 2026 in web addresses follows the format and showed no citation gain

**"2026" sits in the slugs of lists, guides and comparisons, never in service pages or trade how-tos. Posts with it were not cited more often.**

**What we see**
- 27 of 96 slugs contain "2026". About 10 to 12 name an event or a dated data set, where the year belongs. The other 15 to 17 are freshness stamps, mostly on lists, guides and comparisons.
- 0 of 28 service pages and trade how-tos have a year in the slug. Titles can still say 2026 when the slug does not (two service pages, and [[BP-32 best togal ai alternatives|BP-32]]).
- Cited: 1 of 27 posts with a year against 7 of 69 without (p = 0.43). Among tested list-type posts it was 1 of 7 against 1 of 6. The sample is too small to show a gain or a loss.
- Quotr uses year stamps about as often as the rival addresses in the vault (27 of 96 against 9 of 45, p = 0.41). But rival years sit mainly on news items and a few flagship guides, not on evergreen posts ([[Competitor publishing benchmark]]).
- The 45 rival addresses are a small sample, not whole blogs.

**How sure:** Moderate (C-09, 2 of 3 points). The link with format is strong. The "no gain" result is weak evidence either way.

**What it means for Quotr**
- From 1 January 2027 the freshness-stamped addresses and titles will look out of date. Event and data posts should keep their year.

**What to do**
- Decide on each freshness-stamped post before January. Either update the title and keep the address, or redirect to an address without the year.
- Change the visible date only when the content really changes ([[C11 Decide on 2026 in blog web addresses and titles|C11]], [[Refresh plan Q4 2026#January 2027: the year in URLs and titles|Refresh plan, January 2027]], [[What went wrong#W-16 Date signals disagree, and years in evergreen URLs|W-16]]).
- Start with [[BP-81 best planswift alternatives 2026|BP-81]], which AI already cites.
- Retitle roadmap items due in 2027 that say "2026", starting with [[R-48 AI takeoff and estimating prices in 2026|R-48]] (February 2027).

### K-04 The blog is written for commercial buyers; finish trades are the clear gap

**Almost no post targets residential buyers, and finish and envelope trades have almost no posts.**

**What we see**
- Almost no post is written for a residential buyer. The few that touch residential work are [[BP-58 house flipping math 2026|BP-58]], two developer posts and an IBS (home builders' show) recap ([[What went wrong#W-08 Little content for residential and multifamily buyers|W-08]]).
- 5 slugs say "commercial"; none says "residential".
- Finish and envelope trades (cabinets, windows, framing, roofing, tile, insulation, siding, painting): 3 of 42 prompts have a post (7%). Electrical, HVAC, plumbing, concrete and drywall: 19 of 34 (56%). p = 0.000006.
- The trade gap holds even without the prompts the library already marks as needing a new page (2 of 16 against 18 of 25).
- The residential and cost-question gaps are mostly built into the library. Without the "new page" prompts, coverage is similar (residential 50% against 55%; cost and price 45% against 55%).

**How sure:** Strong for the finish-trade gap (C-18, 2 of 3 points). It does not yet show that filling it moves AI answers: tracked prompts with a post were absent 63% of the time, without one 73%.

**What it means for Quotr**
- Quotr has trade landing pages for framing, roofing, tile, insulation and painting, but almost no posts behind them. Framing shares one drywall how-to, and roofing has only a service sample ([[Website audit#8.3 Trade landing pages (23)|Website audit, trade pages]]).
- Whether residential is a target market is still open.

**What to do**
- Answer [[Q-26 Primary audience|Q-26]], then build the residential hub or drop the claim ([[B10 Residential hub; decide on the thin trade pages|B10]], [[What went wrong#W-08 Little content for residential and multifamily buyers|W-08]]).

### K-05 A matching post is a start, not a result

**Prompts with a matching post did a little better, but much of that gap is built into how the prompts were mapped. Most tracked prompts with a matching post still got no Quotr presence.**

**What we see**
- Of 25 tracked prompts with a Quotr blog post as the target, 17 (68%) had no Quotr presence. Only 2 (T16, T43) named Quotr.
- With a post, 8 of 25 had some presence; without one, 1 of 20 (p = 0.03). This is mostly by design: 13 of those 20 have no Quotr page at all. On the 32 core prompts the gap is small (5 of 19 against 1 of 13, p = 0.36).
- All 10 unbranded appearances were blog posts. The 7 prompts aimed at main-site pages got no main-site citation (small sample).
- [[What went wrong#W-04 AI uses Quotr's figures but drops the Quotr name|W-04]] counts 26 prompts, because it also counts T10. Its prompt points to /procurement/ and names [[BP-62 ddp construction materials|BP-62]] only as a second page.
- 71 of 96 posts (74%) match no tested unbranded prompt, so their effect is unknown. Only 1 of those 71 was cited ([[BP-85 commercial estimating services|BP-85]]).

**How sure:** Moderate (C-15, 2.5 of 3 points). The "68% absent" holds firmly. The with/without gap is partly built in.

**What it means for Quotr**
- 11 of the 17 misses are "best X software" or alternatives questions, where AI leans on third-party lists. Rewording alone is unlikely to help there.
- 6 are how-to questions, where an answer-first rewrite with numbers can win a citation, as [[BP-12 is ai takeoff actually accurate yet|BP-12]] (P5) and [[BP-56 how to estimate plumbing from drawings|BP-56]] (N2) did.

**What to do**
- Match every post to at least one buyer prompt, and test a rotating sample each month ([[Tracking set]]).
- A post that matches no prompt needs another reason to stay, such as news, an event or customer proof. Otherwise it is a merge candidate ([[Content refresh playbook]]).

### K-06 Most losses happen before the answer is written

**When Quotr had a matching post, the usual failure was that Perplexity never picked the page as a source.**

**What we see**
- In 27 unbranded tests with a matching Quotr post, a Quotr page reached the source list in 9 (33%): 2 retrieved only, 5 cited without the name (for S9 the name was not recorded), 2 named.
- Once in the list, the page was used in 7 of 9. That is a normal rate for Perplexity (our reading).
- By question type: broad category prompts 0 of 9; all others 9 of 18 (p = 0.012). Service, procurement and alternatives prompts: 7 of 8.
- For these tests, being findable does not look like the main gap. 6 of the 7 missed posts we could check (mostly lists) were recorded as found in web search. Only 2 of them were shown to rank for the prompt itself, and 2 are unconfirmed.
- Trade how-tos may differ: 8 of the 10 checked did not come back ([[Blog health audit#Health by cluster]]).

**How sure:** Moderate (C-36, 2 of 3 points). The index check is small (7 pages), uses a different search tool and leans to list posts.

**What it means for Quotr**
- For category prompts, rewriting the body of a page the engine never picks will not help much on its own.
- For mentions there is a second loss: 7 of the 9 picked pages still did not get Quotr named.

**What to do**
- Report the retrieval rate (KPI L2 part b) separately for prompts where Quotr has a post ([[KPIs and dashboard]]).

### K-07 Quotr was absent from every generic best-software answer

**Quotr appeared in none of the 22 "best X software" answers, but in 4 of 5 service and sourcing answers.**

**What we see**
- 51 unbranded runs: Quotr present in 0 of 22 generic software-category runs, against 10 of 29 others (p = 0.003).
- Quotr's best-of lists, software buyer's guides and Quotr-vs-X posts were never used for their own unbranded prompt (0 of 8, against 9 of 17 other tested posts). All 8 were generic software prompts, so we cannot tell the format from the question type.
- Service and sourcing questions (C10, C12, C14, S6, S9): Quotr was present in 4 of 5. S6 named Quotr, C12 and S9 cited a post, and C10 only retrieved one.
- A service-topic buyer's guide ([[BP-85 commercial estimating services|BP-85]]) was cited, so format alone is not the barrier.
- The lists come back in web search (9 of 9 checked). But AI used 9 lists, guides and head-to-heads, and 8 of them only for prompts that name Quotr.

**How sure:** Moderate (C-10, 2 of 3 points). The question-type result is strong. The format tests do not survive a correction for 8 tests.

**What it means for Quotr**
- New self-ranked "best X software" lists are unlikely to win category answers. They mainly feed answers when someone already names Quotr, so their facts must be right.

**What to do**
- Keep and fix the lists tied to tracked prompts ([[What went wrong#W-07 Best-of lists were not used for tested unbranded prompts|W-07]]). Aim for third-party lists instead ([[B2 Outreach to the best of lists AI cites (Tier A)|B2]]).
- Re-scope [[R-27 Construction procurement software in 2026|R-27]] and [[R-35 AI takeoff tools compared|R-35]], which target this question type (inference).

### K-08 Rival and alternatives answers lean on review directories

**Answers to "X alternatives" and "X vs Y" questions draw heavily on review sites such as G2 and Capterra, where we found no maintained Quotr listing.**

**What we see**
- In 9 unbranded rival and alternatives prompts, review directories took 35 of 150 source slots (23%). Category prompts: about 10%. How-to prompts: 0 of 126. Brand prompts: 6 of 138.
- The rival-against-category gap is borderline (p = 0.047 to 0.067). It is clearer for the 7 prompts that name a rival (29% of slots), but that split was chosen after seeing the data.
- quotr.ai got 3 of the 150 rival slots. Quotr was named in 1 of 9 rival answers (V1, about 15th of 17 brands).
- Quotr's only known review-site listing is a G2 profile under the old "quotr-io" name. It reportedly has 0 reviews (a Perplexity report; G2 blocks direct checks, so not verified). We found no Capterra, GetApp or Software Advice listing ([[Entity fact sheet]]).

**How sure:** Moderate (C-25, 2 of 3 points). One engine, one run per prompt. It is untested whether listings would get Quotr named.

**What it means for Quotr**
- 13 of 96 posts (14%) are comparisons or alternatives posts. They target the question type where directories matter most.

**What to do**
- Start the listing clean-up and review program before writing more comparison posts ([[A13 Directory and profile clean-up|A13]], [[A14 Launch the G2 review program|A14]], [[B11 Review program wave 2|B11]]).

### K-09 How-to answers name no brand, so Learn posts can win citations but rarely mentions

**On Perplexity, how-to answers named no company at all, while almost every Compare answer did.**

**What we see**
- 0 of 8 core how-to (Learn) answers named any brand, against 23 of 24 core Compare answers (p below 0.001). Without the Compare prompts that already name a rival: 16 of 17.
- Quotr's two Learn wins, P5 ([[BP-12 is ai takeoff actually accurate yet|BP-12]]) and N2 ([[BP-56 how to estimate plumbing from drawings|BP-56]]), were both cited but not named.
- 36 of 96 posts (38%) serve only Learn prompts.
- Mentions are rare in Compare answers too. Across all 36 unbranded Compare answers, core and extra, Quotr was named in 2.

**How sure:** Moderate (C-35, 2.5 of 3 points). Much of this is expected, because how-to questions do not ask for products. One engine, one day.

**What it means for Quotr**
- For how-to posts, a citation is the realistic win. Half of the 6-month "named" target (KPI L4) uses P5 and N2, which may be out of reach on Perplexity.

**What to do**
- Judge Learn posts on citations (KPI L2), not on mentions. Give P5 and N2 less weight in L4 ([[KPIs and dashboard]]).
- Check the pattern on ChatGPT and Google AI Mode in the October run before applying it to all engines ([[A15 Measurement setup and multi-engine baseline|A15]]).

### K-10 Rivals are named far more often than Quotr

**In 51 unbranded answers, Quotr was named twice. The leading rivals were named 14 to 17 times.**

**What we see**
- Quotr named in 2 of 51 (3.9%): V1, and S6, whose wording echoes Quotr's own. On the 32 core prompts it was named once (V1), as [[What went wrong#W-02 Almost no third-party proof|W-02]] reports.
- Buildxact was named 17 times, STACK 14, PlanSwift 14 and Togal 11.
- Leaving out prompts that name the rival itself, Buildxact and STACK stay clearly ahead after a correction for 8 comparisons. Buildxact was named without Quotr in 16 prompts, Quotr without Buildxact in 1; for STACK it was 12 against 1. PlanSwift, Togal and Bluebeam are ahead but do not pass the correction. Kreo, Beam AI and Handoff are not clearly different.
- Quotr's page appeared in 10 of the 51 answers: named in 2, used without the name in 5, retrieved only in 2, not recorded in 1.
- Quotr's rival posts cover Togal (3), STACK (2), PlanSwift (2), Beam (1) and Bluebeam (1). None targets Buildxact, the rival AI names most.

**How sure:** Strong for the gap (C-14, 2 of 3 points). Whether more posts would close it was not tested: only 25 of 96 posts match a tested prompt, and there is no before-and-after data.

**What it means for Quotr**
- The blog has built material that AI reads, not yet a name that AI repeats. This measure covers takeoff rivals only, not procurement rivals.

**What to do**
- Track named share against these rivals every month, with a separate procurement rival set ([[Tracking set]]). Third-party proof is the likely lever (inference): see [[What went wrong#W-02 Almost no third-party proof|W-02]].

### K-11 The service line, now most new posts, is barely tracked

**Service pages are most of Quotr's recent output, and 3 of the 8 posts AI cited are service pages, but only 2 tracked prompts measure them.**

**What we see**
- Service posts were 7 of 11 real-dated posts in August and 4 of 7 in September.
- Only 2 of 53 tracked prompts map to a service post: [[E-073 outsourced construction estimating service price per square foot for developers|E-073]] (T12) and [[E-074 how much does it cost to outsource a quantity takeoff|E-074]] (T44). Both were cited (C12, S9).
- Service prompts were cited 2 of 2; the 8 tracked best-of-list prompts 0 of 8 (p = 0.022). Against all other topics the service edge is not significant (p = 0.06), and both wins were narrow price questions.
- 10 of 12 service posts have no tested prompt, including 5 High-priority prompts (E-075, E-076, E-079, E-087, L-136).

**How sure:** Strong for the tracking gap (C-40, 2 of 3 points). Weak for "services win more": it rests on 2 tests.

**What it means for Quotr**
- The planned merges around 2026-10-08 ([[BP-79 construction estimating services|BP-79]] into [[BP-82 outsource construction estimating|BP-82]], [[BP-89 precon on demand outsource bid cost estimation|BP-89]] into [[BP-86 preconstruction services|BP-86]]) and the October rewrite [[R-05 Outsourced construction estimating|R-05]] land on prompts with no baseline.

**What to do**
- Before the redirects, give [[E-075 best construction estimating services in California|E-075]], [[E-076 MEP estimating services cost|E-076]], [[E-079 preconstruction estimating services for general contractors|E-079]], [[E-080 commercial construction estimating services cost|E-080]], [[L-018 should I hire an estimator or outsource estimating|L-018]] and [[L-019 how much does a full-time construction estimator cost compared to outsourcing|L-019]] two Perplexity runs each, then add them to the monthly set ([[A12 Merge duplicate pages|A12]]). E-080, L-018 and L-019 are the untested prompts behind R-05. E-087 and L-136 can follow in the November run.
- Keep the cited addresses: BP-82, [[BP-85 commercial estimating services|BP-85]] and [[BP-87 quantity takeoff services|BP-87]].

### K-12 The tracking set leans on Compare prompts, while most coverage is Learn

**The monthly number mostly watches Compare questions, but about half of the blog's coverage, and of the roadmap, is Learn questions.**

**What we see**
- Share of prompts tracked: Compare 31 of 88 (35%), Decide 8 of 48 (17%), Learn 14 of 146 (10%). p = 0.000007.
- Learn is 56 of the 106 covered prompts (53%) but only 14 of the 53 tracked prompts (26%). 78 of the 106 covered prompts have never been tested.
- The roadmap targets 162 prompts; 77 are Learn, and only 12 of those 77 are tracked.
- The data do not show which stage gets Quotr into answers more often (Compare 7 of 18, Learn 2 of 9, p = 0.67).

**How sure:** Strong (C-33, 2.5 of 3 points). It is a design fact: the set was built from the September test prompts, which leaned to Compare, probably on purpose.

**What it means for Quotr**
- The monthly score will barely register most of the planned how-to and cost content.

**What to do**
- Add a separate Learn panel of 10-15 covered or roadmap-targeted how-to prompts. Score it on whether a quotr.ai page is cited, not on mentions. Keep it apart from the core 40 score ([[Tracking set]], [[KPIs and dashboard]]).

### K-13 The prompt map cannot see duplicate posts

**The vault gives almost every buyer prompt to one post, so it cannot show two Quotr posts competing for the same search.**

**What we see**
- 96 of the 106 covered prompts map to exactly one post.
- Of 94 pairs of overlapping posts, only 10 (11%) share a prompt ID. None of the 10 pairs where one post came back in place of the other shares one.
- "106 of 282 prompts have a Quotr post" overstates coverage. Only 24 have a post confirmed in web search. 20 rest only on posts that did not come back, 60 only on posts never checked, and 2 on a mix of the two. So the number of covered prompts with a post confirmed in web search is somewhere from 24 to 86.
- 18 of those 20 prompts are still marked "existing page fits", and 16 have no roadmap item.

**How sure:** Strong for the mapping fact (C-24, 3 of 3 points). The 20 could move either way. It may rise once the 60 unchecked posts are checked. It may fall: the 15 "not found" results were not re-confirmed, 3 of the 20 prompts belong to September posts that may be too new to show up, and 6 rest on two posts ([[BP-39 quotr ai vs beam ai takeoff estimating comparison|BP-39]] and [[BP-57 bluebeam alternative|BP-57]]) that Perplexity still retrieves for brand prompts. Missing from one search tool is not proof of being missing from Google.

**What it means for Quotr**
- A "one prompt, one main page" check by prompt ID would miss most duplicates ([[What went wrong#W-11 About 12 posts duplicate another Quotr page|W-11]]).

**What to do**
- Before briefing a new post, search its main question for an existing Quotr page, not only its prompt ID ([[Content refresh playbook#7. Do not publish near-duplicate pages]]).
- Re-check the 20 prompts once web search or Search Console is available ([[Q-59 Web search checks for 60 unchecked posts|Q-59]], [[A17 First Search Console audit of the 96 blog posts|A17]]).

---

## Leads that did not pass

> [!caution] These are not findings
> Each lead below lost its numbers in review or scored below 2 of 3 points. Some are partly true but already known, some rest on 3 to 9 tests, and some fall apart once another explanation is allowed for. Do not quote them to Quotr as results. Re-test them when the trigger in the last column happens.

| Lead | Why it did not pass | Worth re-testing when |
|---|---|---|
| **C-04** Near-duplicate posts are made in the same burst, and AI pulls them together | Overlapping posts are typically 20 days apart, which mostly reflects topic campaigns. AI used both posts together mainly in brand prompts. | Quotr's team adds more trade-by-trade service posts, or after the [[A12 Merge duplicate pages\|A12]] merges |
| **C-05** The retired price sits on almost every list and alternatives post | Only posts with a price block can show a price, and only some posts were checked. Firm evidence (the live page or a search engine's stored copy) covers 10 of the 22. 3 more rest on AI answers only ([[What went wrong#W-01 Old prices still showing after the September price change\|W-01]]). | All 22 list and alternatives posts and 8 head-to-heads have been read on the live page ([[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere\|A2]], [[Q-59 Web search checks for 60 unchecked posts\|Q-59]]) |
| **C-06** Brand answers about Quotr are built from old-price posts | Brand prompts pull comparison posts by design. Only 2 of 8 brand answers repeated the old price, and one also cited outside pages with the same figure. | After A2: re-run B2, B4, V2 and B7 as an early before-and-after measure |
| **C-12** New service posts are cited within 31-49 days | The "August" effect is the service topic, from 3 prompts. No post younger than 31 days was tested. | The October run includes an extra set for the 9 posts published after 25 August |
| **C-13** AI takes Quotr's numbers but not its name, unlike rivals | Naming depends on question type: how-to answers name no one, rivals included. Quotr's side rests on 6 tests (p about 0.07). | After [[A8 Put the Quotr name inside key facts on the pages AI already reads\|A8]]: re-run C12 and S9 on [[BP-82 outsource construction estimating\|BP-82]], [[BP-85 commercial estimating services\|BP-85]] and [[BP-87 quantity takeoff services\|BP-87]] |
| **C-39** Questions that ask for a number were always cited (3 of 3) | Only 3 tests, labelled after the results were known. 2 of the 3 are the same service posts as K-11. p = 0.086 after correction. | Cost and accuracy pages such as [[R-41 2026 AI Takeoff Accuracy Benchmark\|R-41]] and [[R-52 Quotr Service by the numbers\|R-52]] are live and tested |
| **C-41** Buyers say "takeoff software", Quotr's lists say "estimating software" | True for slugs (22 of 23 list and alternatives slugs leave out "takeoff"), but no link to AI results. Most titles are unknown. | A cheap trial: add "takeoff" next to "estimating" in the titles of [[BP-55 best drywall estimating software in 2026\|BP-55]] and [[BP-48 best flooring estimating software in 2026\|BP-48]] (T04, T05), then compare in the next run |
| **C-37** Quotr's rival pages carry unsourced or conflicting rival facts, and AI uses them | Accurate, but already in [[What went wrong#W-13 Statistics and competitor facts went out without sources\|W-13]] and task [[A6 Editorial sweep\|A6]]. Only S3 and V3 show AI taking rival facts from Quotr posts, and no wrong fact was repeated. | After A6 on [[BP-32 best togal ai alternatives\|BP-32]], [[BP-81 best planswift alternatives 2026\|BP-81]], [[BP-43 best togal ai alternatives 2026\|BP-43]] and [[BP-51 stack alternative\|BP-51]]: re-run V1, V3 and S3 |
| **C-28** Decide-stage questions are the blog's blind spot | By design: 30 of 35 uncovered Decide prompts belong to main-site pages. The real gap is proof: only 2 of 96 posts are customer stories. | After the disambiguation rewrite ([[R-01 Rewrite disambiguation as a plain Quotr.ai company facts page\|R-01]]) and proof pages ([[B4 Proof pages - case studies with numbers\|B4]]) |
| **C-43** Tracked prompts that are near-copies waste slots | Similar prompts agree mainly because all category prompts are absent. Allowing for question type, the effect is not significant (p = 0.074). | Category prompts start to show Quotr, so wordings can differ |
| **C-11** Alternatives posts miss the rivals AI names most | The "exact match" effect rests on 5 prompts, and Quotr was named in only 1. "Most named" fits only Buildxact, and the test set leans residential. | "Buildxact alternatives" and "Kreo alternatives" are added to the test set, before building [[R-25 Quotr.ai vs Handoff for residential builders\|R-25]] or [[R-36 Quotr.ai vs Buildxact\|R-36]] |
| **C-16** July's procurement posts have not reached buyer-worded questions | 0 of 9 is not worse than Quotr's other unbranded prompts (p = 0.32). 4 of the 9 answers named no vendor at all. | The procurement posts have been checked in web search (none has been checked yet), and the [[B8 Procurement and tariff decision guides\|B8]] guides are live |
| **C-29** Main-site pages (product, pricing, glossary, trade) never surface for unbranded prompts | All 10 Quotr pages that surfaced were blog posts, and 0 of 8 tests aimed at a main-site page. But those were hard category prompts (p = 0.15). | /pricing/ and 2-3 glossary pages have been tested, starting with the "cheapest" and "free trial" prompts (V7, V8) |
| **C-38** Rivals' own best-of lists win the category prompts that Quotr's lists lose | Quotr's own self-ranked alternatives lists were cited (3 of 5), so list format and self-ranking alone are not the blocker. Lists lose on crowded category prompts (n = 8). | The lists are fixed as [[What went wrong#W-07 Best-of lists were not used for tested unbranded prompts\|W-07]] says; then re-run C1, C4 to C6, C11 and N3 |
| **C-08** Sitemap dates do not move when a post is edited | Only 3 posts show a later "Last updated" date than the sitemap. 80 posts have no date check. Already covered by task [[A9 Sitemaps and lastmod dates\|A9]]. | The first A2 price fixes are live: check that a fixed post's sitemap date changed |
| **C-07** New service posts add conflicting fact claims | Most fact fixes are the retired price; without it the gap is not significant (p = 0.12). The newest posts were also checked more closely. | Before the next service post: answer [[Q-15 Turnaround\|Q-15]] and run the check in [[A16 Add a human edit and fact-check step for AI-assisted drafts\|A16]] |

---

## What we ruled out

- **C-19 The first wave (April to early May) does not show up in web search.** The gap came from how the checks were done. Compared like for like, it is not significant (0 of 5 against 8 of 18, p = 0.12). A first-wave post, [[BP-12 is ai takeoff actually accurate yet|BP-12]], was cited.
- **C-26 AI picks the Quotr figures that Quotr states in conflicting ways.** The posts AI used were simply the most researched, so more conflicts were found on them. At equal research depth there is no gap.
- **C-30 Trade coverage is lists; the trade how-tos are missing.** On real how-to questions the gap is not significant (50% against 36%). In the trades Quotr writes about, 73% of how-tos are covered. The uncovered ones are cost and compliance questions.
- **C-45 Each campaign sold a different Quotr, and AI copies the label.** The question drives the label as much as the page does. The brand comparison answers gave one joined-up description.
- **C-17 Short slugs got retrieved; long ones did not.** The result needs choices made after looking, and is not significant across all tested posts (p = 0.057). Since July only 4 of 35 new posts have long slugs anyway.
- **C-23 Posts with many sibling pages are the ones missing from web search.** The link was circular: the overlap lists were written during the same searches. With the check method held equal, there is no link (p = 0.18). The cases themselves stay in [[What went wrong#W-10 Some posts did not come back in web search|W-10]].
- **C-42 Long, specific buyer questions go uncovered.** 51 of the 57 long uncovered prompts belong to gaps we already know (residential, trade, developer, cost). Length did not predict an AI result (p = 0.29).
- **C-44 Tariff questions are well covered but answered from government and media.** "Well covered" depended on hand-picked prompts (tariff prompts alone: 3 of 6). The solid part is already in [[GEO tactics already used]].
- **C-22 Event recaps came early and left no trace.** The bunching depends on the chosen window. No event question was tested, so no recap could be cited.
- **C-20 Quotr publishes almost only on its blog.** The comparison is lopsided. The blog is fully listed, but the LinkedIn, X and other channel histories were never pulled, and 15 of the 20 off-blog items found have no date ([[Publishing beyond the blog]]).
- **C-21 Milestones stay off the newswire, while rivals use it.** We found no release for the seed round or the rename, but task [[B1 Seed-round announcement|B1]] already plans one. We also only see rival milestones that were published.
- **C-27 Quotr compares only itself, so rival-vs-rival questions go to rivals.** Only 3 prompts were tested, one run each. Such questions are 6 of 282 library prompts. The neutral comparison [[R-35 AI takeoff tools compared|R-35]] already covers them.
- **C-31 AI-takeoff questions are saturated.** The group is well covered (14 of 17 prompts have a post), but only 4 were tested. That is too few to show saturation, and the roadmap already handles the group.
- **C-32 Coverage does not follow priority.** Priority ratings were set after the posts were written, so coverage not tracking priority is expected.
- **C-34 General contractors are the best-served buyer.** GC prompts do have more posts (58% against 33%), partly because trade questions carry no GC tag. The tests are too few to show whether it pays off (2 of 7).

---

## How we tested

1. **Proposing.** Proposers suggested candidate patterns over three rounds, 45 in all. Each came with its numbers and, where possible, a statistical test.
2. **Three skeptics per candidate.** Each candidate went to three separate reviewers:
   - **Numbers:** recomputed every figure and test from the data.
   - **Other explanations:** looked for anything else that could produce the same pattern (how the data were collected, topic mix, prompt type, dates).
   - **Usefulness:** asked whether it is new and would change a decision.
3. **Scoring.** Each reviewer gave 1 point (holds), half a point (weak) or 0 (refuted). To survive, a pattern had to keep its numbers under the numbers review and score at least 2 of 3.
4. **Result.** 13 survived and 32 did not. 31 of the 32 are listed under [[#Leads that did not pass]] and [[#What we ruled out]]; C-03 is under [[#Weekdays and same-day batches]]. Where a reviewer said the first wording went too far, this page uses the reviewer's softer wording and recomputed numbers.
5. **Citation count correction.** The first two rounds ran on an older version of the post data. A later check of the test notes showed that 8 posts were cited; 2 more were only retrieved, and 2 appear in test notes but were not cited. The reviewers used the 8-post count, and every citation figure on this page was re-checked against the corrected data.

---

## Related pages

- [[Blog health audit#Patterns and mistakes behind this|Blog health audit]]: the hub for the 96 posts; its patterns section links back here.
- [[What went wrong]]: the 19 problems (W-01 to W-19) that several patterns here explain.
- [[Refresh plan Q4 2026]]: the week-by-week fixes, merges and the January 2027 year decision.
- [[Content refresh playbook]]: how to score, fix, merge and re-test a post.
- [[Tracking set]]: the 53 monthly prompts; K-11 and K-12 suggest additions.
- [[Prompt library]]: the 282 buyer questions behind every coverage figure.
- [[AI visibility baseline]]: the 2026-09-25 Perplexity results used throughout.
- [[Competitor publishing benchmark]]: what rivals publish; no usable rival publishing pace yet.
- [[Publishing beyond the blog]]: Quotr's channels other than the blog.
- [[Google search updates 2025-2026]]: why merges and redirects wait until the spam update ends.
- [[Retainer scope and value case]]: the scope that has to fit Quotr's current pace (K-01).
- [[GEO writing style guide]]: the rules for answer-first pages and putting "Quotr.ai" inside the fact.
- Open questions: [[Q-52 Real publish dates of six posts|Q-52]] (reset dates), [[Q-53 Blog schedule and AI tools|Q-53]] (schedule and pace), [[Q-59 Web search checks for 60 unchecked posts|Q-59]] (unchecked posts).
