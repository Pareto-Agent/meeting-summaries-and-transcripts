# Gemini transcript auto-fetcher

Pulls Google Meet **"Notes by Gemini"** Docs from Google Drive into `../transcripts/`
as plain text, so the `/update-wiki` pipeline can use them when Fireflies fails to
capture a meeting. Runs automatically from the hourly cron (wired into
`~/update-wiki-cron.sh`, before the wiki run).

- `fetch-gemini-transcripts.py` — the fetcher (cron runs this; stdlib only).
- `setup-gdrive-auth.py` — one-time OAuth consent (you run this once).

Credentials live in `~/.gdrive-fetch.json` (chmod 600, **outside** Dropbox/git).
Until that file exists the fetcher no-ops cleanly — it never breaks the wiki run.

---

## One-time setup (~10 min, do once)

### 1. Create a Google Cloud project + OAuth client
1. Go to <https://console.cloud.google.com/> → create a project (e.g. `meeting-wiki`).
2. **Enable the Drive API**: APIs & Services → Library → search "Google Drive API" → Enable.
3. **OAuth consent screen**: APIs & Services → OAuth consent screen.
   - **User type = Internal** ← important. Internal (Workspace) avoids app
     verification *and* avoids the 7-day refresh-token expiry that "External +
     Testing" apps suffer. (`ctenney@paretoagent.ai` is a Workspace account, so
     Internal is available.)
   - App name: anything. Save.
4. **Create credentials**: APIs & Services → Credentials → Create credentials →
   OAuth client ID → **Application type: Desktop app** → Create → **Download JSON**
   (e.g. to `~/Downloads/oauth_client.json`).

### 2. Run the consent flow once
```bash
cd "/Users/coopertenney/Paretoagent Dropbox/Paretoagent Team Folder/Meeting Notes"
python3 scripts/setup-gdrive-auth.py ~/Downloads/oauth_client.json
```
A browser opens → approve **read-only** Drive access. The refresh token is saved to
`~/.gdrive-fetch.json`. Done — the next hourly cron pass starts fetching.

### 3. Verify the first real run (do NOT skip)
```bash
python3 scripts/fetch-gemini-transcripts.py
```
This is the gate. Confirm:
- **`>0 candidates`** — if it says `0 candidate(s)`, the docs aren't reachable from
  Cooper's account and we need the organizer's Drive (domain-wide delegation) instead.
- **No `[!] looks summary-only` flags.** Gemini Docs are tabbed (Summary / Transcript);
  a `text/plain` export can return only the summary tab. If you see that flag, tell me —
  I'll switch extraction to the **Google Docs API** (`documents.get?includeTabsContent`),
  which the same `drive.readonly` scope already authorizes (no re-consent needed).
- **Open one fetched `transcripts/*.txt`** and confirm it contains the actual back-and-forth
  transcript, not just the 3-paragraph summary.

(The Gemini *email* itself — `from:gemini-notes@google.com` — contains the Summary +
action-items-with-owners but **not** the transcript; it's a clean structured fallback if
the Doc path ever proves fussy.)

---

## Notes & limits
- **Scope**: `drive.readonly` only — the script can list and export, nothing else.
- **What it matches**: Google Docs whose name contains `Gemini` or `Transcript`,
  modified in the last `GEMINI_FETCH_LOOKBACK_DAYS` (default 30). Override per-run:
  `GEMINI_FETCH_LOOKBACK_DAYS=90 python3 scripts/fetch-gemini-transcripts.py`.
- **Idempotent**: fetched Drive file IDs are tracked in
  `../transcripts/.drive-fetch-state.json` (gitignored). A doc already present in
  `transcripts/` (e.g. a manual drop) is marked done, not duplicated.
- **Organizer-only**: Gemini Docs save to the *meeting organizer's* Drive. This
  fetches from `ctenney@paretoagent.ai`'s Drive — meetings organized by teammates
  won't appear here without Workspace domain-wide delegation (a heavier setup).
- **Zoom**: not covered by this script. Zoom `.vtt` transcripts need the Zoom API;
  the `/update-wiki` skill already consumes Zoom VTTs dropped into `transcripts/`.
- **Rotate/revoke**: delete `~/.gdrive-fetch.json` and re-run setup, or revoke at
  <https://myaccount.google.com/permissions>.
```
