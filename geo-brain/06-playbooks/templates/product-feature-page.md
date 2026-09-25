# Template: Product, Feature and Trade Page

**What this page is for:** A template for Quotr.ai product pages, feature pages (e.g., the AI Agent) and the 23 trade pages under /software/trades/, so each one states clearly what the feature does, for whom, at what price and with what limits, in a form AI engines can quote.

**Last updated:** 2026-09-25

**Sources:** [../../00-quotr/product-and-features.md](../../00-quotr/product-and-features.md) (§1–3 modules, plans, trades); <../../../research_notes/Quotr GEO AEO strategy audit/quotr_onsite_content_audit.md> (§2 trade pages, §3 /software/ and drywall page, §4 thin trade pages, §6 trade coverage), <../../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md> (§1 product/landing page citation data; Aleyda Solis on templates and integrations pages), <../../../research_notes/Quotr GEO AEO strategy audit/competitor_geo_benchmark.md> (§2 Beam AI and Kreo trade page trees; §5 trade coverage), <../../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md> (C4–C6, C9, C13, C15), <../../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md> (claims #2, #12).

---

## 1. Purpose and what the evidence says

- **Product and landing pages are cited often.** HubSpot's State of AEO 2026 data (vendor-run; directional) put product listings/landing pages first among formats at a 68.5% average citation rate, and Perplexity favoured them most (`verification_geo_evidence.md` claim #12; `geo_content_playbook_b2b.md` §1).
- **Titles that match narrow sub-questions help.** Ahrefs found ChatGPT-cited pages had titles closer to the narrower "fan-out" sub-queries (e.g., "AI takeoff for residential framing") than pages it skipped (`geo_content_playbook_b2b.md` §1).
- **Quotr's trade pages are thin.** The sampled drywall page had an H1, about 25 words of unique copy, two blog links and CTAs; no FAQ, specifics or examples. Thin, templated pages "can look like doorway pages" (onsite audit §3–4). Some trade pages may have been expanded since (the structural-steel page's index copy showed member counts, connection categories and confidence scores), so re-check each one first (product notes §3.1).
- **Competitors win trade prompts with trade pages.** Drywall, flooring and electrical category prompts went to trade-specific vendor landing pages and listicles; Quotr was absent from all three (visibility tests C4–C6). Beam AI (per-trade pages under /subcontractors/) and Kreo (/trades/) have the page trees Quotr could match (competitor benchmark §2).
- **Quotr's differentiators are invisible in product prompts.** "Construction estimating software with material procurement" (C9), "AI estimating software for residential GCs that goes from plans to proposal" (C13) and "best takeoff software for Mac users" (C15) all describe Quotr, yet Quotr was absent.
- **Each page must be genuinely different.** Google's May 2026 guide warns that pages made mainly to catch every query variation can count as scaled content abuse (`verification_geo_evidence.md` claim #2). 23 trade pages are fine **only** if each has trade-specific scope, units, examples and FAQs.

---

## 2. Which prompts this template targets

| ID | Prompt | Priority | Page |
|---|---|---|---|
| E-006 / E-066 | estimating software with material procurement / takeoff all the way to purchase order | High | /software/ + /procurement/ |
| E-008 / E-063 | AI estimating for residential GCs from plans to proposal / AI takeoff tools that work on residential plans | High | /software/ (residential section) or a residential segment page |
| E-009 / E-017 | takeoff software for Mac / online takeoff in a browser, no download | High | /software/ (**platform TO CONFIRM**) |
| E-069, L-036, L-037 | is there a ChatGPT for blueprints / can AI read construction drawings / can ChatGPT do a takeoff | High | AI Agent feature page (new) |
| E-064 | AI takeoff tool that shows confidence scores | Med | AI takeoff feature page ("Smart Matching" name **TO CONFIRM**) |
| E-065, E-019 | local material prices by zip code / built-in cost database | Med | Estimating feature page |
| E-067, E-012 | compare supplier quotes / bid leveling | High | Bid management feature page |
| E-026, L-051 | best takeoff software for drywall contractors / drywall takeoff from blueprints | High | /software/trades/drywall/ |
| L-094 | AI tool that can count electrical symbols on a PDF | High | /software/trades/electrical/ |
| D-034–D-038 | does Quotr work for my trade / on Mac / which files / integrations / exports | High–Low | /software/ and trade pages (several **TO CONFIRM**) |

