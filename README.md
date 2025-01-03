# Mini NLP Toolkit Documentation

## Overview

The **Mini NLP Toolkit** is a lightweight package designed for basic natural language processing (NLP) tasks. It provides tools for tokenization, normalization, stopword removal, stemming, lemmatization, and file preprocessing. Additionally, it supports processing files of various formats including `.txt`, `.csv`, `.json`, `.docx`, and `.pdf`.

## Project Structure

```
mini-nlp-toolkit/
├── README.md
├── requirements.txt
├── setup.py
├── toolkit/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── utils.py
├── examples/
│   ├── example_script.py
│   ├── sample_texts/
│       ├── sample1.txt
│       ├── sample2.txt
├── data/
│   ├── output/
└── .gitignore
```

### Key Directories and Files

- **`toolkit/`**: Contains the core functionality of the toolkit.
- **`examples/`**: Demonstrates how to use the package.
- **`data/`**: Stores input files (`sample_texts/`) and output files (`output/`).
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


## Example Usage

### Example Script: `example_script.py`

The following script demonstrates how to use the **Mini NLP Toolkit** to preprocess text files.

```python
from toolkit import MiniNLPToolkit

toolkit = MiniNLPToolkit()

# Define input and output folders
input_folder = "data/sample_texts"
output_folder = "data/output"

# Specify the file to process
file_name = "sample1.txt"

# Process the file
toolkit.process_file(input_folder, output_folder, file_name)
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

- `.``txt`: Plain text files.
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

For questions or suggestions, please contact:
**Souop Silvain Brayan**

- Email: [souopsylvain@gmail.com](mailto\:souopsylvain@gmail.com)
- GitHub[: ](https://github.com/brayanj4y)[brayanj4y](https://github.com/brayanj4y)
- LinkedIn[: ](https://linkedin.com/in/brayan-j4y)[brayan-j4y](https://linkedin.com/in/brayan-j4y)

