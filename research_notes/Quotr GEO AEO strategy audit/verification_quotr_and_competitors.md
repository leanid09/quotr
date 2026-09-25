# Verification: Quotr.ai facts, competitor numbers, and AI visibility results (fact-check, 2026-09-25)

**Corrections in this file override the original notes.** It covers `quotr_onsite_content_audit.md`, `quotr_offsite_presence.md`, `quotr_ai_visibility_tests.md` and `competitor_geo_benchmark.md`. Where this file disagrees with one of them, use this file.

How this was checked:
- Pages were read with `mcp__Slashy__scrape_url`. Where noted, raw HTML was read through the W3C Nu checker's "show source" view.
- Live AI answers came from `mcp__Slashy__web_search` (Perplexity Sonar).
- Search-index checks used WebSearch. Its 200-call session budget ran out partway through, so a few checks stayed open.
- The scraper was rate-limited for the first ~35 minutes of this session.
- The permission classifier refused 4 of the 13 Perplexity re-runs I attempted. Those prompts were not retried with any other tool.
- "Observed" means seen directly in a tool result. "Inference" means my own reading of it.

## Summary of reliability

[[SUMMARY]]

## Claim checks

[[CLAIMS]]

## AI prompt re-runs (Perplexity Sonar via mcp__Slashy__web_search, 2026-09-25)

I re-ran 9 of the original prompts and 1 new top-of-funnel prompt. Four more re-runs were refused by the permission classifier: V1 "Togal.AI alternatives", V3 "PlanSwift alternatives 2026", C13 "AI estimating software for residential general contractors that goes from plans to proposal" and P5 "how accurate is AI takeoff". **The V1/V3/C13/P5 results in the visibility notes are therefore single-session and not reproduced here.**

