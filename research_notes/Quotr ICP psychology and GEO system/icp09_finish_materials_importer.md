# ICP 9 — The factory-direct finish-materials buyer (China sourcing) for Quotr Procurement

*Research conditions (read first): researched 2026-11-06. 11 web searches were run before the shared WebSearch budget ran out. WebFetch could not reach any site tried (cargotransinc.com, rvia.org, freightfigures.com, greenworldwide.com, federalregister.gov), and the network proxy also refuses old.reddit.com and youtube.com. So every web fact below comes from search-result summaries, not opened pages. Where a summary gave a figure, it is cited to the result URLs, and any conflict between sources is noted. Facts on Quotr and earlier AI tests come from the repo (geo-brain/ and the research_notes audit), which links its own sources. Anything marked **(unverified — training knowledge)** was not checked in this session and must be verified before publishing. Anything marked **SIMULATED** or **estimate** is not observed data. Method: the uploaded ICP-depth GEO framework (trigger → stage → mode → restraining force → prompt → proof), applied to trade and customs compliance instead of health regulation.*

---

## A. Definition and size

### Takeaway
ICP 9 is the person who signs or steers the purchase of a finish package (windows, doors, cabinets, vanities, flooring, tile, quartz, plumbing fixtures, lighting) and is weighing a factory-direct import from China against a domestic dealer. Their budget authority runs from about $30K (one custom home) to $500K+ (multifamily or hospitality). This session could not size the import flows or count the buyers, because search ran out before USITC or Census pulls. The only hard size anchors found are Quotr's own project values, a competitor's minimum order size, and national per-home tariff-cost estimates.

### Cited Findings
**Buyer sub-types (the definition)**
| Sub-type | Role / title | Typical ticket (evidence) | Fit with Quotr Procurement |
|---|---|---|---|
| 9a. Developer / homebuilder procurement lead | Project manager or purchasing manager at a for-sale or build-to-rent developer | Quotr's three Bay Area project cards: $30,437, $97,000 and $108,290 of materials against "market" ranges of $58K–$76K, $187K–$218K and $195K–$245K ([/procurement/](https://quotr.ai/procurement/), via [product-and-features.md](../../geo-brain/00-quotr/product-and-features.md)) | Core. All three published proofs are single addresses in Saratoga, Monte Sereno and Hillsborough |
| 9b. Multifamily developer / purchaser | Development manager, owner's rep | Port2Site targets 50–500+ unit multifamily, BTR and student housing, and recommends 50+ units or $50K+ of materials ([port2site.com/direct-import](https://www.port2site.com/direct-import), via [procurement-and-sourcing.md](../../geo-brain/03-market/competitors/procurement-and-sourcing.md)) | Contested by Port2Site and Wirko (see I) |
| 9c. Hospitality FF&E/OS&E purchaser | Purchasing agent, owner's rep | No sizing found. Quotr has one post, "hospitality-procurement-consolidated-sourcing" (2026-07-21) ([website-audit.md](../../geo-brain/02-current-state/website-audit.md)) | Peripheral today |
| 9d. Supply-and-install contractor | Window/door, cabinet, flooring or tile sub that buys material and installs it | No sizing found | Strong fit with Quotr Software (Plus plan includes "10% off procurement") ([product-and-features.md](../../geo-brain/00-quotr/product-and-features.md)) |
| 9e. Owner-builder | High-net-worth owner building one custom home or rebuild | Quotr's "Residential LA Fire Rebuilding" sample deliverable suggests rebuild demand ([product-and-features.md](../../geo-brain/00-quotr/product-and-features.md)) | Fits the Bay Area card sizes |

