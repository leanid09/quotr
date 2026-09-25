# Construction cost questions, 2026 US market trends and benchmark data (California focus), as of 2026-09-25

Purpose: input for Quotr.ai's 50+ article GEO/SEO roadmap. These notes cover four things. First, which cost questions people ask most. Second, who answers them today, and how. Third, which 2026 market trends make specific cost topics timely. Fourth, which public datasets and methods Quotr could use to publish its own benchmarks. They end with a list of candidate articles.

How to read these notes:
- Everything under **Cited Findings** is **Observed**, meaning it was seen in a source. Everything under **Inferences** is **Inference**, meaning it is my reading of the evidence.
- Provenance tags on Observed items:
  - **(WS)**: seen in a WebSearch result summary or snippet. The page itself was not opened.
  - **(PX)**: seen in a live Perplexity Sonar answer or its citation list, run on 2026-09-25 via `mcp__Slashy__web_search`. Each prompt was run once.
  - **(prior)**: taken from the earlier audit notes in `/home/user/quotr/research_notes/Quotr GEO AEO strategy audit/` (`competitor_geo_benchmark.md` §3 and `verification_quotr_and_competitors.md`).
- Tool limits:
  - The egress proxy blocked WebFetch on every primary page I tried: nahb.org, eyeonhousing.org, calmatters.org, recovery.lacounty.gov, meltplan.com, homeguide.com, exayard.com and shovels.ai. I did not route around the block with other scraping tools. Page-level details such as bylines, update dates, methodology boxes and sample sizes therefore come from search snippets, or are listed as gaps.
  - quotr.ai and quotr.io were not accessed.
  - Calls used: 29 WebSearch calls (slightly above the 20–25 target) and 12 Perplexity checks.
  - Not tested: ChatGPT, Google AI Overviews/AI Mode, Gemini, Claude and Copilot.
- Dates: data older than 2026 carries its date in the text.

---

## 1. Which construction cost questions have the most demand in 2025–2026, and what is the evidence?

### Takeaway
No public keyword-volume figures turned up, so demand has to be read from proxies:
- search results for head terms are crowded with "2026"-dated pages;
- Perplexity pulls 15–38 sources per cost question;
- news coverage was heavy in September 2026 (LA fire rebuild, LA apartment costs, data centers, tariffs);
- remodeling surveys show strong homeowner spending plans.

On these proxies, the highest-volume consumer questions are cost to build a house (national and by state), ADU cost in California, and kitchen and bathroom remodel cost. The highest-value professional questions are also the least well answered today:
- LA fire rebuild cost and progress
- multifamily cost per unit by product type, especially in Los Angeles
- cost per square foot by trade
- tenant improvement cost in Los Angeles
- the dollar cost of California's 2025 Title 24 energy code

