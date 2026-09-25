# QA Log

**What this page is for:** The record of the quality check run on this knowledge brain on 2026-09-25. It covers what was checked, what each QA pass fixed, what the final integration pass fixed, the link-check result, and the consolidated **TO CONFIRM with Quotr** list. That list doubles as the consultant's question list for Quotr.

**Last updated:** 2026-09-25

**Sources:** the five section QA reports (condensed below); the fact-checks [verification_quotr_and_competitors.md](<../../research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>) and [verification_geo_evidence.md](<../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>); the reviewed report [Quotr GEO AEO strategy audit.md](<../../reports/Quotr GEO AEO strategy audit.md>); the raw notes in `research_notes/Quotr GEO AEO strategy audit/`; [../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md).

---

## 1. Summary

| Item | Result |
|---|---|
| Date of check | 2026-09-25 |
| Scope | All Markdown files in `geo-brain/` (63 section pages, plus the 5 root and `_meta` files added in the final pass) |
| Passes | Five section QA passes, then one integrator and final-editor pass |
| Ground truth used, in order | (1) the two fact-check files, (2) the reviewed report, (3) the raw research notes, (4) the entity fact sheet |
| Headline numbers | Consistent across the brain (table in §4) |
| Structure | Every page has an H1, "What this page is for", "Last updated", a Sources line and Related pages at the end |
| Final link check | **0 broken relative links** across 68 files (see §5) |
| Open questions for Quotr | 42, listed in §6 |

---

## 2. What each QA pass checked and fixed (condensed)

