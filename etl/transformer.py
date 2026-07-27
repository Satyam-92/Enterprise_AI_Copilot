def transform_book(book):
    """
    Transform a single book record into a clean format.
    """

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    transformed_book = {
        "title": book["title"],
        "price": float(
            book["price"]
            .replace("Â£", "")
            .replace("£", "")
            .strip()
        ),
        "rating": rating_map.get(book["rating"], 0),
        "availability": book["availability"]
    }

    return transformed_book