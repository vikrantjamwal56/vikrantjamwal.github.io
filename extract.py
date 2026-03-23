from pypdf import PdfReader

def extract_text():
    try:
        reader = PdfReader("Vikrant_CV updated.pdf")
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        with open("cv_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully extracted text to cv_text.txt")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_text()
