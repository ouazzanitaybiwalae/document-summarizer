from transformers import pipeline

# Charger le modèle une seule fois
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_with_llm(text, max_length=130, min_length=30):
    # éviter les textes trop longs (important)
    text = text[:1000]
    
    summary = summarizer(text, 
                         max_length=max_length, 
                         min_length=min_length, 
                         do_sample=False)
    
    return summary[0]['summary_text']

from utils import split_text

def summarize_long_text(text):
    chunks = split_text(text)
    summaries = []
    
    for chunk in chunks:
        summaries.append(summarize_with_llm(chunk))
    
    return " ".join(summaries)