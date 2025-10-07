# FILE: tests/test_streak_engine.py
import os, pytest
from src.core import streak_engine

def test_save_and_get_entries(tmp_path):
    dbfile = tmp_path / "spark_demo.sqlite"
    streak_engine.DB_PATH = str(dbfile)
    streak_engine.init_db()
    streak_engine.saveEntry({"gratitude":"a","win":"b","affirmation":"c"})
    rows = streak_engine.getEntries()
    assert len(rows) == 1

def test_streak_logic(tmp_path):
    dbfile = tmp_path / "spark_demo.sqlite"
    streak_engine.DB_PATH = str(dbfile)
    streak_engine.init_db()
    streak_engine.saveEntry({"gratitude":"g","win":"w","affirmation":"a"})
    s = streak_engine.getStreakStatus()
    assert "current" in s
