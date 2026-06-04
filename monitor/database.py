import sqlite3
from datetime import date

DB_FILE = 'screentime.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS app_usage (
            usage_date TEXT,
            app_name TEXT,
            duration_seconds INTEGER,
            PRIMARY KEY (usage_date, app_name)
        )
    ''')
    conn.commit()
    conn.close()

def log_app_time(app_name, seconds=1):
    if app_name == 'Idle': return
    today = str(date.today())
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO app_usage (usage_date, app_name, duration_seconds)
        VALUES (?, ?, ?)
        ON CONFLICT(usage_date, app_name) DO UPDATE SET
        duration_seconds = duration_seconds + ?
    ''', (today, app_name, seconds, seconds))
    
    conn.commit()
    conn.close()

def get_today_usage():
    today = str(date.today())
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT app_name, duration_seconds 
        FROM app_usage 
        WHERE usage_date = ? 
        ORDER BY duration_seconds DESC
        LIMIT 5
    ''', (today,))
    data = cursor.fetchall()
    conn.close()
    return data
