import sqlite3
import config

def settings_create_table():
    with sqlite3.connect(config.SETTINGS_DIR) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ten TEXT NOT NULL UNIQUE,
                value TEXT)
            """)
        conn.commit()

def settings_insert(ten, value):
    with sqlite3.connect(config.SETTINGS_DIR) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO settings (ten, value) VALUES (?, ?)", (ten, value))
        conn.commit()

def settings_update(ten, value):
    with sqlite3.connect(config.SETTINGS_DIR) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE settings SET value = ? WHERE ten = ?", (value, ten))
        conn.commit()

def settings_upsert(ten, value):
    with sqlite3.connect(config.SETTINGS_DIR) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO settings (ten, value)
            VALUES (?, ?)
            ON CONFLICT(ten) DO UPDATE SET value = excluded.value
            """, (ten, value))
        conn.commit()

def settings_select_all():
    with sqlite3.connect(config.SETTINGS_DIR) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM settings")
        return cursor.fetchall()
    
def settings_get_by_ten(ten, default=None):
    with sqlite3.connect(config.SETTINGS_DIR) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM settings WHERE ten = ?", (ten,))
        row = cursor.fetchone()
        return row[0] if row else default
    
def settings_delete_by_ten(ten):
    with sqlite3.connect(config.SETTINGS_DIR) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM settings WHERE ten = ?", (ten,))
        conn.commit()

def settings_delete_all():
    with sqlite3.connect(config.SETTINGS_DIR) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM settings")
        conn.commit()