from langchain_google_genai import ChatGoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "YOUR_NEW_API_KEY"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

with open("resume.txt", "r", encoding="utf-8") as f:
    resume = f.read()

question = "What skills does the candidate have?"

response = llm.invoke(
    f"""
Resume:
{resume}

Question:
{question}
"""
)

print(response.content)
