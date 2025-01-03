import os
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string
import re
import pandas as pd
from docx import Document
import json
from PyPDF2 import PdfReader

# Ensure necessary NLTK resources are downloaded
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

class MiniNLPToolkit:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def tokenize(self, text):
        """Tokenizes text into sentences and words."""
        sentences = sent_tokenize(text)
        words = word_tokenize(text)
        return sentences, words

    def normalize(self, text):
        """Normalizes text by converting to lowercase and removing punctuation."""
        text = text.lower()
        text = re.sub(f"[{string.punctuation}]", "", text)
        return text

    def remove_stopwords(self, words):
        """Removes stopwords from a list of words."""
        return [word for word in words if word.lower() not in self.stop_words]

    def stem(self, words):
        """Applies stemming to a list of words."""
        return [self.stemmer.stem(word) for word in words]

    def lemmatize(self, words):
        """Applies lemmatization to a list of words."""
        return [self.lemmatizer.lemmatize(word) for word in words]

    def preprocess(self, text):
        """Applies the full preprocessing pipeline to the text."""
        # Tokenize
        _, words = self.tokenize(text)
        # Normalize
        normalized_text = self.normalize(" ".join(words))
        # Remove stopwords
        filtered_words = self.remove_stopwords(normalized_text.split())
        # Lemmatize words
        lemmatized_words = self.lemmatize(filtered_words)
        return " ".join(lemmatized_words)

    def read_file(self, file_path):
        """Reads content from a supported file type."""
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        elif file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
            return " ".join(df.astype(str).values.flatten())
        elif file_path.endswith(".json"):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return json.dumps(data)
        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            return " ".join([p.text for p in doc.paragraphs])
        elif file_path.endswith(".pdf"):
            reader = PdfReader(file_path)
            return " ".join([page.extract_text() for page in reader.pages])
        else:
            raise ValueError("Unsupported file format. Supported formats are: .txt, .csv, .json, .docx, .pdf")

    def process_file(self, input_folder, output_folder, file_name):
        """Processes a file from input_folder and saves the result to output_folder."""
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, f"processed_{file_name}")

        # Ensure output folder exists
        os.makedirs(output_folder, exist_ok=True)

        try:
            # Read the file
            raw_text = self.read_file(input_path)
            # Preprocess the text
            processed_text = self.preprocess(raw_text)
            # Write to output
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(processed_text)
            print(f"Processed file saved to: {output_path}")
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found in '{input_folder}'")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    toolkit = MiniNLPToolkit()
    
    # Define folders
    input_folder = "sample_texts"
    output_folder = "sample_texts"

    # Get user input for file name
    file_name = input("Enter the name of the file to process (e.g., sample1.txt): ")
    
    # Process the file
    toolkit.process_file(input_folder, output_folder, file_name)
