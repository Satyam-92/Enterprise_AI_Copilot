from bs4 import BeautifulSoup
from etl.loader import save_to_csv, save_to_json
from etl.transformer import transform_book


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

        # Transform the raw data
        book_data = transform_book(book_data)

        book_list.append(book_data)

    save_to_csv(book_list)

    save_to_json(book_list)

    print("Books saved successfully!")