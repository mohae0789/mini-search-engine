from src.data_loader import load_documents
from src.preprocessing import preprocess_documents

from src.indexing import (
    create_inverted_index,
    create_positional_index,
    create_biword_index
)

from src.search import (
    biword_query,
    phrase_query,
    proximity_query
)

from src.ranking import (
    calculate_tf,
    calculate_query_score,
    rank_results,
    calculate_idf,
    calculate_tfidf,
    calculate_tfidf_score
)


def main():

    # Load Documents
    documents_folder = "documents"
    documents = load_documents(documents_folder)

    # Preprocessing
    documents = preprocess_documents(documents)

    # Create Indexes
    inverted_index = create_inverted_index(documents)
    positional_index = create_positional_index(documents)
    biword_index = create_biword_index(documents)

    # Display Indexes
    print("\nInverted Index:")
    print(inverted_index)

    print("\nPositional Index:")
    print(positional_index)

    print("\nBiword Index:")
    print(biword_index)

    # Search
    biword_query("machine learning", biword_index)
    phrase_query("python is", positional_index)
    proximity_query("python", "language", 3, positional_index)

    # Ranking
    print("\nTF:")
    print(calculate_tf("learning", documents))

    print("\nQuery Score:")
    print(calculate_query_score("python learning", documents))

    print("\nRanked Results:")
    print(rank_results("python learning", documents))

    print("\nIDF:")
    print(calculate_idf("python", documents))

    print("\nTF-IDF:")
    print(calculate_tfidf("python", "doc1.txt", documents))

    print("\nTF-IDF Ranking:")
    print(calculate_tfidf_score("python learning", documents))


if __name__ == "__main__":
    main()
