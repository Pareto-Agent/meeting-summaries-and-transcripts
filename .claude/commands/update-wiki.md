# Update Wiki from Transcripts

Fetch new transcripts from the Fireflies API and update the wiki.

## Steps

1. Read `wiki/log.md` to extract the list of already-processed Fireflies transcript IDs (look for lines like `fireflies-id: <id>`).

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

   h. Append a new entry to `wiki/log.md`:
      ```
      ## <YYYY-MM-DD> — <title>
      - fireflies-id: <id>
      - Pages updated: <comma-separated list>
      - Summary: <one sentence>
      ```

   i. Update `wiki/index.md` if any new pages were created.

5. Commit all changes:
   ```
   git add -A
   git commit -m "wiki: update from <meeting date> <meeting type>"
   git push origin main
   ```

6. Summarize what was updated.

## API key

Stored in `.claude/settings.local.json` as `FIREFLIES_API_KEY` (env var, not committed). Rotate at app.fireflies.ai if compromised.
