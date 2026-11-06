# ICP 8 — Construction lenders, debt funds, their analysts, loan administrators and third-party cost reviewers (Quotr.ai)

*How this was researched (read first). Current-state date 2026-11-06, US only. About 22 web searches were run before the session's shared search limit ran out. Every attempt to open a page directly (fdic.gov, getbuilt.com, globest.com, eyeonhousing.org, biggerpockets.com) was blocked by the session's network policy. So **every external finding below comes from search-result excerpts, not from pages read in full.** Quotes are shown exactly as the excerpts gave them. Where an excerpt drew on several pages and the exact page is uncertain, the quote is marked "attribution probable". Quotr facts come only from the repo's audit files (`geo-brain/00-quotr/*`, `research_notes/Quotr GEO AEO strategy audit/*`). Anything simulated, estimated or from background knowledge is labeled. Method: the ICP-depth GEO framework (coding chain trigger → stage → mode → restraining force → prompt → proof; four forces; switch timeline; prompt matrix; geography-to-segment pipeline; distribution-based measurement).*

---

## A. Definition and size

### Takeaway
At June 30, 2026, US banks held **$453.5B of construction & development (C&D) loans**: flat on the quarter, down about 3.4% on the year, and tilted toward commercial, multifamily and land ($91.3B of it is 1–4 family). A private-lender market of **$70–153B a year** (depending on scope) sits alongside it, with residential transition (RTL/fix-and-flip/bridge) originations **up 13% year over year in Q1 2026**. Every one of these loans needs someone to say whether the borrower's budget is real. That job today is split across in-house construction teams, third-party plan & cost review (PCR) firms, and draw-management software. Built Technologies already sells an *AI* plan & cost review.

