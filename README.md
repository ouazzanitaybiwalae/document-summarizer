# Smart Document Summarizer (NLP + LLM)

## Overview

This project implements an intelligent document summarization system using Natural Language Processing (NLP) techniques and modern Large Language Models (LLMs).

It supports both:

* Extractive summarization (TF-IDF based)
* Abstractive summarization (LLM using transformers)

---

## Features

* Text preprocessing (cleaning, tokenization, stopwords removal)
* Document chunking for long texts
* Extractive summarization using TF-IDF
* Abstractive summarization using transformer models
* Modular and extensible architecture

---

## How It Works

1. Load input text
2. Clean and preprocess the data
3. Split long text into chunks
4. Apply summarization:

   * TF-IDF (extractive)
   * LLM (abstractive)
5. Merge results into final summary

---

## Project Structure

document-summarizer/
│
├── data/
│   └── sample.txt
│
├── src/
│   ├── preprocess.py
│   ├── summarizer.py
│   ├── summarizer_llm.py
│   ├── utils.py
│
├── main.py
├── requirements.txt
├── README.md

---

## Installation

```bash
git clone <your-repo-link>
cd document-summarizer
pip install -r requirements.txt
```

---

## Usage

1. Add your text file inside the `data/` folder (e.g., `sample.txt`)
2. Run the project:

```bash
python main.py
```

3. You will get two outputs:

* TF-IDF Summary
* LLM Summary

---

## Example Use Cases

* Summarizing academic articles
* Processing long reports
* Extracting key ideas from documents
* Text compression for faster reading

---

## Technologies Used

* Python
* NLTK
* Scikit-learn
* Transformers (Hugging Face)
* NumPy

---

## Future Improvements

* Support for PDF and DOCX files
* Web interface (Streamlit)
* Integration with LLM APIs (OpenAI, etc.)
* Performance optimization

---

## Notes

* LLM summarization uses a pre-trained transformer model
* Long texts are automatically split into smaller chunks

---

## Author

Engineering student in Artificial Intelligence & Data Science
Passionate about NLP, LLMs, and intelligent systems
