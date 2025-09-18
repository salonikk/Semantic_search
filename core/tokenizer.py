from typing import List
import string

def tokenize(text: str, lowercase: bool = True, remove_punctuation: bool = True) -> List[str]:
    """
    Tokenize text into words.
    
    Args:
        text: Input text to tokenize
        lowercase: Whether to convert to lowercase
        remove_punctuation: Whether to remove punctuation
    
    Returns:
        List of tokens (words)
    """
    tokens = []
    for word in text.split():
        if lowercase:
            word = word.lower()
        if remove_punctuation:
            word = word.translate(str.maketrans('', '', string.punctuation))
        tokens.append(word)
    return tokens

if __name__ == "__main__":
    # Test cases for this specific module
    test_cases = [
        "Hello, world!",
        "Python programming is fun!",
        "Don't worry, be happy."
    ]

    for text in test_cases:
        tokens = tokenize(text)
        print(f"Text: '{text}'")
        print(f"Tokens: {tokens}")
        print()