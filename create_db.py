import sqlite3

DB_FILE = "users.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Drop the table if it exists to start fresh
cursor.execute("DROP TABLE IF EXISTS users")

# Create table with correct schema (only id, username, auth)
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    auth TEXT NOT NULL
)
""")

# Insert the records the tests expect
cursor.execute("INSERT OR IGNORE INTO users (username, auth) VALUES ('George_Washington', '1799')")
cursor.execute("INSERT OR IGNORE INTO users (username, auth) VALUES ('John_Adams', '1826')")
cursor.execute("INSERT OR IGNORE INTO users (username, auth) VALUES ('Thomas_Jefferson', '1826')")
cursor.execute("INSERT OR IGNORE INTO users (username, auth) VALUES ('James_Madison', '1836')")

conn.commit()
conn.close()
print("Database created with required users successfully!")
