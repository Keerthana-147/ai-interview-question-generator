# app.py

import streamlit as st
from resume_parser import extract_text_from_pdf
from keyword_extractor import extract_keywords
from gemini_generator import generate_questions_with_openrouter  


# Streamlit App Title and Description
st.set_page_config(page_title="AI Interview Question Generator", layout="centered")
st.title("AI Interview Question Generator")
job_role = st.text_input("Enter the Job Role (e.g., Data Scientist, Backend Developer)")
st.markdown("Upload your **PDF resume** to get personalized interview questions using NLP + Gemini AI.")

# File Uploader
uploaded_file = st.file_uploader("📎 Upload Resume (PDF only)", type=["pdf"])


if uploaded_file:
    # Step 1: Extract Text
    with st.spinner(" Extracting text from your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
    st.success("Resume text extracted!")

    # Step 2: Extract Keywords
    with st.spinner(" Extracting keywords using spaCy..."):
        keywords = extract_keywords(resume_text)
    st.markdown(f"Top Keywords Extracted:** `{', '.join(keywords)}`")

    # Step 3: Generate Questions
    with st.spinner(" Generating interview questions..."):
       prompt = f"""You are an expert interviewer for the role of a {job_role}. Below are key skills and resume highlights:{keywords}Generate 5 personalized, role-specific, technically accurate interview questions. Each question should test the applicant's depth in the skill mentioned, and should be challenging but clear. Avoid generic questions. Format as a numbered list."""
       questions = generate_questions_with_openrouter(prompt)

    # Display Questions
    st.subheader("Generated Interview Questions")
    for i, q in enumerate(questions.split('\n'), 1):  # Gemini usually returns text block
        if q.strip():  # avoid empty lines
            st.markdown(f"{q.strip()}")

