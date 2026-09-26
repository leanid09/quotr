---
type: question
id: Q-51
question: 'Cloudflare crawler data and logs: can the consultant get read access to Cloudflare AI Crawl Control for quotr.ai (or a monthly screenshot), showing which AI bots fetch /blog/ posts and what status codes they get? Is Crawler Hints (IndexNow) on? Where is the site hosted, and are raw access logs kept?'
topic: H. Domains, profiles and technical setup
ask: Quotr
status: open
answer:
answered_on:
---
# Q-51 · Cloudflare crawler data and logs

> [!question] Question for Quotr
> **Cloudflare crawler data and logs:** can the consultant get read access to Cloudflare AI Crawl Control for quotr.ai (or a monthly screenshot), showing which AI bots fetch /blog/ posts and what status codes they get? Is Crawler Hints (IndexNow) on? Where is the site hosted, and are raw access logs kept?

**Why we ask:** we cannot tell whether AI search bots reach the blog posts. See [[Blog health audit]] and [[Tracking setup]] §5.

- **What AI Crawl Control shows.** It is Cloudflare's dashboard for AI bots. It shows requests by bot, by page and by status code. 200 means the page was served. 403, 429 or 503 mean the bot was blocked, slowed or challenged.
- **Posts missing from search.** 15 of 36 posts checked did not come back in targeted web searches ([[What went wrong#W-10 Some posts did not come back in web search|W-10]]). A crawl block is one possible cause. Perplexity cites quotr.ai pages, which suggests its bot gets in (inference; [[Tracking setup]] §5.1). Access for the ChatGPT, Claude and Copilot bots is unverified.
- **Crawler Hints.** A free Cloudflare setting that tells Bing about changed pages through IndexNow (a way to tell search engines a page has changed). It helps after the price fixes on 13 to 16 posts. IndexNow does not reach Google.
- **RSS feed.** The blog feed (/blog/rss.xml) returned a Cloudflare 502 error once. It may have been temporary ([[What went wrong#W-15 Thin or broken crawl paths to the posts|W-15]]).
- **Already asked.** [[Q-34 Cloudflare|Q-34]] asks about the settings ("Block AI bots", managed robots.txt, AI Labyrinth). [[Q-32 quotr.io|Q-32]] asks who controls Cloudflare. This question asks for the data. Task: [[A11 Confirm Cloudflare lets AI search bots in|A11]].

## Answer

*When Quotr answers: put the short answer in the `answer` property, fill `answered_on`, set `status` to `answered`, record the details in [[Tracking setup]] §5, and add a line to [[Changelog]].*

---

From [[Blog health audit]] · H. Domains, profiles and technical setup
