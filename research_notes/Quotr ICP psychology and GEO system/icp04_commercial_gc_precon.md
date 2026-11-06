# ICP 4 — Preconstruction Manager / Chief Estimator at a Mid-Market Commercial GC ($20M–$1B revenue): ICP-depth dossier and GEO system for Quotr.ai

**As of:** 2026-11-06 · **Scope:** US · **Method:** the uploaded ICP-depth GEO framework (coding chain trigger → stage → hot/cold mode → restraining force → prompt → proof; four forces; switch timeline; prompt matrix; geography-to-segment pipeline; distribution-based measurement), applied to the commercial GC precon buyer.

**Read this first: research limits in this pass.**
- The session's shared WebSearch budget ran out after ~22 searches, and WebFetch could not reach g2.com, capterra.com, reddit.com, constructconnect.com or census.gov (DNS/policy blocks in this sandbox). So:
  - **Verbatim quotes below are snippet-level**: they were returned as quoted text by the search engine from the cited page. I could not open the pages to confirm the reviewer, date or full wording. Each is tagged "snippet". Verify on-page before using any quote in public copy.
  - **No Census CBP/SUSB current counts, no ConstructConnect/Dodge state rankings, no subreddit member counts** could be pulled. Those are listed as gaps with the exact table/route to fill them.
  - Section O(2) uses the ~11 research searches I actually ran as the retrieval proxy, because a dedicated fan-out batch could not be run after the budget ran out.
- Facts from Quotr's own files come from `/home/user/quotr/geo-brain/00-quotr/` and the GEO audit notes (cited as local files). Facts from earlier audit notes keep the original external URLs those notes recorded.
- Labels used: **Known** = sourced; **Likely** = strong inference from sourced facts; **Speculative** = hypothesis to validate; **Estimate** = modelled number with stated assumptions; **Simulated** = invented for illustration.

---

## A. Definition and size

### Takeaway
The buyer is the person who owns the number before buyout: a preconstruction manager, director of precon or chief estimator at a commercial/institutional GC (NAICS 236220) that sits roughly between the SBA small-business line ($45M) and the lower half of the ENR Top 400 (No. 400 ≈ $250M; No. 150 ≈ $870M). Current Census counts could not be pulled. An older SUSB baseline plus ENR anchors put the ICP at **roughly 4,000–7,000 firms (estimate)**. Each firm has a precon team that likely runs 2–10 people, and base pay is about $110K–$140K for a precon manager and $160K–$270K for a chief estimator or VP of precon.

