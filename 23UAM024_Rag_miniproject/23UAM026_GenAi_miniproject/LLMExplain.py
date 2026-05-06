from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()

llm = init_chat_model(
    model = "llama-3.3-70b-versatile",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("GROQ_API_KEY")
)

def explain(resume_text, job_description):
    prompt = f"""
    You are an HR assistant.

    Read the RESUME and JOB DESCRIPTION carefully.

    IMPORTANT FORMATTING RULES (must follow strictly):
    - Each section MUST start on a new line
    - Do NOT put Name, Summary, and Reason on the same line
    - Leave ONE blank line between sections
    - Do NOT add extra text outside the format

    OUTPUT FORMAT (follow exactly):

    Name:
    <candidate name>

    Summary:
    <2–4 lines professional summary>

    Reason:
    <clear reason for selection>

    "do not show job description or resume in the final output"
    JOB DESCRIPTION:
    {job_description}

    RESUME:
    {resume_text}
    """


    response = llm.invoke(prompt)
    return response.content