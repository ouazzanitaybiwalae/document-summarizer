from src.preprocess import clean_text
from src.summarizer import summarize_text
from src.summarizer_llm import summarize_with_llm

text = open("data/sample.txt").read()

cleaned = clean_text(text)

# Méthode 1 (classique)
summary_tfidf = summarize_text(cleaned)

# Méthode 2 (LLM)
summary_llm = summarize_with_llm(text)

print("\n=== TF-IDF SUMMARY ===\n")
print(summary_tfidf)

print("\n=== LLM SUMMARY ===\n")
print(summary_llm)