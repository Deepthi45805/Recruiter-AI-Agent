import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("recruiter.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY,
    name TEXT,
    skills TEXT,
    experience TEXT,
    education TEXT
)
""")

# Save changes
conn.commit()

print("Table created successfully!")

# Close connection
conn.close()
