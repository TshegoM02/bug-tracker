import sqlite3

connection = sqlite3.connect("bugs.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bugs (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    severity TEXT,
    status TEXT
)
""")

connection.commit() #Actually save the changes to the database
connection.close() #Done talking to database