---
type: playbook
description: 'How to audit the 96 Quotr blog posts in Google Search Console (plus Bing AI Performance), step by step, and record the results in the article notes.'
last_verified: 2026-09-26
verify_every_days: 90
aliases:
- GSC audit
---
# Search Console audit playbook

> [!abstract] What this page is for
> A click-by-click guide to checking Quotr's blog in Google Search Console (GSC: Google's free dashboard for site owners), with a companion check in Bing Webmaster Tools. It tells you what access to ask for, what "good" looks like in each report, and exactly where to write each result in the brain. No Quotr Search Console data has been seen yet, so this audit is how we find out how each post is really doing in Google.

> [!info]- Sources
> - **Vault notes:** [[Tracking setup]] (sections 3-5: properties, sitemaps, the Generative AI report, the opt-out setting, branded search, re-crawl requests, Bing, Cloudflare), [[KPIs and dashboard]] (KPIs L2 and G3, the monthly dashboard), [[Content refresh playbook]] (the health rubric, flags and the after-refresh routine), [[Website audit]] (robots.txt and sitemaps), and the open questions [[Q-32 quotr.io|Q-32]], [[Q-34 Cloudflare|Q-34]] and [[Q-40 Access and history|Q-40]]. The article note template and the vault rules (CLAUDE.md) for the article properties and the Log.
> - **Data files (2026-09-26):** our research briefing on Google changes (its 13 Search Console audit steps, implications, watch list and caveats); the Google claims register (the claim IDs on this page, such as GSC-12); the per-post dataset and article IDs (post dates, which posts web searches did not return, and which were flagged as cited by AI); the overlap map of posts that answer the same buyer question.
> - **How sure we are:** see the box under "The short version".

---

## The short version

- **This audit turns Google's own data into facts about each post.** Nobody on our side has seen Quotr's Search Console yet. Until we do, how each post does in Google is unknown.
- **Step one is access.** Ask Quotr for Search Console, Bing Webmaster Tools, GA4 (Google Analytics) and read-only Cloudflare.
- **On day one, check two things.** The "Search generative AI" setting must be **off**. If it is on, Quotr gets no impressions or traffic from AI Overviews and AI Mode, Google's AI answers (GSC-15, INDEX-14). Manual actions should say "No issues detected".
- **Indexing is the first check for every post.** Google says a page only needs to be indexed (stored by Google so it can be shown) and allowed to show a snippet to appear in its AI answers (INDEX-05). Start with the 15 posts that targeted web searches did not return. That tool is not Google, so this is a lead, not proof.
- **A Google spam update is rolling out now.** It began on 2026-09-24 and may run to about 2026-10-08 (RANK-21). Save 2026-09-17 to 09-23 as the baseline week. Hold merges and bulk changes until it ends (our inference, not a Google rule).
- **Old numbers need care.** Impressions were over-counted until 2026-04-27 (GSC-12). Only compare periods that start on or after 2026-04-28.
- **Write every result into the article notes:** a few properties, a "Search Console" table and a dated Log line. The Articles tables then update by themselves.

> [!warning] How sure we are
> - **GSC and RANK claims** were found by live web search on 2026-09-26. They were **not** independently re-checked, because the search limit ran out.
> - **INDEX, AI, QUALITY and OTHER claims** were carried over from the 2026-09-25 research. They were fact-checked then only where the vault says so (for example, [[Tracking setup]] cites the fact-check for the Generative AI report and for Bing AI Performance).
> - Some items rest on industry press or vendor blogs only, with no Google source: the num=100 change, AI Mode inside the Web totals, the branded filter's March 2026 date, both Page indexing report freezes, the August 2026 spam update dates and its ranking data, the early-August 2026 volatility, and the AI Overview "position" point.
> - Every claim ID (for example RANK-13) can be traced in the Google claims register (google_claims.json). Re-check a claim against its source before it goes into a client deck.
> - The rules of thumb on this page ("lost more than half its clicks", "two months in a row", the comparison windows) are **our suggestions**, not Google thresholds.
> - Menu names follow the sources. The live Search Console labels may differ slightly.

---

## Before you start

### Access to ask Quotr for

