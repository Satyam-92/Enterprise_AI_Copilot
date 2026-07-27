import csv
import json


def save_to_csv(book_list):

    with open("data/books.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "title",
                "price",
                "rating",
                "availability"
            ]
        )

        writer.writeheader()

        writer.writerows(book_list)


def save_to_json(book_list):

    with open("data/books.json", "w", encoding="utf-8") as file:

        json.dump(
            book_list,
            file,
            indent=4,
            ensure_ascii=False
        )