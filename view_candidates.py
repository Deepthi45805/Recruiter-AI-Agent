import sqlite3

conn = sqlite3.connect("recruiter.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM candidates")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
