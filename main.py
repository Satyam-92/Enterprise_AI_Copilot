from scraper.scraper import fetch_page
from scraper.parser import parse_books


def main():

    html = fetch_page()

    parse_books(html)


if __name__ == "__main__":
    main()