# US Geography-to-Segment Pipeline for Quotr.ai's Construction ICPs (state + metro index)

Status as of 2026-11-06. **Read this first:** this session could not reach the primary data hosts. `api.census.gov`, `www2.census.gov`, `census.gov`, `www.bls.gov`, `eyeonhousing.org`, `ncarb.org` and `news.agc.org` all failed DNS/proxy resolution (WebFetch "ENOTFOUND"; curl "CONNECT tunnel failed, response 403"). The shared web-search budget (200 calls per turn, shared by all researchers) ran out after this researcher's 9th query. The notes therefore use (a) this researcher's 9 searches, (b) web-search results already gathered in this same session by the sibling ICP researchers (original URLs cited), and (c) Quotr's own repo notes. **The state-by-NAICS establishment tables (Layer 1) and the full OEWS state/metro tables (Layer 3) could not be pulled.** The pipeline, join keys, exact pulls and weights are fully specified, so a session with `census.gov` and `bls.gov` allowed can fill them in about 6–10 hours. Every number below carries its release year. Labels: **[M]** measured by the cited source, **[P]** proxy, **[J]** researcher judgment, **[U]** unverified (secondary site or search summary; page not opened).

---

## 1. Unit choice and joins (Step 0): how should the pipeline be built for US construction?

### Takeaway
Run a 50-state + DC first pass, then about 33–40 metros keyed by **5-digit CBSA code**. All federal layers (CBP, SUSB, BPS, OEWS, QCEW) join on state FIPS or CBSA. Only the demand-signal layer (Google Trends and Keyword Planner) is DMA-based, so it needs a documented DMA→CBSA allocation. Unlike the Louisiana ADHD case, the core ICP variable (establishment counts by NAICS) **is measured** at state and metro level. The proxy problem moves to the *pain* layer (estimator scarcity, cost per sq ft) and the *demand-signal* layer.

### Cited Findings

**Data sources, release vintage and join key**

