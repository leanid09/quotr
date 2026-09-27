---
type: page-template
description: FAQ-section template plus a bank of approved Quotr answers built only from confirmed facts.
last_verified: 2026-09-25
verify_every_days: 180
---
# Template: FAQ Block (plus a Bank of Approved Quotr.ai Answers)

> [!abstract] What this page is for
> How to write the FAQ section that sits at the end of a Quotr.ai page, and a ready-to-use bank of FAQ answers about Quotr.ai built only from confirmed facts, with the questions that still need Quotr's confirmation clearly marked.

> [!info]- Sources
> [[Entity fact sheet]] and [[Products and features]] (all answers); [[quotr_onsite_content_audit]] (§3 FAQ findings, §5 inconsistencies), [[verification_quotr_and_competitors]] (claims 6, 30; re-runs B2–B4), [[geo_content_playbook_b2b]] (§2 Gaps: no controlled FAQ study), [[geo_ai_citation_signals_2026]] (§1 Microsoft guidance); [SEJ: Google drops FAQ rich results (2026)](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/); [[Prompt library]] (Stage 3 brand prompts).

---

## 1. Why FAQ blocks, and what they will not do

- **Why:** an FAQ answers the follow-up questions buyers ask AI tools ("does it have a free trial?", "is it the same as Quotr.io?") in short, self-contained passages. Microsoft's guidance for Copilot recommends question-style headings and direct answers (`geo_ai_citation_signals_2026.md` §1).
- **Quotr already uses them:** /software/ (8 questions), /service/ (9), /procurement/ (6), /faq/ (6), and many blog posts (onsite audit §3).
- **What they will not do:**
  - No controlled study shows that adding an FAQ block, or FAQ schema, raises AI citations; the claims seen were agency anecdotes (`geo_content_playbook_b2b.md` §2 Gaps).
  - Google stopped showing FAQ rich results on **May 7, 2026** ([SEJ](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/)). FAQ schema no longer changes how the page looks in Google.
- **So:** write FAQs because they help readers and state facts clearly; keep them accurate; do not expect a ranking or citation jump from them alone.

---

## 2. Rules for writing an FAQ block

1. **4–8 questions per page.** Pick from the [[Prompt library|prompt library]] and from real sales and support questions. No keyword lists.
2. **Question = the buyer's words** ("Does Quotr work on Mac?", not "Platform compatibility").
3. **First sentence answers the question** ("Yes." / "No." / "$79.90 per seat per month."). Then 1–3 sentences of detail.
4. **40–90 words per answer.** If it needs more, it deserves its own section or page; link to it.
5. **Put "Quotr.ai" in the answer**, not just in the question, so a quoted answer carries the brand.
6. **Numbers with dates** for anything that changes (prices, counts).
7. **No duplicate FAQ blocks** across many pages. The pricing questions live on /pricing/ and /software/; blog posts link there.
8. **Visible in the HTML.** An accordion is fine if the text is in the page source.
9. **Schema (optional):** FAQPage markup must copy the visible text exactly ([[Schema markup kit]] 5.4).
10. **Review the bank below whenever the fact sheet changes.**

