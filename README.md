AI-Powered Resume Screener

🚀 Project Overview

The AI Resume Screener is a machine learning-based application that automates resume screening by matching candidates' resumes with job descriptions. It ranks resumes based on relevance using NLP techniques and provides a streamlined dashboard for HR professionals.

📌 Features

Resume Parsing: Extracts text from PDF/DOCX resumes

Skill Extraction: Identifies key skills using NLP (SpaCy, NLTK)

Job Matching: Compares resumes with job descriptions using TF-IDF & Cosine Similarity

REST API: Upload and process resumes via Flask

Database Integration: Store and retrieve resumes using MongoDB/PostgreSQL

Frontend Dashboard: View ranked resumes using Streamlit

🛠 Tech Stack

Backend: Python, Flask

Machine Learning: Scikit-Learn, SpaCy, NLTK

Database: MongoDB / PostgreSQL

Frontend: Streamlit / React.js (Optional)

📂 Project Structure

resume_screener/
├── backend/
│   ├── app.py (Flask API)
│   ├── resume_parser.py (Extract text & skills)
│   ├── job_matcher.py (TF-IDF similarity)
│   ├── requirements.txt
│
├── frontend/
│   ├── dashboard.py (Streamlit UI)
│   ├── templates/
│
├── data/
│   ├── sample_resumes/ (Test resumes)
│   ├── job_descriptions/ (Example JDs)
│
└── README.md

📥 Installation & Setup

Clone the Repository

--bash
git clone https://github.com/vtg2k/resume_scanner.git
cd resume-screener

Set Up Virtual Environment

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

Install Dependencies

pip install -r requirements.txt

Run the Flask API

cd backend
python app.py

Launch the Frontend (Optional)

cd frontend
streamlit run dashboard.py

🔥 Usage

Upload a resume (PDF/DOCX) via the API or frontend

The system extracts skills, experience, and job titles

Compares with job descriptions and ranks resumes

View results in the HR dashboard

📌 Future Enhancements

Integrate GPT/BERT for smarter text understanding

Automated Email Alerts for shortlisted candidates

GraphQL API for better scalability
