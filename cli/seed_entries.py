# FILE: cli/seed_entries.py
import sqlite3, os, datetime

def seed_demo():
    os.makedirs("dist/demo_db", exist_ok=True)
    db_path = "dist/demo_db/spark_demo.sqlite"
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS gratitude_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            gratitude TEXT,
            win TEXT,
            affirmation TEXT
        )
    """)

    demo_entries = [
        ("2025-10-05", "Woke up early and focused", "Finished repo CI", "I persist until proof."),
        ("2025-10-06", "Good conversation with family", "Kept streak alive", "I adapt calmly."),
        ("2025-10-07", "Healthy meal and walk", "Clean CI pass", "I’m proud of progress.")
    ]

    c.executemany("INSERT INTO gratitude_entries (date, gratitude, win, affirmation) VALUES (?, ?, ?, ?)", demo_entries)
    conn.commit()
    conn.close()
    print(f"[✓] Demo database seeded at {db_path}")

if __name__ == "__main__":
    seed_demo()
