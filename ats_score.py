def calculate_ats_score(resume_skills, jd_skills):
    matched_skills = set(resume_skills).intersection(set(jd_skills))

    score = (len(matched_skills) / len(jd_skills)) * 100

    return score, matched_skills


# Example Data
resume_skills = ["Python", "SQL", "Machine Learning"]
jd_skills = ["Python", "SQL", "Power BI", "Excel"]

score, matched = calculate_ats_score(resume_skills, jd_skills)

print("Matched Skills:", matched)
print("ATS Score:", round(score, 2), "%")
