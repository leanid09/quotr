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
health: fair
health_score: 57
action: update
merge_into: ''
priority: medium
rank: 69
status: todo
---
# BP-92. Scope gap construction

> [!abstract] In one line
> A strong answer-first post by the CTO, with a worked example, let down by four unsourced statistics, a 404 link and mismatched dates. Fix the facts and keep it.

**Live page:** [Scope gap construction](https://quotr.ai/blog/scope-gap-construction/) *(title taken from the web address; the live title was not captured)*  
**Published:** 2026-09-10 · **Cluster:** Trade how-tos and fundamentals · **Format:** explainer · **Funnel:** TOFU

## What it covers

Not captured: the post did not come up in the web searches we could run. See the notes from the 2026-09-25 audit below.

**From the 2026-09-25 audit:** "Scope Gaps Cost More Than Pricing Errors"; Junzhe Shi byline; unsourced stats; broken link

## Health check

**Score: 57/100 (fair).** Each area is scored 0-5 using the rubric in [[Content refresh playbook]].

| Freshness | Accuracy | Trust | Structure | Visibility | Uniqueness |
|---|---|---|---|---|---|
| 3 | 2 | 3 | 4 | 1 | 4 |

- **Accuracy:** Four statistics have no source: change orders '8-14% of contract value', '80% ... trace to missing or poor information', '$177 billion a year', and rework 'around 5%'. *(from 2026-09-25 audit)*
- **Accuracy:** '$177 billion a year' is probably the 2018 FMI/PlanGrid estimate of US labour cost lost to non-productive time. It is not a rework or scope-gap cost. The vault style guide quotes the post as calling it rework. Find the primary source before keeping it. *(inferred)*
- **Accuracy:** The blog boilerplate says Quotr is 'based in San Francisco', while /disambiguation/ says Berkeley. The HQ city is TO CONFIRM (Q-01 is open). *(from 2026-09-25 audit)*
- **Trust:** Strong byline: 'By Junzhe Shi, PhD | CTO @Quotr.ai', the best credential signal seen on the blog. *(from 2026-09-25 audit)*
- **Trust:** An internal link to /blog/plug-number-estimating/ returns a 404. *(from 2026-09-25 audit)*
- **Freshness:** The sitemap lastmod is 2026-09-10, but the page says 'Last updated September 24, 2026'. The two dates disagree. *(from 2026-09-25 audit)*
- **Structure:** It opens answer-first ('The short version'). It has a worked $2M bid example, a 5-question FAQ and links to dictionary terms. *(from 2026-09-25 audit)*
- **Visibility:** It was not returned in 7 targeted searches, including a search for its exact title, 'Scope Gaps Cost More Than Pricing Errors'. Rival tools came back instead (PalCode, Provision, MeltPlan, Pelles, Procore and others). These searches were not re-run. *(seen in search 2026-09-26)*
- **Visibility:** It may simply be too new to be indexed. The sitemap date is 16 days old and the page was edited 2 days ago. *(inferred)*
- **Visibility:** For L-011, Perplexity answers cited Piper, Struvia, Meltplan and Exayard, not Quotr. *(from vault prompt library)*
- **Uniqueness:** It is the only Quotr blog post on scope gaps. /dictionary/scope-gap/ covers the same term in short glossary form, and the post links to it. *(from 2026-09-25 audit)*

## Search and AI visibility

- **Web search:** Not returned by 3-7 targeted web searches on 2026-09-26.
- **Cited in the September AI tests:** no.
- **Main buyer question it targets:** what is a scope gap in construction.
- **Buyer questions in the prompt library it serves:** [[L-011 what is a scope gap and how do I avoid it between trades|L-011]].

## What to do

**Action: Update** · **Priority:** medium · **Effort:** S · **Order in the refresh queue:** 69

1. Find a primary source for each of the four statistics and link it with its year, or delete the number. For '$177 billion', check the 2018 FMI/PlanGrid 'Construction Disconnected' report. If it measures non-productive labour time, describe it that way or drop it. Never call it a rework or scope-gap cost.
2. Change the /blog/plug-number-estimating/ link to /dictionary/plug-number/, and have the developer 301 the dead URL to the same place (A10).
3. Replace the 'based in San Francisco' boilerplate with the HQ approved in A1. Until Q-01 is answered, leave the city out.
4. Put 'Quotr.ai' inside the sentence that introduces the worked $2M bid example. Turn the example into a small table with three columns: scope item, which trade assumed it, cost of the gap.
5. Add a short 'Scope gaps by trade' checklist covering the common hand-offs (electrical and low-voltage, drywall and framing, HVAC and plumbing). The vault's R-33 plan already wants to reuse a scope-gap checklist from this post.
6. Cross-link this post to the inclusions/exclusions section of the how-to-bid guide and to /dictionary/scope-gap/, and link the dictionary term back here.
7. Make the on-page date, schema dateModified and sitemap lastmod all show the date of these real edits (A9). Then request indexing in Search Console and Bing, and re-run L-011 2-4 weeks later.

**Add to the page:**
- A primary-source link for each statistic, or remove it
- A scope-gap-by-trade checklist
- A table version of the $2M bid example, with Quotr.ai named in the lead sentence

**Title:** Keep the hook, but lead with the buyer's question. Suggested: 'What Is a Scope Gap? How to Avoid Gaps Between Trades' (53 characters). Use 'Scope gaps cost more than pricing errors' as the first line of the short answer.  
**Web address (URL):** Keep [[BP-92 scope gap construction|BP-92]] (/scope-gap-construction/). It has no year and matches the query.

**Related tasks:** [[A10 De-index the staging site; tidy legacy hosts and broken links|A10]], [[A9 Sitemaps and lastmod dates|A9]], [[A3 Fact-fix sweep, part 2 - every other conflicting fact|A3]], [[A1 Agree and sign off one fact sheet|A1]], [[A16 Add a human edit and fact-check step for AI-assisted drafts|A16]]

**Why now:** The post may not be indexed yet, so fixing it before Google's first full crawl costs nothing in rankings. The vault already lists these fixes as Tier 0. The 404 link and the statistics can be fixed now. Hold the date change and the indexing request until Google's September 2026 spam update ends (about 2026-10-08; RANK-21, seen in search 2026-09-26).

## Sources

- [[Website audit#8.6 Blog posts (all 96), grouped by cluster]] (2026-09-25 audit: sitemap date, cluster, notes)
- [[Blog health audit]] (method, limits and the overlap map)
- Web search results used: <https://palcode.ai/blog/scope-gap-construction-bids-find-missing-scope>, <https://provision.com/blog/scope-gaps-change-orders-cost-general-contractors>, <https://www.meltplan.com/blogs/how-scope-gaps-become-change-orders-a-gc-s-prevention-guide>, <https://www.pelles.ai/university/articles/scope-gaps-expensive-miss>, <https://www.procore.com/library/scope-gap>, <https://quotr.ai/blog/commercial-electrical-takeoff-drawings-to-proposal/>

## Log

- 2026-09-26: health record created by the blog health audit (Claude). Web search was limited, so check the live page before editing it.
