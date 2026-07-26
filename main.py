from scraper.scraper import fetch_page


def main():
    html = fetch_page()
    print(html[:500])


if __name__ == "__main__":
    main()