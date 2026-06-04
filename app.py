import streamlit as st

st.title("Recruiter AI Dashboard")

# Read resume
with open("resume.txt", "r", encoding="utf-8") as f:
    resume_data = f.read()

st.header("Resume Content")
st.text_area("Extracted Resume", resume_data, height=250)

# Match Results
st.header("Match Results")

matched_skills = ["Python", "SQL"]
match_percentage = 66.67

st.write("Matched Skills:", ", ".join(matched_skills))
st.write(f"Match Percentage: {match_percentage}%")
