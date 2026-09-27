---
type: research-note
description: Research on Obsidian vault structure, Bases, daily workflows, AI agents and sharing (September 2026).
date: 2026-09-25
---
# Obsidian vault best practices for the Quotr GEO brain (research notes)

**Date:** 2026-09-25
**Question:** How should the 68-file `geo-brain/` markdown knowledge base become an Obsidian vault that (a) a non-technical marketing consultant uses every day and (b) AI agents (Claude Code, Claude cloud routines) help keep up to date every day?
**Method:** WebSearch plus page reads of official Obsidian docs/changelog, Claude Code docs, plugin repos and 2025–2026 practitioner guides. Where a claim comes from a third-party blog rather than official docs, it is marked "(practitioner)".
**Current state checked in repo:** `geo-brain/` has numbered folders `00-quotr` … `08-action-plan` plus `_meta/` (changelog, QA log). Files use standard Markdown relative links, with angle brackets for paths that contain spaces, e.g. `[x](<../../research_notes/Quotr GEO AEO strategy audit/…md>)`. Several links point **outside** `geo-brain/` (to `../reports/` and `../research_notes/`). Big single-file tables: `prompt-library.md` (573 lines), `buyer-questions-by-trade.md` (722), `tracking-set.md` (309), `content-roadmap.md` (286), `ai-visibility-baseline.md` (378). Every page has a bold "Last updated:" line in the body, but no YAML frontmatter.

---

## 0. State of Obsidian in September 2026 (context for everything below)

- **Current versions:** Desktop 1.13.x is the public release. 1.14.0–1.14.2 (2–15 Sept 2026) are in **Catalyst early access** only. 1.14 adds a **Kanban layout inside Bases**, collapsible groups, and colour highlights. 1.14.2 lets Kanban cards move between folder columns. Source: https://obsidian.md/changelog/
- **1.13 (public, 30 July 2026):** a settings window you can search, a full-screen image viewer, URI confirmation guardrails, Mermaid rendering off by default until you confirm it, and the Note Composer now rewrites links when you extract a section. Source: https://obsidian.md/changelog/2026-07-30-desktop-v1.13.4/
- **Obsidian CLI (official, 1.12 installer or later):** "Anything you can do in Obsidian you can do from the command line." It needs the desktop app running. Commands include `daily:append`, `property:set`, `base:query format=json|csv|md`, `unresolved`, `orphans`, `move`/`rename` (these update links), `tasks`, `search:context` and `publish:add`. Source: https://obsidian.md/help/cli
- **Obsidian Headless (open beta, Feb 2026):** `npm i -g obsidian-headless` gives `ob login`, `ob sync --continuous`, and headless Publish. It works without the desktop app, on Node 22 or later. Obsidian lists its uses as "Give agentic tools access to a vault without access to your full computer" and "Run scheduled automations". Sources: https://obsidian.md/help/headless, https://obsidian.md/help/sync/headless, https://github.com/obsidianmd/obsidian-headless
- **Official agent skills from Obsidian's CEO (kepano):** `obsidian-markdown`, `obsidian-bases`, `json-canvas`, `obsidian-cli` and `defuddle`. To install them, drop them into `.claude/` in the vault root. Source: https://github.com/kepano/obsidian-skills

---

## 1. Vault structure conventions

### What the conventions say

| Convention | Core idea | Source |
|---|---|---|
| **PARA** (Tiago Forte) | Projects / Areas / Resources / Archive as top folders, sorted by how actionable each item is. People often combine it with MOCs once a vault passes about 200 notes. | https://www.natecue.com/en/learn/productivity/map-of-content/ (practitioner) |
| **Johnny.Decimal** | At most 10 areas × 10 categories × 100 IDs, written as `AC.ID` (e.g. `31.04`). Only **two levels deep**, and nothing is stored in areas or categories themselves, only in IDs. | https://johnnydecimal.com/documentation/areas-and-categories, https://johnnydecimal.com/10-19-concepts/11-core/11.01-introduction/ |
| **MOCs / LYT** (Nick Milo) | A "Map of Content" is a note of curated links about one topic. A **Home** note links to the MOCs. Links stop notes getting trapped in one folder, and MOCs stop you getting lost in the web of links. | https://obsidian.rocks/maps-of-content-effortless-organization-for-notes/, https://yu-wenhao.com/en/blog/lyt-framework-guide/ |
| **kepano's "bottom-up" vault** | Few folders and no nesting. Notes are organised by a `categories` **property**, and category pages are **Bases**. Link profusely, use `YYYY-MM-DD` dates everywhere, pluralise tags, default to `list` properties, keep one template per category, and write a style guide. | https://stephango.com/vault |

