# Quotr Content OS (v2)

The operating system for producing 3 original Quotr.ai articles per business day, built on the GEO brain in `../geo-brain/`.

| File | What it is |
|---|---|
| `Quotr_Intelligence_OS_v2.xlsx` | The workbook: 29 tabs, 195 fully specified articles over 13 weeks (Nov 16, 2026 – Feb 12, 2027), briefs, claims, schema, adaptations, scorecard |
| `articles/` | First three full drafts (ART-001–003) with JSON-LD and channel adaptations. Drafts, not publish-ready: see each file's gates |
| `build/` | Python that regenerates the workbook from the v1 upload. Edit the data files and rebuild instead of hand-editing 195 rows |

## How the machine runs

1. **Settings**: start date, lane mix (4 competitor · 7 industry · 2 regional · 1 research · 1 benchmark per week), hours per article.
2. **Context Pack**: the only facts writers and AI tools may use. The AI-briefing cell at the bottom is pasted into ChatGPT/Claude before drafting.
3. **Article Pipeline**: one row per article. Title, buyer query, tracked prompts (T#), persona, format, Quotr-only angle, slug, meta, schema, author, gate, priority.
4. **Article Briefs**: outline, FAQ, required claims, must-not-say, internal links, CTA, and auto-built BlogPosting + BreadcrumbList JSON-LD (col. S).
5. **Production SOP**: T-10 → T+90 timeline, 15 publish gates, AI prompt chain (P1–P8), roles, swap rules, capacity model.
6. **Placement Log / Adaptation Kit**: weeks 1–4 pre-planned to the base distribution plan, with UTM = article ID.
7. **Claim Ledger / AI Prompt Bank / Refresh Queue**: 67 sourced claims (16 TO CONFIRM, 8 never-use), the real 53-prompt tracking set with Sept 2026 baselines, 24 existing URLs to refresh.

## Rebuild

```bash
python3 content-os/build/build.py content-os/build/input/Quotr_Intelligence_OS_v1.xlsx content-os/Quotr_Intelligence_OS_v2.xlsx
```

Then open in Excel (or recalculate with LibreOffice) so formula values are cached.

## Known limits

- 75 of 195 articles are gated on Quotr inputs (fact-sheet sign-off, procurement/service data, customer permission, expert review, benchmark tests). The scheduler places them no earlier than the gate allows; swap rules handle slips.
- Competitor prices and tariff facts are dated; re-verify in the week of publishing.
- Hours per article (4.75) are assumptions; calibrate after week 2. At those hours the revised scope is about $12/production hour against the $3,500/month fee (Economics rows 28–38).
