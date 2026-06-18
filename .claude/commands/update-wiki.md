# Update Wiki from Transcripts

Process any unprocessed meeting transcripts and update the wiki accordingly.

## Steps

1. Read `wiki/log.md` to get the list of already-processed transcript filenames.

2. List all files in `transcripts/`. Identify which ones have NOT yet been processed (i.e., their filename does not appear in `wiki/log.md`).

3. If there are no unprocessed transcripts, report "No new transcripts to process." and stop.

4. For each unprocessed transcript (process oldest first by filename date):

   a. Read the full transcript.

   b. Identify the meeting type:
      - **Standup**: daily/weekly team sync, multiple participants, short updates
      - **1:1**: two participants, check-in format
      - **Advisor demo**: includes an external advisor, product demo or feedback session

   c. Identify all participants by name.

   d. Extract signal per the rules in `CLAUDE.md`.

   e. For each relevant wiki page (people, advisors, projects):
      - If the page doesn't exist, create it using the template in `CLAUDE.md`
      - If the page exists, update it — do NOT duplicate existing content, only add new information
      - Use today's date for "Last updated"

   f. Append a new entry to `wiki/log.md`:
      ```
      ## <YYYY-MM-DD> — <transcript filename>
      - Pages updated: <comma-separated list>
      - Summary: <one sentence describing the meeting>
      ```

   g. Update `wiki/index.md` if any new pages were created (add links under the appropriate section).

5. After processing all transcripts, summarize what was updated.

## Transcript Filename Convention

Name transcripts as: `YYYY-MM-DD_<meeting-type>_<participants-or-topic>.txt`

Examples:
- `2026-06-18_standup_team.txt`
- `2026-06-18_1on1_cooper-alex.txt`
- `2026-06-18_advisor-demo_john-smith.txt`

Tactiq exports can be renamed to this format before dropping into `transcripts/`.
