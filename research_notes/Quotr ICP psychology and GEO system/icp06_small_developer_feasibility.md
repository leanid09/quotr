# ICP 6 — The small-to-mid real estate developer who needs a feasibility-grade construction cost estimate (Quotr.ai)

**Research conditions (read first).** Written 2026-11-06. Fresh web evidence comes from 17 WebSearch calls made before the shared per-turn search budget (200 calls across all agents) ran out. WebFetch and curl were blocked by the session's network policy for biggerpockets.com, reddit.com, census.gov, ternercenter.berkeley.edu, nahb.org, hcd.ca.gov, rlb.com and quotr.ai, and WebSearch refuses a reddit.com domain filter. So: (1) every community quote below is **verbatim search-index snippet text or a verbatim thread title** from BiggerPockets. The thread pages were not opened, so poster names and dates were not visible. (2) No Reddit, LinkedIn or podcast quotes could be collected. (3) The planned fan-out runs ("cost to build a fourplex in Oakland 2026" and others) were **not** run. Section O records the nine open-web searches made during research as retrieval proxies and adds the real Perplexity runs from the September 2026 Quotr audit stored in this repo. (4) Quotr facts come only from the repo's audited notes (`geo-brain/00-quotr/*`, `research_notes/Quotr GEO AEO strategy audit/*`), which cite quotr.ai pages read on 2026-09-25. Engine-mechanics and psychology figures come from the uploaded ICP-depth framework and carry its URLs ("via framework"). Labels: **Known** = sourced; **Likely** = inference from sourced facts; **Speculative/Simulated/Estimate** = say so.

This dossier deepens Persona 4 (developer) and part of Persona 5 (fund/underwriter) in `geo-brain/00-quotr/audiences-and-personas.md`. The prompt library already has a developer block (L-129 to L-146, E-005, E-011, E-073; tracking IDs T08, T12, T28, T45, T47). This file does not repeat them. It adds the coding chains, persona-loaded prompts, geo segments and a coded community sample.

---

## A. Definition and size

### Takeaway
ICP 6 is defined by a **moment** more than by a firm type: a sponsor who needs a credible hard-cost number *before* buying land, before the GC bids, or for a lender or investor. It spans NAICS 236117 for-sale builders, small multifamily and missing-middle sponsors, ADU and lot-split builders, and investor-developers who own each deal through a one-off LLC. The only retrievable count for 236117 is an unverified aggregator figure of about 11.8k firms and 12.6k establishments. Census CBP/SUSB, NAHB, NMHC and BiggerPockets membership figures could not be pulled this session.

