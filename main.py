#!/usr/bin/env python3
"""
Semantic Search Engine - Main Entry Point
"""

from core.tokenizer import tokenize

def main():
    """Main function to run the search engine."""
    print("🔍 Semantic Search Engine")
    print("=" * 30)
    
    # Test the tokenizer
    test_texts = [
        "Hello, world!",
        "Python programming is fun!",
        "Don't worry, be happy."
    ]
    
    for text in test_texts:
        tokens = tokenize(text)
        print(f"Text: '{text}'")
        print(f"Tokens: {tokens}")
        print()

if __name__ == "__main__":
    main()