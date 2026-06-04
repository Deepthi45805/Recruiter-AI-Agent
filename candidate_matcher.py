candidate_skills = [
    "Python",
    "SQL",
    "Machine Learning"
]

jd_skills = [
    "Python",
    "SQL",
    "Data Analysis"
]

candidate_set = set(skill.lower() for skill in candidate_skills)

jd_set = set(skill.lower() for skill in jd_skills)

matched_skills = candidate_set.intersection(jd_set)

match_percentage = (
    len(matched_skills) / len(jd_set)
) * 100

print("Matched Skills:", matched_skills)

print("Match Percentage:",
      round(match_percentage, 2), "%")
