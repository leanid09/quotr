# ICP 1 — The "kitchen-table" owner-estimator at a small MEP / low-voltage trade subcontractor (electrical, plumbing, HVAC, low-voltage, fire alarm; 3–30 employees)

*Prepared 2026-11-06 (US focus). Method: the uploaded ICP-depth GEO framework (trigger → stage → hot/cold mode → restraining force → prompt → proof; four forces; switch timeline; prompt matrix; geography-to-segment pipeline; distribution-based measurement) applied to this buyer, building on `geo-brain/00-quotr/audiences-and-personas.md` (Persona 1), `geo-brain/00-quotr/product-and-features.md`, `geo-brain/03-market/competitor-landscape.md`, `geo-brain/04-prompt-library/buyer-questions-by-trade.md` (§11–13) and `research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md`.*

*Access limits this session (they shape every section):* (1) WebFetch was blocked for api.census.gov, www.census.gov, www.capterra.com and www.reddit.com (proxy 403 / "unable to fetch"), so no page was opened directly; (2) the shared WebSearch budget for the turn (200 calls across all parallel agents) ran out after 17 searches by this agent. **All verbatim quotes below are verbatim as returned in search-engine result snippets; the pages themselves were not opened. No Reddit verbatims could be retrieved.** Census size-class tables, state-level CBP counts, subreddit member counts and the planned dedicated fan-out runs (O.2) could not be pulled; they are listed as Gaps with the exact pull needed. Facts from training knowledge (pre-June 2026) are never in "Cited Findings"; they appear in Inferences/Gaps labeled "training knowledge — verify".

---

## A. Definition and size

### Takeaway
The ICP sits inside two Census industries — NAICS 238210 (electrical *and other wiring* contractors, which includes low-voltage and fire-alarm installers) with **83,342 employer establishments / 1,015,983 employees (2023 CBP)** and NAICS 238220 (plumbing, heating and air-conditioning) with **111,207 establishments / 1,214,761 employees**; average size is only ~11–12 employees per establishment, so the 3–30-employee band is the bulk of the market, but only the plan-bidding (new-construction/TI) subset — not the residential service shops — is Quotr's ICP; a labeled estimate puts that subset at roughly 25,000–45,000 firms.

