from pypdf import PdfReader
import sys

def extract_text(pdf_path, txt_path):
    reader = PdfReader(pdf_path)
    with open(txt_path, 'w', encoding='utf-8') as f:
        for page in reader.pages:
            f.write(page.extract_text() + '\n')

if __name__ == "__main__":
    extract_text("main.pdf", "main_thesis.txt")
