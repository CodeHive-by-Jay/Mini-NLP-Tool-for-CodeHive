# Mini NLP Toolkit

## Overview

The **Mini NLP Toolkit** is a lightweight package designed for basic natural language processing (NLP) tasks. It provides tools for tokenization, normalization, stopword removal, stemming, lemmatization, and file preprocessing. Additionally, it supports processing files of various formats including `.txt`, `.csv`, `.json`, `.docx`, and `.pdf`.

## Project Structure

```
Directory structure:
└── CodeHive-by-Jay-Mini-NLP-Tool-for-CodeHive/
    ├── README.md
    ├── LICENSE
    ├── requirements.txt
    ├── setup.py
    ├── tests/
    │   └── test_preprocess.py
    └── toolkit/
        ├── __init__.py
        ├── preprocess.py
        └── utils.py
```

### Key Directories and Files

- **`toolkit/`**: Contains the core functionality of the toolkit.
- **`README.md`**: Provides an overview of the package.
- **`requirements.txt`**: Lists dependencies required for the project.

## Features

### Class: `MiniNLPToolkit`

#### Methods

1. **`__init__`**
   Initializes the NLP toolkit by loading NLTK resources (stopwords, stemmer, lemmatizer).

2. **`tokenize(self, text)`**

   - Splits text into sentences and words.
   - **Input**: Raw text (string).
   - **Output**: Tuple of sentences (list) and words (list).

3. **`normalize(self, text)`**

   - Converts text to lowercase and removes punctuation.
   - **Input**: Raw text (string).
   - **Output**: Normalized text (string).

4. **`remove_stopwords(self, words)`**

   - Removes common stopwords from a list of words.
   - **Input**: List of words.
   - **Output**: List of filtered words.

5. **`stem(self, words)`**

   - Applies stemming to reduce words to their root forms.
   - **Input**: List of words.
   - **Output**: List of stemmed words.

6. **`lemmatize(self, words)`**

   - Applies lemmatization for better semantic understanding.
   - **Input**: List of words.
   - **Output**: List of lemmatized words.

7. **`preprocess(self, text)`**

   - Combines tokenization, normalization, stopword removal, and lemmatization into a single pipeline.
   - **Input**: Raw text (string).
   - **Output**: Processed text (string).

8. **`read_file(self, file_path)`**

   - Reads and extracts content from supported file formats.
   - **Input**: File path (string).
   - **Output**: File content (string).

9. **`process_file(self, input_folder, output_folder, file_name)`**

   - Processes a file, applies preprocessing, and saves the result to an output folder.
   - **Input**: Input folder path (string), output folder path (string), file name (string).
   - **Output**: Preprocessed file saved to `output_folder`.

### Class: `TextUtils`

#### Methods

1. **`expand_contractions(text, contractions_dict)`**

   - Expands contractions in text based on the provided dictionary.
   - **Input**: Text (string), contractions dictionary (dict).
   - **Output**: Text with expanded contractions (string).

2. **`clean_text(text)`**

   - Cleans text by removing numbers and special characters.
   - **Input**: Text (string).
   - **Output**: Cleaned text (string).

3. **`read_file(file_path)`**

   - Reads a text file and returns its content.
   - **Input**: File path (string).
   - **Output**: File content (string).

4. **`write_file(file_path, content)`**

   - Writes content to a text file.
   - **Input**: File path (string), content (string).
   - **Output**: None.

## Example Usage

### Example Script: `example_script.py`

The following script demonstrates how to use the **Mini NLP Toolkit** to preprocess text files.

```python
from toolkit import MiniNLPToolkit, TextUtils

toolkit = MiniNLPToolkit()
text_utils = TextUtils()

# Define input and output folders
input_folder = "data/sample_texts"
output_folder = "data/output"

# Specify the file to process
file_name = "sample1.txt"

# Process the file
toolkit.process_file(input_folder, output_folder, file_name)

# Example usage of TextUtils
text = "I'm learning NLP. It's fun!"
contractions_dict = {"i'm": "I am", "it's": "it is"}
expanded_text = text_utils.expand_contractions(text, contractions_dict)
print("Expanded Text:", expanded_text)

cleaned_text = text_utils.clean_text(expanded_text)
print("Cleaned Text:", cleaned_text)
```

**Sample Input**: `data/sample_texts/sample1.txt`

```
This is a sample text file. It contains several sentences, words, and punctuation.
```

**Sample Output**: `data/output/processed_sample1.txt`

```
sample text file contain several sentence word punctuation
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CodeHive-by-Jay/Mini-NLP-Tool-for-CodeHive
   ```
