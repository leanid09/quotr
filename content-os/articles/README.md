# Content OS: article drafts (week 1, publish target Monday, November 16, 2026)

Drafted 2026-11-13 from the GEO brain (`geo-brain/`), with time-sensitive facts spot-checked by web search on 2026-11-13. Every draft is **"Draft — needs editor + claim check"**: nothing here is ready to publish until its gates are cleared. Each file holds YAML front matter (gates and `claims_used` for the Claim Ledger), the article, validated JSON-LD, channel adaptations and editor notes.

Word counts are body words from the H1 to the end of the FAQ (excluding the sources list); the figure in brackets includes the sources list.

| ID | Title | Slug | Gates blocking publish | Words |
|---|---|---|---|---|
| [ART-001](ART-001-ai-takeoff-software-pricing-compared.md) | AI takeoff software pricing compared (November 2026): per seat, per project and per square foot | `ai-takeoff-software-pricing-compared` | Quotr.ai Lite AI-detection scope; Estimation Service rate mechanics at 50,000 sq ft, minimum fee, sq ft definition; annual pricing and Plus takeoff credits; standard turnaround; re-check all prices on publish day (PlanSwift tiers, STACK billing); stale Solo/Team pricing removed site-wide first; author sign-off | 1,798 (1,943) |
| [ART-002](ART-002-kitchen-cabinet-vanity-tariffs.md) | Kitchen cabinet and vanity tariffs: what changes on January 1, 2027 and what builders should do now | `kitchen-cabinet-vanity-tariffs-what-builders-should-do` | **Named customs/trade expert review**; re-verify Jan 1, 2027 date on publish day; verify HTS codes, China-wide AD rate (251.64%), Section 301 applicability and stacking, MPF/HMF rates, JEC figures; Quotr Procurement cabinet sourcing, DDP inclusions, rate-change and AD/CVD policy, lead times, delivery area; disclaimer approval | 1,796 (2,039) |
| [ART-003](ART-003-bay-area-factory-direct-finish-materials.md) | What three Bay Area homes paid for factory-direct finish materials (Saratoga, Monte Sereno, Hillsborough) | `bay-area-factory-direct-finish-materials-cost` | **Fix /procurement/ "Client saved ~$0" bug and totals** (sweep row 4); reconcile Myren Dr "~$91,800"; project dates, categories and market-range method; full-DDP confirmation; client permission for street names; lead time, QC, warranty, damage, delivery area, minimums, certifications; verify Port2Site minimum | 1,678 (1,765) |

## How the JSON-LD was built

The `## JSON-LD` block in each draft is generated from the visible H1, front matter and FAQ, so the FAQPage text matches the page word for word. After any edit to an H1, `meta_description` or FAQ, regenerate and re-validate the block (the generator asserts that no FAQ answer contains TO CONFIRM, VERIFY or EXPERT tags, and checks that the JSON parses). The script is not committed; it is a short Python routine.

## Shared open items with Quotr

- One standard Estimation Service turnaround (ART-001).
- Quotr Procurement facts: category list, DDP inclusions, lead times, delivery area, minimum order, warranty and claims (ART-002, ART-003).
- Author pages for Junzhe Shi and Hanyang Liu (schema `url` currently points to LinkedIn).
- A named customs or trade expert reviewer (ART-002; also needed for roadmap items R-12, R-29, R-30).
