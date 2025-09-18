DOCS = ["hello", "hey" ,"chocolate", "candy", "happy", "christmas"]


def run_cli():
    print("Semantic search (toy) -- ready")
    q = input("Query> ")
    while q != "":
        print(q)
        q = input("Query> ")
    


if __name__ == "__main__":
    run_cli()
