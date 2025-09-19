import unittest

from core.vectorizer import build_vocabulary, compute_idf, create_tfidf_vector


class TestBuildVocabulary(unittest.TestCase):
    def test_assigns_unique_increasing_indices(self):
        vocabulary = build_vocabulary(["a b", "b c"])
        self.assertEqual(vocabulary, {"a": 0, "b": 1, "c": 2})

    def test_empty_documents_gives_empty_vocabulary(self):
        self.assertEqual(build_vocabulary([]), {})


class TestComputeIdf(unittest.TestCase):
    def test_word_in_every_document_gets_zero_idf(self):
        documents = ["a a b", "b c"]
        vocabulary = build_vocabulary(documents)
        idf = compute_idf(documents, vocabulary)
        self.assertEqual(idf[vocabulary["b"]], 0.0)

    def test_rarer_word_gets_higher_idf(self):
        documents = ["a a b", "b c"]
        vocabulary = build_vocabulary(documents)
        idf = compute_idf(documents, vocabulary)
        self.assertGreater(idf[vocabulary["a"]], idf[vocabulary["b"]])


class TestCreateTfidfVector(unittest.TestCase):
    def setUp(self):
        self.documents = ["a a b", "b c"]
        self.vocabulary = build_vocabulary(self.documents)
        self.idf = compute_idf(self.documents, self.vocabulary)

    def test_weights_by_term_frequency_and_idf(self):
        vector = create_tfidf_vector("a a b", self.vocabulary, self.idf)
        self.assertAlmostEqual(vector[self.vocabulary["a"]], 2 * self.idf[self.vocabulary["a"]])
        self.assertEqual(vector[self.vocabulary["b"]], 0.0)

    def test_ignores_words_outside_vocabulary(self):
        vector = create_tfidf_vector("a zzz", self.vocabulary, self.idf)
        self.assertEqual(len(vector), len(self.vocabulary))


if __name__ == "__main__":
    unittest.main()
