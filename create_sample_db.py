# create_sample_db.py

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('sample.db')

# Create a cursor object
cursor = conn.cursor()

# Create sample tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

# Insert sample data
cursor.executemany('INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)', [
    ('Alice', 'HR', 70000),
    ('Bob', 'Engineering', 80000),
    ('Charlie', 'Sales', 60000)
])

cursor.executemany('INSERT INTO departments (name) VALUES (?)', [
    ('HR',),
    ('Engineering',),
    ('Sales',)
])

# Commit changes and close connection
conn.commit()
conn.close()
