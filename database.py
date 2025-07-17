import sqlite3
from datetime import datetime

DB_NAME = "permadi.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        tanggal TEXT,
        name TEXT,
        email TEXT PRIMARY KEY,
        umur INTEGER,
        divisi TEXT,
        aktivitas TEXT,
        layanan TEXT,
        keterangan TEXT,
        rca TEXT,
        solusi TEXT,
        status TEXT
    )''')
    conn.commit()
    conn.close()

def insert_data(name, email, umur, divisi, aktivitas, layanan, keterangan, rca, solusi, status):
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
              (tanggal, name, email, umur, divisi, aktivitas, layanan, keterangan, rca, solusi, status))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()
    return data

def update_status(email, status):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET status = ? WHERE email = ?", (status, email))
    conn.commit()
    conn.close()