# Renewal Platform
**Status:** Active
**Owner:** Evan Liang
**Last updated:** 2026-06-23

## Goal
Build an autonomous AI agent system that replaces Account Managers for long-tail renewals — giving AM leaders full visibility into each step of the renewal process.

## Current State
Five-person team building individual modules with dummy data. No live CRM integration yet. **Pivoting (2026-06-22) to a single unified dashboard** that consolidates each person's separate dashboard, with a centralized per-account page (buyer-journey tabs). Migration to the unified dashboard is the near-term focus, targeting a demoable version for the AJ demo on 2026-06-25.

By the **2026-06-22 evening standup**, Parth/Evan had executed a first merge — all four builds stitched into one **Combined Dashboard** (informally "DD" / "Daddy Dashboard" / the "Frankenstein"), living in GitHub under a `combined-dashboard` / dashboard-modules folder. The individual agent functionality is working live (Evan's outreach/language/champion models call the API), but the merged UI is judged only ~35–40% there. Team aligned on a git-branch collaboration model (everyone pulls the combined dashboard as `main`, generates a diff to push their individual work into it, then iterates decentralized with GitHub handling merge conflicts) and decided to also spin up a **parallel clean-sheet rebuild** in case the merge gets too messy.

By the **2026-06-23 evening standup**, Aaron had overnight rebuilt his parallel "Frankenstein" dashboard into a fully unified dashboard with its own data model — using the same 28-account fake corpus spanning all stages from Qualify to Buyer — and merged all conflicts (including Dean's latest proposal work) into `main`. The team agreed to go with **Cooper's "parents" architecture** as the primary codebase going forward (over Aaron's approach); Aaron himself advocated this, citing easier conflict management and cleaner backend design. The next forcing function is the **AJ demo on 2026-06-25**: Evan will lead the voiceover, one team member drives navigation, and the full team gathers in a single conference room.

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
- [ ] **Each team member (by 2026-06-24 evening standup):** hook your stage module into the adjacent stage — e.g., pressing "Approve Plan" in qualification auto-navigates to the next stage's view — so the demo has a narrative flow from stage 1 to 4 (2026-06-23 standup)
- [ ] **Evan:** add a time-frame dropdown (Q2/Q3/Q4/All) to the top-level overview dashboard before AJ demo; send calendar invite for the AJ demo conference-room gathering (2026-06-23 standup)
- [ ] **Team:** run through the full integrated demo narrative at the 2026-06-24 evening standup; give feedback on missing functionality (2026-06-23 standup)
- [ ] **AJ demo (2026-06-25):** Evan leads voiceover; one team member drives navigation; all team in one conference room. Demo narrative: account at monitoring → qualify → outreach (draft from signals) → response → proposal (Dean's deck) → buyer hub → admin view
- [ ] Ask Claude to (a) assess which codebase architecture is better, (b) generate a product architecture diagram as an artifact, (c) count lines of code per dashboard (2026-06-23 standup)
- [ ] **Cooper:** create the canonical fake-company JSON corpus (~100–200 companies, each <$10k) and send to the team — still open from 2026-06-22
- [ ] Pull customer contracts in up front — required for the buyer-engagement module to work, and contracts double as renewal signals
- [ ] Evan: set up a call with the LeanData (LD) team who built a data dictionary, as reference for the proposed data dictionary module
- [ ] (Tentative) Weekend standups: ~once/day, ~30 min, around 1pm, opt-in — proposed by Evan 2026-06-22
- [ ] Julia + Evan: value proposition deck targeting AM leaders — due week of 2026-06-23
- [ ] MCP integration: Cooper + Aaron working on real CRM data connection — deferred until module deliverables are stable
- [x] ~~Team: 1:1s with Evan early week of 2026-06-23 to align on AJ demo plan~~ — at least Cooper's 1:1 with Evan happened by 2026-06-22 (referenced in standup)
- [ ] ~~Parth: scope down to champion agent + language agent only~~ — superseded 2026-06-22: Evan proposed Parth take the unified dashboard (top-level + per-stage) piece; language/voice agent remains active
- [x] ~~Dean + Aaron: start the parallel clean-sheet combined dashboard~~ — superseded 2026-06-23: team went with Cooper's "parents" architecture as the primary codebase; Aaron's parallel build was a valuable prototype but not the path forward

## Decision Log
### 2026-06-23 — Team Standup (evening)
- **Decision:** Adopt **Cooper's "parents" architecture** as the primary unified dashboard codebase going forward. Aaron's overnight rebuild (the parallel approach) is acknowledged as valuable but not the path forward.
- **Rationale:** Aaron himself advocated this — each merge of other team members' work into his build required substantial conflict management; Cooper's build was designed with the backend in mind and has a cleaner, more scalable structure. Each team member's module lives in its own folder, making it easy to edit independently.

### 2026-06-23 — Team Standup (evening)
- **Decision:** AJ demo format: Evan leads voiceover/narration; one team member drives screen navigation. All team gathers in a single conference room (not separate remote sessions). Demo will not bounce between views — tighter, structured narrative flow.
- **Rationale:** Cleaner for the audience; Evan has the context and relationship. Mirrors the format of the earlier Franco (Lean Data RevOps) call.

### 2026-06-23 — Team Standup (evening)
- **Decision:** Each team member to hook their stage module into the adjacent stage before the 2026-06-24 evening run-through, enabling a continuous demo narrative from qualification through buyer hub.
- **Rationale:** A disjointed demo that can't flow naturally between stages undermines the product story. The demo narrative: monitoring → qualify → outreach (AI-drafted from signals) → response received → proposal (Dean's deck) → buyer hub → admin view.

### 2026-06-22 — Team Standup (evening)
- **Decision:** Adopt a standard git-branch collaboration model on the Combined Dashboard. Everyone pulls the combined dashboard as the `main` starting point; each person uses Claude to generate a file/diff that pushes their individual module's latest work into it; from then on everyone works decentralized off `main`, committing/pushing and letting GitHub flag/resolve merge conflicts. No single person "holds the master" — it lives in GitHub.
- **Rationale:** Modules were diverging in separate folders; a single shared `main` removes the bottleneck of coordinating who pushes when and lets people work on their own sub-sections without blocking each other. Evan: "this is the point where we start from one, then branch out again — typical software engineering."
### 2026-06-22 — Team Standup (evening)
- **Decision:** Run a **parallel clean-sheet rebuild** alongside the merge. Dean + Aaron start a fresh combined dashboard from product requirements with a single shared data model, scaffolding **all** renewal stages as modules (~6–7 folders, including the still-missing negotiation and close stages), then fill them in one spec at a time. Compare against the merged version to see which is faster/cleaner.
- **Rationale:** Dean's concern that merging four apps will "blow up" once shared data (a common account model across folders) is involved. AI context from prior iterations makes the merged code inefficient; a clean sheet from known requirements may reach the end goal faster with less code. Framed as competition/parallel-pathing "in the name of going fast."
### 2026-06-22 — Team Standup (evening)
- **Decision:** Standardize on one shared corpus of fake companies across all modules. Cooper to create a canonical JSON (e.g. an "Uber" record) and send it to the team so everyone's dummy data matches; target ~100–200 companies, each <$10,000 (Dean).
- **Rationale:** Each person currently uses different fake companies, so the merged dashboard can't pass consistent data between modules. A single corpus lets the integrated flow actually work end-to-end.
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
- **Combined Dashboard merge (2026-06-22 evening):** Parth built the scaffolding dashboard holding an earlier-today version of each of the four projects; Evan cloned a clean-looking dashboard, fed it the four builds, and Claude produced the merged "Frankenstein"/DD. Open question debated at length: whether modules can be cleanly separated into per-folder ownership when shared account data has to sync across folders — Dean skeptical it separates cleanly; Cooper argued one module can simply read/call data from another folder. Working assumption: each person edits only their own section/folder and pushes; if it gets too tangled, fall back to the clean-sheet rebuild.
- **Dean's proposal/deck dashboard (2026-06-22 evening):** rebuilt to match the others' UI for easier reconciliation. Account-level view shows the deck that was sent plus a rationale (why this deck, why this price) and a built-in **price configurator**. Decks are directly editable in-browser (add/choose blocks, edit text per block — "Google Slides on here"). **Automation settings** auto-send proposals when there are no issues, gated by **scenario rules** (save play, executive, competitive threat, flat renewal, increase) that generate customizable default block options, plus pricing policies/guardrails for escalation, and per-scenario **templates** (e.g. an Executive Deck: cover → value delivered → benchmarking → pricing → next steps) that are editable and persist as the new default. Slide automation remains the most painful part (AI image handling; juggling PDF/JPEG/HTML render-vs-edit conversions).
- **Schedule (2026-06-22 evening):** No standup tomorrow (2026-06-23) — the team has a **sales pitch** instead. Dean + Aaron to use the day for the clean-sheet build.
- **Off-site (2026-06-22 evening):** team picked **paintball**; Hannah is sourcing venues. The Santa Clara/San Jose paintball place closed, so likely Livermore. Cooper to send Hannah discount/free paintball tickets (handed out at a Stanford stand).
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
- **June 23 evening standup — Aaron's overnight rebuild:** Aaron rebuilt his parallel "Frankenstein" dashboard overnight into a fully unified dashboard using the same 28-account fake corpus spanning all stages (Qualify to Buyer). Key functional features working: top-level overview (accounts by stage, at-risk count), clickable stage → account-list view, individual account page with Qualify/Outreach/Proposal/Buyer tabs, live signals + next steps + drafts, voice agent (generates renewal emails with tone matching — tested with "Maldives vacation" scenario), email generation via API, Dean's proposal work integrated (per-account ARR, account-specific deck data), search functional, flag-for-review. Not yet complete: buyer hub schema not updated with replacement stream, proposal "generate" button not wired up, time-frame dropdown (Q2/Q3/Q4) for overview. Cooper's dashboard has a middle layer (stage overview before account list), Overview + Monitoring structure, all TypeScript.
- **AJ context (2026-06-23):** AJ = renewals manager at Lean Data, reports to Brian Burkett (CSO/CRO). Manages commercial accounts (smaller, long-tail renewals). AJ persona: skeptical — "what's in it for me to risk my neck to do this?" The CRO (Brian) will buy on headcount/ROI ("you're helping me take out headcount, deliver outcomes, great") and defer to the renewals leader for product validation. Franco = Head of RevOps at Lean Data; advises CRO on technology decisions; not the decision-maker but can advocate. Call with Franco + Parth happened 2026-06-23 (day of standup).
- **Juliet's pitch outline (read by Evan in 2026-06-23 standup):** Targets renewal leaders at B2B SaaS. Pain: "There's nothing worse than sitting in churn reviews... tracking the renewal pipeline week over week only to have deals that look green fall apart at end of quarter." Problem: long-tail SMB/mid-market accounts (20–50% of revenue) get less visibility as rep span grows. Hook: "enterprise-grade renewal motion at commercial scale without additional headcount." Positioning: sub-agents specialize in each renewal step (qualify → outreach → proposal → buyer eval → negotiate → close) with clearly defined inputs/outputs per stage.

## Related Pages
- [Evan Liang](../people/evan-liang.md)
- [Aaron Rose](../people/aaron-rose.md)
- [Dean Liang](../people/dean-liang.md)
- [Parth Godarajesh](../people/parth-godarajesh.md)
- [Cooper Tenney](../people/cooper-tenney.md)
- [Scott](../advisors/scott.md)
- [AJ](../advisors/aj.md)
