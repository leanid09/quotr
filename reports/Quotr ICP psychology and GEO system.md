# Build Quotr's GEO From Ten Buyers' Triggers

Quotr should build its AI-search presence for four buyers first: **small developers who need a feasibility estimate, small MEP owner-estimators, finish-trade subcontractors, and residential builders and remodelers**. It should run time-boxed bets on **LA fire-rebuild buyers** and **finish-material importers**, let **mid-size MEP chief estimators** ride the MEP assets, and give **commercial GC precon teams, construction lenders and architects** one or two pages each until Quotr confirms the facts those buyers demand. The case rests on three findings. First, Quotr surfaced in **4 of 93 retrieval-proxy searches** run for the ten ICPs, and never as a third-party recommendation, yet it is already the **first (unnamed) citation** for outsourced-estimating price. Second, the answer pools for developer local costs, LA rebuild costs, all-layer finish tariffs and lender review prices are thin, stale or empty. Third, **anxiety, not missing information, is the dominant restraining force for 7 of 10 ICPs**, and habit (a "free" GC number, one $/sq ft figure, Excel or a PM suite) dominates the other three. Quotr's current content answers mostly the pull force, so the system has to be built from proof: accuracy method, cancel and export terms, lender format, compliance documents. Timing sharpens the order. Bluebeam Revu 20 dies on **December 31, 2026**, Section 232 cabinet and vanity tariffs step from **25% to 50% on January 1, 2027**, Opportunity Zone 2.0 maps go live the same day, and the LA fires' second anniversary and 24-month living-expense mark land on **January 7, 2027**. Nothing ships credibly until Quotr settles a service turnaround it currently states **seven different ways** and explains a **$0.25/$0.10 per sq ft price tier that can make a 49,000 sq ft job cost $7,250 more than a 50,000 sq ft one**. One limitation governs every number below. All researchers hit a shared web-search cap and blocked page fetches, so most evidence comes from search snippets, no ChatGPT or Google AI Mode runs were possible, and every AI conversation in this report is a simulation.

*ICP codes used throughout: ICP1 small MEP owner-estimator · ICP2 mid-size specialty-sub chief estimator · ICP3 area/finish-trade sub · ICP4 commercial GC precon · ICP5 residential builder/remodeler · ICP6 small developer (feasibility) · ICP7 disaster-rebuild buyer (LA first) · ICP8 lender, debt fund or cost reviewer · ICP9 finish-materials importer · ICP10 architect needing design-stage costing.*

## Every number here is a lead from search snippets, not a verified page

The research ran on 2026-11-06 under hard network limits, and the operator should read the evidence accordingly. The web-search budget was **200 calls per turn shared by all parallel researchers**, and it ran out early: the geography researcher got 9 queries, the small-MEP researcher 17, the LA-rebuild researcher about 31 and the trigger-calendar researcher 35. Page fetches failed for census.gov, bls.gov, capterra.com, g2.com, reddit.com, nahb.org, agc.org, ncarb.org and others. As a result, **every verbatim quote is verbatim as returned in a search-result snippet; the page itself was not opened**. Reddit verbatims are missing for most ICPs. Census County Business Patterns and BLS occupational tables by state and metro were never pulled, so ICP sizes are labeled estimates and the metro index is ordinal judgment. Tariff facts come from search summaries of Federal Register notices and law-firm alerts, and 2027 trade-show dates are unverified.

On the engine side, **no ChatGPT, Google AI Overviews, AI Mode, Gemini or Copilot answer was captured**. The only real engine measurements remain Quotr's September 2026 Perplexity baseline, in which Quotr was named in 1 of 32 unbranded prompts. The "retrieval proxies" in this report are ordinary web searches that stand in for the sub-queries an engine would fan out to. They show who owns a node, not what an engine would say.

The report labels claims three ways. **Known** means measured by a cited source. **Likely** means a strong inference, to be labeled when published. **Speculative** means a hypothesis to validate first. The geography layer needs about 6–10 hours with census.gov and bls.gov unblocked. The psychology layer needs 6–12 switch interviews per priority ICP, each asking "what exactly did you type, and into what?" The engine layer needs real ChatGPT and AI Mode baselines. Until those exist, use these findings to choose what to test and build, not as figures to quote publicly.

## Four buyers earn the first build; six get bets, riders or a single page

The ranking below scores each ICP on five factors, each from 1 to 5. **Value** (weight 0.20) is pool size times willingness to pay. **Fit** (0.25) is how well a Quotr product serves the buyer today. **Winnability** (0.25) is how thin or conflicted the current answer pool is, and whether Quotr already has unique data or retrieved pages. **Urgency** (0.15) is datable triggers inside the next 90 days. **Readiness** (0.15) is the inverse of blocking Quotr facts. The scores are my judgment from the notes, not a validated model. A sensitivity check that drops urgency entirely leaves the same top four (ICP1 and ICP3 swap places), so the Tier 1 call does not depend on the calendar.

| Rank | ICP | Value | Fit | Win | Urgency | Ready | Score | Tier and role | Lead product |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ICP6 small developer | 4 | 5 | 5 | 3 | 3 | **4.20** | Tier 1: build now | Service |
| 2 | ICP1 small MEP owner-estimator | 4 | 5 | 3 | 5 | 4 | **4.15** | Tier 1: build now | Software |
| 3 | ICP3 finish-trade sub | 4 | 4 | 4 | 3 | 4 | **3.85** | Tier 1: build now | Software |
| 4 | ICP5 residential builder/remodeler | 5 | 4 | 3 | 4 | 3 | **3.80** | Tier 1: build now | Software, Service, Procurement |
| 5 | ICP7 LA rebuild | 2 | 3 | 5 | 5 | 2 | 3.45 | Tier 2: bounded bet, 40–60 h, Dec–Mar | Service (data asset) |
| 6 | ICP9 finish importer | 4 | 3 | 4 | 5 | 1 | 3.45 | Tier 2: explainer now, claims gated | Procurement |
| 7 | ICP2 mid-size MEP chief estimator | 4 | 3 | 3 | 4 | 2 | 3.20 | Tier 2: rides ICP1 assets | Software |
| 8 | ICP4 commercial GC precon | 4 | 3 | 3 | 2 | 2 | 2.90 | Tier 3: one SD-budget page | Service |
| 9 | ICP8 lender/cost reviewer | 3 | 2 | 4 | 2 | 1 | 2.55 | Tier 3: one price-and-SLA page | Service |
| 10 | ICP10 architect | 2 | 2 | 3 | 2 | 2 | 2.25 | Tier 3: entity fixes plus two pages | Service |

**Small developers rank first** because they are the one ICP where Quotr is already inside the retrieval set and the fix is grammatical. Perplexity used Quotr's outsourcing post as its first source for outsourced-estimating price and credited the $0.25 rate to "one outsourced estimating service" ([Quotr blog](https://quotr.ai/blog/outsource-construction-estimating/)). The price is trivial against the buyer's risk, the local-cost pool is stale forum threads and generic calculators, and Quotr holds Bay Area cost data no rival has.

**The two trade-sub ICPs (1 and 3) are the software core.** Lite at $79.90 a seat a month undercuts every paid incumbent, RL Electric gives MEP proof, and the formats that win their prompts are known and cheap: directory reviews, third-party lists, trade calculators.

**Residential builders rank fourth, not first.** They are the largest pool and the gap the prior audit flagged, but Handoff and Buildxact own the head terms. Quotr should attack the uncontested sub-clusters, "keep your PM suite, add takeoff" and time-per-estimate, before it fights for "best residential estimating software."

The middle tier is defined by time and gates. **The LA rebuild bet is worth about 40–60 hours between December and March** because more than 90% of destroyed homes are unbuilt and no independent cost dataset exists. But the homeowner claim lane is crowded and legally sensitive, so the bet leads with a cost tracker, builders and materials. **The importer ICP has the strongest demand-side triggers in the set**, with tariff events roughly every six weeks. However, China-wide antidumping rates make some of Quotr's likely categories uncompetitive, so tariff explainers can ship now while savings and "duty-paid" claims wait for customs-broker review. **Mid-size MEP chief estimators** share the Revu 20 deadline and the accuracy benchmark with ICP1, but their decision pages need security, integration and labor-unit-import facts Quotr has not published.

The bottom tier is honest about fit. GC precon buyers want accuracy against final cost, which Quotr has never published. Lenders need independence, credentials and liability cover that Quotr Service, sold to borrowers, does not have. The architect researcher's own verdict was "secondary (Tier 3)," given a contracting design market, an identity barrier and unconfirmed Revit status.

