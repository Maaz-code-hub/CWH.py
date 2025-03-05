from pypdf import PdfWriter

def merge_pdfs(pdf_list, output_file):
    merger = PdfWriter()
    
    for pdf in pdf_list:
        merger.append(pdf)
    
    merger.write(output_file)
    merger.close()
    print(f"Merged PDF saved as: {output_file}")

if __name__ == "__main__":
    pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]  # Replace with actual file names
    output_pdf = "merged_output.pdf"
    merge_pdfs(pdf_files, output_pdf)
