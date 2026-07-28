from database.loader import insert_books


def save_books(books):
    """
    Save transformed books into PostgreSQL.
    """

    insert_books(books)