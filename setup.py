from setuptools import setup, find_packages
try:
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "A compact toolkit for basic NLP preprocessing tasks."
setup(
    name="mini-nlp-toolkit",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "nltk",
        "spacy",
        "pandas",
        "python-docx",
        "PyPDF2",
    ],
    description="A compact toolkit for basic NLP preprocessing tasks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Souop Silvain Brayan",
    author_email="souopsylvain@gmail.com",
    url="https://github.com/CodeHive-by-Jay/Mini-NLP-Tool-for-CodeHive",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    keywords="nlp preprocessing text tokenization stopwords stemming lemmatization",
)
