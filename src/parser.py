from models import Book


def normalize_isbn(isbn):

    return isbn.replace("-", "").strip()



def normalize_pages(pages):

    if isinstance(pages, int):
        return pages

    return int(
        str(pages)
        .replace("pages", "")
        .strip()
    )



def parse_books(data):

    books = []

    for item in data["books"]:

        book = Book(

            isbn=normalize_isbn(
                item.get("isbn", "")
            ),

            title=item.get(
                "title",
                ""
            ).strip(),

            author=item.get(
                "author",
                ""
            ).strip(),

            publisher=item.get(
                "publisher",
                ""
            ).strip(),

            pages=normalize_pages(
                item.get("pages",0)
            ),

            url="https://demoqa.com/books"

        )

        books.append(book)


    return books