| Tool | What to ask for | Why we need it |
|---|---|---|
| **Google Search Console** | Owner or Full user on the **Domain property** for quotr.ai (a property verified by DNS, a setting in the domain's records, that covers every quotr.ai address). Also the **quotr.io** property, if one exists. | Every step below reads it. The branded-queries filter does not work on sub-properties such as /blog/ (GSC-07). quotr.io is the old domain; [[Tracking setup]] suggests a property there to watch what is still indexed. |
| **Bing Webmaster Tools** | Access to the quotr.ai site | Its AI Performance report shows how often Copilot and Bing AI answers cite each Quotr page, and the "grounding queries" behind them (OTHER-01, OTHER-02). It gives free AI citation data, which Google does not: Google shows impressions only ([[Tracking setup]]). |
| **Google Analytics 4 (GA4)** | Read access | AI referral visits (KPI G1) and demo or trial events (KPI G2). Clicks from Google AI Overviews and AI Mode look like normal Google clicks in GA4, so we need Search Console alongside it ([[Tracking setup]], section 1). |
| **Cloudflare** (the service in front of quotr.ai that can block bots) | Read-only access for quotr.ai: AI Crawl Control, the bot settings, and server logs if any are kept | To check that AI crawlers (the bots AI tools send to read pages) get normal pages, not blocks. Since 2025-07-01, Cloudflare blocks AI crawlers by default for new domains (OTHER-07). The vault's crawl audit found the hidden link of AI Labyrinth, a Cloudflare bot trap, on every quotr.ai page it checked (OTHER-09). See task [[A11 Confirm Cloudflare lets AI search bots in\|A11]] and [[Tracking setup#5.2 Step by step in Cloudflare (whoever owns the Cloudflare account)]]. |

**Where these questions live**
- Access to GA4, Search Console, Bing and forms: [[Q-40 Access and history|Q-40]].
- Cloudflare settings: [[Q-34 Cloudflare|Q-34]].
- quotr.io and who controls it: [[Q-32 quotr.io|Q-32]].
- New questions from this playbook (for example: which property type Quotr uses, and who can change the "Search generative AI" setting) will be in [[Open questions.base|the open questions]].

### Ground rules

- **Look, don't change.** The audit only reads reports. The only changes are chart notes, submitting the blog sitemap if it is missing, and "Request indexing" after a fix.
- **Never touch the "Search generative AI" setting.** Read it, record it, and tell Quotr if it is on.
- **Hold big changes while a Google update rolls out.** Until the September 2026 spam update is complete, hold merges, redirects, retitles, re-dating and batch publishing. Single-page fact fixes (task [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]]) can go ahead with a chart note. (Our inference: this keeps cause and effect readable. It is not a Google rule.)
- **Only compare periods from 2026-04-28 onward** (GSC-12).
- **Save every export** (a CSV file or Google Sheet) with the report name and date in its file name.

### Credit where it is due

- robots.txt (the file that tells bots what they may read) lets every bot in. That includes Google-Extended, the setting that controls use of content for Gemini training. Leave it as it is ([[Website audit]]).
- The blog has its own sitemap (the list of pages a site gives to search engines). It lists all 96 posts plus 8 hub pages.
- Perplexity already reads Quotr's pages. In the September 2026 tests, quotr.ai was in its source list for 6 of 32 buyer questions ([[KPIs and dashboard]]).
- We do not know whether Quotr's team already checks Search Console. Ask first: they may have history and context we can use.

---

## The audit, step by step

Steps 1-13 use the same numbers as our research briefing behind [[Google search updates 2025-2026]], so "audit step 5" means the same thing on every page. Step 14 (Bing) is our addition.

| Step | Report | When (first audit) | Writes to article notes? |
|---|---|---|---|
| 1 | Property and users | Day 1 | No |
| 2 | "Search generative AI" setting | Day 1 | Only if it was ever on |
| 3 | Manual actions | Day 1 | Only if a post is named |
| 4 | Chart notes (annotations) | Day 1, then after every change | Log line per change |
| 5 | September 2026 spam update, before and after | Save the baseline now; compare after it ends | Yes |
| 6 | Sitemaps and Page indexing | First week | Yes |
| 7 | URL Inspection, post by post | First week onward | Yes |
| 8 | Weekly trends per post | First week, then monthly | Yes |
| 9 | Past Google updates | First two weeks | Yes |
| 10 | Generative AI report | First week, then monthly | Yes |
| 11 | Branded and non-branded clicks | First week, then monthly | Yes |
| 12 | Posts that compete for the same searches | After step 8; merges wait for the update to end | Yes |
| 13 | After every refresh or merge | Every change | Yes |
| 14 | Bing AI Performance (companion) | First week, then monthly | Yes |

Words used below:
- **Impressions:** how many times a page was shown in results.
- **Clicks:** how many times someone clicked through to it.
- **CTR (click-through rate):** clicks divided by impressions.
- **Average position:** the page's average place in the results.
- **Canonical:** the main version Google picks when pages look alike.

### Step 1. Check the property and who has access

