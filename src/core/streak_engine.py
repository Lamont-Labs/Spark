"""
SparkApp v2.3 — Deterministic Streak Engine
This script computes the 'bend-not-break' streak pattern deterministically.
"""

import datetime
import json
import os

def compute_streak(entries):
    """Compute streak length with one grace day allowed per week."""
    if not entries:
        return 0
    days = sorted(datetime.date.fromisoformat(d) for d in entries)
    streak, grace, max_streak = 1, 1, 1
    for i in range(1, len(days)):
        delta = (days[i] - days[i - 1]).days
        if delta == 1:
            streak += 1
        elif delta == 2 and grace > 0:
            streak += 1
            grace -= 1
        else:
            max_streak = max(max_streak, streak)
            streak, grace = 1, 1
    return max(max_streak, streak)

def main():
    entries = ["2025-10-01", "2025-10-02", "2025-10-03", "2025-10-05"]
    result = {
        "entries": entries,
        "streak_length": compute_streak(entries),
        "timestamp": str(datetime.datetime.utcnow())
    }
    os.makedirs("provenance", exist_ok=True)
    with open("provenance/streak_result.json", "w") as f:
        json.dump(result, f, indent=2)
    print("[✓] streak_result.json created successfully.")

if __name__ == "__main__":
    main()