### Cited Findings
**Firm universe and size anchors**
- An archived Census SUSB table (pre-2007 NAICS 23622, commercial building construction) lists **39,790 firms**. **17.6%** had 20+ employees, **2.2%** had 100+ and **0.4%** had 500+. A later archived vintage shows **40,490 firms** with 18.1% / 2.4% / 0.4%. These are mid-2000s data, the only firm-size split retrieved — [UNT archive of Census SUSB](https://webarchive.library.unt.edu/eot2008/20080917233023/http:/www.census.gov/epcd/susb/latest/us/US23.HTM); [later vintage](https://webarchive.library.unt.edu/eot2008/20090506200249/http:/www.census.gov/epcd/susb/latest/us/US23.HTM)
- The SBA size standard for NAICS 236220 is **$45M** in average annual receipts over the three most recent fiscal years. One source lists a proposed revision, so check the current figure — [naicslist SBA table](https://naicslist.com/naics/sba-size-standards); [samsearch 236220](https://samsearch.co/naics-ai-lookup/236220-commercial-and-institutional-building-construction)
- **18,162** federal contractors are registered under NAICS 236220. This is a SAM registration count, not a firm census — [fed360](https://www.fed360.agency/contractors/naics/236220) / [sweetspot](https://www.sweetspot.so/markets/federal/naics/236220/) (the summary did not pin which of the two)
- The 2023 County Business Patterns vintage (2017 NAICS) was released June 26, 2025. It holds the current 236220 establishment counts by state and metro, but it was not retrievable here — [Census release](https://www.census.gov/newsroom/press-releases/2025/2023-county-business-patterns.html)
- ENR 2026 Top 400 (2025 revenue): total revenue rose **11.8% to $671.4B** — [Construction Dive](https://www.constructiondive.com/news/top-commercial-contractors-revenue-2026-enr/820930/); [ENR preview](https://www.enr.com/toplists/2026-Top-400-Contractors-1-preview)
- Bottom of the list: RNGD ranked **No. 394 with $253M** in 2025 revenue — [NOLA Newswire](https://nolanewswire.com/2026/05/rngd-named-to-2026-top-400-general-contractors-list-by-enr/). Wagman ranked No. 345 — [Wagman](https://www.wagman.com/?p=10617)
- Middle of the list: Branch ranked **No. 150 with >$870M** — [Construction Owners](https://www.constructionowners.com/news/branch-climbs-to-no-150-on-enr-top-400-contractors-list). Rogers-O'Brien (Texas) climbed **43 spots to No. 74** — [press release](https://smb.tryondailybulletin.com/article/Rogers-OBrien-Construction-Climbs-43-Spots-to-74-on-ENRs-2026-Top-400-Contractors-List/6a1d58fa004597ee6ba13e70)

**Pay** (the bands are recruiter- or pay-site-sourced, so treat them as directional)
- Preconstruction manager base pay is **$115K–$135K** nationally. Senior managers with department scope earn **$145K–$177K+** (The Birmingham Group, a recruiter) — [TBG](https://thebirmgroup.com/preconstruction-manager-salary/)
- Salary.com (April 2026): P25 **$108,300**, P50 **$122,405**, P75 **$133,922** — [Salary.com](https://www.salary.com/research/salary/posting/pre-construction-manager-salary)
- Payscale's 2026 average is **$104,027** — [Payscale](https://www.payscale.com/research/US/Job=Pre-Construction_Manager/Salary)
- Chief Estimator / VP Preconstruction base is **$161,280–$268,780** (P20–P80, six US regions; the upper end reflects the Northeast) — [TBG estimator salary guide](https://thebirmgroup.com/2025-construction-estimator-salary-trends-a-deep-dive-into-senior-chief-estimator-pay/)

**Role definition from job postings**
- A mid-size Fort Worth GC is hiring a precon director to "guide conceptual estimating, budgeting, GMP development, cost planning, and constructability efforts" (snippet) — [Michael Page](https://www.michaelpage.com/job-detail/director-preconstruction-mid-size-fort-worth-gc/ref/jn-102026-7125271)
- A Phoenix-area precon director posting asks the hire to develop conceptual budgets "with minimal input" and to build detailed estimates without relying on subcontractor pricing. The search summary did not pin which result carried this posting; candidates are [Mediabistro](https://www.mediabistro.com/jobs/3541039271-director-preconstruction) and [CSG Talent](https://www.csgtalent.com/jobs/job/preconstruction-director-17066/)

### Inferences
- **ICP firm count (estimate).** Assume commercial GC revenue per employee is about $0.75–1.5M (an unsourced assumption, because subs do most of the work). Then $20M revenue ≈ 15–25 employees, and $1B ≈ 700–1,300 employees.
  - On the SUSB shares, firms with ≥20 employees are about 7,000–7,300 (2000s).
  - Some of those are construction managers or design-builders below $20M.
  - Plausible ICP range: **~4,000–7,000 firms**.
- **ENR slice.** About 250–270 ENR Top 400 firms fall between ~$250M and ~$1B (roughly ranks 130–400). Not all of them are commercial GCs.
- **Seat count (estimate).** At 2–10 precon or estimating staff per firm, that is **~10,000–50,000 seats**. Range check:
  - **Speculative:** team size is unmeasured.
  - **Likely:** the low end (2–4 people) is typical for $20–100M GCs; dedicated precon departments of 6–15 are typical for $300M+.
- **Cost of capacity.** A precon manager at about $122K base × ~1.3 load (assumption) ≈ $160K a year, or about $77/hour. One senior estimator equals the cost of ~13 Quotr Service SD budgets on 40,000 sf jobs ($0.25 × 40,000 = $10,000 each), or ~44 Plus seat-years ($299.90 × 12 = $3,599). This arithmetic is the core of the "precon capacity without headcount" story.
- **Salisbury Moore.** Quotr's files describe it only as an "active commercial estimating customer" (search-index text) — [local entity fact sheet](/home/user/quotr/geo-brain/00-quotr/entity-fact-sheet.md). Its firm type (GC, sub or developer) is not established, so **do not present it as a GC reference until Quotr confirms**.

### Gaps
- **Current firm counts.** 2022 SUSB/Economic Census counts of 236220 firms by receipts size, and 2023 CBP establishments by state, could not be pulled. census.gov is blocked in this sandbox. Route: `api.census.gov/data/2023/cbp?get=ESTAB,EMP,PAYANN&for=state:*&NAICS2017=236220`, plus SUSB 2022 "receipts size" tables.
- **ENR No. 400 cutoff.** The exact 2026 cutoff was not found. ~$250M is inferred from RNGD at No. 394.
- **AGC membership.** Not retrieved this pass. AGC boilerplate commonly cites ~6,500 GC members (background knowledge; verify on agc.org).
- **Team size.** No sourced precon team sizes by revenue band. This needs FMI or recruiter data, or Quotr interviews.

---

## B. Geography: where the ICP is and where to point content

### Takeaway
In 2026 nonresidential growth is a data-center story. Starts are up strongly year to date, while lodging, office and retail are weak. Multifamily recovered. Without current state rankings (a gap), the defensible segments are:
1. Texas Triangle
2. Data-center and megaproject corridors (including the Louisiana and New Mexico megasites seen in 2026 Dodge data)
3. Southeast growth metros
4. California/Bay Area (Quotr's home market, cost- and regulation-distinct)
5. NY/Northeast (largest metro volume, union, highest precon pay)

Geo pages are justified only for cost or regulatory differences (prevailing wage, union vs open shop, state codes). Metro-templated pages are not justified.

### Cited Findings
**Market direction 2026**
- Dodge, September 2026: total starts fell 1.5% to a **$1.33T** annual rate. Nonresidential building was still **up 23.7% YTD**, while offices and data centers together fell 21.4% that month — [inside.lighting, Oct 26, 2026](https://inside.lighting/news/26-10/construction-starts-cool-growth-persists)
- Through August 2026, total starts were **+15.2% YTD**, and **commercial and industrial starts +47.7% YTD**, "powered largely by data centers" — [inside.lighting, Sep 28, 2026](https://inside.lighting/news/26-09/construction-starts-retreat-recent-peak)
- Megaprojects in Dodge monthly data:
  - the **$12.8B "Project Jupiter" data center in New Mexico** (July 2026)
  - a **$3.5B Amazon data center in Louisiana** (August 2026)

  Sources: [inside.lighting Aug 2026](https://inside.lighting/news/26-08/construction-growth-reveals-divided-market); [inside.lighting Sep 2026](https://inside.lighting/news/26-09/construction-starts-retreat-recent-peak) (the summary did not pin which item carried which project)
- "Without data centers, nonresidential construction would be down by 12.7%" (headline, April 2026) — [Planetizen](https://www.planetizen.com/news/2026/04/137339-without-data-centers-nonresidential-construction-would-be-down-127)
- Regional fragments: one Dodge item shows the **South Central region −24.6%** in a month, and another shows the Midwest +3.0% May→June. No state or metro ranking was retrieved — [inside.lighting July 2026](https://inside.lighting/news/26-07/june-construction-starts-fall-nearly-20)
- Multifamily starts rose **12.7%** over the 12 months ending May 2026 — [FloorDaily / Dodge](https://www.floordaily.net/?p=83148)
- The AIA consensus (January 2026) expected nonresidential building spending to rise only about **2%** in 2026, with data centers as the main driver — [LightNOW](https://www.lightnowblog.com/2026/01/2026-construction-forecast/)
- AGC/Sage 2026 Outlook (951 respondents, Nov–Dec 2025):
  - data centers had the strongest net reading, **+57%** (65% expect an increase, 8% a decline)
  - respondents were most pessimistic about **lodging, private office and retail**
  - about **70%** were affected by tariffs

  Sources: [ACHR News](https://www.achrnews.com/articles/165679-data-center-demand-immigration-crackdowns-and-ai-shape-a-mixed-outlook-for-construction-in-2026); [Sage](https://www.sage.com/en-us/blog/2026-construction-industry-outlook/)
- The latest metro ranking retrieved is Dodge's 2022 data: **New York $37.1B (No. 1), Dallas $16.7B (No. 2, +51%)** in commercial plus multifamily starts — [Construction Dive](https://www.constructiondive.com/news/2022-top-10-metros-construction-starts/641780)
- AGC input costs rose **8.9%** from August 2025 to August 2026 (via the prior audit) — [AGC](https://www.agc.org/news/2026/09/10/construction-input-costs-climb-89-between-august-2025-and-august-2026-association-survey-finds-war)
- Chief-estimator pay is highest in the Northeast — [TBG](https://thebirmgroup.com/2025-construction-estimator-salary-trends-a-deep-dive-into-senior-chief-estimator-pay/)

### Inferences — priority geo segments (evidence rows; fill the blanks with CBP and Dodge state data)

| # | Segment | Evidence row (sourced) | Missing evidence to add | Job emphasis | Geo page? |
|---|---|---|---|---|---|
| 1 | **Texas Triangle open-shop mid-market GC** (DFW, Houston, Austin–San Antonio) | Dallas No. 2 metro in 2022 starts ($16.7B); Rogers-O'Brien +43 ENR spots; Fort Worth mid-size GC hiring a precon director for conceptual/GMP work | 2023 CBP 236220 establishments for TX; 2026 Dodge TX starts | High-volume negotiated multifamily, healthcare, K-12, data-center support buildings; speed of SD budgets | **Maybe**: one "Texas commercial construction cost context" page only if Quotr has TX job data |
| 2 | **Data-center and megaproject corridor GC** (support buildings, fit-out, site packages) | C&I starts +47.7% YTD driven by data centers; $12.8B NM and $3.5B LA projects; AGC net +57 for data centers; existing Quotr prompt "how to estimate MEP costs on a data center project" (L-146) | Which mid-market GCs win packages on hyperscale campuses (likely as trade/package GCs, not prime) | MEP-heavy conceptual pricing ($/MW is not a GC-level metric for most mid-market firms); schedule-compressed bid days | **Topic page, not geo page**: "Data center fit-out conceptual estimating" |
| 3 | **Southeast growth-metro GC** (Atlanta, Carolinas, Nashville, Florida, Gulf South incl. New Orleans) | RNGD (Louisiana) at No. 394 ($253M) shows the ICP band; $3.5B Louisiana data center | CBP counts; Dodge metro data for 2025–26 | Multifamily, healthcare and education; hard-bid public work | No (national pages carry it) |
| 4 | **California / Bay Area GC** (Quotr home market) | Quotr already publishes a California estimating-services post (local) and has Bay Area project references | Prevailing-wage and union cost deltas; CA starts | High labor rates, public-works prevailing wage, code-driven costs | **Yes, one page**: costs genuinely differ; Quotr has local proof |
| 5 | **NY / Northeast union-market GC** | NY No. 1 metro (2022, $37.1B); highest chief-estimator pay band | Current Dodge NY data; union wage tables | Union-rate conceptual budgets; owner/cost-consultant reconciliation | Later, only with NY job data |

- **Likely:** geo pages pay off through facts in the content (labor basis, prevailing wage, union rates, local cost indices), not through engines adding city names. That matches the framework's finding that no engine reliably injects location unless it is stated or remembered.
- **Likely:** the strongest geo lever for this ICP is the **persona facts inside prompts** ("$150M GC in Dallas, open shop"). So national pages must carry labor-basis variants (open shop vs union vs prevailing wage) as explicit facts and tables.

### Gaps
- State and metro rankings of nonresidential starts and spending for 2025–2026 (Dodge, ConstructConnect, Census VIP) were not retrieved. Census VIP publishes national private nonresidential spending, not state.
- Union density by state for construction (BLS union membership tables) and the list of state prevailing-wage laws were not retrieved. The federal Davis-Bacon Act (federally funded work over $2,000) is background knowledge; verify before use.
- Manufacturing megaproject regions (e.g., semiconductor fabs in AZ, TX, NY, OH) are background knowledge only; there are no 2026 status figures.

---

## C. Jobs-to-be-done (in their words)

### Takeaway
There are five jobs. Each is phrased the way the buyer would say it, and each is anchored in contract language, job postings or reviews.

### Cited Findings
- Contract language puts the conceptual estimate on the GC or CM at SD: "For the Schematic Design Phase, the Construction Manager shall prepare a quantity take-off cost estimate based on building systems, assemblies, components, etc., and update periodically." (snippet) — [Law Insider clause samples](https://www.lawinsider.com/clause/construction-estimates) / [Law Insider "estimating"](https://www.lawinsider.com/clause/estimating/_3) (not pinned to one page)
- Contract language also requires an early warning: "Advise the Owner if it appears that the Construction Cost Estimate may exceed the Project budget, and make recommendation for corrective action." (snippet) — same Law Insider pages
- Best practice is to set the first total project budget at the end of SD, when drawings are about 20% complete — [DCD](https://dcd.com/articles/budgeting-and-cost-estimating-for-construction-projects/)
- Precon director postings ask for conceptual budgets "with minimal input" and for "conceptual estimating, budgeting, GMP development, cost planning, and constructability" — [Michael Page](https://www.michaelpage.com/job-detail/director-preconstruction-mid-size-fort-worth-gc/ref/jn-102026-7125271)
- Bid leveling takes "anywhere from a day to 2-3 days depending on the project," according to an r/estimators user quoted by a third-party blog (snippet; blog not pinned) — [imagetotable.ai](https://imagetotable.ai/blog/batch-subcontractor-quotes-bid-comparison) / [Archdesk](https://archdesk.com/blog/guide-to-subcontractor-bid-leveling)

### Inferences (JTBD statements; wording is Likely, built from the sources above)
1. **"Give the owner a number I can defend, from whatever drawings exist, by the meeting."** This is the SD/DD conceptual budget, with an assumptions log and contingency.
2. **"Make sure every scope is carried by somebody before bid day closes."** This covers scope sheets, coverage by trade, and plug numbers for uncovered trades.
3. **"Level the sub numbers apples-to-apples and find what's missing before we buy out."** This covers bid leveling and scope-gap detection.
4. **"Keep the estimate alive as the design moves: SD → DD → CD → GMP, without re-taking off from scratch."** This covers versioning, reconciliation and VE.
5. **"Get more pursuits out the door without hiring another estimator."** This covers capacity on demand: Quotr Service or AI takeoff.

### Gaps
- None of the job statements come from Quotr customer interviews. Validate them with 10–12 switch interviews with recent GC buyers or churners, as the framework requires.

---

## D. Psychology

### Takeaway
Precon's status comes from being right early. The first number anchors the owner, and a blown budget is a career-visible miss. The buyer is therefore accuracy- and explainability-anxious, ecosystem-habituated (Procore/ACC, Excel and a 10–15-year cost database), and buys through pilots on live pursuits. Hot moments are bid day and the Friday-afternoon "owner needs a budget Monday" request. Cold moments are January planning, post-mortems after a buyout bust, and tool renewals.

### Cited Findings
- Moving off the first conceptual number creates a credibility problem with the owner: deviations "can create challenges in managing owner expectations and may require additional efforts to realign perceptions" (snippet; source among [Trimble Constructible](https://constructible.trimble.com/blog/how-to-turn-your-conceptual-estimates-into-your-competitive-advantage) and [Procore Library](https://www.procore.com/library/conceptual-estimating), not pinned)
- Under AIA B101 (as summarized in a study guide), if the lowest bona fide bid exceeds the owner's budget, §6.6 gives the owner five specific options. The budget miss becomes a contractual event — [open-exam-prep (secondary)](https://open-exam-prep.com/study-guides/are-pjm/budget-changes/cost-estimating-budget-compliance)
- Conceptual accuracy runs from about **±20%** for a feasibility study to about **±6%** for a complex conceptual design estimate (snippet; source among [Procore Library](https://www.procore.com/library/conceptual-estimating) and [EC&M](https://www.ecmweb.com/design/conceptual-estimates-budgets-and-design-build))
- AI attitudes in construction:
  - Dodge/CMiC (235 contractors, Dec 2025): **87%** expect AI to matter, but only **19%** have adapted workflows. Top concerns are **data accuracy (57%)** and **security (54%)**, and only **26%** rate their own data quality as high
  - Autodesk 2025: construction leaders' **trust in AI fell 14 points**

  Sources (via prior audit): [Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/); [Autodesk](https://www.autodesk.com/blogs/construction/state-of-design-make-spotlight-construction/)
- Leadership pressure: AGC/Sage 2026 found **61%** of firms use AI or plan to increase AI investment (up from 44%). Within that, **23%** use it for estimating and **20%** for design/preconstruction (via prior audit) — [AGC report PDF](https://www.agc.org/sites/default/files/users/user21902/2026%20Construction%20Hiring%20and%20Business%20Outlook%20Report_Final2.pdf)
- A sponsored Construction Dive piece says estimating capacity is now "the core bottleneck in preconstruction." It cites AGC's 2025 outlook: 44% planned to raise AI spending and 35% to raise investment in estimating software — [Construction Dive (sponsored)](https://www.constructiondive.com/spons/why-ai-will-become-the-backbone-of-preconstruction/808560/)
- G2 (1,076 B2B buyers, March 2026; not construction-specific): **51%** start software research in an AI chatbot, **69%** chose a different vendor than planned because of chatbot guidance, and **85%** think more highly of a vendor an AI mentions (via prior audit) — [G2 press release](https://www.prnewswire.com/news-releases/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots-302742807.html)

### Inferences
- **Identity and status (Likely).** Precon is the GC's "brains" before the job is won: it shapes the GMP, the fee and the owner relationship, and is judged when the buyout lands. Postings bundle conceptual estimating, GMP development and constructability into one leader.
- **Career risk (Likely).** The asymmetric loss is "my number was low and we ate it at buyout" or "my number was high and we lost the negotiated job". This produces padding, contingency habits and a demand for a visible **assumptions log** rather than a black-box total. Bricks & Bytes argues that AI skepticism is well-founded when firms are offered "a locked final number with no visible assumptions" (snippet) — [Bricks & Bytes](https://bricks-bytes.beehiiv.com/p/ai-reads-the-blueprint-what-it-reads-next).
- **Owner and architect relationship (Likely).** Precon defends numbers against the owner's cost consultant and the architect's estimate, so reconciliation formats (UniFormat ↔ CSI) are proof assets.
- **Decision style (Likely).**
  - Enterprise-IT review appears at $300M+ firms.
  - Procore or ACC is the system of record, so "does it plug into Procore/ACC/BuildingConnected?" is a gate.
  - Buying happens via a 30–90-day pilot on 1–3 live pursuits, with the chief estimator as champion and a COO or CFO as approver.
  - Contract value is small relative to firm revenue, so the risk is reputational, not financial.
- **Hot vs cold moments (Likely).**

| Mode | Moment | Time cue | What they need from a page |
|---|---|---|---|
| Hot | Owner asks for an SD/DD budget "by Monday" | Friday afternoon; before an owner or board meeting | Turnaround, price, sample deliverable, "start now" |
| Hot | Bid day with thin coverage on one or more trades | Bid day morning to the deadline | Plug-number method, $/sf by trade, quick takeoff |
| Hot | Owner's consultant says the estimate is X% high | Days before a GMP or VE meeting | Reconciliation method, line-by-line format |
| Cold | Post-mortem after a scope gap cost money | After buyout or closeout | Scope-gap checklist; leveling process |
| Cold | CEO "AI plan" or annual tech budget | January; strategic planning | Evaluation matrix, security, integration, pilot plan |
| Cold | Renewal or migration (Sage → cloud, ProEst/DESTINI renewal) | 60–90 days before renewal | Migration path, database import, total cost |

- **Biases that matter, ranked by replication (per the framework).**
  - **Defaults / status quo (robust).** The Procore/ACC ecosystem and Excel templates are the default. Content must lower switching cost (imports, "works alongside Procore") rather than argue features.
  - **Anchoring (robust).** The first SD number anchors the owner. Pages should show how to present ranges, alternates and an assumptions log so the anchor is defensible.
  - **Temporal landmarks (robust).** January outlooks, fiscal-year starts and post-bid-season reviews are fresh-start moments for tool evaluation.
  - **Generic social proof (fragile).** "Thousands of contractors" lines are weak. What works here is **specific, similar-firm references** ("a $150M healthcare GC in Texas"). That is authority and similarity, not generic proof.
  - **Choice overload (≈0 effect).** Ignore it.

### Gaps
- No primary interviews with precon leaders were obtained. "Brains of the GC" identity language, pilot length and approver chain are inferences.
- No FMI precon study was retrieved this pass.

---

## E. Four forces (verbatim quotes with URLs)

### Takeaway
- **Push:** drawings are not complete but a number is due; subs do not respond; costs move (tariffs, +8.9% inputs).
- **Pull:** AI capacity plus leadership mandates.
- **Anxiety:** accuracy, black-box numbers, security.
- **Habit:** Excel leveling, Procore for project management while estimating stays elsewhere, aging but trusted desktop estimating with large cost databases, and painful past migrations.

### Cited Findings (all quotes are **snippet-level**: returned as quoted text by search from the cited page set, not opened on-page)

| # | Force | Verbatim | Who/where | URL |
|---|---|---|---|---|
| 1 | Push (incomplete drawings) | "Drawings that are presented as 75 percent complete but actually lack such basic information as wall types are really just budget drawings masquerading as a bid set." | AWCI *Construction Dimensions*, "Estimator's Edge" column | [AWCI](https://onlinedigeditions.com/article/Estimator%27s+Edge/2436297/295348/article.html) |
| 2 | Push (owner obligation) | "Advise the Owner if it appears that the Construction Cost Estimate may exceed the Project budget, and make recommendation for corrective action." | CM/GC contract clause sample | [Law Insider](https://www.lawinsider.com/clause/construction-estimates) |
| 3 | Push (sub coverage) | "subs who opened an older version are not able to access the updated/new bid form" | BuildingConnected reviewer | [TrustRadius](https://www.trustradius.com/products/autodesk-buildingconnected/reviews/all) |
| 4 | Push (bid-list data quality) | "some companies it finds are sometimes suppliers and not subcontractors" | BuildingConnected reviewer | [SourceForge](https://sourceforge.net/software/product/BuildingConnected) |
| 5 | Habit (Procore for PM, not estimating) | "we still use Procore for project management, but we don't use it for estimating purposes" | Procore / Procore Estimating reviewer | [Capterra Procore Estimating reviews](https://www.capterra.com/p/157661/Esticom/reviews/?page=2) (page not pinned; also [Capterra Procore](https://www.capterra.com/p/56250/Procore/reviews/?page=3)) |
| 6 | Anxiety/cost | "by far, the most expensive solution that we reviewed" | Procore reviewer | [Capterra Procore reviews](https://www.capterra.com/p/56250/Procore/reviews/?page=6) (page not pinned) |
| 7 | Anxiety/complexity | "can tend to be somewhat complicated at times" | Procore Estimating reviewer | [Capterra Procore Estimating](https://www.capterra.com/p/157661/Esticom/reviews/?page=2) |
| 8 | Push (design revisions) | "no easy way of switching back and forth between different blueprints in ProEst during the revision stages" | ProEst reviewer | [Capterra ProEst (CA)](https://www.capterra.ca/reviews/8684/proest) (mirror not pinned) |
| 9 | Anxiety (migration) | "many glitches through the portal since we switched to the new iCloud system" | ProEst reviewer, after the cloud move | [Capterra ProEst (CA)](https://www.capterra.ca/reviews/8684/proest) (mirror not pinned) |
| 10 | Habit (learning curve) | "a learning curve for new users who have been estimating with the traditional, manual process" | DESTINI Estimator G2 reviewer (mid-market architecture/planning firm, May 2020) | [G2](https://www.g2.com/products/destini-estimator/reviews) (may be partly paraphrased by the summarizer) |
| 11 | Anxiety (AI ≠ estimating) | "Because estimating is not quantity takeoff." | Estimator quoted from a discussion thread | [ConstructConnect](https://www.constructconnect.com/blog/are-ai-takeoffs-accurate-in-2026) |
| 12 | Anxiety (AI reliability) | AI takeoff tools are "hit-or-miss" | r/estimators thread (via Perplexity in the prior audit) | [r/estimators](https://www.reddit.com/r/estimators/comments/1lc2lmz/anyone_using_ai_for_estimating/) |
| 13 | Habit (Excel) | "Most GCs do bid leveling in Excel. That is not wrong — Excel is flexible, familiar, and it works." | Vendor blog (vendor voice, not buyer) | [imagetotable.ai](https://imagetotable.ai/blog/batch-subcontractor-quotes-bid-comparison) / [Meltplan](https://www.meltplan.com/blogs/best-bid-leveling-software-for-general-contractors-2026-comparison.md) (not pinned) |
| 14 | Pull (vendor framing) | "AI isn't taking estimators' jobs; it's transforming what the role looks like." | Autodesk blog (vendor) | [Autodesk](https://www.autodesk.com/blogs/construction/ai-preconstruction-workflows/) |

**Further force evidence (paraphrased, not verbatim)**
- **Push.** A GetApp reviewer estimated that **1/3 to 1/2 of contacted subs** do not get the message or do not respond on BuildingConnected; this is a single person's estimate — [GetApp](https://www.getapp.ca/reviews/122135/buildingconnected). A vendor blog reports GCs saying subs rarely submit through the platform — [Downtobid](https://downtobid.com/blog/building-connected-reviews).
- **Habit.** Sage Estimating reviewers call it trusted but aged, with no remote access except via Citrix/RDP and weak BIM interfaces — [TrustRadius](https://www.trustradius.com/compare-products/sage-estimating); [TrustRadius reviews](https://www.trustradius.com/products/sage-estimating/reviews/all).
- **Anxiety (cost).** ProEst is called pricey for smaller firms, with an inflexible report writer and restricted assemblies; Capterra rates value for money at **3.7/5** — [Capterra ProEst](https://www.capterra.co.uk/reviews/8684/proest).
- **Pull.** In Dodge/CMiC, automated proposal generation was rated **92%** effective (via prior audit) — [BusinessWire](https://www.businesswire.com/news/home/20251205015633/en/New-Research-Reveals-Strong-Contractor-Optimism-About-AIs-Transformative-Impact-on-Construction-Industry).

### Inferences — force → prompt class → content answer

| Force | Prompt class it produces | Example prompt form | Quotr content that answers it |
|---|---|---|---|
| Push | "Is this normal / how do others handle X" | "owner wants a budget from SD drawings missing wall types — how do other GCs handle it" | Conceptual-estimating method page with an assumptions-log template |
| Pull | "What actually works for X" | "AI that can price schematic drawings for a GC" | GC hub + SD-budget service page with a sample deliverable |
| Anxiety | "Is X accurate / safe / vs Y" | "how accurate are AI conceptual estimates vs final cost", "does it train on our drawings" | Accuracy-method page with variance data; security and data-use page |
| Habit | "Can I keep doing Y / do I need X" | "is Excel good enough for bid leveling", "can I keep Sage Estimating and add AI takeoff" | "Works alongside Excel/Procore/Sage" pages; import and migration guide |

### Gaps
- No LinkedIn posts or podcast transcripts (e.g., ConTechCrew) by named precon leaders were retrieved, so all quotes are from reviews, columns and threads.
- No current r/ConstructionManagers verbatims: Reddit was unreachable and the search budget ran out.

---

## F. Trigger events and trigger calendar

### Takeaway
Triggers are mostly event-driven (an owner request, a bid day, a lost estimator, a buyout bust), layered on a calendar of fresh-start moments: the January outlook, fiscal-year public spending, spring bid season, and tool renewals. Dodge monthly releases and tariff news are recurring "cost changed" pushes.

### Cited Findings
- The AGC/Sage outlook is released in **January** (2026: Jan 8), and its AI-adoption numbers circulate then — [AGC release](https://www.agc.org/news/2026/01/08/contractors-have-dampened-expectations-2026-apart-data-centers-and-power-projects-amid-worries-about)
- The ENR Top 400 is published in **May**; firm press releases follow — [NOLA Newswire, May 2026](https://nolanewswire.com/2026/05/rngd-named-to-2026-top-400-general-contractors-list-by-enr/)
- Dodge monthly starts reports come out about the **third week of each month** (June 18, July 22, Aug 21, Sep 28, Oct 26 items in 2026) — [inside.lighting](https://inside.lighting/news/26-10/construction-starts-cool-growth-persists)
- Tariffs affected about **70%** of firms (AGC/Sage) — [Sage](https://www.sage.com/en-us/blog/2026-construction-industry-outlook/). In January 2026, 40% of contractors raised bids because of tariffs and 32% bought early (via prior audit) — [AGC](https://www.agc.org/news/2026/01/14/construction-costs-rise-fastest-rate-january-2023-november-outpacing-increases-contractors-bid)

### Inferences — trigger calendar (Likely unless marked)

| When | Trigger | Push type | Mode | Search pattern | Content to have live |
|---|---|---|---|---|---|
| Any Friday / pre-board week | Owner needs an SD/DD budget fast | Event | Hot | "fast conceptual estimate SD drawings" | SD-budget service page (urgent version) |
| Bid days (peak Feb–May for summer starts; school work bids winter–spring for summer construction — *Speculative timing*) | Thin sub coverage | Event | Hot | "plug number uncovered trade", "how many bids per trade" | Coverage and plug-number answer page |
| January | AGC outlook, CEO "AI plan", budget year | Fresh start | Cold | "AI tools for preconstruction 2026/2027" | Evaluation guide + GC hub |
| July 1 (most state fiscal years — *background knowledge*) and Oct 1 (federal FY) | Public program lettings and design starts | Calendar | Cold → hot | "design-build K-12 estimate requirements" | Delivery-method estimate milestones page |
| Aug–Sept (federal Q4 obligations — *background knowledge*) | Federal and military work surges | Calendar | Hot | "Davis-Bacon conceptual estimate" | Prevailing-wage estimating note |
| Monthly (Dodge, AGC PPI releases) | Cost escalation news | Recurring | Cold | "construction cost escalation 2026 %" | Escalation and contingency page (monthly refresh) |
| After buyout / closeout | Scope gap cost the firm | Event | Cold | "how to catch scope gaps between trades" | Scope-gap checklist + leveling guide |
| Estimator resignation / pipeline spike | Capacity gap | Event | Warm/hot | "outsource precon estimating for GC" | Service page with price/sf + sample |
| 60–90 days before renewal (Speculative timing) | Procore/ACC/ProEst/DESTINI/Sage renewal or price change | Event | Cold | "ProEst alternatives", "DESTINI vs ProEst" | Comparison pages |
| Rate cuts / project restarts (*Speculative*; no 2026 rate data retrieved) | Shelved projects re-priced | Macro | Cold → hot | "re-price a 2024 estimate for 2027" | Re-pricing/escalation guide |
| Procore Groundbreak (typically fall) / ENR FutureTech (typically spring) — *background, verify dates* | Category attention spikes | Event | Cold | "best AI precon tools" | Fresh comparison + data release timed to events |

### Gaps
- No sourced 2026 Procore or Autodesk pricing-change events were retrieved. Track Procore's annual price adjustments and ACC/BuildingConnected Pro packaging changes.
- No sourced bid-season seasonality data (e.g., Dodge starts by month by building type). Use Dodge monthly series or Google Trends for "bid leveling" and "conceptual estimate" to confirm.
- No Fed 2026 rate path was retrieved.

---

## G. Switch timeline with prompt form at each stage

### Takeaway
Prompt specificity grows along the timeline: from situational (no category noun), to category plus comparator, to brand plus price plus objection. For this ICP the "deciding" stage almost always includes an integration or security question.

### Cited Findings
- The framework mapping (first thought → passive → active → deciding → consuming) comes from the uploaded methodology (local file). The behavioral anchors for this ICP are the G2 chatbot stats and the Dodge/CMiC concerns cited in D.

### Inferences (prompt forms are Simulated, built from the cited pushes and anxieties)

| Stage | What is happening | Typical prompt form (first person) | Engine behavior to expect | Proof needed |
|---|---|---|---|---|
| First thought | A blown buyout or an SD request with too little time | "Owner wants a budget from 30% SD drawings by Monday and the drawings don't even have wall types. How do GCs usually handle this?" | Methodology answer; no brands; fan-out adds "conceptual estimate", "square foot cost" | Method + $/sf benchmarks + assumptions log |
| Passive looking | Reading about AI in precon; peers mention tools | "Are GCs actually using AI for conceptual estimating yet, or is it just takeoff?" | Survey stats (AGC, Dodge); vendor blogs | Survey data, honest limits |
| Active looking | Building a list | "Best conceptual estimating software for a mid-size commercial GC that uses Procore, 2026" | Fan-out: best / 2026 / reviews / vs DESTINI / ProEst / Procore | Comparison table, review counts, integration list |
| Deciding | 2–3 vendors, pilot design | "DESTINI vs ProEst vs an AI tool like Quotr for SD/DD budgets — which is more accurate, and does any of them integrate with Procore and BuildingConnected?" | Fan-out: brand official, pricing, integration, SOC 2 | Pricing page, security page, integration facts, reference GC |
| Consuming / expanding | Pilot on live pursuits; renewal | "How do I import our historical cost database from Sage Estimating/Excel into [tool]?" | Docs and help pages | Import docs, migration case |

### Gaps
- There are no recorded real prompts from this ICP. The framework's switch interviews should add "what exactly did you type, and where?"

---

## H. Current alternatives and unmet needs (ranked)

### Takeaway
The real competitor set is not only software:
- in-house estimators using Excel and a decade-old cost database
- sub "budget numbers"
- RSMeans
- independent cost consultants
- outsourced estimating shops
- incumbent estimating suites (DESTINI, ProEst, Sage, WinEst)
- the Procore/ACC/BuildingConnected bid stack

The most frequent unmet needs in the evidence are conceptual pricing from incomplete drawings and bid leveling / scope-gap detection. A wave of new AI bid-leveling startups is moving into the second.

### Cited Findings
**Alternatives and their limits**
- **Sub budget numbers** are the norm. A precon director posting explicitly asks for estimates "without relying on subcontractor pricing", which implies most teams do rely on it — [Mediabistro](https://www.mediabistro.com/jobs/3541039271-director-preconstruction) / [CSG Talent](https://www.csgtalent.com/jobs/job/preconstruction-director-17066/) (not pinned)
- **Independent estimators.** Contracts sometimes require "a preliminary probable cost statement prepared by an independent estimator" with schematics (snippet; Law Insider page not pinned) — [Law Insider](https://www.lawinsider.com/clause/schematic-phase)
- **Outsourced preliminary estimates:** "We give you a ballpark figure based on general drawings and specs. Accuracy stays within 20%." (snippet) — [Tyler Estimating](https://tylerestimating.com/preliminary-estimating-services)
- **DESTINI Estimator:**
  - Capterra **4.3 from 36 reviews**; G2 has **one** review
  - Pricing conflicts: one listing says "starting $4,600/yr", while Capterra says contact the vendor

  Sources: [Capterra](https://www.capterra.com/p/161842/DESTINI-Estimator/reviews/); [G2](https://www.g2.com/products/destini-estimator/reviews); [Software Advice](https://www.softwareadvice.com/job-costing/destini-estimator-profile/) / [SoftwareFinder](https://softwarefinder.com/construction/destini-estimator/reviews?page=2) (price source not pinned)
- **ProEst** (Autodesk since 2021): G2 **4.3 from 63**. Cons are cloud-only, price for small firms, report writer, restricted assemblies and blueprint switching during revisions — [G2](https://www.g2.com/products/ProEst/reviews); [Capterra](https://www.capterra.co.uk/reviews/8684/proest)
- **Sage Estimating:** G2 **4.1 from 18**; SelectHub "starting ~$365/user/month" (unverified). Not cloud-native — [G2 compare](https://www.g2.com/compare/sage-construction-management-formerly-corecon-vs-sage-estimating); [SelectHub](https://www.selecthub.com/p/construction-estimating-software/sage-estimating/); [TrustRadius](https://www.trustradius.com/compare-products/sage-estimating)
- **Procore** (platform):
  - top G2 cons are **Missing Features (231)** and **Learning Curve (192)**, across the platform
  - Procore Estimating reviews mention complexity
  - one competitor blog headlines "Procore Estimating: What It Covers and Where It Gets Complicated"

  Sources: [G2](https://www.g2.com/products/procore); [Buildern](https://buildern.com/resources/blog/procore-estimating/)
- **BuildingConnected:** Capterra **4.6** ease of use (204 reviews); TrustRadius **8.7/10** (25). Complaints cover sub response, bid-form versioning, takeoff integration and supplier-vs-sub data — [Capterra](https://www.capterra.com/p/156791/BuildingConnected/reviews/); [TrustRadius](https://www.trustradius.com/products/buildingconnected/reviews)
- **Bid leveling is still manual.** Vendor guides say most GCs level in Excel and lose hours to data entry and version control. A 2026 guide calls leveling one of the last precon tasks done "almost entirely by hand" (vendor claim) — [Archdesk](https://archdesk.com/blog/guide-to-subcontractor-bid-leveling); [Meltplan workflow guide](https://www.meltplan.com/blogs/construction-takeoff-estimating-and-bid-leveling.md)
- **New AI bid-leveling and precon entrants** in 2026 search results:
  - Belidor (AI bid leveling; $3.1M pre-seed per Dealroom)
  - Consight / BudgetBuilder (AI estimating and bid analysis for GCs)
  - Buildr (pursuit, estimating and bid leveling)
  - Axiom Estimating (takeoff, CSI estimates, sub bid leveling)
  - DESTINI (bid leveling inside its suite)

  Sources: [Dealroom](https://app.dealroom.co/companies/belidor); [G2 BudgetBuilder](https://www.g2.com/products/budgetbuilder/reviews); [G2 Buildr](https://www.g2.com/products/buildr/discuss); [G2 Axiom](https://www.g2.com/products/axiom-estimating-llc/reviews); [ConstructionPlacements AI bid leveling tools](https://www.constructionplacements.com/ai-bid-leveling-tools/)
- **AI takeoff is positioned as a first pass.** On-Screen Takeoff claims its AI gets "80% of the way" to a final takeoff, and ConstructConnect says AI takeoffs need human review for higher-risk items — [OnCenter](https://www.oncenter.com/blog/article/what-is-ai-takeoff/); [ConstructConnect](https://www.constructconnect.com/blog/are-ai-takeoffs-accurate-in-2026)
- **Data foundation is weak:** only **26%** of contractors rate their data quality as high (Dodge/CMiC, via prior audit) — [Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/)

### Inferences — unmet needs ranked by frequency in the retrieved evidence (n is small; Likely)

| Rank | Unmet need | Evidence count (sources above) | What fails today | Quotr fit (Known / TO CONFIRM) |
|---|---|---|---|---|
| 1 | **Conceptual estimate from incomplete SD/DD drawings, defensible to the owner** | 7 (contract clauses ×2, DCD, AWCI, job postings ×2, Procore/EC&M accuracy) | Takeoff tools assume measurable drawings; suites need assemblies and a cost DB the team must maintain; sub numbers are slow and padded | Quotr Service does "cost estimates and pro formas" at $/sf (Known); SD-level method and accuracy not published (TO CONFIRM) |
| 2 | **Bid leveling + scope-gap detection** | 6 (Excel default, Archdesk, Meltplan, 5 AI entrants, BuildingConnected takeoff-integration complaint, 1–3 days per leveling) | Excel manual entry; bid platforms collect bids but do not normalize scope | Quotr has "side-by-side bid comparison" and an "AI bid-comparison parser … gap breakdown" (index-only); **GC-side sub-bid leveling TO CONFIRM** |
| 3 | **Sub coverage / response on bid day** | 4 (GetApp 1/3–1/2, Downtobid, TrustRadius versioning, SourceForge supplier-vs-sub) | Invite blasts; stale bid forms; wrong contacts | Not a Quotr strength; answer with plug-number method + quick takeoff for uncovered trades |
| 4 | **Estimate versioning SD→DD→CD and reconciliation** | 3 (ProEst revision switching, AWCI 2–3 revisions each needing fresh takeoff, Trimble/Procore owner-expectation note) | Re-takeoff per revision; manual reconciliation | AI re-takeoff per set is plausible (Likely); Procore/ACC sync unknown |
| 5 | **Historical cost data reuse / data quality** | 2 (Dodge/CMiC 26%; Sage reviews on large DBs) | Data trapped in Sage/WinEst/Excel | Import path unknown (TO CONFIRM) |
| 6 | **Transparency / assumptions for AI outputs** | 3 (Bricks & Bytes, ConstructConnect, r/estimators "hit-or-miss") | Black-box totals | Publish method, assumptions log and variance (to build) |
| 7 | **Price/value of incumbents** | 3 (Procore "most expensive", ProEst value 3.7, Sage ~$365/user/mo) | Platform pricing tied to the suite | Plus $299.90/seat/mo; Service per sf (Known) |
| 8 | **Cloud/mobility** | 2 (Sage reviews) | Desktop + Citrix | Cloud (Known, per product pages) |

### Gaps
- No frequency data from the ICP's own words at scale (e.g., 50 Reddit posts coded). Run the framework's desk ethnography on r/estimators and r/ConstructionManagers once Reddit is reachable.
- RSMeans and cost-consultant pricing and usage among mid-market GCs were not retrieved.

---

## I. Willingness to pay, budget owner, procurement, security, sales cycle, pilots

### Takeaway
Price anchors for one estimating seat run about $3,000–$5,000 a year (STACK, Plus, DESTINI's listed start). Construction software buyers on Capterra expect about $1,600–$4,000 a year. Precon labor costs about $160K or more per person per year. WTP is therefore not the constraint. The gates are proof of accuracy on the firm's own past jobs, security and data use, and Procore/ACC fit. Quotr currently publishes no SOC 2 statement, no named integrations and no GC case study.

### Cited Findings
- **Price anchors:**
  - STACK Takeoff & Estimate "as low as $249/user/month" (local competitor file, from stackct.com/pricing)
  - DESTINI from $4,600/yr (one listing, conflicting)
  - Sage Estimating ~$365/user/month (SelectHub, unverified)

  Sources: [local competitor-landscape.md](/home/user/quotr/geo-brain/03-market/competitor-landscape.md); [SelectHub](https://www.selecthub.com/p/construction-estimating-software/sage-estimating/)
- **Buyer expectations:** Capterra construction buyers expect about **$1,600–$4,000/yr**, and estimating is the most-requested feature. Software Advice says **72%** of 5,000+ construction buyer conversations asked about estimating (via prior audit) — [Capterra Buyer Insight](https://www.capterra.com/resources/construction-software-buyer-insight/); [Software Advice](https://www.softwareadvice.com/construction/cost-estimating-software-comparison/)
- **Security is a top concern:** **54%** in Dodge/CMiC (via prior audit) — [BusinessWire](https://www.businesswire.com/news/home/20251205015633/en/New-Research-Reveals-Strong-Contractor-Optimism-About-AIs-Transformative-Impact-on-Construction-Industry)
- **Quotr facts (local files):**
  - Lite **$79.90**, Plus **$299.90** per seat/month; Enterprise custom; 7-day trial
  - Service **$0.25/sf under 50,000 sf; $0.10/sf above**
  - security copy is one generic line ("industry-standard encryption")
  - **no SOC 2 statement**, no Procore App Marketplace listing found, integrations unnamed
  - Service turnaround is stated **inconsistently** (24 hours vs 3–4 business days vs 1–3 days vs 72 hours)

  Sources: [product-and-features.md](/home/user/quotr/geo-brain/00-quotr/product-and-features.md); [entity-fact-sheet.md](/home/user/quotr/geo-brain/00-quotr/entity-fact-sheet.md)

### Inferences
- **Budget owner (Likely).**
  - At $20–150M firms: the VP Precon or chief estimator, with the owner/president approving.
  - At $150M–$1B firms: precon leadership with COO/CFO sign-off, plus an IT/security review (questionnaire, SSO, data-use clause).
- **Procurement path (Likely).** Trial or demo → **pilot on 1–3 live pursuits (30–90 days)** → compare against the in-house number and the eventual sub/bid result → seat purchase or a Service MSA. Service is easier to buy (a project expense, often billable inside precon fees) than software (overhead).
- **Sales cycle (Speculative).** About 2–6 weeks for Service on a single project, and 2–6 months for multi-seat software at $150M+ firms.
- **Must-have proof for IT (Likely):**
  - whether customer drawings train models (the prior library already has the prompt "does AI estimating software train on my drawings, is my bid data secure", E-071)
  - SOC 2 Type II or a roadmap
  - data residency and retention
  - SSO
- **Pricing clarity matters for GEO.** A GC page should state Service math for typical GC jobs, e.g. a 60,000 sf MOB → $6,000 at $0.10/sf (**TO CONFIRM** whether the $0.10 rate applies to the whole area or only the area above 50,000 sf).

### Gaps
- There is no sourced data on GC software procurement cycles or pilot norms. Ask Quotr's existing commercial customers.
- Procore/ACC platform pricing for mid-market GCs was not retrieved.

---

## J. Vocabulary list

### Takeaway
Content must speak delivery-method and estimate-class language, not "takeoff" language only. Precon buyers search with GMP, CMAR, SD/DD/CD, ROM, UniFormat and "bid leveling".

### Cited Findings
- GMP development, conceptual estimating and constructability appear together in precon director postings — [Michael Page](https://www.michaelpage.com/job-detail/director-preconstruction-mid-size-fort-worth-gc/ref/jn-102026-7125271)
- Quotr already has dictionary entries for GMP, bid leveling, scope gap, plug number and cost code (local prompt-library.md).

### Inferences (vocabulary to use verbatim in headings and FAQ; definitions are background knowledge)
- **Delivery and contracts:**
  - GMP (guaranteed maximum price)
  - CMAR / CM at-risk; CM agency
  - design-build (DB); **progressive design-build (PDB)**
  - IPD
  - hard bid / lump sum / "lowest responsive, responsible bidder"
  - negotiated work; preconstruction services agreement (PSA)
  - savings split; fee; general conditions vs general requirements (GCs/GRs)
  - OH&P; bonding capacity; SDI (subcontractor default insurance)
- **Estimate stages:**
  - ROM (rough order of magnitude)
  - conceptual / parametric estimate
  - **SD / DD / CD estimates** (schematic design, design development, construction documents)
  - AACE estimate classes 5→1 (verify ranges against AACE RP 18R-97 before publishing)
  - basis of estimate; assumptions log; estimate reconciliation
- **Pricing structure:**
  - **allowances**; **alternates** (add/deduct)
  - unit prices
  - **contingency** (design/estimating, construction, owner)
  - escalation; plug numbers; sub "budget numbers" / budgetary pricing
- **Bid management:**
  - ITB (invitation to bid); bid packages; **scope sheets / scope of work**
  - coverage; bid day
  - **bid leveling** / bid tab
  - exclusions, qualifications and clarifications
  - buyout
- **Cost organization:**
  - **CSI MasterFormat** divisions (Div 01–49)
  - **UniFormat II** (A Substructure, B Shell, C Interiors, D Services, E Equipment & Furnishings, F Special Construction, G Sitework)
  - cost codes; $/sf, $/unit, $/bed, $/student
- **Design-cost management:** value engineering (VE); target value design (TVD); constructability review; design-to-budget
- **Labor basis:** open shop / merit shop (ABC); union; **prevailing wage / Davis-Bacon**; PLA (project labor agreement)
- **Tools:** Procore, ACC (Autodesk Construction Cloud), BuildingConnected, ProEst, DESTINI Estimator / DESTINI Optimizer (Beck Technology), Sage Estimating, WinEst (Trimble), Bluebeam Revu, STACK, On-Screen Takeoff, RSMeans

### Gaps
- No verbatim usage frequency for these terms in AI prompts. Validate with Search Console and the GC prompt runs.

---

## K. Channels

### Takeaway
This ICP learns from peers, associations and trade media more than from vendor blogs. For AI engines, LinkedIn articles, review directories, trade media and Reddit are the citable surfaces. Reddit's ChatGPT citation share collapsed twice (Sept 2025, Aug 2026), so it is a wording source more than a citation bet.

### Cited Findings
- **LinkedIn** appears in **11%** of AI responses (No. 1 for professional topics). Articles are 50–66% of cited LinkedIn content (Semrush, via prior audit) — [Search Engine Land](https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138)
- **Reddit's ChatGPT citations** fell from **3.83% to 0.52%** in August 2026 (Promptwatch, via prior audit) — [Axios](https://www.axios.com/2026/08/20/chatgpt-reddit-citations-geo-strategy)
- **r/estimators** appeared in **6 of 45** Perplexity runs in Quotr's category tests, with **no Quotr mentions** — [local citation-sources-map.md](/home/user/quotr/geo-brain/03-market/citation-sources-map.md)
- **Trade press:** ENR and For Construction Pros publish estimating and bidding tech stories, and none mention Quotr (prior audit) — [ENR example](https://www.enr.com/articles/63634-construction-is-about-to-leave-124b-on-the-table-due-to-outdated-bidding)
- **Construction Dive** runs sponsored precon-AI content, which shows a paid content slot exists — [Construction Dive (sponsored)](https://www.constructiondive.com/spons/why-ai-will-become-the-backbone-of-preconstruction/808560/)
- **Review directories** dominate brand "reviews/cons" retrieval for DESTINI, ProEst, Sage Estimating, Procore Estimating and BuildingConnected: Capterra (plus ~10 country mirrors), GetApp, Software Advice, TrustRadius, G2, SelectHub, SourceForge, SoftwareFinder (Section O proxies)

### Inferences — channel table (sizes are gaps)

| Channel | Role for this ICP | AI-citation value | Notes |
|---|---|---|---|
| r/estimators, r/ConstructionManagers, r/Construction | Wording, pain mining; disclosed founder answers | Low-medium in ChatGPT (post-Aug 2026); higher in Perplexity/AIO | Member counts not retrieved |
| LinkedIn (precon leaders, AGC chapters, ENR) | Peer signalling; long-form articles | **High** (No. 1 professional source) | Founder and estimator articles with data |
| AGC (national + chapters), ABC (open shop), DBIA (design-build), CMAA, ASPE (estimators), AACE | Trust, education credits, events | Medium (association pages get cited) | DBIA matters for the PDB trigger |
| Procore Groundbreak; ENR FutureTech; AGC IT Forum (*background*) | Vendor discovery | Low direct; event coverage helps | Time data releases to these |
| ENR, Construction Dive, For Construction Pros, BD+C | Trade authority | **High** (earned media is ~84% of AI citations per Muck Rack, via prior audit) | Contributed articles with original data |
| Podcasts (ConTechCrew, Construction Brothers — *background*) | Founder interviews | Medium (transcripts get cited) | Not retrieved this pass |
| YouTube | Demos: "SD set → budget" | **High in Google AIO/AI Mode** | Quotr has an @QuotrAI channel (local) |
| G2 / Capterra / TrustRadius / Software Advice | Shortlist validation | **Very high** for "reviews/vs/alternatives" fan-outs | Quotr has ~0 reviews (local) |

### Gaps
- Subreddit member counts, AGC/ABC/DBIA event dates for 2027, and podcast download data were not retrieved.

---

## L. Proof required at each stage

### Takeaway
The proof gate for this ICP is "accuracy vs final cost on jobs like mine". Everything else (speed, price, AI) is secondary. The next gates are similar-GC references and security/integration facts.

### Cited Findings
- Data accuracy (57%) and security (54%) are the top AI concerns (Dodge/CMiC) — [BusinessWire](https://www.businesswire.com/news/home/20251205015633/en/New-Research-Reveals-Strong-Contractor-Optimism-About-AIs-Transformative-Impact-on-Construction-Industry)
- 50% of daily-chatbot B2B buyers cite review sites as their No. 1 confidence signal (G2, via prior audit) — [G2 report](https://learn.g2.com/g2-2026-ai-search-insight-report)
- Quotr's case studies are qualitative: the RL Electric page lists outcomes as "AI-assisted", "Reduced", "Dozens", and Salisbury Moore's type of firm is unconfirmed — [local geo-tactics-already-used.md](/home/user/quotr/geo-brain/02-current-state/geo-tactics-already-used.md)

### Inferences

| Stage | Proof required | Quotr has it? | Asset to build |
|---|---|---|---|
| First thought | Clear method; ranges by estimate class; $/sf benchmarks by building type | Partly (blog posts) | "Conceptual estimating from SD drawings" method page with benchmark table |
| Passive | Industry data, honest limits of AI | Weak (State of AI post repackages public data) | Original precon survey or Quotr Service benchmark |
| Active | Comparison table vs DESTINI, ProEst, Sage, STACK, Procore Estimating; review counts | No (no GC comparisons; ~0 reviews) | 3 comparison pages + G2/Capterra review drive |
| Deciding | **SD estimate vs final bid/buyout variance on 10+ jobs**; reference from a similar GC; SOC 2/data-use; Procore/ACC/Excel export | No | Variance study; GC case study; security page; integration facts |
| Consuming | Import of cost DB; onboarding time; support SLA | Unknown | Migration guide; onboarding page |

### Gaps
- Quotr's actual accuracy data (Service estimates vs final costs) is unknown. This is the single most valuable proof to obtain.

---

## M. Coding chains (5–8)

### Takeaway
There are eight chains. Chains 1, 3 and 5 are hot and service-led (Quotr Service is the natural answer). Chains 2, 4, 6, 7 and 8 are cold and software- or content-led.

### Cited Findings
- The chains are built from pushes and anxieties sourced in sections D–H (contract clauses, AWCI, BuildingConnected and ProEst reviews, Dodge/CMiC, AGC/Sage).

### Inferences (prompts are Simulated in the buyer's voice; frequencies are Speculative until coded interviews exist)

| # | Trigger (datable push) | Stage | Mode | Dominant restraining force | Exact prompt (first person) | Proof required |
|---|---|---|---|---|---|---|
| 1 | Owner asks Friday for an SD budget by Monday | Active looking | **Hot** | Anxiety: "will they hold me to it?" | "Owner just sent 30% SD drawings for a 3-story 60,000 sf medical office building in Fort Worth and wants a budget Monday. We're a $150M GC and my estimator is out. What's the fastest way to get a defensible conceptual estimate — can AI do it from the PDFs or should I outsource?" | Stated turnaround, price, a sample SD estimate with assumptions log, $/sf range for MOBs |
| 2 | Missed scope cost the firm at buyout | First thought → passive | Cold | Habit: "our Excel scope sheets work" | "We lost about $180K on a school job because the drywall and framing subs both excluded blocking. How do other GCs catch scope gaps between trades before buyout? Is there software that compares sub bids against the drawings?" | Scope-gap checklist by CSI division; leveling example showing a caught gap |
| 3 | Senior estimator quit; pipeline spike | Active looking | Warm/hot | Anxiety: outsourced quality, confidentiality | "We're a $90M open-shop GC in Houston with 5 pursuits due next month and we just lost our senior estimator. Compare hiring vs outsourcing precon estimating vs AI software — real costs and turnaround?" | Salary vs per-sf comparison, sample deliverable, NDA/security, similar-GC reference |
| 4 | Owner shifting to progressive design-build | Passive | Cold | Habit: "we've always hard-bid with sub numbers" | "We're pursuing our first progressive design-build K-12 project. What cost estimates does the GC deliver at each milestone, how much contingency is normal at SD, and what tools do DB contractors use for target value design?" | Milestone table (concept/SD/DD/GMP), UniFormat model template, DBIA-aligned language |
| 5 | Bid day with thin coverage | Active | **Hot** | Habit: phone + BuildingConnected | "Bid is due at 2 pm tomorrow on a $25M school and I only have one mechanical number and no drywall bids. How do I carry a number for uncovered trades without getting burned?" | Plug-number method, $/sf by trade, quick-takeoff path |
| 6 | CEO mandates an "AI plan" | Active | Cold | Anxiety: security, Procore fit, vendor risk | "Our CEO wants an AI plan for preconstruction. We're a $400M GC on Procore and Autodesk Construction Cloud. Which AI estimating tools actually work for commercial GCs, and how should I structure a 60-day pilot?" | Integration facts, SOC 2/data-use, pilot plan template, case study |
| 7 | Owner's cost consultant says the DD estimate is 12% high | Deciding (a defense, not a purchase) | Hot | Anxiety: credibility | "The owner's cost consultant says our DD estimate for a 120-unit multifamily project is 12% high. How do I reconcile two estimates line by line — UniFormat vs CSI — and present it?" | Reconciliation template, UniFormat↔CSI crosswalk, worked example |
| 8 | Sage/ProEst renewal or migration pain | Deciding | Cold | Habit: 15-year cost database | "We're on Sage Estimating with 15 years of cost history. Is moving to ProEst, DESTINI or an AI-based tool worth it, and how do we migrate our database?" | Migration path, import formats, total cost table, timeline |

### Gaps
- Chain frequencies need the framework's promotion threshold (≥3 of 12 interviews or ≥5 of 50 posts).

---

## N. Prompt matrix

### Takeaway
The matrix has 12 full-context prompts with persona facts, 6 short category prompts and 3 brand prompts. Brand prompts are tracked separately, because they mention the brand ~92% of the time vs ~20% for non-brand prompts (Momentic, per the framework). Demand tiers are **estimates** (heuristic: Reddit/thread density seen in prior audits, presence in vendor content, and fan-out obviousness). They are not measured volumes.

### Cited Findings
- Existing tracked GC prompts and results: T07 (C7, bid management for GCs → ConstructConnect, BuildingConnected, SmartBid, PlanHub, Procore, Kahua, Dodge; Quotr absent) and T41 (bid leveling → Buildertrend, Buildxact, SmartBid, Procore, Contractor Foreman; Quotr absent). The existing library also has GC prompts E-016, E-021 and E-079 — [local tracking-set.md](/home/user/quotr/geo-brain/04-prompt-library/tracking-set.md); [prompt-library.md](/home/user/quotr/geo-brain/04-prompt-library/prompt-library.md)

### Inferences

**Full-context first-person prompts (new; Simulated wording)**

| ID | Prompt | Intent | Stage | Urgency | Mode | Engine | Expected fan-out nodes | Demand tier (est.) |
|---|---|---|---|---|---|---|---|---|
| GC-F1 | "I'm precon manager at a $150M GC in Dallas (Procore, BuildingConnected, Excel). Owner wants a budget Monday from 30% SD drawings for a 60,000 sf medical office building. Can AI produce a defensible conceptual estimate from the PDFs, or should I outsource?" | do / choose-provider | Active | Acute | Hot | ChatGPT, AI Mode | conceptual estimate SD drawings; AI estimating software 2026; outsourced estimating services cost; MOB cost per sf 2026; reviews | 3 |
| GC-F2 | "We're a $90M open-shop GC in Houston, lost our senior estimator, and have 5 bids due next month. Compare hiring an estimator, outsourcing precon estimating and AI estimating software — cost and turnaround." | compare | Active | Acute | Warm | ChatGPT | estimator salary 2026; outsourced estimating cost per sf; AI estimating software for GCs; best 2026 | 3 |
| GC-F3 | "Chief estimator at a $400M GC on Procore and ACC. CEO wants an AI plan for preconstruction. Which AI estimating or bid-leveling tools actually work for commercial GCs, and how do I run a 60-day pilot?" | choose-provider | Active | Exploratory | Cold | ChatGPT, Perplexity | AI preconstruction software 2026; Procore integration; BuildingConnected AI; DESTINI; ProEst; SOC 2 | 3 |
| GC-F4 | "We lost $180K on a K-12 job in Georgia because drywall and framing both excluded blocking. How do GCs catch scope gaps before buyout, and is there software that compares sub bids to the drawings?" | learn → choose | First thought | Recurring | Cold | AI Mode, ChatGPT | scope gap checklist; bid leveling software 2026; AI bid leveling; Excel template | 3 |
| GC-F5 | "Bid day tomorrow on a $25M school in North Carolina; one mechanical number, no drywall. How do I carry uncovered trades and what $/sf should I plug?" | do | Active | Acute | Hot | ChatGPT | plug number; drywall cost per sf 2026; how many bids per trade; school construction cost per sf | 2 |
| GC-F6 | "First progressive design-build K-12 pursuit in Texas. What estimates does the GC deliver at each milestone, what contingency is normal at SD, and what tools do DB firms use for target value design?" | learn | Passive | Exploratory | Cold | ChatGPT, Claude | progressive design-build estimating; DBIA; target value design software; contingency at SD | 2 |
| GC-F7 | "Owner's cost consultant says our DD estimate for a 120-unit podium multifamily job in Phoenix is 12% high. How do I reconcile UniFormat vs CSI line by line?" | do | Deciding | Acute | Hot | ChatGPT | estimate reconciliation; UniFormat to MasterFormat crosswalk; multifamily cost per unit 2026 | 2 |
| GC-F8 | "We're a $250M GC on Sage Estimating with 15 years of cost history. Is moving to ProEst, DESTINI or an AI-based tool worth it, and how do we migrate the database?" | compare | Deciding | Recurring | Cold | ChatGPT, Perplexity | Sage Estimating alternatives; ProEst vs DESTINI; migration; pricing 2026; reviews | 2 |
| GC-F9 | "Data-center fit-out GC in Northern Virginia: owner wants a conceptual budget for a 20 MW hall's electrical and mechanical from a narrative and one-line diagrams. How do precon teams price that early?" | learn | Active | Acute | Hot | ChatGPT | data center construction cost per MW 2026; MEP conceptual estimate; AI estimating MEP | 2 |
| GC-F10 | "Precon director at a $600M healthcare GC: we level 30+ sub bids per pursuit in Excel and it takes 2 days. What AI bid-leveling tools work with BuildingConnected exports, and how accurate are they?" | choose-provider | Active | Recurring | Cold | ChatGPT, Perplexity | best bid leveling software general contractors 2026; AI bid leveling; BuildingConnected integration; reviews | 3 |
| GC-F11 | "We're a $40M Bay Area GC doing prevailing-wage public work. Can AI estimating tools handle California labor rates, or do I still need RSMeans plus local adjustments?" | validate | Passive | Exploratory | Cold | ChatGPT | California construction cost 2026; prevailing wage estimating; RSMeans city cost index; AI estimating accuracy | 1 |
| GC-F12 | "Is AI accurate enough for SD and DD estimates on commercial jobs? I need a number within ±10% of the final GMP before I'd show it to an owner." | validate/trust | Passive → Active | Exploratory | Cold | ChatGPT, AI Mode | AI takeoff accuracy; conceptual estimate accuracy ranges; AACE class; case study | 3 |

**Short category prompts** (some overlap existing IDs; noted)

| ID | Prompt | Intent | Stage | Mode | Expected fan-out | Tier (est.) |
|---|---|---|---|---|---|---|
| GC-S1 | best conceptual estimating software for general contractors 2026 | compare | Active | Cold | best / 2026 / DESTINI / reviews | 3 |
| GC-S2 | best bid leveling software for general contractors (≈ T41/E-012) | compare | Active | Cold | best / 2026 / vs / template | 4 |
| GC-S3 | AI preconstruction software (≈ E-016/E-021) | compare | Active | Cold | best / 2026 / Procore / Autodesk | 4 |
| GC-S4 | DESTINI Estimator alternatives | compare | Deciding | Cold | alternatives / reviews / pricing | 2 |
| GC-S5 | ProEst vs Sage Estimating vs WinEst | compare | Deciding | Cold | vs / reviews / pricing / 2026 | 2 |
| GC-S6 | outsourced preconstruction estimating services for general contractors (≈ E-079) | choose-provider | Active | Warm | cost per sf / turnaround / reviews | 3 |

**Brand prompts** (kept separate)

| ID | Prompt | Intent | Notes |
|---|---|---|---|
| GC-B1 | "Quotr.ai for general contractors — conceptual budgets and bid leveling?" | validate | Tests GC positioning; today there is no GC page to retrieve |
| GC-B2 | "Quotr vs DESTINI Estimator" | compare | No owned comparison exists |
| GC-B3 | "Does Quotr integrate with Procore and BuildingConnected?" (≈ D-037) | validate | Answer depends on confirmed integrations |

### Gaps
- Demand tiers are unvalidated. Use the framework's proxy stack (GSC 5+-word queries, Google volume × 0.115, a Profound trial for the top clusters) before prioritizing.

---

## O. Simulation

### Takeaway
1. A simulated ChatGPT journey for this persona most likely ends with a shortlist of incumbents (DESTINI, ProEst, Procore Estimating/BuildingConnected, STACK) plus outsourced estimating firms. Quotr is absent because nothing on quotr.ai answers the GC conceptual-budget or GC bid-leveling sub-queries.
2. The retrieval proxies show three winning formats: vendor "best X 2026" lists for bid leveling (now crowded by new AI startups), review directories for incumbent "reviews/cons/alternatives" nodes, and long methodology guides (Procore Library, Trimble, EC&M) plus contract-clause sites for conceptual-estimating how-to.
3. Verdict: winnable clusters are SD-budget service ("hot") and conceptual-estimating method. Bid leveling is contestable but crowding fast. Incumbent comparisons are winnable only with review mass. "AI preconstruction software" head terms are a long haul.

### Cited Findings
**(1) SIMULATED ChatGPT conversation.** This is illustrative only: no engine was queried. The brand names reflect the retrieval proxies below and prior Perplexity tests.

> **Persona (simulated):** Dana, precon manager, $150M open-shop GC, Fort Worth; healthcare + multifamily; Procore, BuildingConnected, Bluebeam, Excel; 2 estimators.
>
> **Turn 1 — Dana:** "Owner sent 30% SD drawings for a 60,000 sf MOB and wants a budget Monday. Drawings don't show wall types. How do GCs usually handle this?"
> **ChatGPT (simulated):** Explains a parametric/UniFormat approach, $/sf ranges for MOBs, an assumptions log, and design contingency at SD. Cites a Procore Library-type guide and an estimating-firm page. No software named.
>
> **Turn 2 — Dana:** "Is there AI that can do this from the PDFs?"
> **ChatGPT (simulated):** Lists AI takeoff tools (Togal, STACK, Beam, Kreo) with a caveat that takeoff ≠ conceptual estimate. Mentions DESTINI for conceptual/assembly-based estimating and Procore Estimating. May mention outsourced estimating services.
>
> **Turn 3 — Dana:** "We're on Procore. Which of those integrate, and which are actually used by mid-size commercial GCs?"
> **ChatGPT (simulated):** Favors Procore Estimating and the Autodesk stack (ProEst, BuildingConnected) for ecosystem fit, and DESTINI for conceptual work. Fan-out adds "Procore integration", "reviews", "2026".
>
> **Turn 4 — Dana:** "I need something by Monday — would outsourcing be faster?"
> **ChatGPT (simulated):** Names estimating-service firms seen in prior tests (e.g., blazeestimating, 1800estimating, optimarprecon) and generic per-sf pricing. Quotr's service post might be cited without being named, as happened in C12 ("cited, not named").
>
> **Turn 5 — Dana:** "Give me a shortlist with pricing and a pilot plan."
> **ChatGPT (simulated):** Shortlist: DESTINI Estimator, ProEst, Procore Estimating, STACK, plus 1–2 outsourced estimating firms. **Quotr absent**, because no GC page, no comparison page, no review mass and no published SD method or variance data exist to match the sub-queries.

**(2) Retrieval proxy — not an AI engine answer.** These are WebSearch runs from this session (November 6, 2026), which approximate the engine fan-out nodes.

| # | Query run (≈ fan-out node) | Top domains returned | Brands named | Quotr? | Winning format |
|---|---|---|---|---|---|
| R1 | "reddit r/ConstructionManagers preconstruction estimating software AI bid leveling" (≈ "AI bid leveling software for GCs") | downtobid.com, app.dealroom.co, beck-technology.com, omnionlinestrategies.com, g2.com (Buildr, Axiom, BudgetBuilder), constructconnect.com, constructionplacements.com, chetu.com, nomic.ai, meltplan.com | RedTeam, Belidor, Consight/BudgetBuilder, Buildr, Axiom Estimating, DESTINI | **No** | Vendor guides and "AI bid leveling tools" lists; G2 product pages |
| R2 | "site:reddit.com estimators bid leveling excel general contractor" (≈ "bid leveling template/excel") | imagetotable.ai, omnionlinestrategies.com, archdesk.com, autodesk.com (BuildingConnected), buildxact.com, constructionplacements.com, crewcost.com, meltplan.com ("Best Bid Leveling Software for General Contractors (2026 Comparison)") | BuildingConnected, Buildxact, Meltplan | **No** (Reddit not returned) | Vendor how-to + dated "2026 comparison" listicle |
| R3 | "reddit estimators conceptual estimate schematic design owner wants budget" (≈ "how to do a conceptual estimate from SD") | procore.com/library (14-min guide), lawinsider.com, cca-acc.com, coaa.org, trimble constructible, ecmweb.com, montgomerycountymd.gov | Procore (as publisher) | **No** | Long methodology guide; contract-clause pages |
| R4 | "r/estimators general contractor estimator budget schematic drawings owner deadline" | lawinsider.com (×4), onlinedigeditions.com (AWCI), dcd.com, tylerestimating.com, content.aia.org (SD checklist), open-exam-prep.com | — | **No** | Clause libraries, association checklists, estimating-firm service pages |
| R5 | "Construction Dive preconstruction director AI estimating general contractor conceptual budgets 2026" (≈ "AI preconstruction 2026") | constructiondive.com (sponsored), autodesk.com, nomic.ai, buildops.com, job boards | Autodesk, BuildOps | **No** | Sponsored trade-media post; vendor blog |
| R6 | "DESTINI Estimator reviews G2 Beck Technology conceptual estimating" (≈ "DESTINI reviews") | g2.com, softwarefinder.com, getapp.*, softwareadvice.*, capterra.* (6+ country mirrors), sourceforge.net, softwarereview.com | DESTINI, Zebel (compare) | **No** | Review directories |
| R7 | "ProEst Autodesk review cons estimators" (≈ "ProEst reviews/cons") | capterra.* (10+ mirrors), getapp.*, softwareadvice.*, trustradius.com, softwareconnect.com, g2.com | ProEst | **No** | Review directories |
| R8 | "Sage Estimating review cons outdated" (≈ "Sage Estimating alternatives") | softwarefinder.com, trustradius.com (compare pages vs Fast Track, TradeOff, 4castplus, Provision, Methvin), capterra.com, g2.com (vs STACK, CoConstruct), selecthub.com | Sage Estimating, STACK, ProEst-like peers | **No** | Review directories + G2/TrustRadius compare pages |
| R9 | "Procore estimating module review cons" (≈ "Procore Estimating vs …") | buildern.com (competitor blog), capterra.* compare pages (Procore vs ProContractor, MeasureSquare, McCormick), trustradius.com, g2.com ("ProEst, Trimble WinEst vs Procore") | Procore, ProEst, WinEst | **No** | Competitor "where it gets complicated" review page; directory compares |
| R10 | "BuildingConnected reviews cons bid invites subcontractors" (≈ "BuildingConnected alternatives") | trustradius.com, downtobid.com (vendor review post), capterra.com, softwareadvice.com, getapp.ca, selecthub.com, sourceforge.net | BuildingConnected, PlanHub, ConstructConnect | **No** | Directories + competitor review post |
| R11 | "reddit estimators AI takeoff doesn't work skeptical" (≈ "is AI takeoff accurate") | constructconnect.com ("Are AI takeoffs accurate in 2026"), reddit mirror snapshots, oncenter.com, bricks-bytes newsletter, togal.ai | ConstructConnect, On-Screen Takeoff, Togal | **No** (an earlier Perplexity test cited Quotr's accuracy post first, not named) | Dated incumbent "accuracy 2026" guide |

**(3) Gap verdict per prompt cluster**

| Cluster | Who owns retrieval today | Quotr asset today | Verdict | Why |
|---|---|---|---|---|
| Hot SD budget / "need a budget by Monday" (GC-F1, F2, S6) | Estimating-service firm pages; Procore Library | Service page (not GC-framed); preconstruction-services post | **Winnable — priority 1** | Service pricing per sf is a unique fact; service firms have thin pages; needs confirmed turnaround and a sample SD deliverable |
| Conceptual-estimating method (GC-F6, F7, F12) | Procore Library, Trimble, EC&M, Law Insider, AIA | None GC-specific | **Winnable — priority 2** | Methodology pages win; add original $/sf benchmarks and variance data to out-evidence Procore |
| Bid leveling / scope gaps (GC-F4, F10, S2) | Meltplan 2026 comparison, ConstructionPlacements, Archdesk, Downtobid, new AI startups (Belidor, BudgetBuilder, Axiom, Buildr) | Dictionary term; scope-gap post | **Contestable, crowding fast** | Needs a confirmed GC-side feature first; then a template plus guide; avoid a self-ranked list |
| Incumbent comparisons (GC-F8, S4, S5, B2) | Review directories + competitor review posts (Buildern, Downtobid) | None vs DESTINI/ProEst/Sage | **Winnable on owned pages; directories need reviews** | Competitor "where it gets complicated" posts show honest incumbent reviews get retrieved |
| AI preconstruction head terms (GC-F3, S1, S3) | Autodesk, Procore, ConstructConnect, listicles, sponsored trade media | State of AI post (weak) | **Long haul** | Needs earned media, reviews and an original-data report |
| Bid-day coverage (GC-F5) | Method pages; bid-platform vendors | None | **Winnable (low volume)** | Answer page with plug-number method and trade $/sf |
| Geo/labor-basis (GC-F9, F11) | Cost-data publishers (RSMeans), local firms | California estimating post | **Selective** | Only where Quotr has job data |

### Gaps
- No live ChatGPT, AI Mode or Perplexity runs were made for these prompts in this pass, and the search budget ran out before a dedicated fan-out batch. Baseline each GC prompt 3–5× per engine before acting.

---

## P. GEO system for this ICP on quotr.ai

### Takeaway
Build one GC hub, two urgent service pages and three considered method pages, then add three honest comparison pages and four answer pages. Back them with two original-data assets (SD-vs-final variance; $/sf benchmarks from Service jobs). Off-site, prioritize review mass and trade-media data placements over Reddit. Several pages are blocked on Quotr confirmations:
- GC-side bid leveling
- Service turnaround
- integrations
- SOC 2 status
- Salisbury Moore's firm type and permissions

### Cited Findings
- Engines rewrite prompts into sub-queries with "best/reviews/2026/vs/price/official", and title/slug match to sub-queries predicts citation — framework file; [Ahrefs](https://ahrefs.com/blog/why-chatgpt-cites-pages/) (via prior audit)
- Self-ranked listicles backfire: 69% of the time the publisher was not recommended — [ALM Corp / Lily Ray](https://almcorp.com/news/self-promotional-listicles-ai-overviews-help-competitors-lily-ray-study/) (via prior audit)
- Original data earns ~3.3× citation density (Growth Memo) — [Growth Memo](https://www.growth-memo.com/p/why-most-original-data-never-gets) (via prior audit)
- Quotr has no GC page, GC case study or bid-leveling page; the preconstruction-services post pitches Service as capacity — [local audiences-and-personas.md](/home/user/quotr/geo-brain/00-quotr/audiences-and-personas.md)

### Inferences — owning pages (titles and slugs; "U" = urgent mode, "C" = considered mode)

| # | Page | Slug | Mode | Lead content (first 60 words) | Blockers |
|---|---|---|---|---|---|
| 1 | **Quotr.ai for General Contractors: Conceptual Budgets, AI Takeoff and Bid Comparison for Precon Teams** | `/general-contractors/` | C (hub) | Who it is for ($20M–$1B commercial GCs); 3 jobs; Software vs Service; prices; links | Confirm GC-side leveling and integrations |
| 2 | **Schematic Design Budget, Fast: Turnaround, Price per sq ft and Sample Deliverable** | `/service/schematic-design-budget/` | **U** | "Send SD PDFs → conceptual estimate in [confirmed SLA]; $0.25/sf under 50k sf, $0.10/sf above; includes assumptions log, UniFormat summary, alternates" + Start button | **Resolve turnaround conflict first** |
| 3 | **Precon Capacity on Demand: Outsource GC Estimating Without Hiring** (refresh of /blog/preconstruction-services/) | `/service/preconstruction-estimating-for-gcs/` | U | Cost vs hiring (salary bands sourced), turnaround, NDA/security | Same |
| 4 | **Conceptual Estimating From Schematic Drawings: Method, Accuracy Ranges and Contingency (2026)** | `/conceptual-estimating/` | C | Step method; estimate classes; $/sf benchmark table by building type (from Service jobs) | Needs Quotr data for the benchmark table |
| 5 | **ROM vs SD vs DD vs CD Estimates: What Owners Should Expect at Each Stage** | `/blog/rom-sd-dd-cd-estimates/` | C | Table: drawing completeness, accuracy band, contingency, deliverable | AACE ranges verified |
| 6 | **Subcontractor Bid Leveling: Step-by-Step Guide + Free Template (2026)** | `/bid-leveling/` (+ template download) | C | Steps, scope sheet, normalization, exclusions matrix; template | GC-side feature confirmation for the product CTA |
| 7 | **Scope Gap Checklist by CSI Division for GC Bid Packages** | `/scope-gap-checklist/` | C | Division-by-division common exclusions (blocking, firestopping, temporary protection…) | None |
| 8 | **Bid Day With Thin Coverage: How to Carry Uncovered Trades** | `/blog/bid-day-uncovered-trades-plug-numbers/` | U | Plug-number method, $/sf by trade, risk notes | Trade $/sf data |
| 9 | **Quotr vs DESTINI Estimator (2026): Conceptual Estimating Compared** | `/compare/quotr-vs-destini-estimator/` | C | Honest table: assemblies/cost DB depth (DESTINI) vs AI from PDFs + done-for-you (Quotr); pricing; who should pick which | Monthly refresh |
| 10 | **Quotr vs ProEst (2026)** | `/compare/quotr-vs-proest/` | C | Same pattern; ACC ecosystem fit stated fairly | Monthly refresh |
| 11 | **DESTINI vs ProEst vs Sage Estimating vs WinEst: Which Fits a Mid-Size GC?** | `/compare/gc-estimating-software/` | C | Neutral 4-way table; Quotr in a clearly labeled "AI-first alternative" row, **not ranked #1** | Monthly refresh |
| 12 | Answer: **Can AI Estimate From Schematic Design Drawings?** | `/answers/ai-estimate-schematic-drawings/` | U/C | Direct yes/no with limits, accuracy data, method | Needs variance data |
| 13 | Answer: **Does Quotr Use Our Drawings to Train AI? Security and Data Use** | `/security/` | C | Data-use policy, encryption, SOC 2 status/roadmap, retention, SSO | Confirm facts |
| 14 | Answer: **Does Quotr Work With Procore, ACC/BuildingConnected and Excel?** | `/integrations/` | C | Named integrations and export formats (Excel export conflict to resolve) | Confirm facts |
| 15 | Answer: **Progressive Design-Build Estimating: What the GC Delivers at Each Milestone** | `/blog/progressive-design-build-estimating/` | C | Milestone table; TVD; contingency | None |
| 16 | Geo (one only, initially): **California Commercial Construction Costs: Prevailing Wage, Union Rates and Conceptual Estimating** | `/california-construction-costs/` | C | Labor-basis table; Quotr Bay Area job data | Needs data |

**Proof assets and original data (in order of value)**
1. **SD/DD estimate vs final bid/buyout variance study.** Use 20–50 Quotr Service jobs, anonymized, with a dated methodology page. This is the single highest-value asset for chains 1, 6 and 12.
2. **Cost-per-sf benchmarks by building type and region, from Service jobs**, refreshed quarterly. It feeds pages 2, 4, 8 and 16.
3. **"State of Precon Capacity 2027" survey** of 100–200 precon managers (bid-day coverage, leveling hours, AI use), partnered with an AGC chapter or ASPE. It replaces the weak "State of AI in Preconstruction" post.
4. **One numbers-first GC case study.** First confirm whether Salisbury Moore or AlphaX is a GC; publish with permission, named role and before/after numbers.
5. **Downloadables:** bid-leveling template, scope-gap checklist, SD assumptions-log template.

**Off-site placements, ranked by leverage per hour (Likely)**
1. **G2 + Capterra review drive** in the "construction estimating" and "preconstruction/bid management" categories, from existing commercial customers. Review directories own every incumbent "reviews/cons/alternatives" node (R6–R10).
2. **Listicle/guide inclusion pitches** to independent or semi-independent lists that rank for bid leveling and AI precon (ConstructionPlacements "AI bid leveling tools"; construction.com bid-management list; ConstructConnect's 2026 AI takeoff guide), with a 40–60-word paste-ready blurb.
3. **Trade-media data placement:** a contributed piece in Construction Dive, ENR or For Construction Pros built on asset 1 or 2. Earned media is ~84% of AI citations (Muck Rack, via prior audit).
4. **LinkedIn articles** by the founders and a Quotr senior estimator (monthly; data-led).
5. **YouTube:** a chaptered demo, "30% SD set → conceptual budget", plus a bid-leveling walkthrough. This feeds Google AIO and AI Mode.
6. **Association presence:** an AGC chapter or ABC webinar; DBIA content on progressive DB estimating; ASPE chapter talk.
7. **Procore App Marketplace / Autodesk App Store listing**, only if a real integration exists. Marketplaces are citable directories for "integrates with Procore" sub-queries.
8. **Reddit** (r/estimators, r/ConstructionManagers): disclosed founder answers on conceptual estimating and leveling. Treat as wording and community trust; it is a weak ChatGPT citation lever after the August 2026 drop.

**Refresh cadence:**
- monthly: comparison pages, pricing, integrations, escalation/benchmark tables
- quarterly: the hub and method pages
- annually: the survey and variance study (with a dated methodology)

**Tracking prompts to freeze** (run 3–5×/week on ChatGPT and Google AI Mode; report at cluster level with ± ranges)
1. GC-F1 (hot SD budget, full context)
2. GC-F4 (scope gap → software)
3. GC-F10 (AI bid leveling for a healthcare GC)
4. GC-F12 (is AI accurate enough for SD/DD)
5. GC-S1 "best conceptual estimating software for general contractors 2026"
6. GC-S2 "best bid leveling software for general contractors" (≈ T41)
7. GC-S6 "outsourced preconstruction estimating services for general contractors" (≈ E-079)
8. GC-B2 "Quotr vs DESTINI Estimator" (brand group, reported separately)

**Do / skip / ignore**
- **Do:**
  - resolve the five blockers (GC-side leveling, turnaround, integrations, SOC 2/data use, customer permissions)
  - build the hub plus urgent SD-budget page first
  - publish the variance study
  - build honest incumbent comparisons
  - run the review drive and a bid-leveling template
  - add one California cost page
  - freeze the 8 prompts
- **Skip:**
  - metro-templated geo pages (scaled-content risk)
  - a self-ranked "best precon software" list
  - claiming bid leveling or Procore integration before confirmation
  - Reddit as a primary citation bet
  - schema or llms.txt as citation levers
  - generic "AI-powered" copy without numbers
- **Ignore:**
  - head-term "construction management software" prompts (owned by the Procore/Autodesk platforms)
  - hyperscale data-center prime-contractor prompts (not mid-market GC buying)
  - single-run "AI rank" snapshots

### Gaps
- All page plans depend on Quotr confirmations listed in the blockers. No engine baseline was run for the new GC prompts in this pass.

---

## Q. Known / likely / speculative

### Takeaway
The demand-side facts are well-sourced: the market direction, AI attitudes and the incumbents' review complaints. The ICP's size, team sizes, sales cycle and Quotr's GC-specific capabilities are not.

### Cited Findings
- See the citations in sections A–P.

### Inferences

| Claim class | Known (sourced) | Likely (inference; label it) | Speculative (validate first) |
|---|---|---|---|
| ICP size | SUSB 2000s: ~40k firms in 23622, 17.6–18.1% with 20+ employees; SBA $45M line; ENR No. 394 = $253M, No. 150 ≈ $870M; Top 400 revenue $671.4B | ~4,000–7,000 ICP firms (estimate); ~250–270 ENR firms in $250M–$1B | 10,000–50,000 precon seats; team sizes 2–10 |
| Pay | Precon manager $104K–$135K mid-range (Payscale/Salary.com/TBG); chief estimator/VP $161K–$269K base (TBG) | Loaded cost ≈ $160K+/precon FTE | Bonus share |
| Market 2026 | Nonres starts +23.7% YTD (Sept); C&I +47.7% YTD (Aug) on data centers; nonres ex-data-centers −12.7%; AGC data center net +57; lodging, office and retail weakest; multifamily +12.7% (12 months to May) | Texas, Southeast and data-center corridors hold the most mid-market GC activity | State/metro rankings (not retrieved); rate-cut restarts |
| Buyer psychology | Accuracy 57% / security 54% concerns; trust in AI −14 pts; 61% using or increasing AI; 23% estimating use; G2 51% start research in chatbots | Anchoring on the first SD number; Procore/Excel default; pilots on live pursuits | Pilot length; approver chain; frequency of each chain |
| Incumbent gaps | ProEst revision switching, report writer, value 3.7; Sage not cloud; Procore cost and complexity; BuildingConnected sub response and versioning; DESTINI learning curve; Excel leveling default | Conceptual-from-incomplete-drawings and leveling are the top unmet needs | Exact frequency ranking (needs coded interviews/posts) |
| Competitive search landscape | Directories own incumbent review nodes; vendor 2026 lists own leveling; Procore Library and Trimble own method; new AI leveling startups (Belidor, BudgetBuilder, Axiom, Buildr); Quotr absent in all 11 proxies and in C7/T41 | Hot SD-budget and method clusters are winnable first | Time to first citation for a new GC hub |
| Quotr facts | Pricing; Service $/sf; no GC page; no SOC 2 statement; no named integrations; turnaround conflict; Salisbury Moore = "active commercial estimating customer" (index text) | Service fits the hot chains best | GC-side bid leveling; Procore integration; accuracy vs final cost |

### Gaps
- **Network-blocked this pass:** Census CBP/SUSB current counts; Dodge/ConstructConnect state rankings; on-page verification of every review quote (G2/Capterra/TrustRadius); Reddit thread mining and subreddit sizes; LinkedIn and podcast verbatims from named precon leaders; Procore/Autodesk 2026 pricing changes; union and prevailing-wage state tables.
- **Next pass:** allow g2.com, capterra.com, reddit.com, census.gov and constructconnect.com in the session's network settings. Then pull the CBP 236220 table, verify quotes Q1–Q14 on-page, and run the 12 full-context prompts 3–5× in ChatGPT and AI Mode for a baseline.
