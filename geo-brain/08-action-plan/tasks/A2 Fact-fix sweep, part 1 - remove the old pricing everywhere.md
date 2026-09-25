---
type: task
id: A2
task: 'Fact-fix sweep, part 1: remove old pricing (~13 URLs, /contractors copy, llms.txt), re-crawl, correction emails'
phase: Days 1–30 (Oct 2026)
month: 2026-10
week: 2
rank: 2
owner: Marketing (+ dev)
effort: S
impact: H
depends_on_text: None (price is already confirmed)
status: todo
done_when: the search terms above return no quotr.ai page (the correct "Plus $299.90" is fine); re-crawl requested for every changed URL; both correction emails sent. About 4 weeks later, the branded price prompts quote $79.90 (our expectation; engines re-read pages at different speeds).
---
# A2. Fact-fix sweep, part 1: remove the old pricing everywhere

- **What:** Replace the retired "Solo $299.90 / Team (2–6 seats) $499.90 / Enterprise (7+)" pricing on about 13 quotr.ai URLs, the old indexed copy of /contractors/ and [llms.txt](https://quotr.ai/llms.txt) ("1 User Plan $299.90 / 2–10 Users Plan $499.90"). Known URLs include [stack-alternative](https://quotr.ai/blog/stack-alternative/) (also its FAQ line "cheaper entry point at $299.90/month"), [best-togal-ai-alternatives-2026](https://quotr.ai/blog/best-togal-ai-alternatives-2026/), [structural-steel-estimating](https://quotr.ai/blog/structural-steel-estimating/), [best-concrete-estimating-software-2026](https://quotr.ai/blog/best-concrete-estimating-software-2026/), [ai-bidding-software-construction](https://quotr.ai/blog/ai-bidding-software-construction/), [best-ai-bid-software-for-construction](https://quotr.ai/blog/best-ai-bid-software-for-construction/), [best-flooring-estimating-software-in-2026](https://quotr.ai/blog/best-flooring-estimating-software-in-2026/), [best-electrical-estimating-software-2026](https://quotr.ai/blog/best-electrical-estimating-software-2026/), [rebar-estimating-and-takeoff-software](https://quotr.ai/blog/rebar-estimating-and-takeoff-software/), [best-glazing-estimating-software-2026](https://quotr.ai/blog/best-glazing-estimating-software-2026/), [best-ai-construction-estimating-software-2026](https://quotr.ai/blog/best-ai-construction-estimating-software-2026/), the [buyer's guide](https://quotr.ai/blog/ai-construction-estimating-software-buyers-guide/) and [bluebeam-alternative](https://quotr.ai/blog/bluebeam-alternative/). Then search all 96 posts for `Solo`, `Team (2`, `$499.90`, `1 User Plan`, `2–10 Users`, `$249/seat`, `$41/seat`, `from $299.90`, `starts at $299.90`. Request re-crawls in Google Search Console and Bing Webmaster Tools (or IndexNow). Email [Nomic](https://www.nomic.ai/compare/kreo-alternatives) and [Octopus Builds](https://octopusbuilds.com/blog/ai-development-companies-ai-quoting-estimation), which copied the old price.
- **Why (evidence):** Asked "Quotr.ai vs Togal.AI", Perplexity said Quotr starts "from about $299.90/month", on the original run and on the fact-check re-run. The real entry price is $79.90, so AI quotes nearly four times too much (report; verification file, claim 7 and re-run B4).
- **Owner:** Marketing (edits and emails); dev only if the CMS needs it.
- **Effort / Impact:** S (report: "Marketing, 1–2 days") / H.
- **Depends on:** nothing. The current prices are already confirmed on [/pricing/](https://quotr.ai/pricing/). Write "Quotr.ai Lite", because Kreo also sells plans called Lite and Plus.
- **Done when:** the search terms above return no quotr.ai page (the correct "Plus $299.90" is fine); re-crawl requested for every changed URL; both correction emails sent. About 4 weeks later, the branded price prompts quote $79.90 (our expectation; engines re-read pages at different speeds).
- **How-to:** [[Optimize vs create]] (fact-fix sweep, row 1); [[Pricing page template]] §5; re-crawl steps in [[Tracking setup]] §3.5; correction email in [[Listicle and PR outreach]] §5b.

---

Part of [[30-60-90 plan#Days 1–30 (about October 2026): quick wins and clean-up|30-60-90 plan › Days 1–30]]
