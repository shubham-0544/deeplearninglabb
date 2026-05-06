import chromadb
import os
import embeddings

client = chromadb.PersistentClient(path="./knowledge_base")
collection = client.get_or_create_collection("resumes")

def store_resume(pdf_path):
    resume_embeddings, resume_text, resume_info = embeddings.embed(pdf_path)

    resume_id = os.path.splitext(os.path.basename(pdf_path))[0]

    collection.delete(where={"resume_id": resume_id})

    collection.add(
        ids=[resume_id],
        embeddings=resume_embeddings,
        documents=[resume_text],
        metadatas=[{
            "resume_id": resume_id,
            "source": resume_info["source"],
            "page_count": resume_info["page_count"]
        }]
    )

def search_resumes(job_description, top_k):
    query_embedding = embeddings.embed_text(job_description)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas"]
    )

    return results
