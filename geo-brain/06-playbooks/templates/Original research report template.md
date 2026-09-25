---
type: page-template
description: Template for publishing Quotr data as a recurring, citable index or benchmark.
last_verified: 2026-09-25
verify_every_days: 180
---
# Template: Original Research Report (Index or Benchmark)

> [!abstract] What this page is for
> A template for publishing Quotr's own data as a recurring, citable report (for example a "Factory-Direct vs Domestic Materials Price Index" or a residential cost benchmark), with the method, data table and launch plan that make journalists, list editors and AI engines quote it.

> [!info]- Sources
> [[geo_content_playbook_b2b]] (§1 original research and proprietary data; §3 earned media; §5 case studies), [[competitor_geo_benchmark]] (§2 competitor data assets; §3 tariff and cost answers; §5 white space), [[quotr_onsite_content_audit]] (§2 "original data" posts, §3 /procurement/ data), [[verification_geo_evidence]] (claims #9, #17; H2, H11), [[verification_quotr_and_competitors]] (claims 17, 36); [[White space]] ("Data assets Quotr could publish").

---

## 1. Why original data is Quotr's best content bet

- **Primary research gets cited more.** In a Growth Memo sample of 301 AI-cited pages (316 prompts, 7 verticals), only 8 pages were primary research, but they earned 8.4% of citations: 11.3 citations per page vs 3.4 for everything else, about 3.3x (`geo_content_playbook_b2b.md` §1; not re-checked in the verification pass).
- **But data alone is "necessary but not sufficient"** (Growth Memo, June 2026): winners structure proprietary data for extraction (named method, precise numbers, dates) and keep building authority off-site.
- **The format AI rewards most is the benchmark that answers "which is best" or "what does it cost"** (`geo_content_playbook_b2b.md` §1).
- **No software vendor is cited on tariff and material-cost questions today.** For "how are 2026 tariffs affecting building material costs for home builders and multifamily developers", Perplexity cited only public and media sources: the Senate JEC's April 2026 housing report ($7,500–$10,900 per home), Brookings, NAHB, Construction Dive, Skanska, Cushman & Wakefield, HousingWire (competitor benchmark §3). A vendor with dated, first-party price data could become the practitioner source (white space #1).
- **Competitors already use data assets:** Togal's "peer-reviewed" comparative study vs On-Screen Takeoff (University of Kansas; up to 76% faster, within 5%), Handoff's "trained on 68 million construction costs" claim, Meltplan's cost-per-square-foot benchmarks (competitor benchmark §2–3; verification claim 36).
- **Earned media runs on data.** Muck Rack (May 2026) found earned sources make up 84% of AI citations across ChatGPT, Claude and Gemini, with journalism about 27% (PR-vendor study; "earned" is defined broadly, so never paraphrase as "84% is press coverage"; `verification_geo_evidence.md` claim #17, H11). Trade press needs a news hook; a dataset is one.
- **Quotr's current "original data" posts mostly repackage public sources** (e.g., "State of AI in Preconstruction 2026" is built from Deloitte, ENR, Construction Dive and others), while its real proprietary numbers ("$1.2B+ estimated", "300+ projects a month", "95–99% accuracy") appear only as unsupported claims (onsite audit §2).
- **Keep expectations honest:** the "add statistics and sources" lift from the 2023/2024 GEO paper did not hold up in a 2025 peer-reviewed re-test (C-SEO Bench). The value of a report is that it is **genuinely new information others want to cite**, not a formatting trick (`verification_geo_evidence.md` claim #9, H2).

---

## 2. Candidate reports for Quotr (all need data confirmation)

| Report | Data source inside Quotr | Cadence | Prompts it serves | Who would cite it | Status |
|---|---|---|---|---|---|
| **Factory-Direct vs Domestic Materials Price Index** (windows/doors, cabinets, flooring, bath fixtures) | Quotr Procurement quotes vs local dealer quotes | Quarterly | L-084, L-088, L-112, L-113, L-114, L-120 | NAHB, HousingWire, Construction Dive, BIA, builders | **TO CONFIRM with Quotr** |
| **Residential and multifamily cost benchmarks** ($/SF by building type, region, trade) | Quotr Service estimates (Quotr claims "$1.2B+" estimated; no method yet) | Twice a year | L-130–L-134, E-005, E-011 | Developers, lenders, BDC Network, AI cost answers | **TO CONFIRM** |
| **AI takeoff accuracy benchmark** on residential and multifamily plan sets | Internal benchmarking (today: "95–99% on clean vector PDFs", "80–88% on low-resolution scans", no method) | Yearly | L-035, L-039, L-041, D-019 | Estimators, list editors, r/estimators | **TO CONFIRM** method and data |
| **Lead-time tracker** for imported finish materials | Procurement orders | Monthly | L-083, L-118 | Builders, trade press | **TO CONFIRM** |
| **Tariff cost per home example** | One real takeoff × current tariff rates | When tariffs change | L-113, L-114, L-087 | Press, NAHB, BIA | Needs expert/legal review |
| **Bid spread statistics** (how far apart supplier or sub quotes are) | Bid comparison feature | Twice a year | E-012, L-127 | GCs, trade press | **TO CONFIRM** data exists |

(Adapted from [[White space]].)

**Recommended first report:** the **Factory-Direct vs Domestic Materials Price Index**, because it uses Quotr's most distinctive data, sits in an answer space with no vendor, and gives trade press a quarterly hook. Start small: 3–4 material categories, clear definitions, honest sample size.

---

## 3. Required sections, in order

| # | Section | What goes in it |
|---|---|---|
| 1 | **H1** | "[Report name]: [Period] — [headline finding in numbers]" |
| 2 | **Byline, dates, contact** | Named authors (with roles); published date; next release date; media contact |
| 3 | **Key findings** | 3–5 bullets, each one number + one sentence, each quotable alone and naming Quotr ("Quotr.ai's Q4 2026 index found…") |
| 4 | **Headline chart + data table** | The chart, **and** the same numbers as an HTML table (AI engines read tables, not images) |
| 5 | **Method** | Sample (how many quotes/projects), period, geography, definitions (e.g., what "landed cost" includes), data cleaning, what is excluded, who checked it |
| 6 | **Findings by category** | One H2 per category with its table and a 2–3 sentence explanation |
| 7 | **How this compares with public data** | Put Quotr's numbers next to public benchmarks (NAHB, JEC, BLS PPI) with links and dates |
| 8 | **What it means for builders / developers** | Practical implications; honest caveats |
| 9 | **Limitations** | Sample size, selection bias (Quotr's own customers), regional focus |
| 10 | **Download the data** | CSV and PDF; licence and "Cite as: Quotr.ai, [Report], [date], [URL]" |
| 11 | **FAQ** | 4–6 questions journalists and buyers ask |
| 12 | **Previous editions** | Links to earlier periods (same URL pattern, e.g. /research/materials-price-index/ with an archive) |

**URL pattern:** one stable hub URL (e.g., `/research/materials-price-index/`) updated each period, with archived editions below it. No year in the hub slug.

---

## 4. Filled-in example outline: "Quotr Factory-Direct Materials Price Index, Q4 2026"

**Everything in brackets needs Quotr data and sign-off.**

**H1:** Quotr Factory-Direct Materials Price Index, Q4 2026: [Finish materials landed [X]% below Bay Area dealer prices]

**Key findings (pattern):**
- Quotr.ai's Q4 2026 index found that [kitchen cabinets] delivered duty-paid from [Foshan/Guangdong] manufacturers cost [X]% less than [Bay Area] dealer quotes for the same specification ([N] quotes).
- [Windows and doors]: [X]% lower landed cost; average lead time [Y] weeks.
- Tariffs added [Z]% to landed cost compared with Q3 2026 (tariff rates from [official source]).
- [One category where factory-direct did **not** save money, and why.] (Honesty makes the rest believable.)

**Existing data points to build from:** /procurement/ publishes three project comparisons: Myren Dr, Saratoga ($97,000 vs a $187K–$218K Bay Area market price); Stratford Ct, Monte Sereno ($108,290 vs $195K–$245K); Skyfarm Dr, Hillsborough ($30,437 vs $58K–$76K). Fix the page's "Client saved ~$0" display bug and the totals that do not reconcile before citing it (onsite audit §3, §5; verification claim 17).

**Method (pattern):** "[N] quotes for [categories] requested by Quotr Procurement customers between [dates]; dealer comparison quotes from [N] [Bay Area] suppliers for the same specification; landed cost = factory price + freight + duties + customs + delivery to site; excludes installation."

**Public context table:** JEC April 2026 estimate of tariff cost per home ($7,500–$10,900, per the Perplexity-cited report; open the PDF and confirm before quoting), NAHB tariff updates, BLS PPI series for the relevant materials.

---

## 5. Launch plan (the report is only half the work)

| Step | Action | Owner |
|---|---|---|
| 1 | Legal and customer-permission check on every data point | Quotr |
| 2 | Publish the hub page with HTML tables and the CSV | Marketing |
| 3 | Press release on a wire service + direct pitches to Construction Dive, ENR, For Construction Pros, BuilderOnline, HousingWire, BDC Network (see [[Listicle and PR outreach]]) | Marketing / founders |
| 4 | Founder LinkedIn article with the top 3 findings ([[LinkedIn thought leadership]]) | Founders |
| 5 | 3–6 minute YouTube explainer saying "Quotr.ai" aloud, with chapters ([[YouTube video brief template]]) | Marketing |
| 6 | Offer the data to associations that list Quotr as a member (BIA Bay Area, Modular Building Institute; membership **TO CONFIRM with Quotr**) | Founders |
| 7 | Share findings (with disclosure) where builders are already discussing tariffs ([[Reddit and community]]) | Founder / estimator |
| 8 | Update cost guides and comparison pages to cite the index | Marketing |
| 9 | Track: tariff and cost prompts monthly; press mentions; backlinks | GEO lead |

---

## 6. Schema for this page

- Article or BlogPosting with the real authors + BreadcrumbList ([[Schema markup kit]] 5.5).
- Optional schema.org `Dataset` block for the downloadable CSV (name, description, creator = the Organization `@id`, temporalCoverage, distribution with the CSV URL). Validate it in the Schema.org validator.

---

## 7. Pre-publish checklist

- [ ] Data approved by Quotr; customer permissions recorded; data anonymised.
- [ ] Method section states sample, period, definitions, exclusions and limitations.
- [ ] Key findings are one number + one sentence each, naming Quotr.ai.
- [ ] Every chart has the same numbers in an HTML table.
- [ ] Public benchmarks linked and dated.
- [ ] At least one honest "did not save / did not change" finding if the data shows it.
- [ ] CSV download and "Cite as" line.
- [ ] Next release date published and scheduled.
- [ ] Launch plan owners assigned.
- [ ] Hub URL has no year; editions archived beneath it.

---

## Related pages

- [[Cost guide template]] — cost pages that cite the report
- [[Case study template]] — single-customer proof
- [[Listicle and PR outreach]] — pitching the data
- [[White space]] — why tariffs and landed cost are open
- [[Procurement and sourcing players]] — the factory-direct field
- [[Content roadmap]] — when the report is scheduled
