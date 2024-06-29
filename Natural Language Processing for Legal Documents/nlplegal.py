import spacy
import re
from transformers import pipeline

# Load models
nlp = spacy.load("en_core_web_sm")
summarizer = pipeline("summarization")

def preprocess(text):
    doc = nlp(text)
    return doc

def extract_entities(doc):
    return [(ent.text, ent.label_) for ent in doc.ents]

def extract_clauses(text, clause_type):
    patterns = {
        "confidentiality": r"(confidentiality|non-disclosure)[^\.\n]*\.",
        "termination": r"(termination|end of agreement)[^\.\n]*\."
    }
    pattern = patterns.get(clause_type, r"[^\.\n]*\.")
    clauses = re.findall(pattern, text, flags=re.IGNORECASE)
    return clauses

def generate_summary(text):
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Input your legal document text here
text = """
This Agreement is made and entered into as of the Effective Date by and between the parties. 
1. Confidentiality: The parties agree to maintain in confidence and not to disclose any Confidential Information to any third party.
2. Termination: This Agreement may be terminated by either party upon thirty (30) days written notice to the other party.
"""

# Preprocess
processed_text = preprocess(text)

# Extract entities
entities = extract_entities(processed_text)

# Extract clauses
confidentiality_clauses = extract_clauses(text, "confidentiality")
termination_clauses = extract_clauses(text, "termination")

# Generate summary
summary = generate_summary(text)

# Display results
print("Entities:", entities)
print("Confidentiality Clauses:", confidentiality_clauses)
print("Termination Clauses:", termination_clauses)
print("Summary:", summary)
