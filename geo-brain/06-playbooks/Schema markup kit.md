---
type: playbook
description: Plain-language schema guide with JSON-LD templates for each page type, and what schema can and cannot do.
last_verified: 2026-09-25
verify_every_days: 180
---
# Schema Markup Kit for Quotr.ai

> [!abstract] What this page is for
> A plain-language guide to structured data ("schema") for Quotr.ai, with ready-to-adapt JSON-LD templates for each page type, the rules for using them, how to validate them, and an honest summary of what schema does and does not do for AI citations.

> [!info]- Sources
> [[quotr_onsite_content_audit]] (§3 schema findings), [[verification_quotr_and_competitors]] (claims 14–15; gaps filled #4), [[geo_ai_citation_signals_2026]] (§1, §3), [[verification_geo_evidence]] (claim #1); [[Entity fact sheet]] (all Quotr values); Google Search Central documentation checked via WebSearch on 2026-09-25: [Organization](https://developers.google.com/search/docs/appearance/structured-data/organization), [Software app](https://developers.google.com/search/docs/appearance/structured-data/software-app), [Article](https://developers.google.com/search/docs/appearance/structured-data/article), [Review snippet](https://developers.google.com/search/docs/appearance/structured-data/review-snippet), [General structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies), [HowTo/FAQ changes (Aug 2023)](https://developers.google.com/search/blog/2023/08/howto-faq-changes), [Simplifying the results page (June 2025)](https://developers.google.com/search/blog/2025/06/simplifying-search-results); [Search Engine Journal: Google drops FAQ rich results (2026)](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/); [Schema.org](https://schema.org/).

---

## IMPORTANT: these are templates

- **Every block below is a template, not finished code.** Values in `[SQUARE BRACKETS]` must be replaced with confirmed facts, or the whole line removed.
- **Never publish a placeholder, a guess or a "TO CONFIRM" value in schema.** Schema that contradicts the page, or states a fact Quotr has not confirmed, is worse than no schema.
- **Validate every block** in the [Google Rich Results Test](https://search.google.com/test/rich-results) and the [Schema.org Markup Validator](https://validator.schema.org/) before and after it goes live (Section 6).
- **All Quotr values** (prices, names, founders, profiles) come from [[Entity fact sheet]]. When a fact changes there, change it here and on the site on the same day.

---

## 1. Structured data in plain English

- **What it is:** a small block of code in a page's HTML that labels the facts on the page for machines. For example: "this page is about a software product called Quotr.ai; it has a plan called Lite; the price is 79.90 US dollars per seat per month."
- **The vocabulary** comes from [Schema.org](https://schema.org/), a shared dictionary of "types" (Organization, SoftwareApplication, FAQPage, BlogPosting) and "properties" (name, price, author).
- **The format** Google recommends is **JSON-LD**: a `<script type="application/ld+json">` block, usually in the page `<head>`. It does not change what visitors see.
- **What it can do:**
  - make some pages eligible for Google "rich results" (enhanced listings such as breadcrumbs, video or review stars);
  - state facts unambiguously (which company, which product, which author, which price), which helps machines connect Quotr.ai's pages and profiles into one "entity";
  - keep facts consistent when many pages describe the same company.
- **What it cannot do:** it does not make a page rank or get cited on its own, and it cannot fix facts that are wrong on the page.

---

## 2. What the evidence says about schema and AI citations

| Source | What it says |
|---|---|
| **Google** (AI optimization guide, May 15, 2026) | Structured data is **not required** and there is **"no special schema.org markup"** for AI Overviews or AI Mode. Google still recommends structured data for rich-result eligibility. Its main instruction is to publish "valuable, unique, non-commodity content" (`geo_ai_citation_signals_2026.md` §1, §3; `verification_geo_evidence.md` claim #1). |
| **Microsoft** (Bing/Copilot, Oct 2025) | Recommends schema markup (FAQ, HowTo, Product, Review) as part of making content easy to parse, alongside clear headings and short sections. A newer May 2026 Microsoft post on how its index supports answers was not read (`geo_ai_citation_signals_2026.md` §1; `verification_geo_evidence.md` O12, M7). |
| **Independent data** | An SSRN cross-platform study (author runs a GEO agency) found a pooled **negative** association between schema and AI citation (odds ratio 0.546), explained by a confound (top-ranking pages carry more schema). The author calls schema "an amplifier, not a driver" (`geo_ai_citation_signals_2026.md` §3). No controlled experiment exists. |
| **Rich results are shrinking** | Google limited FAQ rich results to well-known government and health sites in August 2023 and deprecated HowTo rich results the same year ([Google, Aug 2023](https://developers.google.com/search/blog/2023/08/howto-faq-changes)). FAQ rich results stopped appearing entirely on **May 7, 2026**, with Rich Results Test support removed in June 2026 ([SEJ](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/)). In June 2025 Google also phased out seven lesser-used types (Book Actions, Course Info, Claim Review, Estimated Salary, Learning Video, Special Announcement, Vehicle Listing) ([Google](https://developers.google.com/search/blog/2025/06/simplifying-search-results)). |

**How to explain this to Quotr:**
- Schema is **hygiene**, not a citation lever. Do it because it is cheap, it keeps facts consistent, and some engines (Microsoft) say they use it.
- The biggest schema win for Quotr is **fixing what is wrong today** (conflicting Organization data), not adding more types.
- Never pitch schema as "the thing that gets us into ChatGPT".

---

## 3. Quotr's schema today (September 2026 audit)

| Page | What was found | Problem |
|---|---|---|
| Homepage, /software/, /pricing/ | One Organization block, `@id` `https://quotr.ai/#organization`, `name` and `legalName` both "Quotr.ai", description "Enterprise B2B preconstruction, blueprint takeoff, and estimating software.", `sameAs` linkedin quotrai, youtube @QuotrAI, medium, instagram, x quotr_ai | Wrong `legalName` (should be FLOZ Inc.); /software/ shows prices and an 8-question FAQ but has no SoftwareApplication, Offer or FAQPage; /pricing/ has no Offer either (onsite audit §3; verification claim 14, gaps filled #4) |
| /disambiguation/ | Organization with the **same `@id`** but `name`/`legalName` "FLOZ Inc", `alternateName` ["Quotr","Quotr.ai","Quotr by FLOZ Inc","Quotr.io"], founder Junzhe Shi only, funding entries, `memberOf` SkyDeck Batch 19, 14 `sameAs` URLs including legacy handles (linkedin quotrio, x quotr_io); SoftwareApplication `@id` `https://quotr.ai/#software` whose `sameAs` uses the legacy youtube @QuotrIO, with 4 Offers (Lite 79.90, Plus 299.90, Enterprise, Estimation Service "Standard turnaround is 5-7 days"); FAQPage (8 Q&As); WebPage | Two different names and legal names under one `@id`; founder list leaves out Hanyang Liu; legacy handles; a turnaround that conflicts with the site (3–4 business days, "as fast as 24 hours") |
| Blog posts | Article with `"author":{"@type":"Person","name":"quotr.ai"}`, publisher Organization, `datePublished` = `dateModified` | Author is not a person; dates do not track real updates; no FAQPage despite visible FAQs; no BreadcrumbList |
| Dictionary, trade pages, case studies, tutorials, /service/, /procurement/, /faq/ | **Not verified** (scraper rate limit) | Check with the Rich Results Test before changing |
| Not seen anywhere | Product, HowTo, BreadcrumbList, WebSite, Review/AggregateRating, VideoObject | — |
| Assets | Logo and og-cover image served from `public.quotr.io` (legacy domain) | Move to quotr.ai if possible (**TO CONFIRM with Quotr**) |

---

## 4. Rules for every schema block

1. **Match the visible page.** Every value in schema must also be visible on that page (prices, FAQ answers, author, dates). Google's guidelines require marked-up content to be visible to users ([general guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)).
2. **One thing, one `@id`, one set of facts.** Define the Organization once (site-wide) and **reference** it everywhere else with `{"@id": "https://quotr.ai/#organization"}`. Never define the same `@id` with different values on different pages (today's biggest error).
3. **Use `@graph`** to put related blocks on one page (Organization + WebSite, or BlogPosting + BreadcrumbList).
4. **No fake or borrowed ratings.** Do not add `aggregateRating` or `review` unless genuine user reviews are shown on that page. Google's rules: do not aggregate reviews or ratings from other websites (so never copy G2 or Capterra scores into markup), and organizations cannot mark up reviews about themselves on their own site ("self-serving" reviews) ([review snippet guidelines](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)).
5. **No hidden or invented facts.** No funding amounts, factory counts, HQ address, founding year or turnaround until Quotr confirms them (see the fact sheet's inconsistency register).
6. **Put schema in templates, not by hand.** Quotr's site is built with Astro. The Organization/WebSite block belongs in the shared layout; BlogPosting in the blog post template (pulling the real author and dates from the post's front matter); Offers in the pricing component. This way one price change updates everything.
7. **Dates must be real.** `dateModified` changes only when content changes, and matches the visible "Last updated" date and the sitemap `lastmod`.
8. **Validate, then re-check after deploy** (Section 6).

---

## 5. Which block goes on which page

| Page | Blocks | Template |
|---|---|---|
| Every page (site-wide layout) | Organization + WebSite | 5.1 |
| /software/ and /pricing/ | SoftwareApplication with Offers (+ FAQPage if a visible FAQ exists; + BreadcrumbList) | 5.2, 5.4, 5.7 |
| /service/ | Service with Offers (+ FAQPage) | 5.3, 5.4 |
| /procurement/ | Service (description only; no prices until a price list exists) (+ FAQPage) | 5.3 note |
| Blog posts | BlogPosting with real author + BreadcrumbList (+ FAQPage for visible FAQs) | 5.5, 5.7, 5.4 |
| Author pages (to create: e.g., /authors/junzhe-shi/) | ProfilePage + Person | 5.6 |
| Trade pages (/software/trades/*) | BreadcrumbList (+ FAQPage once FAQs are added) | 5.7 |
| Tutorials and video pages | VideoObject (+ HowTo only for true step-by-step text) | 5.8, 5.9 |
| Dictionary terms | DefinedTerm (optional) + BreadcrumbList | 5.10 |
| /disambiguation/ | Reference the site-wide Organization by `@id`; keep FAQPage for its visible FAQ. **Do not** define a second Organization here | 5.1, 5.4 |
| /about-us/ | Organization is already site-wide; add AboutPage if wanted | — |

---

## 5.1 Organization + WebSite (site-wide)

**Purpose:** one clean, consistent description of Quotr.ai as a company, linked to its official profiles (`sameAs`). Google's Organization documentation lists `name`, `alternateName`, `legalName`, `description`, `url`, `logo`, `foundingDate`, `numberOfEmployees`, `address`, `email`, `contactPoint` and `sameAs` among recommended properties; none is required ([Google](https://developers.google.com/search/docs/appearance/structured-data/organization)).

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://quotr.ai/#organization",
      "name": "Quotr.ai",
      "alternateName": ["Quotr", "Quotr.io"],
      "legalName": "FLOZ Inc.",
      "url": "https://quotr.ai/",
      "logo": {
        "@type": "ImageObject",
        "url": "https://quotr.ai/[LOGO-PATH-TO-CONFIRM].png",
        "width": 512,
        "height": 512
      },
      "description": "Quotr.ai is AI construction takeoff, estimating and bid software, with a done-for-you estimating service and factory-direct material procurement.",
      "founder": [
        {
          "@type": "Person",
          "@id": "https://quotr.ai/authors/hanyang-liu/#person",
          "name": "Hanyang Liu",
          "jobTitle": "CEO"
        },
        {
          "@type": "Person",
          "@id": "https://quotr.ai/authors/junzhe-shi/#person",
          "name": "Junzhe Shi",
          "honorificSuffix": "PhD",
          "jobTitle": "CTO"
        }
      ],
      "memberOf": {
        "@type": "Organization",
        "name": "Berkeley SkyDeck (Batch 19)",
        "url": "https://skydeck.berkeley.edu/"
      },
      "sameAs": [
        "https://www.linkedin.com/company/quotrai",
        "https://x.com/quotr_ai",
        "https://www.youtube.com/@QuotrAI",
        "https://www.instagram.com/quotr.ai",
        "https://medium.com/@quotr-ai",
        "https://www.facebook.com/profile.php?id=61572581013981",
        "https://www.crunchbase.com/organization/quotr",
        "https://pitchbook.com/profiles/company/606944-17",
        "https://www.producthunt.com/products/quotr"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://quotr.ai/#website",
      "url": "https://quotr.ai/",
      "name": "Quotr.ai",
      "publisher": { "@id": "https://quotr.ai/#organization" },
      "inLanguage": "en-US"
    }
  ]
}
```

**Fill-in notes:**

| Property | Status | Action |
|---|---|---|
| `legalName` "FLOZ Inc." | High confidence (/terms, F6S) | Use. Replaces today's wrong "Quotr.ai". |
| `alternateName` | High | Keep "Quotr" and "Quotr.io". Drop "Quotr by FLOZ Inc" (not used anywhere else). |
| `logo` | **TO CONFIRM** | Needs a crawlable logo URL, ideally on quotr.ai (today it is on public.quotr.io). Google asks for at least 112x112 px. |
| `founder` | High (both founders on /about-us/, Crunchbase, LinkedIn) | Use both. The Person `@id`s assume author pages will be created at /authors/…; if not, use `https://quotr.ai/about-us/#hanyang-liu` style IDs instead. |
| `memberOf` SkyDeck Batch 19 | High (SkyDeck Batch 19 page) | Optional. |
| `foundingDate`, `address`, `numberOfEmployees`, `email` | **TO CONFIRM** (2023 vs 2024; San Francisco vs Berkeley; 10 vs 11–50; info@quotr.io vs an @quotr.ai address) | **Leave out** until Quotr decides. Then add, e.g. `"foundingDate": "2023"`, `"address": {"@type": "PostalAddress", "streetAddress": "...", "addressLocality": "...", "addressRegion": "CA", "postalCode": "...", "addressCountry": "US"}`. |
| Funding, "220+ factories", "up to 50%" | Low confidence | **Do not add** to schema. |
| `sameAs` | Current-name profiles from the fact sheet §2b–2c | Include only profiles Quotr controls or that describe Quotr correctly. **Add later:** G2 (once renamed from "quotr-io" and checked), Capterra (once listed), Wikidata (once created, e.g. `https://www.wikidata.org/wiki/Q[ID]`), GitHub only if renamed. **Remove** legacy handles (linkedin quotrio, x quotr_io, youtube @QuotrIO). PitchBook: keep only if Quotr is happy that its corrected profile describes the same company (founding year, HQ and investors currently conflict). |

---

## 5.2 SoftwareApplication with Offers (/software/, /pricing/)

**Purpose:** state the product, category and current prices in one place. Google's software-app rich result requires `name`, `offers.price` and either `aggregateRating` or `review` ([Google](https://developers.google.com/search/docs/appearance/structured-data/software-app)). **Quotr has no on-site reviews, so it will not get a star rich result.** The block is still useful as a machine-readable, consistent statement of price and category.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "@id": "https://quotr.ai/#software",
  "name": "Quotr.ai",
  "url": "https://quotr.ai/software/",
  "applicationCategory": "BusinessApplication",
  "applicationSubCategory": "Construction takeoff and estimating software",
  "operatingSystem": "[TO CONFIRM: e.g. Web browser (Windows, macOS)]",
  "description": "AI takeoff, estimating, bid comparison and proposal software for trade subcontractors, general contractors and developers. Upload PDF or image plan sets; the AI counts symbols, measures lengths and calculates areas, and every quantity stays editable.",
  "publisher": { "@id": "https://quotr.ai/#organization" },
  "featureList": [
    "AI takeoff from PDF and image plan sets (counts, lengths, areas)",
    "AI Agent that answers questions about the drawings",
    "Estimating with your own cost database or the Quotr database",
    "Quote requests and side-by-side bid comparison",
    "Proposal PDF export",
    "Optional factory-direct material procurement"
  ],
  "offers": [
    {
      "@type": "Offer",
      "name": "Quotr.ai Lite",
      "url": "https://quotr.ai/pricing/",
      "price": "79.90",
      "priceCurrency": "USD",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "price": "79.90",
        "priceCurrency": "USD",
        "unitText": "per seat per month",
        "billingDuration": "P1M"
      }
    },
    {
      "@type": "Offer",
      "name": "Quotr.ai Plus",
      "url": "https://quotr.ai/pricing/",
      "price": "299.90",
      "priceCurrency": "USD",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "price": "299.90",
        "priceCurrency": "USD",
        "unitText": "per seat per month",
        "billingDuration": "P1M"
      }
    },
    {
      "@type": "Offer",
      "name": "Quotr.ai Enterprise",
      "url": "https://quotr.ai/book-demo/",
      "description": "Custom pricing for complex teams and higher volume."
    }
  ]
}
```

**Fill-in notes:**
- Prices are **High confidence** as of September 2026 (live /pricing/ and /software/, announced Sep 14, 2026). Update the same day any price changes.
- `operatingSystem`: the "runs in any modern browser … no desktop install" wording was seen only in search-index text of Quotr pages. **TO CONFIRM** before use.
- Enterprise has no price; the Rich Results Test may warn about a missing price. That is acceptable; do not invent one.
- `featureList` must match features shown on the page. Remove any the page does not show.
- **Do not** add `aggregateRating` from G2 or Capterra. **Do not** add annual prices until Quotr publishes them (TO CONFIRM).
- **Do not** put the Estimation Service inside this block as an Offer (the current /disambiguation/ schema does). It is a separate service; use 5.3.

---

## 5.3 Service with per-square-foot Offers (/service/)

**Purpose:** describe Quotr Service (done-for-you takeoffs, estimates and pro formas) and its published rates. `FTK` is the UN/CEFACT unit code for square foot.

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://quotr.ai/#estimation-service",
  "name": "Quotr Service",
  "alternateName": "Quotr.ai Estimation Service",
  "serviceType": "Construction takeoff, cost estimating and pro forma service",
  "url": "https://quotr.ai/service/",
  "provider": { "@id": "https://quotr.ai/#organization" },
  "areaServed": { "@type": "Country", "name": "[TO CONFIRM: United States]" },
  "description": "Done-for-you takeoffs, cost estimates and pro formas prepared by Quotr's team with AI. Pricing is sent before Quotr processes your documents.",
  "offers": [
    {
      "@type": "Offer",
      "name": "Projects under 50,000 sq ft",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "price": "0.25",
        "priceCurrency": "USD",
        "unitCode": "FTK",
        "unitText": "per square foot",
        "eligibleQuantity": { "@type": "QuantitativeValue", "maxValue": 49999, "unitCode": "FTK" }
      }
    },
    {
      "@type": "Offer",
      "name": "Projects of 50,000 sq ft and above",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "price": "0.10",
        "priceCurrency": "USD",
        "unitCode": "FTK",
        "unitText": "per square foot",
        "eligibleQuantity": { "@type": "QuantitativeValue", "minValue": 50000, "unitCode": "FTK" }
      }
    }
  ]
}
```

**Fill-in notes:**
- The rates are **High confidence** (live /pricing/). But /service/ itself says "Pricing is project-based and scales with size, scope, and trades", and does not show the rates. **Show the rates on /service/ first**, then add this block (Rule 1: schema must match the visible page).
- **Do not** add a turnaround time until Quotr picks one (today: 24 hours, 3–4 business days, 1–3 days, 5–7 days and 72 hours all appear).
- **Quotr Procurement:** use the same `Service` pattern (`"name": "Quotr Procurement"`, `"serviceType": "Factory-direct construction material sourcing and delivery"`) with **no** `offers`, factory count or savings figures until those are confirmed.

---

## 5.4 FAQPage (any page with a visible FAQ)

**Purpose:** a machine-readable copy of the questions and answers already shown on the page.

**Important:** FAQ rich results no longer appear in Google (since May 7, 2026). The only reasons to keep FAQPage markup are consistency and machine readability (Microsoft lists FAQ schema among its recommendations). It is optional. **The text must match the visible FAQ word for word.**

Example for /software/ (the first answer is the live /software/ FAQ text as scraped on 2026-09-25. The live FAQ also has "How much does Quotr.ai cost?", but its exact wording was not captured: the second answer below is a placeholder, so replace it with the live answer word for word before publishing):

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://quotr.ai/software/#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is procurement required to use Quotr.ai?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Procurement is fully optional. You can run takeoffs, estimates, and proposals without ever using it — or use Quotr.ai to send quote requests to your own suppliers and compare bids side by side."
      }
    },
    {
      "@type": "Question",
      "name": "How much does Quotr.ai cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Quotr.ai costs $79.90 per seat per month on the Lite plan and $299.90 per seat per month on the Plus plan. Enterprise pricing is custom. Every plan includes AI takeoff and a 7-day free trial."
      }
    }
  ]
}
```

**Rules:**
- Only real questions buyers ask (from the [[Prompt library|prompt library]]), not keyword lists.
- 4–8 questions per page. Do not repeat the same FAQ on many pages.
- See [[FAQ block template]] for writing the visible FAQ.

---

## 5.5 BlogPosting with a real author + BreadcrumbList (blog posts)

**Purpose:** say who wrote the post, when it was published and updated, and where it sits on the site. Google recommends listing every author as a Person with `name`, `jobTitle` and an `url` to their author page, and not merging several authors into one field ([Google Article docs](https://developers.google.com/search/docs/appearance/structured-data/article)).

Example using a real post (Scope gaps, published Sep 10, 2026; the page shows "Last updated September 24, 2026"; onsite audit §1, §3):

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BlogPosting",
      "@id": "https://quotr.ai/blog/scope-gap-construction/#article",
      "mainEntityOfPage": "https://quotr.ai/blog/scope-gap-construction/",
      "headline": "Scope Gaps Cost More Than Pricing Errors",
      "description": "[One-sentence summary that matches the page's meta description]",
      "image": "[TO CONFIRM: https://quotr.ai/... featured image URL]",
      "datePublished": "2026-09-10",
      "dateModified": "2026-09-24",
      "inLanguage": "en-US",
      "author": {
        "@type": "Person",
        "@id": "https://quotr.ai/authors/junzhe-shi/#person",
        "name": "Junzhe Shi",
        "honorificSuffix": "PhD",
        "jobTitle": "CTO",
        "url": "https://quotr.ai/authors/junzhe-shi/",
        "worksFor": { "@id": "https://quotr.ai/#organization" }
      },
      "publisher": { "@id": "https://quotr.ai/#organization" },
      "isPartOf": { "@id": "https://quotr.ai/#website" }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://quotr.ai/" },
        { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://quotr.ai/blog/" },
        { "@type": "ListItem", "position": 3, "name": "Scope Gaps Cost More Than Pricing Errors" }
      ]
    }
  ]
}
```

**Fill-in notes:**
- `author` must be a **real person** shown in the visible byline. Replace every `"name": "quotr.ai"` author. If a post truly has no individual author, use `"author": {"@id": "https://quotr.ai/#organization"}` (an Organization) rather than a fake Person, and fix the byline to match.
- `dateModified` = the visible "Last updated" date = sitemap `lastmod`.
- The author `url` needs a real author page (to create). Until it exists, point `url` to the author's LinkedIn profile (Junzhe Shi: https://www.linkedin.com/in/junzhe-shi/).
- For two authors, use an array: `"author": [ {Person 1}, {Person 2} ]`.

---

## 5.6 Author page: ProfilePage + Person (to create, e.g. /authors/junzhe-shi/)

**Purpose:** one page per author with background and links, so bylines lead somewhere (Google's "Who, How, Why" guidance: bylines should lead to information about the author; [Google helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)).

```json
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "@id": "https://quotr.ai/authors/junzhe-shi/",
  "dateModified": "[YYYY-MM-DD]",
  "mainEntity": {
    "@type": "Person",
    "@id": "https://quotr.ai/authors/junzhe-shi/#person",
    "name": "Junzhe Shi",
    "honorificSuffix": "PhD",
    "jobTitle": "CTO",
    "worksFor": { "@id": "https://quotr.ai/#organization" },
    "alumniOf": { "@type": "CollegeOrUniversity", "name": "University of California, Berkeley" },
    "description": "Co-founder and CTO of Quotr.ai. Background in AI and systems engineering, building algorithms at Apple and UC Berkeley.",
    "sameAs": [
      "https://www.linkedin.com/in/junzhe-shi/",
      "https://scholar.google.com/citations?hl=en&user=Fh8qFr4AAAAJ",
      "https://www.researchgate.net/profile/Junzhe-Shi-2"
    ]
  }
}
```

**Fill-in notes:** The description paraphrases the live /about-us/ page ("building algorithms at Apple and UC Berkeley"). For Hanyang Liu, use the architect background from /about-us/; firm names and degree details are Medium confidence (**TO CONFIRM**). Use one LinkedIn profile per founder (Hanyang Liu has two; pick one: [hanyang-liu1](https://www.linkedin.com/in/hanyang-liu1/) is the one used in the fact sheet).

---

## 5.7 BreadcrumbList (trade pages, product pages)

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://quotr.ai/" },
    { "@type": "ListItem", "position": 2, "name": "Software", "item": "https://quotr.ai/software/" },
    { "@type": "ListItem", "position": 3, "name": "Drywall takeoff and estimating" }
  ]
}
```

**Notes:** the breadcrumb must match the visible breadcrumb trail (add a visible trail if the page has none). The last item can omit `item` (it is the current page).

---

## 5.8 VideoObject (tutorials, case-study videos)

**Purpose:** describe an embedded video so search engines can show it. Ahrefs reports YouTube as the most-cited domain in Google AI Overviews (vendor data, early 2026; see [[YouTube and video]]); marking up the videos Quotr embeds on its own pages is low effort.

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "RL Electric's Quotr Journey: Streamlining Proposals and Takeoffs with AI",
  "description": "[Summary that matches the page text: who RL Electric is, what changed, the numbers they report]",
  "thumbnailUrl": "https://i.ytimg.com/vi/Y2_PUPVtVaE/hqdefault.jpg",
  "uploadDate": "[TO CONFIRM: YYYY-MM-DD from YouTube]",
  "duration": "[TO CONFIRM: ISO 8601, e.g. PT3M20S]",
  "embedUrl": "https://www.youtube.com/embed/Y2_PUPVtVaE",
  "publisher": { "@id": "https://quotr.ai/#organization" }
}
```

**Notes:** `name`, `thumbnailUrl` and `uploadDate` are the core properties. Take the upload date and duration from the YouTube video page. Add a text summary or transcript on the page too; the video file alone gives machines little to quote.

---

## 5.9 HowTo (only for true step-by-step pages)

**Caution:** Google deprecated HowTo rich results in 2023, so this block will not create a rich result. Microsoft still lists HowTo schema among its recommendations. Use it only when the page really is a numbered set of steps, and the steps are visible.

Example skeleton for a trade how-to (steps are generic estimating steps; every number must come from a cited source):

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to do a drywall takeoff from PDF plans",
  "description": "A step-by-step method for measuring drywall quantities from a residential plan set.",
  "totalTime": "[TO CONFIRM: e.g. PT2H for a 2,000 sq ft house]",
  "tool": [
    { "@type": "HowToTool", "name": "PDF plan set (floor plans, elevations, sections)" },
    { "@type": "HowToTool", "name": "Takeoff software, for example Quotr.ai" }
  ],
  "step": [
    { "@type": "HowToStep", "position": 1, "name": "Set the drawing scale", "text": "Check the scale on each sheet and set it in your takeoff tool before measuring." },
    { "@type": "HowToStep", "position": 2, "name": "Measure wall lengths", "text": "Trace every wall that gets drywall, by wall type, and record linear feet (LF)." },
    { "@type": "HowToStep", "position": 3, "name": "Calculate wall and ceiling area", "text": "Multiply wall length by ceiling height and add ceiling areas to get square feet (SF)." },
    { "@type": "HowToStep", "position": 4, "name": "Subtract openings", "text": "Subtract doors and windows according to your company's deduction rule." },
    { "@type": "HowToStep", "position": 5, "name": "Convert to sheets and add waste", "text": "Divide by the sheet size you will hang and add a waste factor of [X]% ([source])." }
  ]
}
```

---

## 5.10 DefinedTerm (dictionary entries, optional)

**Purpose:** label a glossary page as the definition of one term in Quotr's Construction Dictionary. Google has no rich result for this type; it is optional and purely descriptive.

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "@id": "https://quotr.ai/dictionary/ai-takeoff/#term",
  "name": "AI takeoff",
  "description": "AI takeoff is construction takeoff done with software that automatically detects, counts and measures items on digital drawings, which an estimator then checks and edits.",
  "url": "https://quotr.ai/dictionary/ai-takeoff/",
  "inDefinedTermSet": {
    "@type": "DefinedTermSet",
    "name": "Quotr.ai Construction Dictionary",
    "url": "https://quotr.ai/dictionary/"
  }
}
```

**Note:** the `description` must match the definition sentence shown on the page (see [[Glossary entry template]]).

---

## 6. How to validate and deploy (step by step)

1. **Fill the template** with confirmed values from the fact sheet. Delete any line you cannot confirm.
2. **Check the JSON syntax** (a missing comma breaks the whole block). The Schema.org validator shows syntax errors.
3. **Test the code snippet** in the [Schema.org Markup Validator](https://validator.schema.org/): paste the code; fix every error. This checks the vocabulary.
4. **Test in the [Google Rich Results Test](https://search.google.com/test/rich-results):** paste the code or a staging URL. This checks Google's own rules for the types it supports (Organization, SoftwareApplication, Article, Breadcrumb, Video, Review). Fix errors; read warnings (a warning for Enterprise's missing price is acceptable).
5. **Compare with the visible page:** every price, answer, author and date in the schema is visible on the page and identical.
6. **Deploy** through the site template (Astro layout or component), not by pasting into one page.
7. **Re-test the live URL** in the Rich Results Test and view the page source to confirm there is exactly **one** Organization definition.
8. **Check Google Search Console → Enhancements** (breadcrumbs, videos, etc.) a week later for errors.
9. **Log it:** date, page, blocks added, validator results.
10. **Re-check** whenever a fact in the fact sheet changes, and at least quarterly.

---

## 7. Quotr fix plan (in order)

| # | Fix | Effort | Why |
|---|---|---|---|
| 1 | Replace the site-wide Organization with template 5.1 (`legalName` FLOZ Inc.; both founders; current `sameAs`); remove the conflicting Organization definition on /disambiguation/ and reference the `@id` instead | Low | Ends the "two names under one `@id`" conflict |
| 2 | Fix blog author schema: real Person authors; honest `dateModified`; add BreadcrumbList | Low–Medium (template change) | Removes "Person: quotr.ai"; aligns dates |
| 3 | Add SoftwareApplication + Offers (5.2) to /software/ and /pricing/; remove the Estimation Service Offer and the "5-7 days" text from the /disambiguation/ SoftwareApplication | Low | Current prices in one consistent block |
| 4 | Show service rates on /service/, then add Service schema (5.3) | Low | Page and schema agree |
| 5 | Add FAQPage to pages with visible FAQs (/software/, /service/, /procurement/, /faq/, posts) | Low | Optional; consistency |
| 6 | Create author pages with ProfilePage (5.6) | Medium | Makes bylines trustworthy |
| 7 | Add VideoObject to /tutorials/ pages and the RL Electric case study | Low | Video visibility |
| 8 | Move logo and og images from public.quotr.io to quotr.ai (**TO CONFIRM with Quotr**) | Low | Removes a legacy-domain signal |

---

## Related pages

- [[GEO writing style guide]] — writing rules the visible page must follow
- [[Page refresh checklist]] — where schema fits in a page refresh
- [[Page templates]] — each template lists its schema
- [[Wikidata and knowledge graph]] — `sameAs`, Wikidata and profile consistency
- [[Entity fact sheet]] — the only source for schema values
- [[Website audit]] — full technical audit
- [[Myths and risks]] — schema and llms.txt myths
