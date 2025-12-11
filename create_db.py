import sqlite3

DB_FILE = "users.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Drop the table if it exists to start fresh
cursor.execute("DROP TABLE IF EXISTS users")

# Create table with correct schema
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    year TEXT,
    auth TEXT
)
""")

# Insert sample users
cursor.execute("INSERT INTO users (username, year, auth) VALUES ('James_Madison', '1836', 'admin')")
cursor.execute("INSERT INTO users (username, year, auth) VALUES ('John_Adams', '1797', 'admin')")
cursor.execute("INSERT INTO users (username, year, auth) VALUES ('Thomas_Jefferson', '1801', 'admin')")
cursor.execute("INSERT INTO users (username, year, auth) VALUES ('George_Washington', '1789', 'admin')")
cursor.execute("INSERT INTO users (username, year, auth) VALUES ('sakul', '2023', 'superadmin')")

conn.commit()
conn.close()
print("Database created and sample users added successfully!")
