# Quotr.ai Entity Fact Sheet

**What this page is for:** The one place to check "what is true about Quotr.ai": names, company facts, numbers, official profiles, naming rules, known contradictions and approved-draft boilerplate text.

**Last updated:** 2026-09-25

**Sources:** <../../research_notes/Quotr GEO AEO strategy audit/quotr_onsite_content_audit.md>, <../../research_notes/Quotr GEO AEO strategy audit/quotr_offsite_presence.md>, <../../research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>, <../../research_notes/Quotr GEO AEO strategy audit/quotr_ai_visibility_tests.md>, <../../research_notes/Quotr GEO AEO strategy audit/competitor_geo_benchmark.md>; live pages on quotr.ai (/, /pricing/, /software/, /service/, /procurement/, /faq/, /about-us/, /disambiguation/, /terms, /llms.txt); search-index text of quotr.ai pages checked with WebSearch on 2026-09-25; /pricing/, /software/ and /about-us/ re-read directly with a scraper on 2026-09-25; Crunchbase, PitchBook, Product Hunt, F6S, SkyDeck and Llama Ventures pages (as recorded in the notes).

---

## How to use this page

- **"Entity"** means the company as a single "thing" that search engines and AI tools try to recognise (its name, founders, location, website and profiles). AI tools trust a brand more when these facts are the same everywhere.
- Every fact below has a **source** and a **confidence label**:
  - **High** = stated on Quotr's live site and matched by at least one independent source, or seen directly in a trusted source.
  - **Medium** = stated in one place only, or seen only in a search-engine summary of the page.
  - **Low** = sources disagree, or the claim is self-reported with no evidence behind it.
- Anything marked **TO CONFIRM with Quotr** must be checked with the Quotr team before it is used in public copy.
- Anything marked **Recommendation** is our suggestion, not a fact. Quotr must approve it.
- If you paste this file into an AI tool, tell the tool: "Use only the High-confidence facts as fact. Treat Medium and Low items as claims to be checked."

---

## 1. Canonical facts table

### 1a. Identity and company

