# ICP 5 — Small residential builder, custom home builder, remodeler or small residential GC (1–20 employees, ~$1M–$20M revenue) who prices jobs from architect plans or own sketches

*Research date: 2026-11-06. US focus. Method: the uploaded ICP-depth GEO framework (coding chain trigger → stage → hot/cold mode → restraining force → prompt → proof; four forces; switch timeline; prompt matrix; geography-to-segment pipeline; measurement as distributions) applied to this buyer.*

*Evidence labels used throughout: **[WS]** = figure or wording taken from a WebSearch result extract on 2026-11-06; the page itself could not be opened because WebFetch/curl to nahb.org, eyeonhousing.org, capterra.com, reddit.com, jlconline.com and census.gov were blocked by this session's network policy (proxy 403 / host not resolvable), so every [WS] item should be re-read on the page before publication. **[Repo]** = from Quotr's existing research (geo-brain, research_notes/Quotr GEO AEO strategy audit, tested 2026-09-25). **[FW]** = from the uploaded ICP framework file. **SIMULATED / ESTIMATE** = researcher-built, not observed. The session's shared web-search budget ran out after ~20 searches, so several planned fan-out runs and all subreddit member counts are listed as gaps rather than guessed.*

---

## A. Definition and size

### Takeaway
This ICP is the median member of NAHB: a builder with ~6 payroll employees, ~5 starts and ~$3.7M revenue a year, or a remodeler with ~5 employees and ~$2.1M revenue — a business where the owner usually prices the job personally, works on 17–30% gross margins, and where the bottom quartile of builders loses money (−1.4% net). Roughly 60,000 single-family GC establishments (NAICS 236115) plus well over 100,000 remodeling firms (236118) sit in the universe, but the exact Census size-class split could not be pulled this session.

