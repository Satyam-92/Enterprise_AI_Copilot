from bs4 import BeautifulSoup
from etl.pipeline import run_pipeline


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

        # Only collect the raw data
        book_list.append(book_data)

    # Run the complete ETL pipeline
    run_pipeline(book_list)

    print("ETL Pipeline executed successfully!")