**Size anchors found**
- Tariff cost per new home: $7,500–$10,900 (Joint Economic Committee, April 2026). Brookings: about $30B added cost, about 90% of it on new construction ([JEC](https://www.jec.senate.gov/public/_cache/files/fe5d79b2-97cb-4c55-aeba-3e31fdd235fd/april-2026-final-jec-report-on-housing.pdf); [Brookings](https://www.brookings.edu/articles/recent-tariffs-threaten-residential-construction/), via [white-space.md](../../geo-brain/03-market/white-space.md)).
- Import flows are contracting: ceramic tile imports fell 25% and vinyl flooring imports 16% in November (reported February 2026; vinyl dollars down 10% year on year) ([Floor Daily](https://www.floordaily.net/flooring-news/ceramic-imports-declined-25-in-november-vinyl-imports-down-16)).
- Contractor behaviour (AGC, January 2026 survey): 40% raised bid prices because of tariffs, 35% passed most or all tariff costs to owners, 32% bought early. Input costs rose 8.9% from August 2025 to August 2026 ([AGC Jan 2026](https://www.agc.org/news/2026/01/14/construction-costs-rise-fastest-rate-january-2023-november-outpacing-increases-contractors-bid); [AGC Sep 2026](https://www.agc.org/news/2026/09/10/construction-input-costs-climb-89-between-august-2025-and-august-2026-association-survey-finds-war), via Perplexity in [buyer-questions-by-trade.md](../../geo-brain/04-prompt-library/buyer-questions-by-trade.md)).
- Lumber and plywood prices were up 9.9% year on year by July 2026 ([AGC](https://www.agc.org/news/2026/08/13/construction-input-costs-climb-71-percent-between-july-2025-and-july-2026-impacts-war-and-tariffs), via [prompt-library.md](../../geo-brain/04-prompt-library/prompt-library.md)).

**HTS headings to pull from USITC DataWeb (HS 2022/2026; verify each 10-digit line at [hts.usitc.gov](https://hts.usitc.gov/))**
| Category | Heading(s) | Verified in-session? |
|---|---|---|
| Quartz surface products | 6810.99.0020, 6810.99.0040, 7020.00.6000 | Yes: Section 201 coverage ([Mondaq](https://www.mondaq.com/unitedstates/international-trade-investment/1829966/new-section-201-safeguard-tariffs-on-quartz-surface-products)) |
| Aluminum doors, windows, frames | 7610.10 | Yes: listed under Annex I-A ([Aluminum Extruders Council](https://aluminumextruderscouncil.blogspot.com/2026/05/section-232-update-focus-on-aluminum.html)) |
| Vinyl / SPC / LVP flooring | 3918.10.10 (rigid core lines .20/.30), 3918.10.20 | Yes ([Wove LVP from CN](https://tariffs.wove.com/us/tariff/3918.10.10.20/luxury-rigid-core-vinyl-plank-tile/from/CN)) |
| Kitchen cabinets, vanities | Section 232 heading 9903.76.03; underlying 9403.40 / 9403.60 | 9903.76.03 yes ([search summary of Section 232 wood sources](https://www.strtrade.com/trade-news-resources/tariff-actions-resources/section-232-tariff-timber-lumber)); underlying codes **(unverified — training knowledge)** |
| Ceramic/porcelain tile 6907; plastic windows 3925.20; wood doors 4418; faucets 8481.80; sanitaryware 6910; lighting 9405 | — | **(unverified — training knowledge)** |

### Inferences
- Quotr's published proof cluster is a custom-home or small-project buyer ($30K–$110K of materials per address), which sits below Port2Site's stated 50-unit / $50K floor. The size segment that is "too small for container importers, too big for big-box" is Quotr's natural slot.
- With the AGC finding that 35% of contractors pass tariffs to owners, the economic buyer is usually the owner or developer even when a contractor places the order. Content should speak to both the payer and the purchaser.
- Falling ceramic and vinyl import volumes in late 2025 are consistent with buyers pausing or switching origin, not with demand disappearing. That fits a "window of dissatisfaction" market.

### Gaps
- No 2024–2026 import values by category and country (China, Vietnam, Malaysia, Mexico) were retrieved. Pull the DataWeb series for the headings above, 2023–2026 YTD.
- No count of developers, builders or hospitality purchasers. Pull from Census County Business Patterns for NAICS 236115/236116/236117/236118 and from NAHB and AHLA membership.
- No per-unit finish-package benchmarks for multifamily or hotel keys were found. Quotr's three cards are the only figures, and their project type and date are not stated.

---

## B. Tariff and trade status as of November 2026 (the dominant trigger)

### Takeaway
As of 2026-11-06 the stack on a Chinese finish import is **MFN duty + legacy Section 301 list duty (often 25%) + either the new 12.5% Section 301 "forced-labor" duty (non-232 goods) or a Section 232 duty (cabinets/vanities 25%, aluminum windows/doors 50% on full value) + any AD/CVD + (quartz) a Section 201 safeguard of 25–50%**.

The IEEPA tariffs are gone: the Supreme Court struck them down on 2026-02-20 and they were terminated on 02-24. Their 10% Section 122 replacement expired on 07-24 and was itself replaced the same day by the forced-labor Section 301 duty. The next hard dates are:
- **Nov 10, 2026:** 178 Section 301 exclusions lapse (extension unconfirmed).
- **Jan 1, 2027:** cabinets and vanities go from 25% to 50%; upholstered wood furniture to 30%.
- **Jan 10, 2027:** the extended US–China "Busan" truce expires.

Chinese-origin wooden cabinets (China-wide AD rate 251.64%) and quartz (AD ~295–337%) are effectively priced out unless the exporter holds a low separate rate.

### Cited Findings
**Legal status timeline**
| Date | Event | Source |
|---|---|---|
| 2020-04-21 | AD/CVD orders on wooden cabinets and vanities from China; continued in 2025 | [FR 2020](https://www.federalregister.gov/documents/2020/04/21/2020-08544/wooden-cabinets-and-vanities-and-components-thereof-from-the-peoples-republic-of-china-antidumping); [FR 2025 continuation](https://www.federalregister.gov/documents/2025/09/17/2025-17986/wooden-cabinets-and-vanities-and-components-thereof-from-the-peoples-republic-of-china-continuation) (via repo glossary) |
| 2024-07 | Commerce final anti-circumvention ruling: cabinets and vanities completed in **Vietnam** from Chinese components are covered by the China orders. No comparable final ruling for Malaysia was found | [ASL Law](https://aslgate.com/united-states-issues-final-conclusion-on-scope-review-and-anti-circumvention-investigation-of-vietnamese-wooden-cabinets/); [KCMA](https://kcma.org/insights/kcma-applauds-positive-step-forward-commerce-unfairly-traded-cabinet-imports-malaysia-and) |
| 2025-01 | AD/CVD orders on quartz surface products from China continued after a five-year review | [FR](https://www.federalregister.gov/documents/2025/01/30/2025-01946/certain-quartz-surface-products-from-the-peoples-republic-of-china-continuation-of-antidumping-and) |
| 2025-05-22 | AD/CVD petitions filed on hardwood and decorative plywood from China, Indonesia and Vietnam (a cabinet-box input) | [Faegre Drinker](https://www.faegredrinker.com/en/insights/publications/2025/5/new-antidumping-duty-and-countervailing-duty-petitions-of-hardwood-and-decorative-plywood-from-indonesia-china-and-vietnam); [FR initiation](https://www.federalregister.gov/documents/2025/06/16/2025-11075/hardwood-and-decorative-plywood-from-the-peoples-republic-of-china-indonesia-the-socialist-republic) |
| 2025-10-14 | Section 232 timber/lumber derivatives in force: cabinets and vanities 25% (heading 9903.76.03); softwood lumber and upholstered wood furniture also covered | [Wiley](https://www.wiley.law/alert-White-House-Imposes-Section-232-Tariffs-on-Imports-of-Timber-Lumber-and-their-Derivative-Products); [STR](https://www.strtrade.com/trade-news-resources/tariff-actions-resources/section-232-tariff-timber-lumber); [Thompson Hine](https://www.thompsonhinesmartrade.com/2026/01/president-trump-delays-section-232-tariff-increase-on-wood-furniture-cabinets-and-vanities/) |
| 2025-12-31 | Proclamation amending Proclamation 10976 **postponed the Jan 1, 2026 step-ups**: cabinets/vanities stay 25% (not 50%) and upholstered furniture stays 25% (not 30%) through Dec 31, 2026; new step-up date Jan 1, 2027 | [Green Worldwide](https://www.greenworldwide.com/section-232-wood-products-tariffs-remain-unchanged-through-2026/); [Allyn](https://www.allynintl.com/en/news-publications/entry/update-section-232-tariffs-on-kitchen-cabinets-vanities-and-furniture); [CargoTrans](https://cargotransinc.com/blog/kitchen-cabinet-vanity-tariffs/). Conflict: an [RVIA 2026-01-05 note](https://www.rvia.org/news-insights/section-232-tariffs-wood-products-announced) calls it a "rollback"; treat "deferral" as correct |
| 2026-02-20 | *Learning Resources, Inc. v. Trump*, 6–3 (Roberts): IEEPA does not authorize tariffs. Refunds left to the lower courts | [A&O Shearman](https://www.aoshearman.com/en/insights/scotus-rejects-ieepa-tariffs-refund-opportunities-and-uncertainty-emerge); [Miller Chevalier](https://www.millerchevalier.com/publication/supreme-court-finds-ieepa-tariffs-unlawful-what-you-need-know); [Norton Rose](https://www.nortonrosefulbright.com/en/knowledge/publications/20f2de87/potential-refunds-us-supreme-court-overturns-ieepa-tariffs) |
| 2026-02-24 | All IEEPA-based tariffs (fentanyl, reciprocal) terminated at 12:00 a.m. ET; Section 122 used as a bridge | [White & Case](https://www.whitecase.com/insight-alert/united-states-terminates-ieepa-based-tariffs-following-supreme-court-decision) |
| 2026-03-04 / 03-31 | CIT ordered refunds on unliquidated entries; Judge Eaton then continued a stay after CBP's declaration. Refunds run through CBP's CAPE system. Amounts conflict: $35.46B across ~8.3M entries vs "$166B+" vs Wharton's up to $175B | [A&O Shearman](https://www.aoshearman.com/en/insights/scotus-rejects-ieepa-tariffs-refund-opportunities-and-uncertainty-emerge); [Wharton](https://budgetmodel.wharton.upenn.edu/p/2026-02-20-supreme-court-tariff-ruling/); [Endless Commerce](https://endlesscommerce.com/playbook/supreme-court-ieepa-tariff-ruling-refunds/) |
| 2026-03-11 | USTR opened Section 301 investigations into structural excess capacity: 21 sectors, 16+ economies including Vietnam. Outcome pending | [GingerControl](https://gingercontrol.com/blog/vietnam-vs-china-import-tariff); [Helen of Troy 10-Q](https://www.sec.gov/Archives/edgar/data/0000916789/000091678926000138/hele-20260831.htm) |
| 2026-04-02 (eff. 04-06) | Section 232 steel/aluminum/copper restructured: duty on **full customs value**; Annex I-A 50%, Annex I-B 25%; goods ≤15% metal by weight drop out; no stacking across metals | [Thompson Coburn](https://www.thompsoncoburn.com/insights/74-april-2-2026-new-proclamation-makes-major-revisions-to-section-232-tariffs-on-steel-aluminum-copper/); [Cassidy Levy](https://www.cassidylevy.com/news/modified-full-value-section-232-metal-tariffs-announced/); [C.H. Robinson](https://www.chrobinson.com/ko-kr/resources/insights-and-advisories/client-advisories/2026q2/04-06-2026-us-expands-n-increases-sec232-tariffs-on-aluminum-steel-n-copper-effective-apr-6/). Conflict: one [EY summary](https://taxnews.ey.com/news/2026-0788) says 25% applies |
| 2026-04-23 | Cabinets AD review 2023–24 final: KM Cabinetry 43.92%, Ancientree 7.67%, separate-rate firms 10.02%, **China-wide 251.64%** | [Federal Register](https://www.federalregister.gov/documents/2026/04/23/2026-07866/wooden-cabinet-and-vanities-and-components-thereof-from-the-peoples-republic-of-china-final-results) (search summary) |
| 2026-05-07 | CIT ruled the Section 122 tariffs exceeded presidential authority; relief only for the named plaintiffs | [Z2Data](https://www.z2data.com/insights/how-the-termination-of-section-122-tariffs-impacts-your-supply-chain/) (search summary) |
| 2026-07-24 | Section 122 (10%) expired after 150 days. **Section 301 forced-labor tariffs** took effect on 60 economies: 10% for those committing to forced-labor import bans, **12.5% for China** | [EY](https://taxnews.ey.com/news/2026-1607-ustr-finalizes-section-301-forced-labor-tariffs-on-60-economies-additional-tariffs-of-10-percent-or-125-percent-take-effect-24-july-2026); [RVIA](https://www.rvia.org/news-insights/section-122-tariffs-replaced-new-section-301-forced-labor-tariffs); [Carter's 10-Q](https://www.sec.gov/Archives/edgar/data/0001060822/000106082226000127/cri-20261003.htm) |
| 2026-07-31 (eff. 08-15) | **Section 201 quartz safeguard**, a 4-year tariff-rate quota. In-quota 25/23/21/19%; over-quota 50/49/48/47%. Year-1 quota 13.0M m² (~140M sq ft), allocated 25% per quarter. Stacks on AD/CVD and Section 301. New headings 9903.45.30/.31. China, India, Vietnam, Turkey, Malaysia, Spain, Italy and Portugal not excluded. (USITC had recommended 25% in-quota / 40% over-quota) | [Mondaq](https://www.mondaq.com/unitedstates/international-trade-investment/1829966/new-section-201-safeguard-tariffs-on-quartz-surface-products); [Stone World](https://www.stoneworld.com/articles/95779-trump-imposes-four-year-tariff-rate-quota-on-imported-quartz-surface-products); [USITC](https://www.usitc.gov/press_room/news_release/2026/er0505_68542.htm); [customsandinternationaltradelaw.com](https://customsandinternationaltradelaw.com/2026/08/10/new-section-201-safeguard-tariffs-on-quartz-surface-products/) |
| 2026-09-23/27 | Bessent announced the "Busan Agreement" truce extended from **Nov 10, 2026 to Jan 10, 2027**. It keeps current suspensions in place and cuts no rates. One source says the White House had not formally documented it | [CNBC](https://www.cnbc.com/2026/09/24/us-china-trade-truce-bessent-trump-xi.html); [NBC](https://www.nbcnews.com/business/economy/us-china-extend-trade-truce-trump-rcna599525); [TariffsTool](https://www.tariffstool.com/guides/us-china-trade-truce-extended-january-2027) |
| 2026-11-09 / 11-10 | Port-fee suspension and BIS Affiliates Rule suspension reportedly expire Nov 9. **178 remaining Section 301 exclusions lapse Nov 10 unless USTR extends them; no extension announced** as of the sources | [Thomson Reuters](https://tax.thomsonreuters.com/blog/section-301-exclusions-expiration/); [FreightFigures](https://www.freightfigures.com/articles/us-china-truce-extended-january-10-2027-november-10-exclusions-port-fees-excess-capacity-importer-playbook) |
| 2027-01-01 | Scheduled: cabinets/vanities 232 rises to 50%; upholstered furniture to 30% | [TC Wholesale Cabinetry](https://tcwholesalecabinetry.com/blog/cabinet-tariffs-2026-2027); [Cabinex](https://cabinexwholesale.com/blogs/navigating-25-section-232-tariff-kitchen-cabinets-2027-increase) |

**Stacking rules found**
- Goods paying a Section 232 duty are exempt from the forced-labor Section 301 duty via heading 9903.05.90; wood products are on that list. Legacy Section 301 China list duties **do** stack on Section 232 goods. No source explicitly confirmed that cabinet HTS lines are on the 9903.05.90 list ([HTS Hero](https://htshero.com/blog/us-tariff-stacking-rules); [Strix](https://strixsmart.com/resources/blog/tariff-stacking-guide-2026); [US Tariff Rates China](https://ustariffrates.com/tariff-rates/china), search summary; the specific page was not isolated).
- A 2026 retailer tracker headlines "Kitchen Cabinet Tariffs 2026: 319.81% Duty From China" and lists AD 251.64% (since 2026-04-23) and CVD 18.17% (since 2025-06-22, after a court ruling), checked October 2026 ([ChinaHomeSource](https://www.chinahomesource.com/us/tariffs/kitchen-cabinets/)).

**Per-category stack for China origin, Nov 2026**
| Category | MFN | Legacy 301 | Forced-labor 301 (12.5%) | Section 232 | AD/CVD | Other | Indicative total, China origin |
|---|---|---|---|---|---|---|---|
| Wood kitchen cabinets / vanities | ~0 **(unverified)** | 25% (implied by tracker) | Exempt (232 good) | 25% → **50% on 2027-01-01** | AD 251.64% China-wide (7.67–43.92% for reviewed firms, 10.02% separate rate) + CVD 18.17% | — | **319.81%** China-wide ([ChinaHomeSource](https://www.chinahomesource.com/us/tariffs/kitchen-cabinets/)); **~78% for a 10.02% separate-rate exporter** (inference: 25+25+10.02+18.17, assuming the 18.17% CVD applies); +25 points on Jan 1, 2027 |
| Quartz slabs/countertops | **(unverified)** | **(unverified)** | **(unverified)** whether 201 goods are exempt | — | AD 295.02–336.69% (USITC final) or 265.81–336.69% (trade summary), plus CVD | 201 TRQ 25% in-quota / 50% over-quota | Effectively prohibitive for China origin ([USITC pub 5578](https://www.usitc.gov/sites/default/files/publications/701_731/pub5578.pdf); [Prosperous America](https://prosperousamerica.org/american-quartz-industry-prevails-against-illegal-dumping-by-india-china-and-turkey/)) |
| LVP/SPC flooring (3918.10) | 5.3% | 25% | 12.5% (replaced Section 122's 10%) | — | No SPC AD/CVD order found | — | **~42.8%** (inference from [Wove](https://tariffs.wove.com/us/tariff/3918.10.10.20/luxury-rigid-core-vinyl-plank-tile/from/CN) + forced-labor rate; stacking of the two 301 actions **(likely, not confirmed)**) |
| Aluminum windows/doors (7610.10) | **(unverified)** | **(unverified)** | Exempt (232 good) | **50% on full value** (Annex I-A, per an industry post) | AD/CVD order on aluminum extrusions from China since 2011-05-26 remains active (2024–25 review under way). Whether finished glazed windows are in scope is **(unverified)** | — | High; ≥50% before legacy 301 and AD/CVD ([AEC](https://aluminumextruderscouncil.blogspot.com/2026/05/section-232-update-focus-on-aluminum.html); [FR 2011](https://www.govinfo.gov/content/pkg/FR-2011-05-26/pdf/2011-13103.pdf); [USITC pub 5375](https://usitc.gov/publications/701_731/pub5375.pdf)) |
| Engineered wood flooring | — | — | — | — | Separate AD case | — | "Most Chinese companies are paying duties of at least 67%" with Section 301 ([Floor Daily](https://www.floordaily.net/flooring-news/antidumping-duties-on-engineered-wood-to-be-published-dec-31)) |
| Ceramic/porcelain tile; faucets; sanitaryware; lighting; uPVC windows; interior wood doors | **(unverified)** | **(unverified)** | 12.5% if not 232/201 goods (inference) | — | none found in-session | — | Not computed: pull HTS Chapter 99 lines |

**Alternative origins**
- **Vietnam:** conflicting. Two sources put Vietnam at the 12.5% forced-labor rate (a 10-Q says the change was "an increase of 2.5%" for China, Vietnam and Thailand). GingerControl says Vietnam has no Section 301 exposure, which is likely stale ([Helen of Troy 10-Q](https://www.sec.gov/Archives/edgar/data/0000916789/000091678926000138/hele-20260831.htm); [US Tariff Rates Vietnam](https://ustariffrates.com/tariff-rates/vietnam); [GingerControl](https://gingercontrol.com/blog/importing-from-vietnam-tariff-guide)). Vietnamese cabinets made from Chinese parts are covered by the China AD/CVD orders ([ASL](https://aslgate.com/united-states-issues-final-conclusion-on-scope-review-and-anti-circumvention-investigation-of-vietnamese-wooden-cabinets/)).
- **Malaysia:** sources disagree on whether any cabinet circumvention order exists ([Wirko](https://www.wirkobuildingsolutions.com/insights/2026-cabinet-tariff-map/); [KCMA](https://kcma.org/insights/kcma-applauds-positive-step-forward-commerce-unfairly-traded-cabinet-imports-malaysia-and)).
- **Mexico:** not researched; status of USMCA goods under the forced-labor 301 is unknown.
- **Transshipment:** if CBP finds goods were transshipped (Chinese goods routed via Vietnam without substantial transformation), China's Section 301 rates plus penalties apply ([GingerControl](https://gingercontrol.com/blog/vietnam-vs-china-import-tariff)).

**How DDP pricing and landed cost respond (mechanics)**
- Landed cost = product + packing + freight + insurance + duties/tariffs + customs fees + inland delivery ([repo glossary](../../geo-brain/04-prompt-library/construction-glossary.md)). Importing guides put landed cost at 1.3–1.7× FOB, but the exact source page was not isolated ([prompt-library L-112](../../geo-brain/04-prompt-library/prompt-library.md)).
- Importing guides warn newcomers about DDP when antidumping duties apply ([SinoEuro Ruida](https://www.snrida.com/blog/complete-guide-importing-building-materials-china), via repo).
- Under Incoterms 2020, DDP delivery happens on the arriving vehicle "ready for unloading". Unloading is normally the buyer's job ([repo glossary template](../../geo-brain/06-playbooks/templates/glossary-entry.md); [ICC](https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/)).

### Inferences
- **DDP flips tariff risk from buyer to seller.** Between quote date and entry date, any rate change (for example the Jan 1, 2027 cabinet step-up) either eats Quotr's margin or forces a repricing clause. Buyers will ask "is the duty locked?" That is the single most important DDP proof point for late 2026. The quote needs three dates: the quote date, the rate date and the entry window.
- **AD/CVD retroactivity is the hidden DDP liability.** AD cash deposits are provisional; final assessment after an administrative review can be higher, years later, and falls on the importer of record (mechanics **(likely — training knowledge)**). If Quotr is importer of record under DDP, it carries that tail. This is a credibility advantage if disclosed and a solvency risk if not.
- **IEEPA refunds go to the importer of record, not to a DDP customer.** Any DDP buyer who paid IEEPA-inflated prices in 2025 has no direct refund claim. Expect "who gets the refund?" questions; a plain policy statement answers them.
- **China-only cabinets are structurally disadvantaged in 2027.** Vietnam- or Malaysia-made cabinets that are not circumventing pay Section 232 only: 25%, then 50%. Chinese cabinets add legacy 301 plus AD/CVD. Quotr needs to know and disclose each cabinet exporter's AD status. The framed-series cabinet line is the most exposed product Quotr sells.
- **Chinese quartz is effectively closed.** Do not market Chinese quartz.
- **Lower-stack categories are where China DDP can still undercut Bay Area dealers:** LVP/SPC (~43% stack), plus probably tile, plumbing fixtures, lighting and non-aluminum doors (to be verified). Aluminum windows face 50% on full value plus 301.
- Tariff volatility itself is the search trigger. The three-month cadence of 2026 (Feb, Apr, Jul, Aug, Sep, Nov, then Jan) means a dated, monthly-refreshed tracker will always have a fresh hook.

### Gaps
- Exact legacy Section 301 list rates for 9403, 6907, 8481, 6910, 9405, 3925 and 7610; whether the 178 exclusions (expiring Nov 10) include any finish-material lines.
- CVD rates for cabinets by company; current quartz CVD rates; whether finished windows fall in the aluminum-extrusion AD/CVD scope.
- Whether Section 201 quartz goods are exempt from the forced-labor 301 duty.
- Status of the Section 301 excess-capacity action and its sector list.
- Exact text of the 2025-12-31 proclamation and the UK/EU/Japan caps on 232 wood duties: one table showed "15% all-in", country unclear.
- None of the primary documents (Federal Register, USTR, CBP CSMS) could be opened; every rate above must be re-verified by a licensed customs broker before publication.

---

## C. Geography

### Takeaway
Finish savings matter most where dealer and installer pricing is highest and project values are large. Quotr's only proof is Bay Area custom homes, so the defensible geo strategy is one California hub plus one Bay Area spoke now. Add an LA rebuild spoke and a Florida impact-window page only if Quotr confirms it delivers there and has the certifications. Templated city pages for Seattle, NYC or Boston are not justified without local proof.

### Cited Findings
- Quotr's three proof projects are in Saratoga, Monte Sereno and Hillsborough (Bay Area) ([product-and-features.md](../../geo-brain/00-quotr/product-and-features.md)).
- Quotr's delivery area conflicts on the same page: "Final-mile delivery to your CA jobsite" versus "any US port or jobsite, coast to coast" (**TO CONFIRM**) ([product-and-features.md](../../geo-brain/00-quotr/product-and-features.md)).
- Quotr is a BIA Bay Area member and has attended IBS 2026, PCBC 2026, Dallas Build Expo 2026, RE:Forge SF and the CBD Fair 2026 in China ([quotr_offsite_presence.md](../Quotr%20GEO%20AEO%20strategy%20audit/quotr_offsite_presence.md); [geo-tactics-already-used.md](../../geo-brain/02-current-state/geo-tactics-already-used.md)).
- Quotr's Service line has a "Fast Cost Estimation (Residential LA Fire Rebuilding)" sample ([product-and-features.md](../../geo-brain/00-quotr/product-and-features.md)).
- NFRC rates and labels window U-factor and SHGC. Energy codes and inspectors often require NFRC-certified ratings. CARB Phase 2 / TSCA Title VI limit formaldehyde in composite wood used in cabinets. cUPC is IAPMO's plumbing listing mark ([repo glossary](../../geo-brain/04-prompt-library/construction-glossary.md)).

**Priority geo segments (evidence rows; segment logic is inference)**
| # | Segment | Evidence row | Job | Regulatory hook (verify) | Priority |
|---|---|---|---|---|---|
| G1 | Bay Area custom-home / luxury SFH builders and owner-builders (Santa Clara, San Mateo, Contra Costa, Marin) | 3/3 Quotr proofs; market finish quotes $58K–$245K per address; BIA Bay Area | Cut a $150K–$250K dealer finish package by ~45–55% without losing spec control | Title 24 window U-factor (2025 Energy Code, eff. 2026-01-01 **(unverified — training knowledge)**); CARB Phase 2 | **1** |
| G2 | LA County fire-rebuild owners and builders (Altadena, Pacific Palisades) | Quotr rebuild-estimate sample; rebuild owners are budget-capped by insurance **(likely)** | Rebuild to code inside an insurance payout | Title 24; CARB; local WUI/Chapter 7A window and door rules **(unverified — training knowledge)** | **2** |
| G3 | California small multifamily, ADU and BTR developers (5–50 units) | Port2Site's floor is 50 units / $50K, which leaves 5–50 units open | Hit a pro-forma finish line per unit | Same as G1 + CALGreen **(unverified)** | **3** |
| G4 | Sunbelt volume builders (TX, FL, AZ) | No Quotr proof; volume builders buy national programs **(likely)** | Lower finish cost per house at scale | FL: Florida Product Approval / Miami-Dade NOA for impact windows in the HVHZ **(unverified — training knowledge)** | 4 (only if Quotr ships outside CA) |
| G5 | Hospitality FF&E/OS&E hubs (purchasing firms concentrated in NYC/Atlanta/Dallas **(unverified)**) | One Quotr blog post; no project proof | Consolidated sourcing per key | Fire codes for FF&E **(unverified)** | 5 (skip for now) |

- **Ports:** LA/Long Beach and Oakland are the natural West Coast gateways for Foshan/Guangdong cargo **(unverified — no port statistics pulled)**.

### Inferences
- Geo pages are justified only where rules genuinely differ. California differs on energy code (Title 24 window U-factor), formaldehyde (CARB originated it) and Prop 65 warnings **(unverified)**. Florida differs on impact-window product approval. A "California factory-direct finish materials: Title 24 and CARB compliance" hub is defensible; "factory-direct windows in Boston" is not.
- Engines do not reliably inject geography unless it is stated or in memory (framework). The geo payoff comes from persona facts inside prompts ("Saratoga custom home", "Altadena rebuild") meeting dated local facts on Quotr pages.

### Gaps
- No metro-level data on finish-package costs, builder counts or permits pulled this session. Next pulls: Census Building Permits Survey by CBSA (SF, San Jose, LA, Seattle, Dallas, Houston, Phoenix, Tampa, Miami) and the BIA Bay Area membership count.
- Title 24 2025 window U-factor maxima by climate zone, Miami-Dade NOA requirements, and California Prop 65 obligations for imported composite-wood cabinets were not verified.
- Quotr's actual delivery footprint and whether it has any NFRC-certified window lines are unknown (**TO CONFIRM with Quotr**).

---

## D. Jobs-to-be-done (in their words)

### Takeaway
There are four core jobs, all expressed as risk-bounded savings: get the finish package under budget, keep spec and code control, make landed cost and timeline predictable, and avoid becoming the person who got scammed. These are working statements drawn from repo personas and observed prompt and title wording. No interview or forum verbatims backed them in this session.

### Cited Findings
- Persona 6 goals: "Lower material cost, predictable landed price, code-compliant products, on-time delivery." Pains: "Dealer markups; tariff uncertainty; surprise freight and duty bills; quality risk when importing directly; long lead times" ([audiences-and-personas.md](../../geo-brain/00-quotr/audiences-and-personas.md)).
- Observed public phrasing: "How to buy and import building materials from China? For house owner / builder / real estate" ([YouTube](https://www.youtube.com/watch?v=BP4TXwEm954)); "How to import building materials to finish your house from China" ([YouTube](https://www.youtube.com/watch?v=3JMRpzvsFoQ)); "Saved $50k with windows from China…" ([YouTube short](https://www.youtube.com/shorts/eUEi-uEzSj8)) (titles via [buyer-questions-by-trade.md](../../geo-brain/04-prompt-library/buyer-questions-by-trade.md)).
- Supplier titles show the "what it does to my number" framing: "Cabinet Tariffs 2026–2027: What They Mean for Your Quote" ([TC Wholesale](https://tcwholesalecabinetry.com/blog/cabinet-tariffs-2026-2027)); "The 2026 Cabinet Tariff Map: What Multifamily Developers Need to Know Before Spec Lock" ([Wirko](https://www.wirkobuildingsolutions.com/insights/2026-cabinet-tariff-map/)); "Will A Quartz Tariff Double Your Countertop Cost?" ([Kitchen Design Partners](https://kitchendesignpartners.com/blog/quartz-tariff-kitchen-countertop-cost/)).

### Inferences (working JTBD statements — **not verbatim**)
1. "When my finish quote comes in 20%+ over the pro forma, help me find a cheaper route for the same spec **before spec lock**, so I don't have to value-engineer the house into something I can't sell."
2. "When tariffs change again, tell me what my cabinets, windows and flooring will actually cost **delivered to my site** on my delivery date, so my bid or budget doesn't go stale."
3. "When I buy from a factory I've never visited, make sure what arrives matches the sample, passes inspection (NFRC, CARB, cUPC), and that someone in the US stands behind it."
4. "When I'm ordering 90+ days out, give me a schedule I can build my critical path around, with Chinese New Year and ocean delays priced in."
5. (Contractor variant) "When I supply and install, let me keep the material margin a dealer currently takes, without becoming an importer myself."

### Gaps
- Needs 6–12 switch interviews with recent Quotr Procurement buyers and lost quotes (framework protocol). The "what did you type, into what" question is especially important.

---

## E. Psychology

### Takeaway
This buyer's dominant restraining force is **anxiety, not habit**: fear of scams and deposit loss, fear of spec or code failure discovered at inspection, and fear of a landed cost that moves after commitment. Tariff whiplash amplifies all three. The domestic dealer quote is the anchor that makes the switch feel worth the risk. Design around the robust biases (anchoring, defaults/status quo, temporal landmarks), not fragile ones (generic social proof, choice overload).

### Cited Findings
- Robust effects (framework ranking): defaults and status-quo framing, d = 0.68 across 58 studies ([Jachimowicz et al.](https://ideas.repec.org/a/cup/bpubpo/v3y2019i02p159-186_00.html)); anchoring replicated as "substantially more powerful" than the original study ([Scientific American](https://www.scientificamerican.com/article/dozens-of-labs-respond-to-bolster-reliability-of-psychology-research)); temporal landmarks / fresh starts ([Dai, Milkman & Riis 2014](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf)).
- Fragile effects: descriptive-norm social proof failed to replicate ([PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0104086)); social cues had the smallest nudge effect, 0.94 pp ([DellaVigna & Linos](https://www.nber.org/system/files/working_papers/w27594/w27594.pdf)); choice overload has a meta-analytic d = 0.02 ([Scheibehenne et al.](https://academic.oup.com/jcr/article/37/3/409/1816569)).
- Time pressure shifts consumers to noncompensatory rules and unique features ([Dhar & Nowlis 1999](https://profiles.wustl.edu/en/publications/the-effect-of-time-pressure-on-consumer-choice-deferral/)).
- Trust in AI alone drops from 42% for purchases under $50 to **5% over $500**; 86% of shoppers who used AI verified elsewhere ([MarTech](https://martech.org/the-ai-shopping-stats-2026-what-you-need-to-know/), via framework).
- Contractors' top AI worries: data accuracy 57%, security 54%. Construction leaders' trust in AI fell 14 points year on year ([Dodge/CMiC via Construction Dive](https://www.constructiondive.com/news/builders-ai-transform-businesses-survey/807555/); [Autodesk](https://www.autodesk.com/blogs/construction/state-of-design-make-spotlight-construction/), via personas file).
- Persona 6 objections: "Quality and certification: will it pass inspection (NFRC, CARB, cUPC)?"; "What if something arrives damaged or wrong?"; "About 90 days is a long lead time." ([audiences-and-personas.md](../../geo-brain/00-quotr/audiences-and-personas.md); these are Quotr-written assumptions, not customer verbatims).

### Inferences
| Dimension | This ICP | Design implication |
|---|---|---|
| Fear of scams | Deposits wired to unknown factories; Alibaba horror stories; "is X legit" prompts | Show a named US entity, a US contract, escrow or staged payment terms (**TO CONFIRM**), factory audit reports, and named references |
| Quality / spec risk | Discovered late, at install or inspection, and costly to fix after a 90-day lead time | Pre-shipment QC reports, sample approval, NFRC/CARB/cUPC documents per SKU, a US warranty and replacement-parts policy |
| Loss of control vs savings | The dealer is slow and pricey but local and accountable | A "control" checklist (samples, video QC, shop drawings and submittals, a US point of contact); never frame it as "trust us" |
| Procurement identity | A procurement lead is judged on zero surprises more than on savings **(likely)**. An owner-builder is judged on savings | Two page modes: a risk-first page for procurement leads, a savings-first page for owner-builders |
| Decision style | Committee of developer + architect/designer + GC (the GC may resist owner-furnished material) | Submittal-ready spec sheets the architect can approve; an installer-friendly packing list; GC-facing FAQ on owner-furnished, contractor-installed (OFCI) **(term unverified for this ICP)** |
| Hot vs cold | **Hot:** domestic quote just came in over budget, a tariff date is days away, or a supplier pushed lead time. **Cold:** pre-design or Canton Fair research | Urgent page leads with "5-day landed quote vs your dealer quote" and a tariff-date cue. Considered page has comparison tables and HTS/AD/CVD detail |
| Anchoring (robust) | The domestic dealer quote anchors "savings %"; the tariff headline ("319.81%") anchors fear | Always show the side-by-side vs a dated dealer quote, and show the realistic stack per category so the scary headline doesn't stick |
| Loss aversion on deposits | A 30%-style factory deposit **(term typical; unverified)** feels like a sunk loss if goods fail | Staged payments tied to QC milestones as a choice-architecture change (not a message tweak) |
| Status quo / defaults (robust) | The default is "use our usual dealer" | Make the comparison cheap: "send us your dealer quote; we return a DDP quote in 3–5 business days" (Quotr's stated quote time, **TO CONFIRM**) |
| Temporal landmarks (robust) | Jan 1, 2027 step-up; Chinese New Year; Q1 buyout | Calendar-anchored urgent pages: "order before X to land before Y" |

### Gaps
- No direct evidence on committee composition or who has veto power; validate in interviews.
- Deposit and payment norms for Quotr are unknown (**TO CONFIRM**).

---

## F. Four forces with verbatim quotes

### Takeaway
**This section is incomplete.** The required ≥8 buyer verbatims from Reddit, BiggerPockets, Houzz and LinkedIn could not be collected: the search budget ran out, and the proxy refuses reddit.com and youtube.com (403 on CONNECT). An earlier Perplexity search in the repo found **no** r/Contractor threads about buying cabinets or windows from China, which suggests this ICP's public talk lives more on YouTube and supplier blogs than on Reddit. Below are the verbatims that do exist with URLs (titles, publisher copy, engine text), clearly typed, plus the forces map and a mining protocol.

### Cited Findings
**Available verbatims (type noted; none is a buyer forum post)**
| # | Force | Verbatim | Type | URL |
|---|---|---|---|---|
| 1 | Pull | "Saved $50k with windows from China…" | Creator video title | [YouTube short](https://www.youtube.com/shorts/eUEi-uEzSj8) |
| 2 | Push / pull | "How to buy and import building materials from China? For house owner / builder / real estate" | Creator video title | [YouTube](https://www.youtube.com/watch?v=BP4TXwEm954) |
| 3 | Push | "How to source building materials from China to the U.S. as tariffs bite" | Sourcing-firm guide title | [George International](https://georgeintl.com/how-to-source-building-materials-from-china-to-usa-as-tariffs-bite/) |
| 4 | Anxiety | "Will A Quartz Tariff Double Your Countertop Cost?" | Designer blog title | [Kitchen Design Partners](https://kitchendesignpartners.com/blog/quartz-tariff-kitchen-countertop-cost/) |
| 5 | Anxiety | "Kitchen Cabinet Tariffs 2026: 319.81% Duty From China" | Retailer page title | [ChinaHomeSource](https://www.chinahomesource.com/us/tariffs/kitchen-cabinets/) |
| 6 | Push (timing) | "…What Multifamily Developers Need to Know Before Spec Lock" | Competitor insight title | [Wirko](https://www.wirkobuildingsolutions.com/insights/2026-cabinet-tariff-map/) |
| 7 | Habit / anxiety | "Local vs imported materials: a GC's guide to navigating the tariffs" | Competitor blog title | [Handoff](https://www.handoff.ai/blog/local-vs-imported-materials-a-gcs-guide-to-navigating-the-tariffs) |
| 8 | Market gap | "the search results do not show a single platform explicitly marketed as a factory-direct marketplace for all building materials" | Perplexity answer text (Sep 2026) | [quotr_offsite_presence.md](../Quotr%20GEO%20AEO%20strategy%20audit/quotr_offsite_presence.md) |
| 9 | Brand perception | "Quotr.ai and FBM Sourcing emphasize sourcing and procurement more than AI takeoff" | Perplexity answer text (re-run) | [verification_quotr_and_competitors.md](../Quotr%20GEO%20AEO%20strategy%20audit/verification_quotr_and_competitors.md) |
| 10 | Pull (claim) | Savings "up to 65%" vs traditional US suppliers; "Saves 15–30%", removes "3–5 layers of margin" | Competitor claims (Build Source; Port2Site) | [buildsourcedirect.com](https://buildsourcedirect.com/); [port2site.com](https://www.port2site.com/direct-import) (search summaries via repo) |

**Forces map (from findings above, the personas file and section B)**
| Force | Content (working) | Strength evidence |
|---|---|---|
| Push | Dealer quote over budget; Section 232 cabinet tariff plus the Jan 2027 step-up; AGC: 40% of contractors raised bids and 35% passed tariffs to owners; dealer lead-time slips | AGC; Section 232 timeline (B) |
| Pull | 40–60% savings stories (Quotr cards 44–60%; YouTube "$50k"); one delivered price; spec freedom (custom sizes, finishes) | Quotr cards; competitor claims |
| Anxiety | Scam or deposit loss; quality and certification failure; AD/CVD surprise; tariff moves after quote; damage in transit; no US warranty | Personas objections; supplier "319.81%" headlines; importer guides warning on DDP plus AD |
| Habit | Dealer relationship, credit terms, local returns, "my GC/installer won't touch owner-supplied material" **(likely)** | Not evidenced in-session |

### Inferences
- With pull claims at 15–65% across vendors, buyers will discount any single savings number. Proof must be per-category and dated, against a named comparable spec.
- The anxiety force has the richest public vocabulary (tariff and duty headlines). The habit force is barely visible publicly. That is a reason to find it in interviews, since it probably drives lost quotes.

### Gaps
- **≥8 buyer verbatims with URLs not obtained.** Mining protocol for the next pass, which needs reddit.com access or a Reddit API key plus 10–15 searches:
  - r/Construction, r/HomeBuilding, r/RealEstateDevelopment, r/Alibaba, r/Contractor, r/KitchenRemodel, r/Hospitality, r/ADU
  - BiggerPockets "cabinets from China" and "windows from China"
  - Houzz "ordered cabinets from China"
  - Trustpilot/Google reviews of FBM Sourcing, Go Global, Trillion Sources, Build Source, Port2Site
  - LinkedIn posts with "factory direct" + "multifamily" + "tariff"
  - YouTube comments under the three videos above (often the richest anxiety verbatims)

  Code each one into the framework chain.

---

## G. Trigger events and trigger calendar

### Takeaway
Triggers are unusually datable for this ICP: tariff effective dates, truce expiries, AD review publications, the quartz quota year and quarters, Chinese New Year, trade fairs and project buyout. Raise prompt-sampling frequency and refresh pages two to four weeks before each.

### Cited Findings and calendar (dated items sourced; seasonal items flagged)
| Date / window | Trigger | Expected prompt surge | Source |
|---|---|---|---|
| 2026-11-09 / 11-10 | Port-fee and Affiliates-Rule suspensions end; 178 Section 301 exclusions lapse unless extended | "did section 301 exclusions expire" | [Thomson Reuters](https://tax.thomsonreuters.com/blog/section-301-exclusions-expiration/) |
| Nov–Dec 2026 | Pre-buying ahead of the Jan 1 cabinet/vanity step-up (25%→50%) | "order cabinets before January 2027 tariff" | [Cabinex](https://cabinexwholesale.com/blogs/navigating-25-section-232-tariff-kitchen-cabinets-2027-increase) |
| **2027-01-01** | Section 232 cabinets/vanities 50%; upholstered furniture 30% (unless deferred again, as happened on 2025-12-31) | "kitchen cabinet tariff 50% 2027" | [TC Wholesale](https://tcwholesalecabinetry.com/blog/cabinet-tariffs-2026-2027) |
| **2027-01-10** | Busan truce expiry (extended from Nov 10) | "US China tariffs January 2027" | [CNBC](https://www.cnbc.com/2026/09/24/us-china-trade-truce-bessent-trump-xi.html) |
| Jan–Feb 2027 | Chinese New Year factory shutdown (CNY 2027 ≈ Feb 6 **(unverified — training knowledge)**); orders placed after ~mid-Dec slip | "chinese new year factory closure lead time" | — |
| Quarterly (from 2026-08-15) | Quartz in-quota volume allocated 25% per quarter. Once the quota fills, the over-quota 50% applies. Year 2 starts 2027-08-15 (23%/49%) | "quartz tariff over quota" | [Mondaq](https://www.mondaq.com/unitedstates/international-trade-investment/1829966/new-section-201-safeguard-tariffs-on-quartz-surface-products) |
| April (annual) | Cabinet AD review finals have been published in April (2026-04-23) | "cabinet antidumping rate 2027" | [FR](https://www.federalregister.gov/documents/2026/04/23/2026-07866/wooden-cabinet-and-vanities-and-components-thereof-from-the-peoples-republic-of-china-final-results) |
| Open | Section 301 excess-capacity action (21 sectors, 16+ economies including Vietnam); IEEPA refund litigation at CIT | "vietnam tariff 2027", "IEEPA refund who gets it" | [Helen of Troy 10-Q](https://www.sec.gov/Archives/edgar/data/0000916789/000091678926000138/hele-20260831.htm); [A&O Shearman](https://www.aoshearman.com/en/insights/scotus-rejects-ieepa-tariffs-refund-opportunities-and-uncertainty-emerge) |
| April & October | Canton Fair. The building and decoration materials phase is usually Phase 2 **(unverified — training knowledge)** | "canton fair building materials 2027" | — |
| Summer (Jul–Aug) | CBD Fair (China Building & Decoration Fair, Guangzhou); Quotr attended in 2026 and posted on 2026-08-27 | "CBD fair 2027" | [website-audit.md](../../geo-brain/02-current-state/website-audit.md) |
| Event-driven | Ocean freight rate spikes; port congestion | "container rate China to Oakland" | Not sourced this session |
| Project-driven | Buyout window: roughly 90–120 days before cabinet/window install for a ~90-day DDP lead (inference from Quotr's "about 90 days", **TO CONFIRM**) | "lead time windows from China to California" | [product-and-features.md](../../geo-brain/00-quotr/product-and-features.md) |
| Show calendar | IBS/KBIS (Feb **(unverified)**), PCBC (Jun **(unverified)**), HD Expo (spring **(unverified)**), BDNY (Nov **(unverified)**) | Brand and category prompts after shows | — |

### Inferences
- 2026 delivered at least seven tariff "events" (Feb 20, Feb 24, Apr 6, Apr 23, Jul 24, Aug 15, Sep 23). That is roughly one every six weeks, which supports a monthly-refresh tracker plus an event-driven update rule (publish within 48 hours of a proclamation or Federal Register notice).
- The Dec 31, 2025 deferral shows the Jan 1 dates can move at the last minute. Pages must say "scheduled" and carry an "as of" date.

### Gaps
- Freight-rate series (Drewry or Freightos China–US West Coast) and 2027 trade-show dates were not pulled.

---

## H. Switch timeline with prompt form at each stage

### Takeaway
The prompt changes from situational ("my cabinet quote is $90k") to categorical ("factory direct cabinets") to evaluative and branded ("Quotr vs sourcing agent", "is X legit"). Each stage needs a different page and proof.

### Cited Findings
- Framework timeline: first thought → passive looking → active looking → deciding → consuming. Problem-aware prompts have no category noun; solution-aware prompts name a category; product-aware prompts name brands. ChatGPT injects "best" into 24.3% of advice-question fan-outs ([framework](/root/.claude/uploads/0814826c-2913-57ec-9cf0-acc28e8d23b1/3fb5eb52-ICP_depth_framework_for_GEO.md); [PPC Land/Peec](https://ppc.land/what-chatgpt-actually-searches-for-5-million-fanout-queries-analyzed/)).

### Inferences
| Stage | What's happening | Prompt form (example; constructed, not observed) | Page that should answer |
|---|---|---|---|
| First thought | Dealer quote lands 20–40% over budget, or a tariff headline | "our kitchen and bath finish quote came in way over budget for a 4,000 sq ft custom home, what are our options" | Hub "Finish package over budget? 5 levers" |
| Passive looking | Reads tariff news; sees a YouTube "saved $50k" video | "is it actually cheaper to buy windows and cabinets from China with the 2026 tariffs" | Honest "when importing pays / doesn't" |
| Active looking | Compares routes; learns vocabulary | "factory direct vs sourcing agent vs alibaba for building materials" · "DDP vs FOB building materials" · "landed cost calculator cabinets china" | Decision guide; calculator; tariff tracker |
| Deciding | Shortlists vendors; checks legitimacy and compliance | "Quotr procurement reviews" · "is [agent] legit" · "do imported windows need NFRC label California" | Brand facts page; compliance pages; references |
| Consuming | Order placed; tracking QC and delivery | "how to inspect cabinets before shipping from china" · "what to do if imported cabinets arrive damaged" | Post-purchase help center (also a GEO asset) |
| Re-decide (next project) | Repeat with memory; terse prompts | "update landed cost for the same cabinets for Q1 2027" | Tracker + index refresh |

### Gaps
- Real stage-by-stage prompts need switch interviews ("what exactly did you type, and into what?").

---

## I. Current alternatives and unmet needs

### Takeaway
Each alternative solves one slice. Dealers and big-box give accountability without savings. Alibaba gives price without accountability. Sourcing agents give access without delivered-price or US liability. Container importers give scale without small-project fit or software. The most frequent unmet need, inferred from competitor claims and tested AI answers, is **one accountable, dated, delivered price for a mixed finish package on a small-to-mid project, with compliance documents**.

### Cited Findings
| Alternative | What it offers | Evidence | What it fails to satisfy |
|---|---|---|---|
| Domestic distributors / dealers | Local accountability, returns, credit | Quotr market ranges $58K–$245K per address vs $30K–$108K DDP ([product-and-features.md](../../geo-brain/00-quotr/product-and-features.md)) | Price (dealer layers; Port2Site cites "3–5 layers of margin"); pass-through of tariffs |
| Big-box pro desks | Speed, availability; integrated into Buildxact (Home Depot) and Handoff (Lowe's) | [competitors/procurement-and-sourcing.md](../../geo-brain/03-market/competitors/procurement-and-sourcing.md) | Limited spec range; domestic pricing only |
| Local "factory direct" dealers | Named in AI answers for C14: Platinum Direct, Floor Daddy Depot, Shop At Home Cabinets, SD Wood, Universal Factory Direct, Northeast Factory Direct | [quotr_ai_visibility_tests.md](../Quotr%20GEO%20AEO%20strategy%20audit/quotr_ai_visibility_tests.md) | "Factory direct" is a label, not an import; savings unclear |
| Alibaba / B2B marketplaces | Price discovery, huge catalog (C10: Alibaba, Global Trade Plaza, AGTS, Marteu, BRKZ, ZeroGap, Commervia) | [tracking-set T10](../../geo-brain/04-prompt-library/tracking-set.md) | No quality or logistics responsibility; buyer becomes importer of record and owns AD/CVD and ISF risk (ISF $5,000 liquidated damages per violation) ([CBP](https://www.help.cbp.gov/s/article/Article-1868), via repo) |
| Sourcing agents (FBM Sourcing, Go Global "5,000+ verified manufacturers", Trillion Sources, Spotyard) | Factory access, QC visits | [competitor_geo_benchmark.md](../Quotr%20GEO%20AEO%20strategy%20audit/competitor_geo_benchmark.md) | Fee on top (5–10% commission per brief, **unverified**); usually FOB not DDP; no US liability or software |
| Container-scale importers (Port2Site; Build Source "supplier and seller of record"; Wirko Building Solutions) | Factory-direct packages, "tariff-smart" VE, multi-country (China, Vietnam, Malaysia, Turkey, Mexico) | [procurement-and-sourcing.md](../../geo-brain/03-market/competitors/procurement-and-sourcing.md); [Wirko](https://www.wirkobuildingsolutions.com/insights/2026-cabinet-tariff-map/) | Port2Site floor of 50 units / $50K; no takeoff or estimating |
| Procurement software (Field Materials AI, Trimble Materials, Archdesk, Procore, Precoro) | Purchasing workflow; Field Materials claims 5–10% savings | [procurement-and-sourcing.md](../../geo-brain/03-market/competitors/procurement-and-sourcing.md) | Does not source cheaper product |
| Buying trips / trade fairs (Canton, CBD Fair) | See factories in person | Quotr attended CBD Fair 2026 | Time, language, follow-through, no delivered price |
| Do nothing / value-engineer | Swap to cheaper domestic spec | AGC: 40% raised bids | Erodes product quality and sale price |

**Unmet needs ranked (frequency proxy = how many alternatives fail it × how often it appears in tested AI answers and competitor copy; inferred ranking)**
1. A delivered, duty-inclusive price with a stated rate date and repricing rule. Fails: Alibaba, agents, most guides. Several importing guides warn about DDP plus AD.
2. Compliance documents per SKU (NFRC, CARB Phase 2/TSCA VI, cUPC) that pass inspection. No competitor page found answering it; repo prompts L-082/L-090/L-101 have no owner.
3. Accountability: a US contracting party, warranty and damage remedy. Fails: Alibaba, agents.
4. Small-to-mid project fit (one house to 50 units). Fails: Port2Site, container importers.
5. Honest category triage (what not to import in 2026–27, e.g. Chinese quartz and China-wide-rate cabinets). No one publishes it.
6. Connection to the estimate (takeoff → material list → quote → PO). Only Quotr claims it, and AI does not yet credit it (T43 re-run).

### Inferences
- The "honest triage" need (#5) is the most differentiating content Quotr can publish. It costs nothing but builds trust, and it is exactly the kind of evaluative passage engines quote.

### Gaps
- Frequency ranks are not measured; validate with the post-purchase trigger survey and lost-quote reasons.
- Sourcing-agent fee levels and Alibaba dispute rates were not verified.

---

## J. Willingness to pay, price anchors, terms, sales cycle

### Takeaway
WTP is anchored on the **dealer quote**: buyers will pay a managed premium over raw factory price if the delivered total beats the dealer by a visible margin. Vendor claims range from 5–10% (procurement software) to 15–30% (Port2Site), 40–55% (Quotr) and "up to 65%" (Build Source). Quotr's own cards imply 44–60% below the quoted market range. Deposits and sales cycle are unverified.

### Cited Findings
| Anchor | Value | Source |
|---|---|---|
| Quotr savings claim | "40–55% average cost reduction per project" (also "up to 50%", "40–50%" elsewhere: conflicting) | [product-and-features.md](../../geo-brain/00-quotr/product-and-features.md); [procurement-and-sourcing.md](../../geo-brain/03-market/competitors/procurement-and-sourcing.md) |
| Quotr project math (computed from the cards) | Myren Dr $97,000 vs $187K–$218K = 48–56% below; Stratford Ct $108,290 vs $195K–$245K = 44–56%; Skyfarm Dr $30,437 vs $58K–$76K = 48–60% | Arithmetic on [/procurement/](https://quotr.ai/procurement/) card figures |
| Port2Site | Saves 15–30%; lead 10–14 weeks; 50+ units or $50K+ | [port2site.com](https://www.port2site.com/direct-import) (via repo) |
| Build Source | "up to 65%" vs US suppliers | [buildsourcedirect.com](https://buildsourcedirect.com/) (via repo) |
| Field Materials AI | 5–10% material savings | [procurement-and-sourcing.md](../../geo-brain/03-market/competitors/procurement-and-sourcing.md) |
| Landed vs FOB | 1.3–1.7× FOB (guides; exact page not isolated) | [prompt-library L-112](../../geo-brain/04-prompt-library/prompt-library.md) |
| Software tie-in | Plus plan $299.90/seat/month includes "10% off procurement" | [product-and-features.md](../../geo-brain/00-quotr/product-and-features.md) |
| Quote and delivery time | Quote in ~3–5 business days; delivery "typically within about 90 days" (**TO CONFIRM**) | [product-and-features.md](../../geo-brain/00-quotr/product-and-features.md) |
| Who pays tariffs | 35% of contractors pass most or all tariff costs to owners | [AGC](https://www.agc.org/news/2026/01/14/construction-costs-rise-fastest-rate-january-2023-november-outpacing-increases-contractors-bid) (via repo) |

### Inferences
- Because the stack moved (for example cabinets +25 points on Jan 1, 2027), Quotr's 44–60% card savings may not hold for 2027 cabinet-heavy packages. The cards are undated, and buyers and engines will test them against current tariff news. Re-quote one card at 2027 rates and publish both numbers.
- The 10% Plus-plan discount only matters if the procurement ticket is large: 10% of $97,000 = $9,700 against $3,599/year for Plus. That is a strong cross-sell for 9d contractors.
- The sales cycle is probably 2–8 weeks from first quote to deposit for a single house, gated by architect approval of samples **(speculative)**.

### Gaps
- Sourcing-agent commission levels, typical deposit terms (30/70 is a common convention, **unverified**), Quotr's payment terms, minimum order, warranty and actual win rates.

---

## K. Vocabulary list

### Takeaway
These buyers use incoterm, customs and compliance vocabulary that marketing pages rarely define with current dates. Each term below should be a short, dated answer block on Quotr pages, with Quotr's name in the sentence.

### Cited Findings
| Term | Plain meaning / current fact | Source |
|---|---|---|
| DDP (Delivered Duty Paid) | Seller delivers to a named place with duties paid and customs cleared; unloading is normally the buyer's job | [ICC Incoterms 2020](https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/) via [glossary](../../geo-brain/04-prompt-library/construction-glossary.md) |
| FOB / EXW / CIF | FOB: seller loads at origin port, then buyer risk (sea only). EXW: buyer collects at factory. CIF: seller pays freight and insurance, risk passes at loading | Same |
| Landed cost | Product + packing + freight + insurance + duties + customs fees + inland delivery | [glossary](../../geo-brain/04-prompt-library/construction-glossary.md) |
| HTS code | 10-digit US code; first 6 = HS; sets duty | [USITC](https://www.usitc.gov/tariff_affairs/about_hts.htm) |
| Section 301 (lists; forced-labor 2026) | USTR trade-remedy duties; China list duties often 25%; forced-labor duty 12.5% for China since 2026-07-24 | [EY](https://taxnews.ey.com/news/2026-1607-ustr-finalizes-section-301-forced-labor-tariffs-on-60-economies-additional-tariffs-of-10-percent-or-125-percent-take-effect-24-july-2026) |
| Section 232 (wood; metals) | National-security tariffs: cabinets/vanities 25% (→50% 2027-01-01); metals on full value since 2026-04-06 | Section B |
| Section 201 safeguard / TRQ; in-quota / over-quota | Quartz 25%/50% from 2026-08-15 | [Mondaq](https://www.mondaq.com/unitedstates/international-trade-investment/1829966/new-section-201-safeguard-tariffs-on-quartz-surface-products) |
| Section 122 | 150-day balance-of-payments surcharge (10%), expired 2026-07-24 | [Z2Data](https://www.z2data.com/insights/how-the-termination-of-section-122-tariffs-impacts-your-supply-chain/) |
| IEEPA tariffs; CAPE refunds | Struck down 2026-02-20; refunds through CBP CAPE | [A&O Shearman](https://www.aoshearman.com/en/insights/scotus-rejects-ieepa-tariffs-refund-opportunities-and-uncertainty-emerge) |
| AD/CVD; China-wide rate; separate rate; cash deposit; administrative review | Cabinets: China-wide 251.64%, separate 10.02% (2026-04-23) | [FR](https://www.federalregister.gov/documents/2026/04/23/2026-07866/wooden-cabinet-and-vanities-and-components-thereof-from-the-peoples-republic-of-china-final-results) |
| Circumvention / scope ruling / transshipment | Vietnam-completed cabinets with Chinese parts covered (2024) | [ASL](https://aslgate.com/united-states-issues-final-conclusion-on-scope-review-and-anti-circumvention-investigation-of-vietnamese-wooden-cabinets/) |
| 9903 headings (e.g. 9903.76.03, 9903.05.90, 9903.45.30/31) | Chapter 99 lines that carry the extra duties | Section B sources |
| Full customs value / Annex I-A / I-B | Metals 232 basis since Apr 2026 | [Thompson Coburn](https://www.thompsoncoburn.com/insights/74-april-2-2026-new-proclamation-makes-major-revisions-to-section-232-tariffs-on-steel-aluminum-copper/) |
| CBP Form 7501 (entry summary); importer of record (IOR); customs broker; ISF 10+2 | 7501 and IOR **(unverified definitions — training knowledge)**; ISF due 24h before loading, $5,000 liquidated damages per violation | [CBP ISF](https://www.help.cbp.gov/s/article/Article-1868) |
| FCL / LCL; 20 ft / 40 ft container | Full vs shared container | [glossary](../../geo-brain/04-prompt-library/construction-glossary.md) |
| QC inspection (pre-shipment, during production); factory audit; golden sample | Vendor-side quality gates | **(unverified — standard trade usage)** |
| Shop drawings; submittals; spec lock; OFCI | Architect/GC approval vocabulary; "spec lock" seen in Wirko's title | [Wirko](https://www.wirkobuildingsolutions.com/insights/2026-cabinet-tariff-map/) |
| NFRC; U-factor; SHGC; Title 24 | Window rating label; CA energy code | [glossary](../../geo-brain/04-prompt-library/construction-glossary.md) |
| CARB Phase 2 / TSCA Title VI | Formaldehyde limits on composite wood | Same |
| cUPC | IAPMO plumbing listing | Same |
| Miami-Dade NOA / Florida Product Approval | Impact-window approvals | **(unverified — training knowledge)** |
| Busan Agreement / truce | US–China pause, extended to 2027-01-10 | [NBC](https://www.nbcnews.com/business/economy/us-china-extend-trade-truce-trump-rcna599525) |

### Inferences
- "Spec lock", "separate rate", "over-quota" and "full value" are 2026-specific terms with almost no plain-English coverage outside law-firm alerts. They are cheap terms to own.

### Gaps
- Exact current definitions and penalties for CBP Form 7501 entries, importer-of-record obligations and country-of-origin marking were not re-verified.

---

## L. Channels

### Takeaway
Public discussion by this ICP is thin on Reddit. One earlier Perplexity check found no r/Contractor threads on buying finishes from China. It is richer on YouTube creator videos, supplier blogs, law-firm and forwarder alerts, and trade press. Trade shows (IBS/KBIS, PCBC, CBD Fair/Canton) are where trust gets built. Subreddit member counts could not be retrieved.

### Cited Findings
| Channel type | Named outlets seen | Evidence |
|---|---|---|
| YouTube creators | Import-from-China building-materials videos and shorts ("Saved $50k with windows from China…") | [buyer-questions-by-trade.md](../../geo-brain/04-prompt-library/buyer-questions-by-trade.md) |
| Trade press (flooring/stone/cabinet) | Floor Daily, FCNews, Floor Trends, Stone World, Stone Update, KCMA insights | Search results in this session ([Floor Daily](https://www.floordaily.net/flooring-news/ceramic-imports-declined-25-in-november-vinyl-imports-down-16); [FCNews](https://www.fcnews.net/2020/08/tariffs-cant-derail-lvts-momentum); [Floor Trends](https://www.floortrendsmag.com/articles/103853-us-trade-rep-finalizes-tariffs-on-chinese-imports); [Stone World](https://www.stoneworld.com/articles/95779-trump-imposes-four-year-tariff-rate-quota-on-imported-quartz-surface-products); [KCMA](https://kcma.org/insights/quartz-surface-products-201-safeguard-determination)) |
| Law-firm / forwarder / customs alerts | Thompson Hine, Thompson Coburn, Wiley, STR, Allyn, Green Worldwide, C.H. Robinson, Expeditors, Mondaq, A&O Shearman, White & Case | Section B |
| Programmatic tariff tools | ustariffrates.com, tariffs.wove.com, tarifflens.ai, tariffstool.com, tariffschart.com, htshero.com, gingercontrol.com, tariffsapi.com, airliftusa.com | Search results (O2) |
| Supplier/dealer explainers | NextDay Cabinets, TC Wholesale Cabinetry, Cabinex, ChinaHomeSource, Wirko, Carmel Imports, Rockheads, HanStone | Search results (O2) |
| Trade shows | IBS 2026, PCBC 2026, Dallas Build Expo 2026, CBD Fair 2026 (Quotr attended); KBIS, HD Expo, BDNY, Canton Fair (**not verified in-session**) | [offsite-presence.md](../../geo-brain/02-current-state/offsite-presence.md) |
| Associations | BIA Bay Area (Quotr member); KCMA (domestic cabinet makers, petitioner-aligned) | [quotr_offsite_presence.md](../Quotr%20GEO%20AEO%20strategy%20audit/quotr_offsite_presence.md); [KCMA](https://kcma.org/insights/kcma-applauds-positive-step-forward-commerce-unfairly-traded-cabinet-imports-malaysia-and) |
| Communities (Reddit/BiggerPockets/Houzz) | r/Construction, r/Contractor, r/ConstructionManagers listed in Quotr's playbook; no member counts | [reddit-and-community.md](../../geo-brain/06-playbooks/offsite/reddit-and-community.md) |

### Inferences
- For Google AI surfaces, YouTube is the strongest owned-media lever: the framework puts YouTube at about 21% of AIO mentions. A chaptered factory-QC and landed-cost walkthrough video fits the ICP's existing YouTube behaviour.
- Trade press that already covers tariffs per category (Floor Daily, Stone World, KCMA insights) is the realistic earned-media target for a landed-cost index.

### Gaps
- Member counts and growth for r/HomeBuilding, r/RealEstateDevelopment, r/Alibaba, r/Hospitality, r/KitchenRemodel; BiggerPockets and Houzz thread density; LinkedIn group sizes; Furniture Today, Kitchen & Bath Design News and Supply Chain Dive coverage not checked.

---

## M. Proof required at each stage + coding chains

### Takeaway
Proof escalates from dated facts (tariff tables, definitions) to per-SKU documents (NFRC, CARB, cUPC, QC reports), then to accountability (US contract, warranty, references, rate-lock terms). The coding chains below are the units the prompt matrix and pages are built from.

### Cited Findings
- 86% of AI-assisted shoppers verify elsewhere; trust in AI alone is 5% over $500 ([MarTech](https://martech.org/the-ai-shopping-stats-2026-what-you-need-to-know/)). So every AI-facing claim needs a one-click-verifiable anchor.
- Quotr's current proof: three priced project cards (with a "Client saved ~$0" display bug), a catalog PDF, a case-study PDF and a 6-question FAQ. No QC or certification page exists ([product-and-features.md](../../geo-brain/00-quotr/product-and-features.md); [buyer-questions-by-trade.md](../../geo-brain/04-prompt-library/buyer-questions-by-trade.md)).

**Proof by stage**
| Stage | Proof required | Quotr has today? |
|---|---|---|
| First thought / passive | Dated tariff facts by category; honest "when importing pays" math | Partial (tariff posts lack finish categories) |
| Active | Landed-cost worked example vs dealer quote; DDP inclusions list; lead-time calendar | Partial (DDP post; no calculator) |
| Deciding | Factory audit summaries; QC report sample; NFRC/CARB/cUPC docs per SKU; US warranty; references; rate-lock/repricing clause; AD/CVD disclosure | Mostly missing (**TO CONFIRM**) |
| Consuming | Damage/replacement process; spare parts; installer packing lists | Unknown |

**Coding chains (trigger → stage → mode → restraining force → exact prompt → proof)**
| # | Trigger | Stage | Mode | Restraining force | Exact prompt (constructed) | Proof required |
|---|---|---|---|---|---|---|
| C1 | Dealer finish quote 20% over pro forma | First thought → active | Hot | Anxiety (quality/scam) | "Our cabinets, vanities and windows quote for a custom home in Saratoga came in at $210k, 20% over budget — is buying factory-direct from China still worth it with 2026 tariffs?" | Side-by-side dated DDP vs dealer quote for the same spec; tariff stack per category |
| C2 | Jan 1, 2027 cabinet step-up headline | Active | Hot (deadline) | Anxiety (landed cost moving) | "If I order kitchen cabinets from China now, will the 50% tariff in January 2027 apply to my order?" | Entry-date rule explained; rate-lock/repricing terms; AD separate-rate status |
| C3 | Bad Alibaba experience (wrong finish, no recourse) | Active | Cold-to-hot | Anxiety (scam) + habit (back to dealer) | "Got burned ordering vanities on Alibaba — is there a US company that handles factory QC and delivers duty paid?" | US contracting entity, QC reports, staged payments, references |
| C4 | Window lead time blew up at domestic supplier | Active | Hot | Anxiety (spec/code) | "Need 42 aluminum windows for a Bay Area build, local lead time is 20 weeks — can I import NFRC-certified windows from China and pass Title 24?" | NFRC certificates/labels per product line; U-factor table; 2026 aluminum 232 cost impact |
| C5 | Multifamily finish budget per unit over | Deciding | Cold (committee) | Habit (GC/architect resistance) | "We're a 24-unit multifamily developer in San Jose — compare Port2Site, a sourcing agent and Quotr for LVP, cabinets and fixtures" | Unit-level price table; submittal-ready spec sheets; comparison of minimums |
| C6 | Tariff headline "319% on Chinese cabinets" | Passive | Cold | Anxiety (fear of hidden duty) | "Is it true kitchen cabinets from China have a 300% tariff?" | Plain AD China-wide vs separate-rate explanation with FR citation; what Quotr's quote includes |
| C7 | Owner-builder rebuilding after the LA fires, insurance cap | First thought | Hot | Anxiety (budget) + unfamiliarity | "Rebuilding my house in Altadena with an insurance cap — how much can I save buying cabinets, flooring and fixtures direct from manufacturers?" | Rebuild example; CARB/Title 24 compliance; delivery to LA |
| C8 | Supply-and-install flooring sub sees margin squeeze | Active | Cold | Habit (dealer credit terms) | "I'm a flooring contractor — how do I buy SPC/LVP direct from a factory in China duty paid without becoming an importer?" | DDP explanation (IOR = seller); min order; 10% off via Quotr Plus |

### Gaps
- Chains are constructed from evidence and logic, not coded from interviews. Promote a chain to the backlog only after ≥3/12 interviews or ≥5/50 community posts (framework threshold).

---

## N. Prompt matrix

### Takeaway
There are 12 full-context first-person prompts, 6 short category prompts and 3 brand prompts. Tags follow the framework. Demand tiers are **estimates** (no GSC, Keyword Planner or Profound data pulled), based on observed SERP crowding and prior audit tests.

### Cited Findings
- Comparative "ask for a pick" prompts earn a 22.8% brand-recommendation rate vs 8.0% for topic-only ([Momentic](https://momenticmarketing.com/blog/prompt-set-worth-tracking)). Comparative prompts earn a 43.3% mention rate vs 18% for informational ([Semrush](https://semrush.com/blog/the-ghost-citations-study/)). Brand prompts must be tracked separately ([Peec](https://peec.ai/blog/how-to-choose-the-right-prompts-for-llm-tracking)).
- Existing tracked prompts for this ICP: T09, T10, T14, T29, T33, T42, T43, T46, T48 ([tracking-set.md](../../geo-brain/04-prompt-library/tracking-set.md)).

### Inferences
**Full-context prompts (persona facts embedded)**
| ID | Prompt | Buyer | Intent | Stage | Urgency | Mode | Engine | Expected fan-out nodes | Tier (est.) |
|---|---|---|---|---|---|---|---|---|---|
| F1 | "I'm building a 4,500 sq ft custom home in Saratoga, CA and the dealer quote for cabinets, vanities, windows and doors is $210k — 20% over budget. Is buying factory-direct from China and having it delivered duty-paid still cheaper after the 2026 tariffs?" | 9e/9a | compare | first→active | acute | hot | ChatGPT | "factory direct cabinets china tariff 2026", "DDP building materials", "cabinet section 232 2026", "best factory direct supplier California" | 3 |
| F2 | "We're a Bay Area developer doing 3 spec homes in Los Gatos. Which is better for kitchen cabinets: a sourcing agent in Foshan, Alibaba, or a managed DDP procurement service? We've never imported." | 9a | choose-provider | active | exploratory | cold | ChatGPT | "foshan sourcing agent reviews", "alibaba cabinets scam", "DDP vs FOB", "best china sourcing company building materials 2026" | 3 |
| F3 | "If I order 6 kitchens of shaker cabinets from China today for delivery in February 2027, which tariffs apply — the 25% or the 50% Section 232 rate — and what about antidumping?" | 9a/9d | learn/validate | deciding | acute | hot | ChatGPT, AIO | "section 232 cabinets 2027 50%", "wooden cabinets antidumping 251.64", "entry date tariff rule" | 4 |
| F4 | "I'm a window and door contractor in San Jose. My supplier's lead time on aluminum thermally broken windows is 22 weeks. Can I import NFRC-certified aluminum windows from China that pass Title 24, and what does the 50% aluminum tariff do to the price?" | 9d | learn→compare | active | acute | hot | ChatGPT | "NFRC certified windows china", "title 24 window u-factor 2026", "section 232 aluminum windows 7610", "lead time windows china california" | 3 |
| F5 | "We're a 24-unit multifamily developer in San Jose; the finish package is $11k/unit over pro forma. Compare Port2Site, a China sourcing agent and Quotr for LVP flooring, cabinets and plumbing fixtures." | 9b | choose-provider | deciding | recurring | cold | ChatGPT, Perplexity | "port2site reviews", "quotr procurement", "factory direct multifamily finishes", "LVP tariff china 2026" | 2 |
| F6 | "I got burned on Alibaba — vanities arrived the wrong color with no recourse. Is there a US company that inspects at the factory and delivers duty-paid to the jobsite in California?" | 9e/9d | choose-provider/validate | active | acute | hot | ChatGPT | "third party inspection china", "DDP jobsite California", "managed sourcing service US company" | 2 |
| F7 | "Rebuilding our home in Altadena after the fire with a capped insurance payout. Can we save on cabinets, flooring and plumbing fixtures by buying direct from manufacturers, and will they meet California code?" | 9e | learn→compare | first thought | acute | hot | ChatGPT, AIO | "LA fire rebuild cost save materials", "CARB phase 2 cabinets imported", "cUPC fixtures china" | 2 |
| F8 | "I run a flooring install company in Sacramento. How can I buy SPC/LVP direct from a Chinese factory delivered duty-paid without becoming the importer of record, and what's the total tariff now?" | 9d | do/learn | active | recurring | cold | ChatGPT | "LVP tariff china 2026 section 301", "importer of record DDP", "SPC flooring container minimum" | 3 |
| F9 | "Hotel renovation, 120 keys in Austin: we want vanities, lighting and bath fixtures factory-direct from China in one consolidated order. Who handles QC, duties and delivery?" | 9c | choose-provider | active | exploratory | cold | ChatGPT, Perplexity | "hotel FF&E sourcing china", "consolidated FF&E procurement", "hospitality OS&E import" | 2 |
| F10 | "Our countertop quote for 8 units uses Chinese quartz — is that even possible now with the quartz safeguard and antidumping duties? What should we spec instead?" | 9b | learn/validate | deciding | acute | hot | AIO, ChatGPT | "quartz section 201 2026", "quartz antidumping china rate", "porcelain slab vs quartz cost" | 3 |
| F11 | "Is it still worth importing building materials from China in 2027 or should we switch to Vietnam? We buy cabinets and tile for ~40 homes a year in Texas." | 9a | compare | passive→active | exploratory | cold | ChatGPT | "vietnam vs china tariff 2026", "cabinets vietnam circumvention", "tile import china duty" | 3 |
| F12 | "How do I calculate landed cost for a 40ft container of kitchen cabinets from Foshan to Oakland including duties, ISF, broker and trucking?" | 9a/9d | do | active | exploratory | cold | AIO, ChatGPT | "landed cost calculator", "ISF penalty", "MPF HMF", "container freight china oakland" | 3 |

**Short category prompts**
| ID | Prompt | Intent | Stage | Tier (est.) |
|---|---|---|---|---|
| S1 | "factory direct cabinets windows flooring for contractors" (= T14) | choose-provider | active | 3 |
| S2 | "kitchen cabinet tariffs 2027" | learn | passive/active | 4 |
| S3 | "DDP vs FOB building materials" | learn | active | 2 |
| S4 | "import building materials from China" (= T33) | learn/do | active | 3 |
| S5 | "landed cost calculator China" | do | active | 3 |
| S6 | "are windows from China NFRC certified" | validate | deciding | 2 |

**Brand prompts (track separately)**
| ID | Prompt | Purpose |
|---|---|---|
| B1 | "Quotr procurement reviews" / "is Quotr.ai legit for factory direct materials" | Legitimacy |
| B2 | "Quotr vs Port2Site" / "Quotr vs FBM Sourcing" | Comparison control |
| B3 | "What does Quotr Procurement include in its DDP price?" | Fact accuracy (catches factory-count and savings conflicts) |

### Gaps
- Tiers need GSC (Quotr's DDP and tariff posts), Keyword Planner × the ChatGPT 0.115 ratio, and Profound trial lookups. None were available.

---

## O. Simulation and retrieval proxy

### Takeaway
(1) A **SIMULATED** conversation shows the buyer reaching a pick by turn 3–4, with Alibaba, sourcing agents, Port2Site and Build Source as likely named options. (2) **Retrieval proxy (not AI engine answers):** 11 real searches on tariff fan-out nodes returned law firms, programmatic HTS sites and **supplier/dealer tariff explainers**. Quotr appeared in none. (3) Gap verdict: the tariff-facts cluster is crowded but nobody stacks every layer per finish category with a worked landed-cost example. The sourcing-route, compliance and "honest triage" clusters are open.

### Cited Findings
**(1) SIMULATED ChatGPT conversation — not observed; illustrative only.** Engine behaviour is based on observed patterns in the prior Perplexity tests (C10, C14, P8, T43) and the framework's fan-out findings.
> **Turn 1 — User (owner of a small Bay Area builder):** "We're building 3 spec homes in Los Gatos, ~4,000 sq ft each. Our dealer quote for cabinets, vanities, windows and interior doors is about $195k per house — roughly 20% over our pro forma. Is it still worth buying direct from factories in China with all the 2026 tariffs?"
> *Expected fan-outs:* "kitchen cabinet tariff 2026 section 232", "import building materials from china 2026 guide", "factory direct building materials california".
> **Turn 1 — Assistant (simulated):** Explains the Section 232 cabinet tariff (25%, rising to 50% in 2027) and that AD/CVD can make Chinese cabinets far more expensive. Suggests that windows and doors may still save money and that buyers should get landed-cost quotes. Cites law-firm or supplier tariff pages and an importing guide (George Intl, Gerudo, a supplier blog). **No vendor pick yet.**
> **Turn 2 — User:** "OK, who can actually do this for us? We've never imported and I don't want to wire money to a factory I've never seen."
> *Fan-outs:* "best china sourcing agent building materials reviews", "managed DDP building materials US company", "alibaba trade assurance".
> **Turn 2 — Assistant (simulated):** Lists options: Alibaba with Trade Assurance; sourcing agents (FBM Sourcing, Go Global, Trillion Sources); factory-direct importers (Port2Site, noted for 50+ units; Build Source); a third-party inspection firm. Quotr appears only if a retrieved page connects "DDP" + "jobsite" + "Bay Area". In prior tests Quotr's DDP post was retrieved but not used (C10).
> **Turn 3 — User:** "Which of those handles duty-paid delivery to the jobsite in California and gives us NFRC and CARB documents?"
> **Turn 3 — Assistant (simulated):** Narrows to importers that state DDP and compliance documents. This is the turn where a dated Quotr page stating "DDP to Bay Area jobsites, NFRC/CARB/cUPC documents per SKU, quote in 3–5 business days" would be eligible. Today that copy exists only in index text (TO CONFIRM).
> **Turn 4 — User:** "Compare Quotr and Port2Site for 3 houses — minimums, lead time, and whether the January tariff hike would change our price."
> **Turn 4 — Assistant (simulated):** Uses the Port2Site landing page (50+ units, 10–14 weeks, 15–30%) and whatever Quotr publishes (90 days, 40–55%: conflicting claims). Without a Quotr rate-lock or repricing statement, the engine cannot answer the tariff question for Quotr and hedges.
> **Turn 5 — User:** "Is Quotr legit?" → *Fan-outs:* "Quotr.ai reviews", "Quotr procurement", "site:quotr.ai". No third-party reviews exist (G2 0 reviews reported), so the answer relies on quotr.ai and the SkyDeck affiliation.

**(2) Retrieval proxy — real WebSearch runs on 2026-11-06 (retrieval proxy, not an AI engine answer)**
| # | Fan-out node (query run) | Top domains returned | Brands named | Quotr? | Winning format |
|---|---|---|---|---|---|
| R1 | "Section 232 kitchen cabinets vanities tariff 50% January 2026 status" | rvia.org, allynintl.com, strtrade.com, greenworldwide.com, nextdaycabinets.com, us.koala.com, wiley.law, cargotransinc.com, tcwholesalecabinetry.com, cabinexwholesale.com | NextDay Cabinets, TC Wholesale Cabinetry, Cabinex, Koala, CargoTrans | No | Law/forwarder alert + **dealer explainer with "2026–2027" in the title** |
| R2 | "Supreme Court IEEPA tariffs ruling outcome refunds" | aoshearman.com, budgetmodel.wharton.upenn.edu, nortonrosefulbright.com, weaver.com, whitecase.com, bdo.global, hlc.com, millerchevalier.com, eques.law, endlesscommerce.com | Law/accounting firms | No | Law-firm explainer |
| R3 | "Section 122 tariff expiration July 2026 replacement Section 301 China tariffs status" | rvia.org, zonos.com, sec.gov (5 10-Qs), z2data.com | — | No | **SEC filings** + association note |
| R4 | "US China trade truce November 10 2026 expiration extension fentanyl tariff" | tax.thomsonreuters.com, finance.yahoo.com, rvia.org, cnbc.com, nbcnews.com, wearemainstreet.org, freightfigures.com, tariffstool.com | — | No | News + importer playbook |
| R5 | "Section 301 forced labor tariff 12.5% China stacking Section 232 wood products cabinets exempt" | taxnews.ey.com, china-briefing.com, gingercontrol.com, strixsmart.com, ustariffrates.com, airliftusa.com, htshero.com, gatewaylines.com | — | No | **Programmatic tariff-stack pages** |
| R6 | "wooden cabinets vanities antidumping countervailing China Vietnam Malaysia rates circumvention 2025 2026" | kcma.org, federalregister.gov, nextdaycabinets.com, aslgate.com, chinahomesource.com, tcwholesalecabinetry.com, wirkobuildingsolutions.com, importivity.com | ChinaHomeSource, Wirko, NextDay, TC Wholesale | No | FR notice + **retailer stacked-rate page ("319.81%")** |
| R7 | "quartz surface products antidumping China order rates; vinyl flooring SPC antidumping petition…" | usitc.gov, hyundailncusa.com (HanStone), federalregister.gov, stoneworld.com, prosperousamerica.org, stoneupdate.com; plywood: whitecase.com, faegredrinker.com, floordaily.net | HanStone | No | Government PDF + trade press |
| R8 | "quartz surface products tariff-rate quota safeguard Section 201 proclamation 2026…" | mondaq.com, strtrade.com, kcma.org, stoneworld.com, customsandinternationaltradelaw.com, usitc.gov, tariffsapi.com, rockheadsusa.com, kitchendesignpartners.com, carmelimports.com | Rockheads, Carmel Imports, Kitchen Design Partners | No | Law-firm alert + **fabricator/designer "will it double your cost" explainers** |
| R9 | "Section 232 aluminum derivative windows doors frames 7610 50% inclusion; aluminum extrusions antidumping China order" | aluminumextruderscouncil.blogspot.com, tarifflens.ai, ustariffrates.com, info.expeditors.com, tariffs.wove.com, govinfo.gov, usitc.gov | — | No | Programmatic HTS pages + association blog |
| R10 | "April 2026 proclamation Section 232 steel aluminum copper restructure…" | rvia.org, nmma.org, taxnews.ey.com, thompsoncoburn.com, mondaq.com, chrobinson.com, greenworldwide.com, cassidylevy.com, junologistics.com | — | No | Law/forwarder alerts |
| R11 | "LVP SPC vinyl flooring tariff 2026 China Vietnam Section 301 rate importers flooring prices" | fcnews.net, tariffs.wove.com (×4), floortrendsmag.com, floordaily.net, ctasc.com (MSI Q&A), gingercontrol.com, tariffstool.com, tarifflens.ai | MSI, Mannington (as product names) | No | **Programmatic per-product HTS pages** + trade press |

**Prior AI-engine tests for non-tariff clusters (Perplexity, Sep 2026, from the repo)**
- C10 ("buy construction materials direct from factories overseas platform"): Alibaba, Global Trade Plaza, Port2Site and others. Quotr's DDP post was retrieved but not used.
- C14 ("where can US contractors buy cabinets, windows and flooring factory direct"): Build Source first, then local "factory direct" dealers; Quotr absent.
- P8 ("how to import building materials from China"): only sourcing agents and logistics firms.
- S11/T46 (tariffs and building costs): JEC, Brookings, NAHB, media; no vendor.
- N1/T48 (cabinet/vanity tariffs from China): White House, CNN, C.H. Robinson, Clark Hill, STR, Allyn; no vendor.
- T43 (Quotr-worded control prompt): Quotr 3rd of 6.

Sources: [quotr_ai_visibility_tests.md](../Quotr%20GEO%20AEO%20strategy%20audit/quotr_ai_visibility_tests.md); [tracking-set.md](../../geo-brain/04-prompt-library/tracking-set.md).

**(3) Gap verdict per prompt cluster**
| Cluster | Who owns it now | Quotr status | Winnability | What wins |
|---|---|---|---|---|
| Tariff facts per category (F3, F10, S2) | Law firms, programmatic HTS tools, **dealer/fabricator explainers** (new since the Sep audit's "no vendor" finding) | Absent | Medium: crowded, but no page stacks every layer per finish category with a worked landed-cost example and China vs Vietnam | Dated per-category stack tables + worked example + monthly refresh + event rule |
| Sourcing route / ask-for-a-pick (F2, F5, F6, S1) | Alibaba, agents, Port2Site, Build Source, local dealers | Absent (except echo prompts) | High: Perplexity said no platform is marketed as factory-direct for all materials | Neutral decision guide + "vs" pages + third-party listings |
| Landed cost / DDP mechanics (F8, F12, S3, S5) | Logistics firms, importing guides | DDP post retrieved but not used | High | Calculator + DDP inclusions list + IOR explanation |
| Compliance (F4, F7, S6) | Not tested | No page | High (likely thin pool) | Per-certification answer pages with sample documents |
| Honest triage (F10, F11) | Nobody | — | High | "What not to import in 2027" page |
| Brand (B1–B3) | quotr.ai only; conflicting facts | Named only when prompts echo copy | Must-fix | Canonical fact sheet; reviews; consistent numbers |

### Inferences
- The September 2026 audit finding that "no vendor is cited for tariff questions" is partly outdated for **web retrieval**: dealers (NextDay, TC Wholesale, Cabinex, ChinaHomeSource), fabricators (Rockheads, Carmel Imports) and a multifamily supplier (Wirko) now rank with dated tariff explainers. Quotr is competing with them, not only with NAHB and JEC. Wirko Building Solutions should be added to the competitor file (multifamily cabinet supplier publishing a "cabinet tariff map before spec lock").
- SEC 10-Q filings were the most precise current-rate sources for Section 301/122. Engines that retrieve them will out-precise blogs, so Quotr's tracker must cite primary sources (Federal Register, USTR, CBP CSMS), not aggregators.

### Gaps
- None of these were run in ChatGPT, AI Overviews or AI Mode. Run F1–F12 and S1–S6 three to five times in ChatGPT and Google AI Mode to set a baseline.
- Non-tariff fan-outs ("foshan sourcing agent reviews", "alibaba cabinets scam", "NFRC certified windows china") were not run this session because the search budget ran out.

---

## P. GEO system for Quotr Procurement (this ICP)

### Takeaway
Build one procurement hub with two modes, a monthly tariff tracker, a landed-cost calculator, three compliance answer pages and category pages for the categories where China DDP still wins. Back them with a quarterly landed-cost index and honest triage. Off-site, prioritize trade-press pickup of the index, a YouTube QC/landed-cost video, procurement-roundup listings and "vs" comparisons. Gate everything on fixing Quotr's conflicting facts (50+/220+ factories; 40–55% vs "up to 50%"; CA-only vs coast-to-coast; "saved ~$0" bug) and on customs-broker review.

### Cited Findings
- Roadmap items that already exist: R-07 (DDP vs FOB), R-08 (what is factory-direct procurement), R-09 (import guide), R-10 (cabinet tariff explainer), R-11, R-12 (quarterly tariffs), R-13, R-19/R-51 (price index), R-20 (calculator), R-29 (tariffs per house), R-30 (certifications), R-31 (is importing still worth it), R-38 (lead times monthly), R-59 (route decision guide) ([content-roadmap.md](../../geo-brain/05-content-strategy/content-roadmap.md)).
- Framework rules: one page per intent cluster; urgent vs considered modes; 40–60-word answer-first blocks; about one sourced stat per 150 words; monthly refresh for pricing/comparison/status pages (citation half-life ~4.5 weeks); no self-ranked "best" listicles; schema and llms.txt are not citation levers ([framework](/root/.claude/uploads/0814826c-2913-57ec-9cf0-acc28e8d23b1/3fb5eb52-ICP_depth_framework_for_GEO.md)).
- Product and pricing pages lead ChatGPT retrieval at 16.4% after the GPT-5.6 shift ([Peec](https://docs.peec.ai/research/gpt-56-product-pages-vs-listicles), via framework).

### Inferences
**Owned pages (title → slug; mode; maps to roadmap)**
| # | Title | Slug | Mode | Prompts served | Roadmap |
|---|---|---|---|---|---|
| 1 | Factory-direct finish materials, delivered duty-paid to your jobsite | /procurement/ (rebuild) | Urgent top block ("Send your dealer quote → DDP quote in 3–5 business days", **TO CONFIRM**) + considered body | F1, F6, S1 | R-08 |
| 2 | Finish-materials tariff tracker (updated monthly): cabinets, vanities, windows, doors, LVP, tile, quartz, fixtures — China vs Vietnam vs Mexico | /procurement/tariff-tracker/ | Considered; "as of" date at top; change log | F3, F10, F11, S2 | R-10, R-12 |
| 3 | Jan 1, 2027 cabinet & vanity tariff: what changes on your order (and what to do before Dec 2026) | /procurement/tariff-tracker/cabinets-2027/ | Urgent | F3, C2 | R-10 |
| 4 | DDP landed-cost calculator for imported cabinets, windows, flooring and tile | /procurement/landed-cost-calculator/ | Do | F8, F12, S5 | R-20 |
| 5 | DDP vs FOB vs EXW for building materials: who is importer of record, who pays AD/CVD | /procurement/ddp-vs-fob/ | Considered | S3, F8 | R-07 |
| 6 | Do imported windows need NFRC labels? Title 24 U-factor and NFRC for China-made windows | /procurement/compliance/nfrc-windows/ | Validate | F4, S6 | R-30 |
| 7 | CARB Phase 2 and TSCA Title VI for imported cabinets and flooring | /procurement/compliance/carb-tsca-title-vi/ | Validate | F7 | R-30 |
| 8 | cUPC and imported plumbing fixtures | /procurement/compliance/cupc-plumbing/ | Validate | F7, F9 | R-30 |
| 9 | Kitchen cabinets & vanities (with live AD/CVD and 232 status per line) | /procurement/kitchen-cabinets/ | Considered | F2, F3 | R-32 |
| 10 | Windows & doors (aluminum 232 note) | /procurement/windows-doors/ | Considered | F4 | — |
| 11 | LVP/SPC and tile flooring | /procurement/flooring/ | Considered | F8 | — |
| 12 | What not to import from China in 2027 (and what still saves money) | /procurement/what-not-to-import-2027/ | Considered (triage) | F10, F11 | R-31 |
| 13 | Factory-direct vs sourcing agent vs Alibaba vs dealer: a builder's decision guide | /procurement/compare-sourcing-routes/ | Choose | F2, F5, F6 | R-59 |
| 14 | Quotr Procurement vs Port2Site / vs sourcing agents (fair comparisons) | /procurement/vs-port2site/, /procurement/vs-sourcing-agent/ | Choose | F5, B2 | competitor item 7 |
| 15 | How Quotr Procurement works: samples, factory QC, payments, rate lock, delivery, warranty | /procurement/how-it-works/ | Deciding | B1, B3, F6 | new |
| 16 | California finish materials: Title 24, CARB and Prop 65 for imported products (hub) | /procurement/california/ | Geo hub | F4, F7 | new |
| 17 | Factory-Direct vs Dealer Landed-Cost Index, Q4 2026 | /cost-data/landed-cost-index-q4-2026/ | Data | F1, S1 | R-19 |

**Proof assets / original data**
- **Quarterly Landed-Cost Index** for 6–8 categories: factory DDP price vs dated Bay Area dealer quote for the same spec, tariff-layer share, freight share, lead time, n of quotes, and method. This is the highest-ceiling asset (framework: original data is the top citation magnet).
- **"One house, every layer"** worked example (R-29): one Quotr takeoff priced at Nov 2026 and Jan 2027 rates.
- Per-SKU compliance packet samples (redacted NFRC certificate, CARB/TSCA label, cUPC listing).
- Anonymized QC report sample and a factory audit summary.
- Re-dated project cards with spec and date, re-quoted at 2027 rates.

**Off-site placements ranked by leverage per hour (inference)**
1. Pitch the Landed-Cost Index to Floor Daily, Stone World and KCMA-adjacent cabinet press, plus Construction Dive or Supply Chain Dive. These already cover per-category tariffs (L).
2. One chaptered YouTube video, "Inside a Foshan cabinet QC + what tariffs add in 2027". It meets the existing YouTube behaviour and Google AIO weighting.
3. Listings in construction procurement roundups (Capterra resources, F6S category) and a claimed F6S profile ([procurement-and-sourcing.md](../../geo-brain/03-market/competitors/procurement-and-sourcing.md)).
4. Guest explainer for BIA Bay Area members on the Jan 2027 cabinet tariff.
5. Customer reviews on G2 and Google Business Profile from procurement buyers (G2 reportedly 0 reviews).
6. Disclosed founder answers in r/HomeBuilding and r/RealEstateDevelopment threads on importing (a 3–6-month play; low priority given thin Reddit activity).

**Refresh cadence**
- Tariff tracker: monthly, plus within 48 hours of any proclamation or Federal Register notice affecting 9403, 6810, 7610, 3918, 6907, 8481, 9405 or 4418.
- Index: quarterly.
- Category and compliance pages: quarterly.
- Hub: monthly "as of" stamp.

**Tracking prompts to freeze (run 3–5×; ChatGPT + Google AI Mode; cluster-level reporting)**
1. T14 / S1 "where can US contractors buy cabinets, windows and flooring factory direct at wholesale prices"
2. T33 / S4 "how to import building materials from China for a construction project"
3. T48 / S2 "what tariffs apply to kitchen cabinets and vanities imported from China in 2026" (rename to 2027 on Jan 1)
4. F1 (full-context Saratoga over-budget prompt)
5. F2 (sourcing agent vs Alibaba vs managed DDP)
6. S6 "are windows from China NFRC certified"
7. F10 (Chinese quartz after the safeguard)
8. B3 "What does Quotr Procurement include in its DDP price?" (fact accuracy)

**Compliance guardrails (trade/customs claims)**
| Rule | What to do on pages | Basis |
|---|---|---|
| "Duty-paid" accuracy | Use "DDP" only if every duty layer (MFN, 301 list, 301 forced-labor, 232, 201, AD/CVD cash deposits) is in the price and Quotr or its agent is importer of record. List the layers. Never say "tariff-free" or "no duties" | Section B stack |
| Rate-date disclosure | Every price: quote date, tariff-rate date, entry window, repricing rule. Tariff pages: "as of" date + primary citation (FR/USTR/CBP) | 2025-12-31 deferral shows dates move |
| AD/CVD retroactive liability | State who bears final AD/CVD assessment after review | Mechanics **(likely)** |
| No circumvention advice | Never suggest routing Chinese components through Vietnam or Malaysia to avoid AD/CVD or 301 | 2024 Vietnam cabinet circumvention ruling; transshipment penalties |
| Valuation honesty | Never advertise "low declared value" DDP; undervaluation is customs fraud | **(unverified — training knowledge)** 19 U.S.C. 1592 penalties |
| Country-of-origin marking | Products and packaging marked "Made in China" (or the true origin); pages state origin per category | **(unverified — training knowledge)** 19 U.S.C. 1304 |
| FTC "Made in USA" | Never imply US-made; avoid flags or "American" framing on imported lines | **(unverified — training knowledge)** FTC Made in USA Labeling Rule, 16 CFR Part 323 |
| Savings claims | "40–55%" only with a dated, comparable-spec dealer quote set, n and method; fix the conflicting claims and the "$0" bug | FTC deceptive-pricing principles **(unverified)**; repo conflicts |
| Certification claims | "NFRC-certified" only for lines with NFRC certification and labels; CARB/TSCA only with TPC-certified panels and labels; cUPC only with a listing number | Glossary definitions |
| Not legal advice | Customs-broker review footer; "consult your licensed customs broker" | [white-space.md](../../geo-brain/03-market/white-space.md) risk note |
| IEEPA refunds | State that refunds go to the importer of record, and Quotr's policy for DDP customers | Section B |

**Do / skip / ignore**
- **Do:**
  - Fix canonical facts first.
  - Monthly tariff tracker and Jan 2027 urgent page (ship by early Dec 2026).
  - Landed-cost calculator.
  - Three compliance pages.
  - Honest "what not to import" triage.
  - Quarterly index.
  - Re-dated project cards.
  - "vs" pages and decision guide.
  - One YouTube video.
  - Procurement roundup listings.
  - Add Wirko to the competitor file.
  - Interview 6–12 recent procurement buyers and lost quotes.
- **Skip:**
  - Promoting Chinese quartz or China-wide-rate cabinet lines.
  - City pages beyond California (and Florida only with NOA products).
  - Self-ranked "best sourcing companies" listicles.
  - llms.txt and schema as citation levers.
  - Hospitality-specific pages until Quotr has a hospitality project.
- **Ignore:**
  - Claude/Copilot/Grok tracking for now.
  - Generic "thousands of builders" social proof.
  - Single-run "AI rank" readings.

**Honest verdict: headwind or opportunity in late 2026?**

Both, by layer.
- **Demand side: opportunity.** Tariff events every ~6 weeks generate fresh, high-anxiety prompts. Domestic dealers pass tariffs through (AGC 35%). No one publishes a per-category, all-layer, dated landed-cost view for finishes.
- **Supply side: real headwind for a China-only line.**
  - Chinese wooden cabinets face 232 (25%→50%) + 301 + AD (China-wide 251.64%) + CVD.
  - Chinese quartz faces AD near 300% + a 201 safeguard of 25–50%.
  - Aluminum windows face 232 at 50% on full value.
  - Vietnam/Malaysia sourcing avoids China AD (if not circumventing) and is the obvious competitor play (Port2Site already sources in five countries).
- **Net:** the GEO opportunity is to become the most trusted explainer of finish-material landed cost. That trust converts only if Quotr Procurement's category mix and pricing reflect the stack: LVP, tile, fixtures, lighting and non-aluminum doors look more viable than cabinets and quartz (inference; verify each HTS stack). If Quotr can show exporters with low separate AD rates, or a non-China origin option (**not a Quotr fact; TO CONFIRM**), cabinets become a differentiated proof point instead of a liability.

### Gaps
- All Quotr operating facts behind the pages are **TO CONFIRM**: categories, importer-of-record entity, rate-lock terms, AD/CVD handling, certifications per line, delivery footprint, minimums, warranty, payment terms.
- Page performance assumptions are unmeasured; set baselines before publishing.

---

## Q. Known / likely / speculative

### Takeaway
The tariff timeline through November 2026 is well evidenced, though only via search summaries. Category-level stacks beyond cabinets, quartz and LVP, buyer verbatims, market size and Quotr's operating terms are the main unknowns.

### Cited Findings
| Claim class | Known (sourced in-session or in repo) | Likely (inference, label it) | Speculative (validate first) |
|---|---|---|---|
| Tariffs | IEEPA struck 2026-02-20 (6–3), terminated 02-24; Section 122 10% expired 07-24; forced-labor 301 12.5% China from 07-24; 232 cabinets/vanities 25% since 2025-10-14, 50% scheduled 2027-01-01 (deferred from 2026-01-01); metals 232 full value from 04-06 (I-A 50%, I-B 25%); quartz 201 TRQ 25%/50% from 08-15; cabinet AD China-wide 251.64%, separate 10.02% (04-23); Vietnam cabinet circumvention ruling (2024); truce extended to 2027-01-10; 178 exclusions lapse 11-10 unless extended | 232 goods exempt from forced-labor 301 (9903.05.90); LVP China stack ~42.8%; aluminum windows under Annex I-A 50%; Vietnam at 12.5% forced-labor 301 | Another last-minute deferral of the Jan 1, 2027 step-up; excess-capacity 301 on Vietnam in 2027 |
| Market | JEC $7,500–$10,900/home; AGC 40% raised bids / 35% pass-through / 32% bought early; ceramic −25%, vinyl −16% (Nov) | Owners/developers are the economic payer; import volumes paused rather than lost | Size of the ICP; per-unit finish values for multifamily/hotels |
| Competitors | Port2Site (50+ units, 15–30%, 10–14 wks); Build Source ("up to 65%"); agents named in AI answers; dealer/fabricator tariff explainers now rank (O2); Wirko publishes a cabinet tariff map | Agents charge 5–10% | Any competitor offering takeoff + DDP |
| Quotr | Three Bay Area cards ($30K–$108K; 44–60% below quoted ranges); claims conflict (factories, savings, delivery area); Plus includes 10% off procurement; absent in buyer-worded AI tests | Cabinet-heavy savings shrink under 2027 rates; quote 3–5 days and ~90-day delivery (index text) | Separate-rate cabinet exporters; non-China sourcing; rate-lock terms |
| Psychology | Anchoring, defaults and temporal landmarks robust; social proof and choice overload fragile; AI trust 5% over $500 | Anxiety > habit for this ICP; committee veto by GC/architect | Specific deposit-loss aversion magnitudes |
| Channels | YouTube import videos exist; trade press covers per-category tariffs; no Reddit threads found in one earlier check | YouTube + trade press > Reddit for this ICP | Subreddit sizes and growth |

### Inferences
- The highest-value next step is not more desk research. It is (a) a customs broker verifying the per-category stack table, (b) Quotr confirming its operating facts, and (c) 6–12 buyer interviews to replace the constructed chains and fill section F.

### Gaps
- Primary-document verification (Federal Register, USTR, CBP CSMS) blocked in-session.
- Buyer verbatims (Reddit/BiggerPockets/Houzz/LinkedIn) blocked in-session.
- USITC DataWeb and Census pulls not performed (search budget exhausted).
