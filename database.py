import sqlite3
from datetime import datetime

DB_NAME = "data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal TEXT,
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
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("""
        INSERT INTO users (
            tanggal, name, email, umur, divisi, aktivitas, layanan, 
            keterangan, rca, solusi, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (tanggal, name, email, umur, divisi, aktivitas, layanan, keterangan, rca, solusi, status))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        SELECT tanggal, name, email, umur, divisi, aktivitas, layanan, 
               keterangan, rca, solusi, status 
        FROM users
    """)
    data = c.fetchall()
    conn.close()
    return data

def update_status(email, status):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET status=? WHERE email=?", (status, email))
    conn.commit()
    conn.close()
