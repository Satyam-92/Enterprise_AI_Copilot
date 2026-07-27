from etl.transformer import transform_book
from etl.loader import save_to_csv, save_to_json
from database.loader import insert_books


def run_pipeline(book_list):
    """
    Run the ETL pipeline:
    Extracted Data -> Transform -> Load
    """

    transformed_books = []

    for book in book_list:
        transformed_book = transform_book(book)
        transformed_books.append(transformed_book)

    # Save to CSV
    save_to_csv(transformed_books)

    # Save to JSON
    save_to_json(transformed_books)

    # Save to PostgreSQL
    insert_books(transformed_books)

    return transformed_books