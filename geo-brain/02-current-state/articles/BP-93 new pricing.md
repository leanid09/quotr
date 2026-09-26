---
type: article
id: BP-93
title: New pricing
quotr_url: https://quotr.ai/blog/new-pricing/
published: 2026-09-14
month: 2026-09
date_note: Blog sitemap date, used as the publish date
cluster: Company news, customer stories and event recaps
format: company news
funnel:
- BOFU
- brand
persona:
- subcontractor
- general contractor
- estimator
trade:
- multi-trade
byline: unknown
primary_query: Quotr.ai pricing
target_prompts: []
web_indexed: not checked
search_check: Not checked (the search limit was reached)
ai_cited: false
cited_in: []
old_pricing: unknown
flags:
- cited by AI
health: fair
health_score: 73
action: update
merge_into: ''
priority: high
rank: 37
status: todo
---
# BP-93. New pricing

> [!abstract] In one line
> Quotr's only product-update post and the source for current pricing. Perplexity cites it for 'Quotr.ai pricing'. Check that it spells out the retired Solo/Team plans so it stops feeding the stale-price error.

**Live page:** [New pricing](https://quotr.ai/blog/new-pricing/) *(title taken from the web address; the live title was not captured)*  
**Published:** 2026-09-14 · **Cluster:** Company news, customer stories and event recaps · **Format:** company news · **Funnel:** BOFU/brand

## What it covers

From the vault, not web search: the 2026-09-14 announcement 'Introduces New Software Pricing: Lite, Plus, and Enterprise', which replaced the old Solo/Team tiers. It is Quotr's only product-update post. Perplexity cited it for the brand prompt 'Quotr.ai pricing' (visibility test B2). *(from web search results)*

**From the 2026-09-25 audit:** "Introduces New Software Pricing: Lite, Plus, and Enterprise"; cited in brand prompts

## Health check

**Score: 73/100 (fair).** Each area is scored 0-5 using the rubric in [[Content refresh playbook]].

| Freshness | Accuracy | Trust | Structure | Visibility | Uniqueness |
|---|---|---|---|---|---|
| 4 | 4 | 3 | 3 | 4 | 4 |

- **Visibility:** Perplexity cited this post for the brand prompt 'Quotr.ai pricing' (test B2, tracked as T35). It cited it next to the remark that 'some Quotr blog pages … mention older … Solo and Team tiers'. The enriched record says ai_cited = false only because the B2 test-run note lists domains, not URLs. The raw test notes name this post. *(from 2026-09-25 AI tests (Perplexity B2; quotr_ai_visibility_tests.md line 109))*
- **Visibility:** We do not know if Google or Bing index it. The web-search check never ran because the budget was used up. *(from 2026-09-25 audit (record: web_indexed 'not checked'))*
- **Accuracy:** The fact sheet names this post as the Sep 14, 2026 announcement of Lite $79.90, Plus $299.90 per seat per month and Enterprise custom. Those prices match /pricing/ as scraped on 2026-09-25. Nobody has checked whether the post body also names the old Solo/Team tiers without saying they were replaced. *(from 2026-09-25 audit (Entity fact sheet, pricing row))*
- **Accuracy:** The retired prices 'Solo $299.90 / Team $499.90' and 'from $299.90' still appear on about 13 Quotr URLs and in llms.txt. Perplexity repeated them in tests V2 and B4. The correct Plus price is the same $299.90 as the old Solo price, which makes the confusion easy. *(from 2026-09-25 AI tests (V2, B4) and 2026-09-25 audit (task A2))*
- **Accuracy:** Quotr has not confirmed annual pricing, and SSO is no longer listed under Enterprise. Neither should appear in the post as fact. *(from 2026-09-25 audit (Entity fact sheet: TO CONFIRM))*
- **Freshness:** The post has a real date, 2026-09-14, not a bulk-reset date. For the 12 newest posts, the sitemap lastmod matches the blog index. The slug 'new-pricing' will mislead once prices change again. *(from 2026-09-25 audit (Website audit 8.6); the 'will mislead' part is inferred)*
- **Trust:** Nobody has seen the byline. 5 of the 12 newest posts that were checked are signed 'By quotr.ai', so this post may be too. *(inferred (from task A7 evidence))*
- **Structure:** Nobody has seen the page. The recorded title suggests a plan announcement. We do not know if it has a plan table or a short answer at the top. *(inferred)*
- **Uniqueness:** It is the blog's only product-update post. The vault maps the price prompts D-008 (High, tracked T35) and D-011 (High) to /pricing/, and this post backs that page up rather than competing with it. *(from vault prompt library (D-008, D-011) and 2026-09-25 audit (Optimize vs create: KEEP, match /pricing/))*

## Search and AI visibility

- **Web search:** Not checked (the search limit was reached).
- **Cited in the September AI tests:** no.
- **Main buyer question it targets:** Quotr.ai pricing.

## What to do

**Action: Update** · **Priority:** high · **Effort:** S · **Order in the refresh queue:** 37

1. Open the live post and check every price against /pricing/ and the Entity fact sheet: Quotr.ai Lite $79.90 and Plus $299.90 per seat per month, Enterprise custom ('for complex teams and higher volume'), 7-day free trial, per seat, no setup fee. Fix any difference as part of the A2 sweep.
2. Search the post for 'Solo', 'Team', '$499.90', '1 User Plan', '2–10 Users', '$249' and '$41'. Old plans may appear only in one plain sentence: 'Solo and Team plans were retired on Sep 14, 2026. The entry price is now Quotr.ai Lite at $79.90 per seat per month.' Do not map old plans to new ones unless Quotr confirms the mapping.
3. Add a 2–3 sentence answer under the H1 with 'Quotr.ai' in the key price sentence. Then add a plan table using /software/#pricing. Plus adds advanced AI, the full Quotr database, 2 hours of guided onboarding, project sharing, 2,000 sq ft of takeoff credits per month and 10% off procurement. Enterprise adds priority support, a dedicated success manager and on-site onboarding. Mark the table 'as of Sep 2026'. The table also answers D-011 'Quotr Lite vs Plus'.
4. Leave out annual pricing and SSO until Quotr answers (fact sheet TO CONFIRM; prompt D-013). Add one line saying current prices live on /pricing/, with a link.
5. If the post says 'By quotr.ai', replace it with a named founder (A7). Keep the published date as 2026-09-14. Show 'Last updated' only after real edits, and make it match the sitemap lastmod (A9).
6. After the edit, request a re-crawl in Google Search Console and Bing (IndexNow) together with the A2 pages. Re-run D-008 (T35) and D-011 in Perplexity 2–4 weeks later. Check that the 'older Solo and Team tiers' remark is gone and that the entry price is quoted as $79.90.

**Add to the page:**
- A 2–3 sentence answer naming Quotr.ai Lite $79.90 as the entry price
- A plan table: Lite / Plus / Enterprise, price per seat per month, what each includes, 'as of Sep 2026'
- One sentence saying Solo and Team were retired on Sep 14, 2026
- A link to /pricing/ as the live source

**Title:** Keep the title the audit recorded: 'Introduces New Software Pricing: Lite, Plus, and Enterprise' (not re-seen in search). Optionally add the brand and month, for example 'Quotr.ai introduces new software pricing: Lite, Plus and Enterprise (September 2026)'. A month in an announcement title is simply accurate. It is not a freshness trick.  
**Web address (URL):** Keep [[BP-93 new pricing|BP-93]] (/new-pricing/) with no redirect. At the next price change, publish a new dated announcement. Add a one-line 'superseded' note at the top of this post linking to /pricing/ and the new post. Do not overwrite the old prices in place.

**Related tasks:** [[A2 Fact-fix sweep, part 1 - remove the old pricing everywhere|A2]], [[A7 Named author bylines and author pages|A7]], [[A9 Sitemaps and lastmod dates|A9]]

**Why now:** AI engines are cited to this post for a tracked price prompt (T35) while still repeating retired prices. Do the fix in the October 2026 A2 old-price sweep, alongside the R-02 pricing-page rebuild.

## Sources

- [[Website audit#8.6 Blog posts (all 96), grouped by cluster]] (2026-09-25 audit: sitemap date, cluster, notes)
- [[Blog health audit]] (method, limits and the overlap map)
- Web search results used: <https://quotr.ai/pricing/>

## Log

- 2026-09-26: health record created by the blog health audit (Claude). Web search was limited, so check the live page before editing it.