2. Navigate to the project directory:
   ```bash
   cd Mini-NLP-Tool-for-CodeHive
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Supported File Formats

- `.txt`: Plain text files.
- `.csv`: Comma-separated values files.
- `.json`: JSON files.
- `.docx`: Word documents.
- `.pdf`: PDF files.

## Future Enhancements

- Add support for additional file formats (e.g., `.xml`).
- Implement advanced NLP features like Named Entity Recognition (NER) and Part-of-Speech (POS) tagging.
- Provide a web interface for easier access.

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or suggestions, please contact the developer:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brayan-j4y/) 
[![Github](https://img.shields.io/badge/Github-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/brayanj4y/)
[![Instagram](https://img.shields# Mini NLP Toolkit

## Overview

The **Mini NLP Toolkit** is a lightweight package designed for basic natural language processing (NLP) tasks. It provides tools for tokenization, normalization, stopword removal, stemming, lemmatization, and file preprocessing. Additionally, it supports processing files of various formats including `.txt`, `.csv`, `.json`, `.docx`, and `.pdf`.

## Project Structure

```
Directory structure:
└── CodeHive-by-Jay-Mini-NLP-Tool-for-CodeHive/
    ├── README.md
    ├── LICENSE
    ├── requirements.txt
    ├── setup.py
    ├── tests/
    │   └── test_preprocess.py
    └── toolkit/
        ├── __init__.py
        ├── preprocess.py
        └── utils.py
```

### Key Directories and Files

- **`toolkit/`**: Contains the core functionality of the toolkit.
- **`README.md`**: Provides an overview of the package.
- **`requirements.txt`**: Lists dependencies required for the project.

## Features

### Class: `MiniNLPToolkit`

#### Methods

1. **`__init__`**
   Initializes the NLP toolkit by loading NLTK resources (stopwords, stemmer, lemmatizer).

2. **`tokenize(self, text)`**

   - Splits text into sentences and words.
   - **Input**: Raw text (string).
   - **Output**: Tuple of sentences (list) and words (list).

3. **`normalize(self, text)`**

   - Converts text to lowercase and removes punctuation.
   - **Input**: Raw text (string).
   - **Output**: Normalized text (string).

4. **`remove_stopwords(self, words)`**

   - Removes common stopwords from a list of words.
   - **Input**: List of words.
   - **Output**: List of filtered words.

5. **`stem(self, words)`**

   - Applies stemming to reduce words to their root forms.
   - **Input**: List of words.
   - **Output**: List of stemmed words.

6. **`lemmatize(self, words)`**

   - Applies lemmatization for better semantic understanding.
   - **Input**: List of words.
   - **Output**: List of lemmatized words.

7. **`preprocess(self, text)`**

   - Combines tokenization, normalization, stopword removal, and lemmatization into a single pipeline.
   - **Input**: Raw text (string).
   - **Output**: Processed text (string).

8. **`read_file(self, file_path)`**

   - Reads and extracts content from supported file formats.
   - **Input**: File path (string).
   - **Output**: File content (string).

9. **`process_file(self, input_folder, output_folder, file_name)`**

   - Processes a file, applies preprocessing, and saves the result to an output folder.
   - **Input**: Input folder path (string), output folder path (string), file name (string).
   - **Output**: Preprocessed file saved to `output_folder`.

### Class: `TextUtils`

#### Methods

1. **`expand_contractions(text, contractions_dict)`**

   - Expands contractions in text based on the provided dictionary.
   - **Input**: Text (string), contractions dictionary (dict).
   - **Output**: Text with expanded contractions (string).

2. **`clean_text(text)`**

   - Cleans text by removing numbers and special characters.
   - **Input**: Text (string).
   - **Output**: Cleaned text (string).

3. **`read_file(file_path)`**

   - Reads a text file and returns its content.
   - **Input**: File path (string).
   - **Output**: File content (string).

4. **`write_file(file_path, content)`**

   - Writes content to a text file.
   - **Input**: File path (string), content (string).
   - **Output**: None.

## Example Usage

### Example Script: `example_script.py`

The following script demonstrates how to use the **Mini NLP Toolkit** to preprocess text files.

```python
from toolkit import MiniNLPToolkit, TextUtils

toolkit = MiniNLPToolkit()
text_utils = TextUtils()

# Define input and output folders
input_folder = "data/sample_texts"
output_folder = "data/output"

# Specify the file to process
file_name = "sample1.txt"

# Process the file
toolkit.process_file(input_folder, output_folder, file_name)

# Example usage of TextUtils
text = "I'm learning NLP. It's fun!"
contractions_dict = {"i'm": "I am", "it's": "it is"}
expanded_text = text_utils.expand_contractions(text, contractions_dict)
print("Expanded Text:", expanded_text)

cleaned_text = text_utils.clean_text(expanded_text)
print("Cleaned Text:", cleaned_text)
```

**Sample Input**: `data/sample_texts/sample1.txt`

```
This is a sample text file. It contains several sentences, words, and punctuation.
```

**Sample Output**: `data/output/processed_sample1.txt`

```
sample text file contain several sentence word punctuation
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CodeHive-by-Jay/Mini-NLP-Tool-for-CodeHive
   ```
2. Navigate to the project directory:
   ```bash
   cd Mini-NLP-Tool-for-CodeHive
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Supported File Formats

- `.txt`: Plain text files.
- `.csv`: Comma-separated values files.
- `.json`: JSON files.
- `.docx`: Word documents.
- `.pdf`: PDF files.

## Future Enhancements

- Add support for additional file formats (e.g., `.xml`).
- Implement advanced NLP features like Named Entity Recognition (NER) and Part-of-Speech (POS) tagging.
- Provide a web interface for easier access.

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or suggestions, please contact the developer:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brayan-j4y/) 
[![Github](https://img.shields.io/badge/Github-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/brayanj4y/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/brayanj4y)  
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:souopsylvain@gmail.com) 
