# Aaron Rose
**Role:** Team Member, Pareto Agent
**Last updated:** 2026-06-23

## Current Focus
Account intelligence module: identifying who to contact (who/what/when), org chart construction, and champion identification from CRM data.

## Open Tasks
- [ ] Hook account-intelligence module into adjacent stage for AJ demo narrative flow (2026-06-23 standup)
- [ ] Scope down to core champion agent + people research; avoid scope creep into ingestion/output (per Evan direction, 2026-06-19)
- [ ] Prepare module demo for AJ call on 2026-06-25

## Notes
- Module deliverable: account intelligence — given an account, identify who to contact, when, and what to say
- Approach: start with existing CRM contacts, cycle through for engagement, escalate to external enrichment (e.g. Clay) if needed
- Long-tail accounts typically only have a few contacts in CRM (less messy than enterprise)
- Working with MCP data source
- **2026-06-22 standup:** Evan noted Aaron's account-intelligence/qualification work will surface in the unified dashboard at the qualification / qualified stages, and that team members would work closely with Aaron on the key status breakdowns and accounts under each stage — one of the areas where the modules start unifying. (Speaker attribution in this transcript was unreliable; only items Evan explicitly tied to Aaron are recorded here.)
- **2026-06-22 standup (evening):** Tapped by Dean/Evan to co-lead the clean-sheet rebuild of the combined dashboard. (Speaker attribution in this transcript is unreliable; only items explicitly assigned to Aaron are recorded.)
- **2026-06-23 Pitch Contest:** Gave the most concise elevator pitch (~15 seconds, well within the 30-second limit); framed the value prop around the push-pull tradeoff on rep time. Went last among the in-room group.
- **2026-06-23 standup (evening):** Demoed his overnight rebuilt combined dashboard — rebuilt from "Frankenstein" into a fully unified dashboard with its own data model, using the same 28-account fake corpus, pushed to `main` with all conflicts (including Dean's latest proposal work) merged. Voice agent and email generation are live. Aaron himself advocated going with Cooper's "parents" architecture: "Every time it's incorporating these, it wasn't a clean merge. It took a lot of conflict management. So I think we should go with parents." Team agreed; acknowledged Aaron's build was valuable but not the path forward. Aaron described the experience of building from scratch: "What it's best at — when it doesn't have things that has to hook into, it can just generate all that." Cooper praised the build; Evan: "Good job on pulling that up."
- **2026-06-16 morning standup (Granola notes; pre-Fireflies):** Assigned to the **Qualification module** — origin of current module ownership. Led a Claude Code best practices walkthrough for the team: use terminal over desktop app; `/plan` before running anything to avoid failed runs and wasted tokens; `ultrathink`/`ultraplan` for large initial builds only; Advisor mode (Opus 4 reviews Sonnet's output after each run — catches errors, saves tokens net); compact frequently past ~300–400k context; keep `CLAUDE.md` updated after every run with repo layout, constraints, and a handoff prompt for the next session ("after every run, update this file and write a handoff document"); spin up research agents by including "spin up a research agent" in the prompt; skills/MCPs worth exploring: browser tools (screenshots), repo cleanup, PRD/spec generation.
- **2026-06-17 morning standup (Granola notes; pre-Fireflies):** Presented Qualification module research. Juliet's feedback: expand signals beyond usage data — add open support tickets, external company news, CRM call history; use LLM to read conversation history and surface direct quotes (goal: meet or exceed judgment of an average sales rep); churn model should be flexible (customer's own model or out-of-the-box); 14-day usage drop window likely too short; compare price to list price or deal pricing rather than median; "high sell potential" = binary flag passed downstream to proposal module — not a hard price recommendation.
- Email: arose@paretoagent.ai
