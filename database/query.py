from database.db import get_connection


def get_all_books():
    """
    Fetch all books from PostgreSQL.
    """

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT id, title, price, rating, availability
    FROM books
    ORDER BY id;
    """

    cursor.execute(query)

    books = cursor.fetchall()

    cursor.close()
    conn.close()

    return books


if __name__ == "__main__":

    books = get_all_books()

    print("=" * 80)
    print("BOOKS IN DATABASE")
    print("=" * 80)

    for book in books:
        print(book)