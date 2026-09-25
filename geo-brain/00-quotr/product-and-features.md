# Quotr.ai Products and Features

**What this page is for:** A plain-English guide to every Quotr.ai product and feature: what it does, who it is for, what goes in and comes out, which plan it belongs to, what proof exists, and what buyers ask AI tools about it.

**Last updated:** 2026-09-25

**Sources:** [quotr_onsite_content_audit.md](<../../research_notes/Quotr GEO AEO strategy audit/quotr_onsite_content_audit.md>), [quotr_offsite_presence.md](<../../research_notes/Quotr GEO AEO strategy audit/quotr_offsite_presence.md>), [verification_quotr_and_competitors.md](<../../research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>), [quotr_ai_visibility_tests.md](<../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>), [competitor_geo_benchmark.md](<../../research_notes/Quotr GEO AEO strategy audit/competitor_geo_benchmark.md>); quotr.ai pages /, /software/, /pricing/, /service/, /procurement/, /faq/, /tutorials/, /case-studies/, /disambiguation/, /contractors/ and blog posts (read in the notes, plus search-index text checked with WebSearch on 2026-09-25); /pricing/, /software/ and /about-us/ re-read directly with a scraper on 2026-09-25.

---

## How to read this page

- **Takeoff** = measuring and counting everything on a set of construction drawings (for example: 240 outlets, 1,800 feet of wall, 3,200 square feet of tile). It is the first step of any estimate.
- **Estimate** = the takeoff quantities multiplied by prices for materials and labour, plus markups.
- **Bid / proposal** = the price a contractor sends to win the job.
- **Procurement / buyout** = actually buying the materials once the job is won.
- **Confidence labels:** **Verified** = seen on a live quotr.ai page in the research notes. **Index-only** = seen only in the search engine's copy of a quotr.ai page (may be out of date). **TO CONFIRM with Quotr** = unknown or conflicting.

---

## 1. The big picture: three product lines

