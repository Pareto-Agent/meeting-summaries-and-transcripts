# Update Wiki from Transcripts

Process any new transcripts in the `transcripts/` folder and update the wiki.

## Steps

1. Read `wiki/log.md` to get the list of already-processed transcript filenames.

2. List all files in `transcripts/` (any `.txt` or `.md` file). Identify which have NOT yet been processed (filename not in `wiki/log.md`).

3. If there are no unprocessed transcripts, report "No new transcripts to process." and stop.

4. For each unprocessed transcript (oldest file date first):

   a. Read the full transcript.

   b. Identify the meeting type from content:
      - **Standup**: multiple participants each giving short updates, blockers, what they're working on
      - **1:1**: two participants in a check-in format
      - **Advisor demo**: includes an external advisor, product demo or feedback discussion

   c. Extract the meeting date from the transcript content (Tactiq includes it in the header). If not found, use the file's modification date.

   d. Identify all participants by name.

   e. Extract signal per the rules in `CLAUDE.md`.

   f. For each relevant wiki page (people, advisors, projects):
      - If the page doesn't exist, create it using the template in `CLAUDE.md`
      - If it exists, update it — do NOT duplicate existing content, only add new information
      - Set "Last updated" to the meeting date

   g. Append a new entry to `wiki/log.md`:
      ```
      ## <YYYY-MM-DD> — <filename>
      - Pages updated: <comma-separated list>
      - Summary: <one sentence>
      ```

   h. Update `wiki/index.md` if any new pages were created.

5. Commit all changes:
   ```
   git add -A
   git commit -m "wiki: update from <meeting date> <meeting type>"
   git push origin main
   ```

6. Summarize what was updated.

## How to add a transcript

After a meeting:
1. Open Tactiq → export transcript as `.txt`
2. Drag the file into the `transcripts/` folder
3. Run `/update-wiki` in Claude Code

No renaming needed — meeting type and date are inferred from content.
