---
type: question
id: Q-54
question: 'One shared block for prices and facts: can prices, the "About Quotr.ai" text and other facts that change (turnaround, factory count, savings) come from one shared block or field in the blog''s content system, so one change updates every post at once?'
topic: H. Domains, profiles and technical setup
ask: Quotr
status: open
answer:
answered_on:
---
# Q-54 · One shared block for prices and facts

> [!question] Question for Quotr
> **One shared block for prices and facts:** can prices, the "About Quotr.ai" text and other facts that change (turnaround, factory count, savings) come from one shared block or field in the blog's content system, so one change updates every post at once?

**Why we ask:** prices seem to be typed into each post (inference), so 11 days after the September price change, many posts still seemed to show the old prices. See [[What went wrong#W-01 Old prices still showing after the September price change|W-01]] and [[Blog health audit]].

- **New pricing.** Live since 2026-09-14: Lite $79.90 and Plus $299.90 per seat per month, Enterprise custom ([[Entity fact sheet]]).
- **Old prices on posts.** On 2026-09-25, 13 to 16 posts still seemed to show the retired "Solo $299.90 / Team $499.90" tiers or "from $299.90". Only 2 were read on the live page. The rest were seen in search-index text and AI answers, which can lag.
- **AI answers.** Perplexity quoted the old entry price in 2 of 8 brand prompts (B4 and V2). The direct "Quotr.ai pricing" prompt gave the right prices.
- **Other facts.** Turnaround, factory count and savings also differ from page to page ([[Q-09 Factory network|Q-09]], [[Q-10 Savings|Q-10]], [[Q-15 Turnaround|Q-15]]). Once Quotr signs them off ([[A1 Agree and sign off one fact sheet|A1]]), a shared block keeps them in step.
- **Same idea as the schema.** The [[Schema markup kit]] already suggests one pricing component for the schema. The same works for the text.
- **Depends on the tool.** How the blog is edited is asked in [[Q-55 Who can edit the blog and add redirects|Q-55]].

## Answer

*When Quotr answers: put the short answer in the `answer` property, fill `answered_on`, set `status` to `answered`, and add a line to [[Changelog]]. If a shared block is possible, add it to the price-change routine in [[Content refresh playbook]].*

---

From [[Blog health audit]] · H. Domains, profiles and technical setup
