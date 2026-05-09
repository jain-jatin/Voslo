import os
from pypdf import PdfReader

pdf_dir = r"c:\Users\ASUS\OneDrive\Downloads\Voslo\Sample PRD"
out_file = r"c:\Users\ASUS\OneDrive\Downloads\Voslo\pdf_text.txt"

with open(out_file, "w", encoding="utf-8") as f_out:
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            filepath = os.path.join(pdf_dir, filename)
            f_out.write(f"\n\n--- EXTRACTING {filename} ---\n")
            try:
                reader = PdfReader(filepath)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                f_out.write(text[:1500]) # Print first 1500 chars to get the skeleton and structure
            except Exception as e:
                f_out.write(f"Error reading {filename}: {e}\n")
