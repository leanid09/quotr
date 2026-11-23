# Traffic, Inbound Measurement and Attribution Operating Manual for Leanid's 90-Day Quotr Engagement (Nov 30, 2026 – Feb 27, 2027)

**Scope:** How Leanid's agency should get access to, baseline, attribute and report Quotr.ai's website traffic and inbound leads during a 90-day GEO/AEO/SEO engagement. It also covers how to set up KPIs so the agency is judged fairly when Quotr asks it to "own growth metrics and TOFU performance".

**Builds on, does not repeat:** `geo-brain/07-measurement/kpis-and-dashboard.md` (KPI tree L1–L10 / G1–G5, Sept 2026 Perplexity baseline, monthly dashboard), `tracking-setup.md` (GA4 regex A/B, GSC, Bing, Cloudflare, HDYHAU options, monthly cadence) and `tools-comparison.md` (Sept 2026 tool prices). Those pages were written for an in-house monthly GEO programme starting in October 2026. This file adds what a contractor needs: access roles, a June–October baseline with seasonality corrections, weekly cadence, attribution set-up as of November 2026, lead-quality definitions, ways to separate effects from confounders, and how to structure accountability.

**Research conditions (read first):**
- **quotr.ai could not be fetched in this session** (proxy refused the connection and WebFetch could not resolve it). Quotr's live tag stack (GA4 ID, GTM container, Clarity, HubSpot or another CRM, form tool) is **not verified**. The prior audit found the site is built with **Astro** and served through **Cloudflare**, not Webflow, WordPress or Framer (`geo-brain/02-current-state/website-audit.md`; `geo-brain/00-quotr/entity-fact-sheet.md`).
- The official doc hosts **support.google.com, learn.microsoft.com, blogs.bing.com and developers.cloudflare.com were blocked for direct fetch.** Findings about them come from search-result extracts of those pages and from secondary coverage. Each finding is labelled. Confirm menu names in the live products.
- Engagement calendar (computed): **Day 1 = Mon Nov 30, 2026; Day 30 = Tue Dec 29; Day 60 = Thu Jan 28, 2027; Day 90 = Sat Feb 27, 2027.** There are 13 Friday reviews: Dec 4, 11, 18, **25 (Christmas)**, **Jan 1 (New Year's Day)**, 8, 15, 22, 29, Feb 5, 12, 19, 26. Thanksgiving is Thu Nov 26, 2026, the week before Day 1. The baseline window Jun 1 (Mon) – Oct 31 (Sat) 2026 is 153 days. Use the 22 full weeks from Jun 1 to Nov 1.
- Labels used below: **[Known]** = documented by the vendor or confirmed by several sources. **[Likely]** = credible secondary reporting or strong inference. **[Speculative]** = plausible but unverified.

---

## Q1. Day-1 access checklist: which tools, which permission level, minimum role

### Takeaway
Ask for **least-privilege, named-user access to the agency's own Google/Microsoft accounts**, never shared logins. In practice that means **GSC Full user** (not Owner), **GA4 property Editor** (Editor is needed for custom channel groups and Analyst is not enough), **GTM container Publish only if the agency will ship tags** (otherwise Edit), **Bing Webmaster Tools Read/Write**, **Cloudflare AI Crawl Control Read Only** (a role added Jan 13, 2026), **Clarity Team member**, read access to the **CRM** with permission to create properties, and **Git repo access** for the Astro site. Quotr should stay the owner of every asset.

### Cited Findings
**Google Search Console**
- Owners have full control and are the only users who can add or remove users. **Full users** "have view rights to all data and can take some actions." Restricted users have limited views. The **Settings → Users and permissions** page is visible only to owners. [Known] — [Google Search Console Help: Managing owners, users, and permissions](https://support.google.com/webmasters/answer/7687615?hl=en) (via search extract; page not directly fetchable)
- A third-party guide's per-feature table says Full users can use URL Inspection with **Request indexing** and can **submit removals**. Restricted users get fetch-only inspection and view-only removals. [Likely; Google's own per-feature table was garbled in extracts] — [GSC Help extract](https://support.google.com/webmasters/answer/7687615?hl=en)
- Google separates **verified owners** from **delegated owners**, and since 2023 owners can change a delegated owner's level (owner, full, restricted). A user who sees "Delegated Owner" but has no Users and Permissions option "is probably a Full User." Some linked products require a verified owner. [Known] — [Google Search Central blog, Feb 2023](https://developers.google.com/search/blog/2023/02/search-console-user-permissions-update)

**GA4**
- GA4 roles are Administrator, Editor, Marketer, Analyst and Viewer (plus None), with optional data restrictions (no cost metrics, no revenue metrics). Editor has full control of settings at property level but cannot manage users. [Known] — [GA4 Help: Access and data-restriction management](https://support.google.com/analytics/answer/9305587?hl=en) (search extract)
- Creating, editing or deleting **custom channel groups requires Editor or Administrator** at property level. Marketer adds audiences, key events/conversions and custom events on top of Analyst. [Likely; third-party, not stated on Google's channel-group page] — [MeasureU](https://measureu.com/google-analytics-permissions); [Jellyfish](https://www.jellyfish.com/en-gb/training/blog/ga4-user-permissions-explained)
- The data-retention setting **only affects Explorations and funnel reports, not standard aggregated reports**. Exploration date ranges beyond the retention window show no data. Options are **2 or 14 months** for standard properties. Sources conflict on the default (University of Colorado guide says 2 months; Usercentrics says 14). [Known for scope; default conflicting] — [GA4 Help: Data retention](https://support.google.com/analytics/answer/7667196?hl=en); [CU Boulder](https://www.colorado.edu/webcentral/resources/website-analytics-transition-google-ga4/data-retention); [Usercentrics](https://usercentrics.com/us/guides/privacy-led-marketing/ga4-data-retention/)

**Bing Webmaster Tools**
- Bing WMT has three user levels: **Administrator, Read/Write (Read/Modify), Read only**. "Read only … can see everything but change nothing." Bing warns that "even an Admin making a mistake can result in an entire site being blocked from our index" and recommends most users be **Read/Modify**. [Likely; sources are 2011–2012, current UI unverified] — [Bing Webmaster blog, Aug 2011](https://blogs.bing.com/webmaster/August-2011/Help-protect-yourself-from-accidental-index-remova); [SEJ](https://searchenginejournal.com/bing-adds-user-levels-to-webmaster-tools/32286)
- The invited user must **accept the delegation** in their own Bing WMT account before access becomes active. [Likely] — [devleader.ca Bing WMT MCP docs](https://www.devleader.ca/projects/bing-webmaster-mcp/tools/add-site-role)

**Cloudflare**
- **AI Crawl Control Read Only role (added Jan 13, 2026):** assigned by an account admin under **Manage Account → Members**, at domain level. Holders can view the **Overview, Crawlers, Metrics, Robots.txt and Settings** tabs but cannot change crawler actions or settings. Other dashboard areas still need their own permissions. [Known] — [Cloudflare changelog, 2026-01-13](https://developers.cloudflare.com/changelog/2026-01-13-ai-crawl-control-read-only-role/) (search extract)
- Referrer analytics in AI Crawl Control ("view top referrers driving traffic to your site") is listed as a **Paid plans** feature. [Known] — [Cloudflare changelog, 2025-10-14 enhanced metrics drilldowns](https://developers.cloudflare.com/changelog/2025-10-14-enhanced-metrics-drilldowns/)

**Microsoft Clarity**
- Clarity has two project roles. **Admin** can change roles, add and remove members, delete the project and manage settings. **Team member** can view and share heatmaps, view recordings and save segments. No Viewer role was found. [Known] — [Clarity docs: Team management](https://learn.microsoft.com/en-us/clarity/team-management) (search extract)
- The **Bot Activity** dashboard is enabled by a **project admin connecting a supported CDN in Project Settings**. [Known] — [Clarity docs: Bot activity](https://learn.microsoft.com/clarity/ai-visibility/bot-activity) (search extract)

**Site/CMS**
- quotr.ai is built with **Astro** (server-rendered; `/_astro/` assets). /disambiguation/ is hand-written static HTML. The site is served through Cloudflare. [Known as of 2026-09-25] — `geo-brain/02-current-state/website-audit.md`; `research_notes/Quotr GEO AEO strategy audit/quotr_onsite_content_audit.md`

### Inferences
**Day-1 access checklist (send to Quotr before Nov 30; owner = Quotr unless noted)**

| # | System | Ask for (minimum role) | Why that role, not more or less | Who grants | Status by Fri Dec 4 |
|---|---|---|---|---|---|
| 1 | **Google Search Console**: Domain property `quotr.ai` (+ `quotr.io` if verified) | **Full user** for the agency's named Google account | Full user covers all data, URL Inspection/Request indexing, sitemaps and removals. Owner adds nothing the agency needs and lets it add or remove users, which Quotr should keep. Ask for **delegated owner only** if the agency must link GSC↔GA4 itself and no Quotr owner is available. A Quotr verified owner can do that link in 2 minutes | Quotr verified owner | ☐ |
| 2 | **GA4** property for quotr.ai (and the app/sign-up stream if separate) | **Editor at property level** (not account Administrator). Accept "No cost metrics" restriction if Quotr wants | Editor is needed to build the custom AI channel group, mark key events, set data retention, create custom dimensions for hidden-field data. Analyst cannot. Do not request user-management rights | Quotr GA4 Administrator | ☐ |
| 3 | **GA4 ↔ GSC link**, **GA4 ↔ Google Ads link** | Read status only | Needed to see Search Console reports inside GA4 and to see paid spend that may confound | Quotr | ☐ |
| 4 | **Google Tag Manager** container (if GTM is used; unverified) | **Edit** if Quotr's developer publishes; **Publish** only if the agency ships tags (hidden-field capture, Clarity, form events). Unverified in this session: GTM container permissions are normally Read / Edit / Approve / Publish | Every tag change is a measurement confounder, so publishing should be logged with version notes | Quotr GTM admin | ☐ |
| 5 | **Bing Webmaster Tools** | **Read/Write** (Read/Modify). Agency must accept the invite | Read/Write is needed for sitemap and URL submission. Admin is unnecessary and Bing itself warns against it | Quotr BWT admin | ☐ |
| 6 | **Cloudflare** zone quotr.ai | **AI Crawl Control Read Only** (+ read-only Analytics/Security analytics if available on Quotr's plan) | Enough to monitor bots, status codes, paths and referrers. Changes to bot rules stay with Quotr's engineer under a change log. Also record Quotr's **plan tier**, because referrer analytics is Paid-plan only | Quotr Cloudflare account admin | ☐ |
| 7 | **Microsoft Clarity** | **Team member**. Ask the **Admin** to connect the Cloudflare CDN for Bot Activity (or grant Admin temporarily for that step) | Team member covers dashboards, recordings and segments. CDN connection is admin-only | Quotr Clarity admin | ☐ |
| 8 | **CRM** (HubSpot assumed but **unverified**) | Read all contacts/deals + **create/edit properties** + create reports/dashboards. No delete, no export-all unless needed | Lead-quality fields and source fields must be added. Pipeline must be visible to judge outcomes | Quotr RevOps/CEO | ☐ |
| 9 | **Form + scheduler stack** (/book-demo/, /contact-us/, /sign-up, Estimation Service upload, Procurement inquiry) | Edit access, or a named Quotr dev with a 48-h SLA | Needed to add HDYHAU field and hidden UTM/referrer fields | Quotr dev | ☐ |
| 10 | **Website repo (Astro)** + deploy pipeline + any headless CMS | Git write via pull requests (branch protection on), preview deploy access | The site is code, not a hosted CMS. Every deploy is a dated change that belongs in the change log | Quotr dev lead | ☐ |
| 11 | **Server/edge logs** | Whatever exists: Cloudflare Logpush/Log Explorer if on plan; host logs otherwise | Raw logs are the only way to verify user-triggered fetches per URL beyond Cloudflare's dashboards | Quotr | ☐ |
| 12 | **Ad platforms** (Google Ads, LinkedIn, Meta, Capterra/G2 paid) | Read-only | Paid spend, especially brand bidding, is a confounder on branded clicks and on demo volume | Quotr | ☐ |
| 13 | **Sales activity data** (outbound sequences in HubSpot/Apollo/Outreach; unverified) | Read-only or a weekly export | Separating inbound from outbound-touched leads | Quotr sales | ☐ |
| 14 | **Prompt tracker** (if bought) | Agency-owned account with Quotr as viewer, or Quotr-owned with agency as admin | Decide who owns history if the engagement ends. Export rights must be in writing | Contract | ☐ |
| 15 | **Release/launch calendar** (product, pricing, PR, events, webinars, funding news) | Shared doc / Slack channel | Confounder log | Quotr marketing (Jaron/Jati/Mia/Jenny) | ☐ |

**Access-hygiene rules (contract annex):** named accounts only. Quotr keeps ownership of all properties and data. Agency access is removed at end of engagement. Agency changes to GA4/GTM/Cloudflare/forms go into a shared **change log** with date and time. The day-90 "data export pack" (GSC, GA4 and BWT exports, prompt-tracker CSV, CRM report definitions) is a deliverable.

### Gaps
- Quotr's actual tag stack, CRM, form tool, Cloudflare plan and whether GTM is used could not be verified (quotr.ai unreachable from this session). Day-1 discovery task: view-source of /, /book-demo/, /sign-up, and run Tag Assistant.
- GTM permission names (Read/Edit/Approve/Publish) and current Bing WMT role names were not re-verified from live docs this session.
- Which Cloudflare role is needed for the separate **Attribution Business Insights** dashboard (crawl-to-referral ratio), and its plan availability, was not found.
- Which CDNs Clarity Bot Activity supports (Cloudflare assumed) was not confirmed. The doc host was blocked.

---

## Q2. Baseline methodology for June–October 2026, with seasonality and a December start

### Takeaway
A plain "June–October average vs. December–February average" comparison is biased **against** the agency. The engagement's first month is the construction and B2B holiday trough. The baseline window contains a core update, a pricing change and a ChatGPT tracking outage. Build a **weekly baseline with a range (band)**, flag anomalous weeks, and **seasonally adjust** with last winter's GSC data and category-demand trends. Judge Day-90 on Feb 2027 (and the Jan 4 – Feb 26 window), not on December.

### Cited Findings
- **Construction seasonality:** contractor work "tends to thin out from October into January". A slowdown starting around December means winter work is sold in August–September. [Likely; contractor-ops source, not software buying] — [Projul](https://projul.com/blog/construction-seasonal-slowdown-guide/)
- For companies selling implementation-heavy software, the high-intensity construction months "can actually be the worst time to close deals". This is a qualitative claim. [Speculative/qualitative] — [Foundamental: AEC industry seasonality](https://www.foundamental.com/perspectives/navigating-the-seasons-unraveling-aec-industry-cycles-and-strategies)
- Construction-software demand in 2026 is soft at the top of the market. Procore's CEO: "we are operating in a demand environment that has become more challenging", with "deal slippage" in the final weeks of Q3. [Known, company-specific] — [Finviz/StockStory on Procore Q3](https://finviz.com/news/219846/procore-technologiess-nyse-pcor-q3-sales-beat-estimates-but-customer-growth-slows-down). L.E.K. (Feb 2026): construction-software performance "will not be uniform" and depends on where activity persists in the construction life cycle — [L.E.K.](https://www.lek.com/insights/industrial/construction-software-during-recession-what-can-we-expect)
- **Google core updates in or next to the windows:** March 2026 (Mar 27 – Apr 8), **May 2026 (May 21 – Jun 2, overlaps baseline days 1–2)**, and **November 2026 (started Nov 10, 2026, ~1:07 pm ET; "may take up to two weeks")**. Coverage notes the last two November core updates ran **longer than three weeks** (Nov 2024 took ~23 days), so the rollout could run into **early-to-mid December**. Google has said nothing about what changed. [Known for start; end date unconfirmed as of Nov 23] — [Search Engine Land](https://searchengineland.com/google-november-2026-core-update-rolling-out-now-501348); [SEJ](https://www.searchenginejournal.com/google-november-2026-core-update/596614/); [SERoundtable](https://www.seroundtable.com/google-november-2026-core-update-42504.html); [seo-kreativ](https://www.seo-kreativ.de/en/blog/google-november-2026-core-update/); [Google Search Status Dashboard](https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history)
- Google's core-update guidance: wait **at least a full week after completion**, then compare Search Console data for that week with the week before rollout began. [Known, via secondary quote of Google doc] — [seo-kreativ](https://www.seo-kreativ.de/en/blog/google-november-2026-core-update/)
- A **Search Console generative-AI reporting/logging error lowered impressions Nov 9–11, 2026**, per coverage. [Likely; secondary] — [aieatingtheworld](https://www.aieatingtheworld.com/articles/google-november-2026-core-update); [Keywords Everywhere](https://keywordseverywhere.com/news/google-algorithm-updates/november-2026-core-update/)
- **ChatGPT tracking outage Oct 8–15, 2026 (inside the baseline):** ChatGPT outbound links reportedly stopped carrying `utm_source` and passed referrers unreliably after the GPT-6 release ("noopener,noreferrer"), so clicks logged as Direct. Tags reportedly returned around Oct 15, but referrers are still missing on many clicks. First diagnosed publicly by Adobe's Cedric Huesler; reportedly later called a bug by OpenAI. [Likely; secondary blogs] — [Relevant Audience](https://www.relevantaudience.com/analytics/chatgpt-gpt-6-utm-referrer-dropped-direct-traffic/); [ALM Corp](https://almcorp.com/news/chatgpt-bug-sent-ai-referral-traffic-to-direct-after-gpt-6/); [sitebrunch](https://www.sitebrunch.com/en/news/chatgpt-referrer-utm-source-missing)
- **Measurement changes inside the baseline window:** GA4's native **AI Assistant channel launched May 13, 2026**. It is forward-only and does not reclassify earlier traffic ([Seer Interactive](https://www.seerinteractive.com/insights/are-ai-sites-like-chatgpt-sending-your-website-traffic); `tracking-setup.md` §1.1). The **GSC Generative AI report** launched in beta **June 3, 2026** and reached **all sites Aug 31, 2026** ([crawlraven](https://crawlraven.com/blog/gsc-ai-performance-reports); [Google](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)). **Bing AI Performance** added Intents, Topics, Citation Share and Compare on **June 16, 2026**, and Topics Portfolio (beta) on **Oct 13, 2026** ([Bing blog June 2026](https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/); [Bing blog Oct 2026](https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/); [Search Engine Land](https://searchengineland.com/bing-webmaster-tools-ai-performance-report-new-topics-portfolio-495584))
- **Quotr-side changes inside the baseline:** new software pricing (Lite $79.90 / Plus $299.90 per seat / Enterprise) announced **Sep 14, 2026** — `geo-brain/00-quotr/entity-fact-sheet.md`. ChatGPT began linking brand names to homepages on **May 7, 2026** (vendor data) — `geo-brain/07-measurement/tracking-setup.md` §1.4.
- GA4 custom channel groups reportedly **apply to historical data** in reports, unlike the native AI channel. [Likely; third-party] — `tracking-setup.md` §1.3 citing [Swydo](https://www.swydo.com/blog/track-ai-traffic-in-ga4/)

### Inferences
**Baseline recipe (Days 1–5, owner: agency, sign-off: Quotr CEO by Fri Dec 11)**

1. **Freeze the data on Day 1.** Export and store (CSV + screenshots, dated):
   - GSC Performance (Web), daily, **Jun 1 2025 → Nov 29 2026** (all GSC history available). By date, by page, by query, by country, with the branded/non-branded split (filter or `quotr` regex minus namesakes). GSC keeps about 16 months (Google documentation; not re-fetched this session), so pulling Day 1 captures **Dec 2025 – Feb 2026 as a same-season reference**. Also export the GSC **Generative AI report** for all available dates. Data will be partial before Aug 31 unless Quotr was in the beta.
   - GA4 **standard** Traffic acquisition report (not Explorations; standard reports ignore retention) by week, by default channel group **and** by the new custom channel group (custom groups apply retroactively; verify). Include key events by event name and landing page.
   - BWT Search Performance + AI Performance (citations, cited pages, grounding queries, intents, citation share) for every available date.
   - Cloudflare AI Crawl Control 30-day snapshot (the dashboard window is short, so save it now).
   - CRM: every inbound lead/trial/demo Jun 1 2025 → Nov 29 2026, with create date, type, source fields, and outcome (meeting held, opp, closed-won).
   - Ad spend by week (Google Ads brand vs non-brand, LinkedIn, Meta, other) and an outbound activity count by week.
2. **Check GA4 retention immediately.** If it is 2 months, Explorations cannot reach June–Sept. Use standard reports for the baseline and set retention to **14 months** on Day 1. The change is not retroactive (inference: deleted user-level data cannot be restored).
3. **Unit = ISO week (Mon–Sun), 22 weeks Jun 1 – Nov 1, 2026.** For each metric compute the **median, the 10th–90th percentile band and the mean**. Low-volume metrics (demos, qualified leads) also get a **4-week rolling sum**.
4. **Flag (don't delete) anomalous weeks** and show the baseline both with and without them:
   - W23 (Jun 1–7): May core update tail.
   - W38 (Sep 14–20) onward: new pricing. Report conversion rate pre/post Sep 14 separately.
   - W41–W42 (Oct 5–18): ChatGPT UTM/referrer outage. Expect ChatGPT referrals to be undercounted and Direct inflated.
   - Any week with a Quotr launch, PR, webinar, trade show, funding news or paid-campaign start (from the launch calendar).
5. **Seasonal adjustment (choose the best available, in this order):**
   - (a) **Quotr's own last winter:** for GSC impressions/clicks, compute the ratio *Dec 2025–Feb 2026 weekly avg ÷ Jun–Oct 2025 weekly avg*, if 2025 data exists on quotr.ai. The domain moved from quotr.io, so check which property holds 2025 data. Apply that ratio to the 2026 baseline to get an **expected** Dec 2026–Feb 2027 value.
   - (b) If Quotr has no usable 2025 data: build a **category demand index** from Google Trends (US, weekly, 2021–2026) for 4–6 non-branded head terms such as "construction estimating software", "takeoff software", "construction takeoff" and "estimating software". Trends gives relative interest, so use the same-term ratio of Dec–Feb to Jun–Oct averaged over 3–5 years. [Speculative method; must be computed on Day 1–3]
   - (c) **GSC impression-share proxy:** non-branded **impressions** respond to demand as well as rank. Track **CTR and average position** on a fixed query set as demand-neutral indicators.
6. **Write targets as "vs. expected", not "vs. baseline":** Day-90 target = baseline × seasonal factor × (1 + uplift). Report actual vs. expected with the baseline band shown.
7. **Exclude the dead zone from judgement.** Treat **Dec 21, 2026 – Jan 3, 2027** (Christmas/New Year) as non-evaluative. Treat **Nov 30 – ~Dec 14** as possibly contaminated by the Nov 2026 core-update rollout. Google's guidance is to wait one full week after completion, so if the update ends around Dec 1–7, clean comparisons start around Dec 8–14. The **evaluation window for lagging outcomes = Jan 4 – Feb 26, 2027 (8 weeks)**, compared with the expected value for the same weeks.
8. **Lag reality:** content published in December mostly can't be indexed, ranked and turned into leads by Day 90. Month-1 targets on output and indexing (Leanid's proposal) are correct. Day-90 lead targets should count the **leading indicators shipped in Month 1** plus the outcome **trend**, not the absolute level.

**What "fair" looks like (to propose in writing):** "Day-90 qualified inbound leads are judged against the seasonally expected value for Jan 4 – Feb 26, 2027, derived from the Jun–Oct 2026 weekly baseline and agreed on Dec 11. December is reported but not judged."

### Gaps
- No source quantified **December/Q4 seasonality for construction estimating/takeoff software web demand or demos**. The seasonal factor must come from Quotr's own data or Google Trends.
- Whether quotr.ai holds 2025 GSC/GA4 data (vs. quotr.io) is unknown.
- The Nov 2026 core update's **completion date** was not confirmed as of Nov 23, 2026. Check the Google Search Status Dashboard on Day 1.
- The GSC 16-month retention figure was not re-fetched from Google this session (long-standing documented behaviour).
- Construction trade-show dates in Jan–Feb 2027 (e.g., World of Concrete, IBS) were not checked. Add them to the confounder log if Quotr attends.

---

## Q3. AI referral attribution: GA4, Clarity and GSC configuration, and the dark-AI-traffic problem

### Takeaway
As of November 2026 nobody can see all AI-driven traffic in click data. GA4's native AI Assistant channel misses some sources and is forward-only. ChatGPT's tags and referrers were unreliable during Oct 8–15. Studies say most AI visits arrive as Direct. Clicks from Google AI Overviews and AI Mode are mixed into google/organic, with **no AI Mode filter in GSC's Performance report**. Use **three lenses together**: (1) a custom GA4 AI channel plus Clarity's AIPlatform channel for *measured* AI clicks, (2) GSC Generative AI and Bing AI Performance for *exposure*, (3) self-reported attribution and "direct-to-deep-page" proxies for *dark* AI influence.

### Cited Findings
**GA4**
- The native **AI Assistant** channel (since **May 13, 2026**) captures sessions with intact referrers only and is forward-only. [Known] — [Seer Interactive](https://www.seerinteractive.com/insights/are-ai-sites-like-chatgpt-sending-your-website-traffic); [Clickport](https://clickport.io/blog/chatgpt-direct-traffic-ga4)
- Google's default-channel documentation names **ChatGPT, Gemini, DeepSeek, Copilot and Grok** as AI Assistant sources. Google has **not published the full referrer list**. Perplexity's status conflicts: several sources say perplexity.ai lands in **Referral**, while one reports perplexity.ai landing in AI Assistant (medium `ai-assistant`) on a property checked in **October 2026**. The Default Channel Group **cannot be edited**. [Known that list is incomplete; Perplexity status conflicting] — [Clique Studios](https://cliquestudios.com/university/resources/ga4-ai-assistant-channel); [Simplytics](https://simplytics.dev/blog/ga4-ai-assistant-channel-what-it-still-hides); [nicelookingdata](https://www.nicelookingdata.com/blog/ga4-ai-traffic-chatgpt-referrals); [swapbiswas](https://swapbiswas.com/blog/ga4-ai-assistant-channel/)
- ChatGPT adds `utm_source=chatgpt.com` to outbound links, often with no medium, so default channel grouping may show "Unassigned". [Known] — `tracking-setup.md` §2 citing [OpenAI publishers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)

**Dark AI traffic**
- A Loamly analysis of **446,405 visits** found **70.6% of AI-referred traffic lands as Direct** in GA4. An Attrifast cohort of 200 sites (May 2026) put **~70% of true ChatGPT sessions** at Direct/(none), and attributed this partly to ChatGPT's web interface passing referrers only ~28% of the time. A Clickport snapshot (April 2026) found **35.7%** of recognised AI sessions had no referrer but carried a UTM tag. Estimates of AI traffic missed by GA4 range from **35–70%**. [Likely directionally; all vendor analyses with differing methods] — [Attrifast](https://attrifast.com/blog/dark-ai-traffic-ga4); [Clickport](https://clickport.io/blog/chatgpt-direct-traffic-ga4); [Seresa](https://seresa.io/blog/ai-data-readiness/dark-ai-traffic-is-not-dark-ga4-is-just-blind)
- ChatGPT UTM/referrer outage **Oct 8–15, 2026** (see Q2). [Likely] — [ALM Corp](https://almcorp.com/news/chatgpt-bug-sent-ai-referral-traffic-to-direct-after-gpt-6/); [Relevant Audience](https://www.relevantaudience.com/analytics/chatgpt-gpt-6-utm-referrer-dropped-direct-traffic/)

**Google AI Overviews / AI Mode**
- Google fixed a May 2025 bug where AI Mode links carried `noreferrer`. AI Mode citation clicks now record as **google / organic**. SearchPilot's reference (updated **April 2026**) says AIO and AI Mode clicks are indistinguishable from standard organic in GA4. **AI Mode sidebar links reportedly still pass no referrer** (fix status unknown). [Known/Likely] — [SEJ](https://www.searchenginejournal.com/google-fixes-ai-mode-traffic-attribution-bug/547946/); [SearchPilot AI traffic source reference (PDF)](https://www.searchpilot.com/hubfs/pdfs/ai-traffic-source-reference.pdf); [SERoundtable](https://www.seroundtable.com/google-ai-mode-sidebar-links-referrers-41016.html)
- **GSC as of late 2026:** the Generative AI report shows **impressions only** (AI Overviews, AI Mode, Discover AI features) by page, country, device and date. AIO/AI Mode **clicks are blended into the Web search type** in the Performance report. There is **no dimension, filter or label isolating AI Mode** in the Performance report, and AI Mode query text appears unlabeled. One guide claims a "Search Appearance → AI Mode" filter exists, but this contradicts other sources and is treated as unreliable. [Known/Likely] — [crawlraven](https://crawlraven.com/blog/gsc-ai-performance-reports); [mintec](https://mintec.co/blog/ai-mode-queries-search-console/); [iMasters](https://imasters.com/seo/search-console-no-filter-ai-overviews-ai-mode-google-docs-show); [nikoalho.fi (90 days of AI Mode query data)](https://nikoalho.fi/writing/ai-mode-queries-search-console/)

**Microsoft Clarity**
- Clarity's **AI channel groups** (introduced **Aug 29, 2025**) classify sessions into **AIPlatform** (organic links in AI chat) and **PaidAIPlatform** (ads inside AI chat). Covered: **ChatGPT, Claude, Copilot, Gemini, Perplexity**, standalone websites only, with AI features embedded in other products excluded. Location: **Dashboard → Traffic/Channels card → Channel tab, filter "AI Platform"**. [Known] — [Clarity docs: AIPlatform and PaidAIPlatform](https://learn.microsoft.com/en-za/clarity/insights/ai-channel-group); [Clarity blog](https://clarity.microsoft.com/blog/ai-channel-groups/); [PPC Land](https://ppc.land/microsoft-clarity-introduces-ai-channel-groups-for-traffic-analytics/)
- Microsoft reported AI referrals up **+155% over eight months** but still **under 1% of overall traffic** across Clarity sites. Clarity also published a study claiming AI traffic **converts at 3x** other channels. [Vendor data] — [MediaPost](https://www.mediapost.com/publications/article/412254/microsoft-exposes-ai-bot-site-traffic.html); [Clarity blog](https://clarity.microsoft.com/blog/ai-traffic-converts-at-3x-the-rate-of-other-channels/)
- The prior brain notes the only peer-reviewed study (973 stores) found ChatGPT traffic converted **below** most channels. Conversion claims are therefore hypotheses. — `kpis-and-dashboard.md` §5

**Bing**
- BWT AI Performance (public preview since Feb 2026) reports Copilot/Bing AI **citations, cited pages and grounding queries**. Added June 16, 2026: **Intents** (Informational, Commercial, Navigational, Learn and Solve, Research, Creation, Local…), **Topics, Citation Share, Compare**. Added Oct 13, 2026: **Topics Portfolio (beta)**, which clusters grounding queries into themes; classification "is AI-generated and can be imperfect". [Known] — [Bing blog June 2026](https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/); [Bing blog Oct 2026](https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/); [Joseph Charnin on Citation Share](https://www.josephcharnin.com/seo/bing-webmaster-tools-ai-citation-share/)

### Inferences
**GA4 configuration (Day 2–3; Editor role)** — extends `tracking-setup.md` §1.3

1. **Admin → Data display → Channel groups → Create new channel group** → name `Quotr – AI-aware (v1, 2026-12-01)`.
2. **Add new channel** `AI assistants (organic)` with conditions (AND):
   - `Session source` **matches regex** (full-match form; GA4 regex is case-sensitive and sources are lowercase):
     ```
     .*(chatgpt\.com|chat\.openai\.com|openai\.com|perplexity\.ai|perplexity|gemini\.google\.com|bard\.google\.com|copilot\.microsoft\.com|copilot\.com|copilot\.cloud\.microsoft|m365\.cloud\.microsoft|edgeservices\.bing\.com|claude\.ai|deepseek\.com|grok\.com|meta\.ai|mistral\.ai|you\.com|phind\.com|poe\.com).*
     ```
   - AND `Session medium` **does not match regex** `.*(cpc|ppc|paid|display|email).*` (so future paid ChatGPT/Copilot ads stay in Paid).
   - [Likely] The first six patterns are documented AI referrers in prior research. `copilot.com`, `copilot.cloud.microsoft`, `m365.cloud.microsoft`, `you.com`, `phind.com` and `poe.com` are **speculative additions** and harmless if unused. The bare `perplexity` catches any `utm_source=perplexity` tagging. Prune to what actually appears in **Session source / medium** after 30 days.
3. Add a second channel `AI assistants (paid)`: same source regex AND medium matches `.*(cpc|ppc|paid).*`. Place it in the Paid block.
4. **Order:** Paid channels → `AI assistants (paid)` → **`AI assistants (organic)` above Organic Search, Referral and Unassigned**. Save. Set as the **primary channel group** only if Quotr agrees, because it changes everyone's default reports. Otherwise compare it side by side.
5. **Custom dimension(s)** (event-scoped, from hidden-field/dataLayer): `first_touch_source`, `first_touch_medium`, `first_landing_page`, `self_reported_source` (sent on form submit), so GA4 key events can be cut by self-reported answer.
6. **Key events:** `generate_lead` (demo), `contact_submit`, `trial_signup`, `estimation_quote_request`, `procurement_inquiry`. Event names are suggestions; keep Quotr's existing names if present. Count **once per session** for lead events.
7. **Saved comparison** in Traffic acquisition: native `Default channel group` vs. custom group. The difference shows what the native AI Assistant channel misses (Perplexity etc.).
8. **Annotations:** GA4 annotations exist only on some surfaces, so keep the authoritative **change log** in the dashboard sheet (Q8).

**Dark-AI proxies (report weekly, never sum with measured AI):**
- **Direct sessions to deep pages:** `Session default channel group = Direct` AND `Landing page` matches `^/blog/|^/software/trades/|^/dictionary/|-vs-|alternatives|best-`. People rarely type long blog URLs, so a rise here after AI visibility gains is a weak signal of untagged AI and app clicks. [Speculative proxy]
- **Branded search** (GSC `quotr` regex minus namesakes; BWT branded queries): read-then-search behaviour.
- **Self-reported AI share** (Q6) is the primary dark-AI measure.

**Clarity (Day 2):** confirm the Clarity tag fires on all marketing pages. Use **Channels → AI Platform** as a **cross-check** of GA4's AI counts. Clarity's list is narrower (5 platforms) but defined by Microsoft. Build a Clarity segment `AIPlatform sessions` and watch 10 recordings a week of AI landings on the homepage and pricing page. That is qualitative evidence of whether AI visitors understand Quotr's offer.

**GSC (Day 2):** (a) Generative AI report weekly: total AI impressions, top 20 pages. Do not add them to Web totals. (b) Performance → Web, Query filter regex for **long conversational queries**, e.g. `^(\S+\s+){7,}\S+$` (8+ words), as a **proxy** for AI Mode-style queries. This is unlabelled and imperfect, so mark it as a proxy. (c) Bracket analysis around **Nov 9–11** (logging error) and the core-update window.

**Bing (Day 2):** weekly export of AI Performance. Track **citations, cited pages, Citation Share vs. Compare competitors** (add STACK, Togal.AI, PlanSwift, Buildxact if Compare allows), **top grounding queries by Intent = Commercial**, and Topics Portfolio clusters. This is the only first-party, citation-level AI metric available for free.

**Known / likely / speculative summary**

| Statement | Status |
|---|---|
| ChatGPT appends `utm_source=chatgpt.com` (normally) | Known |
| ChatGPT tags/referrers unreliable Oct 8–15, 2026 | Likely |
| GA4 AI Assistant channel misses some AI sources; can't be edited | Known |
| Perplexity in or out of native AI Assistant channel | Conflicting; check Quotr's property |
| AIO/AI Mode clicks separable in GA4 | **No** (Known) |
| AIO/AI Mode clicks separable in GSC | **No**; impressions only, in the Generative AI report (Known) |
| A GSC "AI Mode" search-appearance filter exists | Unreliable single claim, treat as no |
| ~35–70% of AI visits arrive as Direct | Likely directionally; vendor estimates |
| AI visitors convert 3x | Vendor claim; contradicted by peer-reviewed e-commerce study |

### Gaps
- No primary Google page listing the AI Assistant channel's referrer set was retrievable. Perplexity's treatment must be checked in Quotr's own GA4.
- Whether **ChatGPT Atlas** browser, the ChatGPT desktop/mobile apps or Perplexity's Comet browser pass referrers in late 2026 was not established.
- No independent (non-vendor) quantification of dark AI traffic was found.
- Whether Microsoft 365 Copilot/`m365.cloud.microsoft` appears as a referrer was not verified.

---

## Q4. AI crawler activity: Cloudflare, Clarity Bot Activity, logs, and what user-triggered fetches mean

### Takeaway
Monitor crawlers for **access health and a direction-of-interest signal**, not as a success KPI. Cloudflare AI Crawl Control (Read Only role) and Clarity Bot Activity (CDN-connected) now give dashboard-level views, including **crawl-to-referral ratios**. **User-triggered fetches** (ChatGPT-User, Perplexity-User, Claude-User) are the most useful bot signal. They fire when a live user's question makes the assistant open a Quotr page, so they are a rough proxy for "Quotr was considered in a real conversation", even when no click follows.

### Cited Findings
- **Cloudflare AI Crawl Control** tabs: Overview, Crawlers, Metrics, Robots.txt, Settings (Read Only role can view all). The Metrics tab includes referrer data on Paid plans. The API exposes the same data, including detection IDs, referrer data and data-transfer metrics. [Known] — [Cloudflare changelog (read-only role)](https://developers.cloudflare.com/changelog/2026-01-13-ai-crawl-control-read-only-role/); [Cloudflare docs: Analyze AI traffic](https://developers.cloudflare.com/ai-crawl-control/features/analyze-ai-traffic); [Cloudflare changelog 2025-10-14](https://developers.cloudflare.com/changelog/2025-10-14-enhanced-metrics-drilldowns/)
- Cloudflare's **Attribution Business Insights** dashboard offers a **site-wide crawl-to-referral ratio over 24 h / 7 d / 30 d** and **per-operator ratios**, plus each bot's ratio and current action. Its plan availability and date were not clear. [Likely] — [Cloudflare blog: Attribution Business Insights](https://blog.cloudflare.com/attribution-business-insights/)
- **Market crawl-to-refer benchmarks (Cloudflare Radar):** launch-era default view Anthropic ~**50,000:1**, OpenAI **887:1**, Perplexity **118:1**. An earlier June 2025 post gave OpenAI **1,700:1**, Anthropic **73,000:1**. Figures are dated and not comparable to each other. [Known as published] — [Cloudflare blog: crawl-to-refer on Radar](https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar); [Cloudflare blog: crawl-to-click gap](https://blog.cloudflare.com/crawlers-click-ai-bots-training/). Prior brain figure (July 2026 secondary): ClaudeBot ~2,237, GPTBot ~217, Google ~4.6 crawls per referral — `tracking-setup.md` §5.5
- **Clarity Bot Activity:** **Dashboards → AI Visibility → Bot Activity**. It is powered by **server-side logs collected via CDN integrations** ("data that client-side analytics simply can't see") and enabled by a project admin in Project Settings. Metrics include **AI crawl request share** (AI-bot requests as a share of all page requests, including human), requests **by operator and by bot**, and **scrape-to-referral insights** that link scraping by each AI operator to referral traffic and let you open the sessions behind those referrals. [Known] — [Clarity docs: Bot activity](https://learn.microsoft.com/clarity/ai-visibility/bot-activity); [Clarity blog: AI bot activity](https://clarity.microsoft.com/blog/ai-bot-activity-in-clarity/); [Clarity blog: scrape-to-referral](https://clarity.microsoft.com/blog/scrape-to-referral-insights/)
- The user-agent roles of OAI-SearchBot, ChatGPT-User, GPTBot, PerplexityBot, Perplexity-User, Claude-SearchBot, Claude-User, ClaudeBot, Googlebot, Google-Extended (a robots.txt control token, not a crawler) and bingbot are tabulated with "allow" recommendations in `tracking-setup.md` §5.4. OpenAI says robots.txt rules may not apply to ChatGPT-User. [Known] — `tracking-setup.md` §5.4; [OpenAI crawler docs](https://developers.openai.com/api/docs/bots)
- Status at the Sept 2026 audit: robots.txt allows all bots, **Cloudflare AI Labyrinth is on**, and whether "Block AI bots" / managed robots.txt are on is **unknown**. Since Jul 1, 2025, Cloudflare blocks AI crawlers by default for new domains. — `tracking-setup.md` §5.1; [Cloudflare press release](https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/)

### Inferences
**Weekly crawler panel (Friday review; ~10 min)**

| Metric | Source | Definition | Why it matters | Alert |
|---|---|---|---|---|
| Wanted bots blocked/challenged | Cloudflare AI Crawl Control → Crawlers (Action column); Metrics by status code | Any 403/429/503/challenge for OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User, Claude-SearchBot, Claude-User, bingbot, Googlebot | Access is a precondition. It is controllable by Quotr's engineer | Any >0 → fix same week |
| Search-index crawls on target URLs | Cloudflare Metrics by path; logs | OAI-SearchBot, PerplexityBot, Claude-SearchBot, bingbot, Googlebot requests to pages shipped/refreshed this engagement | Shows new pages entered the retrieval indexes | New page not fetched by Googlebot+bingbot within 7 days → submit/IndexNow |
| **User-triggered fetches** | Cloudflare Metrics (ChatGPT-User, Perplexity-User, Claude-User); Clarity Bot Activity by bot | Count per week + top 20 URLs | A user-triggered fetch is a strong sign that a real person's conversation pulled a Quotr page into consideration, whether or not a click follows. **Best bot-side leading indicator** | Track trend; per-URL increases on treated pages = early win |
| Training crawls | GPTBot, ClaudeBot, CCBot | Volume only | Long-run model memory; not attributable within 90 days | None |
| Crawl-to-referral ratio by operator | Cloudflare Attribution Business Insights (if available) or Clarity scrape-to-referral | Crawls ÷ referred human visits, 30-day | Efficiency of being crawled. Falling ratio = more visits per crawl | Report monthly; context only |
| AI crawl request share | Clarity Bot Activity | AI-bot requests ÷ all requests | Context for server load and bot growth | None |

**User-triggered fetch caveats [Speculative interpretation]:** (a) one conversation can trigger several fetches. (b) Tracking tools and agencies testing prompts generate fetches, so **exclude the days the prompt tracker runs**, or tag DIY runs. (c) Fetches confirm retrieval, not mention. Pair with prompt-tracking mention rate.

**Logs fallback:** if Quotr has no CDN-connected Clarity and no paid Cloudflare analytics, use the `grep` recipes in `tracking-setup.md` §5.3 on whatever raw logs exist. Trust Cloudflare-verified bot labels over raw user-agent strings, since UAs can be spoofed.

### Gaps
- Which Cloudflare plan quotr.ai is on, and therefore whether referrer analytics or Attribution Business Insights are available, is unknown.
- Clarity Bot Activity's supported CDN list and history window were not retrievable.
- No published benchmark exists for "normal" user-triggered fetch volumes for a small B2B site.

---

## Q5. Prompt-tracking tools (Nov 2026), engine coverage, sample-size/variance, and whether a DIY tracker is enough

### Takeaway
Prices have shifted since the Sept 2026 brain page. Profound's self-serve tiers are disputed and possibly gone. Peec and Otterly are the cheap self-serve options, AthenaHQ has a free tier, and Gumshoe pricing was not found. Tool choice matters less than **sampling design**: AI brand lists almost never repeat between runs (<1% identical lists), so the KPI must be a **mention frequency across many prompt-runs with a confidence interval**, not a rank or a single run. For a 90-day engagement, a **DIY API tracker plus one low-cost tool for UI-based engines** is sufficient. Weekly reporting should show the rolling 4-week rate.

### Cited Findings
**Pricing, Oct–Nov 2026 (verify on vendor pages before purchase)**
- **Otterly.AI:** Lite **$29/mo (15 prompts)**; top published tier **$489/mo**. [Known, vendor-page compilation] — [RankScope (Oct 2026, from vendor pricing pages)](https://rankscope.ai/blog/ai-visibility-tool-pricing); [Get Ryze](https://www.get-ryze.ai/blog/ai-visibility-tools-pricing-compared-2026). Sept brain: Standard $189 (100 prompts), Premium $489 (400) — `tools-comparison.md`
- **Peec AI:** **$95 / $245 / $495** across three tiers. Starter reported at **$80/mo billed annually**. Older euro pricing (€89) also circulates. [Likely] — [RankScope](https://rankscope.ai/blog/ai-visibility-tool-pricing); [Discovered Labs](https://discoveredlabs.com/blog/profound-vs-peec-vs-otterly-which-ai-visibility-platform-should-you-buy)
- **Profound:** disputed. One source shows **$99 and $399, annual only**. Others say no published price and Enterprise contracts at **~$30k–$100k+/yr**. Older reviews say $499/mo. Sept brain recorded a report that Starter/Growth were dropped mid-Sept 2026. [Conflicting] — [Get Ryze](https://www.get-ryze.ai/blog/ai-visibility-tools-pricing-compared-2026); [Stork.ai](https://www.stork.ai/blog/profound-vs-otterly-vs-peec); `tools-comparison.md`
- **Scrunch:** **$300 / $500** vs "starts at **$250/mo**" (acquired by Sitecore, June 2026). [Conflicting] — [Stork.ai](https://www.stork.ai/blog/profound-vs-otterly-vs-peec); [RankScope](https://rankscope.ai/blog/ai-visibility-tool-pricing)
- **AthenaHQ:** free tier, then **$295**. [Likely] — [SEO Counselors](https://seocounselors.com/resources/best-ai-visibility-platform)
- **Cost per tracked prompt at entry tiers:** Scrunch $0.86, Peec $1.90, Otterly $1.93, Profound $1.98. [Likely; one compilation] — [Industry Contents](https://industrycontents.com/ai-visibility-tool-pricing/)
- **Gumshoe:** no pricing found. **Semrush AI Visibility Toolkit** (~$99/domain/mo add-on), **Ahrefs Brand Radar** (per-index add-ons up to $699 for all) and **SE Ranking** tracker are worth considering only if Quotr already licenses the suite. Not re-priced this session. — `tools-comparison.md`

**Variance and sample size**
- **SparkToro (Rand Fishkin) × Gumshoe.ai (Patrick O'Donnell):** 600 volunteers ran 12 identical prompts through ChatGPT, Claude and Google AI ~**3,000 times**. ChatGPT and Google AI returned the **same brand list <1% of the time**, and the **same list in the same order <0.1%**. List length varied from 2–3 to 10+. **Frequency of appearance was more stable than position.** [Known] — [Search Engine Land](https://searchengineland.com/ai-recommendation-lists-rarely-repeat-study-468076); [SEJ](https://www.searchenginejournal.com/ai-recommendations-change-with-nearly-every-query-sparktoro/566242)
- **Conductor counter-analysis:** 14,000 API calls across 10 industries, 7 intents, 5 personas and 4 LLMs concluded recommendations "aren't random". The methods differ from SparkToro's. [Known; vendor] — [Conductor Academy](https://www.conductor.com/academy/ai-recommendation-consistency-analysis/)
- Separate coverage examines what repeated ChatGPT runs reveal about brand visibility. [Context] — [Search Engine Land](https://searchengineland.com/repeated-chatgpt-runs-brand-visibility-468552)
- Prior brain: with Quotr's 32-prompt core set, **one prompt ≈ 3 percentage points**, so targets should hold for two consecutive monthly runs. API answers (Perplexity Sonar) can differ from consumer apps. — `kpis-and-dashboard.md` §4; `tools-comparison.md` §2

### Inferences
**Sampling design (the part that matters more than the vendor):**
- KPI = **mention rate = prompt-runs naming Quotr ÷ total prompt-runs**, per engine. Report it with a **95% interval ≈ ±1.96·√(p(1−p)/n)**. Example: at p = 10% with n = 100 runs, the CI is about ±6 pp. At n = 300 it is about ±3.4 pp. To detect a move from 3% to 9% with reasonable confidence, each comparison period needs about 150–300 prompt-runs per engine. [Inference: standard binomial math]
- **Weekly:** run the Tier-A prompts (23) **×3 runs × 2–3 engines** ≈ 140–210 runs/week via API/tool. Report the **rolling 4-week mention rate**, because weekly numbers are noisy. The prior brain advised monthly for an in-house team. Weekly running is fine **as long as the headline is a rolling rate**.
- Split prompts into **treated** (topics where Leanid ships or refreshes content) and **control** (topics he does not touch) for a difference-in-differences read (Q8).
- **DIY tracker (sufficient for 90 days) [Likely]:** a script calling (a) OpenAI Responses API with web search, (b) Perplexity Sonar, (c) Gemini API with Google Search grounding, (d) Anthropic API with web search. It stores full answer text, cited URLs, brand mentions (regex on Quotr.ai + competitor list + namesake exclusions: Quotr Pro, getquotr, quotrhq, Quartr) and timestamps in a sheet or DB. Cost is low (API pennies per run). **Limits:** API ≠ consumer UI (personalisation, memory, ads). Google **AI Overviews/AI Mode** have no official API, so cover them with a tool or manual logged-out checks.
- **Buy vs. DIY for this engagement:** DIY for ChatGPT/Perplexity/Gemini/Claude API lines, plus **one** low-cost tool for UI-based Google AIO/AI Mode. Candidates: Otterly Standard or Peec Starter/Pro. Check that the tool covers AI Mode/AIO and exports raw answers. **Tool ownership:** contract should state Quotr owns the account or receives a full CSV export at Day 90.
- **What not to promise:** rank/position targets, or "visibility score" targets on a vendor's proprietary metric.

### Gaps
- Gumshoe pricing and current engine coverage were not found. Live vendor pages were not fetched (only compilations dated Oct 2026 or earlier).
- No source states the minimum runs per prompt for a stable B2B mention rate. The binomial guidance above is an inference.
- Whether Profound still sells self-serve plans in Nov 2026 is unresolved.

---

## Q6. Self-reported attribution and lead quality: definitions, form fields and CRM fields

### Takeaway
Self-reported attribution ("How did you first hear about Quotr?") is the **primary** way to capture AI influence that click data can't see. Public B2B/SaaS examples (Tally, Vercel) show AI becoming a top-cited source, though that evidence is secondary and mostly self-serve SaaS. Pair it with **captured first-touch data** and a **written definition of a Qualified Inbound Lead (QIL)** per Quotr motion (Software demo, Software trial, Estimation Service, Procurement). With that in place the agency is judged on qualified leads and pipeline, not raw form fills.

### Cited Findings
- **Tally (form builder):** co-founder Marie Martens reported **ChatGPT drove ~25% of new signups** in late April–early May 2025. A SimilarWeb figure in the same piece puts ChatGPT at 9.6% of web referrals, which is a different measure. Tally asks every new signup **which exact prompt led them to Tally**. Later coverage (Aug 2026) describes AI search as Tally's #1 channel, with **10,000+ new users/week** via ChatGPT or Perplexity. [Likely; secondary] — [Foundation Inc.](https://foundationinc.co/lab/tally-geo/); [Enterprise DNA AI Pulse, 2026-08-19](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-19-a-bootstrapped-form-builder-crosses-5m-arr-on-ai-search-as-i)
- **Vercel:** CEO Guillermo Rauch is quoted as going from **1% to 10% of signups from ChatGPT within six months**. No primary source was found. [Speculative/secondary] — [Product Hunt discussion](https://www.producthunt.com/p/chatgpt/how-many-customers-do-you-get-from-chatgpt)
- **G2 (July 2026), as summarised:** review sites (**38%**) and AI chatbots (**37%**) were about equally influential in shaping B2B buyer shortlists. This is shortlist influence, not attribution, and the original was not checked. [Secondary] — [grixhub](https://grixhub.com/b2b-ai-search/)
- Practitioner guidance recommends adding a ChatGPT/AI-assistant option to demo and signup forms (some suggest an extra "did an AI tool recommend us?" checkbox). They argue it is the main way to capture AI discovery because referral tags survive only on some paths. Most such sources are vendors. [Opinion] — [Falora](https://falora.ai/blog/self-reported-attribution-b2b); [ReddiReach](https://www.reddireach.com/blog/ai-search-attribution-in-2026-prove-found-us-on-chatgpt)
- **No reliable data shows AI is the top self-reported source for B2B in 2026.** The search found advice, not CRM-level datasets. — (search result synthesis; see sources above)
- Quotr's motions and prices: Software (7-day free trial; Lite $79.90 / Plus $299.90 per seat / Enterprise custom), **Estimation Service** ($0.25/sq ft under 50,000 sq ft; $0.10 above), **Procurement** (factory-direct materials). Core persona = trade subcontractor owner/estimator across 23 trades; also GCs/precon, and materials buyers. — `geo-brain/00-quotr/entity-fact-sheet.md`; `geo-brain/00-quotr/audiences-and-personas.md`
- The prior brain already specifies the HDYHAU question, 14 options and an optional "What did you ask the AI?" follow-up. — `tracking-setup.md` §6.2

### Inferences
**HDYHAU changes vs. `tracking-setup.md` §6.2 (small but important):**
- Keep the 14 options. Make it **required on /book-demo/, /contact-us/, Estimation Service and Procurement forms**. On the **trial** flow, put it on the first onboarding screen, required but with a "Don't remember" option to protect signup conversion.
- Add **multi-select "Where else did you research Quotr?"** (optional). AI often assists rather than originates, and a single-select undercounts it.
- Keep the conditional **"What did you ask the AI?"** free text. It is the best prompt-library input and shows whether prompts match the tracked set.
- **Randomise option order** except "Other", to reduce primacy bias. [Inference]
- Sales repeats the question on the first call and writes the answer to `self_reported_source_verified`.

**Qualified Inbound Lead (QIL) definition — propose for Quotr sign-off by Dec 11**

| Motion | Counts as *Inbound Lead* | Counts as **QIL** (agency is judged on this) | Excluded (junk) |
|---|---|---|---|
| Software demo request | Completed /book-demo/ form | Business email or verifiable company; role in construction (owner, estimator, PM, precon, purchasing); company is a contractor/sub/GC/developer in a served geography; **demo held or sales-accepted within 5 business days** | Students, job seekers, vendors/agencies selling to Quotr, competitors, duplicates, spam, existing customers seeking support |
| Software trial | Account created | **Activated trial** = plan set uploaded and ≥1 takeoff/estimate run within 7 days (adjust to Quotr's product event), from an ICP company | Disposable emails, no activity, duplicate accounts |
| Estimation Service | Quote request with plans | Real project with plan documents; trade within Quotr's coverage; quote sent | Spam, unscoped requests with no documents |
| Procurement | Materials inquiry | Named project or material list with quantities; served delivery area | Non-construction, price-shoppers with no project (or tag separately) |

- **North-star outcome for Day 90:** **QILs + SQL/opportunities created from inbound, with $ pipeline**. Raw leads are reported but are not a target.
- **Exclusion rule for fairness:** leads with an **outbound touch in the prior 30 days** (sequence email, call, LinkedIn message) are reported separately as "outbound-assisted inbound". [Inference]

**CRM fields to add (names are suggestions; HubSpot assumed but unverified)**

| Field (internal name) | Type | Set by | Purpose |
|---|---|---|---|
| `lead_type` | Picklist: software_demo / software_trial / estimation_service / procurement / contact_other | Form | Separate motions |
| `self_reported_source` | Picklist (14 options from §6.2) | Form | Primary AI-influence measure |
| `self_reported_research_multi` | Multi-select | Form | AI as assist |
| `ai_prompt_text` | Text | Form (conditional) | Prompt library + validation |
| `self_reported_source_verified` | Picklist | Sales | Corrects form answer |
| `ft_source`, `ft_medium`, `ft_campaign`, `ft_referrer`, `ft_landing_page`, `ft_timestamp` | Text/date | Hidden fields from a first-party cookie (GTM) | First-touch "what analytics saw" |
| `lt_source`, `lt_medium`, `lt_landing_page` | Text | Hidden fields | Last touch before conversion |
| `ga_client_id` | Text | Hidden field from `_ga` cookie | Join CRM ↔ GA4 |
| `ai_click_flag` | Boolean (formula: ft or lt source matches AI regex) | Workflow | Measured AI click |
| `ai_any_flag` | Boolean (ai_click_flag OR self-reported AI OR AI in multi-select) | Workflow | Total AI influence |
| `engagement_page_flag` | Boolean (ft/lt landing page in agency's treated URL list) | Workflow | Ties leads to agency-shipped pages |
| `icp_fit` | Picklist A/B/C/No | Sales/enrichment | Quality |
| `trade`, `company_size_band`, `role` | Picklist | Form/enrichment | Segment by persona |
| `qualification_status` | QIL / Not QIL / Pending | Sales within 5 business days | Agency judged on QIL |
| `disqualification_reason` | Picklist (student, vendor, competitor, spam, out-of-area, no project, duplicate, existing customer) | Sales | Diagnose junk |
| `prior_outbound_touch_30d` | Boolean + date | Sales-tool sync | Confounder separation |
| `sal_date`, `meeting_held_date`, `opportunity_created_date`, `pipeline_amount`, `closed_won_date` | Date/currency | CRM | Lagging outcomes |

**Dependencies Quotr must commit to:** sales sets `qualification_status` within 5 business days, and leads are worked within 1 business day (the site promises a reply "within one business day" — `entity-fact-sheet.md`). Without this, QIL counts are unreliable and the agency cannot be judged on them.

### Gaps
- Quotr's CRM, current lead-source fields and form tool were not verified.
- No construction-tech-specific benchmark for QIL rates or self-reported AI share was found.
- Original G2 July 2026 report and Vercel's primary statement were not retrieved.

---

## Q7. Weekly dashboard spec for the Friday performance review

### Takeaway
A one-page weekly view with **four layers**: (1) delivery and controllables, (2) access and indexing health, (3) visibility (search + AI), (4) traffic and qualified inbound. Every metric shows **this week, 4-week rolling, baseline band and seasonally expected value**. A **confounder and change log** sits on the same page. The monthly dashboard in `kpis-and-dashboard.md` §6 stays as the deeper monthly view.

### Cited Findings
- Leading SEO indicators are best tracked weekly and "reflect efforts you control right now". Leading indicators typically respond within **4–8 weeks**. Stakeholder reporting should lead with lagging outcomes supported by leading trends. [Opinion, practitioner] — [Nikolay Krastev](https://nikolaykrastev.com/?p=1933); [Semrush: proving enterprise SEO performance](https://www.semrush.com/blog/prove-enterprise-seo-performance/)
- Prompt-level AI results are volatile run to run (Q5), and 40–60% of cited domains change month to month per Profound (vendor). — `kpis-and-dashboard.md` §5
- First-party sources available weekly: GSC Performance and Generative AI report (impressions only), BWT AI Performance (citations, grounding queries, intents, citation share), GA4, Clarity AI channel and Bot Activity, Cloudflare AI Crawl Control. — Q3/Q4 citations above

### Inferences
**Cadence rules**
- **Reporting week = Mon–Sun**, closed on Sunday. **Data pull Thursday**, covering the prior full week; GSC data lags about 2 days. **Review Friday, 30 min.** Holiday Fridays: **Dec 25 → hold Wed Dec 23** (covers Dec 14–20). **Jan 1 → hold Mon Jan 4** (covers Dec 21 – Jan 3 as one "holiday block", marked non-evaluative).
- Tooling: Looker Studio (GA4 + GSC native connectors) + a Google Sheet for BWT, Cloudflare, Clarity, the prompt tracker and CRM exports. Or HubSpot dashboards if the CRM is HubSpot.
- **Colour logic:** green = above the seasonally expected value's band; amber = inside the band; red = below the band **for 2 consecutive weeks**. A single-week red is never escalated.

**Page layout (spec)**

| Block | Metric | Definition / filter | Source | Owner | Type |
|---|---|---|---|---|---|
| **A. Delivery (controllable)** | Pages shipped / refreshed vs. plan | Count vs. weekly plan; list URLs | Change log | Agency | Output (committed) |
| | Off-site actions shipped | Listicle pitches, review asks, profiles fixed | Tracker | Agency (+Quotr approvals) | Output |
| | Approval turnaround | Median hours from draft → Quotr approval | Tracker | **Quotr** | Dependency |
| | Tracking items done | Access checklist, form fields, channel group, key events | Checklist | Agency + Quotr dev | Output |
| **B. Health** | Indexed share of shipped URLs | GSC URL Inspection / Pages report; BWT | GSC, BWT | Agency | Leading (high control) |
| | Days to first Googlebot / bingbot crawl | Per new URL | Cloudflare, GSC | Agency | Leading |
| | Wanted AI bots blocked | Count of non-200 for wanted bots | Cloudflare | Quotr eng | Health gate |
| | User-triggered AI fetches (treated URLs / all) | ChatGPT-User + Perplexity-User + Claude-User | Cloudflare / Clarity | — | Leading (influenced) |
| **C. Search visibility** | Non-brand impressions & clicks — treated pages vs control pages | GSC Web, page groups | GSC | Agency | Leading (influenced) |
| | Brand clicks/impressions | `quotr` regex minus namesakes | GSC, BWT | Shared | Lagging proxy |
| | Avg position / CTR on fixed query set (30–50 queries) | Demand-neutral | GSC | Agency | Leading |
| **D. AI visibility** | GSC AI impressions (total, treated pages) | Generative AI report | GSC | Agency | Leading |
| | Bing AI citations, cited pages, Citation Share | AI Performance | BWT | Agency | Leading |
| | Mention rate & citation rate per engine (rolling 4-wk, with CI) — treated vs control prompts | Prompt tracker | DIY/tool | Agency | Leading |
| | Brand accuracy errors (8 branded prompts) | Checklist from `tracking-set.md` | Tracker | Agency | Leading |
| **E. Traffic** | Sessions by custom channel group | Incl. `AI assistants (organic)` | GA4 | — | Lagging |
| | AI sessions by source; AI landing pages | Regex channel | GA4 + Clarity AIPlatform | — | Lagging |
| | Direct-to-deep-page sessions (dark-AI proxy) | Q3 filter | GA4 | — | Proxy |
| | Organic sessions to treated vs control pages | Landing page groups | GA4 | Agency | Lagging (influenced) |
| **F. Inbound** | Inbound leads by `lead_type` | CRM create date | CRM | — | Lagging |
| | **QILs** (by type) + 4-wk rolling + vs expected | `qualification_status = QIL` | CRM | **Shared** | **Primary outcome** |
| | % leads with `ai_any_flag`; self-reported AI share | Q6 fields | CRM | — | AI influence |
| | QIL from treated landing pages | `engagement_page_flag` | CRM | Agency | Attributable outcome |
| | Outbound-assisted inbound (separate line) | `prior_outbound_touch_30d` | CRM | Sales | Confounder |
| | Pipeline $ from inbound QILs (monthly) | Opp amount | CRM | Quotr | Business outcome |
| **G. Confounder & change log** | Core updates, ChatGPT/GA4 tracking changes, paid spend Δ, outbound volume Δ, launches/PR/events, site/tag deploys, holidays | Dated entries | Log | Both | Context |
| **H. Decisions & asks** | 3 lines max | — | — | Both | — |

### Gaps
- Whether Quotr's lead volume is large enough for weekly QIL reads is unknown. If weekly QILs are in single digits, report **4-week rolling only** for Block F.
- No Bing WMT Looker Studio connector was verified. Plan for CSV/API pulls.

---

## Q8. Separating Leanid's impact from confounders (algorithm updates, paid, sales outbound, launches, maturing content)

### Takeaway
A site of Quotr's size cannot support formal SEO split-testing. Use **matched treated-vs-control page groups and prompt groups** (difference-in-differences), **lead-level confounder flags** in the CRM, and a **dated change log**. Classify each outcome as **attributable** (treated pages and prompts), **contributory** (brand and dark AI) or **external**. Agree this classification on Day 1–10, before any results exist.

### Cited Findings
- SEO split tests need scale: Semrush suggests **≥300 templated pages** and warns that small low-traffic sites "may cause unreliable results". [Known/opinion] — [Semrush](https://www.semrush.com/blog/seo-a-b-split-testing-101/)
- Causal Impact builds its counterfactual from **unchanged control pages**. Accuracy depends on test-data size, pre-period length and control choice. Etsy used it when pre-test groups differed slightly. SearchPilot moved off Causal Impact to an SEO-specific model. [Known] — [Oncrawl](https://www.oncrawl.com/technical-seo/quality-causalimpact-predictions/); [SearchPilot](https://www.searchpilot.com/resources/blog/the-math-behind-searchpilot-how-seo-a/b-testing-actually-works)
- When comparable pages are scarce, **matched groups based on historical behaviour** can beat a random split. Pre/post without a control is possible but weaker. [Opinion] — [Search Engine Land](https://searchengineland.com/technical-seo-testing-build-stronger-experiment-484537)
- You "can't attribute any fluctuations in traffic or rankings to your changes unless the pages have been re-crawled". Use a random or matched split with unchanged pages as control. [Opinion] — [Ahrefs](https://ahrefs.com/blog/seo-testing)
- Low-traffic sites may need longer than the typical 2–4-week test window. [Opinion] — [Sitebulb](https://sitebulb.com/resources/guides/seo-testing-with-low-traffic-how-to-make-smart-calls-on-small-sites/)
- Core-update timing and Google's "wait a week after completion" guidance: see Q2. — [seo-kreativ](https://www.seo-kreativ.de/en/blog/google-november-2026-core-update/)
- Quotr has **96 blog posts** (blog sitemap), 23 trade pages and a dictionary, so existing content is still maturing and is a background trend. — `tracking-setup.md` §3.1; `entity-fact-sheet.md`

### Inferences
**Confounder register (set up Day 1; review every Friday)**

| Confounder | Mechanism | How to detect | How to neutralise |
|---|---|---|---|
| **Nov 2026 core update** (from Nov 10; may run into Dec) | Rank shifts site-wide | Status dashboard; site-wide GSC step change on both treated and control pages | DiD on treated vs control. Exclude rollout weeks + 1 week from the evaluation |
| Future core/spam updates (Q1 2027) | Same | Same | Same; log dates |
| GSC logging error Nov 9–11 | Gen-AI impressions dip | Known dates | Exclude from AI-impression baseline |
| ChatGPT tag/referrer behaviour (Oct 8–15 outage; future changes) | Shifts AI ↔ Direct | Sudden AI drop + Direct rise with flat GSC | Track AI+Direct-deep combined; note dates |
| GA4/GTM/consent changes | Measurement step changes | Change log | Log every deploy. Compare before/after on control pages |
| **Paid spend** (esp. brand bidding, LinkedIn, review-site PPC) | Moves demos and brand clicks | Weekly spend by campaign | Report paid-sourced leads separately. Ask Quotr to hold brand spend flat or log changes |
| **Sales outbound** | Prospects visit or book after outbound | `prior_outbound_touch_30d` | Report "outbound-assisted inbound" as a separate line |
| **Product launches / pricing / PR / funding / webinars / events** | Brand spikes | Launch calendar | Flag weeks. Judge on non-brand and treated-page metrics |
| **Existing content maturing** (posts from Aug–Nov 2026) | Organic growth regardless of agency | Control group trend | Control group = pages untouched by the agency. Only the **excess** over control counts |
| **Seasonality / holidays** | Dec–early Jan trough | Seasonal factor (Q2) | Judge vs expected. Holiday block non-evaluative |
| Competitor moves / AI engine model changes | AI answer shifts | Control prompts move too | DiD on treated vs control prompts |

**Design: treated vs control (Day 3–10)**
- **Page groups:** from the 96 posts + trade pages, pick **treated** (pages the agency will refresh or build clusters around) and a **matched control** set of similar type, traffic level and trend over Jun–Oct (e.g., pair by 22-week click median and slope). Freeze both lists in writing. New pages have no pre-period, so judge them on absolute indexing/impressions/citations and compare against the "new pages Quotr published Jun–Oct" cohort (time-since-publish curves).
- **Prompt groups:** tag the 53 tracked prompts as **treated** (topics the agency targets) vs **control** (not targeted). Report mention-rate DiD.
- **Readout:** `Effect = (Treated_post − Treated_pre) − (Control_post − Control_pre)`, with pre = Jun–Oct seasonally adjusted, post = Jan 4 – Feb 26. Show it as a direction plus magnitude with the caveat that it is not a statistically powered test. [Inference]
- **Attribution tiers for leads:** (1) **Attributable** = QIL whose first or last landing page is a treated/new page, or whose self-reported answer is AI with a prompt matching a treated topic. (2) **Contributory** = QIL with AI self-report or brand-search first touch, not tied to treated pages. (3) **External** = paid, outbound-assisted, events, referrals.

### Gaps
- No validated methodology for very small sites exists (per sources). DiD on matched groups here is pragmatic, not statistically guaranteed.
- Quotr's page-level traffic distribution (whether enough comparable pages exist for matched groups) is unknown until GSC access.

---

## Q9. KPI accountability structure: leading vs lagging, what's controllable, and red flags in "own growth metrics"

### Takeaway
Rewrite "own growth metrics and TOFU performance" as a **three-tier contract**:
1. **Commit** to outputs the agency controls.
2. **Target** leading indicators it strongly influences.
3. **Share accountability** for business outcomes (qualified inbound, pipeline) that depend on Quotr's sales, paid, product and approvals.

Judge outcomes against the **seasonally expected baseline** agreed by Dec 11, with named Quotr dependencies. Owning outcomes without control of the levers is the core red flag.

### Cited Findings
- Agencies should be held to the **same KPIs as the in-house team**, not a separate set. Revenue ranks 4th among agency/freelance SEOs' top metrics, while in-house SEOs put **MQLs** 4th. [Opinion/survey] — [SEJ #AskanSEO (Jenny Halasz)](https://www.searchenginejournal.com/askanseo-jenny-halasz-seo-measurement-metrics/161408/)
- Leading indicators are weekly, controllable and forecastable. They respond in about 4–8 weeks. Lead stakeholder reporting with lagging outcomes. [Opinion] — [Nikolay Krastev](https://nikolaykrastev.com/?p=1933); [Semrush](https://www.semrush.com/blog/prove-enterprise-seo-performance/)
- Prior brain targets are explicitly "SUGGESTED … not agreed with Quotr". Conversion of AI visitors is "unproven: measure it, don't assume it". — `kpis-and-dashboard.md` §4
- Search results gave **no** authoritative source on contract clauses for outcome ownership or agency red flags. — (Q9 search, see Gaps)

### Inferences
**Proposed accountability structure (for the SOW / Day-1 kickoff)**

| Tier | What | Examples (90-day) | Agency stance | Evidence |
|---|---|---|---|---|
| **1. Committed outputs** (fully controllable) | Work shipped on schedule | N pages published/refreshed per month (per content plan); technical fixes (sitemaps in robots.txt, lastmod, stale-price URLs = 0, llms.txt fixed); tracking stack live by Dec 11 (channel group, key events, HDYHAU, CRM fields); weekly Friday report 13/13; monthly prompt-tracking run | **Guaranteed**, with remedy if missed for agency-side reasons | Change log, URLs |
| **2. Leading indicators** (high influence, some external noise) | Signals that precede traffic | ≥90% of shipped URLs indexed in Google and Bing within 14 days; 0 wanted AI bots blocked; treated-page non-brand impressions vs control (DiD positive by Day 90); GSC AI impressions and Bing AI citations on treated pages rising; mention rate on treated prompts (rolling 4-wk) up vs control; branded-answer errors ≤2/8 | **Targets** with directional ranges, reviewed Day 30/60. Missed targets trigger a plan change, not a penalty | GSC, BWT, Cloudflare, tracker |
| **3. Business outcomes** (shared; Quotr controls sales, paid, product, pricing, site conversion UX) | Qualified inbound and pipeline | QILs (Jan 4 – Feb 26) vs seasonally expected value; % QIL with AI influence; QILs from treated pages; inbound pipeline $ | **Shared accountability**: agency reports and diagnoses. "Success" = beat expected band. Not a sole-ownership guarantee | CRM with QIL definition |

**Reframing Leanid's proposal:** "Month 1 = content output and indexing" maps to Tiers 1–2, which is good. "Day 90 = qualified inbound leads vs a June–October baseline" stays, **if** (a) the baseline is seasonally adjusted, (b) the evaluation window is Jan 4 – Feb 26, (c) QIL is defined and qualified by Quotr's sales within 5 days, and (d) outbound-assisted and paid-sourced leads are separated.

**Quotr-side dependencies to write into the SOW (each with an SLA)**
1. Access checklist complete by **Fri Dec 4**.
2. Content/SME approvals within **2 business days**. Track the approval-turnaround metric.
3. Dev time for forms/hidden fields/tag changes within **5 business days** of request.
4. Sales qualifies inbound within **5 business days** and works leads within 1.
5. Paid brand spend held flat or changes logged. Outbound sequences logged.
6. Launch/PR/pricing calendar shared and kept current.
7. Baseline and seasonal factor signed off by **Fri Dec 11**. Targets fixed after that (no moving goalposts).

**Red flags when a client asks a contractor to "own growth metrics" [Inference; no authoritative source found]**
- Ownership of **lead or revenue numbers without control** of the levers (paid budget, sales follow-up, pricing, website conversion design, product onboarding).
- **No agreed baseline or definition** ("leads" undefined, so junk volume counts or good leads get disqualified after the fact).
- **Attribution method chosen after results** (e.g., last-click only, which hides AI/dark influence; or "it was sales" for every win).
- **90-day outcome guarantees for organic/AI channels** where indexing-to-lead lag is often longer than the window, **plus a December start**.
- **Agency can't see the CRM** or pipeline it is judged on.
- **Approval bottlenecks** not counted against the timeline.
- **Shared-credit ambiguity** with the in-house team (Jaron/Jati/Mia/Jenny). Who wrote, approved or promoted each asset should be logged.
- Vendor "visibility scores" used as contractual KPIs. They are proprietary, volatile and non-portable.
- Data/asset ownership unclear at exit (tracker accounts, dashboards, content drafts).

**Suggested contract language (short form):** "Agency commits to Tier-1 deliverables; Tier-2 indicators are targets reviewed at Day 30/60; Tier-3 outcomes (qualified inbound leads and pipeline) are shared goals measured against the seasonally adjusted Jun–Oct 2026 baseline agreed on Dec 11, 2026, evaluated over Jan 4 – Feb 26, 2027, excluding paid-sourced and outbound-assisted leads, and conditional on the Client dependencies in Annex X."

### Gaps
- No primary or authoritative source found on SEO/GEO agency contract clauses, outcome-based pricing norms, or red flags. This section is reasoned from the measurement findings and should be reviewed by whoever covers contract terms in this research set.
- Quotr's historical inbound volume and QIL rate are unknown, so numeric Day-90 targets cannot be set in these notes. They must come from the Day-1 baseline.
