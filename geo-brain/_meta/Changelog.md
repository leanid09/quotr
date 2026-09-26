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
- If a **TO CONFIRM** item was answered, set its note in `00-quotr/open-questions` to `status: answered` (it leaves the open list) and note it here.
- After any edit session, run the vault check (`python3 .claude/scripts/vault_check.py`, see [[QA log]] §5) and record the result.

---

## Entries

### 2026-09-26 — Blog health audit: structure added (work in progress)

**Type:** Structure
**Changed by:** Claude (AI helper), at the GEO consultant's request
**Checked by:** the vault check script (0 problems)

**What changed**
- New record type **article**: one note per live Quotr blog post, in `02-current-state/articles`, with its health, recommended action and refresh status. Rules are in [[CLAUDE]].
- New live table `Articles.base` (refresh queue, all articles, by month, by cluster, cited by AI, old price, merge or retire, and more) and a new note template (`Article`).
- New properties in `.obsidian/types.json` (for example `published`, `byline`, `health`, `health_score`, `action`, `flags`). The vault check and the export script now know about articles.
- The article notes and the audit pages are being written now. This entry will be replaced by the full entry when they land.

### 2026-09-25 — Brain turned into an Obsidian vault (v1.1)

**Type:** Structure
**Changed by:** Claude (AI helper), at the GEO consultant's request
**Checked by:** the vault check script (0 problems) and a test run in Obsidian 1.13.4: 0 broken links, every live table renders with the expected counts, and a cell-by-cell comparison showed no table content was lost

**What changed**
- The whole `quotr` folder is now an Obsidian vault. [[Home]] is the daily dashboard and opens at startup. Rules for AI helpers are in [[CLAUDE]].
- Pages were renamed to readable titles (for example `entity-fact-sheet.md` became `Entity fact sheet.md`, `README.md` became [[Start here]]). All 2,100 internal links are now Obsidian `[[links]]`.
- Every page has properties: `type`, a one-line `description`, `last_verified` (was "Last updated") and `verify_every_days`. "What this page is for" and "Sources" are now boxes (callouts); Sources is folded.
- The big tables became one note per item, with live tables (Obsidian Bases) in their place: 282 prompts (with the tracking-set data), 64 September 2026 test runs, 68 content pieces, 48 tasks and 48 open questions. Pages keep all their explanation.
- New: note templates (daily note, weekly and monthly review, test run, prompt, content piece, task, question), a `journal` folder, four index pages ([[Competitor profiles]], [[Playbooks]], [[Off-site playbooks]], [[Page templates]]), bookmarks, graph colours and shared settings in `.obsidian`.
- New: `.claude/scripts/vault_check.py` (links, headings, properties and tables) and `.claude/scripts/build_exports.py` (plain-text copies of the tables in `geo-brain/_exports`, for AI tools and GitHub).

**Why**
- To use the brain every day in Obsidian, following steps 1–6 of [[Obsidian vault and daily updates plan]]. Two changes from that plan: facts stay as text in the [[Entity fact sheet]] (embedding them would break sentences), and Claude never writes in daily notes, so it cannot clash with your edits.

**Files affected**
- All pages (renamed, properties, links); new folders `04-prompt-library/prompts`, `07-measurement/test-runs`, `05-content-strategy/roadmap`, `08-action-plan/tasks`, `00-quotr/open-questions`, `journal`, `_meta/note-templates`, `_exports`.

**TO CONFIRM items resolved or added**
- None resolved. The 42 questions for Quotr and the 6 checks for us are now notes in `00-quotr/open-questions` ([[QA log]] §6 shows them live).

**Vault check:** 0 problems (`python3 .claude/scripts/vault_check.py`).

---

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
- [Item, and whether it was resolved (question note set to answered) or added as a new question note.]

**Vault check:** [number] problems after this change.
```

---

## Related pages

- [[QA log]] — the 2026-09-25 QA record, link-check method and the TO CONFIRM list
- [[Start here]] — the monthly maintenance routine
- [[Entity fact sheet]] — update this first when a Quotr fact changes
- [[Tracking set]] — the monthly test whose results you log here
