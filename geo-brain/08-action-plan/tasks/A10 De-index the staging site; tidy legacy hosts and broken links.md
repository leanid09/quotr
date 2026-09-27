---
type: task
id: A10
task: De-index the staging site; tidy legacy quotr.io hosts and 404s
phase: Days 1–30 (Oct 2026)
month: 2026-10
week: 2
rank: 10
owner: Dev
effort: S
impact: M
depends_on_text: Access to test.quotr.io and quotr.io
status: todo
done_when: removal requests accepted; a site:test.quotr.io search returns nothing; quotr.io URLs return 301s to the matching quotr.ai pages; the brand prompt "Quotr.ai pricing" no longer cites test.quotr.io in the next monthly run.
---
# A10. De-index the staging site; tidy legacy hosts and broken links

- **What:** Keep [test.quotr.io](https://test.quotr.io/disambiguation/) behind its login, add `noindex`, and request removal in Search Console and Bing Webmaster Tools. Check that quotr.io pages 301-redirect page-to-page to quotr.ai (for example [quotr.io/pricing/](https://quotr.io/pricing/) currently serves the pricing page with a canonical to quotr.ai; whether it redirects is unknown). Decide where the FireTips app ([firetips.quotr.io](https://firetips.quotr.io/)) should live. Fix the 404s (/blog/plug-number-estimating/; www.quotr.ai/resources/) and point the 404 page's "Back home" button to / instead of /dashboard/project.
- **Why (evidence):** Perplexity cited the staging page for "Quotr.ai pricing" on the original run and again on the fact-check re-run (verification file, re-run B2 and Gaps filled #3).
- **Owner:** Dev.
- **Effort / Impact:** S / M.
- **Depends on:** access to test.quotr.io, quotr.io and DNS.
- **Done when:** removal requests accepted; a `site:test.quotr.io` search returns nothing; quotr.io URLs return 301s to the matching quotr.ai pages; the brand prompt "Quotr.ai pricing" no longer cites test.quotr.io in the next monthly run.
- **How-to:** [[Optimize vs create]] (sweep section E, rows 42–43, 48); [[Website audit]] §5.

---

Part of [[30-60-90 plan#Days 1–30 (about October 2026): quick wins and clean-up|30-60-90 plan › Days 1–30]]
