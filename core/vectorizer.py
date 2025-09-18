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

def create_binary_bow(document: str, vocabulary: Dict[str, int]) -> List[int]:
    """
    Create binary Bag-of-Words vector for a single document.
    
    Args:
        document: Document text
        vocabulary: Word -> index mapping
        
    Returns:
        Binary vector (1 if word present, 0 if absent)
    """
    vector = [0] * len(vocabulary)
    for word in tokenize(document):
        if word in vocabulary:
            vector[vocabulary[word]] = 1
    return vector