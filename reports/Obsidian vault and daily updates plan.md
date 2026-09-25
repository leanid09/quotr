# How to make the Quotr GEO brain a better Obsidian vault, and keep it fresh every day

**Date:** 2026-09-25
**Based on:** a structural check of all 68 brain pages, plus research into Obsidian best practices ([notes](<../research_notes/obsidian_vault_best_practices.md>)).

---

## The short version

The brain has good content, but it was built as a **report**, not as a **working tool**. To use it every day in Obsidian, it needs six changes:

1. **Open the right folder.** Open the whole `quotr` repo as the vault, not just `geo-brain/`, or 529 links break.
2. **Label every page.** Add a small info block (called "properties") so you can sort and filter pages.
3. **Break up the giant tables.** Give each question, each content piece and each AI test its own small note.
4. **Keep each fact in one place.** Every other page shows it from there instead of copying it.
5. **Add daily and weekly routines** in Obsidian, with ready-made note templates.
6. **Let Claude do the daily updates.** It proposes changes, and you approve them before they go in.

---

## 1. What's wrong today (the check)

| What I checked | Result | Why it matters |
|---|---|---|
| Pages with properties (the info block at the top) | **0 of 68** | You can't filter "overdue", "to confirm" or "owner: marketing" |
| Links that point outside `geo-brain/` | **529** | They break if you open only that folder |
| Link style | All standard `[text](path)` links, **0 Obsidian `[[links]]`** | Links break when files get renamed; they're harder to write by hand |
| Average page length | **~4,000 words** (biggest: 13,300) | Hard to read on a phone; slow in AI tools; tables lag in Obsidian |
| Big tables | **492** | 200+ questions and 68 content pieces are stuck inside tables, so you can't tick off or track single items |
| Checkboxes | **216**, spread over many pages | There's no single to-do view |
| "TO CONFIRM" notes | **465**, scattered | There's no single list of open questions for Quotr |
| Daily notes, templates, Obsidian settings | **None** | Nothing supports everyday use yet |
| Instructions for AI helpers | **None** | Claude could accidentally overwrite facts or history |

**The good news:** folder names are already neat and numbered, file names are unique, and every link currently works. Nothing needs rewriting; it needs **reshaping**.

---

## 2. The target vault (what it should look like)

```
quotr/                      ← open THIS as the Obsidian vault
  Home.md                   ← dashboard: today's tasks, overdue pages, latest scores
  CLAUDE.md                 ← rules for AI helpers
  geo-brain/
    00-quotr/facts/         ← one note per key fact (price, HQ, factory count…)
    01-geo-fundamentals/    ← long reading pages (keep as they are)
    02-current-state/
    03-market/competitors/  ← already one note per competitor ✓
    04-prompt-library/prompts/    ← NEW: one note per question (E07, T12…)
    05-content-strategy/roadmap/  ← NEW: one note per content piece (R-01…R-62)
    06-playbooks/           ← keep as they are
    07-measurement/test-runs/     ← NEW: one note per AI test (question × engine × date)
    08-action-plan/tasks/   ← NEW: one note per task
    _meta/ templates/ daily/ weekly/
  research_notes/  reports/ ← evidence (read-only)
```

**Rule of thumb:**
- Something you **read**, like guides, playbooks and the style guide, stays a long page.
- Something you **track**, like questions, content pieces, tasks, test runs and facts, becomes one small note each.

---

## 3. Labels on every note (properties)

Each note gets a short block at the top. Example for one content piece:

```yaml
---
type: roadmap-item
id: R-06
status: planned        # idea / planned / writing / published / refreshed
priority: P1
month: 2026-11
persona: [subcontractor]
trade: [drywall]
target_prompts: ["[[E07]]", "[[T12]]"]
owner: marketing
last_verified: 2026-09-25
verify_every_days: 30
---
```

Why this helps: Obsidian's built-in **Bases** feature turns these labels into live, editable tables. For example:
- **"Overdue for checking":** anything where `last_verified` is older than `verify_every_days`
- **"Content board":** roadmap items grouped by status (a Kanban board is in early access)
- **"Open questions for Quotr":** every fact with `status: to-confirm`, all 465 mentions reduced to one list
- **"AI visibility over time":** all test runs, filtered by question or engine

Use **Bases** (built into Obsidian), not the older Dataview or Kanban plugins. Their authors have mostly stopped updating them.

*Note: the example Bases setups in the research notes come from guides and were not tested in Obsidian. Check them against Obsidian's help page first.*

