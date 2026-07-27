from database.db import get_connection


def create_books_table():
    """
    Create the books table if it doesn't already exist.
    """

    conn = get_connection()
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS books (
        id SERIAL PRIMARY KEY,
        title VARCHAR(500),
        price DECIMAL(10,2),
        rating INTEGER,
        availability VARCHAR(100)
    );
    """

    cursor.execute(create_table_query)

    conn.commit()

    print("✅ Books table created successfully!")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    create_books_table()