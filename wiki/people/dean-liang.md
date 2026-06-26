# Dean Liang
**Role:** Team Member, Pareto Agent
**Last updated:** 2026-06-25

## Current Focus
Storytelling / renewal deck module: generating the narrative and renewal deck for each account given account intelligence and context. Now building a drag-and-drop, configurable deck editor backed by a block library, so the deck can be edited in the browser (intended for the forward-deployed engineer to adjust decks).

## Open Tasks
- [x] ~~Prepare renewal deck module demo for AJ call on 2026-06-25~~ — occurred; Dean showed the customer-facing demo design at June 24 evening standup
- [ ] Work on pricing engine in a separate local environment (not main demo repo) to avoid breaking the dashboard for 1-2 days (June 25 evening standup)
- [ ] Think through product architecture — shared components, data flow between stages, how real LeanData data will integrate (Evan asked, June 25 evening standup)
- [ ] Timeline slider: build configurable follow-up and escalation timer UI (currently in progress, June 25 evening standup)
- [ ] Merge account page code to ensure visual consistency across the interface (June 24 evening standup)

## Notes
- Module deliverable: renewal story/deck — the "why" of how to justify renewal pricing for each account
- Preference: 1:1 meetings for technical/data-specific questions (raised in standup working-cadence discussion)
- **2026-06-25 standup (evening, post-AJ-demo):** Working on UI small things + building a configurable timeline slider for follow-up and escalation timing. Raised the pricing engine question: unifying how each sub-agent classifies/prices an account would require breaking the demo environment for 1-2 days. Evan suggested working on it locally/separately. Evan asked Dean to think through product architecture (shared components, cross-stage data flow) as real LeanData data integration approaches.
- **2026-06-24 standup (evening, pre-AJ-demo):** Showed customer-facing demo design to the team — per-stage output view (outreach email → proposal deck → buyer engagement → negotiation → closing), intended to be used alongside the dashboard during the AJ demo. Had a merge conflict mid-meeting when the standardized account page was accidentally overwritten; resolved.
- **2026-06-22 standup:** Rebuilt the slides from scratch using a 6-slide template, then had AI synthesize ~14 more on top of it (still needed heavy back-and-forth per slide; thinks the result looks better than the original six). Building scenario decks (flat renewal, increase, executive competitive threat), ~6 big slides each. Credited by Evan with the centralized-account-page idea behind the unified dashboard.
- **2026-06-22 standup (evening):** Demoed a heavily-rebuilt proposal dashboard (very different from 9am): account-level view with the sent deck, rationale, a built-in price configurator, in-browser deck editing (blocks + text), and automation settings with scenario rules (save play / executive / competitive threat / flat / increase), pricing guardrails, and editable per-scenario templates. Called slide automation "one of the most annoying things I've ever worked on" (AI image handling, PDF/JPEG/HTML conversion). Skeptical the merge separates cleanly once shared account data is involved; pushed the clean-sheet fallback ("if I was designing a combined app from scratch with a single data model, let me specify the requirements — that might be faster"). Agreed to lead the clean-sheet build with Aaron and credited the day's chaos as expected ("I expected us to be a bit more chaotic — we're reaching that point").
- **2026-06-23 Pitch Contest:** Gave a polished 5-minute pitch using the shared team slide deck (went after Cooper and Parth); articulated the maturity-levels differentiation and three entry-point call-to-action.
- **2026-06-23 standup (evening):** Dean's latest proposal work had been merged into Aaron's combined dashboard by Aaron (Evan: "I have no idea what it does. I would love for Dean to tell me what I'm looking at"). The per-account deck now updates based on account name — e.g. switching to Dunder Mifflin shows Dunder Mifflin numbers, champion name populated in text. Evan asked Dean to clarify what his latest drop does within the combined build.
- **2026-06-16 morning standup (Granola notes; pre-Fireflies):** Assigned to the **Proposal module** — origin of current module ownership.
- **2026-06-17 morning standup (Granola notes; pre-Fireflies):** Presented Proposal module research. Agent ingests signals from Qualification and Outreach, decomposes existing PowerPoint templates into story components, and reassembles into a tailored renewal deck. Pricing logic for v1: identify renewal increase vs. downsell risk — keep it simple. Key principle: value story and numbers must be consistent end-to-end. Juliet's feedback: value story is critical — include new features/capabilities released since last renewal; think through structural "elements of a value story"; modular slide components (ROI, usage, pricing, new features) that can be mixed and matched (how AMs already work today); objection handling is out of scope for this agent — goes to a separate downstream agent.
- Email: dliang@paretoagent.ai
