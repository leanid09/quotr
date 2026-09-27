---
type: baseline
description: 'Every place outside quotr.ai where Quotr appears (or should): reviews, directories, lists, press, social.'
last_verified: 2026-09-25
verify_every_days: 30
---
# Quotr Off-Site Presence (Baseline, September 2026)

> [!abstract] What this page is for
> A complete list of every place outside quotr.ai where Quotr shows up (or should show up), with status, numbers and links, so the team knows what exists, what is wrong, and what is missing.
>
> *Baseline measured on 2026-09-25.*

> [!info]- Sources
> Research notes [[quotr_offsite_presence]] (main source), [[verification_quotr_and_competitors]] (corrections override the other notes), [[quotr_ai_visibility_tests]], [[competitor_geo_benchmark]], [[verification_geo_evidence]] (general evidence caveats). Every row below links to the page it came from.

---

## Why off-site presence matters (in two lines)

AI answer engines trust what **other** websites say about a brand more than what the brand says about itself. In our tests, when a fact about Quotr came only from quotr.ai, Perplexity often used it without naming Quotr, or added "vendor assertions" and "not independently validated". See [[Signals that matter]].

## How we checked (and what we could not check)

- Pages were read with a scraping tool; AI answers came from Perplexity (Sonar model); search results came from a web search tool. All on 2026-09-25.
- **G2 blocked our scraper** (anti-bot wall). **Reddit could not be searched** with the web search tool. The scraper was also rate-limited for part of the day, so several lists were checked with a site-restricted search instead of by reading the page. These cases are marked "search check" below.
- Status words used on this page:
  - **Active:** exists and looks current.
  - **Weak:** exists but has little in it (no reviews, few followers).
  - **Stale / wrong:** exists but shows old or conflicting facts.
  - **Unclaimed:** a listing exists that Quotr does not appear to control.
  - **Not found:** we looked and found nothing.
  - **Unverified:** reported by an AI engine or search summary, but we could not open the page.

---

## Summary

