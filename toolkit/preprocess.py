import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string
import re

# Ensure necessary NLTK resources are downloaded
nltk_resources = ["punkt", "stopwords", "wordnet"]
for resource in nltk_resources:
    try:
        nltk.data.find(f"tokenizers/{resource}") if resource == "punkt" else nltk.data.find(f"corpora/{resource}")
    except LookupError:
        nltk.download(resource)

class MiniNLPToolkit:
    def __init__(self):
        try:
            self.stop_words = set(stopwords.words("english"))
        except LookupError:
            raise RuntimeError("NLTK stopwords resource not found. Run `nltk.download('stopwords')`.")
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def tokenize(self, text):
        """Tokenizes text into sentences and words."""
        if not text:
            raise ValueError("Input text cannot be empty.")
        sentences = sent_tokenize(text)
        words = word_tokenize(text)
        return sentences, words

    def normalize(self, text):
        """Normalizes text by converting to lowercase and removing punctuation."""
        if not text:
            raise ValueError("Input text cannot be empty.")
        text = text.lower()
        text = re.sub(f"[{string.punctuation}]", "", text)
        return text

    def remove_stopwords(self, words):
        """Removes stopwords from a list of words."""
        if not words:
            raise ValueError("Input word list cannot be empty.")
        return [word for word in words if word.lower() not in self.stop_words]

    def stem(self, words):
        """Applies stemming to a list of words."""
        if not words:
            raise ValueError("Input word list cannot be empty.")
        return [self.stemmer.stem(word) for word in words]

    def lemmatize(self, words):
        """Applies lemmatization to a list of words."""
        if not words:
            raise ValueError("Input word list cannot be empty.")
        return [self.lemmatizer.lemmatize(word) for word in words]

    def preprocess(self, text):
        """Applies the full preprocessing pipeline to the text."""
        if not text:
            raise ValueError("Input text cannot be empty.")
        try:
            _, words = self.tokenize(text)
            normalized_text = self.normalize(" ".join(words))
            filtered_words = self.remove_stopwords(normalized_text.split())
            lemmatized_words = self.lemmatize(filtered_words)
            return " ".join(lemmatized_words)
        except Exception as e:
            raise RuntimeError(f"Preprocessing failed: {str(e)}")
