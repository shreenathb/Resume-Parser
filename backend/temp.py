import PyPDF2

def getText():
    pdf_path = "/Users/shreenath/Documents/CollegeProjects/Resume-Parser/backend/uploads/Shreenath_Bandivadekar_C2K221260_Resume.pdf"
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text