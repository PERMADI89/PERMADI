import sqlite3
import pandas as pd
from datetime import datetime

DB_NAME = "data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            name TEXT,
            email TEXT,
            umur INTEGER,
            divisi TEXT,
            aktivitas TEXT,
            layanan TEXT,
            keterangan TEXT,
            rca TEXT,
            solusi TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_data(name, email, umur, divisi, aktivitas, layanan, keterangan, rca, solusi, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO activities (timestamp, name, email, umur, divisi, aktivitas, layanan, keterangan, rca, solusi, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (timestamp, name, email, umur, divisi, aktivitas, layanan, keterangan, rca, solusi, status))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM activities ORDER BY id DESC", conn)
    conn.close()
    return df
