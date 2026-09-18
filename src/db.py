import sqlite3

def init_db():
    conn = sqlite3.connect("database/logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            action TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_log(ip, action, timestamp):
    conn = sqlite3.connect("database/logs.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (ip, action, timestamp) VALUES (?, ?, ?)", (ip, action, timestamp))
    conn.commit()
    conn.close()

def fetch_logs():
    conn = sqlite3.connect("database/logs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs")
    rows = cursor.fetchall()
    conn.close()
    return rows
