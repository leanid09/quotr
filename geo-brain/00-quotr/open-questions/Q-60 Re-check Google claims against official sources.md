---
type: question
id: Q-60
question: 'Re-check the 135 Google claims (IDs such as RANK-13) on the Google search updates page against official Google sources, once a new session has search allowance. Start with the claims we quote to Quotr.'
topic: K. Still unverified (for us to check)
ask: us
status: open
answer:
answered_on:
---
# Q-60 · Re-check Google claims against official sources

> [!question] To check ourselves
> Re-check the 135 Google claims (IDs such as RANK-13) on the Google search updates page against official Google sources, once a new session has search allowance. Start with the claims we quote to Quotr.

**Why we check:** none of the 135 claims was re-checked on 2026-09-26, because the search limit ran out. See [[Google search updates 2025-2026#Claim register]].

- **Found today.** 42 claims on ranking updates (RANK) and Search Console (GSC) were found by live web search on 2026-09-26. None was re-checked by a second search.
- **Carried over.** 93 claims on indexing (INDEX), AI Overviews and AI Mode (AI), quality rules (QUALITY), freshness (FRESH) and other engines (OTHER) come from the research of 2026-09-25.
- **No official page.** 80 of the 135 claims list no official Google page among their sources. 20 of those are about other engines (such as Bing or ChatGPT), so the right check there is that engine's own page, not Google's.
- **Press only.** Some facts rest on industry press alone, such as both Page indexing report freezes (GSC-11, GSC-17). The claim register lists only press for the "Search generative AI" control (GSC-15), but [[Tracking setup]] §3.3 links a Search Console help page for it. Start there.

**Start with these**

| Claims | What they say (short) | Why it matters | Official Google source listed? |
|---|---|---|---|
| RANK-21 | The September 2026 spam update began on 2026-09-24 and may take up to two weeks | Sets when merges and redirects can start | Yes |
| RANK-13 | The May 2026 core update ran from 2026-05-21 to 2026-06-02 | Before-and-after windows in the Search Console audit | Yes |
| RANK-07, RANK-15, INDEX-20, QUALITY-10 | Sites that rank themselves first in their own "best X" lists lost about 30-50% of Google visibility from January 2026 | The main risk for Quotr's 22 list posts | No (a practitioner's report) |
| QUALITY-12 | Google has not confirmed that pattern | Keeps our warning fair | No |
| GSC-12 | Impressions were over-counted until 2026-04-27 | Older Search Console data needs care | Yes |
| GSC-13, GSC-14, GSC-16 | The Generative AI report shows impressions only, for all sites since 2026-08-31 | AI impressions per post | Yes |
| GSC-15 | A "Search generative AI" control can take a site out of AI features | It must stay off | No |
| GSC-11, GSC-17 | The Page indexing report froze twice | Read the report's date first | No |
| INDEX-05, AI-05, AI-08, QUALITY-05 | Google's AI features guidance: be indexed and allow snippets; no special tricks; a page for every query variation can count as scaled content abuse | What we tell Quotr to do and not do | Yes |

For the practitioner claims there is no official Google page to find. Confirm the original report instead, and check that Google has still not commented.

**How to check**

1. Use the re-check steps in [[Google search updates 2025-2026#How sure are we?|How sure are we?]] on the Google search updates page.
2. Fix any wrong claim on that page. Change its `last_verified` only after the whole page has been checked.
3. Also settle one mismatch: [[Tracking setup]] §3.4 says the branded-queries filter reached all eligible sites on 2026-03-11, while GSC-08 says about March 2026, with the exact date unknown.

## Answer

*When checked: put the finding in the `answer` property, fill `answered_on`, set `status` to `answered`, and add a line to [[Changelog]].*

---

From [[Google search updates 2025-2026]] · K. Still unverified (for us to check)
