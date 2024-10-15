import sqlite3
from datetime import datetime, timedelta

DATABASE_FILE = "db/karma.db"

def initialize_db():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT 0,
        urgency_importance TEXT NOT NULL,
        date_created DATE DEFAULT CURRENT_DATE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS karma_points (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        points INTEGER NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def add_task(task_name, urgency_importance):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task_name, urgency_importance, completed) VALUES (?, ?, 0)', (task_name, urgency_importance))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE date_created = CURRENT_DATE')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task_status(task_name, completed):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = ? WHERE task_name = ?', (completed, task_name))
    conn.commit()
    conn.close()

def calculate_previous_day_karma():
    yesterday = (datetime.now() - timedelta(days=1)).date()

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tasks WHERE date_created = ?', (yesterday,))
    tasks = cursor.fetchall()

    completed_tasks = sum(1 for task in tasks if task[2] == 1)
    total_tasks = len(tasks)
    karma_points = completed_tasks * 10 - (total_tasks - completed_tasks) * 5

    cursor.execute('INSERT INTO karma_points (date, points) VALUES (?, ?)', (yesterday, karma_points))
    conn.commit()
    conn.close()

def check_new_day():
    today = datetime.now().date()

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute('SELECT MAX(date) FROM karma_points')
    last_date = cursor.fetchone()[0]

    if last_date is None or datetime.strptime(last_date, '%Y-%m-%d').date() < today:
        return True
    return False

def get_karma_points():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT date, points FROM karma_points ORDER BY date')
    data = cursor.fetchall()
    conn.close()
    return data
