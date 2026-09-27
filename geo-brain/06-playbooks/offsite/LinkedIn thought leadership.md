---
type: playbook
description: 'Founder-led LinkedIn: profile fixes, topics, formats, cadence and templates.'
last_verified: 2026-09-25
verify_every_days: 180
---
# LinkedIn Thought Leadership Playbook (Founder-Led)

> [!abstract] What this page is for
> How Quotr.ai's founders (Hanyang Liu and Junzhe Shi, PhD) and team use LinkedIn to publish practical expertise that construction buyers read and AI engines cite, including profile fixes, topics, formats, cadence, templates and rules.

> [!info]- Sources
> [[geo_content_playbook_b2b]] (§3 LinkedIn founder-led content; §3 inferences), [[verification_geo_evidence]] (claims #16, #18; section D "not re-checked"; M10), [[quotr_offsite_presence]] (§3 LinkedIn and founder thought leadership; §4 entity signals; §5 AI summary errors), [[geo_ai_citation_signals_2026]] (§2 domain concentration); [[Entity fact sheet]] (§1a founders, §2b social profiles); [[Citation sources map]] (§4 target 20); FTC [Endorsement Guides Q&A](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking) (checked via WebSearch, 2026-09-25).

---

## 1. Why LinkedIn, and why founder-led

- **LinkedIn is heavily cited for professional topics.** A Semrush study (325,000 prompts, Jan–Feb 2026; 89K LinkedIn URLs cited by ChatGPT Search, AI Mode and Perplexity) reported that LinkedIn appeared in 11% of AI responses, ranked #2 overall and #1 for professional topics (`geo_content_playbook_b2b.md` §3). **This study was not re-checked in the verification pass**, so quote it as "reported by Semrush".
- **What gets cited, in that study:**
  - LinkedIn **articles** were 50–66% of cited LinkedIn content; feed posts 15–28%.
  - The median cited post had only 15–25 reactions and at most 1 comment: **relevance beats popularity**.
  - 54–64% of cited posts shared knowledge or practical advice.
  - ChatGPT Search and AI Mode more often cited **individual creators** (59%); Perplexity more often cited **Company Pages** (59%).
- **LinkedIn ranks third** among cited domains in Peec AI's 30M-source analysis (after Reddit and YouTube), and vendor trackers in mid-2026 saw citations shifting further toward YouTube, LinkedIn and Reddit (`verification_geo_evidence.md` claim #16, M10).
- **Perplexity already cites Quotr's LinkedIn company page** (linkedin.com/company/quotrai) on brand prompts (offsite notes §5).
- **Founders have real credibility that is not yet used:** Hanyang Liu trained as an architect; Junzhe Shi holds a UC Berkeley PhD and built algorithms at Apple and UC Berkeley. The offsite notes found no Quotr-specific public thought leadership from Junzhe Shi and only one Substack article by Hanyang Liu ([AI AEC Digest](https://aiaecdigest.substack.com/p/stop-listening-watch-what-customers-do)) (offsite notes §3).

---

## 2. Fix the profiles first (week 1)

LinkedIn profiles are entity signals that AI tools read. Today they carry errors that leak into AI answers.

| Profile | Problem found | Fix |
|---|---|---|
| Company page [linkedin.com/company/quotrai](https://www.linkedin.com/company/quotrai) ("Quotr.ai"; about 1,077 followers per Perplexity, unverified) | A search summary still describes Quotr as "an AI assistant providing real-time cost estimation and Revit integration to help architects" (legacy positioning) | Rewrite **About** with the canonical sentence: "Quotr.ai (formerly Quotr.io) is AI construction takeoff, estimating and bid software, with a done-for-you estimating service and factory-direct material procurement." Website = https://quotr.ai. Add specialties (AI takeoff, construction estimating, bid management, construction procurement). HQ/location **TO CONFIRM** |
| linkedin.com/company/quotrio | Listed on /disambiguation/ as a "verified" profile | If it is Quotr's, merge or retire it and point to /quotrai; remove it from /disambiguation/ and schema |
| linkedin.com/company/flozdesign | Cited by Perplexity; link to Quotr **TO CONFIRM** | Decide: rename to show "FLOZ Inc. — maker of Quotr.ai", or retire |
| Hanyang Liu: two profiles ([hanyang-liu1](https://www.linkedin.com/in/hanyang-liu1/), [hanyang-liu-0a8145b3](https://www.linkedin.com/in/hanyang-liu-0a8145b3/)) | Splits authority; a search summary merged another startup's news ("$4.2M seed led by Initialized Capital… zerank-1") into a summary about him | Keep one profile (hanyang-liu1 is used in the fact sheet) and close or merge the other following LinkedIn's help process; headline "Co-founder & CEO, Quotr.ai — AI takeoff and estimating"; About states his architecture background; Featured section links to Quotr.ai articles |
| Junzhe Shi ([junzhe-shi](https://www.linkedin.com/in/junzhe-shi/), "Junzhe Shi - Quotr") | Minimal Quotr-specific content | Headline "Co-founder & CTO, Quotr.ai — AI for construction drawings"; About mentions UC Berkeley PhD and Apple algorithms work; Featured links |
| Team members (e.g., Tianyi Zong, COO; Jati Ibloguen, Growth: titles **TO CONFIRM**) | — | Current employer "Quotr.ai", consistent spelling |

---

## 3. What to write about (topic map)

Pick topics where each founder has real, first-hand knowledge. Each topic should map to buyer prompts in the [[Prompt library|prompt library]].

| Founder | Topic pillar | Example article titles | Prompts |
|---|---|---|---|
| **Hanyang Liu (CEO, architect)** | Design meets cost: why estimates derail projects | "Why good designs die at the first cost estimate (and how to stop it)" | L-136, L-144 |
| | Factory-direct materials, honestly | "Factory-direct finishes: when they save money, and when they don't" | L-084, L-120 |
| | Tariffs and landed cost for builders | "What 2026 tariffs mean for a Bay Area kitchen, line by line" | L-113, L-114, L-087 |
| **Junzhe Shi, PhD (CTO)** | How AI reads drawings | "How AI takeoff actually counts symbols (and where it fails)" | L-036, L-038 |
| | Accuracy, measured | "We tested AI takeoff on scanned plans. Here's what broke." | L-035, L-039, L-041 |
| | Scope gaps and data quality | "Scope gaps cost more than pricing errors" (existing blog post, adapted) | L-011, L-026 |
| **Both / team** | Customer stories with numbers | "From 20-hour takeoffs to 1–2 hours: what changed at RL Electric" (with permission) | D-017 |
| | Original data releases | "Q4 materials price index: 3 findings" | L-113, L-124 |

**Rule of thumb from the Semrush study:** practical, knowledge-sharing content is what gets cited. Avoid pure announcements, hiring posts and generic motivation.

---

## 4. Formats and cadence (recommendation)

| Format | Why | Cadence (per founder) |
|---|---|---|
| **LinkedIn article** (long-form, 800–1,500 words) | Articles were the majority of cited LinkedIn content in the Semrush study | 1–2 a month |
| **Newsletter** (LinkedIn's newsletter feature, collecting the articles) | Subscribers get notified; builds a series | Monthly issue = the article |
| **Feed post** (150–300 words, one idea, one number) | Reach and discussion; can be cited when it shares advice | 2–3 a week |
| **Native video clip** (30–90 seconds, from YouTube videos) | Reuses video work | 2 a month |
| **Document/carousel post** (a checklist or table) | Easy to save and share | 1 a month |
| **Company page post** | Perplexity cited Company Pages more often in the Semrush study | Reshare every founder article with a one-line summary |

Syndication: republish (or adapt) key data posts and guides from quotr.ai as founder articles, with a link back to the original (Handoff syndicates its listicle to LinkedIn Pulse; citation map target 20).

---

## 5. Templates

### 5a. Article outline

```
Title: [A specific claim or question estimators care about, with a number if possible]

1. The answer in 2–3 sentences (what you learned / what to do).
2. Why it matters (a cost, time or risk number, with its source).
3. What we saw (first-hand: a real plan set, a job, a dataset — with permission).
   - Table or 3–5 bullets with numbers.
4. What still goes wrong / limits (honest).
5. A practical checklist readers can use tomorrow (5–7 points).
6. One line on Quotr.ai with disclosure:
   "I co-founded Quotr.ai, which [does X]. [Link] — but the checklist above works with any tool."
7. Sources.
```

### 5b. Feed post

```
[Hook: one surprising, specific fact from real work.]

[2–4 short lines of explanation.]

[One number, with where it came from.]

[A question to the reader.]

(I'm co-founder of Quotr.ai; this came from [our data / a customer job, shared with permission].)
```

**Example (draft; numbers must be approved):**
> On one Saratoga build, the materials order came in at $97K through factory-direct sourcing, against a $187K–$218K Bay Area market price (as Quotr reports it on our procurement page).
> The catch: [lead time / what the builder had to plan for].
> When would you trade lead time for that kind of saving?
> (I co-founded Quotr.ai, which runs this sourcing programme.)

---

## 6. Rules

1. **Facts match the fact sheet.** Current prices; no unconfirmed numbers (funding amount, factory count, savings %, accuracy %, HQ, founding year) until Quotr confirms them.
2. **Disclose the connection** when recommending Quotr.ai. The founders' profiles show their role, but add an explicit line when a post promotes Quotr. The FTC's Endorsement Guides say employees should disclose their employment when endorsing their employer's products on social media ([FTC](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking)). This applies to every team member who posts about Quotr.
3. **Customer data only with permission.**
4. **Name consistency:** "Quotr.ai" (not Quotr.io, not QUOTR) in headlines, About sections and articles.
5. **No engagement pods, bought followers or automated comment bots.**
6. **Human-written.** AI can help draft; a founder edits and approves every piece in their own voice.

---

## 7. How to measure

| Metric | Source | Cadence |
|---|---|---|
| Articles and posts published per founder | Log | Monthly |
| Followers (company page and founders); newsletter subscribers | LinkedIn analytics | Monthly |
| LinkedIn URLs (Quotr founders or company) cited in AI answers for tracked prompts | Prompt tracking ([[Tracking set]]) | Monthly |
| Referral sessions from linkedin.com | GA4 | Monthly |
| Inbound: DMs, demo requests mentioning a post; "How did you hear about us?" = LinkedIn | CRM / form | Monthly |
| AI answers to "Who founded Quotr.ai?" (D-004) accurate and free of the Initialized/zerank-1 conflation | Prompt tracking | Quarterly |

---

## Related pages

- [[Wikidata and knowledge graph]] — keeping LinkedIn consistent with other profiles
- [[YouTube and video]] — video clips for LinkedIn
- [[Listicle and PR outreach]] — turning articles into bylines and pitches
- [[Original research report template]] — data to publish as articles
- [[GEO writing style guide]] — writing and naming rules
- [[Entity fact sheet]] — founder bios and profile URLs
