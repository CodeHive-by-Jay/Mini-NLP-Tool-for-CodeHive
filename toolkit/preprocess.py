import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string
import re

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
