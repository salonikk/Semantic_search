import math
from typing import Dict, List, Tuple

from core.vectorizer import create_tfidf_vector

def cosine_similarity(vector_a: List[float], vector_b: List[float]) -> float:
    """
    Cosine of the angle between two vectors: 1.0 means identical direction,
    0.0 means no overlap. Using cosine instead of a raw dot product keeps
    long documents from winning purely by having more words.
    """
    norm_a = math.sqrt(sum(a * a for a in vector_a))
    norm_b = math.sqrt(sum(b * b for b in vector_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0

    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    return dot_product / (norm_a * norm_b)

def search(
    query: str,
    documents: List[str],
    vocabulary: Dict[str, int],
    idf: List[float],
    vectors: List[List[float]],
) -> List[Tuple[float, str]]:
    """
    Rank documents by cosine similarity between TF-IDF vectors.
    """
    query_vector = create_tfidf_vector(query, vocabulary, idf)
    scored = [
        (cosine_similarity(query_vector, vector), document)
        for document, vector in zip(documents, vectors)
    ]

    scored.sort(reverse=True)
    return scored