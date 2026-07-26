from bs4 import BeautifulSoup


def parse_books(html):

    soup = BeautifulSoup(html, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print(f"Total Books Found: {len(books)}\n")

    for book in books:

        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p")["class"][1]


        print(f"Title : {title}")
        print(f"Price : {price}")
        print(f"Rating : {rating}")
        print("-" * 50)