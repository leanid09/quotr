---
type: baseline
description: 'A fair list of the 19 things that held back the Quotr blog and GEO work in 2026, with evidence, context and a fix for each.'
last_verified: 2026-09-26
verify_every_days: 90
aliases:
- Mistakes review
---
# What went wrong

> [!abstract] What this page is for
> A fair, evidence-based list of what held back Quotr's blog and GEO (generative engine optimisation: getting named in AI answers) work from March to September 2026. Each item says what happened, how we know, why it matters and what to do, with links to the task that fixes it. Use it to explain the starting point to Quotr and to justify the plan, alongside the credit in "What Quotr got right".

> [!info]- Sources
> Vault notes: [[GEO tactics already used]], [[AI visibility baseline]], [[Website audit]], [[Off-site presence]], [[Presence scorecard]], [[Entity fact sheet]], [[Tracking set]], [[Optimize vs create]], [[Content priorities]], [[30-60-90 plan]], [[GEO writing style guide]], [[KPIs and dashboard]], [[Togal AI]], [[STACK]], the task notes in the action plan and the open questions ([[Q-15 Turnaround]], [[Q-26 Primary audience]], [[Q-40 Access and history]] and others named below).
> Data files: the mistakes review of 2026-09-26 (19 findings, each checked by an evidence skeptic and a fairness skeptic; this page uses their corrected wording); the computed blog statistics of 2026-09-26 (volume, timing, clusters, old prices, AI citations, web search checks); the blog post ID list of 2026-09-26; the post-by-post data of 2026-09-26; and the Google claims register of 2026-09-26 (claim IDs such as RANK-13).

---

## The short version

- **We found 19 problems. All 19 held up under review,** but most were softened: the evidence was weaker, or the context fairer, than the first draft said. This page uses the corrected versions.
- **Most urgent (small fix):** retired prices still showed on about 13 posts (up to 16) and in llms.txt 11 days after the 14 September price change. In 2 of 8 brand prompts, Perplexity quoted an entry price about 3.75 times the real one ([[#W-01 Old prices still showing after the September price change|W-01]]).
- **Biggest (large fix):** almost all online effort went into Quotr's own posts. AI engines read them but rarely name Quotr: 1 of 32 unbranded prompts, about 0.7% share of voice. Reviews, neutral lists and press are missing ([[#W-02 Almost no third-party proof|W-02]]).
- **Facts and naming:** Quotr's own pages give different turnaround, factory and savings numbers. When AI uses Quotr's figures, it often drops the Quotr name (W-03, W-04, W-05).
- **Format bets:** the 17 best-of lists were not used for any tested unbranded prompt. The alternatives posts and the Service posts did get used (W-06, W-07, W-14).
- **Housekeeping:** the blog sitemap is missing from robots.txt, dates disagree, test-site copies are still in search indexes, and many posts are signed by the company (W-15 to W-19).
- **Fair view:** these are common growing pains for a seed-stage team that published 96 posts in about six months. Most fixes are already tasks in the [[30-60-90 plan]]. Fix facts now; hold merges and redirects until Google's September spam update ends, around 2026-10-08 (RANK-21).

> [!note] Words used on this page
> - **Prompt:** a question typed into an AI tool. **Unbranded prompt:** one that does not name Quotr.
> - **Retrieved / cited / named:** the AI looked at a Quotr page / used it as a source / said "Quotr" in the answer.
> - **Test IDs:** B, C, N, O, P, S and V codes (for example C12) are prompts from the 2026-09-25 Perplexity tests in [[AI visibility baseline]]. T01-T53 are tracked prompts in [[Tracking set]]. E-### and L-### are prompt library IDs.
> - **p value:** how likely a pattern is to be chance. Below 0.05 usually means "probably not chance". Small samples still need caution.
> - **Claim IDs** (RANK-, QUALITY-, AI-, INDEX-, FRESH-, OTHER-, GSC-): Google and industry facts from the Google claims register. RANK and GSC claims were found by live web search on 2026-09-26 and were **not** independently re-checked (the search limit ran out). The others were carried over from the 2026-09-25 research and were fact-checked then only where the vault says so.

---

## At a glance

Impact: how much it holds back Quotr's AI visibility or trust. Effort: S = small, M = medium, L = large.

| ID | What went wrong | Impact | Effort | Fix in a few words | Related tasks |
|---|---|---|---|---|---|
| W-01 | Old prices still on about 13 posts (up to 16) and in llms.txt | High | S | Replace with one dated price line; ask for a re-crawl | [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere\|A2]], [[A4 Fix llms.txt\|A4]], [[A9 Sitemaps and lastmod dates\|A9]], [[B12 Follow up correction outreach\|B12]] |
| W-02 | Almost no third-party proof: reviews, neutral lists, press | High | L | Move about a fifth of effort to reviews, lists and PR | [[A13 Directory and profile clean-up\|A13]], [[A14 Launch the G2 review program\|A14]], [[B1 Seed-round announcement\|B1]], [[B2 Outreach to the best of lists AI cites (Tier A)\|B2]], [[B6 YouTube - one channel, and the series starts\|B6]], [[B7 Founder presence - LinkedIn and estimator communities\|B7]], [[B11 Review program wave 2\|B11]], [[C2 Press pitches built on the dataset\|C2]], [[C5 Tier B and procurement-category list outreach\|C5]], [[C7 Review drive - first 10 genuine reviews\|C7]], [[D8 Off-site scale-up - ConstructConnect pitch after 10+ reviews; reviews to 25-30\|D8]] |
| W-03 | Quotr's own facts differ from page to page | High | M | Sign off one fact sheet; align every page | [[A1 Agree and sign off one fact sheet\|A1]], [[A3 Fact-fix sweep, part 2 - every other conflicting fact\|A3]], [[A4 Fix llms.txt\|A4]], [[A5 Rewrite disambiguation as a plain company facts page\|A5]], [[A16 Add a human edit and fact-check step for AI-assisted drafts\|A16]] |
| W-04 | AI uses Quotr's figures but drops the Quotr name | High | S | Put "Quotr.ai" in the same sentence as each figure | [[A8 Put the Quotr name inside key facts on the pages AI already reads\|A8]], [[A1 Agree and sign off one fact sheet\|A1]], [[A3 Fact-fix sweep, part 2 - every other conflicting fact\|A3]], [[D3 AI takeoff accuracy benchmark + How we test page (R-41)\|D3]] |
| W-05 | Little original data; headline numbers have no method | High | L | Publish methods, datasets, tools and numbers-first case studies | [[A8 Put the Quotr name inside key facts on the pages AI already reads\|A8]], [[A3 Fact-fix sweep, part 2 - every other conflicting fact\|A3]], [[B4 Proof pages - case studies with numbers\|B4]], [[B5 Prepare the first original dataset\|B5]], [[B9 Spec and start building the first two free tools\|B9]], [[C1 Publish the first original dataset\|C1]], [[C2 Press pitches built on the dataset\|C2]], [[C3 Ship the first free tools\|C3]], [[C4 LA fire-rebuild cost guide\|C4]], [[D2 Residential and multifamily cost per sq ft by trade (R-40)\|D2]], [[D3 AI takeoff accuracy benchmark + How we test page (R-41)\|D3]], [[D4 Second price-index edition, Q1 2027 (R-51)\|D4]], [[D7 More numbers-first case studies; Service by the numbers; security page\|D7]] |
| W-06 | The Service pivot was built as a dozen similar pages | High | M | One Service hub plus 3-4 distinct pages | [[A1 Agree and sign off one fact sheet\|A1]], [[A3 Fact-fix sweep, part 2 - every other conflicting fact\|A3]], [[A8 Put the Quotr name inside key facts on the pages AI already reads\|A8]], [[A12 Merge duplicate pages\|A12]], [[D7 More numbers-first case studies; Service by the numbers; security page\|D7]] |
| W-07 | 17 best-of lists were not used for tested unbranded prompts | High | M | No new self-ranked lists; cut to 6-8 honest ones | [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere\|A2]], [[A12 Merge duplicate pages\|A12]], [[B2 Outreach to the best of lists AI cites (Tier A)\|B2]], [[C5 Tier B and procurement-category list outreach\|C5]], [[D6 Honest comparisons - four-way table, Buildxact, Quotr.ai alternatives\|D6]] |
| W-08 | Little content for the residential and multifamily buyers Quotr names | High | L | Answer Q-26, then build hubs or drop the claim | [[A1 Agree and sign off one fact sheet\|A1]], [[B10 Residential hub; decide on the thin trade pages\|B10]], [[C4 LA fire-rebuild cost guide\|C4]], [[C6 Developer hub, deep electrical page, integrations page, one honest comparison\|C6]], [[D2 Residential and multifamily cost per sq ft by trade (R-40)\|D2]], [[D5 Persona hubs and deep trade pages\|D5]] |
| W-09 | Procurement is described mainly in Quotr's own terms | High | M | Rewrite around buyer wording; one lead page | [[A1 Agree and sign off one fact sheet\|A1]], [[B8 Procurement and tariff decision guides\|B8]], [[B9 Spec and start building the first two free tools\|B9]], [[C3 Ship the first free tools\|C3]], [[C5 Tier B and procurement-category list outreach\|C5]], [[D1 Tariff data story and import guides (R-29 to R-32)\|D1]] |
| W-10 | 15 of 36 checked posts did not come back in web search | High | M | Get Search Console; audit indexing and bot access | [[A15 Measurement setup and multi-engine baseline\|A15]], [[A11 Confirm Cloudflare lets AI search bots in\|A11]], [[A12 Merge duplicate pages\|A12]] |
| W-11 | About 12 posts duplicate another Quotr page | Medium | M | Merge with redirects after the spam update | [[A12 Merge duplicate pages\|A12]], [[A15 Measurement setup and multi-engine baseline\|A15]] |
| W-12 | Output grew faster than the editing check | Medium | S | Named editor sign-off; 8-12 pieces a month | [[A16 Add a human edit and fact-check step for AI-assisted drafts\|A16]], [[A6 Editorial sweep\|A6]], [[A12 Merge duplicate pages\|A12]] |
| W-13 | Statistics and competitor facts went out without sources | Medium | M | Link and date every fact; fix the wrong ones | [[A6 Editorial sweep\|A6]], [[A16 Add a human edit and fact-check step for AI-assisted drafts\|A16]], [[D6 Honest comparisons - four-way table, Buildxact, Quotr.ai alternatives\|D6]] |
| W-14 | Comparison coverage is lopsided | Medium | M | Merge the Togal pair; honest "best for" pages | [[A12 Merge duplicate pages\|A12]], [[A6 Editorial sweep\|A6]], [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere\|A2]], [[D6 Honest comparisons - four-way table, Buildxact, Quotr.ai alternatives\|D6]], [[C6 Developer hub, deep electrical page, integrations page, one honest comparison\|C6]] |
| W-15 | Crawl paths to the posts are thin or broken | Medium | S | Blog sitemap in robots.txt; plain-HTML archive; fix links | [[A9 Sitemaps and lastmod dates\|A9]], [[A10 De-index the staging site; tidy legacy hosts and broken links\|A10]], [[A15 Measurement setup and multi-engine baseline\|A15]], [[A16 Add a human edit and fact-check step for AI-assisted drafts\|A16]] |
| W-16 | Date signals disagree; years in evergreen URLs | Medium | M | One real date field; no year in new URLs | [[A9 Sitemaps and lastmod dates\|A9]], [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere\|A2]], [[A12 Merge duplicate pages\|A12]] |
| W-17 | Test-site and old-domain copies still in search indexes | Medium | S | Noindex, removal requests, redirects | [[A10 De-index the staging site; tidy legacy hosts and broken links\|A10]], [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere\|A2]], [[A4 Fix llms.txt\|A4]] |
| W-18 | Company bylines instead of named authors | Low-medium | M | Named authors, author pages, correct schema | [[A7 Named author bylines and author pages\|A7]] |
| W-19 | llms.txt not updated, and it asks AI to cite Quotr | Low | S | Update it; delete the "Recommendation" block | [[A4 Fix llms.txt\|A4]], [[A5 Rewrite disambiguation as a plain company facts page\|A5]] |

---

## W-01 Old prices still showing after the September price change

**Impact:** high · **Effort:** S · **Confidence:** high that the problem exists; medium on the exact number of posts

**What happened**
- Quotr changed its prices on 2026-09-14 and announced it in [[BP-93 new pricing|BP-93]]: Quotr.ai Lite $79.90 per seat per month, Plus $299.90, Enterprise custom.
- On 2026-09-25, 11 days later, the retired "Solo $299.90 / Team $499.90" plans, or "from $299.90", still showed for about 13 posts. Up to 3 more may carry them.
- llms.txt (a plain summary file of the site for AI tools) shows an even older plan set: "1 User Plan" and "2-10 Users Plan".
- Prices seem to be typed into each post by hand, not pulled from one shared place (inference).
- Three new posts went out in those 11 days. We found no owner for price updates and no list of the pages that hold prices.
- Fair context: the price was correct when the posts were written. At the change they had been live a median of 82 days (range 34-118). 11 days is a short window.
- Fair context: asked directly "Quotr.ai pricing" (B2), Perplexity gave the correct prices. The wrong price shows up in comparison and brand answers.

**Evidence**
- Strength varies by post. 2 posts were read on the live page ([[BP-51 stack alternative|BP-51]], [[BP-43 best togal ai alternatives 2026|BP-43]]). About 8 showed the old price in search-index text (the copy a search engine stored). 3 showed it only through AI answers. 3 more are weaker matches that are not on the vault list. Stored copies can lag, so some live pages may already be fixed (blog statistics §9; [[GEO tactics already used]] tactic 26).
- Perplexity repeated the old entry price in 2 of 8 brand prompts: B4 ("Quotr.ai vs Togal.AI", on both runs) and V2. It said Quotr starts "from about $299.90/month", about 3.75 times the real $79.90 ([[AI visibility baseline]]). B2 was correct but also mentioned the older Solo/Team packaging.
- Perplexity retrieved or cited 11 of the 16 flagged posts, against 11 of the other 80 (p about 0.00002). Caveat: 3 of the 16 were flagged because Perplexity cited them with the old price. Without them, p is about 0.0005, still strong. The other 80 posts are unchecked, not clean.
- The stack-alternative FAQ, read directly, says "Quotr.ai is a cheaper entry point at $299.90/month". $299.90 is now the Plus price, so old and new plans get mixed up.
- llms.txt, read directly: "1 User Plan: $299.90/month (as low as $249/seat/month billed annually)" and "2-10 Users Plan: $499.90/month".
- Two outside sites copied the old price: Nomic and Octopus Builds ([[Entity fact sheet]] §4).
- AI-17: Google shows an AI Overview (the AI summary above the results) on 83.4% of price and cost searches, 95.4% of "X vs Y" searches and 81.3% of "best of" searches (Seer Interactive). These pages get summarised before anyone clicks.
- Tracked prompt T22 "cheapest AI takeoff software" is Absent. The old price is not shown to be the cause.

