from pypdf import PdfReader

def extract_resume(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

resume_text = extract_resume("resume.pdf")

print(resume_text)

with open("resume.txt", "w", encoding="utf-8") as f:
    f.write(resume_text)

print("Resume saved to resume.txt")