### Cited Findings
- NAICS 238210 is "Electrical Contractors **and Other Wiring Installation** Contractors" (the "other wiring" covers low-voltage/structured cabling and alarm wiring) — [NAICS.com 238210](https://www.naics.com/?p=16020); [SAMSearch 238210](https://samsearch.co/naics-ai-lookup/238210-electrical-contractors-and-other-wiring-installation)
- 2023 County Business Patterns, NAICS 238210: **83,342 establishments with paid employees; 1,015,983 employees (week of March 12, 2023); ~$77.8B annual payroll (~$76,545 per employee, incl. part-time)**; a further **159,693 nonemployer** electrical businesses exist outside CBP. Secondary aggregators, not the Census table itself (Census was not reachable) — [StartBusinessByState electrician statistics](https://startbusinessbystate.com/electrician-industry-statistics/); [NAICScodes.org electricians](https://naicscodes.org/naics-code-for/electricians/)
- CBP counts *locations*, not firms: "a company with three shops counts three times" — [StartBusinessByState](https://startbusinessbystate.com/electrician-industry-statistics/)
- 2023 CBP was released June 26, 2025 (latest vintage as of this note) — [Census press release](https://www.census.gov/newsroom/press-releases/2025/2023-county-business-patterns.html)
- 2023 CBP, NAICS 238220: **111,207 employer establishments; 1,214,761 employees; ~$89.5B payroll**; Census does not split HVAC from plumbing — [StartBusinessByState HVAC statistics](https://startbusinessbystate.com/hvac-industry-statistics/); [NAICScodes.org plumbing/HVAC](https://naicscodes.org/naics-code-for/plumbing-hvac/)
- "895 counties have fewer than 3 electrical contractors with staff" (title of a CBP-based analysis) — [StartBusinessByState](https://startbusinessbystate.com/?p=24102)
- Cost estimators (SOC 13-1051): 225,310 employed, mean annual wage $76,740 (May 2022); national median $35.94/hour (May 2023) — [BLS OEWS May 2022](https://www.bls.gov/oes/2022/may/oes131051.htm); [BLS OEWS May 2023](https://www.bls.gov/oes/2023/may/oes131051.htm). Third-party sites report a May 2025 median of $78,740 (not verified on BLS) — [Wagedex](https://wagedex.com/jobs/cost-estimators)
- Roles in this ICP (from existing Quotr persona work): owner/estimator, estimator or PM at specialty trades; "in smaller firms the owner often does the estimates after hours" (flagged there as an assumption) — `geo-brain/00-quotr/audiences-and-personas.md` §3
- Capterra: 95% of STACK's reviewers are small businesses and 81% work in construction — the small-trade buyer is the dominant reviewer population for takeoff tools — [Capterra STACK reviews](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/)

### Inferences
- Average establishment size is 1,015,983 ÷ 83,342 ≈ **12.2** (electrical) and 1,214,761 ÷ 111,207 ≈ **10.9** (plumbing/HVAC) employees (arithmetic). Means are pulled up by a few large firms, so the median establishment is well under 10 employees (likely).
- **Labeled estimate (speculative) of the ICP universe:** ~194,500 MEP employer establishments → perhaps 45–55% fall in the 3–30-employee band (~90k–105k) → perhaps 25–45% of those bid plan-based new construction/TI from invitations rather than living on service/replacement work → **~25,000–45,000 target firms**, plus an unknown number of low-voltage/fire-alarm firms classified under NAICS 561621 (security systems services) rather than 238210 (training knowledge — verify). Every factor here must be replaced by the CBP EMPSZES pull and a 50-firm call sample.
- **Revenue (speculative):** with payroll ≈ $76.5k/employee and specialty-trade payroll typically ~30–35% of receipts (training knowledge — verify against the Economic Census receipts table), a 10-person shop is roughly a $2–2.5M business and the 3–30 band spans roughly $0.6M–$7.5M.
- **Roles that touch the purchase:** owner (licensed master/qualifier, also chief estimator), spouse/partner or office manager (books, card on file, sometimes counts devices), foreman who "checks the number", occasionally a junior estimator. The estimator labour market (BLS mean ~$77k + burden) is the anchor the owner implicitly compares software against.
- Service-heavy HVAC/plumbing shops (the ServiceTitan/Housecall Pro market) are a *different* ICP: they quote from site visits, not PDFs. Excluding them is the single biggest sizing correction.

### Gaps
- CBP 2023 size-class (EMPSZES) rows for 238210/238220, the share under 20 employees, and receipts by size (2022 Economic Census) were not retrievable (api.census.gov/www.census.gov blocked). Pull: `https://api.census.gov/data/2023/cbp?get=NAICS2017_LABEL,EMPSZES,EMPSZES_LABEL,ESTAB,EMP,PAYANN&for=us:*&NAICS2017=238210` (repeat for 238220, 561621; add `&for=state:*` for B).
- One aggregator claimed 76.8% of 238220 establishments have <10 employees (2023) — the specific page could not be identified in the search summary; unverified.
- BLS May 2024/2025 OEWS pages for 13-1051 and 47-2111 (electricians) were not retrieved.
- No source found for the share of MEP firms that bid plan-based work vs. service work.

---

## B. Geography

### Takeaway
State-level counts could not be pulled this session, so the geographic case rests on (i) AGC's finding that 2026 demand is soft *except* data centers and power, (ii) Quotr's Bay Area home market and existing California/data-center content, and (iii) real place-based differences in labour-rate inputs, energy code and licensing. Geo pages are justified for **California (Title 24 + home market)** and **prevailing-wage public work**, plus one **data-center/large-MEP spoke** — not 50 templated state pages.

### Cited Findings
- AGC/Sage 2026 Outlook headline: "Contractors have dampened expectations for 2026 apart from data centers and power projects" — [AGC news release, Jan 8 2026](https://www.agc.org/news/2026/01/08/contractors-have-dampened-expectations-2026-apart-data-centers-and-power-projects-amid-worries-about)
- Construction input costs rose 7.1% (Jul 2025–Jul 2026) and 8.9% (Aug 2025–Aug 2026) per AGC, citing war and tariffs — material-escalation pressure on fixed bids — [AGC Aug 13 2026](https://www.agc.org/news/2026/08/13/construction-input-costs-climb-71-percent-between-july-2025-and-july-2026-impacts-war-and-tariffs); [AGC Sep 10 2026](https://www.agc.org/news/2026/09/10/construction-input-costs-climb-89-between-august-2025-and-august-2026-association-survey-finds-war) (URL slugs read as 7.1% and 8.9%; headline figures not re-opened)
- Quotr already publishes a data-center MEP piece ("data center construction estimating: MEP subcontractor choke point") and a California estimating-services page — [Quotr data-center post](https://quotr.ai/blog/data-center-construction-estimating-mep-subcontractor-choke-point/); [Quotr California services](https://quotr.ai/blog/construction-estimating-services-california/)
- Quotr Service shows a "Residential LA Fire Rebuilding" sample deliverable — `geo-brain/00-quotr/audiences-and-personas.md` §1 (from quotr.ai /service/)
- County concentration is uneven: 895 US counties have fewer than three electrical employer establishments — [StartBusinessByState](https://startbusinessbystate.com/?p=24102)
- The framework's rule: local pages only where "supply, pricing or regulation genuinely differ"; Google's scaled-content-abuse policy targets "many pages … with little value" and applies to AI Overviews/AI Mode — [uploaded framework, citing Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies)

### Inferences
**Priority geo segments (evidence rows partly to-be-filled; status labeled)**

| # | Segment | Why (evidence status) | Job that differs by place | Evidence row to pull (lite path) | Page justified? |
|---|---|---|---|---|---|
| G1 | **Bay Area / Northern California small electrical & low-voltage subs** | Quotr's home market (Berkeley SkyDeck), existing CA content; Title 24 energy code is California-only (training knowledge: 2025 Title 24 effective Jan 1 2026 — verify) | Lighting-controls, EV-ready and heat-pump scope on TI bids; C-10 (electrical) / C-7 (low-voltage) licensing; prevailing wage on public work | CBP 2023 ESTAB 238210/238220 for CA + Bay Area counties; BLS OEWS electricians wage for SF/SJ MSAs; DIR prevailing-wage determinations | **Yes** — one California hub (Title 24 + prevailing wage), 2 metro spokes max |
| G2 | **Data-center & power corridor MEP subs (2nd/3rd tier)** — N. Virginia, central Ohio, Phoenix, DFW, Atlanta (training knowledge — verify with Dodge starts) | AGC: data centers/power are the 2026 exception (cited) | Bigger sheet counts, gear/feeder-heavy takeoffs, compressed bid windows; small subs bid scopes to larger electrical primes | Dodge or ConstructConnect data-center starts by state; CBP 2019→2023 238210 growth by state | **One spoke**, built on the existing data-center post, not per-state pages |
| G3 | **Sun Belt housing + light-commercial subs** (TX, FL, GA, Carolinas, AZ, TN — training knowledge) | Volume of per-opening/per-fixture residential + TI bidding (inference) | Per-opening / per-fixture pricing, fast turnaround for builders | Census building permits by state; CBP growth; Trends DMA index for "electrical estimating software" | **No geo page**; persona facts go into prompts, content stays national |
| G4 | **Prevailing-wage public-works subs** (CA, NY, NJ, IL, WA, MA etc. — training knowledge: states with "little Davis-Bacon" laws; several states repealed theirs 2015–2017 — verify) | Labour rate is a *legal input* that changes the estimate | Certified payroll, wage determinations, fringe in labour units | DOL SAM.gov wage determinations; state DIR/DOL rate tables | **Yes — one topical page** ("prevailing-wage electrical estimate"), not per state |
| G5 | Midwest/South manufacturing & EV/battery megaproject ring (OH, MI, IN, KY, TN, GA — training knowledge) | Manufacturing starts (not pulled) | Industrial power, long conduit runs | Dodge manufacturing starts by state | No page until data shows volume |

**What really differs by place (and should become facts on pages):** (a) **labour rates** — open-shop vs union vs prevailing wage (Davis-Bacon federal; state laws); (b) **energy code** — California Title 24 Part 6 (lighting controls, EV readiness) vs IECC adoption elsewhere; (c) **NEC edition adopted** — states lag the 2023 NEC by one or two cycles, which changes AFCI/GFCI/surge scope (training knowledge — verify on NFPA's adoption map); (d) **licensing** — state vs municipal electrical licensing; California C-10/C-7/C-20/C-36 classes (training knowledge); (e) **material pricing/tariff exposure** (AGC input-cost data, national). Everything else (how to count devices, how to read a riser) is national and should not be geo-templated.
- No engine has been shown to add a user's city to a non-local software prompt spontaneously (framework); geography pays off via persona facts in prompts and place-specific facts on a few pages.

### Gaps
- CBP 2023 by state (and 2019→2023 growth) for 238210/238220; Dodge/ConstructConnect starts by state for data centers and manufacturing; Census building permits — not pulled (Census blocked; search budget exhausted).
- Title 24 2025 effective date, NEC adoption map and prevailing-wage state list are training knowledge here; verify before publishing.
- RL Electric's location is not stated in the repo; if it is Bay Area, it anchors G1.

---

## C. Jobs-to-be-done (in their own words)

### Takeaway
Five jobs recur, and four are about *time and not losing money*, not about "AI": get the number out before bid day, stop missing scope, bid more without hiring, keep evenings/weekends, and look as professional as bigger subs to GCs.

### Cited Findings
- Small-shop pain in their own words: bidding without a system meant "coming in way to high on my bids" — Mike Holt forum, small residential shop owner (thread attribution from search summary; verify) — [Mike Holt "estimating program small residential company"](https://forums.mikeholt.com/threads/estimating-program-small-residential-company.33963/post-33963)
- RL Electric (Quotr customer): takeoff from about 20 hours to 1–2 hours (homepage testimonial) — `geo-brain/00-quotr/product-and-features.md` §3.1; [RL Electric video](https://www.youtube.com/watch?v=Y2_PUPVtVaE)
- Vendor/industry framing of the night-work pattern: "many contractors still do takeoffs manually at night after full workdays" (paraphrase in search summary of a Skool community post); a sibling thread is titled "Estimating Burnout" — [Skool: bottlenecks in estimating & takeoffs](https://www.skool.com/construction-contractors/intro-looking-at-bottlenecks-in-estimating-takeoffs); [Skool: Estimating Burnout](https://chat.skool.com/construction-contractors/estimating-burnout)
- ELECTRICAL CONTRACTOR magazine runs a recurring "Your Business" estimating column on working under deadline ("estimating under pressure", "how long should it take") — [ECmag: estimating under pressure pt 2](https://www.ecmag.com/magazine/articles/article-detail/your-business-estimating-under-pressure-part-2); [ECmag: how long should it take](https://www.ecmag.com/section/your-business/how-long-should-it-take)
- Real questions already logged for the trades: "How do you estimate/bid on jobs?" (r/electricians), "How do you estimate electrical?" (r/estimators), "Pricing sq. ft. vs. per opening" (Electrician Talk), "Going rate per fixture – new construction" (PlumbingZone), "New construction HVAC bid questions" (HVAC-Talk) — `geo-brain/04-prompt-library/buyer-questions-by-trade.md` §11–13 with URLs ([r/electricians](https://www.reddit.com/r/electricians/comments/2cpo3y/how_do_you_estimatebid_on_jobs/), [r/estimators](https://www.reddit.com/r/estimators/comments/1mkde6w/how_do_you_estimate_electrical/), [Electrician Talk](https://www.electriciantalk.com/threads/pricing-sq-ft-vs-per-opening.5112/), [PlumbingZone](https://www.plumbingzone.com/threads/going-rate-per-fixture-new-construction.82414/), [HVAC-Talk](https://hvac-talk.com/vbb/threads/1803581-New-Construction-HVAC-bid-questions))

### Inferences
| # | Job (owner's voice — composite, not verbatim) | Functional / emotional / social |
|---|---|---|
| J1 | "Get me a number I trust off these 40 sheets before Thursday at 2." | Functional; hot |
| J2 | "Don't let me miss a whole fixture type or a feeder and eat it on the job." | Functional + fear |
| J3 | "Let me bid twice as many jobs without hiring an estimator I can't afford or keep." | Economic |
| J4 | "Give me my nights and Sundays back — my wife is done counting outlets at the kitchen table." | Emotional / family |
| J5 | "Make my proposal look like the big guys' so the GC takes me seriously." | Social / status |

### Gaps
- No switch interviews exist yet; these jobs should be validated with 6–12 recent Quotr sign-ups/churns per the framework (≥3 of 12 rule).

---

## D. Psychology

### Takeaway
A field-identity owner ("I'm an electrician, not a desk guy") who estimates under a hard external deadline, distrusts anything that might make *his* number wrong, prefers buying outright to subscriptions, and decides alone or with a spouse; the hot moment is a weeknight before bid day, the cold moment is a slow week, a renewal notice or year-end. Design around defaults, anchoring and temporal landmarks; do not lean on generic social proof or choice-overload tactics.

### Cited Findings
- **Risk posture — accuracy fear dominates:** contractors' top AI concerns are data accuracy (57%) and security (54%); only 26% rate their own data quality high (Dodge/CMiC, 235 contractors, Dec 2025) — [Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/); construction leaders' trust in AI fell 14 points YoY — [Autodesk State of Design & Make 2025](https://www.autodesk.com/blogs/construction/state-of-design-make-spotlight-construction/)
- **Adoption is mainstream now:** 52% of construction firms use AI tools, 80% of users daily (Houzz, mid-2026) — [Roofing Contractor](https://www.roofingcontractor.com/articles/102644-ai-use-jumps-among-construction-firms-houzz-survey-finds); 23% of firms use AI for estimating (AGC/Sage) — [AGC](https://www.agc.org/news/2026/01/08/contractors-have-dampened-expectations-2026-apart-data-centers-and-power-projects-amid-worries-about)
- **Subscription aversion / buy-once preference:** on Mike Holt's forum the most recent "best bid software" thread praises a tool as a one-time purchase with no subscription (search summary paraphrase) — [Mike Holt "Best Bid Software"](https://forums.mikeholt.com/threads/best-bid-software.2586877/); a different poster argued a one-time ~$2,000 purchase was worth it for residential and commercial work (thread not identified in the summary; one of the Mike Holt estimating-software threads, e.g. [Electrical Estimating software](https://forums.mikeholt.com/threads/electrical-estimating-software.49959/latest) — verify)
- **Price anchoring to cheap tools:** "I just can't see spending $1500 plus when you can get this software for about $30" — Mike Holt forum (verbatim per snippet; thread among [Electrical Estimating software](https://forums.mikeholt.com/threads/electrical-estimating-software.49959/latest) / [estimating and billing software](https://forums.mikeholt.com/threads/estimating-and-billing-software.28090/latest); verify)
- **Forum peers advise "try demos and training before buying"; some note you may need a maintenance subscription for updates** (search summary) — [Mike Holt "Estimating software"](https://forums.mikeholt.com/threads/estimating-software.88756/)
- **Biases ranked by replication (framework):** defaults/status quo d = 0.68 ([Jachimowicz et al. 2019](https://ideas.repec.org/a/cup/bpubpo/v3y2019i02p159-186_00.html)); anchoring replicates strongly ([Scientific American](https://www.scientificamerican.com/article/dozens-of-labs-respond-to-bolster-reliability-of-psychology-research)); temporal landmarks/fresh start (+82.1% "diet" searches at New Year, +14.4% at week start — [Dai, Milkman & Riis 2014](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf)); weak: generic social proof (0.94 pp in 126 RCTs — [DellaVigna & Linos](https://www.nber.org/system/files/working_papers/w27594/w27594.pdf)) and choice overload (d = 0.02 — [Scheibehenne et al. 2010](https://academic.oup.com/jcr/article/37/3/409/1816569)) (all via uploaded framework)
- **Time pressure shifts choice toward non-compensatory rules and unique features, and reduces deferral** — [Dhar & Nowlis, JCR 1999](https://profiles.wustl.edu/en/publications/the-effect-of-time-pressure-on-consumer-choice-deferral/) (via framework)
- **Strong habits override intentions** (β = −0.05 for strong habits) — [Ji & Wood 2007](https://dornsife.usc.edu/wendy-wood/wp-content/uploads/sites/183/2023/10/ji.wood_.2007_habitual_purchase_and_consumption.pdf); subscribers attend to renewal in ~18% of months — [Einav et al.](https://economics.northwestern.edu/docs/events/nemmers/2022/einav.pdf) (via framework)

### Inferences
| Dimension | Profile (likely unless marked) |
|---|---|
| Identity / status | Licensed tradesperson first; estimating is "paperwork that pays". Pride in "knowing my numbers"; software that "does it for you" threatens the craft → frame AI as *counting* (tedium), owner keeps *pricing* (judgment). |
| Risk posture | Loss-averse on the number (a missed scope item is a loss he eats personally); low-risk-tolerant on vendors (small, unreviewed vendors feel risky); moderate on price (< $100/mo is "card-on-file" money). |
| Decision style | Solo or owner + spouse; satisficing; peer-validated (forum, supply-house rep, another sub); tries on a real bid, not a demo file. |
| Time pressure | Bid dates are fixed by GCs; work is front-loaded to the 24–48 h before the bid (training knowledge: commercial bid deadlines commonly mid-week afternoons — verify). |
| **Hot moments** | Weeknights 9 pm–1 am in the 1–3 days before a bid; Sunday evening ("planning the week, 4 ITBs due"); immediately after losing a bid by a wide margin or finding a missed item on a job. |
| **Cold moments** | Slow weeks (often winter), renewal emails (STACK/Bluebeam), year-end tax planning (training knowledge: Section 179 year-end purchases — verify), association/trade-show season, Saturday morning office time. |
| Influencers | Spouse/partner/office manager (pays, often counts); foreman/lead (sanity-checks labour); supply-house counter rep (often provides free gear/lighting quotes — training knowledge, verify); GC estimators (format expectations); peers on Mike Holt/Electrician Talk/Reddit; accountant (cash/tax timing). |
| Biases to design for | **Defaults:** pre-loaded assemblies/labour units and a default trade template; trial defaults to "upload your real bid". **Anchoring:** show cost-per-bid next to "an estimator costs ~$77k/yr (BLS)" and "Bluebeam/STACK seat cost" — not next to Togal's $299. **Temporal landmarks:** Jan 1 / Revu 20 end-of-life Dec 31 2026 / new bid season / Monday. **Power of now:** "counts on your sheets tonight". |
| Biases to skip | "Join 10,000 contractors" lines (weak + Quotr has no review base); reducing options for "choice overload". |

### Gaps
- Time-of-day/day-of-week behavior is inferred; validate with Quotr's own trial sign-up timestamps (GA4/CRM) — the cheapest hard evidence available.
- No survey found on how many owners estimate after hours or how often spouses participate.

---

## E. Four forces (push, pull, anxiety, habit) with verbatim quotes

### Takeaway
Push is time + wrong numbers; pull is "count it for me" speed; **anxiety is the strongest restraining force** (AI accuracy, lock-in, price hikes, support); habit is "paper/Excel/the $30 program works". Incumbent reviews supply abundant anxiety/habit language that Quotr pages must answer directly.

### Cited Findings
**Verbatim quotes (as returned in search snippets; pages not opened; spelling preserved)**

| # | Force | Quote | Who / where | URL |
|---|---|---|---|---|
| Q1 | Push (price vs usage) + Habit | "In the end, I couldn't justify the price tag for as little as we actually used it. Maybe if we were estimating huge jobs every other day but it was to expensive for our small team." | STACK reviewer, Capterra | [Capterra STACK reviews](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/) |
| Q2 | Anxiety (price hike, lock-in) | "Jacked the price up 50% after the first year." … "Then when we decided to go to another program and cancel our subscription Stack locked us out of all our estimates and held it for ransom." | STACK reviewer, Capterra | [Capterra STACK reviews](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/) |
| Q3 | Anxiety (billing) | "Took price increase money from account without notice. refused to refund." | STACK reviewer, Capterra | [Capterra STACK reviews](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/) |
| Q4 | Push (cost of switching) | "We are a small operation and couldn't a high purchase price plus training costs." | STACK reviewer, Capterra | [Capterra STACK reviews](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/) |
| Q5 | Push → Pull | "non responsive to customer service issues. Much better and far far cheaper options available." | STACK reviewer, Capterra | [Capterra STACK reviews](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/) |
| Q6 | Push (tool friction) | "The system is to cumbersome, it takes way to many clicks to find and get an item ready to count." | ConEst IntelliBid reviewer | [Software Advice IntelliBid reviews](https://www.softwareadvice.com/construction/conest-intellibid-profile/reviews/) |
| Q7 | Push (tool friction) | "What I like least about IntelliBid is that the reporting process can sometimes be cumbersome, especially when trying to extract certain data out of ConEst." | ConEst reviewer, Capterra UK | [Capterra UK IntelliBid](https://www.capterra.co.uk/software/87139/intellibid) |
| Q8 | Anxiety (vendor trust) | "Bait & switch scammers" (1-star review title) | PlanSwift reviewer, Capterra | [Capterra PlanSwift reviews](https://capterra.com/p/70808/PlanSwift/reviews/) |
| Q9 | Habit (cheap anchor) | "I just can't see spending $1500 plus when you can get this software for about $30" | Mike Holt forum member | [Mike Holt "Electrical Estimating software"](https://forums.mikeholt.com/threads/electrical-estimating-software.49959/latest) (thread attribution from summary; verify) |
| Q10 | Habit | National Electrical Estimator is "easy, cheap, almost idiot proof" | Mike Holt forum member | [Mike Holt "estimating and billing software"](https://forums.mikeholt.com/threads/estimating-and-billing-software.28090/latest) (attribution unverified) |
| Q11 | Push (losing bids) | "coming in way to high on my bids" | Small shop owner bidding without a system, Mike Holt | [Mike Holt small residential company](https://forums.mikeholt.com/threads/estimating-program-small-residential-company.33963/post-33963) (attribution unverified) |
| Q12 | Pull (fit for small shop) | "great system for a small contractor, and it's very reasonably priced" | Mike Holt poster about Electrical Bid Manager (a vendor staffer also replied in thread) | [Mike Holt "vision estimating software"](https://forums.mikeholt.com/goto/post?id=1457939) (attribution unverified) |
| Q13 | Anxiety (data updates) | McCormick "seemed so buggy with the pricing updates" | Mike Holt poster (older experience) | [Mike Holt "Best estimating software for commercial work?"](https://forums.mikeholt.com/threads/best-estimating-software-for-commercial-work.2590999/) (attribution unverified) |
| Q14 | Anxiety (AI accuracy, expert voice) | "Symbol recognition trusts the legend. If the legend and the fixture schedule disagree, the software picks one. A whole device category can disappear, and no one notices until the material order." | AI Insights News article (not a buyer) | [AI Insights News](https://aiinsightsnews.net/audit-ai-electrical-estimate/) |
| Q15 | Anxiety (input quality) | "Most bid sets arrive as flattened PDFs." | Same article | [AI Insights News](https://aiinsightsnews.net/audit-ai-electrical-estimate/) |
| Q16 | Anxiety (AI) | r/estimators users call past AI takeoff "hit-or-miss" (observed via Perplexity in the sibling note) | r/estimators | [r/estimators AI takeoff thread](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/) |
| Q17 | Pull (proof) | RL Electric: takeoff "20 hours … 1–2 hours" | Quotr homepage testimonial | `geo-brain/00-quotr/product-and-features.md`; [RL Electric video](https://www.youtube.com/watch?v=Y2_PUPVtVaE) |

**Other force evidence (non-verbatim)**
- PlanSwift (Capterra ~4.3, ~396 reviews): complaints cluster on support (most frequent), file handling ("works best with flat PDFs"), takeoff not auto-updating the linked workbook, crashes/licensing; electrical users praise assemblies/templates — [Capterra PlanSwift reviews](https://capterra.com/p/70808/PlanSwift/reviews/)
- Togal.AI on G2: 4.8 from 53 reviews; top cons "Missing Features (11 reviews)", "Improvement Needed (4)"; G2 says there are not enough reviews to provide buying insight; Trustpilot ~3.2 — [G2 Togal reviews](https://g2.com/products/togal-ai/reviews); [Trustpilot Togal](https://at.trustpilot.com/review/www.togal.ai)
- Bluebeam: perpetual licence sales ended Sep 30 2023 (Revu 21+ subscription-only); ~10% list-price rise from June 1 2024; Revu 20 end of support July 31 2026 and **end of life Dec 31 2026** (single third-party source); one forum complaint that every user needs a subscription — [Microsol Resources](https://microsolresources.com/?p=16003); [Softabase](https://softabase.com/software/construction/bluebeam-revu); [Tom's Hardware forum](https://forums.tomshardware.com/threads/bluebeam-revu-alternative.3788212)

### Inferences
| Force | Content of the force for this ICP | Prompt class it generates (framework mapping) |
|---|---|---|
| **Push** | Nights/weekends lost; bids late or skipped; wide misses ("way to high"); tool friction (clicks, crashes, flat-PDF limits); price hikes on renewal (STACK 50%, Bluebeam +10%, Revu 20 EOL) | "is there a faster way to…", "why do I keep losing bids…", "cheaper alternative to [tool]" |
| **Pull** | Automatic device/fixture counts; browser/Mac; month-to-month; trade templates; done-for-you fallback on crunch weeks | "best [trade] takeoff software for small contractors", "AI that counts electrical symbols" |
| **Anxiety** | AI misses a category (Q14); scanned/flattened PDFs (Q15); lock-in/data hostage (Q2); surprise billing (Q3); small vendor with no reviews (Quotr: 0 G2 reviews per repo); learning time during bid season | "is AI takeoff accurate", "[brand] reviews", "[brand] vs [brand]", "can I export my data" |
| **Habit** | Highlighters + Bluebeam count tool + Excel; $30 legacy estimator (Q9–Q10); "I know my labour units" | "do I really need estimating software", "can I just use Bluebeam and Excel" |
- Anxiety is the *dominant restraining force* (7 of 17 quotes) — so Quotr's decision pages must lead with accuracy method, export/cancel terms and price-lock language, not features.

### Gaps
- No Reddit verbatims (r/electricians, r/HVAC, r/Plumbing, r/lowvoltage) could be retrieved; no YouTube comments; no Beam AI, Accubid or McCormick review verbatims (searches ran out). Mike Holt quote-to-thread mapping must be verified by opening the threads.

---

## F. Trigger events and trigger calendar

### Takeaway
The highest-value datable trigger right now is **Bluebeam Revu 20 end-of-life on December 31, 2026** (eight weeks away), followed by year-end/new-year landmarks, renewal price hikes, an estimator quitting, a run of lost bids, a missed-scope loss, and bid-volume spikes from data-center/power work.

### Cited Findings
- Revu 20: end of support July 31 2026; end of life Dec 31 2026 (Studio Sessions/Projects/API stop working) — [Softabase](https://softabase.com/software/construction/bluebeam-revu) (single source; verify with Bluebeam)
- Bluebeam ~10% price rise effective June 1 2024 for new subscriptions, added users and renewals — [Microsol Resources](https://microsolresources.com/?p=16003)
- STACK renewal increase anecdote: "Jacked the price up 50% after the first year." — [Capterra STACK reviews](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/)
- Input-cost escalation 7.1–8.9% YoY (2026) and November 2025 costs "outpacing increases contractors bid" — [AGC Jan 14 2026](https://www.agc.org/news/2026/01/14/construction-costs-rise-fastest-rate-january-2023-november-outpacing-increases-contractors-bid); [AGC Sep 10 2026](https://www.agc.org/news/2026/09/10/construction-input-costs-climb-89-between-august-2025-and-august-2026-association-survey-finds-war)
- Data centers/power are the 2026 demand exception — [AGC Jan 8 2026](https://www.agc.org/news/2026/01/08/contractors-have-dampened-expectations-2026-apart-data-centers-and-power-projects-amid-worries-about)
- Fresh-start landmarks raise goal-directed search (+82.1% at New Year; +14.4% week start) — [Dai, Milkman & Riis](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf)
- Existing Quotr persona triggers (assumption-level): bid-invite spike, lost bid because the price was late, estimator quits, renewal notice, missed-scope job, move to browser/Mac — `geo-brain/00-quotr/audiences-and-personas.md` §3

### Inferences
**Trigger calendar (dates known where cited; others likely/speculative)**

| When | Trigger | Status | Mode | Action for Quotr |
|---|---|---|---|---|
| **Nov 6 → Dec 31 2026** | Revu 20 EOL; year-end budget/tax spend | Known (EOL single-source) / likely (tax) | Cold → hot as date nears | Publish "Revu 20 end of life: options for small subs" page now; refresh Dec 1 and Dec 20 |
| Jan 1–31 | New-year landmark; new bid season planning; annual renewals | Likely | Cold | "2027 best estimating software for small electrical contractors" refresh dated Jan 2027 |
| Feb–May | Public/school summer-work bid season; spring ITB volume spike (training knowledge — verify with Dodge/PlanHub data) | Likely | Hot | Urgent-mode "bid due tomorrow" pages + Service turnaround offer |
| Any week | 3–10 lost bids in a row | Speculative frequency | Cold post-mortem | "Why am I losing bids: scope vs labour units" answer page |
| Any week | Estimator quits / owner sick | Likely | Hot | "Hire vs outsource vs software: cost per bid" calculator |
| Any job | Missed-scope loss discovered at rough-in | Likely | Cold (anger) | Scope-gap checklist (existing /blog/scope-gap-construction/) + legend-vs-schedule cross-check |
| On renewal date | STACK/PlanSwift/Bluebeam renewal email | Likely | Cold, deadline-bounded | "Alternatives" pages with price-lock and export terms |
| Monday mornings, Sunday nights | Weekly ITB review | Likely | Mixed | Schedule social/forum activity and email for Sun 6–10 pm |
| Ongoing 2026–27 | Data-center/power bid invites to small MEP subs | Known demand / speculative reach to small subs | Cold | Data-center spoke page |

### Gaps
- No PlanHub/BuildingConnected/Dodge data on monthly ITB volume to small subs was retrieved; the seasonality row is training knowledge.

---

## G. Switch timeline with prompt form at each stage

### Takeaway
Prompts move from situational venting with no category noun ("doing takeoffs till midnight") to category nouns ("electrical takeoff software"), then to brands, prices and objections ("Quotr vs PlanSwift", "does STACK lock your data"), then to how-to-in-product prompts.

### Cited Findings
- Framework mapping: first-thought prompts are vague and situational; active-looking prompts contain category nouns and comparators; deciding prompts contain brand names, prices and objections; the engine itself injects "best" into 24.3% of advice-question fan-outs — [uploaded framework; PPC Land/Peec](https://ppc.land/what-chatgpt-actually-searches-for-5-million-fanout-queries-analyzed/)
- 51% of B2B buyers start software research in an AI chatbot; 69% chose a different vendor than planned because of chatbot guidance (G2, cross-industry) — [G2 via PR Newswire](https://www.prnewswire.com/news-releases/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots-302742807.html)

### Inferences
| Stage | What's happening | Prompt form (example) | Engine/place |
|---|---|---|---|
| First thought | Third late night this week; spouse complains; lost a bid | "is there a faster way to do electrical takeoffs at night" / "how do small electrical contractors keep up with bids" | ChatGPT on phone; Google |
| Passive looking | Notices ads, forum threads, a peer's tablet | "can AI count outlets on a PDF plan" / "is AI takeoff any good r/estimators" | Google (Reddit results), YouTube |
| Active looking | Has an ITB due; sets aside Saturday | "best electrical takeoff software for small contractors 2026 under $150/month mac" | ChatGPT, Google AI Mode, Capterra |
| Deciding | 2–3 names; fears accuracy/lock-in | "Quotr vs PlanSwift for electrical", "STACK price increase", "Togal reviews", "can I cancel Quotr anytime" | ChatGPT + vendor pricing pages + G2/Capterra |
| Consuming | 7-day trial on a real bid | "how to count fixtures from a lighting schedule in Quotr", "export Quotr takeoff to Excel" | Vendor docs, YouTube tutorials, ChatGPT |

### Gaps
- Real typed prompts per stage require switch interviews asking "what exactly did you type, and into what?" (framework's key question); none exist yet.

---

## H. Current alternatives and what does NOT satisfy them

### Takeaway
The real competitor is "paper + Bluebeam count tool + Excel + my own labour units", with legacy electrical estimators (ConEst, Accubid, McCormick, Electrical Bid Manager, National Electrical Estimator), general takeoff tools (PlanSwift, STACK), AI takeoff (Togal, Beam AI, Kreo) and outsourced estimators as the other options. Ranked unmet needs (tiny sample, n = 22 complaint snippets): **(1) price/value for a small, infrequent user; (2) vendor behaviour — price hikes, billing, lock-in, support; (3) friction/learning curve; (4) PDF/scan handling and AI accuracy trust; (5) stability; (6) missing features.**

### Cited Findings
- **Pricing landscape for small electrical shops (vendor-published, via search):** Accubid publishes no price; Trimble Estimation MEP $1,950/user/yr; TurboBid ~$135/mo; STACK $299/user/mo; PlanSwift $2,000–3,000/seat/yr; small shops should budget ~$60–299/mo; implementation can run $2,000–5,000 — [BuildOps cost guide](https://buildops.com/resources/electrical-estimating-software-cost); [BuildOps small-contractor list](https://buildops.com/resources/electrical-estimating-software-for-small-contractor). Conflicts: STACK "as low as $249/user/month" and PlanSwift "$1,749/user/year" elsewhere — `geo-brain/03-market/competitor-landscape.md` §2; Capterra lists PlanSwift "from $49 per user per month" — [Capterra PlanSwift](https://capterra.com/p/70808/PlanSwift/reviews/)
- Vendor guide: budget options from $29/mo, dedicated electrical tools ~$99/mo, cloud platforms $158–250/mo; general construction tools "lack electrical-specific features like NEC labor units, conduit fill calculations, and pre-built electrical assemblies" (vendor claim) — [ElectricalTakeoffSoftware.com](https://www.electricaltakeoffsoftware.com/blog/electrical-estimating-software-for-small-contractor)
- AI-native options: Togal Growth $299/user/mo (yearly); Beam AI done-for-you ~$15–25K/yr per trade (ConstructConnect estimate); Kreo from $35/user/mo — `geo-brain/03-market/competitor-landscape.md` §2; [G2 Togal pricing](https://www.g2.com/products/togal-ai/pricing)
- Legacy electrical estimators discussed by small shops on Mike Holt: Best Bid (one-time purchase), Electrical Bid Manager (Vision InfoSoft), ConEst IntelliBid + SureCount, Accubid, McCormick, TurboBid, Red Rhino; no consensus pick for small residential/light commercial shops — [Mike Holt small-business thread](https://forums.mikeholt.com/threads/electrical-estimating-software-for-small-businesses.147953/); [Mike Holt "Best Bid Software"](https://forums.mikeholt.com/threads/best-bid-software.2586877/)
- ConEst's split into IntelliBid + SureCount means two interfaces (claim made by competitor McCormick) — [McCormick ConEst review](https://www.mccormicksys.com/?p=87667)
- Outsourcing risk anecdote: a contractor who used an outside estimating service absorbed losses on that job (single forum anecdote, search summary) — [Mike Holt "Estimating Services"](https://forums.mikeholt.com/threads/estimating-services.133922/post-133922)
- Gartner Digital Markets (SMB construction buyers): 45% run operations manually, 12% have no system — [Gartner Digital Markets](https://www.gartner.com/en/digital-markets/insights/stand-out-in-your-category-with-construction-buyer-insights)
- Review-based complaints: see E (STACK Q1–Q5, ConEst Q6–Q7, PlanSwift Q8 + support/file/crash themes, Togal "Missing Features", Bluebeam subscription/price changes)

### Inferences
**Unmet-need ranking (count of complaint snippets gathered this session, n = 22; directional only)**

| Rank | Unmet need | Count | Examples | What Quotr must show |
|---|---|---|---|---|
| 1 | Price fits a small, irregular user; no purchase + training penalty | 6 | Q1, Q4, Q5, Q9, Accubid unpublished, Bluebeam per-user subscription | $79.90 Lite, month-to-month, cost-per-bid math |
| 2 | Vendor behaviour: hikes, billing, lock-in, support | 6 | Q2, Q3, Q5, Q8, PlanSwift support, Bluebeam +10% | Written price-lock/export/cancel policy; named support |
| 3 | Friction / learning curve / clicks | 3 | Q6, Q7, PlanSwift learning curve | Time-to-first-count on a real sheet (video) |
| 4 | PDF/scan handling and AI accuracy | 3 | Q14, Q15, Q16, PlanSwift "flat PDFs" | Published method + error rates on scans vs vector (Quotr's own 95–99% / 80–88% claims need a method page) |
| 5 | Stability (crashes, lag) | 2 | PlanSwift, STACK | Browser-based, no install |
| 6 | Missing features / trade depth | 2 | Togal "Missing Features (11)", general tools lack labour units | Trade assemblies, labour-unit library, fire-alarm/low-voltage symbol sets |
- **"Doing nothing" is strong:** a $30 legacy estimator + Bluebeam count tool + Excel is "good enough" for many (Q9–Q10). The wedge is not replacing their pricing brain but removing *counting time*.
- **Outsourcing alternative:** supply-house quotes (free, training knowledge) and estimating services. Quotr Service at $0.25/sq ft prices a 30,000 sq ft TI at **$7,500 per bid** (arithmetic) — very high for a sub whose hit rate is low (hit-rate data not found). Either Service is priced per project across trades (TO CONFIRM) or it is mis-fit for this ICP; Plus's 2,000 sq ft/month of takeoff credits covers only a small tenant space. This is a likely positioning gap: the ICP needs a **per-sheet or per-trade crunch-week price**.

### Gaps
- No 1–3-star review verbatims for Beam AI, Accubid, McCormick or Togal; no Reddit complaint threads (blocked). Frequency counts must be redone on ≥50 reviews per tool (Capterra/G2/Software Advice) when fetch access exists.

---

## I. Willingness to pay, price anchors, who pays, sales cycle, trial behavior

### Takeaway
Card-on-file territory is roughly **$60–300/month**, with annual construction-software budgets of **$1,600–4,000**; anchors are the "$30 program", PlanSwift ~$1,749–3,000/yr, STACK ~$249–299/mo, Togal $299/mo and an estimator at ~$77k/yr. Quotr Lite ($958.80/yr) sits under every anchor; the owner (or spouse) pays on a card, decides in days-to-weeks, and trials on a live bid.

### Cited Findings
- Construction software buyers expect to spend about $1,600–4,000/yr; pricing and ease of use dominate selection — [Capterra buyer insight](https://www.capterra.com/resources/construction-software-buyer-insight/)
- Small electrical shop budget ~$60–299/month — [BuildOps cost guide](https://buildops.com/resources/electrical-estimating-software-cost)
- Anchors: STACK $249–299/user/mo; PlanSwift $1,749–3,000/seat/yr; Togal $299/user/mo; Kreo $35; Trimble Estimation MEP $1,950/yr; TurboBid ~$135/mo — see H sources
- "$1500 plus" vs "$30" anchor (Q9) and preference for one-time purchase — [Mike Holt](https://forums.mikeholt.com/threads/best-bid-software.2586877/)
- Estimator labour cost anchor: BLS mean $76,740 (May 2022) — [BLS](https://www.bls.gov/oes/2022/may/oes131051.htm)
- Quotr: Lite $79.90/seat/mo, Plus $299.90, Enterprise custom; 7-day free trial, "Cancel anytime — no charge if canceled"; no annual price shown; retired $299.90/$499.90 plans still appear on ~13 Quotr URLs and in llms.txt, making entry price look ~4× higher to AI engines — `geo-brain/00-quotr/product-and-features.md` §2
- Forum norm: try demos/training first — [Mike Holt "Estimating software"](https://forums.mikeholt.com/threads/estimating-software.88756/)

### Inferences
- **Who pays:** owner's business card; spouse/office manager often executes and polices renewals (likely).
- **Sales cycle:** self-serve, 1–21 days from active looking to paid, compressed by a bid date (likely); trial is judged on *one real bid* — if the first count on their own sheets is wrong or slow, the trial is over (likely).
- **Trial risk:** a 7-day trial that starts on a Tuesday night may end before the next bid; defaults matter — offer "trial clock starts at first upload" or a 14-day trial in bid season (speculative test).
- **Value math to publish (arithmetic):** if takeoff falls from 20 h to 2 h (RL Electric) on 4 bids/month, ~72 owner-hours/month are freed; at the BLS estimator median (~$36/h) that is ~$2,600/month vs $79.90.
- **Price-message risk:** stale $299.90 pricing in AI answers anchors Quotr *above* PlanSwift's monthly equivalent — fix before any off-site push (repo finding).

### Gaps
- No primary data on how long MEP subs trial before buying or conversion rates; Quotr's own trial-to-paid by trade is the best source.

---

## J. Vocabulary list

### Takeaway
Pages and prompts must use the trade's nouns; the engine's sub-queries will contain them.

### Cited Findings
- Electrical: openings/devices, per-opening pricing, LF conduit and wire, home runs, circuits, panel schedule, service size (200A/400A), feeders, labour units, assemblies; Plumbing: fixture count/schedule, per-fixture pricing, LF pipe by system (CW/HW/waste/vent) and material (PEX, copper, PVC/ABS DWV), fittings, risers, rough-in vs trim-out, fixture allowance; HVAC: tons, CFM, Manual J/S/D, duct LF, sheet-metal weight, diffusers/grilles/registers, line sets — `geo-brain/04-prompt-library/buyer-questions-by-trade.md` §11–13; [ACCA Manual J](https://www.acca.org/standards/technical-manuals/manual-j)
- "NEC labor units, conduit fill calculations, and pre-built electrical assemblies" as buyer feature language — [ElectricalTakeoffSoftware.com](https://www.electricaltakeoffsoftware.com/blog/electrical-estimating-software-for-small-contractor)
- Legend vs fixture schedule conflict; flattened PDFs — [AI Insights News](https://aiinsightsnews.net/audit-ai-electrical-estimate/)

### Inferences
| Domain | Terms (training knowledge where not cited above) |
|---|---|
| Bidding | ITB / invitation to bid, bid date, bid form, plans and specs, addenda, alternates, inclusions/exclusions, scope letter, RFI, pre-bid walk, plan room, bid bond, retainage, prequal, bid-hit ratio, "number", buyout, VE (value engineering) |
| Electrical | device counts, home runs, branch vs feeder, one-line/riser diagram, lighting/fixture schedule, legend, EMT/MC/Romex (NM-B), wire pulls, conduit fill, gear (switchgear/panelboards), temp power, NECA *Manual of Labor Units* (MLU), labour factor/difficulty factor |
| Low-voltage / fire alarm | structured cabling, drops, IDF/MDF, Cat6, access control, CCTV, FACP, initiating devices (smokes, heats, pulls), notification appliances (horn/strobes), NAC panels, BICSI, NFPA 72 |
| Plumbing | DFU (drainage fixture units), underground/rough/top-out/trim, cleanouts, water heaters, gas piping |
| HVAC | RTUs, VAV boxes, ductwork by gauge, sheet-metal pounds, controls, TAB |
| Commercial terms | prevailing wage, Davis-Bacon, certified payroll, union vs open shop, Title 24 (CA), NEC 2023 adoption |
| Their tools | Bluebeam "count tool", highlighters, PlanSwift, STACK, ConEst, Accubid, McCormick, Excel, PlanHub, BuildingConnected, ConstructConnect, Dodge |

### Gaps
- Low-voltage and fire-alarm terms are training knowledge; validate against r/lowvoltage / r/firealarms threads and Quotr's /software/trades/low-voltage/ and /fire-protection/ pages.

---

## K. Channels where they read and ask

### Takeaway
Forums (Mike Holt, Electrician Talk, ContractorTalk, HVAC-Talk, PlumbingZone) and Reddit (r/estimators, r/electricians, r/HVAC, r/Plumbing/r/plumbers, r/Construction) carry the peer questions; review directories own the "reviews/alternatives" node; ELECTRICAL CONTRACTOR (ecmag.com) and association channels (IEC, NECA, PHCC, ACCA, BICSI) carry trust. Member counts could not be retrieved.

### Cited Findings
- Mike Holt forum threads on small-shop estimating software dominate retrieval for "small electrical contractor estimating software recommendation" (9 of 9 results in this session's search) — [Mike Holt forums](https://forums.mikeholt.com/threads/electrical-estimating-software-for-small-businesses.147953/)
- Electrician Talk, PlumbingZone, HVAC-Talk, ContractorTalk, r/electricians, r/estimators, r/plumbers, r/askaplumber, r/HVAC threads host bidding questions — `geo-brain/04-prompt-library/buyer-questions-by-trade.md` (URLs in C)
- r/estimators appeared in 6 of 32 Perplexity prompts' citations; YouTube was never cited in 45 Perplexity runs — `quotr_ai_visibility_tests.md` §5
- ELECTRICAL CONTRACTOR magazine's "Your Business" estimating columns — [ECmag](https://www.ecmag.com/section/your-business/how-long-should-it-take)
- Review directories: Capterra (STACK ~1,348–1,400 reviews; PlanSwift ~396), Software Advice, G2, SourceForge, Trustpilot — see E/H
- Beam AI promoted instant HVAC takeoffs at AHR Expo 2026 — `geo-brain/04-prompt-library/buyer-questions-by-trade.md` §13 (from competitor benchmark)
- Other observed discovery venues (AI-engine synthesis, not survey-backed): Facebook estimator groups, YouTube demos, trade shows — `geo_content_playbook_b2b.md` §6

### Inferences
| Channel | Type | Members/size | Role in journey |
|---|---|---|---|
| r/estimators, r/electricians, r/HVAC, r/Plumbing, r/plumbers, r/Construction, r/lowvoltage, r/firealarms | Reddit | **Not retrieved** (gap) | Passive/active looking; anxiety validation |
| Mike Holt forum, Electrician Talk, ContractorTalk, HVAC-Talk, PlumbingZone | Forums | Not retrieved | Peer picks; old threads still retrieved |
| Facebook groups (electrical estimating, contractor owner groups) | Social | Not retrieved | Spouse/office manager participation (likely) |
| YouTube: RL Electric video, Quotr demo, trade estimating tutorials ("Electrical Estimating for New Residential Construction Simplified", "Best Plumbing Takeoff Software for Contractors") | Video | Not retrieved | Consuming + deciding proof ([video](https://www.youtube.com/watch?v=Mp_Vvpm2ybo), [video](https://www.youtube.com/watch?v=MAWJZ95NOMk)) |
| IEC (open-shop electrical; apprenticeship), NECA (union electrical; MLU publisher), PHCC, ACCA, MCAA/SMACNA, BICSI, AFAA/NFPA | Associations | Not retrieved | Trust, webinars, chapter events (training knowledge) |
| EC&M, Electrical Contractor (ecmag.com), ACHR News, Contracting Business, PHC News | Trade press | Not retrieved | Authority; listicle-free zone where data stories land |
| NECA Show, IEC Convention, AHR Expo, BICSI conferences | Events | — | Cold-mode discovery |
| Capterra/GetApp/Software Advice (one listing), G2, SourceForge | Directories | — | Deciding; AI citation source |

### Gaps
- Subreddit member counts (GummySearch-type data), Facebook group sizes, association membership numbers, podcast list and YouTube creator names were not retrieved; required before ranking community placements by reach.

---

## L. Proof required at each stage

### Takeaway
Proof must be one-click verifiable and specific to *their* sheets: a time-to-first-count video at first thought, an accuracy method at active looking, review counts and price/cancel terms at deciding, and a working count on their own bid in the trial.

### Cited Findings
- 86% of AI-assisted shoppers verify elsewhere; trust in AI alone falls from 42% under $50 to 5% over $500 — [MarTech via framework](https://martech.org/the-ai-shopping-stats-2026-what-you-need-to-know/)
- Construction buyers' top AI concern is data accuracy (57%) — [Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/)
- Quotr's accuracy claims (95–99% on vector PDFs; 80–88% on low-res scans) are self-reported without a method page; RL Electric case page shows no numbers; G2 reportedly 0 reviews — `geo-brain/00-quotr/product-and-features.md` §3.1, §4
- Engines demote self-published claims to fact citations and promote brands on independent lists/review alternatives pages — `quotr_ai_visibility_tests.md` §5 inferences

### Inferences
| Stage | Proof that satisfies | Quotr has today? |
|---|---|---|
| First thought | 60–90-sec video: real electrical sheet → device counts; "tonight" framing | Partly (demo video) |
| Passive | Peer voice (RL Electric owner on camera), forum answer from a real estimator | Partly |
| Active | Accuracy method page: test sets, vector vs scan, error by device type, what to double-check (legend vs schedule) | **No** |
| Deciding | 10+ verified reviews on Capterra/G2; price table incl. month-to-month, export, cancel, price-lock; "vs PlanSwift/STACK/Bluebeam" page with honest trade-offs | **No** (reviews), partly (vs posts with stale pricing) |
| Consuming | Trade template loaded by default; "first bid in 30 min" tutorial; human onboarding (Plus has 2 h) | Partly |

### Gaps
- No customer-provided accuracy data beyond RL Electric's time claim.

---

## M. Coding chains (trigger → stage → mode → restraining force → exact prompt → proof)

### Takeaway
Eight chains cover the ICP; four are hot-mode (bid-deadline driven) and need urgent-mode pages, four are cold-mode and need considered comparison pages. Prompts are composites written in the ICP's register (not observed verbatims).

### Cited Findings
- Chain structure and the "promote at ≥3/12 interviews or 5/50 posts" threshold come from the uploaded framework (synthesis, not a published rule) — uploaded framework §"Code every buyer…"
- Trigger evidence: Revu 20 EOL ([Softabase](https://softabase.com/software/construction/bluebeam-revu)); STACK hike (Q2, [Capterra](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/)); losing bids (Q11, [Mike Holt](https://forums.mikeholt.com/threads/estimating-program-small-residential-company.33963/post-33963)); AI miss anxiety (Q14, [AI Insights News](https://aiinsightsnews.net/audit-ai-electrical-estimate/))

### Inferences
| # | Trigger | Stage | Mode | Restraining force | Prompt typed (composite, SIMULATED wording) | Proof required |
|---|---|---|---|---|---|---|
| M1 | 4 ITBs due same week (PlanHub/BuildingConnected) | First thought → passive | **Hot**, 10:30 pm Tue | Habit ("highlighters work") | "is there a faster way to count outlets and lights off pdf plans i have 3 bids due this week" | 60-sec video on an electrical sheet; free trial today |
| M2 | Lost a bid because number was late / skipped bid | Active | Hot, next morning | Anxiety (AI accuracy) | "can AI takeoff software actually count electrical symbols accurately or do i still have to recount" | Method page + error table; legend/schedule cross-check |
| M3 | Missed a fixture type / feeder, ate $8k | First thought → active | Cold (angry), weekend | Anxiety (AI also misses) | "how do I stop missing scope on electrical bids checklist" | Checklist page + feature that flags legend vs schedule mismatches |
| M4 | Only estimator quits | Active | **Hot** | Anxiety (cost, ramp) | "my estimator quit, should I hire another one, outsource takeoffs or get AI software, what does each cost for a 20 person electrical company" | Cost-per-bid calculator: BLS wage vs Service vs Lite |
| M5 | Revu 20 EOL Dec 31 / Bluebeam renewal | Deciding | Cold → hot near date | Habit (knows Bluebeam) | "bluebeam revu 20 end of life what should a small electrical contractor switch to for takeoff" | Dated EOL page; price table; "keep your PDFs/markups" |
| M6 | STACK renewal +50% | Deciding | Cold | Anxiety (lock-in again) | "cheaper alternative to STACK takeoff that lets me export my estimates" | Written export/cancel policy; month-to-month price |
| M7 | First data-center / large TI invite (200+ sheets) | Active | Cold | Anxiety (scale) | "takeoff software that can handle a 300 sheet electrical set for a data center bid" | Case/benchmark on a large set; Service fallback price per sheet |
| M8 | Spouse "no more weekends" / year-end | First thought | Hot emotion, cold time | Habit | "how do small electrical contractors handle estimating without working every night" | Peer story (RL Electric owner), time saved per bid |

### Gaps
- Chains are hypotheses until 6–12 switch interviews + 50 community posts are coded; frequency per chain unknown.

---

## N. Prompt matrix

### Takeaway
Twelve full-context first-person prompts (persona facts embedded), six short category prompts and three brand prompts, tagged per the framework. Demand tiers are labeled estimates (no volume data pulled).

### Cited Findings
- Fan-out injection rates: "best" 15.3%, "review(s)" 6.8%, "2026" 5.4%, "vs" 4.3% (Peec, 5M fan-outs); GPT-5.6 fan-outs carry "2026" 22.9%, "official" 13.1%, "price" 8.9%, and 75.9% of `site:` searches target brand domains (Ahrefs) — [PPC Land/Peec](https://ppc.land/what-chatgpt-actually-searches-for-5-million-fanout-queries-analyzed/); [Ahrefs](https://ahrefs.com/blog/query-fan-out-chatgpt/)
- "Ask for a pick" prompts get a 22.8% brand-recommendation rate vs 8.0% for topic-only — [Momentic](https://momenticmarketing.com/blog/prompt-set-worth-tracking); brand prompts mention the brand 91.6% vs 19.6% non-brand (keep separate) — [Momentic](https://momenticmarketing.com/blog/prompt-set-worth-tracking)
- Persona facts change which brands are named — [Profound](https://www.tryprofound.com/blog/do-answer-engines-customize-responses-to-different-personas)
- 72% of 5,000+ Software Advice construction-buyer conversations asked about estimating (demand proxy) — [Software Advice](https://www.softwareadvice.com/construction/cost-estimating-software-comparison/)

### Inferences
**Full-context prompts (first person; SIMULATED wording)**

| ID | Prompt | Intent | Stage | Urgency | Mode | Engine | Expected fan-out nodes | Tier (est.) |
|---|---|---|---|---|---|---|---|---|
| F1 | "I own a 9-person electrical shop in Fort Worth, TX. I do takeoffs every night till midnight off PlanHub invites with highlighters and the Bluebeam count tool. Is there a faster way to count devices and fixtures off PDF plans without hiring an estimator?" | learn → pick | First thought/passive | Acute | Hot | ChatGPT | AI electrical takeoff software; best electrical takeoff software 2026; Bluebeam count tool alternative; reviews | 3 |
| F2 | "Small commercial electrical contractor, 14 employees, Phoenix. We bid 6–8 tenant improvements a week from BuildingConnected; my wife and I do takeoffs in Bluebeam and price in Excel. What estimating software with NECA labor units should we buy for under $200 a month?" | ask-for-a-pick | Active | Recurring | Cold | ChatGPT, AI Mode | best electrical estimating software small contractors 2026; price; NECA labor units software; Accubid vs ConEst vs McCormick | 4 |
| F3 | "I run a 6-person plumbing sub in Charlotte doing new multifamily. I use PlanSwift on an old Windows laptop and Excel for pricing. Is it worth switching to STACK or an AI takeoff tool for fixture counts and pipe runs?" | compare | Active/deciding | Exploratory | Cold | ChatGPT | PlanSwift vs STACK; AI plumbing takeoff 2026; reviews; price | 3 |
| F4 | "HVAC contractor, 20 guys, Columbus, Ohio — we're starting to bid data-center and warehouse mechanical packages. Can AI takeoff accurately measure duct and count diffusers from mechanical drawings, or will I miss scope?" | validate | Active | Exploratory | Cold | ChatGPT, Perplexity | AI HVAC takeoff accuracy; duct takeoff software 2026; reviews; Togal/Beam HVAC | 2 |
| F5 | "Bid is due Thursday 2 pm — 42 electrical sheets for a 60,000 sq ft school in Sacramento, prevailing wage. I don't have time. Who can do an electrical takeoff for me by Wednesday and what does it cost?" | do (outsource) | Active | **Acute** | **Hot** | Google AI Mode, ChatGPT | electrical takeoff services; estimating services California; price per sheet; Beam AI; fast turnaround | 3 |
| F6 | "I've done takeoffs on paper with highlighters for 20 years at my low-voltage company in Tampa (8 techs — structured cabling, access control). Do I actually need software or can I stay with Excel?" | learn (habit) | First thought | Exploratory | Cold | ChatGPT | low voltage estimating software; structured cabling takeoff; is it worth it | 2 |
| F7 | "C-10 electrical contractor in San Jose, 11 employees. Does the 2025 Title 24 code change how I estimate lighting controls on commercial TI bids, and is there takeoff software that handles it?" | local / learn | Active | Recurring | Cold | AI Mode, ChatGPT | Title 24 2025 lighting controls; electrical estimating California; software | 2 |
| F8 | "Our Bluebeam Revu 20 licenses stop working at the end of this year and a subscription for 3 users isn't worth it — we only use it for counts on electrical bids. What's a cheaper takeoff option for a small electrical sub?" | ask-for-a-pick | Deciding | **Dated (Dec 31)** | Cold→hot | ChatGPT | Bluebeam alternatives takeoff 2026; Bluebeam price; Revu 20 end of life; reviews | 3 (seasonal 4) |
| F9 | "My only estimator just quit. 25-person electrical contractor in Nashville, 12 bids due this month. Hire, outsource takeoffs, or buy AI software — what does each cost?" | compare | Active | Acute | Hot | ChatGPT | estimator salary 2026; outsourced estimating cost; AI estimating software price | 3 |
| F10 | "We lost 9 of our last 10 commercial bids to GCs in Atlanta. Electrical, 10 employees. How do I tell if my takeoffs are missing scope or my labor units are too high?" | learn | First thought | Recurring | Cold | ChatGPT | bid hit rate electrical; labor units too high; scope gaps | 2 |
| F11 | "Fire alarm contractor in Dallas, 7 people. We count smokes, pulls and horn/strobes by hand on FA plans and quote in Excel. Is there takeoff software that recognizes fire alarm symbols?" | ask-for-a-pick | Active | Recurring | Cold | ChatGPT, Perplexity | fire alarm takeoff software; Countfire; symbol recognition | 2 |
| F12 | "Has anyone used Quotr for electrical takeoffs? 5-person shop in Sacramento — I'd run the 7-day trial on a real bid this weekend. Will it handle scanned PDF plans?" | validate | Deciding | Acute | Hot | ChatGPT, Google | Quotr reviews; Quotr.ai pricing; Quotr vs Togal; AI takeoff scanned PDF accuracy | 1 (brand) |

**Short category prompts**

| ID | Prompt | Intent | Stage | Tier (est.) |
|---|---|---|---|---|
| S1 | best electrical estimating software for small contractors | pick | Active | 4 |
| S2 | AI takeoff software for electrical contractors | pick | Active | 3 |
| S3 | plumbing takeoff software 2026 | pick | Active | 3 |
| S4 | HVAC duct takeoff software | pick | Active | 2 |
| S5 | low voltage estimating software | pick | Active | 2 |
| S6 | outsource electrical takeoff cost | do/price | Active | 2 |

**Brand prompts (track separately)**

| ID | Prompt | Intent | Tier (est.) |
|---|---|---|---|
| B1 | Quotr vs PlanSwift | compare | 1 |
| B2 | is Quotr.ai legit / Quotr reviews | validate | 1 |
| B3 | Quotr vs Togal for electrical takeoff | compare | 1 |

Tier scale (estimate): 5 = head category with directory pages; 1 = brand-only. Assigned from observed directory/listicle density in retrieval, not volume.

### Gaps
- No Google volume, GSC impressions or Profound panel lookups; tiers must be re-scored with Quotr's Search Console (5+-word queries) and Ahrefs AI-adjusted volume (Google × 0.115 for ChatGPT).

---

## O. Simulation of the AI search journey

### Takeaway
The simulated persona reaches a shortlist of STACK, PlanSwift, ConEst/Accubid/McCormick and Togal without Quotr; real retrieval runs this session show **Quotr absent from 9 of 10 retrieval sets**, present only when the query is an AI-accuracy how-to (its own blog post). Review directories own every "reviews" node, vendor listicles from service-software firms own "best for small contractors", and old Mike Holt threads own the peer node.

### Cited Findings
**O.2 Retrieval proxy (WebSearch result sets, 2026-11-06) — "retrieval proxy, not an AI engine answer"**

| # | Query run (fan-out node it proxies) | Top domains returned | Brands named in results/summary | Quotr? | Winning format |
|---|---|---|---|---|---|
| R1 | small-shop electrical estimating software, Accubid too expensive (≈ "best electrical estimating software small contractors 2026") | sourceforge.net, buildops.com ×2, sparkquote.ai ×2, thejobquote.com, electricaltakeoffsoftware.com, fieldtechreviews.com, softwareworld.co ([SourceForge](https://sourceforge.net/software/electrical-estimating/for-small-business/), [BuildOps](https://buildops.com/resources/electrical-estimating-software-for-small-contractor), [SparkQuote](https://sparkquote.ai/guides/best-electrical-estimating-software-small-contractors), [SoftwareWorld](https://www.softwareworld.co/electrical-estimating-software-for-small-businesses/)) | Accubid, Trimble Estimation MEP, TurboBid, STACK, PlanSwift, SparkQuote | **No** | Vendor-owned 2026 listicles + directories |
| R2 | r/electricians estimating software small shop (≈ "reddit best estimating software electrician") | electricaltakeoffsoftware.com, forums.mikeholt.com ×8, one spam page | National Electrical Estimator, Electrical Bid Manager, others | No | Forum threads (Reddit not returned) |
| R3 | Mike Holt small electrical estimating software (≈ peer recommendation node) | forums.mikeholt.com ×9 ([example](https://forums.mikeholt.com/threads/best-bid-software.2586877/)) | Best Bid, Electrical Bid Manager, ConEst IntelliBid/SureCount, Accubid, McCormick, TurboBid, Red Rhino | No | Forum threads (many 10–15+ years old) |
| R4 | PlanSwift reviews cons (≈ "PlanSwift reviews") | capterra.com + 10 regional Capterra domains | PlanSwift | No | Review directory |
| R5 | ConEst IntelliBid reviews cons (≈ "ConEst reviews") | softwareadvice.com, capterra ×8, sourceforge, **mccormicksys.com** (competitor-written "ConEst review") | ConEst, McCormick | No | Directory + competitor-authored review page |
| R6 | Togal.AI reviews cons (≈ "Togal reviews") | g2.com ×8 (reviews, pricing, features, compare, alternatives), trustpilot ×2, capterra alternatives, b2bsalestools, plus off-topic results | Togal, Procore, Autodesk Forma | No | Review directory |
| R7 | STACK reviews cons price increase (≈ "STACK price increase") | Capterra only (16 results across capterra.com and 7 regional Capterra domains) | STACK | No | Review directory |
| R8 | Bluebeam price increase / perpetual end (≈ "Bluebeam price 2026", "Revu 20 end of life") | costbench, microsolresources (reseller), drawboard (competitor), thepricer, tomshardware forum, arkance, atgusa, novedge, softabase | Bluebeam, Drawboard | No | Reseller/competitor pricing explainers |
| R9 | AI takeoff electrical symbol accuracy (≈ "is AI takeoff accurate electrical") | aginera.ai, **quotr.ai**, aiinsightsnews.net, g2 (Drawer AI), businesswire (eTakeoff), togal, ycombinator | Aginera, Drawer AI, eTakeoff, Togal, **Quotr** (its post [how to estimate electrical work from drawings](https://quotr.ai/blog/how-to-estimate-electrical-work-from-drawings-conduit-devices-labor/) was result #2) | **Yes (owned page)** | Vendor how-to blogs |
| R10 | Prior Perplexity run C6 "best takeoff software for electrical contractors" (2026-09-25, from repo) | buildops, getapp, softwareadvice, capterra, countfire, mccormicksys, trimble, bluebeam, servicetitan, stackct, constructionbids.ai | ConEst IntelliBid, Countfire, PlanSwift, Trimble AccuBid, McCormick | No (Quotr's best-electrical post not retrieved) | Directories + vendor trade pages — `quotr_ai_visibility_tests.md` §1 |

### Inferences
**O.1 SIMULATED ChatGPT conversation (not a real transcript; responses modeled on R1–R10 retrieval patterns)**

*Persona: Dave, 47, owner of an 11-person electrical contractor in Sacramento, CA (C-10). Wife Lisa runs the office and helps count devices. Bids TI and light commercial from BuildingConnected and PlanHub; 3 Bluebeam Revu 20 licences + Excel with labour units copied from an old NECA manual. Tuesday, 10:47 pm, three bids due this week.*

1. **Dave:** "im doing takeoffs till midnight again, 3 bids due this week. is there a faster way to count outlets and lights off pdf plans without hiring an estimator"
 **ChatGPT (simulated):** explains Bluebeam count tool/Visual Search, then "dedicated takeoff software" (PlanSwift, STACK) and "AI takeoff" (Togal.AI, Beam AI, Kreo); suggests outsourcing for crunch weeks. *Fan-out likely:* "AI electrical takeoff software 2026", "Bluebeam visual search count symbols".
2. **Dave:** "does the AI stuff actually work on electrical plans or do i have to recount everything"
 **ChatGPT (simulated):** "works best on clean vector PDFs; struggles with scans and non-standard symbols; always check legend vs fixture schedule"; cites vendor blogs (Aginera, possibly Quotr's how-to as a *fact source*, not named). *Fan-out:* "AI takeoff accuracy electrical symbols", "AI takeoff reviews reddit".
3. **Dave:** "ok what should a 11 person electrical company buy, under $150 a month, we're on bluebeam revu 20 which dies dec 31"
 **ChatGPT (simulated):** shortlist = ConEst IntelliBid/SureCount, McCormick, Accubid ("pricier, quote-based"), Trimble Estimation MEP ($1,950/yr), STACK, PlanSwift, Kreo (cheap AI); notes Bluebeam subscription option. Quotr absent (not on directories/listicles in R1/R10). *Fan-out:* "best electrical estimating software small contractors 2026 price", "Bluebeam Revu 20 end of life".
4. **Dave:** "stack vs planswift vs togal for electrical, which one won't screw me on price"
 **ChatGPT (simulated):** pulls Capterra/G2 alternatives pages (R4–R7): STACK cloud but renewal-price complaints; PlanSwift desktop/Windows; Togal $299/mo AI. *Fan-out:* "STACK price increase reviews", "PlanSwift vs STACK", "Togal pricing".
5. **Dave:** "anything newer and cheaper that does the counting with AI and lets me cancel monthly"
 **ChatGPT (simulated):** Kreo, Easy Takeoffs, possibly Quotr if its pricing page is retrieved via `site:` fan-out with correct $79.90 price; risk it repeats stale $299.90 pricing (repo finding).
6. **Dave:** "give me a shortlist of 3 i can try this weekend"
 **ChatGPT (simulated):** "STACK (free tier), Kreo (cheap AI), ConEst IntelliBid (electrical-specific)". Quotr appears only if steps 3–5 retrieved a third-party page naming it.

**O.3 Gap verdict per prompt cluster**

| Cluster | Who owns retrieval | Quotr status | Verdict | Fastest lever |
|---|---|---|---|---|
| "Best electrical estimating software for small contractors" (S1, F2) | Vendor listicles (BuildOps, SparkQuote, ElectricalTakeoffSoftware), SourceForge, SoftwareWorld, Capterra | Absent (R1, R10) | **Gap — winnable** (thin, vendor-conflicted pool) | Free SourceForge listing; Capterra listing + reviews; SoftwareWorld inclusion; refresh owned post with correct price |
| "[Incumbent] reviews / price increase / alternatives" (F3, F8, M5–M6) | Capterra, G2, Software Advice, Trustpilot; competitor-authored review pages (McCormick on ConEst) | Absent (R4–R8) | **Gap — partially winnable** | Directory profile so Quotr shows on "alternatives"; honest "X review for small electrical shops" pages (McCormick precedent) |
| Peer recommendation ("reddit/forum best software") | Mike Holt threads (old), r/estimators | Absent (R2–R3) | Slow (3–12 months) | Disclosed estimator participation; answer old threads with new posts |
| AI accuracy / how-to (F4, M2) | Vendor how-to blogs | **Present via owned post** (R9) | **Strength — convert** | Add method/data; write brand into key steps so it is *named*, not just cited |
| Bluebeam Revu 20 EOL (F8) | Resellers, competitor Drawboard | Absent (R8) | **Time-boxed gap** (8 weeks) | Publish dated EOL decision page now |
| Outsource takeoff now (F5) | Estimating-service firms (repo: blazeestimating, 1800estimating) | Quotr post cited, not named (repo) | Gap — price-fit problem | Per-sheet/per-trade crunch price |
| Low-voltage / fire-alarm (F6, F11, S5) | Not run (budget) | Unknown | Likely gap (Countfire UK-focused per repo) | Trade page depth + symbol set proof |

### Gaps
- Planned dedicated fan-out runs not executed (search budget exhausted): "best HVAC takeoff software 2026", "plumbing takeoff software small subcontractor 2026", "low voltage takeoff software", "fire alarm takeoff software", "outsource electrical takeoff cost per sheet", "Quotr vs PlanSwift", "Bluebeam Revu 20 end of life alternatives". No ChatGPT/AI Mode answers were run; R1–R9 are web-search retrieval only.

---

## P. GEO system for this ICP

### Takeaway
Build one MEP-sub hub, two urgent-mode pages (bid-tonight; Revu 20 EOL), four considered decision pages, six answer pages and two geo/topical pages; fix stale pricing first; create two proof assets (accuracy benchmark, small-sub estimating survey); then spend off-site hours on directories (Capterra/G2/SourceForge), listicle inclusion, and disclosed forum participation, tracking 8 frozen prompts on ChatGPT + Google AI Mode as cluster-level distributions.

### Cited Findings
- Product/pricing/spec pages lead GPT-5.6 retrieval (16.4%) while listicles fell to 8.2% — owned factual pages are back in scope — [Peec](https://docs.peec.ai/research/gpt-56-product-pages-vs-listicles) (via framework)
- Self-ranked listicles: 69% did not get their own brand recommended; brands lost 29–49% traffic after self-ranked lists — [Something Inc.](https://somethinginc.com/blog/2026-ai-citation-data-review/); [Position Digital](https://www.position.digital/blog/listicle-outreach-guide/) (via framework)
- Evidence density lifts share of answer (quotations +40.9%, statistics +30.6%) — [arXiv 2311.09735](https://arxiv.org/abs/2311.09735); retrieval explains 32% of citation variance vs page properties 2.8% — [arXiv 2610.15033](https://arxiv.org/abs/2610.15033) (via framework)
- Freshness: median citation half-life ~4.5 weeks; 75% of cited pages updated within a year — [NoGood](https://nogood.io/blog/content-freshness-ai-citations/) (via framework)
- Branded web mentions correlate 0.664 with AI Overview visibility vs backlinks 0.218 — [Ahrefs](https://ahrefs.com/blog/ai-overview-brand-correlation/) (via framework)
- Measurement: 50 prompts daily beats 10 prompts 5×/day; treat changes as real only if they persist 3 periods — [Peec](https://peec.ai/blog/the-key-to-prompt-tracking); [Texta](https://www.texta.ai/blog/answer-variability-study-why-chatgpt-gives-different-answers) (via framework)
- Recurring third-party pages that drive takeoff answers (constructioncoverage, TDPM, ConstructConnect guide, G2/Capterra alternatives, SourceForge AI takeoff) and no Quotr presence on them — `quotr_ai_visibility_tests.md` §5
- Existing Quotr MEP assets: trade pages /software/trades/{electrical, plumbing, hvac, low-voltage, fire-protection}/; posts on electrical/plumbing/HVAC how-to, best-electrical-2026, electrical/HVAC/MEP estimating services, data-center MEP, scope gap — repo URL list (e.g., [electrical trade page](https://quotr.ai/software/trades/electrical/), [low-voltage](https://quotr.ai/software/trades/low-voltage/), [fire-protection](https://quotr.ai/software/trades/fire-protection/))

### Inferences
**P.1 Owned pages (create = new; optimize = existing URL)**

| Type | Mode | Proposed title | Slug | Create/optimize | Serves |
|---|---|---|---|---|---|
| Hub | Both | AI Takeoff & Estimating for Small Electrical, Plumbing, HVAC and Low-Voltage Subs (3–30 people) | /software/mep-subcontractors/ | Create | J1–J5; links trade pages |
| Urgent | **Hot** | Bid Due Tomorrow? Get Device and Fixture Counts From Your PDFs Tonight | /software/mep-subcontractors/bid-due-tomorrow/ | Create | M1, F1, F5 (lead: 3 steps, trial now, Service turnaround, one proof number) |
| Urgent (dated) | Cold→hot | Bluebeam Revu 20 End of Life (Dec 31, 2026): Takeoff Options for Small Electrical Subs | /compare/bluebeam-revu-20-end-of-life-takeoff-options/ | Create **now** | M5, F8 (refresh Dec 1, Dec 20, Jan 5) |
| Decision | Cold | Best Electrical Estimating Software for Small Contractors (2026 → 2027): Prices, Labor Units, Trials | /blog/best-electrical-estimating-software-2026/ | **Optimize** (fix stale price; add small-shop table; honest picks incl. ConEst/McCormick/STACK; do not self-rank #1) | S1, F2 |
| Decision | Cold | Hire an Estimator vs Outsource Takeoffs vs AI Software: Cost per Bid for a 5–30 Person Sub | /pricing/cost-per-bid-calculator/ | Create | M4, F9 (BLS wage, Service per-sq-ft, Lite) |
| Decision | Cold | Quotr vs PlanSwift vs STACK for Electrical Takeoff: Price, Lock-in, Export, Accuracy | /compare/quotr-vs-planswift-vs-stack-electrical/ | Create (consolidate older vs posts) | B1, F3, M6 |
| Decision | Cold | Quotr Pricing, Cancellation and Data Export — Plain Answers | /pricing/ (FAQ block) | Optimize | Anxiety Q2–Q3; B2 |
| Answer | Cold | Can AI Count Electrical Symbols Accurately? Our Test on N Public Bid Sets (Vector vs Scanned) | /blog/ai-electrical-takeoff-accuracy-test/ | Create (from proof asset 1) | M2, F4, F12 |
| Answer | Cold | Legend vs Fixture Schedule Mismatches: The Scope Gap That Sinks Electrical Bids | /blog/electrical-scope-gaps-legend-vs-schedule/ | Create (link /blog/scope-gap-construction/) | M3, F10 |
| Answer | Cold | Electrical Estimating: Per Opening vs Per Square Foot vs Labor Units | /blog/electrical-estimating-per-opening-vs-per-square-foot/ | Create (planned L-092) | F2, F10 |
| Answer | Cold | Fire Alarm Takeoff From PDF Plans: Counting Initiating and Notification Devices | /blog/fire-alarm-takeoff-from-pdf/ | Create | F11 |
| Answer | Cold | Low-Voltage Takeoff: Drops, Cable Footage and IDF Counts From Plans | /blog/low-voltage-takeoff-structured-cabling/ | Create | F6, S5 |
| Answer | Cold | HVAC Duct and Diffuser Takeoff From Mechanical Plans with AI | /blog/how-to-estimate-hvac-sheet-metal-mechanical-plan/ | Optimize (add AI accuracy section) | F4, S4 |
| Geo | Cold | California Electrical Estimating: Title 24 (2025) Lighting Controls and Prevailing Wage | /blog/california-electrical-estimating-title-24-prevailing-wage/ | Create (verify code facts) | G1, F7 |
| Topical geo | Cold | How to Estimate Prevailing-Wage Electrical Work (Davis-Bacon and State Rates) | /blog/prevailing-wage-electrical-estimate/ | Create | G4, F5 |
| Spoke | Cold | Data-Center Electrical and Mechanical Takeoffs for Small Subs | /blog/data-center-construction-estimating-mep-subcontractor-choke-point/ | Optimize | G2, M7 |

Format rules (framework): 40–60-word answer first under each H2; one sourced stat per ~150 words; dated update line; named estimator reviewer; plain HTML; tables near top; no keyword stuffing; product/pricing facts mirrored exactly across /pricing/, hub and comparison pages.

**P.2 Proof assets / original data**
1. **Public-bid-set accuracy benchmark** (10–20 publicly posted electrical/FA/LV plan sets; Quotr counts vs two human estimators; error by device type; vector vs scanned; method page + downloadable table). Highest leverage for the dominant anxiety force.
2. **"Small MEP Sub Estimating Report 2027"** (n ≥ 200 via IEC/PHCC chapters, r/estimators, customer list): hours per takeoff, % of estimating after 6 pm/weekends, bids/week, hit rate, tools used, cost of a missed scope item. No such survey was found in this research — pitchable to ECmag/EC&M/ACHR News.
3. **RL Electric case with numbers** (hours, bids/week before/after, a quote from the owner) on /case-studies/rl-electric/ + YouTube chapters.
4. **Revu 20 EOL cost calculator** (seats × subscription vs alternatives) — time-boxed to Q4 2026.
5. **60–90-sec "count a real sheet" videos** per trade (electrical, FA, LV, plumbing, HVAC).

**P.3 Off-site placements ranked by leverage per hour (estimates)**

| Rank | Placement | Why (evidence) | Effort |
|---|---|---|---|
| 1 | **Capterra/GetApp/Software Advice** single listing + 10–20 reviews from MEP customers (RL Electric first) | Directories own every "reviews/alternatives" node (R4–R7, R10) | 4–8 h + review asks |
| 2 | **G2** profile under "Quotr.ai" + reviews | G2 alternatives pages recur in citations (repo) | 3–6 h |
| 3 | **SourceForge** free listing in "electrical estimating for small business" and "AI takeoff" | Appeared in R1 and C1 retrieval | 1–2 h |
| 4 | **SoftwareWorld** small-business electrical estimating list | Appeared in R1 | 1–2 h outreach |
| 5 | **constructioncoverage.com, TDPM, ContraVault, ConstructionPlacements** list inclusion (paste-ready 40–60-word blurb, correct price) | Recur in 6–7 Perplexity prompts (repo) | 2–6 weeks, 3–5 h |
| 6 | **Mike Holt forum / Electrician Talk** disclosed estimator participation (answer small-shop software threads with practical advice, signature disclosure) | Forum threads own peer node (R2–R3) | 2 h/week, 3–12 months |
| 7 | **r/estimators, r/electricians** (9:1 rule; no new-account promotion) | r/estimators cited in 6/32 prompts (repo) | 1–2 h/week, 3–6 months |
| 8 | **ECmag "Your Business" / EC&M / ACHR News** contributed data story from proof asset 2 | Trade press carries estimating columns (cited) | After survey |
| 9 | **YouTube**: chaptered long-form trade demos + RL Electric | YouTube matters for Google AI surfaces (framework) though 0 Perplexity citations (repo) | 4–6 h/video |
| 10 | **Associations** (IEC chapter webinar on "AI takeoff accuracy", PHCC/ACCA, BICSI for LV) | Trust for cold mode (inference) | Quarterly |

**P.4 Refresh cadence:** pricing, comparison, Revu-EOL and "best" pages monthly (EOL page twice in December); hub and answer pages quarterly; accuracy benchmark annually with a dated re-run; survey annually.

**P.5 Tracking prompts to freeze (ChatGPT + Google AI Mode; 3–5 runs/week; report cluster-level mention/citation/recommendation/SoV vs STACK, PlanSwift, ConEst, Togal, Kreo with ± ranges)**
1. best electrical estimating software for small contractors (S1)
2. AI takeoff software for electrical contractors (S2)
3. F1 full-context (Fort Worth, 9-person, nights, PlanHub, Bluebeam)
4. F8 full-context (Revu 20 EOL, 3 users, electrical counts) — retire after Q1 2027
5. plumbing takeoff software for small subcontractors (S3 variant)
6. fire alarm / low voltage takeoff software (F11/S5 merged)
7. outsource electrical takeoff cost (S6)
8. Quotr vs PlanSwift (B1, brand group — reported separately)

**P.6 Do / skip / ignore**
- **Do:** fix stale $299.90 pricing everywhere first; accuracy benchmark; directory listings + reviews; Revu-20 EOL page this month; cost-per-bid calculator; honest comparison pages with export/cancel facts; California + prevailing-wage pages; disclosed forum presence; RL Electric numbers; per-sheet/per-trade crunch pricing test for Service.
- **Skip:** 50 state pages; a self-ranked "best" list putting Quotr #1; schema/llms.txt as levers; generic "thousands of contractors" claims; Reddit astroturfing; reproducing NECA MLU tables (copyright — training knowledge).
- **Ignore (for this ICP):** Claude/Copilot/Grok tracking; residential-service HVAC/plumbing (ServiceTitan market); procurement messaging (finish materials are not this buyer's job).

### Gaps
- Effort hours are estimates; Quotr's capacity, current review count and Capterra status need confirmation; whether Service can price per sheet/trade is unknown (TO CONFIRM with Quotr).

---

## Q. Known / likely / speculative

### Takeaway
Sizing and the anxiety-dominant force picture are reasonably grounded; geography, timing patterns, channel sizes and prompt wording remain hypotheses that switch interviews, CBP pulls and real engine runs must confirm.

### Cited Findings
- See sections A–P for the source of each "Known" item.

### Inferences
| Claim class | Known (cited) | Likely (strong inference — label it) | Speculative (validate first) |
|---|---|---|---|
| Size | 83,342 electrical (238210) and 111,207 plumbing/HVAC (238220) employer establishments, ~1.0M and ~1.2M employees (2023 CBP via aggregators); 159,693 electrical nonemployers; avg ~11–12 employees | Median establishment <10 employees; low-voltage/FA partly in 238210 | 25k–45k plan-bidding target firms; revenue $0.6M–7.5M band |
| Geography | AGC: 2026 demand soft except data centers/power; input costs +7.1–8.9% | California hub justified (home market, Title 24, prevailing wage); one data-center spoke | Specific corridor states/metros; Sun Belt growth ranking; NEC/Title 24/prevailing-wage specifics (training knowledge) |
| Psychology | Accuracy (57%) and security (54%) top AI concerns; AI use 52% of firms; replication ranking of biases | Owner identity, solo/spouse decisions, hot weeknights before bid day, buy-once preference | Exact hot hours; spouse participation rate; trial-length effect |
| Forces | Price/lock-in/billing/friction complaints in STACK, ConEst, PlanSwift reviews; Bluebeam licence/price changes; Revu 20 EOL Dec 31 2026 (single source) | Anxiety is the dominant restraining force; habit = $30 tools + Bluebeam + Excel | Frequency ranking (n = 22 snippets) |
| Price | Budgets $1,600–4,000/yr; small shops $60–299/mo; competitor price points; Quotr Lite $79.90, 7-day trial | Lite is below every anchor; stale pricing hurts | Service $0.25/sq ft mis-fits subs (needs Quotr confirmation) |
| AI visibility | Quotr absent from 9/10 retrieval sets here and from C6; present only via own AI-accuracy how-to; directories own reviews nodes | Directory listings + reviews are the cheapest unlock | Specific mention-rate gains or timelines |
| Prompts | Fan-out injection rates; pick prompts 22.8% vs 8.0% | The 12 full-context prompts represent real chains | Demand tiers (no volume data) |

### Gaps
- Biggest evidence holes, in order: (1) switch interviews with recent MEP sign-ups/churns; (2) CBP size-class and state pulls; (3) Reddit verbatims and subreddit sizes; (4) real ChatGPT/AI Mode runs of the frozen prompts; (5) Quotr's own trial timestamps by hour/day and trade.
