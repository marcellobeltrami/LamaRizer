import PyPDF2

# PDF -> Text
def PdfToText(pdf_path):
    # Convert PDF to text
    text = ''
    with open(pdf_path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        for page_num in range(pdf.getNumPages()):
            page = pdf.getPage(page_num)
            text += page.extract_text()
    return text

# Convert TXT to string
def TxtToText(txt_path):
    # Convert TXT to text
    with open(txt_path, 'r') as f:
        text = f.read()