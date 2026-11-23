# Regional / local GEO and SEO strategy for Quotr.ai

**Researched:** 2026-11-23. **Scope:** which regional ("local GEO") plays Quotr.ai should run, how, and which to avoid; URL and template structure; data each page needs; 90-day page count; how AI engines treat location; spam risks.

**Method and limits (read first):**
- Web research was done with WebSearch only. WebFetch was blocked in this session for quotr.ai, developers.google.com and steadydemand.com (DNS not allowed), so **no page was read in full**. Every external finding below comes from search-result summaries of the cited page. Treat exact wording and numbers as "as summarised by search". Re-check quotes from Google's spam-policy page before putting them in a client deck.
- Quotr facts come from the existing vault (`geo-brain/00-quotr/*`, last checked 2026-09-25), not from a fresh read of quotr.ai, because quotr.ai could not be reached from this session.
- Labels used: **[Known]** = stated by a primary or reliable source; **[Likely]** = good evidence but indirect, secondary or partial; **[Speculative]** = my judgment or an untested idea.
- Prior research already covers the national data hub (R-19, proposed URL `/data/`), tariff explainers (R-10, R-12), the LA fire-rebuild cost guide (R-21) and the California cost guide (R-55). This file does not repeat that work. It only adds the regional layer and says which of those items to merge into it.

---

## 1. How do ChatGPT, Perplexity, Google AI Overviews / AI Mode and Gemini handle location in software recommendations?

### Takeaway
AI engines use the user's location mainly for **local-business** questions (maps, "near me", trades and services). There is **no study showing that they localize B2B software recommendations within the US by the user's IP**. Within-US variation seems to come mostly from a **place named in the prompt**, not from where the user is. Recommendations do vary a lot **by country and by language**. Regional **cost** questions ("cost to rebuild in LA", "ADU cost California") are already answered from regional pages, mostly local contractors' pages and news. So Quotr's regional opening is **regional data questions, not "software + state" questions**.

