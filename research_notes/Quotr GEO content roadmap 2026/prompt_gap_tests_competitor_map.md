# New buyer-prompt gap tests (Open / Contested / Saturated), competitor content map and Quotr post mapping for the Quotr.ai GEO content roadmap (US, as of 2026-09-25)

**How this was run (read first)**
- **Engine:** Perplexity through `mcp__Slashy__web_search`. Every response returned `"model": "sonar"`, so this is Perplexity's Sonar API model. ChatGPT, Google AI Overviews/AI Mode, Gemini, Claude and Copilot could not be queried from this environment.
- **Prompts:** 59 new prompts, written the way buyers phrase them and each run once on 2026-09-25. None repeats the earlier tests (C1–C15, V1–V10, P1–P8, B1–B7 in `quotr_ai_visibility_tests.md`, or the prompts in `competitor_geo_benchmark.md`). One is deliberate: AI2 ("AI takeoff accuracy 2026") is a year-stamped variant of earlier P5 ("how accurate is AI takeoff"), included to check whether freshness changes the citation set.
- **Refusals and rate limits:** no Slashy call was refused or rate-limited.
- **WebSearch (25 calls):**
  - 9 cross-checks of individual prompts (PR1, PR2, PR11, CO2, CO3, CO8, TR1, AI1, BD1)
  - 6 `site:quotr.ai` checks, each restricted to the quotr.ai domain
  - 10 competitor inventory and identity queries, each restricted to competitor domains
- **WebFetch:** I tried to read competitor sitemaps. Every attempt was **refused with `EGRESS_BLOCKED`** (www.meltplan.com, exayard.com, easytakeoffs.com). I did not retry with other tools. quotr.ai and quotr.io were not fetched, per instructions. As a result, the competitor volume figures below are only **counts of pages seen in search results**. They are lower bounds, not sitemap totals.
- **Labels:**
  - Observed = seen in a tool result.
  - Inference = my own judgment.
  - Named = the brand appears in the answer text.
  - Cited = the URL is used as an inline citation.
  - Retrieved only = the URL is in the citation array, but the answer never uses it.
- **Classification criteria (Inference, applied to Observed answers and citations):**
  - **Open:** the answer is thin, generic, contradictory or built from off-target pages (homepages, consumer or non-US documents), and no strong vendor or authority page owns the exact question.
  - **Contested:** several decent on-topic pages, none dominant. This is usually a mix of vendor, service-firm and niche sites.
  - **Saturated:** authority pages dominate (government, NAHB, AIA, JLL, ENR, Procore Library, big software brands), or 8+ on-topic vendor pages, calculators or templates compete.
- **Freshness** is approximated from dates in URLs and titles and from publication dates visible in the results (Inference).

---

## 1. Which new buyer prompts are Open, Contested or Saturated, and who is named and cited?

### Takeaway
Of 59 new prompts, **8 are Open, 24 Contested and 27 Saturated**.
- **Open topics:** 6 of the 8 are procurement and finish-material cost questions (landed cost of Chinese cabinets, tile, imported windows under Title 24, developer bulk buying, factory-direct savings, cabinet budget per unit). The other 2 are developer feasibility-estimate questions. Those are exactly Quotr's Procurement line and its developer Estimation Service. **Quotr has no page for any of the 8, and none cited Quotr.**
- **Where Quotr appears:** it was cited in **6 of 59 (10.2%)** and present in the citation array in **7 of 59 (11.9%)**. Every one of those was a Contested topic where Quotr already has a page full of numbers. Quotr was **named in 0 of 59**.
- **Saturated clusters:**
  - Bidding: 6 of 6, owned by the Procore Library, field-service software blogs and Meltplan.
  - Trade how-tos: 7 of 11, owned by calculators and vendor trade pages.

### Cited Findings

#### 1a. Results table (Perplexity Sonar, 2026-09-25, one run per prompt)
Columns "Brands named" and "Top cited domains" are Observed. "Class." is an Inference based on the criteria above. Page types are in parentheses. Bold = quotr.ai.

