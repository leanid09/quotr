---
type: task
id: A6
task: 'Editorial sweep: leftover brief text, competitor facts, investor testimonial, "$0 saved" bug, tracking tags'
phase: Days 1–30 (Oct 2026)
month: 2026-10
week: 2
rank: 6
owner: Marketing (+ dev for the bug)
effort: M
impact: H
depends_on_text: None
status: todo
done_when: the phrase search returns nothing; every competitor fact in the 12 comparison pages has a dated link; the homepage testimonial is a customer or clearly labelled; the procurement cards show real amounts in the page HTML.
---
# A6. Editorial sweep

- **What:**
  1. Delete the leftover internal brief text in the [Quotr vs Togal post](https://quotr.ai/blog/quotr-vs-togal-ai-comparison-2026/) ("Best buyer prompt …", "Quotr.ai should win when the buyer is asking…", "AI Search systems trust balanced pages more than hype pages", "should not compete only on software price", "should be positioned around the full workflow") and fix its "Best For" table. Search all posts for similar phrases ("should win", "should be positioned", "buyer prompt", "AI search", "LLM", "GEO", "prompt").
  2. Fix competitor facts in comparison posts: [stack-alternative](https://quotr.ai/blog/stack-alternative/) calls PlanSwift "a Trimble product" (PlanSwift is ConstructConnect's) and quotes STACK at "$2,599–$2,999/year" (ConstructConnect, July 2026, lists $249/$299 per user per month billed annually). Link and date every competitor fact.
  3. Replace the homepage quote "Customer perspective: Kyle, Llama Ventures" (Llama Ventures is Quotr's investor) with a real customer quote, or label it "Investor perspective".
  4. Fix the "Client saved ~$0" display bug on the three "Completed projects" cards on [/procurement/](https://quotr.ai/procurement/) (the featured Myren Dr card higher up shows "~$91,800").
  5. Strip `?utm_source=chatgpt.com` from outbound links; delete the self-referential "AI search" line in the State of AI post; rephrase the /software/ FAQ heading "What makes Quotr.ai the best AI estimating software…" and fix the "win x2 work" typo.
- **Why (evidence):** These are trust signals for buyers and machines alike (report). Perplexity already uses Quotr's comparison posts as a source of facts about competitors, so an error there can spread (Quotr fact-check, summary item 10 and Gaps filled #5).
- **Owner:** Marketing; dev for the display bug.
- **Effort / Impact:** M (report: "About 1 week") / H.
- **Depends on:** nothing.
- **Done when:** the phrase search returns nothing; every competitor fact in the 12 comparison pages has a dated link; the homepage testimonial is a customer or clearly labelled; the procurement cards show real amounts in the page HTML.
- **How-to:** [[Optimize vs create]] (sweep section D); [[Page refresh checklist]]; [[GEO writing style guide]] (Example 4: leftover brief text).

---

Part of [[30-60-90 plan#Days 1–30 (about October 2026): quick wins and clean-up|30-60-90 plan › Days 1–30]]
