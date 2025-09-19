import unittest

from core.tokenizer import tokenize


class TestTokenize(unittest.TestCase):
    def test_lowercases_by_default(self):
        self.assertEqual(tokenize("Hello World"), ["hello", "world"])

    def test_strips_punctuation_by_default(self):
        self.assertEqual(tokenize("Hello, world!"), ["hello", "world"])

    def test_apostrophe_is_removed_not_split(self):
        self.assertEqual(tokenize("Don't worry"), ["dont", "worry"])

    def test_lowercase_false_keeps_case(self):
        self.assertEqual(tokenize("Hello World", lowercase=False), ["Hello", "World"])

    def test_remove_punctuation_false_keeps_punctuation(self):
        self.assertEqual(
            tokenize("Hello, world!", remove_punctuation=False),
            ["hello,", "world!"],
        )

    def test_empty_string_returns_empty_list(self):
        self.assertEqual(tokenize(""), [])


if __name__ == "__main__":
    unittest.main()
