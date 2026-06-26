# Aaron Rose
**Role:** Team Member, Pareto Agent
**Last updated:** 2026-06-26

## Current Focus
**Owns the qualification workstream** (confirmed in the 2026-06-26 re-org) — LeanData data → qualify/categorize accounts; pricing/modeling to follow. Continues account-intelligence work (who to contact, org chart, champion identification).

## Open Tasks
- [ ] Broaden the data pull to serve all workstreams, not just qualification — contracts and emails are needed downstream; resolve how to fetch full contract PDFs (MCP points to them but can't download them) (2026-06-26 standup)
- [x] ~~Prepare module demo for AJ call on 2026-06-25~~ — occurred
- [ ] Validate qualification rules with Evan — are churn-risk and upsell classifications correct? (June 25 evening standup)
- [ ] Build standup scrum board displaying team daily tasks; link to Dropbox transcript folder for eventual automation (June 25 evening standup)
- [ ] Send updated slide deck to Evan for feedback before next market research call (June 25 evening standup)
- [ ] Implement global filter across entire dashboard website — selected period applies to all views simultaneously (June 24 evening standup)
- [ ] Update account data to reflect only 4 quarters of 2026 (not multi-year) (June 24 evening standup)

## Notes
- **2026-06-26 standup (work re-org):** Qualification confirmed as Aaron's single-owner workstream (decoupled from the prototype). Evan flagged that Aaron currently pulls only what qualification needs — the data layer should also pull contracts (physical PDFs) and emails for the other workstreams; contract PDFs can't currently be downloaded through the LeanData MCP.
- Module deliverable: account intelligence — given an account, identify who to contact, when, and what to say
- Approach: start with existing CRM contacts, cycle through for engagement, escalate to external enrichment (e.g. Clay) if needed
- Long-tail accounts typically only have a few contacts in CRM (less messy than enterprise)
- Working with MCP data source
- **2026-06-25 standup (evening, post-AJ-demo):** Proposed a structured standup format: "Today, this is what I worked on. This is what I'm working on. This is what's blocking me." — displayed on a visual dashboard artifact. Plans to build a scrum board linked to Dropbox transcripts folder; estimates 1-2 weeks to automate. Reported qualification module is working end-to-end (downloads emails/calls from LeanData, combs through for upsell/churn signals); next step is rule validation with Evan. Worked on slides today (not code). Sent updated deck for Evan's feedback.
- **2026-06-24 standup (evening, pre-AJ-demo):** Tasked with implementing a global dashboard filter and updating data to 4 quarters 2026 only.
- **2026-06-22 standup:** Evan noted Aaron's account-intelligence/qualification work will surface in the unified dashboard at the qualification / qualified stages, and that team members would work closely with Aaron on the key status breakdowns and accounts under each stage — one of the areas where the modules start unifying. (Speaker attribution in this transcript was unreliable; only items Evan explicitly tied to Aaron are recorded here.)
- **2026-06-22 standup (evening):** Tapped by Dean/Evan to co-lead the clean-sheet rebuild of the combined dashboard. (Speaker attribution in this transcript is unreliable; only items explicitly assigned to Aaron are recorded.)
- **2026-06-23 Pitch Contest:** Gave the most concise elevator pitch (~15 seconds, well within the 30-second limit); framed the value prop around the push-pull tradeoff on rep time. Went last among the in-room group.
- **2026-06-23 standup (evening):** Demoed his overnight rebuilt combined dashboard — rebuilt from "Frankenstein" into a fully unified dashboard with its own data model, using the same 28-account fake corpus, pushed to `main` with all conflicts (including Dean's latest proposal work) merged. Voice agent and email generation are live. Aaron himself advocated going with Cooper's "parents" architecture: "Every time it's incorporating these, it wasn't a clean merge. It took a lot of conflict management. So I think we should go with parents." Team agreed; acknowledged Aaron's build was valuable but not the path forward. Aaron described the experience of building from scratch: "What it's best at — when it doesn't have things that has to hook into, it can just generate all that." Cooper praised the build; Evan: "Good job on pulling that up."
- **2026-06-16 morning standup (Granola notes; pre-Fireflies):** Assigned to the **Qualification module** — origin of current module ownership. Led a Claude Code best practices walkthrough for the team: use terminal over desktop app; `/plan` before running anything to avoid failed runs and wasted tokens; `ultrathink`/`ultraplan` for large initial builds only; Advisor mode (Opus 4 reviews Sonnet's output after each run — catches errors, saves tokens net); compact frequently past ~300–400k context; keep `CLAUDE.md` updated after every run with repo layout, constraints, and a handoff prompt for the next session ("after every run, update this file and write a handoff document"); spin up research agents by including "spin up a research agent" in the prompt; skills/MCPs worth exploring: browser tools (screenshots), repo cleanup, PRD/spec generation.
- **2026-06-17 morning standup (Granola notes; pre-Fireflies):** Presented Qualification module research. Juliet's feedback: expand signals beyond usage data — add open support tickets, external company news, CRM call history; use LLM to read conversation history and surface direct quotes (goal: meet or exceed judgment of an average sales rep); churn model should be flexible (customer's own model or out-of-the-box); 14-day usage drop window likely too short; compare price to list price or deal pricing rather than median; "high sell potential" = binary flag passed downstream to proposal module — not a hard price recommendation.
- Email: arose@paretoagent.ai