### Recommendation for this vault (a hybrid)

1. **Keep the existing numbered top folders (`00-quotr` … `08-action-plan`, `_meta`).** This is effectively a lightweight Johnny.Decimal "areas" layer. It is already familiar and sorts well in the file explorer. Do **not** add nested sub-folders beyond what exists. Johnny.Decimal's two-level rule and kepano's no-nesting rule agree on this.
2. **Put a `Home.md` (the front door) and one MOC per folder on top.** The existing `README.md` becomes `Home.md`, or `README.md` gets pinned as the Home note with a bookmark. Each folder gets a `00 Index` note (e.g. `03-market/03 Market MOC.md`) that is **mostly embedded Bases** plus a few curated links. The consultant navigates Home → MOC → item, never the raw file tree.
3. **Make properties, not folders, the main query dimension.** Every note gets `type:` (e.g. `fact-sheet`, `competitor`, `prompt`, `roadmap-item`, `test-run`, `playbook`, `template`, `kpi`, `decision`, `daily`). Bases filter on `type == "prompt"`. This is more stable than folder or tag filters, which "drift during refactors" (got.md schema rule 1: https://got.md/obsidian-bases/).
4. **Atomic notes versus long notes.** Split a document when its rows are **records with their own lifecycle** (status, owner, date, result) that people will filter, sort, link to or update one at a time. Keep narrative pages long when they are read top to bottom (fundamentals, style guide, playbooks, fact sheet).

| Current file | Recommendation | Why |
|---|---|---|
| `04-prompt-library/prompt-library.md` (200+ prompts) | **Split: one note per prompt** in `04-prompt-library/prompts/` named by stable ID (`E07 Togal.AI alternatives.md`). The old page becomes a MOC with a Base table. | Each prompt has a stage, persona, trade, priority, target URL and a **test history**. Test-run notes must link to a prompt. Large markdown tables lag in the editor (see §6). |
| `04-prompt-library/tracking-set.md` | Drop it as a separate table. Make it a `tracking: true` checkbox property on prompt notes plus a Base view "Tracking set". | Removes duplicated data that can drift out of sync. |
| `05-content-strategy/content-roadmap.md` (68 items) | **Split: one note per roadmap item** (`05-content-strategy/roadmap/R012 Togal alternatives page.md`) with `status`, `priority`, `owner`, `due`, `target_prompts` (links), `url`. The MOC holds a Base table plus a Kanban view (see §2). | Items move through statuses daily, and a Kanban board over files is the natural daily view. |
| `03-market/competitors/*.md` | **Already one note per competitor.** Add frontmatter (`type: competitor`, `tier`, `pricing_from`, `g2_reviews`, `last_verified`) and let `competitor-landscape.md` embed a Base. | The data becomes sortable, and staleness can be tracked per competitor. |
| `buyer-questions-by-trade.md`, `construction-glossary.md` | Keep them long (reference reading). Optionally split the glossary later if terms become link targets. | They are read as documents, not managed as records. |
| `02-current-state/ai-visibility-baseline.md` | Keep it as the **narrative summary** of the first baseline. Put the raw per-prompt results in test-run notes (§3). | The narrative is read once; the results are queried forever. |
| `00-quotr/entity-fact-sheet.md` | Keep it as one note (the single source of truth), but give each fact a block ID (`^fact-hq`, `^fact-price-lite`) so other notes **embed** facts instead of copying them (§2). | One fact lives in one place. |

5. **Naming.** Use sentence-case file names with a stable ID prefix for records (`E07 …`, `R012 …`, `2026-09-25 Perplexity E07.md`). Avoid `# | ^ : %% [[ ]]` in names, because they break links (https://obsidian.md/help/links). Put all dates in ISO format (https://stephango.com/vault).

---

## 2. Obsidian features to use (and core vs community status in 2026)

### Core features: use these, they are stable and maintained by Obsidian

- **Properties (YAML frontmatter).** The types are Text, List, Number, Checkbox, Date and Date & time. The type is fixed **per property name, vault-wide**, and stored in `.obsidian/types.json`. Commit that file so agents and humans share one schema. Default to `list` if a field might ever hold more than one value (kepano). Sources: https://obsidian.md/help/properties, https://stephango.com/vault
  - Suggested core schema: `type`, `status`, `priority`, `owner`, `tags`, `aliases`, `created`, `updated`, `last_verified` (date), `verify_every_days` (number), `source_of_truth` (checkbox), `sources` (list of links/URLs).
  - Prompt note: `id`, `stage` (learn/evaluate/decide), `persona` (list), `trade` (list), `intent`, `priority`, `tracking` (checkbox), `target_url`, `target_page` (link).
  - Test-run note: `type: test-run`, `date`, `engine` (perplexity/chatgpt/google-aio/google-ai-mode/gemini/claude/copilot), `prompt` (link), `quotr_mentioned` (checkbox), `quotr_rank` (number), `quotr_cited` (checkbox), `competitors_named` (list of links), `cited_domains` (list), `accuracy_issue` (text), `run_by` (agent/human).
- **Links.** Obsidian supports wikilinks `[[Note]]` and Markdown links `[text](path.md)`. Wikilinks are the default because they are compact. Markdown links need URL-encoding (`%20`) unless you wrap the destination in `<…>`. Folder paths start at the vault root. Settings → Files & links → `Use [[Wikilinks]]` toggles which one Obsidian writes. Source: https://obsidian.md/help/links
  - Angle-bracket destinations with spaces (what `geo-brain` uses now) **render and resolve fine**, but Obsidian **does not generate** them, and a long-standing forum request says rename handling for them is incomplete. The Better Markdown Links plugin exists to fill that gap. Sources: https://github.com/mnaoumov/obsidian-better-markdown-links, https://forum.obsidian.md/t/support-internal-links-with-markdown-angle-bracket-syntax-especially-rename/36007
  - **Recommendation:** switch to **wikilinks** for links inside the vault. They are shorter, rename-safe, and readable by agents with the kepano `obsidian-markdown` skill. Quartz 5 supports them too. Keep Markdown links only for external URLs. If GitHub rendering of the repo matters more than Obsidian, the alternative is Markdown links with Settings → "New link format: Relative path to file", and no spaces in folder names (rename `research_notes/Quotr GEO AEO strategy audit/` to `quotr-geo-audit/`). Do the conversion with a script in one PR.
  - **Make the vault root the repo root**, or move `reports/` and `research_notes/` inside the vault. Otherwise the `../reports/…` links point outside the vault and show as broken or unresolved in Obsidian.
- **Aliases** (`aliases:` property): let `[[Togal]]`, `[[Togal.AI]]` and `[[togal-ai]]` resolve to one note. This is useful for competitor and product names. Source: https://obsidian.md/help/links
- **Embeds and block references.** `![[Note#Heading]]` or `![[Note#^block-id]]` embed a section or block that updates live when the source changes. Manual block IDs may use letters, numbers and dashes. Use this for the fact sheet: other pages embed `![[entity-fact-sheet#^fact-price-lite]]` rather than copying "$79.90". Source: https://obsidian.md/help/links (block section)
- **Bases (core plugin; introduced in 1.9 in 2025, List and Map views in 1.10, Kanban in 1.14 early access).** These are database views over notes and their properties, stored in `.base` files or embedded as a ```` ```base ```` code block. Views: table, cards, list, map, and (early access) kanban. They support formulas, summaries, grouping, CSV export, and **editing properties in place**. `this` makes context-aware dashboards: embed `Tests.base#For this prompt` in every prompt note to show its history. The CLI can query them (`obsidian base:query path=… format=json`). Sources: https://obsidian.md/help/bases, https://obsidian.md/help/bases/syntax, https://got.md/obsidian-bases/, https://obsidian.md/changelog/
  - Useful formulas for this vault: staleness `if(last_verified, ((today() - last_verified) / 86400000).round(), null)`, and a stale flag `if(formula.days_since_verified > verify_every_days, "STALE", "")`. The pattern follows got.md's "due in days" recipe.
- **Bases vs Dataview.** **Default to Bases.** Dataview's author last committed in June 2024. Datacore, its successor, is still BRAT-only beta in 2026. Bases is core, editable in place, and Quartz 5 renders it. Keep Dataview only if you need inline fields or DataviewJS analytics. Sources: https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian/, https://abdulkadersafi.com/blog/dataview-vs-datacore-vs-bases, https://github.com/blacksmithgu/datacore
- **Canvas (core, open JSON Canvas format).** Good for a one-page visual "GEO system map" or a client workshop board, e.g. Quotr entity → proof sources → review sites → AI engines. It is not a working tool for daily updates. kepano's `json-canvas` skill lets Claude write `.canvas` files. Source: https://github.com/kepano/obsidian-skills
- **Graph view (core).** Nice for spotting orphan notes. Low daily value for a non-technical user. The CLI `orphans` / `deadends` / `unresolved` commands are more actionable for agent QA. Source: https://obsidian.md/help/cli
- **Daily notes (core)** and the **Templates core plugin** (`{{date}}`, `{{time}}`, `{{title}}`). These are enough for the consultant's daily note. The CLI can `daily:append` from agents. Source: https://obsidian.md/help/cli
- **Callouts (core Markdown extension).** `> [!warning] TO CONFIRM with Quotr`, `> [!important] Source of truth`, `> [!info] Last verified 2026-09-25`. They make status visible to a non-technical reader, and Quartz renders them. Source: https://quartz.jzhao.xyz/features/callouts
- **Bookmarks (core):** pin Home, Today's daily note, "Stale facts" Base, "This week's roadmap" Base.
- **Web Clipper (official)** for saving competitor pages or AI answers into `Clippings/` with properties. Source: https://stephango.com/vault

### Community plugins (keep to a minimum; each one runs code with full access to the vault)

| Plugin | 2026 status | Verdict for this vault |
|---|---|---|
| **Obsidian Git** (Vinzent03) | Maintained. Auto commit-and-sync on an interval, pull on startup. Solid on desktop. **Its own docs call mobile "very unstable".** Sources: https://github.com/Vinzent03/obsidian-git, https://www.stephanmiller.com/obsidian-git-sync-mobile/ | **Use on desktop only** (details in §4). |
| **Templater** | Maintained and widely recommended in 2026 lists (https://aiproductivity.ai/blog/obsidian-plugins-productivity/). | **Optional.** Core Templates is enough. Add Templater only if you want prompts in templates (e.g. "Which engine?") or auto-filled dates across folders. |
| **Tasks** | Maintained. Due dates, recurrence, vault-wide task queries. | **Optional.** For a non-technical user, a roadmap Base with `status`/`due` properties is simpler than Tasks emoji syntax. Plain `- [ ]` checklists in daily notes plus the CLI `tasks` command cover the rest. |
| **Periodic Notes** | Still listed in 2026 guides (https://automatemylife.blog/best-obsidian-plugins-2026/). | **Optional.** Weekly and monthly notes can simply be template-created notes in `_meta/reviews/`. |
| **Kanban** (mgmeyers) | **Looking for new maintainers.** Last release 2.0.51 on 2024-05-31. Sources: https://github.com/mgmeyers/obsidian-kanban/blob/main/MAINTAINERS.md, https://www.obsidianstats.com/plugins/obsidian-kanban | **Avoid.** Use the **Bases Kanban layout** (1.14; early access now, public soon) grouped by `status`. Until then, use a Bases table grouped by status. |
| **Dataview** | Maintained only lightly. | **Avoid for new work.** Use Bases. |
| **Local REST API** (coddingtonbear) | Active. **Built-in MCP server at `/mcp/` since v5.0 (July 2026)**, with 15 tools (vault read/write/append/patch, search, periodic-note paths, commands). Sources: https://github.com/coddingtonbear/obsidian-local-rest-api, https://contextbolt.com/blog/obsidian-mcp-claude/ | **Optional.** Only for Claude Desktop/Code talking to a *running* local Obsidian. Not needed for the Git-based workflow. |

Security: Obsidian cannot sandbox plugins, so they inherit the app's access. Obsidian's small team cannot review every plugin release. Fewer plugins means a smaller attack surface. Sources: https://obsidian.md/help/plugin-security, https://news.ycombinator.com/item?id=45307242

---

## 3. Daily and ongoing update workflows

### Folder additions

```
_meta/
  daily/            2026-09-25.md …        (consultant daily log)
  reviews/          2026-W39 weekly.md, 2026-09 monthly.md
  decisions/        2026-09-25 Use G2 as primary review site.md
  changelog.md      (append-only, one line per change; agents write here)
  templates/        Daily.md, Weekly review.md, Test run.md, Prompt.md, Roadmap item.md, Decision.md, Competitor.md
  bases/            Prompts.base, Tests.base, Roadmap.base, Staleness.base, Competitors.base
07-measurement/
  test-runs/        2026-09-25 perplexity E07.md …   (one note per prompt per engine per run)
```

### Daily note template (for the consultant; about 5 minutes a day)

```markdown
---
type: daily
date: {{date:YYYY-MM-DD}}
---
# {{date:YYYY-MM-DD}}

> [!summary] What the agent did overnight
> (Claude appends a summary here: new test runs, changed facts, stale pages, open PRs)

## Today's prompt checks
- [ ] Spot-check 3 tracking prompts in ChatGPT / Google AI Mode (log each as a test run)

## Changes I made / learned
- 

## Client asks / decisions
- 

## Links
![[Staleness.base#Stale this week]]
![[Roadmap.base#Due this week]]
```

The agent writes the callout through the CLI (`obsidian daily:append content=…`) or, in the Git flow, by editing `_meta/daily/YYYY-MM-DD.md` directly.

### Weekly and monthly reviews

- **Weekly (Friday, about 20 min):** a template embeds `Tests.base#Last 7 days` (mention rate by engine), `Roadmap.base#Moved this week`, and `Staleness.base`. The consultant writes 3 bullets: wins, risks, next week. Claude can pre-draft the review from the week's daily notes, a pattern described in https://www.buildmvpfast.com/blog/obsidian-claude-ai-knowledge-management-system-2026 (practitioner).
- **Monthly:** re-run the full tracking set across all engines, update `07-measurement/kpis-and-dashboard.md` from Base summaries, review decisions, and archive completed roadmap items (`status: done`). kepano's "review the reviews" fractal pattern (daily → monthly → yearly) fits here: https://stephango.com/vault

### Changelog and decision log

- `_meta/changelog.md`: **append-only**, newest first, one line per change: `2026-09-26 · agent · updated [[entity-fact-sheet]] ^fact-price-lite (Lite $79.90 confirmed on /pricing) · PR #12`.
- `_meta/decisions/`: one note per decision (`type: decision`, `date`, `status: proposed|accepted|superseded`, `supersedes: [[…]]`). A decision Base shows accepted decisions. This is an ADR-style log, so "why did we do X" has an answer.

### Staleness flags and source-of-truth facts

- Every note gets `last_verified` (date) and `verify_every_days` (e.g. fact sheet 30, competitor 60, fundamentals 180). A **Staleness Base** computes days since verification and flags STALE (formula in §2). This replaces the free-text "**Last updated:**" line. Keep that line only as a rendered callout for GitHub readers, or drop it.
- **Source-of-truth rule:** facts live in `00-quotr/entity-fact-sheet.md` with block IDs, and every other page **embeds** them. A fact marked "TO CONFIRM" uses a `> [!warning]` callout and `status: to-confirm`, so a Base can list all unconfirmed facts.
- Agents must update `last_verified` **only** when they actually re-checked a source, and must cite the URL in `sources`.

### Tracking AI-visibility tests over time (one note per test run)

- **One note = one prompt × one engine × one date.** Properties as in §2. The body holds the raw answer text (or an excerpt), the cited URLs, and notes.
- **Why one note per run:** Bases can then compute trends (group by `engine`, filter `date >= today() - "30d"`, summary = % `quotr_mentioned`). Each prompt note embeds `Tests.base#For this prompt` (filter `prompt == this`, or `file.hasLink(this.file)`) to show its own history. Competitor notes embed `list(competitors_named).contains(this)` views. This is got.md's "People + Meetings" `this` pattern applied to prompts and tests: https://got.md/obsidian-bases/
- **Volume check:** about 40 tracking prompts × 7 engines × 4 runs a month ≈ 1,100 notes a month, or roughly 13k a year. That is fine for Obsidian: reported slowdowns start around 50k notes (https://forum.obsidian.md/t/help-obsidian-lags-with-many-notes/82241), and 1.14.2 removed the simplified search algorithm above 10k files (changelog). Still, **archive by year** (`test-runs/2026/`), keep bodies short, and if run volume grows, consider a monthly roll-up note plus CSV export (Bases "export view as CSV", fixed in 1.14.2).
- Base example (`Tests.base`):

```yaml
filters:
  and:
    - 'type == "test-run"'
formulas:
  mentioned_num: 'if(quotr_mentioned, 1, 0)'
views:
  - type: table
    name: Last 30 days
    filters:
      and:
        - 'date >= today() - "30d"'
    groupBy: engine
    order: [date, prompt, engine, quotr_mentioned, quotr_rank, competitors_named]
  - type: table
    name: For this prompt
    filters:
      and:
        - 'prompt == this'
    order: [date, engine, quotr_mentioned, quotr_rank]
```

(Check the exact YAML keys against https://obsidian.md/help/bases/syntax before shipping, because the syntax changed in early versions per got.md.)

---

## 4. AI + Obsidian

### Recommended architecture: the GitHub repo is the hub

```
GitHub repo (quotr)  ← source of truth, PR review, history
   ↑ push branch claude/*  (Claude Code cloud routine, nightly)
   ↑ push/pull            (Claude Code local sessions, the developer)
   ↕ Obsidian Git plugin  (consultant's DESKTOP vault; auto-pull on open, auto commit-and-sync every 10–15 min)
   ↓ GitHub Action        (Quartz 5 build → client site)
Phone: read-only via the published site, or a separate sync path (see pitfalls)
```

- **Obsidian Git (desktop):** set "pull on startup", auto commit-and-sync every 10–15 minutes, and "commit-and-sync after stopping file edits". On desktop it shells out to real git, so it behaves exactly like git. Sources: https://github.com/Vinzent03/obsidian-git, https://www.stephanmiller.com/obsidian-git-sync-mobile/
- **`.gitignore`:** ignore `.obsidian/workspace*.json`, `.obsidian/cache`, `.trash/`. **Commit** `.obsidian/types.json`, `.obsidian/app.json` (link settings), `.obsidian/core-plugins.json`, `.obsidian/community-plugins.json`, templates and `.base` files, so every device and agent shares the schema.

### Claude Code working directly in the vault

- **`CLAUDE.md` in the vault root** is the standard pattern. It holds the numbered structure, the frontmatter schema, and rules for how Claude behaves inside the vault. Add a `.claude/` folder with skills. Sources: https://kennethreitz.org/essays/2026-03-06-obsidian_vaults_and_claude_code, https://www.stefanimhoff.de/writing/agentic-note-taking-obsidian-claude-code/, https://blog.starmorph.com/blog/obsidian-claude-code-integration-guide (practitioner)
- **Install kepano/obsidian-skills** into `.claude/skills/` so Claude writes valid wikilinks, callouts, properties, `.base` YAML and `.canvas` JSON: https://github.com/kepano/obsidian-skills
- **Agent-safe conventions to put in CLAUDE.md:**
  1. Never rename or move a note with plain `mv`. Use `obsidian move`/`rename` (the CLI updates links when "Automatically update internal links" is on), or run a link-rewrite script plus an `unresolved`-links check in the same commit. Sources: https://obsidian.md/help/cli (move/rename)
  2. Never change a property's **type** (types.json is vault-wide). Only add properties listed in the schema section.
  3. Facts: edit only `entity-fact-sheet.md`, always with a source URL and an updated `last_verified`. Never copy facts into other pages; embed them instead.
  4. Test runs: create new notes only. Never edit past runs (they are an append-only history).
  5. Every change adds a line to `_meta/changelog.md`.
  6. Keep notes under about 300 lines. Split instead of growing tables.
  7. Don't touch `.obsidian/` except `types.json` via PR.
  8. Mark anything uncertain `status: to-confirm` with a `> [!warning]` callout.
- **Checks to run before commit** (script or skill): unresolved links = 0 (`obsidian unresolved total` when the app is running, or a small script in CI), YAML parses, required properties present, no property-type conflicts.

### MCP and Local REST API (optional, local only)

- The Local REST API plugin (v5+) serves MCP at `https://127.0.0.1:27124/mcp/` with a bearer token. Claude Code supports HTTP MCP natively. Tools: `vault_read/write/append/patch`, `search_query`, `periodic_note_get_path`, `command_execute`, and so on. Sources: https://github.com/coddingtonbear/obsidian-local-rest-api, https://mcp.directory/blog/obsidian-mcp-complete-guide-2026
- **Use it when:** the consultant chats with Claude Desktop and wants it to read or append the open daily note while Obsidian is running. **Don't rely on it** for scheduled cloud work (Obsidian isn't running there). Plain file access plus Git is simpler, and the diffs are reviewable.
- **Alternative inside Obsidian:** Claudian or the Claude Sidebar plugins embed Claude Code in Obsidian's side panel (https://community.obsidian.md/plugins/realclaudian). This adds convenience but also another community plugin to trust.

### Scheduled and remote agents doing daily updates

- **Claude Code routines** (research preview since April 2026; Pro/Max/Team/Enterprise): a saved prompt + repos + connectors, triggered by a **schedule** (minimum hourly), an **API POST**, or **GitHub events** (PR/release). They run on Anthropic cloud with the laptop closed. They clone the repo from its default branch and **push only to `claude/`-prefixed branches** by default. Pushes to protected branches are rejected. Create them at claude.ai/code/routines or with `/schedule` in the CLI. A green run status means "no infra error", not "task succeeded", so read the transcript. Source: https://code.claude.com/docs/en/routines
- **Suggested routines:**
  1. **Nightly "prompt test" routine (weekdays, e.g. 06:45 local).** Run the tracking prompts on engines reachable via API or connector (e.g. Perplexity Sonar). Write one `test-runs/` note per result. Append a summary callout to today's daily note. Update `changelog.md`. Open a PR titled `Daily GEO update YYYY-MM-DD`. API keys go in the environment's credentials, not in the repo. Allow the engine's domain in the environment's network settings.
  2. **Weekly "staleness and QA" routine.** Query staleness, re-verify stale fact-sheet items and competitor pricing pages, and fix unresolved links. Open a PR with the changes and a checklist of what still needs a human.
  3. **GitHub-trigger routine on `pull_request.opened`** from `claude/*`. A second pass reviews the agent's own PR against the CLAUDE.md rules (schema, links, sources).
- **Review model for a non-technical owner:** keep `main` protected and let routines open PRs. Either the consultant merges from the GitHub mobile app after reading the summary, or a technical owner merges. Low-risk classes (new test-run notes only) can be auto-merged by a required-checks workflow, while fact changes always need a human. Obsidian Git on the consultant's desktop pulls the merged result the next time the app opens.
- **Conflicts:** they arise when the consultant edits the same file the agent edited before pulling. Mitigations: (a) agents mostly **create new files** (test runs, decisions) rather than editing shared ones; (b) the daily note has an agent section and a human section, and the agent only appends; (c) auto-pull on startup plus short commit intervals; (d) a scheduled time window for agents (overnight). Git conflicts inside Obsidian are awkward for non-technical users. The Git Vault Sync and Git Sync community plugins offer conflict UIs (https://community.obsidian.md/plugins/git-vault-sync), but prevention beats resolution.
- **Alternative if Git is too technical for the consultant:** Obsidian Sync (Standard $4/mo annual, Plus $8/mo; shared vaults need every collaborator to have Sync) on the consultant's devices, plus **Obsidian Headless `ob sync --continuous`** on a small server where agents edit files and commit to GitHub for history. Sources: https://obsidian.md/blog/standard-plan/, https://obsidian.md/help/sync/collaborate, https://obsidian.md/help/sync/headless. Trade-off: you lose PR review before changes reach the consultant, unless agents write to a staging folder.

---

## 5. Sharing with the client

| Option | Cost and effort | Access control | Notes | Source |
|---|---|---|---|---|
| **Obsidian Publish** | $8/site/mo annual, $10 monthly. No build pipeline. | **Site-wide password only**; no per-page protection. | Easiest for a non-technical owner: choose notes and click publish. Graph and search included. Headless and CLI (`publish:add changed`) allow automation. | https://unmarkdown.com/blog/obsidian-publish-alternatives, https://help.obsidian.md/publish/security, https://obsidian.md/help/cli |
| **Quartz 5** (released Sept 2026) | Free. GitHub template + GitHub Actions → GitHub Pages / Cloudflare / Netlify / Vercel. Node 22+. | **EncryptedPages plugin:** per-page AES-256-GCM passwords from a frontmatter field, `unlisted`/`stealth` options. Client-side only: "protects against casual browsing, not determined attackers". Also ExplicitPublish, RemoveDrafts, UnlistedPages. | **Renders Bases (`BasesPage`) and Canvas**, plus wikilinks, callouts, backlinks and graph. Best fit for the Git-hub architecture: every merged PR rebuilds the site. | https://quartz.jzhao.xyz/, https://quartz.jzhao.xyz/plugins/encryptedpages, https://quartz.jzhao.xyz/features/bases |
| **Shared Obsidian Sync vault** | The client needs their own Sync subscription. | Per-vault. | Real collaboration, but the client must install Obsidian. | https://obsidian.md/help/sync/collaborate |
| **Export** | Free. | n/a | Bases view → CSV (the prompt/roadmap tables for spreadsheets). The core plugin exports a note to PDF. Plain markdown files open anywhere ("file over app"). | https://obsidian.md/changelog/, https://stephango.com/file-over-app |

**Recommendation:** Quartz 5 on a private-ish URL, using `ExplicitPublish` so only notes with `publish: true` go out. Keep `_meta/`, drafts and internal notes out. Use EncryptedPages or host-level auth (e.g. Cloudflare Access) for anything sensitive. Use Obsidian Publish instead if nobody technical will maintain a build.

---

## 6. Pitfalls

- **Huge files and tables.** Large markdown tables stutter while typing, and notes made mostly of tables with long cell text have glitched when scrolling or reopening. Sources: https://forum.obsidian.md/t/large-markdown-table-causes-slowness/78593, https://forum.obsidian.md/t/a-note-with-multiple-large-tables-glitches-out-corrupts-content/78402. This is the strongest argument for splitting the prompt library and roadmap into one note per item plus Bases views.
- **Broken links on rename.** Obsidian updates links only when the rename happens *inside Obsidian* (or through the CLI) and "Automatically update internal links" is on. Renames by git, Finder or an agent's `mv` break links silently. Angle-bracket Markdown links are not generated by Obsidian and have weaker rename support. Mitigations: wikilinks, CLI moves, unresolved-link checks in CI. Sources: https://obsidian.md/help/cli, https://forum.obsidian.md/t/support-internal-links-with-markdown-angle-bracket-syntax-especially-rename/36007
- **Links pointing outside the vault.** The current `../reports/…` and `../research_notes/…` links will not resolve if only `geo-brain/` is opened as the vault. Open the repo root as the vault, or move the sources in.
- **Over-linking.** Linking every mention creates graph noise and hides important links. Link first mentions of entities (kepano's rule: https://stephango.com/vault), link records to their parents (test run → prompt → roadmap item), and let MOCs and Bases do the aggregation.
- **Plugin bloat.** Each community plugin is unsandboxed code with full access (https://obsidian.md/help/plugin-security), and abandoned plugins break (Kanban: https://github.com/mgmeyers/obsidian-kanban/blob/main/MAINTAINERS.md). Target: **core only, plus Obsidian Git**, and optionally Templater. Bases replaces Dataview and Kanban.
- **Property type conflicts.** One name has one type vault-wide. If an agent writes `priority: "high"` in one note and `priority: 1` in another, filters silently fail. Commit `types.json` and validate in CI. Watch for `tags.contains()` vs `file.hasTag()` and list vs scalar mismatches in Bases (https://got.md/obsidian-bases/).
- **Mobile sync with Git.** The Git plugin on iOS and Android uses isomorphic-git: no SSH, no rebase, no LFS, and it can crash on clone or pull depending on free RAM. The author discourages mobile use. For mobile, use GitSync (native git client app), Obsidian Sync, or read the published site. **Never point two sync systems at the same folder.** Source: https://www.stephanmiller.com/obsidian-git-sync-mobile/
- **Bases caveats.** Filters placed in "This view" rather than global, `this` changing meaning when embedded, and image-heavy card views crashing on mobile (https://got.md/obsidian-bases/). The Kanban layout is early access until 1.14 goes public.
- **Agent overreach.** Routines run autonomously with every included connector's write access. Remove unneeded connectors, keep `main` protected, and remember a green run status ≠ success (https://code.claude.com/docs/en/routines).
- **"Don't delegate understanding."** kepano deliberately does his reviews by hand (https://stephango.com/vault). Keep the consultant's weekly review human-written, even if Claude pre-drafts the data.

---

## Migration checklist (concrete, in order)

1. Open the **repo root** as the vault. Commit `.obsidian/` config (minus workspace files) and add a `.gitignore`.
2. Add `CLAUDE.md` (vault rules, schema), `.claude/skills/` (kepano obsidian-skills), and `_meta/templates/`.
3. Script pass 1: add YAML frontmatter to all 68 files (`type`, `last_verified` from the existing "Last updated" line, `verify_every_days`, `sources`).
4. Script pass 2: convert internal Markdown links to wikilinks. Rename the `research_notes/Quotr GEO AEO strategy audit/` folder to one without spaces. Verify 0 unresolved links.
5. Script pass 3: split `prompt-library.md` and `tracking-set.md` into prompt notes, and `content-roadmap.md` into roadmap-item notes. Convert the Sept 2026 Perplexity baseline (40 prompts) into `test-runs/` notes.
6. Create `Prompts.base`, `Tests.base`, `Roadmap.base` (table + kanban), `Staleness.base`, `Competitors.base`, and a MOC per folder that embeds them. Turn `README.md` into `Home.md`.
7. Install Obsidian Git on the consultant's desktop. Protect `main`. Create the nightly and weekly Claude Code routines that open PRs.
8. Set up Quartz 5 with ExplicitPublish, deployed by GitHub Actions, for the client view.
