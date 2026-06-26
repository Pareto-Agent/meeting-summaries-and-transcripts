# Update Wiki from Transcripts

Fetch new transcripts from the Fireflies API and update the wiki.

## Transcript archival convention (where processed transcripts live)

```
transcripts/
  morning/      standups starting before 12:00 local → YYYY-MM-DD-standup-morning.<source>.txt
  evening/      standups starting 12:00 or later     → YYYY-MM-DD-standup-evening.<source>.txt
  <root>        all NON-standups (1:1s, demos, etc.)  → YYYY-MM-DD-<slug>.<source>.txt
  _inbox/       raw auto-fetched native files awaiting processing (the Drive fetcher writes here)
  _superseded/  redundant duplicate sources, kept for provenance — never read for signal
```

- `<source>` ∈ `fireflies | gemini | zoom | granola`. **Omit** the `.<source>` tag when a
  meeting has only ONE source; add it only when 2+ sources exist for the same meeting.
- **slot**: `morning` if the meeting starts before 12:00 local, else `evening`.
- One meeting may have several files (one per source) sharing the same base name.
- Name collisions: append `-2`, `-3`.
- Always write archival files to this convention — never a flat ad-hoc name in root.

## Steps

1. Read `wiki/log.md` to extract what has already been processed:
   - Fireflies transcript IDs (lines like `fireflies-id: <id>`)
   - Native-fallback files already consumed (lines like `gemini-file: <filename>` or `zoom-file: <filename>`)
   so neither a Fireflies meeting nor a native-only (Gemini/Zoom) meeting is processed twice.

2. Fetch transcripts from the Fireflies GraphQL API:

   ```bash
   curl -s -X POST https://api.fireflies.ai/graphql \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $FIREFLIES_API_KEY" \
     -d '{"query": "{ transcripts { id title date duration organizer_email participants sentences { speaker_name raw_text } } }"}'
   ```

   Identify which transcripts have NOT yet been processed (ID not in `wiki/log.md`). Process oldest first (by `date`).

3. If there are no unprocessed transcripts, report "No new transcripts to process." and stop.

4. For each unprocessed transcript (oldest first):

   **Duplicate handling — be conservative.** A transcript is a duplicate ONLY when its actual content matches an already-processed one (e.g. the same meeting captured by two recorders). A shared title and calendar day are NOT sufficient — the same team can hold a morning and an evening standup on the same date. Before marking anything `[DUPLICATE]`, compare the API `date` timestamp (down to the time, not just the day) AND skim the reconstructed text against the candidate. When in doubt, process it as a real meeting — silently dropping a genuine meeting is far worse than a redundant entry. Only when you are confident it is a true duplicate, log it as `[DUPLICATE]` with `Pages updated: none` and skip archiving a second transcript.

   a. Reconstruct the full transcript text from `sentences[].speaker_name` + `sentences[].raw_text`.

      **Native fallback (when `sentences` is null or empty).** Fireflies sometimes joins a
      meeting (non-zero `duration`) but returns no transcript. When that happens, look in
      `transcripts/` for a native companion transcript of the SAME meeting and use it instead.
      Match by date — the date embedded in the companion filename must equal the meeting's API
      `date` — and, if several share a date, by the closest time. Recognized native sources:
      - **Google Meet** — files named `*Notes by Gemini*` or `*- Transcript*` (`.txt` or `.pdf`).
        Filename date is `YYYY_MM_DD` (manual downloads) or `YYYY-MM-DD` (auto-fetched
        from Drive — the fetcher names files after the Doc title). Treat `_` and `-` as
        equivalent date separators when matching. Fully speaker-attributed; the file header
        reads `Meeting records Transcript` when a transcript exists (vs `Recording`/notes-only).
      - **Zoom** — files named `*.transcript.vtt` (WebVTT). Filename date is the `GMTYYYYMMDD`
        prefix (this is UTC — convert to the local meeting day before matching). Parse the VTT:
        strip `WEBVTT`, cue numbers, and `HH:MM:SS.mmm --> ...` timing lines; keep the spoken
        text (Zoom VTT lines are often `Speaker Name: text`).

      Read the companion via the Read tool (it handles `.txt`, `.pdf`, and `.vtt`). In the log
      entry record `source: fireflies+<gemini|zoom>-fallback`. If NO companion file exists, log
      the meeting as a stub (`Pages updated: none`, note "transcript unavailable") so it isn't
      reprocessed.

      **Choosing which source to extract signal from (when a meeting has BOTH a Fireflies and a
      native transcript).** A blind quality test (2026-06-26) found neither tool is reliably
      better — they fail differently, by meeting type:
      - **Diarization (who said what):** Gemini diarizes by Meet audio-stream, so it is excellent
        for **remote** meetings (each person on their own connection) but collapses every line
        onto the host/organizer for **in-room** meetings (one shared mic). Fireflies diarizes
        acoustically, so it *sometimes* recovers in-room speakers but is inconsistent.
      - **Rule of thumb:** pick the transcript that actually shows **multiple distinct speakers**
        for attribution — check each source's speaker labels and prefer the one that isn't
        collapsed to a single name. For a **remote** meeting that's usually **Gemini**; for an
        **in-room** standup it's often **Fireflies** (when Gemini shows only the host). If BOTH
        collapse to one speaker, say so in the entry's Caveat and keep attribution thin /
        project-level. Cross-check proper nouns (names, companies) between the two — Gemini
        occasionally garbles them, Fireflies fragments and sometimes cuts off early.
      - Gemini files also bundle an AI summary + decisions + action-items; use those to
        corroborate extracted signal, but verify against the raw transcript before relying on them.

   b. Identify the meeting type from content:
      - **Standup**: multiple participants each giving short updates, blockers, what they're working on
      - **1:1**: two participants in a check-in format
      - **Advisor demo**: includes an external advisor, product demo or feedback discussion

   c. Use the `date` field from the API response as the meeting date (Unix timestamp → YYYY-MM-DD).

   d. Identify all participants from `participants` (flat list of email addresses).

   e. Extract signal per the rules in `CLAUDE.md`.

   f. Save the reconstructed transcript for archival following the **Transcript archival
      convention** above: standups → `morning/`|`evening/` as `YYYY-MM-DD-standup-<slot>.fireflies.txt`
      (slot by start time); non-standups → root as `YYYY-MM-DD-<slug>.fireflies.txt` (slug =
      lowercase title, spaces → hyphens, max 40 chars). Drop the `.fireflies` tag if this is the
      meeting's only source. NEVER overwrite an existing transcript file — add `-2` on collision.

   g. For each relevant wiki page (people, advisors, projects):
      - If the page doesn't exist, create it using the template in `CLAUDE.md`
      - If it exists, update it — do NOT duplicate existing content, only add new information
      - Set "Last updated" to the meeting date

   h. Append a new entry to `wiki/log.md`. Include the line that identifies the source so it is
      never reprocessed — a `fireflies-id:` for API meetings, a `gemini-file:`/`zoom-file:` for
      native-only meetings — plus a `source:` tag:
      ```
      ## <YYYY-MM-DD> — <title>
      - fireflies-id: <id>          # OR: gemini-file: <name> / zoom-file: <name>
      - source: <fireflies | fireflies+gemini-fallback | fireflies+zoom-fallback | gemini | zoom>
      - Pages updated: <comma-separated list>
      - Summary: <one sentence>
      ```

   i. Update `wiki/index.md` if any new pages were created.

