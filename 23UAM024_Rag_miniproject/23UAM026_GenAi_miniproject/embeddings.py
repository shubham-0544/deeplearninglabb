from langchain_community.embeddings import HuggingFaceEmbeddings
import pdftotext

# Load model ONCE
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def embed(pdf_path):
    resume_text, resume_info = pdftotext.load_pdf_resume(pdf_path)

    resume_text = resume_text.strip()
    if not resume_text:
        raise ValueError(f"Empty resume text: {pdf_path}")

    # ONE resume → ONE embedding
    embedding = embedding_model.embed_query(resume_text)

    return [embedding], resume_text, resume_info


def embed_text(text: str):
    text = text.strip()
    if not text:
        raise ValueError("Empty text for embedding")

    return embedding_model.embed_query(text)
