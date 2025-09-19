import unittest

from core.index import build_index


class TestBuildIndex(unittest.TestCase):
    def test_returns_one_vector_per_document(self):
        documents = ["a b", "b c", "c"]
        _vocabulary, _idf, vectors = build_index(documents)
        self.assertEqual(len(vectors), len(documents))
        self.assertTrue(all(len(v) == len(_vocabulary) for v in vectors))

    def test_word_in_every_document_contributes_nothing(self):
        documents = ["common rare", "common only"]
        vocabulary, _idf, vectors = build_index(documents)
        self.assertEqual(vectors[0][vocabulary["common"]], 0.0)

    def test_rare_word_has_nonzero_weight_where_present(self):
        documents = ["common rare", "common only"]
        vocabulary, _idf, vectors = build_index(documents)
        self.assertGreater(vectors[0][vocabulary["rare"]], 0.0)
        self.assertEqual(vectors[1][vocabulary["rare"]], 0.0)


if __name__ == "__main__":
    unittest.main()
