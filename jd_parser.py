with open("job_description.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

skills = ["Python", "SQL", "Machine Learning", "Pandas"]
education_list = ["B.Tech", "B.E", "MCA", "M.Tech"]

found_skills = [s for s in skills if s.lower() in jd_text.lower()]
found_education = [e for e in education_list if e.lower() in jd_text.lower()]

experience = ""

for line in jd_text.split("\n"):
    if "years" in line.lower():
        experience = line

print("Required Skills:", found_skills)
print("Education:", found_education)
print("Experience:", experience)
