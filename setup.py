from setuptools import setup, find_packages

setup(
    name="MiniNLPToolkit",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "nltk",
        "spacy",
        "pandas",
        "python-docx",
        "PyPDF2"
    ],
    description="A compact toolkit for basic NLP preprocessing tasks.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Souop Silvain Brayan",
    author_email="souopsylvain@gmail.com",
    url="https://github.com/CodeHive-by-Jay/Mini-NLP-Tool-for-CodeHive",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic"
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "mininlp=MiniNLPToolkit.main:run",  # Assuming there's a main entry point to the package
        ]
    },
    include_package_data=True,
    keywords="nlp preprocessing text tokenization stopwords stemming lemmatization",
)
