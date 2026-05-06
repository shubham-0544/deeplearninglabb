from langchain_community.document_loaders import PyPDFLoader

def load_pdf_resume(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    resume_content=""
    for page in docs:
        resume_content+=page.page_content
    metadata = {
        "source": pdf_path,
        "page_count": len(docs)
    }
    return resume_content, metadata

# resume_path="C:/Users/haris/Downloads/LOU/fake-resumes/resume-003.pdf"
# resume_text, resume_info = load_pdf_resume(resume_path)
# print(resume_info)
# print(resume_text)