from pypdf import PdfWriter
import os

def merge_pdfs(pdf_list, output_path):
    # Initialize the PDF writer
    merger = PdfWriter()

    # Append each PDF to the writer
    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_path)


# Usage
files_to_merge = ["file1.pdf", "file2.pdf", "file3.pdf"]
merge_pdfs(files_to_merge, "merged_output24.pdf")

print(f"Merged PDF created successfully! at {os.getcwd()}")