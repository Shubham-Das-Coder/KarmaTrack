import sqlite3
from datetime import datetime

DB_PATH = 'db/karmatrack.db'

def initialize_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create tasks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            urgency INTEGER NOT NULL,
            importance INTEGER NOT NULL,
            completed BOOLEAN NOT NULL,
            date_added DATE NOT NULL
        )
    ''')

    # Create karma points table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS karma_points (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            points INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def check_new_day():
    # Compare today's date with last recorded date in tasks table
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT MAX(date_added) FROM tasks')
    last_date = cursor.fetchone()[0]

    today = datetime.now().date()
    conn.close()
    
    if not last_date or last_date != str(today):
        return True
    return False

def calculate_previous_day_karma():
    # Calculate points for the previous day's tasks and add to karma points
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    today = datetime.now().date()
    cursor.execute('SELECT COUNT(*) FROM tasks WHERE completed = 1 AND date_added = ?', (today,))
    completed_tasks = cursor.fetchone()[0]
    
    points = completed_tasks * 10  # Example: 10 points per completed task

    cursor.execute('INSERT INTO karma_points (date, points) VALUES (?, ?)', (today, points))
    conn.commit()
    conn.close()
