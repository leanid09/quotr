---
type: question
id: Q-52
question: 'Real publish dates: when did these 6 blog posts first go live? Their blog-sitemap dates were reset to 2026-07-15 or 2026-07-24. What happened on those days (a rebuild or a move)? Is an edit history kept (in the content system or the code), so real publish and last-changed dates can be restored?'
topic: H. Domains, profiles and technical setup
ask: Quotr
status: open
answer:
answered_on:
---
# Q-52 · Real publish dates of six posts

> [!question] Question for Quotr
> **Real publish dates:** when did these 6 blog posts first go live? Their blog-sitemap dates were reset to 2026-07-15 or 2026-07-24. What happened on those days (a rebuild or a move)? Is an edit history kept (in the content system or the code), so real publish and last-changed dates can be restored?

| Post | Date in the blog sitemap | What we know |
|---|---|---|
| [[BP-66 ai construction estimating software that turns plans into prices in minutes\|BP-66]] | 2026-07-15 | AI explainer: software that turns plans into prices |
| [[BP-70 construction costs surged 12 6 in 2026 how ai estimation helps\|BP-70]] | 2026-07-24 | Cost post. Its URL has a 12.6% figure we could not trace ([[Q-58 Sources for statistics in posts\|Q-58]]) |
| [[BP-71 how ai construction takeoff works in 2026\|BP-71]] | 2026-07-24 | AI explainer: how AI takeoff works |
| [[BP-72 how rl electric cut estimating time with ai powered takeoffs\|BP-72]] | 2026-07-24 | RL Electric customer story. The same story is on /case-studies/rl-electric/ |
| [[BP-73 ibs 2026 from the magic of orlando to the reality of ai implementation\|BP-73]] | 2026-07-24 | IBS 2026 recap. The show was reportedly in February 2026, so July is unlikely to be the real date (from the publishing research; not re-checked) |
| [[BP-75 the architects survival guide unlocking new revenue streams in pre construction\|BP-75]] | 2026-07-24 | Guide for architects. Quotr's only post for architects |

Two more posts share these dates but are counted as real dates in our data: [[BP-65 ai agent for construction|BP-65]] (2026-07-15) and [[BP-74 metric imperial construction takeoff|BP-74]] (2026-07-24). [[Optimize vs create]] marks BP-74 as a bulk date too. They may also have been reset (inference), so please confirm these two as well.

**Why we ask:** wrong dates distort the timing statistics and hide which Google updates each post has lived through. See [[Blog health audit]] and [[What went wrong#W-16 Date signals disagree, and years in evergreen URLs|W-16]].

- **Timing statistics.** These 6 posts had to be left out. July shows 23 posts in the sitemap but only 17 with real dates ([[Publishing patterns and correlations]]).
- **Google updates.** A post's age decides which updates it has faced ([[Google search updates 2025-2026]]).
- **Dates disagree.** The sitemap date, the "Last updated" line on the page and the schema date (code that describes the page to machines) do not always match. Task [[A9 Sitemaps and lastmod dates|A9]] ties them to one real date.
- **Timing (inference).** Do not change dates on the live site until the September spam update ends, about 2026-10-08 (RANK-21).

## Answer

*When Quotr answers: put the short answer in the `answer` property, fill `answered_on`, set `status` to `answered`, correct the `published` date in each article note, and add a line to [[Changelog]].*

---

From [[Blog health audit]] · H. Domains, profiles and technical setup
