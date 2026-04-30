"""Shell helper — intentionally vulnerable for SAST testing."""
import subprocess


def list_directory(path: str) -> str:
    # B607: subprocess called with a partial executable path
    result = subprocess.run(["ls", path], capture_output=True, text=True)
    return result.stdout
