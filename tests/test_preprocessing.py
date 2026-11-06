import unittest

from src.preprocessing import preprocess_documents


class TestPreprocessing(unittest.TestCase):

    def test_lowercase(self):
        documents = {
            "doc1.txt": "PYTHON PROGRAMMING"
        }

        result = preprocess_documents(documents)

        self.assertEqual(
            result["doc1.txt"],
            ["python", "programming"]
        )

    def test_remove_punctuation(self):
        documents = {
            "doc1.txt": "Hello, World!"
        }

        result = preprocess_documents(documents)

        self.assertEqual(
            result["doc1.txt"],
            ["hello", "world"]
        )

    def test_tokenization(self):
        documents = {
            "doc1.txt": "machine learning is useful"
        }

        result = preprocess_documents(documents)

        self.assertEqual(
            result["doc1.txt"],
            ["machine", "learning", "is", "useful"]
        )


if __name__ == "__main__":
    unittest.main()
