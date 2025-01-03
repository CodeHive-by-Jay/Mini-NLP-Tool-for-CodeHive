from setuptools import setup, find_packages

setup(
    name="mini-nlp-toolkit",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "nltk",
        "spacy",
    ],
    description="A compact toolkit for basic NLP preprocessing tasks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/mini-nlp-toolkit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
