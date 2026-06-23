# Cooper Tenney
**Role:** Co-founder / Team Member, Pareto Agent
**Last updated:** 2026-06-22

## Current Focus
Buyer hub module: tracking how buyers engage with renewal materials, identifying who else gets involved in the buying process (CFO, procurement, etc.), and gathering engagement signals for the AM leader. As of the 2026-06-22 evening standup, **leading the centralized account-page integration** for the merged Combined Dashboard.

Owning the **account page** within the new unified dashboard (per Evan's proposed split, 2026-06-22). After his 1:1 with Evan, refocused the dashboard on activity/engagement and days-to-renew; it's now a list of accounts plus a recent-activity feed across all accounts (e.g. "added a stakeholder"). Still working on MCP integration for real CRM data.

## Open Tasks
- [ ] **Lead the centralized account-page integration** (evening standup, 2026-06-22): figure out how to pull the right code/functionality from each module into the single per-account page everyone lands on regardless of stage — "an interesting test for Claude," per Dean
- [ ] Create the canonical fake-company JSON corpus (~100–200 companies, each <$10k) and send it to the team so everyone's dummy data matches (evening standup, 2026-06-22)
- [ ] Add the API key Evan's build depends on (his merged build uses Cooper's key, which others can't access) — "later today" (2026-06-22)
- [ ] Pull the Combined Dashboard, diff his module against it, and generate a file to push his changes in (evening standup, 2026-06-22)
- [ ] Write a spec for his module (parallel clean-sheet effort, 2026-06-22)
- [ ] Send Hannah the discount/free paintball tickets for the off-site (2026-06-22)
- [ ] Build the centralized account page for the unified dashboard (the per-account view the various stage dashboards drill into)
- [ ] Keep a copy of the current dashboard to iterate on during the unified-dashboard migration; write an integration markdown file documenting connections / required components
- [ ] Continue MCP integration for real data querying
- [ ] Prepare buyer hub + account page demo for AJ call on 2026-06-25
- [ ] Keep using dummy data until module deliverable is well-defined (per Evan direction, 2026-06-19)

## Notes
- Module deliverable: buyer hub — once champion engages, track who else gets involved, what information they need, buyer engagement signals
- Idea discussed: SlideShare-style deck tracking (which pages viewed, how many times, who it was forwarded to)
- Updated design scheme to align more closely with Evan's design
- **2026-06-22 standup:** Added column-header sort and a checkbox filter popover to the dashboard (e.g. filter to only tier-upgrade accounts) — built cleanly with Claude. Proposed the migration approach of each person copying their current dashboard and writing integration markdown files so the centralizing agent can quickly tell which files/connections are needed.
- **2026-06-22 standup (evening):** Demoed his account page (buyer-evaluation stage). Argued repeatedly that per-module folder separation is workable — a module can read/call data from another folder when needed — and that the team was over-complicating the merge. Endorsed the git-branch workflow and pushed to merge now ("I'm ready... it opens up more opportunities and doesn't take away"). Supported the parallel clean-sheet idea and suggested Dean draft the combined spec since he "has the best vision."
- **Competitor to study (Evan, 2026-06-22):** **High Spot** — a seller-side sales-enablement company that has built a buyer-engagement module — flagged as a relevant reference for the buyer hub (see [Renewal Platform](../projects/renewal-platform.md) competitive notes).
- Email: ctenney@paretoagent.ai
