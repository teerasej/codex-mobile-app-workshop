"""Check a running Service Desk Lite lab API. Creates one synthetic request.
Run interactively: python scripts/check_api.py --base-url http://127.0.0.1:8000
This is a contract checker, not an API implementation or a production audit.
"""
import argparse
import getpass
import json
import secrets
import sys
import uuid
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen

EXPECTED_FIELDS = {
    "id", "title", "description", "category", "status", "owner_username", "created_at"
}

def call(base, method, path, payload=None, token=None, form=False):
    headers = {"Accept": "application/json"}
    data = None
    if payload is not None:
        data = (urlencode(payload).encode("utf-8") if form
                else json.dumps(payload, ensure_ascii=False).encode("utf-8"))
        headers["Content-Type"] = ("application/x-www-form-urlencoded" if form
                                   else "application/json")
    if token:
        headers["Authorization"] = "Bearer " + token
    request = Request(base + path, data=data, headers=headers, method=method)
    try:
        with urlopen(request, timeout=30) as response:
            return response.status, json.load(response)
    except HTTPError as error:
        try:
            body = json.loads(error.read().decode("utf-8"))
        except (ValueError, UnicodeError):
            body = None
        return error.code, body

def expect(label, result, status):
    actual, body = result
    if actual != status:
        # Do not print bodies, request headers, passwords or access tokens.
        raise AssertionError(f"{label}: expected HTTP {status}, got {actual}")
    print(f"PASS {label}: HTTP {status}")
    return body

def valid_request(body, owner):
    assert isinstance(body, dict), "Response is not an object"
    assert EXPECTED_FIELDS <= set(body), "Response is missing required fields"
    assert body["owner_username"] == owner, "Response owner is wrong"
    assert body["category"] in ("it", "facility", "equipment")
    assert body["status"] in ("new", "in_progress", "done")
    assert 5 <= len(body["title"].strip()) <= 100
    assert 10 <= len(body["description"].strip()) <= 500
    uuid.UUID(body["id"])
    assert "password" not in body and "password_hash" not in body

def login(base, user, password):
    body = expect(f"login {user}", call(base, "POST", "/auth/token",
                 {"username": user, "password": password}, form=True), 200)
    assert body.get("token_type", "").lower() == "bearer", "Missing bearer token type"
    token = body.get("access_token")
    assert isinstance(token, str) and token, "Missing access token"
    return token

def run_checks(base, password1, password2):
    health = expect("health", call(base, "GET", "/health"), 200)
    assert health["status"] == "ok" and health["version"], "Health contract mismatch"
    expect("missing token", call(base, "GET", "/requests"), 401)
    expect("invalid token", call(base, "GET", "/requests", token="not-a-token"), 401)
    expect("wrong password", call(base, "POST", "/auth/token",
           {"username": "learner01", "password": secrets.token_urlsafe(40)}, form=True), 401)
    token1 = login(base, "learner01", password1)
    token2 = login(base, "learner02", password2)
    before = expect("list own requests", call(base, "GET", "/requests", token=token1), 200)
    assert isinstance(before, list), "List response must be a JSON array"
    for item in before:
        valid_request(item, "learner01")
    good = {
        "title": "API check " + uuid.uuid4().hex[:8],
        "description": "Synthetic request created by the workshop contract checker.",
        "category": "it"
    }
    expect("blank title", call(base, "POST", "/requests",
           dict(good, title="     "), token1), 422)
    expect("wrong category", call(base, "POST", "/requests",
           dict(good, category="other"), token1), 422)
    expect("forged owner", call(base, "POST", "/requests",
           dict(good, owner_username="learner02"), token1), 422)
    created = expect("create", call(base, "POST", "/requests", good, token1), 201)
    valid_request(created, "learner01")
    assert created["status"] == "new"
    request_id = created["id"]
    own = expect("read created", call(base, "GET", "/requests/" + request_id,
                 token=token1), 200)
    assert own["title"] == good["title"]
    expect("other owner cannot read", call(base, "GET", "/requests/" + request_id,
           token=token2), 404)
    expect("other owner cannot edit", call(base, "PATCH",
           "/requests/" + request_id + "/status", {"status": "done"}, token2), 404)
    expect("wrong status", call(base, "PATCH", "/requests/" + request_id + "/status",
           {"status": "closed"}, token1), 422)
    updated = expect("update status", call(base, "PATCH",
                     "/requests/" + request_id + "/status", {"status": "done"}, token1), 200)
    assert updated["status"] == "done"
    again = expect("read updated", call(base, "GET", "/requests/" + request_id,
                   token=token1), 200)
    assert again["status"] == "done"
    after = expect("list after create", call(base, "GET", "/requests", token=token1), 200)
    assert len(after) == len(before) + 1, "Unexpected count; use an isolated learner database"
    other = expect("other owner's list", call(base, "GET", "/requests", token=token2), 200)
    for item in other:
        valid_request(item, "learner02")
    assert all(item["id"] != request_id for item in other)
    missing_id = str(uuid.uuid4())
    expect("missing UUID", call(base, "GET", "/requests/" + missing_id,
           token=token1), 404)
    print("PASS contract checks. Synthetic request retained for persistence check:", request_id)
    print("Restart API, sign in again, and GET this ID to verify persistence separately.")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True)
    args = parser.parse_args()
    base = args.base_url.rstrip("/")
    parsed = urlsplit(base)
    if parsed.username or parsed.password or parsed.query or parsed.fragment:
        parser.error("Base URL must not contain credentials, query or fragment.")
    if parsed.path not in ("", "/") or not parsed.hostname:
        parser.error("Use API origin only, without a path.")
    if parsed.scheme != "https" and not (
        parsed.scheme == "http" and parsed.hostname in ("localhost", "127.0.0.1", "::1")
    ):
        parser.error("Use HTTPS for cloud, or HTTP only for loopback lab.")
    print("This check creates one synthetic request in your isolated training database.")
    p1 = getpass.getpass("Password for learner01 (hidden): ")
    p2 = getpass.getpass("Password for learner02 (hidden): ")
    try:
        run_checks(base, p1, p2)
    except (AssertionError, URLError, ValueError, KeyError, TypeError, TimeoutError):
        print("FAIL: API contract or connection check failed. See the last PASS above.")
        print("Inspect the failing route/status locally; do not paste passwords or tokens.")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
