---
type: article
id: BP-92
title: Scope gap construction
quotr_url: https://quotr.ai/blog/scope-gap-construction/
published: 2026-09-10
month: 2026-09
date_note: Blog sitemap date, used as the publish date
cluster: Trade how-tos and fundamentals
format: explainer
funnel:
- TOFU
persona:
- subcontractor
- general contractor
- estimator
trade:
- multi-trade
byline: unknown
primary_query: what is a scope gap in construction
target_prompts:
- '[[L-011 what is a scope gap and how do I avoid it between trades|L-011]]'
web_indexed: 'no'
search_check: Not returned by 3-7 targeted web searches on 2026-09-26
ai_cited: false
cited_in: []
old_pricing: unknown
flags:
- broken link
- date mismatch
- named author
- not in web search
- unsourced stats
health: poor
health_score: 53
action: update
merge_into: ''
priority: medium
rank: 63
status: todo
---
# BP-92. Scope gap construction

> [!abstract] In one line
> A strong answer-first post by the CTO, with a worked example. Four unsourced statistics, an unconfirmed HQ city, a 404 link and mismatched dates let it down. Fix the facts and keep it.

**Live page:** [Scope gap construction](https://quotr.ai/blog/scope-gap-construction/) *(title taken from the web address; the live title was not captured)*  
**Published:** 2026-09-10 · **Cluster:** Trade how-tos and fundamentals · **Format:** explainer · **Funnel:** TOFU

## What it covers

Not captured: the post did not come up in the web searches we could run. See the notes from the 2026-09-25 audit below.

**From the 2026-09-25 audit:** "Scope Gaps Cost More Than Pricing Errors"; Junzhe Shi byline; unsourced stats; broken link

## Health check

**Score: 53/100 (poor).** Each area is scored 0-5 using the rubric in [[Content refresh playbook]].

| Freshness | Accuracy | Trust | Structure | Visibility | Uniqueness |
|---|---|---|---|---|---|
| 3 | 1 | 3 | 4 | 1 | 4 |

- **Accuracy:** Four statistics have no source: change orders '8-14% of contract value', '80% ... trace to missing or poor information', '$177 billion a year', and rework 'around 5%'. *(from 2026-09-25 audit)*
- **Accuracy:** '$177 billion a year' probably comes from the 2018 FMI/PlanGrid estimate of US labour cost lost to non-productive time. That is not a rework or scope-gap cost. The vault style guide shows the sentence as 'rework costs the industry $177 billion a year'. If that is the post's wording, the figure is mislabelled. Find the primary source before keeping it. *(inferred)*
- **Accuracy:** The blog boilerplate on this post says Quotr is 'based in San Francisco', but /disambiguation/ says Berkeley. The HQ city is TO CONFIRM (Q-01 is open), so the post states an unconfirmed Quotr fact as true. Because two Quotr pages conflict, accuracy is scored 1. *(from 2026-09-25 audit)*
- **Trust:** Strong byline: 'By Junzhe Shi, PhD | CTO @Quotr.ai', the best credential signal seen on the blog. *(from 2026-09-25 audit)*
- **Trust:** An internal link to /blog/plug-number-estimating/ returns a 404. *(from 2026-09-25 audit)*
- **Freshness:** The sitemap lastmod is 2026-09-10, but the page says 'Last updated September 24, 2026'. The two dates disagree. *(from 2026-09-25 audit)*
- **Structure:** It opens answer-first ('The short version'). It has a worked $2M bid example, a 5-question FAQ and links to dictionary terms. *(from 2026-09-25 audit)*
- **Visibility:** It was not returned in 7 targeted searches, including one for its exact title, 'Scope Gaps Cost More Than Pricing Errors'. Rival tools came back instead (PalCode, Provision, MeltPlan, Pelles, Procore and others). This was one pass and was not re-run. *(seen in search 2026-09-26)*
- **Visibility:** It may simply be too new to be indexed. The sitemap date is 16 days old and the page was edited 2 days ago. *(inferred)*
- **Visibility:** Its prompt L-011 is Medium priority and not tracked. When Perplexity answered it, the answers cited Piper, Struvia, Meltplan and Exayard, not Quotr. *(from vault prompt library)*
- **Uniqueness:** It is the only Quotr blog post on scope gaps. /dictionary/scope-gap/ covers the same term in short glossary form, and the post links to it. *(from 2026-09-25 audit)*

## Search and AI visibility

- **Web search:** Not returned by 3-7 targeted web searches on 2026-09-26.
- **Cited in the September AI tests:** no.
- **Main buyer question it targets:** what is a scope gap in construction.
- **Buyer questions in the prompt library it serves:** [[L-011 what is a scope gap and how do I avoid it between trades|L-011]].

## What to do

**Action: Update** · **Priority:** medium · **Effort:** S · **Order in the refresh queue:** 63

1. Ask Quotr where the four statistics came from (Q-58 is open). For each one, link a primary source with its year, or delete it. For '$177 billion', check the 2018 FMI/PlanGrid 'Construction Disconnected' report. If it measures non-productive labour time, say that or drop it. Never call it a rework or scope-gap cost.
2. Change the /blog/plug-number-estimating/ link to /dictionary/plug-number/. Have the developer 301 the dead URL to the same place (A10).
3. Take 'based in San Francisco' out of the boilerplate until Q-01 is answered and A1 approves one HQ city. Then use that city on every page (A3).
4. Turn the worked $2M bid example into a small table with three columns: scope item, which trade assumed it, cost of the gap. In the lead sentence, name Quotr.ai and say whether this is a real Quotr.ai estimate or an illustration.
5. If the post has no checklist yet, add a short 'Scope gaps by trade' checklist for the common hand-offs (electrical and low-voltage, drywall and framing, HVAC and plumbing). R-33 (January 2027) plans to reuse a scope-gap checklist from this post, so build it once, here.
6. Cross-link this post with the inclusions/exclusions section of the how-to-bid guide. Link /dictionary/scope-gap/ back to this post as the full answer for L-011.
7. Once the edits are live, make the on-page date, schema dateModified and sitemap lastmod all show the same real edit date (A9). Request indexing in Search Console and Bing, and re-run L-011 in Perplexity 2-4 weeks later.

**Add to the page:**
- A primary-source link for each statistic, or remove it
- A scope-gaps-by-trade checklist that R-33 can reuse
- A table version of the $2M bid example, labelled as real or illustrative, with Quotr.ai named in the lead sentence

**Title:** Keep the hook, but lead with the buyer's question. Suggested: 'What Is a Scope Gap? How to Avoid Gaps Between Trades' (53 characters). Use 'Scope gaps cost more than pricing errors' as the first line of the short answer.  
**Web address (URL):** Keep [[BP-92 scope gap construction|BP-92]] (/scope-gap-construction/). It has no year and matches the query.

**Related tasks:** [[A10 De-index the staging site; tidy legacy hosts and broken links|A10]], [[A9 Sitemaps and lastmod dates|A9]], [[A3 Fact-fix sweep, part 2 - every other conflicting fact|A3]], [[A1 Agree and sign off one fact sheet|A1]], [[A16 Add a human edit and fact-check step for AI-assisted drafts|A16]]

**Why now:** The vault already lists these fixes as Tier 0 and P1, and they take days, not weeks. The post may not be indexed yet (inferred), so fixing it before a full crawl costs nothing in rankings. Fix the 404 link, the statistics and the HQ line now. Hold the date change and the indexing request until Google's September 2026 spam update ends (about 2026-10-08; RANK-21, seen in search 2026-09-26, not re-checked).

## Sources

- [[Website audit#8.6 Blog posts (all 96), grouped by cluster]] (2026-09-25 audit: sitemap date, cluster, notes)
- [[Blog health audit]] (method, limits and the overlap map)
- Web search results used: <https://palcode.ai/blog/scope-gap-construction-bids-find-missing-scope>, <https://provision.com/blog/scope-gaps-change-orders-cost-general-contractors>, <https://www.meltplan.com/blogs/how-scope-gaps-become-change-orders-a-gc-s-prevention-guide>, <https://www.pelles.ai/university/articles/scope-gaps-expensive-miss>, <https://www.procore.com/library/scope-gap>, <https://quotr.ai/blog/commercial-electrical-takeoff-drawings-to-proposal/>

## Log

- 2026-09-26: health record created by the blog health audit (Claude). Web search was limited, so check the live page before editing it.
