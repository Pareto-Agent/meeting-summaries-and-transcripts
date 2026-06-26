# Update Wiki from Transcripts

Fetch new transcripts from the Fireflies API and update the wiki.

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

      Read the companion via the Read tool (it handles `.txt`, `.pdf`, and `.vtt`). Prefer a
      complete native transcript over a partial Fireflies pull. In the log entry record
      `source: fireflies+<gemini|zoom>-fallback`. If NO companion file exists, log the meeting
      as a stub (`Pages updated: none`, note "transcript unavailable") so it isn't reprocessed.

   b. Identify the meeting type from content:
      - **Standup**: multiple participants each giving short updates, blockers, what they're working on
      - **1:1**: two participants in a check-in format
      - **Advisor demo**: includes an external advisor, product demo or feedback discussion

   c. Use the `date` field from the API response as the meeting date (Unix timestamp → YYYY-MM-DD).

   d. Identify all participants from `participants` (flat list of email addresses).

   e. Extract signal per the rules in `CLAUDE.md`.

   f. Save the reconstructed transcript to `transcripts/<YYYY-MM-DD>-<slug>.txt` for archival (slug = lowercase title, spaces → hyphens, max 40 chars). If that path already exists for a *different* transcript (e.g. two meetings the same day share a title), add a disambiguating suffix (e.g. `-evening`, `-2`) — NEVER overwrite an existing transcript file.

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
    scan `transcripts/` for native transcript files — `*Notes by Gemini*`, `*- Transcript*`
    (`.txt`/`.pdf`), and `*.transcript.vtt` (Zoom) — whose meeting is NOT yet in `wiki/log.md`.
    Track these by filename (`gemini-file:` / `zoom-file:` lines), since they have no
    fireflies-id. These are real meetings Fireflies missed entirely (e.g. an ad-hoc call with no
    calendar invite, or a join the bot was never admitted to). Process each exactly like a
    Fireflies meeting (steps 4b–4i): derive the date from the filename (Zoom `GMT` prefix is UTC —
    convert to local), read content via the Read tool, extract signal, update wiki pages, and
    append a log entry with `source: gemini` or `source: zoom` and a `gemini-file:`/`zoom-file:`
    line naming the source file (no `fireflies-id`). This is what makes native transcripts a true
    fallback path rather than a manual rescue — a missed/empty Fireflies capture no longer means a
    lost meeting, as long as the native transcript file has landed in `transcripts/`.

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
