from langchain_google_genai import ChatGoogleGenerativeAI

# Gemini API Key
API_KEY = "YOUR_API_KEY"

# Read resume text
with open("resume.txt", "r", encoding="utf-8") as f:
    resume = f.read()

# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=API_KEY
)

prompt = f"""
Extract the following details from this resume:

1. Name
2. Skills
3. Education
4. Experience

Resume:
{resume}

Return the output in a clean format.
"""

response = llm.invoke(prompt)

print(response.content)