### Cited Findings
**What the engines say about location**
- [Known] ChatGPT search "may use an approximate location based on your IP address to provide relevant local results". Sharing precise device location is optional and off by default. Users get better local results by naming a city, neighbourhood or postal code in the question. A VPN can change the location ChatGPT infers. — [OpenAI Help Center: Searching the web with ChatGPT](https://help.openai.com/en/articles/9237897-chatgpt-search)
- [Likely] Google AI Mode "customizes outputs based on the searcher's location if they have that information", so two users can see different AI Mode results for the same query. — [Whitespark guide to Google AI Mode for local businesses](https://whitespark.ca/guides/whitesparks-guide-to-googles-ai-mode-for-local-businesses/) (a local-SEO firm's guide; I found no official Google document on how AI Mode weights location)
- [Likely] Perplexity's search API supports explicit country and finer location settings. ChatGPT rewrites a question into targeted searches and uses approximate IP location. — secondary article summarised in search results: [IntelligentHQ: Why Australian buyers get different AI answers](https://www.intelligenthq.com/?p=134646)
- [Gap] No source was found on how Gemini (the app) uses location for software or cost answers.

**Local-business behaviour (where location clearly matters)**
- [Likely] In a 36-prompt test, a map of local providers appeared in 12/12 prompts that named a city and in 3/12 prompts with no city. Even "CRM software" produced a map of local providers when the prompt named Munich. The test could not tell whether location came from IP or the prompt. — [Scaile: How ChatGPT surfaces local businesses (50 chats)](https://scaile.tech/blog/fundamentals/mechanics/how-chatgpt-surfaces-local-businesses)
- [Likely] BrightLocal: two runs of the same ChatGPT local search shared only **23%** of businesses (Sept 2026 study). A secondary roundup also says 90% of ChatGPT's local recommendations fall within 287 km of the searcher. — summarised in [Elev8 Operations: AI search statistics 2026](https://www.elev8operations.com/guides/ai-search-statistics-for-local-businesses-2026) and [Steady Demand research index](https://www.steadydemand.com/local-search-ai-industry-research-index/) (the primary BrightLocal pages were not opened)
- [Likely] BrightLocal: Google Maps named the tracked business in 66% of 200,085 localized searches, against 32–38% for AI answers. Use of ChatGPT and other generative AI for local recommendations rose from 6% to 45% in a year (BrightLocal consumer survey 2026). — same roundups as above
- [Known] BrightLocal's ChatGPT-sources study (data collected Nov 2024): business websites were 58% of local sources, business mentions 27%, directories 15%. — [BrightLocal: Uncovering ChatGPT search sources](https://www.brightlocal.com/learn/local-seo/uncovering-chatgpt-search-sources/). BrightLocal's AI directory study found **Yelp** in 80% of ChatGPT local answers — [BrightLocal: AI directory sources](https://www.brightlocal.com/resources/ai-directory-sources/). An August 2026 spot check of 10 San Francisco queries found Yelp in none (sources conflict; small sample).
- [Likely] Whitespark, 540 local queries: AI Overviews showed on 15% of local queries, while the Local Pack showed on 93%. Other sources give 68% and 7.9% for AI Overviews on local searches, so measured rates depend heavily on the query set. — summarised in [Elev8 Operations](https://www.elev8operations.com/guides/ai-search-statistics-for-local-businesses-2026) and [Whitespark AI Mode guide](https://whitespark.ca/guides/whitesparks-guide-to-googles-ai-mode-for-local-businesses/)
- [Likely] Sterling Sky (June 2026, 322 markets): AI local packs showed about 32% as many businesses as traditional 3-packs, with fewer unique businesses in 88% of markets. — summarised in [Elev8 Operations](https://www.elev8operations.com/guides/ai-search-statistics-for-local-businesses-2026)
- [Likely] SOCi: ChatGPT recommended 1.2% of multi-location brands' locations, against 35.9% that appear in the Google local 3-pack. — same roundup

**Software and brand recommendations by country and language**
- [Likely] FTA Global "Context Report": 159 of 206 brands appeared in only one country. A repeated question gave the same top brand only 35% of the time. In **HR software**, none of the top US brands appeared in any other country tested. — [MediaBrief: FTA Global launches Context Report](https://mediabrief.com/fta-global-launches-context-report/)
- [Speculative evidence: single author, small sample] A crypto-card test across 9 countries: ChatGPT named a local product in 35% of non-US answers, Google AI Overviews 25%, Perplexity 3%, Claude 0%. — [HackerNoon](https://hackernoon.com/i-asked-4-ai-engines-about-crypto-cards-from-9-countries-they-know-the-answer-and-wont-say-it)
- [Likely] A Massive report found that crossing a border rarely changed an assistant's opinion of a brand. This partly contradicts the FTA finding: country changes *which* brands are listed more than *how* a brand is described. — [Massive: AI brand visibility](https://www.joinmassive.com/blog/ai-brand-visibility-ai-plays-favorites-it-wont-trash-you)
- [Likely] The query's language changes which brands AI recommends, because the answer is written in that language rather than translated (SEJ coverage of research with 1,650 responses). A Stellarcast study found only 11% overlap between German and English answers on Perplexity, while ChatGPT's German answers varied no more than its normal run-to-run noise. — [Search Engine Journal: Lost in translation](https://searchenginejournal.com/lost-in-translation-how-language-changes-which-brand-ai-recommends/591585); [ContentGrip: Stellarcast](https://www.contentgrip.com/stellarcast-ai-visibility-local-language/)
- [Likely] An arXiv study of exposure to Google AI search found that the query's country of origin explains a meaningful share of the variation. — [arXiv 2602.13415](https://arxiv.org/html/2602.13415v1)

**Do "software + state" queries pull regional pages?**
- [Likely] A web search for state-specific construction estimating software (Texas, Florida, California) returned only national listicles (Capterra, Software Advice with 244 products, G2). No state-specific software pages ranked. — WebSearch, 2026-11-23: [Capterra](https://www.capterra.com/construction-estimating-software/), [Software Advice](https://www.softwareadvice.com/project-management/cost-estimating-software-comparison/)

**Do regional cost questions pull regional pages? (from prior Quotr research)**
- [Known, Perplexity only] "Cost to rebuild a house after the LA fires per sq ft 2026" (T47) cited Bloomberg and local GCs (Benson Construction, Amerbuild, UBIC, Vaisman). California ADU cost questions cite local builder pages (CALI ADU, GreatBuildz). Tariff questions named no software vendor. — `geo-brain/04-prompt-library/tracking-set.md` (T47); `geo-brain/04-prompt-library/buyer-questions-by-trade.md` (developer section); [CALI ADU](https://cali-adu.com/blog/cost-to-build-adu/)

### Inferences
- [Likely] For "best AI takeoff software" a contractor in Dallas and one in Sacramento probably get much the same answer. The user's IP mainly affects local-business answers. A state-level "software" page would be competing for an answer that is not localized anyway.
- [Likely] When a prompt names a place plus software ("estimating software Texas"), engines may switch to local **estimating-service firms** or local maps (the Scaile CRM/Munich pattern) rather than SaaS. That is a weak target for Quotr Software. It is a plausible target for Quotr Service, but Service is delivered remotely, so a city page for it would be a doorway (see §2).
- [Likely] Regional **cost, material-price, tariff-impact and landed-cost** questions differ genuinely by place. AI engines already cite regional pages for them, mostly local contractors and news with thin data. Quotr has proprietary data here (zip-code cost database, procurement quotes, Service estimates). This is the regional white space.
- [Likely] Country and language matter far more than US state for brand lists. Expanding to another country or language means **starting brand visibility from zero** there (see §5).
- [Speculative] Google AI Mode and AI Overviews draw on the regular index and ranking systems (per prior research's note on Google's May 2026 AI-optimization guide). So a strong regional data page that ranks in Google should also feed AI Mode answers for regional cost queries.

### Gaps
- No study measures whether ChatGPT, Perplexity, AI Mode or Gemini change **B2B SaaS** recommendations by **US state** based on user location. This needs Quotr's own test (prompt set in §7).
- Gemini's location handling for informational and software answers was not found.
- Primary BrightLocal, Whitespark and Sterling Sky pages could not be opened. Figures come from secondary roundups.

---

## 2. Google's doorway and scaled-content rules: what makes location pages acceptable vs spam? Who does regional programmatic pages well?

### Takeaway
Google treats near-identical "[service] in [city]" pages that funnel to one destination as **doorway abuse**. It treats mass-produced pages made mainly to rank, whether by AI or by people, as **scaled content abuse**. A location page is acceptable when it holds **data and help that genuinely differ by place** and the site holds only as many such pages as it can back with real data. For a single national SaaS product, "software in [state]" pages are textbook doorways. "[State] construction cost data" pages built on proprietary local numbers are not.

### Cited Findings
- [Known] Google's spam policies list **doorway abuse**: sites or pages created to rank for specific, similar queries that send users to intermediate pages less useful than the final destination. Its listed examples include "having multiple domain names or pages targeted at specific regions or cities that funnel users to one page". (An exact-phrase search matched Google's spam-policy page; the page itself could not be fetched here.) — [Google Search Central: Spam policies](https://developers.google.com/search/docs/essentials/spam-policies); [Google 2015: An update on doorway pages](https://developers.google.com/search/blog/2015/03/an-update-on-doorway-pages)
- [Known] **Scaled content abuse** (introduced March 2024) is defined as generating many pages mainly to manipulate rankings rather than help users. It applies "whether content is produced through automation, human efforts, or some combination". — [Google Search Central blog, March 2024 core update and new spam policies](https://developers.google.com/search/blog/2024/03/core-update-spam-policies); [Spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [Known, via prior Quotr research] Google's May 2026 AI-search guide names "valuable, unique, non-commodity content" as the main factor. It warns that making pages for every variation of a query can break the scaled-content rules. — [Google AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), as recorded in `geo-brain/05-content-strategy/content-priorities.md`
- [Likely] John Mueller told a site owner that about 1,300 city landing pages aimed at "keyword + city" queries would be doorway pages against Google's guidelines. The article dates this to 2019; one vendor dates it to 2023 office hours (date conflict). — [Search Engine Roundtable: City landing pages can be doorway pages](https://www.seroundtable.com/google-city-landing-pages-doorway-pages-28670.html)
- [Gap] No 2025–2026 statement by Mueller or Danny Sullivan specifically about location pages was found. Vendor claims of a "2026 classifier" or "deindexing above 70% templated share" have no Google source and should be ignored. — searched 2026-11-23
- [Likely] Search Engine Land, "Multi-location SEO: how to structure geographic pages at scale": more geographic pages do not mean more visibility. They can cause internal competition, split authority, conflicting local information and maintenance load. Build the fewest pages needed. "The keyword has volume" is not enough reason to publish a page. The real risk is letting "the template become the entire page". — [Search Engine Land](https://searchengineland.com/multi-location-seo-structure-geographic-pages-483959)
- [Likely] BrightLocal suggests more than half of each location page's content should be unique to that location. — [BrightLocal: location pages](https://www.brightlocal.com/learn/local-seo/location-pages/)
- [Likely] Search Engine Journal warns that templated local pages that only swap the city name may face indexing instability. — [SEJ: local SEO for multiple locations](https://www.searchenginejournal.com/local-seo-multiple-locations/370704/)

**Examples of regional cost and location content**
- [Known] RSMeans (Gordian) localizes costs for **more than 930 locations across North America** through City Cost Indexes and Location Factors. The City Cost Index base is a 30-major-city national average set to 100, updated quarterly. Gordian says it spends more than 30,000 hours a year researching local market conditions. — [RSMeans 2026 Square Foot TOC (PDF)](https://www.rsmeans.com/media/wysiwyg/product_pdf/2026-SQFT-TOCs.pdf); [Gordian City Cost Index](https://www.gordian.com/resources/city-cost-index/); [Gordian Q2 2026 Construction Cost Insights (PDF)](https://www.gordian.com/uploads/2026/05/BDC-Gordian-Q2-2026-Construction-Costs-Insights-Report-FINAL.pdf)
- [Known] Fixr cost guides are organised **by project, not by city**. Each gives a national average range first, then itemised and labour/material breakdowns from pricing databases, licensed contractors and experts, with a named author and a last-updated date. No city variants were found. — [Fixr llms.txt](https://fixr.com/llms.txt)
- [Likely] Angi built folders for every US state and city, with each home-services category under them. Its company-list (directory) folder brings in about 35% of organic traffic. These are **directory pages with real local listings**, not cost pages. — [Foundation Inc: Angi "near me" SEO strategy](https://foundationinc.co/lab/angi-near-me-seo-strategy)
- [Likely] Programmatic-SEO practitioners say city pages work only with real local data: actual price range in that city, real job examples, local code requirements. A page that only swaps "Austin" for "Phoenix" is treated as duplicate. (Vendor opinion.) — [The Stacc: programmatic SEO for home services](https://thestacc.com/blog/programmatic-seo-home-services/)
- [Gap] No HomeGuide, ProEst, Buildertrend or Procore regional cost-page case study with traffic or citation results was found. Competitor regional pages (Togal, STACK, Beam, Handoff, Kreo) were not found in search either.

### Inferences
- [Likely] **The acceptable-vs-spam test for Quotr** is three questions per page: (1) Would the numbers and advice change if you swapped the place name? They must. (2) Does the page answer the question in place, rather than funnel to /software/ or /book-demo/? (3) Can Quotr refresh it with its own data at least quarterly? A page that fails any of these should not be published.
- [Likely] The model to copy is **RSMeans-style location factors plus Fixr-style transparency** (dated, authored, method shown), **not Angi-style city folders**. Angi's folders work because each holds a real local directory. Quotr has no local inventory of businesses, only data.
- [Speculative] With 23 trade pages that are already thin (about 25 words of unique text on the drywall page, per prior audit), crossing trades with states (23 × 50 = 1,150 URLs) is the single highest-risk move Quotr could make. Expect it to trigger scaled-content signals site-wide, not just on the new pages.

### Gaps
- Google's full current list of doorway and scaled-content examples could not be quoted verbatim (fetch blocked). Re-check the wording at the spam-policies URL before quoting.
- No case data on how many regional pages a B2B SaaS site can carry before quality signals drop.

---

## 3. What genuinely regional data could Quotr own? Which public datasets can it combine with its own data?

### Takeaway
Quotr's defensible regional data is (a) **its zip-code cost database**, (b) **factory-direct DDP quotes versus local dealer prices** for finish materials, delivered to named metros, and (c) **Service estimates** aggregated by state and metro. Public data (BLS wages, Census permits and establishments, FRED/BLS PPI, USITC trade data, freight indices, tariff proclamations) gives context and credibility. It is commodity on its own, so it must not be the core of any page. Tariffs are set nationally; what varies by region is **port, freight, drayage and local price**, so tariff content should show *impact on regional examples*, not "tariffs in Texas" pages.

### Cited Findings
**Quotr's own regional assets (from the vault, not re-verified)**
- [Known, vault] Quotr Software offers "Quotr's average costs by US zip code" and "a maintained construction estimating database with material, labor, and assembly rates by region" (full database on Plus). Where the regional data comes from and how often it updates is **TO CONFIRM**. — `geo-brain/00-quotr/product-and-features.md` §3.3, citing [quotr.ai/software](https://quotr.ai/software/)
- [Known, vault] Procurement is DDP: factory cost, export packing, ocean freight, US customs and duties, final-mile delivery and certification documents (NFRC, CARB, cUPC). Categories: windows/doors, garage doors, cabinetry/millwork, flooring, bath/plumbing fixtures. Delivery about 90 days. The delivery area is **contradictory on the same page**: "Final-mile delivery to your CA jobsite" vs "any US port or jobsite, coast to coast". — `geo-brain/00-quotr/product-and-features.md` §3.11
- [Known, vault] The only published regional price proof is three Bay Area projects: Myren Dr, Saratoga ($97,000 vs $187K–$218K market); Stratford Ct, Monte Sereno ($108,290 vs $195K–$245K); Skyfarm Dr, Hillsborough ($30,437 vs $58K–$76K). Also an LA fire-rebuild sample deliverable and the FireTips app (Feb 2025). Service claims estimates for "$1.2B+" of projects (unverified). — [quotr.ai/procurement](https://quotr.ai/procurement/), via `geo-brain/00-quotr/entity-fact-sheet.md`

**Tariffs and duties (national, as of late 2026)**
- [Known] On Feb 20, 2026 the Supreme Court ruled 6–3 that IEEPA does not authorise tariffs. Section 301, Section 232 and the 2026 Section 122 surcharge rest on other laws and were not affected. — [Global Trade Alert: From IEEPA to Section 122](https://globaltradealert.org/blog/from-ieepa-to-section-122); [Thomson Reuters: tariff authorities after IEEPA](https://tax.thomsonreuters.com/blog/after-ieepa-which-tariff-authorities-does-the-u-s-government-still-have-and-what-global-manufacturers-need-to-know/)
- [Likely, sources conflict] A temporary Section 122 global surcharge (reported as 10%) applied from about Feb 24 to Jul 24, 2026. One source says the Court of International Trade struck it down on May 7, 2026, with an appeal pending. Legacy China Section 301 rates remain (reported as 7.5%–25%, up to 100% for some goods). One source reports new Section 301 "forced-labor" tariffs since Jul 24 (12.5% for China); single secondary source, verify. — [Tariffs Tool: Section 122 expired July 24](https://www.tariffstool.com/guides/section-122-tariff-rates-2026); [Drip Capital](https://www.dripcapital.com/en-us/resources/blog/supreme-court-tariff-case)
- [Known] Proclamation 11021 (Apr 2, 2026) puts Section 232 duties on the **full value** of steel, aluminium and copper articles and derivatives: 50% for articles made entirely or almost entirely of these metals, 25% for derivatives made substantially of metal. Articles with 15% or less metal content are outside the metals tariffs. Proclamation 11032 (Jun 1, 2026) adjusted the treatment of some derivatives, including systems and components mainly for residential use. — [White House fact sheet, Apr 2026](https://www.whitehouse.gov/fact-sheets/2026/04/fact-sheet-president-donald-j-trump-strengthens-tariffs-on-steel-aluminum-and-copper/); [Federal Register, Proclamation 11021](https://www.federalregister.gov/documents/full_text/html/2026/04/09/2026-06960.html); [EY tax news](https://taxnews.ey.com/news/2026-0788-us-presidential-proclamation-modifies-section-232-tariffs-on-steel-aluminum-copper-and-their-derivative-products)
- [Likely] Kitchen cabinets and vanities: 25% Section 232 since Oct 14, 2025 (Proclamation 10976), rising to 50% on Jan 1, 2027 (Proclamation 11000 delayed the increase). Softwood lumber: 10% Section 232, on top of Canadian countervailing duties of about 14–20%. — [CargoTrans: kitchen cabinet tariffs](https://cargotransinc.com/blog/kitchen-cabinet-vanity-tariffs/); [GEODIS customs corner](https://geodis.com/us-en/resources/customs-corner/us-announces-new-section-232-tariffs-timber-lumber-and-wood-products). An RVIA page claims a rollback; most sources contradict it — [RVIA](https://www.rvia.org/news-insights/section-232-tariffs-wood-products-announced)
- [Known, vault] AD/CVD orders on wooden cabinets and vanities from China have applied since Apr 21, 2020 and were continued after a 2025 sunset review. — [Federal Register AD order](https://www.federalregister.gov/documents/2020/04/21/2020-08544/wooden-cabinets-and-vanities-and-components-thereof-from-the-peoples-republic-of-china-antidumping), via `geo-brain/04-prompt-library/buyer-questions-by-trade.md`

**Material price inflation (national)**
- [Known] AGC: input prices for new nonresidential construction rose **13.3%** year over year (Oct 2025 to Oct 2026), driven largely by fuel and metals. The truck-freight PPI rose 25%. In July, y/y: aluminium mill shapes +40%, steel mill products +22%, copper and brass +18%, lumber and plywood +9.9%. In August the diesel PPI was up 78% y/y. — [AGC Data DIGest, 2026-11-13 (PDF)](https://www.agc.org/sites/default/files/Files/Communications/Economics/datadigest20261113.pdf); [AGC Construction Inflation Alert, Oct 2026 (PDF)](https://www.agc.org/sites/default/files/users/user21902/Construction%20Inflation%20Alert%20Cover%20Oct%202026_v3.pdf)
- [Known] FRED carries material-level PPI series such as gypsum building materials (WPU13710102 and industry series PCU3274203274201), gypsum products (WPU1371) and the Construction Materials special index (WPUSI012011). These are **national** series. — [FRED WPU13710102](https://fred.stlouisfed.org/series/WPU13710102); [FRED PCU3274203274201](https://fred.stlouisfed.org/series/PCU3274203274201); [FRED WPUSI012011](https://fred.stlouisfed.org/graph/?g=1OHcN)

**Freight and ports (what actually varies by region)**
- [Likely] Asia to US West Coast average spot rate was $6,031 per FEU on Jul 16, 2026 (Xeneta). Recent long-term contract rates were $1,915/FEU. A Freightos snapshot of unclear year showed $1,916 to the West Coast vs $3,457 to the East Coast. — [FreightWaves](https://www.freightwaves.com/?p=570387)
- [Known] Descartes' monthly Global Shipping Report gives port-level container import volumes (Los Angeles, Long Beach, NY/NJ, Savannah, Houston). Volumes swing widely month to month; for example, in April 2026 LA was +19.5% and NY/NJ −43.0%. — [Descartes Global Shipping Report, April 2026](https://www.descartes.com/resources/knowledge-center/global-shipping-report-April-2026-container-imports-ease)

**Public regional datasets (for context columns)**
- [Known] Census Building Permits Survey: state, metro and county permit counts, monthly and annual. — [Census BPS state chart (PDF)](https://www.census.gov/construction/bps/pdf/state_chart.pdf); [NAHB permits by state and metro](https://www.nahb.org/News-and-Economics/Housing-Economics/State-and-Local-Data/Building-Permits-by-State-and-Metro-Area)
- [Known] County Business Patterns: establishments by NAICS (e.g., 238 specialty trades) by state and county. Current counts were not retrieved. Historical only: the 2002 Economic Census had 43,204 NAICS 238 establishments in CA, 27,279 in FL and 23,519 in TX. — [Census CBP](https://www.census.gov/programs-surveys/cbp.html); [2002 Economic Census, TX](https://webarchive.library.unt.edu/eot2008/20080916223918/http:/www.census.gov/econ/census02/data/tx/TX000_23.HTM)
- [Known] BLS: specialty-trade-contractor industry data (NAICS 238), with QCEW establishment counts through Q1 2026. OEWS publishes state and metro wages by occupation. — [BLS NAICS 238](https://www.bls.gov/iag/tgs/iag238.htm); [BLS OEWS](https://www.bls.gov/oes/)

### Inferences
**Regional data ideas, ranked (my judgment)**

| Rank | Data asset | Varies by region? | Quotr-owned? | Verdict |
|---|---|---|---|---|
| 1 | **Factory-direct (DDP) vs local dealer price** for cabinets, vanities, LVP, porcelain tile, interior doors, windows, fixtures, delivered to named metros | Yes: dealer prices, freight leg and drayage differ by metro | **Yes** (procurement quotes plus dealer quotes Quotr collects) | **Run** (core moat). Gated on the delivery-area answer. |
| 2 | **State and metro unit-cost tables** for 8–10 trades (material, labour, installed) from the zip-code database and Service estimates | Yes | **Yes**, if the database is Quotr's own and not licensed (TO CONFIRM) | **Run** |
| 3 | **Landed cost by US gateway** (LA/LB, Oakland, Seattle–Tacoma, Houston, Savannah, NY/NJ): transit days from South China, freight, port and drayage costs, worked DDP example | Yes: West vs East/Gulf Coast freight and transit differ | Partly: Quotr's shipments plus public freight indices | **Run as one hub**; split into per-port pages only with real shipments |
| 4 | **Labour cost by state** (BLS OEWS for carpenters, drywall installers, electricians, plumbers, roofers, tile setters, HVAC) | Yes | No (public) | **Context column only**. Commodity alone. |
| 5 | **Permit and code differences that change material choice and cost** (e.g., California energy code and CARB rules for composite wood; Florida wind-zone product approvals for windows and doors) | Yes | Partly (Quotr's certification know-how) | **Run inside state pages.** Needs expert review. |
| 6 | **Construction activity** (Census permits, CBP establishments, QCEW employment) | Yes | No | **Context only** |
| 7 | **Tariff/duty impact by material** | **No** (national rates) | No | **One national tracker** (R-10/R-12). State pages show the impact on local examples and link to it. |
| 8 | **National PPI trends** (FRED/BLS) | No (national) | No | **Context only** |
| 9 | **Imports by customs district** of HTS chapters for cabinets, tile, vinyl flooring and windows (USITC DataWeb / Census USA Trade Online) | Yes | No, but unusual and citable | **Speculative add-on** for the ports hub |

- [Likely] Tariff pages split by state would be doorways in all but name: same rates, place name swapped. Regional value comes from the freight leg, dealer markup and code rules.
- [Speculative] The **zip-code database** is Quotr's most scalable regional asset. If it is Quotr's own data, state pages can publish aggregated medians with sample sizes. If it is licensed (for example from RSMeans or similar), publishing it may breach the licence and would also be commodity. Confirming this is the first gating question.

### Gaps
- Source, coverage, licence and refresh cadence of Quotr's zip-code cost database: **TO CONFIRM with Quotr**.
- Whether Procurement delivers outside California: **TO CONFIRM**. This gates every non-California factory-direct comparison.
- Which US ports Quotr's shipments actually use, and how many shipments and quotes exist per metro.
- Current CBP counts of NAICS 238 establishments by state (not retrieved; pull from the Census API).
- Florida product-approval and California CARB/Title 24 specifics were **not verified in this session**. They need expert-reviewed sources before publication.
- No public **regional** material-price index was found (BLS PPI is national). This confirms the gap Quotr could fill, but it also means its index can't be cross-checked against a public one.

---

## 4. Trade × region matrix: which trades and which states and metros first?

### Takeaway
Start with **California, Texas and Florida**, then **North Carolina, Georgia and Arizona**. Those six led US housing permits in 2025. California also has all of Quotr's proof, and Texas has its strongest event tie (Dallas Build Expo). Cover trades as **rows in a table on each state page**, not as separate URLs. Put first the trades where Quotr has both software and procurement relevance: **cabinets, flooring (LVP and tile), windows and doors, plumbing fixtures**. Then add **drywall, roofing, electrical, HVAC and plumbing labour**.

### Cited Findings
- [Known] 2025 total permitted housing units (Census): **Texas 210,217 (1st); Florida 178,297; California 103,856; North Carolina 86,167; Georgia 61,196; Arizona 51,532**. US total 1,431,616. — [Census BPS state chart (PDF)](https://www.census.gov/construction/bps/pdf/state_chart.pdf); [Census annual highlights (PDF)](https://www.census.gov/construction/bps/pdf/annual_highlights.pdf)
- [Known] 2025 single-family permits: Texas led with 140,002 (−11.7% vs 2024). Florida (2nd) fell 10.3% and North Carolina (3rd) fell 6.9%. US single-family: 909,280. — [NAHB Eye on Housing, Mar 2026](https://eyeonhousing.org/2026/03/single-family-permits-end-2025-on-a-soft-note/)
- [Likely] Multifamily: Texas had the most permits. Over the first ten months of 2025, Florida rose 27.8% and California 19.8%, and the top ten states issued 60.2% of multifamily permits. — same NAHB series
- [Known, vault] Quotr attended IBS 2026, **Dallas Build Expo 2026 (Booth #277)**, RE:Forge SF, NHCA Build the Builder, **PCBC 2026** (California) and CBD Fair 2026. Its memberships include BIA Bay Area. — `geo-brain/00-quotr/entity-fact-sheet.md`
- [Known, vault] Quotr has 23 national trade pages under /software/trades/. Several are thin (drywall about 25 words of unique text). — `geo-brain/05-content-strategy/content-priorities.md`
- [Gap] Current state counts of specialty-trade contractors (CBP NAICS 238) were not retrieved, and no Dodge or ABC/AGC state rankings were found.

### Inferences
**Recommended state order (my judgment)**

| Wave | State | Why | Lead metros for tables |
|---|---|---|---|
| 1 | **California** | All Quotr proof (Bay Area procurement projects, LA fire rebuild, "California estimating services" post); confirmed delivery area; HQ; PCBC; BIA Bay Area | SF Bay Area, Los Angeles, Sacramento, San Diego |
| 1 | **Texas** | #1 in permits (total, single-family and multifamily); Dallas Build Expo; Gulf port (Houston) | Dallas–Fort Worth, Houston, Austin, San Antonio |
| 1 | **Florida** | #2 in permits; multifamily rising; distinctive wind-code product rules affect imported windows and doors | Miami, Tampa, Orlando, Jacksonville |
| 2 | North Carolina | #4 in permits | Charlotte, Raleigh–Durham |
| 2 | Georgia | #5; Savannah port | Atlanta, Savannah |
| 2 | Arizona | #6; West Coast port logistics | Phoenix, Tucson |

- [Speculative] Texas and Florida pages should go out **without** factory-direct comparisons if Procurement is California-only, saying "available in California; contact us for other states". Otherwise the page makes an offer Quotr can't fill.

**Trade columns on each state page (8 required, up to 10)**
1. Cabinets ($/linear ft, factory-direct DDP vs dealer)
2. Flooring: LVP and porcelain tile ($/sq ft material and installed)
3. Windows ($/unit by type) and exterior/interior doors
4. Plumbing fixtures and vanities ($/fixture)
5. Drywall ($/sq ft hung, taped, finished)
6. Roofing ($/square: asphalt shingle; tile/metal where common, e.g., FL and AZ)
7. Electrical ($/point, $/sq ft rough-in)
8. HVAC ($/ton installed)
9. (optional) Framing ($/sq ft)
10. (optional) Painting ($/sq ft)

Each cell shows Quotr median, low–high range, sample size (n), date window, and the BLS OEWS median wage for the related occupation in that state.

### Gaps
- Which trades and states hold the most Quotr users and Service jobs (internal data). That should override permit rankings if it differs.
- Regional demand for estimating software itself (search volume by state) was not measurable in this session.

---

## 5. International and Spanish: hreflang for Canada, Australia or UK? Spanish content for US Hispanic contractors?

### Takeaway
**Do not** build Canada, Australia or UK versions or hreflang now. Quotr's cost database is US zip-code based, Procurement is US customs and DDP only, and brand lists are country-specific. Buildxact (Australia) and Kreo (UK) already hold those home markets. A **small, conditional Spanish (es-US) pilot** is worth considering, because Hispanic workers are about a third of the US construction labour force and AI answers in Spanish name different brands. Run it only if Quotr can support Spanish-speaking buyers (sales, onboarding, ideally the user interface).

### Cited Findings
- [Known] Hispanic workers were **32.8%** of the US construction labour force in 2024, against 19.9% across all industries (NAHB analysis of federal data). — [NAHB Eye on Housing, Oct 2026](https://eyeonhousing.org/2026/10/nearly-one-in-three-construction-workers-are-hispanic/). CPWR: 34% in 2023, up from 16.5% in 2000 — [Hispanic Construction Council 2025 report](https://simplebooklet.com/2025hispanicconstructioncouncilreport?textonly=1) and CPWR data as summarised. BLS: 30.0% in 2020 — [BLS Spotlight](https://www.bls.gov/spotlight/2022/the-construction-industry-labor-force-2003-to-2020/home.htm)
- [Known] BLS notes that 2025 annual CPS estimates were affected because the October 2025 survey was not collected during the federal shutdown. — [BLS CPS table 18c](https://www.bls.gov/cps/cpsaat18c.htm)
- [Likely] Competitors are adding Spanish. eSUB launched a Spanish option in its mobile apps, citing rising client requests (and a vendor claim that 75% of foreign-language speakers on jobsites speak Spanish). Projul advertises a full Spanish interface. Procore has an in-app language setting and machine-learning support for Spanish, French and Portuguese drawings. — [eSUB press release](https://prnewswire.com/news-releases/esub-construction-software-launches-spanish-option-301864674.html); [Projul en español](https://projul.com/features/projul-en-espanol/); [Procore: languages](https://support.procore.com/faq/what-languages-are-available-in-procore); [Procore: multilingual ML for drawings](https://www.procore.com/en-gb/whats-new/multilingual-ml-support-for-pdm-drawings)
- [Likely] Language changes which brands AI recommends: answers are composed in the query's language, not translated. On Perplexity, German and English answers overlapped only 11%. — [SEJ](https://searchenginejournal.com/lost-in-translation-how-language-changes-which-brand-ai-recommends/591585); [ContentGrip](https://www.contentgrip.com/stellarcast-ai-visibility-local-language/)
- [Likely] Country-level brand sets barely overlap (159 of 206 brands appeared in only one country; top US HR-software brands appeared nowhere else). — [MediaBrief/FTA Global](https://mediabrief.com/fta-global-launches-context-report/)
- [Likely] Buildxact runs country sections (/au/, /uk/) and expanded to Canada in 2019. No evidence was found on how it implements hreflang. — [Buildxact AU news](https://www.buildxact.com/au/category/news/page/4/); [Buildxact expands to Canada](https://www.buildxact.com/au/2019/05)
- [Known] Google: subdirectories on a gTLD (e.g., example.com/es/) are easy to set up and maintain. Use hreflang to declare language and region versions. Google "may not crawl, index, or rank all content" on locale-adaptive pages that change content by perceived country or language. — [Google: managing multi-regional and multilingual sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites); [Google: localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Known, vault] Quotr's database is "average costs by US zip code". Procurement handles "US customs". — `geo-brain/00-quotr/product-and-features.md`

### Inferences
- [Likely] **Canada, Australia, UK: avoid in the next 90 days.** There is no local cost data, no DDP route, no local proof, and entrenched local brands. hreflang without a localized offer only creates duplicate English pages.
- [Speculative] **Spanish pilot (gated):** 3 es-US pages at most: (1) AI takeoff and estimating for contractors (software page equivalent), (2) buying finish materials factory-direct with DDP, (3) 2026 tariffs on building materials, a short explainer linking to the English tracker. Requirements: written or reviewed by a fluent construction-literate editor, not machine-translated at scale; a Spanish demo or contact path; hreflang es-US ↔ en-US with x-default English. Success measure: Quotr named in Spanish prompts (§7) within 60 days of publishing.
- [Likely] The buyer is the **owner or estimator**, not the field worker. Workforce share overstates the buyer opportunity. The share of Hispanic-**owned** contracting firms is the better sizing metric (gap).
- [Speculative] Mass machine translation of the site is a scaled-content risk. I recall that Google's scaled-content examples mention automated transformations such as translation, but I could not verify the wording in this session.

### Gaps
- Does the Quotr app, onboarding or support work in Spanish? (TO CONFIRM)
- Share and count of Hispanic-owned construction firms and their software adoption (CPWR's Dec 2024 bulletin on business ownership exists, but figures were not retrieved).
- Spanish-language search and prompt volume for construction-software terms.

---

## 6. Local entity signals: Google Business Profile, associations, local press. Which earn citations?

### Takeaway
**Skip Google Business Profile.** An online-only SaaS is not eligible, and GBP mainly feeds local-pack and maps answers Quotr doesn't compete in. The regional entity signals that matter are **crawlable mentions on regional third-party sites**: association member directories and newsletters (HBAs, AGC/ABC chapters), regional business journals and trade press. Ideally these cite Quotr's regional data.

### Cited Findings
- [Known] Google Business Profile requires in-person contact with customers during stated hours. Online-only businesses are listed as ineligible. Service-area businesses must travel to customers, and virtual offices don't count unless staffed. — [Google: Business eligibility and ownership guidelines](https://support.google.com/business/answer/13763036); [Google: Guidelines for representing your business](https://support.google.com/business/answer/3038177)
- [Likely] Whitespark's 2026 local ranking-factors survey found three of the top five AI-search visibility factors were citation (third-party mention) factors. This is for local businesses; transfer to SaaS is an inference. — summarised in [Steady Demand research index](https://www.steadydemand.com/local-search-ai-industry-research-index/)
- [Known] NAHB's federation has more than 700 state and local home builders associations (its directories page says 600+). — [NAHB: About](https://www.nahb.org/Why-NAHB/About-NAHB/About-NAHB); [NAHB associations directory](https://www.nahb.org/nahb-community/nahb-directories/associations-directory)
- [Known] AGC has 87 chartered chapters (its FAQ says 89). — [AGC chapters](https://www.agc.org/connect/chapters); [AGC membership FAQ](https://agc.org/connect/join/agc-membership-faq)
- [Gap] ABC chapter count not found.
- [Known, vault] Quotr already lists BIA Bay Area and Modular Building Institute memberships (old "quotr-io" slugs). It attended Dallas Build Expo and PCBC. A paid EIN Presswire release about the LA FireTips app exists. No earned trade-press coverage was found. — `geo-brain/00-quotr/entity-fact-sheet.md`
- [Known, vault] On Perplexity, the LA-rebuild cost answer cites Bloomberg and local GCs. That shows regional news and local business pages are the sources cited for regional cost questions. — `geo-brain/04-prompt-library/tracking-set.md` (T47)

### Inferences
- [Likely] **Do:** (1) Fix the BIA Bay Area and MBI listings to "Quotr.ai" and link quotr.ai. (2) Join one builder association per wave-1 state as an associate member and get the directory listing: BIA Bay Area (have), one Texas HBA (Dallas, as the Build Expo tie) or the Texas Association of Builders, and one Florida association (Florida Home Builders Association or a local HBA). (3) Pitch each state page's data to that state's association newsletter and to a regional business journal ("Factory-direct finishes cut X% off a Bay Area custom-home budget; here is the data"). (4) Speak at or sponsor one chapter event per wave-1 state. Event pages and recaps are crawlable third-party mentions.
- [Likely] **Don't:** create a GBP, a service-area profile for "procurement delivery", or listings on Yelp-type local directories. They are ineligible or irrelevant for B2B SaaS. If a staffed office with customer visits exists, a GBP is technically possible but still low value. (Office status: TO CONFIRM; the vault has a San Francisco vs Berkeley HQ conflict that must be resolved before any NAP-type listing.)
- [Speculative] Association directories are low-authority individually. Their value is consistent entity facts (name, URL, category) across many sites, plus occasional data citations in newsletters, which AI engines do crawl.

### Gaps
- Which specific chapters' directories and newsletters are indexed and cited by Perplexity, ChatGPT or AI Mode (test with the prompt set).
- Membership costs and the lead time for associate membership listings.

---

## 7. Which regional prompts should be added to Quotr's tracking set?

### Takeaway
Add about **24 regional prompts** to the tracking set (in `geo-brain/04-prompt-library/tracking-set.md`), in five groups. Run each **twice**: once with no location, and once with the engine's location set to the named state. That shows both whether Quotr is cited and whether engines localize software answers at all. Today the only regional prompt tracked is T47 (LA fire rebuild).

### Cited Findings
- [Known] ChatGPT uses approximate IP location, and naming a city or postal code improves local results. — [OpenAI Help Center](https://help.openai.com/en/articles/9237897-chatgpt-search)
- [Likely] Perplexity's API supports country and location parameters. — [IntelligentHQ](https://www.intelligenthq.com/?p=134646)
- [Known] Advanced Web Ranking supports custom-location tracking of AI Overviews. — [AWR help: AI Overviews custom location tracking](https://www.advancedwebranking.com/help/ai-overviews-custom-location-tracking)
- [Likely] ChatGPT local answers repeat only about 23% of the time, so a single run is unreliable. — BrightLocal via [Elev8 Operations](https://www.elev8operations.com/guides/ai-search-statistics-for-local-businesses-2026)
- [Known, vault] The existing tracking set holds T47 ("how much does it cost to rebuild a house after the LA fires per square foot 2026"), Quotr absent. — `geo-brain/04-prompt-library/tracking-set.md`

### Inferences
**Proposed regional prompt set (IDs suggested as RG-01 to RG-24)**

*A. Does the engine localize software? (tests §1; Quotr Software)*
- RG-01 best construction estimating software for contractors in Texas
- RG-02 best AI takeoff software for roofing contractors in Florida
- RG-03 construction takeoff and estimating software for California subcontractors 2026
- RG-04 estimating software that uses local material prices by zip code

*B. Regional cost questions (state and metro pages)*
- RG-05 how much does drywall cost per square foot installed in Texas in 2026
- RG-06 cost per square foot to build a house in Florida in 2026
- RG-07 kitchen cabinet cost per linear foot in the San Francisco Bay Area 2026
- RG-08 LVP flooring installed cost per square foot in Phoenix 2026
- RG-09 construction material prices in Florida 2026
- RG-10 construction labor rates California vs Texas 2026
- RG-11 how much does it cost to build an ADU in Los Angeles in 2026 (pairs with T47)

*C. Factory-direct, ports and landed cost (procurement)*
- RG-12 landed cost of importing kitchen cabinets from China to Houston
- RG-13 how long does it take to ship building materials from China to Los Angeles
- RG-14 which US port is cheapest for importing building materials from China
- RG-15 where can Bay Area builders buy cabinets and windows factory direct
- RG-16 DDP building materials delivered to a jobsite in Texas
- RG-17 can I import windows from China for a house in Florida (hurricane code approval)

*D. Regional tariff impact*
- RG-18 how are 2026 tariffs affecting home building costs in Texas
- RG-19 tariff impact on construction material costs in California 2026

*E. Spanish (only if the pilot runs)*
- RG-20 mejor software de estimación de construcción con IA
- RG-21 software para cuantificar planos de construcción (takeoff)
- RG-22 comprar gabinetes y ventanas directo de fábrica en China con entrega DDP en Estados Unidos
- RG-23 aranceles 2026 en materiales de construcción importados de China
- RG-24 cuánto cuesta construir una casa por pie cuadrado en Texas 2026

**How to run** [Speculative protocol]: run monthly on ChatGPT (search on), Perplexity (Sonar, with `user_location` set to the state for the "located" run), Google AI Mode and AI Overviews (signed out, location set through a rank tracker such as AWR), and Gemini. Run 3 times per prompt per condition because of variance. Log whether Quotr is named, whether quotr.ai is cited, which regional sources are cited (local GCs, news, associations, government), and whether the answer is local-business-style (map or local firms) or vendor-style. Group A answers "do we ever need state software pages?". If located runs of RG-01 to RG-04 return the same national vendors as non-located runs, the answer is no.

### Gaps
- Baselines for ChatGPT, AI Mode and Gemini don't exist yet for any Quotr prompt (prior tests were Perplexity only).

---

## 8. Recommended regional plan: plays to run and avoid, URL structure, page template, 90-day page count, risks

### Takeaway
Run a **data-led regional layer of 12 URLs in 90 days** (9 committed plus 3 gated on data), plus an optional 3-page Spanish pilot, for a **hard cap of 15**. These are "construction cost data" pages for 6 states, 2–3 metros where Quotr has real projects, and a landed-cost-by-port hub. All sit under the planned `/data/` hub. Do **not** publish "software in [state]", "estimating services in [city]" or trade × city pages, and don't create a Google Business Profile. Each regional page must carry Quotr-only numbers with sample sizes, dates and a method, or it doesn't ship.

### Cited Findings
- Google's doorway examples include pages for regions or cities that funnel users to one page. Scaled content abuse covers mass pages made mainly to rank, by AI or by people. — [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- Build the fewest geographic pages needed. Keyword volume alone is no reason to publish one. — [Search Engine Land](https://searchengineland.com/multi-location-seo-structure-geographic-pages-483959)
- Make more than half of each location page unique. — [BrightLocal](https://www.brightlocal.com/learn/local-seo/location-pages/)
- Primary-data pages earned 3.3× more AI citations per page than other pages in a 1,075-citation study. — [Growth Memo](https://www.growth-memo.com/p/why-most-original-data-never-gets), via `reports/Quotr GEO AEO strategy audit.md`
- Prior audit: "Do less of … '[trade] estimating services' or city-by-city variations". — `reports/Quotr GEO AEO strategy audit.md`
- Prior roadmap already plans R-19 (data hub, `/data/`), R-21 (LA fire rebuild, Dec 2026), R-55 (California residential costs, Mar 2027), R-10 and R-12 (tariffs). — `geo-brain/05-content-strategy/content-roadmap.md`
- Everything else here draws on §1–§7.

### Inferences

#### 8.1 Plays to RUN (in priority order)
| # | Play | What | Confidence it's worth it |
|---|---|---|---|
| R1 | **State cost-data pages** | 6 states (CA, TX, FL, then NC, GA, AZ). Unit-cost tables for 8–10 trades × 3–4 metros from Quotr data, plus labour, permit and code context. | [Likely] high: regional cost answers currently cite thin local pages |
| R2 | **Metro factory-direct vs dealer pages** | Only where Quotr has real projects: SF Bay Area now. Los Angeles = **make R-21 this page** (don't build two). One TX metro only if the data threshold is met. | [Likely] high: unique proof, white space |
| R3 | **Landed cost by US gateway (hub)** | One page: a table of 5–6 gateways, transit days from Nansha/Yantian/Shekou, current freight index, drayage to 2–3 metros each, a worked DDP example. Calculator later. | [Likely] medium–high: tariff and import answers cite no vendor today |
| R4 | **Regional prompt tracking** | RG-01 to RG-24, located vs non-located | [Known need] |
| R5 | **Regional earned signals** | One association per wave-1 state, newsletter and business-journal data pitches, fixed listings | [Likely] medium |
| R6 | **Spanish pilot (gated)** | 3 es-US pages with hreflang, only with Spanish support | [Speculative] |

#### 8.2 Plays to AVOID
| # | Avoid | Why |
|---|---|---|
| A1 | `/construction-estimating-software/{state}/`, "AI takeoff software in Texas" | The product is identical everywhere, so the page funnels to one destination: Google's doorway example. No evidence engines localize SaaS by state. |
| A2 | "{Trade} estimating services in {city}" (expanding the existing "California estimating services" post pattern) | Service is remote; this is the city-page doorway pattern; the prior audit already says stop |
| A3 | Trade × state or trade × city URL matrix (23 trades × 50 states = 1,150 pages), AI-generated | Scaled content abuse; site-wide quality risk; Quotr can't refresh it |
| A4 | Separate "tariffs in {state}" pages | Tariff rates are national; only the place name would change |
| A5 | Google Business Profile, service-area profiles, Yelp-style listings | Ineligible (online-only) or irrelevant |
| A6 | Canada, Australia or UK hreflang or ccTLDs; IP-based locale-adaptive content | No local offer or data; Google may not crawl locale-adaptive content |
| A7 | Pages built only from public data (BLS, Census, PPI) or republished RSMeans figures | Commodity; RSMeans is licensed data |
| A8 | Machine-translating the site into Spanish | Quality and scaled-content risk; brand answers in Spanish need native content |

#### 8.3 URL structure
```
/data/                                      ← national data hub (R-19, already planned)
/data/costs/                                ← "Construction costs by state": US map + table of all 50 states
                                              (states without a page appear as a table row only, not a URL)
/data/costs/{state}/                        ← e.g. /data/costs/texas/
/data/costs/{state}/{metro}/                ← gated; e.g. /data/costs/california/san-francisco-bay-area/
                                                         /data/costs/california/los-angeles/  (= R-21)
/data/landed-cost/                          ← US gateway hub + worked DDP examples (+ calculator later)
/data/landed-cost/{gateway}/                ← gated on real shipments; e.g. /data/landed-cost/los-angeles-long-beach/
/data/tariffs/ (or the R-12 URL)            ← ONE national tracker; state pages link here, never copy it
/es/...                                     ← Spanish pilot only; hreflang es-US ↔ en-US, x-default = English
```
- Trade pages (`/software/trades/{trade}/`) link to the matching state-table rows (anchors such as `/data/costs/texas/#drywall`). They don't spawn state children.
- Breadcrumbs: Data › Construction costs › Texas › Dallas–Fort Worth.
- Canonical: self-referencing. No near-duplicate siblings. If two metros' tables come out nearly identical, merge them into the state page.

#### 8.4 Page template: state cost-data page (required fields)
**Publish gate (all must be true) [Speculative thresholds, set by me]:**
1. Quotr has its own (not licensed) cost data for at least 8 trades in at least 3 metros of the state, dated within 12 months, with n shown.
2. At least one real anonymized worked example from that state (Service estimate or procurement quote).
3. At least 50% of the page (tables plus text) differs from every sibling state page.
4. A named estimator reviewer, and an expert reviewer for code and tariff lines.
If a state fails the gate, it stays a **row** on `/data/costs/`, not a page.

| # | Section / field | Content and data source | Refresh |
|---|---|---|---|
| 1 | Title / H1 | "{State} construction costs 2026: material, labor and installed prices by trade" | yearly |
| 2 | Byline + dates | Named author and estimator-reviewer; "Data as of {month YYYY}"; `dateModified` changed **only** when data changes | quarterly |
| 3 | Answer-first summary (40–60 words) | 3 headline numbers (e.g., median $/sq ft drywall installed in DFW; cabinet $/LF factory-direct vs dealer; state cost index vs US = 100) | quarterly |
| 4 | **State and metro cost index** | Quotr zip-code database aggregated to the state and 3–4 metros, indexed to the Quotr US median = 100; method linked | quarterly |
| 5 | **Trade unit-cost table** (8–10 trades × metros) | Material, labour and installed; low / median / high; **n**; date window. Source: Quotr database plus Service estimates | quarterly |
| 6 | **Labour table** | BLS OEWS state and metro median hourly wage for SOC 47-2031 carpenters, 47-2081 drywall, 47-2111 electricians, 47-2152 plumbers, 47-2181 roofers, 47-2044 tile setters, 49-9021 HVAC; vs US | yearly (OEWS release) |
| 7 | **Factory-direct vs local dealer** (if Procurement serves the state) | 5–7 finish items: DDP delivered price vs median of local dealer quotes (n, dates, how collected), plus "when local supply wins" (lumber, urgent items) | quarterly |
| 8 | **Logistics route** | Nearest gateway(s), ocean transit days, typical door-to-door lead time (about 90 days, TO CONFIRM), drayage range; link to `/data/landed-cost/` | quarterly |
| 9 | **Tariff impact on local examples** | One worked line, e.g., "a $X cabinet package for a Houston spec home: duty layers (Section 232 25% → 50% from Jan 1, 2027; AD/CVD where applicable) = $Y"; link to the national tracker, rates not restated in full | on each tariff change |
| 10 | **Codes and permits that change cost** | State-specific items that affect material choice (e.g., CA energy code and CARB composite-wood rules; FL wind-zone product approvals for windows and doors). Expert-reviewed, with primary sources | yearly |
| 11 | **Market context** | Census BPS permits (state total, single- vs multifamily, top permit metros); CBP NAICS 238 establishments; QCEW construction employment | yearly / quarterly |
| 12 | **Worked example** | One anonymized real project from the state: scope, takeoff quantities, priced estimate, procurement savings | per new project |
| 13 | FAQ (4–6) | Drawn from the RG prompts for that state | quarterly |
| 14 | Method, sources, limits | How medians are computed, sample sizes, exclusions, licence; revision log | each update |
| 15 | Download + embed | CSV of the tables (CC-BY with attribution link); chart embed code (link earning) | each update |
| 16 | Schema | `Dataset` (name, description, `spatialCoverage` Place for state or metro, `temporalCoverage`, `variableMeasured`, `measurementTechnique`, `creator` Organization, `license`, `distribution` DataDownload CSV) + `WebPage` (`dateModified`, `author`, `reviewedBy`) + `BreadcrumbList`; optional `FAQPage` | each update |
| 17 | Conversion (secondary) | "Price your own plans with your zip code" (Software trial) and "Get a DDP quote" (Procurement) blocks below the data, never instead of it | — |

**Metro page** = same template, narrower: at least 5 real procurement quotes or at least 10 Service estimates in the metro within 12 months [Speculative threshold]; adds neighbourhood or project-type examples (custom home, ADU, multifamily) and a named local case study.

**Landed-cost hub fields:** gateway table (LA/LB, Oakland, Seattle–Tacoma, Houston, Savannah, NY/NJ) × [ocean transit days from South China; latest spot and contract freight from a named index with date; port and terminal fees; drayage $ to 2–3 metros; typical customs-exam and dwell risk; states typically served]; one worked DDP vs FOB example per gateway (e.g., a 40-ft container of cabinets or LVP); Incoterms explainer link; tariff tracker link; optional USITC DataWeb chart of imports by customs district for HTS chapters relevant to cabinets, tile, vinyl flooring and windows [Speculative add-on].

#### 8.5 How many pages in 90 days, and when
| Window | New regional URLs | Notes |
|---|---|---|
| Days 1–30 | 4: `/data/costs/` hub, `/data/costs/california/`, `/data/costs/texas/`, `/data/costs/florida/` | Before day 1, settle three gates: database ownership; Procurement delivery area; HQ fact. **R-55 is folded into the California page.** |
| Days 31–60 | 4: `/data/costs/california/san-francisco-bay-area/`, `/data/costs/california/los-angeles/` (**= R-21**, LA fire rebuild), `/data/landed-cost/` hub, `/data/costs/north-carolina/` | Bay Area page uses the 3 published projects plus new ones. Fix the "~$0 saved" display bug first. |
| Days 61–90 | 1 committed + 3 gated: `/data/costs/georgia/` (committed), then gated: `/data/costs/arizona/`, one Texas metro (DFW or Houston), one gateway page (LA/LB or Oakland) | Gated items ship only if they pass the publish gate |
| Optional | 3 Spanish pilot pages | Only with Spanish sales and onboarding support |
| **Total** | **9 committed + 3 gated = 12; with Spanish, hard cap 15** | Prior roadmap pace is 7–12 pieces a month; this adds about 3–4 a month, offset by merging R-21 and R-55 |

- [Speculative] Why 12 and not 50 or 500: each page needs real Quotr data and a quarterly refresh. Quotr's published regional proof today is three Bay Area projects. A small team can maintain about 12 data pages; more would go stale, and stale dated data is worse than none for AI citation and trust.

#### 8.6 Risks and mitigations
| Risk | Level | Mitigation |
|---|---|---|
| Doorway classification | High if A1–A3 are built; low for R1–R3 | Publish gate; answer in place; no funnel-only pages; merge near-duplicates |
| Scaled content abuse (AI-written state pages) | High if pages are templated prose | Tables from real data; human-written analysis per state; cap of 15 |
| Stale or wrong numbers quoted by AI | Medium–high (tariffs changed several times in 2026: IEEPA struck down Feb 20; Section 122 in and out; metals rules changed Apr 2 and Jun 1) | "As of" dates on every rate; tariff facts kept on one national page; update log; expert review |
| Offer mismatch (factory-direct shown where Quotr can't deliver) | High until the delivery area is confirmed | Gate section 7 of the template on delivery-area confirmation |
| Data licence breach (if the database is licensed) | Unknown | Confirm ownership; publish only Quotr-derived aggregates |
| Inconsistent entity facts (HQ SF vs Berkeley; 50+ vs 220+ factories; savings ranges) | High: it spreads onto every regional page | Pull facts from one canonical fact sheet; fix before launch |
| Over-reading local-search studies | Medium | Those studies are about local businesses, not SaaS. Validate with the RG prompt set before expanding. |

### Gaps
- All three launch gates (database ownership, delivery area, HQ) need Quotr's answers. The plan's size depends on them.
- No competitor benchmark exists for regional data pages in construction SaaS (no Togal, STACK, Beam, Handoff or Kreo regional pages found), so there is no outside proof of the citation lift. Treat the first wave as an experiment, measured with RG-05 to RG-19.
- The exact current Section 301 and Section 122 status should be re-verified against USTR, CBP CSMS and the Federal Register on the day each page is published.
