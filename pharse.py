import fitz  # PyMuPDF

# Path to your PDF file
pdf_path = "C:/Users/balag/Desktop/science2.pdf"

# Path to save the extracted text file
output_text_file = 'C:/Users/balag/OneDrive/Documents/StudentpdfOutput/extracted_text.txt'

# Function to extract text from PDF using PyMuPDF
def extract_text_from_pdf(pdf_path):
    extracted_text = ''
    with fitz.open(pdf_path) as doc:
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            extracted_text += page.get_text()
    return extracted_text

# Extract text from PDF using PyMuPDF
extracted_text = extract_text_from_pdf(pdf_path)

# Save extracted text to a text file
with open(output_text_file, 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print("Text extracted from PDF and saved to another file successfully.")
