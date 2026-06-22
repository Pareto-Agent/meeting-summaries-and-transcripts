# Renewal Platform
**Status:** Active
**Owner:** Evan Liang
**Last updated:** 2026-06-22

## Goal
Build an autonomous AI agent system that replaces Account Managers for long-tail renewals — giving AM leaders full visibility into each step of the renewal process.

## Current State
Five-person team building individual modules with dummy data. No live CRM integration yet. **Pivoting (2026-06-22) to a single unified dashboard** that consolidates each person's separate dashboard, with a centralized per-account page (buyer-journey tabs). Migration to the unified dashboard is the near-term focus, targeting a demoable version for the AJ demo on 2026-06-25.

## Module Architecture
| Module | Owner | Deliverable |
|--------|-------|-------------|
| Account intelligence | Aaron Rose | Who/what/when — champion identification, org chart, contact waterfall; surfaces in the unified dashboard at the qualification/qualified stages |
| Renewal deck / story | Dean Liang | Renewal narrative and deck — the "why" for pricing |
| Buyer hub | Cooper Tenney | Engagement tracking — who opens, who else gets involved, buyer signals |
| Agent orchestration | Parth Godarajesh | Champion agent, language/voice agent, response agent — core micro-agent layer |
| Unified dashboard | Parth Godarajesh (top-level + per-stage views) + Cooper Tenney (account page) | Single dashboard across the whole book of business + centralized account page; supersedes the separate admin dashboard (proposed cross-functional split, Evan, 2026-06-22) |
| Data dictionary (proposed) | TBD | Per-customer canonical field definitions — what "ARR"/"renewal" means and which field maps to it (new module idea floated by Evan, 2026-06-22) |

## Open Items
- [ ] **Unified dashboard migration plan** (team, 2026-06-22): (1) build a fake/placeholder unified dashboard, (2) everyone freezes & saves their current work as a fallback before the migration, (3) detach each person's dashboard from their underlying agents/functionality, (4) integrate agents into the unified dashboard one stage at a time (qualification → outreach → …). Use the fake-data pipeline for the integration.
- [ ] Each person: keep a copy of their current dashboard to iterate on during the migration; create an integration markdown file documenting connections / required components so the centralizing agent can read them
- [ ] Pull customer contracts in up front — required for the buyer-engagement module to work, and contracts double as renewal signals
- [ ] Evan: set up a call with the LeanData (LD) team who built a data dictionary, as reference for the proposed data dictionary module
- [ ] AJ demo: validate stages + visibility hypothesis, now with the unified dashboard demoable — 2026-06-25
- [ ] (Tentative) Weekend standups: ~once/day, ~30 min, around 1pm, opt-in — proposed by Evan 2026-06-22
- [ ] Julia + Evan: value proposition deck targeting AM leaders — due week of 2026-06-23
- [ ] MCP integration: Cooper + Aaron working on real CRM data connection — deferred until module deliverables are stable
- [x] ~~Team: 1:1s with Evan early week of 2026-06-23 to align on AJ demo plan~~ — at least Cooper's 1:1 with Evan happened by 2026-06-22 (referenced in standup)
- [ ] ~~Parth: scope down to champion agent + language agent only~~ — superseded 2026-06-22: Evan proposed Parth take the unified dashboard (top-level + per-stage) piece; language/voice agent remains active

