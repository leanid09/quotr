---
type: task
id: A9
task: Sitemaps and lastmod dates
phase: Days 1–30 (Oct 2026)
month: 2026-10
week: 2
rank: 9
owner: Dev
effort: S
impact: M
depends_on_text: Code access
status: todo
done_when: robots.txt shows three sitemap lines (or one index); a sample of 10 URLs shows lastmod dates that match their pages; both sitemaps submitted in Search Console and Bing Webmaster Tools.
---
# A9. Sitemaps and lastmod dates

- **What:** Add `Sitemap: https://quotr.ai/blog/sitemap.xml` to [robots.txt](https://quotr.ai/robots.txt) (or publish one sitemap index). Make lastmod the real date of the last content change, matching the page's "Last updated" date. Add /disambiguation/ and /blog/ to the main sitemap. Keep robots.txt otherwise as it is (it lets every bot in, which is right).
- **Why (evidence):** robots.txt lists the main and dictionary sitemaps but not the 96-post blog sitemap. Every URL in the main sitemap says "Last modified: 2026-09-25, weekly", so the date means nothing. Some blog dates disagree with the page (Togal alternatives: sitemap 2026-06-16 vs page "Last updated August 4, 2026") (verification file, claims 1–4). Bing powers Copilot, so helping Bing find the blog matters (report).
- **Owner:** Dev.
- **Effort / Impact:** S (report's technical hygiene total: "Developer, 1 day") / M.
- **Depends on:** code access.
- **Done when:** robots.txt shows three sitemap lines (or one index); a sample of 10 URLs shows lastmod dates that match their pages; both sitemaps submitted in Search Console and Bing Webmaster Tools.
- **How-to:** [[Website audit]] §3; [[Optimize vs create]] (sweep section E, rows 44–46); [[Tracking setup]] §3.1 and §4.2.

---

Part of [[30-60-90 plan#Days 1–30 (about October 2026): quick wins and clean-up|30-60-90 plan › Days 1–30]]
