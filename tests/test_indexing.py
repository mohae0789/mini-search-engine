import unittest

from src.indexing import (
    create_inverted_index,
    create_positional_index,
    create_biword_index
)


class TestIndexing(unittest.TestCase):

    def setUp(self):
        self.documents = {
            "doc1.txt": ["python", "is", "powerful"],
            "doc2.txt": ["python", "is", "useful"]
        }

    def test_inverted_index(self):
        result = create_inverted_index(self.documents)

        self.assertEqual(
            result["python"],
            {"doc1.txt", "doc2.txt"}
        )

    def test_positional_index(self):
        result = create_positional_index(self.documents)

        self.assertEqual(
            result["python"]["doc1.txt"],
            [0]
        )

    def test_biword_index(self):
        result = create_biword_index(self.documents)

        self.assertEqual(
            result["python is"],
            {"doc1.txt", "doc2.txt"}
        )


if __name__ == "__main__":
    unittest.main()
