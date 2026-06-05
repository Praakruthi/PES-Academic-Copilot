from pypdf import PdfReader
import google.generativeai as genai

# -----------------------------
# Gemini API Configuration
# -----------------------------
API_KEY = "GEMINI_API_KEY"

genai.configure(api_key=API_KEY)

# -----------------------------
# Read PDF
# -----------------------------
pdf_file = input("Enter PDF file path: ")

reader = PdfReader(pdf_file)

document_text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        document_text += page_text

print("\nPDF loaded successfully!")
print(f"Characters extracted: {len(document_text)}")

# -----------------------------
# Ask Question
# -----------------------------
question = input("\nAsk a question about the document: ")

# -----------------------------
# Create Prompt
# -----------------------------
prompt = f"""
You are a helpful study assistant.

Use the following document to answer the question.

DOCUMENT:
{document_text}

QUESTION:
{question}

If the answer is not present in the document,
say that the information is not available.
"""

# -----------------------------
# Gemini Model
# -----------------------------
model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(prompt)

# -----------------------------
# Display Answer
# -----------------------------
print("\nAnswer:\n")
print(response.text)