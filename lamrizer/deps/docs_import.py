import PyPDF2
import docx

# PDF -> Text
def PdfToText(pdf_path):
    # Convert PDF to text
    text = ''
    with open(pdf_path, 'rb') as f:
        pdf = PyPDF2.PdfReader(f)
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            text += page.extract_text()
    return text

# Convert TXT to string
def TxtToText(txt_path):
    # Convert TXT to text
    with open(txt_path, 'r') as f:
        text = f.read()
    
    return text

# DOCX -> Text
def DocxToText(docx_path):
    # Convert DOCX to text using python-docx
    doc = docx.Document(docx_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text