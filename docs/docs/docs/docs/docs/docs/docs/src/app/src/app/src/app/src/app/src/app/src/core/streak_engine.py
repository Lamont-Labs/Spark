# FILE: src/core/streak_engine.py
import sqlite3, os, datetime, json

DB_PATH = os.path.join(os.path.dirname(__file__), "../../dist/demo_db/spark_demo.sqlite")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE,
            gratitude TEXT,
            win TEXT,
            affirmation TEXT
        )
    """)
    conn.commit()
    conn.close()

def saveEntry(entry):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    today = datetime.date.today().isoformat()
    conn.execute("INSERT OR REPLACE INTO entries (date, gratitude, win, affirmation) VALUES (?, ?, ?, ?)",
                 (today, entry.get("gratitude"), entry.get("win"), entry.get("affirmation")))
    conn.commit()
    conn.close()

def getEntries():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.execute("SELECT * FROM entries ORDER BY date DESC")
    rows = [dict(id=r[0], date=r[1], gratitude=r[2], win=r[3], affirmation=r[4]) for r in cur.fetchall()]
    conn.close()
    return rows

def getStreakStatus():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.execute("SELECT date FROM entries ORDER BY date DESC LIMIT 7")
    dates = [datetime.date.fromisoformat(r[0]) for r in cur.fetchall()]
    conn.close()
    if not dates: return {"current":0,"best":0,"message":"Start your first streak!"}
    streak = 1
    for i in range(1, len(dates)):
        if (dates[i-1] - dates[i]).days <= 1: streak += 1
        else: break
    best = streak
    msg = "On fire! Keep it up 🔥" if streak>=3 else "You’re building momentum."
    return {"current": streak, "best": best, "message": msg}
