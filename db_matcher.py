import sqlite3

conn = sqlite3.connect("recruiter.db")

cursor = conn.cursor()

cursor.execute("SELECT name, skills FROM candidates")

candidates = cursor.fetchall()

jd_skills = ["Python", "SQL", "Data Analysis"]

jd_set = set(skill.lower() for skill in jd_skills)

for candidate in candidates:

    name = candidate[0]

    skills = candidate[1].split(",")

    candidate_set = set(skill.strip().lower() for skill in skills)

    matched_skills = candidate_set.intersection(jd_set)

    match_percentage = (
        len(matched_skills) / len(jd_set)
    ) * 100

    print("\nCandidate:", name)

    print("Matched Skills:", matched_skills)

    print("Match Percentage:",
          round(match_percentage, 2), "%")

conn.close()
