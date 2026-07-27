from database.db import get_connection


def insert_books(books):
    conn = get_connection()
    cursor = conn.cursor()

    # Clear existing data
    cursor.execute("TRUNCATE TABLE books RESTART IDENTITY;")

    query = """
    INSERT INTO books (title, price, rating, availability)
    VALUES (%s, %s, %s, %s)
    """

    for book in books:
        cursor.execute(
            query,
            (
                book["title"],
                book["price"],
                book["rating"],
                book["availability"],
            ),
        )

    conn.commit()

    print(f"✅ {len(books)} books inserted successfully!")

    cursor.close()
    conn.close()