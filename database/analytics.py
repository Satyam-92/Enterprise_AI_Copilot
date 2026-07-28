from database.db import get_connection


def get_total_books():
    """
    Return the total number of books.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM books;")
    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total


def get_average_price():
    """
    Return the average price of all books.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT ROUND(AVG(price), 2) FROM books;")
    average = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return average


def get_highest_priced_book():
    """
    Return the most expensive book.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, price
        FROM books
        ORDER BY price DESC
        LIMIT 1;
    """)

    book = cursor.fetchone()

    cursor.close()
    conn.close()

    return book


def get_lowest_priced_book():
    """
    Return the cheapest book.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, price
        FROM books
        ORDER BY price ASC
        LIMIT 1;
    """)

    book = cursor.fetchone()

    cursor.close()
    conn.close()

    return book


def get_books_by_rating(rating):
    """
    Return all books with the specified rating.
    Rating should be an integer (1-5).
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, price, rating
        FROM books
        WHERE rating = %s
        ORDER BY price DESC;
    """, (rating,))

    books = cursor.fetchall()

    cursor.close()
    conn.close()

    return books


def search_books(keyword):
    """
    Search books by title.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, price, rating
        FROM books
        WHERE title ILIKE %s
        ORDER BY title;
    """, (f"%{keyword}%",))

    books = cursor.fetchall()

    cursor.close()
    conn.close()

    return books