# Renewal Platform
**Status:** Active
**Owner:** Evan Liang
**Last updated:** 2026-06-26

## Goal
Build an autonomous AI agent system that replaces Account Managers for long-tail renewals — giving AM leaders full visibility into each step of the renewal process.

## Current State
Five-person team building individual modules with dummy data. No live CRM integration yet. **Pivoting (2026-06-22) to a single unified dashboard** that consolidates each person's separate dashboard, with a centralized per-account page (buyer-journey tabs). Migration to the unified dashboard is the near-term focus, targeting a demoable version for the AJ demo on 2026-06-25.

By the **2026-06-22 evening standup**, Parth/Evan had executed a first merge — all four builds stitched into one **Combined Dashboard** (informally "DD" / "Daddy Dashboard" / the "Frankenstein"), living in GitHub under a `combined-dashboard` / dashboard-modules folder. The individual agent functionality is working live (Evan's outreach/language/champion models call the API), but the merged UI is judged only ~35–40% there. Team aligned on a git-branch collaboration model (everyone pulls the combined dashboard as `main`, generates a diff to push their individual work into it, then iterates decentralized with GitHub handling merge conflicts) and decided to also spin up a **parallel clean-sheet rebuild** in case the merge gets too messy.

By the **2026-06-23 evening standup**, Aaron had overnight rebuilt his parallel "Frankenstein" dashboard into a fully unified dashboard with its own data model — using the same 28-account fake corpus spanning all stages from Qualify to Buyer — and merged all conflicts (including Dean's latest proposal work) into `main`. The team agreed to go with **Cooper's "parents" architecture** as the primary codebase going forward (over Aaron's approach); Aaron himself advocated this, citing easier conflict management and cleaner backend design. The next forcing function is the **AJ demo on 2026-06-25**: Evan will lead the voiceover, one team member drives navigation, and the full team gathers in a single conference room.

On the morning of **2026-06-24**, Evan ran a full end-to-end demo of the Combined Dashboard for **Juliet Lo** (remote). Juliet gave strong positive feedback — "massive kudos", "feels real", "feels robust", "totally impressed at how much has taken place over the last few days." The team is now ~24 hours from the AJ demo. Key clarifications from the session: (1) "telemetry" is a better framing than "dashboard" — stages are populated automatically by agents, not by humans entering CRM data; (2) the best demo approach is walking through a **single deal progressing through all stages**, showing actual automation outputs (email drafts, proposal deck, buyer hub engagement telemetry) — not a time-slider animation; (3) email/proposal **auto-send flow**: drafts are created in advance and sent automatically on a timeline by default; the manager can review/edit during the draft window but approval is not required; (4) a **escalations/notifications inbox** is missing and should be added; (5) **unreachable contacts** should be surfaced at the contact level alongside departed contacts.

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
- [ ] **Engineering:** Add escalations / notifications inbox — dashboard-level feed showing flagged items and escalations across all stages; callable from any stage (Juliet feedback, 2026-06-24)
- [ ] **Engineering:** Show "unreachable" contact status at the contact level alongside departed contacts — after X attempts over Y days with no response, auto-classify as unreachable (Juliet feedback, 2026-06-24)
- [ ] **Evan / Dean:** Send "output stuff" (stage automation outputs showcase) to Juliet for use as placeholder slides in the design partner pitch deck (2026-06-24 standup)
- [ ] **Juliet:** Apply Pareto Agent color/design template to pitch deck slides using Claude (2026-06-24 standup)
- [ ] **Cooper:** Design a Pareto Agent logo (side project mentioned by Evan, 2026-06-24 standup)
- [ ] **Each team member (by 2026-06-24 evening standup):** hook your stage module into the adjacent stage — e.g., pressing "Approve Plan" in qualification auto-navigates to the next stage's view — so the demo has a narrative flow from stage 1 to 4 (2026-06-23 standup)
- [ ] **Evan:** add a time-frame dropdown (Q2/Q3/Q4/All) to the top-level overview dashboard before AJ demo; send calendar invite for the AJ demo conference-room gathering (2026-06-23 standup)
- [ ] **Team:** run through the full integrated demo narrative at the 2026-06-24 evening standup; give feedback on missing functionality (2026-06-23 standup)
- [x] ~~**AJ demo (2026-06-25):** Evan leads voiceover; one team member drives navigation; all team in one conference room. Demo narrative: account at monitoring → qualify → outreach (draft from signals) → response → proposal (Dean's deck) → buyer hub → admin view~~ — demo day arrived; format set
- [ ] **Team (by end of week 2026-06-25):** Pull LeanData bottom 200 accounts filtered by rep ownership — Cooper to provide the two rep names; review data dictionary fields to determine what to pull (2026-06-25 standup)
- [ ] **Outreach demo (before next demo):** Improve to show champion journey / contact-sequencing UI with configurable follow-up timers — no ZoomInfo integration needed for demo; focus on the UI path (2026-06-25 standup)
- [ ] **Cooper (outreach module):** Consolidate settings — combine current tabs 1, 2, 3 into a single settings icon (2026-06-25 standup)
- [ ] **Cooper:** Write script for each team member to pull LeanData data onto their local machine; data must NOT be stored on GitHub (2026-06-25 standup)
- [ ] **Team:** Build LLM evals for outreach email quality — judgment LLM assesses generated email output; analogous to a doctest (2026-06-25 standup)
- [ ] Ask Claude to (a) assess which codebase architecture is better, (b) generate a product architecture diagram as an artifact, (c) count lines of code per dashboard (2026-06-23 standup)
- [ ] **Cooper:** create the canonical fake-company JSON corpus (~100–200 companies, each <$10k) and send to the team — still open from 2026-06-22
- [ ] Pull customer contracts in up front — required for the buyer-engagement module to work, and contracts double as renewal signals
- [x] ~~Evan: set up a call with the LeanData (LD) team who built a data dictionary~~ — LeanData has already sent their company-specific data dictionary to the team (2026-06-25 standup)
- [ ] (Tentative) Weekend standups: ~once/day, ~30 min, around 1pm, opt-in — proposed by Evan 2026-06-22
- [ ] Julia + Evan: value proposition deck targeting AM leaders — due week of 2026-06-23
- [ ] MCP integration: Cooper + Aaron working on real CRM data connection — deferred until module deliverables are stable
- [x] ~~Team: 1:1s with Evan early week of 2026-06-23 to align on AJ demo plan~~ — at least Cooper's 1:1 with Evan happened by 2026-06-22 (referenced in standup)
- [ ] ~~Parth: scope down to champion agent + language agent only~~ — superseded 2026-06-22: Evan proposed Parth take the unified dashboard (top-level + per-stage) piece; language/voice agent remains active
- [x] ~~Dean + Aaron: start the parallel clean-sheet combined dashboard~~ — superseded 2026-06-23: team went with Cooper's "parents" architecture as the primary codebase; Aaron's parallel build was a valuable prototype but not the path forward
- [ ] **Unassigned:** Rename "Out of cycle" to "Off cycle" in the dashboard (June 24 evening standup)
- [ ] **Parth:** Configure 200 demo accounts in JSON with hardcoded "stories" — binary blocked/not-blocked per stage, so the date slider demonstrates pipeline movement (June 24 evening standup)
- [ ] **Aaron:** Implement global filter across entire dashboard website — selected period (e.g. Q3 2026) applies to all views simultaneously (June 24 evening standup)
- [ ] **Aaron:** Update account data to reflect only 4 quarters of 2026, not multi-year (June 24 evening standup)
- [ ] **Dean:** Work on pricing engine in a separate local environment or new folder — would break the demo environment for 1-2 days if done in the main repo (June 25 evening standup)
- [ ] **Dean:** Think through product architecture — shared components, data flow between stages, how real LeanData data will flow through each module (June 25 evening standup)
- [ ] **Aaron:** Build standup scrum board displaying team daily tasks; link to Dropbox transcript folder for eventual automation (June 25 evening standup)
- [ ] **Cooper:** Standardize transcript file naming and folder structure in Dropbox (date-based names, morning/evening subfolders) (June 25 evening standup)
- [x] ~~**Cooper + Evan:** June 26 1:1 to review LeanData email data metadata and determine categorization strategy before ingestion~~ — held 2026-06-26 (see Decision Log)
- [ ] **Cooper:** Write down email-corpus segmentation theories (group-by dimensions) for Evan to validate; group the pulled emails by account in pandas as a first pass (2026-06-26 1:1)
- [ ] **Cooper:** Tie account names to each pulled email — account name appears to be missing from the export and is needed to link emails to accounts/qualifications (2026-06-26 1:1)

## Decision Log
### 2026-06-26 — Cooper × Evan 1:1 (outreach email-corpus strategy)
- **Decision:** Before generating outreach emails, validate and segment the pulled LeanData email data rather than feeding it to the LLM raw. Sequence: (1) understand the data structure — columns, and how emails link to accounts/contacts (account name must be tied to each email; it appears missing from the current export); (2) assess data quality and trim to the high-value subset ("garbage in → garbage out"); (3) segment, then for each segment gather its emails, measure cluster consistency, and only then have Claude derive a canonical/template email per scenario.
- **Segmentation dimensions:** account ARR size (a $5k account behaves differently from a $40k one); qualification type (upsell/downsell — supplied by Aaron's qualification module); renewal status (in-process vs closed-won/closed-lost, the latter usable as labeled training data); recipient/contact; and time-series (gap between 1st/2nd/3rd email and when to move to the next contact — feeds the champion-finder). Assemble into a decision tree (e.g. downsell below an ARR threshold → a specific template).
- **Interim:** use basic/placeholder qualifications to stress-test segmentation until Aaron's real qualification output is available; group emails by account in pandas first. Champion-finder may end up owned alongside this work.
- **Rationale:** Customers want emails in their own voice, so templates must be derived from real, well-understood, consistent email clusters — not generated from scratch. Cleaning and segmenting first prevents training on noise. Extends the 2026-06-25 outreach-email-generation decision (analyze existing emails → scenario corpus → reverse tone classification).

### 2026-06-25 — Standup
- **Decision:** Use AJ's LeanData accounts as the training corpus for outreach email generation.
- **Rationale:** AJ's accounts are the first real-data test case; emails trained on his book of business will surface what the modules need to prove before going live.

### 2026-06-25 — Standup
- **Decision:** Gate to go live = must prove qualification AND outreach modules work; currently still proof of concept. No fixed timeline.
- **Rationale:** Going live depends on demonstrating these two modules work correctly rather than on a fixed date.

### 2026-06-25 — Standup
- **Decision:** Qualification is rule-based initially; AJ will dictate the rules because he knows the accounts. Focus is on upsell opportunities.
- **Rationale:** Starting with simple, human-defined rules lets the team prove the qualification loop works before adding ML-derived complexity. AJ will refine the edges once the team's classification feels right.

### 2026-06-25 — Standup
- **Decision:** Outreach email generation approach (Cooper's design): (1) analyze customer's existing emails and generate a scenario-based email corpus; (2) reverse: use LLM to classify the tone of the generated email; (3) use tone classification to *tweak* the email, not to generate it. This inverts the common "tone sliders → LLM generates" approach.
- **Rationale:** Customers want emails in their own tone and voice — starting from their existing emails is the only way to achieve that. The reverse approach generates from real data first, then makes small adjustments based on a tone scale.

### 2026-06-25 — Standup
- **Decision:** LeanData data to be pulled locally via script; NOT stored on GitHub. Cooper will write a script each team member can run to pull data onto their own machine.
- **Rationale:** Customer data should not live in the shared GitHub repo. Local storage restricts access to physical possession of the laptop.

### 2026-06-25 — Standup
- **Decision:** Outreach contact sequencing is rule-based: send to first account contact → if no response after 1 week, send follow-up → after ~3 weeks MIA, escalate to find alternate contact. Every account has ~3 contacts. For demo purposes, only need a UI showing this journey with configurable timers — no ZoomInfo integration yet.
- **Rationale:** AJ's biggest fear is a contact going MIA for 20–30 days with no structured follow-up. Rule-based timers are more consistent than relying on AMs to manually remember. The agent is more reliable than a human who gets distracted.

### 2026-06-25 — Stand up (evening, post-AJ-demo)
- **Decision:** Current prototype = front-end UI validation tool with synthetic data; real LeanData data integration will require a separate rebuild with different module architecture. The demo environment will remain intact for external demos.
- **Rationale:** Evan: "What we just built was a front-end UI prototype to validate — is this the type of functionality someone wants with phony data?" Mixing real data into the prototype creates structural conflicts (different data models, security constraints, pricing engine complexity). Cleaner to build production modules fresh with the correct architecture than to retrofit the prototype.

### 2026-06-25 — Stand up (evening, post-AJ-demo)
- **Decision:** Phase 2 sequence: ~1-2 weeks to understand LeanData data → qualification running on real data (AJ can interact) → outreach email drafts (~1 week later) → proposal → buyer engagement (needs security architecture guidance).
- **Rationale:** Staged approach lets AJ interact with each phase incrementally, building confidence. Firmographic analysis (distribution by Q, avg deal size, unique contacts) comes first — Evan: "What are we trying to categorize?" before running qualification.

### 2026-06-24 — Dashboard Optimization (13:32 PDT)
- **Decision:** Establish an information hierarchy standard for all stage pages: **"process first, status second."** Top of each stage view = process stages (e.g. unapproved deals, drafted-but-not-sent emails); secondary section = outcome/status stages (e.g. unreachable accounts, engaged accounts).
- **Rationale:** Existing layout was inconsistent — Qualification showed outcome stages (approved/not approved) while Outreach showed process stages (not started/draft/sent/waiting). Normalizing all stage views to the same structure makes the product predictable and legible across all modules.

### 2026-06-24 — Dashboard Optimization (13:32 PDT)
- **Decision:** Remove redundant high-level metrics (forecasted ARR, account size) from individual stage sub-pages. Remove "Overview" header from top of main dashboard. Format GDR in brackets. Standardize fonts across all dashboard pages (currently ~5 font variants) and standardize plot/box layout schemes to be consistent across all views.
- **Rationale:** These metrics already appear in the top-level dashboard superstructure; showing them again on every sub-page adds visual noise. The "Overview" label is redundant — the page is self-evidently an overview. Visual inconsistency (multiple fonts, inconsistent chart designs) makes the product feel unfinished.

### 2026-06-24 — Stand up (evening, pre-AJ-demo)
- **Decision:** Demo data approach: hardcode 200 accounts in a JSON file with a "story" — binary flags for blocked/not-blocked at each stage, with stage progression determined by date offset. No complex real-time agent communication between sub-modules needed for the demo.
- **Rationale:** The date slider already causes deals to move between stages based on time logic. Adding a one-bit "blocked at this stage" flag per account produces realistic pipeline spread without requiring actual inter-agent messaging — fast to implement and sufficient to demonstrate the product.

### 2026-06-24 — Stand up (evening, pre-AJ-demo)
- **Decision:** Code freeze: no new code pushes on the morning of the AJ demo. Wording/UI changes only; no structural changes.
- **Rationale:** Last-minute structural changes risk breaking the entire dashboard right before the demo. Small visual tweaks are acceptable; new features create merge conflicts and instability.

### 2026-06-24 — Product Demo / Strategy Session (Juliet Lo)
- **Decision:** Frame the product as **"telemetry"** rather than a "dashboard." Stages are populated automatically by agents, not by humans manually entering data into a CRM.
- **Rationale:** The dashboard UI risks looking like any other enterprise software. "Telemetry" captures that the system reflects real-time deal state driven by automation, not by human entry — which is the core differentiation.

### 2026-06-24 — Product Demo / Strategy Session (Juliet Lo)
- **Decision:** Demo strategy: walk through a **single deal progressing through all stages** to show automation outputs (qualification forecast, outreach emails, proposal deck, buyer hub cockpit telemetry). Do NOT use a time-slider / animation showing deals auto-progressing.
- **Rationale:** Juliet: customers are not ready for the system to run fully autonomously without oversight — they want to see what's happening and drill in. The automation is demonstrated by showing outputs generated without human input. AJ will likely say "show me one of my accounts" — a concrete single-deal walkthrough handles this naturally.

### 2026-06-24 — Product Demo / Strategy Session (Juliet Lo)
- **Decision:** Clarified approval / auto-send flow: emails and proposals are drafted in advance of the send date and sent **automatically on a timeline** by default. The manager can review/edit during the draft window; approval is optional. Nothing requires a human to click "send."
- **Rationale:** Prevents demo confusion between "we're autonomous" and "you can approve before it goes." Managers who want to review everything can; after 5–10 cycles they'll let it run. The draft window gives visibility without requiring a gatekeeper.

### 2026-06-24 — Strategy Session (Juliet Lo)
- **Decision:** Design partnership Phase 1 goal = **validate the core product** (are the stages right? outputs look right? is the dashboard right?) — NOT tailored implementation per customer.
- **Rationale:** Juliet: tailoring to each customer during Phase 1 changes the focus from product validation to implementation, meaning the team won't get generalizable feedback on usability and functionality. The product should work for all customers, not be custom-built each time.

### 2026-06-24 — Strategy Session (Juliet Lo)
- **Decision:** Pilot timeline should be at least **12 weeks (one quarter)**, not 8 weeks.
- **Rationale:** Renewal cycles are 120+ days. An 8-week pilot doesn't cover a full renewal cycle, so the team can't measure outcomes. One quarter gives a full cycle to validate end-to-end.

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
### 2026-06-17 — Morning Standup (research review + Juliet feedback)
- **Decision:** Keep v1 simple — get client buy-in on a basic model before adding edge cases. Complexity introduced too early creates too many failure points.
- **Rationale:** Juliet: a 7-step process with 5% variance per step compounds into an unworkable output. Prove the pipeline works end-to-end before optimizing individual modules.

### 2026-06-17 — Morning Standup (research review + Juliet feedback)
- **Decision:** Work within seller systems first — don't try to change how renewals work; make it easy for sellers to do things their way.
- **Rationale:** Evan, citing a call with Rol at Guard Square: radical pricing/usage transparency → high NRR and a small renewals team. Worth keeping as a long-term direction signal; not something to impose on day one.

### 2026-06-17 — Morning Standup (research review + Juliet feedback)
- **Decision:** "High sell potential" signal from the qualification module is a **binary flag** passed downstream — not a hard price recommendation. Pricing logic lives in the proposal module.
- **Rationale:** Keeps module scope clean; qualification signals the opportunity, proposal owns the pricing.

### 2026-06-17 — Morning Standup (research review + Juliet feedback)
- **Decision:** Buyer portal ROI calculator: buyer inputs (headcount, usage assumptions, etc.) are configurable; proposed pricing is fixed. No self-serve pricing exploration.
- **Rationale:** Buyers need to stress-test the value story; pricing decisions remain the seller's domain.

### 2026-06-18 — Stand up (evening, initial prototype review)
- **Decision:** Demo flow: present the generated PowerPoint output first, then walk through the block system and customization logic.
- **Rationale:** Showing the polished output creates impact and frames the "how" as a feature, not overhead. Explaining blocks first risks losing the audience before they see the value.

### 2026-06-18 — Stand up (evening, initial prototype review)
- **Decision:** Buyer hub product terminology: use "products" or "SKUs" (what the client is using/buying), not "utilization."
- **Rationale:** "Utilization" is vague; "products/SKUs" maps directly to what buyers recognize and care about renewing.

### 2026-06-18 — Stand up (evening, initial prototype review)
- **Decision:** Dashboard UI layout: move input controls (rationale, signals) to the main view; shift supplementary content/info to the sidebar. Centralizes user control.
- **Rationale:** Users interact with inputs primarily; putting them front and center reduces friction and clarifies the workflow.

### 2026-06-16 — Morning Standup
- **Decision:** Assign pipeline modules: Aaron → Qualification, Parth → Outreach, Dean → Proposal, Cooper → Buyer Evaluation. Negotiation stage excluded from scope.
- **Rationale:** Each team member owns one renewal stage end-to-end. Negotiation excluded — too many edge cases for v1.

### 2026-06-16 — Morning Standup
- **Decision:** Use Replit for fast prototyping; use Claude Code for spec writing and the real build. The two are separate environments.
- **Rationale:** Replit spins up a live site + database quickly but is hard to redirect once set on an approach; Claude Code is easier to iterate and change direction in, and feeds into GitHub.

## Notes
- **ICP pitch framing (Juliet, 2026-06-12 onboarding):** Juliet's opening pitch hook for the renewals long-tail problem: "5–10 extra points of growth in your renewal space without hiring extra people." Target in that session: B2B SaaS $30M+ ARR (the June 19 standup later settled on $10M+ ARR as the floor; $30M is characterized as where the problem "starts to become painful" — both figures are attributed to their respective sources, not treated as a settled change). Three GTM entry paths: (a) cover untouched accounts; (b) A/B pilot vs. human reps; (c) backfill churned rep headcount. Three-step agent maturity model: (1) foundational standards; (2) clone the top rep; (3) continuous self-improvement.
- **Buyer hub design decisions (2026-06-19 1:1 design review; Gemini single-speaker diarization — attribution unreliable):** Key decisions from the post-Scott-review design session: single scrollable account list sorted by days to renewal; per-row engagement level (not / somewhat / very engaged); aggregate summary hidden on account drill-down; "Contracts" expanded to "Documents" section (MSAs, product briefs, prior versions); highlights rather than redlines for change tracking; BookIt/Calendly-style scheduler within buyer interface; admin view tracks stakeholder engagement + doc-open status; section-level heat map (Crazy Egg style) discussed. See also: [Cooper Tenney](../people/cooper-tenney.md).
- **Post-AJ-demo (2026-06-25):** AJ demo occurred on June 25 with Evan leading voiceover and the team in one conference room. AJ may believe the demo environment is something he can access and play with — clarification needed at next interaction.
- **LeanData email data volume (Cooper, 2026-06-25 evening):** 2 reps have sent ~4,800 outgoing emails to ~360 accounts over 1 year (~17k total artifacts including calls and calendar invites). Data is structured (emails belong to specific accounts). Next step before ingestion: firmographic analysis — distribution by quarter, avg deal size, unique contacts.
- **Phase 2 architecture (Evan, 2026-06-25 evening):** Demo prototype will continue to be used for external demos with synthetic data. Real-data work per module will be done in separate local environments. Once modules are proven with real data, a production rebuild with the correct architecture will happen — qualification may transfer; outreach, pricing, and later stages need different structures built fresh.
- **Slide generation tool (Evan, 2026-06-18 evening standup):** Automated deck-generation tool using account signals (posture: flat/up-sell/down-sell, tenure, health metrics) to assemble slides from "blocks" — categorized slide types treated as puzzle pieces assembled per scenario. Inputs/rationale moved to main view, content preview to sidebar (UI layout decision, June 18 standup).
- **LeanData data pipeline (2026-06-25):** LeanData has already sent their company-specific data dictionary. Next step: identify the bottom 200 accounts by rep ownership (Cooper to provide two rep names), review the data dictionary to select the right fields, then pull data locally via script (not in GitHub). Goal: begin data analysis by start of next week.
- **Outreach email system — two tracks (2026-06-25):** (1) Demo track: improve outreach demo to show champion journey / contact-sequencing UI with configurable timers (immediate); (2) Product track: build actual email generation and contact sequencing product once LeanData data is available. First proof point with AJ: he likes the initial draft email.
- **Data dictionary is a live blocker for agents (Cooper, 2026-06-25):** One of the biggest stumbling blocks to agents going live right now is pulling the wrong data. Without a data dictionary, every agent re-derives field meanings. LeanData having one pre-built is a significant advantage. Cooper expects someone in the market will solve this problem broadly within ~3 months.
- **Demo multi-tab safety (ongoing):** Team continues to keep multiple browser tabs open during live demos as a fallback in case of internet/system issues; screenshots prepared as a further backup.
- **2026-06-24 morning session — demo + pitch deck review with Juliet Lo:** Evan walked Juliet through the Combined Dashboard (monitoring → qualification → outreach → proposal deck → buyer hub cockpit). The "cockpit" gives per-account visibility into who on the buying team engaged, when, and what they looked at — "a level of visibility that no one ever has." Juliet proposed a **three-layer demo framework**: (1) renewals leader dashboard overview (book-of-business funnel, stage drill-down); (2) single-deal walkthrough showing automation outputs; (3) RevOps configuration layer (rules engine, signal changes) — only surface layer 3 if the audience includes RevOps/forward-deployed engineers. Cooper asked (via text chat, relayed by Evan) how to best demonstrate the automation side; Juliet answered: show the outputs themselves (emails, decks, buyer hub), not an animation. Evan and Juliet discussed staged value delivery during a design partnership: week 1 = qualification outputs for all accounts; week 2 = outreach templates drafted; week 3 = proposal decks — so customers get tangible value at each step rather than waiting for the full system. Juliet also presented her pitch deck to the team and took feedback from Evan (add a "process you can stand by" punch line, incorporate "green churn," add a before/after or staged-timeline slide).
- **Business model (confirmed 2026-06-24):** Pareto gets paid on **closed deals** (outcomes-based, not on number of renewals handled). The headline metric on the dashboard is deals Pareto actually closed. Dashboard covers only Pareto's assigned book of business — but the long-term vision is expansion until the CRM is no longer needed.
- **Auditability parallel (Evan, 2026-06-24):** Auditability (what email was sent, why, at what decision point) became one of Lean Data's defining features because teams needed to reconstruct what happened when deals went wrong. The draft history and auto-send audit trail in this system should serve the same role — and will be how teams discover and fix edge cases over time ("automate → discover edge case → fix → next time you don't have to worry about it").
- **Context-as-moat (Evan, 2026-06-24):** The differentiator vs. point solutions is having context across all stages in one system. Competitors automating individual stages actually degrade the sales rep (reps no longer do research, find contacts, etc. — they lose context). Pareto's system retains full context, making negotiation tractable — you know exactly how engaged the buyer is, what they've looked at, whether they've even opened the contract.
- **Renewals leader persona deepened (Juliet, 2026-06-24):** Risk-averse; motivated by respect from sales peers (new business gets the glory; renewals is often "thankless"). Company thinks renewals "should be scientific," making the renewals leader disproportionately blamed when deals fall apart. They can't answer exec questions in churn reviews because they have hundreds of accounts with no visibility into most of them. "Green churn" (Rachel's term): churn in deals that looked on track — the type that blindsides them and triggers the painful churn review. Distinct from churn caused by product never being adopted (not the renewals leader's fault).
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
- **Rol at Guard Square (Evan reference, 2026-06-17):** Evan described a call with Rol at Guard Square where radical pricing and usage transparency led to high NRR, minimal negotiation overhead, and a small renewals team. Cited as a long-term direction for where the product could lead customers — not a day-one requirement.
- **June 17 research review session (Granola notes; pre-Fireflies):** All four team members presented module research; Juliet Lo gave structured feedback on each. First substantive external feedback session on the module designs (before Fireflies was set up June 19 and before the June 24 dashboard demo). Per-module feedback detail is captured in each module owner's wiki page and in the June 17 Decision Log entries above.
- **Original module assignments (2026-06-16):** Aaron → Qualification, Parth → Outreach, Dean → Proposal, Cooper → Buyer Evaluation. Negotiation stage excluded from scope (too many edge cases for v1). These assignments are the origin of the current module ownership table above.

## Related Pages
- [Evan Liang](../people/evan-liang.md)
- [Aaron Rose](../people/aaron-rose.md)
- [Dean Liang](../people/dean-liang.md)
- [Parth Godarajesh](../people/parth-godarajesh.md)
- [Cooper Tenney](../people/cooper-tenney.md)
- [Juliet Lo](../people/juliet-lo.md)
- [Scott](../advisors/scott.md)
- [AJ](../advisors/aj.md)
