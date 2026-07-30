import json


FILE="output/books.jsonl"



def load_books():

    books=[]

    with open(
        FILE,
        encoding="utf-8"
    ) as f:

        for line in f:

            books.append(
                json.loads(line)
            )

    return books



def test_number_books():

    books=load_books()

    assert len(books)==8



def test_isbn_normalization():

    books=load_books()

    for book in books:

        assert "-" not in book["isbn"]



def test_duplicates():

    books=load_books()

    isbn=[
        b["isbn"]
        for b in books
    ]

    assert len(isbn)==len(set(isbn))