| ID | Prompt (verbatim) | Cluster | Class. | Brands named in answer text | Top cited domains (page types) | Quotr present? | Notes (freshness; key facts in the answer) |
|---|---|---|---|---|---|---|---|
| PR1 | landed cost of kitchen cabinets from China 2026 | Procurement | Open | none | buildtana (contractor import-duty guide); artcheerkitchen, bfpcabinetry, allurekitchencabinet, hsysourcing, parlunbuilding (China factory/sourcing-agent blogs); tcwholesalecabinetry (US wholesaler blog); tonlexing, unicargo, icontainers (logistics, landed-cost calculator); calcmytariff; thestreet (news) | No | Mostly 2026-dated. "1.4–1.7x FOB"; $8,000 FOB → ~$12,550 landed. The answer calls the cabinet duty "25% Section 301" and uses "assumed AD/CVD". The WebSearch summary instead describes a stacked Sec. 232 + Sec. 301 + AD/CVD burden (see 1c). |
| PR2 | DDP vs FOB for building materials | Procurement | Contested | none | baierfloor (flooring factory); **quotr.ai (#2 citation)**; trade.gov (gov); globalsources, cosmosourcing, riwick, importivity (sourcing/QC firms); investopedia, edc.ca, tradefinanceglobal (reference) | **Cited 4x inline, not named** (/blog/ddp-construction-materials/) | Evergreen. The answer says DDP can run 15–25% above FOB (riwick, cosmosourcing). In WebSearch, Quotr is not in the top 9. |
| PR3 | are quartz countertops from China subject to tariffs | Procurement | Saturated | none | rulings.cbp.gov, thefederalregister, usitc, trade.gov ADCVD (gov); strtrade x3 (trade-law firm); NPR, Chicago Tribune, Axios, Bloomberg, KQED (news); felixdeco, wove (tariff lookups) | No | Current to Sep 2026. Base duty free (HTS 6810.99.0010) + 25% Ch. 99 on China + AD/CVD orders + a new tariff-rate quota from Aug 15, 2026 (25% in-quota / 50% over-quota). |
| PR4 | how to check if imported cabinets are CARB compliant | Procurement | Contested | none | ww2.arb.ca.gov x7 (gov PDFs/FAQs); columbiaforestproducts, marshcabinets (manufacturer PDFs); nfpaglobalsolutions (certifier); tcwholesalecabinetry, fbmsourcing (importer/agent guides); goodairhomes | No | Gov docs dated 2014–2024. Checklist: CARB Phase 2 + TSCA Title VI statement, TPC/mill documents, labels, invoice/BOL statement, CBP ACE import certification. |
| PR5 | how long does it take to ship building materials from China to California | Procurement | Saturated | none | freightos x2, icontainers, unicargo, gofreight, ship4wd, tonlexing x2, sino-shipping, DHL, freightright, gerudologistics (logistics firms, transit calculators); alibaba | No | Evergreen. 14–25 days port-to-port to LA/Long Beach; 20–35 days door-to-door; air 3–7 days. Production lead time not quantified. |
| PR6 | tariff on kitchen cabinets and vanities 2026 | Procurement | Saturated | none | whitehouse.gov (gov); troutman, wiley, bakerdonelson (law); strtrade, chrobinson, ghy, nnrglobal (customs/trade); nahb.org; ABC, CBS, CNBC (news); nextdaycabinets, tcwholesalecabinetry (sellers) | No | Dec 2025–Sep 2026. 25% Section 232 through 2026; the increase to 50% is delayed to Jan 1, 2027. |
| PR7 | is it cheaper to import porcelain tile from China than buy in the US | Procurement | Open | none | contigoceramics x3, tilesandbathroom x2, hansetile, skytouchceramic (China tile factories); architessa, crossville (US sellers warning about tariffs); tonlexing, gerudologistics (logistics); alibaba, accio, ustradestack.ai, easygoglobal | No | Mixed dates. Contradictory: "30–60% below US distributor pricing" vs "more than twice as expensive" after duties. No AD/CVD rate is stated. |
| PR8 | how to vet a Chinese building materials factory before placing an order | Procurement | Contested | none (SGS/TÜV mentioned as audit firms) | olachina, hsysourcing, firstlinkpartners, oppeinhome, georgestones, qcadvisor x2, meritustech, importivity, js-sourcing, czoverseas, proqc (sourcing agents, QC firms); dracon (NZ); einpresswire PRs | No | Mostly undated. Generic supplier vetting. US building-code documentation (ASTM/UL/CARB/NFRC) is covered only thinly. |
| PR9 | can I use windows imported from China on a California project Title 24 NFRC | Procurement | Open | none | energy.ca.gov x9, dgs.ca.gov x3, napacounty (gov/code); gocodebook x2 (code reference); view.com, glass.org, usglassmag, coolroofs, lightsocal | No | Code docs 2015–2025. No cited page is about imported windows. The engine infers that "country of origin is not the issue; NFRC rating/label required". |
| PR10 | how do multifamily developers buy cabinets flooring and fixtures in bulk direct from manufacturers | Procurement | Open | none in text | ~20 supplier homepages: cpbuild, summitedgecabinet, cabocabinetgroup, r3cabinets, atlasbuildsupply, grandior (MF cabinet suppliers); apogeeinteriors, carpenterstone, kbbuildingsolutions (turnkey interior packages); glidelock, perfectbuildingsupply, crownharvesthardware, spragginsinc, scsmultifamily, maplehaususa | No | Undated homepages. No neutral guide and no data. This is Quotr's exact proposition, but Quotr is absent. |
| PR11 | how much can home builders save buying finish materials direct from factories in China | Procurement | Open | none | hsysourcing x6 (one China sourcing agent); newser; firstlinkpartners x2; okbuildpro; chinadirectsourcing.com.au; georgebuildings; kdwalmsley substack; LinkedIn x3; alibaba | No | Undated. Claims 25–50% savings, 30–45% net; imports pay off above a $40–100k finish budget. The WebSearch top 9 is a Substack newsletter, YouTube and sourcing agents; no Quotr. |
| PR12 | long lead time construction materials 2026 | Procurement | Saturated | none | dpr.com (Q3 2026 report), skanska x3, linbeck, terrapincg, bdcnetwork, linesight, beroe (GC/consultant market reports); buildmatinsight, freightcenter, banamind.ai, teamgantt, cmicglobal, procore | No | Current. Transformers 52–74 weeks, switchgear 40–70, generators ~40, steel 14–24+. Lead times for residential finishes are absent. |
| CO1 | cost per square foot to build an ADU in California 2026 | Cost | Saturated | none | abodu, samara, ameradu, andalusiadrafting, adupilot (calculator), ladu, ycd.studio, hamilton-exteriors, cali-adu, imkatconstruction, tinyhomecottages (ADU builders' cost guides); sweeten, blockrenovation; LA Times, patch, TheRealDeal | No | 2026-dated. $200–$450/sf; detached $300–$500+. |
| CO2 | multifamily construction cost per unit 2026 | Cost | Contested | none | buildmatinsight x4, irecruit, propertybuild, terrapincg, willowdaleequity, multifamily.loans, designtransitionstudio, apers.app, analytics.loan (aggregators/lenders); bidflow.visidex, meltplan (estimating vendors); NREL, ULI, taxcreditadvisor, CoStar | No | 2026-dated. $150k–$450k/unit; garden $150–250k; podium $240–380k; high-rise $420–700k+. WebSearch adds exayard (vendor). No Quotr. |
| CO3 | LA fire rebuild cost per square foot | Cost | Contested | none | bensonconstructiongroup x3, aplaconstruction, vaismanconstruction, avicaconstruction, dwdbuilders, laconstructioncompliance, constructelements (LA contractors); recovery.lacounty.gov (gov FAQ); Bloomberg, TheRealDeal, LA Times (news); reddit | No | 2025–Sep 2026. $350–$750+/sf, commonly $450–$600; hillside $1,000–$1,800+. The WebSearch top 9 is local contractors and engineers; no Quotr. |
| CO4 | cost to build a fourplex in California | Cost | Contested | none | sb1211.us, homeadvisor x2, angi, fixr, costtoconstruct, latestcost x2, propertybuild (cost guides); oneestimate.ai (AI estimating vendor, CA calculator); rand.org; biggerpockets, reddit | No | Mixed dates. $750k–$1.3M in CA; $300–$450/sf stick-built; ~$29k/unit CA impact fees (RAND). |
| CO5 | cost to build a house in the Bay Area per square foot 2026 | Cost | Contested | none | customhome.us x2, barccibuilders, azizconstruction, alhomesbuilder, homeblue (Bay Area builders); costtobuildhouse, homeadvisor, angi, opendoor, tect (cost guides); autodesk (blog); oneestimate.ai; dgs.ca.gov (CCCI); reddit | No | 2026-dated. $350–$750/sf custom; San Francisco $600–$1,000+. |
| CO6 | construction cost breakdown by trade percentage for a new single family home | Cost | Saturated | NAHB (as source) | nahb.org x4 (industry survey); newbuildtools x2, construction-physics, costtobuildhouse, resiclubanalytics, statista, fixr, opendoor | No | Uses the 2024 NAHB survey: interior finishes 24.1%, rough-ins 19.2%, framing 16.6%, exterior finishes 13.4%, foundations 10.5%, site work 7.6%. |
| CO7 | podium apartment building construction cost per square foot 2026 | Cost | Contested | none | buildermuse x3 (incl. "construction cost index 2026"), buildmatinsight x4, terrapincg, landsouth, innergyintegral, irecruit, evstudio, pereff (aggregators, developers, architects); bidflow.visidex; rsmeans; bdcnetwork | No | 2026-dated. $240–$340/sf hard cost; podium deck alone $55–$80/sf. |
| CO8 | how much to budget for kitchen cabinets per unit in an apartment project | Cost | Open | none | atlasbuildsupply, kraftersland (MF cabinet suppliers); homeadvisor x2, angi x2, homeguide x2, fixr, modernize, homelight, homewyse (consumer remodel cost guides); woodweb | No | Mixed dates. $1,200–$1,800/unit basic; $3,900–$7,900 turnkey installed. WebSearch adds $80–$350/LF and KCMA A161.1. Only 2 pages are multifamily-specific. |
| TR1 | how to estimate drywall for a commercial project | Trade how-to | Contested | none | dfeestimating (service firm); simplysub (template); **quotr.ai (#3)**; joist; nationaldrywallauthority; stackct; procore (calculator); easytakeoffs (trade page); fieldpulse; estimatingedge; reddit r/estimators; calculators (certainteed, arcsite, turn2engineering, wutools) | **Cited ~6x inline, not named** (/blog/how-to-estimate-drywall-framing-commercial-floor-plan/) | Evergreen. In WebSearch, Quotr is not in the top 9 (joist, buildbook, contractorplus, scopetakeoff, estimatorflorida…). |
| TR2 | how to do an electrical takeoff from PDF plans | Trade how-to | Saturated | none (Bluebeam only in the closing offer) | easytakeoffs x2 (#1, trade page); solidtakeoff, circuittakeoff, electricaltakeoffsoftware, aginera x3, ibeam.ai x2, countfire, buildvisionai, drawer.ai, groundplan, stackct, bluebeam (vendor trade/feature pages); zipdo, worldmetrics (list farms) | No | Evergreen. Neither of Quotr's two electrical how-tos was retrieved. |
| TR3 | how to price a roofing job | Trade how-to | Saturated | none | getjobber x3, servicetitan x3, joist x3, simplywise x3, housecallpro, jobnimbus, zuper, build-folio (field-service software blogs); iko (manufacturer); nextdoor; angi | No | Evergreen. xBuild (roofing AI) is not cited. |
| TR4 | how to estimate a concrete slab foundation quantities and cost | Trade how-to | Saturated | none | calculators: calcdomain, buildvisionai, calculatorsoup, lowes, quikrete, sakrete x2, concretenetwork, calculator.net, tooldone, invoicefly, concretecalculatormax; structville, build-construct | No | Evergreen calculators. |
| TR5 | how to do a plumbing takeoff from drawings | Trade how-to | Saturated | none | **YouTube x8**; easytakeoffs (trade page); thetakeoff.ai (handbook); procore (library); bluebeam; buildvisionai; togal (blog); exayard (learn); buildxact; fieldpulse; scribd | No | Evergreen. YouTube is cited heavily. Quotr's plumbing how-to was not retrieved. |
| TR6 | how to estimate HVAC ductwork from mechanical drawings | Trade how-to | Contested | none | ibeam.ai x4 (blog guides, /subcontractors/hvac, /estimate/hvac-estimating-software); ductiq x3, buildvisionai x2, canaveral.ai, exayard, vertigraph, planswift, wendes (vendors); worldestimating (service); cedengineering (continuing-education course) | No | Evergreen. Beam AI leads. Quotr's HVAC how-to was not retrieved. |
| TR7 | how to estimate framing lumber for a house | Trade how-to | Saturated | none | calculators (angi x2, easytakeoffs, probuildercalc, homeprojectcalculator, infinitycalculator, omnicalculator, housecallpro); vendor guides (projul, simplywise, buildxact, exayard); iambuilders, pineconelumber, theplancollection, homeadvisor | No | Evergreen. |
| TR8 | how to estimate tile installation for a bathroom job | Trade how-to | Saturated | none | homeguide x2, homedepot, taskrabbit, modernize, angi, thespruce, bobvila, sweeten, blockrenovation, homewyse x2, bankrate (consumer cost guides); simplywise x2; lowes, calculator.net | No | 2026 consumer cost pages. |
| TR9 | how to estimate a commercial painting job | Trade how-to | Saturated | none | housecallpro, getjobber, fieldpulse, servicefusion, projul, estimatingedge, procore (vendors); benjaminmoore, ppgpaints, homedepot (brands/retail); thecpia, paintersacademy, alpinepainting, ppdpainting; airtasker, homeguide | No | Evergreen. |
| TR10 | how to estimate electrical labor hours per device | Trade how-to | Contested | NECA (Manual of Labor Units) | anvilfield, calcimator, field-pm, elecalculator, professioncalculators, heymaxgethammer (small calculators/blogs); pelles.ai x2, tradesquote.ai, buildops (vendors); necanet, benelli (NECA MLU); ecmweb (trade press); durandassociates, craftsman-book (PDF manuals) | No | Evergreen. Duplex receptacle 0.35–0.75 h; single-pole switch 0.30–0.60 h; fixture 0.50–0.75 h; 1.2–2.0x site-condition factors. |
| TR11 | how to do a kitchen cabinet takeoff from architectural plans | Trade how-to | Contested | none (Bluebeam only in the closing offer) | unicalibreestimating, thevirtualestimation, blazeestimating, marhamagroup, truecadd (estimating services); exayard x2, stackct, easytakeoffs, takeoffbot.ai, buildxact (vendors); ccccabinets, buildcabinets (cabinet makers); slabwise; woodweb; myquoteiq (2026 list) | No | Undated niche. |
| SV1 | how much does a freelance construction estimator charge | Service | Contested | none | lathire, optimarprecon, cost4estimating (estimating firms); swivl.tech; upwork x5, guru x2, freelancer, truelancer (marketplaces); reddit x3; constructionplacements; nobledesktop; ziprecruiter | No | Mixed dates. $30–$120/h (US $50–$100); takeoffs $200–$800; commercial estimates $1,500–$5,000+. |
| SV2 | outsourced estimating vs in-house estimator | Service | Contested | none | **quotr.ai (~10 inline citations, the most-cited source)**; vortexestimating, parametricestimates, edgeestimates (2026 benchmark), lathire, blazeestimating, unicalibreestimating, asestimation, worldestimating (estimating firms); stackct (blog); iambuilders x2; LinkedIn x4; reddit; buildmetric (AU) | **Cited, not named** (/blog/outsource-construction-estimating/) | 2026/mixed. The answer's in-house cost of "$90K–$130K+" blends several sources; Quotr's own page says $115K–$195K (see 1c). Quotr's /outsourcing-vs-hiring-an-estimator/ was not retrieved. |
| SV3 | construction estimator salary California 2026 | Service | Saturated | ZipRecruiter, Salary.com, Indeed (as sources) | ziprecruiter x4, salary.com x5, indeed x9, zippia, amundsongroup | No | Current. CA average $81,915 (ZipRecruiter) vs $98,718 (Salary.com). |
| SV4 | best construction estimating services for general contractors | Service | Contested | Edge Estimates, NEDES Estimating, Do Estimating, QTO Estimating, Royal Estimation, USA Estimating Solutions | edgeestimates, nedesestimating x2, doestimating, qtoestimating, royalestimation, usaestimatingsolutions, constructem, estimators.us, eliteestimatingsolutions, nationwideestimating, paragonestimating, iambuilders (firms' own pages and self-ranked lists); gitnux, f6s (list farms); aspenational (ASPE directory); forbes | No | Undated. Many firms rank themselves; there is no independent authority. |
| SV5 | how long does an outsourced construction estimating service take to deliver a bid estimate | Service | Contested | none | blazeestimating, lathire, mindwhiz, worldestimating, constructem, aconengineering, nedesestimating, aaaestimating, 1800estimating, designandbids, outsourceestimating, lewisestimating, californiaconstructionestimating, vortexestimating, totaltakeoffs (service firms); **quotr.ai (array only)** | **Retrieved only** (/blog/outsource-construction-estimating/) | Undated. 24–48 h standard; 2–5 business days for complex jobs; rush 8–12 h. |
| SV6 | who can prepare a construction cost estimate for a development feasibility study | Service/Developer | Open | none | usbr.gov, gsa.gov, fhwa.dot.gov, wbdg.org (US gov); hkis.org.hk x3 (Hong Kong), cits.wa.gov.au (Australia), unido, timor-leste.gov.tl; cmu.edu, tuiasi.ro (academic); areadevelopment | No | Old PDFs (about 2006–2020). Nothing is aimed at US private developers. |
| DV1 | how to estimate hard costs for a multifamily pro forma | Developer | Contested | none | innergyintegral, getbuilt, buildoraiq, stackrows x2 (vendors); jmco, focalinvest, maxlifedevelopment, thesisdriven, breakingintowallstreet, mergersandinquisitions (finance education); mass.gov, mhp.net, hdc-nw, durhamnc.gov, housingsolutionslab (public/nonprofit); NAR PDF; mmcginvest | No | Mixed dates. MA mid-rise wood frame ~$370/SF; FL garden $180–$260/SF, mid-rise $250–$400/SF; 5–10% contingency. |
| DV2 | construction budget template for developers | Developer | Saturated | none | projectmanager x4, smartsheet x4, bauwise x2, mastt x2, template.net x2, ganttpro x2, asana, sourcetable, projul, levelset (template sites) | No | Undated. All are generic construction budgets; none is a development budget covering land, hard and soft costs, and financing. |
| DV3 | hard costs vs soft costs percentage real estate development | Developer | Saturated | none | lintonglobalsolutions, marsh-partners, dwellsy, dealworthit, feldmanequities, monday, jdj-consulting, rets.ai, leaddeveloper, simoncre, multifamily.loans, adventuresincre, fundrise, dealpath (real-estate finance education) | No | Evergreen. Hard 70–85%, soft 15–30%. |
| DV4 | what contingency percentage to use in a construction budget | Developer | Saturated | none | aia.org, procore, fhwa (authorities); getbuilt, rabbet, buildertrend, projul, mastt, buildern, contractorforeman, gocodes, projectmanager (vendors); builderscapital; indeed; youngarchitect | No | Evergreen. 5–10% default; 10–15% for renovations. |
| DV5 | how to estimate construction costs before plans are finished for a land deal | Developer | Open | none | buildxact x3, procore, autodesk x2, deltek, sage, projectmanager, startbuild (vendors); rsmeans; wbdg, cmu, byui, tamu (reference/academic); homedepot; bartleby | No | Evergreen. A generic "conceptual estimate" answer with nothing on land-deal underwriting. |
| DV6 | construction cost escalation assumption for a pro forma 2026 | Developer | Saturated | JLL, Beck Group, Skanska, Altus (as sources) | jll x2, constructionowners (Beck Group), enr, skanska, taxcreditadvisor x2, finance-commerce, altusgroup, urbanland.uli, edzarenski, Turner & Townsend, Cushman & Wakefield (via tradingview), abccarolinas | No | Current. Base case 4–6%; stress case 7–10%. |
| DV7 | best real estate development pro forma software | Developer | Contested | ARGUS Developer, ARGUS Enterprise, DealCheck, Rabbet, TestFit | aprao (#1, vendor blog); northspyre (vendor blog); altusgroup; zipdo x2, wifitalents x2, worldmetrics x2 (list farms); sourceforge x3, softwareadvice (directories) | No | 2026 list farms. Quotr's two pro forma comparison posts were not retrieved. |
| BD1 | how to level subcontractor bids | Bidding | Saturated | none | meltplan (#1); buildr x2, archdesk, provision (2026 guide), beck-technology, datagrid, downtobid, exayard, buildxact, rib-software, ruh.ai (vendor guides); procore x2 (library + support); byui (textbook) | No | Mixed dates. "Plug numbers" is a cited step. The WebSearch top 9 (buildxact, downtobid, archdesk, crewcost, buildr x2, speclens, trueleveler, planhub) has no Quotr. |
| BD2 | markup vs margin in construction | Bidding | Saturated | none | constructiononline, trybeam, simplywise, procore, buildern x2, foreman.co, projul, ruh.ai, rib-software, jobtread, buildertrend (vendor explainers); gierschgroup | No | Evergreen. |
| BD3 | bid leveling template excel | Bidding | Saturated | BuildWorkPro, EstimateHawk, BuildIntel, Downtobid (template sources) | meltplan x3, buildworkpro, estimatehawk, constructionbids.ai x2, buildintel, construction.live, downtobid x2, quirepaper, procore, smartsheet, projectmanager, template.net, etsy, Microsoft marketplace x2, reddit | No | 2026 templates. |
| BD4 | what is a good overhead and profit percentage for a general contractor | Bidding | Saturated | none | projul x3, build-folio x2, buildern x2, planyard, cnba.us, togal (blog), procore, nextinsurance, txrac, angi, hubstaff, relayfi, buildingadvisor, gierschgroup | No | Evergreen. "10 and 10" rule (~20% markup). |
| BD5 | how to write a construction bid proposal as a subcontractor | Bidding | Saturated | none | smartsheet x3, projectmanager x2, proposify, getjobber, adobe, legaltemplates, skynova, monday, anygen (templates); procore x2, autodesk x2, stackct, buildvisionai, planhub (vendors) | No | Evergreen. |
| BD6 | what is a good bid hit ratio for subcontractors | Bidding | Saturated | none | enr (trade press); procore; constructconnect x2 (incl. "bid hit ratio commercial GCs 2026"); autodesk; construction.com; downtobid; projul; gobridgit; pilrs; cmaanet (association); sunflowerbank; constructionbusinessowner | No | Mixed dates. 20–30% hit rate; private work 4–6:1; public work 7–11:1. |
| AI1 | can ChatGPT do a construction takeoff | AI in precon | Contested | none | pilars.ai (page titled with this exact question); **quotr.ai (5 inline)**; technbrains; ruh.ai; buildxact; exayard (ChatGPT integration page); togal (blog); kreo x2; YouTube x5; reddit x2; OpenAI community; LinkedIn | **Cited 5x, not named** (/blog/chatgpt-for-construction-estimating/) | Mixed dates. In WebSearch, Quotr ranks #5 of 9 (behind Togal x2, ForConstructionPros and the OpenAI community). |
| AI2 | AI takeoff accuracy 2026 | AI in precon | Contested | Handoff (H1 benchmark), Togal.AI (subject of an ASC paper) | bildrix (#1, research page); **quotr.ai (#2)**; thetakeoff.ai (8-tool test, 2026); bricks-bytes x2 (Handoff H1 coverage); aginera; easytakeoffs; dancumberlandlabs; kreo; contravault x3; ASC 2026 paper (storage.googleapis.com); flowtivity; Stanford AI Index | **Cited 4x, not named** (/blog/is-ai-takeoff-actually-accurate-yet/) | 2026. Year-stamped variant of earlier P5; Quotr keeps a top-2 slot. Quotr's figures (95–99% on vector PDFs, 80–88% on scans) are used as rows in the benchmark table. |
| AI3 | AI estimating software for home builders | AI in precon | Saturated | Buildxact, Houzz Pro, Handoff, Togal.AI, Beam AI | buildxact x3, pro.houzz x2, handoff x2, togal, ibeam.ai, countbricks, alicetechnologies (vendor pages); thedigitalprojectmanager, layer3labs, nomic.ai, simplywise (listicles); nahb.org (sponsored Buildxact post) | No | Mixed dates. Recommendations go to vendors with review and NAHB footprints. |
| AI4 | how are general contractors using AI in preconstruction 2026 | AI in precon | Contested | none (AGC data cited) | **quotr.ai (#1 citation)**; provision x4, buildr x2, meltplan, chetu (vendors); enr x7, builtworlds x2 (trade press/lists); agc.org; contractorplus; businesswire (MIT–Suffolk study, Sep 16, 2026); natlawreview/einpresswire (Wyre AI) | **Cited first (2 inline), not named** (/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/) | Current. AGC-compiled uses: office/admin 45%, estimating 23–24%, bid management 22%, design/precon 20%. |
| AI5 | can AI compare subcontractor bids and find scope gaps | AI in precon | Saturated | none | piper-ai, trueleveler, getboon, constructionbids.ai, miragemetrics x2, meltplan x3, greatbuildz, c-link, buildr, arctisai, temelion, datagrid, omnionlinestrategies (~15 AI bid-leveling vendors); nomic.ai x2; costtoconstruct ("best AI bid leveling 2026") | No | 2026. A crowded AI bid-leveling niche. |
| AI6 | does AI takeoff work on scanned plans | AI in precon | Contested | none | thetakeoff.ai x2 (#1); rifflecm; appintent; buildr; handoff; technbrains; dreamztech; contractorcounter; eano; constructconnect (2026); dancumberlandlabs; stackct; palcode; bildrix; markovate; buildvisionai; kreo | No | 2026. Quotr's accuracy post covers scans but was not retrieved for this phrasing. |
| AI7 | how to use ChatGPT or Claude for construction estimating | AI in precon | Contested | none (ChatGPT and Claude are the subjects) | **YouTube x7**; buildr, ruh.ai, clickup, billd, hourly.io, exayard, simplywise, togal (blogs); reddit x2; Google Books; elspub (journal) | No | Mixed dates. Quotr's ChatGPT post was not retrieved for this "how to use" phrasing. |
| AI8 | how is AI used in construction procurement | AI in precon / Procurement | Contested | BRKZ (as example) | procore x2 (library); procurepro x2, conwize, buildops, zycus, lightsource, wipfli, cmicglobal, wrike (vendors); nomic.ai; enr x4; businesswire (MIT–Suffolk); itbrief, globenewswire, ventureburn (BRKZ $31M, Sep 14, 2026); costar | No | Current. The only concrete example is a GCC company (BRKZ); there is no US building-materials buyout example. |
| AI9 | will AI replace construction estimators | AI in precon | Saturated | none | gordian, constructconnect, mccormicksys, autodesk x2, procore, stackct, beck-technology, handoff, documentcrunch, civils.ai, technbrains (vendors); enr; cmaanet; constructionplacements; LinkedIn x2 | No | Mixed, evergreen. |

#### 1b. Tallies (Observed, hand-counted from the results above)
| Cluster | Prompts | Open | Contested | Saturated | Quotr cited in answer | Quotr in citation array (incl. retrieved only) | Quotr named |
|---|---|---|---|---|---|---|---|
| Procurement and importing (PR1–PR12) | 12 | 5 | 3 | 4 | 1 (PR2) | 1 | 0 |
| Cost questions (CO1–CO8) | 8 | 1 | 5 | 2 | 0 | 0 | 0 |
| Trade estimating how-tos (TR1–TR11) | 11 | 0 | 4 | 7 | 1 (TR1) | 1 | 0 |
| Estimating service and hiring (SV1–SV6) | 6 | 1 | 4 | 1 | 1 (SV2) | 2 (SV2, SV5) | 0 |
| Developer and pro forma (DV1–DV7) | 7 | 1 | 2 | 4 | 0 | 0 | 0 |
| Bidding (BD1–BD6) | 6 | 0 | 0 | 6 | 0 | 0 | 0 |
| AI in preconstruction (AI1–AI9) | 9 | 0 | 6 | 3 | 3 (AI1, AI2, AI4) | 3 | 0 |
| **Total** | **59** | **8** | **24** | **27** | **6 (10.2%)** | **7 (11.9%)** | **0 (0%)** |

- **Observed:** Quotr pages cited or retrieved:
  - [ddp-construction-materials](https://quotr.ai/blog/ddp-construction-materials/) (PR2)
  - [how-to-estimate-drywall-framing-commercial-floor-plan](https://quotr.ai/blog/how-to-estimate-drywall-framing-commercial-floor-plan/) (TR1)
  - [outsource-construction-estimating](https://quotr.ai/blog/outsource-construction-estimating/) (SV2 cited, SV5 retrieved only)
  - [chatgpt-for-construction-estimating](https://quotr.ai/blog/chatgpt-for-construction-estimating/) (AI1)
  - [is-ai-takeoff-actually-accurate-yet](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/) (AI2)
  - [state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs](https://quotr.ai/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/) (AI4, first citation)
- **Observed:** vendor or product brands were named as recommendations or examples in the answer text in only **6 of 59 prompts**: AI2, AI3, AI8, BD3, DV7 and SV4. All other answers were generic and gave only citations. See the table rows.
- **Observed:** the 8 Open prompts are PR1, PR7, PR9, PR10, PR11, CO8, SV6 and DV5. Six are about finish materials, procurement and cost; two are about developer feasibility estimates. Evidence for each:
  - PR1: factory blogs and a muddled duty stack — [buildtana](https://buildtana.com/articles/import-duties-building-materials-contractors-guide), [allurekitchencabinet](https://www.allurekitchencabinet.com/blog/kitchen-cabinets-from-china-complete-import-buying-guide-2026)
  - PR7: contradictory tile claims — [contigoceramics](https://contigoceramics.com/can-we-import-tiles-from-china/) vs [architessa](https://architessa.com/blogs/blog/chinese-tariffs-tile-industry)
  - PR9: generic Title 24 code documents — [gocodebook](https://gocodebook.com/us/california/california-energy-code/building-envelope-and-fenestration/fenestration-ratings-installation-and-special-systems), [CEC](https://www.energy.ca.gov/filebrowser/download/8883?fid=8883)
  - PR10: supplier homepages — [cpbuild](https://cpbuild.com/why-cp-build/what-we-do/), [summitedgecabinet](https://summitedgecabinet.com/multi-family)
  - PR11: one sourcing agent — [hsysourcing](https://www.hsysourcing.com/importing-villa-building-materials-from-china.html)
  - CO8: two supplier pages — [atlasbuildsupply](https://atlasbuildsupply.com/how-much-do-multi-family-kitchen-cabinets-cost/), [kraftersland](https://www.kraftersland.com/builder-cabinet-packages-pricing-grades-guide/)
  - SV6: non-US and older government/academic PDFs — [HKIS](https://www.hkis.org.hk/ufiles/QS-costplans2016.pdf), [WBDG](https://www.wbdg.org/design-disciplines/cost-estimating)
  - DV5: generic vendor explainers — [Buildxact](https://www.buildxact.com/us/blog/types-of-construction-estimates/), [RSMeans](https://www.rsmeans.com/resources/construction-cost-estimate-guide)

#### 1c. Facts surfaced in answers that writers will need (Observed; verify against primary sources before publishing)
- **Cabinets and vanities, Section 232:** a 25% tariff applies through 2026. The planned increase to 50% was delayed to Jan 1, 2027 — [STR Trade](https://www.strtrade.com/trade-news-resources/str-trade-report/trade-report/january/tariff-increase-delayed-on-furniture-kitchen-cabinets-vanities), [NAHB](https://www.nahb.org/blog/2026/01/wood-product-tariff-delays), [White House fact sheet](https://www.whitehouse.gov/fact-sheets/2025/12/fact-sheet-president-donald-j-trump-adjusts-imports-of-timber-lumber-and-their-derivative-products-into-the-united-states/)
- **Cabinets and vanities, stacked duties (WebSearch summary, not verified):**
  - Section 232 has applied since Oct 14, 2025 and stacks on Section 301 and AD/CVD.
  - The China AD/CVD orders (from 2020, extended Sept 2025) run up to 262.18% AD and 293.45% CVD, so the effective duty can exceed 70%.
  - NAHB is quoted as estimating that a $3,000 imported stock cabinet set lands at $3,750–$4,200.
  - The SERP included [Allyn International](https://www.allynintl.com/en/news-publications/entry/update-section-232-tariffs-on-kitchen-cabinets-vanities-and-furniture) and [NextDAY Cabinets](https://nextdaycabinets.com/kitchen-cabinet-tariffs-in-2026-what-contractors-and-builders-need-to-know-about-section-232-tariff-updates/). **I could not confirm which page states which figure.**
  - This **conflicts with** the Perplexity PR1 answer, which describes the cabinet duty as "25% Section 301" — [buildtana](https://buildtana.com/articles/import-duties-building-materials-contractors-guide)
- **Quartz:**
  - Base duty is free (HTS 6810.99.0010), with a 25% Chapter 99 duty on China — [CBP ruling N323819](https://rulings.cbp.gov/ruling/N323819)
  - AD/CVD orders on quartz from China were continued — [Federal Register](https://thefederalregister.org/documents/2025-01946/certain-quartz-surface-products-from-the-people-s-republic-of-china-continuation-of-antidumping-and-countervailing-duty-)
  - A tariff-rate quota on quartz surface products took effect Aug 15, 2026: 25% in-quota and 50% over-quota in year one, applying to all countries except Canada and Mexico — [STR Trade](https://www.strtrade.com/trade-news-resources/str-trade-report/trade-report/august/import-restrictions-on-quartz-surface-products-take-effect-aug-15)
  - A KQED URL in the citations is titled "California regulators unveil plan to ban new quartz countertops amid rising worker deaths" — [KQED](https://www.kqed.org/news/12100477/california-regulators-unveil-plan-to-ban-new-quartz-countertops-amid-rising-worker-deaths). Only the title was seen; the rule's status is unverified.
- **DDP vs FOB:** DDP is said to cost 15–25% more than FOB ([riwick](https://riwick.com/fob-vs-ddp-shipping-risk-cost-comparison/), [Cosmo Sourcing](https://www.cosmosourcing.com/blog/fob-vs-ddp-incoterms-pros-and-cons)), or 10–20% more with "default to FOB" advice in the WebSearch summary ([ship4wd](https://ship4wd.com/incoterms/fob-vs-ddp), [HiSourcing](https://www.hisourcing.com/fob-vs-ddp/)). This counter-narrative is what a Quotr DDP page must answer.
- **Factory-direct savings claims:**
  - 25–50% claimed, 30–45% net after freight and duty; imports pay off above a $40–60k or $80–100k finish budget — [hsysourcing](https://www.hsysourcing.com/importing-villa-building-materials-from-china.html), [hsysourcing 2](https://www.hsysourcing.com/sourcing-windows-cabinets-flooring-china-us-luxury-homes.html)
  - 25–40% — [newser](https://www.newser.com/expert-time/US-Residential-Construction-Sourcing-Shift-Rising-Direct-Imports-of-Chinese-Building-Materials-11-483)
  - Section 301 adds 7.5–25% — [First Link Partners](https://firstlinkpartners.com/importing-building-materials/)
  - WebSearch: cabinets and flooring 40–50%, windows 30–40%, $4,000–$8,000 per multifamily unit — [kdwalmsley Substack](https://kdwalmsley.substack.com/p/the-simple-math-why-even-small-construction)
- **Cabinets per apartment unit:** $1,200–$1,800 basic; $2,200–$3,200 mid; $4,500–$7,000+ high-end cabinets only — [Atlas Build Supply](https://atlasbuildsupply.com/how-much-do-multi-family-kitchen-cabinets-cost/). Turnkey installed $3,900–$7,900 — [Krafters Land](https://www.kraftersland.com/builder-cabinet-packages-pricing-grades-guide/)
- **Multifamily costs:**
  - $150k–$450k per unit; podium $240k–$380k per unit; "$225k middle-of-the-road" — [Buildmatinsight](https://buildmatinsight.com/construction-cost/app-cost/apartment-complex-construction-cost-comparison), [Visidex Bidflow](https://www.bidflow.visidex.com/articles/how-to-estimate-multifamily-buildout)
  - Podium $240–$340/SF hard cost — [BuilderMuse](https://buildermuse.com/residential/podium-apartment-construction-cost-2026/)
  - Massachusetts mid-rise wood frame ~$370/SF hard cost — [Mass.gov](https://www.mass.gov/info-details/home-for-everyone-construction-finance-explainer)
  - California impact fees average ~$29k per unit — [RAND](https://www.rand.org/news/press/2025/04/cost-to-build-multifamily-housing-in-california-more.html)
- **LA fire rebuild:**
  - $350–$750+/sf, commonly $450–$600; hillside $1,000–$1,800+ — [Benson Construction Group](https://www.bensonconstructiongroup.com/fire-rebuild-cost-los-angeles)
  - WebSearch: Palisades $550–$900/sf; pre-construction and carrying costs add 25–40% — [LAGBS 2026 guide](https://www.lagbs.com/post/altadena-eaton-fire-rebuild-cost-2026), [B+W Engineering](https://bwengr.com/blog/2026/04/12/altadena-rebuild-costs/)
- **Escalation for 2026 pro formas:**
  - JLL: ~5% year over year, with a risk of ~8% in the second half of 2026 — [JLL](https://www.jll.com/en-us/insights/2026-midyear-us-construction-perspective)
  - Beck Group: 4.1–4.6% — [Construction Owners](https://www.constructionowners.com/news/beck-group-updates-2026-construction-cost-outlook-for-owners-and-developers)
  - Skanska: 4–6% baseline, 7–10% under tariff scenarios — [Skanska](https://interactive.usa.skanska.com/2026-winter-construction-market-trends)
- **Lead times:** transformers 52–74 weeks, switchgear 40–70 weeks, generators ~40 weeks — [DPR Q3 2026](https://www.dpr.com/view/q3-2026-market-conditions-report), [Terrapin](https://terrapincg.com/news/commercial-construction-material-lead-times-2026)
- **Estimator cost:**
  - Freelancers $30–$120/h; commercial estimate $1,500–$5,000+ — [LatHire](https://lathire.com/outsource-construction-estimating/), [Optimar](https://optimarprecon.com/how-much-does-construction-estimating-cost/)
  - California salary $81,915 ([ZipRecruiter](https://www.ziprecruiter.com/Salaries/Construction-Estimator-Salary--in-California)) vs $98,718 ([Salary.com](https://www.salary.com/research/salary/listing/construction-estimator-salary/ca))
  - Outsourcing wins below ~12–15 estimates a month; hiring wins at 20+ — [Quotr](https://quotr.ai/blog/outsource-construction-estimating/), [Edge Estimates](https://edgeestimates.com/construction-estimating-cost-benchmark-2026/)
- **AI takeoff accuracy:**
  - Handoff's public H1 benchmark: 81.6%, vs ~55% for general-purpose models and ~77–78% for human estimators — [Bricks & Bytes](https://bricks-bytes.com/ai/ai-construction-takeoffs-two-weeks-to-two-hours-handoff/)
  - Independent ASC 2026 paper on Togal: small but statistically significant deviations — [ASC paper](https://storage.googleapis.com/cm-app-90d65.firebasestorage.app/ASC_2026_Papers/paper_157.pdf)
  - 2026 comparison of 8 tools across 6 drawing types — [thetakeoff.ai](https://www.thetakeoff.ai/blog/ai-takeoff-software-comparison-8-tools-across-six-drawing-types-in-2026)
- **AI adoption:** AGC-compiled data shows AI used for office/admin 45%, estimating 23–24%, bid management 22%, design/precon 20% — [ContractorPlus](https://contractorplus.app/blog/ai-adoption-contractors-2026). MIT–Suffolk study released Sept 16, 2026 — [BusinessWire](https://www.businesswire.com/news/home/20260916688771/en/MIT-Suffolk-Release-Joint-Study-on-How-Artificial-Intelligence-is-Transforming-the-Construction-Industry)
- **SV2 figure blending (Observed discrepancy):**
  - Perplexity gave in-house estimator cost as "$90K–$130K+", citing parametricestimates, lathire and quotr.ai.
  - The `site:quotr.ai` WebSearch summary of Quotr's own page says a fully loaded in-house estimator costs **$115,000–$195,000/yr** — [Quotr outsource post](https://quotr.ai/blog/outsource-construction-estimating/)
  - So the engine blends Quotr's figures with competitors' figures.

#### 1d. Perplexity vs WebSearch and non-vendor sources (Observed)
- **Perplexity cites Quotr where classic search does not rank it:**
  - PR2 (DDP vs FOB) and TR1 (commercial drywall): Perplexity cited Quotr, but Quotr is not in the WebSearch top 9 — [ship4wd](https://ship4wd.com/incoterms/fob-vs-ddp), [scopetakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/)
  - AI1 (ChatGPT takeoff): Quotr ranks #5 of 9 in WebSearch — [Quotr](https://quotr.ai/blog/chatgpt-for-construction-estimating/)
  - This repeats the earlier P5 pattern: Perplexity-cited but outside the WebSearch top 9.
- **The AI1 WebSearch summary repeated a claim** already flagged as unverified in the earlier audit: "Independent 2025 testing has put ChatGPT around 65–75% accuracy reading construction drawings." Its source page among the results (Togal, OpenAI community, Quotr, Exayard, ruh.ai, SmartAIforWork) could not be identified.
- **Community and social sources (hand-tallied):**
  - LinkedIn appeared in the citation arrays of **12 of 59** prompts (PR3, PR8, PR11, CO7, SV2, SV4, TR6, AI1, AI4, AI5, AI8, AI9).
  - Reddit appeared in **10 of 59** (TR1, TR11, CO3, CO4, CO5, SV1, SV2, BD3, AI1, AI7).
  - YouTube appeared in **3 of 59**, with 20 video URLs, 19 of them unique (TR5 x8, AI1 x5, AI7 x7). This revises the earlier audit's observation that YouTube was never cited in 45 runs. Example: [YouTube plumbing takeoff](https://www.youtube.com/watch?v=YIaGv-2Dor4)

### Inferences
- **The Open topics line up with Quotr's moat.** Six of the eight Open prompts ask about landed cost, compliance, bulk buying, savings and per-unit budgets for finish materials. Right now these answers are assembled from Chinese sourcing-agent blogs, supplier homepages and code PDFs. A US-buyer-side page with dated, sourced numbers and real project data (Quotr's Bay Area procurement comparisons) has a realistic path to becoming the default citation. The two developer feasibility prompts (SV6, DV5) map directly onto Quotr's developer Estimation Service.
- **Quick wins are refreshes.** In all six prompts where Quotr is cited, it already has a page with explicit numbers, and all six are Contested. Refreshing those pages (dates, sourced statistics, worked examples, brand-attributed statements such as "Quotr.ai's Estimation Service data shows…") is the cheapest way to keep the citations and start earning brand naming.
- **Naming, not retrieval, is the problem.** Quotr was named 0 times in 59 prompts. Its six cited topics are how-tos and explainers, where Perplexity rarely names any vendor. Quotr needs attributable original data (a named dataset or benchmark), named expert authors, and third-party corroboration (the earlier audit's G2/listicle findings) to convert citations into mentions.
- **Avoid generic bidding and trade how-tos.**
  - Bidding (6/6 Saturated) is owned by the Procore Library, field-service vendors and Meltplan.
  - The simple-trade how-tos (roofing, concrete, framing, tile, painting, electrical-takeoff basics) are owned by calculators and vendor trade pages.
  - Quotr should enter only through niche angles: plug numbers, supplier-quote leveling for material buyout, electrical labor units, and cabinet/millwork takeoff tied to procurement.
- **Tariff content carries accuracy and maintenance risk.** The PR1 answer is wrong or muddled about the cabinet duty stack. A correct, dated, broker-reviewed page could become the reference, but it needs a named update owner, because the Section 232 rate changes on Jan 1, 2027 and quartz rules changed Aug 15, 2026.
- **Off-site distribution matters on these topics.** LinkedIn (12/59) and Reddit (10/59) are cited more often than most vendor domains. Founder or expert LinkedIn articles that restate Quotr's data, and authentic r/estimators participation, are likely to feed these same answers. YouTube matters for "how to do X takeoff" and "how to use ChatGPT/Claude" queries.
- **Fix Quotr's inconsistent facts before publishing in these clusters.** The earlier audit found turnaround stated as 24 hours, 3–4 days and 5–7 days; factory count as 50+ vs 220+; and savings as "up to 50%" vs 40–55%. The `site:quotr.ai` summary for procurement still returns both 50+ and 220+ factories and both "up to 50%" and "40–55%". SV5 (turnaround) and PR11 (savings) are exactly where those conflicts would surface.

### Gaps
- Only Perplexity Sonar was tested, one run per prompt. ChatGPT, Google AI Overviews/AI Mode, Gemini, Claude and Copilot could not be queried. Earlier reruns showed citation arrays stable day to day but brand order varying.
- Classification is a judgment call applied to one answer and its citations. Borderline cases: PR4 (strong government sources, but only 2 importer-checklist pages), DV5 (strong generic domains, but off-target) and TR5 (many vendor pages plus YouTube).
- Search and prompt volume per topic was not measured, so "winnable" does not mean "high demand".
- Tariff and AD/CVD figures come from answer text and search summaries, not from reading CBP or Federal Register primary pages. They need verification.
- I could not identify the channels behind the 19 cited YouTube videos, so I cannot tell whether any competitor owns them.

---

## 2. What do the most visible competitors publish (clusters and formats, rough volume), and which of their pages get cited?

### Takeaway
- **Most-cited vendor domains:** the **Procore Library is the most-cited vendor domain** (14 of 59 prompts). Next come Buildxact, STACK and Exayard (7 each), Easy Takeoffs and BuildVision AI (6), then Meltplan and Togal (5). Quotr also has 7, but it holds them with explainers and has no brand naming.
- **Formats competitors win with that Quotr lacks:**
  - free **calculators** (BuildVision AI, Easy Takeoffs, Procore)
  - free **templates** (Meltplan, Exayard, Procore, BuildVision AI, STACK)
  - programmatic **"cost to build X 2026" guides** (Exayard, Meltplan, Togal; also oneestimate.ai for California cities)
  - **library/glossary hubs** (Procore, Bluebeam, STACK)
  - per-trade pages (Easy Takeoffs, Beam AI, STACK, Exayard)
- **Comparison hubs and YouTube:** Beam AI and Togal add comparison ("vs") hubs and **YouTube** webinars and demos.
- **Procurement rivals are absent:** Field Materials, xBuild, Bobyard and Foreman AI were **not cited in any of the 59 prompts**, and no competitor publishes factory-direct or landed-cost content.

### Cited Findings

#### 2a. Competitor domains cited across the 59 prompts (Observed; number of prompts whose citation array contains the domain, hand-tallied ±1)
| Rank | Domain | Prompts | Which prompts (page types) |
|---|---|---|---|
| 1 | procore.com (Library) | 14 | TR1 (calculator), TR5, TR9, DV4, DV5, BD1, BD2, BD3, BD4, BD5, BD6, AI8, AI9, PR12 (library explainers, templates) |
| 2 | linkedin.com | 12 | posts/articles (see 1d) |
| 3 | reddit.com | 10 | r/estimators and real-estate subreddits (see 1d) |
| 4 | simplywise.com | 8 | TR3, TR7, TR8, TR10, BD2, DV4, AI3, AI7 (contractor-app blog) |
| 5 | buildxact.com | 7 | TR5, TR7, TR11, DV5, BD1, AI1, AI3 (evergreen how-to blog, feature pages) |
| 5 | stackct.com | 7 | TR1, TR2, TR11, SV2, BD5, AI6, AI9 (trade software pages, blog) |
| 5 | exayard.com | 7 | TR5, TR6, TR7, TR11, BD1, AI1, AI7 (learn pages, trade pages, cost guides, ChatGPT integration) |
| 5 | projul.com | 7 | TR7, TR9, DV2, DV4, BD2, BD4, BD6 (templates, explainers) |
| 5 | **quotr.ai** | 7 | PR2, TR1, SV2, SV5, AI1, AI2, AI4 |
| 5 | angi.com | 7 | CO4, CO5, CO8, TR3, TR7, TR8, BD4 (consumer cost guides) |
| 11 | autodesk.com | 6 | TR1, CO5, DV5, BD5, BD6, AI9 |
| 11 | easytakeoffs.com | 6 | TR1, TR2, TR5, TR7, TR11, AI2 (trade pages, calculators, listicle) |
| 11 | buildvisionai.com | 6 | TR2, TR4, TR5, TR6, BD5, AI6 (features, calculator, templates, "best X") |
| 14 | enr.com, buildr.com, meltplan.com, togal.ai | 5 each | ENR: news/data; buildr: AI/bid guides; Meltplan: bid-leveling cluster, cost benchmarks; Togal: blog explainers |
| 18 | ibeam.ai, handoff.ai, kreo.net, thetakeoff.ai, nomic.ai, buildmatinsight, terrapincg, hsysourcing, tonlexing | 3 each | Beam: TR2, TR6 (4 URLs), AI3; Handoff: AI3, AI6, AI9; Kreo: AI1, AI2, AI6 |
| — | bluebeam.com | 2 | TR2, TR5 (workflows page) |
| — | contravault.com | 1 | AI2 (3 listicles) |
| — | bobyard.com, fieldmaterials.com, foremanai.co, xBuild | 0 | not cited in these 59 prompts |

#### 2b. Formats and observed volume by competitor (Observed from WebSearch results and citation arrays; volumes are pages seen in results, i.e. lower bounds, because sitemaps were egress-blocked)
- **Procore Library**
  - **Formats:**
    - library explainers for nearly every bidding, estimating and budgeting definition: bid leveling, markup and margin, overhead and profit, contingency, bid-hit ratio, bid proposals, plumbing takeoff, painting estimating, AI estimating, procurement intelligence
    - calculators ([drywall calculator](https://www.procore.com/library/calculators/drywall-calculator))
    - templates ([estimate template](https://www.procore.com/library/construction-estimate-template), [bid tabulation template](https://www.procore.com/library/bid-tabulation))
    - a [glossary](https://www.procore.com/library/glossary)
    - survey reports: [Future State of Construction](https://www.procore.com/ebooks/future-state-of-construction), 1,200+ decision-makers in 8 countries — [press release](https://www.procore.com/press/future-state-of-construction-report)
  - **Cited in:** 14 prompts, e.g. [bid leveling](https://www.procore.com/library/construction-bid-leveling), [bid-hit ratio](https://www.procore.com/library/bid-hit-ratio), [procurement intelligence](https://www.procore.com/en-gb/library/procurement-intelligence).
- **Buildxact**
  - **Formats:** a large US blog of evergreen residential estimating guides (≥8 US guides surfaced by one query):
    - [how to estimate construction costs](https://www.buildxact.com/us/blog/how-to-estimate-construction-costs/)
    - [how to estimate building materials](https://www.buildxact.com/us/blog/how-to-estimate-building-materials/)
    - [construction estimating guide](https://www.buildxact.com/us/blog/construction-estimating/)
    - [bid leveling for residential builders](https://www.buildxact.com/us/blog/what-is-the-process-of-bid-leveling/)
    - also feature pages and NAHB sponsored content ([NAHB sponsored post](https://www.nahb.org/blog/2025/02/sponsored-buildxact))
  - **Cited in:** 7 prompts.
- **STACK**
  - **Formats:**
    - trade software pages (drywall, electrical, [cabinetry](https://www.stackct.com/cabinetry-takeoff-estimating-construction-software/))
    - blog: [bid template](https://www.stackct.com/blog/construction-bid-template/), [glossary](https://www.stackct.com/blog/construction-glossary/), [2026 construction forecast](https://www.stackct.com/blog/2026-construction-forecast-five-things-contractors-need-to-know/), outsource vs in-house, AI for takeoffs
    - a [Floor Plan AI page](https://www.stackct.com/floor-plan-ai/)
  - **Cited in:** 7 prompts.
- **Exayard**
  - **Formats:**
    - **programmatic "cost to X" 2026 guides** (≥6 seen): [cost per square foot](https://exayard.com/blog/construction-cost-per-square-foot), [apartment complex 2026](https://exayard.com/blog/cost-to-build-apartment-complex), [home addition](https://exayard.com/blog/home-addition-cost), [concrete slab](https://exayard.com/blog/cost-to-pour-a-concrete-slab), [garage](https://exayard.com/blog/cost-to-build-a-garage), [framing cost per sq ft](https://exayard.com/blog/framing-cost-per-square-foot)
    - template round-ups: [12 estimating templates 2026](https://exayard.com/blog/construction-estimating-template-free), [7 estimate samples 2026](https://exayard.com/blog/construction-estimate-sample-1)
    - /learn/ trade takeoff pages ([plumbing takeoff](https://exayard.com/learn/plumbing-takeoff))
    - trade software pages ([HVAC](https://exayard.com/hvac-estimating-software), [cabinetry/millwork](https://exayard.com/cabinetry-millwork-takeoff-software))
    - a [ChatGPT integration page](https://exayard.com/integrations/chatgpt)
  - **Cited in:** 7 prompts; the integration page appears in AI1 and AI7.
- **Easy Takeoffs**
  - **Formats:**
    - a [calculators hub](https://easytakeoffs.com/calculators) covering concrete, roofing, drywall, [framing](https://easytakeoffs.com/calculators/framing-lumber) and tile
    - /trades/ pages ([drywall](https://easytakeoffs.com/trades/drywall), electrical, plumbing, general contractor)
    - "best X" and alternatives listicles ([best AI takeoff](https://easytakeoffs.com/blog/best-ai-takeoff-software), [best free construction calculators 2026](https://easytakeoffs.com/blog/best-free-construction-calculators))
  - **Cited in:** 6 prompts; it is the #1 citation for the electrical takeoff prompt (TR2).
- **BuildVision AI**
  - **Formats:**
    - a [calculator suite](https://www.buildvisionai.com/calculators) (drywall, framing, [concrete slab](https://www.buildvisionai.com/calculators/concrete-slab-calculator), [construction cost](https://www.buildvisionai.com/calculators/construction-cost-calculator))
    - [/tools](https://www.buildvisionai.com/tools)
    - templates ([estimate](https://www.buildvisionai.com/templates/construction-estimate), [bid 2026](https://www.buildvisionai.com/templates/construction-bid))
    - "best X" listicles ([takeoff 2026](https://www.buildvisionai.com/best-construction-takeoff-software), [HVAC estimating](https://www.buildvisionai.com/best-hvac-estimating-software))
    - /construction-estimating/(trade), /features, /use-cases
  - **Cited in:** 6 prompts.
- **Meltplan**
  - **Formats:**
    - a **bid-leveling cluster** (≥6 posts): [how to level sub bids](https://www.meltplan.com/blogs/how-to-level-subcontractor-bids-a-step-by-step-process-for-gc-estimators), [free Excel template](https://www.meltplan.com/blogs/the-bid-leveling-template-gcs-actually-use-free-excel-download), [spreadsheet from scratch](https://www.meltplan.com/blogs/how-to-build-a-bid-leveling-spreadsheet-from-scratch), [best bid-leveling software 2026](https://www.meltplan.com/blogs/best-bid-leveling-software-for-general-contractors-2026-comparison), AI bid leveling, [/bid product page](https://www.meltplan.com/bid)
    - **cost benchmarks** ([$/SF 2026 by building type](https://www.meltplan.com/blogs/construction-cost-per-square-foot-2026-us-benchmarks-by-building-type), [ENR CCI explainer](https://www.meltplan.com/blogs/enr-construction-cost-index-what-it-is-and-how-to-use-it))
    - estimating how-to and [estimate templates](https://www.meltplan.com/blogs/construction-estimate-templates-free-downloads-and-best-practices-for-gc-estimators)
    - a [GC AI guide 2026](https://www.meltplan.com/blogs/ai-tools-for-construction-the-gc-s-guide-2026)
  - **Cited in:** 5 prompts; it is the #1 citation for "how to level subcontractor bids" and has 3 URLs in the bid-leveling-template prompt.
- **Togal.AI**
  - **Formats:**
    - "vs" pages ([vs PlanSwift](https://www.togal.ai/vs/planswift), [vs Bluebeam](https://www.togal.ai/vs/bluebeam))
    - blog explainers ([commercial cost per sq ft](https://www.togal.ai/blog/commercial-construction-costs-per-square-foot), [average profit margin](https://www.togal.ai/blog/average-profit-margin-for-construction-industry), [ChatGPT + Togal](https://www.togal.ai/blog/chatgpt-togal-ai-takeoff-construction-software))
    - **YouTube** (≥7 videos surfaced, one of them a Beck Technology + Togal video): a [full-length demo](https://www.youtube.com/watch?v=MJB6HEyWAQg), a [flooring takeoff webinar](https://www.youtube.com/watch?v=TPN8_322B0s), MEP takeoff in under 4 minutes
  - **Cited in:** 5 prompts, all blog pages plus the homepage.
- **Beam AI (ibeam.ai)**
  - **Formats:**
    - a [/compare hub](https://www.ibeam.ai/compare) (≥6 pages seen: [vs STACK](https://www.ibeam.ai/compare/vs-stack), [vs Autodesk Takeoff](https://www.ibeam.ai/compare/vs-autodesk-takeoff), vs Active Takeoff, vs Square Takeoff, [vs zzTakeoff](https://www.ibeam.ai/compare/vs-zztakeoff))
    - /subcontractors/(trade) ([HVAC](https://www.ibeam.ai/subcontractors/hvac)), /estimate/(trade), /suppliers/(trade)
    - blog trade guides ([HVAC takeoffs](https://www.ibeam.ai/blog/guide-to-accurate-hvac-takeoffs))
    - a [YouTube channel](https://www.youtube.com/@iBeamAI) and the [BuildUp webinar series](https://www.youtube.com/watch?v=OTViOqw0lEI)
  - **Cited in:** 3 prompts, with 4 URLs in the HVAC ductwork prompt.
- **Handoff**
  - **Formats:**
    - long-form guides ([AI estimating ultimate guide 2026](https://www.handoff.ai/blog/ai-estimating-software-the-ultimate-guide-for-contractors-2026), [what AI takeoffs can and can't read](https://handoff.ai/blog/seven-things-ai-takeoffs-can-and-cant-read-on-your-construction-plans))
    - a product page ([/instant-ai-estimates](https://www.handoff.ai/instant-ai-estimates))
    - a public H1 benchmark, covered by [Bricks & Bytes](https://bricks-bytes.com/ai/handoff-h1-not-a-takeoff-tool-dmitry-alexin/)
  - **Cited in:** 3 prompts; named in AI3.
- **Kreo:** explainers ([what is AI takeoff](https://www.kreo.net/news-2d-takeoff/what-is-ai-takeoff), [ChatGPT for takeoff](https://www.kreo.net/news-2d-takeoff/chatgpt-for-takeoff-and-estimating)) and solution pages. **Cited in:** 3 prompts.
- **Bluebeam:** [glossary](https://www.bluebeam.com/resources/glossary/) and a [takeoff workflows page](https://www.bluebeam.com/workflows/takeoffs-and-estimation/). **Cited in:** 2 prompts.
- **ContraVault:** a high-volume "10/15 best X software 2026" listicle factory (≥7 seen): [AI takeoff](https://www.contravault.com/blog/10-best-ai-takeoff-software-tools-for-construction-in-2026), AI estimating, structural steel, [piping](https://www.contravault.com/blog/10-best-piping-estimating-software-solutions-in-2026), mechanical, [AI bidding (15)](https://www.contravault.com/blog/15-ai-construction-bidding-software-tools-in-2026). **Cited in:** 1 prompt (AI2, 3 URLs).
- **Foreman AI (foremanai.co):** a blog listicle, [9 best AI takeoff 2026 "with real pricing"](https://foremanai.co/blog/best-ai-takeoff-software-2026), and an explainer, [what is a construction takeoff (2026)](https://foremanai.co/blog/what-is-a-construction-takeoff). **Cited in:** 0. Note: "foreman.co", cited in BD2, is a different domain and its relationship to Foreman AI is unverified.
- **Field Materials AI:**
  - **Formats:**
    - blog: [vendor quote management](https://www.fieldmaterials.com/blog/how-you-manage-vendor-quotes-can-lead-to-higher-material-costs), [pricing intelligence](https://www.fieldmaterials.com/blog/pricing-intelligence-radar-construction-material-prices), ROI, [top 2026 procurement software listicle](https://www.fieldmaterials.com/blog/top-2026-construction-procurement-software-construction-material-management-software-providers), AI agents
    - platform pages ([quote management](https://www.fieldmaterials.com/platform/construction-quote-management-software), [building material prices](https://www.fieldmaterials.com/platform/building-material-prices))
    - trade pages (mechanical contractors)
  - **Claims:** 5–10% material savings; trained on documents from 25,000+ suppliers (WebSearch summary).
  - **Cited in:** 0 of these 59 prompts.
- **Bobyard:** blog "vs" pages with a landscape focus ([vs On-Screen Takeoff](https://www.bobyard.com/blogs/bobyard-vs-on-screen-takeoff/)). **Cited in:** 0.
- **xBuild:**
  - **Company:** $19M Series A (Jan 2026) led by N47, with Rackhouse Ventures and Andreessen Horowitz. It launched "Roofing Proposals" (a residential roofing estimate in under 15 minutes). It began in 2025 with an insurance-focused estimating tool and reports 15,000+ projects and $250M in volume. It plans to expand into concrete, landscaping, painting, windows and doors, glazing, insulation, HVAC and plumbing — [SiliconANGLE](https://siliconangle.com/2026/01/20/xbuild-raises-19m-launch-ai-powered-residential-roofing-contract-estimation-product/), [PR Newswire](https://www.prnewswire.com/news-releases/xbuild-raises-19m-series-a-launches-ai-powered-residential-roofing-estimate-product-302664721.html)
  - **Formats:** visible content is press syndication (Yahoo Finance, Roofing Contractor, IIReporter) and a third-party review ([Contractor ToolStack](https://contractortoolstack.com/software/xbuild/)).
  - **Cited in:** 0, including the roofing pricing prompt (TR3).
- **Other AI-native vendors cited in these tests that are not on the list:**
  - pilars.ai: exact-match "can ChatGPT do takeoffs" page — [pilars.ai](https://pilars.ai/can-chatgpt-do-construction-takeoffs)
  - thetakeoff.ai: handbook and a 2026 8-tool test — [thetakeoff.ai](https://www.thetakeoff.ai/handbook/mep-takeoff)
  - buildr.com, provision.com, aginera.ai, oneestimate.ai (programmatic California city cost calculator — [oneestimate.ai](https://oneestimate.ai/en/california/cost-calculator)), bildrix (research page — [bildrix](https://bildrix.com/research/ai-takeoff-accuracy)), ruh.ai, nomic.ai

#### 2c. Format coverage matrix (Observed in this session and in the earlier benchmark; "—" = not observed, not proven absent)
| Competitor | Calculators | Cost guides ($/SF, cost to build) | Templates | Glossary / library | State-of / survey reports | vs / alternatives hub | Trade pages | YouTube |
|---|---|---|---|---|---|---|---|---|
| Procore Library | Yes | — | Yes | Yes | Yes (Future State) | — | — | — |
| Buildxact | — | Partial (cost breakdowns) | Partial | Yes (evergreen blog) | — | — | Feature pages | Tutorials (earlier audit) |
| STACK | — | — | Yes (bid template) | Yes (glossary) | Forecast 2026 | — | Yes | — |
| Exayard | — | **Yes (≥6 "cost to X 2026")** | Yes (round-ups) | /learn | — | — | Yes | — |
| Easy Takeoffs | **Yes (hub)** | Calculator cost estimates | — | — | — | Yes (alternatives) | Yes | — |
| BuildVision AI | **Yes (suite)** | Cost calculator | Yes | Docs | — | "best X" lists | Yes | — |
| Meltplan | — | **Yes ($/SF 2026, ENR CCI)** | **Yes (bid leveling, estimate)** | — | — | Best-of comparisons | — | — |
| Togal.AI | — | Yes (commercial $/SF) | — | Blog explainers | Peer-reviewed study (earlier) | Yes (/vs/) | Webinars | **Yes** |
| Beam AI | — | — | Checklists (earlier) | Blog trade guides | — | **Yes (/compare hub)** | **Yes** | **Yes** |
| Handoff | — | "68M costs" data claim (earlier) | — | Long-form guides | Public H1 benchmark | Own listicles | Persona pages | — |
| Kreo | — | — | — | Explainers | — | /compare-against/ (earlier) | /trades/ (earlier) | — |
| Field Materials | — | Material price platform | — | Blog | — | Procurement listicle | Trade pages | — |
| ContraVault, Foreman AI | — | — | — | Explainers | — | **Listicle factories** | — | — |
| **Quotr (for contrast)** | ROI calculator only | None | None | 55 thin dictionary terms | Secondary-source "State of AI" | 12 comparison pages | 23 thin trade pages | 5 tutorials |

### Inferences
- **Competitors win top-of-funnel citations with utility formats and breadth, not with better opinions.** The Procore Library's 14/59 shows that a deep, evergreen explainer library beats scattered posts. Quotr's 55-term dictionary is the closest equivalent but is too thin to compete (the one term sampled in the earlier audit was ~200 words).
- **Quotr should not clone saturated utilities** (concrete, drywall and framing calculators; generic estimate and bid templates). Engines already cite 10+ of those per query. It should build utilities no competitor has:
  - a landed-cost and duty calculator for finish materials
  - a DDP vs FOB comparison calculator
  - a per-unit finish-package budget calculator
  - an outsourced vs in-house estimating break-even calculator
  - a developer budget template covering land, hard costs, soft costs, financing and contingency
- **Programmatic cost pages work for small vendors.** Exayard, Meltplan and oneestimate.ai get cited next to RSMeans and NAHB. Quotr can do California- and finish-material-specific versions backed by real estimate and procurement data, which is more defensible than national averages.
- **Procurement white space is confirmed.** None of the procurement-focused rivals (Field Materials, xBuild, Bobyard) appeared in 59 answers, and no software vendor appeared in any Open procurement answer. The competition on landed cost, compliance and factory-direct topics is Chinese sourcing agents and logistics blogs, not software companies.
- **Video is a secondary lever.** YouTube is cited for plumbing takeoff and ChatGPT/Claude estimating queries, and Togal and Beam run webinar series. Adding short videos to Quotr's ChatGPT and takeoff pages, plus its 5 existing tutorials, is a medium-term way into those answers.

### Gaps
- **No sitemap totals:** WebFetch was egress-blocked for meltplan.com, exayard.com and easytakeoffs.com, so volumes are counts of pages seen in search results, not totals. Blog cadence, total post counts, schema and llms.txt could not be checked.
- **xBuild's domain** did not appear in any result (xbuild.com and xbuild.ai returned nothing), so its owned content is unknown.
- **Unverified volumes:** content volume for Bobyard, Foreman AI and Field Materials was sampled with one query each. Handoff's, Buildxact's and STACK's YouTube programs were not verified; only Togal and Beam video results appeared.
- **Single engine and run:** citation counts come from one Perplexity run per prompt. Google AI Overviews may weight these domains differently (e.g., more YouTube and Reddit).

---

## 3. How do Quotr's existing posts map to the candidate topics (refresh, consolidate or create new)?

### Takeaway
- **Refresh first:** Quotr has **6 pages that are already cited** on Contested topics. They should be refreshed first.
- **Consolidate:** it has **overlapping posts in about 7 clusters** (estimating services, electrical how-tos, AI explainers, pro forma software, procurement process, cost/tariff trend posts, AI bid software).
- **Create new:** it has **no page at all** for the 8 Open topics or for most cost and procurement specifics (material-specific landed cost and tariffs, CARB/NFRC/cUPC compliance, factory vetting, per-unit finish budgets, California cost benchmarks, LA fire rebuild costs, feasibility estimates, hard-cost pro forma how-to, cabinet/millwork takeoff, electrical labor units, plug numbers).

### Cited Findings

#### 3a. What `site:quotr.ai` searches surfaced (Observed)
- **Procurement query:**
  - Pages returned: [construction-procurement-process](https://quotr.ai/blog/construction-procurement-process/), [ai-agents-for-construction-procurement-and-buyout](https://quotr.ai/blog/ai-agents-for-construction-procurement-and-buyout/), [quantity-takeoff-services](https://quotr.ai/blog/quantity-takeoff-services/), [construction-estimating-services](https://quotr.ai/blog/construction-estimating-services/), [/contractors](https://quotr.ai/contractors), [/disambiguation/](https://quotr.ai/disambiguation/). **No tariff-, CARB-, NFRC- or material-specific landed-cost page appeared.**
  - Summary text: DDP covers "factory cost, export packing, ocean freight, US customs and duties, final-mile delivery, and certification documents (NFRC, CARB, cUPC)", with categories of windows and doors, garage doors, cabinetry and millwork, flooring, and bath and plumbing fixtures.
  - It also shows **both** "50+ verified factories" and "220+ vetted factories", and **both** "up to 50% below retail" and "40–55% below dealer pricing".
- **Cost query:** only [dictionary/cost-per-square-foot](https://quotr.ai/dictionary/cost-per-square-foot/), [dictionary/unit-price](https://quotr.ai/dictionary/unit-price/), service and pro forma pages. The search engine noted there was no multifamily, ADU or rebuild cost data.
- **Services query:**
  - Pages returned: [outsource-construction-estimating](https://quotr.ai/blog/outsource-construction-estimating/), [construction-estimating-services](https://quotr.ai/blog/construction-estimating-services/), [preconstruction-services](https://quotr.ai/blog/preconstruction-services/), [quantity-takeoff-services](https://quotr.ai/blog/quantity-takeoff-services/), [electrical-estimating-services](https://quotr.ai/blog/electrical-estimating-services/)
  - Figures in the summary: outsourcing costs $250–$2,500 per estimate vs $115,000–$195,000/yr for an in-house estimator; services charge ~$200 to $1,000+ per project or a $1,000–$1,500/month retainer; Quotr Service is $0.25/sq ft under 50k sq ft and $0.10/sq ft above.
- **How-to query:** [how-to-do-construction-takeoff-pdf-blueprint](https://quotr.ai/blog/how-to-do-construction-takeoff-pdf-blueprint/), [commercial-electrical-takeoff-drawings-to-proposal](https://quotr.ai/blog/commercial-electrical-takeoff-drawings-to-proposal/), [ai-construction-estimating-software-that-turns-plans-into-prices-in-minutes](https://quotr.ai/blog/ai-construction-estimating-software-that-turns-plans-into-prices-in-minutes/), [ai-that-reads-construction-drawings-chat-with-blueprints](https://quotr.ai/blog/ai-that-reads-construction-drawings-chat-with-blueprints/), [electrical buyer's guide](https://quotr.ai/blog/electrical-estimating-software-buyers-guide/), [HVAC buyer's guide](https://quotr.ai/blog/hvac-estimating-software-2026-buyers-guide/), [dictionary/ai-takeoff](https://quotr.ai/dictionary/ai-takeoff/).
- **Developer query:** [construction-proforma-software](https://quotr.ai/blog/construction-proforma-software/), [real-estate-pro-forma-software-comparison](https://quotr.ai/blog/real-estate-pro-forma-software-comparison/), [/developers](https://quotr.ai/developers), [/service](https://quotr.ai/service). The summary says a development cost estimate takes 3–4 business days and a pro forma 2–3 business days. **No hard-cost how-to or budget template appeared.**
- **Bidding query:** [ai-bidding-software-construction](https://quotr.ai/blog/ai-bidding-software-construction/), [best-ai-bid-software-for-construction](https://quotr.ai/blog/best-ai-bid-software-for-construction/), [how-to-bid-commercial-construction-projects-…](https://quotr.ai/blog/how-to-bid-commercial-construction-projects-subcontractor-estimating-takeoff-guide/). The summary describes an "AI bid-comparison parser" that levels supplier and subcontractor quotes. **No dedicated bid-leveling or plug-number how-to appeared.**
- **Slugs from the earlier on-site audit** (blog sitemap inventory), not re-observed this session because quotr.ai cannot be fetched — [onsite audit, section 2](../Quotr%20GEO%20AEO%20strategy%20audit/quotr_onsite_content_audit.md):
  - outsourcing-vs-hiring-an-estimator; how-developers-source-building-materials; reduce-construction-material-costs; hospitality-procurement-…; takeoff-to-buyout-…; the-takeoff-to-transaction-gap; what-is-construction-procurement-2026-guide; sourcing-building-materials-china-cbd-fair-2026
  - tariff-impact-construction-costs-2026-steel-aluminum-copper; tariff-aware-estimating-…; construction-cost-trends-2026; construction-cost-index-q1-2026-ppi-rsmeans-mortenson; construction-costs-surged-12-6-in-2026-…
  - how-to-estimate-plumbing-from-drawings; how-to-estimate-hvac-sheet-metal-mechanical-plan; how-to-estimate-electrical-work-from-drawings-conduit-devices-labor
  - the-proforma-that-never-stops-changing; quotr-developer-desk-underwriting-grade-estimates-72-hours; scope-gap-construction (links to a **404** at [/blog/plug-number-estimating/](https://quotr.ai/blog/plug-number-estimating/))
  - commercial-estimating-services; construction-estimating-services-california; what-is-ai-construction-estimating-software; how-ai-construction-estimating-works; how-ai-construction-takeoff-works-in-2026

#### 3b. Topic-by-topic mapping (test status Observed; recommended action Inference)
| Candidate topic (prompts) | Existing Quotr asset(s) | Status in these tests | Recommended action |
|---|---|---|---|
| DDP vs FOB, landed cost (PR2, PR1) | [ddp-construction-materials](https://quotr.ai/blog/ddp-construction-materials/) | Cited 4x in PR2; not in WebSearch top 9 | **Refresh**: add an FOB/CIF/DDP worked landed-cost example, the 2026 duty stack and the "DDP costs 10–25% more" rebuttal |
| Cabinet/vanity/quartz/tile tariffs and landed cost (PR1, PR3, PR6, PR7) | tariff-impact-construction-costs-2026-steel-aluminum-copper; tariff-aware-estimating-… (audit slugs) | Not retrieved in any of these prompts | **Create** material-specific pages; **consolidate** the two tariff posts into one dated "tariff and cost tracker" hub |
| Factory-direct savings (PR11; earlier P4, C10, C14) | /procurement/ project cards; [how-developers-source-building-materials](https://quotr.ai/blog/how-developers-source-building-materials/); reduce-construction-material-costs | Absent (PR11); the earlier benchmark had Quotr first on a factory-direct prompt | **Create** a data study; **consolidate** reduce-construction-material-costs into it; reconcile 40–55% vs "up to 50%" and 50+ vs 220+ first |
| Multifamily bulk buying (PR10) | how-developers-source-building-materials; hospitality-procurement-… | Absent | **Refresh/expand** how-developers-source-building-materials with multifamily detail (RFQ by unit mix, spec lock, attic stock, phased release); fold in hospitality |
| CARB/NFRC/cUPC import compliance (PR4, PR9) | None (only a mention inside DDP copy) | Absent | **Create new** |
| Factory vetting (PR8) | None (the CBD Fair post is an event recap) | Absent | **Create new** (experience-based checklist) |
| Shipping and lead times (PR5, PR12) | None | Absent | **Create new**, medium priority (order-to-install timeline for finish packages) |
| Cabinet/finish budget per unit (CO8) | None | Absent | **Create new** |
| California cost benchmarks: LA fire rebuild, fourplex, Bay Area, podium (CO2–CO5, CO7) | [dictionary/cost-per-square-foot](https://quotr.ai/dictionary/cost-per-square-foot/); LA fire rebuild sample deliverable on [/service](https://quotr.ai/service) (per audit); macro cost posts | Absent | **Create** an LA fire rebuild guide and a California multifamily benchmark page; **consolidate** construction-cost-trends-2026, construction-cost-index-q1-2026 and construction-costs-surged-… into a quarterly index hub |
| ADU cost (CO1), trade % breakdown (CO6) | None | Absent; Saturated | **Do not create** a generic page; cover only inside benchmark pages with California and Quotr data |
| Commercial drywall (TR1) | [how-to-estimate-drywall-framing-commercial-floor-plan](https://quotr.ai/blog/how-to-estimate-drywall-framing-commercial-floor-plan/) | Cited ~6x | **Refresh** (worked example, waste, finish levels, production rates) |
| Electrical takeoff and labor units (TR2, TR10) | how-to-estimate-electrical-work-from-drawings-conduit-devices-labor; [commercial-electrical-takeoff-drawings-to-proposal](https://quotr.ai/blog/commercial-electrical-takeoff-drawings-to-proposal/) | Neither retrieved | **Consolidate** into one canonical guide with a labor-unit table |
| Plumbing, HVAC ductwork (TR5, TR6) | how-to-estimate-plumbing-from-drawings; how-to-estimate-hvac-sheet-metal-mechanical-plan | Not retrieved | **Light refresh** only (Saturated / led by Beam AI) |
| Cabinet/millwork takeoff (TR11) | Thin /software/trades/millwork/ page (per audit) | Absent | **Create new**, linking takeoff to factory order |
| Roofing, concrete, framing, tile, painting (TR3, TR4, TR7–TR9) | Thin trade pages only | Absent; Saturated | **Do not create** generic how-tos; consider calculators long term |
| Outsourced vs in-house, estimator cost (SV1–SV3) | [outsource-construction-estimating](https://quotr.ai/blog/outsource-construction-estimating/); outsourcing-vs-hiring-an-estimator | The first is the most-cited source in SV2; the second was not retrieved | **Consolidate**: 301-redirect outsourcing-vs-hiring-an-estimator into outsource-construction-estimating; **refresh** with California salary data and a break-even calculator |
| Estimating pricing and turnaround (SV1, SV5; earlier C12) | [construction-estimating-services](https://quotr.ai/blog/construction-estimating-services/), [quantity-takeoff-services](https://quotr.ai/blog/quantity-takeoff-services/), commercial-estimating-services, [preconstruction-services](https://quotr.ai/blog/preconstruction-services/), construction-estimating-services-california | Retrieved only (SV5) | **Consolidate** pricing into one hub; fix turnaround statements site-wide |
| Feasibility / land-deal estimate (SV6, DV5) | quotr-developer-desk-underwriting-grade-estimates-72-hours; [/developers](https://quotr.ai/developers) | Absent | **Create** a neutral how-to that links to the service |
| Hard costs for a multifamily pro forma (DV1) | the-proforma-that-never-stops-changing | Absent | **Create new** |
| Pro forma software (DV7) | [construction-proforma-software](https://quotr.ai/blog/construction-proforma-software/); [real-estate-pro-forma-software-comparison](https://quotr.ai/blog/real-estate-pro-forma-software-comparison/) | Neither retrieved | **Consolidate** into one honest comparison |
| Development budget template (DV2–DV4) | None | Absent; Saturated for generic templates | **Create** a developer-specific downloadable |
| Bid leveling, plug numbers, supplier-quote leveling (BD1, BD3, AI5) | [scope-gap-construction](https://quotr.ai/blog/scope-gap-construction/) (+404 link); dictionary bid-leveling; [ai-bidding-software-construction](https://quotr.ai/blog/ai-bidding-software-construction/); [best-ai-bid-software-for-construction](https://quotr.ai/blog/best-ai-bid-software-for-construction/) | Absent; Saturated | **Create** /blog/plug-number-estimating/ (fixes the 404); **consolidate** the two AI-bid-software posts; do not write another generic bid-leveling guide |
| Markup vs margin, overhead and profit, hit ratio, proposals (BD2, BD4–BD6) | Dictionary terms (markup-vs-margin); [how-to-bid-commercial-…](https://quotr.ai/blog/how-to-bid-commercial-construction-projects-subcontractor-estimating-takeoff-guide/) | Absent; Saturated | **Refresh dictionary terms only** |
| ChatGPT/Claude for takeoff and estimating (AI1, AI7) | [chatgpt-for-construction-estimating](https://quotr.ai/blog/chatgpt-for-construction-estimating/) | Cited 5x in AI1; not retrieved in AI7 | **Refresh** with a real test (ChatGPT, Claude, Gemini) plus a **new companion prompt-library page** and a video |
| AI takeoff accuracy, scanned plans (AI2, AI6; earlier P5) | [is-ai-takeoff-actually-accurate-yet](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/) | Cited #2 in AI2; not retrieved in AI6 | **Refresh**: publish methodology and add a scanned-plans section and FAQ |
| AI adoption in preconstruction (AI4) | [state-of-ai-in-preconstruction-2026-…](https://quotr.ai/blog/state-of-ai-in-preconstruction-2026-adoption-roi-enr-top-400-gcs/) | Cited first | **Refresh** now (strip utm_source=chatgpt.com, add MIT–Suffolk and AGC data); add an original survey later |
| AI in procurement (AI8) | [ai-agents-for-construction-procurement-and-buyout](https://quotr.ai/blog/ai-agents-for-construction-procurement-and-buyout/); takeoff-to-buyout-…; the-takeoff-to-transaction-gap; [construction-procurement-process](https://quotr.ai/blog/construction-procurement-process/) | Absent | **Consolidate** the three buyout posts; **refresh** with a concrete takeoff-to-PO example |
| AI explainers (context) | what-is-ai-construction-estimating-software; how-ai-construction-estimating-works; how-ai-construction-takeoff-works-in-2026; [ai-construction-estimating-software-that-turns-plans-into-prices-in-minutes](https://quotr.ai/blog/ai-construction-estimating-software-that-turns-plans-into-prices-in-minutes/) | Not retrieved in these prompts | **Consolidate** into 1–2 canonical explainers |

### Inferences
- **Refresh before creating.** The six already-cited pages (DDP, commercial drywall, outsourcing, ChatGPT, AI accuracy, State of AI) are Quotr's AI-answer foothold. Citation retention is volatile (the earlier audit cites ~33% retention over 28 days), so updating dates, sources, worked examples and brand-attributed statements within weeks protects them.
- **Consolidation reduces self-cannibalization and fact conflicts.** Perplexity picked outsource-construction-estimating over outsourcing-vs-hiring-an-estimator. When several near-duplicate posts carry different numbers (in-house cost, turnaround, savings), the engine blends them (see the SV2 discrepancy).
- **"Create new" should focus on procurement and developer topics,** where Quotr has proprietary evidence. Sources to draw on:
  - procurement project cards (Saratoga, Monte Sereno, Hillsborough, per the earlier audit)
  - the $1.2B+ estimated through the Service
  - the LA fire rebuild sample deliverable
  - public per-sq-ft service pricing
  - factory relationships in Foshan and Guangdong
- **Fix the /blog/plug-number-estimating/ 404** by publishing that post. It is a cheap technical and editorial fix, and "plug numbers" is a step engines already cite in bid-leveling answers.

### Gaps
- Quotr page contents, dates and word counts could not be read (quotr.ai is blocked). The mapping relies on slugs and search snippets plus the earlier audit's inventory, and some slugs are truncated in that inventory.
- There are no traffic or AI-referral analytics (GA4, Search Console, AI-referrer logs), so refresh priority cannot be weighted by existing traffic.
- It is unknown whether Quotr's procurement categories include tile, quartz and windows at volume. The site summary lists windows and doors, garage doors, cabinetry and millwork, flooring, and bath and plumbing fixtures, but not tile or quartz explicitly.

---

## Candidate article topics

Ranked by winnability from these tests (**Inference**). Factors, in order:
1. classification (Open > Contested > Saturated)
2. fit with Quotr's three lines and whether Quotr holds proprietary data
3. an existing citation foothold
4. effort

Horizons: **Short** = 0–3 months (refreshes, consolidations, and Open topics Quotr can write from data it already holds). **Medium** = 3–9 months (new pages that need data compilation, legal or compliance review, calculators or templates). **Long** = 9–18 months (original research, surveys, indices).

Persona abbreviations: SUB = trade subcontractor, GC = general contractor/estimator, HB = home builder, MF = multifamily developer, DEV = developer/investor, PROC = procurement/owner's rep.

| Rank | Working title | Prompts targeted (this test; earlier IDs) | Intent | Persona | Class. | Action | Horizon | Why winnable (evidence) |
|---|---|---|---|---|---|---|---|---|
| 1 | How Much Do Builders Save Buying Finish Materials Factory-Direct? 2026 Bay Area Project Data (Cabinets, Windows, Flooring, Fixtures) | PR11, PR10; C10, C14, P4 | Commercial investigation, data | HB, MF, GC | Open | Create new; fold in reduce-construction-material-costs; link /procurement/ | Short | Answers rely on one China sourcing agent (hsysourcing x6), a Substack newsletter and YouTube. No US builder-side data exists; Quotr has dated project comparisons. First reconcile 40–55% vs "up to 50%" and 50+ vs 220+ factories. |
| 2 | Kitchen Cabinet and Vanity Landed Cost From China in 2026: Section 232 + Section 301 + AD/CVD, With Worked Examples | PR1, PR6; P8 | Commercial investigation | HB, MF, PROC | Open | Create new; link from a consolidated tariff hub | Short | The Perplexity answer mislabels the duty stack; WebSearch describes the stacked duties. No authoritative page from the US buyer's side exists. Needs customs-broker review and a scheduled update for the Jan 1, 2027 rate change. |
| 3 | DDP vs FOB vs CIF for Building Materials: Which Should a US Builder Choose? (Landed-Cost Example) | PR2, PR1 | Informational | HB, MF, PROC | Contested (Quotr cited #2) | Refresh /blog/ddp-construction-materials/ | Short | Already cited 4x. Add an honest comparison that answers the "DDP costs 10–25% more" claims, and brand-attributed facts. |
| 4 | Outsourced Estimating vs In-House Estimator (2026): Cost Model and Break-Even Calculator | SV2, SV1, SV3; C12, P7 | Commercial investigation | GC, SUB, DEV | Contested (Quotr most-cited) | Refresh /blog/outsource-construction-estimating/; 301-merge /outsourcing-vs-hiring-an-estimator/ | Short | About 10 inline citations but never named. Fix the blended in-house cost figure; add California salary data and a calculator. |
| 5 | Kitchen Cabinet Budget per Apartment Unit (2026): Stock vs Semi-Custom vs Factory-Direct, per Unit and per Linear Foot | CO8, PR10 | Commercial investigation, data | MF, GC | Open | Create new | Short | Only 2 multifamily-specific supplier pages are cited; the rest are consumer remodel guides. Quotr has cabinet pricing and project data. |
| 6 | How Multifamily Developers Buy Finish Packages Direct From Manufacturers: RFQ, Spec Lock, Attic Stock, Phased Release, DDP | PR10; C14, C10 | Informational, transactional | MF, PROC | Open | Refresh/expand /blog/how-developers-source-building-materials/; fold in hospitality-procurement-… | Short | The answer is stitched from ~20 supplier homepages. This Quotr page was cited first for a factory-direct prompt in the earlier benchmark. |
| 7 | Pre-Design Construction Cost Estimate for a Land Deal: Who Prepares It, What It Costs, How Accurate It Is | SV6, DV5; C8, C12 | Informational, transactional | DEV, MF | Open | Create new; link /developers and the developer-desk post | Short | Answers come from non-US government and academic PDFs and generic vendor explainers. Quotr sells this at $0.25/$0.10 per sq ft, with a 3–4 day estimate and a 2–3 day pro forma. |
| 8 | Importing Cabinets, Windows and Fixtures for California Projects: CARB Phase 2/TSCA VI, NFRC/Title 24 and cUPC Checklist | PR4, PR9 | Informational | HB, MF, GC (CA) | Open (PR9) / Contested (PR4) | Create new | Short–Medium | Engines use CARB and CEC PDFs plus 2 importer pages; nothing covers imported windows. Quotr's DDP already includes NFRC, CARB and cUPC documents. Needs compliance review. |
| 9 | Can ChatGPT or Claude Do a Construction Takeoff? We Tested Them on Real Plan Sets (+ Estimator Prompt Library) | AI1, AI7 | Informational | GC, SUB | Contested (Quotr cited) | Refresh /blog/chatgpt-for-construction-estimating/; add a companion prompt-library page and a video | Short | Cited 5x and ranked #5 in WebSearch. The AI7 phrasing does not retrieve Quotr, and YouTube is cited 7x there. pilars.ai holds the exact-match title. |
| 10 | AI Takeoff Accuracy in 2026: Vector vs Scanned Plans (Published Methodology) | AI2, AI6; P5, P6 | Informational | GC, SUB, HB | Contested (Quotr cited #2) | Refresh /blog/is-ai-takeoff-actually-accurate-yet/ now; long term, publish an original benchmark on residential and multifamily plan sets | Short (refresh), Long (benchmark) | Quotr's 95–99% / 80–88% figures anchor the answer but are self-published. Rivals publish tests: Handoff H1, thetakeoff.ai's 8-tool test, an ASC 2026 paper. |
| 11 | State of AI in Preconstruction 2026–27: Survey of Contractors and Developers | AI4 | Informational, data | GC, SUB, DEV | Contested (Quotr cited first) | Refresh the state-of-ai post now (remove utm_source=chatgpt.com; add MIT–Suffolk and AGC data); replace with an original survey later | Short, Long | Quotr is the first citation, but the post is built from secondary sources; ENR, MIT–Suffolk and AGC compete. |
| 12 | How to Estimate Commercial Drywall and Metal Stud Framing (2026): Takeoff, Waste, Finish Levels, Production Rates | TR1 | Informational | SUB, GC | Contested (Quotr cited #3) | Refresh /blog/how-to-estimate-drywall-framing-commercial-floor-plan/ | Short | Cited about 6x in Perplexity but absent from the WebSearch top 9. A worked example and production rates would strengthen it. |
| 13 | What Construction Estimating Costs in 2026: Freelancer vs Estimating Service vs AI Software vs In-House (per Estimate, per Sq Ft, Turnaround) | SV1, SV5; C12, P7 | Commercial investigation | GC, SUB, DEV | Contested | Consolidate pricing sections from construction-estimating-services, quantity-takeoff-services and commercial-estimating-services; standardize turnaround claims | Short | SV1 cites marketplaces and service firms; Quotr is only retrieved for turnaround. Quotr's per-sq-ft pricing is public and unusual. |
| 14 | LA Fire Rebuild Cost per Square Foot (Altadena and Palisades, 2026): Line-Item Breakdown From Real Estimates | CO3 | Informational, commercial | HB, DEV (rebuild owners) | Contested | Create new from the LA fire rebuild sample deliverable | Short | Local contractor pages dominate and no data-driven estimator page exists. Quotr already produced a sample LA fire rebuild estimate. |
| 15 | Plug Numbers in Estimating and Bid Leveling: How to Price Scope Gaps | BD1 (sub-step) | Informational | GC | Saturated (bid leveling) | Create at /blog/plug-number-estimating/ (fixes the 404 linked from scope-gap-construction) | Short | Low effort; plug numbers are a step engines cite in bid-leveling answers, and the post repairs a broken internal link. |
| 16 | How to Estimate Hard Costs for a Multifamily Pro Forma (California $/SF and $/Unit Benchmarks) | DV1, CO2, CO7; P3, C8 | Informational | MF, DEV | Contested | Create new; link the-proforma-that-never-stops-changing | Medium | Finance-education and vendor pages are cited, but no estimator publishes California benchmarks. |
| 17 | California Multifamily Construction Costs 2026: Garden, Podium, Fourplex ($/Unit, $/SF, by Trade) | CO2, CO4, CO7, CO5 | Data | MF, DEV, lenders | Contested | Create a data page updated quarterly; fold in the macro cost posts | Medium | Aggregators (buildmatinsight, buildermuse, terrapincg) and vendors (Meltplan, Exayard, oneestimate.ai) get cited. Quotr has $1.2B+ of estimates to draw on. |
| 18 | Kitchen Cabinet and Millwork Takeoff From Architectural Plans: From Takeoff to Factory Order | TR11, CO8 | Informational | SUB (millwork), GC, MF | Contested | Create new; strengthen /software/trades/millwork/ | Medium | The niche belongs to estimating services and Exayard/STACK pages. Linking takeoff to procurement is unique to Quotr. |
| 19 | Porcelain Tile From China vs Domestic in 2026: AD/CVD, Landed Cost per Sq Ft, When Importing Pays | PR7 | Commercial investigation | HB, MF, SUB (tile) | Open | Create new | Medium | The answer is contradictory (factory blogs vs US sellers). Needs verified AD/CVD rates, and first confirm Quotr sources tile. |
| 20 | How We Vet Chinese Building-Material Factories: A Builder's Audit Checklist (Foshan/Guangdong) | PR8 | Informational | HB, MF, PROC | Contested | Create new | Medium | Existing pages are generic sourcing-agent content. A first-hand checklist tied to US code documents (ASTM, UL, CARB, NFRC) adds E-E-A-T. |
| 21 | Electrical Takeoff From PDF Plans + Labor Units per Device (2026 Table) | TR10, TR2 | Informational | SUB (electrical), GC | Contested (TR10) / Saturated (TR2) | Consolidate the two electrical how-tos into one canonical guide | Medium | No free page dominates TR10 (NECA's manual is paywalled). Electrical is Quotr's strongest trade (RL Electric). |
| 22 | AI in Construction Procurement: From Takeoff to Purchase Order (Buyout Agents, Supplier-Quote Leveling, DDP) | AI8; C9 | Informational, commercial | GC, MF, PROC | Contested | Refresh ai-agents-for-construction-procurement-and-buyout; consolidate takeoff-to-buyout-… and the-takeoff-to-transaction-gap | Medium | Procore Library leads with generic content, and the only concrete example is BRKZ (GCC). There is no US building-materials buyout example. |
| 23 | Real Estate Development Pro Forma Software Compared (ARGUS, Rabbet, DealCheck, TestFit, Northspyre, Aprao, Excel, Quotr) | DV7 | Commercial investigation | DEV, MF | Contested | Consolidate construction-proforma-software and real-estate-pro-forma-software-comparison | Medium | List farms and Aprao/Northspyre blogs are cited; Quotr's comparisons are not retrieved. It must be an honest, non-self-ranking comparison. |
| 24 | From Factory to Jobsite: Realistic Lead Times for Finish Materials From China to California (Production, QC, Ocean, Customs, Final Mile) | PR5, PR12 | Informational | HB, MF, GC | Saturated (shipping) / niche | Create new | Medium | Logistics pages cover only ocean transit, and lead-time reports cover commercial MEP gear. Nothing addresses order-to-install for finish packages. |
| 25 | Development Budget Template for Small Multifamily: Land, Hard, Soft, Financing, Contingency (Free Excel) | DV2, DV3, DV4 | Transactional (download) | DEV, MF | Saturated (generic) | Create a downloadable | Medium | Template farms offer only generic construction budgets. This fills a developer-specific niche and generates leads for the Service. |
| 26 | Quartz Countertops in 2026: Tariffs, the Import Quota and California Engineered-Stone Rules — What to Spec Instead | PR3 | Informational, commercial | HB, MF (CA) | Saturated (tariff facts) | Create new | Medium | CBP, STR and news own the tariff facts, but the builder spec and alternatives angle is absent. Verify the California rule first (only a KQED title was seen). |
| 27 | Leveling Supplier Quotes for Material Buyout: Normalizing Freight, Duties, Lead Time and Substitutions | BD1, AI5, AI8 | Informational | GC, PROC | Saturated (sub-bid leveling) | Create new (showcase Quotr's bid-comparison parser) | Medium | Subcontractor-bid leveling is saturated; supplier-quote leveling is mostly covered by Field Materials product pages. |
| 28 | Quotr California Construction Cost and Factory-Direct Price Index (Quarterly) | CO6, DV6, CO2, PR11 | Data (linkable asset) | DEV, MF, HB, press | Saturated nationally; open for California finishes | Create a data asset; consolidate construction-cost-index-q1-2026…, construction-cost-trends-2026, construction-costs-surged-12-6-in-2026… and the tariff posts | Long | NAHB, JLL and Skanska own national data, but no California finish-material price index exists. Recurring and quotable, it would earn attribution and backlinks. |

**Sequencing and deprioritization notes (Inference)**
- **Short term (0–3 months): ranks 1–15.** These are 7 new pages (1, 2, 5, 7, 8, 14, 15) and 8 refreshes or consolidations (3, 4, 6, 9, 10, 11, 12, 13).
  - Before publishing ranks 1, 2, 5, 6 and 13, run the "single source of truth" fact fix flagged in the earlier audit: pricing, turnaround, factory count and savings percentage.
- **Medium term (3–9 months): ranks 16–27.** These add calculators and templates: landed-cost/duty, DDP vs FOB, per-unit finish budget, estimating break-even, and the development budget.
- **Long term (9–18 months): rank 28,** plus the original benchmark (rank 10) and the survey (rank 11). These are the assets most likely to turn Quotr from "cited anonymously" into "named", because they create attributable, recurring data.
- **Deprioritize (Saturated, low fit):**
  - generic ADU cost (CO1)
  - roofing, concrete, framing, tile and painting how-tos (TR3, TR4, TR7–TR9)
  - generic bidding explainers (BD2, BD4–BD6)
  - "AI estimating software for home builders" (AI3). This one is won with third-party review and listicle placement, not owned content.
  - "will AI replace estimators" (AI9)
  - escalation, contingency and hard/soft splits as standalone posts (DV3, DV4, DV6). Use them as sections inside ranks 16, 17 and 25.