Quotr.ai describes itself as "The all-in-one estimation platform" ([homepage](https://quotr.ai/)). It sells three things:

| Product line | In one sentence | Main buyer | How it is sold | Main page |
|---|---|---|---|---|
| **Quotr Software** | Do-it-yourself AI takeoff, estimating, bids and proposals from PDF plans | Trade subcontractors and their estimators; GCs | Monthly per-seat subscription: Lite $79.90, Plus $299.90, Enterprise custom; 7-day free trial | [/software/](https://quotr.ai/software/) (also served at [/contractors/](https://quotr.ai/contractors/), which carries a canonical tag pointing to /software) |
| **Quotr Service** | Done-for-you takeoffs, cost estimates and pro formas, made by Quotr's team with AI | Developers, GCs and subs who want estimates without doing them | Per project: $0.25/sq ft under 50,000 sq ft; $0.10/sq ft above 50,000 sq ft | [/service/](https://quotr.ai/service/) (also served at [/developers/](https://quotr.ai/developers/)) |
| **Quotr Procurement** | Managed factory-direct buying of finish materials from manufacturers in China, delivered duty-paid to the jobsite | Developers, homebuilders and contractors buying windows, doors, cabinets, flooring and fixtures | Per project quote (no fixed price list published) | [/procurement/](https://quotr.ai/procurement/) |

The workflow Quotr sells is: **plans → takeoff → estimate → bid → procurement**. The live /software/ page puts it as: "From the moment plans hit your inbox to the moment a supplier's PO is signed Quotr.ai owns every step" and "One platform from takeoff to purchase order". No other AI takeoff vendor in the research combines software, a done-for-you service and factory-direct procurement (see [positioning-and-proof-points.md](positioning-and-proof-points.md)).

---

## 2. Software plans and pricing

| Plan | Price | Label on site | What is included (live /software/ page, scraped 2026-09-25) |
|---|---|---|---|
| **Lite** | $79.90 per seat per month | "Most popular" · "Essential takeoff tools" | Basic AI agent; on-screen takeoff tools; AI symbol detection; area detection; custom database |
| **Plus** | $299.90 per seat per month | "Best value" · "Takeoff, estimating & services" | Everything in Lite, plus: advanced AI; full Quotr database; 2 hours of guided onboarding; project sharing; 2,000 sq ft of takeoff credits per month; 10% off procurement |
| **Enterprise** | Custom ("for complex teams and higher volume") | "Custom for complex teams" | Everything in Plus, plus: priority support; dedicated success manager; on-site onboarding and training; custom features and workflows |

- "AI takeoff on every plan. Per seat, no setup fee. 7-day free trial." ([/software/#pricing](https://quotr.ai/software/#pricing))
- What the Plus "takeoff credits" are (for example, credits toward Quotr Service takeoffs) is not explained on the page. **TO CONFIRM with Quotr.**
- The "10% off procurement" perk in Plus is the only published link between the software plans and Quotr Procurement.
- Source: [/pricing/](https://quotr.ai/pricing/), [/software/](https://quotr.ai/software/), /disambiguation/ schema Offers. **Verified.** New pricing was announced on Sep 14, 2026 ([new-pricing post](https://quotr.ai/blog/new-pricing/)).
- 7-day free trial; "Cancel anytime — no charge if canceled." **Verified** (scrape of /pricing/, 2026-09-25).
- The /pricing/ page describes software as "monthly software for takeoff, estimates, bidding, and procurement" and offers a 30-minute demo at [/book-demo/](https://quotr.ai/book-demo); the team promises replies "within one business day".
- No annual price is shown on /pricing/. (The retired "1 User Plan" in llms.txt said "as low as $249/seat/month billed annually"; do not reuse it.) **TO CONFIRM with Quotr** whether Lite/Plus have annual rates.
- Procurement is optional. The live /software/ FAQ says: "Is procurement required to use Quotr.ai? No. Procurement is fully optional. You can run takeoffs, estimates, and proposals without ever using it — or use Quotr.ai to send quote requests to your own suppliers and compare bids side by side." **Verified.**
- **Retired plans — do not use:** "Solo $299.90/month", "Team (2–6 seats) $499.90/month", "Enterprise (7+)", "1 User Plan $299.90", "2–10 Users Plan $499.90". About 13 Quotr URLs (mostly blog posts, plus the old indexed copy of /contractors/) and llms.txt still show these (verification file, Gaps filled #2). AI tools repeat them, so Quotr's entry price looks nearly four times higher than it is ($299.90 vs $79.90).

---

## 3. Module-by-module guide

### 3.1 AI Takeoff (Quotr Software)

| Item | Detail |
|---|---|
| What it does | "Upload a PDF or image plan set and Quotr.ai organizes every sheet. AI counts symbols, measures lengths, and calculates areas across the full set." Quantities come out "by assembly and location" and flow into the estimate; "every extracted quantity stays editable — full estimator control" (live [/software/](https://quotr.ai/software/), scraped 2026-09-25). Includes a takeoff editor and custom drawing scale (tutorials "Takeoff Editor Overview" and "How to Set a Custom Drawing Scale", [/tutorials/](https://quotr.ai/tutorials/)). |
| Who it is for | Trade subcontractor estimators; GC estimators; developers' teams. The /contractors/ copy frames it as "subscription software you run in-product — estimates, procurement, and proposal exports stay in your workspace, not through a concierge turnaround" (index-only). |
| Inputs | PDF and image plan sets (**Verified**, live /software/). Metric and imperial units are both supported. DWG and Revit files are mentioned only in some indexed Quotr pages, not on the live /software/ page. **TO CONFIRM with Quotr** whether DWG/Revit are supported today. |
| Outputs | Quantities (counts, lengths, areas) linked to marked-up drawings, feeding the estimate |
| Platform | Cloud-based and browser-based: "runs in any modern browser on any operating system", "no desktop install", so it works on Mac and Windows (index-only text of Quotr's PlanSwift comparison and alternatives posts). This is a real contrast with Windows-only desktop tools such as PlanSwift. |
| Plan | All plans ("AI takeoff on every plan"). Lite lists on-screen takeoff tools, AI symbol detection and area detection; Plus adds "Advanced AI" and 2,000 sq ft of takeoff credits per month. |
| Trades | 23 trade workflow pages: electrical, concrete, drywall, flooring, plumbing, HVAC, roofing, framing, masonry, painting, insulation, fire protection, demolition, earthwork, structural steel, glazing, doors and hardware, tile, waterproofing, low voltage, landscaping, sitework, millwork ([sitemap.xml](https://quotr.ai/sitemap.xml)). The onsite audit found them thin (the drywall page had about 25 words of unique copy), but the search-index copy of the [structural steel page](https://quotr.ai/software/trades/structural-steel/) now shows more detail (member counts and lengths by type, connection categories, decking areas, confidence scores). Some trade pages may have been expanded; re-check before rewriting them. The live /software/ grid gives a one-line scope per trade (for example, Electrical: "Outlets, panels, conduit, fixtures"; Roofing: "Membranes, flashings, insulation, drains"). |
| Speed claim | Live /software/ FAQ: "Contractors using Quotr.ai have cut takeoff time by up to 80% — from around 20 hours to just 1–2"; elsewhere on the page: "cutting estimate turnaround by up to 80%". The maths does not match (20→1–2 hours is 90–95%). Customer quote: RL Electric "20 hours … 1–2 hours" (homepage testimonial). |
| Accuracy claim | "95–99% accuracy on counts on clean vector PDFs (Quotr internal benchmarking)"; "roughly 80–88% on low-resolution scans" ([Togal-alternatives post](https://quotr.ai/blog/best-togal-ai-alternatives-2026/); [chat-with-blueprints post](https://quotr.ai/blog/ai-that-reads-construction-drawings-chat-with-blueprints/), index-only). Self-reported; no method page. |
| Smart Matching | Quotr's name for confidence-scored detection: the AI counts every item with a per-item confidence score and an audit trail back to the drawing, so the estimator knows which items to review before the bid goes out. It detects rooms, counts, openings, doors, windows and key symbols (index-only text of Quotr blog and /contractors/ pages). **TO CONFIRM with Quotr** that this is the current official feature name. |
| Proof points | RL Electric case study and [YouTube video](https://www.youtube.com/watch?v=Y2_PUPVtVaE); [product demo video](https://www.youtube.com/watch?v=I0dsjz7Y_kc); tutorials. Missing: a published accuracy test. |

**Questions buyers ask AI tools about this:**
- "What is the best AI takeoff software for [electrical / drywall / HVAC] contractors in 2026?"
- "How accurate is AI takeoff compared with manual takeoff?"
- "Can AI do a takeoff from a scanned PDF?"
- "Which AI takeoff tools work on residential plans?"
- "Is Quotr.ai better than Togal.AI for takeoff?"
- "How long does an AI takeoff take for a 50-page plan set?"
- "What is the cheapest AI takeoff software with a free trial?"

### 3.2 AI Agent ("chat with your blueprints")

| Item | Detail |
|---|---|
| What it does | You ask questions about the drawings in plain English. "The Quotr AI Agent reads your plans directly. Ask about symbol counts, room dimensions, openings — anything on the drawing" (live /software/, scraped 2026-09-25). The comparison table on /software/ adds that the built-in AI "answers questions, counts quantities & runs workflows". Blog: ["AI That Reads Construction Drawings: Chat With Your Blueprints Using Quotr.ai"](https://quotr.ai/blog/ai-that-reads-construction-drawings-chat-with-blueprints/). Quotr also ran an "Ask your plans AI agent" webinar (LinkedIn post by Hanyang Liu, offsite notes §3). |
| Who it is for | Estimators, project managers, GCs and developers who need fast answers from big drawing sets |
| Inputs / outputs | PDF plan sets in; plain-English answers, counts and dimensions out |
| Plan | Lite includes a "Basic AI agent"; Plus includes "Advanced AI" (live /software/ pricing). What "advanced" adds is **TO CONFIRM with Quotr**. |
| Positioning note | Quotr's own post says "the estimator still owns the final number" (index-only). That balanced line is good for AI trust. |
| Name | The live /software/ page uses "Quotr AI Agent" (and "AI Agent", "Basic AI agent"). Pick one name (see [entity-fact-sheet.md](entity-fact-sheet.md#3-naming-rules)). |

**Questions buyers ask AI tools:**
- "Can AI read construction drawings?"
- "Is there a ChatGPT for blueprints?"
- "Can ChatGPT do a construction takeoff?" (Quotr has a post: [chatgpt-for-construction-estimating](https://quotr.ai/blog/chatgpt-for-construction-estimating/))
- "What AI tool can answer questions about a plan set?"
- "How do I find all the door hardware specs in a 200-page drawing set quickly?"

### 3.3 Estimating and cost database

| Item | Detail |
|---|---|
| What it does | Turns takeoff quantities into a priced estimate. "Use your cost database or Quotr's average costs by US zip code. Line items link to editable markups on the drawing" (live /software/). The Quotr database is described as "a maintained construction estimating database with material, labor, and assembly rates by region"; you can "layer in your own pricing and supplier costs" and "apply per-project markups in seconds" (live /software/). Lite includes a "custom database"; Plus includes the "full Quotr database". An older indexed copy of the page adds that users can "use the built-in item library or plug in your own labor, assemblies, location-based pricing, and markup rules" (index-only). Tutorial: "How to Manage Your Database" ([/tutorials/](https://quotr.ai/tutorials/)). |
| Who it is for | Sub and GC estimators; owners who price their own jobs |
| Inputs / outputs | Quantities + unit costs + markups in; priced estimate out |
| Plan | Lite: custom (your own) database. Plus and Enterprise: full Quotr database. |
| Proof | Tutorials; ROI calculator. Missing: detail on where the regional cost data comes from and how often it updates. **TO CONFIRM with Quotr.** |

**Questions buyers ask AI tools:**
- "What is the best construction estimating software with a built-in cost database?"
- "How do I estimate labour and materials for an electrical job?"
- "Markup vs margin in construction — what is the difference?" (Quotr has a dictionary term: markup-vs-margin)
- "Can estimating software use local material prices by zip code?"

### 3.4 Proposals and exports

| Item | Detail |
|---|---|
| What it does | Exports marked-up drawings, takeoff sheets and "a polished proposal when ready to close — no rebuilding deliverables by hand". Users "tie a reusable proposal shell to your working estimate and export a polished PDF — pricing stays synced to the live estimate" (index-only text of /software/ and /contractors/). Tutorial: "How to Export a Proposal". |
| Outputs | Live /software/ lists: "Marked-up plan PDFs; Takeoff and quantity exports; Client-ready proposals; RFQs and bid comparison when you need them". Proposals: "Turn any estimate into a polished proposal PDF in one click … Your scope, exclusions & pricing … Brand-aligned and ready to send". The file format of "takeoff and quantity exports" (Excel/CSV?) is not stated; an indexed Quotr page says Quotr "does not export to Excel". **TO CONFIRM with Quotr.** |
| Plan | Not split by plan on the pricing table (appears to be core to all plans; **TO CONFIRM**) |

**Questions buyers ask AI tools:**
- "What software goes from plans to proposal automatically?"
- "Best software to create construction bid proposals for subcontractors"
- "Can I export an AI takeoff to Excel?"

### 3.5 Bid management and supplier pricing

| Item | Detail |
|---|---|
| What it does | "Quote requests & side-by-side bid comparison in-app" and "RFQs and bid comparison when you need them" (live /software/). Users can "send quote requests to your own suppliers and compare bids side by side. Bring your own vendor list and pricing" (live /software/ FAQ). Also: export line items or comparison sheets (index-only text). Tutorial: "How to Manage Bids". The /disambiguation/ description says Quotr "manages bids with side-by-side comparison" (index-only). Users can "add your own suppliers and compare their quotes inside the app, so existing trade relationships and deals carry in". An "AI bid-comparison parser scans multiple supplier quotes and generates a side-by-side pros/cons and gap breakdown, so you can level competing bids in minutes" (index-only text of Quotr blog pages). |
| Who it is for | Subs collecting supplier quotes; GCs levelling sub bids (**TO CONFIRM** whether GC-side bid levelling is supported) |
| Plan | **TO CONFIRM** |
| Proof | Blog posts: [ai-bidding-software-construction](https://quotr.ai/blog/ai-bidding-software-construction/), [best-ai-bid-software-for-construction](https://quotr.ai/blog/best-ai-bid-software-for-construction/), how-subcontractors-bid-gcs-without-giving-away-margin; dictionary term bid-leveling. Both bidding posts still show retired pricing. |

**Questions buyers ask AI tools:**
- "What is the best bid management software for subcontractors?"
- "How do I level subcontractor bids?"
- "Software to compare supplier quotes for construction materials"
- "AI bidding software for construction 2026"

### 3.6 Revit integration ("Quotr.ai Estimate" add-in)

| Item | Detail |
|---|---|
| What it does | A Revit add-in that "pulls quantities and elements straight from your model to auto-generate an estimate on the main Quotr.ai dashboard", with location-based pricing, room templates and a maintained item library with private database support (index-only text of /disambiguation/ and /contractors/). |
| History | This was Quotr's original 2024-era product for architects: F6S still describes "Quotr Assist" and "Quotr Connector (automatic sync with Autodesk Revit)" and "real-time cost estimation during design iterations" ([F6S](https://www.f6s.com/software/quotr)); YouTube: ["How To Use Quotr Estimate \| Cost Estimation Revit Extension"](https://www.youtube.com/watch?v=zNIXcvCbWAg). |
| Who it is for | Architects and design-build teams working in Revit (BIM) |
| Status | **TO CONFIRM with Quotr** whether it is still offered, and on which plan. It was not found on the Autodesk App Store in a search. |
| Risk | Old Revit/architect descriptions on F6S, Crunchbase and LinkedIn make AI tools describe Quotr as "an AI assistant … Revit integration to help architects" (offsite notes §4). Keep it as a secondary feature, not the headline. |

**Questions buyers ask AI tools:**
- "Revit add-in for cost estimating"
- "How do I get a cost estimate from a Revit model?"
- "BIM to estimate software for architects"

### 3.7 Other integrations and security

- Integrations: the /faq/ answer says Quotr "easily integrates with popular design software and project management tools" but names none ([/faq/](https://quotr.ai/faq/)). No Procore App Marketplace listing was found. **TO CONFIRM with Quotr:** the list of live integrations.
- Security: one generic line, "industry-standard encryption" (llms.txt, /faq/). No security page, SOC 2 statement or data-retention policy was found. **TO CONFIRM with Quotr.**
- Why it matters: in a Dodge/CMiC survey of 235 contractors (published Dec 2025), the top AI concerns were data accuracy (57%) and security (54%) ([geo_content_playbook_b2b.md](<../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md>), §6; this survey was not re-checked in the fact-check).

### 3.8 ROI calculator

- Page: [/roi-calculator/](https://quotr.ai/roi-calculator/), also embedded on /software/. **Verified.**
- Inputs you can change: estimators on the team, bids per estimator each week, hours per takeoff today, and fully loaded hourly cost (live /software/, scraped 2026-09-25).
- The live calculator says: "we model an 80% cut in takeoff time, minus Lite per-seat cost" and "Figures are illustrative … Actual results vary by trade, plan complexity, and how your team works today." With its default inputs (2 estimators, 5 bids a week each, 6 hours per takeoff, $65/hour) it shows $160,322 estimated annual savings net of Lite, 48 hours saved a week, $13,360 monthly savings and "+40" extra bids a week.
- An older search-index copy of the page said "85% average reduction". The live figure is **80%**; the 85% version is stale.
- Good bottom-of-funnel asset. It is the only calculator on the site (no material or trade calculators).

### 3.9 Quotr Service (done-for-you estimating)

| Item | Detail |
|---|---|
| What it does | Quotr's team, using its own AI, produces takeoffs, cost estimates and pro formas for you. You send scope and drawings; you receive "decision-ready" outputs ([/service/](https://quotr.ai/service/)). |
| Process | A 6-step process on /service/. The search-index copy summarises it as: request and scope (share drawings, assumptions, timeline and material preferences) → Quotr processes the inputs → final report with cost breakdown is delivered (index-only). |
| Deliverables | Development cost estimate; deal-level financial pro forma; trade takeoffs. A "Sample deliverables" library of 9 documents, for example "All Trade Takeoff (Residential)", "Fast Cost Estimation (Residential LA Fire Rebuilding)", "HVAC Cost Estimation (Commercial)". 6 of the 8 visible samples are commercial. |
| How it links to the software | "Every Quotr Service engagement includes the software": results come back as a live, editable project inside Quotr (PDF markups and adjustable line items, "not a dead 500-row spreadsheet"), and the AI agent cites the exact sheet each count came from and flags likely missing scope (index-only text of the [electrical estimating services post](https://quotr.ai/blog/electrical-estimating-services/)). **TO CONFIRM with Quotr** that this applies to all Service jobs. |
| Coverage | "Currently spanning 26 sub-trades" (/service/ FAQ, 9 questions). Service posts cover both commercial work and residential work such as electrical takeoffs for tract and custom homes (index-only). |
| Price | $0.25/sq ft under 50,000 sq ft; $0.10/sq ft for 50,000+ sq ft; "Pricing is sent before we process your documents" (/pricing/, scraped 2026-09-25). **Verified.** /service/ also says pricing is "project-based". /pricing/ lists "Development cost estimates delivered in 3–4 business days; Pro formas delivered in 2–3 business days". |
| Turnaround | Conflicting: 3–4 business days (estimates) and 2–3 (pro formas) on /pricing/; "as fast as 24 hours" on homepage and /service/; 1–3 business days (llms.txt); 5–7 days (schema). See [entity-fact-sheet.md](entity-fact-sheet.md#4-inconsistency-register), row 3. |
| Named service offers in the blog | "Precon on Demand" (1–3 days); "Developer Desk: underwriting-grade estimates in 72 hours"; MEP, HVAC and electrical estimating services; California estimating services ([blog sitemap](https://quotr.ai/blog/sitemap.xml)) |
| Volume claims | "$1.2B+ in construction projects" estimated (Sep 24, 2026 post); "300+ projects a month, 4× faster" (blog teaser). Self-reported; no data published. |
| Proof | Sample deliverables; BiltWise ("developer-stage budgets", index-only). Quotr's service-pricing post is the **first citation** Perplexity uses for "outsourced estimating price per square foot", but the answer does not name Quotr (visibility tests C12, reproduced in the verification file). |

**Questions buyers ask AI tools:**
- "How much does it cost to outsource a construction estimate?"
- "Outsourced construction estimating service price per square foot"
- "Should I hire an estimator or outsource estimating?"
- "How long does a construction cost estimate take?"
- "Who can do a cost estimate for a multifamily project fast?"
- "How much does it cost to rebuild a house after the LA fires per square foot?" (Quotr sells an LA fire-rebuild estimate but was absent from this answer)
- "What is a construction pro forma and who can build one for me?"

### 3.10 Pro forma support

- Part of Quotr Service: "pro formas in 2–3 business days" (/pricing/, /software/).
- Blog coverage: [construction-proforma-software](https://quotr.ai/blog/construction-proforma-software/), "Quotr.ai vs. Aprao vs. Excel Spreadsheets" ([real-estate-pro-forma-software-comparison](https://quotr.ai/blog/real-estate-pro-forma-software-comparison/)), the-proforma-that-never-stops-changing.
- **TO CONFIRM with Quotr:** is pro forma a software feature, or only part of the service?

**Questions buyers ask AI tools:** "best real estate pro forma software", "how to build a development pro forma", "pro forma template for multifamily development".

### 3.11 Quotr Procurement (factory-direct materials)

| Item | Detail |
|---|---|
| What it does | A managed program that sources materials directly from factories in China. Quotr handles factory access, sampling, quality control, shipping, US customs, duties and final-mile delivery. The homepage calls it "A procurement program, not software or estimating services". |
| Contact | procurement@quotr.ai (given in the [construction procurement process post](https://quotr.ai/blog/construction-procurement-process/), search-index text) |
| Pricing model | DDP ("Delivered Duty Paid") = one price that covers factory cost, export packing, ocean freight, US customs and duties, final-mile delivery and certification documents (NFRC, CARB, cUPC) (index-only text of homepage and /procurement/). |
| Material categories | Windows and doors, garage doors, cabinetry and millwork, flooring, bath and plumbing fixtures (index-only). A cabinetry line named "QUOTR Framed Series" appears on /procurement/. **TO CONFIRM** the current category list. |
| Factories | "50+ audited manufacturers in Foshan & Guangdong" (homepage, /procurement/) vs "220+ vetted factories" (llms.txt, /disambiguation/). **Conflict — TO CONFIRM.** |
| Quote and delivery times | Quote: "typically … about 3–5 business days" (index-only text of quotr.ai pages; also "full quote in 3–5 days" in [how-developers-source-building-materials](https://quotr.ai/blog/how-developers-source-building-materials/), via competitor notes). Delivery: "typically within about 90 days" to the jobsite (index-only text of /contractors/), so "long-lead categories should be engaged early". Products are made to your specs, with video calls to review finished items before shipment. **TO CONFIRM with Quotr.** |
| Delivery area | Conflicting on the same page: "Final-mile delivery to your CA jobsite" vs "any US port or jobsite, coast to coast". **TO CONFIRM.** |
| Proof | Three project cards on /procurement/: Myren Dr, Saratoga ($97,000 vs $187K–$218K Bay Area market); Stratford Ct, Monte Sereno ($108,290 vs $195K–$245K); Skyfarm Dr, Hillsborough ($30,437 vs $58K–$76K). A product catalog PDF and a Saratoga Myren Dr case-study PDF. A 6-question FAQ. Claimed "40–55% average cost reduction per project". Live display bug: the three "Completed projects" cards show "Client saved ~$0" (the featured Myren Dr card shows "~$91,800"). |
| Who it is for | Developers and homebuilders (the three project examples are street addresses in Saratoga, Monte Sereno and Hillsborough, Bay Area towns; project type is not stated); contractors who supply finish materials |
| AI visibility | Perplexity names Quotr for "factory-direct … with AI takeoff and procurement" prompts that echo Quotr's own wording (1st in one run, 3rd on re-run), but **not** for plain buyer phrasing such as "where can US contractors buy cabinets, windows and flooring factory direct" (verification file, Contradiction #4). |

**Questions buyers ask AI tools:**
- "Where can US contractors buy cabinets, windows and flooring factory direct?"
- "How do I import building materials from China for a construction project?"
- "What does DDP mean for construction materials?"
- "How much can I save buying building materials direct from the factory?"
- "Are Chinese cabinets and windows up to US code? What certifications do I need (NFRC, CARB, cUPC)?"
- "How are 2026 tariffs affecting building material costs?"
- "Best construction procurement software 2026"

---

### 3.12 The live /software/ FAQ (8 questions, scraped 2026-09-25)

These are the questions Quotr already answers on its main product page. They are good seeds for AI-friendly FAQ content and for FAQPage schema (the page has no FAQPage markup today; see [../06-playbooks/schema-markup-kit.md](../06-playbooks/schema-markup-kit.md)).

1. How fast is AI takeoff with Quotr.ai?
2. How does AI construction takeoff work?
3. What makes Quotr.ai the best AI estimating software for contractors? (answer: "Most tools cover one stage; Quotr.ai owns the full bid-to-buyout workflow")
4. Does Quotr.ai support automated takeoff from PDF and image plans?
5. Does Quotr.ai support metric and imperial units?
6. Is procurement required to use Quotr.ai?
7. How much does Quotr.ai cost? (answer lists the current Lite/Plus/Enterprise prices and plan contents)
8. Does Quotr.ai work for electrical, HVAC, and other specialty trades?

Other live-page notes: the typo "Built for how contractors actually win x2 work" is still on the page; the comparison table "Traditional estimating vs Quotr.ai" covers takeoff, bid time, pricing, procurement, proposals, live sync, app stack and AI agent.

---

## 4. Supporting resources (not products, but part of the offer)

| Resource | URL | Count / detail | GEO note |
|---|---|---|---|
| Blog | [quotr.ai/blog/](https://quotr.ai/blog/) | 96 posts, most published Apr–Sep 2026 (peak 22–25 a month in May–June) | Largest content asset; see [../02-current-state/website-audit.md](../02-current-state/website-audit.md) |
| Construction dictionary | [quotr.ai/dictionary/](https://quotr.ai/dictionary/) | 55 terms (e.g. ai-takeoff, bid-leveling, scope-gap, markup-vs-margin, rfi, change-order, panel-schedule) | Short (~200 words each), no author, no sources |
| Tutorials | [quotr.ai/tutorials/](https://quotr.ai/tutorials/) | 6 (5 videos + 1 text guide) | Transcripts not verified |
| Case studies | [quotr.ai/case-studies/](https://quotr.ai/case-studies/) | 4: RL Electric, AlphaX, BiltWise Structures, Salisbury Moore | RL Electric page has no numbers |
| Trade pages | /software/trades/[trade]/ | 23 | Mostly thin |
| ROI calculator | [/roi-calculator/](https://quotr.ai/roi-calculator/) | 1 | Only calculator on the site |
| Sample deliverables | On [/service/](https://quotr.ai/service/) | 9 documents | Mostly commercial |
| FireTips (free LA fire-rebuild app) | [firetips.quotr.io](https://firetips.quotr.io/) | 1 (launched Feb 2025, per an EIN Presswire release found via WebSearch) | Rebuild steps, timelines and costs for LA fire victims; sits on the old quotr.io domain and is not linked from quotr.ai in the notes. A ready-made residential top-of-funnel asset |
| Procurement catalog and case-study PDFs | On [/procurement/](https://quotr.ai/procurement/) | 2 PDFs | |

---

## 5. Feature gaps and unknowns to raise with Quotr

1. What "Advanced AI" (Plus) adds over the "Basic AI agent" (Lite), and what the Plus "2,000 sq ft takeoff credits / month" can be used for.
2. Supported file types beyond PDF and images (DWG, Revit, CAD?).
3. Named integrations (Procore, QuickBooks, Excel, Bluebeam, others?) and export formats.
4. Security: encryption detail, SOC 2 status, data ownership, whether customer drawings are used to train models.
5. Status of the Revit add-in.
6. Whether "Smart Matching" (confidence-scored counting) is the official feature name, and which plans include it.
7. Whether pro forma is a software feature.
8. Service turnaround: standard and rush.
9. Procurement: categories, delivery area, lead times, minimum order size, warranty and returns.
10. Where the zip-code cost data comes from and how often it updates.
11. Confirm browser and Mac support in official product copy (blog posts say Quotr runs in any modern browser with no install; "best takeoff and estimating software for Mac users" was one of the test prompts, and Quotr was not named). Is there a mobile or tablet experience?

---

## Related pages

- [entity-fact-sheet.md](entity-fact-sheet.md) — canonical facts, profiles and naming rules
- [audiences-and-personas.md](audiences-and-personas.md) — who uses each product
- [positioning-and-proof-points.md](positioning-and-proof-points.md) — why Quotr is different and what proves it
- [../03-market/competitor-landscape.md](../03-market/competitor-landscape.md) — how rival products compare
- [../04-prompt-library/prompt-library.md](../04-prompt-library/prompt-library.md) — full list of buyer prompts to track
- [../04-prompt-library/construction-glossary.md](../04-prompt-library/construction-glossary.md) — construction terms explained
