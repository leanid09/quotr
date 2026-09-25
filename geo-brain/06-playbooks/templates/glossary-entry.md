# Template: Glossary Entry (Construction Dictionary Term)

**What this page is for:** A template for entries in Quotr.ai's Construction Dictionary (quotr.ai/dictionary/) so each term has a quotable one-sentence definition, a real example with numbers, and a clear link to how Quotr.ai handles it.

**Last updated:** 2026-09-25

**Sources:** <../../../research_notes/Quotr GEO AEO strategy audit/quotr_onsite_content_audit.md> (§2 dictionary inventory, §3 sample page "AI Takeoff", §4 assessment), <../../../research_notes/Quotr GEO AEO strategy audit/competitor_geo_benchmark.md> (§3: pages cited for "what is AI takeoff"; the Easy Takeoffs definition lifted into a summary), <../../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md> (§2 Aleyda Solis content prioritization; §7 click resilience), <../../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md> (claim #2); [../../04-prompt-library/construction-glossary.md](../../04-prompt-library/construction-glossary.md); [International Chamber of Commerce: Incoterms® 2020](https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/) and [ICC Academy: DAP or DDP](https://academy.iccwbo.org/incoterms/article/incoterms-2020-dap-or-ddp/) (for the DDP example; checked via WebSearch on 2026-09-25).

---

## 1. Purpose and what the evidence says

- **What Quotr has:** 55 dictionary terms under /dictionary/ (e.g., ai-takeoff, quantity-takeoff, bid-leveling, scope-gap, markup-vs-margin, rfi, change-order, panel-schedule, rebar, rough-in-plumbing, guaranteed-maximum-price, design-build), published June 16 – July 15, 2026 and not updated since. The sampled "What Is AI Takeoff?" entry is definition-first but short (~200 words), with no author and no sources (onsite audit §2–3).
- **What AI engines cited instead:** for "what is AI takeoff / how do I do a takeoff from PDF plans", Perplexity cited Bluebeam, Buildxact, BuildVision AI, Houzz Pro, Autodesk and ruh.ai's glossary, **not** Quotr's dictionary page, even though it exists and ranks (competitor benchmark §3).
- **Quotable definitions travel:** Easy Takeoffs' one-line definition ("AI-assisted means the software drafts a result and a human reviews and owns it…") was lifted into a search summary (competitor benchmark §3).
- **Generic definitions have limited value on their own:** Aleyda Solis's content-prioritization framework says "another generic definition … is unlikely to generate meaningful, incremental value", and AI can answer simple definitions without a click (`geo_content_playbook_b2b.md` §2, §7). So each Quotr entry must add something specific: a worked example with numbers, a Quotr-specific view, or a link to a tool.
- **Keep one page per term.** Do not spin up many near-duplicate term pages for keyword variants (`verification_geo_evidence.md` claim #2).

---

## 2. Which prompts this template targets

| ID | Prompt | Priority | Dictionary page |
|---|---|---|---|
| L-033 / L-034 | what is AI takeoff / what is AI construction estimating software | Med | [/dictionary/ai-takeoff/](https://quotr.ai/dictionary/ai-takeoff/) |
| L-030 / L-045 | what is a construction takeoff / takeoff vs estimate | Med / Low | [/dictionary/quantity-takeoff/](https://quotr.ai/dictionary/quantity-takeoff/) |
| L-004 / L-005 | markup vs margin; markup for a 30% margin | Med / Low | [/dictionary/markup-vs-margin/](https://quotr.ai/dictionary/markup-vs-margin/) (add the formula and worked example) |
| L-110 | what does DDP mean when buying building materials | **High** | New term (ties to Quotr Procurement) |
| L-115 / L-117 | what is an HTS code; what is an ISF filing | Med / Low | New import terms |
| L-126 | what is buyout in construction | Med | New or existing term |
| L-135 | hard costs vs soft costs in real estate development | Med | New term |
| L-044 | what is an AI agent for construction | Med | New term (ties to the Quotr.ai AI Agent) |
| L-095 / L-099 | panel schedule; rough-in plumbing | Low | Existing terms |

**Priority:** upgrade the terms tied to High prompts and to Quotr's product first (ai-takeoff, quantity-takeoff, bid-leveling, scope-gap, markup-vs-margin), then add the import and procurement terms (DDP, HTS code, landed cost, buyout), where no software vendor owns the answer (see [../../03-market/white-space.md](../../03-market/white-space.md)).

---

## 3. Required sections, in order

| # | Section | What goes in it | Length |
|---|---|---|---|
| 1 | **H1** | "What Is [Term]?" (or "[Term]: Definition and Example") | 1 line |
| 2 | **One-sentence definition** | "[Term] is [category] that [does what], used by [who] to [outcome]." Must work alone if quoted | 20–35 words |
| 3 | **Short explanation** | 2–3 sentences: how it works, in plain words | 40–70 words |
| 4 | **Why it matters** | Who cares and what goes wrong without it | 2–4 bullets |
| 5 | **Example with numbers** | A small worked example (quantities, costs, formula) | Table or 3–5 lines |
| 6 | **Formula** (if any) | Written out, with units | 1–2 lines |
| 7 | **How it works in Quotr.ai** | One brand-attributed sentence linking to the product or service page | 1–2 sentences |
| 8 | **Common confusions** | "[Term] vs [similar term]" | 2–4 bullets |
| 9 | **Related terms** | 3–6 dictionary links | List |
| 10 | **Sources** | Standards bodies, associations, codes | 1–3 links |
| 11 | **Byline and dates** | Author or "Reviewed by [estimator]"; Published / Last updated | 1 line |

**Target length:** 250–500 words. Longer only if the term needs a worked example.

---

## 4. Filled-in example outline A: "What is DDP (Delivered Duty Paid)?" (new term, L-110)

**H1:** What Is DDP (Delivered Duty Paid) in Building Materials?

**One-sentence definition (draft, based on the ICC's Incoterms® 2020 wording):**
> DDP (Delivered Duty Paid) is an Incoterms® trade rule under which the seller delivers goods cleared for import, ready for unloading at the buyer's named destination, and bears all the costs and risks of getting them there, including import duties, taxes and customs formalities.

**Short explanation:** For a builder, a DDP price for windows or cabinets means one delivered price to the named place, instead of separate bills for freight, customs clearance and duties. Under Incoterms® 2020, DDP delivery happens on the arriving vehicle "ready for unloading", so unloading is normally the buyer's job unless the contract says otherwise; the buyer should also check where the named place is (port, warehouse or jobsite).

**Why it matters:**
- It makes a landed cost comparable with a local dealer quote.
- It moves customs paperwork and duty risk to the seller.
- It is the basis of Quotr Procurement's pricing (see below).

**Example with numbers:** a table comparing an FOB quote plus freight, duty (rate from the tariff schedule; sourced), customs broker and inland delivery vs one DDP price. Use real figures from a Quotr procurement quote only with permission (**TO CONFIRM with Quotr**).

**How it works in Quotr.ai (draft):**
> Quotr Procurement sources finish materials from manufacturers in China and delivers them duty-paid to the jobsite, so the price Quotr quotes includes shipping, customs and duties to your site. See [/procurement/](https://quotr.ai/procurement/) and [ddp-construction-materials](https://quotr.ai/blog/ddp-construction-materials/).
> (Delivery area — California only or all US — is **TO CONFIRM with Quotr**; /procurement/ says both.)

**Common confusions:** DDP vs FOB; DDP vs DAP (duties not included); "landed cost" vs "DDP price".

**Related terms:** landed cost, HTS code, customs broker, ISF filing, buyout, lead time.

**Sources:** [ICC Incoterms® 2020](https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/); [ICC Academy: DAP or DDP](https://academy.iccwbo.org/incoterms/article/incoterms-2020-dap-or-ddp/); U.S. Customs and Border Protection for import basics.

---

## 5. Filled-in example outline B: "What is AI takeoff?" (upgrade of the existing entry, L-033)

**One-sentence definition (draft):**
> AI takeoff is construction takeoff done with software that automatically detects, counts and measures items on digital drawings, which an estimator then checks and edits before pricing.

**Short explanation:** You upload the plan set; the software finds symbols (outlets, doors, fixtures), measures lengths (walls, pipe, conduit) and calculates areas (floors, roofs). Results still need a human check, especially on scanned or low-quality drawings.

**Why it matters:** takeoff is the slowest part of many estimates; faster takeoff means more bids; accuracy concerns remain (57% of contractors named data accuracy as a top AI concern in the Dodge/CMiC survey, `geo_content_playbook_b2b.md` §6).

**Example with numbers:** "On a [N]-sheet residential set, the AI counted [X] outlets and [Y] doors; the estimator corrected [Z] items flagged as low-confidence." Use a real, sourced test (**TO CONFIRM with Quotr**; today's accuracy figures are internal and unpublished).

**How it works in Quotr.ai:**
> In Quotr.ai, you upload a PDF or image plan set; the AI counts symbols, measures lengths and calculates areas across the full set, and every extracted quantity stays editable by the estimator. AI takeoff is included on every Quotr.ai plan. See [/software/](https://quotr.ai/software/).

**Common confusions:** AI takeoff vs digital (manual on-screen) takeoff; AI takeoff vs a done-for-you takeoff service; takeoff vs estimate.

**Related terms:** quantity takeoff, scope gap, bid leveling, unit price, plug number.

---

## 6. Schema for this page

- DefinedTerm (optional) + BreadcrumbList; the `description` equals the visible one-sentence definition ([../schema-markup-kit.md](../schema-markup-kit.md) 5.10, 5.7).
- If the page has a byline and dates, BlogPosting-style `author` and `dateModified` can be added via an Article/WebPage block; keep them consistent with the visible byline.

---

## 7. Pre-publish checklist

- [ ] One-sentence definition works when read alone.
- [ ] Explanation in plain words; jargon defined.
- [ ] Worked example with numbers (sourced or labelled Quotr data).
- [ ] One brand-attributed "How it works in Quotr.ai" sentence with a link.
- [ ] "Common confusions" section.
- [ ] 3–6 related-term links; linked **from** at least one blog post or trade page.
- [ ] Sources listed; reviewer or author named; dates shown.
- [ ] Not a near-duplicate of another term page.
- [ ] Schema (if used) matches the visible definition.

---

## Related pages

- [faq-block.md](faq-block.md) — for short Q&A that does not need a full term page
- [trade-how-to-guide.md](trade-how-to-guide.md) — guides that link to dictionary terms
- [../geo-writing-style-guide.md](../geo-writing-style-guide.md) — definition-writing rule (Rule 7)
- [../../04-prompt-library/construction-glossary.md](../../04-prompt-library/construction-glossary.md) — construction terms and units
- [../../01-geo-fundamentals/geo-glossary.md](../../01-geo-fundamentals/geo-glossary.md) — GEO terms
- [../../03-market/white-space.md](../../03-market/white-space.md) — import and procurement topics
