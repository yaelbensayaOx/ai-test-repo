"""User lookup — intentionally vulnerable for SAST testing."""
import sqlite3


def find_user_by_email(email: str):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    # B608: SQL injection via string formatting
    query = "SELECT id, email FROM users WHERE email = '" + email + "'"
    cur.execute(query)
    return cur.fetchone()
