"""

Phase 1, 2: Very simple history log — appends each routed task to a JSON file.

"""

import json
import os
from datetime import datetime, timezone

HISTORY_FILE = os.path.join(os.path.dirname(__file__), "history_log.json")


def log_entry(prompt: str, model: str, reason: str, method: str) -> None:
    entries = load_history()
    entries.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "prompt": prompt,
        "model": model,
        "reason": reason,
        "method": method,
    })
    # Keep only the most recent 50 entries so the file doesn't grow forever.
    entries = entries[-50:]

    with open(HISTORY_FILE, "w") as f:
        json.dump(entries, f, indent=2)


def load_history() -> list:
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)
