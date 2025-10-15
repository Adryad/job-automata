# utils/storage.py
import sqlite3
from datetime import datetime

class Storage:
    def __init__(self, db_path):
        self.db_path = db_path
        self._ensure_tables()

    def _conn(self):
        return sqlite3.connect(self.db_path)

    def _ensure_tables(self):
        conn = self._conn()
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT,
            job_title TEXT,
            company TEXT,
            job_link TEXT,
            applied_at TEXT,
            status TEXT
        )
        """)
        conn.commit()
        conn.close()

    def add_application(self, platform, job_title, company, job_link, status="applied"):
        conn = self._conn()
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO applications (platform, job_title, company, job_link, applied_at, status)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (platform, job_title, company, job_link, datetime.utcnow().isoformat(), status))
        conn.commit()
        conn.close()
