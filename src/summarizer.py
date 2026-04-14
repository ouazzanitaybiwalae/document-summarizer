from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def summarize_text(text, n_sentences=3):
    sentences = text.split('.')
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    
    scores = np.sum(X.toarray(), axis=1)
    ranked_sentences = np.argsort(scores)[-n_sentences:]
    
    summary = '. '.join([sentences[i] for i in sorted(ranked_sentences)])
    
    return summary