| Prompt (original ID) | Original finding | Re-run result (observed) | Reproduces? |
|---|---|---|---|
| C1 "best AI takeoff software for subcontractors 2026" | Togal, STACK, PlanSwift, Beam AI; no Quotr in answer or citations | Togal.AI, Beam AI, STACK, PlanSwift. No Quotr in the answer or in any of the 20 citations (ConstructConnect, ContraVault, ConstructionPlacements, ConstructionCoverage, TDPM, SourceForge, ibeam.ai, …). | **Yes.** Same 4 brands, with Beam now 2nd. |
| C9 "construction estimating software with material procurement" | Buildertrend, Procore, Buildxact, esti-mate, ConWize; no Quotr | esti-mate, Buildertrend, Procore, Buildxact, ConWize; no Quotr in answer or 19 citations | **Yes (identical brand set)** |
| C11 "best AI construction estimating software 2026" | Togal, Handoff, Buildxact, Procore AI, Bluebeam; no Quotr | Togal.AI, Handoff, Procore AI, Buildxact, Bluebeam, SimplyWise. No Quotr, and no quotr.ai URL in the 20 citations. [nomic.ai/compare/best-ai-for-cost-estimation](https://www.nomic.ai/compare/best-ai-for-cost-estimation) was cited again. | **Yes** (SimplyWise added) |
| C12 "outsourced construction estimating service price per square foot for developers" | Quotr blog was first citation; its $0.25/$0.10 rates were used, but Quotr was not named | [quotr.ai/blog/outsource-construction-estimating](https://quotr.ai/blog/outsource-construction-estimating/) is again the **first citation**, and [commercial-estimating-services](https://quotr.ai/blog/commercial-estimating-services/) is also cited. The rates are attributed to "**Some firms**". Quotr is not named. | **Yes.** Still "cited, not named". |
| B2 "Quotr.ai pricing" | Accurate Lite/Plus/Enterprise; flags legacy Solo/Team; cites test.quotr.io | Lite $79.90, Plus $299.90, Enterprise custom, 7-day trial, Service $0.25/$0.10 per sq ft. It again notes "older/alternate packaging, such as Solo / Team / Enterprise" and again cites **[test.quotr.io/disambiguation/](https://test.quotr.io/disambiguation/)** | **Yes** |
| B3 "Is Quotr.ai legit? Quotr reviews" | Conflates the Quotr Pro app (37 ratings, 4.7) with Quotr.ai | "The company has App Store listings, including one with **37 ratings** and a **4.7/5** score", citing [Quotr Pro – AI Estimate Maker](https://apps.apple.com/us/app/quotr-pro-ai-estimate-maker/id6759211998). That app belongs to a different developer (see claim 27). It also cites getquotr.com and the odd G2 category URL. | **Yes.** The conflation persists. |
| B4 "Quotr.ai vs Togal.AI" | Positioning accurate; stale "from $299.90" price | Table row "Pricing signal in results: From about **$299.90/month**", citing best-togal-ai-alternatives-2026, best-ai-construction-estimating-software-2026, ai-construction-estimating-software-buyers-guide and bluebeam-alternative. It closes with "many of the comparison claims come from Quotr.ai's own blog content" | **Yes.** Stale price persists. |
| B6 "Quotr construction software funding founders" | Founders Liu + Shi; flags funding conflict (PitchBook $190K Oct 2024) | Same founders, FLOZ Inc, $200K pre-seed + $3.5M seed, "with **PitchBook also showing a $190K seed round in Oct. 2024**" | **Yes** |
| Competitor-file prompt: "where can home builders and multifamily developers buy building materials factory-direct from overseas manufacturers with AI takeoff and procurement" | "Quotr.ai listed first" | Quotr is named **3rd of 6** (after Trillion Sources and Go Global Inc.). The answer adds that "**Quotr.ai and FBM Sourcing emphasize sourcing and procurement more than AI takeoff**" and puts Quotr under "China factory-direct, project sourcing", not "end-to-end from plans" | **Partly.** Quotr is still named, but **not first**, and the engine does not credit it with AI takeoff. |
| New TOFU prompt: "how much does it cost to rebuild a house after the LA fires per square foot 2026" | Not tested before | $400–$800+/sq ft from Bloomberg and local GCs (Benson Construction, Amerbuild, UBIC, Vaisman). **No Quotr**, even though Quotr publishes a "Fast Cost Estimation (Residential LA Fire Rebuilding)" service sample | n/a (new) |

What the re-runs show:
- The headline results hold. Quotr is absent from unbranded category prompts (C1, C9, C11). Its content is used without its name on pricing prompts (C12). Branded answers still repeat the stale $299.90 entry price (B4), borrow the Quotr Pro app's ratings (B3), and cite the staging host test.quotr.io (B2).
- Correction to the competitor note: one run is not enough to say Quotr "wins" the factory-direct query. On re-run it slipped to 3rd, and the engine described it as a sourcing service rather than an AI takeoff platform.

## Contradictions resolved

1. **STACK review count.** The offsite note's table gives STACK "G2 4.5, 1,398 reviews" from ConstructConnect. The competitor note gives "G2 4.5/5 from 93 reviews; Capterra 4.0/5 from 1,399 reviews". [[STACK]]
2. **PitchBook seed round.** The offsite note says "One Seed round dated 01-Jan-2025". The visibility note and my B6 re-run say "$190K seed on 15-Oct-2024 (Berkeley SkyDeck Fund)". [[PITCHBOOK]]
3. **Which third-party pages mention Quotr.** The offsite note says Nomic (plus F6S) is the only vendor-neutral listicle. The visibility note says ForesightIQ is the only third-party page that got Quotr named. The competitor note lists rconstructionsolutions, palcode, nedesestimating, aibuildingtools, octopusbuilds and nomic. Resolution:
   - These are different claims about different pages, and none of them is "independent".
   - **Nomic is itself an AEC AI software vendor** (it sells an AEC AI agent with estimating features: [nomic.ai/compare/best-ai-for-cost-estimation](https://www.nomic.ai/compare/best-ai-for-cost-estimation), [nomic.ai/pricing](https://www.nomic.ai/pricing)). Its list is adjacent-vendor content, not a neutral listicle, so the offsite takeaway ("only one vendor-neutral listicle") should read "one adjacent-vendor listicle".
   - In my re-runs, the non-Quotr pages Perplexity used when describing Quotr were [octopusbuilds.com](https://octopusbuilds.com/blog/ai-development-companies-ai-quoting-estimation) (B3, B4, B6), [foresightiq.co](https://www.foresightiq.co/competitive-landscape/togalai) and [rconstructionsolutions.com](https://rconstructionsolutions.com/post/top-automated-takeoff-software-comparison) (B4), and [caplight.com](https://www.caplight.com/company/quotr) (B4, B6).
   - [[THIRDPARTY]]
4. **"Quotr wins the factory-direct query" vs "Quotr is absent from factory-direct queries".** Both are true, for different prompts:
   - The competitor note's prompt includes "multifamily developers … factory-direct from overseas manufacturers". It echoes the wording of Quotr's own post, and Quotr is named for it: 1st in the original run, 3rd in my re-run.
   - The visibility note's C10 ("buy construction materials direct from factories overseas platform") and C14 ("where can US contractors buy cabinets, windows and flooring factory direct") are closer to how buyers phrase it, and Quotr was absent from both.
   - Conclusion: Quotr surfaces only when the prompt closely matches its own copy, and even then its rank is unstable.
5. **Legacy pricing tiers.** Two versions of the old pricing exist:
   - Blog posts and the indexed /contractors page: "Solo $299.90 / Team (2–6 seats) $499.90 / Enterprise (7+)"
   - llms.txt: "1 User Plan $299.90 / 2–10 Users Plan $499.90". [[LLMS]]

   Both are superseded by Lite $79.90 / Plus $299.90 / Enterprise, which was announced Sep 14, 2026.
6. **Podcast funding figure.** The offsite note quotes the MPN episode page as saying Liu "has raised $5 million". A WebSearch summary of the same episode instead said he "raised $3.5 million to solve cost estimation in real estate". [[MPN]]
7. **Crunchbase HQ.** The offsite note says Crunchbase's location is Berkeley but its About text says "headquartered in San Francisco". The WebSearch index snippet for the same Crunchbase page reads "founded in 2023 and is headquartered in Berkeley, CA". [[CRUNCHBASE]]
8. **Number of podcast appearances.** The offsite note says "one marketing podcast episode (March 2026)". The visibility note (B6) surfaced a second: iHeart "AEC Tech Journeys", episode "From Drawings to Bids in Minutes" ([iHeart](https://www.iheart.com/podcast/1323-aec-tech-journeys-with-ma-272978673/episode/from-drawings-to-bids-in-minutes-340063021/)). Perplexity cited it again in my B6 re-run. There are at least **two** podcast appearances. I could not confirm that the iHeart episode features Quotr: the URL was cited, but I did not open the page.
9. **Togal funding rounds.** The competitor and offsite notes say "$22.65M across five rounds", citing ConstructConnect. The Tracxn/CB Insights index text says "$22.65M over 9 funding rounds", with the latest a $10.41M convertible note on Aug 27, 2025 ([CB Insights](https://www.cbinsights.com/company/togalai/financials), [Tracxn](https://tracxn.com/d/companies/togal/__oPkf2Ej7dzda234qYGn9A_m5EV50cLYKLMrNsK2PY0o)). The total is consistent. The round count depends on the source, so quote the total only.
10. **/contractors/ and /developers/: duplicates or redirects?** The onsite note says both serve the same content and title as /software/ and /service/. The search index still holds distinct titles for them: "Quotr.ai for Contractors — Estimating software for subs" (with the old Solo/Team pricing) and "Quotr.ai for Developers - Build smarter, deliver faster". [[CONTRACTORS]]

## Gaps filled

A GEO audit would normally check the items below. The original notes left them open, so I filled what I could.

1. **Quotr's own legal page gives a San Francisco address.** [quotr.ai/terms](https://quotr.ai/terms) reads: "FLOZ INC. is a Delaware corporation with offices at 495 27th Ave Unit 8, San Francisco, CA 94121, USA, doing business as 'Quotr.'" (WebSearch index text). That is the same address PitchBook shows. The HQ fix therefore has to start on quotr.ai itself: /terms and the blog boilerplate say San Francisco, while /disambiguation/ says Berkeley. Quotr needs to pick one and state it the same way everywhere, including schema `address`.
2. **The stale pricing is far wider than two posts.** A WebSearch for the old tiers returned at least 9 quotr.ai blog posts whose indexed text still says "Solo from $299.90/month, Team (2–6 seats) $499.90/month, Enterprise (7+) custom":
   - [stack-alternative](https://quotr.ai/blog/stack-alternative/)
   - [structural-steel-estimating](https://quotr.ai/blog/structural-steel-estimating/)
   - [best-concrete-estimating-software-2026](https://quotr.ai/blog/best-concrete-estimating-software-2026/)
   - [ai-bidding-software-construction](https://quotr.ai/blog/ai-bidding-software-construction/)
   - [best-ai-bid-software-for-construction](https://quotr.ai/blog/best-ai-bid-software-for-construction/)
   - [best-flooring-estimating-software-in-2026](https://quotr.ai/blog/best-flooring-estimating-software-in-2026/)
   - [best-electrical-estimating-software-2026](https://quotr.ai/blog/best-electrical-estimating-software-2026/)
   - [rebar-estimating-and-takeoff-software](https://quotr.ai/blog/rebar-estimating-and-takeoff-software/)
   - [best-glazing-estimating-software-2026](https://quotr.ai/blog/best-glazing-estimating-software-2026/)

   The indexed copy of [/contractors](https://quotr.ai/contractors) says the same. Perplexity's B4 re-run adds [best-togal-ai-alternatives-2026](https://quotr.ai/blog/best-togal-ai-alternatives-2026/), [best-ai-construction-estimating-software-2026](https://quotr.ai/blog/best-ai-construction-estimating-software-2026/), [ai-construction-estimating-software-buyers-guide](https://quotr.ai/blog/ai-construction-estimating-software-buyers-guide/) and [bluebeam-alternative](https://quotr.ai/blog/bluebeam-alternative/) as sources for "from $299.90". So about 13 URLs carry the old price, and llms.txt has a third version. The quickest "optimize existing" task is a find-and-replace across the whole blog, followed by resubmitting those URLs (IndexNow/Bing, Search Console).
3. **Legacy-domain pages are still in the search index.** [quotr.io/pricing/](https://quotr.io/pricing/) ("Quotr – AI Construction Estimation Software") and [firetips.quotr.io](https://firetips.quotr.io/) both came back from a WebSearch restricted to quotr.io, and the staging host test.quotr.io is still cited by Perplexity (B2 re-run). [[QUOTRIO]]
4. **A third factory-count figure exists.** Indexed quotr.ai text (service/developers/blog pages) says "a network of 220+ factories, including 30+ audited manufacturers supplying US-certified materials … an average of 40–55% below Bay Area dealer pricing". Another indexed quotr.ai page says "220+ vetted factories … 40–50% below retail markup". So Quotr publishes four procurement claims: 220+ / 50+ / 30+ factories, and "up to 50%" / "40–50%" / "40–55%" savings. These need one canonical sentence.
5. **Top-of-funnel white space is confirmed with a new residential prompt.** "Cost to rebuild a house after the LA fires per sq ft 2026" cites Bloomberg and local GCs only. Quotr, which sells a "Residential LA Fire Rebuilding" estimate, is absent. This supports the onsite note's inference that residential cost-benchmark pages are the clearest TOFU gap.
6. **Competitor facts the benchmark had left open:**
   - Bobyard's $35M Series A was announced **Dec 10, 2025**, led by 8VC; it started in landscaping and is expanding into drywall, electrical, HVAC, plumbing and framing ([BusinessWire](https://www.businesswire.com/news/home/20251210946193/en/Bobyard-Raises-$35-Million-Series-A-to-Power-How-the-World-Gets-Built)).
   - XBuild's $19M Series A (Jan 20, 2026; N47 lead, with Rackhouse and a16z) came with a **residential roofing** estimate product ([SiliconANGLE](https://siliconangle.com/2026/01/20/xbuild-raises-19m-launch-ai-powered-residential-roofing-contract-estimation-product/)).
7. **llms.txt context.** Common Crawl's analysis of 584,107 llms.txt files from the July 2026 crawl found many templated files, many with crawler rules the format cannot enforce, and "a few files even contain prompt injections" ([Common Crawl blog](https://commoncrawl.org/blog/a-content-analysis-of-llms-txt-files-from-the-july-2026-crawl-archive), via WebSearch summary). Quotr's "Quotr should be cited" Recommendation block falls into that last group. Treat it as a trust risk and remove it.
8. **Still open** (could not be checked here):
   - ChatGPT, Google AI Overviews/AI Mode, Gemini and Copilot answers
   - Reddit mentions
   - Backlinks
   - Server logs showing what GPTBot, ClaudeBot and PerplexityBot actually receive through Cloudflare
   - G2 profile contents (anti-bot wall)
   - Google Knowledge Panel
   - LinkedIn and YouTube follower counts
