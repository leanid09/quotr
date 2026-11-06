# ICP 3 — Owner / estimator at an area & finish-trade subcontractor (drywall & metal framing, acoustical ceilings, flooring, tile, painting, roofing, siding, insulation, concrete flatwork): psychology, search behavior and a GEO system for Quotr.ai

**As of:** 2026-11-06. **Scope:** US. **Method:** the ICP-depth GEO framework (coding chain trigger → stage → hot/cold mode → restraining force → prompt → proof; four forces; switch timeline; prompt matrix; geography-to-segment pipeline; measurement as distributions), built on top of the existing geo-brain (personas, trade question bank, competitor map, Sept-2026 Perplexity visibility tests).

**Labels used throughout:** [K] known (measured, cited) · [L] likely (strong inference) · [S] speculative (hypothesis to validate) · [EST] researcher estimate · [SIM] simulated · [DESIGN] recommendation · [CALC] arithmetic on cited numbers.

**Research-environment limits (read before using):** In this session WebFetch was blocked for every host tried (census.gov, eyeonhousing.org, contractortalk.com, capterra.com; the Census and BLS APIs returned proxy 403s), reddit.com is not accessible to the search user agent, and the shared WebSearch budget for this turn ran out after 14 searches. So: (1) firm counts come from third-party restatements of Census CBP, not from data.census.gov; (2) "verbatim" review text is the fragment the search index surfaced — the page itself was not opened, so re-check wording before publishing; (3) Reddit/ContractorTalk wording is limited to thread titles (verbatim) already logged with URLs in the geo-brain; (4) only 4 fresh retrieval-proxy searches ran, so section O also reuses the dated 2026-09-25 Perplexity runs from the repo, labeled as such. Existing repo work is built on, not repeated: see `geo-brain/04-prompt-library/buyer-questions-by-trade.md` (trade questions, units, pains), `geo-brain/03-market/competitor-landscape.md`, and `research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md`.

---

## A. Definition and size: how many of these firms exist, how big they are, and how Hispanic the owner and worker base is

### Takeaway
The ICP is a population of tens of thousands of small employer firms per trade: roughly 25,500 roofing and 20,800 drywall/insulation establishments with paid employees in 2023 (about 8–12 employees each on average), plus a large non-employer tail. Construction is the #1 sector for Hispanic-owned employer firms (70,571 firms in 2021), and the field workforce in exactly these trades is majority Hispanic (drywall ~68–75%, roofing ~64%, painting ~62%), so bilingual owners and Spanish-first crews are a structural feature of the ICP, not a niche.

### Cited Findings
**Firm counts (Census County Business Patterns, CBP)**

