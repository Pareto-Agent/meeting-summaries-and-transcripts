# Update Wiki from Tactiq Transcripts

Fetch new meeting transcripts from Gmail (sent by Tactiq after each meeting) and update the wiki.

## How transcripts arrive

Tactiq is configured to auto-email the transcript to ctenney@paretoagent.ai after every meeting.
Emails come from Tactiq (search: `from:tactiq.io`) with the transcript in the body.

## Steps

1. Read `wiki/log.md` to get the list of already-processed email subjects/dates.

2. Search Gmail for Tactiq transcript emails:
   - Query: `from:tactiq.io` (or `subject:transcript from:tactiq` if needed)
   - Look for emails not yet recorded in `wiki/log.md`
   - If no new emails found, report "No new transcripts." and stop.

3. For each new email (oldest first):

   a. Fetch the full email body — this is the meeting transcript.

   b. Identify the meeting type from content:
      - **Standup**: multiple participants, each giving short status updates, blockers
      - **1:1**: exactly two participants in a check-in format
      - **Advisor demo**: includes an external advisor, product demo or feedback discussion

   c. Extract the meeting date from the email date header or transcript content.

   d. Identify all participants by name.

   e. Extract signal per the rules in `CLAUDE.md`.

   f. For each relevant wiki page (people, advisors, projects):
      - If the page doesn't exist, create it using the template in `CLAUDE.md`
      - If it exists, update it — do NOT duplicate existing content, only add new information
      - Set "Last updated" to the meeting date

   g. Save the raw transcript text to `transcripts/<YYYY-MM-DD>_<meeting-type>_<participants>.txt`
      (use the meeting date and type inferred from content — this is for archival only)

   h. Append a new entry to `wiki/log.md`:
      ```
      ## <YYYY-MM-DD> — <email subject>
      - Pages updated: <comma-separated list>
      - Summary: <one sentence>
      ```

   i. Update `wiki/index.md` if any new pages were created.

4. Commit all changes with message: `wiki: update from <meeting date> <meeting type>`

5. Summarize what was updated.

## Tactiq email setup (one-time)

In Tactiq settings, enable: **Integrations → Email → Send transcript to my email after each meeting**.
The email will go to ctenney@paretoagent.ai automatically after every call.