## Decision Log
### 2026-06-22 — Team Standup
- **Decision:** Consolidate the team's separate dashboards into a single unified dashboard plus a centralized per-account page (buyer-journey tabs across the top; status/stage and an audit log of steps per account).
- **Rationale:** Gives the AM leader uniform visibility across all stages and accounts — something renewals managers don't have today. In an agentic world the automations move deals between stages (no manual CRM data entry), so over time this format can replace the CRM (syncs with the CRM to start).
### 2026-06-22 — Team Standup
- **Decision:** Design the system *not* assuming a human (AM) in the loop at each step; the human who reviews/tunes/onboards is the **forward-deployed engineer (FD)**, not the customer.
- **Rationale:** AJ feedback — customers do not want to configure their own agents ("you tell us our voice through analysis"). Many accounts handed to Pareto have no AM assigned at all. Acknowledged by Evan as a fair, explicit risk factor (real-world rollout will likely be gradual, AM-as-champion first); raised as a discussion point during the standup.
### 2026-06-19 — Team Standup
- **Decision:** Continue using dummy data for at least another week; do not stitch modules together yet.
- **Rationale:** Still in product definition phase. Stitching data too early distracts from clarifying what each module does well. "Build a great leg before building the chair."
### 2026-06-19 — Team Standup
- **Decision:** Product is autonomous agent (not a co-pilot). Goal is to replace AMs, not assist them.
- **Rationale:** Long-tail AM leaders can't manage hundreds of accounts; they need AI that runs the process, not a tool that helps them run it.
### 2026-06-19 — Team Standup
- **Decision:** Target buyer = CRO (budget), end user = AM Leader. ICP = companies with $10M+ ARR (also PE-backed).
- **Rationale:** CRO cares about scalability and revenue; AM leader is the daily user. Validated through multiple customer research calls.
### 2026-06-19 — Team Standup
- **Decision:** Core value proposition to AM leader = **visibility** — concrete, measurable deliverables at each renewal step, like a manufacturing floor.
- **Rationale:** AM leaders with 400+ accounts are reactive and don't have a methodical process. Giving them visibility into each step is the differentiated value vs. generic LLM tools.

## Notes
- **Unified dashboard design (2026-06-22):** top-level book-of-business metrics + a pipeline funnel by stage; a "monitoring" stage (name still TBD) for deals not yet in a defined stage; viewable by quarter. Clicking a stage drills into a per-stage dashboard; clicking an account drills into a single centralized account page (the same page regardless of stage). Centralized-account-page idea credited to Dean. Plan to zip the Replit prototype and hand it to Claude Code to centralize the team's agents onto it.
- **Data dictionary (new module idea, 2026-06-22):** per-customer mapping from canonical business terms to concrete fields (e.g. "when we say ARR, use this field"; "renewal means this, calculated this way"). Rationale: every agentic company has this problem — without it, every agent re-derives field meanings. Used for signal validation. Evan to reference LeanData's internal data dictionary (LD is instead shipping a dedupe module).
- **Renewal plan / forecasting view (2026-06-22, owner not reliably attributable in transcript):** a renewal-plan view is being refined per Scott's feedback — cleaner per-account plan layout; header metrics for amount expiring per month and projected ARR (with churn/upsell forecasting, possibly applying a churn-percentage rather than subtracting all forecasted churn); an NRR waterfall chart (Scott's suggestion — grouping the "down" movements together is being explored to make it less confusing); and a rules engine where rules written in plain English are auto-coded (signals → rules → plans). Being prepared to port/send data to other modules.
- **Fake vs. real data (2026-06-22):** reaffirmed using the fake/dummy-data pipeline for the dashboard integration — fake data is evenly distributed across categories so design gaps surface rather than data gaps; real-data reintegration is described as a small change later.
- **Process direction (2026-06-19 working session):** goal for the coming week is to maintain velocity while starting to coordinate more across modules; Evan expects to change/innovate on process to enable this. Plan to bring in external people to evaluate whether the team is building things correctly, and to trial some sessions as **demos instead of code reviews**.
- **Working cadence** (as of 2026-06-19): two standups per day (morning + afternoon); afternoon standup moving to 5:30pm
- MCP = external CRM data source (e.g. Lean Data); used to query account/contact data without storing it centrally
- Clay discussed as contact enrichment waterfall for champion identification
- SlideShare-style deck engagement tracking floated as feature idea for buyer hub (which pages opened, by whom, how many times)
- "John from Site Tracker" mentioned as a prospect who wanted champion-finding help
- **Competitive exercise (2026-06-22):** Evan had the team map a competitor to each module (tracked on an "intern sheet") to inform dashboard/account-page design. Called out for the **buyer hub: High Spot** — a sales-enablement (seller-side) company that has built a buyer-engagement module — as a relevant reference to study ("someone who tried to do it from a very different perspective"). Evan said he's "not worried" about it competitively.
- Julia (role unclear — possibly a team member or contractor) working on value prop deck

## Related Pages
- [Evan Liang](../people/evan-liang.md)
- [Aaron Rose](../people/aaron-rose.md)
- [Dean Liang](../people/dean-liang.md)
- [Parth Godarajesh](../people/parth-godarajesh.md)
- [Cooper Tenney](../people/cooper-tenney.md)
- [Scott](../advisors/scott.md)
- [AJ](../advisors/aj.md)
