# Partnerships and Marketplaces Playbook

**What this page is for:** How Quotr.ai can earn trusted third-party listings and mentions through integration marketplaces (Procore, Autodesk, QuickBooks), industry partners, associations and co-marketing, what each route requires, and how to decide which to pursue.

**Last updated:** 2026-09-25

**Sources:** [geo_content_playbook_b2b.md](<../../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md>) (§1 Aleyda Solis on integrations pages; §3 inference on integration marketplaces), [quotr_offsite_presence.md](<../../../research_notes/Quotr GEO AEO strategy audit/quotr_offsite_presence.md>) (§1 Procore network; §3 memberships and partnerships), [quotr_onsite_content_audit.md](<../../../research_notes/Quotr GEO AEO strategy audit/quotr_onsite_content_audit.md>) (§2 formats absent; §6 integrations and security gaps), [competitor_geo_benchmark.md](<../../../research_notes/Quotr GEO AEO strategy audit/competitor_geo_benchmark.md>) (§1–2 competitor partnerships), [verification_quotr_and_competitors.md](<../../../research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>) (gaps filled); [../../00-quotr/product-and-features.md](../../00-quotr/product-and-features.md) (§3.6–3.7 Revit add-in, integrations); competitor profiles [../../03-market/competitors/togal-ai.md](../../03-market/competitors/togal-ai.md), [../../03-market/competitors/handoff.md](../../03-market/competitors/handoff.md). Marketplace requirements checked via WebSearch on 2026-09-25: [Procore Partner Program](https://developers.procore.com/partner), [Procore marketplace requirements](https://developers.procore.com/documentation/partner-content-reqs), [Procore listing guidelines](https://developers.procore.com/documentation/marketplace-listing-guidelines), [Autodesk AECO Technology Partner Program](https://www.autodesk.com/partner-signup), [Autodesk Construction Cloud integrations](https://construction.autodesk.com/partners/integrate-with-autodesk-construction-cloud/), [Autodesk App Store Revit publisher guidelines](https://aps.autodesk.com/app-store/publisher-center/revit), [Intuit: list on the QuickBooks App Store](https://developer.intuit.com/app/developer/qbo/docs/go-live/list-on-the-app-store), [Intuit technical requirements](https://developer.intuit.com/app/developer/qbo/docs/go-live/publish-app/technical-requirements).

---

## 1. Why partners and marketplaces (and how strong the evidence is)

- **Third-party pages carry most AI citation weight.** In Aleyda Solis's August 2026 study, 82.3% of top cited SaaS sources were external to the brand (`verification_geo_evidence.md` claim #18). A marketplace listing or a partner's page is a third-party page that describes Quotr in someone else's words.
- **Google AI Mode cites integrations and templates pages for SaaS** (qualitative finding from Aleyda Solis; `geo_content_playbook_b2b.md` §1).
- **But no data measures the AI-citation effect of marketplace listings.** The notes call Procore and QuickBooks marketplaces "plausible third-party corroboration sources" with no impact data (`geo_content_playbook_b2b.md` §3). Pursue them for **customers and distribution first**; AI visibility is a side benefit.
- **Competitors use partners:** Togal.AI is sold as an AI add-on inside eTakeoff (about $1,800/year/user) and has a Beck Technology / DESTINI Estimator partnership (2022); Handoff offers materials purchasing through Lowe's and counts Nemetschek (Bluebeam's owner) and Masco among its investors; Buildxact advertises live dealer pricing (competitor profiles; competitor benchmark §1–2).
- **Buyers ask about integrations:** "does Quotr integrate with Procore or QuickBooks" (D-037) and "can I export an AI takeoff to Excel" (E-068) are in the prompt library. Today Quotr's /faq/ says it "easily integrates with popular design software and project management tools" without naming any, and there is no integrations page (onsite audit §3, §6).

---

## 2. Where Quotr stands

