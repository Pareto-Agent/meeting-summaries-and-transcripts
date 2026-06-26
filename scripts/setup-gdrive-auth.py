#!/usr/bin/env python3
"""
One-time Google OAuth consent for the Gemini transcript fetcher.

Run ONCE from your Mac (needs a browser):

    python3 scripts/setup-gdrive-auth.py ~/Downloads/oauth_client.json

where oauth_client.json is the file you download from Google Cloud Console:
  Credentials -> Create credentials -> OAuth client ID -> Application type
  "Desktop app".

It opens a browser, you approve READ-ONLY Drive access, and the resulting
refresh token is written to ~/.gdrive-fetch.json (chmod 600, outside Dropbox/git).
After this, fetch-gemini-transcripts.py runs unattended from cron.

stdlib only -- no pip installs.
"""
import http.server
import json
import os
import sys
import threading
import urllib.parse
import urllib.request

SCOPE = "https://www.googleapis.com/auth/drive.readonly"
CRED_OUT = os.path.expanduser("~/.gdrive-fetch.json")
AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"

_code = {}


class _Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        _code["code"] = params.get("code", [None])[0]
        _code["error"] = params.get("error", [None])[0]
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Auth complete. Close this tab and return to the terminal.")

    def log_message(self, *a):
        pass


def load_client(path):
    d = json.load(open(path))
    d = d.get("installed") or d.get("web") or d
    return d["client_id"], d["client_secret"]


def main():
    if len(sys.argv) < 2:
        print("usage: python3 scripts/setup-gdrive-auth.py /path/to/oauth_client.json")
        return 1
    client_id, client_secret = load_client(sys.argv[1])

    # Loopback redirect on an ephemeral port (the supported flow for Desktop clients).
    srv = http.server.HTTPServer(("127.0.0.1", 0), _Handler)
    port = srv.server_address[1]
    redirect_uri = f"http://127.0.0.1:{port}/"

    auth = AUTH_URL + "?" + urllib.parse.urlencode({
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": SCOPE,
        "access_type": "offline",   # needed to receive a refresh_token
        "prompt": "consent",        # force a refresh_token even on re-consent
    })

    print("Opening your browser for Google consent...")
    print("If it does not open, paste this URL into a browser:\n")
    print(auth, "\n")
    try:
        import webbrowser
        threading.Thread(target=lambda: webbrowser.open(auth), daemon=True).start()
    except Exception:
        pass

    srv.handle_request()  # serve exactly the one redirect, then stop

    if _code.get("error"):
        print(f"Consent error: {_code['error']}")
        return 1
    code = _code.get("code")
    if not code:
        print("No authorization code received.")
        return 1

    data = urllib.parse.urlencode({
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }).encode()
    with urllib.request.urlopen(urllib.request.Request(TOKEN_URL, data=data, method="POST"),
                                timeout=60) as r:
        tok = json.loads(r.read())

    if "refresh_token" not in tok:
        print("No refresh_token returned. Revoke the prior grant at")
        print("  https://myaccount.google.com/permissions")
        print("then re-run. Raw response:", tok)
        return 1

    out = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": tok["refresh_token"],
    }
    with open(CRED_OUT, "w") as f:
        json.dump(out, f, indent=2)
    os.chmod(CRED_OUT, 0o600)
    print(f"\nSaved credentials to {CRED_OUT}")
    print("The fetcher is now live -- it will run on the next cron pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
