# keyword_extractor.py
import spacy

# Load English model (download once using: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    keywords = []

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop and token.is_alpha:
            keywords.append(token.lemma_.lower())

    # Return top unique 10 keywords
    keywords = list(set(keywords))
    return keywords[:10]
