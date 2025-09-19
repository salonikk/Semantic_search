# Semantic Search

A from-scratch search engine built to understand how search ranking works under the hood, starting from binary bag-of-words.

## Run it

```
python3 main.py
```

Type a query at the `Query>` prompt and press Enter. Press Enter on an empty line to exit.

Documents come from `data/sample_docs.txt`, one document per line.

## Run the tests

```
python3 -m unittest discover -s tests
```

## How it works

- `core/tokenizer.py` — splits text into lowercase, punctuation-free tokens.
- `core/vectorizer.py` — builds a vocabulary (word -> index) and turns a document into a binary bag-of-words vector (1 if the word is present, 0 otherwise).
- `core/index.py` — builds the vocabulary and one vector per document.
- `core/search.py` — turns the query into a vector the same way, then ranks documents by how many query words they share.
