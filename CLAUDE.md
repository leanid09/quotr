# Rules for AI helpers in this vault

This repository is an **Obsidian vault**: the Quotr.ai GEO knowledge brain. A non-technical GEO consultant opens it in Obsidian every day. Every change must keep it readable, linked and consistent. Read [[Start here]] for what the brain contains.

## Map

| Path | What it is | Can you edit it? |
|---|---|---|
| `Home.md` | The daily dashboard (opens at startup) | Yes, carefully |
| `geo-brain/` | The knowledge, in numbered folders `00-quotr` … `08-action-plan` | Yes, following the rules below |
| `*.base` files | Live tables (Obsidian Bases). Pages embed their views by name: `![[Tasks.base#Next up]]` | Yes; never rename a view that is embedded |
| `geo-brain/_meta/note-templates/` | Templates for new notes | Yes |
| `geo-brain/_exports/` | Plain-text copies of the live tables, for AI tools and GitHub | Never by hand: run the export script |
| `journal/` | The consultant's daily notes and reviews | **Never** |
| `reports/`, `research_notes/` | Dated evidence | **Never** change the text |
| `.obsidian/` | Shared Obsidian settings | Only `types.json`, and only when you add a property |

## Notes that are records (one note per item)

| Kind | Folder | `type` | File name | Key properties |
|---|---|---|---|---|
| Prompt (buyer question) | `geo-brain/04-prompt-library/prompts/` | `prompt` | `E-001 best AI takeoff software for subcontractors 2026` | `id`, `prompt` (word for word), `stage`, `group`, `persona`, `trade`, `intent`, `priority`, `page_status`, `tracking`, `tracking_id`, `tier` |
| AI test run | `geo-brain/07-measurement/test-runs/YYYY-MM/` | `test-run` | `2026-10-06 ChatGPT T01` | `date`, `engine`, `test_id`, `test_set`, `prompt_note` (link), `prompt`, `branded`, `quotr_named`, `quotr_sources`, `competitors_named` (links), `result_summary` |
| Content piece | `geo-brain/05-content-strategy/roadmap/` | `roadmap-item` | `R-07 DDP vs FOB for building materials …` | `id`, `title`, `cluster`, `target_prompts` (links), `priority`, `month` (`YYYY-MM`), `status`, `owner` |
| Task | `geo-brain/08-action-plan/tasks/` | `task` | `A1 Agree and sign off one fact sheet` | `id`, `task`, `phase`, `rank`, `owner`, `effort`, `impact`, `depends_on` (links), `status`, `done_when` |
| Open question | `geo-brain/00-quotr/open-questions/` | `question` | `Q-01 Headquarters` | `id`, `question`, `topic`, `ask` (`Quotr` or `us`), `status`, `answer`, `answered_on` |
| Blog article (health record for a live Quotr post) | `geo-brain/02-current-state/articles/` | `article` | `BP-45 quotr vs togal ai comparison 2026` | `id`, `title`, `quotr_url`, `published`, `cluster`, `format`, `byline`, `health`, `health_score`, `action`, `merge_into`, `priority`, `rank`, `status`, `flags` |

Status values: tasks `todo`, `doing`, `blocked`, `done`, `dropped` · content `planned`, `writing`, `published`, `refreshed`, `dropped` · questions `open`, `answered` · articles `ok` (no work needed), `todo`, `doing`, `done`, `dropped`.

Every other page (guides, plans, playbooks, profiles) has `type`, a one-line `description`, `last_verified` (the date someone last checked it against its sources) and `verify_every_days` (how often to re-check), plus optional `aliases`.

## Rules

1. **Links.** Use wikilinks for anything inside the vault: `[[Note name]]`, `[[Note name#Heading]]`, `[[Note name|shown text]]`. Inside a table cell, escape the pipe: `[[Note name\|shown text]]`. Keep normal Markdown links for web addresses.
2. **Unique names.** Links use the file name only, so every file name must be unique. Check before you create a note. Do not rename or move notes; if you must, update every link in the same commit.
3. **Properties.** Use only the properties above and in `.obsidian/types.json`, with the same type (a list stays a list). Put links in properties in quotes: `"[[E-001 best AI takeoff software for subcontractors 2026|E-001]]"`. Dates are `YYYY-MM-DD`.
4. **Facts about Quotr** live in [[Entity fact sheet]]. Change a fact there first, with its source, then update the other pages. Never state a TO CONFIRM fact as true.
5. **History is append-only.** Never edit a past test run; add a new one. Never delete a prompt, task, content piece or question; set its status to `dropped` or `answered` instead.
6. **Last checked.** Change `last_verified` only when you really re-checked the page against its sources.
7. **Changelog.** Add an entry at the top of [[Changelog]] for every change to facts, numbers, plans or structure.
8. **Answers from Quotr.** When a question is answered: fill `answer` and `answered_on`, set `status: answered`, update the fact sheet, and log it in the changelog.
9. **Before every commit**, run both commands and fix anything they report:
   - `python3 .claude/scripts/vault_check.py` (must end with `0 problems`)
   - `python3 .claude/scripts/build_exports.py` (refreshes `geo-brain/_exports/`)
10. **Git.** Work on a `claude/…` branch and open a pull request for the consultant to approve. Never push to `main`.
11. **Style.** Plain English, short sentences, one idea per bullet. For anything that will be published, follow [[GEO writing style guide]].

## Recording an AI test run

1. Create `geo-brain/07-measurement/test-runs/YYYY-MM/YYYY-MM-DD Engine T##.md` from `geo-brain/_meta/note-templates/Test run.md`: one note per prompt, per engine, per run.
2. Fill the properties. For the monthly run, `test_set` is `YYYY-MM tracking` and `test_id` is the tracking ID (`T01` … `T53`). Link `prompt_note` to the prompt note. List profiled competitors in `competitors_named` as links (`"[[STACK]]"`, `"[[Togal AI]]"` …) and put the answer, or its key part, in the body.
3. Add one changelog line for the run. The tables on Home, in [[Tracking set]] and in each prompt note update by themselves.