### Cited Findings
**Search results as a demand signal**
- (WS) The query "cost to build a house per square foot 2026" returned nine results, all with "2026" in the title:
  - a marketplace: [Opendoor](https://www.opendoor.com/articles/how-much-does-it-cost-to-build-a-house)
  - builder blogs: [Dunn & Stone](https://www.dunnandstonebuilders.com/knowledge-center/how-much-does-it-cost-to-build-a-house), [Holloway Family Homes](https://hollowayfamilyhomes.com/how-much-does-it-cost-to-build-a-house-per-square-foot-in-2026/), [Fin Home Contracting](https://finhomecontracting.com/blog/home-building/cost-per-square-foot-to-build-a-house-2026/), [Hafsa Building Group](https://hafsabuildinggroup.com/custom-home-cost-2026/)
  - an estimating firm: [estimators.us](https://estimators.us/average-cost-to-build-a-house/)
  - a single-topic site with pages by state, size and finish: [CostToBuildAHouse.com](https://costtobuildahouse.com/cost-to-build-a-house)
- (WS) Searching for public search-volume data on "cost to build a house" returned only keyword-tool landing pages ([Keywords Everywhere](https://keywordseverywhere.com/tools/search-volume-checker/)) and a contractor keyword study ([Contracting Empire](https://contractingempire.com/contractor-keyword-study/)). None gave a volume figure. A "most searched home services on Google" list exists, dated 2025 and not opened: [Hook Agency](https://hookagency.com/blog/most-searched-home-services/).

**AI answers as a demand signal (PX, 2026-09-25): how many sources Perplexity cited per question**

| Question | Sources cited |
|---|---|
| California house $/sq ft | 18 |
| Title 24 (2025 code) cost | 38 |
| SF/LA tenant improvement | 31 |
| SB 9 fourplex | 29 |
| California ADU | 25 |
| LA fire rebuild status | 21 |
| LA apartments per unit | 21 |
| Multifamily per unit by type | 20 |
| Texas vs Florida $/sq ft | 20 |
| Kitchen/bath remodel | 19 |
| Framing $/sq ft | 19 |
| Data center $/MW | 15 |

The individual sources are in the Section 2 table.

**News coverage as a demand signal**
- (PX citations) LA fire rebuild:
  - Pasadena Star-News, 2026-09-22: [six neighboring Altadena homes rebuilt in six months](https://www.pasadenastarnews.com/2026/09/22/sharing-in-the-planning-6-altadena-neighboring-homes-get-rebuilt-in-six-months/)
  - Daily News, 2026-09-25: [Malibu reaches 100-permit rebuilding milestone](https://www.dailynews.com/2026/09/25/malibu-reaches-100-permit-rebuilding-milestone-as-infrastructure-challenges-shape-fire-recovery/)
  - LA Times, 2026-09-15: [LA County had no plan to guide recovery, new report finds](https://www.latimes.com/california/story/2026-09-15/la-county-had-no-plan-to-guide-recovery-after-2025-fires-new-report-finds)
  - Pasadena Now: [More than 1,000 Altadena homes are rising; half the burn zone has yet to break ground](https://pasadenanow.com/main/more-than-1000-altadena-homes-are-rising-half-the-burn-zone-has-yet-to-break-ground) (date not captured)
  - (WS) Bloomberg 2026 feature: [The LA Fire Recovery Nightmare](https://www.bloomberg.com/features/2026-los-angeles-fire-recovery/)
- (PX citations) Los Angeles multifamily costs:
  - LA Times, 2026-09-22: [LA developers aren't building more apartments despite epic housing shortage](https://www.latimes.com/california/story/2026-09-22/la-developers-arent-building-more-apartments-despite-epic-housing-shortage)
  - The Real Deal, 2026-09-23: [Measure ULA, rising costs plaguing Los Angeles developers](https://therealdeal.com/la/2026/09/23/measure-ula-rising-costs-plaguing-los-angeles-developers/)
  - LA Times, 2026-09-11: [the California condo is dying](https://www.latimes.com/california/story/2026-09-11/california-condo-is-dying-why-its-making-housing-crisis-worse)
  - LA Times, 2026-09-23: [LA approves $466 million in affordable housing spending](https://www.latimes.com/california/story/2026-09-23/la-approves-466-million-in-affordable-housing-spending)
- (WS) Data centers: Axios, 2026-09-01, [data center construction spending surged in July](https://www.axios.com/2026/09/01/ai-data-center-constructon-spending); [ConstructConnect September 2026 Data Center Report](https://news.constructconnect.com/september-2026-data-center-report-year-to-date-spending-nearly-three-times-a-year-ago).
- (PX citations) San Francisco office build-outs: Bizjournals, 2026-09-24, [what tenants want in high-end offices](https://www.bizjournals.com/sanfrancisco/news/2026/09/24/what-tenants-want-in-high-end-offices.html); SF Standard, 2026-09-24, [office boom](https://sfstandard.com/2026/09/24/office-boom-san-francisco-housing-shortage/).

**Remodeling demand**
- (WS) One search summary drew on [HIRI](https://www.hiri.org/blog/homeowner-project-activity-trends), [Angi](https://www.angi.com/articles/most-popular-home-projects.htm) and [Opendoor](https://www.opendoor.com/articles/seven-best-home-improvements-of-2022). I did not verify which page each figure came from. The summary said:
  - homeowners planning projects in 2026 expected to spend about $7,117 on average, and nearly $24,000 on major renovations;
  - kitchens and guest bathrooms were each remodeled by 24% of homeowners;
  - about 32% of homeowners planned maintenance projects, with high mortgage rates cited as a reason to renovate instead of moving.
- (PX) For kitchens, Perplexity gave a national average of about $26,900–$27,000, with most homeowners spending $14,600–$41,600 ([realcostiq](https://realcostiq.com/data/average-kitchen-remodel-cost/), [Angi](https://www.angi.com/articles/how-much-should-kitchen-remodel-cost.htm)). For bathrooms it said it had "no strong search-result coverage" for 2026 and gave no figure.

**Earlier audit**
- (prior) A multifamily $/sq ft prompt cited [Meltplan](https://www.meltplan.com/blogs/construction-cost-per-square-foot-2026-us-benchmarks-by-building-type), [Exayard](https://exayard.com/blog/cost-to-build-apartment-complex), [RSMeans](https://www.rsmeans.com/resources/how-much-does-it-cost-to-build-an-apartment-complex), latestcost.com, buildmatinsight and BDC Network.
- (prior) A tariff prompt cited only government, association and media sources (JEC, Brookings, NAHB, Construction Dive).
- (prior) An "LA fire rebuild cost per sq ft 2026" prompt gave $400–$800+ per sq ft, citing Bloomberg and local contractors (Benson, Amerbuild, UBIC, Vaisman). Quotr was absent.

### Inferences
- Proxy-based demand ranking, since actual search volumes are unknown:

| Rank | Question cluster | Demand | Quotr fit |
|---|---|---|---|
| 1 | Cost to build a house per sq ft (national, CA, TX, FL) | Highest consumer volume; marketplaces own it | Medium: homeowners are not core buyers, but builders and subcontractors quote these numbers |
| 2 | California ADU cost (detached, garage conversion, JADU, prefab) | High, California-specific | High |
| 3 | Kitchen and bathroom remodel cost | High consumer volume; bathroom 2026 is under-served | Medium, through factory-direct cabinets, vanities and tile |
| 4 | LA fire rebuild cost and progress | Spiky, news-driven, high local intent | Very high: Quotr already sells a Residential LA Fire Rebuilding estimate |
| 5 | Multifamily cost per unit or per door by product type | Low volume, high value; answers are thin | Very high: developers and pro formas |
| 6 | Cost per sq ft by trade | Medium volume per trade, many long-tail variants | Very high: subcontractor customers and takeoff data |
| 7 | Duplex, triplex, fourplex and SB 9 | Low–medium, California-specific | High |
| 8 | Commercial tenant improvement cost | Medium, B2B | Medium–high for SF/LA tenant-improvement subcontractors |
| 9 | Data center cost per MW | High news interest, owned by institutions | Low, except for spillover effects on labor and materials |

- Fresh pages get used quickly. Perplexity cited articles published one to three days earlier (Bizjournals 2026-09-24; Daily News 2026-09-25), so a tracker updated monthly or more often can be picked up fast.

### Gaps
- No keyword volumes: Google Keyword Planner, Ahrefs, Semrush and Search Console were not available, and Google Trends was not queried. The ranking above rests on proxies only.
- No public study of AI prompt volume for construction cost questions was found.
- Only Perplexity was tested, with one run per prompt. Answers can change between runs.

---

## 2. Who owns these answers today in Google and AI answers? Format, freshness, data sources, and how small vendors got cited

### Takeaway
Ownership splits into three groups:
- **Consumer questions** ("cost to build a house," "remodel cost," "ADU cost") belong to cost marketplaces (HomeAdvisor/Angi, HomeGuide, Fixr), Opendoor and HomeLight, local builder blogs and, notably, Autodesk's blog.
- **Data center cost** belongs to large real estate and cost-consulting firms: JLL, Cushman & Wakefield, Turner & Townsend and CBRE.
- **Professional residential questions** have no authoritative owner. These are multifamily cost per unit, LA apartments, trade $/sq ft, LA tenant improvements, Title 24 cost and rebuild progress. Small vendors, brokers and contractors win them with dated pages built around tables, including Exayard, Meltplan, oneestimate.ai, clscre.com, terrapincg.com and LA rebuild contractors.

Several expected sources did not appear in any of the 12 answers: Forbes Home, Bankrate, RLB, Cumming, Mortenson and Turner Building Cost Index. RSMeans appeared only in an earlier-audit answer. Quotr appeared in none of the 12.

### Cited Findings
**AI answer audit (PX, 2026-09-25, one run each)**

| Prompt (short) | Answer given | Main sources cited | Quality flag |
|---|---|---|---|
| CA house $/sq ft incl. Bay Area and LA | CA $200–$500+; LA $400–$750 (custom); Bay Area $450–$950+ (SF/Marin $650–$950+, San Jose $550–$800) | [HomeAdvisor](https://www.homeadvisor.com/cost/architects-and-engineers/build-house-california/), [Fixr](https://www.fixr.com/costs/build-house-california), [HomeGuide](https://homeguide.com/costs/cost-to-build-a-house-in-california), [heyday.build](https://heyday.build/blog/cost-to-build-a-house-in-california/), [buildmatinsight](https://buildmatinsight.com/construction-cost/app-cost/california-house-construction-cost-regional-breakdown), [Barcci Builders](https://www.barccibuilders.com/blog/new-home-construction-cost-bay-area-2026), [City Ventures](https://cityventures.com/blog/average-cost-to-build-house-in-california-2026/), [HomeLight](https://www.homelight.com/blog/buyer-cost-to-build-a-house-in-california/), [Autodesk](https://www.autodesk.com/blogs/construction/how-much-does-it-cost-to-build-a-house-in-2026/) | Wide ranges and no primary data; no Title 24 or tariff context |
| Texas vs Florida $/sq ft | TX ~$150–$225; Opendoor table TX $162 vs FL $170 (includes contractor fees) | [Opendoor](https://www.opendoor.com/articles/how-much-does-it-cost-to-build-a-house), [realpha](https://www.realpha.com/blog/cost-to-build-a-house-in-texas), [HomeGuide TX](https://homeguide.com/costs/cost-to-build-a-house-in-texas), [texasestimate](https://texasestimate.com/residential-estimating-services/cost-to-build-a-home-in-texas/), [costtobuildhouse TX](https://www.costtobuildhouse.com/states/texas), [JDJ Consulting](https://jdj-consulting.com/construction-cost-per-square-foot-in-texas-the-2026-guide/), [Reddit r/Homebuilding](https://www.reddit.com/r/Homebuilding/comments/1u72ka6/anyone_care_to_share_custom_home_build_pricing_in/), [Fixr TX](https://www.fixr.com/costs/build-house-texas) | Florida is thin: the answer said Florida guidance was "less directly quoted" |
| CA ADU: detached vs garage conversion vs JADU | Detached $150k–$400k+; garage conversion $60k–$160k; JADU <$50k to ~$120k | Local builders ([Safeway Remodel](https://www.safewayremodel.com/blog/adu-cost-california-2026), [IMKAT](https://imkatconstruction.com/how-much-does-an-adu-cost-in-california-in-2026/), [YCD Studio](https://ycd.studio/blog/adu-cost-bay-area-2026), [ladu.co](https://www.ladu.co/articles/adu-cost-los-angeles)), calculators ([ADU Pilot](https://www.adupilot.com/tools/adu-cost-calculator), [aduzoning.org](https://www.aduzoning.org/adu-cost-calculator/)), [Samara](https://www.samara.com/insights/adu-cost-california), [Angi](https://www.angi.com/articles/how-much-do-adu-costs.htm), [LA Construction Compliance](https://www.laconstructioncompliance.com/adu-cost-los-angeles-2026-price-guide/), a press release on [WBOC](https://www.wboc.com/online_features/press_releases/construction-by-maya-urges-los-angeles-homeowners-to-understand-california-adu-rules-before-starting-fall/article_9f0fbad7-ef96-5edd-8e87-8da8c82b1dbe.html) | Very wide ranges; no official data (HCD); prefab not broken out |
| SB 9 fourplex in California | "$1.0M–$1.8M total"; SB 9 lot split $55k–$75k; Bay Area new build $600–$1,000/sq ft; LA Urban Lot Split fee $3,978 | [HomeAdvisor fourplex](https://www.homeadvisor.com/cost/architects-and-engineers/build-a-fourplex/) (national $400k–$1M, average $750k), [withpat](https://withpat.com/blog/sb9-lot-split-costs-2026), [Bay Area ADU Manager](https://bayareaadumanager.com/blog/sb-9-adu-stacking-bay-area-lot-split-2026), [LA Metro Home Finder](https://www.lametrohomefinder.com/blog/sb-9-lot-splits-bay-area-cities), [LA City Planning SB 9 FAQ](https://planning.lacity.gov/odocument/597fb369-6fbd-4148-a057-3f33233405d2/SB9FAQ2.7l.pdf), [HCD SB 9 fact sheet](https://www.hcd.ca.gov/sites/default/files/docs/planning-and-community/sb-9-fact-sheet.pdf), [DGS CCCI](https://www.dgs.ca.gov/RESD/Resources/Page-Content/Real-Estate-Services-Division-Resources-List-Folder/DGS-California-Construction-Cost-Index-CCCI), [oneestimate.ai calculator](https://oneestimate.ai/en/california/cost-calculator), [Terner Center](https://ternercenter.berkeley.edu/research-and-policy/2026-california-legislative-preview/) | Thin: the total is stitched together from national HomeAdvisor figures and CA sources, plus unrelated news citations |
| Multifamily per unit: garden vs podium vs wrap vs mid-rise | Garden $150k–$265k/unit; podium/wrap $240k–$485k; mid-rise $260k–$525k. Per sq ft: garden $130–$250, podium/wrap $200–$400+, mid-rise $250–$425 | [apers.app](https://apers.app/learn/asset-classes/multifamily/garden-vs-midrise-vs-highrise-density-economics), [irecruit](https://www.irecruit.co/guides/apartment-complex-construction-cost), [Visidex BidFlow](https://www.bidflow.visidex.com/articles/how-to-estimate-multifamily-buildout), [Meltplan](https://www.meltplan.com/blogs/construction-cost-per-square-foot-2026-us-benchmarks-by-building-type), [LandSouth](https://landsouth.com/which-multifamily-product-type-is-right-for-your-site/), [Terrapin CG](https://terrapincg.com/news/multi-family-wood-frame-construction-cost-per-unit-2026), [Inabnet (Tampa/Austin)](https://www.inabnet.com/news/multifamily-construction-cost-per-unit-tampa-austin-2026/), [PerEff (DFW cost per door)](https://pereff.com/insights/multifamily-ground-up-cost-per-door-dfw-2026), [Buildermuse](https://buildermuse.com/residential/apartment-building-cost-per-square-foot-2026/) | Aggregator and vendor pages only; no institutional data; mass timber absent |
| LA apartments per unit | $350k–$500k/unit for typical Type V wood-frame podium; $550k–$900k+ high-rise; hard cost $250–$350/sq ft | [CLS CRE](https://clscre.com/blog/ground-up-multifamily-construction-los-angeles-2026.html) (small brokerage blog, top source), [oneestimate.ai LA](https://oneestimate.ai/en/california/los-angeles) ($250–$450/sq ft), [irecruit](https://www.irecruit.co/guides/apartment-complex-construction-cost), [LinkedIn post](https://www.linkedin.com/posts/jeff-palmer-pmi_what-does-it-cost-to-build-a-non-trophy-westside-activity-7450331674287996928-lERY), [RAND (Apr 2025)](https://www.rand.org/news/press/2025/04/cost-to-build-multifamily-housing-in-california-more.html), [Multifamily Dive](https://www.multifamilydive.com/news/california-texas-housing-costs-construction-analysis/746113/), [BiggerPockets](https://www.biggerpockets.com/forums/24/topics/160796-new-construction-costs-for-apartment-buildings-in-la-county) | Thin: one small blog plus one AI-native vendor carry the answer |
| LA fire rebuilt homes and permits (Sept 2026) | "100 fully rebuilt Altadena homes as of July 7, 2026"; "3,728 permits issued in LA County"; also "fewer than a dozen" at one year and "33 of about 1,700 Altadena homes" | [PR Newswire via FT markets, 2026-09-21](https://markets.ft.com/data/announce/detail?dockey=600-202609211227PR_NEWS_USPRX____SF52804-1), [ca.gov LA fires tracker](https://www.ca.gov/lafires/track-progress/), [NBC News](https://www.nbcnews.com/news/us-news/year-la-area-wildfires-destroyed-thousands-homes-fewer-dozen-rebuilt-rcna252751), [AP](https://apnews.com/article/california-wildfires-la-altadena-rebuild-home-construction-c7bc38063fd8db94dc96522d9e60a836), [Yahoo](https://www.yahoo.com/news/articles/california-families-neighborhood-coming-back-111100722.html), [Grist](https://grist.org/housing/la-homes-not-rebuilt-after-last-years-wildfires/), [McKinsey](https://www.mckinsey.com/industries/real-estate/our-insights/how-los-angeles-can-accelerate-recovery-after-the-2025-wildfires) | Contradictory: four figures from different dates and areas; no single dated source |
| Kitchen and bath remodel 2026 | Kitchen about $26.9k–$27k average ($14.6k–$41.6k typical); no bathroom figure | [realcostiq](https://realcostiq.com/data/average-kitchen-remodel-cost/), cabinet sellers ([USA Cabinet Store](https://www.usacabinetstore.com/kitchen-remodeling-cost/), [Kitchen Cabinet Kings 2026 ROI report](https://kitchencabinetkings.com/2026-kitchen-roi-report), [CabinetSelect](https://cabinetselect.com/how-much-does-a-kitchen-remodel-cost/)), [Angi](https://www.angi.com/articles/how-much-should-kitchen-remodel-cost.htm), [NerdWallet](https://www.nerdwallet.com/home-ownership/home-improvement/learn/kitchen-remodel-cost), [Houzz](https://www.houzz.com/cost/9-cost-to-remodel-a-kitchen), [Block Renovation](https://www.blockrenovation.com/guides/cost/kitchen-remodel-cost), [Build-Folio calculator](https://build-folio.com/financing/kitchen-remodel-calculator/) | Bathroom 2026 gap; cabinet retailers get cited |
| Framing $/sq ft 2026 | $7–$16/sq ft of floor area (labor $4–$10, materials $3–$6); 2,000 sq ft house ≈ $14k–$32k (some sources $22k–$60k) | **[Exayard](https://exayard.com/blog/framing-cost-per-square-foot) (first citation)** plus [a second Exayard page](https://exayard.com/blog/cost-to-frame-a-house), [Angi](https://www.angi.com/articles/cost-to-frame-house.htm), [myBuildIQ](https://www.mybuildiq.com/en-us/blog/house-framing-cost-2026), [HomeAdvisor](https://www.homeadvisor.com/cost/walls-and-ceilings/install-carpentry-framing/), [CostFlowAI calculator](https://costflowai.com/calculators/framing/), [HomeGuide](https://homeguide.com/costs/cost-to-frame-a-house), [Buildermuse ("framing labor rates hit $12.50/sf")](https://buildermuse.com/residential/residential-framing-labor-rates-hit-1250sf-/) | Consistent across sources, but see the NAHB comparison under Inferences |
| Office tenant improvement 2026, SF Bay Area and LA | Bay Area standard $90–$180/sq ft (light $35–$80; high-end $200–$350+); SF fit-out $219–$228/sq ft; LA: none found, used CA-wide $100–$150 | [Arch General Construction](https://www.archgeneralconstruction.com/posts/bay-area-commercial-tenant-improvements-2026), [Bizjournals 2026-09-24](https://www.bizjournals.com/sanfrancisco/news/2026/09/24/what-tenants-want-in-high-end-offices.html), [Bisnow](https://www.bisnow.com/news/san-francisco/construction-development/san-francisco-san-jose-most-expensive-markets-office-improvements-134046), [Cushman & Wakefield Office Fit-Out Cost Guide](https://www.cushmanwakefield.com/en/united-states/insights/office-fit-out-cost-guide), [Burnette Co](https://burnetteco.com/tenant-improvement-cost/), [Allwork.space (Apr 2026)](https://allwork.space/2026/04/this-part-of-the-u-s-has-the-highest-office-build-out-costs-and-it-keeps-rising/) | No LA-specific 2026 benchmark |
| Data center $/MW 2026 | JLL about $11.3M/MW shell-and-core (global); C&W US average $17.6M/MW all-in excluding chips/GPUs, up 21%; AI builds $15M–$25M+/MW | [JLL](https://www.jll.com/en-us/insights/market-outlook/data-center-outlook), [C&W 2026 guide](https://ir.cushmanwakefield.com/news/press-release-details/2026/Cushman--Wakefield-Releases-2026-Data-Center-Development-Cost-Guide-Citing-21-Rise-in-Per-MW-Construction-Costs/default.aspx), [Turner & Townsend DCCI 2025–26](https://www.turnerandtownsend.com/en-us/insights/data-center-construction-cost-index-2025-2026/), [CBRE](https://www.cbre.com/insights/reports/global-data-center-trends-2026), [GlobeSt 2026-08-26](https://www.globest.com/2026/08/26/data-center-construction-costs-jump-21-as-23t-pipeline-takes-shape/) | Solid, and owned by institutions |
| Title 24 2025 cost of a new home | "Somewhat higher construction budget, lower long-term costs"; no dollar figure | [CEC news Jan 2026](https://www.energy.ca.gov/news/2026-01/californias-energy-code-update-guides-construction-cleaner-healthier-buildings), [CEC 2025 standards](https://www.energy.ca.gov/programs-and-topics/programs/building-energy-efficiency-standards/2025-building-energy-efficiency), [Title 24 Stakeholders 2025 cycle](https://title24stakeholders.com/cycle/2025/), [Hanson Bridgett](https://www.hansonbridgett.com/publications/251230_8187_construction-laws-2026) | Thin: no cost numbers anywhere |

**National "cost to build a house" search results (WS)**

A summary across the nine results listed in Section 1 gave the figures below. I did not verify which page supplied each one.
- $150–$250/sq ft for standard builds; more than $400/sq ft for custom homes in high-cost markets
- $185–$245/sq ft for a mid-range builder-grade home
- $200–$550+/sq ft for custom homes
- a national average home cost of $323,000, with most between $139,000 and $531,000
- "NAHB pegs … $162 per square foot for a 2,647-square-foot home, excluding land and contractor overhead"; adding a 15–25% contractor markup gives about $195/sq ft
- regional swings of 20–50%

NAHB's 2024 breakdown is also republished by third parties such as [ResiClub](https://www.resiclubanalytics.com/p/the-cost-breakdown-for-constructing-a-single-family-home-in-2024).

**LA fire rebuild cost pages (WS)**
- [LAGBS](https://www.lagbs.com/post/altadena-eaton-fire-rebuild-cost-2026): custom Altadena rebuilds in 2026 mostly run about **$450–$750/sq ft**, including architecture, engineering, permits and construction.
- Another contractor page in the same results gives **$485–$650+/sq ft** turnkey. Candidates are [Benson Construction Group](https://www.bensonconstructiongroup.com/fire-rebuild-los-angeles) and [Vaisman Construction](https://www.vaismanconstruction.com/fire-rebuild-resources/how-much-does-it-cost-to-rebuild-home-after-wildfire-los-angeles/); the attribution was not verified.
- [Bloomberg](https://www.bloomberg.com/features/2026-los-angeles-fire-recovery/): one Palisades example at about $650/sq ft, or about $2.6M for a 4,000 sq ft house.
- One contractor page claims insurance payouts in the Palisades run "$500–$600/SF short" of rebuild cost. This is an outlier and unverified.
- Other ranking guides:
  - [DWD Builders](https://www.dwdbuilders.com/intel/altadena-wildfire-rebuild-contractor-guide-2026) (covers permits, Chapter 7A and costs)
  - [AndHaus](https://www.andhaus.co/la-rebuild)
  - [UBIC](https://ubic.co/blog/cost-to-rebuild-a-home-in-altadena-after-the-eaton-fire)
  - [NPLD](https://nplinedesign.com/fire-damage-restoration-los-angeles)
  - [tect.com](https://www.tect.com/feeds/blog/average-cost-rebuild-house-fire)
  - [LA Construction Compliance](https://www.laconstructioncompliance.com/los-angeles-fire-rebuild-permits/)
  - [Alto Builders](https://altobuilds.com/altadena-fire-rebuild)
  - [My Heart Construction](https://www.myheartconstruction.com/blog/what-homeowners-in-altadena-need-to-know-about-rebuilding-after-a-fire)
- A data vendor, Shovels, published [LA Wildfires Recovery: What the Permit Record Shows](https://www.shovels.ai/blog/la-wildfire-rebuild-permit-data/), which ranks for permit questions.

**Small vendors' benchmark formats (WS)**
- A search summary attributed the following to the [Meltplan benchmark page](https://www.meltplan.com/blogs/construction-cost-per-square-foot-2026-us-benchmarks-by-building-type), though it blends in other results, so I did not verify the page-level attribution:
  - "Commercial construction costs $14 to $1,200+ per square foot **as of September 2026**"
  - building-type rows: pre-engineered metal building shells $14–$30/sq ft; self-storage $25–$170; dry warehouse $55–$175; cold storage $130–$350+; medical office $250–$450; quick-service restaurants $535–$850+; healthcare $200–$1,000+; data centers $600–$1,200+
  - "regional adjustments add or subtract 25 to 50 percent"; "soft costs add another 15 to 30 percent"
- Exayard runs a parallel page, [A Guide to Construction Cost Per Square Foot in 2026](https://exayard.com/blog/construction-cost-per-square-foot). Contractors publish the same format: [Terrapin CG](https://terrapincg.com/news/commercial-construction-cost-per-square-foot-by-building-type-2026) and [Buildermuse](https://buildermuse.com/commercial/commercial-construction-cost-per-square-foot-2026/).
- AI-native or software vendors cited in these answers:
  - Exayard: framing
  - Meltplan: multifamily and commercial
  - oneestimate.ai: California city pages and calculator
  - myBuildIQ and CostFlowAI: framing
  - Visidex BidFlow and apers.app: multifamily
  - constructionbids.ai: [RSMeans guide](https://constructionbids.ai/blog/rsmeans-construction-cost-data-guide) and [data center report](https://constructionbids.ai/data-center-construction-report-2026)
  - Autodesk: cited in the CA, framing and TX/FL answers
  - Archistar: [AI plan check blog](https://www.archistar.ai/blog/approved-building-permits/), which ranks for LA rebuild permitting

**Answer format and freshness (PX)**
- Every cost answer used the same structure:
  - a table of ranges, often split into budget, mid and high tiers;
  - regional rows;
  - caveats about scope ("hard cost vs all-in," "excludes land, financing, off-site utilities, fees," "unit size matters");
  - an offer to tailor the numbers to a city or size.
- Most cited pages carry "2026" in the URL or title, for example `...-bay-area-2026`, `...-cost-per-unit-2026`, `house-framing-cost-2026` and `...-dfw-2026`.

### Inferences
- How small vendors got cited. Six patterns recur:
  1. The year appears in the title and URL, plus an "as of" date (Meltplan).
  2. One range per product type in a table, with tiers and regional rows, which is the same shape Perplexity outputs.
  3. Explicit scope notes (hard vs all-in; exclusions).
  4. A narrow, local focus: a small LA brokerage (CLS CRE) is the lead source for LA apartment cost per unit, and Bay Area and Altadena builders win local prompts.
  5. Calculators and programmatic geography pages (oneestimate.ai city pages, CostToBuildHouse state pages, ADU calculators).
  6. Original data (the Shovels permit analysis, the United Policyholders survey, RAND) gets cited on news-driven questions.
- Institutional indexes (Turner, RLB, Mortenson, RSMeans City Cost Index) are not cited for $/sq ft or per-unit questions. They publish index levels and escalation rates, not $/sq ft by building type. Quotr can fill that gap by converting index movements plus its own estimate data into $/sq ft ranges for California product types.
- Consumer head terms (national "cost to build a house") are saturated by marketplaces and Opendoor. Quotr's better entry points are California-specific and professional questions whose current answers are thin, contradictory or rest on one small blog: multifamily per unit, LA apartments, LA rebuild, trade $/sq ft, Title 24 cost, bathroom 2026, LA tenant improvements and SB 9.
- Competitive risk: AI-native rivals are already building out programmatic cost pages (Exayard's trade pages, Meltplan's building-type benchmarks, oneestimate.ai's California city pages, CostFlowAI and myBuildIQ calculators). Each month Quotr waits lets their citation position harden.
- A possible definitional gap on framing:
  - NAHB's 2024 survey puts framing at 16.6% of construction cost ($428,215 × 16.6% ÷ 2,647 sq ft ≈ **$26.9/sq ft**, my arithmetic from the Section 4 figures).
  - The framing figure AI cites is **$7–$16/sq ft**.
  - The gap is probably definitional: NAHB's framing stage may include trusses, sheathing and roof framing. It is still a candidate "why estimates differ" article.

### Gaps
- Update dates, bylines, methodology statements and data sources could not be recorded for HomeGuide, Angi/HomeAdvisor, Fixr, Meltplan, Exayard or oneestimate.ai, because WebFetch was blocked for those domains.
- Google organic rank positions and Google AI Overviews citations were not measured. Neither were ChatGPT, Gemini, Claude or Copilot.
- Forbes Home and Bankrate were absent from all 12 Perplexity answers, but I did not check whether they rank in Google.
- Cumming, RLB and Mortenson cost pages were never cited, and I did not check whether they have consumer-facing $/sq ft pages.

---

## 3. Which 2026 market trends make specific cost topics timely?

### Takeaway
Seven trends in September 2026 make specific cost topics timely:
1. **Multifamily is contracting.** August starts fell 14.6% year over year, deliveries are forecast to drop 28% in 2026, and LA developers are publicly stalling.
2. **Mortgage rates are back at 7.03%** as of 2026-09-24.
3. **Input costs are up 8.9% year over year** (August), with lumber, steel, copper wire and switchgear each up more than 10%.
4. **Data center construction is booming**: about $75B a year, up 57% year over year. It is drawing skilled mechanical and electrical labor, as are immigration enforcement effects that 29% of firms report.
5. **New codes and laws are in force.** California's 2025 energy code applies to permits from 2026-01-01, and SB 79 transit upzoning took effect 2026-07-01.
6. **A tariff deadline is coming.** Cabinet and vanity duties are scheduled to rise from 25% to 50% on 2027-01-01.
7. **The LA fire rebuild has moved from permits to construction**, with contradictory progress figures and a documented insurance gap of $247/sq ft.

### Cited Findings
**Housing starts and permits (August 2026 data, released September 2026)**
- (WS) Total starts were 1,275,000 at a seasonally adjusted annual rate (SAAR). That is 2.6% below July's revised 1,309,000 and 1.2% below August 2025's 1,291,000 ([Census NRC August 2026](https://www.census.gov/construction/nrc/pdf/newresconst.pdf)).
- (WS) By segment ([NAHB, Sept 2026](https://www.nahb.org/news-and-economics/press-releases/2026/09/single-family-starts-rebound-but-market-challenges-persist); [Yield PRO](https://yieldpro.com/2026/09/multifamily-starts-and-completions-both-fall-again-in-august/): "multifamily starts and completions both fall again in August"):

| Series | Level (SAAR) | vs July | vs Aug 2025 |
|---|---|---|---|
| Single-family starts | 918,000 | +7.6% | +5.2% |
| Single-family permits | 878,000 | −1.8% | +1.3% |
| Multifamily starts | 357,000 | −21.7% | −14.6% |
| Multifamily permits | 516,000 | −4.3% | +7.5% |
| Permits in buildings of 5+ units | 467,000 | — | — |

- (WS) In May 2026, total starts fell 15.4% to 1.177M, the lowest since May 2020, and multifamily starts fell 40.2%, the steepest monthly drop since April 2009 ([Faris Capital Partners](https://www.fariscapitalpartners.com/blogs/housing-starts-hit-a-six-year-low-heres-why-apartment-investors-should-pay-close-attention); secondary source, verify against Census).

**Multifamily pipeline and sentiment**
- (WS) NMHC's June 2026 Quarterly Survey ([NMHC June 2026](https://www.nmhc.org/research-insight/nmhc-construction-survey/2026/quarterly-survey-of-apartment-construction--development-activity-june-2026/)):
  - 55% said starts were unchanged from three months earlier;
  - 46% expect improvement over the next 6–12 months, down from 68% in March 2026;
  - 14% expect decline, up from 5%.
- (WS) New multifamily deliveries are projected to fall 28% to 382,000 units in 2026 and another 24% in 2027. This comes from a search summary. It is probably [Apartments.com's 2026 supply outlook](https://www.apartments.com/grow/learning-center/supply-vacancy-outlook-2026), but I did not verify the attribution.
- (PX citations) Los Angeles coverage: LA Times 2026-09-22 (developers not building); The Real Deal 2026-09-23 (Measure ULA and rising costs); LA Times 2025-10-01, [apartment development pipeline dries up](https://www.latimes.com/business/story/2025-10-01/apartment-development-pipeline-dries-up-in-spite-of-demand-for-housing). Links are in Section 1.
- (WS) RAND, April 2025 ([press release](https://www.rand.org/news/press/2025/04/cost-to-build-multifamily-housing-in-california-more.html), [report RRA3743-1](https://www.rand.org/pubs/research_reports/RRA3743-1.html)):
  - multifamily costs **2.3×** as much to build in California as in Texas, and **1.5×** as much as in Colorado;
  - development fees average about **$29,000 per unit in CA**, $12,000 in CO and $1,000 in TX;
  - California projects take **more than 22 months longer** than in Texas;
  - California affordable housing costs **$640/sq ft**, against $228/sq ft for market-rate housing in Texas;
  - the sample covers **more than 140 completed projects**.

**Mortgage rates**
- (WS) Freddie Mac's 30-year fixed rate averaged 6.71% on 2026-09-03, 6.76% on 09-10, 6.95% on 09-17 and **7.03% on 09-24**, against 6.30% a year earlier ([Freddie Mac 7.03%](https://www.globenewswire.com/news-release/2026/09/24/3368592/0/en/mortgage-rates-average-7-03.html), [6.95%](https://www.globenewswire.com/news-release/2026/09/17/3364253/0/en/mortgage-rates-average-6-95.html), [PMMS](https://www.freddiemac.com/pmms)).

**Construction spending and the data center boom**
- (WS) Total construction spending in July 2026 was **$2,157.6 billion SAAR**. (The search summary said "trillion," which is a typo; the figure is in billions.) That is down 0.5% on the month and 3.8% on the year, the lowest since October 2023 ([MDM](https://www.mdm.com/news/top-distributor-sectors/building-materials-construction/july-u-s-construction-spending-falls-to-near-3-year-low-despite-data-center-boom/)).
- (WS) Data center construction ran at about **$75.2B SAAR in July 2026**, up 6.2% on the month and **57.2% on the year** ([Axios 2026-09-01](https://www.axios.com/2026/09/01/ai-data-center-constructon-spending); [yournews 2026-09-02](https://yournews.com/2026/09/02/7183957/u-s-data-center-construction-spending-jumps-nearly-60-as-ai/)).
- (WS) ConstructConnect ([report](https://news.constructconnect.com/september-2026-data-center-report-year-to-date-spending-nearly-three-times-a-year-ago)):
  - July 2026 data center starts totaled $2.7B across 23 projects;
  - year to date: 136 projects and **$84.1B**, nearly three times a year earlier;
  - new builds are shifting to the Midwest and South.
- (PX) Cushman & Wakefield's 2026 Data Center Development Cost Guide puts the US average at $17.6M/MW, excluding chips and GPUs, and reports per-MW construction costs up **21%** ([C&W](https://ir.cushmanwakefield.com/news/press-release-details/2026/Cushman--Wakefield-Releases-2026-Data-Center-Development-Cost-Guide-Citing-21-Rise-in-Per-MW-Construction-Costs/default.aspx); [GlobeSt 2026-08-26](https://www.globest.com/2026/08/26/data-center-construction-costs-jump-21-as-23t-pipeline-takes-shape/)).
- (PX citations) California passed a data center oversight package in September 2026: [Reuters 2026-09-21](https://www.reuters.com/legal/litigation/california-governor-signs-broad-data-center-oversight-bill-package-2026-09-21/), [The Register 2026-09-22](https://www.theregister.com/ai-and-ml/2026/09/22/california-tightens-datacenter-rules-on-water-and-power/5298028), [CalMatters](https://calmatters.org/economy/technology/2026/09/new-california-laws-data-centers/). I saw only the headlines.

**Material prices and tariffs**
- (WS) ABC's analysis of BLS producer price index (PPI) data ([Construction Citizen](https://constructioncitizen.com/blog/abc-construction-materials-prices-jump-again-august/2609161), [Roofing Contractor](https://www.roofingcontractor.com/articles/102682-construction-material-prices-surge-in-august), [HVAC/P July](https://hvacpproducts.com/2026/08/abc-construction-materials-prices-flat-in-july-up-7-4-from-a-year-ago/)):
  - construction input prices rose **1.2%** in August 2026 and are up **8.9% year over year**;
  - nonresidential inputs are up 8.8% year over year;
  - iron and steel, softwood lumber, **switchgear**, and **copper wire and cable** are each up more than 10%;
  - July 2026 was flat on the month and up 7.4% on the year.
- (WS) Section 232 wood-products tariffs ([Wiley](https://www.wiley.law/alert-White-House-Imposes-Section-232-Tariffs-on-Imports-of-Timber-Lumber-and-their-Derivative-Products); [GHY](https://www.ghy.com/trade-compliance/us-tariffs-lumber-upholstered-furniture-cabinets-vanities/); [Green Worldwide](https://www.greenworldwide.com/new-section-232-wood-product-tariffs-effective-october-14-2025/)):
  - effective **2025-10-14**: 10% on softwood lumber and timber, **25% on kitchen cabinets and vanities**, 25% on upholstered furniture;
  - a **2025-12-31 proclamation delayed** the scheduled 2026-01-01 increases (cabinets and vanities to 50%, upholstered furniture to 30%) until **2027-01-01**, citing trade negotiations ([CNN 2026-01-01](https://www.cnn.com/2026/01/01/business/trump-furniture-tariff-delay-intl-hnk), [NAHB Jan 2026](https://www.nahb.org/blog/2026/01/wood-product-tariff-delays), [Thompson Hine](https://www.thompsonhinesmartrade.com/2026/01/president-trump-delays-section-232-tariff-increase-on-wood-furniture-cabinets-and-vanities/), [Federal Register 2026-01-09](https://www.federalregister.gov/documents/2026/01/09/2026-00327/amendments-to-adjusting-imports-of-timber-lumber-and-their-derivative-products-into-the-united)).
  - **Conflict:** another search summary said the 50% rate took effect on 2026-01-01. The sources above contradict it, so treat 25% as the 2026 rate.
- (WS) Cabinets and furniture of Chinese origin may face effective rates above 70% once Section 232 is stacked on Section 301 and antidumping/countervailing duties, depending on classification (trade-compliance summary; not verified). Source set: [GHY](https://www.ghy.com/trade-compliance/us-tariffs-lumber-upholstered-furniture-cabinets-vanities/), [NextDAY Cabinets](https://nextdaycabinets.com/kitchen-cabinet-tariffs-in-2026-what-contractors-and-builders-need-to-know-about-section-232-tariff-updates/).
- (prior) The Joint Economic Committee's April 2026 housing report estimated tariffs add $7,500–$10,900 per home ([JEC](https://www.jec.senate.gov/public/_cache/files/fe5d79b2-97cb-4c55-aeba-3e31fdd235fd/april-2026-final-jec-report-on-housing.pdf)). NAHB also posted on tariff relief in September 2026 ([NAHB](https://www.nahb.org/blog/2026/09/tariff-relief-building-materials)); I did not read that post.

**Cost indexes**
- (WS) **Turner Building Cost Index**, Q2 2026 ([Construction Dive](https://www.constructiondive.com/news/turners-building-cost-index-q2-2026/826514/), [Turner](https://www.turnerconstruction.com/insights/high-growth-sectors-continue-to-drive-u-s-construction-activity)):
  - index at **1552**, up 1.44% on the quarter and 5.15% on the year (nonresidential, US);
  - demand is strongest in data centers, semiconductors and advanced manufacturing;
  - the biggest challenge is "availability of skilled Mechanical and Electrical labor."
- (WS) **RLB North America**, Q2 2026 report, released 2026-06-29 ([RLB](https://www.rlb.com/americas/insight/rlb-construction-cost-report-north-america-q2-2026/), [GlobeNewswire](https://www.globenewswire.com/news-release/2026/06/29/3318960/0/en/RLB-North-America-Releases-Q2-2026-Construction-Cost-Report.html)):
  - national index at **288.58**, up from 285.47, or about 1.1% on the quarter (my arithmetic);
  - national backlog at **8.8 months**, lifted by data centers;
  - supply pressure attributed to transport and fuel costs from shipping re-routed around Middle East conflicts.
- (WS) **Mortenson**, Q1 2026 ([Mortenson](https://www.mortenson.com/news-insights/construction-cost-index-q1-2026)):
  - nonresidential costs up **1.69%** on the quarter and **6.77%** on the year;
  - year-over-year components: materials +7.0%, trade partner work +6.6%;
  - quarterly change by city: Seattle +0.56%, Portland +0.86%, Minneapolis +1.10%, Chicago +1.53%, Phoenix +1.97%, Milwaukee +2.19%, Denver +2.44%, Salt Lake City +3.38%;
  - drivers cited: data center and manufacturing demand, and long lead times for electrical and power-distribution equipment;
  - a [Q3 2026 edition](https://www.mortenson.com/news-insights/construction-cost-index-q3-2026) exists, but I did not read it.

**Labor and immigration enforcement**
- (WS) The 2026 AGC of America–NCCER Workforce Survey, released 2026-09-03 ([AGC](https://www.agc.org/news/2026/09/03/construction-workforce-shortages-remain-acute-despite-soft-market-conditions-data-centers-strain), [ENR](https://www.enr.com/articles/61266-increased-ice-enforcement-adds-to-constructions-labor-shortage-woes-agc-survey-finds)):
  - 1,830 responses, collected July 8 to August 14, 2026;
  - 87–90% of firms reported difficulty filling salaried or hourly craft positions;
  - about **29%** reported at least one direct or indirect impact from immigration enforcement in the past six months;
  - 16% said their subcontractors lost workers, and 12% said workers left or failed to appear;
  - 28% did data center work in the past 12 months. Of those, **58%** saw more competition for skilled workers and **49%** saw more wage pressure;
  - firms in the South reported the most enforcement impact and the Northeast the least.

**Insurance and the LA fire underinsurance gap**
- (WS) United Policyholders' one-year LA fire survey ([UP](https://uphelp.org/united-policyholders-la-wildfires-year-one-survey-report/), [UP advocacy post](https://uphelp.org/united-policyholders-one-year-los-angeles-fire-survey-the-kind-of-advocacy-policyholders-deserve/)):
  - **69%** of total-loss respondents lacked enough insurance to rebuild;
  - the **average underinsurance gap was $247/sq ft**;
  - 24% still did not know whether they were underinsured;
  - 64% reported claim problems. Of those, 69% cited communication delays, 68% payment delays and **61% an inadequate replacement-cost estimate from the insurer**, and 43% had to restart when their adjuster changed.
- (WS) Insurance Journal, 2026-01-20: [LA Fire Survivors Got a Rude Surprise That Could Hit More Americans](https://www.insurancejournal.com/news/west/2026/01/20/854686.htm).

**Energy codes**
- (PX) California's 2025 Energy Code applies to projects permitted on or after **2026-01-01**. The California Energy Commission (CEC) says it will cut bills by "nearly half" compared with the latest national standards and save $4.8B over 30 years. It pushes heat pumps and smarter controls, and in some cases solar PV and battery storage ([CEC Jan 2026](https://www.energy.ca.gov/news/2026-01/californias-energy-code-update-guides-construction-cleaner-healthier-buildings), [CEC standards page](https://www.energy.ca.gov/programs-and-topics/programs/building-energy-efficiency-standards/2025-building-energy-efficiency), [DGS BSC bulletin](https://www.dgs.ca.gov/-/media/Divisions/BSC/06-News/Information-Bulletins/2025/BSC-Bulletin-25-01-FINAL.pdf)). The AI answer gave no incremental dollar cost.
- (WS) 2024 IECC (national model energy code):
  - A DOE analysis says it could add up to about **$14,000** per typical single-family home, depending on the state. It puts the total at $57B if every state adopted it, compared with current state codes. It also cites more than $9.2B a year in added costs relative to 2006 code levels ([DOE](https://www.energy.gov/articles/energy-department-analysis-finds-proposed-international-building-codes-would-cost); [Roofing Contractor](https://www.roofingcontractor.com/articles/102650-doe-says-2024-energy-code-could-add-billions-in-housing-costs)).
  - The Southwest Energy Efficiency Project (SWEEP) disputes the analysis ([SWEEP](https://www.swenergy.org/the-cost-of-energy-codes-is-the-doe-missing-the-big-picture/)).
  - Adoption is limited: Illinois adopted the 2024 IECC in November 2025, Rhode Island has adopted it, and most states remain on older versions ([IMT 2026 outlook](https://imt.org/news/2026-energy-codes-outlook/)).

**California housing laws**
- (WS) **SB 79** was signed 2025-10-10 and takes effect in incorporated cities on **2026-07-01**:
  - allows housing up to **95 ft** and **160 units per acre** near qualifying transit, regardless of local zoning (these are the top-tier maximums);
  - applies only in 10 counties: Alameda, Contra Costa, Los Angeles, Orange, Sacramento, San Bernardino, Santa Clara, San Diego, San Francisco and San Mateo;
  - lets cities adopt implementing ordinances that exclude some parcels;
  - includes tenant protections.

  Sources: [Holland & Knight](https://www.hklaw.com/en/insights/publications/2025/10/california-gov-gavin-newsom-signs-sb-79), [H&K June 2026 implementation tracker](https://www.hklaw.com/en/insights/publications/2026/06/tracking-sb-79-implementation-before-the-train-leaves-the-station), [Manatt](https://www.manatt.com/insights/newsletters/client-alert/sb-79-transformative-upzoning-near-transit-in-california), [Buchalter](https://www.buchalter.com/insights/high-density-transit-zones-california-authorizes-transit-oriented-development-with-senate-bill-79/), [Coblentz](https://www.coblentzlaw.com/unfamiliar-terrain/coming-to-a-major-transit-stop-near-you-upzoning-under-sb-79/), [CA YIMBY](https://cayimby.org/legislation/sb-79/). Law firms dominate this topic.
- (PX) **SB 9**: Los Angeles charges a **$3,978** Parcel Map Urban Lot Split application fee before surcharges and other agency fees ([LA City Planning SB 9 FAQ](https://planning.lacity.gov/odocument/597fb369-6fbd-4148-a057-3f33233405d2/SB9FAQ2.7l.pdf)). HCD's SB 9 fact sheet was also cited ([HCD](https://www.hcd.ca.gov/sites/default/files/docs/planning-and-community/sb-9-fact-sheet.pdf)).
- (WS) **ADUs**:
  - Los Angeles County accounts for nearly 60% of ADUs produced statewide since 2018, per HCD Annual Progress Report data. The attribution comes from a search summary ([HCD APR dashboard](https://www.hcd.ca.gov/housing-open-data-tools/apr-dashboard)).
  - ADU permits rose from about 6,000 in 2018 to almost 16,000 in 2019 (older data).
  - HCD published a 2025 update to its ADU handbook ([HCD ADU handbook](https://www.hcd.ca.gov/sites/default/files/docs/policy-and-research/adu-handbook-update.pdf)).
  - ABAG hosted a session on 2025 Annual Progress Reports and HCD's ADU affordability survey findings ([ABAG](https://abag.ca.gov/technical-assistance/2025-annual-progress-reports-update-hcd-adu-affordability-survey-findings)).
- (PX citations) Governor's legislative updates in September 2026 ([2026-09-14](https://www.gov.ca.gov/2026/09/14/governor-newsom-signs-legislation-9-14-2026/), [2026-09-18](https://www.gov.ca.gov/2026/09/18/governor-newsom-issues-legislative-update-9-18-26/)) and the [Terner Center 2026 California legislative preview](https://ternercenter.berkeley.edu/research-and-policy/2026-california-legislative-preview/). I did not read their housing content.

**LA fire rebuild: status, permitting and cost**
- (WS) Early 2026:
  - more than **2,600 residential permits** had been issued across the Palisades and Altadena, about one for every five of the nearly **13,000 homes lost**;
  - another 3,340 were under review;
  - fewer than 20% of burned homes had permits ([CalMatters, Jan 2026](https://calmatters.org/housing/2026/01/la-fires-rebuild-permitting/)).
- (WS) Rebuild permits were issued in fewer than three months on average. Single-family and ADU permits came "three times faster" than in the five years before the fires ([Governor 2025-11-19](https://www.gov.ca.gov/2025/11/19/governors-actions-and-local-efforts-push-permit-approvals-for-la-fire-recovery-forward-at-rapid-pace); [CalMatters](https://calmatters.org/housing/2026/01/la-fires-rebuild-permitting/)). The search summary blended the two sources.
- (WS) Altadena permit activity peaked in October 2025 at **1,954 permits**, more than five times its pre-fire baseline of 382 a month. This is probably from [Shovels](https://www.shovels.ai/blog/la-wildfire-rebuild-permit-data/), which I did not verify, and probably counts all permit types.
- (WS) LA County relaunched its [Permitting Progress Dashboard](https://recovery.lacounty.gov/rebuilding/permitting-progress-dashboard/) in December 2025. It tracks more than **12,000 rebuild projects across seven phases** and refreshes every three hours. The dashboard itself was blocked for WebFetch.
- (WS) Completion counts over time:
  - Nov 2025: fewer than 0.1% of homes completed (search summary; source unclear).
  - Early Jan 2026, one year on: fewer than a dozen homes rebuilt and about 900 under construction ([NBC](https://www.nbcnews.com/news/us-news/year-la-area-wildfires-destroyed-thousands-homes-fewer-dozen-rebuilt-rcna252751), [AP](https://apnews.com/article/california-wildfires-la-altadena-rebuild-home-construction-c7bc38063fd8db94dc96522d9e60a836)).
  - March 2, 2026: 13 rebuilt, 1 in Pacific Palisades and 12 in the Eaton area ([California Globe](https://californiaglobe.com/fr/los-angeles-palisades-fire-rebuilds-13-total/)). The summary's wording was garbled.
  - (PX) July 7, 2026: **100 Altadena homes fully rebuilt**, per the county dashboard as quoted in a 2026-09-21 press release.
  - (PX) Also reported: 3,728 permits countywide ([ca.gov tracker](https://www.ca.gov/lafires/track-progress/), date of figure unknown) and "33 of about 1,700 Altadena homes" rebuilt ([Yahoo](https://www.yahoo.com/news/articles/california-families-neighborhood-coming-back-111100722.html), date unknown).
  - September 2026: Malibu issued its 100th rebuild permit ([Daily News 2026-09-25](https://www.dailynews.com/2026/09/25/malibu-reaches-100-permit-rebuilding-milestone-as-infrastructure-challenges-shape-fire-recovery/)).
- (WS) **AI plan check.** On 2025-04-30 the Governor launched Archistar's AI tool (eCheck, now "AI PreCheck"). It checks designs against local zoning and building codes before submission. It is free to LA City and County through LA Rises and Steadfast LA, with contributions from Autodesk and Amazon ([Governor](https://www.gov.ca.gov/2025/04/30/governor-newsom-announces-launch-of-new-ai-tool-to-supercharge-the-approval-of-building-permits-and-speed-recovery-from-los-angeles-fires/), [Archistar LA](https://www.archistar.ai/losangeles/), [StateScoop](https://statescoop.com/california-ai-pilot-building-permits-la-wildfires/)). It is used in LA and Malibu ([Letter Four](https://www.letterfour.com/blog/accelerating-fire-recovery-with-ai-plan-check-in-los-angeles-la-county-and-malibu)). LA County Public Works presented "Rebuilding Together Using AI-Assisted Plan Check" on 2026-03-13 ([LA County DPW deck](https://file.lacounty.gov/SDSInter/dpw/recovery/1204847_RebuildingTogether_Archistarv2DRAFTPPT31126.pdf)).
- (WS) **Self-certification.** Mayor Bass's Emergency Executive Order No. 6 (2025-04-22) created LADBS's first plan-check self-certification pilot for Palisades rebuilds ([EO 6](https://dbs.lacity.gov/sites/default/files/efs/pdf/publications/EO-6-Emergency-Executive-Order-Self-Certification-Pilot-Program.pdf), [LADBS pilot page](https://dbs.lacity.gov/self-certification-pilot-program), [Mayor: expansion](https://mayor.lacity.gov/news/mayor-bass-expands-las-first-ever-self-certification-pilot-program-further-expedite-palisades), [Mayor: standard plans](https://mayor.lacity.gov/news/mayor-bass-announces-first-approvals-under-new-standard-plan-pilot-program-further-expedite), [Mayor: first certificate of occupancy](https://mayor.lacity.gov/news/mayor-bass-announces-first-certificate-occupancy-issued-home-being-rebuilt-pacific-palisades)):
  - California-registered architects with at least three years of registration certify that plans meet the California Residential Code;
  - those plans skip plan check, but buildings are still inspected;
  - the pilot was later expanded to licensed civil engineers;
  - LADBS also runs a Standard Plan pilot;
  - the Mayor announced the first certificate of occupancy for a Palisades rebuild (date not captured).
  - LADBS also publishes a self-certification guide for commercial tenant improvements ([LADBS TI guide](https://dbs.lacity.gov/sites/default/files/efs/pdf/publications/Self-Certification-Implementation-Guide-Commercial-Tenant-Improvements.pdf)).
- (WS) **Codes.** About 1,000 more Eaton Fire properties must follow wildfire building codes if their permits are approved in 2026 ([LAist](https://laist.com/brief/news/climate-environment/altadena-los-angeles-homes-rebuild-fire-resistant)). Contractor guides cover Chapter 7A requirements ([DWD Builders](https://www.dwdbuilders.com/intel/altadena-wildfire-rebuild-contractor-guide-2026)). LA County publishes minimum submittal requirements for rebuilds ([LA County DPW PDF](https://dpw.lacounty.gov/bsd/lib/fp/Building/Residential/Fire%20Rebuild%20Minimum%20Submittal%20Requirements.pdf)).
- Rebuild cost per sq ft and insurance gap: see Section 2 (**$450–$750/sq ft** custom Altadena; **$485–$650+** turnkey; a Palisades example at about **$650/sq ft**) and the United Policyholders figures above (**$247/sq ft** average gap).

### Inferences
Timeliness map for the content plan:

| Topic | Window | Why |
|---|---|---|
| LA fire rebuild | Now through at least 2027 | Rebuilds have moved from permits to construction (100 Altadena completions by July 2026; Malibu's 100th permit in Sept 2026). Official and media counts conflict, AI answers mix them, and the $247/sq ft insurance gap makes rebuild estimates decision-critical. A monthly, dated tracker is a clear opening. |
| Cabinet and vanity tariffs | Q4 2026, before 2027-01-01 | The scheduled jump from 25% to 50% gives a dated news peg for landed-cost content, which fits Quotr's factory-direct procurement. |
| Title 24 cost | Now | The code has been in force since 2026-01-01. AI answers have no dollar figures, so the first credible line-item cost comparison can own the answer. |
| Multifamily cost and SB 79 feasibility | Next 3–9 months | Starts and deliveries are falling while developers re-underwrite 2027–2028 starts. SB 79 has been live since 2026-07-01, and law firms own the legal explainers but not the cost side. |
| Labor and materials escalation | Ongoing | Inputs are up 8.9% year over year, switchgear and copper are up more than 10%, and the AGC survey shows data center and immigration pressure. Subcontractors need escalation guidance, and a Quotr take on "labor $/sq ft by trade" is timely. |
| Remodel, ADU and garage conversion | Now | With mortgage rates at 7.03% as of 2026-09-24, the renovate-instead-of-move story gets stronger. |
| Data centers | Spillover only | Institutions own $/MW. Quotr's opening is how data centers raise electrical and mechanical costs and lead times for residential and commercial subcontractors. |

### Gaps
- **2025 CEQA reforms** (the budget trailer bills signed in mid-2025) were not researched or verified this session.
- **ADU law changes for 2025–2026** were not verified. Only the HCD 2025 handbook update and an ADU contractor's legislation page ([ADU West Coast](https://aduwestcoast.com/adu-legislation-2025-key-changes-homeowners/)) surfaced, and neither was read.
- **Current LA County dashboard numbers** (September 2026) could not be read directly because WebFetch was blocked. Every rebuild count above is second-hand and dated as noted.
- **Broader insurance costs** were not researched: builder's risk premiums, the California FAIR Plan, and homeowners insurance availability as a cost factor.
- **The September 2026 NAHB "tariff relief" post** was not read. The legal status of other (non-232) tariffs was not checked.
- **Cumming's 2026 market reports and ENR's cost indexes** were not found or checked.
- **The DOE 2024 IECC analysis** has no captured publication date.

---

## 4. Which public datasets and methods could Quotr use for credible, repeatable cost benchmarks, and what do credible benchmark pages disclose?

### Takeaway
Quotr can build credible benchmarks by combining three layers:
1. **Its own estimate data.** Quotr claims $1.2B+ estimated and 300+ projects a month.
2. **Public anchors for structure and cross-checks:** NAHB's cost shares and stage breakdown, Census starts, spending and home-size series, RAND's California multifamily study, and Cushman & Wakefield's tenant-improvement and data center guides.
3. **Public escalation and location series for updates:** BLS PPI via ABC, Turner, RLB and Mortenson indexes, the RSMeans City Cost Index, and California's DGS construction cost index.

Credible publishers disclose the same things every time: date or period, sample size, geography, unit definition, inclusions and exclusions, index base, and what drives changes.

### Cited Findings
**Candidate datasets**

| Dataset | Latest seen | What it gives | Source |
|---|---|---|---|
| NAHB *Cost of Constructing a Home* (biennial builder survey) | 2024 survey, published 2025-01-20 | Construction cost **64.4%** of sale price (record since 1998; 60.8% in 2022); finished lot 13.7% (17.8% in 2022); overhead 5.7%; commissions 2.8%; financing 1.5%; marketing 0.8%; profit 11.0%. Average construction cost **$428,215 ≈ $162/sq ft** (series high). Stages: interior finishes 24.1%, major system rough-ins 19.2%, framing 16.6%, exterior finishes 13.4%, foundations 10.5%, site work 7.6%, final steps 6.5%, other 2.1%. Average home about 2,647 sq ft (WS). | [NAHB special study](https://www.nahb.org/news-and-economics/housing-economics-plus/special-studies/special-studies-pages/cost-of-constructing-a-home-in-2024), [Eye on Housing](https://eyeonhousing.org/2025/01/cost-of-constructing-a-home-in-2024/), [NAHB blog](https://www.nahb.org/blog/2025/01/cost-of-construction-survey-2024) (WS; pages blocked) |
| Census New Residential Construction (monthly) | August 2026 | Starts, permits and completions by structure type and region | [Census NRC](https://www.census.gov/construction/nrc/current/index.html) |
| Census Construction Spending, C30 (monthly) | July 2026 | Spending by type, including a data center category | [Census C30 release PDF (July 2025 edition, shown only as an example of the format)](https://www.census.gov/construction/c30/pdf/pr202507.pdf); the July 2026 figures above came through [MDM](https://www.mdm.com/news/top-distributor-sectors/building-materials-construction/july-u-s-construction-spending-falls-to-near-3-year-low-despite-data-center-boom/) and [Axios](https://www.axios.com/2026/09/01/ai-data-center-constructon-spending); [Our World in Data series](https://ourworldindata.org/grapher/monthly-spending-data-center-us) |
| Census Characteristics of New Housing (annual, from the Survey of Construction) | 2025 data, published 2026-07-01 (WS) | Median completed new single-family home **2,142 sq ft in 2025**, the smallest since 2009 and 13% below the 2015 peak of 2,467 (WS). NAHB's quarterly medians for 2025 **starts** ranged 2,125–2,190 sq ft, a different measure. | [Census CHARS](https://www.census.gov/construction/chars/), [Eye on Housing](https://eyeonhousing.org/2026/03/small-gains-for-new-single-family-home-size/) |
| BLS Producer Price Index (monthly), as analyzed by ABC | August 2026 | Input price indexes by commodity (lumber, steel, copper wire, switchgear) | [ABC via Construction Citizen](https://constructioncitizen.com/blog/abc-construction-materials-prices-jump-again-august/2609161) |
| Turner Building Cost Index (quarterly, nonresidential, US) | Q2 2026 = 1552 | National nonresidential escalation and drivers | [Turner cost index](https://www.turnerconstruction.com/cost-index), [Q1 2026 PDF](https://turnerconstruction.com/uploads/cost-index-Q1-2026.pdf) |
| RLB Construction Cost Report (quarterly) | Q2 2026, national 288.58 | National and city indexes, backlog indicator, market commentary. City detail (LA, SF) is in the full report, which I did not read. | [RLB Q2 2026](https://www.rlb.com/americas/insight/rlb-construction-cost-report-north-america-q2-2026/) |
| Mortenson Construction Cost Index (quarterly) | Q1 2026 read; Q3 2026 exists | National plus eight metros, none in California. Splits materials from trade partner work. | [Mortenson index](https://www.mortenson.com/cost-index) |
| RSMeans City Cost Index (Gordian) | 2026 data and books | Location factors from a composite model: **9 building types, 66 materials, 21 trades, 6 equipment items**, weighted by actual usage. Factors convert national averages to local rates for "over 370 local markets" (Gordian). A third party says RSMeans tracks 97,000+ unit-cost line items across 970 locations; the counts conflict. | [Gordian CCI explainer](https://www.gordian.com/resources/city-cost-index-everything-need-know/), [Gordian localizing](https://www.gordian.com/resources/localizing-estimates-city-cost-index/), [constructionbids.ai](https://constructionbids.ai/blog/rsmeans-construction-cost-data-guide), [2026 book](https://www.rsmeans.com/products/books/2026-cost-data-books/2026-building-construction-costs-book) |
| California DGS Construction Cost Index (CCCI) | Not read | California state cost index; cited twice by Perplexity | [DGS CCCI](https://www.dgs.ca.gov/RESD/Resources/Page-Content/Real-Estate-Services-Division-Resources-List-Folder/DGS-California-Construction-Cost-Index-CCCI) (PX citation; methodology not verified) |
| RAND, *High Cost of Producing Multifamily Housing in California* | April 2025 | CA vs TX vs CO cost/sq ft, fees per unit, timelines; more than 140 completed projects | [RAND report](https://www.rand.org/pubs/research_reports/RRA3743-1.html), [PDF](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA3700/RRA3743-1/RAND_RRA3743-1.pdf) |
| Cushman & Wakefield Office Fit-Out Cost Guide; Data Center Development Cost Guide | 2026 | Tenant-improvement $/sq ft by market (SF $219–$228, PX); $/MW with exclusions stated | [Fit-out guide](https://www.cushmanwakefield.com/en/united-states/insights/office-fit-out-cost-guide), [DC guide](https://ir.cushmanwakefield.com/news/press-release-details/2026/Cushman--Wakefield-Releases-2026-Data-Center-Development-Cost-Guide-Citing-21-Rise-in-Per-MW-Construction-Costs/default.aspx) |
| HCD Annual Progress Reports dashboard and California Open Data | 2018 to latest | Permits, entitlements and completions by jurisdiction, including ADUs | [HCD APR dashboard](https://www.hcd.ca.gov/housing-open-data-tools/apr-dashboard) |
| LA County Permitting Progress Dashboard; ca.gov LA fires tracker | Live | Rebuild projects by phase; permits issued | [LA County dashboard](https://recovery.lacounty.gov/rebuilding/permitting-progress-dashboard/), [ca.gov tracker](https://www.ca.gov/lafires/track-progress/) |
| United Policyholders LA fire survey | Year one (about Jan 2026) | Underinsurance share and $/sq ft gap | [UP report](https://uphelp.org/united-policyholders-la-wildfires-year-one-survey-report/) |
| AGC–NCCER Workforce Survey (annual) | 2026-09-03 | Labor shortage, immigration and data center pressures | [AGC survey PDF](https://www.agc.org/sites/default/files/users/user21902/2026%20Workforce%20Survey%20Analysis%20(4).pdf) |
| NMHC Quarterly Survey of Apartment Construction and Development | June 2026 | Developer sentiment, cost and financing conditions | [NMHC](https://www.nmhc.org/research-insight/nmhc-construction-survey/2026/quarterly-survey-of-apartment-construction--development-activity-june-2026/) |
| Freddie Mac PMMS (weekly) | 2026-09-24 | Mortgage rates | [PMMS](https://www.freddiemac.com/pmms) |
| California Energy Commission / CASE Title 24 stakeholder studies | 2025 code cycle | Code cost-effectiveness analyses, which could supply Title 24 incremental costs | [Title 24 Stakeholders](https://title24stakeholders.com/cycle/2025/) (PX citation; contents not read) |

**What credible benchmark publishers disclose (observed practices)**
- **Sample and scope:** RAND states more than 140 completed projects across three states and splits market-rate from subsidized housing. AGC gives n = 1,830 and its field dates. United Policyholders defines its sample as total-loss respondents one year after the fires. (Sources in the table above.)
- **Units and exclusions:** NAHB separates construction cost from lot, overhead, commissions, financing, marketing and profit. Cushman & Wakefield states $/MW "excluding chips and GPUs." Meltplan states "as of September 2026," regional ±25–50% and soft costs of +15–30% (WS, attribution in Section 2).
- **Index construction:** RSMeans publishes its composite model (9 building types, 66 materials, 21 trades, 6 equipment items) and its localization logic. Turner, RLB and Mortenson publish the index level with quarterly and yearly change, plus the drivers. Mortenson splits materials from trade partner work. RLB adds a backlog indicator. (Sources in the table above.)
- **Context and records:** NAHB states when a figure is a series record, such as "highest in the history of this series" for $162/sq ft (WS).
- **In AI answers (PX):** answers repeatedly quote scope caveats ("hard vs all-in," "excludes land/financing/off-site utilities," "unit size matters"). Pages that state these plainly supply the text that gets quoted.

### Inferences
**Recommended benchmark method for Quotr ("Quotr Cost Benchmarks")**
1. **Scope and units.**
   - Headline figures are hard construction cost: contractor general conditions, overhead and profit, plus subcontractor labor, materials and equipment.
   - State explicitly that land, soft costs (design, permits and fees, financing), off-site utilities and furniture/fixtures/equipment are excluded.
   - Report $/gross sq ft plus $/unit or $/door for multifamily; $/sq ft of floor area for single-family homes and ADUs; and trade-specific units (per square for roofing, per sq ft of wall board, per linear foot of cabinets).
   - Offer an optional "all-in" view using ratios from NAHB (single-family) or RAND and industry sources (multifamily).
2. **Sample.**
   - Use Quotr Estimation Service projects within a stated date window.
   - Disclose **n per cell** and suppress cells with fewer than about 10 projects.
   - Say plainly that these are **estimates, not final contract costs or actuals**.
   - Report the **median and the 25th–75th percentile range**, not the mean.
3. **Normalization.**
   - Bring all projects to a common price date using BLS PPI categories (materials) and a labor escalator. The labor escalator could come from BLS wage data, which I did not verify here.
   - Adjust for location using a published index (RSMeans City Cost Index or RLB city indexes) and name the index used.
4. **Breakouts.**
   - Building type: custom and production single-family, ADU (detached, garage conversion, JADU, prefab), duplex to fourplex, garden, wrap, podium and mid-rise multifamily, and mass timber when n allows.
   - Region: LA, Bay Area, San Diego, Sacramento, rest of California, plus Texas and Florida if data exists.
   - Trade: map to NAHB stages or CSI divisions.
5. **Disclosure block on every page.**
   - date and version, n, regions, inclusions and exclusions, method, index sources, author (a named estimator) and reviewer, and a changelog;
   - a downloadable CSV;
   - "cite this as" text.
6. **Cross-checks against public anchors.** Compare with NAHB's $162/sq ft national figure (2024) and its stage shares, RAND's California multifamily ratios, Cushman & Wakefield's SF tenant-improvement figure, and the rebuild ranges above. Explain any divergence, for example the framing definition gap noted in Section 2.
7. **Cadence.** Update quarterly, timed to RLB, Turner and Mortenson. Publish a monthly material-price note when the BLS PPI comes out.
8. **A differentiator only Quotr has:** a factory-direct vs domestic landed-cost comparison for finish categories (cabinets, vanities, tile, windows). Show the tariff line (Section 232 at 25% through 2026, scheduled to reach 50% on 2027-01-01) so pages stay accurate as rates change.

### Gaps
- The NAHB 2024 survey's sample size (number of builders) and its exact line-item dollar figures were not captured; WebFetch was blocked for nahb.org and eyeonhousing.org.
- ENR's Building Cost Index and Construction Cost Index (20-city) and Cumming's reports were not checked this session.
- The DGS CCCI methodology and its current value were not verified.
- It was not verified whether LA, SF and other California city permit open-data portals include job valuation fields.
- BLS wage series (OEWS) for construction trades by California metro were not checked.
- The Terner Center's construction cost research, beyond the legislative preview citation, was not reviewed.
- Quotr's internal data (how many projects per building type, region and trade; estimate vs award vs actual) is unknown and has to be confirmed with Quotr before committing to published n.

---

## Candidate article topics

### Takeaway
Twenty candidates follow, ordered by recommended horizon. The strongest short-term bets are topics where current AI answers are thin, contradictory or dependent on one small blog, and where Quotr has proprietary data: LA fire rebuild (cost tracker, insurance gap, permitting), the Title 24 cost impact, cabinet and vanity tariffs before 2027-01-01, 2026 bathroom and kitchen costs with landed-cost pricing, and a trade $/sq ft hub. Multifamily and SB 79/SB 9 benchmarks are the medium-term core, and a quarterly Quotr California Residential & Multifamily Cost Index is the long-term flagship.

### Cited Findings
- Evidence for each topic is linked inline below and detailed in Sections 1–3. Competition levels come from the 12 Perplexity checks (PX), the WebSearch results (WS) and the earlier audit (prior).

### Inferences
Every topic below is an Inference: a recommendation built on the cited evidence.

**Short-term (0–3 months)**

1. **LA Fire Rebuild Cost Tracker 2026: cost per sq ft in Altadena, the Palisades and Malibu (updated monthly)**
   - Prompts:
     - "How much does it cost to rebuild a house after the LA fires per square foot in 2026?"
     - "Altadena rebuild cost per square foot"
     - "Pacific Palisades rebuild cost 2026"
     - "How many homes have been rebuilt after the LA fires?"
     - "How many rebuild permits have been issued?"
   - Intent: benchmark report plus news explainer, as a living tracker.
   - Persona: fire-affected homeowners and their architects; rebuild GCs and subcontractors; lenders.
   - Why now:
     - The PX status answer mixed four inconsistent figures: fewer than a dozen rebuilt at one year; 100 Altadena homes as of 2026-07-07; 3,728 permits countywide; 33 of about 1,700 Altadena homes.
     - News peaked on 2026-09-22 and 2026-09-25 (Pasadena Star-News, Daily News).
     - Cost answers rely on Bloomberg and local contractors at $400–$800+/sq ft (prior).
     - The average underinsurance gap is $247/sq ft ([UP](https://uphelp.org/united-policyholders-la-wildfires-year-one-survey-report/)).
   - Competition observed: medium. About 10 local contractor guides, Bloomberg, and Shovels for permits. No one publishes repeatable estimate data.
   - Data needed:
     - Quotr's LA fire estimates from its "Fast Cost Estimation (Residential LA Fire Rebuilding)" work, anonymized, as $/sq ft by size, finish level and area;
     - line items for Chapter 7A and Title 24 2025;
     - dated monthly snapshots of the LA County dashboard, the ca.gov tracker and figures from Malibu and the City of LA.

2. **Is Your Insurance Enough to Rebuild? LA Fire Underinsurance Gap Calculator (2026)**
   - Prompts: "Is my insurance enough to rebuild after the Eaton fire?", "average underinsurance gap LA fires", "replacement cost vs rebuild cost".
   - Intent: calculator plus how-to.
   - Persona: homeowners, public adjusters, attorneys, architects.
   - Why now:
     - 69% of total-loss respondents are underinsured, the average gap is $247/sq ft, and 24% still don't know whether they are underinsured.
     - 61% of respondents with claim problems said the insurer's replacement-cost estimate was inadequate ([UP](https://uphelp.org/united-policyholders-la-wildfires-year-one-survey-report/)).
   - Competition observed: low. Only qualitative contractor posts such as [Vaisman](https://www.vaismanconstruction.com/fire-rebuild-resources/how-much-does-it-cost-to-rebuild-home-after-wildfire-los-angeles/).
   - Data needed: Quotr's $/sq ft rebuild ranges by size and finish, code-upgrade line items, and the UP statistics. Frame it as cost estimation, not insurance or legal advice.

3. **LA Rebuild Permits in 2026: AI Plan Check (Archistar), Self-Certification and Standard Plans, and What Each Saves**
   - Prompts: "How does AI plan check work for LA fire rebuilds?", "LADBS self-certification pilot requirements", "How long does a rebuild permit take in LA County?"
   - Intent: how-to and news explainer.
   - Persona: architects, engineers, GCs, homeowners.
   - Why now:
     - EO No. 6 self-certification (2025-04-22), later expanded to civil engineers ([LADBS](https://dbs.lacity.gov/self-certification-pilot-program)).
     - Archistar AI PreCheck ([Governor 2025-04-30](https://www.gov.ca.gov/2025/04/30/governor-newsom-announces-launch-of-new-ai-tool-to-supercharge-the-approval-of-building-permits-and-speed-recovery-from-los-angeles-fires/)).
     - LA County's AI plan check deck ([2026-03-13](https://file.lacounty.gov/SDSInter/dpw/recovery/1204847_RebuildingTogether_Archistarv2DRAFTPPT31126.pdf)).
     - Permits issued in under three months on average (WS).
   - Competition observed: low–medium (Archistar's blog, Letter Four, LADBS and Mayor pages).
   - Data needed: public program rules; plan-to-permit day counts from Quotr's clients; how a takeoff and estimate fits the submittal.

4. **What California's 2025 Title 24 Energy Code Adds to the Cost of a New Home or ADU (2026)**
   - Prompts: "How much does Title 24 2025 add to construction cost?", "heat pump requirement new home California 2026 cost", "solar and battery requirement new construction cost".
   - Intent: news explainer plus cost data.
   - Persona: builders, ADU builders, rebuild homeowners, mechanical/electrical/plumbing subcontractors.
   - Why now: in force for permits from 2026-01-01. The PX answer had **no dollar figure** and cited only the CEC, DGS and a law firm ([CEC](https://www.energy.ca.gov/news/2026-01/californias-energy-code-update-guides-construction-cleaner-healthier-buildings)).
   - Competition observed: low on dollar figures.
   - Data needed: Quotr line items (heat pump water heater, heat pump HVAC, PV, battery, controls, envelope) by home type and climate zone; CASE cost-effectiveness studies.

5. **Kitchen Cabinet and Vanity Tariffs 2026–2027: A Landed-Cost Calculator for Builders**
   - Prompts: "kitchen cabinet tariff 2026", "Will cabinet tariffs go to 50% in 2027?", "landed cost of cabinets imported from China", "tariff on bathroom vanities".
   - Intent: news explainer plus calculator.
   - Persona: home builders, multifamily developers, remodelers, procurement leads.
   - Why now:
     - The 25% rate holds through 2026; the increase to 50% is scheduled for **2027-01-01** after the 2025-12-31 delay ([NAHB](https://www.nahb.org/blog/2026/01/wood-product-tariff-delays), [CNN](https://www.cnn.com/2026/01/01/business/trump-furniture-tariff-delay-intl-hnk)).
     - Stacked rates may exceed 70% for goods of Chinese origin (unverified).
     - Tariff prompts cite no vendor at all (prior).
   - Competition observed: medium (trade law firms, cabinet sellers such as NextDAY). No builder-cost vendor.
   - Data needed: HTS codes and rates, Quotr's delivered-duty-paid (DDP) quotes, freight and lead times. Keep a dated changelog because rates move.

6. **Bathroom and Kitchen Remodel Cost 2026, with Tariff-Adjusted Cabinet, Vanity and Tile Prices**
   - Prompts: "bathroom remodel cost 2026", "kitchen remodel cost 2026", "cabinet cost per linear foot 2026", "How much do tariffs add to a kitchen remodel?"
   - Intent: cost data.
   - Persona: remodelers, home builders, homeowners.
   - Why now: PX found **no 2026 bathroom source**. Cabinet sellers ([USA Cabinet Store](https://www.usacabinetstore.com/kitchen-remodeling-cost/), [Kitchen Cabinet Kings](https://kitchencabinetkings.com/2026-kitchen-roi-report)) are cited for kitchens. Kitchens and guest baths are each remodeled by 24% of homeowners (WS).
   - Competition observed: high for kitchens (Angi, NerdWallet, Houzz); low–medium for 2026 bathrooms and the tariff angle.
   - Data needed: Quotr factory-direct DDP prices against domestic dealer quotes; labor ranges by California metro.

7. **Construction Cost per Square Foot by Trade (2026): a hub plus spokes for framing, drywall, electrical, plumbing, HVAC, roofing, flooring and concrete**
   - Horizon: publish the hub and two or three spokes short-term, the rest medium-term.
   - Prompts: "framing cost per square foot 2026", "drywall installed cost per sq ft", "electrical rough-in cost per square foot new construction", "plumbing cost per sq ft new house", "roofing cost per square 2026", "concrete slab cost per sq ft 2026".
   - Intent: cost data.
   - Persona: trade subcontractors, GCs, estimators.
   - Why now:
     - [Exayard](https://exayard.com/blog/framing-cost-per-square-foot) is the first framing citation.
     - AI answers quote $7–$16/sq ft against about $26.9/sq ft implied by NAHB's framing share (a definitional gap; my arithmetic).
     - ABC reports lumber, steel, copper wire and switchgear up more than 10% year over year.
     - AGC reports labor pressure.
   - Competition observed: medium–high (Exayard, Angi, HomeGuide, myBuildIQ, CostFlowAI).
   - Data needed: Quotr takeoff quantities × unit prices by trade and California metro; BLS PPI series; clear unit definitions (floor area, wall area or roof squares).

8. **How to Read a Construction Cost Benchmark: Hard vs Soft Costs, per Unit vs per Door, Location Factors (and Quotr's Methodology)**
   - Prompts: "What's included in construction cost per square foot?", "hard costs vs soft costs multifamily", "How do I adjust construction costs for location?", "What is a city cost index?"
   - Intent: what-is and how-to. This page also underpins trust in every other benchmark.
   - Persona: developers, estimators, homeowners.
   - Why now: every PX cost answer added scope caveats. Pages that define scope clearly get quoted.
   - Competition observed: medium (Gordian's City Cost Index explainer, RSMeans guides).
   - Data needed: a methodology page and glossary, following the Section 4 method.

9. **Construction Material Price Tracker (monthly): lumber, steel, copper wire, switchgear, drywall and cabinets, factory-direct vs domestic**
   - Prompts: "Are construction material prices going up in 2026?", "lumber prices September 2026", "Why is switchgear so expensive?", "copper wire price increase construction".
   - Intent: monthly benchmark report.
   - Persona: estimators, subcontractors, builders, developers.
   - Why now: ABC shows inputs up 8.9% year over year in August 2026, with several categories up more than 10% ([ABC](https://constructioncitizen.com/blog/abc-construction-materials-prices-jump-again-august/2609161)).
   - Competition observed: high authority (ABC, AGC, NAHB), but none publishes factory-direct comparisons.
   - Data needed: BLS PPI (public) and Quotr's quotes.

10. **ADU Cost in California (2026): Detached vs Garage Conversion vs JADU vs Prefab, with Line-Item Budgets for LA and the Bay Area**
    - Horizon: publish v1 short-term, then refresh.
    - Prompts: "How much does an ADU cost in California in 2026?", "garage conversion ADU cost Los Angeles", "JADU cost", "prefab ADU cost California", "ADU cost per square foot Bay Area".
    - Intent: cost data plus calculator.
    - Persona: ADU builders and subcontractors, homeowners, fire rebuilders adding ADUs.
    - Why now:
      - LA County accounts for about 60% of California ADUs since 2018 (WS, HCD APR).
      - The PX answer gives wide ranges from local builders and calculators.
      - ADUs are drawing national coverage in September 2026 ([WaPo 2026-09-19](https://www.washingtonpost.com/business/2026/09/19/accessory-dwelling-units-can-provide-extra-room-income/)).
    - Competition observed: high but fragmented. Calculators get cited.
    - Data needed: Quotr ADU takeoffs and estimates; factory-direct finish package prices.

**Medium-term (3–9 months)**

11. **California Cost to Build a House per Square Foot (2026): LA, Bay Area, San Diego, Sacramento, with a Trade-by-Trade Breakdown**
    - Could also grow into a state series covering Texas and Florida.
    - Prompts: "cost to build a house per square foot California 2026", "... Bay Area", "... Los Angeles", "Florida cost to build per sq ft 2026".
    - Intent: cost data and benchmark.
    - Persona: custom and small builders, subcontractors, homeowners, developers.
    - Why now: PX ranges are wide and rest on marketplaces and builder blogs, and Florida is thin. Title 24 applies from 2026-01-01, and inputs are up 8.9% year over year.
    - Competition observed: high (HomeAdvisor, Fixr, HomeGuide, HomeLight, Autodesk, Opendoor).
    - Data needed: Quotr single-family estimates by metro and finish; NAHB stage shares; RSMeans or RLB location factors; Census median home size.

12. **Multifamily Construction Cost per Unit (2026): Garden vs Wrap vs Podium vs Mid-Rise vs Mass Timber, California vs Texas**
    - Prompts: "multifamily construction cost per unit 2026", "podium vs wrap cost per unit", "cost per door to build apartments in California", "mass timber apartment cost premium".
    - Intent: benchmark report.
    - Persona: multifamily developers, GCs, lenders.
    - Why now:
      - Multifamily starts are down 14.6% year over year (August 2026), and NMHC optimism fell from 68% to 46%.
      - Deliveries are forecast to drop 28% in 2026.
      - RAND puts California at 2.3× Texas.
      - AI answers rely on aggregator and vendor pages.
    - Competition observed: medium (Meltplan, Exayard, irecruit, apers.app, Visidex; RSMeans in the earlier audit).
    - Data needed: Quotr multifamily estimates with unit count, gross sq ft, product type, parking type and n per cell; clear per unit, per door and per gross sq ft definitions.

13. **What It Costs to Build Apartments in Los Angeles in 2026, and Why Starts Stalled**
    - Horizon: short-to-medium.
    - Prompts: "How much does it cost per unit to build apartments in Los Angeles in 2026?", "LA apartment construction cost per square foot", "How does Measure ULA affect development?"
    - Intent: benchmark plus news explainer.
    - Persona: LA developers, investors, brokers.
    - Why now: [LA Times 2026-09-22](https://www.latimes.com/california/story/2026-09-22/la-developers-arent-building-more-apartments-despite-epic-housing-shortage) and [The Real Deal 2026-09-23](https://therealdeal.com/la/2026/09/23/measure-ula-rising-costs-plaguing-los-angeles-developers/). The top AI sources are a small brokerage blog ([CLS CRE](https://clscre.com/blog/ground-up-multifamily-construction-los-angeles-2026.html)) and [oneestimate.ai](https://oneestimate.ai/en/california/los-angeles).
    - Competition observed: low–medium.
    - Data needed: Quotr LA multifamily estimates; LA fees; RAND ratios.

14. **SB 79 Feasibility: What a Transit-Oriented Project Costs to Build Under California's Upzoning (95 ft / 160 Units per Acre)**
    - Prompts: "What can I build under SB 79?", "SB 79 pro forma", "cost to build a 7-story apartment near transit in LA 2026".
    - Intent: explainer, cost data and a pro forma template.
    - Persona: developers, landowners, architects.
    - Why now: effective 2026-07-01 in 10 counties, with cities adopting implementing ordinances ([H&K June 2026](https://www.hklaw.com/en/insights/publications/2026/06/tracking-sb-79-implementation-before-the-train-leaves-the-station)).
    - Competition observed: law firms own the legal explainers. The cost side was not tested in AI; I found no cost-focused pages in WebSearch.
    - Data needed: Quotr podium and mid-rise benchmarks; a pro forma template; construction-type cost thresholds, to be verified with a code consultant.

15. **SB 9 Duplex and Fourplex Cost in California (2026): Lot-Split Fees, Hard Costs and a Pro Forma**
    - Prompts: "cost to build a fourplex in California under SB 9", "SB 9 lot split cost", "duplex construction cost Los Angeles 2026".
    - Intent: cost data plus pro forma.
    - Persona: small developers, homeowner-investors, builders.
    - Why now: the PX answer stitched national HomeAdvisor fourplex numbers together to reach "$1.0M–$1.8M." LA's lot split fee is $3,978 ([LA Planning](https://planning.lacity.gov/odocument/597fb369-6fbd-4148-a057-3f33233405d2/SB9FAQ2.7l.pdf)).
    - Competition observed: low–medium (withpat, Bay Area ADU Manager, LA Metro Home Finder).
    - Data needed: Quotr small-multifamily estimates; city fee schedules; Quotr's developer pro forma format.

16. **Construction Labor Costs 2026: Immigration Enforcement, Data Centers and Wage Pressure, and What to Budget by Trade**
    - Prompts: "construction labor shortage 2026", "How is immigration enforcement affecting construction?", "Are data centers raising electrician wages?", "construction labor cost per hour California 2026".
    - Intent: news explainer plus data.
    - Persona: subcontractors, GCs, developers.
    - Why now: in the AGC–NCCER survey (2026-09-03), 29% of firms reported enforcement impacts; among firms doing data center work, 58% saw more labor competition and 49% more wage pressure ([AGC](https://www.agc.org/news/2026/09/03/construction-workforce-shortages-remain-acute-despite-soft-market-conditions-data-centers-strain)). Turner's Q2 2026 index names mechanical and electrical labor as the biggest challenge.
    - Competition observed: AGC and ENR own the statistics, but no one covers the $/sq ft impact by trade.
    - Data needed: labor rates from Quotr bids; BLS OEWS (to verify).

17. **Commercial Tenant Improvement Cost per Square Foot (2026): San Francisco, the Bay Area and Los Angeles**
    - Prompts: "tenant improvement cost per square foot 2026 Los Angeles", "office build-out cost San Francisco 2026", "TI allowance vs actual cost".
    - Intent: cost data.
    - Persona: commercial GCs, tenant-improvement subcontractors, tenants and brokers.
    - Why now: the PX answer found **no LA-specific 2026 benchmark**. SF fit-out runs $219–$228/sq ft ([Cushman & Wakefield](https://www.cushmanwakefield.com/en/united-states/insights/office-fit-out-cost-guide) via Bizjournals 2026-09-24). LADBS offers self-certification for commercial tenant improvements.
    - Competition observed: medium (Cushman & Wakefield guide, local GCs).
    - Data needed: Quotr tenant-improvement estimates by scope level (light, standard, high-end).

**Long-term (9–18 months)**

18. **Quotr California Residential & Multifamily Cost Index (quarterly)**
    - Prompts: "construction cost index California 2026", "How much have construction costs risen in Los Angeles?", "residential construction cost escalation forecast 2027".
    - Intent: flagship benchmark report, with a press release each quarter.
    - Persona: developers, lenders, appraisers, press.
    - Why now: the existing indexes are nonresidential (Turner), skip California metros (Mortenson) or keep city detail inside reports (RLB). I found no California residential index.
    - Competition observed: low for California residential.
    - Data needed: at least four quarters of Quotr estimate data with n per cell, the published method, a CSV download and a changelog.

19. **The Data Center Spillover: How the AI Build-Out Is Raising Electrical and Mechanical Costs for Housing and Commercial Projects**
    - Priority: low.
    - Prompts: "How are data centers affecting construction costs?", "Why are electricians so expensive in 2026?", "switchgear lead times 2026".
    - Intent: explainer.
    - Persona: electrical and mechanical subcontractors, GCs, developers.
    - Why now:
      - Data center construction reached $75.2B SAAR in July 2026, up 57.2% year over year, and ConstructConnect counts $84.1B in starts year to date.
      - In the AGC survey, 58% of firms doing data center work see more competition for skilled workers.
      - ABC reports switchgear and copper up more than 10%; Mortenson cites long equipment lead times.
    - Competition observed: institutions own $/MW; the spillover angle was not tested.
    - Data needed: comparisons from Quotr's electrical and mechanical bids.

20. **2024 IECC and Your Budget: Which States Adopted It and What It Adds per Home**
    - Priority: low (national, less California-relevant).
    - Prompts: "2024 IECC cost per home", "Which states adopted the 2024 IECC?"
    - Intent: explainer.
    - Persona: builders and subcontractors outside California.
    - Why now: the DOE's roughly $14,000-per-home claim against SWEEP's rebuttal; Illinois (November 2025) and Rhode Island have adopted ([DOE](https://www.energy.gov/articles/energy-department-analysis-finds-proposed-international-building-codes-would-cost), [IMT](https://imt.org/news/2026-energy-codes-outlook/)).
    - Competition observed: medium (DOE, IMT, trade press).
    - Data needed: public sources; Quotr costs for the code-driven line items.

**Cross-cutting notes on format, for every benchmark page**
- Put "2026" and an "as of [date]" in the title and first paragraph.
- Include a tiered range table with regional rows, then a scope and exclusions box.
- Show n and the method, and link to the methodology page (topic 8).
- Add an FAQ written in the exact prompt wording above.
- Offer a CSV and "cite this" text.
- Name the estimator as author.
- Update monthly or quarterly with a visible changelog.

These choices mirror what got Meltplan, Exayard, CLS CRE and oneestimate.ai cited (Section 2).

### Gaps
- Search volumes for every prompt listed are unknown. Validate with Google Keyword Planner or Search Console before final prioritization.
- Before publishing, confirm with Quotr how much proprietary data exists: projects per type, region and trade, and whether they are estimates, awards or actuals. Topics 1, 7, 10–13 and 18 depend on it.
- LA fire and insurance topics (1–3) should be reviewed for accuracy and tone, and should not read as legal or insurance advice.
- The SB 79 construction-type cost thresholds (topic 14) need code-consultant verification.
- AI competition was measured on Perplexity only, one run per prompt. ChatGPT, Google AI Overviews/AI Mode, Gemini, Claude and Copilot may cite different sources.
