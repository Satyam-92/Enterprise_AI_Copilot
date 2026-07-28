import pandas as pd

from ml.preprocess import preprocess_books


def create_features():
    """
    Create features for embedding generation.
    """

    df = preprocess_books()

    # Normalize title
    df["title"] = (
        df["title"]
        .str.lower()
        .str.strip()
    )

    # Convert rating to string
    df["rating"] = df["rating"].astype(str)

    # Create one combined text column
    df["text"] = (
        "Title: " + df["title"] +
        " | Price: $" + df["price"].astype(str) +
        " | Rating: " + df["rating"] +
        " | Availability: " + df["availability"]
    )

    return df