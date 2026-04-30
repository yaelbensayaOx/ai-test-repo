# autofix-test-repo

Tiny Python project with intentional vulnerabilities used to test OX SAST
autofix on `org_YImTYFhy1NlgjqpW` (dev). Each finding here maps to a rule
from `autofix-service/src/chatgpt_autofixable_rules.txt`, so the autofix
service should be able to produce an AI fix for it.

| File | Rule | Finding |
|---|---|---|
| `app/auth.py` | B324 | `hashlib.md5` used to hash passwords |
| `app/db.py` | B608 | SQL string concatenation (SQL injection) |
| `app/runner.py` | B607 | `subprocess` with partial executable path |
| `app/debug_app.py` | B201 | Flask app started with `debug=True` |

DO NOT USE IN PRODUCTION. Every file is intentionally vulnerable.
