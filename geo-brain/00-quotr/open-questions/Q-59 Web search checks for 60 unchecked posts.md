---
type: question
id: Q-59
question: 'Re-run the targeted web search checks (site:, exact-URL and exact-title searches) for the 60 blog posts not checked on 2026-09-26, once a new session has search allowance. At the same time, re-read the live pages of the posts flagged for retired prices, and re-check the blog RSS feed.'
topic: K. Still unverified (for us to check)
ask: us
status: open
answer:
answered_on:
---
# Q-59 · Web search checks for 60 unchecked posts

> [!question] To check ourselves
> Re-run the targeted web search checks (site:, exact-URL and exact-title searches) for the 60 blog posts not checked on 2026-09-26, once a new session has search allowance. At the same time, re-read the live pages of the posts flagged for retired prices, and re-check the blog RSS feed.

**Why we check:** the search limit ran out on 2026-09-26, so the web search picture covers only 36 of 96 posts. See [[Blog health audit]] and [[What went wrong#W-10 Some posts did not come back in web search|W-10]].

- **What was checked.** 36 posts: 21 came back, 15 did not.
- **Not a rate.** The sample was not random. List posts were checked on 2026-09-25 and how-tos on 2026-09-26. So "15 of 36" is not a rate for the whole blog.
- **Old prices.** Up to 16 posts are flagged: 13 on the vault list and 3 weaker matches from search summaries. Only 2 were read on the live page ([[BP-51 stack alternative|BP-51]] and [[BP-43 best togal ai alternatives 2026|BP-43]]). 4 more list posts were never checked for old prices: [[BP-52 best plumbing estimating software 2026|BP-52]], [[BP-55 best drywall estimating software in 2026|BP-55]], [[BP-37 electrical estimating software buyers guide|BP-37]] and [[BP-64 trade estimating software|BP-64]].
- **RSS feed.** /blog/rss.xml returned a Cloudflare 502 error once. Check it again before telling Quotr ([[What went wrong#W-15 Thin or broken crawl paths to the posts|W-15]]).

**How to check**

1. For each post, run the same 3 to 7 searches as before: a site: search, an exact-URL search and a search for the post's own title.
2. Write "found" or "not found" and the date in the post's article note.
3. "Not found" is a lead for URL Inspection in the [[Search Console audit playbook]], not proof. Once Search Console access arrives ([[Q-49 Search Console and Bing set-up|Q-49]]), its Page indexing report replaces this check.
4. For the old prices, open each flagged post and look for "Solo", "Team (2", "$499.90" and "from $299.90". Write the result in the article note.

> [!note]- The 60 posts not checked
> BP-01, BP-02, BP-03, BP-07, BP-08, BP-09, BP-12, BP-14, BP-16, BP-18, BP-19, BP-21, BP-23, BP-25, BP-27, BP-29, BP-30, BP-31, BP-33, BP-35, BP-36, BP-37, BP-38, BP-40, BP-41, BP-42, BP-49, BP-50, BP-52, BP-55, BP-56, BP-58, BP-59, BP-60, BP-61, BP-62, BP-63, BP-64, BP-65, BP-66, BP-68, BP-69, BP-70, BP-71, BP-72, BP-73, BP-75, BP-78, BP-79, BP-82, BP-84, BP-85, BP-87, BP-88, BP-89, BP-91, BP-93, BP-94, BP-95, BP-96.

## Answer

*When checked: put the finding in the `answer` property, fill `answered_on`, set `status` to `answered`, and add a line to [[Changelog]].*

---

From [[Blog health audit]] · K. Still unverified (for us to check)
