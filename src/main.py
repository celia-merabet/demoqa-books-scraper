from scraper import fetch_books
from parser import parse_books
from exporter import export_jsonl
from config import OUTPUT_FILE, MAX_BOOKS
from logger import setup_logger



def main():

    logger = setup_logger()


    logger.info(
        "Début de la collecte DemoQA Books"
    )


    data = fetch_books()


    books = parse_books(data)


    books = books[:MAX_BOOKS]


    logger.info(
        f"{len(books)} livres récupérés"
    )


    export_jsonl(
        books,
        OUTPUT_FILE
    )


    logger.info(
        f"Export terminé : {OUTPUT_FILE}"
    )



if __name__ == "__main__":

    main()