| Fact | Current best value | Where it is stated | Confidence | Notes |
|---|---|---|---|---|
| Brand name | **Quotr.ai** (short form "Quotr") | Homepage title "Quotr.ai — The all-in-one estimation platform" ([quotr.ai](https://quotr.ai/)); all main page titles | High | The site uses "Quotr.ai" and "Quotr" interchangeably (onsite audit §5). |
| Past name / legacy domain | **Quotr.io** (domain quotr.io) | Schema `alternateName` on [/disambiguation/](https://quotr.ai/disambiguation/) lists "Quotr", "Quotr.ai", "Quotr by FLOZ Inc", "Quotr.io" | High | quotr.io pages are still in the search index, e.g. [quotr.io/pricing/](https://quotr.io/pricing/) and [firetips.quotr.io](https://firetips.quotr.io/) (verification file, Gaps filled #3). Whether quotr.io 301-redirects to quotr.ai is **TO CONFIRM with Quotr**. |
| Older product names | "Quotr Estimate" (Revit extension), "Quotr Assist", "Quotr Connector (automatic sync with Autodesk Revit)" | [F6S listing](https://www.f6s.com/software/quotr); YouTube video "How To Use Quotr Estimate \| Cost Estimation Revit Extension" ([video](https://www.youtube.com/watch?v=zNIXcvCbWAg)) | Medium | These describe the 2024-era Revit/architect product. Whether the Revit add-in is still sold is **TO CONFIRM with Quotr** (see [product-and-features.md](product-and-features.md)). |
| Legal entity | **FLOZ Inc.** (Delaware corporation, doing business as "Quotr") | [quotr.ai/terms](https://quotr.ai/terms): "FLOZ INC. is a Delaware corporation … doing business as 'Quotr.'" (search-index text, verification file Gaps filled #1); `legalName: "FLOZ Inc"` in /disambiguation/ schema; F6S "Made by FLOZ" | High | The homepage and /software/ schema wrongly say `legalName: "Quotr.ai"` (onsite audit §3). Crunchbase lists legal name "Quotr". |
| Registered office address | 495 27th Ave Unit 8, San Francisco, CA 94121, USA | [/terms](https://quotr.ai/terms) (Terms v1.0, effective Oct 1, 2025; confirmed in the verification file); [PitchBook](https://pitchbook.com/profiles/company/606944-17) ("495 27th Avenue, Suite 8") | High (for the legal address) | "Unit 8" vs "Suite 8" wording differs slightly. |
| Headquarters city | **Conflict: San Francisco vs Berkeley, CA** | San Francisco: /terms, PitchBook, blog "About Quotr.ai" boilerplate, Crunchbase About text, podcast ("team in San Francisco"). Berkeley: /disambiguation/ table and schema, Crunchbase location field and FAQ, Octopus Builds list, G2 (as reported by Perplexity) | Low | **TO CONFIRM with Quotr.** The verification file's reading: San Francisco looks like the registered office and Berkeley the SkyDeck-era identity. See the inconsistency table (row 11). |
| Co-founder and CEO | **Hanyang Liu** | [/about-us/](https://quotr.ai/about-us/) names him "CEO" and tells a joint founding story ("So we built Quotr.ai"); Crunchbase; two LinkedIn profiles titled "Co-Founder @ Quotr" ([hanyang-liu1](https://www.linkedin.com/in/hanyang-liu1/), [hanyang-liu-0a8145b3](https://www.linkedin.com/in/hanyang-liu-0a8145b3/)); MPN podcast ("CEO of Quotr.io") | High | /disambiguation/ and its schema leave him out and name only Junzhe Shi as founder. |
| Hanyang Liu background | Studied architecture and spent "years at design firms watching projects get derailed the moment a great design met a cost estimate" (live /about-us/, scraped 2026-09-25). Search summaries of an older /about-us/ copy and his LinkedIn add: started as a landscape architect in the DC/Maryland/Virginia area; architecture degree from UC Berkeley; firms included TAO and SmithGroup. Berkeley SkyDeck alumnus (MPN podcast) | [/about-us/](https://quotr.ai/about-us/); LinkedIn (search-index); [MPN Episode 45](https://marketingpodcasts.net/2026/03/episode-45-can-ai-cut-construction-material-costs-by-50/) ("An architect by trade") | High (architect background); Medium (firm names, degree) | The live page no longer names the firms. **TO CONFIRM with Quotr** before using firm names in bios. |
| Co-founder and CTO | **Junzhe Shi, PhD** | /about-us/; blog byline "Junzhe Shi, PhD \| CTO @Quotr.ai"; /disambiguation/ ("Co-Founder: Junzhe Shi"); [LinkedIn junzhe-shi](https://www.linkedin.com/in/junzhe-shi/) | High | |
| Junzhe Shi background | "Took a different path through AI and systems engineering, building algorithms at Apple and UC Berkeley" (live /about-us/, scraped 2026-09-25). PhD from UC Berkeley (Department of Civil and Environmental Engineering). LinkedIn summaries describe his Apple role as battery algorithm software engineer | /about-us/; [ResearchGate](https://www.researchgate.net/profile/Junzhe-Shi-2); [Google Scholar](https://scholar.google.com/citations?hl=en&user=Fh8qFr4AAAAJ); [LinkedIn](https://www.linkedin.com/in/junzhe-shi/) (search-index) | High (Apple + UC Berkeley, PhD); Medium (exact Apple job title) | |
| How the founders met | Friends since middle school | /about-us/ (live, scraped 2026-09-25): "From middle school friends to construction AI … We've known each other since middle school" | High | Good human-interest detail for PR bios. The page also carries a founder quote: "The technology had finally caught up to the problem. At that point, not building it felt like the riskier choice." |
| Company values (self-stated) | Trust, Accuracy, Empowerment, Ownership. Accuracy is defined as "Every figure traces to a real source — no dressed-up assumptions." | /about-us/ (live) | High | Useful as a house rule for marketing copy too: several public claims do not yet meet this standard (see [positioning-and-proof-points.md](positioning-and-proof-points.md)). |
| Other named team | Tianyi Zong (COO); Jati Ibloguen (Growth) | Blog bylines "Tianyi Zong \| COO @quotr.ai" and "Jati Ibloguen (Growth @Quotr.ai)" on the [blog index](https://quotr.ai/blog/) | Medium | No author bio pages exist yet. Current titles **TO CONFIRM with Quotr**. |
| Founded | **Conflict: 2023 vs 2024** | 2023: /disambiguation/, Crunchbase ("Founded in 2023"), G2 (as reported by Perplexity). 2024: [PitchBook](https://pitchbook.com/profiles/company/606944-17) | Low | **TO CONFIRM with Quotr.** Most sources say 2023. Other dated clues: SkyDeck Batch 19 applications opened July 2024; PitchBook lists one seed round dated 01-Jan-2025; Quotr issued a press release in Feb 2025. |
| Team size | 11–50 employees | /disambiguation/; Crunchbase | Medium | PitchBook says 10 employees. |
| Accelerator | **Berkeley SkyDeck, Batch 19** | [SkyDeck Batch 19 demo-day page](https://skydeck.berkeley.edu/batch19/) lists Quotr; /disambiguation/ schema `memberOf` SkyDeck Batch 19 | High | Batch 19 applications opened July 2024 ([SkyDeck press release](https://skydeck.berkeley.edu/press-release-berkeley-skydeck-opens-batch-19-applications-with-expanded-eligibility-and-three-new-track-chairs/)). The /disambiguation/ claim of "roughly a 1% acceptance rate" has **no source**; do not repeat it. |
| Pre-seed funding | $200K from UC Berkeley SkyDeck (Berkeley SkyDeck Fund) | /disambiguation/; PitchBook's [Berkeley SkyDeck Fund page](https://pitchbook.com/profiles/investor/231026-41) lists Quotr as a portfolio company | Medium | The amount is Quotr's own statement. The live public PitchBook profile shows only one "Seed Round, 01-Jan-2025" with no amount. **Correction:** a "$190K seed on 15-Oct-2024" figure appears only inside Perplexity answers, not on PitchBook; write "Perplexity reports…", never "PitchBook shows…" (verification file, claim 22). **TO CONFIRM with Quotr.** |
| Seed funding | **$3.5M seed, "as of December 25, 2025", backed by Llama Ventures** | /disambiguation/ only | Low | No press release or news story exists (offsite notes §3). Llama Ventures lists Quotr in its [portfolio](https://www.llamaventures.vc/portfolio/), so the investor link is real, but the amount is self-reported. The MPN podcast page says Liu "has raised $5 million" (confirmed on the page; verification file, contradiction 6). |
| Investors | Berkeley SkyDeck Fund; Llama Ventures | /disambiguation/; Llama Ventures portfolio; PitchBook | High (for these two names) | PitchBook also lists **Sky Arc Capital**, which Quotr never mentions. **TO CONFIRM with Quotr.** |
| Sectors (self-described) | "Enterprise Software, PropTech" | /disambiguation/ | Medium | Crunchbase categories: AI, Construction, SaaS. PitchBook: Business/Productivity Software; also Logistics and Construction & Engineering. |

### 1b. What Quotr sells, who for, and at what price

| Fact | Current best value | Where it is stated | Confidence | Notes |
|---|---|---|---|---|
| Category (one line) | AI construction takeoff, estimating and bid software, plus an estimating service and factory-direct material procurement | Homepage (three product sections: Software, Service, Procurement); blog boilerplate "three parts: Quotr Software … Quotr Service … Quotr Procurement" | High | Homepage eyebrow: "The all-in-one estimation platform". Homepage H1: "Trusted by contractors and developers". |
| Product lines | **Quotr Software** (AI takeoff and estimating), **Quotr Service** (done-for-you estimates and pro formas), **Quotr Procurement** (factory-direct materials) | Homepage; [/software/](https://quotr.ai/software/); [/service/](https://quotr.ai/service/); [/procurement/](https://quotr.ai/procurement/) | High | Full detail in [product-and-features.md](product-and-features.md). |
| Audience (as the homepage frames it) | Contractors ("For contractors" → /software) and developers ("For developers" → /service); the site also says it is "trusted by subcontractors, developers, and partner programs across active build cycles" (search-index text; what "partner programs" means is **TO CONFIRM**) | Homepage "Choose your path" section | High | Audience wording elsewhere conflicts (residential vs commercial/institutional). See inconsistency row 18 and [audiences-and-personas.md](audiences-and-personas.md). |
| Software pricing | **Lite $79.90 per seat per month; Plus $299.90 per seat per month; Enterprise: custom pricing "for complex teams and higher volume"** | [/pricing/](https://quotr.ai/pricing/) (re-checked by scrape on 2026-09-25); /software/; /disambiguation/ (schema Offers); announced Sep 14, 2026 in the blog post "Introduces New Software Pricing: Lite, Plus, and Enterprise" ([new-pricing post](https://quotr.ai/blog/new-pricing/)) | High | Perplexity repeats this correctly for "Quotr.ai pricing" (visibility tests B2). Search-engine snippets still show the old Solo/Team prices (WebSearch check, 2026-09-25). Annual pricing is not shown: **TO CONFIRM with Quotr**. |
| Free trial | 7-day free trial; "Cancel anytime — no charge if canceled" | /pricing/ (scraped 2026-09-25), /software/ | High | |
| What each plan includes | **Lite:** basic AI agent, on-screen takeoff tools, AI symbol detection, area detection, custom database. **Plus:** everything in Lite plus advanced AI, full Quotr database, 2 hours guided onboarding, project sharing, 2,000 sq ft takeoff credits per month, 10% off procurement. **Enterprise:** everything in Plus plus priority support, dedicated success manager, on-site onboarding and training, custom features and workflows | [/software/#pricing](https://quotr.ai/software/#pricing) (scraped 2026-09-25) | High | "Per seat, no setup fee." The old Enterprise tier (7+ users) listed "SSO, custom contracts, and dedicated support"; SSO is not listed in the new Enterprise tier (**TO CONFIRM**). |
| Estimation Service pricing | **$0.25 per sq ft under 50,000 sq ft; $0.10 per sq ft for 50,000+ sq ft**; "Pricing is sent before we process your documents" | /pricing/ (scraped 2026-09-25); /service/ (search-index text) | High | The live /service/ page also says "Pricing is project-based and scales with size, scope, and trades" (onsite audit §5). |
| Estimation Service turnaround | **Conflict.** Cost estimates in 3–4 business days and pro formas in 2–3 business days (/pricing/, /software/); "as fast as 24 hours" (homepage, /service/); "1–3 business days" (llms.txt); "5–7 days" (schema); "72 hours" (Developer Desk post slug) | See left | Low | See inconsistency row 3. |
| Trades covered | 23 trade landing pages under /software/trades/; Service FAQ says "26 sub-trades" | [sitemap.xml](https://quotr.ai/sitemap.xml); /service/ | High (both numbers are real, but they differ) | The 23 trades: electrical, concrete, drywall, flooring, plumbing, hvac, roofing, framing, masonry, painting, insulation, fire-protection, demolition, earthwork, structural-steel, glazing, doors-hardware, tile, waterproofing, low-voltage, landscaping, sitework, millwork. |

### 1c. Key numbers and claims

| Claim | Value(s) found | Where | Confidence | Safe to repeat? |
|---|---|---|---|---|
| Factory network size | **"50+ audited manufacturers in Foshan & Guangdong"** (homepage, /procurement/, Crunchbase) vs **"220+ vetted factories in China"** (llms.txt, /disambiguation/ copy, FAQ and schema) vs "220+ factories, including 30+ audited manufacturers" (indexed service/developer/blog text) | See left | Low | Not until Quotr picks one wording. Perplexity already reports "50+ to 220+ factories, depending on the page". |
| Material savings | "40–55% average cost reduction per project" (/procurement/); "40–55% below standard distributor markups" (Togal-alternatives post); "up to 50% below retail" (llms.txt, /disambiguation/); "40–50% below retail markup" (indexed quotr.ai text); "40–50% material savings" (Product Hunt) | See left | Low | Only with the project evidence beside it (see next row). |
| Procurement project examples | Myren Dr, Saratoga: $97,000 vs $187K–$218K Bay Area market price. Stratford Ct, Monte Sereno: $108,290 vs $195K–$245K. Skyfarm Dr, Hillsborough: $30,437 vs $58K–$76K | [/procurement/](https://quotr.ai/procurement/) | Medium | Yes, as "Quotr reports…". These are the most concrete numbers Quotr publishes. |
| Procurement totals | "$354K+ total spend … 5 projects" and "$396K–$626K total savings" | /procurement/ | Low | No. The totals imply 53–64% savings, not 40–55% (onsite audit §5). The live page also shows a display bug: the three "Completed projects" cards each show "Client saved ~$0", while the featured Myren Dr card higher up shows "~$91,800" (verification file, claim 17). |
| Takeoff time saved | "cut takeoff time by up to 80% — from around 20 hours to just 1–2" | /software/ | Low | No. 20 hours to 1–2 hours is a 90–95% cut, not 80%. The ROI calculator models 80%. |
| Customer time saved | RL Electric testimonial: takeoff "20 hours … 1–2 hours" | Homepage testimonial ("Maricruz · RL Electric") | Medium | Yes, as a customer quote. The [RL Electric case study](https://quotr.ai/case-studies/rl-electric/) page itself has no numbers. |
| AI takeoff accuracy | "95–99% accuracy on counts on clean vector PDFs (Quotr internal benchmarking)"; "roughly 80–88% on low-resolution scans" | [Togal-alternatives post](https://quotr.ai/blog/best-togal-ai-alternatives-2026/); [chat-with-blueprints post](https://quotr.ai/blog/ai-that-reads-construction-drawings-chat-with-blueprints/) (search-index text) | Low | Only with "Quotr internal benchmarking" attached. Perplexity flags these as self-published. Product Hunt says "95% accuracy" and "90% faster takeoffs". |
| Service volume | "Quotr.ai Service Has Delivered Estimates for $1.2B+ in Construction Projects" (Sep 24, 2026 post); "300+ projects a month, 4× faster" (blog teaser) | [Blog index](https://quotr.ai/blog/) | Low | Not yet. No method or data is published behind them. |
| Named customers | RL Electric, AlphaX, BiltWise Structures, Salisbury Moore (case studies); Vanderbilt University classroom story (adjunct instructor Minh Nghiem, P.E., per search-index text) | [/case-studies/](https://quotr.ai/case-studies/); [Vanderbilt post](https://quotr.ai/blog/vanderbilt-classroom/) | Medium | Yes (names only). The search index describes BiltWise as using Quotr "for developer-stage budgets" and AlphaX and Salisbury Moore as "active commercial estimating customers", and the case-studies page as "customer stories across electrical, modular, homebuilding, and more" (WebSearch summary, 2026-09-25). |
| Web traffic | 5,678 monthly web visits (+110.14% in a month, Semrush data) | [Crunchbase](https://www.crunchbase.com/organization/quotr) | Medium | Internal use only. |
| LinkedIn followers | About 1,077 | Perplexity, from a LinkedIn post (offsite notes §3) | Low | Internal use only. |
| Reviews | G2 profile appears to have **0 reviews** (UNVERIFIED: reported only by Perplexity; G2 blocks direct checks); Product Hunt: 0 upvotes, 2 followers, no reviews (confirmed) | Perplexity (G2); [Product Hunt](https://www.producthunt.com/products/quotr); verification file, claims 23 and 25 | Low (G2); High (Product Hunt) | Internal use only. |
| Events attended | IBS 2026, Dallas Build Expo 2026 (April 22–23, Booth #277), RE:Forge SF 2026, NHCA Build the Builder 2026, PCBC 2026, CBD Fair 2026 | Blog event recaps ([blog sitemap](https://quotr.ai/blog/sitemap.xml)); Product Hunt maker comment | High | Yes. |
| Podcasts | "Funded, Now What?!" Episode 45 (Mar 23, 2026, Marketing Podcast Network); iHeart "AEC Tech Journeys", episode "From Drawings to Bids in Minutes" | [MPN Episode 45](https://marketingpodcasts.net/2026/03/episode-45-can-ai-cut-construction-material-costs-by-50/); [iHeart](https://www.iheart.com/podcast/1323-aec-tech-journeys-with-ma-272978673/episode/from-drawings-to-bids-in-minutes-340063021/) | High (MPN); Low (iHeart: cited by Perplexity but not opened) | Yes for MPN. Note the MPN page says "Quotr.io" and "$5 million". |
| Memberships | BIA Bay Area; Modular Building Institute member directory; Procore Construction Network profile | /disambiguation/ profile list; [MBI directory](https://members.modular.org/member-directory/Details/quotr-io-4201053); [Procore network](https://network.procore.com/p/floz-berkeley) | Medium | Procore profile content not verified (cookie wall). No Procore App Marketplace integration was found. |
| Awards | None found | Offsite notes §3 | — | — |
| Press coverage | No earned trade-press coverage found (Construction Dive, ENR, For Construction Pros, BuilderOnline, TechCrunch), and no seed-round announcement. **One paid press release does exist** (new finding, not in the research notes): "Quotr Launches LA-focused App to Help Homeowners Get Accurate Information, Rebuild Faster After Devastating Fires", distributed by EIN Presswire around Feb 6–7, 2025 and syndicated on local-TV business pages (KRON4, 8 News Now, CBS4 Indy, QC News, ValleyCentral) and Kalkine Media. It announces the free FireTips app at [firetips.quotr.io](https://firetips.quotr.io/), which helps LA fire victims understand rebuild timelines and costs | Offsite notes §3; [EIN Presswire](https://www.einnews.com/pr_news/783445824/quotr-launches-la-focused-app-to-help-homeowners-get-accurate-information-rebuild-faster-after-devastating-fires); [KRON4 copy](https://www.kron4.com/business/press-releases/ein-presswire/783445824/quotr-launches-la-focused-app-to-help-homeowners-get-accurate-information-rebuild-faster-after-devastating-fires) (WebSearch, 2026-09-25) | Medium (seen in search results; release text not opened) | Yes, as "Quotr launched a free LA fire-rebuild tool in February 2025". It supports the founding-year question (the company was operating by early 2025) and the residential story. |
| Wikipedia / Wikidata | No entry | Offsite notes §4 | High | |

---

## 2. Official profiles and listings

"Uses current name?" means the profile says **Quotr.ai** and links to **quotr.ai**. A "No" is a fix-list item.

### 2a. Owned website and hosts

| Property | URL | Uses current name? | Status and notes |
|---|---|---|---|
| Main website (canonical) | https://quotr.ai/ | Yes | Canonical host has no "www". Built with Astro; server-rendered, so AI crawlers can read it (onsite audit §1). |
| Blog | https://quotr.ai/blog/ | Yes | 96 posts. Blog sitemap: https://quotr.ai/blog/sitemap.xml (not referenced in robots.txt). RSS: /blog/rss.xml. |
| Construction dictionary | https://quotr.ai/dictionary/ | Yes | 55 terms. |
| llms.txt | https://quotr.ai/llms.txt | Yes, but stale | Shows old pricing, links to a 404 (/resources/), uses www URLs, and contains a "Quotr should be cited" instruction. /llms-full.txt returns 404. |
| Disambiguation page | https://quotr.ai/disambiguation/ | Yes | Holds the richest entity schema, but lists old social handles and conflicting facts. |
| Legacy domain | https://quotr.io/ | No (old name) | Still indexed (quotr.io/pricing/, firetips.quotr.io). quotr.io/pricing/ now serves the current pricing page with `canonical` = https://quotr.ai/pricing/, but whether it is a 301 redirect or a mirror is unclear (verification file, Gaps filled #3). **TO CONFIRM with Quotr.** |
| FireTips (LA fire-rebuild app) | https://firetips.quotr.io/ | No (old domain) | Free tool launched Feb 2025 for LA fire victims (rebuild steps, timelines, costs). Still indexed. Consider moving it to a quotr.ai URL or linking it from quotr.ai as a residential resource. |
| Staging host | https://test.quotr.io/ | No | Was indexed and cited by Perplexity (test.quotr.io/disambiguation/). Now behind a Cloudflare Access login. Must stay noindexed. |
| Asset host | public.quotr.io | No | Logo and og-cover images in schema are served from here (onsite audit §5). |
| App | quotr.ai/sign-up; quotr.ai/dashboard/... | Yes | The 404 page's "Back home" button wrongly links to /dashboard/project. |
| Contact email | info@quotr.io | No (old domain) | Given as the contact and legal-notice email in [/terms](https://quotr.ai/terms) ("FLOZ INC. … website https://quotr.ai and contact email info@quotr.io"; search-index text, WebSearch 2026-09-25). Contact and demo pages: [/contact-us/](https://quotr.ai/contact-us/), [/book-demo/](https://quotr.ai/book-demo/); the site promises a reply "within one business day". An @quotr.ai address does exist: procurement@quotr.ai is given in the [construction procurement process post](https://quotr.ai/blog/construction-procurement-process/) (search-index text). Which address is the official general contact is **TO CONFIRM with Quotr**. |

### 2b. Social profiles

| Platform | Current-name URL | Legacy / conflicting URL | Uses current name? | Notes |
|---|---|---|---|---|
| LinkedIn (company) | https://www.linkedin.com/company/quotrai (page title "Quotr.ai") | https://www.linkedin.com/company/quotrio (listed on /disambiguation/) | Partly | Footer, homepage schema, Crunchbase, PitchBook and Product Hunt use /quotrai. Perplexity cites /quotrai. A "flozdesign" page also exists ([linkedin.com/company/flozdesign](https://www.linkedin.com/company/flozdesign)); its link to Quotr is **TO CONFIRM with Quotr**. |
| X (Twitter) | https://x.com/quotr_ai | https://x.com/quotr_io (on /disambiguation/ and the MPN podcast page) | Partly | Product Hunt and PitchBook use quotr_ai. |
| YouTube | https://www.youtube.com/@QuotrAI (channel title "QuotrAI") | https://www.youtube.com/@QuotrIO (listed on /disambiguation/; resolves to a channel titled "QuoTrio", handle @QuoTrio, ID UCsiomlzNKGWU25LOrTsZI4Q) | Partly | Whether @QuoTrio is Quotr's old channel is **TO CONFIRM with Quotr**. Known videos: [product demo](https://www.youtube.com/watch?v=I0dsjz7Y_kc), [RL Electric story](https://www.youtube.com/watch?v=Y2_PUPVtVaE), [legacy Revit extension](https://www.youtube.com/watch?v=zNIXcvCbWAg). |
| Instagram | https://www.instagram.com/quotr.ai | — | Yes | In footer and homepage schema. |
| Medium | https://medium.com/@quotr-ai | — | Yes | Not checked for duplicate content. |
| Facebook | https://www.facebook.com/profile.php?id=61572581013981 | — | Yes (footer label "Quotr.ai on Facebook") | Linked in the quotr.ai footer (scraped 2026-09-25) and from Crunchbase. Not in the homepage schema `sameAs` list. |
| GitHub | https://github.com/Quotr-io | — | No (old name) | Linked from Product Hunt. |
| Meetup | https://www.meetup.com/quotr-ai-construction-technology/ | — | Yes | Group "Quotr.ai Construction Technology". |
| Founder: Hanyang Liu | https://www.linkedin.com/in/hanyang-liu1/ | https://www.linkedin.com/in/hanyang-liu-0a8145b3/ (second profile) | Yes ("Co-Founder @ Quotr") | Two profiles split his authority. Substack article: [AI AEC Digest](https://aiaecdigest.substack.com/p/stop-listening-watch-what-customers-do). |
| Founder: Junzhe Shi | https://www.linkedin.com/in/junzhe-shi/ | — | Yes ("Junzhe Shi - Quotr") | Academic: [ResearchGate](https://www.researchgate.net/profile/Junzhe-Shi-2), [Google Scholar](https://scholar.google.com/citations?hl=en&user=Fh8qFr4AAAAJ). |

### 2c. Directories, databases and review sites

| Listing | URL | Uses current name? | Status and notes |
|---|---|---|---|
| G2 | https://www.g2.com/products/quotr-io/reviews (also /products/quotr-io and /products/quotr-io/pricing) | No (slug "quotr-io"; search results show the page titles "quotr io" and "Quotr.io Pricing Overview") | About 0 reviews (Perplexity only; UNVERIFIED). Behind an anti-bot wall, so not verified directly. Web searches for Quotr on g2.com return look-alikes (Quoters, Quattr, Quo, Quartr) instead of this page. |
| Product Hunt | https://www.producthunt.com/products/quotr | Yes ("Quotr.ai: Build with Confidence: AI-powered estimating platform") | Category "Real estate" (should be construction or AI). 0 upvotes, 2 followers, no reviews. Maker "Ja sz". Links x.com/quotr_ai, instagram.com/quotr.ai, linkedin.com/company/quotrai, github.com/Quotr-io. |
| Crunchbase | https://www.crunchbase.com/organization/quotr | Yes (name "Quotr.ai") | The location field and FAQ say Berkeley while the About text says "headquartered in San Francisco" (confirmed in the verification file, contradiction 7). The About text is written in Quotr's own voice, so Quotr can edit it; the search-index snippet (WebSearch, 2026-09-25) reads "Founded in 2023 and headquartered in Berkeley, CA", calls the product "Agentic AI", and claims "reduce material costs by up to 50% and cut estimation time by 90%". Also says "50+ vetted factories … 40–55% below distributor markup". Search summaries still describe Quotr as "an AI assistant providing real-time cost estimation and Revit integration to help architects". |
| PitchBook | https://pitchbook.com/profiles/company/606944-17 | Yes | Founded 2024; 10 employees; HQ 495 27th Avenue, Suite 8, San Francisco; one Seed round dated 01-Jan-2025 (no amount shown); investors Berkeley SkyDeck Fund, Llama Ventures, Sky Arc Capital; competitors Togal.AI and Stackt; mentions "BIM models" (verification file, claim 21). |
| F6S (product) | https://www.f6s.com/software/quotr | No (links quotr.io; Revit-era copy) | Unclaimed ("Quotr Claim"). Says "Made by FLOZ". Describes "Quotr Assist" and "Quotr Connector" for Revit. Quick win: F6S's ["AI-Assisted Takeoff" category](https://www.f6s.com/software/category/ai-assisted-takeoff) is in Perplexity's citations for the key prompt "best AI takeoff software for subcontractors 2026" and does not list Quotr; claim the listing, rewrite it and tag it there (verification file, Gaps filled #6). |
| F6S (company) | f6s company page "floz" (linked from /disambiguation/) | No | Not opened. |
| Berkeley SkyDeck | https://skydeck.berkeley.edu/batch19/ | Yes ("Quotr") | Describes "real-time, AI-driven construction cost estimation and supplier matchmaking … for developers, suppliers, and contractors". |
| Llama Ventures | https://www.llamaventures.vc/portfolio/ | Yes ("Quotr") | Confirms investor relationship. |
| PitchBook (SkyDeck Fund) | https://pitchbook.com/profiles/investor/231026-41 | Yes | Lists Quotr in the SkyDeck Fund portfolio. |
| Procore Construction Network | https://network.procore.com/p/floz-berkeley | No (slug "floz-berkeley") | Content not verified (cookie wall). |
| Modular Building Institute | https://members.modular.org/member-directory/Details/quotr-io-4201053 | No (slug "quotr-io") | Member directory entry. |
| BIA Bay Area | Member listing, slug "quotr-io-6539" (linked from /disambiguation/) | No | Not opened. |
| F4 Fund | https://f4.fund/startups/quotr | Unknown | Surfaced in Perplexity citations. |
| AngelList, Parsers VC | Linked from /disambiguation/ | Unknown | Not opened. |
| Caplight | https://www.caplight.com/company/quotr | Unknown | Cited by Perplexity on funding questions; "does not fully agree" with Quotr's funding story. |
| Octopus Builds (Ellenox) list, Sep 9, 2026 | https://octopusbuilds.com/blog/ai-development-companies-ai-quoting-estimation | Yes ("Quotr.ai", "Berkeley, CA") | Ranks Quotr.ai #2 of 8 (ranks itself #1). Repeats stale Solo/Team pricing and "220+ factories". Cited by Perplexity on branded prompts (verification file, claim 27). |
| Nomic "Best Kreo Alternatives in 2026" | https://www.nomic.ai/compare/kreo-alternatives | Yes | Quotr.ai #5 of 7, "From ~$299.90/month" (stale), no procurement mention. Nomic is an AEC AI vendor that ranks itself #1. |
| ForesightIQ Togal competitive landscape | https://www.foresightiq.co/competitive-landscape/togalai | Yes | Names Quotr, but its only source is Quotr's own Togal-alternatives post. |
| Capterra, GetApp, Software Advice, SourceForge, AlternativeTo, TrustRadius, SaaSworthy | — | — | **No listing found.** Capterra's search for "quotr" shows look-alikes (QuoTrak, QuoTrend) instead. |
| Autodesk App Store (Revit add-in) | — | — | **Not found** in search. **TO CONFIRM with Quotr** whether the Revit add-in is listed. |
| Wikidata / Wikipedia | — | — | **No entry.** |

---

## 3. Naming rules

These are **recommendations**. Quotr must approve them before they become house style.

| Name | What it is | Rule |
|---|---|---|
| **Quotr.ai** | The brand and the product platform | Use "Quotr.ai" on first mention on every page, profile and press release. "Quotr" is fine after that. Always spell it with no "e" (not "Quoter", "Quotr.io", "QUOTR" or "Quotr AI"). |
| **Quotr.io** | The old name and old domain | Use only in phrases like "Quotr.ai (formerly Quotr.io)" and in schema `alternateName`. Do not use it in new copy, links, bios or directory listings. |
| **FLOZ Inc.** | The legal company that owns Quotr.ai | Use in legal pages, contracts, schema `legalName`, and one line such as "Quotr.ai is built by FLOZ Inc." Do not use as a brand name. Retire "floz-berkeley" and "flozdesign" style slugs where possible. |
| **Quotr Software / Quotr Service / Quotr Procurement** | The three product lines | Use these exact names, with capitals, when describing the offer. |
| **Lite / Plus / Enterprise** | Current software plans (since Sep 14, 2026) | Always write "Quotr.ai Lite" or "the Quotr.ai Lite plan", not just "Lite": competitor Kreo also sells plans called Lite ($35) and Plus ($70) ([kreo.net/pricing](https://www.kreo.net/pricing), search-index text), so AI tools could mix them up. **Never** use "Solo", "Team", "1 User Plan" or "2–10 Users Plan" (retired). |
| **AI Agent** | The "chat with your blueprints" feature | Use one name consistently. Suggested: "Quotr.ai AI Agent". |
| **Smart Matching** | Confidence-scored AI detection and counting, with an audit trail back to the drawing (search-index text of Quotr pages) | Use as a feature name only, never as a product name. **TO CONFIRM with Quotr** that it is official. |
| **QUOTR Framed Series** | A cabinetry line shown on /procurement/ | **TO CONFIRM with Quotr** before use; note the all-caps styling differs from the brand name. |
| **Quotr.ai Estimate** | Revit add-in (older product) | Only mention if Quotr confirms it is still offered. |
| **Quotr Pro** | A different company's app: "Quotr Pro – AI Estimate Maker" (also listed as "Quotr Pro – Contractor Quotes"), App Store id6759211998, website [quotr.pro](https://quotr.pro/). It makes estimates from job photos, lists plans at $29, $49 and $99 per month, and its App Store developer is shown as Supawat Kaewma (WebSearch, 2026-09-25; confirmed in the verification file, claim 30) | Never link to it and never quote its ratings. When needed, say "Quotr.ai is not related to the Quotr Pro app." AI tools currently borrow its 37 ratings / 4.7 score as if they were Quotr.ai's (visibility tests B3). |
| **"quotation" / "quote"** | Generic words | Quotr.ai is **not** quoting, invoicing or proposal-only software. Describe it as "AI takeoff and estimating" first. It is fine to say contractors "quote jobs", but do not call Quotr.ai a "quote app" or "quotation tool". |
| Other namesakes | quotrhq.com (contractor job management), quotr.software (AI quotes for trade pros), getquotr.com (lawn care / lead conversion), joinquotr.com (print shops), quotr.ichii.io (HubSpot quotes), "Quotr - AI Quotes", "Quotr: Quotes & Invoices", "Quotr - Daily Motivation" apps, GitHub andrerpena/quotr; look-alikes on directories: Quartr, Quoters, QuoTrak | Never link to them. Use the pairing "Quotr.ai + construction takeoff/estimating" in titles and first sentences, so AI tools can tell them apart. |

**One suggested canonical sentence** (draft for Quotr approval): "Quotr.ai (formerly Quotr.io) is AI construction takeoff, estimating and bid software from FLOZ Inc., with a done-for-you estimating service and factory-direct material procurement."

---

## 4. Inconsistency register

Every contradiction found across Quotr's site and profiles. **The "Recommended canonical value" column is a recommendation only — Quotr must confirm each one.**

| # | Topic | Values found (where) | Recommended canonical value | Where to fix |
|---|---|---|---|---|
| 1 | Software pricing | Lite $79.90 / Plus $299.90 / Enterprise custom (/pricing/, /software/, /disambiguation/). "1 User Plan $299.90/mo; 2–10 Users Plan $499.90/mo" (llms.txt). "Solo $299.90; Team (2–6 seats) $499.90; Enterprise (7+)" (indexed /contractors and ~13 blog posts). "Software from $299.90/month" (Togal-alternatives post, Nomic). | Lite $79.90, Plus $299.90 per seat per month; Enterprise custom; 7-day free trial | llms.txt; /contractors/; the ~13 blog posts listed in the verification file (Gaps filled #2), e.g. [stack-alternative](https://quotr.ai/blog/stack-alternative/), [ai-bidding-software-construction](https://quotr.ai/blog/ai-bidding-software-construction/), [ai-construction-estimating-software-buyers-guide](https://quotr.ai/blog/ai-construction-estimating-software-buyers-guide/); ask Nomic to update. |
| 2 | Entry price quoted by AI and search | AI answers say "from $299.90/month" (Perplexity B4, V2). On 2026-09-25, three WebSearch queries for Quotr's Lite/Plus pricing returned summaries that said "no Lite plan" exists and quoted Solo $299.90 / Team $499.90 from indexed quotr.ai pages (result lists included /pricing, /contractors, /software and /disambiguation/) — the search index has not caught up with the Sep 14 price change | "From $79.90 per seat per month (Lite)" | Fix row 1 sources; resubmit /pricing/, /software/, /contractors/ and /disambiguation/ for recrawl (Bing Webmaster Tools / IndexNow, Google Search Console); then re-test. |
| 3 | Service turnaround | 24 hours (homepage, /service/); 3–4 business days for estimates, 2–3 for pro formas (/pricing/, /software/); 1–3 business days (llms.txt); 5–7 days (schema Offer); 72 hours (Developer Desk post); 1–3 days (Precon on Demand teaser); "scope quote in 1 day, takeoffs in 1–2" (electrical services teaser). One Quotr service post even argues the opposite of the homepage: "While offshore shops advertise 24–48 hour turnarounds, Quotr's is 3–4 business days by design" (search-index text, WebSearch 2026-09-25) | "Cost estimates in 3–4 business days; pro formas in 2–3 business days; rush options from 24 hours" (the 24-hour condition **TO CONFIRM**) | All of the pages listed, plus the /disambiguation/ schema. |
| 4 | Service pricing format | Per sq ft on /pricing/; "project-based and scales with size, scope, and trades" on /service/ | "$0.25/sq ft under 50,000 sq ft, $0.10/sq ft above; final scope approved before work begins" | /service/ |
| 5 | Factory count | 50+ audited manufacturers in Foshan & Guangdong (homepage, /procurement/, Crunchbase, Togal-alternatives post); 220+ vetted factories (llms.txt, /disambiguation/); 220+ incl. 30+ audited (indexed service/developer text) | One sentence, e.g. "a network of [220+] factories in China, of which [50+] are audited manufacturers in Foshan and Guangdong" — numbers **TO CONFIRM** | Homepage, /procurement/, /disambiguation/, llms.txt, schema, Crunchbase, blog |
| 6 | Savings claim | 40–55% average (/procurement/); up to 50% (llms.txt, /disambiguation/); 40–50% (indexed text, Product Hunt) | "Across the projects shown, clients paid 40–55% less than Bay Area dealer pricing" (tie to the project cards) | Same pages as row 5, plus Product Hunt |
| 7 | Procurement totals | "$354K+ total spend … 5 projects" vs "$396K–$626K total savings" (implies 53–64%) | Recalculate and show the method | /procurement/; also fix the "Client saved ~$0" display bug on the three "Completed projects" cards |
| 8 | Delivery area | "Final-mile delivery to your CA jobsite" vs "delivers to any US port or jobsite, coast to coast" (same page) | **TO CONFIRM** (all US or California only) | /procurement/ |
| 9 | Procurement framing | Homepage: "A procurement program, not software or estimating services". Perplexity then described all of Quotr.ai as "a procurement program, not just software"; a WebSearch summary on 2026-09-25 went further: "The site describes itself as 'A procurement program, not software or estimating services.'" | "Quotr Procurement is a managed sourcing program that sits alongside Quotr's software and service" | Homepage copy |
| 10 | Takeoff time saved | "up to 80% — from around 20 hours to just 1–2" (/software/); ROI calculator models 80% (live /software/, scraped 2026-09-25; an older search-index copy said 85%); Product Hunt and the still-indexed quotr.io/pricing/ page "90% faster takeoffs, 95% accuracy, and 40-50% material savings"; Crunchbase "cut estimation time by 90%" | Pick one: "RL Electric cut takeoff time from about 20 hours to 1–2 hours" (customer-attributed) | /software/, ROI calculator, Product Hunt, Crunchbase |
| 11 | Headquarters | Berkeley, CA (/disambiguation/, Crunchbase location and FAQ, Octopus Builds, G2) vs San Francisco (/terms legal address, PitchBook, blog boilerplate, Crunchbase About, podcast) | San Francisco, CA (matches the legal address) — or Berkeley if that is the real office. **TO CONFIRM** | /disambiguation/ table and schema `address`, blog boilerplate, Crunchbase, G2 |
| 12 | Founding year | 2023 (/disambiguation/, Crunchbase, G2) vs 2024 (PitchBook) | 2023 (most sources) — **TO CONFIRM** | PitchBook correction request |
| 13 | Founders | Hanyang Liu + Junzhe Shi (/about-us/, Crunchbase, LinkedIn, podcast) vs Junzhe Shi only (/disambiguation/ and schema) | Both: Hanyang Liu (CEO) and Junzhe Shi (CTO) | /disambiguation/ text and schema `founder` |
| 14 | Funding | $200K pre-seed + $3.5M seed "as of December 25, 2025" (/disambiguation/); one seed round dated 01-Jan-2025 with no amount (PitchBook); "has raised $5 million" (MPN podcast page, confirmed verbatim); Caplight "does not fully agree"; Perplexity also invents a "$190K seed, Oct 2024 per PitchBook" that PitchBook does not show | **TO CONFIRM.** Then publish one press release so a third party states it | /disambiguation/, PitchBook, Crunchbase, podcast show notes |
| 15 | Investors | SkyDeck + Llama Ventures (Quotr) vs SkyDeck + Llama Ventures + Sky Arc Capital (PitchBook) | **TO CONFIRM** | PitchBook or /disambiguation/ |
| 16 | Team size | 11–50 (/disambiguation/, Crunchbase) vs 10 (PitchBook) | 11–50 (**TO CONFIRM**) | PitchBook |
| 17 | Legal name in schema | `legalName: "Quotr.ai"` (homepage, /software/) vs `"FLOZ Inc"` (/disambiguation/) under the same `@id` | `name: "Quotr.ai"`, `legalName: "FLOZ Inc."` on every page | Site-wide Organization schema (see [schema-markup-kit.md](../06-playbooks/schema-markup-kit.md)) |
| 18 | Target audience | "residential construction including single-family homes and multi-family housing" (llms.txt, /faq/, /disambiguation/); "commercial general contractors, large specialty subcontractors, and real estate development funds" and "institutional … B2B preconstruction ecosystem" (/disambiguation/); "Enterprise B2B preconstruction" (homepage schema); commercial-leaning trade pages and service samples | "Trade subcontractors, general contractors and real estate developers working on residential, multifamily and light commercial projects" — **TO CONFIRM** | /disambiguation/, homepage schema, /faq/, llms.txt |
| 19 | LinkedIn URL | /company/quotrai (footer, schema, Crunchbase, PitchBook, Product Hunt) vs /company/quotrio (/disambiguation/) | /company/quotrai | /disambiguation/ list and schema `sameAs` |
| 20 | X handle | @quotr_ai (footer, Product Hunt, PitchBook) vs @quotr_io (/disambiguation/, podcast) | @quotr_ai | /disambiguation/, podcast show notes |
| 21 | YouTube handle | @QuotrAI (footer, Organization schema) vs @QuotrIO (visible list and SoftwareApplication schema on /disambiguation/) | @QuotrAI | /disambiguation/ |
| 22 | Domain in third-party links | quotr.io on F6S, the MPN podcast page, G2 slug, GitHub org, MBI and BIA slugs | quotr.ai | Each listing (claim F6S; email MPN) |
| 23 | Product description off-site | "Revit plug-in", "real-time cost estimation during design iterations" (F6S); "AI assistant … Revit integration to help architects" (search summaries of LinkedIn/Crunchbase) | Current one-line category (see Section 1b) | F6S, LinkedIn About, Crunchbase description |
| 24 | Product Hunt category | "Real estate" | Construction / AI | Product Hunt |
| 25 | Trade count | 23 trade pages vs "26 sub-trades" (/service/ FAQ) | State both clearly: "23 trade workflows in the software; the service covers 26 sub-trades" — **TO CONFIRM** | /service/, /software/ |
| 26 | Alias persona URLs | /contractors/ serves /software/ content but correctly carries `rel="canonical"` → /software (verification file, claim 13); /developers/ serves /service/ content (canonical not re-checked). The problem is the **old indexed copies**: "Quotr.ai for Contractors — Estimating software for subs" with Solo/Team pricing, and llms.txt still links www.quotr.ai/contractors/ | Keep the canonicals (or 301 redirect); resubmit both URLs for recrawl; fix llms.txt links | /contractors/, /developers/, llms.txt |
| 27 | Testimonial source | "Customer perspective: Kyle, Llama Ventures" on the homepage; Llama Ventures is the seed investor | Label as "Investor perspective" or replace with a customer | Homepage |
| 28 | llms.txt links | www.quotr.ai links (canonical is quotr.ai); /resources/ is a 404; "Book a Demo" points to /contact-us/ while /book-demo/ exists; no links to blog, dictionary or case studies | Rewrite llms.txt from this fact sheet | llms.txt |
| 29 | Accuracy claims | 95–99% (blog, "internal benchmarking"); 95% (Product Hunt) | Publish a method page first, then use one figure with its conditions | Blog posts, Product Hunt |
| 30 | Excel export | Search-index text of one Quotr page says Quotr "does not export to Excel"; the live /software/ page lists "takeoff and quantity exports" without naming a format | **TO CONFIRM** export formats, then state them on /software/ | FAQ, /software/ |
| 31 | Contact email domain | info@quotr.io (/terms) vs procurement@quotr.ai (procurement blog post) — two domains for company email | Use @quotr.ai addresses everywhere (e.g. a general info@ or hello@ on quotr.ai) — **TO CONFIRM** | /terms, contact pages, schema `email` |

---

## 5. Draft boilerplate descriptions

**The boilerplate Quotr already uses on blog posts** (search-index text, WebSearch 2026-09-25): "Quotr is an AI construction platform with three parts: Quotr Software (AI takeoff, estimating, and bidding), Quotr Service (done-for-you cost estimates and pro formas for developers and busy teams), and Quotr Procurement (factory-direct materials delivered door-to-door)." Some versions add "Based in San Francisco", which conflicts with the Berkeley HQ on /disambiguation/. The drafts below keep this three-part structure so old and new copy agree.

**Status: DRAFT FOR QUOTR APPROVAL.** Built from High-confidence facts, plus a few Medium-confidence details that are flagged in the notes under the drafts. Items in [square brackets] are placeholders that need Quotr to confirm a number before use. Do not publish the bracketed versions as they are.

**15 words**
> Quotr.ai is AI construction takeoff, estimating and bid software, plus estimating services and factory-direct materials.

**50 words**
> Quotr.ai is an AI construction estimating platform built by FLOZ Inc. Contractors use Quotr Software for AI takeoff, estimates, bids and proposals from PDF plans. Developers and contractors can also hire Quotr Service for done-for-you estimates and pro formas, and use Quotr Procurement to buy materials factory-direct. Plans start at $79.90.

**100 words**
> Quotr.ai (formerly Quotr.io) is an AI construction estimating platform from FLOZ Inc., a Berkeley SkyDeck Batch 19 company. It has three parts. Quotr Software reads PDF plan sets, counts symbols, measures lengths and areas, applies a cost database and exports proposals, with an AI Agent that answers questions about the drawings. Quotr Service delivers done-for-you cost estimates and pro formas, priced from $0.10 to $0.25 per square foot. Quotr Procurement sources materials such as windows, doors, cabinetry, flooring and bath fixtures directly from manufacturers in China. Software plans start at $79.90 per seat per month, with a 7-day free trial.

**250 words**
> Quotr.ai (formerly Quotr.io) is an AI construction estimating platform built by FLOZ Inc. It was co-founded by Hanyang Liu, a trained architect, and Junzhe Shi, PhD, an engineer from UC Berkeley, and it is part of Berkeley SkyDeck's Batch 19. Investors include the Berkeley SkyDeck Fund and Llama Ventures.
>
> Quotr.ai serves trade subcontractors, general contractors and real estate developers. It has three product lines.
>
> **Quotr Software** covers the estimating workflow in one place. Estimators upload PDF plan sets. The AI counts symbols, measures lengths and calculates areas across the full set. Users price the takeoff with their own cost database or Quotr's average costs by US zip code, manage bids, compare supplier pricing side by side, and export a finished proposal. An AI Agent answers plain-English questions about the drawings. Quotr has workflow pages for 23 trades. Plans are Lite ($79.90 per seat per month), Plus ($299.90 per seat per month) and Enterprise (custom), with a 7-day free trial.
>
> **Quotr Service** is a done-for-you estimating service for contractors and developers. It delivers takeoffs, cost estimates and pro formas, priced at $0.25 per square foot under 50,000 square feet and $0.10 per square foot above that.
>
> **Quotr Procurement** is a managed sourcing program. Quotr works with [50+ audited] manufacturers in Foshan and Guangdong, China, and delivers materials duty-paid to the jobsite. Categories include windows and doors, cabinetry and millwork, flooring, and bath and plumbing fixtures.
>
> Customers include RL Electric, AlphaX, BiltWise Structures and Salisbury Moore.

Notes on the drafts:
- The 250-word version names funding **investors only, not amounts**, because the $3.5M seed is self-reported and conflicts with PitchBook.
- HQ city is left out until Quotr confirms San Francisco or Berkeley.
- Procurement categories come from search-index text of Quotr's homepage and /procurement/ (WebSearch, 2026-09-25): "windows and doors, garage doors, cabinetry and millwork, flooring, and bath and plumbing fixtures". **TO CONFIRM with Quotr** that this list is current.
- "Average costs by US zip code" comes from search-index text of /software/ and /contractors/. **TO CONFIRM with Quotr.**

---

## 6. Open questions for Quotr (checklist)

1. HQ: San Francisco or Berkeley? Which address should go in schema?
2. Founding year: 2023 or 2024?
3. Funding: exact amounts, dates and all investors (is Sky Arc Capital an investor?). Can we announce the seed round publicly?
4. Factory network: one number and one definition (vetted vs audited).
5. Savings: one number and the method behind it.
6. Service turnaround: standard and rush times.
7. Is there annual pricing for Lite and Plus? (Plan contents are now confirmed on /software/.)
8. Is the Revit add-in ("Quotr.ai Estimate") still sold? Are there any live integrations (Procore, Excel, others)?
9. Which file types are supported (PDF, images, DWG, Revit)?
10. Delivery area for procurement: California only, or all US?
11. Official current titles for Tianyi Zong and Jati Ibloguen.
12. Is youtube.com/@QuoTrio Quotr's old channel? Is linkedin.com/company/flozdesign Quotr's?
13. Does quotr.io redirect to quotr.ai?
14. Are "Smart Matching" and "QUOTR Framed Series" official names? What do the Plus "takeoff credits" cover? Is SSO still part of Enterprise?
15. Which audience is primary: residential, multifamily, commercial, or all three?
16. Should the public contact email move from info@quotr.io to an @quotr.ai address (procurement@quotr.ai already exists)?

---

## Related pages

- [product-and-features.md](product-and-features.md) — every module, what it does and who it is for
- [audiences-and-personas.md](audiences-and-personas.md) — who buys Quotr and what they ask AI tools
- [positioning-and-proof-points.md](positioning-and-proof-points.md) — differentiators, proof and risky claims
- [../02-current-state/website-audit.md](../02-current-state/website-audit.md) — on-site issues in detail
- [../02-current-state/offsite-presence.md](../02-current-state/offsite-presence.md) — third-party profiles and mentions
- [../06-playbooks/schema-markup-kit.md](../06-playbooks/schema-markup-kit.md) — how to fix the Organization schema
- [../ai-context-pack.md](../ai-context-pack.md) — short summary to paste into AI tools