- **Where:** the property drop-down, then **Settings** (the users list).
- **How:**
  1. Ask Quotr to add you as a user.
  2. In the property drop-down, check there is a **Domain property** for quotr.ai, verified by DNS. A URL-prefix property alone (one web address, such as the /blog/ folder) is not enough.
  3. Note the owner and everyone else who has access.
  4. Check whether a quotr.io property exists ([[Tracking setup#3.1 Properties and sitemaps (one-off)]]).
- **Good looks like:** a verified Domain property for quotr.ai that you can read. This matters because the branded-queries filter does not work on sub-properties such as /blog/ (GSC-07, GSC-08).
- **Record:** not in article notes. Write the property type, owner and access date in [[Tracking setup#3.1 Properties and sitemaps (one-off)]]. When Quotr answers the access question ([[Q-40 Access and history|Q-40]]), fill it in (vault rule 8). Add a [[Changelog]] line.

### Step 2. Check the "Search generative AI" setting

- **Where:** the property-level "Search generative AI" control. Google's help page explains it: [Search Console Help](https://support.google.com/webmasters/answer/16908024?hl=en).
- **How:** open it and read its state. **Change nothing.** If it is on, find out when it was switched on, and by whom.
- **Good looks like:** **off.** When it is on, the site gets no impressions or traffic from AI Overviews, AI Mode or Discover's AI features. Google says the setting is not a ranking signal for normal Search, and it is separate from Google-Extended (GSC-15, INDEX-11, INDEX-14, AI-11).
- **Record:** the state and date in [[KPIs and dashboard]] (KPI L2 d) and [[Tracking setup#3.3 Do NOT opt out]]. Confirming it is off is part of task [[A11 Confirm Cloudflare lets AI search bots in|A11]]. If it was ever on, add those dates to every article note's Search Console section. They explain zero AI impressions for that period.

### Step 3. Manual actions

- **Where:** **Security & Manual actions → Manual actions**. (A manual action is a penalty that Google staff apply by hand.)
- **How:** open the report once. If an action is listed, pause the audit. Read which pages and which policy it names.
- **Good looks like:** "No issues detected".
- **Record:** the result and date in [[Website audit]]. If an action names blog posts, add the flag `manual action (GSC)` to each one, plus a Log line. After the August 2025 spam update, Google's advice to affected sites was to review its spam policies (RANK-05). Our reading (inference): a site recovers by fixing the policy problem, not by waiting.

### Step 4. Add chart notes (annotations)

- **Where:** **Performance → Search results**. Right-click the chart to add a note. Each note holds up to 120 characters, and a property can hold 200 (GSC-06).
- **How:** add these notes now. From then on, add one for every Quotr batch-publish day, refresh and merge.

| Date | Note to paste | Claim |
|---|---|---|
| 2026-04-27 | Impression over-count fixed. Compare only from 2026-04-28. | GSC-12 |
| 2026-05-21 | May 2026 core update starts | RANK-13 |
| 2026-06-02 | May 2026 core update ends | RANK-13 |
| 2026-06-24 | June 2026 spam update (to 06-26) | RANK-17 |
| 2026-08-13 | Gen AI and Discover logging error starts; data reportedly restored about 08-21 | GSC-19 |
| 2026-08-18 | August 2026 spam update (to 08-21) | RANK-18 |
| 2026-09-14 | New pricing post published (BP-93) | Quotr blog ([[BP-93 new pricing\|BP-93]]) |
| 2026-09-24 | September 2026 spam update starts; multimodal filter added | RANK-21, GSC-20 |
| The day it ends | September 2026 spam update ends | RANK-21 |

- **Good looks like:** every event that can move the numbers is on the chart. Then nobody reads a Google change or a bug as a content effect.
- **Record:** notes are deleted after 500 days, and they do not show in comparison mode (GSC-06). So keep a permanent copy:
  - The table above is the permanent list of past events.
  - For each refresh, merge or re-date, add a Log line in the article note.
  - Add site-wide events to the "Changes this month that could affect numbers" line of the [[KPIs and dashboard#6. One-page monthly dashboard (template)|monthly dashboard]].

### Step 5. Save the spam update baseline, then compare

- **Where:** **Performance → Search results** (Web), **Pages** tab.
- **How:**
  1. Add a Page filter: URLs containing `/blog/`.
  2. Set the dates to **2026-09-17 to 2026-09-23** (Thursday to Wednesday). Export clicks, impressions, CTR and average position per post. This is the baseline week.
  3. Watch the [Google Search Status Dashboard](https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history) (Google's public list of updates). Google said the update may take up to two weeks, so it could run to about 2026-10-08 (RANK-21).
  4. When it shows the update complete, export the first full Thursday-to-Wednesday week after the end. Compare each post with its baseline.
- **Good looks like:** no post drops out of the results or loses most of its impressions. Our rule of thumb: look into any post that loses more than half its clicks or impressions.
- **Watch first (inference):** the 12 estimating-services posts, 11 of them published in August-September 2026: BP-25, BP-79, BP-82, BP-84 to BP-87, BP-89, BP-91, BP-94 to BP-96.
- **Context:** 95 of the 96 posts were live when this update began. [[BP-96 quotr service estimates|BP-96]] is dated the same day. The August 2026 spam update was short but sharp. SE Ranking data, reported by Search Engine Land, showed 16.71% of top-10 addresses fell beyond position 100, against 9.2% in a quiet five-day period in July (RANK-19).
- **Record:** a dated row in the post's Search Console table. Where the rule of thumb is met, add the flag `dropped after update (GSC)` and a Log line. If a post or cluster drops sharply, check it against Google's spam policies, especially scaled content abuse (making many pages without added value; QUALITY-01, QUALITY-02).

### Step 6. Sitemaps and Page indexing

- **Where:** **Indexing → Sitemaps**, then **Indexing → Pages** (the Page indexing report).
- **How:**
  1. Check that `https://quotr.ai/blog/sitemap.xml` is submitted. Submit it if not. (Listing it in robots.txt is task [[A9 Sitemaps and lastmod dates|A9]].)
  2. In Page indexing, first read the report's "last updated" date. The report froze twice in the past year (GSC-11, GSC-17).
  3. Filter to the blog sitemap. Export the not-indexed addresses with their reasons.
- **Good looks like:**
  - The blog sitemap is read without errors and lists 104 addresses (8 hub pages plus 96 posts).
  - All 96 posts are indexed.
  - No post is excluded by noindex (a tag that tells Google not to store the page).
  - Google has not picked a different canonical, except where Quotr intends it.
- **Why it matters:** a post that is not indexed cannot be cited in AI Overviews or AI Mode, however good it is (INDEX-05, AI-05, QUALITY-07).
- **Record:** in each article note: the indexing state, the reason if not indexed, and the check date. Update `web_indexed` and `search_check` (see "Record the results in the brain" below). Add the flag `not indexed (GSC)` where it applies.

### Step 7. URL Inspection, one post at a time

- **Where:** **URL Inspection**. Paste the post's web address.
- **Order:**

| Order | Posts | Why this order |
|---|---|---|
| 1 | The 15 posts that targeted web searches did not return on 2026-09-26: [[BP-04 how to price construction job\|BP-04]], [[BP-05 construction takeoff guide\|BP-05]], [[BP-06 quotr vs traditional estimating\|BP-06]], [[BP-10 construction estimating mistakes to avoid\|BP-10]], [[BP-11 how ai construction estimating works\|BP-11]], [[BP-13 blueprint to priced estimate workflow\|BP-13]], [[BP-26 quotr vs excel\|BP-26]], [[BP-39 quotr ai vs beam ai takeoff estimating comparison\|BP-39]], [[BP-44 flooring trades how to quote flooring jobs and win more work\|BP-44]], [[BP-45 what is ai construction estimating software\|BP-45]], [[BP-53 how subcontractors bid gcs without giving away margin\|BP-53]], [[BP-57 bluebeam alternative\|BP-57]], [[BP-74 metric imperial construction takeoff\|BP-74]], [[BP-90 outsourcing vs hiring an estimator\|BP-90]], [[BP-92 scope gap construction\|BP-92]] | The web search tool is not Google, so this is only a lead, not proof |
| 2 | The 18 posts from [[BP-40 commercial signage takeoff sign schedule bid package\|BP-40]] to [[BP-57 bluebeam alternative\|BP-57]] | Published 2026-06-11 to 07-03, while the Page indexing report was frozen (GSC-17) |
| 3 | The 12 posts flagged as cited by AI: [[BP-12 is ai takeoff actually accurate yet\|BP-12]], [[BP-17 how to do construction takeoff pdf blueprint\|BP-17]], [[BP-32 best togal ai alternatives\|BP-32]], [[BP-51 stack alternative\|BP-51]], [[BP-56 how to estimate plumbing from drawings\|BP-56]], [[BP-57 bluebeam alternative\|BP-57]], [[BP-59 how developers source building materials\|BP-59]], [[BP-62 ddp construction materials\|BP-62]], [[BP-81 best planswift alternatives 2026\|BP-81]], [[BP-82 outsource construction estimating\|BP-82]], [[BP-85 commercial estimating services\|BP-85]], [[BP-87 quantity takeoff services\|BP-87]] | The most valuable posts to protect. (A later check found 8 of the 12 were really used in an answer; see [[Content refresh playbook]].) |
| 4 | All the other posts | So every post has Google's own answer |

- **How:** for each post, note three things:
  1. Is the post on Google?
  2. Which canonical did Google select?
  3. When was it last crawled (read by Google's bot)?

  Then run the **live test**. Confirm the page has no noindex and no nosnippet (a tag that stops Google showing a text preview).
- **Good looks like:** the post is on Google, Google's canonical is the post itself, it was crawled after its last real edit, and snippets are allowed.
- **Record:** in the article note, a line like "URL Inspection (date): on Google yes/no; Google canonical; last crawl". For posts that overlap, note which address Google picked. This feeds `merge_into` (step 12).

The live list below shows every post whose `web_indexed` is `no`. It changes as you record Google's answers.

![[Articles.base#Not found in web search]]

### Step 8. Weekly trends per post

- **Where:** **Performance → Search results**. Set the chart to **Weekly** (the drop-down starts on Daily; GSC-10). For a quick weekly look, use the **Insights** report, which shows rising and falling pages (GSC-03).
- **How:**
  1. Use only dates from 2026-04-28 onward.
  2. Export clicks, impressions, CTR and position per post for the last three months.
  3. Each week, glance at Insights for rising and falling pages.
  4. The experimental AI-powered configuration can set filters from a plain-language request. Always check the filters it picks. It cannot export (GSC-09).
- **Good looks like:** a clean weekly series for each post, no comparison that crosses 2026-04-27, and a short list of declining posts.
- **Record:** one row per month in each article note: clicks, impressions, CTR, average position. Add the flag `declining (GSC)` when clicks fall two months in a row (our suggested rule).

### Step 9. Past Google updates

- **Where:** **Performance → Search results → Date → Compare**.
- **How:** compare windows of equal length that start on the same weekday and sit outside the rollout. The windows below are our choice, not Google's. Group the results by cluster.

| Update | Before | After | Posts live at the start | Claim |
|---|---|---|---|---|
| May 2026 core update (2026-05-21 to 06-02) | 2026-05-07 to 05-20 | 2026-06-04 to 06-17 | BP-01 to BP-21 | RANK-13 |
| June 2026 spam update (2026-06-24 to 06-26) | 2026-06-17 to 06-23 | 2026-07-01 to 07-07 | BP-01 to BP-49 | RANK-17 |
| August 2026 spam update (2026-08-18 to 08-21) | 2026-08-11 to 08-17 | 2026-08-25 to 08-31 | BP-01 to BP-84 | RANK-18 |

- **Too new to judge (inference):** posts under about four weeks old are still ramping up. Mark them "too new to judge".
- **Don't blame 2026-08-01 to 08-06 on an update.** There was volatility then, but Google confirmed no update (RANK-20).
- **Context:** only 21 of the 96 posts were live when the May 2026 core update began. Most of the blog has never been through a core update.
- **Post dates are approximate.** They come from the blog sitemap. Six posts (BP-66, BP-70 to BP-73 and BP-75) have reset dates, so their real publish dates are unknown. The "posts live" lists could shift by a few posts.
- **Good looks like:** no cluster shows a consistent drop after an update, especially the list, comparison and service clusters.
- **Record:** one line per update in each article note, for example: "May 2026 core: clicks A to B, impressions A to B; gain / loss / flat / too new". Add the flag `dropped after update (GSC)` where it applies.

### Step 10. The Generative AI report

- **Where:** **Performance → Generative AI** (Search) ([Search Console Help](https://support.google.com/webmasters/answer/16984139?hl=en)).
- **How:**
  1. Set the dates from **2026-05-18**, the first day with data (GSC-14).
  2. Export AI impressions per page, by month. Check the country (US) and the device.
  3. Do not add these numbers to the Web totals. They are already inside them (INDEX-13, AI-10).
  4. Ignore "position" here. An AI Overview gets one position for the whole block (INDEX-15, single source).
  5. If 2026-08-13 to 08-17 still looks low, mark it as the logging error (GSC-19).
  6. Note the new multimodal filter from 2026-09-24 (GSC-20).
- **Good looks like:** a list of posts with AI impressions, ideally including the comparison, list and cost posts. The numbers move in the same direction as the monthly AI test runs ([[Tracking set]]).
- **Limits:** impressions only, with no clicks, CTR or queries (GSC-14). Whether quotr.ai has enough volume to show data at all is unknown. [[BP-01 vanderbilt classroom|BP-01]] to [[BP-17 how to do construction takeoff pdf blueprint|BP-17]] went live before 2026-05-18, so their first weeks have no AI data.
- **Record:** in each article note, the monthly "AI impressions" in the Search Console table, and the flag `AI impressions (GSC)`. Compare with `ai_cited` and `cited_in`, which hold the September test results. Send the site total to [[KPIs and dashboard#3.1 Leading KPIs (early signals)|KPI L2 (d)]].

### Step 11. Branded and non-branded clicks

- **Where:** **Performance → Search results**, the branded queries filter (branded queries are searches that include "Quotr").
- **How:**
  1. If the filter is there, split clicks into branded and non-branded, for the whole site and per post.
  2. If it is missing (a small site or the wrong property type), add a Query filter, choose Custom (regex, a text pattern), and type `quotr`. Then exclude namesakes such as `quotr pro` ([[Tracking setup#3.4 Branded search (monthly; trend reviewed quarterly)]]).
- **Good looks like (inference):** blog posts earn mostly non-branded clicks. These measure how far the blog reaches new buyers.
- **Record:** branded clicks and impressions for the whole site go monthly to [[KPIs and dashboard#3.2 Lagging KPIs (business results)|KPI G3]]. In each article note, record the non-branded share of clicks each month.
- **A date to reconcile:** [[Tracking setup]] says the filter reached all eligible sites on March 11, 2026. GSC-08 says about March 2026, exact date unknown. Fix this when Tracking setup is next verified.

### Step 12. Posts that compete for the same searches

- **Where:** **Performance → Search results**, the **Queries** and **Pages** tabs. If Insights shows query groups, use them too. They appear only for properties with a large query volume (GSC-05).
- **How:** for each overlap group, filter by a shared query. Then open the Pages tab to see how many Quotr addresses share its impressions.

| Group | Shared query to try | Posts |
|---|---|---|
| Togal.AI alternatives | `togal` | [[BP-15 quotr vs togal ai comparison 2026\|BP-15]], [[BP-32 best togal ai alternatives\|BP-32]], [[BP-43 best togal ai alternatives 2026\|BP-43]] |
| STACK | `stack` | [[BP-34 quotr ai vs stack browser first takeoff procurement\|BP-34]], [[BP-51 stack alternative\|BP-51]] |
| AI bid software | `bid software` | [[BP-08 ai construction proposals takeoff to proposal\|BP-08]], [[BP-47 ai bidding software construction\|BP-47]], [[BP-80 best ai bid software for construction\|BP-80]] |
| Pro forma | `pro forma` | [[BP-22 real estate pro forma software comparison\|BP-22]], [[BP-29 the proforma that never stops changing\|BP-29]], [[BP-49 construction proforma software\|BP-49]] |
| Estimating services | `estimating services` | [[BP-79 construction estimating services\|BP-79]], [[BP-82 outsource construction estimating\|BP-82]], [[BP-84 construction estimating services california\|BP-84]], [[BP-85 commercial estimating services\|BP-85]], [[BP-86 preconstruction services\|BP-86]], [[BP-87 quantity takeoff services\|BP-87]], [[BP-89 precon on demand outsource bid cost estimation\|BP-89]], [[BP-90 outsourcing vs hiring an estimator\|BP-90]] |

The full map of 20 overlap groups is in [[Blog health audit]].

- **Good looks like:** one Quotr address leads each main query. Where several share it, one is the clear winner on clicks, impressions and AI impressions.
- **Why it matters:** Google's spam policies count "creating many pages with search keywords that make little sense to readers" as scaled content abuse (QUALITY-02). Google's May 2026 AI guide adds separate pages for every variation of a question, made mainly to steer AI answers (QUALITY-05, INDEX-06, AI-07). Genuine coverage of subtopics is fine.
- **Record:** in each article note, the shared queries and which address leads. On the losing post, set `merge_into` to the winner and add the flag `shares queries (GSC)`. This feeds task [[A12 Merge duplicate pages|A12]].
  - Where possible, keep the addresses AI already cites (for example BP-32, BP-82, BP-85 and BP-87).
  - Merges wait until the September 2026 spam update is complete.

![[Articles.base#Merge or retire]]

### Step 13. After every refresh or merge

- **On the day:** add a chart note. Then paste the address into URL Inspection and click **Request indexing** ([[Tracking setup#3.5 After fixing pages: ask Google to re-read them]]).
- **Optional (needs a script):** pull hourly data through the Search Analytics API (a way for scripts to fetch Search Console data) for 10 days, to see whether Google picked up the change. The Search Console screens show hourly data only for the last 24 hours (GSC-01).
- **After 28 days:** compare clicks, impressions and AI impressions with the 28 days before. Do not measure across a core or spam update rollout.
- **Good looks like:** every refresh has a before-and-after row that does not overlap a Google update.
- **Record:** a Log line ("YYYY-MM-DD: refreshed: what changed; chart note added") and a before-and-after row in the Search Console table. The full after-refresh routine is in [[Content refresh playbook#After each refresh]].

### Step 14. Bing Webmaster Tools: AI Performance (companion check)

- **Where:** [Bing Webmaster Tools](https://www.bing.com/webmasters), the **AI Performance** report ([[Tracking setup#4.3 The AI Performance report (monthly)]]).
- **What it shows:** how often Copilot and Bing AI answers cite Quotr's pages, and which pages (OTHER-01). It also lists "grounding queries": the search phrases Copilot generated to find and cite the pages (OTHER-02). It is summary data only. It does not show single answers, exact prompts or why a page was chosen ([[Tracking setup]]).
- **How sure:** Microsoft announced it as a public preview on 2026-02-10; some coverage says 02-11 (OTHER-01). This was carried over from the 2026-09-25 research, and the vault's fact-check still describes it as a public preview.
- **How:** export the cited pages and the grounding queries each month.
- **Good looks like:** Quotr posts among the cited pages, and grounding queries that match the questions the posts answer.
- **Record:** the monthly Bing AI citations in each cited post's Search Console table. Site totals go to KPI L2 (e) in [[KPIs and dashboard]]. New real question wording from the grounding queries goes to [[Prompt library]].

---

## Record the results in the brain

### Site-wide results (not in article notes)

| Result | Where it goes |
|---|---|
| Property type, owner, users, access date (step 1) | [[Tracking setup#3.1 Properties and sitemaps (one-off)]]; answer [[Q-40 Access and history\|Q-40]] when Quotr replies |
| "Search generative AI" setting and date (step 2) | [[KPIs and dashboard]] (L2 d) and [[Tracking setup#3.3 Do NOT opt out]] |
| Manual actions result (step 3) | [[Website audit]] |
| Past events on the chart (step 4) | The table in step 4 is the permanent list; new site-wide events go in the monthly dashboard |
| Site AI impressions (step 10) | [[KPIs and dashboard]], KPI L2 (d) |
| Branded clicks and impressions (step 11) | [[KPIs and dashboard]], KPI G3 |
| Bing AI citations and grounding queries (step 14) | [[KPIs and dashboard]], KPI L2 (e); [[Prompt library]] |
| Every audit | One line at the top of [[Changelog]] (vault rule 7) |

### In each article note

Each post has one article note (for example [[BP-32 best togal ai alternatives|BP-32]]). Open it in Obsidian and do four things.

**1. Update the properties**

| Property | What to set | Example |
|---|---|---|
| `web_indexed` | Google's answer from URL Inspection: `yes` or `no`. Until you inspect a post, leave what is there (`yes`, `no` or `not checked` from the web searches of 2026-09-25 and 09-26). | `yes` |
| `search_check` | One line that names the source and the date. | `URL Inspection (Search Console), 2026-10-02: on Google` |
| `flags` | Add the Search Console flags from the table below. Remove a flag when it no longer applies, and say so in the Log. | `not indexed (GSC)` |
| `health` and `health_score` | If Search Console changes the picture, re-score the **Visibility** area with the rubric in [[Content refresh playbook#How we score a post's health]]. Then update the score and the band. | — |
| `status` | If a post marked `ok` or `done` now has a problem flag, set it to `todo`. Say in the Log what needs doing. | `todo` |
| `merge_into` (and `action`) | Only after step 12, and only if the decision changed. Link to the keeper, in quotes. | `"[[BP-32 best togal ai alternatives]]"` |
| `ai_cited` and `cited_in` | **Leave as they are.** They record the September 2026 tests. AI impressions go in the flags and the table instead. | — |

**2. Use these flags** (type them exactly, so the tables can be searched)

| Flag | Add it when | Step |
|---|---|---|
| `not indexed (GSC)` | Page indexing or URL Inspection says the post is not on Google | 6, 7 |
| `manual action (GSC)` | The Manual actions report names the post | 3 |
| `dropped after update (GSC)` | The post lost more than half its clicks or impressions after a Google update (our rule of thumb) | 5, 9 |
| `declining (GSC)` | Clicks fell two months in a row (our suggested rule) | 8 |
| `AI impressions (GSC)` | The post has impressions in the Generative AI report | 10 |
| `shares queries (GSC)` | Another Quotr post leads on its main query | 12 |

**3. Add a "Search Console" section**

The first time, add this block just above `## Log`. Then add new lines and rows below the old ones. Never edit an old row.

```
## Search Console

**Indexing checks**
- YYYY-MM-DD: on Google yes/no · reason if not · Google canonical: this post / [other address] · last crawl YYYY-MM-DD · snippets allowed yes/no

**Numbers** (Web search; only windows from 2026-04-28)

| Window | Clicks | Impressions | CTR | Avg position | AI impressions (Google) | Bing AI citations | Non-branded share | Note |
|---|---|---|---|---|---|---|---|---|
| 2026-09-17 to 09-23 (baseline) | | | | | | | | |

**Google updates**
- May 2026 core: clicks A to B, impressions A to B; gain / loss / flat / too new
```

If the "Search generative AI" setting was ever on (step 2), add a line with those dates here.

**4. Add a Log line**

Add one line at the bottom, under `## Log`, in this form:

```
- YYYY-MM-DD: what you found or changed, who checked it.
```

Fill-in examples:

```
- YYYY-MM-DD: URL Inspection: on Google yes; Google canonical = this post; last crawl YYYY-MM-DD. Set web_indexed to yes (web search had not returned it on 2026-09-26). Checked by [name].
- YYYY-MM-DD: September 2026 spam update: clicks A to B, impressions A to B (baseline week vs first full week after). Added flag dropped after update (GSC); status set to todo. Checked by [name].
- YYYY-MM-DD: refreshed: [what changed]; chart note added; indexing requested. Checked by [name].
```

- The Log is append-only. Add a new line; never edit an old one.
- Never delete an article note (vault rule 5).

### How the Articles tables update by themselves

The Articles tables (Obsidian Bases) read the note properties live. Save a note, and every table that shows it changes. You do not need to edit any table.

| When you change… | …this table changes |
|---|---|
| `web_indexed` | "Not found in web search" (posts with `no`) |
| `status` to `todo` or `doing` | "Refresh queue" and "Full refresh plan" |
| `flags` | The Flags column in "Refresh queue" and "Worst health first" |
| `health_score` | "Worst health first", and the average score per cluster in "By cluster" |
| `action` or `merge_into` | "Merge or retire" and "Full refresh plan" |

The plain-text copies of these tables (in the exports folder) refresh only when the export script runs. An AI helper runs it before each commit (vault rule 9).

---

## Known data quirks

### Quirks that change the numbers

| Quirk | Dates | What it does | What to do | Claim |
|---|---|---|---|---|
| **Impressions over-counted** | 2025-05-13 to 2026-04-27 | Impressions were too high, so CTR and position were off too. Clicks were fine. Old data was not corrected. Affects BP-01 to BP-06, which went live before the fix. | Compare only windows from 2026-04-28. Use clicks for anything earlier. | GSC-12 |
| **The num=100 change** | About 2025-09-12 to 09-14 | Impressions fell for most sites, and average position looked better. This was not a ranking change. One analysis found 87.7% of 319 properties lost impressions. | Context only: every Quotr post went live after it (the first on 2025-12-19). Do not start a site-wide trend line before it. | GSC-04 |
| **AI Mode inside the Web totals** | From June 2025 (exact day unknown) | AI Mode clicks, impressions and positions are mixed into the normal Performance totals and cannot be separated there. | Read Web totals as "classic results plus AI Mode". Use the Generative AI report for AI impressions. | GSC-02 |
| **Page indexing report froze (first time)** | 2025-11-17 to 2025-12-18 | The report stopped updating. Google said only reporting was affected, not crawling or indexing. | Read the "last updated" date before trusting the report. | GSC-11 |
| **Page indexing report froze (second time)** | 2026-06-11 to 2026-07-03 | Stale data for about three weeks. 18 posts (BP-40 to BP-57) went live in that window. | Use URL Inspection for those posts (step 7). | GSC-17 |
| **Generative AI logging error** | From 2026-08-13; restored about 2026-08-21 | Lowered AI impressions in the Generative AI (Search) report and Discover data. The missing data for 08-13 to 08-17 was reportedly restored. | If it still looks low, mark it as the error, not a real loss. | GSC-19 |
| **New multimodal filter** | From 2026-09-24 | A new search type for Lens, Circle to Search, image uploads and Chrome "Search this image". This traffic was not counted before. It has no query data. Whether it changes the default totals is unknown. | Add a chart note. Take care reading late-September trends. | GSC-20 |

### Limits of the tools

| Limit | What it means | Claim |
|---|---|---|
| **Generative AI report: impressions only** | No clicks, CTR or queries. Data starts on 2026-05-18, with no backfill. Split by page, country and date (and device in the Search report). Live for all sites from 2026-08-31. | GSC-13, GSC-14, GSC-16 |
| **AI impressions are part of Web** | The AI report is a filtered view of Web data. Never add it to the Web totals. | INDEX-13, AI-10 |
| **"Position" in AI Overviews** | The whole AI Overview block gets one position, so it is not a rank among the cited links (single source). | INDEX-15 |
| **Chart notes expire** | Up to 120 characters, 200 per property, deleted after 500 days. Hidden in comparison mode and the 24-hour view. | GSC-06 |
| **Branded filter can be missing** | Not available for sub-properties (such as /blog/) or low-impression sites. | GSC-07, GSC-08 |
| **Query groups can be missing** | Only for properties with a large query volume. | GSC-05 |
| **AI-powered configuration** | Experimental. It can misread requests and cannot export. | GSC-09 |
| **Hourly data** | The screens show only the last 24 hours. The API goes back 10 days. | GSC-01 |
| **Bing AI Performance** | Public preview; summary data only. | OTHER-01, OTHER-02 |

---

## How often

| When | What to do | Steps |
|---|---|---|
| **Once, when access arrives** | The full first audit: access, settings, chart notes for past events, indexing of all 96 posts, past updates, overlaps, Bing | 1-12, 14 |
| **When the September 2026 spam update ends** (about 2026-10-08) | Compare the first full week after it with the baseline week | 5 |
| **After every refresh or merge** | Chart note, Request indexing, 28-day before-and-after | 13 |
| **Weekly glance** (optional) | Insights: rising and falling pages; any fix that needs a re-crawl request | 8, 13 |
| **Monthly light check** (first week, with the monthly AI test run) | See the checklist below | 2, 6, 8, 10, 11, 14 |
| **Quarterly full audit** | Everything in the monthly check, plus the steps listed here. The first one fits the day-90 review in late December 2026 ([[Tracking setup]]). | 1, 3, 7, 9, 12 |
| **When Google announces a core or spam update** | Freeze bulk changes, add chart notes for the start and end, and compare by cluster after it ends | 4, 9 |

**Monthly light check**
- [ ] The "Search generative AI" setting is still off (step 2).
- [ ] Google's [data anomalies page](https://support.google.com/webmasters/answer/6211453?hl=en) shows no new logging problem.
- [ ] The Page indexing report's "last updated" date is recent, and no new post is missing (step 6).
- [ ] Each post has its monthly row: clicks, impressions, CTR, position (step 8).
- [ ] AI impressions per post and the site total are recorded (step 10).
- [ ] Branded clicks and impressions are recorded (step 11).
- [ ] Bing AI citations and new grounding queries are recorded (step 14).
- [ ] One [[Changelog]] line for the check.

**Quarterly full audit, on top of the monthly check**
- [ ] Users on the property are still right (step 1).
- [ ] Manual actions: still "No issues detected" (step 3).
- [ ] URL Inspection on every flagged post, every post refreshed or merged, and every new post (step 7).
- [ ] Before-and-after for any Google update in the quarter (step 9).
- [ ] Overlap check for every group, including new posts (step 12).

---

## Related pages

- [[Content refresh playbook]]: how to refresh, merge or retire a post, and the health rubric
- [[Blog health audit]]: how the 96 posts were scored, and the full overlap map
- [[Google search updates 2025-2026]]: Google's updates and what they mean for Quotr
- [[Refresh plan Q4 2026]]: the dated plan for October to December 2026
- [[What went wrong]]: the findings behind this audit
- [[Tracking setup]]: setting up Search Console, Bing, GA4 and Cloudflare
- [[KPIs and dashboard]]: where the site-wide numbers go each month
