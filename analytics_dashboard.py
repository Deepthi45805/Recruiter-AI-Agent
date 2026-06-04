import streamlit as st
import pandas as pd

# Title
st.title("Recruitment Analytics Dashboard")

# Sample Candidate Data
data = {
    "Candidate": ["Deepthi", "Rahul", "Priya"],
    "ATS Score": [85, 70, 90],
    "Match %": [80, 60, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Table
st.subheader("Candidate Analytics")
st.dataframe(df)

# Summary Metrics
st.subheader("Summary")

st.metric("Total Candidates", len(df))
st.metric("Average ATS Score", round(df["ATS Score"].mean(), 2))

# ATS Score Chart
st.subheader("ATS Scores")
st.bar_chart(df.set_index("Candidate")["ATS Score"])

# Match Percentage Chart
st.subheader("Skill Match Percentage")
st.line_chart(df.set_index("Candidate")["Match %"])
