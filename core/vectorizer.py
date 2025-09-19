import math
from typing import Dict, List
from core.tokenizer import tokenize

def build_vocabulary(documents: List[str]) -> Dict[str, int]:
    """
    Build vocabulary from a list of documents.

    Args:
        documents: List of document texts

    Returns:
        Dictionary mapping word -> index
    """
    vocabulary = {}
    for document in documents:
        for word in tokenize(document):
            if word not in vocabulary:
                vocabulary[word] = len(vocabulary)
    return vocabulary

def compute_idf(documents: List[str], vocabulary: Dict[str, int]) -> List[float]:
    """
    Compute inverse document frequency for each word in the vocabulary:
    idf(word) = log(num_documents / num_documents_containing_word).
    """
    document_frequency = [0] * len(vocabulary)
    for document in documents:
        for word in set(tokenize(document)):
            if word in vocabulary:
                document_frequency[vocabulary[word]] += 1

    num_documents = len(documents)
    return [math.log(num_documents / df) for df in document_frequency]

def create_tfidf_vector(document: str, vocabulary: Dict[str, int], idf: List[float]) -> List[float]:
    """
    Create a TF-IDF vector for a single document: raw term frequency weighted
    by how rare each word is across the corpus.

    Args:
        document: Document text
        vocabulary: Word -> index mapping
        idf: Inverse document frequency per word, aligned to vocabulary indices

    Returns:
        TF-IDF vector
    """
    term_frequency = [0] * len(vocabulary)
    for word in tokenize(document):
        if word in vocabulary:
            term_frequency[vocabulary[word]] += 1
    return [count * idf[index] for index, count in enumerate(term_frequency)]