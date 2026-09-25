---
type: playbook
description: 'The YouTube and video strategy: channel fixes, series, creators, podcasts and measurement.'
last_verified: 2026-09-25
verify_every_days: 180
---
# YouTube and Video Playbook

> [!abstract] What this page is for
> The video strategy for Quotr.ai: why video matters for AI visibility, how to fix and run the YouTube channel, which series to make, how to work with creators, podcasts and webinars, and how to measure it. (For the brief used for each single video, see [[YouTube video brief template]].)

> [!info]- Sources
> [[geo_content_playbook_b2b]] (§1 video, §3 YouTube mentions, §7), [[geo_ai_citation_signals_2026]] (§2, §4 YouTube), [[verification_geo_evidence]] (claims #13, #18; H7; M10), [[quotr_offsite_presence]] (§3 YouTube, podcasts), [[competitor_geo_benchmark]] (§2 Togal and Beam AI video and event programmes), [[quotr_onsite_content_audit]] (§2 tutorials); [[Entity fact sheet]] (§2b social profiles); FTC [Endorsement Guides Q&A](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking) (checked via WebSearch, 2026-09-25).

---

## 1. Why video (with the right caveats)

| Finding | Source | Caveat |
|---|---|---|
| YouTube mentions (titles, transcripts, descriptions) were the **strongest correlate** of brand visibility in ChatGPT, AI Mode and AI Overviews (~0.737), ahead of branded web mentions (0.66–0.71) and far ahead of backlinks | Ahrefs, 75K brands (Dec 2025; press release May 26, 2026); `verification_geo_evidence.md` claim #13 | Correlation, not causation. Big brands have more of everything (H7) |
| YouTube is the most-cited domain in Google AI Overviews (Ahrefs, early 2026); reported at ~23% (Surfer) to ~30% (BrightEdge) of AIO citations | `geo_ai_citation_signals_2026.md` §2, §4; `geo_content_playbook_b2b.md` §1 | Secondary summaries of vendor studies |
| YouTube was the **largest source domain** for SaaS in Aleyda Solis's August 2026 study; social/community/video made up 45.7% of top cited SaaS sources | `verification_geo_evidence.md` claim #18 | Cross-vertical sample of 15 brands |
| Video was ~1% of cited sources in ChatGPT vs ~23% in Google AI Mode (SaaS subverticals) | `geo_content_playbook_b2b.md` §1 (Aleyda Solis) | Not re-checked in the verification pass |
| In Quotr's own Perplexity tests, YouTube was **never** cited in any of the 45 runs | [[Citation sources map]]; `quotr_ai_visibility_tests.md` §5 | Only Perplexity was tested; ChatGPT and Google's AI features were not |
| Vendor trackers (July–Sept 2026) see citations shifting toward YouTube, LinkedIn and Reddit | `verification_geo_evidence.md` M10 | Vendor data |

**Read-out:** video is most likely to pay off in **Google AI Overviews and AI Mode**, and as a brand-mention signal across engines. It also sells: contractors want to see AI takeoff work on real drawings before they trust it.

---

## 2. Where Quotr's video stands today

| Asset | Status | Source |
|---|---|---|
| [youtube.com/@QuotrAI](https://www.youtube.com/@QuotrAI) (title "QuotrAI") | Current channel; in the site footer and Organization schema | Fact sheet §2b |
| youtube.com/@QuotrIO | Listed on /disambiguation/; resolves to a channel titled "QuoTrio" (handle @QuoTrio, ID UCsiomlzNKGWU25LOrTsZI4Q). Whether Quotr owns it is **TO CONFIRM** | Offsite notes §3 |
| [AI Construction Estimating Software Demo (Quotr.ai)](https://www.youtube.com/watch?v=I0dsjz7Y_kc) | Product demo | Offsite notes §3 |
| [RL Electric's Quotr Journey](https://www.youtube.com/watch?v=Y2_PUPVtVaE) | Customer story (no numbers on the case-study page) | Offsite notes §3; onsite audit §3 |
| [How To Use Quotr Estimate — Revit Extension](https://www.youtube.com/watch?v=zNIXcvCbWAg) | Legacy Revit product; feeds old "Revit for architects" descriptions | Offsite notes §4 |
| ["Funded, Now What?!" Ep. 45 with Quotr.io](https://www.youtube.com/watch?v=CMGyqn5VI9I) | Podcast video; uses the old name | Offsite notes §3 |
| /tutorials/ | 5 video tutorials (Takeoff Editor Overview, How to Manage Your Database, How to Export a Proposal, How to Manage Bids, Quotr.ai Software Demo) + 1 text guide | Onsite audit §2 |
| Subscribers, views, upload cadence | Not retrievable | Offsite notes §3 Gaps |

**What competitors do:** Togal runs 2026 webinars on YouTube, trade-specific sessions (e.g., a flooring takeoff webinar that surfaced in search for a flooring-takeoff question; prompt library L-059), weekly "#TogalTuesdays" sessions and podcast guest spots; Beam AI demoed "instant AI HVAC takeoffs" at AHR Expo 2026 with a syndicated press release (competitor benchmark §2).

---

## 3. Channel clean-up (first 2 weeks)

1. **One channel:** publish only on @QuotrAI. Confirm whether @QuoTrio/@QuotrIO is Quotr's; if yes, point it to @QuotrAI and stop using it; update /disambiguation/ and schema `sameAs` to @QuotrAI only.
2. **Channel name and About text:** "Quotr.ai" with the one-line category sentence from the fact sheet; link to quotr.ai.
3. **Legacy videos:** add a pinned comment and description line to the Revit video ("This shows our earlier Revit extension. Quotr.ai today is AI takeoff, estimating and bid software: [link]"), or unlist it if Quotr no longer sells the add-in (**TO CONFIRM**).
4. **Existing tutorials:** add chapters, corrected captions, a first description line that answers "what this shows", and links; embed each on /tutorials/ with VideoObject schema.
5. **Playlists:** "Trade takeoffs", "Customer stories", "Factory-direct materials", "Product how-tos", "AI takeoff: honest tests".

---

## 4. Content pillars and cadence

**Cadence (recommendation for a small team):** 2 long videos a month (4–10 minutes) + 4 Shorts cut from them. Consistency beats volume.

| Pillar | Example videos | Prompts served |
|---|---|---|
| **Trade takeoffs on real plans** | Drywall, flooring, roofing, electrical symbol counts, window and door schedules | L-047, L-051, L-059, L-074, L-081, L-094 |
| **Honest AI tests** | "How accurate is AI takeoff on a scanned plan? We checked every count" | L-035, L-039, L-041 |
| **Customer stories (numbers-first)** | RL Electric remake; a procurement project walk-through (Myren Dr, Saratoga) | D-017, D-048 |
| **Factory-direct explained** | DDP vs FOB; landed cost; quality checks; lead times | L-110–L-112, L-118, L-120, L-121 |
| **Data explainers** | Quarterly materials price index in 3 minutes | L-113, L-114 |
| **Fair comparisons** | "Manual vs AI takeoff on the same plan set"; honest tool comparisons with dated prices | D-021, E-059 |
| **Founder talks** | Architect's view of estimating; engineering view of AI accuracy | Brand + trust |

Each video follows the brief in [[YouTube video brief template]]: answer in the first 15 seconds, "Quotr.ai" said aloud, chapters (first at 00:00, 3+ chapters, 10+ seconds each), corrected captions, facts from the fact sheet.

---

## 5. Beyond the own channel: creators, podcasts, webinars, events

Brand mentions on **other** channels count too (the Ahrefs correlation is about mentions anywhere on YouTube).

| Route | How | Notes |
|---|---|---|
| **Construction and estimating creators** | Offer a real plan set, a login and a founder interview; let them test and say what they think | Research relevant channels first (estimating educators, trade YouTubers); no scripted praise |
| **Paid creator content** | Only with clear disclosure: FTC Endorsement Guides require disclosing material connections (payment, free product); creators should also use YouTube's paid-promotion disclosure setting | See [[Review generation]] §6a |
| **Podcasts with video** | Pitch founders to construction-tech and precon podcasts (e.g., The Preconstruction Podcast, where Togal's team has appeared; AEC Tech Journeys, where Perplexity cites an episode that appears to feature Quotr, not yet opened: **TO CONFIRM with Quotr**) | Ask hosts to write "Quotr.ai" and link quotr.ai in show notes (the MPN episode notes still say "Quotr.io" and link quotr.io) |
| **Webinars** | Monthly or quarterly: "AI takeoff on your own plans, live"; "Tariffs and landed cost Q&A" | Record, chapter and publish on YouTube; Quotr has run an "Ask your plans AI agent" webinar before |
| **Events** | Record short demos at trade shows (Quotr attended IBS 2026, Dallas Build Expo 2026, PCBC 2026 and others) | Publish within a week with the event name in the title |

---

## 6. Repurposing (one video → many assets)

- Embed on the matching quotr.ai page (how-to, trade page, case study) with a text summary or transcript and VideoObject schema.
- Cut 2–4 Shorts (under 60 seconds) with one clear point each.
- Founder LinkedIn post with a native clip ([[LinkedIn thought leadership]]).
- Quote the key line in the newsletter.
- Answer a relevant Reddit or forum question with the insight, and link only if allowed ([[Reddit and community]]).

---

## 7. Rules

1. Facts match [[Entity fact sheet]]; current prices only; no unconfirmed claims.
2. Customer and data permissions in writing before filming or showing plans.
3. Show at least one honest limitation per product video.
4. Disclose every paid or gifted creator relationship.
5. No fake engagement (bought views, comments or subscribers).
6. Name consistency: "Quotr.ai" in the channel name, titles and descriptions; never "Quotr.io" except "formerly Quotr.io" where history matters.

---

## 8. How to measure

| Metric | Source | Cadence |
|---|---|---|
| Videos published vs plan | Log | Monthly |
| Views, watch time, subscribers | YouTube Studio | Monthly |
| Videos that mention "Quotr.ai" on **other** channels and podcasts | Search + log | Monthly |
| YouTube URLs appearing in AI Overviews/AI Mode citations for tracked prompts | Prompt tracking ([[Tracking set]]) | Monthly |
| Generative-AI impressions for pages with embedded videos | Google Search Console generative AI report (see [[Tracking setup]]) | Monthly |
| Referral sessions from youtube.com | GA4 | Monthly |
| "How did you hear about us?" = YouTube | Demo/trial form | Monthly |

---

## Related pages

- [[YouTube video brief template]] — the brief for each video
- [[Case study template]] and [[Trade how-to guide template]] — pages the videos pair with
- [[Schema markup kit]] — VideoObject markup
- [[LinkedIn thought leadership]] — repurposing clips on LinkedIn
- [[Togal AI]] — a competitor's video programme
- [[Off-site earned media plan]] — where video fits the plan