### Cited Findings
**Firm counts (US)**
- NAICS 236115 (new single-family construction, except for-sale builders): **~60,635 establishments**, attributed by a third-party aggregator to County Business Patterns 2023; another aggregator gives **59,568** (year not stated); one site gives a **$117.8B** market size citing the 2022 Economic Census. None verified against census.gov — [WS] [Vanta Insights](https://vantainsights.com/industry/236115-new-single-family-housing-construction); [HigherGov](https://www.highergov.com/naics/236115-new-single-family-housing-construction-except-for-sale-builders/); [Mewayz](https://data.mewayz.com/industry/236115) (which number belongs to which site was not pinned).
- For historical scale, a Census Statistical Abstract table (2002 NAICS basis) listed **~113,948** establishments in 236115 — [WS] [Census Statistical Abstract 2009, table 919 (UNT archive)](https://webarchive.library.unt.edu/web/20090827041825/http://www.census.gov/compendia/statab/tables/09s0919.pdf). Inference below; definitions may differ.
- NAICS 236118 (residential remodelers): **132,711 firms / 133,345 establishments / 462,690 employees** per a commercial directory that names no source — [WS] [Mewayz NAICS 236118](https://data.mewayz.com/industry/236118) (treat as unverified).
- BLS payroll series for 236118 (production and nonsupervisory employees only) ran **285.4k–297.1k** across 2024 monthly readings — [WS] [BLS CES table 6b, Aug 2024](https://www.bls.gov/ces/data/employment-and-earnings/2024/table6b_202408.htm).
- County Business Patterns 2023 publishes establishments by employment-size class at 6-digit NAICS (the right source for the 1–20-employee cut) — [WS] [data.gov CBP 2023](https://catalog.data.gov/dataset/2023-county-business-patterns); [Census CBP API](https://www.census.gov/programs-surveys/cbp/data/api.html). The API call (`/data/2023/cbp?...NAICS2017=236115`) was blocked (proxy 403).

**Size of the typical firm (NAHB member censuses, 2025 data, published Sept 2026)**
- Builder members: median **5 housing starts** in 2025 (6 in 2024), **~7% started none**, median **6 payroll employees** (unchanged since 2023), median revenue **$3.7M** (flat). NAHB attributes low headcount to "extensive use of subcontractors" — [WS] [NAHB blog, Sept 2026](https://www.nahb.org/blog/2026/09/builder-member-census-median-revenue-flat); [Eye on Housing](https://eyeonhousing.org/2026/09/who-are-nahbs-builder-members-2/).
- Remodeler members: median revenue **$2.1M** in 2025, up ~24% from **$1.7M** in 2024; median **5 employees**. In 2024 the largest revenue band (**44%**) was **$1M–$5M** — [WS] [NAHB remodelers census](https://www.nahb.org/blog/2026/09/residential-remodelers-nahb-census-data); [Eye on Housing](https://eyeonhousing.org/2026/09/nahb-remodelers-what-the-data-says/); [Pro Remodeler](https://www.proremodeler.com/home/news/55324854/nahb-remodeler-members-mostly-operate-small-businesses).

**Margins (NAHB Cost of Doing Business)**
- Single-family builders, FY2023 (2025 edition): **gross 20.7%, net 8.7%** (highest in 30+ years; series peak 10% in 1991); cost of sales **79.3%** of revenue, operating expenses **12.0%**. **Top 25%: 29.7% gross / 17.7% net. Bottom 25%: 17.0% gross / −1.4% net.** FY2020: 18.2% / 7.0%. NAHB expected 2024 margins to shrink because of rate buydowns and price cuts — [WS] [NAHB press release, Apr 2025](https://www.nahb.org/news-and-economics/press-releases/2025/04/nahbs-new-study-provides-statistics-and-data-on-builder-financial-performance); [Eye on Housing](https://eyeonhousing.org/2025/03/builders-profit-margins-improved-in-2023/).
- Remodelers, FY2024 (2026 edition): **gross 29.9%, net 6.3%** (highest since 1996; 3% in 2011) — [WS] [Eye on Housing, Apr 2026](https://eyeonhousing.org/2026/04/remodelers-saw-profit-margin-gains-in-2024/).

**Software use and estimating time**
- Houzz State of the Industry 2025 (n = 1,537 US renovation businesses): **37% of specialty contractors and 33% of general contractors** relied on software for estimating costs or bids — [WS] [2025 US Houzz State of the Industry (PDF)](https://st.hzcdn.com/static/econ/2025_US_Houzz_State_of_the_Industry.pdf).
- Remodeling/JLC reader panel: "nearly half" of companies spend **more than 10 hours** preparing a bid, some **up to 50 hours** on a single bid, and most still do it free — [WS] [JLC reader survey on competitive bidding](https://www.jlconline.com/business/reader-survey-on-competitive-bidding/) (survey date/sample not captured).
- A remodeling consultancy's illustration (not a survey) assumes ~45 minutes per estimate vs ~3 hours for a thorough one — [WS] [Remodelers Advantage](https://remodelersadvantage.com/?p=6849).
- Construction firms using AI tools for business tasks: 52% in mid-2026 (Houzz), 80% of users daily; 23% use AI for estimating (AGC/Sage, Jan 2026) — [Repo] [Roofing Contractor on Houzz survey](https://www.roofingcontractor.com/articles/102644-ai-use-jumps-among-construction-firms-houzz-survey-finds); [AGC/Sage 2026 Outlook](https://www.agc.org/news/2026/01/08/contractors-have-dampened-expectations-2026-apart-data-centers-and-power-projects-amid-worries-about).

**Cost structure of the product they sell**
- NAHB Construction Cost survey (fielded fall 2024): construction = **64.4%** of the average new-home sales price (**$428,215 of $665,298**), finished lot 13.7%; highest construction share since the survey began in 1998. A secondary source derives **~$162/sq ft** on a 2,647 sq ft home (arithmetic checks out) — [WS] [Pro Builder](https://probuilder.com/how-much-home-sales-price-construction-costs); [Corridor Business](https://corridorbusiness.com/national-association-of-home-builders-over-half-of-homes-sales-price-goes-to-construction-costs/).
- Regulation adds **$131,734** (26.4% of a $499,500 average price, Jan 2026) per a separate NAHB study — [WS] [LBM Journal](https://www.lbmjournal.com/industry-news/data/press-release/15827189/national-association-of-home-builders-new-nahb-study-shows-regulatory-costs-jumped-40-in-5-years).

### Inferences
- The ICP's "1–20 employees, $1M–$20M" band brackets the NAHB medians, so NAHB/NARI member data is a fair proxy; the 236115+236118 universe is likely ~150,000–190,000 establishments before nonemployers (sum of the unverified counts; label as estimate).
- The 236115 establishment count roughly halved between the 2002 table (~114k) and 2023 (~60k), consistent with consolidation after 2008 — **likely**, but definitions and coverage may differ; verify before quoting.
- Margin arithmetic makes the "lost money on one job" trigger concrete: at a 20.7% gross / 8.7% net builder margin, a 5% estimating miss on direct costs (79.3% of revenue) wipes out ~4 points of net, about half the year's profit; for the bottom quartile (−1.4% net) any miss is a loss. (Researcher arithmetic.)
- Two-thirds of renovation GCs (67%) do **not** use software for estimating (Houzz 2025) → the main alternative is Excel/gut feel, not a competitor product; "habit" is the dominant restraining force.

### Gaps
- Census CBP 2023 / SUSB size-class counts (1–4, 5–9, 10–19 employees) for 236115 and 236118, and Nonemployer Statistics counts — API and site blocked.
- Houzz 2026 State of the Industry estimating-software share (only 2025 found).
- NARI member profile (revenue, employees) — not searched before the budget ran out.
- Hours-per-estimate from a probability survey (only the JLC reader panel and a consultant illustration found).

---

## B. Geography

### Takeaway
Volume is in the Sun Belt (Texas 140,002 single-family permits in 2025, then Florida and North Carolina; Houston, Dallas, Phoenix, Atlanta, Charlotte lead metros), but estimate accuracy is worth the most in high-cost California markets where Quotr already has proof (Bay Area procurement projects, LA fire-rebuild sample) and where $/sq ft runs several times the ~$162 national construction figure. Recommended: one California hub with Bay Area and LA-rebuild spokes first, a Texas Triangle spoke second, Carolinas/Atlanta third; no 50-state pages.

### Cited Findings
**Single-family permits 2025 (volume markets)**
- US single-family permits 2025: **909,280** — [WS] [NAHB Eye on Housing, Mar 2026](https://eyeonhousing.org/2026/03/single-family-permits-end-2025-on-a-soft-note/).
- Texas **#1 with 140,002 permits (−11.7% vs 2024)**; Florida #2 (**−10.3%**); North Carolina #3 (**−6.9%**) — [WS] [NAHB permits by state and metro](https://www.nahb.org/News-and-Economics/Housing-Economics/State-and-Local-Data/Building-Permits-by-State-and-Metro-Area); [Eye on Housing](https://eyeonhousing.org/2026/03/single-family-permits-end-2025-on-a-soft-note/) (sources differ; Florida/NC absolute counts not captured).
- Metro leaders (GlobeSt, Jan 27 2026, year-to-date; cut-off month not confirmed): **Houston 40,471 (−11%), Dallas 34,778 (−14%), Phoenix 20,318 (−23%), Atlanta 19,610 (−12%), Charlotte 14,211 (−13%)** — [WS] [GlobeSt](https://www.globest.com/amp/2026/01/27/single-family-permits-decline-as-builders-adjust-to-market-challenges/). Through July 2025, Austin had 9,839 (−7%) — [WS] [GlobeSt, Sept 2025](https://www.globest.com/amp/2025/09/17/mixed-signals-for-housing-permits-as-metro-rankings-shift-again/).

**Remodeling spend (all markets)**
- Harvard JCHS LIRA (latest, ~Oct 2026): annual owner improvement spending **$524B in 2026-Q4 → $527B in 2027-Q3**, growth easing **2.4% → 1.5%**; flat remodeling permits and building-product sales cited; next release **Jan 21, 2027** — [WS] [JCHS](https://www.jchs.harvard.edu/press-releases/remodeling-spending-continues-stagnate); [NARI repost of an earlier 2026 release](https://nari.org/nari-blog-main/remodeling-spending-slowdown/). April 2026 revision had $509B (end 2025) → $518B (2026-Q4) — [WS] [JCHS](https://www.jchs.harvard.edu/press-releases/remodeling-growth-set-downshift-late-2026).
- JCHS *Improving America's Housing 2025*: improvement and repair spending rose from **$404B (2019) to $611B (2022)**, expected above $600B through 2025; homeowners spent ~**$4,700** on improvements in 2023 — [WS] [JCHS report PDF](https://www.jchs.harvard.edu/sites/default/files/reports/files/Harvard_JCHS_Improving_Americas_Housing_2025.pdf).
- Older JCHS metro data (2013 data, 2015 report): San Francisco and San Jose had the highest improvement spending in the West; discretionary kitchen/bath/addition projects concentrate in high-home-value metros — [WS] [JCHS Improving America's Housing 2015 ch. 4](https://www.jchs.harvard.edu/sites/jchs.harvard.edu/files/jchs_improving_americas_housing_2015_chap4.pdf) (dated).

**High-cost markets and Quotr's existing footprint**
- National construction cost ~**$162/sq ft** (NAHB fall-2024 survey, derived) vs LA fire-rebuild answers of **$400–$800+/sq ft** from Bloomberg and local GCs (Perplexity test S12) — [WS] [Pro Builder](https://probuilder.com/how-much-home-sales-price-construction-costs); [Repo] buyer-questions-by-trade.md §17.
- Quotr Procurement proof sits in the Bay Area: Myren Dr, Saratoga **$97,000 vs $187K–$218K** Bay Area market; Stratford Ct, Monte Sereno **$108,290 vs $195K–$245K**; Skyfarm Dr, Hillsborough **$30,437 vs $58K–$76K** (project type not stated) — [Repo] [quotr.ai/procurement](https://quotr.ai/procurement/) via product-and-features.md §3.11.
- Quotr Service sample library includes "Fast Cost Estimation (Residential LA Fire Rebuilding)"; Quotr launched a free "FireTips" app for LA fire victims in Feb 2025 — [Repo] [quotr.ai/service](https://quotr.ai/service/); [firetips.quotr.io](https://firetips.quotr.io/).
- Quotr lists BIA Bay Area membership (status TO CONFIRM) and attended Dallas Build Expo in 2026 — [Repo] audiences-and-personas.md §5; partnerships-and-marketplaces.md.
- Quotr's estimating database offers "Quotr's average costs by US zip code" — [Repo] [quotr.ai/software](https://quotr.ai/software/) via product-and-features.md §3.3.

### Inferences — priority geo segments (evidence rows)

| # | Segment | Evidence row | Job / why Quotr fits | Prompt stems | Priority |
|---|---|---|---|---|---|
| G1 | **Bay Area custom home, ADU and remodel builder** (Santa Clara, San Mateo, Alameda, Contra Costa) | Highest-cost market; JCHS (dated) top West remodel spend in SF/San Jose; Quotr HQ Berkeley, BIA Bay Area member (TO CONFIRM); 3 procurement projects with 45–56% below-market finish packages (Quotr-reported) | Accurate plan-based numbers on $1M+ jobs where a 5% miss is $50k+; finish packages (cabinets, windows) are a large share | "cost to build a custom home per square foot Bay Area 2026", "ADU cost San Jose 2026", "estimating software custom home builder California" | **1 (home turf, proof exists)** |
| G2 | **LA fire-rebuild builder** (Palisades, Altadena, Malibu) | $400–$800+/sq ft answers; Quotr rebuild sample + FireTips app; insurance-driven homeowners need fast, defensible numbers | Urgent "homeowner/insurer needs a number" job → Quotr Service $0.25/sq ft | "cost to rebuild a house after the LA fires per square foot 2026", "rebuild estimate for insurance claim" | **1b** |
| G3 | **Texas Triangle custom/small-volume builder** (Houston, Dallas–Fort Worth, Austin) | TX 140,002 permits (−11.7%); Houston and Dallas top metros, both down 11–14% | Falling volume → more bids per win → estimate speed and win rate; lumber/tariff swings on fixed bids | "estimating software for custom home builders Texas", "cost per square foot to build a house Houston 2026" | 2 |
| G4 | **Carolinas + Atlanta growth corridor** | NC #3 (−6.9%); Charlotte 14,211, Atlanta 19,610 | Same speed job; many 1–10-person builders (likely) | "home builder estimating software Charlotte", "cost to build per square foot NC 2026" | 3 |
| G5 | **Northeast / Pacific NW high-cost remodelers** (Boston, NYC suburbs, Seattle, Portland) | **Evidence gap**: no 2025 metro remodel-spend table retrieved | Older stock, complex remodels; likely high value per estimate | — | Hold until data |

- **Are geo pages justified?** Yes, but narrowly. $/sq ft genuinely differs by 2.5–5× between the national construction figure and LA rebuild answers, and Quotr claims zip-code cost data, so a California hub plus 2 metro spokes (Bay Area, LA rebuild) carries real, citable differences. Texas/NC spokes only if Quotr's zip-code database yields distinct, dated numbers. Templated 50-state pages would fall under the scaled-content-abuse risk the framework documents ([FW] Google spam policies). Energy-code (e.g., California Title 24) and permit-timeline pages are plausible differentiators but unsourced here — verify first.
- Volume markets (TX, FL, NC) argue for speed/price messaging (Lite, Service); high-cost markets argue for accuracy and finish-materials savings (Plus, Procurement).

### Gaps
- Full-year 2025 metro permit ranking from Census BPS (only GlobeSt YTD found); California, Washington and Massachusetts state permit counts.
- JCHS 2025 metro per-owner remodeling spend (needed for G5).
- Google Trends/Keyword Planner demand by DMA (not pulled).
- California Title 24 2025 effective date and permit timelines (not sourced this session).

---

## C. Jobs-to-be-done (in the buyer's words)

### Takeaway
Five jobs recur: get a number the homeowner will sign without losing my shirt; stop burning nights on free estimates; turn architect PDFs into quantities fast; protect a fixed bid from material swings; and look professional enough to win against bigger outfits. Wording below mixes observed thread titles with researcher-written job statements (labeled).

### Cited Findings
- Observed buyer wording (thread titles, verbatim): "Bidding on kitchen remodels" — [Repo] [ContractorTalk](https://www.contractortalk.com/threads/bidding-on-kitchen-remodels.337881/); "Contractor mark up on cabinets?" — [Repo] [Houzz discussion](https://www.houzz.com/discussions/2687506/contractor-mark-up-on-cabinets); "Question about sending estimates for jobs" — [Repo] [r/Construction](https://www.reddit.com/r/Construction/comments/1buzvjn/question_about_sending_estimates_for_jobs/); "How fast do you estimate?" — [Repo] [r/estimators](https://www.reddit.com/r/estimators/comments/1j7h8eu/how_fast_do_you_estimate/); "Are there actually any AI-based takeoff software?" — [Repo] [r/estimators](https://www.reddit.com/r/estimators/comments/1kadwx5/are_there_actually_any_aibased_takeoff_software/).
- Remodel pricing practice: fixed price for known scope plus cost-plus allowances for hidden conditions and selections; "Never price a remodel from photos, phone descriptions, or 'it is just a simple bathroom.'" (vendor guide wording) — [WS] [Projul, how to price a remodel job](https://projul.com/blog/how-to-price-remodel-job).
- NAHB Remodelers on estimate depth: the estimate must be "Specific enough to guess at each element of the scope of work, and general enough not to waste too much time if you don't get the job." — [WS] [Pro Remodeler (NAHB Remodelers column)](https://proremodeler.com/3-tips-charging-estimates) (page not opened; attribution to this URL is the search engine's).

### Inferences
| Job (researcher wording, built from the evidence above) | Situation | Desired outcome |
|---|---|---|
| J1 "Give me a number I can stand behind by Friday" | Homeowner/architect wants a price this week | A defensible, itemized bid from the plan set without guessing |
| J2 "Stop giving away 10 hours per free estimate" | Too many tire-kicker requests | Rough-but-safe ballpark in minutes; full estimate only for qualified jobs |
| J3 "Get the quantities off these PDFs without counting by hand" | Architect plans, owner's sketch | Takeoff (SF, LF, EA) feeding my own unit costs |
| J4 "Don't let lumber/tariffs eat my fixed bid" | Price swings between bid and buyout | Current costs, escalation clause, allowances that hold |
| J5 "Look as professional as the big builders" | Competing against firms with estimators | Clean proposal with options, selections and allowances |

### Gaps
- No switch interviews were possible; the framework's 6–12 recent-switcher interviews remain the validation step.

---

## D. Psychology

### Takeaway
A field-trained owner who now runs a 5–6-person company, prices at night, fears underpricing more than losing a bid, distrusts software "built for commercial", and buys alone (or with a spouse/bookkeeper). Hot moments: the evening after a site visit and the day a homeowner pushes for a number; cold moments: winter planning and the New Year. Design around anchoring, status-quo/defaults and temporal landmarks (robust); do not lean on generic social proof or choice overload (fragile).

### Cited Findings
- Owner-run, small headcount: median 5–6 employees, heavy subcontracting — [WS] [NAHB builder census](https://www.nahb.org/blog/2026/09/builder-member-census-median-revenue-flat); [NAHB remodeler census](https://www.nahb.org/blog/2026/09/residential-remodelers-nahb-census-data).
- After-hours estimating is the norm (headlines, verbatim): "Estimating Firm's Log-In Records Prove It: Working Late Is Standard Business for Remodelers" — [WS] [JLC](https://www.jlconline.com/?p=87891); "Work Late Hours? You're Not Alone" — [WS] [JLC](https://www.jlconline.com/?p=109495).
- Free-estimate resentment (headlines, verbatim): "If Time Is Money, Why Are You Still Offering Free Estimates?" — [WS] [JLC](https://www.jlconline.com/business/sales-marketing/if-time-is-money-why-are-you-still-offering-free-estimates_o/); "Giving It Away: It's Time to Dispel the Free-Estimate Myth" — [WS] [JLC](https://www.jlconline.com/?p=58782).
- Fear of losing money outweighs fear of losing the bid (forum advice): "Do not take the job if you will lose money and not stay in business." — [WS] Fine Homebuilding forum thread (one of [pricing mistake](https://finehomebuilding.com/forum/pricing-mistake-what-to-do) / [estimating strategy](https://finehomebuilding.com/forum/estimating-strategy); exact thread not pinned).
- Distrust of AI accuracy: data accuracy is contractors' top AI worry (57%, Dodge/CMiC); r/estimators threads call AI takeoff "hit-or-miss" — [Repo] [Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/); [r/estimators](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/). Construction leaders' trust in AI fell 14 points YoY (Autodesk) — [Repo] [Autodesk](https://www.autodesk.com/blogs/construction/state-of-design-make-spotlight-construction/).
- Category self-identity cue: Handoff tells AI it is **not** "a commercial construction management platform" and that its users are "remodelers, home builders, trade contractors" — [Repo] [handoff.ai official information](https://www.handoff.ai/official-information-about-handoff). Quotr's own /disambiguation/ calls it a platform for "commercial general contractors, large specialty subcontractors, and real estate development funds" — [Repo] audiences-and-personas.md §5.
- Outlook mood: 69% of construction firms expected product/material costs to rise in 2026 (Houzz Q1 2026 barometer); 86% expected to change how they run the business (Q4 2025) — [WS] [Houzz Q1 2026 barometer](https://www.houzz.com/magazine/2026q1-u-s-houzz-pro-industry-barometer-construction-stsetivw-vs~184309158); [Houzz Q4 2025](https://www.houzz.com/magazine/home-professionals-close-2025-with-varying-levels-of-optimism-stsetivw-vs~182774788).
- Bias replication ranking (apply as written): robust = defaults/status quo (d = 0.68), anchoring, temporal landmarks (New Year "diet" searches +82.1%); fragile = generic social proof (smallest nudge effect, 0.94 pp), choice overload (meta d = 0.02); hot/cold empathy gap and time pressure shift buyers to non-compensatory rules — [FW] (Jachimowicz 2019; Many Labs; Dai, Milkman & Riis 2014; DellaVigna & Linos; Scheibehenne 2010; Dhar & Nowlis 1999).

### Inferences
| Trait | Evidence status | GEO implication |
|---|---|---|
| Identity: tradesman → owner; estimating learned on the job | Likely (headcount, forum tone) | Write like a builder, show units (SF/LF/EA), never "enterprise" language |
| Fear of underpricing > fear of losing bid | Likely (forum advice, bottom-quartile −1.4% net) | Lead accuracy claims with "how to check the AI's numbers" steps, not speed alone |
| Homeowner pressure ("need a number this week") | Likely | Urgent-mode page: "ballpark from plans in 24 h" with Service price per sq ft |
| Time poverty / night estimating | Known (JLC headlines, >10 h per bid) | Pages should answer in the first 60 words; mobile-readable |
| Distrust of "software that doesn't get residential" | Likely (Handoff positioning works; Quotr's own commercial framing) | A residential hub must say "single-family, custom, ADU, remodel" in titles, examples and plan sizes |
| Decision unit: solo owner, spouse often bookkeeper | **Speculative** (no source found) | Pricing page must be self-serve; monthly, cancel-anytime |
| Hot moments: 8–11 pm after site visits; day a homeowner calls | Likely | Urgent answer pages + "do it for me" Service CTA |
| Cold moments: Dec–Feb planning, New Year, IBS/KBIS | Likely (temporal landmarks robust) | Considered-mode comparison pages, refreshed before January |
| Anchoring | Robust | Publish clear anchors: Lite $79.90/seat vs Handoff Scale $719–$899/mo for plan takeoff; Service $0.25/sq ft vs owner's 10 h |
| Status quo / defaults | Robust | "Keep Buildertrend/JobTread for PM, add estimating" framing lowers habit force |
| Generic social proof ("thousands of builders") | Fragile | Use verifiable review counts and named residential case studies instead |

### Gaps
- No interview or survey on the spouse/bookkeeper role or on time-of-day of estimating beyond JLC headlines.
- No source for the share of owners who estimate personally vs employ an estimator.

---

## E. Four forces (with verbatim quotes)

### Takeaway
Push = underpriced jobs, night/free estimating, material swings, forced migrations (CoConstruct → Buildertrend) and PM-suite price hikes; Pull = "more features at a lower price", AI takeoff from plans, local current costs; Anxiety = AI accuracy, residential fit, learning curve; Habit = Excel, gut-feel $/sq ft, an existing PM suite. Most verbatims available this session are review/forum extracts captured by search (not opened) and thread titles from prior research.

### Cited Findings
**Verbatim quotes (each with URL; [WS] = search-extract wording, page not opened)**

| # | Force | Quote (verbatim) | Speaker / context | Source |
|---|---|---|---|---|
| 1 | Push (price) | "price to be too high for our small construction firm to handle" | Capterra reviewer, small firm, about Buildertrend | [WS] Capterra review pages returned for the query, e.g. [Buildertrend reviews p.3](https://www.capterra.com/p/70092/Buildertrend/reviews/?page=3), [p.8](https://www.capterra.com/p/70092/Buildertrend/reviews/?page=8) (exact page not pinned) |
| 2 | Push → switch | "BuilderTrend's system was way too expensive and too cumbersome for the fast-paced, agile environment of our General Contracting firm" | GC who switched to JobTread | [WS] [Capterra JobTread reviews](https://capterra.com/p/218503/JobTread/reviews/) (pages 2–5 returned; not pinned) |
| 3 | Push (price shock) | "the price of buildertrend was about to triple" | Former Buildertrend user, now JobTread | [WS] [Capterra JobTread reviews p.3](https://capterra.com/p/218503/JobTread/reviews/?page=3) (not pinned) |
| 4 | Push (estimating module) | "the estimate software is bad, and way too complicated" | Reviewer who moved off CoConstruct | [WS] [Capterra JobTread reviews p.4](https://capterra.com/p/218503/JobTread/reviews/?page=4) (not pinned) |
| 5 | Pull | "a lot more features at a lower price" | JobTread reviewer explaining the switch | [WS] [Capterra JobTread reviews p.2](https://capterra.com/p/218503/JobTread/reviews/?page=2) (not pinned) |
| 6 | Habit / anxiety (time) | "Specific enough to guess at each element of the scope of work, and general enough not to waste too much time if you don't get the job." | NAHB Remodelers column on estimates | [WS] [Pro Remodeler](https://proremodeler.com/3-tips-charging-estimates) |
| 7 | Push (free estimates) | "If Time Is Money, Why Are You Still Offering Free Estimates?" | JLC headline (trade voice) | [WS] [JLC](https://www.jlconline.com/business/sales-marketing/if-time-is-money-why-are-you-still-offering-free-estimates_o/) |
| 8 | Push (night work) | "Working Late Is Standard Business for Remodelers" | JLC headline citing an estimating firm's log-in records | [WS] [JLC](https://www.jlconline.com/?p=87891) |
| 9 | Anxiety (losing money) | "Do not take the job if you will lose money and not stay in business." | Fine Homebuilding forum reply to an underbidding contractor | [WS] [Fine Homebuilding forum](https://finehomebuilding.com/forum/pricing-mistake-what-to-do) (thread not pinned) |
| 10 | Anxiety (AI) | "Are there actually any AI-based takeoff software?" | r/estimators thread title | [Repo] [r/estimators](https://www.reddit.com/r/estimators/comments/1kadwx5/are_there_actually_any_aibased_takeoff_software/) |
| 11 | Anxiety (AI) | "hit-or-miss" (on AI takeoff tools) | r/estimators commenters, via Perplexity | [Repo] [r/estimators](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/) |
| 12 | Push (forced migration) | "Leaving CoConstruct? Here is why builders are choosing JobTread" (title as indexed) | JobTread blog targeting migrating CoConstruct users | [WS] [JobTread blog](https://jobtread.com/blog/leaving-coconstruct-here-is-why-builders-are-choosing-jobtread) |
| 13 | Habit (Mac/tooling) | "macOS takeoff app that actually works" | r/estimators thread title | [Repo] [r/estimators](https://www.reddit.com/r/estimators/comments/1rpfwg0/macos_takeoff_app_that_actually_works/) |
| 14 | Push (materials) | "Contractor mark up on cabinets?" | Houzz discussion title | [Repo] [Houzz](https://www.houzz.com/discussions/2687506/contractor-mark-up-on-cabinets) |

**Paraphrased evidence (not quotable verbatim)**
- Capterra Buildertrend reviews (search summary): estimating is "the most common target" — overly complicated, line items can't be grouped as needed, the software struggles with many line items and the vendor's fix was to "use fewer lines"; long learning curve for budgets/estimates/selections; price hard to justify for few projects a year; one introductory rate rose after onboarding; positives: estimating templates, job-costing budget, support — [WS] [Capterra Buildertrend reviews](https://www.capterra.com/p/70092/Buildertrend/reviews/) (pages 1, 5, 7, 8, 16, 37).
- A Capterra comparison page cites a user saying Buildertrend feels restrictive for highly detailed or non-standard estimates — [WS] [Capterra Buildertrend vs Buildxact](https://www.capterra.com/compare/70092-173135/Buildertrend-vs-buildXACT).
- Buildxact reviewers: pricing features complex for new users; mobile app "needs refinement" — [Repo] buildxact.md (search summary).
- r/Contractor "Bidding" thread: one commenter lost a bid for not being expensive enough; another compared selling a premium service to a Ferrari buyer who wants a Honda — [WS] (mirror of r/Contractor/comments/1jrg2jj; [reddit.com link](https://www.reddit.com/r/Contractor/comments/1jrg2jj/bidding/)).

### Inferences
| Force | Strength for this ICP | Prompt class it produces |
|---|---|---|
| Push | Strong and event-driven (bad job, price hike, migration, tariff) | "is it normal to lose money on…", "how do I stop doing free estimates", "how to price lumber swings into a fixed bid" |
| Pull | Moderate; attracted by AI takeoff and lower price | "software that does takeoff from architect PDFs for home builders", "Buildertrend alternative cheaper" |
| Anxiety | Strong: accuracy, residential fit, learning curve, import quality (Procurement) | "is AI takeoff accurate on residential plans", "Quotr reviews", "Handoff vs Quotr" |
| Habit | Strongest (≈2/3 of GCs use no estimating software; PM suites entrenched) | "do I need estimating software or is Excel fine", "can Buildertrend do takeoffs" |
- Content that answers only pull ("best AI estimating software") leaves the two restraining forces unanswered — the framework's warning applies directly ([FW]).

### Gaps
- No direct reads of r/Contractor, r/HomeBuilding, r/Carpentry, ContractorTalk, JLC forums, Facebook groups, G2/App Store reviews of Houzz Pro, Handoff, Clear Estimates or Joist (blocked/budget). Recommend a 2–4-hour desk-ethnography pass (50 top posts per community) before content production.

---

## F. Trigger events and trigger calendar

### Takeaway
Triggers are a mix of datable calendar landmarks (New Year, IBS/KBIS in February, spring rush, LIRA release Jan 21 2027, the **Jan 1 2027 Section 232 cabinet/vanity tariff step-up**) and private shocks (a money-losing job, a PM-suite price hike, an office manager quitting, a homeowner deadline). The cabinet-tariff date is ~8 weeks away and is the single best-timed trigger for Quotr's Procurement cross-sell.

### Cited Findings
- Section 232 tariff of **25%** on imported kitchen cabinets, vanities and parts since **Oct 14, 2025**; increase to **50%** delayed to **Jan 1, 2027**; AD/CVD orders on Chinese wooden cabinets/vanities since Apr 21, 2020, continued 2025 — [Repo] [Thompson Hine SmarTrade](https://www.thompsonhinesmartrade.com/2026/01/president-trump-delays-section-232-tariff-increase-on-wood-furniture-cabinets-and-vanities/); [Federal Register](https://www.federalregister.gov/documents/2025/09/17/2025-17986/wooden-cabinets-and-vanities-and-components-thereof-from-the-peoples-republic-of-china-continuation).
- Tariff cost **$7,500–$10,900 per home** (JEC, Apr 2026); ~$30B added, ~90% on new construction (Brookings) — [Repo] [JEC report](https://www.jec.senate.gov/public/_cache/files/fe5d79b2-97cb-4c55-aeba-3e31fdd235fd/april-2026-final-jec-report-on-housing.pdf); [Brookings](https://www.brookings.edu/articles/recent-tariffs-threaten-residential-construction/).
- AGC: 40% of contractors raised bid prices because of tariffs (Jan 2026 survey); input costs +8.9% Aug 2025–Aug 2026; lumber and plywood +9.9% YoY by July 2026 — [Repo] [AGC Jan 2026](https://www.agc.org/news/2026/01/14/construction-costs-rise-fastest-rate-january-2023-november-outpacing-increases-contractors-bid); [AGC Sept 2026](https://www.agc.org/news/2026/09/10/construction-input-costs-climb-89-between-august-2025-and-august-2026-association-survey-finds-war); [AGC Aug 2026](https://www.agc.org/news/2026/08/13/construction-input-costs-climb-71-percent-between-july-2025-and-july-2026-impacts-war-and-tariffs).
- Remodeling cooling: LIRA growth easing to 1.5% by 2027-Q3; next release Jan 21, 2027 — [WS] [JCHS](https://www.jchs.harvard.edu/press-releases/remodeling-spending-continues-stagnate).
- Spring seasonality: Houzz Q2 2026 barometer fielded Mar 17–Apr 6 (n = 462 construction firms); trade coverage "Construction pros see spring rebound despite economic uncertainty" — [WS] [Houzz Q2 2026](https://www.houzz.com/magazine/2026q2-u-s-houzz-pro-industry-barometer-construction-stsetivw-vs~185077238); [JBiz News](https://jbiznews.com/?p=306211).
- Fresh-start effect: New Year raises goal-related searches (diet +82.1%); start of week +14.4% — [FW] Dai, Milkman & Riis 2014.
- CoConstruct migration as a trigger: JobTread runs "Leaving CoConstruct" content — [WS] [JobTread](https://jobtread.com/blog/leaving-coconstruct-here-is-why-builders-are-choosing-jobtread).

### Inferences — trigger calendar (dated where possible)
| Window | Trigger | Mode | Product line | Content/refresh action |
|---|---|---|---|---|
| Nov–Dec 2026 | Cabinet/vanity 232 step-up on **Jan 1, 2027**; year-end bids for spring starts | Cold → hot near deadline | Procurement, Software | Publish dated "232 cabinet tariff Jan 1, 2027: what builders should do now" by early Dec |
| Late Dec–Jan | New Year fresh start; winter planning; LIRA release **Jan 21, 2027** | Cold/considered | Software (Lite/Plus) | Refresh all comparison/pricing pages in first week of January |
| February | IBS + KBIS (typically co-located "Design & Construction Week"; 2027 dates not verified) | Cold, browsing | Software, Procurement | Event-timed "what we saw" + demo offers; booth/talk if feasible |
| Mar–May | Spring rush: bid volume peaks, homeowner deadlines | **Hot** | Service ($0.25/sq ft), Lite | Urgent pages: "need a number this week" |
| Any time | Lost money on a job / underpriced change orders | **Hot** then reflective | Software | "Underpriced a job? what to fix in your estimate" |
| Any time | PM-suite renewal or price hike (Buildertrend "about to triple") | Considered | Software | "Keep your PM tool, add estimating" + vs pages |
| Any time | Office manager/estimator quits | Hot | Service, Plus | "Outsourced estimating for home builders: cost per sq ft" |
| Any time | Lumber/tariff news spike (AGC monthly PPI posts) | Hot (for open bids) | Software (cost DB), Procurement | Monthly-refreshed "material cost update for builders" |
| Summer–fall | Slower remodel growth → more competitive bids, more free estimates | Mixed | Software, Service | "paid vs free estimates" guidance |

### Gaps
- IBS/KBIS 2027 dates and location; PCBC dates — not verified.
- CoConstruct sunset date — not verified.
- No Google Trends seasonality pulled for "estimating software" or "cost to build per square foot".

---

## G. Switch timeline with prompt form at each stage

### Takeaway
Prompt tense and specificity track the stage: vague situational prompts at first thought, category nouns while actively looking, brand names and prices when deciding. For this ICP the timeline is short when triggered by a hot event (days) and long when it is a PM-suite renewal (months).

### Cited Findings
- Stage-to-prompt mapping (first thought → passive → active → deciding → consuming), awareness levels (problem-aware → solution-aware → product-aware) and fan-out injection of "best", "reviews", "2026", "vs", "price" — [FW] (Moesta/Spiek; Peec fan-out analysis; Ahrefs).
- 51% of B2B software buyers start research in an AI chatbot (G2 survey, directional) — [Repo] [G2/PR Newswire](https://www.prnewswire.com/news-releases/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots-302742807.html).
- Free trials: Quotr 7 days; Handoff 7 days; Buildxact 14 days and a $0 Go plan — [Repo] pricing reads 2026-09-25.

### Inferences
| Stage | Typical duration (estimate) | What is happening | Prompt form (examples, researcher-written) |
|---|---|---|---|
| 1 First thought | Hours after a trigger | "I can't keep doing this" | "I lost $30k on a remodel because I underpriced framing, how do contractors avoid this" |
| 2 Passive looking | 1–8 weeks | Notices peers' tools, YouTube, FB groups | "how do small builders do estimates from architect plans", "is Excel good enough for estimating a custom home" |
| 3 Active looking | 1–3 weeks | Names category, sets constraints | "best estimating software for custom home builders 2026 that does takeoff from PDFs", "Buildertrend estimating vs standalone estimating software" |
| 4 Deciding | 3–10 days | Brands, prices, objections | "Quotr vs Handoff for a 4-person builder", "is AI takeoff accurate on residential plans", "Quotr pricing per seat" |
| 5 Trial/onboarding | 7–14 days | Runs one real job | "how to set markup in Quotr", "how to import my cost book" |
| 6 Re-decision | Renewal or bad job | Keep/expand/churn | "Quotr alternatives", "cheaper estimating software for remodelers" |
- In-market arithmetic ([FW] method): if the software re-decision interval is ~3–5 years (**speculative**), ~5–8% of firms are choosing estimating software in any quarter; but the *informational* clusters (pricing, $/sq ft, markup, tariffs) recur on every job, so they deserve more pages than "best software" alone.

### Gaps
- No observed switch timelines (needs 6–12 interviews with recent Quotr/Handoff/Buildxact sign-ups and churns).

---

## H. Current alternatives and what does NOT satisfy them

### Takeaway
The real competitor is "no estimating software" (≈2/3 of GCs): Excel, gut-feel $/sq ft, sub/supplier quotes and cost-plus. Among tools, estimating is buried in PM suites that small firms find expensive and complicated, and plan-based takeoff is missing, paywalled or capped in residential tools. Ranked unmet needs below are by evidence emphasis, not a coded count.

### Cited Findings
- Only 33% of renovation GCs and 37% of specialty contractors use software for estimating — [WS] [Houzz 2025 SOI](https://st.hzcdn.com/static/econ/2025_US_Houzz_State_of_the_Industry.pdf).
- Pricing method guidance: hybrid fixed price + cost-plus allowances; formula price = labor hours × billable rate + materials + sub bids + contingency; warning that overestimating billable days underprices every job — [WS] [Projul](https://projul.com/blog/how-to-price-remodel-job) and other guides returned for the same query (attribution per search extract).
- Handoff: AI takeoff from plans only on **Scale ($719/mo annual, $899 monthly)**, residential plans **up to 5,000 sq ft**; Flex $119/$149 has none — [Repo] [handoff.ai/pricing](https://www.handoff.ai/pricing).
- Buildxact: Blu Takeoff Assistant only as +$99/mo on Pro or included in Master ($509/$599); Blu Estimate Reviewer +$149/mo; described by Handoff as "AI as a paid add-on" — [Repo] [buildxact.com/us/pricing](https://www.buildxact.com/us/pricing/).
- Buildertrend estimating complaints: complicated, rigid line-item grouping, struggles with many lines, learning curve, cost for small firms (paraphrased extract) — [WS] [Capterra Buildertrend reviews](https://www.capterra.com/p/70092/Buildertrend/reviews/).
- Cost data locality is a selling point competitors make: Handoff claims AI "trained on 68 million construction costs" updated "on a daily basis for every single city in the US" — [Repo] [handoff.ai](https://handoff.ai/); [Handoff help](https://help.handoff.ai/en/articles/9778395-how-do-i-get-local-pricing-in-my-estimates).
- Buyers' AI concern is accuracy (57%) — [Repo] [Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/).

### Inferences
| Alternative | Why it persists | What it fails to satisfy |
|---|---|---|
| Gut-feel $/sq ft | Fast, homeowner-friendly | Hides scope differences; fails on custom/high-finish jobs and on remodels |
| Excel + own cost book | Free, owner controls it | Manual takeoff; stale prices; hard to make professional proposals |
| Cost-plus contracts | Shifts price risk to owner | Homeowners increasingly want a fixed number; still needs a budget estimate |
| Sub/supplier quotes rolled up | Real prices | Late, gappy quotes; no like-for-like comparison (bid leveling) |
| PM suite estimating (Buildertrend, JobTread, Houzz Pro, CoConstruct legacy) | Already paid for | Complex, rigid, no or weak plan takeoff; price climbs |
| Residential estimators (Handoff, Buildxact, Clear Estimates, Joist) | Built for residential | Plan takeoff paywalled/capped (Handoff Scale; Buildxact Master/add-on) or absent; Joist/Clear Estimates evidence not gathered |
| Outsourced estimators | No learning curve | Turnaround and cost per job unknown to buyer (Quotr Service price is published) |

**Unmet needs ranked (evidence emphasis; label: rank is the researcher's reading of search summaries and prior tests, n not counted)**
1. Estimating inside PM suites is too complicated/rigid (Capterra summary calls estimating "the most common target"; quote #4).
2. PM-suite price too high for small firms / price hikes (quotes #1–3).
3. Plan-based takeoff missing, paywalled or capped in residential tools (Handoff Scale ≤5,000 sq ft; Buildxact add-on).
4. Learning curve/setup time (Capterra summary).
5. Distrust of AI accuracy (57%; "hit-or-miss").
6. Cost data not local or not current during tariff/lumber swings (AGC 40% raised bids; Handoff's daily-cost claim shows the need).
7. Mac/browser access (r/estimators thread).
8. Finish-material cost and lead time (cabinets, windows) not handled by any estimating tool except domestic dealer links (Buildxact Home Depot ordering; Handoff Lowe's per search summary) — [Repo].

### Gaps
- No 1–3-star review mining of Houzz Pro, Handoff, Clear Estimates, Joist (G2/Capterra/App Store blocked). Needed for a true frequency rank.

---

## I. Willingness to pay, price anchors, who pays, sales cycle, trial behavior

### Takeaway
The buyer pays out of pocket, compares against $1,600–$4,000/year construction-software budgets and against residential anchors from $0 (Buildxact Go) to $899/month (Handoff Scale). Quotr Lite ($79.90/seat) undercuts every plan-takeoff option for a 1–2-person firm; Quotr Service at $0.25/sq ft prices a 2,500 sq ft custom home estimate at ~$625 — roughly the value of the 10+ owner-hours a bid takes.

### Cited Findings
| Product | Price (as last verified) | Plan takeoff? | Source |
|---|---|---|---|
| **Quotr Lite** | $79.90/seat/mo; 7-day trial, cancel anytime | AI takeoff (Lite: "basic AI agent", symbol/area detection, custom database) | [Repo] [quotr.ai/pricing](https://quotr.ai/pricing/), [/software](https://quotr.ai/software/) |
| **Quotr Plus** | $299.90/seat/mo; incl. 10% off procurement, 2,000 sq ft takeoff credits/mo (meaning TO CONFIRM) | Advanced AI, full Quotr database | [Repo] same |
| **Quotr Service** | $0.25/sq ft <50,000 sq ft; $0.10/sq ft above; price sent before processing | Done-for-you | [Repo] [quotr.ai/pricing](https://quotr.ai/pricing/) |
| Handoff | Flex $119/$149; Pro $239/$299 (12-mo); Scale $719/$899 per company/mo; 7-day trial | Only Scale, ≤5,000 sq ft | [Repo] [handoff.ai/pricing](https://www.handoff.ai/pricing) |
| Buildxact | Go $0; Foundation $169/$199; Pro $339/$399; Master $509/$599; unlimited users; 14-day trial | Digital takeoff on Foundation; AI Takeoff Assistant add-on/Master | [Repo] [buildxact.com/us/pricing](https://www.buildxact.com/us/pricing/) |
| JobTread | "$50 to $75 per user per month" (per competitor Projul) | Not established | [WS] [Projul best JobTread alternatives](https://projul.com/blog/best-jobtread-alternatives) |
| Buildertrend | Final cost "requires a company quote" (per search extract); reviewers report price rises ("about to triple") | Not established | [WS] [Capterra](https://www.capterra.com/compare/70092-218503/Buildertrend-vs-JobTread) |
| Typical construction software budget | ~$1,600–$4,000/yr | — | [Repo] [Capterra buyer insight](https://www.capterra.com/resources/construction-software-buyer-insight/) |

- Quotr ROI calculator default assumes $65/hour estimator time and an 80% takeoff-time cut ("illustrative") — [Repo] [quotr.ai/roi-calculator](https://quotr.ai/roi-calculator/).
- Retired Quotr prices ("Solo $299.90/month", etc.) still appear on ~13 Quotr URLs and llms.txt, making Quotr look ~4× more expensive than Lite — [Repo] product-and-features.md §2.

### Inferences
- Annual arithmetic (researcher): Quotr Lite 1 seat = **$959/yr**, 2 seats = $1,918; Buildxact Foundation = $2,030/yr (annual billing, unlimited users); Handoff Flex = $1,428/yr (no plan takeoff); Handoff Scale = **$8,628/yr** (plan takeoff). For a 1–3-person builder Quotr Lite is the cheapest plan-takeoff option found; for 6+ users Buildxact's unlimited-user model can be cheaper — say so on comparison pages.
- Service arithmetic: 1,000 sq ft ADU ≈ $250; 2,500 sq ft custom home ≈ $625; 5,000 sq ft ≈ $1,250. Against JLC's ">10 hours per bid" at Quotr's own $65/h default that is $650+ of owner time per bid — a strong, honest anchor for the "office manager quit / homeowner needs a number this week" triggers. Minimum order size unknown (TO CONFIRM).
- Who pays: owner, on a card, monthly — **likely**; spouse/bookkeeper approval — **speculative**.
- Sales cycle: hot triggers → trial within days; PM-suite replacement → months around renewal (likely). Trial behavior (one real job during a 7-day trial) is **speculative**; a 7-day trial may be too short for builders who bid a few jobs a month — test a "first estimate done for you" onboarding.

### Gaps
- Houzz Pro, Clear Estimates, Joist and JobTread official pricing pages not read (blocked). Buildertrend public price tiers not confirmed.
- No data on trial-to-paid rates or annual-plan uptake for this ICP.

---

## J. Vocabulary list

### Takeaway
Use the builder's words in titles and first sentences; engines inject them into sub-queries. Pricing words (cost-plus, fixed bid, allowances, change orders, markup vs margin) and plan words (takeoff, SF/LF/EA, plan set) matter most.

### Cited Findings
- General estimating terms seen in threads: takeoff, unit cost, labor units, assemblies, overhead, profit, markup vs margin, contingency, allowance, plug number, inclusions/exclusions, scope gap, bid leveling, RFI, addendum, change order — [Repo] buyer-questions-by-trade.md §15.
- Cabinets: LF of uppers/bases, RTA vs assembled vs custom, fillers/panels/crown; compliance CARB Phase 2/TSCA Title VI, ANSI/KCMA A161.1 — [Repo] §10.
- Import terms: DDP, FOB, EXW, landed cost, HTS code, Section 232, Section 301, AD/CVD, ISF (10+2), lead time, NFRC, cUPC — [Repo] §16.
- Remodel pricing: fixed price for known scope + cost-plus allowances; T&M — [WS] [Projul](https://projul.com/blog/how-to-price-remodel-job); Fine Homebuilding forum threads.

### Inferences
| Group | Terms (owner vocabulary) |
|---|---|
| Contract/pricing | fixed bid, lump sum, cost-plus (fee %), T&M, GMP (rare at this size), allowances, selections, change order, escalation clause, deposit/draw schedule, retainage (rare residential) |
| Margin | markup vs margin, overhead & profit (O&P), "10 and 10", contingency, gross profit, job costing |
| Plans | plan set, architect plans, my sketch, PDF plans, takeoff, SF/LF/EA/CY, "per square foot", "per opening" (electrical), conditioned vs gross sq ft |
| Job types | custom home, spec home, ADU, addition, kitchen/bath remodel, whole-house remodel, design-build, rebuild (fire) |
| Workflow | bid, proposal, estimate vs quote, ballpark/budget number, "free estimate", paid estimate/design agreement, sub quotes, supplier quote, lumber package, buyout |
| Materials | lumber package, windows & doors, cabinets, flooring, fixtures, finish schedule, lead time, tariffs |
| Tools named | Buildertrend, CoConstruct, JobTread, Houzz Pro, Buildxact, Handoff, Clear Estimates, Joist, Excel, QuickBooks |

### Gaps
- Regional vocabulary (e.g., Texas "spec builder" vs California "ADU") not validated with interviews.

---

## K. Channels

### Takeaway
They read and ask in trade forums and press (ContractorTalk, Fine Homebuilding, JLC, Pro Builder, Pro Remodeler, Remodelers Advantage), Reddit (r/Contractor, r/Construction, r/estimators, r/HomeBuilding), YouTube how-tos, Facebook groups (including vendor-run ones like "Handoff Nation"), associations (NAHB/local HBAs such as BIA Bay Area, NARI) and shows (IBS, KBIS, PCBC). Member counts could not be retrieved.

### Cited Findings
- Search-visible communities for this ICP's questions: ContractorTalk, Fine Homebuilding forum, JLC, Mike Holt forum, BiggerPockets, Houzz discussions, r/Contractor (mirror), r/Construction, r/estimators — [WS] retrieval runs R1/R4 (section O); [Repo] buyer-questions-by-trade.md.
- r/estimators appeared in the sources of 6 of 32 test prompts (Perplexity, 2026-09-25) — [Repo] presence-scorecard.md.
- Handoff runs a "Handoff Nation" Facebook group, webinars, a contractor course, and pays ambassadors for content — [Repo] [Handoff Nation](https://www.facebook.com/groups/820048150161667/); [handoff.ai/affiliates](https://www.handoff.ai/affiliates).
- Buildxact runs an official Reddit account and a YouTube channel — [Repo] [u/Buildxact-JobDone](https://www.reddit.com/user/Buildxact-JobDone/); [@buildxactusa](https://www.youtube.com/@buildxactusa).
- Trade press syndicates research: NARI republishes JCHS LIRA; Pro Remodeler, Inman, Hardwood Floors, Tile Letter carried the LIRA — [WS] [NARI](https://nari.org/nari-blog-main/remodeling-spending-slowdown/); [Pro Remodeler](https://proremodeler.com/news/news/55375552/remodeling-growth-to-slow-sharply-in-early-2027).
- Houzz's own research is syndicated by Kitchen & Bath Design News, Floor Daily, Stone World, Tile Letter — [WS] section O run R6.
- Events: IBS, PCBC, Dallas Build Expo (Quotr attended 2026) — [Repo] partnerships-and-marketplaces.md. Podcast: The Preconstruction Podcast — [Repo] listicle-and-pr-outreach.md.
- AI usage: ChatGPT 44% of US adults, Gemini 24% (Pew, Feb 2026) — [FW]; 52% of construction firms use AI tools (Houzz 2026) — [Repo].

### Inferences
- Engines to track for this ICP: ChatGPT and Google AI Overviews/AI Mode (largest reach); Perplexity as the prior-audit baseline; skip Claude/Copilot/Grok ([FW] engine guidance).
- YouTube and Reddit carry outsized weight on Google surfaces ([FW]); for this ICP YouTube how-to ("estimate a custom home from plans") is likely the highest-leverage owned video format.

### Gaps
- Subreddit member counts (r/Contractor, r/HomeBuilding, r/Construction, r/Carpentry, r/estimators), Facebook group sizes, YouTube creator names/subscriber counts (contractor-business creators), podcast list — Reddit and YouTube unreachable and search budget exhausted.

---

## L. Proof required at each stage

### Takeaway
Early stages need credible free answers (numbers, worked examples); deciding needs residential-specific proof (plans like mine, accuracy check, real price, reviews), and the Procurement cross-sell needs certification, landed-cost and lead-time proof.

### Cited Findings
- 86% of shoppers who used AI for research verified elsewhere; trust in AI alone falls to 5% over $500 — [FW] (MarTech).
- Quotr has ~0 G2 reviews and no Capterra listing; AI engines borrow the unrelated "Quotr Pro" app's 4.7 rating for "Is Quotr legit?" — [Repo] offsite-presence.md.
- Buildxact uses a Capterra/Software Advice "Top Home Builder Solution 2026" award as content; Capterra 4.6 from ~174 reviews — [Repo] buildxact.md.
- Procurement proof today: three Bay Area project cards; "40–55% average cost reduction" claim conflicts with "up to 50%"; display bug "Client saved ~$0" — [Repo] product-and-features.md §3.11.

### Inferences
| Stage | Proof the buyer needs | Quotr has today | Gap to close |
|---|---|---|---|
| First thought | A clear explanation + a number (e.g., markup vs margin table, $/sq ft range) | Little residential content | Answer pages with sourced numbers |
| Passive looking | Peer stories, "how others estimate custom homes" | None residential | One residential case study; YouTube walkthrough |
| Active looking | Category lists that include Quotr; residential feature fit (plan sizes, ADU/custom/remodel) | Absent from C2/C13/N5 answers | Residential hub; directory listings; listicle inclusion |
| Deciding | Fair vs pages; real price; accuracy check method; reviews from builders | Lite price exists but stale prices persist on ~13 URLs | Fix pricing; publish accuracy test; 10–20 Capterra/G2 reviews |
| Trial | First estimate done fast on own plans | Service exists | "First residential estimate done for you" offer (TO CONFIRM) |
| Procurement cross-sell | Certifications (NFRC, CARB, cUPC), landed cost incl. 232 + AD/CVD, lead time (~90 days, TO CONFIRM), warranty/damage | Project cards only | Certification FAQ, tariff explainer, landed-cost calculator |

### Gaps
- Quotr's own residential accuracy data and residential customer list (TO CONFIRM with Quotr).

---

## M. Coding chains (trigger → stage → mode → restraining force → exact prompt → proof)

### Takeaway
Seven chains cover the ICP; the strongest content opportunities are chains 1, 3, 5 and 7, where no software vendor yet owns the answer or where Quotr's Service/Procurement are uniquely relevant. All prompts are **researcher-written** from the evidence (no interview verbatims available).

### Cited Findings
- Chain method and stage/mode definitions — [FW].
- Evidence anchoring each chain: quotes #1–14 (section E), JLC >10 h per bid (A), cabinet 232 Jan 1 2027 (F), Handoff/Buildxact takeoff paywalls (H).

### Inferences
| # | Trigger (datable?) | Stage | Mode | Dominant restraining force | Exact prompt (SIMULATED wording) | Proof required |
|---|---|---|---|---|---|---|
| M1 | Lost money on an underpriced remodel (private; any month) | First thought → passive | Hot, evening | Habit ("I just need to be more careful in Excel") | "I'm a remodeler with 6 guys in Raleigh and I just lost about $25k on a kitchen and addition because I missed framing and electrical scope. How do contractors make sure their estimates from plans don't miss stuff?" | Step-by-step scope checklist; markup vs margin table; "how AI takeoff counts from plans and how to check it" |
| M2 | Homeowner wants a number this week (private; peaks Mar–May) | Active | Hot, time-pressured | Anxiety (accuracy) | "Homeowner needs a price by Friday on a 2,800 sq ft custom home from architect PDFs. Is there a service or software that can do the takeoff and give me a ballpark in a day or two?" | Turnaround time; published $/sq ft price ($0.25/sq ft); sample residential deliverable |
| M3 | Too many free estimates for tire-kickers (seasonal; JLC theme) | Passive | Cold (weekend) | Habit ("everyone gives free estimates") | "Should I start charging for estimates as a small remodeler? I'm spending 10+ hours on bids for people who never sign." | Data on time per bid; paid-estimate scripts; fast ballpark tool to qualify leads |
| M4 | PM-suite price hike or CoConstruct migration (renewal date) | Active → deciding | Considered | Habit (sunk setup) + anxiety (learning curve) | "Buildertrend is raising my price and their estimating is too complicated. I'm a 4-person custom builder in San Jose — should I switch to JobTread or keep Buildertrend and add a separate estimating tool that does takeoffs from PDFs?" | Side-by-side table incl. per-seat vs per-company math; "works alongside your PM tool" integration facts |
| M5 | Lumber/tariff swing between bid and buyout; cabinet 232 → 50% on Jan 1 2027 (datable) | Active | Hot near deadline | Anxiety (import quality/lead time) | "Cabinet tariffs go to 50% on January 1. I have three custom homes starting in spring with cabinet allowances of $40–60k each — should I lock in cabinets now and are factory-direct cabinets from China worth it after duties?" | Dated tariff explainer with Federal Register links; landed-cost math incl. AD/CVD; lead time; certifications; Quotr Procurement project cards |
| M6 | Office manager/estimator quits (private) | Active | Hot | Anxiety (quality of outsourced work) | "My estimator just quit and I have 5 bids due this month for home additions in Austin. What does outsourced residential estimating cost and is it any good?" | $/sq ft price; turnaround; sample; who checks the numbers; editable output in software |
| M7 | Winter planning / New Year (Dec–Jan, datable) | Passive → active | Cold, considered | Habit | "It's January and I want to stop estimating in Excel this year. I'm a small residential GC in Charlotte doing 6–8 custom homes a year — what's the best estimating software that does takeoff from plans, and what does it really cost?" | Fair comparison incl. prices; trial terms; residential case study |
| M8 | Deciding between finalists (any) | Deciding | Considered | Anxiety (brand legitimacy) | "Quotr vs Handoff for a custom home builder — which is better for takeoffs from architect plans and what do they cost?" | Fair vs page on quotr.ai; consistent facts across G2/Capterra/LinkedIn; reviews |

### Gaps
- Frequency of each chain unknown; promote chains to the backlog only after ≥3 of 12 interviews or ≥5 of 50 community posts match ([FW] threshold).

---

## N. Prompt matrix

### Takeaway
12 full-context prompts carry persona facts (builder type, size, city/state, current tools); 6 short category prompts and 3 brand prompts are kept separate because brand prompts mention the brand ~92% of the time and would swamp averages ([FW] Momentic/Peec). Demand tiers are **labeled estimates**.

### Cited Findings
- Ask-for-a-pick prompts: 22.8% brand-recommendation rate vs 8.0% for topic-only; comparative prompts 43.3% mention rate vs 18% informational; ChatGPT fan-out injects "best" (15.3%), "reviews" (6.8%), "2026", "vs", "price"; persona facts change which brands are named — [FW].
- Baselines from Quotr's prior Perplexity tests: C2, C13, C14, N5, S1, S4 all **Absent** — [Repo] quotr_ai_visibility_tests.md; tracking-set.md.

### Inferences
**Full-context first-person prompts (persona facts are SIMULATED)**

| ID | Prompt | Intent | Stage | Urgency | Mode | Engine | Expected fan-out nodes | Demand tier (est.) |
|---|---|---|---|---|---|---|---|---|
| F1 | "I run a 4-person custom home building company in San Jose, CA. I use Buildertrend for scheduling but do estimates in Excel from the architect's PDFs. What software can do the takeoff from the plans and build the estimate, and what does it cost?" | choose-provider | Active | Exploratory | Cold | ChatGPT, AI Mode | best residential estimating software 2026; takeoff software home builders; Buildertrend estimating; Handoff pricing; Buildxact pricing; reviews | 4 |
| F2 | "I'm a remodeler in Raleigh with 6 employees. I just lost money on a kitchen + addition because I missed scope. How do I make my estimates from plans more accurate?" | diagnose/learn → do | First thought | Acute | Hot | ChatGPT | how to estimate a remodel from plans; estimating checklist; common estimating mistakes contractors; markup vs margin | 4 |
| F3 | "Homeowner wants a number by Friday on a 2,800 sq ft custom home in Austin, TX. I have the plan set as PDFs. Is there a service that does residential takeoffs and estimates in 24–48 hours, and what does it cost?" | choose-provider | Active | Acute | Hot | ChatGPT, AIO | outsourced construction estimating service cost per square foot; residential takeoff service; turnaround | 3 |
| F4 | "Small residential GC in Charlotte, 8 employees, 6–8 custom homes a year. Buildertrend vs JobTread vs a dedicated estimating tool — which is better for estimating from plans?" | compare | Active | Exploratory | Cold | ChatGPT, AI Mode | Buildertrend vs JobTread 2026; JobTread estimating; best estimating software small builders; reviews | 3 |
| F5 | "We were on CoConstruct and got moved to Buildertrend. I'm a design-build remodeler in Seattle with 10 people. Their estimating is too complicated. What are good alternatives just for estimating?" | compare/alternatives | Active | Recurring (renewal) | Considered | ChatGPT | CoConstruct alternatives; Buildertrend estimating alternatives; Buildertrend reviews; best remodeler estimating software | 2 |
| F6 | "I build ADUs in Los Angeles (3 of us) and use Houzz Pro. Fire rebuild clients need a budget fast for insurance. What's the cost per square foot to rebuild in Altadena/Palisades in 2026 and what tool can do takeoffs from plans?" | learn + choose | Active | Acute | Hot | AIO, ChatGPT | LA fire rebuild cost per square foot 2026; ADU cost Los Angeles; Houzz Pro takeoff; residential takeoff software | 3 |
| F7 | "Custom home builder in the Bay Area. Cabinet tariffs go to 50% on Jan 1. I have three homes starting in spring with $40–60k cabinet allowances. Should I buy now, and are factory-direct cabinets from China worth it after duties?" | validate/do | Active | Acute (dated) | Hot | ChatGPT, AIO | section 232 cabinet tariff 2027; AD/CVD wooden cabinets China; factory direct cabinets for builders; landed cost | 3 (rising to 4 in Dec) |
| F8 | "I'm a remodeler in Boston with 5 employees and I'm drowning in free estimates for people who don't hire me. Should I charge for estimates, and is there a faster way to give a ballpark from photos or plans?" | diagnose/learn | Passive | Recurring | Cold | ChatGPT | should contractors charge for estimates; paid estimate design agreement; ballpark estimate tool | 3 |
| F9 | "Our office manager who did all our estimates in Clear Estimates just quit. We're a 7-person remodeling company in Atlanta. Do I hire an estimator, outsource, or switch to AI estimating software?" | compare | Active | Acute | Hot | ChatGPT | hire vs outsource estimator cost; estimating services residential; Clear Estimates alternatives; AI estimating software | 2 |
| F10 | "Houston custom builder, 15 employees, ~20 homes a year. Lumber and tariffs keep moving between bid and buyout. How should I handle escalation in fixed-price contracts, and what software keeps material prices current?" | learn + choose | Active | Recurring | Considered | ChatGPT, AI Mode | escalation clause residential construction; lumber prices 2026; estimating software real-time material prices | 3 |
| F11 | "I'm a one-man remodeler in Phoenix using Joist for quotes. Work slowed down this year. Is there affordable software that does takeoffs from plans so I can bid bigger jobs from GCs and architects?" | choose-provider | Active | Exploratory | Cold | ChatGPT | cheap takeoff software; Joist alternatives; residential takeoff software price; free trial | 2 |
| F12 | "Bay Area builder, 5 people, choosing between Handoff and Quotr for AI takeoff from architect plans plus buying finishes. Which is better and what's the real monthly cost for 2 users?" | compare | Deciding | Exploratory | Considered | ChatGPT, Perplexity | Handoff vs Quotr; Handoff pricing 2026; Quotr pricing; reviews; AI takeoff residential accuracy | 1 |

**Short category prompts**

| ID | Prompt | Intent | Stage | Expected fan-out | Prior baseline | Demand tier (est.) |
|---|---|---|---|---|---|---|
| S1 | best construction estimating software for residential contractors | choose | Active | best 2026, reviews, residential | C2 Absent (Clear Estimates, Buildxact, Houzz Pro, Buildertrend, JobTread, QuickBooks) | 4 |
| S2 | AI estimating software for home builders from plans | choose | Active | AI takeoff residential, plans to proposal | C13 Absent (Handoff, BuildVision, Houzz Pro, Buildxact, Beam) | 3 |
| S3 | how much does it cost to build a house per square foot in California 2026 | learn | Passive | $/sq ft by region, 2026 | Not tested | 5 |
| S4 | how to estimate a remodel from plans | learn/do | First thought | step-by-step, checklist | Not tested | 4 |
| S5 | markup vs margin for contractors | learn | First thought | calculator, table | Not tested (answers cite Procore, JobTread, Projul, Groundplan per prior Perplexity note) | 4 |
| S6 | where can home builders buy cabinets and windows factory direct | choose | Active | factory direct, wholesale, builders | C14 Absent (Build Source etc.) | 2 |

**Brand prompts (track separately)**

| ID | Prompt | Stage | Expected fan-out | Demand tier (est.) |
|---|---|---|---|---|
| B1 | Quotr vs Handoff for residential builders | Deciding | Handoff pricing, Quotr pricing, reviews, official | 1 |
| B2 | Quotr vs Buildxact | Deciding | Buildxact pricing, Capterra, reviews | 1 |
| B3 | Is Quotr legit? Quotr reviews for home builders | Deciding | G2, Capterra, App Store (risk: "Quotr Pro" confusion) | 1 |

Tier method (labeled estimate): 5 = consumer + pro volume (cost per sq ft); 4 = high-frequency pro how-to or category list; 3 = specific but recurring pro situation; 2 = niche situation; 1 = brand/decision prompts (low volume, high value). No GSC/Keyword Planner/Profound volumes were available.

### Gaps
- No live baseline for F1–F12 in ChatGPT/AI Mode; run 3–5 times each before using as KPIs.

---

## O. Simulation of the AI search journey

### Takeaway
SIMULATED conversation: a Bay Area custom builder moves from a money-losing job to a shortlist in five turns; on current evidence the shortlist would be Handoff, Buildxact, Buildertrend/JobTread and Clear Estimates/Houzz Pro, with Quotr absent. Retrieval-proxy runs show the sub-query layer is owned by review directories, vendor "vs"/how-to pages, trade press and consumer cost guides — no Quotr page appeared in any of eight runs.

### Cited Findings
**(1) SIMULATED 5-turn ChatGPT conversation — NOT a real transcript. Assistant turns are predictions built from the prior Perplexity answers (2026-09-25) and the retrieval-proxy runs below.**

| Turn | User (persona: "Dan", owner, 5-person custom home + remodel firm, San Mateo County CA; Buildertrend for PM, Excel for estimates — SIMULATED) | Predicted assistant behaviour (SIMULATED) | Likely fan-out sub-queries |
|---|---|---|---|
| 1 | "I underbid a whole-house remodel by about $40k — missed scope in framing and electrical. How do builders avoid that when pricing from architect plans?" | Generic advice: line-item takeoff, scope checklist, contingency 5–10%, markup vs margin, fixed + allowances; may mention "estimating software such as Buildertrend, Buildxact, Clear Estimates" | how to avoid underbidding construction; estimating checklist remodel; markup vs margin |
| 2 | "Is there software that does the takeoff from the PDFs for me? I don't want another huge system — I already pay for Buildertrend." | Lists AI/residential estimating tools; Handoff likely first (owns "residential" + "plans to proposal"), Buildxact, Houzz Pro, Togal/STACK for takeoff | best AI takeoff software residential 2026; Handoff takeoff; Buildxact takeoff |
| 3 | "What do those cost for 2 users, and which ones actually do takeoff from plans and not just estimates?" | Price table: Handoff Flex/Pro/Scale (takeoff only on Scale), Buildxact Foundation/Pro/Master (AI takeoff add-on), STACK; may be inaccurate on Buildertrend (quote-only) | Handoff pricing 2026; Buildxact pricing; STACK pricing |
| 4 | "Will AI takeoff be accurate on a custom home with weird rooflines? And are the costs local to the Bay Area?" | Caveats on accuracy; cites vendor accuracy claims (Togal 98%, STACK ~3%), Handoff "local pricing daily"; suggests verifying with a manual check | AI takeoff accuracy residential; Handoff local pricing; reviews |
| 5 | "Give me a shortlist of 3 for a 5-person Bay Area builder, and is there anything that also helps on cabinets and windows costs with these tariffs?" | Shortlist likely Handoff, Buildxact, Buildertrend (or JobTread); for materials: Buildxact dealer/Home Depot ordering, Handoff supplier/Lowe's, local dealers; factory-direct answers name sourcing companies, not software | best estimating software with material ordering; factory direct cabinets for builders; tariffs cabinets 2027 |

**(2) Retrieval proxy — WebSearch runs, 2026-11-06 ("retrieval proxy, not an AI engine answer")**

| Run | Fan-out node it stands in for | Query as run | Top domains returned | Brands named | Quotr? | Winning format |
|---|---|---|---|---|---|---|
| R1 | "how to price a remodel / avoid underbidding" | reddit r/Contractor underbid job lost money estimate how do you price remodel | projul.com, forums.mikeholt.com, Reddit mirror of r/Contractor, stackct.com, finehomebuilding.com (×4), electrical-contractor.net, jlconline.com, **handoff.ai** (remodeling pricing guide), biggerpockets.com, tradewebsites/builtright blogs | Projul, STACK, Handoff | No | Vendor pricing how-to with formula + old forum threads |
| R2 | "Buildertrend vs JobTread / Buildertrend alternatives" | reddit Buildertrend estimating too expensive switched JobTread small builder | capterra.com (JobTread reviews pp.1–5; Buildertrend pp.3, 8; compare), jobtread.com (vs Buildertrend; leaving CoConstruct; why losing money), getapp.com (Buildertrend vs JobTread for remodelers), projul.com, g2.com compare, ingenious.build, personal blog | Buildertrend, JobTread, CoConstruct, Jobber, Projul | No | Review-directory pages + vendor "vs" pages |
| R3 | "Buildertrend reviews estimating" | Buildertrend reviews estimating too complicated expensive small builder (capterra.com only) | Capterra Buildertrend review pages (1, 5, 7, 8, 16, 20, 37, 41), Buildertrend vs Buildxact, Buildertrend vs BuildBook | Buildertrend, Buildxact, BuildBook | n/a (domain-restricted) | Review pages (directories are the proof layer) |
| R4 | "how long should an estimate take / should I charge for estimates" | NAHB remodelers survey estimating time how many hours per estimate small remodeler free estimates | jlconline.com (×8), remodelersadvantage.com, proremodeler.com, finehomebuilding.com forum (×2), consultant blog | None (Remodelers Advantage = consultancy) | No | Trade-press reader survey + opinion columns — **no software vendor present** |
| R5 | "cost to build a house per square foot 2026" | NAHB 2026 construction cost survey share of sales price per square foot cost new home | homelight.com, nowbam.com (HBA), costtobuildahouse.com, nahb.org, alphanews.org, lbmjournal.com, corridorbusiness.com, aol.com, e2value.com, probuilder.com, opendoor.com | None | No | NAHB survey restated by consumer cost guides and local HBAs |
| R6 | "do remodelers use estimating software / industry data" | Houzz State of the Industry 2026 residential renovation businesses survey findings software estimating | houzz.com (research hub ×7), st.hzcdn.com PDF, kitchenbathdesign.com, floordaily.net, stoneworld.com, uslightingtrends.com, tileletter.com, kbbfocus.com, jbiznews.com | Houzz (Houzz Pro) | No | **Vendor-owned original survey syndicated by trade press** |
| R7 | "remodeling market outlook 2027" (planning context) | JCHS LIRA October 2026 remodeling spending forecast 2027 | jchs.harvard.edu (×4), woodworkingnetwork.com, nari.org, woodshopnews.com, inman.com, proremodeler.com, hardwoodfloorsmag.com, tileletter.com, lbmjournal.com, ctasc.com | None | No | Institutional forecast syndicated by associations/trade press |
| R8 | "where are homes being built 2025–2026" (geo context) | 2025 single-family permits top metro areas Houston Dallas Atlanta Phoenix Charlotte permits ranking | credaily.com, globest.com (×5), nahb.org, nar.realtor, electricalmarketing.com, builderonline.com, constructionowners.com, kvia.com | None | No | Data news posts restating NAHB/Census |

Planned fan-out runs **not executed** (search budget exhausted): "best estimating software for custom home builders 2026", "Handoff vs Buildxact", "cost to build a house per square foot Bay Area 2026", "kitchen cabinet tariff January 2027 builders", "should contractors charge for estimates", "fixed price vs cost plus custom home", "Clear Estimates alternatives", "Houzz Pro takeoff review".

**Actual AI-engine answers from Quotr's prior audit (Perplexity Sonar, 2026-09-25) — [Repo] quotr_ai_visibility_tests.md, competitor_geo_benchmark.md, tracking-set.md**
| Prompt | Brands named | Key sources | Quotr |
|---|---|---|---|
| C2 best construction estimating software for residential contractors | Clear Estimates, Buildxact, Houzz Pro, Buildertrend, JobTread, QuickBooks | Workyard, Capterra analysis, ConstructionCoverage, buildxact, buildertrend, pro.houzz | Absent |
| C13 AI estimating software for residential GCs, plans to proposal | Handoff, BuildVision AI, Houzz Pro, Buildxact, Beam (trybeam) | handoff.ai ×4, sourceforge, constructionplacements | Absent |
| S1 best AI takeoff + estimating 2026 for residential subs and GCs | Handoff (remodelers/subs), Handoff or Buildxact (small GC), STACK, Togal | Handoff's own "6 best" listicle (1st citation) | Absent |
| S4 residential bid leveling | Buildertrend, Buildxact, SmartBid, Procore, Contractor Foreman | worldmetrics, softwareconnect | Absent |
| N5 Handoff alternatives for residential contractors | Foreman, SimplyWise, Houzz Pro, Buildertrend, Buildxact, JobTread, Jobber, Contractor Foreman | SimplyWise, Foreman, SourceForge, GetApp, G2, Capterra alternatives pages | Absent |
| C14 buy cabinets, windows, flooring factory direct | Build Source, Platinum Direct, Floor Daddy Depot, Shop At Home Cabinets, others | supplier sites, houzz | Absent |

### Inferences — (3) gap verdict per prompt cluster
| Cluster | Who owns it now | Quotr gap | Winnability (est.) | Move |
|---|---|---|---|---|
| Residential software choice (S1, S2, F1, F4) | Handoff, Buildxact, Buildertrend, JobTread, Houzz Pro, Clear Estimates via directories + vendor listicles | Total absence | Medium-hard | Residential hub + Capterra/G2 listing and reviews + listicle inclusion (Workyard, ConstructionCoverage, GetApp category) |
| PM-suite switching (F5, F9, R2, R3) | JobTread/Projul vs pages + Capterra | Absent; but no one owns "keep your PM tool, add estimating" | **Medium-easy** | Neutral decision page + "works with Buildertrend/JobTread" page |
| Pricing/underbid how-to (F2, S4, S5, R1) | Projul, Handoff, STACK guides + forums | Absent | Medium | Worked residential example + calculator, better than vendor guides |
| Estimate time / free estimates (F8, R4) | Trade press only | No vendor present | **Easy-medium** | Original time-per-estimate data + paid-estimate guide + Service as option |
| $/sq ft cost (S3, F6, R5) | NAHB restated by consumer guides; LA answers from Bloomberg/local GCs | Absent | Medium (CA metros) | Dated CA $/sq ft pages from Quotr data |
| Tariffs/finish materials (F7, S6, C14) | Government, law/logistics firms, suppliers | No software vendor | **Easy-medium (white space)** | Dated 232 cabinet explainer + landed-cost calculator + procurement proof |
| Outsourced estimating (F3, F9) | Estimating-service firms (prior P7, C12) | Quotr's service-pricing post already the first Perplexity citation for "outsourced estimating price per square foot" but brand not named | Medium-easy | Residential Service page with worked $/sq ft examples |
| Brand (B1–B3) | Quotr own pages + confusion with Quotr Pro | Entity confusion | Easy once pages exist | Fair vs pages; entity fact sheet consistency |

### Gaps
- Live ChatGPT/AI Mode runs not possible in this session; assistant turns above are predictions.

---

## P. GEO system for this ICP

### Takeaway
Build one residential hub, two California cost spokes, four decision pages, eight answer pages (urgent + considered versions) and three calculators; seed proof with a residential accuracy test, a Bay Area finish-materials price comparison and a time-per-estimate survey; get listed and reviewed on Capterra/G2 before chasing listicles; freeze 8 tracking prompts and report as distributions. Procurement is the cross-sell inside allowances/selections and the Jan 1 2027 cabinet tariff.

### Cited Findings
- One page per intent cluster; engines favour deep single-topic pages; product/pricing pages lead ChatGPT retrieval (16.4%); freshness: 75% of cited pages updated within a year, ~4.5-week citation half-life; self-ranked listicles risky (69% didn't get own brand recommended); schema and llms.txt not citation levers; Reddit 3–6-month play; measurement: 3–5 runs, cluster level, ±ranges, 3-period confirmation; 50 prompts daily → ±6.1 pts monthly — [FW].
- Handoff's kit: persona pages (/builders, /remodelers), 9 vs pages, dated listicle (first citation), cost-data hub, webinars, FB group, paid creators — [Repo] handoff.md.
- Quotr's existing assets to reuse: Service pricing post (first Perplexity citation for outsourced estimating price), procurement project cards, LA rebuild sample, zip-code cost database, ROI calculator, STACK/PlanSwift alternative posts — [Repo].
- Quotr pricing hygiene issue: ~13 URLs + llms.txt with retired $299.90 pricing — [Repo].

### Inferences
**1. Owning pages on quotr.ai (titles and slugs; U = urgent-mode, C = considered-mode)**

| Type | Title | Slug | Mode | Prompts served |
|---|---|---|---|---|
| Hub | AI Takeoff and Estimating for Home Builders and Remodelers: Plans → Estimate → Proposal → Finish Materials | /residential/ | C | S1, S2, F1, F4 |
| Persona spoke | Estimating Software for Custom Home Builders (from architect PDFs) | /residential/custom-home-builders/ | C | F1, F7, F12 |
| Persona spoke | Estimating Software for Remodelers: kitchen, bath, additions, whole-house | /residential/remodelers/ | C | F2, F5, F8 |
| Persona spoke | ADU Builders: takeoff and cost estimates for California ADUs | /residential/adu-builders/ | C | F6 |
| Service (U) | Need a Number This Week? Residential Takeoffs and Estimates from $0.25/sq ft | /service/residential-estimates/ | U | F3, F6, F9, M2, M6 |
| Cost hub | Cost to Build a House per Square Foot (2026–2027): national and California data | /residential/cost-per-square-foot/ | C | S3 |
| Cost spoke | Bay Area Custom Home and ADU Cost per Square Foot, dated quarterly | /residential/cost-per-square-foot/bay-area/ | C | S3, F1 |
| Cost spoke | LA Fire Rebuild Cost per Square Foot (Palisades, Altadena, Malibu) | /residential/cost-per-square-foot/la-fire-rebuild/ | U/C | F6 |
| Decision | Quotr vs Handoff for Residential Builders (fair, with prices) | /compare/quotr-vs-handoff/ | C | F12, B1 |
| Decision | Quotr vs Buildxact | /compare/quotr-vs-buildxact/ | C | B2 |
| Decision | Keep Buildertrend or JobTread for PM — Add Takeoff and Estimating Alongside It | /residential/use-with-buildertrend-jobtread/ | C | F4, F5, M4 |
| Decision | PM Suite vs Standalone Estimator vs Done-for-You: How Small Builders Should Choose (neutral, no self-ranking) | /residential/how-to-choose-estimating-software/ | C | S1, F1, F9 |
| Answer (U) | Underpriced a Job? 7 Estimate Fixes to Make Before Your Next Bid | /blog/underpriced-construction-job-fixes/ | U | F2, M1 |
| Answer (C) | How to Estimate a Custom Home from Architect Plans: worked 2,800 sq ft example | /blog/how-to-estimate-custom-home-from-plans/ | C | S4, F1 |
| Answer (C) | How to Estimate a Remodel from Plans (scope checklist + allowances) | /blog/how-to-estimate-remodel-from-plans/ | C | S4, F2 |
| Answer (C) | Markup vs Margin for Builders and Remodelers (table + calculator) | /blog/markup-vs-margin-builders/ | C | S5 |
| Answer (C) | Should You Charge for Estimates? Data on hours per bid and scripts that work | /blog/should-contractors-charge-for-estimates/ | C | F8, M3 |
| Answer (C) | Fixed Price vs Cost-Plus for Custom Homes and Remodels | /blog/fixed-price-vs-cost-plus-residential/ | C | F10 |
| Answer (U, dated) | Cabinet and Vanity Tariffs Rise to 50% on Jan 1, 2027: what builders should do now | /blog/cabinet-vanity-tariff-2027-builders/ | U | F7, M5 |
| Answer (C) | Escalation Clauses and Allowances: protecting fixed bids from lumber and tariff swings | /blog/escalation-clause-allowances-residential/ | C | F10 |
| Calculator | Markup/Margin Calculator for Contractors | /tools/markup-margin-calculator/ | U | S5 |
| Calculator | What Does a Free Estimate Cost You? (hours × rate × win rate) | /tools/estimate-cost-calculator/ | U | F8 |
| Calculator | Finish-Materials Landed-Cost Calculator (cabinets, windows, doors; incl. 232 + AD/CVD fields) | /tools/landed-cost-calculator/ | C | F7, S6 |

Page format rules (from [FW]): 40–60-word direct answer under each heading; one sourced statistic per ~150 words; tables near top; visible update date; named author with building/estimating credentials; plain server-rendered HTML; under 2,000 words for lists.

**2. Proof assets / original data (ranked by citation ceiling)**
1. **Residential takeoff accuracy test** — Quotr AI vs manual takeoff on 10–20 real single-family/ADU/remodel plan sets (SF, LF, EA by trade), with method page. Needs Quotr data (TO CONFIRM). Answers anxiety #1 (57% accuracy worry).
2. **"State of Residential Estimating 2027" survey** with BIA Bay Area / a NARI chapter: hours per estimate, % paid estimates, win rate, tools used. Fills the gap that only the JLC reader panel exists; model on Houzz's syndicated research (R6).
3. **Bay Area finish-materials price comparison** — factory-direct DDP vs local market from Quotr's three project cards, dated, with category breakdown (fix "Client saved ~$0" bug and the 40–55% vs "up to 50%" conflict first).
4. **Quarterly California $/sq ft index** from Quotr's zip-code database (TO CONFIRM how it is sourced and refreshed).
5. **One named residential case study** (custom home or ADU): time saved, estimate vs final cost.

**3. Off-site placements ranked by leverage per hour (estimate)**
| Rank | Placement | Why | Effort |
|---|---|---|---|
| 1 | Fix entity/pricing hygiene: retire $299.90 pricing on ~13 URLs + llms.txt; make /disambiguation/ say "residential builders and remodelers" | Engines repeat stale prices and commercial-only framing | 3–5 h |
| 2 | Capterra (feeds GetApp/Software Advice) + G2 listing under "residential construction estimating"; 10–20 reviews from residential users | C2 cites Capterra analysis; N5 cites GetApp/G2/Capterra alternatives; Buildxact wins with 174 Capterra reviews | 6–10 h + review asks |
| 3 | Pitch inclusion in pages engines already cite for residential prompts: Workyard residential estimating compare, ConstructionCoverage estimating, ConstructionPlacements AI estimating, Square Takeoff residential list, worldmetrics residential bidding | Thin comparison pools; 2–6 weeks per placement ([FW]) | 1–2 h each |
| 4 | One chaptered YouTube video: "Estimate a 2,800 sq ft custom home from architect PDFs" (+ Shorts) | YouTube heavily cited on Google surfaces ([FW]) | 6–8 h |
| 5 | BIA Bay Area / NARI chapter lunch-and-learn + co-branded survey (asset 2) | Local credibility; original data | 8–12 h |
| 6 | Trade press with data: Pro Builder, Pro Remodeler, JLC, Remodelers Advantage (time-per-estimate data; tariff explainer) | Trade press syndicates data widely (R6, R7) | 3–4 h per pitch |
| 7 | Disclosed founder participation in r/Contractor, r/HomeBuilding, r/estimators, ContractorTalk, Fine Homebuilding forum | 3–6-month play; trust channel | 1 h/week |
| 8 | IBS/KBIS 2027 presence (talk or meetings) | Cold-mode buyers browsing; event recap content | Variable |

**4. Refresh cadence**
- Monthly: comparison/pricing pages (Handoff, Buildxact, Buildertrend, JobTread prices), tariff page (through Jan 2027 and after), material-cost update.
- Quarterly: $/sq ft pages, hub, persona spokes, proof data.
- Event-driven: LIRA release (Jan 21, 2027), AGC monthly PPI, Federal Register tariff notices, competitor price changes.
- Before Jan 1 each year: all considered-mode pages refreshed for the New Year window.

**5. Tracking prompts to freeze (≥4 weeks, 3–5 runs each, ChatGPT + Google AI Mode/AIO; report cluster-level mention / citation / recommendation / share of voice vs Handoff, Buildxact, Buildertrend, JobTread, Houzz Pro, with ± ranges)**
| # | Prompt | Cluster | Baseline |
|---|---|---|---|
| T1 | best construction estimating software for residential contractors | Software choice | C2 Absent |
| T2 | AI estimating software for residential general contractors that goes from plans to proposal | Software choice | C13 Absent |
| T3 | Handoff alternatives for residential contractors | Alternatives | N5 Absent |
| T4 | F1 (San Jose custom builder, Buildertrend + Excel, takeoff from architect PDFs) | Full-context choice | Not run |
| T5 | F4 (Charlotte GC: Buildertrend vs JobTread vs dedicated estimating tool) | Switching | Not run |
| T6 | how much does it cost to build a house per square foot in the Bay Area 2026 | Cost | Not run |
| T7 | F7 (cabinet tariff Jan 1 2027, factory-direct cabinets worth it) | Tariff/procurement | Not run (N1 named no vendor) |
| T8 | Quotr vs Handoff for residential builders (brand group, reported separately) | Brand | Not run |

**6. Procurement cross-sell angle**
- Insert procurement where the builder already thinks about finishes: allowances and selections (cabinets, windows/doors, flooring, fixtures) in estimates; the Jan 1 2027 cabinet/vanity 232 step-up; landed-cost math. Plus plan's "10% off procurement" is the only published software↔procurement link — make it visible on residential pages.
- Honesty constraints: ~90-day delivery (TO CONFIRM) means Procurement fits considered/winter planning for spring starts, not "need it this week"; explain how DDP prices handle 232 and AD/CVD on Chinese wooden cabinets (TO CONFIRM); publish certifications (NFRC, CARB, cUPC) only once confirmed; reconcile factory counts (50+ vs 220+) and delivery area (CA vs nationwide).

**7. Do / skip / ignore**
- **Do:** residential hub + 3 persona spokes; urgent Service page with $/sq ft examples; fair vs pages (Handoff, Buildxact) and a "use alongside Buildertrend/JobTread" page; dated cabinet-tariff page before December; CA cost pages from own data; pricing hygiene; Capterra/G2 listing + residential reviews; one YouTube walkthrough; residential accuracy test; trigger-calendar refreshes; distribution-based measurement.
- **Skip:** self-ranked "best estimating software" listicle; 50-state or city-template cost pages; schema or llms.txt as citation levers (keep schema for entity clarity only); "Instructions for AI assistants" blocks; generic "thousands of builders" claims; paid placements before a baseline; fighting Handoff head-on for "remodelers" with no residential proof.
- **Ignore (for now):** Claude/Copilot/Grok tracking; prompt-volume counts as a decision variable; choice-overload arguments; Northeast/PNW geo pages until metro data exists.

### Gaps
- Quotr facts needed before publishing: residential plan-size limits, Lite vs Plus takeoff limits on residential sets, "takeoff credits" meaning, Service minimum order, residential customer proof, procurement lead time/categories/duty handling, BIA Bay Area membership status.

---

## Q. Known / likely / speculative

### Takeaway
Market size, margins, permits, competitor prices and current AI-answer ownership are known (with the [WS] caveat that pages were not opened); psychology and journey patterns are likely; persona prompts, demand tiers, chain frequencies and conversion behaviour are speculative until interviews and live runs.

### Cited Findings
- See sections A–P for every source.

### Inferences
| Claim class | Known (measured; cite with source) | Likely (strong inference; label it) | Speculative (validate first) |
|---|---|---|---|
| Size and economics | NAHB medians: builders 5 starts, 6 employees, $3.7M; remodelers 5 employees, $2.1M; builder margins 20.7%/8.7% (bottom quartile −1.4% net); remodelers 29.9%/6.3%; 33%/37% use estimating software (Houzz 2025); >10 h per bid for ~half (JLC panel) | ~60k 236115 establishments (aggregator, CBP 2023); 236115+236118 universe ~150–190k establishments | Share of owners who estimate personally; spouse-bookkeeper role |
| Geography | TX 140,002 permits (−11.7%); FL #2, NC #3; Houston/Dallas/Phoenix/Atlanta/Charlotte lead metros; LIRA $524B → $527B; LA rebuild $400–$800+/sq ft answers; Quotr's Bay Area procurement projects | CA hub + Bay Area/LA spokes justified; TX volume favours speed messaging | Northeast/PNW priority; Trends-based demand by DMA |
| Triggers | Cabinet/vanity 232 to 50% on Jan 1, 2027; AGC: 40% raised bids due to tariffs, input costs +8.9%; LIRA next release Jan 21, 2027 | New Year/winter planning and spring rush as prompt peaks; CoConstruct migration as a switch window | Exact seasonality curve for "estimating software" prompts |
| Forces and psychology | Review/forum wording on PM-suite price and estimating complexity (search extracts); AI accuracy is top worry (57%); free-estimate and late-night themes in trade press | Habit (Excel, PM suite) is the strongest restraining force; fear of underpricing > fear of losing bids | Time-of-day of prompts; trial behaviour; decision unit |
| AI answers | Quotr absent from C2, C13, S1, S4, N5, C14 (Perplexity, Sept 2026); Handoff/Buildxact own residential; directories, vendor vs pages, trade press and cost guides own the sub-query layer (retrieval proxy) | ChatGPT/AI Mode show similar ownership; "keep your PM tool" and "estimate time" clusters are uncontested | Persona facts (city, tools) shift brand lists for this ICP |
| Quotr fit | Lite $79.90/seat; Plus $299.90 with 10% off procurement; Service $0.25/$0.10 per sq ft; Procurement DDP finishes from China; cheapest plan-takeoff option for 1–3 users vs Handoff Scale/Buildxact Master (arithmetic) | Service $/sq ft ≈ value of owner's 10+ h per bid | Residential accuracy level; procurement fit for small builders' order sizes and timelines |

### Gaps
- All [WS] items need a direct page read before publication; network policy blocked nahb.org, eyeonhousing.org, capterra.com, reddit.com, jlconline.com and census.gov in this session.
- Interviews (6–12 recent switchers), live ChatGPT/AI Mode baselines and community member counts are the three missing evidence layers.