**Why it matters**
- Buyers who ask AI to compare Quotr with rivals (B4, V2) hear an entry price about 3.75 times too high.
- They are also shown a $499.90 "Team" plan that no longer exists.
- Inference: this undercuts the $79.90 Lite plan, which is aimed at price-sensitive buyers.
- When Quotr's own pages disagree, every other Quotr fact looks weaker.
- Two outside lists repeat the error, so it will outlast the on-site fix unless someone asks them to correct it.

**What to do**
1. Run [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]] now. It is a factual correction, so it does not need to wait for the spam update.
2. Search all 96 posts for "Solo", "Team (2", "$499.90", "from $299.90", "starts at $299.90", "1 User Plan", "$249/seat" and "$41/seat".
3. Replace each hit with one dated line: "Quotr.ai Lite $79.90 per seat per month; Plus $299.90; Enterprise custom (as of [date]; see /pricing/)".
4. Read the 3 weaker matches and the 4 unchecked posts (below) before counting them.
5. Better still, pull the price from one shared block or CMS field (a setting in the website's content system), so the next change updates every post at once.
6. Update the "last modified" date on each changed post, because the change is real. Ask Google Search Console and Bing to re-crawl (re-read) them. For Bing, IndexNow or Cloudflare Crawler Hints does this automatically.
7. Fix llms.txt ([[A4 Fix llms.txt|A4]]). Email Nomic and Octopus Builds, then follow up ([[B12 Follow up correction outreach|B12]]).
8. Write down a price-change routine: same-day update of posts, llms.txt and schema (the hidden labels that describe a page to machines); then a re-crawl request; then emails to outside sites.
9. Keep a refresh register: each URL, the facts on it that change, an owner and a next check date. Re-check pricing and comparison pages every quarter. No task covers this register yet.
10. Re-test B2, B4, V2 and T22 about four weeks after the fix.

**Posts affected**
- On the vault list (13): [[BP-51 stack alternative]], [[BP-77 structural steel estimating]], [[BP-54 best concrete estimating software 2026]], [[BP-47 ai bidding software construction]], [[BP-80 best ai bid software for construction]], [[BP-48 best flooring estimating software in 2026]], [[BP-46 best electrical estimating software 2026]], [[BP-83 rebar estimating and takeoff software]], [[BP-76 best glazing estimating software 2026]], [[BP-43 best togal ai alternatives 2026]], [[BP-24 best ai construction estimating software 2026]], [[BP-19 ai construction estimating software buyers guide]], [[BP-57 bluebeam alternative]].
- Weaker matches, read before counting (3): [[BP-20 quotr ai vs planswift ai takeoff procurement comparison 2026]], [[BP-32 best togal ai alternatives]], [[BP-81 best planswift alternatives 2026]] (for BP-81 the match is "likely misattributed").
- Not yet checked (4): [[BP-52 best plumbing estimating software 2026]], [[BP-55 best drywall estimating software in 2026]], [[BP-37 electrical estimating software buyers guide]], [[BP-64 trade estimating software]].
- Also llms.txt and the old stored copy of /contractors/ (see W-17).

![[Articles.base#Old price still showing]]

**Related tasks:** [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]] · [[A4 Fix llms.txt|A4]] · [[A9 Sitemaps and lastmod dates|A9]] · [[B12 Follow up correction outreach|B12]]

---

## W-02 Almost no third-party proof

**Impact:** high · **Effort:** L · **Confidence:** high

**What happened**
- Quotr published 96 posts in about six months. Outside quotr.ai we found about 20 items in about 20 months.
- Quotr did real launch and offline work: six 2026 trade shows, a founder podcast, a Product Hunt launch and a G2 profile. Little of it left a trace online that AI engines can cite.
- There was no press release for the seed round, the new pricing or any of the event appearances.
- We found no reviews, no place in the neutral lists AI cites, and no Reddit mention (one Perplexity check; our search tool cannot reach Reddit).
- So AI engines retrieve Quotr's pages but rarely name Quotr in unbranded answers: 1 of 32 prompts, on one engine.
- On-site work alone has not been enough so far.
- Fair context: Quotr is a seed-stage company about two years old. STACK, PlanSwift and Buildxact have had a decade or more to collect reviews and press. The fairer comparison is with young rivals such as Bobyard and xBuild.
- Fair context: some gaps may have reasons we cannot see. The funding figure is unsettled ($3.5M on the site, $5M on the March podcast), which makes a seed release harder. Reviews need customers who are willing to write them.

**Evidence**
- Only 1 wire release ever (EIN Presswire, February 2025, for FireTips). The Product Hunt launch got 0 upvotes. No earned trade press. This inventory relies mainly on the 2026-09-25 vault research; a fresh search could not be run.
- quotr.ai was in the source list for 6 of 32 unbranded prompts (tied 15th, level with reddit.com) and cited in 4. Quotr was named in 1 (3.1%). Share of voice (Quotr's share of all brand mentions) is about 0.7%, against about 6.5% each for STACK, PlanSwift and Buildxact. In category prompts Quotr was named in 0 of 15; fact-check re-runs of C1, C9 and C11 confirmed this ([[AI visibility baseline]]).
- The most-cited domains across the 32 unbranded prompts were capterra.com (9), g2.com (9) and sourceforge.net (8). The Construction Coverage, TDPM and ConstructConnect lists appear in 6-7 prompts each ([[Off-site presence]]).
- Quotr reportedly has 0 G2 reviews and no Capterra, GetApp or Software Advice listing. Rivals have about 30 to 4,000+ reviews.
- Quotr is missing from every heavily cited 2026 roundup that was checked. The 3 outside pages that name it are vendor or aggregator pages (Nomic, Octopus Builds, ForesightIQ). Two of them show the old price ([[Presence scorecard]]).
- The only unbranded naming (V1) cited ForesightIQ and Quotr's own post together. ForesightIQ's only source on Quotr is Quotr's blog. Inference: even a weak outside echo may help.
- Brand answers draw about 60-70% of their sources from Quotr itself. For "Is Quotr.ai legit?" (B3), Perplexity borrowed the unrelated Quotr Pro app's 4.7 rating, because Quotr.ai has no reviews of its own.
- AI-20 (Aleyda Solis, August 2026): third-party sources made up 82.3% of SaaS citations in AI answers. r/estimators was a source in 6 of 32 prompts.
- Young rivals distribute. Bobyard issued wire releases for its June and July 2026 trade launches (its December 2025 release was funding news). xBuild is in ConstructConnect's guide with a funding release and no G2 reviews (the link between the two is an inference). A copy of Handoff's list exists on LinkedIn Pulse. Buildxact turned a Capterra award into a news post (one example).

**Why it matters**
- Engines name and recommend brands that independent sources vouch for (inference from the test pattern).
- Without that, unbranded naming stays near 3% and share of voice near 0.7%, however many posts ship.
- Each new post adds to a story only Quotr tells, which engines appear to discount (inference).
- "Is Quotr legit?" is answered with an unrelated app's rating. That hurts trust at the moment of purchase.

**What to do**

Rebalance for the next 90 days: move about a fifth of content effort to distribution. The exact share is a judgement call.
1. A seed-round release using fact-sheet numbers, once the funding figure is settled ([[B1 Seed-round announcement|B1]]).
2. A G2 review programme, which also feeds Capterra, GetApp and Software Advice ([[A14 Launch the G2 review program|A14]], [[B11 Review program wave 2|B11]], [[C7 Review drive - first 10 genuine reviews|C7]]).
3. Outreach to the lists AI cites: Construction Coverage, TDPM, ConstructConnect and ContraVault ([[B2 Outreach to the best of lists AI cites (Tier A)|B2]], [[C5 Tier B and procurement-category list outreach|C5]], [[D8 Off-site scale-up - ConstructConnect pitch after 10+ reviews; reviews to 25-30|D8]]).
4. Founder bylines, monthly LinkedIn articles and answers in r/estimators that state the founder's role ([[B7 Founder presence - LinkedIn and estimator communities|B7]]).
5. One YouTube channel with a short video for each key page ([[B6 YouTube - one channel, and the series starts|B6]]).
6. A release or pitch for every launch, event and dataset, as Bobyard did for its 2026 trade launches ([[C2 Press pitches built on the dataset|C2]]).
7. Clean up old directory profiles ([[A13 Directory and profile clean-up|A13]]).
8. Track third-party pages that name Quotr every month (KPIs L7, L8 and L10 in [[KPIs and dashboard]]).

**Posts affected**
- The whole programme, most directly the 30 list and comparison posts, which compete with G2, Capterra and editors' lists.
- [[BP-93 new pricing]]: no release went with it.
- The 6 event recaps, which nothing outside the blog mentions apart from one Product Hunt comment: [[BP-73 ibs 2026 from the magic of orlando to the reality of ai implementation]], [[BP-07 dallas build expo 2026 recap]], [[BP-09 re forge sf 2026 recap]], [[BP-14 nhca build the builder 2026 recap]], [[BP-78 pcbc 2026 recap quotr ai takeoff service]], [[BP-88 sourcing building materials china cbd fair 2026]].

**Related tasks:** [[A13 Directory and profile clean-up|A13]] · [[A14 Launch the G2 review program|A14]] · [[B1 Seed-round announcement|B1]] · [[B2 Outreach to the best of lists AI cites (Tier A)|B2]] · [[B6 YouTube - one channel, and the series starts|B6]] · [[B7 Founder presence - LinkedIn and estimator communities|B7]] · [[B11 Review program wave 2|B11]] · [[C2 Press pitches built on the dataset|C2]] · [[C5 Tier B and procurement-category list outreach|C5]] · [[C7 Review drive - first 10 genuine reviews|C7]] · [[D8 Off-site scale-up - ConstructConnect pitch after 10+ reviews; reviews to 25-30|D8]]. See also [[Publishing beyond the blog]].

---

## W-03 Quotr's own facts differ from page to page

**Impact:** high · **Effort:** M · **Confidence:** high

**What happened**
- Most posts were written before there was one signed-off fact sheet, so each repeats the version the writer had (inference).
- Some differences may be legitimate: different services, rush options, or "network" versus "audited" factories. But the pages rarely say which case applies, so readers and engines see conflicts.
- Turnaround appears as "as fast as 24 hours", "1-3 business days", "3-4 business days by design" and "5-7 days". One post has "72 hours" in its URL.
- The factory count appears as "50+ audited manufacturers", "220+ vetted factories" or "220+ including 30+ audited".
- Savings appear as "40-55%", "40-50%" or "up to 50%". Time saved appears as 80%, 85% or 90%.
- The HQ city is split. The blog boilerplate says "Based in San Francisco", which matches the legal address in /terms. /disambiguation/ says Berkeley.
- Company email uses two domains: procurement@quotr.ai on a blog post and info@quotr.io in /terms.

**Evidence**
- [[Website audit]] §11 records 7 turnaround versions, 4 factory counts and 5 savings claims across Quotr pages.
- The [[Entity fact sheet]] conflict register (§4) has 31 rows. Row 10 shows time saved as 80% (/software/, ROI calculator), 85% (an older stored copy) and 90% (Product Hunt, Crunchbase).
- Confirmed on posts: turnaround on [[BP-25 quotr developer desk underwriting grade estimates 72 hours|BP-25]] (the URL), [[BP-91 electrical estimating services|BP-91]] and [[BP-89 precon on demand outsource bid cost estimation|BP-89]] (teasers). Factories and savings on [[BP-43 best togal ai alternatives 2026|BP-43]] ("50+", "40-55%", read directly) and [[BP-24 best ai construction estimating software 2026|BP-24]] ("220+", "40-50%", search summary). A second email domain on [[BP-69 construction procurement process|BP-69]].
- 5 more are flagged for checking, with no conflicting value recorded yet: [[BP-95 mep estimating services|BP-95]], [[BP-59 how developers source building materials|BP-59]], [[BP-88 sourcing building materials china cbd fair 2026|BP-88]], [[BP-12 is ai takeoff actually accurate yet|BP-12]], [[BP-18 ai that reads construction drawings chat with blueprints|BP-18]]. A keyword scan flags 24 of 96 posts.
- [[BP-51 stack alternative|BP-51]] and [[BP-92 scope gap construction|BP-92]] carry the San Francisco boilerplate. That matches the legal address, so they are not wrong. The HQ split is a site-wide decision ([[Q-01 Headquarters|Q-01]]).
- Engines notice. Perplexity: "Quotr publicly claims access to 50+ to 220+ factories, depending on the page". 5 of 8 brand prompts had accuracy problems. B3 called Quotr "plausibly legitimate but not independently well-validated" ([[AI visibility baseline]]).
- llms.txt says "220+ vetted factories in China" and "1-3 business days". The homepage and /procurement/ say "50+ audited manufacturers".
- Still open: [[Q-01 Headquarters|Q-01]], [[Q-05 Official contact email|Q-05]], [[Q-09 Factory network|Q-09]], [[Q-10 Savings|Q-10]], [[Q-15 Turnaround|Q-15]], [[Q-18 Accuracy|Q-18]], [[Q-19 Time saved|Q-19]].
- QUALITY-07: Google's AI features draw on pages in the normal Search index, so every indexed page's facts can feed AI answers. OTHER-03: Microsoft asks for facts that agree with authoritative sources. OTHER-04 (low confidence): Bing's AI layer checks whether key facts can be retrieved and are fresh.

**Why it matters**
- Turnaround, savings and factory count are the numbers buyers use to choose the Service and Procurement lines.
- When pages disagree, engines hedge ("depending on the page") or state one version without saying others exist.
- Inference: the conflicts make every other Quotr claim look less reliable.
- A buyer who reads "24 hours" on the homepage and "3-4 business days by design" on a service post may not know what to expect (inference).

**What to do**
1. Have the CEO sign off one value for each fact ([[A1 Agree and sign off one fact sheet|A1]]). This answers Q-01, Q-05, Q-09, Q-10, Q-15, Q-18 and Q-19.
2. Where two numbers are both true, say which case each covers (for example standard versus rush, or audited versus network factories).
3. Update the posts to match ([[A3 Fact-fix sweep, part 2 - every other conflicting fact|A3]]), starting with the 6 confirmed posts above, then the 5 flagged ones.
4. Then update the site pages and llms.txt ([[A4 Fix llms.txt|A4]], [[A5 Rewrite disambiguation as a plain company facts page|A5]]).
5. Put the boilerplate and key numbers in shared snippets, so they cannot drift again.
6. If a number in a URL stops being true (the "72 hours" URL), move the post to a URL without it with a 301 redirect (a permanent forward from the old address).
7. Show the per-square-foot Service rates on /service/ as well as /pricing/. "Project-based" and a rate can both be true, but one clear line is better.
8. Add "every fact matches the fact sheet" to the pre-publish checklist ([[A16 Add a human edit and fact-check step for AI-assisted drafts|A16]]).

**Posts affected**
- Confirmed (6): [[BP-25 quotr developer desk underwriting grade estimates 72 hours]], [[BP-91 electrical estimating services]], [[BP-89 precon on demand outsource bid cost estimation]], [[BP-43 best togal ai alternatives 2026]], [[BP-24 best ai construction estimating software 2026]], [[BP-69 construction procurement process]].
- To check (5): [[BP-95 mep estimating services]], [[BP-59 how developers source building materials]], [[BP-88 sourcing building materials china cbd fair 2026]], [[BP-12 is ai takeoff actually accurate yet]], [[BP-18 ai that reads construction drawings chat with blueprints]].
- Also the homepage, /service/, /pricing/, /procurement/, /disambiguation/, /terms and llms.txt.

**Related tasks:** [[A1 Agree and sign off one fact sheet|A1]] · [[A3 Fact-fix sweep, part 2 - every other conflicting fact|A3]] · [[A4 Fix llms.txt|A4]] · [[A5 Rewrite disambiguation as a plain company facts page|A5]] · [[A16 Add a human edit and fact-check step for AI-assisted drafts|A16]]

---

## W-04 AI uses Quotr's figures but drops the Quotr name

**Impact:** high · **Effort:** S · **Confidence:** medium (one engine, small counts)

**What happened**
- When Perplexity used a Quotr post in an unbranded answer, it usually kept the number or the steps and dropped the brand.
- The clearest case is C12, on the original run and the fact-check re-run. Its first citation was a Quotr post. It repeated Quotr's $0.25 / $0.10 per sq ft rates but credited them to "one outsourced estimating service" or "Some firms".
- Inference (the posts were not re-read): the rates are written without "Quotr.ai" in the same sentence. That is normal for an educational post, but it gives the engine nothing to credit.
- In other cases the engine took general facts from Quotr posts: market ranges (S9), PlanSwift facts (V3, S3) and plumbing steps (N2). Not naming Quotr there is normal.
- Credit where due: the posts are good enough to be picked, often as the first source. That is hard to earn.
- Caveat: rivals whose pages were cited were usually named, but they also have reviews, press and lists vouching for them (W-02). So part of this gap is probably brand strength, not wording (inference). Putting the brand in key sentences is a cheap test, not a guaranteed fix.

**Evidence**
- 8 of 51 unbranded Perplexity runs cited a Quotr blog post, and 2 more retrieved one without using it. Quotr was named in 2: V1 (about 15th of 17 brands) and S6, a prompt that copies Quotr's own wording.
- A Quotr post was the first citation, but Quotr was not named, in C12, P5 and N2. In C12 and P5 the answer named no brand at all.
- Rivals were often named when their own pages were cited: STACK 5 of 7 prompts, Buildxact 5 of 8, Easy Takeoffs 5 of 7, Beam AI 4 of 7, Kreo 3 of 5. Not always: Procore 3 of 8, Bluebeam 2 of 6. quotr.ai: 1 of 6.
- 26 of the 45 unbranded tracked prompts have a matching Quotr post. A Quotr page was used in 9 of those 26 (35%), but Quotr was named in only 2 (8%). T12 is marked "Cited, not named" ([[Tracking set]]).
- The facts that should carry the name also differ across pages: accuracy appears as 95-99% and 80-88% on scans, and Perplexity paraphrased it as 94-99% ([[Q-18 Accuracy|Q-18]]). Brand answers call the accuracy claims "self-published".
- Post age does not explain it. Cited and uncited posts had median ages of 82.5 and 99.5 days (p=0.27, no real difference). The Service posts had a median age of about 34 days, and 3 of 12 were already used.
- Data note: the blog statistics list 12 "cited" posts. The test notes show that [[BP-57 bluebeam alternative|BP-57]] and [[BP-17 how to do construction takeoff pdf blueprint|BP-17]] were not retrieved, so the true count is 10.
- OTHER-17: since May 2026, ChatGPT links named brands straight to their homepages. A named mention adds a direct route to the site.

**Why it matters**
- A citation without the name does not make buyers remember Quotr.
- It does not add to share of voice either.
- The buyer learns what outsourced estimating costs, but not who charges it.
- The clearest case sits on the Service pages, which bring in revenue.

**What to do**
1. Rewrite the key sentences so "Quotr.ai" sits in the same sentence as each number ([[A8 Put the Quotr name inside key facts on the pages AI already reads|A8]]). Example: "Quotr.ai's Estimation Service charges $0.25 per sq ft under 50,000 sq ft (September 2026)."
2. Start with [[BP-82 outsource construction estimating|BP-82]] and [[BP-85 commercial estimating services|BP-85]] (Quotr's own rates), then [[BP-12 is ai takeoff actually accurate yet|BP-12]] (Quotr's accuracy figures).
3. Use one approved value per fact from the fact sheet ([[A1 Agree and sign off one fact sheet|A1]], [[A3 Fact-fix sweep, part 2 - every other conflicting fact|A3]]).
4. Add a two-line "how we measured this" note, with date and sample, to the accuracy and turnaround figures ([[D3 AI takeoff accuracy benchmark + How we test page (R-41)|D3]]).
5. Make "brand in the fact" a rule for every new post (Rule 4 in [[GEO writing style guide]]).
6. After the re-crawl, re-run C12, P5, N2 and V3 twice each. Track KPI L4 ("Cited, not named" turned into named) in [[KPIs and dashboard]].
7. Later, get the same figures repeated on outside sites (W-02).

**Posts affected**
- Priority (Quotr's own figures): [[BP-82 outsource construction estimating]], [[BP-85 commercial estimating services]], [[BP-12 is ai takeoff actually accurate yet]].
- Used for general facts, where no name is expected: [[BP-87 quantity takeoff services]] (S9), [[BP-56 how to estimate plumbing from drawings]] (N2), [[BP-81 best planswift alternatives 2026]] (V3).
- Retrieved only, not used: [[BP-51 stack alternative]], [[BP-62 ddp construction materials]].

![[Articles.base#Cited by AI]]

**Related tasks:** [[A8 Put the Quotr name inside key facts on the pages AI already reads|A8]] · [[A1 Agree and sign off one fact sheet|A1]] · [[A3 Fact-fix sweep, part 2 - every other conflicting fact|A3]] · [[D3 AI takeoff accuracy benchmark + How we test page (R-41)|D3]]

---

## W-05 Little original data, and headline numbers have no method

**Impact:** high · **Effort:** L · **Confidence:** high

**What happened**
- The programme wrote about the market but published little that only Quotr could publish.
- The 6 cost and market posts and the "State of AI in Preconstruction" post summarise other people's numbers.
- Quotr does have proof it could use: the ROI calculator, the free FireTips rebuild app (on the old domain), the RL Electric story and video, 9 Service sample deliverables and dated procurement results on /procurement/ (for example Saratoga). The blog barely draws on them.
- There are 2 customer-story posts (RL Electric and Vanderbilt) against 6 event recaps. The RL Electric case study gives no numbers.
- Quotr's headline figures come with no method: $1.2B+ estimated, 300+ projects a month, 95-99% accuracy and "under 12 minutes".
- Fair context: original datasets need enough jobs and customer consent, which a startup about two years old may only now have. The raw material seems to exist now: procurement prices against Bay Area market prices, and Service job data.

**Evidence**
- Quotr has published 0 original datasets.
- Only 1 of the 6 cost and market posts had its prompt tested: [[BP-23 tariff impact construction costs 2026 steel aluminum copper|BP-23]] (S11, tracked as T46). It was not used. AI cited only government, media and trade bodies (JEC, Brookings, NAHB, Construction Dive) and no software vendor. The other 5 were not tested ([[GEO tactics already used]] tactic 31).
- [[BP-27 state of ai in preconstruction 2026 adoption roi enr top 400 gcs|BP-27]] is built from Deloitte, ENR, Construction Dive, DPR, Chubb and Skanska, with no Quotr data point. [[BP-35 construction cost index q1 2026 ppi rsmeans mortenson|BP-35]] is a roundup of third-party indexes.
- Where Quotr holds unique data, it was absent. For S12 (LA fire rebuild cost), Bloomberg and local builders were cited, although Quotr sells a "Fast Cost Estimation (Residential LA Fire Rebuilding)" sample. For P3 and L-130 (multifamily cost per sq ft), the benchmarks came from others.
- Tools: the ROI calculator is the only one. For "how to estimate drywall for a house" (T27, Absent), AI cited free calculators from EasyTakeoffs and Procore.
- Proof: the RL Electric case study lists its outcomes only as "AI-assisted", "Reduced" and "Dozens". Its one figure sits in a homepage testimonial signed with a first name only ([[Website audit]] §7, §9.1).
- [[BP-96 quotr service estimates|BP-96]] appears on the blog index as "Quotr.ai Service Has Delivered Estimates for $1.2B+..." (matched by date; not opened). We found no method for that figure anywhere on the site.
- One /software/ sentence says "up to 80%" time saved and also "from around 20 hours to just 1-2", which is a 90-95% cut. [[Website audit]] §10: "Proprietary figures exist only as unsupported claims". [[Q-17 Volume claims|Q-17]], [[Q-18 Accuracy|Q-18]] and [[Q-19 Time saved|Q-19]] are open.
- Engines discount these claims but reward specific numbers. In B3, Perplexity called the 95-99% claim "self-published". Yet [[BP-12 is ai takeoff actually accurate yet|BP-12]], the most number-specific explainer, was Perplexity's first citation for P5, even though it was not in the web-search top 9.
- Competitors publish proof others can cite. Togal publishes a University of Kansas comparison with On-Screen Takeoff, which it labels peer-reviewed. STACK has an interactive precon benchmark and Handoff a cost-data hub.
- QUALITY-06 and AI-08: Google's 2026-05-15 guide names "valuable, unique, non-commodity content" as the main factor for its AI features. FRESH-14 (low confidence): dates and numbers best predict ChatGPT citations.

**Why it matters**
- Without its own numbers, Quotr competes as one more summary of common facts, and engines prefer the original sources.
- Numbers without a method get treated as marketing: engines hedge, or use the figure and drop the name (W-04).
- Inference: in side-by-side answers, a rival with outside validation (Togal) looks more credible.
- Data and tools are also what earn links and press (W-02).

**What to do**
1. Short term (hours): tie each number to Quotr and its conditions, for example "In Quotr.ai's internal testing on [N] plan sets, [month year], ..." ([[A8 Put the Quotr name inside key facts on the pages AI already reads|A8]]).
2. Remove "under 12 minutes" unless it has been measured. Use one time-saved figure ([[A3 Fact-fix sweep, part 2 - every other conflicting fact|A3]]). Get Q-17, Q-18 and Q-19 answered.
3. Move about a third of new production to assets only Quotr can make (a judgement call). Each gets a method note, a date, a sample size and the brand in its key sentences:
   - a factory-direct versus US dealer price index ([[B5 Prepare the first original dataset|B5]], [[C1 Publish the first original dataset|C1]], [[D4 Second price-index edition, Q1 2027 (R-51)|D4]]);
   - cost per sq ft by trade from Service jobs ([[D2 Residential and multifamily cost per sq ft by trade (R-40)|D2]]);
   - an accuracy benchmark with a "How we test" page ([[D3 AI takeoff accuracy benchmark + How we test page (R-41)|D3]]);
   - a "Service by the numbers" page that explains how $1.2B+ is counted ([[D7 More numbers-first case studies; Service by the numbers; security page|D7]]);
   - a landed-cost calculator and a drywall calculator ([[B9 Spec and start building the first two free tools|B9]], [[C3 Ship the first free tools|C3]]);
   - the LA fire-rebuild guide, built from an anonymised estimate ([[C4 LA fire-rebuild cost guide|C4]]);
   - two numbers-first case studies, RL Electric and Saratoga ([[B4 Proof pages - case studies with numbers|B4]]).
4. Pitch each dataset to trade press ([[C2 Press pitches built on the dataset|C2]]).
5. Add at least one Quotr data point and a method line to each cost, tariff and "state of" post. Stop calling roundups "reports".
6. Keep event recaps short. Pause new generic explainers until these assets exist.

**Posts affected**
- Cost and market posts (6): [[BP-03 construction cost trends 2026]], [[BP-23 tariff impact construction costs 2026 steel aluminum copper]], [[BP-31 tariff aware estimating material escalation every bid]], [[BP-35 construction cost index q1 2026 ppi rsmeans mortenson]], [[BP-41 data center construction estimating mep subcontractor choke point]], [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps]]. Plus [[BP-27 state of ai in preconstruction 2026 adoption roi enr top 400 gcs]].
- Headline numbers with no method: [[BP-43 best togal ai alternatives 2026]] (95-99%, "internal benchmarking"), [[BP-18 ai that reads construction drawings chat with blueprints]] (80-88% on scans), [[BP-12 is ai takeoff actually accurate yet]] (accuracy figures, per Perplexity), [[BP-96 quotr service estimates]] ($1.2B+, in the title). Also /software/ and the homepage. Where "under 12 minutes" comes from is unclear.
- The opposite problem, no numbers at all: [[BP-72 how rl electric cut estimating time with ai powered takeoffs]].

**Related tasks:** [[A8 Put the Quotr name inside key facts on the pages AI already reads|A8]] · [[A3 Fact-fix sweep, part 2 - every other conflicting fact|A3]] · [[B4 Proof pages - case studies with numbers|B4]] · [[B5 Prepare the first original dataset|B5]] · [[B9 Spec and start building the first two free tools|B9]] · [[C1 Publish the first original dataset|C1]] · [[C2 Press pitches built on the dataset|C2]] · [[C3 Ship the first free tools|C3]] · [[C4 LA fire-rebuild cost guide|C4]] · [[D2 Residential and multifamily cost per sq ft by trade (R-40)|D2]] · [[D3 AI takeoff accuracy benchmark + How we test page (R-41)|D3]] · [[D4 Second price-index edition, Q1 2027 (R-51)|D4]] · [[D7 More numbers-first case studies; Service by the numbers; security page|D7]]

---

## W-06 The Service pivot was built as a dozen similar pages

**Impact:** high · **Effort:** M · **Confidence:** medium

**What happened**
- From August the mix swung to the outsourced Estimation Service: 11 of the 18 posts in August and September.
- The pivot looks sound. After the alternatives lists, this is the cluster AI uses most. 3 of the 12 Service posts were used as sources, a strong rate for posts only weeks old.
- But it was built as many similar pages: general, commercial, preconstruction, precon-on-demand, California, electrical, HVAC and MEP.
- Trade and service-type pages are normal practice, and some may earn their place. Still, researchers flagged 11 overlapping pairs among the 12 Service posts.
- The HVAC and MEP posts went out on the same day and cover much the same ground.
- The pages state turnaround and Service pricing in different ways (W-03). [[Q-15 Turnaround|Q-15]] is still open, so we could not confirm one standard.
- In the one prompt where these pages were cited (C12), the engine quoted Quotr's rates but credited them to "one outsourced estimating service" (W-04).
- This item overlaps with W-03, W-04 and W-11. Count the problem once.

**Evidence**
- Bottom-of-funnel or brand posts (for buyers close to a decision): 5 of 70 in April-July, against 12 of 18 in August-September. Service posts were 7 of 11 in August and 4 of 7 in September (blog statistics §5-6).
- [[BP-82 outsource construction estimating|BP-82]] was the first citation in C12 on the original run and on the fact-check re-run. [[BP-85 commercial estimating services|BP-85]] (C12) and [[BP-87 quantity takeoff services|BP-87]] (S9) were also cited. Only 2 Service posts had a tested prompt. Tracked T12 is "Cited, not named" and T44 is "Cited".
- [[BP-94 hvac estimating services|BP-94]] and [[BP-95 mep estimating services|BP-95]] went out on 2026-09-18, and each flags the other. Prompts E-075 and E-079 are each served by 2 Service posts.
- Site-wide there are 7 turnaround claims, including "72 hours" in a URL. /service/ says "project-based" while /pricing/ gives $0.25 or $0.10 per sq ft ([[Website audit]] §11). [[Q-27 Lead product for top of funnel|Q-27]] is also open.
- Tracked T32 "how long does a construction estimate take" has no Quotr page and is Absent.
- INDEX-06, QUALITY-05 and AI-07: making separate pages for every variation of a question, mainly to manipulate AI answers, can count as scaled content abuse (a Google spam rule). Whether Google sees these pages that way is unknown; there is no Search Console data.

**Why it matters**
- The best-performing Service pages give AI a price but no brand and no single turnaround.
- So citations do not turn into named recommendations for the product Quotr is now pushing.
- Inference: the variant pages may split links between them.
- Near-identical variants are the pattern Google's scaled-content policy describes. Twelve pages is not mass production, and there is no sign of a penalty. But merging the clear duplicates removes the risk.

**What to do**
1. First settle the turnaround and the Service pricing wording in the fact sheet (Q-15; [[A1 Agree and sign off one fact sheet|A1]]).
2. Build one Service hub plus 3-4 clearly different pages:
   - outsourced estimating, which absorbs [[BP-79 construction estimating services|BP-79]];
   - GC preconstruction, which absorbs [[BP-89 precon on demand outsource bid cost estimation|BP-89]];
   - quantity-takeoff pricing;
   - MEP, which absorbs HVAC unless Search Console shows separate demand.
3. Redirect the rest with 301s after the September spam update ends, around 2026-10-08 (RANK-21; [[A12 Merge duplicate pages|A12]]).
4. Write the key facts with the brand attached, for example "Quotr.ai's Estimation Service charges $0.25/sq ft under 50k sq ft and $0.10 above" ([[A8 Put the Quotr name inside key facts on the pages AI already reads|A8]]).
5. Hold off on more city pages until the hub exists.
6. Add a "Service by the numbers" page with its method ([[D7 More numbers-first case studies; Service by the numbers; security page|D7]]).

**Posts affected**
- August-September Service posts (11): [[BP-79 construction estimating services]], [[BP-82 outsource construction estimating]], [[BP-84 construction estimating services california]], [[BP-85 commercial estimating services]], [[BP-86 preconstruction services]], [[BP-87 quantity takeoff services]], [[BP-89 precon on demand outsource bid cost estimation]], [[BP-91 electrical estimating services]], [[BP-94 hvac estimating services]], [[BP-95 mep estimating services]], [[BP-96 quotr service estimates]].
- Also [[BP-90 outsourcing vs hiring an estimator]], and [[BP-25 quotr developer desk underwriting grade estimates 72 hours]] (May), which needs a turnaround fix.

**Related tasks:** [[A1 Agree and sign off one fact sheet|A1]] · [[A3 Fact-fix sweep, part 2 - every other conflicting fact|A3]] · [[A8 Put the Quotr name inside key facts on the pages AI already reads|A8]] · [[A12 Merge duplicate pages|A12]] · [[D7 More numbers-first case studies; Service by the numbers; security page|D7]]

---

## W-07 Best-of lists were not used for tested unbranded prompts

**Impact:** high · **Effort:** M · **Confidence:** medium

**What happened**
- Quotr built 22 list posts: 17 best-of lists and buyer's guides, plus 5 "alternatives to X" posts.
- 13 went live in June, more than half of that month's 25 posts. 9 of those came in the last 13 days of June.
- Quotr ranks itself first in the lists we could check: by a direct read on [[BP-43 best togal ai alternatives 2026|BP-43]], and through search summaries on [[BP-32 best togal ai alternatives|BP-32]] and [[BP-81 best planswift alternatives 2026|BP-81]]. The order in the other lists was not recorded.
- The best-of lists underperformed. Of the 7 whose prompt was tested, none was retrieved, cited or named.
- 5 of the 17 appear in brand answers (V2, B2, B3, B4, B7), where they spread the retired price. The other 12 were not seen in any test.
- The alternatives posts did much better. They were Quotr's most-used format in unbranded answers, and [[BP-32 best togal ai alternatives|BP-32]] produced Quotr's only unbranded naming (V1).
- Context: from February 2026, practitioners reported Google losses for self-ranked "best X" lists. All 22 of these posts went live after that report.
- Fair context: analysts dispute a targeted penalty, Google has not confirmed one, and competitors publish self-ranked lists too. Handoff's list led two answers, but Handoff also has press and review listings.
- Only Perplexity was tested. Without Search Console data, a Google loss is a risk to manage, not a measured fact.
- Publishing lists quickly to cover "best X software" prompts was a reasonable bet. The lesson: the format needs outside support to get Quotr recommended.

**Evidence**
- By month: May 2, June 13, July 4, August 3. 10 of the 22 have "2026" in the URL. The June run went from [[BP-33 hvac estimating software 2026 buyers guide|BP-33]] (June 2) to [[BP-55 best drywall estimating software in 2026|BP-55]] and [[BP-54 best concrete estimating software 2026|BP-54]] (both June 30).
- 7 of the 17 best-of posts map to a prompt that was tested unbranded (C1, C4, C5, C6, C7, C11, N3, S5). A Quotr page was retrieved in 0, cited in 0 and named in 0. Posts in other groups whose prompt was tested were used in 9 of 18 (p=0.027; small sample, one engine). Their 8 tracked prompts (T01, T04, T05, T06, T07, T11, T42, T50) were all Absent.
- Caveat: these are category prompts, where Quotr is absent whatever the page type (0 of 15). The format may not be the cause.
- It is not an age or findability problem. [[BP-24 best ai construction estimating software 2026|BP-24]] came back 4th of 9 in web search for C1, but Perplexity did not retrieve it. All 9 checked best-of posts were found in web search. The group's median age is 93 days, about the same as the alternatives posts (92).
- What won instead: C1 cited ConstructConnect, ContraVault, Construction Placements, Construction Coverage, TDPM and SourceForge. C4-C6 cited rivals' trade pages and list farms (gitnux, worldmetrics, zipdo).
- In B7 ("Quotr alternatives"), about 10 of the 18 citations were Quotr's own posts.
- About 13 of the 22 carry the retired price (up to 15 if the unconfirmed ones hold; see W-01).
- Handoff's own list was the first citation for S1 and was cited in C11.
- Timing claims. RANK-07 and QUALITY-10: self-ranked "best X" lists lost roughly 30-50% of Google visibility from about 2026-01-20 (Lily Ray, 3 February 2026). QUALITY-11: scaled "alternatives" pages and posts "lightly refreshed with 2026" were among the hardest hit. RANK-13 and RANK-15: the May 21-June 2 core update, during which the losses reportedly continued. RANK-22: no core update since 2026-06-02, so 18 of these lists have never been through one.
- RANK-16, QUALITY-13 and AI-19: when a company's own list was cited in an AI Overview, the company was left out of the recommendation 69% of the time. AI-17: "best of" searches show an AI Overview 81.3% of the time.
- Counter-evidence. RANK-08: analysts dispute a listicle-specific penalty. QUALITY-12 and FRESH-09: Google has not confirmed a targeted update. FRESH-11 (low confidence): "best X" lists are 43.8% of the page types ChatGPT cites.

**Why it matters**
- The 17 best-of lists, 18% of output, earned no unbranded use in the tests.
- Their main AI role today is carrying the retired price into brand answers.
- It is a format engines use as a source of facts but rarely as a reason to recommend its author (RANK-16).
- Inference: if Google demotes this pattern, as observers report for other B2B sites, the pages would also drop out of AI Overviews and AI Mode (QUALITY-07).

**What to do**
1. Now: remove the retired prices (W-01) and ask for a re-crawl.
2. Stop publishing new self-ranked lists.
3. Save a per-page baseline from Search Console and its Generative AI report (data from 2026-05-18; GSC-13, GSC-14, AI-10). Add a Search Console note for every change (GSC-06). See [[Search Console audit playbook]].
4. After the September spam update ends (around 2026-10-08, RANK-21), cut the 17 best-of posts to about 6-8. Keep the ones that rank or map to tracked prompts.
5. Merge the rest with 301 redirects ([[A12 Merge duplicate pages|A12]]): [[BP-47 ai bidding software construction|BP-47]] into [[BP-80 best ai bid software for construction|BP-80]]; the two electrical guides ([[BP-46 best electrical estimating software 2026|BP-46]], [[BP-37 electrical estimating software buyers guide|BP-37]]); the buyer's guide [[BP-19 ai construction estimating software buyers guide|BP-19]] with [[BP-24 best ai construction estimating software 2026|BP-24]]; and [[BP-49 construction proforma software|BP-49]] into the pro forma comparison [[BP-22 real estate pro forma software comparison|BP-22]].
6. Rewrite the pages you keep as "best for [situation]" guides. Each needs a line saying Quotr publishes it, the criteria used, no automatic #1, linked and dated competitor facts, a "where rivals are stronger" section and a named reviewer.
7. Move trade depth to the product trade pages, where Quotr is the subject.
8. Keep "2026" in a title only if every entry was re-checked this year.
9. Put the saved effort into the third-party lists these prompts cite ([[B2 Outreach to the best of lists AI cites (Tier A)|B2]], [[C5 Tier B and procurement-category list outreach|C5]]).
10. Note: no task yet covers rewriting all 17 so that Quotr stops ranking itself first. Today it exists only as row-level advice in [[Optimize vs create]].

**Posts affected**
- Best-of lists and buyer's guides (17): [[BP-19 ai construction estimating software buyers guide]], [[BP-24 best ai construction estimating software 2026]], [[BP-33 hvac estimating software 2026 buyers guide]], [[BP-37 electrical estimating software buyers guide]], [[BP-46 best electrical estimating software 2026]], [[BP-47 ai bidding software construction]], [[BP-48 best flooring estimating software in 2026]], [[BP-49 construction proforma software]], [[BP-50 construction procurement software]], [[BP-52 best plumbing estimating software 2026]], [[BP-54 best concrete estimating software 2026]], [[BP-55 best drywall estimating software in 2026]], [[BP-64 trade estimating software]], [[BP-76 best glazing estimating software 2026]], [[BP-77 structural steel estimating]], [[BP-80 best ai bid software for construction]], [[BP-83 rebar estimating and takeoff software]].
- The 5 alternatives posts are covered in W-14.

**Related tasks:** [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]] · [[A12 Merge duplicate pages|A12]] · [[B2 Outreach to the best of lists AI cites (Tier A)|B2]] · [[C5 Tier B and procurement-category list outreach|C5]] · [[D6 Honest comparisons - four-way table, Buildxact, Quotr.ai alternatives|D6]]. Google timing detail: [[Google search updates 2025-2026]].

---

## W-08 Little content for residential and multifamily buyers

**Impact:** high · **Effort:** L · **Confidence:** medium

**What happened**
- Quotr's llms.txt and /faq/ say it serves residential and multifamily builders. Its procurement proof is Bay Area homes.
- The blog leans commercial. 5 URLs say "commercial". None says residential, home, multifamily, ADU or remodel.
- The residential exceptions we found are [[BP-58 house flipping math 2026|BP-58]], two developer posts and an IBS (home builders' show) recap. The FireTips rebuild app sits off the blog, on the old domain.
- The drywall how-to is framed on a commercial floor plan. The vault notes that the HVAC and electrical how-tos have no residential section.
- The tracked residential and developer questions are where Quotr has no page and is absent.
- Fair context: the consultant built the tracked set from Quotr's stated audience in September 2026, after most posts were written. So this is a gap to fill, not a past mistake.
- If Quotr's real buyer is commercial, the content is right and the positioning claim is the problem. Either way, engines get a mixed signal.

**Evidence**
- 0 of 96 URLs contain residential, home, multifamily, ADU or remodel (real titles were seen for only 14 posts). 5 contain "commercial": [[BP-85 commercial estimating services|BP-85]], [[BP-36 how to estimate drywall framing commercial floor plan|BP-36]], [[BP-30 commercial electrical takeoff drawings to proposal|BP-30]], [[BP-40 commercial signage takeoff sign schedule bid package|BP-40]], [[BP-28 how to bid commercial construction projects subcontractor estimating takeoff guide|BP-28]].
- Persona tags across the posts: subcontractor 73, estimator 63, general contractor 61, developer 24, house flipper 1. Trade tags: multi-trade 60, roofing 1, framing or lumber 0.
- 17 of the 45 unbranded tracked prompts are marked "new page needed", and all 17 are Absent. 14 of those are residential or developer prompts, and 13 are High priority. Examples: T02, T13, T28, T45, T47, T52, T53 ([[Tracking set]]).
- Of the 17 residential tracked prompts, 15 are Absent, 1 is retrieved only (T25) and 1 names Quotr (T43). AI names Clear Estimates, Buildxact, Houzz Pro, Buildertrend, JobTread and Handoff instead ([[Audiences and personas]]).
- 13 of 23 trade landing pages have no supporting content. Roofing has only a service sample ([[Website audit]] §8.3).
- The audience statements conflict: "single-family homes and multi-family housing" (llms.txt, /faq/) against "commercial general contractors ... development funds" (/disambiguation/). [[Q-26 Primary audience|Q-26]] is open.

**Why it matters**
- Residential and multifamily buyers find no Quotr answer, so AI recommends Handoff or Buildxact.
- Engines read audience claims that contradict each other, which weakens any category recommendation.
- Content effort went into general and commercial topics where incumbents already dominate.

**What to do**
1. Get [[Q-26 Primary audience|Q-26]] answered before writing more.
2. If residential and multifamily are real markets, build:
   - the residential hub ([[B10 Residential hub; decide on the thin trade pages|B10]]);
   - the multifamily and developer hub ([[C6 Developer hub, deep electrical page, integrations page, one honest comparison|C6]], [[D5 Persona hubs and deep trade pages|D5]]);
   - residential drywall, lumber-package and roofing guides;
   - the LA rebuild cost guide from a real Quotr estimate ([[C4 LA fire-rebuild cost guide|C4]]);
   - residential cost per sq ft by trade ([[D2 Residential and multifamily cost per sq ft by trade (R-40)|D2]]);
   - residential sections in the existing trade how-tos.
3. If they are not real markets, remove the residential claims from llms.txt, /faq/ and /disambiguation/, and drop those prompts from tracking.
4. Either way, choose the target prompts before briefing a page.

**Posts affected**
- Could carry residential sections: [[BP-36 how to estimate drywall framing commercial floor plan]], [[BP-42 how to estimate hvac sheet metal mechanical plan]], [[BP-21 how to estimate electrical work from drawings conduit devices labor]], [[BP-59 how developers source building materials]].
- 17 tracked prompts have no adequate page.

**Related tasks:** [[A1 Agree and sign off one fact sheet|A1]] · [[B10 Residential hub; decide on the thin trade pages|B10]] · [[C4 LA fire-rebuild cost guide|C4]] · [[C6 Developer hub, deep electrical page, integrations page, one honest comparison|C6]] · [[D2 Residential and multifamily cost per sq ft by trade (R-40)|D2]] · [[D5 Persona hubs and deep trade pages|D5]]

---

## W-09 Procurement is described mainly in Quotr's own terms

**Impact:** high · **Effort:** M · **Confidence:** medium (4 procurement posts had a tested prompt, on one engine)

**What happened**
- 10 procurement posts (7 of them in July 2026) build Quotr's own category language: "takeoff-to-buyout", "the takeoff-to-transaction gap" and "factory-direct with AI takeoff and procurement". They also lean on DDP (delivered duty paid: the seller covers shipping and import duties to the site), a standard trade term.
- Coining terms is a normal way to build a new category, and no rival owns this ground yet.
- Inference: buyers phrase the need differently. The lack of outside proof (W-02) may matter as much as wording.
- In the tests, buyer-worded prompts left Quotr absent, or retrieved but not used (C10).
- Quotr was named only in S6, which echoes Quotr's own wording. There the engine described it as a sourcing service, not as AI takeoff software that also sources materials.
- Two Quotr pages target the core "estimating software with material procurement" prompt (E-006, tested as C9), and a third targets a close variant (E-066). None was among the 19 citations for C9 on either run.

**Evidence**
- C9 "construction estimating software with material procurement" (tracked as T09): Buildertrend, Procore, Buildxact, esti-mate and ConWize were named. The answer had 19 citations, none from quotr.ai. The fact-check re-run gave the same result.
- S6 echoes Quotr's wording. Quotr was named 1st, then 3rd of 6 on the re-run. The engine filed it under "China factory-direct, project sourcing" and said it emphasises "sourcing and procurement more than AI takeoff".
- Buyer wording: for C10, [[BP-62 ddp construction materials|BP-62]] was retrieved but not used, and Alibaba and 7 others were named. For C14, Quotr was absent and 8 factory-direct retailers were named. For P4 "how to reduce building material costs", no brand was named, although [[BP-61 reduce construction material costs|BP-61]] targets it. For L-109 "how to import building materials from China", Quotr was absent.
- O5: "the search results do not show a single platform explicitly marketed as a factory-direct marketplace" ([[Off-site presence]]). The ground is open.
- Of the 4 procurement posts with a tested prompt, two were touched (C10 retrieved only; S6 with Quotr's own wording). None was named for a buyer-worded prompt.
- Quotr's pages disagree on the network (220+, 50+ or 30+ factories) and on savings (40-50% or 40-55%). Engines hedge: "depending on the page".

**Why it matters**
- This is the category where rivals are absent and Quotr's story is unique.
- Yet the content does not yet connect Quotr to the words buyers use.
- Being called a sourcing service is not wrong, since Quotr does source from China. But the software half, the main revenue line, drops out of the description.

**What to do**
1. Rewrite the lead pages around the buyer phrasings in the tracking set: C9/E-006, C10/E-081, C14/E-082, L-108 and L-109.
2. Open each with one plain sentence that covers both halves: "Quotr.ai is AI takeoff and estimating software that can also buy the materials factory-direct and deliver them DDP."
3. After the spam update ends, merge [[BP-02 the takeoff to transaction gap|BP-02]] into [[BP-38 takeoff to buyout construction estimating procurement platform|BP-38]] (the R-13 rebuild). Keep [[BP-50 construction procurement software|BP-50]] as a neutral category guide for E-013.
4. Use one approved factory count and one savings figure ([[A1 Agree and sign off one fact sheet|A1]]).
5. Add dated project numbers from /procurement/ with the Quotr name attached. Example: Saratoga, $97,000 against a $187K-$218K market price.
6. Build the DDP landed-cost calculator and the procurement guides ([[B8 Procurement and tariff decision guides|B8]], [[B9 Spec and start building the first two free tools|B9]], [[C3 Ship the first free tools|C3]], [[D1 Tariff data story and import guides (R-29 to R-32)|D1]]).
7. Pitch the procurement roundups ([[C5 Tier B and procurement-category list outreach|C5]]).

**Posts affected**
- Procurement posts (10): [[BP-02 the takeoff to transaction gap]], [[BP-38 takeoff to buyout construction estimating procurement platform]], [[BP-59 how developers source building materials]], [[BP-60 what is construction procurement 2026 guide]], [[BP-61 reduce construction material costs]], [[BP-62 ddp construction materials]], [[BP-63 ai agents for construction procurement and buyout]], [[BP-68 hospitality procurement consolidated sourcing]], [[BP-69 construction procurement process]], [[BP-88 sourcing building materials china cbd fair 2026]].
- Plus [[BP-50 construction procurement software]].

**Related tasks:** [[A1 Agree and sign off one fact sheet|A1]] · [[B8 Procurement and tariff decision guides|B8]] · [[B9 Spec and start building the first two free tools|B9]] · [[C3 Ship the first free tools|C3]] · [[C5 Tier B and procurement-category list outreach|C5]] · [[D1 Tariff data story and import guides (R-29 to R-32)|D1]]

---

## W-10 Some posts did not come back in web search

**Impact:** high · **Effort:** M · **Confidence:** low to medium

**What happened**
- In targeted searches (site: searches, exact-URL searches and exact-title searches), 15 of 36 posts never came back.
- All 15 misses came from 23 live checks on 2026-09-26, mostly on posts not already seen the day before. The sample was not random: list posts were checked on 2026-09-25 and how-tos on 2026-09-26. So "15 of 36" is not a rate for the whole blog.
- Most of the missed posts were 2 to 5 months old, so newness does not explain it.
- The search tool is not Google. This is a warning sign, not proof that the posts are missing from Google's index (the list of pages Google can show). Perplexity did retrieve 2 of the 15.
- We had no Search Console or Bing data ([[Q-40 Access and history|Q-40]]), so we cannot tell whether Quotr already checks indexing.
- Cloudflare's AI Labyrinth bot trap is on. It targets bots that ignore crawl rules, not verified search crawlers. Whether Cloudflare's "Block AI bots" setting is off is unconfirmed ([[Q-34 Cloudflare|Q-34]]).
- Before this review, no vault page or task planned a Page indexing audit of the 96 posts.

**Evidence**
- 36 posts checked: 21 found, 15 not found. The 15: 8 trade how-tos, 4 head-to-head comparisons, 2 AI explainers and 1 alternatives list (blog statistics §11).
- Ages of the 15 when checked (days): 16, 25, 64, 86, 89, 101, 102, 108, 123, 138, 142, 142, 156, 158, 163. Median 108 for posts not found, 99 for posts found.
- For 11 of the 15, another Quotr page came back instead (see W-11). Most of these were site: searches, which return other Quotr pages by design, so this is a hint, not proof.
- 14 of the 15 map to at least one prompt in the prompt library, so they target buyer questions Quotr wants to win.
- List and comparison posts were found 17 of 22 times, other formats 4 of 14 (p=0.0061). Selection bias: the 2026-09-25 fact-check looked mainly at list posts.
- Perplexity retrieved [[BP-57 bluebeam alternative|BP-57]] and [[BP-39 quotr ai vs beam ai takeoff estimating comparison|BP-39]] for brand prompts on 2026-09-25, so those two are in some index. 60 posts were never checked (search limit).
- The AI Labyrinth hidden link is on every checked page. OTHER-07: since July 2025, Cloudflare blocks AI crawlers by default on new domains.

**Why it matters**
- If some of these posts are not indexed, or Google folds them into a sister post, they cannot be a source link in AI Overviews or AI Mode (INDEX-05, AI-05).
- Bing feeds Copilot. ChatGPT's search providers are not public (OTHER-14).
- The missed posts are mostly how-tos and explainers, which should answer buyers' early questions.
- Without Search Console, Bing and Cloudflare data, the cause is unknown: a crawl block, Google choosing another page as the main version, or low demand.
- Perplexity cites quotr.ai, so its crawler gets in. Access for ChatGPT, Claude and Copilot crawlers is unverified.

**What to do**
1. Get Search Console and Bing Webmaster Tools access (Q-40; [[A15 Measurement setup and multi-engine baseline|A15]]).
2. Export the Page indexing report. Run URL Inspection on the 15 posts first, then all 96, and record each post's status. How-to: [[Search Console audit playbook]].
3. Act on the reason Google gives. "Duplicate, Google chose different canonical" (Google picked a different page as the main version): merge the post into that page with a 301 ([[A12 Merge duplicate pages|A12]]). "Crawled / Discovered - currently not indexed": add plain HTML links to it from the hubs and 2-3 related posts (W-15), then request indexing.
4. In Cloudflare's AI Crawl Control, confirm that Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, Claude-SearchBot and PerplexityBot get normal (200) responses on /blog/ pages ([[A11 Confirm Cloudflare lets AI search bots in|A11]]).
5. Confirm the Search Console "Search generative AI" opt-out is off (GSC-15).
6. Add "posts indexed out of 96" as a monthly KPI.
7. Steps 1, 2, 4 and 5 only read data and can start now. Hold merges until the September spam update ends, around 2026-10-08 (RANK-21).

**Posts affected**
- Not found in web search (15): [[BP-04 how to price construction job]], [[BP-05 construction takeoff guide]], [[BP-06 quotr vs traditional estimating]], [[BP-10 construction estimating mistakes to avoid]], [[BP-11 how ai construction estimating works]], [[BP-13 blueprint to priced estimate workflow]], [[BP-26 quotr vs excel]], [[BP-39 quotr ai vs beam ai takeoff estimating comparison]], [[BP-44 flooring trades how to quote flooring jobs and win more work]], [[BP-45 what is ai construction estimating software]], [[BP-53 how subcontractors bid gcs without giving away margin]], [[BP-57 bluebeam alternative]], [[BP-74 metric imperial construction takeoff]], [[BP-90 outsourcing vs hiring an estimator]], [[BP-92 scope gap construction]].
- 60 of the 96 posts have never been checked.

**Related tasks:** [[A15 Measurement setup and multi-engine baseline|A15]] · [[A11 Confirm Cloudflare lets AI search bots in|A11]] · [[A12 Merge duplicate pages|A12]]

---

## W-11 About 12 posts duplicate another Quotr page

**Impact:** medium · **Effort:** M · **Confidence:** medium

**What happened**
- Some posts answer the same question as an existing Quotr page.
- The clearest cases: two Togal alternatives lists, two AI bidding lists, two electrical buyer guides, three procurement pages for one need, and near-identical HVAC and MEP Service pages.
- The vault marks about 12 posts for merging ([[Optimize vs create]]).
- Researchers also flagged topic overlap in 49 post pairs covering 64 of 96 posts. Much of that is normal for topic clusters and does not prove the pages compete.
- In search checks, a sister Quotr page often came back instead of the post searched for (11 of the 15 misses in W-10). That fits pages competing, but may also reflect how the search tool works.
- Inference: posts were briefed without checking for an existing page.
- Fair context: publishing fast to cover many prompts makes some duplication likely. The fix is a merge pass plus a "one prompt, one main page" rule.
- The Togal, Service and procurement cases also appear in W-06, W-07, W-09 and W-14.

**Evidence**
- 49 overlap pairs covering 64 of 96 posts; 42 of 98 overlap checks are unconfirmed, so treat this as an upper bound. Overlaps appear in 9 of 10 clusters.
- 10 prompt library questions each have 2 or more Quotr posts.
- Togal: [[BP-43 best togal ai alternatives 2026|BP-43]] ("Top 10", 2026-06-16), [[BP-32 best togal ai alternatives|BP-32]] ("by Trade", 2026-06-02) and [[BP-15 quotr vs togal ai comparison 2026|BP-15]] come back together at results 5-7 in web search, below four review directories (FRESH-16). Perplexity retrieved both lists. So far the pair shows no harm.
- Search answers merge Quotr's two PlanSwift pages.
- Service: 11 overlap pairs among the 12 Service posts. HVAC and MEP went out on the same day and flag each other.
- Procurement: two pages target E-006 and a third targets the close variant E-066. None was among the 19 citations for C9 on either run.
- Other pairs flagged for merging: [[BP-11 how ai construction estimating works|BP-11]] / [[BP-45 what is ai construction estimating software|BP-45]]; [[BP-69 construction procurement process|BP-69]] / [[BP-60 what is construction procurement 2026 guide|BP-60]]; [[BP-47 ai bidding software construction|BP-47]] / [[BP-80 best ai bid software for construction|BP-80]]; the two electrical buyer guides; [[BP-49 construction proforma software|BP-49]] / [[BP-22 real estate pro forma software comparison|BP-22]].
- INDEX-06, QUALITY-05 and AI-07: a separate page for every question variation, mainly to manipulate AI answers, can count as scaled content abuse. An Ahrefs study of 75,000 brands found page count barely correlates with AI visibility (about 0.194) ([[Content priorities]]).

**Why it matters**
- Inference: near-duplicates can split links and citation signals, so the one slot Quotr could win may go to neither page.
- Each duplicate is one more page to fix when a fact changes.
- A pile of variant pages carries scaled-content risk while Google runs spam updates.
- Inference: Google may fold a post into its sister, which could explain some misses in W-10.

**What to do**
1. Get Search Console access and pull the "Duplicate, Google chose different canonical" rows ([[A15 Measurement setup and multi-engine baseline|A15]]).
2. Merge the roughly 12 posts listed in [[Optimize vs create]] with 301 redirects. Start with the Togal pair, merged into the URL without a year ([[A12 Merge duplicate pages|A12]]).
3. Wait for the September spam update to finish (around 2026-10-08, RANK-21) before redirecting.
4. Before briefing any new post, check the prompt library and the post table for an existing URL to extend. The rule is one prompt, one main page.

**Posts affected**

![[Articles.base#Merge or retire]]

**Related tasks:** [[A12 Merge duplicate pages|A12]] · [[A15 Measurement setup and multi-engine baseline|A15]]

---

## W-12 Output grew faster than the editing check

**Impact:** medium · **Effort:** S · **Confidence:** high on volume; medium on how widespread the slips are

**What happened**
- Output went from 1 post in March and 6 in April to 22 in May and 25 in June. It then fell to 17, 11 and 7 a month.
- In the four weeks from mid-June to mid-July, all 55 dictionary terms also went live.
- Inference: the CEO's March podcast on GEO and unbranded search terms suggests volume was a deliberate strategy. Covering many buyer questions fast is a reasonable aim.
- The later slowdown is not a problem. It lands close to the 8-12 pieces a month the vault recommends.
- The problem is that the final check did not keep up. In 2 of the roughly 6 posts read in full, notes from the writing brief and ChatGPT tracking tags reached the live page. The other ~90 posts are unchecked.
- Fair context: logged issues per post are flat by month (about 5 per post), so the spike posts are not worse one by one. There were just more of them.

**Evidence**
- Real-dated posts by month (90 posts): December 2025 1, March 1, April 6, May 22, June 25, July 17, August 11, September 7. May and June together are 47 of 90 (52%).
- Average 5.4 posts a week from May 11 to July 13, against 2.33 from August 3 to September 28. Peak week 7 posts; 9 weeks with 5 or more (blog statistics §1-2).
- 16 days had 2 or more posts (35 posts, 39%), with 3-post days on 2026-05-07, 2026-06-02 and 2026-07-07. Only 6 of the 22 same-day pairs were in the same cluster. That points to a queue of finished drafts; same-day publishing is not the harm in itself.
- 2026-06-16 to 2026-07-15: 23 blog posts plus 55 dictionary terms, none updated since.
- Brief notes in [[BP-15 quotr vs togal ai comparison 2026|BP-15]], read directly: a table row "Best buyer prompt" followed by a target prompt; "Quotr.ai should win when the buyer is asking: ..." followed by a list of prompts; "should be emphasized across electrical, HVAC"; "AI Search systems trust balanced pages more than hype pages"; "Quotr.ai should not compete only on software price"; and "should be positioned around the full workflow". Its "Best For" table contradicts its own conclusion ([[GEO tactics already used]] tactics 44-45).
- [[BP-27 state of ai in preconstruction 2026 adoption roi enr top 400 gcs|BP-27]] says "That internal link structure matters for both readers and AI search.", and every outbound link carries "?utm_source=chatgpt.com" (a tracking tag that suggests it was drafted with ChatGPT).
- Typos: "win x2 work" on /software/ and "he true cost..." in a COO post teaser.
- [[BP-10 construction estimating mistakes to avoid|BP-10]]: search summaries (not tied to this exact URL) describe product jargon for beginners ("neural pattern recognition", "semantic cost mapping"). Check the page.
- QUALITY-01: "using generative AI tools to generate many pages without adding value" is scaled content abuse. QUALITY-15 (an Ahrefs study, correlation only): AI-written text does not hurt rankings in itself, so the risk here is the missing human edit. QUALITY-09: Google asks why and how content was made.

**Why it matters**
- "Quotr.ai should win when the buyer is asking..." reads as an internal note that the page targets AI prompts.
- Inference: a buyer, journalist or rival who screenshots it can present the page as a marketing script. It undercuts the page's own "Honest Limitations" section.
- The tracking tags and typos show the final check missed things. That invites doubt about the numbers, for a company that sells accuracy.
- Volume did not buy visibility: after 96 posts, Quotr is named in 1 of 32 unbranded prompts.

**What to do**
1. Run the phrase search in [[A6 Editorial sweep|A6]] on all 96 posts: "should win", "should be positioned", "should be emphasized", "buyer prompt", "AI search", "LLM", "GEO", "prompt" and "utm_source=chatgpt.com". Delete what it finds and fix the Best For table.
2. From now on, a named editor signs off every post against the pre-publish checklist ([[GEO writing style guide]] §7-8; [[A16 Add a human edit and fact-check step for AI-assisted drafts|A16]]). The checks: facts match the fact sheet, no brief or prompt text, every number sourced and dated, links work, and the piece is clearly different from existing pages.
3. Cap output at 8-12 pieces a month, new and rebuilt together. This pace is in [[Content priorities]] and the [[30-60-90 plan]] but in no task; add it to A16.
4. Report "pieces that passed the quality bar" each month, not post count.

**Posts affected**
- Confirmed brief or bot text (2): [[BP-15 quotr vs togal ai comparison 2026]], [[BP-27 state of ai in preconstruction 2026 adoption roi enr top 400 gcs]].
- To check (1): [[BP-10 construction estimating mistakes to avoid]].
- Most exposed: the 47 May-June posts and the 55 dictionary terms.

![[Articles.base#By month]]

**Related tasks:** [[A16 Add a human edit and fact-check step for AI-assisted drafts|A16]] · [[A6 Editorial sweep|A6]] · [[A12 Merge duplicate pages|A12]]. Timing patterns in detail: [[Publishing patterns and correlations]].

---

## W-13 Statistics and competitor facts went out without sources

**Impact:** medium · **Effort:** M · **Confidence:** high that sources are missing; a few specific errors confirmed

**What happened**
- Numbers went out with no link, date or method. Quotr's posts sometimes disagree about competitors.
- [[BP-92 scope gap construction|BP-92]] (CTO byline) uses "$177 billion a year", "8-14% of contract value" for change orders, "80% ... trace to missing or poor information" and "around 5%" rework, all without sources. The $177 billion figure probably comes from a study of wasted labour, not scope gaps (inference).
- [[BP-51 stack alternative|BP-51]] calls PlanSwift "a Trimble product". PlanSwift belongs to ConstructConnect, as Quotr's own PlanSwift comparison ([[BP-20 quotr ai vs planswift ai takeoff procurement comparison 2026|BP-20]]) says.
- The same post gives STACK's price as "$2,599-$2,999/year". That is incomplete and undated rather than plainly wrong.
- The same post calls Quotr "a cheaper entry point at $299.90/month", while its own STACK figure (about $217-$250 a month) is lower.
- [[BP-15 quotr vs togal ai comparison 2026|BP-15]] quotes Togal at "$299/month" with no link. That matches Togal's own pricing page (Growth $299 per user per month, billed yearly, seen 2026-09-25; [[Togal AI]]). A search summary of a Togal alternatives post says Togal "does not publish pricing", which would be wrong (not yet confirmed on the page).
- The URL of [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps|BP-70]] carries a 12.6% figure we could not trace.
- Fair context: unsourced vendor statistics are common across construction-tech blogs. Some Quotr posts cite well: [[BP-27 state of ai in preconstruction 2026 adoption roi enr top 400 gcs|BP-27]] names Deloitte, ENR and DPR in the text.

**Evidence**
- [[Website audit]] §7: four unsourced statistics in the scope-gap post. Search found no match for the 8-14% figure.
- STACK's own pricing page shows Takeoff & Estimate from $249 per user per month and a free version (seen 2026-09-25; [[STACK]]). $249 a month billed annually is $2,988 a year, inside the post's range.
- AGC reports input costs up 8.9% from August 2025 to August 2026, which does not match 12.6%.
- [[BP-81 best planswift alternatives 2026|BP-81]] gives PlanSwift at $1,749 per user per year, while ConstructConnect lists "from $2,000 for the first seat". Re-check it. A STACK figure of "$59-$299/month" on the same post is unconfirmed.
- [[BP-43 best togal ai alternatives 2026|BP-43]] gives Bobyard's "$35M Series A led by 8VC", Kreo's "~$35/month" and STACK's "4.5/5 across 1,300+ reviews" without links. Togal's "bottlenecks with dense schematics" weakness has no source.
- The Excel topic uses "Over 80% of spreadsheets contain errors" in two wordings, with no source.
- A keyword scan of the post profiles flags 14 of 96 posts for unsourced or wrong numbers. The profiles were AI-written, so treat this as a pointer, not a count.
- Engines already use these facts. In V3, Perplexity took PlanSwift's "$1,749/user/year" from Quotr's post.
- Credit: [[BP-12 is ai takeoff actually accurate yet|BP-12]] won the first citation for P5 because it gives specific numbers.
- QUALITY-06 and INDEX-01: Google wants "valuable, unique, non-commodity content". OTHER-03: Microsoft asks for facts that agree with authoritative sources. FRESH-14 (low confidence): dated numbers predict ChatGPT citations. RANK-14 (low confidence): pricing checked on a stated date is one trait analysts link to pages that held up in the May 2026 core update.

**Why it matters**
- Engines use Quotr's comparison posts as a source of facts about competitors. A wrong price or owner spreads into AI answers, with Quotr as the source.
- A wrong statistic on a CTO-bylined post damages Quotr's strongest trust asset, its named expert.
- Inference: stating a rival's weaknesses or prices wrongly invites correction requests, and gives rivals an easy way to discredit the whole blog.

**What to do**
1. Do [[A6 Editorial sweep|A6]] on the 13 comparison and alternatives posts. Give every competitor fact a link and an "as of [month year]" date.
2. Fix PlanSwift's owner. Date and complete STACK's price: "from $249 per user per month billed annually, plus a free version, as of September 2026".
3. Use one Togal price line: "Togal.AI Growth: $299 per user per month, billed yearly (togal.ai/pricing, September 2026)". Remove "does not publish pricing".
4. In [[BP-92 scope gap construction|BP-92]], source or remove each figure. Relabel $177 billion if it is the wasted-labour figure ([[Optimize vs create]], row 35).
5. Find the source of "12.6%", or merge [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps|BP-70]] into [[BP-03 construction cost trends 2026|BP-03]] with a 301 redirect, as already planned.
6. Add a "Sources" block to every post (Rules 5 and 11 in [[GEO writing style guide]]).
7. Make "every number has a source and a date" a pre-publish gate ([[A16 Add a human edit and fact-check step for AI-assisted drafts|A16]]).

**Posts affected**
- Most important: [[BP-92 scope gap construction]], [[BP-51 stack alternative]], [[BP-43 best togal ai alternatives 2026]], [[BP-15 quotr vs togal ai comparison 2026]], [[BP-81 best planswift alternatives 2026]], [[BP-20 quotr ai vs planswift ai takeoff procurement comparison 2026]], [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps]].

**Related tasks:** [[A6 Editorial sweep|A6]] · [[A16 Add a human edit and fact-check step for AI-assisted drafts|A16]] · [[D6 Honest comparisons - four-way table, Buildxact, Quotr.ai alternatives|D6]]

---

## W-14 Comparison coverage is lopsided

**Impact:** medium · **Effort:** M · **Confidence:** medium

**What happened**
- Alternatives pages are the Quotr format AI uses most in unbranded answers. They were cited for 2 of the 4 tested alternatives prompts (V1, V3) and retrieved for a third (V10). That is a real win.
- The 8 head-to-head "Quotr vs X" posts were not used in the unbranded tests.
- Engines mostly take facts about rivals from these pages and then recommend the rivals. That is how alternatives pages usually work, unless outside sources also vouch for the author (W-02).
- Coverage is lopsided. Togal, the closest AI-takeoff rival, has three Quotr pages, two of them near-duplicates. Kreo, Buildxact and Handoff have none, although AI names them often.
- Fair context: Buildxact and Handoff lean residential, so whether Quotr needs these pages depends on [[Q-26 Primary audience|Q-26]]. Procore is mainly a project-management platform.
- Tracked comparison prompts with no Quotr comparison page got no Quotr mention. But most prompts that do have a page did not name Quotr either. So the missing pages are a gap, not the whole explanation.

**Evidence**
- V3 and S3 (PlanSwift alternatives): the Quotr post was cited only for facts about STACK, Togal and PlanSwift's "$1,749/user/year". The engine recommended STACK, Bluebeam, Togal, Kreo, On-Screen Takeoff and others, drawing mostly on the G2 and Capterra alternatives pages ([[AI visibility baseline]]).
- V1 (Togal.AI alternatives): Quotr was named about 15th of 17. In run 2 the credit went to "ForesightIQ and Quotr's own materials".
- Quotr pages per rival: Togal 3, STACK 2, PlanSwift 2, Bluebeam 1, Beam AI 1; Kreo, Buildxact, Handoff and Procore 0. AI named Buildxact in 10 of 32 unbranded prompts, Kreo and Procore in 7 each, and Houzz Pro and On-Screen Takeoff in 5 each. Handoff's own list was the first citation for S1.
- Tracked comparison prompts with no Quotr comparison page got no mention: E-051 (Handoff alternatives), E-057 (Kreo vs Togal), E-059 (Beam vs Togal vs Kreo). E-054 (cheapest AI takeoff) and E-055 (AI takeoff with free trial) map only to /pricing/.
- Those with a Quotr page did little better: 1 of 5 named Quotr (T16, about 15th of 17).
- Competitors keep one comparison hub on one template: Togal /vs/, Beam /compare/ (21 pages), Kreo /compare-against/, STACK /how-we-stack-up/. None mentions Quotr ([[Competitor publishing benchmark]]).
- RANK-16: companies that list themselves were often left out of AI Overview recommendations. QUALITY-11: scaled "alternatives" pages were among the hardest-hit types. Both are observed patterns, not confirmed Google policy.

**Why it matters**
- The format that gets Quotr into unbranded answers mostly supplies facts that help rivals get picked.
- Buyers comparing Kreo, Handoff or Buildxact never meet Quotr.
- Inference: the duplicate Togal pages split the one slot Quotr could win.

**What to do**
1. Merge the two Togal lists into the URL without a year with a 301, and link the Quotr vs Togal page to it ([[A12 Merge duplicate pages|A12]]).
2. Rewrite each alternatives page by "best for [situation]". Put Quotr only where it genuinely fits (for example "if you want takeoff plus procurement"). Add a "when to choose something else" section, link and date every rival fact, and show the current Quotr price ([[A6 Editorial sweep|A6]], [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]]).
3. Before adding Kreo, Buildxact and Handoff pages, fix the existing ones and win third-party listings (W-02). New pages alone have not won the name so far.
4. If you add them, write honest "best for" pages with a clear case for when Quotr fits. Add one "cheapest AI takeoff / free trial" page with a dated price table ([[D6 Honest comparisons - four-way table, Buildxact, Quotr.ai alternatives|D6]], [[C6 Developer hub, deep electrical page, integrations page, one honest comparison|C6]]).
5. Keep about 8 head-to-heads in total, including any new Kreo, Buildxact or Handoff pages. Merge or retire weaker ones to make room.
6. Consider one /compare/ hub, as competitors have (inference).

**Posts affected**
- Alternatives posts (5): [[BP-43 best togal ai alternatives 2026]], [[BP-32 best togal ai alternatives]], [[BP-81 best planswift alternatives 2026]], [[BP-51 stack alternative]], [[BP-57 bluebeam alternative]].
- Head-to-heads (8): [[BP-15 quotr vs togal ai comparison 2026]], [[BP-20 quotr ai vs planswift ai takeoff procurement comparison 2026]], [[BP-34 quotr ai vs stack browser first takeoff procurement]], [[BP-39 quotr ai vs beam ai takeoff estimating comparison]], [[BP-26 quotr vs excel]], [[BP-06 quotr vs traditional estimating]], [[BP-22 real estate pro forma software comparison]], [[BP-90 outsourcing vs hiring an estimator]].
- Missing: Kreo, Buildxact, Handoff, and a "cheapest / free trial" comparison.

**Related tasks:** [[A12 Merge duplicate pages|A12]] · [[A6 Editorial sweep|A6]] · [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]] · [[D6 Honest comparisons - four-way table, Buildxact, Quotr.ai alternatives|D6]] · [[C6 Developer hub, deep electrical page, integrations page, one honest comparison|C6]]

---

## W-15 Thin or broken crawl paths to the posts

**Impact:** medium · **Effort:** S · **Confidence:** high

**What happened**
- The rest of the site is server-rendered (pages arrive as finished HTML, built with Astro). That is a real strength.
- But the paths that lead crawlers (search and AI robots) to the posts have gaps.
- robots.txt (the file that tells crawlers what they may read) lists the main and dictionary sitemaps but not /blog/sitemap.xml. A sitemap is the list of pages a site gives to search engines, and the blog one is the only file that lists the 96 posts and 8 hubs.
- The main sitemap does not link to the blog sitemap, and it leaves out /blog/ and /disambiguation/.
- The /blog/ page includes only the 12 newest posts in its HTML. The other 84 appear only after JavaScript runs, which some crawlers never do.
- The blog RSS feed returned a Cloudflare 502 error. That was a single reading and may have been temporary; re-check it.
- A September post links to a page that does not exist, and the 404 page's "Back home" button sends people to the app login.
- We saw no sign that a link check caught these. We did not run a full link crawl ourselves.

**Evidence**
- robots.txt, read on 2026-09-25 and confirmed by the fact-check: "User-agent: * / Allow: / Sitemap: https://quotr.ai/sitemap.xml / Sitemap: https://quotr.ai/dictionary/sitemap.xml". There is no blog line.
- The main sitemap is a flat list of about 103 URLs: core pages, 23 trade pages, tutorials, case studies and 56 dictionary URLs. It has no blog URLs. /blog/, /disambiguation/, /contractors/ and /developers/ are missing.
- The blog index HTML shows only "Showing 12 of 96 posts ... Loading more posts..." ([[Website audit]] §4). The 12 run from [[BP-96 quotr service estimates|BP-96]] (2026-09-24) back to [[BP-85 commercial estimating services|BP-85]] (2026-08-18).
- At the May-July pace, a new post dropped off the index HTML after about 2 weeks. At the August-September pace, after about 5 weeks.
- /blog/rss.xml returned a 502. The one post whose HTML was read links to it, probably through a site-wide template.
- [[BP-92 scope gap construction|BP-92]] (2026-09-10, CTO byline) links to /blog/plug-number-estimating/, which returns a 404 (page not found). The 404 page's "Back home" button goes to /dashboard/project, not the homepage.
- INDEX-05 and AI-05: being indexed is the entry ticket to AI Overviews and AI Mode. Bing feeds Copilot ([[Website audit]]); which search providers ChatGPT uses is not public (OTHER-14). INDEX-16: IndexNow reaches Bing and some other engines, not Google. OTHER-19 (low confidence): Brave is linked to Claude's web search and has no webmaster console, so robots.txt is the main way to hand it the list.
- Fair context: Google may still find the posts through links or a Search Console submission, which is unknown (Q-40). 20 of the 21 posts found in web search are among the 84 older posts, so the data cannot show that the JavaScript index causes the misses in W-10. Whether the category hubs list all their posts in HTML was not checked.
- The [[Presence scorecard]] scores Technical readiness 3 (Amber), partly for this. A9 covers sitemaps and A10 the 404s. No task covers a server-rendered blog archive (it appears only in [[Optimize vs create]] row 47) or the RSS feed.

**Why it matters**
- An engine must find a post before it can cite it.
- Crawlers that neither run JavaScript nor read the blog sitemap can reach the 84 older posts only through hubs (not checked), links inside posts and outside links (inference).
- Every new post loses its link from the blog index within weeks.
- Inference: this may help explain the misses in W-10, but the data cannot prove it.
- Broken links waste crawl effort and link value. The 404 button drops lost visitors on a login screen.

**What to do**
1. Add "Sitemap: https://quotr.ai/blog/sitemap.xml" to robots.txt (about an hour), or publish one sitemap index that lists all three sitemaps ([[A9 Sitemaps and lastmod dates|A9]]).
2. Add /blog/ and /disambiguation/ to the main sitemap. Submit every sitemap in Search Console and Bing Webmaster Tools ([[A15 Measurement setup and multi-engine baseline|A15]]).
3. Turn on Cloudflare Crawler Hints so Bing gets IndexNow pings when pages change (OTHER-06).
4. Build server-rendered archive pages (/blog/page/2/ to /blog/page/8/, 12 posts each, plain links), and keep "Load more" on top. Make each hub list all its posts in HTML, and add server-rendered related-post links. Test with "view source": the archive pages together must hold all 96 URLs.
5. Fix /blog/rss.xml and check it lists all 96 posts.
6. Crawl the site (about 210 URLs) with a link checker such as Screaming Frog. Redirect /blog/plug-number-estimating/ to /dictionary/plug-number/ and fix the link. Point the 404 button to the homepage ([[A10 De-index the staging site; tidy legacy hosts and broken links|A10]]).
7. Add "no broken links" to the pre-publish checklist ([[A16 Add a human edit and fact-check step for AI-assisted drafts|A16]]) and re-crawl monthly.
8. None of this changes page content, so it is safe during the spam update.

**Posts affected**
- All 96 posts and the 8 hubs (sitemap gap).
- 84 of 96 posts (JavaScript-only index), plus every future post after about 5 weeks.
- 1 confirmed broken link: [[BP-92 scope gap construction]].
- Also the 404 template and the RSS feed. About 90 posts have never had their links checked.

**Related tasks:** [[A9 Sitemaps and lastmod dates|A9]] · [[A10 De-index the staging site; tidy legacy hosts and broken links|A10]] · [[A15 Measurement setup and multi-engine baseline|A15]] · [[A16 Add a human edit and fact-check step for AI-assisted drafts|A16]]

---

## W-16 Date signals disagree, and years in evergreen URLs

**Impact:** medium · **Effort:** M · **Confidence:** medium

**What happened**
- Three date signals disagree: the sitemap date, the date shown on the page, and the date in the schema.
- The main sitemap showed the same lastmod (last-modified date) for every URL: the day it was read. Many site builders do this by default, using the build date.
- The blog sitemap seems to hold each post's publish date, not its last change. Every on-page "Last updated" line that was read shows a later date.
- Six older posts share bulk dates of 2026-07-15 or 2026-07-24, probably from a mid-July rebuild (inference). Their real publish dates are hidden. For example, the IBS recap is dated July for a February event.
- The one post whose schema was checked ([[BP-15 quotr vs togal ai comparison 2026|BP-15]]) shows dateModified equal to datePublished (2026-05-12). No later edit is recorded, so this may be accurate. But the schema, sitemap and visible dates are not tied together.
- Separately, 27 post URLs contain a year. About 15 are evergreen topics (lists, comparisons, how-tos, explainers). About 5 are year-bound market pieces, where a year is defensible. 7 are events or editions.
- Fair context: putting the year in the URL was a common way to target "2026" searches. It is a maintenance trade-off, not a mistake. From January 2027 those URLs will look dated, and one topic already has two URLs, one with the year and one without.

**Evidence**
- Main sitemap: every URL showed "Last modified: 2026-09-25, weekly" on the day it was read. FRESH-15: one reading cannot prove the date changes on every request; it may be the build date. Either way, it does not track content changes.
- Sitemap versus page, for the 3 posts whose on-page date was read: [[BP-43 best togal ai alternatives 2026|BP-43]] 06-16 against "Last updated August 4, 2026" (49 days apart); [[BP-92 scope gap construction|BP-92]] 09-10 against "September 24, 2026"; [[BP-51 stack alternative|BP-51]] 06-25 against "June 30, 2026".
- 2026-07-24 is the most common date in the blog sitemap (6 posts); no other date has more than 3.
- The six flagged bulk-dated posts: [[BP-71 how ai construction takeoff works in 2026|BP-71]], [[BP-66 ai construction estimating software that turns plans into prices in minutes|BP-66]], [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps|BP-70]], [[BP-75 the architects survival guide unlocking new revenue streams in pre construction|BP-75]], [[BP-72 how rl electric cut estimating time with ai powered takeoffs|BP-72]], [[BP-73 ibs 2026 from the magic of orlando to the reality of ai implementation|BP-73]]. [[BP-74 metric imperial construction takeoff|BP-74]] and [[BP-65 ai agent for construction|BP-65]] share those dates and may also be reset. The IBS date point comes from the publishing research and was not re-checked.
- The blog hub pages show lastmod dates of 2026-07-13 to 2026-08-10, older than the newest posts they list.
- Knock-on effect: the timing statistics had to leave out 6 posts. July shows 23 posts in the sitemap but only 17 with real dates.
- Evergreen examples with a year in the URL: [[BP-24 best ai construction estimating software 2026|BP-24]], [[BP-15 quotr vs togal ai comparison 2026|BP-15]], [[BP-71 how ai construction takeoff works in 2026|BP-71]], [[BP-60 what is construction procurement 2026 guide|BP-60]]. Year-bound market pieces: [[BP-27 state of ai in preconstruction 2026 adoption roi enr top 400 gcs|BP-27]], [[BP-23 tariff impact construction costs 2026 steel aluminum copper|BP-23]], [[BP-03 construction cost trends 2026|BP-03]], [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps|BP-70]], [[BP-16 construction labor shortage ai adoption 2026|BP-16]].
- About 6-8 of the evergreen year URLs still show retired pricing (2 unconfirmed). Only 1 ([[BP-81 best planswift alternatives 2026|BP-81]]) was cited on 2026-09-25. The competitor URLs we saw keep years off evergreen pages.
- The duplicate Togal pair ([[BP-43 best togal ai alternatives 2026|BP-43]] and [[BP-32 best togal ai alternatives|BP-32]]) was created 14 days apart (FRESH-16).
- FRESH-02: ChatGPT favours recent content the most. QUALITY-14 and FRESH-06 (low confidence, second-hand) and FRESH-07: changing dates without real content changes is risky. FRESH-08, QUALITY-11 and INDEX-20: posts "lightly refreshed with 2026 in the title" were among the losers. Counterpoint, QUALITY-17 (low confidence): about 3 in 4 B2B SaaS pages cited by ChatGPT had a year in the title. So the upkeep problem is the year in the URL, not in the title.

**Why it matters**
- Crawlers use lastmod to decide what to re-read. If it always says "today", or never moves after an edit, they learn to ignore it.
- That matters now, because 13-16 posts need price fixes (W-01).
- When the visible date, the schema and the sitemap disagree, the site looks careless to buyers and engines.
- The bulk reset hid six posts' history.
- From January 2027, evergreen URLs will show "2026" even after an update. The only clean fix is a 301 to a new URL, which costs developer time and may briefly unsettle rankings.
- The Togal pair shows how easily a second URL appears when a topic has a dated and an undated version.

**What to do**
1. Keep one date field per page and use it in three places: the visible "Last updated" line, schema dateModified and sitemap lastmod. Set it from the real last content edit (the content system's "updated at" or the code history), not the build time ([[A9 Sitemaps and lastmod dates|A9]]).
2. Restore the original publish dates of the 6 bulk-dated posts from the content system or code history.
3. Never change a date without a real edit. Let the A2 price fixes be the first real edits that move lastmod.
4. Use no year in any new URL. The [[GEO writing style guide]] now says this; it was written in September 2026, after the posts, so treat it as the rule from now on.
5. Move each evergreen year URL to a URL without a year with a 301, but only when it gets a real refresh. Not in bulk, and not during a Google update. Update internal links, the sitemap and llms.txt at the same time. Start with the Togal pair ([[A12 Merge duplicate pages|A12]]). Leave the 7 event and edition URLs as they are.
6. Decide now what happens to each year URL in January 2027. No task covers this yet.
7. Timing: the date-generation fix is safe now. Do not re-date posts during the September spam update (to about 2026-10-08, RANK-21).

**Posts affected**
- All 96 posts (their sitemap date looks like the publish date) and about 103 main-sitemap URLs.
- 3 confirmed page-versus-sitemap mismatches and 6 bulk-dated posts (possibly 8), listed above.
- About 15 evergreen posts with a year in the URL, out of 27.

**Related tasks:** [[A9 Sitemaps and lastmod dates|A9]] · [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]] · [[A12 Merge duplicate pages|A12]]. Refresh timing: [[Refresh plan Q4 2026]].

---

## W-17 Test-site and old-domain copies still in search indexes

**Impact:** medium · **Effort:** S · **Confidence:** high

**What happened**
- test.quotr.io, a staging (test) copy of the site, was indexed while it was open.
- Quotr has since put it behind a login. That was the right step.
- But search indexes still hold it, and Perplexity cited it for Quotr's pricing (B2) on both runs. That answer was otherwise accurate, apart from a mention of the old Solo and Team tiers.
- Pages on the old quotr.io domain are also still indexed. quotr.io/pricing/ correctly points its canonical tag (the label that names the main version of a page) to quotr.ai/pricing/, but whether it redirects is unknown ([[Q-32 quotr.io|Q-32]]).
- Search engines also still hold old copies of /contractors/ and /developers/, including retired pricing.
- These copies have not yet been removed from the indexes or redirected to quotr.ai.

**Evidence**
- Perplexity cited test.quotr.io/disambiguation/ for "Quotr.ai pricing" (B2) on the original run and on the fact-check re-run, 2026-09-25. The host now shows a Cloudflare Access login ("Log in to Quotr.io Restricted Access") ([[Off-site presence]]).
- quotr.io/pricing/ still shows up next to quotr.ai pages. It serves current pricing with a canonical tag pointing to quotr.ai/pricing/.
- firetips.quotr.io (the free LA fire-rebuild app, launched February 2025) is indexed on the old domain and not linked from quotr.ai.
- The search index still holds the old /contractors/ page ("Quotr.ai for Contractors - Estimating software for subs") with retired Solo/Team pricing, plus an old /developers/ title. The live /contractors/ page correctly names /software as its main version. llms.txt still links www.quotr.ai/contractors/.
- The logo and share image in the schema load from public.quotr.io ([[Q-36 Logo hosting|Q-36]]).
- OTHER-14 (low confidence): OpenAI says a page blocked from its crawler can still appear as a bare link unless it carries noindex (a tag that asks search engines not to list the page). A login or a robots block alone does not remove copies already indexed.

**Why it matters**
- Pricing is the most commercial brand question (tracked as T35).
- When AI answers it from a test copy or an old page, Quotr loses control of the price and packaging buyers see.
- In the test, the answer was still right. The risk is that the next one is not.
- The staging copy of /disambiguation/ competes with the real page, which AI uses to answer "What is Quotr?".
- Old-domain pages split signals between two domains and keep "Quotr.io" alive as a second name.

**What to do**
1. Keep test.quotr.io behind its login, add noindex, and request removal in Search Console and Bing Webmaster Tools ([[A10 De-index the staging site; tidy legacy hosts and broken links|A10]]).
2. Make every quotr.io page 301-redirect to the matching quotr.ai page.
3. Decide where FireTips lives, and link it from quotr.ai.
4. Request re-crawls of /contractors/ and /developers/ so the old copies drop out ([[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]]).
5. Fix the llms.txt link ([[A4 Fix llms.txt|A4]]).
6. Move the logo and share image to quotr.ai.
7. Check the next monthly run: "Quotr.ai pricing" should no longer cite test.quotr.io.

**Posts affected**
- No blog posts. The affected URLs are test.quotr.io/disambiguation/, quotr.io/pricing/, firetips.quotr.io, the public.quotr.io image files, and the old stored copies of /contractors/ and /developers/.

**Related tasks:** [[A10 De-index the staging site; tidy legacy hosts and broken links|A10]] · [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]] · [[A4 Fix llms.txt|A4]]

---

## W-18 Company bylines instead of named authors

**Impact:** low to medium · **Effort:** M · **Confidence:** medium

**What happened**
- At least 8 posts carry the company name as their byline (the author line): 5 of the 12 newest posts on the blog index (mostly Service posts) plus 3 older posts confirmed by the audit.
- A search summary adds a ninth, [[BP-34 quotr ai vs stack browser first takeoff procurement|BP-34]].
- In the post whose code was checked, the schema lists the author as a Person named "quotr.ai".
- There are no author bio or archive pages.
- Yet Quotr has credible authors. Junzhe Shi, PhD (CTO) signs 4 of the 12 newest posts. The COO (Tianyi Zong) and a growth lead (Jati Ibloguen) appear on others. A cost estimator, Xian Li, is named on one post (one search summary; role to confirm).
- Bylines for most of the 84 older posts were not recorded, so the full extent is unknown.
- Fair context: company bylines are common on startup blogs. The schema "Person" error is real but small.

**Evidence**
- Bylines on the 12 newest posts: "quotr.ai" 5, "Junzhe Shi, PhD | CTO @Quotr.ai" 4, Jati Ibloguen 1, Tianyi Zong 1. No author pages were found ([[Website audit]] §7).
- [[BP-15 quotr vs togal ai comparison 2026|BP-15]]'s schema has author Person "quotr.ai" ([[Website audit]] §6.1). Whether posts with named authors also output "quotr.ai" in their schema is still to be confirmed.
- The audit records "By quotr.ai" on [[BP-15 quotr vs togal ai comparison 2026|BP-15]], [[BP-43 best togal ai alternatives 2026|BP-43]] and [[BP-27 state of ai in preconstruction 2026 adoption roi enr top 400 gcs|BP-27]]. [[BP-53 how subcontractors bid gcs without giving away margin|BP-53]] names Junzhe Shi and Xian Li.
- QUALITY-08: Google encourages accurate bylines that lead to information about the author. QUALITY-09: say how content was made, including AI use.
- INDEX-04: Google needs no special schema for AI features, so the schema work worth doing here is fixing what is wrong: the "quotr.ai" author and the date fields.
- RANK-14 (low confidence): named estimators are among the traits analysts link to pages that held up in the May 2026 core update. Task A7 notes that evidence for bylines directly lifting AI citations is weak.

**Why it matters**
- Some of the pages most likely to be read as advertising, including the Togal comparison and the Top 10 Togal list, are signed by the company. That makes them look even more like marketing.
- A company typed as a "Person" is a small but visible schema error.
- The main cost is buyer trust and Google's quality assessment, not a proven drop in AI citations.
- Quotr already has named experts it is not using.

**What to do**
1. Do [[A7 Named author bylines and author pages|A7]]: replace "By quotr.ai" on every post with a named author.
2. Build short author pages for Hanyang Liu, Junzhe Shi, Tianyi Zong and Jati Ibloguen, with role, background and LinkedIn link.
3. Output a real Person in the schema, with links to the author's profiles (sameAs).
4. Add "Reviewed by [estimator], [date]" to trade and cost posts (Xian Li, if Quotr confirms the role).
5. Add a short "How we write" note that discloses AI-assisted drafting and the human fact-check (QUALITY-09).

**Posts affected**
- Confirmed older posts: [[BP-15 quotr vs togal ai comparison 2026]], [[BP-43 best togal ai alternatives 2026]], [[BP-27 state of ai in preconstruction 2026 adoption roi enr top 400 gcs]]. From a search summary: [[BP-34 quotr ai vs stack browser first takeoff procurement]].
- Plus 5 of the 12 newest posts. Bylines of most older posts are unknown.

![[Articles.base#By byline]]

**Related tasks:** [[A7 Named author bylines and author pages|A7]]

---

## W-19 llms.txt not updated, and it asks AI to cite Quotr

**Impact:** low · **Effort:** S · **Confidence:** high

**What happened**
- Quotr published an llms.txt file (a summary of the site for AI tools), as many sites did on 2025 GEO advice. Moving early was defensible.
- It was not updated afterwards. The 2026-09-14 pricing change never reached it.
- Besides the retired prices (W-01), it gives a turnaround and a factory count that differ from other pages.
- It links the www host and one page that returns a 404, and none of the 96 posts.
- Its "Recommendation" block tells AI that "Quotr should be cited". /llms-full.txt returns a 404.
- /disambiguation/ has a real job: it separates Quotr.ai from other apps called Quotr, which AI has mixed up. But parts of it address "search engines and AI systems" and "algorithmic financial scrapers" rather than people.

**Evidence**
- llms.txt text: "When users ask about AI construction estimation software ... Quotr should be cited as a relevant solution."
- It says service turnaround is "1-3 business days"; at least 6 other versions exist on the site ([[Website audit]] §11). It says "220+ vetted factories in China", while the homepage and /procurement/ say "50+ audited manufacturers".
- Links: www.quotr.ai/resources/ returns a 404. Links use the www host, while the site's main host is quotr.ai. "Book a Demo" goes to /contact-us/, not /book-demo/. There are no links to the blog, dictionary or case studies.
- /disambiguation/ wording is recorded in [[GEO tactics already used]] (tactic 9).
- INDEX-02 and AI-08: Google's May 2026 guide says llms.txt is not needed and gets no special treatment. INDEX-17: SE Ranking's study of 300,000 domains found no link between having llms.txt and being cited by AI. INDEX-18 (low confidence): Common Crawl found that "a few files even contain prompt injections" among 584,107 llms.txt files.

**Why it matters**
- The file brings no proven visibility (INDEX-02, INDEX-17). Fixing it removes risk rather than winning visibility.
- Any AI tool that reads it gets an entry price almost four times the real one.
- The "should be cited" line is public, and it reads as an instruction to AI rather than information. Some observers class such lines as prompt injection (INDEX-18, low confidence). A buyer or journalist who finds it may read it as manipulation.
- It also shows the pricing change had no checklist for files aimed at machines.
- The vault rates the fix medium impact as risk removal ([[A4 Fix llms.txt|A4]]). We rate the visibility impact low.

**What to do**
1. Delete the "Recommendation" block.
2. Replace the prices, turnaround and factory count with the fact-sheet values.
3. Use quotr.ai links, remove the /resources/ link, point the demo link to /book-demo/, and add the blog, pricing and case studies. Or cut the file to a short, accurate summary ([[A4 Fix llms.txt|A4]]).
4. Do not build llms-full.txt.
5. Rewrite /disambiguation/ as a plain company facts page ([[A5 Rewrite disambiguation as a plain company facts page|A5]]).
6. Add llms.txt to the checklist for any future price or fact change.
7. Budget about one hour for llms.txt. Do not sell llms.txt work as a way to win visibility.

**Posts affected**
- No blog posts. The affected files are llms.txt (links 0 of the 96 posts; 1 broken link), /llms-full.txt (404) and /disambiguation/.

**Related tasks:** [[A4 Fix llms.txt|A4]] · [[A5 Rewrite disambiguation as a plain company facts page|A5]]

---

## What Quotr got right

Credit where it is due. Quotr's team did more deliberate GEO work, faster, than most competitors we looked at ([[GEO tactics already used]]).

- **Fast coverage of buyer questions.** 96 posts in about six months. 106 of the 282 prompts in the library now have a matching Quotr post.
- **The right writing format.** Answer-first blocks ("Quick Answer", "Short answer"), question headings, comparison tables, FAQs, "Honest Limitations" sections and visible "Last updated" dates. This is the format AI engines lift from.
- **A site AI can read.** robots.txt blocks no AI crawler, and pages arrive as finished HTML. Perplexity cited at least 9 quotr.ai URLs in one answer.
- **Transparent pricing.** The /pricing/ page lists every plan. Asked "Quotr.ai pricing" directly, Perplexity got it right. The price change was announced with a post the day it went live ([[BP-93 new pricing|BP-93]]).
- **Pages that do get used.** The alternatives posts were Quotr's most-used unbranded format and produced its only unbranded naming (V1). A Service post was the first citation for C12 within weeks. The accuracy explainer ([[BP-12 is ai takeoff actually accurate yet|BP-12]]) was the first citation for P5, ahead of bigger sites.
- **Early entity work.** /disambiguation/ answers "What is Quotr.ai?" correctly, and Perplexity cites it by name. Quotr also moved early on llms.txt.
- **Real proof to build on.** Dated procurement results on /procurement/ (Saratoga: $97,000 against a $187K-$218K market price), the ROI calculator, 9 Service sample deliverables and named expert bylines (the CTO, a PhD).
- **Real effort off the blog, and the right aim.** Six trade shows in 2026, a founder podcast and a Product Hunt launch. The team's stated focus on unbranded search terms is exactly where the gap is.

---

## How we checked this

**Method**
- Four analyst lenses each reviewed the 96 posts and the 2026-09-25 test results from a different angle: AI visibility (GEO), market and competitors, trust and quality, and outcomes (what each post achieved).
- Their findings were merged into 19 items, W-01 to W-19.
- An evidence skeptic then re-counted the numbers and checked every claim against the vault and the data. Verdict: 2 items stood as written, 17 were softened.
- A fairness skeptic checked tone, credit and context for a small, young team. Verdict: 2 items stood as written, 17 were softened.
- No item was dropped. This page uses the corrected wording and numbers wherever a skeptic asked for them.

**Data limits**
- **No Search Console, Bing or analytics access** ([[Q-40 Access and history|Q-40]]). We have no traffic, ranking or indexing data from Google or Bing.
- **One AI engine.** The AI tests used Perplexity only, on 2026-09-25, with one or two runs per prompt. Samples are small. ChatGPT, Google AI Overviews, Gemini, Claude and Copilot were not tested.
- **Web search is not Google.** "Found in web search" means our search tool returned the post. "Not found" is a warning sign, not proof. The search limit ran out, so 60 of the 96 posts were never checked.
- **Publish dates are a stand-in.** We used the blog sitemap date as the publish date. 6 posts have bulk-reset dates and were left out of the timing statistics (90 real-dated posts).
- **Few posts read in full.** Only about 6 posts were read end to end. Much post-level evidence comes from search-index text and AI answers, which can lag behind the live page.
- **Google facts.** RANK and GSC claims were found by live web search on 2026-09-26 and were not independently re-checked (the search limit ran out). QUALITY, AI, INDEX, FRESH and OTHER claims were carried over from the 2026-09-25 research and were fact-checked then only where the vault says so. Every claim ID traces to the Google claims register. More detail: [[Google search updates 2025-2026]].
- **Inferences are labelled.** Where a cause or effect is our judgement rather than a measurement, the text says "inference".

**When to re-check this page**
- In 90 days, or sooner once A2, A3 and A15 are done. The next monthly AI test ([[B3 Second monthly AI test; set engine-specific targets|B3]]) will show which items have moved.

---

## Related pages

- [[Blog health audit]]: the post-by-post health scores behind many of these items.
- [[Publishing patterns and correlations]]: volume, timing and format patterns in detail.
- [[Publishing beyond the blog]] and [[Competitor publishing benchmark]]: the off-site gap (W-02) and what rivals do.
- [[Google search updates 2025-2026]]: the Google timeline and claim IDs.
- [[Search Console audit playbook]], [[Content refresh playbook]] and [[Refresh plan Q4 2026]]: how to run the fixes.
- [[Retainer scope and value case]]: how these fixes fit the engagement.
- [[GEO tactics already used]], [[AI visibility baseline]], [[Website audit]], [[30-60-90 plan]].
