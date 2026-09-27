---
type: article
id: BP-35
title: Construction cost index q1 2026 ppi rsmeans mortenson
quotr_url: https://quotr.ai/blog/construction-cost-index-q1-2026-ppi-rsmeans-mortenson/
published: 2026-06-03
month: 2026-06
date_note: Blog sitemap date, used as the publish date
cluster: Cost and market data
format: data or market report
funnel:
- TOFU
persona:
- general contractor
- developer
- estimator
trade:
- multi-trade
byline: unknown
primary_query: construction cost index 2026
target_prompts:
- '[[L-124 construction materials price index 2026 (PPI)|L-124]]'
web_indexed: not checked
search_check: Not checked (the search limit was reached)
ai_cited: false
cited_in: []
old_pricing: unknown
flags:
- no Quotr data
- year in URL
health: poor
health_score: 50
action: rewrite
merge_into: ''
priority: medium
rank: 56
status: todo
---
# BP-35. Construction cost index q1 2026 ppi rsmeans mortenson

> [!abstract] In one line
> A Q1 2026 roundup of outside cost indexes, now two quarters old. Move it to one living index tracker on a URL without year or quarter, and link Quotr's own price index when it launches.

**Live page:** [Construction cost index q1 2026 ppi rsmeans mortenson](https://quotr.ai/blog/construction-cost-index-q1-2026-ppi-rsmeans-mortenson/) *(title taken from the web address; the live title was not captured)*  
**Published:** 2026-06-03 · **Cluster:** Cost and market data · **Format:** data or market report · **Funnel:** TOFU

## What it covers

Not captured: the post did not come up in the web searches we could run. See the notes from the 2026-09-25 audit below.

**From the 2026-09-25 audit:** Third-party data roundup

## Health check

**Score: 50/100 (poor).** Each area is scored 0-5 using the rubric in [[Content refresh playbook]].

| Freshness | Accuracy | Trust | Structure | Visibility | Uniqueness |
|---|---|---|---|---|---|
| 1 | 3 | 3 | 3 | 3 | 2 |

- **Freshness:** It covers Q1 2026 only, and its sitemap date is 2026-06-03. On 2026-09-26, Q2 has closed and Q3 ends on 2026-09-30, so newer releases have probably replaced its numbers. *(from 2026-09-25 audit (blog sitemap); 'replaced' is inferred)*
- **Freshness:** The slug is tied to one quarter ('q1-2026'). The vault plans a refresh every quarter but does not say how the URL will be handled. *(from 2026-09-25 audit (Optimize vs create))*
- **Uniqueness:** The vault calls it a third-party data roundup (PPI, RSMeans, Mortenson) and plans to link Quotr's own index once it exists. Nothing suggests the page holds Quotr data. Scored 2. *(from 2026-09-25 audit; 'no Quotr data' inferred)*
- **Uniqueness:** Overlap group G07 keeps it separate from construction-cost-trends-2026, the keeper for 'why did costs go up'. This page should own the index numbers (L-124); the trends page owns the explanation. *(agreed overlap map (G07))*
- **Visibility:** Its prompt, L-124 (Medium), was not tested, and no AI test cites the post. The ENR cost page is recorded as where buyers ask the question, not as an AI citation. Scored 3: unknown, with no negative test. *(from vault prompt library (L-124); from 2026-09-25 AI tests)*
- **Visibility:** Web search visibility is unknown. The post was not checked. *(not checked in search on 2026-09-26 (search limit reached), so unknown)*
- **Accuracy:** No wrong fact is known. But Q1 numbers without a clear 'as of' date could be repeated as if they were current. *(inferred)*
- **Trust:** The slug names the outside sources, which suggests they are credited. The byline was not seen. Scored 3. *(inferred from the slug; byline not recorded)*
- **Structure:** It is a data report, which usually means tables AI can quote. The page was not seen. *(inferred)*

## Search and AI visibility

- **Web search:** Not checked (the search limit was reached).
- **Cited in the September AI tests:** no.
- **Main buyer question it targets:** construction cost index 2026.
- **Buyer questions in the prompt library it serves:** [[L-124 construction materials price index 2026 (PPI)|L-124]].

## What to do

**Action: Rewrite** · **Priority:** medium · **Effort:** M · **Order in the refresh queue:** 56

1. Replace the Q1 figures with the latest release of each index (BLS PPI for construction inputs, RSMeans, Mortenson), each with its release date and a link. Consider adding ENR's cost indexes, since ENR's cost page is where L-124 was seen. Use one table with five columns: index, what it measures, latest value, change since Q1 2026, release date.
2. Open with a 40–80 word answer to L-124 ('construction materials price index 2026 (PPI)'): the latest PPI change, what it means for material prices, and its 'as of' date.
3. Add a 'How to use an index in a bid' section with one worked example of adjusting a material price for escalation. Link tariff-aware-estimating-material-escalation-every-bid.
4. Link construction-cost-trends-2026 for why costs moved and tariff-impact-construction-costs-2026-steel-aluminum-copper for tariffs. Both stay separate under G07, so do not repeat their content.
5. At the first real data update, move the page to a URL without year or quarter, for example /blog/construction-cost-index/, with a 301 from the Q1 slug. Update the page recorded for L-124. After that, update the same URL each quarter with a dated 'What changed' note, and keep the sitemap lastmod equal to the real update date (A9).
6. When Quotr's Factory-Direct vs US Dealer Price Index launches (R-19, planned for December 2026, task C1), add a section comparing it with the public indexes. Until then, make no claims about Quotr prices.
7. Add a named author (A7). Add an in-house estimator as reviewer only if Quotr confirms one. One search summary names a 'Cost Estimator, Quotr.ai' on another post, but this is unconfirmed.

**Add to the page:**
- Table of the latest index values with release dates
- Answer-first block for L-124 with an 'as of' date
- Worked example of using an index in a bid
- Section linking Quotr's price index once R-19 is live

**Title:** The live title was not seen. Take the quarter out of the main title, for example 'Construction cost index tracker: PPI, RSMeans and Mortenson compared'. Show the latest quarter and 'Updated [date]' under the H1. Do not swap 'Q1' for 'Q3' without new data.  
**Web address (URL):** Move it to a URL without year or quarter, with a 301, at the next real data update (about October–November 2026). This follows the vault's rule that recurring pages get year-free URLs. Keep that URL for every later edition.

**Related tasks:** [[A7 Named author bylines and author pages|A7]], [[A9 Sitemaps and lastmod dates|A9]], [[C1 Publish the first original dataset|C1]]

**Why now:** Its Q1 2026 numbers are two quarters old, and Q3 closes on 2026-09-30. The next index releases are the natural moment to move to one living URL, before Quotr's own index launches in December.

## Overlaps with other Quotr posts

- **2026 construction cost trends** (buyer question: "Why did construction costs go up so much in 2026, and what are they doing now?"): competes with [[BP-03 construction cost trends 2026|BP-03]], [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps|BP-70]], [[BP-23 tariff impact construction costs 2026 steel aluminum copper|BP-23]]. Main page: [[BP-03 construction cost trends 2026]].

See the full map in [[Blog health audit#Posts that compete with each other]].

## Sources

- [[Website audit#8.6 Blog posts (all 96), grouped by cluster]] (2026-09-25 audit: sitemap date, cluster, notes)
- [[Blog health audit]] (method, limits and the overlap map)

## Log

- 2026-09-26: health record created by the blog health audit (Claude). Web search was limited, so check the live page before editing it.
