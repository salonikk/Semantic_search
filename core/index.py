from typing import Dict, List, Tuple

from core.vectorizer import build_vocabulary, compute_idf, create_tfidf_vector

def build_index(documents: List[str]) -> Tuple[Dict[str, int], List[float], List[List[float]]]:
    """
    Build a vocabulary, per-word IDF, and one TF-IDF vector per document.
    """
    vocabulary = build_vocabulary(documents)
    idf = compute_idf(documents, vocabulary)
    vectors = [create_tfidf_vector(document, vocabulary, idf) for document in documents]
    return vocabulary, idf, vectors