import re
import string

class TextUtils:
    @staticmethod
    def expand_contractions(text, contractions_dict):
        """Expands contractions in text based on the provided dictionary."""
        if not text or not contractions_dict:
            raise ValueError("Input text and contractions dictionary cannot be empty.")
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
        if not text:
            raise ValueError("Input text cannot be empty.")
        text = re.sub(r"\d+", "", text)  # Remove numbers
        text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
        return text.strip()

    @staticmethod
    def read_file(file_path):
        """Reads a text file and returns its content."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except IOError as e:
            raise IOError(f"Error reading file {file_path}: {str(e)}")

    @staticmethod
    def write_file(file_path, content):
        """Writes content to a text file."""
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
        except IOError as e:
            raise IOError(f"Error writing to file {file_path}: {str(e)}")