**Answer pattern:**
> **Q: [Buyer's question]?**
> [Direct answer in one sentence, with "Quotr.ai" and a number/date if relevant.] [One or two sentences of detail.] [Link to the page with more.]

---

## 3. Approved answer bank (confirmed facts only)

These answers use only High-confidence facts from the fact sheet as of 2026-09-25. **Re-check prices on /pricing/ before each use.**

| Prompt ID | Question | Approved answer |
|---|---|---|
| D-001 | What is Quotr.ai? | Quotr.ai is AI construction takeoff, estimating and bid software, with a done-for-you estimating service (Quotr Service) and factory-direct material procurement (Quotr Procurement). Contractors upload PDF or image plan sets; the AI counts symbols, measures lengths and calculates areas, and the quantities flow into estimates, bid comparisons and proposals. |
| D-006 | Is Quotr.io the same company as Quotr.ai? | Yes. Quotr.ai was formerly called Quotr.io. It is the same product and company, built by FLOZ Inc. The current website is quotr.ai. |
| D-020 | Is Quotr Pro the same as Quotr.ai? | No. Quotr Pro is a separate app from a different developer (website quotr.pro). Quotr.ai is not related to it, and Quotr Pro's app-store ratings are not Quotr.ai ratings. |
| D-005 | Who owns Quotr.ai? | Quotr.ai is built by FLOZ Inc., a Delaware corporation. It was co-founded by Hanyang Liu (CEO), who trained as an architect, and Junzhe Shi, PhD (CTO), who built algorithms at Apple and UC Berkeley. Quotr.ai is a Berkeley SkyDeck Batch 19 company. |
| D-008 / D-009 | How much does Quotr.ai cost? | As of September 2026, Quotr.ai costs $79.90 per seat per month on the Lite plan and $299.90 per seat per month on the Plus plan. Enterprise pricing is custom. Every plan includes AI takeoff, with no setup fee. See [quotr.ai/pricing](https://quotr.ai/pricing/). |
| D-010 | Does Quotr.ai have a free trial? | Yes. Quotr.ai offers a 7-day free trial, and you can cancel anytime with no charge if you cancel during the trial. |
| D-011 | What is the difference between Quotr.ai Lite and Plus? | Quotr.ai Lite ($79.90 per seat per month) includes a basic AI agent, on-screen takeoff tools, AI symbol detection, area detection and a custom database. Quotr.ai Plus ($299.90 per seat per month) adds advanced AI, the full Quotr database, 2 hours of guided onboarding, project sharing, 2,000 sq ft of takeoff credits per month and 10% off procurement. |
| D-012 | How much does Quotr's estimating service cost? | Quotr.ai's Estimation Service (Quotr Service) charges $0.25 per square foot for projects under 50,000 sq ft and $0.10 per square foot for projects of 50,000 sq ft and above. Quotr sends the price before it starts work on your documents. |
| D-039 | Is procurement required to use Quotr.ai? | No. Procurement is fully optional. You can run takeoffs, estimates, and proposals without ever using it — or use Quotr.ai to send quote requests to your own suppliers and compare bids side by side. *(This is the live /software/ FAQ text.)* |
| D-034 (partial) | Which trades does Quotr.ai support? | Quotr.ai has trade workflows for 23 trades, including electrical, plumbing, HVAC, drywall, framing, concrete, flooring, roofing, painting, insulation, tile, glazing, structural steel, masonry and millwork. *(Add the "26 sub-trades" covered by Quotr Service only after Quotr explains the difference.)* |
| — | What does Quotr.ai's AI Agent do? | The Quotr.ai AI Agent reads your plans and answers plain-English questions about them, such as symbol counts, room dimensions and openings. It is included on every plan (basic on Lite, advanced on Plus). |
| — | Can I use my own prices in Quotr.ai? | Yes. Quotr.ai lets you price takeoffs with your own cost database or with Quotr's database of material, labour and assembly rates, and apply your own markups per project. The full Quotr database is included on the Plus plan. |
| D-048 (partial) | Does Quotr Procurement really save money? | Quotr reports project examples on its procurement page. For example, for a project on Myren Dr in Saratoga, California, Quotr reports a materials price of $97,000 against a Bay Area market price of $187,000–$218,000. Results vary by project and material. *(Do not add a general savings percentage until Quotr confirms one.)* |

---

## 4. Questions that need Quotr's confirmation first

Do **not** publish answers to these until Quotr confirms the facts (see the fact sheet's open questions). Draft placeholders are given so the team knows what is needed.

| Prompt ID | Question | What is unclear | Placeholder |
|---|---|---|---|
| D-013 | Does Quotr.ai offer annual pricing? | No annual price on /pricing/ | [TO CONFIRM: annual rates for Lite and Plus] |
| D-035 | Does Quotr work on Mac? | "Runs in any modern browser … no desktop install" seen only in search-index text | [TO CONFIRM: browser-based on Windows and macOS?] |
| D-036 | What file types does Quotr.ai accept? | PDF and images confirmed; DWG and Revit only in some indexed pages | [TO CONFIRM: PDF, images, DWG, Revit?] |
| D-037 | Does Quotr integrate with Procore or QuickBooks? | /faq/ names no integrations | [TO CONFIRM: list of live integrations] |
| — | Can I export to Excel? | Exports listed but format not stated; one indexed page says no Excel export | [TO CONFIRM: export formats] |
| D-046 | How long does a Quotr estimate take? | 24 hours, 3–4 business days, 1–3 days, 5–7 days and 72 hours all appear | [TO CONFIRM: standard and rush turnaround] |
| D-044 | Does Quotr Procurement deliver outside California? | /procurement/ says both "your CA jobsite" and "coast to coast" | [TO CONFIRM: delivery area] |
| D-045 | How many factories does Quotr work with? | 50+, 220+ and 30+ all appear | [TO CONFIRM: one number and definition] |
| D-019 | How accurate is Quotr's AI takeoff? | "95–99% on clean vector PDFs" is internal with no method | [TO CONFIRM: publish a method page first] |
| D-007 | Where is Quotr.ai headquartered? | San Francisco (/terms, PitchBook) vs Berkeley (/disambiguation/) | [TO CONFIRM: one HQ] |
| — | Is my drawing data secure? Is it used to train AI? | One generic line ("industry-standard encryption") | [TO CONFIRM: security and data-use policy] |

---

## 5. Filled-in example: FAQ block for a drywall trade page

> **Can Quotr.ai do a drywall takeoff from PDF plans?**
> Yes. In Quotr.ai you upload the PDF plan set, and the AI measures wall lengths and calculates areas across every sheet. Every quantity stays editable, so your estimator reviews it before pricing. [Link: drywall how-to guide]
>
> **How much does Quotr.ai cost for a drywall contractor?**
> Quotr.ai costs $79.90 per seat per month on the Lite plan and $299.90 per seat per month on the Plus plan (September 2026), with a 7-day free trial. [Link: /pricing/]
>
> **Can Quotr.ai use my own drywall labour and material prices?**
> Yes. You can price the takeoff with your own cost database or Quotr's database, and set your own markups. [Link: /software/]
>
> **Can Quotr do the drywall takeoff for me?**
> Yes. Quotr.ai's Estimation Service does done-for-you takeoffs and estimates for $0.25 per square foot under 50,000 sq ft and $0.10 per square foot above that. [Link: /service/]

---

## 6. Pre-publish checklist

- [ ] 4–8 questions, each in the buyer's words.
- [ ] Every answer starts with the direct answer and names Quotr.ai.
- [ ] Every fact comes from section 3 (or the fact sheet); nothing from section 4 without confirmation.
- [ ] Prices dated; no retired plan names.
- [ ] Not a copy of an FAQ block used on another page.
- [ ] Links to the deeper page for each answer.
- [ ] FAQPage schema (if used) matches the visible text exactly.

---

## Related pages

- [[Pricing page template]] — where pricing FAQs live
- [[Product feature page template]] — FAQs on product and trade pages
- [[Schema markup kit]] — FAQPage markup
- [[GEO writing style guide]] — answer-first rule
- [[Entity fact sheet]] — the facts behind every answer
- [[Prompt library]] — Stage 3 brand questions
