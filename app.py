import pandas as pd

st.header("Recruitment Analytics Dashboard")

data = {
    "Candidate": ["Deepthi", "Rahul", "Priya"],
    "ATS Score": [85, 70, 90],
    "Match %": [80, 60, 95]
}

df = pd.DataFrame(data)

st.subheader("Candidate Analytics")
st.dataframe(df)

st.subheader("Summary")
st.metric("Total Candidates", len(df))
st.metric("Average ATS Score", round(df["ATS Score"].mean(), 2))

st.subheader("ATS Scores")
st.bar_chart(df.set_index("Candidate")["ATS Score"])

st.subheader("Skill Match Percentage")
st.line_chart(df.set_index("Candidate")["Match %"])
