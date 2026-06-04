from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os

GOOGLE_API_KEY = "YOUR_API_KEY"

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GOOGLE_API_KEY
)

prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Extract the following information from the resume.

Name:
Skills:
Experience:
Education:

Resume:
{resume}

Return only JSON format.

Example:
{{
"name":"Deepthi",
"skills":["Python","SQL","AWS"],
"experience":"1 year",
"education":"B.Tech"
}}
"""
)

resume_text = """
Paste your extracted resume text here
"""

chain = prompt | llm

response = chain.invoke({"resume": resume_text})

print(response.content)
