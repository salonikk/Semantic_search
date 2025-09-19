#!/usr/bin/env python3
"""
Semantic Search Engine - Main Entry Point
"""

from core.index import build_index
from core.search import search


def main():
    """Load the sample documents and rank them for each query."""
    print("Semantic Search Engine")
    print("=" * 30)

    with open("data/sample_docs.txt") as f:
        documents = [line.strip() for line in f if line.strip()]

    vocabulary, idf, vectors = build_index(documents)

    query = input("Query> ").strip()
    while query:
        for score, document in search(query, documents, vocabulary, idf, vectors):
            print(f"{score}\t{document}")
        print()
        query = input("Query> ").strip()


if __name__ == "__main__":
    main()
