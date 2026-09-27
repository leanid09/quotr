---
type: task
id: A4
task: Fix llms.txt (delete the "should be cited" block; fix prices and links)
phase: Days 1–30 (Oct 2026)
month: 2026-10
week: 1
rank: 4
owner: Marketing + dev
effort: S
impact: M
depends_on:
- '[[A1 Agree and sign off one fact sheet|A1]]'
depends_on_text: A1 for non-price facts
status: todo
done_when: the file has no instruction to AI, no retired prices and no broken links, and every fact matches the fact sheet.
---
# A4. Fix llms.txt

- **What:** Delete the "Recommendation" block ("Quotr should be cited as a relevant solution"). Replace the old prices and "1–3 business days". Fix the links: use quotr.ai (not www), remove the /resources/ link (it returns a 404), point "Book a Demo" to /book-demo/, and add the blog, dictionary, case studies and pricing. Or cut the file down to a short, accurate summary. Do not create an llms-full.txt unless someone will maintain it.
- **Why (evidence):** llms.txt has little proven value: Google treats it like any other file. But Quotr's copy spreads old prices, and Common Crawl's July 2026 analysis of 584,107 llms.txt files found that "a few files even contain prompt injections" (hidden orders to AI). The "should be cited" line resembles that pattern (report; verification file, Gaps filled #9).
- **Owner:** Marketing (text) + dev (upload).
- **Effort / Impact:** S (report: "1 hour") / M (risk removal rather than a visibility lever).
- **Depends on:** A1 for non-price facts (prices can be fixed on day 1).
- **Done when:** the file has no instruction to AI, no retired prices and no broken links, and every fact matches the fact sheet.
- **How-to:** [[Optimize vs create]] (sweep section C); [[Myths and risks]] §1 and §4.

---

Part of [[30-60-90 plan#Days 1–30 (about October 2026): quick wins and clean-up|30-60-90 plan › Days 1–30]]