| NAICS | Trade | Establishments with paid employees | Employees | Year | Source / caveat |
|---|---|---|---|---|---|
| 238310 | Drywall & insulation (incl. acoustical ceilings, plaster) | **20,760** | **250,758** | CBP 2023 | [Vantage Insights restating CBP 2023](https://vantainsights.com/industry/238310-drywall-insulation-contractors) — third-party; not checked on data.census.gov |
| 238160 | Roofing | **25,519** (up from 24,532 in 2022) | **215,242** | CBP 2023 | [The Roofing Brief, US roofing contractor count](https://theroofingbrief.com/us-roofing-contractor-count-report/) (several sites cite the same CBP figure) |
| 238160 | Roofing (all "business entities", different measure) | 59,589 | — | undated | [naics.com six-digit table](https://www.naics.com/six-digit-naics/?code=23) — not comparable with CBP; likely includes non-employer firms |
| 238330 | Flooring | 12,626 "US business entities" | — | undated | [naics.com](https://www.naics.com/six-digit-naics/?code=23) — not a CBP figure; unverified |
| 238320 / 238340 / 238110 / 238170 | Painting / tile & terrazzo / poured concrete / siding | not retrieved | — | — | Gap (see below) |

- CBP 2023 was released June 26, 2025 and reports establishments, employment (week of March 12) and payroll at national, state, metro, county and ZIP level — [Census Bureau release](https://www.census.gov/newsroom/press-releases/2025/2023-county-business-patterns.html); table [CB2300CBP](https://data.census.gov/table/CBP2023.CB2300CBP).
- [CALC] Average size: drywall/insulation 250,758 ÷ 20,760 ≈ **12.1 employees per establishment**; roofing 215,242 ÷ 25,519 ≈ **8.4**. Roofing establishments grew (25,519 − 24,532) ÷ 24,532 ≈ **+4.0%** from 2022 to 2023.

**Hispanic ownership (Census Annual Business Survey, ABS)**
- Construction was the top sector for Hispanic-owned employer businesses: **70,571 firms** (2021 reference year, ABS 2022), out of **406,086** Hispanic-owned employer firms in total — [Census Bureau story, Oct 2024](https://census.gov/library/stories/2024/10/hispanic-owned-businesses.html) (via search summary). [CALC] 70,571 ÷ 406,086 ≈ **17.4%** of Hispanic-owned employer firms are in construction.
- For the 2017 reference year the construction figure was **50,187 firms (15.6%)** — via search summary of a Census-based profile, [Morris County EDC](https://morriscountyedc.org/a-profile-of-the-nations-hispanic-owned-businesses-construction-sector/) (attribution of this specific number to that page is uncertain). [CALC] 50,187 → 70,571 is **+41%** in four years.
- Trade press covered the same ABS trend for roofing: "Census Data Shows Increase in Latino Business Ownership" — [Roofing Contractor](https://www.roofingcontractor.com/articles/99026-census-data-shows-increase-in-latino-business-ownership) (title only; body not opened).

**Hispanic share of the workforce (BLS CPS–based analyses)**

| Measure | Value | Year | Source |
|---|---|---|---|
| Hispanic share of construction labor force | **32.8%** (vs 19.9% all industries) | 2024 | NAHB, via search summary — [NAHB blog Oct 2025](https://www.nahb.org/blog/2025/10/diversity-of-construction-workforce); [Eye on Housing](https://eyeonhousing.org/2025/10/hispanics-comprise-nearly-one-third-of-the-construction-labor-force/) |
| Same, latest NAHB headline | "Nearly one in three construction workers are Hispanic" | Oct 2026 | [Eye on Housing, Oct 2026](https://eyeonhousing.org/2026/10/nearly-one-in-three-construction-workers-are-hispanic/) (title only) |
| Hispanic share of construction employment | **35.4% of 12.1 million** | 2025 | [EngiMarket, BLS-based table](https://www.engimarket.com/blog/immigrant-workers-in-construction-statistics/) (secondary) |
| Hispanic share, drywall installers | **75.2%** (CPWR, 2023) / **68.5%** drywall installers & tapers (EngiMarket, 2025) | 2023 / 2025 | CPWR via [ENR (BNP digital)](https://digital.bnpmedia.com/article/SAFETY/4938139/841967/article.html) and [The Roofing Brief 2026 industry report](https://theroofingbrief.com/2026-roofing-contractor-industry-report/); [EngiMarket](https://www.engimarket.com/blog/immigrant-workers-in-construction-statistics/) |
| Hispanic share, roofers | **63.9%** (CPWR, 2023) / **64.6%** (EngiMarket, 2025) | 2023 / 2025 | same as above |
| Hispanic share, painters | **62.5%** | 2023 | CPWR via [ENR](https://digital.bnpmedia.com/article/SAFETY/4938139/841967/article.html) |
| Foreign-born share by trade | drywall & ceiling tile installers **57%**, plasterers & stucco **56%**, roofers **53%**, painters **53%**, carpet/floor/tile installers **51%**; all construction **26.3%** (record) | 2024 | [NAHB, April 2026](https://www.nahb.org/blog/2026/04/Which-States-and-Construction-Trades-Depend-the-Most-on-Immigrant-Workers); [Ahwatukee Foothills News citing NAHB](https://www.ahwatukee.com/real_estate/immigrants-comprise-big-share-of-building-trades/article_53bdfa03-87a8-45b7-be0d-f5d37b842303.html); [Construction Owners](https://www.constructionowners.com/news/immigrant-workers-hit-record-share-of-u-s-construction-workforce) |
| Other estimates | NHCA: ~30–31%, ~3.7 million workers; foreign-born drywall & ceiling installers 56.9%, painters 50.2%, roofers 50% · Hispanic Construction Council: 33.8% (2023), projected 35.2% by 2025 | 2023–2024 | [NHCA via PRWeb](https://www.prweb.com/releases/national-hispanic-construction-alliance-releases-groundbreaking-report-on-hispanics-in-construction-and-outlines-2025-policy-priorities-302394192.html); [Hispanic Construction Council](https://www.constructionowners.com/press-release/hispanic-construction-council-highlights-labor-shortage-in-2025-report) |

- Sources disagree on exact years and on Hispanic vs foreign-born definitions (do not mix the 75% Hispanic and 57% foreign-born drywall figures) — noted in the search summaries above.

### Inferences
- [L] At ~8–12 employees per establishment, the typical buyer is an owner who still estimates personally, or a firm with one estimator — the same "owner estimates after hours" pattern the geo-brain persona assumed (`audiences-and-personas.md` §3), now with a size number behind it.
- [L] The 59,589 roofing "entities" vs 25,519 employer establishments implies a non-employer/1-person tail at least as large as the employer base — buyers who will never pay for a $299/seat tool but can pay $79.90.
- [L] Hispanic ownership of construction firms (17.4% of Hispanic employer firms, growing ~41% in 4 years) plus a 64–75% Hispanic field workforce in drywall/roofing/painting means a meaningful share of owners in this ICP came up from the crew and are bilingual; Spanish is a jobsite language even where the bid to the GC is in English.

### Gaps
- CBP 2023 counts for 238320 painting, 238340 tile, 238110 poured concrete, 238170 siding and the CBP 238330 flooring figure were not retrieved (Census API/website blocked here). Pull from [CB2300CBP](https://data.census.gov/table/CBP2023.CB2300CBP) (NAICS filter) plus the CBP employment-size-class columns for the size distribution (share with <10 / 10–49 / 50+ employees).
- The share of **all** construction employer firms that are Hispanic-owned needs the ABS construction-sector denominator (ABS table "Statistics for employer firms by industry, sex, ethnicity, race and veteran status"); not retrieved. Six-digit (trade-level) Hispanic ownership is not published by ABS to my knowledge — confirm.
- Non-employer counts (Census Nonemployer Statistics) by trade not retrieved.

---

## B. Geography: where the firms and the construction starts are, priority geo segments, and whether Spanish and geo pages are justified

### Takeaway
Single-family permitting is led by Houston and Dallas, then Phoenix, Atlanta, Charlotte and Austin, with Orlando and Tampa in the top 10 — the Sun Belt concentration the ICP brief assumed. Five evidence-backed segments fall out (Texas Triangle, Florida I-4 + South Florida, Phoenix/Las Vegas desert Southwest, Atlanta + Carolinas, Southern California fire-rebuild home market); geo pages are justified only where code, weather or pricing genuinely differ, and Spanish is justified as a measured pilot, not a full-site localization.

### Cited Findings
**Housing permits by metro (the demand that feeds finish-trade bid volume)**

| Metro | Single-family permits, 12 months to mid-2025 | Other 2025 figures | Source |
|---|---|---|---|
| Houston | ~30,000 (#1) | Houston and DFW each >65,000 total housing units permitted in full-year 2025; Houston #1 Jan–Feb 2025 | [GlobeSt, Sept 2025](https://www.globest.com/amp/2025/09/17/mixed-signals-for-housing-permits-as-metro-rankings-shift-again/); [Orion Property](https://www.orionprop.com/topfive/metro-phoenix-ranks-no-4-in-the-nation-for-new-home-construction/); [Construction Owners](https://www.constructionowners.com/news/texas-tops-u-s-in-single-family-home-construction) |
| Dallas–Fort Worth | ~26,000 (#2) | see above | same |
| Phoenix | 15,713 | 2025: 39,145 units incl. 24,002 single-family, down 15% YoY; metro ranked #4 for new homes | [GlobeSt](https://www.globest.com/amp/2025/09/17/mixed-signals-for-housing-permits-as-metro-rankings-shift-again/); [AZ Big Media](https://azbigmedia.com/real-estate/metro-phoenix-ranks-no-4-in-the-nation-for-new-home-construction/) |
| Atlanta | 13,731 | 11,833 (year to June 2025, other GlobeSt piece) | [GlobeSt Sept 2025](https://www.globest.com/amp/2025/09/17/mixed-signals-for-housing-permits-as-metro-rankings-shift-again/); [GlobeSt Aug 2025](https://www.globest.com/amp/2025/08/20/housing-split-between-weak-single-family-and-resilient-multifamily-construction/) |
| Charlotte | 10,879 | — | [GlobeSt Sept 2025](https://www.globest.com/amp/2025/09/17/mixed-signals-for-housing-permits-as-metro-rankings-shift-again/) |
| Austin | 9,839 | — | same |
| Orlando, Tampa Bay | in national top 10 (early 2025) | — | [Construction Owners](https://www.constructionowners.com/ca/news/texas-cities-lead-nation-in-new-home-construction-report-finds) |
| Trend caveat | Jan 2026 report: Houston 40,471, Dallas 34,778 (both down YTD), Phoenix −23% to 20,318 — period unclear | — | [GlobeSt, Jan 2026](https://www.globest.com/amp/2026/01/27/single-family-permits-decline-as-builders-adjust-to-market-challenges/) |

- Labor-side pressure in the same markets: homebuilders report struggling to find workers amid ICE crackdowns — [Axios, Sept 22, 2026](https://www.axios.com/2026/09/22/home-builders-immigrant-workers-ice); NAHB ranks states by immigrant reliance (state figures not captured) — [NAHB April 2026](https://www.nahb.org/blog/2026/04/Which-States-and-Construction-Trades-Depend-the-Most-on-Immigrant-Workers); [Homes.com summary](https://www.homes.com/news/these-states-rely-the-most-on-foreign-born-construction-workers-homebuilder-report-finds/1334299020/).
- Quotr already has a Southern California hook: a Feb 2025 paid wire release for a free LA fire-rebuild app (FireTips) — [EIN Presswire](https://www.einnews.com/pr_news/783445824/quotr-launches-la-focused-app-to-help-homeowners-get-accurate-information-rebuild-faster-after-devastating-fires) (logged in `geo-brain/02-current-state/offsite-presence.md`), and a California estimating-services post ([quotr.ai/blog/construction-estimating-services-california](https://quotr.ai/blog/construction-estimating-services-california/)).
- A competitor already localizes into Spanish: STACK runs Spanish (and French) site versions incl. a Spanish pricing page — [stackct.com/es/precios](https://www.stackct.com/es/precios/). A construction AI vendor publishes "Running a Construction Crew on WhatsApp — in Spanish" — [Velora blog](https://velora.ai/blog/construction-crew-whatsapp-spanish/) (title only).
- Framework rule: local pages are justified only where supply, pricing or regulation genuinely differ; templated city pages risk Google's scaled-content-abuse policy, which applies to AI Overviews/AI Mode — [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies) (via framework file). No engine has been shown to add the user's city to a non-local prompt spontaneously (framework file).

### Inferences
**Priority geo segments [DESIGN; evidence rows from the table above; trade mix per segment is L unless cited]**

| # | Segment | Evidence row | Dominant trades / job | Why it differs (justifies content) | Language posture |
|---|---|---|---|---|---|
| 1 | **Texas Triangle volume sub** (Houston, DFW, Austin, San Antonio) | #1, #2 and #6 SF permit metros; Houston+DFW >65k units each in 2025 | Drywall & metal framing (commercial TI + production homes), concrete flatwork, roofing (hail) | Highest bid volume; production-builder pricing per board / per SF; hail reroof cycle (L) | Bilingual owner, Spanish crew (L) — best Spanish pilot market |
| 2 | **Florida I-4 + South Florida** (Orlando, Tampa, Miami) | Orlando, Tampa in top-10 permits | Roofing (new-build + hurricane), tile/flooring (condo, multifamily), stucco/drywall | Hurricane season and Florida wind/roof code drive roofing scope (L); Togal.AI is Miami-based (competitor home turf, `competitor-landscape.md`) | Bilingual; Caribbean/South American Spanish (L) |
| 3 | **Desert Southwest** (Phoenix, Las Vegas) | Phoenix 39,145 units (24,002 SF) in 2025, −15% YoY | Drywall, stucco/plaster, concrete flatwork, tile | Slowing starts → more bids per win (price pressure trigger) (L) | Bilingual (L) |
| 4 | **Atlanta + Carolinas** (Atlanta, Charlotte, Raleigh) | Atlanta 13.7k, Charlotte 10.9k SF permits | Drywall, flooring, siding, insulation for production homes | Siding/insulation more prominent in Southeast/East production homes (L) | Mixed; growing Hispanic sub base (S) |
| 5 | **Southern California home market** (LA rebuild, Inland Empire) | Quotr's own FireTips/LA rebuild history; CA estimating-services post | Drywall, roofing, flooring, framing on rebuilds | Fire rebuild + California code (L); Quotr is Bay Area-based and can show local proof | Bilingual (L) |

- [L] Geo pages: build **trade × region pages only where facts differ** (e.g., "Roofing takeoff from plans for Florida new construction", "Texas drywall bid pricing per board, 2026 survey data", "LA fire rebuild finish-trade estimating"). Do **not** generate "drywall takeoff software Houston/Dallas/…" templates.
- [L] Spanish: justified as a **pilot** (one Spanish hub + 3 answer pages + Spanish YouTube) because the owner/worker base is heavily Hispanic and STACK already localizes; **not** justified as a full /es/ mirror until Search Console shows Spanish queries or interviews confirm Spanish-first research behavior.
- [S] Las Vegas and Raleigh belong in segments 3–4 but no permit numbers were retrieved for them.

### Gaps
- State- and metro-level CBP counts per trade NAICS (to rank where the *firms* are, not just the starts) — blocked. Method: CB2300CBP by state/MSA for 238310/238330/238340/238160/238110, normalize per 1,000 permits.
- Commercial starts by metro (Dodge) not retrieved; acoustical-ceiling and commercial drywall demand tracks commercial/TI starts, not housing permits.
- No data found on Spanish-language search or AI-assistant use by contractors (Google Trends/Keyword Planner and Search Console were not accessible).

---

## C. Jobs-to-be-done in the buyer's own words

### Takeaway
Five jobs recur across the thread titles and review language: get more bids out without night work, get quantities right (boards, squares, boxes, yards) so waste and missed scope don't eat the margin, price to win without giving the job away, look professional to the GC, and protect material margin from price spikes. Only the last one touches Quotr Procurement.

### Cited Findings
- Thread titles that state the job in the buyer's words (verbatim titles, URLs logged in `buyer-questions-by-trade.md`): "Newbie… How to bid drywall jobs" ([ContractorTalk](https://www.contractortalk.com/threads/newbie-how-to-bid-drywall-jobs.274761/)); "Old drywaller, new estimator" ([ContractorTalk](https://www.contractortalk.com/threads/old-drywaller-new-estimator.9091/)); "Total squares for bid? How do you guys come up with your total?" ([ContractorTalk](https://www.contractortalk.com/threads/total-squares-for-bid-how-do-you-guys-come-up-with-your-total.37342/)); "How much extra LVP do I really need?" ([r/Flooring](https://www.reddit.com/r/Flooring/comments/1dnye47/how_much_extra_lvp_do_i_really_need_currently/)); "Siding installation: charge by square or by job?" ([ContractorTalk](https://www.contractortalk.com/threads/siding-installation-charge-by-square-or-by-job.148615/)); "New construction flatwork price?" ([ContractorTalk](https://www.contractortalk.com/threads/new-construction-flatwork-price.88489/)); "Commercial tile install per SF price" ([ContractorTalk](https://www.contractortalk.com/threads/commercial-tile-install-per-sf-price.125029/)); "Best takeoff software for a drywall contractor?" ([r/estimators](https://www.reddit.com/r/estimators/comments/1gl3bi8/best_takeoff_software_for_a_drywall_contractor/)).
- Speed is the pull users describe: a PlanSwift reviewer said the tool turned "a task that was several hours in the making, to minutes" — [Capterra PlanSwift reviews](https://www.capterra.com/p/70808/PlanSwift/reviews/) (fragment surfaced by search index).
- Material escalation is now a bidding job: in AGC's January 2026 survey 40% of contractors raised bid prices because of tariffs and 32% bought early; input costs rose 8.9% Aug 2025→Aug 2026 (AGC via the geo-brain, not re-opened) — [AGC Jan 2026](https://www.agc.org/news/2026/01/14/construction-costs-rise-fastest-rate-january-2023-november-outpacing-increases-contractors-bid); [AGC Sept 2026](https://www.agc.org/news/2026/09/10/construction-input-costs-climb-89-between-august-2025-and-august-2026-association-survey-finds-war).

### Inferences
JTBD statements [DESIGN — synthesized from the cited titles; validate verbatim in switch interviews]:

| # | Job (buyer phrasing) | Trades | Quotr line |
|---|---|---|---|
| J1 | "Turn 20 bid invites a week into the 5 I can actually price, and get them out before the GC's deadline without doing takeoffs at 2 a.m." | All, esp. drywall, ceilings, flooring | Software (AI area/symbol detection); Service for overflow |
| J2 | "Get my boards / squares / boxes / yards right the first time, so I don't eat the waste or a wall type I missed." | Drywall, roofing, flooring, tile, concrete | Software (area detection, editable takeoff, confidence flags) |
| J3 | "Know what to charge per board, per square, per SF in *my* market so I win without giving the job away." | All | Software cost database by ZIP (claimed on /software/) + original price data |
| J4 | "Send the GC a clean, itemized bid with exclusions that looks like the big guys made it." | All commercial-facing | Software (bids/proposals) |
| J5 | "Lock material cost before the price jumps — or buy direct so my supply-and-install margin survives tariffs." | Flooring, tile, (cabinets for remodel-oriented subs) | Procurement (flooring listed; tile TO CONFIRM) |

### Gaps
- No interview verbatims exist yet for this ICP; the "20 invites → 5 bids" framing is the brief's hypothesis, not a measured bid volume. No published source on finish-sub bid volume or hit rate was found.

---

## D. Psychology: identity, risk, price posture, trust in tech, language, hot vs cold moments, and which biases matter

### Takeaway
This buyer is a field-born, loss-averse, price-anchored owner who distrusts AI accuracy and decides fast only under bid-day pressure; design around robust effects (defaults, anchoring, temporal landmarks, time pressure) and ignore fragile ones (generic social proof, choice overload).

### Cited Findings
- Identity / field origin: "Old drywaller, new estimator" ([ContractorTalk](https://www.contractortalk.com/threads/old-drywaller-new-estimator.9091/)) and "Newbie… How to bid drywall jobs" ([ContractorTalk](https://www.contractortalk.com/threads/newbie-how-to-bid-drywall-jobs.274761/)) show estimators coming from the crew without formal estimating training.
- Price posture: typical construction software budget about **$1,600–$4,000 per year** — [Capterra buyer insight](https://www.capterra.com/resources/construction-software-buyer-insight/) (undated, likely 2024–25). GetApp's PlanSwift summary: "upgrade fees, recurring payments, and limited payment flexibility can make it expensive for smaller businesses" — [GetApp PlanSwift](https://www.getapp.com/all-software/a/planswift/) (search-index fragment). STACK reviewers describe price rising at each renewal and no multi-user discount — [Capterra STACK reviews](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/) (search summary, paraphrase).
- Trust in tech: data accuracy is contractors' #1 AI worry (57%), security 54% — [Dodge/CMiC via Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/); construction leaders' trust in AI fell 14 points YoY — [Autodesk State of Design & Make](https://www.autodesk.com/blogs/construction/state-of-design-make-spotlight-construction/) (both via geo-brain, not re-checked). r/estimators threads call AI takeoff "hit-or-miss" — [r/estimators](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/) (via Perplexity summary in the repo audit).
- AI adoption is rising anyway: 52% of construction firms use AI for business tasks (+20 pts vs 2025), 80% of users daily (Houzz, 601 firms, June–July 2026) — [Roofing Contractor](https://www.roofingcontractor.com/articles/102644-ai-use-jumps-among-construction-firms-houzz-survey-finds); 24% of commercial specialty contractors use AI for estimating, 22% for bid management — [ServiceTitan 2026](https://www.servicetitan.com/press/servicetitan-report-finds-ai-adoption-more-than-doubles-among-commercial); 51% of B2B software buyers start research in an AI chatbot (G2, interested party) — [G2 via PR Newswire](https://www.prnewswire.com/news-releases/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots-302742807.html).
- Verification behavior: 86% of US shoppers who used AI for product research verified elsewhere; trust in AI alone falls from 42% under $50 to 5% over $500 — [MarTech](https://martech.org/the-ai-shopping-stats-2026-what-you-need-to-know/) (via framework file).
- Bias replication ranking (via framework file): **robust** — defaults/status quo d = 0.68 ([Jachimowicz et al. 2019](https://ideas.repec.org/a/cup/bpubpo/v3y2019i02p159-186_00.html)); anchoring replicates ([Scientific American on Many Labs](https://www.scientificamerican.com/article/dozens-of-labs-respond-to-bolster-reliability-of-psychology-research)); temporal landmarks / fresh start ([Dai, Milkman & Riis 2014](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf)); time pressure shifts choice to noncompensatory rules and unique features and cuts deferral ([Dhar & Nowlis, JCR 1999](https://profiles.wustl.edu/en/publications/the-effect-of-time-pressure-on-consumer-choice-deferral/)). **Fragile** — generic social proof (smallest nudge effect, 0.94 pp; [DellaVigna & Linos](https://www.nber.org/system/files/working_papers/w27594/w27594.pdf)); choice overload d = 0.02 ([Scheibehenne et al. 2010](https://academic.oup.com/jcr/article/37/3/409/1816569)).

### Inferences
| Dimension | Profile [L unless marked] | Design implication |
|---|---|---|
| Identity | Craft pride; "I came up hanging board / tearing off roofs"; family business, often a spouse on the books; reputation with 4–8 GCs is the asset | Speak trade, not software; show the trade's units (boards, squares) on the first screen; never imply the AI replaces the estimator's judgment |
| Risk posture | Loss-averse about *bad bids* (missed wall type, under-ordered LVP) more than about software spend; the worst outcome is winning a job priced wrong | Lead with accuracy controls (confidence flags, sheet-level audit trail) before speed |
| Price posture | Anchors on what they pay now: $0 (paper/Excel), Bluebeam seat, PlanSwift/STACK (~$2,000–3,000/yr), per-roof report fees, an offshore estimator per takeoff | Put the anchor table on the pricing/decision page; Lite at $79.90 is under every anchor except "free" |
| Trust in tech | Low for AI accuracy, higher for tools peers use; trusts YouTube demos on real plans and other subs more than vendor claims | Real-plan videos; peer reviews on Capterra/G2; third-party accuracy test |
| Language | English for GC-facing bids; Spanish with crew; owner may research in either (S for research language) | Spanish pilot; bilingual proposal templates as a hook (S) |
| Hot moments | Bid due tomorrow; the night after field work (roughly 8 pm–1 am); Sunday-night bid prep; the day after a storm (roofing); the day an estimator quits | Urgent-mode pages: one decisive cue, one proof, a "today" path (trial now, overnight Service) |
| Cold moments | Winter slowdown / Jan planning; after losing several bids on price; PlanSwift/STACK renewal notice; trade-show week (World of Concrete, IRE, Surfaces) | Considered-mode pages: comparison tables, price math, migration guides |
| Decision style | Noncompensatory under bid pressure ("does it do my trade, what's it cost, can I start tonight") | Answer those three in the first 60 words of every trade page |

- [L] Bias design (robust only): **defaults** — pre-loaded trade assemblies, default waste factors per trade, trial that starts with a sample plan already loaded; **anchoring** — show "per bid" cost vs offshore takeoff and vs legacy seat; **temporal landmarks** — January "set up for the season" and spring bid-season campaigns; **time pressure** — urgent pages that state one unique cue (e.g., "boards and studs from your PDF tonight"). **Skip** "thousands of contractors trust us" lines and "too many options" arguments.
- [S] Time-of-day pattern (night/Sunday) is practitioner inference — validate with Search Console hour-of-day data and interview question "what time was it when you searched?".

### Gaps
- No survey isolates Hispanic-owned subcontractors' trust in software/AI, nor their research language. No time-of-day search data for this ICP.

---

## E. Four forces with verbatim quotes (push, pull, anxiety, habit)

### Takeaway
Push is pricing/quantity confusion and time; pull is "hours to minutes"; anxiety is accuracy on *my* trade's quirks (roll goods, cut-up rooms, crashes on big sets) and cost creep; habit is sunk investment in a desktop tool and "how we've always priced it." Current content answers pull only — the framework's main failure mode.

### Cited Findings
Quote type key: **T** = thread title (verbatim; URL logged in geo-brain); **R** = review fragment surfaced verbatim by the search index (page not opened this session — re-check before publishing); **P** = paraphrase via another engine's summary (not a verbatim quote).

| # | Force | Quote | Type | Source |
|---|---|---|---|---|
| 1 | Push | "Newbie… How to bid drywall jobs" | T | [ContractorTalk](https://www.contractortalk.com/threads/newbie-how-to-bid-drywall-jobs.274761/) |
| 2 | Push | "Total squares for bid? How do you guys come up with your total?" | T | [ContractorTalk](https://www.contractortalk.com/threads/total-squares-for-bid-how-do-you-guys-come-up-with-your-total.37342/) |
| 3 | Push | "How much extra LVP do I really need?" | T | [r/Flooring](https://www.reddit.com/r/Flooring/comments/1dnye47/how_much_extra_lvp_do_i_really_need_currently/) |
| 4 | Push | "$12/sheet of drywall install, is that good?" | T | [r/Construction](https://www.reddit.com/r/Construction/comments/x36v0a/12sheet_of_drywall_install_is_that_good/) |
| 5 | Push | "a 12x12 bedroom would be priced different than a room that's all cut up with vaulted ceilings" | P (as summarised in search results) | [ContractorTalk "Drywall estimating and bidding"](https://www.contractortalk.com/threads/drywall-estimating-and-bidding.21199/) |
| 6 | Pull | "a task that was several hours in the making, to minutes" | R | [Capterra PlanSwift reviews](https://www.capterra.com/p/70808/PlanSwift/reviews/) |
| 7 | Pull | "Best takeoff software for a drywall contractor?" | T | [r/estimators](https://www.reddit.com/r/estimators/comments/1gl3bi8/best_takeoff_software_for_a_drywall_contractor/) |
| 8 | Pull | "Is there an AI automated takeoff software tool?" | T | [r/estimators](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/) |
| 9 | Anxiety | "are there actually any AI-based takeoff software" | T | [r/estimators](https://www.reddit.com/r/estimators/comments/1kadwx5/are_there_actually_any_aibased_takeoff_software/) |
| 10 | Anxiety | "hit-or-miss" (on AI takeoff tools) | P (Perplexity summary of the threads) | [r/estimators](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/) |
| 11 | Anxiety | "measure seems to not handle roll goods correctly with some settings missing for how installers will actually perform the install" | R | [Capterra MeasureSquare reviews](https://www.capterra.com/p/175111/Measure-Square/reviews/) |
| 12 | Anxiety | "sometimes tells you one less than you actually need" (rolls of sheet vinyl) | R | [Software Advice MeasureSquare reviews](https://www.softwareadvice.com/construction/measuresquare-profile/reviews/) / [Capterra](https://www.capterra.com/p/175111/Measure-Square/reviews/) |
| 13 | Anxiety | "freezes or crashes if too many drawings loaded" | R | [Capterra PlanSwift reviews](https://www.capterra.com/p/70808/PlanSwift/reviews/) |
| 14 | Anxiety | "not the best for stairs and doesn't include luxury vinyl product scenarios" | R | [Capterra MeasureSquare reviews](https://www.capterra.com/p/175111/Measure-Square/reviews/) |
| 15 | Habit | "support and maintenance is an additional couple hundred dollars every year" | R | [Capterra PlanSwift reviews](https://www.capterra.com/p/70808/PlanSwift/reviews/) |
| 16 | Habit | told they "would have to pay an annual subscription to "support" their perpetual license" | R (fragment) | [Capterra PlanSwift reviews](https://www.capterra.com/p/70808/PlanSwift/reviews/) |
| 17 | Habit | "some updates remove/change functionality that you may have grown used to" | R | [Capterra MeasureSquare reviews](https://www.capterra.com/p/175111/Measure-Square/reviews/) |
| 18 | Habit | "Siding installation: charge by square or by job?" | T | [ContractorTalk](https://www.contractortalk.com/threads/siding-installation-charge-by-square-or-by-job.148615/) |
| 19 | Habit / identity | "Old drywaller, new estimator" | T | [ContractorTalk](https://www.contractortalk.com/threads/old-drywaller-new-estimator.9091/) |

- Capterra's own AI review summary for PlanSwift says "most users comment bugs and issues cause regular crashes, data loss, and interruptions to productivity" and that phone support is "difficult to reach, slow to respond, and often unhelpful" — [Capterra PlanSwift](https://www.capterra.com/p/70808/PlanSwift/reviews/) (this is Capterra's summary text, not a user).
- STACK reviewers (paraphrase): price rises each renewal, no multi-user discount, slow on large plan sets and laggy on fluctuating internet, outages during bid deadlines, no offline mode, limited proposal formatting — [Capterra STACK reviews](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/) (search summary; no verbatim fragments surfaced).

### Inferences
- Force → prompt-class mapping (framework): push → "how do I / how much / is $X good" prompts (quotes 1–5); pull → "best software for [trade]" (6–8); anxiety → "does AI takeoff actually work / is X accurate for [trade quirk]" (9–14); habit → "do I need to switch / can I keep PlanSwift / alternative that keeps my assemblies" (15–19).
- [L] For finish trades, anxiety is **trade-specific** (roll goods, flash cove, stairs, cut-up rooms, pitch/waste on hips and valleys), so a generic "95–99% accurate" claim does not neutralize it; trade-specific worked examples do.
- [L] Habit is anchored in **pricing method** ("per board", "per square", "by job"), not just in software; Quotr's estimate templates must accept the sub's own unit pricing method or habit wins.

### Gaps
- No Facebook group posts, YouTube comments, Spanish-language posts, Togal.AI/Beam AI/EagleView/Roofr/Bluebeam 1–3-star reviews were retrievable this session (Reddit blocked; WebFetch blocked; search budget exhausted). These are needed to reach the ≥8-quotes-per-force bar the framework recommends for a full engagement.

---

## F. Trigger events and trigger calendar

### Takeaway
Triggers cluster into a predictable calendar (January planning and trade shows, Feb–May bid season, June–Nov hurricane season, spring hail, Q4 renewals and tariff dates) plus event-driven pushes (estimator quits, bid lost on price, crew idle, plan set crashes the tool, material price spike, labor shortage from immigration enforcement).

### Cited Findings
- Tariff/price-spike trigger: AGC Jan 2026 — 40% raised bid prices due to tariffs, 35% passed most/all costs to owners, 32% bought early; input costs +8.9% Aug 2025→Aug 2026 — [AGC](https://www.agc.org/news/2026/01/14/construction-costs-rise-fastest-rate-january-2023-november-outpacing-increases-contractors-bid), [AGC](https://www.agc.org/news/2026/09/10/construction-input-costs-climb-89-between-august-2025-and-august-2026-association-survey-finds-war) (via geo-brain). Cabinets/vanities: 25% Section 232 tariff since Oct 14, 2025, increase to 50% delayed to **Jan 1, 2027** — [Thompson Hine SmarTrade](https://www.thompsonhinesmartrade.com/2026/01/president-trump-delays-section-232-tariff-increase-on-wood-furniture-cabinets-and-vanities/) (via geo-brain).
- Labor trigger: builders struggling to find workers amid ICE crackdowns — [Axios, Sept 22, 2026](https://www.axios.com/2026/09/22/home-builders-immigrant-workers-ice).
- Tool-change trigger: PlanSwift moved to subscription in 2025 (per Quotr's post as quoted by Perplexity; ConstructConnect lists annual subscriptions from $2,000 for the first seat) — [ConstructConnect 2026 guide](https://www.constructconnect.com/blog/ai-powered-takeoff-and-estimating-software-a-contractors-guide-to-the-top-players-in-2026); a reviewer objected to paying an annual subscription to "support" a perpetual license — [Capterra](https://www.capterra.com/p/70808/PlanSwift/reviews/).
- Roofing new-construction trigger: aerial reports can struggle with trees and new construction — [roofingsoftwareguide.com](https://roofingsoftwareguide.com/roundups/best-roofing-aerial-imagery-software/) (via Perplexity summary in geo-brain).
- Atlantic hurricane season runs June 1–November 30 — [NOAA National Hurricane Center](https://www.nhc.noaa.gov/) (standard definition; not re-opened this session).
- Temporal-landmark effect (fresh starts raise goal-directed search) — [Dai, Milkman & Riis 2014](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf) (via framework file).

### Inferences
**Trigger calendar [DESIGN; month timing L unless cited]**

| Month | Trigger | Trades most affected | Mode | Prompt cluster to pre-warm |
|---|---|---|---|---|
| Jan | Fresh start; set up for season; World of Concrete and Surfaces (Las Vegas, typically Jan–Feb — verify dates) | Concrete, flooring/tile | Cold | "best estimating software for [trade] 2027", "STACK vs PlanSwift" |
| Jan 1, 2027 | Cabinet/vanity tariff step to 50% (scheduled) | Remodel-oriented finish subs, cabinet installers | Cold→hot | "cabinet tariff 2027", "buy cabinets factory direct duty paid" (Procurement) |
| Feb–Mar | International Roofing Expo (typically Q1 — verify); hail season begins in Texas (L) | Roofing | Cold/hot | "roofing takeoff software new construction" |
| Feb–May | Spring bid season: invite spike from GCs and production builders (L) | Drywall, ceilings, flooring, paint | **Hot** | "fastest drywall takeoff from PDF", "drywall estimating service overnight" |
| Any week | GC bid day (deadline pressure), estimator quits, crew idle next month | All | **Hot** | "takeoff service 24 hours [trade]", "how to bid faster" |
| Any week | Lost 3+ bids on price | All | Cold | "what do drywall subs charge per board 2026 [state]" |
| Jun 1–Nov 30 | Hurricane season; post-storm reroof surge (FL, Gulf) | Roofing, siding | Hot (but aerial-report lane) | Skip insurance reroof; target "new construction roof takeoff from plans" |
| Q3–Q4 | Software renewal notices; budget planning | All | Cold | "PlanSwift alternative", "cheaper than STACK" |
| Monthly | Material price/tariff news (LVP, porcelain, drywall) | Flooring, tile, drywall | Cold→hot | "LVP price 2026 contractor", "factory direct porcelain tile duty paid" |

### Gaps
- No primary data on bid-invite seasonality for subs (BuildingConnected/PlanHub invite volumes would answer it). Event dates for 2027 (World of Concrete, Surfaces, IRE) not verified this session. No sourced drywall/gypsum or LVP-specific tariff facts were retrieved (BLS PPI for gypsum products is the suggested source).

---

## G. Switch timeline with the prompt form at each stage

### Takeaway
Prompts move from situational pricing questions (no category noun) to "best [trade] takeoff software" to brand-vs-brand and price objections; Quotr currently has no presence at stages 1–3, which is where the shortlist forms.

### Cited Findings
- Framework: first-thought prompts are vague and situational, active-looking prompts contain category nouns and comparators, deciding prompts contain brand names, prices and objections; engines inject "best", "reviews", "2026", "vs" and brand names into fan-outs — [PPC Land / Peec fan-out analysis](https://ppc.land/what-chatgpt-actually-searches-for-5-million-fanout-queries-analyzed/), [Ahrefs](https://ahrefs.com/blog/query-fan-out-chatgpt/) (via framework file).
- Ask-for-a-pick prompts yield a 22.8% brand recommendation rate vs 8.0% topic-only — [Momentic](https://momenticmarketing.com/blog/prompt-set-worth-tracking); comparative prompts 43.3% brand-mention rate vs 18% informational — [Semrush](https://semrush.com/blog/the-ghost-citations-study/) (via framework file).

### Inferences
| Stage | What's happening [L] | Prompt form (example) [DESIGN] | Quotr presence today [K from repo tests] |
|---|---|---|---|
| 1. First thought | "I can't keep up with bids" / lost on price | "how do drywall subs bid more jobs without hiring an estimator" · "is $12 a sheet to hang good in Houston" | None (P2-type prompts go to calculators and cost guides) |
| 2. Passive looking | Watches a YouTube takeoff video, asks a peer, reads a Facebook group | "how to do a drywall takeoff from PDF fast" · "drywall takeoff Bluebeam vs PlanSwift" | None |
| 3. Active looking | Category nouns appear | "best takeoff software for drywall contractors" · "AI takeoff for flooring" · "roof takeoff from plans software" | Absent (C4, C5, N4) |
| 4. Deciding | Brands, price, objections | "STACK vs PlanSwift for drywall" · "Togal vs Beam for small subs" · "cheapest AI takeoff" · "Quotr reviews" | Absent on V6/V7; brand prompts answered from Quotr's own pages; reviews conflated with Quotr Pro app (B3) |
| 5. First use / consuming | Trial on a live bid | "how to set drywall waste factor in [tool]" · "import my PlanSwift assemblies" | Tutorials exist ([/tutorials/](https://quotr.ai/tutorials/)); trade-specific ones not found |
| 6. Repeat loop | Monthly bid crunch, renewals | Terse, memory-assisted: "do the takeoff for this set" / "price check LVP" (S) | — |

### Gaps
- No recorded prompts from actual switchers; the "what exactly did you type, and into what?" interview question has not been asked of this ICP.

---

## H. Current alternatives and what does not satisfy them (incl. doing nothing, paper, offshore estimating), unmet needs ranked by frequency

### Takeaway
The live alternatives are paper/scale ruler + Excel, Bluebeam (measuring, not estimating), legacy PlanSwift/On-Screen Takeoff, STACK, trade specialists (MeasureSquare, The EDGE), aerial roof reports, and paid outsourcing (offshore-style estimating firms, Beam AI's done-for-you). The most frequent complaints are cost creep for small shops, crashes/slowness on large plan sets, support, learning curve and trade-specific calculation gaps — all addressable by an affordable browser tool *if* Quotr proves accuracy on the trade's quirks.

### Cited Findings
| Alternative | What fails to satisfy (evidence) | Source |
|---|---|---|
| PlanSwift (desktop) | Crashes/data loss; "freezes or crashes if too many drawings loaded"; support hard to reach; steep learning curve; desktop-only; Dropbox multi-user issues; extra support/maintenance fees; 2025 subscription change; from $2,000 first seat/yr | [Capterra](https://www.capterra.com/p/70808/PlanSwift/reviews/); [GetApp](https://www.getapp.com/all-software/a/planswift/); [Software Advice](https://www.softwareadvice.com/construction/planswift-takeoff-estimating-profile/reviews/) ($2,000/yr starting price); [ConstructConnect](https://www.constructconnect.com/blog/ai-powered-takeoff-and-estimating-software-a-contractors-guide-to-the-top-players-in-2026) |
| STACK (cloud) | Renewal increases; no multi-user discount; slow on large sets; outages near bid deadlines; no offline mode; limited proposal formatting; clumsy price imports. Entry $249/user/mo, plus a **free version** | [Capterra STACK](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/); [stackct.com/pricing](https://www.stackct.com/pricing/) |
| MeasureSquare (flooring) | Roll goods/sheet vinyl miscalculation; flash cove; stairs; LVP scenarios; pattern creation cumbersome; laggy on big projects; no iOS; desktop needs Windows via Parallels on Mac; license-by-license | [Capterra](https://www.capterra.com/p/175111/Measure-Square/reviews/); [Software Advice](https://www.softwareadvice.com/construction/measuresquare-profile/reviews/) |
| Aerial roof reports (EagleView, Hover, RoofSnap, Roofr) | Work for existing roofs; struggle with trees and **new construction** (no roof yet) | [roofingsoftwareguide.com](https://roofingsoftwareguide.com/roundups/best-roofing-aerial-imagery-software/); [theroofingbrief.com comparison](https://theroofingbrief.com/eagleview-vs-hover-vs-roofsnap/) (via geo-brain) |
| Bluebeam | Positioned for markup/measurement, "not built for estimating" (geo-brain persona pain); recommended in drywall answers anyway (C4) | `audiences-and-personas.md` §3; C4 run |
| AI-native tools (Togal.AI, Beam AI) | Togal $299/user/mo billed yearly; Beam done-for-you ~$15–25K/yr per trade, no public self-serve price; AI takeoff "hit-or-miss" sentiment | [togal.ai/pricing](https://www.togal.ai/pricing); [ConstructConnect](https://www.constructconnect.com/blog/ai-powered-takeoff-and-estimating-software-a-contractors-guide-to-the-top-players-in-2026); [r/estimators](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/) |
| Outsourced/offshore estimating services | Crowded pool of per-takeoff services ranks for service-price prompts (blazeestimating, optimarprecon, quantifyna, nedesestimating, 1800estimating, estimators.us, constructem) | C12 run (`quotr_ai_visibility_tests.md`); e.g. [Construct Estimates drywall services](https://constructestimates.com/drywall-estimating-services/) |
| Doing nothing / paper + Excel | Hours per takeoff; bids missed; scope gaps — RL Electric (electrical, not finish trade) ~20 hours per takeoff before Quotr | Quotr homepage testimonial via `buyer-questions-by-trade.md` |

### Inferences
**Unmet needs ranked by frequency across the mined reviews/threads [EST — counts are "number of products/sources where the theme appeared", n ≈ 6 sources]**

| Rank | Unmet need | Appeared for | Quotr can credibly answer? |
|---|---|---|---|
| 1 | Affordable for a small shop; no renewal creep; fair multi-seat pricing | PlanSwift, STACK, GetApp summary, Capterra budget | **Yes** — Lite $79.90/seat/mo, no setup fee, monthly |
| 2 | Doesn't crash/slow on big plan sets; works near bid deadline | PlanSwift, STACK, MeasureSquare | Unproven — needs a published large-set performance test |
| 3 | Trade-specific quantity logic (rolls, stairs, flash cove, waste by pattern, pitch/hip/valley, wall types) | MeasureSquare, ContractorTalk/Reddit titles | Partly — area detection exists; trade logic must be shown per trade |
| 4 | Easy to learn / reachable support | PlanSwift, MeasureSquare | Plausible — Plus includes 2 h onboarding; Lite support level TO CONFIRM |
| 5 | Works on Mac/iPad/browser | MeasureSquare, PlanSwift | **Yes** (browser-based) |
| 6 | AI that is actually accurate on my drawings | r/estimators | Needs third-party evidence |
| 7 | Roof quantities when there's no roof yet | Aerial-report limitation | **Yes** — plan-based takeoff is Quotr's natural roofing lane |
| 8 | Help on overflow weeks without hiring | Service pool in C12 | Yes — Quotr Service; but see price math in I |

### Gaps
- 1–3-star reviews for Togal.AI, Beam AI, EagleView, Hover, Roofr, The EDGE and Bluebeam were not mined (budget exhausted). Offshore estimating per-takeoff prices were not retrieved.

---

## I. Willingness to pay, price anchors, who pays, sales cycle and trial behavior

### Takeaway
The owner pays out of operating cash against a $1,600–$4,000/yr software norm; Quotr Lite ($959/seat/yr) undercuts every paid incumbent, but Quotr Service at $0.25/sq ft is expensive for routine finish-trade bids and has a price cliff at 50,000 sq ft that should be explained or smoothed.

### Cited Findings
| Anchor | Price | Source |
|---|---|---|
| Typical construction software budget | ~$1,600–$4,000/yr | [Capterra](https://www.capterra.com/resources/construction-software-buyer-insight/) |
| Quotr Lite / Plus | $79.90 / $299.90 per seat per month; 7-day free trial, "Cancel anytime — no charge if canceled"; Plus includes 2 h onboarding, 2,000 sq ft takeoff credits/mo, 10% off procurement | [quotr.ai/pricing](https://quotr.ai/pricing/), [/software/](https://quotr.ai/software/) (scraped 2026-09-25, `product-and-features.md`) |
| Quotr Service | $0.25/sq ft under 50,000 sq ft; $0.10/sq ft at 50,000+ | [quotr.ai/pricing](https://quotr.ai/pricing/) |
| STACK | Takeoff & Estimate from $249/user/mo; free version | [stackct.com/pricing](https://www.stackct.com/pricing/) |
| PlanSwift | From $2,000 first seat/yr (ConstructConnect, July 2026); $1,749/user/yr per Quotr's own post (conflict) | [ConstructConnect](https://www.constructconnect.com/blog/ai-powered-takeoff-and-estimating-software-a-contractors-guide-to-the-top-players-in-2026) |
| Togal.AI | Growth $299/user/mo billed yearly | [togal.ai/pricing](https://www.togal.ai/pricing) |
| Togal add-on inside eTakeoff | $1,800/yr/user | ConstructConnect guide (via `competitor-landscape.md`) |
| Beam AI done-for-you | ~$15–25K/yr per trade | [ConstructConnect](https://www.constructconnect.com/blog/ai-powered-takeoff-and-estimating-software-a-contractors-guide-to-the-top-players-in-2026) |
| Trust ceiling for AI-only recommendations | Trust in AI alone falls to 5% for purchases over $500 | [MarTech](https://martech.org/the-ai-shopping-stats-2026-what-you-need-to-know/) (via framework) |

### Inferences
- [CALC] Lite = $958.80/seat/yr — below the Capterra budget floor, ~32% of STACK's $249 entry, ~48% of PlanSwift's $2,000. At 20 bids/week (~87/month), Lite ≈ **$0.92 per bid** (assumes 4.33 weeks/month).
- [CALC] Service at $0.25/sq ft: a 2,500 sq ft production house = **$625**; a 20,000 sq ft TI = **$5,000**; a 49,999 sq ft job = **$12,500** but a 50,000 sq ft job = **$5,000** (price cliff). For a sub who wins ~1 in 4–5 bids (S — no hit-rate data), paying $625–$5,000 per *bid* is uneconomic for routine invites; Service fits overflow, large jobs and "estimator quit" weeks.
- [L] Who pays: the owner (often the estimator) with a company card; spouse/office manager may hold the books; no procurement department. Sales cycle: same-day to two weeks for Lite; Plus/Enterprise for 10+ person estimating departments (drywall/ceiling subs doing commercial).
- [L] Trial behavior: subs trial on a **live bid**, so a 7-day trial that starts on a slow week wastes itself; a "start the trial on your next bid" or plan-set-based trial (credits) matches the job better. STACK's free tier makes "free" the reference point for cold-mode searches ("free drywall takeoff software").
- [S] Plus's 2,000 sq ft of monthly credits (if they are Service credits, TO CONFIRM) equal ~$500 of Service at $0.25 — a concrete, citable value line for the Plus tier.

### Gaps
- Aerial roof report prices (EagleView/Hover/Roofr per report) and offshore per-takeoff prices were not retrieved — both are the most important anchors for roofing and outsourcing pages. No data on finish-sub hit rates or bids per week.

---

## J. Vocabulary list (English trade units and terms, Spanish equivalents where documented)

### Takeaway
Pages must speak in each trade's selling unit (board/sheet, square, box, SY, CY, board foot, LF) and plan vocabulary (wall types, partition schedule, RCP, finish schedule, elevations); Spanish jobsite equivalents were not documented in any retrievable source, so Spanish terms below are standard translations to validate.

### Cited Findings
English vocabulary (from `buyer-questions-by-trade.md` and `construction-glossary.md`, which cite ContractorTalk, Reddit and calculator sources):
- **Drywall / framing:** SF of board split walls vs ceilings; sheets/boards (4×8 = 32 SF; 4×12 = 48 SF); hang vs finish; finish Levels 0–5; Type X fire-rated, moisture-resistant; LF corner bead/trim; mud boxes, tape rolls, screws; ~10% waste; metal studs/track LF; board feet (lumber).
- **Acoustical ceilings:** [L] RCP (reflected ceiling plan), ACT (acoustical ceiling tile), grid/main tee/cross tee, wall angle LF, ceiling heights, soffits. (RCP listed in the brief; not in the retrieved sources.)
- **Flooring:** net SF by room and material; carpet in SY; waste then round up to boxes/cartons; LF transitions, base, trim; stair treads (each); subfloor prep, moisture testing, demo as separate lines; waste 5–7% skilled straight lay, ~10% default, 12–15%+ diagonal/complex (unverified ranges).
- **Tile:** SF floor/wall; boxes; LF bullnose/Schluter-type edges; thinset bags, grout bags, backer board (3×5 panel = 15 SF), waterproofing membrane; pattern (straight, diagonal, herringbone) changes waste.
- **Painting:** SF walls/ceilings; coats; coverage ~250–400 SF/gal; production rate SF/hour; LF trim; doors/frames each; lifts/scaffold.
- **Roofing:** square = 100 SF; pitch/slope (rise per 12" run) factor; LF ridge, hip, valley, eave, rake; drip edge; underlayment rolls; bundles; flashing; waste higher on cut-up roofs; commercial: membranes, insulation boards, drains.
- **Siding:** wall area from elevations less openings; squares; LF J-channel, corners, starter strip, trim; soffit/fascia; ~10% waste.
- **Insulation:** SF by assembly; R-value by code; spray foam in board feet (1 SF × 1"); open- vs closed-cell; bags of blown-in at depth.
- **Concrete flatwork:** CY = L × W × thickness ÷ 27; 4" slab ≈ 1 CY per 80 SF; rebar (lb/tons, LF by size), wire mesh, formwork SF/LF, short-load fees, pump, finishing.
- **Bid/GC terms:** bid invite, bid day, scope letter/exclusions, alternates, addenda, bid leveling, unit pricing (`buyer-questions-by-trade.md` §15).

### Inferences
Spanish terms [S — standard/regional translations, **not** documented jobsite usage; validate with bilingual estimators before publishing]:

| English | Spanish candidates | Note |
|---|---|---|
| drywall / sheetrock | tablaroca (MX), panel de yeso, "sheetrock" (anglicism) | Search both "drywall" and "tablaroca" |
| takeoff | cuantificación, cómputo/levantamiento de cantidades, "takeoff" | English term likely kept |
| estimate / bid | estimado, presupuesto, cotización / oferta, propuesta | "estimado" common in US Spanish (S) |
| plans / blueprints | planos | — |
| square (roofing) | "square", cuadro (100 pies cuadrados) | Validate |
| waste | desperdicio, merma | — |
| metal studs / track | postes/canales metálicos, "metal studs" | — |
| mud / tape | pasta/compuesto, cinta | — |
| shingles | tejas asfálticas, "shingles" | — |
| flooring / tile | pisos / loseta, azulejo, cerámica, porcelanato | — |
| general contractor | contratista general | — |

### Gaps
- No documented US jobsite Spanish/Spanglish glossary for these trades was retrieved; a bilingual estimator review is required. Partition-schedule/wall-type and RCP vocabulary is from domain knowledge, not a cited source.

---

## K. Channels: where this ICP reads and asks

### Takeaway
The ICP reads trade forums (ContractorTalk, DrywallTalk, PaintTalk), trade subreddits, YouTube takeoff and math videos, Capterra/G2 review pages, trade publications and association channels; AI engines already cite r/estimators, Capterra/GetApp/Software Advice and list-farm pages for these prompts. Community sizes could not be measured this session.

### Cited Findings
- Forums with live ICP threads: [ContractorTalk](https://www.contractortalk.com/) (drywall, roofing, siding, tile, flatwork, insulation threads above); [DrywallTalk](https://www.drywalltalk.com/threads/drywall-estimating.2284/); [PaintTalk](https://www.painttalk.com/threads/how-to-do-estimates-for-interior-painting.93337/) (all via `buyer-questions-by-trade.md`).
- Subreddits with ICP threads: r/estimators, r/Flooring, r/Construction (URLs in E); r/estimators appeared in 6 of 32 Perplexity answers in the Sept audit (`offsite-earned-media-plan.md`).
- YouTube videos the ICP learns from: [How To Do A Drywall Quantity Takeoff](https://www.youtube.com/watch?v=fZejqlj-eyU), [PlanSwift + Excel drywall](https://www.youtube.com/watch?v=cGIblB10oYI), [Bluebeam drywall](https://www.youtube.com/watch?v=q5IALR_-3uQ), [How to Write Roofing Estimates Using Roof Measurements](https://www.youtube.com/watch?v=O5QycPWhnLA), [Math for roofers](https://m.youtube.com/watch?v=bzsRhxx-OvY), [Togal flooring takeoff webinar](https://www.youtube.com/watch?v=TPN8_322B0s) (competitor).
- Review directories cited by engines for trade prompts: GetApp, Capterra, Software Advice, G2 (C4, C5, V-prompts). STACK has ~1,400 Capterra reviews; Togal.AI showed "No Reviews" on Capterra (2026-09-25) — `competitor-landscape.md`.
- Trade press covering this ICP's AI adoption: [Roofing Contractor](https://www.roofingcontractor.com/articles/102644-ai-use-jumps-among-construction-firms-houzz-survey-finds) (Houzz survey; xBuild $19M roofing-estimating raise [here](https://www.roofingcontractor.com/articles/101802-xbuild-raises-19m-to-transform-construction-estimating)).
- Hispanic construction organizations with published reports: [National Hispanic Construction Alliance](https://www.prweb.com/releases/national-hispanic-construction-alliance-releases-groundbreaking-report-on-hispanics-in-construction-and-outlines-2025-policy-priorities-302394192.html); [Hispanic Construction Council](https://www.constructionowners.com/press-release/hispanic-construction-council-highlights-labor-shortage-in-2025-report). An agency guide on reaching Hispanic contractors exists ([Kleber & Associates](https://kleberandassociates.com/?p=11722), title only).
- Spanish crew communication on WhatsApp is a vendor-blog topic ([Velora](https://velora.ai/blog/construction-crew-whatsapp-spanish/), title only).
- Engine reach (US adults, Feb 2026): ChatGPT 44%, Gemini 24%, Copilot 17%, Claude 6% — [Pew](https://www.pewresearch.org/internet/2026/06/17/americans-and-ai-2026-chatbots-smart-devices-and-views-on-impact/markdown) (via framework).

### Inferences
| Channel | Type | Role for this ICP [L] | Note |
|---|---|---|---|
| AWCI ([awci.org](https://www.awci.org)) + *Walls & Ceilings* ([wconline.com](https://www.wconline.com)) | Association / trade pub | Drywall, framing, acoustical ceilings, plaster | Contributed article with original data |
| NRCA ([nrca.net](https://www.nrca.net)) + *Roofing Contractor*; International Roofing Expo | Association / pub / event | Roofing | New-construction-from-plans angle |
| NWFA ([nwfa.org](https://www.nwfa.org)), *Floor Covering News* ([fcnews.net](https://www.fcnews.net)), Surfaces/TISE | Association / pub / event | Flooring, tile | Procurement cross-sell (LVP, porcelain) |
| PDCA ([pdca.org](https://www.pdca.org)) | Association | Painting | Low priority |
| ACI ([concrete.org](https://www.concrete.org)), ASCC ([ascconline.org](https://www.ascconline.org)), World of Concrete | Association / event | Concrete flatwork | WOC is the January anchor event |
| Hispanic orgs (NHCA, HCC, USHCC chapters) | Association | Hispanic-owned subs | Spanish webinar/pilot partner (S) |
| Facebook trade groups, WhatsApp crews | Community | Peer referrals, Spanish | Not citable by engines; recruitment channel only |
| Supply houses (drywall, roofing, flooring distributors) | Channel | Counter-staff referrals, rebates | Partnership hypothesis (S) |

(Association/pub/event URLs and typical months are from prior knowledge and were **not** re-verified this session.)

### Gaps
- Subreddit member counts (r/Drywall, r/Flooring, r/Roofing, r/Concrete, r/Construction, r/estimators), Facebook group sizes, YouTube creator subscriber counts and any WhatsApp community documentation: not retrievable (Reddit blocked, budget exhausted). 2027 event dates unverified.

---

## L. Proof required at each stage

### Takeaway
Early stages need the trade's math and local price facts (not software); active looking needs a real-plan demo and third-party listing; deciding needs reviews from the same trade, a price comparison, migration help and an accuracy method; first use needs a fast first takeoff on the buyer's own plan.

### Cited Findings
- Evidence density decides share of answer once retrieved: quotes +40.9%, statistics +30.6%, citations +27.5% position-adjusted visibility — [arXiv 2311.09735](https://arxiv.org/abs/2311.09735) (via framework). Self-published Quotr numbers (95–99% accuracy, $1.2B+ estimated) are hedged or anonymized by engines because they lack method — `competitor-landscape.md` §3. Togal's citable proof is a University of Kansas study (up to 76% faster, within 5%) — [Togal case study](https://www.togal.ai/case-study/peer-reviewed-study-togal-ai-vs-on-screen-takeoff).
- Engines anonymize Quotr when it is the sole source ("one outsourced estimating service", C12).

### Inferences
| Stage | Proof that satisfies this ICP [DESIGN] | Owner |
|---|---|---|
| First thought | Dated per-board/per-square/per-SF price ranges by state with method; calculators that show the math | Quotr answer pages + original survey |
| Passive | 5–10 min YouTube on a real plan set for *my* trade, English and Spanish | Quotr YouTube |
| Active | Listed on the third-party pages engines cite (Capterra/GetApp, constructioncoverage, exayard, gitnux-type lists); trade page that answers "does it do my trade, cost, start tonight" in 60 words | Off-site + trade hub |
| Deciding | ≥10 Capterra/G2 reviews from finish trades; anchor table vs STACK/PlanSwift/Togal/offshore; migration guide; published accuracy test with method and an outside estimator | Reviews program, decision page, benchmark |
| First use | First takeoff on own plan in <30 min; trade defaults (waste, sheet size, pitch factors); Spanish onboarding option (S) | Product/onboarding |

### Gaps
- No evidence on which proof type converts this ICP best (interviews needed).

---

## M. Coding chains: trigger → stage → mode → restraining force → exact prompt → proof required

### Takeaway
Seven chains cover the ICP; the four highest-value for Quotr are the bid-season speed chain (drywall/ceilings), the PlanSwift/STACK renewal chain, the new-construction roofing chain, and the flooring price-spike chain that opens Procurement.

### Cited Findings
- Chain method and four-forces mapping — framework file; trigger evidence per chain is cited in sections E, F, H, I.

### Inferences
[DESIGN; prompts are illustrative first-person forms built from the cited vocabulary; frequency must be validated by ≥3 of 12 interviews or ≥5 of 50 community posts]

| # | Trigger | Stage | Mode | Restraining force | Exact prompt | Proof required |
|---|---|---|---|---|---|---|
| M1 | Spring bid spike; 3 GC bids due Thursday | Active | **Hot** | Anxiety: "AI misses wall types" | "fastest way to do a drywall takeoff from PDF plans tonight, boards and metal studs, accurate on commercial wall types" | Real-plan video by wall type; confidence flags; trial that starts on own plan |
| M2 | Lost 3 bids on price in a month | First thought | Cold | Habit: "my per-board price has always worked" | "what are drywall subs charging per board to hang and finish in Texas 2026, production homes" | Dated price ranges by state with n and method (original survey) |
| M3 | Estimator quits mid-season | Active | **Hot** | Anxiety: outsourced quality, turnaround | "drywall estimating service cost per takeoff, 24 hour turnaround, vs buying AI takeoff software" | Published per-sq-ft price incl. cliff explanation, turnaround SLA (resolve 24 h vs 3–4 days conflict), sample deliverable |
| M4 | New-construction roof package, no house to fly | Active | Hot | Habit: EagleView workflow | "how to get roof squares, ridge, hip and valley lengths from architectural plans for new construction, software" | Worked plan→squares example with pitch factors; side-by-side vs aerial use cases |
| M5 | PlanSwift subscription/renewal or crash on a big set | Deciding | Cold | Habit: years of assemblies; switching cost | "PlanSwift alternative for drywall that runs in a browser, imports my assemblies, cheaper than STACK" | Migration guide; price anchor table; large-set performance note |
| M6 | LVP/porcelain price jump or tariff news | Passive→active | Cold | Anxiety: quality, duties, lead time | "can a flooring contractor buy LVP or porcelain tile factory direct with duties paid, is it cheaper than distributor" | Landed-cost table (FOB vs DDP), QC/sample process, lead time, references (Procurement) |
| M7 | Spanish-dominant owner asked by GC for typed, itemized bid | First thought | Cold | Anxiety: language + tech | "cómo hacer un estimado profesional de drywall para un contratista general" | Spanish template + Spanish video + bilingual support line (S) |
| (skip) | Hurricane/hail reroof surge | Active | Hot | Habit: aerial reports for existing roofs | "fastest roof measurement report after storm" | Not Quotr's lane — aerial vendors own it; do not build |

### Gaps
- None of the chains is frequency-validated; no switch interviews have been run for this ICP.

---

## N. Prompt matrix (full-context, short category, brand)

### Takeaway
Track 12 full-context prompts (3 in Spanish, flagged speculative), 6 short category prompts and 3 brand prompts in separate groups; the highest-value cells are "ask for a pick" prompts with trade + crew size + city + current tool embedded.

### Cited Findings
- Brand prompts mention the brand 91.6% of the time vs 19.6% for non-brand and must be tracked separately — [Momentic](https://momenticmarketing.com/blog/prompt-set-worth-tracking), [Peec](https://peec.ai/blog/how-to-choose-the-right-prompts-for-llm-tracking) (via framework). Persona facts in a prompt change which brands are named — [Profound](https://www.tryprofound.com/blog/do-answer-engines-customize-responses-to-different-personas) (via framework). Fan-outs inject "2026", "best", "reviews", "price", "official" — [Ahrefs](https://ahrefs.com/blog/query-fan-out-chatgpt/) (via framework).

### Inferences
Tags: intent ∈ {learn, compare, pick, local, validate, do}; stage per G; urgency ∈ {acute, recurring, exploratory}; engine: ChatGPT (C), Google AIO/AI Mode (G), Perplexity (P). **Demand tier is a labeled [EST]** (1 = rare, 5 = very common), based on thread density in the geo-brain and engine behavior, not on measured volume.

**Full-context first-person prompts**

| ID | Prompt | Intent | Stage | Urgency | Mode | Engine | Expected fan-out nodes | Tier [EST] |
|---|---|---|---|---|---|---|---|---|
| F1 | "I run a 15-man drywall and metal stud company in Houston. We get 20+ bid invites a week from GCs on commercial TI and I do takeoffs with a scale ruler and Excel at night. What's the fastest takeoff software that counts boards and studs from PDF plans, and what does it cost per month?" | pick | Active | acute | Hot | C, G | best drywall takeoff software 2026 · AI drywall takeoff · price per month · STACK vs PlanSwift · reviews | 4 |
| F2 | "I own a flooring company in Dallas–Fort Worth with 8 installers, mostly LVP and carpet for multifamily builders. MeasureSquare is slow on big apartment sets. Is there AI software that measures rooms by finish type from the PDF and figures waste and boxes?" | pick | Active | recurring | Cold | C, G | best flooring takeoff software 2026 · AI flooring takeoff · MeasureSquare alternatives · waste factor LVP | 3 |
| F3 | "I'm a roofing contractor in Tampa doing new-construction townhomes for builders. EagleView doesn't work because the roofs aren't built yet. What software do roofers use to get squares, ridge, hip and valley from the architectural plans?" | pick | Active | acute | Hot | C, G, P | roofing takeoff software from plans · new construction roof measurement · EagleView alternative blueprints · 2026 | 3 |
| F4 | "Acoustical ceiling sub in Phoenix, I bid ACT grid and tile off reflected ceiling plans. Bluebeam works for measuring but it's slow. Which takeoff tools read RCPs and count grid, tile and light fixtures automatically?" | pick | Active | recurring | Cold | C, P | ceiling takeoff software · RCP takeoff · Bluebeam alternatives takeoff · AI count | 2 |
| F5 | "Concrete flatwork contractor in Atlanta, 3 crews pouring driveways, sidewalks and slabs for production builders. I figure cubic yards by hand from site plans. Is there an app that does the takeoff from PDF and gives yards, rebar and forms?" | pick | Active | recurring | Cold | C, G | concrete takeoff software 2026 · concrete estimating app · free concrete estimating software · cubic yard calculator | 3 |
| F6 | "Commercial painting company in Charlotte, 20 painters. I measure wall SF in PlanSwift but it went to subscription and support is bad. What are cheaper PlanSwift alternatives in 2026 for a painting contractor?" | compare | Deciding | recurring | Cold | C, G, P | PlanSwift alternatives 2026 · painting estimating software · price · reviews | 3 |
| F7 | "Drywall contractor in Las Vegas — my estimator just quit and bid season is starting. Should I pay an estimating service per takeoff or buy AI takeoff software? What do drywall estimating services charge?" | compare | Active | acute | Hot | C, G | drywall estimating services cost · outsourced takeoff price per sq ft · AI takeoff software price · reviews | 3 |
| F8 | "Tile and stone installer in Orlando, we supply and install porcelain for condo projects. Tariffs and distributor prices are killing my margin. Can I buy porcelain tile factory direct with duties paid delivered to the job, and is it actually cheaper?" | learn→pick | Passive | recurring | Cold | C, G | buy porcelain tile direct from China contractor · DDP tile · tariffs tile 2026 · landed cost | 2 |
| F9 | "Siding and insulation sub in Raleigh doing production homes. I need siding squares from elevations and insulation SF by R-value from the plans. Is there one takeoff software that does both?" | pick | Active | recurring | Cold | C | siding takeoff software · insulation takeoff · elevation takeoff · 2026 | 2 |
| F10 (ES) | "Tengo una compañía de drywall y framing en Houston con 12 trabajadores. Hago los estimados a mano con escala y Excel y no me da tiempo para todas las invitaciones de los contratistas generales. ¿Qué programa con inteligencia artificial me saca las hojas y los metal studs de los planos en PDF y cuánto cuesta?" | pick | Active | acute | Hot | C | software takeoff drywall · programa estimados construcción · "best drywall takeoff software" (engine may fan out in English) | 1–2 [S] |
| F11 (ES) | "Soy contratista de techos en Miami. Para casas nuevas no puedo usar EagleView. ¿Cómo saco los squares del techo de los planos y qué software recomiendan?" | learn→pick | Active | acute | Hot | C | roofing takeoff from plans · software techos · EagleView alternative | 1 [S] |
| F12 (ES) | "Instalo pisos LVP y cerámica en Phoenix. ¿Cuánto desperdicio debo calcular y hay una app que lo calcule de los planos?" | learn | First thought | recurring | Cold | C, G | desperdicio LVP · LVP waste factor · flooring calculator · takeoff app | 1–2 [S] |

**Short category prompts**

| ID | Prompt | Intent | Stage | Engine | Tier [EST] | Repo link |
|---|---|---|---|---|---|---|
| S1 | best takeoff software for drywall contractors | pick | Active | C, G, P | 4 | = T04/C4 |
| S2 | best takeoff software for flooring contractors | pick | Active | C, G, P | 3 | = T05/C5 |
| S3 | best roofing takeoff software for new construction from plans | pick | Active | C, G, P | 3 | = T51/N4 |
| S4 | cheapest AI takeoff software for small subcontractors | compare | Deciding | C, P | 3 | near V7 |
| S5 | drywall estimating services cost per takeoff | compare | Active | C, G | 3 | new |
| S6 | mejor software para estimar drywall | pick | Active | C | 1 [S] | new |

**Brand prompts**

| ID | Prompt | Intent | Stage | Tier [EST] |
|---|---|---|---|---|
| B1 | Quotr.ai reviews for drywall contractors | validate | Deciding | 1 |
| B2 | Quotr vs STACK for a small flooring contractor | compare | Deciding | 1 |
| B3 | Quotr.ai pricing for small subcontractors / is Quotr legit | validate | Deciding | 1–2 |

### Gaps
- No measured demand (GSC, Keyword Planner, Profound volumes) for any of these prompts. Spanish prompts have no demand evidence at all; treat them as an experiment (3 prompts, 3 runs each, monthly).

---

## O. Simulation: a simulated ChatGPT journey, actual retrieval runs, and the gap verdict

### Takeaway
In the simulated journey the buyer reaches a shortlist of STACK, PlanSwift, Togal.AI (and Beam AI or The EDGE by trade) without Quotr ever entering; retrieval evidence (this session's searches and the September Perplexity runs) shows the shortlist is built from vendor-owned trade listicles, list farms and review directories, which is exactly where Quotr is missing.

### Cited Findings
**(2) Retrieval runs.** Fresh WebSearch runs on 2026-11-06 are labeled **"retrieval proxy, not an AI engine answer."** Repo runs from 2026-09-25 were real Perplexity Sonar answers and are labeled **"prior AI engine run."** Only 4 fresh runs fit before the shared search budget ran out.

| # | Query (fan-out node) | Label | Top domains, in order | Brands named | Quotr appears? | Winning format |
|---|---|---|---|---|---|---|
| R1 | drywall takeoff software (r/estimators drywall takeoff software PlanSwift STACK bids hours) | Retrieval proxy, 2026-11-06 | Block 1: quickadminsoftware, constructestimates (drywall estimating *services*), constructem, myquoteiq ×2, ustechautomations, capterra (PlanSwift reviews), alternativeto ×2 · Block 2: buzzbid, servicebusinessacademy, **quotr.ai** (/blog/best-drywall-estimating-software-in-2026/), quickadminsoftware, gitnux ×2, struvia (STACK vs PlanSwift), myquoteiq ×2, wifitalents | STACK, PlanSwift, The EDGE, Bluebeam Revu | **Retrieved (own self-ranked listicle, ~3rd in block 2); not named in summary** | "Best drywall estimating software 2026" listicles (vendor + list farm) |
| R2 | PlanSwift review cons (reviews node) | Retrieval proxy (review domains only) | softwareadvice, capterra (+5 pages), getapp, trustradius | PlanSwift | No — Quotr has no Capterra/GetApp/Software Advice listing | Review directory |
| R3 | STACK takeoff review cons (reviews node) | same | capterra ×10 (reviews pages, pricing page) | STACK | No | Review directory |
| R4 | MeasureSquare review cons flooring (reviews node) | same | softwareadvice ×2, capterra ×5, getapp (vs Square Takeoff), capterra compare (vs AutoCAD, vs Buildxact) | MeasureSquare, Square Takeoff, Buildxact | No | Review directory + compare pages |
| C4 | best takeoff software for drywall contractors | Prior AI engine run (Perplexity, 2026-09-25) | worldmetrics, myquoteiq, exayard, gitnux, pro.houzz, bluebeam, projul, reddit r/estimators, estimatingedge, buildxact, constructconnect, constructioncoverage, softwareadvice, stackct | STACK, The EDGE, QuoteIQ, Bluebeam, Houzz Pro, Buildxact, PlanSwift | No | Listicles + vendor trade pages |
| C5 | best takeoff software for flooring contractors | Prior AI engine run | getapp, myquoteiq, exayard, pro.houzz, planswift, gitnux ×4, oncenter, measuresquare, ibeam.ai, buildxact, estimatingedge, arcsite, stackct | The EDGE, MeasureSquare, PlanSwift, STACK, Autodesk Takeoff, QuoteIQ, On Center | No | List farms (gitnux ×4) + vendor pages |
| N4 | best roofing takeoff software for new construction from plans | Prior AI engine run | worldmetrics, buildvision, zipdo, easytakeoffs, ibeam.ai roofing page, buildxact, oncenter, zztakeoff | STACK, Beam AI, On-Screen Takeoff + Quick Bid, Buildxact (+ Roofr, Hover, RoofSnap as measurement tools) | No | Vendor trade pages + list farms |
| P2 | how to estimate drywall for a house | Prior AI engine run | homeadvisor, easytakeoffs, finehomebuilding, homeguide, onsitecalculator, procore, thespruce, certainteed, arcsite, omnicalculator, buildvisionai, inchcalculator, autodesk | none | No | **Calculators** (3 software vendors cited via calculators) |
| V10 | STACK takeoff alternatives for small residential subcontractors | Prior AI engine run | easytakeoffs ×2, scopetakeoff, ustechautomations, oneestimate.ai, constructionbids.ai, exayard, getonecrew, softwareconnect, projul, **quotr.ai**, g2 ×3, getapp, myquoteiq, buildern, constructioncoverage, capterra | Easy Takeoffs, Buildxact, Square Takeoff, PlanSwift, Bluebeam, eTakeoff | Retrieved only (stack-alternative post) | Competitor "alternatives" posts |
| C14 | where can US contractors buy cabinets, windows and flooring factory direct at wholesale prices | Prior AI engine run | buildsourcedirect, platinumdirectsupply, floordaddydepot, shopathomecabinets, sdwoodcabinet, kraftersland, floorkitchenresource, ufd1, northeastfactorydirect, houzz | Build Source, Platinum Direct, Floor Daddy Depot, etc. | No | Local "factory direct" dealer pages |

Sources for prior runs: `research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md` §5 and `geo-brain/04-prompt-library/tracking-set.md` (T51, T53).

### Inferences
**(1) SIMULATED ChatGPT conversation — [SIM] not a real transcript; brand lists are modeled on the retrieval evidence above.** Persona (composite): Javier, 41, owner of a 14-person drywall & metal framing sub in Houston; bids commercial TI for 6 GCs plus some production homes; takeoffs with a scale ruler, Excel and a lapsed Bluebeam trial; English for bids, Spanish with crew.

| Turn | Javier types | Simulated ChatGPT behavior | Likely fan-out (from F/G) |
|---|---|---|---|
| 1 (10:40 pm, Tuesday) | "how do drywall guys do takeoffs faster, I'm doing them by hand at night and missing bids" | Explains digital takeoff; mentions Bluebeam, PlanSwift, STACK, "AI takeoff tools like Togal"; offers to recommend | "best drywall takeoff software 2026", "AI drywall takeoff" |
| 2 | "commercial TI, 15 guys, Houston. I need boards and studs from PDF. what's best and what does it cost" | Shortlist: STACK (cloud, free tier, $249+), PlanSwift (desktop, ~$2,000/yr), Togal.AI ($299/mo, AI), maybe Beam AI (done-for-you), The EDGE (drywall-specific); cites myquoteiq/gitnux/STACK drywall page | "STACK pricing 2026", "Togal pricing", "drywall takeoff software reviews" |
| 3 | "does the AI actually get wall types right or do I still have to check everything" | Hedged: AI accuracy varies by drawing quality; cites Togal's KU study, Reddit skepticism; advises trial on own plans | "AI takeoff accuracy", "Togal review", "r/estimators AI takeoff" |
| 4 | "anything cheaper than 300 a month for a small company" | Suggests STACK free tier, Easy Takeoffs, Square Takeoff, Kreo; Quotr *could* appear here only if its $79.90 price is on third-party pages (it is not, and stale $299.90 pricing persists in ~13 Quotr URLs) | "cheapest AI takeoff software", "drywall takeoff software free" |
| 5 | "my estimator might quit, can I just pay someone to do takeoffs" | Lists offshore estimating firms and Beam AI; may cite Quotr's service post anonymously ("one service charges $0.25/sq ft") as in C12 | "drywall estimating services cost", "outsourced takeoff price per sq ft" |
| Shortlist | — | **STACK, Togal.AI, PlanSwift (+ Beam AI for service)** — Quotr absent | — |

**(3) Gap verdict per prompt cluster [DESIGN]**

| Cluster | Who owns it | Quotr status | Verdict | Fastest lever |
|---|---|---|---|---|
| Trade "best takeoff software" (drywall, flooring, roofing) | Vendor trade listicles (myquoteiq, STACK, estimatingedge), list farms (gitnux, worldmetrics, exayard), review directories | Absent (own listicle retrieved in R1 only) | **High gap, winnable** | Capterra/G2 listing + finish-trade reviews; inclusion on exayard/constructioncoverage/gitnux-type lists; rewrite trade hubs |
| Trade how-to / quantities (P2-type) | Calculators (HomeAdvisor, Easy Takeoffs, Procore, BuildVision, CertainTeed) | Absent; no calculators | **High gap, winnable** | Drywall, flooring-waste, roof-squares-from-plans, concrete-yardage calculators |
| Reviews node ("X reviews", "X cons") | Capterra/GetApp/Software Advice/TrustRadius | Not listed | **Blocking gap** | List on Capterra network + G2; seed 10–20 verified finish-trade reviews |
| Alternatives (PlanSwift/STACK/MeasureSquare) | Competitor "alternatives" posts (Easy Takeoffs, Projul) + directories | Retrieved, not named | Medium gap | Rewrite alternatives posts with first-line direct answers + fix stale prices |
| New-construction roofing from plans | Beam roofing page, STACK, OST, Buildxact | Absent; trade page only | **Open lane** (aerial tools can't do it) | Roofing-from-plans guide + worked example + video |
| Outsourced takeoff price | Offshore service firms + Quotr (anonymous) | Cited, not named | Medium gap | Brand-attributed price sentences; explain 50k cliff |
| Factory-direct flooring/tile (Procurement) | Local "factory direct" dealers | Absent | **Open lane** | Landed-cost index for LVP/porcelain (extends roadmap R-19) |
| Spanish prompts | Unknown (untested) | Untested | Experiment | 3 Spanish pages + 3 tracked prompts |

### Gaps
- No real ChatGPT or Google AI Mode runs were possible from this environment; the Spanish prompts and F1–F12 have **no baseline**. Remaining fan-outs to run when budget allows: "AI drywall takeoff accuracy", "drywall estimating services cost per takeoff", "flooring takeoff software AI 2026", "roof takeoff from blueprints software", "concrete takeoff software free", "software para estimar drywall", "buy LVP factory direct contractor".

---

## P. GEO system for this ICP on and off quotr.ai

### Takeaway
Build trade hubs that answer "does it do my trade / what it costs / start tonight" in 60 words, add four calculators and three decision pages, publish one bilingual original dataset on finish-trade bidding, get listed and reviewed on the Capterra network and G2, and run a Spanish pilot; keep Procurement as a flooring/tile cross-sell, not the lead.

### Cited Findings
- Engines rarely cite homepages and favor single-topic pages several folders deep; product, pricing and spec pages lead ChatGPT retrieval at 16.4% after GPT-5.6 — [Similarweb](https://aisearch.similarweb.com/blog/most-cited-domains-llms/), [Peec](https://docs.peec.ai/research/gpt-56-product-pages-vs-listicles) (via framework). Self-ranked listicles rarely get the publisher recommended (69% did not) — [Something Inc.](https://somethinginc.com/blog/2026-ai-citation-data-review/) (via framework). Median citation half-life ~4.5 weeks; 75% of LLM-cited pages updated within a year — [NoGood](https://nogood.io/blog/content-freshness-ai-citations/) (via framework). Schema and llms.txt are not citation levers — [Ahrefs schema test](https://ahrefs.com/blog/schema-ai-citations/), [Ahrefs llms.txt](https://ahrefs.com/blog/llmstxt-study/) (via framework).
- Quotr's drywall trade page had ~25 unique words at audit; Quotr has no trade calculators; calculators earned three software vendors citations on P2 — `competitor-landscape.md` §3. ~13 Quotr URLs still show retired $299.90 "Solo" pricing — `product-and-features.md`.
- Measurement must be distributional: <1% identical brand lists across runs; 50 prompts daily beats 10 prompts ×5; treat changes as real only beyond ±15% WoW / ±10% MoM and persisting 3 periods — [SEJ/SparkToro](https://www.searchenginejournal.com/ai-recommendations-change-with-nearly-every-query-sparktoro/566242), [Peec](https://peec.ai/blog/the-key-to-prompt-tracking), [Texta](https://www.texta.ai/blog/answer-variability-study-why-chatgpt-gives-different-answers) (via framework).

### Inferences
**1. Owning pages on quotr.ai [DESIGN]** (existing slugs reused where they exist; "new" = create)

| Type | Title | Slug | Mode | Key content |
|---|---|---|---|---|
| Trade hub (rewrite) | Drywall & Metal Framing Takeoff Software — Boards, Studs and Wall Types from PDF Plans | /software/trades/drywall/ | Both | 60-word answer (trades, price $79.90, trial); wall-type/partition-schedule demo; finish levels; per-board vs per-SF estimate templates; FAQ |
| Trade hub (rewrite) | Flooring Takeoff Software — SF by Finish, Waste and Boxes from Plans | /software/trades/flooring/ | Both | Room-by-finish detection; waste presets by pattern; carpet SY; stairs/transitions; Procurement callout (LVP, if confirmed) |
| Trade hub (rewrite) | Roofing Takeoff from Plans for New Construction — Squares, Pitch, Ridge/Hip/Valley | /software/trades/roofing/ | Both | When aerial reports work vs when plans are required; worked example |
| Trade hub (new, confirm not existing) | Acoustical Ceiling Takeoff from Reflected Ceiling Plans | /software/trades/acoustical-ceilings/ | Considered | RCP reading, grid/tile/wall-angle counts |
| Trade hubs (rewrite/new) | Concrete flatwork; Tile; Painting; Siding (new); Insulation | /software/trades/concrete/, /tile/, /painting/, /siding/ (new), /insulation/ | Considered | Trade unit math + demo |
| Decision page | Takeoff Software for Small Subcontractors: Price per Seat and per Bid (2026) — STACK, PlanSwift, Togal, MeasureSquare, Quotr | /compare/takeoff-software-small-subcontractors/ | Considered | Anchor table with sources and dates; "choose X if…" rows that sometimes point away from Quotr (no self-ranking) |
| Decision page | Do It Yourself, AI Software or Outsource? Cost per Bid for Drywall, Flooring and Roofing Subs | /compare/software-vs-estimating-service-vs-outsourcing/ | Considered | Per-bid math; Quotr Service price incl. the 50k sq ft step explained |
| Decision page | PlanSwift Alternatives for Finish Trades (Browser, Mac, Keep Your Assemblies) | /blog/planswift-alternative/ (rewrite existing alternatives post) | Considered | Migration steps; corrected PlanSwift price with source |
| Answer + calculator | Drywall Calculator: Sheets, Mud, Tape and Waste from Wall Area | /tools/drywall-calculator/ | Urgent | Shows formula; links to "do it from PDF" |
| Answer + calculator | Flooring Waste Calculator (LVP, tile, carpet by pattern) | /tools/flooring-waste-calculator/ | Urgent | Pattern-based waste; boxes |
| Answer + calculator | Roof Squares from Plans Calculator (pitch factor) | /tools/roof-squares-calculator/ | Urgent | Pitch multipliers; ridge/hip/valley LF |
| Answer + calculator | Concrete Yardage Calculator for Flatwork | /tools/concrete-calculator/ | Urgent | CY, short load, rebar estimate |
| Urgent page | Bid Due Tomorrow? Drywall Takeoff from Your PDF Tonight | /service/drywall-takeoff-overnight/ (only if turnaround can be guaranteed) | **Hot** | One cue, one price, one SLA (resolve the 24 h vs 3–4 day conflict first) |
| Answer page | How to Read Wall Types and Partition Schedules for a Drywall Takeoff | /blog/drywall-wall-types-partition-schedule-takeoff/ | Considered | Plan excerpts, checklist of commonly missed scope |
| Answer page | How Drywall Subs Price per Board vs per SF (2026, by State) | /data/drywall-pricing-2026/ | Cold | Original survey data (below) |
| Procurement cross-sell | LVP and Porcelain Tile: Factory-Direct Landed Cost vs US Distributor (Q1 2027) | /data/factory-direct-flooring-tile-price-index/ | Cold | Extends roadmap R-19; FOB vs DDP; lead time; QC; only categories Quotr confirms |
| Spanish pilot | Software de takeoff y estimados con IA para contratistas de drywall, pisos y techos | /es/ (hub) + /es/drywall/, /es/techos-desde-planos/, /es/desperdicio-pisos/ | Both | Bilingual-reviewed; Spanish video embedded |

**2. Proof assets / original data [DESIGN]**
- **Finish-Trade Bidding Benchmark 2027** (bilingual survey, target n = 200–400 via AWCI/NWFA/NRCA newsletters, Hispanic orgs, supply houses): bids/week, hit rate, hours per takeoff, tools used, per-board/per-square/per-SF prices by state, waste factors used. Publish with method page; pitch to Walls & Ceilings, Roofing Contractor, FCNews. No such dataset was found in any retrieved source.
- **Open accuracy test**: 10 real plan sets per trade (drywall boards by wall type, flooring SF by finish, roof squares) — Quotr AI vs a named independent estimator, with error distribution published.
- **Three finish-trade case studies** (Texas drywall, Florida flooring/tile, new-construction roofing) — Quotr currently has only RL Electric (electrical).
- **Price index** (monthly or quarterly): factory-direct vs distributor for LVP/porcelain (Procurement) and an input-cost tracker citing BLS PPI (gypsum, asphalt shingles) — sources to verify.

**3. Off-site placements ranked by leverage per hour [EST]**

| Rank | Placement | Why | Effort |
|---|---|---|---|
| 1 | Capterra/GetApp/Software Advice + G2 listings under "Quotr.ai", 10–20 verified reviews from finish-trade users | Owns the "reviews" fan-out node (R2–R4) and feeds alternatives pages; Togal has no Capterra reviews (open lane) | 6–10 h + customer asks |
| 2 | Inclusion on lists engines cite for C4/C5/N4 (exayard, constructioncoverage, buzzbid, servicebusinessacademy, gitnux/worldmetrics/wifitalents-type farms, ConstructConnect guide) with a 40–60-word blurb and $79.90 price | These pages are the citation pool | 1 h per pitch, 2–6 weeks |
| 3 | YouTube: one chaptered video per trade hub on a real plan (English), plus 2 Spanish videos (drywall, roofing-from-plans) | YouTube is a top AIO/AI Mode source (framework) | 4–6 h per video |
| 4 | Fix stale pricing on ~13 Quotr URLs and llms.txt | Engines repeat $299.90 entry price | 2–3 h |
| 5 | Disclosed founder/estimator participation in r/estimators, r/Drywall, r/Flooring, r/Roofing, ContractorTalk, DrywallTalk (9:1 rule) | r/estimators cited in C4; 3–6-month play | 1–2 h/week |
| 6 | Contributed data articles in Walls & Ceilings, Roofing Contractor, FCNews (from the benchmark) | Earned mentions; news/partner citations rising in ChatGPT (framework) | 8–12 h after data exists |
| 7 | Hispanic construction orgs (NHCA, HCC, USHCC chapters): Spanish webinar "estimados profesionales para contratistas generales" | Spanish pilot distribution; recruitment for interviews | 4–6 h |
| 8 | Supply-house partnerships (drywall, roofing, flooring distributors) | Counter referrals; co-branded calculators | Speculative; longer cycle |

**4. Refresh cadence [DESIGN]:** pricing/decision/comparison pages monthly; calculators and trade hubs quarterly; price index monthly or quarterly; seasonal pages pre-warmed 4–6 weeks before trigger (bid season by mid-January; Florida roofing by May; tariff pages before Jan 1, 2027).

**5. Tracking prompts to freeze (run 3–5×, ChatGPT + Google AI Mode/AIO, Perplexity optional; report cluster-level mention / citation / recommendation rates with ± ranges)**

| # | Prompt | Group |
|---|---|---|
| TP1 | best takeoff software for drywall contractors (= T04) | Category |
| TP2 | best takeoff software for flooring contractors (= T05) | Category |
| TP3 | best roofing takeoff software for new construction from plans (= T51) | Category |
| TP4 | F1 (Houston drywall, full context) | Full-context |
| TP5 | F7 (estimator quit — service vs software, Las Vegas) | Full-context |
| TP6 | cheapest AI takeoff software for small subcontractors | Category |
| TP7 | can a flooring contractor buy LVP or porcelain tile factory direct with duties paid | Procurement |
| TP8 | mejor software para estimar drywall | Spanish experiment |

**6. Do / skip / ignore**
- **Do:** trade hub rewrites with 60-word answers; four calculators; Capterra/G2 listing + finish-trade reviews; list-inclusion outreach; roofing-from-plans lane; per-bid price math (incl. Service step at 50k sq ft); bilingual benchmark survey; real-plan videos; stale-price cleanup; Spanish pilot (hub + 3 pages + 2 videos); Procurement cross-sell for flooring/tile only where categories are confirmed; switch interviews (6–12 recent sign-ups/churns) that record exact prompts.
- **Skip:** city-templated pages ("drywall takeoff software in [city]"); insurance/storm reroof measurement content (aerial vendors' lane); self-ranked "best drywall software" listicles as a lead tactic; full /es/ site mirror before demand evidence; schema/llms.txt as citation levers; paid placements before baseline.
- **Ignore:** Claude/Copilot/Grok tracking for this ICP; generic "trusted by thousands" social proof; choice-overload arguments; unverified "AI is 99% accurate" claims without method.

**Procurement cross-sell note [L]:** the cleanest bridge is the flooring/tile sub who **supplies and installs** (J5, M6): their margin is material margin, they feel tariff and distributor price swings directly, and Plus already includes "10% off procurement." Drywall, roofing, concrete, painting and insulation are not Procurement categories, so do not attach Procurement messaging to those hubs. Cabinets matter only for remodel-oriented finish subs ahead of the Jan 1, 2027 tariff step.

### Gaps
- Quotr facts to confirm before publishing: whether an acoustical-ceilings trade page exists; Service turnaround (24 h vs 3–4 days); meaning of Plus "takeoff credits"; Procurement categories (flooring, tile); support level for Lite; whether a Spanish UI or support exists (no evidence found).

---

## Q. Known / likely / speculative

### Takeaway
Firm counts for drywall and roofing, Hispanic workforce shares, permit geography, competitor prices and review complaints are known; the psychology, trigger timing and channel weights are likely; Spanish-language search behavior, hot-hour timing and the size of the Procurement cross-sell are speculative.

### Cited Findings
| Claim class | Known (cite freely) | Likely (label as inference) | Speculative (validate first) |
|---|---|---|---|
| Size | Drywall/insulation 20,760 establishments, 250,758 employees; roofing 25,519 / 215,242 (CBP 2023, via third parties); ~8–12 employees per establishment [CALC] | Non-employer tail ≥ employer base in roofing | Counts for painting, tile, concrete, siding (not retrieved) |
| Hispanic share | 70,571 Hispanic-owned construction employer firms (2021), top sector; Hispanic share of construction workforce ~32.8–35.4%; drywall 68.5–75.2%, roofing ~64%, painting 62.5%; foreign-born drywall 57% | Many owners came up from crews and are bilingual | Owners research software in Spanish; Spanish AI prompts have measurable demand |
| Geography | Houston, DFW lead permits; Phoenix, Atlanta, Charlotte, Austin next; Orlando/Tampa top 10; Phoenix −15% in 2025 | Texas Triangle is the best Spanish-pilot market; Florida roofing differs on code/storms | Las Vegas/Raleigh priority (no data retrieved) |
| Tools & pains | PlanSwift crashes/support/cost; STACK renewal creep/slow large sets; MeasureSquare roll-goods/stairs/LVP gaps; aerial reports weak on new construction; prices of STACK, PlanSwift, Togal, Beam | Small-shop price sensitivity dominates; trade-specific accuracy is the main anxiety | Togal/Beam/EagleView complaint themes (not mined) |
| AI visibility | Quotr absent from C4, C5, N4, P2, C14; own listicle retrieved in R1 but not named; reviews node owned by Capterra network | Calculators + reviews + list inclusion move trade prompts first | Spanish prompts' answer pool |
| Psychology | Robust biases: defaults, anchoring, fresh start, time pressure; fragile: social proof, choice overload | Loss aversion about bad bids > software spend; night/Sunday hot moments | Exact hours of hot searching |
| Economics | Lite $959/yr vs $1,600–4,000 budget; Service $0.25/$0.10 per sq ft with a step at 50k | Service is uneconomic for routine finish-trade bids, good for overflow | Plus credits = ~$500 of Service per month |

### Inferences
- The single biggest unlock for this ICP is not content volume but **third-party presence on the reviews and list nodes** plus **trade-unit calculators**, because those are the formats that won every trade prompt observed.

### Gaps
- Everything above needs a first real baseline in ChatGPT and Google AI Mode (none possible here) and 6–12 switch interviews with finish-trade owners, at least 3 of them Spanish-dominant, asking "what exactly did you type, and into what?"