| Item | Status | Source |
|---|---|---|
| Named integrations | **None named** on the site | Onsite audit §3 (/faq/) |
| Integrations page | Does not exist | Onsite audit §2 |
| Procore App Marketplace | **No listing found** | Offsite notes §1 |
| Procore Construction Network | Profile at [network.procore.com/p/floz-berkeley](https://network.procore.com/p/floz-berkeley) (content not verified: cookie wall; old "floz" slug) | Offsite notes §1 |
| Autodesk App Store (Revit add-in "Quotr.ai Estimate") | **Not found** in search; whether the add-in is still sold is **TO CONFIRM** | Product notes §3.6 |
| QuickBooks App Store | Not found | — |
| Excel export | Formats not stated; one indexed Quotr page says no Excel export | Fact sheet row 30 (**TO CONFIRM**) |
| Associations | Listed in the Modular Building Institute member directory (slug "quotr-io"); a BIA Bay Area member listing is linked from /disambiguation/ but was not opened. Current membership **TO CONFIRM with Quotr** | Offsite notes §3; fact sheet §1c |
| Education | Vanderbilt University classroom story (Quotr blog only; no third-party source) | Offsite notes §3 |
| Accelerator / investors | Berkeley SkyDeck Batch 19 page and Llama Ventures portfolio list Quotr | Verification claim 29 |

**First step (no engineering needed):** Quotr confirms which integrations and export formats are live. Everything below depends on that answer.

---

## 3. Integration marketplaces: requirements at a glance

Requirements summarised from the platforms' developer pages (via WebSearch, 2026-09-25). Re-read the current documentation before starting.

| Marketplace | Who it reaches | What it takes (summary) | Fit for Quotr |
|---|---|---|---|
| **Procore App Marketplace** ([developers.procore.com](https://developers.procore.com/)) | GCs and specialty contractors using Procore | Join the Technology Partner Program (sandbox access); build an integration; pass app validation and the Marketplace Approval Checklist; meet listing guidelines. Programme gates cited on the partner page include at least 1 test customer, at least 1 monthly active customer, completed app validation and a partner support SLA under 48 hours | **High** if customers use Procore: sending takeoff quantities or estimates into Procore projects or budgets is a natural link. Procore also appears in AI answers for bid management and procurement prompts |
| **Autodesk Construction Cloud integrations** ([integrations page](https://construction.autodesk.com/partners/integrate-with-autodesk-construction-cloud/)) | Autodesk Build/Docs users; precon teams | Join the Autodesk AECO Technology Partner Program; build the integration; Autodesk lists 400+ integrations and 275+ partners; partners get a 50% discount on initial Autodesk Developer Network membership | **Medium–High**: Autodesk wins "multifamily takeoff" answers by default (competitor benchmark §1); being listed alongside Autodesk tools puts Quotr near that answer space |
| **Autodesk App Store (Revit add-ins)** ([publisher guidelines](https://aps.autodesk.com/app-store/publisher-center/revit)) | Architects and design-build teams in Revit | Register as a publisher; app must work with the current Revit version (Revit 2026) on supported Windows versions; submit through the publisher centre | **Only if** the Revit add-in is still a product. If not, retire old Revit descriptions instead ([wikidata-and-knowledge-graph.md](wikidata-and-knowledge-graph.md)) |
| **QuickBooks App Store** ([Intuit developer](https://developer.intuit.com/app/developer/qbo/docs/go-live/list-on-the-app-store)) | Small contractors using QuickBooks Online | Technical review against Intuit's requirements (Intuit's blog cites about 20 days on average), an app assessment/security questionnaire, and ongoing annual review | **Medium**: useful for small subs if estimates or purchase orders need to flow into accounting; build only if customers ask |

**Rules for any marketplace:**
1. **Never list an integration that does not exist or is "coming soon".** Marketplace pages are fact sources for AI; a false claim spreads.
2. **One name:** list as "Quotr.ai", with the canonical one-liner and current prices ([../../00-quotr/entity-fact-sheet.md](../../00-quotr/entity-fact-sheet.md)).
3. **Security answers ready:** marketplaces and IT buyers ask about data handling. Quotr has only one generic line ("industry-standard encryption"); a security page is needed first (**TO CONFIRM** policies with Quotr). Construction buyers rank security as a top AI concern (54% in the Dodge/CMiC survey; `geo_content_playbook_b2b.md` §6).
4. **Support promise you can keep** (e.g., Procore's SLA gate).

---

## 4. Build an integrations page on quotr.ai (do this with the first real integration)

AI engines need one clear page that answers "does Quotr.ai integrate with X?".

**Sections (in order):**
1. H1 "Quotr.ai integrations"
2. Quick answer: the list of live integrations and export formats, dated.
3. Table: integration / what syncs (direction, data) / plan availability / setup time / docs link.
4. One section per integration: how it works, screenshots, limitations.
5. Exports: formats (PDF proposals and marked-up plans are confirmed; spreadsheet formats **TO CONFIRM**).
6. "Not yet supported": be explicit (it stops AI tools from guessing).
7. FAQ (D-037, E-068).

Use [../templates/product-feature-page.md](../templates/product-feature-page.md) for structure and [../schema-markup-kit.md](../schema-markup-kit.md) for BreadcrumbList/FAQPage.

---

## 5. Other partnership routes (no engineering required)

| Route | Examples | What it produces | First step |
|---|---|---|---|
| **Associations** | BIA Bay Area and Modular Building Institute (listed as a member); NAHB; NMHC | Member resources, event talks, co-published data on association sites (strong authority for tariffs and multifamily questions) | Ask BIA and MBI about member content slots, webinars, or a data briefing |
| **Manufacturers and logistics partners** (Quotr Procurement) | Factories Quotr sources from; freight forwarders; customs brokers | Co-published guides on quality checks, certifications (e.g., NFRC for windows, CARB/TSCA for cabinets, cUPC for fixtures — all High-priority prompts L-082, L-090, L-101), landed-cost data | Identify 1–2 partners willing to co-author a guide (**TO CONFIRM** with Quotr's procurement team) |
| **Referral partners** | Estimating consultants, architects, lenders' cost reviewers | Mentions on their sites; referrals | Create a simple referral programme page (terms **TO CONFIRM**) |
| **Complementary software** (non-competing: CRM, project management, accounting) | — | Joint webinars, "works with" pages, co-authored guides | Start with tools Quotr customers already use |
| **Education** | Vanderbilt University classroom use (first-party story) | A university page or course listing that names Quotr.ai | Ask the instructor whether the course page can mention the tool |
| **Accelerator and investors** | Berkeley SkyDeck; Llama Ventures | Portfolio updates, newsletters, demo-day content | Send the canonical one-liner and any news (e.g., the seed announcement once confirmed) |
| **Events** | IBS, PCBC, Dallas Build Expo (Quotr attended in 2026) | Speaker listings, exhibitor directories, recap coverage | Apply for speaking slots with a data-led talk |

**Co-marketing package (reuse for every partner):** a joint webinar (recorded for YouTube), a joint case study with numbers, a partner blog post on each site, and, for significant partnerships, a press release pitched to trade press ([listicle-and-pr-outreach.md](listicle-and-pr-outreach.md)).

---

## 6. How to decide what to pursue

Score each option 1–3 and pursue the top two:

| Criterion | Question |
|---|---|
| Customer demand | How many current customers or prospects ask for it? |
| Buyer reach | Does the partner reach Quotr's personas (subs, residential GCs, developers)? |
| Effort | Engineering weeks, review time, ongoing support |
| Proof value | Will the partner name Quotr.ai on a page AI engines read (marketplace listing, association site, press)? |
| Prompt fit | Does it answer a tracked prompt (D-037, E-066, E-006, E-012)? |

**Suggested order (recommendation, pending Quotr's input):** (1) confirm and publish current integrations/exports on an integrations page; (2) association content with BIA Bay Area and MBI (no engineering); (3) Procore integration and marketplace listing if customer demand confirms it; (4) manufacturer co-published quality/certification guides for Quotr Procurement.

---

## 7. Tracking

| Metric | How | Cadence |
|---|---|---|
| Live integrations and listings | Log | Quarterly |
| Partner pages that name Quotr.ai correctly | Audit | Quarterly |
| Referral sessions from marketplaces and partner sites | GA4 | Monthly |
| AI answer to D-037 ("does Quotr integrate with Procore or QuickBooks") accurate | Prompt tracking | Monthly |
| Leads and customers sourced from partners | CRM | Monthly |

---

## Related pages

- [wikidata-and-knowledge-graph.md](wikidata-and-knowledge-graph.md) — keeping partner and directory profiles consistent
- [listicle-and-pr-outreach.md](listicle-and-pr-outreach.md) — announcing partnerships
- [review-generation.md](review-generation.md) — review sites (G2 also has integration-partner categories)
- [../templates/product-feature-page.md](../templates/product-feature-page.md) — structure for an integrations page
- [../../00-quotr/product-and-features.md](../../00-quotr/product-and-features.md) — integrations and Revit add-in status
- [../../03-market/competitors/procurement-and-sourcing.md](../../03-market/competitors/procurement-and-sourcing.md) — procurement players and partners
