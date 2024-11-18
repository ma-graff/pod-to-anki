### Basic initial testing counter for the frequency of words in a text file

import os
import string
from collections import Counter

# Function to read all text files from a directory
def load_transcriptions(directory):
    all_text = ""
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                all_text += file.read() + " "
    return all_text

# Function to preprocess text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Function to count word or phrase frequencies
def count_frequencies(text, phrase_length=1):
    words = text.split()
    if phrase_length == 1:
        return Counter(words)
    else:
        phrases = zip(*[words[i:] for i in range(phrase_length)])
        return Counter([" ".join(phrase) for phrase in phrases])

# Directory containing the transcription files
directory = "/Users/matt/Documents/GitHub/pod-to-anki/test_data/fr_CA"

# Load and preprocess the text
transcriptions = load_transcriptions(directory)
clean_text = preprocess_text(transcriptions)

# Count word frequencies
word_counts = count_frequencies(clean_text, phrase_length=1)  # Change phrase_length for multi-word phrases
ranked_words = word_counts.most_common()

# Save ranked words to a file
output_file = "word_rankings.txt"
with open(output_file, 'w', encoding='utf-8') as f:
    for word, count in ranked_words:
        f.write(f"{word}\t{count}\n")

print(f"Word rankings saved to {output_file}")