4B. **Native-only meetings (Fireflies never captured them).** After the Fireflies list is done,
    scan for native transcript files the Fireflies pass didn't already consume — look in
    `transcripts/_inbox/` (where the Drive fetcher drops raw files), in `transcripts/` root, and
    RECURSIVELY in `morning/`/`evening/`. Recognize `*Notes by Gemini*`, `*- Transcript*`,
    `*Gemini Export*` (`.txt`/`.pdf`) and `*.transcript.vtt` (Zoom). For each whose meeting is
    NOT yet in `wiki/log.md`:
      i.  **Canonicalize the file first** — rename/move it to its proper home per the Transcript
          archival convention (standup → `morning/`|`evening/`; else root; with the right
          `.<source>` tag). A raw `_inbox/` file must end up at its canonical path, not stay in
          `_inbox/`. If a canonical file for that meeting+source already exists, this is a
          duplicate source — move it to `_superseded/` instead of overwriting.
      ii. Then process exactly like a Fireflies meeting (steps 4b–4i): derive the date (Zoom
          `GMT` prefix is UTC — convert to local) and slot, read content via the Read tool,
          extract signal, update wiki pages, and append a log entry with `source: gemini|zoom`
          plus a `gemini-file:`/`zoom-file:` line naming the **canonical** path (no `fireflies-id`).
    Apply the date-based dedup rule below so already-covered meetings aren't reprocessed. This is
    what makes native transcripts a true fallback — a missed/empty Fireflies capture no longer
    means a lost meeting, as long as the native file has landed in `transcripts/` (or `_inbox/`).

    **Dedup against already-covered meetings (critical — the auto-fetcher pulls a backlog).**
    A native file is "not yet processed" only if no log entry covers its MEETING — not merely if
    its filename is new. The same meeting can arrive as a manual `YYYY_MM_DD` drop, an auto-fetched
    `YYYY-MM-DD` Doc, AND a Fireflies capture. Before processing a native-only file, find any
    log entry with the SAME date (treat `_`/`-` as equal) and a compatible title/time, then:
      - **Already covered with real content** (the entry has `Pages updated: <pages>`): do NOT
        re-extract or duplicate wiki content. Just append a `gemini-file:`/`zoom-file:` line to
        that existing entry recording this file as an additional archival source, and move on.
      - **Existing entry is a stub** (`Pages updated: none`, "transcript unavailable"): the native
        file is exactly the missing content — process it now and UPDATE that entry in place
        (set its source and pages), rather than adding a second entry for the same meeting.
      - **No matching entry**: it's a genuinely new meeting — process it fresh (4b–4i).
    When unsure whether two are the same meeting, compare the reconstructed text, not just the
    title. Prefer one entry per real meeting with multiple source lines over duplicate entries.

5. Commit all changes locally (do NOT push):
   ```
   git add -A
   git commit -m "wiki: update from <meeting date> <meeting type>"
   ```
   The commit is a local-only rollback safety net. Sync to the team happens via
   Dropbox, not GitHub — there is intentionally no `git push` step. Do not push.

6. Summarize what was updated.

## API key

Stored in `.claude/settings.local.json` as `FIREFLIES_API_KEY` (env var, not committed). Rotate at app.fireflies.ai if compromised.
