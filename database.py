import sqlite3

def create_tables(db_name="bugs.db"):
    connection = sqlite3.connect(db_name)
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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY,
        bug_id INTEGER,
        comment TEXT
    )
    """)

    connection.commit() #Actually save the changes to the database
    connection.close() #Done talking to database

if __name__ == "__main__":
    create_tables()