Across all ten ICPs, the operator should skip five things. Skip **self-ranked "best X" lists**: 69% of cited self-promotional listicles did not get their own brand recommended ([Something Inc.](https://somethinginc.com/blog/2026-ai-citation-data-review/)). Skip **city-templated pages**, which Google's scaled-content policy targets ([Google](https://developers.google.com/search/docs/essentials/spam-policies)). Skip **schema and llms.txt as citation levers**, **Reddit as a ChatGPT citation bet** (Reddit's share of ChatGPT citations fell from 3.83% to 0.52% in August 2026 ([Axios](https://www.axios.com/2026/08/20/chatgpt-reddit-citations-geo-strategy))), and **generic "thousands of contractors" social proof**. Generic social proof was the smallest nudge effect in 126 field RCTs ([DellaVigna & Linos](https://www.nber.org/system/files/working_papers/w27594/w27594.pdf)), and Quotr has no review base to back it.

## Ten buyers, ten trigger chains: who they are and what fails them

The table compresses each ICP's coding chain into its most decision-relevant links. After it, each ICP gets a short dossier that adds its evidence, a verbatim, and what Quotr should build. Hot moments are inferred from deadlines and community timing. Validate them against Quotr's own trial and form timestamps, which are the cheapest hard evidence available.

| ICP | Size anchor (label) | Priority geography | Sharpest datable trigger | Hot moment | Dominant restraining force | Where they ask | What current options fail to do |
|---|---|---|---|---|---|---|---|
| 1 Small MEP owner-estimator | 25k–45k plan-bidding firms (speculative) | Houston, DFW, Phoenix; one CA page; one data-center page | Revu 20 end of life, Dec 31, 2026 | Weeknight 9 pm–1 am before bid day | Anxiety (AI miss, lock-in, price hikes) | Mike Holt, Electrician Talk, r/estimators, Capterra | Fair price for irregular use; no lock-in; trustworthy counts on flattened PDFs |
| 2 Mid-size chief estimator | 6k–9.5k firms (speculative) | Data-center corridor: NoVA, Phoenix, DFW, Atlanta, Columbus | Revu 20 EOL; estimator resigns | Bid-season week an estimator quits | Anxiety (accuracy, DB migration, security) plus habit | Trade forums, ACHR News, associations | Keep the labor-unit database; stable on large sets; security documentation |
| 3 Finish-trade sub | Roofing 25,519 and drywall 20,760 establishments (known via aggregators) | Texas Triangle, Florida I-4, Atlanta/Carolinas, Phoenix, SoCal | Spring bid season; renewal; LVP/tile price spikes | Night before a GC bid | Anxiety about trade quirks, plus habit | ContractorTalk, DrywallTalk, trade subreddits, YouTube | Trade unit math (rolls, squares, wall types); no crashes on big sets; affordable seats |
| 4 Commercial GC precon | 4k–7k firms (estimate) | Houston, DFW, LA, NYC, Phoenix, NoVA | Owner asks Friday for an SD budget by Monday | Friday afternoon; bid day | Anxiety (explainability, security) plus habit (Excel, Procore) | Peers, associations, trade media, LinkedIn | Defensible conceptual number from incomplete drawings; bid leveling |
| 5 Residential builder/remodeler | ~60k single-family GC plus >100k remodeling establishments (likely) | Bay Area and LA first; Texas; Carolinas/Atlanta | Money-losing job; PM-suite price hike; Jan 1 cabinet tariff | Evening after a site visit | Habit (Excel, gut $/sq ft, PM suite) | ContractorTalk, JLC, Fine Homebuilding, Facebook groups | Plan takeoff without paywalls; estimating that is not buried in a PM suite |
| 6 Small developer | LLC sponsors invisible to NAICS (likely) | Bay Area, LA, Austin/DFW, Seattle–Portland | LOI feasibility clock; lender asks for a budget | Feasibility window; lender deadline | Habit (one $/sq ft, GC's free number) plus lender anxiety | BiggerPockets, r/RealEstateDevelopment | Local, current, product-specific cost; independence from the GC; lender format |
| 7 LA rebuild | ~11,400 homes destroyed, >90% unbuilt (known) | Altadena, Palisades, Malibu | Jan 7, 2027 anniversary and 24-month ALE mark | Bid shock; settlement letter | Anxiety (fraud, lowball) plus habit (insurer's number) | Local news, nonprofits, recovery centers | Independent, dated, line-item cost reference |
| 8 Lender/cost reviewer | $453.5B bank C&D book (known) | California private lenders; national otherwise | Thin budget before credit committee | Committee week; draw overrun | Anxiety (defensibility, examiner) plus habit (PCR firm, GC contract) | Scotsman Guide, AAPL, CMA, BiggerPockets | Published price; days not weeks; budget-to-scope reconciliation |
| 9 Finish importer | Not sized | Bay Area, LA, Inland Empire | Jan 1 cabinet 50%; Jan 10 truce expiry | Dealer quote 20% over budget | Anxiety (scams, spec/code, moving landed cost) | YouTube, supplier blogs, trade press | One accountable, dated, delivered price with compliance documents |
| 10 Architect | 19,000+ firms, ~75% under 10 staff (known) | California only, until local data exists | Bid opening over budget | Bid opening | Habit (GC's free number) plus liability anxiety | Archinect, AIA chapters, trade press | Independent number at SD/DD without a costly consultant |

### Small MEP owner-estimators fear a wrong count more than a $79.90 bill

The first ICP is the owner of a 3–30-person electrical, plumbing, HVAC, low-voltage or fire-alarm sub who still does the takeoffs. The 2023 County Business Patterns, as reported by aggregators, count **83,342 electrical and 111,207 plumbing/HVAC employer establishments**, averaging about 11–12 employees ([StartBusinessByState](https://startbusinessbystate.com/electrician-industry-statistics/); [StartBusinessByState HVAC](https://startbusinessbystate.com/hvac-industry-statistics/)). Excluding service-only shops leaves a labeled estimate of **25,000–45,000 plan-bidding firms**. The owner is a licensed tradesperson who treats estimating as paperwork that pays and decides alone or with a spouse who runs the books. He searches hot in the one to three nights before a bid.

**Anxiety carried 7 of 17 verbatims.** A STACK reviewer wrote that the vendor "jacked the price up 50% after the first year" and then "locked us out of all our estimates and held it for ransom" ([Capterra](https://www.capterra.com/p/147181/STACK-Takeoff/reviews/)). An industry article warns that when "the legend and the fixture schedule disagree, the software picks one" ([AI Insights News](https://aiinsightsnews.net/audit-ai-electrical-estimate/)). Habit is the cheap legacy tool plus Bluebeam's count tool and Excel: "I just can't see spending $1500 plus when you can get this software for about $30" ([Mike Holt forum](https://forums.mikeholt.com/threads/electrical-estimating-software.49959/latest)).

The sharpest datable trigger is **Bluebeam Revu 20's end of life on December 31, 2026**. On that date perpetual licenses lose Studio and API features, and open and enterprise licenses are deactivated ([Bluebeam](https://www.bluebeam.com/upgrade-from-revu-20/)). In the retrieval proxy, resellers and the rival Drawboard already own that sub-query. Recurring triggers are an estimator quitting, a run of lost bids, a missed-scope loss and STACK or PlanSwift renewal notices.

A tally of 22 complaint snippets ranks the unmet needs (directional only):

| Unmet need | Snippets |
|---|---|
| Price that fits an irregular user | 6 |
| Vendor behavior on price hikes, billing and lock-in | 6 |
| Tool friction | 3 |
| PDF and AI accuracy | 3 |
| Stability | 2 |
| Trade depth | 2 |

Price is Quotr's strongest card. Lite costs **$958.80 a year**, below the $1,600–4,000 budget construction-software buyers expect ([Capterra](https://www.capterra.com/resources/construction-software-buyer-insight/)). The anchors it beats are STACK at $249–299 a month and PlanSwift at $1,749–3,000 a seat a year ([BuildOps](https://buildops.com/resources/electrical-estimating-software-cost)). RL Electric cut takeoff time from 20 hours to 1–2 hours ([video](https://www.youtube.com/watch?v=Y2_PUPVtVaE)). If that holds on four bids a month, an owner frees about 72 hours, worth roughly $2,600 at the estimator median wage (arithmetic).

Service is the misfit here. At $0.25 per sq ft, a 30,000 sq ft tenant improvement costs **$7,500 per bid**, which a sub with a low hit rate will not pay. This ICP needs a per-sheet or per-trade crunch-week price.

Quotr's single retrieval win for this ICP is telling. Its how-to post on [estimating electrical work from drawings](https://quotr.ai/blog/how-to-estimate-electrical-work-from-drawings-conduit-devices-labor/) ranked second for an AI-accuracy query. That makes an accuracy method page the conversion point. Quotr's self-reported 95–99% (vector) and 80–88% (scanned) accuracy figures ([Quotr blog](https://quotr.ai/blog/best-togal-ai-alternatives-2026/)) currently carry no published method.

### Mid-size MEP chief estimators guard a labor-unit database, not a takeoff

The second ICP runs a 2–10-person estimating team at a 50–499-employee mechanical, electrical, plumbing, fire-protection or glazing sub. That is roughly **6,000–9,500 firms**, an order-of-magnitude estimate. Their own labor cost is the anchor. The median cost estimator in specialty trades earned **$79,130 in May 2024** ([BLS](https://www.bls.gov/ooh/business-and-financial/cost-estimators.htm)), about 22 Quotr Plus seat-years. The chief estimator's status rests on owning the firm's labor units and assemblies, and a failed rollout during bid season is a visible career risk. So this buyer pilots on a past bid, defers to habit, and switches only when a dated push forces it.

Habit sounds like a forum member's verdict on Accubid and ConEst: "They both do basically the same thing" ([Mike Holt forum](https://forums.mikeholt.com/threads/accubid-vs-conest.140707/post-2201733)). Trimble Accubid Anywhere still draws complaints on Capterra about price, support, bugs and having to rebuild the database ([Capterra](https://www.capterra.com/p/193712/Trimble-Accubid-Anywhere/reviews/)).

The push comes from data centers, the one growth engine. AGC's 2026 outlook expected a weak year "apart from data centers and power projects" ([AGC](https://www.agc.org/news/2026/01/08/contractors-have-dampened-expectations-2026-apart-data-centers-and-power-projects-amid-worries-about)). Census data-center construction spending passed **$50.7B at an annual rate in April 2026** ([Bloomberg](https://www.bloomberg.com/news/articles/2026-06-01/us-construction-spending-on-data-centers-eclipses-50-billion)). The DC–Northern Virginia metro shows the scarcity: 3,780 cost estimators at a 0.84 location quotient and a $95,620 mean wage ([BLS](https://www.bls.gov/regions/mid-atlantic/news-release/occupationalemploymentandwages_washingtondc.htm)).

The structural insight is that **no AI-native competitor claims to replace an MEP labor-unit database**. Until import from Accubid, ConEst, McCormick or QuoteSoft is proven, Quotr's credible position is "AI counts that feed the estimate you already trust." The decision pages for this ICP stay gated on three facts Quotr has not published: security posture, named integrations, and a labor-unit import path.

### Finish-trade subs buy trade math and reviews, not AI claims

The third ICP spans drywall and metal framing, acoustical ceilings, flooring, tile, painting, roofing, siding, insulation and concrete flatwork. Roofing (**25,519 establishments**) and drywall/insulation (**20,760**) alone are tens of thousands of small employers ([NAICScodes.org](https://naicscodes.org/code/238160-roofing-contractors); [Vantage](https://vantainsights.com/industry/238310-drywall-insulation-contractors)). The field workforce is majority Hispanic: drywall installers 68.5–75.2% and painters 62.5% ([ENR/CPWR](https://digital.bnpmedia.com/article/SAFETY/4938139/841967/article.html); [EngiMarket](https://www.engimarket.com/blog/immigrant-workers-in-construction-statistics/)). Construction is the top sector for Hispanic-owned employer firms ([Census](https://census.gov/library/stories/2024/10/hispanic-owned-businesses.html)).

The push shows up in thread titles. One asks "Total squares for bid? How do you guys come up with your total?" ([ContractorTalk](https://www.contractortalk.com/threads/total-squares-for-bid-how-do-you-guys-come-up-with-your-total.37342/)). Another asks "$12/sheet of drywall install, is that good?" ([r/Construction](https://www.reddit.com/r/Construction/comments/x36v0a/12sheet_of_drywall_install_is_that_good/)). The anxiety is about each trade's quirks, not about AI in the abstract. MeasureSquare "sometimes tells you one less than you actually need" on sheet vinyl ([Software Advice](https://www.softwareadvice.com/construction/measuresquare-profile/reviews/)), and PlanSwift "freezes or crashes if too many drawings loaded" ([Capterra](https://www.capterra.com/p/70808/PlanSwift/reviews/)).

Aerial roof reports fail on new construction because there is no roof to fly yet ([Roofing Software Guide](https://roofingsoftwareguide.com/roundups/best-roofing-aerial-imagery-software/)). That leaves plan-based roofing takeoff as an open lane.

What wins this ICP's prompts is not AI messaging. In Quotr's September Perplexity test, the answer to "how to estimate drywall for a house" cited calculators, three of them from software vendors. Quotr's drywall trade page carried about 25 words of its own text ([Quotr](https://quotr.ai/software/trades/drywall/)).

Service at $0.25 per sq ft prices a 2,500 sq ft production house at $625. That works for overflow weeks, not routine bids. Procurement belongs only on flooring and tile pages aimed at subs who supply and install. Spanish is justified as a measured pilot (three pages, two videos and tracked prompts), not as a mirror of the whole site.

### Commercial GC precon buys accuracy against final cost

The fourth ICP is the preconstruction manager or chief estimator at a commercial GC between the SBA small-business line (about $45M in revenue) and the lower half of the ENR Top 400 (about $250M–$870M). That is roughly **4,000–7,000 firms** (estimate). Precon managers earn **$115K–$135K** base and chief estimators or VPs **$161K–$269K** ([TBG](https://thebirmgroup.com/preconstruction-manager-salary/); [TBG](https://thebirmgroup.com/2025-construction-estimator-salary-trends-a-deep-dive-into-senior-chief-estimator-pay/)), so software price is not the constraint. Status comes from being right early, because the first schematic-design (SD) number anchors the owner.

Three verbatims carry the forces:

| Force | Quote | Source |
|---|---|---|
| Push | "Drawings that are presented as 75 percent complete but actually lack such basic information as wall types are really just budget drawings masquerading as a bid set" | [AWCI](https://onlinedigeditions.com/article/Estimator%27s+Edge/2436297/295348/article.html) |
| Habit | "we still use Procore for project management, but we don't use it for estimating purposes" | [Capterra](https://www.capterra.com/p/157661/Esticom/reviews/?page=2) |
| Anxiety | "Because estimating is not quantity takeoff" | [ConstructConnect](https://www.constructconnect.com/blog/are-ai-takeoffs-accurate-in-2026) |

The hot moments are the Friday request for a Monday SD budget and bid day with thin sub coverage. The most frequent unmet needs in the evidence are conceptual estimates from incomplete SD and design-development (DD) sets (7 sources) and bid leveling with scope-gap detection (6). New AI entrants such as Belidor ($3.1M pre-seed) are crowding into leveling ([Dealroom](https://app.dealroom.co/companies/belidor)). Quotr was absent from all 11 retrieval proxies for this ICP.

The fit is Service, for the hot SD-budget chain. Everything else is blocked on four confirmations: GC-side sub-bid leveling, Procore and Autodesk integrations, SOC 2 status, and one turnaround.

### Residential builders are held by habit and the PM suite they already pay for

The median NAHB builder member started **5 homes in 2025** with 6 payroll employees and $3.7M in revenue ([NAHB](https://www.nahb.org/blog/2026/09/builder-member-census-median-revenue-flat)). Builders earn 20.7% gross and 8.7% net margins, and the bottom quartile loses money at −1.4% net ([NAHB](https://www.nahb.org/news-and-economics/press-releases/2025/04/nahbs-new-study-provides-statistics-and-data-on-builder-financial-performance)). A 5% estimating miss on direct costs therefore erases about half a year's profit (arithmetic). Only **33% of renovation GCs use estimating software** ([Houzz](https://st.hzcdn.com/static/econ/2025_US_Houzz_State_of_the_Industry.pdf)), and nearly half of remodelers spend more than 10 hours preparing a bid, mostly for free ([JLC](https://www.jlconline.com/business/reader-survey-on-competitive-bidding/)).

Habit is the strongest restraining force: Excel, a gut $/sq ft and the PM suite already paid for. The push is price shock and complexity inside those suites. Former users wrote that "the price of buildertrend was about to triple" and that "the estimate software is bad, and way too complicated" ([Capterra](https://capterra.com/p/218503/JobTread/reviews/)).

Residential rivals paywall plan takeoff:

| Rival | Where plan takeoff sits | Source |
|---|---|---|
| Handoff | Only on the Scale plan, **$719 a month billed annually**, for plans up to 5,000 sq ft | [Handoff](https://www.handoff.ai/pricing) |
| Buildxact | AI takeoff is a **$99-a-month add-on** | [Buildxact](https://www.buildxact.com/us/pricing/) |

That makes Quotr Lite the cheapest plan-takeoff option for one to three users (arithmetic). Service prices a 2,500 sq ft custom home estimate at $625.

The triggers are a money-losing job, a homeowner who wants a number by Friday, a PM-suite renewal, the New Year, and the January 1 cabinet tariff step-up. The tariff step-up makes Procurement a real cross-sell inside cabinet and finish allowances.

Geography splits the ICP. Texas has the volume, with **140,002 single-family permits in 2025** (−11.7%) ([NAHB Eye on Housing](https://eyeonhousing.org/2026/03/single-family-permits-end-2025-on-a-soft-note/)). California has the value and Quotr's only proof. Two clusters have no software vendor in them: "keep your PM tool, add estimating," and estimate time and free estimates, which only trade press answers.

### Small developers anchor on one $/sq ft and the GC's free number

The sixth ICP is defined by a moment rather than a firm type. It is a sponsor who needs a credible hard-cost number before closing on land, before the GC bids, or for a lender. Fifty-two BiggerPockets thread titles were coded for this research:

| What the thread asks | Threads | Share |
|---|---|---|
| Local, current cost | 23 | 44% |
| Does the deal pencil | 8 | 15% |
| GC overrun | 7 | 13% |
| Names a place | 15 | 29% |

The local-cost, pencil and overrun clusters clear the framework's promotion threshold of 5 in 50 posts ([example thread](https://www.biggerpockets.com/forums/44/topics/456545-finding-the-cost-to-build?page=1)).

The habit is a single $/sq ft anchor built from comps. One poster was told to "get comps, subtract the land value, then divide by the sq ft" ([BiggerPockets](https://www.biggerpockets.com/forums/738/topics/921760-portland-4plex-townhome-build-cost-and-contractor-recommendations)). The other default is the GC's free precon number. The anxiety is whether the number survives a lender or a limited partner, and the push arrives in titles such as "Contractor suddenly over budget by 40%" ([BiggerPockets](https://www.biggerpockets.com/forums/67/topics/1105632-contractor-suddenly-over-budget-by-40)).

Calculators win pre-plan retrieval, taking all nine results in one proxy. But at least one describes its own output as ±20–30% and "not for construction loans or bids" ([EstimationPro](https://estimationpro.ai/tools/cost-to-build-a-house-calculator)).

Quotr's price is trivial against the risk this buyer carries. Service costs **$1,000 for a 4,000 sq ft fourplex**. That is 0.04–0.11% of hard costs at the $220–$700 per sq ft range AI answers already quote. One 1% extension fee on a $3M loan is **$30,000** (arithmetic).

Real cost differences justify a few geo pages. Bay Area multifamily hard costs ran **$81 per sq ft** above the rest of California, and LA's ran **$35** above ([Terner Center](https://ternercenter.berkeley.edu/wp-content/uploads/2020/08/Hard_Construction_Costs_March_2020.pdf)). Hard dates add triggers: the Opportunity Zone 2.0 map takes effect January 1, 2027 ([Kiplinger](https://www.kiplinger.com/taxes/tax-planning/how-governors-pick-opportunity-zone-2-designations)), and Texas SB 840 and SB 15 took effect September 1, 2025 ([Foley](https://www.foley.com/insights/publications/2025/07/texas-enacts-critical-real-estate-reforms-senate-bills-15-17-840/)).

### LA rebuild owners face a $300,000–$500,000 gap with no independent cost data

The Palisades and Eaton fires destroyed about **16,250 structures**, roughly 11,400 of them homes ([NBC LA](https://nbclosangeles.com/news/california-wildfires/map-damage-assessment-eaton-palisades-fire/3620536/)). By autumn 2026 only about 215 homes were complete in unincorporated Altadena ([Lytemods](https://lytemods.com/fire-rebuild/altadena)). In the Palisades, 1,557 of 3,984 destroyed homes had filed to rebuild and **48 were finished** ([Alto Builds](https://altobuilds.com/palisades-fire-rebuild)), which means about 61% of Palisades owners had not filed at all. Permits also slowed: median times for Altadena filings rose from 95 to 199 days ([Shovels](https://www.shovels.ai/blog/la-wildfire-rebuild-permit-data/)).

The insurance gap is the push. In an LAist survey of AAA policyholders in Altadena, average dwelling coverage was **$628,000**, adjusters' rebuild estimates averaged $867,000 and contractor quotes averaged **$928,000** ([LAist](https://laist.com/brief/news/climate-environment/eaton-palisades-fire-altadena-aaa-insurance-rebuild-costs)). Department of Angels survey respondents reported being **$500,000 short on average** ([LAist](https://laist.com/brief/news/climate-environment/fire-rebuilding-costs-new-funds-financing-attempt-to-fill-gaps)).

The cost answers engines retrieve come from contractor marketing: $350–850 per sq ft in Altadena and $550–1,200 in the Palisades. One of those contractor pages admits there is "no government or academic dataset tracking per-square-foot LA rebuild pricing" ([Altadena Custom Home Builder](https://altadenacustomhomebuilder.com/blog/cost-to-rebuild-a-house-after-a-fire-in-los-angeles-2026-numbers)).

Anxiety here is earned. Headlines report an unlicensed contractor taking thousands from Altadena homeowners ([ABC7](https://abc7.com/post/altadena-homeowners-hoping-rebuild-eaton-fire-sent-thousands-man-turned-unlicensed-contractor/17876660/)). Habit is deference to the insurer's number.

The hard trigger is **January 7, 2027**. That date is the second anniversary and the 24-month mark for additional living expenses under Insurance Code §2060 ([Property Insurance Coverage Law](https://www.propertyinsurancecoveragelaw.com/blog/california-wildfire-ale-extensions/)).

ClaimArchitect already owns "valuation to dispute the insurer" in the Palisades ([LA Business Journal](https://labusinessjournal.com/featured/tool-identifies-insurance-payout-estimate-gaps/)). Quotr's white space is the area-wide, dated, line-item cost tracker plus the builder and materials layers. It must stay strictly on the "estimate, not adjusting" side of the line, which means:

| Guardrail | What it requires | Source |
|---|---|---|
| No public adjusting | Never negotiate, "maximize" or settle claims, or be paid a share of a claim | [CDI notice](https://www.insurance.ca.gov/0250-insurers/0300-insurers/0200-bulletins/bulletin-notices-commiss-opinion/upload/Notice-Solicitation-by-Public-Adjusters-in-the-Southern-California-Wildfire-Areas.pdf) |
| No cold outreach to survivors | Respect state limits on post-disaster solicitation | [CDI notice](https://www.insurance.ca.gov/0250-insurers/0300-insurers/0200-bulletins/bulletin-notices-commiss-opinion/upload/Notice-Solicitation-by-Public-Adjusters-in-the-Southern-California-Wildfire-Areas.pdf) |
| License link | Link the CSLB license lookup on every bid page | — |
| Price-gouging cap | Raise no LA prices more than 10% while an emergency order covers the goods or services | [EG Attorneys](https://www.egattorneys.com/price-gouging-penal-code-396) |

### Lenders lack a published review price, but Quotr is not bank-grade yet

US banks held **$453.5B of construction and development loans** at June 30, 2026, of which $91.3B was 1–4 family ([FDIC](https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-second-quarter-2026.pdf); [NAHB Eye on Housing](https://eyeonhousing.org/2026/08/single-family-adc-lending-falls-back-in-q2/)). Private residential-transition originations, covering fix-and-flip, bridge and similar loans, rose **13% year over year in Q1 2026** ([SFR Analytics](https://newsletter.sfranalytics.com/p/april-2026-private-lending-market)).

The buyer's identity is "the person who didn't miss it." The California Mortgage Association just published a case titled "A Broken Construction Project and A $750,000 Loss" ([CMA](https://www.californiamortgageassociation.org/2026/06/09/a-broken-construction-project-and-a-750000-loss/)).

Built already sells an AI plan-and-cost review (PCR) that it says returns "in 15 minutes, at less than half the cost of a traditional review," benchmarked on 389,649 projects. Built publishes no price ([Built](https://getbuilt.com/blog/plan-and-cost-review-construction-loans/)). Draw inspections run $75 to $1,000 per visit ([Ventavid](https://www.ventavid.com/blog/construction-draw-inspection)).

Ranked by evidence count, the unmet needs are:

| Unmet need | Sources |
|---|---|
| Turnaround | 5 |
| Reconciling the budget to the plans' scope | 5 |
| Review cost | 4 |

**Nobody in the retrieved set publishes a PCR price.** Quotr's $0.25 per sq ft (about $700 for a 2,800 sq ft spec home) is therefore a unique, quotable fact.

The honest assessment is that Quotr Service fits a private lender's or fund's **desk second opinion**, not a bank-grade independent PCR. The gaps are concrete:

| Gap | Why it matters |
|---|---|
| Independence | Service is sold to borrowers, and Procurement supplies the same project teams |
| Credentials | No named, credentialed reviewer stands behind the report |
| Liability | No E&O cover or reliance letter is stated |
| Security | No SOC 2 statement |
| Turnaround | The SLA conflicts across Quotr's own pages |

### Importers get a fresh tariff trigger every six weeks as China supply narrows

The ninth ICP signs or steers a finish package worth $30K to $500K+. The package covers windows, doors, cabinets, vanities, flooring, tile, quartz, fixtures and lighting, and this buyer weighs a factory-direct import from China against a domestic dealer.

As of November 6, the duty stack on a Chinese finish import is layered. It starts with the most-favored-nation duty and legacy Section 301 list duties, which are often 25%. Most finish categories then add **Section 301 "forced-labor" duties of 12.5% on China**, in effect since July 24, 2026 ([EY](https://taxnews.ey.com/news/2026-1607-ustr-finalizes-section-301-forced-labor-tariffs-on-60-economies-additional-tariffs-of-10-percent-or-125-percent-take-effect-24-july-2026)). Category-specific duties sit on top:

| Category | Additional duties | Source |
|---|---|---|
| Cabinets and vanities | Section 232 at 25%, stepping to **50% on January 1, 2027** | [Green Worldwide](https://www.greenworldwide.com/section-232-wood-products-tariffs-remain-unchanged-through-2026/) |
| Wooden cabinets | Antidumping rate of **251.64% China-wide** (April 2026 review) | [Federal Register](https://www.federalregister.gov/documents/2026/04/23/2026-07866/wooden-cabinet-and-vanities-and-components-thereof-from-the-peoples-republic-of-china-final-results) |
| Aluminum windows and doors | Section 232 at 50% on full value | [Thompson Coburn](https://www.thompsoncoburn.com/insights/74-april-2-2026-new-proclamation-makes-major-revisions-to-section-232-tariffs-on-steel-aluminum-copper/) |
| Quartz | Section 201 safeguard quota of 25% in-quota and 50% over-quota, on top of antidumping duties | [Mondaq](https://www.mondaq.com/unitedstates/international-trade-investment/1829966/new-section-201-safeguard-tariffs-on-quartz-surface-products) |

The extended US–China truce runs to **January 10, 2027** ([CNBC](https://www.cnbc.com/2026/09/24/us-china-trade-truce-bessent-trump-xi.html)).

The dominant restraining force is anxiety, not habit. Buyers fear wiring a deposit to an unseen factory, failing a code inspection, and a landed cost that moves after commitment. The dealer quote is the anchor that makes the switch feel worth the risk.

Quotr's three Bay Area project cards show finish packages priced 44–60% below the quoted market ranges. Saratoga, for example, came in at $97,000 against a $187K–$218K local quote ([Quotr](https://quotr.ai/procurement/)). Its rival Port2Site advertises 15–30% savings on 50+ unit orders in 10–14 weeks ([Port2Site](https://www.port2site.com/direct-import)).

The retrieval proxy corrects the prior audit. **Dealers and fabricators now rank with dated tariff explainers**, so "no vendor cited on tariffs" is no longer true for web retrieval. Still, no page stacks every duty layer per finish category with a worked landed-cost example.

The honest verdict is that demand is rising while China-only supply is shrinking. LVP, tile, fixtures, lighting and non-aluminum doors look more viable than cabinets and quartz (inference; verify each HTS stack).

### Architects search at bid opening, when the contract makes redesign free

There are **more than 19,000 US architecture firms, about three-quarters with fewer than 10 staff** ([AIA](https://www.aia.org/aia-architect/article/latest-insights-2024-firm-survey-report)). They are working in a contracting market: the Architecture Billings Index fell to **44.7 in September 2026** ([AIA](https://www.aia.org/resource-center/abi-september-2026-architecture-firm-billings-slump-deepens)).

This buyer's identity is designer, not estimator. Yet AIA B101-2017 keeps the duty to redesign "without additional compensation" when bids exceed the owner's budget, with an added exception for market conditions ([AIA Contract Documents](https://help.aiacontracts.com/hc/en-us/articles/1500010280541)). So the hot moment is bid opening. The habit is the GC's free number plus the last project's $/sq ft, and forum posters say they rely on a GC or outside estimator ([Archinect](https://archinect.com/forum/thread/150340217/budgets-pricing-and-responsibility)).

Quotr holds a real authority asset in its founder. He describes "years at design firms watching projects get derailed the moment a great design met a cost estimate" ([Quotr](https://quotr.ai/about-us/)).

The tool-pick prompts belong to Autodesk, RIB CostX, RSMeans and Trimble. Legacy listings that still call Quotr a Revit plug-in ([F6S](https://www.f6s.com/software/quotr)) risk engines promising architects an integration Quotr may no longer sell. Service fits the hot moment, at about $800 for a 3,200 sq ft house, but only after Quotr confirms it produces estimates from SD drawings.

## Geography justifies seven segments and fewer than ten pages, not forty

The pipeline runs in two passes: 50 states first, then about 33 metros keyed by CBSA code. It scores five layers for each ICP group:

| Layer | What it measures |
|---|---|
| A. Concentration | Establishments by NAICS |
| B. Demand growth | Permits, starts, data-center flags |
| C. Pain | Estimator wage and scarcity, $/sq ft gaps, regional labor impact |
| D. Regulatory distinctness | Rules that differ by state or metro |
| E. Quotr fit | First-party projects, delivery coverage |

Weights differ by ICP group. One sanity rule from the framework changed the design. For trade subs and GCs, removing regulation and Quotr-fit barely moved the ranking (rank correlation 0.98–0.99, no top-10 swaps), so those two layers became **gates for whether a geo page is legitimate**, not scoring weights. The census and BLS tables could not be pulled, so tiers are judgment anchored on a few measured values.

The state picture is clear at the top. California, Texas and Florida lead in estimators, with **25,850, 20,240 and 14,150** in May 2023 ([BLS](https://www.bls.gov/oes/2023/may/oes131051.htm)), and they lead in permits too. Arizona, Georgia, North Carolina, Virginia, Washington and New York form tier 2.

Pain splits into two geographies:

| Pain type | Where | Evidence | Quotr product with the biggest ROI |
|---|---|---|---|
| Value per hour | CA, NY, MA, WA, DC | Bay Area hard costs +$81/sq ft ([Terner Center](https://ternercenter.berkeley.edu/wp-content/uploads/2020/08/Hard_Construction_Costs_March_2020.pdf)); Seattle estimators earn $99,570 at an LQ of 1.44 ([BLS](https://www.bls.gov/regions/west/news-release/occupationalemploymentandwages_seattle.htm)) | Service and Procurement |
| Capacity | Sun Belt | 42% of Southern contractors report immigration-enforcement impacts ([AGC](https://www.agc.org/news/2026/09/03/construction-workforce-shortages-remain-acute-despite-soft-market-conditions-data-centers-strain)); Phoenix cost escalation +5.30% a year ([RLB](https://www.rlb.com/wp-content/uploads/sites/4/2026/06/Q2-2026-QCR_7.7.2026.pdf)) | Software seats that replace estimator hours |

The provisional metro index puts LA first for subs, residential and developer, procurement and architect ICPs. Houston is first for GCs and lenders, and SF–Oakland and San Jose rank second and third for procurement.

| Segment | Primary ICPs | Dated evidence | Strength |
|---|---|---|---|
| Bay Area high-cost home, ADU and remodel (SF–Oakland, San Jose) | 5, 6, 9, 10 | +$81/sq ft hard-cost premium; Quotr procurement cards (Saratoga $97,000 vs $187K–$218K) | Strong (first-party data) |
| LA rebuild zone (Palisades, Altadena, Malibu) | 7, 5, 9, 8 | ~11,400 homes destroyed; 48 Palisades homes complete; permit medians up to 199 days | Strong (sources interested) |
| Texas Triangle volume (Houston, DFW, Austin, San Antonio) | 1, 3, 4, 5, 6, 8 | 140,002 single-family permits (2025); Houston 40,471 and DFW 34,778 ([GlobeSt](https://www.globest.com/amp/2026/01/27/single-family-permits-decline-as-builders-adjust-to-market-challenges/)); SB 840/SB 15 | Medium (no Quotr data yet) |
| Data-center MEP corridor (Phoenix, DFW, NoVA, Atlanta, Columbus, Reno) | 2, 1, 4 | $50.7B annual-rate data-center spending; AIA data centers +33% (2026) and +24.7% (2027) ([AIA](https://www.aia.org/resource-center/july-2026-consensus-construction-forecast)) | Medium; metro split unmeasured |
| Florida storm, condo and Live Local | 3, 5, 6, 9 | Florida 178,297 units (2025); rules unverified | Weak to medium |
| Carolinas and Southeast single-family belt | 3, 5, 1 | Charlotte 14,211 and Atlanta 19,610 single-family permits (2025 YTD) | Medium |
| Northeast and Pacific NW high-wage design and precon | 10, 4, 2, 6 | Seattle estimators $99,570; rules unverified | Weak to medium |

The legitimacy test is that a geo page is justified only if **at least two of three** conditions hold: the rules differ (licensing, code, wage, zoning or disaster), prices differ materially, or Quotr has local first-party data. California passes all three. Texas passes the first two but should wait for **10–20 Quotr estimates** in the state. Florida passes only on recall and needs verification. The data-center corridor earns one page, not six. Procurement earns one delivery-region page, because tariffs are national.

The resulting year-one plan is **one national hub and seven to nine spokes**:

| Spoke type | Spokes |
|---|---|
| State | California, Texas, Florida |
| Metro or zone | Bay Area, LA rebuild, Houston–DFW |
| Corridor | Data-center MEP |
| Procurement | Delivery regions |

That replaces 40 city pages, and California spokes come first.

Language is a geographic variable too. Hispanic workers make up **32.8% of the construction labor force** ([NAHB Eye on Housing](https://eyeonhousing.org/2025/10/hispanics-comprise-nearly-one-third-of-the-construction-labor-force/)), which justifies running 3–4 of ICP3's interviews in Spanish and a Spanish pilot aimed at Texas, Florida, Arizona, Nevada and California.

No engine has been shown to add a user's city to a non-local prompt on its own. Geography therefore pays off only through place-specific facts on pages and persona facts in prompts. Run ten rebuild, ADU and state-rule prompts with and without a city, three times each in ChatGPT and Perplexity, before building more geo pages.

Recruit switch interviews mainly where each ICP concentrates:

| ICP | Recruit from |
|---|---|
| ICP1 | Houston, DFW and Phoenix |
| ICP2 | NoVA, Phoenix and DFW |
| ICP3 | Houston, DFW, Atlanta and Charlotte |
| ICP5 | Bay Area, LA and Houston/DFW |
| ICP6 | Bay Area, LA and Austin/DFW |
| ICP7 | Altadena and Palisades (10 of 12) |

## Simulated AI journeys end without Quotr in all ten ICPs

Researchers ran 93 web searches shaped like the fan-out sub-queries each ICP's journey would trigger. **Quotr surfaced in 4.** Three of those were its own blog posts appearing in results without being named as a pick, and one was a 2025 press-release repost on a branded query.

| ICP | Proxy runs | Quotr appeared | Who owns the nodes today | Winning format |
|---|---|---|---|---|
| 1 | 9 | 1 (own AI-accuracy how-to) | Vendor listicles (BuildOps, SparkQuote), SourceForge, Capterra, Mike Holt threads | Vendor "2026" listicles, directories, old forum threads |
| 2 | 9 | 1 (own PlanSwift pricing post) | Review sites, Mike Holt, resellers, rivals' "X review" pages (McCormick on ConEst) | Competitor-authored review/alternatives pages |
| 3 | 4 | 1 (own drywall listicle, not named) | Vendor trade listicles, list farms, Capterra network | "Best drywall software 2026" lists; calculators |
| 4 | 11 | 0 | Directories; Meltplan and AI-leveling startups; Procore Library and Trimble guides | Dated vendor comparisons; long method guides |
| 5 | 8 | 0 | Capterra, vendor "vs" pages, JLC and Houzz research, consumer cost guides | Review pages; vendor-owned surveys syndicated by trade press |
| 6 | 9 | 0 | BiggerPockets (14 of 19 and 18 of 20 results), calculators, practitioner blogs, agency templates | Forum threads; calculators |
| 7 | 12 | 1 (press repost, brand query) | Contractor "2026 guide" pages, local news, nonprofits, law firms, ClaimArchitect | Dated contractor guides; Redfin-style data releases |
| 8 | 10 | 0 | Built, engineering firms, Scotsman Guide (1–4 years old), directories | Vendor blogs with hard numbers; no price anywhere |
| 9 | 11 | 0 | Law firms, programmatic HTS sites, dealer and fabricator tariff explainers | Dated "2026–2027" dealer explainers |
| 10 | 10 | 0 | Contract PDFs, AACE standards, consumer fee guides, Archinect | Clause libraries; forum threads |

The simulations below are modeled, not captured. Each assistant turn was written from the retrieval evidence above and from Quotr's September Perplexity answers. Read them as a map of where a missing asset blocks Quotr's entry, not as predictions of exact output.

| ICP | Simulated persona | Turn 1 (verbatim style) | Shortlist at the last turn | Turn where Quotr could enter | Asset that would earn the entry |
|---|---|---|---|---|---|
| 1 | Dave, 11-person electrical sub, Sacramento, three Revu 20 seats | "im doing takeoffs till midnight again, 3 bids due this week…" | ConEst, Kreo, STACK | Turn 5, "anything newer and cheaper… cancel monthly" | Correct $79.90 pricing page plus cancel/export terms; Capterra listing |
| 2 | Chief estimator, 160-person electrical sub, NoVA, Accubid plus Revu 20 | "One of my senior estimators just gave notice…" | Togal, Beam, STACK; "stay on Accubid" | Turn 3, "what works alongside Accubid" | Coexistence/import page; MEP accuracy benchmark |
| 3 | Javier, 14-person drywall sub, Houston | "how do drywall guys do takeoffs faster…" | STACK, Togal, PlanSwift (Beam for service) | Turn 4, "anything cheaper than 300 a month" | Third-party list carrying $79.90; finish-trade reviews |
| 4 | Dana, precon at a $150M GC, Fort Worth | "Owner sent 30% SD drawings… budget Monday" | DESTINI, ProEst, Procore Estimating, STACK, service firms | Turn 4, "would outsourcing be faster" | SD-budget page with one SLA and a sample |
| 5 | Dan, 5-person custom builder, San Mateo County | "I underbid a whole-house remodel by about $40k…" | Handoff, Buildxact, Buildertrend or JobTread | Turns 2 and 5 (alongside Buildertrend; cabinet tariffs) | "Use alongside your PM suite" page; Jan 1 tariff page |
| 6 | Ex-flipper, Oakland fourplex lot | "Rough cost to build a fourplex?" | RSMeans, cost consultant, unnamed estimating firms | Turns 2–3 (lender wants a budget; consultant vs AI) | Method page, sample, brand-attributed price sentence |
| 7 | Altadena owner, $607K coverage | "Is that enough to rebuild?" | ClaimArchitect, public adjusters, contractors | Turn 5, "what should a line-item estimate include" | Dated tracker plus anonymized line-item sample |
| 8 | Credit analyst, Charlotte community bank | "$6.2M for 24 townhomes feels low…" | Built, PCR firms, draw inspectors | Turn 5, "shortlist with prices and turnaround" | Published price and SLA page |
| 9 | Spec builder, three Los Gatos homes | "Dealer quote is $195k per house… still worth importing?" | Alibaba, sourcing agents, Port2Site, Build Source | Turn 3, "who delivers duty-paid with NFRC and CARB documents" | DDP inclusions, compliance pages, rate-lock statement |
| 10 | Principal, 8-person San Diego firm | "Bids came in 27% over… do I have to redesign for free?" | Cost consultant, GC precon, Autodesk, RIB CostX, RSMeans | Turns 3–4 (independent estimate this week) | B101 72-hour-plan page; consultant-vs-AI decision page |

The developer journey shows how small the fix can be. In the simulated current state, the ex-flipper's second turn ("I signed an LOI with 21 days of feasibility… my lender wants a line-item budget") retrieves lender blogs and estimate-class explainers. The third turn compares a cost consultant, GC precon and "AI estimating services." The likely answer repeats "$0.25 per sq ft" as what "one service" charges, without naming Quotr, because that is the observed Perplexity behavior.

In the target state, each turn retrieves a different Quotr asset:

| Turn | What the buyer asks | What the engine cites in the target state |
|---|---|---|
| 1 | Rough cost for an Oakland fourplex | A sentence beginning "Quotr.ai's Q4 2026 Bay Area index puts fourplex hard costs at…" |
| 2 | How to get a credible budget before closing | A dated "estimate before you close" method page and sample |
| 3 | Consultant vs GC precon vs AI estimating | A fair decision page plus one BiggerPockets thread naming Quotr |
| 4 | Will my lender accept it | A dated page quoting one named lender |

Every one of those assets is cheap except the index, which depends on Quotr agreeing to publish aggregate Service data.

The pattern across all ten ICPs is that **engines reach a pick by turn three to five, and Quotr's entry point is almost always a fact the buyer asks for at the deciding stage**: a correct price, one turnaround, a cancel policy, a lender statement, a compliance document, an accuracy method. The research found no evidence that a better-written introductory article would change those picks.

## The GEO system: fix facts, ship three dated pages, then prove

### Ninety-day build order

The framework's rule is one page per intent cluster, an urgent version and a considered version where buyers search under time pressure, and evidence density over volume. Engines rewrite prompts into sub-queries carrying "2026," "official" and "price." GPT-5.6 now retrieves brand product and pricing pages more often than listicles, 16.4% against 8.2% ([Peec](https://docs.peec.ai/research/gpt-56-product-pages-vs-listicles); [Ahrefs](https://ahrefs.com/blog/query-fan-out-chatgpt/)). That puts Quotr's own factual pages back in scope, provided the facts agree.

| Window | Build | ICPs served | Effort (researcher estimates) |
|---|---|---|---|
| Nov 6–20 | Decide one turnaround, the 50,000 sq ft tier rule, procurement categories/delivery/importer of record, a security statement and Revit status. Remove retired $299.90 pricing from ~13 URLs and llms.txt. Rewrite fetched pages so the brand travels with each fact ("Quotr.ai's Service charges $0.25 per sq ft…") | All | Leadership 1–2 days; marketing 3–5 h |
| By Nov 20 | **Bluebeam Revu 20 end-of-life decision page** (refresh Dec 1, Dec 20, Jan 5, then convert to "after EOL") | 1, 2 | 1 day |
| By Dec 5 | **Cabinet and vanity tariff Jan 1, 2027 page** plus monthly tariff tracker v1, customs-broker reviewed | 9, 5, 3, 7 | 2–3 days plus broker review |
| Nov–Dec | **Developer hub** with three urgent pages (feasibility estimate, lender-ready budget, GC bid over budget), one decision page and residential sample deliverables | 6 (8 reuses the lender page) | 1–2 weeks |
| By Dec 15 | **LA rebuild hub**, tracker v1, coverage-to-sq-ft calculator, bid-check page; FireTips 301 to quotr.ai; anniversary data pitch ready | 7 | Part of the 40–60 h bet |
| Dec–Jan | **MEP sub hub** plus "bid due tomorrow" (only once turnaround is fixed); cost-per-bid calculator; Capterra/GetApp/Software Advice and G2 listings with the first 10 reviews | 1, 2, 3, 5 | 4–8 h + 3–6 h + review asks |
| January | **Year-stamp sweep** to "2027" with real changes logged. **Residential hub** plus "use alongside Buildertrend/JobTread." Trade-hub rewrites plus drywall and roof-squares calculators | 5, 3, all | 2–3 weeks |
| Jan–Feb | Accuracy benchmark method and first results; Q4 2026 Hard-Cost Index released in January (fresh-start window); 6–12 switch interviews per Tier 1 ICP | 1, 2, 3, 5, 6, 7 | Data-dependent |

### Owned pages by ICP

| ICP | Hub | Urgent pages (hot mode) | Considered pages (cold mode) | Geo pages |
|---|---|---|---|---|
| 6 | /developers/ (today it only mirrors /service/) | Feasibility estimate; lender-ready budget; GC bid over budget | Cost consultant vs GC precon vs AI estimating; four samples; product cost pages (fourplex, ADU, SB 9, build-to-rent); pro forma template | Max five data-backed metro pages (Bay Area, LA, Austin, Seattle–Portland, later South Florida) |
| 1 | /software/mep-subcontractors/ | Bid due tomorrow; Revu 20 EOL | Cost per bid (hire vs outsource vs software); Quotr vs PlanSwift vs STACK; pricing/cancel/export FAQ; accuracy test; legend-vs-schedule scope gaps; fire-alarm and low-voltage takeoff | California Title 24 plus prevailing wage; data-center spoke |
| 3 | Trade hubs (drywall, flooring, roofing, ceilings, concrete, tile, painting, siding) | Four calculators; drywall overnight (only with a guaranteed SLA) | Takeoff for small subs, price per seat and per bid; software vs service vs outsourcing; PlanSwift alternatives; wall types and partition schedules | Spanish pilot (/es/ plus three pages) |
| 5 | /residential/ plus custom builder, remodeler and ADU spokes | Service "need a number this week"; underpriced-job fixes; cabinet tariff page | Quotr vs Handoff; Quotr vs Buildxact; use alongside Buildertrend/JobTread; how to choose (neutral); worked custom-home estimate; markup vs margin; should you charge for estimates | Bay Area and LA rebuild cost spokes |
| 7 | /rebuild/los-angeles/ with tracker | Check a rebuild bid; ALE documents checklist (links out); lot-buyer estimate | Line-item estimate explainer; rebuild vs sell; Chapter 7A and Zone 0 costs; prefab vs stick-built; finish materials | Altadena, Palisades, Malibu spokes |
| 9 | /procurement/ rebuilt with an urgent top block | Jan 1, 2027 cabinet tariff | Tariff tracker; DDP vs FOB; landed-cost calculator; NFRC, CARB/TSCA and cUPC pages; category pages; "what not to import in 2027"; sourcing-route guide; vs Port2Site; how it works; Landed-Cost Index | California compliance hub |
| 2 | /mep-estimating-teams/ | Revu 20 EOL (shared); estimator quit mid-season | Accubid alternatives ("keep Accubid, add AI counts"); ConEst vs Accubid vs McCormick; Estimation MEP alternatives; OST alternatives; cost of an estimator; migration guide (gated); /security/ (gated) | Data-center page (shared) |
| 4 | /general-contractors/ | SD budget fast; precon capacity on demand; bid day with uncovered trades | Conceptual estimating method; ROM vs SD vs DD vs CD; bid-leveling guide plus template; scope-gap checklist; Quotr vs DESTINI and vs ProEst | One California commercial cost page |
| 8 | /lenders/ | Budget review from plans in 72 hours at $0.25/sq ft (after the SLA is fixed) | Methodology; redacted sample report; PCR options compared; cost-to-complete; contingency | LA fire-rebuild budget review |
| 10 | /architects/ | Bids over budget (B101 §6.6–6.7, 72-hour plan); check the GC's DD number | SD cost estimate (Class 4–5, UniFormat); consultant vs GC vs AI; founder essay; Revit FAQ stating the truth | California cost page (conditional) |

All pages follow the framework's format. Each heading opens with a 40–60-word direct answer, there is about one sourced statistic per 150 words, and tables sit near the top. Every page carries a visible update date and a named, credentialed reviewer. Product facts must be mirrored exactly across /pricing/, hubs and comparison pages.

Comparison, pricing, tariff and tracker pages refresh monthly, because the median citation half-life is about 4.5 weeks ([NoGood](https://nogood.io/blog/content-freshness-ai-citations/)). Hubs and answer pages refresh quarterly.

### Four shared proof assets cover all ten ICPs

Proof is the binding constraint: buyers in 7 of 10 ICPs are held back mainly by anxiety. Original data is the asset most likely to be cited. In one prior study, primary-research pages earned 3.3 times more citations per page ([Growth Memo](https://www.growth-memo.com/p/why-most-original-data-never-gets)). Building one asset per ICP would dilute the effort. These four cover all ten ICPs between them:

| Asset | What it contains | ICPs served | Gate |
|---|---|---|---|
| AI takeoff accuracy benchmark | 10–20 public plan sets per trade cluster, vector vs scanned, Quotr vs two named human estimators, error distribution by item, dated method | 1, 2, 3, 5 (and 4's AI-accuracy chain) | Plan sets and estimator time |
| Quotr Hard-Cost Index (quarterly) | Median and IQR $/sq ft and $/door by metro × product from Service jobs, with n and method; LA rebuild tracker as a monthly sub-series | 6, 5, 7, 8, 10, 4 | Permission to publish aggregates from the "$1.2B+ estimated" claim |
| Landed-Cost Index plus tariff tracker | Factory DDP vs a dated Bay Area dealer quote for 6–8 categories; every duty layer; lead time; n of quotes | 9, 5, 3 (flooring/tile), 7 | Customs-broker review; confirmed categories |
| Estimate-vs-outcome variance study | SD/DD estimates vs bids or buyout; borrower budget vs takeoff gap by trade | 4, 10, 8, 6 | Whether Quotr tracks outcomes after it estimates |

One combined **"State of Estimating 2027" survey** should replace the five separate surveys the notes propose. Run it bilingually, with role and trade splits (owner-estimators, chief estimators, finish trades, precon, residential), through AWCI, IEC, PHCC, NARI and BIA Bay Area channels. It would measure hours per takeoff, after-hours share, bids per week, hit rate, tools used and prices per unit. No such dataset surfaced in any retrieved source. One survey costs less than five and gives trade press a single annual hook, timed to ride the Houzz and AGC/NCCER September news cycle.

### Off-site placements and engines by ICP

The default engine pair for every ICP is ChatGPT plus Google AI Overviews and AI Mode. Perplexity stays in the set for the trade-sub ICPs, where directory-led answers dominate and Quotr has a September baseline. Copilot and Claude are quarterly checks for GC, lender and architect prompts until Quotr's own "how did you hear about us" data says otherwise.

| ICP | First off-site placements (leverage per hour) | Engines tracked |
|---|---|---|
| 1, 2, 3 | Capterra network plus G2 with 10–20 reviews per trade cluster; SourceForge and SoftwareWorld listings; pitches to ConstructionCoverage, TDPM, exayard and ConstructConnect lists; disclosed estimator participation on Mike Holt and ContractorTalk; trade press (ECmag, ACHR News, Walls & Ceilings, Roofing Contractor, FCNews) from the survey; one chaptered YouTube video per trade | ChatGPT, AI Mode, Perplexity |
| 5 | Capterra and G2 residential category; Workyard and ConstructionCoverage lists; JLC, Pro Remodeler and Pro Builder data pitches; BIA Bay Area or NARI session; one custom-home YouTube walkthrough | ChatGPT, AIO/AI Mode |
| 6 | Disclosed founder answers in BiggerPockets cost threads (1 h a week); index pitches to Terner Center, CA YIMBY, Casita Coalition, SPUR and Bisnow; one guest method piece on a lender blog | ChatGPT, AI Mode, Perplexity |
| 7 | Anniversary data pitch to LA Business Journal, LAist, Pasadena Now, Palisadian-Post and SMDP; nonprofit data partnerships (Department of Angels, EFSN, Altadena Land Initiatives, United Policyholders); in-person clinics | AIO/AI Mode, ChatGPT |
| 9 | Landed-Cost Index pitched to Floor Daily, Stone World and cabinet trade press; one factory-QC YouTube video; procurement roundups and a claimed F6S profile | ChatGPT, AI Mode |
| 4 | G2 and Capterra review drive in estimating and bid-management categories; ConstructionPlacements leveling list; Construction Dive or ENR data piece; founder LinkedIn articles | ChatGPT, AI Mode; Copilot quarterly |
| 8 | Scotsman Guide contributed article (6–8 h); AAPL and CMA webinar; Rabbet or Land Gorilla partnership pitch | ChatGPT; Copilot quarterly |
| 10 | Entity fixes on F6S, Crunchbase and LinkedIn Revit copy (2–4 h); founder op-ed and answers on Archinect; AIA chapter small-firm talk | ChatGPT, AIO; Claude quarterly |

### Prompt matrix: 24 full-context prompts join the tracking set

The existing 53-prompt tracking set has three limits. It holds short, context-free prompts. It is baselined only on Perplexity. Its rules explicitly forbid adding persona context. The framework's evidence says persona facts change which brands engines name, and that "ask for a pick" prompts produce brand recommendations **22.8%** of the time against 8.0% for topic-only prompts ([Momentic](https://momenticmarketing.com/blog/prompt-set-worth-tracking)). The merge therefore adds a persona layer rather than replacing the old set.

| Group | Contents | Cadence |
|---|---|---|
| A | The 23 Tier A prompts, unchanged, for continuity | Daily on ChatGPT and AI Mode; weekly on Perplexity |
| F | The 24 full-context ICP prompts below, weighted by tier | Daily on ChatGPT and AI Mode; retire dated prompts on schedule |
| B | The 30 Tier B prompts, as a watch list | Monthly |
| Brand | The existing brand prompts plus four ICP brand prompts (Quotr vs PlanSwift; Quotr vs Handoff; Quotr lender acceptance; Quotr vs Built), reported separately | Daily |

Brand prompts are reported separately because they mention the brand about 92% of the time against 20% for unbranded prompts.

Groups A and F total **47 prompts a day per engine, or about 2,800 runs a month across two engines**. A Rankscale Pro seat at $99 covers about 4,800 answers a month ([Rankscale](https://rankscale.ai/pricing)).

| ID | ICP | Full-context prompt (abridged; simulated wording) | Intent / stage / mode | Expected fan-out nodes | Owning page | Retire |
|---|---|---|---|---|---|---|
| F01 | 6 | 5,000 sq ft Oakland lot under LOI, 3 weeks of feasibility left; fourplex cost per sq ft and per door in 2026; how to get a credible estimate before closing | pick / active / hot | fourplex cost Oakland 2026; cost per door; estimating service developers | /developers/feasibility-estimate/ | — |
| F02 | 6 | Lender wants a trade breakdown for a 6-unit Sacramento townhome project at SD; what format, who prepares it independently | do / deciding / hot | lender budget requirements; construction budget template | /developers/lender-ready-construction-budget/ | — |
| F03 | 6 | GC bid for a 12-unit San Jose walk-up came in 30% over; IC in 10 days; check for padding and value-engineer | validate / consuming / hot | bid over budget VE; bid leveling | /developers/gc-bid-over-budget/ | — |
| F04 | 6 | New construction cost per sq ft for a California fourplex, 2026, investor-grade finishes | learn / passive / cold | California fourplex cost 2026; RSMeans; Terner | /cost-to-build/fourplex/ | Rename to 2027 in Jan |
| F05 | 1 | 9-person electrical shop, Fort Worth; nightly takeoffs with highlighters and the Bluebeam count tool; faster way without hiring | learn→pick / first thought / hot | AI electrical takeoff 2026; Bluebeam count alternative; reviews | /software/mep-subcontractors/ | — |
| F06 | 1 | Revu 20 licenses stop working at year-end; 3 users only count electrical devices; cheaper takeoff option | pick / deciding / dated | Bluebeam alternatives 2026; Revu 20 end of life; price | Revu 20 EOL page | After Q1 2027 |
| F07 | 1 | Only estimator quit; 25-person Nashville electrical sub, 12 bids this month; hire vs outsource vs AI, costs | compare / active / hot | estimator salary 2026; outsourced estimating cost; AI estimating price | Cost-per-bid calculator | — |
| F08 | 1 | Bid due Thursday 2 pm, 42 electrical sheets, 60,000 sq ft Sacramento school, prevailing wage; who does a takeoff by Wednesday and at what cost | do / active / hot | electrical takeoff services; price per sheet; turnaround | Bid due tomorrow (MEP) | — |
| F09 | 3 | 15-person commercial drywall sub, Houston; boards and studs from PDF; best tool and cost | pick / active / hot | best drywall takeoff software 2026; STACK pricing; Togal pricing | /software/trades/drywall/ | — |
| F10 | 3 | Roof squares, ridge, hip and valley from architectural plans for new construction; software | do / active / hot | roof takeoff from blueprints; pitch factor; aerial vs plans | /software/trades/roofing/ | — |
| F11 | 3 | Flooring contractor: buy LVP or porcelain factory-direct duty-paid; cheaper than a distributor? | compare / passive→active / cold | LVP tariff 2026; DDP flooring; landed cost | /procurement/flooring/ | — |
| F12 | 5 | 4-person San Jose custom builder on Buildertrend plus Excel; switch to JobTread or add a separate estimating tool for PDF takeoff | compare / deciding / cold | Buildertrend vs JobTread; estimating software takeoff residential | /residential/use-with-buildertrend-jobtread/ | — |
| F13 | 5 | January; small Charlotte GC, 6–8 custom homes a year; stop estimating in Excel; best software with plan takeoff and real cost | pick / active / cold | best estimating software custom home builders 2027; Handoff pricing; Buildxact pricing | /residential/custom-home-builders/ | — |
| F14 | 5 | Cabinet tariffs go to 50% on Jan 1; three spring custom homes with $40–60k allowances; lock in now; factory-direct worth it? | compare / active / hot (dated) | cabinet tariff 2027; factory-direct cabinets; AD/CVD | Cabinet tariff 2027 page | Rename after Jan 1 |
| F15 | 7 | Contractor quoted $780,000 to rebuild a 1,400 sq ft Altadena house; fair for 2026; what line items | validate / deciding / hot | Altadena rebuild cost per sq ft 2026; CSLB; line items | /rebuild/check-a-rebuild-bid/ | — |
| F16 | 7 | Independent line-item rebuild estimate for an LA insurance claim before accepting the settlement | do / active / cold | independent rebuild estimate LA; Xactimate vs contractor | /rebuild/line-item-rebuild-estimate/ | — |
| F17 | 9 | Saratoga custom home: cabinets, vanities and windows quote $210k, 20% over; factory-direct from China worth it with 2026 tariffs? | compare / first thought / hot | cabinet tariff 2026; import building materials China; factory direct California | /procurement/ | — |
| F18 | 9 | Sourcing agent vs Alibaba vs a managed duty-paid importer for a 3-house finish package | pick / active / cold | best sourcing agent building materials; Trade Assurance; DDP jobsite | /procurement/compare-sourcing-routes/ | — |
| F19 | 2 | 5-estimator electrical team on Accubid, NoVA data-center bids up 30%, hit rate down; tools that help without replacing Accubid | pick / active / cold | Accubid alternatives; AI takeoff MEP; data center electrical estimating | /compare/accubid-alternatives/ | — |
| F20 | 2 | Phoenix mechanical sub, 6 estimators on Revu 20 perpetual; buy Revu 21 or move counts to AI takeoff | compare / active / dated | Revu 21 pricing; Bluebeam alternatives estimators | Revu 20 EOL page | After Q1 2027 |
| F21 | 4 | Owner sent 30% SD drawings for a 60,000 sq ft Fort Worth MOB, budget by Monday; AI from PDFs or outsource | do / active / hot | conceptual estimate from SD; MOB cost per sq ft; outsourced precon | /service/schematic-design-budget/ | — |
| F22 | 4 | Lost $180K on a school because drywall and framing subs both excluded blocking; how GCs catch scope gaps before buyout; software that compares bids to drawings | learn / first thought / cold | scope gap checklist; bid leveling software 2026 | /scope-gap-checklist/ | — |
| F23 | 8 | Community bank credit analyst; borrower's $2.4M budget for 10 townhomes looks low; independent budget check from the plans in 2–3 days | do / active / hot | plan and cost review fast; PCR cost; construction budget review | /lenders/construction-budget-review/ | — |
| F24 | 10 | Bids on a clinic came in 27% over the owner's budget under AIA B101; redesign for free; find the overrun fast | learn→do / first thought / hot | B101 6.7 redesign; bids exceed budget options; independent estimate | /architects/bids-over-budget/ | — |

Each ICP's notes also carry 6 short category prompts and 3 brand prompts. Import them into the prompt library under new ICP-prefixed IDs. Fold overlapping short prompts into existing tracker items; for example, the drywall, flooring, electrical, roofing and LA-rebuild prompts map to T04, T05, T06, T51 and T47.

The existing audiences file maps onto the new ICPs as follows:

| Existing persona | New ICPs |
|---|---|
| Persona 1 | ICP1, ICP2, ICP3 |
| Persona 4 | ICP6, ICP7 |
| Persona 8 (outsourcing buyer) | Dissolves into the hot chains of ICP1, ICP3, ICP4, ICP5 and ICP6 |

The remaining personas map one-to-one.

### Measurement and the trigger calendar

Measurement must treat results as distributions. Identical prompts return the same brand list less than 1% of the time ([SEJ/SparkToro](https://www.searchenginejournal.com/ai-recommendations-change-with-nearly-every-query-sparktoro/566242)), and 91% of cited URLs appear in only one engine ([Growth Memo](https://www.growth-memo.com/p/the-consensus-gap)). Freeze each group for at least four weeks and run it once daily. Report monthly at the cluster level as four separate rates, each with a ± range: mention rate, citation rate, recommendation rate, and share of voice against named rivals. Never report a single prompt's result. Fifty prompts run daily give about **±6.1 points** of monthly margin, against ±13.2 for 10 prompts run five times a day ([Peec](https://peec.ai/blog/the-key-to-prompt-tracking)). Treat a change as real only if it exceeds ±15% week over week or ±10% month over month and persists for three periods ([Texta](https://www.texta.ai/blog/answer-variability-study-why-chatgpt-gives-different-answers)).

Log every run's date against the calendar below, and raise sampling in the weeks around December 9 to January 15. That way, movements can be attributed to triggers rather than noise.

| Date | Trigger (status) | ICPs | Page that must be live |
|---|---|---|---|
| Nov 10, 2026 | 178 Section 301 exclusions lapse unless extended (snippet-level) | 9 | Tariff tracker v1 |
| Mid-Nov and monthly | ABC producer-price analysis; September inputs +11.2% year over year ([BDC Network](https://www.bdcnetwork.com/products-and-materials/article/55413400/construction-material-prices-jump-22-in-september-up-112-year-over-year)) | 1, 2, 3, 5 | Escalation pages refreshed monthly |
| Dec 9 | FOMC meeting after a September hike ([CNBC](https://www.cnbc.com/2026/10/28/fed-interest-rate-decision-october-2026.html)) | 6, 8, 5 | Developer hub; contingency pages |
| Dec 11 | Surface-transportation funding stopgap expires ([Polyurea Magazine](https://polyureamagazine.com/2026/10/03/iija-extension-december-2026/)) | 2, 4 (secondary) | None |
| Dec 27 | OZ 2.0 Treasury certification deadline | 6 | OZ 2.0 cost-feasibility answer page |
| Dec 31 | Bluebeam Revu 20 end of life | 1, 2 | Revu 20 EOL page |
| Jan 1, 2027 | Cabinets/vanities to 50%; OZ 2.0 maps live; new California laws | 9, 5, 3, 7, 6 | Cabinet tariff page; OZ page |
| Jan 7 | LA fires second anniversary; 24-month ALE mark | 7, 8, 6 | LA rebuild hub, tracker, data pitch |
| Jan 10 | US–China truce expiry | 9 | Tariff tracker |
| ~Jan 8–21 | AGC/Sage outlook; ABC workforce estimate (the January 2026 edition already projected ~456,000 workers needed in 2027) ([EC&M](https://ecmweb.com/construction/news/55344103/construction-industry-must-attract-349000-workers-in-2026)); JCHS remodeling forecast ([JCHS](https://www.jchs.harvard.edu/press-releases/remodeling-growth-set-downshift-late-2026)) | All | "2027" year-stamp sweep; Hard-Cost Index Q4 |
| Feb 6 | Chinese New Year; factory closures | 9, 5 | Lead-time calendar |
| Feb (TBC) | IBS and KBIS | 5, 9 | Show-timed press release and demo videos |
| Mar–May | Spring bid season (unverified) | 1, 3, 4 | Urgent "bid due" pages and calculators |
| Jun (TBC) | AIA Conference on Architecture | 10 | Architect cluster |
| Sep–Oct 2027 | AGC/NCCER workforce survey; Houzz AI report; Bluebeam outlook | All | State of Estimating 2027 survey release |
| Jan 7, 2028 | LA 36-month mark | 7 | Tracker refresh |

## Confirm thirteen Quotr facts before publishing

These facts gate pages across most ICPs. Two of them, turnaround and the price tier, block every urgent-mode page in the system. Several carry over from the prior audit's fact sheet. The rest are new requirements created by ICP-specific pages.

| Fact | Versions or gaps found | Pages it gates |
|---|---|---|
| 1. Service turnaround | Stated at least seven ways: "as fast as 24 hours" (homepage, [/service/](https://quotr.ai/service/)); 3–4 business days for estimates and 2–3 for pro formas ([/pricing/](https://quotr.ai/pricing/)); 1–3 business days ([llms.txt](https://quotr.ai/llms.txt)); 5–7 days (schema offer); 72 hours (Developer Desk post); "scope quote in 1 day, takeoffs in 1–2" (electrical services teaser); and one post claiming "3–4 business days by design" against offshore 24–48-hour shops | Every urgent page for ICPs 1, 3, 4, 5, 6, 8, 10 |
| 2. The 50,000 sq ft price tier | $0.25 per sq ft under 50,000 and $0.10 above. If the lower rate applies to the whole project, 49,000 sq ft costs **$12,250** and 50,000 costs **$5,000**. Subs also need a per-sheet or per-trade price ($7,500 for a 30,000 sq ft TI bid) | Price examples for ICPs 1, 3, 4, 6, 8, 10 |
| 3. Lender acceptance and independence | No lender statement. Service is sold to borrowers; Procurement supplies projects; no named credentialed reviewer; no E&O cover or reliance letter; no engineer partner | ICP6 lender page; all of ICP8 |
| 4. Security and data use | Only "industry-standard encryption"; no SOC 2 statement, retention policy or answer on whether drawings train models; SSO dropped from the listed Enterprise tier | ICP2, ICP4 and ICP8 decision pages |
| 5. Procurement tariff exposure | Categories sold, origin countries, importer of record, which duty layers the DDP price includes (most-favored-nation, Section 301 list, 301 forced-labor 12.5%, Section 232, Section 201, AD/CVD), rate-lock and repricing terms, exporters with low separate AD rates vs the 251.64% China-wide rate, January 1 entry-date rule | All of ICP9; ICP5, 3 and 7 cross-sell |
| 6. Procurement claims | Savings stated as "up to 50%," "40–50%" and "40–55%" (cards imply 44–60%); factory count "50+ audited," "220+ vetted" and "220+ incl. 30+ audited"; delivery "CA jobsite" vs "coast to coast" on the same page ([Quotr](https://quotr.ai/procurement/)); ~90-day delivery; 3–5-day quote; NFRC, CARB/TSCA and cUPC certifications per SKU; "Client saved ~$0" display bug | ICP9, 5, 7, 6 |
| 7. Software pricing hygiene | Retired $299.90 Solo and $499.90 Team plans still on ~13 URLs and in llms.txt against the live $79.90 Lite ([example](https://quotr.ai/blog/stack-alternative/)) | Every comparison page for ICPs 1, 2, 3, 5 |
| 8. Plus "2,000 sq ft takeoff credits" | Unclear whether these are Service credits (about $500 a month at $0.25) or software credits | ICP1, 3, 5 pricing pages |
| 9. Capabilities | GC-side sub-bid leveling; Procore, ACC and Excel integrations or export; labor-unit and assembly import from Accubid, ConEst, McCormick or QuoteSoft; SD/UniFormat conceptual estimates; Revit add-in and DWG support; residential plan-size limits; Lite support level; any Spanish interface or support | ICP2, 4, 10, 3 |
| 10. Proof permissions and data | Publishing aggregates behind "$1.2B+ estimated" (no method today); whether estimate-vs-bid outcomes are tracked; RL Electric numbers and location; BiltWise details; Salisbury Moore's firm type; named estimator credentials; any licensed staff | All four proof assets |
| 11. Entity facts | FireTips status on a legacy domain; Revit-era copy on F6S and Crunchbase; HQ Berkeley vs San Francisco; funding $3.5M vs $5M; founders listed one vs two ways (from the prior audit) | Brand prompts in all ICPs |
| 12. Geographic depth | Number of Quotr estimates by state, especially Texas and Florida | Texas and Florida spokes |
| 13. Trial terms | 7-day trial, "Cancel anytime — no charge if canceled" ([Quotr](https://quotr.ai/pricing/)); auto-renewal disclosures under California rules not researched; whether the trial clock can start at first upload | ICP1, 3, 5 decision pages |

## Known, likely and speculative across the ten ICPs

| Claim class | Known (cite freely, with source) | Likely (label as inference) | Speculative (validate first) |
|---|---|---|---|
| Market size | 83,342 electrical and 111,207 plumbing/HVAC establishments; 25,519 roofing; 20,760 drywall/insulation (CBP 2023 via aggregators); $453.5B bank C&D loans; 19,000+ architecture firms; ~11,400 LA homes destroyed | ~60k single-family GC establishments; ICP5 universe 150k–190k | ICP1 25k–45k plan-bidding firms; ICP2 6k–9.5k; ICP4 4k–7k; ICP9 unsized |
| Geography | CA/TX/FL lead estimators and permits; Seattle and DC estimator LQ and wages; Bay Area +$81/sq ft; Zone 0 and SB 840/SB 15 dates | Seven segments; CA hub first; one data-center page | Metro index values; Florida rules; DMA demand; engines adding geography |
| Psychology | Defaults, anchoring and fresh-start effects replicate ([Jachimowicz](https://ideas.repec.org/a/cup/bpubpo/v3y2019i02p159-186_00.html); [Dai, Milkman & Riis](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf)); social proof and choice overload are weak; data accuracy is the top contractor AI concern at 57% ([Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/)) | Anxiety dominates 7 of 10 ICPs, habit 3; hot weeknight and deadline moments | Exact hot hours; spouse role; Spanish search behavior |
| Triggers | Revu 20 EOL; Jan 1 tariff step-up; OZ 2.0 dates; Jan 7 ALE mark; FOMC Dec 9; +11.2% input prices | December pre-buy and January re-quote waves; New Year software buying | Construction bid seasonality; 2027 trade-show dates |
| Alternatives and pains | Review complaints on STACK, PlanSwift, Accubid, MeasureSquare, Buildertrend, ProEst; Handoff and Buildxact paywalls; Built AI PCR claims; insurer anchoring and fraud cases | Price and lock-in (subs), habit (residential), local data (developers) as top unmet needs | Frequency rankings beyond small snippet tallies |
| AI visibility | Quotr named in 1 of 32 unbranded Perplexity prompts; first but unnamed citation for outsourced-estimating price; 4 of 93 retrieval proxies | Directories and reviews gate trade-sub prompts; data gates cost prompts | Any timeline to first citation; Copilot and Claude weight for GC, lender and architect prompts |
| Buyer behavior | 51% of B2B buyers start in chatbots ([G2](https://company.g2.com/news/buyer-behavior-2026)); 94% fact-check AI and shortlist 2.7 vendors ([TrustRadius](https://www.prnewswire.com/news-releases/trustradius-2026-b2b-buying-disconnect-report-reveals-ai-has-changed-how-buyers-research-but-not-what-they-trust-302825792.html)); only 28% of construction firms have AI in production ([Bluebeam](https://www.financialcontent.com/article/gnwcq-2026-10-13-bluebeam-report-brings-constructions-ai-paradox-to-light-firms-running-ai-in-production-report-real-savings-but-only-28-have-gotten-that-far)) | Construction research starts in Google more often than chatbots today | Device split; construction-specific chatbot share |
| Quotr fit | Lite $79.90; Plus $299.90; Service $0.25/$0.10; Bay Area procurement cards; LA rebuild sample | Service fits ICP4, 6, 7, 10 hot chains; Lite fits ICP1, 3, 5 | Accuracy level; lender acceptance; SD capability; viable import categories |

## Conclusion

The deeper finding is that Quotr's AI-visibility gap differs in kind from one buyer to the next, so a single content playbook cannot close it. For trade subs it is a gate problem: directories, reviews and third-party lists decide the shortlist, and Quotr is not on them. For developers, rebuild owners, lenders and architects it is a data problem: the answer pools are thin, stale or conflicted, and one dated, method-backed number from Quotr's own jobs would out-evidence them. For importers it is an operations problem: tariff demand is real, but no page can promise a delivered price until Quotr states what that price includes. This reframes the prior audit's call for "original data." Quotr needs a few specific datasets, each wired to a named buyer chain, and the existing tracking set becomes useful once it carries those buyers' persona facts.

The second implication is about sequence. Quotr's own inconsistencies are the critical path: seven turnaround claims, a price tier with a $7,250 cliff, and three factory counts. Engines already repeat Quotr's prices anonymously, and buyers in seven of ten ICPs are held back mainly by anxiety. The cheapest gain in the whole system is therefore a single consistent, brand-attributed set of facts. The December–January window is a one-time chance to publish dated pages for Revu 20, the cabinet tariff and the LA anniversary before "2027" fan-outs start retrieving whoever got there first. After that, the system should be judged on distributions over three periods and checked against switch interviews.