- **Reviews:** Quotr has almost no review footprint. The G2 profile (`quotr-io`) reportedly has **0 reviews** (reported by Perplexity only; G2 blocks direct checks, so UNVERIFIED). No Capterra, GetApp, Software Advice, TrustRadius, SourceForge or AlternativeTo listing was found. Competitors that AI engines recommend have roughly **30 to 4,000+** reviews on G2 or Capterra.
- **"Best of" lists:** only **three** outside comparison pages are confirmed to name Quotr, and none is independent: **Nomic** (#5 of 7 Kreo alternatives; Nomic ranks itself #1), **Octopus Builds** (#2 of 8; the author ranks itself #1) and **ForesightIQ** (whose only source on Quotr is Quotr's own blog). Nomic and Octopus Builds both repeat the old $299.90 price. Quotr is absent from every heavily cited 2026 roundup we checked.
- **Community:** **Zero** Reddit mentions found. A YouTube channel and LinkedIn page exist, but YouTube was never cited in 45 AI test runs, and handles are split between old and new names.
- **Press:** **No** earned trade-press coverage and **no** press release for the $3.5M seed round. One paid wire release exists (EIN Presswire, Feb 2025, about the free FireTips LA fire-rebuild app). Two podcast appearances are known (one confirmed by reading the page).
- **Entity data:** Crunchbase, PitchBook, F6S, Product Hunt and the podcast pages disagree with each other and with quotr.ai on HQ, founding year, founders, funding, factory count and domain.
- **Name collisions:** at least 8 unrelated products use the name "Quotr", several aimed at contractors. AI engines already mix them up.

**Biggest gap:** third-party proof (reviews, neutral lists, press). More content on quotr.ai cannot replace it.

---

## 1. Master table: every platform and mention found

### 1a. Review sites and software directories

| Platform | URL | Status | Numbers | What it says / issues |
|---|---|---|---|---|
| G2 | https://www.g2.com/products/quotr-io/reviews | Weak (Unverified) | 0 reviews, "0.0/5" (Perplexity report) | Linked by Quotr as a "Verified Organizational Profile" on /disambiguation/. Scraper blocked by G2's anti-bot wall. Perplexity says vendor "QUOTR", founded 2023, HQ Berkeley. Listed under the old slug `quotr-io`. A site search for Quotr on G2 returned look-alikes instead (Quoters, Quattr, Quo, Qualified.io). |
| G2 category pages | [construction estimating p.4](https://www.g2.com/categories/construction-estimating-software/free?order=g2_score&page=4); [construction management (FR)](https://www.g2.com/fr/categories/construction-management/free?open_modal_url=/products/re-flow-field-management/wishlists?host_path=%252Fcategories%252Fconstruction-management%252Ffree&order=popular&page=15) | Unverified | A "4.4/5.0" figure next to Quotr (Perplexity report) | Perplexity read this as a category snapshot, not real reviews. Ambiguous; do not quote it. |
| Capterra | https://www.capterra.com/search/?query=quotr | Not found | 20 search results, none Quotr | Search routes to a "Quoting" category and shows look-alikes (QuoTrak, QuoTrend, HyperQuote Takeoff, Quotation Expert). Capterra's footer links to G2 company pages. **Confirmed:** G2 agreed to buy Capterra, GetApp and Software Advice from Gartner (announced January 2026; reportedly closed Feb 5, 2026), so one G2 vendor account and review program now feeds all four directories. |
| GetApp | https://www.getapp.com/construction-software/takeoff/ | Not found (search check) | — | Only category pages returned. |
| Software Advice | https://www.softwareadvice.com/construction/cost-estimating-software-comparison/ | Not found (search check) | — | Software Advice lists 23 tools for subcontractor estimating; Quotr not among search results. |
| TrustRadius | https://www.trustradius.com/construction-takeoff-and-estimating | Not found (search check) | — | Category page only. |
| SourceForge | https://sourceforge.net/software/product/Quotr/ | Not found | HTTP 404 | SourceForge's AI takeoff category was cited in AI answers (C1, V7). |
| AlternativeTo | https://alternativeto.net/software/quotr/about/ | Not found | HTTP 404 | — |
| SaaSworthy, SoftwareWorld, Krowdbase, Slashdot, SoftwareSuggest | e.g. https://www.saasworthy.com/list/construction-estimating | Not found (search check) | — | Generic category pages only. |
| Product Hunt | https://www.producthunt.com/products/quotr | Weak | 0 upvotes, 2 followers, "No reviews yet" | Listed as "Quotr.ai: Build with Confidence: AI-powered estimating platform". Launched in 2026 (about 7 months before the check) in the **"Real estate"** category (tags: SaaS, AI, Construction). Claims "90% faster takeoffs, 95% accuracy, and 40-50% material savings". Maker "Ja sz". Maker comment promotes Dallas Build Expo, April 22–23, Booth #277. Links x.com/quotr_ai, instagram.com/quotr.ai, linkedin.com/company/quotrai, github.com/Quotr-io. |
| F6S | https://www.f6s.com/software/quotr | Unclaimed, stale | No reviews | Page shows "Quotr Claim" (unclaimed). Describes the **old product**: "construction cost-estimation and project cost management SaaS that provides real-time cost estimation during design iterations", "Quotr Assist", "Quotr Connector (automatic sync with Autodesk Revit…)". "Made by FLOZ". Links quotr.io. |
| F6S company page | f6s company/floz (linked from /disambiguation/) | Unverified | — | Not opened. |
| Procore Construction Network | https://network.procore.com/p/floz-berkeley | Unverified | — | Linked from /disambiguation/. Scrape returned only a cookie wall. No Procore App Marketplace integration listing was found. |
| Apple App Store | — | Not applicable | — | No Quotr.ai app found. Several **unrelated** "Quotr" apps exist (see Section 7). |

### 1b. Company and startup databases

| Database | URL | Status | Numbers / facts shown | Issues |
|---|---|---|---|---|
| Crunchbase | https://www.crunchbase.com/organization/quotr | Active, partly wrong | Name "Quotr.ai"; legal name "Quotr"; also known as "Quotr, Quotr.ai". Founders Hanyang Liu and Junzhe Shi. One Seed round, lead investor Llama Ventures. "50+ vetted factories across Foshan and Guangdong… 40–55% below distributor markup". Categories AI, Construction, SaaS. Headcount 11–50. CB Rank 40,965; Growth Score 68; Heat Score 82. Monthly web visits 5,678 (+110.14% in the past month, Semrush data). Competitors listed: Autodesk, Trimble, STACK. Links linkedin.com/company/quotrai and a Facebook page (ID 61572581013981). | HQ conflict on the same page (confirmed by the fact-check): the location field and FAQ say Berkeley, while the About text says "Founded in 2023 and headquartered in San Francisco". The About text is written in Quotr's own voice, so Quotr can edit it. A search-index snippet of the page shows "headquartered in Berkeley, CA" instead. A search summary quoted an old description: "an AI assistant providing real-time cost estimation and Revit integration to help architects". |
| PitchBook | https://pitchbook.com/profiles/company/606944-17 | Active, conflicting | Year founded **2024**; 10 employees; HQ **495 27th Avenue, Suite 8, San Francisco, CA 94121**. Investors: Berkeley SkyDeck Fund, Llama Ventures, **Sky Arc Capital** (Quotr never mentions Sky Arc). Primary industry Business/Productivity Software; also Logistics and Construction & Engineering. Competitors: Togal.AI and Stackt. Description mentions "construction drawings and BIM models". Links linkedin.com/company/quotrai and twitter.com/quotr_ai. | **Resolved by the fact-check:** the live public page shows only "Seed Round, 01-Jan-2025" with **no amount**. The "$190K seed on 15-Oct-2024" figure appears only inside Perplexity answers (reported twice) and its origin is unknown, so write "Perplexity reports…", never "PitchBook shows…". Founding year (2024), headcount (10) and the Sky Arc Capital investor still conflict with Quotr's own pages. Quotr's /disambiguation/ page warns that "entity associations in public financial databases may be lagging or misattributed". |
| PitchBook (SkyDeck Fund page) | https://pitchbook.com/profiles/investor/231026-41 | Active | Lists Quotr as a portfolio company | — |
| Caplight | https://www.caplight.com/company/quotr | Unverified | — | Cited by Perplexity in funding answers; it "does not fully agree" with other sources. A separate Caplight page, https://www.caplight.com/company/quotrhq, belongs to a **different** company (quotrhq.com). |
| F4 Fund | https://f4.fund/startups/quotr | Unverified | — | Linked from /disambiguation/; cited by Perplexity. Not opened. |
| AngelList | (linked from /disambiguation/) | Unverified | — | Not opened. |
| Parsers VC | (linked from /disambiguation/, as "quotr.io") | Unverified | — | Uses the legacy domain name. |
| salaryguide.com | https://salaryguide.com/companies/quotr | Unverified | — | Surfaced as a Perplexity citation. |
| industrialcorp.org | industrialcorp.org/u/quotr | Unverified | — | Surfaced as a Perplexity citation. |
| prospeo, luma | (cited in the funding/founders answer, B6) | Unverified | — | Not opened. |
| Wikipedia / Wikidata | — | Not found | — | No entry for Quotr or FLOZ. No Google Knowledge Panel evidence found (could not test directly). |

### 1c. Accelerator, investor and membership pages

| Page | URL | Status | What it says |
|---|---|---|---|
| Berkeley SkyDeck, Batch 19 | https://skydeck.berkeley.edu/batch19/ | Active | Quotr provides "real-time, AI-driven construction cost estimation and supplier matchmaking… for developers, suppliers, and contractors" (search snippet). Batch 19 applications opened July 2024 ([SkyDeck release](https://skydeck.berkeley.edu/press-release-berkeley-skydeck-opens-batch-19-applications-with-expanded-eligibility-and-three-new-track-chairs/)). The only Quotr hit in a press-domain search. |
| Llama Ventures portfolio | https://www.llamaventures.vc/portfolio/ | Active | Lists "Quotr" (scraped). No funding announcement found. |
| BIA Bay Area member directory | member "quotr-io-6539" (linked from /disambiguation/) | Unverified | Uses the legacy "quotr-io" name. |
| Modular Building Institute directory | https://members.modular.org/member-directory/Details/quotr-io-4201053 | Unverified | Uses the legacy "quotr-io" name. |

### 1d. Third-party pages that mention Quotr

No page in this list is independent editorial. The fact-check confirmed three pages that name Quotr (Nomic, Octopus Builds, ForesightIQ); all are vendor or aggregator content. The four pages marked "Via Perplexity" below were never opened, so whether they mention Quotr is **UNVERIFIED**.

| Page | URL | How we know | What it says about Quotr |
|---|---|---|---|
| Nomic, "Best Kreo Alternatives in 2026" (last reviewed September 2026) | https://www.nomic.ai/compare/kreo-alternatives | Scraped | Quotr.ai is **#5 of 7**: "AI takeoff-to-proposal automation for contractors… Pricing: From ~$299.90/month" (stale price; the current entry plan is Lite at $79.90). No mention of procurement or factory-direct materials. |
| Nomic, "Best AI for cost estimation" | https://www.nomic.ai/compare/best-ai-for-cost-estimation | Unverified | Cited in Quotr brand prompts (B2, B4) and in C11, so it may mention Quotr. Not opened. |
| ForesightIQ, Togal.AI competitive landscape | https://www.foresightiq.co/competitive-landscape/togalai | Via Perplexity | The **only third-party page seen getting Quotr named in an unbranded answer** ("Togal.AI alternatives", run 2: "emphasized by ForesightIQ and Quotr's own materials as an end-to-end alternative"). The fact-check found that its only source for Quotr is Quotr's own [best-togal-ai-alternatives](https://quotr.ai/blog/best-togal-ai-alternatives/) post, so it is not independent proof. |
| R Construction Solutions, automated takeoff comparison | https://rconstructionsolutions.com/post/top-automated-takeoff-software-comparison | Via Perplexity (UNVERIFIED) | Reportedly a comparison table that includes Quotr. Not opened. |
| PalCode, AI for construction takeoffs | https://palcode.ai/blog/ai-for-construction-takeoffs-tools-that-work | Via Perplexity (UNVERIFIED) | A competing vendor's 2026 list. Not opened. |
| NEDES Estimating | https://nedesestimating.com/construction-estimating-companies-ai-automation-real-time-pricing/ | Via Perplexity (UNVERIFIED) | Reportedly a table entry, "tied to supply pricing". Not opened. |
| AI Building Tools | https://aibuildingtools.com/best-ai-for/construction-estimation | Via Perplexity (UNVERIFIED) | Not opened. |
| Octopus Builds (Ellenox), "AI development companies for AI quoting and estimation" (Sep 9, 2026) | https://octopusbuilds.com/blog/ai-development-companies-ai-quoting-estimation | Read by the fact-check | Quotr.ai is **#2 of 8** (the author ranks itself #1). Repeats the **old Solo $299.90 / Team $499.90 pricing**, "220+ factories", "95–99% accuracy" and "Berkeley, CA". Perplexity cites it when describing Quotr (B3, B4, B6 re-runs). Ask them to update the price. |

### 1e. Community and social

| Channel | URL | Status | Numbers | Notes |
|---|---|---|---|---|
| Reddit | — | Not found | 0 mentions found | Perplexity found no posts naming Quotr in r/estimators, r/Construction or r/Contractor. Web search tool cannot access Reddit, so this is a one-source check. |
| YouTube: @QuotrAI | https://www.youtube.com/@QuotrAI | Active | Subscribers, views, video count not retrieved | Channel titled "QuotrAI". Listed in the homepage schema and footer. |
| YouTube: @QuotrIO | https://www.youtube.com/@QuotrIO/videos | Unclear | — | Quotr lists this handle on /disambiguation/. It resolves to a channel titled **"QuoTrio"** (handle @QuoTrio, channel ID UCsiomlzNKGWU25LOrTsZI4Q). Whether it is Quotr's old channel is **TO CONFIRM with Quotr**. |
| YouTube videos | [Demo](https://www.youtube.com/watch?v=I0dsjz7Y_kc); [RL Electric case study](https://www.youtube.com/watch?v=Y2_PUPVtVaE); [Revit extension (legacy)](https://www.youtube.com/watch?v=zNIXcvCbWAg); ["Funded, Now What?!" Ep. 45](https://www.youtube.com/watch?v=CMGyqn5VI9I) | Active | — | "AI Construction Estimating Software Demo (Quotr.ai)"; "RL Electric's Quotr Journey: Streamlining Proposals and Takeoffs with AI"; "How To Use Quotr Estimate \| Cost Estimation Revit Extension" (old product, still live); podcast video "with Quotr.io". |
| LinkedIn company page | https://www.linkedin.com/company/quotrai | Active | About 1,077 followers (Perplexity report, unverified) | Titled "Quotr.ai". Cited by Perplexity. A search summary pulled an old "Revit / architects" description linked to this page. |
| LinkedIn old slug | linkedin.com/company/quotrio | Unclear | — | Linked from /disambiguation/ as a "Verified Organizational Profile". Differs from the homepage (quotrai). |
| LinkedIn "flozdesign" | https://www.linkedin.com/company/flozdesign | Unverified | — | Cited by Perplexity in "What is Quotr?" answers. Relation to FLOZ Inc TO CONFIRM with Quotr. |
| LinkedIn founder profiles | [Hanyang Liu (hanyang-liu1)](https://www.linkedin.com/in/hanyang-liu1/); [Hanyang Liu (second profile)](https://www.linkedin.com/in/hanyang-liu-0a8145b3/); [Junzhe Shi](https://www.linkedin.com/in/junzhe-shi/) | Active | — | Hanyang Liu has **two** profiles, both "Co-Founder @ Quotr". A search summary wrongly merged another startup's news into his profile (see Section 9). |
| LinkedIn job post | https://www.linkedin.com/jobs/view/growth-intern-at-quotr-4354499801 | Active | — | "Growth Intern at Quotr". Cited by Perplexity in brand answers. |
| LinkedIn post (webinar) | [Hanyang Liu post](https://www.linkedin.com/posts/hanyang-liu1_ask-your-plans-ai-agent-quotrai-webinar-activity-7489098660396290050-c3A4) | Active | — | "Ask your plans AI agent" webinar. Source of the 1,077-follower figure. |
| X (Twitter) | x.com/quotr_io and x.com/quotr_ai | Split | Followers and activity not retrieved | @quotr_io is linked by /disambiguation/ and the MPN podcast page. @quotr_ai is linked by Product Hunt, PitchBook and the homepage schema. |
| Instagram | instagram.com/quotr.ai | Not checked | — | Listed in homepage schema and on Product Hunt. |
| Medium | medium.com/@quotr-ai | Not checked | — | Listed in homepage schema. Whether it duplicates blog posts is unknown. |
| Facebook | Facebook page ID 61572581013981 (via Crunchbase) | Not checked | — | — |
| GitHub | github.com/Quotr-io | Not checked | — | Linked from Product Hunt. Uses the legacy name. |
| Meetup | https://www.meetup.com/quotr-ai-construction-technology/ | Active | — | Group "Quotr.ai Construction Technology". Size not retrieved. |
| Substack | https://aiaecdigest.substack.com/p/stop-listening-watch-what-customers-do | Active | — | Hanyang Liu wrote "Stop Listening to What Customers Say, Watch What They Do" on the AI AEC Digest. |
| Academic profiles | [Junzhe Shi, ResearchGate](https://www.researchgate.net/profile/Junzhe-Shi-2); [Google Scholar](https://scholar.google.com/citations?hl=en&user=Fh8qFr4AAAAJ) | Active | — | UC Berkeley Civil & Environmental Engineering PhD. No Quotr-specific public thought leadership found from him off-site. |

### 1f. Press, podcasts, events and awards

| Item | URL | Status | Details |
|---|---|---|---|
| "Funded, Now What?!" Episode 45, Marketing Podcast Network (Mar 23, 2026) | https://marketingpodcasts.net/2026/03/episode-45-can-ai-cut-construction-material-costs-by-50/ | Active (scraped) | Guest Hanyang Liu, "CEO of Quotr.io", "founder of Quotr.io and a Berkeley Skydeck alumnus… An architect by trade… leading a technical team in San Francisco". Links quotr.io, not quotr.ai. Topics include "GEO Strategy: … focusing on 'Unbranded' search terms", "AI-powered service is a better sales pitch than AI Platform" and "The Wikipedia Hack". **Funding figure:** the page itself says he "has raised $5 million" (confirmed by the fact-check; a search summary had wrongly said "$3.5 million"). That conflicts with the $3.5M seed on /disambiguation/. |
| iHeart "AEC Tech Journeys", episode "From Drawings to Bids in Minutes" | https://www.iheart.com/podcast/1323-aec-tech-journeys-with-ma-272978673/episode/from-drawings-to-bids-in-minutes-340063021/ | Unverified | Cited by Perplexity in two funding/founder answers. We did not open the page, so we cannot confirm it features Quotr. |
| Trade press (Construction Dive, ENR, For Construction Pros, BuilderOnline, TechCrunch) | — | Not found | Site-restricted search returned no Quotr article. ENR and For Construction Pros do publish estimating tech stories ([ENR example](https://www.enr.com/articles/63634-construction-is-about-to-leave-124b-on-the-table-due-to-outdated-bidding); [FCP example](https://www.forconstructionpros.com/construction-technology/estimating-bidding/article/22159258/3-cool-construction-estimating-software-trends)). |
| Newswires (PR Newswire, Business Wire, GlobeNewswire), VentureBeat, Crunchbase News | — | Not found | No release for the "$3.5M seed, Llama Ventures" round. |
| EIN Presswire (paid wire release), about Feb 6–7, 2025: "Quotr Launches LA-focused App to Help Homeowners Get Accurate Information, Rebuild Faster After Devastating Fires" | [EIN Presswire](https://www.einnews.com/pr_news/783445824/quotr-launches-la-focused-app-to-help-homeowners-get-accurate-information-rebuild-faster-after-devastating-fires) | Active (seen in search results; text not opened) | Announces the free FireTips app at firetips.quotr.io. Syndicated to local-TV business pages (e.g. KRON4). Paid wire, not earned press, and it uses the old quotr.io domain. Found by a WebSearch on 2026-09-25; not in the research notes. |
| Dallas Build Expo, April 22–23, 2026, Booth #277 | [Product Hunt maker post](https://www.producthunt.com/products/quotr) | Past event | Only known off-site trace of a trade-show appearance. Quotr's blog also has recaps of IBS 2026, Dallas Build Expo 2026, RE:Forge SF 2026, NHCA Build the Builder 2026, PCBC 2026 and CBD Fair 2026 (first-party). |
| Awards | — | Not found | None found in any search. |
| Customers and partners (third-party) | [RL Electric video](https://www.youtube.com/watch?v=Y2_PUPVtVaE) | Partial | RL Electric appears in a customer video. The Vanderbilt classroom story exists only on Quotr's blog ([vanderbilt-classroom](https://quotr.ai/blog/vanderbilt-classroom/)); no Vanderbilt-side source found. |

### 1g. Legacy and staging domains still visible to search and AI

| Host / URL | Status | Why it matters |
|---|---|---|
| https://quotr.io/pricing/ ("Quotr – AI Construction Estimation Software") | Still in search index | Old domain page. Whether quotr.io redirects to quotr.ai is **not confirmed**. |
| https://firetips.quotr.io/ | Still in search index | Old subdomain hosting FireTips, Quotr's free LA fire-rebuild app (launched Feb 2025 per the EIN Presswire release). Page content not checked. Worth moving to or linking from quotr.ai. |
| https://test.quotr.io/disambiguation/ | Cited by Perplexity (twice, including the fact-check re-run for "Quotr.ai pricing") | Staging copy. Now shows a Cloudflare Access login ("Log in to Quotr.io Restricted Access"), so it was indexed at some point and is still being cited. |
| public.quotr.io | In use | Logo and og-cover images in quotr.ai schema are served from here. |
| quotr.io (links from F6S, MPN podcast, Parsers VC, BIA, MBI) | Legacy | Third parties still point to the old domain. |

---

## 2. Entity facts: what each source says

This is the core problem for AI engines. When sources disagree, engines hedge or pick the wrong one. The correct values are **TO CONFIRM with Quotr** and belong in [[Entity fact sheet]].

| Fact | quotr.ai /disambiguation/ | Other quotr.ai pages | Crunchbase | PitchBook | Podcast (MPN) | Other |
|---|---|---|---|---|---|---|
| Legal entity | FLOZ Inc | Homepage schema legalName "Quotr.ai"; /terms: "FLOZ INC., a Delaware corporation with offices at 495 27th Ave Unit 8, San Francisco" (search-index text adds "doing business as 'Quotr'") | Legal name "Quotr" | — | "Quotr.io" | F6S: "Made by FLOZ" |
| Founded | 2023 | — | 2023 | **2024** | — | G2 (per Perplexity): 2023 |
| HQ | **Berkeley, CA** | Blog boilerplate: "based in San Francisco"; /terms: 495 27th Ave Unit 8, San Francisco, CA 94121 | Berkeley (location field and FAQ) vs "headquartered in San Francisco" (About text); both confirmed on the page | 495 27th Avenue, Suite 8, San Francisco | "team in San Francisco" | G2 (per Perplexity): Berkeley |
| Founders | Junzhe Shi only ("Co-Founder") | /about-us/: Hanyang Liu (CEO) and Junzhe Shi (CTO) as co-founders | Hanyang Liu and Junzhe Shi | — | Hanyang Liu, "founder" and "CEO" | LinkedIn: both "Co-Founder @ Quotr" |
| Funding | $200K pre-seed (SkyDeck) + $3.5M seed (Llama Ventures) "as of December 25, 2025" | Not on /about-us/ | One Seed round, lead Llama Ventures | One seed round dated 01-Jan-2025, no amount shown; investors SkyDeck Fund, Llama Ventures, Sky Arc Capital. (A "$190K seed, 15-Oct-2024" figure appears only in Perplexity answers, not on PitchBook.) | "has raised $5 million" (confirmed on the page) | Caplight "does not fully agree" |
| Headcount | 11–50 | — | 11–50 | 10 | — | — |
| Factory network | 220+ vetted factories; up to 50% below retail | Homepage and /procurement/: "50+ audited manufacturers in Foshan & Guangdong"; indexed service/developer pages: "220+ factories, including 30+ audited manufacturers"; savings "40–55%" and "40–50%" | 50+ factories; 40–55% below distributor markup | — | "cut … material costs by 50%" (episode title) | Product Hunt: "40-50% material savings" |
| Entry price | Lite $79.90 / Plus $299.90 / Enterprise | About 13 Quotr URLs (mostly blog posts, plus the indexed /contractors copy): "Solo $299.90 / Team $499.90"; llms.txt: "1 User $299.90 / 2–10 Users $499.90" | — | — | — | Nomic: "From ~$299.90/month"; Octopus Builds: Solo $299.90 / Team $499.90 |
| Product described as | AI takeoff, estimating, bids, procurement | Same | AI + construction SaaS; one search summary: "Revit integration to help architects" (old) | "construction drawings and BIM models" | Material cost cutting | F6S: Revit plug-in (old) |
| Domain / handles | Lists quotrio / quotr_io / QuotrIO and QuotrAI | Footer: quotrai / quotr_ai / QuotrAI | linkedin quotrai | linkedin quotrai, twitter quotr_ai | quotr.io, x.com/quotr_io | Product Hunt: quotr_ai, quotrai, GitHub Quotr-io |

---

## 3. Third-party "best of" lists: who includes Quotr

These are the lists AI engines lean on for "best X" and "X alternatives" questions. For where each one is cited, see [[Citation sources map]].

### 3a. AI takeoff and estimating roundups

| List | Publisher type | Quotr included? | How checked |
|---|---|---|---|
| [ConstructConnect, "AI-Powered Takeoff and Estimating Software: … Top Players in 2026" (Aug 3, 2026)](https://www.constructconnect.com/blog/ai-powered-takeoff-and-estimating-software-a-contractors-guide-to-the-top-players-in-2026) | Vendor network (owns On-Screen Takeoff and PlanSwift) | **No.** Covers On-Screen Takeoff, PlanSwift, STACK, eTakeoff, InEight, Procore Estimating, Togal.AI, Beam AI, xBuild. | Page read |
| [The Digital Project Manager, best AI estimating](https://thedigitalprojectmanager.com/tools/best-ai-estimating-software/) | Independent listicle | No | Search check |
| [TDPM, best AI construction estimating](https://thedigitalprojectmanager.com/tools/best-ai-construction-estimating-software/) | Independent listicle | No (not seen) | AI citation only |
| [Construction Coverage, takeoff software](https://constructioncoverage.com/takeoff-software) | Independent listicle | No | Search check |
| [ContraVault, 10 best AI takeoff tools 2026](https://www.contravault.com/blog/10-best-ai-takeoff-software-tools-for-construction-in-2026) | AI-native vendor | No | Search check |
| [ContraVault, 10 best AI construction estimating 2026](https://www.contravault.com/blog/10-best-ai-construction-estimating-softwares-in-2026) | AI-native vendor | No (not seen) | AI citation only |
| [Construction Placements, best AI estimating](https://www.constructionplacements.com/best-ai-estimating-software-construction/) | Independent listicle | No | Search check |
| [Dan Cumberland Labs, AI construction estimating](https://dancumberlandlabs.com/blog/ai-construction-estimating-software/) | Independent / agency | No | Search check |
| [Handoff, 6 best AI construction estimating 2026](https://www.handoff.ai/blog/6-best-ai-construction-estimating-software-2026-picks-compared) | Competitor (ranks itself #1) | Not seen | AI citation only |
| [Layer3 Labs, best AI tools for construction](https://www.layer3labs.io/comparisons/best-ai-tools-for-construction) | Unknown | Unknown | AI citation only |
| [learn.g2.com, best construction estimating](https://learn.g2.com/best-construction-estimating-software) | Review-site blog | Unknown | AI citation only |
| [Robotics & Automation News, 6 AI estimating tools tested](https://roboticsandautomationnews.com/2026/02/19/6-ai-construction-estimating-software-tested-on-complex-project-accuracy/98967/) | Trade/tech media | Unknown | AI citation only |
| [BuildVision AI, best takeoff software](https://www.buildvisionai.com/best-construction-takeoff-software) | Competitor | No | Search check |
| [AppIntent, AI takeoff](https://www.appintent.com/software/construction/AI/Takeoff/) | Directory | No | Search check |
| PalCode, Aginera, Meltplan, Struvia, ConTechFinder, Projul, OneCrew, Bridgit, ScopeTakeoff | Mostly vendor blogs | No (PalCode's takeoff list may mention Quotr, per Perplexity) | Search check |
| [Foreman AI, 9 best AI takeoff tools 2026](https://foremanai.co/blog/best-ai-takeoff-software-2026), Easy Takeoffs, SoftwareWorld, Slashdot, topbusinesssoftware, gitnux, worldmetrics | Vendor blogs / directories / list farms | No ("did not find a specific product or review called Quotr.ai") | Search check |
| [Nomic, Kreo alternatives](https://www.nomic.ai/compare/kreo-alternatives) | Adjacent vendor | **Yes, #5 of 7** (stale price, no procurement) | Page read |

### 3b. Directory "alternatives" pages for the tools buyers switch from

| Page | Quotr included? |
|---|---|
| [G2 Togal alternatives](https://www.g2.com/products/togal-ai/competitors/alternatives), [Capterra Togal alternatives](https://www.capterra.com/p/10001876/Togal-AI/alternatives/), [SourceForge Togal alternatives](https://sourceforge.net/software/product/Togal.AI/alternatives), [TrustRadius Togal competitors](https://www.trustradius.com/products/togal.ai/competitors), [SoftwareWorld](https://www.softwareworld.co/competitors/togalai-alternatives/), [Krowdbase](https://www.krowdbase.com/alternatives/togal.ai) | No (search check). These rank above Quotr's own Togal posts for "Togal.AI alternatives 2026". |
| [G2 PlanSwift alternatives](https://www.g2.com/products/planswift/competitors/alternatives), [Capterra PlanSwift alternatives](https://www.capterra.com/p/70808/PlanSwift/alternatives/) | No (search check) |
| [G2 STACK alternatives](https://www.g2.com/products/stack-takeoff-estimate/competitors/alternatives), [GetApp Togal alternatives](https://www.getapp.com/construction-software/a/togal-ai/alternatives/), [Software Advice takeoff comparison](https://www.softwareadvice.com/construction/takeoff-software-comparison/) | No (search check) |

Without reviews, Quotr cannot appear on these pages. They are built largely from review counts and category fit.

### 3c. Procurement and factory-direct roundups

| List | Quotr included? |
|---|---|
| [Capterra procurement roundup](https://www.capterra.com/resources/best-procurement-software-reviews-analysis/) | No |
| [Field Materials, top 2026 construction procurement software](https://www.fieldmaterials.com/blog/top-2026-construction-procurement-software-construction-material-management-software-providers) | No (competitor-owned) |
| [WorldMetrics](https://worldmetrics.org/best/construction-procurement-software/), [Gitnux](https://gitnux.org/best/construction-purchasing-software/), [WifiTalents](https://wifitalents.com/best/construction-material-management-software/) | No |
| [F6S construction procurement category](https://www.f6s.com/software/category/construction-procurement) | No |
| [Archdesk procurement tools list](https://archdesk.com/blog/the-best-construction-procurement-software-tools) | No |

Perplexity said of this category: "the search results do not show a single platform explicitly marketed as a factory-direct marketplace for all building materials." This is open ground. See [[White space]].

---

## 4. Competitor off-site footprint (for comparison)

Ratings "as of July 2026" from ConstructConnect's guide, unless noted. Caution: that guide labels its review sources inconsistently (it called STACK's Capterra count a G2 count in one place), so treat the site labels as approximate.

| Platform | G2 rating | G2 reviews | Other |
|---|---|---|---|
| Togal.AI | 4.8 | 60 | G2 "Highest Performer" badge (July 2026). G2 seller page shows "Read 57 Reviews". Raised $22.65M in total. |
| Beam AI | 4.9 | 30 | Perplexity reported 37 on a G2 compare page (different date). Beam's own AHR Expo press release says "rated 4.9 on Capterra and Software Advice". Press releases syndicated to PR Newswire, Morningstar, Yahoo Finance. |
| STACK | Not confirmed | **Under 100** (G2 seller page title "Read 78 Reviews"; Perplexity reported 93) | **Capterra: about 1,400 reviews** (ConstructConnect's table: "4.5/5.0 (1,398 reviews, Capterra)"; Perplexity: 4.0 from 1,399). The fact-check resolved this: 1,398 is the Capterra count, not G2. Publishes "Seven G2 Awards for Summer 2026". |
| On-Screen Takeoff | 4.4 | 148 | — |
| PlanSwift | 4.3 | 35 | — |
| Procore Estimating | 4.6 | 4,205 | — |
| InEight | 4.1 | 46 | — |
| eTakeoff | 4.7 | 5 | — |
| Kreo | 4.5 | 32 (search summary); seller page "39 Reviews" | — |
| Buildxact | — | — | Capterra 4.6 (Buildxact's newsroom: "4.6 out of 5 from more than 150 verified reviews"; search summaries show about 165–174); "Top Home Builder Solution" by Capterra and Software Advice for 2026. |
| **Quotr.ai** | **reported 0.0 (unverified)** | **reported 0 (unverified)** | No Capterra, GetApp or Software Advice listing found. Product Hunt 0 upvotes. |

More in [[Competitor landscape]].

---

## 5. Name collisions ("other Quotrs")

At least 8 unrelated products share the name. Several target the same contractor audience, so the risk is real brand confusion, not just the generic word "quotation".

| Product | What it is | URL | Seen in AI answers? |
|---|---|---|---|
| Quotr Pro – AI Estimate Maker / Contractor Quotes | Contractor quotes app (App Store id6759211998); different developer. Quotr's /disambiguation/ names quotr.pro as its domain. | [App Store (US)](https://apps.apple.com/us/app/quotr-pro-ai-estimate-maker/id6759211998) | **Yes.** Its 37 ratings / 4.7 were presented as Quotr.ai's trust signal (B3, both runs and the re-run). It was the #1 web result for "Quotr.ai reviews". |
| Quotr (quotrhq.com) | "AI-Powered Job Management for Contractors" | https://quotrhq.com/ | Yes (B5) |
| Caplight "quotrhq" | Company page for quotrhq | https://www.caplight.com/company/quotrhq | Yes ("What is Quotr?") |
| quotr.software | "Quotr — AI Quotes for Trade Pros" | https://quotr.software/ | Not seen |
| getquotr.com | Lawn-care quoting / lead conversion | https://www.getquotr.com/ | Yes (B3, B5) |
| joinquotr.com | Print-shop quoting | https://www.joinquotr.com/ | Not seen |
| quotr.ichii.io | HubSpot quote generator | https://quotr.ichii.io/ | Not seen |
| Quotr – AI Quotes | Photo-based trade quotes app (id6785211053) | [App Store (CA)](https://apps.apple.com/ca/app/quotr-ai-quotes/id6785211053) | Yes (flagged as separate app) |
| QUOTR: Quotes & Invoices / Devis & Facture | French quotes and invoices app (id6780415475) | [App Store](https://apps.apple.com/us/app/quotr-devis-facture/id6780415475?l=fr-FR) | Yes (B3, B5) |
| Quotr – Daily Motivation | Quote-widget app (id6749962592) | [App Store](https://apps.apple.com/pt/app/quotr-daily-motivation/id6749962592) | Yes (B5) |
| GitHub repos | andrerpena/quotr (stock-quote CLI); code-boxx/quotr | https://github.com/andrerpena/quotr | Yes ("What is Quotr?") |

Directory look-alikes: Capterra shows QuoTrak and a "Quoting" category; G2 shows "Quoters" and (in an alternatives answer) "Quartr", a different company.

---

## 6. Legacy positioning still live off-site

- **F6S** describes the old Revit plug-in product ([F6S](https://www.f6s.com/software/quotr)).
- **YouTube** still hosts "How To Use Quotr Estimate | Cost Estimation Revit Extension" ([video](https://www.youtube.com/watch?v=zNIXcvCbWAg)).
- A **search summary** described Quotr.ai as "an AI assistant providing real-time cost estimation and Revit integration to help architects save time", sourced to LinkedIn and Crunchbase.
- **Product Hunt** files Quotr under "Real estate".

---

## 7. How AI engines use (and misuse) the off-site record

Short version here; full detail in [[AI visibility baseline]].

- **"What is Quotr?"** Perplexity opens with "Quotr is a name used by several different products" and lists namesakes before settling on Quotr.ai.
- **"Is Quotr.ai legit? Reviews"** Perplexity borrows the Quotr Pro app's 4.7 rating, says "G2 shows 0 reviews for QUOTR", and concludes "plausibly legitimate but not independently well-validated".
- **Funding and founders:** Perplexity flags that Quotr's $3.5M claim disagrees with "a $190K seed round" it attributes to PitchBook. PitchBook's live page shows no such amount, so this part of the answer is itself an error.
- **A wrong merge:** a search summary about Hanyang Liu said "The company raised a $4.2M seed round led by Initialized Capital and released a state-of-the-art reranker zerank-1". No Quotr source supports this; it appears to be another startup's news merged into Quotr's record. Thin, inconsistent entity data makes this kind of error more likely.

---

## 8. Gaps, ranked by impact and ease

Based on the research notes' own ranking (realism × impact). Plans live in [[Off-site earned media plan]].

| # | Gap | Why it matters | Effort |
|---|---|---|---|
| 1 | **No confirmed reviews on G2 (reportedly 0); no Capterra / GetApp / Software Advice listing** | Review directories were the #1 and #2 most-cited domains in our tests (9 of 32 prompts each). "Alternatives" answers and editor roundups are built from review counts. Since G2 now owns Capterra, GetApp and Software Advice, one review program can feed all four. | Medium (customer outreach) |
| 2 | **Stale and conflicting third-party profiles** (F6S unclaimed with Revit copy; Crunchbase HQ and factory count; PitchBook founding year, HQ, investors, round; Product Hunt "Real estate"; podcast notes with quotr.io and $5M; Nomic and Octopus Builds with the old $299.90 price) | AI engines use these to confirm facts. Today they create doubt. | Low (hours) |
| 3 | **Split handles** (quotrio / quotr_io / QuotrIO vs quotrai / quotr_ai / QuotrAI) | Mixed signals about which accounts are official. | Low |
| 4 | **Missing from neutral "best of" lists** | Category answers draw on these. Quotr was absent from all heavily cited ones. | Medium (editor outreach, demo accounts) |
| 5 | **Missing from procurement roundups** | Uncontested category in AI answers. | Medium |
| 6 | **No press for the $3.5M seed; no trade-press bylines** | A wire story would give AI engines an independent source for funding, HQ and category. Founders (architect; Berkeley engineering PhD) have the credentials for bylines. | Medium |
| 7 | **No Wikidata item** | A realistic, factual entity record (FLOZ Inc, founding date, HQ, website, social IDs). Low-cost hygiene; there is no evidence it is a lever (fact-check note H16 in the GEO-evidence verification file). A Wikipedia article is not realistic until independent press exists; treat the podcast's "Wikipedia hack" with caution. | Low |
| 8 | **Zero Reddit presence** | r/estimators was cited in 6 of 32 prompts, and threads ask whether AI takeoff works. The community is sceptical, so only transparent, founder-disclosed help will work. | Ongoing |
| 9 | **YouTube never cited; channel split** | Industry studies report YouTube among the most-cited domains in AI Overviews, and YouTube mentions correlate strongly with AI visibility (a correlation, not proven cause). Buyers also watch demos. See [[Signals that matter]]. | Medium |
| 10 | **Legacy and staging hosts in the index** (quotr.io/pricing, firetips.quotr.io, test.quotr.io) | Stale copy can resurface in AI answers. | Low (technical) |

---

## 9. Open questions (TO CONFIRM with Quotr)

- The true G2 profile contents (review count, categories, display name). Can the listing be renamed from "quotr-io" to "Quotr.ai"?
- Correct HQ (Berkeley or San Francisco), founding year (2023 or 2024), founder list (is Hanyang Liu a co-founder?), and funding (is $3.5M the total, or $5M as the podcast says? who is Sky Arc Capital? is there any real "$190K" round behind the figure Perplexity attributes to PitchBook?).
- Which factory count and savings figure is current (220+, 50+ or 30+ factories; up to 50%, 40–50% or 40–55%)?
- Does quotr.io 301-redirect to quotr.ai? Is test.quotr.io blocked from indexing?
- Is youtube.com/@QuotrIO ("QuoTrio") Quotr's old channel? Is LinkedIn "flozdesign" related?
- Does the iHeart "AEC Tech Journeys" episode feature Quotr?
- LinkedIn follower count, YouTube subscriber and view counts, X activity.
- Does the Procore Construction Network profile have current content? Any Procore App Marketplace plans?
- Any backlinks data (not measured in this research).

---

## Related pages

- [[Presence scorecard]] — scores for reviews, lists, community and press
- [[AI visibility baseline]] — how AI engines answer, prompt by prompt
- [[Website audit]] — on-site facts that should match these profiles
- [[GEO tactics already used]] — including the profile link list on /disambiguation/
- [[Entity fact sheet]] — the single source of truth for company facts
- [[Citation sources map]] — which third-party sites AI engines cite most
- [[Competitor landscape]] — competitor footprints in more detail
- [[Off-site earned media plan]] — the plan to close these gaps
- [[Review generation]] and [[Listicle and PR outreach]] — step-by-step off-site playbooks (more in the same folder)
