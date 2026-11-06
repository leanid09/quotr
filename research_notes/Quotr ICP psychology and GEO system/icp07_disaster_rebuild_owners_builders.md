# ICP 7 — Disaster-rebuild buyers (LA January 2025 fires first; Lahaina, Helene and Florida second): psychology, prompts and GEO system for Quotr.ai

**Research date:** 2026-11-06 (current state as of November 2026). **Researcher scope:** ICP 7 only.

**How this research was done, and its limits (read first):**
- The method follows the uploaded ICP-depth GEO framework: geography → segments → coding chains → prompt matrix → pages and placements → compliance → known/likely/speculative.
- **About 31 web searches ran before the shared search budget ran out**, which was 200 searches per turn across all agents. **WebFetch was blocked by the session's network allowlist** (uphelp.org, calmatters.org and therenology.com failed DNS; quotr.ai and firetips.quotr.io returned proxy 403s). **Reddit could not be searched**, because the search tool's user agent is blocked by reddit.com.
- So every fact below comes from **search-result extracts**, not full-page reads, unless stated otherwise. Where an extract cited a group of results without naming which page held a figure, I cite the most likely page and say so.
- **Secondary markets** (Lahaina, western NC, Florida, and 2025–2026 disasters) were **not researched** before the budget ran out. They appear only as clearly labelled background knowledge or as gaps.
- Quotr facts come only from `/home/user/quotr/geo-brain/00-quotr/*.md` and earlier research notes in this repo.
- Labels used throughout: **[Known]** = sourced; **[Likely]** = inference from sourced facts; **[Speculative]** = hypothesis; **[SIMULATED]** = written by the researcher, not observed; **[Estimate]** = researcher's tier or number.

---

## A. Definition and size

### Takeaway
About 16,250 structures were destroyed, including about 11,400 homes. By the end of September 2026, permits were moving fast but completions were tiny: about 215 homes finished in unincorporated Altadena and 30–48 in the Palisades. So **more than 90% of destroyed homes are still unbuilt in November 2026**, and about 60% of Palisades owners have not even filed to rebuild. Surveys disagree on the exact rate, but they agree on scale: a large majority of total-loss owners are underinsured. Shortfalls run from about $300,000 (Altadena, AAA policyholders) to about $500,000 on average (Department of Angels survey), and to $1.5M per home in a vendor's Palisades sample. Contractor-quoted rebuild costs are $350–$850 per sq ft in Altadena and $550–$1,200 in the Palisades. **No independent per-sq-ft dataset exists.**

