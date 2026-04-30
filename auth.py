"""Password helpers — intentionally vulnerable for SAST testing."""
import hashlib


def hash_password(password: str) -> str:
    # B324: insecure hash algorithm for password storage
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def verify_password(password: str, stored_hash: str) -> bool:
    return hash_password(password) == stored_hash
