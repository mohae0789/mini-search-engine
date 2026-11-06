import unittest

from src.ranking import (
    calculate_tf,
    calculate_query_score,
    rank_results,
    calculate_idf,
    calculate_tfidf,
    calculate_tfidf_score
)


class TestRanking(unittest.TestCase):

    def setUp(self):
        self.documents = {
            "doc1.txt": ["python", "is", "powerful", "python"],
            "doc2.txt": ["machine", "learning", "uses", "python"],
            "doc3.txt": ["information", "retrieval", "is", "important"]
        }

    def test_calculate_tf(self):
        result = calculate_tf("python", self.documents)

        self.assertEqual(
            result,
            {"doc1.txt": 2, "doc2.txt": 1}
        )

    def test_calculate_query_score(self):
        result = calculate_query_score(
            "python learning",
            self.documents
        )

        self.assertEqual(
            result,
            {"doc1.txt": 2, "doc2.txt": 2}
        )

    def test_rank_results(self):
        result = rank_results("python", self.documents)

        self.assertEqual(result[0][0], "doc1.txt")
        self.assertEqual(result[0][1], 2)

    def test_calculate_idf(self):
        result = calculate_idf("python", self.documents)

        self.assertAlmostEqual(result, 0.405465, places=5)

    def test_calculate_tfidf(self):
        result = calculate_tfidf(
            "python",
            "doc1.txt",
            self.documents
        )

        self.assertAlmostEqual(result, 0.810930, places=5)

    def test_calculate_tfidf_score(self):
        result = calculate_tfidf_score(
            "python learning",
            self.documents
        )

        self.assertEqual(result[0][0], "doc2.txt")


if __name__ == "__main__":
    unittest.main()
