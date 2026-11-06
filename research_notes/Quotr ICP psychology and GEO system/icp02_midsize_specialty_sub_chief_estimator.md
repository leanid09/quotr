# ICP 2 — Chief estimator / estimating manager at a mid-size specialty subcontractor (MEP, fire protection, glazing): ICP-depth dossier and GEO system for Quotr.ai

**As of:** 2026-11-06 · **Scope:** US · **Method:** the uploaded ICP-depth GEO framework (coding chain trigger → stage → hot/cold mode → restraining force → prompt → proof; four forces; switch timeline; prompt matrix; geography-to-segment pipeline; measurement as distributions), applied to a B2B buyer instead of ADHD parents.

**Research limits (read first).** 14 live WebSearch queries were run on 2026-11-06 before the session's shared search budget (200 per turn across all agents) was used up. Direct page fetches to census.gov, api.census.gov, bls.gov, capterra.com, forums.mikeholt.com and reddit.com were refused by the session network policy, so Census SUSB/CBP size-class tables, BLS industry tables, full review pages and subreddit member counts could **not** be pulled. Verbatim quotes below come from search-engine extracts of the named pages (marked "extract"); re-open each page before publishing a quote. Sourced material already in this repo (AGC/Sage, ServiceTitan, Dodge/CMiC, G2 buyer survey, Perplexity tests of 2026-09-25, competitor pricing) is reused with its original link and flagged "repo note, not re-checked here". Everything simulated or estimated is labeled.

**Persona shorthand used throughout:** "CE" = chief estimator / estimating manager; "MEP sub" = electrical, mechanical/HVAC, plumbing, fire protection, curtain wall/glazing subcontractor with 50–500 employees and ~$10M–$150M revenue; team of 2–10 estimators on Accubid, ConEst, McCormick, QuoteSoft/FastPipe, Trimble Estimation MEP, On-Screen Takeoff (OST), PlanSwift or Bluebeam Revu; buying committee = owner/president, CFO/controller, IT (often outsourced MSP).

---

## A. Definition and size

### Takeaway
The firm count for the 50–499-employee band could not be pulled from SUSB in this session; an explicitly labeled estimate puts it at roughly **6,000–9,500 US firms** across NAICS 2382x + 238150 (speculative, order-of-magnitude). The value anchor is solid: the median cost estimator in **specialty trade contractors earned $79,130 (May 2024)**, which equals ~22 Quotr Plus seat-years or ~83 Lite seat-years.

