# Wikidata, Knowledge Graph and Profile Consistency Playbook

**What this page is for:** How to make Quotr.ai one clear, consistent "entity" across Wikidata, Crunchbase, PitchBook, directories and social profiles, so AI engines stop mixing it up with other "Quotr" products and stop repeating conflicting facts; includes a Wikidata item plan and cautions about Wikipedia.

**Last updated:** 2026-09-25

**Sources:** [quotr_offsite_presence.md](<../../../research_notes/Quotr GEO AEO strategy audit/quotr_offsite_presence.md>) (§1, §4 entity signals and name collisions, §5 AI descriptions, §6), [verification_quotr_and_competitors.md](<../../../research_notes/Quotr GEO AEO strategy audit/verification_quotr_and_competitors.md>) (claims 19–24, 28–30; contradictions 2, 6–8; gaps filled #1, #3), [geo_content_playbook_b2b.md](<../../../research_notes/Quotr GEO AEO strategy audit/geo_content_playbook_b2b.md>) (§3 Wikipedia/Wikidata), [geo_ai_citation_signals_2026.md](<../../../research_notes/Quotr GEO AEO strategy audit/geo_ai_citation_signals_2026.md>) (§1 parametric knowledge; §3 /disambiguation/ inference), [verification_geo_evidence.md](<../../../research_notes/Quotr GEO AEO strategy audit/verification_geo_evidence.md>) (H16; O4), [quotr_onsite_content_audit.md](<../../../research_notes/Quotr GEO AEO strategy audit/quotr_onsite_content_audit.md>) (§4–5); [../../00-quotr/entity-fact-sheet.md](../../00-quotr/entity-fact-sheet.md). Policies checked via WebSearch on 2026-09-25: [Wikidata:Notability](https://www.wikidata.org/wiki/Wikidata:Notability), [Wikipedia: Notability (organizations and companies)](https://en.wikipedia.org/wiki/Wikipedia:Notability_(organizations_and_companies)), [Wikipedia: Conflict of interest](https://en.wikipedia.org/wiki/Wikipedia:Conflict_of_interest), [Wikipedia: Paid-contribution disclosure](https://en.wikipedia.org/wiki/Wikipedia:Paid-contribution_disclosure), Wikidata properties [P4264](https://www.wikidata.org/wiki/Property:P4264), [P2088](https://www.wikidata.org/wiki/Property:P2088), [P2397](https://www.wikidata.org/wiki/Property:P2397), [P12689](https://www.wikidata.org/wiki/Property:P12689); [PitchBook: update your profile](https://pitchbook.com/help/update-your-profile); [Crunchbase: edit a profile](https://support.crunchbase.com/hc/en-us/articles/115010477107-Edit-a-Profile-on-Crunchbase).

---

## 1. Plain-English background

- **Entity:** the company as one "thing" machines recognise, with a name, website, founders, location and profiles.
- **Knowledge graph:** a database of entities and the facts that link them. Google has one; AI models build their own picture of a brand from everything written about it.
- **Why it matters for AI answers:** ChatGPT runs a live web search on only about a third of prompts (Nectiv 31%, 2025; OtterlyAI 34.5%, Feb 2026; both not re-checked). The rest are answered from the model's training data, which is built from broad web mentions, so consistent facts across the web shape what AI "knows" about Quotr (`geo_ai_citation_signals_2026.md` §1).
- **Wikidata:** a free, open database of facts run by the Wikimedia Foundation (the people behind Wikipedia). Each entity is an "item" with an ID (a "QID") and statements such as "official website = quotr.ai".
- **Evidence level:** that a Wikidata item helps AI entity recognition is a PR-agency opinion with no published data. Treat it as **low-cost hygiene, not a lever** (`verification_geo_evidence.md` H16).

---

## 2. The problem today: one company, many versions

AI tools already show the effects:
- **Perplexity** answered "What is Quotr?" with "a name used by several different products", listing unrelated apps, and borrowed the Quotr Pro app's **37 ratings / 4.7** for Quotr.ai (offsite notes §5; verification claim 30).
- A search summary described Quotr as **"an AI assistant … Revit integration to help architects"** (legacy positioning from F6S, LinkedIn and Crunchbase).
- A summary about Hanyang Liu **merged another startup's funding news** ("$4.2M seed led by Initialized Capital… zerank-1").
- Perplexity reports a **"$190K seed, Oct 2024, per PitchBook"** that the live PitchBook page does not show (verification claim 22).

**Conflicting facts across Quotr-controlled and third-party sources** (fact sheet §4; verification contradictions 2, 6–8):

| Fact | Versions found |
|---|---|
| Name / domain | Quotr.ai vs Quotr.io (F6S, podcast, G2 slug, GitHub "Quotr-io", MBI and BIA slugs) |
| HQ | San Francisco (/terms legal address, PitchBook, blog footers, Crunchbase About, podcast) vs Berkeley (/disambiguation/, Crunchbase location field, Octopus Builds) |
| Founded | 2023 (/disambiguation/, Crunchbase) vs 2024 (PitchBook) |
| Founders | Hanyang Liu + Junzhe Shi (/about-us/, Crunchbase, LinkedIn) vs Junzhe Shi only (/disambiguation/) |
| Funding | $200K pre-seed + $3.5M seed (/disambiguation/) vs "raised $5 million" (MPN podcast) vs one seed round dated 01-Jan-2025 with no amount shown (PitchBook); Perplexity adds a "$190K seed" it credits to PitchBook, which the PitchBook page does not show |
| Investors | SkyDeck + Llama Ventures vs + Sky Arc Capital (PitchBook) |
| Employees | 11–50 vs 10 (PitchBook) |
| Factory network | "50+ audited manufacturers" (homepage, /procurement/) vs "220+ vetted factories" (llms.txt, /disambiguation/) vs "220+ factories, including 30+ audited manufacturers" (other indexed Quotr text) |
| Social handles | linkedin quotrai vs quotrio; x quotr_ai vs quotr_io; youtube @QuotrAI vs @QuotrIO |

**Name collisions** (offsite notes §4): Quotr Pro (App Store id6759211998, quotr.pro), quotrhq.com, quotr.software, getquotr.com, joinquotr.com, quotr.ichii.io, several "Quotr" apps, GitHub andrerpena/quotr; directory look-alikes QuoTrak, Quoters, Quartr.

---

## 3. Step 1: decide the canonical facts (Quotr must approve)

Nothing below can be fixed until Quotr answers the open questions in [../../00-quotr/entity-fact-sheet.md](../../00-quotr/entity-fact-sheet.md) §6. Fill this master record once and copy it everywhere.

| Field | Canonical value | Status |
|---|---|---|
| Brand name | Quotr.ai | Confirmed |
| Former name | Quotr.io | Confirmed |
| Legal name | FLOZ Inc. (Delaware corporation) | Confirmed (/terms) |
| Official website | https://quotr.ai | Confirmed |
| One-line description | "AI construction takeoff, estimating and bid software, with a done-for-you estimating service and factory-direct material procurement." | Draft for approval |
| Founders | Hanyang Liu (CEO), Junzhe Shi, PhD (CTO) | Confirmed by /about-us/, Crunchbase, LinkedIn |
| Accelerator | Berkeley SkyDeck, Batch 19 | Confirmed |
| Investors | Berkeley SkyDeck Fund; Llama Ventures (+ Sky Arc Capital?) | **TO CONFIRM** |
| HQ | San Francisco or Berkeley | **TO CONFIRM** |
| Founded | 2023 or 2024 | **TO CONFIRM** |
| Funding amounts | — | **TO CONFIRM**; announce publicly before listing |
| Employees | 11–50 or ~10 | **TO CONFIRM** |
| Social handles | linkedin.com/company/quotrai; x.com/quotr_ai; youtube.com/@QuotrAI; instagram.com/quotr.ai; medium.com/@quotr-ai; Facebook profile id 61572581013981 | Recommended (current-name handles) |
| Logo | One file, hosted on quotr.ai | **TO CONFIRM** |

---

## 4. Step 2: fix every profile (the consistency sweep)

| # | Profile | Fix | How |
|---|---|---|---|
| 1 | **quotr.ai itself** | /disambiguation/ (neutral rewrite; one audience; both founders; current handles), blog boilerplate (one HQ), /about-us/ (add founded, HQ once confirmed), schema Organization ([../schema-markup-kit.md](../schema-markup-kit.md) 5.1), llms.txt | Site edits |
| 2 | **Crunchbase** ([organization/quotr](https://www.crunchbase.com/organization/quotr)) | Location field and About text disagree (Berkeley vs San Francisco); factory and savings claims; legacy "Revit … architects" summary | Claim the profile ("Claim this profile" at the bottom, verified with a company email or LinkedIn), then edit fields |
| 3 | **PitchBook** ([606944-17](https://pitchbook.com/profiles/company/606944-17)) | Founding year 2024; HQ; 10 employees; Sky Arc Capital; "BIM models" description | Use PitchBook's data-feedback / "Update this profile" route |
| 4 | **F6S** ([software/quotr](https://www.f6s.com/software/quotr)) | Unclaimed; Revit-era description; links quotr.io | Claim; rewrite; link quotr.ai; add to the "AI-Assisted Takeoff" category |
| 5 | **G2** (quotr-io) | Name/slug "quotr io" | Claim; rename to Quotr.ai ([review-generation.md](review-generation.md)) |
| 6 | **Product Hunt** | Category "Real estate"; links GitHub "Quotr-io" | Re-categorise; update links |
| 7 | **LinkedIn** | Company About (legacy positioning); duplicate company page (quotrio); flozdesign page; Hanyang Liu's two personal profiles | See [linkedin-thought-leadership.md](linkedin-thought-leadership.md) §2 |
| 8 | **YouTube** | @QuotrIO / "QuoTrio" channel listed on /disambiguation/ | Confirm ownership; consolidate on @QuotrAI ([youtube-and-video.md](youtube-and-video.md)) |
| 9 | **X** | @quotr_io listed on /disambiguation/ and podcast notes | Use @quotr_ai everywhere; if @quotr_io is Quotr's, point it to @quotr_ai |
| 10 | **GitHub** (Quotr-io) | Old name | Rename or add "Quotr.ai" to the profile (optional) |
| 11 | **Podcast show notes** (MPN Episode 45) | "CEO of Quotr.io", "raised $5 million", links quotr.io | Email the host with corrections |
| 12 | **Memberships** (BIA Bay Area "quotr-io-6539"; Modular Building Institute "quotr-io-4201053"; Procore Construction Network "floz-berkeley") | Old names and slugs | Ask each to update the name, website and description |
| 13 | **Investor and accelerator pages** (SkyDeck Batch 19, Llama Ventures portfolio) | Check descriptions match | Email with the one-liner |
| 14 | **Legacy hosts** | quotr.io pages still indexed; test.quotr.io was indexed and cited | Make quotr.io 301-redirect to quotr.ai (**TO CONFIRM** current behaviour); keep test.quotr.io behind login and `noindex` |

---

## 5. Step 3: create a Wikidata item (after Step 1)

### 5a. Is Quotr eligible?

Wikidata's notability policy accepts an item if it "refers to an instance of a clearly identifiable conceptual or material entity that can be described using serious and publicly available references", or if it fills a structural need ([Wikidata:Notability](https://www.wikidata.org/wiki/Wikidata:Notability)). That bar is lower than Wikipedia's. Quotr can point to Berkeley SkyDeck's Batch 19 page, Crunchbase, PitchBook and the Llama Ventures portfolio as public references. Items with weak references can still be deleted by the community, so reference every statement.

### 5b. Conflict-of-interest etiquette

- Create a personal Wikidata account (not a shared "Quotr" account). State the connection on your user page (e.g., "I work for / consult for Quotr.ai (FLOZ Inc.)").
- Add only verifiable, neutral facts. No marketing language in labels or descriptions.

### 5c. Suggested item content (fill with confirmed values only)

| Field / property | Value | Reference |
|---|---|---|
| Label (English) | Quotr.ai | quotr.ai |
| Description | AI construction takeoff and estimating software company (keep it short and neutral) | — |
| Aliases | Quotr; Quotr.io; FLOZ Inc. | quotr.ai/disambiguation/, /terms |
| instance of (P31) | business / software company (search Wikidata for the correct class items) | — |
| official website (P856) | https://quotr.ai | quotr.ai |
| official name (P1448) | FLOZ Inc. (check whether a separate item for the legal entity is better; one item is simpler for a small company) | quotr.ai/terms |
| founded by (P112) | Hanyang Liu; Junzhe Shi (as text-linked items only if person items are warranted; otherwise omit) | /about-us/, Crunchbase |
| inception (P571) | **TO CONFIRM** (2023 or 2024) | — |
| headquarters location (P159) | **TO CONFIRM** | — |
| country (P17) | United States | /terms |
| industry (P452) | construction software / software industry (pick existing items) | — |
| LinkedIn company ID (P4264) | quotrai | linkedin.com/company/quotrai |
| Crunchbase organization ID (P2088) | quotr | crunchbase.com/organization/quotr |
| PitchBook profile ID (P12689) | company/606944-17 (only after the profile is corrected) | pitchbook.com |
| YouTube channel ID (P2397) | the channel ID of @QuotrAI (look it up in YouTube; **not** the @QuoTrio ID) | youtube.com |
| X username (P2002) | quotr_ai | x.com |

**Then:** add the Wikidata URL to the Organization schema `sameAs` on quotr.ai ([../schema-markup-kit.md](../schema-markup-kit.md) 5.1), and keep the item updated when facts change (add it to your Wikidata watchlist).

---

## 6. Wikipedia: not now

- **Notability bar:** a company is presumed notable only with "significant coverage in multiple reliable secondary sources that are independent of the subject"; the guideline is deliberately strict to stop promotion ([WP:NCORP](https://en.wikipedia.org/wiki/Wikipedia:Notability_(organizations_and_companies))). Quotr has no independent trade-press coverage yet (offsite notes §3), so an article would very likely be deleted.
- **Conflict of interest:** Wikipedia strongly discourages people with a financial connection from editing articles about their company directly; paid contributors **must** disclose their employer, client and affiliation under the Wikimedia Terms of Use ([paid-contribution disclosure](https://en.wikipedia.org/wiki/Wikipedia:Paid-contribution_disclosure); [COI guideline](https://en.wikipedia.org/wiki/Wikipedia:Conflict_of_interest)).
- **Treat "Wikipedia hacks" with caution.** The March 2026 podcast episode with Quotr's CEO listed "The Wikipedia Hack" as a topic (offsite notes §3). We do not know what was meant, so ask the team before anyone acts. Any undisclosed or promotional editing risks deletion, reputational damage and a permanent record on the article's talk page.
- **What to do instead:** earn independent coverage first ([listicle-and-pr-outreach.md](listicle-and-pr-outreach.md)). If Quotr later becomes notable, request an article through Wikipedia's "Articles for Creation" process with full disclosure, or let independent editors write it.
- **Context:** Wikipedia was a very large share of ChatGPT's top-cited sources in Aug 2024–Jun 2025 data (Profound: 47.9% of its top-10 source share; not re-checked in the verification pass). ChatGPT's Wikipedia citations dropped sharply in September 2025, so treat that figure as historical, although Muck Rack (May 2026) still found Wikipedia the top domain ChatGPT cites (`verification_geo_evidence.md` O4). Either way, Quotr cannot get there without independent coverage first.

---

## 7. Knowledge panel and name-collision defence

- **Google knowledge panel:** none was observed (not directly testable in the research). If one appears for "Quotr.ai", use Google's process for claiming a knowledge panel and suggest corrections.
- **Disambiguation page:** keep /disambiguation/, but rewrite it as a plain fact page for humans ("Quotr.ai is not related to the Quotr Pro app…"), remove text addressed to "search engines and AI systems" and "algorithmic financial scrapers", fix the audience contradiction and list only current profiles (onsite audit §4).
- **Always pair the brand with the category** in titles and first sentences: "Quotr.ai — AI construction takeoff and estimating software".
- **Never link to namesake products** or repeat their ratings.

---

## 8. Checklist and tracking

- [ ] Canonical record (section 3) approved by Quotr.
- [ ] quotr.ai pages and schema updated to the canonical record.
- [ ] Crunchbase claimed and corrected.
- [ ] PitchBook correction submitted.
- [ ] F6S claimed and rewritten; G2 renamed; Product Hunt re-categorised.
- [ ] LinkedIn, YouTube and X consolidated on current handles.
- [ ] Podcast, membership, investor and accelerator pages emailed.
- [ ] quotr.io redirects checked; test.quotr.io noindexed.
- [ ] Wikidata item created with references; linked from schema `sameAs`.
- [ ] No Wikipedia article attempted until independent coverage exists.

| Metric | How | Cadence |
|---|---|---|
| Profiles matching the canonical record | Audit table | Quarterly |
| AI answers to D-001/D-002 ("What is Quotr(.ai)?"), D-004 (founders/funding), D-006 (Quotr.io), D-020 (Quotr Pro) accurate, no namesake mix-ups | Prompt tracking ([../../04-prompt-library/tracking-set.md](../../04-prompt-library/tracking-set.md)) | Monthly |
| Wikidata item live and unchanged by others | Watchlist | Monthly |

---

## Related pages

- [../../00-quotr/entity-fact-sheet.md](../../00-quotr/entity-fact-sheet.md) — canonical facts, inconsistency register, open questions
- [../schema-markup-kit.md](../schema-markup-kit.md) — Organization schema and `sameAs`
- [review-generation.md](review-generation.md) — G2 and Capterra profiles
- [linkedin-thought-leadership.md](linkedin-thought-leadership.md) — LinkedIn profile fixes
- [partnerships-and-marketplaces.md](partnerships-and-marketplaces.md) — marketplace and partner listings
- [../../02-current-state/offsite-presence.md](../../02-current-state/offsite-presence.md) — full list of third-party profiles