---

## 3. Required sections, in order

### 3a. Feature or product page

| # | Section | What goes in it |
|---|---|---|
| 1 | **H1** | What it does in buyer words: "Chat with your construction drawings: Quotr.ai AI Agent" |
| 2 | **Quick answer** | 40–70 words: what it does, who it is for, which plan includes it, price from |
| 3 | **How it works** | 3–5 numbered steps with screenshots (alt text) |
| 4 | **What it can do** | Table: task → example → output |
| 5 | **Inputs and outputs** | File types, units, export formats (**only confirmed ones**) |
| 6 | **Accuracy and review** | How results are checked (confidence scores, editable quantities); honest limits (scanned PDFs, complex drawings) |
| 7 | **Example** | A real plan set: what was asked/measured, result, time (sourced) |
| 8 | **Plans and pricing** | Which plan includes it; link to /pricing/ |
| 9 | **Proof** | Case study, video, reviews (dated) |
| 10 | **Compared with the alternatives** | Manual method and 1–2 named tools, fairly |
| 11 | **FAQ** | 4–6 questions |
| 12 | **Related** | Trade pages, how-to guides, dictionary terms |

### 3b. Trade page (/software/trades/[trade]/)

| # | Section | What goes in it |
|---|---|---|
| 1 | **H1** | "AI [trade] takeoff and estimating software" |
| 2 | **Quick answer** | What Quotr.ai measures for this trade, from which drawings, and the price from |
| 3 | **Scope table (trade-specific)** | Items → unit (EA, LF, SF, CY, squares) → how Quotr.ai measures it → what the estimator checks |
| 4 | **Workflow** | Plans → takeoff → estimate (own or Quotr database) → bid comparison → proposal → (optional) procurement for this trade's materials |
| 5 | **Example** | A sample plan for this trade with quantities (from the sample-deliverables library if permitted) |
| 6 | **Residential vs commercial** | What differs for this trade (state Quotr's focus once confirmed) |
| 7 | **Limits** | Where AI needs a human check for this trade |
| 8 | **Proof** | Trade-specific case study or video |
| 9 | **Want it done for you?** | Quotr Service for this trade ($0.25/$0.10 per sq ft) |
| 10 | **FAQ** | 4–6 trade questions from [buyer-questions-by-trade.md](../../04-prompt-library/buyer-questions-by-trade.md) |
| 11 | **Related** | Trade how-to guide, cost guide, dictionary terms, best-of post for the trade |

**Minimum bar before a trade page is "done":** 400+ words of trade-specific content, a scope table, one example, one FAQ block, and at least one link to a trade how-to. If a trade cannot meet this yet, consider consolidating it into a broader page (e.g., "Finishes: tile, painting, millwork") rather than keeping a thin page.

---

## 4. Filled-in example outline A: AI Agent feature page (new)

**H1:** Chat with Your Construction Drawings: the Quotr.ai AI Agent

**Quick answer (draft, confirmed facts):**
> The Quotr.ai AI Agent reads your plan set and answers plain-English questions about it, such as symbol counts, room dimensions and openings. It is included on every Quotr.ai plan: a basic AI agent on Lite ($79.90 per seat per month) and advanced AI on Plus ($299.90 per seat per month), with a 7-day free trial (September 2026).

**What it can do (table):** /software/ says you can "ask about symbol counts, room dimensions, openings — anything on the drawing". Illustrative questions to show (test each in the product before publishing): "How many duplex outlets are on level 2?" → count; "What are the dimensions of bedroom 3?" → dimensions; "List all door openings" → openings. Add more only from real product behaviour, with screenshots.

**Accuracy and review:** "The estimator still owns the final number" (Quotr's own wording in index text). Explain how to check answers against the drawing.

**Limits (TO CONFIRM with Quotr):** what "advanced AI" adds on Plus; file types; behaviour on scanned PDFs.

**FAQ:** "Is there a ChatGPT for blueprints?" (answer: yes, tools like the Quotr.ai AI Agent, Togal.CHAT and STACK Assist do this; describe fairly), "Can ChatGPT do a construction takeoff?" (link to [chatgpt-for-construction-estimating](https://quotr.ai/blog/chatgpt-for-construction-estimating/)), "Does the AI Agent replace the estimator?"

---

## 5. Filled-in example outline B: drywall trade page (rewrite)

**H1:** AI Drywall Takeoff and Estimating Software

**Quick answer (draft):**
> Quotr.ai measures drywall wall lengths and calculates wall and ceiling areas from PDF plan sets, then turns the quantities into a priced estimate and proposal. Every quantity stays editable. Plans start at $79.90 per seat per month with a 7-day free trial; Quotr Service can also do the takeoff for you at $0.25 per sq ft under 50,000 sq ft (September 2026).

**Scope table (draft; confirm each row with Quotr's product team):**

| Item | Unit | How Quotr.ai measures it | Estimator checks |
|---|---|---|---|
| Walls by type | LF → SF | Traced lengths × heights | Wall types and heights |
| Ceilings and soffits | SF | Area detection | Ceiling heights, soffits |
| Openings | EA / SF | Detected doors and windows | Deduction rule |
| Sheets | EA (by size) | From SF + waste | Waste factor |
| Corner bead and trims | LF | [TO CONFIRM] | [ ] |

**Example:** [2,000 SF] residential plan from the sample library (**TO CONFIRM**), with quantities.

**Fix from today's page:** the current copy says "from commercial floor plans" only; add residential if Quotr confirms residential is a core audience.

**FAQ:** see the drywall example in [faq-block.md](faq-block.md).

**Links:** drywall how-to ([trade-how-to-guide.md](trade-how-to-guide.md) example), drywall cost guide ([cost-guide.md](cost-guide.md) example), [best-drywall-estimating-software-in-2026](https://quotr.ai/blog/best-drywall-estimating-software-in-2026/) (after its pricing fix).

---

## 6. Trade page priority order

Based on High-priority prompts in the [prompt library](../../04-prompt-library/prompt-library.md) and the trades with the least supporting content (onsite audit §6):

1. **Drywall, flooring, roofing, framing** (High how-to and tool prompts; roofing has only a trade page and one service sample).
2. **Windows and doors, cabinets/millwork, tile** (where takeoff meets Quotr Procurement; see [../../03-market/white-space.md](../../03-market/white-space.md)). Note: Quotr has "doors-hardware", "millwork" and "tile" pages; windows are covered under "glazing" (**check naming with Quotr**).
3. **Electrical, plumbing, HVAC** (already have supporting posts; add scope tables and brand-attributed examples).
4. The remaining trades: expand or consolidate.

---

## 7. Schema for these pages

- /software/: SoftwareApplication with Offers + FAQPage + BreadcrumbList ([../schema-markup-kit.md](../schema-markup-kit.md) 5.2, 5.4, 5.7).
- Feature and trade pages: BreadcrumbList; FAQPage for visible FAQs; VideoObject for demos. Reference the SoftwareApplication by `@id` (`https://quotr.ai/#software`) rather than redefining it.
- Remove the repeated trade grid (it appears three times in the delivered text of /software/; onsite audit §1).

---

## 8. Pre-publish checklist

- [ ] H1 says what the feature does or which trade, in buyer words.
- [ ] Quick answer names Quotr.ai, the plan that includes it and the price from (dated).
- [ ] Trade pages: scope table with units; 400+ words of trade-specific content; one example; FAQ.
- [ ] Only confirmed file types, integrations, exports and platforms are stated.
- [ ] Limits section (scanned PDFs, complex drawings, what the estimator checks).
- [ ] Proof: case study, video or dated reviews (or none claimed).
- [ ] No claims from the "risky" list (80% maths, unmethodical accuracy %, factory counts).
- [ ] Links to how-to, cost guide, dictionary terms and /pricing/.
- [ ] Schema references the SoftwareApplication `@id`; validated.
- [ ] Not a near-copy of another trade page.

---

## Related pages

- [pricing-page.md](pricing-page.md) — the plan details every product page links to
- [trade-how-to-guide.md](trade-how-to-guide.md) and [cost-guide.md](cost-guide.md) — supporting trade content
- [faq-block.md](faq-block.md) — approved answers
- [youtube-video-brief.md](youtube-video-brief.md) — demo videos for each feature and trade
- [../../00-quotr/product-and-features.md](../../00-quotr/product-and-features.md) — module-by-module facts and open questions
- [../../04-prompt-library/buyer-questions-by-trade.md](../../04-prompt-library/buyer-questions-by-trade.md) — trade questions for FAQs
- [../../03-market/competitors/beam-ai.md](../../03-market/competitors/beam-ai.md) — the trade-page tree to learn from
