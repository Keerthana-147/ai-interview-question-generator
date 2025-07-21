#  AI Interview Question Generator

Generate personalized interview questions from a resume using **NLP** and **Gemini AI**.

---

##  Features

-  Upload resume (PDF)
-  Extracts keywords using `spaCy`
-  Generates interview questions using Gemini via OpenRouter API
-  Built with `Streamlit` for a simple web UI

---

##  Tech Stack

- Python 
- Streamlit
- spaCy (NLP)
- OpenRouter (Gemini API wrapper)

---

## Project Structure

ai-interview-question-generator/
- app.py # Streamlit app
- resume_parser.py # Extract text from PDF
- keyword_extractor.py # NLP keyword extraction
- gemini_generator.py # Gemini/OpenRouter API integration
- requirements.txt # All dependencies



