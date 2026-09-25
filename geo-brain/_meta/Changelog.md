---
type: log
description: Dated log of changes to the brain, with a template for future entries.
last_verified: 2026-09-25
---
# Changelog

> [!abstract] What this page is for
> A dated record of every meaningful change to this knowledge brain: what changed, why, which files, and who checked it. Anyone updating the brain adds an entry here, newest first, using the template at the bottom.

> [!info]- Sources
> the QA and integration record in [[QA log]]; the research files listed in [[Sources]].

---

## How to log a change

- Add a new entry **at the top** of "Entries" (newest first), using the template below.
- Log changes to facts, numbers, recommendations or structure. Typo fixes don't need an entry.
- If a **fact about Quotr** changed, say what the old and new values were and where the new value came from (Quotr sign-off, a live page, a re-test). Update [[Entity fact sheet]] first, then the other pages.
- If a **TO CONFIRM** item was answered, remove it from the list in [[QA log]] §6 and note it here.
- After any edit session, run the link check (method in [[QA log]] §5) and record the result.

---

## Entries

### 2026-09-25 — Brain created (v1.0)

**Type:** Created
**Changed by:** research and writing team; integration and final edit pass
**Checked by:** five section QA passes, then an integrator pass (see [[QA log]])

**What happened**
- Created the Quotr.ai GEO knowledge brain from the September 2026 research audit: 63 pages in nine topic folders (`00-quotr` to `08-action-plan`), including 12 page templates and 7 off-site playbooks.
- Added the root files: [[Start here]] (start here), [[AI context pack]] (AI briefing, about 1,750 words) and [[Sources]] (about 950 unique outside sources, grouped by type).
- Added this `_meta` folder: [[QA log]] and this changelog.

**Baseline facts recorded** (all as of 2026-09-25; Perplexity was the only engine tested)
- Quotr named in 1 of 32 unbranded Perplexity questions (about 3%); STACK, PlanSwift and Buildxact named in 10 each.
- A quotr.ai page appeared in the source list of 6 of 32 answers (cited in the answer text of 4).
- Live pricing: Lite $79.90 and Plus $299.90 per seat per month, Enterprise custom, 7-day trial; retired Solo/Team pricing still on about 13 Quotr URLs and in llms.txt.
- Site content: 96 blog posts, 55 dictionary terms, 23 trade pages, 6 tutorials, 4 case studies.
- G2 owns Capterra, GetApp and Software Advice (deal announced January 2026).

**Corrections made during QA** (summary; full list in [[QA log]])
- Applied the two fact-check files everywhere: three confirmed outside pages naming Quotr (Nomic, Octopus Builds, ForesightIQ; none independent), the "$190K" figure credited to Perplexity (not PitchBook), STACK review counts (Capterra about 1,400; G2 under 100), PlanSwift owned by ConstructConnect, and G2 ownership of the Gartner review sites.
- Aligned the monthly test cadence (four engine runs monthly; Claude and Copilot quarterly; a full six-tool baseline in October 2026) and the two meanings of "cited" (6 of 32 in the source list, 4 of 32 in the answer text).
- Labelled single-session test results, unverified third-party claims and figures that were not re-checked.
- Converted 294 plain-text references to the research notes into working links; the final link check found 0 broken relative links.

**Files affected:** all.

**Open items carried forward:** the TO CONFIRM list in [[QA log]] §6.

---

## Template for future entries

Copy this block to the top of "Entries" and fill it in.

```
### YYYY-MM-DD — [short title, e.g. "October tracking run" or "HQ confirmed as San Francisco"]

**Type:** Fact update / New test results / New page / Page rewrite / Structure / Link fixes / Other
**Changed by:** [name]
**Checked by:** [name, or "not yet checked"]

**What changed**
- [One line per change. For a fact: old value → new value, and the source (Quotr sign-off, live page URL, test run ID).]

**Why**
- [Reason: Quotr confirmed a fact, a page on quotr.ai changed, a new monthly test, a new study, a correction.]

**Files affected**
- [relative/path/to/file.md] (section)

**TO CONFIRM items resolved or added**
- [Item, and whether it was resolved or newly added to qa-log.md §6.]

**Link check:** [number] broken relative links after this change.
```

---

## Related pages

- [[QA log]] — the 2026-09-25 QA record, link-check method and the TO CONFIRM list
- [[Start here]] — the monthly maintenance routine
- [[Entity fact sheet]] — update this first when a Quotr fact changes
- [[Tracking set]] — the monthly test whose results you log here
