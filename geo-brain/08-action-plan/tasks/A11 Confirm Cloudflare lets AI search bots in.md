---
type: task
id: A11
task: Confirm Cloudflare lets AI search bots in; do not opt out of Google's AI features
phase: Days 1–30 (Oct 2026)
month: 2026-10
week: 1
rank: 11
owner: Dev
effort: S
impact: M
depends_on_text: Cloudflare access
status: todo
done_when: the Cloudflare or server-log check shows 200 responses for the bots above on key pages, with none blocked or challenged; the Search Console opt-out setting is confirmed off.
---
# A11. Confirm Cloudflare lets AI search bots in (and do not opt out of Google's AI features)

- **What:** In Cloudflare, check that AI search crawlers get normal pages: OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot, Bingbot and Googlebot. Confirm "AI Labyrinth" (Cloudflare's trap for badly behaved bots) was switched on deliberately, and that any "Block AI bots" setting is off. In Search Console, do **not** use Google's new opt-out from AI features.
- **Why (evidence):** Every page carries a hidden AI Labyrinth link, and the research could not see from outside whether Cloudflare also blocks the AI bots Quotr wants (report; verification file, claim 16). Quotr needs AI visibility, so opting out of Google's AI Overviews and AI Mode would work against it (report).
- **Owner:** Dev (whoever owns Cloudflare).
- **Effort / Impact:** S (1–2 hours, then 15 minutes a month) / M (a precondition; high if something turns out to be blocked).
- **Depends on:** Cloudflare access.
- **Done when:** the Cloudflare or server-log check shows 200 responses for the bots above on key pages, with none blocked or challenged; the Search Console opt-out setting is confirmed off.
- **How-to:** [[Tracking setup]] §5 and §3.3; [[How AI engines choose sources]] §2.

---

Part of [[30-60-90 plan#Days 1–30 (about October 2026): quick wins and clean-up|30-60-90 plan › Days 1–30]]
