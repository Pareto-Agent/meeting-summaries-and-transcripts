# Cooper Tenney
**Role:** Co-founder / Team Member, Pareto Agent
**Last updated:** 2026-06-23

## Current Focus
Buyer hub module: tracking how buyers engage with renewal materials, identifying who else gets involved in the buying process (CFO, procurement, etc.), and gathering engagement signals for the AM leader. As of the 2026-06-22 evening standup, **leading the centralized account-page integration** for the merged Combined Dashboard.

Owning the **account page** within the new unified dashboard (per Evan's proposed split, 2026-06-22). After his 1:1 with Evan, refocused the dashboard on activity/engagement and days-to-renew; it's now a list of accounts plus a recent-activity feed across all accounts (e.g. "added a stakeholder"). Still working on MCP integration for real CRM data.

## Open Tasks
- [ ] Hook qualification-stage module into adjacent stage for AJ demo narrative flow (2026-06-23 standup)
- [ ] Merge dashboard into main once out of Claude usage jail (2026-06-23 standup)
- [ ] Create the canonical fake-company JSON corpus (~100–200 companies, each <$10k) and send it to the team so everyone's dummy data matches (evening standup, 2026-06-22)
- [ ] Send Hannah the discount/free paintball tickets for the off-site (2026-06-22)
- [ ] Build the centralized account page for the unified dashboard (the per-account view the various stage dashboards drill into)
- [ ] Continue MCP integration for real data querying
- [ ] Prepare buyer hub + account page demo for AJ call on 2026-06-25

## Notes
- Module deliverable: buyer hub — once champion engages, track who else gets involved, what information they need, buyer engagement signals
- Idea discussed: SlideShare-style deck tracking (which pages viewed, how many times, who it was forwarded to)
- Updated design scheme to align more closely with Evan's design
- **2026-06-22 standup:** Added column-header sort and a checkbox filter popover to the dashboard (e.g. filter to only tier-upgrade accounts) — built cleanly with Claude. Proposed the migration approach of each person copying their current dashboard and writing integration markdown files so the centralizing agent can quickly tell which files/connections are needed.
- **2026-06-22 standup (evening):** Demoed his account page (buyer-evaluation stage). Argued repeatedly that per-module folder separation is workable — a module can read/call data from another folder when needed — and that the team was over-complicating the merge. Endorsed the git-branch workflow and pushed to merge now ("I'm ready... it opens up more opportunities and doesn't take away"). Supported the parallel clean-sheet idea and suggested Dean draft the combined spec since he "has the best vision."
- **Competitor to study (Evan, 2026-06-22):** **High Spot** — a seller-side sales-enablement company that has built a buyer-engagement module — flagged as a relevant reference for the buyer hub (see [Renewal Platform](../projects/renewal-platform.md) competitive notes).
- **2026-06-23 Pitch Contest:** Went first (order determined by spin wheel). Gave a 30-sec elevator + 5-min sales pitch — ran over the elevator-pitch limit ("I'm running one minute" — Parth). This is the "sales pitch instead of standup" session referenced in the 06-22 evening standup.
- **2026-06-23 standup (evening):** Cooper's "parents" dashboard architecture was selected as the primary codebase going forward (over Aaron's parallel build). Cooper was in "usage jail" (Claude API token limit hit) at the time of the meeting — expected to resolve in ~6 minutes; this was blocking the merge of his dashboard into main. His dashboard was shown to the team: Overview + Monitoring structure, middle layer (stage overview before account list), all TypeScript, modular (each person in own folder), features include approve/flag/flag-for-review per account. Numbers slightly off in demo (1–6 instead of 1–7 in one view) and some data not loaded. Team noted each person's section in its own folder makes independent editing clean.
- Email: ctenney@paretoagent.ai