### Pass 1: Quotr and current state (`00-quotr`, `02-current-state`)
- **Off-site presence:** applied the fact-check. Three outside pages are confirmed to name Quotr (Nomic, Octopus Builds, ForesightIQ), and none is independent. Octopus Builds is now shown as read (#2 of 8; it repeats the old Solo/Team pricing, "220+ factories" and "Berkeley, CA"). Four Perplexity-reported listicles are marked UNVERIFIED. The PitchBook seed round is resolved (01-Jan-2025, no amount; "$190K" appears only in Perplexity answers). The podcast's "$5 million" is confirmed. G2 ownership of Capterra, GetApp and Software Advice is confirmed. STACK's reviews are about 1,400 on Capterra and under 100 on G2. The paid EIN Presswire release (Feb 2025, FireTips app) was added.
- **Audiences:** corrected the budget maths. Lite (about $959 per seat per year) is *below* Capterra's $1,600–$4,000 band. Unchecked surveys are labelled.
- **Baseline, website audit, scorecard, tactics review:** fixed the Search Console date (worldwide since Aug 31, 2026) and the Bing date (Feb 10, 2026, preview). Marked G2 "0 reviews" UNVERIFIED. /contractors/ is confirmed as a canonical alias of /software. Group C has 10 old-price posts. Added the "~$91,800" nuance to the "$0 saved" bug. The stale-price wording is now "about 13 Quotr URLs (mostly blog posts, plus the indexed /contractors copy) and llms.txt", with an effect of "nearly four times".
- **Fact sheet:** verified /terms wording; Crunchbase shows both HQ cities; replaced a broken link.
- **Other:** the "$249 annual" rate belonged to the old "1 User Plan"; Beam's turnaround range; tone softened; glossary terms added.

### Pass 2: Market and prompts (`03-market`, `04-prompt-library`)
- Fixed "Gartner network" labels (G2 owns the sites since the January 2026 deal).
- Aligned "pages that mention Quotr" with the fact-check everywhere, and added the ForesightIQ caveat (its only source is Quotr's blog).
- STACK review counts corrected; the invented "G2 73–93" range was removed.
- Added Quotr's own competitor errors (PlanSwift called "a Trimble product"; an out-of-date STACK price).
- Headline numbers made explicit (1 of 32 vs 10 each; share of voice about 0.7% explained).
- Togal fix list corrected; Togal study details added (University of Kansas; up to 76% faster; within 5%).
- /blog/plug-number-estimating/ flagged as a 404. The prompt-library summary was recounted by script (127 existing pages fit; 64 need work). The tracking set is 53 prompts (45 unbranded).
- RL Electric's "20 hours to 1–2" is from the homepage testimonial, not the case study.
- Beam AI's $30.5M Series B and Handoff's $5.8M round spot-checked and confirmed.

### Pass 3: Fundamentals and measurement (`01-geo-fundamentals`, `07-measurement`)
- Test cadence aligned with the tracking set in four files.
- "Cited" vs "in the source list" separated: 4 of 32 (12.5%) and 6 of 32 (18.8%). A "Retrieval rate" glossary entry was added.
- The LA-rebuild prompt was separated from the 8 how-to prompts. Single-session results labelled (P5, V3; C12 reproduced).
- Double count fixed (~13 URLs already include /contractors).
- Claims widened to "AI engines" were narrowed back to Perplexity. ConstructConnect is flagged as a vendor list.
- Weak-evidence labels added (G2 count, Conductor and Similarweb, surveys, Ahrefs llms.txt 97%, Profound wording). The FTC penalty is now "more than $50,000, adjusted yearly". Scrunch is described as "Sitecore announced it is buying Scrunch (June 2026)". The scorecard cadence is monthly. 16 plain-text source references converted to links.

### Pass 4: Strategy and plan (`05-content-strategy`, `08-action-plan`)
- The "94–99%" accuracy figure was replaced with an "[approved figure]" placeholder in the sample sentences. quotr.io/pricing/ was removed from the stale-price list (it now serves current prices).
- Search-index claims hedged (Bing and ChatGPT; Claude and Brave).
- References disambiguated as "Quotr fact-check" vs "GEO-evidence fact-check"; four wrong claim numbers fixed.
- Broken links removed; the meeting brief was toned down and its unsupported comparisons labelled. The effort split now sums to 100%. PitchBook, Sky Arc Capital and the employee count were added to task A13.
- Unchecked vendor studies labelled; jargon lists added.

### Pass 5: Playbooks (`06-playbooks`)
- Headline test numbers added to the outreach playbook and best-of template.
- The AEC Tech Journeys podcast was changed from "appearance" to "cited by Perplexity; not opened; TO CONFIRM". YouTube is now "never cited in any of the 45 Perplexity runs". BIA membership is TO CONFIRM.
- Single-session results labelled (V1, V3, P5, C13). The PlanSwift $1,749 price is attributed to a Perplexity answer.
- Retired-plan labels fixed. Schema kit handles and FAQ note corrected. Wikidata funding and factory rows corrected. Invented "finish materials" removed. Wrong prompt ID fixed (L-011).
- Spot-checks confirmed: FAQ rich results ended May 7, 2026; G2's $100 incentive cap; Wikidata P12689 is the PitchBook ID.

---

## 3. Fixes made in the final integration pass

| # | File(s) | Fix | Why |
|---|---|---|---|
| 1 | `03-market/competitors/beam-ai.md` | "Beam says 1–4 days … consistently" now notes Beam's own variation (24–72 h, 24–48 h) | Contradicted the page's own table |
| 2 | `06-playbooks/offsite/review-generation.md` | "Gartner Digital Markets sites" now reads "former Gartner Digital Markets sites, which G2 now owns" | G2 ownership (January 2026 deal) |
| 3 | `04-prompt-library/tracking-set.md` | Added: the two meanings of "cited" (6 of 32 in the source list; 4 of 32 in the answer text); how engines are counted (five surfaces, four monthly engine runs); a note that Claude and Copilot run quarterly, which departs from the report's all-six monthly advice, with a full six-tool baseline in October and each quarter; AI Overviews, Claude and Copilot rows in the monthly summary template | Cross-folder issues from passes 3 and 4 |
| 4 | `08-action-plan/30-60-90-plan.md`, `08-action-plan/meeting-brief.md`, `05-content-strategy/top-of-funnel-strategy.md` | "About 50 questions across six AI tools" and "test across six engines" now match the tracking set (53 prompts; four engines monthly; Claude and Copilot quarterly; six-tool October baseline) | Consistency with the tracking set |
| 5 | `02-current-state/geo-tactics-already-used.md` | "No competitor has written a page about Quotr" became "no competitor comparison page targeting Quotr was found". Tactic 26's "10 carry stale prices" was recounted against the website audit's group C (10 confirmed, plus 3 alternatives posts and the /contractors copy). The fix list now includes /contractors. The accuracy figure is labelled as Perplexity's wording (94–99%) against Quotr's own (95–99%; 80–88% on scans) | Passes 3 and 4; the notes support only the narrower claim |
| 6 | `03-market/white-space.md` | Accuracy wording as in #5; "BIA Bay Area (Quotr is a member)" became TO CONFIRM | The BIA listing was never opened |
| 7 | `03-market/citation-sources-map.md` | "G2 (0 reviews)" is now UNVERIFIED (Perplexity only). "BIA Bay Area (member), MBI (member)" is now "listed; TO CONFIRM" | Pass 5 |
| 8 | `05-content-strategy/offsite-earned-media-plan.md` | "Associations Quotr belongs to" became "Associations Quotr lists", with TO CONFIRM | Pass 5 |
| 9 | `02-current-state/offsite-presence.md` | The G2 "0 reviews" summary line is labelled UNVERIFIED | Consistency |
| 10 | `03-market/competitor-landscape.md` | "4,205 G2 reviews" for Procore is now "4,205 reviews per ConstructConnect (review site not re-checked)" | ConstructConnect mislabels review sites (it called STACK's Capterra count a G2 count) |
| 11 | `00-quotr/positioning-and-proof-points.md` | "Reads as manipulation" became "Can read as an attempt to steer AI answers" | House tone rule |
| 12 | 60 files | Converted **294** plain-text source references such as `<../../research_notes/…md>` into clickable Markdown links. They were not links in standard Markdown, because autolinks need a full web address | All note and report references now resolve and can be clicked |
| 13 | `08-action-plan/*`, `00-quotr/entity-fact-sheet.md` | Restored links to the new [../README.md](../README.md) and [../ai-context-pack.md](../ai-context-pack.md); the fact sheet now links to this QA log | These files now exist |
| 14 | New files | [../README.md](../README.md), [../ai-context-pack.md](../ai-context-pack.md), [../sources.md](../sources.md), this QA log, [changelog.md](changelog.md) | Integration deliverables |
| 15 | `00-quotr/audiences-and-personas.md`, `00-quotr/entity-fact-sheet.md` | "Quotr is a BIA Bay Area member" now says the membership is listed on /disambiguation/ and is TO CONFIRM; the fact sheet's Memberships row says the same for both BIA and MBI | Same issue as #6–8, found in the final sweep |
| 16 | `02-current-state/offsite-presence.md` and others | Final sweep for known error phrases ("Gartner network", "PitchBook shows $190K", PlanSwift "Trimble", unhedged HQ, founding year or factory counts, price variants). Only quoted or correctly labelled uses remain | Consistency |

---

## 4. Headline numbers: consistency check

Checked by searching the whole brain for each figure and its likely variants (for example "named in N of 32", "N posts", "Lite $…", "Gartner"). No conflicting values remain.

| Figure | Value used everywhere | Ground truth |
|---|---|---|
| Unbranded Perplexity questions naming Quotr | **1 of 32 (about 3%)** | Report; visibility notes §5 |
| Rivals named most | **STACK, PlanSwift, Buildxact: 10 each** (Togal.AI 8) | Report |
| quotr.ai in the source list / cited in the answer | **6 of 32** (as often as reddit.com) / **4 of 32** | Report; tracking-set.md (both definitions now explained) |
| Site content | **96 blog posts, 55 dictionary terms, 23 trade pages**, 6 tutorials, 4 case studies | Quotr fact-check, claims 2–3 |
| Old pricing | Retired Solo $299.90 / Team $499.90 on **about 13 URLs** (mostly blog posts, plus the indexed /contractors copy) and llms.txt; "nearly four times" the real entry price | Quotr fact-check, summary item 1 and Gaps filled #2 |
| Live pricing | **Lite $79.90, Plus $299.90 per seat per month**; Enterprise custom; 7-day trial | Quotr fact-check, claim 6; /pricing/ |
| Review-site ownership | **G2 owns Capterra, GetApp and Software Advice** (deal announced January 2026) | Quotr fact-check, claim 37a |
| Engines tested | **Perplexity only**; ChatGPT, Google AI Overviews and AI Mode, Gemini, Claude and Copilot not tested | Report; Quotr fact-check |
| Outside pages naming Quotr | Nomic, Octopus Builds, ForesightIQ (none independent) | Quotr fact-check, contradiction 3 |
| "$190K seed" | Appears only in Perplexity answers, not on PitchBook | Quotr fact-check, claim 22 |

---

## 5. Link check

**Method.** A small Python script reads every `.md` file in `geo-brain/`. It skips fenced code blocks and inline code, then extracts every Markdown link target (`[text](target)`, `[text](<target with spaces>)` and reference-style `[x]: target`). It ignores `http`, `https`, `mailto` and `#` targets, strips `#anchors`, decodes `%20`, resolves each target relative to the file's folder, and checks that the file or folder exists. It also flags bare `<../path>` references, which standard Markdown shows as plain text.

**Result on 2026-09-25 (final run):** 68 files, 2,098 relative links checked, **0 broken**, 0 bare path references. This includes every link to `../research_notes/Quotr GEO AEO strategy audit/…` and to `../reports/Quotr GEO AEO strategy audit.md`.

**History today:** the section passes left 0 broken links among the 63 section pages. The integrator pass converted 294 bare references into links. The new root pages were briefly broken until the files they point to were created (for example, links from [../sources.md](../sources.md) to this log). The final result is 0.

To repeat the check, a developer can recreate the script from the method above (about 30 lines of Python), or ask an AI tool with file access: "List every relative Markdown link in this folder whose target file does not exist."

---

## 6. TO CONFIRM with Quotr: the consolidated question list

This list merges and de-duplicates the open items from all five QA passes and the fact sheet's §6. **Bring it to the Quotr meeting.** When an item is answered, update [../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md) first, then remove the item here and log it in [changelog.md](changelog.md).

### A. Company identity
1. **Headquarters:** San Francisco (the /terms legal address, 495 27th Ave Unit 8; PitchBook; blog footers) or Berkeley (/disambiguation/, Crunchbase location)? Which address goes in schema?
2. **Founding year:** 2023 (/disambiguation/, Crunchbase) or 2024 (PitchBook)?
3. **Team:** size (11–50 vs PitchBook's 10); current titles for Tianyi Zong (COO) and Jati Ibloguen (Growth); author titles and bios for bylines.
4. **Founder bios:** may we name TAO, SmithGroup and the UC Berkeley architecture degree for Hanyang Liu?
5. **Official contact email:** info@quotr.io (on /terms) or an @quotr.ai address (procurement@quotr.ai exists)?

### B. Funding and investors
6. **Amounts and dates:** $200K pre-seed and $3.5M seed "as of December 25, 2025" (/disambiguation/) vs "$5 million" (podcast page). Which is right, and can the seed round be announced publicly?
7. **Sky Arc Capital:** is it an investor? PitchBook lists it; Quotr never mentions it.
8. **"$190K seed, Oct 2024":** does Quotr know where this figure comes from? It appears only in Perplexity answers.

### C. Quotr Procurement
9. **Factory network:** one number and one definition: 220+ vetted factories, 50+ audited manufacturers, or "220+ including 30+ audited"?
10. **Savings:** one figure and its method. Pages say up to 50%, 40–50% and 40–55%, and the /procurement/ totals imply 53–64%.
11. **Delivery area:** California only, or anywhere in the US? The same page says both.
12. **Offer details:** current product categories, order minimums, and what the delivered (DDP) price includes (tariffs, anti-dumping and countervailing (AD/CVD) duties, freight).
13. **Names:** is "QUOTR Framed Series" an official product line?
14. **Data:** can aggregated project and price data be published (for a price index), and can supplier names appear?

### D. Quotr Service
15. **Turnaround:** the standard and rush times. Pages say 24 hours, 72 hours, 1–3, 3–4 and 5–7 business days.
16. **Scope:** minimum job size; what "26 sub-trades" means against the 23 trade pages.
17. **Volume claims:** can "$1.2B+ in projects estimated" and "300+ projects a month" be backed by a method (count and date range)?

### E. Quotr Software
18. **Accuracy:** one approved figure and its conditions (95–99% on clean vector PDFs; about 80–88% on scans). Will Quotr publish the benchmark method?
19. **Time saved:** "up to 80%" vs "90% faster" vs RL Electric's 20 hours to 1–2 hours. Which one, and on what basis?
20. **Revit add-in:** are "Quotr Estimate" and "Quotr Connector" still sold? Is there an Autodesk App Store listing?
21. **Integrations and exports:** which integrations are live (Procore, Excel, QuickBooks, others)? Which export formats (is Excel export supported)?
22. **Files and platforms:** which file types (PDF, images, DWG, Revit)? Does it run in the browser on Mac?
23. **Feature names:** is "Smart Matching" official? What should the chat feature be called ("AI Agent")?
24. **Plans:** is there annual pricing for Lite and Plus? What do the Plus "2,000 sq ft takeoff credits" cover? Is SSO still in Enterprise? What does Lite's "AI detection" do (buyers compare it with Kreo's Lite and Plus)?
25. **Security:** SOC 2 status and encryption details for a security page.

### F. Audience and positioning
26. **Primary audience:** residential and multifamily, commercial, or both? /disambiguation/ says both.
27. **Lead product for top of funnel:** Software, Service or Procurement?
28. **"Partner programs":** what does the homepage mean by it?

### G. Customers and proof
29. **Permissions:** which customers will approve named results (RL Electric, AlphaX, BiltWise Structures, Salisbury Moore, the Saratoga client, Vanderbilt/Minh Nghiem)? RL Electric's measured result details; the full name for the "Maricruz" testimonial.
30. **Homepage quote:** replace "Customer perspective: Kyle, Llama Ventures" with a customer quote, or relabel it as an investor quote?
31. **Win/loss:** which competitors come up in sales deals, and why does Quotr win or lose?

### H. Domains, profiles and technical setup
32. **quotr.io:** does it 301-redirect to quotr.ai or mirror it? Who controls quotr.io, test.quotr.io and Cloudflare?
33. **Indexing:** is test.quotr.io noindexed? Does /developers/ carry a canonical tag to /service/?
34. **Cloudflare:** is "Block AI bots" on? Is the managed robots.txt on? Is AI Labyrinth on deliberately? What status codes do AI search bots receive?
35. **Old accounts:** are YouTube @QuotrIO ("QuoTrio") and LinkedIn "flozdesign" Quotr's? Can the quotrio and quotr_io handles be retired or redirected?
36. **Logo hosting:** keep the logo on public.quotr.io, or move it to quotr.ai?
37. **Memberships:** is Quotr a current member of BIA Bay Area and the Modular Building Institute?
38. **Podcasts:** does the iHeart "AEC Tech Journeys" episode ("From Drawings to Bids in Minutes") feature Quotr?

### I. Reviews and directories
39. **G2:** how many reviews does the "quotr-io" profile have, who has access, and can it be renamed to Quotr.ai? How will the G2 listing carry over to Capterra, GetApp and Software Advice? Is the team aware of G2's incentive rules?

### J. Measurement, process and budget
40. **Access and history:** GA4, Search Console, Bing Webmaster Tools, CRM and form access. Which key events exist? Can GA4 AI-traffic history back to January 2026 be pulled?
41. **Owners and budget:** who owns the monthly dashboard and the review drive? What budget exists for a tracking tool, YouTube and PR?
42. **Process and plans:** how is content made today, and who edits AI drafts before they go live? What did "The Wikipedia Hack" on the podcast mean, and is anything like it planned?

### Still unverified by the research (for us to check, not questions for Quotr)
- Baselines for ChatGPT, Google AI Overviews and AI Mode, Gemini, Claude and Copilot (October 2026).
- Whether rconstructionsolutions, PalCode, NEDES and aibuildingtools really mention Quotr (reported by Perplexity; not opened).
- The single-session results V1, V3, C13 and P5 (the fact-check's re-runs were refused).
- Quotr's Reddit footprint, backlinks, and LinkedIn and YouTube follower counts.
- WebSearch rank claims (for example, Quotr's roundup "4th of 9" for C1).
- Third-party studies and surveys marked "not re-checked" (listed in the GEO-evidence fact-check, section D), and all tool prices.

---

## Related pages

- [changelog.md](changelog.md) — dated change history and the entry template
- [../README.md](../README.md) — start page and the monthly maintenance routine
- [../00-quotr/entity-fact-sheet.md](../00-quotr/entity-fact-sheet.md) — where answered questions are recorded first
- [../08-action-plan/meeting-brief.md](../08-action-plan/meeting-brief.md) — the meeting where these questions are asked
- [../sources.md](../sources.md) — every source, grouped