### Cited Findings
**Bank C&D book (FDIC call-report data, latest published quarter = Q2 2026; the Q3 2026 QBP is normally released in late November)**
- FDIC-insured institutions held **$453.5B** of C&D loans at June 30, 2026, flat for the quarter. Year-over-year decline is reported as 3.49% by one source and ~3.35% by another, so the sources conflict slightly — [FDIC QBP Q2 2026 PDF](https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-second-quarter-2026.pdf); [Construction Loans Tracker Q2 2026](https://commercialbuildersandcontractors.com/construction-lending-tracker/); [acren.ai Bank CRE Lending Trends Q2 2026](https://acren.ai/resources/bank-commercial-real-estate-exposure)
- NAHB/FDIC: total AD&C loans **$453.5B in Q2 2026**, up from $453.3B in Q1. 1–4 family residential construction & land development fell 0.4% to **$91.3B**. Loans 30+ days past due or nonaccrual fell to **$967.8M, 1.1%** of 1–4 family construction volume — [NAHB Eye on Housing, Aug 2026](https://eyeonhousing.org/2026/08/single-family-adc-lending-falls-back-in-q2/)
- Q1 2026: "other real estate development" (non-1–4 family) loans fell 1.8% to **$361.5B** — [NAHB Eye on Housing, Mar/Jun 2026](https://eyeonhousing.org/2026/03/adc-loan-volume-falls-despite-declining-financing-costs/)
- FDIC Q2 2026 industry past-due + nonaccrual rate **1.44%** (−9 bp QoQ). Non-owner-occupied CRE past-due/nonaccrual at banks >$250B fell for a 7th straight quarter to **3.08%** (peak 4.99% in Q3 2024). **"Smaller banks carry higher concentrations of these loans relative to assets and capital."** Reserve coverage 172.7% — [FDIC QBP Q2 2026](https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-second-quarter-2026.pdf); [FDIC Q2 2026 speech](https://www.fdic.gov/news/speeches/2026/fdic-quarterly-banking-profile-second-quarter-2026)
- **No clean Q2 2026 C&D noncurrent rate** could be read from the excerpts (the FDIC table text came back garbled). See Gaps.

**Concentration**
- Built Technologies (undated vendor blog): "out of nearly 4,760 banks, 763 have either CRE or construction loan concentration ratios that exceed these thresholds" (this combines the CRE and C&D tests) — [Built, "The 300% rule"](https://getbuilt.com/blog/the-300-rule-for-cre-construction-lending/)
- Named banks above 100% C&D-to-capital: **Bank OZK 118.2%, Provident Bank 190.3%** (GlobeSt, June 2026) — [GlobeSt](https://www.globest.com/amp/2026/06/09/cre-risk-builds-at-smaller-banks-as-giants-grow-cautious/). **Mid-America Bank 130.98%** (Q2 2026) — [BankRegReports](https://www.bankregreports.com/banks/mid-america-bank-919456/loans/)

**Private lenders (fix-and-flip, bridge, ground-up)**
- Geraci LLP (Feb 2026): US private money origination is about **$70–80B a year**, and DSCR lending may pass fix-and-flip within 2–3 years — [automateloandocs summary of Geraci stats](https://automateloandocs.com/pages/blog/private-lending-industry-statistics.html)
- Forecasa 2025 (broader scope): **288,525 loans (+5.4%), $153.1B (+9.1%)**. Vacant-land originations **+67% to 24,650 units** (a ground-up signal) — [SFR Analytics newsletter, Apr 2026](https://newsletter.sfranalytics.com/p/april-2026-private-lending-market)
- Q1 2026 private-lender originations **$29.7B (+4.0% YoY)**. **RTL +13.0% YoY**. DSCR $10.7B (−8.8%) — [SFR Analytics, Apr 2026](https://newsletter.sfranalytics.com/p/april-2026-private-lending-market). This conflicts with the Lightning Docs CEO, who called RTL roughly flat in 2026; his "more than $4 billion in monthly loan originations" covers one platform's users only — [Private Lender Link, Aug 2026](https://privatelenderlink.com/2026/08/the-state-of-private-lending-in-mid-2026-with-nema-daghbandan/)
- House flips fell from **407,417 (2022) to 297,045 (2025)** — [WeLend fix-and-flip benchmarks](https://www.welendllc.com/blog/fix-and-flip-loan-rates) (attribution probable; the excerpt pooled several private-lending pages)
- Single-lender data points: Lima One "$184.7M funded" in Q2 2026 (scope unclear; source page within the result set not confirmed — candidates [CrowdfundedWealth fix-and-flip lenders](https://www.crowdfundedwealth.com/articles/best-fix-and-flip-lender-2026), [SFR Analytics](https://newsletter.sfranalytics.com/p/april-2026-private-lending-market)). RCN Capital "$8.2B originated", 15-year track record — [CrowdfundedWealth RCN review](https://www.crowdfundedwealth.com/reviews/rcn-capital-review)
- Typical private construction loan size **$500K–$5M** (Geraci table) — [automateloandocs](https://automateloandocs.com/pages/blog/private-lending-industry-statistics.html) (attribution probable)

**Draw-management and budget-review vendors**
- Built serves "over 150 leading U.S. construction lenders, including U.S. Bank, Fifth Third Bank, and Citizens Bank" — [Growth Engineer profile of Built](https://growthengineer.ai/startups/built-technologies). Its AI partner says it handled "$100B+ in lending activity" — [MightyBot case study](https://mightybot.ai/blog/how-ai-agents-transformed-construction-lending-built-technologies/)
- **Built sells plan & cost review.** Its terms PDF (v10-22) defines it as "a third-party, pre-loan analysis of Client's construction project documents for omissions, discrepancies, and deviations from best practices" — [Built supplemental T&Cs, PCR](https://getbuilt.com/wp-content/uploads/2022/11/supplemental-tcs-plan-and-cost-review-v-10-22-3.pdf). Built now markets an **AI plan & cost review benchmarked on 389,649 completed construction projects**, "returned in 15 minutes" — [Built PCR blog](https://getbuilt.com/blog/plan-and-cost-review-construction-loans/)
- Other draw/loan-admin software: Land Gorilla (G2 4.8 from 30 reviews, per-loan pricing) — [G2](https://ai.g2.com/product/land-gorilla); [Software Advice](https://www.softwareadvice.com/loan-origination/construction-loan-manager-profile). Rabbet (per-draw pricing, SOC 2) — [Rabbet lender pricing](https://rabbet.com/lenders-pricing); [Software Advice AU](https://www.softwareadvice.com.au/software/693551/Rabbet-Construction-Lending)
- Named PCR / project-monitoring / draw-inspection firms found: Merritt Engineering — [merrittengineering.com](https://merrittengineering.com/plan-cost-reviews/). Innergy Integral (PNW and Southwest banks, credit unions, SBA lenders) — [Innergy Integral](https://integral-c94.pages.dev/resources/pre-construction-loan-review/). Partner Engineering & Science — [Partner ESI](https://www.partneresi.com/services/construction-progress-monitoring). Vertex — [Vertex](https://vertexeng.com/services/project-advisory/construction-monitoring/). Trinity — [Trinity](https://www.trinityonline.com/blog/tips-for-assessing-a-project-budget). LenderConsulting — [lenderconsulting.com](https://www.lenderconsulting.com/plan-specification-and-cost-review/). Millman National Land Service (draw inspections) — [Millman](https://millmanland.com/company-news/what-is-a-draw-inspection/). CFSI (fund control) — [thinkcfsi](https://www.thinkcfsi.com/the-construction-lenders-guide-to-fund-control/). AxisPointe and Ventavid (remote and video draw inspection) — [Ventavid](https://www.ventavid.com/blog/construction-draw-inspection)

**Roles that make up the buying unit**
- Lima One runs an **in-house construction team** that reviews the budget and the general contractor during underwriting — [Lima One new construction](https://www.limaone.com/new-construction-loans/)
- Built's reviews list its main users as "finance leaders, accounts payable teams, and construction administrators" — [Capterra Built](https://www.capterra.com/p/159434/Built/reviews/)

| Role | Where | What they own | Quotr fit |
|---|---|---|---|
| Underwriter / credit analyst | Private RTL & ground-up lenders, community/regional banks, debt funds | Pre-close budget sufficiency, LTC math, credit memo | **Core** (pre-close desk review) |
| Construction loan officer / RM | Banks | Origination speed vs. diligence; orders PCR | Influencer; speed buyer |
| In-house construction manager / "construction risk" | Larger private lenders (e.g., Lima One), banks | Budget & GC review, draw approvals | Buyer of a *tool* (Quotr Software) or overflow service |
| Construction loan administrator / draw admin | Banks, servicers, funds | Draw packages, G702/G703, inspections, retainage | Weak (Quotr has no draw product) |
| PCR / project-monitor firm reviewer | Third-party engineering/consulting firms | Signed PCR report, site visits, draw sign-off | **Potential channel/partner** (white-label takeoff) or competitor |
| Debt / development fund analyst | Private credit & RE debt funds, family offices | Screening many sponsor budgets fast | **Core** (fits "real estate development funds" on /disambiguation/) |

### Inferences
- Implied commercial/multifamily/land C&D in Q2 2026 is ≈ **$362B** ($453.5B − $91.3B; arithmetic, not a reported figure).
- The budget-review job splits into a **bank segment** (regulated, slow, vendor-panel, prefers signed third-party reports) and a **private-lender/fund segment** (speed, volume, smaller loans, often in-house). Quotr's desk-based, $/sq ft, 72-hour Service fits the second much better.
- Built's presence on both sides — draw software at 150+ lenders *plus* AI plan & cost review — makes it the incumbent Quotr would be compared against in AI answers about "AI construction budget review".

### Gaps
- Q2 2026 C&D **noncurrent rate** and the **2026 count of banks with C&D ≥100% of capital** were not retrievable. The 763/4,760 figure is undated and combines the CRE and C&D tests. Needs an FFIEC call-report pull (Schedule RC-C, item 1.a) by bank.
- No sizing found for the **draw-management software market**, the **number of PCR firms**, or **team sizes** per role.
- No market-wide **ground-up private construction volume** figure.

---

## B. Geography

### Takeaway
Geography matters less for this ICP than for consumer ICPs. Lenders buy nationally, and private RTL lenders (Kiavi, Lima One, RCN) lend in many states. Evidence does support **3–5 segments**, but only one or two justify geo pages: **California private lenders, including LA fire-rebuild loans**. Quotr has real local proof there (a Bay Area base, a California estimating post, an "LA Fire Rebuilding" sample deliverable), and the California Mortgage Association has just published a construction-loss case. The other segments are reached through topic pages and channels, not geo pages.

### Cited Findings
- C&D concentration is a **smaller-bank** issue: "Smaller banks carry higher concentrations of these loans relative to assets and capital" — [FDIC QBP Q2 2026](https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-second-quarter-2026.pdf)
- Named high-C&D banks: Bank OZK 118.2% and Provident Bank 190.3% of capital — [GlobeSt, June 2026](https://www.globest.com/amp/2026/06/09/cre-risk-builds-at-smaller-banks-as-giants-grow-cautious/). Mid-America Bank 130.98% — [BankRegReports](https://www.bankregreports.com/banks/mid-america-bank-919456/loans/)
- California private-lender trade body CMA published "A Broken Construction Project and A $750,000 Loss" (June 9, 2026). In that ground-up loan the borrower's self-prepared budget was never checked against the scope or a builder's budget — [CMA](https://www.californiamortgageassociation.org/2026/06/09/a-broken-construction-project-and-a-750000-loss/)
- Regional PCR supply exists: Innergy Integral serves banks, credit unions and SBA lenders in the **Pacific Northwest and Southwest** (e.g., a "Lender Advisory Services Seattle WA" page) — [Innergy Integral Seattle](https://integral-c94.pages.dev/markets/lender-advisory-services-seattle-wa/)
- Private lenders publish metro case studies (Lima One: Denver new construction) — [Lima One Denver](https://www.limaone.com/case-study/denver-co/). RCN Capital reviews carry a "Georgia" warning headline (content not retrieved) — [Real Estate Skills RCN review](https://www.realestateskills.com/blog/rcn-capital-review)
- Quotr local proof (internal): a "Fast Cost Estimation (Residential LA Fire Rebuilding)" sample deliverable and a "California estimating services" post — [product-and-features.md §3.9](../../geo-brain/00-quotr/product-and-features.md)

**Priority geo segments (evidence rows)**

| # | Segment | Evidence row (cited) | Job | Geo page? |
|---|---|---|---|---|
| 1 | **California private lenders + LA fire-rebuild construction loans** | CMA $750K loss case (2026); Quotr LA-rebuild sample; Quotr California estimating post; Bay Area base | "Is this rebuild/ground-up budget real at California costs?" | **Yes: one California lender page + one LA-rebuild budget-review page** (supply, cost levels and rebuild rules really do differ) |
| 2 | **Small-bank C&D concentrators (≥100% of capital)** — names so far: Bank OZK (AR), Provident (NJ), Mid-America Bank | GlobeSt/BankRegReports ratios; FDIC "smaller banks carry higher concentrations" | Independent budget check before credit committee; exam-ready file | **No.** Use a national "for community banks" page |
| 3 | **National RTL / ground-up private lenders** (Kiavi, Lima One, RCN, Builders Capital) | RTL +13% YoY Q1 2026; vacant-land loans +67% (2025); Lima One in-house budget review | High-volume scope-of-work/budget screening on small loans | **No.** Use a topic page ("fix-and-flip & spec-build budget review") |
| 4 | **PNW / Mountain West / Southwest community banks & SBA lenders** served by regional PCR firms | Innergy Integral's PNW/Southwest footprint | Faster/cheaper alternative or overflow for the local PCR firm | **No.** Channel/partner play |
| 5 | **Debt / development funds** (geo-agnostic, metro-heavy) | /disambiguation/ names "real estate development funds"; OCC SRP names private credit as an area to watch | Screen many sponsor budgets consistently | **No** |

### Inferences
- Applying the framework's pipeline to banks would mean: unit = bank (not county); layers = C&D/capital ratio, C&D growth, asset size (<$10B), state, noncurrent C&D, and RC-C 1-4 family share. A vendor-panel/"uses Built" flag would come from Built's public customer list. Score, take the top quartile, cluster by state and loan mix. This is about **4–6 analyst hours with FFIEC bulk data** (estimate).
- Background knowledge (not verified this session): Sun Belt states (GA, FL, TX, NC, TN, UT, AZ) have historically led housing starts and community-bank C&D concentration. Treat as a hypothesis until the call-report pull is done.
- Engines do not reliably inject geography into lender prompts. Put geography into persona facts in prompts and into data on pages. Do not build templated state pages.

### Gaps
- No state- or metro-level 2026 C&D-concentration table and no metro fix-and-flip/ground-up volume (ATTOM/Forecasa metro data not retrieved).
- The LA-fire-rebuild lending volume was not sourced this session.

---

## C. Jobs-to-be-done (in their words; synthesized, wording grounded in cited vocabulary)

### Takeaway
There are five jobs. Two are core for Quotr (pre-close budget sufficiency and fund-scale screening), one is adjacent (helping borrowers bring lender-ready budgets), and two are mostly out of scope (draw monitoring and the signed report itself).

### Cited Findings
- Lenders want "plans approved, and budgets complete with GC contracts before approving the financing" — BiggerPockets lender reply, excerpt (attribution probable to [BP "New Ground up Construction Loan Lender"](https://www.biggerpockets.com/forums/432/topics/1131567-new-ground-up-construction-loan-lender))
- PCR is "an independent assessment of a construction project's plans, specifications, and budget, conducted by a qualified third party before the construction loan closes" — [Innergy Integral](https://integral-c94.pages.dev/resources/plan-and-cost-review/)
- In the CMA loss case, the pre-construction review of budget vs. scope was skipped in underwriting — [CMA](https://www.californiamortgageassociation.org/2026/06/09/a-broken-construction-project-and-a-750000-loss/)
- Cost-to-complete logic: "if updated bids indicate that the remaining electrical scope will cost $275,000, the project already has a $75,000 shortfall" — [CFSI](https://www.thinkcfsi.com/the-construction-lenders-guide-to-fund-control/)

| # | Job (buyer's words — synthesized) | Who | Core for Quotr? |
|---|---|---|---|
| J1 | "Tell me if this $2.4M budget is real — quantities, not just $/sq ft — before credit committee on Thursday." | Bank underwriter, fund analyst | **Core** |
| J2 | "Screen 30 sponsor budgets this quarter with one consistent method, so I'm not trusting 30 different GCs." | Debt/development fund, RTL lender credit team | **Core** |
| J3 | "Make sure the scope of work and the line-item budget actually match before we fund a fix-and-flip or spec build." | Private RTL underwriter / in-house construction team | **Core** (small-loan economics) |
| J4 | "When a draw comes in over budget, tell me the real cost-to-complete before I advance another dollar." | Loan administrator, asset manager | Adjacent (re-estimate service, no site inspection) |
| J5 | "Give me a signed, independent report I can put in the file for the examiner/investor." | Bank credit admin, fund IC | **Not met today** (needs credentials, reliance, independence; see P) |

### Inferences
- J1–J3 are desk work from PDFs. That is exactly Quotr's AI takeoff + Service. J4 needs site verification Quotr does not offer. J5 is a trust and legal product, not an estimating one.

### Gaps
- No interview or community verbatims from *bank* underwriters were found. The wording is synthesized from vendor and lender pages. Validate with 6–12 switch interviews (framework protocol).

---

## D. Psychology

### Takeaway
This buyer's identity is **"the person who didn't miss it."** Blame avoidance and an examiner/IC audience outweigh speed in banks. In private RTL lending, speed-to-close competition pushes the other way. The robust biases to design for are **anchoring on the borrower's budget**, **status-quo/default vendor panels**, and **temporal landmarks** (credit-committee day, quarter-end, exam).

### Cited Findings
**Regulatory and exam pressure**
- The 2006 Interagency CRE Concentration Guidance still applies. Its C&D screen is 100% of Tier 1 capital plus the allowance for credit losses (the CRE screen is 300%), and the thresholds are "supervisory triggers, not limits" — [Resolve blog, 2026](https://resolvepay.com/blog/12-statistics-illustrating-concentration-risk-thresholds-lenders-watch); [Built "300% rule"](https://getbuilt.com/blog/the-300-rule-for-cre-construction-lending/)
- OCC Spring 2026 Semiannual Risk Perspective: "Credit risk within the federal banking system remains manageable in aggregate." Certain CRE segments' credit and refinancing risk "warrant ongoing monitoring". Private credit is named as an area to watch — [OCC SRP Spring 2026](https://www.occ.treas.gov/publications-and-resources/publications/semiannual-risk-perspective/files/pub-semiannual-risk-perspective-spring-2026.pdf); [RegReport, May 7, 2026](https://www.regreport.info/2026/05/07/new-ai-products-on-market-present-possible-risks-benefits-agency-advised-in-latest-risk-perspective/)
- NAHB: "This marks the eighteenth consecutive quarter that residential builders and developers have reported tightening credit conditions." NAHB net easing index −12.0 vs. the Fed's +3.7. AD&C effective rates were >0.6 pp above end-2025 — [NAHB, Aug 2026](https://eyeonhousing.org/2026/08/single-family-adc-lending-falls-back-in-q2/)

**Speed-to-close vs. diligence (private lenders)**
- An unclear scope of work or a first-time GC on a $1M project "will kill a deal faster than a lower credit score" — [Slate Financial, 2026](https://www.slatefinancial.io/blog/wp-ground-up-construction-loans-2026-spec-builders-without-bank)
- RCN is described as "willing to fund heavy construction budgets (100% of rehab costs) that other lenders are too scared to touch" — [Real Estate Skills](https://www.realestateskills.com/blog/rcn-capital-review) (third-party blog claim)
- "leading lenders conduct exhaustive due diligence before funding projects, confirming budgets, validating construction schedules" — [Scotsman Guide](https://www.scotsmanguide.com/news/private-capital-is-powering-new-construction-opportunities/)

**Reliance on the borrower's GC / in-house review**
- Lima One reviews the budget in-house and runs a GC review — [Lima One](https://www.limaone.com/new-construction-loans/)
- Experience gate: "most lenders would want 2-3 projects (buy, rehab, hold/sell, construction) experience usually in the last 3 years minimum" — BiggerPockets reply, excerpt (attribution probable to [BP "Construction Loans Lenders"](https://www.biggerpockets.com/forums/49/topics/1035974-construction-loans-lenders))

**Bias ranking (framework replication status → lender application)**

| Bias / effect | Replication status (framework) | How it shows up in this ICP | Design rule |
|---|---|---|---|
| Anchoring | Robust (Many Labs) | The borrower's budget anchors the underwriter. Reviews "adjust from" it instead of building bottom-up | Lead pages with **quantity-based independent number vs. borrower number** (variance table), not a reaction to the anchor |
| Defaults / status quo | Robust (d = 0.68) | Approved-vendor panels, "our PCR firm," "Built does it in our system" | Offer a **plug-in default**: a standard engagement letter, a one-page report format that drops into the credit memo, an API or Built/Rabbet-compatible export |
| Temporal landmarks | Robust (Dai, Milkman & Riis) | Credit committee day, quarter-end call report, exam start, fund close | Trigger-calendar content and outreach; "results before committee" SLA |
| Loss aversion / blame avoidance | Not in the framework's ranking — practitioner inference | "Nobody gets fired for using the engineering firm" | Named credentialed reviewer + liability terms + sample report beat "AI" claims |
| Generic social proof | Fragile | "Trusted by 100+ lenders" lines | Use **named** lender references and a methodology instead |
| Choice overload | Fragile (d ≈ 0.02) | Ignore | — |

**Hot vs. cold moments**

| Mode | Moment | Time cue |
|---|---|---|
| **Hot** | Credit committee in 48–72 hours and the budget looks thin; borrower threatening to go to a faster lender; draw request reveals an overrun; a loan in default needs cost-to-complete | Weekday evenings before committee; month/quarter-end |
| **Cold** | Building or refreshing the vendor panel; a fund launching a construction-lending strategy; exam prep/policy review; annual budget for loan-admin tools | Q4 planning, post-exam, post-fund-close |

### Inferences
- Bank buyers in hot mode still won't buy an *unknown* vendor overnight. Hot-mode wins go to whoever is already on the panel. So Quotr's hot-mode play is (a) private lenders and funds without panels and (b) "second opinion before committee," used *alongside* the formal PCR.
- The independence-and-credentials question is the decisive anxiety for banks (see E, P). AI speed alone triggers "is this defensible?" anxiety. Built addresses this directly with "supports the underwriter's decision instead of replacing it" (E).

### Gaps
- No 2026 OCC/FDIC exam findings specific to C&D budget review were retrieved. The OCC SRP text was not readable in full.
- Background knowledge, not verified this session: the 2015 Interagency Statement on Prudent Risk Management for CRE Lending, and the 2023 Interagency Guidance on Third-Party Relationships (vendor due diligence). Verify before citing on site.

---

## E. Four forces with verbatim quotes

### Takeaway
**Push** comes from slow draws and reviews and from budget/scope mismatches that cause real losses. **Pull** is fixed-price, minutes-to-days, AI-assisted review that fits the loan file. **Anxiety** centres on reviewer competence, defensibility and liability. **Habit** is in-house review, the existing PCR firm, and "GC contracts + contingency" as the proxy for budget quality. Most available verbatims are vendor/lender voices. Genuine bank-underwriter voice was not found (Reddit and LinkedIn were not retrievable).

### Cited Findings
| Force | Verbatim (as shown in search excerpt) | Speaker type | Source |
|---|---|---|---|
| Push | "The AI Draw Agent completes draw reviews in under 3 minutes and catches 2X more risks than manual review, which runs 5+ business days at most lenders." | Vendor (Built) | [Built AI draw review](https://getbuilt.com/blog/ai-draw-review-automation/) (attribution probable) |
| Push | "Some lenders have turnaround times of 2 weeks, other lenders are much faster." | BiggerPockets lender-member | [BP "Hard Money Draws on a reimbursement basis"](https://www.biggerpockets.com/forums/67/topics/994794-hard-money-draws-on-a-reimbursement-basis) (attribution probable) |
| Push | "if updated bids indicate that the remaining electrical scope will cost $275,000, the project already has a $75,000 shortfall" | Fund-control firm | [CFSI](https://www.thinkcfsi.com/the-construction-lenders-guide-to-fund-control/) |
| Push | "A Broken Construction Project and A $750,000 Loss" (title; the case is a skipped budget-vs-scope review) | CA private-lender trade body | [CMA, June 2026](https://www.californiamortgageassociation.org/2026/06/09/a-broken-construction-project-and-a-750000-loss/) |
| Push | "will kill a deal faster than a lower credit score" (about an unclear scope of work / first-time GC) | Private lender blog | [Slate Financial](https://www.slatefinancial.io/blog/wp-ground-up-construction-loans-2026-spec-builders-without-bank) |
| Pull | "An AI-powered review is priced differently: highly competitive, fixed pricing per file, returned in 15 minutes, at less than half the cost of a traditional review." | Vendor (Built) | [Built PCR blog](https://getbuilt.com/blog/plan-and-cost-review-construction-loans/) |
| Pull | "keeps everything in place for each loan & helps you get inspections & draws paid out quickly" | Lender-role reviewer of Built | [G2 Built reviews](https://www.g2.com/products/built/reviews) / [Capterra](https://www.capterra.com/p/159434/Built/reviews/) (page uncertain) |
| Pull | Built replaces "PDFs being e-signed and sent back and forth between all parties" | Lender-role reviewer | [G2 Built reviews](https://www.g2.com/products/built/reviews) / [Capterra](https://www.capterra.com/p/159434/Built/reviews/) (page uncertain) |
| Anxiety | "staff performing the draw inspection may lack the experience and training necessary to identify current or potential issues" | Lender consultancy | [LenderConsulting](https://www.lenderconsulting.com/plan-specification-and-cost-review/) |
| Anxiety | "A data-model review supports the underwriter's decision instead of replacing it." | Vendor (Built), pre-empting AI anxiety | [Built PCR blog](https://getbuilt.com/blog/plan-and-cost-review-construction-loans/) |
| Anxiety | "have not been overly impressed with it" · "not super user friendly" | Built users | [Capterra Built reviews](https://www.capterra.com/p/159434/Built/reviews/) |
| Anxiety | "Plan and cost review is a third-party, pre-loan analysis of Client's construction project documents for omissions, discrepancies, and deviations from best practices." (The terms also limit liability and disclaim warranties.) | Vendor terms | [Built PCR T&Cs](https://getbuilt.com/wp-content/uploads/2022/11/supplemental-tcs-plan-and-cost-review-v-10-22-3.pdf) |
| Habit | "Lima One's in-house team will review the budget to ensure it is sufficient and appropriate for the project in view." | Private lender | [Lima One](https://www.limaone.com/new-construction-loans/) (attribution probable) |
| Habit | "The budget that's submitted to the lender should have a contingency line item." | BiggerPockets reply | [BP "Hard Money Draw Question"](https://www.biggerpockets.com/forums/67/topics/1161974-hard-money-draw-question) (attribution probable) |
| Habit | "Hard-cost contingencies may only be reallocated to increases in hard-cost line items." | Trade press | [Scotsman Guide, Construction Lending 101](https://www.scotsmanguide.com/commercial/construction-lending-101/) |
| Habit | "Credit risk within the federal banking system remains manageable in aggregate." | Regulator (OCC) | [OCC SRP Spring 2026](https://www.occ.treas.gov/publications-and-resources/publications/semiannual-risk-perspective/files/pub-semiannual-risk-perspective-spring-2026.pdf) |

### Inferences
- Force → prompt class mapping for this ICP:
  - Push → "borrower budget looks low, how do I check it" / "draw over budget what to do"
  - Pull → "fast construction budget review service" / "AI plan and cost review"
  - Anxiety → "is AI cost review accepted by regulators/examiners" / "PCR firm vs AI" / "who signs the report"
  - Habit → "do I need a third-party cost review for a $1M spec loan" / "can I rely on the GC contract"
- Built has already written content for all four forces. Quotr has written for none.

### Gaps
- No r/CommercialRealEstate, r/RealEstate-finance or LinkedIn verbatims were retrievable. No American Banker or National Mortgage News 2026 quotes. BiggerPockets attributions need to be confirmed by opening each thread.

---

## F. Trigger events and trigger calendar

### Takeaway
The triggers are **deal-driven** (a thin budget before committee, a borrower switching lenders, a draw overrun, a default), **calendar-driven** (call reports, QBP releases, OCC risk reports, fiscal-year vendor reviews, spring flip season) and **news-driven** (losses like the CMA case, rate moves, tariffs).

### Cited Findings
- QBP Q2 2026 data was published by late August 2026 (the NAHB analysis is dated Aug 2026) — [NAHB](https://eyeonhousing.org/2026/08/single-family-adc-lending-falls-back-in-q2/)
- OCC Spring 2026 SRP was released around May 7, 2026 — [RegReport](https://www.regreport.info/2026/05/07/new-ai-products-on-market-present-possible-risks-benefits-agency-advised-in-latest-risk-perspective/). A fall edition was reported in mid-December 2025 — [RegReport, Dec 16, 2025](https://www.regreport.info/2025/12/16/occ-system-risk-report-emphasizes-innovation-economic-cyber-risks-eyed)
- AD&C borrowing costs rose (>0.6 pp above end-2025) in Q2 2026, and builders reported an 18th straight quarter of tightening — [NAHB](https://eyeonhousing.org/2026/08/single-family-adc-lending-falls-back-in-q2/). In Q1, NAHB titled its post "ADC loan volume falls despite declining financing costs" — [NAHB, Mar 2026](https://eyeonhousing.org/2026/03/adc-loan-volume-falls-despite-declining-financing-costs/)
- Loss news as a trigger: CMA's $750K case (June 2026) — [CMA](https://www.californiamortgageassociation.org/2026/06/09/a-broken-construction-project-and-a-750000-loss/)
- RTL volume up 13% YoY in Q1 2026 — [SFR Analytics](https://newsletter.sfranalytics.com/p/april-2026-private-lending-market)

| Window | Trigger | Who searches | Mode |
|---|---|---|---|
| Jan–Feb | Q4 call reports (background: due ~30 days after quarter-end); Q4 QBP (late Feb); spring flip acquisitions start | Bank credit; RTL lenders | Cold → hot as deals arrive |
| Mar–Jun | Spring/summer starts peak → new loans + first draws; OCC spring SRP (~May); Q1 QBP (~late May) | All | Hot (deal volume) |
| Jul–Sep | Draw volume peak; Q2 QBP (~late Aug); hurricane season cost shocks in Gulf/FL (speculative) | Loan admins, asset managers | Hot (draws/overruns) |
| Oct–Dec | Year-end closing rush; budget/vendor-panel planning; Q3 QBP (~late Nov); OCC fall SRP (~Dec) | Bank & fund leadership | Cold (panel, tools) + hot (year-end closings) |
| Event | Fed rate cut or rise (FOMC 8×/yr, background) → refinance & new-deal volume; tariff changes → budget repricing; a lender loss or default in the news; a regulator or LP asks for independent cost review; a fund closes a construction strategy | Everyone | Mostly hot |

### Inferences
- Raise prompt-tracking sampling and publish refreshed cost/variance data the week after each QBP release and each OCC SRP, and in March (spring deal ramp).

### Gaps
- No 2026 FOMC decision dates/outcomes were retrieved. No data on exam-cycle timing by bank. No seasonality data for "plan and cost review" search demand.

---

## G. Switch timeline with prompt form at each stage (framework stages)

### Takeaway
Prompts move from situational and vague ("borrower budget looks low") to category nouns ("plan and cost review firms", "AI construction budget review") to brand-and-objection prompts ("Built plan and cost review vs [firm]", "is Quotr independent").

| Stage | What's happening | Prompt form (examples) | Dominant force |
|---|---|---|---|
| First thought | A budget looks thin; a draw comes in over; the LP/examiner asks "who reviewed this budget?" | "borrower's construction budget seems low for a 12-unit townhome deal, how do I tell" | Push |
| Passive looking | Reading Scotsman Guide/AAPL/BP; noticing Built's AI review | "what does a plan and cost review include" · "how do lenders check a construction budget" | Push + pull |
| Active looking | Comparing options for this deal or for the panel | "plan and cost review firms for private lenders 2026" · "AI construction budget review vs third-party cost review" · "plan and cost review cost" | Pull vs. anxiety |
| Deciding | Validating credentials, liability, SLA, price, sample | "Built plan and cost review pricing" · "is an AI cost review acceptable to bank examiners" · "Quotr construction budget review sample report" | Anxiety + habit |
| Consuming / re-decision | Using it on deals; renews at panel review or after a miss | "how to reconcile third-party cost review with borrower budget variance" · "cost to complete estimate for stalled construction loan" | Habit (new default) |

### Inferences
- The re-decision interval for a *vendor panel* is long (annual or longer, inferred), so in-market share at panel level is small. The *per-deal* decision ("do I order a second opinion on this one?") recurs weekly at active lenders. That is where Quotr can win without a panel switch.

### Gaps
- Stage-specific verbatim prompts were not observed. They are synthesized from cited vocabulary.

---

## H. Current alternatives and what does not satisfy them

### Takeaway
The alternatives are **(1) traditional PCR/project-monitor firms**, **(2) Built's AI PCR + draw software**, **(3) in-house construction teams**, **(4) draw inspectors**, **(5) RSMeans/benchmark $/sq ft**, and **(6) trusting the GC contract + contingency**. Ranked by evidence count, the unmet needs are **turnaround**, **budget-to-scope reconciliation**, **cost on small loans**, **reviewer consistency/competence**, and **audit trail**. Early-stage drawings is likely but unevidenced.

### Cited Findings
| Alternative | Evidence | What fails |
|---|---|---|
| Traditional PCR / project monitor | Ordered pre-close, often passed to the borrower as a closing cost; price "variable, quote-based"; turnaround "days to weeks" — [Built PCR blog](https://getbuilt.com/blog/plan-and-cost-review-construction-loans/). A "small fraction of the loan amount" (vendor claim) — [Innergy Integral](https://integral-c94.pages.dev/resources/pre-construction-loan-review/) | No published prices; slow; uneconomic on small RTL loans (inference) |
| Built AI PCR | 389,649-project benchmark; 15 min; fixed per-file fee, less than half the traditional cost — [Built](https://getbuilt.com/blog/plan-and-cost-review-construction-loans/) | Benchmark-based (likely $/line-item comparison, not plan quantities — inference); tied to the Built ecosystem; no public price |
| In-house construction team | Lima One in-house budget + GC review — [Lima One](https://www.limaone.com/new-construction-loans/) | Capacity limits in volume spikes (inference) |
| Draw inspectors | $75–150 residential / $250–350 commercial (inspector price) — [Ventavid citing Millman](https://www.ventavid.com/blog/construction-draw-inspection); inspector competence concerns — [LenderConsulting](https://www.lenderconsulting.com/plan-specification-and-cost-review/) | Verify progress, not budget sufficiency |
| Benchmarks / RSMeans | AI answers for developer cost prompts cite RSMeans, Brookings, RAND, lender blogs — [repo visibility tests](../Quotr%20GEO%20AEO%20strategy%20audit/quotr_ai_visibility_tests.md) | $/sq ft can't catch scope omissions |
| Trust GC contract + contingency | "budgets complete with GC contracts" — [BP](https://www.biggerpockets.com/forums/432/topics/1131567-new-ground-up-construction-loan-lender); contingency line — [BP](https://www.biggerpockets.com/forums/67/topics/1161974-hard-money-draw-question) | The CMA $750K loss shows the gap — [CMA](https://www.californiamortgageassociation.org/2026/06/09/a-broken-construction-project-and-a-750000-loss/) |

**Unmet needs ranked by evidence frequency (count of independent sources in this research; a proxy, not a survey)**

| Rank | Unmet need | Evidence count | Sources |
|---|---|---|---|
| 1 | Turnaround (draws 5–10 business days / 2 weeks; PCR days–weeks) | 5 | Built ×2, BP ×2, Lendmire summary of BP ([Lendmire](https://www.lendmire.com/hard-money-draw-process-checks/)) |
| 2 | Budget ↔ scope reconciliation / omissions / shortfall | 5 | CMA, CFSI, Innergy ("budget shortfall" as the most common finding, paraphrase), BP scope-change thread, Built PCR T&C "omissions, discrepancies" |
| 3 | Cost (PCR fees opaque; draw fees $75–$1,000) | 4 | Built, Innergy, inspection-fee sources (I) |
| 4 | Reviewer competence / consistency | 2 | LenderConsulting; Capterra mixed reviews |
| 5 | Audit trail / document chaos | 2 | G2/Capterra lender reviews |
| 6 | Early-stage / incomplete drawings | 0 found | Inference from Quotr's "early-stage" positioning; validate |

### Inferences
- Quotr's credible wedge is **#2 + #1 + #3 on small and mid loans**: a *quantity takeoff from the actual plans* reconciled line by line to the borrower budget, in ~72 hours, at a published per-sq-ft price. No competitor in the retrieved set publishes a PCR price.

### Gaps
- No published dollar fee for traditional PCR was found (background expectation of roughly $1K–$15K+ by project size is **unverified; do not publish**).

---

## I. Willingness to pay, price anchors, who pays, procurement, sales cycle

### Takeaway
The anchors this buyer sees are draw inspections at **$75–$1,000 per visit**, PCR fees that are opaque and usually **passed to the borrower**, Built AI PCR at "less than half" of traditional, and per-loan/per-draw software. Quotr's published **$0.25/sq ft** maps to about **$700 for a 2,800 sq ft spec home** and **$3,500 for 14,000 sq ft**. That is competitive, but the tier boundary creates a cliff that must be clarified.

### Cited Findings
- Draw inspection fees: "$200 - $1,000 per inspection, dependent on location, cost of project and inspector assigned" (a lender disclosure); a bank fee sheet lists a $750 progress draw inspection fee; another lender charges $280 per draw paid to the inspection company; another says fees "range from $300 to $500 and are funded from the approved draw" — search excerpts drawn from [Hingham Savings](https://helpcenter.hinghamsavings.com/en/articles/2017159-construction-inspection-process), [Citizens Bank fee schedule](https://www.citizensbank.com/dam/6a53971d-329f-486d-911e-b42100cd8a1a/common-servicing-fees-original-file.pdf), [OfferMarket](https://www.offermarket.us/blog/what-is-the-draw-request-process-for-offermarket-capital-construction-loans) (which figure belongs to which page is not confirmed)
- Inspector-side pricing: residential $75–150, commercial $250–350 (Millman, via a 2026 vendor blog citing a 2020 release) — [Ventavid](https://www.ventavid.com/blog/construction-draw-inspection); a Minnesota inspector forum poster: lenders "typically they are willing to pay $50 to $75" — [InterNACHI](https://forum.nachi.org/t/draw-inspection-how-to-how-much/241713)
- Who pays: PCR is often passed to the borrower as a closing cost — [Built](https://getbuilt.com/blog/plan-and-cost-review-construction-loans/). Draw inspections: Millman says the lender pays — [Millman](https://millmanland.com/company-news/what-is-a-draw-inspection/); a sample loan agreement says the borrower pays the inspector's fees — [Law Insider](https://www.lawinsider.com/clause/construction-inspector) (conflict: it varies by lender)
- Software: Rabbet prices per draw; GetApp lists a "starting price of US$107.50" (scope unclear) — [Rabbet pricing](https://rabbet.com/lenders-pricing); [GetApp](https://www.getapp.com/finance-accounting-software/a/rabbet-for-construction-lenders). Land Gorilla per-loan, with a "$25.00 one time" listing (unverified) — [Software Advice](https://www.softwareadvice.com/loan-origination/construction-loan-manager-profile). A Built case cites "$50K annual cost generating $2.5M in value" (unverified) — [Growth Engineer](https://growthengineer.ai/startups/built-technologies)
- Vendor due diligence: Rabbet advertises SOC 2 compliance — [Software Advice AU](https://www.softwareadvice.com.au/software/693551/Rabbet-Construction-Lending). Quotr has no security page or SOC 2 statement ("industry-standard encryption" only) — [product-and-features.md](../../geo-brain/00-quotr/product-and-features.md)
- Quotr Service price: $0.25/sq ft under 50,000 sq ft; $0.10/sq ft above; "Pricing is sent before we process your documents" — [product-and-features.md §3.9](../../geo-brain/00-quotr/product-and-features.md)

**Price arithmetic (Quotr published rates; calculation)**

| Project | Quotr Service | Compare |
|---|---|---|
| 2,800 sq ft spec home | ~$700 | Roughly 1–3 draw inspections at the $200–$1,000 lender-billed range |
| 14,000 sq ft (12-unit townhomes) | ~$3,500 | Traditional PCR: unpublished |
| 49,000 sq ft | ~$12,250 | **Cliff:** 51,000 sq ft at $0.10 = ~$5,100 if the lower rate applies to the whole area. **TO CONFIRM with Quotr** how the tier applies |

### Inferences
- The payer is usually the **borrower** (via closing costs). The buyer is the **lender**. So price sensitivity is lower than the per-file fee suggests, and the real currency is **turnaround and defensibility**.
- Bank procurement will require third-party-risk due diligence (security, financials, insurance, BCP). Background knowledge: the 2023 Interagency Third-Party Risk Management guidance. Expect a multi-month bank sales cycle versus days to weeks for private lenders and funds (speculative; no data).

### Gaps
- No PCR fee schedules, no Built AI PCR dollar price, no sales-cycle data, no data on how often lenders absorb versus pass through PCR fees.

---

## J. Vocabulary list

| Term | Meaning in this ICP (short) |
|---|---|
| LTC (loan-to-cost) | Loan ÷ total project cost; the budget review directly drives it |
| LTV / LTARV / ARV | Loan-to-value; loan-to-after-repair-value (fix-and-flip) |
| Hard cost / soft cost | Physical construction vs. fees, permits, design, financing |
| Contingency (hard/soft) | Reserve line; may only be reallocated within the same class — [Scotsman Guide](https://www.scotsmanguide.com/commercial/construction-lending-101/) |
| Draw schedule / draw request | Staged disbursements tied to completed work |
| Schedule of values (SOV) | Line-item breakdown of the contract sum used for draws |
| AIA G702 / G703 | Application and Certificate for Payment / Continuation Sheet (draw forms) |
| Retainage | % withheld from each draw until completion |
| Plan and cost review (PCR) / "plan, spec and cost review" | Pre-close third-party review of plans, specs and budget — [Innergy Integral](https://integral-c94.pages.dev/resources/plan-and-cost-review/) |
| Project monitor / construction monitor / construction consultant | Lender's third-party rep for PCR + draw sign-off — [Vertex](https://vertexeng.com/services/project-advisory/construction-monitoring/) |
| Budget review / feasibility review / cost-to-complete | Sufficiency check pre-close; re-forecast mid-project — [CFSI](https://www.thinkcfsi.com/the-construction-lenders-guide-to-fund-control/) |
| Interest reserve | Budgeted interest funded from the loan |
| Fund control | Third-party disbursement control — [CFSI](https://www.thinkcfsi.com/the-construction-lenders-guide-to-fund-control/) |
| Scope of work (SOW) | Fix-and-flip/ground-up line list submitted with the budget — [Lima One](https://www.limaone.com/construction-draw-process-explained/) |
| RTL / DSCR | Residential transition loan (fix-and-flip/bridge/ground-up) / debt-service-coverage rental loan — [SFR Analytics](https://newsletter.sfranalytics.com/p/april-2026-private-lending-market) |
| C&D / AD&C concentration (100% / 300%) | Supervisory screening ratios — [Resolve](https://resolvepay.com/blog/12-statistics-illustrating-concentration-risk-thresholds-lenders-watch) |
| Reliance letter, E&O | Lets the lender rely on a third-party report; professional liability cover (industry terms; no source retrieved) |
| Gap / shortfall / "in balance" | Remaining funds < cost-to-complete → borrower must re-balance (industry term) |

---

## K. Channels

### Takeaway
The channels are trade press and associations for private lenders (**AAPL, CMA, Scotsman Guide, Private Lender Link, SFR Analytics, Geraci**), bank-staff forums (**BankersOnline, MyComplianceResource**), **BiggerPockets** lender forums, review sites (**G2/Capterra** construction-lending categories), and the NAHB AD&C data stream. Bank channels (RMA, ABA, ICBA, MBA CREF) are background knowledge only.

### Cited Findings
- AAPL publishes market articles — [AAPL "From New Frontier to Established Markets"](https://aaplonline.com/articles/market-trends/from-new-frontier-to-established-markets)
- CMA publishes loss case studies — [CMA](https://www.californiamortgageassociation.org/2026/06/09/a-broken-construction-project-and-a-750000-loss/)
- Scotsman Guide runs construction-lending how-tos — [Scotsman Guide](https://www.scotsmanguide.com/commercial/walk-the-constructionloan-tightrope/)
- Private Lender Link interviews — [Private Lender Link](https://privatelenderlink.com/2026/08/the-state-of-private-lending-in-mid-2026-with-nema-daghbandan/). SFR Analytics newsletter (Glenn Hull) — [SFR Analytics](https://newsletter.sfranalytics.com/p/april-2026-private-lending-market)
- Bank staff discuss construction inspection fees on BankersOnline — [BankersOnline](https://bankersonline.com/forum/ubbthreads.php/topics/2086917/inspection-fees-construction-loans) — and MyComplianceResource — [MCR forum](https://mycomplianceresource.com/forums/topic/disclosure-on-construction-inspection-fees/)
- BiggerPockets forums 67/49/432 host hard-money and construction-lender threads — [BP](https://www.biggerpockets.com/forums/67/topics/1159424-private-and-hard-money-lender-rehab-draw-requirements)
- G2/Capterra list Built, Land Gorilla, Rabbet, BankLabs Construct — [G2](https://www.g2.com/products/banklabs-construct/reviews)
- NAHB AD&C Financing Survey — [NAHB](https://www.nahb.org/news-and-economics/housing-economics/indices/adc-financing-survey)

### Gaps
- No podcast or LinkedIn creator list was retrieved. RMA/ABA/ICBA/MBA channel fit was not verified.

---

## L. Proof required at each stage

| Stage | Proof the buyer needs | Quotr has it today? |
|---|---|---|
| First thought / passive | A clear method explainer: what a budget review checks (quantities, unit costs, scope gaps, contingency, soft costs) with a worked variance example | No (Developer Desk post is product-led) |
| Active | Sample **redacted lender report**; turnaround SLA; published price; comparison vs. PCR firm / Built AI / in-house | Partial: price yes; SLA conflicting (24h / 72h / 3–4 days / 5–7 days); no lender sample |
| Deciding (private/fund) | Named reviewer with credentials (e.g., PE, ASPE CPE, AACE CCP — background knowledge); 2–3 lender/fund references; accuracy back-test vs. actual costs | No |
| Deciding (bank) | All of the above + engagement letter addressed to the lender, **reliance letter**, **E&O/professional liability certificate**, **independence/conflict policy**, security/SOC 2, financial stability | No |
| Consuming | Consistent format that drops into the credit memo; audit trail (sheet-level citations: Quotr's agent "cites the exact sheet each count came from" — index-only, TO CONFIRM) | Partial |

---

## M. Coding chains (trigger → stage → mode → restraining force → exact prompt → proof)

| # | Trigger (datable) | Stage | Mode | Restraining force | Exact prompt (synthesized) | Proof required |
|---|---|---|---|---|---|---|
| M1 | Credit committee Thursday; the sponsor's $2.4M budget is 18% below the analyst's $/sq ft gut check | Active | **Hot** | Habit ("our PCR firm takes 3 weeks, so we'll just rely on the GC contract") | "I'm a credit analyst at a community bank. A borrower's $2.4M budget for 10 townhomes looks low. How can I get an independent budget check from the plans in 2–3 days?" | Turnaround SLA, sample variance report, price |
| M2 | Private RTL lender's volume up ~13% YoY; the in-house construction team is backlogged | Active | Hot (recurring) | Anxiety ("outsourced reviewer won't know our standards") | "We're a private lender doing 40 fix-and-flip and spec loans a month and our construction team can't keep up with scope-of-work reviews. Who offers outsourced budget review for lenders?" | Consistent template, per-file price, references from lenders |
| M3 | Draw #4 reveals the electrical line 30% over; the borrower asks to reallocate contingency | Consuming | Hot | Anxiety ("is the whole budget wrong?") | "Borrower's draw shows electrical 30% over budget and they want to use contingency. How do I estimate cost-to-complete on a construction loan?" | Cost-to-complete method, re-estimate from plans, fast SLA |
| M4 | Fund LPs or IC ask "who independently reviewed construction budgets?" after a peer's loss (e.g., the CMA case) | Passive → active | Cold | Anxiety (defensibility) | "What's the standard for independent construction cost review for a real estate debt fund, and what does a plan and cost review report include?" | Methodology page, credentialed reviewer, sample report, liability terms |
| M5 | Bank exam scheduled; C&D at 120% of capital | Active | Cold | Habit (existing vendor) + anxiety (examiner acceptance) | "Do bank examiners accept AI-assisted construction cost reviews, or do we need an engineer's plan and cost review?" | Clear statement of what Quotr is/isn't; partner engineer sign-off; examiner-friendly report |
| M6 | Borrower pushes to close in 10 days or go to a faster lender | Deciding | **Hot** | Habit (PCR SLA) | "fastest plan and cost review for a ground-up construction loan" | 72-hour SLA, price, sample |
| M7 | Fund launching a construction-lending strategy; building a vendor panel | Active | Cold | Anxiety (vendor risk) | "Best plan and cost review and construction monitoring firms for a new construction debt fund in 2026, compare Built, engineering firms and AI options" | Comparison page, SOC 2/security, insurance, references |
| M8 | LA fire-rebuild loan; borrower's budget built on pre-fire costs | Active | Hot | Anxiety (local cost levels) | "Is $425 per square foot realistic for a Pacific Palisades rebuild? I'm underwriting a construction loan and need an independent budget check." | LA cost data, local sample report |

All chains are synthesized from the cited triggers and vocabulary and must be validated in interviews (framework threshold: ≥3 of 12 interviews or ≥5 of 50 posts).

---

## N. Prompt matrix

**Demand tier = labeled estimate** (no GSC, Keyword Planner or Profound data was pulled. Tiers are based on population size from A and observed content-pool density from O). Engine = which to track first (ChatGPT; Google AIO/AI Mode; Perplexity where noted).

### Full-context first-person prompts (12)
| ID | Prompt | Intent | Stage | Urgency | Mode | Engine | Expected fan-out nodes | Tier (est.) |
|---|---|---|---|---|---|---|---|---|
| F1 | "I'm a credit analyst at a $1.5B community bank in North Carolina. A sponsor's $6.2M budget for 24 townhomes looks thin and credit committee is Thursday. How do I get an independent construction budget review from the plans fast?" | choose-provider | Active | Acute | Hot | ChatGPT, AIO | plan and cost review firms · turnaround · cost · AI budget review · Built · 2026 | 3 |
| F2 | "We're a private lender doing ~40 fix-and-flip and ground-up loans a month nationally; our in-house construction team is backlogged on scope-of-work reviews. Who offers outsourced construction budget review for lenders, and what does it cost?" | choose-provider | Active | Recurring | Hot | ChatGPT | outsourced budget review lenders · price · best · Built · in-house vs outsource | 3 |
| F3 | "As an analyst at a real estate debt fund screening 30 multifamily sponsor budgets a quarter, what tools or services give a consistent independent hard-cost check?" | compare | Active | Recurring | Cold | ChatGPT, Perplexity | AI construction cost estimating for underwriting · RSMeans · Built · best · 2026 | 2 |
| F4 | "Our borrower's draw shows electrical 30% over budget on a $3M spec build and they want to use contingency. How should a lender estimate cost-to-complete?" | diagnose/learn | Consuming | Acute | Hot | ChatGPT, AIO | cost to complete construction loan · contingency reallocation · draw inspection | 3 |
| F5 | "I'm a construction loan officer at a regional bank. Do examiners accept AI-assisted plan and cost reviews or do we need an engineer-signed PCR?" | validate/trust | Deciding | Exploratory | Cold | ChatGPT | OCC/FDIC guidance · interagency CRE guidance · plan and cost review requirements | 2 |
| F6 | "A borrower wants to close a ground-up loan in 10 days and our PCR firm quotes 3 weeks. What's the fastest credible plan and cost review option?" | choose-provider | Deciding | Acute | Hot | ChatGPT, AIO | fastest plan and cost review · AI · Built 15 minutes · price | 3 |
| F7 | "I underwrite construction loans for a California private lender. How do I check whether a borrower's $1.1M budget for a 2,800 sq ft spec home in Sacramento is realistic?" | diagnose/learn | Active | Acute | Hot | ChatGPT, AIO | cost per sq ft California 2026 · budget review checklist · RSMeans | 3 |
| F8 | "We're launching a construction-lending debt fund in 2026. Compare plan and cost review firms, Built's AI review and in-house construction managers for a vendor panel." | compare | Active | Exploratory | Cold | ChatGPT, Perplexity | best plan and cost review firms · Built vs · project monitoring · SOC 2 | 2 |
| F9 | "I'm underwriting a Pacific Palisades fire-rebuild construction loan; the budget says $425/sq ft. Is that realistic and who can review it independently?" | local + choose-provider | Active | Acute | Hot | ChatGPT, AIO | LA rebuild cost per sq ft 2026 · fire rebuild construction loan · budget review LA | 2 |
| F10 | "I'm a construction loan administrator. What should I check in a G703 continuation sheet against the original budget before approving a draw?" | do | Consuming | Recurring | Cold | AIO | G702 G703 · schedule of values · retainage · draw checklist | 3 |
| F11 | "As a hard money underwriter, what are the most common things missing from fix-and-flip scope-of-work budgets?" | diagnose/learn | Passive | Exploratory | Cold | ChatGPT, AIO | scope of work template lender · rehab budget mistakes · contingency % | 3 |
| F12 | "Our bank's C&D loans are over 100% of capital. What independent budget-review process will hold up in our next exam?" | validate/trust | Active | Exploratory | Cold | ChatGPT | interagency CRE concentration guidance · construction loan administration · PCR | 2 |

### Short category prompts (6)
| ID | Prompt | Intent | Stage | Mode | Tier (est.) |
|---|---|---|---|---|---|
| S1 | "plan and cost review cost" | compare/price | Active | Cold | 3 |
| S2 | "third-party construction cost review for lenders" (= repo E-086) | choose-provider | Active | Cold | 3 |
| S3 | "AI construction budget review for lenders" | choose-provider | Active | Hot | 2 |
| S4 | "how to check a developer's construction budget as a lender" (= repo L-141) | learn | Passive | Cold | 3 |
| S5 | "how much contingency should a construction budget have lender" (= repo L-142) | learn | Passive | Cold | 4 |
| S6 | "best plan and cost review firms 2026" | choose-provider | Active | Cold | 2 |

### Brand prompts (3)
| ID | Prompt | Intent | Watch for |
|---|---|---|---|
| B1 | "Quotr construction budget review for lenders" | validate | Is Quotr described as a lender/fund service; namesake confusion (Quotr Pro); pricing accuracy |
| B2 | "Quotr vs Built plan and cost review" | compare | Whether Quotr is named at all; claims about independence |
| B3 | "Is Quotr.ai independent / who reviews Quotr estimates" | trust | Reviewer credentials, conflicts (procurement line) |

---

## O. Simulation

### O1. SIMULATED ChatGPT conversation (not a real run; written to show the likely journey and fan-out)
*Persona: Dana, credit analyst, $1.5B community bank, Charlotte NC; C&D ≈115% of capital; deal: 24 townhomes, $6.2M hard-cost budget; committee Thursday. ChatGPT memory holds: "works in commercial lending at a community bank in Charlotte."*

1. **Dana:** "Sponsor's budget for 24 townhomes is $6.2M hard cost, about $172/sq ft. Feels low for Charlotte in 2026. How do I sanity-check it before Thursday?"
   **SIMULATED answer:** walks through $/sq ft benchmarks, citing RSMeans and NAHB-type sources; suggests comparing to recent comps and checking contingency (5–10%); recommends a third-party plan and cost review. *Likely fan-out:* "townhome construction cost per square foot Charlotte 2026", "plan and cost review construction loan".
2. **Dana:** "Our PCR firm quotes 2–3 weeks. Faster options?"
   **SIMULATED answer:** names Built's AI plan & cost review ("results in minutes"), regional engineering/PCR firms, draw-inspection firms, and possibly "AI estimating tools"; caveats about examiner acceptance. *Fan-out:* "fast plan and cost review AI", "Built plan and cost review", "best plan and cost review firms 2026". **Quotr likely absent** (no lender page exists).
3. **Dana:** "I only have the PDF plan set and the sponsor's line-item budget. Can anything do a takeoff and compare line items?"
   **SIMULATED answer:** this is the node where AI takeoff tools (Togal, STACK, Quotr) *could* appear, but framed for contractors, not lenders. *Fan-out:* "AI takeoff from PDF plans", "construction estimating service per square foot".
4. **Dana:** "Would an examiner accept that versus an engineer's report?"
   **SIMULATED answer:** generic: PCR isn't specifically mandated, but sound risk management under interagency CRE guidance expects qualified independent review; suggests using AI output as a supplement. *Fan-out:* "interagency guidance construction loan budget review", "OCC construction lending handbook".
5. **Dana:** "Give me a shortlist with prices and turnaround."
   **SIMULATED answer:** Built (price "contact"), named PCR firms ("quote-based"), draw inspectors ($75–$1,000). **Opening:** a vendor with a *published* price and SLA (Quotr's $0.25/sq ft, 72 h) would be uniquely quotable here, *if* a lender-facing page existed.

### O2. Retrieval proxy — real WebSearch runs (2026-11-06). **Retrieval proxy, not an AI engine answer.**
| # | Sub-query run | Top domains | Brands named | Quotr? | Winning format |
|---|---|---|---|---|---|
| R1 | plan and cost review fee construction lender third-party cost review price | getbuilt.com (PCR T&C PDF), integral-c94.pages.dev (Innergy Integral), globest.com (2011), merrittengineering.com, djc.com; noise from gov permit fee tables | Built, Innergy Integral, Merritt Engineering | No | Vendor service pages/terms; **no price published anywhere** |
| R2 | "plan and cost review" construction lender typical fee $ turnaround days | getbuilt.com ×2, lendoor.com, ledgertc.com, fedlaws.org, amerisave.com | Built | No | Vendor blog with a traditional-vs-AI comparison |
| R3 | draw inspection fee construction loan per inspection cost | hinghamsavings.com, citizensbank.com, bankersonline.com, mycomplianceresource.com, millmanland.com, offermarket.us, forum.nachi.org | Millman, Hingham Savings, Citizens | No | Bank fee disclosures + practitioner forums |
| R4 | Built Technologies AI plan and cost review launch lenders budget review automated | getbuilt.com ×4, mightybot.ai ×2, growthengineer.ai | Built, MightyBot | No | Vendor news + blog with hard numbers (15 min, 389,649 projects) |
| R5 | project monitoring services lender construction consultant firms … plan and cost review | partneresi.com ×4, integral-c94.pages.dev ×5, vertexeng.com, trinityonline.com, globest.com, lexisnexis.com | Partner ESI, Vertex, Innergy Integral, Trinity, Bureau Veritas | No | Engineering-firm service pages |
| R6 | Rabbet construction draw management software reviews pricing lenders | rabbet.com, getapp/capterra/softwareadvice (many), credaily.com | Rabbet | No | Pricing page + directories |
| R7 | Land Gorilla construction loan software pricing per loan reviews | capterra (×10 locales), softwareadvice, getapp, g2 | Land Gorilla | No | Review directories |
| R8 | Kiavi / Lima One / RCN / Builders Capital construction budget feasibility review requirement | limaone.com ×3, crowdfundedwealth.com ×3, realestateskills.com ×2, newsilver.com, lynkmortgage.com | Lima One, RCN, Kiavi | No | Lender's own product pages + affiliate review blogs |
| R9 | Scotsman Guide private lender construction budget review draw management cost overruns | scotsmanguide.com ×5, getbuilt.com, trinityonline.com, thinkcfsi.com | Built, Trinity, CFSI | No | Trade-press how-tos (dated 1–4 years) |
| R10 | r/CommercialRealEstate construction loan lender third-party cost review budget sponsor | cappartnersinc.com, creativeglobalfundingservices.com, terrapincg.com, contracts.justia.com, sec.gov | — (no Reddit returned) | No | Broker checklists + loan-agreement exhibits |

### O3. Gap verdict per prompt cluster
| Cluster | Prompts | Who owns the pool today | Quotr gap | Verdict |
|---|---|---|---|---|
| Learn: what is PCR / how to check a borrower budget | F7, F11, S4, S5 | Engineering-firm pages, Built blog, Scotsman Guide (old), broker checklists | Absent; no method page | **Winnable**: thin, dated pool; a dated, evidence-dense method page with a worked variance example can enter |
| Price/turnaround of review | S1, F6, F2 | **Nobody publishes a price**; Built says "less than half" | Absent but holds the only published price | **Highest-leverage white space**: a transparent price + SLA page |
| AI / tool comparison | S3, F3, F8, B2 | **Built** (15 min, 389,649 projects) | Absent | Contested. Needs a fair comparison page + third-party mentions; won't out-rank Built on "AI PCR" alone |
| Trust/regulatory | F5, F12 | Regulator PDFs, Built governance blog | Absent; and Quotr can't claim examiner acceptance | Answer honestly ("supplement, not substitute, unless engineer-signed"). Low conversion, high trust value |
| Draw monitoring / G703 | F4, F10 | Built, Rabbet, Land Gorilla, Millman, bank fee pages | No product | **Skip** except cost-to-complete re-estimate (F4) |
| Local cost levels (CA/LA rebuild) | F7, F9 | RSMeans, cost blogs (Meltplan/Exayard in prior audit) | Has LA-rebuild sample + CA post | **Winnable** with original $/sq ft data from Service jobs |

---

## P. GEO system for this ICP

### Takeaway
Build **one lender/fund hub, one independent budget-review service page (urgent version), one methodology + sample report (considered version), one fair comparison page, and 5–6 answer pages**. Lead with the white space no one fills: **published price + SLA + quantity-based variance report**. But do not claim "independent third-party review" until the independence, credential and liability gaps below are closed.

### Owning pages (titles and slugs)
| Page | Slug | Mode | Core content / proof |
|---|---|---|---|
| Hub: "Construction budget review for lenders and debt funds" | /lenders/ | Both | Who it's for (private RTL, ground-up, community banks, debt funds); jobs J1–J4; links |
| Service (urgent): "Construction budget review from plans in 72 hours — $0.25/sq ft" | /lenders/construction-budget-review/ | **Hot** | 40–60-word answer; SLA; price table with worked examples; upload CTA; one named reviewer; one sample excerpt |
| Methodology (considered): "How Quotr reviews a borrower's construction budget" | /lenders/budget-review-methodology/ | Cold | Takeoff → unit costs → line-item variance → scope-gap flags → contingency/soft-cost checks; limitations (no site visit; not an appraisal; not engineer-sealed unless partnered); data sources; update date |
| Sample report: "Sample lender budget review (redacted, 24-unit townhomes)" | /lenders/sample-budget-review-report/ | Cold | Downloadable PDF + HTML summary table |
| Comparison: "Plan and cost review options for lenders, 2026: engineering firms vs Built AI review vs in-house vs desk review" | /lenders/plan-and-cost-review-options/ | Cold | Fair table (turnaround, price transparency, site visits, signed report, best for). Not a self-ranked "best" list |
| California/LA: "LA fire-rebuild construction budget review for lenders" | /lenders/la-fire-rebuild-budget-review/ | Hot | Local $/sq ft ranges from Quotr jobs (TO CONFIRM data), rebuild scope pitfalls |
| Answer: "What is a plan and cost review (PCR)?" | /blog/what-is-a-plan-and-cost-review/ | Cold | Definition, what it checks, who orders, who pays |
| Answer: "How lenders check a borrower's construction budget (checklist)" | /blog/how-lenders-check-construction-budget/ (maps L-141) | Cold | 12-point checklist |
| Answer: "How much contingency should a construction budget carry? (lender view)" | /blog/construction-contingency-lender-requirements/ (L-142) | Cold | Ranges with sources |
| Answer: "Cost-to-complete on a construction loan: how to re-estimate mid-project" | /blog/cost-to-complete-construction-loan/ | Hot | Method + re-estimate offer |
| Answer: "Fix-and-flip scope of work: the 10 items lenders most often find missing" | /blog/fix-and-flip-scope-of-work-lender-review/ | Cold | Original data from Service jobs if available |
| Answer: "Hard vs soft costs in a construction loan budget" | /blog/hard-vs-soft-costs-construction-loan/ (L-135) | Cold | Glossary-plus |

### Proof assets and original data (ranked by citation ceiling)
1. **"Borrower Budget Gap Report" (semiannual):** anonymized median variance between sponsor budgets and Quotr takeoff-based estimates, by trade and project type. Requires Quotr's job data and a published method (the "$1.2B+ estimated" claim has no method today). Highest ceiling. Scotsman Guide/AAPL/CMA are plausible pick-ups (inference).
2. Redacted sample report + one-page methodology PDF.
3. Named reviewer bios with credentials, plus a partner engineer if one is added.
4. Back-test: Quotr estimates vs. final costs on N completed projects (TO CONFIRM data exists).
5. Security page (encryption, data ownership, training policy, SOC 2 status or roadmap).

### Off-site placements ranked by leverage per hour (estimates)
| Rank | Placement | Why | Effort |
|---|---|---|---|
| 1 | Contributed article to **Scotsman Guide** (commercial/private lending) on "reading a borrower's budget against the plans" with a worked variance table | Scotsman pages already surface in R9; the content pool is 1–4 years old | 6–8 h |
| 2 | **AAPL** and **CMA** article/webinar (CMA just ran a budget-review loss case) | Direct private-lender audience; California fit | 4–6 h each |
| 3 | **BiggerPockets** lender/hard-money forums: disclosed answers on SOW/budget review | BP threads surface for borrower-side and lender-side prompts | 1 h/week, 3–6-month play |
| 4 | Partnership/integration pitch to **Rabbet / Land Gorilla** (neither shows a PCR product in this research; Built has one) | Places Quotr in the loan-admin workflow and their content | 4 h + BD time |
| 5 | **Private Lender Link** / SFR Analytics newsletter interview | Niche, credible, retrievable | 2–3 h |
| 6 | BankersOnline / MyComplianceResource answers (bank staff) | Hard to promote; low volume | Low priority |
| 7 | G2/Capterra listing in a lender-relevant category | Only if Quotr Software is positioned for lender analysts | Defer |

### Refresh cadence
- Service/price/SLA page and comparison page: **monthly** (price and competitor claims move).
- Budget Gap Report: **semiannual**, timed one week after the Q4 and Q2 QBP releases (late Feb / late Aug).
- Answer pages: quarterly. LA rebuild page: quarterly with new job data.

### Tracking prompts to freeze (run daily or 3×/week, ChatGPT + Google AIO/AI Mode; report cluster-level mention/citation/recommendation rates with ± ranges over ≥3 periods)
1. F1 (community bank, thin budget, Thursday committee)
2. F2 (private lender, outsourced SOW/budget review)
3. F6 (fastest credible PCR)
4. S1 "plan and cost review cost"
5. S2 "third-party construction cost review for lenders"
6. S3 "AI construction budget review for lenders"
7. F9 (LA fire-rebuild budget check)
8. B2 "Quotr vs Built plan and cost review" (brand group, reported separately)

### Do / skip / ignore
- **Do:** lender hub + urgent service page + methodology + sample report; publish price and **one** SLA (fix the 24h/72h/3–4d/5–7d conflict first); resolve the $0.10/$0.25 tier cliff wording; a fair comparison page; Scotsman/AAPL/CMA placements; Budget Gap original data; a California/LA-rebuild page; an independence policy.
- **Skip:** draw-management/G703 content beyond one answer page (no product); state pages for banks; "best plan and cost review firms" self-ranked listicle; claiming examiner acceptance; llms.txt/schema as a lever (framework).
- **Ignore:** chasing Built on "AI draw review"; generic "trusted by lenders" lines without named references; Claude/Copilot tracking for this ICP (framework engine priority).

### Honest assessment: does Quotr Service meet lender requirements today?
**No. It is a good fit for private lenders' and funds' *desk second opinion*, but not for a bank-grade *independent plan and cost review*.**

| Requirement (lender view) | Quotr today (from repo audit) | What it would need |
|---|---|---|
| Independence (engaged by and reporting to the lender; no borrower conflict) | Service is sold to developers/GCs (borrowers); Quotr Procurement sells materials to project teams, a potential conflict | Lender-engaged product line; a conflict policy (no review of budgets Quotr prepared or projects it supplies) |
| Named, credentialed reviewer / sign-off | None stated for Service | Named reviewers (e.g., CPE/CCP/PE — background knowledge) or a partner engineering firm that signs |
| Liability: E&O and reliance letter | Not disclosed | Professional liability cover; reliance-letter template |
| Site verification (draws, progress) | None (desk-based) | Partner with draw inspectors, or scope explicitly to pre-close desk review + cost-to-complete |
| Consistent SLA | Conflicting (24h/72h/1–3d/3–4d/5–7d) | One SLA + rush tier |
| Security / vendor due diligence | "Industry-standard encryption" only; no SOC 2 | Security page; SOC 2 roadmap (Rabbet advertises SOC 2) |
| Sample lender report & method | None for lenders | Publish both |
| Price transparency | **Yes** ($0.25/$0.10 per sq ft) — a real differentiator | Clarify the tier boundary; offer a per-file flat fee for small RTL loans to match Built's "fixed pricing per file" framing |

**Positioning options (inference):** (a) a "pre-committee desk budget review" for private lenders and funds; (b) a partnership with a PCR/engineering firm, with Quotr doing takeoff/estimate and the partner signing; (c) a borrower-side "lender-ready budget package" (fits current Service and persona 4) marketed to lenders as "ask your borrower for one" (not independent, but it raises budget quality at intake).

---

## Q. Known / likely / speculative

| Claim class | Known (cited) | Likely (inference, label it) | Speculative (validate first) |
|---|---|---|---|
| Market size | C&D $453.5B (Q2 2026); 1–4 family $91.3B; PD/NA 1.1% of 1–4 family; private origination $70–80B (Geraci) vs $153.1B (Forecasa, broader); RTL +13% YoY Q1 2026; flips 297,045 (2025) | Commercial/MF/land C&D ≈ $362B; private market growth concentrated in RTL and ground-up | Count of banks with C&D ≥100% in 2026; number of PCR firms; team sizes |
| Competition | Built sells PCR (T&C 2022) and AI PCR (15 min, 389,649 projects, < half the cost); Built serves 150+ lenders; Rabbet per-draw + SOC 2; Land Gorilla per-loan, G2 4.8/30 | Built is the default AI answer for "AI plan and cost review" | Built's actual AI PCR price; whether its AI uses plan quantities |
| Prices | Draw inspections $75–$1,000 range (multiple sources); PCR fee often passed to the borrower; Quotr $0.25/$0.10 per sq ft | Borrower pays most PCR fees, so the lender buys on speed and defensibility | Traditional PCR $1K–$15K+ (background, unverified) |
| Psychology | Interagency thresholds are screening triggers; OCC: CRE segments warrant monitoring; NAHB: 18 quarters of tightening; anchoring/defaults/temporal landmarks are robust (framework) | Blame avoidance dominates banks; speed dominates private RTL | Examiner attitudes to AI-assisted reviews |
| Geography | Smaller banks hold higher CRE concentrations; Bank OZK 118.2%, Provident 190.3%; CMA loss case (CA); Innergy serves PNW/Southwest | California/LA rebuild is Quotr's best geo spoke | Sun Belt ranking of C&D concentration (needs call-report pull) |
| AI visibility | Quotr absent in all 10 retrieval-proxy runs; nobody publishes a PCR price; prior audit: RSMeans/benchmark pages win developer cost prompts | Price + SLA page is the fastest entry; Scotsman/AAPL/CMA placements shift ChatGPT | Simulated conversation content (O1) — must be tested with real runs |
| Quotr readiness | Service is borrower-facing; SLA conflict; no SOC 2; no lender sample | Fits private lenders/funds as a desk second opinion | Lenders would accept Quotr without an engineer partner |

### Gaps (overall)
- Search budget was exhausted and direct page fetches were blocked. No Reddit/LinkedIn verbatims; no 2026 C&D noncurrent rate; no state-level concentration table; no PCR fee schedule; no interview data. Next steps: an FFIEC bulk call-report pull (RC-C) for B; open the BiggerPockets/CMA/Built pages to confirm quote attribution; 6–12 switch interviews with private-lender underwriters and fund analysts recruited through AAPL/CMA/BP; real ChatGPT/AIO runs of the 8 frozen prompts (3–5 runs each) to replace the O1 simulation.
