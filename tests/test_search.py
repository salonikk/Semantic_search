import unittest

from core.index import build_index
from core.search import cosine_similarity, search


class TestCosineSimilarity(unittest.TestCase):
    def test_identical_vectors_score_one(self):
        self.assertAlmostEqual(cosine_similarity([1, 2, 3], [1, 2, 3]), 1.0)

    def test_zero_vector_scores_zero(self):
        self.assertEqual(cosine_similarity([0, 0], [1, 2]), 0.0)


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.documents = [
            "python programming is fun",
            "data science is fun",
            "cooking is relaxing",
        ]
        self.vocabulary, self.idf, self.vectors = build_index(self.documents)

    def test_ranks_more_overlapping_document_first(self):
        results = search("python fun", self.documents, self.vocabulary, self.idf, self.vectors)
        self.assertEqual(results[0][1], "python programming is fun")

    def test_no_overlap_scores_zero(self):
        results = search("xyz", self.documents, self.vocabulary, self.idf, self.vectors)
        self.assertTrue(all(score == 0 for score, _ in results))

    def test_returns_one_result_per_document(self):
        results = search("fun", self.documents, self.vocabulary, self.idf, self.vectors)
        self.assertEqual(len(results), len(self.documents))


if __name__ == "__main__":
    unittest.main()