### Cited Findings
- NAICS 236117 covers establishments "primarily engaged in building new homes on land that is owned or controlled by the builder", and speculative or merchant builders of single-family homes are classed under 236117, not 236115 — [NAICS.com 236117](https://www.naics.com/naics-code-description/?v=2017&code=236117); [IBISWorld 236115 description](https://www.ibisworld.com/classifications/naics/236115/new-single-family-housing-construction-except-for-sale-builders)
- An aggregator reports **11,761 firms, 12,612 establishments and 130,923 employees** in NAICS 236117. The year and underlying source are not stated, so this is **unverified** against Census CBP — [Mewayz industry data 236117](https://data.mewayz.com/industry/236117)
- Hard construction costs are **more than 60% of total development costs** for California multifamily (240 projects, 2009–2018). The hard-cost estimate is the biggest single line in this buyer's pro forma — [Terner Center, Hard Construction Costs (March 2020)](https://ternercenter.berkeley.edu/wp-content/uploads/2020/08/Hard_Construction_Costs_March_2020.pdf)
- Typical small-deal shapes in forum threads: duplexes with units "near 1,000 sq ft" (a South Florida builder's advice), fourplexes, 1,200–1,800 sq ft investor-grade homes (Bradenton), 400 sq ft garage-conversion ADUs (San Diego) and a 6-story, 12-unit building — [BP South Florida duplex thread](https://www.biggerpockets.com/forums/44/topics/1283662-first-duplex-build-in-south-florida-fha-construction-loan-validate-construction); [BP Bradenton thread](https://www.biggerpockets.com/forums/311/topics/1154803-cost-to-build-a-duplex-or-4plex-in-bradenton-fl); [BP ADU San Diego thread](https://www.biggerpockets.com/forums/61/topics/805149-adu-strategies-in-san-diego); [BP 12-unit thread](https://www.biggerpockets.com/forums/44/topics/287541-cost-to-build-a-6-floor-12-units-apartment-building)
- Financing context from BiggerPockets: a builder who ran over budget refinanced mid-build with a hard-money lender at **90% loan-to-cost for 12 months**, with the added funds tied to an updated, more accurate budget. The same article uses a **1% extension fee on a $3M loan** as an example of margin strain — [BiggerPockets blog, construction loans](https://www.biggerpockets.com/blog/getting-your-construction-project-over-the-finish-line)
- The "investor graduating from fix-and-flip" path shows up in thread titles: "Building a fourplex as my first deal. Trial by fire.", "Building a 4-plex instead of buying one…", "Calling it quits, should I build my own duplex?" — [BP 154511](https://www.biggerpockets.com/forums/88/topics/154511-building-a-fourplex-as-my-first-deal-trial-by-fire); [BP 265300](https://www.biggerpockets.com/forums/44/topics/265300-building-a-4-plex-instead-of-buying-one?page=1); [BP 861625](https://www.biggerpockets.com/forums/44/topics/861625-calling-it-quits-should-i-build-my-own-duplex)
- Quotr already routes "For developers" from the homepage to /service/ (also served at /developers/), and its boilerplate describes Quotr Service as "done-for-you cost estimates and pro formas for developers and busy teams" — repo `geo-brain/00-quotr/product-and-features.md` and `entity-fact-sheet.md` (from [quotr.ai/service/](https://quotr.ai/service/) and blog search-index text, 2026-09-25)

### Inferences
- **Segment map (Likely; the sizes are illustrative assumptions, not measured):**

| Sub-segment | Typical project | Typical GFA (assumption) | Team (Likely) | Who demands the cost number |
|---|---|---|---|---|
| ADU builder / investor (CA) | 1–4 ADUs per lot, or ~10/yr | 400–1,200 sq ft each | 1–3 | Self, hard-money or HELOC lender |
| SB 9 / lot-split / small-lot subdivider | 2–10 homes | 2,000–15,000 sq ft | 1–5 | Land seller's deadline, construction lender |
| Missing-middle infill (duplex to 12-plex) | 2–12 units | 2,000–12,000 sq ft | 1–5 | Lender (LTC), private equity partners |
| Small multifamily sponsor (13–150 units) | walk-up, garden, 5-over-1 | 12,000–150,000 sq ft | 3–10 + outside GC/architect | Lender, LP investment committee |
| Build-to-rent (BTR) community | 20–150 homes | 30,000–200,000 sq ft | 3–10 | Institutional capital partner |
| Light commercial / conversion | retail-to-resi, small office | 5,000–40,000 sq ft | 1–5 | Lender, tenant |

- **Sizing method to run when Census access exists (Likely-valid method, numbers not pulled):** (a) Census CBP/SUSB establishment counts for 236117 and 237210 by state; (b) Building Permits Survey 2–4-unit and 5+-unit structures by CBSA, divided by an average units-per-project assumption, gives a project count; (c) CA HCD APR dashboard ADU permits by jurisdiction; (d) the share of projects by sponsors with fewer than 10 staff (NAHB builder surveys). The output should be stated as a range per metro, not a national headline.
- Most of the ICP is invisible in NAICS: one-deal LLCs and investor-developers file under real estate or holding codes, so 236117 is a floor, not the population.

### Gaps
- Census CBP/SUSB counts for 236117, 237210 and 531390, NAHB small-builder shares, NMHC sponsor counts, BiggerPockets membership and ULI/NAIOP small-developer membership: not retrieved (census.gov blocked; search budget exhausted).
- Team composition (1–10 staff) is a brief assumption, not a sourced figure.
- Typical deal sizes in dollars by sub-segment: no survey source found.

---

## B. Geography

### Takeaway
Hard costs differ by multiples across the metros this ICP builds in. California production costs run about **2.3× Texas per rentable sq ft**, the Bay Area carries an **$81/sq ft premium and LA $35/sq ft** over the rest of California, and forum anecdotes range from **~$120/sq ft (Indianapolis) to $400–$800+/sq ft (LA fire rebuild)**. Rules also differ: Texas SB 840 and SB 15 took effect Sept 1, 2025, and OZ 2.0 maps take effect Jan 1, 2027. So **a small set of data-backed metro pages is justified**; templated city pages are not. Priority for Quotr: Bay Area, LA, Texas (Austin/DFW), the Pacific Northwest, then Florida.

### Cited Findings
- Controlling for project characteristics, hard costs were **$81/sq ft higher in the Bay Area** and **$35/sq ft higher in the LA region** than in the rest of California. Prevailing-wage projects cost **$30/sq ft more**. Per-sq-ft hard costs rose **25%** over 2009–2018 (240 projects) — [Terner Center 2020](https://ternercenter.berkeley.edu/wp-content/uploads/2020/08/Hard_Construction_Costs_March_2020.pdf) (data now 7+ years old; no newer Terner per-sq-ft update was found)
- RAND (April 2025): California's production cost per rentable sq ft is **2.3 times** Texas's — [Planetizen summary](https://www.planetizen.com/node/134768) (search snippet); the RAND report Perplexity cites for multifamily cost questions is [RAND RRA3743-1](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA3700/RRA3743-1/RAND_RRA3743-1.pdf) (repo audit P3)
- **Texas SB 15 and SB 840 took effect September 1, 2025.** SB 840 allows multifamily and mixed-use projects with at least 65% residential space in areas zoned office, commercial, retail, warehouse or mixed-use, with no rezoning or special permit, and limits parking, traffic-study and utility-upgrade demands on commercial-to-residential conversions. SB 15 (small lots) applies in cities over 150,000 people in counties over 300,000; minimum-lot figures differ by source (lots of 4,000 sq ft or less, versus Fort Worth's 3,000 sq ft on certain 5-acre-plus unplatted parcels) — [Texas Senate SB 15 analysis](https://capitol.texas.gov/tlodocs/89R/analysis/html/SB00015I.htm); [Greater Palestine SB 840 notice](https://www.gptx.org/News-Articles/Notice-Effective-September-1st-Senate-Bill-840); [Foley](https://www.foley.com/insights/publications/2025/07/texas-enacts-critical-real-estate-reforms-senate-bills-15-17-840/); [Fort Worth](https://www.fortworthtexas.gov/departments/development-services/development-legislation); [Austin Nov 2025 presentation](https://services.austintexas.gov/edims/document.cfm?id=462645)
- California: HCD's APR dashboard shows **more than 100,000 ADUs permitted since 2017** (cumulative; secondary source) — [Casita Coalition](https://casitacoalition.squarespace.com/casita-coalition-blog/california-reaches-major-housing-milestonemore-than-100000-adus-permitted-since-2017). Jurisdictions file APRs with HCD/OPR **by April 1** for the prior calendar year — [Placer County APR deck](https://www.placer.ca.gov/DocumentCenter/View/86623/2025-031325-PowerPoint-Presentation-Item-1A---2024-Housing-Element-and-General-Plan-Annual-Progress-Reports); ABAG runs an APR and ADU affordability-survey update — [ABAG](https://abag.ca.gov/technical-assistance/annual-progress-reports-update-hcd)
- **OZ 2.0:** the new map takes effect **January 1, 2027**. Governors nominated tracts July–September 2026, with an extension to Oct 28, 2026, and Treasury certification runs in November 2026 (now). Qualified Rural Opportunity Funds get a **30% exclusion** of deferred gain after five years. One source claims a 2027–2028 overlap with OZ 1.0 maps. End date: Dec 31, 2036 per a HUD deck, conflicting with an earlier House-stage summary (2033) — [HUD OZ overview deck](https://invest.hawaii.gov/wp-content/uploads/2026/06/HUD_OZ-Overview.pdf); [Kiplinger](https://www.kiplinger.com/taxes/tax-planning/how-governors-pick-opportunity-zone-2-designations); [Bernstein Shur](https://www.bernsteinshur.com/insights-events/opportunity-zones-2-0-a-new-era-for-investment-especially-in-rural-communities/); [EIG](https://eig.org/opportunity-zones-2-0-where-things-stand/); [CLA](https://www.claconnect.com/en/resources/blogs/real-estate/rural-america-prepare-for-changes-to-the-opportunity-zone-program)
- Metro cost anecdotes (BiggerPockets; anecdotal, many years old):
  - Austin: quotes "around $180-200 a square foot with rental grade finishes" — [BP 931457](https://www.biggerpockets.com/forums/44/topics/931457-how-much-would-it-cost-me-to-build-a-fourplex-in-austin-tx)
  - Bradenton FL: ~$165/sq ft conditioned, $90–100 garages, $60 porches — [BP 1154803](https://www.biggerpockets.com/forums/311/topics/1154803-cost-to-build-a-duplex-or-4plex-in-bradenton-fl)
  - South Florida duplex: planner's $250–300/sq ft versus a builder's suggested $205–225/sq ft with a GC (thread ~211 days old at index time) — [BP 1283662](https://www.biggerpockets.com/forums/44/topics/1283662-first-duplex-build-in-south-florida-fha-construction-loan-validate-construction)
  - Central Florida: a GC quoted $80–90/sq ft for a block duplex from a stock stamped plan (~415 days old) — [BP 571271](https://www.biggerpockets.com/forums/52/topics/571271-any-one-in-the-central-florida-build-quadplexes#post_5388993)
  - Portland: $144–154/sq ft (fourplex) and $155–197 (townhouse) from a comps method (~2,100 days old); a Portland-area GC cited $150/sq ft hard plus $20k/unit SDC fees — [BP 921760](https://www.biggerpockets.com/forums/738/topics/921760-portland-4plex-townhome-build-cost-and-contractor-recommendations)
  - Indianapolis: $120–140/sq ft builder quotes — [BP 661426](https://www.biggerpockets.com/forums/44/topics/661426-duplex-or-fourplex-building-cost-in-indianapolis)
  - San Diego ADU: $250/sq ft construction plus $50/sq ft soft (citing Maxable; thread attribution per search summary) — [BP 805149](https://www.biggerpockets.com/forums/61/topics/805149-adu-strategies-in-san-diego)
- LA fire rebuild: **$400–$800+/sq ft** in a Perplexity answer that cited Bloomberg and local GCs (Benson Construction, Amerbuild, UBIC, Vaisman); Quotr was absent even though it sells a "Fast Cost Estimation (Residential LA Fire Rebuilding)" sample — repo `research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md` (run 2026-09-25)
- Quotr's own geographic proof is Bay Area residential: procurement cards at Myren Dr, Saratoga ($97,000 vs a $187K–$218K Bay Area market range), Stratford Ct, Monte Sereno and Skyfarm Dr, Hillsborough; the LA fire-rebuild sample; and the free FireTips app for LA fire victims (Feb 2025) — repo `product-and-features.md`, `entity-fact-sheet.md` ([quotr.ai/procurement/](https://quotr.ai/procurement/); [firetips.quotr.io](https://firetips.quotr.io/))

### Inferences
- **Priority geo segments for Quotr (Likely; the scores are judgment):**

| # | Segment | Evidence row | Job | Regulatory posture | Prompt stems | Fit for Quotr |
|---|---|---|---|---|---|---|
| 1 | **Bay Area infill and lot-split developer** (Oakland, San Jose, Peninsula, Contra Costa) | Highest CA hard-cost premium (+$81/sf, Terner); Quotr HQ; 3 procurement cards in Saratoga/Monte Sereno/Hillsborough; ADU threads for San Jose (BP 466365) | Prove a fourplex, SB 9 split or ADU pencils against Bay Area costs before closing | SB 9; ADU law; small-lot law (verify SB 684/SB 1123) | "cost to build fourplex Oakland 2026", "SB 9 lot split build cost San Jose" | **Highest**: home market, procurement savings most visible where costs are highest |
| 2 | **LA rebuild + ADU developer** (Altadena, Pacific Palisades, LA City ADU builders) | $400–$800+/sf rebuild answer with no Quotr; LA +$35/sf (Terner); 4 LA/SoCal ADU threads in the coded sample | Lender- or insurer-ready rebuild budget; repeatable ADU cost model | Fire-rebuild permitting, ADU law, SB 9 | "cost to rebuild per sq ft Altadena 2026", "ADU cost Los Angeles 2026" | **High**: Quotr has a rebuild sample and FireTips, but no page |
| 3 | **Texas commercial-to-resi and small-lot developer** (Austin, DFW, Houston, San Antonio) | SB 840/SB 15 live since Sept 1, 2025; CA 2.3× TX cost gap (RAND); Austin $180–200/sf anecdote | Fast feasibility on newly by-right commercial parcels; BTR per-door budgets | SB 840 (≥65% residential by right in commercial zones), SB 15 small lots, Austin HOME (verify) | "SB 840 multifamily commercial zoning cost to build", "BTR cost per door Texas 2026" | **Medium-high**: volume of new by-right sites; Quotr has no Texas proof yet |
| 4 | **Pacific NW middle-housing builder** (Portland, Seattle) | Portland $150/sf hard + $20k/unit SDC; soft costs 30–35% of hard (BP 921760) | Price 2–6 units on single lots allowed by state middle-housing law | WA HB 1110, OR HB 2001 (verify) | "cost to build fourplex Seattle 2026 HB 1110" | **Medium**: rules differ, cost data thin |
| 5 | **Florida infill/Live Local developer** (Tampa, South Florida, Sarasota-Manatee) | $165–300/sf spread in 3 Florida threads; Live Local Act (verify) | Underwrite mixed-income projects on commercial parcels | Live Local Act (verify) | "Live Local Act project construction cost per unit" | **Medium-low**: far from home base |

- **Are geo pages justified?** Yes for 4–5 metro pages carrying distinct cost data and distinct rules (the CA–TX 2.3× gap and the $81/sf Bay Area premium are real, citable differences). No for dozens of templated "cost to build in {city}" pages, which the framework flags as scaled-content-abuse risk (via framework: [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies)).
- OZ 2.0 creates a **cross-geography trigger segment** (rural QROF projects from 2027) rather than a metro page. It is best served by one answer page.

### Gaps
- Census BPS 2024–2026 permit counts by metro (2–4 and 5+ units): not retrieved.
- Statewide CA ADU permits per year (the brief's "~25k+/yr") could not be verified this session; only the cumulative "100,000+ since 2017" is sourced.
- **Unverified regulatory list (training knowledge; verify before publishing):** CA SB 9 (effective Jan 1, 2022); SB 684 (small-lot subdivisions of up to 10 units on multifamily-zoned parcels, effective mid-2024) and SB 1123 (extends it to vacant single-family lots, effective mid-2025); WA HB 1110 middle housing; OR HB 2001; Montana 2023 duplex/ADU laws (litigation history); Austin HOME phases 1–2 (2023–2024); Florida Live Local Act (2023, amended 2024). An unread [JD Supra "2026 California New Laws – Housing"](https://www.jdsupra.com/legalnews/2026-california-new-laws-key-updates-1480637/) and a CA SB 1122 (2025–26) bill analysis appeared in results and should be checked.
- Current (2026) third-party hard-cost indices (RLB, Cumming, JLL, Turner): not retrieved.

---

## C. Jobs-to-be-done (their words)

### Takeaway
Five jobs recur. The buyer's own words are thread titles, which double as prompt templates: "is this a good deal", "validate construction $$", "proof read my estimate", "over budget by 40%", "cost components breakdown".

### Cited Findings
- "How do you determine new construction costs and is this a good deal" — [BP 1104711](https://biggerpockets.com/forums/44/topics/1104711-how-do-you-determine-new-construction-costs-and-is-this-a-good-deal)
- "First duplex build in South Florida (FHA construction loan). Validate construction $$" — [BP 1283662](https://www.biggerpockets.com/forums/44/topics/1283662-first-duplex-build-in-south-florida-fha-construction-loan-validate-construction)
- "Proof read my estimate" — [BP 1179899](https://biggerpockets.com/forums/44/topics/1179899-proof-read-my-estimate)
- "Contractor suddenly over budget by 40%" — [BP 1105632](https://www.biggerpockets.com/forums/67/topics/1105632-contractor-suddenly-over-budget-by-40); "New Construction - Builder overbudget and might not close in time" — [BP 1058604](https://www.biggerpockets.com/forums/51/topics/1058604-new-construction-builder-overbudget-and-might-not-close-in-time)
- "Please Advise: ADU Cost Components Breakdown?" — [BP 861664](https://www.biggerpockets.com/forums/548/topics/861664-please-advise-adu-cost-components-breakdown); "Pre-design ADU plans" — [BP 880212](https://www.biggerpockets.com/forums/548/topics/880212-pre-design-adu-plans)
- "Need help with analysis on a new build on purchased land" — [BP 930277](https://biggerpockets.com/forums/88/topics/930277-need-help-with-analysis-on-a-new-build-on-purchased-land)

### Inferences
| # | Job (buyer's words → JTBD) | When | Quotr line |
|---|---|---|---|
| J1 | "Is this a good deal?" → *Tell me, before my feasibility period runs out, whether this lot pencils at a hard cost I can defend.* | Land under LOI or contract | Service (estimate + pro forma) |
| J2 | "Validate construction $$" → *Check the GC's or builder's number independently, before I sign it or my lender sees it.* | GC budget received; loan application | Service |
| J3 | "Proof read my estimate" → *Make my budget look credible to a lender or LP: line items, contingency, soft costs.* | Term sheet, investor memo | Service (lender-format estimate + pro forma) |
| J4 | "Over budget by 40%" → *Find where the bid is high and what I can value-engineer, fast, without killing rents or resale.* | Bid day; mid-construction | Service + Procurement (finish-package savings) |
| J5 | "Cost components breakdown" / "Pre-design plans" → *Get a line-item number from early or partial drawings and reuse it across deals.* | Massing/SD stage; repeat ADU or BTR product | Software (Plus) for repeat builders; Service for one-offs |

### Gaps
- No switch interviews have been run with Quotr's developer customers (BiltWise or others). The job wording comes from forum titles, not from buyers of Quotr.

---

## D. Psychology

### Takeaway
The buyer is a deal-maker whose identity rests on "finding the deal". Optimism shows up as undersized contingency and stale GC numbers. Two dread scenarios dominate: being anchored by the GC's number, and having the lender or LP poke holes in the budget. The most powerful bias here is **anchoring on a single $/sq ft figure**, which is also the most robust bias in the replication record. Hot moments run on a clock (feasibility period, lender deadline, bid day). Cold moments are deal-screening sessions.

### Cited Findings
- **Anchoring replicates strongly** (Many Labs: "substantially more powerful than Kahneman's original study suggested"); **defaults/status quo d = 0.68**; temporal landmarks are robust (e.g., "diet" searches +14.4% at the start of a week). Generic social proof is fragile (0.94 pp in 126 RCTs) and choice overload averages d = 0.02 — via framework: [Scientific American](https://www.scientificamerican.com/article/dozens-of-labs-respond-to-bolster-reliability-of-psychology-research); [Jachimowicz et al.](https://ideas.repec.org/a/cup/bpubpo/v3y2019i02p159-186_00.html); [Dai, Milkman & Riis](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf); [DellaVigna & Linos](https://www.nber.org/system/files/working_papers/w27594/w27594.pdf); [Scheibehenne et al.](https://academic.oup.com/jcr/article/37/3/409/1816569)
- **Time pressure** pushes buyers toward noncompensatory rules, gives more weight to unique features and reduces deferral; the hot–cold empathy gap means cold planners underpredict what they will want when hot — via framework: [Dhar & Nowlis](https://profiles.wustl.edu/en/publications/the-effect-of-time-pressure-on-consumer-choice-deferral/); [Stanford Center on Longevity](https://longevity.stanford.edu/?p=21187)
- Trust in AI recommendations alone falls from **42% under $50 to 5% over $500**, and 86% of US shoppers who used AI for product research verified elsewhere. A multi-million-dollar build decision will always be cross-checked — via framework: [MarTech](https://martech.org/the-ai-shopping-stats-2026-what-you-need-to-know/)
- $/sq ft anchoring in the buyer's own words: "120 is a safe estimate" ([BP 661426](https://www.biggerpockets.com/forums/44/topics/661426-duplex-or-fourplex-building-cost-in-indianapolis)); and the comps heuristic "get comps, subtract the land value, then divide by the sq ft to get a ballpark estimate of the cost/sq ft to build new" ([BP 921760](https://www.biggerpockets.com/forums/738/topics/921760-portland-4plex-townhome-build-cost-and-contractor-recommendations))
- Optimism and its cost (practitioner sources): one guide calls undersized contingency the most common way developers "manufacture returns that don't survive execution"; another warns that setting contingency "based on what fits in the pro forma rather than what the project requires" "consistently produces overruns". A budget built from a GC estimate bid 18 months earlier, in a market up 12%, "will understate hard costs by 12% before the first change order is written" (search-snippet text) — [Innergy Integral, multifamily pro forma construction costs](https://integral-c94.pages.dev/resources/multifamily-proforma-construction-costs/); [Innergy Integral, construction budget overruns](https://integral-c94.pages.dev/resources/construction-budget-overruns/)
- Strategic fear of the GC's number: "Tell your contractor your budget?" — [BP 146350](https://www.biggerpockets.com/forums/67/topics/146350-tell-your-contractor-your-budget)
- A general cost article warns that $/sq ft "varies dramatically based on labor rates around the country", recommends hiring a takeoff and estimating firm once drawings and scopes exist, and advises against thin margins — [MPA Magazine](https://www.mpamag.com/us/specialty/commercial/how-to-effectively-estimate-construction-costs-on-a-property/212820)

### Inferences
- **Identity:** an entrepreneur and deal-maker, often an ex-flipper used to rehab budgets they control line by line. New construction removes that control (GC, architect, city), which raises anxiety and the appetite for an *independent* number.
- **Decision style:** satisficing under a deadline. They want one defensible number with a range, not a model. Comparisons happen in cold mode, picks in hot mode.
- **Hot vs cold moments (Likely):**

| Moment | Mode | Clock | What they need first |
|---|---|---|---|
| Feasibility period running (LOI/PSA signed) | Hot | Days to weeks | Turnaround, price, "is this credible to my lender" |
| Lender asks for line-item budget | Hot | Term-sheet deadline | Lender-acceptable format, named preparer |
| Bid day: GC is 30% over | Hot | Equity/IC meeting | Line-item comparison, VE options with $ |
| Deal-screening session (evening/weekend, *speculative*) | Cold | None | $/sq ft and $/door ranges by metro and product, dated |
| Reform or OZ news; tax planning | Cold | Quarter or year end | "What can I build here and does it pencil?" |

- **Bias design rules (ranked by replication):** (1) *Anchoring* is robust: publish dated $/sq ft **and** $/door ranges by metro and product type, so the AI answer's anchor is Quotr's, with Quotr's name attached. (2) *Defaults/status quo* are robust: the default is the "free" GC precon number or comps minus land; content must name the default and show its failure mode (stale, padded, missing site work). (3) *Temporal landmarks* are robust: time content and refreshes to Jan 1 (new laws, OZ 2.0) and April 1 (CA APR data). (4) *Social proof* is fragile: skip "trusted by developers" lines and use a named lender-accepted sample or a named customer instead. (5) *Choice overload* barely moves anyone: a four-option comparison page is fine.

### Gaps
- No peer-reviewed source on optimism bias in small-developer cost estimates was retrieved (Flyvbjerg's work was not pulled). The Innergy Integral lines are practitioner opinion.
- Time-of-day/week patterns (the "Sunday deal analysis" brief) have no source here and are speculative.

---

## E. Four forces (verbatim quotes)

### Takeaway
Push comes from overruns and hidden site costs. Pull is toward a calculator, a breakdown or validation. Anxiety centers on the GC relationship and on whether the number survives scrutiny. Habit is the comps-minus-land rule of thumb and a single $/sq ft. Fourteen verbatim items with URLs follow. All are BiggerPockets search-index snippets or thread titles; Reddit, LinkedIn and podcast quotes could not be collected.

### Cited Findings
**Push (situation is unbearable)**
1. "Contractor suddenly over budget by 40%" (thread title) — [BP 1105632](https://www.biggerpockets.com/forums/67/topics/1105632-contractor-suddenly-over-budget-by-40)
2. "New Construction - Builder overbudget and might not close in time" (title) — [BP 1058604](https://www.biggerpockets.com/forums/51/topics/1058604-new-construction-builder-overbudget-and-might-not-close-in-time). Search summary of the thread: a builder claimed nearly $250,000 over a $781,000 fixed-price contract, pushing the construction loan past its one-year term (paraphrase, not a quote)
3. "My contractor has blown throw the allocated budget" (title, sic) — [BP 907059](https://www.biggerpockets.com/forums/12/topics/907059-my-contractor-has-blown-throw-the-allocated-budget)
4. "these cost can go as high as $40k if you end up in an area that requires ATU septic system" — [BP 1154803](https://www.biggerpockets.com/forums/311/topics/1154803-cost-to-build-a-duplex-or-4plex-in-bradenton-fl)

**Pull (the new solution attracts)**
5. "Where can I find a new construction calculator" (title) — [BP 705023](https://www.biggerpockets.com/forums/311/topics/705023-where-can-i-find-a-new-construction-calculator)
6. "Please Advise: ADU Cost Components Breakdown?" (title) — [BP 861664](https://www.biggerpockets.com/forums/548/topics/861664-please-advise-adu-cost-components-breakdown)
7. "… Validate construction $$" (title) — [BP 1283662](https://www.biggerpockets.com/forums/44/topics/1283662-first-duplex-build-in-south-florida-fha-construction-loan-validate-construction)

**Anxiety (of the new / of being wrong)**
8. "Tell your contractor your budget?" (title) — [BP 146350](https://www.biggerpockets.com/forums/67/topics/146350-tell-your-contractor-your-budget)
9. "Proof read my estimate" (title) — [BP 1179899](https://biggerpockets.com/forums/44/topics/1179899-proof-read-my-estimate)
10. "What is a reasonable estimate for constructing an ADU in LA?" (title) — [BP 792997](https://www.biggerpockets.com/forums/548/topics/792997-what-is-a-reasonable-estimate-for-constructing-an-adu-in-la)

**Habit (of the present)**
11. "His advise to me was to get comps, subtract the land value, then divide by the sq ft to get a ballpark estimate of the cost/sq ft to build new." — [BP 921760](https://www.biggerpockets.com/forums/738/topics/921760-portland-4plex-townhome-build-cost-and-contractor-recommendations)
12. "Using his method with comps my realtor sent me, my estimates for new construction for a fourplex = $144-$154/sq ft and for a townhouse = $155-$197/sq ft." — [BP 921760](https://www.biggerpockets.com/forums/738/topics/921760-portland-4plex-townhome-build-cost-and-contractor-recommendations)
13. "Around $165 per sq ft on conditioned space (for an average 1200 to 1800 sq ft house, 8-9ft high ceiling, everything is investor grade finishes), $90-100 per sq ft for garages/unconditioned storage, $60 per sq ft for porches/opened spaces." — [BP 1154803](https://www.biggerpockets.com/forums/311/topics/1154803-cost-to-build-a-duplex-or-4plex-in-bradenton-fl)
14. "Land- $40-$65/per sq ft (more in higher density zones), $150/ sq ft of hard costs for construction, $20k per unit in SDC fees. Your soft cost ratio will probably be about 30-35% of your hard costs." — [BP 921760](https://www.biggerpockets.com/forums/738/topics/921760-portland-4plex-townhome-build-cost-and-contractor-recommendations) (attributed to this Portland thread by the search summary; it may sit in a linked Portland thread)
- Also habit/anchor: "120 is a safe estimate" — [BP 661426](https://www.biggerpockets.com/forums/44/topics/661426-duplex-or-fourplex-building-cost-in-indianapolis); quotes "around $180-200 a square foot with rental grade finishes" — [BP 931457](https://www.biggerpockets.com/forums/44/topics/931457-how-much-would-it-cost-me-to-build-a-fourplex-in-austin-tx)

### Inferences
- **Force → prompt class → content (framework mapping applied):**

| Force | Prompt class it produces | Example prompt form | Content that answers it |
|---|---|---|---|
| Push | "Why is this happening / what now" | "GC bid 30% over my pro forma what do I do" | VE checklist + bid-check method (urgent page) |
| Pull | "What actually works for…" | "fastest way to get a construction cost estimate for a land deal" | Developer hub + sample estimate + turnaround/price |
| Anxiety | "Is X legit / X vs Y / will lender accept" | "will a lender accept a third-party construction estimate", "cost consultant vs GC precon vs AI estimating" | Decision page, lender-format sample, named estimator, method |
| Habit | "Do I really need X / can I just keep doing Y" | "is $/sq ft good enough for a pro forma" | Answer page: when $/sq ft breaks (site work, utilities, SDC, septic), estimate classes |

- Quotr today answers mostly **pull** (service posts). Anxiety and habit prompts are uncovered, and C12 shows that even pull content is credited anonymously.

### Gaps
- Reddit (r/RealEstateDevelopment, r/realestateinvesting, r/CommercialRealEstate, r/ADU), LinkedIn and podcast verbatims: not collected. reddit.com is blocked for both WebSearch filters and fetch.
- Poster names, dates and reply context for every BP quote: thread pages not opened.

---

## F. Trigger events and trigger calendar

### Takeaway
Triggers are mostly **deal-clock events**: LOI/feasibility window, lender budget request, GC bid, investor memo, overrun. Around them sit a few **datable policy landmarks**: Treasury OZ 2.0 certification now (Nov 2026), the OZ 2.0 map and California new laws on Jan 1, CA APR data on April 1, and Texas laws on Sept 1 in legislative years. Interest-rate and tariff news are cold-mode triggers.

### Cited Findings
- OZ 2.0 timeline (nominations Jul–Sep 2026 → extension to Oct 28 → Treasury certification Nov 2026 → map live Jan 1, 2027; rural 30% exclusion after five years) — [HUD OZ deck](https://invest.hawaii.gov/wp-content/uploads/2026/06/HUD_OZ-Overview.pdf); [Bernstein Shur](https://www.bernsteinshur.com/insights-events/opportunity-zones-2-0-a-new-era-for-investment-especially-in-rural-communities/); [Kiplinger nomination guide](https://www.kiplinger.com/taxes/tax-planning/how-investors-can-prep-for-new-opportunity-zones)
- Texas SB 15/SB 840 effective Sept 1, 2025, with cities updating codes into November 2025 — [Austin presentation](https://services.austintexas.gov/edims/document.cfm?id=462645); [Fort Worth](https://www.fortworthtexas.gov/files/assets/public/v/1/89th-legislative-updates-to-zoning-ordinance-and-impact-fee-program.pdf)
- CA APRs (ADU and housing permits) due to HCD by April 1 — [Placer County](https://www.placer.ca.gov/DocumentCenter/View/86623/2025-031325-PowerPoint-Presentation-Item-1A---2024-Housing-Element-and-General-Plan-Annual-Progress-Reports)
- Loan clocks: hard-money 12-month term at 90% LTC; extension fees (1% of $3M) strain margins — [BiggerPockets blog](https://www.biggerpockets.com/blog/getting-your-construction-project-over-the-finish-line); an overrun pushing a construction loan past its one-year term — [BP 1058604](https://www.biggerpockets.com/forums/51/topics/1058604-new-construction-builder-overbudget-and-might-not-close-in-time)
- Stale-estimate trigger: a GC estimate 18 months old in a market up 12% understates hard costs by 12%; one guide recommends stress-testing hard costs at +10% with a six-month schedule extension — [Innergy Integral](https://integral-c94.pages.dev/resources/construction-budget-overruns/)
- Tariff news is a live cost trigger: JEC (April 2026) put tariff costs at $7,500–$10,900 per home, and NAHB posted on tariffs in July and Sept 2026 — repo `geo-brain/03-market/white-space.md` ([JEC report](https://www.jec.senate.gov/public/_cache/files/fe5d79b2-97cb-4c55-aeba-3e31fdd235fd/april-2026-final-jec-report-on-housing.pdf); [NAHB Sept 2026](https://www.nahb.org/blog/2026/09/tariff-relief-building-materials))
- Temporal landmarks raise intent (fresh-start effect) — via framework: [Dai, Milkman & Riis](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf)

### Inferences
**Trigger calendar, Nov 2026 – Oct 2027** (V = verified date; L = likely; S = speculative)

| When | Trigger | Status | Expected prompt surge | Quotr action |
|---|---|---|---|---|
| Nov 2026 (now) | Treasury certifies OZ 2.0 tracts | V | "is my parcel in an OZ 2.0 zone", "rural OZ project cost" | Publish OZ 2.0 cost-feasibility answer page before Jan 1 |
| Nov–Dec 2026 | Year-end tax planning (gains → OZ funds; 1031 clocks) | L | "where to put capital gains real estate development 2027" | Investor-memo cost template |
| Jan 1, 2027 | OZ 2.0 map live; CA housing laws effective (Jan 1 cadence per JD Supra 2026 list); fresh-start landmark | V (OZ) / L (CA) | "what can I build under [new law] 2027" | Refresh CA regulation + cost pages; Q4 index release |
| Feb–Apr 2027 | Spring starts; construction-loan applications | L | "lender construction budget template" | Lender-format sample push |
| Apr 1, 2027 | CA APRs (ADU/permit data) due | V | none direct; new data for pages | Update ADU and SB 9 pages with APR data |
| Mid-2027 | Texas 90th Legislature (odd-year session; bills often effective Sept 1) | L | "new Texas housing law 2027 developers" | Watch list; refresh Texas page by Sept 1 |
| Rolling | LOI with 30–60-day feasibility period | L (practice, unsourced) | Hot: "cost to build [type] [city] estimate fast" | Urgent page + 72-hour offer |
| Rolling | Lender asks for line-item budget | V (forum) | "what cost breakdown do construction lenders want" | Lender-format page |
| Rolling | GC bid 20–40% over | V (forum: "over budget by 40%") | "GC bid too high how to check / value engineer" | VE page + bid-check service |
| Rolling | Fed rate moves, tariff announcements | L | Cold: "will construction costs go down 2027" | Quarterly index commentary |

### Gaps
- FOMC 2026–2027 meeting dates, current rate path and construction-loan rate data: not retrieved.
- Typical feasibility-period length for small land deals (30 vs 60 vs 90 days): no source found; it is practice knowledge.
- California 2027 effective dates for specific bills: not verified.

---

## G. Switch timeline with prompt forms

### Takeaway
Prompt specificity rises along the timeline: from vague situational ("can I build a fourplex on my lot") through category nouns ("construction cost estimate for developers", "cost consultant") to brand plus objection ("Quotr lender accepted?"). The ex-flipper's first switch is from **GC napkin numbers to any independent estimate**. Repeat buyers switch again from a per-project service to software when deal flow becomes regular.

### Cited Findings
- Moesta/Spiek timeline (first thought → passive → active → deciding → consuming) and the rule "no push, no search" — via framework: [jobstobedone.org](https://jobstobedone.org/?p=3423)
- First-thought wording in titles: "Considering building a fourplex, how much could I expect to make" — [BP 94582](https://www.biggerpockets.com/forums/12/topics/94582-considering-building-a-fourplex-how-much-could-i-expect-to-make); "Building a duplex worth it?" — [BP 557716](https://www.biggerpockets.com/forums/48/topics/557716-building-a-duplex-worth-it)
- Active-looking wording: "How to estimate cost of new construction" — [BP 902665](https://www.biggerpockets.com/forums/88/topics/902665-how-to-estimate-cost-of-new-construction); "Where can I find a new construction calculator" — [BP 705023](https://www.biggerpockets.com/forums/311/topics/705023-where-can-i-find-a-new-construction-calculator)
- Deciding-stage wording: "Validate construction $$" — [BP 1283662](https://www.biggerpockets.com/forums/44/topics/1283662-first-duplex-build-in-south-florida-fha-construction-loan-validate-construction)

### Inferences
| Stage | Typical trigger | Duration (Likely) | Prompt form (example) | Awareness level | What must be on the page |
|---|---|---|---|---|---|
| 1. First thought | Reform news; flip margins shrink; lot listing | Weeks–months | "can I build a fourplex on a 5,000 sq ft lot in Oakland" / "is building a duplex worth it vs buying" | Problem-aware | What's allowed + rough $/door + rent/sale check |
| 2. Passive looking | Deal screening sessions | Weeks | "cost to build a fourplex per sq ft 2026 California" | Problem-aware | Dated metro × product ranges |
| 3. Active looking | LOI signed; feasibility clock | 3–30 days | "how to get a construction cost estimate before buying land", "construction cost estimating service for developers" | Solution-aware | Method, sample estimate, price, turnaround |
| 4. Deciding | Lender or LP asks; GC number in hand | 1–10 days | "cost consultant vs GC preconstruction vs AI estimating service", "is Quotr legit lender" | Product-aware | Comparison table, named preparer, lender format, refund/revision terms |
| 5. Consuming | Estimate delivered; GC bids arrive | Weeks | "GC bid 30% over estimate value engineering", "how to compare GC bid to independent estimate" | Product-aware | Bid-leveling, VE options, procurement quotes |
| 6. Re-decision | Next deal (~1–3/yr for small sponsors, *estimate*) | Per deal | Terse repeat: "estimate for my new 8-unit in San Jose" (memory-equipped) | Brand-aware | Account/portal, Plus seat vs per-project math |

### Gaps
- No interview data on stage durations or on which tool (ChatGPT, Google, BP, broker) is used at each stage. The framework's "what exactly did you type" question has not yet been asked of this ICP.

---

## H. Current alternatives and unmet needs

### Takeaway
Alternatives are the GC's free precon budget (paid for by the expected job), the comps-minus-land rule, single $/sq ft anecdotes, online calculators (explicitly not lender-grade), RSMeans, cost consultants, estimating firms, Excel/ARGUS pro formas, and doing nothing. In a coded sample of 52 BiggerPockets thread titles, the most frequent unmet need is **local, current $/sq ft or per-unit numbers (44%)**, then **"does it pencil" checks (15%)**, then **protection from GC overruns or an independent check (19% combined)**. Lender format and early-drawing estimates are rarer in titles but carry the highest stakes.

### Cited Findings
- AI answers today recommend **ConstructionOnline, RSMeans, Autodesk Forma Estimate, Procore, STACK, RIB CostX, Trimble WinEst, Houzz Pro** for "software for multifamily developers to estimate construction costs" (C8). For outsourced developer estimating (C12), no brand is named but estimating firms are cited (blazeestimating, optimarprecon, quantifyna, nedesestimating, lathire, constructem, dfeestimating, estimators.us, 1800estimating), and **Quotr's post is the first citation, anonymized** — repo `quotr_ai_visibility_tests.md` (Perplexity, 2026-09-25; e.g., [ConstructionOnline multifamily](https://us.constructiononline.com/multifamily-construction-software), [RSMeans online](https://www.rsmeans.com/products/online), [Quotr outsource post](https://quotr.ai/blog/outsource-construction-estimating/))
- Multifamily cost answers cite **Meltplan and Exayard** cost pages next to RSMeans, latestcost, buildmatinsight and BDC Network — repo `competitor_geo_benchmark.md` ([Meltplan benchmarks](https://www.meltplan.com/blogs/construction-cost-per-square-foot-2026-us-benchmarks-by-building-type); [Exayard](https://exayard.com/blog/cost-to-build-apartment-complex))
- Calculators win generic "estimate before plans" retrieval (builditcalc, Mastt, calcsummit, Housecall Pro, freeconstructioncalculator, constructionspedia, smartconstructs, **estimationpro.ai**, buildrefs). One describes its output as ±20–30% (AACE Class 5) and "not for construction loans or bids" (search summary; the exact page among these was not identified) — open-web search run 2026-11-06 (see O.2, R1), e.g., [EstimationPro calculator](https://estimationpro.ai/tools/cost-to-build-a-house-calculator)
- Early estimates are 30–50% accurate and late ones 5–15% (lender blog cited by Perplexity) — repo `prompt-library.md` L-137 ([multifamily.loans](https://www.multifamily.loans/apartment-finance-blog/hard-vs-soft-construction-costs-for-multifamily-developers/))
- What $/sq ft leaves out, in buyers' words: ATU septic up to $40k ([BP 1154803](https://www.biggerpockets.com/forums/311/topics/1154803-cost-to-build-a-duplex-or-4plex-in-bradenton-fl)); $20k/unit SDC fees and soft costs at 30–35% of hard ([BP 921760](https://www.biggerpockets.com/forums/738/topics/921760-portland-4plex-townhome-build-cost-and-contractor-recommendations))
- The 52 coded threads, with URLs (titles verbatim, codes are mine):

| Code | Meaning | Threads (BP topic IDs) | Count | Share |
|---|---|---|---|---|
| LC | Local/unit cost: "what does it cost to build X (in Y)" | 456545, 456232, 1104711, 369943, 537627, 71643, 1107563, 540799, 931457, 616589, 686399, 1036890, 1239292, 1154803, 661426, 921760, 244886, 287541, 970174, 792997, 1126489, 1137494, 466365 | 23 | 44% |
| PEN | Does it pencil / build vs buy | 99571, 1104711, 930277, 265300, 94582, 557716, 861625, 1035633 | 8 | 15% |
| OVR | GC overrun, price change, GC risk | 146350, 110742, 1105632, 1058604, 852123, 907059, 285966 | 7 | 13% |
| MTH | How to estimate (method) | 519129, 456232, 1104711, 902665, 664478 | 5 | 10% |
| VAL | Validate / proofread a number | 1179899, 1283662, 792997 | 3 | 6% |
| LND | Lender or loan named in title | 1283662, 1058604, 285966 | 3 | 6% |
| GCF | Find a builder / GC fee | 921760, 571271, 186622 | 3 | 6% |
| EAR | Early-stage / pre-design / design cost | 880212, 832767 | 2 | 4% |
| LIN | Line-item breakdown | 861664 | 1 | 2% |
| TOOL | Seeking a calculator or tool | 705023 | 1 | 2% |
| REG | Regulation-driven feasibility (SB 9) | 1035633 | 1 | 2% |
| GEN | General/other | 466506, 1119674, 154511, 805149 | 4 | 8% |
| *Place named in title* | | 540799, 931457, 616589, 1154803, 661426, 921760, 571271, 1283662, 1035633, 970174, 792997, 805149, 832767, 1137494, 466365 | 15 | 29% |

  Thread URLs follow the pattern `https://www.biggerpockets.com/forums/{forum}/topics/{id}-{slug}`. All 52 appeared in the WebSearch results listed in the Research-conditions note, e.g., [456545](https://www.biggerpockets.com/forums/44/topics/456545-finding-the-cost-to-build?page=1), [519129](https://biggerpockets.com/forums/44/topics/519129-estimating-a-new-construction-project), [99571](https://biggerpockets.com/forums/44/topics/99571-new-construction-opportunity---need-advice), [456232](https://biggerpockets.com/forums/311/topics/456232-how-to-determine-the-cost-of-new-construction), [902665](https://www.biggerpockets.com/forums/88/topics/902665-how-to-estimate-cost-of-new-construction), [664478](https://biggerpockets.com/forums/44/topics/664478-how-do-i-estimate-my-construction-costs), [369943](https://www.biggerpockets.com/forums/67/topics/369943-costs-to-build-on-empty-lot), [537627](https://www.biggerpockets.com/forums/432/topics/537627-multifamily-construction-fourplex), [71643](https://www.biggerpockets.com/forums/432/topics/71643-how-much-does-a-new-4-plex-cost), [1107563](https://www.biggerpockets.com/forums/853/topics/1107563-teardowns-new-builds-rehab-costs), [540799](https://biggerpockets.com/forums/311/topics/540799-cost-to-build-4-plex-in-minnesota), [466506](https://biggerpockets.com/forums/44/topics/466506-building-a-new-fourplex), [616589](https://biggerpockets.com/forums/586/topics/616589-cost-sqft-for-a-4-plex-in-salt-lake-city), [686399](https://biggerpockets.com/forums/432/topics/686399-cost-of-building-a-fourplex), [1036890](https://biggerpockets.com/forums/311/topics/1036890-new-construction-cost-per-square-foot), [1239292](https://www.biggerpockets.com/forums/48/topics/1239292-building-cost-for-fourplex-duplex), [244886](https://www.biggerpockets.com/forums/311/topics/244886-how-much-would-it-cost-me-to-build-a-four-plex-apartment-building), [1119674](https://www.biggerpockets.com/forums/44/topics/1119674-ground-up-construction), [110742](https://www.biggerpockets.com/forums/67/topics/110742-general-contractor-losing-money-and-potentially-bailing-on-the-job), [852123](https://www.biggerpockets.com/forums/44/topics/852123-contractor-that-raise-agreed-price-after-taking-deposit), [186622](https://www.biggerpockets.com/forums/44/topics/186622-general-contractors-fees-for-building-a-new-house), [285966](https://www.biggerpockets.com/forums/51/topics/285966-203-k-loan-stuck-with-a-bad-contractor-who-wants-to-charge-more), [1035633](https://www.biggerpockets.com/forums/44/topics/1035633-sb-9-to-lot-split-or-not-la-city), [970174](https://www.biggerpockets.com/forums/48/topics/970174-ca-adu-build-progress-pics-costs-and-anything-else-you-want-to-know), [1126489](https://www.biggerpockets.com/forums/48/topics/1126489-what-are-you-building-costs-for-adus), [832767](https://www.biggerpockets.com/forums/548/topics/832767-los-angeles-adu-design-cost), [1137494](https://www.biggerpockets.com/forums/12/topics/1137494-how-much-is-a-socal-adu), [466365](https://www.biggerpockets.com/forums/311/topics/466365-cost-of-building-an-adu-in-san-jose) (others linked in sections C–E).

### Inferences
- **Coding caveat:** the sample comes from six cost-focused queries (one on overruns, one on ADU/SB 9), coded by title only. It inflates LC, OVR and California. Treat the shares as directional.
- **What does NOT satisfy them (ranked):**

| Rank | Unmet need | Evidence | Who fails it today |
|---|---|---|---|
| 1 | **Local, current, product-specific cost numbers** (metro × fourplex/ADU/townhome; $/sq ft *and* $/door; site and utility adders) | 44% LC; 29% name a place; anecdotes are 1–6 years old | Forums (stale), calculators (generic), RSMeans (needs expertise), programmatic "2026 price guides" (thin) |
| 2 | **Independence from the GC** (check a padded or stale bid; avoid anchoring the GC) | 19% OVR + VAL; "Tell your contractor your budget?" | GC precon is free but conflicted; consultants cost time |
| 3 | **Speed inside the feasibility clock** | Hot triggers; Quotr's 72h/2–4-day promise | Consultants and GC precon (turnaround not sourced) |
| 4 | **Lender/LP-acceptable format** (trade breakdown, contingency, soft costs, named preparer) | LND titles; LTC lending at 75–90% depends on the budget | Calculators ("not for loans"); $/sq ft; Excel without backup |
| 5 | **Estimates from early drawings** (massing/SD/stock plans) | EAR/MTH threads; estimate-class accuracy | GCs won't price SDs firmly; RSMeans needs quantities |
| 6 | **A pro forma that updates when costs change** | Quotr blog "the proforma that never stops changing" | Excel/ARGUS disconnected from takeoff |

- **GC precon "for free":** the trade-off (a free budget in exchange for the job, with an incentive to recover through change orders) appears in a practitioner source: a GC who wins on a thin budget "has limited margin to absorb errors and strong incentive to recover through change orders" (search-snippet text; exact page among the results for "GC bids came in way over budget pro forma" not identified, so treat as unattributed).

### Gaps
- Cost-consultant fee levels, GC paid-precon fees and RSMeans subscription prices: not retrieved.
- ARGUS and BiggerPockets calculator usage by this ICP: no data.

---

## I. Willingness to pay, price anchors, payer, sales cycle

### Takeaway
At **$0.25/sq ft, Quotr Service costs $1,000 for a 4,000 sq ft fourplex and $2,500 for a 10,000 sq ft project**, roughly 0.04–0.13% of hard costs at the $/sq ft ranges AI answers already quote. That is trivial next to the risks it addresses: one 1% loan-extension fee on $3M is $30,000. The price is not the barrier. Credibility (lender acceptance, a named preparer) and the turnaround promise are. Note a **pricing cliff**: as published, a 49,000 sq ft project costs $12,250 and a 50,000 sq ft project $5,000, unless the tiers are marginal.

### Cited Findings
- Quotr Service: **$0.25/sq ft under 50,000 sq ft; $0.10/sq ft for 50,000+ sq ft**; "Pricing is sent before we process your documents"; development cost estimates in **3–4 business days**, pro formas in **2–3** (/pricing/); conflicting "as fast as 24 hours", "72 hours" (Developer Desk), "1–3 business days" (llms.txt), "5–7 days" (schema) — repo `product-and-features.md`, `entity-fact-sheet.md` (from [quotr.ai/pricing/](https://quotr.ai/pricing/), [quotr.ai/service/](https://quotr.ai/service/), [Developer Desk post](https://quotr.ai/blog/quotr-developer-desk-underwriting-grade-estimates-72-hours/))
- Quotr Software: Lite **$79.90**/seat/mo; Plus **$299.90**/seat/mo (adds 2,000 sq ft of takeoff credits per month and 10% off procurement; what the credits cover is TO CONFIRM); Enterprise custom — repo `product-and-features.md` ([quotr.ai/pricing/](https://quotr.ai/pricing/))
- Quotr's own outsourcing benchmark, cited by Perplexity: "$0.03–$0.10/sq ft and $250–$2,500 per estimate" for outsourced quantity takeoffs — repo `ai-visibility-baseline.md` S9 ([quantity-takeoff-services](https://quotr.ai/blog/quantity-takeoff-services/))
- AI answers quote **$220–$700/sq ft and $150k–$250k per unit** for multifamily (P3) — repo `white-space.md` (Perplexity, 2026-09-25)
- Lender economics: hard money at 90% LTC with an updated budget; a 1% extension fee on $3M — [BiggerPockets blog](https://www.biggerpockets.com/blog/getting-your-construction-project-over-the-finish-line)
- Forum price anchors buyers already hold: $165/sq ft (Bradenton), $180–200 (Austin), $120–140 (Indianapolis), $205–300 (South Florida) — threads in section B

### Inferences
- **Fee anchors (arithmetic on published rates; GFA assumptions are illustrative):**

| Project (assumed GFA) | Quotr Service fee | Hard cost at $220/sf (low end of AI range) | Fee as % of hard cost |
|---|---|---|---|
| Single ADU (800 sf) | $200 | $176k | 0.11% |
| SB 9 split, 2 homes (2,400 sf) | $600 | $528k | 0.11% |
| Fourplex (4,000 sf) | $1,000 | $880k | 0.11% |
| 10–12 units (10,000 sf) | $2,500 | $2.2M | 0.11% |
| 40 units (40,000 sf) | $10,000 | $8.8M | 0.11% |
| 49,000 sf | $12,250 | $10.8M | 0.11% |
| 50,000 sf | **$5,000** (if a flat tier) | $11.0M | 0.05% |
| 150 units (120,000 sf) | $12,000 | $26.4M | 0.05% |

- **Who pays:** the sponsor, from pre-development cash (Likely). On funded deals the cost is often recoverable as a soft cost (Likely, unsourced). LPs and lenders demand the estimate but rarely pay for it.
- **Sales cycle:** hot-mode purchase decided in **1–10 days** inside a feasibility or lender window (Likely). Conversion hinges on (1) a visible sample, (2) a turnaround stated once and consistently, (3) a named estimator or PE, and (4) price before upload, which Quotr already offers.
- **Plan fit:** a 1–3 deal/year sponsor should buy per-project Service. Software Plus ($3,599/yr per seat) makes sense only for repeat ADU, BTR or lot-split builders running several estimates a month (Likely).
- **WTP ceiling (Speculative):** a sponsor who would pay a GC nothing and a consultant several thousand dollars will likely accept $1k–$10k if the output is lender-ready. Validate with five recent buyers.

### Gaps
- Cost-consultant and paid-precon fee benchmarks; any lender statement on accepting third-party or AI-assisted estimates; whether Quotr's 50k tier is marginal or flat (TO CONFIRM with Quotr); rush pricing.

---

## J. Vocabulary list

### Takeaway
Content and prompts must carry the buyer's terms, especially **$/door, $/sq ft, hard vs soft, LTC, yield on cost, contingency, VE, SD/DD/CD, and the law names** (SB 9, SB 840, HB 1110, Live Local, OZ 2.0), because engines inject these into fan-outs.

### Cited Findings
- Terms seen in buyer text: "cost/sq ft", "investor grade finishes", "conditioned space", "unconditioned storage", "SDC fees", "soft cost ratio", "ATU septic", "comps", "land value" — BP threads [1154803](https://www.biggerpockets.com/forums/311/topics/1154803-cost-to-build-a-duplex-or-4plex-in-bradenton-fl), [921760](https://www.biggerpockets.com/forums/738/topics/921760-portland-4plex-townhome-build-cost-and-contractor-recommendations); "rental grade finishes" — [931457](https://www.biggerpockets.com/forums/44/topics/931457-how-much-would-it-cost-me-to-build-a-fourplex-in-austin-tx); "FHA construction loan" — [1283662](https://www.biggerpockets.com/forums/44/topics/1283662-first-duplex-build-in-south-florida-fha-construction-loan-validate-construction); "LTC", "loan to cost" — [BP blog](https://www.biggerpockets.com/blog/getting-your-construction-project-over-the-finish-line)
- "Hard costs vs soft costs" answers cite adventuresincre and dealworthit glossaries — repo `prompt-library.md` L-135 ([A.CRE hard costs](https://www.adventuresincre.com/glossary/hard-costs/))
- Law names: SB 840, SB 15 ([Foley](https://www.foley.com/insights/publications/2025/07/texas-enacts-critical-real-estate-reforms-senate-bills-15-17-840/)); SB 9 ([BP 1035633](https://www.biggerpockets.com/forums/44/topics/1035633-sb-9-to-lot-split-or-not-la-city)); OZ 2.0, QROF ([CLA](https://www.claconnect.com/en/resources/blogs/real-estate/rural-america-prepare-for-changes-to-the-opportunity-zone-program))

### Inferences
- **Money:** pro forma · development budget · total development cost (TDC) · hard costs · soft costs · land/acquisition · site work (horizontal) vs vertical · contingency (hard, soft, owner) · escalation · general conditions · OH&P / GC fee · GMP · cost-plus · stipulated sum · draw schedule · interest reserve · LTC · LTV · DSCR · debt yield · yield on cost / untrended YOC · development spread · cap rate · NOI · IRR · equity multiple · exit value · per-door / per-unit / per-key · $/sq ft (gross vs net rentable) · efficiency ratio · impact fees / SDCs / utility taps
- **Stage and estimate:** napkin / back-of-envelope · ROM · conceptual estimate · AACE Class 5→1 · massing study · schematic design (SD) · design development (DD) · construction documents (CD) · permit set · takeoff · bid leveling · scope gap · alternates · value engineering (VE) · precon · GC budget · third-party cost review
- **Product:** ADU / JADU · SB 9 lot split / urban lot split · small-lot subdivision (SB 684/SB 1123, verify) · missing middle · duplex/triplex/fourplex · townhome · cottage court · walk-up · garden-style · 5-over-1 / podium · BTR / SFR · mixed-use · commercial-to-residential conversion (TX SB 840) · fire rebuild
- **Entitlement and tax:** by-right / ministerial · discretionary · density bonus · HOME (Austin) · middle housing (WA HB 1110 / OR HB 2001) · Live Local Act · OZ 2.0 · QOF / QROF · 1031
- **Materials (Procurement bridge):** finish package · long-lead items · DDP · tariffs · landed cost · FF&E

### Gaps
- No frequency data on which terms this ICP uses most in AI prompts (needs GSC/WildChat filtering).

---

## K. Channels

### Takeaway
Confirmed: **BiggerPockets forums** dominate open-web retrieval for small-developer cost questions (14 of 19 results for a fourplex-cost query; 18 of 20 for an estimating query). r/RealEstateDevelopment topics feed Perplexity answers that cite lender blogs (multifamily.loans, propertybuild, mmcginvest, Innergy Integral). Practitioner blogs (Brandon Donnelly, Built) and policy groups (Terner, CA YIMBY, Casita Coalition, ABAG) surface for cost-and-policy queries. Member counts could not be collected.

### Cited Findings
- BP forum sub-forums seen: 44 (new construction), 311 (cost questions), 432 (multifamily), 548 (ADU), 48, 67, 12, 51, 52, 61, 88, 586, 738, 853 (forum IDs in URLs) — threads in section H
- r/RealEstateDevelopment topic searches led Perplexity answers to cite [multifamily.loans](https://www.multifamily.loans/apartment-finance-blog/hard-vs-soft-construction-costs-for-multifamily-developers/), [innergyintegral.com](https://innergyintegral.com/resources/multifamily-proforma-construction-costs/), [propertybuild.com](https://propertybuild.com/multifamily-construction/), [mmcginvest.com](https://www.mmcginvest.com/multifamily-feasibility-study) — repo `buyer-questions-by-trade.md`
- Practitioner/finance blogs in retrieval: [Brandon Donnelly, "Demystifying the development pro forma"](https://brandondonnelly.com/demystifying-the-development-pro-forma), [Built, development pro forma](https://getbuilt.com/blog/development-pro-forma/) — open-web search R2, 2026-11-06
- Policy and data sources in retrieval: [Terner Center](https://ternercenter.berkeley.edu/wp-content/uploads/2020/08/Hard_Construction_Costs_March_2020.pdf), [CA YIMBY cost analysis](https://cayimby.org/how-to-beat-the-high-cost-of-construction/), [SPUR LIHTC costs](https://www.spur.org/sites/default/files/2020-06/lihtc_construction_costs_2020.pdf), [Casita Coalition](https://casitacoalition.squarespace.com/casita-coalition-blog/california-reaches-major-housing-milestonemore-than-100000-adus-permitted-since-2017), [ABAG](https://abag.ca.gov/technical-assistance/annual-progress-reports-update-hcd) — open-web searches R5, R7
- Quotr attended or recapped **RE:Forge SF 2026** and **PCBC 2026**. The citation map lists BIA Bay Area, NAHB and NMHC as partnership targets — repo `audiences-and-personas.md`, `citation-sources-map.md`

### Inferences
| Channel | Role for ICP 6 | Engine pull (Likely) | Priority |
|---|---|---|---|
| BiggerPockets forums (44, 311, 432, 548) | Where ex-flippers ask cost questions; threads rank in open-web retrieval | Google AIO/AI Mode, Perplexity | **1** |
| r/RealEstateDevelopment, r/realestateinvesting, r/ADU | Peer validation; Perplexity/Google cite Reddit | Perplexity, Google | 2 |
| Construction-lender and broker blogs (multifamily.loans, propertybuild, Built) | Already cited for method questions | ChatGPT, Perplexity | 2 |
| CA policy/data orgs (Terner, CA YIMBY, Casita Coalition, ABAG) | Authority for CA cost and ADU data; pitch the index | ChatGPT, Claude | 3 |
| BIA Bay Area, local developer meetups, RE:Forge, PCBC | Trust, case studies, speaking | Indirect (press mentions) | 3 |
| YouTube (feasibility walk-throughs) | Google surfaces cite YouTube heavily (via framework) | Google AIO/AI Mode | 3 |
| LinkedIn (founder posts, Pulse) | B2B credibility; Handoff's listicle syndicated there | ChatGPT (Bing) | 4 |
| ULI / NAIOP / NMHC | Skew larger sponsors | Low for this ICP | 5 |

### Gaps
- Member counts: BiggerPockets, r/RealEstateDevelopment, r/realestateinvesting, r/CommercialRealEstate, r/ADU, ULI, NAIOP; podcast and YouTube channel names and audience sizes — **not collected** (blocked or out of budget). The brief's request for member counts is unmet.

---

## L. Proof required at each stage

### Takeaway
Each stage needs a different, verifiable artifact. The engine will cite Quotr only if those artifacts exist as **retrievable pages with numbers and Quotr's name in the sentence**, because Perplexity anonymized Quotr's prices in C12.

### Cited Findings
- When a Quotr page is the only source for a fact, Perplexity anonymized the brand ("one outsourced estimating service"), so **brand-attributed statements and third-party corroboration** are needed — repo `quotr_ai_visibility_tests.md` C12
- Quotr's sample deliverables library has 9 documents; **6 of 8 visible samples are commercial**; one is "Fast Cost Estimation (Residential LA Fire Rebuilding)" — repo `product-and-features.md` ([quotr.ai/service/](https://quotr.ai/service/))
- Objections already logged for this persona: "Will the estimate be accurate enough for underwriting?", "Who stands behind the numbers?", "I have never heard of Quotr" (no press, about 0 G2 reviews) — repo `audiences-and-personas.md`, `competitor-landscape.md`
- Over $500, trust in AI recommendations alone is 5%, so buyers verify — via framework: [MarTech](https://martech.org/the-ai-shopping-stats-2026-what-you-need-to-know/)

### Inferences
| Stage | Proof required | Quotr has it? | Gap to close |
|---|---|---|---|
| First thought / passive | Dated $/sq ft and $/door ranges by metro × product, with source and date | No (no cost pages) | Metro cost pages + quarterly index |
| Active | **Sample estimate** for a fourplex/ADU/SB 9 (line items by CSI division or trade, site/utility adders, contingency, soft costs); method page (estimate classes, inputs needed) | Partial (commercial-heavy samples) | 3 residential developer samples (fourplex, SB 9 split, 24-unit walk-up) |
| Deciding | Price before upload (✓), **one** consistent turnaround, named estimator/PE, revision policy, lender-format statement, a named developer customer with numbers | Price yes; others no or conflicting | Fix turnaround conflict; BiltWise case with numbers; "lender-ready format" page; ask 1–2 lenders for an acceptance quote (TO CONFIRM) |
| Consuming | Editable live project, bid-leveling against GC bid, VE options in $, procurement quote for finishes | Yes per Quotr copy (live editable project; TO CONFIRM for all Service jobs); Procurement cards | Publish a VE case: "GC +30% → closed gap by $X" |
| Re-decision | Portfolio view, $/door history across deals | Unknown | Quarterly index doubles as retention content |

### Gaps
- No evidence on whether any lender has accepted a Quotr estimate. This is the single most valuable fact to confirm.

---

## M. Coding chains (trigger → stage → mode → restraining force → prompt → proof)

### Takeaway
Eight chains cover the ICP. Four are hot and decide revenue (C1–C4). Four are cold and shape the anchor (C5–C8).

### Cited Findings
- Chain format and the promotion threshold (≥3 of 12 interviews or ≥5 of 50 posts) — via framework (uploaded file; threshold labeled there as a synthesis). The coded BP sample (n = 52) clears the ≥5 threshold for LC (23), PEN (8) and OVR (7); VAL, LND and EAR fall below it — section H.

### Inferences
| # | Trigger (datable push) | Stage | Mode | Dominant restraining force | Exact prompt (full-context form) | Proof required | Promotion status |
|---|---|---|---|---|---|---|---|
| C1 | Lot under LOI, 30-day feasibility | Active | Hot | Anxiety: "is the GC's napkin number real?" | "I have a 5,000 sq ft lot in Oakland under LOI with 3 weeks of feasibility left. What does a fourplex cost to build per sq ft and per door in 2026, and how do I get a credible estimate before I close?" | Dated Bay Area fourplex range; sample estimate; turnaround; price | Promote (LC 23/52) |
| C2 | Lender asks for line-item budget | Deciding | Hot | Anxiety: "will a lender accept a non-GC estimate?" | "My construction lender wants a cost breakdown by trade for my 6-unit townhome project in Sacramento before the term sheet. My architect is only at schematic design. What format do lenders accept and who can prepare it independently?" | Lender-format sample; named preparer; contingency and soft-cost lines | Below threshold in titles (LND 3/52); promote on stakes |
| C3 | GC bid 30% over pro forma | Consuming / re-decision | Hot | Habit: renegotiate with the same GC | "Our GC's bid for a 12-unit walk-up in San Jose came in 30% over my hard-cost budget and my equity partner's IC meets in 10 days. How do I check if the bid is padded and where can I value-engineer?" | Line-item bid comparison; VE options with $; finish-package procurement quote | Promote (OVR 7/52) |
| C4 | Investor memo / LP deck due | Deciding | Hot→warm | Anxiety: credibility to LPs | "We're a 3-person team underwriting a 40-home build-to-rent community outside San Antonio. Our investor memo is due in 3 weeks. Should we hire a cost consultant or use an estimating service for hard costs per door?" | Comparison table; method; sensitivity (+10% hard, +6 months) | Speculative (no BTR evidence collected) |
| C5 | State reform effective (SB 9/SB 840/HB 1110) | First thought | Cold | Habit: keep flipping | "Texas SB 840 lets me build apartments on commercially zoned land in Austin. Does a 24-unit 3-story walk-up pencil, and what would hard costs be?" | Worked example: cost + rent + yield on cost | Promote for CA (REG/PEN) |
| C6 | Deal-screening session | Passive | Cold | Habit: $/sq ft rule of thumb | "new construction cost per square foot for a fourplex in California 2026 investor grade finishes" | Dated index by metro × product; adders list | Promote (LC) |
| C7 | Tariff or rate news | Passive | Cold | Anxiety: escalation | "How are 2026 tariffs changing what it costs small developers to build a fourplex, and can I lock finish costs?" | Landed-cost data; procurement savings cards | Supported by repo tariff white space |
| C8 | Fire loss / rebuild with insurer or lender clock | Active | Hot | Anxiety: insurer/lender scrutiny | "We're rebuilding a 2,200 sq ft house plus a detached ADU on a burned lot in Altadena. The lender wants a line-item budget in two weeks. What does a rebuild cost per sq ft in 2026 and who can produce the budget fast?" | LA rebuild sample deliverable; local unit costs | Supported (S12 absent; Quotr sample exists) |

### Gaps
- No chain has been validated with switch interviews; mode and force tags are inferred from titles.

---

## N. Prompt matrix

### Takeaway
Twelve persona-loaded prompts, six short category prompts and three brand prompts, tagged for intent, stage, urgency, mode, engine, expected fan-out nodes and an **estimated** demand tier. Track ChatGPT and Google AI Mode/AIO; add Perplexity because it already cites Quotr's service posts.

### Cited Findings
- ChatGPT averages ~2.1 fan-out sub-queries and injects "best" (15.3%), "reviews" (6.8%) and "2026" (5.4%). GPT-5.6 fan-outs carry "2026" 22.9% and "price" 8.9% of the time. Persona facts change which brands are named. Memory injects city and context into searches — via framework: [PPC Land/Peec](https://ppc.land/what-chatgpt-actually-searches-for-5-million-fanout-queries-analyzed/); [Ahrefs](https://ahrefs.com/blog/query-fan-out-chatgpt/); [Profound](https://www.tryprofound.com/blog/do-answer-engines-customize-responses-to-different-personas); [TechCrunch](https://techcrunch.com/2025/04/18/chatgpt-will-now-use-its-memory-to-personalize-web-searches)
- "Ask for a pick" prompts produce a 22.8% brand-recommendation rate vs 8.0% for topic-only prompts; comparative prompts reach 43.3% vs 18% mention rates — via framework: [Momentic](https://momenticmarketing.com/blog/prompt-set-worth-tracking); [Semrush](https://semrush.com/blog/the-ghost-citations-study/)
- Pew: ChatGPT reaches 44% of US adults, Gemini 24% — via framework: [Pew](https://www.pewresearch.org/internet/2026/06/17/americans-and-ai-2026-chatbots-smart-devices-and-views-on-impact/markdown)

### Inferences
**Demand tier (1–5) is an ESTIMATE** from coded-thread density (section H), the existence of programmatic "2026 price guide" pages for the head term (a sign of search demand), and repo priority. No GSC or panel volumes were pulled.

**N.1 Full-context first-person prompts**

| ID | Prompt | Intent | Stage | Urgency | Mode | Engine | Expected fan-out nodes | Tier (est.) |
|---|---|---|---|---|---|---|---|---|
| F1 | "I flipped six houses in the East Bay and now have a 5,000 sq ft lot in Oakland under LOI with 3 weeks of feasibility left. What will a ~4,000 sq ft fourplex cost to build in 2026 per sq ft and per door, and how do I get a credible estimate before I close?" | Learn → choose provider | Active | Acute | Hot | ChatGPT, AI Mode | cost to build fourplex Oakland 2026 · Bay Area construction cost per square foot 2026 · fourplex cost per unit California · construction cost estimate before buying land · best estimating service developers | 3 |
| F2 | "My partner and I bought a burned lot in Altadena and are rebuilding a 2,200 sq ft house plus a detached ADU to rent. The lender wants a line-item construction budget in two weeks. What does a fire rebuild cost per sq ft in 2026 and who can produce a lender-ready budget fast?" | Choose provider | Active | Acute | Hot | ChatGPT, AIO | LA fire rebuild cost per square foot 2026 · Altadena rebuild contractors · construction budget for lender · ADU cost Los Angeles 2026 | 3 |
| F3 | "Our GC's bid for a 12-unit walk-up in San Jose came in 30% over the hard-cost budget in my pro forma, and my equity partner's IC meets in 10 days. How do I tell if the bid is padded and what can I value-engineer without hurting rents?" | Diagnose → do | Consuming | Acute | Hot | ChatGPT | GC bid over budget what to do · value engineering multifamily · independent construction cost review · bid leveling · San Jose construction costs 2026 | 3 |
| F4 | "My construction lender, a community bank, wants a detailed cost breakdown by trade for my 6-unit townhome project in Sacramento before issuing a term sheet. My architect is only at schematic design. What format do lenders accept and can I get one prepared independently of my GC?" | Validate/trust | Deciding | Acute | Hot | ChatGPT | construction loan budget template · lender requirements construction cost breakdown · third-party cost review lender · schematic design estimate accuracy | 3 |
| F5 | "I own a single-family lot in San Jose and want to use SB 9 to split it and build two 1,200 sq ft homes to sell. What will site work, utilities and vertical construction cost in 2026, and what's the cheapest way to get a reliable estimate from schematic drawings?" | Learn → choose | Active | Exploratory→acute | Cold→hot | ChatGPT, AIO | SB 9 lot split cost · cost to build house San Jose 2026 per sq ft · utility connection fees San Jose · construction estimate from schematic plans | 3 |
| F6 | "I'm a small developer in Austin negotiating a 0.6-acre commercially zoned lot. Under Texas SB 840 I could build a 24-unit, 3-story walk-up by right. Before I go hard, how do I estimate hard costs, and is the GC's free preconstruction budget good enough for a construction lender?" | Learn → compare | Active | Acute | Hot | ChatGPT | SB 840 multifamily commercial zoning · cost to build apartments Austin 2026 per unit · GC preconstruction budget vs independent estimate · construction lender requirements Texas | 2 |
| F7 | "We're a 3-person team planning a 40-home build-to-rent community outside San Antonio. Our investor memo is due in 3 weeks and needs hard cost per home plus horizontal costs. What does BTR cost per door in 2026, and should we hire a cost consultant or an estimating service?" | Compare → choose | Deciding | Acute | Hot | ChatGPT | build to rent construction cost per door 2026 · BTR horizontal costs per lot · cost consultant fees · construction estimating service for developers best | 2 |
| F8 | "I'm in Seattle looking at a lot where HB 1110 now allows four units. I only have a massing study from my architect. Can I get a construction cost estimate from just a massing study, and how accurate would it be?" | Learn/trust | Active | Exploratory | Cold | ChatGPT, Perplexity | HB 1110 fourplex cost Seattle · conceptual estimate accuracy AACE class 5 · cost per sq ft townhouse Seattle 2026 | 2 |
| F9 | "I'm evaluating a 60-unit Live Local Act project on a commercial parcel in Tampa and need hard costs to underwrite before my LOI expires in 30 days. What's a realistic cost per unit in 2026 and who can estimate it quickly?" | Learn → choose | Active | Acute | Hot | ChatGPT | Live Local Act construction cost per unit · Tampa apartment construction cost 2026 · fast construction cost estimate developer | 2 |
| F10 | "I have about $1.5M of 2026 capital gains and want to put it into an Opportunity Zone 2.0 project from 2027: 12 rental cottages in a rural tract in California's Central Valley. How do I estimate construction costs to see if the 30% rural exclusion makes it pencil?" | Learn | Passive | Exploratory | Cold | ChatGPT | opportunity zone 2.0 rural 30% exclusion · QROF · cost to build small home Central Valley 2026 · cottage court construction cost | 1 |
| F11 | "I build backyard ADUs on investor-owned lots in Los Angeles, about 10 a year at 600–800 sq ft. I want a repeatable cost model per ADU and lower finish costs (cabinets, windows, flooring). What's a realistic 2026 cost per sq ft and is buying finishes factory-direct from China worth it?" | Learn → choose | Passive→active | Recurring | Cold | ChatGPT, AIO | ADU cost per square foot Los Angeles 2026 · ADU finish package cost · buy cabinets windows factory direct China contractor · tariffs cabinets 2026 | 2 |
| F12 | "I'm under contract on a 9,000 sq ft single-story retail building in Fresno that I want to convert to medical office, with 45 days of due diligence. What does a conversion or TI cost per sq ft in 2026, and who can estimate it from as-built PDFs fast?" | Choose provider | Active | Acute | Hot | ChatGPT | retail to medical office conversion cost per sq ft 2026 · tenant improvement cost Fresno · estimate from PDF plans service | 1 |

**N.2 Short category prompts** (existing library IDs noted where they overlap)

| ID | Prompt | Intent | Stage | Mode | Fan-out nodes | Tier (est.) |
|---|---|---|---|---|---|---|
| S1 | cost to build a fourplex in Oakland 2026 | Learn (local cost) | Passive | Cold | per sq ft · per unit · Bay Area · 2026 | 3 |
| S2 | construction cost estimate for real estate developers | Choose provider | Active | Hot | best · services · price · reviews (≈ E-005/E-073) | 3 |
| S3 | independent construction cost estimate before buying land | Choose provider | Active | Hot | feasibility · third-party · cost consultant (≈ L-136) | 2 |
| S4 | cost consultant vs GC preconstruction vs estimating service | Compare | Deciding | Cold/hot | fees · pros cons · best | 2 |
| S5 | cost per door to build multifamily California 2026 | Learn | Passive | Cold | per unit · garden · podium · RSMeans (≈ L-131) | 3 |
| S6 | GC bid came in over budget what to do | Diagnose/do | Consuming | Hot | value engineering · bid leveling · contingency (≈ L-140) | 3 |

**N.3 Brand prompts** (track separately; brand prompts mention the brand ~92% of the time, via framework [Momentic](https://momenticmarketing.com/blog/prompt-set-worth-tracking))

| ID | Prompt | Intent | Fan-out nodes |
|---|---|---|---|
| B1 | "Is Quotr.ai legit for developer construction cost estimates, and will lenders accept them?" | Validate | Quotr reviews · Quotr Service · site:quotr.ai · lender |
| B2 | "Quotr Service vs RSMeans vs hiring a cost consultant for a small multifamily deal" | Compare | Quotr pricing · RSMeans cost · cost consultant fees |
| B3 | "How much does Quotr charge for a cost estimate or pro forma and how fast is it?" | Price | Quotr pricing per square foot · turnaround (conflict today) |

### Gaps
- Demand tiers lack GSC, Keyword Planner and Profound inputs. Prompts are not yet baselined (3–5 runs × 2 engines).

---

## O. Simulation

### Takeaway
(1) A **simulated** five-turn ChatGPT journey shows Quotr entering only if the buyer names it, because today's retrieval pool for this persona is forums, calculators, lender blogs, research PDFs and incumbents. (2) Nine open-web searches made during this research, used as **retrieval proxies (not AI engine answers)**, returned Quotr in **0 of 9**. Real Perplexity runs from the September audit show Quotr absent in five developer prompts and cited-not-named in one. (3) The most winnable clusters are local cost (metro × product) and outsourced developer estimating, where the content pool is thin or Quotr is already retrieved.

### Cited Findings
**O.2 Retrieval proxy table — open-web WebSearch results, 2026-11-06 (retrieval proxy, not an AI engine answer).** These were research queries, not the planned fan-out set; bias notes in the last column.

| # | Query run | Top domains | Brands named | Quotr? | Winning format | Bias note |
|---|---|---|---|---|---|---|
| R1 | r/RealEstateDevelopment how do you estimate construction costs before plans "per square foot" GC | builditcalc, mastt, calcsummit, housecallpro, freeconstructioncalculator, constructionspedia, smartconstructs, estimationpro.ai, buildrefs | Mastt, Housecall Pro, EstimationPro | No | **Calculators (9/9)** | Clean proxy for "estimate before plans" |
| R2 | reddit RealEstateDevelopment GC bids came in way over budget pro forma hard costs | integral-c94.pages.dev (Innergy Integral) ×2, getbuilt.com, brandondonnelly.com ×4, spacing.ca, sfport.com, county/state housing templates (Prince George's, Florida Housing, mass.gov, SC Housing/Cumming report), brickunderground | Built, Cumming (report) | No | **Practitioner explainers + agency budget templates** | Clean proxy for overrun/VE |
| R3 | biggerpockets fourplex new construction cost per square foot builder quote too high | biggerpockets (14/19), angi.com, risingsunartscentre.org ×3 and selector.kurlon.com (programmatic "2026 price guide" pages) | Angi | No | **Forum threads**; thin programmatic pages also rank | Query names BP (biased) |
| R4 | biggerpockets forum how to estimate construction costs new construction before buying land developer | biggerpockets (18/20), mpamag.com | — | No | Forum threads + trade article | Query names BP (biased) |
| R5 | Terner Center hard construction costs per square foot California multifamily 2025 | ternercenter (4 PDFs), cayimby ×3, nlihc, spur, siliconvalleyathome, San Leandro/Pleasanton docs, irecruit.co, planetizen, calmatters | — | No | **Research PDFs + advocacy explainers** | Query names Terner (biased) |
| R6 | reddit contractor bids came in over budget duplex/fourplex/ADU new construction investor | housing.hpd.nyc.gov (ADU budget), hcd.ca.gov ADU finance guide, techcrunch (Cottage), teamblind, yahoo news, barchart PR, homeadvisor | Cottage, HomeAdvisor | No | **Public-agency budget guides + news** | Clean |
| R7 | California ADU permits 2025 HCD annual progress report number | city APR PDFs (Jurupa Valley, Lathrop, Placerville, Placer County, Santa Ana, Del Rey Oaks), ABAG, Casita Coalition, JD Supra, bill analysis | — | No | **Government documents** | Data lookup |
| R8 | Texas SB 840 SB 15 2025 small lots multifamily commercial zones effective date | Fort Worth ×2, Austin, Greater Palestine, capitol.texas.gov, Foley, Mondaq, Texas Law Book, Nat Law Review, Hunton, Bisnow, Northmarq, Community Impact | Northmarq | No | **Law-firm alerts + city notices** | Regulation lookup |
| R9 | opportunity zones 2.0 One Big Beautiful Bill new designations January 1 2027 rural | Withum, EIG, Kiplinger ×2, Bernstein Shur, HUD deck, IEDC, CaliberCos, CLA, Pillsbury, HCVT, Warren Averett, ICSC | Caliber | No | **Accounting/law explainers** | Regulation lookup |

- Source for all rows: WebSearch result lists in this session (URLs cited in sections A–K, e.g., [estimationpro.ai](https://estimationpro.ai/tools/cost-to-build-a-house-calculator), [Innergy Integral](https://integral-c94.pages.dev/resources/construction-budget-overruns/), [Built](https://getbuilt.com/blog/development-pro-forma/), [Angi fourplex cost](https://www.angi.com/articles/build-fourplex-cost.htm), [programmatic page example](https://new.risingsunartscentre.org/news/4-plex-construction-cost-price-guide-2026.html), [NYC HPD ADU budget](https://housing.hpd.nyc.gov/adu/budget), [CA HCD ADU finance guide](https://www.hcd.ca.gov/policy-research/accessorydwellingunits/docs/cc%20adu%20finance%20guide%20for%20homeowners%20v5%203.18.21_ada.pdf))
- **Real AI-engine results from the repo (Perplexity Sonar, 2026-09-25):** C8 developer software → Absent (ConstructionOnline, RSMeans, Autodesk Forma Estimate, Procore, STACK…); C12 outsourced estimating for developers → **Cited, not named** (first citation, rates repeated anonymously); P3 how to estimate multifamily → Absent (RSMeans, Brookings, RAND, lenders; $220–$700/sf); S10 multifamily $/sf 2026 → Absent (Meltplan, Exayard, RSMeans); S12 LA fire rebuild $/sf → Absent (Bloomberg + local GCs); L-136 estimate before buying land → seen citing multifamily.loans — repo `quotr_ai_visibility_tests.md`, `tracking-set.md`, `prompt-library.md`

### Inferences
**O.1 SIMULATED ChatGPT conversation — illustrative only; NOT a real engine run.** The persona is fictional. Expected fan-outs and citations are predictions from O.2 and the repo baseline.

> **Turn 1 — first thought, Sunday evening, cold.** *User:* "I've done six flips in the East Bay. A 5,000 sq ft lot in Oakland just came up and I think it allows four units. Rough cost to build a fourplex?"
> *Expected fan-outs:* "cost to build fourplex Oakland 2026", "Bay Area construction cost per square foot 2026".
> *Simulated answer:* a wide $/sq ft range with a Bay Area premium (likely from Terner's +$81/sf and generic guides such as Angi or programmatic pages), a reminder that land, soft costs and site work are extra, and advice to "get a local GC quote". **No vendor named.**

> **Turn 2 — active, hot (LOI signed, 3 weeks left).** *User:* "I signed an LOI with 21 days of feasibility. My GC buddy says $350 a foot, napkin. My lender wants a line-item budget. How do I get something credible without full drawings?"
> *Expected fan-outs:* "construction cost estimate before buying land", "estimate from schematic design accuracy", "construction lender budget requirements".
> *Simulated answer:* explains estimate classes (calculators ±20–30%, not lender-grade), suggests a cost consultant or GC precon, and cites lender blogs (multifamily.loans, propertybuild). **Quotr absent** (no method page or sample exists).

> **Turn 3 — deciding, compare.** *User:* "Cost consultant vs paying a GC for precon vs one of these AI estimating services. Which for a ~$2M fourplex?"
> *Expected fan-outs:* "cost consultant fees construction", "best construction estimating service for developers 2026", "AI construction estimating developers".
> *Simulated answer:* pros and cons table. It names RSMeans, possibly Autodesk/ConstructionOnline (C8 pattern) and estimating firms (C12 pattern). It may repeat "$0.25/sq ft" as "one service charges…", **without naming Quotr** (observed C12 behavior).

> **Turn 4 — brand check (only if the user saw Quotr elsewhere, e.g., in a BP reply).** *User:* "Is Quotr.ai legit? Would my lender accept their estimate?"
> *Expected fan-outs:* "Quotr.ai reviews", "site:quotr.ai developer", "Quotr Service pricing".
> *Simulated answer:* describes Quotr accurately (B1 was accurate in the audit), notes no third-party reviews, and **cannot answer the lender question** because no page addresses it. It quotes one of several conflicting turnarounds.

> **Turn 5 — consuming.** *User:* "Quotr's estimate was $X; the GC's bid came in 30% higher. How do I value-engineer?"
> *Simulated answer:* a generic VE list. A Quotr VE case page, bid-leveling sample or procurement savings card would be the only way Quotr re-enters here.

**Desired future state (target):** Turn 1 cites Quotr's Bay Area index ("Quotr.ai's Q4 2026 Bay Area index puts fourplex hard costs at …"). Turn 2 cites Quotr's "estimate before you close" method page and sample. Turn 3 names Quotr in a fair comparison, from Quotr's decision page **and** a third-party list or BP thread. Turn 4 answers lender acceptance from a dated Quotr page plus a named lender quote.

**O.3 Gap verdict per prompt cluster**

| Cluster | Who owns it now | Content-pool quality | Quotr status | Verdict |
|---|---|---|---|---|
| Local cost: metro × product (S1, S5, F1, F5, F11) | BP threads (stale), calculators, Angi, thin programmatic 2026 pages, Meltplan/Exayard for multifamily | **Thin/stale** | Absent | **Win: build first** (data pages + index) |
| Outsourced developer estimating (S2, S3, F4, F9, F12) | Estimating firms; Quotr retrieved but anonymized | Medium | Cited, not named | **Win fast:** brand-attributed rewrites + developer hub |
| Compare/decide (S4, F6, F7) | Generic advice; no decision page found | Thin | Absent | **Win:** fair decision page |
| Overrun/VE (S6, F3) | Practitioner blogs (Innergy Integral, Brandon Donnelly, Built), agency templates | Medium | Absent | Win with a VE case + bid-check page |
| Lender format (F2, F4) | Lender blogs, agency templates | Medium | Absent | Win if a lender-acceptance proof exists |
| Developer software (C8) | Autodesk, RSMeans, ConstructionOnline, Procore | Strong incumbents | Absent | **Deprioritize:** reframe as service, not software |
| Regulation feasibility (F6, F8, F10) | Law firms, cities, accounting firms | Strong | Absent | Don't compete on law; own "cost to build under SB 9/SB 840/OZ 2.0" |
| Macro cost research (Terner/RAND) | Research institutions | Strong | Absent | Long play: original index pitched to these orgs |

### Gaps
- **The planned fan-out runs were NOT executed** because the shared search budget was exhausted. Run next, 3× each on ChatGPT and Google AI Mode: "cost to build a fourplex in Oakland 2026", "construction cost estimate for real estate developers", "cost consultant vs GC preconstruction", "ADU cost per square foot Los Angeles 2026", "LA fire rebuild cost per square foot 2026", "SB 9 lot split construction cost San Jose", "build to rent construction cost per door 2026", "construction loan budget template lender requirements".

---

## P. GEO system for Quotr (this ICP)

### Takeaway
Build **one real developer hub** (today /developers/ only mirrors /service/), **three urgent-mode pages** (feasibility estimate, lender-ready budget, GC bid too high), **one considered decision page**, **3 residential sample deliverables**, **4–5 metro cost pages backed by Quotr data**, and a **quarterly Bay Area/LA hard-cost index**. Rewrite every service fact as a brand-attributed sentence. Off-site, BiggerPockets answers and pitching the index to CA policy orgs give the most leverage per hour.

### Cited Findings
- AI engines favor deep, single-topic pages over homepages; GPT-5.6 product, pricing and spec pages lead ChatGPT retrieval at 16.4%; brand web mentions correlate 0.664 with AIO visibility versus 0.218 for backlinks; self-ranked listicles carry risk; citation half-life is ~4.5 weeks — via framework: [Peec](https://docs.peec.ai/research/gpt-56-product-pages-vs-listicles); [Ahrefs](https://ahrefs.com/blog/ai-overview-brand-correlation/); [Something Inc.](https://somethinginc.com/blog/2026-ai-citation-data-review/); [NoGood](https://nogood.io/blog/content-freshness-ai-citations/)
- Small vendors (Meltplan, Exayard) get cited for multifamily cost with benchmark pages — repo `competitor_geo_benchmark.md`
- Quotr's /developers/ serves /service/ content; service facts are anonymized when Quotr is the only source; the turnaround conflict exists across 6+ pages — repo `entity-fact-sheet.md`, `quotr_ai_visibility_tests.md`
- Measurement: 50 prompts run daily beat 10 prompts run 5× daily (±6.1 vs ±13.2 points monthly); treat changes as real only beyond ±10% month-over-month and persisting 3 periods — via framework: [Peec](https://peec.ai/blog/the-key-to-prompt-tracking); [Texta](https://www.texta.ai/blog/answer-variability-study-why-chatgpt-gives-different-answers)

### Inferences
**P.1 Owning pages (titles and slugs; U = urgent mode, C = considered mode)**

| Page | Slug | Mode | Leads with | Answers |
|---|---|---|---|---|
| Developer hub: "Construction cost estimates and pro formas for real estate developers" | /developers/ (make it real; keep /service/ canonical for the service) | Both | 60-word answer: what you send, what you get, price ($0.25/sf), one turnaround, sample links | S2, B1, B3 |
| "Need a construction cost estimate before your feasibility period ends?" | /developers/feasibility-estimate/ | **U** | What we need (lot, unit mix, massing/SD), turnaround, price calculator, sample | C1, F1, F9, F12 |
| "Lender-ready construction budget: what lenders ask for, and a sample" | /developers/lender-ready-construction-budget/ | **U** | Trade breakdown, contingency, soft costs, named preparer, downloadable sample | C2, F2, F4 |
| "GC bid came in over budget? Check it line by line and value-engineer" | /developers/gc-bid-over-budget/ | **U** | 5-step bid check, VE levers in $, procurement option | C3, F3, S6 |
| "Cost consultant vs GC preconstruction vs AI estimating service (2026)" | /developers/cost-consultant-vs-gc-precon-vs-ai-estimating/ | **C** | Fair comparison table: price, speed, independence, lender acceptance, early-drawing ability; where Quotr is *not* the right choice | S4, F6, F7, B2 |
| Sample deliverables (HTML + PDF): fourplex Oakland; SB 9 two-home split San Jose; 24-unit walk-up; LA fire rebuild + ADU | /developers/samples/{fourplex-oakland, sb9-lot-split-san-jose, 24-unit-walk-up, la-fire-rebuild-adu}/ | C | Line items, adders, assumptions, date | L-stage proof |
| Metro cost pages (data-backed only; max 5) | /cost-to-build/bay-area/ · /cost-to-build/los-angeles/ · /cost-to-build/austin/ · /cost-to-build/seattle-portland/ · (later) /cost-to-build/south-florida/ | C | $/sf and $/door by product (ADU, SB 9 home, fourplex, townhome, walk-up), adders (utilities, SDC/impact fees, septic), date, method | S1, S5, F1, F5 |
| Product answer pages | /cost-to-build/fourplex/ · /cost-to-build/adu-california/ · /cost-to-build/sb-9-lot-split/ · /cost-to-build/build-to-rent/ · /cost-to-build/fire-rebuild-los-angeles/ | C | Range table + "what drives it" + link to sample | F5, F7, F11, F2 |
| Answer pages (habit/anxiety) | /developers/guides/estimate-accuracy-by-design-stage/ · /how-much-contingency-small-multifamily/ · /hard-vs-soft-costs/ · /cost-per-door-vs-cost-per-square-foot/ · /cost-to-build-under-sb-840/ · /opportunity-zone-2-0-rural-cost-feasibility/ | C | 40–60-word direct answer, one sourced stat per ~150 words | C5, C6, F8, F10 |
| Pro forma template (free) | /tools/development-pro-forma-template-small-multifamily/ | C | XLSX/Sheets with hard/soft/land/contingency, linked to the service | L-138 |
| **Quotr Residential Hard-Cost Index** (quarterly) + methodology | /data/hard-cost-index/ (+ /q4-2026/) | C | Median $/sf by metro × product from Service and Procurement jobs; n; date; method | C6, C7 |

**Copy rules for every page:** state facts as "Quotr.ai's Service charges $0.25/sq ft…" (fixes C12 anonymization). Publish **one** turnaround (e.g., "3–4 business days; pro formas 2–3; rush TO CONFIRM"). Name the estimator or reviewer. Date every number. Fix or explain the 50k pricing cliff.

**P.2 Proof assets and original data**
1. **Quarterly Bay Area/LA hard-cost index** from Service + Procurement data (Quotr claims "$1.2B+ estimated"; method unpublished; what can be shared is TO CONFIRM). Release a Q4 2026 edition in January 2027 to ride the fresh-start landmark.
2. **Three residential samples** (above). Today's samples are mostly commercial.
3. **BiltWise case study with numbers** ("developer-stage budgets"; the full case is not read; TO CONFIRM).
4. **Lender acceptance statement**: one named construction lender or broker quote (TO CONFIRM).
5. **Procurement savings cards** reframed for developers ($/door finish package): Saratoga $97,000 vs $187K–$218K market. Fix the "~$0" display bug.

**P.3 Off-site placements ranked by leverage per hour (Likely)**

| Rank | Placement | Why | Effort | Engine |
|---|---|---|---|---|
| 1 | **Disclosed founder answers in BiggerPockets cost threads** (forums 44, 311, 432, 548) with real numbers, linking samples only where allowed | BP threads dominate open-web retrieval for these queries (R3/R4); 44% of threads ask for local cost | 1 h/week | AIO/AI Mode, Perplexity |
| 2 | **Pitch the hard-cost index** to Terner Center, CA YIMBY, Casita Coalition, ABAG, SPUR, Bisnow, BDC Network | These orgs own the CA cost/ADU pool (R5, R7); earned mentions drive AIO visibility | 4–6 h/quarter | ChatGPT, Claude, AIO |
| 3 | **Construction-lender and broker blogs** (multifamily.loans-type, Built): guest method piece, "how lenders read a budget" | Already cited for method prompts | 4 h one-off | ChatGPT, Perplexity |
| 4 | **Fair-list inclusion** for "estimating services for developers" and "pro forma software" (A.CRE, independent estimating lists) | C12 pool is thin and unbranded | 2–3 h/month | ChatGPT |
| 5 | **YouTube**: 12-minute "fourplex feasibility estimate in Oakland, start to finish" with chapters | Google surfaces cite long-form YouTube (via framework) | 6–8 h one-off | AIO/AI Mode |
| 6 | **r/RealEstateDevelopment, r/ADU**: disclosed answers, 9:1 rule | 3–6-month play | 1 h/week | Perplexity, Google |
| 7 | **BIA Bay Area / RE:Forge / PCBC** talk or member resource | Authority + press | Per event | Indirect |
| 8 | **Entity hygiene** (one fact sheet, sameAs, consistent turnaround) | Removes conflicting facts engines repeat | 2–4 h | All |

**P.4 Refresh cadence:** index and metro pages **quarterly** (Jan/Apr/Jul/Oct; add CA APR data after April 1). Price, turnaround and samples **monthly** checks. Regulation pages on effective dates (Jan 1; Texas Sept 1 in legislative years; OZ 2.0 Jan 1, 2027). Comparison page monthly. Urgent pages quarterly.

**P.5 Tracking prompts to freeze (≥4 weeks, once daily, ChatGPT + Google AI Mode, Perplexity optional)**
1. F1 (Oakland fourplex, LOI, feasibility)
2. F3 (GC bid +30%, San Jose)
3. F4 (lender wants breakdown, Sacramento)
4. F2 (Altadena rebuild + ADU)
5. S2 "construction cost estimate for real estate developers"
6. S4 "cost consultant vs GC preconstruction vs estimating service"
7. S1 "cost to build a fourplex in Oakland 2026"
8. B1 (brand: legit + lender acceptance)
Report mention, citation, recommendation and SoV (vs RSMeans, Autodesk, estimating firms, Meltplan/Exayard) at cluster level with ± ranges; brand prompts reported separately.

**P.6 Do / skip / ignore**
- **Do:** developer hub; three urgent pages; one decision page; three residential samples; quarterly index with method; 4–5 metro pages with Quotr data; brand-attributed fact sentences; a single turnaround; BP founder participation; index pitches to CA policy orgs; lender-acceptance proof.
- **Skip:** templated city pages beyond the 5 metros; a self-ranked "best estimating services" listicle; competing for "developer software" (C8) head terms; legal explainers of SB 9/SB 840/OZ 2.0 (link to law firms and own the cost angle); llms.txt and schema as citation levers (via framework).
- **Ignore:** prompt-volume counts as a decision variable; generic "trusted by developers" social proof; the 95:5 heuristic.

### Gaps
- Whether Quotr's Service data can be published in aggregate (index feasibility), lender relationships, the BiltWise details and the turnaround truth all need Quotr confirmation.

---

## Q. Known / likely / speculative

### Takeaway
The cost-spread, regulation-date, Quotr-pricing and retrieval-pool facts are solid. Sizing, channel sizes, consultant fees, lender acceptance and every interview-based claim are still open.

### Cited Findings
- See the sources in sections A–P. Every Known row below points to a cited line above.

### Inferences
| Claim class | Known (sourced) | Likely (inference, label it) | Speculative (validate first) |
|---|---|---|---|
| Size | 236117 definition; aggregator 11.8k firms (unverified); hard costs >60% of TDC (Terner) | ICP is mostly LLC sponsors invisible to NAICS; 1–10-person teams | Any national count of "small developers" |
| Geography | Bay Area +$81/sf, LA +$35/sf (2009–18); CA 2.3× TX (RAND 2025); TX SB 15/SB 840 effective Sept 1, 2025; OZ 2.0 Jan 1, 2027 with rural 30% exclusion; CA APRs due April 1; >100k CA ADUs since 2017 | Bay Area → LA → Texas → PNW → Florida order for Quotr; 4–5 metro pages justified | CA ~25k ADUs/yr; SB 684/SB 1123/HB 1110/Live Local/Austin HOME details (unverified this session) |
| Buyer language and forces | 14+ verbatim BP snippets and titles; coded sample: LC 44%, PEN 15%, OVR 13%, VAL 6%, LND 6% | Lender format and early-drawing needs are high-stakes despite low title frequency | Reddit/LinkedIn/podcast phrasing; "Sunday deal analysis" timing |
| Psychology | Anchoring, defaults and temporal landmarks robust; social proof and choice overload weak; time pressure → noncompensatory choice; trust in AI alone 5% over $500 | $/sq ft is the dominant anchor; the GC's number is the status-quo default | Ex-flipper identity effects on WTP |
| Alternatives | AI answers name ConstructionOnline, RSMeans, Autodesk, estimating firms; calculators dominate pre-plan queries; Meltplan/Exayard cited for MF cost | GC precon is "free" but conflicted | Consultant fee levels; RSMeans use by this ICP |
| Quotr | $0.25/$0.10 per sq ft; Lite $79.90, Plus $299.90; turnaround conflict; samples mostly commercial; C12 cited-not-named; Bay Area procurement cards; LA rebuild sample | 49k vs 50k sq ft pricing cliff (if flat tier); per-project Service fits 1–3 deals/yr | Lender acceptance of Quotr estimates; index publishable from Service data |
| GEO | Quotr absent in 0/9 proxy searches and 5 of 6 repo developer runs; BP threads dominate open-web cost retrieval; thin programmatic "2026 price guide" pages rank | Local-cost and developer-estimating clusters are the fastest wins | Specific timelines to first citation |

### Gaps
- Run the 8 fan-out prompts (section O Gaps). Pull Census CBP/BPS and the HCD APR dashboard. Collect Reddit, LinkedIn and podcast verbatims and channel member counts. Get cost-consultant and paid-precon fees. Run 6–12 switch interviews with recent Quotr Service developer buyers (BiltWise first) and ask, "what exactly did you type, and where?"
