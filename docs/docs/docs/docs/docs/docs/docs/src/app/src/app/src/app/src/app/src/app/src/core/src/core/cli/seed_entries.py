# FILE: cli/seed_entries.py
import json, os, random
from src.core import streak_engine

SAMPLE_PROMPTS = json.load(open(os.path.join("src/core/prompt_bank.json")))

def run_seed(mode="teen"):
    entries = []
    for i in range(5):
        e = {
            "gratitude": random.choice(SAMPLE_PROMPTS[mode]),
            "win": "Completed demo seed step",
            "affirmation": "I am growing every day."
        }
        entries.append(e)
        streak_engine.saveEntry(e)
    print(f"Seeded {len(entries)} demo entries for mode={mode}")

if __name__ == "__main__":
    streak_engine.init_db()
    run_seed("teen")
