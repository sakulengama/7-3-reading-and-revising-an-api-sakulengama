import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()
cur.execute("SELECT username, auth FROM users ORDER BY username")
print(cur.fetchall())
conn.close()
