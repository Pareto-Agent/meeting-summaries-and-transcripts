# Renewal Platform
**Status:** Active
**Owner:** Evan Liang
**Last updated:** 2026-06-19

## Goal
Build an autonomous AI agent system that replaces Account Managers for long-tail renewals — giving AM leaders full visibility into each step of the renewal process.

## Current State
Five-person team building individual modules with dummy data. No live CRM integration yet. Each module producing a specific deliverable. First design partner demo (AJ) scheduled for 2026-06-25.

## Module Architecture
| Module | Owner | Deliverable |
|--------|-------|-------------|
| Account intelligence | Aaron Rose | Who/what/when — champion identification, org chart, contact waterfall |
| Renewal deck / story | Dean Liang | Renewal narrative and deck — the "why" for pricing |
| Buyer hub | Cooper Tenney | Engagement tracking — who opens, who else gets involved, buyer signals |
| Agent orchestration | Parth Godarajesh | Champion agent, language/voice agent, response agent — core micro-agent layer |
| Admin dashboard | Cooper Tenney | Snapshot of all accounts; renewals health view for AM leader |

## Open Items
- [ ] All modules: keep using dummy data, define each module's deliverable clearly before stitching — owner: all, deadline: week of 2026-06-23
- [ ] Parth: scope down to champion agent + language agent only (per Evan, 2026-06-19)
- [ ] Julia + Evan: value proposition deck targeting AM leaders — due week of 2026-06-23
- [ ] Team: 1:1s with Evan early week of 2026-06-23 to align on AJ demo plan
- [ ] AJ demo: validate stages + visibility hypothesis — 2026-06-25
- [ ] MCP integration: Cooper + Aaron working on real CRM data connection — deferred until module deliverables are stable

## Decision Log
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
- **Working cadence** (as of 2026-06-19): two standups per day (morning + afternoon); afternoon standup moving to 5:30pm
- MCP = external CRM data source (e.g. Lean Data); used to query account/contact data without storing it centrally
- Clay discussed as contact enrichment waterfall for champion identification
- SlideShare-style deck engagement tracking floated as feature idea for buyer hub (which pages opened, by whom, how many times)
- "John from Site Tracker" mentioned as a prospect who wanted champion-finding help
- Julia (role unclear — possibly a team member or contractor) working on value prop deck

## Related Pages
- [Evan Liang](../people/evan-liang.md)
- [Aaron Rose](../people/aaron-rose.md)
- [Dean Liang](../people/dean-liang.md)
- [Parth Godarajesh](../people/parth-godarajesh.md)
- [Cooper Tenney](../people/cooper-tenney.md)
- [Scott](../advisors/scott.md)
- [AJ](../advisors/aj.md)
