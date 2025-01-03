import re
import string

class TextUtils:
    @staticmethod
    def expand_contractions(text, contractions_dict):
        """Expands contractions in text based on the provided dictionary."""
        contractions_pattern = re.compile(
            '|'.join(re.escape(key) for key in contractions_dict.keys()),
            flags=re.IGNORECASE
        )

        def replace(match):
            matched_text = match.group(0)
            return contractions_dict.get(matched_text.lower(), matched_text)

        return contractions_pattern.sub(replace, text)

    @staticmethod
    def clean_text(text):
        """Cleans text by removing numbers and special characters."""
        text = re.sub(r"\d+", "", text)  # Remove numbers
        text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
        return text.strip()

    @staticmethod
    def read_file(file_path):
        """Reads a text file and returns its content."""
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def write_file(file_path, content):
        """Writes content to a text file."""
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
