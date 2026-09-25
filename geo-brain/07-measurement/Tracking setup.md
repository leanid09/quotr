---
type: playbook
description: Step-by-step setup of GA4, Search Console, Bing Webmaster Tools, crawler checks, form field and reporting rhythm.
last_verified: 2026-09-25
verify_every_days: 180
---
# GEO Tracking Setup (Step by Step)

> [!abstract] What this page is for
> Step-by-step instructions for setting up everything Quotr needs to measure GEO/AEO progress: GA4 for AI referral visits, Google Search Console and Bing Webmaster Tools, AI crawler checks in Cloudflare or server logs, a "How did you hear about us?" field, the monthly manual prompt test, and a weekly, monthly and quarterly reporting rhythm.

> [!info]- Sources
> Final report [[Quotr GEO AEO strategy audit]] (30-day action 7 and 10, measurement section). Research notes [[geo_content_playbook_b2b]] (§4: GA4 channel, regex, forms, CRM, cadence), [[geo_ai_citation_signals_2026]] (§1 crawlers and `utm_source=chatgpt.com`; §4–5), [[verification_geo_evidence]] (claims 3, 7; M1; H17), [[quotr_onsite_content_audit]] (§1 robots.txt, sitemaps, Cloudflare AI Labyrinth), [[quotr_ai_visibility_tests]] (method). Brain files [[How AI engines choose sources]] (crawler table), [[Website audit]], [[Tracking set]]. Setup details checked on 2026-09-25 with web search: Google [GA4 channel docs](https://support.google.com/analytics/answer/9164320), [SEJ on the GA4 AI channel](https://www.searchenginejournal.com/google-analytics-adds-ai-assistant-as-default-channel-group/574974/), [Swydo](https://www.swydo.com/blog/track-ai-traffic-in-ga4/), [Seybold](https://seybold.de/en/guide/ai-traffic-google-analytics-4/), [Analytics Mania](https://www.analyticsmania.com/post/regex-in-google-analytics-4/), [Lawrence Hitches on AI Mode in GA4](https://www.lawrencehitches.com/google-ai-mode-traffic-ga4/), [Google: Search Console generative AI reports](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports), [Search Console help](https://support.google.com/webmasters/answer/16984139?hl=en), [Google: branded queries filter](https://developers.google.com/search/blog/2025/11/search-console-branded-filter), [Search Engine Land on the filter's expansion](https://searchengineland.com/google-search-console-branded-queries-filter-expands-471387), [Bing AI Performance](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview), [Cloudflare AI Crawl Control docs](https://developers.cloudflare.com/ai-crawl-control/), [Cloudflare: AI crawlers blocked by default](https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/), [Cloudflare Crawler Hints docs](https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/).

---

## 0. Overview: what to set up, and in what order

The report puts measurement setup in the **first 30 days** and estimates it at **2–3 days** of work: "Without a baseline, no one can prove progress" ([[Quotr GEO AEO strategy audit|report]]).

| # | Setup task | Who (suggested) | Time (estimate) | Section |
|---|---|---|---|---|
| 1 | GA4: check the native AI Assistant channel; add a custom AI channel that also catches Perplexity; mark key events | Marketing + developer | 2–3 hours | §1 |
| 2 | Learn the UTM and attribution blind spots | Marketing | 30 minutes | §2 |
| 3 | Google Search Console: properties, sitemaps, Generative AI report, branded filter, re-crawl requests | Marketing | 1–2 hours | §3 |
| 4 | Bing Webmaster Tools: import site, sitemaps, AI Performance report, IndexNow | Marketing + developer | 1 hour | §4 |
| 5 | AI crawler check in Cloudflare (and server logs if available) | Developer / whoever owns Cloudflare | 1–2 hours, then 15 min a month | §5 |
| 6 | "How did you hear about us?" field on demo, contact and trial forms, plus a CRM field | Marketing + developer | Half a day | §6 |
| 7 | Monthly manual prompt test (first run in early October 2026) | GEO consultant / marketing | About 3 hours a month (Lite) | §7 |
| 8 | Reporting rhythm and dashboard | GEO consultant | 1 hour to set up | §8 |

Owners are suggestions. **Who controls GA4, Search Console, Bing Webmaster Tools, Cloudflare, the forms and the CRM is TO CONFIRM with Quotr.** The report also asks "Who controls Cloudflare, quotr.io and test.quotr.io?".

Menu names below were correct as far as we could check on 2026-09-25. Google, Microsoft and Cloudflare rename menus often; if a name differs, search the product's help pages for the feature name.

---

## 1. GA4: track visits from AI tools

### 1.1 What GA4 does on its own (and what it misses)

- **On May 13, 2026, GA4 added a native "AI Assistant" channel** to its default channel group. Visits from recognised AI chatbots get the medium `ai-assistant` and appear under that channel ([SEJ](https://www.searchenginejournal.com/google-analytics-adds-ai-assistant-as-default-channel-group/574974/); [[verification_geo_evidence|verification claim 7]]).
- **Which AI tools it recognises:** Google's "What's new" note named ChatGPT, Gemini and Claude. The later channel definition lists ChatGPT, Gemini, DeepSeek, Copilot and Grok. **Perplexity is not included**; its visits still land in "Referral" ([Google](https://support.google.com/analytics/answer/9164320); verification claim 7).
- **It is not retroactive.** It only labels visits from the date Google switched it on for the property ([[geo_content_playbook_b2b|playbook §4]]).
- **Some AI visits still land in Direct or Referral** (in-app browsers, pasted links). See §2.

So Quotr should **keep the native channel and add its own custom AI channel** on top.

### 1.2 Check the native channel (5 minutes)

1. In GA4, go to **Reports → Acquisition → Traffic acquisition**.
2. Make sure the table's first column is **Session default channel group**.
3. Look for a row called **AI Assistant**. Note its sessions and key events for the last full month.
4. Change the first column to **Session source / medium** and look for `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com`, `claude.ai`. This shows what the native channel is missing.

### 1.3 Create a custom channel group with an "AI assistants (all)" channel

1. Go to **Admin → Data display → Channel groups**.
2. Click **Create new channel group**. Name it `Quotr channels (with AI)`. GA4 starts you with a copy of the default channels.
3. Click **Add new channel**. Name it `AI assistants (all)`.
4. Add a condition: **Source** → **partially matches regex** → paste the regex below.
   - If you can only choose **matches regex** (a full match), wrap the pattern like this: `.*(` + pattern + `).*`.
   - GA4 regex is **case sensitive**, and these sources are recorded in lowercase, so keep the pattern lowercase ([Swydo](https://www.swydo.com/blog/track-ai-traffic-in-ga4/)).
5. Save the channel, then **drag it above "Referral"** in the list. Rules run from top to bottom, so a visit is labelled by the first rule it matches ([[geo_content_playbook_b2b|playbook §4]]). Keep it **below the Paid channels**, so that any future paid ChatGPT ads tagged as paid stay in Paid (our suggestion).
6. Save the group.
7. Use it: in **Traffic acquisition**, change the first column to your new channel group (`Session Quotr channels (with AI)`).

**Good news:** third-party GA4 guides report that **custom channel groups also work on past data**, unlike the native channel ([Swydo](https://www.swydo.com/blog/track-ai-traffic-in-ga4/); [Summit](https://www.summit.co.uk/opinions-news/native-ga4-vs-custom-regex-navigating-the-new-era-of-ai-traffic/)). So Quotr can pull AI referrals for **January–September 2026** on setup day and use them as the G1 baseline in [[KPIs and dashboard]]. (Not checked in Quotr's own property: TO CONFIRM.)

**Regex A: the core list from the research notes** ([[geo_content_playbook_b2b|playbook §4]])

```
chatgpt\.com|chat\.openai\.com|perplexity\.ai|gemini\.google\.com|copilot\.microsoft\.com|claude\.ai
```

**Regex B: extended list (recommended).** Adds older and smaller AI tools that third-party GA4 guides include ([Seybold](https://seybold.de/en/guide/ai-traffic-google-analytics-4/); [Swydo](https://www.swydo.com/blog/track-ai-traffic-in-ga4/)).

```
chatgpt\.com|chat\.openai\.com|perplexity\.ai|gemini\.google\.com|bard\.google\.com|copilot\.microsoft\.com|edgeservices\.bing\.com|claude\.ai|deepseek\.com|grok\.com|meta\.ai|mistral\.ai
```

What each part catches:

| Pattern | AI tool |
|---|---|
| `chatgpt\.com`, `chat\.openai\.com` | ChatGPT (new and old web address) |
| `perplexity\.ai` | Perplexity (**not** in GA4's native channel) |
| `gemini\.google\.com`, `bard\.google\.com` | Google Gemini app (and its old name, Bard) |
| `copilot\.microsoft\.com`, `edgeservices\.bing\.com` | Microsoft Copilot (web and inside the Edge browser) |
| `claude\.ai` | Claude |
| `deepseek\.com`, `grok\.com`, `meta\.ai`, `mistral\.ai` | DeepSeek, Grok, Meta AI, Mistral |

The `\.` means "a real dot". Review the list every quarter: look in **Session source / medium** for new AI sources and add them.

**Not caught by any regex:** clicks from **Google AI Overviews and AI Mode**. They come from google.com and look exactly like normal Google organic clicks in GA4 ([Lawrence Hitches](https://www.lawrencehitches.com/google-ai-mode-traffic-ga4/)). Use the Search Console Generative AI report instead (§3).

### 1.4 A saved exploration for the monthly report

1. Go to **Explore → Free form**. Name it `AI referrals – monthly`.
2. Dimensions: **Session source**, **Landing page + query string**, **Session default channel group**.
3. Metrics: **Sessions**, **Engaged sessions**, **Key events**, **Session key event rate**.
4. Filter: **Session source** partially matches regex (Regex B).
5. Rows: Session source. Then a second tab with rows = Landing page.

What to look at each month:
- Sessions by AI source (for the G1 KPI).
- **Landing pages.** Since May 7, 2026, ChatGPT links brand names straight to their homepages, and Profound (a vendor) reports B2B software referrals from ChatGPT up more than 200% after that change ([[verification_geo_evidence|verification claim 6]]). Expect the homepage to be a top AI landing page; make sure it explains Quotr to a first-time visitor.
- Key events from AI sources vs organic search (for KPI G2, "AI-referred demos and signups"; not to be confused with the G2 review site).

### 1.5 Key events (conversions)

1. Go to **Admin → Data display → Events**.
2. Mark as **key events** the events for: demo request ([/book-demo/](https://quotr.ai/book-demo/)), contact form ([/contact-us/](https://quotr.ai/contact-us/)), trial signup ([/sign-up](https://quotr.ai/sign-up)) and, if tracked, the first project created in the app.
3. If these events don't exist yet, a developer needs to add them. **Which events Quotr tracks today is TO CONFIRM with Quotr.**

### 1.6 Data retention

Go to **Admin → Data collection and modification → Data retention** and set event data retention to **14 months** (the longest standard option), so explorations can compare the same month a year later.

---

## 2. UTM and attribution caveats (read before trusting the numbers)

A **UTM tag** is text added to a link (such as `?utm_source=chatgpt.com`) that tells analytics where a visit came from.

| Caveat | What happens | What to do |
|---|---|---|
| **ChatGPT tags its links** | ChatGPT adds `utm_source=chatgpt.com` to links it sends people to ([OpenAI FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq), via the signals notes) | Good for tracking. GA4 then shows source `chatgpt.com` |
| **…often with no medium** | The tag usually has no `utm_medium`, so GA4 records medium `(not set)` and the default channel group may file the visit under "Unassigned" ([Swydo](https://www.swydo.com/blog/track-ai-traffic-in-ga4/); third-party guides) | The custom channel in §1.3 matches on **Source only**, so it catches these visits whatever the medium |
| **Shared links keep the tag** | If someone copies a ChatGPT link and emails it to a colleague, the colleague's visit also counts as ChatGPT | Minor inflation; accept it |
| **Missing referrer** | Visits from AI desktop and mobile apps, in-app browsers, or pasted links can arrive with no referrer and show up as **Direct** ([[geo_content_playbook_b2b\|playbook §4]]) | AI referrals are **undercounted**. Pair GA4 with the self-reported form field (§6) and branded search (§3) |
| **Google AI Overviews and AI Mode** | Clicks look like normal Google organic clicks; GA4 cannot separate them | Use Search Console's Generative AI report (impressions only) |
| **Read-then-search behaviour** | A buyer sees "Quotr.ai" in an AI answer, then later searches "Quotr" or types the URL. GA4 records branded search or Direct, not AI | Track branded search (§3.4) and self-reported source (§6) |
| **Don't tag internal links** | UTM tags on links from one quotr.ai page to another restart the session and wipe the true source | Never put UTM tags on internal links, including links in llms.txt |
| **Do tag links you place on other sites** | Links in the G2 profile, Crunchbase, YouTube descriptions, LinkedIn posts and press releases can carry tags, for example `?utm_source=g2&utm_medium=referral&utm_campaign=profile` | Lets Quotr see which off-site profiles send visits |
| **Paid ChatGPT ads (if ever tested)** | OpenAI's ads sit next to answers, not inside them ([[Quotr GEO AEO strategy audit\|report]]) | Tag ad links with a paid medium (for example `utm_medium=paid-ai`) so they stay separate from organic AI visits |

---

## 3. Google Search Console

### 3.1 Properties and sitemaps (one-off)

1. Add a **Domain property** for `quotr.ai` (verified by DNS). It covers all quotr.ai addresses.
2. Add a second Domain property for **`quotr.io`**, the old domain. It lets Quotr watch and clean up what is still indexed there: `quotr.io/pricing/`, `firetips.quotr.io` and the staging site `test.quotr.io`, which Perplexity still cited for "Quotr.ai pricing" ([[Entity fact sheet]]; [[Website audit]]).
3. Go to **Sitemaps** and submit all three sitemaps:
   - `https://quotr.ai/sitemap.xml`
   - `https://quotr.ai/blog/sitemap.xml` (96 posts; today it is **not listed in robots.txt**, so crawlers that rely on robots.txt only find posts through links)
   - `https://quotr.ai/dictionary/sitemap.xml`
4. Ask the developer to add the blog sitemap to robots.txt and to use real "last updated" dates in the main sitemap (today every page claims it changed "today") ([[Quotr GEO AEO strategy audit|report]], 30-day action 7).

### 3.2 The Generative AI performance report (monthly)

- **What it is:** a report showing how often Quotr's pages appeared in **AI Overviews, AI Mode** and Discover's AI features. It breaks results down by page, country and date (and by device in the Search report). It was announced in June 2026 and reached **all sites worldwide on Aug 31, 2026** ([Google](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports); [SEJ](https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/); verification M1).
- **Where:** under **Performance** in the left menu, the **Generative AI** report ([Search Console help](https://support.google.com/webmasters/answer/16984139?hl=en)).
- **Limits:** impressions only. **No clicks, no click-through rate, no queries.** The numbers are a filtered view of the normal Web data, so **don't add them to Web totals** (verification M1).
- **Each month, export:** total AI impressions; the top 10 pages by AI impressions; the change vs last month. Watch whether fixed pages (pricing, /disambiguation/) and new data or tool pages move up.

### 3.3 Do NOT opt out

Search Console also has a **"Search generative AI" control** that removes a site from AI Overviews, AI Mode and Discover's AI features ([Search Console help](https://support.google.com/webmasters/answer/16908024?hl=en); verification M1). **Quotr should not use it.** The report is explicit: Quotr needs the visibility.

### 3.4 Branded search (monthly; trend reviewed quarterly)

- **Option 1: the branded queries filter.** Google introduced a filter for branded vs non-branded queries in November 2025 and made it available to **all eligible sites** on March 11, 2026 ([Google](https://developers.google.com/search/blog/2025/11/search-console-branded-filter); [Search Engine Land](https://searchengineland.com/google-search-console-branded-queries-filter-expands-471387)). It may not appear for smaller sites.
- **Option 2: a regex filter.** In **Performance → Search results**, add a **Query** filter → **Custom (regex)** → `quotr`. Record clicks and impressions.
- **Watch for namesakes.** Some "quotr" searches are for other products, such as the Quotr Pro app ([[Quotr GEO AEO strategy audit|report]]). Look at the top queries and exclude obvious namesake ones (for example add a second filter: Query → doesn't match regex → `quotr pro`).
- The playbook suggests a **quarterly** branded-search trend review ([[geo_content_playbook_b2b|playbook §4]]).

### 3.5 After fixing pages: ask Google to re-read them

After the old Solo/Team pricing is removed from the ~13 affected URLs ([[Optimize vs create]]):
1. Paste each fixed URL into **URL Inspection** and click **Request indexing**.
2. Note the date. Next month, check the "last crawl" date and whether branded AI answers now quote **$79.90**. That is the report's first proof point.
3. In the `quotr.io` property, use **Removals** for any `test.quotr.io` URLs that are still indexed, and make sure the staging site stays `noindex` and behind its login.

---

## 4. Bing Webmaster Tools (and why Bing matters)

### 4.1 Why Bing matters

- **Copilot is built on Bing's index.** If a page isn't in Bing, Copilot and Bing's AI answers can't use it ([[How AI engines choose sources]]).
- **ChatGPT** says it gets some results from "third-party search providers". OpenAI has not said publicly which ones. Bing is often assumed, but that is **not confirmed** ([[geo_ai_citation_signals_2026|signals notes §1]]). Being well indexed in Bing is cheap insurance either way.
- **Claude** web search is linked to **Brave Search** (Brave is the search provider named in Anthropic's subprocessor list; not confirmed as "the index") ([[verification_geo_evidence|verification claim 29]]). Brave has no equivalent of Bing Webmaster Tools; a quarterly check of `site:quotr.ai` on [search.brave.com](https://search.brave.com/) is enough.
- Bing Webmaster Tools gives **first-party AI citation data** for free, which Google does not (Google shows impressions only).

### 4.2 Setup (one-off)

1. Sign in at [bing.com/webmasters](https://www.bing.com/webmasters) and choose **Import from Google Search Console** (fastest), or add `https://quotr.ai` and verify it.
2. Submit the same three sitemaps as in §3.1.
3. Turn on **IndexNow** so Bing hears about changed pages immediately. Quotr already uses Cloudflare, whose free **Crawler Hints** setting sends IndexNow signals: in the Cloudflare dashboard, turn on Crawler Hints (under Caching → Configuration) ([Cloudflare docs](https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/)). IndexNow is supported by Bing and some other engines, not Google ([[How AI engines choose sources]]).
4. After the pricing fix, also submit the fixed URLs with Bing's **URL Submission** tool.

### 4.3 The AI Performance report (monthly)

- **What it is:** a **public preview** report announced on Microsoft's blog on **February 10, 2026** ([Bing](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview); verification claim 3). Some coverage dates it February 11.
- **What it shows:** how many times Copilot and Bing AI answers **cited** Quotr's pages, **which pages**, and the **"grounding queries"**: the search phrases Copilot generated behind the scenes to find content ([[geo_ai_citation_signals_2026|signals notes §1]]; [Bing](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)).
- **Limits:** summary data only. It does not show individual answers, exact user prompts, or why a page was chosen.
- **Each month, export:** total citations, number of cited pages, top 10 cited pages, top 10 grounding queries. Grounding queries are a free source of **real question wording** for [[Prompt library]].

---

## 5. AI crawler checks (Cloudflare and server logs)

### 5.1 Why check

AI engines can only cite pages their crawlers can fetch. Quotr's robots.txt lets every bot in (`User-agent: *` / `Allow: /`). But the site sits behind **Cloudflare**, which has separate switches that can block or challenge bots. From outside, the research could not see whether they are on ([[Quotr GEO AEO strategy audit|report]]; [[Website audit]]). The report lists "Confirm Cloudflare is not blocking AI search bots" as a first-30-days task.

What is known today:
- **Cloudflare AI Labyrinth is on.** Every checked page has a hidden, `nofollow` link to `/cdn-cgi/content?id=…`. It is a trap that leads bots which **ignore crawl rules** into AI-generated decoy pages. It should not affect well-behaved crawlers ([[quotr_onsite_content_audit|onsite notes §1]]; [Cloudflare docs](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/)). Keep it, but confirm it was switched on deliberately.
- **Unknown:** whether Cloudflare's **"Block AI bots"** or **managed robots.txt** settings are on. Because robots.txt has not been rewritten, they are **probably off**, but this is **TO CONFIRM with Quotr** ([[quotr_onsite_content_audit|onsite notes §1]]).
- **Why it's worth checking:** since **July 1, 2025**, Cloudflare asks every new domain whether to allow AI crawlers, and blocks AI crawlers by default for new domains ([Cloudflare press release](https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/)). When quotr.ai was added to Cloudflare, and what was chosen, is **TO CONFIRM with Quotr**. Perplexity citing quotr.ai pages suggests at least PerplexityBot gets through.

### 5.2 Step by step in Cloudflare (whoever owns the Cloudflare account)

1. Log in to Cloudflare and select the **quotr.ai** zone.
2. Open **AI Crawl Control** (Cloudflare's dashboard for AI bots; it replaced the earlier "AI Audit") ([Cloudflare blog](https://blog.cloudflare.com/introducing-ai-crawl-control/); [docs](https://developers.cloudflare.com/ai-crawl-control/)).
3. **Overview tab:** note total AI crawler requests, the most common status code, the most popular paths, and requests grouped by company (OpenAI, Microsoft, Google, Anthropic, and others) for the last 30 days ([Cloudflare docs](https://developers.cloudflare.com/ai-crawl-control/features/analyze-ai-traffic/)).
4. **Crawlers tab:** check the **Actions** column. Every bot in the table in §5.4 marked "Allow" should be **allowed**, not blocked or set to charge ([Cloudflare docs](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)).
5. Look at requests by **path pattern** (for example `/blog/*`, `/pricing/`). Are the blog and pricing pages being crawled?
6. In the bot and security settings, check:
   - **Block AI bots:** off.
   - **Managed robots.txt:** off, or not disallowing the bots Quotr wants.
   - **AI Labyrinth:** on is fine.
   - Any **bot protection mode, firewall (WAF) custom rule or rate limit** that challenges or blocks verified bots: none should hit the bots in §5.4.
7. Take a screenshot of the Overview and Crawlers tabs for the monthly file.

### 5.3 If server logs are available (developer)

Where quotr.ai is hosted, and whether raw access logs are kept, is **TO CONFIRM with Quotr** (the site is built with Astro and served through Cloudflare). If logs exist, these commands give a quick monthly count. They assume a standard "combined" log format, where the status code is the 9th field.

```
# 1. Requests per AI bot this month
grep -E -o -i "OAI-SearchBot|ChatGPT-User|GPTBot|PerplexityBot|Perplexity-User|Claude-SearchBot|Claude-User|ClaudeBot|bingbot|Googlebot|Applebot|CCBot" access.log | sort | uniq -c | sort -rn

# 2. Status codes one bot received (repeat per bot; 200 = good, 403/429/503 = blocked, limited or challenged)
grep -i "OAI-SearchBot" access.log | awk '{print $9}' | sort | uniq -c

# 3. Which pages one bot fetched most
grep -i "PerplexityBot" access.log | awk '{print $7}' | sort | uniq -c | sort -rn | head -20

# 4. Did anyone fetch llms.txt?
grep "/llms.txt" access.log | wc -l
```

**Beware fake bots.** Anyone can pretend to be "GPTBot" in a user-agent. Cloudflare labels bots it has verified; some AI companies (such as OpenAI) also publish the addresses their crawlers use ([OpenAI crawler docs](https://developers.openai.com/api/docs/bots)). Trust Cloudflare's verified counts over raw log counts.

### 5.4 AI crawler user-agents to watch

"User-agent" is the name a bot gives when it visits. Recommendations from [[How AI engines choose sources]].

| Company | User-agent | What it does | Quotr should |
|---|---|---|---|
| OpenAI | **OAI-SearchBot** | Finds pages for ChatGPT search results and citations. OpenAI: don't block it if you want to appear | **Allow** (most important) |
| OpenAI | **ChatGPT-User** | Fetches a page live when a ChatGPT user's question needs it. OpenAI says robots.txt rules may not apply to it | **Allow** |
| OpenAI | **GPTBot** | Collects training data | **Allow** (Quotr wants to be in the models' memory) |
| OpenAI | **OAI-AdsBot** | Checks landing pages of ChatGPT ads | Only relevant if Quotr runs ChatGPT ads |
| Google | **Googlebot** | Builds Google's index, which feeds AI Overviews, AI Mode and Gemini's search grounding | **Allow** |
| Google | **Google-Extended** (a robots.txt control, not a separate bot) | Controls use of content for Gemini training and Gemini app grounding; does not affect Search or AI Overviews | **Allow** |
| Microsoft | **bingbot** | Builds Bing's index, which feeds Copilot | **Allow** |
| Anthropic | **Claude-SearchBot** | Indexes content for Claude's search results | **Allow** |
| Anthropic | **Claude-User** | Fetches a page when a Claude user's question needs it | **Allow** |
| Anthropic | **ClaudeBot** | Collects training data | **Allow** |
| Perplexity | **PerplexityBot** | Builds Perplexity's index | **Allow** |
| Perplexity | **Perplexity-User** | Fetches pages live for a user's question | **Allow** |
| Apple | **Applebot** (crawler); **Applebot-Extended** (robots.txt control for Apple AI training) | Apple search and AI features | **Allow** |
| Common Crawl | **CCBot** | Open web crawl that many AI models train on | **Allow** |

### 5.5 How to read crawler numbers

- **Crawling is not the same as being cited.** Cloudflare-based figures (July 2026, secondary summary) put ClaudeBot at about 2,237 crawls per referral and GPTBot at about 217, against about 4.6 for Google ([[geo_content_playbook_b2b|playbook §4]]). Lots of bot hits don't mean lots of visits.
- **What matters:** (1) wanted bots get **200** responses; (2) **key pages** (blog posts, /pricing/, /disambiguation/, new data and tool pages) get crawled; (3) fixed pages are **re-crawled soon after the fix**.
- **llms.txt:** expect few or no AI-bot requests. An Ahrefs study of 137K domains reportedly found 97% of llms.txt files got no requests in a month (not re-checked by the fact-check) ([[geo_content_playbook_b2b|playbook §4]]).

---

## 6. "How did you hear about us?" field

Analytics misses much of AI's influence (see §2). Asking people directly catches it. The playbook recommends a **required** field on demo and trial forms, plus tagging AI-sourced deals in the CRM ([[geo_content_playbook_b2b|playbook §4]]).

### 6.1 Where

- [/book-demo/](https://quotr.ai/book-demo/): **required**.
- [/contact-us/](https://quotr.ai/contact-us/): required.
- [/sign-up](https://quotr.ai/sign-up) (7-day trial): add it to the signup flow or the first onboarding screen. If making it required hurts signups, make it optional there (our suggestion; test it).

Which form tool and CRM Quotr uses is **TO CONFIRM with Quotr**.

### 6.2 The question and options (copy-paste)

**Question:** "How did you first hear about Quotr?" (single choice)

| Option (shown to the buyer) | Why it's there |
|---|---|
| ChatGPT | Largest AI assistant |
| Google search results | Classic search |
| Google AI answer (AI Overview, AI Mode or Gemini) | Separates Google's AI from classic search |
| Perplexity | Only engine with a baseline |
| Another AI assistant (Claude, Copilot or other) | Catch-all for AI |
| YouTube | Video is a key channel in the plan |
| Reddit | r/estimators is cited by AI |
| Facebook group | Estimator groups |
| LinkedIn | Founder presence |
| Review site (G2, Capterra or similar) | Review drive |
| Industry article, newsletter or podcast | Press and podcast |
| Trade show or event | Offline channel |
| Colleague or friend | Word of mouth |
| Other (please tell us) | Free text |

**Optional follow-up** (shown only if an AI option is picked): "What did you ask the AI? (optional)". This captures real buyer wording for the prompt library. The Semrush measurement guide mentions form tools such as Tally that let users type the query they used ([[geo_content_playbook_b2b|playbook §4]]).

### 6.3 Make it usable

1. Save the answer into a **CRM field** (for example "Self-reported source") on the contact and the deal.
2. Also save, in hidden form fields, the **first-touch source/medium and landing page** from the visit, so each lead has both what analytics saw and what the buyer said (our suggestion).
3. Ask sales to repeat the question on the first call and correct the field if needed.
4. Each month, count answers by option for the G4 KPI in [[KPIs and dashboard]]. Within one or two quarters this should be Quotr's best evidence of which channels matter (playbook inference).

---

## 7. Monthly manual prompt test (the routine)

The full method, all 53 prompts and the templates are in [[Tracking set]]. This is the checklist version.

**When:** the first week of each month, same days each time (for example the first Tuesday–Thursday). First multi-engine run: **early October 2026**.

**Monthly checklist**

1. **Prepare:** copy last month's run-log sheet. Note any pages fixed or published last month and which prompts they should affect.
2. **Sessions:** use logged-out, temporary or clean sessions; run from a US location; one new chat per prompt; no follow-up questions (except "search the web" for ChatGPT, which you note down).
3. **Run the prompts** (choose one level):
   - **Lite (about 3 hours):** the 23 Tier A prompts once each in ChatGPT, Google AI Mode and Perplexity; note whether Google shows an AI Overview; all 53 prompts twice through the Perplexity Sonar API (scripted) to compare with September.
   - **Standard (10–15 hours by hand, or use a tool):** Tier A twice and Tier B once, in ChatGPT, Google AI Mode / AI Overviews, Perplexity and Gemini.
   - **Quarterly add-on:** Claude and Copilot, all prompts once.
4. **Record** for every run: engine and model shown, Quotr named (Y/N), position, how Quotr is described, sentiment, accuracy problems (checklist in [[Tracking set|Tracking set §3.6]]), quotr.ai URLs cited, retrieved-only URLs, competitors named, top cited domains, third-party pages naming Quotr, screenshot or share link.
5. **Score** with the formulas in [[Tracking set|Tracking set §3.7]]: mention rate, citation rate, retrieval rate, cited-not-named count, share of voice, average position, brand accuracy. **One row per engine; never blend engines.** Use the first run for headline numbers and the second to flag "unstable" results.
6. **Log new third-party pages** that name Quotr in [[Off-site presence]].
7. **Add first-party data:** Search Console AI impressions, Bing AI citations, GA4 AI sessions and key events, form answers, Cloudflare crawler status.
8. **Fill the dashboard** in [[KPIs and dashboard|KPIs and dashboard §6]] and write the 5-line monthly note ([[Tracking set|Tracking set §4.4]]).

**Why monthly, not weekly:** AI citations change a lot from month to month and changes take weeks to show, so weekly prompt checks mostly measure noise ([[geo_content_playbook_b2b|playbook §4]]).

**Where to keep it (suggested):** one shared spreadsheet called "Quotr GEO tracking" with tabs: `Run log` (one row per run), `Monthly summary` (one row per engine per month), `Prompt trend` (Tier A prompts by month), `Dashboard`, `Change log` (pages fixed or published, tool or engine changes).

---

## 8. Reporting cadence

| Cadence | Time (estimate) | What to check | Output |
|---|---|---|---|
| **Weekly** (e.g. Monday) | 15–30 min | GA4 AI sessions and key events (anything unusual?); Cloudflare AI Crawl Control (any wanted bot blocked or erroring?); new G2 reviews; new mentions of "Quotr.ai" (set a free Google Alert); any fixes shipped that need a re-crawl request. **Don't re-run prompts weekly** | A 3-line Slack or email note, only if something changed |
| **Monthly** (first week) | Half a day (Lite) to 2 days (Standard, by hand) | Full prompt test (§7); Search Console Generative AI report and branded search; Bing AI Performance; GA4 AI channel and landing pages; form answers; reviews and list inclusions; crawler health; re-score [[Presence scorecard]] | Monthly dashboard ([[KPIs and dashboard\|KPIs and dashboard §6]]) plus the 5-line note |
| **Quarterly** | 1 day | 3-month trends by engine, including the presence-scorecard trend; Claude and Copilot runs; branded-search trend; AI vs organic conversion comparison; swap in up to 5 new prompts ([[Tracking set\|Tracking set §5]]); update the GA4 regex with new AI sources; review tool choice and budget ([[AI visibility tools compared]]); review targets | Quarterly review deck or doc for Quotr leadership |
| **Day-90 review** (late December 2026) | Half a day | Compare against the 90-day targets in [[KPIs and dashboard\|KPIs and dashboard §4]]; decide the next quarter's priorities | Short decision memo |

### First three months (suggested calendar)

| When | Measurement milestone |
|---|---|
| Late Sept – mid Oct 2026 | Complete setup §1–§6; pull GA4 AI history for Jan–Sep 2026 |
| Early Oct 2026 | First multi-engine prompt test = **October baseline** for ChatGPT, Google AI Mode / AI Overviews, Gemini |
| Early Nov 2026 | Second run; set engine-specific targets from October; check whether branded answers now quote $79.90 after the pricing fix |
| Early Dec 2026 | Third run; first 3-month view for Perplexity (Sep–Dec) |
| Late Dec 2026 | Day-90 review |

---

## 9. Open questions (TO CONFIRM with Quotr)

- Who has admin access to GA4, Search Console, Bing Webmaster Tools, Cloudflare, the website forms and the CRM?
- Is GA4 installed on both the marketing site and the app's sign-up flow? Which key events exist?
- When was quotr.ai added to Cloudflare, and are "Block AI bots" and managed robots.txt off? Is AI Labyrinth intentional?
- Where is the site hosted, and are raw access logs kept?
- Which form tool and CRM are used, and can a required source field be added?
- Is quotr.io a 301 redirect to quotr.ai or a mirror? (Affects which Search Console property shows what.)

---

## Related pages

- [[KPIs and dashboard]] — KPI definitions, September 2026 baseline, suggested targets and the monthly dashboard
- [[AI visibility tools compared]] — paid AI-visibility trackers vs the free manual routine
- [[Tracking set]] — the 53 tracked prompts, run rules and templates
- [[AI visibility baseline]] — September 2026 results and method
- [[Website audit]] — robots.txt, sitemaps, Cloudflare and staging-site findings
- [[How AI engines choose sources]] — how each engine finds pages, and the full crawler table
- [[Traffic and funnel impact]] — why AI traffic is undercounted and reach is measured as presence
- [[30-60-90 plan]] — where measurement setup sits in the plan