### Cited Findings
**ICP definition (researcher's framing, built from the brief).** Four sub-buyers:
- (1) total-loss **homeowners** deciding to rebuild, downsize or sell;
- (2) **owner-builders** (survivors who are or hire GCs and manage their own rebuild);
- (3) **small builders and design-build firms** pricing many rebuild bids;
- (4) **lot buyers** (developers and investors) who need fast cost and pro forma numbers.

**Destruction (CAL FIRE DINS figures as reported after containment):**

| Fire | Structures destroyed | of which homes | Damaged (homes) | Acres | Source |
|---|---|---|---|---|---|
| Palisades | 6,837 | 5,419 | 1,017 (764) | 23,448 | [NBC LA](https://nbclosangeles.com/news/california-wildfires/map-damage-assessment-eaton-palisades-fire/3620536/); [TODAY](https://www.today.com/today/amp/rcna190281) |
| Eaton | 9,418 (CBS: 9,413) | 6,011 | 1,073 (645) (CBS: 1,074) | ~14,000 | [NBC LA](https://nbclosangeles.com/news/california-wildfires/map-damage-assessment-eaton-palisades-fire/3620536/); [CBS LA](https://www.cbsnews.com/amp/losangeles/news/palisades-and-eaton-fires-now-among-most-destructive-wildfires-recorded-in-california-history) |
| Combined | ~16,250 | ~11,430 | ~2,090 structures | | derived |

- DINS "structures" include sheds and some non-homes. CalMatters instead counts "nearly 13,000 homes lost" ([CalMatters, Jan 2026](https://calmatters.org/housing/2026/01/la-fires-rebuild-permitting/)). This is probably a housing-unit count rather than a structure count. **Do not mix the two definitions on one page.**
- No formal CAL FIRE "final" report surfaced in search. Treat these as the widely reported post-containment figures (search extract).

**Permits and completions (latest found):**

| Jurisdiction | Permits / filings | Under construction | Completed (CofO) | Date | Source |
|---|---|---|---|---|---|
| City + County, all fire areas | 6,612 applications; 3,106 rebuild permits issued | — | — | late Jan 2026 | [Governor, Feb 6 2026](https://www.gov.ca.gov/2026/02/06/governor-newsom-announces-funding-for-la-fire-survivors-to-access-pre-built-housing-to-further-speed-recovery-and-maintain-neighborhood-character/) |
| Palisades + Altadena residential | >2,600 permits ("roughly one for every five of the nearly 13,000 homes lost") | — | — | Jan 2026 | [CalMatters](https://calmatters.org/housing/2026/01/la-fires-rebuild-permitting/) |
| LA County unincorporated (mostly Altadena) | 3,671 building permits | 2,310 | 215 | Sep 26 2026 (county data as relayed by a contractor guide; not checked against the dashboard) | [Lytemods](https://lytemods.com/fire-rebuild/altadena) |
| same | 2,981 permits | 1,796 | 100 | Jul 2026 | [Golden Line Construction](https://www.goldenlineconstruction.com/blog/altadena-eaton-fire-rebuild-guide) |
| Altadena | ">400 permitted rebuilds sit in limbo" (from the URL slug); insurance and cost, not bureaucracy, blamed | | | Sep 8 2026 | [The Real Deal](https://therealdeal.com/la/2026/09/08/more-than-400-permitted-rebuilds-sit-in-limbo-in-altadena/) |
| City of LA, Pacific Palisades | 1,419 properties permitted | — | 28 | Jul 7 2026 (LADBS via FOX LA) | [Alto Builds](https://altobuilds.com/palisades-fire-rebuild) |
| same | 1,196 permits | 1,006 | 30 | Aug 5 2026 | [palisadesfirerebuilding.com](https://palisadesfirerebuilding.com/rebuild-status) |
| same | 1,557 of 3,984 destroyed homes filed to rebuild | — | 48 | Oct 2026 | [Therenology](https://www.therenology.com/journal/palisades-altadena-fire-rebuild-insurance-contractors) |
| Westside (wider than the Palisades) | 1,663 permits | — | 65 CofO/final | date unclear | [myvilla.la tracker](https://myvilla.la/research/westside-rebuild-tracker.html) |
| Malibu | 101 SFR rebuild permits (33 in Feb 2026) | — | 1 | Sep 22–26 2026 | [SMDP](https://www.smdp.com/malibu-reaches-palisades-fire-rebuilding-milestones-with-100th-permit-first-certificate-of-occupancy/); [JW Enterprises](https://jwenterprises.com/malibu-fire-rebuild-update/) |
| Pasadena | **not found** | | | | Pasadena has its own dashboard per [ca.gov Rebuilding LA](https://www.ca.gov/lafires/rebuilding-la) |

- Milestones:
  - April 2025: about 3.5 months after the fires, LA County had issued 7 rebuild permits ([National Review](https://www.nationalreview.com/corner/three-and-a-half-months-later-los-angeles-county-has-issued-seven-rebuilding-permits/); a partisan source, but the number is factual).
  - First Palisades CofO: Nov 21, 2025, 915 N Kagawa St ([LA Downtown News](https://www.ladowntownnews.com/news/palisades-rebuild-first-certificate-of-occupancy-issued-as-recovery-accelerates/article_02a255e2-76e0-4ae4-ae9a-d7ff654676fa.html)). A Westside Current headline says that first rebuild went to a "New Owner, Not Displaced Family" ([Westside Current](https://www.westsidecurrent.com/pacific_palisades/a-rebuilt-home-in-the-palisades-marks-progress-but-not-a-family-s-return/article_44617644-5d3e-49a9-9bcf-99b2c0420cf1.html)).
  - First Altadena CofO: early December 2025, East Loma Alta Dr ([ABC7](https://abc7.com/post/first-fully-rebuilt-home-altadena-eaton-fire-given-certificate-occupancy-meaning-safe-cleared-move/18249727/)).
  - At the one-year mark, "fewer than a dozen" homes had been rebuilt ([NBC News/AP](https://www.nbcnews.com/news/us-news/year-la-area-wildfires-destroyed-thousands-homes-fewer-dozen-rebuilt-rcna252751)).
- Permit speed: rebuild permits are being issued about 3× faster than comparable SFR/ADU permits were in the five years before the fires. But median permit times rose between early-2025 and early-2026 filings: **Palisades 97 → 134 days; Altadena 95 → 199 days** (search extract attributed to CalMatters coverage, [CalMatters](https://calmatters.org/housing/2026/01/la-fires-rebuild-permitting/)).
- Historical base rate: LA Times reporting (as relayed in search) found **only 38% of families who lost homes in the five biggest California wildfires before 2025 had rebuilt after eight years** ([Marketplace](https://www.marketplace.org/story/2026/01/08/eaton-fire-survivors-struggle-to-rebuild-one-year-on); attribution within the result set is not certain).

**Rebuild vs sell:**
- The Department of Angels survey of more than 2,000 survivors found **90% planning to rebuild**, a majority "more determined than ever" ([LAist](https://laist.com/brief/news/climate-environment/fire-rebuilding-costs-new-funds-financing-attempt-to-fill-gaps); [California Community Foundation](https://www.calfund.org/news-and-events/a-year-after-la-wildfires-most-survivors-are-still-displaced-and-struggling-financially-department-of-angels-survey-finds/)).
- Lot sales, Redfin Q3 2025 ([LAist](https://laist.com/brief/news/housing-homelessness/los-angeles-fires-january-2025-redfin-investor-purchase-empty-lots-sales); [Redfin via Business Wire](https://www.businesswire.com/news/home/20251230482895/en/Vacant-Lots-for-Sale-Are-Piling-Up-After-the-L.A.-Fires-Investors-Are-Buying-40-of-Those-That-Sell)):
  - Altadena: 61 lots sold in the quarter; 225 listed (2 before the fires).
  - Palisades: 119 lots sold; 300+ listed (7 before the fires).
- The Palisades filing rate is 1,557/3,984 ≈ 39% ([Therenology](https://www.therenology.com/journal/palisades-altadena-fire-rebuild-insurance-contractors)). Read the other way, about 61% had not filed by October 2026: a mix of undecided owners, owners still in design, and sellers.

**Underinsurance (sources conflict; keep them apart):**
- **United Policyholders (UP) 12-month survey** ([PDF](https://uphelp.org/wp-content/uploads/2026/03/UP-Survey-2025-LA-Wildfires-12-MO-Summary-Results-Export.pdf); summary via search):
  - Only **7% of total-loss respondents had enough insurance to rebuild**.
  - Those who were short averaged **36% below rebuild cost in the Eaton fire and 46% in the Palisades fire**.
  - Responses: 547 total, 421 Eaton-linked and 254 Palisades-linked (the overlap is unexplained). The "675 households" figure in one extract equals 421 + 254.
- A different relay of the UP data says **69% of total-loss respondents lacked enough insurance, averaging $247/sq ft short** ([tect.com](https://www.tect.com/feeds/blog/average-cost-rebuild-house-fire); secondary vendor blog). **This conflicts with the "7% had enough" figure.** Verify against the PDF before publishing either number.
- UP's Amy Bach expected underinsurance as high as **75–80% in Altadena**, against a typical two-thirds of wildfire victims (search extract; [UP](https://uphelp.org/a-broken-system-is-keeping-california-homes-underinsured-millions-have-no-idea-theyre-at-risk/)).
- A claims study by Klein (relayed by UP) found **71.3% of destroyed homes underinsured, by about 19% on average**. It is built on insurers' self-reported data and covers California only. UP's headline: "Insurers' own rebuild estimates are driving most underinsurance" ([UP](https://uphelp.org/insurers-own-rebuild-estimates-are-driving-most-underinsurance-study-finds/)).
- **LAist, AAA policyholders in Altadena** (34 neighbours surveyed) ([LAist](https://laist.com/brief/news/climate-environment/eaton-palisades-fire-altadena-aaa-insurance-rebuild-costs)):
  - average AAA dwelling coverage **$628,000**;
  - field adjusters' average rebuild cost **$867,000** (+41%);
  - contractor quotes averaged **$928,000**;
  - average gap about **$300,000**.
- **Department of Angels** (July survey, >2,000 survivors): homeowners short **$500,000 on average** after insurance; the typical renter is $100,000 short (October report) ([LAist](https://laist.com/brief/news/climate-environment/fire-rebuilding-costs-new-funds-financing-attempt-to-fill-gaps)).
- **Altadena Land Initiatives** program materials: a gap of "40% to 50% of their rebuild costs" ([Pasadena Now](https://pasadenanow.com/main/eaton-fire-survivors-nonprofit-opens-zero-interest-rebuild-financing-to-more-altadena-homeowners)).
- **ClaimArchitect** (a vendor with a stake in the result) ([LA Business Journal](https://labusinessjournal.com/featured/tool-identifies-insurance-payout-estimate-gaps/)):
  - 37 Palisades client cases;
  - average gap **$603/sq ft ≈ $1.5M per home**, ranging from $164K to $3.4M;
  - a separate extract gives a median gap of $559/sq ft.
- Average Altadena policy was **$607,000 (2023)** ([Catalyst California](https://www.catalystcalifornia.org/campaign-tools/publications/red-tape-to-recovery-tracking-altadena-rebuilding)).
- Insurers had paid **>$23.7B** on the two fires as of March 3 (year as relayed, probably 2026). The California Department of Insurance (CDI) had recovered >$280M for survivors through direct intervention ([Pasadena Now](https://pasadenanow.com/main/altadena-founded-survivor-network-opens-insurance-survey-to-build-a-public-record-of-how-insurers-performed)).

**Rebuild cost per sq ft (2025–2026, almost all from contractor marketing):**
- Altadena: $350–400 standard to mid-range (one builder); $450–550 standard / $550–675 upgraded / $675–850 custom (a "TESH Group" full-scope analysis); $450–750 including architecture, engineering and permits.
- Palisades: $650–1,200 quoted; $550–900 typical custom.
- Policies written years ago often assumed **$200–250/sq ft**.
- One contractor page says outright that **"there is no government or academic dataset tracking per-square-foot LA rebuild pricing."**
- Sources: [altadenacustomhomebuilder.com](https://altadenacustomhomebuilder.com/blog/cost-to-rebuild-a-house-after-a-fire-in-los-angeles-2026-numbers); [bwengr.com](https://bwengr.com/blog/2026/04/12/altadena-rebuild-costs/); [ZMA Legacy](https://www.zmalegacybuilders.com/blog/cost-to-rebuild-after-fire-altadena-2026); [Alto Builds](https://altobuilds.com/palisades-fire-rebuild); [UBIC](https://ubic.co/blog/cost-to-rebuild-a-home-in-altadena-after-the-eaton-fire); [Amerbuild](https://www.amerbuild.com/fire-rebuild/). Which page carries which range was not verified within this set.
- Other figures: Vaisman puts LA at $350–600/sq ft ([Vaisman](https://www.vaismanconstruction.com/fire-rebuild-resources/how-much-does-it-cost-to-rebuild-home-after-wildfire-los-angeles/)). Quotr's own earlier test of this prompt returned $400–$800+/sq ft from Bloomberg and local GCs ([verification note](<../Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>)).
- Tariffs on lumber and cabinets imposed in fall 2025 are expected to raise homebuilding costs ([CNN, Jan 8 2026](https://www.cnn.com/2026/01/08/us/altadena-la-fires-rebuilding-invs)).

### Inferences
- [Likely] **Completion share by late 2026:** Altadena 215 of about 6,000 homes ≈ 3.6%; Palisades 48 of 3,984 ≈ 1.2%; Malibu 1 CofO. Even with about 3,300 homes under construction (2,310 + 1,006), most construction cost decisions (finishes, change orders, materials buying) still lie ahead in 2027–2028. Most rebuild-or-sell decisions for the about 60% of Palisades owners who have not filed also lie ahead.
- [Likely] **Serviceable pool for Quotr (rough, labelled estimate):**
  - ~11,400 destroyed homes minus ~2,000 lots sold or listed, minus ~250 completed → **~9,000 households** still facing a cost decision.
  - Plus the builders and lot-buyers serving them.
  - Contractor counts: one platform alone (Bidsy) onboarded **>200 GCs and subs in the Palisades** ([SMDP](https://smdp.com/palibuilds-is-rewriting-the-rebuild-playbook-in-pacific-palisades)).
- [Likely] Per-sq-ft framing beats per-home framing. Example: at $450–550/sq ft, the average 2023 Altadena policy of $607K rebuilds only about **1,100–1,350 sq ft** before soft costs. That "how many square feet does my Coverage A buy" angle is quotable and original.
- [Likely] Underinsurance is the norm, not the edge case. Every survey converges on a majority underinsured, with dollar gaps in the hundreds of thousands. The exact percentage is contested.

### Gaps
- The official LA County / LADBS / Pasadena / Malibu dashboard numbers for October–November 2026 were not read directly (fetch blocked). Pasadena permit counts were not found at all.
- No per-area count of lots sold versus rebuilding in 2026 (Redfin data ends Q3 2025).
- The UP survey's conflicting "7% enough" versus "69% short" figures are unresolved.
- No independent per-sq-ft dataset; every per-sq-ft range is contractor marketing.

---

## B. Geography: sub-area segments and page-worthiness

### Takeaway
The LA rebuild market resolves into four evidence-backed segments with genuinely different economics, so they justify separate spokes: West Altadena, East Altadena/Pasadena, Pacific Palisades, and Malibu. One LA hub plus three spokes (Altadena, Palisades, Malibu) is defensible. Lahaina, western NC and Florida could not be researched this session and should not get pages until researched.

### Cited Findings
**Segment evidence rows (LA):**

| Segment | Evidence row | Job / economics | Source |
|---|---|---|---|
| **S1 West Altadena legacy homeowner** (historic Black homeownership) | 81% of Black households in Altadena owned homes (SAJE, 2023). UCLA Bunche: 61% of Black households were inside the fire perimeter vs 50% of non-Black. More than half of Black homeowners are 65+. Black and Latino households were more than twice as likely as white households to lack insurance. UCLA: Black homeowners were "the least likely to have moved toward rebuilding." Displacement risk was already high in western Altadena before the fire. | Keep generational wealth; close a 40–50% gap; resist investor offers. Low Coverage A, often FAIR Plan. Older and less likely to use ChatGPT [Likely]. | [LA Public Press](https://lapublicpress.org/2025/05/altadena-eaton-fire-rebuild-landlords-newsom/); [Inside Climate News](https://insideclimatenews.org/news/04042025/black-residents-of-altadena-struggle-after-la-fires/); [High Country News](https://www.hcn.org/articles/a-year-after-the-eaton-fire-permit-delays-keep-black-families-from-returning/); [NPR](https://www.npr.org/2025/02/08/nx-s1-5278617/black-altadenans-seek-hope-and-resilience-in-the-wake-of-the-la-wildfires) (which page carries which figure is approximate, from search extracts) |
| | FAIR Plan policies in ZIPs in or near the Eaton zone grew from about 7,000 (2023) to about 9,500 (2024). The FAIR Plan had about 1,369 Eaton property claims by Feb 19 (2025). Lawsuits allege FAIR Plan delays and underpayment. | FAIR Plan dwelling caps make the gap structural. | [Inside Climate News](https://insideclimatenews.org/news/04042025/black-residents-of-altadena-struggle-after-la-fires/); [Daily Journal](https://www.dailyjournal.com/articles/386060-homeowner-sues-fair-plan-over-denied-eaton-fire-claim); [Legal Newsline](https://www.legalnewsline.com/state-courts/altadena-palisades-residents-sue-fair-plan-over-wildfire-claim-denials-underpayments/article_2a49a61f-3ef9-4265-819d-e06581faa79c.html) |
| | Targeted capital exists: the BET/NAACP/WME Altadena Community Preservation Fund (by census tract, including FAIR Plan and underinsured owners); Altadena Land Initiatives zero-interest gap financing. | A "gap stack" of insurance, SBA, grants and zero-interest loans; needs a documented budget. | [BET](https://www.bet.com/article/kohaj0/altadena-community-preservation-fund-launched-to-support-black-homeowners-impacted-by-eaton-fire); [Pasadena Now](https://pasadenanow.com/main/eaton-fire-survivors-nonprofit-opens-zero-interest-rebuild-financing-to-more-altadena-homeowners) |
| **S2 East Altadena / Pasadena-adjacent professional household** | No separate east/west data found. Altadena-wide facts apply: the AAA cohort (coverage $628K; contractor quotes $928K); average policy $607K; typical lot sale $510K; 44.3% of Altadena lot sales to investors (27 of 61). | Underinsured by ~$300K; deciding size and finishes; ALE pressure. More likely to use ChatGPT [Likely]. | [LAist AAA](https://laist.com/brief/news/climate-environment/eaton-palisades-fire-altadena-aaa-insurance-rebuild-costs); [Catalyst](https://www.catalystcalifornia.org/campaign-tools/publications/red-tape-to-recovery-tracking-altadena-rebuilding); [LAist Redfin](https://laist.com/brief/news/housing-homelessness/los-angeles-fires-january-2025-redfin-investor-purchase-empty-lots-sales) |
| | Altadena Not for Sale: about 60% of all property purchases in the fire area were by investors (August); 8 companies bought 76 properties, about a quarter of Altadena sales in year one. | Lot-sale pressure; community norm against selling. | [SMDP](https://www.smdp.com/investors-snap-up-fire-zone-properties-and-housing-recovery-struggles/); [AOL/LA Times](https://www.aol.com/articles/investors-keep-buying-burned-lots-110000414.html) |
| **S3 Pacific Palisades high-net-worth owner** | Typical lot sold for **$1.6M**; investors were 40.3% of lot sales (48 of 119); 300+ lots listed. Quotes run $650–1,200/sq ft. ClaimArchitect's average gap is $603/sq ft (≈$1.5M). 39% had filed by October 2026; 48 finished. | Rebuild-vs-sell arithmetic dominates; architect-led custom work; large finish packages (a Procurement fit). | [LAist Redfin](https://laist.com/brief/news/housing-homelessness/los-angeles-fires-january-2025-redfin-investor-purchase-empty-lots-sales); [Alto Builds](https://altobuilds.com/palisades-fire-rebuild); [LABJ](https://labusinessjournal.com/featured/tool-identifies-insurance-payout-estimate-gaps/); [Therenology](https://www.therenology.com/journal/palisades-altadena-fire-rebuild-insurance-contractors) |
| | Mayor's executive order suspends rebuild fees for Palisades residents. Debris removal was completed at >1,000 Palisades properties (date in the release). | Fees and timing differ from County rules. | [Mayor Bass, fees](https://mayor.lacity.gov/news/mayor-bass-issues-emergency-executive-order-suspending-collection-rebuilding-fees-palisades); [Mayor Bass, debris](https://mayor.lacity.gov/news/mayor-bass-highlights-completion-debris-removal-more-1000-properties-palisades-efficiency) |
| **S4 Malibu coastal owner** | 101 SFR rebuild permits and 1 CofO (September 2026), up from 33 in February 2026. Guides headline "Why So Few Permits Have Been Issued" and "Permits, Septic & Coastal Rules". Investor share of Malibu lot sales "more than doubled" year on year. | Septic and coastal adders; the slowest permits; the highest cost per sq ft [Likely]. | [SMDP](https://www.smdp.com/malibu-reaches-palisades-fire-rebuilding-milestones-with-100th-permit-first-certificate-of-occupancy/); [DWD Builders](https://www.dwdbuilders.com/intel/malibu-fire-rebuild-permit-delays-2026); [Lytemods Malibu](https://lytemods.com/fire-rebuild/malibu); [LAist Redfin](https://laist.com/brief/news/housing-homelessness/los-angeles-fires-january-2025-redfin-investor-purchase-empty-lots-sales) |
| **S5 Pasadena (city) owner** | Pasadena runs its own permitting dashboard; no count found. | Fold into the Altadena spoke for now. | [ca.gov Rebuilding LA](https://www.ca.gov/lafires/rebuilding-la) |
| **S6 Small builders and design-build firms (cross-area)** | Bidsy onboarded 200+ GCs and subs in the Palisades. Contractor sites publish per-area "2026 rebuild guides" (DWD, Lytemods, Golden Line, Alto, ZMA), showing heavy competition for homeowner leads. | Bid volume; speed from PDF to bid; materials price shocks. Software Lite/Plus fit. | [SMDP PaliBuilds](https://smdp.com/palibuilds-is-rewriting-the-rebuild-playbook-in-pacific-palisades); [DWD Altadena](https://www.dwdbuilders.com/intel/altadena-wildfire-rebuild-contractor-guide-2026) |
| **S7 Lot buyers / developers** | Investors bought about 2 in 5 lots sold (versus about 21% pre-fire). Lots cost $510K (Altadena) and $1.6M (Palisades). LA Times: "Locals wanted to rebuild … Then the big investors moved in." | Fast cost estimate and pro forma before an offer. Service fit, **but reputational risk** (see P). | [LAist Redfin](https://laist.com/brief/news/housing-homelessness/los-angeles-fires-january-2025-redfin-investor-purchase-empty-lots-sales); [Yahoo/LA Times](https://www.yahoo.com/news/articles/locals-wanted-rebuild-pacific-palisades-110000300.html) |

**Secondary US markets: NOT researched this session (search budget exhausted).** Background knowledge below is labelled and must be verified before any use:
- Lahaina, Maui (fire of Aug 8, 2023): about 2,200 structures destroyed, mostly residential. [Background, unverified]
- Hurricane Helene (late September 2024): severe flood and landslide losses across western NC (Buncombe/Asheville; Chimney Rock village largely destroyed) and Florida's Big Bend. [Background, unverified]
- Hurricane Milton (October 2024): Tampa Bay and Florida's west coast. In flood-zone rebuilds, FEMA/NFIP's "substantial damage" (50%) rule drives elevation costs. [Background, unverified]
- 2025–2026 disasters: none researched. [Gap]

### Inferences
- [Likely] **Pages:**
  - Justified: one LA hub plus an **Altadena** spoke (covering Pasadena), a **Palisades** spoke and a **Malibu** spoke. Their cost bands, permit regimes (County vs City of LA vs Malibu/coastal), insurance profiles and lot values all differ materially, which passes the framework's "local page only where supply, price or regulation differ" test.
  - Not justified: a separate West vs East Altadena page. Cover the difference as sections, because no east/west cost or permit data exists.
- [Likely] **Do not** build Lahaina, WNC or Florida pages until researched. When they are, a single "rebuild cost after a disaster: how to estimate" national page with state sections is safer than templated city pages (the scaled-content-abuse risk in the framework).
- [Likely] The **builder** and **lot-buyer** segments need no geography split beyond the hub. Their prompts are tool and price prompts.

### Gaps
- ACS income and age figures for Altadena and the Palisades were not pulled (Census not reachable).
- Per-area FAIR Plan shares for 2025–2026 were not found.
- No east/west Altadena split of permits or costs.
- Malibu homes-destroyed count not found.
- Secondary markets not researched.

---

## C. Jobs-to-be-done in their words

### Takeaway
Five jobs recur across news, survivor groups and vendor positioning. The first two are where Quotr's line-item estimating is directly relevant. The third is a Quotr Service/pro forma job. The fourth is a Procurement job. The fifth is a Software job.

### Cited Findings
- Survivors are told to "obtain multiple contractor estimates before accepting any settlement" and to verify CSLB licenses, which is the common advice in rebuild guides (search extract across [CNN](https://www.cnn.com/2026/01/08/us/altadena-la-fires-rebuilding-invs) and [DWD Builders](https://www.dwdbuilders.com/intel/altadena-wildfire-rebuild-contractor-guide-2026)).
- ClaimArchitect's job framing: a rebuild estimate "in a format that insurance companies read" ([LABJ](https://labusinessjournal.com/featured/tool-identifies-insurance-payout-estimate-gaps/)).
- A survivor who is a GC "managed the rebuild himself to cut costs" after a low payout. Another household is "scaling down plans … considering a smaller manufactured house" ([CNN](https://www.cnn.com/2026/01/08/us/altadena-la-fires-rebuilding-invs); paraphrase from search extract).
- Factory-built rebuilds are "gaining ground in Altadena and the Palisades" ([Wildfire LA](https://www.wildfirela.org/2026/03/07/a-faster-path-home-why-factory-built-rebuilds-are-gaining-ground-in-altadena-and-the-palisades/)). The state funded access to pre-built housing ([Governor](https://www.gov.ca.gov/2026/02/06/governor-newsom-announces-funding-for-la-fire-survivors-to-access-pre-built-housing-to-further-speed-recovery-and-maintain-neighborhood-character/)).

### Inferences
JTBD statements, written in buyer language [Likely; phrasing synthesized from the sources above, not verbatim]:
1. **"Know what it really costs to rebuild my house, line by line, before I accept the insurance settlement."** (homeowner; S1–S4)
2. **"Tell me whether this contractor's bid is fair, so I don't get gouged or scammed."** (homeowner; all)
3. **"Figure out whether to rebuild, build smaller, or sell the lot, with real numbers."** (homeowner, S3/S1; lot buyer S7)
4. **"Stretch the insurance money by buying windows, cabinets and flooring for less, without risking code or quality."** (owner-builder, builder; Procurement)
5. **"Turn the architect's PDFs into a bid fast, because I have more rebuild requests than I can price."** (small builder S6; Software)

### Gaps
- No switch interviews. These JTBDs must be validated with 6–12 recent rebuild decision-makers (the framework's protocol).

---

## D. Psychology: trauma, distrust, insurance dynamics, community, hot/cold moments, biases

### Takeaway
The buyer is displaced, older than the typical software buyer (especially in West Altadena), and negotiating against an insurer that anchors the number through its own estimating software. Distrust of contractors is earned: there are documented unlicensed-contractor stings and frauds. Community identity ("Altadena Not for Sale", "more determined than ever") pushes toward rebuilding. Calendar landmarks (anniversaries, the 24-month ALE mark) create the hot moments. Design around the robust biases (anchoring, defaults, temporal landmarks, time pressure), not around generic social proof.

### Cited Findings
- **Insurer anchoring is built in:** carriers set dwelling limits with Verisk's 360Value, and adjusters price losses with Verisk's Xactimate ([Bankrate via AOL](https://www.aol.com/replacement-cost-reality-check-home-144324677.html)). UP: "Insurers' own rebuild estimates are driving most underinsurance" ([UP](https://uphelp.org/insurers-own-rebuild-estimates-are-driving-most-underinsurance-study-finds/)).
- **Adversarial dynamics persist:** attorneys "are still seeing a steady rise in disputes" more than a year on ([Insurance Journal, Feb 24 2026](https://www.insurancejournal.com/news/west/2026/02/24/859293.htm); search extract). There are FAIR Plan lawsuits ([Legal Newsline](https://www.legalnewsline.com/state-courts/altadena-palisades-residents-sue-fair-plan-over-wildfire-claim-denials-underpayments/article_2a49a61f-3ef9-4265-819d-e06581faa79c.html)). The Every Fire Survivors Network (EFSN) and UCLA launched an insurer-by-insurer conduct survey in September 2026 ([HeySoCal](https://heysocal.com/2026/09/15/fire-survivors-ucla-launch-insurance-survey); [Pasadena Now](https://pasadenanow.com/main/altadena-founded-survivor-network-opens-insurance-survey-to-build-a-public-record-of-how-insurers-performed)).
- **Contractor fraud is real:**
  - Two Altadena homeowners "moved too fast" and sent tens of thousands to an unlicensed contractor ([ABC7](https://abc7.com/post/altadena-homeowners-hoping-rebuild-eaton-fire-sent-thousands-man-turned-unlicensed-contractor/17876660/)).
  - An $18,000 deposit was lost ([Moneywise](https://moneywise.com/news/news/california-wildfire-contractor-fraud-scam)).
  - An email-interception invoice scam ([Spectrum, Sep 18 2026](https://spectrumlocalnews.com/ca/california/wildfires/2026/09/18/altadena-fire-survivor-scams)).
  - Six unlicensed contractors were charged after a Palisades sting over >$1M in bids ([SM Mirror, Jul 2026](https://smmirror.com/2026/07/undercover-sting-catches-fraudulent-rebuilding-schemes-operating-in-pacific-palisades/)).
  - The County approved a unanimous anti-fraud education campaign ([SMDP](https://www.smdp.com/la-county-moves-to-shield-fire-survivors-from-contractor-scams/); [MyNewsLA, Sep 1 2026](https://mynewsla.com/crime/2026/09/01/laco-looks-to-crack-down-on-scams-targeting-wildfire-victims/)).
- **Community influence:**
  - Department of Angels: 90% plan to rebuild, with a majority "more determined than ever" ([LAist](https://laist.com/brief/news/climate-environment/fire-rebuilding-costs-new-funds-financing-attempt-to-fill-gaps)).
  - The Altadena Not for Sale tracking ([SMDP](https://www.smdp.com/investors-snap-up-fire-zone-properties-and-housing-recovery-struggles/)).
  - Calls to protect the community from "predatory developers" ([LA Public Press](https://lapublicpress.org/2025/05/altadena-eaton-fire-rebuild-landlords-newsom/)).
- **Financial strain:** most survivors are "still displaced and struggling financially" one year on ([California Community Foundation](https://www.calfund.org/news-and-events/a-year-after-la-wildfires-most-survivors-are-still-displaced-and-struggling-financially-department-of-angels-survey-finds/)).
- **Age:** more than half of Black homeowners in Altadena are 65+, which raises exposure to underinsurance, predatory buyers and multi-year timelines ([HCN](https://www.hcn.org/articles/a-year-after-the-eaton-fire-permit-delays-keep-black-families-from-returning/)).
- **Framework replication ranking** (from the uploaded framework):
  - robust: defaults/status quo (d = 0.68), anchoring, temporal landmarks (fresh-start), time pressure → noncompensatory choice (Dhar & Nowlis), and the hot–cold empathy gap;
  - fragile: generic social proof and choice overload (d ≈ 0.02).

### Inferences
**Hot vs cold moments (dates verified in F):**

| Moment | Mode | Why |
|---|---|---|
| Contractor bid arrives above Coverage A | **Hot** | Bid shock combined with fraud fear. "Moved too fast" is the documented failure mode. |
| Adjuster's estimate or settlement offer arrives | Hot → cold | The anchor is set; owners need time to compare. |
| Jan 7 anniversary (2026, **2027**) | Hot | Temporal landmark, media wave, and the 24-month ALE mark in 2027. |
| ALE extension request or denial | Hot | Housing is at stake. |
| Lot listing comps / investor letter | Cold → hot | Rebuild-vs-sell arithmetic, then an offer deadline. |
| Permit issued → construction start | Cold | Materials and finish decisions; Procurement window. |
| Builder: bid backlog | Hot (operational) | Lost jobs from slow estimates. |

**Biases to design around** [Likely, applying the framework]:
- **Anchoring (robust).** The insurer's 360Value/Xactimate number and the first contractor bid both anchor. Counter-anchor with **dated, sourced per-sq-ft bands by area** and a line-item template. The goal is to show components, not to argue a number.
- **Default / status quo (robust).** "Like-for-like" rebuilds get expedited plan check ([LA County FAQ](https://recovery.lacounty.gov/faq/)). That is choice architecture favouring same-size rebuilds, so content should price **like-for-like first** and then show the cost of deviation.
- **Temporal landmarks (robust).** Jan 7 anniversaries and the 24-month ALE mark. Refresh content and pitch data in December–January.
- **Time pressure (robust).** Under pressure, survivors use noncompensatory rules (e.g. "is the license valid?"). Urgent pages should lead with 1–2 decisive cues: a CSLB check and "never pay more than X up front" (verify the legal limit before stating it).
- **Social proof (fragile generically, but local identity matters).** Do not use "thousands of homeowners trust us". Use named local institutions instead (nonprofit partners, local press).
- **Trauma and decision fatigue:** [Likely, not directly sourced]. No study found. The search for "decision fatigue" returned nothing specific. Treat it as an interview hypothesis.

### Gaps
- No first-person Reddit or Facebook verbatims (both inaccessible).
- No study of decision fatigue in this population.
- Device and engine usage by age segment is unknown.

---

## E. Four forces with verbatim quotes

### Takeaway
Push (the gap, red tape, ALE) is loud in the record. Pull is split between "an estimate insurers will read", factory-built speed, and gap financing. Anxiety centres on fraud, investors and being lowballed. Habit shows up as like-for-like defaults and deference to the insurer's number. **Caveat:** I could not collect first-person Reddit or Facebook posts. The quotes below are verbatim **as rendered in search-result extracts or headlines**, and the type of each is labelled. Several are headlines or reporter text, not survivor voice.

### Cited Findings

| # | Force | Verbatim quote | Speaker type | URL |
|---|---|---|---|---|
| 1 | Push | "Rebuilding Altadena bogs down in red tape and frustration" | Advocacy headline (UP) | [uphelp.org](https://uphelp.org/rebuilding-altadena-bogs-down-in-red-tape-and-frustration/) |
| 2 | Push | "Many homeowners still face a gap of 40% to 50% of their rebuild costs, often hundreds of thousands of dollars, after insurance proceeds" | Nonprofit program materials (Altadena Land Initiatives) via reporter | [Pasadena Now](https://pasadenanow.com/main/eaton-fire-survivors-nonprofit-opens-zero-interest-rebuild-financing-to-more-altadena-homeowners) |
| 3 | Push | "the average insurance payout is roughly $600 per square foot short for a realistic rebuild in the Palisades" | Reporter, relaying a vendor's data | [Spectrum News 1](https://spectrumlocalnews.com/ca/california/wildfires/2026/01/22/insurance-payouts-short-in-palisades) |
| 4 | Push | "Red tape or red ink? Permitting data suggests latter causing lag on rebuilding Altadena" | Trade-press headline | [The Real Deal](https://therealdeal.com/la/2026/09/08/more-than-400-permitted-rebuilds-sit-in-limbo-in-altadena/) |
| 5 | Push | "A year after the Eaton Fire, permit delays keep Black families from returning" | News headline | [High Country News](https://www.hcn.org/articles/a-year-after-the-eaton-fire-permit-delays-keep-black-families-from-returning/) |
| 6 | Pull | "We reconstruct the home in digital, CAD-level detail, that allows us to get much more accurate rebuild quote in a format that insurance companies read." | Vendor founder (ClaimArchitect) | [LA Business Journal](https://labusinessjournal.com/featured/tool-identifies-insurance-payout-estimate-gaps/) |
| 7 | Pull | "A Faster Path Home: Why Factory-Built Rebuilds Are Gaining Ground in Altadena and the Palisades" | Community news headline | [Wildfire LA](https://www.wildfirela.org/2026/03/07/a-faster-path-home-why-factory-built-rebuilds-are-gaining-ground-in-altadena-and-the-palisades/) |
| 8 | Pull / Anxiety | "Your insurance company sent in their team; here's why you need yours" (title from URL slug; punctuation approximate) | Public-adjuster-style local column | [Palisadian-Post](https://palipost.com/your-insurance-company-sent-in-their-team-heres-why-you-need-yours/) |
| 9 | Anxiety | "A California wildfire survivor says she paid a contractor $18,000 to rebuild her home — then he disappeared before finishing the job" | News headline, survivor story | [Moneywise](https://moneywise.com/news/news/california-wildfire-contractor-fraud-scam) |
| 10 | Anxiety | "Altadena homeowners hoping to rebuild after Eaton Fire sent thousands to alleged unlicensed contractor" | News headline, survivor story | [ABC7](https://abc7.com/post/altadena-homeowners-hoping-rebuild-eaton-fire-sent-thousands-man-turned-unlicensed-contractor/17876660/) |
| 11 | Anxiety | "Locals wanted to rebuild Pacific Palisades, Altadena. Then the big investors moved in" | LA Times headline (syndicated) | [Yahoo News](https://www.yahoo.com/news/articles/locals-wanted-rebuild-pacific-palisades-110000300.html) |
| 12 | Anxiety | Warning signs: "vague or blank contracts, refusing to show their proof of license or requesting large upfront payments" | Consumer advocate, via reporter | [Moneywise](https://moneywise.com/news/news/california-wildfire-contractor-fraud-scam) (attribution within the result set approximate) |
| 13 | Anxiety (analog market) | "It's a gut punch" (Marshall fire survivors, Colorado, on being underinsured) | Survivor voice, in headline | [UP](https://uphelp.org/its-a-gut-punch-marshall-fire-survivors-fear-their-homes-were-underinsured-and-they-cant-afford-to-rebuild/?print=print) |
| 14 | Habit | Survivors are "more determined than ever" to rebuild | Survey report language (Department of Angels) | [LAist](https://laist.com/brief/news/climate-environment/fire-rebuilding-costs-new-funds-financing-attempt-to-fill-gaps) |
| 15 | Habit / trust boundary | ClaimArchitect is "not a public adjusting firm, law firm, or insurance company" and "does not negotiate, adjust, or settle insurance claims" | Vendor disclaimer | [claimarchitect.com](https://claimarchitect.com/press/palisades-fires-gap) (page set approximate) |
| 16 | Habit | Rebuild projects "are considered like-for-like replacements and will receive an expedited plan check" (as rendered in extract) | Government FAQ | [LA County Recovers FAQ](https://recovery.lacounty.gov/faq/) |

### Inferences
- [Likely] **The force mix by prompt class:**
  - push → "why is my insurance so far short", "why is my rebuild stuck";
  - pull → "independent estimate", "prefab cheaper?";
  - anxiety → "is this bid fair / is this contractor legit / should I sell";
  - habit → "can I just take the insurer's number and rebuild the same house".
- Quotr's pull story (an independent, line-item, fast, cheap estimate) maps to quotes 3 and 6. But quote 15 shows the boundary competitors draw: estimate, never adjust.
- [Likely] Anxiety prompts (9–12) are where trust proof decides the outcome. A Bay Area startup with no LA references starts at a disadvantage.

### Gaps
- **The ≥8 first-person survivor verbatims from Reddit (r/Altadena, r/LosAngeles, r/PacificPalisades), Nextdoor and public Facebook groups were not collected**, because the search tool cannot reach reddit.com and fetch was blocked.
- Joy Chen's (EFSN) "huge gaps…" line and Amy Bach's 75–80% expectation came only as paraphrases, so they are not listed as quotes.
- Recommend 2–4 hours of manual community mining with the framework's codebook before publishing.

---

## F. Trigger events and trigger calendar

### Takeaway
The next 15 months hold three hard landmarks: the **Jan 7, 2027 second anniversary and 24-month ALE mark**, the **24-month SBA drawdown windows** (counted per borrower), and the **Jan 7, 2028 36-month mark**. Add rolling triggers: bid shock, adjuster estimates, permit issuance, lot offers, Zone 0 finalization, and new California insurance laws that take effect Jan 1, 2027.

### Cited Findings

| Date | Trigger | Status | Source |
|---|---|---|---|
| Jan 7, 2025 | Palisades and Eaton fires; 100% contained after 24 days | Known | [TODAY](https://www.today.com/today/amp/rcna190281) |
| Jan 7, 2025 → Jan 7, 2026 | PC 396 price-gouging protections for **building materials and construction** in LA County, extended by executive order to Jan 7, 2026. **No later extension found** for construction. Rental-housing protections ran through Mar 29, 2026. | Known (expiry); later status unverified | [Governor, Feb 1 2025](https://www.gov.ca.gov/2025/02/01/icymi-state-continues-to-protect-la-firestorm-survivors-from-price-gouging/); [LA City Attorney report, Mar 12 2026](https://cityclerk.lacity.org/onlinedocs/2025/25-0006-S77_rpt_atty_03-12-26.pdf) |
| Feb 6–7, 2025 | Quotr's paid release on FireTips (free LA rebuild-cost app) | Known | [Blogspot repost](https://rcnamericaca.blogspot.com/2025/02/quotr-launches-la-focused-app-to-help.html); [EIN Presswire](https://www.einnews.com/pr_news/783445824/quotr-launches-la-focused-app-to-help-homeowners-get-accurate-information-rebuild-faster-after-devastating-fires) |
| 2025 (rolling) | Debris removal completions (e.g. >1,000 Palisades properties) → design and permit filing starts | Known (exact dates in release) | [Mayor Bass](https://mayor.lacity.gov/news/mayor-bass-highlights-completion-debris-removal-more-1000-properties-palisades-efficiency) |
| Nov 21, 2025 / early Dec 2025 | First CofOs (Palisades / Altadena): "it can be done" proof moments | Known | [LA Downtown News](https://www.ladowntownnews.com/news/palisades-rebuild-first-certificate-of-occupancy-issued-as-recovery-accelerates/article_02a255e2-76e0-4ae4-ae9a-d7ff654676fa.html); [ABC7](https://abc7.com/post/first-fully-rebuilt-home-altadena-eaton-fire-given-certificate-occupancy-meaning-safe-cleared-move/18249727/) |
| Dec 23, 2025 | State and LA Rises rebuild resource page (includes Archistar AI permitting) | Known | [Governor](https://www.gov.ca.gov/2025/12/23/governor-and-la-rises-announce-new-online-resource-to-further-help-la-fire-survivors-navigate-rebuilding/) |
| Jan 7, 2026 | 1st anniversary; SBA deadline extension; media wave (CNN, NBC, Marketplace) | Known | [SBA/Mammoth Times relay](https://business.mammothtimes.com/mammothtimes/article/gnwcq-2026-1-7-on-one-year-anniversary-of-california-wildfires-sba-extends-disaster-relief-deadlines-as-local-bureaucrats-stall-recovery); [CNN](https://www.cnn.com/2026/01/08/us/altadena-la-fires-rebuilding-invs) |
| Feb 6, 2026 | State funding for pre-built housing | Known | [Governor](https://www.gov.ca.gov/2026/02/06/governor-newsom-announces-funding-for-la-fire-survivors-to-access-pre-built-housing-to-further-speed-recovery-and-maintain-neighborhood-character/) |
| Mar 2026 | UP 12-month survey published | Known | [UP PDF](https://uphelp.org/wp-content/uploads/2026/03/UP-Survey-2025-LA-Wildfires-12-MO-Summary-Results-Export.pdf) |
| Jun 30, 2026 → Jul 1, 2026 | SBA final extension: approved borrowers get **24 months from their loan authorization date** to draw funds; Builder Self-Certification option added. About $3.4B approved for about 13,000 LA borrowers; about $1B reportedly disbursed. | Known | [SBA, Jul 1 2026](https://www.sba.gov/article/2026/07/01/sba-announces-final-disaster-relief-extension-january-2025-los-angeles-wildfire-survivors); [SBA, Jun 16 2026](https://www.sba.gov/article/2026/06/16/final-deadline-accept-sba-disaster-funds-los-angeles-wildfires-approaching); [Spectrum](https://spectrumlocalnews.com/ca/california/business/2026/07/01/kathryn-barger-urges-la-county-residents-to-apply-for-disaster-relief) |
| Aug 19 / Aug 28, 2026 | Board of Forestry adopts **emergency Zone 0** rules (5-ft ember-resistant zone) and sends them to the Office of Administrative Law (OAL). New structures comply on adoption; existing ones within about 3 years. OAL approval **not confirmed**. | Known (adoption); effective date unverified | [BB&K](https://bbklaw.com/resources/la090926-california-board-of-forestry-adopts-emergency-zone-0-regulations-under-ab-3074); [KRCR](https://krcrtv.com/news/local/california-approves-zone-0-rules-what-homeowners-need-to-know); [Pasadena agenda, Apr 2026](https://ww2.cityofpasadena.net/2026%20Agendas/Apr_13_26/AR%2013.pdf) |
| Sep 1, 2026 | LA County anti-contractor-fraud measures | Known | [MyNewsLA](https://mynewsla.com/crime/2026/09/01/laco-looks-to-crack-down-on-scams-targeting-wildfire-victims/) |
| Sep 15, 2026 | **AB 1847** signed: mortgage forbearance extended from 12 to 24 months; request deadline **Jan 7, 2029**. EFSN/UCLA insurer survey launches. | Known (secondary sources) | Search extract across [coverageclassroom](https://coverageclassroom.com/learn/california-disaster-insurance-claim-rights) / [financialsupportresources](https://www.financialsupportresources.com/post/la-wildfire-displacement-help-2027); [HeySoCal](https://heysocal.com/2026/09/15/fire-survivors-ucla-launch-insurance-survey) |
| Oct 2026 | Department of Angels "Community Voices" October 2026 report (exists; contents not read) | Known (existence) | [DoA PDF](https://static1.squarespace.com/static/6792c245599ed84703227b1e/t/6ad6b10d415a5710f7c384cd/1792454925809/Department+of+Angels+Community+Voices+LA+Fire+Recovery+Report_October+2026.pdf) |
| **Jan 1, 2027** | New California law(s) take effect, including an ALE protection for smoke-damaged homes: no termination of ALE until the home is restored and cleared for occupancy | Likely (secondary source) | [propertyinsurancecoveragelaw](https://www.propertyinsurancecoveragelaw.com/blog/california-wildfire-ale-extensions/) |
| **Jan 7, 2027** | **24-month ALE mark** under Ins. Code §2060, which requires at least 24 months after a state-of-emergency loss, plus up to 12 more months for delays beyond the owner's control. Not an automatic cutoff; the dollar limit is unchanged. Also the 2nd anniversary. | Known (law via secondary sources and the CDI tips page) | [propertyinsurancecoveragelaw](https://www.propertyinsurancecoveragelaw.com/blog/california-wildfire-ale-extensions/); [CDI Top Ten Tips](https://www.insurance.ca.gov/01-consumers/140-catastrophes/TopTenTips_WildfireClaimants.cfm); [CDI Bulletin 2025-2](https://www.insurance.ca.gov/0250-insurers/0300-insurers/0200-bulletins/bulletin-notices-commiss-opinion/upload/Bulletin-2025-2-Wildfire-Consumer-Protections-and-Advanced-Payments.pdf) |
| ~Jul 2027 → mid-2028 | SBA 24-month drawdown windows close **borrower by borrower** (each authorization date + 24 months) | Known (rule); dates vary | [SBA](https://www.sba.gov/article/2026/07/01/sba-announces-final-disaster-relief-extension-january-2025-los-angeles-wildfire-survivors) |
| **Jan 7, 2028** | 36-month mark: end of the maximum ALE extension. Likely also the deadline to collect replacement-cost holdback (the Ins. Code §2051.5 36-month rule), but **not verified this session**. | Likely | [coverageclassroom](https://coverageclassroom.com/learn/california-rebuilding-after-wildfire-insurance) (not opened) |
| Jan 7, 2029 | AB 1847 forbearance request deadline | Known (secondary) | as above |
| Rolling | Adjuster Xactimate estimate / settlement offer; contractor bid; permit issued; investor letter or lot comps; SCE claim decision (Eaton) | Known as event types | [SCE claim guide](https://victorcaballero.com/filing-a-claim-with-sce-for-eaton-fire-damage-what-altadena-and-pasadena-residents-need-to-know/) |
| Pending | **SB 876** (larger extended replacement cost / law-and-ordinance cushions; one extract says ≥50% ERC and 20% law-and-ordinance). **Enactment status and effective date conflict across sources.** **AB 597** (15% cap on public adjuster fees, applied to additional recovery) is listed as dead or in committee. | Unverified | [Insurance Business](https://www.insurancebusinessmag.com/us/news/catastrophe/california-mandates-bigger-rebuild-cushions-as-voters--demand-the-right-to-sue-insurers-592887.aspx); [Digital Democracy SB 876](https://calmatters.digitaldemocracy.org/bills/ca_202520260sb876); [BillTrack50 AB 597](https://www.billtrack50.com/billdetail/1833028) |

### Inferences
- [Likely] **The peak demand window for Quotr content is December 2026 to February 2027.** The anniversary media wave, the 24-month ALE mark and new-law explainers all coincide. Sample AI prompts more often around it, as the framework does for calendar-periodic clusters.
- [Likely] The SBA drawdown deadlines and the Builder Self-Certification option create a **documented-budget need**: a line-item estimate to support each draw. That is a natural Service use case. Speculative until SBA documentation requirements are checked.
- [Likely] Zone 0 finalization creates a **cost-adder question** ("what do Zone 0 and Chapter 7A add?"). Quotr can answer it from takeoffs.

### Gaps
- The §2051.5 36-month rule was not verified. SB 876 status and SB 495 (contents) status were not verified.
- No dates for the "SB 549/AB rebuild laws" named in the brief; I found nothing on SB 549.
- Debris-removal completion dates by area were not retrieved. OAL approval of Zone 0 is unconfirmed.
- The price-gouging status after Jan 7, 2026 is unconfirmed.

---

## G. Switch timeline with prompt form at each stage

### Takeaway
Prompt specificity rises as the buyer moves along the timeline. Quotr's winnable entry is at "active looking" (cost and estimate prompts) and "deciding" (bid-check and rebuild-vs-sell prompts).

### Cited Findings
- Framework: first-thought prompts are vague and situational; active-looking prompts carry category nouns; deciding prompts carry brands, prices and objections (uploaded framework).
- Stage evidence: debris removal → permits (expedited for like-for-like) → construction → CofO ([LA County Road to Rebuilding](https://recovery.lacounty.gov/road/); [Fire Rebuild FAQ](https://recovery.lacounty.gov/wp-content/uploads/2025/02/Fire-Rebuild-FAQ.pdf)).

### Inferences

| Stage | Typical moment (LA) | Prompt form [SIMULATED examples] | Quotr role |
|---|---|---|---|
| First thought | Weeks 0–8; ALE starts; the insurer calls | "my house burned down in the Eaton fire what do I do first" | None (UP, CDI and the county own this) |
| Passive looking | Debris cleared; coverage letter read | "is $600k enough to rebuild a house in Altadena" | Cost hub (counter-anchor) |
| Active looking | Adjuster estimate received; architect hired | "how to get an independent rebuild cost estimate for an insurance claim Los Angeles" / "cost per sq ft rebuild Altadena 2026" | Line-item estimate page; Service; calculator |
| Deciding | Contractor bids in; lot offer in hand | "is $780k a fair bid for a 1,400 sq ft rebuild in Altadena" / "rebuild or sell my Palisades lot" / "ClaimArchitect vs public adjuster" | Bid-check page; rebuild-vs-sell page; brand/comparison pages |
| Consuming / building | Permit issued; finishes chosen | "cheaper windows and cabinets for fire rebuild tariffs" / "Zone 0 compliant materials cost" | Procurement; materials cost pages |
| Builder track | Bid backlog | "estimating software for residential rebuild contractors PDF plans" | Software Lite/Plus |

### Gaps
- Real prompt phrasing per stage needs switch interviews and the "what did you type, and where?" question.

---

## H. Current alternatives and what fails to satisfy

### Takeaway
The market is crowded with free government and nonprofit navigators, contractor-marketing cost guides, and one directly competing vendor stack (**PaliBuilds / Bidsy / ClaimArchitect**). What is missing is an independent, dated, line-item cost reference that is neither the insurer's nor a contractor's. Trust gaps (fraud), the insurance gap itself, and financing are the most frequent unmet needs.

### Cited Findings

| Alternative | What it does | What fails (evidence) | Source |
|---|---|---|---|
| Insurer's 360Value limit + adjuster's Xactimate estimate | Sets Coverage A and prices the loss | Insurers' own estimates "driving most underinsurance". In the AAA cohort, the adjuster's estimate was 41% above coverage. | [UP](https://uphelp.org/insurers-own-rebuild-estimates-are-driving-most-underinsurance-study-finds/); [LAist](https://laist.com/brief/news/climate-environment/eaton-palisades-fire-altadena-aaa-insurance-rebuild-costs); [AOL/Bankrate](https://www.aol.com/replacement-cost-reality-check-home-144324677.html) |
| Public adjusters | Negotiate the claim for a fee | California had "no limit" on fees per CDI's proposal context; the 15% cap (AB 597) was not enacted as far as found. CDI restricts solicitation in the wildfire areas. | [Insurance Business / propertyinsurancecoveragelaw](https://www.propertyinsurancecoveragelaw.com/blog/ab-597-public-adjuster-fee-cap/); [CDI notice](https://www.insurance.ca.gov/0250-insurers/0300-insurers/0200-bulletins/bulletin-notices-commiss-opinion/upload/Notice-Solicitation-by-Public-Adjusters-in-the-Southern-California-Wildfire-Areas.pdf) |
| Attorneys | Bad-faith and FAIR Plan litigation | Slow; disputes rising | [Insurance Journal](https://www.insurancejournal.com/news/west/2026/02/24/859293.htm) |
| **ClaimArchitect** (PaliBuilds) | AI, CAD-level rebuild valuation from the policy and adjuster's estimate. Flat fee, refunded if the valuation doesn't beat the adjuster's estimate. Neighbourhood pages (Palisades underinsurance, smoke damage). | Palisades-centric; self-reported results (37 cases) | [LABJ](https://labusinessjournal.com/featured/tool-identifies-insurance-payout-estimate-gaps/); [claimarchitect.com/pacific-palisades](https://claimarchitect.com/pacific-palisades/) |
| **Bidsy / PaliBuilds** | 200+ local GCs and subs; free office hours on Wednesdays at the Palisades Recovery Center | Palisades-only | [SMDP](https://smdp.com/palibuilds-is-rewriting-the-rebuild-playbook-in-pacific-palisades); [Circling the News](https://www.circlingthenews.com/?p=43106) |
| LA Builders Alliance interactive tool | Connects homeowners with a builder | Builder-referral, not independent pricing | [Westside Current](https://www.westsidecurrent.com/pacific_palisades/free-interactive-tool-launched-to-support-palisades-fire-rebuilding/article_3f659d66-4265-4e32-9316-47e769612825.html) |
| State / LA Rises portal (Archistar AI permitting); LA County Recovers; LA Times-covered rebuild portal | Navigation, permitting | No cost estimates found in extracts | [Governor](https://www.gov.ca.gov/2025/12/23/governor-and-la-rises-announce-new-online-resource-to-further-help-la-fire-survivors-navigate-rebuilding/); [LA Times via Magzter](https://www.magzter.com/es/stories/newspaper/Los-Angeles-Times/PORTAL-AIMS-TO-STREAMLINE-REBUILDS-AFTER-LA-FIRES) |
| Contractor cost guides (DWD, Lytemods, Golden Line, Alto, ZMA, UBIC, Amerbuild, Vaisman) | Per-sq-ft ranges, permit counts by area, "2026" in the title | Self-interested; ranges vary widely; one admits "no … dataset" exists | see A |
| Factory-built / modular (state-funded pre-built option; Homebound's LA program page) | Faster or cheaper path | Fit with lot, design and permits; comparisons unclear | [Wildfire LA](https://www.wildfirela.org/2026/03/07/a-faster-path-home-why-factory-built-rebuilds-are-gaining-ground-in-altadena-and-the-palisades/); [Homebound](https://homebound.com/la-fire-recovery) |
| Nonprofits (Department of Angels, EFSN, ALI, the BET/NAACP fund, UP) | Surveys, advocacy, zero-interest gap loans, grants | Do not produce estimates | see B/D |
| Quotr FireTips (Feb 2025) | Free, ZIP-localized, GenAI rebuild cost estimate plus timeline summary for total/major-loss owners | Current status unknown; on a legacy domain; only a blogspot repost surfaced in search | [Blogspot repost](https://rcnamericaca.blogspot.com/2025/02/quotr-launches-la-focused-app-to-help.html); [entity fact sheet](../../geo-brain/00-quotr/entity-fact-sheet.md) |

**Unmet needs ranked by frequency in this source set** [Estimate: count of distinct sources in this note raising each]:
1. Insurance gap / underinsurance (≈14 sources)
2. Contractor trust and fraud (≈8)
3. Permit or "limbo" delays (≈7)
4. Gap financing (≈6)
5. Investor pressure to sell (≈6)
6. An independent, credible cost number (≈4, explicitly the "no dataset" admission plus ClaimArchitect)
7. Materials and tariff costs (≈2)

### Inferences
- [Likely] **Quotr's real white space is an independent, dated, line-item cost reference**, published openly, separate from claim negotiation. ClaimArchitect owns the "valuation to dispute the insurer" slot in the Palisades. Quotr can be the area-wide **cost transparency layer** plus the **builder and materials layer**, where no competitor in this note operates.
- [Likely] Unmet need #6 is low-frequency but high-leverage. AI engines currently answer cost prompts from contractor marketing, a thin and conflicted pool. That is the framework's "thin comparison shelf" condition.

### Gaps
- ClaimArchitect's fee was not found. The current state of FireTips could not be checked (403). Modular companies were not compared.

---

## I. Willingness to pay, price anchors, who pays, sales cycle

### Takeaway
Anchors are large: public adjusters take an uncapped percentage of the claim, and gaps run to hundreds of thousands of dollars. Quotr's Service price is tiny by comparison ($375–$1,000 for a typical home at $0.25/sq ft). For homeowners the price objection is trust, not price. For builders, Software at $79.90/seat/month competes with spreadsheets.

### Cited Findings
- Public adjuster fees had no statutory cap. AB 597 proposed **15%**, calculated only on additional recovery; it was not enacted as far as found ([propertyinsurancecoveragelaw](https://www.propertyinsurancecoveragelaw.com/blog/ab-597-public-adjuster-fee-cap/); [BillTrack50](https://www.billtrack50.com/billdetail/1833028)). The industry campaigned against the cap ([Newswire](https://www.newswire.com/news/wildfire-victims-warn-ab-597-would-strip-critical-support-from-22600454)).
- ClaimArchitect charges a flat fee with a money-back guarantee if its valuation does not exceed the adjuster's estimate (amount not found) ([LABJ](https://labusinessjournal.com/featured/tool-identifies-insurance-payout-estimate-gaps/)).
- Quotr Service: **$0.25/sq ft under 50,000 sq ft**, with estimates delivered in 3–4 business days and pro formas in 2–3. Quotr Software: Lite **$79.90**, Plus **$299.90** per seat per month ([product-and-features.md](../../geo-brain/00-quotr/product-and-features.md)).
- Money sources for the gap: SBA ($3.4B approved; [SBA](https://www.sba.gov/article/2026/07/01/sba-announces-final-disaster-relief-extension-january-2025-los-angeles-wildfire-survivors)); ALI zero-interest loans ([Pasadena Now](https://pasadenanow.com/main/eaton-fire-survivors-nonprofit-opens-zero-interest-rebuild-financing-to-more-altadena-homeowners)); the BET/NAACP fund ([BET](https://www.bet.com/article/kohaj0/altadena-community-preservation-fund-launched-to-support-black-homeowners-impacted-by-eaton-fire)); SCE claims for Eaton ([SCE claim guide](https://victorcaballero.com/filing-a-claim-with-sce-for-eaton-fire-damage-what-altadena-and-pasadena-residents-need-to-know/)).
- One builder FAQ says pre-construction, permits, housing and finishes add **25–60%** to the base contract (vendor claim from a search extract; which page holds it is uncertain, most likely [DWD Builders](https://www.dwdbuilders.com/intel/altadena-wildfire-rebuild-contractor-guide-2026) or [Altadena Custom Home Builder](https://altadenacustomhomebuilder.com/blog/cost-to-rebuild-a-house-after-a-fire-in-los-angeles-2026-numbers)).

### Inferences
- [Estimate] **Quotr Service on a typical home:** 1,500 sq ft Altadena ≈ **$375**; 2,100 sq ft ≈ $525; 3,800 sq ft Palisades ≈ **$950**. A 15% public adjuster fee on a $300K supplemental recovery would be about $45K. Quotr can credibly say it costs "less than 0.1% of the rebuild" (for example, $525 on a ~$1M rebuild). Do not frame it against adjusters, because Quotr must not imply it recovers claim money.
- [Speculative] Who pays: mostly homeowners, out of pocket or from ALE-adjacent funds. Whether insurers reimburse an independent estimate as a soft cost is **unknown**. For builders and developers it is a normal cost of doing business. Lenders or SBA may require budgets (to verify).
- [Likely] **Sales cycles:** homeowner 1–8 weeks from bid shock to decision, as one purchase in a multi-year process; builder trial-to-paid in days to weeks; developer in days (pre-offer).

### Gaps
- Architect and estimator fee anchors for LA rebuilds were not sourced. Insurer reimbursability of estimate fees is unknown.

---

## J. Vocabulary list

### Takeaway
Content must use the claim, code and permit words survivors use, because AI fan-outs inject them (insurer names, "Xactimate", "Chapter 7A", "Zone 0", "like-for-like").

### Cited Findings
- **Insurance:**
  - Coverage A (dwelling) / Coverage D (ALE, "loss of use"); Ins. Code §2060 ALE 24 + 12 months ([propertyinsurancecoveragelaw](https://www.propertyinsurancecoveragelaw.com/blog/california-wildfire-ale-extensions/)).
  - Extended replacement cost (ERC) and law-and-ordinance / code upgrade coverage (SB 876 context; [Insurance Business](https://www.insurancebusinessmag.com/us/news/catastrophe/california-mandates-bigger-rebuild-cushions-as-voters--demand-the-right-to-sue-insurers-592887.aspx)).
  - **Xactimate** and **360Value** (Verisk) ([AOL/Bankrate](https://www.aol.com/replacement-cost-reality-check-home-144324677.html)).
  - FAIR Plan and difference-in-conditions (FAIR Plan sources in B).
  - Public adjuster ([CDI notice](https://www.insurance.ca.gov/0250-insurers/0300-insurers/0200-bulletins/bulletin-notices-commiss-opinion/upload/Notice-Solicitation-by-Public-Adjusters-in-the-Southern-California-Wildfire-Areas.pdf)).
  - Advance payments ([CDI Bulletin 2025-2](https://www.insurance.ca.gov/0250-insurers/0300-insurers/0200-bulletins/bulletin-notices-commiss-opinion/upload/Bulletin-2025-2-Wildfire-Consumer-Protections-and-Advanced-Payments.pdf)).
  - "Underinsured", "rebuild gap", "shortfall".
- **Building and permits:**
  - like-for-like and expedited plan check ([LA County FAQ](https://recovery.lacounty.gov/faq/));
  - Chapter 7A (WUI) ([DWD](https://www.dwdbuilders.com/intel/altadena-wildfire-rebuild-contractor-guide-2026));
  - Zone 0 / ember-resistant 5-ft zone ([BB&K](https://bbklaw.com/resources/la090926-california-board-of-forestry-adopts-emergency-zone-0-regulations-under-ab-3074));
  - certificate of occupancy (CofO); permitting progress dashboard ([PFAR](https://pfar.org/permitting-progress-dashboard-stay-up-to-date/));
  - septic and coastal (Malibu) ([Lytemods](https://lytemods.com/fire-rebuild/malibu));
  - debris removal ([Mayor Bass](https://mayor.lacity.gov/news/mayor-bass-highlights-completion-debris-removal-more-1000-properties-palisades-efficiency));
  - Builder Self-Certification (SBA) ([SBA](https://www.sba.gov/article/2026/07/01/sba-announces-final-disaster-relief-extension-january-2025-los-angeles-wildfire-survivors));
  - factory-built / pre-built ([Wildfire LA](https://www.wildfirela.org/2026/03/07/a-faster-path-home-why-factory-built-rebuilds-are-gaining-ground-in-altadena-and-the-palisades/)).
- **Community and orgs:** EFSN, Department of Angels, Altadena Land Initiatives, Altadena Not for Sale, LA Rises, PaliBuilds/Bidsy/ClaimArchitect, SCE claim (sources in B, D, H).
- **Fraud:** CSLB license lookup at cslb.ca.gov; home improvement contract ([SMDP](https://www.smdp.com/la-county-moves-to-shield-fire-survivors-from-contractor-scams/)); PC 396 price gouging ([egattorneys](https://www.egattorneys.com/price-gouging-penal-code-396)).

### Inferences
- [Likely] Other terms to cover once verified: ACV vs RCV; recoverable depreciation / holdback; scope of loss; supplement; appraisal clause; proof of loss; ROE (right-of-entry) for debris removal; Phase 1 / Phase 2 debris; soil testing; SB 9 lot split / ADU (relevant to lot buyers).

### Gaps
- Local slang from Reddit and Facebook was not collected.

---

## K. Channels

### Takeaway
This ICP reads hyper-local news and nonprofit channels, attends in-person recovery centers, and is reached through survivor networks. AI engines retrieve from local news, contractor guides, nonprofits and law firms (see O). Facebook group member counts were not obtainable.

### Cited Findings
- **Local news cited in this research:**
  - LAist ([e.g.](https://laist.com/brief/news/climate-environment/eaton-palisades-fire-altadena-aaa-insurance-rebuild-costs))
  - Pasadena Now ([e.g.](https://pasadenanow.com/main/altadena-nonprofit-launches-program-to-help-eaton-fire-survivors-bridge-rebuilding-costs))
  - Palisadian-Post ([e.g.](https://palipost.com/new-survey-seeks-to-record-insurers-postfire-recovery-conduct/)), Palisades News, Circling the News, Westside Current
  - SMDP, Spectrum News 1, ABC7, LA Business Journal, The Real Deal, LA Times (syndicated), CalMatters, High Country News, Marketplace
- **Survivor and community orgs:**
  - EFSN (efsurvivors.net; insurer survey at FireSurvey.org) ([Palisadian-Post](https://palipost.com/new-survey-seeks-to-record-insurers-postfire-recovery-conduct/))
  - Department of Angels ([deptofangels.org](https://www.deptofangels.org/news/helping-community-rebuild-one-connection-at-a-time))
  - Altadena Land Initiatives; Altadena Not for Sale; the BET/NAACP/WME fund
  - UP surveys and workshops ([UP surveys](https://uphelp.org/media/surveys/))
  - LA2050 "Destination Rebuild" ([LA2050](https://la2050.org/ideas/2025/destination-rebuild))
- **In person:** PaliBuilds Wednesday office hours at the Palisades Recovery Center ([Circling the News](https://www.circlingthenews.com/?p=43106)).
- **Government:** LA County Recovers; ca.gov Rebuilding LA; LA Rises ([ca.gov](https://www.ca.gov/lafires/rebuilding-la)).
- **Podcast:** "Rebuild LA" podcast ([Buzzsprout](https://rebuildla.buzzsprout.com/2441905/episodes/17281428-rebuild-la-episode-028-saving-whole-neighborhoods-from-wildfire-with-fire-aside-s-jason-brooks)).

### Inferences
- [Likely] **Engines for this ICP:** Google (AI Overviews / AI Mode) is primary for the 65+ West Altadena segment. ChatGPT matters for professional Altadena and Palisades owners and for builders. Perplexity is optional. This follows Pew's reach figures as cited in the framework.
- [Likely] Steadfast LA (named in the brief) and Facebook groups such as Altadena or Palisades rebuild groups exist, but member counts were not verified.

### Gaps
- Facebook group names and member counts, Nextdoor, subreddit sizes, YouTube channels: none collected (tools blocked). Steadfast LA not verified.

---

## L. Proof required at each stage

### Takeaway
Trust outweighs everything. Each stage needs one verifiable credential that can be checked in a click. Quotr's current proof for this ICP is thin: a sample deliverable, a 2025 paid press release, and no local references.

### Cited Findings
- Survivors are advised to verify CSLB licenses and beware of vague contracts and large upfront payments ([Moneywise](https://moneywise.com/news/news/california-wildfire-contractor-fraud-scam); [SMDP](https://www.smdp.com/la-county-moves-to-shield-fire-survivors-from-contractor-scams/)).
- Competitor proof stack: earned local business press (LABJ, Spectrum), a refund guarantee, a "format insurers read" claim, and a clear "not a PA/law firm" disclaimer ([LABJ](https://labusinessjournal.com/featured/tool-identifies-insurance-payout-estimate-gaps/)).
- Quotr proof: the "Fast Cost Estimation (Residential LA Fire Rebuilding)" sample; a paid EIN release (Feb 2025); no earned press; Bay Area base ([entity fact sheet](../../geo-brain/00-quotr/entity-fact-sheet.md); [product-and-features](../../geo-brain/00-quotr/product-and-features.md)).
- The framework notes that trust in AI recommendations alone falls to 5% for purchases over $500, and that 86% verify elsewhere (uploaded framework).

### Inferences

| Stage | Proof required [Likely] | Quotr has today | Gap |
|---|---|---|---|
| Passive (cost) | Dated per-sq-ft bands by area with sources; method shown | No LA cost page | Build the hub and tracker |
| Active (estimate) | Sample line-item estimate (CSI or Xactimate-like categories); named estimator with credentials; turnaround and price; "not a public adjuster" disclaimer | Sample deliverable; price | Named estimator (**TO CONFIRM** credentials); disclaimer |
| Deciding (bid check) | A bid-comparison checklist that links to CSLB; independence statement (no contractor referral fees) | None | Write a conflict-of-interest policy |
| Deciding (rebuild vs sell) | Lot-value data (Redfin) plus rebuild cost; neutral framing | None | Calculator |
| Building (materials) | Code certs (NFRC, CARB, cUPC per the fact sheet); LA project references; landed-cost examples | Bay Area project cards | LA reference projects |
| Builder (software) | Free trial; residential rebuild demo; local builder testimonial (FTC-compliant) | 7-day trial | Residential/rebuild case |

### Gaps
- Whether Quotr's estimators hold any credentials (CPE/AACE, licensed GC) is unknown (**TO CONFIRM with Quotr**).

---

## M. Coding chains

### Takeaway
Eight chains cover the ICP. Chains 1, 2, 5 and 6 are Quotr's priority; chain 4 is "link out only".

### Inferences
[Likely; chains synthesized from the sourced triggers and forces; prompt text SIMULATED]

| # | Trigger (datable) | Stage | Mode | Restraining force | Exact prompt [SIMULATED] | Proof required |
|---|---|---|---|---|---|---|
| 1 | Contractor bid exceeds Coverage A (the AAA cohort: $928K bids vs $628K coverage) | Deciding | Hot | Anxiety (gouging/fraud) | "A contractor quoted $780,000 to rebuild my 1,400 sq ft house in Altadena. Is that fair for 2026 and what should the line items be?" | Dated per-sq-ft bands by area; line-item template; CSLB link |
| 2 | Adjuster's Xactimate estimate or settlement letter | Active → deciding | Cold | Habit (anchoring on the insurer's number) | "How do I get an independent line-item rebuild estimate for my insurance claim in Los Angeles before I accept the settlement?" | Sample estimate; "estimate, not adjusting" disclaimer; price and turnaround |
| 3 | Investor letter or lot comps ($510K Altadena / $1.6M Palisades) | Deciding | Cold → hot | Anxiety (losing community, lowball) | "Should I rebuild or sell my burned lot in the Palisades? Insurance pays $2.4M, lots sell for $1.6M." | Rebuild cost vs lot value worksheet; Redfin data; neutral |
| 4 | 24-month ALE mark (Jan 7, 2027) | Active | Hot | Push | "My ALE ends January 2027 and my rebuild hasn't started — can I get an extension in California?" | CDI / Ins. Code §2060 citation. **Quotr links out; it does not advise.** |
| 5 | Permit issued, finishes selection | Consuming | Cold | Habit (buy through the GC) | "How can I save on windows and cabinets for my fire rebuild with tariffs raising prices?" | DDP landed-cost example; code certs; references |
| 6 | Builder bid backlog (multiple rebuild RFPs) | Active | Hot (operational) | Habit (spreadsheets) | "Best estimating software to turn architect PDFs into residential rebuild bids fast" | Trial; residential demo; per-seat price |
| 7 | Lot under LOI / offer deadline | Deciding | Hot | Anxiety (underwriting accuracy) | "Who can do a fast construction cost estimate and pro forma for a 2,000 sq ft rebuild plus ADU on an Altadena lot?" | 2–4 day turnaround; per-sq-ft price; sample pro forma |
| 8 | Zone 0 adopted (Aug 19, 2026) / Chapter 7A plan check comments | Active | Cold | Anxiety (surprise costs) | "What do Zone 0 and Chapter 7A add to the cost of rebuilding a house in Altadena?" | Line-item adders from real takeoffs; regulation citations |

---

## N. Prompt matrix

### Takeaway
Twelve full-context prompts, six short prompts and three brand prompts. All prompt text is **[SIMULATED]** and built from sourced persona facts. Demand tiers are **[Estimate]** (no volume data; based on news and result density and on trigger frequency).

### Inferences
**Full-context first-person prompts:**

| ID | Prompt [SIMULATED] | Persona facts | Intent | Stage | Urgency | Mode | Engine | Expected fan-out nodes | Tier (1–5) [Est.] |
|---|---|---|---|---|---|---|---|---|---|
| F1 | "I'm 71 and lost my 1,400 sq ft 1950s house in west Altadena in the Eaton fire. I had the FAIR Plan plus a DIC policy with about $480,000 for the dwelling. A contractor quoted $780,000. Is that reasonable for Altadena in 2026, and how do I check it line by line before signing?" | W. Altadena, 65+, FAIR Plan | validate/trust | deciding | acute | hot | Google AIO, ChatGPT | Altadena rebuild cost per sq ft 2026; contractor bid red flags CSLB; FAIR Plan rebuild gap; line-item bid checklist | 4 |
| F2 | "Our adjuster's Xactimate estimate for our 2,100 sq ft Altadena home is $860K but Coverage A is $630K plus 25% extended replacement. Before we accept, how do we get an independent line-item rebuild estimate the insurer will actually consider?" | E. Altadena, major carrier | choose-provider | active | event | cold | ChatGPT | independent rebuild estimate LA; ClaimArchitect; public adjuster fees California; Xactimate vs contractor bid | 4 |
| F3 | "We lost a 3,800 sq ft house in the Pacific Palisades. The insurer will pay about $2.4M for the dwelling and lots on our street sell for around $1.6M. What would rebuilding cost in 2026, and is rebuilding or selling the lot smarter?" | Palisades HNW | compare/decide | deciding | exploratory | cold | ChatGPT | Palisades rebuild cost per sq ft 2026; Palisades lot prices Redfin; rebuild vs sell | 4 |
| F4 | "Our ALE runs out in January 2027 and our Altadena permit was just issued but construction hasn't started. How do we get an extension and show the delay wasn't our fault?" | Altadena, permitted | do | active | acute | hot | Google AIO | California ALE 24 months extension; Ins Code 2060; CDI | 5 (Quotr: link out) |
| F5 | "I'm a licensed GC and lost my own house in Altadena. I'll run the rebuild myself to stretch the insurance money. What's the fastest way to do a full takeoff from my architect's PDF plans, and how can I buy windows and cabinets cheaper with the new tariffs?" | owner-builder | do / choose-provider | consuming | recurring | cold | ChatGPT | AI takeoff software residential; cabinet tariffs 2026; factory-direct windows California | 2 |
| F6 | "I run a 6-person design-build firm in Pasadena and get 10+ Altadena fire rebuild bid requests a month. What estimating software turns architect PDFs into line-item bids without hiring another estimator?" | builder S6 | choose-provider | active | recurring | hot | ChatGPT, Perplexity | best residential estimating software 2026; AI takeoff; Buildxact/Handoff/Quotr | 3 |
| F7 | "I'm considering a burned 7,500 sq ft lot in Altadena for about $500K to build a 2,000 sq ft house plus an ADU under the new fire codes. Who can give me a fast construction cost estimate and pro forma before I make an offer?" | lot buyer S7 | choose-provider | deciding | acute | hot | ChatGPT | Altadena lot prices; construction cost estimate service per sq ft; Chapter 7A cost | 3 |
| F8 | "We're rebuilding in Malibu after the Palisades fire and need septic and coastal permits. How much more per square foot is a Malibu rebuild than the Palisades, and which line items do coastal and septic rules add?" | Malibu S4 | learn/compare | active | exploratory | cold | Google AIO | Malibu rebuild cost per sq ft 2026; Malibu septic rebuild cost; coastal development permit rebuild | 2 |
| F9 | "LA County says like-for-like rebuilds get expedited plan check. If I rebuild my 1,600 sq ft Altadena house 30% bigger, how much more will it cost and how much longer will permits take?" | Altadena | compare | active | exploratory | cold | Google AIO, ChatGPT | like-for-like definition LA County; Altadena permit times 2026; cost per added sq ft | 3 |
| F10 | "Is a factory-built or modular home actually cheaper and faster than stick-built for an Altadena fire rebuild in 2026? Insurance is $550K for a 1,700 sq ft house." | Altadena | compare | active | exploratory | cold | ChatGPT | prefab rebuild Altadena cost; state pre-built funding; modular vs stick-built cost | 3 |
| F11 | "What do Chapter 7A and the new Zone 0 ember-resistant rules add to the cost of rebuilding a house in Altadena — vents, siding, windows, the first five feet — line by line?" | Altadena | learn | active | event (Zone 0) | cold | Google AIO | Chapter 7A cost; Zone 0 regulations 2026; ember-resistant vents price | 3 |
| F12 | "We lost our home in the Hurricane Helene flooding near Asheville. Insurance and FEMA won't cover the rebuild. How do I get a realistic cost estimate for a 1,500 sq ft house in Buncombe County in 2026?" | WNC (unresearched) | learn / choose-provider | active | exploratory | cold | Google AIO | Helene rebuild cost per sq ft; FEMA substantial damage; Buncombe permits | 2 [Speculative] |

**Short prompts:**

| ID | Prompt | Intent | Stage | Tier [Est.] |
|---|---|---|---|---|
| S1 | cost to rebuild house Altadena per square foot 2026 | learn | passive/active | 4 |
| S2 | independent rebuild cost estimate Los Angeles fire insurance | choose-provider | active | 3 |
| S3 | is my fire rebuild contractor bid too high | validate | deciding | 3 |
| S4 | rebuild or sell burned lot Palisades | compare | deciding | 3 |
| S5 | best estimating software for fire rebuild contractors | choose-provider | active | 2 |
| S6 | factory direct cabinets windows LA fire rebuild tariffs | choose-provider | consuming | 2 |

**Brand prompts** (track separately, per the framework):

| ID | Prompt | Purpose |
|---|---|---|
| B1 | "Quotr FireTips LA fire rebuild cost app — is it still available?" | Entity freshness; legacy-domain risk |
| B2 | "Quotr.ai vs ClaimArchitect for an LA fire rebuild estimate" | Comparison framing; tests whether the engine knows the difference (estimate vs claim valuation) |
| B3 | "Is Quotr.ai legit for LA fire rebuild cost estimates?" | Trust; checks for the known Quotr Pro app conflation in the fact sheet |

---

## O. Simulation

### Takeaway
(1) A simulated ChatGPT journey shows an Altadena homeowner moving from "is my coverage enough" to "who gives me an independent line-item estimate", with ClaimArchitect, public adjusters and contractors as the default picks. (2) Twelve real searches run during this research, recorded as a **retrieval proxy, not an AI engine answer**, show contractor-marketing guides, local news, nonprofits and law firms owning the sub-queries. Quotr appears only as a 2025 press-release repost on the brand query. (3) The cost and estimate clusters are open; the deadline and claims clusters are not Quotr's to win.

### Cited Findings
**(2) Retrieval proxy** (WebSearch results from this session, Nov 6 2026; queries were run as research queries that double as likely fan-out sub-queries; **not an AI engine answer**):

| # | Sub-query (as run) | Top domains returned | Brands / orgs named | Quotr? | Winning format |
|---|---|---|---|---|---|
| R1 | LA fire rebuild cost per square foot 2026 Altadena Palisades contractor bids | altadenacustomhomebuilder.com, amerbuild.com, dwdbuilders.com, zmalegacybuilders.com (×2), altobuilds.com, bwengr.com, lytemods.com, ubic.co | Contractor brands; "TESH Group" | **No** | Contractor "2026 guide" pages with per-sq-ft tiers by area, year in title |
| R2 | LA fire rebuild permits issued completed homes 2026 Altadena Palisades | calmatters.org, gov.ca.gov, nationalreview.com, altobuilds.com, pfar.org, dwdbuilders.com, therenology.com, palisadesfirerebuilding.com, mckinsey.com | CalMatters, Governor, McKinsey | No | News + independent trackers + contractor guides |
| R3 | United Policyholders survey Eaton Palisades underinsured 2026 | uphelp.org (×6), insurancebusinessmag.com, efsurvivors.net, thebusinessjournal.com | UP, EFSN | No | Nonprofit survey PDF + news |
| R4 | Altadena Palisades burned lots sold percentage 2026 investors | laist.com, businesswire.com (Redfin), yahoo.com (LA Times), smdp.com, pfar.org, aol.com, barchart.com, nbcnews.com | Redfin; Altadena Not for Sale | No | **Original data release** (Redfin) syndicated widely |
| R5 | California ALE 24 months … January 2027 extension | propertyinsurancecoveragelaw.com, insurance.ca.gov (×2), coverageclassroom.com (×2), haffnerlawyers.com, naumannlegal.com, fireandsmokeattorneys.com, financialsupportresources.com | CDI; law firms | No | Law-firm explainers + regulator |
| R6 | California public adjuster fee cap … LA fires | billtrack50.com, propertyinsurancecoveragelaw.com, newswire.com, legiplex, insurance.ca.gov, propertycasualty360.com | CDI; AB 597 | No | Bill trackers + law blogs |
| R7 | SBA disaster loan deadline Los Angeles wildfires | sba.gov (×3), uphelp.org, insurancebusinessmag.com, smallbiztrends.com, palipost.com, palisadesnews.com, spectrumlocalnews.com | SBA, UP | No | Official releases |
| R8 | fire survivor decision fatigue rebuild … contractors scams trust | smdp.com, spectrumlocalnews.com, abc7.com, moneywise.com, mynewsla.com, smmirror.com, altadenabuilderdirectory.com, dwdbuilders.com, foxnews.com | LA County, CSLB | No | Local news on fraud |
| R9 | LAist fire survivors rebuild cost underinsured "per square foot" | uphelp.org, laist.com, labusinessjournal.com, philadelphiafed.org, vaismanconstruction.com, tect.com, fbia.com, altadenacustomhomebuilder.com | UP, ClaimArchitect, AAA | No | News with survey numbers + vendor blogs |
| R10 | ClaimArchitect Palisades insurance payout gap rebuild estimate tool | **claimarchitect.com (×5)**, labusinessjournal.com, spectrumlocalnews.com, aol.com | ClaimArchitect, Verisk (Xactimate/360Value) | No | **Neighbourhood landing pages + earned local business press** |
| R11 | Malibu Pasadena fire rebuild permits dashboard 2026 | smdp.com, calmatters.org, malibucity.org, goldenlineconstruction.com, dwdbuilders.com, lytemods.com, jwenterprises.com, ca.gov, cbsnews.com | City of Malibu | No | News + city + contractor guides |
| R12 (brand) | Quotr FireTips LA fire rebuild app homeowners | rcnamericaca.blogspot.com (Quotr release repost), palisadesnews.com, westsidecurrent.com, la2050.org, laist.com (sponsored), gov.ca.gov, homebound.com, miyamotointernational.com | **Quotr (FireTips, via repost only)**; PaliBuilds/ClaimArchitect; LA Builders Alliance tool; LA Rises/Archistar | **Yes, weakly** (repost of the Feb 2025 release; firetips.quotr.io not returned) | Press-release repost; competitor tool news |

- An earlier run of the literal prompt "how much does it cost to rebuild a house after the LA fires per square foot 2026" (Sept 2026) cited Bloomberg plus local GCs (Benson Construction, Amerbuild, UBIC, Vaisman), with **no Quotr** ([verification note](<../Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>)).

### Inferences
**(1) SIMULATED 5-turn ChatGPT conversation** (Altadena homeowner; persona built from sourced facts; assistant wording is the researcher's projection of typical behaviour, **not a captured answer**):

> **[SIMULATED] Turn 1 — User:** "My house in Altadena burned in the Eaton fire. Insurance says my dwelling coverage is $607,000. Is that enough to rebuild?"
> **[SIMULATED] Assistant:** Says it depends on size and finishes; cites 2026 contractor ranges ($450–$750/sq ft); notes that UP and other surveys show most total-loss owners were underinsured; suggests checking extended replacement cost and code-upgrade coverage; recommends getting multiple bids. *(Expected fan-out: "Altadena rebuild cost per square foot 2026", "United Policyholders underinsured Eaton".)*
>
> **[SIMULATED] Turn 2 — User:** "It's 1,500 sq ft. The adjuster's estimate is $760K and a contractor quoted $910K. Who's right?"
> **[SIMULATED] Assistant:** Explains Xactimate versus contractor pricing; lists the usual gaps (soft costs, Chapter 7A, code upgrades, current labour); suggests an independent line-item estimate, a public adjuster, or an attorney; mentions ClaimArchitect as an example of a service that builds rebuild valuations. *(Fan-out: "independent rebuild estimate Los Angeles", "Xactimate vs contractor bid", "public adjuster California fees".)*
>
> **[SIMULATED] Turn 3 — User:** "I don't want to give a public adjuster 10–15%. Is there something cheaper that just tells me what it should cost?"
> **[SIMULATED] Assistant:** Lists options: an independent estimator or cost consultant, ClaimArchitect, a builder-referral tool, nonprofit help (UP, Department of Angels). Quotr is not named, because no Quotr page matches "independent rebuild estimate Altadena".
>
> **[SIMULATED] Turn 4 — User:** "How do I know a contractor isn't scamming me?"
> **[SIMULATED] Assistant:** CSLB lookup; avoid large deposits and blank contracts; cites the County's fraud campaign and local news on unlicensed-contractor stings.
>
> **[SIMULATED] Turn 5 — User:** "OK — what should a line-item rebuild estimate for a 1,500 sq ft house in Altadena include, and what's a fair total?"
> **[SIMULATED] Assistant:** Gives a generic CSI-style trade breakdown from contractor blogs, with per-sq-ft bands and no dated local source. **This is the slot a dated Quotr line-item example plus tracker could own.** The homeowner picks a path: two more bids plus an independent estimate.

**(3) Gap verdict per prompt cluster** [Likely]:

| Cluster | Who owns retrieval | Quotr verdict |
|---|---|---|
| Cost per sq ft by area | Contractor marketing guides; no independent dataset | **OPEN — top priority.** A dated, sourced, line-item tracker can out-evidence contractor pages (framework: evidence density decides share once retrieved). |
| Independent estimate / insurance gap | ClaimArchitect (5 owned pages + LABJ + Spectrum), UP, LAist | **Contested.** Win the "what a line-item estimate includes" and "how to compare an insurer estimate with bids" angle; never the claim-dispute angle. |
| Bid check / contractor trust | Local news, County, CSLB | **Partly open.** A bid-checklist page with a CSLB link; trust earned via partners. |
| Rebuild vs sell / lot buyers | Redfin data, news | **Open** for a calculator that pairs Redfin lot values with rebuild cost. |
| Deadlines (ALE, SBA, forbearance, public adjuster rules) | CDI, SBA, law firms | **Ignore** (link out; compliance risk). |
| Permit status / timelines | News, trackers, contractor guides | **Skip** as a standalone; cite on the hub. |
| Builders' estimating software (rebuild) | Not tested this session | Likely Buildxact/Handoff/Houzz Pro etc. (per the personas file C2/C13); needs testing. |
| Materials / tariffs for rebuilds | CNN mention only | **Open** (Procurement angle). |
| Brand | Blogspot repost; competitor tools crowd the query | **Weak entity.** Move FireTips onto quotr.ai. |

### Gaps
- No live ChatGPT, Gemini or AI Overviews runs were possible. The retrieval proxy reflects one search backend on one day.
- No builder-software or materials sub-queries were run before the budget ran out.

---

## P. GEO system for Quotr for this ICP

### Takeaway
Build **one LA rebuild cost hub with a dated, sourced cost tracker**, three area spokes, an insurance-gap ("sq ft your coverage buys") calculator, a rebuild-vs-sell worksheet, and builder/materials pages, in urgent and considered versions. Earn placement through local data journalism and nonprofit partnerships, not self-promotion. Stay strictly on the "estimate, not adjusting" side of the line. **Verdict: worth a bounded bet now.** More than 90% of homes are unbuilt, the January 2027 landmarks are coming, and no independent cost dataset exists. But the homeowner claim-help lane is crowded and compliance-sensitive. Lead with the data asset and the builder, lot-buyer and materials lanes.

### Cited Findings
- AI engines retrieve contractor "2026 guide" pages for cost queries, and the vendor ClaimArchitect owns its own named-query results with neighbourhood pages and earned local press (O, R1, R10).
- Original data gets syndicated: the Redfin lot-sale release was picked up by LAist, the LA Times, SMDP, Barchart and NBC (R4).
- Compliance anchors:
  - PC 396 (>10% price increases on covered goods and services during an emergency; up to $10,000 fines and/or 1 year in jail) ([egattorneys](https://www.egattorneys.com/price-gouging-penal-code-396); [Santa Monica](https://santamonica.gov/blog/california-s-anti-price-gouging-law-prohibits-contractors-from-over-charging-customers-for-repair-and-emergency-clean-up-services-during-declared-emergency)).
  - The CDI public-adjuster solicitation notice ([CDI](https://www.insurance.ca.gov/0250-insurers/0300-insurers/0200-bulletins/bulletin-notices-commiss-opinion/upload/Notice-Solicitation-by-Public-Adjusters-in-the-Southern-California-Wildfire-Areas.pdf)).
  - The ClaimArchitect disclaimer model ([claimarchitect.com](https://claimarchitect.com/press/palisades-fires-gap)).
  - County anti-fraud rules ([SMDP](https://www.smdp.com/la-county-moves-to-shield-fire-survivors-from-contractor-scams/)).
- Framework rules applied: one page per intent cluster; local pages only where price or regulation differ; per-sq-ft facts as quotable sentences; monthly refresh for pricing and data pages (citation half-life about 4.5 weeks); no self-ranked listicles; schema and llms.txt are not levers.

### Inferences
**1. Owned pages** (titles and slugs proposed; all [Likely]):

| Page | Slug | Mode | Content spine | Product |
|---|---|---|---|---|
| **LA Fire Rebuild Cost 2026: dated, sourced cost per sq ft by neighborhood** (hub) | `/rebuild/los-angeles/` | Considered | Tracker table (Altadena / Palisades / Malibu; like-for-like vs upgrade; finish tiers); every number dated and sourced; methodology; "updated monthly" | Service, FireTips successor |
| Altadena & Pasadena rebuild cost (Eaton fire), 2026 | `/rebuild/los-angeles/altadena/` | Considered | County permit regime; like-for-like; Chapter 7A; west/east sections; gap-financing pointers (ALI, the BET/NAACP fund) | Service |
| Pacific Palisades rebuild cost 2026 | `/rebuild/los-angeles/pacific-palisades/` | Considered | City of LA rules and fee waiver; larger homes; rebuild vs lot value | Service, Procurement |
| Malibu rebuild cost 2026: septic, coastal and slope adders | `/rebuild/los-angeles/malibu/` | Considered | Coastal and septic line items; permit pace | Service |
| **How many square feet does your coverage rebuild? (calculator)** | `/rebuild/coverage-to-square-feet-calculator/` | Urgent + considered | Inputs: Coverage A, ERC %, code-upgrade %, area, finish tier → buildable sq ft and gap. **Outputs are a cost comparison, not a claim value.** | Service lead-in |
| What a line-item rebuild estimate includes (and what insurer estimates often leave out) | `/rebuild/line-item-rebuild-estimate/` | Considered | Real anonymized Quotr "Residential LA Fire Rebuilding" sample; trade-by-trade split; soft costs | Service |
| **Got a rebuild bid over your insurance? 7 things to check this week** | `/rebuild/check-a-rebuild-bid/` | **Urgent** | CSLB link first; deposit and contract red flags (cite County/CSLB); line-item asks; one authority marker | Service |
| Rebuild or sell your burned lot: 2026 numbers (worksheet) | `/rebuild/rebuild-vs-sell-lot/` | Considered | Redfin lot values + rebuild cost bands + timeline; neutral, community-respectful | Service |
| What Chapter 7A and Zone 0 add to rebuild cost (line items) | `/rebuild/chapter-7a-zone-0-cost/` | Considered | Vents, siding, glazing, 5-ft zone, from takeoffs; regulation dates | Software, Procurement |
| Factory-built vs stick-built rebuild cost in LA (2026) | `/rebuild/prefab-vs-stick-built-cost/` | Considered | Like-for-like comparison; state program pointer | Service |
| Windows, doors and cabinets for fire rebuilds: tariff-era costs and code certifications | `/rebuild/finish-materials-cost/` | Considered | DDP landed-cost examples; NFRC/CARB/cUPC; lead times | Procurement |
| Estimating LA fire rebuilds for builders: PDF plans to line-item bid | `/rebuild/for-builders/` | Considered | Workflow, residential demo, per-seat pricing | Software |
| Construction cost estimate and pro forma for a burned-lot purchase | `/rebuild/lot-buyer-estimate/` | Urgent | 2–3 day turnaround; per-sq-ft price; sample pro forma; **"we also serve owners rebuilding their own homes"** | Service |
| ALE ends Jan 2027? Documents to have ready (links to CDI/UP) | `/rebuild/ale-deadline-documents/` | Urgent | **No advice**; a checklist of cost documents; links to CDI, UP and the statute summary | Brand trust only |

**2. Proof assets and original data** (priority order):
- (a) **Quotr LA Rebuild Cost Tracker**, quarterly with monthly refresh:
  - median and IQR per sq ft by area and finish tier from anonymized Quotr Service estimates (**needs customer permission and n-size disclosure**);
  - trade split; materials index (cabinets, windows, lumber);
  - a methodology page; dated, with a CSV download.
- (b) **"Coverage vs cost" brief:** sq ft that the average 2023 Altadena policy ($607K, Catalyst) buys at today's bands.
- (c) **Anonymized line-item sample** (the existing LA rebuild deliverable).
- (d) **FireTips migration:** 301 to `/rebuild/los-angeles/` or relaunch with a date stamp. The legacy domain is a stale-entity risk (fact sheet).
- (e) **Named estimator bio** with credentials (**TO CONFIRM**).

**3. Off-site placements**, ranked by leverage per hour [Estimate]:
1. **Data pitch** to LA Business Journal, LAist, Pasadena Now, Palisadian-Post and SMDP with tracker findings around the **Jan 7, 2027 anniversary**. Precedent: LABJ and Spectrum covered ClaimArchitect's data; Redfin's data syndicated widely.
2. **Nonprofit data partnership.** Offer free tracker data or estimate clinics to the Department of Angels, EFSN, Altadena Land Initiatives and UP (resource-list inclusion; disclosed, no lead harvesting).
3. **In-person clinics** at recovery centers (the PaliBuilds model). Altadena is not yet served by PaliBuilds-style office hours (per sources found).
4. **One chaptered YouTube walkthrough:** "reading a 1,500 sq ft Altadena rebuild estimate line by line".
5. **Builder channels:** BIA LA/Ventura, LA Builders Alliance (verify), local supplier counters (Software/Procurement).
6. **Disclosed founder participation** in r/Altadena / r/LosAngeles: a 3–6-month play, 9:1 rule, never soliciting victims.
7. **Entity hygiene:** the FireTips → quotr.ai redirect; consistent "Quotr.ai" naming.

**4. Refresh cadence:**
- Tracker and hub: **monthly** (December–February weekly checks around Jan 7).
- Area spokes: monthly (permit counts) and quarterly (narrative).
- Calculator inputs: quarterly.
- Regulation pages: on each change (Zone 0 OAL, SB 876, Jan 1, 2027 laws).

**5. Tracking prompts to freeze** (≥4 weeks; ChatGPT + Google AIO; 3–5 runs; cluster-level reporting):
- T1 "how much does it cost to rebuild a house in Altadena per square foot 2026" (S1)
- T2 "how much does it cost to rebuild after the LA fires per square foot 2026" (the existing S12 baseline)
- T3 F2 (independent line-item estimate before accepting a settlement)
- T4 F1 (bid check, 65+ FAIR Plan persona)
- T5 F3 (Palisades rebuild vs sell)
- T6 F6 (builder estimating software for rebuild bids)
- T7 S6 (factory-direct finishes for rebuild, tariffs)
- T8 B2 (Quotr.ai vs ClaimArchitect)

**6. Compliance guardrails** [Likely; legal references to be confirmed by counsel]:
- **Public adjusting:**
  - Quotr must not negotiate, "maximize", "recover" or "fight" claims, or be paid on a percentage of a claim.
  - Mirror the ClaimArchitect-style disclaimer: "Quotr.ai provides construction cost estimates. It is not a public adjuster, law firm or insurer and does not negotiate or settle insurance claims."
  - Respect CDI limits on post-disaster solicitation (the CDI notice).
  - **No cold outreach to survivors.**
- **CSLB / contractor licensing:**
  - Quotr must not imply it builds, bids or supervises work, and must not refer contractors for fees without disclosure.
  - Every bid page links to the CSLB license lookup.
  - Whether any Quotr staff hold licenses: **TO CONFIRM**. Do not claim "licensed estimators" otherwise.
- **PC 396 price gouging:**
  - Quotr Procurement and Service pricing in LA County must not rise more than 10% while any declared emergency order covering those goods and services is active.
  - The construction-materials extension ran to Jan 7, 2026, and no later extension was found; verify the current status before any LA price change.
- **FTC endorsements and claims:**
  - Survivor testimonials must be real, typical or clearly qualified, with any compensation or discount disclosed.
  - Procurement's "40–55% savings" needs substantiation per project (fact sheet).
  - No fake reviews.
- **Respect and ethics:**
  - No fear or trauma copy; no "investor"-forward messaging in Altadena (community norm: Altadena Not for Sale).
  - The lot-buyer page must stay neutral and must not appear on area pages aimed at survivors.
  - Privacy: no tracking pixels on calculator inputs that reveal insurer or financial details.

**7. Do / skip / ignore:**
- **Do:**
  - the cost tracker and hub, plus 3 spokes;
  - the calculator; the urgent bid-check page;
  - FireTips migration; the anniversary data pitch; nonprofit partnerships;
  - builder and materials pages;
  - tracking T1–T8;
  - switch interviews (6–12 recent rebuilders/builders), with the "what did you type, and where" question.
- **Skip:**
  - claim-dispute content; public adjuster comparisons ("PA vs Quotr");
  - deadline advice pages beyond link-out checklists;
  - permit-status trackers (others do this);
  - templated pages for every LA neighbourhood or Lahaina/WNC/FL until researched;
  - self-ranked "best rebuild estimators" lists.
- **Ignore:**
  - Claude/Copilot/Grok tracking for this ICP;
  - generic social proof ("thousands trust us");
  - schema or llms.txt as levers.

**8. Verdict** [Likely]:
- **Yes, a bounded bet: about 40–60 hours over Dec 2026 to Mar 2027** [Estimate].
- **The window is not closing yet.** About 3.6% of Altadena and 1.2% of Palisades homes were complete by Sep–Oct 2026; about 61% of Palisades owners had not filed. The historical base rate (38% rebuilt after 8 years in earlier California fires) means decisions continue into 2028+.
- Window landmarks: the 24-month ALE mark (Jan 7, 2027), SBA drawdowns (2027–2028) and the 36-month mark (Jan 2028).
- **Why bounded:**
  - Homeowner claim-help is crowded (ClaimArchitect, public adjusters, attorneys) and legally sensitive.
  - Quotr lacks local references and trust credentials.
  - Homeowners pay small tickets ($375–$950).
- **Highest expected value:**
  - (1) the **independent cost tracker**, which wins AI citations and press because no dataset exists;
  - (2) **builders** (Software, recurring revenue);
  - (3) **materials during tariff-era finish buying** (Procurement, high ticket);
  - (4) homeowner Service as a low-price trust product.
- Re-assess after the January 2027 anniversary cycle, using T1–T8 baselines and inbound counts.

### Gaps
- The legal review of each guardrail (CSLB scope, public adjuster statute wording, current PC 396 orders) is not done.
- Quotr's willingness to publish anonymized estimate data is unknown.
- FireTips' current state is unknown.

---

## Q. Known / likely / speculative

| Claim class | Known (sourced) | Likely (inference, labelled) | Speculative (validate first) |
|---|---|---|---|
| Size | ~16,250 structures / ~11,430 homes destroyed (DINS as reported); Altadena 3,671 permits / 2,310 under construction / 215 complete (Sep 26 2026, county data via a contractor guide); Palisades 1,557 of 3,984 filed, 48 complete (Oct 2026); Malibu 101 permits, 1 CofO | >90% of destroyed homes unbuilt in Nov 2026; ~9,000 households with cost decisions ahead | Exact numbers of sellers vs rebuilders in 2026 |
| Insurance gap | AAA cohort: $628K coverage vs $928K bids; DoA average $500K short; UP: 36% (Eaton) / 46% (Palisades) average shortfall; Klein 71.3% underinsured | Underinsurance is the majority case | UP's "7% had enough" vs "69% short" reconciliation |
| Cost per sq ft | Contractor ranges $350–850 (Altadena), $550–1,200 (Palisades); "no government or academic dataset" | An independent tracker would be cited | Quotr's own median per sq ft (needs data) |
| Geography | West Altadena: 81% Black homeownership, 61% of Black households in the perimeter, >half of Black homeowners 65+; lot prices $510K / $1.6M; investor share ~40% | Four spokes justified | East/west Altadena cost differences |
| Psychology | Fraud cases and stings; "more determined than ever"; insurer anchoring via 360Value/Xactimate; like-for-like expedited | Bid shock and anniversary are hot moments; anchoring/defaults/time pressure apply | Decision-fatigue effects; engine choice by age |
| Triggers | ALE ≥24 months + 12 (Ins. Code §2060); SBA 24 months from authorization; Zone 0 adopted Aug 19 2026; AB 1847 signed Sep 15 2026; PC 396 construction order to Jan 7 2026 | Dec 2026–Feb 2027 demand peak | §2051.5 36-month deadline; SB 876 status; Jan 1 2027 laws |
| Competition | ClaimArchitect / PaliBuilds / Bidsy; LA Builders Alliance tool; state/LA Rises portal; contractor guides own cost queries | Quotr can own "independent cost transparency" plus builder/materials | Engines will name Quotr after a tracker launch |
| Quotr | Service $0.25/sq ft; Software $79.90 / $299.90; FireTips launched Feb 2025 (paid release); LA rebuild sample exists; absent from LA rebuild answers (Sep 2026 test) | FireTips on the legacy domain hurts entity clarity | FireTips still live and working; estimator credentials |
| Secondary markets | — (not researched) | — | Lahaina, WNC, FL demand; 2025–2026 disasters |

### Gaps (overall)
- **Search budget exhausted** after about 31 searches; WebFetch blocked; Reddit unreachable.
- Missing as a result:
  - first-person community verbatims;
  - Facebook group counts;
  - official October–November 2026 dashboard figures;
  - Pasadena permits;
  - ACS demographics;
  - all secondary-market research (Lahaina, Helene in WNC and Florida, Milton, 2025–2026 disasters);
  - SB 549 / SB 495 / §2051.5 verification;
  - a builder-software fan-out test;
  - FireTips' live status.
- A follow-up session with fetch access to uphelp.org, calmatters.org, recovery.lacounty.gov, ladbs.org, malibucity.org, cityofpasadena.net and reddit.com would close most of these.
