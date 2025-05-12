import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('apps_database.db')
cursor = conn.cursor()

# Create tables for system apps and web apps
cursor.execute('''
CREATE TABLE IF NOT EXISTS system_apps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    app_name TEXT NOT NULL,
    app_path TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS web_apps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    app_name TEXT NOT NULL,
    app_url TEXT NOT NULL
)
''')

# Insert sample data into system_apps table
system_apps = [
    ('File Explorer', 'C:/Windows/explorer.exe'),
    ('Notepad', 'C:/Windows/System32/notepad.exe'),
    ('Calculator', 'C:/Windows/System32/calc.exe')
]

cursor.executemany('''
INSERT INTO system_apps (app_name, app_path)
VALUES (?, ?)
''', system_apps)

# Insert sample data into web_apps table
web_apps = [
    ('Google', 'https://www.google.com'),
    ('YouTube', 'https://www.youtube.com'),
    ('GitHub', 'https://github.com')
]

cursor.executemany('''
INSERT INTO web_apps (app_name, app_url)
VALUES (?, ?)
''', web_apps)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Databases and sample data created successfully.")