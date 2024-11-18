import os
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Function to load all text files from a directory
def load_transcriptions(directory):
    transcriptions = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                transcriptions.append(file.read())
    return transcriptions

# Function to preprocess text
def preprocess_text(text):
    # Convert to lowercase and remove punctuation
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    return text

# Function to rank terms using TF-IDF
def rank_terms(documents, max_features=100, ngram_range=(1, 1)):
    vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=ngram_range, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.sum(axis=0).A1  # Sum weights across all documents
    term_scores = list(zip(feature_names, scores))
    ranked_terms = sorted(term_scores, key=lambda x: x[1], reverse=True)
    return ranked_terms

# Directory containing the transcription files
directory = "/Users/matt/Documents/GitHub/pod-to-anki/test_data/fr_CA"

# Load, preprocess, and vectorize the transcriptions
transcriptions = load_transcriptions(directory)
processed_texts = [preprocess_text(doc) for doc in transcriptions]

# Rank words (or phrases) using TF-IDF
ranked_terms = rank_terms(processed_texts, max_features=200, ngram_range=(1, 2))  # Adjust max_features and ngram_range as needed

# Save ranked terms to a file
output_file = "ranked_terms_tfidf.txt"
with open(output_file, 'w', encoding='utf-8') as f:
    for term, score in ranked_terms:
        f.write(f"{term}\t{score:.4f}\n")

print(f"Ranked terms saved to {output_file}")
