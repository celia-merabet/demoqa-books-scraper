import json
import os


def export_jsonl(books, filename):

    os.makedirs(
        os.path.dirname(filename),
        exist_ok=True
    )


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:


        for book in books:

            file.write(
                json.dumps(
                    book.model_dump(),
                    ensure_ascii=False
                )
                + "\n"
            )