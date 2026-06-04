import sqlite3

conn = sqlite3.connect("recruiter.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO candidates (name, skills, experience, education)
VALUES (?, ?, ?, ?)
""", (
    "Deepthi",
    "Python, SQL, Machine Learning",
    "Fresher",
    "B.Tech"
))

conn.commit()

print("Candidate inserted successfully!")

conn.close()
