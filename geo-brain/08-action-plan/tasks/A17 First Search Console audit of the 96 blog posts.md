---
type: task
id: A17
task: First Search Console audit of the 96 blog posts (indexing, before-and-after, overlaps, Bing)
phase: Days 1–30 (Oct 2026)
month: 2026-10
week: 1
rank: 15.5
owner: GEO consultant (Quotr gives access)
effort: M
impact: M
depends_on: []
depends_on_text: Search Console and Bing access (Q-49)
status: todo
done_when: steps 1-12 and 14 of the Search Console audit playbook are done once; every article note has its indexing state and a dated Log line; the spam-update before-and-after is recorded; the list of posts that are not indexed, and the pairs of posts that share the same searches, is sent to marketing.
---
# A17. First Search Console audit of the 96 blog posts

- **What:** Run the one-off first audit in [[Search Console audit playbook]] (steps 1-12, plus step 14 for Bing Webmaster Tools):
  1. Day 1: check that the "Search generative AI" setting is off and that manual actions say "No issues detected".
  2. Save 2026-09-17 to 2026-09-23 as the baseline week, before Google's September 2026 spam update (RANK-21).
  3. Check indexing (whether Google has stored the page so it can show it) for all 96 posts. Start with the 15 posts that targeted web searches did not return.
  4. Record clicks, impressions and AI impressions for each post.
  5. Find pairs of posts that compete for the same searches.
  6. Write every result into the article notes: properties, flags and a dated Log line.
- **Why (evidence):**
  - No Quotr Search Console data has been seen yet. How each post does in Google is unknown ([[Search Console audit playbook]]).
  - 15 of the 36 posts checked did not come back in 3-7 targeted searches each. 60 posts were not checked, because the search limit ran out on 2026-09-26. The search tool is not Google, so only Search Console can confirm indexing ([[What went wrong]], W-10).
  - Google says a page must be indexed to appear as a source in its AI answers (INDEX-05).
  - Every merge in [[Refresh plan Q4 2026]] waits for Search Console data on both pages.
  - Task A15 sets up the reports and the AI baseline. It does not check the posts one by one.
- **Owner:** GEO consultant. Quotr adds the consultant as a user ([[Q-49 Search Console and Bing set-up|Q-49]], [[Q-40 Access and history|Q-40]]).
- **Effort / Impact:** M / M (it steers the merges and the refresh order; it does not move an AI-answer number by itself).
- **Depends on:** access to Search Console and Bing Webmaster Tools. Start in week 1, next to [[A15 Measurement setup and multi-engine baseline|A15]]. If access comes late, save the baseline week first: the dates can still be exported afterwards.
- **Done when:** steps 1-12 and 14 of the Search Console audit playbook are done once; every article note has its indexing state and a dated Log line; the spam-update before-and-after is recorded; the list of posts that are not indexed, and the pairs of posts that share the same searches, is sent to marketing.
- **How-to:** [[Search Console audit playbook]] (the step table and "How often"); [[Tracking setup]] §3; [[Content refresh playbook]] ("After each refresh"); the live list of posts not found in web search: `Articles.base`, view "Not found in web search".

---

Part of [[30-60-90 plan#Days 1–30 (about October 2026): quick wins and clean-up|30-60-90 plan › Days 1–30]] · Schedule: [[Refresh plan Q4 2026]]
