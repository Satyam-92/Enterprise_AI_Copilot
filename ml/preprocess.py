import pandas as pd
from database.db import get_engine


def load_books():
    """
    Load books from PostgreSQL into a Pandas DataFrame.
    """

    engine = get_engine()

    query = """
    SELECT
        title,
        price,
        rating,
        availability
    FROM books;
    """

    df = pd.read_sql(query, engine)

    return df


def preprocess_books():
    """
    Perform basic preprocessing.
    """

    df = load_books()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna("Unknown")

    return df