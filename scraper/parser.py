import csv
import json
from bs4 import BeautifulSoup


def save_to_csv(book_list):

    with open("data/books.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["title", "price", "rating", "availability"]
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


def parse_books(html):

    soup = BeautifulSoup(html, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print(f"Total Books Found: {len(books)}\n")

    book_list = []

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating = book.find("p")["class"][1]

        availability = (
            book.find("p", class_="instock availability")
            .text
            .strip()
        )

        book_data = {
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability
        }

        book_list.append(book_data)

    save_to_csv(book_list)

    save_to_json(book_list)

    print("Books saved successfully!")