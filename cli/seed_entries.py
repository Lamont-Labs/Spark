"""
SparkApp v2.3 — Demo Seeder
Purpose: Creates or refreshes a local SQLite demo DB with synthetic entries.
This is a deterministic, self-contained seed script for CI.
"""

import os
import sqlite3
from datetime import datetime

DB_PATH = os.environ.get("SPARK_DB_PATH", "dist/demo_db/spark_demo.sqlite")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def seed_demo_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            gratitude TEXT,
            win TEXT,
            affirmation TEXT
        )
    """)
    demo_rows = [
        ("2025-10-01", "A good morning walk", "Finished first demo run", "I am consistent."),
        ("2025-10-02", "Time with family", "Fixed workflow", "I follow through."),
        ("2025-10-03", "Learning progress", "Improved CI", "I keep improving.")
    ]
    cur.executemany("INSERT INTO entries (date, gratitude, win, affirmation) VALUES (?, ?, ?, ?)", demo_rows)
    conn.commit()
    conn.close()
    print(f"[✓] Demo DB seeded with {len(demo_rows)} entries at {DB_PATH}")

if __name__ == "__main__":
    seed_demo_data()
