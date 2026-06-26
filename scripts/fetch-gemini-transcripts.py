#!/usr/bin/env python3
"""
Fetch Google Meet "Notes by Gemini" transcript Docs from Google Drive and drop
them into transcripts/ as plain-text files the /update-wiki pipeline consumes.

Why this exists: Fireflies auto-join/transcription is unreliable. Gemini notes
live in Google Drive as Google *Docs*, which show up in the Drive-for-Desktop
mount only as 177-byte .gdoc pointer stubs (not text) -- so a dumb file copy
can't bridge them. This exports each Doc as real text via the Drive API.

Auth: OAuth installed-app refresh token in ~/.gdrive-fetch.json, created once by
  setup-gdrive-auth.py. Read-only Drive scope (drive.readonly).

Cron-safe by design:
  - stdlib only (urllib) -- no pip deps to break in a minimal cron env
  - always exits 0; any error is logged but never blocks the hourly wiki run
  - idempotent: tracks fetched Drive file IDs in transcripts/.drive-fetch-state.json
"""
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

CRED_PATH = os.path.expanduser("~/.gdrive-fetch.json")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANSCRIPTS_DIR = os.path.normpath(os.path.join(HERE, "..", "transcripts"))
STATE_PATH = os.path.join(TRANSCRIPTS_DIR, ".drive-fetch-state.json")
LOOKBACK_DAYS = int(os.environ.get("GEMINI_FETCH_LOOKBACK_DAYS", "30"))
TOKEN_URL = "https://oauth2.googleapis.com/token"
DRIVE_FILES = "https://www.googleapis.com/drive/v3/files"
GDOC_MIME = "application/vnd.google-apps.document"


def log(m):
    print(f"[gemini-fetch] {m}", flush=True)


def http(method, url, data=None, headers=None):
    if isinstance(data, dict):
        data = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def load_creds():
    if not os.path.exists(CRED_PATH):
        return None
    try:
        c = json.load(open(CRED_PATH))
    except Exception as e:
        log(f"could not read {CRED_PATH}: {e}")
        return None
    return c if c.get("refresh_token") else None


def access_token(c):
    status, body = http("POST", TOKEN_URL, data={
        "client_id": c["client_id"],
        "client_secret": c["client_secret"],
        "refresh_token": c["refresh_token"],
        "grant_type": "refresh_token",
    })
    if status != 200:
        raise RuntimeError(f"token refresh failed {status}: {body[:300]!r}")
    return json.loads(body)["access_token"]


def load_state():
    if os.path.exists(STATE_PATH):
        try:
            return set(json.load(open(STATE_PATH)).get("fetched_ids", []))
        except Exception:
            return set()
    return set()


def save_state(ids):
    os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)
    json.dump({"fetched_ids": sorted(ids)}, open(STATE_PATH, "w"), indent=2)


def safe_name(name):
    return re.sub(r"[/\\:]+", "-", name).strip()[:120]


def list_docs(token):
    since = (datetime.datetime.now(datetime.timezone.utc)
             - datetime.timedelta(days=LOOKBACK_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")
    # Gemini saves both a "Notes by Gemini" doc (which contains the transcript)
    # and sometimes a separate "Transcript" doc. Match either.
    q = (f"mimeType='{GDOC_MIME}' and trashed=false and modifiedTime > '{since}' "
         "and (name contains 'Gemini' or name contains 'Transcript')")
    params = urllib.parse.urlencode({
        "q": q,
        "fields": "files(id,name,modifiedTime)",
        "orderBy": "modifiedTime desc",
        "pageSize": "100",
    })
    status, body = http("GET", f"{DRIVE_FILES}?{params}",
                        headers={"Authorization": f"Bearer {token}"})
    if status != 200:
        raise RuntimeError(f"list failed {status}: {body[:300]!r}")
    return json.loads(body).get("files", [])


def export_doc(token, file_id):
    params = urllib.parse.urlencode({"mimeType": "text/plain"})
    status, body = http("GET", f"{DRIVE_FILES}/{file_id}/export?{params}",
                        headers={"Authorization": f"Bearer {token}"})
    if status != 200:
        raise RuntimeError(f"export {file_id} failed {status}: {body[:200]!r}")
    return body.decode("utf-8", "replace")


def main():
    creds = load_creds()
    if not creds:
        log(f"no credentials at {CRED_PATH} yet -- run scripts/setup-gdrive-auth.py once. Skipping.")
        return 0
    try:
        token = access_token(creds)
    except Exception as e:
        log(f"auth error (non-fatal): {e}")
        return 0
    try:
        docs = list_docs(token)
    except Exception as e:
        log(f"list error (non-fatal): {e}")
        return 0

    state = load_state()
    new = 0
    for d in docs:
        if d["id"] in state:
            continue
        out = os.path.join(TRANSCRIPTS_DIR, safe_name(d["name"]) + ".txt")
        if os.path.exists(out):
            state.add(d["id"])  # already present from a manual drop; mark done
            continue
        try:
            text = export_doc(token, d["id"])
        except Exception as e:
            log(f"export error for {d['name']!r} (skipped): {e}")
            continue
        os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)
        with open(out, "w") as f:
            f.write(text)
        state.add(d["id"])
        new += 1
        # Gemini Docs are tabbed (Summary / Transcript). A text/plain export may
        # return only the first tab -- self-report so a summary-only export is
        # caught instead of silently shipping thin notes. Fix without re-consent
        # by switching extraction to the Docs API (documents.get?includeTabsContent),
        # which drive.readonly already authorizes.
        has_transcript = "transcript" in text.lower()
        flag = "" if (has_transcript and len(text) > 2000) else "  [!] looks summary-only — verify tab export"
        log(f"fetched: {os.path.basename(out)} ({len(text)} chars){flag}")

    save_state(state)
    log(f"done -- {new} new, {len(docs)} candidate(s) in last {LOOKBACK_DAYS}d.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