---

## 4. One home for every fact

Today the price "$79.90" is typed into dozens of pages. When it changes, every copy has to be found.

**Better:** each fact lives once, in the fact sheet, with a tag. Other pages show it using an embed, like `![[entity-fact-sheet#^price-lite]]`. Change it in one place and it updates everywhere.

- Facts not yet confirmed get `status: to-confirm` and a yellow warning box.
- **Past test results are never edited.** New runs are added as new notes. That's how you see progress over time.

---

## 5. The everyday routine

| When | Who | What | Time |
|---|---|---|---|
| **Daily** | Claude (automatic) | Asks AI engines 5–10 questions from the tracking set, saves each answer as a test-run note, flags big changes | 0 min for you |
| **Daily** | You | Open **Home** → check the flags → approve Claude's changes → note what you did in today's daily note | 10 min |
| **Weekly** | Claude + you | Staleness check (overdue pages), broken-link check, weekly summary note | 20 min |
| **Monthly** | You | Full 50-question tracking set, update the scorecard, review the plan, add a changelog entry | 1–2 h |

**Daily note template** (created automatically each day):
- AI checks: what changed today (links to test runs)
- Fixes made on quotr.ai
- New reviews / mentions / press found
- Decisions and questions for Quotr
- Tomorrow's top 3

---

## 6. Letting Claude help safely

1. **GitHub is the hub.** Your Obsidian and Claude both sync through the `quotr` repo. On your computer, the **Obsidian Git** plugin pulls changes at startup and saves every 10–15 minutes.
   - Its author calls it unstable on phones. On a phone, use Obsidian Sync or the published website instead.
   - Never use two sync tools on the same folder.
2. **Rules file (`CLAUDE.md`).** This tells Claude:
   - create new notes rather than rewrite old ones;
   - only add to daily notes, never change them;
   - never change facts without a source;
   - always update `last_verified` with a link;
   - log every change in the changelog.
3. **Scheduled Claude runs.** A nightly test run and a weekly check-up.
   - Claude puts its changes in a **proposal** (a pull request) and doesn't change the main copy directly.
   - Changes to facts always need your click to approve. New test results can be approved automatically.
   - This scheduling feature is still in preview, so watch it for the first few weeks.
4. **Keep plugins to a minimum.** Use Obsidian's built-in features plus Obsidian Git, and maybe Templater. Community plugins get full access to your computer.

---

## 7. Sharing with Quotr

| Option | Cost | Good for | Watch out |
|---|---|---|---|
| **Quartz 5** (free website built from the vault) | Free | Publishing only the notes you choose; shows tables and warning boxes | Needs a one-time technical setup; page passwords are light protection only |
| **Obsidian Publish** | ~$8–10/month | Easiest, no tech | Only one password for the whole site |

Either way, **don't publish internal pages** like the meeting brief or the notes on Quotr's weaknesses. Share only chosen pages.

---

## 8. How to get there (step by step)

| Step | What | Effort | Who |
|---|---|---|---|
| 1 | Make the repo root the vault; add Home, CLAUDE.md, templates folder, Obsidian settings | ½ day | Claude |
| 2 | Add properties to all 68 pages; swap "Last updated" for `last_verified` | ½ day | Claude |
| 3 | Split the prompt library, tracking set, roadmap, action plan and test results into single notes (~350 notes) | 1 day | Claude |
| 4 | Turn the fact sheet into one-fact-per-tag, and add embeds elsewhere | ½ day | Claude, then you review |
| 5 | Switch links to Obsidian `[[links]]` and re-check that none are broken | 2 h | Claude |
| 6 | Build the Bases views: overdue, content board, open questions, visibility trend | ½ day | Claude, then you test in Obsidian |
| 7 | Set up Obsidian Git on your laptop | 20 min | You (I'll guide you) |
| 8 | Turn on the nightly and weekly Claude runs | 1 h | Claude, you approve |
| 9 | (Optional) publish a client-safe site with Quartz | ½ day | Claude |

**Steps 1–6 can be done in this session.** Steps 7 and 8 need a few clicks from you.

---

## 9. Risks to keep in mind

- **Too many links and plugins** make the vault slow and messy. Link only when it helps.
- **Renaming files outside Obsidian** breaks links. Rename inside Obsidian, or let Claude run a link check.
- **Only Perplexity is tested today.** The daily runs should add ChatGPT and Google results when access allows.
- **AI answers change from run to run.** Look at weekly trends, not single days.
