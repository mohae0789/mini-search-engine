# Mini Search Engine

A simple search engine built with Python as an educational Information Retrieval project.

## Project Overview

This project demonstrates the fundamental concepts of Information Retrieval (IR), including text preprocessing, indexing, searching, and document ranking.

## Features

- **Text Preprocessing:** Lowercase conversion, punctuation removal, and tokenization.
- **Inverted Index:** Maps each term to the documents containing it.
- **Positional Index:** Stores the positions of terms in documents.
- **Biword Index:** Stores consecutive word pairs.
- **Biword Search:** Searches using consecutive word pairs.
- **Phrase Search:** Finds exact phrases in documents.
- **Proximity Search:** Finds terms within a specified distance.
- **TF Ranking:** Ranks documents based on term frequency.
- **TF-IDF Ranking:** Ranks documents based on term importance.

## Project Structure

```text
mini-search-engine/
├── documents/
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── indexing.py
│   ├── search.py
│   └── ranking.py
├── tests/
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── test_indexing.py
│   ├── test_search.py
│   └── test_ranking.py
├── main.py
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.8 or higher.

No external libraries are currently required.

## How to Run

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd mini-search-engine
```

3. Run the project:

```bash
python main.py
```

## Run Tests

Run all unit tests using:

```bash
python -m unittest discover -s tests -v
```

## Concepts Learned

- Information Retrieval
- Text Processing
- Inverted Indexing
- Positional Indexing
- Biword Indexing
- Phrase and Proximity Queries
- Term Frequency (TF)
- Inverse Document Frequency (IDF)
- TF-IDF Ranking
- Unit Testing
- Modular Python Project Structure

## Future Improvements

- Build a graphical interface using Streamlit.
- Improve search result ranking.
- Add more test cases.
- Support larger document collections.

## Author

Your Name
Mohamed Ahmed Mohamed
