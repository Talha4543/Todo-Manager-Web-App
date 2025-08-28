import sqlite3

DB_NAME = "todos.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Todos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        title TEXT,
        completed INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()
