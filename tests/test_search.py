import unittest
from unittest.mock import patch

from src.search import (
    biword_query,
    phrase_query,
    proximity_query
)

from src.indexing import (
    create_positional_index,
    create_biword_index
)


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.documents = {
            "doc1.txt": ["python", "is", "a", "powerful", "language"],
            "doc2.txt": ["machine", "learning", "uses", "python"]
        }

        self.positional_index = create_positional_index(self.documents)
        self.biword_index = create_biword_index(self.documents)

    def test_biword_query(self):
        with patch("builtins.print") as mock_print:
            biword_query("machine learning", self.biword_index)

            mock_print.assert_called_with(
                "Search Results:", {"doc2.txt"}
            )

    def test_phrase_query(self):
        with patch("builtins.print") as mock_print:
            phrase_query("python is", self.positional_index)

            mock_print.assert_any_call(
                "Phrase found in:", "doc1.txt"
            )

    def test_proximity_query(self):
        with patch("builtins.print") as mock_print:
            proximity_query(
                "python",
                "language",
                4,
                self.positional_index
            )

            mock_print.assert_any_call(
                "Proximity found in:", "doc1.txt"
            )


if __name__ == "__main__":
    unittest.main()
