import streamlit as st
import os
from ChromaStore import store_resume, search_resumes
from LLMExplain import explain


st.title("AI Resume Shortlisting App")
st.success("Backend Connected Successfully")

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.write(f"{len(uploaded_files)} files uploaded")

UPLOAD_DIR = "uploaded_resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)
if st.button("Store Resumes"):
    if uploaded_files:
        for file in uploaded_files:
            save_path = os.path.join(UPLOAD_DIR, file.name)
            with open(save_path, "wb") as f:
                f.write(file.read())

            store_resume(save_path)
        st.success("Resumes stored successfully!")
    else:
        st.error("Please upload at least one resume PDF.")

st.header("Shortlist Resumes")

job_description = st.text_area(
    "Enter Job Description",
    height=50
)

top_k = st.number_input(
    "Number of resumes to shortlist",
    min_value=1,
    max_value=10,
    value=3
)

if st.button("Shortlist"):
    if not job_description.strip():
        st.error("Please enter a job description.")
    else:
        results = search_resumes(job_description, top_k)

        st.subheader("Shortlisted Resumes")

        ids = results["ids"][0]
        metas = results["metadatas"][0]

        documents = results["documents"][0]
        metas = results["metadatas"][0]

        for i, meta in enumerate(metas):
            st.write(f"**{i+1}. Resume ID:** {meta['resume_id']}")
            st.divider()

            explanation = explain(  
                resume_text=documents[i],
                job_description=job_description
            )

            st.text(explanation)
            st.divider()