### Cited Findings
- BLS OOH: cost estimators' median annual wage **$77,070 (May 2024)**; in **specialty trade contractors $79,130**; lowest 10% < **$46,330**, highest 10% > **$128,640** — [BLS Occupational Outlook Handbook, Cost Estimators](https://www.bls.gov/ooh/Business-and-Financial/Cost-estimators.htm) (via search extract; page fetch blocked).
- Third-party (not BLS) reports a May 2025 OEWS national median of **$78,740** — [Wagedex SOC 13-1051](https://wagedex.com/jobs/cost-estimators). Treat as unverified until the BLS May 2025 table is opened.
- Census published **2022 SUSB** tables by industry and enterprise employment size (U.S. and state, 6-digit NAICS) — [Census 2022 SUSB annual tables](https://www.census.gov/data/tables/2022/econ/susb/2022-susb-annual.html); [release note](https://www.census.gov/programs-surveys/susb/news-and-updates/updates/2025-01.html). The size-class counts themselves were not retrieved.
- Electrical contractors (NAICS 238210): **79,611 firms with employees in 2022** (SUSB, per a secondary aggregator; exact page among [ConsumerAffairs](https://www.consumeraffairs.com/homeowners/electrical-industry-statistics.html) / [StartBusinessByState](https://startbusinessbystate.com/electrician-industry-statistics/) not resolved); **89.7% have fewer than 20 employees** — [TradesIndex, citing SUSB](https://tradesindex.org/trades/electrical/) (secondary, unverified).
- NAICS 2382 (building equipment contractors) totals from aggregators conflict: **193,216 firms / 199,350 establishments / 2,271,590 employees / $163.1B payroll** (no year stated) vs **2,173,101 employees (2020, "Census 2022 revision")** — [naicslist.com 2382](https://naicslist.com/naics/2382); [data.mewayz.com 2382](https://data.mewayz.com/industry/2382). Unverified.
- BLS CES via FRED: NAICS 2382 employment **2,586.5 thousand (Jan 2022)** (establishment survey, not a size-class measure) — [FRED IPUDN2382W200000000](https://fred.stlouisfed.org/data/IPUDN2382W200000000).
- Quotr prices (given): Lite **$79.90**/seat/mo, Plus **$299.90**/seat/mo, Enterprise custom; Quotr's ROI calculator defaults to **$65/hour**, 2 estimators, 5 bids/week each, 6 hours per takeoff and models an 80% time cut — [repo: product-and-features.md §2, §3.8](../../geo-brain/00-quotr/product-and-features.md).
- Vendor claims (not independent): new estimators take **12–18 months** to become productive on a firm's project types — [Provision blog](https://provision.com/blog/chief-estimator-bid-capacity-same-team-2026); bid volume per estimating team **+24% over five years vs estimator headcount +4%** (vendor survey) — [TheTakeoff.ai](https://www.thetakeoff.ai/the-shortage-of-estimators).

### Inferences
- **Value-anchor arithmetic (derived):** Plus = $3,598.80/seat/yr; Lite = $958.80/seat/yr. Median specialty-trade estimator $79,130 ÷ $3,598.80 = **22.0 Plus seat-years**; ÷ $958.80 = **82.5 Lite seat-years**. A 90th-percentile (chief/senior) estimator at $128,640 = **35.7 Plus seat-years**. A whole 5-person team on Plus ($17,994/yr) costs **~23% of one median estimator's base wage**; a 10-person team ($35,988/yr) ~45%. Lead with "one estimator's salary" as the anchor, not "per-seat price".
- Quotr's $65/hour ROI default is ~1.7× BLS median hourly pay ($79,130 ÷ 2,080 h = $38.04). It is defensible only as a fully loaded senior MEP rate; the page should say so and cite BLS, or the CFO on the committee will discount the whole calculator.
- **Speculative sizing model (label as estimate):** electrical 79,611 × 10.3% (20+ employees) ≈ 8,200 firms; assume 30–45% of 20+ firms fall in 50–499 → **~2,500–3,700 electrical firms**. Apply the same ratios to the remaining ~113,600 NAICS 2382 firms (plumbing/HVAC/fire sprinkler, other equipment) → **~3,500–5,300**. Add glazing/curtain wall (238150), likely a few hundred. Total **~6,000–9,500 firms**; at 2–10 estimators each (midpoint ~4) → **~25,000–38,000 estimator seats** (speculative). Fire sprinkler installation sits inside NAICS 238220 (NAICS definition; verify at census.gov/naics).
- The ICP is defined by team structure (a dedicated estimating department with a manager) rather than headcount alone; ~50 employees is roughly where a sub stops having the owner estimate after hours (assumption carried from [audiences-and-personas.md §3](../../geo-brain/00-quotr/audiences-and-personas.md), "confirm with customer interviews").

### Gaps
- SUSB 2022 enterprise-size counts for 238210/238220/238290/238150 (file `us_state_6digitnaics_2022.xlsx`; sum classes 50–99 and 100–499; note SUSB's top class splits at 500) — blocked; pull when census.gov is allowed.
- BLS OEWS May 2025 industry rows for NAICS 2382/2381 (employment and mean wage of 13-1051) — blocked.
- No ASPE, MCAA, NECA or SMACNA estimator salary survey or estimating-department size benchmark was retrieved.

---

## B. Geography

### Takeaway
No metro-level evidence could be retrieved this session, so geography is presented as a pipeline plus candidate segments tagged "likely/speculative". The one sourced macro signal: AGC/Sage's 2026 outlook headline says contractors expect a weak 2026 **"apart from data centers and power projects"**. Geo pages are justified only for a data-center MEP hub and for original labor-rate data by metro; state pages are not.

### Cited Findings
- AGC/Sage 2026 Construction Hiring & Business Outlook (Jan 2026): "Contractors have dampened expectations for 2026 apart from data centers and power projects amid worries about…" (release title) — [AGC news release](https://www.agc.org/news/2026/01/08/contractors-have-dampened-expectations-2026-apart-data-centers-and-power-projects-amid-worries-about) (repo note, not re-checked).
- Quotr already has a sector post, "data-center-construction-estimating-mep-subcontractor-choke-point" (2026-06-11) — [quotr.ai post](https://quotr.ai/blog/data-center-construction-estimating-mep-subcontractor-choke-point/); repo marks it KEEP for prompt L-146 "how to estimate MEP costs on a data center project" — [prompt-library.md](../../geo-brain/04-prompt-library/prompt-library.md).
- Quotr's database prices "by US zip code" with "material, labor, and assembly rates by region" — [repo: product-and-features.md §3.3](../../geo-brain/00-quotr/product-and-features.md).
- Estimator wages vary by metro and are published per metro by BLS and re-published programmatically (Wagedex has pages for Omaha, Reading PA, Eugene OR, College Station TX, etc.) — [Wagedex metro pages](https://wagedex.com/jobs/cost-estimators/metro/omaha-ne-ia).

### Inferences
**Geography-to-segment pipeline adapted from the framework (unit = MSA; join on CBSA code):**

| Layer | Variable | Source to pull | Weight (software buyer) |
|---|---|---|---|
| A. Firm density | Establishments in 238210/238220/238290/238150 with 50–499 employees | Census CBP 2022/2023 by MSA × size class | 0.30 |
| B. Bid-volume pressure | Data-center MW under construction; semiconductor/battery plant capex; hospital construction starts | CBRE/JLL data-center reports; Commerce CHIPS awards; Dodge starts | 0.30 |
| C. Estimator scarcity/cost | 13-1051 employment and mean wage by MSA; job-posting count | BLS OEWS MSA file; Indeed/LinkedIn | 0.20 |
| D. Labor-model complexity | Union density (NECA/IBEW, UA, SMART) vs open shop; prevailing-wage share | NECA/MCAA chapter maps; state DOL | 0.10 |
| E. Demand signal | Trends/Keyword Planner at DMA for "electrical estimating software", "MEP estimator jobs" | Google Trends (DMA only) | 0.10 |

**Candidate priority segments (speculative until the rows are filled):**

| # | Segment | Why (brief + reasoning) | Evidence row status |
|---|---|---|---|
| 1 | **Northern Virginia / DC–Baltimore data-center electrical & mechanical subs** | Brief names it as the largest data-center bid market; electrical scope dominates data-center MEP value (inference) | To fill (CBRE MW, CBP 238210 50–499 in DC MSA, OEWS wage) |
| 2 | **Phoenix** (data centers + semiconductor fab work) | Brief names data centers and semiconductor plants; mechanical/process piping and electrical demand | To fill |
| 3 | **Dallas–Fort Worth / Texas Triangle** | Brief names DFW; large open-shop MEP base (likely) | To fill |
| 4 | **Columbus / Central Ohio** | Brief names Columbus; data-center and fab-related work (fab timing must be verified) | To fill |
| 5 | **Atlanta** | Brief names Atlanta; data centers + healthcare | To fill |

- **Are geo pages justified?** Only where the facts genuinely differ (framework rule). For software, the differences that are real and citable are (a) bid-volume drivers (data centers, fabs, hospitals), (b) estimator wage levels by metro (BLS), and (c) labor-rate assumptions (union vs open shop). So: **one data-center MEP estimating hub** with a 5-metro evidence table, and **one "MEP labor rates and estimator cost by metro" data page** built from BLS + Quotr's own regional database (if Quotr permits publishing aggregates — TO CONFIRM). **Skip** 50-state or city pages for software — scaled-content risk per the framework.
- Quotr's Enterprise tier includes on-site onboarding; a Bay Area base makes West-Coast on-site cheapest, but none of the five bid-hot metros are in California (inference).

### Gaps
- No data-center pipeline (MW), fab capex, hospital starts, CBP-by-MSA counts or OEWS-by-MSA wages were retrieved; the five metros are from the brief, not verified here.
- Union vs open-shop share by metro for MEP trades not retrieved.

---

## C. Jobs-to-be-done (in their words)

### Takeaway
Five jobs recur across the evidence: bid more with the same team, never miss scope, keep the database/labor units, get off an aging or repriced license without a bad bid season, and prove payback to the owner. The phrasings below are synthesized from the sourced pains (no switch interviews exist yet).

### Cited Findings
- Vendor content aimed at this exact buyer is titled "Chief Estimator's Guide to Bidding More Work With the Same Team in 2026" — [Provision](https://provision.com/blog/chief-estimator-bid-capacity-same-team-2026); "Your Best Estimator Retires in 5 Years. Your Bid Volume Doesn't." — [Atreyus](https://atreyus.ai/research/best-estimator-retires-bid-volume-doesnt); recruiters frame the role as "Chief Estimator Recruiting: Bid Risk Is Raising the Bar" — [Birm Group](https://thebirmgroup.com/chief-estimator-recruiting-bid-risk-preconstruction-leaders/).
- Estimators often lack time to cross-check drawings against Division 23 for coordination conflicts (vendor claim) — [Provision](https://provision.com/blog/chief-estimator-bid-capacity-same-team-2026).
- Accubid Anywhere reviewer: can't use existing databases and would need to rebuild them (paraphrase of extract) — [Capterra Accubid Anywhere reviews](https://www.capterra.com/p/193712/Trimble-Accubid-Anywhere/reviews/).
- Quotr's own pain framing: "Scope Gaps Cost More Than Pricing Errors" — [quotr.ai post](https://quotr.ai/blog/scope-gap-construction/) (repo).

### Inferences
| # | Job (synthesized, first person) | Force it maps to |
|---|---|---|
| J1 | "Get more bids out the door with the people I have — I can't hire another estimator fast enough." | Push (capacity) |
| J2 | "Make sure we never leave a feeder, a riser or a whole spec section off a bid again." | Push (fear of missed scope) |
| J3 | "Keep 15 years of labor units, assemblies and pricing — don't make me rebuild the database." | Habit/anxiety (data) |
| J4 | "Get my team off a license that's being sunset or repriced without blowing a bid season." | Push (vendor event) |
| J5 | "Show the owner and CFO, with our own numbers, that this pays back before I put my name on it." | Anxiety (career risk) |

### Gaps
- No switch interviews with CEs; jobs need validation (framework: 9–17 interviews for saturation).

---

## D. Psychology

### Takeaway
The CE's status rests on bid accuracy and on owning the firm's estimating database; a failed rollout during bid season is a visible career risk, so this buyer decides by side-by-side proof on a past bid, defers to habit, and only switches when a dated push (license end, resignation, volume spike) forces the issue. Design for status-quo bias, anchoring and temporal landmarks; ignore generic social proof.

### Cited Findings
- Incumbent preference is largely about which tool an estimator learned first: Mike Holt forum users describe Accubid and ConEst as "both… good estimating programs that have extensive data bases of items and assemblies. They both do basically the same thing." (extract) — [Mike Holt forum, Accubid vs ConEst](https://forums.mikeholt.com/threads/accubid-vs-conest.140707/post-2201733); [earlier thread](https://forums.mikeholt.com/threads/accubid-vs-conest.41000/post-41000) (post-level attribution not resolved).
- Contractors' top AI concerns: **data accuracy 57%, security 54%**; only **19%** have adapted workflows; only **26%** rate their own data quality high (Dodge/CMiC, 235 GCs and trade contractors, Dec 2025) — [Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/) (repo note, not re-checked).
- Construction leaders' trust in AI fell **14 points** year over year (Autodesk 2025) — [Autodesk](https://www.autodesk.com/blogs/construction/state-of-design-make-spotlight-construction/) (repo note).
- r/estimators threads describe AI takeoff as "hit-or-miss" — [r/estimators](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/) (observed via Perplexity in the repo audit; reddit not reachable here).
- Burnout loop: pressure never to decline bids plus unrealistic deadlines → burnout → turnover → more load on the rest (vendor article) — [SketchDeck](https://sketchdeck.ai/blog/the-steel-estimating-crunch-labor-capacity-and-competitive-pressure-explained/).
- Replication ranking to design around (from the framework): defaults/status quo **d = 0.68** — [Jachimowicz et al. 2019](https://ideas.repec.org/a/cup/bpubpo/v3y2019i02p159-186_00.html); anchoring replicates strongly — [Scientific American](https://www.scientificamerican.com/article/dozens-of-labs-respond-to-bolster-reliability-of-psychology-research); temporal landmarks — [Dai, Milkman & Riis 2014](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf); generic social proof fragile — [DellaVigna & Linos](https://www.nber.org/system/files/working_papers/w27594/w27594.pdf); choice overload d ≈ 0.02 — [Scheibehenne et al.](https://academic.oup.com/jcr/article/37/3/409/1816569); time pressure shifts to noncompensatory rules — [Dhar & Nowlis 1999](https://profiles.wustl.edu/en/publications/the-effect-of-time-pressure-on-consumer-choice-deferral/).

### Inferences
| Dimension | Profile (likely unless marked) |
|---|---|
| Identity/status | "The person whose number goes out the door." Status = hit rate + no blown jobs + the database they built. Often promoted from estimator; may hold a CPE (ASPE) or came up as a journeyman (speculative). |
| Career risk | A rollout that slows the team during bid season, or one missed-scope loss traced to AI counts, is attributed to the CE personally; owner sees cost, not counterfactual. |
| Core fear | Missed scope on a hard-bid job the firm then must build at a loss (J2). AI is feared as a new source of silent misses. |
| Decision style | Committee: CE = champion and evaluator; owner/president = approver; CFO = payback; IT/MSP = security veto. Evidence = re-run a past bid (known answer) side-by-side; reference from a same-trade sub; 30–90-day pilot on overflow work (speculative durations). |
| Hot moments (urgent mode) | Bid-day crunch (multiple bids due same week); the week an estimator resigns; a renewal/sunset notice (e.g., Bluebeam Revu 20 EOL Dec 31, 2026); after losing a job on a scope miss. Time of day: evenings and weekends after bid days (speculative). |
| Cold moments (considered mode) | Post-bid lulls, budget season (Q4 for calendar-year firms), January planning, vendor renewal 60–90 days out (speculative). |

**Biases to design for (ranked by replication):**
1. **Status quo/default (robust):** offer a "keep your estimating tool, add AI counts" path first; full replacement second. A default migration plan (who does what in weeks 1–4) lowers deferral.
2. **Anchoring (robust):** anchor on one estimator's salary ($79,130 median, BLS) and on the incumbent's per-seat cost (PlanSwift $1,749–$3,000/yr; Accubid "$3,000+"/yr unverified), never on Lite's $79.90 alone.
3. **Temporal landmarks (robust):** Dec 31, 2026 Bluebeam Revu 20 EOL; vendor renewal dates; fiscal year start; post-bid-season "fresh start".
4. **Time pressure (supported):** urgent pages must lead with 1–2 decisive cues (works on your drawings by Monday; done-for-you overflow at a fixed per-sq-ft price).
5. **Social proof (fragile generic, strong specific):** "thousands of contractors" lines are worthless; a named same-trade sub with before/after numbers is the risk reducer B2B buyers need (inference).

### Gaps
- No CE interviews; time-of-day/week patterns are unmeasured.
- No data on how often CEs (vs owners) initiate software searches.

---

## E. Four forces (push, pull, anxiety, habit) with verbatim quotes

### Takeaway
Push is dominated by incumbent price, support and bugs plus capacity pressure; pull is cloud access and speed; anxiety is AI accuracy, database migration and learning curve; habit is "they all do the same thing" and loyalty to the classic desktop version. Quotes are review/forum extracts — re-open each URL before publishing.

### Cited Findings
| # | Force | Verbatim (extract) | Speaker / context | Source |
|---|---|---|---|---|
| 1 | Push (support) | "the tech would just close the ticket without calling or resolution" | Accubid Anywhere reviewer | [Capterra](https://www.capterra.com/p/193712/Trimble-Accubid-Anywhere/reviews/) |
| 2 | Push (support) | phone hold of "over 2.5 hour" … "without a pick up" (fragments) | Accubid Anywhere reviewer | [Capterra](https://www.capterra.com/p/193712/Trimble-Accubid-Anywhere/reviews/) |
| 3 | Push (price) | "the per user cost is expensive" | Accubid reviewer | [Capterra](https://www.capterra.com/p/193712/Trimble-Accubid-Anywhere/reviews/) |
| 4 | Push (quality) / Anxiety (new versions) | "lots of bugs with the program that should have been ironed out before releasing the new program" | Accubid Anywhere reviewer (vs Classic) | [Capterra p.2](https://www.capterra.com/p/193712/Trimble-Accubid-Anywhere/reviews/?page=2) |
| 5 | Habit | "Classic version is still far better" | Accubid reviewer | [Capterra p.2](https://www.capterra.com/p/193712/Trimble-Accubid-Anywhere/reviews/?page=2) |
| 6 | Push (rigidity) | "assemblies are not very dynamic" | Accubid reviewer | [Capterra](https://www.capterra.com/p/193712/Trimble-Accubid-Anywhere/reviews/) |
| 7 | Anxiety (learning) | "the learning curve on Enterprise is steep"; "high cost for one on one training" | Accubid reviewers | [Capterra](https://www.capterra.com/p/193712/Trimble-Accubid-Anywhere/reviews/) |
| 8 | Push (vendor) | "a lot of problems waiting on the sale team not calling me back" | Accubid reviewer | [Capterra](https://www.capterra.com/p/193712/Trimble-Accubid-Anywhere/reviews/) |
| 9 | Habit | "both… good estimating programs that have extensive data bases of items and assemblies. They both do basically the same thing." | Electrical forum member | [Mike Holt forum](https://forums.mikeholt.com/threads/accubid-vs-conest.140707/post-2201733) |
| 10 | Pull (UX) | ConEst gives "better control over the input with way fewer mouse clicks" | Ex-Accubid user | [Mike Holt forum](https://forums.mikeholt.com/threads/accubid-vs-conest.41000/post-41000) (post not resolved) |
| 11 | Pull (UX) | "Accubid/Livecount is much more up to date, easy to navigate and learn" | Forum member | [Mike Holt forum](https://forums.mikeholt.com/threads/accubid-vs-conest.140707/post-2201733) (post not resolved) |
| 12 | Pull (cloud) | "even if our internal systems are down, we're still able to estimate" | Estimating manager, Trimble launch customer (2019) | [Trimble/PR Newswire](https://www.prnewswire.com/news-releases/trimble-announces-accubid-anywhere-an-all-in-one-hosted-estimating-solution-for-mep-and-ict-contractors-300897650.html) |
| 13 | Pull (cloud) | "anytime we log on, we know we are using the latest version of the software" | Same | [Trimble/PR Newswire](https://www.prnewswire.com/news-releases/trimble-announces-accubid-anywhere-an-all-in-one-hosted-estimating-solution-for-mep-and-ict-contractors-300897650.html) |
| 14 | Anxiety (AI) | AI takeoff is "hit-or-miss" | r/estimators users | [r/estimators](https://www.reddit.com/r/estimators/comments/1qjzjfi/is_there_an_ai_automated_takeoff_software_tool/) (repo, via Perplexity) |
| 15 | Push (price, third-party) | McCormick "can be expensive, especially for smaller construction firms or independent estimators" | SelectHub analyst | [SelectHub](https://www.selecthub.com/p/construction-estimating-software/mccormick-estimating/) |
| 16 | Push (vendor policy) | "Revu 21 utilizes a subscription model, rather than a licensing and maintenance model." | Bluebeam support | [Bluebeam licensing FAQ](https://support.bluebeam.com/revu/resources/licensing-and-installation-faq.html) |

Supporting non-quote evidence:
- Accubid Anywhere: **3.7/5 from 69 reviews** on Capterra; Capterra's own summary notes slow operation, extra clicks, delayed calculations and errors — [Capterra](https://www.capterra.com/p/193712/Trimble-Accubid-Anywhere/reviews/).
- A Mike Holt poll of **23 voters**: ConEst **43.5%**, Accubid **30.4%** (likely the "top 3 estimating software poll" thread) — [Mike Holt poll](https://forums.mikeholt.com/threads/top-3-estimating-software-poll.64425/page-2).
- A forum member asked whether ConEst customers had to rebuild databases moving from Windows XP to Vista (an Accubid salesperson's claim; unanswered) — [Mike Holt forum](https://forums.mikeholt.com/threads/accubid-vs-conest.140707/post-2201733) — i.e., migration fear is used as a competitive weapon.

### Inferences
| Force | Strength for this ICP | Prompt class it generates (framework mapping) | Content that answers it |
|---|---|---|---|
| Push | High when a dated event exists; otherwise chronic | "why is our estimating so slow / is it normal to wait 2 hours for Trimble support / estimator quit what now" | Urgent answer pages; capacity calculator |
| Pull | Medium; cloud and speed are known, AI counts are the new pull | "what actually works for electrical takeoff on data center drawings" | Decision pages with trade-specific demos |
| Anxiety | **Highest**: AI accuracy, DB migration, learning curve, security | "is AI takeoff accurate for MEP / Quotr vs Togal / can I import my Accubid database / SOC 2" | Benchmarks, migration guide, security page |
| Habit | High: "they all do the same thing", Classic loyalty, database lock-in | "do I really need to replace Accubid / can I just keep Bluebeam" | "Keep your estimating tool, add AI counts" coexistence page |

A content plan answering only pull prompts leaves the two restraining forces — the strongest here — unaddressed.

### Gaps
- No verbatim quotes retrieved for ConEst, McCormick, QuoteSoft/FastPipe, Trimble Estimation MEP, OST, fire protection or glazing estimators (search budget exhausted; review sites blocked). r/estimators, r/electricians, r/HVAC and ContractorTalk threads could not be opened.
- No LinkedIn or YouTube comment quotes retrieved.

---

## F. Trigger events and trigger calendar

### Takeaway
The single most actionable dated trigger is **Bluebeam Revu 20's end of life on December 31, 2026** (eight weeks from now): perpetual Revu 20 loses Studio and API features and open/enterprise licenses are deactivated, forcing a Revu 21 subscription decision. PlanSwift's 2025 move to subscription and Trimble's long push to Accubid Anywhere are real but older; no 2025–2026 Accubid/ConEst/McCormick sunset was found.

### Cited Findings
**Vendor events (verified 2024–2026 changes in bold):**
| Vendor | What changed | Date | Source |
|---|---|---|---|
| Bluebeam | Perpetual license sales ended | Sep 30, 2023 | [Bluebeam Revu 20 EOL](https://www.bluebeam.com/upgrade-from-revu-20/); [Graitec](https://graitec.com/us/tech-resources/bluebeam-ends-sales-of-perpetual-licenses-open-and-enterprise-licensing/) |
| Bluebeam | **Revu 20 end of support**: tech support and self-service license management end; license reassignment to new machines no longer supported | **Jul 31, 2026** | [Bluebeam](https://www.bluebeam.com/upgrade-from-revu-20/); [ncored](https://ncored.com/guides/bluebeam-revu-20-end-of-life.html) |
| Bluebeam | **Revu 20 end of life**: perpetual loses Studio Sessions/Projects and API integrations; a serial-1 perpetual license can still run locally; open and enterprise licenses deactivated on or before this date | **Dec 31, 2026** | [Bluebeam](https://www.bluebeam.com/upgrade-from-revu-20/); [Graitec](https://graitec.com/us/tech-resources/bluebeam-ends-sales-of-perpetual-licenses-open-and-enterprise-licensing/) |
| Bluebeam | Revu 21 subscription-only, annual per named user, no monthly option; ~$260–$590/user/yr (third-party) | Ongoing | [Bluebeam FAQ](https://support.bluebeam.com/revu/resources/licensing-and-installation-faq.html); [Drawboard](https://www.drawboard.com/blog/bluebeam-pricing) |
| Bluebeam | AI "Max" tier added (search summary) | May 2026 | [repo: bluebeam.md](../../geo-brain/03-market/competitors/bluebeam.md) |
| PlanSwift (ConstructConnect) | **Subscription-only for new buyers** (several blogs say perpetual ended 2025; ConstructConnect support still lists legacy perpetual customers); price ~$1,749–$2,000/seat/yr, Essential $2,000 vs Core $3,000 reported; old perpetual $1,595 + ~$200–250/yr maintenance; lapsed maintenance not reinstated | 2025 | [Vertigraph](https://www.vertigraph.com/learn/takeoff-software-pricing-2026); [Struvia pricing](https://www.struvia.co/blog/planswift-pricing-review); [Exayard](https://exayard.com/blog/planswift-software-cost); [Fervor Studio](https://fervorstudio.ca/news/planswift-review-pricing-alternatives/); [Quotr post](https://quotr.ai/blog/best-planswift-alternatives-2026/) |
| PlanSwift | **Sign-in moves from license key to email/password** for subscription and perpetual customers (sign-in only, not price) | **Jun 2026** | Same result set (one source; not resolved) |
| ConstructConnect Takeoff | Annual contracts cannot be cancelled mid-term (one source) | — | Same result set |
| Trimble Accubid | Accubid Anywhere launched as cloud-hosted subscription at MEP Basecamp; later Project and Extension APIs | Aug 7, 2019; APIs later | [Trimble news](https://news.trimble.com/2019-08-07-Trimble-Announces-Accubid-Anywhere,-an-All-In-One-Hosted-Estimating-Solution-for-MEP-and-ICT-Contractors); [Engineering.com](https://www.engineering.com/trimble-adds-new-api-capabilities-to-accubid-anywhere-estimating-application/) |
| Trimble MEP | Portfolio "available on subscription"; License Management Portal still lists Accubid Classic, Trimble Estimation Desktop and pooled perpetual AutoBid licenses; **no announced Classic/perpetual end found** (a Trimble poster in a SketchUp forum said no end to perpetual support had been announced — different product) | Ongoing | [Trimble MEP](https://mep.trimble.com/en-gb/resources/home/top-5-subscription-benefits-for-mep-companies); [License portal guide (PDF)](https://s3.amazonaws.com/mepdownloads-na.trimble.com/client-downloads/Autobid/Support/Downloads/License+Management+Portal+-+User+Guide.pdf); [SketchUcation](https://community.sketchucation.com/post/1568270) |
| McCormick (Foundation Software) | **Press release on cloud vs on-premises**: floating licensing on hosted platforms vs named licensing on-prem; "Cloud or desktop deployable" | **Jul 24, 2026** | [AccessNewswire](https://www.accessnewswire.com/newsroom/en/computers-technology-and-internet/mccormick-breaks-down-cloud-vs.-on-premises-estimating-software-f-1194167); [McCormick 2026 guide](https://www.mccormicksys.com/blog/the-best-electrical-estimating-software-2026-guide/) |
| ConEst (JDM Technology Group) | Since 1989; IntelliBid, SureCount, Conest Connect, CE Cloud; acquired Cert-In (undated); **no 2025 acquisition found** | — | [conest.com](https://conest.com/); [news](https://conest.com/news/); [CE Cloud](https://conest.com/products/ce-cloud-software/) |
| Procore | Acquired Esticom (electrical estimating) | 2020 | [V2 Cloud](https://v2cloud.com/guides/electrical-estimating-software/conest-vs-esticom) |
| eTakeoff | Announced AI takeoff | Oct 30, 2024 | [BusinessWire](https://www.businesswire.com/news/home/20241030940672/en/eTakeoff-Announces-Availability-of-Cutting-Edge-AI-Takeoff-Solution) |

**Industry-calendar items with sources:** AGC/Sage outlook (January) — [AGC](https://www.agc.org/news/2026/01/08/contractors-have-dampened-expectations-2026-apart-data-centers-and-power-projects-amid-worries-about); ServiceTitan commercial specialty contractor report (Mar 30, 2026) — [ServiceTitan](https://www.servicetitan.com/press/servicetitan-report-finds-ai-adoption-more-than-doubles-among-commercial); Dodge/CMiC AI survey (Dec 2025) — [BusinessWire](https://www.businesswire.com/news/home/20251205015633/en/New-Research-Reveals-Strong-Contractor-Optimism-About-AIs-Transformative-Impact-on-Construction-Industry) (repo notes).

### Inferences
**Trigger calendar (dated where sourced; other timing speculative):**
| Window | Trigger | Type | Expected prompt surge (speculative) |
|---|---|---|---|
| Now → Dec 31, 2026 | Bluebeam Revu 20 EOL; open/enterprise deactivation | Vendor, hard date | "Revu 20 end of life what to do", "Bluebeam alternative for takeoff counts", "Revu 21 price per user" |
| Q4 (Oct–Dec) | Budget season for calendar-FY firms; annual renewals (PlanSwift/OST, Bluebeam, Togal annual billing) | Budget/renewal | "is X worth renewing", "X alternatives 2027" |
| Jan–Feb | Fresh-start landmark; outlook reports; post-bonus resignations (speculative) | Landmark/people | "estimator quit how to cover bids", "hire vs outsource estimator" |
| Spring–summer | Peak bid season (speculative; varies by market) | Volume | "outsourced MEP takeoff fast turnaround", "bid more with same team" |
| Any time | Estimator resigns/retires; hit rate drops; scope-miss loss; data-center invite spike; server/OS refresh retires on-prem install | Internal, datable | Situation-first prompts (see M) |

- Windows 10 end of support (Oct 2025, Microsoft) and on-prem server refreshes are plausible triggers for desktop-estimating migrations (verify date and relevance; not researched here).

### Gaps
- Whether Trimble has announced any end of sale/support for Accubid Classic, Trimble Estimation (QuoteSoft/AutoBid) or price increases in 2025–2026: not found; must check Trimble MEP notices directly.
- OST pricing/subscription changes 2024–2026: not retrieved separately (OST and PlanSwift are both ConstructConnect).
- NECA, MCAA, SMACNA, AFSA, ASPE 2026–2027 event dates: not retrieved.

---

## G. Switch timeline with prompt form at each stage

### Takeaway
This buyer's timeline is long and gated by a committee: first thought is triggered by a person or a deadline, passive looking happens in forums and peers, active looking begins with incumbent-named "alternatives" and "vs" prompts, and deciding turns on a past-bid side-by-side plus security review. Durations below are speculative.

### Cited Findings
- Framework timeline: first thought → passive looking → active looking → deciding → consuming; prompt specificity rises along it (problem-aware → category noun → brand + price + objection) — [uploaded framework](</root/.claude/uploads/0814826c-2913-57ec-9cf0-acc28e8d23b1/3fb5eb52-ICP_depth_framework_for_GEO.md>); Moesta's forces model — [jobstobedone.org](https://jobstobedone.org/?p=3423).
- B2B buyers: **51%** start software research in an AI chatbot more often than Google; **71%** use chatbots somewhere; **69%** chose a different vendor than planned because of chatbot guidance; **40%** say evaluation is the longest stage (G2, Mar 2026, cross-industry) — [G2 press release](https://www.prnewswire.com/news-releases/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots-302742807.html) (repo note).
- Capterra construction buyers expect to spend **~$1,600–$4,000/yr**; estimating is the most-requested feature — [Capterra buyer insight](https://www.capterra.com/resources/construction-software-buyer-insight/) (repo note).

### Inferences
| Stage | Duration (speculative) | Who | Prompt form (example) | Engine/venue |
|---|---|---|---|---|
| 1. First thought | Days after trigger | CE | Situation, no category noun: "my senior electrical estimator just quit and we have 4 data center bids due in 3 weeks what do I do" | ChatGPT (memory on), peers |
| 2. Passive looking | 1–3 months | CE | Category + incumbent: "is AI takeoff any good for electrical yet", "anyone replaced Accubid" | r/estimators, Mike Holt, LinkedIn, ChatGPT |
| 3. Active looking | 1–2 months | CE + 1 senior estimator | Brand-laden comparison: "Accubid alternatives with AI takeoff 2026", "Togal vs Beam vs Quotr for MEP" | ChatGPT, Google AI Mode, G2/Capterra compare pages |
| 4. Deciding | 1–3 months | Committee | Objection + proof: "Quotr SOC 2", "can Quotr import Accubid labor units", "AI takeoff accuracy test electrical", "cost of estimator vs software" | ChatGPT/Copilot (IT), vendor pages, references |
| 5. Consuming / onboarding | 1–3 months | Team | "how to set up assemblies in Quotr", "export Quotr takeoff to Accubid/Excel" | Vendor docs, YouTube |
| 6. Re-decision | Annual renewal | CE + CFO | "is Quotr worth it vs Togal renewal" | ChatGPT |

### Gaps
- No measured sales-cycle or stage durations for MEP estimating software.

---

## H. Current alternatives and what does NOT satisfy them

### Takeaway
The real competitor is "stay on Accubid/ConEst/McCormick/QuoteSoft + Bluebeam and work overtime", followed by "hire" (slow) and "outsource overflow". Across the reviews retrieved, the most frequent unmet needs are price, support, bugs/performance, learning curve and database migration; AI-accuracy distrust is the dominant objection to the AI-native alternatives.

### Cited Findings
**Alternatives and their limits:**
| Alternative | Cost anchor | What fails | Source |
|---|---|---|---|
| Stay on Accubid (Classic/Anywhere) | "$3,000+/year per seat with annual maintenance" (2026 vendor-written review, unverified); older forum: ~$1,200/user license | Price, support delays, bugs in new version, DB rebuild, rigid assemblies, steep learning curve | [Capterra](https://www.capterra.com/p/193712/Trimble-Accubid-Anywhere/reviews/); price from result set ([BuildVision](https://www.buildvisionai.com/best-electrical-estimating-software) / [BestBid](https://bestbidestimating.com/?p=17643), page not resolved) |
| Stay on McCormick | Not published | "can be expensive"; SelectHub score 66/100 | [SelectHub](https://www.selecthub.com/p/construction-estimating-software/mccormick-estimating/) |
| Stay on ConEst | Not published | No review cons retrieved; forum migration rumor (XP→Vista DB rebuild) | [Mike Holt](https://forums.mikeholt.com/threads/accubid-vs-conest.140707/post-2201733) |
| PlanSwift / OST | $1,749–$3,000/seat/yr | Steep learning curve, document compatibility, glitches, licensing issues, slow support (Capterra summary); Windows desktop | [repo: planswift.md](../../geo-brain/03-market/competitors/planswift.md) |
| Bluebeam Revu (counts) | $260–$590/user/yr | Not an estimating tool; subscription model, complexity, lag on large files (summary) | [repo: bluebeam.md](../../geo-brain/03-market/competitors/bluebeam.md) |
| STACK | "as low as $249/user/month" | Annual price increases, bugs, freezing/crashes, slow on large takeoffs (G2 summary) | [repo: stack.md](../../geo-brain/03-market/competitors/stack.md) |
| Togal.AI | Growth $299/user/mo billed yearly; Business custom 4+ users | Accuracy drops on complex/low-quality drawings; limited PM integrations; pricing opacity (G2 summary) | [repo: competitor-landscape.md](../../geo-brain/03-market/competitor-landscape.md) |
| Beam AI (done-for-you) | ~$15–25K/yr per trade (ConstructConnect); claims ±1% of in-house accuracy | 1–4-day turnaround; not self-serve | [repo](../../geo-brain/03-market/competitor-landscape.md); [G2 discuss](https://www.g2.com/products/beam-ai/discuss) |
| Kreo | from $35/user/mo | Slowness with large files (G2 summary) | [repo: kreo.md](../../geo-brain/03-market/competitors/kreo.md) |
| Hire an estimator | $79,130 median; 12–18 months to productivity (vendor claim) | Slow, scarce, fixed cost regardless of bid volume | [BLS](https://www.bls.gov/ooh/Business-and-Financial/Cost-estimators.htm); [Provision](https://provision.com/blog/chief-estimator-bid-capacity-same-team-2026); [BBN Times](https://www.bbntimes.com/companies/why-labor-shortages-are-driving-contractors-toward-outsourced-estimating-services) |
| Outsource to estimating services | Quotr Service $0.25/sq ft <50k sq ft, $0.10 above; others unpublished | Quality varies; unclear pricing among firms | [repo: audiences-and-personas.md §10](../../geo-brain/00-quotr/audiences-and-personas.md) |
| Excel | — | (no ICP-specific evidence retrieved) | — |

### Inferences
**Unmet needs ranked by frequency in the retrieved evidence (desk tally of distinct sources, small n, not a survey):**
| Rank | Unmet need | Sources mentioning | Quotr's current answer (repo) |
|---|---|---|---|
| 1 | Price / per-seat cost and annual increases | Accubid (×2), McCormick, STACK, PlanSwift, Bluebeam → 6 | Transparent per-seat price; Lite $79.90 — **strong** |
| 2 | Bugs, freezing, slowness on large sets | Accubid, STACK, Kreo, Bluebeam, PlanSwift → 5 | No public performance evidence — **gap** |
| 3 | Support/vendor responsiveness | Accubid (×2), PlanSwift → 3 | Enterprise success manager, on-site onboarding — **claimable** |
| 4 | Learning curve / training cost | Accubid (×2), PlanSwift, Bluebeam → 4 | Plus includes 2 h guided onboarding — **partial** |
| 5 | Database/labor-unit migration ("rebuild the DB") | Accubid, ConEst rumor → 2 (high severity) | "Custom database"; import path from Accubid/ConEst **not documented — TO CONFIRM** |
| 6 | AI accuracy on complex/low-quality drawings | Togal G2, r/estimators, Dodge 57% → 3 | Self-reported 95–99% vector / 80–88% scans, no method page — **gap** |
| 7 | Assemblies flexibility | Accubid → 1 | Quotr DB has "labor, and assembly rates"; flexibility unproven — **TO CONFIRM** |
| 8 | Integrations (PM, accounting, incumbent estimating) | Togal → 1; Trimble's own APIs as baseline | No named integrations; Excel export unclear — **gap** |
| 9 | Security/data control | Dodge 54%; Autodesk trust −14 → 2 | "industry-standard encryption" only; no SOC 2 statement — **gap** |

- Structural insight: MEP incumbents' moat is the **labor-unit database** (items, assemblies, labor units built over years), not takeoff. AI-native tools (Togal, Beam, Kreo) attack takeoff; none in the evidence claims to replace an MEP labor-unit database. Quotr's most credible MEP position is therefore **"AI counts and measurements that feed the estimate you already trust"** until migration/import is proven.
- No labor-database integration (NECA/MCAA-style labor units) appears in any AI-native competitor's evidence retrieved (inference from absence; verify).

### Gaps
- 1–3-star reviews for ConEst, McCormick, QuoteSoft/FastPipe, Trimble Estimation MEP, OST and Beam AI could not be mined (search exhausted; Capterra/G2 blocked).
- No published pricing for ConEst, McCormick, Trimble Estimation MEP or Accubid confirmed from vendor pages.

---

## I. Willingness to pay, budget owner, procurement, security

### Takeaway
Per-seat price is not the barrier (incumbents already cost ~$1,750–$3,000+/seat/yr and an estimator costs ~$79k); the barriers are proof of accuracy, migration risk and IT/security sign-off. Quotr's Plus tier ($3,598.80/seat/yr) sits at Togal's price and inside incumbents' range; its missing security and integration documentation is the procurement blocker.

### Cited Findings
- Price anchors: PlanSwift ~$1,749–$3,000/seat/yr; Bluebeam ~$260–$590/user/yr; Togal $299/user/mo billed yearly; STACK $249/user/mo; Beam done-for-you ~$15–25K/yr per trade; Accubid "$3,000+/yr" (unverified) — sources in F and H.
- Capterra construction buyers' expected spend **$1,600–$4,000/yr**; pricing and ease of use dominate selection — [Capterra](https://www.capterra.com/resources/construction-software-buyer-insight/) (repo note).
- McCormick sells hosted floating licenses vs on-prem named licenses as a cost lever — [AccessNewswire](https://www.accessnewswire.com/newsroom/en/computers-technology-and-internet/mccormick-breaks-down-cloud-vs.-on-premises-estimating-software-f-1194167).
- Security is the #2 AI concern (54%) — [Construction Dive / Dodge-CMiC](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/) (repo note).
- Quotr: no security page, SOC 2 statement or data-retention policy found; integrations unnamed; whether drawings train models TO CONFIRM — [repo: product-and-features.md §3.7, §5](../../geo-brain/00-quotr/product-and-features.md).
- AI adoption among commercial specialty contractors: **24%** use AI for cost estimation, **22%** for bid management; **38%** report measurable impact (ServiceTitan, 1,000+ leaders, Mar 2026) — [ServiceTitan](https://www.servicetitan.com/press/servicetitan-report-finds-ai-adoption-more-than-doubles-among-commercial) (repo note).

### Inferences
| Item | Likely answer (label) |
|---|---|
| Budget owner | Owner/president (approval); CFO/controller (payback); CE controls the requirement and evaluation (likely) |
| WTP ceiling per seat | ~$3,000–$4,000/seat/yr is normal for MEP estimating (anchors above); Plus fits. Enterprise pricing should be framed per team, against one estimator salary (inference) |
| Payback framing | "Fewer than one hire": 10 Plus seats ≈ 45% of one median estimator's base pay (derived) |
| Procurement steps (speculative) | Demo → past-bid side-by-side → security questionnaire (IT/MSP) → reference call with same-trade sub → 30–90-day paid pilot on 1–2 seats → annual contract |
| Sales cycle (speculative) | 2–6 months; compressed to weeks when a hard date (Bluebeam Dec 31) or a resignation is the trigger |
| Pilot expectation (likely) | Re-run a recently bid job with a known answer; compare counts, linear footage and labor hours to the submitted estimate; measure hours saved |
| Security/IT must-haves (likely) | SOC 2 Type II or roadmap, SSO/SAML, role-based access, data ownership and deletion, explicit "no training on your drawings without consent", US data residency, export of all data on exit |
| Service line fit | Quotr Service as overflow insurance during a pilot: e.g., a 40,000 sq ft medical office at $0.25 = $10,000; whether >50k projects are billed at a flat $0.10 or tiered is ambiguous in the given pricing — TO CONFIRM before publishing examples |

### Gaps
- No primary data on MEP subs' software procurement process, sales-cycle length or security questionnaires.
- Quotr's security posture, integrations and annual pricing are unknown (TO CONFIRM with Quotr).

---

## J. Vocabulary list

### Takeaway
Content must use the trade's own nouns (labor units, assemblies, bid leveling, alternates, scope letters, CSI divisions) or engines will not match it to this persona's fan-out sub-queries. Definitions below are domain knowledge unless a source is shown; verify before publishing.

### Cited Findings
- Labor units (hours per device or per foot) and assemblies (priced group of items, e.g., "receptacle with box, wire and labour") — [repo: buyer-questions-by-trade.md](../../geo-brain/04-prompt-library/buyer-questions-by-trade.md); labor unit/production rate defined in [repo glossary](../../geo-brain/04-prompt-library/construction-glossary.md).
- Incumbent vocabulary visible in sources: "items and assemblies", "databases" (Mike Holt), "managed pricing services", "graphical takeoff", "ICT contractors" (Trimble), "change order tracking" (McCormick), "floating vs named licensing" (McCormick), "Division 23" (Provision).

### Inferences
| Cluster | Terms (use verbatim in page copy and H2s) |
|---|---|
| Labor | labor units, NECA Manual of Labor Units (MLU), MCAA labor units, labor factors/adjusters (height, congestion, difficulty), crew mix, man-hours, productivity, union vs open-shop rates, prevailing wage/Davis-Bacon |
| Database | items, assemblies, price updates/managed pricing (e.g., Trade Service pricing), material lists, quote requests, vendor quotes, extensions |
| Takeoff | device counts, fixture counts, linear footage, conduit/wire runs, feeders, branch circuits, home runs, ductwork by gauge/size, fittings, hangers, sprinkler heads, risers, curtain wall/storefront lites, mullions, sq ft of glazing |
| Bid process | bid day, invitation to bid (ITB), addenda, alternates, allowances, unit prices, inclusions/exclusions, scope letter, qualifications, bid leveling, plug number, hit rate/win rate, bid/no-bid |
| Specs | CSI MasterFormat Div 21 Fire Suppression, 22 Plumbing, 23 HVAC, 25 Integrated Automation, 26 Electrical, 27 Communications, 28 Electronic Safety & Security; Div 08 (08 40 00 entrances/storefronts/curtain walls) for glazing |
| Sectors | data center, mission critical, hyperscale, fab/cleanroom, healthcare, design-assist, design-build, hard bid, negotiated |
| Tools | Accubid Classic/Anywhere, LiveCount, ConEst IntelliBid/SureCount/CE Cloud, McCormick Design Estimating Pro, QuoteSoft/AutoBid/FastPipe/FastDuct, Trimble Estimation MEP, OST, PlanSwift, Bluebeam Revu 20/21 |

### Gaps
- NECA MLU and MCAA labor-unit naming/licensing terms not verified this session; check before claiming any compatibility.

---

## K. Channels

### Takeaway
This buyer asks peers in trade forums and subreddits, reads trade pubs that cover MEP software (ACHR News, Contractor, PHC News, Contracting Business), and attends trade-association events; member counts could not be retrieved. Trade pubs that covered Trimble's Accubid Anywhere launch are the proven PR route for MEP estimating software.

### Cited Findings
- Mike Holt forums host long-running "Accubid vs ConEst" and "best estimating software for commercial work" threads (2004–recent) — [Mike Holt](https://forums.mikeholt.com/threads/best-estimating-software-for-commercial-work.2590999/post-3046892).
- Trade press that covered the Accubid Anywhere launch: [PHC News](https://www.phcppros.com/articles/9906-trimble-announces-accubid-anywhere), [Contractor](https://www.contractormag.com/technology/article/20884126/trimble-announces-accubid-anywhere), [Contracting Business](https://www.contractingbusiness.com/technology/article/20871250/trimble-releases-accubid-anywhere), [ACHR News](https://www.achrnews.com/articles/151958-inside-trimble-s-new-accubid-anywhere-estimating-solution-for-mep-and-ict-contractors), [Engineering.com](https://www.engineering.com/trimble-adds-new-api-capabilities-to-accubid-anywhere-estimating-application/).
- McCormick syndicates press releases via AccessNewswire to [Yahoo Finance](https://finance.yahoo.com/technology/articles/mccormick-breaks-down-cloud-vs-151500658.html) and [PR-Inside](https://www.pr-inside.com/mccormick-breaks-down-cloud-vs-on-premises-estimating-software-for-r5204491.htm).
- Reddit threads relevant to this persona already logged in the repo: r/estimators "how do you estimate electrical", "electrical estimation", "anyone using AI for estimating", "AI in estimating"; r/HVAC; r/plumbers; ElectricianTalk; PlumbingZone; HVAC-Talk — [repo: prompt-library.md](../../geo-brain/04-prompt-library/prompt-library.md).
- Quotr has no trade-press coverage (Construction Dive, ENR, For Construction Pros) — [repo: offsite-presence.md](../../geo-brain/02-current-state/offsite-presence.md).
- Electrical Contractor magazine publishes an annual contractor profile — [EC Mag 2022 profile](https://www.ecmagdigital.com/ecmag/library/item/electrical_contractor_july_2022/4026964/).

### Inferences
| Channel | Role for this ICP | Priority |
|---|---|---|
| r/estimators, r/electricians, r/HVAC, r/Plumbing, r/Construction | Passive looking; Reddit feeds Google AIO/Perplexity citations | High (12-month, disclosed participation) |
| Mike Holt forums, ElectricianTalk, ContractorTalk, PlumbingZone, HVAC-Talk | Incumbent-tool debates; long-lived threads | High for electrical |
| Capterra/G2/Software Advice/GetApp compare pages | Appear for "X vs Y" and "X reviews" retrieval (see O) | High |
| Trade pubs: ACHR News, Contractor, PHC News, Contracting Business, EC&M, Electrical Contractor (NECA), ENR, Construction Dive, For Construction Pros | Considered-mode credibility; ChatGPT news-citation share rising (framework) | High |
| Associations/events: NECA convention, MCAA (incl. estimating/technology events), SMACNA, AFSA/NFSA (fire), NGA/glazing groups, ASPE chapters, IEC/ABC | Deciding-stage references; speaking slots | Medium |
| Vendor user groups (Trimble, ConEst, McCormick) | Where incumbents' users compare notes | Watch only |
| YouTube (side-by-side demos), LinkedIn (CE posts) | Proof and peer signal | Medium |

### Gaps
- Member counts for r/estimators, r/electricians, r/HVAC, r/Construction; LinkedIn group sizes; ASPE membership; 2026–2027 conference dates — not retrievable (reddit and gummysearch blocked; search budget exhausted).
- No podcast list verified.

---

## L. Proof required at each stage

### Takeaway
Each stage needs a different proof object; the deciding stage needs evidence Quotr does not yet publish (method-backed accuracy benchmark, same-trade quantified reference, security documentation, import/export proof).

### Cited Findings
- Togal publishes a "peer-reviewed" study vs On-Screen Takeoff and cites a 2025 Kansas University study on G2 — [repo: competitor-landscape.md](../../geo-brain/03-market/competitor-landscape.md); [G2 Togal discuss](https://www.g2.com/products/togal-ai/discuss). Beam claims ±1% of in-house accuracy — [G2 Beam discuss](https://www.g2.com/products/beam-ai/discuss).
- Quotr's accuracy claim is self-reported with no method page; RL Electric numbers appear only in a first-name homepage testimonial ("20 hours … 1–2 hours"), not on the case-study page — [repo: positioning-and-proof-points.md](../../geo-brain/00-quotr/positioning-and-proof-points.md).
- Dodge/CMiC: automated proposal generation rated **92%** effective by users (repo note) — [Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/).

### Inferences
| Stage | Proof that satisfies | Quotr has? |
|---|---|---|
| First thought | A credible framing of the problem with numbers (estimator cost, bid-capacity math) | Partly (ROI calculator; needs BLS citation) |
| Passive | Peer voices (forum/Reddit), a trade-specific demo video | Weak (RL Electric video only) |
| Active | Fair comparison tables vs incumbents (Accubid, ConEst, McCormick, QuoteSoft) and AI-natives; trade-specific symbol demos (electrical, mechanical, plumbing, fire, glazing) | No MEP incumbent comparisons |
| Deciding | Published accuracy benchmark with method by trade; same-trade reference with full name and numbers; security page/SOC 2 status; import/export proof (Excel, incumbent formats); pilot terms | No |
| Consuming | Onboarding plan, database setup tutorials, success manager | Partly (tutorials; Enterprise success manager) |

### Gaps
- No independent MEP-specific AI takeoff accuracy benchmark was found in this session.

---

## M. Coding chains (trigger → stage → mode → restraining force → exact prompt → proof)

### Takeaway
Seven chains cover the ICP; three are time-boxed and winnable now (Bluebeam EOL, resignation/capacity, overflow outsourcing), four are considered-mode decision chains that need proof assets first.

### Cited Findings
- Chain components are sourced in D–L; prompts below are **synthesized** (no captured prompts from this ICP exist yet).

### Inferences
| # | Trigger (datable) | Stage | Mode | Dominant restraining force | Exact prompt typed (synthesized) | Proof required |
|---|---|---|---|---|---|---|
| M1 | Bluebeam Revu 20 EOL Dec 31, 2026 | Active | Hot (deadline) | Habit ("we know Bluebeam") | "Our Bluebeam Revu 20 perpetual licenses lose Studio after Dec 31 — should my 6 mechanical estimators just buy Revu 21 or switch to an AI takeoff tool for counts?" | Dated EOL facts; cost table Revu 21 vs AI takeoff; "keep Bluebeam for markup, move counts" workflow |
| M2 | Senior estimator resigns mid-bid-season | First thought → active | Hot | Anxiety (AI misses scope) | "My senior electrical estimator quit and we have 4 data center bids due this month. Can AI takeoff cover the gap or should I outsource takeoffs?" | Turnaround time; same-trade case; done-for-you option with price |
| M3 | Data-center invites double; hit rate falls | Passive → active | Cold→hot | Habit (Accubid DB) | "We bid 30% more data center work this year with the same 5 estimators on Accubid and our hit rate dropped. What tools help estimators bid more without replacing Accubid?" | Coexistence workflow; hours-saved data; Accubid export/import proof |
| M4 | PlanSwift/OST renewal under subscription | Active | Cold | Anxiety (learning curve) | "PlanSwift alternatives for a glazing contractor measuring curtain wall and storefront — browser-based, with AI, under $3,000 per seat" | Glazing-specific demo; price table; trial |
| M5 | Owner asks CE to justify a new tool | Deciding | Cold | Anxiety (career risk) | "How do I build an ROI case for AI takeoff software for a 4-person estimating team vs hiring another estimator?" | BLS-cited cost model; calculator with method |
| M6 | IT/MSP security review | Deciding | Cold | Anxiety (data) | "Does Quotr.ai have SOC 2 and do they train AI on our drawings?" | Security page; data-use policy |
| M7 | Server/OS refresh retires on-prem McCormick/QuoteSoft install | Passive | Cold | Habit + migration anxiety | "We run McCormick on a local server that IT wants to retire — cloud estimating options for a plumbing and mechanical contractor and how hard is migration?" | Migration guide; data export path; timeline |

Promotion rule (framework synthesis): promote a chain to the content backlog when it recurs in ≥3 of 12 interviews or ≥5 of 50 community posts; currently all chains are hypotheses.

### Gaps
- Chains need validation through switch interviews with recent MEP buyers of Quotr (e.g., RL Electric) and lost deals.

---

## N. Prompt matrix

### Takeaway
Twelve full-context prompts carry trade, team size, metro and incumbent tool; six short category prompts and three brand prompts are kept in separate groups because brand prompts inflate mention rates. Demand tiers are labeled estimates from proxy density, not volumes.

### Cited Findings
- Comparative/"ask for a pick" prompts produce higher brand-recommendation rates (22.8% vs 8.0%) — [Momentic](https://momenticmarketing.com/blog/prompt-set-worth-tracking); fan-outs inject "best", "reviews", "2026", "vs", brand names — [PPC Land / Peec](https://ppc.land/what-chatgpt-actually-searches-for-5-million-fanout-queries-analyzed/); persona facts change brand lists — [Profound](https://www.tryprofound.com/blog/do-answer-engines-customize-responses-to-different-personas) (all via framework).
- Observed: for "best takeoff software for electrical contractors" (Perplexity, 2026-09-25) the answer named ConEst IntelliBid, Countfire, PlanSwift, Trimble AccuBid, McCormick; Quotr absent — [repo: quotr_ai_visibility_tests.md](<../Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>).

### Inferences
**Full-context first-person prompts (persona facts embedded; all synthesized):**
| ID | Prompt | Intent | Stage | Urgency | Mode | Engine | Expected fan-out nodes (speculative) | Demand tier (est.) |
|---|---|---|---|---|---|---|---|---|
| F1 | "I'm chief estimator at a 180-person electrical contractor in Northern Virginia. 5 estimators on Accubid Classic, data center invites doubled, a senior estimator just gave notice. Can AI takeoff count devices and conduit on data center drawings well enough to free up an estimator, and which tools work alongside Accubid?" | choose-provider | Active | Acute | Hot | ChatGPT | best AI takeoff electrical 2026; Accubid integration; AI takeoff accuracy electrical; Togal vs Beam; data center electrical estimating | 2 |
| F2 | "6 mechanical estimators in Phoenix on QuoteSoft and Bluebeam Revu 20. Revu 20 hits end of life Dec 31. Buy Revu 21 subscriptions or move counts to an AI takeoff tool that feeds our labor units?" | compare | Active | Acute (dated) | Hot | ChatGPT, Google AI Mode | Bluebeam Revu 20 end of life; Revu 21 price 2026; Bluebeam alternatives takeoff; QuoteSoft alternatives | 3 |
| F3 | "Plumbing contractor in Dallas, 90 employees, 3 estimators on FastPipe. Our hit rate fell from 1 in 6 to 1 in 10 and bid volume is up. What are mid-size plumbing subs using in 2026 to estimate faster?" | learn → pick | Passive | Recurring | Cold | ChatGPT | best plumbing estimating software 2026; Trimble Estimation reviews; AI takeoff plumbing fixtures | 2 |
| F4 | "Fire sprinkler contractor in Atlanta, 2 estimators counting heads and pipe in On-Screen Takeoff. Is there AI that counts sprinkler heads and measures branch lines from PDFs accurately?" | choose-provider | Active | Exploratory | Cold | Google AI Mode, ChatGPT | AI takeoff fire sprinkler; OST alternatives; sprinkler estimating software 2026 | 1 |
| F5 | "Curtain wall and storefront glazing sub in Columbus, 3 estimators in PlanSwift, now on annual subscription. Browser-based alternatives with AI for glazing takeoff under $3k/seat?" | compare | Active | Renewal | Cold | ChatGPT | PlanSwift alternatives 2026; glazing takeoff software; PlanSwift price 2026 | 2 |
| F6 | "Electrical sub, 45 bids a month, McCormick on a local server IT wants to retire. Cloud estimating options and how painful is migrating our database?" | compare/do | Passive | Event | Cold | ChatGPT, Copilot | McCormick cloud; McCormick alternatives; migrate estimating database | 2 |
| F7 | "Is it cheaper to hire another estimator at about $85k, outsource takeoffs, or buy AI takeoff for my 4-person electrical estimating team in Columbus?" | compare | Deciding | Event | Cold | ChatGPT | estimator salary Columbus BLS; outsourced takeoff cost per sq ft; AI takeoff pricing | 3 |
| F8 | "I own a $60M mechanical contractor. My chief estimator wants AI takeoff software. What should I ask about accuracy, data security and SOC 2 before we sign?" | validate | Deciding | Exploratory | Cold | ChatGPT, Copilot | AI takeoff accuracy; construction software SOC 2; vendor security questionnaire | 2 |
| F9 | "How do I run a fair side-by-side test of AI takeoff vs my estimators on a hospital job we already bid (electrical, 120 sheets)?" | do | Deciding | Exploratory | Cold | ChatGPT | AI takeoff accuracy test; benchmark method; Togal study | 1 |
| F10 | "How do I move 15 years of Accubid labor units and assemblies into a new estimating program without rebuilding everything?" | do | Deciding | Event | Cold | ChatGPT, Google | Accubid export database; Accubid alternatives import; ConEst migration | 2 |
| F11 | "Need overflow takeoffs for three hospital MEP bids in Atlanta due in 10 days — services that turn around in 3–5 days and price per sq ft?" | choose-provider | Active | Acute | Hot | Google AI Mode, Perplexity | MEP estimating services cost; outsourced takeoff turnaround; per sq ft | 3 |
| F12 | "Our 7-person electrical estimating team bids design-assist data center work in DFW. Which estimating software handles alternates, labor factors and bid leveling best for MEP in 2026?" | choose-provider | Active | Recurring | Cold | ChatGPT | best MEP estimating software 2026; Accubid vs ConEst vs McCormick; bid leveling | 2 |

**Short category prompts:** S1 "best electrical estimating software 2026" (tier 4) · S2 "Accubid alternatives" (tier 2) · S3 "AI takeoff for MEP contractors" (tier 2) · S4 "best mechanical estimating software for HVAC contractors" (tier 3) · S5 "On-Screen Takeoff alternatives" (tier 2) · S6 "MEP estimating services cost" (tier 3).

**Brand prompts (track separately):** B1 "Quotr.ai review for electrical contractors" · B2 "Quotr vs Togal for MEP takeoff" · B3 "Does Quotr work with Accubid or ConEst?"

Tier method (estimate): 1–5 from proxy density (forum/Reddit threads in repo and this session, presence of review-site compare pages, observed "best of 2026" vendor pages); no prompt volumes were measured.

### Gaps
- No GSC, Keyword Planner, Profound or Reddit API volume data; tiers are judgment.

---

## O. Simulation of the AI search journey

### Takeaway
(1) A simulated ChatGPT conversation shows the persona reaching a shortlist of incumbents + Togal/Beam/STACK without Quotr. (2) Nine research queries run today, used as retrieval proxies, show the evaluation layer is owned by review sites, forums, resellers and rival vendors' "review/alternatives" pages; Quotr surfaced in 1 of 9 (its own PlanSwift pricing post). (3) The biggest, most time-boxed gap is Bluebeam Revu 20 EOL content, already being harvested by competitors.

### Cited Findings
**(1) SIMULATED ChatGPT conversation — illustrative only, not a real engine output.** Persona: chief estimator, 160-person electrical sub, Northern Virginia, 5 estimators on Accubid Classic + Bluebeam Revu 20.

> **T1 (user):** "One of my senior estimators just gave notice and we have more data center bids than ever. I run a 5-person electrical estimating team on Accubid. What are my options?"
> **T1 (assistant, simulated):** Lists hire / outsource / productivity tools; suggests AI takeoff to cut counting time; asks about drawing types.
> **T2 (user):** "Do AI takeoff tools actually work on electrical drawings? I've heard they're hit-or-miss."
> **T2 (assistant, simulated):** Explains accuracy depends on vector vs scanned PDFs and symbol legends; names Togal.AI, Beam AI (done-for-you QA), STACK, and electrical-specific tools; recommends a pilot on a past bid.
> **T3 (user):** "I don't want to replace Accubid — our labor units are in there. What works alongside it?"
> **T3 (assistant, simulated):** Mentions Accubid's own takeoff (LiveCount), Bluebeam for counts, OST/PlanSwift; notes Trimble APIs; suggests exporting counts to Excel.
> **T4 (user):** "Also our Bluebeam Revu 20 licenses end Dec 31. Should we just renew?"
> **T4 (assistant, simulated):** Summarizes Revu 21 subscription pricing; offers alternatives such as Drawboard or STACK.
> **T5 (user):** "Give me a shortlist of three to demo next month with pricing."
> **T5 (assistant, simulated):** Shortlist: Togal.AI (~$299/user/mo), Beam AI (managed takeoff), STACK (from $249/user/mo); "stay on Accubid for estimating."

Grounding for the simulated brand set: Perplexity named ConEst, Countfire, PlanSwift, Trimble AccuBid, McCormick for electrical takeoff and Togal, STACK, PlanSwift, Beam AI for "best AI takeoff for subcontractors" — [repo: quotr_ai_visibility_tests.md](<../Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>). Quotr appeared in 1 of 32 unbranded prompts in that audit.

**(2) Retrieval proxy, not an AI engine answer — WebSearch runs on 2026-11-06 that match expected fan-out nodes:**
| # | Fan-out node (query as run) | Top domains returned | Brands named | Quotr appears? | Winning format |
|---|---|---|---|---|---|
| R1 | PlanSwift subscription / perpetual / price 2025 | vertigraph.com, fervorstudio.ca, **quotr.ai**, g2.com, easytakeoffs.com, struvia.co (×2), exayard.com | PlanSwift, Easy Takeoffs, Quotr (own post title), CoConstruct | **Yes (#3, own blog "Top 7 PlanSwift Alternatives for 2026")** | Dated "pricing 2026" explainers and "alternatives 2026" listicles |
| R2 | Bluebeam perpetual license end / Revu 21 transition | graitec.com, bluebeam.com, drawboard.com, licenseware, ncored.com (×4), brightergraphics.com, helonic.com, automatalabs.ca, support.bluebeam.com | Bluebeam, Drawboard (alt), ncored/Automata ("what to switch to") | No | Reseller FAQs + competitors' "Revu 20 EOL: what to switch to in 2026" pages |
| R3 | Accubid vs ConEst electrical estimating | forums.mikeholt.com (×10+), capterra.com compare, slashdot, bestbidestimating.com, buildvisionai.com, trustradius (ConWize vs Accubid) | Accubid, ConEst, ConWize, CostEstimator.com | No | Forum threads + review-site compare pages |
| R4 | Accubid reviews cons | capterra.com (×7 incl. regional), softwareadvice.com | Accubid Anywhere/Classic, STACK (compare) | No | Review directories |
| R5 | Trimble Accubid subscription / perpetual / Estimation MEP | trimble.com subdomains (×5), achrnews.com, zoftwarehub, sitechcs, cansel.ca, sketchucation | Accubid Anywhere | No | Vendor pages + trade press |
| R6 | ConEst acquired / IntelliBid | conest.com (×5), v2cloud.com, linkedin, **mccormicksys.com ("ConEst Review… Pros, Cons & Alternatives")**, itqlick.com | ConEst, Esticom/Procore, McCormick | No | Rival vendor's "X review/alternatives" page |
| R7 | McCormick cloud 2025–2026 | yahoo finance, accessnewswire, pr-inside, mccormicksys.com (×4 incl. "Best Electrical Estimating Software (2026 Guide)"), softwareadvice, selecthub | McCormick, Foundation | No | Syndicated press release + vendor self-published "best of 2026" |
| R8 | chief estimator can't hire / estimator shortage / bid volume | provision.com (×2), atreyus.ai, thetakeoff.ai, sketchdeck.ai, dancumberlandlabs.com, thebirmgroup.com, bbntimes.com, worldteams.com | Provision, Atreyus, TheTakeoff.ai (AI vendors) | No | AI-vendor thought leadership ("Chief Estimator's Guide… 2026") |
| R9 | AI takeoff accuracy MEP (reddit-targeted) | g2.com discuss (Beam, Togal, OST), cbinsights, businesswire (×4) | Beam AI (±1%), Togal (Kansas U. study), eTakeoff, Drawer AI | No | G2 discussion pages + press releases |

Not run (search budget exhausted; run these next as the dedicated fan-out battery): "best electrical estimating software 2026", "Accubid alternatives 2026", "AI takeoff MEP contractors", "best mechanical estimating software HVAC 2026", "QuoteSoft alternatives", "On-Screen Takeoff alternatives 2026", "MEP estimating services cost per square foot", "fire sprinkler estimating software", "curtain wall estimating software".

### Inferences
**(3) Gap verdict per prompt cluster:**
| Cluster | Who owns retrieval now | Quotr status | Winnability | Verdict |
|---|---|---|---|---|
| Vendor-event (Bluebeam Revu 20 EOL) | Resellers + Drawboard, ncored, Helonic, Automata | Absent | High, but closes after Dec 31 | **Act this week** (urgent page) |
| Vendor-event (PlanSwift subscription/pricing) | Pricing explainers; Quotr's post already retrieved | Present (fact source) | High | Refresh facts monthly; add MEP angle |
| Incumbent alternatives (Accubid/ConEst/McCormick/QuoteSoft) | Forums, Capterra compare, rival vendors' review pages | Absent | Medium-high (thin independent pool) | Build honest decision pages + get Capterra MEP reviews |
| Capacity/estimator shortage | AI-vendor blogs (Provision, Atreyus, TheTakeoff.ai) | Absent (Quotr's labor-shortage post not retrieved) | Medium | Out-evidence with BLS-cited cost model + original data |
| AI accuracy trust | G2 discussions, vendor study claims | Cited-not-named in prior P5 test | Medium | Publish method-backed MEP benchmark |
| Best electrical/MEP software (head) | Directories + incumbents' self-published guides | Absent (C6) | Low-medium | Listicle inclusion + reviews, not self-ranking |
| Security/procurement | Untested | Unknown | Medium | Publish security page (after facts confirmed) |

### Gaps
- No real ChatGPT, Google AI Mode or Copilot runs for this ICP; the planned fan-out battery was not run.

---

## P. GEO system for this ICP

### Takeaway
Build one MEP-estimating-team hub, six decision pages anchored on incumbents and the Bluebeam deadline, four answer pages that neutralize anxiety (accuracy, migration, security, cost of an estimator), and two proof assets (MEP accuracy benchmark; quantified RL Electric case). Off-site, prioritize Capterra/G2 MEP reviews, trade-press placement and forum participation over self-ranked listicles.

### Cited Findings
- Existing Quotr assets to upgrade rather than duplicate: [/software/trades/electrical/](https://quotr.ai/software/trades/electrical/), [best-electrical-estimating-software-2026](https://quotr.ai/blog/best-electrical-estimating-software-2026/) (stale pricing; not retrieved for C6), [mep-estimating-services](https://quotr.ai/blog/mep-estimating-services/), [hvac-estimating-services](https://quotr.ai/blog/hvac-estimating-services/), [data-center MEP post](https://quotr.ai/blog/data-center-construction-estimating-mep-subcontractor-choke-point/), [best-planswift-alternatives-2026](https://quotr.ai/blog/best-planswift-alternatives-2026/), [bluebeam-alternative](https://quotr.ai/blog/bluebeam-alternative/) (shows stale pricing), [is-ai-takeoff-actually-accurate-yet](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/) — [repo: prompt-library.md](../../geo-brain/04-prompt-library/prompt-library.md); [repo: bluebeam.md](../../geo-brain/03-market/competitors/bluebeam.md).
- Repo already flags "best MEP estimating software for subcontractors" (E-042) and "On-Screen Takeoff alternatives" (E-048) as NEW PAGE NEEDED — [prompt-library.md](../../geo-brain/04-prompt-library/prompt-library.md).
- Framework rules: one page per intent cluster; urgent vs considered page modes; no self-ranked listicles; refresh comparison/pricing monthly; skip llms.txt and schema-as-lever; measure as distributions — [uploaded framework](</root/.claude/uploads/0814826c-2913-57ec-9cf0-acc28e8d23b1/3fb5eb52-ICP_depth_framework_for_GEO.md>).

### Inferences
**Owned pages (titles and slugs; "U" = urgent mode, "C" = considered mode):**
| # | Type | Title | Slug | Mode | Answers chains |
|---|---|---|---|---|---|
| 1 | Hub | AI Takeoff for MEP Estimating Teams (2–10 Estimators): Electrical, Mechanical, Plumbing, Fire, Glazing | /mep-estimating-teams/ | C | M3, M5 |
| 2 | Decision (U) | Bluebeam Revu 20 End of Life (Dec 31, 2026): What MEP Estimators Should Do Before the Deadline | /guides/bluebeam-revu-20-end-of-life-estimators/ | U | M1 |
| 3 | Decision | Trimble Accubid Alternatives for Electrical and MEP Estimating Teams (2026) — including "keep Accubid, add AI counts" | /compare/accubid-alternatives/ | C | M3, M10-type |
| 4 | Decision | ConEst IntelliBid vs Accubid vs McCormick vs AI Takeoff: An Honest 2026 Comparison for Electrical Contractors | /compare/conest-vs-accubid-vs-mccormick/ | C | F12 |
| 5 | Decision | QuoteSoft / Trimble Estimation MEP Alternatives for Mechanical and Plumbing Contractors | /compare/trimble-estimation-mep-alternatives/ | C | F2, F3 |
| 6 | Decision | On-Screen Takeoff Alternatives (2026) for Commercial Subcontractors | /compare/on-screen-takeoff-alternatives/ | C | F4 |
| 7 | Decision (U) | Lost an Estimator Mid-Bid-Season? 3 Ways to Cover the Gap This Week (Overflow Takeoffs, AI Counts, Temp Hire) | /guides/estimator-quit-cover-bids/ | U | M2, F11 |
| 8 | Answer | What an Estimator Really Costs in 2026 (BLS) vs AI Takeoff Seats vs Outsourcing — with Calculator Method | /guides/cost-of-an-estimator-vs-ai-takeoff/ | C | M5, F7 |
| 9 | Answer | How Accurate Is AI Takeoff on Electrical and Mechanical Drawings? Method and Results by Trade | /benchmarks/ai-takeoff-accuracy-mep/ | C | F9, M6-adjacent |
| 10 | Answer / migration | Moving Off Desktop Estimating: How to Keep Your Labor Units and Assemblies (Accubid, ConEst, McCormick, QuoteSoft) | /guides/migrate-estimating-database-labor-units/ | C | M7, F10 (publish only what Quotr can actually import/export — TO CONFIRM) |
| 11 | Answer | Security and Data Handling for Estimating Teams: SOC 2 Status, Data Ownership, Model Training | /security/ | C | M6, F8 (facts TO CONFIRM) |
| 12 | Answer | Data Center MEP Estimating: Takeoff Volumes, Labor Factors and Bid Capacity (5-Metro Evidence Table) | upgrade existing data-center post | C | F1, F12 |
| 13 | Trade spokes | Upgrade /software/trades/{electrical, hvac, plumbing, fire-protection, glazing}/ with trade-specific symbol demos, vocabulary from J, and links to 3–11 | existing slugs | C | All |

**Proof assets / original data (ranked):**
1. **MEP AI takeoff accuracy benchmark** — 5 public plan sets per trade (vector + scanned), counts/LF vs two human estimators, published error distribution and method; refresh twice a year. Highest leverage: anxiety is the strongest force and no independent MEP benchmark was found.
2. **Quantified RL Electric case study** — full name/title, before/after hours (20 → 1–2 per homepage testimonial), bids per month, any hit-rate change.
3. **"Estimating Capacity 2027" survey** of CEs (bids per estimator, hit rate, hours per takeoff, tools) — co-brand with a trade association or ASPE chapter if possible.
4. **MEP labor-rate and estimator-cost-by-metro page** from BLS + Quotr DB aggregates (if Quotr allows).

**Off-site placements ranked by leverage per hour (estimates):**
| Rank | Placement | Why | Effort |
|---|---|---|---|
| 1 | Capterra/G2 reviews from MEP customers (target 10+ electrical/mechanical) | Capterra compare pages surface for "Accubid vs" and "Accubid reviews" (R3, R4); Togal has no Capterra reviews (repo) | Low per review |
| 2 | Trade-press product/data story (ACHR News, Contractor, PHC News, Contracting Business, EC&M) with the benchmark | These outlets covered Accubid Anywhere; ChatGPT cites news increasingly (framework) | Medium |
| 3 | Disclosed participation in Mike Holt forums, ElectricianTalk, r/estimators | Forums dominate incumbent-comparison retrieval (R3) | 12-month habit |
| 4 | Independent "best electrical/MEP estimating software 2026" lists (Software Advice, GetApp, ConstructionCoverage, BuildOps) | Cited in C6 | Medium; 2–6 weeks |
| 5 | YouTube: side-by-side "AI vs estimator on a real electrical set" (chaptered, long-form) | Proof for passive/deciding stages; AIO cites YouTube | Medium |
| 6 | Syndicated press release for the benchmark (wire → Yahoo Finance) | McCormick uses this route (R7) | Low |
| 7 | ASPE chapter/NECA/MCAA session talk | Deciding-stage references | High |

**Refresh cadence:** Bluebeam EOL page weekly until Jan 15, 2027, then convert to "after EOL" page; comparison and pricing pages monthly; benchmark semi-annually; hub and trade spokes quarterly.

**Tracking prompts to freeze (≥4 weeks; run 3–5×, ChatGPT + Google AI Mode, Perplexity optional; report cluster-level mention/citation/recommendation rates with ± ranges):**
1. "best electrical estimating software 2026" (S1)
2. "Accubid alternatives" (S2)
3. F2 (Bluebeam Revu 20 EOL, mechanical, Phoenix)
4. F1 (electrical, NoVA, Accubid, data centers)
5. "AI takeoff for MEP contractors" (S3)
6. "MEP estimating services cost" (S6)
7. F7 (hire vs outsource vs AI, Columbus)
8. B3 "Does Quotr work with Accubid or ConEst?" (brand group)

**Do / skip / ignore:**
- **Do:** Bluebeam EOL page now; Accubid/ConEst/McCormick/QuoteSoft decision pages written as fair conditional recommendations ("stay if…, add AI counts if…, switch if…"); BLS-cited cost-of-estimator page; MEP benchmark; Capterra/G2 MEP reviews; confirm and publish security, integrations and import/export facts; fix stale pricing on existing posts; switch interviews with 6–12 MEP users (ask "what exactly did you type, and where").
- **Skip:** self-ranked "best MEP estimating software" listicle with Quotr #1; 50-state or city pages; claims of Accubid/NECA labor-unit compatibility before verified; llms.txt; schema as a citation lever; paid listicle placements before baseline.
- **Ignore:** generic "thousands of contractors trust us" social proof; single-run "AI rank" dashboards; Claude/Grok tracking for this ICP (Copilot optional if IT-sanctioned use is confirmed).

### Gaps
- Quotr's actual MEP capabilities (labor-unit import, assemblies flexibility, Excel/incumbent export, integrations, SOC 2) are unknown and gate pages 3, 10 and 11.

---

## Q. Known / likely / speculative

### Takeaway
Hard facts are the wage anchor, the Bluebeam dates, PlanSwift's subscription model, incumbent ownership and the review complaints; the firm count, geography ranking, timelines and prompt demand are estimates.

### Cited Findings
- See sections A–P for each source.

### Inferences
| Claim class | Known (cite) | Likely (label) | Speculative (validate) |
|---|---|---|---|
| Size & value anchor | Estimator median $77,070; specialty trades $79,130; p90 >$128,640 (BLS May 2024); 2022 SUSB published | Electrical 79,611 employer firms, 89.7% <20 employees (secondary) | ~6,000–9,500 ICP firms; ~25–38k estimator seats |
| Vendor triggers | Bluebeam perpetual sales ended Sep 30, 2023; Revu 20 support end Jul 31, 2026; EOL Dec 31, 2026; Revu 21 subscription-only; Accubid Anywhere 2019; McCormick in Foundation portfolio, Jul 2026 cloud release; ConEst in JDM | PlanSwift subscription-only for new buyers since 2025 at ~$1,749–$3,000/seat/yr; June 2026 sign-in change | Any Accubid Classic/Trimble Estimation sunset; 2026 price increases |
| Forces | Accubid Capterra 3.7/69 with support, price, bug, DB-rebuild, assemblies complaints; "they both do basically the same thing" (forum) | Anxiety (accuracy, migration, security) outweighs pull for this ICP | Time-of-day hot moments; resignation seasonality |
| Market/AI | AGC/Sage 23%, ServiceTitan 24% AI in estimating; Dodge 57% accuracy / 54% security concerns (repo notes, not re-checked) | Data centers drive MEP bid volume (AGC headline) | Five metro ranking; fab timing |
| GEO | Quotr absent for electrical takeoff (C6); retrieval for incumbent clusters owned by forums, review sites, rival vendors (R1–R9) | Bluebeam-EOL and incumbent-alternatives clusters are the cheapest wins | Specific citation lift timelines; demand tiers |
| Quotr facts | Prices, Service rates, 7-day trial, RL Electric testimonial, no SOC 2 statement found (repo) | Coexistence positioning ("add AI counts to Accubid") fits best today | Import of incumbent databases; integrations; Enterprise deal size |

### Gaps
- Re-run when network access allows: SUSB/CBP size classes, BLS OEWS industry/MSA rows, Capterra/G2 1–3-star reviews for ConEst, McCormick, Trimble Estimation, OST, Beam; Reddit member counts and threads; the dedicated fan-out battery; Trimble/ConstructConnect official notices for 2025–2026.
