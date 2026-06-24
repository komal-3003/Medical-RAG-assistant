import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    """
    Extracts all text from an uploaded PDF file.

    Parameters:
        uploaded_file: Streamlit UploadedFile object

    Returns:
        str: Extracted text from the PDF
    """

    text = ""

    # Open PDF from uploaded file bytes
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    # Read each page
    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text
