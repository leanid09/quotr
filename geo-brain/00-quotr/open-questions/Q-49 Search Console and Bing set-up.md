---
type: question
id: Q-49
question: 'Search Console and Bing set-up: is quotr.ai verified as a Domain property in Google Search Console, and is there one for quotr.io? Who is the owner? Can the consultant be added as a Full user there, and with read-write rights in Bing Webmaster Tools? Is /blog/sitemap.xml submitted in both? Has the "Search generative AI" control ever been switched on? Does anyone check the Page indexing report today?'
topic: J. Measurement, process and budget
ask: Quotr
status: open
answer:
answered_on:
---
# Q-49 · Search Console and Bing set-up

> [!question] Question for Quotr
> **Search Console and Bing set-up:** is quotr.ai verified as a Domain property in Google Search Console, and is there one for quotr.io? Who is the owner? Can the consultant be added as a Full user there, and with read-write rights in Bing Webmaster Tools? Is /blog/sitemap.xml submitted in both? Has the "Search generative AI" control ever been switched on? Does anyone check the Page indexing report today?

**Why we ask:** without this data, the blog audit cannot say which posts are indexed, which were hit by a Google update, or which show up in AI answers. See [[Blog health audit]] and [[Search Console audit playbook]].

- **Domain property.** A Domain property covers every quotr.ai address. It is verified through DNS (the domain's settings). The branded-queries filter does not work on a smaller property, such as one for /blog/ only (GSC-07).
- **Full user.** A Restricted user can only look. A Full user can also submit sitemaps and ask Google to re-read fixed posts.
- **Bing.** Bing Webmaster Tools is Microsoft's version of Search Console. Bing feeds Copilot ([[Website audit]]).
- **Blog sitemap.** /blog/sitemap.xml is the only file that lists all 96 posts. It is not named in robots.txt ([[What went wrong#W-15 Thin or broken crawl paths to the posts|W-15]]). So we need to know whether it was submitted directly.
- **AI control.** Search Console has a "Search generative AI" setting that takes a whole site out of AI Overviews and AI Mode ([[Tracking setup]] §3.3; GSC-15). It must stay off. If it was ever on, it would explain missing AI data for that time.
- **Indexing.** In targeted web searches on 2026-09-25 and 2026-09-26, 15 of 36 posts checked did not come back. That tool is not Google, and the sample was not random, so this is a lead, not proof. We cannot see whether Quotr already checks indexing ([[What went wrong#W-10 Some posts did not come back in web search|W-10]]).
- **Already asked.** [[Q-40 Access and history|Q-40]] asks for access in general. This question adds the details the blog audit needs. [[Q-32 quotr.io|Q-32]] asks whether quotr.io redirects to quotr.ai.

## Answer

*When Quotr answers: put the short answer in the `answer` property, fill `answered_on`, set `status` to `answered`, record the property type, owner and access date in [[Tracking setup]] §3.1, and add a line to [[Changelog]].*

---

From [[Blog health audit]] · J. Measurement, process and budget
