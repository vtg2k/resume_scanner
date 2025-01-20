import spacy
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

def extract_skills(text):
    doc = nlp(text)
    skills = [token.text for token in doc if token.pos_ == "NOUN"]
    return set(skills)

resume_text = extract_text_from_pdf("sample_resume.pdf")
print("Extracted Skills:", extract_skills(resume_text))

def match_resume_to_job(resume_text, job_desc):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    similarity_score = cosine_similarity(vectors[0], vectors[1])
    return similarity_score[0][0]

resume_text = "Python, Machine Learning, Django, SQL"
job_desc = "Looking for a Python developer with experience in ML and Django."
score = match_resume_to_job(resume_text, job_desc)

print(f"Resume Match Score: {score:.2f}")
