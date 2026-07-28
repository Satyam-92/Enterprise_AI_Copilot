from scraper.scraper import fetch_page
from scraper.parser import parse_books


def run_scraper():
    """
    Execute the complete scraping workflow.
    """

    html = fetch_page()

    if html:
        parse_books(html)