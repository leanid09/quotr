# Content formats, article structures and topic prioritization for AI search and SEO: September 2026 update for Quotr.ai

*Method note (read first).* Status date: 2026-09-25. These notes add only what is **new, missing or contradicting** relative to the earlier evidence base:
- `geo_ai_citation_signals_2026.md` ("signals")
- `geo_content_playbook_b2b.md` ("playbook")
- `verification_geo_evidence.md` (mostly PENDING; it confirms only Google's May 15, 2026 AI-optimization guide)
- For Quotr-specific observations: `quotr_ai_visibility_tests.md` ("tests"; Perplexity runs of 2026-09-25)

**Tool limits.** 31 WebSearch calls were made. WebFetch was refused (EGRESS_BLOCKED) on every domain tried: seroundtable.com, x.com, anicca.co.uk, stackedmarketer.com, techcrunch.com, searchengineland.com, blogs.bing.com and arxiv.org. As instructed, no workaround was attempted. **No page was read in full.** Every finding comes from search-engine summaries of the linked URL. Treat numbers as "reported by X" and open the source before quoting a figure externally.

**Labels.**
- **[Observed]**: stated in the linked source (via search summary).
- **[Inference]**: my own reasoning.

**Source types.**
- *First-party*: Google, Microsoft, OpenAI.
- *Regulator*.
- *Academic preprint*: arXiv or SSRN, not peer-reviewed.
- *Vendor*: a company selling SEO, AI-visibility, analytics or PR tools or services. Agencies are included.
- *Trade press / secondary*.
- *Practitioner opinion*.

---

## 1. What changed in AI search between June and September 2026 that affects content strategy

### Takeaway
Summer 2026 brought five content-relevant shifts:
1. **Google made AI answers longer and more like AI Mode, and started policing manipulation of them.** AI Overviews now auto-expand into AI Mode-style answers. Since May 15, attempts to manipulate AI answers count as spam, and the year's fourth spam update began Sept 24.
2. **Publishers can now opt out of Google's AI features in Search Console.** This followed a UK CMA requirement on June 3. The global rollout was reportedly finished by Aug 31.
3. **Ads and commerce moved into AI answers.**
   - ChatGPT ads now include conversion-optimized bidding and product carousels, and run in 40+ countries.
   - Google is adding agentic checkout and testing conversational ads in AI Mode.
   - OpenAI dropped in-chat checkout in favor of "discover in AI, buy on site".
4. **Chatbot traffic kept fragmenting.** August 2026 shares: ChatGPT 54.2%, Gemini 26.5%, Claude 9.5%, Copilot 1.6%, Perplexity 1.0%.
5. **Measurement improved and new studies downgraded "tricks".** Bing now reports citation share, intents and topics. New studies weaken the case for schema and Q&A formatting as levers, and strengthen the case for maintained, evidence-dense pages, tools and multi-source consensus.

### Cited Findings
*Already established in earlier notes (not repeated):*
- Google's May 15 guide ("still SEO"; no llms.txt, special schema or chunking needed) — signals §1; verification #1
- Preferred Sources in AI Overviews/AI Mode, May 27 — signals §1
- ChatGPT branded-link update, May 7 — signals §4
- GA4 "AI Assistant" channel, May 13 — playbook §4
- Reddit's August 2026 collapse in ChatGPT citations — playbook §3
- Muck Rack May 2026 earned-media study — playbook §3

**Google AI Overviews and AI Mode**
- **[Observed]** In September 2026 Google "started to push AI Mode into AI Overviews". AI Overviews can now expand automatically into a longer, AI Mode-style answer, which removes the manual "Show more" step for some queries. — [SERoundtable Sept 2026 webmaster report](https://www.seroundtable.com/sept-2026-google-webmaster-report-41979.html) (trade press); [Harri Digital](https://www.harridigital.co.uk/blog/google-september-2026-update-ai-overviews-expansion) (agency blog)
- **[Observed]** Other September items:
  - AI Mode shows link carousel cards for developing stories.
  - Google tested AI-generated images in AI Overviews, then paused the test.
  - AI Mode is reported as "partially powered by Gemini 3.7 Flash".
  
  — [SERoundtable Sept 2026 report](https://www.seroundtable.com/sept-2026-google-webmaster-report-41979.html)
- **[Observed]** On July 16, 2026, AI Mode gained the ability to link to and interact with select apps. Only the headline was available. — [TechCrunch](https://techcrunch.com/2026/07/16/googles-ai-mode-now-lets-you-link-and-interact-with-select-apps/)
- **[Observed]** At Google Marketing Live (late May 2026, with rollout continuing through the summer), Google expanded the Universal Commerce Protocol (UCP):
  - checkout inside AI Mode and Gemini via Google Pay, with PayPal to follow;
  - a Universal Cart across retailers;
  - tests of new conversational ad formats in AI Mode.
  
  — [Google blog: GML shopping updates](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/); [Google blog: Universal Cart](https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/); [Search Engine Land](https://searchengineland.com/google-expands-universal-commerce-protocol-and-launches-new-agentic-shopping-tools-478113); [eMarketer](https://www.emarketer.com/content/google-brings-checkout-ai-mode-races-rivals-agentic-commerce) (first-party + trade press)
- **[Observed] Publisher opt-out from AI features** (regulator plus first-party action, reported via secondary sources):
  - March 2026: Google agreed to give publishers an AI Overviews opt-out ([VideoWeek, Mar 19](https://videoweek.com/2026/03/19/google-agrees-to-give-publishers-an-ai-overview-opt-out-but-concerns-remain/)).
  - **June 3, 2026:** the UK CMA issued a Publisher Conduct Requirement. Google launched a Search Console toggle the same day. It stops a site's content being used to ground AI Overviews, AI Mode and AI summaries in Discover, while the site keeps its blue links and standard Discover presence.
  - Google said it would roll the toggle out globally, and summaries report the rollout was **completed Aug 31**.
  
  — [TechCrunch, Jun 3](https://techcrunch.com/2026/06/03/publishers-will-be-able-to-opt-out-of-ai-search-thanks-to-new-regulation/); [ALM Corp](https://almcorp.com/blog/google-ai-overviews-publisher-opt-out-controls-2026/); [Hazem Khattab](https://hazemkhattab.com/google-ai-overviews-opt-out-search-console/); [MediaPost](https://www.mediapost.com/publications/article/416681/google-gives-publishers-opt-out-for-ai.html). Digiday frames it as an opt-out publishers "can't safely use" because it costs visibility — [Digiday](https://digiday.com/media/googles-ai-opt-out-leaves-publishers-with-a-choice-they-cant-safely-use/). *The "global, completed Aug 31" detail was not verified against Google.*
- **[Observed] Spam policy extended to AI answers (May 15, 2026; in force throughout the window).** Google's spam definition now includes "attempting to manipulate generative AI responses in Google Search". Enforcement (demotion or removal) runs on the same track as ranking spam. Coverage lists these as in scope:
  - "recommendation poisoning, biased ranking listicles, or prompt-injection tactics";
  - "inauthentic mentions and scaled content abuse".
  
  *That list is commentators' framing; it was not verified as Google's own wording.* — [Search Engine Land](https://searchengineland.com/google-updates-search-spam-policies-to-clarify-it-applies-to-generative-ai-responses-477657); [PPC Land](https://ppc.land/google-spam-policies-now-officially-cover-ai-overviews-and-ai-mode-in-search/); [Gizmodo](https://gizmodo.com/googles-spam-policies-now-apply-to-attempts-to-manipulate-ai-2000759393); [WinBuzzer](https://winbuzzer.com/2026/05/17/google-search-spam-policy-ai-overviews-ai-mode-manipulation-xcxwbn/)
- **[Observed]** The **September 2026 spam update** began rolling out on **Sept 24, 2026**. It is the fourth spam update of 2026, and Google said it could take up to two weeks. — [Coalition Technologies](https://coalitiontechnologies.com/blog/google-september-2026-spam-update); [TechJuice](https://www.techjuice.pk/google-september-spam-update-2026-rollout/); [SERoundtable](https://www.seroundtable.com/sept-2026-google-webmaster-report-41979.html)
- **[Observed]** Recent core updates:
  - The most recent confirmed core update found is **May 2026**, completed in under 12 days.
  - An unconfirmed update in January 2026 hit "commodity content", including self-serving listicles.
  - No June–September 2026 core update surfaced in these searches. That is not proof there was none.
  
  — [SERoundtable](https://www.seroundtable.com/google-may-2026-core-update-done-41435.html); [Search Engine Land](https://searchengineland.com/google-may-2026-core-update-rollout-is-now-complete-479119); [Glenn Gabe / GSQI](https://www.gsqi.com/marketing-blog/core-roars-back-google-may-2026-core-update-analysis/)
- **[Observed, ambiguous]** A newsletter headline says "over 25% of AI Overviews now include external links, up from almost none". Neither the measure (probably in-text links rather than the source panel) nor the underlying study is known. — [Stacked Marketer](https://www.stackedmarketer.com/news/40-less-search-traffic-a-slow-burn-spam-update-and-ai-overviews-that-link-out/)

**ChatGPT / OpenAI**
- **[Observed] ChatGPT Ads update, Aug 7, 2026** (reported by agency and trade-press sources; not verified against OpenAI):
  - conversion-optimized CPC (oCPC) in beta for product-feed campaigns;
  - dynamic URL parameters, new measurement integrations and budget pacing;
  - a test of multi-product carousel ads at the bottom of conversations;
  - ads live in **40+ countries** through OpenAI's Ads Solutions team and partners;
  - self-serve Ads Manager in nine markets (US, UK, CA, AU, NZ, JP, KR, BR, MX), with 31 European countries "coming soon".
  
  — [ALM Corp](https://almcorp.com/news/chatgpt-ads-conversion-bidding-carousel-ads-august-2026/); [SERoundtable](https://www.seroundtable.com/openai-chatgpt-ads-updates-42017.html); [Choice OMG](https://choice.marketing/blog/chatgpt-ads-2026-field-guide/); [WriteNexa](https://www.writenexa.com/blog/chatgpt-ads-adds-product-carousels-as-openai-pushes-into-shopping-search/). *Conflict:* the unverified claim in the signals note that ads reached the EU "from Aug 23" is not supported by this August summary, which still lists Europe as "coming soon".
- **[Observed, low reliability]** A claim that "ChatGPT ads hit 51% of US replies" — [tech-insider.org](https://tech-insider.org/chatgpt-ads-rollout-2026/). The signals note already rated this site low-reliability. Do not use.
- **[Observed] OpenAI retired Instant Checkout in March 2026**, about six months after launch.
  - It repositioned ChatGPT shopping toward product research, with checkout moving back to merchants' own sites.
  - One summary reports that Walmart measured in-ChatGPT checkout converting about 3× worse than a click-through to Walmart.
  
  — [CNBC, Mar 24, 2026](https://www.cnbc.com/2026/03/24/openai-revamps-shopping-experience-in-chatgpt-after-instant-checkout.html); [Exploding Topics](https://explodingtopics.com/blog/agentic-commerce-protocol); [Digital Applied](https://www.digitalapplied.com/blog/ai-agentic-commerce-discover-in-ai-buy-on-site-2026)
- **[Observed] Citation frequency (seoClarity, vendor).** From March 2026 ChatGPT sharply reduced how often it cites external sources, then rebounded toward pre-March levels by May 2026. When it does cite, it cites fewer sources. — [seoClarity](https://www.seoclarity.net/chatgpt-citation-decline-analysis)
- **[Observed]** SERoundtable reported "OpenAI Makes ChatGPT Sources Less Visible" in late summer 2026. The details could not be read. — [SERoundtable](https://www.seroundtable.com/openai-chatgpt-sources-less-visible-41864.html)

**Traffic share: Gemini and Claude up, Perplexity and Copilot small**
- **[Observed]** Similarweb (vendor panel data) share of generative-AI *website* traffic. This measures visits to the chatbot sites, not app use or referrals.

  | Platform | Aug 2025 | Feb 2026 | Aug 2026 |
  |---|---|---|---|
  | ChatGPT | 73.3% | 56.7% | **54.2%** |
  | Gemini | 12.9% | 25.4% | **26.5%** |
  | Claude | 1.9% | 6.0% | **9.5%** |
  | DeepSeek | 4.0% | 3.4% | 3.4% |
  | Grok | 2.6% | 3.7% | 2.5% |
  | Copilot | 2.0% | ~1.x% (truncated) | 1.6% |
  | Perplexity | 2.0% | n/a | 1.0% |

  — [Similarweb on X (Aug 2026 update)](https://x.com/Similarweb/status/2096878021378466096) (the X post itself was blocked; the August 2026 figures come from the search summary); [Momentic](https://momenticmarketing.com/blog/top-ai-chatbots)
- **[Observed]** The Decoder reported ChatGPT "claws back web traffic share to 55.5 percent as Gemini's brief comeback fades" (month not captured). This suggests month-to-month noise of 1–2 points. — [The Decoder](https://the-decoder.com/chatgpt-claws-back-web-traffic-share-to-55-5-percent-as-geminis-brief-comeback-fades/)

**Microsoft Copilot / Bing**
- **[Observed] Bing Webmaster Tools AI Performance report, June 16, 2026 update** (first-party, via summaries):
  - Four features added in preview globally: **Intents, Topics, Citation Share and Compare**.
  - These sit on top of the February 2026 metrics: Total Citations, Average Cited Pages, Grounding Queries and page-level citation activity.
  - Microsoft describes Citation Share as "observational", "not a ranking system or a competitive scoreboard". It does not expose competitor domains.
  - Coverage is Copilot, Bing and select partners. It does not include ChatGPT, Perplexity or AI Overviews.
  
  — [Bing blog](https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/); [Digital Applied](https://www.digitalapplied.com/blog/bing-webmaster-tools-ai-citation-share-2026-geo-guide); [OtterlyAI](https://otterly.ai/blog/bing-webmaster-tools-ai-performance-report/)

**Perplexity**
- **[Observed]** Perplexity's share of generative-AI web traffic halved to 1.0% (Aug 2026), from 2.0% a year earlier (Similarweb, above).
- **[Observed]** The Comet Plus publisher revenue pool ($42.5M, paying for human visits, citations and agent actions) dates from 2025, so it is not a new development. — [Digiday](https://digiday.com/media/how-perplexity-new-revenue-model-works-according-to-its-head-of-publisher-partnerships/); [Digital Watch](https://dig.watch/updates/publishers-set-to-earn-from-comet-plus-perplexitys-new-initiative)
- No first-party June–September 2026 change to Perplexity's citation behavior was found.

**Citation share by platform (Reddit, YouTube, LinkedIn, Wikipedia)**
- **[Observed] Wellows (vendor; 5.5M social-media citations, 2026).** Share of social-media citations:
  - Reddit 46.4% and YouTube 31.8% (78.2% combined).
  - In ChatGPT and Perplexity, Reddit leads with 53.6–62.8% of social citations.
  - In Google AI Overviews and AI Mode, more than half of social citations are YouTube.
  - Copilot favors LinkedIn, at 43.8% of its social citations.
  
  — [Wellows](https://wellows.com/blog/social-media-ai-citations-report-2026/)
- **[Observed] 5W "AI Platform Citation Source Index 2026" (PR agency).**
  - Reddit, Wikipedia, YouTube, LinkedIn, Forbes and 10 other sources take about 68% of citations across ChatGPT, Claude, Gemini, Perplexity and AI Overviews.
  - Reddit alone is put at about 40% of "multi-engine aggregate citation frequency".
  
  — [5W](https://www.5wpr.com/new/5w-publishes-the-ai-platform-citation-source-index-2026-the-50-websites-that-control-ai/); [Everything-PR](https://everything-pr.com/ai-platform-citation-source-index-2026). *Conflict:* this does not fit Evertune's finding that even the most-cited domain rarely exceeds about 5% of a platform's citations (signals §2), or the August 2026 fall of Reddit to about 0.5% of ChatGPT citations (playbook §3). The metric looks non-comparable, and its method is unclear.
- **[Observed]** Several agencies claim YouTube has overtaken Reddit as the #1 social source for AI citations (dates and method unclear). This conflicts with Wellows' Reddit-first ranking and probably depends on the engine mix (Google surfaces vs ChatGPT). — [Radyant](https://www.radyant.io/guides/youtube-ai-search-visibility-citation-framework); [PikaSEO](https://pikaseo.com/articles/youtube-overtakes-reddit-ai-citations); see also [OtterlyAI YouTube AI citation study 2026](https://otterly.ai/blog/youtube-ai-citation-study-2026/) (vendor; title only)
- **[Observed]** Semrush Q1 2026 (325K prompts): LinkedIn had a **14.3%** share of ChatGPT Search responses, as restated by [Everything-PR's ChatGPT citation index](https://everything-pr.com/chatgpt-citation-source-index-2026). See also [Semrush LinkedIn study](https://www.semrush.com/blog/linkedin-ai-visibility-study/) (vendor).

**New studies published in or near the window (used in §2–§4)**
- **[Observed]** Six new studies are relevant:
  - arXiv 2607.14035, a critical survey of GEO (July 15, 2026; academic preprint). Used in §3.
  - arXiv 2604.25707, on citation selection vs "citation absorption" (April 2026; academic preprint). Used in §4.
  - Ahrefs schema quasi-experiment (May 11, 2026; vendor). Used in §3.
  - Seer Interactive content recency study (citations from March–June 2026; agency). Used in §3.
  - StudioHawk "Format Leverage" (1.2M AI referral visits, January–July 2026; agency). Used in §2.
  - Search Engine Journal's summary of two AI Overview intent studies (2026). Used in §2.
  
  Links are given in those sections.

### Inferences
- **[Inference]** For Quotr, the biggest change is **enforcement, not features**. Three things have now happened:
  - Google names manipulation of AI answers as spam.
  - The January update hit self-serving listicles.
  - A September spam update is rolling out.
  
  Quotr's library of "best X 2026" and "X alternatives" posts that rank Quotr first is therefore a Google policy risk. It is also a cross-engine visibility risk, because ChatGPT, Perplexity and Copilot draw partly on Google and Bing retrieval (signals §1). Fix these pages before publishing more like them.
- **[Inference]** Longer, auto-expanded AI answers built by query fan-out mean more citation slots per answer but fewer clicks. Content should aim to win specific sub-question passages and brand mentions. The pages that still get clicks (pricing, product, calculators, quote requests) must convert.
- **[Inference]** Gemini (about 27%) and Claude (about 10%) now make up more than a third of chatbot web traffic, so a ChatGPT-only content plan misses a large part of the market. Two practical consequences:
  - Google's surfaces lean on YouTube among social sources, so key assets need video companions.
  - Claude retrieves through Brave ([Profound](https://www.tryprofound.com/blog/what-is-claude-web-search-explained)), so Bing and Brave indexing hygiene should be part of every template's checklist.
- **[Inference]** Quotr should **not** use the new Search Console AI opt-out. It needs AI visibility more than it needs to withhold content.
- **[Inference]** Paid placements now exist for "best takeoff software"-type prompts (ChatGPT ads with oCPC; AI Mode ad tests). Organic content should aim at what ads can't buy: being the cited evidence and the brand named in the answer text. ChatGPT citations are volatile and becoming less visible, so being named in the answer matters more than a footnote link.
- **[Inference]** OpenAI's retreat from in-chat checkout ("discover in AI, buy on site") means Quotr's procurement, pricing and quote-request pages on quotr.ai remain the conversion point. AI answers are the discovery layer, so product and pricing facts must be crawlable and consistent.

### Gaps
- Nothing was read in full because WebFetch was blocked. Four items rest on summaries only: Google's exact spam-policy wording and examples, the opt-out toggle's global status, OpenAI's August 2026 ads details, and the "sources less visible" change.
- No June–September 2026 core update was confirmed or ruled out.
- No first-party Perplexity or Gemini-app changes to citation behavior were found in the window. No new Google personalization changes were found for June–September (the earlier notes cover Preferred Sources, May 27, and Personal Intelligence, March).
- A Wikipedia snippet lists a ChatGPT "stable release" on Sept 14, 2026 on a new model. This is unverified and not used.
- Whether Search Console now separates AI Mode and AI Overviews data remains unverified.
- Two items surfaced but could not be identified: a "40% less search traffic" finding (Stacked Marketer) and an "AI Mode study" in a weekly roundup ([Anicca](https://anicca.co.uk/blog/weekly-update-search-marketing-25-09-2026/)).

---

## 2. What 2026 evidence says about each content type, and which intents AI answers satisfy vs which still drive clicks

### Takeaway
The best new format-level evidence is StudioHawk's first-party analytics study: 1.2M AI-referred visits across 600+ sites, January–July 2026. Measured as AI referral traffic relative to page supply, the ranking is:
- tools, templates and calculators: **7.5×**
- how-to: 5.65×
- definitions: 5.41×
- listicles: 5.09×
- comparisons: 4.44×
- guides: 4.17×
- statistics pages: 2.52×

Google, meanwhile, shows AI Overviews on almost every "why" (92.3%) and "what" (85.7%) query, and increasingly on commercial searches. So definitional and how-to pages still win some AI-referral clicks but keep losing Google clicks.

Comparison and alternatives pages remain legitimate if they are honest, tested, documented and published in moderation (Lily Ray). The risk is scale and self-ranking. Original data wins citations and mentions more than clicks. Podcasts have only weak, PR-vendor evidence: the transcript is the citable asset. No dataset on case studies was found.

### Cited Findings
*Already established (not repeated):*
- HubSpot/Wix format citation rates — playbook §1
- Growth Memo: primary research earns 3.3× citation density; DATE and NUMBER entities — playbook §1
- Ahrefs: "best X" lists are 43.8% of ChatGPT-cited page types — signals §2
- Lily Ray's early-2026 penalty data and the 69% "omitted from own listicle" finding — playbook §1
- AI Mode sessions are 93% zero-click (Semrush 2025) — signals §5
- Aleyda Solis's "click resilience" dimension — playbook §2/§7

**Format leverage for AI referral clicks**
- **[Observed] StudioHawk "Format Leverage" study (agency).**
  - Data: first-party analytics from 600+ businesses in StudioHawk's portfolio; **1,203,748 AI-referred visits** from ChatGPT, Gemini, Perplexity, Claude and Copilot; January–July 2026.
  - Metric: leverage ratio = share of AI referral traffic ÷ share of pages.

  | Format | AI-traffic leverage |
  |---|---|
  | Interactive tools, templates, calculators | **7.5** |
  | How-to | 5.65 |
  | Definitions | 5.41 |
  | Listicles | 5.09 |
  | Comparison pages | 4.44 |
  | Guides | 4.17 |
  | Statistics pages | 2.52 |

  — [StudioHawk](https://studiohawk.com.au/blog/ai-search-format-leverage/); [Lawrence Hitches](https://www.lawrencehitches.com/ai-traffic-leverage-ratio/). *Caveats:* this is an agency's own client portfolio, with industry mix and page-classification method unknown. It measures clicks, not citations, and is not B2B-construction specific.
- **[Observed] Why calculators earn citations (vendor opinion).** A model can quote the numbers, formula and method around a tool even though it cannot run the tool. — [MaxAEO](https://maxaeo.ai/blog/interactive-tools-ai-citations/)
- **[Observed] Earlier Quotr test.** For "how to estimate drywall for a house", the citations were dominated by calculator pages. Three software vendors won citations that way: EasyTakeoffs, Procore and BuildVision. — tests §3 ([Procore drywall calculator](https://www.procore.com/library/calculators/drywall-calculator), [EasyTakeoffs drywall calculator](https://easytakeoffs.com/calculators/drywall))

**Intent: where AI absorbs the click and where clicks remain**
- **[Observed] Search Engine Journal, summarizing two 2026 studies (Clara Soteras).** The country and dataset of the underlying studies were not captured.
  - Question words that trigger an AI Overview: "why" **92.3%** of the time, "what" **85.7%**, "who" 68.4%.
  - Longer queries are interrogative and 75.2% evergreen.
  - AI Overviews appear on 34.6% of evergreen searches but only **1.1%** during breaking news, and co-occur with Top Stories just 1.4% of the time.
  
  — [Search Engine Journal](https://www.searchenginejournal.com/how-ai-is-reshaping-search-intent-what-2-studies-reveal/587491/)
- **[Observed] Semrush (vendor; study date not confirmed, probably 2025–26).** Over a six-month window, the share of **commercial-intent** results pages with an AI Overview **grew 71%**, while **transactional** fell 5%. — [Semrush](https://www.semrush.com/blog/ai-overviews-commercial-search-study/)
- **[Observed] Directional only; primary source not identified.** Informational queries are 74% zero-click vs 31% for transactional queries. — [Omnibound compilation](https://www.omnibound.ai/blog/zero-click-search-statistics)

**Comparisons, alternatives and best-of lists after the early-2026 crackdown**
- **[Observed] Lily Ray (practitioner), February 2026.**
  - She spoke with about 20 affected companies and found about 40 more; one company had around 2,000 self-promotional listicles.
  - Recurring flaws: the publisher had never used the competitor products, had run no tests, documented no method, and ranked itself #1 simply because it was the publisher.
  - Her position: comparison content "can absolutely be a legitimate and useful content format when done thoughtfully and in moderation. The problem isn't the tactic itself; it's the scale."
  
  — [Lily Ray Substack](https://lilyraynyc.substack.com/p/is-google-finally-cracking-down-on); [ZeroRank summary](https://zerorank.ai/blog/listicle-crackdown). Related: ["It Works Until It Doesn't: AI Content Strategies That Backfire"](https://lilyraynyc.substack.com/p/it-works-until-it-doesnt-ai-content-risks) and the [BuzzStream interview](https://www.buzzstream.com/blog/lily-ray-podcast/) (titles only).
- **[Observed] Contrary practitioner opinion.** Some argue the "listicle penalty" is about scaled, low-quality patterns, not the format, and that honest self-inclusive lists still work. — [SearchLayered](https://searchlayered.com/self-promotional-listicles/); [Ibrahim Furkan Özçelik](https://ibrahimfurkanozcelik.com/writing/listicle-penalty-isnt-about-listicles)
- **[Observed]** Google's May 15 spam policy covers manipulation of AI answers, and coverage names "biased ranking listicles" as an example (§1).
- **[Observed] Earlier Quotr test.** Competitor-owned alternatives pages and G2/Capterra alternatives pages dominate "X alternatives" answers. Quotr's own alternatives posts were cited as sources of facts about competitors (e.g., PlanSwift's pricing), but Quotr itself was not recommended. — tests §2 ([G2 PlanSwift alternatives](https://www.g2.com/products/planswift/competitors/alternatives))

**Original research, indices and benchmarks**
- **[Observed]** StudioHawk found "statistics pages" had the **lowest** AI-traffic leverage (2.52) of the formats measured (above).
- **[Observed] Academic preprint.** Pages whose content is actually absorbed into answers are more likely to contain "numerical facts, definitions, comparisons, and procedural steps" — [arXiv 2604.25707](https://arxiv.org/abs/2604.25707). Details in §4.
- **[Observed] Earlier Quotr test.** Two number-rich Quotr pages were the **first inline citation** in their answers, but Quotr was not named:
  - "Is AI takeoff actually accurate yet?" (94–99% accuracy on clean vector sets, into the 80s on scans);
  - the outsourced-estimating post ($0.25/sq ft under 50k sq ft, $0.10/sq ft above).
  
  — tests §3/§1 ([accuracy post](https://quotr.ai/blog/is-ai-takeoff-actually-accurate-yet/), [outsource post](https://quotr.ai/blog/outsource-construction-estimating/))

**Video, podcasts and LinkedIn**
- **[Observed] Video.** More than half of Google AI Overview and AI Mode social citations are YouTube ([Wellows](https://wellows.com/blog/social-media-ai-citations-report-2026/), vendor). This is in addition to the Ahrefs finding that YouTube mentions are the strongest AI-visibility correlate, at 0.737 ([BusinessWire](https://www.businesswire.com/news/home/20260526119691/en/Across-75000-Brands-YouTube-Mentions-Are-the-Strongest-Signal-of-AI-Visibility-New-Ahrefs-Report-Reveals)). In Quotr's own Perplexity tests, YouTube was never cited for construction-software prompts (tests §5).
- **[Observed] Podcasts: "Podcast Citation Index 2026" (PR agency).**
  - Window: December 2025–May 2026; 5,214 citations of 187 podcasts across five AI engines.
  - Shows without publicly indexed transcripts scored lower on extractability, and most shows outside the top 10 failed on transcript access rather than content quality.
  - Spotify and Apple Podcasts act as distribution surfaces, not citation surfaces.
  
  — [Everything-PR](https://everything-pr.com/the-podcast-citation-index-2026)
  
  A further unverified vendor claim says podcast pages with structured transcripts plus FAQPage/AudioObject markup were cited 2–3× more often. This conflicts with the Ahrefs schema result in §3. — [Parse](https://parse.gl/blog/podcast-ai-visibility-playbook)
- **[Observed] LinkedIn.** LinkedIn had a 14.3% share of ChatGPT Search responses in Q1 2026 (Semrush, as restated above), and Copilot's social citations favor LinkedIn at 43.8% (Wellows). The earlier Semrush finding that *articles* make up 50–66% of cited LinkedIn content is in playbook §3 ([Semrush](https://www.semrush.com/blog/linkedin-ai-visibility-study/)).

**Case studies, templates and glossaries**
- **[Observed]** StudioHawk groups templates with tools (7.5×) and puts definitions at 5.41×, above comparisons and guides.
- **[Observed]** No 2026 dataset isolating citation or click rates for **case studies** was found (see Gaps).

### Inferences
- **[Inference] Intent-to-value map for Quotr** (synthesized from StudioHawk, Search Engine Journal, Semrush, Aleyda Solis and the tests note):

  | Intent (Quotr example) | Does AI answer it fully? | Still drives clicks, demos or signups? | Business value | Best format |
  |---|---|---|---|---|
  | Transactional / pricing ("Quotr pricing", "outsourced estimating price per sq ft") | Partly: AI quotes the numbers | **Yes**, verification and quotes | Highest | Cost guide, pricing page, quote CTA |
  | Commercial investigation ("Togal vs Kreo", "PlanSwift alternatives", "takeoff software for framing subs") | Shortlists in the answer; AI Overviews spreading here | **Yes**, buyers verify | High | Tested comparisons, need-based alternatives, persona pages |
  | Task completion ("drywall calculator", "estimate template") | No: the user must act | **Yes** (7.5× leverage) | Medium (top of funnel, strong path to product) | Calculator, template |
  | Procedural ("how to do a takeoff from PDF plans") | Mostly (AI Overviews on "how/what") | Some AI-referral clicks (5.65×) | Medium-low | Trade-specific how-to with worked example and tool links |
  | Definitional ("what is DDP", "what is a quantity takeoff") | Yes on Google ("what" 85.7%) | Few Google clicks; some AI clicks (5.41×) | Low unless Quotr has a distinct angle | Glossary hub plus a few differentiated definitions |
  | Data-seeking ("material prices 2026", "AI takeoff accuracy") | Answer quotes the number | Low clicks; high citations and mentions | High for brand and PR | Data report / index |
  | Breaking news ("tariff change impact on lumber") | Rarely (AI Overviews on 1.1% of breaking news) | Clicks during the news window | Situational | News explainer |

- **[Inference] Content-type verdicts for Quotr:**

  | Content type | Best 2026 evidence | Verdict |
  |---|---|---|
  | How-to guides | 5.65× leverage; AI Overviews on "how/what" queries | Keep a *few*, trade-specific, answer-first, each with a worked example and a calculator or template link. Merge generic ones. |
  | What-is / glossary | 5.41×; "what" queries trigger AI Overviews 85.7% of the time | One glossary hub plus standalone pages only where Quotr has a distinct angle (DDP / factory-direct, AI takeoff accuracy). |
  | Cost guides | No direct study; Quotr's number-rich pricing post was the first citation; DATE/NUMBER entities predict ChatGPT citations | High priority wherever Quotr owns the numbers. Refresh quarterly. |
  | Comparisons ("vs") | HubSpot: ChatGPT cites comparisons at 95% (prior); 4.44×; Lily Ray on moderation | A few, tested, with disclosure and balance. |
  | Alternatives | Competitor and G2 alternatives pages dominate; policy risk at scale | One page per competitor with real switching demand, grouped by need, never "Quotr #1" by default. |
  | Best-of lists (on quotr.ai) | 69% self-omission; January 2026 hit; spam policy | Don't publish self-ranked lists. Replace them with a neutral "how to choose" guide and pursue third-party lists. |
  | Original research / benchmarks | 3.3× citation density (prior); lowest click leverage (2.52) | A core medium-term bet for citations, mentions and PR, not traffic. |
  | Calculators / tools | 7.5×; drywall-calculator evidence in Quotr's own vertical | High. Build 3–5 trade calculators. |
  | Templates / downloads | Grouped with tools at 7.5× | Medium-high. Show the contents in HTML, not only behind a download. |
  | Case studies | No citation data | Medium, mainly for conversion and corroboration. Publish off-site too (trade press, customer LinkedIn). |
  | Video / YouTube | Strongest correlate; Google surfaces cite YouTube | A companion video for every flagship asset. |
  | Podcasts | Weak PR-vendor evidence | Low. Guest spots only, with transcripts published on quotr.ai. |
  | LinkedIn articles | Articles are 50–66% of cited LinkedIn content; 14.3% ChatGPT Search share; Copilot favors LinkedIn | Cheap reuse: estimator-bylined articles summarizing data and templates. |
  | News explainers | Search Engine Journal (1.1%); AI Mode developing-story carousels | Occasional, only for events that matter to buyers. |

- **[Inference]** Because how-to answers rarely name any software brand (tests §3), top-of-funnel pages help Quotr only if they carry Quotr's own quotable numbers or tools. Otherwise they earn anonymous citations at best.

### Gaps
- No construction/AEC-specific format study.
- No case-study citation or click data.
- The date of the Semrush commercial-intent study and the market of the Search Engine Journal studies were not confirmed.
- StudioHawk's page-type classification and how it handled homepages were not visible. Homepages now receive many ChatGPT clicks after the May 7 branded-link change (signals §4).
- The podcast evidence is PR-vendor only.

---

## 3. Topical authority, cadence, refresh, pruning, AI-assisted writing, E-E-A-T and structured data: 2026 evidence

### Takeaway
The best 2026 evidence on each of these topics:
- **Refresh.** The freshness AI engines reward comes from **maintaining existing pages, not publishing new ones** (Seer: 72% of LLM-cited pages were updated within the past year, but only 42% were published within it).
- **Schema.** It **does not causally move AI citations** (Ahrefs quasi-experiment: AI Mode +2.4% and ChatGPT +2.2%, both noise; AI Overviews −4.6%, confounded by a prior decline).
- **Academic view.** A July 2026 critical survey of 45 studies finds **no GEO technique with a stable, longitudinal, cross-platform causal effect** on discoverability.
- **Clusters and pruning.** The widely quoted multipliers (2–3×, 2.7×, 40–60%) are vendor claims with undisclosed methods.
- **Authors and dates.** Bylines, outbound links and "last updated" dates correlate with citation (HubSpot), but no causal study exists.
- **AI-assisted writing.** Using AI to write is not penalized as such, but scaled or manipulative content is now explicitly spam in AI surfaces.
- **Publishing cadence.** No credible cadence study for small B2B brands was found.

### Cited Findings
*Already established (not repeated):*
- Ahrefs: AI-cited URLs are 25.7% fresher; ChatGPT has the strongest recency bias — playbook §2
- Ahrefs: page count correlates only about 0.19 with AI visibility — playbook §1
- No penalty for AI-written content per se (Ahrefs) — signals §2
- Google says no special schema is needed; Microsoft recommends schema; the SSRN study found a negative schema association — signals §3
- Date-only "refreshes" are discounted — playbook §2

**Refresh and recency**
- **[Observed] Seer Interactive 2026 recency study (agency).** Based on ChatGPT, Gemini and Perplexity citations, March–June 2026.
  - Of **4,124 cited pages** with readable publish and update dates, **72% had been updated in the past year but only 42% were published in the past year**.
  - Seer's conclusion: the freshness LLMs reward "is produced by maintaining old pages, not by publishing new ones".
  - Staleness varies by industry: financial-services content goes stale quickly, energy content stays useful longer.
  - Across Seer's GEO work since 2024, **no brand has had fully accurate representation across LLMs**. Seer recommends tracking the percentage of brand attributes that LLMs report accurately, as a leading indicator ahead of share of voice.
  
  — [Seer Interactive](https://www.seerinteractive.com/insights/study-content-recencys-impact-on-ai-visibility-in-2026)
- **[Observed] Seer, AI bot crawling (study year unclear; possibly its earlier recency study).** About 65% of AI-bot hits targeted content published in the past year, and about 90% hit content from the last three years. — [Seer](https://www.seerinteractive.com/insights/study-ai-brand-visibility-and-content-recency)

**Structured data (schema)**
- **[Observed] Ahrefs, "We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved" (May 11, 2026; vendor quasi-experiment).**
  - Design: 1,885 pages that added JSON-LD between August 2025 and March 2026, compared with 4,000 matched control pages over 30 days before and after.
  - AI Mode: **+2.4%**; ChatGPT: **+2.2%**. Both are statistically indistinguishable from noise.
  - AI Overviews: **−4.6%**, statistically significant, but treated and control pages were both already on a steep downward trend before schema was added.
  
  — [Ahrefs](https://ahrefs.com/blog/schema-ai-citations/); [Cicero summary](https://cicero.studio/en/blog/ahrefs-schema-markup-ai-citations-study-2026/). Critiques: ["right, but testing the wrong thing"](https://www.iloveseo.net/the-ahrefs-schema-study-is-right-and-its-testing-the-wrong-thing/) and a [methodology note](https://mishamanko.com/research/ahrefs-schema-study-methodology) (titles only).
- **[Observed] Correlational counter-data (vendors).** About 71% of ChatGPT-cited pages and 65% of AI Mode-cited pages carry structured data. This is correlation, and it conflicts with Ahrefs' near-null causal result. — [AirOps](https://www.airops.com/blog/chatgpt-content-structure); [Averi](https://www.averi.ai/how-to/llm%E2%80%91optimized-content-structures-tables-faqs-snippets) (the summary did not make clear which page reported which figure)
- **[Observed, unverified]** A claim that direct retrieval tests show AI systems ignore hidden JSON-LD and read only visible HTML. — [GoTechArk](https://gotechark.com/blog/schema-for-ai-citations/)

**Topical authority and hub-and-spoke clusters (weak evidence)**
- **[Observed] Vendor claims, restated by an agency blog. Methods not disclosed.**
  - "Slate's 2026 AI SEO benchmark": domains with 10+ interlinked pages on a topic earn AI citations at **2–3×** the rate of single-page competitors, and hub-and-spoke linking lifts citation rates from about 12% to 41% on pillar queries.
  - Unattributed: clustered content gets "3.2× more AI citations".
  - "Yext 2025": bidirectional internal links give about **2.7×** citation probability.
  
  — [Passionfruit](https://www.getpassionfruit.com/blog/topical-authority-clusters-for-ai-search-citations)

**Pruning and consolidation (weak evidence)**
- **[Observed] Vendor claim.** Consolidation raises AI citation rates by 40–60%. No dataset is disclosed. — [ZipTie](https://ziptie.dev/blog/content-pruning-for-ai-visibility/); related [CompetLab](https://competlab.com/ai-visibility/content-consolidation-ai-visibility)
- **[Observed] Secondary; primary source not verified.** QuickBooks reportedly removed 2,000+ blog posts (over 40% of its Resource Center). Organic traffic rose 20% within weeks and eventually reached 44% above baseline. — [ZipTie](https://ziptie.dev/blog/content-pruning-for-ai-visibility/)

**AI-assisted writing and quality**
- **[Observed]** Google's May 15 spam policy brings manipulation of AI answers, and scaled content abuse in AI surfaces, under enforcement. The September 2026 spam update is live (§1).
- **[Observed] Practitioner.** Lily Ray has documented large brands hit after scaling AI content. — [All I Need For My Website summary](https://www.allineedformywebsite.com/expert-insights/lily-ray-ai-content-scaling-google-penalty/); ["It Works Until It Doesn't"](https://lilyraynyc.substack.com/p/it-works-until-it-doesnt-ai-content-risks)

**E-E-A-T, authors and dates**
- **[Observed] HubSpot "State of AEO 2026" (vendor; ChatGPT, Gemini, Perplexity and AI Overviews citations, December 2025–March 2026), as restated by an agency blog.** Pages with outbound links, statistics, author bios and visible "last updated" dates correlate with higher citation rates. — [Passionfruit summary](https://www.getpassionfruit.com/blog/topical-authority-clusters-for-ai-search-citations); related [HubSpot formats research](https://blog.hubspot.com/marketing/content-format-types-that-earn-citations)
- No causal study linking bylines or credentials to AI citations was found (see Gaps).

**Academic synthesis of GEO evidence**
- **[Observed] "Optimizing Visibility in Generative Engines: A Critical Survey of GEO (2023–2026)".** Version dated July 15, 2026; 45 studies published November 2023–July 2026; academic preprint (SSRN lists the author as Olivier Martinez). Key conclusions:
  - "already-retrieved content can causally alter its citation or use, but no reviewed technique shows a stable, longitudinal, cross-platform causal effect on organic discoverability or downstream behavior".
  - The original GEO paper's gains are "valid within its experimental setting but conditional on a source already being present in a fixed context".
  - Evidence is "strong for a causal effect conditional on context, moderate for certain informational properties, and weak for transmission through to traffic".
  - Commercial audits show "low source overlap, substantial run-to-run variability, and persistent fidelity gaps".
  - It proposes a measurement protocol built on repeated measurements, paraphrases, controls and human validation.
  
  — [arXiv 2607.14035](https://arxiv.org/abs/2607.14035); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7122261)

### Inferences
- **[Inference] Refresh beats new.** Quotr's highest-return "freshness" move is to substantively update the posts that are already retrieved, cited or ranking, rather than publish net-new posts. Updates should add new numbers, a method note, a named author and a visible "Updated [date]: what changed" log. Candidates:
  - the accuracy post;
  - the outsourced-estimating and commercial-estimating pricing posts;
  - the PlanSwift, Togal and STACK alternatives posts;
  - the DDP post.
- **[Inference] Consolidate the listicle and alternatives library.** Merge overlapping "best X 2026" and "X alternatives" posts into:
  - one canonical page per competitor with real switching demand;
  - one neutral buyer's guide.
  
  301-redirect the rest. The evidence for an AI-citation *uplift* from consolidation is weak (vendor claims only), but the *downside* of keeping these pages is documented (the January 2026 hit, the spam policy and the 69% self-omission finding).
- **[Inference] Schema is hygiene, not a lever.** Keep Organization, Article (author, datePublished, dateModified), SoftwareApplication/Product and BreadcrumbList for rich results, Bing/Copilot and entity clarity. Don't budget schema projects as citation drivers, and never mark up content that isn't visible.
- **[Inference] Clusters.** Build a few *deep* clusters around Quotr's three businesses:
  - AI takeoff by trade;
  - estimating service and costs;
  - factory-direct materials, DDP and import.
  
  Avoid broad coverage. The case rests mainly on classic topical relevance, internal linking and user journeys; the AI-specific evidence is weak.
- **[Inference] AI-assisted writing** is acceptable for drafting. Differentiation must come from inputs AI can't synthesize:
  - Quotr's pricing, procurement and takeoff data;
  - tests on real plan sets;
  - estimator review under a named byline with trade and years of experience.
- **[Inference] Cadence.** 96 posts in about 26 weeks is roughly 3.7 per week. The evidence (page count barely correlates with visibility; scaled content was penalized; freshness comes from maintenance) argues for fewer, deeper assets plus a standing refresh programme. See Deliverable 3.
- **[Inference]** The survey's "weak transmission to traffic" finding and the high run-to-run variability mean Quotr should treat every tactic as a hypothesis. Measure with repeated runs and paraphrased prompts, and judge after about 90 days, not after one snapshot.

### Gaps
- No causal evidence on author credentials or E-E-A-T signals and AI citation.
- No credible publishing-cadence study for small B2B brands.
- The uplift figures for topical clusters and pruning are vendor claims with undisclosed methods.
- HubSpot State of AEO 2026 methodology was not visible.
- The critiques of the Ahrefs schema study could not be read beyond their titles.

---

## 4. The structure of a highly citable article, by intent, with examples of frequently cited pages

### Takeaway
Structure matters at the **passage** level. Pages whose content is absorbed into answers are longer, modular, semantically aligned with the answer, and full of **extractable evidence**: definitions, numerical facts, comparisons and procedural steps. However, **Q&A formatting alone does not improve absorption** (arXiv 2604.25707), and schema does not causally help (Ahrefs).

The evidence-backed pattern for a citable page:
1. A direct answer in the first 100–150 words, sitting in the first 30% of the page.
2. H2s that mirror the sub-questions buyers actually ask (query fan-out).
3. A direct 1–2 sentence answer opening each section.
4. Tables for comparisons, numbered steps for procedures, and dated numbers with sources.
5. A named author and a visible update date.

In Quotr's category, the most-cited pages are independent listicles, directory alternatives pages, calculators, cost-data pages, vendor guides, and a couple of Quotr's own number-rich posts, which are cited without Quotr being named.

### Cited Findings
*Already established (not repeated):*
- 44.2% of ChatGPT citations come from the first 30% of a page ([Growth Memo](https://www.growth-memo.com/p/the-science-of-how-ai-pays-attention))
- Titles and URLs that match fan-out sub-queries predict ChatGPT citation ([Ahrefs](https://ahrefs.com/blog/why-chatgpt-cites-pages/))
- Microsoft recommends question-like headings and short single-idea sections ([Microsoft](https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers))
- Google says no chunking is needed and warns that a page per fan-out variant is scaled content abuse ([Google](https://developers.google.com/search/docs/appearance/ai-features))
- Aleyda Solis: the direct answer belongs in the first 1–2 sentences under each heading ([Aleyda Solis checklist](https://www.aleydasolis.com/en/ai-search/ai-search-optimization-checklist/))

**Academic preprints (2026)**
- **[Observed] "From Citation Selection to Citation Absorption" (April 2026, v2).**
  - Sample: 602 controlled prompts across ChatGPT, Google AI Overviews/Gemini and Perplexity; 21,143 valid search-layer citations; 18,151 fetched pages; 72 extracted features.
  - Perplexity cites the most sources per prompt. ChatGPT cites fewer but with "substantially higher average citation influence".
  - High-influence pages are "longer, more modular, more semantically aligned with the generated answer, and more likely to contain extractable evidence genres such as definitions, numerical facts, comparisons, and procedural steps".
  - "**Q&A formatting alone does not improve absorption.**"
  
  — [arXiv 2604.25707](https://arxiv.org/abs/2604.25707); [HackerNoon summary](https://hackernoon.com/what-21000-ai-citations-reveal-about-generative-engine-optimization)
- **[Observed] GEO-SFE (March 2026).** Controlled structural feature engineering at three levels:
  - macro: document architecture;
  - meso: information chunking;
  - micro: visual emphasis.
  
  Across six mainstream generative engines, it improved citation rate by **17.3%** and subjective quality by 18.5%. This is a lab setting in which the page is already in the engine's context. — [arXiv 2603.29979](https://arxiv.org/abs/2603.29979)
- **[Observed] FeatGEO (April 2026).** Optimizing interpretable structural, content and linguistic features improved citation visibility across three engines while keeping or improving content quality. — [arXiv 2604.19113](https://arxiv.org/pdf/2604.19113)

**Vendor and practitioner structure data (2026)**
- **[Observed] Vendors.**
  - 68.7% of ChatGPT-cited pages follow a proper sequential heading structure (H1 → H2 → H3).
  - Pages with question-based headings and FAQ sections see a "2.8× citation lift" (origin of this figure unclear).
  - ChatGPT "left 85% uncited" of the pages it retrieved. This **conflicts** with Ahrefs' earlier finding that about half of retrieved pages get cited (playbook §1).
  
  — [AirOps](https://www.airops.com/blog/chatgpt-content-structure); [Averi](https://www.averi.ai/how-to/llm%E2%80%91optimized-content-structures-tables-faqs-snippets); [Parse](https://parse.gl/blog/content-structure-for-ai-citation)
- **[Observed] Practitioner guidance.** Put direct answers in the first 100–150 words. Open every H2 by answering one question directly, and don't start with a trend, anecdote or generic setup. — [Parse](https://parse.gl/blog/content-structure-for-ai-citation); [HubSpot AEO page-structure guide](https://blog.hubspot.com/marketing/aeo-page-structure)
- **[Observed] HubSpot State of AEO 2026 (vendor).** Outbound links, statistics, author bios and visible "last updated" dates correlate with higher citation rates (§3).

**Examples of frequently cited pages in Quotr's category** (observed in the earlier Perplexity tests of 2026-09-25; their on-page structure could not be inspected)
- **[Observed]** Independent listicles:
  - [constructioncoverage.com/takeoff-software](https://constructioncoverage.com/takeoff-software), cited in 6 prompts;
  - [TheDigitalProjectManager best AI estimating software](https://thedigitalprojectmanager.com/tools/best-ai-estimating-software/), 6 prompts;
  - [ContraVault 10 best AI takeoff tools 2026](https://www.contravault.com/blog/10-best-ai-takeoff-software-tools-for-construction-in-2026).
  
  — tests §5
- **[Observed]** Directory alternatives pages ([G2](https://www.g2.com/products/planswift/competitors/alternatives), Capterra, GetApp, SourceForge) and competitor-owned alternatives posts. — tests §2
- **[Observed]** Calculators (HomeAdvisor, Procore, EasyTakeoffs, BuildVision, CertainTeed), the RSMeans multifamily cost page, and Bluebeam's 2026 takeoff guide. — tests §3
- **[Observed]** Quotr's number-rich accuracy post and its outsourced-estimating pricing post were each the **first inline citation** in their answers, but Quotr was not named ("one outsourced estimating service"). — tests §1/§3

### Inferences
- **[Inference] How to resolve the FAQ conflict.** The academic study (Q&A formatting alone doesn't help) and the vendor claim (2.8×) can both be true if FAQs work only when they carry real, specific evidence. Use 2–5 FAQs only for distinct buyer questions not answered elsewhere on the page, answer each with specifics (numbers, conditions), and don't rely on FAQ schema.
- **[Inference] Being cited without being named is Quotr's specific structural failure.** The fix belongs in the page:
  - a brand-attribution sentence next to each proprietary number (e.g., "Quotr.ai's estimating service charges $0.25/sq ft under 50,000 sq ft (Sept 2026)");
  - a named method ("Quotr Takeoff Accuracy Benchmark");
  - author and organization named near the data.
  
  This makes the fact hard to quote anonymously. It is consistent with Growth Memo's finding that named methods and precise statistics predict citation ([Growth Memo](https://www.growth-memo.com/p/why-proprietary-data-is-your-most)).
- **[Inference]** A universal "citable page" specification, applied to all templates, is given as B0 in Deliverable 1.

### Gaps
- The structure of the construction pages cited in the tests could not be inspected (fetch blocked).
- No study isolates the effect of visible update logs or change notes.
- The origin of the "2.8× FAQ lift" and "85% uncited" figures is unknown.
- The GEO-SFE and FeatGEO lab results may not carry over to organic retrieval (see the §3 survey).

---

## 5. Which prioritization model fits, how to balance short-, medium- and long-term bets, and what credible practitioners recommend

### Takeaway
Practitioners converge on scoring topics by:
- business value (how close to a purchase);
- citation and **mention** potential (unique, verifiable, quotable facts plus a natural reason to name the brand);
- click resilience (tools, live data, decision support, places to act);
- ability to win (existing retrieval, competition, unique assets);
- effort, as a discount;
- a separate **risk gate** for anything that looks like AI-answer manipulation.

On sequencing, maintain and consolidate first (Seer, Lily Ray, Google policy). Then build click-resilient and data assets (StudioHawk, Growth Memo). Throughout, build multi-source third-party consensus (Aleyda Solis, Mike King).

### Cited Findings
*Already established (not repeated):*
- Aleyda Solis: the three prioritization dimensions (click resilience, citation potential, brand-mention potential), the checklist sequence, and "a 3rd-party citation problem" — playbook §1/§2 ([content prioritization](https://www.aleydasolis.com/en/ai-search/content-prioritization-ai-search/); [3rd-party citations](https://www.aleydasolis.com/en/ai-search/ai-search-citations/))
- Growth Memo: the benchmark "which is best" format; proprietary data is "necessary but not sufficient" — playbook §1 ([Growth Memo](https://www.growth-memo.com/p/why-most-original-data-never-gets))
- Profound: the Ramp segment-page case, and 40–60% of cited domains changing month to month — playbook §2/§4 ([Profound volatility](https://www.tryprofound.com/blog/ai-search-volatility))

**New or re-checked practitioner input**
- **[Observed] Mike King / iPullRank (practitioner, agency).**
  - "Relevance engineering" merges content strategy, information retrieval, UX, digital PR and AI, and calls for an omni-media content plan.
  - Quote surfaced in search: "If five out of six sources say your brand is the answer, AI will recommend you. If you only show up once, you disappear." The exact page is not confirmed.
  - iPullRank's AI Search Strategy Program roadmap includes "prioritization criteria, business impact analysis, timelines and milestones".
  
  — [SEO Week 2026 session](https://seoweek.org/mike-king-2026/); [FOUND Conf session](https://foundconf.com/session-mike-king/); [Advanced Web Ranking interview](https://www.advancedwebranking.com/blog/optimizing-new-search-how-relevance-engineering-is-reshaping-seo); [iPullRank program](https://ipullrank.com/ai-search-strategy-program)
- **[Observed] Lily Ray.** Comparisons are legitimate "when done thoughtfully and in moderation"; the problem is scale. — [Lily Ray](https://lilyraynyc.substack.com/p/is-google-finally-cracking-down-on)
- **[Observed] Seer.** Maintain old pages; use accuracy of brand attributes as a leading KPI. — [Seer](https://www.seerinteractive.com/insights/study-content-recencys-impact-on-ai-visibility-in-2026)
- **[Observed] Ahrefs (vendor).** Adding schema doesn't move AI citations (§3). YouTube mentions are the strongest visibility correlate ([BusinessWire](https://www.businesswire.com/news/home/20260526119691/en/Across-75000-Brands-YouTube-Mentions-Are-the-Strongest-Signal-of-AI-Visibility-New-Ahrefs-Report-Reveals)).
- **[Observed] StudioHawk (agency).** Tools, templates and calculators earn the most AI referral traffic per page (§2).
- **[Observed] Academic survey.** Measure with repeated runs, paraphrases and controls; the evidence is weak for effects reaching traffic (§3).
- **[Observed] Search Engine Land / Search Engine Journal (trade press).** Coverage of Google's AI-spam policy (§1) and the intent studies (§2).

### Inferences
- **[Inference] Evidence-strength summary** (synthesized; "+" means helps, "0" means no effect, "−" means hurts):

  | Lever | Direction | Strength of evidence | Key source(s) |
  |---|---|---|---|
  | Front-loaded, answer-first content | + citation | Moderate (large observational study) | Growth Memo (44.2%) |
  | Extractable evidence (numbers, definitions, comparisons, steps) | + absorption | Moderate (academic, observational) | arXiv 2604.25707 |
  | Structural feature engineering | + in lab | Moderate (controlled lab) | arXiv 2603.29979 |
  | Q&A/FAQ formatting on its own | 0 | Moderate (academic) vs vendor claims | arXiv 2604.25707 vs AirOps |
  | Adding schema | 0 | Moderate (vendor quasi-experiment) | Ahrefs, May 2026 |
  | Substantive updates to existing pages | + citation | Moderate (observational) | Seer 2026; Ahrefs |
  | Tools, templates, calculators | + AI clicks | Moderate (first-party analytics, agency) | StudioHawk |
  | Original data / benchmarks | + citations, mentions | Moderate (observational) | Growth Memo |
  | Topical clusters | + ? | Weak (vendor) | Slate/Yext via Passionfruit |
  | Pruning / consolidation | + ? | Weak (vendor, anecdote) | ZipTie |
  | Author bios, "last updated" dates | + (correlation) | Weak–moderate | HubSpot 2026 |
  | Self-ranked listicles or alternatives pages at scale | − | Moderate (case series) plus first-party policy | Lily Ray; Google, May 15 |
  | Scaled AI or templated pages, inauthentic mentions | − | Strong (first-party policy and enforcement) | Google spam policy; Sept 2026 spam update |
  | Third-party mentions, YouTube, earned media | + visibility | Moderate (large correlational) | Ahrefs; Muck Rack; Aleyda Solis |

- **[Inference]** A weighted additive score with gates (Deliverable 2) suits a small team better than a pure multiplicative score. Multiplication makes one-point judgment swings dominate, and it has no natural place for policy risk, which is now the most consequential failure mode.

### Gaps
- No published, validated topic-scoring model for AI search was found. The weights below are judgment anchored in the evidence above and should be recalibrated on Quotr's own 90-day outcomes.
- No construction-specific evidence on how quickly new pages enter AI answers.

### Deliverable 1: Article templates by intent type
*All templates are [Inference], synthesized from the findings above. Each one inherits the B0 baseline.*

#### B0. Baseline for every template (the "citable page" specification)
1. **Title:** plain and descriptive, matching the sub-question: "[Task/Topic] for [trade/persona]: [qualifier]". Add a year only if the content genuinely changes every year (cost guides, data reports). *(Ahrefs title/URL-to-fan-out match; the early-2026 penalty on "2026"-in-title refreshes.)*
2. **URL:** a descriptive slug without the year, so it survives refreshes.
3. **Byline:** a real, named person with role and relevant credentials (e.g., "Senior estimator, 12 years in residential framing"), linked to an author page. Add a "Reviewed by" line where a subject expert reviewed the page. *(HubSpot correlation; no causal evidence.)*
4. **"Last updated [date]"** at the top, plus a short change log at the bottom saying what changed. Only update the date when the substance changes. *(Seer; date-only refreshes are discounted.)*
5. **Answer-first summary:** 40–80 words in the first 100–150 words that directly answer the main question, with the key number or definition. No preamble. *(Growth Memo 44.2%; Parse/HubSpot.)*
6. **Key-facts box or table:** 3–6 facts with numbers, units, dates and sources. *(arXiv 2604.25707 on extractable evidence; Growth Memo DATE/NUMBER.)*
7. **H2s phrased as the sub-questions buyers ask.** Each section opens with a 1–2 sentence direct answer and covers one idea. Do not create separate pages per wording variant. *(Microsoft; Aleyda Solis; Google fan-out warning.)*
8. **Evidence types:** definitions, numbers with units and dates, comparison tables, numbered procedures. *(arXiv 2604.25707.)*
9. **Sources:** link primary sources inline, and describe the method behind Quotr's own data. *(GEO paper, prior notes; HubSpot outbound links.)*
10. **Brand attribution:** one natural sentence tying Quotr to the topic and to any proprietary number ("Quotr.ai (formerly Quotr.io), an AI takeoff, estimating and factory-direct materials platform…"). No keyword stuffing. *(Tests: "cited, not named".)*
11. **FAQs:** optional, 2–5 real and distinct questions answered with specifics. FAQ schema is optional and not a citation lever. *(arXiv; Ahrefs.)*
12. **Visible HTML only:** no hidden text, and no content that exists only in scripts or images. Schema limited to hygiene: Article with author and dateModified, BreadcrumbList, plus type-specific markup. *(Ahrefs; Google.)*
13. **Companion video:** a 1–3 minute YouTube walkthrough embedded on the page, with "Quotr" spoken aloud and in the title and description. *(Ahrefs YouTube correlation; Wellows; Aleyda Solis on AI Mode video.)*
14. **Internal links:** to the cluster hub, the matching tool or template, and the relevant pricing, demo or quote page.
15. **Indexing hygiene:** submitted in Google Search Console and Bing Webmaster Tools; not blocked for OAI-SearchBot, Claude-SearchBot or PerplexityBot. *(signals §1.)*

#### T1. How-to guide (procedural intent)
- **Use for:** "how to do a drywall takeoff from PDF plans"; "how to estimate framing lumber for a 2,400 sq ft house".
- **Outline:**
  1. Answer-first summary: the method in 2–3 sentences, typical time, and the key rule of thumb (e.g., waste factor %).
  2. "What you need": a table of inputs (plan type, scale, units, tools).
  3. Numbered steps, one H3 each: action → why → common mistake → number.
  4. Worked example on a real plan: a quantities table, screenshots or a video.
  5. A "manual vs software vs outsourced" table (time, cost, accuracy, best for). This is where Quotr's software and service fit naturally.
  6. A QA checklist of mistakes to avoid.
  7. FAQ (2–4 questions).
  8. Sources and update log.
- **Must have:** numbered steps, a worked example, at least 1 table, at least 3 dated numbers with units, and a link to the matching calculator or template.
- **Avoid:** generic intros, one page per keyword variant, and unsupported accuracy claims.
- **Refresh:** yearly or when the method or prices change.
- **KPI:** citations across the how-to prompt cluster; assisted demo starts.

#### T2. What-is / definition / glossary page
- **Use for:** a single glossary hub, plus standalone pages only where Quotr has a distinct angle: "What is DDP for construction materials?", "What is AI takeoff (and how accurate is it)?"
- **Outline:**
  1. A one-sentence definition (what category it belongs to + what distinguishes it).
  2. A 2–3 sentence expansion with a number or example.
  3. "How it works": a short numbered list or diagram.
  4. A disambiguation table (e.g., DDP vs FOB vs CIF: who pays freight, duty and insurance; where risk transfers).
  5. When it matters and for whom.
  6. A worked example with numbers.
  7. Links to related terms.
  8. Sources and update date.
- **Must have:** a definition that can be quoted word for word, a comparison table, and an example.
- **Avoid:** thin pages for every variant, and generic terms already owned by Procore, Autodesk or Bluebeam unless Quotr adds data.
- **Refresh:** yearly.
- **KPI:** citation on definitional prompts; internal clicks to tools and cost guides.

#### T3. Cost guide
- **Use for:** "outsourced construction estimating cost per sq ft (2026)", "cost to build a fourplex per sq ft", "drywall cost per sheet 2026".
- **Outline:**
  1. Answer-first range with unit and "as of" date ("As of Sept 2026: $A–$B per sq ft; typical $M").
  2. A price table by segment (size, region, trade, grade) with a source for each row.
  3. What drives the cost (factors with their % impact).
  4. **A method box:** Quotr quote and procurement data (n, date range), supplier price lists, public indices, and exclusions.
  5. A worked budget for a typical project.
  6. How to reduce the cost, including a factual description of the factory-direct/DDP option.
  7. CTA: calculator, "get an estimate" or "request a materials quote".
  8. FAQ.
  9. Update log.
- **Must have:** dated ranges, units, a method, sources, and a brand-attribution sentence next to Quotr's own rates.
- **Avoid:** undated ranges and copying other sites' ranges without a source.
- **Refresh:** **quarterly**, and immediately after any material price shock.
- **KPI:** being named or cited on cost prompts; quote requests.

#### T4. Comparison page (X vs Y, or X vs Y vs Quotr)
- **Use for:** only the pairings buyers actually search, e.g., "Togal vs Kreo", "Quotr vs Togal", "Bluebeam vs STACK for takeoff".
- **Outline:**
  1. **Disclosure line:** "We make Quotr. Here's how we tested."
  2. Verdict by use case: "Choose Togal if…, Kreo if…, Quotr if…"
  3. An at-a-glance table: price (dated, with a link to each vendor's pricing page), platform, supported trades, AI features, outputs, integrations, trial.
  4. **Test results on the same plan set:** time and accuracy against a manual baseline, with screenshots and video.
  5. "Where [competitor] is stronger", stated honestly.
  6. Who should choose which, by persona.
  7. What users say, with links to G2, Capterra and Reddit, quoted accurately.
  8. FAQ.
  9. Method and update log.
- **Must have:** a method, disclosure, balance, and dated pricing with sources.
- **Avoid:** templated pages churned out across dozens of competitors, and unverifiable claims about competitors.
- **Refresh:** quarterly, or whenever a competitor changes pricing or features.
- **KPI:** being named in "X vs Y" answers; demo starts.

#### T5. Alternatives page ("X alternatives")
- **Use for:** one page per competitor with real switching demand, e.g., "PlanSwift alternatives (cloud and Mac options)", "STACK alternatives for small residential subs". Merge duplicate "best X alternatives 2026" posts into these.
- **Outline:**
  1. Answer-first, grouped by why people leave: "If you're leaving PlanSwift because it's Windows-only → A, B; because of the subscription price → C, D."
  2. Why teams switch, with sources (pricing changes, platform limits).
  3. A shortlist table **grouped by need** (not one ranked list): best for, limitations, dated price, platform.
  4. 3–7 short profiles, each with "best for / not for". Quotr appears where it genuinely fits, with disclosure.
  5. Migration notes: file formats, export, learning curve.
  6. How we evaluated: criteria, plus test notes if any.
  7. FAQ.
  8. Update log.
- **Must have:** incumbents and free or cheaper options included, need-based grouping, and disclosure.
- **Avoid:** "Quotr #1" by default, year-only retitles, and 10+ tool dumps.
- **Refresh:** quarterly.
- **KPI:** being named in "X alternatives" answers (currently 1 of 9 comparison prompts, tests §2).

#### T6. Data or benchmark report (original research / index)
- **Use for:** "Quotr Factory-Direct vs US Distributor Materials Price Index (Q4 2026)", "AI Takeoff Accuracy Benchmark: 10 plan sets, 5 tools".
- **Outline:**
  1. 3–5 headline findings, each a quotable sentence with a number and a date.
  2. A key chart plus the underlying data table in HTML.
  3. **Method:** sample, sources, period, definitions, limitations, conflicts of interest.
  4. Results by segment (trade, region, material).
  5. What it means for contractors and developers.
  6. A downloadable CSV and a "cite this report" box with a suggested citation.
  7. A **named method or index** (a stable, reusable name).
  8. Author and reviewer, publication schedule, change log.
  9. Press contact.
- **Must have:** a stable URL (new editions update it, with an archive of past editions), a method, and a named entity.
- **Avoid:** statistics with no method, and cherry-picked comparisons.
- **Refresh:** on a fixed schedule (quarterly index; annual benchmark).
- **KPI:** citations, brand mentions, trade-press pickups and links. Traffic is secondary; statistics pages have the lowest click leverage.

#### T7. Calculator page
- **Use for:** "drywall calculator (sheets, mud, tape, screws)", "concrete yardage calculator", "framing lumber calculator", "outsourced estimating cost calculator".
- **Outline:**
  1. The tool above the fold: works without login, on mobile.
  2. A one-paragraph answer-first explanation of what it calculates and its defaults.
  3. **The formula in visible HTML**, with a worked example.
  4. An assumptions table (waste %, sheet sizes, coverage rates) with sources.
  5. How to read the result and next steps ("for full plan sets, use takeoff software or our estimating service").
  6. Related calculators.
  7. FAQ (2–4 questions).
  8. Estimator byline and update date.
- **Must have:** formula, example and assumptions as visible text; print or export; no gate.
- **Avoid:** tools that only work in JavaScript with no explanatory text.
- **Refresh:** yearly, or when material specs or prices change.
- **KPI:** AI referral clicks, citations on "how to estimate X" prompts, tool-to-trial conversion.

#### T8. Template or download page
- **Use for:** "construction estimate template (Excel/Google Sheets)", "material takeoff sheet", "bid proposal template for subcontractors".
- **Outline:**
  1. Answer-first description: what the template does, who it's for, formats.
  2. **A preview in visible HTML**: sample rows and a list of fields.
  3. Download, ungated or lightly gated (optional email for update notices).
  4. How to use it, as numbered steps.
  5. A filled-in worked example.
  6. When to move up to software (honest thresholds).
  7. FAQ.
  8. Version number and update date.
- **Must have:** the content visible in HTML, because crawlers cannot use a file behind a form; a version number.
- **Avoid:** hard gates and a bare download button with no explanation.
- **Refresh:** 1–2 times a year.
- **KPI:** downloads, citations, trial starts.

#### T9. Case study
- **Use for:** "How a 12-person framing sub cut takeoff time from 6 hours to 40 minutes", or a developer using the estimating service plus DDP procurement.
- **Outline:**
  1. Results summary at the top: numbers with the period and how they were measured.
  2. Customer profile: trade, size, region, project types.
  3. The problem: the process and time before.
  4. What they did: the workflow with Quotr software, service and procurement, with screenshots.
  5. A before-and-after table.
  6. A named quote from the customer with their role.
  7. Limitations and what didn't work.
  8. How similar firms can replicate it.
  9. Links to the product, a relevant comparison and a cost guide.
  10. Date.
- **Must have:** verifiable numbers and a named customer, with permission.
- **Avoid:** anonymous "Company X" stories without numbers.
- **Refresh:** yearly (add outcomes).
- **Distribution:** also place it off-site (trade press, the customer's LinkedIn, a video interview) to create third-party corroboration.
- **KPI:** conversion assist; being named on "does AI takeoff work for [trade]" prompts.

#### T10. News explainer
- **Use for:** events that matter to buyers, e.g., "[tariff or duty change]: what it means for material costs", "[code change]: what estimators need to update", a major AI-takeoff product change.
- **Outline:**
  1. What happened: dated, 2–3 sentences, linking the primary source.
  2. What it means, with numbers: cost impact ranges and effective dates.
  3. Who is affected: trades, regions, materials.
  4. What to do now: a checklist.
  5. A data point from Quotr's own quotes, if available.
  6. A timeline table.
  7. A live update log.
  8. A link to the evergreen cost guide or hub.
- **Must have:** publication within 24–72 hours, primary sources, and a date on every claim.
- **Avoid:** general industry news with no buyer impact. After about 4–8 weeks, fold the content into the evergreen hub.
- **KPI:** clicks during the news window. AI Overviews appear on only 1.1% of breaking-news searches, and AI Mode now shows developing-story link carousels. Trade-press pickup is a secondary KPI.

### Deliverable 2: Topic-scoring model (simple, evidence-anchored)
*[Inference]. Score each topic 1–5 on six criteria, multiply by the weights, and convert to a score out of 100 (weighted sum × 20). Then apply the gates.*

| # | Criterion | Weight | 5 = | 1 = | Evidence anchor |
|---|---|---|---|---|---|
| 1 | **Business value (BV)** | 25% | Maps to a Quotr revenue line (software, estimating service, procurement) at purchase stage (pricing, vs, alternatives, service cost) for a priority persona | Generic awareness, no product path | G2 buyer data and Aleyda Solis "places to act" (prior notes) |
| 2 | **Citation and mention potential (CM)** | 20% | Quotr holds unique first-party numbers or tests, *and* the answer would naturally name a vendor | Commodity information; answers name no brands | Growth Memo; arXiv 2604.25707; tests (how-to answers name no brands) |
| 3 | **Click resilience (CR)** | 15% | Tool, template, live pricing, quote/demo action, or detailed decision support | "What/why" definitions that AI Overviews answer fully | StudioHawk; Search Engine Journal intent data; Aleyda Solis |
| 4 | **Ability to win (AW)** | 20% | A Quotr URL is already retrieved or cited for this prompt cluster, or the niche is uncontested, or Quotr has a unique asset | Answers dominated by G2/Capterra, Procore/Autodesk and entrenched independent listicles | Tests §1–§5; Growth Memo (top 10 domains take 46% of citations) |
| 5 | **Effort, inverted (EF)** | 10% | Refresh in under 1 day | New tool, data pipeline or recurring index | Team capacity |
| 6 | **Risk, inverted (RK)** | 10% | Neutral educational or data content | Self-ranked listicle, scaled templated pages, inauthentic mentions | Google spam policy (May 15); Lily Ray |

**Gates (applied before ranking):**
- **G1 risk gate.** RK ≤ 2 → do not publish as designed. Redesign it (e.g., a neutral guide) or drop it.
- **G2 value gate.** BV ≤ 2 **and** CM ≤ 2 → park it, or fold it into a hub page.

**Tie-breakers, in order:**
1. It fills a prompt where competitors are named but Quotr isn't (tests).
2. It feeds an off-site asset: YouTube, LinkedIn or a trade-press pitch.
3. It consolidates existing posts.

**Horizon assignment:**
- **Short term (0–3 months):** score ≥ 75 and EF ≥ 4. This is mostly refreshes and consolidations, plus bottom-of-funnel pages.
- **Medium term (3–9 months):** score ≥ 65 and EF 2–3. Tools, templates, tested comparisons, first data edition, clusters.
- **Long term (9–18 months):** compounding assets whose value builds over editions and mentions: recurring index, YouTube library, third-party lists, earned media. Start these early even if they score lower on effort.

**Worked example** (scores are illustrative, grounded in the tests note):

| Topic | Type | BV | CM | CR | AW | EF | RK | Score | Gate | Horizon |
|---|---|---|---|---|---|---|---|---|---|---|
| A. Refresh "Outsourced construction estimating cost per sq ft (2026 rates)" | Cost guide (refresh) | 5 | 5 | 4 | 5 | 5 | 5 | **97** | Pass | Short |
| B. "Togal vs Kreo vs Quotr: tested on one residential plan set" | Comparison (new) | 5 | 4 | 4 | 3 | 3 | 3 | **77** | Pass, with method and disclosure | Short → Medium |
| C. Quarterly "Factory-direct vs US distributor materials price index" | Data report | 4 | 5 | 3 | 4 | 2 | 4 | **77** | Pass | Medium (1st edition) → Long (recurring) |
| D. Drywall takeoff calculator | Calculator | 3 | 4 | 5 | 3 | 2 | 5 | **72** | Pass | Medium |
| E. "What is a construction takeoff?" | Definition | 2 | 1 | 1 | 2 | 5 | 4 | **43** | G2 → fold into glossary hub | Only as a hub entry |
| F. New "Best AI takeoff software 2026" ranking Quotr #1 | Self-ranked listicle | 4 | 2 | 3 | 2 | 4 | 1 | 55 | **G1 fail** | Don't publish. Replace with a neutral "How to choose AI takeoff software" guide and outreach to third-party lists |

Rationale for each row:
- **A.** Quotr's post was already the first inline citation but anonymous (tests C12). The refresh adds a brand-attribution sentence, a method box, dated rates and a table. It needs only a refresh (EF 5) and carries no risk.
  - Calculation: 0.25×5 + 0.2×5 + 0.15×4 + 0.2×5 + 0.1×5 + 0.1×5 = 4.85 → 97.
- **B.**
  - For: ChatGPT favors comparisons (HubSpot, prior), and business value is high.
  - Against: answers are dominated by G2 and independent listicles (AW 3), and the page needs genuine testing (EF 3) and careful framing (RK 3).
- **C.** It follows Growth Memo's benchmark pattern. Procurement top-of-funnel prompts are uncontested by software vendors (tests P4/P8), hence AW 4. It needs a data pipeline (EF 2).
- **D.** Tools have 7.5× click leverage (StudioHawk), and calculators dominate "estimate drywall" answers. But competitors already have calculators (AW 3), and it needs developer time (EF 2).
- **E.** "What" queries trigger AI Overviews 85.7% of the time, and generic definitions are owned by Procore, Autodesk and Bluebeam (tests P1).
- **F.** Lily Ray's 69% self-omission finding and Google's spam policy put this below the risk gate.

*Optional quick check:* a multiplicative score, BV × CM × AW × EF, gives the same top four here (A 625, B 180, C 160, D 72). But it ranks F (64) above E (20) because it ignores risk and click resilience, which is why the gate is required.

**Recalibration.** After each quarter, compare predicted and actual results for each topic: named-mention rate on the prompt set, citations (including Bing Citation Share), AI referrals and demo or quote starts. Shift weights by ±5 points toward the criteria that best predicted wins.

### Deliverable 3: Sequencing short-, medium- and long-term bets, and publishing cadence for a small team
*[Inference], grounded in Seer (maintenance > new), Ahrefs (page count ~0; schema null), Lily Ray and Google's policy (scale risk), StudioHawk (tools), Growth Memo (benchmarks), Aleyda Solis and Mike King (third-party consensus), and the arXiv survey (measure over time).*

**Portfolio balance (share of effort):**

| Months | Short-term | Medium-term | Long-term |
|---|---|---|---|
| 0–3 | ~50% | ~30% | ~20% |
| 4–9 | ~30% | ~40% | ~30% |
| 10–18 | ~20% | ~30% | ~50% |

For a 50+ item plan, a workable split is about **18 short-term items** (10 or more of them refreshes or consolidations), **about 22 medium-term** and **about 12 long-term**. Start long-term data collection (price index, accuracy benchmark) in month 1, because it needs lead time.

**Short term (0–3 months): remove risk and turn existing retrieval into named mentions**
1. Audit and consolidate self-ranked "best X" and "X alternatives" posts. Leave one canonical page per competitor with real switching demand (T5/T4) plus one neutral "how to choose" guide; 301-redirect the rest; remove default "#1 Quotr" rankings.
2. Refresh the 5–10 Quotr pages that are already retrieved or cited (tests §5) to B0 standard. Add brand-attribution sentences, dated numbers, method, author and update log. Also fix stale pricing tiers and staging-host indexing (tests B2).
3. Publish 3–5 bottom-of-funnel pages: a pricing explainer, 2–3 tested comparisons (T4), and persona/trade pages (the Ramp pattern, playbook §5).
4. Set up measurement:
   - a monthly prompt set with repeated runs and paraphrases;
   - Bing AI Performance (Intents, Topics, Citation Share);
   - the GA4 AI channel;
   - a "How did you hear about us?" field on demo and quote forms;
   - a brand-attribute accuracy score (Seer).

**Medium term (3–9 months): click-resilient and citation-grade assets**
- 3–5 calculators (T7) and 2–3 templates (T8).
- The first edition of the materials price index and of the AI takeoff accuracy benchmark (T6).
- Two trade clusters (hub plus 5–8 T1/T2/T3 spokes each).
- 2–4 case studies (T9).
- A YouTube companion for every flagship asset.
- Estimator-bylined LinkedIn articles.
- Data pitches to trade press.

**Long term (9–18 months): compounding authority and multi-source consensus**
- Quarterly index editions on a stable URL, and an annual benchmark.
- A consolidated glossary hub.
- Third-party presence: inclusion in independent listicles, G2/Capterra review volume, trade-press coverage.
- A YouTube library.
- News explainers (T10) only when an event matters to buyers.

**Cadence for a small team** (e.g., a content lead, an estimator subject expert at 4–6 h/week, part-time developer and video help):
- **New substantive assets:** 4–6 a month (about 1–1.5 a week), each with a unique input (Quotr data, a test or a tool). This is down from about 16 a month (96 posts in about 6 months).
- **Refreshes and consolidations:** 8–12 a month in months 0–3 (clean-up), then 4–6 a month on a standing basis.
- **Review cycles:**
  - pricing, comparisons, alternatives and cost guides: **quarterly** and whenever something changes;
  - data index: quarterly;
  - how-to, definitions and templates: yearly or when facts change;
  - news explainers: live, then folded into evergreen pages.
- **Monitoring:** monthly, not weekly. Monthly domain drift runs at 40–60% (Profound, prior), so weekly readings are mostly noise. Judge each bet after about 90 days, with at least two runs per prompt.
- **Stop rules:**
  - no new year-in-title retitles without substantive changes;
  - no new self-ranked lists;
  - no pages per fan-out variant;
  - no "seeding" of inauthentic mentions (now explicitly in scope of Google's spam policy per coverage).
- **Off-site in parallel:** every flagship owned asset should get at least one off-site echo: a YouTube video, a LinkedIn article, a trade-press pitch or a community answer. AI recommendations follow multi-source consensus (Mike King; Aleyda Solis's finding that 84–93% of SaaS citation weight is third-party).
