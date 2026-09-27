---
type: task
id: A3
task: 'Fact-fix sweep, part 2: every other conflicting fact, including schema legal name'
phase: Days 1–30 (Oct 2026)
month: 2026-10
week: 2
rank: 3
owner: Marketing + dev
effort: M
impact: H
depends_on:
- '[[A1 Agree and sign off one fact sheet|A1]]'
depends_on_text: A1
status: todo
done_when: a spot-check of the homepage, /software/, /service/, /procurement/, /pricing/, /faq/, /about-us/, /disambiguation/, llms.txt and 10 random blog posts finds one value per fact; the schema shows one Organization with one legal name. Do not add new schema types as a lever; the report says "Fix the conflict; don't expand the markup."
---
# A3. Fact-fix sweep, part 2: every other conflicting fact

- **What:** Copy the approved A1 values onto every page, file and schema block that disagrees: factory count; savings claims ("up to 50%", "40–50%", "40–55%"); turnaround; HQ (including blog footer boilerplate "based in San Francisco"); founders; funding; target audience; trade count (23 trade pages vs "26 sub-trades"); takeoff-time claim (the /software/ page says "up to 80% — from around 20 hours to just 1–2", which is really a 90–95% cut); procurement totals on /procurement/; delivery area. Fix the site-wide Organization schema so it says `name: "Quotr.ai"` and `legalName: "FLOZ Inc."` everywhere (today the homepage says `legalName: "Quotr.ai"` and /disambiguation/ says "FLOZ Inc" under the same ID).
- **Why (evidence):** When pages disagree, AI hedges, guesses or averages (report). The conflicts are confirmed on Quotr's own pages (verification file, claims 8, 11, 12, 14, 17, 18).
- **Owner:** Marketing (copy); dev (schema).
- **Effort / Impact:** M / H.
- **Depends on:** A1.
- **Done when:** a spot-check of the homepage, /software/, /service/, /procurement/, /pricing/, /faq/, /about-us/, /disambiguation/, llms.txt and 10 random blog posts finds one value per fact; the schema shows one Organization with one legal name. Do not add new schema types as a lever; the report says "Fix the conflict; don't expand the markup."
- **How-to:** [[Optimize vs create]] (sweep sections A and B); [[Schema markup kit]] §5.1 and §7; [[FAQ block template]] (approved answer bank).

---

Part of [[30-60-90 plan#Days 1–30 (about October 2026): quick wins and clean-up|30-60-90 plan › Days 1–30]]
