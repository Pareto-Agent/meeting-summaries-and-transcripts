# Evan Liang
**Role:** Co-founder / CEO, Pareto Agent (standup leader, product strategy)
**Last updated:** 2026-06-23

## Current Focus
Leading product strategy and overall agent architecture. Drove the 2026-06-22 pivot to a single unified dashboard + centralized account page for the [Renewal Platform](../projects/renewal-platform.md). Coordinating external advisor calls and customer research.

## Open Tasks
- [ ] Lead AJ demo (2026-06-25): voiceover/narration while one team member drives navigation; all team in one conference room
- [ ] Add time-frame dropdown (Q2/Q3/Q4/All) to the top-level overview dashboard before AJ demo (2026-06-23 standup)
- [ ] Send calendar invite to full team for AJ demo conference-room session (2026-06-23 standup)
- [ ] Set up a call with the LeanData (LD) team about their data dictionary, as reference for the proposed data dictionary module (2026-06-22)
- [ ] Work with Julia on value proposition deck for AM Leader — due week of 2026-06-23
- [ ] Continue calibrating 6 micro-agents (language style, drafter, response agent, champion finder, ingestion, proposal)
- [ ] (Tentative) Set up a meeting with Jesse — hoping for Thursday next week (~2026-06-25)
- [ ] Find external people to evaluate whether the team is building things correctly; trial some sessions as demos instead of code reviews

## Notes
- Runs two standups per day (morning + afternoon); afternoon standup moving to 5:30pm
- Strategic decision: keep using dummy data for at least another week; don't stitch modules together until each module's deliverable is well-defined
- Product direction: **autonomous agent**, not a co-pilot — long-term goal is to replace AMs, not assist them
- ICP defined: companies with $10M+ ARR; also PE-backed companies
- Decision maker target: **CRO** (budget owner); end user: **AM Leader**
- Core value prop: concrete visibility into each step of the renewal process — making it measurable like a manufacturing floor
- Worked at a company where a CTO was impressed by a simplified version of their own complex flowchart
- **Mentorship session 2026-06-19** (group working session; led by Evan): leadership/operating philosophy —
  - Bureaucracy is a function of headcount, not process; once a company crosses a certain size the org "feeds itself" (middle management equates power with number of reports). Cites Google's heavy efforts to avoid bureaucracy post-IPO.
  - "Fake work" (term he attributes to Stewart Butterfield): activity that looks busy but doesn't move the business forward (e.g. months prepping a board deck, "meetings to prepare for a meeting"). Founders feel headcount as expense/runway; managers often don't.
  - Sees the team's AI-native working style as genuinely faster than how he worked before; thinks it will disrupt consulting/traditional roles.
- **Next-week goal:** maintain momentum and keep iterating fast, but start coordinating more — may change/innovate on processes to do so.
- **Availability:** told the team he's always reachable and will typically respond within 1–2 hours; wants to make sure no one is blocked.
- **2026-06-22 standup (evening):** Executed the first merge — stitched all four builds into one working Combined Dashboard ("DD"/"Daddy Dashboard"/"Frankenstein"); his agents (outreach, language, champion models) run live against the API, though the merged UI is ~35–40% there. Laid out the git-branch collaboration model (pull `main`, generate a diff to push individual work in, then decentralized commit/push with GitHub resolving conflicts; "I don't hold the master — it's in GitHub"). Cited an information-systems degree while diagramming the branch flow. Acknowledged a future break point where shared data would force a harder rework, and endorsed the parallel clean-sheet rebuild.
- **2026-06-23 Pitch Contest:** Organized and facilitated an internal pitch contest (30-sec elevator + 5-min sales pitch, order by spin wheel) for the full team including remote participants Juliet Lo and H. Fong. This is the "sales pitch instead of standup" day referenced in the 06-22 evening standup.
- **2026-06-23 standup (evening):** Reviewed Aaron's overnight rebuilt combined dashboard vs. Cooper's "parents" build. Team agreed to go with Cooper's architecture; Evan facilitated the decision. Laid out the AJ demo plan: Evan leads voiceover, one person drives, all in one conference room; tighter narrative flow (no bouncing). Read Juliet's pitch outline aloud to the team as the framing for how to talk to renewals leaders. Also relayed context on Lean Data org structure: Brian Burkett = CSO/CRO; AJ reports to Brian and manages commercial renewals (the skeptical end-user persona); Franco = Head of RevOps (tech advisor to CRO, not a direct report). Call with Franco + Parth happened earlier that day. Emphasized that the CRO won't want to see the product — he buys on ROI/headcount; AJ is the one who needs to be convinced at the product level.
- **2026-06-22 standup:** Pitched the unified dashboard vision (single dashboard across the book of business + centralized account page); proposed a cross-functional split (Parth on the dashboard piece, Cooper on the account page). Argued the agentic CRM needs far less manual input than Salesforce-style CRMs because automations move deals between stages. Held a stance (while calling it a "fair risk factor") that the product should not be designed assuming a human AM in the loop — the forward-deployed engineer is the human who onboards/tunes. Floated once-a-day weekend standups (~1pm, opt-in).