| Layer | Dataset (latest vintage found) | Geography published | Join key | Source / note |
|---|---|---|---|---|
| 1 Concentration | County Business Patterns **2023** (released **June 26, 2025**); employer establishments, March-12 employment, payroll; 2017 NAICS | National, state, CSA, MSA/μSA, county, congressional district, ZIP | State FIPS; CBSA | [Census press release 2025](https://www.census.gov/newsroom/press-releases/2025/2023-county-business-patterns.html); [CBP API docs](https://www.census.gov/data/developers/data-sets/cbp-zbp/cbp-api.html) |
| 1 Concentration (firm size) | SUSB **2022** annual tables (state × NAICS × enterprise size), published April 2025 | US and states | State FIPS | [Census SUSB 2022](https://www.census.gov/data/tables/2022/econ/susb/2022-susb-annual.html) (via sibling ICP2 search) |
| 1 Caveat | Census says CBP should not be used as a time series | — | — | [Census CBP FAQ / API page](https://www.census.gov/programs-surveys/cbp/data/api.html) (via sibling ICP4 search summary) |
| 3 Pain | OEWS **May 2025** estimates are out (metro news releases dated May 2025); based on six semiannual panels over 3 years | National, state, MSA, BLS nonmetro areas | State FIPS; MSA code (≈CBSA) | [BLS OEWS May 2025 technical notes](https://www.bls.gov/oes/2025/may/oes_tec.htm); [BLS May 2025 release PDF](https://www.bls.gov/news.release/pdf/ocwage.pdf); mirror: [Virginia Open Data OEWS state May 2025](https://data.virginia.gov/dataset/oews-state-may-2025) |
| 3 Pain | Location quotient = local occupational concentration ÷ national; >1 = more concentrated than the US | — | — | [BLS OEWS Cost Estimators May 2023](https://www.bls.gov/oes/2023/may/oes131051.htm) |

**Reference CBSA codes for the metro pass (identifiers; check against the OMB 2023 delineation file before joining)** [J; codes recalled, not re-fetched]

| Metro | CBSA | Metro | CBSA | Metro | CBSA |
|---|---|---|---|---|---|
| New York–Newark–Jersey City | 35620 | Los Angeles–Long Beach–Anaheim | 31080 | Chicago–Naperville–Elgin | 16980 |
| Dallas–Fort Worth–Arlington | 19100 | Houston–Pasadena–The Woodlands | 26420 | Atlanta–Sandy Springs–Roswell | 12060 |
| Washington–Arlington–Alexandria | 47900 | Miami–Fort Lauderdale–West Palm Beach | 33100 | Phoenix–Mesa–Chandler | 38060 |
| Boston–Cambridge–Newton | 14460 | Riverside–San Bernardino–Ontario | 40140 | San Francisco–Oakland–Fremont | 41860 |
| Seattle–Tacoma–Bellevue | 42660 | Tampa–St. Petersburg–Clearwater | 45300 | San Diego–Chula Vista–Carlsbad | 41740 |
| Denver–Aurora–Centennial | 19740 | Orlando–Kissimmee–Sanford | 36740 | Charlotte–Concord–Gastonia | 16740 |
| San Antonio–New Braunfels | 41700 | Austin–Round Rock–San Marcos | 12420 | Portland–Vancouver–Hillsboro | 38900 |
| Sacramento–Roseville–Folsom | 40900 | Las Vegas–Henderson–North Las Vegas | 29820 | Columbus, OH | 18140 |
| Nashville–Davidson–Murfreesboro–Franklin | 34980 | San Jose–Sunnyvale–Santa Clara | 41940 | Jacksonville | 27260 |
| Raleigh–Cary | 39580 | Salt Lake City–Murray | 41620 | Reno | 39900 |
| Syracuse | 45060 | Asheville | 11700 | Kahului–Wailuku (Maui) | 27980 |

### Inferences
- **Unit choice.** State first: licensing, energy code, prevailing wage and housing law are state-made, and they decide whether a geo page is legitimate. Metro second: construction labor markets, cost indices (RLB/Cumming/Turner) and permit data are metro-native. ZIP/ZCTA is unnecessary for a B2B estimating product. Exception: the LA rebuild zone, which should be drawn at the burn-perimeter level (Palisades in the City of LA; Altadena in unincorporated LA County).
- **Step 1 pulls (exact, for the follow-up session):**
  - CBP 2023: `api.census.gov/data/2023/cbp?get=NAME,NAICS2017,ESTAB,EMP,PAYANN&for=state:*&NAICS2017={code}`, then the same with `for=metropolitan statistical area/micropolitan statistical area:*`.
  - Codes: 236115, 236116, 236117, 236118, 236220, 238210, 238220, 238310, 238330, 238160, 238110, 238320, 238340, 541310.
  - Add `EMPSZES` for size bands. Size bands separate ICP1 (owner-estimator, 1–9 employees) from ICP2 (mid-size, 20–499).
  - Add Nonemployer Statistics for 236118 and 238xxx. Remodelers and finish trades are heavily non-employer.
- **Step 2:** join on state FIPS or CBSA; min–max normalize within the unit; invert "good-is-low" variables; flag OEWS-suppressed cells.
- **Join gotchas** [J]:
  - BPS, CBP and OEWS adopted the 2023 OMB delineations at different times, so metro boundaries can differ by vintage.
  - Connecticut's 2022 switch from counties to planning regions breaks county-level joins across years.
  - OEWS publishes some BLS-defined nonmetropolitan areas that have no CBSA.
  - DMAs do not nest in CBSAs (see Section 6).

### Gaps
- Could not open the Census API, BPS text files or OEWS tables (host blocked). Release dates for **CBP 2024** (expected around mid-2026) and the official **OEWS May 2025 national release date** could not be confirmed.
- CBSA codes above are from recall; verify against the OMB Bulletin 23-01 delineation file.

---

## 2. Layer 1: Where do the ICPs concentrate (establishments by NAICS, state and metro)?

### Takeaway
National 2023 counts were found (via secondary sites citing CBP). The **state and metro top-10 tables per NAICS could not be pulled.** Measured proxies (estimator employment, all-industry establishments, permits) put **California, Texas and Florida first** in absolute size in every group. New York and Pennsylvania come next for estimators. Small, owner-run shops dominate: about 90% of electrical contractors have fewer than 20 employees [U]. That makes ICP1/ICP3 a long tail, not a metro-elite phenomenon.

### Cited Findings

**National ICP pool by NAICS (CBP 2023 unless stated)**

| ICP | NAICS | Establishments | Employees | Year / source | Label |
|---|---|---|---|---|---|
| ICP1/2 electrical | 238210 | 83,342 | 1,015,983 | CBP 2023 via [naicscodes.org](https://naicscodes.org/naics-code-for/electricians/), [startbusinessbystate](https://startbusinessbystate.com/electrician-industry-statistics/) | [U] |
| ICP1/2 electrical (firms) | 238210 | 79,611 firms with employees; 89.7% of businesses <20 employees; 50.1% receipts <$500k | — | SUSB 2022 via [tradesindex](https://tradesindex.org/trades/electrical/), [electriciansalary](https://electriciansalary.com/electrical-contractor-owner-salary) | [U] |
| ICP1/2 electrical (nonemployers) | 238210 | 159,693 nonemployer businesses (excluded from CBP) | — | Nonemployer Statistics via [startbusinessbystate](https://startbusinessbystate.com/electrician-industry-statistics/) | [U] |
| ICP1/2 plumbing/HVAC | 238220 | 111,207 | 1,214,761 | CBP 2023 via [naicslist](https://naicslist.com/naics/238220), [vantainsights](https://vantainsights.com/industry/238220-plumbing-heating-air-conditioning); 76.8% of establishments <10 employees (aggregator) | [U] |
| ICP3 drywall/insulation | 238310 | 20,760 | 250,758 | CBP 2023 via [Vantage Insights](https://vantainsights.com/industry/238310-drywall-insulation-contractors) | [U] |
| ICP3 roofing | 238160 | 25,519 (24,532 in 2022) | 215,242 | CBP 2023 via [naicscodes.org](https://naicscodes.org/code/238160-roofing-contractors), [theroofingbrief](https://theroofingbrief.com/us-roofing-contractor-count-report/) | [U] |
| ICP3 flooring | 238330 | not found (naics.com "12,626 business entities", undated; not CBP) | — | [naics.com](https://www.naics.com/six-digit-naics/?code=23) | gap |
| ICP3 concrete / painting / tile | 238110 / 238320 / 238340 | not found | — | — | gap |
| ICP5 single-family GCs | 236115 | 60,635 (CBP 2023, one aggregator) vs 59,568 (undated) | — | [vantainsights](https://vantainsights.com/industry/236115-new-single-family-housing-construction), [mewayz](https://data.mewayz.com/industry/236115) | [U], conflicting |
| ICP5/6 for-sale builders | 236117 | 12,612 establishments; 11,761 firms; 130,923 employees (year unclear) | — | [mewayz](https://data.mewayz.com/industry/236117) | [U] |
| ICP4 commercial GCs | 236220 | not found | — | — | gap |
| ICP10 architects (firms) | 541310 | not found | — | — | gap |
| ICP10 architects (people) | licensed architects | 116,005 in 2024 (NBTN 2025); **+6% in 2025** (NBTN 2026; total not surfaced) | — | [archcareersguide 2025](https://www.archcareersguide.com/?p=13710); [archcareersguide 2026](https://www.archcareersguide.com/ncarb-by-the-numbers-2026/) | [U] |
| Context: Hispanic-owned construction employer firms | 23 | 70,571 firms (2021 data, ABS 2022), top sector among 406,086 Hispanic-owned employer firms | — | [Census ABS story 2024](https://census.gov/library/stories/2024/10/hispanic-owned-businesses.html) (via sibling search) | [M] via summary |
| Context: Hispanic share of construction labor force | — | **32.8% (2024)** vs 19.9% all industries | — | [NAHB Eye on Housing, Oct 2025](https://eyeonhousing.org/2025/10/hispanics-comprise-nearly-one-third-of-the-construction-labor-force/) | [M] via summary |

**State-level concentration proxies actually obtained**

| State | Cost estimators employed, OEWS **May 2023** | All-industry employer establishments, CBP **2023** | 2025 housing units permitted (BPS 2025) |
|---|---|---|---|
| California | **25,850** | 1,029,689 [U] | 103,856 [U] |
| Texas | **20,240** | 670,877 [U] | **210,217** [U] |
| Florida | **14,150** | 645,575 [U] | 178,297 [U] |
| New York | 9,680 | — | — |
| Pennsylvania | 9,620 | — | — |
| North Carolina | — | — | 86,167 [U] |
| Georgia | — | — | 61,196 [U] |

Sources: OEWS from [BLS OEWS Cost Estimators May 2023](https://www.bls.gov/oes/2023/may/oes131051.htm) (search summary of the BLS page; [CareerExplorer](https://www.careerexplorer.com/careers/cost-estimator/job-market/) gives a different undated set: CA 26,020, TX 20,760, FL 13,720, NY 11,980, PA 9,420). Establishments from [interobservers](https://interobservers.com/desk/data/county-business-patterns/) citing CBP 2023. Permits from [Buildermuse](https://buildermuse.com/residential/top-10-states-for-residential-construction-in/) citing the Census BPS 2025 annual state file.

### Inferences
- **Likely ordering for every trade NAICS (absolute counts):** CA, TX, FL lead; NY, PA, IL, GA, NC, OH, AZ, WA, NJ, VA follow. Basis: the estimator and all-industry orderings above plus permit volume. This is a prior, not a measurement. Per-capita concentration (the variable that stops "biggest state wins") is unknown until CBP is pulled.
- **Size bands matter more than totals.** ICP1 (owner-estimator) is the ~90% of electrical and plumbing/HVAC shops under 20 employees, plus non-employers. ICP2 (chief estimator) is the 20–499 band. Geo targeting for ICP1 should follow *permit volume and new-household growth* (where small shops form). ICP2 should follow *nonresidential megaproject pipelines* (Section 3).
- **Language is a geographic variable.** With 32.8% of the construction labor force Hispanic (2024) and construction the top sector for Hispanic-owned employer firms, Spanish-language trade content is a real lever in TX, FL, CA, AZ and NV. The state shares were not pulled.

### Gaps
- **Top-10 states and top-10 metros per NAICS group (the core Layer 1 deliverable) were not obtained.** Pull CBP 2023 by state and MSA for the 14 codes in Section 1 (about 28 API calls), plus SUSB 2022 state × size.
- No count found for 236220, 238330, 238110, 238320, 238340 or 541310 establishments.
- NCARB state-by-state architect counts (NBTN 2026 "State of Licensure") not opened (ncarb.org blocked).
- The secondary-site national counts should be re-verified against data.census.gov table CB2300CBP.

---

## 3. Layer 2: Where is estimating demand growing fastest (permits, spending, starts, megaprojects)?

### Takeaway
**Residential volume** is concentrated in Texas (210,217 units; 140,002 single-family permits in 2025), Florida and the Carolinas/Georgia, but is **shrinking**: US single-family permits were −2.6% YTD through August 2026. **Nonresidential growth is almost entirely data centers.** Census put data-center construction at a $50.7B annual rate in April 2026 (rising to roughly $85B in August per a secondary analysis). Dodge commercial and industrial starts were +47.7% YTD through August 2026. AIA's July 2026 consensus has total nonresidential building at −0.3% in 2026 but data centers at +33%. Growth geography for MEP estimators is therefore the data-center corridor. For residential and finish trades it is the Texas Triangle plus the Southeast. California is a *cost-and-rebuild* market, not a *volume-growth* market.

### Cited Findings

**State permits (Census BPS; release year noted)**

| State | 2025 total units | 2025 single-family (SF) | SF Δ 2025 vs 2024 | 2026 YTD SF | SF share 2025 |
|---|---|---|---|---|---|
| Texas | 210,217 [U] | **140,002** [M] | **−11.7%** | **98,378 through Aug 2026, −3.4%** (Jan 2026 alone was −21.3%) | 66.9% [U] |
| Florida | 178,297 [U] | — | −10.3% | −5.0% through June 2026 (Jan −14.9%) | 62.4% [U] |
| California | 103,856 [U] | — | — | — | — |
| North Carolina | 86,167 [U] | 65,303 [U] | −6.9% | — | 75.8% [U] |
| Georgia | 61,196 [U] | — | — | — | — |
| Nevada | — | — | — | **−26.3% through Aug 2026 (steepest decline)** | — |
| **US** | ~1.43M [U] | **909,280** (NAHB) vs 911,900 (BusinesStats) | down | **620,558 through Aug 2026, −2.6%** | — |

Sources: [NAHB Eye on Housing, Mar 2026 "Single-family permits end 2025 on a soft note"](https://eyeonhousing.org/2026/03/single-family-permits-end-2025-on-a-soft-note/); [NAHB state/metro permit page](https://www.nahb.org/news-and-economics/housing-economics/state-and-local-data/building-permits-by-state-and-metro-area); [Buildermuse](https://buildermuse.com/residential/top-10-states-for-residential-construction-in/); [StatsPanda](https://statspanda.com/building-permits-per-capita-by-state); [BusinesStats](https://businesstats.com/us-building-permits-statistics/); [Residential Design (Aug 2026 YTD)](https://residentialdesignmagazine.com/single-family-permitting-august-2026); [Eye on Housing, Aug 2026 (through June)](https://eyeonhousing.org/2026/08/single-family-permitting-declines-through-june-as-multifamily-activity-remains-stronger/); [Eye on Housing, Apr 2026 (January)](https://eyeonhousing.org/2026/04/single-family-permits-decline-sharply-to-start-2026/).

**Metro permits (periods differ; compare only within a row group)**

| Metro | SF permits, 2025 YTD (GlobeSt Jan 2026; cutoff month not stated, likely Nov) | SF 12-mo to ~mid-2025 (GlobeSt Sept 2025) | 5+ unit permits 2025 (ACREN, Census-based) | Other |
|---|---|---|---|---|
| Houston | **40,471 (−11%)** | ~30,000 | 16,385 | **31,416 SF through Aug 2026, #1 metro**; >65,000 total units 2025 |
| Dallas–Fort Worth | **34,778 (−14%)** | ~26,000 | **24,607** | >65,000 total units 2025; MF permits down ~1,850 YoY (July 2026) |
| Phoenix | 20,318 (**−23%**) | 15,713 | 14,800 | 39,145 total / 24,002 SF in 2025, −15% (AZ Big Media); MF #6 nationally with 5,850 through May 2026 (RealPage) |
| Atlanta | 19,610 (−12%) | 13,731 | 11,052 | annual MF permitting −8% (RealPage, May 2026) |
| Charlotte | 14,211 (−13%) | 10,879 | — | — |
| Austin | — | 9,839 | — | — |

Sources: [GlobeSt, Jan 2026](https://www.globest.com/amp/2026/01/27/single-family-permits-decline-as-builders-adjust-to-market-challenges/); [GlobeSt, Sept 2025](https://www.globest.com/amp/2025/09/17/mixed-signals-for-housing-permits-as-metro-rankings-shift-again/); [ACREN](https://acren.ai/resources/multifamily-building-permits-by-metro); [AZ Big Media](https://azbigmedia.com/real-estate/metro-phoenix-ranks-no-4-in-the-nation-for-new-home-construction/); [Orion](https://www.orionprop.com/topfive/metro-phoenix-ranks-no-4-in-the-nation-for-new-home-construction/); [RealPage Metro Permits July 2026](https://www.realpage.com/analytics/metro-permits-july-2026/); [Residential Design](https://residentialdesignmagazine.com/single-family-permitting-august-2026). Conflict: [Spacial AI](https://spacial.io/blueprint/metros) labels Houston 25,721 / Dallas 22,599 / Phoenix 13,935 / Atlanta 11,833 as "through June 2025 YTD". GlobeSt (Aug 2025) gives the same Phoenix and Atlanta figures as "year ended June 2025". The period definition is uncertain. NAHB (Sept 2025) reports single-family construction **down in large metros and up in rural areas** ([NAHB press release](https://www.nahb.org/news-and-economics/press-releases/2025/09/single-family-construction-down-in-large-metros-up-in-rural-areas)).

**Nonresidential and megaproject signals (national unless noted)**

| Signal | Figure | Date / release | Source |
|---|---|---|---|
| Census data-center construction spending | **$50.7B SAAR**, first time above general office | April 2026 (reported June 2026) | [Bloomberg, June 1, 2026](https://www.bloomberg.com/news/articles/2026-06-01/us-construction-spending-on-data-centers-eclipses-50-billion) |
| Same, later readings | $84.95B SAAR, +73% YoY (Aug 2026); "$96.5B" (Sept 2026, preliminary, one tracker) | Aug–Sept 2026 | [mlq.ai](https://mlq.ai/news/us-census-data-center-construction-hits-507b-annualized-rate-surpassing-office-spending/), [neoteo](https://www.neoteo.com/en/us-data-center-construction-hit-a-reported-record-annual-pace-in-august) [U]; the jump from April is large, so check the Census C30 release |
| Dodge total starts | −1.5% to **$1.33T SAAR** (Sept 2026); nonresidential building +23.7% YTD; commercial starts −18.4% in September as hotel, office and data-center groundbreakings paused | Sept 2026 | [inside.lighting](https://inside.lighting/news/26-10/construction-starts-cool-growth-persists); [buildwcg](https://www.buildwcg.com/blog-posts/dodge-september-2026-construction-starts-fall-1-5-percent-commercial-2026) |
| Dodge YTD through August | total starts **+15.2%**; commercial and industrial **+47.7%** (data centers) | Aug 2026 | [Construction Dive / Dodge coverage](https://www.constructiondive.com/news/surge-july-construction-starts-megaproject-volatility-dodge/828521/); [inside.lighting](https://inside.lighting/news/26-09/construction-starts-retreat-recent-peak) |
| Named megaprojects | $12.8B "Project Jupiter" data center, **New Mexico** (July 2026); $3.5B Amazon data center, **Louisiana** (Aug 2026) | 2026 | [Dodge via ECM / electricalmarketing](https://www.ecmweb.com/construction/article/55372566/data-centers-continue-to-dominate-construction-pipeline) [U: exact page not mapped] |
| AIA Consensus Forecast (July 2026) | Nonresidential building **−0.3% (2026), +3.0% (2027)**; data centers **+33.0% (2026), +24.7% (2027)** (about 8% of nonresidential by 2027); manufacturing **−11.6% (2026)**, −0.6% (2027); health care +2.6%/+4.4%; panel spread for 2026: Dodge −1.3%, ConstructConnect +4.7% | July 2026 | [AIA July 2026 CCF](https://www.aia.org/resource-center/july-2026-consensus-construction-forecast) |
| ABC Backlog Indicator | **8.8 months** (June 2026); 8.4 (Oct 2025) | 2026 | [ABC](https://www.abc.org/News-Media/News-Releases/abcs-construction-backlog-indicator-inched-higher-in-june-contractors-remain-confident) |
| AGC/Sage 2026 outlook (951 firms, 49 states + DC, fielded Nov–Dec 2025) | Expectations dampened **except data centers and power**; ~70% hit by tariffs; 61% use or plan more AI (estimating among the top uses) | Jan 8, 2026 | [AGC](https://www.agc.org/index%2Ephp/news/2026/01/08/contractors-have-dampened-expectations-2026-apart-data-centers-and-power-projects-amid-worries-about); [Sage](https://www.sage.com/en-us/blog/2026-construction-industry-outlook/) |
| Remodeling (ICP5) | Home improvement and repair $404B (2019) → $611B (2022), expected >$600B through 2025 | JCHS 2025 | [Harvard JCHS Improving America's Housing 2025](https://www.jchs.harvard.edu/sites/default/files/reports/files/Harvard_JCHS_Improving_Americas_Housing_2025.pdf) |
| LA rebuild (ICP7) | 6,612 applications / **3,106 rebuild permits issued** (city + county, late Jan 2026); Palisades and Altadena generated **20,069 building permits** in the year after the fires (data through Feb 2026 / Dec 2025) | 2026 | [CA Governor, Feb 6, 2026](https://www.gov.ca.gov/2026/02/06/governor-newsom-announces-funding-for-la-fire-survivors-to-access-pre-built-housing-to-further-speed-recovery-and-maintain-neighborhood-character/); [Shovels](https://www.shovels.ai/blog/la-wildfire-rebuild-permit-data/) |
| Opportunity Zones 2.0 (ICP6) | New OZ map effective **Jan 1, 2027**; governor nominations July–Sept 2026 (extension to Oct 28, 2026) | 2026 | [EIG](https://eig.org/opportunity-zones-2-0-where-things-stand/); [HUD OZ overview via Hawaii](https://invest.hawaii.gov/wp-content/uploads/2026/06/HUD_OZ-Overview.pdf) |

### Inferences
- **Growth ranking for estimating demand** [J]:
  - (1) Data-center MEP work in the corridor metros. This is the only nonresidential segment with double-digit forecast growth. MEP is the estimate-heavy trade.
  - (2) Texas Triangle and Southeast single-family. Volume is still largest, but it is declining. Fewer starts means more bids per win, which raises estimating load per job won. That is a pain-side argument, not a demand-side one, and needs interview validation.
  - (3) Multifamily, which is recovering in places (national multifamily starts +12.7% over 12 months to May 2026 per Dodge, via sibling search) while DFW, Houston, Phoenix and Atlanta permits slowed in 2026.
  - (4) LA rebuild: permits run far ahead of completions.
- **Manufacturing megaprojects are a falling signal.** AIA expects manufacturing spending −11.6% in 2026. Semiconductor and battery regions (Phoenix, Columbus, Syracuse) should be weighted on *data-center* and *in-progress fab* work, not new manufacturing starts.
- **Census VIP has no state detail for private construction** [J, recall]. State or metro nonresidential growth must come from Dodge/ConstructConnect metro lists (paid or press releases) or from permit valuation in BPS.

### Gaps
- No 2026 Dodge or ConstructConnect **metro or state** starts ranking was found. The latest Dodge top-metro list found is 2022: New York $37.1B, Dallas $16.7B ([Construction Dive 2022 top 10 metros](https://www.constructiondive.com/news/2022-top-10-metros-construction-starts/641780)).
- **Dated megaproject figures for Northern Virginia, Phoenix (TSMC), DFW, Columbus/New Albany (Intel, data centers), Atlanta, Austin/Taylor (Samsung), Reno (Tahoe Reno Industrial Center) and Syracuse/Clay (Micron) were not retrieved.** Recall to verify [U]:
  - TSMC's total Arizona commitment was raised to about $165B in March 2025.
  - Intel pushed the first Ohio fab to around 2030–31 (announced Feb 2025).
  - Micron's Clay, NY complex is "up to $100B".
  - Northern Virginia is the largest US data-center market.
  - Do not publish any of these without sources.
- BPS **metro** 2025 annual and 2026 YTD files and **state 5+ unit** counts not opened (census.gov blocked).
- No state-level LA/Helene/Lahaina rebuild permit totals beyond LA.

---

## 4. Layer 3: Where is the pain most acute (estimator scarcity, labor and construction costs)?

### Takeaway
Pain concentrates in **high-cost coastal metros**: the Bay Area, LA, NYC, Boston and Seattle. There each estimator hour and each cost error is worth the most. Evidence:
- Bay Area hard costs ran **+$81/sq ft** and LA **+$35/sq ft** versus the rest of California (Terner, 2020).
- California's production cost per rentable sq ft is **2.3× Texas** (RAND, 2025).
- Seattle cost estimators earn $99,570 mean with LQ 1.44 (May 2025); Massachusetts tops state pay at about $100,840.

Pain is also **rising fastest in Sun Belt growth metros**: RLB puts Phoenix escalation at 5.30% a year, and **42% of Southern contractors** report immigration-enforcement impacts (AGC/NCCER 2026). Nationally, ABC says the industry must attract **349,000 workers in 2026** and 456,000 in 2027.

### Cited Findings

**Cost estimators (SOC 13-1051), BLS OEWS**

| Geography | Employment | LQ | Mean annual wage | Release | Source |
|---|---|---|---|---|---|
| US | 225,310 (May 2022); median $77,070 (May 2024) | 1.00 | $76,740 mean (May 2022) | May 2022 / May 2024 | [BLS OEWS May 2022](https://www.bls.gov/oes/2022/may/oes131051.htm); [BLS OOH](https://www.bls.gov/ooh/business-and-financial/cost-estimators.htm) (via sibling searches) |
| US median, May 2025 | $78,740 (third-party sites citing BLS) | — | — | May 2025 | [U] via sibling ICP1 search ([wagedex](https://wagedex.com/jobs/cost-estimators)) |
| Specialty trade contractors (industry) | median $79,130 | — | — | May 2024 | [BLS OOH](https://www.bls.gov/ooh/business-and-financial/cost-estimators.htm) |
| California | 25,850 | — | — | May 2023 | [BLS May 2023](https://www.bls.gov/oes/2023/may/oes131051.htm) |
| Texas | 20,240 | — | — | May 2023 | same |
| Florida | 14,150 | — | — | May 2023 | same |
| New York | 9,680 | — | — | May 2023 | same |
| Pennsylvania | 9,620 (appears in the high-concentration/LQ table) | >1 (value not surfaced) | — | May 2023 | same; sibling summary |
| Massachusetts | 4,960 (May 2022) | — | **$100,100 (May 2022)**; $100,840 top-paying state (Nue Career, year unclear) | — | [BLS May 2022](https://www.bls.gov/oes/2022/may/oes131051.htm); [Nue Career](https://nuecareer.com/careers/cost-estimator/salary-by-state) [U] |
| **Seattle–Tacoma–Bellevue MSA** | **4,340** | **1.44** | **$99,570** ($47.87/h) | **May 2025** | [BLS West regional release](https://www.bls.gov/regions/west/news-release/occupationalemploymentandwages_seattle.htm) |
| **Washington–Arlington–Alexandria MSA** | **3,780** | **0.84** | **$95,620** ($45.97/h) | **May 2025** | [BLS Mid-Atlantic release](https://www.bls.gov/regions/mid-atlantic/news-release/occupationalemploymentandwages_washingtondc.htm) |

**Labor scarcity and cost indices**

| Indicator | Figure | Date | Source |
|---|---|---|---|
| ABC workforce gap | **349,000** net new workers needed in **2026**; **456,000 in 2027**; up to 499,000 in 2026 if spending picks up; each extra $1B of spending ≈ 3,450 jobs; most 2026 demand is retirements | Jan 2026 | [EC&M / ABC](https://ecmweb.com/construction/news/55344103/construction-industry-must-attract-349000-workers-in-2026); [Yahoo Finance](https://finance.yahoo.com/news/construction-labor-demand-gap-forecast-082400425.html); 2025 figure was 439,000 ([Bisnow](https://www.bisnow.com/national/news/construction-development/report-construction-industry-needs-to-attract-439000-new-workers-this-year-127708)) |
| Immigration-enforcement impact by region (AGC/NCCER 2026 Workforce Survey, fielded July–Aug 2026) | US 29% of firms (28% in 2025); **South 42%, Northeast 37%, West 22%, Midwest 17%**; 16% say subs lost workers; 6% had jobsite visits | Sept 3, 2026 | [AGC](https://www.agc.org/news/2026/09/03/construction-workforce-shortages-remain-acute-despite-soft-market-conditions-data-centers-strain); [Roofing Contractor](https://www.roofingcontractor.com/articles/102656-immigration-enforcement-affects-29-of-contractors-agc-nccer-survey-finds) |
| RLB national cost index | **292.28** (July 2026); +1.28% QoQ; **+4.45% YoY**; described as a "two-speed market" | Q3 2026 | [RLB Q3 2026 QCR](https://www.rlb.com/wp-content/uploads/sites/4/2026/09/Q3-2026-QCR.pdf); [GlobeNewswire](https://www.globenewswire.com/news-release/2026/09/29/3371048/0/en/rider-levett-bucknall-rlb-q3-2026-construction-cost-report-reveals-dynamic-two-speed-market.html) |
| RLB city escalation (YoY to April 2026) | **Phoenix +5.30%**, Denver +4.59%, Los Angeles +4.15% (index values 30,480 LA and 21,205 Denver per search summary; units unclear, do not treat as $/sq ft) | Q2 2026 | [RLB Q2 2026 QCR](https://www.rlb.com/wp-content/uploads/sites/4/2026/06/Q2-2026-QCR_7.7.2026.pdf); [RLB Q2 summary](https://www.rlb.com/americas/insight/rlb-construction-cost-report-north-america-q2-2026/) |
| California multifamily hard costs (240 projects, 2009–2018) | **Bay Area +$81/sq ft, LA region +$35/sq ft** vs rest of CA; prevailing-wage projects **+$30/sq ft**; hard costs >60% of total development cost; +25% per sq ft over the decade | Terner Center, March 2020 | [Terner Center Hard Construction Costs 2020](https://ternercenter.berkeley.edu/wp-content/uploads/2020/08/Hard_Construction_Costs_March_2020.pdf) |
| California vs Texas | CA production cost per rentable sq ft **2.3×** Texas | RAND, April 2025 | via sibling ICP6 search summary (RAND page not mapped) [U] |
| LA fire rebuild $/sq ft (contractor marketing pages; no government dataset) | Altadena $350–$400 (standard), $450–$550 standard / $550–$675 upgraded / $675–$850 custom (TESH Group analysis), $450–$750 incl. A&E and permits; **Palisades $550–$900 and $650–$1,200**; older policies assumed **$200–$250/sq ft** | 2026 | [DWD Builders](https://www.dwdbuilders.com/intel/altadena-wildfire-rebuild-contractor-guide-2026); [Alto Builds](https://altobuilds.com/palisades-fire-rebuild); [UBIC](https://ubic.co/blog/cost-to-rebuild-a-home-in-altadena-after-the-eaton-fire); [Amerbuild](https://www.amerbuild.com/fire-rebuild/) [U: interested sources] |
| Perplexity answer to "cost to rebuild a house after the LA fires per sq ft 2026" | $400–$800+/sq ft from Bloomberg and local GCs; **Quotr absent** | test 2026-09-25 | [Quotr repo: verification_quotr_and_competitors.md](<../Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>) |
| California ADU (builder pages) | about $300–$500+/sq ft; detached ADUs often $225,000–$400,000+ | 2026 | [Quotr repo: buyer-questions-by-trade.md](<../../geo-brain/04-prompt-library/buyer-questions-by-trade.md>) [U: builder-interested] |
| Bay Area finish-materials price gap (Quotr procurement cards) | Saratoga $97,000 vs $187K–$218K Bay Area market; Monte Sereno $108,290 vs $195K–$245K; Hillsborough $30,437 vs $58K–$76K | quotr.ai, 2026 | [Quotr repo: quotr_onsite_content_audit.md](<../Quotr GEO AEO strategy audit/quotr_onsite_content_audit.md>) ("Quotr reports") |

### Inferences
- **Two kinds of pain, two geographies** [J]:
  - **Value-per-hour pain** is highest in CA, NY, MA, WA and DC. Wages near $95–100k, and $/sq ft gaps of $35–$81 over the state average and multiples over Texas, make every estimate and every finish-cost error expensive. Quotr's Service ($0.25/sq ft) and Procurement have the largest dollar ROI here.
  - **Capacity pain** (too few estimators and crews for the bid volume) is most likely in the Sun Belt growth and data-center metros: the South's 42% immigration-enforcement impact, Phoenix's top RLB escalation, and data-center MEP backlogs. Software seats replacing estimator hours fit here.
- **How to read LQ.** LQ above 1 (Seattle 1.44) means *more* estimators per job. That marks a larger buyer pool (ICP2 concentration), not scarcity. LQ below 1 in a booming market (DC/NoVA 0.84 alongside data-center growth) is the better scarcity flag. The scarcity variable should be **estimators per $1M of permit value or starts**, inverted, plus wage level, not LQ alone.
- **The Terner and RAND gaps justify separate CA and TX cost content.** Cost per sq ft differs by multiples, not percentages. That is the strongest legitimate reason for geo cost pages.

### Gaps
- Full OEWS May 2024/May 2025 state and metro tables for 13-1051 (employment, LQ, mean wage) not obtained (bls.gov blocked). Pull `oesm25st` and `oesm25ma`.
- Construction trade wages by state (QCEW NAICS 23 average weekly wage, 2025) not obtained.
- No Turner, Cumming or JLL city $/sq ft tables obtained. RLB city $/sq ft ranges by building type exist in the Q3 2026 PDF but were not read.
- RAND 2025 primary page not identified.
- No estimator vacancy/postings data (Indeed/Lightcast) by metro.

---

## 5. Layer 4: Which regulation and supply differences genuinely justify geo pages?

### Takeaway
Verified differences that change what an estimate contains:
- **California:** Zone 0 ember-resistant rules adopted Aug 19, 2026; LA rebuild permitting that differs between the City of LA and LA County; prevailing wage adds about +$30/sq ft; more than 100,000 ADUs permitted since 2017.
- **Texas:** SB 840 and SB 15 took effect Sept 1, 2025 (by-right residential in commercial zones; small lots in large cities).
- **National tariff changes** (Section 232 cabinets/vanities 25% through Dec 31, 2026, scheduled to rise to 50% on Jan 1, 2027) change procurement math everywhere. That justifies a *procurement* page, not a *geo* page.

Other commonly cited differences could not be verified this session (Florida Live Local and DBPR, WA/OR middle housing, NYC LL97, Title 24 2025, CSLB thresholds, Helene and Lahaina rebuild status, port statistics). Treat them as "likely, verify before publishing".

### Cited Findings

| Geography | Difference | Status / date | Why it changes an estimate | Source |
|---|---|---|---|---|
| CA (statewide; local roll-outs vary) | **Zone 0** (0–5 ft ember-resistant zone) emergency regulations adopted by the Board of Forestry **Aug 19, 2026**; sent to OAL **Aug 28, 2026** (OAL approval not confirmed); San Diego applied it to **new structures from Feb 28, 2026** (existing from Feb 28, 2027); Oakland existing homes 2029; Pasadena: new properties comply immediately, existing within 3 years | 2026 | Rebuild and new-build scopes in fire zones add hardscape, materials and vents | [BB&K](https://bbklaw.com/resources/la090926-california-board-of-forestry-adopts-emergency-zone-0-regulations-under-ab-3074); [KRCR](https://krcrtv.com/news/local/california-approves-zone-0-rules-what-homeowners-need-to-know); [San Diego](https://www.sandiego.gov/sites/default/files/2026-04/zone-0-guidelines-for-existing-structures.pdf); [Oakland](https://www.oaklandca.gov/Public-Safety-Streets/Fire/Wildfire-District-Inspections/Zone-0); [Pasadena agenda](https://ww2.cityofpasadena.net/2026%20Agendas/Apr_13_26/AR%2013.pdf) |
| LA rebuild zone | **Structures destroyed:** Palisades 6,837 (5,419 homes) + 1,017 damaged; Eaton 9,418 (6,011 homes) + 1,073 damaged (CBS: 9,413/1,074). Total >18,000 destroyed or damaged | CAL FIRE figures as reported in 2025 | Defines the addressable rebuild pool (~11,400 homes destroyed) | [NBC LA](https://nbclosangeles.com/news/california-wildfires/map-damage-assessment-eaton-palisades-fire/3620536/); [TODAY](https://www.today.com/today/amp/rcna190281); [CBS LA](https://www.cbsnews.com/amp/losangeles/news/palisades-and-eaton-fires-now-among-most-destructive-wildfires-recorded-in-california-history) |
| LA rebuild: permits vs completions | **Eaton (county):** 3,671 permits / 2,310 under construction / **215 completed** (Sept 26, 2026, citing county data [U]). **Palisades:** 1,196 permits / 1,006 under construction / **30 COs** (Aug 5, 2026); LADBS 1,419 permitted / 28 COs (July 7, 2026); 1,557 of 3,984 destroyed Palisades homes filed, **48 finished** (Oct 2026) | 2026 | Most owners are still pre-construction or mid-build, so estimate, re-bid and insurance-gap jobs remain live | [Lytemods](https://lytemods.com/fire-rebuild/altadena); [Palisades Fire Rebuilding status](https://palisadesfirerebuilding.com/rebuild-status); [Alto Builds](https://altobuilds.com/palisades-fire-rebuild); [Therenology](https://www.therenology.com/journal/palisades-altadena-fire-rebuild-insurance-contractors) |
| LA rebuild: process split | Altadena is unincorporated (**LA County** recovery program and Building & Safety); Palisades is in the **City of LA** (LADBS). Median permit times rose: Palisades **97→134 days**, Altadena **95→199 days** (early-2025 vs Jan–Mar 2026 filings); county filings before April 2026 median **162 days** (data updated mid-Oct 2026). County treats like-for-like rebuilds as expedited plan check | Oct 2026 | Two jurisdictions with different timelines, so one page needs two process tables | [Shovels](https://www.shovels.ai/blog/la-wildfire-rebuild-permit-data/); [Letter Four](https://www.letterfour.com/blog/one-year-after-the-fires-building-differently-in-altadena-and-palisades); [LA County Rebuild FAQ](https://recovery.lacounty.gov/wp-content/uploads/2025/02/Fire-Rebuild-FAQ.pdf) |
| CA prevailing wage | Prevailing-wage multifamily projects cost **+$30/sq ft** on average (2009–2018 sample) | Terner 2020 | Public and subsidized jobs need different labor rates | [Terner Center](https://ternercenter.berkeley.edu/wp-content/uploads/2020/08/Hard_Construction_Costs_March_2020.pdf) |
| CA ADUs | **>100,000 ADUs permitted since 2017** (HCD APR dashboard, per secondary source) | 2025–26 | ADU volume plus state ADU law is a distinct CA estimating segment | [Casita Coalition](https://casitacoalition.squarespace.com/casita-coalition-blog/california-reaches-major-housing-milestonemore-than-100000-adus-permitted-since-2017) [U] |
| TX | **SB 840**: multifamily or mixed-use (≥65% residential) by right in office, commercial, retail, warehouse and mixed-use zones; limits added parking, traffic-study and utility requirements for conversions. **SB 15**: small-lot single-family in cities >150,000 in counties >300,000 (lot minimum 3,000–4,000 sq ft by source). Both effective **Sept 1, 2025** | 2025 | New product types (conversions, small-lot homes) need fresh cost models in DFW, Houston, Austin and San Antonio | [Foley](https://www.foley.com/insights/publications/2025/07/texas-enacts-critical-real-estate-reforms-senate-bills-15-17-840/); [Texas Senate analysis SB 15](https://capitol.texas.gov/tlodocs/89R/analysis/html/SB00015I.htm); [Fort Worth](https://www.fortworthtexas.gov/files/assets/public/v/1/89th-legislative-updates-to-zoning-ordinance-and-impact-fee-program.pdf); [Austin](https://services.austintexas.gov/edims/document.cfm?id=462645) |
| National, procurement | **Section 232**: wood kitchen cabinets and vanities **25% through Dec 31, 2026**; rise to 50% deferred to **Jan 1, 2027** (Dec 31, 2025 proclamation; the 2027 date rests on trade sources) | 2026 | Landed-cost math changes on Jan 1, 2027 everywhere, so the page is national, not geo | [Green Worldwide](https://www.greenworldwide.com/section-232-wood-products-tariffs-remain-unchanged-through-2026/); [Allyn Intl](https://www.allynintl.com/en/news-publications/entry/update-section-232-tariffs-on-kitchen-cabinets-vanities-and-furniture) |
| National, developer geography | **Opportunity Zones 2.0**: new tract map effective **Jan 1, 2027** | 2026 | Tract-level geography for ICP6 (a list page is defensible once Treasury publishes) | [EIG](https://eig.org/opportunity-zones-2-0-where-things-stand/) |
| Quotr footprint | Procurement cards are all Bay Area (Saratoga, Monte Sereno: San Jose MSA 41940; Hillsborough: SF MSA 41860); Quotr sells an LA fire-rebuild estimate sample and launched FireTips (Feb 2025); copy conflicts on whether procurement delivers outside California; indexed copy says delivery "typically within about 90 days" | 2026 | Quotr can only *prove* CA geography today | [Quotr repo: website-audit.md](<../../geo-brain/02-current-state/website-audit.md>); [prompt-library.md (D-044, L-118)](<../../geo-brain/04-prompt-library/prompt-library.md>); [firetips.quotr.io](https://firetips.quotr.io/) |

### Inferences
**Geo-page legitimacy test** [J]: a geo page is justified only if at least two of these hold:
- (a) rules differ (licensing, code, wage, zoning, disaster);
- (b) prices differ materially ($/sq ft, labor rate, delivery or lead time);
- (c) Quotr has *local first-party data* (estimates, project cards, quotes).

Applied:
- **California passes all three.** Bay Area: (b)+(c). LA: (a)+(b)+(c).
- **Texas passes (a)+(b)**, with weak (c). Prioritize collecting Texas estimates.
- **Florida passes (a)+(b) on recall only.** Verify first.
- **Data-center corridor metros pass (b) only** (labor and escalation). They justify one corridor page, not six metro pages.
- **Procurement** geography is about delivery region and port, not tariffs (tariffs are national). One page with a West Coast / Gulf / Southeast / Northeast delivery table is legitimate. Per-city import pages are not.

### Gaps
Could not verify this session (all believed true from recall; **verify before any page cites them**):

| Item | What to verify |
|---|---|
| **CSLB** | License required above a job-value threshold (believed raised from $500 to $1,000 by AB 2622 from Jan 1, 2025) |
| **Texas licensing** | No statewide general-contractor license; TDLR licenses electricians and A/C contractors; TSBPE licenses plumbers |
| **Florida DBPR CILB** | Certified vs registered contractors |
| **Florida Live Local Act** | SB 102 (2023), amended in 2024 and 2025 |
| **California Title 24 Part 6 (2025 code)** | Applies to permit applications from Jan 1, 2026 |
| **CA SB 9 (2021) and SB 79 (2025)** | Transit-oriented upzoning |
| **WA HB 1110 (2023) and OR HB 2001 (2019)** | Middle housing |
| **NYC Local Law 97** | Emissions caps from 2024; tighter in 2030 |
| **State prevailing-wage laws** | Which states have them |
| **Disaster zones** | Hurricane Helene (western NC, Sept 2024) and Lahaina (Aug 2023) rebuild status |
| **Ports** | 2025 TEU for LA/Long Beach, Oakland, Savannah, Houston |

The ICP7 sibling's Helene and Lahaina searches also hit the search cap.

---

## 6. Layer 5: What demand-signal data exist (Google Trends, Keyword Planner) and what are their limits?

### Takeaway
Only DMA-level (Nielsen "metro") and state-level relative interest are available. Values are normalized 0–100 and low-volume terms are suppressed. B2B terms such as "construction takeoff software" will mostly be suppressed below state level. Keyword Planner gives volume ranges that degrade for small areas. Most AI prompts match no keyword at all. Layer 5 should carry **≤10% weight**, be used for consumer-side terms ("cost to build", "rebuild cost", "ADU cost"), and serve as a tie-breaker, not a driver.

### Cited Findings
- Google Trends publishes a normalized 0–100 index and suppresses low-volume terms. Keyword Planner warns that "targeting a small geographic area makes forecasts less accurate". The framework uses both at DMA level only. — [Google Trends Help 4365533](https://support.google.com/trends/answer/4365533); [Google Ads Help 3022575](https://support.google.com/google-ads/answer/3022575) (as cited in the uploaded framework, `3fb5eb52-ICP_depth_framework_for_GEO.md`)
- 65–85% of ChatGPT prompts match no keyword in a 27-billion-keyword database. — [Semrush](https://www.semrush.com/blog/chatgpt-search-insights/) (as cited in the framework)
- Memory can rewrite a search such as "restaurants near me I'd like" into "good vegan restaurants, San Francisco" before retrieval. Adding persona details to a prompt changes which brands are named. — [TechCrunch](https://techcrunch.com/2025/04/18/chatgpt-will-now-use-its-memory-to-personalize-web-searches); [Profound](https://www.tryprofound.com/blog/do-answer-engines-customize-responses-to-different-personas) (as cited in the framework)
- "No engine has been shown to add a user's city to a non-local prompt spontaneously." — framework honesty note (uploaded file)
- Quotr's tracked prompts already include geo-qualified ones: "best construction estimating services in California" (E-075, served by `/blog/construction-estimating-services-california/`); "how much does it cost to build an ADU in California 2026" (L-133); "…rebuild a house after the LA fires…" (L-134, Quotr absent); "how long does it take to ship building materials from China to California" (L-118). — [Quotr repo: prompt-library.md](<../../geo-brain/04-prompt-library/prompt-library.md>)

### Inferences
- **What Trends can show** [J]: state and DMA *relative* interest for consumer-cost terms ("cost to build a house", "ADU cost", "fire rebuild cost", "roof replacement cost"). These are useful for ICP5–7 and ICP9 page ordering. For B2B tool terms ("takeoff software", "estimating software"), expect "not enough data" in most DMAs. Use national Trends for seasonality only.
- **Method:** pull Trends by `geo=US`, resolution = state and metro (DMA). Allocate DMA values to CBSAs by population share through a DMA–county crosswalk; Nielsen's crosswalk is proprietary, so public approximations must be documented as an assumption. Pull Keyword Planner by state and DMA for 20–30 terms with an active Ads account; low-spend accounts see bucketed ranges.
- **Better demand signal for B2B:** count of *geo-qualified* prompts and community posts from the ICP interviews and Reddit/forum mining (for example "Houston", "Texas", "Bay Area" in r/estimators and r/Contractor threads). The Trends index is the weaker signal.

### Gaps
- No Trends or Keyword Planner pulls were run (no tool access, no search budget). No state or DMA values exist for any term.
- Whether Google Trends shows any metro-level data for "construction takeoff software" is untested.

---

## 7. Scoring index, top metros per ICP group, and named geo segments

### Takeaway
A **provisional** index is below. Components are tiered 0–3 from the cited evidence plus judgment, min–max normalized, and weighted per ICP group. It ranks:
- **LA, Houston, DFW, NYC, Phoenix, DC/NoVA** at the top for trade subs and GCs.
- **LA, SF–Oakland, NYC, San Jose** at the top for residential/developers.
- **LA, SF–Oakland, San Jose** far ahead for procurement.

Sanity checks applied the framework's rule that each component must move the ranking:
- Regulation and Quotr-fit did **not** move trade-sub or GC rankings (ρ 0.98–0.99, 0 top-10 swaps). They were removed from those groups' weights and turned into a **geo-page gate**.
- Size (A) still correlates 0.83 with the composite for subs, GCs and lenders. Replace A with a size/per-capita blend once CBP is pulled.

Seven named segments follow.

### Cited Findings
Inputs come from Sections 2–5. Every cited figure in the segment evidence rows below is sourced there; this section adds only the scoring arithmetic.

### Inferences

**Index components and weights** (the weights are the researcher's design, not a validated model)

| Component | Variable when fully pulled (source, release) | Provisional coding used here | Subs ICP1–3 | GCs ICP4 | Res/Dev/Rebuild ICP5–7 | Lenders ICP8 | Procurement ICP9 | Architects ICP10 |
|---|---|---|---|---|---|---|---|---|
| A. ICP concentration | CBP 2023 establishments for the group's NAICS; 0.5·size rank + 0.5·per-capita rank (size cap) | tier 0–3 from permit/estimator/establishment proxies | 0.25 | 0.25 | 0.20 | 0.25 | 0.15 | 0.35 |
| B. Demand growth | BPS 2025 + 2026 YTD units and Δ; Dodge metro starts; data-center/fab flag | tier from Section 3 | 0.35 | 0.40 | 0.25 | 0.35 | 0.15 | 0.20 |
| C. Pain / value per hour | OEWS 13-1051 estimators per $1M permit value (inverted) + mean wage; RLB/Terner $/sq ft and escalation; AGC regional labor impact | tier from Section 4 | 0.40 | 0.35 | 0.25 | 0.20 | 0.25 | 0.25 |
| D. Regulatory/supply distinctness | count of verified state/metro rule differences (Section 5) | tier | gate | gate | 0.15 | 0.10 | 0.10 | 0.20 |
| E. Quotr fit | Quotr first-party projects in metro; port proximity; delivery coverage | tier | gate | gate | 0.15 | 0.10 | 0.35 | 0 |
| F. Demand signal | Trends/KP DMA values allocated to CBSA | **not measured** (weight 0; add ≤0.10 when pulled) | 0 | 0 | 0 | 0 | 0 | 0 |

**Sanity-rule results** (drop-one test: Spearman ρ between full and drop-one ranks, and number of top-10 swaps)

| Group | Drop A | Drop B | Drop C | Drop D | Drop E | ρ(composite, A only) | Action |
|---|---|---|---|---|---|---|---|
| Subs | 0.94 / 1 | 0.85 / 3 | **0.68 / 3** | — (gate) | — (gate) | 0.83 | First run (D/E at 0.05) gave D/E ρ 0.99 / 0 swaps, so moved to gate |
| GCs | 0.97 / 0 | 0.77 / 4 | 0.72 / 4 | — | — | 0.84 | Same; A barely moves the ranking, so cap size when real data arrive |
| Res/Dev | 0.97 / 1 | 0.90 / 4 | 0.92 / 1 | 0.98 / 1 | 0.99 / 0 | 0.74 | D and E are nearly collinear with C (California is high on all three). Keep them, but re-test with measured data |
| Lenders | 0.96 / 0 | 0.81 / 4 | 0.92 / 2 | 0.97 / 1 | 0.99 / 1 | 0.83 | E is weak and lender-HQ data are missing; add an FDIC C&D-loan component |
| Procurement | 0.97 / 1 | 0.95 / 2 | 0.88 / 2 | 0.96 / 2 | 0.96 / 3 | 0.62 | Every component moves the ranking |
| Architects | 0.93 / 2 | 0.94 / 3 | 0.91 / 2 | 0.94 / 2 | — | 0.76 | Every component moves the ranking |

**Provisional metro index** (tiers 0–3: **[M]** where Sections 2–5 give a measured figure, otherwise **[J]**; composite 0–1 with rank)

| Metro (CBSA) | A | B | C | D | E | Subs | GCs | Res/Dev | Lenders | Procure | Arch |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Los Angeles (31080) | 3 | 1.5 | 3 | 3 | 2.5 | 0.74 (#1) | 0.70 (#3) | 0.79 (#1) | 0.72 (#2) | 0.83 (#1) | 0.85 (#1) |
| New York (35620) | 3 | 1.5 | 3 | 2.5 | 0.5 | 0.74 (#2) | 0.70 (#4) | 0.66 (#3) | 0.63 (#4) | 0.58 (#4) | 0.81 (#2) |
| Houston (26420) | 3 | 3 | 1.5 | 1.5 | 1 | 0.70 (#3) | 0.74 (#1) | 0.62 (#5) | 0.72 (#1) | 0.52 (#6) | 0.69 (#4) |
| Dallas–Fort Worth (19100) | 3 | 3 | 1.5 | 1.5 | 0.5 | 0.70 (#4) | 0.74 (#2) | 0.60 (#6) | 0.71 (#3) | 0.46 (#10) | 0.69 (#5) |
| Phoenix (38060) | 2.5 | 2.5 | 2 | 1 | 0.5 | 0.67 (#5) | 0.68 (#5) | 0.53 (#8) | 0.60 (#6) | 0.44 (#13) | 0.60 (#8) |
| Washington DC–NoVA (47900) | 2.5 | 2.5 | 2 | 1 | 0.5 | 0.67 (#6) | 0.68 (#6) | 0.53 (#9) | 0.60 (#7) | 0.44 (#14) | 0.60 (#9) |
| SF–Oakland (41860) | 2.5 | 1 | 3 | 3 | 3 | 0.60 (#7) | 0.55 (#8) | 0.71 (#2) | 0.60 (#5) | 0.82 (#2) | 0.74 (#3) |
| Atlanta (12060) | 2.5 | 2.5 | 1.5 | 1 | 1 | 0.57 (#8) | 0.59 (#7) | 0.49 (#11) | 0.57 (#8) | 0.43 (#15) | 0.54 (#14) |
| Boston (14460) | 2 | 1 | 3 | 1.5 | 0.5 | 0.56 (#9) | 0.51 (#11) | 0.46 (#15) | 0.42 (#19) | 0.44 (#12) | 0.55 (#13) |
| Seattle (42660) | 2 | 1.5 | 2.5 | 2 | 1 | 0.55 (#10) | 0.52 (#10) | 0.52 (#10) | 0.49 (#11) | 0.50 (#7) | 0.58 (#10) |
| Riverside–San Bernardino (40140) | 2 | 2 | 2 | 2.5 | 1.5 | 0.53 (#11) | 0.53 (#9) | 0.57 (#7) | 0.56 (#9) | 0.55 (#5) | 0.61 (#7) |
| San Jose (41940) | 1.5 | 1 | 3 | 3 | 3 | 0.51 (#12) | 0.46 (#12) | 0.64 (#4) | 0.51 (#10) | 0.77 (#3) | 0.61 (#6) |
| San Diego (41740) | 2 | 1 | 2.5 | 2.5 | 1 | 0.46 (#13) | 0.42 (#19) | 0.48 (#13) | 0.42 (#17) | 0.48 (#9) | 0.57 (#11) |
| Miami (33100) | 2 | 1.5 | 2 | 2.5 | 1 | 0.45 (#14) | 0.43 (#17) | 0.48 (#12) | 0.46 (#14) | 0.45 (#11) | 0.56 (#12) |
| Denver (19740) | 2 | 1.5 | 2 | 1 | 0.5 | 0.45 (#15) | 0.43 (#18) | 0.37 (#20) | 0.38 (#20) | 0.34 (#18) | 0.44 (#20) |
| Austin (12420) | 2 | 2 | 1.5 | 1.5 | 0.5 | 0.43 (#16) | 0.45 (#13) | 0.40 (#18) | 0.44 (#15) | 0.33 (#19) | 0.47 (#18) |
| Charlotte (16740) | 2 | 2 | 1.5 | 1 | 0.5 | 0.43 (#17) | 0.45 (#14) | 0.37 (#19) | 0.42 (#18) | 0.31 (#23) | 0.43 (#21) |
| Orlando (36740) | 2 | 2 | 1.5 | 2 | 0.5 | 0.43 (#18) | 0.45 (#15) | 0.43 (#16) | 0.46 (#12) | 0.35 (#16) | 0.51 (#15) |
| Tampa (45300) | 2 | 2 | 1.5 | 2 | 0.5 | 0.43 (#19) | 0.45 (#16) | 0.43 (#17) | 0.46 (#13) | 0.35 (#17) | 0.51 (#16) |
| Chicago (16980) | 2.5 | 1 | 2 | 1 | 0.5 | 0.40 (#20) | 0.38 (#24) | 0.34 (#22) | 0.34 (#25) | 0.33 (#20) | 0.45 (#19) |
| Sacramento (40900) | 1.5 | 1.5 | 2 | 2.5 | 1.5 | 0.40 (#21) | 0.39 (#23) | 0.47 (#14) | 0.43 (#16) | 0.49 (#8) | 0.49 (#17) |
| Raleigh (39580) | 1.5 | 2 | 1.5 | 1 | 0.5 | 0.39 (#22) | 0.40 (#20) | 0.33 (#23) | 0.38 (#22) | 0.28 (#25) | 0.36 (#24) |
| Nashville (34980) | 1.5 | 2 | 1.5 | 0.5 | 0.5 | 0.39 (#23) | 0.40 (#21) | 0.30 (#25) | 0.36 (#23) | 0.26 (#26) | 0.32 (#25) |
| Columbus (18140) | 1.5 | 2 | 1.5 | 0.5 | 0.5 | 0.39 (#24) | 0.40 (#22) | 0.30 (#26) | 0.36 (#24) | 0.26 (#27) | 0.32 (#26) |
| Portland (38900) | 1.5 | 1 | 2 | 2 | 0.5 | 0.31 (#25) | 0.29 (#27) | 0.33 (#24) | 0.29 (#26) | 0.31 (#22) | 0.40 (#22) |
| Salt Lake City (41620) | 1.5 | 1.5 | 1.5 | 0.5 | 0.5 | 0.30 (#26) | 0.30 (#26) | 0.24 (#28) | 0.27 (#27) | 0.23 (#28) | 0.27 (#29) |
| Kahului–Wailuku (27980) | 0.25 | 1 | 2.5 | 2 | 0.5 | 0.30 (#27) | 0.26 (#28) | 0.30 (#27) | 0.23 (#29) | 0.31 (#24) | 0.31 (#27) |
| Jacksonville (27260) | 1.5 | 2 | 1 | 2 | 1 | 0.29 (#28) | 0.31 (#25) | 0.36 (#21) | 0.38 (#21) | 0.32 (#21) | 0.38 (#23) |
| Las Vegas (29820) | 1.5 | 1 | 1.5 | 0.5 | 0.5 | 0.21 (#29) | 0.20 (#32) | 0.18 (#30) | 0.18 (#30) | 0.19 (#30) | 0.22 (#30) |
| Reno (39900) | 0.5 | 1.5 | 1.5 | 0.5 | 0.5 | 0.21 (#30) | 0.21 (#30) | 0.17 (#31) | 0.18 (#31) | 0.17 (#31) | 0.14 (#32) |
| Syracuse (45060) | 0.5 | 1.5 | 1.5 | 0.5 | 0 | 0.21 (#31) | 0.21 (#31) | 0.14 (#32) | 0.16 (#32) | 0.11 (#33) | 0.14 (#33) |
| San Antonio (41700) | 1.5 | 1.5 | 1 | 1.5 | 0.5 | 0.20 (#32) | 0.21 (#29) | 0.24 (#29) | 0.26 (#28) | 0.20 (#29) | 0.29 (#28) |
| Asheville (11700) | 0.5 | 1 | 1.5 | 1.5 | 0 | 0.12 (#33) | 0.11 (#33) | 0.14 (#33) | 0.11 (#33) | 0.12 (#32) | 0.17 (#31) |

Measured anchors behind the tiers:
- Houston and DFW B=3: largest SF and 5+ permits (Section 3).
- Phoenix B=2.5 and C=2: 14,800 5+ units; RLB +5.30%.
- DC–NoVA C=2: estimator LQ 0.84, $95,620.
- Seattle C=2.5: LQ 1.44, $99,570.
- SF/San Jose C=3: Terner +$81/sq ft. E=3: procurement cards.
- LA C=3 and D=3: rebuild $/sq ft, Zone 0, the two-jurisdiction permit split.
- Nevada (Las Vegas, Reno) B lowered: −26.3% SF YTD.

Everything else is [J].

**Top metros per ICP group** (provisional; re-run after the CBP/OEWS/BPS pull). One adjustment is applied: for ICP7, the index is overridden by the event geography.

| ICP group | Top 8–10 metros (in order) |
|---|---|
| ICP1–3 trade subs (MEP owner-estimators, mid-size chief estimators, finish trades) | LA, NYC, Houston, DFW, Phoenix, DC–NoVA, SF–Oakland, Atlanta, Boston, Seattle. **For finish trades (ICP3) specifically**, swap Boston and NYC for Charlotte and Tampa/Orlando. Basis: single-family volume and Hispanic-owned small firms [J] |
| ICP4 commercial GC precon | Houston, DFW, LA, NYC, Phoenix, DC–NoVA, Atlanta, SF–Oakland, Riverside–San Bernardino, Seattle |
| ICP5 residential builders/remodelers | LA, SF–Oakland, San Jose, Houston, DFW, Riverside–San Bernardino, Phoenix, Atlanta, Charlotte, Tampa. Charlotte and Tampa are promoted over NYC and DC on single-family permit evidence [J] |
| ICP6 small developers (infill, ADU, BTR) | SF–Oakland, San Jose, LA, Austin, DFW, Houston, Seattle, Portland, Miami, Phoenix. Basis: ADU, SB 840/SB 15, middle-housing and Live Local rules [partly U] |
| ICP7 disaster rebuild | **LA (Palisades + Altadena) only at scale**; Asheville/western NC and Maui are narrative or contrast sites (index ranks them #31–33) |
| ICP8 lenders, debt funds, cost reviewers | Houston, LA, DFW, NYC, SF–Oakland, Phoenix, DC–NoVA, Atlanta, Riverside–San Bernardino, San Jose (lender-HQ component missing; Charlotte likely under-ranked [J]) |
| ICP9 finish-materials importers (procurement) | LA, SF–Oakland, San Jose, NYC, Riverside–San Bernardino, Houston, Seattle, Sacramento, San Diego, DFW |
| ICP10 architects (design-stage costing) | LA, NYC, SF–Oakland, Houston, DFW, San Jose, Riverside–San Bernardino, Phoenix, DC–NoVA, Seattle |

**State first pass** (provisional tiers [J] anchored on the measured columns in Sections 2–4)

| Tier | States | Why |
|---|---|---|
| 1 | **California, Texas, Florida** | Largest estimator pools (May 2023: 25,850 / 20,240 / 14,150) and permit volumes (2025: 103,856 / 210,217 / 178,297 units); CA highest cost and most distinct rules; TX highest volume plus SB 840/SB 15 |
| 2 | Arizona, Georgia, North Carolina, Virginia (NoVA), Washington, New York | Growth plus data centers (AZ, GA, VA), single-family volume (NC 86,167 units, GA 61,196), high-cost and high-wage estimator markets (WA, NY) |
| 3 | Colorado, Tennessee, Ohio, South Carolina, Nevada, Utah, Oregon, Massachusetts, Illinois, New Jersey, Pennsylvania | Mid-size markets. MA has top estimator pay (~$100k). NV is shrinking (−26.3% SF YTD 2026). OH (Columbus) is a data-center and fab bet |

**Named geo segments** (Step 4 of the framework: one evidence row, one job-to-be-done and example prompt stems each)

| # | Segment (geo) | Primary ICPs | Evidence row (dated) | Job-to-be-done | Example prompt stems | Evidence strength |
|---|---|---|---|---|---|---|
| 1 | **Bay Area high-cost home, ADU and remodel market** (SF–Oakland 41860 + San Jose 41940) | ICP5, ICP6, ICP9, ICP10 | Terner 2020: hard costs **+$81/sq ft** vs rest of CA; CA >100,000 ADUs since 2017 [U]; Quotr cards: Saratoga **$97,000 vs $187K–$218K**, Monte Sereno $108,290 vs $195K–$245K, Hillsborough $30,437 vs $58K–$76K ("Quotr reports"); Quotr HQ/SkyDeck | "Know the real number before I commit to a client or lender, and cut finish costs that dominate a Bay Area budget" | "how much does it cost to build a detached ADU in San Jose 2026"; "are factory-direct cabinets from China cheaper than Bay Area dealers after tariffs"; "cost per square foot to remodel a kitchen in Palo Alto 2026"; "Title 24 2025 cost impact for a new home in the Bay Area" [U regulation] | Strong (Quotr has first-party data) |
| 2 | **LA rebuild zone** (Palisades in City of LA; Altadena in unincorporated LA County; CBSA 31080) | ICP7 (primary), ICP5, ICP9, ICP8 | 6,837 + 9,418 structures destroyed (~11,400 homes); Eaton 3,671 permits / **215 completed** (Sept 2026 [U]); Palisades 1,196 permits / **30 COs** (Aug 2026); median permit time Altadena **95→199 days**; rebuild quotes $350–$1,200/sq ft vs policies assuming $200–$250; Zone 0 adopted Aug 19, 2026; Quotr absent from the rebuild-cost answer (Sept 2026) | "Get a line-item rebuild estimate I can put in front of my insurer and compare against contractor bids, and decide rebuild vs sell" | "cost per square foot to rebuild in Altadena vs Pacific Palisades 2026"; "my insurance limit is $X for a 2,000 sq ft house, is it enough to rebuild in Altadena"; "how long does an LA County fire rebuild permit take 2026"; "does Zone 0 apply to my rebuild in Altadena" | Strong (but most figures come from interested contractor pages; label them) |
| 3 | **Texas Triangle volume market** (Houston 26420, DFW 19100, Austin 12420, San Antonio 41700) | ICP1, ICP3, ICP4, ICP5, ICP6, ICP8 | TX **210,217 units** and **140,002 SF permits in 2025** (−11.7%); 98,378 SF through Aug 2026 (−3.4%); Houston **40,471**, DFW **34,778** SF (2025 YTD); DFW **24,607** 5+ units (2025); SB 840/SB 15 effective Sept 1, 2025; South 42% immigration-enforcement impact (2026); CA cost per rentable sq ft 2.3× TX (RAND 2025 [U]) | "Bid more jobs per week with the estimators I have, at Texas-level margins" | "best takeoff software for electrical contractors in Houston"; "how many drywall bids can one estimator do a week Dallas"; "cost per square foot to convert an office to apartments in Dallas under SB 840"; "small lot home construction cost Austin 2026" | Medium (volume measured; Quotr has no TX proof yet) |
| 4 | **Data-center and fab MEP corridor** (Phoenix 38060, DFW, DC–NoVA 47900, Atlanta 12060, Columbus 18140, Reno 39900; Syracuse 45060 as fab outlier) | ICP2 (primary), ICP1, ICP4 | Census data-center spending **$50.7B SAAR (Apr 2026)**; Dodge commercial and industrial starts **+47.7% YTD (Aug 2026)**; AIA data centers **+33% (2026), +24.7% (2027)**; RLB Phoenix **+5.30%** YoY; DC–NoVA estimators **LQ 0.84, $95,620** (May 2025); ABC needs **349,000** workers in 2026 | "Turn 500-sheet MEP sets into a defensible bid faster than the GC's deadline without hiring another $95k estimator" | "AI takeoff for data center electrical one-lines and cable tray"; "how do mechanical subs estimate data center cooling faster"; "construction estimator salary Northern Virginia 2026 hire or outsource"; "Phoenix electrical estimator shortage data centers" | Medium for national growth; **metro split unmeasured** |
| 5 | **Florida storm, condo and Live Local market** (Miami 33100, Tampa 45300, Orlando 36740, Jacksonville 27260) | ICP3 (roofing/flooring), ICP5, ICP6, ICP9 | FL **178,297 units (2025)**; SF −10.3% (2025), −5.0% H1 2026; FL 14,150 estimators (May 2023); Live Local / DBPR / storm rules **[U]** | "Price storm, roof and condo repair work fast, and price affordable multifamily under Live Local" | "roof replacement cost per square foot Tampa 2026"; "Live Local Act apartment construction cost Miami"; "flooring estimate software for Florida contractors" | Weak to medium (regulatory evidence unverified) |
| 6 | **Carolinas and Southeast single-family growth belt** (Charlotte 16740, Raleigh 39580, Atlanta 12060, Nashville 34980; Asheville 11700 as Helene contrast) | ICP3, ICP5, ICP1 | NC **86,167 units, 65,303 SF** (2025, −6.9% SF); GA 61,196 units; Charlotte **14,211**, Atlanta **19,610** SF (2025 YTD); NAHB: SF construction down in large metros, up in rural areas (Sept 2025) | "Keep up with production-builder bid volume as a small finish or MEP sub" | "drywall takeoff software for subcontractors Charlotte"; "cost to build a house per square foot Raleigh 2026"; "how to estimate flooring for tract homes faster" | Medium |
| 7 | **Northeast and Pacific NW high-wage design and precon market** (NYC 35620, Boston 14460, Seattle 42660, Portland 38900) | ICP10, ICP4, ICP2, ICP6 | MA estimators ~$100k (top state); Seattle **4,340 estimators, LQ 1.44, $99,570** (May 2025); WA/OR middle housing and NYC LL97 **[U]** | "Give clients a credible design-stage number without a $100k estimator on staff" | "conceptual estimate cost per square foot NYC 2026"; "cost to build a fourplex in Seattle under middle housing 2026" [U]; "how do small architecture firms price schematic design estimates" | Weak to medium |

### Gaps
- The index is **ordinal and judgment-heavy**. Tiers must be replaced by min–max-normalized measured values (CBP 2023, BPS 2025/2026, OEWS May 2025, RLB/Cumming city $/sq ft, FDIC C&D loans by state) before any external use.
- Lender (ICP8) concentration needs FDIC Call Report construction and land-development loans by bank HQ state; not pulled.
- Segment 4's split among Phoenix, NoVA, DFW, Atlanta, Columbus and Reno is not measured. Data-center MW or $ by metro (CBRE/JLL/Dodge) was not retrieved.

---

## 8. Recommendation: hub-and-spoke geo content plan and switch-interview geographies

### Takeaway
Build **one national hub plus 7–9 geo spokes in year 1, not 40 metro pages**:
- 3 state spokes: CA, TX, FL.
- 3 metro or zone spokes: Bay Area, LA rebuild, Houston–DFW.
- 1 corridor page (data-center MEP).
- 1 procurement delivery-region page.
- Optional: Pacific NW/NYC later.

Each spoke must carry dated local data that Quotr or public sources uniquely supply. Recruit switch interviews mainly in the Bay Area, LA, Houston/DFW, Phoenix and NoVA, with Florida and the Carolinas as secondary sites.

### Cited Findings
- **Scaled content:** Google's spam policies prohibit "scaled content abuse" (many pages produced mainly to manipulate rankings with little value). City-swap pages are the textbook case. — [Google Search Central spam policies](https://developers.google.com/search/docs/essentials/spam-policies) (policy known; page not re-opened this session)
- **Quotr's current geo footprint** — [Quotr repo: website-audit.md](<../../geo-brain/02-current-state/website-audit.md>); [white-space.md](<../../geo-brain/03-market/white-space.md>)
  - Bay Area procurement cards.
  - LA rebuild estimate sample and FireTips.
  - A California estimating-services blog post.
  - No Texas, Florida or data-center content.
- **Small vendors do get cited on cost benchmarks.** Meltplan and Exayard cost pages are cited next to RSMeans for multifamily $/sq ft prompts. — [Quotr repo: competitor_geo_benchmark.md](<../Quotr GEO AEO strategy audit/competitor_geo_benchmark.md>)
- **Sample-size rule:** saturation within 9–17 interviews; 92% of codes after 12 (framework sources). — [PubMed](https://pubmed.ncbi.nlm.nih.gov/34785096/) (as cited in the framework)

### Inferences

**Hub-and-spoke plan** [J]

| # | Page | Type | Unique data it must carry (anti-thin requirements) | Refresh |
|---|---|---|---|---|
| H | **US construction cost and estimating capacity by region (2026)** | National hub | Table of the 7 segments: permits (BPS, dated), estimator wage and LQ (OEWS May 2025), RLB/Turner escalation, Quotr median $/sq ft by region from its own estimates (n stated), and links to spokes | Quarterly |
| S1 | **California construction costs and rules (2026)** | State spoke | Title 24 2025, CSLB, prevailing wage (+$30/sq ft Terner), ADU/SB 9/SB 79, Zone 0; CA vs TX cost gap (RAND 2.3×); Quotr CA estimate medians | Quarterly |
| S1a | **Bay Area ADU and home-build cost + factory-direct finish savings** | Metro spoke | Quotr's anonymized Bay Area estimates (n, date, range), the three procurement cards with method, ADU $/sq ft by type | Quarterly |
| S1b | **LA fire rebuild cost and permit guide (Palisades vs Altadena)** | Zone spoke | City vs County process tables, permits vs completions (dated), median permit days, $/sq ft by finish tier from Quotr rebuild estimates vs contractor-page ranges, insurance-gap worksheet, Zone 0 | Monthly while permits are active |
| S2 | **Texas construction estimating and costs (Houston, DFW, Austin)** | State spoke | No-state-GC-license explainer [verify], SB 840/SB 15 product types, TX permits by metro (dated), TX vs CA $/sq ft; **publish only once Quotr has ≥10–20 TX estimates** | Quarterly |
| S3 | **Florida construction estimating (storm, roof, condo, Live Local)** | State spoke | DBPR licensing, Live Local, storm/roof code [all verify first]; FL permits | Semiannual |
| C1 | **Data-center and fab MEP estimating corridor** | Corridor page (not per-metro) | National data-center spending (Census), Dodge/AIA growth, a metro table (Phoenix, NoVA, DFW, Atlanta, Columbus, Reno) with OEWS estimator wage/LQ and RLB escalation; MEP takeoff benchmarks from Quotr | Quarterly |
| P1 | **Factory-direct delivery by US region** (West Coast / Gulf / Southeast / Northeast) | Procurement spoke | Port of entry, transit and drayage days, landed-cost example per region, which regions Quotr actually delivers to (resolve the "outside California" conflict first), Section 232 timeline | Quarterly |
| Later | Pacific NW / NYC design-stage costing | Optional | Only with local Quotr projects | — |

**Do not build** [J]:
- "[Trade] estimating software in [City]" or "AI takeoff in [State]" matrices. The product is identical everywhere.
- Standalone Reno, Syracuse or Columbus megaproject pages.
- Lahaina or western NC rebuild pages without local partners or data.
- "Construction estimating services in [City]" doorway pages.

**Switch-interview recruiting geography** (12 per ICP; roughly 60–70% from the primary geos) [J]

| ICP | Primary recruit geos | Secondary | Why |
|---|---|---|---|
| ICP1 small MEP owner-estimators | Houston, DFW, Phoenix | LA, Atlanta | Volume plus Sun Belt capacity pain |
| ICP2 mid-size chief estimators | DC–NoVA, Phoenix, DFW | Atlanta, Columbus | Data-center MEP backlog |
| ICP3 finish-trade subs | Houston, DFW, Atlanta, Charlotte | Tampa/Orlando, Riverside | Single-family volume. Run **3–4 interviews in Spanish** (32.8% Hispanic workforce) |
| ICP4 GC precon managers | NYC, LA, DFW, Houston | Phoenix, Seattle | Commercial volume and high cost |
| ICP5 residential builders/remodelers | Bay Area, LA, Houston/DFW | Charlotte/Raleigh, Tampa | Cost pain (CA) vs volume (TX/SE) contrast |
| ICP6 small developers | Bay Area (ADU/SB 9), LA, Austin/DFW (SB 840/15) | Portland/Seattle, Miami | Each tests a different reform trigger |
| ICP7 rebuild | Altadena, Palisades (10 of 12) | Asheville, Maui (1 each, contrast) | Live permits and insurance-gap trigger |
| ICP8 lenders/cost reviewers | LA/SoCal private lenders, NYC debt funds | DFW, Phoenix | Where ground-up lending and rebuild budgets concentrate [J] |
| ICP9 importers | LA/Long Beach-adjacent (Inland Empire), Bay Area | Houston, NYC/NJ, Miami | Port-adjacent importers |
| ICP10 architects | Bay Area, LA, NYC | Seattle, Boston | High-cost design markets |

### Gaps
- The Texas and Florida spokes depend on Quotr data that may not exist (TO CONFIRM with Quotr: estimate counts by state).
- Quotr's delivery coverage outside California is unresolved.
- No Quotr customer-location data were available to check where current users are.

---

## 9. Honesty notes: measured vs proxy, engine geography behavior, and which geo pages would be thin

### Takeaway
Measured at state and metro level once pulled:
- establishment counts (CBP);
- permits (BPS);
- estimator employment and wages (OEWS).

Always proxies:
- "pain" (estimator scarcity, cost per sq ft from indices or contractor pages);
- regional nonresidential growth (Dodge press lists);
- demand signal (Trends/KP).

Engines are not shown to add geography to non-local prompts. Geo pages pay off only when the *prompt* carries the geography (rebuild, ADU, state rules) or when memory injects it.

### Cited Findings
- Framework honesty notes:
  - No engine has been shown to spontaneously add a user's city to a non-local prompt.
  - Geography pays off "through facts in the content and persona facts in the prompt".
  - True deserts are "too small for content scale".
  - Source: uploaded framework, `3fb5eb52-ICP_depth_framework_for_GEO.md` (Louisiana section).
- 91% of cited URLs appear in only one engine; identical prompts return the same brand list <1% of the time. Measure geo pages as distributions. — [Growth Memo](https://www.growth-memo.com/p/the-consensus-gap); [SEJ/SparkToro](https://www.searchenginejournal.com/ai-recommendations-change-with-nearly-every-query-sparktoro/566242) (as cited in the framework)
- **LA rebuild data:** no government or academic dataset tracks LA rebuild $/sq ft; contractor pages are "directional market signals". — sibling ICP7 search summary of [bwengr](https://bwengr.com/blog/2026/04/12/altadena-rebuild-costs/) / contractor pages [U]
- **Census CBP:** not recommended as a time series. — [Census CBP API page](https://www.census.gov/programs-surveys/cbp/data/api.html)

### Inferences

| Item | Status |
|---|---|
| Establishments by NAICS × state/metro (CBP 2023) | **Known/measurable**; not pulled this session |
| Permits by state/metro (BPS 2025, 2026 YTD) | **Known** for TX, FL, NC, GA, US and the top 5–6 metros (secondary summaries of Census/NAHB); the rest unpulled |
| Estimator employment, LQ, wage (OEWS) | **Known** for 5 states (May 2023) and 2 metros (May 2025); the rest unpulled |
| Estimator *scarcity* | **Proxy** (estimators per $ permits; wage; AGC regional survey). No vacancy data |
| Cost per sq ft by metro | **Proxy** (RLB escalation; Terner 2020 CA gaps; RAND CA/TX ratio; contractor pages for LA) |
| Data-center / megaproject growth by metro | **Likely** (national data measured; metro split unmeasured) |
| Regulation differences | **Known** for CA Zone 0, LA permitting and TX SB 840/15; **likely** for FL, WA/OR, NYC, CSLB, Title 24 |
| Demand signal by DMA | **Speculative** (not pulled; B2B terms likely suppressed) |
| Segment JTBDs and prompt stems | **Speculative** until the switch interviews run |

**Thin-page risk list** [J]:
- Any city page without Quotr first-party numbers.
- All six data-center metros as separate pages.
- Florida before its rules are verified and FL estimates exist.
- Texas before Quotr has TX estimates.
- Western NC and Maui rebuild pages.
- Trade × metro matrices.
- "Estimating services in [state]" pages beyond California.

### Gaps
- Not run: the engine test that would settle geography behavior. Run 10 rebuild/ADU/state-rule prompts with and without a city, three times each in ChatGPT and Perplexity, and log whether sub-queries add geography.
- Data-host access (`census.gov`, `bls.gov`, `ncarb.org`, `eyeonhousing.org`, `agc.org`) and more search budget are needed to replace the provisional index with measured values.
